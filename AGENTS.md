# 俄国革命知识库（1860s–1929）编排总纲与工作区规范

本工作区是一个面向严肃历史与社会科学研究的**俄国革命多层级知识库**，时间跨度覆盖**早期民粹派运动（1860s–1870s）直至 1929 年斯大林击败布哈林集团（“大转变”定局）**。

主会话 Agent 担任 **总编排者（Chief Historiographical Orchestrator）**，不包揽繁重的底层搬运与孤立检索，而是积极将任务拆解并分派给 `.opencode/agents/` 下的专职子 Agent 并行协作。

---

## 一、角色分工与跨 Provider 多模型分派准则（Orchestration Roster）

本工作区同时接入 T3 Code 当前启用的 **5 大模型 Provider**（`codex`、`cursor`、`grok`、`antigravity_2`、`opencode`），机器可读绑定表位于 `config/agent_models.json`，完整盘点见 `docs/MODEL_ROUTING.md`。

| Agent ID | 角色名称 | 绑定的跨 Provider 可用模型池（主力 → 专长备选） | 写目录边界 |
| :--- | :--- | :--- | :--- |
| `source-extractor` | **原文提取与规整官** | ① `codex`: `gpt-6-luna`<br>② `opencode`: `google/gemini-4-argon#high`<br>③ `opencode`: `deepseek/deepseek-flash#high`<br>④ `opencode`: `opencode/nemotron-3.5-super-vl-free#high` | `sources/*`, `inbox/*`, `BIBLIOGRAPHY_WISHLIST.md`, `scripts/*` |
| `close-reader` | **全文精读与论断提炼官**<br>*(禁 grep/shell/web)* | ① `antigravity_2`: `claude-opus-5-5`<br>② `opencode`: `google/gemini-4-hydrogen#high` (及 `antigravity_2` 同款)<br>③ `codex`: `gpt-6.1-sol`<br>④ `opencode`: `deepseek/deepseek-v4-pro#high`<br>⑤ `cursor`: `composer-2.5` / `grok-4.7` (500k) | `reading-notes/*`, `historiography/claims/*` |
| `web-scout` | **外网史料与学术侦察官** | ① `grok`: `grok-4.7`<br>② `grok`: `grok-4.7-build-fast`<br>③ `antigravity_2`: `claude-sonnet-5-5`<br>④ `opencode`: `google/gemini-4-carbon#high` | `sources/web-archive/*`, `sources/WEB_REPOSITORIES.md`, `reading-notes/web-briefs/*`, `BIBLIOGRAPHY_WISHLIST.md` |
| `chronicle-weaver` | **多尺度编年史官** | ① `codex`: `gpt-6.1-sol`<br>② `codex`: `gpt-6-astra`<br>③ `opencode`: `deepseek/deepseek-v4-pro#high`<br>④ `antigravity_2`: `claude-sonnet-5-5` | `timeline/*`, `cards/events/*` |
| `graph-curator` | **知识图谱与卡片策展官** | ① `antigravity_2`: `claude-sonnet-5-5`<br>② `codex`: `gpt-6.1-terra`<br>③ `opencode`: `google/gemini-4-carbon#high`<br>④ `antigravity_2`: `claude-opus-5-5` | `cards/*`, `graph/*`, `historiography/debates/*`, `historiography/scholars/*`, `glossary/*` |
| `dialectic-auditor` | **史学史对勘与审计官**<br>*(纯只读异源交叉审计)* | ① `antigravity_2`: `claude-opus-5-5`<br>② `codex`: `gpt-6.1-sol` (`xhigh`)<br>③ `grok`: `grok-4.7` (`xhigh`)<br>④ `opencode`: `deepseek/deepseek-v4-pro#max` | `audits/*` |

### 编排与跨模型调度铁律
1. **双通道择优派发**：
   - 派发至 **`codex` / `cursor` / `grok` / `antigravity_2`**（或指定跨驱动参数）时：先保证当前线程已调用过一次 `orchestrator_capabilities`，再用 `delegate_task` 传入 `config/agent_models.json` 中对应的 `target`，并在 `task` 中附带 `.opencode/agents/<role>.md` 的角色规约（可通过 `python scripts/kb.py delegate-prompt <role> --task "..."` 一键生成载荷）。
   - 派发至 **`opencode`** 绑定模型时：可直接调用原生 `subagent` 工具，自动挂载 `.opencode/agents/<role>.md` 硬权限围栏。
2. **异源模型交叉审计（Cross-Family Adversarial Audit）**：指派 `dialectic-auditor` 审计某张卡片或综述时，**必须选择与撰写该卡片的模型不同家族（Family）的模型**（如 Claude 撰写的卡片交由 GPT-6.1 或 Grok 4.7 审计），杜绝同源模型的思维定势与叙事盲区。
3. **入库与阐释分离、并行无冲突**：新书进 `inbox/` 后先派 `source-extractor` 生成章节与 `toc.md`，再派 `close-reader` 整章精读，最后由 `chronicle-weaver` 与 `graph-curator` 并行织网；缺书随时登记至 `BIBLIOGRAPHY_WISHLIST.md`。

---

## 二、五大史学与知识工程铁律

1. **双历法强制规范（Dual-Calendar Discipline）**
   - 1918 年 2 月 14 日苏俄改历之前的所有俄国本土事件，必须同时核清 **俄历（儒略历，O.S.）** 与 **公历（格里高利历，N.S.）**。
   - **换算铁律**：19 世纪（1800-03-01 至 1900-02-28）`N.S. = O.S. + 12 天`；20 世纪（1900-03-01 至 1918-01-31 O.S.）`N.S. = O.S. + 13 天`。机器排序统一使用公历 ISO 日期 `date_ns`，叙事文本写为 `1917-10-25 [O.S.] / 1917-11-07 [N.S.]`。可用 `python scripts/kb.py date` 核验。

2. **反 N+1 偏斜读取协议（Anti-Skew Context Protocol）**
   - 每张卡片严格采用三层结构：`[T1] 60秒定性微摘要`、`[T2] 核心脉络 + 带时效的关系摘要边表 + 史学争鸣槽`、`[T3] 深度考证与引文档案`。
   - 研究任一复杂节点前，优先运行或读取 `python scripts/kb.py pack <CARD_ID>` 生成的 **1-Hop 平衡上下文包**（主卡 T1+T2 + 全部一跳邻居等长 T1 微摘要 + 双向关系边实质 + 争鸣光谱 + 盲区告警），严禁随机点开两三张邻居长卡就下定论。

3. **史学流派多元并置（Historiographical Pluralism）**
   - 严禁将单一史学家或单一政治派别的叙事直接写成无主语的“客观定论”。
   - 重大争议议题必须关联 `historiography/debates/DEB-*` 争鸣卡，显式区分：**经验事实共识** vs **史家解释分歧**（如苏联正统派、托派/左翼马克思主义、西方极权主义/自由派、西方社会史修正派、新制度/地缘现代性学派、后苏联俄罗斯档案学派等）。
   - 当亲历者著作（如托洛茨基、苏汉诺夫、米留科夫、克伦斯基、布哈林）被引用时，必须区分其 **“在场见证（一手史料）”** 与 **“事后政治阐释/历史论断（二手论断）”** 双重属性。

4. **信源分级与出处可追溯（Provenance & Epistemic Tiers）**
   - `S级`：原始档案、会议速记记录、当时法令/报刊/书信原文。
   - `A级`：同行评议学术专著与期刊论文。
   - `B级`：事后回忆录、权威专业史学辞书。
   - `C级`：维基百科与普通网页——**仅作检索跳板与译名/日期初筛，严禁作为卡片论断的最终证据**。

5. **暂缓向量化原则（No Premature Vectorization）**
   - 当前阶段严禁引入向量数据库或 Chunk-RAG 工具。概念跨期漂移（如“苏维埃”“国家资本主义”“富农”在 1870–1929 间的语义裂变）与论战文本中的反讽引述必须依赖 `glossary/` 概念系谱、`graph/edges.jsonl` 显式关系与 `close-reader` 整章语境精读处理。

---

## 三、常用工具命令（`scripts/kb.py`）

- 俄历/公历精确换算：`python scripts/kb.py date 1881-03-01 --from os` 或 `python scripts/kb.py date 1917-10-25 --from os`
- 生成文献章节行号目录（供 `close-reader` 顺读）：`python scripts/kb.py toc <markdown文件路径>`
- 多层级时间线切片查询：`python scripts/kb.py timeline --max-level 2 --from 1927-01-01 --to 1929-12-31`
- 编译 1-Hop 防偏斜上下文包：`python scripts/kb.py pack <CARD_ID> --write`
- 全库一致性、断链、孤岛与史学偏斜体检：`python scripts/kb.py audit-graph`
- 查看各角色绑定的跨 Provider 模型矩阵：`python scripts/kb.py models`
- 生成跨 Provider `delegate_task` 标准角色派发载荷：`python scripts/kb.py delegate-prompt <role> --slot <slot> --task "<具体任务>"`
