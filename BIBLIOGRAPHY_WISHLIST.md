# 待寻核心电子书与一手档案补缺清单（Bibliography Wishlist v3）

> **更新状态（2026-11-20 · 第二批 16 部新书入库与 DjVu 解码后）**：
> - 本地 `inbox/` 当前共 **156 个核心文献文件（2,352.4 MB）**，已通过升级版 `scripts/extract_book.py`（支持 PDF / 逐页合并 EPUB / DOCX / 原生纯 Python DjVu `TXTz` 解码）全量规整为 `sources/primary/` **13 部** + `sources/monographs/` **150 部**（总计 **163 部**，详见 [`sources/LITERATURE_CATALOG.md`](./LITERATURE_CATALOG.md)）。
> - 原愿望单 `ADD-02`（McKean 1990）、`ADD-03`（Emmons 1968）、`ADD-04`（Swain 1996）、`ADD-05`（Scott B. Smith 2011）、`ADD-06`（Lara Douds 2018）、`ADD-07`（Simon Pirani 2008）、`ADD-08` 第3卷（《Как ломали НЭП》1928年11月全会速记，213.8万字符俄文全文）、`ADD-09`（Kotkin 2017 第2卷）、`ADD-11`（Robert C. Allen 2003）、`ADD-12`（Terry Martin 2001）以及 Ascher《斯托雷平传》(2001)、Burds《农民的梦想》(1998)、和田春树《俄国革命：彼得格勒，1917年2月》、Stites《革命的梦想》**均已成功提取入库并纳入 FTS5 章节雷达**！

---

## 一、待补齐分卷与核心缺书（4 项）

| 编号 | 优先级 | 中文译名 / 主题 | 英文/俄文原书名 | 作者/编者 | 补缺价值说明 |
| :--- | :---: | :--- | :--- | :--- | :--- |
| `WISH-01` | 🔴 P0 | 《新经济政策是如何被打破的》其余四卷（第 1、2、4、5 卷） | *Как ломали НЭП. Стенограммы пленумов ЦК ВКП(б) 1928–1929 гг.* Тома 1, 2, 4, 5 (2000) | В. П. Данилов, О. В. Хлевнюк 编 | 第 3 卷（1928年11月全会）已由 DjVu 完整提取；补齐 1928年4月/7月及 1929年4月/11月全会速记原档可实现 S 级全覆盖 |
| `WISH-02` | 🔴 P0 | 《苏维埃俄国史：一国社会主义（1924–1926）》（全三卷） | *Socialism in One Country, 1924–1926* (Vols. 1–3, 1958–1964) | E. H. Carr | 填补卡尔 14 卷本中唯一尚缺的 1924–1926 关键断代（连接已入库的 `Interregnum` 与 `Foundations`） |
| `WISH-03` | 🟠 P1 | 《1905年俄国革命（下卷：权威重建）》及上卷带文字层版 | *The Revolution of 1905: Authority Restored* (1992) & Vol. 1 OCR/EPUB | Abraham Ascher | 当前入库的上卷 PDF（1994印本）系无文字层纯扫描件（已标记 `needs_ocr: true`），建议补带文字层版本及下卷 |
| `WISH-04` | 🔵 P2 | 《1921年喀琅施塔得：布尔什维克主义的遗产》 | *Kronstadt 1917–1921: The Fate of a Soviet Democracy* (1983) | Israel Getzler | 当前库内关于两艘主力舰 94% 1918 年前老水兵统计系经 Figes 转引，补入原书可核对原始名册分母 |

---

## 二、本地 `inbox/` 残损下载文件待替换提醒（2 项，已自动隔离）

| 文件名 | 当前状态 | 诊断原因 | 建议处理 |
| :--- | :---: | :--- | :--- |
| `Telling October- Memory and the Making of the Bolshevik Revolution ... .pdf` | `needs_ocr: true` | 下载流在 `916 KB` 处截断（缺失 `%%EOF` 尾标，0 可读页） | 重新下载完整版 PDF/EPUB 覆盖 `inbox/` 同名文件后重跑 `extract_book.py` |
| `Revolution of the Mind- Higher Learning among the Bolsheviks, 1918 - 1929 ... .pdf` | `needs_ocr: true` | 下载流在 `512 KB` 处截断（缺失 `%%EOF` 尾标，0 可读页） | 重新下载 Michael David-Fox (1997) 完整版覆盖后重跑 `extract_book.py` |
