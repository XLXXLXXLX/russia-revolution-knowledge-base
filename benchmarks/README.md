# 俄国革命知识库（1860s–1929）基准评测体系 (`benchmarks/`)

本目录旨在彻底扭转“只刷卡片数量与形式完整度、忽视检索实效与讲史可读性（古德哈特定律）”的偏差，在任何工程重构或大批量改卡**之前**锁定客观基线，并在**之后**持续拦截退化。

## 一、五大正交评测套件总览

| 套件 | 文件 | 构建者 | 评测维度 |
| :--- | :--- | :--- | :--- |
| **B1** | `suites/b1_graph_and_integrity_cases.json` | 主 Agent (`gemini-4-carbon`) | YAML 元数据解析保真（多行列表/行尾注释）、卡片 `2.2` 关系表与 `edges.jsonl` 多时段边同步率、`CLM -> SCH/Card` 外键完整性、跨世纪双历法数学回归与 `1918-02-14` 改历后防误加 13 天扫描 |
| **B2** | `suites/b2_context_budget_bundles.json` | 主 Agent (`gemini-4-carbon`) | 单枢纽与多卡联合查询编译字符预算（控制 `204k -> <=65k`）、**100% 一跳邻居与边缘关键人物零丢失召回**、`CLM-*`/`SCH-*` 可追溯性、全库 `[T1] <= 150` 字约束 |
| **B3** | `suites/b3_chapter_radar_queries.jsonl` | 子 Agent (`gemini-4-neon`) | 145 本专著/原典章节定位雷达（`Hit@3`、`Hit@5`、`MRR`、查询延迟）及纯扫描无文字层空书 `needs_ocr` 隔离率 |
| **B4A** | `suites/b4a_historiography_1861_1918.jsonl` | 子 Agent (`gemini-4-hydrogen`) | `1861–1918.03` 对抗性史实、因果时序、双历法、回忆录信源层级与多流派史学争鸣金丝雀题集 |
| **B4B** | `suites/b4b_historiography_1918_1929.jsonl` | 异源子 Agent (`grok-4.7`) | `1918.03–1929` 多时段关系反转（如乌格拉诺夫）、机构任期边界（古比雪夫/康德拉季耶夫）、改历后陷阱与情态分寸金丝雀题集 |
| **B5** | `suites/b5_mode_a_prompts.jsonl` | 子 Agent (`gemini-4-argon`) | **模态 A “对外讲史”端到端散文评测**：拒绝“干巴数据库腔”、零工程脚手架泄露（`[T1]`/`CLM-`/`[O.S.]`）、自然中文双历法、边缘行动者锚点与跨模型盲审打分 |

## 二、快速命令

```powershell
# 1. 维护健康度自检（验证所有实体/路径锚点未腐烂、holdout 比例合规、无作弊硬编码）
python benchmarks/run_benchmarks.py check-health

# 2. 运行全量只读基准评测（或仅跑 holdout 防过拟合切片）
python benchmarks/run_benchmarks.py run
python benchmarks/run_benchmarks.py run --split holdout

# 3. 锁定改动前/改动后命名基线快照
python benchmarks/run_benchmarks.py run --save-baseline v0_pre_refactor

# 4. 改动后与基线做逐指标回归比对（任何指标退化即返回非零退出码）
python benchmarks/run_benchmarks.py compare benchmarks/baselines/v0_pre_refactor.json benchmarks/results/latest.json

# 5. 对模态 A 历史长文回答执行反干巴/反黑话体检并生成异源模型盲审载荷
python benchmarks/run_benchmarks.py eval-prose --prompt-id B5-PROSE-01 --answer-file benchmarks/results/sample_answers/B5-PROSE-01.md --emit-judge-prompt
```

定期维护规程详见 [`benchmarks/MAINTENANCE.md`](./MAINTENANCE.md)。
