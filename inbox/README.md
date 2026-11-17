# 文献投递箱（`inbox/`）使用说明

请将您找到的任何与俄国革命（1860s–1929）相关的电子书、论文或档案文件直接放入本目录。

## 支持格式与语种
- **格式**：`PDF`（文字版或扫描版均可）、`EPUB`、`DOCX`、`TXT`、`HTML`、`MD`。
  - *提示：若是 `.djvu` 或 `.mobi/.azw3` 格式，若您手头方便转为 `.pdf` 或 `.epub` 最佳；若直接放入原格式，`source-extractor` 也会尝试用本地 Python 工具链转换。*
- **语种**：**中文、英文、俄文（Русский）** 均完全支持，德文/法文史料亦可直接投递。

## 命名建议（非强制）
随意保留原始下载文件名即可！如果方便带上 [`BIBLIOGRAPHY_WISHLIST.md`](../BIBLIOGRAPHY_WISHLIST.md) 中的编号（例如 `BIB-020_Cohen_Bukharin.pdf`），识别会更快；即使文件名是乱码或俄文缩写，`source-extractor` 也会读取扉页与版权页自动核验版本信息。

## 投递后流程
放入文件后，只需在对话中告诉我（例如：“我往 inbox 放了科恩的布哈林传和文图里的书”），我会自动编排：
1. `source-extractor`：提取全文至 `sources/`，保留纸书页码锚点 `[p. xx]`，生成章节行号目录 `toc.md`，更新书单状态；
2. `close-reader`：按研究优先级整章精读，产出阅读札记与原子论断卡 `CLM-*`；
3. `chronicle-weaver` & `graph-curator`：同步充实多级时间线与防偏斜知识卡片图谱。
