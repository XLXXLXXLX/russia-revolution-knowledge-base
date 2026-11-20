# 1-Hop 去重平衡上下文包：`MTG-1917-04-7th-april-party-conference`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`MTG-1917-04-7th-april-party-conference`** (俄国社会民主工党（布尔什维克）第七次全国代表会议（四月会议） | `cards/meetings/MTG-1917-04-7th-april-party-conference.md` | `multi-perspective`): 已覆盖=`april-theses-primary, intraparty-pluralism, loginov-minutes-based, trotsky-haimson-lenin-dominance, pipes-sukhanov-lenin-centered, rabinowitch-party-pluralism`；待补=`post-soviet-minutes-based, conference-proceedings-independent-verification, nationality-debate-specialist`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1917-04-24至04-29[O.S.]/05-07至05-12[N.S.]，布尔什维克四月会议以71:39:8通过列宁当前形势决议，拒绝信任临时政府，支持土地国有化与苏维埃夺权；但民族自决、中央规模及齐美尔瓦尔德会议问题上列宁遭多数反对，党内分歧鲜明。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **会议背景：四月危机与临时政府**：会议开幕（`04-24 [O.S.] / 05-07 [N.S.]`）距米留可夫照会引发的“四月危机”（`04-18—04-21 [O.S.]`）仅 3 日；站内 L3 记列宁在会上斥彼得格勒委员会左翼 21 日“打倒临时政府”传单为冒险主义，并自称“和平侦察”（`timeline/L3_daily/1917-04_lenin_arrival_april_theses_and_milyukov_note.md` L264–281）。《四月提纲》要求不支持临时政府，争取从革命第一阶段转向第二阶段；加米涅夫则强调民主革命尚未完成，主张对临时政府实行监督。会议结束时的投票：列宁《关于当前形势》决议 **71 赞成、39 反对、8 弃权**（Loginov ch10 L376–378）；针对临时政府态度的决议**仅 3 票反对、8 人弃权**，加米涅夫的“监督”方案被否决（ch10 L93–95）；加米涅夫自认与列宁仅在监督问题上有分歧（L75–83）。该路线不能等同于会议已决定立即武装夺权。
- **土地与政权**：会议支持没收地主土地及土地国有化，并主张全部政权转归苏维埃。列宁同时强调向工兵群众耐心解释、争取多数（决议写入“极其需要谨慎和小心”）；《四月提纲》第8条明确不把当前任务称为立即实施社会主义。
- **民族自决**：列宁维护民族分离自决权；皮达可夫（代表部分民族地区党组织作补充报告）、捷尔任斯基、马哈拉泽反对该立场，认为其与无产阶级国际主义及集中的革命战略相冲突。对列宁决议草案的投票：**56 赞成、16 反对、18 弃权**（Loginov ch10 L65–74）。承认分离权不等于主张所有民族必须分离。
- **国际问题：列宁在齐美尔瓦尔德问题上败北**：Loginov 记列宁坚决反对俄社民工党参加有欧洲“中派”参与的齐美尔瓦尔德派国际会议，**但代表们不接受其论据，决议以全票反对（仅列宁一人赞成）通过**（ch10 L59–64）；L3 称之为 `1:8` 孤立（L280）。这一反例说明会议并非“投票机器”；它与列宁另行主张创立新国际属于不同议题。个别发言与速记原文仍待核。
- **中央机构**：4月29日 [O.S.] 在 109 名代表的无记名投票中选出九人中央委员会（Loginov ch10 L575–582）：列宁 104 票、季诺维也夫 101、斯大林 97、加米涅夫 95、米柳京 82、诺根 76、斯维尔德洛夫 71、斯米尔加 53、费奥多罗夫 48；候补委员首二位费奥多罗维奇 41 票、布勃诺夫 32 票。列宁曾提议将中央委员会由 9 人增至 13 人，多数代表投票反对（L522–524）；九人中央仍留有四名温和派（L3 L280）。什利亚普尼科夫、莫洛托夫等原俄国局成员未达候选票数（L584–586）。
- **规模**：约 8 万党员、152 名代表（Loginov ch09 part_3 L590）；与二月时相比党员增长两倍。代表数 152 大于各项投票的 118（71+39+8）和 109（中央选举）张票，不得把任何一项票数直接当作全体代表数。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `POL-april-theses-1917` | `debates_and_develops` | 1917年春 | 会议围绕提纲的政府、土地和政权方向讨论并形成决议，不等于照单逐条通过全文。 | 《四月提纲》；当前形势决议 71:39:8（Loginov ch10 L376–378） |
| `PER-lenin` | `advocates` | 1917年春 | 反对信任临时政府并主张争取苏维埃多数；在齐美尔瓦尔德参加问题（1:8）、民族自决（56:16:18）和中央扩员（9→13）上被多数否决或反对。 | Loginov ch10 L59–74、L522–524 |
| `PER-kamenev` | `contests` | 1917年春 | 主张对临时政府实行监督；监督方案被否，加米涅夫自认与列宁仅此一处分歧；仍以 95 票当选中央委员。 | Loginov ch10 L75–95、L575–582 |
| `CON-dual-power` | `responds_to` | 1917年春 | 以转移政权的主张回应临时政府与苏维埃并存。 | 《四月提纲》 |
| `ORG-bolsheviks-rcpb-vkpb` | `elects_leadership` | 1917年春 | 在公开的内部路线分歧中，以 109 人无记名投票选举九人中央委员会。 | Loginov ch10 L575–582；L3 L264、L280 |

### 2.3 史学争鸣光谱
**文本事实**：列宁提纲否定支持临时政府，主张向苏维埃政权过渡，并拒绝把立即实施社会主义当成直接任务。**解释分歧**（站内 L3 L280 已建五派对照，可对读）：
- **Trotsky / Haimson（列宁主导论）**：Trotsky（`trotsky_1930_history_rr_zh` ch17）强调列宁以超凡意志压倒党内温和派；Haimson 2005 把会议置于列宁—加米涅夫—李可夫的理论对峙中（`CLM-haimson-2005-lenin-wartime-to-april-1917-theoretical-leap`）。
- **Loginov（会议记录为据的多元论）**：以会议记录反驳“投票机器”——齐美尔瓦尔德 1:8、民族自决 56:16:18、中央扩员遭否决、中央仍有温和派（`CLM-loginov-lenin-vs-party-moderates-1917`，ch10 L59–95）。
- **Rabinowitch（党组织多元并行）**：强调彼得格勒委员会（PK）、中央委员会与军事组织并行及自主，四月危机中 PK 左翼与中央的张力（站内 [`rabinowitch_1968_prelude_zh/ch04_2斗争开始.md`](../../sources/monographs/rabinowitch_1968_prelude_zh/ch04_2斗争开始.md)；`CLM-rabinowitch-1976-open-democratic-mass-party` 关注1917年全年，不可直接推定为四月会议每项投票的证据）。
- **Pipes / Sukhanov（列宁中心论）**：Pipes 把四月危机中的“和平侦察”视为未遂的政变试探（`CLM-pipes-1990-october-classic-coup`）；Sukhanov 以当事人观察把列宁描绘为布尔什维克的精神中心，离开列宁则失魂（`sources/monographs/sukhanov_1922_personal_record`）。
- **缺口**：后苏联档案速记对勘的独立研究（`post-soviet-minutes-based`）。

不应把支持主要路线误作所有细节一致。

## 2. 一跳邻域全量微摘要目录 (去重后共 5 个节点，0 截断)
- **`POL-april-theses-1917`**（《四月提纲：论无产阶级在这次革命中的任务》）: 1917年4月列宁归国后提出的十项纲领：宣布不给临时政府任何支持、批判“革命护国主义”、主张从资产阶级革命第一阶段向工兵苏维埃掌权第二阶段过渡，并倡议没收地主土地实现全部土地国有化、全国银行合并受苏维埃监督与更改党名；打破加米涅夫—斯大林有条件支持临时政府路线，经党内激烈辩论逐步重塑布尔什维克战略。 ‖ `←MTG-1917-04-7th-april-party-conference`[debates_and_develops|1917年春]: 会议围绕提纲的政府、土地和政权方向讨论并形成决议，不等于照单逐条通过全文。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←MTG-1917-04-7th-april-party-conference`[advocates|1917年春]: 反对信任临时政府并主张争取苏维埃多数；在齐美尔瓦尔德参加问题（1:8）、民族自决（56:…
- **`PER-kamenev`**（列夫·加米涅夫）: 老布尔什维克、首任全俄中执委主席。1917年自四月至立宪会议一贯坚守温和宪政社会主义联盟路线并公开反对十月起义；1924年十三大联手季诺维也夫压下《列宁遗嘱》，1925年十四大公开发言反斯大林“领袖”集权后失势；1928年7月密会布哈林并留下外泄笔记，反成右派致命罪证。 ‖ `←MTG-1917-04-7th-april-party-conference`[contests|1917年春]: 主张对临时政府实行监督；监督方案被否，加米涅夫自认与列宁仅此一处分歧；仍以 95 票当选…
- **`CON-dual-power`**（双重政权（两个政权并存））: 萌芽于1905年苏维埃；1917-03-02[O.S.]/03-15[N.S.]至七月事件，临时政府名义主权与彼得格勒苏维埃工兵实力、“有条件支持”并存。列宁四月称两类阶级专政交织，七月宣布终结，九月再提苏维埃夺权；修正史学强调多中心失序与双方虚弱。 ‖ `←MTG-1917-04-7th-april-party-conference`[responds_to|1917年春]: 以转移政权的主张回应临时政府与苏维埃并存。
- **`ORG-bolsheviks-rcpb-vkpb`**（布尔什维克派—俄共（布）—联共（布））: 布尔什维克起于1903年社民工党二大后的党内多数派，经流亡、地下活动与1917年群众扩张成为执政党；1918年称俄共（布），1925年称联共（布）。它从地方主动性较强的革命党，演变为拥有任命网络与纪律制裁的党国核心，过程分阶段且存争议。 ‖ `←MTG-1917-04-7th-april-party-conference`[elects_leadership|1917年春]: 在公开的内部路线分歧中，以 109 人无记名投票选举九人中央委员会。 ； `→MTG-1917-04-7th-april-party-conference`[party-conference|1917-04]: 代表约8万党员的口径，路线转向后的党内讨论

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 2 项)
### `DEB-1917-dual-power-and-february-origins`：二月革命起源与“双重政权”宪制形成之争（1917）
## [T1] 核心问题定义
二月革命是无领导的群众爆发，还是工厂与兵营中分散的积极分子推动的起义？沙皇退位后，杜马临时委员会、苏维埃与临时政府如何谈判并形成彼此制约的权力格局？群众压力、精英选择和战时危机的因果权重仍有争议，不能以宫廷阴谋代替街头革命。

## [T2] 各学派立场对照矩阵
**经验基准**：1917-02-23 [O.S.] / 1917-03-08 [N.S.] 国际妇女节罢工扩大；27日 [O.S.] / 3月12日 [N.S.] 首都预备营哗变，国家杜马临时委员会与彼得格勒工兵代表苏维埃在塔夫利达宫东西两翼同日成立；3月1日 [O.S.] / 3月14日 [N.S.] 苏维埃发布《第一号命令》；3月2日 [O.S.] / 3月15日 [N.S.] 尼古拉二世在普斯科夫退位并传位米哈伊尔大公；3月3日 [O.S.] / 3月16日 [N.S.] 米哈伊尔大公签署《拒绝即位宣言》（将最高政权形制交由普选立宪会议决定并呼吁服从临时政府），同日临时政府举行首次内阁会议。各机构的正式法统主张与实际暴力和行政控制力并不重合。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 社会史、次精英网络与2018年宪制自我修正 | Tsuyoshi Hasegawa, *The February Revolution: Petrograd, 1917* (1981; rev. ed. 2018) | 街头起义既非纯粹盲目自发也非布尔什维克中央指挥，而是跨党派工厂与兵营“中下层积极分子（sub-elite activists）”在各党上层犹豫时串联引爆；2018年新版更推翻自己1981年“杜马自由派系不情愿革命者”旧论，证明杜马临时委员会先于苏维埃建立军事委员会、于2月27日晚11:30主动夺权，且“双重政权”并非苏维埃自愿让权（苏维埃并无国家行政机器可让），而是米留可夫在3月3日首次内阁会议上蓄意废黜国家杜马、自断民选法统后，反使强势临时政府沦为需仰赖虚弱苏维埃合法性的无根政权。 | `CLM-hasegawa-2018-sub-elite-activists`；`CLM-hasegawa-2018-duma-committee-revision`；`CLM-hasegawa-2018-dual-power-origins` | 高度聚焦首都彼得格勒五日决战，对外省政权接收与农村公社反应需结合地方档案补充。 |
| 自由派困境与“叹着气的革命者” | Fedor Gaida, *Liberal Opposition in Russia, 1914–1917* (2003) | 与Hasegawa 2018年版针锋相对：论证杜马自由派缺乏基层组织，在二月并非胸有成竹的主动夺权者，而是因畏惧沙皇军法审判与街头暴民清洗才仓促接权的“叹着气的革命者／革命的俘虏”；二月获胜的不是作为立宪机构的第四届杜马，而是作为群众集会物理场所的塔夫利达宫，这一事实同样从档案层面直接证伪了“自由派预先策划二月革命”的阴谋论。 | `CLM-gaida-2003-liberals-in-february-1917` | 偏重杜马自由派上层书信与内阁心态，不能单独解释2月27日驻军哗变的兵营微观动因。 |
| 当事人夜间妥协见证（B级文献） | N. N. Sukhanov, *The Russian Revolution, 1917* (1922) | 以苏维埃执委会亲历者视角记录3月1–2日夜与米留可夫、古契科夫的谈判：苏维埃多数派因惧怕“资产阶级退缩导致军事反革命镇压”，以“不入阁、有条件支持、保留士兵控制权”达成双重政权契约。 | `CLM-sukhanov-1922-dual-power-pact` | 属B级当事人回忆录，兼具在场见证与孟什维克国际派事后自我辩护，须与双方会议速记互证。 |
| 革命马克思主义阶级主权论（B级文献） | Leon Trotsky, *History of the Russian Revolution* (1930–32) | 将双重政权界定为一切伟大革命中“两个不可调和统治阶级（资产阶级与无产阶级/兵农）分掌正式政权与实际武装”的过渡性主权分裂，断言其内在结构不稳定性必然通向十月二次革命或反革命专政。 | `CLM-trotsky-1930-dual-power-instability` | 属B级十月领导人事后理论化，将二月的多党协商张力嵌入通向十月布尔什维克夺权的目的论轨道。 |
| 孟什维克“革命护国主义”与联合政府陷阱 | Ziva Galili, *The Menshevik Leaders in the Russian Revolution* (1989) | 第二章从粮食与铁路技术依赖、对失控“士兵革命”的疑虑及工人反专政心理正面解释3月初双重政权的诞生；随后以“革命护国主义”和5月入阁解释苏维埃社会权威与联合政府行政责任之间的致命撕裂。 | `CLM-galili-1989-revolutionary-defensism`；`CLM-galili-1989-coalition-government-trap` | 5月以后的联合政府危机属双重政权中后期演变，应与2月底3月初的政权创生机制分段考察。 |
| 精英宫廷阴谋论及其社会史反证 | 叶夫根尼·斯皮岑（E. Yu. Spitsyn）《俄罗斯帝国与苏联通史》第3卷（B级新传统主义综合）；Orlando Figes, *A People's Tragedy* (1996) | 斯皮岑渲染军方高层、杜马自由派与协约国驻俄使团的“精英倒沙皇阴谋”；Figes（注：所引论断卡主论3月《第一号命令》后至10月的军纪瓦解、社会等级逆转与“战壕布尔什维主义”）与Hasegawa、Fedor Gaida共同证明基层士兵拒绝向人群开火及社会反威权爆发具有完全独立于精英接触的动力。 | `CLM-spitsyn-february-1917-elite-conspiracy-thesis`；`CLM-figes-1996-soldier-mutiny-and-social-inversion` | 上层倒沙皇接触或普斯科夫劝退绝不等于指挥2月23–27日街头罢工与预备营哗变；混淆精英善后与起义命令链违反证据等级铁律。 |

### `DEB-1917-october-coup-or-social-revolution`：十月革命：少数派政变还是社会革命？
## [T1] 核心问题定义
十月武装夺权是少数派政变，还是工人、士兵与农民社会革命的政治表达？有组织的起义与广泛的基层动员能否同时成立，苏维埃多数又能否代表全国选民？这些问题涉及不同地区、不同时间的支持与合法性，不能以一次投票或一次攻占行动互相替代。

## [T2] 各学派立场对照矩阵
**经验基准**：彼得格勒苏维埃军事革命委员会组织行动，临时政府于1917-10-25 [O.S.] / 1917-11-07 [N.S.] 被推翻；第二次全俄工兵代表苏维埃代表大会当晚开幕，孟什维克与右派社革党抗议退场，大会于10月26日 [O.S.] / 11月8日 [N.S.] 通过《和平法令》《土地法令》并组建人民委员会。据站内选举统计（`DATA-01-1905-1917-strikes-and-petrograd-elections`、`DATA-07-1905-1918-unions-moscow-swings-and-constituent-assembly-votes`），布尔什维克在1917年9月莫斯科区杜马获51.5%选票、11月全俄立宪会议选举在大城市与北/西前线占优，但在全国立宪会议总票中仅占约22.5%–24%（社革党各单合占约37%–40%，且选票名册未反映10月左翼社革党独立分党）。苏维埃代表、立宪会议选民与农村夺地农民并非同一政治总体。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 自由主义“静默技术性政变”论 | Richard Pipes, *The Russian Revolution* (1990) | 援引马拉帕尔泰“静默技术性政变”概念，断言十月并非群众起义，而是列宁与军革委利用临时政府权威真空发动的少数派武装夺权，且本质上是**“针对全国苏维埃组织本身的政变”**——抢在苏维埃二大开幕前推翻临时政府，将全国苏维埃代表置于既成事实之下。 | `CLM-pipes-1990-october-classic-coup` | 将工人赤卫队与驻军顺从简化为阴谋家操纵，难以解释布尔什维克在9–11月两都市/区杜马及北方前线选票中的真实多数。 |
| 开放性群众政党与托洛茨基苏维埃合法性策略 | Alexander Rabinowitch, *The Bolsheviks Come to Power* (1976) | 1917年的彼得格勒布尔什维克并非铁板一块的密谋集团，而是吸收数万工人兵士、容忍加米涅夫—季诺维也夫公开异议的开放性群众政党；夺权成功关键在于**托洛茨基策略**——以彼得格勒苏维埃军革委“保卫苏维埃与卫戍部队”为名实施防御性展开，并将政权移交严格锚定于第二次全俄苏维埃代表大会开幕，以赢得无党派工兵的苏维埃合法性认同。 | `CLM-rabinowitch-1976-open-democratic-mass-party`；`CLM-rabinowitch-1976-october-three-factions-debate`；`CLM-rabinowitch-1976-trotsky-soviet-congress-strategy` | 首都党组织的战前民主开放性与苏维埃防卫策略，不能自动推及外省夺权或10月底维克热尔谈判破裂后的一党专政化。 |
| 列宁“稍纵即逝窗口”与先行夺权论（与托洛茨基路线之张力） | Vladlen T. Loginov, *Lenin in 1917: On the Brink of the Possible* (2017) | 与拉比诺维奇聚焦托洛茨基“等待并依托苏维埃二大”形成直接张力：洛吉诺夫论证列宁之所以痛斥“等待苏维埃代表大会是白痴行为或背叛、拖延就是死亡”，是因为洞察到10月中旬无政府浪潮与军事反革命夹击下存在“稍纵即逝的夺权窗口”，唯有在大会开幕前先行武装夺权、造成既成事实，才能迫使动摇的苏维埃大会接管政权。 | `CLM-loginov-lenin-1917-fleeting-window-of-power` | 高度认同列宁对紧急时机的政治直觉，但恰恰从反面印证了“先行夺权把苏维埃二大置于既成事实”的程序正当性争议。 |
| 工厂控制与莫斯科“政策先于党派”社会史 | S. A. Smith, *Red Petrograd* (1983); Diane P. Koenker, *Moscow Workers and the 1917 Revolution* (1981) | S. A. Smith证明彼得格勒工厂委员会推行“工人监督”最初是防止企业主关厂与经济崩溃的防御性自救，而非按意识形态蓝图消灭资本主义；Koenker证明莫斯科十月经历了与彼得格勒截然不同的惨烈炮战，且莫斯科多数工人虽在原则上拥护苏维埃政权，却**拒绝为党派垄断冒内战风险**（支持多党社会主义联合），其激进化遵循**“政策先于党派（policy before party）”**的理性渐进机制。 | `CLM-smith-sa-1983-defensive-workers-control`；`CLM-koenker-1981-moscow-october-armed-struggle-vs-petrograd`；`CLM-koenker-1981-rational-incremental-radicalization` | 两都工业工人的防御性/理性选择不能代表占人口八成的农村公社或边疆民族地区。 |
| 维克热尔妥协流产与立宪会议合法性冲突 | John D. Basil, *The Mensheviks in the Revolution of 1917* (1984); 姚海（主编）《俄国革命史》(2013); Alexander Rabinowitch, *The Bolsheviks in Power* (2007) | Basil与姚海剖析十月后全俄铁道工会（维克热尔）调停与清一色社会主义联合政府谈判：孟什维克内部分裂与10月29–30日士官生暴动撕裂妥协，布尔什维克中央内部加米涅夫、季诺维也夫、李可夫、诺金等辞职警告“纯布尔什维克政府只能靠政治恐怖维持”；姚海与Rabinowitch (2007) 进一步揭示苏维埃阶级专政逻辑与普选立宪会议（1918年1月5–6日被武力解散）之间不可调和的二元合法性冲突。 | `CLM-basil-1984-october-and-vikzhel-collapse`；`CLM-yao-hai-post-october-coalition-failure-and-one-party-formation`；`CLM-yao-hai-constituent-assembly-vs-soviet-legitimacy-clash`；`CLM-rabinowitch-2007-constituent-assembly` | 维克热尔谈判与立宪会议解散解释了十月向一党制滑落的制度拐点，但不能反过来否定10月25日临时政府已彻底丧失首都工兵支持的事实。 |
| 当事人革命解释与反对派在场反证（B级文献） | [B级当事人文献] Leon Trotsky, *History of the Russian Revolution* (1930–32); N. N. Sukhanov, *The Russian Revolution, 1917* (1922) | 托洛茨基将起义定性为“在苏维埃合法性掩护下实施的武装夺权艺术”；**苏汉诺夫的证言尤具史学张力**——他虽作为孟什维克国际派痛斥布尔什维克政权缺乏民主准备、悔恨温和派10月25日夜退场将苏维埃拱手让给列宁，却**以亲历反对者身份断然驳斥右翼“纯军事阴谋”说**，证言彼得格勒工人与驻军当时确以压倒性多数支持推翻临时政府。 | `CLM-trotsky-1930-art-of-insurrection-and-soviet-legality`；`CLM-sukhanov-1922-october-walkout-tragedy` | 两者均属B级当事人回忆与事后政治辩护（托洛茨基旨在反击斯大林并凸显自身军革委功绩，苏汉诺夫旨在检讨国际派失策），必须与当时会议速记对读。 |
| 农民道德经济、帝国边疆与十月记忆建构 | Orlando Figes (1996); Ronald Grigor Suny (2017); Eric Blanc (2021); Frederick C. Corney, *Telling October* (2004) | Figes揭示农民公社夺地遵循自身“道德经济”，利用《土地法令》将既成黑分土地合法化而非服从城市党令；Suny综合社会史与阶级话语极化；Blanc将1917年十月放入帝国边疆民族与阶级互动视野；Corney则考证党史委（Istpart）与1920年代庆典如何将原本混乱多中心的十月夺权事后重塑为宏大叙事神话。 | `CLM-figes-1996-peasant-moral-economy-1917`；`CLM-suny-2017-totalitarian-vs-social-history-turn`；`CLM-suny-2017-class-discourse-and-polarization`；`CLM-blanc-2021-borderlands-in-1905-and-1917`；`CLM-corney-2004-istpart-and-institutionalizing-october-memory` | 农民夺地与边疆动员支持推翻旧政权，但并不等于授权布尔什维克随后的余粮收集制与一党垄断；记忆建构研究不可消解1917年秋真实的社会崩溃。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/31 条)
- **`CLM-haimson-2005-lenin-wartime-to-april-1917-theoretical-leap`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. 27-38 [PDF pp. 61-72]; pp. 245-247 [PDF pp. 279-281]]: 
- **`CLM-loginov-lenin-vs-party-moderates-1917`** [`SCH-loginov-vladlen`(弗拉德连·洛吉诺夫) | pp. 145-146, 165-167, 265, 272-273, 340-343, 527-528]: 
- **`CLM-rabinowitch-1976-open-democratic-mass-party`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-hasegawa-2018-sub-elite-activists`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. 643–645 (PDF pp. 664–666); cf. pp. 203–204, 218 (PDF pp. 224–225, 239)]: 
- **`CLM-hasegawa-2018-duma-committee-revision`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. xiii–xiv (PDF pp. 14–15); pp. 366–368, 377–378 (PDF pp. 387–389, 398–399); p. 652 (PDF p. 673)]: 
- **`CLM-hasegawa-2018-dual-power-origins`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. 626–638 (PDF pp. 647–659); cf. pp. 649, 660 (PDF pp. 670, 681)]: 
- **`CLM-gaida-2003-liberals-in-february-1917`** [`SCH-gaida-fedor`(费奥多尔·盖达) | pp. 355-356, 433-439]: 
- **`CLM-sukhanov-1922-dual-power-pact`** [`SCH-sukhanov-nikolai`(尼古拉·苏汉诺夫) | pp. 117–126, 150, 153–158 (PDF pp. 163–172, 196, 199–204); cf. pp. 68, 104–108, 113–114]: 
- **`CLM-trotsky-1930-dual-power-instability`** [`SCH-trotsky-leon`(列夫·达维多维奇·托洛茨基 · participant-historian) | （中译 EPUB 无纸页；第一卷第十一、十六章）]: 
- **`CLM-galili-1989-revolutionary-defensism`** [`SCH-galili-ziva`(齐娃·加利利) | pp. 134-140, 148-151 (PDF pp. 152-158, 174-177)]: 
- **`CLM-galili-1989-coalition-government-trap`** [`SCH-galili-ziva`(齐娃·加利利) | pp. 169-170, 177-181 (PDF pp. 195-196, 203-207)]: 
- **`CLM-spitsyn-february-1917-elite-conspiracy-thesis`** [`SCH-spitsyn-yevgeny`(叶夫根尼·斯皮岑) | PDF pp. 11–15, 24, 28]: 
- **`CLM-figes-1996-soldier-mutiny-and-social-inversion`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 404-412]: 
- **`CLM-rabinowitch-1976-october-three-factions-debate`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-rabinowitch-1976-trotsky-soviet-congress-strategy`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-loginov-lenin-1917-fleeting-window-of-power`** [`SCH-loginov-vladlen`(弗拉德连·洛吉诺夫) | pp. 523-524, 531-532, 560-561, 621-622, 656-658]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-koenker-1981-moscow-october-armed-struggle-vs-petrograd`** [`SCH-koenker-diane`(黛安·P·科恩克尔) | pp. 329–355 (local PDF pp. 345–371); p. 366 (PDF p. 382)]: 
- **`CLM-koenker-1981-rational-incremental-radicalization`** [`SCH-koenker-diane`(黛安·P·科恩克尔) | pp. 359–363 (local PDF pp. 375–379); p. 254 (PDF p. 270)]: 
- **`CLM-basil-1984-october-and-vikzhel-collapse`** [`SCH-basil-john`(约翰·D·巴兹尔) | pp. 165–175（本地 PDF 同号）]: 
- **`CLM-yao-hai-post-october-coalition-failure-and-one-party-formation`** [`SCH-yao-hai`(姚海) | [PDF pp. 532-535, 543-569]]: 
- **`CLM-yao-hai-constituent-assembly-vs-soviet-legitimacy-clash`** [`SCH-yao-hai`(姚海) | [PDF pp. 574-596]]: 
- **`CLM-rabinowitch-2007-constituent-assembly`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 88-91, 105-110, 121-127]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 2 条 L3 逐日细节见 `timeline/L3_daily/`)
