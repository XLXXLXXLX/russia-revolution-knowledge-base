# 1-Hop 去重平衡上下文包：`EVT-1921-1922-volga-famine-and-church-valuables-crisis`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`EVT-1921-1922-volga-famine-and-church-valuables-crisis`** (伏尔加—乌拉尔饥荒、国际救济与教会珍宝冲突 | `cards/events/EVT-1921-1922-volga-famine-and-church-valuables-crisis.md` | `multi-perspective`): 已覆盖=`provincial-social-history, state-church-conflict, international-relief, political-biographical-loginov`；待补=`verified-national-demographic-estimates, full-confiscation-financial-accounts, primary-text-lenin-1922-03-19-letter`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
内战、征粮与生产运输崩溃叠加1920—1921年歉收旱灾，酿成大饥荒；Figes估全国死亡约500万。ARA与国家救济并行，独立赈济遭压制。1922年征收教会财物引发冲突；列宁3月19日信主张利用饥荒推进没收，其目标是反动神职人员还是教会本身，史家有分歧。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **灾害形成**：Figes 指出伏尔加地区本易歉收，但1920年歉收后又遇1921年严霜与夏旱；真正使危机致命的，是内战期征粮使农民退回自给生产，未留安全储备——1920年伏尔加地区播种面积已较1917年下降四分之一，布尔什维克仍继续征走口粮与种子（ch23 L27–28）。1921年春“四分之一的农民”挨饿。征粮、减种、战争与干旱的相对权重因地区而异，不能归为单一原因。1921年以粮食税替代余粮征集也未能立即解除饥荒。
- **国内与国际救援**：直到 `1921-07` 苏俄政府才公开承认饥荒（Figes ch23 L39）。高尔基 `1921-07-13` 发出呼吁，全俄赈饥委员会（Pomgol）于 `1921-07-21` 成立，被Figes称为共产党统治下“第一个也是最后一个独立的社会团体”，含高尔基、科罗连科、斯坦尼斯拉夫斯基等73名成员，并被配以以加米涅夫为首的12人党团“小组”监督（L44）。胡佛的美国救济署（ARA）提出独立运作、释放美国公民两条件；列宁在 Pomgol 为获取美援之后下令将其关闭，`1921-08-27` 除高尔基、科罗连科外成员遭契卡逮捕，后被流放（L46）。援助与政治控制并存。
- **征用与冲突**：`1922-02-23` 全俄中央执行委员会下令征收教会贵重物品用于救济；牧首季洪 `1922-02-28` 发表呼吁书（Loginov ch08 L844）。舒亚发生流血冲突后，`1922-03-16` 政治局决议“没收工作尚未准备好，至少在有些地方需要推迟”（Loginov ch08 L850）；`1922-03-17` 托洛茨基提出利用神职人员内部分裂的指示草案（L851–856）；`1922-03-19` 列宁致政治局的信称“正是现在、而且只有现在”，应“以最疯狂、最无情的精力”进行没收，以争取农民的同情或至少中立，且不触动牧首本人，须首先没收最富有的大修道院与教堂，对“舒亚的叛乱者”及“最危险的黑色百人团分子”应逮捕、审判并枪决（L857–865，Loginov 引文；原信全文未入库）；`1922-03-20` 政治局否决国家政治保卫局逮捕吉洪的提议，带修改通过托洛茨基草案（L866–867）；`1922-04-12` 政治局表决吸收安东尼主教参加饥民救济工作（L890）。牧首季洪其后遭软禁。

### 2.2 时效关系摘要边表
| 关联节点 | 关系类型 | 有效时段 | 关系实质与依据 |
| :--- | :--- | :--- | :--- |
| `POL-war-communism` | `intensifies_vulnerability` | 1918–1921 | 长期征收消耗储备，旱灾又重创收成；Figes ch23 L27–28；地方征粮差异见罗利编著札记。 |
| `PER-gorky` | `mobilizes_relief` | `1921-07-13` 起 | 高尔基呼吁与参与 Pomgol 的筹建；外国粮药救济（ARA）并存，独立赈济空间遭政权压缩（Figes ch23 L41–46）。 |
| `INS-sovnarkom-and-vtsik` | `confiscates` | `1922-02-23` 起 | 财政救灾理由与对教会机构的强制打击相互交织（全俄中执委法令）。 |
| `INS-politburo-orgburo-secretariat` | `postpones_then_resumes_confiscation` | `1922-03-16` → `03-20` | `03-16` 决议推迟，`03-20` 带修改通过托洛茨基指示草案并否决逮捕吉洪；Loginov ch08 L850–867。 |
| `PER-lenin` | `directs_repression` | `1922-03-19` | 信件主张利用饥荒时机强行没收并处置“反动神职人员”；Loginov 将其限定为对政治对手而非对宗教本身，见 2.3；原信全文未入库。 |
| `PER-trotsky` | `drafts_confiscation_line` | `1922-03-17` → `03-30` | 起草利用“进步神职人员”分化教会的指示，3月30日再函支持国家政治保卫局措施（Loginov ch08 L851–856、L870–871）。 |
| `POL-nep` | `contextualizes` | 1921–1922 | 粮食税取代余粮征集，未能立即消除饥荒。 |

> 节点缺口：Pomgol、ARA、东正教会、牧首季洪、国家政治保卫局（教会案侦办）、莫斯科教会案审判等站内暂无独立卡片，已不以悬空 ID 代替，建议另行新建 ORG/EVT 卡。

### 2.3 史学争鸣光谱
- **灾因**：灾情与大规模国际救助有充分共识；Figes 把征粮造成的“无储备”置于自然灾害之前，强调“一半人祸一半天灾”（ch23 L27）；旱灾、战争遗产、强征政策及行政能力的比例难以用全国单一数据衡量。地方研究能显示征粮和政治暴力的具体机制，但不能自动推算全国总额。
- **教会问题**：站内可核的两种读法并置于 Loginov ch08。其一为“列宁信件显示强烈政治意图”：信中要求趁饥荒“只有现在”最无情推进，并枪决“叛乱者”（L863–865）。其二为 Loginov 的限定性解读：他把该信看作针对“反动神职人员”这一政治力量，批评把此信等同于“摧毁东正教会本身、从肉体上消灭神职人员阶层”的说法为“蓄意的谎言”，并指出1922年3月下旬起列宁已不再直接参与教会事务（L857–862、L889）；他据赫穆尔金对35篇学位论文的统计，认为各地被判最高刑罚者“不到40人”，所谓“一万人”之说是“意识形态神话”（L881–887；波利斯基称8,100人，来源未说明）。Loginov 为立场鲜明的辩护性传记，其“限定性解读”与处决数是该作者的判断，须与独立研究对照。救济财政解释则重视饥荒中筹集外汇与食品的现实需求；二者不互斥：实际财政流向须依赖征收、销售和采购账目检验。
- **外部待核线索**：学界另有政治史论者强调意识形态敌意与国家整体打击教会的计划；该论点**未在站内 Pipes 原文核得**（站内 Pipes 仅在 `ch07_introduction.md` L19 一句提到饥荒夺走“逾五百万”人命），本卡不将其归于任何具名学者，也不将其扩大为已证实的全面灭绝计划。

## 2. 一跳邻域全量微摘要目录 (去重后共 7 个节点，0 截断)
- **`POL-war-communism`**（战时共产主义）: 1918年夏至1921年3月苏维埃经济政策总称：余粮收集制、中小工业国有化、取缔私商、货币贬值与实物配给并举；因内战饥荒与国家能力崩溃而强化，却在1921年喀琅施塔得与坦波夫危机下为新经济政策实物税所取代；其性质是应急、乌托邦跃进还是国家统制传统延续，史家分歧剧烈。 ‖ `←EVT-1921-1922-volga-famine-and-church-valuables-crisis`[intensifies_vulnerability|1918–1921]: 长期征收消耗储备，旱灾又重创收成；Figes ch23 L27–28；地方征粮差异见罗利…
- **`PER-gorky`**（马克西姆·高尔基）: 俄国及苏联著名作家、政论家（1868—1936）。1905—1907年力助布尔什维克筹款，1908—1910年赞助卡普里党校并倡“造神说”。1917—1918年主编《新生活报》撰《不合时宜的思想》痛斥街头暴力与专政，内战期营救学者；1921年赴欧，1928—1932年归苏并背书斯大林体制。 ‖ `←EVT-1921-1922-volga-famine-and-church-valuables-crisis`[mobilizes_relief|1921-07-13 起]: 高尔基呼吁与参与 Pomgol 的筹建；外国粮药救济（ARA）并存，独立赈济空间遭政权压… ； `→EVT-1921-1922-volga-famine-and-church-valuables-crisis`[relief-initiator|1921.07–1922]: 向国际社会发出饥荒求援呼吁并筹建民间赈济委员会（Pomgol），因当局解散独立赈济组织而深感羞辱遂赴欧流寓
- **`INS-sovnarkom-and-vtsik`**（人民委员会与全俄、全苏中央执行委员会）: 苏维埃代表大会闭会期间，中执委在宪制上监督政府，人民委员会却迅速掌握施政与大量法令制定。苏俄与1922年成立的苏联各有中执委与人民委员会，不能混同。党内领导与国家机关关系不断变化，政治局权重日增，但1920年代仍须经政府落实决策。 ‖ `←EVT-1921-1922-volga-famine-and-church-valuables-crisis`[confiscates|1922-02-23 起]: 财政救灾理由与对教会机构的强制打击相互交织（全俄中执委法令）。
- **`INS-politburo-orgburo-secretariat`**（联共（布）中央政治局—组织局—书记处与官职等级名册制）: 1919年3月俄共八大后常设政治局、组织局与书记处，分掌政治决策、组织行政及日常党务人事。1922年4月斯大林任总书记后逐步控制议程、秘密文件分发与干部名册调配。经1924年七人小组协调、1925—1929年联盟重组与纪律整肃，托洛茨基、季诺维也夫、布哈林先后退出决策核心。 ‖ `←EVT-1921-1922-volga-famine-and-church-valuables-crisis`[postpones_then_resumes_confiscation|1922-03-16 → 03-20]: 03-16 决议推迟，03-20 带修改通过托洛茨基指示草案并否决逮捕吉洪；Logino…
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←EVT-1921-1922-volga-famine-and-church-valuables-crisis`[directs_repression|1922-03-19]: 信件主张利用饥荒时机强行没收并处置“反动神职人员”；Loginov 将其限定为对政治对手…
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←EVT-1921-1922-volga-famine-and-church-valuables-crisis`[drafts_confiscation_line|1922-03-17 → 03-30]: 起草利用“进步神职人员”分化教会的指示，3月30日再函支持国家政治保卫局措施（Login…
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←EVT-1921-1922-volga-famine-and-church-valuables-crisis`[contextualizes|1921–1922]: 粮食税取代余粮征集，未能立即消除饥荒。

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 2 项)
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

### `DEB-1921-kronstadt-and-nep-origins`：喀琅施塔得起义与新经济政策的双轨转折
## [T1] 核心问题定义
喀琅施塔得是白卫阴谋、农民反抗，还是要求重建劳动者苏维埃民主的革命者起义？1921年实物税与禁止党内派别同期出现，如何解释经济退却和政治收紧的联系、彼此差异及长期后果？

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 社会史与反阴谋论 | Paul Avrich, *Kronstadt, 1921* (1970) | 水兵构成有变化但老兵仍领导起义；诉求为去除单党垄断的多左翼劳动者苏维埃，证据不支持流亡白卫事先操纵，也未提出米留可夫伪造的“不要共产党人的苏维埃”口号。 | `CLM-avrich-1970-sailor-social-composition`; `CLM-avrich-1970-soviets-without-bolsheviks`; `CLM-avrich-1970-white-plot-refutation` | 起义者内部差异及后苏联解密海军档案仍需补充。 |
| 党内组织史与国家—社会契约论 | Robert V. Daniels (1960); Lewis Siegelbaum (1992) | 十大《关于党的统一》（含秘密第7条）构成布尔什维克组织史决定性转折；1921年新政实质是“放开经济市民社会空间，同时彻底封闭党内外政治异议空间”。 | `CLM-daniels-1960-tenth-congress-turning-point`; `CLM-siegelbaum-1992-nep-fragile-social-compromise`; `CLM-carr-1952-nep-retreat-and-commanding-heights` | 党内规则与宏观契约仍需结合外省微距失控过程。 |
| 农村反征粮战争与外省地方史 | Orlando Figes (1996); Donald J. Raleigh (2001) | 1920—1921年坦波夫、西西伯利亚农村战争与萨拉托夫“地方喀琅施塔得”工潮早于水兵起义撼动政权根基，迫使列宁在2月上旬先行酝酿粮食税退却。 | `CLM-figes-1996-peasant-wars-and-nep-retreat`; `CLM-raleigh-2001-center-periphery-weak-state-nep` | 农民起义口号不可无差别套用于喀琅施塔得水兵。 |
| 苏维埃官方／布尔什维克当事人 | 1921年政府通告与十大材料 | 指称白卫反革命及冰融后外国干涉风险，主张铁血镇压与党内绝对统一；属当时政权危机认知与宣传，非已证实的事前阴谋事实。 | `CLM-avrich-1970-white-plot-refutation` | 混淆事后白卫侨民募款企图与水兵起义真实起源。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 19/19 条)
- **`CLM-carr-1952-war-communism-internal-contradictions`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 70-120 (Chs. 17–18)]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 56–58, 69, 185–188, 217–218, 283–284]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-smith-sa-1983-from-workers-control-to-nationalization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 155–156, 166–169, 177–179, 184–186, 192（即源文件标注 PDF pp. 160–161, 171–174, 182–184, 189–191, 197）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-daniels-1960-left-communists-1918`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 70-81]: Daniels：1918年左翼捍卫革命纲领，却在分裂关头受党统一约束
- **`CLM-figes-1996-peasant-wars-and-nep-retreat`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 775-785]: 
- **`CLM-zemskov-1929-dekulakization-demographic-baseline`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | PDF pp. 6-11, 15-19, 52, 218 (原书 pp. 4-9, 13-17, 50, 216)]: 
- **`CLM-avrich-1970-sailor-social-composition`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 101-105]: 
- **`CLM-avrich-1970-soviets-without-bolsheviks`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 198-201, 179-180]: 
- **`CLM-avrich-1970-white-plot-refutation`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 143-147, 816-818]: 
- **`CLM-daniels-1960-tenth-congress-turning-point`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 146-153]: Daniels：1921年十大将党统一转化为压缩合法反对空间的组织制度
- **`CLM-siegelbaum-1992-nep-fragile-social-compromise`** [`SCH-siegelbaum-lewis`(刘易斯·H·西格尔鲍姆) | pp. 84, 91-93, 102-117, 136-144, 180-186 (PDF pp. 98, 105-107, 116-131, 150-158, 194-200)]: 
- **`CLM-carr-1952-nep-retreat-and-commanding-heights`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 118-166 (Chs. 18–20)]: 
- **`CLM-raleigh-2001-center-periphery-weak-state-nep`** [`SCH-raleigh-donald`(唐纳德·J·罗利) | Local PDF pp. 16–18, 139–173; English print pagination not verified]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
