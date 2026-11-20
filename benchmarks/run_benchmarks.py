#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
俄国革命知识库（1860s–1929）统一基准评测与定期维护 CLI (`benchmarks/run_benchmarks.py`)

核心设计原则：
1. 纯只读评测：绝不修改 `cards/`、`graph/`、`historiography/`、`sources/`、`timeline/` 或 `scripts/`。
2. 反古德哈特（Anti-Goodhart）：同时测量底层结构保真度（B1）、多卡上下文压缩与零邻居丢失（B2）、
   145本史料章节定位与纯扫描空书隔离（B3）、跨家族史实/历法/分寸对抗陷阱（B4A/B4B），以及“对外讲史”模态A文风可读性（B5）。
3. 可定期维护：内置 `check-health` 自检锚点腐烂、dev/holdout 比例、审计缺陷转回归覆盖率与复习周期 SLA。

子命令：
  python benchmarks/run_benchmarks.py check-health
  python benchmarks/run_benchmarks.py run [--split all|dev|holdout] [--save-baseline <tag>]
  python benchmarks/run_benchmarks.py compare <baseline_json> <candidate_json>
  python benchmarks/run_benchmarks.py eval-prose [--prompt-id B5-PROSE-01 --answer-file path.md | --answers-dir dir/]
"""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import re
import statistics
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

BENCH_DIR = Path(__file__).resolve().parent
ROOT = BENCH_DIR.parent
SUITES_DIR = BENCH_DIR / "suites"
BASELINES_DIR = BENCH_DIR / "baselines"
RESULTS_DIR = BENCH_DIR / "results"

ID_PAT = re.compile(r"\b(?:PER|ORG|INS|EVT|MTG|POL|CON)-[A-Za-z0-9-]+\b")
DEB_PAT = re.compile(r"\bDEB-[A-Za-z0-9-]+\b")
CLM_PAT = re.compile(r"\bCLM-[A-Za-z0-9_-]+\b")
SCH_PAT = re.compile(r"\bSCH-[A-Za-z0-9_-]+\b")
DUAL_DATE_PAT = re.compile(r"(\d{4}-\d{2}-\d{2})\s*\[O\.S\.\]\s*/\s*(\d{4}-\d{2}-\d{2})\s*\[N\.S\.\]")


# ============================================================================
# 基础加载工具
# ============================================================================

def load_kb_module() -> Any:
    spec = importlib.util.spec_from_file_location("kb_mod", ROOT / "scripts" / "kb.py")
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_sync_remap() -> dict[str, str]:
    sync_path = ROOT / "scripts" / "sync_graph_and_packs.py"
    if not sync_path.exists():
        return {}
    txt = sync_path.read_text(encoding="utf-8")
    m = re.search(r"ID_REMAP\s*=\s*(\{.*?\})", txt, flags=re.S)
    if not m:
        return {}
    try:
        return json.loads(m.group(1))
    except Exception:
        return {}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for idx, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        s = raw.strip()
        if not s:
            continue
        try:
            rows.append(json.loads(s))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path.relative_to(ROOT).as_posix()}:{idx} JSON 解析失败: {exc}") from exc
    return rows


def parse_yaml_frontmatter(md_text: str) -> tuple[dict[str, Any], str]:
    text = md_text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, text
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return {}, text
    fm = yaml.safe_load(text[4:end_idx]) or {}
    body = text[end_idx + 5 :]
    return (fm if isinstance(fm, dict) else {}), body


def normalize_yaml_value(v: Any) -> Any:
    if isinstance(v, (dt.date, dt.datetime)):
        return v.isoformat()
    if isinstance(v, list):
        return [normalize_yaml_value(x) for x in v]
    if isinstance(v, dict):
        return {str(k): normalize_yaml_value(val) for k, val in v.items()}
    return v


def index_all_repo_entities() -> dict[str, dict[str, Any]]:
    entities: dict[str, dict[str, Any]] = {}
    for folder in ("cards", "historiography"):
        base = ROOT / folder
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.md")):
            if p.name.lower() == "readme.md":
                continue
            txt = p.read_text(encoding="utf-8")
            fm, body = parse_yaml_frontmatter(txt)
            cid = str(fm.get("id") or p.stem)
            entities[cid] = {
                "id": cid,
                "stem": p.stem,
                "path": p,
                "rel_path": p.relative_to(ROOT).as_posix(),
                "fm": normalize_yaml_value(fm),
                "body": body,
                "raw": txt,
            }
            if p.stem not in entities:
                entities[p.stem] = entities[cid]
    return entities


def extract_card_22_rows(card_text: str, cid: str, id_remap: dict[str, str]) -> list[dict[str, Any]]:
    """提取卡片 2.2 关系表中的所有有向边行（包含未映射/悬空目标以便检测）。"""
    rows: list[dict[str, Any]] = []
    for line in card_text.splitlines():
        s = line.strip()
        if not (s.startswith("|") and s.endswith("|")):
            continue
        cols = [c.strip() for c in s.strip("|").split("|")]
        if len(cols) < 4:
            continue
        if "---" in cols[0] or "---" in cols[1]:
            continue
        m = ID_PAT.search(cols[0])
        if not m:
            continue
        raw_target = m.group(0)
        mapped_target = id_remap.get(raw_target, raw_target)
        if mapped_target == cid:
            continue
        rel = re.sub(r"`|\*", "", cols[1]).strip() or "related-to"
        period = re.sub(r"`|\*", "", cols[2]).strip() or "1861-1929"
        digest = re.sub(r"`", "", cols[3]).strip()
        if not digest or "一句话" in digest:
            continue
        rows.append(
            {
                "source": cid,
                "raw_target": raw_target,
                "target": mapped_target,
                "relation": rel[:60],
                "period": period[:60],
                "digest": digest,
            }
        )
    return rows


# ============================================================================
# 维护自检：check-health
# ============================================================================

def cmd_check_health(args: argparse.Namespace) -> int:
    reg_path = SUITES_DIR / "registry.json"
    if not reg_path.exists():
        print(f"❌ 缺少注册表: {reg_path}", file=sys.stderr)
        return 1

    reg = load_json(reg_path)
    policy = reg.get("maintenance_policy", {})
    sla_days = int(policy.get("review_sla_days", 14))
    min_holdout = float(policy.get("min_holdout_ratio", 0.2))
    today = dt.date.fromisoformat(args.as_of) if args.as_of else dt.date(2026, 11, 19)

    entities = index_all_repo_entities()
    issues: list[str] = []
    warnings: list[str] = []
    suite_stats: list[dict[str, Any]] = []

    # 1. 检查生产脚本是否硬编码作弊 Benchmark ID
    bench_id_leak_pat = re.compile(r"\b(?:B1-(?:FM|EDGE|CAL)-\d+|B2-\d+|B3-(?:LOC|QRN)-\d+|B4[AB]-\d+|B5-PROSE-\d+)\b")
    for prod_script in (ROOT / "scripts").glob("*.py"):
        stxt = prod_script.read_text(encoding="utf-8", errors="ignore")
        leaks = bench_id_leak_pat.findall(stxt)
        if leaks:
            issues.append(f"反作弊告警: 生产脚本 `{prod_script.name}` 硬编码了 Benchmark ID: {sorted(set(leaks))}")

    audited_origins: set[str] = set()

    for sinfo in reg.get("suites", []):
        sid = sinfo["id"]
        spath = ROOT / sinfo["path"]
        if not spath.exists():
            issues.append(f"[{sid}] 套件文件不存在: `{sinfo['path']}`")
            continue

        last_rev = dt.date.fromisoformat(sinfo.get("last_reviewed", "2026-11-19"))
        age_days = (today - last_rev).days
        if age_days > sla_days:
            warnings.append(f"[{sid}] 超过定期复审周期 SLA ({age_days} 天 > {sla_days} 天)，请轮换部分 holdout 题目并更新 last_reviewed")

        items: list[dict[str, Any]] = []
        if sinfo["format"] == "json":
            doc = load_json(spath)
            if sid == "B1":
                items = (
                    doc.get("frontmatter_canary_cards", [])
                    + doc.get("multi_period_edge_canaries", [])
                    + doc.get("calendar_regression_vectors", [])
                )
            elif sid == "B2":
                items = doc.get("bundles", [])
        else:
            items = load_jsonl(spath)

        if not items:
            issues.append(f"[{sid}] 套件为空: `{sinfo['path']}`")
            continue

        seen_ids: set[str] = set()
        dev_cnt = 0
        holdout_cnt = 0
        broken_anchors = 0

        for it in items:
            iid = str(it.get("id", ""))
            if not iid:
                issues.append(f"[{sid}] 存在缺失 id 的条目")
            elif iid in seen_ids:
                issues.append(f"[{sid}] 存在重复 id: `{iid}`")
            seen_ids.add(iid)

            sp = it.get("split", "dev")
            if sp == "holdout":
                holdout_cnt += 1
            else:
                dev_cnt += 1

            origin = str(it.get("origin", ""))
            if origin.startswith("audit_regression:"):
                audited_origins.add(origin.split(":", 1)[1].strip())

            # 校验不同套件的实体与路径锚点
            for card_key in ("card_id", "source", "target"):
                if card_key in it and it[card_key] not in entities:
                    broken_anchors += 1
                    issues.append(f"[{sid}:{iid}] 锚点实体不存在: `{it[card_key]}`")
            for list_card_key in ("card_ids", "must_retain_neighbors", "must_retain_debates", "target_cards", "recommended_pack_ids"):
                for ref_id in it.get(list_card_key, []):
                    if ref_id not in entities:
                        broken_anchors += 1
                        issues.append(f"[{sid}:{iid}] 列表实体不存在 (`{list_card_key}`): `{ref_id}`")
            for path_list_key in ("expected_paths", "expected_books", "source_anchors", "reference_files"):
                for rel_p in it.get(path_list_key, []):
                    if not (ROOT / rel_p).exists():
                        broken_anchors += 1
                        issues.append(f"[{sid}:{iid}] 磁盘路径不存在 (`{path_list_key}`): `{rel_p}`")
            if "target_book_dir" in it and not (ROOT / it["target_book_dir"]).exists():
                broken_anchors += 1
                issues.append(f"[{sid}:{iid}] 目标书目录不存在: `{it['target_book_dir']}`")

            # B3 locate_chapter 额外核验 query / substring 真实性
            if sid == "B3" and it.get("kind") == "locate_chapter":
                exp_paths = it.get("expected_paths", [])
                vsub = str(it.get("verified_substring", ""))
                if exp_paths and (ROOT / exp_paths[0]).exists() and vsub:
                    ch_txt = (ROOT / exp_paths[0]).read_text(encoding="utf-8", errors="ignore")
                    if vsub not in ch_txt:
                        broken_anchors += 1
                        issues.append(f"[{sid}:{iid}] verified_substring 未在 `{exp_paths[0]}` 中命中")

        holdout_ratio = holdout_cnt / len(items)
        if holdout_ratio < min_holdout:
            warnings.append(f"[{sid}] holdout 比例偏低 ({holdout_ratio:.1%} < {min_holdout:.0%})")

        suite_stats.append(
            {
                "suite": sid,
                "total": len(items),
                "dev": dev_cnt,
                "holdout": holdout_cnt,
                "holdout_ratio": round(holdout_ratio, 3),
                "broken_anchors": broken_anchors,
                "author": sinfo.get("author", ""),
            }
        )

    # 检查近期审计报告是否已沉淀回归用例
    recent_audits = sorted((ROOT / "audits").glob("AUD-19*.md")) + sorted((ROOT / "audits").glob("AUD-20*.md"))
    uncovered_audits = []
    for ap in recent_audits:
        short_id = "-".join(ap.stem.split("-")[:2])  # e.g. AUD-20A
        if short_id not in audited_origins and ap.stem not in audited_origins:
            uncovered_audits.append(short_id)
    if uncovered_audits:
        warnings.append(
            f"近期审计报告尚未全部标注回归映射 (`origin: audit_regression:<ID>`): {', '.join(uncovered_audits)}（可在下次维护时补充 P0/P1 金丝雀）"
        )

    print("=== Benchmark 体系健康度与定期维护自检 (`check-health`) ===")
    for st in suite_stats:
        print(
            f"- [{st['suite']}] 共 {st['total']:2d} 题 (dev={st['dev']}, holdout={st['holdout']}, "
            f"holdout占比={st['holdout_ratio']:.0%}, 断锚={st['broken_anchors']}) | 作者: {st['author']}"
        )
    if warnings:
        print("\n⚠️ 维护提醒 (Warnings):")
        for w in warnings:
            print(f"  - {w}")
    if issues:
        print(f"\n❌ 发现 {len(issues)} 项基准健康硬伤:")
        for iss in issues[:30]:
            print(f"  - {iss}")
        return 1

    print("\n✅ 所有注册 Benchmark 套件 JSON 语法、实体/文献路径锚点、反硬编码隔离与 holdout 划分全部健康！")
    return 0


# ============================================================================
# Suite B1: 图谱、元数据、外键与双历法保真度评测
# ============================================================================

def eval_b1(split_filter: str, entities: dict[str, dict[str, Any]]) -> dict[str, Any]:
    doc = load_json(SUITES_DIR / "b1_graph_and_integrity_cases.json")
    kb = load_kb_module()
    id_remap = load_sync_remap()

    # 1. YAML Frontmatter 保真度对比 (kb.py 当前解析器 vs PyYAML safe_load)
    kb_cards = kb.load_all_cards()
    fm_total = 0
    fm_exact = 0
    fm_mismatches: list[str] = []
    critical_keys = ("id", "title", "type", "coverage_status", "perspectives_present", "perspectives_missing", "related_debates")

    for cid, kb_entry in sorted(kb_cards.items()):
        p = kb_entry["path"]
        yaml_fm, _ = parse_yaml_frontmatter(p.read_text(encoding="utf-8"))
        yaml_fm = normalize_yaml_value(yaml_fm)
        kb_fm = normalize_yaml_value(kb_entry["meta"])
        fm_total += 1
        mismatch_reasons = []
        for k in critical_keys:
            if k in yaml_fm and kb_fm.get(k) != yaml_fm.get(k):
                mismatch_reasons.append(f"{k}: kb={kb_fm.get(k)!r} != yaml={yaml_fm.get(k)!r}")
        # 检查所有标量/嵌套字符串是否残留未剥离的 `# ` 行尾注释
        for k, v in yaml_fm.items():
            kv = kb_fm.get(k)
            if isinstance(v, str) and isinstance(kv, str) and v != kv and "#" in kv:
                mismatch_reasons.append(f"{k}: trailing_comment_unstripped({kv!r})")
            elif isinstance(v, dict) and isinstance(kv, dict):
                for sk, sv in v.items():
                    skv = kv.get(sk)
                    if isinstance(sv, str) and isinstance(skv, str) and sv != skv:
                        mismatch_reasons.append(f"{k}.{sk}: kb={skv!r} != yaml={sv!r}")
        if not mismatch_reasons:
            fm_exact += 1
        else:
            fm_mismatches.append(f"{cid} ({'; '.join(mismatch_reasons[:2])})")

    fm_parity_rate = fm_exact / max(fm_total, 1)

    canary_fms = [x for x in doc["frontmatter_canary_cards"] if split_filter in ("all", x["split"])]
    canary_fm_pass = sum(1 for x in canary_fms if not any(m.startswith(x["card_id"] + " ") for m in fm_mismatches))

    # 2. 卡片 2.2 表与 graph/edges.jsonl 多时段同步度 & 悬空目标检测
    card_files = sorted((ROOT / "cards").rglob("*.md"))
    valid_card_ids = {p.stem for p in card_files if p.name.lower() != "readme.md"}
    edges = load_jsonl(ROOT / "graph" / "edges.jsonl")
    edges_by_pair: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for e in edges:
        edges_by_pair.setdefault((e["source"], e["target"]), []).append(e)

    table_rows_valid: list[dict[str, Any]] = []
    unresolved_targets: list[str] = []
    table_by_pair: dict[tuple[str, str], list[dict[str, Any]]] = {}

    for p in card_files:
        if p.name.lower() == "readme.md":
            continue
        cid = p.stem
        rows = extract_card_22_rows(p.read_text(encoding="utf-8"), cid, id_remap)
        for r in rows:
            if r["target"] not in valid_card_ids:
                unresolved_targets.append(f"{cid} -> {r['raw_target']}")
            else:
                table_rows_valid.append(r)
                table_by_pair.setdefault((cid, r["target"]), []).append(r)

    digest_synced = 0
    stale_or_missing_rows: list[str] = []
    for r in table_rows_valid:
        cand_edges = edges_by_pair.get((r["source"], r["target"]), [])
        if any(ce.get("digest", "").strip() == r["digest"].strip() for ce in cand_edges):
            digest_synced += 1
        else:
            stale_or_missing_rows.append(f"{r['source']} -> {r['target']} ({r['period']})")

    digest_sync_rate = digest_synced / max(len(table_rows_valid), 1)

    multi_pairs_in_cards = {pair: rlist for pair, rlist in table_by_pair.items() if len(rlist) >= 2}
    multi_pairs_retained = sum(
        1 for pair, rlist in multi_pairs_in_cards.items() if len(edges_by_pair.get(pair, [])) >= len(rlist)
    )
    multi_edge_retention_rate = (
        multi_pairs_retained / len(multi_pairs_in_cards) if multi_pairs_in_cards else 1.0
    )

    edge_canaries = [x for x in doc["multi_period_edge_canaries"] if split_filter in ("all", x["split"])]
    edge_canary_pass = 0
    for ec in edge_canaries:
        found_edges = edges_by_pair.get((ec["source"], ec["target"]), [])
        periods_joined = " | ".join(str(e.get("period", "")) for e in found_edges)
        if len(found_edges) >= ec["min_distinct_edges"] and all(
            sub in periods_joined for sub in ec.get("expected_period_substrings", [])
        ):
            edge_canary_pass += 1

    # 3. 跨集合外键完整性 (CLM -> SCH, CLM -> Card/DEB, 重复 SCH)
    sch_files = sorted((ROOT / "historiography" / "scholars").glob("SCH-*.md"))
    valid_sch_ids = {p.stem for p in sch_files}
    sch_norm_titles: dict[str, list[str]] = {}
    for sp in sch_files:
        sfm, _ = parse_yaml_frontmatter(sp.read_text(encoding="utf-8"))
        en_name = str((sfm.get("names") or {}).get("en") or sfm.get("title") or sp.stem).lower()
        en_key = re.sub(r"[^a-z\u4e00-\u9fff]+", "", en_name)
        if en_key:
            sch_norm_titles.setdefault(en_key, []).append(sp.stem)
    # 另检测姓氏+首字母高度重合的重复学者卡（如 SCH-smith-sa vs SCH-smith-stephen）
    duplicate_sch_groups: list[list[str]] = [v for v in sch_norm_titles.values() if len(v) > 1]
    if "SCH-smith-sa" in valid_sch_ids and "SCH-smith-stephen" in valid_sch_ids:
        if ["SCH-smith-sa", "SCH-smith-stephen"] not in duplicate_sch_groups:
            duplicate_sch_groups.append(["SCH-smith-sa", "SCH-smith-stephen"])

    clm_files = sorted((ROOT / "historiography" / "claims").glob("CLM-*.md"))
    clm_sch_total = 0
    clm_sch_valid = 0
    broken_clm_sch: list[str] = []
    referenced_sch: set[str] = set()

    clm_card_refs_total = 0
    clm_card_refs_valid = 0
    broken_clm_cards: list[str] = []

    for cp in clm_files:
        cfm, _ = parse_yaml_frontmatter(cp.read_text(encoding="utf-8"))
        sch_val = cfm.get("scholar") or cfm.get("scholars")
        sch_list = sch_val if isinstance(sch_val, list) else ([sch_val] if sch_val else [])
        for sv in sch_list:
            sv_s = str(sv).strip()
            clm_sch_total += 1
            if sv_s in valid_sch_ids:
                clm_sch_valid += 1
                referenced_sch.add(sv_s)
            else:
                broken_clm_sch.append(f"{cp.stem}: {sv_s}")

        for rk in ("targets_cards", "related_cards", "cards", "target_cards", "debate", "related_debates", "debates"):
            rvals = cfm.get(rk) or []
            if isinstance(rvals, str):
                rvals = [rvals]
            for rv in rvals:
                rv_s = str(rv).strip()
                if not rv_s:
                    continue
                clm_card_refs_total += 1
                if rv_s in entities:
                    clm_card_refs_valid += 1
                else:
                    broken_clm_cards.append(f"{cp.stem} ({rk}): {rv_s}")

    clm_scholar_fk_valid_rate = clm_sch_valid / max(clm_sch_total, 1)
    clm_card_fk_valid_rate = clm_card_refs_valid / max(clm_card_refs_total, 1)
    sch_reachability_rate = len(referenced_sch) / max(len(valid_sch_ids), 1)

    # 4. 双历法数学向量回归 & 1918-02-14 改历后误标双历扫描
    cal_vectors = [x for x in doc["calendar_regression_vectors"] if split_filter in ("all", x["split"])]
    cal_passed = 0
    cal_failures: list[str] = []
    for vec in cal_vectors:
        try:
            y, m, d = kb.parse_iso_date(vec["input_date"], vec["src_cal"])
            if not vec["valid"]:
                cal_failures.append(f"{vec['id']}: 非法日期未被拦截 ({vec['input_date']} {vec['src_cal']})")
                continue
            if vec["src_cal"] == "os":
                jdn = kb.julian_to_jdn(y, m, d)
                got_os = kb.fmt_ymd((y, m, d))
                got_ns = kb.fmt_ymd(kb.jdn_to_gregorian(jdn))
            else:
                jdn = kb.gregorian_to_jdn(y, m, d)
                got_ns = kb.fmt_ymd((y, m, d))
                got_os = kb.fmt_ymd(kb.jdn_to_julian(jdn))
            if got_os == vec["expected_os"] and got_ns == vec["expected_ns"]:
                cal_passed += 1
            else:
                cal_failures.append(f"{vec['id']}: got {got_os}/{got_ns}, expected {vec['expected_os']}/{vec['expected_ns']}")
        except ValueError:
            if not vec["valid"]:
                cal_passed += 1
            else:
                cal_failures.append(f"{vec['id']}: 合法日期被误判异常")

    cal_vector_pass_rate = cal_passed / max(len(cal_vectors), 1)

    whitelist_kw = doc.get("post_reform_dual_date_whitelist_keywords", [])
    post_reform_violations: list[str] = []
    math_mismatch_in_md: list[str] = []

    for md_dir in ("cards", "historiography", "timeline"):
        base = ROOT / md_dir
        if not base.exists():
            continue
        for mp in sorted(base.rglob("*.md")):
            for lineno, line in enumerate(mp.read_text(encoding="utf-8").splitlines(), start=1):
                for m in DUAL_DATE_PAT.finditer(line):
                    os_s, ns_s = m.group(1), m.group(2)
                    try:
                        oy, om, od = kb.parse_iso_date(os_s, "os")
                        ny, nm, nd = kb.parse_iso_date(ns_s, "ns")
                        if kb.julian_to_jdn(oy, om, od) != kb.gregorian_to_jdn(ny, nm, nd):
                            math_mismatch_in_md.append(f"{mp.relative_to(ROOT).as_posix()}:{lineno} ({os_s} vs {ns_s})")
                    except ValueError:
                        math_mismatch_in_md.append(f"{mp.relative_to(ROOT).as_posix()}:{lineno} (invalid {os_s}/{ns_s})")
                    if ns_s >= "1918-02-14":
                        if not any(kw in line for kw in whitelist_kw):
                            post_reform_violations.append(
                                f"{mp.relative_to(ROOT).as_posix()}:{lineno} -> `{os_s} [O.S.] / {ns_s} [N.S.]`"
                            )

    # 5. 检查 YAML 中改历后伪构 *_os 字段 & 卡片正文提示词残迹泄漏
    post_reform_yaml_os: list[str] = []
    prompt_meta_leaks: list[str] = []
    meta_leak_pat = re.compile(r"(?:任务示例所称|按本任务要求|提示词要求|待子代理补齐)")
    for folder in ("cards", "historiography/debates"):
        for mp in sorted((ROOT / folder).rglob("*.md")):
            if mp.name.lower() == "readme.md":
                continue
            raw_txt = mp.read_text(encoding="utf-8")
            fm, body = parse_yaml_frontmatter(raw_txt)
            dates_map = fm.get("dates") if isinstance(fm.get("dates"), dict) else fm
            if isinstance(dates_map, dict):
                for os_key, ns_key in (("start_os", "start_ns"), ("end_os", "end_ns"), ("birth_os", "birth_ns"), ("death_os", "death_ns")):
                    os_v = str(dates_map.get(os_key) or "").strip()
                    ns_v = str(dates_map.get(ns_key) or "").strip()
                    if os_v and re.match(r"^\d{4}-\d{2}-\d{2}$", os_v):
                        if (ns_v >= "1918-02-14" or os_v >= "1918-02-01") and not any(kw in raw_txt[:800] for kw in whitelist_kw):
                            post_reform_yaml_os.append(f"{mp.stem}.{os_key}={os_v}")
            for m_leak in meta_leak_pat.finditer(body):
                prompt_meta_leaks.append(f"{mp.stem}: `{m_leak.group(0)}`")

    th = doc["thresholds"]
    metrics = {
        "frontmatter_parity_rate": round(fm_parity_rate, 4),
        "frontmatter_mismatch_count": len(fm_mismatches),
        "frontmatter_canary_pass_rate": round(canary_fm_pass / max(len(canary_fms), 1), 4),
        "multi_period_edge_retention_rate": round(multi_edge_retention_rate, 4),
        "multi_period_edge_canary_pass_rate": round(edge_canary_pass / max(len(edge_canaries), 1), 4),
        "card_table_digest_sync_rate": round(digest_sync_rate, 4),
        "stale_or_missing_edge_rows": len(stale_or_missing_rows),
        "unresolved_table_target_count": len(unresolved_targets),
        "clm_scholar_fk_valid_rate": round(clm_scholar_fk_valid_rate, 4),
        "broken_clm_scholar_fk_count": len(broken_clm_sch),
        "clm_card_fk_valid_rate": round(clm_card_fk_valid_rate, 4),
        "broken_clm_card_fk_count": len(broken_clm_cards),
        "duplicate_scholar_count": len(duplicate_sch_groups),
        "sch_reachability_rate": round(sch_reachability_rate, 4),
        "calendar_vector_pass_rate": round(cal_vector_pass_rate, 4),
        "markdown_dual_date_math_errors": len(math_mismatch_in_md),
        "post_reform_false_dual_date_count": len(post_reform_violations),
        "post_reform_yaml_os_count": len(post_reform_yaml_os),
        "card_meta_prompt_leak_count": len(prompt_meta_leaks),
    }
    passed = (
        metrics["frontmatter_parity_rate"] >= th["frontmatter_parity_rate_min"]
        and metrics["multi_period_edge_retention_rate"] >= th["multi_period_edge_retention_rate_min"]
        and metrics["card_table_digest_sync_rate"] >= th["card_table_digest_sync_rate_min"]
        and metrics["unresolved_table_target_count"] <= th["unresolved_table_target_count_max"]
        and metrics["clm_scholar_fk_valid_rate"] >= th["clm_scholar_fk_valid_rate_min"]
        and metrics["clm_card_fk_valid_rate"] >= th["clm_card_fk_valid_rate_min"]
        and metrics["duplicate_scholar_count"] <= th["duplicate_scholar_count_max"]
        and metrics["calendar_vector_pass_rate"] >= th["calendar_vector_pass_rate_min"]
        and metrics["post_reform_false_dual_date_count"] <= th["post_reform_false_dual_date_count_max"]
        and metrics["post_reform_yaml_os_count"] <= th.get("post_reform_yaml_os_count_max", 0)
        and metrics["card_meta_prompt_leak_count"] <= th.get("card_meta_prompt_leak_count_max", 0)
        and metrics["markdown_dual_date_math_errors"] == 0
    )
    return {
        "suite": "B1",
        "passed": passed,
        "metrics": metrics,
        "samples": {
            "frontmatter_mismatches": fm_mismatches[:8],
            "stale_or_missing_edges": stale_or_missing_rows[:8],
            "unresolved_table_targets": unresolved_targets[:8],
            "broken_clm_scholar_fks": broken_clm_sch[:8],
            "broken_clm_card_fks": broken_clm_cards[:8],
            "duplicate_scholars": duplicate_sch_groups,
            "post_reform_violations": post_reform_violations,
            "post_reform_yaml_os": post_reform_yaml_os,
            "prompt_meta_leaks": prompt_meta_leaks,
        },
    }


# ============================================================================
# Suite B2: 多卡上下文预算、去重效率与零邻居丢失评测
# ============================================================================

def compile_bundle_via_kb_cli(card_ids: list[str]) -> tuple[str, str]:
    """优先尝试多卡单次编译 `kb.py pack ID1 ID2 ...`，若旧版 CLI 不支持则回退逐卡编译拼接（反映真实读取负载）。"""
    if len(card_ids) > 1:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "kb.py"), "pack", *card_ids],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=ROOT,
        )
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout, "multi_card_native"

    chunks: list[str] = []
    for cid in card_ids:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "kb.py"), "pack", cid],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=ROOT,
        )
        if proc.returncode == 0:
            chunks.append(proc.stdout)
    return "\n\n".join(chunks), "single_card_concat_fallback"


def eval_b2(split_filter: str, entities: dict[str, dict[str, Any]]) -> dict[str, Any]:
    doc = load_json(SUITES_DIR / "b2_context_budget_bundles.json")
    id_remap = load_sync_remap()
    card_files = sorted((ROOT / "cards").rglob("*.md"))
    valid_card_ids = {p.stem for p in card_files if p.name.lower() != "readme.md"}

    # 从 2.2 关系表构建真实无向一跳邻接基准图
    true_adj: dict[str, set[str]] = {cid: set() for cid in valid_card_ids}
    for p in card_files:
        if p.name.lower() == "readme.md":
            continue
        cid = p.stem
        for r in extract_card_22_rows(p.read_text(encoding="utf-8"), cid, id_remap):
            if r["target"] in valid_card_ids:
                true_adj[cid].add(r["target"])
                true_adj[r["target"]].add(cid)

    bundles = [b for b in doc["bundles"] if split_filter in ("all", b["split"])]
    bundle_details: list[dict[str, Any]] = []

    for b in bundles:
        cids = b["card_ids"]
        compiled_text, mode_used = compile_bundle_via_kb_cli(cids)
        char_len = len(compiled_text)
        budget_ok = char_len <= b["max_compiled_chars"]

        expected_1hop: set[str] = set()
        for cid in cids:
            expected_1hop |= true_adj.get(cid, set())
        expected_1hop -= set(cids)

        surfaced_ids = set(ID_PAT.findall(compiled_text))
        retained_1hop = expected_1hop & surfaced_ids
        recall_1hop = len(retained_1hop) / len(expected_1hop) if expected_1hop else 1.0
        missing_1hop = sorted(expected_1hop - surfaced_ids)

        must_nb = b.get("must_retain_neighbors", [])
        nb_hits = sum(1 for n in must_nb if n in surfaced_ids)
        canary_recall = nb_hits / len(must_nb) if must_nb else 1.0

        must_deb = b.get("must_retain_debates", [])
        surfaced_debs = set(DEB_PAT.findall(compiled_text))
        deb_recall = sum(1 for d in must_deb if d in surfaced_debs) / len(must_deb) if must_deb else 1.0

        clm_count = len(set(CLM_PAT.findall(compiled_text)))
        sch_count = len(set(SCH_PAT.findall(compiled_text)))

        bundle_details.append(
            {
                "id": b["id"],
                "mode": mode_used,
                "chars": char_len,
                "budget": b["max_compiled_chars"],
                "budget_ok": budget_ok,
                "expected_1hop_count": len(expected_1hop),
                "recall_1hop": round(recall_1hop, 4),
                "missing_1hop_sample": missing_1hop[:6],
                "peripheral_canary_recall": round(canary_recall, 4),
                "debate_recall": round(deb_recall, 4),
                "distinct_clm_refs": clm_count,
                "distinct_sch_refs": sch_count,
            }
        )

    # 检查全部实体卡 + 争鸣卡 [T1] 字数上限 (<=150 非空白字符)
    kb = load_kb_module()
    t1_checked = 0
    t1_compliant = 0
    t1_violations: list[str] = []
    for folder in ("cards", "historiography/debates"):
        for p in sorted((ROOT / folder).rglob("*.md")):
            if p.name.lower() == "readme.md":
                continue
            _, body = parse_yaml_frontmatter(p.read_text(encoding="utf-8"))
            tiers = kb.extract_tiers(body)
            t1_raw = re.sub(r"^##\s+\[T1\][^\n]*\n?", "", tiers.get("T1", "")).strip()
            nws = len(re.sub(r"\s+", "", t1_raw))
            t1_checked += 1
            if 0 < nws <= doc["thresholds"]["t1_max_non_ws_chars"]:
                t1_compliant += 1
            else:
                t1_violations.append(f"{p.stem}: {nws} chars")

    budget_pass_rate = sum(1 for x in bundle_details if x["budget_ok"]) / max(len(bundle_details), 1)
    mean_1hop_recall = statistics.mean(x["recall_1hop"] for x in bundle_details) if bundle_details else 1.0
    min_1hop_recall = min((x["recall_1hop"] for x in bundle_details), default=1.0)
    mean_canary_recall = statistics.mean(x["peripheral_canary_recall"] for x in bundle_details) if bundle_details else 1.0
    mean_chars = int(statistics.mean(x["chars"] for x in bundle_details)) if bundle_details else 0
    t1_rate = t1_compliant / max(t1_checked, 1)

    th = doc["thresholds"]
    metrics = {
        "bundle_budget_pass_rate": round(budget_pass_rate, 4),
        "mean_bundle_chars": mean_chars,
        "b2_01_hub_trio_chars": next((x["chars"] for x in bundle_details if x["id"] == "B2-01"), 0),
        "mean_one_hop_neighbor_recall": round(mean_1hop_recall, 4),
        "min_one_hop_neighbor_recall": round(min_1hop_recall, 4),
        "peripheral_canary_recall": round(mean_canary_recall, 4),
        "bundles_with_sch_surfaced_rate": round(
            sum(1 for x in bundle_details if x["distinct_sch_refs"] > 0) / max(len(bundle_details), 1), 4
        ),
        "t1_cap_compliance_rate": round(t1_rate, 4),
        "t1_violation_count": len(t1_violations),
    }
    passed = (
        metrics["bundle_budget_pass_rate"] >= th["bundle_budget_pass_rate_min"]
        and metrics["min_one_hop_neighbor_recall"] >= th["one_hop_neighbor_recall_min"]
        and metrics["peripheral_canary_recall"] >= th["peripheral_canary_recall_min"]
        and metrics["t1_cap_compliance_rate"] >= th["t1_cap_compliance_rate_min"]
    )
    return {
        "suite": "B2",
        "passed": passed,
        "metrics": metrics,
        "bundles": bundle_details,
        "t1_violations": t1_violations[:10],
    }


# ============================================================================
# Suite B3: 145本史料章节定位雷达 (locate-chapters) 与纯扫描空书隔离
# ============================================================================

def is_chapter_effectively_empty(md_text: str) -> bool:
    cleaned = re.sub(r"(?m)^#.*$", "", md_text)
    cleaned = re.sub(r"(?m)^>\s*.*$", "", cleaned)
    cleaned = re.sub(r"<!--.*?-->", "", cleaned, flags=re.S)
    cleaned = re.sub(r"_\[本页无嵌入式文本层[^\]]*\]_", "", cleaned)
    cleaned = re.sub(r"_\[No embedded text[^\]]*\]_", "", cleaned, flags=re.I)
    cleaned = re.sub(r"---\s*Page\s*\d+\s*---", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\s+", "", cleaned)
    return len(cleaned) < 40


def eval_b3(split_filter: str) -> dict[str, Any]:
    suite_path = SUITES_DIR / "b3_chapter_radar_queries.jsonl"
    if not suite_path.exists():
        return {"suite": "B3", "passed": False, "error": "Missing b3_chapter_radar_queries.jsonl", "metrics": {}}

    items = [x for x in load_jsonl(suite_path) if split_filter in ("all", x.get("split", "dev"))]
    loc_items = [x for x in items if x.get("kind") == "locate_chapter"]
    qrn_items = [x for x in items if x.get("kind") == "quarantine_empty_scan"]

    # 检测 kb.py 是否已实现 locate-chapters
    help_proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "kb.py"), "--help"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        cwd=ROOT,
    )
    has_locate_cli = "locate-chapters" in help_proc.stdout

    rr_list: list[float] = []
    hits_at_3 = 0
    hits_at_5 = 0
    latencies_ms: list[float] = []
    misses: list[str] = []

    if has_locate_cli and loc_items:
        for it in loc_items:
            q = it["query"]
            t0 = time.perf_counter()
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "kb.py"), "locate-chapters", q, "--top", "10", "--json"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                cwd=ROOT,
            )
            elapsed_ms = (time.perf_counter() - t0) * 1000.0
            latencies_ms.append(elapsed_ms)

            ranked_paths: list[str] = []
            if proc.returncode == 0 and proc.stdout.strip():
                try:
                    parsed = json.loads(proc.stdout)
                    ranked_paths = [str(r.get("path", "")).replace("\\", "/") for r in parsed]
                except json.JSONDecodeError:
                    for line in proc.stdout.splitlines():
                        m = re.search(r"(sources/[A-Za-z0-9_./-]+\.md)", line)
                        if m:
                            ranked_paths.append(m.group(1))

            exp_paths = {p.replace("\\", "/") for p in it.get("expected_paths", [])}
            exp_books = {b.replace("\\", "/").rstrip("/") for b in it.get("expected_books", [])}

            rank_found = 0
            for idx, rp in enumerate(ranked_paths, start=1):
                if rp in exp_paths or any(rp.startswith(eb + "/") for eb in exp_books):
                    rank_found = idx
                    break
            if rank_found > 0:
                rr_list.append(1.0 / rank_found)
                if rank_found <= 3:
                    hits_at_3 += 1
                if rank_found <= 5:
                    hits_at_5 += 1
            else:
                rr_list.append(0.0)
                misses.append(f"{it['id']} ({q})")
    else:
        rr_list = [0.0 for _ in loc_items]
        misses = [f"{it['id']} ({it['query']}): locate-chapters 未实现" for it in loc_items[:6]]

    # 扫描全库纯扫描无文字层空书隔离状态
    empty_books_total = 0
    empty_books_quarantined = 0
    unquarantined_books: list[str] = []

    for cat in ("monographs", "primary"):
        cat_dir = ROOT / "sources" / cat
        if not cat_dir.exists():
            continue
        for bdir in sorted(cat_dir.iterdir()):
            if not bdir.is_dir():
                continue
            ch_files = sorted(bdir.glob("ch*.md"))
            if not ch_files:
                continue
            empty_cnt = sum(1 for cf in ch_files if is_chapter_effectively_empty(cf.read_text(encoding="utf-8", errors="ignore")))
            if empty_cnt / len(ch_files) >= 0.9:
                empty_books_total += 1
                mf = bdir / "manifest.yaml"
                quarantined = False
                if mf.exists():
                    mf_data = yaml.safe_load(mf.read_text(encoding="utf-8")) or {}
                    if mf_data.get("needs_ocr") is True:
                        quarantined = True
                if quarantined:
                    empty_books_quarantined += 1
                else:
                    unquarantined_books.append(bdir.relative_to(ROOT).as_posix())

    qrn_canary_passed = 0
    for qit in qrn_items:
        bdir = ROOT / qit["target_book_dir"]
        mf = bdir / "manifest.yaml"
        if mf.exists() and (yaml.safe_load(mf.read_text(encoding="utf-8")) or {}).get("needs_ocr") is True:
            qrn_canary_passed += 1

    hit3 = hits_at_3 / max(len(loc_items), 1)
    hit5 = hits_at_5 / max(len(loc_items), 1)
    mrr = statistics.mean(rr_list) if rr_list else 0.0
    med_ms = round(statistics.median(latencies_ms), 2) if latencies_ms else None
    quarantine_rate = empty_books_quarantined / max(empty_books_total, 1)
    qrn_canary_rate = qrn_canary_passed / max(len(qrn_items), 1)

    metrics = {
        "locate_chapters_implemented": 1 if has_locate_cli else 0,
        "chapter_hit_at_3": round(hit3, 4),
        "chapter_hit_at_5": round(hit5, 4),
        "chapter_mrr": round(mrr, 4),
        "median_query_ms": med_ms if med_ms is not None else -1.0,
        "empty_scan_books_detected": empty_books_total,
        "empty_scan_quarantine_rate": round(quarantine_rate, 4),
        "quarantine_canary_pass_rate": round(qrn_canary_rate, 4),
    }
    passed = has_locate_cli and hit5 >= 0.85 and quarantine_rate >= 1.0
    return {
        "suite": "B3",
        "passed": passed,
        "metrics": metrics,
        "samples": {
            "locator_misses": misses[:8],
            "unquarantined_empty_books": unquarantined_books,
        },
    }


# ============================================================================
# Suite B4 (B4A + B4B): 对抗性史实、历法、任期与多元史学金丝雀卡片体检
# ============================================================================

def eval_b4(split_filter: str, entities: dict[str, dict[str, Any]]) -> dict[str, Any]:
    paths = [
        ("B4A", SUITES_DIR / "b4a_historiography_1861_1918.jsonl"),
        ("B4B", SUITES_DIR / "b4b_historiography_1918_1929.jsonl"),
    ]
    all_items: list[dict[str, Any]] = []
    for tag, p in paths:
        if p.exists():
            for row in load_jsonl(p):
                if split_filter in ("all", row.get("split", "dev")):
                    row["_subsuite"] = tag
                    all_items.append(row)

    if not all_items:
        return {"suite": "B4", "passed": False, "error": "Missing B4A/B4B jsonl files", "metrics": {}}

    card_clean_count = 0
    trap_hits_in_repo: list[str] = []
    pluralism_ready_count = 0

    for it in all_items:
        tcards = [entities[cid] for cid in it.get("target_cards", []) if cid in entities]
        combined_text = "\n".join(tc["raw"] for tc in tcards)

        # 检查 trap_assertions 中显式带引号或代码反引号的精确错误片段是否残留在目标卡片中
        item_trapped = False
        for trap in it.get("trap_assertions", []):
            quoted_literals = re.findall(r"`([^`]{4,80})`", trap)
            for lit in quoted_literals:
                if lit in combined_text:
                    item_trapped = True
                    trap_hits_in_repo.append(f"{it['id']}: 目标卡命中陷阱字面量 `{lit}`")
        if not item_trapped:
            card_clean_count += 1

        # 检查目标主卡是否全部达到 multi-perspective 且至少挂载 2 种视角或争鸣锚点
        cards_mp = all(
            tc["fm"].get("coverage_status") == "multi-perspective"
            for tc in tcards
            if tc["rel_path"].startswith("cards/")
        )
        if cards_mp:
            pluralism_ready_count += 1

    metrics = {
        "total_canary_cases": len(all_items),
        "b4a_count": sum(1 for x in all_items if x["_subsuite"] == "B4A"),
        "b4b_count": sum(1 for x in all_items if x["_subsuite"] == "B4B"),
        "card_literal_trap_free_rate": round(card_clean_count / len(all_items), 4),
        "target_card_multi_perspective_rate": round(pluralism_ready_count / len(all_items), 4),
    }
    passed = metrics["card_literal_trap_free_rate"] >= 1.0 and metrics["target_card_multi_perspective_rate"] >= 1.0
    return {
        "suite": "B4",
        "passed": passed,
        "metrics": metrics,
        "samples": {"repo_trap_hits": trap_hits_in_repo[:12]},
    }


# ============================================================================
# Suite B5: 模态 A “对外讲史” 上下文就绪度 & 文章反干巴/反黑话自动评分器
# ============================================================================

def eval_b5_readiness(split_filter: str) -> dict[str, Any]:
    suite_path = SUITES_DIR / "b5_mode_a_prompts.jsonl"
    if not suite_path.exists():
        return {"suite": "B5", "passed": False, "error": "Missing b5_mode_a_prompts.jsonl", "metrics": {}}

    prompts = [x for x in load_jsonl(suite_path) if split_filter in ("all", x.get("split", "dev"))]
    pack_loads: list[int] = []
    for pr in prompts:
        txt, _ = compile_bundle_via_kb_cli(pr.get("recommended_pack_ids", []))
        pack_loads.append(len(txt))

    mean_pack_chars = int(statistics.mean(pack_loads)) if pack_loads else 0
    max_pack_chars = max(pack_loads, default=0)
    over_80k = sum(1 for c in pack_loads if c > 80000)
    empty_or_broken = sum(1 for c in pack_loads if c < 1500)

    metrics = {
        "prompt_count": len(prompts),
        "mean_recommended_pack_chars": mean_pack_chars,
        "max_recommended_pack_chars": max_pack_chars,
        "prompts_exceeding_80k_pack_budget": over_80k,
        "empty_or_broken_packs": empty_or_broken,
    }
    passed = over_80k == 0 and empty_or_broken == 0 and len(prompts) > 0
    return {"suite": "B5", "passed": passed, "metrics": metrics}


def score_single_mode_a_answer(prompt_obj: dict[str, Any], answer_md: str) -> dict[str, Any]:
    """对单篇模态 A 历史回答执行 Stage-1 确定性反干巴/反脚手架泄露体检 + 生成 Stage-2 盲审载荷。"""
    details_pat = re.compile(r"<details>.*?</details>", flags=re.S | re.I)
    has_details = bool(details_pat.search(answer_md))
    body_only = details_pat.sub("", answer_md).strip()

    sc = prompt_obj.get("style_contract", {})
    forbid_tokens = sc.get(
        "forbid_scaffolding_tokens",
        ["[T1]", "[T2]", "[T3]", "CLM-", "PER-", "EVT-", "ORG-", "DEB-", "1-Hop", "[O.S.]", "[N.S.]", "start_ns", "coverage_status"],
    )
    leaked_tokens = [tok for tok in forbid_tokens if tok in body_only]
    inline_links = re.findall(r"\[[^\]]+\]\((?:file://|\.\.?/|cards/|historiography/)[^)]+\)", body_only)

    zh_chars = len(re.findall(r"[\u4e00-\u9fff]", body_only))
    min_zh = int(sc.get("min_chinese_chars", 1600))

    non_empty_lines = [ln.strip() for ln in body_only.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    bullet_lines = [ln for ln in non_empty_lines if re.match(r"^(?:[-*+]|\d+\.)\s+", ln)]
    bullet_ratio = len(bullet_lines) / max(len(non_empty_lines), 1)
    max_bullet_ratio = float(sc.get("max_bullet_line_ratio", 0.18))

    prose_paras = [
        p.strip()
        for p in re.split(r"\n\s*\n", body_only)
        if p.strip() and not p.strip().startswith(("#", "-", "*", "1.", ">", "|"))
    ]
    mean_para_chars = int(statistics.mean(len(p) for p in prose_paras)) if prose_paras else 0
    quote_marks = len(re.findall(r"[“「『]", body_only))

    anchors = prompt_obj.get("required_historical_anchors", [])
    anchor_hits = 0
    missing_anchors: list[str] = []
    for anc in anchors:
        kws = anc.get("keywords_any", [])
        if any(kw in answer_md for kw in kws):
            anchor_hits += 1
        else:
            missing_anchors.append(anc.get("concept", str(kws)))
    anchor_recall = anchor_hits / len(anchors) if anchors else 1.0

    score = 100.0
    score -= 15.0 * len(leaked_tokens)
    score -= 10.0 * len(inline_links)
    if sc.get("require_trailing_details_block", True) and not has_details:
        score -= 15.0
    if zh_chars < min_zh:
        score -= min(25.0, (min_zh - zh_chars) / max(min_zh, 1) * 30.0)
    if bullet_ratio > max_bullet_ratio:
        score -= min(25.0, (bullet_ratio - max_bullet_ratio) * 80.0)
    if mean_para_chars < 110:
        score -= 10.0
    score -= (1.0 - anchor_recall) * 30.0
    score = max(0.0, round(score, 1))

    judge_prompt = (
        f"请你作为盲审历史学期刊主编，严格依据以下标准对这篇俄国革命史回答打分（禁止看情面，重点揪出“干巴数据库腔”与史实偏颇）：\n\n"
        f"【读者原问题】\n{prompt_obj['user_prompt']}\n\n"
        f"【必须自然融入的核心史学脉络】\n"
        + "\n".join(f"- {s}" for s in prompt_obj.get("required_historiographical_schools", []))
        + "\n\n【严禁踩中的史实/分寸陷阱】\n"
        + "\n".join(f"- {t}" for t in prompt_obj.get("forbidden_factual_traps", []))
        + f"\n\n【本题专向审美与考据判据】\n{prompt_obj.get('judge_rubric_notes', '')}\n\n"
        f"请按 5 个维度各打 1–5 分（总分 25 分，>=21 分为优秀，<16 分为不合格需重写）：\n"
        f"1. 叙事可读性与历史现场感（拒绝干瘪罗列与说明书腔）\n"
        f"2. 组织/阶级/财政机制的因果穿透力\n"
        f"3. 多流派史学争鸣的无痕学术综合\n"
        f"4. 史实、双历法自然表述与情态限定词精确度\n"
        f"5. 边缘关键行动者覆盖（反枢纽大卡偏斜）\n\n"
        f"【待审文章全文】\n{answer_md}\n"
    )

    return {
        "prompt_id": prompt_obj["id"],
        "stage1_hygiene_score": score,
        "passed_stage1": score >= 85.0 and not leaked_tokens and anchor_recall >= 0.85,
        "zh_chars": zh_chars,
        "bullet_line_ratio": round(bullet_ratio, 3),
        "mean_prose_para_chars": mean_para_chars,
        "quotation_count": quote_marks,
        "has_trailing_details": has_details,
        "leaked_scaffolding_tokens": leaked_tokens,
        "inline_link_count": len(inline_links),
        "anchor_recall": round(anchor_recall, 4),
        "missing_anchors": missing_anchors,
        "stage2_blind_judge_prompt": judge_prompt,
    }


def cmd_eval_prose(args: argparse.Namespace) -> int:
    prompts = {row["id"]: row for row in load_jsonl(SUITES_DIR / "b5_mode_a_prompts.jsonl")}
    results: list[dict[str, Any]] = []

    if args.prompt_id and args.answer_file:
        if args.prompt_id not in prompts:
            print(f"未知 prompt_id: {args.prompt_id}", file=sys.stderr)
            return 1
        ans = Path(args.answer_file).read_text(encoding="utf-8")
        res = score_single_mode_a_answer(prompts[args.prompt_id], ans)
        results.append(res)
    elif args.answers_dir:
        adir = Path(args.answers_dir)
        for pid, pobj in sorted(prompts.items()):
            cand = adir / f"{pid}.md"
            if cand.exists():
                results.append(score_single_mode_a_answer(pobj, cand.read_text(encoding="utf-8")))
    else:
        print("请提供 (--prompt-id 与 --answer-file) 或 --answers-dir", file=sys.stderr)
        return 1

    for r in results:
        status = "✅ PASS" if r["passed_stage1"] else "❌ FAIL"
        print(
            f"{status} [{r['prompt_id']}] Stage-1={r['stage1_hygiene_score']}/100 | "
            f"中文字数={r['zh_chars']} | 列表占比={r['bullet_line_ratio']:.1%} | "
            f"均段长={r['mean_prose_para_chars']} | 锚点召回={r['anchor_recall']:.0%} | "
            f"黑话泄露={r['leaked_scaffolding_tokens']}"
        )
        if args.emit_judge_prompt:
            jp_out = RESULTS_DIR / f"judge_prompt_{r['prompt_id']}.txt"
            RESULTS_DIR.mkdir(parents=True, exist_ok=True)
            jp_out.write_text(r["stage2_blind_judge_prompt"], encoding="utf-8")
            print(f"  -> 已导出盲审提示词: {jp_out.relative_to(ROOT).as_posix()}")

    return 0 if all(r["passed_stage1"] for r in results) else 1


# ============================================================================
# 统一运行 (`run`) 与基线回归对比 (`compare`)
# ============================================================================

def render_markdown_report(report: dict[str, Any]) -> str:
    lines = [
        f"# 俄国革命知识库 Benchmark 评测报告 (`{report['tag']}`)",
        "",
        f"- **评测时间**: `{report['timestamp']}`",
        f"- **评测集划分 (`split`)**: `{report['split']}`",
        f"- **Git HEAD**: `{report['git_head']}` (工作区变更文件数: `{report['git_dirty_files']}`)",
        "",
        "## 一、五大套件总览记分板",
        "",
        "| 套件 | 状态 | 核心指标摘要 |",
        "| :--- | :---: | :--- |",
    ]
    s = report["suites"]
    if "B1" in s:
        m = s["B1"]["metrics"]
        lines.append(
            f"| **B1 图谱/元数据/历法保真** | {'✅ PASS' if s['B1']['passed'] else '❌ FAIL'} | "
            f"YAML保真 `{m['frontmatter_parity_rate']:.1%}` (失真 `{m['frontmatter_mismatch_count']}`) · "
            f"多时段边保留 `{m['multi_period_edge_retention_rate']:.1%}` · "
            f"2.2边同步率 `{m['card_table_digest_sync_rate']:.1%}` · "
            f"悬空目标 `{m['unresolved_table_target_count']}` · "
            f"CLM->SCH外键 `{m['clm_scholar_fk_valid_rate']:.1%}` · "
            f"改历后误标 `{m['post_reform_false_dual_date_count']}` |"
        )
    if "B2" in s:
        m = s["B2"]["metrics"]
        lines.append(
            f"| **B2 上下文预算与零盲区召回** | {'✅ PASS' if s['B2']['passed'] else '❌ FAIL'} | "
            f"预算达标率 `{m['bundle_budget_pass_rate']:.1%}` · "
            f"`B2-01`三枢纽字符数 `{m['b2_01_hub_trio_chars']:,}` · "
            f"一跳邻居最低召回 `{m['min_one_hop_neighbor_recall']:.1%}` · "
            f"边缘人物金丝雀召回 `{m['peripheral_canary_recall']:.1%}` · "
            f"T1字数合规 `{m['t1_cap_compliance_rate']:.1%}` |"
        )
    if "B3" in s and s["B3"].get("metrics"):
        m = s["B3"]["metrics"]
        lines.append(
            f"| **B3 145本章节雷达与空书隔离** | {'✅ PASS' if s['B3']['passed'] else '❌ FAIL'} | "
            f"`locate-chapters`已实现 `{bool(m['locate_chapters_implemented'])}` · "
            f"Hit@3 `{m['chapter_hit_at_3']:.1%}` · Hit@5 `{m['chapter_hit_at_5']:.1%}` · MRR `{m['chapter_mrr']:.3f}` · "
            f"纯扫描空书隔离率 `{m['empty_scan_quarantine_rate']:.1%}` (`{m['empty_scan_books_detected']}` 本检出) |"
        )
    if "B4" in s and s["B4"].get("metrics"):
        m = s["B4"]["metrics"]
        lines.append(
            f"| **B4 跨家族对抗史实金丝雀** | {'✅ PASS' if s['B4']['passed'] else '❌ FAIL'} | "
            f"总题数 `{m['total_canary_cases']}` (`B4A={m['b4a_count']}`, `B4B={m['b4b_count']}`) · "
            f"卡片字面陷阱清零率 `{m['card_literal_trap_free_rate']:.1%}` · "
            f"目标卡多元定稿率 `{m['target_card_multi_perspective_rate']:.1%}` |"
        )
    if "B5" in s and s["B5"].get("metrics"):
        m = s["B5"]["metrics"]
        lines.append(
            f"| **B5 模态A讲史散文就绪度** | {'✅ PASS' if s['B5']['passed'] else '❌ FAIL'} | "
            f"题库 `{m['prompt_count']}` 道 · 推荐包均值 `{m['mean_recommended_pack_chars']:,}` 字符 · "
            f"超 80k 字符过载题数 `{m['prompts_exceeding_80k_pack_budget']}` |"
        )

    lines.extend(["", "## 二、关键诊断样本（Top Defects Exposed by Benchmark）", ""])
    if "B1" in s:
        smp = s["B1"]["samples"]
        for k, label in (
            ("frontmatter_mismatches", "YAML 元数据解析失真样本"),
            ("unresolved_table_targets", "卡片 2.2 悬空目标 ID"),
            ("stale_or_missing_edges", "卡片 2.2 未同步至 edges.jsonl 样本"),
            ("broken_clm_scholar_fks", "CLM -> SCH 断链外键样本"),
            ("post_reform_violations", "1918-02-14 改历后误加深双历标签"),
            ("post_reform_yaml_os", "1918-02-14 改历后 YAML 伪构 *_os 字段"),
            ("prompt_meta_leaks", "卡片成品正文泄漏编纂提示词元话语"),
        ):
            vals = smp.get(k, [])
            if vals:
                lines.append(f"- **{label}** (`{len(vals)}` 条展示): {', '.join(f'`{x}`' for x in vals[:5])}")
    if "B3" in s and s["B3"].get("samples"):
        unq = s["B3"]["samples"].get("unquarantined_empty_books", [])
        if unq:
            lines.append(f"- **未隔离纯扫描空书 (`needs_ocr` 缺失, 共 {len(unq)} 本)**: {', '.join(f'`{x}`' for x in unq[:8])}")
    if "B4" in s and s["B4"].get("samples"):
        traps = s["B4"]["samples"].get("repo_trap_hits", [])
        if traps:
            lines.append(f"- **B4 卡片残留字面陷阱**: {', '.join(traps[:6])}")

    return "\n".join(lines) + "\n"


def cmd_run(args: argparse.Namespace) -> int:
    entities = index_all_repo_entities()
    selected = [x.strip().upper() for x in args.suites.split(",")] if args.suites != "all" else ["B1", "B2", "B3", "B4", "B5"]

    head_proc = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=ROOT)
    status_proc = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=ROOT)
    dirty_cnt = len([ln for ln in status_proc.stdout.splitlines() if ln.strip()])

    suites_out: dict[str, Any] = {}
    if "B1" in selected:
        suites_out["B1"] = eval_b1(args.split, entities)
    if "B2" in selected:
        suites_out["B2"] = eval_b2(args.split, entities)
    if "B3" in selected:
        suites_out["B3"] = eval_b3(args.split)
    if "B4" in selected:
        suites_out["B4"] = eval_b4(args.split, entities)
    if "B5" in selected:
        suites_out["B5"] = eval_b5_readiness(args.split)

    tag = args.save_baseline or "latest"
    report = {
        "tag": tag,
        "timestamp": dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).isoformat(timespec="seconds"),
        "split": args.split,
        "git_head": head_proc.stdout.strip() or "unknown",
        "git_dirty_files": dirty_cnt,
        "overall_passed": all(v.get("passed", False) for v in suites_out.values()),
        "suites": suites_out,
    }

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    md_report = render_markdown_report(report)
    (RESULTS_DIR / "latest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (RESULTS_DIR / "latest.md").write_text(md_report, encoding="utf-8")

    if args.save_baseline:
        BASELINES_DIR.mkdir(parents=True, exist_ok=True)
        b_json = BASELINES_DIR / f"{args.save_baseline}.json"
        b_md = BASELINES_DIR / f"{args.save_baseline}.md"
        b_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        b_md.write_text(md_report, encoding="utf-8")
        print(f"📌 已保存基线快照: {b_json.relative_to(ROOT).as_posix()} 与 {b_md.relative_to(ROOT).as_posix()}\n")

    print(md_report)
    return 0


# 指标方向定义：higher_is_better=True 表示数值上升为改进、下降为退化；False 反之
METRIC_POLARITY: dict[str, bool] = {
    "frontmatter_parity_rate": True,
    "frontmatter_mismatch_count": False,
    "multi_period_edge_retention_rate": True,
    "card_table_digest_sync_rate": True,
    "stale_or_missing_edge_rows": False,
    "unresolved_table_target_count": False,
    "clm_scholar_fk_valid_rate": True,
    "broken_clm_scholar_fk_count": False,
    "clm_card_fk_valid_rate": True,
    "duplicate_scholar_count": False,
    "post_reform_false_dual_date_count": False,
    "post_reform_yaml_os_count": False,
    "card_meta_prompt_leak_count": False,
    "markdown_dual_date_math_errors": False,
    "bundle_budget_pass_rate": True,
    "mean_bundle_chars": False,
    "b2_01_hub_trio_chars": False,
    "min_one_hop_neighbor_recall": True,
    "peripheral_canary_recall": True,
    "t1_cap_compliance_rate": True,
    "chapter_hit_at_3": True,
    "chapter_hit_at_5": True,
    "chapter_mrr": True,
    "empty_scan_quarantine_rate": True,
    "card_literal_trap_free_rate": True,
    "target_card_multi_perspective_rate": True,
    "mean_recommended_pack_chars": False,
    "prompts_exceeding_80k_pack_budget": False,
}


def cmd_compare(args: argparse.Namespace) -> int:
    base = load_json(Path(args.baseline))
    cand = load_json(Path(args.candidate))

    print(f"# Benchmark 回归对比: `{base['tag']}` -> `{cand['tag']}`\n")
    print("| 套件 | 指标 | 基线 (`Baseline`) | 当前 (`Candidate`) | 变化 (`Δ`) | 判定 |")
    print("| :--- | :--- | ---: | ---: | ---: | :---: |")

    regressions = 0
    for sid in sorted(cand.get("suites", {}).keys()):
        bm = (base.get("suites", {}).get(sid) or {}).get("metrics", {})
        cm = (cand.get("suites", {}).get(sid) or {}).get("metrics", {})
        for k, cval in cm.items():
            if k not in bm or not isinstance(cval, (int, float)) or k not in METRIC_POLARITY:
                continue
            bval = bm[k]
            delta = cval - bval
            higher_better = METRIC_POLARITY[k]
            if abs(delta) < 1e-6:
                verdict = "➖ 持平"
            elif (delta > 0 and higher_better) or (delta < 0 and not higher_better):
                verdict = "🟢 提升"
            else:
                verdict = "🔴 退化"
                regressions += 1
            print(f"| `{sid}` | `{k}` | `{bval}` | `{cval}` | `{delta:+.4g}` | {verdict} |")

    if regressions > 0:
        print(f"\n❌ 检测到 {regressions} 项指标发生退化 (REGRESSION)！")
        return 1
    print("\n✅ 零退化通过 (Zero Regressions)！")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="俄国革命知识库 Benchmark 运行与维护工具")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_health = sub.add_parser("check-health", help="校验所有套件锚点有效性、反作弊隔离与维护周期 SLA")
    p_health.add_argument("--as-of", default=None, help="指定维护检查基准日期 YYYY-MM-DD")
    p_health.set_defaults(func=cmd_check_health)

    p_run = sub.add_parser("run", help="运行只读基准评测并输出 JSON/Markdown 报告")
    p_run.add_argument("--suites", default="all", help="逗号分隔套件，如 B1,B2,B3,B4,B5 或 all")
    p_run.add_argument("--split", default="all", choices=["all", "dev", "holdout"], help="按 dev/holdout 切片评测防过拟合")
    p_run.add_argument("--save-baseline", default=None, help="将本次结果持久化保存至 benchmarks/baselines/<tag>.json")
    p_run.set_defaults(func=cmd_run)

    p_cmp = sub.add_parser("compare", help="对比两个基准快照并拦截任何指标退化")
    p_cmp.add_argument("baseline", help="基线 JSON 路径")
    p_cmp.add_argument("candidate", help="候选 JSON 路径")
    p_cmp.set_defaults(func=cmd_compare)

    p_prose = sub.add_parser("eval-prose", help="评测模态 A 对外讲史文章的可读性、黑话零泄露与史实锚点")
    p_prose.add_argument("--prompt-id", default=None, help="如 B5-PROSE-01")
    p_prose.add_argument("--answer-file", default=None, help="待评测 Markdown 回答文件")
    p_prose.add_argument("--answers-dir", default=None, help="批量评测目录（内含 B5-PROSE-XX.md）")
    p_prose.add_argument("--emit-judge-prompt", action="store_true", help="同时生成跨模型盲审打分提示词")
    p_prose.set_defaults(func=cmd_eval_prose)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
