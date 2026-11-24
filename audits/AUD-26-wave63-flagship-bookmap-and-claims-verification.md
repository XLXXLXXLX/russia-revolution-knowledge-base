---
id: AUD-26-wave63-flagship-bookmap-and-claims-verification
type: audit
auditor_model: gemini-4-carbon-programmatic-slice-verifier
target_wave: W63
role: dialectic-auditor
status: remediated
updated_at: "2026-11-24"
---

# AUD-26｜Wave 63 七部旗舰专著整书导图（`BOOK-MAP-*`）与 68 张原子论断卡逐字对勘报告（Defect-Only）

- **核验对象**：按用户审定范围（剔除布哈林与斯大林政治传记，保留其余 7 部旗舰专题专著），对 `Lewin (1968)`、`Rabinowitch (1976)`、`Rabinowitch (2007)`、`S. A. Smith (1983)`、`Daniels (1960)`、`Martin (2001)`、`Hirsch (2005)` 共 **7 份**整书逐章深度导图（`BOOK-MAP-*.md`）、**68 张**新增 `CLM-*.md` 原子论断卡、新建学者卡 `SCH-hirsch-francine.md` 及同步回写的 5 张学者卡、4 张争鸣卡与 2 张实体卡进行全量逐字核验。
- **核验方法**：剥离 PDF 页眉/页码标记、Unicode 合字（`ﬁ`/`ﬂ`）与行尾断词连字符后，对全部 68 张 `CLM-*` 的 **317 个原文引述片段**执行跨切片精确子串比对，并校验 YAML 外键、改历前后双历法算术（`1918-02-14` 边界）及 1929 年底断代纪律。

## P0 / P1（已闭环修补项）

| 缺陷编号 | 严重度 | 位置 | 原缺陷描述 | 闭环修补动作 |
| :--- | :--- | :--- | :--- | :--- |
| `P0-01` | `P0` | `CLM-martin-2001-russian-resentment-and-rsfsr-asymmetry-1923-1929.md` | 第一段英文块引文将原书 `ch17_the_reemergence_of_the_russians.md#L16` 的 `"the unique threat the Russians posed to Soviet unity"` 误录为 `"the Russian nationality posed"`（多出一词） | 已回核原书第 10 章切片逐字符订正为 `"the Russians posed"`，复测 317/317 引文片段 100% 命中 |
| `P0-02` | `P0` | `CLM-lewin-peasants-1968-batrak-...`、`CLM-martin-2001-affirmative-action-...` 等 4 文 | 初次从主会话预览流归集时混入 `<truncated ... bytes>` 截断预览文本 | 已改由各子 Agent 独立完整日志（`transcript_full.jsonl`）全量重提覆盖，全库 75 份新增文件 0 截断标记 |
| `P1-01` | `P1` | `CLM-smith-sa-1983-*.md`（共 9 张） | 顶层 YAML `supports` / `rebuts` / `qualifies` 填入自由文本评述（如 `'Paul Avrich（...）'`）而非规范 `CLM-*` 外键数组 | 已将全部非 ID 学术评述无损迁入正文末节“学术对话坐标”，YAML 三字段统一归零为 `[]` |
| `P1-02` | `P1` | `CLM-rabinowitch-2007-*.md`（4 张）及 `BOOK-MAP-rabinowitch-2007` / `smith-1983` / `daniels-1960` | 存在省略年份的旧历对照（如 `1918-01-08 [O.S.] / 01-21 [N.S.]`）、单列未配对 `1917-05-30 [O.S.]` 及改历说明处的 `1918-02-01 [O.S.]` 机器标签 | 已按儒略历 `+13` 天规则补齐完整 `YYYY-MM-DD [O.S.] / YYYY-MM-DD [N.S.]`，并将改历日说明规范化为自然中文表述 |
| `P1-03` | `P1` | `SCH-rabinowitch-alexander.md` | `[T3]` 回写旧卡索引时误将 `CLM-rabinowitch-1976-open-democratic-mass-party` 简写为 `-open-mass-party` | 已核对磁盘实存全部 28 张 `CLM-rabinowitch-*` 文件名精确对齐 |
