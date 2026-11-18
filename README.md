<img src="assets/icon.svg" width="64" height="64" alt="">

# 俄国革命多层级知识库（1860s 早期民粹派 — 1929 斯大林击败布哈林）

本工作区是一个面向历史学与社会科学深度研究的**多层级俄国革命知识库与双模态史学研究平台**，时间跨度覆盖 **1861 年农奴制改革与早期民粹派运动直至 1929 年底斯大林击败布哈林集团（“大转变”与全盘集体化定局）**。

- **对外问答与专题写作模态（默认面向读者）**：后台静默调用 `graph/packs/` 1-Hop 防偏斜上下文包、L3 逐日微距卷、精读札记与多语种一手原典，前台隐藏一切数据库标签与机器黑话，输出**鲜活饱满、富有人物肌理与多学派纵深的长篇历史叙事**（出处统一折叠于文末 `<details>`）。
- **对内建库与多 Agent 编排模态**：由总编排者协同 6 个职责与写目录严格隔离的专职子 Agent（提取、精读、外网侦察、编年、图谱、异源对抗审计），持续消化馆藏专著与解密档案。

---

## 当前馆藏与知识图谱规模

- **四级双历法时间线（`timeline/`）**：1 个 L0 十阶段总览 + 114 节点 L1 骨干大事记 + **10 卷 L2 分期月度编年（`E01–E10` 全覆盖）** + **20 卷 L3 逐日/逐时风暴眼微距卷** + **612 条**经俄历/公历数学核验的 `events_ledger.jsonl` 原子事件。
- **三层防偏斜卡片与概念系谱（`cards/` & `glossary/`）**：覆盖核心人物、政党派别、党国制度、历史事件、代表大会、经济政策以及 **11 张横跨数十年的核心概念系谱卡（`CON-*`）** 与 25 概念跨期语义裂变排雷总表（[`glossary/CONCEPT_GENEALOGY_INDEX.md`](./glossary/CONCEPT_GENEALOGY_INDEX.md)）。
- **多元史学争鸣与原子论断库（`historiography/` & `reading-notes/`）**：累计 **460+ 张** 校验通过的卡片/争鸣母题（`DEB-*`）/学者档案（`SCH-*`）/带原文直引页码锚点的原子论断卡（`CLM-*`），配套 **130+ 条** 时效有向关系边与 1-Hop 上下文包、**6 份** 定量微序列档案（`data/DATA-01..06`）、**35+ 篇** 多语种 S 级一手历史文献（`sources/web-archive/`）以及 **129 部** 已拆解分章的本地专著与档案汇编。

---

## 核心导航入口

| 模块 | 路径 | 说明 |
| :--- | :--- | :--- |
| **双模态交互总则与编排规范** | [`AGENTS.md`](./AGENTS.md) / [`.opencode/agents/`](./.opencode/agents/) | 对外讲史文风规范、6 大专职 Subagent 角色权限边界与五大史学铁律 |
| **跨 Provider 模型路由表** | [`docs/MODEL_ROUTING.md`](./docs/MODEL_ROUTING.md) / [`config/agent_models.json`](./config/agent_models.json) | Antigravity Gemini Ultra 5x / Codex / Grok / OpenCode 分层调度矩阵 |
| **方法论与架构设计** | [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md) | 四级双历法时间线、反 N+1 偏斜图谱机制、延迟向量化路线图 |
| **标准卡片与论断模板** | [`docs/TEMPLATES.md`](./docs/TEMPLATES.md) | `[T1]/[T2]/[T3]` 卡片、争鸣母题卡与原子论断卡规范 |
| **概念系谱与反讽排雷总表** | [`glossary/CONCEPT_GENEALOGY_INDEX.md`](./glossary/CONCEPT_GENEALOGY_INDEX.md) | 25 个核心概念在 1860s–1929 七个时段的语义漂移与误读排雷 |
| **定量经济与政治微序列** | [`data/`](./data/) | 罢工选票、剪刀差指数、涅姆奇诺夫表五重批判、契卡—OGPU 统计与集体化跃升 |
| **L0–L3 多尺度时间线** | [`timeline/L0_macro_epochs.md`](./timeline/L0_macro_epochs.md) | L0 十阶段 → L1 骨干大事 → L2 十卷分期脉络 → L3 二十卷微距编年 |
| **待寻电子书需求清单** | [`BIBLIOGRAPHY_WISHLIST.md`](./BIBLIOGRAPHY_WISHLIST.md) | 本地 `inbox/` 205 部库存对照与少量待补卷次清单 |

---

## 本地管理 CLI（`scripts/kb.py`）

```powershell
# 1. 俄历 (O.S.) 与公历 (N.S.) 精确双向换算（自动区分19世纪+12天与20世纪+13天）
python scripts/kb.py date 1881-03-01 --from os
python scripts/kb.py date 1917-10-25 --from os

# 2. 为长篇文献生成章节行号索引（供 close-reader 在禁用 grep 下整章连续精读）
python scripts/kb.py toc docs/ARCHITECTURE.md

# 3. 按时间窗口与缩放层级查询双历法时间线
python scripts/kb.py timeline --max-level 2 --from 1921-01-01 --to 1929-12-31

# 4. 编译 1-Hop 防偏斜平衡上下文包（输出至 graph/packs/<ID>.md）
python scripts/kb.py pack PER-bukharin --write

# 5. 全库结构、双历法数学校验与待建卡片队列体检
python scripts/kb.py audit-graph
```
