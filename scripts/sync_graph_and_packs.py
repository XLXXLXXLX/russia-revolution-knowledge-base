# -*- coding: utf-8 -*-
"""Synchronize graph/aliases.yaml, graph/edges.jsonl, timeline/events_ledger.jsonl, and all 1-Hop Context Packs."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
import yaml

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent

ID_REMAP = {
    "ORG-bolsheviks": "ORG-bolsheviks-rcpb-vkpb",
    "ORG-left-communists": "ORG-left-communists-1918",
    "ORG-united-opposition": "ORG-left-and-united-opposition",
    "ORG-right-opposition": "ORG-right-opposition-1928",
    "MTG-1921-03-10th-party-congress": "MTG-1921-rcpb-10th-congress",
    "EVT-1918-03-03-brest-litovsk-treaty": "EVT-1918-03-brest-litovsk-treaty",
    "MTG-1903-07-rsdlp-2nd-congress": "MTG-1903-rsdlp-2nd-congress",
}


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, flags=re.S)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def main() -> int:
    card_files = sorted((ROOT / "cards").rglob("*.md"))
    valid_ids: dict[str, Path] = {p.stem: p for p in card_files}
    print(f"Found {len(valid_ids)} entity cards in cards/**.")

    # 1. Sync graph/aliases.yaml
    aliases_path = ROOT / "graph" / "aliases.yaml"
    aliases_doc = yaml.safe_load(aliases_path.read_text(encoding="utf-8")) or {}
    entities_map = aliases_doc.get("entities", {})
    added_aliases = []
    append_blocks = []

    for cid, cpath in sorted(valid_ids.items()):
        if cid in entities_map:
            continue
        fm = parse_frontmatter(cpath.read_text(encoding="utf-8"))
        names = fm.get("names") or {}
        zh = fm.get("title") or cid
        ru = names.get("ru") or ""
        en = names.get("en") or ""
        al = names.get("aliases") or []
        block = [
            f"\n  {cid}:",
            f"    canonical_zh: {json.dumps(str(zh), ensure_ascii=False)}",
            f"    ru: {json.dumps(str(ru), ensure_ascii=False)}",
            f"    en: {json.dumps(str(en), ensure_ascii=False)}",
            f"    aliases: {json.dumps([str(x) for x in al], ensure_ascii=False)}",
        ]
        append_blocks.append("\n".join(block))
        added_aliases.append(cid)

    if append_blocks:
        orig_txt = aliases_path.read_text(encoding="utf-8").rstrip()
        aliases_path.write_text(orig_txt + "\n" + "\n".join(append_blocks) + "\n", encoding="utf-8")
        print(f"Added {len(added_aliases)} new entity entries to graph/aliases.yaml.")
    else:
        print("graph/aliases.yaml already contains all entity IDs.")

    # 2. Extract typed edges from card 2.2 Markdown tables -> graph/edges.jsonl
    edges_path = ROOT / "graph" / "edges.jsonl"
    existing_edges = [
        json.loads(line)
        for line in edges_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    seen_pairs = {(e["source"], e["target"], e["relation"]) for e in existing_edges}
    seen_undirected_Check = {(e["source"], e["target"]) for e in existing_edges}
    new_edges = []

    id_pat = re.compile(r"\b(?:PER|ORG|INS|EVT|MTG|POL|CON)-[A-Za-z0-9-]+\b")
    ev_pat = re.compile(r"\b(?:CLM|DEB|DATA|RN|MTG|EVT|POL|CON|ORG|INS|PER)-[A-Za-z0-9_-]+\b")

    for cid, cpath in sorted(valid_ids.items()):
        txt = cpath.read_text(encoding="utf-8")
        for line in txt.splitlines():
            s = line.strip()
            if not (s.startswith("|") and s.endswith("|")):
                continue
            cols = [c.strip() for c in s.strip("|").split("|")]
            if len(cols) < 4:
                continue
            # First col must contain a target entity ID
            m = id_pat.search(cols[0])
            if not m:
                continue
            raw_target = m.group(0)
            target = ID_REMAP.get(raw_target, raw_target)
            if target == cid or target not in valid_ids:
                continue
            rel = re.sub(r"`|\*", "", cols[1]).strip() or "related-to"
            period = re.sub(r"`|\*", "", cols[2]).strip() or "1861-1929"
            digest = re.sub(r"`", "", cols[3]).strip()
            if not digest or "一句话" in digest or "---" in rel:
                continue
            ev_list = []
            if len(cols) >= 5:
                ev_list = list(dict.fromkeys(ev_pat.findall(cols[4])))
            key = (cid, target, rel)
            if key in seen_pairs or (cid, target) in seen_undirected_Check:
                continue
            seen_pairs.add(key)
            seen_undirected_Check.add((cid, target))
            new_edges.append(
                {
                    "source": cid,
                    "target": target,
                    "relation": rel[:60],
                    "period": period[:60],
                    "digest": digest,
                    "evidence": ev_list[:6],
                }
            )

    if new_edges:
        all_edges = existing_edges + new_edges
        edges_path.write_text(
            "\n".join(json.dumps(e, ensure_ascii=False) for e in all_edges) + "\n",
            encoding="utf-8",
        )
        print(f"Added {len(new_edges)} verified edges -> total {len(all_edges)} edges in graph/edges.jsonl.")
    else:
        print(f"No new edges added (total {len(existing_edges)}).")

    # 3. Merge timeline staging JSONLs
    subprocess.run([sys.executable, str(ROOT / "scripts" / "kb.py"), "merge-timeline"], check=True)

    # 4. Recompile all 1-Hop Context Packs
    for idx, cid in enumerate(sorted(valid_ids.keys()), start=1):
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "kb.py"), "pack", cid, "--write"],
            check=True,
            stdout=subprocess.DEVNULL,
        )
    print(f"Compiled all {len(valid_ids)} 1-Hop Context Packs in graph/packs/!")

    # 5. Run full audit-graph
    subprocess.run([sys.executable, str(ROOT / "scripts" / "kb.py"), "audit-graph"], check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
