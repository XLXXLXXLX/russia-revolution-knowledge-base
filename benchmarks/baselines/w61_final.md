# 俄国革命知识库 Benchmark 评测报告 (`w61_final`)

- **评测时间**: `2026-11-22T00:06:09+08:00`
- **评测集划分 (`split`)**: `all`
- **Git HEAD**: `8234804` (工作区变更文件数: `70`)

## 一、五大套件总览记分板

| 套件 | 状态 | 核心指标摘要 |
| :--- | :---: | :--- |
| **B1 图谱/元数据/历法保真** | ✅ PASS | YAML保真 `100.0%` · 多时段边保留 `100.0%` · 2.2边同步率 `100.0%` (僵尸边 `0`) · CLM外键 `100.0%` · 改历误标 `0` |
| **B2 上下文预算与零盲区召回** | ✅ PASS | 预算达标 `100.0%` · `B2-01`字符 `59,268` · 一跳召回 `100.0%` · 主卡CLM召回 `100.0%` · 时段标记保留 `100.0%` · 全库T1合规 `100.0%` |
| **B3 文献章节雷达与空书隔离** | ✅ PASS | 书级Hit@5 `93.8%` · 精确章Hit@3 `78.1%` / Hit@5 `81.2%` (MRR `0.658`) · 中位耗时 `62.4ms` · 空扫隔离 `100.0%` |
| **B4 跨家族对抗史实/经验金丝雀** | ✅ PASS | 总题数 `45` · 正向锚点 `100.0%` · 禁用错误清零 `100.0%` · 故障注入捕获率 `100.0%` |
| **B5 模态A学术长文实测闭环** | ✅ PASS | 推荐包均值 `66,780` 字符 · 实测Holdout长文 `3` 篇 (通过率 `100.0%`, 均分 `100.0`) · 异源盲审报告 `True` |

## 二、关键诊断样本（Top Defects Exposed by Benchmark）

- **B3 精确章节未命中样本**: `B3-LOC-23 (VSNKh) -> exact chapter miss (top3=['sources/articles/oppenheim_1973_supreme_economic_council_1917_1921/ch24_image_25.md', 'sources/articles/oppenheim_1973_supreme_economic_council_1917_1921/ch20_image_21.md', 'sources/articles/oppenheim_1973_supreme_economic_council_1917_1921/ch07_image_8.md'])`, `B3-OCR-01 (October has been making us) -> exact chapter miss (top3=['sources/monographs/corney_2004_telling_october/ch04_introduction_writing_the_event.md', 'sources/monographs/douds_2018_inside_lenins_government/ch10_inside_lenin_s_government.md', 'sources/monographs/khalid_2015_making_uzbekistan_zh/ch03_acknowledgments.md'])`, `B3-OCR-03 (There are no parallel unions in Russia) -> exact chapter miss (top3=['sources/monographs/kotkin_2017_stalin_v2/ch24_stalin.md', 'sources/monographs/carr_1964_socialism_in_one_country_v3p1/ch21_pages_526-550.md', 'sources/monographs/smith_1983_red_petrograd/ch00_pages_1-25.md'])`
