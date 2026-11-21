# 同行评议学术论文与专题考证库（`sources/articles/`）

本目录专门存放覆盖 **1860s–1929 年俄国革命史** 的 **中文、英文、俄文（及法/德文）同行评议期刊论文、集刊论文与专题档案考证文章**（默认信源等级：`epistemic_tier: A`）。

## 一、核心采集方法论：以高质量专著为起点的引文顺藤摸瓜法（Monograph-Seeded Citation Chaining）

严禁在海量数据库中盲目随机搜词；获取期刊论文应坚持 **“旗舰专著参考文献/尾注挖掘 → 多专著共引（Co-citation）加权 → 定向核查下载 → 写回引文溯源边”** 四步法：

1. **挖掘旗舰专著书目与尾注**：直接扫描 `sources/monographs/` 中同行评议权威专著（如 Kotsonis 2014、McDonald 2011、Douds 2018、Allen 2003、Pirani 2008、Burds 1998、Khlevniuk 2015、Rabinowitch 2007、Hildermeier 2000 等）的 `Bibliography` 与 `Notes` 切片，提取被一流史家反复征引或重点商榷的期刊论文。
2. **优先采集三类高杠杆论文**：
   - **多部专著共同征引（Co-cited）的奠基性论文**（如 Haimson 1964–65 社会稳定性两篇原文、Fitzpatrick 1993 阶级归属建构、Engelstein 1993、Frank 1987、Weissman 1986 等）；
   - **直接填补卡片 `perspectives_missing` 或量化模型源头的原始论文**（如 Hunter & Szyrmer 1991、Hoch 2004、Plaggenborg 1990/1995、Wheatcroft 1974、Rigby 1988 等）；
   - **依托地方省市档案的微观实证论文**（如莫斯科“列宁征兆”、斯维尔德洛夫与全俄中执委、乡村通讯员运动、各省右倾事件等）。
3. **显式记录专著引文溯源（`cited_by_monographs`）**：在每篇论文的 `manifest.yaml` 中记录 `cited_by_monographs: [...]`，保留从馆藏专著到专题论文的学术脉络图谱。

## 二、入库与自动索引规范

1. **通过 `annas-mcp` 下载**：将原始 PDF 存入 `inbox/articles/<slug>.pdf`（二进制原文自动由 `.gitignore` 忽略）。
2. **统一提取与元数据生成**：
   ```powershell
   python scripts/extract_book.py --input "inbox/articles/<slug>.pdf" --out-dir "sources/articles/<slug>"
   ```
   - 自动生成 `manifest.yaml`（记录标题、作者、语种、`epistemic_tier: "A"`、`cited_by_monographs`、`needs_ocr` 状态）与 `toc.md`（纳入 Git 索引），正文切片 `*.md` 自动接入 `python scripts/kb.py locate-chapters` 三语 FTS5 检索雷达。
3. **开放获取（OA）网页全文论文**：若直接从 CyberLeninka、OpenEdition（*Cahiers du Monde russe*）等平台抓取结构化全文 Markdown，亦可存入 `sources/web-archive/` 并在 YAML 头标注 `epistemic_tier: A`。
