---
id: AUD-22-wave61-codex-cross-family-audit
type: audit
auditor_model: codex/gpt-6.1-sol
target_wave: W61
status: closed
remediated_at: "2026-11-21"
remediation_summary: "All 2 P0 and 13 P1 defects verified against sources/ and remediated 100%; B4B-24 canary promoted to b4b_historiography_1918_1929.jsonl."
updated_at: "2026-11-21"
---

## P0

### P0-01｜将“五年内生产合作化”误写为“一年内合作化／集体化”

**位置**：`reading-notes/kak_lomali_nep_1928_1929_plenums/RN-W61-july1928-april1929-nov1929-stenograms.md:137`。

**原文**：“政府下令一年内将合作化/集体化覆盖率提至 `85%`”。

**证成**：`sources/primary/kak_lomali_nep_1929_v5_ru/ch00_pages_1-25.md:250–255` 明确区分两个期限：要求 **10 月 10 日前制定措施计划**，目标是 **五年内**使不少于 85% 农户实现“生产合作化”，并推动初级生产合作组织转为大型集体农庄。现文同时压缩了实施期限、混同了组织形态。

| 原文本 | 精确替换文本 |
|---|---|
| `1929-06-25 [N.S.]` 政府下令一年内将合作化/集体化覆盖率提至 `85%` | `1929-06-25 [N.S.]` 人民委员会责成国家计委会同合作社与集体农庄运动领导机关，于同年10月10日前制定措施计划，以在五年内使不少于85%的农户实现生产合作化，并推动初级生产合作组织转为大型集体农庄 |

### P0-02｜战时共产主义卡仍保留被原著明确否定的喀琅施塔得口号

**位置**：`cards/policies/POL-war-communism.md:27`。

**原文**：“喀琅施塔得起义呼唤‘没有共产党人的苏维埃’”。

**证成**：`sources/monographs/avrich_1970_kronstadt/ch07_pages_176-200.md:879–888` 明言该口号并非喀琅施塔得口号，水兵没有采用它；同章 `:128–132` 给出的口号是“一切权力归苏维埃，而非政党”。现文亦与本波升级的 `DEB-1921-kronstadt-and-nep-origins.md:19` 冲突。

| 原文本 | 精确替换文本 |
|---|---|
| **喀琅施塔得起义** 呼唤“没有共产党人的苏维埃” | **喀琅施塔得起义**要求自由重选苏维埃，提出“一切权力归苏维埃，而非政党”；Avrich明确指出，“没有共产党人的苏维埃”并非起义者采用的口号 |

## P1

### P1-01｜施略普尼科夫来信日期误认，并压缩了马林诺夫斯基揭露与处决的时序

**位置**：`reading-notes/kak_lomali_nep_1928_1929_plenums/RN-W61-july1928-april1929-nov1929-stenograms.md:106`。

**原文**：“施略普尼科夫 `1929-03-24` 复函”；“1917年革命查明真相枪决马林诺夫斯基后”。

**证成**：

- `sources/primary/kak_lomali_nep_1929_v4_ru/ch06_pages_151-175.md:115–123` 的回信说收到的是布哈林 **3月24日的询问便条**，不能据此给回信定日。
- 同文件 `:151–155` 区分革命后揭露与随后处决；`ch28_pages_701-725.md:368–375` 注释明确处决发生于 **1918年**。

| 原文本 | 精确替换文本 |
|---|---|
| 布哈林调阅列宁研究院档案与施略普尼科夫 `1929-03-24 [N.S.]` 复函 | 布哈林调阅列宁研究院档案，并宣读施略普尼科夫对其1929年3月24日询问便条的回信；此处速记未据该日期确定回信日期 |
| 1917 年革命查明真相枪决马林诺夫斯基后列宁再未重提此语 | 布哈林称，1917年革命后马林诺夫斯基的密探身份得到揭露，此后列宁不再重复这一评价；本卷编者注另明确，马林诺夫斯基于1918年返俄后受审并被处决 |

### P1-02｜Popkins论文仍以Burbank作为作者外键

**位置**：`historiography/claims/CLM-burbank-2000-peasant-volost-courts-code-and-custom.md:4、41`。

**原文**：`scholar: SCH-burbank-jane`；“保留……外键以维护全库学者学派索引稳定”。

**证成**：`sources/articles/burbank_2000_code_versus_custom_volost_court_appeals/ch00_pages_1-17.md:7–15` 明确署名 Gareth Popkins。已有 `SCH-popkins-gareth`，保留既有卡片ID并不要求继续保留错误作者外键。正文说明无法修正结构化查询中的错误归属。

| 原文本 | 精确替换文本 |
|---|---|
| `scholar: SCH-burbank-jane` | `scholar: SCH-popkins-gareth` |
| 本卡保留 `SCH-burbank-jane` 外键以维护全库学者学派索引稳定 | 本卡保留既有卡片ID与馆藏目录名，作者外键指向 `SCH-popkins-gareth`；Jane Burbank列为相关研究脉络，不作为本文作者 |

### P1-03｜Plaggenborg分项合计矛盾未明确标识

**位置**：

- `historiography/claims/CLM-kotsonis-plaggenborg-tsarist-indirect-and-direct-taxation.md:30`
- `reading-notes/late_imperial_fiscal_and_haimson/RN-W61-kotsonis-hoch-plaggenborg-burbank-haimson.md:108、117`

**原文**：“总计 `538.1` 百万卢布”；表内农村 `189.4`、城市工业 `349.7`，仅注“正文总计口径标为538.1”。

**证成**：`sources/articles/plaggenborg_1995_tax_policy_peasant_poverty_1881_1905/ch13_p_65.md:16–29` 分项加总为 **539.1**；`:34–44` 正文却印为 **538.1**。这不是已经证实的“口径差异”，而是原文内部尚待解释的算术不一致。

| 位置／原文本 | 精确替换文本 |
|---|---|
| CLM第30行：“总计 **`538.1` 百万卢布**” | 按表2分项加总为**539.1百万卢布**，作者正文另记538.1百万卢布，两者相差1.0百万；以下保留表列分项，并将35%／65%标为作者的约数 |
| RN第108行：“总计 `538.1` 百万卢布” | 分项复算合计539.1百万卢布；作者正文记538.1百万卢布，原文内部存在未解释的合计差异 |
| RN第117行注释 | 原文正文记538.1百万；本表两栏及各商品分项加总均为539.1百万。差异原因未核明，不另造统计口径解释。 |

### P1-04｜Getzler的概率推算被升级为确定的全舰队统计

**位置**：

- `historiography/claims/CLM-getzler-1983-kronstadt-soviet-democracy-and-1921-veterans.md:19、27、43`
- `reading-notes/kronstadt_and_early_party_state/RN-W61-getzler-holquist-duval-oppenheim-rigby.md:50、157`
- `cards/events/EVT-1921-kronstadt.md:54、88`
- `historiography/debates/DEB-1921-kronstadt-and-nep-origins.md:19`

**原文**：“至少75.5%系1918年前入伍”；“全舰队 `>=75.5%`”。

**证成**：`sources/monographs/getzler_1983_kronstadt/ch08_pages_201-225.md:834–840` 使用 **“are likely to have been”**；`ch11_pages_276-300.md:981–986` 说明相关注释使用出生年份资料推断资历。现有中文删掉了概率模态，不能再称为确定的全舰队入伍年份统计。

| 原文本类型 | 精确替换文本 |
|---|---|
| “至少75.5%系／是在1918年前入伍” | Getzler推测，1921年1月1日服役的波罗的海舰队水兵中，很可能至少75.5%在1918年前入伍 |
| “全舰队 `>=75.5%`” | 全舰队1918年前入伍者比例：Getzler推测很可能至少75.5%，非完整入伍年份名册的直接统计值 |

### P1-05｜对Getzler数字不闭合擅自补造原因

**位置**：

- `historiography/claims/CLM-getzler-1983-kronstadt-soviet-democracy-and-1921-veterans.md:43`
- `reading-notes/kronstadt_and_early_party_state/RN-W61-getzler-holquist-duval-oppenheim-rigby.md:49`

**原文**：“系原统计口径尾差”；“系原档案分年汇总口径微差”。

**证成**：`sources/monographs/getzler_1983_kronstadt/ch08_pages_201-225.md:823–834` 确实同时写出2,028、1,904和137，但没有解释多出的13人；`ch11_pages_276-300.md:979–980` 仅给出Semanov出处。尚未读取其原始分年资料，不能确定是口径重叠、排印错误还是其他原因。

| 原文本 | 精确替换文本 |
|---|---|
| 系原统计口径尾差 | Getzler原文数字内部不闭合，原因尚未核明；不得擅自归因于统计口径或舍入 |
| 系原档案分年汇总口径微差，摘录时须原样保留…… | Getzler所列两个分子合计2,041，比所列分母2,028多13人；现有出处未解释差异。引述须保留原数并标明该矛盾，待核Semanov第66页及其所据资料 |

### P1-06｜四月全会名单被当作逐次投票清点表，旧“300名委员”残留

**位置**：

- `reading-notes/kak_lomali_nep_1928_1929_plenums/RN-W61-july1928-april1929-nov1929-stenograms.md:100`
- `cards/meetings/MTG-1929-04-cc-joint-plenum.md:28、39、46、48`

**原文**：“赞成票约为232票”；“300余名中央与中监委委员”；“300对13……均已核实”。

**证成**：

- `sources/primary/kak_lomali_nep_1929_v4_ru/ch21_pages_526-550.md:104–107` 是全会出席名单汇总：301人，其中中委65、中监委180，合计245名具表决权委员。
- `ch20_pages_501-525.md:1195–1199` 记录反对10、弃权3，主席称出席中委及中监委“约250人”，没有报精确赞成数。
- 301名与会者中包含候补中委和中审委委员，不能全部改称“中央与中监委委员”。

| 原文本 | 精确替换文本 |
|---|---|
| 按245名实到表决权人数计，赞成票约为232票 | 原记录未报精确赞成票数；245为全会出席名单中的具表决权委员总数，不据此反推本次投票的精确赞成数 |
| 第28行“在实到245名表决权委员中以” | 在主席所称“约250名出席中委与中监委委员”中，以 |
| 第39行“中央—中监委联席300余人多数” | 中央—中监委联席全会多数 |
| 第46行“300对13会场对峙” | 全会名单301人、其中245名具表决权委员，以及决议反对10票、弃权3票的记录 |
| 第48行“300余名中央与中监委委员” | 联席全会中的中央委员与中监委委员 |

### P1-07｜十一月全会反推“约60票赞成”，并出现“全体赞成而有反对票”的矛盾措辞

**位置**：

- `historiography/claims/CLM-kak-lomali-nep-1929-v5-nov-plenum-bukharin-expulsion.md:18、28、60`
- `reading-notes/kak_lomali_nep_1928_1929_plenums/RN-W61-july1928-april1929-nov1929-stenograms.md:165、197`
- `cards/meetings/MTG-1929-11-cc-plenum.md:26`
- `timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md:253`

**证成**：`sources/primary/kak_lomali_nep_1929_v5_ru/ch21_pages_526-550.md:397–407、603–608` 明确现场反对2票、无人弃权，布哈林与李可夫缺席，另有布哈林书面意见；没有清点赞成票总数。全会名单中的64名中委不等于闭幕会实际参加该次表决的人数。

| 原文本类型 | 精确替换文本 |
|---|---|
| “全体出席中委赞成、仅2票反对”／“全体赞成、仅2票反对” | 除托姆斯基、乌加罗夫投反对票外，其余现场投票者赞成，无人弃权 |
| 第60行“扣除缺席……赞成票约为60票、反对2票” | 全会名单列64名中央委员，但该名单不是第14次会议的投票清点表；原件仅明确现场反对2票、无人弃权，并记布哈林与李可夫缺席，不据此反推精确赞成票数 |

### P1-08｜把《中央消息报》刊期写成名录训令批准日

**位置**：

- `historiography/claims/CLM-ali-rigby-secretariat-and-1923-nomenklatura-origins.md:31`
- `reading-notes/kronstadt_and_early_party_state/RN-W61-getzler-holquist-duval-oppenheim-rigby.md:144–145`

**原文**：“1926-01-18新训令”；“1926-03-08更将……精确切分”。

**证成**：`sources/articles/rigby_1988_origins_of_nomenklatura_system/ch00_pages_1-16.md:478–508` 仅说1926年初及数周后；`:770、787–789` 的1月18日、3月8日是所引《中央消息报》的期刊日期。注52还说明后一分配修订了1924年底通过的既有分配，不能直接把刊期当作决定日。

| 原文本 | 精确替换文本 |
|---|---|
| `1926-01-18 [N.S.]` 新训令 | 1926年初新训令，其摘要与官方说明刊于1926年1月18日《中央消息报》第1期 |
| `1926-03-08 [N.S.]` 更将核心No.1精确切分为 | 1926年3月8日《中央消息报》第9期刊载的No.1权限分配为 |
| RN第144–145行日期栏 | 分别改为“1926年初训令；摘要刊于1926-01-18”与“权限调整；资料刊于1926-03-08”，不将刊期标作批准日 |

### P1-09｜名录人数的中央管辖范围与No.1汇总范围扩大

**位置**：

- `historiography/claims/CLM-ali-rigby-secretariat-and-1923-nomenklatura-origins.md:30–31`
- `reading-notes/kronstadt_and_early_party_state/RN-W61-getzler-holquist-duval-oppenheim-rigby.md:144`
- `cards/institutions/INS-politburo-orgburo-secretariat.md:47`
- `cards/meetings/MTG-1924-05-13th-party-congress.md:48`
- `historiography/scholars/SCH-rigby-th.md:22`

**证成**：

- `sources/articles/rigby_1988_origins_of_nomenklatura_system/ch00_pages_1-16.md:461–465` 的3,500／1,500后附有“部分情况下属下级党委名录”限定，不能无保留地全部算作中央直接管辖。
- `:478–486` 给出No.1为1,870、No.2为1,640、选任附表1,590及另一附表数百职，随后报相关职位逾5,500；现文把汇总值全部塞入No.1。仅1,870＋1,590＋数百，也不能支持“No.1逾5,500”。

| 原文本类型 | 精确替换文本 |
|---|---|
| 中央No.1约3,500、中央No.2约1,500 | 据十三大报告推算，第1、第2号名录分别涉及约3,500与1,500名国家机关官员；Rigby注明部分情况下属下级党委名录，不能全部视为中央直接管辖 |
| No.1总职位逾5,500／1926年扩至No.1逾5,500职 | Rigby在列举中央第1、第2号名录及附加类别后，报告相关职位总计逾5,500；不得将这一汇总值直接标作No.1单项职数 |

### P1-10｜海姆森争鸣卡混用年度与上半年数据

**位置**：`historiography/debates/DEB-1914-haimson-thesis-stability.md:23`。

**原文**：“1914年上半年1,337,458人（政治罢工占79.2%）”。

**证成**：

- `sources/articles/haimson_1964_social_stability_urban_russia_pt1/ch09_p_627.md:83–87`：年度总行1,337,458，政治项985,655。
- `ch10_p_628.md:14–22`：上半年1,254,441，政治项982,810，且不含华沙省。
- 两组相应比例分别约73.7%和78.3%，均不是79.2%。

| 原文本 | 精确替换文本 |
|---|---|
| 1914年上半年1,337,458人（政治罢工占79.2%） | 1914年上半年1,254,441罢工人次，其中政治罢工982,810人次，约占78.3%，且该统计不含华沙省；同文年度总行另列1,337,458人次、政治罢工985,655人次，不与上半年口径混用 |

### P1-11｜KAPROST综合情景增益被缩写为“不搞集体化”的单项效应

**位置**：

- `historiography/claims/CLM-hunter-szyrmer-1991-kaprost-early-soviet-alternatives.md:19`
- `reading-notes/nep_countryside_and_party_levy/RN-W61-carr-mcdonald-hatch-weissman-hunter-lih.md:110–114、150`
- `cards/policies/POL-first-five-year-plan.md:47`
- `historiography/debates/DEB-1928-bukharin-alternative.md:29`

**证成**：`sources/articles/hunter_szyrmer_1991_testing_early_soviet_economic_alternatives/ch11_p_263.md:44–152` 将人口、城市化、消费、国防、外贸、生产率等参数的单项效果与综合效果分别列出。`:97–100` 显示情景1、3和2、4采用不同的生产率提高假设；`ch10_p_262.md:47–63` 明言这是外生设定的10%／20%生产率改善。29.6%—40.1%是多参数组合结果。

| 位置／原文本 | 精确替换文本 |
|---|---|
| CLM第19行“若保留非集体化个体农业并采取较平缓的工业化节奏” | 在取消集体化、调整人口与城市化参数，并外生提高生产率等联合假设下 |
| RN第110行标题 | 情景1–4的多参数组合结果：包含无集体化、不同人口与城市化路径、外生生产率提高等假设 |
| RN第150行“模型证明不搞集体化与大清洗本可……” | 模型在无集体化及外生生产率提高等组合假设下估算，1941年初固定资本存量可比历史基准高29.6%—40.1%；该区间不是取消集体化的单项净效应 |
| POL第47行“证明若不搞集体化并放缓冲锋节奏” | 在无集体化、较慢城市化及外生生产率提高等组合假设下估算 |
| DEB第29行“模型证无集体化下……” | 模型在包含无集体化的多参数组合假设下，估算1941年初固定资本可高出29.6%—40.1% |

### P1-12｜向Allen追加了未见于其原文的批评，并把模型分歧写成已完成的定量裁决

**位置**：

- `reading-notes/nep_countryside_and_party_levy/RN-W61-carr-mcdonald-hatch-weissman-hunter-lih.md:121`
- `historiography/claims/CLM-hunter-szyrmer-1991-kaprost-early-soviet-alternatives.md:43`

**原文**：Allen指出KAPROST“人为叠加10%—20%外生生产率红利”；据此断言集体化“并非……在纯重工业资本存量上输给温和路径30%—40%”。

**证成**：`sources/monographs/allen_2003_farm_to_factory/ch07_pages_176-200.md:443–473` 提出的可能解释是 **外生迁移率和预定城乡人均消费水平**，没有在该段批评10%—20%生产率参数，并明确说模型复杂、原因并非立即清楚。`:432–442` 的8%是1939年非农资本存量、5%是GDP；不能将其直接当作对1941年资本存量区间的统一口径反证。

**替换矩阵**：

| 位置 | 精确替换文本 |
|---|---|
| RN第121行整段 | **Allen对模型差异的解释**：Allen（2003，pp.166–167）认为，Hunter与Szyrmer模型较负面的集体化评价，可能与外生设定城乡迁移率及预定城乡人均消费水平有关；后一设定使农业减产时资本与劳动转向消费品部门以维持消费。他在此未将10%—20%的生产率参数列为批评对象。Allen自身模型在相同高投资率下，得到1939年集体化情景非农资本存量比延续NEP高8%、GDP高5%的结果。这些结果与KAPROST的1941年资本存量估算存在模型、时点和指标范围差别，应并列呈现，不能直接据此宣布其中一个区间已被定量推翻。 |
| CLM第43行中Allen批评部分 | Allen（2003，pp.166–167）提出，外生迁移率与预定城乡人均消费水平可能解释Hunter—Szyrmer模型较负面的集体化评价；该段没有批评其10%—20%的生产率参数。Allen自己的1939年非农资本存量与GDP比较，亦须同KAPROST的1941年资本存量结果区分指标、时点和模型条件。 |

### P1-13｜把1922年秘密信息机构布设误写为GPU秘密政治局改组

**位置**：`reading-notes/kronstadt_and_early_party_state/RN-W61-getzler-holquist-duval-oppenheim-rigby.md:85`。

**原文**：“1922年重组为GPU秘密政治局信息网”。

**证成**：`sources/articles/holquist_1997_bolshevik_surveillance_pan_european/ch16_p_431.md:40–51` 及 `ch17_p_432.md:21–23` 说的是国家保卫机关被要求在各类机构、企业内设立秘密信息机构。`ch34_p_449.md:30–36` 另将OGPU中央和地方秘密政治部门的设立定在1931年。现文将网络布设指令改写成了特定部门的1922年改组。

| 原文本 | 精确替换文本 |
|---|---|
| 1922 年重组为 GPU 秘密政治局信息网 | 1922年国家保卫机关被要求在国家、社会、合作社及私人机构和企业中设立秘密信息机构；此处不指1931年设立的中央和地方秘密政治部门 |

## B4A／B4B金丝雀题建议

1. **B4A：全会人数与精确赞成票陷阱。** 给出四月全会301人名单、其中65名中委与180名中监委，以及反对10、弃权3；再给出十一月全会64名中委名单、布哈林与李可夫缺席、现场反对2。追问能否认定赞成票分别为232和60。**判分锚点**：不得把全会累计出席名单当作单次投票清点表；保留原件明确记录的反对、弃权及缺席信息。

2. **B4B：Getzler分母、模态与源内矛盾。** 给出2,028、1,904、137及“at least 75.5% are likely…”原文，要求形成中文摘要。**判分锚点**：93.9%限于两舰已知入伍年份样本；75.5%保留推测模态；指出分子合计多13人且原因未明，不编造“舍入尾差”或“档案分年口径微差”。