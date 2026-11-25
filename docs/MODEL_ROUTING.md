# 三层算力预算与复杂度调度策略（Declarative Model Routing Policy）

本文档定义本工作区的**声明式、客户端无关**模型路由策略。角色规范存放在 [`agents/`](../agents/)；模型与 Provider 实例名不再写死在 Python 脚本中，而是由主控官在当前宿主运行时（**Paseo**、**T3 Code** 等）动态发现可用池后原生调用。

---

## 一、三层全局调度原则（订阅优先 · 稀缺保护 · 自动分流）

### 1. 第一顺位：日常订阅主力层（默认优先）
平时所有常规提取、整章精读、外网检索、编年织网、建卡与交叉审计，优先消耗当前可用订阅池中的常规主力模型：
- **OpenAI / Codex 常规池**：`gpt-6.2-sol`、`gpt-6.1-sol`、`gpt-6.1-terra`、`gpt-6-luna`
  - *保护规则*：**`gpt-6.2-astra` / `gpt-6-astra` 留作极复杂攻坚王牌**，不用于日常普通任务。
- **xAI / Grok 池**：`grok-4.7`、`grok-4.7-build-fast`（外网侦察与异源挑战主力）。
- **Antigravity 常规池**：`claude-sonnet-5-5`、`gemini-4-neon`、`gemini-4-hydrogen`、`gemini-4-argon`、`gemini-3.8-flash`
  - *保护规则*：**`claude-opus-5-5` 配额稀少**，严禁用于普通日常任务，专留给极复杂攻坚或核心大卡终审。

### 2. 尖峰升级：极复杂任务攻坚层
仅当遇到**理论极度艰深、多源史料严重冲突的逐时考证、横跨近七十年的概念系谱重构、或核心枢纽大卡终极审计**时，精准启用：
1. **`gpt-6.2-astra`**（高/超高推理）
2. **`claude-opus-5-5`**（稀缺配额）
3. **`gemini-4-carbon`**（高思考）

### 3. 跨池分流兜底层（限流 / 窗口触顶 / 余额耗尽时自动接管）
当任一订阅池返回限流、5h 窗口上限或配额耗尽错误时，立即切换至其余尚有余量的可用池：
- **简单/常规任务**（章节切分、目录生成、元数据提取、单点日期入账、格式核验、基础检索）：优先 **`gemini-3.8-flash`**（高思考）或 **`gpt-6-luna`**（中思考）。
- **复杂任务**（整章精读、论断提炼、多流派争鸣卡片编纂、史学对勘审计）：优先 **`gemini-4-argon`** 或 **`gemini-4-neon`**（高思考），极高难度再升级至 **`gemini-4-carbon`**。

---

## 二、六大 Agent 角色能力倾向速查表

| 角色 ID | 🟢 日常主力倾向 | 🔴 极复杂攻坚倾向 | 🟡 跨池分流倾向 |
| :--- | :--- | :--- | :--- |
| **`source-extractor`**<br>原文提取与规整官 | `gpt-6-luna` / `gemini-4-argon` | `gpt-6.2-astra` | 简：`gemini-3.8-flash`<br>繁：`gemini-4-argon` |
| **`close-reader`**<br>全文精读与论断提炼官 | `claude-sonnet-5-5` / `gemini-4-hydrogen` / `gpt-6.1-sol` | `claude-opus-5-5` *(稀缺)* / `gpt-6.2-astra` / `gemini-4-carbon` | 简：`gemini-3.8-flash`<br>繁：`gemini-4-argon` |
| **`web-scout`**<br>外网史料与学术侦察官 | `grok-4.7` / `grok-4.7-build-fast` / `claude-sonnet-5-5` | `gemini-4-carbon` / `gpt-6.2-astra` | 简：`gemini-3.8-flash`<br>繁：`gemini-4-argon` |
| **`chronicle-weaver`**<br>多尺度编年史官 | `gpt-6.2-sol` / `claude-sonnet-5-5` | `gpt-6.2-astra` (`xhigh`) | 简：`gemini-3.8-flash`<br>繁：`gemini-4-argon` |
| **`graph-curator`**<br>知识图谱与卡片策展官 | `claude-sonnet-5-5` / `gemini-4-neon` / `gpt-6.1-terra` | `claude-opus-5-5` *(稀缺)* / `gpt-6.2-astra` / `gemini-4-carbon` | 简：`gemini-3.8-flash`<br>繁：`gemini-4-argon` |
| **`dialectic-auditor`**<br>史学史对勘与审计官 *(须异源)* | `gpt-6.2-sol` (`xhigh`) / `grok-4.7` (`xhigh`) / `claude-sonnet-5-5` / `gemini-4-neon` | `claude-opus-5-5` *(稀缺)* / `gpt-6.2-astra` (`xhigh`) / `gemini-4-carbon` | 简：`gemini-3.8-flash`<br>繁：`gemini-4-argon` |

---

## 三、宿主运行时原生派发对照（客户端自适配）

派发子 Agent 时，主控官在任务提示词开头要求子 Agent **先读取并遵守 `agents/<role>.md`**（或直接嵌入其写目录围栏与禁令），再按当前客户端原生调用：

| 宿主客户端 | 发现可用模型 | 派发工具 | 免审批 / 后台收尾要点 |
| :--- | :--- | :--- | :--- |
| **Paseo** | `list_profiles` / `list_providers` / `list_models` / `inspect_provider` | `create_agent`（配合 `send_agent_prompt`） | `antigravity` / `codex` 设 `settings.modeId = "full-access"`；`grok` 设 `settings.features = { "auto_accept": true }`；后台波次可设 `background: true`，结束后 `archive_agent` 归档 |
| **T3 Code** | 宿主已配置 Provider 实例列表 | `delegate_task` | 按 T3 实际实例名（如 `codex` / `grok` / `antigravity_2`）与原生推理选项直接传入 |
| **其他客户端** | 宿主原生配置 | 宿主原生子 Agent 工具 | 保持写目录围栏与异源交叉审计铁律不变，任务后统一 `git status / git diff` 验尸 |
