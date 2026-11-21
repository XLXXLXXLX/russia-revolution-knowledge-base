# 同行评议学术论文与专题考证库（`sources/articles/`）

本目录专门存放覆盖 **1860s–1929 年俄国革命史** 的 **中文、英文、俄文（及法/德文）同行评议期刊论文、集刊论文与专题档案考证文章**（默认信源等级：`epistemic_tier: A`；若系当代政论或档案刊布则按实质标 `S` 或 `A`）。

## 入库与自动索引规范

1. **原始文件投递**：将 PDF / DOCX / HTML / EPUB 论文放入 `inbox/`（或子目录 `inbox/articles/`，二进制原文自动由 `.gitignore` 忽略）。
2. **统一提取与元数据生成**：
   ```powershell
   python scripts/extract_book.py "inbox/<论文文件名>.pdf" --out-dir "sources/articles/<author_year_short_slug>"
   ```
   - 自动生成 `manifest.yaml`（记录页数、语种、`epistemic_tier: "A"`、`needs_ocr` 巡检状态）与 `toc.md`（纳入 Git 索引），正文切片 `*.md` 本地保留供 `close-reader` 顺序精读并自动接入 `python scripts/kb.py locate-chapters` 三语 FTS5 检索雷达。
3. **开放获取（OA）网页全文论文**：若直接从 CyberLeninka、OpenEdition（*Cahiers du Monde russe*）等开放获取平台抓取结构化全文 Markdown，亦可按现有规范存入 `sources/web-archive/` 并在 YAML 头标注 `epistemic_tier: A`。
