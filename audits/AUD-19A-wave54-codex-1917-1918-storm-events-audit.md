# AUD-19A｜W60-G1：Wave 54 1917–1918 风暴期六张核心事件卡跨家族对抗审计

- **审计日期**：2026-11-19
- **审计官**：Google Gemini（跨家族对抗审计官，`W60-G1` / `AUD-19A`）
- **被审编纂**：OpenAI `gpt-6.1-sol`（Wave 54 / `W54-C1` 升格定稿，Batch E1 六张 1917–1918 风暴期核心事件卡）
- **只读与工具边界**：唯一允许写入/修改的文件为本报告；严禁修改任何 `cards/`、`claims/`、`debates/`、`sources/`、`graph/`、`config/` 文件；全程零 `read_url_content`、零外网抓取、零子代理派生、零 `pack --write` 或 `sync_graph_and_packs.py`；一切史实、数字、页码、机构译名与引证均基于本地馆藏（`sources/monographs/`、`sources/web-archive/`、`reading-notes/`、`data/`、`timeline/L3_daily/`、`historiography/` 及相邻卡片）。
- **两阶段落盘**：阶段一已完成六卡机械检查与 01–03 逐行原书核验并先期写盘；本终稿补齐 04–06 三张卡逐行核验、全局统计、可执行精确替换矩阵及六卡 SHA-256 前后一致性复核。

---

## 一、六卡机械合规与双历算术总览

通过只读 Python 脚本对六张被审卡执行 YAML 解析、`[T1]` 去空白字符计数、`2.2` 边表列数检查、本地相对链接实存校验、反引号实体 ID 全库索引校验，以及全部显式 `[O.S.] / [N.S.]` 双历日期对的 `+13` 日算术校验。

| 编号 | 事件卡 ID | YAML 必填与 `multi-perspective` | `[T1]` 去空白字数（≤150） | `2.2` 边表列数 | 相对链接断链 | 反引号 ID 悬空 | 外链数 | 历法核查结果 |
| :--- | :--- | :---: | ---: | :---: | ---: | ---: | ---: | :--- |
| 01 | `EVT-1917-02-february-revolution` | 合规 | 104 | 严格 5 列（11 行） | 0 | 0 | 0 | 16/16 组显式双历 `+13` 日通过；L71 缺 `[N.S.]` 标示（见 `E1-04`） |
| 02 | `EVT-1917-07-july-days` | 合规 | 108 | 严格 5 列（11 行） | 0 | 0 | 2 | 17/17 组显式双历 `+13` 日通过 |
| 03 | `EVT-1917-10-october-revolution` | 合规 | 109 | 严格 5 列（12 行） | 0 | 0 | 2 | 22/22 组显式双历 `+13` 日通过 |
| 04 | `EVT-1918-01-constituent-assembly-dispersal` | 合规 | 114 | 严格 5 列（11 行） | 0 | 0 | 3 | 11/11 组显式双历 `+13` 日通过 |
| 05 | `EVT-1918-03-brest-litovsk-treaty` | 见 `E1-11` | 106 | 严格 5 列（11 行） | 0 | 0 | 1 | 改历前 6/6 组 `+13` 日通过；**YAML 违规保留改历后伪构 `end_os: '1918-03-02'`**（全库事件卡唯一特例，见 `E1-11`） |
| 06 | `EVT-1918-09-red-terror-and-left-sr-rupture` | 合规 | 112 | 严格 5 列（12 行） | 0 | 0 | 5 | 全改历后公历，无重复加减 13 日错位 |

**总体评价**：Batch E1 六张卡在结构合规、表层双历算术（+13 日）、多学派视域覆盖（尤其是对 Pipes、Rabinowitch、Radkey、Daniels、Leggett、Mozokhin、S. A. Smith、Koenker 的并列辨析）及区分“署日/跨午夜表决”“选票/席位/党派”“命令文本/执行清单”等方面整体编纂水准较高，未见断链、悬空 ID 或显式双历加减算术错误。但跨模型家族下钻原书切片逐行比对后，仍检出 **1 项 P0（原书统计数据倒置）、10 项 P1（机构误译、切片/章节号混写、二手转引误归、决议时间前移、零命中数据表挂接、选举层级混称、改历后伪构 `end_os`、提示词元话语泄漏、`[T1]` 单学派事实化、原书归因/页码偏漏）及 5 项 P2（合计 16 项）**。

---

## 二、阶段一逐卡深审（01—03）

### 01｜`cards/events/EVT-1917-02-february-revolution.md`（1917年二月革命）

**正向核验**：
- 1917-02-22 至 03-03 [O.S.] 全部 16 组双历换算（+13 日）正确；
- 2 月 22 日 [O.S.] 普梯洛夫闭厂 `26,700` 人与 Hasegawa `ch18_chapter_11_the_workers_and_the_revolutio.md`（印刷 p. 197 / PDF p. 218）吻合；
- 2 月 26 日 [O.S.] 四处主要射击约 `170–200` 人死伤与 `ch23_chapter_15_bloody_sunday_february_26.md`（p. 264）吻合；
- 3 月 3 日 [O.S.] 立宪民主党中央决定、临时政府首次内阁会议第 87 条争议、格林卡未制作正式纪要与 Nikolaev 保留均与 `ch40_chapter_29_the_provisional_government_th.md`（pp. 625–628 / PDF pp. 646–649）主旨一致；
- `pipes_1990_russian_rev/ch16_section.md`（Ch. 8 *The February Revolution*）与 `figes_1996_peoples_tragedy/ch15_8_glorious_february.md` 均精准对应二月革命章节。

**检出问题**：

- **`E1-01`｜P0｜2 月 23 日罢工受波及工厂数在保安局与警察/公署报表之间完全颠倒（违背所引原书）**
  - **位置**：`EVT-1917-02-february-revolution.md` L47。
  - **原文**：`| 1917-02-23 [O.S.] / 03-08 [N.S.] | 78,444／50 | 公署87,534／43厂 | 128,388人 | 后一数包含被闭厂的普梯洛夫工人；Hasegawa pp.206–208。 |`
  - **原书铁证**：`sources/monographs/hasegawa_february_1917/ch20_chapter_12_the_beginning_february_23.md`（印刷 p. 208 fn. 24 / PDF p. 229）原文逐字载明：
    > *"According to the Okhrana report, the number of strikes and of the struck factories was respectively **78,444 and 43**; according to the police report, respectively **87,534 and 50**; according to Leiberov, **128,388 and 49**."*
  - **成因与定级**：卡片盲从了上游 `DATA-01` 的既有倒置错误而未回核所引 Hasegawa p. 208 注 24，导致保安局（Okhrana）`43` 厂与警察报表 `50` 厂彻底互换。此属直接违背所引原书核心统计的硬错，定级 **P0**（并请主控官在后续维护波次同步核修上游 `DATA-01`）。

- **`E1-02`｜P1｜将直属沙皇内政部的彼得格勒市行政长官/治安总长 `Gradonachal'nik`（巴尔克）及其公署误译为“市长公署”**
  - **位置**：`EVT-1917-02-february-revolution.md` L45、L47–49。
  - **原文**：表头作 `市长公署报表／巴尔克约计`，行内称 `公署87,534／43厂`、`公署197,000／131厂；巴尔克约200,000人`、`公署／巴尔克240,000人`。
  - **原书核验**：Hasegawa `ch20`–`ch22` 明确称 A. P. Balk 为 `Gradonachal'nik`（градоначальник，沙皇内政部直属彼得格勒市行政长官／首都警政治安长官），`gradonachal'stvo` 为首都治安指挥中枢（*"headquarters of the security authorities during the February days"*）。译为“市长公署”极易与民选城市杜马市长（`городской голова`，P. I. Lelianov / Yu. N. Glebov）混淆；且 23 日 `87,534 / 50` 厂原书注 24 明确为 `police report`（警察局报表），24–25 日方为 `gradonachal'stvo`。定级 **P1**。

- **`E1-03`｜P1｜Hasegawa 馆藏切片文件名编号与原书章节号混写，`ch20–22` 未入 T3，且 `p.626` 起页偏后 1 页**
  - **位置**：`EVT-1917-02-february-revolution.md` L43、L53、L57、L63、L65。
  - **核验**：本地 `sources/monographs/hasegawa_february_1917/` 中，`ch20`–`ch22` 是切片前缀，对应原书 **Chapters 12–14**（原书 Ch. 20–22 实为 `ch29`–`ch32` 苏维埃与尼古拉二世章）；`ch40` 对应原书 **Chapter 29**（立宪民主党中央 3 月 3 日决议载于印刷 **p. 625** [PDF p. 646]，非 p. 626）；`ch41` 对应原书 **Chapter 30**。正文写 `ch20–22` 却未在 T3 给出对应切片链接，读者必然误检原书第 20–22 章。定级 **P1**。

- **`E1-04`｜P2｜对 T3 已链 `ch41` 的列伊别罗夫伤亡互斥可加性判断失准，且边表 L71 时段未标公历、依据挂接偏移**
  - **位置**：`EVT-1917-02-february-revolution.md` L53、L71。
  - **核验**：
    1. L53 称“致残与受伤的人员重叠未由本地摘要核清，故不把三栏相加制造独立人数总额”，但 T3 L87 直接链接的 `ch41_chapter_30_conclusion.md` 紧接其后明写：*"Of the total of **1,740** killed, wounded and crippled insurgents, 535 or 30 percent were workers and 832 or 48 percent were soldiers"*（`313 + 1,136 + 291 = 1,740`），表明列伊别罗夫对起义者三栏实按互斥口径汇总（仅双方合并总和 `1,947` 未由原书明示）；
    2. L71 `EVT-1917-10-october-revolution` 有效时段作 `1917-03至11`，未标注 `[N.S.]`（俄历十月革命在 10 月），且依据列挂 `CLM-blanc-2021-borderlands-in-1905-and-1917`（核心论题为帝国边疆 vs 中心政治分化，与该行“二月制度冲突构成十月条件”并非最直接对应）。定级 **P2**。

---

### 02｜`cards/events/EVT-1917-07-july-days.md`（1917年七月事变）

**正向核验**：
- 17 组显式双历算术（+13 日）全部无误；
- 严格区分 6 月 18 日 [O.S.] 攻势受阻与 7 月 6 日 [O.S.] 德奥反攻全面溃败、区分李沃夫在任与克伦斯基事变后接任、区分托洛茨基当时区联派身份；
- 对 Pipes `ch19_section.md` 的核读准确无误：原书确有 *"His role in the preparations for the July escapade cannot be established"* 及 *"the exact uses to which the Bolsheviks put the German money remains obscure"*；
- 7 月 3 日下午 4 时中央委员会劝阻决定获 Rabinowitch `ch07_5七月起义开始.md`（L386–393 / PDF p. 87）证实。

**检出问题**：

- **`E1-05`｜P1｜将斯塔尔采夫（V. I. Startsev）的档案估算误归为 Boll（1979）本人估算，并漏标时段与 T3 锚点**
  - **位置**：`EVT-1917-07-july-days.md` L52 及 T3（L76–90）。
  - **原文**：`Boll估计约五千至六千赤卫队员，属于武装工人组织规模，不能充作全部游行人数。`
  - **原书与论断核验**：`historiography/claims/CLM-boll-1979-red-guards-radicalization-to-july.md` L34 直引 Boll (1979, p. 143) 原文：
    > *"The careful calculations of **V. I. Startsev**, based upon archival records of a special benefit fund established in 1930 for former Red Guardsmen, indicate that five to six thousand Red Guardsmen existed in Petrograd **at the end of June** despite the negative posture of the Petrograd Soviet."*
  - **定级**：将 Boll 转引的苏联史家斯塔尔采夫（V. I. Startsev）“6 月底”档案估算简写成“Boll 估计”，属二手转引归因失准，且 T3 未挂接 `CLM-boll-1979-red-guards-radicalization-to-july`。定级 **P1**。

- **`E1-06`｜P1｜中央委员会最终转向并撤回《真理报》制止呼吁的时间被前移至“午夜前”**
  - **位置**：`EVT-1917-07-july-days.md` L46。
  - **原文**：`午夜前中央撤回已付排的反示威呼吁，决定出面领导“和平而有组织的武装示威”，次日《真理报》头版因而留白。`
  - **原书铁证**：Rabinowitch《革命的前奏》本地中译切片 `sources/monographs/rabinowitch_1968_prelude_zh/ch07_5七月起义开始.md`（L529、L686–702 / PDF pp. 91, 95–96）明载：
    - L529：“尽管布尔什维克中央委员会**直到 7 月 4 日凌晨才改变其反对街头示威的官方立场**……”
    - L686：“在执行委员会开始联席会议后不久（即**大约凌晨 1 点**），布尔什维克中央委员会数小时来第一次成员齐集，在塔夫利达宫与彼得格勒委员会和军事组织的代表会面。”
    - L695–701：直到约**凌晨 2 点**三万名普梯洛夫工人抵达塔夫利达宫并接到喀琅施塔得拉斯科尔尼科夫来电后，中央委员会才最终决定授权领导，并于 **7 月 4 日凌晨**从当天《真理报》样板中撤下制止呼吁。
  - **成因与定级**：卡片直接照搬 `RN-W8B` 札记的压缩表述（“午夜前”），未核对原书 `ch07`，把 7 月 4 日凌晨 1–2 时以后的关键决策错压缩回 3 日午夜前。定级 **P1**。

- **`E1-07`｜P1｜T3 挂接 `DATA-01` 对七月事变属零命中无关数据表**
  - **位置**：`EVT-1917-07-july-days.md` L83。
  - **核验**：全文检索 `data/DATA-01-1905-1917-strikes-and-petrograd-elections.md`，`七月`、`July`、`07-03`、`07-04`、`赤卫队`、`机枪` 均为 **0 命中**（该表仅覆盖 1905 罢工、1917.02 罢工、5–6 月 12 区杜马选举、夏苏维埃工人部/厂委会、9 月 9 日主席团表决与立宪会议），且 Card 02 正文全篇未引用 `DATA-01` 任何数值；相反，正文实际引用的 Boll/Startsev 赤卫队论断卡却缺失于 T3。定级 **P1**。

---

### 03｜`cards/events/EVT-1917-10-october-revolution.md`（1917年十月革命）

**正向核验**：
- 22 组显式双历算术（+13 日）全部正确；
- `DATA-01` 的 20.4% / 55% / 73%、10 月 10 日中央 `10:2`、10 月 16 日扩大会议异文（托洛茨基 `20:2:3` vs 本地拉比诺维奇中译切片 `ch14_12起义道路上的障碍.md` `19:2:4`）、苏汉诺夫记国际主义派党团约 `14:12` 决定跟退、`1917-10-26_decrees-on-peace-and-land.md` 的 242 份农民委托书与跨午夜闭幕（10 月 27 日凌晨 5 时 15 分）、11 月 4 日 [O.S.] 温和派辞职与莫斯科 10 月 25 日—11 月 2/3 日 [O.S.] 巷战均获本地馆藏证实；
- `figes_1996_peoples_tragedy/ch18_11_lenin_s_revolution.md` 精确对应十月革命章。

**检出问题**：

- **`E1-08`｜P1｜将莫斯科 6 月“市杜马”选举与 9 月“17 区杜马”选举混称为同一级“莫斯科区杜马”**
  - **位置**：`EVT-1917-10-october-revolution.md` L43。
  - **原文**：`DATA-07所录莫斯科区杜马布党选票由1917-06-25 [O.S.] / 07-08 [N.S.] 75,409票升至09-24 [O.S.] / 10-07 [N.S.] 199,337票（约51%）`
  - **数据表铁证**：`data/DATA-07-1905-1918-unions-moscow-swings-and-constituent-assembly-votes.md` L94–97 明确将两次选举分列为不同行政层级：
    - `1917-06-25 [O.S.] / 07-08 [N.S.]` 为**莫斯科市杜马选举**（总有效票 `615,393`，投票率约 `63%`，布党 `75,409` 票，占 `11.7%` / `12%`）；
    - `1917-09-24 [O.S.] / 10-07 [N.S.]` 为**莫斯科 17 区杜马选举**（总有效票 `387,280`，投票率约 `38%`，布党 `199,337` 票，占 `51%`）。
  - **定级**：将市级杜马与区级杜马混写成同一级“莫斯科区杜马”，属选举口径错写。定级 **P1**。

- **`E1-09`｜P2｜Pipes 冬宫局部“约五人死亡”在所挂 `CLM-pipes-1990-october-classic-coup` 中 0 命中，T3 缺原书 `ch20_section.md` 链接**
  - **位置**：`EVT-1917-10-october-revolution.md` L49 及 T3（L78–103）。
  - **核验**：L49 提及“Pipes 的冬宫局部约五人死亡”，原书 `sources/monographs/pipes_1990_russian_rev/ch20_section.md` 确有原文（*"The total casualties were five killed and several wounded, most of them victims of stray bullets"*），但 T3 仅链 `CLM-pipes-1990-october-classic-coup.md`（经检索该论断卡含 `冬宫`/`五`/`死` 均为 0 命中），未直接挂接 `ch20_section.md`。定级 **P2**。

---

## 三、阶段二逐卡深审（04—06）

### 04｜`cards/events/EVT-1918-01-constituent-assembly-dispersal.md`（1918年1月全俄立宪会议召开与解散）

**正向核验**：
- 11 组显式双历算术（+13 日）全部无误；
- 斯维亚季茨基/Radkey 703 席分母（`299 + 81 + 19 = 399 / 703 = 56.8%`；布党 `168 / 703 = 23.9%`）与普罗塔索夫/姚海 715 席口径（`370 + 40 = 410 / 715 = 57.3%`；布党 `175 / 715 = 24.5%`）严格分列，并与 `DATA-07`、`ORG-psr`、`CLM-yao-hai-constituent-assembly-vs-soviet-legitimacy-clash` 完全吻合；
- 两京市区总体未过半（彼得格勒含驻军 `45.2%` / 驻军 `75%`；莫斯科 `47%–47.9%` / 驻军 `90%`）与 `DATA-07` 严丝合缝；
- 主席选举 `244:153`（Rabinowitch `ch08` p. 114）、议程表决 `237:146`（p. 120）、热列兹尼亚科夫“卫兵累了”（p. 124）、斯维尔德洛夫 1 月 11 日 [O.S.] 三大报告 21 死（p. 109）与《新生活报》医院调查 15 死（pp. 109–110）均获原书证实；
- `pipes_1990_russian_rev/ch21_section.md` 与 `RN-W20` 均命中立宪会议内容，无零命中错挂。

**检出问题**：

- **`E1-10`｜P2｜Rabinowitch（2007）三处微观定位偏差：跨章缺链、`pp.106–109` 漏末页 p.110、混淆 5 日党团会议与 6 日中执委会反对者场景**
  - **位置**：`EVT-1918-01-constituent-assembly-dispersal.md` L51、L53、L57 及 T3（L88）。
  - **原书核验**：
    1. L51 引 `Rabinowitch（2007）pp.89–91`（加米涅夫温和派与党团改组），核对切片范围可知印刷 pp. 89–91 位于 **第 3 章** `sources/monographs/rabinowitch_2007_in_power/ch07_3_gathering_forces.md`（Book pp. 80–103 / PDF pp. 103–126），而 T3 L88 仅链接了 **第 4 章** `ch08_4_the_fate_of_the_constituent_assembly.md`（Book pp. 104–128）；
    2. L53 标 `《新生活报》医院调查录15死，斯维尔德洛夫在01-11 [O.S.] / 01-24 [N.S.]苏维埃三大报告录21死（Rabinowitch pp.106–109）`，原书 `ch08` 中斯维尔德洛夫 21 死在 Book p. 109（PDF p. 132），但《新生活报》医院调查 15 死完整论述跨至 **Book p. 110**（PDF p. 133：*"fifteen estimated to have been killed by Gorky's pro-Constituent Assembly Novaia zhizn' based on a survey of Petrograd hospitals..."*），应标 `pp.106–110`；
    3. L57 在“同日稍后的全俄中央执行委员会正式解散法令才是国家机关的制度决定”后紧接“梁赞诺夫、洛佐夫斯基等反对仍未能阻止”；核原书 `ch08`，梁赞诺夫与洛佐夫斯基二人共同反对列宁路线发生于 **1 月 5 日 [O.S.] 布尔什维克立宪会议党团会议**（pp. 111, 121），而在 **1 月 6 日 [O.S.] 全俄中执委解散会议**（p. 125）公开抗议并要求停议调查者为**梁赞诺夫**（及左社司法人民委员什泰因贝格），洛佐夫斯基未出现在 6 日中执委记录中。定级 **P2**。

---

### 05｜`cards/events/EVT-1918-03-brest-litovsk-treaty.md`（1918年布列斯特-里托夫斯克和约危机与签约）

**正向核验**：
- 改历前 6 组显式双历（1917-11-20/12-03 至 1918-01-28/02-10）`+13` 日换算无误；
- 核心投票链经原书逐一核实全部精准：`1918-01-08 [O.S.] / 01-21 [N.S.]` 63 名积极分子咨询票（布哈林 32 : 托洛茨基 16 : 列宁 15）；`01-11 [O.S.] / 01-24 [N.S.]` 中央 `9:7`；`1918-02-18 [N.S.]` 晚中央 `7:5:1`（Rabinowitch `ch11`）；`02-23 [N.S.]` 中央 **`7:4:4`**（4 反对：布哈林、乌里茨基、布勃诺夫、洛莫夫；4 弃权：托洛茨基、克列斯廷斯基、捷尔任斯基、越飞，均在 Daniels `ch03` p. 76 及 Rabinowitch `ch11` 完全证实）；`02-23/24 [N.S.]` 全俄中执委终计唱名 `116:85:26` 与初计举牌 `112:86:22` 分列；`03-06..08 [N.S.]` 俄共七大 Rabinowitch p. 198（PDF p. 221）`30:12:4` vs Daniels p. 80 & p. 482 n. 52 `28:9`（`28:9:1`）并列辨析；
- T3 所链 `service_2009_trotsky_zh/ch03_19_夺取政权.md` 虽以第 19 章命名，但实际覆盖第 19–27 章，内含 29 处布列斯特/不战不和叙述，`daniels_1960_conscience/ch03_pages_76-100.md`（Book pp. 58–82）、`cohen_1973_bukharin/ch03–04`、`carr_bolshevik_rev_v3_zh/ch03_第五部分_苏俄与世界_part_1.md`（58 处命中）均命中有效，无错挂。

**检出问题**：

- **`E1-11`｜P1｜改历后事件在 YAML 中保留倒推伪构的 `end_os: '1918-03-02'`（全库事件卡唯一违例）**
  - **位置**：`EVT-1918-03-brest-litovsk-treaty.md` L15（YAML）及 L43。
  - **核验**：扫描全库 `cards/events/*.md`，**`EVT-1918-03-brest-litovsk-treaty.md` 是唯一一张对 1918-02-14 改历后日期填写 `*_os` 字段的事件卡**（相邻政策卡 `POL-brest-litovsk-treaty.md` 及本批 `EVT-1918-09-red-terror-and-left-sr-rupture.md` 均正确省略改历后 `*_os`）。尽管 L43 正文解释其为“推算儒略历坐标”，但在机器可读 YAML 中保留 `end_os: '1918-03-02'` 既违背全库改历后不置旧历的统一规范，又因 `1918-03-02` 紧邻 `1918-03-03 [N.S.]` 签约日，极易被下游脚本或读者误读为签约前一日。应从 YAML 删除 `end_os` 行（保留 `start_os: '1917-12-02'`、`start_ns: '1917-12-15'`、`end_ns: '1918-03-15'` 或 `1918-03-16`），并相应精简 L43 历法说明。定级 **P1**。

- **`E1-12`｜P1｜成品正文泄漏内部编纂提示词元话语（“任务示例所称布列斯特专门DEB文件”）**
  - **位置**：`EVT-1918-03-brest-litovsk-treaty.md` L43。
  - **原文**：`现库不存在任务示例所称布列斯特专门DEB文件，挂接实存的战时共产主义前夜／左派路线与红色恐怖起源争鸣，前者主题较本事件宽，不能冒称已有同名专卡。`
  - **问题**：在定稿百科卡片 `[T2]` 正文中直接出现“任务示例所称……”属于明显的编纂工作流指令泄漏，严重破坏知识库成品文本的自足性。应改写为中性说明（如说明本卡挂接的两张相邻争鸣卡范围大于布列斯特单一事件，删除“任务示例所称”等提示词残迹）。定级 **P1**。

- **`E1-13`｜P2｜全俄苏维埃四大 `784:261:115` 批准日期未交代 15 日夜至 16 日跨午夜异记，且 T3 缺 Rabinowitch 原书切片链接**
  - **位置**：`EVT-1918-03-brest-litovsk-treaty.md` L47、L53 及 T3（L76–94）。
  - **原书核验**：
    1. L53 单写 `15日以784∶261∶115批准和约`，但 T3 L87 直接链接的 `carr_bolshevik_rev_v3_zh/ch03_第五部分_苏俄与世界_part_1.md` 明记：“然后在 **1918 年 3 月 16 日**，在全俄苏维埃第四次代表大会上，经过两天激烈的辩论……以 784 票对 261 票的多数通过了政府批准的动议”；Rabinowitch `ch12`（p. 206）亦记左翼共产主义者于大会最后一日（16 日）宣读反对和约并宣布弃权的正式声明。实系 15 日深夜至 16 日凌晨跨午夜议程所致，建议仿照 Card 03 对土地法令的严谨写法改为“15 日夜至 16 日凌晨以 `784∶261∶115` 批准和约（法令署日多作 15 日，Carr 等通史记 16 日）”；
    2. 正文 L47、L53 直接引用 `Rabinowitch相关章节` 与 `Rabinowitch（2007，p.198）`，但 T3 仅链接 `RN-W2`，未直链实存的 `rabinowitch_2007_in_power/ch11_6_the_socialist_fatherland_is_in_danger.md` 与 `ch12_7_an_obscene_peace.md`。定级 **P2**。

---

### 06｜`cards/events/EVT-1918-09-red-terror-and-left-sr-rupture.md`（1918年夏左翼社革党决裂与红色恐怖制度化）

**正向核验**：
- 全部日期（`1918-06-11`、`07-04..10`、`07-06..07`、`07-06..21`、`07-10..11`、`08-11`、`08-30`、`09-02..05`、`09-10`、`1918-11`）均为苏俄改历后纯公历，无任何旧历混用或重复加减 13 日错位；
- `1918-09-05_decree-on-red-terror.md` 四项要点、9 月 10 日《消息报》第 195 号刊布、正文无“人质”条款、刊布本署库尔斯基/彼得罗夫斯基/邦奇-布鲁耶维奇与打字原稿另署福季耶娃（非列宁或捷尔任斯基亲署）全部与馆藏 S 级原典严丝合缝；
- 9 月 4 日《消息报》刊彼得罗夫斯基通电（Leggett `ch04` PDF p. 146）、1918 年 11 月拉齐斯《红色恐怖》引文（Leggett p. 114 / PDF p. 152）、Leggett `pp. 359–360`（PDF pp. 397–398）关于 `140,000` 直接处决与另估至少 `140,000` 镇压起义/监狱集中营死亡的口径均与原书逐字吻合；
- Mozokhin 34 省 `6,300`（反革命罪 `1,637`）、1919 前 7 月 35 省 `2,089`（反革命罪 `387`）、1921 年 `9,701`、有案可查约 `1.75 万` 及 VChK 全期上限 `不超过 5 万` 全部与 `mozokhin_extrajudicial_powers_zh/ch04`–`ch05`（PDF pp. 15–16）原书数据一致。

**检出问题**：

- **`E1-14`｜P1｜`[T1]` 将 Rabinowitch 的单学派修正解释（“意图逼废和约而非夺取苏维埃政权”）直接写为无归属、无争议事实**
  - **位置**：`EVT-1918-09-red-terror-and-left-sr-rupture.md` L36（`[T1]`）。
  - **原文**：`1918年7月左翼社革党刺杀米尔巴赫，意图逼废和约而非夺取苏维埃政权，继遭布党镇压。8月30日乌里茨基遇害、列宁遇刺后，9月5日红色恐怖法令把隔离阶级敌人与枪决制度化。一党垄断和暴力升级须分别追踪，登记死亡数不是全部受害者。`
  - **史学边界核验**：本卡 `[T2]` L46 自身即明确将该判断标注为 **“Rabinowitch 的核心修正”**（*"Rabinowitch（pp.294、308–309）认为……不是企图推翻苏维埃政权并自行夺权"*），边表 L60 亦明写“据 Rabinowitch”；原书 `ch17` p. 294 同样承认传统史学与苏联官方多将其视为企图推翻政权的叛乱（含普罗希扬短暂占领中央电报局等争议行动）。将这一仍具史学分歧的修正派解释无主语写入 `[T1]` 定性摘要，违背“不得把单一学派解释写成 `[T1]` 无争议事实”之铁律。修复后须保持 `[T1]` 去空白字数 ≤ 150（下文建议文本经实测为 **123 字**）。定级 **P1**。

- **`E1-15`｜P1｜Rabinowitch `ch17` 两处归因与页码偏差：将左社资格委质疑的 399 人简归“Rabinowitch 质疑”，且彼得格勒 161 人结案漏标 `p.301`**
  - **位置**：`EVT-1918-09-red-terror-and-left-sr-rupture.md` L44、L46。
  - **原书铁证**：
    1. L44 写 `Rabinowitch（2007，p.288）质疑约399名布党代表资格及构成，属于他的档案重建`；但 `ch17_11_the_suicide_of_the_left_srs.md` Book p. 288（PDF p. 311）原文明确交代：开幕初步席位为布党 `678`、左社 `269`、其余 `88`（共 `1,035` 正式代表），而 **`roughly 399 Bolshevik delegates whose right to be seated was challenged by the Left SR minority in the congress's credentials commission`**——`399` 并非 Rabinowitch 自行重建出的独立数字，而是**大会资格审查委员会中左翼社革党少数派当年提出质疑的布党代表人数**，Rabinowitch 援引该数并辅以莫吉廖夫省档案判断存在“大量旁证（substantial circumstantial evidence）”，同时在同页开篇坦言选举从未经过独立调查、现今亦恐难复查；
    2. L46 仅引 `Rabinowitch（pp.294、308–309）` 却在同段后半句给出“对后者被捕 161 人的调查至 12 月未证实反苏阴谋”，经核该条彼得格勒契卡 161 人档案及 `1918-12-10` 结案决议实载于 **Book p. 301（PDF p. 324）**，原页码漏列 `p.301`。定级 **P1**。

- **`E1-16`｜P2｜Mozokhin 表格第 3 行漏标原书明言的“约三年（缺 1920 年）”及“17 个地区未经核实”统计缺口**
  - **位置**：`EVT-1918-09-red-terror-and-left-sr-rupture.md` L77–79。
  - **原书核验**：`sources/monographs/mozokhin_extrajudicial_powers_zh/ch04`–`ch05`（PDF pp. 15–16）原文明确提示两项重要统计边界：(1) 1918（34 省 `6,300`）与 1919 前 7 个月（35 省 `2,089`）系与拉齐斯早年口径比对之汇总，且**“其中有 17 个地区的数据未经核实”**；(2) `约 1.75 万人` 明确写明系**“在近四年的三年时间里”**（即未完整计入 1919 年后 5 个月与 1920 年全年）。卡片表格仅注“漏计克里米亚、喀琅施塔得等”，补出原书明言的年份缺口与 17 地区未核实限定，可防读者把 `17,500` 误读为完整覆盖 1918–1921 四整年的连续档案总计。定级 **P2**。

---

## 四、问题分级汇总与可执行修复替换矩阵

### 4.1 统计汇总

| 等级 | 数量 | 编号清单 | 核心分布 |
| :--- | ---: | :--- | :--- |
| **P0** | **1** | `E1-01` | Card 01（1）：2 月 23 日罢工工厂数原书倒置 |
| **P1** | **10** | `E1-02`, `E1-03`, `E1-05`, `E1-06`, `E1-07`, `E1-08`, `E1-11`, `E1-12`, `E1-14`, `E1-15` | Card 01（2）、Card 02（3）、Card 03（1）、Card 05（2）、Card 06（2） |
| **P2** | **5** | `E1-04`, `E1-09`, `E1-10`, `E1-13`, `E1-16` | Card 01（1）、Card 03（1）、Card 04（1）、Card 05（1）、Card 06（1） |
| **合计** | **16** | `E1-01`–`E1-16` | 6 卡均有具体、可闭环的源码级改进项 |

### 4.2 可执行精准替换矩阵（主控官逐条闭环用）

| 编号 | 等级 | 卡片文件 | 行号 | 问题摘要 | 建议精确替换文本 / 操作 |
| :--- | :---: | :--- | :--- | :--- | :--- |
| `E1-01` | **P0** | `cards/events/EVT-1917-02-february-revolution.md` | L47 | 2 月 23 日保安局与警察/公署罢工工厂数倒置（`50` 与 `43` 互换，违背 Hasegawa p. 208 fn. 24） | 将 L47 替换为：`\| 1917-02-23 [O.S.] / 03-08 [N.S.] \| 78,444／43厂 \| 警察局87,534／50厂 \| 128,388人／49厂 \| 后一数包含被闭厂的普梯洛夫工人；Hasegawa 原书第12章（切片ch20）pp.206–208、注24。（同步记档待修上游DATA-01） \|` |
| `E1-02` | **P1** | `cards/events/EVT-1917-02-february-revolution.md` | L45, L48–49 | 将沙皇内政部直属市行政长官 `Gradonachal'nik`（巴尔克）及其治安机关误译为“市长公署” | 将 L45 表头 `市长公署报表／巴尔克约计` 替换为 `警察局／市行政长官公署（巴尔克）`；L48 `公署197,000／131厂；巴尔克约200,000人` 改为 `市行政长官公署197,000／131厂；巴尔克约200,000人`；L49 `公署／巴尔克240,000人` 改为 `市行政长官公署／巴尔克240,000人` |
| `E1-03` | **P1** | `cards/events/EVT-1917-02-february-revolution.md` | L43, L53, L57, L63, L65, T3 | Hasegawa 切片号（`ch20–22`/`ch40`/`ch41`）与原书章号（第12–14、29、30章）混写；`ch20–22` 缺 T3 链；L57 漏 p.625 | L43 `Hasegawa（2018，ch20–22）` 改为 `Hasegawa（2018，原书第12–14章／切片ch20–22）`；L53、L63 `Hasegawa ch41` 改为 `Hasegawa 原书第30章（ch41）`；L57、L65 `Hasegawa ch40，pp.626–634` 改为 `Hasegawa 原书第29章（ch40），pp.625–634`；T3 补链 `ch20`–`ch22` 三个切片 |
| `E1-04` | **P2** | `cards/events/EVT-1917-02-february-revolution.md` | L53, L71 | L53 误称列伊别罗夫三栏互斥性“未由本地摘要核清”（实 `ch41` 明记起义者合 `1,740`）；L71 `1917-03至11` 缺 `[N.S.]` 且依据列挂 Blanc 略偏 | L53 `致残与受伤的人员重叠未由本地摘要核清，故不把三栏相加制造独立人数总额。` 改为 `原书ch41将起义者三栏合计1,740人（313＋1,136＋291），显系按互斥口径统计；但双方合计1,947人未由原书明列，本卡仍保留分栏不另造全俄总额。`；L71 时段改为 `1917-03至10 [O.S.] / 03至11 [N.S.]`，依据列改为 `DEB-1917-dual-power-and-february-origins；CLM-blanc-2021-borderlands-in-1905-and-1917（边疆对照）` |
| `E1-05` | **P1** | `cards/events/EVT-1917-07-july-days.md` | L52, T3 | 将 Boll (1979, p. 143) 转引的 V. I. Startsev 6 月底档案估算误归为“Boll 估计”，且 T3 缺 Boll 论断卡 | L52 `Boll估计约五千至六千赤卫队员，属于武装工人组织规模，不能充作全部游行人数。` 替换为 `Boll（1979，p.143）转引斯塔尔采夫（V. I. Startsev）档案估算，6月底彼得格勒约有五千至六千名赤卫队员，属于武装工人组织基数，不能充作七月全部游行人数。`；T3 补链 `CLM-boll-1979-red-guards-radicalization-to-july` |
| `E1-06` | **P1** | `cards/events/EVT-1917-07-july-days.md` | L46 | 中央委员会转向与撤回《真理报》呼吁的时间误提前至“午夜前”，违背 Rabinowitch `ch07`（7 月 4 日凌晨 1–2 时后） | L46 `午夜前中央撤回已付排的反示威呼吁，决定出面领导“和平而有组织的武装示威”，次日《真理报》头版因而留白。` 替换为 `至7月4日 [O.S.] 凌晨约1时中央才在塔夫利达宫成员齐集，凌晨2时后（普梯洛夫工人抵达、拉斯科尔尼科夫来电后）方最终决定出面领导“和平而有组织的武装示威”，并撤回已付排的《真理报》反示威呼吁，致4日头版留白。` |
| `E1-07` | **P1** | `cards/events/EVT-1917-07-july-days.md` | L83 (T3) | T3 链接 `DATA-01` 对七月事变系 0 命中无关数据表 | 删除 L83 `- [DATA-01-1905-1917-strikes-and-petrograd-elections](../../data/DATA-01-1905-1917-strikes-and-petrograd-elections.md)`，替换为 `- [CLM-boll-1979-red-guards-radicalization-to-july](../../historiography/claims/CLM-boll-1979-red-guards-radicalization-to-july.md)`（并可按需补链 `rabinowitch_1968_prelude_zh/ch07_5七月起义开始.md`） |
| `E1-08` | **P1** | `cards/events/EVT-1917-10-october-revolution.md` | L43 | 将莫斯科 6 月“市杜马”与 9 月“17 区杜马”选举混称为同一级“莫斯科区杜马” | L43 `DATA-07所录莫斯科区杜马布党选票由1917-06-25 [O.S.] / 07-08 [N.S.] 75,409票升至09-24 [O.S.] / 10-07 [N.S.] 199,337票（约51%）` 替换为 `DATA-07所录莫斯科布党选票由1917-06-25 [O.S.] / 07-08 [N.S.] 市杜马选举的75,409票（约11.7%–12%，投票率约63%）升至09-24 [O.S.] / 10-07 [N.S.] 17区杜马选举的199,337票（约51%，投票率约38%）` |
| `E1-09` | **P2** | `cards/events/EVT-1917-10-october-revolution.md` | T3 (L86 后) | L49 所引 Pipes 冬宫约五人死亡在 `CLM-pipes-1990-october-classic-coup` 中 0 命中，T3 缺原书切片 | 在 T3 L86 后补链 `- [ch20_section](../../sources/monographs/pipes_1990_russian_rev/ch20_section.md)` |
| `E1-10` | **P2** | `cards/events/EVT-1918-01-constituent-assembly-dispersal.md` | L51, L53, L57, T3 | (a) `pp.89–91` 属 `ch07_3`，T3 仅链 `ch08_4`；(b) 《新生活报》15 死跨至 p.110；(c) 洛佐夫斯基反对在 5 日党团会而非 6 日中执委会 | (a) T3 L88 前补链 `- [ch07_3_gathering_forces](../../sources/monographs/rabinowitch_2007_in_power/ch07_3_gathering_forces.md)`；(b) L53 `Rabinowitch pp.106–109` 改为 `Rabinowitch pp.106–110`；(c) L57 `梁赞诺夫、洛佐夫斯基等反对仍未能阻止。` 改为 `此前5日布党党团会上的梁赞诺夫、洛佐夫斯基反对，以及6日中执委会上梁赞诺夫与左社什泰因贝格的抗议，均未能阻止解散。` |
| `E1-11` | **P1** | `cards/events/EVT-1918-03-brest-litovsk-treaty.md` | L15 (YAML), L43 | 全库事件卡中唯一对改历后日期保留伪构旧历 `end_os: '1918-03-02'` | 删除 YAML L15 `end_os: '1918-03-02'`（保留 `start_os: '1917-12-02'`、`start_ns: '1917-12-15'`、`end_ns: '1918-03-15'`）；将 L43 中 `YAML的end_os＝1918-03-02只是与end_ns＝1918-03-15配对的**推算儒略历坐标**，不是苏俄当时实际行政日期；不得据此把3月15日再加13天。start日期则是实际旧历停战日。` 替换为 `start日期采改历前实际双历（差13日）；苏俄1918-02-14 [N.S.] 改历后行政不再行用儒略历，故YAML结束日期仅列end_ns，不另造推算旧历。` |
| `E1-12` | **P1** | `cards/events/EVT-1918-03-brest-litovsk-treaty.md` | L43 | 正文泄漏内部工作流提示词“现库不存在任务示例所称布列斯特专门DEB文件” | 将 L43 末句 `现库不存在任务示例所称布列斯特专门DEB文件，挂接实存的战时共产主义前夜／左派路线与红色恐怖起源争鸣，前者主题较本事件宽，不能冒称已有同名专卡。` 替换为 `本卡挂接的两项相邻争鸣（战时共产主义起源与红色恐怖起源）覆盖议题宽于布列斯特和约本身，用于承接左翼共产主义者与左社退阁后的路线分歧。` |
| `E1-13` | **P2** | `cards/events/EVT-1918-03-brest-litovsk-treaty.md` | L53, T3 | 苏维埃四大批准日期未注 15 日夜至 16 日跨午夜异记（Carr 记 16 日）；T3 缺 Rabinowitch 原书 `ch11`/`ch12` 链接 | L53 `03-14..16 [N.S.]全俄苏维埃非常四大举行，15日以**784∶261∶115**批准和约。` 替换为 `03-14..16 [N.S.]全俄苏维埃非常四大举行，15日夜至16日凌晨以**784∶261∶115**批准和约（官方决议多署15日，Carr等通史记16日）。`；T3 补链 `rabinowitch_2007_in_power/ch11_6_the_socialist_fatherland_is_in_danger.md` 与 `ch12_7_an_obscene_peace.md` |
| `E1-14` | **P1** | `cards/events/EVT-1918-09-red-terror-and-left-sr-rupture.md` | L36 (`[T1]`) | 将 Rabinowitch 修正解释（“意图逼废和约而非夺取苏维埃政权”）直接作为无争议事实写入 `[T1]` | 将 L36 `[T1]` 替换为（去空白 **123 字**，严格 ≤150）：`1918年7月左翼社革党刺杀米尔巴赫，其意在逼废和约抑或夺权存史学争议，随后遭布党镇压并被逐出苏维埃权力核心。8月30日乌里茨基遇害、列宁遇刺后，9月5日红色恐怖法令将集中营隔离与枪决制度化。一党垄断与暴力升级须分别追踪，登记死亡数非全部受害者。` |
| `E1-15` | **P1** | `cards/events/EVT-1918-09-red-terror-and-left-sr-rupture.md` | L44, L46 | L44 将左社资格审查委质疑的 399 名布党代表简归“Rabinowitch 质疑”；L46 彼得格勒 161 人结案实载于 `p.301`，原页码漏列 | L44 `Rabinowitch（2007，p.288）质疑约399名布党代表资格及构成，属于他的档案重建，不能写成所有研究者公认的造假总数。` 替换为 `开幕初步统计为布党678、左社269、余88（共1,035正式代表）；资格审查委员会左社少数派质疑约399名布党代表资格，Rabinowitch（2007，p.288）佐以莫吉廖夫省档案认为存在有力旁证，同时坦言选举未经独立调查，不能写成公认造假总数。`；L46 `Rabinowitch（pp.294、308–309）` 改为 `Rabinowitch（pp.294、301、308–309）` |
| `E1-16` | **P2** | `cards/events/EVT-1918-09-red-terror-and-left-sr-rupture.md` | L77–79 | Mozokhin 表格漏标原书 `ch05` PDF p.16 明言的“约三年（未完整含 1920 年）”及“17 个地区未经核实”统计边界 | 将 L77 说明栏末尾补 `（原书注1918–1919合计中17地区数据未经核实）`；将 L79 `约1918—1921年有案可查合计` 改为 `约1918—1921年（原书明言系近四年中的约三年统计）有案可查合计`，说明栏补 `未完整覆盖1919后5个月与1920年，且漏计克里米亚、喀琅施塔得等；9,701已在合计范围内，不可重复相加。` |

---

## 五、只读边界声明与六卡 SHA-256 前后复核

本次审计全程未修改任何被审卡片、论断、争鸣、数据表、札记、原书或图谱文件，唯一写入目标为本报告 `audits/AUD-19A-wave54-codex-1917-1918-storm-events-audit.md`。以下为审计开工前与完工后的只读 SHA-256 逐一比对结果：

| 卡片文件 | 开工前 SHA-256 | 完工后 SHA-256 | 一致性 |
| :--- | :--- | :--- | :---: |
| `cards/events/EVT-1917-02-february-revolution.md` | `6f0f10784b21991aa9f08980f4f057d64b10b0629ddceb3ff867c47e61ddb624` | `6f0f10784b21991aa9f08980f4f057d64b10b0629ddceb3ff867c47e61ddb624` | 一致（未修改） |
| `cards/events/EVT-1917-07-july-days.md` | `1b2e124ca915e997435555d84f56e1b13276e43c0904c95039ddc8467b452505` | `1b2e124ca915e997435555d84f56e1b13276e43c0904c95039ddc8467b452505` | 一致（未修改） |
| `cards/events/EVT-1917-10-october-revolution.md` | `3a43699aca6ebe5b25e311c089595a2a6ff40658dc4784db563e4c76fc79181a` | `3a43699aca6ebe5b25e311c089595a2a6ff40658dc4784db563e4c76fc79181a` | 一致（未修改） |
| `cards/events/EVT-1918-01-constituent-assembly-dispersal.md` | `63b536ee9cae122fdf673716b75ba777569698addf8509b53b636073b328cba7` | `63b536ee9cae122fdf673716b75ba777569698addf8509b53b636073b328cba7` | 一致（未修改） |
| `cards/events/EVT-1918-03-brest-litovsk-treaty.md` | `aee9c380e65535d27e6dd6d507a1aeec6dde1f031b5f0b5fe343598cb285f795` | `aee9c380e65535d27e6dd6d507a1aeec6dde1f031b5f0b5fe343598cb285f795` | 一致（未修改） |
| `cards/events/EVT-1918-09-red-terror-and-left-sr-rupture.md` | `3cc3378a559bc9e8504359eb5da1aa2fb314c9b8ed594a10cdb652a7177ba69f` | `3cc3378a559bc9e8504359eb5da1aa2fb314c9b8ed594a10cdb652a7177ba69f` | 一致（未修改） |
