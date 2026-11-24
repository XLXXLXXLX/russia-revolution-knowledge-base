# Benchmark 定期维护与反过拟合规程 (`MAINTENANCE.md`)

Benchmark 一旦停止维护，要么因仓库卡片重命名而发生**锚点腐烂（Anchor Rot）**，要么因工程改动专门迎合已知测试题而沦为**应试摆设（Goodhart Overfitting）**。为此，本库确立以下四项强制维护机制：

---

## 一、四大触发式与周期式维护节点

### 1. 每次脚本或图谱重构前后（Pre/Post-Refactor Gate）
1. **动手前**：先运行 `python benchmarks/run_benchmarks.py check-health` 确认套件本身健康，再运行 `python benchmarks/run_benchmarks.py run --save-baseline <pre_tag>` 冻结改动前基线。
2. **改动后**：同时运行全量集与保留集：
   - `python benchmarks/run_benchmarks.py run --split dev`
   - `python benchmarks/run_benchmarks.py run --split holdout`
   - `python benchmarks/run_benchmarks.py compare benchmarks/baselines/<pre_tag>.json benchmarks/results/latest.json`
3. **放行标准**：**零退化（Zero Regressions）**，且 `holdout` 集提升幅度不得显著低于 `dev` 集（差距 `>10%` 视为针对 `dev` 题硬编码过拟合，必须打回重改）。

### 2. 每次异源交叉审计（`AUD-*`）发现 `P0/P1` 缺陷后（Audit -> Canary 沉淀机制）
- 凡是在 `audits/AUD-*.md` 中新查实的 **P0 史实/历法/归因错误** 或高频 **P1 情态越界/多阶段边丢失**，在修完卡片的同时，必须抽取其中最具代表性的 1–2 个陷阱追加至 `b4a_historiography_1861_1918.jsonl` 或 `b4b_historiography_1918_1929.jsonl`，并标注 `"origin": "audit_regression:AUD-XX"`。
- `check-health` 会自动扫描 `audits/` 目录，对尚未沉淀回归题的新审计报告发出维护提醒。

### 3. 每次新拆解入库一批电子书（`sources/` 扩容）后
- 当新增入库专著/原典 `>= 5` 本时，向 `b3_chapter_radar_queries.jsonl` 补充 2–4 条覆盖新书核心章节与概念的定位测试（含至少 1 条 `holdout`）；若新入库 PDF 含纯扫描本，同步补充或核验 `needs_ocr` 隔离项。

### 4. 双周 / 每 5 个建库波次定期轮换（14-Day SLA Rotation）
- `suites/registry.json` 为每个套件设定 `review_sla_days: 14`。一旦超期，`check-health` 自动告警。
- 定期复审动作：
  1. **轮换 20% 题项**：由**非主撰写模型家族**的子 Agent 抽换 `B3`/`B4`/`B5` 中已长期满分的简单题，替换为更刁钻的跨时期边缘行动者、档案细节或读者真实追问；
  2. **模态 A 真题抽检**：从 `B5` 的 `holdout` 集中抽取至少 2–3 道题生成完整“对外讲史”文章，通过 `eval-prose` Stage-1 自动门槛与异源盲审 Stage-2（`>=21/25` 分），防止工程演进后文风重新变干巴；
  3. 更新 `suites/registry.json` 中对应套件的 `last_reviewed` 日期，并在下方维护日志登记。

---

## 二、三条红线（Anti-Cheat Guardrails）

1. **严禁在 `scripts/` 生产代码中硬编码任何 Benchmark 题号或测试特判**（`check-health` 会自动扫描 `scripts/*.py` 中的 `B1-`..`B5-` 标识符并直接判败）。
2. **严禁通过删减一跳邻居（如强行截断 Top-15）来伪造 `B2` 字符预算达标**——`B2` 同时锁定 `min_one_hop_neighbor_recall == 100%` 与边缘人物金丝雀召回率。
3. **卡片 ID 合法合并/重命名时**：必须走显式迁移映射并同步更新 `suites/` 中的引用锚点，绝不允许注释掉报错检查。

---

## 三、维护变更台账（Changelog）

| 日期 | 版本 | 维护人 / 协作模型 | 变更摘要 |
| :--- | :--- | :--- | :--- |
| `2026-11-19` | `v1.0.0` | `gemini-4-carbon` + 子代理 (`neon`, `hydrogen`, `grok-4.7`, `argon`) | 初建 B1–B5 五大基准套件、`run_benchmarks.py` 评测/维护引擎，并在代码与卡片整改前锁定 `v0_pre_refactor` 基线 |
| `2026-11-24` | `v1.6.0` | `gemini-4-carbon` | Wave 63 七部旗舰专著整书拆解收口：将 `AUD-26` 查实的马丁《肯定性行动帝国》第10章英文原引词序与俄联邦制度不对称/赫希“双重同化”陷阱沉淀为 `B4B-28`，收敛 `DEB-1923` 等多卡上下文包冗余使全部 12 组 `B5` 推荐包低于 `80,000` 字符预算，冻结 `w63_final` 基线 |
