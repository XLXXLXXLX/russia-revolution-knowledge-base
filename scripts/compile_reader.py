#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
俄国革命知识库 `reader/` 独立专题读本手动编译器与质量门禁 CLI
- 严格遵循无状态全量编译（Stateless Full Recompile），绝不喂 git diff；
- 提供编译前输入预净化（剥离建库工程内务话术、展开裸实体 ID）；
- 提供正文/尾注双层比例、反机器黑话、反审计防御补丁腔与 B4 陷阱校验；
- 通过 SHA-256 快照（`reader/build_manifest.json`）静默追踪上游卡片变更（FRESH / STALE / MISSING）。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
FRAMEWORK_DIR = ROOT / "framework"
if str(FRAMEWORK_DIR) not in sys.path:
    sys.path.insert(0, str(FRAMEWORK_DIR))

from engine.kb_core import KBEngine, load_jsonl  # noqa: E402

MANIFEST_PATH = ROOT / "reader" / "book_manifest.yaml"
STATE_PATH = ROOT / "reader" / "build_manifest.json"

FORBID_SCAFFOLDING_TOKENS = [
    "[T1]",
    "[T2]",
    "[T3]",
    "CLM-",
    "PER-",
    "EVT-",
    "ORG-",
    "INS-",
    "MTG-",
    "POL-",
    "CON-",
    "DEB-",
    "SCH-",
    "RN-W",
    "DATA-0",
    "1-Hop",
    "[O.S.]",
    "[N.S.]",
    "start_ns",
    "end_ns",
    "coverage_status",
    "multi-perspective",
]

# 正文中严禁出现的“审计防御补丁腔”与建库内务痕迹（尾注中允许客观说明档案未载或口径差异，但不允许工程黑话）
BODY_DEFENSIVE_META_PATTERNS = [
    r"不能凭任务中的建议",
    r"站内实存原典",
    r"站内已核",
    r"本卷不补",
    r"本卷不沿用",
    r"编排角色：",
    r"待子代理补齐",
    r"待补核",
    r"不可反推为",
    r"不得反推为",
    r"本地\s*OCR",
    r"不另立侧车",
]

HOUSEKEEPING_LINE_PATTERNS = [
    re.compile(r"^>\s*编排角色：.*$", re.M),
    re.compile(r"[^。；\n]*不能凭任务中的建议文件名[^。；\n]*[。；]?", re.M),
    re.compile(r"[^。；\n]*站内实存原典文件名为[^。；\n]*[。；]?", re.M),
    re.compile(r"[^。；\n]*original_pages[^。；\n]*混入[^。；\n]*[。；]?", re.M),
    re.compile(r"^###\s+3\.[34]\s+.*(?:待补|缺口).*?(?=^#|\Z)", re.M | re.S),
]


def load_manifest() -> dict[str, Any]:
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_build_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {"chapters": {}}
    with open(STATE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_build_state(state: dict[str, Any]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
        f.write("\n")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()[:16]


def resolve_chapter_dependencies(cards: dict[str, dict[str, Any]], ch: dict[str, Any]) -> dict[str, str]:
    deps: dict[str, str] = {}
    for cid in ch.get("pack_cards", []):
        if cid not in cards:
            raise KeyError(f"Chapter {ch['id']} references unknown card ID: {cid}")
        rel = cards[cid]["rel_path"]
        deps[rel] = sha256_file(ROOT / rel)
    for ref in ch.get("reference_files", []):
        p = ROOT / ref
        if not p.exists():
            raise FileNotFoundError(f"Chapter {ch['id']} references missing file: {ref}")
        deps[ref] = sha256_file(p)
    return deps


def sanitize_context_for_writer(raw_text: str, id_to_title: dict[str, str]) -> str:
    cleaned = raw_text
    for pat in HOUSEKEEPING_LINE_PATTERNS:
        cleaned = pat.sub("", cleaned)

    # 将形如 **`PER-pyatakov`** 的孤立行内实体代码展开为带中文名的可读文本
    def _expand_inline_entity(m: re.Match[str]) -> str:
        eid = m.group(1)
        title = id_to_title.get(eid)
        return f"**{title}**（`{eid}`）" if title else m.group(0)

    cleaned = re.sub(r"\*\*`((?:PER|ORG|INS|EVT|MTG|POL|CON)-[a-z0-9-]+)`\*\*", _expand_inline_entity, cleaned)
    return re.sub(r"\n{3,}", "\n\n", cleaned).strip()


def build_chapter_bundle(engine: KBEngine, manifest: dict[str, Any], ch_id: str) -> str:
    chapters = {c["id"]: c for c in manifest["chapters"]}
    if ch_id not in chapters:
        raise SystemExit(f"Unknown chapter ID '{ch_id}'. Valid IDs: {', '.join(chapters)}")
    ch = chapters[ch_id]
    cards = engine.load_all_cards()
    edges = load_jsonl(ROOT / "graph" / "edges.jsonl")
    events = load_jsonl(ROOT / "timeline" / "events_ledger.jsonl")
    aliases_text = (ROOT / "graph" / "aliases.yaml").read_text(encoding="utf-8")
    id_to_title = {cid: str(c["meta"].get("title", cid)) for cid, c in cards.items()}

    pack_text = engine.compile_pack_markdown(
        ch["pack_cards"], cards, edges, events, aliases_text, max_chars=70000
    )
    pack_text = sanitize_context_for_writer(pack_text, id_to_title)

    # 提取参考文件的核心定量/分期摘要（避免超长文件撑爆上下文，保留前 14,000 字符）
    ref_blocks: list[str] = []
    for ref in ch.get("reference_files", []):
        p = ROOT / ref
        txt = p.read_text(encoding="utf-8")
        txt = sanitize_context_for_writer(txt, id_to_title)
        if len(txt) > 13500:
            txt = txt[:13500].rstrip() + "\n\n...[长卷后段略，核心史实已见上文与主卡上下文包]..."
        ref_blocks.append(f"### 参考档案 `{ref}`\n\n{txt}")

    st = manifest.get("style_targets", {})
    sec_lines = []
    for idx, s in enumerate(ch.get("section_plan", []), 1):
        sec_lines.append(f"{idx}. **`## {s['heading']}`**（目标篇幅占比 `{s['weight']}`）：{s['focus']}")

    endnote_tips = ch.get("endnote_guidance") or [
        "仅将有学术参考价值的版本异文、不同史家票数/人数统计口径边界收入章末 `## 注释与考证说明`（`[^1]`–`[^6]`），正文绝不插入审计免责话术。"
    ]
    forbid_traps = ch.get("forbid_patterns") or []

    header = [
        f"# `{ch['id']}` 无状态全量编译载荷：{ch['number']}｜{ch['title']}",
        "",
        "## 壹、章节编译铁律（执笔前必读！）",
        f"- **全章目标体量**：中文字符约 **{ch.get('target_zh_chars', 9500)} 字**（合格区间 `{st.get('min_zh_chars', 7500)}–{st.get('max_zh_chars', 12500)}` 中文字），采用**高可读性现代学术史专著散文体**（对标 Rabinowitch、Figes、Fitzpatrick、Kotkin、Carr）。",
        "- **拒绝干瘪提纲与拒绝廉价煽情**：正文原则上不使用无序/有序列表（列表行占比必须 `<= 8%`），以逻辑饱满、承转自然的学术散文段落展开（平均段长 200–360 字）；严禁无档案依据的心理/动作小说脑补，严禁“催命符”“生死线”“惊险赌局”“万劫不复”“怒火中烧”等通俗惊悚套话。",
        "- **克服“校勘细节喧宾夺主”的双层分流铁律**：",
        "  1. **静默守界（Silent Compliance）**：遇到输入材料中的口径边界警告时，在正文写作中**直接给出准确合规的表述**，严禁在正文插入括号去解释“为什么不能反推某票数”“本库未收录某异文”等防御性补丁腔！",
        "  2. **正文 / 章末尾注（`[^1]`）物理分流**：正文 100% 聚焦宏观结构矛盾、制度财政机制、人物抉择与主流学派解释交锋；版本删改层次、名册分母边界与多管道伤亡差异统一收进章末 `## 注释与考证说明`（共 `3–8` 条编号尾注 `[^1]`，尾注总字数占全章不超过 `12%`）。",
        "- **无感规范呈现与零黑话泄漏**：",
        "  - 1918 年 2 月改历前日期使用自然中文（如“1917 年俄历 10 月 25 日（公历 11 月 7 日）”，同段后续可自然简写），1918 年 2 月 14 日起苏俄本土事件直接使用公历，严禁出现 `[O.S.]`、`[N.S.]`、`[T1]/[T2]/[T3]`、`CLM-*`、`PER-*`、`DEB-*`、`1-Hop` 等任何机器代码标签！",
        "  - 正文与尾注中**禁止插入任何 Markdown 文件链接**；全章最末尾统一附一个干净的 `<details><summary>附：本章依托的核心档案与延伸阅读索引</summary>...</details>`，列出本章依据的相对路径链接（如 `[EVT-1921-kronstadt.md](../cards/events/EVT-1921-kronstadt.md)`）。",
        "",
        "## 贰、本章固定分节大纲与篇幅配额锁（Section Weight Lock）",
        f"- 章节主标题请严格写为：`# {ch['number']}｜{ch['title']}`（顶部不要写 YAML Frontmatter，让读者打开文件即见书名章题！）",
        *sec_lines,
        "- **`## 注释与考证说明`**：集中放置 `[^1]` 至 `[^6]` 学术考证尾注：",
        *[f"  - {tip}" for tip in endnote_tips],
        "- **章末折叠档案索引**：`<details><summary>附：本章依托的核心档案与延伸阅读索引</summary>...</details>`",
    ]
    if forbid_traps:
        header.append("")
        header.append("## 叁、本章严禁踩中的史实陷阱（Forbid Patterns）")
        for t in forbid_traps:
            header.append(f"- 严禁写出匹配 `{t}` 的错误论断！")

    header.extend(
        [
            "",
            "---",
            "",
            "## 肆、平铺去重 1-Hop 核心卡片上下文包（已预脱敏）",
            "",
            pack_text,
            "",
            "---",
            "",
            "## 伍、配套编年、争鸣与定量序列参考摘编",
            "",
            "\n\n---\n\n".join(ref_blocks),
            "",
        ]
    )
    return "\n".join(header)


def evaluate_chapter_markdown(
    cfg_raw: dict[str, Any], manifest: dict[str, Any], ch: dict[str, Any], md_text: str
) -> dict[str, Any]:
    st = manifest.get("style_targets", {})
    has_yaml_frontmatter = md_text.lstrip().startswith("---")

    details_pat = re.compile(r"<details>.*?</details>", flags=re.S | re.I)
    has_details = bool(details_pat.search(md_text))
    without_details = details_pat.sub("", md_text).strip()

    # 切分正文与 `## 注释与考证说明` 尾注区
    endnote_sec_pat = re.compile(r"(?m)^##\s+注释与考证说明\s*$")
    m_end = endnote_sec_pat.search(without_details)
    if m_end:
        body_prose = without_details[: m_end.start()].strip()
        endnotes_block = without_details[m_end.end() :].strip()
    else:
        body_prose = without_details
        endnotes_block = ""

    leaked_tokens = [tok for tok in FORBID_SCAFFOLDING_TOKENS if tok in without_details]
    inline_links = re.findall(r"\[[^\]]+\]\((?:file://|\.\.?/|cards/|historiography/|timeline/|data/)[^)]+\)", without_details)

    cliches = (cfg_raw.get("benchmarks", {}) or {}).get("melodrama_cliches") or []
    melodrama_hits = [c for c in cliches if c in without_details]

    defensive_hits = [pat for pat in BODY_DEFENSIVE_META_PATTERNS if re.search(pat, body_prose)]
    trap_hits = [pat for pat in (ch.get("forbid_patterns") or []) if re.search(pat, without_details)]

    missing_anchor_groups: list[list[str]] = []
    for group in ch.get("must_contain_any") or []:
        if not any(kw in without_details for kw in group):
            missing_anchor_groups.append(group)

    zh_total = len(re.findall(r"[\u4e00-\u9fff]", without_details))
    zh_body = len(re.findall(r"[\u4e00-\u9fff]", body_prose))
    zh_endnotes = len(re.findall(r"[\u4e00-\u9fff]", endnotes_block))
    endnote_share = zh_endnotes / max(zh_total, 1)

    endnote_defs = re.findall(r"(?m)^\[\^(\d+)\]:", endnotes_block or without_details)
    endnote_refs = set(re.findall(r"\[\^(\d+)\](?!:)", body_prose))
    orphan_endnotes = sorted(set(endnote_defs) - endnote_refs)
    missing_endnote_defs = sorted(endnote_refs - set(endnote_defs))

    non_empty_lines = [ln.strip() for ln in body_prose.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    bullet_lines = [ln for ln in non_empty_lines if re.match(r"^(?:[-*+]|\d+\.)\s+", ln)]
    bullet_ratio = len(bullet_lines) / max(len(non_empty_lines), 1)

    prose_paras = [
        p.strip()
        for p in re.split(r"\n\s*\n", body_prose)
        if p.strip() and not p.strip().startswith(("#", "-", "*", "1.", ">", "|"))
    ]
    zh_para_lengths = [len(re.findall(r"[\u4e00-\u9fff]", p)) for p in prose_paras]
    mean_para_zh = int(statistics.mean(zh_para_lengths)) if zh_para_lengths else 0

    h2_headings = [
        ln.strip()[3:].strip()
        for ln in body_prose.splitlines()
        if ln.strip().startswith("## ")
    ]

    score = 100.0
    issues: list[str] = []
    if has_yaml_frontmatter:
        score -= 10.0
        issues.append("顶部含有机器 YAML Frontmatter（应保持纯书稿标题开篇）")
    if leaked_tokens:
        score -= 15.0 * len(leaked_tokens)
        issues.append(f"正文/尾注泄漏工程标签: {leaked_tokens}")
    if inline_links:
        score -= 10.0 * len(inline_links)
        issues.append(f"正文/尾注含行内文件链接 ({len(inline_links)} 处)")
    if melodrama_hits:
        score -= 8.0 * len(melodrama_hits)
        issues.append(f"命中煽情套话: {melodrama_hits}")
    if defensive_hits:
        score -= 12.0 * len(defensive_hits)
        issues.append(f"正文残留审计防御补丁腔: {defensive_hits}")
    if trap_hits:
        score -= 25.0 * len(trap_hits)
        issues.append(f"命中严禁史实陷阱: {trap_hits}")
    if missing_anchor_groups:
        score -= 10.0 * len(missing_anchor_groups)
        issues.append(f"缺失必含核心史实锚点组: {missing_anchor_groups}")
    if not has_details:
        score -= 15.0
        issues.append("缺失章末 <details> 延伸阅读档案索引")

    min_zh = int(st.get("min_zh_chars", 7500))
    max_zh = int(st.get("max_zh_chars", 12500))
    if zh_total < min_zh or zh_total > max_zh:
        score -= 10.0
        issues.append(f"全章中文字数 {zh_total} 超出目标区间 [{min_zh}, {max_zh}]")

    max_bullet = float(st.get("max_bullet_line_ratio", 0.08))
    if bullet_ratio > max_bullet:
        score -= 15.0
        issues.append(f"正文列表行占比 {bullet_ratio:.1%} 超过上限 {max_bullet:.1%}")

    min_para = int(st.get("min_mean_para_chars", 170))
    max_para = int(st.get("max_mean_para_chars", 430))
    if mean_para_zh < min_para or mean_para_zh > max_para:
        score -= 8.0
        issues.append(f"平均段落中文字数 {mean_para_zh} 超出舒适阅读区间 [{min_para}, {max_para}]")

    min_en = int(st.get("min_endnotes", 3))
    max_en = int(st.get("max_endnotes", 10))
    max_en_share = float(st.get("max_endnote_char_share", 0.14))
    if len(endnote_defs) < min_en or len(endnote_defs) > max_en:
        score -= 8.0
        issues.append(f"考证尾注条数 {len(endnote_defs)} 不在目标区间 [{min_en}, {max_en}]")
    if endnote_share > max_en_share:
        score -= 12.0
        issues.append(f"考证尾注字数占比 {endnote_share:.1%} 超过上限 {max_en_share:.1%}（校勘过重）")
    if orphan_endnotes or missing_endnote_defs:
        score -= 10.0
        issues.append(f"尾注引用与定义不匹配: 未引={orphan_endnotes}, 未定义={missing_endnote_defs}")

    expected_secs = len(ch.get("section_plan") or [])
    if len(h2_headings) != expected_secs:
        score -= 8.0
        issues.append(f"正文二级小节数 {len(h2_headings)} 与大纲预设 {expected_secs} 节不符")

    score = max(0.0, round(score, 1))
    passed = score >= 92.0 and not issues
    return {
        "chapter_id": ch["id"],
        "passed": passed,
        "score": score,
        "zh_total": zh_total,
        "zh_body": zh_body,
        "zh_endnotes": zh_endnotes,
        "endnote_share": round(endnote_share, 3),
        "endnote_count": len(endnote_defs),
        "bullet_ratio": round(bullet_ratio, 3),
        "mean_para_zh": mean_para_zh,
        "sections_found": len(h2_headings),
        "issues": issues,
    }


def cmd_status(engine: KBEngine, manifest: dict[str, Any]) -> int:
    state = load_build_state()
    cards = engine.load_all_cards()
    with open(ROOT / "kb_config.yaml", "r", encoding="utf-8") as f:
        cfg_raw = yaml.safe_load(f)

    print(f"=== 《{manifest['book_title']}》编译状态总览 ===")
    print(f"{'ID':<6} | {'状态':<8} | {'中文字数':>8} | {'尾注占比':>8} | {'门禁分':>6} | {'变更依赖':>8} | 章节标题")
    print("-" * 102)
    compiled_count = 0
    total_zh = 0
    for ch in manifest["chapters"]:
        cid = ch["id"]
        fpath = ROOT / ch["file"]
        deps_now = resolve_chapter_dependencies(cards, ch)
        rec = state.get("chapters", {}).get(cid, {})
        deps_old = rec.get("dependency_hashes", {})

        if not fpath.exists():
            status = "MISSING"
            zh_str, en_str, sc_str, dirty_str = "-", "-", "-", "-"
        else:
            compiled_count += 1
            md_txt = fpath.read_text(encoding="utf-8")
            ev = evaluate_chapter_markdown(cfg_raw, manifest, ch, md_txt)
            total_zh += ev["zh_total"]
            dirty_files = [k for k, v in deps_now.items() if deps_old.get(k) != v]
            if not deps_old:
                status = "UNSTAMP"
            elif dirty_files:
                status = "STALE"
            else:
                status = "FRESH"
            zh_str = f"{ev['zh_total']:,}"
            en_str = f"{ev['endnote_share']:.1%}({ev['endnote_count']})"
            sc_str = f"{ev['score']:.0f}" + ("✅" if ev["passed"] else "⚠️")
            dirty_str = str(len(dirty_files))

        print(f"{cid:<6} | {status:<8} | {zh_str:>8} | {en_str:>8} | {sc_str:>6} | {dirty_str:>8} | {ch['number']}·{ch['title']}")
    print("-" * 102)
    print(f"已编译章节: {compiled_count}/{len(manifest['chapters'])} 章 | 累计正文字数: {total_zh:,} 中文字")
    return 0


def cmd_bundle(engine: KBEngine, manifest: dict[str, Any], args: argparse.Namespace) -> int:
    bundle_txt = build_chapter_bundle(engine, manifest, args.chapter_id)
    if args.out:
        out_p = Path(args.out)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(bundle_txt, encoding="utf-8")
        print(f"✅ 已生成 `{args.chapter_id}` 无状态预脱敏编译包 -> {out_p} ({len(bundle_txt):,} chars)")
    else:
        print(bundle_txt)
    return 0


def cmd_verify(manifest: dict[str, Any], args: argparse.Namespace) -> int:
    with open(ROOT / "kb_config.yaml", "r", encoding="utf-8") as f:
        cfg_raw = yaml.safe_load(f)
    chapters = {c["id"]: c for c in manifest["chapters"]}
    targets: list[dict[str, Any]] = []
    if args.all:
        targets = list(chapters.values())
    elif args.existing:
        targets = [c for c in chapters.values() if (ROOT / c["file"]).exists()]
    elif args.chapter_id:
        if args.chapter_id not in chapters:
            raise SystemExit(f"Unknown chapter ID: {args.chapter_id}")
        targets = [chapters[args.chapter_id]]
    else:
        raise SystemExit("Specify a chapter_id, --existing, or --all.")

    if not targets:
        print("⚠️ 当前尚无已生成的章节文件可供校验。")
        return 1

    any_fail = False
    for ch in targets:
        p = ROOT / ch["file"]
        if not p.exists():
            print(f"❌ [{ch['id']}] 文件尚未生成: {ch['file']}")
            any_fail = True
            continue
        ev = evaluate_chapter_markdown(cfg_raw, manifest, ch, p.read_text(encoding="utf-8"))
        badge = "✅ PASS" if ev["passed"] else "❌ FAIL"
        print(
            f"{badge} [{ch['id']}] 得分={ev['score']} | 总中文字={ev['zh_total']:,} "
            f"(正文={ev['zh_body']:,}, 尾注={ev['zh_endnotes']:,} [{ev['endnote_share']:.1%}, {ev['endnote_count']}条]) | "
            f"列表占比={ev['bullet_ratio']:.1%} | 均段长={ev['mean_para_zh']}字 | 小节={ev['sections_found']}"
        )
        for iss in ev["issues"]:
            print(f"   - ⚠️ {iss}")
        if not ev["passed"]:
            any_fail = True
    return 1 if any_fail else 0


def cmd_stamp(engine: KBEngine, manifest: dict[str, Any], args: argparse.Namespace) -> int:
    with open(ROOT / "kb_config.yaml", "r", encoding="utf-8") as f:
        cfg_raw = yaml.safe_load(f)
    chapters = {c["id"]: c for c in manifest["chapters"]}
    state = load_build_state()
    state.setdefault("chapters", {})

    cards = engine.load_all_cards()
    for cid in args.chapter_ids:
        if cid not in chapters:
            raise SystemExit(f"Unknown chapter ID: {cid}")
        ch = chapters[cid]
        p = ROOT / ch["file"]
        if not p.exists():
            raise SystemExit(f"Cannot stamp missing chapter file: {ch['file']}")
        ev = evaluate_chapter_markdown(cfg_raw, manifest, ch, p.read_text(encoding="utf-8"))
        if not ev["passed"]:
            raise SystemExit(f"Cannot stamp {cid}: verification failed ({ev['issues']})")
        deps = resolve_chapter_dependencies(cards, ch)
        state["chapters"][cid] = {
            "file": ch["file"],
            "stamped_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "zh_total": ev["zh_total"],
            "endnote_count": ev["endnote_count"],
            "score": ev["score"],
            "dependency_hashes": deps,
        }
        print(f"📌 已锁定 `{cid}` 上游快照指纹（共 {len(deps)} 个依赖文件，中文字数 {ev['zh_total']:,}）")

    save_build_state(state)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="俄国革命知识库 reader/ 专题读本手动编译器")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", help="查看 15 章编译状态、可读性指标与上游依赖新鲜度")

    p_bun = sub.add_parser("bundle", help="生成单章无状态、预脱敏的编译载荷包")
    p_bun.add_argument("chapter_id", help="章节 ID，如 ch09")
    p_bun.add_argument("--out", help="输出文件路径")

    p_ver = sub.add_parser("verify", help="校验已生成章节的反黑话、反补丁腔与可读性比例")
    p_ver.add_argument("chapter_id", nargs="?", help="章节 ID，如 ch09")
    p_ver.add_argument("--existing", action="store_true", help="校验所有已生成的章节")
    p_ver.add_argument("--all", action="store_true", help="校验全部 15 章（含缺失检查）")

    p_st = sub.add_parser("stamp", help="审校通过后记录当前上游卡片 SHA-256 指纹")
    p_st.add_argument("chapter_ids", nargs="+", help="要盖戳锁定的章节 ID 列表")

    args = parser.parse_args()
    engine = KBEngine(ROOT)
    manifest = load_manifest()

    if args.cmd == "status":
        return cmd_status(engine, manifest)
    if args.cmd == "bundle":
        return cmd_bundle(engine, manifest, args)
    if args.cmd == "verify":
        return cmd_verify(manifest, args)
    if args.cmd == "stamp":
        return cmd_stamp(engine, manifest, args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
