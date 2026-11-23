---
id: AUD-25-wave62-claims-and-scholars-verification
type: audit
auditor_model: gemini-4-carbon-programmatic-slice-verifier
target_wave: W62B-W62D
role: dialectic-auditor
status: remediated
updated_at: "2026-11-23"
---

# AUD-25｜Wave 62B–62D 新增 38 张英俄论文论断卡与 31 张学者卡切片逐字对勘报告（Defect-Only）

- **核验对象**：`CR62B`（16 张英文 `CLM-*`）、`CR62C`（13 张英文 `CLM-*`）、`CR62D`（9 张俄文 `CLM-*`）及配套新建的 31 张 `SCH-*` 学者卡。
- **核验方法**：打开全部 38 张 `CLM-*` 指向的 `sources/articles/<slug>/ch*.md` 原始提取切片，对全部块引文（去断行连字符与省略号切分后逐段滑动窗口比对）、期刊名/卷期/页码、改历前后双历法算术、`[T1] <= 150` 非空白字符及外键进行全量校验。
- **P0（逐字引文伪造/分母硬伤）**：**0 项**（全部 38 张英俄 `CLM-*` 的 `Verbatim Quotes` 均在对应 `sources/articles/<slug>/` 切片中 100% 命中印出原文；`SCH-berk-stephen` 刊名已核定为 *Russian History* 2 (1975)，`SCH-mcdermott-kevin` 刊名已核定为 *European History Quarterly* 25:3 (1995)，全部 31 张新 `SCH-*` 的 `[T1]` 介于 115–146 字之间）。

## P2（已闭环修补项）

| 缺陷编号 | 位置 | 原缺陷描述 | 闭环修补动作 |
| :--- | :--- | :--- | :--- |
| `P2-01` | `CLM-boyd-1968-origins-of-petrograd-order-no-1.md:38-39, 43` | 缩写旧历 `03-01 [O.S.]`、`03-02 [O.S.]`、`03-05..06 [O.S.]`、`03-07 [O.S.]` 及 `2月27日至3月8日 [O.S.]` 同行未并列 `+13` 公历孪生 | 已全部补齐完整双历对（`03-14`、`03-15`、`03-18..19`、`03-20`、`03-12 至 03-21 [N.S.]`） |
| `P2-02` | `CLM-avrich-1963-bolsheviks-and-workers-control.md:19` | Thesis 段 `1917-11-03 [O.S.]` 与 `11-14 [O.S.]` 仅在下方论证段标有公历，本行缺 `[N.S.]` 孪生 | 已补齐 `1917-11-03 [O.S.] / 11-16 [N.S.]` 与 `1917-11-14 [O.S.] / 11-27 [N.S.]` |
| `P2-03` | `CLM-gaida-2017-provisional-government-governing-principles.md:24-26` | 1917 年春夏密集法案缩写旧历（`03-25..28`、`05-09..12`、`03-09`、`04-21`、`06-12`、`07-01`、`08-01`、`08-27 [O.S.]` 等）缺同行 `+13` 公历 | 已逐项换算并补齐全部 12 处 `[N.S.]` 公历对应日 |
