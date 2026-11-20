#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
单进程高速同步脚本 (`scripts/sync_graph_and_packs.py`):
1. 同步 `graph/aliases.yaml`；
2. 使用 `kb.extract_card_22_rows` 单一解析器从全部实体卡 `### 2.2` 表格重建 `graph/edges.jsonl`
   （100% 单一真源，零僵尸 bootstrap 边残留，100% 保留多时段同向双边，对悬空目标 ID 显式报错）；
3. 归并候选时间线；可选 `--write-packs` 生成本地 `.gitignore` 缓存包；
4. 执行增强版 `kb.py audit-graph`。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
VENV_SITE = ROOT / ".venv" / "Lib" / "site-packages"
if VENV_SITE.exists() and str(VENV_SITE) not in sys.path:
    sys.path.insert(0, str(VENV_SITE))
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

import yaml  # noqa: E402
import kb  # noqa: E402

# 保持向后兼容导出，统一指向 kb.ID_REMAP 单一真源
ID_REMAP = kb.ID_REMAP


def main() -> int:
    parser = argparse.ArgumentParser(description="高速同步图谱边表与译名消歧表")
    parser.add_argument("--write-packs", action="store_true", help="可选：同时在本地 .gitignore 缓存目录 graph/packs/ 生成静态单卡包")
    parser.add_argument("--skip-packs", action="store_true", help="兼容旧参数（默认即不写静态 packs）")
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

    # 2. Pure single-source-of-truth rebuild of graph/edges.jsonl from card ### 2.2 tables
    edges_path = ROOT / "graph" / "edges.jsonl"
    table_edges: list[dict[str, Any]] = []
    seen_table_keys: set[tuple[str, str, str, str]] = set()
    unresolved_errors: list[str] = []

    for cid, cpath in sorted(valid_ids.items()):
        txt = cpath.read_text(encoding="utf-8")
        rows = kb.extract_card_22_rows(txt, cid, ID_REMAP)
        for r in rows:
            if r["peer_id"] not in valid_ids:
                unresolved_errors.append(f"{cid} -> {r['raw_target']}")
                continue
            edge_key = (r["source"], r["target"], r["relation"], r["period"])
            if edge_key in seen_table_keys:
                continue
            seen_table_keys.add(edge_key)
            table_edges.append(
                {
                    "source": r["source"],
                    "target": r["target"],
                    "relation": r["relation"],
                    "period": r["period"],
                    "digest": r["digest"],
                    "evidence": r["evidence"],
                }
            )

    if unresolved_errors:
        print(f"❌ 卡片 2.2 表存在 {len(unresolved_errors)} 个未解析悬空目标 ID，拒绝静默丢弃:", file=sys.stderr)
        for u in unresolved_errors:
            print(f"  - {u}", file=sys.stderr)
        return 1

    edges_path.write_text(
        "\n".join(json.dumps(e, ensure_ascii=False) for e in table_edges) + "\n",
        encoding="utf-8",
    )
    print(f"Synced graph/edges.jsonl: {len(table_edges)} live 2.2 edges (0 zombie bootstrap edges).")

    # 3. Merge timeline staging JSONLs in-process
    kb.cmd_merge_timeline(argparse.Namespace())

    # 4. Optional local cache packs
    if args.write_packs and not args.skip_packs:
        all_cards = kb.load_all_cards()
        events = kb.load_jsonl(ROOT / "timeline" / "events_ledger.jsonl")
        aliases_text = aliases_path.read_text(encoding="utf-8") if aliases_path.exists() else ""
        pack_dir = ROOT / "graph" / "packs"
        pack_dir.mkdir(parents=True, exist_ok=True)
        for cid in sorted(valid_ids.keys()):
            rendered = kb.compile_pack_markdown([cid], all_cards, table_edges, events, aliases_text, max_tl_level=2)
            (pack_dir / f"{cid}.md").write_text(rendered, encoding="utf-8")
        print(f"Compiled {len(valid_ids)} local cached 1-Hop Context Packs in graph/packs/!")

    # 5. Run enhanced audit-graph
    return kb.cmd_audit(argparse.Namespace())


if __name__ == "__main__":
    raise SystemExit(main())
