<img src="assets/icon.svg" width="64" height="64" alt="">

# 俄国革命多层级知识库（1860s 早期民粹派 — 1929 斯大林击败布哈林）

本工作区是一个面向历史学与社会科学深度研究的**多 Agent 协同知识库**。由主会话担任**总编排者（Orchestrator）**，协同 6 个权限与职责严格隔离的专职子 Agent，系统梳理从 19 世纪六七十年代民粹派运动兴起、1905 与 1917 革命、内战、新经济政策，直至 1929 年斯大林在党内决战中击败布哈林集团的完整历史进程与学术争鸣。

---

## 核心导航入口

| 模块 | 路径 | 说明 |
| :--- | :--- | :--- |
| **编排总纲与角色定义** | [`AGENTS.md`](./AGENTS.md) / [`.opencode/agents/`](./.opencode/agents/) | 6 大专职 Subagent 角色分工、权限边界与五大史学铁律 |
| **跨 Provider 模型绑定表** | [`docs/MODEL_ROUTING.md`](./docs/MODEL_ROUTING.md) / [`config/agent_models.json`](./config/agent_models.json) | 盘点 T3 Code 5 大可用 Provider（Codex / Cursor / Grok / Antigravity / OpenCode）并为每类 Agent 绑定专属模型池 |
| **方法论与架构设计** | [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md) | 四级双历法时间线、反 N+1 偏斜图谱机制、延迟向量化路线图 |
| **标准卡片与论断模板** | [`docs/TEMPLATES.md`](./docs/TEMPLATES.md) | 人物/组织/事件/会议/概念/制度卡、争鸣母题卡与原子论断卡规范 |
| **待寻电子书需求清单** | [`BIBLIOGRAPHY_WISHLIST.md`](./BIBLIOGRAPHY_WISHLIST.md) | **您找书的对照表**：找到电子版直接丢入 [`inbox/`](./inbox/) 即可 |
| **公开互联网档案导航** | [`sources/WEB_REPOSITORIES.md`](./sources/WEB_REPOSITORIES.md) | MIA（俄/英/中）、IstMat、CyberLeninka、俄罗斯国家历史图书馆等入口 |
| **L0–L3 多尺度时间线** | [`timeline/L0_macro_epochs.md`](./timeline/L0_macro_epochs.md) | L0 十阶段总览 → L1 骨干大事记 → L2 月度脉络 → L3 逐日/逐时微距卷 |
| **知识卡片与争鸣示范** | [`cards/`](./cards/) / [`historiography/`](./historiography/) | 已初始化 `ORG-narodnaya-volya`、`PER-bukharin`、`POL-nep` 与 `DEB-1928-bukharin-alternative` |

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
