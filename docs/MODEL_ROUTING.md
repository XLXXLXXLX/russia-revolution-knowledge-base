# 三层算力预算与复杂度调度策略（Model Routing & Quota Policy）

本文档定义本工作区的模型调度优先级准则，机器可读配置位于 [`config/agent_models.json`](../config/agent_models.json)，可通过 `python scripts/kb.py models` 或 `python scripts/kb.py delegate-prompt <role> --tier <tier> --task "..."` 调用。

---

## 一、三层全局调度铁律（严守订阅优先与稀缺配额保护）

### 1. 第一顺位：日常订阅主力池（`--tier subscription` — 默认优先消耗！）
平时所有常规提取、整章阅读、外网检索、编年织网、建卡与交叉审计，**一律优先调用以下三大订阅制 Provider 的常规主力模型**：
- **`codex`（GPT 订阅常规池）**：`gpt-6.1-sol`、`gpt-6.1-terra`、`gpt-6-luna`
  - *保护规则*：**`gpt-6-astra` 留作极复杂任务王牌**，不用于日常普通任务。
- **`grok`（Grok 订阅池）**：`grok-4.7`、`grok-4.7-build-fast`（及同为订阅内含的 `cursor/composer-2.5`、`cursor/grok-4.7`）。
- **`antigravity_2`（Antigravity 订阅常规池）**：`claude-sonnet-5-5`、`gemini-4-hydrogen`、`gemini-4-argon`、`gemini-3.8-flash`
  - *保护规则*：**`antigravity_2` 中的 `claude-opus-5-5` 配额稀少**，严禁用于普通日常任务，专留给极复杂攻坚或核心大卡终审！

### 2. 尖峰升级：极复杂任务攻坚池（`--tier apex` — 额度未耗尽但遇硬骨头时启用！）
仅当遇到**理论极度艰深、多源史料严重冲突的逐时考证、横跨近七十年的概念系谱重构、或核心枢纽大卡终极审计**时，才精准启用以下三大攻坚王牌：
1. **`codex` / `gpt-6-astra`** (`reasoningEffort: "high" | "xhigh"`)
2. **`antigravity_2` / `claude-opus-5-5`** (`thinking_level: "high"`，少量稀缺配额)
3. **`opencode` / `google/gemini-4-carbon#high`**（OpenCode 中的 Gemini API Carbon）

### 3. 降级兜底：订阅额度耗尽接管池（`--tier fallback-simple` / `fallback-complex`）
当上述 GPT / Grok / Antigravity 订阅额度耗尽（返回限流或配额耗尽提示）时，平滑切换至 **`opencode`**：
- **简单/常规任务**（`--tier fallback-simple`：章节切分、目录生成、元数据提取、单点日期入账、格式核验、基础检索）
  👉 统一使用 **`opencode` / `deepseek/deepseek-flash#high`**（即 **DeepSeek V4.1 Flash 1017 / `ds4.1f`**）。
- **复杂任务**（`--tier fallback-complex`：整章精读、论断提炼、多流派争鸣卡片编纂、史学对勘审计）
  👉 优先使用 **`opencode` / `google/gemini-4-argon#high`**；仅在难度极高、Argon 仍不足以驾驭时，升级动用 **`opencode` / `google/gemini-4-carbon#high`**。

---

## 二、六大 Agent 角色三层绑定速查表

| 角色 ID | 🟢 日常订阅主力 (`subscription`) | 🔴 极复杂攻坚 (`apex`) | 🟡 额度耗尽兜底 (`fallback`) |
| :--- | :--- | :--- | :--- |
| **`source-extractor`**<br>原文提取与规整官 | • `codex / gpt-6-luna`<br>• `antigravity_2 / gemini-4-argon` *(或 `3.8-flash`)* | • `codex / gpt-6-astra` | • 简单：`opencode / deepseek-flash#high` (`ds4.1f`)<br>• 复杂：`opencode / gemini-4-argon#high` |
| **`close-reader`**<br>全文精读与论断提炼官 | • `antigravity_2 / claude-sonnet-5-5`<br>• `antigravity_2 / gemini-4-hydrogen`<br>• `codex / gpt-6.1-sol` | • `antigravity_2 / claude-opus-5-5` *(稀缺)*<br>• `codex / gpt-6-astra`<br>• `opencode / gemini-4-carbon#high` | • 简单：`opencode / deepseek-flash#high` (`ds4.1f`)<br>• 复杂：`opencode / gemini-4-argon#high` *(极难升 `carbon`)* |
| **`web-scout`**<br>外网史料与学术侦察官 | • `grok / grok-4.7`<br>• `grok / grok-4.7-build-fast`<br>• `antigravity_2 / claude-sonnet-5-5` | • `opencode / gemini-4-carbon#high`<br>• `codex / gpt-6-astra` | • 简单：`opencode / deepseek-flash#high` (`ds4.1f`)<br>• 复杂：`opencode / gemini-4-argon#high` *(极难升 `carbon`)* |
| **`chronicle-weaver`**<br>多尺度编年史官 | • `codex / gpt-6.1-sol`<br>• `antigravity_2 / claude-sonnet-5-5` | • `codex / gpt-6-astra` (`xhigh`)<br>• `opencode / gemini-4-carbon#high` | • 简单：`opencode / deepseek-flash#high` (`ds4.1f`)<br>• 复杂：`opencode / gemini-4-argon#high` *(极难升 `carbon`)* |
| **`graph-curator`**<br>知识图谱与卡片策展官 | • `antigravity_2 / claude-sonnet-5-5`<br>• `codex / gpt-6.1-terra` | • `antigravity_2 / claude-opus-5-5` *(稀缺)*<br>• `codex / gpt-6-astra`<br>• `opencode / gemini-4-carbon#high` | • 简单：`opencode / deepseek-flash#high` (`ds4.1f`)<br>• 复杂：`opencode / gemini-4-argon#high` *(极难升 `carbon`)* |
| **`dialectic-auditor`**<br>史学史对勘与审计官 | • `codex / gpt-6.1-sol` (`xhigh`)<br>• `grok / grok-4.7` (`xhigh`)<br>• `antigravity_2 / claude-sonnet-5-5` | • `antigravity_2 / claude-opus-5-5` *(稀缺)*<br>• `codex / gpt-6-astra` (`xhigh`)<br>• `opencode / gemini-4-carbon#high` | • 简单：`opencode / deepseek-flash#high` (`ds4.1f`)<br>• 复杂：`opencode / gemini-4-argon#high` *(极难升 `carbon`)* |

---

## 三、前期实测已剔除的不可用条目备忘
- `cursor` 下的 `claude-opus-5-5` / `claude-sonnet-5-5` / `claude-fable-5-2` / `kimi-k3` / `glm-5p3`（周额度不含）；`cursor` 下仅 `composer-2.5` 与 `grok-4.7` 可作为轻量辅助。
- `opencode` 下的 `google/deep-research-max-preview-04-2026`（Agent 专用接口，非对话模型）。
