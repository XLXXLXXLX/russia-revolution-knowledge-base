#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
俄国革命知识库（1860s–1929）核心辅助工具 CLI

支持子命令:
  1. date             俄历 (O.S., 儒略历) 与公历 (N.S., 格里高利历) 精确双向换算
  2. toc              生成文献章节与标题行号索引 (供 close-reader 无 grep 整章顺读)
  3. timeline         按时间窗、层级 (L0-L3)、时代或实体切片查询双历法时间线
  4. pack             编译单卡或多卡去重 1-Hop 平衡上下文包 (零邻居截断 + 紧凑预算 + CLM/SCH 穿透)
  5. locate-chapters  基于本地 SQLite FTS5 (trigram) 的 145 本史料章节定位雷达 (仅返回章节坐标，不泄片段，自动隔离纯扫描空书)
  6. audit-graph      全库结构、外键、2.2悬空目标、[T1]字数与双历法一致性体检
  7. models           查看各 Agent 绑定的跨 Provider 模型池
  8. delegate-prompt  生成精简无路由冗余的跨 Provider T3 delegate_task 标准载荷
  9. scan-inbox       扫描 inbox/ 生成轻量级 Git 追踪元数据清单
  10. merge-timeline  归并候选事件 JSONL 进入主 events_ledger.jsonl
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / ".cache"
FTS_DB_PATH = CACHE_DIR / "kb_chapters.sqlite"

ENTITY_ID_PAT = re.compile(r"\b(?:PER|ORG|INS|EVT|MTG|POL|CON)-[A-Za-z0-9-]+\b")
CLM_ID_PAT = re.compile(r"\bCLM-[A-Za-z0-9_-]+\b")
DEB_ID_PAT = re.compile(r"\bDEB-[A-Za-z0-9-]+\b")
DUAL_DATE_PAT = re.compile(r"(\d{4}-\d{2}-\d{2})\s*\[O\.S\.\]\s*/\s*(\d{4}-\d{2}-\d{2})\s*\[N\.S\.\]")

POST_REFORM_WHITELIST = (
    "白军",
    "白卫",
    "邓尼金",
    "弗兰格尔",
    "高尔察克",
    "东正教",
    "牧首",
    "流亡",
    "侨民",
    "旧历习惯",
    "顿河",
    "南俄",
    "错误配对",
    "不得沿用",
    "不沿用",
    "误作",
    "误写",
)


# ============================================================================
# 1. 儒略历 (O.S.) <-> 格里高利历 (N.S.) 精确换算 (基于儒略日 JDN 整数算法)
# ============================================================================

def is_leap_julian(y: int) -> bool:
    return y % 4 == 0


def is_leap_gregorian(y: int) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def validate_ymd(y: int, m: int, d: int, calendar: str) -> None:
    if not (1 <= m <= 12):
        raise ValueError(f"非法月份: {m}")
    leap = is_leap_julian(y) if calendar == "os" else is_leap_gregorian(y)
    dim = [0, 31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m]
    if not (1 <= d <= dim):
        raise ValueError(f"{calendar.upper()} 历法下不存在该日期: {y:04d}-{m:02d}-{d:02d}")


def parse_iso_date(text: str, calendar: str) -> tuple[int, int, int]:
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", text.strip())
    if not m:
        raise ValueError(f"日期格式须为 YYYY-MM-DD，收到: {text}")
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    validate_ymd(y, mo, d, calendar)
    return y, mo, d


def julian_to_jdn(y: int, m: int, d: int) -> int:
    a = (14 - m) // 12
    y2 = y + 4800 - a
    m2 = m + 12 * a - 3
    return d + (153 * m2 + 2) // 5 + 365 * y2 + y2 // 4 - 32083


def gregorian_to_jdn(y: int, m: int, d: int) -> int:
    a = (14 - m) // 12
    y2 = y + 4800 - a
    m2 = m + 12 * a - 3
    return d + (153 * m2 + 2) // 5 + 365 * y2 + y2 // 4 - y2 // 100 + y2 // 400 - 32045


def jdn_to_julian(jdn: int) -> tuple[int, int, int]:
    c = jdn + 32082
    d_ = (4 * c + 3) // 1461
    e = c - (1461 * d_) // 4
    m_ = (5 * e + 2) // 153
    day = e - (153 * m_ + 2) // 5 + 1
    month = m_ + 3 - 12 * (m_ // 10)
    year = d_ - 4800 + m_ // 10
    return year, month, day


def jdn_to_gregorian(jdn: int) -> tuple[int, int, int]:
    a = jdn + 32044
    b = (4 * a + 3) // 146097
    c = a - (146097 * b) // 4
    d_ = (4 * c + 3) // 1461
    e = c - (1461 * d_) // 4
    m_ = (5 * e + 2) // 153
    day = e - (153 * m_ + 2) // 5 + 1
    month = m_ + 3 - 12 * (m_ // 10)
    year = 100 * b + d_ - 4800 + m_ // 10
    return year, month, day


def fmt_ymd(ymd: tuple[int, int, int]) -> str:
    return f"{ymd[0]:04d}-{ymd[1]:02d}-{ymd[2]:02d}"


def cmd_date(args: argparse.Namespace) -> int:
    src_cal = args.src.lower()
    y, m, d = parse_iso_date(args.date_str, src_cal)
    if src_cal == "os":
        jdn = julian_to_jdn(y, m, d)
        os_str = fmt_ymd((y, m, d))
        ns_str = fmt_ymd(jdn_to_gregorian(jdn))
    else:
        jdn = gregorian_to_jdn(y, m, d)
        ns_str = fmt_ymd((y, m, d))
        os_str = fmt_ymd(jdn_to_julian(jdn))

    reform_jdn = gregorian_to_jdn(1918, 2, 14)
    oy, om, od = parse_iso_date(os_str, "os")
    offset = 13 if (oy == 1900 and om == 2 and od == 29) else (jdn - gregorian_to_jdn(oy, om, od))
    if jdn >= reform_jdn:
        note = "注意：苏俄已于 1918-02-14 [N.S.] 正式改行公历，此后国内官方文献通常直接使用公历（白卫军控制区及东正教会除外）。"
    else:
        note = f"苏俄改历前日期（该日俄历与公历相差 {offset} 天）"

    print(f"- 俄历 (Old Style / 儒略历): {os_str}")
    print(f"- 公历 (New Style / 格里高利历): {ns_str}")
    print(f"- 标准叙事写法: {os_str} [O.S.] / {ns_str} [N.S.]")
    print(f"- 历法说明: {note}")
    return 0


# ============================================================================
# 2. 结构化 TOC 行号生成器 (供 close-reader 无 grep 整段顺读)
# ============================================================================

def cmd_toc(args: argparse.Namespace) -> int:
    target = Path(args.path)
    if not target.is_absolute():
        target = ROOT / target
    if not target.exists():
        print(f"错误: 文件不存在 {target}", file=sys.stderr)
        return 1

    lines = target.read_text(encoding="utf-8").splitlines()
    total = len(lines)
    headings: list[tuple[int, int, str]] = []
    in_fence = False

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            headings.append((idx, len(m.group(1)), m.group(2)))

    rel = target.relative_to(ROOT) if target.is_relative_to(ROOT) else target
    print(f"# 结构化目录索引: `{rel.as_posix()}` (总行数: {total})\n")
    if not headings:
        print(f"- 全文无 Markdown 标题，可直接用 `read` 读取第 `1`–`{total}` 行。")
        return 0

    print("| 层级 | 标题 | 起始行 (`offset`) | 结束行 | 段落行数 (`limit`) |")
    print("| :--- | :--- | ---: | ---: | ---: |")
    for i, (start_line, level, title) in enumerate(headings):
        end_line = total
        for next_line, next_level, _ in headings[i + 1 :]:
            if next_level <= level:
                end_line = next_line - 1
                break
        span = end_line - start_line + 1
        indent = "　" * (level - 1)
        print(f"| H{level} | {indent}{title} | `{start_line}` | `{end_line}` | `{span}` |")
    return 0


# ============================================================================
# 卡片与台账加载辅助函数 (基于 PyYAML safe_load 100% 保真)
# ============================================================================

def _normalize_yaml_types(val: Any) -> Any:
    if isinstance(val, (dt.date, dt.datetime)):
        return val.isoformat()
    if isinstance(val, list):
        return [_normalize_yaml_types(x) for x in val]
    if isinstance(val, dict):
        return {str(k): _normalize_yaml_types(v) for k, v in val.items()}
    return val


def parse_frontmatter(md_text: str) -> tuple[dict[str, Any], str]:
    """使用 PyYAML 标准解析器读取 YAML Frontmatter 与正文，彻底消除多行列表与行尾注释失真。"""
    md_text = md_text.replace("\r\n", "\n")
    if not md_text.startswith("---\n"):
        return {}, md_text
    end_idx = md_text.find("\n---\n", 4)
    if end_idx == -1:
        return {}, md_text
    fm_block = md_text[4:end_idx]
    body = md_text[end_idx + 5 :]
    loaded = yaml.safe_load(fm_block) or {}
    if not isinstance(loaded, dict):
        return {}, body
    return _normalize_yaml_types(loaded), body


# 保留同名别名以兼容外部只读调用
parse_simple_frontmatter = parse_frontmatter


def extract_tiers(body: str) -> dict[str, str]:
    """提取卡片中的 [T1], [T2], [T3] 分层文本。"""
    tiers: dict[str, list[str]] = {}
    current: str | None = None
    for line in body.splitlines():
        m = re.match(r"^##\s+\[(T[123])\]", line.strip())
        if m:
            current = m.group(1)
            tiers[current] = [line]
        elif current:
            tiers[current].append(line)
    return {k: "\n".join(v).strip() for k, v in tiers.items()}


def load_all_cards() -> dict[str, dict[str, Any]]:
    cards: dict[str, dict[str, Any]] = {}
    search_dirs = [ROOT / "cards", ROOT / "historiography"]
    for base in search_dirs:
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.md")):
            if p.name.lower() == "readme.md":
                continue
            text = p.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)
            cid = str(meta.get("id") or p.stem)
            entry = {
                "id": cid,
                "stem": p.stem,
                "path": p,
                "rel_path": p.relative_to(ROOT).as_posix(),
                "meta": meta,
                "body": body,
                "tiers": extract_tiers(body),
            }
            cards[cid] = entry
            if p.stem not in cards:
                cards[p.stem] = entry
    return cards


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    items: list[dict[str, Any]] = []
    for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        s = line.strip()
        if not s:
            continue
        try:
            items.append(json.loads(s))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path.name} 第 {idx} 行 JSON 解析失败: {exc}") from exc
    return items


# ============================================================================
# 3. 多尺度时间线切片查询
# ============================================================================

def cmd_timeline(args: argparse.Namespace) -> int:
    events = load_jsonl(ROOT / "timeline" / "events_ledger.jsonl")
    filtered = []
    for ev in events:
        if ev.get("level", 99) > args.max_level:
            continue
        d_ns = ev.get("date_ns", "")
        if args.date_from and d_ns < args.date_from:
            continue
        if args.date_to and d_ns > args.date_to:
            continue
        if args.era and ev.get("era") != args.era:
            continue
        if args.entity:
            refs = set(ev.get("actors", []) + ev.get("cards", []) + ev.get("debates", []))
            if args.entity not in refs:
                continue
        filtered.append(ev)

    filtered.sort(key=lambda x: (x.get("date_ns", ""), x.get("time_of_day") or "", x.get("id", "")))
    print(f"# 时间线查询结果 (共 {len(filtered)} 条, max_level=L{args.max_level})\n")
    for ev in filtered:
        d_ns = ev.get("date_ns")
        d_os = ev.get("date_os")
        date_disp = f"{d_os} [O.S.] / {d_ns} [N.S.]" if d_os else f"{d_ns} [N.S.]"
        lvl = ev.get("level")
        era = ev.get("era", "")
        print(f"- **[L{lvl} | {era}] {date_disp}** — **{ev.get('title')}** (`{ev.get('id')}`)")
        print(f"  {ev.get('summary')}")
    return 0


# ============================================================================
# 4. 单卡与多卡去重 1-Hop 防偏斜上下文包编译器 (pack)
# ============================================================================

def compile_pack_markdown(
    card_ids: list[str],
    cards: dict[str, dict[str, Any]],
    edges: list[dict[str, Any]],
    events: list[dict[str, Any]],
    aliases_text: str,
    max_tl_level: int = 2,
) -> str:
    primary_set = set(card_ids)
    related_edges = [
        e for e in edges if e.get("source") in primary_set or e.get("target") in primary_set
    ]

    neighbor_ids: list[str] = []
    for e in related_edges:
        for endpoint in (e.get("source"), e.get("target")):
            if endpoint and endpoint not in primary_set and endpoint not in neighbor_ids:
                neighbor_ids.append(endpoint)

    header_label = " + ".join(f"`{cid}`" for cid in card_ids)
    out: list[str] = [
        f"# 1-Hop 去重平衡上下文包：{header_label}",
        "",
        "> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。",
        "",
        "## 0. 认知完备度与反偏斜仪表盘",
    ]

    for cid in card_ids:
        c = cards[cid]
        meta = c["meta"]
        cov = meta.get("coverage_status", "unknown")
        p_present = meta.get("perspectives_present") or []
        p_missing = meta.get("perspectives_missing") or []
        if isinstance(p_present, str):
            p_present = [p_present]
        if isinstance(p_missing, str):
            p_missing = [p_missing]
        path_part = f" | `{c['rel_path']}`" if len(card_ids) <= 3 else ""
        out.append(
            f"- **`{cid}`** ({meta.get('title', '')}{path_part} | `{cov}`): "
            f"已覆盖=`{', '.join(p_present) if p_present else '未标注'}`；"
            f"待补=`{', '.join(p_missing) if p_missing else '无'}`"
        )
        if cov in ("stub", "draft"):
            out.append(f"  - ⚠️ 主卡 `{cid}` 当前完备度为 `{cov}`，尚未达到多源交叉核实定稿状态。")
        if len(p_present) < 2 and not cid.startswith("DEB-"):
            out.append(f"  - ⚠️ 主卡 `{cid}` 当前仅显式标注 {len(p_present)} 种视角，注意防范单一叙事偏斜。")

    missing_neighbors = [nid for nid in neighbor_ids if nid not in cards]
    if missing_neighbors:
        out.append(f"- ⚠️ 一跳邻域中存在尚未建卡节点 ({len(missing_neighbors)} 个): `{', '.join(missing_neighbors)}`")
    out.append("")

    # 1. 主卡核心层 ([T1] + [T2])
    rel_md_link_pat = re.compile(
        r"\[([^\]]+)\]\((?:\.\.?/|cards/|historiography/|reading-notes/|sources/|timeline/|glossary/)[^)]+\)"
    )
    any_id_pat = re.compile(r"\b(?:PER|ORG|EVT|MTG|POL|CON|LOC|DOC|WORK|DEB|CLM|SCH|RN)-[A-Za-z0-9_-]+\b")
    sec23_pat = re.compile(r"(?ms)^###\s+2\.3\b.*$")
    pipe_pad_pat = re.compile(r"[ \t]*\|[ \t]*")

    out.append("## 1. 主卡核心层 ([T1] + [T2])")
    for cid in card_ids:
        c = cards[cid]
        meta = c["meta"]
        tiers = c["tiers"]
        t1_block = tiers.get("T1", "_缺失 [T1]_")
        t2_block = tiers.get("T2", "_缺失 [T2]_")
        if len(card_ids) > 1:
            out.append(f"### 主卡 `{cid}`：{meta.get('title', '')}")
            t1_block = rel_md_link_pat.sub(r"\1", t1_block)
            t2_block = rel_md_link_pat.sub(r"\1", t2_block)
            if len(card_ids) >= 5:
                # 压缩表格多余空格，并将与第 3 节重复的 2.3 争鸣叙述折叠为保留全部实体/论断 ID 的紧凑索引行
                t2_lines = [
                    pipe_pad_pat.sub(" | ", ln).strip() if ln.lstrip().startswith("|") else ln
                    for ln in t2_block.splitlines()
                ]
                t2_block = "\n".join(t2_lines)
                m23 = sec23_pat.search(t2_block)
                if m23:
                    kept_ids = list(dict.fromkeys(any_id_pat.findall(m23.group(0))))
                    id_str = " ".join(f"`{kid}`" for kid in kept_ids) if kept_ids else "见下节"
                    t2_block = t2_block[: m23.start()].rstrip() + f"\n\n### 2.3 关联史学争鸣（已去重归并至第 3 节）\n- 关联锚点：{id_str}"
        out.append(t1_block)
        out.append("")
        out.append(t2_block)
        out.append("")

    # 2. 全量一跳邻域紧凑微摘要目录 (100% 保留全部邻居 [T1] 与时效多边，消除主卡出边自重复)
    out.append(f"## 2. 一跳邻域全量微摘要目录 (去重后共 {len(neighbor_ids)} 个节点，0 截断)")
    if not neighbor_ids:
        out.append("- _当前 `graph/edges.jsonl` 中尚无关联边。_")

    nb_total = len(neighbor_ids)
    primary_with_t2_edges = {
        cid for cid in card_ids if "2.2" in cards[cid]["tiers"].get("T2", "") and "|" in cards[cid]["tiers"].get("T2", "")
    }
    for nid in neighbor_ids:
        n_edges = [e for e in related_edges if e.get("source") == nid or e.get("target") == nid]
        edge_parts: list[str] = []
        seen_struct_tags: set[str] = set()
        for e in n_edges:
            s, t = e.get("source"), e.get("target")
            rel = e.get("relation", "")
            per = e.get("period", "")
            dig = str(e.get("digest", "")).strip()
            if s in primary_with_t2_edges and t == nid:
                if nb_total > 95 and len(card_ids) >= 5:
                    tag = f"`←{s}`[{rel}]"
                elif nb_total > 25:
                    tag = f"`←{s}`[{rel}|{per}]"
                else:
                    dig_disp = dig[:44] + "…" if len(dig) > 46 else dig
                    tag = f"`←{s}`[{rel}|{per}]: {dig_disp}"
            elif s == nid:
                if nb_total > 95 and len(card_ids) >= 5:
                    tag = f"`→{t}`[{rel}]"
                elif nb_total > 75:
                    tag = f"`→{t}`[{rel}|{per}]"
                elif nb_total > 25:
                    dig_disp = dig[:38] + "…" if len(dig) > 40 else dig
                    tag = f"`→{t}`[{rel}|{per}]: {dig_disp}"
                else:
                    tag = f"`→{t}`[{rel}|{per}]: {dig}"
            else:
                dig_disp = dig[:40] + "…" if len(dig) > 42 else dig
                tag = f"`{s}->{t}`[{rel}|{per}]: {dig_disp}"
            if tag not in seen_struct_tags:
                seen_struct_tags.add(tag)
                edge_parts.append(tag)

        if nid in cards:
            ncard = cards[nid]
            nmeta = ncard["meta"]
            ntitle = nmeta.get("title", "")
            nt1 = re.sub(r"^##\s+\[T1\][^\n]*\n?", "", ncard["tiers"].get("T1", "")).strip()
            nt1_one_line = rel_md_link_pat.sub(r"\1", re.sub(r"\s+", " ", nt1))
            out.append(
                f"- **`{nid}`**（{ntitle}）: {nt1_one_line} ‖ {' ； '.join(edge_parts)}"
            )
        else:
            in_alias = "已登记译名表" if nid in aliases_text else "未登记译名表"
            out.append(f"- **`{nid}`** `[待建卡 Stub | {in_alias}]` ‖ {' ； '.join(edge_parts)}")
    out.append("")

    # 3. 去重关联史学争鸣光谱 + CLM/SCH 学者学派穿透索引（若 DEB 已在主卡层完整展开则不再重复打印）
    debate_ids: list[str] = []
    referenced_clms: list[str] = []

    for cid in card_ids:
        c = cards[cid]
        for did in c["meta"].get("related_debates") or []:
            if did not in debate_ids and did not in primary_set:
                debate_ids.append(did)
        for did in DEB_ID_PAT.findall(c["body"]):
            if did not in debate_ids and did not in primary_set:
                debate_ids.append(did)
        for clm_id in (c["meta"].get("core_claims") or []) + CLM_ID_PAT.findall(c["body"]):
            if clm_id not in referenced_clms:
                referenced_clms.append(clm_id)

    for e in related_edges:
        for ev_ref in e.get("evidence") or []:
            ev_s = str(ev_ref)
            if ev_s.startswith("DEB-") and ev_s not in debate_ids and ev_s not in primary_set:
                debate_ids.append(ev_s)
            elif ev_s.startswith("CLM-") and ev_s not in referenced_clms:
                referenced_clms.append(ev_s)

    out.append(f"## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 {len(debate_ids)} 项)")
    if not debate_ids:
        out.append("- _相关争鸣已在第 1 节主卡展开，或暂无额外挂载的 `DEB-*` 母题卡。_")

    compact_debates = len(debate_ids) > 2 or len(card_ids) > 1
    for did in debate_ids:
        if did in cards:
            dcard = cards[did]
            dmeta = dcard["meta"]
            dt1 = re.sub(r"^##\s+\[T1\][^\n]*\n?", "", dcard["tiers"].get("T1", "")).strip()
            for clm_id in (dmeta.get("core_claims") or []) + CLM_ID_PAT.findall(dcard["body"]):
                if clm_id not in referenced_clms:
                    referenced_clms.append(clm_id)
            if compact_debates:
                schools = dmeta.get("perspectives_present") or []
                path_tag = f" | `{dcard['rel_path']}`" if len(card_ids) <= 4 else ""
                out.append(
                    f"- **`{did}`**（{dmeta.get('title', '')}{path_tag} | 流派 `{', '.join(schools)}`）：{dt1}"
                )
            else:
                out.append(f"### `{did}`：{dmeta.get('title', '')}")
                out.append(dcard["tiers"].get("T1", ""))
                out.append("")
                out.append(dcard["tiers"].get("T2", ""))
                out.append("")
        else:
            out.append(f"- ⚠️ 引用了尚未创建的争鸣卡 `{did}`")

    # 穿透关联 CLM -> SCH 展示具体史学家与学派归属
    if referenced_clms:
        out.append("")
        clm_limit = 12 if len(card_ids) >= 5 else (16 if len(card_ids) > 2 else 24)
        out.append(f"### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 {min(len(referenced_clms), clm_limit)}/{len(referenced_clms)} 条)")
        for clm_id in referenced_clms[:clm_limit]:
            if clm_id not in cards:
                continue
            ccard = cards[clm_id]
            cmeta = ccard["meta"]
            sch_raw = cmeta.get("scholar") or cmeta.get("scholars") or ""
            sch_list = sch_raw if isinstance(sch_raw, list) else ([sch_raw] if sch_raw else [])
            sch_tags: list[str] = []
            for sid in sch_list:
                sid_s = str(sid).strip()
                if sid_s in cards:
                    smeta = cards[sid_s]["meta"]
                    trad = smeta.get("tradition") or smeta.get("school") or ""
                    trad_s = ", ".join(trad) if isinstance(trad, list) else str(trad)
                    sch_tags.append(f"`{sid_s}`({smeta.get('title', '')}{f' · {trad_s}' if trad_s else ''})")
                elif sid_s:
                    sch_tags.append(f"`{sid_s}`")
            pages = cmeta.get("original_pages") or cmeta.get("pages") or ""
            out.append(
                f"- **`{clm_id}`** [{', '.join(sch_tags) if sch_tags else '未标学者'}{f' | {pages}' if pages else ''}]: "
                f"{cmeta.get('title', '')}"
            )
    out.append("")

    # 4. 去重关联时间线锚点 (默认 L0-L2 骨干事件；多卡高扇出时优先保留宏观 L0/L1 与多卡交集事件)
    all_linked_events = [
        ev
        for ev in events
        if primary_set & set((ev.get("actors") or []) + (ev.get("cards") or []) + (ev.get("debates") or []))
    ]
    l3_hidden = sum(1 for ev in all_linked_events if ev.get("level", 2) > max_tl_level)
    shown_events = [ev for ev in all_linked_events if ev.get("level", 2) <= max_tl_level]
    shown_events.sort(key=lambda x: (x.get("date_ns", ""), x.get("time_of_day") or "", x.get("id", "")))

    tl_cap = 32 if len(card_ids) >= 5 else 42
    l2_omitted = 0
    if len(card_ids) >= 3 and len(shown_events) > tl_cap:
        scored_ev: list[tuple[int, int, str, dict[str, Any]]] = []
        for ev in shown_events:
            ev_refs = set((ev.get("actors") or []) + (ev.get("cards") or []) + (ev.get("debates") or []))
            overlap = len(primary_set & ev_refs)
            is_macro = 1 if ev.get("level", 2) <= 1 else 0
            scored_ev.append((-overlap, -is_macro, ev.get("date_ns", ""), ev))
        scored_ev.sort(key=lambda x: (x[0], x[1], x[2]))
        l2_omitted = len(scored_ev) - tl_cap
        shown_events = sorted(
            [x[3] for x in scored_ev[:tl_cap]],
            key=lambda x: (x.get("date_ns", ""), x.get("time_of_day") or "", x.get("id", "")),
        )

    compact_tl = len(shown_events) > 28 or len(card_ids) >= 5
    extra_notes = []
    if l2_omitted:
        extra_notes.append(f"已按多卡交集优先折叠低重合 L2 旁支 {l2_omitted} 条")
    if l3_hidden:
        extra_notes.append(f"另有 {l3_hidden} 条 L3 逐日细节见 `timeline/L3_daily/`")
    out.append(
        f"## 4. 关联时间线骨干锚点 (L0–L{max_tl_level} 展示 {len(shown_events)} 条"
        + (f"，{'；'.join(extra_notes)}" if extra_notes else "")
        + ")"
    )
    for ev in shown_events:
        d_os = ev.get("date_os")
        d_ns = ev.get("date_ns")
        d_disp = f"{d_os} [O.S.] / {d_ns} [N.S.]" if d_os else f"{d_ns} [N.S.]"
        ev_refs = set((ev.get("actors") or []) + (ev.get("cards") or []) + (ev.get("debates") or []))
        is_shared_or_macro = (ev.get("level", 2) <= 1 or len(primary_set & ev_refs) >= 2) and len(card_ids) < 5
        if compact_tl and not is_shared_or_macro:
            out.append(f"- **{d_disp}** (`{ev.get('id')}`, L{ev.get('level')}): **{ev.get('title')}**")
        else:
            out.append(f"- **{d_disp}** (`{ev.get('id')}`, L{ev.get('level')}): **{ev.get('title')}** — {ev.get('summary')}")

    return "\n".join(out).strip() + "\n"


def cmd_pack(args: argparse.Namespace) -> int:
    cards = load_all_cards()
    edges = load_jsonl(ROOT / "graph" / "edges.jsonl")
    events = load_jsonl(ROOT / "timeline" / "events_ledger.jsonl")
    aliases_path = ROOT / "graph" / "aliases.yaml"
    aliases_text = aliases_path.read_text(encoding="utf-8") if aliases_path.exists() else ""

    req_ids: list[str] = []
    for raw_id in args.card_ids:
        if raw_id not in cards:
            print(f"错误: 未找到卡片 ID `{raw_id}`。", file=sys.stderr)
            return 1
        canonical_id = cards[raw_id]["id"]
        if canonical_id not in req_ids:
            req_ids.append(canonical_id)

    rendered = compile_pack_markdown(
        req_ids,
        cards,
        edges,
        events,
        aliases_text,
        max_tl_level=args.max_tl_level,
    )

    if args.write:
        if len(req_ids) != 1:
            print("错误: `--write` 仅用于单卡静态包落盘；多卡联合编译请直接读取标准输出。", file=sys.stderr)
            return 1
        pack_dir = ROOT / "graph" / "packs"
        pack_dir.mkdir(parents=True, exist_ok=True)
        dest = pack_dir / f"{req_ids[0]}.md"
        dest.write_text(rendered, encoding="utf-8")
        print(f"已编译并写入平衡上下文包: {dest.relative_to(ROOT).as_posix()}")
    else:
        print(rendered)
    return 0


# ============================================================================
# 5. 145本史料章节定位雷达 (`locate-chapters`, SQLite FTS5 trigram + 空书隔离)
# ============================================================================

def _is_chapter_effectively_empty(md_text: str) -> bool:
    cleaned = re.sub(r"(?m)^#.*$", "", md_text)
    cleaned = re.sub(r"(?m)^>\s*.*$", "", cleaned)
    cleaned = re.sub(r"<!--.*?-->", "", cleaned, flags=re.S)
    cleaned = re.sub(r"_\[本页无嵌入式文本层[^\]]*\]_", "", cleaned)
    cleaned = re.sub(r"_\[No embedded text[^\]]*\]_", "", cleaned, flags=re.I)
    cleaned = re.sub(r"---\s*Page\s*\d+\s*---", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\s+", "", cleaned)
    return len(cleaned) < 40


def _compute_corpus_signature() -> str:
    count = 0
    latest_mtime = 0.0
    for cat in ("monographs", "primary", "web-archive"):
        base = ROOT / "sources" / cat
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.suffix.lower() in (".md", ".yaml"):
                count += 1
                mt = p.stat().st_mtime
                if mt > latest_mtime:
                    latest_mtime = mt
    return f"{count}:{int(latest_mtime)}"


def ensure_chapter_fts_index(force_rebuild: bool = False) -> sqlite3.Connection:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    sig = _compute_corpus_signature()

    if FTS_DB_PATH.exists() and not force_rebuild:
        conn = sqlite3.connect(FTS_DB_PATH)
        try:
            row = conn.execute("SELECT val FROM meta WHERE key='corpus_sig'").fetchone()
            if row and row[0] == sig:
                return conn
        except sqlite3.Error:
            pass
        conn.close()
        FTS_DB_PATH.unlink(missing_ok=True)

    conn = sqlite3.connect(FTS_DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("CREATE TABLE meta (key TEXT PRIMARY KEY, val TEXT);")
    conn.execute(
        "CREATE TABLE quarantined_books (book_dir TEXT PRIMARY KEY, slug TEXT, source_file TEXT, empty_ratio REAL);"
    )
    conn.execute(
        "CREATE VIRTUAL TABLE chapters_fts USING fts5("
        "path UNINDEXED, book_dir UNINDEXED, line_count UNINDEXED, title, body, tokenize='trigram'"
        ");"
    )

    fts_rows: list[tuple[str, str, int, str, str]] = []
    qrn_rows: list[tuple[str, str, str, float]] = []

    for cat in ("monographs", "primary"):
        cat_dir = ROOT / "sources" / cat
        if not cat_dir.exists():
            continue
        for bdir in sorted(cat_dir.iterdir()):
            if not bdir.is_dir():
                continue
            rel_bdir = bdir.relative_to(ROOT).as_posix()
            mf_path = bdir / "manifest.yaml"
            mf_data: dict[str, Any] = {}
            if mf_path.exists():
                try:
                    mf_data = yaml.safe_load(mf_path.read_text(encoding="utf-8")) or {}
                except Exception:
                    mf_data = {}
            ch_files = [
                cf for cf in sorted(bdir.glob("*.md")) if cf.name.lower() not in ("toc.md", "readme.md")
            ]
            if not ch_files:
                continue

            texts = [(cf, cf.read_text(encoding="utf-8", errors="ignore")) for cf in ch_files]
            empty_cnt = sum(1 for _, t in texts if _is_chapter_effectively_empty(t))
            empty_ratio = empty_cnt / len(texts)
            if mf_data.get("needs_ocr") is True or empty_ratio >= 0.9:
                src_name = str(mf_data.get("source_file") or mf_data.get("title") or bdir.name)
                qrn_rows.append((rel_bdir, bdir.name, src_name, round(empty_ratio, 4)))
                continue

            for cf, txt in texts:
                if _is_chapter_effectively_empty(txt):
                    continue
                first_h = re.search(r"(?m)^#\s+(.+?)\s*$", txt)
                ch_title = first_h.group(1) if first_h else cf.stem
                fts_rows.append(
                    (
                        cf.relative_to(ROOT).as_posix(),
                        rel_bdir,
                        txt.count("\n") + 1,
                        f"{bdir.name} {ch_title}",
                        txt,
                    )
                )

    web_dir = ROOT / "sources" / "web-archive"
    if web_dir.exists():
        for wf in sorted(web_dir.rglob("*.md")):
            if wf.name.lower() in ("readme.md", "index.md"):
                continue
            txt = wf.read_text(encoding="utf-8", errors="ignore")
            first_h = re.search(r"(?m)^#\s+(.+?)\s*$", txt)
            w_title = first_h.group(1) if first_h else wf.stem
            fts_rows.append(
                (
                    wf.relative_to(ROOT).as_posix(),
                    wf.parent.relative_to(ROOT).as_posix(),
                    txt.count("\n") + 1,
                    w_title,
                    txt,
                )
            )

    with conn:
        conn.executemany("INSERT INTO quarantined_books VALUES (?, ?, ?, ?)", qrn_rows)
        conn.executemany("INSERT INTO chapters_fts VALUES (?, ?, ?, ?, ?)", fts_rows)
        conn.execute("INSERT INTO meta VALUES ('corpus_sig', ?)", (sig,))

    return conn


def search_chapters(query: str, top_k: int = 10, force_rebuild: bool = False) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    conn = ensure_chapter_fts_index(force_rebuild=force_rebuild)
    q_clean = query.strip()
    raw_tokens = [
        tok.strip()
        for tok in re.split(r"[\s()（）\[\]【】/—–\-·,，:：;；\"'“”‘’]+", q_clean)
        if len(tok.strip()) >= 2
    ]
    if not raw_tokens and q_clean:
        raw_tokens = [q_clean]

    tri_tokens = [t for t in raw_tokens if len(t) >= 3]
    short_tokens = [t for t in raw_tokens if len(t) < 3]

    candidates: dict[str, dict[str, Any]] = {}

    # 1) Trigram FTS5 精确/组合查询 (>=3 字符词元毫秒级倒排命中)
    if tri_tokens:
        escaped = ['"' + t.replace('"', '""') + '"' for t in tri_tokens]
        and_expr = " AND ".join(escaped)
        rows = conn.execute(
            "SELECT path, book_dir, line_count, title, bm25(chapters_fts, 0.0, 0.0, 0.0, 5.0, 1.0) AS score "
            "FROM chapters_fts WHERE chapters_fts MATCH ? ORDER BY score LIMIT ?",
            (and_expr, max(top_k * 4, 30)),
        ).fetchall()
        for path, bdir, lcnt, title, bm25_val in rows:
            candidates[path] = {
                "path": path,
                "book_dir": bdir,
                "lines": int(lcnt),
                "title": title,
                "score": round(-float(bm25_val) + 10.0, 4),
            }

        # 若多词 AND 命中不足，补充 OR 召回并按命中词元数重排
        if len(candidates) < top_k and len(escaped) > 1:
            or_expr = " OR ".join(escaped)
            or_rows = conn.execute(
                "SELECT path, book_dir, line_count, title, body, bm25(chapters_fts, 0.0, 0.0, 0.0, 4.0, 1.0) AS score "
                "FROM chapters_fts WHERE chapters_fts MATCH ? ORDER BY score LIMIT 40",
                (or_expr,),
            ).fetchall()
            for path, bdir, lcnt, title, body, bm25_val in or_rows:
                if path in candidates:
                    continue
                hay = (title + "\n" + body).lower()
                matched_cnt = sum(1 for t in raw_tokens if t.lower() in hay)
                candidates[path] = {
                    "path": path,
                    "book_dir": bdir,
                    "lines": int(lcnt),
                    "title": title,
                    "score": round(-float(bm25_val) + matched_cnt * 2.5, 4),
                }

    # 2) 短词元 (<3 字符，如双字中文人名“柳廷”) LIKE 补充扫描
    if short_tokens and (not tri_tokens or not candidates):
        where_clauses = []
        params: list[str] = []
        for st in short_tokens:
            where_clauses.append("(body LIKE ? OR title LIKE ?)")
            pat = f"%{st}%"
            params.extend([pat, pat])
        sql = (
            "SELECT path, book_dir, line_count, title, body FROM chapters_fts WHERE "
            + " AND ".join(where_clauses)
            + " LIMIT 60"
        )
        for path, bdir, lcnt, title, body in conn.execute(sql, params).fetchall():
            freq = sum(body.lower().count(st.lower()) + title.lower().count(st.lower()) * 4 for st in short_tokens)
            candidates[path] = {
                "path": path,
                "book_dir": bdir,
                "lines": int(lcnt),
                "title": title,
                "score": round(float(freq), 4),
            }

    # 3) 检查是否触碰已隔离的纯扫描空书 (`needs_ocr`)
    quarantine_hits: list[dict[str, Any]] = []
    for bdir, slug, src_file, eratio in conn.execute("SELECT book_dir, slug, source_file, empty_ratio FROM quarantined_books"):
        hay_q = f"{bdir} {slug} {src_file}".lower()
        if any(t.lower() in hay_q for t in raw_tokens):
            quarantine_hits.append(
                {
                    "book_dir": bdir,
                    "source_file": src_file,
                    "empty_ratio": eratio,
                    "warning": "该书系纯扫描无嵌入式文本层 (needs_ocr: true)，已从章节检索与精读中隔离。",
                }
            )

    conn.close()
    ranked = sorted(candidates.values(), key=lambda x: (-x["score"], x["path"]))[:top_k]
    return ranked, quarantine_hits


def cmd_locate_chapters(args: argparse.Namespace) -> int:
    ranked, qrn_hits = search_chapters(args.query, top_k=args.top, force_rebuild=args.rebuild)
    if args.json:
        # 保持列表顶层结构以兼容自动化调用；隔离告警可通过 stderr 提示
        if qrn_hits:
            for qh in qrn_hits:
                print(f"[QUARANTINE needs_ocr] {qh['book_dir']} ({qh['source_file']})", file=sys.stderr)
        print(json.dumps(ranked, ensure_ascii=False, indent=2))
        return 0

    print(f"# 史料章节定位雷达: `{args.query}` (Top {len(ranked)}，仅返章节坐标，请派 `close-reader` 整章顺读)\n")
    if qrn_hits:
        print("## ⚠️ 纯扫描无文字层隔离告警 (`needs_ocr: true`)")
        for qh in qrn_hits:
            print(f"- **`{qh['book_dir']}`** (`{qh['source_file']}`, 空页率 `{qh['empty_ratio']:.0%}`): {qh['warning']}")
        print()

    if not ranked:
        print("- _未命中有效带文本层章节。请尝试同义译名、俄/英文原词或检查是否属于待 OCR 书目。_")
        return 0

    print("| 排名 | 章节路径 (`path`) | 章节标题 | 总行数 | 相关度分 |")
    print("| ---: | :--- | :--- | ---: | ---: |")
    for idx, r in enumerate(ranked, start=1):
        print(f"| {idx} | `{r['path']}` | {r['title'].replace('|', '｜')} | `{r['lines']}` | `{r['score']:.2f}` |")
    return 0


# ============================================================================
# 6. 全库健康度、外键、2.2目标、T1字数与双历法审计 (audit-graph)
# ============================================================================

def cmd_audit(_args: argparse.Namespace) -> int:
    cards = load_all_cards()
    edges = load_jsonl(ROOT / "graph" / "edges.jsonl")
    events = load_jsonl(ROOT / "timeline" / "events_ledger.jsonl")

    errors: list[str] = []
    stubs: set[str] = set()

    # 1) 检查卡片三层协议与 [T1] <= 150 字红线
    seen_paths: set[Path] = set()
    for cid, c in cards.items():
        if c["path"] in seen_paths:
            continue
        seen_paths.add(c["path"])
        ctype = c["meta"].get("type")
        if ctype == "claim":
            continue
        for req_tier in ("T1", "T2"):
            if req_tier not in c["tiers"]:
                errors.append(f"卡片 `{cid}` ({c['rel_path']}) 缺少 `## [{req_tier}]` 标准分段")
        if c["rel_path"].startswith(("cards/", "historiography/debates/")) and "T1" in c["tiers"]:
            t1_body = re.sub(r"^##\s+\[T1\][^\n]*\n?", "", c["tiers"]["T1"]).strip()
            nws = len(re.sub(r"\s+", "", t1_body))
            if nws == 0 or nws > 150:
                errors.append(f"卡片 `{cid}` [T1] 去空白字符数为 {nws}（须在 1..150 之间）")

    # 2) 检查卡片 2.2 表格是否存在悬空目标 ID
    valid_entity_stems = {p.stem for p in (ROOT / "cards").rglob("*.md") if p.name.lower() != "readme.md"}
    sync_remap: dict[str, str] = {}
    sync_file = ROOT / "scripts" / "sync_graph_and_packs.py"
    if sync_file.exists():
        m_rm = re.search(r"ID_REMAP\s*=\s*(\{.*?\})", sync_file.read_text(encoding="utf-8"), flags=re.S)
        if m_rm:
            try:
                sync_remap = json.loads(m_rm.group(1))
            except Exception:
                sync_remap = {}

    for p in sorted((ROOT / "cards").rglob("*.md")):
        if p.name.lower() == "readme.md":
            continue
        for ln in p.read_text(encoding="utf-8").splitlines():
            s = ln.strip()
            if s.startswith("|") and s.endswith("|"):
                cols = [x.strip() for x in s.strip("|").split("|")]
                if len(cols) >= 4 and "---" not in cols[0] and "---" not in cols[1] and "一句话" not in cols[3]:
                    m_id = ENTITY_ID_PAT.search(cols[0])
                    if m_id:
                        mapped = sync_remap.get(m_id.group(0), m_id.group(0))
                        if mapped != p.stem and mapped not in valid_entity_stems:
                            errors.append(f"卡片 `{p.stem}` 2.2 表引用了不存在的目标 ID `{m_id.group(0)}`")

    # 3) 检查 CLM -> SCH 与 CLM -> Card/DEB 外键完整性
    valid_sch = {p.stem for p in (ROOT / "historiography" / "scholars").glob("SCH-*.md")}
    for cp in sorted((ROOT / "historiography" / "claims").glob("CLM-*.md")):
        cfm, _ = parse_frontmatter(cp.read_text(encoding="utf-8"))
        sval = cfm.get("scholar") or cfm.get("scholars")
        slist = sval if isinstance(sval, list) else ([sval] if sval else [])
        for sv in slist:
            if str(sv).strip() not in valid_sch:
                errors.append(f"论断卡 `{cp.stem}` 引用了无效学者外键 `{sv}`")
        for rk in ("related_cards", "cards", "target_cards", "related_debates", "debates"):
            rvals = cfm.get(rk) or []
            if isinstance(rvals, str):
                rvals = [rvals]
            for rv in rvals:
                if str(rv).strip() and str(rv).strip() not in cards:
                    errors.append(f"论断卡 `{cp.stem}` ({rk}) 引用了不存在的实体 `{rv}`")

    # 4) 检查 edges.jsonl 字段完整性
    for idx, e in enumerate(edges, start=1):
        s, t = e.get("source"), e.get("target")
        if not s or not t or not e.get("period") or not e.get("digest"):
            errors.append(f"edges.jsonl 第 {idx} 行缺少必填字段 (source/target/period/digest)")
            continue
        if s not in cards:
            stubs.add(s)
        if t not in cards:
            stubs.add(t)

    # 5) 校验双历法台账数学一致性 & Markdown 改历后误加 13 天检查
    reform_str = "1918-02-14"
    for ev in events:
        eid = ev.get("id", "?")
        d_ns = ev.get("date_ns")
        d_os = ev.get("date_os")
        prec = ev.get("precision")
        if prec == "day" and d_ns:
            try:
                ny, nm, nd = parse_iso_date(d_ns, "ns")
                jdn_ns = gregorian_to_jdn(ny, nm, nd)
                if d_ns < reform_str:
                    if not d_os:
                        errors.append(f"时间线 `{eid}` ({d_ns}) 早于苏俄改历日，必须填写俄历 `date_os`")
                    else:
                        oy, om, od = parse_iso_date(d_os, "os")
                        jdn_os = julian_to_jdn(oy, om, od)
                        if jdn_ns != jdn_os:
                            expected_ns = fmt_ymd(jdn_to_gregorian(jdn_os))
                            errors.append(
                                f"时间线 `{eid}` 俄历/公历换算错误! 俄历 {d_os} 应对应公历 {expected_ns}，当前填为 {d_ns}"
                            )
            except ValueError as exc:
                errors.append(f"时间线 `{eid}` 日期非法: {exc}")

    for md_dir in ("cards", "historiography", "timeline"):
        base = ROOT / md_dir
        if not base.exists():
            continue
        for mp in sorted(base.rglob("*.md")):
            for lineno, line in enumerate(mp.read_text(encoding="utf-8").splitlines(), start=1):
                for m_dd in DUAL_DATE_PAT.finditer(line):
                    os_s, ns_s = m_dd.group(1), m_dd.group(2)
                    try:
                        oy, om, od = parse_iso_date(os_s, "os")
                        ny, nm, nd = parse_iso_date(ns_s, "ns")
                        if julian_to_jdn(oy, om, od) != gregorian_to_jdn(ny, nm, nd):
                            errors.append(f"{mp.relative_to(ROOT).as_posix()}:{lineno} 双历换算不等 ({os_s} vs {ns_s})")
                    except ValueError as exc:
                        errors.append(f"{mp.relative_to(ROOT).as_posix()}:{lineno} 非法双历日期: {exc}")
                    if ns_s >= reform_str and not any(kw in line for kw in POST_REFORM_WHITELIST):
                        errors.append(
                            f"{mp.relative_to(ROOT).as_posix()}:{lineno} 改历后日期误标俄历加13天 (`{os_s} [O.S.] / {ns_s} [N.S.]`)"
                        )

    inbox_dir = ROOT / "inbox"
    inbox_files = (
        [p for p in inbox_dir.iterdir() if p.is_file() and p.name.lower() != "readme.md"]
        if inbox_dir.exists()
        else []
    )
    inbox_mb = sum(p.stat().st_size for p in inbox_files) / (1024 * 1024)

    print("=== 俄国革命知识库：全库结构、外键与双历法体检报告 ===")
    print(f"- 已建独立文件总数 (卡片/争鸣/学者/论断): {len(seen_paths)}")
    print(f"- 时效有向关系边总数:                   {len(edges)}")
    print(f"- 底层双历法事件台账条数:               {len(events)}")
    print(f"- 边表引用的待建 Stub 节点 ({len(stubs)} 个): {', '.join(sorted(stubs)) if stubs else '无'}")
    print(f"- inbox/ 本地电子书库存:                {len(inbox_files)} 个文件 (合计 {inbox_mb:.1f} MB)")

    if errors:
        print(f"\n❌ 发现 {len(errors)} 项结构、外键或历法硬伤:")
        for err in errors[:40]:
            print(f"  - {err}")
        return 1

    print("\n✅ 校验通过：YAML 元数据、[T1] 字数、2.2 目标、CLM/SCH 外键与双历法换算 100% 一致！")
    return 0


# ============================================================================
# 7. 跨 Provider 模型绑定查询与精简 delegate_task 载荷生成
# ============================================================================

def load_agent_models_cfg() -> dict[str, Any]:
    cfg_path = ROOT / "config" / "agent_models.json"
    if not cfg_path.exists():
        raise FileNotFoundError(f"未找到模型绑定配置文件: {cfg_path}")
    return json.loads(cfg_path.read_text(encoding="utf-8"))


def cmd_models(args: argparse.Namespace) -> int:
    cfg = load_agent_models_cfg()
    agents_cfg = cfg.get("agents", {})
    if args.role:
        if args.role not in agents_cfg:
            print(f"错误: 未知角色 `{args.role}`。可选: {', '.join(agents_cfg.keys())}", file=sys.stderr)
            return 1
        targets = {args.role: agents_cfg[args.role]}
    else:
        targets = agents_cfg

    print("# Agent 三层预算与复杂度模型绑定表\n")
    for role_id, info in targets.items():
        print(f"## `{role_id}` — {info.get('title')} (OpenCode 兜底默认: `{info.get('opencode_native_model')}`)")
        if info.get("cross_family_rule"):
            print(f"> 💡 {info['cross_family_rule']}")
        for idx, b in enumerate(info.get("bindings", [])):
            if args.tier and b.get("tier") != args.tier:
                continue
            t = b["target"]
            opts = json.dumps(t.get("options", {}), ensure_ascii=False)
            tier_tag = b.get("tier", "subscription")
            print(
                f"  [{idx}] ({tier_tag}) `{b['slot']}` [{b['family']}] -> provider=`{t['providerInstanceId']}`, "
                f"model=`{t['model']}`, options=`{opts}`"
            )
            print(f"      适用场景: {b['use_when']}")
        print()
    return 0


def _strip_routing_bloat(role_body: str) -> str:
    """剥离角色模板中仅面向主控官的模型路由段落，避免子 Agent 浪费上下文 Token。"""
    return re.sub(
        r"(?ms)^##\s+绑定模型分级策略.*?(?=^##\s+|\Z)",
        "",
        role_body,
    ).strip()


def cmd_delegate_prompt(args: argparse.Namespace) -> int:
    cfg = load_agent_models_cfg()
    agents_cfg = cfg.get("agents", {})
    if args.role not in agents_cfg:
        print(f"错误: 未知角色 `{args.role}`", file=sys.stderr)
        return 1

    info = agents_cfg[args.role]
    bindings = info.get("bindings", [])
    chosen = None
    if args.slot:
        for idx, b in enumerate(bindings):
            if args.slot in (str(idx), b["slot"]):
                chosen = b
                break
    if chosen is None and args.tier:
        for b in bindings:
            if b.get("tier") == args.tier:
                chosen = b
                break
    if chosen is None:
        chosen = bindings[0]

    agent_md_path = ROOT / ".opencode" / "agents" / f"{args.role}.md"
    _, role_body = parse_frontmatter(agent_md_path.read_text(encoding="utf-8"))
    clean_role_body = _strip_routing_bloat(role_body)

    composed_task = (
        f"【角色身份与铁律】你当前以专职角色 `{args.role}`（{info.get('title')}）在工作区 `{ROOT.as_posix()}` 执行任务。\n"
        f"请严格遵守以下角色规范与写目录围栏，绝不越界修改其他目录文件：\n\n"
        f"{clean_role_body}\n\n"
        f"---\n"
        f"【本次具体派发任务】\n{args.task.strip()}\n"
    )

    payload = {
        "title": f"[{args.role}] {args.task.strip()[:48]}",
        "role": info.get("t3_role", "research"),
        "target": chosen["target"],
        "dispatch_hint": chosen["dispatch"],
        "family": chosen["family"],
        "task": composed_task,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def cmd_scan_inbox(args: argparse.Namespace) -> int:
    inbox_dir = ROOT / "inbox"
    files = sorted(
        [p for p in inbox_dir.iterdir() if p.is_file() and p.name.lower() != "readme.md"],
        key=lambda x: x.name.lower(),
    )
    size_counts: dict[int, int] = {}
    for p in files:
        sz = p.stat().st_size
        size_counts[sz] = size_counts.get(sz, 0) + 1

    records: list[dict[str, Any]] = []
    for idx, p in enumerate(files, start=1):
        sz = p.stat().st_size
        ext = p.suffix.lower()
        flags: list[str] = []
        if ext in (".crdownload", ".part", ".tmp"):
            flags.append("unfinished_download")
        if ext == ".caj":
            flags.append("caj_proprietary_format")
        if size_counts[sz] > 1:
            flags.append("exact_size_duplicate")
        if p.name == "Lars T. Lih - Lenin Rediscovered - What Is to Be Done In Context (2008).pdf" and sz < 400_000:
            flags.append("corrupted_zlib_stream")
        records.append(
            {
                "seq": idx,
                "filename": p.name,
                "ext": ext,
                "size_kb": round(sz / 1024, 1),
                "flags": flags,
            }
        )

    total_mb = sum(p.stat().st_size for p in files) / (1024 * 1024)
    flagged = [r for r in records if r["flags"]]
    print(f"扫描完成: 共 {len(records)} 个文件, 合计 {total_mb:.1f} MB, 标记异常/重复文件 {len(flagged)} 个。")
    if args.write:
        out_path = ROOT / "sources" / "inbox_inventory.jsonl"
        out_path.write_text(
            "\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n",
            encoding="utf-8",
        )
        print(f"已写入轻量级 Git 追踪目录清单: {out_path.relative_to(ROOT).as_posix()}")
    return 0


def cmd_merge_timeline(_args: argparse.Namespace) -> int:
    ledger_path = ROOT / "timeline" / "events_ledger.jsonl"
    by_id: dict[str, dict[str, Any]] = {}
    for ev in load_jsonl(ledger_path):
        by_id[ev["id"]] = ev

    cand_files = sorted((ROOT / "timeline").rglob("_*events.jsonl"))
    merged_count = 0
    for cf in cand_files:
        for ev in load_jsonl(cf):
            clean = {
                "id": ev["id"],
                "date_ns": ev["date_ns"],
                "date_os": ev.get("date_os"),
                "precision": ev.get("precision", "day"),
                "level": ev.get("level", 2),
                "era": ev.get("era", ""),
                "title": ev.get("title", ""),
                "summary": ev.get("summary", ""),
                "actors": ev.get("actors", []),
                "cards": ev.get("cards", []),
                "debates": ev.get("debates", []),
                "sources": ev.get("sources", []),
            }
            if ev.get("time_of_day"):
                clean["time_of_day"] = ev["time_of_day"]
            by_id[clean["id"]] = clean
            merged_count += 1
        cf.unlink()

    sorted_items = sorted(by_id.values(), key=lambda x: (x.get("date_ns", ""), x.get("time_of_day") or "", x.get("id", "")))
    ledger_path.write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in sorted_items) + "\n",
        encoding="utf-8",
    )
    print(f"已归并 {len(cand_files)} 个候选文件中的 {merged_count} 条记录 -> 主台账当前共 {len(sorted_items)} 条独立事件。")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="俄国革命知识库核心管理 CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_date = sub.add_parser("date", help="俄历(os)与公历(ns)精确双向换算")
    p_date.add_argument("date_str", help="ISO 日期 YYYY-MM-DD")
    p_date.add_argument("--from", dest="src", choices=["os", "ns"], required=True, help="输入日期所属历法")
    p_date.set_defaults(func=cmd_date)

    p_toc = sub.add_parser("toc", help="生成 Markdown 文献章节与行号索引")
    p_toc.add_argument("path", help="目标 Markdown 文件路径")
    p_toc.set_defaults(func=cmd_toc)

    p_tl = sub.add_parser("timeline", help="多尺度双历法时间线切片查询")
    p_tl.add_argument("--max-level", type=int, default=3, choices=[0, 1, 2, 3])
    p_tl.add_argument("--from", dest="date_from", default=None, help="起始公历日期 YYYY-MM-DD")
    p_tl.add_argument("--to", dest="date_to", default=None, help="结束公历日期 YYYY-MM-DD")
    p_tl.add_argument("--era", default=None, help="阶段编号如 E01..E10")
    p_tl.add_argument("--entity", default=None, help="关联实体或争鸣 ID")
    p_tl.set_defaults(func=cmd_timeline)

    p_pack = sub.add_parser("pack", help="编译单卡或多卡去重 1-Hop 防偏斜平衡上下文包")
    p_pack.add_argument("card_ids", nargs="+", help="一个或多个目标卡片 ID，如 PER-stalin PER-bukharin POL-nep")
    p_pack.add_argument("--max-tl-level", type=int, default=2, choices=[0, 1, 2, 3], help="时间线默认展开最大层级 (默认 L2)")
    p_pack.add_argument("--write", action="store_true", help="单卡模式下写入 graph/packs/<ID>.md")
    p_pack.set_defaults(func=cmd_pack)

    p_loc = sub.add_parser("locate-chapters", help="基于 SQLite FTS5 trigram 定位 145 本史料具体章节并告警空书")
    p_loc.add_argument("query", help="中/英/俄检索词，如 '乌格拉诺夫' 或 'scissors crisis'")
    p_loc.add_argument("--top", type=int, default=10, help="返回前 N 个候选章节 (默认 10)")
    p_loc.add_argument("--json", action="store_true", help="输出机器可读 JSON 列表")
    p_loc.add_argument("--rebuild", action="store_true", help="强制重建 .cache/kb_chapters.sqlite 索引")
    p_loc.set_defaults(func=cmd_locate_chapters)

    p_audit = sub.add_parser("audit-graph", help="全库断链、外键、2.2目标、[T1]字数与双历法体检")
    p_audit.set_defaults(func=cmd_audit)

    p_models = sub.add_parser("models", help="查看各 Agent 绑定的跨 Provider 模型池")
    p_models.add_argument("--role", default=None, help="按角色 ID 过滤，如 close-reader")
    p_models.add_argument(
        "--tier",
        default=None,
        choices=["subscription", "apex", "fallback-simple", "fallback-complex"],
        help="按预算/复杂度层级过滤",
    )
    p_models.set_defaults(func=cmd_models)

    p_dp = sub.add_parser("delegate-prompt", help="生成跨 Provider T3 delegate_task 标准载荷")
    p_dp.add_argument("role", help="角色 ID，如 close-reader / dialectic-auditor")
    p_dp.add_argument("--slot", default=None, help="指定具体模型槽位名或序号")
    p_dp.add_argument(
        "--tier",
        default="subscription",
        choices=["subscription", "apex", "fallback-simple", "fallback-complex"],
        help="预算层级，默认优先走 subscription 订阅池",
    )
    p_dp.add_argument("--task", required=True, help="派发给该子 Agent 的具体任务说明")
    p_dp.set_defaults(func=cmd_delegate_prompt)

    p_scan = sub.add_parser("scan-inbox", help="扫描 inbox/ 生成轻量级 Git 追踪元数据清单")
    p_scan.add_argument("--write", action="store_true", help="写入 sources/inbox_inventory.jsonl")
    p_scan.set_defaults(func=cmd_scan_inbox)

    p_merge_tl = sub.add_parser("merge-timeline", help="归并候选事件 JSONL 进入主 events_ledger.jsonl")
    p_merge_tl.set_defaults(func=cmd_merge_timeline)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except Exception as exc:  # noqa: BLE001
        print(f"执行错误: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
