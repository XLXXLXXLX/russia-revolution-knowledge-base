---
id: AUD-29B-wave64-erlich-audit
type: audit
auditor_model: antigravity/gemini-4-neon
target_wave: W64
role: dialectic-auditor
status: closed
remediated_at: "2026-11-25"
updated_at: "2026-11-25"
---

# AUD-29B｜Wave 64 埃尔利赫《苏联工业化争论，1924–1928》精读产出异源交叉审计（Defect-Only）

- **审计对象**：`BOOK-MAP-erlich-1960-industrialization.md`（1 份）及新增 `CLM-erlich-1960-*.md`（8 份），共 9 份（主撰写模型家族：OpenAI `codex/gpt-6.2-sol`；异源审计模型家族：Google `antigravity/gemini-4-neon`）。
- **核验范围与零缺陷项摘要**：
  - **原文直引（11/11 片段）**：全部逐字命中 `sources/monographs/erlich_1960_industrialization/` 对应切片，无 P0 错字、删改或页码张冠李戴。
  - **YAML 外键与相对链接**：`SCH-erlich-alexander`、3 张 `DEB-*`、11 张实体/事件/政策/会议/概念卡、3 张原有 `CLM-*` 及 `BOOK-MAP-lewin-1968-peasants.md` 全部实存无坏链，`supports`/`rebuts`/`qualifies` 合规。
  - **历法纪律**：所涉 1920 年代苏俄事件均使用单公历 `[N.S.]`，无伪造 `[O.S.]`。
  - **逐文件零 P0/P1 项**：`CLM-erlich-1960-bukharin-future-bricks.md`、`CLM-erlich-1960-feldman-reproduction-threshold.md`、`CLM-erlich-1960-replacement-echo.md`、`CLM-erlich-1960-stalin-fourteenth-to-procurement.md` 均 **无 P0/P1 缺陷**（仅列 P2 微瑕）。
- **缺陷计数**：**P0 = 0｜P1 = 5｜P2 = 9**。

---

## 一、P1 缺陷清单（5 项）

| 编号 | 文件 | 位置 | 缺陷描述 |
| :--- | :--- | :--- | :--- |
| `P1-01` | `reading-notes/erlich_1960_industrialization/BOOK-MAP-erlich-1960-industrialization.md` | L39 | **跨章归属漂移**：导言小结将“战前设备的可用程度与战后国内购买力也不再沿同一比例恢复”锚定至 `pp. xvi–xvii`（`ch02#L46–L103`）。核对原文，该对比出自第 II 章普列奥布拉任斯基（`pp. 32–36`）与第 VI 章（`p. 101`）；`pp. xvi–xvii` 实际陈述的长期隐忧是农产品商品量在 1923 年回升至战前约 62%（切片 OCR 误作 `6.2 per cent`）后增幅停滞、工业在 1925 年跃进后增速趋缓且 1913 年基线本身仍属落后。 |
| `P1-02` | `historiography/claims/CLM-erlich-1960-bazarov-levelling-off.md` | L25–L26 | **核心论证漏锚 `p. 66` 并错锚至第 VII 章脚注**：第 2 条末句“反对把全部新增投资押在周期较长的新设施上”止于 `pp. 63–65, ch06#L411–L507`，漏掉了该论证所在的 `p. 66`（`ch06#L508–L537`）；第 3 条前两句（部分改装换取较早产出、缓解建筑工人工资引发的需求失衡、新厂投产后降低该比重）同样源自 `pp. 65–66`（`ch06#L493–L537`）与 `p. 136`（`ch09#L421–L457`），却仅锚定到第 VII 章统计脚注 `p. 137, ch09#L478–L490`。 |
| `P1-03` | `historiography/claims/CLM-erlich-1960-capital-famine-accelerator.md` | L26 | **希克斯对读锚点失落且逻辑错接**：第 3 条在“零售端涨价信号”句后称“埃尔利赫借此与希克斯论战后复苏的论述对读（pp. 102–103，ch08#L46–L124）”。核对原文，埃尔利赫引述希克斯 1947 年论文位于 `pp. 101–102`（`ch08#L30–L46`），用以对读普列奥布拉任斯基关于**现有产能趋尽后在技术上须将新增劳动力转向投资品生产**的命题，并非承接 `p. 103` 脚注的零售价格信号；且 `#L46–L124` 将希克斯引文排斥在外。 |
| `P1-04` | `historiography/claims/CLM-erlich-1960-imported-machinery-stock-flow.md` | L25 | **核心经济学术语误译**：第 2 条将 `p. 143 n.`（`ch09#L728–L761`）的 `addition to the domestic K-producing capacity` / `K-producing stock` 译为“进口能在国产厂房竣工前形成库存”。此处 `stock` 指**资本品生产能力／固定资本存量**而非商业“库存（inventory）”；误译导致正文与标题“存量与流量边界”脱节。 |
| `P1-05` | `historiography/claims/CLM-erlich-1960-shanin-export-led-sequencing.md` | L26 | **论点缺失出处锚点**：第 3 条首句“沙宁允许按军备期限提前转移投资，也承认暂时保护幼稚工业”仅锚定于第 VII 章 `pp. 133–135、141–144`（`ch09`），但“按军备期限（如五年内武装干涉）提前转移”的论述完全出自第 II 章 `pp. 28–29`（`ch05#L23–L71`），`ch09` 中并无该项内容。 |

---

## 二、P2 缺陷清单（9 项）

| 编号 | 文件 | 位置 | 缺陷描述 |
| :--- | :--- | :--- | :--- |
| `P2-01` | `BOOK-MAP-erlich-1960-industrialization.md` | L62, L67, L97 | L62 `progressive taxation` 误作“渐进税”（同文 L45 为“累进税”）；“超额拨款可延长工期”将 `p. 82`（1927-11 演说）与 `p. 83`《经济学家札记》（在建项目停顿并最终拖慢发展）混述；尾注锚点 `ch14#L197–L201` 混入注 11–12（精确为 `#L199–L201`）。L67“近五年工业产量拟增约 75%”误译 `"during the coming five years"`（应为“未来五年”）。L97 单页误用复数 `pp. xvii`（应为 `p. xvii`）。 |
| `P2-02` | `CLM-erlich-1960-bazarov-levelling-off.md` | L10, L32, L36 | YAML `original_pages: "pp. 60–66"` 漏列正文所引 `pp. 75–77, 136–137`；直引精确行号为 `ch06#L300–L304`（原 `#L299` 多含前半行）；语境说明宜明示该引文为埃尔利希 1960 年的理论概括而非巴扎罗夫原文直译。 |
| `P2-03` | `CLM-erlich-1960-bukharin-future-bricks.md` | L9–L10, L26 | YAML `local_source_path` 止于 `#L5-L234`（正文已引至 `#L457`），`original_pages` 漏列 `ch07#L264–L273` 所在的 `p. 84`；L26 刊期尾注精确为 `ch14#L199–L201`。 |
| `P2-04` | `CLM-erlich-1960-capital-famine-accelerator.md` | L10 | YAML `original_pages: "pp. 101–104, 118–119"` 漏列正文所引 `p. 40` 与第二段直引所在的 `p. xx`。 |
| `P2-05` | `CLM-erlich-1960-feldman-reproduction-threshold.md` | L10, L25, L36 | YAML `original_pages` 漏列第 3 条所引 `p. 151`；L25“最终拖慢整个系统”弱于原文 `p. 149 n.` 的 `"begin to level off and then to contract"`（先趋缓、继而收缩）；L36“资本产出率”宜与前文统一为“资本产出比”。 |
| `P2-06` | `CLM-erlich-1960-imported-machinery-stock-flow.md` | L10, L32 | YAML `original_pages: "pp. 141–144"` 漏列第 1 条所引 `pp. 45–48`；直引精确行号为 `ch09#L719–L722`（原 `#L718` 多含前半行）。 |
| `P2-07` | `CLM-erlich-1960-replacement-echo.md` | L9–L10, L26 | L26 模型参数设定（5%、十年、一年、三年重置不足）始于 `p. 109` 脚注（`ch08#L363–L372`），设备衰减脚注 (2) 与正文结论延续至 `p. 113`（`ch08#L619–L648`），YAML 与第 3 条页码/行号锚点可同步补全。 |
| `P2-08` | `CLM-erlich-1960-shanin-export-led-sequencing.md` | L32, L40 | Quote 1 精确行号为 `ch05#L82–L84`（L85 为空行）；语境说明未明示两段直引分别属于沙宁 1926 年原文（埃尔利赫译引）与埃尔利赫 1960 年批评，建议补一句层级区分。 |
| `P2-09` | `CLM-erlich-1960-stalin-fourteenth-to-procurement.md` | L26, L32, L36, L40 | L26 将斯大林 `pp. 172–173` 原话 `"not hindering kulak farming ... giving him power"` 中的“富农（kulak）”淡化为“富裕农户”，弱化了斯大林政治定性与埃尔利赫分析语域（`well-to-do peasants`）的区分；且斯大林反对粮价上调与进口粮食的论据引自 `Sochineniya, XII, 45–47, 92–95`（1929 年 4 月追述批判），宜在语境中与 1928 年表述分期注明；两段直引精确行号为 `ch07#L488–L489` 与 `ch10#L872`。 |

---

## 三、精确替换矩阵（Target -> Replacement）

### 1. `reading-notes/erlich_1960_industrialization/BOOK-MAP-erlich-1960-industrialization.md`

- **`P1-01`（L39）**
  - **Target**:
    ```markdown
    1923 年剪刀差与稍后的商品荒是两种不同的失衡。战前设备的可用程度与战后国内购买力也不再沿同一比例恢复（pp. xvi–xvii，[ch02#L46–L103](../../sources/monographs/erlich_1960_industrialization/ch02_introduction_xv.md#L46-L103)）。
    ```
  - **Replacement**:
    ```markdown
    1923 年剪刀差与稍后的商品荒是两种不同的失衡；更持续的隐忧在于，农产品商品量在 1923 年回升至战前约 62%（切片 OCR 误作 `6.2 per cent`）后便鲜有进一步增长，工业虽较快逼近 1913 年水平，却在 1925 年跃进后明显趋缓，而 1913 年的落后水平本身并非理想停靠点（pp. xvi–xvii，[ch02#L46–L103](../../sources/monographs/erlich_1960_industrialization/ch02_introduction_xv.md#L46-L103)）。
    ```

- **`P2-01a`（L62）**
  - **Target**:
    ```markdown
    布哈林在 1928-09-30 [N.S.]《经济学家札记》中以冶金、工业现产与建设的比例、农原料三个瓶颈说明，超额拨款可延长工期、挤压相关生产并加重商品荒。十五大方案兼顾小工业、农业局部技术改进、提高班次和有选择的新建；财源依靠渐进税和自愿储蓄。埃尔利赫指出后两者若无配套可能相互抵消，多班制还会加速设备损耗，库存不足时不能排除暂时失衡（pp. 81–89，[ch07#L147–L457](../../sources/monographs/erlich_1960_industrialization/ch07_part_one_the_debate_part_4.md#L147-L457)；刊期 [ch14#L197–L201](../../sources/monographs/erlich_1960_industrialization/ch14_references_202.md#L197-L201)）。
    ```
  - **Replacement**:
    ```markdown
    布哈林在 1928-09-30 [N.S.]《经济学家札记》中以冶金、工业现产与建设的比例、农原料三个瓶颈说明，超额拨款将导致在建项目中止、挤压相关生产、加重商品荒并最终拖慢增速。十五大方案兼顾小工业、农业局部技术改进、提高班次和有选择的新建；财源依靠累进税和自愿储蓄。埃尔利赫指出后两者若无配套可能相互抵消，多班制还会加速设备损耗，储备不足时不能排除暂时失衡（pp. 81–89，[ch07#L147–L457](../../sources/monographs/erlich_1960_industrialization/ch07_part_one_the_debate_part_4.md#L147-L457)；刊期 [ch14#L199–L201](../../sources/monographs/erlich_1960_industrialization/ch14_references_202.md#L199-L201)）。
    ```

- **`P2-01b`（L67）**
  - **Target**:
    ```markdown
    1927 年十五大报告在近五年工业产量拟增约 75% 的表述之外
    ```
  - **Replacement**:
    ```markdown
    1927 年十五大报告在未来五年工业产量拟增约 75% 的表述之外
    ```

- **`P2-01c`（L97）**
  - **Target**:
    ```markdown
    | pp. xvii、pp. 60–66、pp. 117–118，
    ```
  - **Replacement**:
    ```markdown
    | p. xvii、pp. 60–66、pp. 117–118，
    ```

### 2. `historiography/claims/CLM-erlich-1960-bazarov-levelling-off.md`

- **`P2-02a`（L10）**
  - **Target**:
    ```yaml
    original_pages: "pp. 60–66"
    ```
  - **Replacement**:
    ```yaml
    original_pages: "pp. 60–66, 75–77, 136–137"
    ```

- **`P1-02`（L25–L26）**
  - **Target**:
    ```markdown
    2. 巴扎罗夫反对把冶金和金属加工业整体搁置。推迟重置会损失设备及熟练工人，铁路、河运和可出口的采掘业也需要重工业投入。与此同时，他反对把全部新增投资押在周期较长的新设施上（pp. 63–65，[ch06#L411–L507](../../sources/monographs/erlich_1960_industrialization/ch06_part_one_the_debate_part_3.md#L411-L507)）。
    3. 部分改装以较低的长期效率换取较早的产出，可在新厂未投产而建筑工人工资已形成需求时缓解失衡。新能力投产后可降低此类投资比重。埃尔利赫另引国营工业数据，旧厂扩建与换装在 1925/26、1926/27、1927/28 年度投资中分别占 55.2%、56.1%、55.7%，其中包含较彻底的改造，且与资本性大修分别统计（p. 137，[ch09#L478–L490](../../sources/monographs/erlich_1960_industrialization/ch09_part_two_the_issues_and_the_aftermath_pa.md#L478-L490)）。
    ```
  - **Replacement**:
    ```markdown
    2. 巴扎罗夫反对把冶金和金属加工业整体搁置。推迟重置会损失设备及熟练工人，铁路、河运和可出口的采掘业也需要重工业投入。与此同时，他反对把全部新增投资押在周期较长的新设施上（pp. 63–66，[ch06#L411–L537](../../sources/monographs/erlich_1960_industrialization/ch06_part_one_the_debate_part_3.md#L411-L537)）。
    3. 部分改装以较低的长期效率换取较早的产出，可在新厂未投产而建筑工人工资已形成需求时缓解失衡，新能力投产后则可降低此类投资比重（pp. 65–66、136，[ch06#L493–L537](../../sources/monographs/erlich_1960_industrialization/ch06_part_one_the_debate_part_3.md#L493-L537)、[ch09#L421–L457](../../sources/monographs/erlich_1960_industrialization/ch09_part_two_the_issues_and_the_aftermath_pa.md#L421-L457)）。埃尔利赫另引国营工业数据，旧厂扩建与换装在 1925/26、1926/27、1927/28 年度投资中分别占 55.2%、56.1%、55.7%，其中包含较彻底的改造，且与资本性大修分别统计（p. 137，[ch09#L478–L490](../../sources/monographs/erlich_1960_industrialization/ch09_part_two_the_issues_and_the_aftermath_pa.md#L478-L490)）。
    ```

- **`P2-02b`（L32, L36）**
  - **Target**:
    ```markdown
    `[p. 60 | ch06_part_one_the_debate_part_3.md#L299-L304]`
    ```
  - **Replacement**:
    ```markdown
    `[p. 60 | ch06_part_one_the_debate_part_3.md#L300-L304]`
    ```
  - **Target**:
    ```markdown
    趋缓指增长率随利用率接近上限而下降。原文未估计特定函数形式，也未给出旧厂改装与新建投资的最优比率。
    ```
  - **Replacement**:
    ```markdown
    上方引文系埃尔利赫 1960 年对巴扎罗夫“趋缓曲线”机制的概括转述（非巴扎罗夫原文直译）；趋缓指增长率随利用率接近上限而下降。原文未估计特定函数形式，也未给出旧厂改装与新建投资的最优比率。
    ```

### 3. `historiography/claims/CLM-erlich-1960-bukharin-future-bricks.md`

- **`P2-03`（L9–L10, L26）**
  - **Target**:
    ```yaml
    local_source_path: "sources/monographs/erlich_1960_industrialization/ch07_part_one_the_debate_part_4.md#L5-L234"
    original_pages: "pp. 78–83, 85–89"
    ```
  - **Replacement**:
    ```yaml
    local_source_path: "sources/monographs/erlich_1960_industrialization/ch07_part_one_the_debate_part_4.md#L5-L457"
    original_pages: "pp. 78–89"
    ```
  - **Target**:
    ```markdown
    刊期见 [ch14#L197–L201](../../sources/monographs/erlich_1960_industrialization/ch14_references_202.md#L197-L201)
    ```
  - **Replacement**:
    ```markdown
    刊期见 [ch14#L199–L201](../../sources/monographs/erlich_1960_industrialization/ch14_references_202.md#L199-L201)
    ```

### 4. `historiography/claims/CLM-erlich-1960-capital-famine-accelerator.md`

- **`P2-04`（L10）**
  - **Target**:
    ```yaml
    original_pages: "pp. 101–104, 118–119"
    ```
  - **Replacement**:
    ```yaml
    original_pages: "pp. xx, 40, 101–104, 118–119"
    ```

- **`P1-03`（L26）**
  - **Target**:
    ```markdown
    3. 布哈林担忧投资先把受压经济推过稳定界限。普列奥布拉任斯基担忧压低价格而不调整产能，会使涨价信号停留在零售端，未能引导资源进入工业。埃尔利赫借此与希克斯论战后复苏的论述对读，并提醒苏联计划存在自主投资动机，不能把整个过程简化为诱发投资（pp. 102–103，[ch08#L46–L124](../../sources/monographs/erlich_1960_industrialization/ch08_part_two_the_issues_and_the_aftermath_pa.md#L46-L124)）。
    ```
  - **Replacement**:
    ```markdown
    3. 布哈林担忧投资先把受压经济推过稳定界限；普列奥布拉任斯基则担忧压低价格而不调整产能，会使涨价信号停留在零售端而无法引导资源进入工业。埃尔利赫一方面引述希克斯 1947 年论战后复苏时关于“既有产能耗尽后在技术上须将新增劳动力投向投资品生产”的论断与普列奥布拉任斯基对读（pp. 101–102，[ch08#L30–L46](../../sources/monographs/erlich_1960_industrialization/ch08_part_two_the_issues_and_the_aftermath_pa.md#L30-L46)），另一方面提醒苏联计划包含自主投资动机，不能将整个过程简化为诱发投资（pp. 102–103，[ch08#L71–L124](../../sources/monographs/erlich_1960_industrialization/ch08_part_two_the_issues_and_the_aftermath_pa.md#L71-L124)）。
    ```

### 5. `historiography/claims/CLM-erlich-1960-feldman-reproduction-threshold.md`

- **`P2-05`（L10, L25, L36）**
  - **Target**:
    ```yaml
    original_pages: "pp. 147–150, 184"
    ```
  - **Replacement**:
    ```yaml
    original_pages: "pp. 147–151, 184"
    ```
  - **Target**:
    ```markdown
    消费品部门扩张过久可使其重置需求侵吞投资品余量，最终拖慢整个系统
    ```
  - **Replacement**:
    ```markdown
    消费品部门扩张过久可使其重置需求侵吞并超出投资品余量，导致系统先趋缓、继而收缩
    ```
  - **Target**:
    ```markdown
    对长期消费的排序取决于部门资本产出率、设备寿命、建设时滞及实际供给。
    ```
  - **Replacement**:
    ```markdown
    对长期消费的排序取决于部门资本产出比、设备寿命、建设时滞及实际供给。
    ```

### 6. `historiography/claims/CLM-erlich-1960-imported-machinery-stock-flow.md`

- **`P2-06a`（L10）**
  - **Target**:
    ```yaml
    original_pages: "pp. 141–144"
    ```
  - **Replacement**:
    ```yaml
    original_pages: "pp. 45–48, 141–144"
    ```

- **`P1-04`（L25）**
  - **Target**:
    ```markdown
    2. 埃尔利赫在 p. 143 注中比较两条路径：用消费品 C 换取资本品 K，或先建国产 K 的工厂。进口能在国产厂房竣工前形成库存，厂房投产后则可反复生产年流量，差距因此变小。进口仍可能因外国生产效率较高而占优（pp. 143–144，[ch09#L715–L761](../../sources/monographs/erlich_1960_industrialization/ch09_part_two_the_issues_and_the_aftermath_pa.md#L715-L761)）。
    ```
  - **Replacement**:
    ```markdown
    2. 埃尔利赫在 p. 143 注中比较两条路径：用消费品 C 换取资本品 K，或先建国产 K 的工厂。进口能在国产厂房竣工前先行形成生产性资本存量（K-producing capacity），但待国产厂房竣工并形成可反复产出 K 年流量的资本存量后，二者在产能上的净差距会显著缩小；进口仍可能因外国生产效率较高（传统比较优势）而占优（pp. 143–144，[ch09#L715–L761](../../sources/monographs/erlich_1960_industrialization/ch09_part_two_the_issues_and_the_aftermath_pa.md#L715-L761)）。
    ```

- **`P2-06b`（L32）**
  - **Target**:
    ```markdown
    `[p. 143 | ch09_part_two_the_issues_and_the_aftermath_pa.md#L718-L722]`
    ```
  - **Replacement**:
    ```markdown
    `[p. 143 | ch09_part_two_the_issues_and_the_aftermath_pa.md#L719-L722]`
    ```

### 7. `historiography/claims/CLM-erlich-1960-replacement-echo.md`

- **`P2-07`（L9–L10, L26）**
  - **Target**:
    ```yaml
    local_source_path: "sources/monographs/erlich_1960_industrialization/ch08_part_two_the_issues_and_the_aftermath_pa.md#L145-L614"
    original_pages: "pp. 104–112"
    ```
  - **Replacement**:
    ```yaml
    local_source_path: "sources/monographs/erlich_1960_industrialization/ch08_part_two_the_issues_and_the_aftermath_pa.md#L145-L648"
    original_pages: "pp. 33–34, 104–113"
    ```
  - **Target**:
    ```markdown
    三年工期或设备运转中持续衰减会使回稳更困难（pp. 110–112，[ch08#L373–L614](../../sources/monographs/erlich_1960_industrialization/ch08_part_two_the_issues_and_the_aftermath_pa.md#L373-L614)）。
    ```
  - **Replacement**:
    ```markdown
    三年工期或设备运转中持续衰减会使回稳更困难（pp. 109–113，[ch08#L363–L648](../../sources/monographs/erlich_1960_industrialization/ch08_part_two_the_issues_and_the_aftermath_pa.md#L363-L648)）。
    ```

### 8. `historiography/claims/CLM-erlich-1960-shanin-export-led-sequencing.md`

- **`P1-05`（L26）**
  - **Target**:
    ```markdown
    3. 沙宁允许按军备期限提前转移投资，也承认暂时保护幼稚工业。埃尔利赫指出，农业累积本身会占用钢铁和设备，后期调回资金无法补回此前少建的投资品产能。外贸可缓冲这一限制，但比较成本计算还须考虑苏联出口规模、国际粮市需求、贸易条件、要素禀赋和国内互补关系（pp. 133–135、141–144，[ch09#L281–L374](../../sources/monographs/erlich_1960_industrialization/ch09_part_two_the_issues_and_the_aftermath_pa.md#L281-L374)、[ch09#L614–L692](../../sources/monographs/erlich_1960_industrialization/ch09_part_two_the_issues_and_the_aftermath_pa.md#L614-L692)、[ch09#L773–L780](../../sources/monographs/erlich_1960_industrialization/ch09_part_two_the_issues_and_the_aftermath_pa.md#L773-L780)）。
    ```
  - **Replacement**:
    ```markdown
    3. 沙宁允许按军备期限提前转移投资，也承认暂时保护幼稚工业（pp. 28–29，[ch05#L23–L71](../../sources/monographs/erlich_1960_industrialization/ch05_part_one_the_debate_part_2.md#L23-L71)）。埃尔利赫指出，农业累积本身会占用钢铁和设备，后期调回资金无法补回此前少建的投资品产能；外贸可缓冲这一限制，但比较成本计算还须考虑苏联出口规模、国际粮市需求、贸易条件、要素禀赋和国内互补关系（pp. 133–135、141–144，[ch09#L281–L374](../../sources/monographs/erlich_1960_industrialization/ch09_part_two_the_issues_and_the_aftermath_pa.md#L281-L374)、[ch09#L614–L692](../../sources/monographs/erlich_1960_industrialization/ch09_part_two_the_issues_and_the_aftermath_pa.md#L614-L692)、[ch09#L773–L780](../../sources/monographs/erlich_1960_industrialization/ch09_part_two_the_issues_and_the_aftermath_pa.md#L773-L780)）。
    ```

- **`P2-08`（L32, L40）**
  - **Target**:
    ```markdown
    `[p. 29 | ch05_part_one_the_debate_part_2.md#L82-L85]`
    ```
  - **Replacement**:
    ```markdown
    `[p. 29 | ch05_part_one_the_debate_part_2.md#L82-L84]`
    ```
  - **Target**:
    ```markdown
    经济方案的相似性是埃尔利赫的比较判断。
    ```
  - **Replacement**:
    ```markdown
    经济方案的相似性是埃尔利赫的比较判断；上方两段直引中，第一段为埃尔利赫译引沙宁 1926 年原文，第二段为埃尔利赫 1960 年的经济学史评述。
    ```

### 9. `historiography/claims/CLM-erlich-1960-stalin-fourteenth-to-procurement.md`

- **`P2-09`（L26, L32, L36, L40）**
  - **Target**:
    ```markdown
    就应急方案而言，他以实际工资与进口设备机会成本反对提价和粮食进口，并把给富裕农户扩大经营余地表述为赋予其权力（pp. 170–173，[ch10#L744–L885](../../sources/monographs/erlich_1960_industrialization/ch10_part_two_the_issues_and_the_aftermath_pa.md#L744-L885)）。
    ```
  - **Replacement**:
    ```markdown
    就应急方案而言，他以实际工资与进口设备机会成本反对提价和粮食进口，并将“不阻碍富农（kulak）经济”直接等同于放任富农自由与赋予其政治权力（pp. 170–173，[ch10#L744–L885](../../sources/monographs/erlich_1960_industrialization/ch10_part_two_the_issues_and_the_aftermath_pa.md#L744-L885)）。
    ```
  - **Target**:
    ```markdown
    `[p. 90 | ch07_part_one_the_debate_part_4.md#L488-L490]`
    ```
  - **Replacement**:
    ```markdown
    `[p. 90 | ch07_part_one_the_debate_part_4.md#L488-L489]`
    ```
  - **Target**:
    ```markdown
    `[p. 173 | ch10_part_two_the_issues_and_the_aftermath_pa.md#L871-L872]`
    ```
  - **Replacement**:
    ```markdown
    `[p. 173 | ch10_part_two_the_issues_and_the_aftermath_pa.md#L872]`
    ```
  - **Target**:
    ```markdown
    布哈林—李可夫提价、必要时进口粮食的具体说法，部分来自斯大林 1929 年 4 月的批判，埃尔利赫将其列为有根据的推断（p. 171 注，[ch10#L817–L825](../../sources/monographs/erlich_1960_industrialization/ch10_part_two_the_issues_and_the_aftermath_pa.md#L817-L825)）。
    ```
  - **Replacement**:
    ```markdown
    布哈林—李可夫提价、必要时进口粮食的具体说法，部分来自斯大林 1929 年 4 月的批判（《斯大林文集》第 12 卷，包括斯大林本人对实际工资与进口设备机会成本的反驳），埃尔利赫将其列为有根据的推断（p. 171 注、p. 172，[ch10#L817–L854](../../sources/monographs/erlich_1960_industrialization/ch10_part_two_the_issues_and_the_aftermath_pa.md#L817-L854)；尾注 [ch14#L351](../../sources/monographs/erlich_1960_industrialization/ch14_references_202.md#L351)）；“赋权”三段论则出自 1928 年 11 月全会（同书第 11 卷 p. 275，[ch14#L352](../../sources/monographs/erlich_1960_industrialization/ch14_references_202.md#L352)），而“富裕农民／农村上层”属埃尔利赫随后的分析语域。
    ```
