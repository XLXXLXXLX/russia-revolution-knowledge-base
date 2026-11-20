#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
单进程高速同步脚本 (`scripts/sync_graph_and_packs.py`):
1. 同步 `graph/aliases.yaml`；
2. 从全部卡片 `### 2.2` 表格刷新并重建 `graph/edges.jsonl`（100% 保留多时段同向双边、100% 刷新审计后新摘要、对悬空目标 ID 显式报错）；
3. 归并候选时间线并单进程内存编译 `graph/packs/*.md`（耗时 ~1s，替代旧版 184 次子进程 ~48s）；
4. 执行增强版 `kb.py audit-graph`。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

import kb  # noqa: E402

ID_REMAP = {
    "ORG-bolsheviks": "ORG-bolsheviks-rcpb-vkpb",
    "ORG-left-communists": "ORG-left-communists-1918",
    "ORG-united-opposition": "ORG-left-and-united-opposition",
    "ORG-right-opposition": "ORG-right-opposition-1928",
    "MTG-1921-03-10th-party-congress": "MTG-1921-rcpb-10th-congress",
    "EVT-1918-03-03-brest-litovsk-treaty": "EVT-1918-03-brest-litovsk-treaty",
    "MTG-1903-07-rsdlp-2nd-congress": "MTG-1903-rsdlp-2nd-congress",
}

ID_PAT = re.compile(r"\b(?:PER|ORG|INS|EVT|MTG|POL|CON)-[A-Za-z0-9-]+\b")
EV_PAT = re.compile(r"\b(?:CLM|DEB|DATA|RN|MTG|EVT|POL|CON|ORG|INS|PER)-[A-Za-z0-9_-]+\b")


def main() -> int:
    parser = argparse.ArgumentParser(description="高速同步图谱边表、译名消歧表与上下文包")
    parser.add_argument("--skip-packs", action="store_true", help="仅同步 aliases 与 edges.jsonl，跳过静态 packs 写盘")
    args = parser.parse_args()

    card_files = sorted(p for p in (ROOT / "cards").rglob("*.md") if p.name.lower() != "readme.md")
    valid_ids: dict[str, Path] = {p.stem: p for p in card_files}
    print(f"Found {len(valid_ids)} entity cards in cards/**.")

    # 1. Sync graph/aliases.yaml
    aliases_path = ROOT / "graph" / "aliases.yaml"
    aliases_doc = yaml.safe_load(aliases_path.read_text(encoding="utf-8")) or {}
    entities_map = aliases_doc.get("entities", {})
    append_blocks: list[str] = []

    for cid, cpath in sorted(valid_ids.items()):
        if cid in entities_map:
            continue
        fm, _ = kb.parse_frontmatter(cpath.read_text(encoding="utf-8"))
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

    if append_blocks:
        orig_txt = aliases_path.read_text(encoding="utf-8").rstrip()
        aliases_path.write_text(orig_txt + "\n" + "\n".join(append_blocks) + "\n", encoding="utf-8")
        print(f"Added {len(append_blocks)} new entity entries to graph/aliases.yaml.")
    else:
        print("graph/aliases.yaml already contains all entity IDs.")

    # 2. Full refresh of graph/edges.jsonl from card 2.2 tables (preserving multi-period edges!)
    edges_path = ROOT / "graph" / "edges.jsonl"
    existing_edges = kb.load_jsonl(edges_path)

    table_edges: list[dict[str, Any]] = []
    seen_table_keys: set[tuple[str, str, str, str]] = set()
    overridden_directed_pairs: set[tuple[str, str]] = set()
    unresolved_errors: list[str] = []

    for cid, cpath in sorted(valid_ids.items()):
        txt = cpath.read_text(encoding="utf-8")
        for line in txt.splitlines():
            s = line.strip()
            if not (s.startswith("|") and s.endswith("|")):
                continue
            cols = [c.strip() for c in s.strip("|").split("|")]
            if len(cols) < 4:
                continue
            if "---" in cols[0] or "---" in cols[1]:
                continue
            m0 = ID_PAT.findall(cols[0])
            arrow_mode = False
            if m0:
                raw_targets = m0
                rel = re.sub(r"`|\*", "", cols[1]).strip() or "related-to"
                period = re.sub(r"`|\*", "", cols[2]).strip() or "1861-1929"
                digest = re.sub(r"`", "", cols[3]).strip()
                ev_col = cols[4] if len(cols) >= 5 else ""
                direction = "→"
            elif len(cols) >= 5 and cols[0] in ("→", "←", "↔", "->", "<-", "<->") and ID_PAT.search(cols[2]):
                arrow_mode = True
                direction = cols[0]
                rel = re.sub(r"`|\*", "", cols[1]).strip() or "related-to"
                raw_targets = ID_PAT.findall(cols[2])
                period = re.sub(r"`|\*", "", cols[3]).strip() or "1861-1929"
                digest = re.sub(r"`", "", cols[4]).strip()
                ev_col = cols[4]
            else:
                continue

            if not digest or "一句话" in digest:
                continue
            ev_list = list(dict.fromkeys(EV_PAT.findall(ev_col))) if ev_col else []

            for raw_target in raw_targets:
                target = ID_REMAP.get(raw_target, raw_target)
                if target == cid:
                    continue
                if target not in valid_ids:
                    unresolved_errors.append(f"{cid} -> {raw_target}")
                    continue
                if arrow_mode and direction in ("←", "<-"):
                    src_id, dst_id = target, cid
                else:
                    src_id, dst_id = cid, target

                edge_key = (src_id, dst_id, rel[:60], period[:60])
                if edge_key in seen_table_keys:
                    continue
                seen_table_keys.add(edge_key)
                overridden_directed_pairs.add((src_id, dst_id))
                table_edges.append(
                    {
                        "source": src_id,
                        "target": dst_id,
                        "relation": rel[:60],
                        "period": period[:60],
                        "digest": digest,
                        "evidence": ev_list[:6],
                    }
                )

    if unresolved_errors:
        print(f"❌ 卡片 2.2 表存在 {len(unresolved_errors)} 个未解析悬空目标 ID，拒绝静默丢弃:", file=sys.stderr)
        for u in unresolved_errors:
            print(f"  - {u}", file=sys.stderr)
        return 1

    # 保留仅存在于旧 edges.jsonl 中、未在对应主卡 2.2 表重定义、且两端均为合法实体卡的引导边（如 PER-osinsky 等）
    preserved_bootstrap: list[dict[str, Any]] = []
    for e in existing_edges:
        s, t = e.get("source"), e.get("target")
        if s in valid_ids and t in valid_ids and (s, t) not in overridden_directed_pairs:
            preserved_bootstrap.append(e)

    merged_edges = table_edges + preserved_bootstrap
    edges_path.write_text(
        "\n".join(json.dumps(e, ensure_ascii=False) for e in merged_edges) + "\n",
        encoding="utf-8",
    )
    print(
        f"Synced graph/edges.jsonl: {len(table_edges)} live 2.2 edges + {len(preserved_bootstrap)} bootstrap edges = {len(merged_edges)} total."
    )

    # 3. Merge timeline staging JSONLs in-process
    kb.cmd_merge_timeline(argparse.Namespace())

    # 4. Recompile static packs in-process (fast <1.5s) unless --skip-packs
    if not args.skip_packs:
        all_cards = kb.load_all_cards()
        events = kb.load_jsonl(ROOT / "timeline" / "events_ledger.jsonl")
        aliases_text = aliases_path.read_text(encoding="utf-8") if aliases_path.exists() else ""
        pack_dir = ROOT / "graph" / "packs"
        pack_dir.mkdir(parents=True, exist_ok=True)
        for cid in sorted(valid_ids.keys()):
            rendered = kb.compile_pack_markdown([cid], all_cards, merged_edges, events, aliases_text, max_tl_level=2)
            (pack_dir / f"{cid}.md").write_text(rendered, encoding="utf-8")
        print(f"Compiled all {len(valid_ids)} 1-Hop Context Packs in-process!")

    # 5. Run enhanced audit-graph
    return kb.cmd_audit(argparse.Namespace())


if __name__ == "__main__":
    raise SystemExit(main())
