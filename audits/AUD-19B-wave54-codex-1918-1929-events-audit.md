# AUD-19B｜Wave 54 Codex 1918–1929 年核心事件卡跨家族对抗审计（Batch E2，6 张）

- **审计任务**：`W61-G2` / `AUD-19B`（Cross-Family Adversarial Audit：OpenAI `gpt-6.1-sol` Wave 54 `W54-C2` 升格定稿 → Google Gemini 对抗审计）
- **审计日期**：2026-11-19
- **审计性质**：**纯只读审计**；本文件为唯一允许写入/修改的文件，未改动任何 `cards/`、`claims/`、`debates/`、`sources/`、`graph/` 或 `config/` 文件
- **写盘进度**：**阶段二完结（全 6 张机械检查 + 逐行馆藏原书/一手文献对抗审计 + `E2-01`..`E2-17` 精确修复矩阵 + 闭卷 SHA-256 复核）**
- **发现总计**：**17 项**（**P0: 1** ｜ **P1: 9** ｜ **P2: 7**）

---

## 0. 基线哈希与机械合规核查（全 6 张）

### 0.1 审计前 SHA-256 基线记录

| 序号 | 卡片路径 | 开审前 SHA-256 |
| :---: | :--- | :--- |
| 01 | `cards/events/EVT-1918-1920-russian-civil-war.md` | `6d7fecf1277fc1c2781ee5925dee89812257a4ea180e2ad5a4ef1df94f02a7a1` |
| 02 | `cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md` | `8e7176ddbf7cb753cb17c2b794e0734257d895acad2475229ea410ec21b2bbd4` |
| 03 | `cards/events/EVT-1921-kronstadt.md` | `111402b2915e60db3d926255712ff411b83b035d23d012dcf20ffe18da33c3aa` |
| 04 | `cards/events/EVT-1923-scissors-crisis.md` | `edc6d979a8f88f8980ac5c678bdd45fc889c2f4dbdac4515c06a010ed475bfb6` |
| 05 | `cards/events/EVT-1928-grain-procurement-crisis.md` | `7f8c493e88932ce3cbda7175e8f597803c5dbbca13dd8b7a02fd0c8900b486c5` |
| 06 | `cards/events/EVT-1929-great-turn-and-dekulakization-launch.md` | `6e3cb59e6fbfb3490bfa96037e41729c65184bfb22b118f07151817a9817df35` |

### 0.2 机械与结构合规总表（全 6 张）

| 序号 | 卡片 | YAML 必填字段 | `coverage_status` | `[T1]` 去空白字数（≤150） | `2.2` 边表严格 5 列 | 站内相对链接与反引号 ID 实存 | 外部 HTTP 链接 |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 01 | `EVT-1918-1920-russian-civil-war.md` | ✅ | `multi-perspective` ✅ | 117 ✅ | 12/12 行 ✅ | 8/8 链接、18/18 ID ✅ | 0 ✅ |
| 02 | `EVT-1920-1921-tambov-and-peasant-revolts.md` | ✅ | `multi-perspective` ✅ | 116 ✅ | 9/9 行 ✅ | 12/12 链接、16/16 ID ✅ | 0 ✅ |
| 03 | `EVT-1921-kronstadt.md` | ✅ | `multi-perspective` ✅ | 113 ✅ | 9/9 行 ✅ | 12/12 链接、17/17 ID ✅ | 0 ✅ |
| 04 | `EVT-1923-scissors-crisis.md` | ✅ | `multi-perspective` ✅ | 115 ✅ | 9/9 行 ✅ | 14/14 链接、16/16 ID ✅ | 0 ✅ |
| 05 | `EVT-1928-grain-procurement-crisis.md` | ✅ | `multi-perspective` ✅ | 118 ✅ | 12/12 行 ✅ | 19/19 链接、26/26 ID ✅ | 0 ✅ |
| 06 | `EVT-1929-great-turn-and-dekulakization-launch.md` | ✅ | `multi-perspective` ✅ | 115 ✅ | 12/12 行 ✅ | 22/22 链接、25/25 ID ✅ | 0 ✅ |

---

## 01｜[`EVT-1918-1920-russian-civil-war.md`](../cards/events/EVT-1918-1920-russian-civil-war.md)

**总判**：历法处理严谨（1918年2月后战事统一公历，仅对白军旧历文书补列俄/公历对照）、兵力累计与存量分账清晰、Mozokhin 统计限定与 DuGarm/Raleigh 署名拆分准确；存在 **1 项 P1（`CLM-mawdsley-1987-sovdepia-demographic-industrial-base` 跨卡挂错引文）** 与 **2 项 P2（1918–1919 关键军事节点日期压缩、`DEB-1918-war-communism` 反向关联不对称）**。无 P0。

### 1.1 正向核实（对照本地馆藏无误）
- `[T1]`（L20）：117 字（≤150），准确定位红白主战场、边疆民族国家竞争与克里米亚撤离非全战线终点。
- 建军与兵力口径（L26、L72–75）：`1918-05-29` 转向义务兵役、`>4.8万` 累计前沙俄军官 vs `1918` 年底 `22,000` 在役、`1919-06` 150 万在册／35.6 万一线、`60万` 库存／`46万` 年产量，均与 `DATA-05` 及 `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` 一致。
- 1919–1920 历法与战役异文（L30、L32）：邓尼金《莫斯科训令》`1919-07-03 [N.S.] / 06-20 [O.S.]`（`+13` 天）、奥廖尔失守 `10-13`（Kakurin）vs `10-14`（Mawdsley）均属公历异文、`10-20` 收复奥廖尔、`10-24` 收复沃罗涅日；弗兰格尔 `1920-04-04 [N.S.] / 03-22 [O.S.]` 接掌、`05-25 [O.S.] / 06-07 [N.S.]` 土地令（`+13` 天）、`11-14—16` 约 14.6 万官兵与难民撤离，与 `PER-denikin`、`PER-wrangel`、`timeline/L3_daily/1919-10_civil_war_southern_and_petrograd_climax.md` 完全相符。
- 红色恐怖口径与地方史校勘（L36、L61–62）：`1918-09-05` 红色恐怖法令、Mozokhin `1918年34省6,300人` / `1919年前7个月35省2,089人`（`DATA-06 §A.1`）、指出 `CLM-smith-scott-2011-psr-third-force-collapse` 实为 Radkey 1963 而不冒称直读 Smith 2011、明确 DuGarm 坦波夫章与 Raleigh 萨拉托夫章不混署，均属高质量核查。

### 1.2 审计发现
- **`E2-01` [P1]｜L59 错将 Mawdsley 2008 年序言关于“农民政治无力”的论点挂给 `CLM-mawdsley-1987-sovdepia-demographic-industrial-base`**
  - **卡片原文（L59）**：“其2008年序又明确，‘农民政治上的无力’不是没有农民起义，内部战争也不能无证据地取代红白主战场为首要军事解释（`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`；RN-W6）。”
  - **馆藏实证核查**：逐行核查 `historiography/claims/CLM-mawdsley-1987-sovdepia-demographic-industrial-base.md`（L1–56），该卡**完全只讨论**苏维埃约 30 省／6,000 万人口腹地、帝国军工库存与铁路及旧军官数量，**没有任何一行**提及“2008 年序”或“农民政治上的无力”。该论述实际位于：
    - `sources/monographs/mawdsley_1987_civil_war/ch02_preface_to_the_2008_edition.md` L99–119（pp. 10–11，*"political impotence of the peasantry"*）；
    - `historiography/claims/CLM-mawdsley-1987-civil-war-militarized-regime.md` L28（明确列明 2008 版序“农民政治上的无力”）；
    - `reading-notes/mawdsley_carr/RN-W6-civil-war-heartland-and-1923-scissors.md` L34–38。
  - **修复方向**：L59 的“2008年序”句须拆出并挂接 `CLM-mawdsley-1987-civil-war-militarized-regime` 与 `RN-W6`，而腹地人口军工前句保留 `CLM-mawdsley-1987-sovdepia-demographic-industrial-base`。

- **`E2-02` [P2]｜L26、L30 对 1918–1919 关键军事节点日期过度模糊/压缩**
  - **卡片原文**：L26 写“与1918年春夏捷克斯洛伐克军团冲突”、“9月成立共和国革命军事委员会”；L30 写“高尔察克春攻在4—6月遭红军东线反击”。
  - **馆藏实证核查**：
    - 捷克军团起义在馆藏 `sources/monographs/mawdsley_1987_civil_war/ch12_8_siberia_the_directory_and_kolchak.md` L34 明确记为 **`1918年5月下旬`**（*"uprising of the Czechoslovak Corps at the end of May 1918"*）；
    - 共和国革命军事委员会（RVSR）成立于 **`1918年9月2日`**（`INS-rkka-red-army-and-rvr.md` L25、`PER-trotsky.md` L26）；
    - 高尔察克春攻于 **`1919年3月初`** 发动并推进至4月中旬，红军东线南集群自 **`1919年4月28日`** 反击至 **`6月9日`** 收复乌法（`PER-kolchak.md` L27）。现写“春攻在4—6月遭红军东线反击”容易把进攻起讫与反攻起讫混同为“4—6月”。

- **`E2-03` [P2]｜`related_debates` 与 `DEB-1918-war-communism-ideology-or-emergency` 反向关联不对称（跨卡联动备注）**
  - **事实**：本卡 L15 挂接 `DEB-1918-war-communism-ideology-or-emergency`，但 `debates/DEB-1918-war-communism-ideology-or-emergency.md` L6 `core_cards` 仅列 `EVT-1921-kronstadt`（未列 `EVT-1918-1920-russian-civil-war` 与 `EVT-1920-1921-tambov-and-peasant-revolts`）。因本次审计严禁修改 `debates/` 文件，此项列为跨文件图谱同步建议，不在本卡内破坏既有关联。

---

## 02｜[`EVT-1920-1921-tambov-and-peasant-revolts.md`](../cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md)

**总判**：对 DuGarm 中文译稿页码与作者归属校勘精准（`pp.103–138`、`127–130`、`131–138`），Carr `2月8日 / 2月24日` 时序与 `DATA-04` 十大票型边界严密，未误用站外未入藏的 `1921-06-12` 日期；但存在 **2 项 P1（漏用馆藏已有的坦波夫爆发精确日期 `1920-08-19` 与卡缅卡村起点、将馆藏已有的 `PER-tukhachevsky` / `0116号命令` / `Leggett (1981)` 兵力俘虏数笼统写进“待核/研究”）** 与 **1 项 P2（§3.2 来源表漏列已入库的 Leggett 与 `PER-antonov`、辩论卡反向不对称）**。无 P0。

### 2.1 正向核实（对照本地馆藏无误）
- `[T1]`（L20）：116 字（≤150），准确区分粮食税让步与夏季镇压、零星延续与“立即和解”的误读。
- DuGarm 与 Raleigh 分工（L26、L63、L71–75）：对照 `RN-W32` 与 `sources/primary/raleigh_2001_provincial_landscapes_zh/ch05_第3章_坦波夫的地方政治与粮食斗争.md`（L750–929），PDF 页码 `pp.103–138`、戈尔丁—马尔戈林案 `pp.127–130`、1920年8月以后 `pp.131–138` 全部准确。
- Carr 与十大口径（L30、L65、L67）：`1921-02-08` 与 `1921-02-24` 早于 `02-28` 喀琅施塔得舰上决议（`RN-W23`、`carr_bolshevik_rev_v2_zh/ch18` PDF pp.119, 123）；`DATA-04` `694` 名表决代表与工会案 `336:50:18`（2 弃权）口径准确。
- 毒气命令日期防幻觉审查：经检索全库，**`1921-06-12` 日期在本地馆藏中并不存在**，卡片不在正文中擅自填入站外日期符合防伪引要求。

### 2.2 审计发现
- **`E2-04` [P1]｜遗漏馆藏已明载的爆发日 `1920-08-19` 与卡缅卡村起点，且模糊了起义早期非安东诺夫单人主导的领导演变**
  - **卡片原文**：YAML L10 为 `start_ns: "1920-08-01"`；L26 写“1920年夏坦波夫抗征粮冲突扩展为安东诺夫武装主导的起义”；L28 只写“（1920年8月—1921年初）”。
  - **馆藏实证核查**：
    - 爆发精确日期 `1920-08-19` 在站内明确有据：`sources/monographs/leggett_1981_cheka/ch12_pages_361-390.md` L338（*"began on 19 August 1920, when starving peasants of Kirsanov District rebelled"*）及 `ch15` L1784；
    - 起点地点与初始领导在 `sources/monographs/figes_1996_peoples_tragedy/ch22_...`（L18–25）与 `cards/people/PER-antonov.md`（L20、L26）中明确记为：**基尔萨诺夫县卡缅卡村（Kamenka）** 于 8 月农民击毙征粮队引发起义，最初由地方农民兼社革党人 **Grigorii Plezhnikov**（格里戈里·普列日尼科夫）领头，直至 **1920 年 11 月**安东诺夫才受邀出任统一军事总指挥部首领。
  - **影响**：卡内直接将 8 月起点概括为“安东诺夫武装主导的起义”，且在 `start_ns` 与 T3 未交代 `1920-08-19`（Leggett）与 8 月月窗的区别。

- **`E2-05` [P1]｜L32、L86 绕过站内已有的 `PER-tukhachevsky`（0116 号命令、`1921-04-27` 任命）与 `Leggett (1981)` 具体镇压统计**
  - **卡片原文**：L32 仅笼统称“馆藏研究记述了毒气清剿命令……”；L86 把“第130号与第171号命令须分别核准编号、日期和对象；毒气命令……”一并置于外部缺口，只挂 `Figes` 而不挂站内其他已核节点。
  - **馆藏实证核查**：
    - `cards/people/PER-tukhachevsky.md` L27、L58、L76 已在站内明确识别化学武器命令编号为 **第 0116 号命令**，并明确界定**第 130 号与第 171 号命令**为连坐扣押人质与集中营机制（同时诚实标明第 0116 号命令的具体签发日—即外部通行 `1921-06-12`—及第 130/171 号命令原文未入藏，属于 S 级原件缺口）；
    - `PER-antonov.md` L27 与 `leggett_1981_cheka/ch12_pages_361-390.md` L432–444, L493 在站内提供了一系列高价值具体数字：`1921-03-01` 政府军已投入 `32,500` 步兵与 `8,000` 骑兵；`1921-04-27` 图哈切夫斯基受命全权统帅、`05-06` 抵达前线；Leggett 称游击队由 5 月约 `21,000` 人（与 Figes 一致）降至 7 月中旬约 `1,200` 人，截至 `1921-07-20` 已扣押约 `5,000` 名人质待流放；`PER-antonov.md` L27 另汇 Figes 6 月底约 `50,000` 农民入营及总体约 `10万` 被关押／流放、`1.5万` 被枪决的估计。
  - **影响**：卡片既未在正文中写出 `1921-04-27` 任命、`0116 号` 命令号及 Leggett 兵力时间锚，也未在 3.3 说明站内人物卡已区分 `0116` 与 `130/171` 编号。

- **`E2-06` [P2]｜§3.2 来源表漏列已入库的 `Leggett (1981)` 与 `PER-antonov.md`，且与 `DEB-1918-war-communism` 反向不对称**
  - `sources/monographs/leggett_1981_cheka/ch12_pages_361-390.md`（pp.330–334）在站内专门论述坦波夫爆发日、红军兵力变化、图哈切夫斯基上任与契卡人质数，`PER-antonov.md` 已在 2.2 引用（L40），两者均未列入 §3.2 锚点清单。另 `DEB-1918-war-communism-ideology-or-emergency.md` L6 `core_cards` 未双向收录本卡（跨卡同步备注）。

---

## 03｜[`EVT-1921-kronstadt.md`](../cards/events/EVT-1921-kronstadt.md)

**总判**：对《十五条决议》三阶段文本（`02-28` 舰上、`03-01` 支队/广场、`03-02` 临革委）、两次表决分开、十大开幕与第一次强攻同日（`03-08`）并置、粮食税酝酿（`02-08/24`）与落实（`03-15/21`）处理扎实；但存在 **1 项直接史实错误（P0：L32 强行禁止把图哈切夫斯基列为 3 月 5 日最后通牒联署人，与馆藏 Avrich 原文及 L3 微距卷正面冲突）**、**1 项 P1（L71 对 Avrich 论断卡页码的指责以偏概全，L54 否定馆藏中实存的 `94% 老兵` 统计出处）** 与 **1 项 P2（缺列馆藏已有的红军／起义者分层伤亡量化锚点）**。

### 3.1 正向核实（对照本地馆藏无误）
- `[T1]`（L20）：113 字（≤150），准确定位政治诉求、跨冰夺岛及“经济退却 ≠ 政治开放”。
- 十五条决议与表决分层（L28–30、L66、L75）：对照 `sources/web-archive/E02_E07_foundational_docs/1921-03-01_petropavlovsk-resolution.md`，正确指出库内 S 级原典为 `03-01` 文本、`02-28` 另有政府通报旁证、支队“全票、2 弃权”与卫戍“压倒多数、Vasiliev 与 Kalinin 反对”不混并。
- 十大与军事并行时序（L34、L67–68）：`03-07` 炮击、`03-08` 一攻失利兼十大开幕、`03-15` 实物税、`03-16` 炮火准备兼《关于党的统一》、“约 300 名十大代表赴前线”与 `694` 名表决代表区分、`03-17` 总攻、`03-18` 攻陷、`03-21` 实物税法令，全部准确。

### 3.2 审计发现
- **`E2-07` [P0]｜L32 对 3 月 5 日最后通牒联署人的史实错误（错误“纠正”并禁止实存的图哈切夫斯基联署）**
  - **卡片原文（L32）**：“3月5日最后通牒由托洛茨基与红军总司令谢尔盖·加米涅夫签发；图哈切夫斯基受命指挥第七集团军，不能把他加写为该通牒的第三位联署者。”
  - **馆藏实证核查**：两份核心本地馆藏直接证伪该句“禁止加写图哈切夫斯基”的断言：
    1. `sources/monographs/avrich_1970_kronstadt/ch06_pages_151-175.md` L432–435（原书 p.161 及脚注 25，引 *Trotskii, Kak vooruzhalas' revoliutsiia, III, part 1, 202*）：
       > *"The co-signers of the ultimatum were **S. S. Kamenev**, commander in chief of the Red Army, and **M. N. Tukhachevsky**, commander of the Seventh Army in Petrograd."*（另有 `ch06` L423–430 明述最后通牒“was issued over Trotsky's signature”并在次段补全此二位联署人）。
    2. `timeline/L3_daily/1921-03_kronstadt_and_10th_congress.md` L86：
       > “托洛茨基与红军总司令谢·谢·卡梅涅夫、第 7 集团军司令图哈切夫斯基联合发表公报与最后通牒。”
  - **次级译名瑕疵（同句）**：L32 将红军总司令 `S. S. Kamenev` 译为“谢尔盖·加米涅夫”，易与政治局委员 `L. B. Kamenev`（加米涅夫）混淆；L3 微距卷统一使用区分译法“**谢·谢·卡梅涅夫**”。
  - **危害判定**：P0 级（把正确史实明确写为“不能把他加写为该通牒的第三位联署者”，属于主动输出反向史实错误）。

- **`E2-08` [P1]｜L71 对 Avrich 论断卡页码的指责以偏概全，且 L54 忽略站内 Figes 转引的 Getzler `94%` 老兵数据**
  - **卡片原文**：
    - L71：“Avrich本库按PDF分块，三张论断卡的历史页码字段与分块名并非处处对应，特别是白卫阴谋卡混入异常高页码；本卡优先用其明确的论证段与RN-W3定位，不沿用那些异常数字。”
    - L54：“现有论断也未给出足以代表全要塞的‘94%老兵’统计（`CLM-avrich-1970-sailor-social-composition`）。”
  - **馆藏实证核查**：
    1. **页码核查**：逐一检视 3 张 Avrich 论断卡：
       - `CLM-avrich-1970-sailor-social-composition.md` L9：`original_pages: "pp. 101-105"`，精准对应 `ch04_pages_101-125.md`，正文未混入 Markdown 行号；
       - `CLM-avrich-1970-soviets-without-bolsheviks.md` L9：`original_pages: "pp. 198-201, 179-180"`（`ch08` 与 `ch07`），仅正文括号出现 2 处从 `RN-W3` 抄来的 Markdown 行号（`pp.914-937`、`pp.939-949`）；
       - `CLM-avrich-1970-white-plot-refutation.md` L9：`original_pages: "pp. 143-147, 816-818"`（且正文括号有 `pp.561-575`），这是唯一在 YAML `original_pages` 中混入 `RN-W3` 行号 `816-818` 的卡片。L71 泛称“三张论断卡的历史页码字段与分块名并非处处对应”不准确——分块名 `chNN_pages_XXX-YYY.md` 与 `original_pages` 在前两张卡均一一对应。
    2. **`94% 老兵` 核查**：该数字虽不在 Avrich 3 张论断卡内，却**明确实存于本库** `sources/monographs/figes_1996_peoples_tragedy/ch22_...`（L81）：*"On the two major ships involved in the mutiny, the Petropavlovsk and the Sevastopol, **94 per cent** of the crew had been recruited before 1918"*（引 Israel Getzler 1983），并已收入 `timeline/L3_daily/1921-03_kronstadt_and_10th_congress.md` L52、L199。L54 的关键边界应精准表述为：“`94%` 源自站内 Figes 转引的 Getzler 研究，且口径仅为两艘主力舰（《彼得罗巴甫洛夫斯克》与《塞瓦斯托波尔》号）1918 年前入伍水兵，不能外推代表全要塞驻军，且 Getzler（1983）原书未独立入藏。”

- **`E2-09` [P2]｜L32、L69 只提示“分统计管道”，却未给出站内已有的 Avrich / Figes 具体伤亡与处决区间**
  - **事实**：`sources/monographs/avrich_1970_kronstadt/ch09_pages_226-245.md`（pp.227–228）与 `timeline/L3_daily/1921-03_kronstadt_and_10th_congress.md` L162–166 已提供清晰分层数字：
    - 红军官方数字约 `700` 阵亡、`2,500` 伤（Avrich p.227；`L3` 记苏方后补“死伤约 1,900”，另彼得格勒医院 `03-03—21` 收治伤员与冻伤休克 `>4,000` 人、院内死亡 `527` 人）；美国驻维堡领事 Quarton 估苏方总死伤约 `10,000`（含约 `15` 名十大代表）；
    - 起义者据 Avrich p.228 约 `600` 阵亡、`>1,000` 伤、约 `2,500`（或逾 `2,000`）被俘，`03-20` 夜间首审处决 `13` 人，随后数周先枪决数百名（“several hundred”）、此后数月另处决及流放劳改营数百至两千余人；
    - 另 Figes `ch22` 记红军阵亡逾 `10,000`（系将 Quarton 的总死伤口径转写为阵亡）与 `500` 即刻处决 + 逾 `2,000` 随后处决。本卡仅写“约 8,000 人撤入芬兰”，略去了最核心的红军／起义者伤亡对比区间及 Avrich 与 Figes 对 Quarton `10,000` 口径的史料分歧。

---

## 04｜[`EVT-1923-scissors-crisis.md`](../cards/events/EVT-1923-scissors-crisis.md)

**总判**：纯公历（`N.S.`）标注、`1913=100` 指数口径纪律（严守 Carr `187/171`、`58/49`、`141/134`、`77/68` 与斯特鲁米林 `323%` 边界、禁止零售/批发跨行相除）、1923 年式苏维埃卢布与切尔文量纲区分，以及《新方针》公开信“署日 `12-08` vs 见报 `12-11` vs `1924` 小册子”分期均处理出色；但存在 **1 项 P1（L32 错述《四十六人声明》“两份名单共 47 人次签名”的物理打字稿结构）** 与 **1 项 P2（L30 未点明 `276/89` 实指国家计委 Gosplan 批发物价指数，兼及 L86/L15 跨卡分级与反向链接边界）**。无 P0。

### 4.1 正向核实（对照本地馆藏无误）
- `[T1]`（L20）：115 字（≤150），准确把握经济失衡（滞销/欠薪/价格剪刀）与党内民主争论在列宁缺席下的交汇。
- 价格指数与货币口径（L26、L30、L36、L68–74）：对照 `sources/monographs/carr_1954_interregnum/ch95_image096.md`、`ch96_image097.md`（原书 pp. 95–96, 127）及 `DATA-02-1922-1924-scissors-crisis-and-chervonets.md`，`1922-09` 十二大插图交点、`1923-10-01` 工业零售 `187`/批发 `171`、农业零售 `58`/批发 `49`、零售比约 `3.22` 倍、斯特鲁米林 `323%`、`1924-01-01` `141/134` 与 `77/68`，以及苏维埃纸币月发行 `1923-09` `60亿` 跃升至 `1923-12` `1100亿`（1923 年式卢布）与 `0.35 / 7.0` 百万切尔文流通额全部精准且严格分列。
- 1923 年 10–12 月政治时序（L32、L34）：托洛茨基 `10-08` 致中央及中监委信、`10-15`《四十六人声明》（俄文刊本据 `10-18` 政治局记录重建，阿·别洛博罗多夫、弗·马克西莫夫斯基、安·布勃诺夫旁题 `11/Х.23`，阿·戈尔茨曼另纸题 `12/Х-23`）、`10-25—27` 联席全会、`12-05` 妥协决议、`12-08` 署日公开信、`12-11` 见报《真理报》、《苏共中央通报》中保留“省代表会议及党代表大会选举”中间链而英/中译本删落（`1923-10-15_declaration-of-the-forty-six.md` L93），以及避开 `RN-W6` L172 将 `П. К. Коганович` 误作拉扎尔·卡冈诺维奇的陷阱，均经直接核实无误。

### 4.2 审计发现
- **`E2-10` [P1]｜L32 错述《四十六人声明》的打字稿物理构成（误称“两份名单共47人次签名”）**
  - **卡片原文（L32）**：“两份名单共47人次签名、阿·戈尔茨曼重复，实为46位独立签名者；托洛茨基未联署，部分签名者附保留意见。”
  - **馆藏实证核查**：逐行核查 `sources/web-archive/E01_E10_supplements/1923-10-15_declaration-of-the-forty-six.md` L38、L55、L89、L170–174、L204–206 及《苏共中央通报》1990 年第 6 期原编者注 L268：
    > *"Подлинник документа представлен двумя оригинальными машинописными текстами... Первый текст содержит **34** подписи, второй— **12**."*（两份原始打字稿分别包含 **34 个** 与 **12 个** 签名，`34 + 12 = 46` 个正文签名，而非 47 个。）
    而产生“第 47 次出现”的原因是 `А. Гольцман`（#14）在第一份打字稿签名后，又另附了一张 **`12/Х-23` 另纸说明（отдельный лист）** 并再次落款（L89：“签了《四十六人声明》的 А. Гольцман 还附了一张单独的条子。这张条子不是第 47 人”）。将“两份打字稿共 46 处正文签名 + 戈尔茨曼另纸附签 1 次（总计 47 人次落款）”误缩成“两份名单共 47 人次签名”，歪曲了一级文献的物理文本结构。

- **`E2-11` [P2]｜L30 未点明“另套276／89等数字”为国家计委（Gosplan）批发物价指数口径，兼及 L86/L15 跨卡分级与反向关联边界**
  - **卡片原文（L30）**：“这些是特定系列与观察日；不能与另套276／89等数字混接，也不能把工业零售187除以农业批发49后仍称‘零售比’。”
  - **馆藏实证核查**：
    1. L30 引“276／89”源自 `timeline/L3_daily/1923-10_scissors_and_new_course_crisis.md` L43（“不要拿另套批发指数276与89来拼接”），但未点明该组数字属 **国家计委（Gosplan）批发物价指数** 系列（区别于 Carr 采用《经济生活报》1913=100 之 TsSU 零售/批发序列），且“276／89”并无本站已入藏的一级原始月表支撑，正文中宜明示“（见于 L3 对另一套国家计委批发指数的口径警示，非同序列拼接对象）”。
    2. L86 依据 `CLM-deutscher-1959-disarmed-prophet-paradox.md` L7 标作 `A 级`，但该论断卡本身将 1923 年争论错误挂接至 `debate: DEB-1903-bolshevik-menshevik-split`（L11），且 `L3 1923-10` L215 将 Deutscher 三部曲中译本定为 `B 级`（宜在本卡 L86 注明“站内按 A 级编目、中译本无原书纸页”，避免口径混淆）；另 L15 所挂接的 `DEB-1922-lenin-testament-and-stalin-rise`（L6）与 `DEB-1928-bukharin-alternative`（L9）均未在 `core_cards` 中反向收录 `EVT-1923-scissors-crisis`（跨卡同步备注）。

---

## 05｜[`EVT-1928-grain-procurement-crisis.md`](../cards/events/EVT-1928-grain-procurement-crisis.md)

**总判**：定量边界严密（`DATA-03` 1927.10–12 月度 `104 / 64.5 / 59.9` vs `152 / 157 / 146` 万吨、涅姆奇诺夫表 `26%→13.3%` 及 `466.2/4052=11.51% vs 11.2%` 原表算术差、拒绝融合 Lewin `75%–80%` 与涅表 `74%`、4 月 1 日 `596/576` 百万普特窗口隔离、`DATA-06` `13,616,151` vs `6,345,277` 吨及 `49,068` 征粮逮捕 vs `95,208` 破案数、Arapovich `28.8%/6.8%/20%`、Zemskov 两套版本定级分列均精准）；但存在 **2 项 P1（彻底遗漏与 1928 年粮食危机同步交织的沙赫特事件及 `DEB-1928-shakhty`；L30 无保留沿袭 Cohen“1月赴乌拉尔和西伯利亚”误述而违背站内 L3/Kotkin/Khlevniuk 考证并漏列 `1928-01-06` 密令与 `1.28亿普特` 年底缺口）** 与 **1 项 P2（§2.2 漏列正文所叙 `PER-tomsky`、`MTG-1929-04-cc-joint-plenum` 与 `MTG-1929-11-cc-plenum`，且 L38 未切分 11-17 逐出与 11-25/26 检讨）**。无 P0。

### 5.1 正向核实（对照本地馆藏无误）
- `[T1]`（L20）：118 字（≤150），精准区分总产、商品粮与国家采购分母。
- 数据与分期纪律（L26、L32、L36、L38、L77–86）：对照 `DATA-03`、`DATA-06`、`CLM-lewin-peasants-1968-ural-siberian-method`、`CLM-arapovich-1929-skills-quotas-and-heavy-industry-mobilization`，严格将 `1928-01` 第 107 条与 `1928–1929` 冬春成型、1929 年 4 月五倍罚金与 6 月刑法 61(3) 分期，且拒绝将“1928—1930-03 撤换 82% 村苏维埃主席”压缩进 1929 单年。
- 莫斯科与右翼败局时序（L34）：`07-04—12` 七月全会、`07-09` 贡赋演说、`07-11` 布—加密会、`09-30`《札记》、乌格拉诺夫 10 月地方清洗与莫洛托夫 11 月接掌莫斯科市委不合日，与 `RN-W6`、`L3 1928-1929` 完全一致。

### 5.2 审计发现
- **`E2-12` [P1]｜L15、§2.1 与 §2.2 彻底遗漏同期并行的 1928 年沙赫特事件（`EVT-1928-shakhty-affair-show-trial`）与 `DEB-1928-shakhty-specialist-baiting-and-cultural-revolution`**
  - **馆藏实证核查**：
    1. `historiography/debates/DEB-1928-shakhty-specialist-baiting-and-cultural-revolution.md` L6 `core_cards` 已明确将 `EVT-1928-grain-procurement-crisis` 列为核心关联卡；
    2. `cards/events/EVT-1928-shakhty-affair-show-trial.md` L39 在边表中双向挂接 `EVT-1928-grain-procurement-crisis`（`parallel_political_track`，1928 年春）；
    3. `timeline/L3_daily/1928-01_siberian_grain_expedition_and_shakhty_affair.md` L84–98 与 `Kotkin RN-W1C` 实证显示两条危机轨道从 1928 年 3 月至 7 月严密同步：四月联席全会（`04-06—11`）并行处理粮食报告与沙赫特案；**1928 年 7 月 9 日**沙赫特案 5 名工程师被枪决，与斯大林在七月全会发表粮食“贡赋”与“阶级斗争尖锐化”演说同日；而布哈林、托姆斯基三月附和沙赫特破坏阴谋论，直接拆散了原本可能联手古比雪夫、奥尔忠尼启则制约斯大林的高层防线。Card 05 从 YAML 到 T2/T3 通篇只字不提沙赫特案，属于显著的并行脉络遗漏与图谱单向断链。

- **`E2-13` [P1]｜L30 无保留采纳 Cohen“1月赴乌拉尔和西伯利亚”写法，违背站内档案考证（斯大林本人仅赴西伯利亚），且漏列 `1928-01-06` 绝密指令与 `1.28 亿普特` 年底累计缺口锚点**
  - **卡片原文（L30）**：“斯大林1月赴乌拉尔和西伯利亚，1月20日新西伯利亚讲话把问题归为‘富农’操纵并要求动用反投机刑法第107条。”
  - **馆藏实证核查**：
    1. `Cohen ch11` p.278 确有 *"through Siberia and the Urals"* 之概括表述，但站内多部直接依据档案的一级/A 级考证——`timeline/L3_daily/1928-01_siberian_grain_expedition_and_shakhty_affair.md` L46, L50–74（据 `Carr–Davies p.50`）、`CLM-khlevniuk-2015-defeat-of-right-opposition.md` L24、`RN-W1C-1928-siberian-turn-and-bukharin.md`——均已证明：1928 年 1 月 12 日政治局分兵中，**乌拉尔由什维尔尼克（Shvernik）前往**（莫洛托夫赴乌克兰，米高扬与安德烈耶夫赴北高加索），斯大林因奥尔忠尼启则告病顶替，**1928-01-15 至 02-06 仅亲自巡视西伯利亚**（新西伯利亚 `01-18—20`、巴尔瑙尔 `01-21—22`、鲁布佐夫斯克 `01-23`、鄂木斯克 `1月下旬`、泰加站 `01-30` 密电、克拉斯诺亚尔斯克 `01-31—02-02`，`02-06` 返京）。Card 05 直接照搬 Cohen 早期概括写“斯大林1月赴乌拉尔和西伯利亚”，未按 L3 分站考证予以订正；
    2. 此外，L26–30 遗漏了站内反复作为危机转折基准的两个核心事实锚点：一是 **1927 年底国家谷物收购较上年累计短缺约 `1.28 亿普特`（约合 `209–210 万吨`）**（`L3 1928-01` L34, L44，`Velikanova ch06`）；二是 **`1928-01-06`** 斯大林亲笔起草、以撤职处分相威胁的绝密督粮指令（`L3 1928-01` L45），此为第 107 条全面激活前夜的直接政策触发点。

- **`E2-14` [P2]｜L34/L38 所叙 `PER-tomsky` 与两次全会 `MTG-1929-04-cc-joint-plenum`、`MTG-1929-11-cc-plenum` 缺席 §2.2 边表，且 L38 未切分“11-17 逐出”与“11-25/26 检讨”**
  - **卡片原文**：L34 明载“同李可夫、托姆斯基反对强制”，L38 仅写“1929年4月联席全会、随后计划批准与秋季指标跃升压缩了温和路线。十一月全会将布哈林逐出政治局”。
  - **馆藏实证核查**：§2.2 边表已收录 `PER-bukharin`、`PER-rykov`、`PER-sokolnikov`、`PER-uglanov`、`PER-molotov`，唯独漏列 **`PER-tomsky`** 与 **`MTG-1929-04-cc-joint-plenum`**、**`MTG-1929-11-cc-plenum`**；且 L38 未明确 `1929-11-10—17` 全会区间（`11-17` 仅逐出布哈林、警告李可夫与托姆斯基并保留二人政治局席位）及会后 **`11-25` 三人签署、`11-26` 见报《真理报》** 的公开检讨声明（`MTG-1929-11` L26、`L3 1928-1929` L247–256）。

---

## 06｜[`EVT-1929-great-turn-and-dekulakization-launch.md`](../cards/events/EVT-1929-great-turn-and-dekulakization-launch.md)

**总判**：1929 年 11–12 月《苏联农村的悲剧》第 2 卷档案链条极为精密（`12-05` 设 18 人委员会、`12-07` 设全苏农业人民委员部、`12-08` 鲍曼小组三分类、`12-18` 一致草案保留奶牛/小畜/退股条款、`12-22` 呈报、`12-25` 斯大林否决信、`12-27` 阶级消灭公开宣告、1930.01.05/30 分期界限，`26,380` vs `27,519` 二万五千人、`13,616,151` vs `6,345,277` 吨、`49,068` 征粮逮捕与 Zemskov/Arapovich 统计纠偏均高度可靠）；但存在 **2 项 P1（L30 将 Doc 9“截至 1929 年 12 月 15 日”统计截点错缩成“12月15日以后汇总”；L26 跳过 1929 年 4 月 16–23 日联席全会与 4 月 23–29 日十六次党代表会议 `17.5%` 播种比例基准，且 L28 遗漏 `11-25/26` 右翼公开检讨）** 与 **1 项 P2（L88 Doc 15 漏注 `PDF p.90`，§2.2 漏列 `PER-rykov`、`PER-tomsky`、`MTG-1929-04-cc-joint-plenum` 及 `DEB-1928-bukharin-alternative` 反向关联）**。无 P0。

### 6.1 正向核实（对照本地馆藏无误）
- `[T1]`（L20）：115 字（≤150），严格区分政治发动、名义入庄、真实生产改组与次年驱逐定型。
- 夏秋指标四级跳与 12 月委员会档案链（L26、L30、L32–36、L75–90）：对照 `DATA-06`、`CLM-davies-1980-autumn-1929-great-turn-fabrication`、`RN-W20` 及 `tragedy_soviet_village_v2_1929_zh/ch04`–`ch05`，`6月1日 100万户/3.9%`、`10月1日 190万户/7.5%`、`7月 800万→8月 1300万→10月 1500万→12-11 俄联邦 2400万公顷(+60%)`（不混同全苏 `~3000万` 公顷）、`12-18` 一致草案保留家庭奶牛与退社退股权（非恢复 NEP）、`12-25` 斯大林致莫洛托夫信“不合适”、`12-27` 土地学家会议演说，全部逐一可证。
- Zemskov 人口边界与 Arapovich 数据（L66–68）：`1,803,392`（1930–1931 特殊移民含重复子集，不得标为 1929 死亡）、拒采 `1930.08` `21.4%` 为 1929 自愿率、B 级译稿 metadata 分列、`28.8%/6.8%/20%` 配额定位准确。

### 6.2 审计发现
- **`E2-15` [P1]｜L30 将 Doc 9 的统计截点（“截至 1929 年 12 月 15 日”）错写为“12月15日以后汇总”**
  - **卡片原文（L30）**：“12月15日以后汇总下伏尔加96区中51区报称集体化≥70%，这不是‘全苏53.1%的农户已入庄’（`CLM-tragedy-village-1929-november-plenum-escalation`）。”
  - **馆藏实证核查**：核对一级原件 `sources/primary/tragedy_soviet_village_v2_1929_zh/ch04_1929年11月_1930年12月_part_2.md` L156–166（Doc 9）及 `DATA-06` L140、`CLM-tragedy-village-1929-november-plenum-escalation` L28：
    > 文件标题：《苏联国家统计局关于各地区集体化进展的资料 和苏联边缘**截至1929年12月15日**，根据报道编制……》；落款编成日期标为“**不早于 1929年12月15日**”（`≥1929-12-15`）。
    “12月15日以后”是**汇编文件成文日期下限**，而非数字涵盖的时点——51/96（53.1%）统计的是**截至 1929 年 12 月 15 日**的进度。现行缩略句抹去了“截至12月15日”截点，容易被误读为“12月15日之后（下旬）才达到该水平”。

- **`E2-16` [P1]｜L26 跳过 1929 年 4 月联席全会与第十六次党代表会议（`17.5%` 播种比例基准）具名节点，且 L28 遗漏 `1929-11-25/26` 右翼公开检讨日期**
  - **卡片原文**：
    - L26：“1929年春正式批准的五年计划没有设定年底即完成全盘集体化：Davies记其至1933年春预计集体农庄约370万户。”
    - L28：“11月10—17日中央全会将布哈林逐出政治局，警告李可夫、托姆斯基等并要求停止右倾宣传；后二人未在同一日丧失全部党政职务。”
  - **馆藏实证核查**：
    1. 核对 `cards/meetings/MTG-1929-04-cc-joint-plenum.md` L10–11, L28 及 `timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md` L215–219：1929 年春真正承接 4 月 `16—23 日` 联席全会并正式批准一五计划“最优方案”的党史节点是 **`1929 年 4 月 23—29 日` 联共（布）第十六次党代表会议**，其批准方案预设到五年计划期末（1932/33 年）集体农庄与国营农场合计仅占全国播种面积 **`17.5%`**（另有 Davies 所记至 1933 年春集体农庄约 `370 万户` 指标）。L26 未具名“第十六次党代表会议（04-23—29）”和 **`17.5%`** 播种面积占比基准，使 `4月会议 → 11月全会 → 12月27日讲话` 三段跃迁的春季起点不够清晰；
    2. 同理，L28 只写李可夫、托姆斯基未在 `11-17` 同日失职，遗漏了紧随全会闭幕 8 天后 **`1929-11-25` 三人联署、`11-26` 见报《真理报》** 的公开检讨声明（`MTG-1929-11-cc-plenum.md` L26、`L3 1928-1929` L256）——即科恩所界定的布哈林有组织反对派正式终结日。

- **`E2-17` [P2]｜L88 漏标 Doc 15 所占 `PDF p.90`，且 §2.2 边表漏列 `PER-rykov`、`PER-tomsky`、`MTG-1929-04-cc-joint-plenum`（附 `DEB-1928` 反向不对称提示）**
  - **馆藏实证核查**：
    1. `sources/primary/tragedy_soviet_village_v2_1929_zh/ch05_1929年11月_1930年12月_part_3.md` L224–270 显示，Doc 15（`12-22` 雅科夫列夫报告）位于 **`PDF p.90`**，Doc 16（`12-25` 斯大林致莫洛托夫信）题头在 `p.90` 末而正文在 **`PDF p.91`**。L88 合写为“12月22日呈报Doc 15及25日信Doc 16（p.91）”漏掉了 `p.90`；
    2. 正文 L28、L38 均写及李可夫、托姆斯基（且 L38 特别提及库班抗议者高呼布、李、托三人姓名），但 §2.2 边表只列 `PER-bukharin` 而未列实存节点 `PER-rykov`、`PER-tomsky` 及春季基线节点 `MTG-1929-04-cc-joint-plenum`（注：雅科夫列夫本人站内尚未建 `PER-yakovlev` 卡，不予虚挂）；
    3. 本卡 L15 挂接 `DEB-1928-bukharin-alternative`，但 `historiography/debates/DEB-1928-bukharin-alternative.md` L9 `core_cards` 未反向列出 `EVT-1929-great-turn-and-dekulakization-launch`（跨卡图谱同步备注）。

---

## 07｜汇总统计与可执行精确修复矩阵（`E2-01`..`E2-17`）

### 7.1 严重度与卡片分布汇总
| 卡片 | P0 | P1 | P2 | 合计 | 编号 |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `01｜EVT-1918-1920-russian-civil-war.md` | 0 | 1 | 2 | 3 | `E2-01`, `E2-02`, `E2-03` |
| `02｜EVT-1920-1921-tambov-and-peasant-revolts.md` | 0 | 2 | 1 | 3 | `E2-04`, `E2-05`, `E2-06` |
| `03｜EVT-1921-kronstadt.md` | 1 | 1 | 1 | 3 | `E2-07`, `E2-08`, `E2-09` |
| `04｜EVT-1923-scissors-crisis.md` | 0 | 1 | 1 | 2 | `E2-10`, `E2-11` |
| `05｜EVT-1928-grain-procurement-crisis.md` | 0 | 2 | 1 | 3 | `E2-12`, `E2-13`, `E2-14` |
| `06｜EVT-1929-great-turn-and-dekulakization-launch.md` | 0 | 2 | 1 | 3 | `E2-15`, `E2-16`, `E2-17` |
| **总计** | **1** | **9** | **7** | **17** | `E2-01`..`E2-17` |

> **`[T1]` 长度约束复核**：上述全部 17 项修复建议均**不触及任何卡片的 `## [T1]` 微摘要段落**；修复实施后，6 张卡的 `[T1]` 去空白字数仍严格维持在 **113–118 字**（均 `≤ 150` 字红线）。

### 7.2 精确可执行修复矩阵

| 编号 | 等级 | 卡片文件 | 行号 | 问题摘要 | 建议精确替换文本 |
| :---: | :---: | :--- | :---: | :--- | :--- |
| `E2-01` | **P1** | `cards/events/EVT-1918-1920-russian-civil-war.md` | L59 | 错将 Mawdsley 2008 年序“农民政治无力”挂给 `sovdepia-demographic-industrial-base` 卡，实载于 `civil-war-militarized-regime` 卡 | 将 `（`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`；RN-W6）。` 拆分为：`……是胜利的基础（`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`）；其2008年序又明确，‘农民政治上的无力’不是没有农民起义，内部战争也不能无证据地取代红白主战场为首要军事解释（`CLM-mawdsley-1987-civil-war-militarized-regime`；RN-W6）。` |
| `E2-02` | **P2** | `cards/events/EVT-1918-1920-russian-civil-war.md` | L26, L30 | 捷克军团起义、RVSR 成立与高尔察克春攻／红军反攻起讫日期模糊压缩 | L26 `与1918年春夏捷克斯洛伐克军团冲突` → `与1918年5月下旬捷克斯洛伐克军团起义`；`9月成立共和国革命军事委员会` → `9月2日成立共和国革命军事委员会`；L30 `高尔察克春攻在4—6月遭红军东线反击` → `高尔察克3月初发动春攻，4月28日至6月9日遭红军东线南集群反击并丢失乌法` |
| `E2-03` | **P2** | `cards/events/EVT-1918-1920-russian-civil-war.md`（联动 `debates/DEB-1918`） | L15（跨卡 L6） | `DEB-1918-war-communism-ideology-or-emergency` 未反向收录本卡于 `core_cards` | 本卡 L15 保留不动；待后续图谱同步波次在 `historiography/debates/DEB-1918-war-communism-ideology-or-emergency.md` L6 `core_cards` 补入 `"EVT-1918-1920-russian-civil-war"` |
| `E2-04` | **P1** | `cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md` | L10, L26, L28 | 遗漏馆藏明载爆发日 `1920-08-19`、卡缅卡村起点及初期普列日尼科夫领导阶段 | L10 `start_ns: "1920-08-01"` → `start_ns: "1920-08-19"`（或保留月窗并于 L26 注出）；L26 `1920年夏坦波夫抗征粮冲突扩展为安东诺夫武装主导的起义` → `1920年8月19日基尔萨诺夫县卡缅卡村（Kamenka）爆发抗征粮起义，初期由地方农民普列日尼科夫（G. Plezhnikov）领头，11月安东诺夫出任统一军事总指挥，扩展为大规模农民战争` |
| `E2-05` | **P1** | `cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md` | L32, L86 | 绕过站内 `PER-tukhachevsky`（`0116` 号令、`04-27` 任命）与 `Leggett`/`PER-antonov` 具体清剿数字 | L32 `图哈切夫斯基统率集中兵力，以正规军、骑兵和技术兵器清剿` 补实为：`1921年3月1日红军已投入32,500步兵与8,000骑兵，4月27日图哈切夫斯基受命全权统帅（5月6日抵前线），在正规军围剿外配以第130、171号人质/集中营令及第0116号毒气清剿令（`PER-tukhachevsky`、`PER-antonov`；Leggett 记游击队由5月约21,000人降至7月中旬约1,200人，至7月20日扣押约5,000名人质，Figes 另估6月底约50,000农民入营）。`；L86 说明改为：`第130、171号与第0116号命令编号及性质已在站内 `PER-tukhachevsky` 辨析，其俄文原件、第0116号确切签发日及毒气实际投放/致死统计仍待 S 级补核。` |
| `E2-06` | **P2** | `cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md` | §3.2（L82 后） | §3.2 来源表漏列已入库 `Leggett (1981)` 与 `PER-antonov.md`，且 `DEB-1918` 反向不对称 | 在 L82 后追加两行：<br>`- [Leggett：契卡清剿坦波夫](../../sources/monographs/leggett_1981_cheka/ch12_pages_361-390.md)：A 级，1920-08-19 爆发日、兵力变化与人质数字（pp.330—334）。`<br>`- [安东诺夫人物卡](../../cards/people/PER-antonov.md)：早期领导演变与镇压估算汇核。`<br>（另建议后续同步在 `DEB-1918` L6 补入 `"EVT-1920-1921-tambov-and-peasant-revolts"`） |
| `E2-07` | **P0** | `cards/events/EVT-1921-kronstadt.md` | L32 | **反向史实错误**：强行禁止把图哈切夫斯基列为 3 月 5 日最后通牒第三联署人，直接违背 Avrich `ch06` p.161 fn.25 与 `L3 1921-03` L86；且 `谢尔盖·加米涅夫` 易与 `L. B. Kamenev` 混淆 | `3月5日最后通牒由托洛茨基与红军总司令谢尔盖·加米涅夫签发；图哈切夫斯基受命指挥第七集团军，不能把他加写为该通牒的第三位联署者。` → `3月5日最后通牒由托洛茨基署名发布，并与红军总司令谢·谢·卡梅涅夫（S. S. Kamenev，区别于列·鲍·加米涅夫）及新任第七集团军司令图哈切夫斯基联合签发（Avrich ch06 p.161 fn.25；1921年3月微距卷）。` |
| `E2-08` | **P1** | `cards/events/EVT-1921-kronstadt.md` | L54, L71 | L71 对 Avrich 3 张卡页码指责以偏概全（仅 `white-plot` YAML 混入 `816-818`）；L54 忽视站内 Figes `ch22` L81 与 `L3` L52/199 已实载 Getzler `94%` 双舰统计 | L54 `现有论断也未给出足以代表全要塞的‘94%老兵’统计（`CLM-avrich-1970-sailor-social-composition`）。` → `站内 Figes（ch22）与微距卷转引 Israel Getzler 记“《彼得罗巴甫洛夫斯克》与《塞瓦斯托波尔》号两艘主力舰94%舰员于1918年前入伍”，但该口径仅覆盖两舰且 Getzler 原书未入藏，不能外推代表全要塞驻军（`CLM-avrich-1970-sailor-social-composition`）。`<br>L71 `Avrich本库按PDF分块，三张论断卡的历史页码字段与分块名并非处处对应，特别是白卫阴谋卡混入异常高页码；` → `Avrich 论断卡中仅 `CLM-avrich-1970-white-plot-refutation` 的 `original_pages` 混入 RN-W3 行号（816-818），前两张卡的印页字段与 `chNN_pages_XXX-YYY` 分块一致（`soviets-without-bolsheviks` 正文括号偶见行号）；` |
| `E2-09` | **P2** | `cards/events/EVT-1921-kronstadt.md` | L32, L69 | 未列站内 Avrich `ch09` pp.227–228、Figes `ch22` 与 `L3` L162–166 已有的分层伤亡与处决区间 | 在 L69 表格追加一行：<br>`\| 伤亡与镇压分层区间 \| 红军官方约700阵亡、2,500伤（彼得格勒医院收治>4,000、死527），美国领事 Quarton 估苏方总死伤约10,000（Figes 误作阵亡）；起义者据 Avrich ch09 约600阵亡、>1,000伤、2,500被俘，03-20 夜处决13人后数周续枪决数百至两千余人 \|` |
| `E2-10` | **P1** | `cards/events/EVT-1923-scissors-crisis.md` | L32 | 错把《四十六人声明》两份打字稿正文（`34+12=46`）与戈尔茨曼另纸（`+1=47` 人次）混写成“两份名单共47人次签名” | `两份名单共47人次签名、阿·戈尔茨曼重复，实为46位独立签名者；` → `俄文原件两份打字稿分别含34与12个正文签名（合计46人），阿·戈尔茨曼（А. Гольцман）另于10月12日附纸再签一次形成47人次落款，实为46位独立签名者；` |
| `E2-11` | **P2** | `cards/events/EVT-1923-scissors-crisis.md` | L30, L86（联动 L15） | L30 未标明 `276/89` 属国家计委（Gosplan）批发物价指数；L86 未注 Deutscher 论断卡跨辩论挂接与中译 B 级差异 | L30 `不能与另套276／89等数字混接` → `不能与 L3 微距卷所警示的另一套国家计委（Gosplan）批发指数（276／89）混接`；L86 `A 级作者解释，非当事人共识。` → `论断卡编目为 A 级作者解释（对应中译本无原书纸页，L3 另作 B 级处理，且该卡误挂 `DEB-1903`），非当事人共识。`（另备忘 `DEB-1922` / `DEB-1928` 反向同步） |
| `E2-12` | **P1** | `cards/events/EVT-1928-grain-procurement-crisis.md` | L15, L34, §2.2 | 彻底遗漏同期并行的 1928 年沙赫特事件（`EVT-1928-shakhty-affair-show-trial`）及 `DEB-1928-shakhty-specialist-baiting-and-cultural-revolution`（后者已将本卡列入 `core_cards`） | L15 `related_debates` 补入 `"DEB-1928-shakhty-specialist-baiting-and-cultural-revolution"`；L34 七月全会前增一句：`同期并行的沙赫特技术专家案（1928年3—7月）与征粮危机共振，7月9日5名死刑犯枪决正与斯大林七月全会“贡赋”暨“阶级斗争尖锐化”演说同日，而布哈林、托姆斯基三月附和抓捕削弱了同古比雪夫、奥尔忠尼启则的制衡联盟（`EVT-1928-shakhty-affair-show-trial`）。`；§2.2 边表新增 `\| `EVT-1928-shakhty-affair-show-trial` \| `parallel_political_track` \| 1928.03—07 \| 沙赫特案与粮食危机在四月、七月全会并行升级，重塑反右阵线 \| 沙赫特事件卡；L3 `1928-01` \|` |
| `E2-13` | **P1** | `cards/events/EVT-1928-grain-procurement-crisis.md` | L26, L30 | L30 沿用 Cohen“1月赴乌拉尔和西伯利亚”误述（实为什维尔尼克赴乌拉尔，斯大林 `01-15—02-06` 仅赴西伯利亚），且漏列 `1927` 年底 `1.28亿普特` 缺口与 `1928-01-06` 绝密指令 | L26 句末补：`（至1927年底国家收购较上年累计短缺约1.28亿普特／约209–210万吨，L3 `1928-01`）。`；L30 `斯大林1月赴乌拉尔和西伯利亚，1月20日新西伯利亚讲话把问题归为“富农”操纵并要求动用反投机刑法第107条。` → `1928年1月6日政治局签发斯大林起草的绝密督粮通令后，1月12日高层分兵（什维尔尼克赴乌拉尔、米高扬赴北高加索），斯大林本人1月15日至2月6日秘密巡视西伯利亚（Cohen 泛写“乌拉尔和西伯利亚”，实行程为新西伯利亚、巴尔瑙尔、鲁布佐夫斯克、鄂木斯克及克拉斯诺亚尔斯克），1月20日新西伯利亚闭门讲话把问题归为“富农”操纵并强令适用刑法第107条。` |
| `E2-14` | **P2** | `cards/events/EVT-1928-grain-procurement-crisis.md` | L38, §2.2 | L38 缺 `11-10—17` 全会区间与 `11-25/26` 检讨；§2.2 漏列正文所叙 `PER-tomsky`、`MTG-1929-04-cc-joint-plenum`、`MTG-1929-11-cc-plenum` | L38 `十一月全会将布哈林逐出政治局` → `11月10—17日中央全会将布哈林逐出政治局并警告李可夫、托姆斯基（25日三人签署检讨、26日见报）`；§2.2 边表补列 `PER-tomsky`、`MTG-1929-04-cc-joint-plenum`、`MTG-1929-11-cc-plenum` 三行 |
| `E2-15` | **P1** | `cards/events/EVT-1929-great-turn-and-dekulakization-launch.md` | L30 | 将 Doc 9 “**截至** 1929年12月15日”统计截点错缩为“12月15日以后汇总” | `12月15日以后汇总下伏尔加96区中51区报称集体化≥70%` → `成文不早于12月15日的苏联国家统计局汇总（统计截至1929年12月15日进度）显示下伏尔加96区中51区报称集体化≥70%` |
| `E2-16` | **P1** | `cards/events/EVT-1929-great-turn-and-dekulakization-launch.md` | L26, L28 | L26 漏写 1929年4月联席全会（`04-16—23`）与第十六次党代表会议（`04-23—29`）`17.5%` 播种比例基准；L28 漏写 `11-25/26` 右翼公开检讨日期 | L26 `1929年春正式批准的五年计划没有设定年底即完成全盘集体化：Davies记其至1933年春预计集体农庄约370万户。` → `1929年4月16—23日联席全会与4月23—29日第十六次党代表会议正式批准的一五计划“最优方案”，仍预设期末集体与国营农场合计仅占播种面积17.5%（Davies 另记至1933年春预计集体农庄约370万户），并未设定当年底完成全盘集体化。`；L28 `后二人未在同一日丧失全部党政职务。` → `后二人未在同一日被逐出政治局，直至11月25日三人联署公开检讨声明（26日见报）。` |
| `E2-17` | **P2** | `cards/events/EVT-1929-great-turn-and-dekulakization-launch.md` | L88, §2.2（联动 `DEB-1928`） | L88 漏标 Doc 15 所占 `PDF p.90`；§2.2 漏列 `PER-rykov`、`PER-tomsky`、`MTG-1929-04-cc-joint-plenum`；`DEB-1928` 反向不对称 | L88 `12月22日呈报Doc 15及25日信Doc 16（p.91）` → `12月22日呈报Doc 15（p.90）及25日信Doc 16（pp.90—91）`；§2.2 边表补列 `PER-rykov`、`PER-tomsky` 与 `MTG-1929-04-cc-joint-plenum`（注：`PER-yakovlev` 站内尚未建卡，不虚挂）；备忘后续在 `DEB-1928` L9 补入本卡 ID |

---

## 08｜审计闭卷 SHA-256 只读复核（0 篡改证明）

审计全部结束后再次执行只读 SHA-256 校验，6 张被审事件卡与开审前基线逐字节完全一致（**0 修改**）：

| 序号 | 卡片路径 | 开审前 SHA-256 | 闭卷后 SHA-256 | 一致性 |
| :---: | :--- | :--- | :--- | :---: |
| 01 | `cards/events/EVT-1918-1920-russian-civil-war.md` | `6d7fecf1277fc1c2781ee5925dee89812257a4ea180e2ad5a4ef1df94f02a7a1` | `6d7fecf1277fc1c2781ee5925dee89812257a4ea180e2ad5a4ef1df94f02a7a1` | ✅ 完全一致 |
| 02 | `cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md` | `8e7176ddbf7cb753cb17c2b794e0734257d895acad2475229ea410ec21b2bbd4` | `8e7176ddbf7cb753cb17c2b794e0734257d895acad2475229ea410ec21b2bbd4` | ✅ 完全一致 |
| 03 | `cards/events/EVT-1921-kronstadt.md` | `111402b2915e60db3d926255712ff411b83b035d23d012dcf20ffe18da33c3aa` | `111402b2915e60db3d926255712ff411b83b035d23d012dcf20ffe18da33c3aa` | ✅ 完全一致 |
| 04 | `cards/events/EVT-1923-scissors-crisis.md` | `edc6d979a8f88f8980ac5c678bdd45fc889c2f4dbdac4515c06a010ed475bfb6` | `edc6d979a8f88f8980ac5c678bdd45fc889c2f4dbdac4515c06a010ed475bfb6` | ✅ 完全一致 |
| 05 | `cards/events/EVT-1928-grain-procurement-crisis.md` | `7f8c493e88932ce3cbda7175e8f597803c5dbbca13dd8b7a02fd0c8900b486c5` | `7f8c493e88932ce3cbda7175e8f597803c5dbbca13dd8b7a02fd0c8900b486c5` | ✅ 完全一致 |
| 06 | `cards/events/EVT-1929-great-turn-and-dekulakization-launch.md` | `6e3cb59e6fbfb3490bfa96037e41729c65184bfb22b118f07151817a9817df35` | `6e3cb59e6fbfb3490bfa96037e41729c65184bfb22b118f07151817a9817df35` | ✅ 完全一致 |

