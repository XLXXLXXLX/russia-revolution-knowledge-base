# `reader/` 专题读本编译规范（Stateless Monograph Compilation Spec）

本目录承载俄国革命知识库的**面向读者独立顺读层（Reader-Facing Monograph Layer）**——《帝国裂解与革命锻造：俄国革命与早期苏维埃体制（1861–1929）》（四编十五章）。

与回答单点提问的“即时模态 A”不同，`reader/` 旨在为不提问的读者提供一部**兼具学术深度与高度可读性的连贯历史专著**；同时，与底层 `cards/` 的高密度图谱中间表示（IR）严格动静分离。

---

## 一、三大架构原则（防漂移、零日常负担、去校勘喧宾夺主）

### 1. 手动触发、无状态全量编译（Manual & Stateless Full Recompile）
- **日常零同步负担**：推进日常建库与审计波次（修改 `cards/`、`historiography/`、`timeline/`）时，**绝不自动改写 `reader/`**，避免每次 `git diff` 触发大模型的“近因与补丁显著性偏斜（Diff Salience Bias）”。
- **哈希脏页监测**：由 `python scripts/compile_reader.py status` 对比 `reader/build_manifest.json` 中记录的上游依赖文件 SHA-256 指纹，静默标出 `FRESH` / `STALE` / `MISSING`。
- **里程碑平铺重编译**：仅在用户手动决定更新某章时，调用 `python scripts/compile_reader.py bundle <ch_id>` 将该章关联卡片**无差别平铺打包**（完全抹除哪张卡是早期撰写、哪张卡是近期新增的时间戳痕迹），严格按 `reader/book_manifest.yaml` 预设的**分节结构与篇幅权重（Section Weight Lock）**从零编译整章（纯错别字或单点数字勘误除外，可直接人工修字后 `stamp`）。

### 2. “静默守界”与“正文—尾注双层分流”（Overcoming Textual-Criticism Bloat）
底层卡片历经数十轮对抗审计，包含大量口径排雷与防误读警示。编译 `reader/` 章节时必须执行严格的**主次分流纪律**：
- **铁律 A · 静默守界（Silent Compliance）**：
  严格区分**“遵守史实边界”**与**“在正文背诵免责声明”**。例如底层卡片警示*“出席名单列 245 名表决委员，原记录未清点精确赞成数，不得反推为 232 票”*，正文只需自然准确地写出*“联席全会以压倒多数赞成、10 票反对、3 票弃权通过决议”*——**严禁在正文中插入“尽管名单有245人但原档未记精确赞成票故不可反推为232票”之类的防御性说明**。
- **铁律 B · 正文与章末尾注（`[^1]`）物理分流**：
  - **正文层（占全章篇幅 ≥ 88%）**：只聚焦宏观结构张力、制度财政与组织运作机制、关键历史人物的行动抉择，以及主要史学流派（苏联正统派、自由派、社会史修正派、新制度/现代性学派、后苏联档案学派等）的正面解释交锋。唯一允许进入正文的数据辨析，是**本身构成重大历史转折或核心学术公案的争论**（如 1928 年斯大林援引“涅姆钦诺夫表”引发的商品粮之争）。
  - **章末考证尾注层（`## 注释与考证说明`，编号 `[^1]`–`[^8]`，占全章篇幅 ≤ 12%）**：凡属版本删改层级（如斯大林 1929 年 4 月演说三版异文）、不同文献票数或伤亡口径差异（如 1903 年崩得退场票数、喀琅施塔得两舰名册与全舰队推算边界、各方伤亡统计管道差异），若确有学术交代价值，一律下沉至章末 `[^n]` 尾注，绝不打断正文叙事心流。
- **铁律 C · 编译前输入预净化（Pre-Pack Sanitizer）**：
  `scripts/compile_reader.py bundle` 在打包上下文时，自动清洗底层卡片中的建库内务语句（如 `站内实存原典文件名为…`、`编排角色：…`、`待子代理补齐…`），并将行内裸实体 ID（如 `PER-pyatakov`）自动还原为中文译名，从源头防止工程疤痕污染执笔模型。

### 3. “高可读性学术专著”语体标准（Readable Scholarly Prose）
- **标杆文风**：对标 Alexander Rabinowitch、Orlando Figes、Sheila Fitzpatrick、Stephen Kotkin 与 E. H. Carr 的成熟历史专著笔法——**既有严密的制度、财政与阶级结构分析，又有清晰克制的时空现场感、具体历史人物的处境张力与精当的一手档案原话点睛**。
- **段落与排版呼吸感**：
  - 全章正文以连贯流畅的自然段推进（列表行占比必须 `≤ 8%`，原则上正文不使用项目符号罗列）；
  - 段落长度富有节奏（平均自然段 200–380 字，避免千字密不透风的巨型段落，也避免一句话一段的碎片腔）；
  - 1918 年 2 月改历前日期采用自然中文表述（如“1917 年俄历 10 月 25 日（公历 11 月 7 日）”，同一小节内上下文已明示俄历时可自然简写，不堆砌机器代码标签）；
  - **零机器黑话与零行内卡片链接**：正文与尾注严禁出现 `[T1]/[T2]/[T3]`、`CLM-*`、`PER-*`、`[O.S.]/[N.S.]` 等内部工程符号；全章末尾统一附一个干净的 `<details><summary>附：本章依托的核心档案与延伸阅读索引</summary>...</details>` 供读者按需下钻底层卡片、定量表与精读札记。

---

## 二、手动编译与验收工作流（CLI Reference）

```powershell
# 1. 查看全书 15 章当前状态、字数、卫生分与上游卡片变更（FRESH / STALE / MISSING）
python -X utf8 scripts/compile_reader.py status

# 2. 为指定章节生成无状态、已预脱敏的编译载荷包（供执笔子 Agent 顺读撰写）
python -X utf8 scripts/compile_reader.py bundle ch09 --out <bundle_path.md>

# 3. 对已生成的章节运行自动化门禁校验（反黑话泄漏、反防御补丁腔、列表率、尾注占比、B4陷阱扫描）
python -X utf8 scripts/compile_reader.py verify ch09
python -X utf8 scripts/compile_reader.py verify --existing

# 4. 人工/主会话审校通过后，写入当前上游卡片 SHA-256 指纹快照（标记为 FRESH）
python -X utf8 scripts/compile_reader.py stamp ch09
```
