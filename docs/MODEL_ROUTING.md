# T3 Code 全模型实测连通性报告与最终绑定矩阵

本文档记录了对工作区候选模型池（21 个原列模型 + 2 个 Cursor 补测模型，共 **23 个跨 Provider 模型入口**）逐一派发真实文献小任务的实测结果，并据此锁定最终生产级模型绑定表（同步写入 [`config/agent_models.json`](../config/agent_models.json)）。

---

## 一、23 个模型实测连通性总表（17 通 / 6 剔除）

| 序号 | Provider | 模型 ID | 实测状态 | 完成的实战小任务产出 / 失败原因 |
| :--- | :--- | :--- | :---: | :--- |
| M01 | `codex` | `gpt-6-luna` | ✅ **调通** | 生成 `inbox/` 前30本书分拣表 `sources/inbox_triage_part1.md` |
| M02 | `codex` | `gpt-6.1-sol` | ✅ **调通** | 精读拉比诺维奇开篇 `reading-notes/RN-01-rabinowitch-opening.md` |
| M03 | `codex` | `gpt-6-astra` | ✅ **调通** | 创建马尔托夫人物卡 `cards/people/PER-martov-l.md` |
| M04 | `codex` | `gpt-6.1-terra` | ✅ **调通** | 创建“工农结合”概念系谱卡 `cards/concepts/CON-smychka.md` |
| M05 | `cursor` | `claude-sonnet-5-5` | ❌ **剔除** | Cursor 周额度限制：`not included in your weekly usage`（改走 `antigravity_2`） |
| M06 | `cursor` | `claude-opus-5-5` | ❌ **剔除** | Cursor 周额度限制（改走 `antigravity_2`） |
| M07 | `cursor` | `claude-fable-5-2` | ❌ **剔除** | Cursor 周额度限制 |
| M08 | `cursor` | `kimi-k3` | ❌ **剔除** | Cursor 周额度限制 |
| M09 | `cursor` | `glm-5p3` | ❌ **剔除** | Cursor 周额度限制 |
| P01 | `cursor` | `grok-4.7` *(500k, 补测)* | ✅ **调通** | 精读萨哈罗夫《在十字路口(1921-1929)》`reading-notes/RN-02-sakharov-crossroads.md` |
| P02 | `cursor` | `composer-2.5` *(补测)* | ✅ **调通** | 秒级精读托洛茨基《俄国革命史》俄文版前言 `reading-notes/RN-03-trotsky-preface.md` |
| M10 | `grok` | `grok-4.7` | ✅ **调通** | 考证布哈林1928《经济学家札记》多语底本 `reading-notes/web-briefs/WB-01-bukharin-1928-notes.md` |
| M11 | `grok` | `grok-4.7-build-fast` | ✅ **调通** | 考证列宁1923《论合作社》口授/刊发日期与全集卷次 `reading-notes/web-briefs/WB-03-lenin-on-cooperation.md` |
| M12 | `antigravity_2` | `claude-sonnet-5-5` | ✅ **调通** | 创建普列奥布拉任斯基人物卡 `cards/people/PER-preobrazhensky.md` |
| M13 | `antigravity_2` | `claude-opus-5-5` | ✅ **调通** | 对种子卡进行严苛史学挑刺审计 `audits/AUD-01-seed-cards-review.md` |
| M14 | `antigravity_2` | `gemini-4-hydrogen` | ✅ **调通** | 精读《苏维埃共产主义的雅各宾渊源》后半部及方法论局限 `reading-notes/RN-05-jacobin-conclusion.md` |
| M15 | `opencode` | `google/gemini-4-argon` | ✅ **调通** | 逐本核验 `inbox/` 后31个PDF扉页版权页 `sources/inbox_triage_part3.md` |
| M16 | `opencode` | `deepseek/deepseek-flash` | ✅ **调通** | 提炼首批核心专著与超界隔离清单 `sources/inbox_highlights_flash.md` |
| M17 | `opencode` | `opencode/nemotron-3.5-super-vl-free` | ✅ **调通** | 提取生成萨哈罗夫专著元数据 `sources/monographs/sakharov_2012_crossroads/manifest_draft.yaml` |
| M18 | `opencode` | `google/gemini-4-hydrogen` | ✅ **调通** | 无 `grep` 顺读核验拉比诺维奇史料来源 `reading-notes/RN-06-rabinowitch-sources.md` |
| M19 | `opencode` | `deepseek/deepseek-v4-pro` | ✅ **调通** | 创建1921喀琅施塔得起义事件卡 `cards/events/EVT-1921-kronstadt.md` |
| M20 | `opencode` | `google/deep-research-max-preview-04-2026` | ❌ **剔除** | 接口类型不兼容：`refers to an agent, but was provided in the 'model' field` |
| M21 | `opencode` | `google/gemini-4-carbon` | ✅ **调通** | 原生 `subagent` 创建土地平分社卡片 `cards/organizations/ORG-chernyi-peredel.md` |

---

## 二、实测锁定后的六大角色生产模型池（100% 实测可用）

- **`source-extractor`（原文提取与规整官）**：
  1. `codex` / `gpt-6-luna`（Python 分章与页码脚本主力）
  2. `opencode` / `google/gemini-4-argon#high`（多语种 PDF 扉页与版面直读核验主力）
  3. `opencode` / `deepseek/deepseek-flash#high`（批量文本高速规整）
  4. `opencode` / `opencode/nemotron-3.5-super-vl-free#high`（YAML 元数据与视觉辅助）
- **`close-reader`（全文精读与论断提炼官）**：
  1. `antigravity_2` / `claude-opus-5-5`（深度史学专著与思想论战精读旗舰）
  2. `opencode` / `google/gemini-4-hydrogen#high`（及 `antigravity_2/gemini-4-hydrogen`，禁 grep 长章顺读主力）
  3. `codex` / `gpt-6.1-sol`（经济史定量统计与严密逻辑章节精读）
  4. `opencode` / `deepseek/deepseek-v4-pro#high`（中文马列译本与党内路线论战精读）
  5. `cursor` / `composer-2.5` + `cursor` / `grok-4.7` (500k)（高速导论/短篇精读）
- **`web-scout`（外网史料与学术侦察官）**：
  1. `grok` / `grok-4.7`（跨语种冷门一手底本与版本源流考据王牌）
  2. `grok` / `grok-4.7-build-fast`（高速日期、卷次页码与 URL 核校）
  3. `antigravity_2` / `claude-sonnet-5-5`（在线长篇一手文献清洗入库）
  4. `opencode` / `google/gemini-4-carbon#high`（日常书目排摸与书单维护）
- **`chronicle-weaver`（多尺度编年史官）**：
  1. `codex` / `gpt-6.1-sol`（L3 逐日/逐时风暴眼微距编年与双历法核对主力）
  2. `codex` / `gpt-6-astra`（日常增量编年与人物/事件卡织入）
  3. `opencode` / `deepseek/deepseek-v4-pro#high`（OpenCode 围栏台账维护）
  4. `antigravity_2` / `claude-sonnet-5-5`（长时段 L1/L2 脉络聚合）
- **`graph-curator`（知识图谱与卡片策展官）**：
  1. `antigravity_2` / `claude-sonnet-5-5`（`[T1]/[T2]/[T3]` 卡片撰写与争鸣矩阵主力）
  2. `codex` / `gpt-6.1-terra`（`CON-*` 概念系谱卡、`edges.jsonl` 重构与 `pack` 编译）
  3. `opencode` / `google/gemini-4-carbon#high`（俄/英/中译名与化名消歧）
  4. `antigravity_2` / `claude-opus-5-5`（重大史学公案 `DEB-*` 顶层综合）
- **`dialectic-auditor`（史学史对勘与反偏见审计官 — 异源交叉审计）**：
  1. `[Anthropic系]` `antigravity_2` / `claude-opus-5-5`
  2. `[OpenAI系]` `codex` / `gpt-6.1-sol` (`xhigh`)
  3. `[xAI系]` `grok` / `grok-4.7` (`xhigh`)
  4. `[DeepSeek系]` `opencode` / `deepseek/deepseek-v4-pro#max`
