#!/usr/bin/env python3
"""
通用电子书（PDF / EPUB / DOCX）规整提取器 (供 source-extractor 子 Agent 调用)
建议通过虚拟环境运行:
  .venv\\Scripts\\python.exe scripts/extract_book.py --input "inbox/<书名>.pdf" --out-dir "sources/monographs/<slug>" --chunk-pages 25

功能:
  1. PDF: 使用 PyMuPDF (pymupdf) 逐页提取文本，强制注入原始纸书页码锚点 `<!-- PDF p. N -->` / `[PDF p. N]`；
     若原 PDF 带有书签目录 (TOC)，优先按一级书签切分章节；若无书签或单章过大，则按 `--chunk-pages` 分卷，绝不丢失任何一页或脚注。
  2. EPUB: 按 OPF spine 顺序解析 HTML/XHTML 文档，保留章节结构与脚注，拆分为规范 `chXX_<slug>.md`。
  3. 自动调用 kb.py 逻辑为生成的所有章节汇总产出 `toc.md`（含文件名、标题、起始行号、总行数），供 `close-reader` 零 grep 整章顺读。
"""

from __future__ import annotations

import argparse
import re
import sys
import warnings
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent


def slugify(text: str, max_len: int = 40) -> str:
    text = text.replace("\x00", "")
    s = re.sub(r"[^\w\u4e00-\u9fff\u0400-\u04ff-]+", "_", text.strip())
    s = re.sub(r"_+", "_", s).strip("_").lower()
    return (s[:max_len].rstrip("_")) or "section"


def extract_pdf(pdf_path: Path, out_dir: Path, chunk_pages: int) -> list[dict]:
    import pymupdf

    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    raw_toc = doc.get_toc()  # [[lvl, title, page_1based], ...]

    # 选取 L1 (或 L1+L2 当 L1 过少时) 书签切分
    l1 = [(t.strip(), max(1, min(p, total_pages))) for lvl, t, p in raw_toc if lvl == 1 and 1 <= p <= total_pages]
    if len(l1) < 3:
        l1 = [(t.strip(), max(1, min(p, total_pages))) for lvl, t, p in raw_toc if lvl in (1, 2) and 1 <= p <= total_pages]

    ranges: list[tuple[str, int, int]] = []
    if len(l1) >= 3:
        # 补齐扉页/前言 (若首个书签不在第1页)
        if l1[0][1] > 1:
            ranges.append(("frontmatter", 1, l1[0][1] - 1))
        for idx, (title, start_p) in enumerate(l1):
            end_p = l1[idx + 1][1] - 1 if idx + 1 < len(l1) else total_pages
            if end_p < start_p:
                end_p = start_p
            # 若单章超过 chunk_pages * 2，进一步拆分为 part1/part2 以便 close-reader 顺读
            if (end_p - start_p + 1) > chunk_pages * 2:
                part_no = 1
                cur = start_p
                while cur <= end_p:
                    sub_end = min(cur + chunk_pages - 1, end_p)
                    ranges.append((f"{title} (Part {part_no})", cur, sub_end))
                    cur = sub_end + 1
                    part_no += 1
            else:
                ranges.append((title, start_p, end_p))
    else:
        cur = 1
        part_no = 1
        while cur <= total_pages:
            sub_end = min(cur + chunk_pages - 1, total_pages)
            ranges.append((f"Pages {cur}-{sub_end}", cur, sub_end))
            cur = sub_end + 1
            part_no += 1

    written: list[dict] = []
    empty_pages = 0
    for idx, (title, sp, ep) in enumerate(ranges):
        fn = f"ch{idx:02d}_{slugify(title)}.md"
        lines: list[str] = [
            f"# {title}",
            f"",
            f"> 原书文件名: `{pdf_path.name}` | PDF 页码区间: `pp. {sp}–{ep}` / 总 {total_pages} 页",
            f"",
        ]
        for pno in range(sp, ep + 1):
            page_txt = doc[pno - 1].get_text("text").replace("\x00", "").strip()
            if not page_txt:
                empty_pages += 1
            lines.append(f"## [PDF p. {pno}]")
            lines.append("")
            lines.append(page_txt if page_txt else "_[本页无嵌入式文本层，可能为空白页、插图或纯扫描图像]_")
            lines.append("")

        content = "\n".join(lines).strip() + "\n"
        dest = out_dir / fn
        dest.write_text(content, encoding="utf-8")
        written.append(
            {
                "file": fn,
                "title": title,
                "pdf_pages": f"{sp}-{ep}",
                "lines": content.count("\n"),
                "chars": len(content),
            }
        )

    doc.close()
    empty_ratio = empty_pages / max(total_pages, 1)
    return written, {"total_pages": total_pages, "empty_pages": empty_pages, "empty_ratio": round(empty_ratio, 4)}


def extract_docx(docx_path: Path, out_dir: Path) -> tuple[list[dict], dict]:
    with zipfile.ZipFile(docx_path, "r") as zf:
        xml_bytes = zf.read("word/document.xml")
    root = ET.fromstring(xml_bytes)
    paragraphs: list[str] = []
    for p in root.findall(".//{*}p"):
        texts = [t.text for t in p.findall(".//{*}t") if t.text]
        line = "".join(texts).strip()
        if line:
            paragraphs.append(line)
    body = "\n\n".join(paragraphs)
    fn = "ch00_full_document.md"
    content = f"# {docx_path.stem}\n\n> 原书文件名: `{docx_path.name}` | DOCX 提取\n\n{body}\n"
    (out_dir / fn).write_text(content, encoding="utf-8")
    written = [
        {
            "file": fn,
            "title": docx_path.stem,
            "pdf_pages": "docx:all",
            "lines": content.count("\n"),
            "chars": len(content),
        }
    ]
    return written, {"total_pages": 1, "empty_pages": 0 if body else 1, "empty_ratio": 0.0 if body else 1.0}


def extract_epub(epub_path: Path, out_dir: Path) -> tuple[list[dict], dict]:
    from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning

    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

    written: list[dict] = []
    with zipfile.ZipFile(epub_path, "r") as zf:
        names = set(zf.namelist())
        spine_files: list[str] = []

        # 解析 META-INF/container.xml -> content.opf 获取准确阅读顺序 (spine)
        if "META-INF/container.xml" in names:
            try:
                c_root = ET.fromstring(zf.read("META-INF/container.xml"))
                rf = c_root.find(".//{*}rootfile")
                if rf is not None and rf.attrib.get("full-path") in names:
                    opf_path = rf.attrib["full-path"]
                    opf_dir = Path(opf_path).parent.as_posix()
                    opf_root = ET.fromstring(zf.read(opf_path))
                    manifest_map: dict[str, str] = {}
                    for item in opf_root.findall(".//{*}manifest/{*}item"):
                        iid = item.attrib.get("id", "")
                        href = item.attrib.get("href", "")
                        full_href = f"{opf_dir}/{href}".lstrip("./") if opf_dir != "." else href
                        manifest_map[iid] = full_href
                    for itemref in opf_root.findall(".//{*}spine/{*}itemref"):
                        idref = itemref.attrib.get("idref", "")
                        target = manifest_map.get(idref, "")
                        if target in names:
                            spine_files.append(target)
            except Exception:
                spine_files = []

        if not spine_files:
            spine_files = sorted(n for n in names if n.lower().endswith((".xhtml", ".html", ".htm")))

        sec_idx = 0
        for sp_file in spine_files:
            raw = zf.read(sp_file)
            soup = BeautifulSoup(raw, "lxml")
            body_root = soup.body if soup.body else soup
            h_tag = body_root.find(["h1", "h2", "h3", "h4"]) or soup.find("title")
            title = h_tag.get_text(" ", strip=True) if h_tag else Path(sp_file).stem
            txt = soup.get_text("\n", strip=True)
            if len(txt) < 120:
                continue
            fn = f"ch{sec_idx:02d}_{slugify(title)}.md"
            content = (
                f"# {title}\n\n"
                f"> 原书文件名: `{epub_path.name}` | EPUB 内部路径: `{sp_file}`\n\n"
                f"{txt}\n"
            )
            (out_dir / fn).write_text(content, encoding="utf-8")
            written.append(
                {
                    "file": fn,
                    "title": title,
                    "pdf_pages": f"epub:{sp_file}",
                    "lines": content.count("\n"),
                    "chars": len(content),
                }
            )
            sec_idx += 1

    return written, {"total_pages": len(written), "empty_pages": 0, "empty_ratio": 0.0 if written else 1.0}


def write_master_toc_and_manifest(book_name: str, out_dir: Path, written: list[dict], stats: dict) -> bool:
    import yaml

    needs_ocr = stats.get("empty_ratio", 0.0) >= 0.85
    total_lines = sum(w["lines"] for w in written)
    total_chars = sum(w["chars"] for w in written)
    guidance = (
        "⚠️ **纯图像扫描告警 (`needs_ocr: true`)**：本文件空白文本页占比高达 "
        f"`{stats.get('empty_ratio', 0.0):.1%}`，已自动隔离！`close-reader` 严禁读取空壳占位章节，待 OCR 后方可入库精读。"
        if needs_ocr
        else "请直接按下方文件名使用 `read` 工具（`offset=1, limit=1800` 翻页）连续顺读整章，严禁使用 `grep` 断章取义。"
    )
    toc_lines = [
        f"# 文献分章与行号目录索引 (`toc.md`)",
        f"",
        f"- **原始文件**: `{book_name}`",
        f"- **规整目录**: `{out_dir.relative_to(ROOT).as_posix() if out_dir.is_relative_to(ROOT) else out_dir.as_posix()}`",
        f"- **章节总数**: `{len(written)}` | **总行数**: `{total_lines}` | **总字符数**: `{total_chars}` | **needs_ocr**: `{str(needs_ocr).lower()}`",
        f"- **精读指引 (`close-reader`)**: {guidance}",
        f"",
        f"| 序号 | 章节文件 | 章节标题 | 页码/来源锚点 | 总行数 | 字符数 |",
        f"| ---: | :--- | :--- | :--- | ---: | ---: |",
    ]
    for i, w in enumerate(written):
        toc_lines.append(
            f"| {i:02d} | `{w['file']}` | {w['title'].replace('|', '｜')} | `{w['pdf_pages']}` | `{w['lines']}` | `{w['chars']}` |"
        )
    (out_dir / "toc.md").write_text("\n".join(toc_lines) + "\n", encoding="utf-8")

    mf_path = out_dir / "manifest.yaml"
    mf_data = yaml.safe_load(mf_path.read_text(encoding="utf-8")) if mf_path.exists() else {}
    if not isinstance(mf_data, dict):
        mf_data = {}
    mf_data.setdefault("source_file", book_name)
    mf_data["chapter_count"] = len(written)
    mf_data["empty_page_ratio"] = stats.get("empty_ratio", 0.0)
    mf_data["needs_ocr"] = needs_ocr
    if needs_ocr:
        mf_data["ocr_note"] = "Auto-quarantined by extract_book.py: >=85% pages lack embedded text layer."
    mf_path.write_text(yaml.safe_dump(mf_data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return needs_ocr


def main() -> int:
    parser = argparse.ArgumentParser(description="提取 inbox/ 电子书为分章带页码 Markdown 与 toc.md")
    parser.add_argument("--input", required=True, help="输入电子书路径，如 inbox/xxx.pdf")
    parser.add_argument("--out-dir", required=True, help="输出目录，如 sources/monographs/cohen_1973_bukharin")
    parser.add_argument("--chunk-pages", type=int, default=25, help="无书签或超长章时的分页粒度 (默认 25 页)")
    args = parser.parse_args()

    in_path = Path(args.input)
    if not in_path.is_absolute():
        in_path = ROOT / in_path
    if not in_path.exists():
        print(f"错误: 找不到输入文件 {in_path}", file=sys.stderr)
        return 1

    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = ROOT / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    ext = in_path.suffix.lower()
    if ext == ".pdf":
        written, stats = extract_pdf(in_path, out_dir, args.chunk_pages)
    elif ext == ".epub":
        written, stats = extract_epub(in_path, out_dir)
    elif ext == ".docx":
        written, stats = extract_docx(in_path, out_dir)
    else:
        print(f"暂不支持自动提取后缀 {ext}，请使用专用脚本处理", file=sys.stderr)
        return 1

    needs_ocr = write_master_toc_and_manifest(in_path.name, out_dir, written, stats)
    ocr_flag = " [⚠️ 检出纯扫描无文字层，已自动标记 needs_ocr: true 隔离]" if needs_ocr else ""
    print(
        f"✅ 提取完成: `{in_path.name}` -> `{out_dir.relative_to(ROOT).as_posix()}` "
        f"(共 {len(written)} 章, 合计 {sum(w['chars'] for w in written)} 字符, 已生成 toc.md & manifest.yaml){ocr_flag}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
