<img src="assets/icon.svg" width="64" height="64" alt="">

# 俄国革命多层级知识库（1860s 早期民粹派 — 1929 斯大林击败布哈林）

本工作区是一个面向历史学与社会科学深度研究的**多层级俄国革命知识库与双模态史学研究平台**，时间跨度覆盖 **1861 年农奴制改革与早期民粹派运动直至 1929 年底斯大林击败布哈林集团（“大转变”与全盘集体化定局）**。

- **对外史学分析与专题写作模态（模态 A，默认面向读者）**：后台静默运行 `python scripts/kb.py pack <ID...>` 动态编译去重 1-Hop 防偏斜上下文包并检索 L3 微距卷、定量序列、精读札记与多语种原典；前台彻底隐藏一切数据库标签与机器黑话，**默认采用冷静、克制、严谨深入的专业学术史分析文风（`模态 A1`，严禁小说式脑补与廉价戏剧化煽情），亦支持按需切换至克制纪实叙事体（`模态 A2`）**，出处统一折叠于文末 `<details>`。
- **对内建库与多 Agent 编排模态（模态 B）**：由总编排者协同 6 个职责与写目录严格隔离的专职子 Agent（提取、精读、外网侦察、编年、图谱、异源 Defect-Only 对抗审计），持续消化馆藏专著与解密档案。

---

## 当前馆藏与知识图谱规模

- **四级双历法时间线（`timeline/`）**：1 个 L0 十阶段总览 + 114 节点 L1 骨干大事记 + **10 卷 L2 分期月度编年（`E01–E10` 全覆盖）** + **28 卷 L3 逐日/逐时风暴眼微距卷** + **731 条**经俄历/公历数学核验的 `events_ledger.jsonl` 原子事件。
- **三层防偏斜卡片与概念系谱（`cards/` & `glossary/`）**：共 **192 张实体卡 + 23 张史学争鸣母题卡（合计 215 张核心卡，100% 全部达成 `multi-perspective` 多视角交叉核验定稿，100% 具备标准 `### 2.2` 时效关系边表，0 draft）**，配套 27 概念跨期语义裂变排雷总表（[`glossary/CONCEPT_GENEALOGY_INDEX.md`](./glossary/CONCEPT_GENEALOGY_INDEX.md)）。
- **多元史学争鸣与原子论断库（`historiography/` & `reading-notes/`）**：累计 **764 个** 校验通过的卡片/争鸣母题（`DEB-*`）/学者档案（`SCH-*`，共 168 张，全部遵守 `[T1] ≤ 150` 字）/带原文直引页码锚点的原子论断卡（`CLM-*`，共 381 张）、**132 份** 全文精读札记与外网文献简报、**40 份** 跨模型家族异源对抗审计报告（`audits/`，含 `AUD-23A..D`、`AUD-24`、`AUD-25`，P0/P1 100% 闭环清零），配套 **1,623 条** 100% 源自卡片 `### 2.2` 单一真源的时效有向关系边（0 悬空 Stub、0 僵尸引导边）、**9 份** 定量微序列档案（`data/DATA-01..09`）、**207 篇** 多语种 S/A/B 级在线原典与史学专栏（`sources/web-archive/`）、支持中英俄期刊论文入库的 [`sources/articles/`](./sources/articles/) 管线（已入库 **79 篇**中/英/俄核心期刊论文），以及 **204 部** 已拆解分章的本地专著、辞书与速记档案汇编（`25` 部一手原典 + `179` 部学术专著/辞书，连同 79 篇期刊论文合计 **283 部/篇 100%** 全部具备完整可读纯文本并同 207 篇在线文献一并纳入 SQLite FTS5 索引，`needs_ocr` 空扫隔离 0 部，详见 [`sources/LITERATURE_CATALOG.md`](./sources/LITERATURE_CATALOG.md)）。

---

## 核心导航入口

| 模块 | 路径 | 说明 |
| :--- | :--- | :--- |
| **独立顺读专题专著层（不提问直接通读）** | [`reader/`](./reader/README.md) / [`reader/SPEC.md`](./reader/SPEC.md) | 四编十五章《俄国革命与早期苏维埃体制（1861–1929）》高可读学术读本（手动无状态编译、正文与考证尾注分流） |
| **通用框架子模块与项目配置** | [`framework/`](./framework/README.md) / [`kb_config.yaml`](./kb_config.yaml) | 可复用于一般历史学与社会学研究的通用知识库引擎、方法论文档与一键脚手架 |
| **双模态交互总则与编排规范** | [`AGENTS.md`](./AGENTS.md) / [`.opencode/agents/`](./.opencode/agents/) | 对外讲史文风规范、6 大专职 Subagent 角色权限边界与五大史学铁律 |
| **跨 Provider 模型路由表** | [`docs/MODEL_ROUTING.md`](./docs/MODEL_ROUTING.md) / [`config/agent_models.json`](./config/agent_models.json) | Antigravity / Codex / Grok / OpenCode 分层调度矩阵 |
| **方法论与架构设计** | [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md) | 四级双历法时间线、反 N+1 偏斜图谱机制、暂缓向量化原则 |
| **标准卡片与论断模板** | [`docs/TEMPLATES.md`](./docs/TEMPLATES.md) | `[T1]/[T2]/[T3]` 卡片、争鸣母题卡与原子论断卡规范 |
| **概念系谱与反讽排雷总表** | [`glossary/CONCEPT_GENEALOGY_INDEX.md`](./glossary/CONCEPT_GENEALOGY_INDEX.md) | 27 个核心概念在 1860s–1929 七个时段的语义漂移与误读排雷 |
| **定量经济与政治微序列** | [`data/`](./data/) | 罢工选票、剪刀差指数、涅姆奇诺夫表五重批判、契卡—OGPU 统计与集体化跃升 |
| **L0–L3 多尺度时间线** | [`timeline/L0_macro_epochs.md`](./timeline/L0_macro_epochs.md) | L0 十阶段 → L1 骨干大事 → L2 十卷分期脉络 → L3 二十八卷微距编年 |
| **全量文献总目** | [`sources/LITERATURE_CATALOG.md`](./sources/LITERATURE_CATALOG.md) | 全库 204 部专著/档案 + 79 篇三语核心期刊论文（283 项 100% 可读纯文本）、207 篇在线文献总目 |
| **待寻电子书愿望单** | [`BIBLIOGRAPHY_WISHLIST.md`](./BIBLIOGRAPHY_WISHLIST.md) | 剩余待补分卷与残损底本替换提醒 |
| **自动化基准评测门禁** | [`benchmarks/README.md`](./benchmarks/README.md) | `B1–B5` 五大反古德哈特基准套件（含故障注入与模态 A 长文实测） |

---

## 本地管理与评测 CLI（`scripts/kb.py` & `benchmarks/run_benchmarks.py`）

```powershell
# 1. 俄历 (O.S.) 与公历 (N.S.) 精确双向换算（自动区分19世纪+12天与20世纪+13天）
python scripts/kb.py date 1881-03-01 --from os
python scripts/kb.py date 1917-10-25 --from os

# 2. 全库史料章节级 FTS5 定位雷达（支持中/英/俄及双字高频词，自动隔离 needs_ocr 空扫书）
python scripts/kb.py locate-chapters "乌格拉诺夫" --top 8

# 3. 动态编译单卡或多卡去重 1-Hop 防偏斜平衡上下文包（100% 保留邻居、时段与 CLM/SCH 锚点）
python scripts/kb.py pack PER-bukharin PER-stalin PER-uglanov

# 4. 单进程同步译名表与 2.2 时效边表并执行全库外键/双历法体检
python scripts/sync_graph_and_packs.py

# 5. 运行 B1–B5 健康度检查与全套基准回归门禁
python benchmarks/run_benchmarks.py check-health
python benchmarks/run_benchmarks.py run --save-baseline latest_snapshot
```
