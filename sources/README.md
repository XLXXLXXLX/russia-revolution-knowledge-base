# 史料与文献目录导航（`sources/`）

- **全量文献总目**：[`sources/LITERATURE_CATALOG.md`](./LITERATURE_CATALOG.md)（完整收录 `sources/primary/` **24 部**一手档案与原典、`sources/monographs/` **178 部**学术专著与回忆录、[`sources/articles/`](./articles/) 中英俄同行评议期刊论文库、[`sources/web-archive/`](./web-archive/) **49 篇**多语种 S/A 级在线文献，以及 `inbox/` 本地文献库存；当前已拆解 **202 部**馆藏文献 **100% 全部具备完整可检索纯文本**，`needs_ocr` 空扫待处理数为 **0**）。
- **待寻核心文献与多语种论文清单**：[`../BIBLIOGRAPHY_WISHLIST.md`](../BIBLIOGRAPHY_WISHLIST.md)（追踪待补档案分卷、专著及高优先级中/英/俄学术期刊论文补盲方向）。
- **公开在线档案与开放获取论文库导航**：[`sources/WEB_REPOSITORIES.md`](./WEB_REPOSITORIES.md)。
- **原始文献库存快照**：[`sources/inbox_inventory.jsonl`](./inbox_inventory.jsonl)（含文件体积与完整性巡检标签）。

## 子目录职责与提取规范
- `sources/primary/`：经 `scripts/extract_book.py` 规整的一手原始文献（联共中央全会速记记录 DjVu `TXTz` 全文、法令、文集、书信、报刊、当事人在场记录，`S级`）。
- `sources/monographs/`：经 `scripts/extract_book.py` 分章提取并附带 `manifest.yaml` 与 `toc.md` 的史学专著与回忆录（`A级/B级`；纯扫描无文字层文件自动标记 `needs_ocr: true` 并从检索索引隔离）。
- `sources/articles/`：经 `scripts/extract_book.py` 提取的**中、英、俄语同行评议期刊论文与专题考证文章**（`A级`，详见 [`sources/articles/README.md`](./articles/README.md)，与专著同等纳入 SQLite FTS5 `locate-chapters` 三语检索雷达，适合针对微观制度、地方档案与具体任免/统计口径做精准补盲）。
- `sources/web-archive/`：由 `web-scout` 从公开互联网一级数字档案站与开放获取学术平台抓取固化的多语种 S/A 级文献。
