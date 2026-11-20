# 1-Hop 去重平衡上下文包：`ORG-democratic-centralists`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`ORG-democratic-centralists`** (民主集中派 | `cards/organizations/ORG-democratic-centralists.md` | `multi-perspective`): 已覆盖=`opposition-history-daniels, political-economy-carr, party-leadership-primary-documents`；待补=`fifteen-platform-original-full-text, regional-opposition-archives, levy-soviet-democracy-comparison`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
民主集中派是1919年初结成的布尔什维克党内反对派，萨普罗诺夫、奥新斯基、弗·斯米尔诺夫等为重要代表，批评以任命和行政命令取代集体领导与基层参与。成员及立场随时间变化：1923年部分人联署《四十六人声明》；后期“十五人集团”须与早期派别区分。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **1918年前史与1919年形成**：奥新斯基同为1918年左派共产主义者（`ORG-left-communists-1918`），反官僚议题有所承袭，但后者组织实体已非同一派别。1919年初，奥新斯基、萨普罗诺夫、弗·米·斯米尔诺夫、马克西莫夫斯基结成民主集中派（`PER-osinsky`；`PER-sapronov`；Daniels 1960, p. 95）。1919年八大上的军事反对派与组织问题争论见 `MTG-1919-03-8th-party-congress`。批评者反对以少数人任命取代党内选举、合议与地方苏维埃的实质权力，并非反对一切集中，而是要求民主讨论、集体领导与统一执行结合（`CON-democratic-centralism-and-vanguard`）。不能假设每人在1919–1927年始终同派。
- **九大与十大（1920–1921）**：1920年一长制、劳动军事化、地方自主和委员会权力成为焦点。1920年11月莫斯科省代表会议选举中，工人反对派、民主集中派（萨普罗诺夫）与伊格纳托夫集团合计124席，对中央委员会支持者的154席；1921年1月莫斯科基层代表投票中萨普罗诺夫得7票（列宁57票、托洛茨基20票），见 `ORG-workers-opposition`（Daniels pp. 138–140 / PDF pp. 156–158）。1921-03-16十大通过《关于党的统一》（`WEB-1921-03-16-on-party-unity`；`POL-ban-on-factions-1921`；`MTG-1921-rcpb-10th-congress`），限制有组织派别。各代表的具体主张并不一致，不能把九大后的完整集团纲领倒投到1919年八大。
- **与工人反对派的异同**：两者都批评官僚主义和要求扩大基层参与，但工人反对派提出以产业工会和生产者代表大会掌管国民经济；民主集中派重点是党、苏维埃与行政机关的集体领导与选举责任，而非简单主张由工会取代国家经济机关（`ORG-workers-opposition`；Daniels, *The Conscience of the Revolution*）。其社会基础和政策意见亦非铁板一块。
- **1923年到1927年**：`1923-10-15 [N.S.]` 《四十六人声明》（`WEB-1923-10-15-declaration-of-the-forty-six`，S 级，中俄英三版）的签署者包含民主集中派人士及其他反对派人士，批评经济管理与党内官僚化；声明既非民主集中派独自提出，也不等于后来的联合反对派（`CLM-carr-1954-platform-of-46-economic-roots`；`ORG-left-and-united-opposition`）。1926–1927年萨普罗诺夫、弗·斯米尔诺夫所属的“十五人集团”（`PER-sapronov`）进一步认为苏维埃政权与党已失去无产阶级专政实质，与托洛茨基等联合反对派的判断不能简单混同。库内 `WEB-1927-09-platform-joint-opposition` 的 `edition_note` 把《15人政纲》系于 `1927-06-27` 并视为联合反对派9月政纲的前序；它与萨普罗诺夫—斯米尔诺夫集团是同一文件、同一群体还是名称巧合，库内尚无结论，故此处不对该集团起止年份和文本归属作断言。1927年十五大扩大开除反对派，库内 L3 记 `1927-12-18 [N.S.]`（`MTG-1927-12-15th-party-congress`；`timeline/L3_daily/1927-10_tenth_anniversary_and_15th_congress.md`）；具体成员的开除时间与处置范围仍须逐人核对，不能推断所有早期民主集中派成员处分相同。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 关系实质 | 依据 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-bolsheviks-rcpb-vkpb` | `internal-opposition-to-apparatus` | 1919–1927 | 争取党和苏维埃机关的集体领导，后与中央公开决裂 | `PER-sapronov`；`PER-osinsky` |
| `PER-sapronov` | `core-leader` | 1919–1927 | 民主集中派核心人物，1921年1月莫斯科基层投票7票，后属“十五人集团” | Daniels 1960 pp. 95、116、138、140 |
| `PER-osinsky` | `core-theorist` | 1919–1921 | 八大组织问题主发言人，1923年联署四十六人声明 | Daniels 1960 p. 95；`PER-osinsky` 卡 |
| `ORG-left-communists-1918` | `partial-antecedent` | 1918–1919 | 奥新斯基同为左派共产主义者，议题有承袭，组织实体已非同一 | `ORG-left-communists-1918` 卡；`CLM-daniels-1960-left-communists-1918` |
| `ORG-workers-opposition` | `parallel-critics-with-distinct-program` | 1920–1921 | 共同反官僚化，但经济管理方案有别；1920-11莫斯科三派共124席对154席 | Daniels pp. 138–140（经 `ORG-workers-opposition`） |
| `MTG-1919-03-8th-party-congress` | `party-congress-debate` | 1919-03 | 组织问题与军事反对派争论 | `PER-osinsky` 卡；`MTG-1919-03-8th-party-congress` 卡 |
| `MTG-1921-rcpb-10th-congress` | `subject-to-congress-resolution` | 1921-03 | 十大统一决议限制有组织派别 | `WEB-1921-03-16-on-party-unity` |
| `POL-ban-on-factions-1921` | `subject-to-disciplinary-rule` | 1921起 | 统一决议要求解散派别，限制持续组织活动 | `WEB-1921-03-16-on-party-unity`；`RN-W1C-communist-oppositions-1918-1929`（仅对禁派别规则成立，不含民主集中派本体） |
| `CLM-carr-1954-platform-of-46-economic-roots` | `partial-signatory-overlap` | 1923 | 四十六人跨越不同党内反对派，以经济与组织问题联合 | Carr 1954；`WEB-1923-10-15-declaration-of-the-forty-six` |
| `ORG-left-and-united-opposition` | `distinct-oppositions` | 1926–1927 | 判断政权性质与托洛茨基等联合反对派不同 | `WEB-1927-09-platform-joint-opposition`（身份待核） |
| `MTG-1927-12-15th-party-congress` | `expulsion-context` | 1927-12 | 十五大扩大开除反对派 | L3 `1927-10_tenth_anniversary_and_15th_congress`（`1927-12-18 [N.S.]`） |
| `CON-democratic-centralism-and-vanguard` | `conceptual-framework` | 1919–1927 | 要求集体领导与统一执行结合的概念背景 | `CON-democratic-centralism-and-vanguard` 卡 |

### 2.3 史学争鸣光谱
Daniels 强调党内反对派对革命民主理想的持续申诉与1921年统一规则的制度后果；其对 DC 本体的具体依据库内由 `PER-sapronov`、`PER-osinsky` 与 `ORG-workers-opposition` 经 Daniels 页码承载，`RN-W1C-communist-oppositions-1918-1929` 札记只涉及工人反对派、禁派别与新经济政策路线。党领导层一侧的论证以原典为准：《关于党的统一》与列宁1918年5月文本（`sources/web-archive/W32_milestone_docs/1918-05_lenin-left-wing-childishness-state-capitalism.md`）体现党领导层对集中管理、纪律与专家一长制的辩护立场，但库内无对 DC 的逐条回应。卡尔对1923年声明的经济背景提醒我们，党内民主诉求和工业、信贷危机密切交织。对1926–1927年激进化，需将反对派对政权性质的判断作为政治诊断，而非未经检验的社会事实；后来史家的“热月”类比（`CON-thermidor-and-bureaucracy`）与 Levy 的苏维埃民主解释（`CLM-levy-1987-makhaevism-intelligentsia-new-class-critique`；`CLM-soviet-democracy-1924-1927-ozhivlenie-sovetov-paradox`）可作对读，库内尚未逐页对勘。

## 2. 一跳邻域全量微摘要目录 (去重后共 11 个节点，0 截断)
- **`MTG-1919-03-8th-party-congress`**（俄国共产党（布尔什维克）第八次代表大会）: 1919年3月18日至23日，俄共（布）八大在内战中通过第二党纲，围绕民族自决、红军正规化与党内集中化激烈争辩，提出巩固与中农的联盟。大会及会后一中全会确立政治局、组织局和书记处常设框架，否定党组织联邦制并强化党团对苏维埃的控制；军事反对派与民主集中派的抗辩凸显集权并非无争议。 ‖ `→ORG-democratic-centralists`[opposition-origin|1919-03]: 奥新斯基、萨普罗诺夫在八大对党内集中化与官僚化的批评构成该派直接源头。 ； `←ORG-democratic-centralists`[party-congress-debate|1919-03]: 组织问题与军事反对派争论
- **`MTG-1921-rcpb-10th-congress`**（俄国共产党（布尔什维克）第十次代表大会）: 1921年3月8日至16日，俄共（布）十大在经济崩溃与喀琅施塔得起义交织下召开。大会决定以粮食税取代余粮收集制，开启新经济政策转向；同时终结工会大辩论，通过《关于党的统一》禁止派别活动并谴责工人反对派。经济退却与党内纪律收紧并行，会后中央与书记处改组重塑了组织权力格局。 ‖ `→ORG-democratic-centralists`[constrained|1921-03]: 虽强调党内民主与集体原则，仍被全面纳入禁派纪律红线约束之下。 ； `←ORG-democratic-centralists`[subject-to-congress-resolution|1921-03]: 十大统一决议限制有组织派别
- **`ORG-bolsheviks-rcpb-vkpb`**（布尔什维克派—俄共（布）—联共（布））: 布尔什维克起于1903年社民工党二大后的党内多数派，经流亡、地下活动与1917年群众扩张成为执政党；1918年称俄共（布），1925年称联共（布）。它从地方主动性较强的革命党，演变为拥有任命网络与纪律制裁的党国核心，过程分阶段且存争议。 ‖ `→ORG-democratic-centralists`[internal-opposition|1919–1927]: 集团反对党政任命和官僚化，后遭纪律制裁 ； `←ORG-democratic-centralists`[internal-opposition-to-apparatus|1919–1927]: 争取党和苏维埃机关的集体领导，后与中央公开决裂
- **`PER-sapronov`**（季莫费·萨普罗诺夫）: 油漆工人出身的老布尔什维克，1918–1919年任莫斯科省苏维埃执委会主席，民主集中派组织领袖。八大至十大批判垂直委派制把党员变为“顺从的留声机”；1923年签署《四十六人声明》，1926–1927年组十五人集团，称苏联蜕变为国家资本主义专政，十五大遭开除。 ‖ `←ORG-democratic-centralists`[core-leader|1919–1927]: 民主集中派核心人物，1921年1月莫斯科基层投票7票，后属“十五人集团”
- **`PER-osinsky`**（瓦列里安·奥博连斯基（N·奥新斯基））: 奥辛斯基为布尔什维克经济学家、最高国民经济委员会首任主席（1917.12–1918.03），左派共产主义者及民主集中派理论家。反对布列斯特和约、专家一长制与党机关官僚集中；1923年联署《四十六人声明》，1926–1928年掌中央统计局，因坚持客观粮食统计、抵制政治干预遭免职。 ‖ `←ORG-democratic-centralists`[core-theorist|1919–1921]: 八大组织问题主发言人，1923年联署四十六人声明
- **`ORG-left-communists-1918`**（1918年左翼共产主义者）: 1918年初俄共（布）内以布哈林、奥新斯基、拉狄克、普列奥布拉任斯基为首的极左集团，借《共产党人》（`Коммунист`）杂志反对《布列斯特和约》与列宁“国家资本主义”一长制；俄共七大批准和约后作为有组织派别逐步消解，但其国际主义与反官僚化诉求深刻塑造此后党内反对派谱系。 ‖ `←ORG-democratic-centralists`[partial-antecedent|1918–1919]: 奥新斯基同为左派共产主义者，议题有承袭，组织实体已非同一
- **`ORG-workers-opposition`**（工人反对派）: 俄共（布）党内以产业工人和工会干部为主体的左翼反对派（1920–1922），由什利亚普尼科夫、梅德韦杰夫及理论代言人柯伦泰领导。在1920–1921年工会争论中痛斥党政官僚化与专家“一长制”，主张由“全俄生产者代表大会”及工会自治管理国民经济；1921年十大被定性为无政府工团主义倾向并遭解散。 ‖ `←ORG-democratic-centralists`[parallel-critics-with-distinct-program|1920–1921]: 共同反官僚化，但经济管理方案有别；1920-11莫斯科三派共124席对154席
- **`POL-ban-on-factions-1921`**（《关于党的统一》派别禁令）: 俄共十大于1921年3月16日通过《关于党的统一》，要求解散按纲领组成的派别，并保留规定渠道的批评。秘密第七条设中央领导成员的特殊处分程序；1924年1月公开宣读、1926年7月首次动用开除季诺维也夫出政治局，危机措置遂渐成约束反对派的工具，但不同年份执行不等同原条文。 ‖ `←ORG-democratic-centralists`[subject-to-disciplinary-rule|1921起]: 统一决议要求解散派别，限制持续组织活动 ； `→ORG-democratic-centralists`[并列受禁派别|1921起]: 因主张集体领导与反对委派制而在十大大体失去合法平台。
- **`ORG-left-and-united-opposition`**（1923–1927年左翼反对派与托季联合反对派）: 1923年剪刀差危机触发的托洛茨基—普列奥布拉任斯基“左翼反对派”，经1926年春与季诺维也夫—加米涅夫“新反对派”结盟为托季联合反对派；以《四十六人声明》与《1927年政纲》批判官僚体制与“一国社会主义”、主张价格—财政渠道的计划工业化，于1927年12月十五大被组织摧毁。 ‖ `←ORG-democratic-centralists`[distinct-oppositions|1926–1927]: 判断政权性质与托洛茨基等联合反对派不同
- **`MTG-1927-12-15th-party-congress`**（联共（布）第十五次代表大会）: 1927年12月2—19日莫斯科举行。大会追认11月对托洛茨基、季诺维也夫的开除党籍处分，并于12月18日另行开除加米涅夫等75名托季联合反对派骨干及萨普罗诺夫派；同时通过编制首个五年计划指示与渐进合作化—集体化决议，开启NEP末期转折前奏。 ‖ `←ORG-democratic-centralists`[expulsion-context|1927-12]: 十五大扩大开除反对派
- **`CON-democratic-centralism-and-vanguard`**（先锋队党与民主集中制）: 布尔什维克组织原则的跨期复合概念：从民意党集中制与特卡乔夫“自觉少数”，经1902年职业革命家论、1905–1906年成文的民主集中制及1917年群众政党，至1921年禁派令与斯大林书记处官职名册制，派别空间收缩；部分制度史研究强调干部任命权日益压过民主原则。 ‖ `←ORG-democratic-centralists`[conceptual-framework|1919–1927]: 要求集体领导与统一执行结合的概念背景

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 1 项)
### `DEB-1918-war-communism-ideology-or-emergency`：战时共产主义与早期一党制本质之争：内战应急、乌托邦跃进还是国家统制连续？
## [T1] 核心问题定义
1918至1921年的全面国有化、余粮收集制、取缔私商、劳动军事化，以及多党苏维埃收为一党专政，究竟是内战与供给崩溃逼出的生存应急，还是反市场乌托邦的激进兑现，抑或一战以来国家统制与基层危机交互的结果？“战时共产主义”是1921年转向时的事后标签，须分清措施序列与事后总结。

## [T2] 各学派立场对照矩阵

**经验共识**：1917年底至1918年春尚存布尔什维克—左翼社革党联合执政与“国家资本主义”探索；1918年夏起全面国有化与强制征粮随内战升级扩展；1920年达至劳动军事化与无货币幻想顶峰；1921年3月俄共十大在农村起义与喀琅施塔得危机下转向实物税（NEP）与党内派别禁令。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **内战军事应急与双元矛盾论** | E. H. Carr, *The Bolshevik Revolution*, Vol. 2 (1952); Evan Mawdsley, *The Russian Civil War* (1987) | 强调工业瓦解、封锁与300万红军补给迫使政权诉诸垂直“总局主义”与强制征粮；但Carr同时指出1920年后期确曾滋生把战时自然经济奉为直接通往共产主义捷径的意识形态幻象。 | `CLM-carr-1952-war-communism-internal-contradictions`; `CLM-mawdsley-1987-civil-war-militarized-regime`; `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` | 单靠军事紧急状态难以完全解释1920年底内战大局已定后为何仍出台小手工业全面国有化令。 |
| **意识形态乌托邦与废法专政论** | Martin Malia, *The Soviet Tragedy* (1994); Richard Pipes, *The Russian Revolution* (1990) | 认为消灭私有产权与市场交换本就是马克思主义核心诉求，内战只是扫除了渐进障碍、催化乌托邦跃进；Pipes强调契卡与排斥反对派早于大规模内战爆发。 | `CLM-pipes-1990-red-terror-leninist-logic`; `CLM-pipes-1990-october-classic-coup` | 易将不同阶段的应急妥协（如1918春列宁国家资本主义方案）回溯拉平为单一既定时间表。 |
| **战时国家统制连续与自下而上倒逼论** | Lars T. Lih; S. A. Smith, *Red Petrograd* (1983); David Hoffmann (2011) | 揭示沙皇与临时政府在一战中已启动粮食专卖与国家统制；Smith证明1917–1918春77%早期企业没收源自基层工厂委员会应对关厂危机的自下而上压力，而非中央乌托邦指令。 | `CLM-smith-sa-1983-defensive-workers-control`; `CLM-smith-sa-1983-from-workers-control-to-nationalization`; `CLM-hoffmann-2011-continuum-of-total-war-1914-1929` | 总体战技术连续性不能替代对布尔什维克消灭整个有产阶级政治权利之独特意识形态动力的解释。 |
| **复合危机、党内张力与农村社会钳制论** | Alexander Rabinowitch (2007); Robert V. Daniels (1960); Moshe Lewin (1968/1985) | 追踪布列斯特和约、左翼社革党决裂及左翼共产主义者/工人反对派论战如何一步步锁死多党与党内多元空间，同时揭示小农汪洋的反抗最终迫使政权在1921年退却但保留了战时强制记忆。 | `CLM-rabinowitch-2007-contingency-of-dictatorship`; `CLM-daniels-1960-left-communists-1918`; `CLM-figes-1996-peasant-wars-and-nep-retreat`; `CLM-zemskov-1929-dekulakization-demographic-baseline` | 首都与萨拉托夫、坦波夫、乌拉尔等外省的时间差与暴力烈度须结合地方档案（Raleigh、Churakov）细化。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 17/17 条)
- **`CLM-carr-1954-platform-of-46-economic-roots`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 113-115, 374-375]: 
- **`CLM-daniels-1960-left-communists-1918`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 70-81]: Daniels：1918年左翼捍卫革命纲领，却在分裂关头受党统一约束
- **`CLM-levy-1987-makhaevism-intelligentsia-new-class-critique`** [`SCH-levy-carl`(卡尔·利维) | pp. 17, 113-114, 220, 239-241, 273-275]: 
- **`CLM-soviet-democracy-1924-1927-ozhivlenie-sovetov-paradox`** [`SCH-kubi-michael`(米夏埃尔·库比) | PDF pp. 31-37, 53-55, 127-128, 156-157]: 
- **`CLM-carr-1950-politburo-orgburo-displacement-of-state-organs`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | [PDF pp. 96, 100-105, 109-114]]: 
- **`CLM-daniels-1960-tenth-congress-turning-point`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 146-153]: Daniels：1921年十大将党统一转化为压缩合法反对空间的组织制度
- **`CLM-carr-1952-war-communism-internal-contradictions`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 70-120 (Chs. 17–18)]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 56–58, 69, 185–188, 217–218, 283–284]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-smith-sa-1983-from-workers-control-to-nationalization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 155–156, 166–169, 177–179, 184–186, 192（即源文件标注 PDF pp. 160–161, 171–174, 182–184, 189–191, 197）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-figes-1996-peasant-wars-and-nep-retreat`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 775-785]: 
- **`CLM-zemskov-1929-dekulakization-demographic-baseline`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | PDF pp. 6-11, 15-19, 52, 218 (原书 pp. 4-9, 13-17, 50, 216)]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
