# 史学史对勘与反偏见审计报告（AUD-12）：第 26 波 6 张枢纽组织与政策卡片逐字异源审计

- **审计角色**：`dialectic-auditor`（史学史对勘与反偏见审计官，纯只读异源对勘）
- **审计日期**：`2026-11-18`
- **被审对象**（共 6 张枢纽组织与政策卡片，由 Cursor Composer 起草）：
  1. [`cards/organizations/ORG-provisional-government.md`](../cards/organizations/ORG-provisional-government.md)（1917年俄国临时政府）
  2. [`cards/organizations/ORG-petrograd-soviet.md`](../cards/organizations/ORG-petrograd-soviet.md)（彼得格勒工兵代表苏维埃）
  3. [`cards/organizations/ORG-bund.md`](../cards/organizations/ORG-bund.md)（崩得：立陶宛、波兰和俄罗斯犹太工人总同盟）
  4. [`cards/organizations/ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md)（马赫诺运动 / 乌克兰革命起义军）
  5. [`cards/policies/POL-april-theses-1917.md`](../cards/policies/POL-april-theses-1917.md)（《四月提纲：论无产阶级在这次革命中的任务》）
  6. [`cards/policies/POL-first-five-year-plan.md`](../cards/policies/POL-first-five-year-plan.md)（第一个五年计划）
- **对勘基准**：`python scripts/kb.py date` 儒略/公历与 JDN 换算器、`python scripts/kb.py audit-graph`、库内一手文献（[`1917-04-04_april-theses.md`](../sources/web-archive/E06_E10_turning_points/1917-04-04_april-theses.md)）、专书提取文本（[`mawdsley_1987_civil_war_zh`](../sources/monographs/mawdsley_1987_civil_war_zh/)、[`hobsbawm_1959_primitive_rebels_zh`](../sources/monographs/hobsbawm_1959_primitive_rebels_zh/)、[`getzler_1967_martov`](../sources/monographs/getzler_1967_martov/) 等）及 28 张关联 `CLM-*` / 既有实体卡。
- **审计总结论**：**不予直接放行，须按本报告第四节逐行清单完成 12 项 P0 级硬伤修复与 9 项 P1 级规范校准后方可定稿**。
  - **结构与断链底线**：全库 `CLM-*` 与 `DEB-*` 节点 ID 引用均真实存在（0 个虚构 `CLM-*` / `DEB-*` ID），1897 年崩得成立（`+12 天`）与 1918-02-14 后纯公历纪律总体合规；
  - **核心致命硬伤（P0）**：
    1. **1917 双历倒扣与漏标**：[`POL-april-theses-1917.md`](../cards/policies/POL-april-theses-1917.md) L11 将十月起义俄历日期 `1917-10-25` 误填进公历键 `end_ns`，再倒减 13 天造出假俄历 `1917-10-12 [O.S.]`；[`ORG-petrograd-soviet.md`](../cards/organizations/ORG-petrograd-soviet.md) L20、L28、L59、L80 四处将俄历 `1917-08-31` 漏标双历并直接混入公历序列（公历实为 `1917-09-13 [N.S.]`）。
    2. **输入法/机翻幻觉乱码词**：[`ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md) L26 将乌克兰草原写成中国地理名词 **`“江淮平原”`**，L33 机翻 **`“货架外特征”`**，L40 出现拉丁—西里尔混血乱码 **`“taчанka”`**；[`ORG-petrograd-soviet.md`](../cards/organizations/ORG-petrograd-soviet.md) L25 将“苏汉诺夫”误打为 **`“苏联汉诺夫”`**；[`ORG-bund.md`](../cards/organizations/ORG-bund.md) L25 造出 **`“独立族自治州”`**、L27 将崩得领袖梅杰姆（Medem）误作 **`“年甸”`**、L46 出现西里尔—拉丁混拼 **`“кorenizatsiya”`**；[`POL-first-five-year-plan.md`](../cards/policies/POL-first-five-year-plan.md) L10、L33 将“十五大”截断为 **`“1927-12-15 五大”`/`“五大”`**，L35 给布哈林捏造股市俗语 **`“骑牛入市”`**。
    3. **职务、机构与军事史实张冠李戴**：[`ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md) L26 捏造 **`“1920 曾与弗兰格尔结盟打击红军”`**（史实是马赫诺严词拒绝并处决弗兰格尔使者），并将南线消灭马赫诺的红军统帅 **伏龙芝** 张冠李戴为 **图哈切夫斯基**；[`ORG-petrograd-soviet.md`](../cards/organizations/ORG-petrograd-soviet.md) L36 将苏维埃执委会主席（实为齐赫伊泽）张冠李戴给 **策烈铁里（`chairman-of-ie`）**，并在 L59 将通过 8 月 31 日布尔什维克决议的 **彼得格勒苏维埃全体大会** 误写成 **执委会**；[`ORG-provisional-government.md`](../cards/organizations/ORG-provisional-government.md) L28、L58 将 `1917-09-25 [O.S.] / 1917-10-08 [N.S.]` 成立的 **第三届联合内阁（含 6 名社会主义部长）** 误定性为“无社会主义者的技术内阁”；[`POL-first-five-year-plan.md`](../cards/policies/POL-first-five-year-plan.md) L26 将 **1929 年 5 月第五次全苏苏维埃代表大会** 误写成“第五届全俄苏维埃代表大会”（全俄五大实为 1918 年 7 月左派社革党起义那次），并将 `04-16–23` **四月中央联席全会** 与 `04-23–29` **第十六次党代表会议** 焊成同一个会议。
    4. **转述句加英文双引号伪充直引 & 本地路径断链**：[`ORG-bund.md`](../cards/organizations/ORG-bund.md) L62 将自撰英文改写句放入 `> "..."` 双引号；4 张卡片合计存在 **5 处 `reading-notes/` 与 `sources/monographs/` 路径断链**。

---

## 一、 专项核查 A：历法换算与纪年纪律（`kb.py date` 逐项验算）

### 1.1 逐卡历法核验总表

| 卡片 ID | 核查时段与规则 | 卡片标注 | `kb.py date` 验算结果 | 审计结论 |
| :--- | :--- | :--- | :--- | :--- |
| [`ORG-bund.md`](../cards/organizations/ORG-bund.md) | 19 世纪（`+12 天`）与 1903 伦敦当地公历 | L10/L25/L72: `1897-09-25 [O.S.] / 1897-10-07 [N.S.]`；1903 二大按伦敦公历不倒扣俄历；`end_ns: "1921-03-21"` | `1897-09-25 [O.S.]` + 12d = `1897-10-07 [N.S.]` | **PASS**（成立日与伦敦单公历完全准确；`end_ns` 建议微调对齐 1921-03-12 明斯克并党大会，见 P1） |
| [`ORG-provisional-government.md`](../cards/organizations/ORG-provisional-government.md) | 1917.03–11（`+13 天`） | `03-02/03-15`、`03-03/03-16`、`03-05/03-18`、`04-18/05-01`、`05-05/05-18`、`07-08/07-21`、`09-25/10-08`、`10-26/11-08` | 全部差值均为 `+13 天` | **WARN（P1）**：双历算术全部正确；但 L38、L39 边表有效时段仅写 `[O.S.]` 未附 `[N.S.]`，且 L57 将克伦斯基继任日（`07-21`）与第二届联立内阁组成日（`07-24 [O.S.] / 08-06 [N.S.]`）混同 |
| [`ORG-petrograd-soviet.md`](../cards/organizations/ORG-petrograd-soviet.md) | 1917.02–11（`+13 天`） | `02-27/03-12`、`03-01/03-14`、`03-14/03-27`、`04-04/04-17`、`10-16/10-29`、`10-25/11-07`、`10-26/11-08` 正确；**唯独 `1917-08-31` 四处裸写** | `1917-08-31 [O.S.]` + 13d = **`1917-09-13 [N.S.]`** | **FAIL（P0）**：L20、L28、L59、L80 将俄历 `1917-08-31` 漏标 `[O.S.]` 及公历 `1917-09-13 [N.S.]`，L59 更直接把俄历 `1917-08-31` 填进公历主键列；L28、L61 漏标托洛茨基当选主席双历（`1917-09-09 [O.S.] / 09-22 [N.S.]` 主席团辞职，`1917-09-25 [O.S.] / 10-08 [N.S.]` 托洛茨基当选） |
| [`POL-april-theses-1917.md`](../cards/policies/POL-april-theses-1917.md) | 1917.04–11（`+13 天`） | L10/L25/L75: `04-04/04-17`、`04-05/04-18`、`04-07/04-20` 正确；**L11: `end_ns: "1917-10-25" # 1917-10-12 [O.S.]`** | 十月起义为 `1917-10-25 [O.S.] / 1917-11-07 [N.S.]` | **FAIL（P0）**：L11 把十月夺权的俄历日期 `1917-10-25` 误当公历写入 `end_ns`，再倒减 13 天捏造出毫无史实依据的 `1917-10-12 [O.S.]` |
| [`ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md) | 1918–1921（1918-02-14 后纯公历） | `start_ns: "1918-01-01"`, `end_ns: "1921-08-31"`；正文未伪造俄历 | 纯公历区间合规 | **PASS（附 P1 校准）**：未犯改历后倒造俄历错误；`1918-01-01` 与 `1921-08-31` 为首尾占位符（马赫诺于 `1921-08-28` 越过德涅斯特河入罗马尼亚，见 `mawdsley_1987_civil_war_zh/ch09:610-611`） |
| [`POL-first-five-year-plan.md`](../cards/policies/POL-first-five-year-plan.md) | 1927–1929（纯公历） | `start_ns: "1928-04-01"`, `end_ns: "1929-12-31"`；L79 明确说明纯公历 | 纯公历区间合规 | **FAIL（P0 文字截断）**：L10 注释写 `1927-12-15 五大`，系将 `1927-12 十五大` 误打成假日期 `1927-12-15` 加错误届次 `五大`（十五大会期实为 `1927-12-02` 至 `12-19`）；L79 `1929年2月14日后` 笔误（改历实为 `1918年2月14日后`） |

---

## 二、 专项核查 B：机翻/输入法乱码幻觉词、伪造引号直引、职务/史实张冠李戴与断链核查

### 2.1 机翻与输入法乱码幻觉词（共查出 11 处，皆为 P0）

1. **`“江淮平原”`**（[`ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md) L26）：
   - **原文**：`以马匹拖拽机枪车的 тачанка 实现江淮平原高机动突袭。`
   - **审计裁定**：**严重中国地理名词穿越幻觉**！“江淮平原”位于中国江苏、安徽两省淮河与长江之间。马赫诺黑军驰骋的是 **乌克兰南部草原 / 黑海北岸草原（南俄第聂伯河左岸至亚速海黑土草原，Ukrainian / Pontic steppe）**。
2. **`“货架外特征”`**（[`ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md) L33）：
   - **原文**：`但无政府主义组织形式更具货架外特征`
   - **审计裁定**：英文 `off-the-shelf`（非现成/非标）的生硬机翻乱码，应改为 `更具无政府公社自治与高机动游击编制特征`。
3. **`“taчанka”`**（[`ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md) L40）与 **`“кorenizatsiya”`**（[`ORG-bund.md`](../cards/organizations/ORG-bund.md) L46）：
   - **原文**：`采用高度机动的 taчанka 战术`（L40）；`苏联 кorenizatsiya 在扩大意第绪公共领域同时`（L46）。
   - **审计裁定**：同一单词内混用拉丁字母与西里尔字母（`ta`+`чан`+`ka`；西里尔 `к`+拉丁 `orenizatsiya`），应统一为纯俄文 `тачанка` / `коренизация` 或纯拉丁转写 `tachanka` / `korenizatsiia`。
4. **`“南国武装解体”`**（[`ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md) L11）：
   - **原文**：`# 1921年夏马赫诺流亡，南国武装解体`
   - **审计裁定**：“南国”系汉语文学词汇，应改为 `南俄/乌克兰起义武装解体`。
5. **`“苏联汉诺夫”`**（[`ORG-petrograd-soviet.md`](../cards/organizations/ORG-petrograd-soviet.md) L25）：
   - **原文**：`1917-03-01 [O.S.] / 1917-03-14 [N.S.] 苏联汉诺夫见证士兵向索科洛夫口授的《第一号命令》全文`
   - **审计裁定**：输入法联想错字，将当事人 **苏汉诺夫（N. N. Sukhanov）** 误打为“苏联汉诺夫”。
6. **`“独立族自治州”`**（[`ORG-bund.md`](../cards/organizations/ORG-bund.md) L25）：
   - **原文**：`1898 年俄社民工党一大筹备中崩得以独立族自治州形式与会`
   - **审计裁定**：1898 年俄国社会民主工党一大决议规定崩得作为 **“仅在专门涉及犹太无产阶级的问题上独立的自治组织”（автономная организация）** 加入党，“独立族自治州”系现代行政区划名词乱码。
7. **`“年甸”`**（[`ORG-bund.md`](../cards/organizations/ORG-bund.md) L27）：
   - **原文**：`党的领导层（如年甸、利别尔）在1914年后分化为护国与反战`
   - **审计裁定**：与马克·利别尔（Mark Liber）并列的崩得最高理论领袖是 **弗拉基米尔·梅杰姆（Vladimir Medem / В. Д. Медем，又译麦德姆）**，俄国内战与一战中亦无任何名为“年甸”的崩得领袖，“年甸”系“梅杰姆”的严重字形/输入法乱码。
8. **`“等_nationality语境_”`**（[`ORG-bund.md`](../cards/organizations/ORG-bund.md) L47）：
   - **原文**：`(`CLM-carr-1952-nep-retreat-and-commanding-heights` 等_nationality语境_)`
   - **审计裁定**：夹杂未清理的英文草稿标记，且 `CLM-carr-1952-nep-retreat-and-commanding-heights` 论述的是 1921 年新经济政策退却与经济制高点，并非民族问题论断卡，应改为指向 [` sources/monographs/carr_1950_bolshevik_rev_v1_en/ch05_pages_126-150.md`](../sources/monographs/carr_1950_bolshevik_rev_v1_en/ch05_pages_126-150.md)（Carr 第一卷民族章节）。
9. **`“第 i 届省苏维埃”`**（[`ORG-provisional-government.md`](../cards/organizations/ORG-provisional-government.md) L76）：
   - **原文**：`列全俄第 i 届省苏维埃对中央权力的实际服从度统计（待 DATA-05 扩展）。`
   - **审计裁定**：残留循环变量占位符 `第 i 届` 且简写 `DATA-05`，应改为 `全俄第一届苏维埃代表大会及各省苏维埃对中央权力的实际服从度统计（待 DATA-05-1917-1920-factory-demographics-and-civil-war-forces 扩展）`。
10. **`“1927-12-15 五大”` / `“五大授权编制”`**（[`POL-first-five-year-plan.md`](../cards/policies/POL-first-five-year-plan.md) L10、L33）：
    - **原文**：L10 `# 剪刀差危机后计划论证高潮（亦可从1927-12-15 五大授权编制起算）`；L33 `五大授权编制并宣示集体化方向`。
    - **审计裁定**：将 `1927-12 十五大` 错切为 `1927-12-15 五大`（联共十五大会期为 `1927-12-02` 至 `12-19`，俄社民工党五大则是 1907 年伦敦代表大会！）。
11. **`“骑牛入市”`**（[`POL-first-five-year-plan.md`](../cards/policies/POL-first-five-year-plan.md) L35）：
    - **原文**：`“骑牛入市”均衡增长方案被最高方案排挤`
    - **审计裁定**：现代股市俗语乱入。布哈林与列宁晚年的经典比喻是 **“骑着农民的瘦马”（крестьянская лошадёнка）** 与 **“乌龟/蜗牛般速度”（черепашьим шагом）**，以及“发家致富”与城乡市场结合（`смычка`），绝无“骑牛入市”之说。

---

### 2.2 伪造引号直引与引文核查（对比全部 18 张被引 `CLM-*` 及 S 级原文）

经将 6 张卡片 T3 的全部引文逐字比对库内 `CLM-*` 原文直引栏与 S 级文献：
- **完全吻合项（16 条）**：
  - `ORG-provisional-government.md`：苏汉诺夫 `[pp. 124–125]` 与 `[p. 158]`、长谷川 `[p. 660 / PDF p. 681]`、盖达 `[p. 438]`、加利利 `[p. 169 / PDF p. 195]` 均与对应 `CLM-*` 逐字一致；
  - `ORG-petrograd-soviet.md`：苏汉诺夫 `[p. 282]`、长谷川 `[p. 633 / PDF p. 654]`、拉比诺维奇 `[pp. 391–392 / PDF pp. 414–415]`、博利 `[p. 130]` 均与对应 `CLM-*` 逐字一致；
  - `ORG-bund.md`：海姆森 `[p. 188]` 逐字一致；
  - `ORG-makhnovshchina.md`：霍布斯鲍姆 `ch06#L109-L114`、阿夫里奇 `[pp. 198-199]` 逐字一致；
  - `POL-april-theses-1917.md`：《四月提纲》第 2–3 条、洛吉诺夫 `[pp. 166–167]`、苏汉诺夫 `[pp. 276–277]` 逐字一致；
  - `POL-first-five-year-plan.md`：埃利希 `[pp. 167-168 / PDF pp. 182-183]`、费尔泽 `[p. 71 · PDF p. 77]` 逐字一致。
- **违规项（2 处，1 处 P0 自造英文加双引号、1 处 P1 转述套用引文块）**：
  1. **【P0 自撰英文改写句加双引号】[`ORG-bund.md`](../cards/organizations/ORG-bund.md)（L61–L62）**
     - **卡片原文**：
       `> "The secret organization acts as the flywheel driving the broad workers' party, much as the Bund had practised among the Jewish proletariat" [paraphrase anchored pp. 78–79]`
     - **对勘 [`CLM-getzler-1967-martov-1903-clause-one.md`](../historiography/claims/CLM-getzler-1967-martov-1903-clause-one.md)（L23、L30）**：Getzler 原书 pp. 78–79 的“飞轮（flywheel）”出现在第 23 行中文论证链概括中，而第 30 行英文原文直引实为：
       `> "The workers' party envisaged by Martov consisted of the organized professional revolutionaries 'plus the sum total of the active advanced elements of the proletariat'. What he and Axelrod and their supporters really had in mind was something like the Bund which had succeeded in embedding its excellent organization of professional revolutionaries in a large, active, and widespread party of the masses of the Jewish proletariat." [p. 79]`
     - **审计裁定**：严禁将卡片起草者自己用英文拼写的概要句打上双引号 `"..."` 放进原文引证栏（即便尾注写了 `paraphrase` 亦违反引文规范）。必须替换为 Getzler `[p. 79]` 的真实英文原句，或去掉英文与双引号改用中文转述。
  2. **【P1 中文转述误用引文块 `>`】[`ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md)（L61–L62）**
     - **卡片原文**：`> 马赫诺黑军突破白军后方防线，连克亚速海港口与叶卡捷琳诺斯拉夫，迫使邓尼金抽调精锐（ch13, 原书 pp. 213–214）。`
     - **对勘 [`CLM-mawdsley-1987-white-movement-structural-defeat.md`](../historiography/claims/CLM-mawdsley-1987-white-movement-structural-defeat.md)（L29）**：该句系论断卡“论证链条与依据”第 1 条的中文提炼，并非 Mawdsley 专书原文直引。应去掉行首 `>` 或明确标注“（论断卡提要转述）”。

---

### 2.3 职务、机构、内阁届次与历史事实张冠李戴（共 9 处硬伤）

1. **【P0 马赫诺与弗兰格尔结盟伪史 + 剿灭统帅张冠李戴】[`ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md)（L26、L55）**
   - **卡片原文 L26**：`` `1920` 曾与弗兰格尔结盟打击红军，旋即再与红军签约对付弗兰格尔，协议破裂后遭图哈切夫斯基两面夹击。``
   - **卡片原文 L55**：`| IV | 1920下 | 弗兰格尔克里米亚政府 | 短暂再次结盟后破裂 |`（表意含混，易与 L26 联动误读为与弗兰格尔结盟）
   - **对勘 [`sources/monographs/mawdsley_1987_civil_war_zh/ch09_第二部分_1919_白军之年_part_1.md`](../sources/monographs/mawdsley_1987_civil_war_zh/ch09_第二部分_1919_白军之年_part_1.md#L608-L610)、[`ch10`](../sources/monographs/mawdsley_1987_civil_war_zh/ch10_第二部分_1919_白军之年_part_2.md#L417) 与 [`ch15`](../sources/monographs/mawdsley_1987_civil_war_zh/ch15_第三部分_1920_胜利之年_part_2.md#L970)**：
     - **第一处史实颠倒**：1920 年夏弗兰格尔派使者向马赫诺提议结盟反共，**马赫诺断然拒绝并处决了弗兰格尔信使**（`ch09:608`：“1920 年，马赫诺又拒绝了弗兰格尔与其结盟的提议”；`ch15:970`：“马赫诺都拒绝加入白军”）；同年 10 月马赫诺与红军签订《斯塔罗别利斯克协定》，派黑军主力协助红军强渡锡瓦什海湾攻克克里米亚击溃弗兰格尔。马赫诺**从未与弗兰格尔结盟打击红军**！
     - **第二处统帅张冠李戴**：1920 年 11 月末红军攻克克里米亚后撕毁协议、指挥南方面军及乌克兰与克里米亚武装力量围剿马赫诺黑军的统帅是 **米哈伊尔·伏龙芝（M. V. Frunze）**（同卡 L36 边表已正确写明 `PER-frunze | final-campaign-commander`），而**绝非图哈切夫斯基**（图哈切夫斯基 1920 年指挥西方面军对波兰作战，1921 年春镇压喀琅施塔得与坦波夫起义，从未指挥南线剿灭马赫诺）！

2. **【P0 苏维埃执委会主席张冠李戴 + 8月31日表决机构错位】[`ORG-petrograd-soviet.md`](../cards/organizations/ORG-petrograd-soviet.md)（L36、L59）**
   - **卡片原文 L36**：`| PER-tsereteli | chairman-of-ie | 1917.03–1917.09 | 任内务与邮电部长同时主导执委会，推动社会主义入阁 |`
   - **卡片原文 L59**：`| 1917-08-31 | 执委会夜间会议首次通过布尔什维克决议（需与后续选举记票分读） |`
   - **对勘 [`PER-tsereteli.md`](../cards/people/PER-tsereteli.md) 与 [`CLM-galili-1989-revolutionary-defensism.md`](../historiography/claims/CLM-galili-1989-revolutionary-defensism.md)**：
     - **职务错位（L36）**：1917 年 2 月 27 日至 9 月 9 日 [O.S.] 彼得格勒苏维埃及其执行委员会（Исполком）的正式**主席（Chairman）始终是齐赫伊泽（N. S. Chkheidze）**！策烈铁里是执委会常务局（“星室”）核心领袖与演说主将，并非执委会主席（关系类型应改为 `de-facto-leader-of-ec` 或 `star-chamber-leader`，不得标为 `chairman-of-ie`）。
     - **机构错位（L59）**：`1917-08-31 [O.S.] / 1917-09-13 [N.S.]` 夜间至次日凌晨以 `279 : 115`（51 弃权）首次通过布尔什维克《关于政权问题》决议的是 **彼得格勒苏维埃全体大会（Plenum / Пленум Петросовета）**，恰恰是因为孟什维克—社革党把持的**执委会/主席团**在全体大会上败北，齐赫伊泽与策烈铁里才于 `1917-09-09 [O.S.] / 1917-09-22 [N.S.]` 全体大会信任投票再度落败后辞职！写成“执委会夜间会议通过布尔什维克决议”颠倒了全会与执委会的对立关系。

3. **【P0 1917年9月25日第三届联立内阁被误定性为“无社会主义者的技术内阁” + 3月3日内阁会议误作“政府宣言”】[`ORG-provisional-government.md`](../cards/organizations/ORG-provisional-government.md)（L10、L25、L28、L57–58、L76）**
   - **卡片原文 L28 & L58**：`` `1917-09-25 [O.S.] / 1917-10-08 [N.S.]` 克伦斯基组成无社会主义者的“技术内阁”``；L58 `克伦斯基技术内阁 | 1917-10-08 起`。
   - **审计裁定**：**内阁性质严重张冠李戴**！科尔尼洛夫事件后，克伦斯基于 `1917-09-01 [O.S.] / 1917-09-14 [N.S.]` 成立过为期三周的五人“执政内阁（Директория）”；而于 **`1917-09-25 [O.S.] / 1917-10-08 [N.S.]` 组建的第四届临时政府实为“第三届联合内阁（Third Coalition Cabinet）”**，其中既包括立宪民主党人（科诺瓦洛夫、特列тья科夫、斯米尔诺夫、基什金等），也包含 **6 名温和派社会主义部长**（孟什维克格沃兹杰夫任劳工部长、尼基京任内务兼邮电部长、马良托维奇任司法部长，以及普罗科波维奇、利沃夫斯基等），绝非“无社会主义者的技术内阁”！
   - **卡片原文 L57**：`克伦斯基第二届联立 | 1917-07-21 起` —— `1917-07-08 [O.S.] / 1917-07-21 [N.S.]` 是克伦斯基接替李沃夫出任看守内阁总理之日，而 **第二届联立内阁** 历经半月难产，实于 **`1917-07-24 [O.S.] / 1917-08-06 [N.S.]`**（7月23日夜至24日）方才正式组成（参 [`PER-tsereteli.md`](../cards/people/PER-tsereteli.md) L30）。
   - **卡片原文 L10、L25、L76**：L10 写 `1917-03-02 [O.S.] 米留可夫等内阁成立并自承“全部完满权力”`，L25 写 `1917-03-03 [O.S.] / 1917-03-16 [N.S.] 政府宣言宣布承担全部完满政治权力`，L76 写 `1917-03-16 全权宣言`。对照 [`CLM-hasegawa-2018-dual-power-origins.md`](../historiography/claims/CLM-hasegawa-2018-dual-power-origins.md) L25–28，3 月 2 日夜议定并于 3 月 3 日见报的是与苏维埃妥协的《临时政府宣言》，而宣称继承“全部完满权力（вся полнота власти）”、排挤罗将柯并切断同第四届国家杜马法统联系的，是 **3 月 3 日 [O.S.] / 3 月 16 日 [N.S.] 临时政府首次正式闭门内阁会议（First Cabinet Meeting）的决议**，不能把闭门内阁会议决议混同于公开发表的《政府宣言》。

4. **【P0 1929年全苏苏维埃五大误作“全俄五大” + 四月全会与十六次党代表会议混同】[`POL-first-five-year-plan.md`](../cards/policies/POL-first-five-year-plan.md)（L26、L58）**
   - **卡片原文 L26**：`` `1929-04-16` 至 `23` **联共（布）中央委员会暨中央监察委员会联席会议（第十六次代表会议）** 讨论工业速度与农村政策；`1929-05` **第五届全俄苏维埃代表大会** 正式批准 **最高方案** 控制数字``
   - **审计裁定**：
     - **第一处会议嫁接**：`1929-04-16` 至 `04-23` 召开的是 **联共（布）中央与中监委四月联席全会**（[`MTG-1929-04-cc-joint-plenum.md`](../cards/meetings/MTG-1929-04-cc-joint-plenum.md)，主攻右倾问题）；而审议通过第一个五年计划最高方案的 **联共（布）第十六次代表会议（XVI конференция ВКП(б)）** 则于 **`1929-04-23` 至 `04-29`** 召开。二者是前后衔接但性质不同的两个党内会议，不能用括号等同！
     - **第二处国体/届次错乱**：1929 年 5 月 20–28 日批准一五计划最高方案的是 **苏联第五次全国苏维埃代表大会（简称“全苏苏维埃五大”，V Всесоюзный съезд Советов СССР）**，而非“第五届全俄苏维埃代表大会”（“全俄苏维埃五大”是 1918 年 7 月在莫斯科大剧院召开的俄罗斯联邦第五次苏维埃代表大会，1929 年 5 月的俄罗斯联邦苏维埃大会已是第十四届）。

5. **【P0 《四月提纲》土地纲领张冠李戴 + 《真理报》态度失实 + 第9条表文错字】[`POL-april-theses-1917.md`](../cards/policies/POL-april-theses-1917.md)（L20、L45、L59）**
   - **卡片原文 L20**：`并倡议银行国有化、土地社会化与改党名`
   - **对勘 [`1917-04-04_april-theses.md`](../sources/web-archive/E06_E10_turning_points/1917-04-04_april-theses.md)（L70–77，第6、7条）**：《四月提纲》第 6 条明确主张 **“没收地主的全部土地。把国内一切土地收归国有（Национализация всех земель）”**（同卡 L58 亦正确写为“土地国有、银行合并”），而“土地社会化（социализация земли）”是社会革命党（`ORG-psr`）的纲领术语（列宁直至 1917 年 10 月《土地法令》才借用社革党的农民委托书）。同时第 7 条原文为“立刻把全国所有银行合并成一个全国性的银行，由工人代表苏维埃进行监督”。L20 应改为 `并倡议土地国有化、全国银行合并归苏维埃监督与更改党名`。
   - **卡片原文 L45**：`《真理报》一周后才拒收全文`
   - **对勘 [`CLM-sukhanov-1922-lenin-april-arrival-shock.md`](../historiography/claims/CLM-sukhanov-1922-lenin-april-arrival-shock.md) 与 [`CLM-loginov-lenin-vs-party-moderates-1917.md`](../historiography/claims/CLM-loginov-lenin-vs-party-moderates-1917.md)（L31）**：列宁 4 月 4 日宣读提纲，**3 天后（4 月 7 日 [O.S.]）《真理报》第 26 号即全文刊登了《四月提纲》**，次日（4 月 8 日 [O.S.]）加米涅夫撰文《我们的分歧》代表编辑部声明列宁的总公式“令人无法接受（unacceptable）”。所谓“一周后才拒收全文”完全违背同卡 L25 已写明的事实！
   - **卡片原文 L59**：`| 9–10 | 改国际名称、建新国际 | 党派 переименование 动议 |` —— 第 9 条是 **更改党的名称（改称共产党）**，而非“改国际名称”。

6. **【P1 波兰崩得结局失实 + 民族文化自治大会地点错植】[`ORG-bund.md`](../cards/organizations/ORG-bund.md)（L20、L28、L69）**
   - **卡片原文 L20、L28**：L20 `最终并入俄共（布）及波兰社民党与立宪路线`；L28 `波兰侧则续存于改组后的波兰社民工党`。
   - **审计裁定**：1918–1939 年波兰第二共和国时期，**波兰崩得（Ogólny Żydowski Związek Robotniczy „Bund” w Polsce）始终作为独立的犹太社会主义政党存续并发展壮大**（1930 年代末成为波兰犹太市政选举第一大党），直到二战爆发与大屠杀，并未并入什么“波兰社民工党”。
   - **卡片原文 L69**：`民族文化自治 1907 布拉格大会文稿` —— 崩得确立民族文化自治纲领的是 **1901 年比亚韦斯托克第四次代表大会（4th Congress in Białystok）** 与 **1905 年苏黎世第六次代表大会 / 1906 年利沃夫第七次代表大会**；崩得并无“1907 布拉格大会”（1912 年布拉格会议系列宁主持的俄社民工党第六次全俄代表会议）。

---

### 2.4 库内文件路径断链与错配核查（共 5 处断链）

| 所在卡片与行号 | 卡片所写路径 | 存在性 | 正确库内路径 / 修正方案 |
| :--- | :--- | :--- | :--- |
| [`ORG-petrograd-soviet.md`](../cards/organizations/ORG-petrograd-soviet.md) L77 | `rabinowitch_2007_in_power/`（未带前缀，紧跟 `sources/monographs/rabinowitch_1968_prelude_zh/`） | 路径不完整 | 补全为 `` `sources/monographs/rabinowitch_2007_in_power/` `` 及 `` `reading-notes/rabinowitch_2007_in_power/` `` |
| [`ORG-bund.md`](../cards/organizations/ORG-bund.md) L68 | `` `reading-notes/blanc_2021_borderlands/` `` | **FALSE（断链）** | 改为 `` `reading-notes/blanc_2021_rev_sd/` `` |
| [`ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md) L67–68 | `` `sources/monographs/mawdsley_1987_civil_war/`（尤其 ch13 南线 1919、ch16–19 1920）``；`` `sources/monographs/hobsbawm_1959_primitive_rebels_zh/ch06`, `ch31–32` `` | **FALSE（文件名不匹配）** | Mawdsley 中译提取目录为 `` `sources/monographs/mawdsley_1987_civil_war_zh/` ``（1920 南线在 `ch15`–`ch16`，`ch17–18` 为参考书目）；Hobsbawm 精确文件为 `ch06_第二章_绿林好汉.md`、`ch31_六_古赖波勒叶的无政府主义公社.md`、`ch32_七_农民不信任政府.md` |
| [`POL-april-theses-1917.md`](../cards/policies/POL-april-theses-1917.md) L72 | `` `reading-notes/rabinowitch_1968_prelude/` `` | **FALSE（断链）** | 改为 `` `sources/monographs/rabinowitch_1968_prelude_zh/` `` 及 `` `reading-notes/RN-01-rabinowitch-opening.md` `` |
| [`POL-first-five-year-plan.md`](../cards/policies/POL-first-five-year-plan.md) L72–73 | `` `sources/monographs/davies_soviet_history/` ``；`` `sources/monographs/carr_bolshevik_rev/` `` | **FALSE（两处均断链）** | 改为 `` `sources/monographs/davies_industrialisation_en/` ``、`` `sources/monographs/davies_1980_collective_farm_zh/` `` 与 `` `sources/monographs/carr_davies_1969_foundations_v1p1/` ``（注：NEP 末期计划机构在 Carr & Davies《计划经济的基础 1926–1929》，不在《布尔什维克革命 1917–1923》） |

---

## 三、 逐卡审计详情小结

1. **[`ORG-provisional-government.md`](../cards/organizations/ORG-provisional-government.md)**：双历算术全部准确，四派史学光谱（Gaida / Hasegawa / Galili / Rabinowitch）结构均衡、引文真实。主要硬伤在于把 `1917-09-25 [O.S.] / 1917-10-08 [N.S.]` 成立的 **第三届联合内阁** 误称为“无社会主义者的技术内阁”（P0），把 `1917-03-03 [O.S.] / 1917-03-16 [N.S.]` 首次闭门内阁会议确立“全部完满权力”并撇开杜马的决定误称为公开发表的《政府宣言》（P1），将第二届联立内阁组成日（`07-24 [O.S.] / 08-06 [N.S.]`）与克伦斯基接任总理日（`07-08 [O.S.] / 07-21 [N.S.]`）合并（P1），以及 L76 残留 `第 i 届` 变量占位符（P1）。
2. **[`ORG-petrograd-soviet.md`](../cards/organizations/ORG-petrograd-soviet.md)**：引文全部精准锚定。主要硬伤在于 L25 输入法幻觉词 `苏联汉诺夫`（P0），L20/L28/L59/L80 四处将俄历 `1917-08-31` 漏标双历 `1917-08-31 [O.S.] / 1917-09-13 [N.S.]` 并混入公历表（P0），L36 将策烈铁里误标为苏维埃执委会主席 `chairman-of-ie`（主席实为齐赫伊泽，P0），以及 L59 将通过 8 月 31 日布尔什维克决议的“苏维埃全体大会”误作“执委会夜间会议”（P0）。
3. **[`ORG-bund.md`](../cards/organizations/ORG-bund.md)**：`1897-09-25 [O.S.] / 1897-10-07 [N.S.]`（+12 天）与 1903 伦敦公历完全准确。主要硬伤在于 L25 `独立族自治州` 与 L27 `年甸`（实为梅杰姆 Medem）两处严重乱码（P0），L46 俄英混拼 `кorenizatsiya` 与 L47 `_nationality语境_`（P0），L62 将自撰英文改写句打上双引号充当 Getzler 原文（P0），L20/L28 误称波兰崩得并入“波兰社民工党”（P1），L68 路径断链与 L69“1907 布拉格大会”错植（P1）。
4. **[`ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md)**：纯公历合规，Hobsbawm 与 Avrich 引文准确。主要硬伤在于 L26 惊现中国地理名词 **`江淮平原`**（P0）、捏造 **`1920 曾与弗兰格尔结盟打击红军`** 并把南线红军统帅 **伏龙芝** 张冠李戴为 **图哈切夫斯基**（P0），以及 L33 `货架外特征`、L40 `taчанka` 乱码（P0）。
5. **[`POL-april-theses-1917.md`](../cards/policies/POL-april-theses-1917.md)**：宣读与发表双历（`04-04/04-17`、`04-07/04-20`）及 S 级正文直引准确。主要硬伤在于 L11 将俄历 `1917-10-25` 当公历填入 `end_ns` 并倒减 13 天造出假俄历 `1917-10-12 [O.S.]`（P0），L20 将提纲第 6 条“土地国有化”误写成社革党的“土地社会化”（P0），L45 捏造“《真理报》一周后才拒收全文”（P0），L59 将第 9 条“改党名”误作“改国际名称”（P1），以及 L72 路径断链（P1）。
6. **[`POL-first-five-year-plan.md`](../cards/policies/POL-first-five-year-plan.md)**：Erlich、Davies、Filtzer 引文与核心数据扎实。主要硬伤在于 L10、L33 将“1927-12 十五大”截断为 `1927-12-15 五大` / `五大`（P0），L26 将 `04-16–23` 四月联席全会与 `04-23–29` 第十六次党代表会议混为一谈、并将 1929 年 5 月 **全苏苏维埃五大** 误写成“第五届全俄苏维埃代表大会”（P0），L35 乱用股市词汇 `“骑牛入市”`（P0），L10/L47 混入 1923 年剪刀差论断卡 `CLM-carr-1954-scissors-crisis-mechanics`（P1），L72–73 两处馆藏目录断链与 L79 `1929年2月14日后` 笔误（P1）。

---

## 四、 逐行可执行修改清单（Actionable Line-by-Line Checklist）

> 请后续可写权限 Agent 严格按以下行号与替换文本逐条执行修改，完成后复跑 `python scripts/kb.py audit-graph`：

### 4.1 [`cards/organizations/ORG-provisional-government.md`](../cards/organizations/ORG-provisional-government.md)

- [ ] **L10**（P1 区分 3月2日组阁与 3月3日首次内阁会议）：
  - 原文：`start_ns: "1917-03-15" # 1917-03-02 [O.S.] 米留可夫等内阁成立并自承“全部完满权力”`
  - 改为：`start_ns: "1917-03-15" # 1917-03-02 [O.S.] 国家杜马临时委员会宣布临时政府成立（次日首次内阁会议自承“全部完满权力”）`
- [ ] **L20**（P0 修正内阁构成概述）：
  - 原文：`经四届内阁（李沃夫独任、三次社会主义联立）未能稳住宪政民主，终为十月起义推翻。`
  - 改为：`经四届内阁（李沃夫首届、五月至九月三次资产阶级—社会主义联立内阁及九月短期五人执政内阁）未能稳住宪政民主，终为十月起义推翻。`
- [ ] **L25**（P1 区分公开发表的《政府宣言》与 3月3日首次内阁闭门会议）：
  - 原文：`` `1917-03-03 [O.S.] / 1917-03-16 [N.S.]` 政府宣言宣布承担**全部完满政治权力**，并切断与第四届国家杜马机制性联系，代议制根基反被自由派亲手削弱（`CLM-hasegawa-2018-dual-power-origins`）。``
  - 改为：`` `1917-03-03 [O.S.] / 1917-03-16 [N.S.]` 临时政府首次正式内阁会议排挤罗将柯，宣布政府掌握不受杜马制约的**全部完满权力（вся полнота власти）**并切断与第四届国家杜马机制性联系，代议制根基反被自由派亲手削弱（`CLM-hasegawa-2018-dual-power-origins`）。``
- [ ] **L27–L28**（P0 修正第二、三届联立内阁日期与性质，纠正“无社会主义者的技术内阁”硬伤）：
  - 原文：
    ```markdown
    - **克伦斯基独掌与第三届政府（1917.07–09）**：`1917-07-08 [O.S.] / 1917-07-21 [N.S.]` 克伦斯基接任总理；临时政府下决心派惩戒部队恢复前线秩序，却无法满足工兵自决诉求，权威加速流失（`CLM-rabinowitch-1968-grassroots-soldier-sailor-radicalism`）。八月科尼洛夫兵谏失败后，临时政府威信崩塌，苏维埃左翼决议首次占上风。
    - **第四届技术与终局（1917.09–10）**：`1917-09-25 [O.S.] / 1917-10-08 [N.S.]` 克伦斯基组成无社会主义者的“技术内阁”，列强承认与全俄民主会议均未能挽回局势；`1917-10-26 [O.S.] / 1917-11-08 [N.S.]` 彼得格勒军事革命委员会接管首都据点，内阁成员在冬宫被驱散或被捕，正式终结。
    ```
  - 改为：
    ```markdown
    - **克伦斯基接任总理与第二届联立内阁（1917.07–08）**：`1917-07-08 [O.S.] / 1917-07-21 [N.S.]` 克伦斯基接任总理，并于 `1917-07-24 [O.S.] / 1917-08-06 [N.S.]` 组成第二届联立内阁；临时政府试图恢复前线军纪与死刑，却无法满足工兵诉求，权威加速流失（`CLM-rabinowitch-1968-grassroots-soldier-sailor-radicalism`）。八月科尔尼洛夫事件挫败后，自由派阁员辞职、临时政府威信崩塌，苏维埃左翼决议首次占上风。
    - **五人执政内阁、第三届联立内阁与终局（1917.09–10）**：`1917-09-01 [O.S.] / 1917-09-14 [N.S.]` 克伦斯基一度设五人“执政内阁（Директория）”，旋于 `1917-09-25 [O.S.] / 1917-10-08 [N.S.]` 再度吸纳立宪民主党人与温和社会主义者（格沃兹杰夫、尼基京等）组成第三届联立内阁（第四届政府），全俄民主会议与预备议会均未能挽回局势；`1917-10-26 [O.S.] / 1917-11-08 [N.S.]` 彼得格勒军事革命委员会攻占冬宫，留守阁员被捕，正式终结。
    ```
- [ ] **L38–L39**（P1 边表补齐双历）：
  - 原文：`1917.07.03–07.05 [O.S.]` 与 `1917.10.25–26 [O.S.]`
  - 改为：`1917.07.03–05 [O.S.] / 07.16–18 [N.S.]` 与 `1917.10.25–26 [O.S.] / 11.07–08 [N.S.]`
- [ ] **L55–L58**（P0 修正 3.1 四届内阁对照表）：
  - 原文：
    ```markdown
    | 李沃夫第一届 | 1917-03-15 起 | G. E. Lvov | 与苏维埃协议、土地与和平拖延；4月米留可夫照会 |
    | 首届联立 | 1917-05-18 起 | Lvov + 社会主义阁员 | 六月攻势、士兵抗调；七月镇压 |
    | 克伦斯基第二届联立 | 1917-07-21 起 | A. F. Kerensky | 前线惩戒旅、立宪会议档期争议 |
    | 克伦斯基技术内阁 | 1917-10-08 起 | Kerensky | 科尼洛夫后遗症；终被十月起义终结 |
    ```
  - 改为：
    ```markdown
    | 第一届（李沃夫内阁） | 1917-03-15 [03-02 O.S.] 起 | G. E. Lvov | 与苏维埃协议、土地与和平拖延；米留可夫照会引爆四月危机 |
    | 第二届（第一届联立） | 1917-05-18 [05-05 O.S.] 起 | G. E. Lvov（含6名社会主义阁员） | 六月攻势溃败、驻军抗调；七月事变与李沃夫辞职 |
    | 第三届（第二届联立） | 1917-07-21 [07-08 O.S.] 继任 / 08-06 [07-24 O.S.] 组阁 | A. F. Kerensky | 国务会议极化、科尔尼洛夫事件（9月14日[N.S.]起暂设五人执政内阁） |
    | 第四届（第三届联立） | 1917-10-08 [09-25 O.S.] 起 | A. F. Kerensky（含立宪民主党与温和社会主义阁员） | 预备议会空转、全面权威瘫痪；11月8日[N.S.]冬宫陷落终结 |
    ```
- [ ] **L76**（P1 清理占位符 `第 i 届` 并补全 `DATA-05` ID）：
  - 原文：`临时政府部长会议速记、1917-03-16 全权宣言俄文原文与地方州长官承认电报；列全俄第 i 届省苏维埃对中央权力的实际服从度统计（待 DATA-05 扩展）。`
  - 改为：`临时政府部长会议记录（Журналы заседаний）、1917-03-15 [03-02 O.S.] 政府宣言及 1917-03-16 [03-03 O.S.] 首次内阁会议俄文记录；全俄第一届苏维埃代表大会及各省苏维埃对中央权力的实际服从度统计（参 DATA-05-1917-1920-factory-demographics-and-civil-war-forces 后续扩展）。`

---

### 4.2 [`cards/organizations/ORG-petrograd-soviet.md`](../cards/organizations/ORG-petrograd-soviet.md)

- [ ] **L20**（P0 补齐 8 月 31 日双历）：
  - 原文：`夏秋左翼浪潮下于8月31日首次通过布尔什维克决议，托洛茨基任主席`
  - 改为：`夏秋左翼浪潮下于俄历8月31日（公历9月13日）首次通过布尔什维克决议，托洛茨基随后当选主席`
- [ ] **L25**（P0 修正输入法乱码 `苏联汉诺夫`）：
  - 原文：`` `1917-03-01 [O.S.] / 1917-03-14 [N.S.]` 苏联汉诺夫见证士兵向索科洛夫口授的**《第一号命令》**全文``
  - 改为：`` `1917-03-01 [O.S.] / 1917-03-14 [N.S.]` 苏汉诺夫见证士兵向索科洛夫口授的**《第一号命令》**全文``
- [ ] **L28**（P0 补齐 8 月 31 日与托洛茨基当选主席双历）：
  - 原文：`` `1917-08-31` 夜苏维埃首次通过布尔什维克主导决议；托洛茨基于九月当选主席。``
  - 改为：`` `1917-08-31 [O.S.] / 1917-09-13 [N.S.]` 夜苏维埃全体大会首次通过布尔什维克《关于政权问题》决议；`1917-09-09 [O.S.] / 1917-09-22 [N.S.]` 齐赫伊泽—策烈铁里主席团辞职，`1917-09-25 [O.S.] / 1917-10-08 [N.S.]` 托洛茨基当选苏维埃主席。``
- [ ] **L36**（P0 修正策烈铁里职务张冠李戴 `chairman-of-ie`）：
  - 原文：`| PER-tsereteli | chairman-of-ie | 1917.03–1917.09 | 任内务与邮电部长同时主导执委会，推动社会主义入阁 | CLM-galili-1989-revolutionary-defensism |`
  - 改为：`| PER-tsereteli | star-chamber-leader | 1917.03–1917.09 | 作为执委会常务局（“星室”）核心领袖（主席为齐赫伊泽）兼邮电、代理内务部长，主导革命护国与联立入阁路线 | CLM-galili-1989-revolutionary-defensism |`
- [ ] **L39–L40**（P1 边表补齐双历）：
  - 原文：`1917.07.03–05 [O.S.]` 与 `1917.10.25–26 [O.S.]`
  - 改为：`1917.07.03–05 [O.S.] / 07.16–18 [N.S.]` 与 `1917.10.25–26 [O.S.] / 11.07–08 [N.S.]`
- [ ] **L59**（P0 修正公历列混入俄历 `1917-08-31` 及将“苏维埃全体大会”误作“执委会”）：
  - 原文：``| `1917-08-31` | 执委会夜间会议首次通过布尔什维克决议（需与后续选举记票分读） |``
  - 改为：``| `1917-09-13` [08-31 O.S.] | 苏维埃全体大会夜间会议首次通过布尔什维克决议（`279:115:51`），击败执委会多数派；`1917-10-08` [09-25 O.S.] 托洛茨基接任主席 |``
- [ ] **L77**（P1 补全馆藏路径前缀）：
  - 原文：``- `sources/monographs/rabinowitch_1968_prelude_zh/`、`rabinowitch_2007_in_power/` ``
  - 改为：``- `sources/monographs/rabinowitch_1968_prelude_zh/`、`sources/monographs/rabinowitch_2007_in_power/` ``
- [ ] **L80**（P0 补齐双历）：
  - 原文：`` `1917-08-31` 布尔什维克决议表决委员名单与门外驻军态度``
  - 改为：`` `1917-08-31 [O.S.] / 1917-09-13 [N.S.]` 布尔什维克决议表决代表名单与门外驻军态度``

---

### 4.3 [`cards/organizations/ORG-bund.md`](../cards/organizations/ORG-bund.md)

- [ ] **L11**（P1 精准对齐俄国崩得明斯克第十三次特别代表大会并党日期）：
  - 原文：`end_ns: "1921-03-21" # 俄共（布）十大前后地方组织并入一党专政体系`
  - 改为：`end_ns: "1921-03-12" # 1921年3月5–12日俄国崩得明斯克第十三次代表会议决议解散并入俄共（布）（波兰崩得独立存续至二战）`
- [ ] **L20**（P1 修正波兰崩得结局）：
  - 原文：`提出民族文化自治理论，内战后再度分裂，最终并入俄共（布）及波兰社民党与立宪路线。`
  - 改为：`提出民族文化自治理论；内战后苏俄境内组织于1921年3月并入俄共（布），波兰崩得则作为独立犹太社会主义政党存续至二战时期。`
- [ ] **L25**（P0 修正乱码词 `独立族自治州`）：
  - 原文：`1898 年俄社民工党一大筹备中崩得以独立族自治州形式与会，推动将民族问题写入建党议程`
  - 改为：`1898 年俄社民工党一大筹备与召开中，崩得以“仅在专门涉及犹太无产阶级的问题上独立的自治组织”形式入党，推动将民族问题写入建党议程`
- [ ] **L26**（P1 补充二大退场票数异文说明）：
  - 原文：`崩得以**5:38–41**左右败北后退场，客观上消除部分反对派票源，使列宁派在随后中央机构选举中取得五票多数`
  - 改为：`崩得五名代表（大会记录作 5 票，Haimson 记作 4 票）在联邦制与唯一代表权条款败北后退场，连同经济派 2 票退场客观上改变大会算术，使列宁派从党章第一条的少数（22:28）反转为后续中央机构选举的多数`
- [ ] **L27**（P0 修正人名乱码 `年甸` -> `弗拉基米尔·梅杰姆`）：
  - 原文：`党的领导层（如年甸、利别尔）在1914年后分化为护国与反战`
  - 改为：`党的领导层（如弗拉基米尔·梅杰姆 Vladimir Medem、马克·利别尔 Mark Liber）在1914年后分化为国际主义反战派与护国派`
- [ ] **L28**（P1 修正波兰崩得史实）：
  - 原文：`1921 年前后俄共（布）取缔独立派别，崩得组织并入地方党务网络，波兰侧则续存于改组后的波兰社民工党`
  - 改为：`1921 年 3 月俄国共产崩得（Komfarband）与俄国崩得多数派在明斯克会议上解散并入俄共（布）（设犹太部 Yevsektsiya），而波兰境内的崩得则作为独立政党在波兰第二共和国持续活动至 1940 年代`
- [ ] **L46–L47**（P0 修正俄英混拼 `кorenizatsiya` 与草稿残留 `_nationality语境_`）：
  - 原文：
    ```markdown
      - **[民族政策比较 / George Liber]** (`CLM-liber-1992-korenizatsiia-paradox-late-1920s`)：苏联 `кorenizatsiya` 在扩大意第绪公共领域同时拒绝崩得式超领土文化自治，制造无法被中央完全消化的民族诉求。
      - **[制度连续论 / E. H. Carr]** (`CLM-carr-1952-nep-retreat-and-commanding-heights` 等_nationality语境_)：崩得并入标志布尔什维克对社会主义少民组织的吞并逻辑，与孟什维克、乌克兰社民党命运同构。
    ```
  - 改为：
    ```markdown
      - **[民族政策比较 / George Liber]** (`CLM-liber-1992-korenizatsiia-paradox-late-1920s`)：苏联本土化政策（`коренизация` / `korenizatsiia`）在扩大意第绪语公共领域的同时拒绝崩得式超领土民族文化自治，改以领土苏维埃制吸纳民族诉求。
      - **[制度吸纳论 / E. H. Carr]**（`sources/monographs/carr_1950_bolshevik_rev_v1_en/ch05_pages_126-150.md`）：崩得在苏俄境内的分裂与并入标志布尔什维克对少数民族社会主义政党的制度化吸收逻辑，与乌克兰借道左翼独立派并党的轨迹同构。
    ```
- [ ] **L61–L62**（P0 将自撰英文改写句替换为 Getzler `[p. 79]` 真实原文直引）：
  - 原文：
    ```markdown
    - **Getzler 论马尔托夫“飞轮”与崩得参照**（`CLM-getzler-1967-martov-1903-clause-one`）：
      > "The secret organization acts as the flywheel driving the broad workers' party, much as the Bund had practised among the Jewish proletariat" `[paraphrase anchored pp. 78–79]`
    ```
  - 改为：
    ```markdown
    - **Getzler 论马尔托夫建党观对崩得群众党模式的参照**（`CLM-getzler-1967-martov-1903-clause-one`）：
      > "The workers' party envisaged by Martov consisted of the organized professional revolutionaries 'plus the sum total of the active advanced elements of the proletariat'. What he and Axelrod and their supporters really had in mind was something like the Bund which had succeeded in embedding its excellent organization of professional revolutionaries in a large, active, and widespread party of the masses of the Jewish proletariat." `[p. 79]`
    ```
- [ ] **L68–L69**（P1 修复 `reading-notes` 断链与“1907布拉格大会”史实错误）：
  - 原文：
    ```markdown
    - `reading-notes/blanc_2021_borderlands/`（1905 边疆苏维埃）
    - 崩得专项 `CLM-*` 仍稀缺：民族文化自治 1907 布拉格大会文稿、1917 年崩得第七代表大会记录待 `close-reader` 入库。
    ```
  - 改为：
    ```markdown
    - `reading-notes/blanc_2021_rev_sd/`（1905 与 1917 边疆社民党）
    - 崩得专项 `CLM-*` 仍稀缺：1901 年比亚韦斯托克四大及 1905 年苏黎世六大“民族文化自治”决议文本、1917 年至 1921 年崩得代表大会记录待 `close-reader` 入库。
    ```

---

### 4.4 [`cards/organizations/ORG-makhnovshchina.md`](../cards/organizations/ORG-makhnovshchina.md)

- [ ] **L11**（P1 修正 `南国` 措辞并注明越境确切日）：
  - 原文：`end_ns: "1921-08-31" # 1921年夏马赫诺流亡，南国武装解体`
  - 改为：`end_ns: "1921-08-28" # 1921年8月28日马赫诺率残部渡过德涅斯特河流亡罗马尼亚，南乌克兰起义军主力解体`
- [ ] **L26**（P0 清除 `江淮平原` 幻觉词、纠正“与弗兰格尔结盟”伪史及“图哈切夫斯基”统帅张冠李戴）：
  - 原文：``- **黑军、тачанка 与三方回旋（1918–1920）**：起义军改编为 **革命起义军（РПАУ，“黑军”）**，以马匹拖拽机枪车的 **тачанка** 实现江淮平原高机动突袭。`1918–1919` 与红军合作对抗德意志方面的乌克兰独立军与白军；邓尼金1919年进攻时马赫诺反复撕开其后方，迫邓尼金抽调精锐（`CLM-mawdsley-1987-white-movement-structural-defeat`）。`1920` 曾与弗兰格尔结盟打击红军，旋即再与红军签约对付弗兰格尔，协议破裂后遭图哈切夫斯基两面夹击。``
  - 改为：``- **黑军、тачанка 与三方回旋（1918–1920）**：起义军改编为 **乌克兰革命起义军（РПАУ，“黑军”）**，以马匹拖拽机枪车的 **тачанка（机枪马车）** 在乌克兰南部黑土草原实现高机动突袭。`1918–1919` 先后抗击德奥占领军、彼得留拉督政府与白军；1919年秋邓尼金进逼莫斯科最危急时刻，马赫诺突破白军后方防线连克梅利托波尔、别尔江斯克、叶卡捷琳诺斯拉夫，迫使邓尼金抽调前线精锐回援（`CLM-mawdsley-1987-white-movement-structural-defeat`）。`1920` 年夏马赫诺断然拒绝并处决弗兰格尔派来的求盟使者，于同年 10 月与红军签订《斯塔罗别利斯克政治与军事协定》协同攻克克里米亚击败弗兰格尔；11 月下旬克里米亚战事甫定，红军南方面军司令 **伏龙芝（M. V. Frunze）** 即下令背盟围剿黑军。``
- [ ] **L33**（P0 清除机翻词 `货架外特征`）：
  - 原文：`| EVT-1920-1921-tambov-and-peasant-revolts | parallel-peasant-war | 1920–1921 | 与坦波夫等农民抗征构成农民战争弧，但无政府主义组织形式更具货架外特征 | CLM-hobsbawm-1959-archaic-peasant-rebellion-vs-modern-party |`
  - 改为：`| EVT-1920-1921-tambov-and-peasant-revolts | parallel-peasant-war | 1920–1921 | 与坦波夫等农民抗征构成反战时共产主义农民战争弧，但以无政府共产主义公社与自由苏维埃为独特纲领标志 | CLM-hobsbawm-1959-archaic-peasant-rebellion-vs-modern-party |`
- [ ] **L40**（P0 修正拉丁—西里尔混拼 `taчанka`）：
  - 原文：`采用高度机动的 taчанka 战术与地方苏维埃自治实验。`
  - 改为：`采用高度机动的 тачанка（tachanka，机枪马车）战术与地方自由苏维埃自治实验。`
- [ ] **L55**（P0 明确 1920 下半年系与红军再次结盟共击弗兰格尔）：
  - 原文：`| IV | 1920下 | 弗兰格尔克里米亚政府 | 短暂再次结盟后破裂 |`
  - 改为：`| IV | 1920.10–11 | 弗兰格尔克里米亚白军 | 拒绝弗兰格尔求盟，与红军签订斯塔罗别利斯克协定协同入克里米亚，胜后遭红军背盟突袭 |`
- [ ] **L61–L62**（P1 区分转述与原文直引）：
  - 原文：
    ```markdown
    - **Mawdsley 论邓尼金后方崩溃**（`CLM-mawdsley-1987-white-movement-structural-defeat`）：
      > 马赫诺黑军突破白军后方防线，连克亚速海港口与叶卡捷琳诺斯拉夫，迫使邓尼金抽调精锐（`ch13`, 原书 pp. 213–214）。
    ```
  - 改为：
    ```markdown
    - **Mawdsley 论邓尼金后方崩溃（论断卡提要）**（`CLM-mawdsley-1987-white-movement-structural-defeat`）：1919年10月马赫诺黑军突破白军后方防线，连克亚速海港口别尔江斯克、马里乌波尔与重镇叶卡捷琳诺斯拉夫，迫使邓尼金从莫斯科方向前线抽调精锐回援（`ch13_第二部分_1919_白军之年_part_5.md#L314-L327`，原书 pp. 213–214, 216–217）。
    ```
- [ ] **L67–L68**（P1 修正本地专书目录与文件名）：
  - 原文：
    ```markdown
    - `sources/monographs/mawdsley_1987_civil_war/`（尤其 ch13 南线 1919、ch16–19 1920）
    - `sources/monographs/hobsbawm_1959_primitive_rebels_zh/ch06`, `ch31–32`
    ```
  - 改为：
    ```markdown
    - `sources/monographs/mawdsley_1987_civil_war_zh/`（尤其 `ch09`、`ch13` 1919年南线与 `ch15`–`ch16` 1920年南线；英文版 `sources/monographs/mawdsley_1987_civil_war/`）
    - `sources/monographs/hobsbawm_1959_primitive_rebels_zh/ch06_第二章_绿林好汉.md`、`ch31_六_古赖波勒叶的无政府主义公社.md`、`ch32_七_农民不信任政府.md`
    ```

---

### 4.5 [`cards/policies/POL-april-theses-1917.md`](../cards/policies/POL-april-theses-1917.md)

- [ ] **L11**（P0 修正把十月起义俄历 `1917-10-25` 误填进 `end_ns` 再倒减出假俄历 `1917-10-12 [O.S.]` 的严重历法硬伤）：
  - 原文：`end_ns: "1917-10-25" # 1917-10-12 [O.S.] 十月夺权前作为党内战略总纲逐步落实`
  - 改为：`end_ns: "1917-11-07" # 1917-10-25 [O.S.] 十月起义与苏维埃二大夺权，提纲核心战略目标落地`
- [ ] **L20**（P0 修正第6条“土地社会化”术语错位）：
  - 原文：`并倡议银行国有化、土地社会化与改党名；打破加米涅夫—斯大林有条件支持临时政府路线`
  - 改为：`并倡议没收地主土地实现全部土地国有化、全国银行合并受苏维埃监督与更改党名；打破加米涅夫—斯大林有条件支持临时政府路线`
- [ ] **L45**（P0 修正《真理报》“一周后才拒收全文”失实表述）：
  - 原文：`亲历者记录士兵欲用刺刀对付列宁、加米涅夫耸肩“等着”，《真理报》一周后才拒收全文——强调四月提纲在左翼民主派眼中的突兀与危险。`
  - 改为：`亲历者记录士兵闻言欲用刺刀对付列宁、加米涅夫耸肩称“等着瞧”，《真理报》于4月7日[O.S.]刊出提纲全文后次日即由加米涅夫撰文公开声明编辑部认为列宁的总公式“令人无法接受”——突显四月提纲在左翼民主派与党内温和派眼中的突兀与震动。`
- [ ] **L59**（P1 修正第9条提要“改国际名称”错字）：
  - 原文：`| 9–10 | 改国际名称、建新国际 | 党派 переименование 动议 |`
  - 改为：`| 9–10 | 修改党纲、改党名为共产党、建革命新国际 | 党的重新命名（переименование）与同第二国际决裂动议 |`
- [ ] **L72**（P1 修复 `reading-notes/rabinowitch_1968_prelude/` 断链）：
  - 原文：``- `reading-notes/rabinowitch_1968_prelude/`（基层激进化）``
  - 改为：``- `sources/monographs/rabinowitch_1968_prelude_zh/` 及 `reading-notes/RN-01-rabinowitch-opening.md`（基层激进化）``

---

### 4.6 [`cards/policies/POL-first-five-year-plan.md`](../cards/policies/POL-first-five-year-plan.md)

- [ ] **L10**（P0 修正 `1927-12-15 五大` 截断错字与 `剪刀差危机` 概念混淆）：
  - 原文：`start_ns: "1928-04-01" # 剪刀差危机后计划论证高潮（亦可从1927-12-15 五大授权编制起算）`
  - 改为：`start_ns: "1928-04-01" # 1927–1928粮食收购危机后计划论证高潮（亦可从 1927-12-02 至 12-19 联共〔布〕十五大授权编制起算）`
- [ ] **L26**（P0 拆分四月联席全会与第十六次党代表会议，并将“第五届全俄苏维埃代表大会”修正为“第五次全苏苏维埃代表大会”）：
  - 原文：``- **四月全会与最高方案批准（1929.04–05）**：`1929-04-16` 至 `23` **联共（布）中央委员会暨中央监察委员会联席会议（第十六次代表会议）** 讨论工业速度与农村政策；`1929-05` **第五届全俄苏维埃代表大会** 正式批准 **最高方案** 控制数字，投资与产出指标显著高于原“起点方案”（Davies, Soviet History；`MTG-1929-04-cc-joint-plenum`）。``
  - 改为：``- **四月联席全会、十六次党代表会议与最高方案批准（1929.04–05）**：`1929-04-16` 至 `23` **联共（布）中央委员会与中央监察委员会四月联席全会** 击败布哈林右派（`MTG-1929-04-cc-joint-plenum`），紧接着 `1929-04-23` 至 `29` **联共（布）第十六次代表会议（XVI конференция ВКП(б)）** 与 `1929-05-20` 至 `28` **苏联第五次全国苏维埃代表大会（全苏苏维埃五大）** 正式批准五年计划 **最高方案（оптимальный вариант）**，投资与产出指标显著高于原“起点方案”（`CLM-erlich-1960-stalin-overkill-turn`、`CLM-davies-1980-autumn-1929-great-turn-fabrication`）。``
- [ ] **L33**（P0 修正 `五大授权编制`）：
  - 原文：`| MTG-1927-12-15th-party-congress | mandated | 1927.12 | 五大授权编制并宣示集体化方向 | 会议卡 |`
  - 改为：`| MTG-1927-12-15th-party-congress | mandated | 1927.12 | 联共（布）十五大通过关于编制第一个五年计划的指示并宣示扩大农业集体化方向 | `MTG-1927-12-15th-party-congress` |`
- [ ] **L35**（P0 清除股市俗语 `“骑牛入市”`）：
  - 原文：`| PER-bukharin | defeated-alternative | 1928–1929 | “骑牛入市”均衡增长方案被最高方案排挤 | CLM-erlich-1960-bukharin-balanced-growth, CLM-cohen-1973-bukharin-organizational-defeat |`
  - 改为：`| PER-bukharin | defeated-alternative | 1928–1929 | 主张工农市场结合（смычка）与兼顾消费平衡的渐进工业化方案，被最高方案与非常措施排挤 | CLM-erlich-1960-bukharin-balanced-growth, CLM-cohen-1973-bukharin-organizational-defeat |`
- [ ] **L47**（P1 移除 1923 年剪刀差卡片 `CLM-carr-1954-scissors-crisis-mechanics`，改挂 1929 集体化卡片）：
  - 原文：`- **[档案计量史学 / R. W. Davies, E. H. Carr]** (CLM-davies-1980-autumn-1929-great-turn-fabrication, CLM-carr-davies-1969-grain-price-scissor-1927, CLM-carr-1954-scissors-crisis-mechanics)`
  - 改为：`- **[档案计量史学 / R. W. Davies, E. H. Carr]** (CLM-davies-1980-autumn-1929-great-turn-fabrication, CLM-davies-1980-november-plenum-to-dekulakization, CLM-carr-davies-1969-grain-price-scissor-1927)`
- [ ] **L58**（P0 补齐 4 月 23–29 日第十六次党代表会议）：
  - 原文：`| 1929-04-16—23 | 中央联席会议 | 工业速度与农村路线摊牌 |`
  - 改为：`| 1929-04-16–23 / 04-23–29 | 四月中央联席全会 / 第十六次党代表会议 | 联席全会击败右倾；十六次代表会议正式通过五年计划最高方案 |`
- [ ] **L69**（P1 修正术语 `剪刀差危机` -> `1927–1928年粮食收购危机`）：
  - 原文：`官方粮价周期失误加剧农民售粮犹豫，为一五计划前的剪刀差危机埋伏笔。`
  - 改为：`官方工农价格与比价调控失误加剧农民售粮犹豫，为一五计划前夕的 1927–1928 年粮食收购危机埋下伏笔。`
- [ ] **L72–L73**（P1 修复两处不存在的 `sources/monographs/` 路径断链）：
  - 原文：
    ```markdown
    - `sources/monographs/davies_soviet_history/`（1929 卷）
    - `sources/monographs/carr_bolshevik_rev/`（NEP 末期计划机构）
    ```
  - 改为：
    ```markdown
    - `sources/monographs/davies_industrialisation_en/` 及 `sources/monographs/davies_1980_collective_farm_zh/`（Davies 1980 工业化与集体化卷）
    - `sources/monographs/carr_davies_1969_foundations_v1p1/`（Carr & Davies《计划经济的基础 1926–1929》计划机构与价格政策）
    ```
- [ ] **L79**（P1 修正改历年份笔误 `1929年2月14日` -> `1918年2月14日`）：
  - 原文：`1929年2月14日后苏俄官方仅用公历，无需再附俄历。`
  - 改为：`1918年2月14日后苏俄/苏联官方仅用公历，无需再附俄历。`
