# 史料与文献目录导航（`sources/`）

- **全量文献总目**：[`sources/LITERATURE_CATALOG.md`](./LITERATURE_CATALOG.md)（完整收录 `sources/primary/` **17 部**一手档案与原典、`sources/monographs/` **170 部**学术专著与回忆录、[`sources/web-archive/`](./web-archive/) **49 篇**多语种 S 级在线原典，以及 `inbox/` 本地电子书库存；全馆 **187 部**拆解文献 **100% 全部具备完整可检索纯文本**，`needs_ocr` 纯扫描/残卷待处理数已清零为 **0 部**）。
- **待寻核心文献愿望单**：[`../BIBLIOGRAPHY_WISHLIST.md`](../BIBLIOGRAPHY_WISHLIST.md)（持续追踪新增入库批次、剩余待补卷次与需替换残损/纯扫底本条目）。
- **公开在线档案库导航**：[`sources/WEB_REPOSITORIES.md`](./WEB_REPOSITORIES.md)。
- **原始电子书库存快照**：[`sources/inbox_inventory.jsonl`](./inbox_inventory.jsonl)（含文件体积与 `truncated_pdf_missing_eof` 完整性自动巡检标签）。

## 子目录职责与提取规范
- `sources/primary/`：经 `scripts/extract_book.py` 规整的一手原始文献（联共中央全会速记记录 DjVu `TXTz` 全文、法令、文集、书信、报刊、当事人在场记录）。
- `sources/monographs/`：经 `scripts/extract_book.py` 分章提取并附带 `manifest.yaml` 与 `toc.md` 的史学专著与论文（纯扫描无文字层或残损下载文件自动标记 `needs_ocr: true` 并从 `locate-chapters` 检索索引中隔离）。
- `sources/web-archive/`：由 `web-scout` 从公开互联网一级数字档案站抓取固化的多语种 S 级文献。
