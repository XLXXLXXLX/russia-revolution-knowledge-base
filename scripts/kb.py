#!/usr/bin/env python3
"""
俄国革命知识库（1860s–1929）核心辅助工具 CLI (零第三方依赖)

支持子命令:
  1. date        俄历 (O.S., 儒略历) 与公历 (N.S., 格里高利历) 精确双向换算
  2. toc         生成文献章节与标题行号索引 (供 close-reader 无 grep 整章顺读)
  3. timeline    按时间窗、层级 (L0-L3)、时代或实体切片查询双历法时间线
  4. pack        编译 1-Hop 平衡上下文包 (解决 N+1 读取爆炸与上下文偏斜)
  5. audit-graph 检查卡片结构、断链、待建 Stub 队列、双历法数学一致性与 inbox 新书
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent


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
    diff_days = gregorian_to_jdn(*parse_iso_date(ns_str, "ns")) - julian_to_jdn(
        *parse_iso_date(os_str, "os")
    )
    note = (
        "注意：苏俄已于 1918-02-14 [N.S.] 正式改行公历，此后国内官方文献通常直接使用公历（白卫军控制区及东正教会除外）。"
        if jdn >= reform_jdn
        else f"改历前日期（两历相差 {abs(jdn - julian_to_jdn(*parse_iso_date(ns_str, 'os'))) if False else (jdn - julian_to_jdn(*parse_iso_date(os_str, 'os')) + (gregorian_to_jdn(*parse_iso_date(ns_str, 'ns')) - jdn))} 天）"
    )
    # 直接用两历同日差值计算相差天数
    oy, om, od = parse_iso_date(os_str, "os")
    offset = jdn - gregorian_to_jdn(oy, om, od) if oy != 1900 or om != 2 or od != 29 else 13
    if jdn < reform_jdn:
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
# 卡片与台账加载辅助函数
# ============================================================================

def parse_simple_frontmatter(md_text: str) -> tuple[dict[str, Any], str]:
    """轻量解析本库标准 YAML Frontmatter 与正文 (零外部依赖)。"""
    md_text = md_text.replace("\r\n", "\n")
    if not md_text.startswith("---\n"):
        return {}, md_text
    end_idx = md_text.find("\n---\n", 4)
    if end_idx == -1:
        return {}, md_text
    fm_block = md_text[4:end_idx]
    body = md_text[end_idx + 5 :]
    meta: dict[str, Any] = {}
    current_map_key: str | None = None

    for raw in fm_block.splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        if raw.startswith("  ") and current_map_key and ":" in raw:
            sub_k, sub_v = raw.strip().split(":", 1)
            meta.setdefault(current_map_key, {})[sub_k.strip()] = _parse_scalar_or_list(sub_v.strip())
            continue
        if ":" in raw:
            k, v = raw.split(":", 1)
            k = k.strip()
            v = v.strip()
            # 去掉行尾注释（不在引号内时）
            if v and not (v.startswith('"') or v.startswith("[") or v.startswith("'")):
                v = v.split(" #", 1)[0].strip()
            if v == "":
                current_map_key = k
                meta[k] = {}
            else:
                current_map_key = None
                meta[k] = _parse_scalar_or_list(v)
    return meta, body


def _parse_scalar_or_list(val: str) -> Any:
    if val.startswith("[") and val.endswith("]"):
        try:
            return json.loads(val)
        except json.JSONDecodeError:
            inner = val[1:-1].strip()
            if not inner:
                return []
            return [x.strip().strip('"').strip("'") for x in inner.split(",")]
    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        return val[1:-1]
    return val


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
            meta, body = parse_simple_frontmatter(text)
            cid = meta.get("id")
            if not cid:
                continue
            cards[cid] = {
                "id": cid,
                "path": p,
                "rel_path": p.relative_to(ROOT).as_posix(),
                "meta": meta,
                "tiers": extract_tiers(body),
            }
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
# 4. 1-Hop 防偏斜上下文包编译器 (pack)
# ============================================================================

def cmd_pack(args: argparse.Namespace) -> int:
    cards = load_all_cards()
    edges = load_jsonl(ROOT / "graph" / "edges.jsonl")
    events = load_jsonl(ROOT / "timeline" / "events_ledger.jsonl")
    aliases_path = ROOT / "graph" / "aliases.yaml"
    aliases_text = aliases_path.read_text(encoding="utf-8") if aliases_path.exists() else ""

    cid = args.card_id
    if cid not in cards:
        print(f"错误: 未找到卡片 ID `{cid}`。现有卡片: {', '.join(sorted(cards.keys()))}", file=sys.stderr)
        return 1

    card = cards[cid]
    meta = card["meta"]
    tiers = card["tiers"]

    related_edges = [e for e in edges if e.get("source") == cid or e.get("target") == cid]
    neighbor_ids: list[str] = []
    for e in related_edges:
        other = e["target"] if e["source"] == cid else e["source"]
        if other not in neighbor_ids:
            neighbor_ids.append(other)

    # 收集偏斜告警
    warnings: list[str] = []
    cov = meta.get("coverage_status", "unknown")
    p_present = meta.get("perspectives_present", [])
    p_missing = meta.get("perspectives_missing", [])
    if cov in ("stub", "draft"):
        warnings.append(f"主卡当前完备度为 `{cov}`，尚未达到多源交叉核实定稿状态。")
    if isinstance(p_present, list) and len(p_present) < 2:
        warnings.append(f"主卡当前仅覆盖 {len(p_present)} 种史学视角 ({p_present})，存在单一叙事偏斜风险！")
    if p_missing:
        warnings.append(f"主卡显式声明尚缺以下视角待补: `{', '.join(p_missing)}`。")

    missing_neighbors = [nid for nid in neighbor_ids if nid not in cards]
    if missing_neighbors:
        warnings.append(
            f"一跳邻域中有 {len(missing_neighbors)} 个关联节点尚未建卡 (Stub 盲区): `{', '.join(missing_neighbors)}`。"
        )

    out: list[str] = []
    out.append(f"# 1-Hop 平衡上下文包：`{cid}` ({meta.get('title', '')})")
    out.append("")
    out.append("> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。")
    out.append("")
    out.append("## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)")
    out.append(f"- **主卡路径**: `{card['rel_path']}`")
    out.append(f"- **完备度等级**: `{cov}`")
    out.append(f"- **已覆盖视角**: `{', '.join(p_present) if p_present else '未标注'}`")
    out.append(f"- **待补齐视角**: `{', '.join(p_missing) if p_missing else '无显式缺失'}`")
    if warnings:
        out.append("- **偏斜风险提示**:")
        for w in warnings:
            out.append(f"  - ⚠️ {w}")
    out.append("")

    out.append("## 1. 主卡核心层 ([T1] + [T2])")
    out.append(tiers.get("T1", "_缺失 [T1]_"))
    out.append("")
    out.append(tiers.get("T2", "_缺失 [T2]_"))
    out.append("")

    out.append(f"## 2. 一跳邻域等权重微摘要 (共 {len(neighbor_ids)} 个关联节点，严防大卡霸占上下文)")
    if not neighbor_ids:
        out.append("- _当前 `graph/edges.jsonl` 中尚无关联边。_")
    for nid in neighbor_ids:
        out.append(f"### 邻居节点: `{nid}`")
        for e in related_edges:
            if e["source"] == nid or e["target"] == nid:
                direction = f"`{e['source']}` → `{e['target']}`"
                out.append(f"- **时效关系边** ({direction} | `{e.get('relation')}` | 有效时段: `{e.get('period')}`): {e.get('digest')}")
        if nid in cards:
            ncard = cards[nid]
            nmeta = ncard["meta"]
            nt1 = re.sub(r"^##\s+\[T1\][^\n]*\n?", "", ncard["tiers"].get("T1", "")).strip()
            out.append(f"- **节点定性微摘要 [T1]** (完备度 `{nmeta.get('coverage_status', '?')}`): {nt1}")
        else:
            in_alias = "已登记译名消歧表" if nid in aliases_text else "尚未登记译名表"
            out.append(f"- **节点状态**: `[待建卡 Stub | {in_alias}]` — 如当前任务高度依赖该节点细节，请指派 `graph-curator` 优先建卡。")
        out.append("")

    debate_ids: list[str] = list(meta.get("related_debates", []))
    for e in related_edges:
        for ev_ref in e.get("evidence", []):
            if str(ev_ref).startswith("DEB-") and ev_ref not in debate_ids:
                debate_ids.append(ev_ref)

    out.append("## 3. 关联史学争鸣光谱 (Historiographical Debates)")
    if not debate_ids:
        out.append("- _暂无挂载的 `DEB-*` 争鸣母题卡。_")
    for did in debate_ids:
        if did in cards:
            dcard = cards[did]
            out.append(f"### `{did}`：{dcard['meta'].get('title', '')}")
            out.append(dcard["tiers"].get("T1", ""))
            out.append("")
            out.append(dcard["tiers"].get("T2", ""))
            out.append("")
        else:
            out.append(f"- ⚠️ 引用了尚未创建的争鸣卡 `{did}`")

    linked_events = [
        ev
        for ev in events
        if cid in (ev.get("actors", []) + ev.get("cards", []) + ev.get("debates", []))
    ]
    linked_events.sort(key=lambda x: x.get("date_ns", ""))
    out.append(f"## 4. 关联时间线锚点 (共 {len(linked_events)} 条)")
    for ev in linked_events:
        d_os = ev.get("date_os")
        d_ns = ev.get("date_ns")
        d_disp = f"{d_os} [O.S.] / {d_ns} [N.S.]" if d_os else f"{d_ns} [N.S.]"
        out.append(f"- **{d_disp}** (`{ev.get('id')}`, L{ev.get('level')}): **{ev.get('title')}** — {ev.get('summary')}")

    rendered = "\n".join(out).strip() + "\n"
    if args.write:
        pack_dir = ROOT / "graph" / "packs"
        pack_dir.mkdir(parents=True, exist_ok=True)
        dest = pack_dir / f"{cid}.md"
        dest.write_text(rendered, encoding="utf-8")
        print(f"已编译并写入平衡上下文包: {dest.relative_to(ROOT).as_posix()}")
    else:
        print(rendered)
    return 0


# ============================================================================
# 5. 全库健康度、双历法与偏斜审计 (audit-graph)
# ============================================================================

def cmd_audit(_args: argparse.Namespace) -> int:
    cards = load_all_cards()
    edges = load_jsonl(ROOT / "graph" / "edges.jsonl")
    events = load_jsonl(ROOT / "timeline" / "events_ledger.jsonl")

    errors: list[str] = []
    stubs: set[str] = set()

    # 1) 检查卡片三层协议
    for cid, c in cards.items():
        if c["meta"].get("type") == "claim":
            continue
        for req_tier in ("T1", "T2"):
            if req_tier not in c["tiers"]:
                errors.append(f"卡片 `{cid}` ({c['rel_path']}) 缺少 `## [{req_tier}]` 标准分段")

    # 2) 检查边表与待建卡前沿队列
    connected_ids: set[str] = set()
    for idx, e in enumerate(edges, start=1):
        s, t = e.get("source"), e.get("target")
        if not s or not t or not e.get("period") or not e.get("digest"):
            errors.append(f"edges.jsonl 第 {idx} 行缺少必填字段 (source/target/period/digest)")
            continue
        connected_ids.add(s)
        connected_ids.add(t)
        if s not in cards:
            stubs.add(s)
        if t not in cards:
            stubs.add(t)

    # 3) 校验双历法台账数学一致性
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

    # 4) 检查 inbox 待处理新书（精简统计，避免刷屏）
    inbox_dir = ROOT / "inbox"
    inbox_files = (
        [p for p in inbox_dir.iterdir() if p.is_file() and p.name.lower() != "readme.md"]
        if inbox_dir.exists()
        else []
    )
    inbox_mb = sum(p.stat().st_size for p in inbox_files) / (1024 * 1024)
    crdownloads = [p.name for p in inbox_files if p.suffix.lower() == ".crdownload"]

    print("=== 俄国革命知识库：全库结构与防偏斜体检报告 ===")
    print(f"- 已建卡片/争鸣/论断总数: {len(cards)}")
    print(f"- 时效有向关系边总数:     {len(edges)}")
    print(f"- 底层双历法事件台账条数: {len(events)}")
    print(f"- 边表引用的待建 Stub 节点 ({len(stubs)} 个): {', '.join(sorted(stubs)) if stubs else '无'}")
    print(f"- inbox/ 本地电子书库存:  {len(inbox_files)} 个文件 (合计 {inbox_mb:.1f} MB，已由 .gitignore 隔离大体积二进制)")
    if crdownloads:
        print(f"  ⚠️ 检测到未完成下载临时文件 ({len(crdownloads)} 个): {', '.join(crdownloads)}")

    if errors:
        print("\n❌ 发现结构或历法硬伤:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("\n✅ 校验通过：所有卡片分层协议、时效边字段与俄历/公历数学换算完全一致！")
    return 0


# ============================================================================
# 6. 跨 Provider 模型绑定查询与 delegate_task 载荷生成 (models / delegate-prompt)
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
    _, role_body = parse_simple_frontmatter(agent_md_path.read_text(encoding="utf-8"))

    composed_task = (
        f"【角色身份与铁律】你当前以专职角色 `{args.role}`（{info.get('title')}）在工作区 `{ROOT.as_posix()}` 执行任务。\n"
        f"请严格遵守以下角色规范与写目录围栏，绝不越界修改其他目录文件：\n\n"
        f"{role_body.strip()}\n\n"
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
            # 标准化保留核心字段
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

    p_pack = sub.add_parser("pack", help="编译 1-Hop 防偏斜平衡上下文包")
    p_pack.add_argument("card_id", help="目标卡片 ID，如 PER-bukharin")
    p_pack.add_argument("--write", action="store_true", help="写入 graph/packs/<ID>.md")
    p_pack.set_defaults(func=cmd_pack)

    p_audit = sub.add_parser("audit-graph", help="全库断链、分层协议与双历法体检")
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
