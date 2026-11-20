# 1-Hop 去重平衡上下文包：`POL-ban-on-factions-1921`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`POL-ban-on-factions-1921`** (《关于党的统一》派别禁令 | `cards/policies/POL-ban-on-factions-1921.md` | `multi-perspective`): 已覆盖=`primary-text, kollontai-opposition, daniels-organizational, khlevniuk-institutional, apalkov-leadership, goldman-anti-teleological`；待补=`regional-implementation, individual-case-primary-records`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 150字定性微摘要
俄共十大于1921年3月16日通过《关于党的统一》，要求解散按纲领组成的派别，并保留规定渠道的批评。秘密第七条设中央领导成员的特殊处分程序；1924年1月公开宣读、1926年7月首次动用开除季诺维也夫出政治局，危机措置遂渐成约束反对派的工具，但不同年份执行不等同原条文。

## [T2] 核心脉络与史学争鸣
### 2.1 决议条文与历史演进
- **危机背景与公开条款（1921-03-16）**：工会争论、经济崩溃及喀琅施塔得起义构成 1921 年 3 月俄共（布）十大的紧迫背景（694 名有表决权代表中，工会决议以 `336:50:18` 通过，反对《关于党的统一》仅 `<30` 票，详参 `DATA-04-party-membership-and-congress-votes-1903-1929`）。3 月 16 日通过本第 1—6 条公开，第 6 条命令立即解散一切按特定纲领建立的派别，否则开除出党；决议同时允许在党刊或《争论专页》等指定渠道展开批评，不能把该决议等同于此后一切意见分歧在法律上自动归罪。
- **秘密第 7 条的精确程序**：第 7 条当时保密。它授权中央在破坏纪律或恢复/容忍派别活动时施行处分；针对**中央委员、候补中央委员及中央监察委员会委员**的极端处分（将中央委员降为候补乃至开除出党），须召开中央委员会全会并邀请全体候补中央委员与中央监察委员会委员参加，以**联席全会三分之二多数**决定。适用对象与联席表决门槛须严格界定，列宁虽称希望无需动用该条，却坚持将其作为威慑后盾保留。
- **从“反派别纪律”到 1926-07-23 首次正式动用第 7 条**：1922 年十一大与《四十六人声明》（1923-10-15）、托洛茨基《新方针》（1923-12-08）显示党内围绕“指定制”与经济危机的冲突持续升级。**1924-01-17** 十三次党代表会议上斯大林公开宣读秘密第 7 条（**不同于 1924 年 5 月召开的俄共（布）十三大**）。至 1923—1927 年多数派虽频繁以一般反派别纪律打击反对派，却并非每次都正式启动第 7 条联席程序；历史上**第一次正式援引秘密第 7 条**的制度分水岭，发生在 **1926-07-23 中央与中监委联席全会**：多数派借“拉舍维奇林中密会事件”正式援引第 7 条，将 **`PER-zinoviev`** 逐出政治局并将拉舍维奇开除出中央委员会，此后更以此套程序进一步清剿 1927 年联合反对派。

### 2.2 核心关系网络（结构化边表）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | 起草与报告人 | 1921.03 | 起草《关于党的统一》及秘密第7条并作大会总结报告。 | `CLM-daniels-1960-tenth-congress-turning-point` |
| `MTG-1921-rcpb-10th-congress` | 通过场合 | 1921-03-16 | 大会以压倒多数通过公开条款与秘密第7条，同步开启NEP。 | `CLM-daniels-1960-tenth-congress-turning-point` |
| `EVT-1921-kronstadt` | 危机催化剂 | 1921.03 | 起义震撼催化代表大会迅速收紧党内派别活动空间。 | `DEB-1921-trade-union-controversy-and-party-unity` |
| `POL-nep` | 双轨耦合 | 1921–1929 | 经济退却与政治收紧并行的十大“双轨结构”制度前提。 | `CLM-daniels-1960-tenth-congress-turning-point` |
| `ORG-workers-opposition` | 首要直接对象 | 1920–1922 | 草案直接点名批评的对象，其纲领与独立活动空间被取缔。 | `CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists` |
| `ORG-democratic-centralists` | 并列受禁派别 | 1921起 | 因主张集体领导与反对委派制而在十大大体失去合法平台。 | `RN-W1C-communist-oppositions-1918-1929` |
| `MTG-1922-03-11th-party-congress` | 后续纪律升级 | 1922.03 | 审查工人反对派“二十二人声明”，持续重划派别纪律边界。 | `RN-W1C-communist-oppositions-1918-1929` |
| `ORG-left-and-united-opposition` | 制度约束对象 | 1923–1927 | 左翼与联合反对派的申诉和联合在反派别框架下被定性违纪。 | `CLM-apalkov-2023-collective-to-personal-dictatorship` |
| `PER-zinoviev` | 首例第7条靶标 | 1926-07-23 | 1926年7月联席全会首次正式援引秘密第7条将其逐出政治局。 | `CLM-apalkov-2023-collective-to-personal-dictatorship` |
| `PER-stalin` | 制度运用者 | 1923–1927 | 借助书记处任命制与反派别武器逐步瓦解各级反对派联盟。 | `CLM-khlevniuk-2015-secretariat-and-nomenklatura` |
| `INS-politburo-orgburo-secretariat` | 执行中枢 | 1921–1929 | 书记处与中监委协同把应急条款转化为常态化干部筛查杠杆。 | `CLM-khlevniuk-2015-collective-leadership-erosion` |
| `CON-democratic-centralism-and-vanguard` | 学理母概念 | 1921–1929 | 从列宁式民主集中制内部张力向高度集权纪律化的制度拐点。 | `CLM-daniels-1960-tenth-congress-turning-point` |
| `DEB-1921-trade-union-controversy-and-party-unity` | 核心争鸣 | 1920–1922 | 工会争论、喀琅施塔得危机与派别禁令起源的因果定位。 | `CLM-daniels-1960-tenth-congress-turning-point` |
| `DEB-1928-bukharin-alternative` | 延展争鸣 | 1923–1929 | 禁令与官僚机构如何锁死1920年代党内路线替代空间。 | `CLM-khlevniuk-2015-defeat-of-right-opposition` |

### 2.3 史学争鸣
- **组织转折 vs. 机构演进**：R. V. Daniels（1960）将十大视为布尔什维克组织史的关键转折点，同时指出列宁在 1921 年仍拒绝完全禁止按纲领竞选代表（`CLM-daniels-1960-tenth-congress-turning-point`）；Oleg Khlevniuk（2015）侧重书记处人事任免权、名录制度与集体领导的渐进侵蚀（`CLM-khlevniuk-2015-secretariat-and-nomenklatura`、`CLM-khlevniuk-2015-collective-leadership-erosion`、`CLM-khlevniuk-2015-defeat-of-right-opposition`）；D. I. Apalkov（2023）借助中央全会与政治局斗争规则剖析集体领导向个人独裁的转化（`CLM-apalkov-2023-collective-to-personal-dictatorship`）。
- **反对派文本与反目的论边界**：对照柯伦泰（S 级，`CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists`）、《四十六人声明》（`CLM-carr-1954-platform-of-46-economic-roots`）与 1927 年联合反对派政纲可见，早期反对派自身亦难以突破“党垄断合法性”前提。Wendy Goldman（2011，`CLM-goldman-2011-1920s-oppositions-to-enemy-category`）进一步作出关键反目的论区分：1920 年代依托派别禁令与审查的党内纪律处分（purge），与 1936—1937 年将政治异议抽空为“人民公敌”（vrag naroda）并实施肉体消灭的致命大恐怖之间存在结构性跃迁，不能把 1921 年第 7 条视作自动滑向 1937 年的宿命起点。

## 2. 一跳邻域全量微摘要目录 (去重后共 18 个节点，0 截断)
- **`CON-democratic-centralism-and-vanguard`**（先锋队党与民主集中制）: 布尔什维克组织原则的跨期复合概念：从民意党集中制与特卡乔夫“自觉少数”，经1902年职业革命家论、1905–1906年成文的民主集中制及1917年群众政党，至1921年禁派令与斯大林书记处官职名册制，派别空间收缩；部分制度史研究强调干部任命权日益压过民主原则。 ‖ `→POL-ban-on-factions-1921`[emergency-measure -> permanent-weapon|1921-03–1929]: 被设计为危机时期的“临时”纪律，1923–1929年成为排斥党内反对派的重要纪律工具 ； `←POL-ban-on-factions-1921`[学理母概念|1921–1929]: 从列宁式民主集中制内部张力向高度集权纪律化的制度拐点。
- **`CON-workers-control`**（工人监督（工厂委员会与生产者自治））: 工人监督源自1905年车间行动；1917年彼得格勒工厂委员会为保就业、维持生产实行防御性监督，十月后写入《工人监督条例》。1918年起经济崩溃与国有化推动部分委员会并入工会，中央管理与劳动纪律强化；1921年生产者自治方案遭党内否决，但基层实践与合议管理并未骤然消失。 ‖ `→POL-ban-on-factions-1921`[organizationally-foreclosed-by|1921-03-16起]: 派别禁令切断了党内工人民主派合法结社呼吁车间自治的制度通道
- **`EVT-1921-kronstadt`**（喀琅施塔得水兵起义）: 1921年二月底至三月，喀琅施塔得水兵与居民以十五条决议要求改选苏维埃、开放劳动者及左翼政治自由，并成立临时革命委员会。红军跨冰夺回要塞，镇压与实物税、禁派决议交叠；经济退却早已酝酿，起义加剧其紧迫性，却未带来政治权力的开放。 ‖ `→POL-ban-on-factions-1921`[political_closure|1921.03.16起]: 危机背景下限制党内组织化异议，未给予水兵的多左翼苏维埃方案合法空间 ； `←POL-ban-on-factions-1921`[危机催化剂|1921.03]: 起义震撼催化代表大会迅速收紧党内派别活动空间。
- **`INS-politburo-orgburo-secretariat`**（联共（布）中央政治局—组织局—书记处与官职等级名册制）: 1919年3月俄共八大后常设政治局、组织局与书记处，分掌政治决策、组织行政及日常党务人事。1922年4月斯大林任总书记后逐步控制议程、秘密文件分发与干部名册调配。经1924年七人小组协调、1925—1929年联盟重组与纪律整肃，托洛茨基、季诺维也夫、布哈林先后退出决策核心。 ‖ `→POL-ban-on-factions-1921`[constitutional_weapon|1921.03–1929.12]: 十大《关于党的统一》第7条赋予中央全会（含全体候补中委与全体中监委委员）三分之二多数处分并开除中委的法定武器 ； `←POL-ban-on-factions-1921`[执行中枢|1921–1929]: 书记处与中监委协同把应急条款转化为常态化干部筛查杠杆。
- **`MTG-1921-rcpb-10th-congress`**（俄国共产党（布尔什维克）第十次代表大会）: 1921年3月8日至16日，俄共（布）十大在经济崩溃与喀琅施塔得起义交织下召开。大会决定以粮食税取代余粮收集制，开启新经济政策转向；同时终结工会大辩论，通过《关于党的统一》禁止派别活动并谴责工人反对派。经济退却与党内纪律收紧并行，会后中央与书记处改组重塑了组织权力格局。 ‖ `→POL-ban-on-factions-1921`[resolution|1921-03-16]: 以不足30张反对票通过《关于党的统一》，内含秘而不宣的第7条三分之二除名机制。 ； `←POL-ban-on-factions-1921`[通过场合|1921-03-16]: 大会以压倒多数通过公开条款与秘密第7条，同步开启NEP。
- **`ORG-bolsheviks-rcpb-vkpb`**（布尔什维克派—俄共（布）—联共（布））: 布尔什维克起于1903年社民工党二大后的党内多数派，经流亡、地下活动与1917年群众扩张成为执政党；1918年称俄共（布），1925年称联共（布）。它从地方主动性较强的革命党，演变为拥有任命网络与纪律制裁的党国核心，过程分阶段且存争议。 ‖ `→POL-ban-on-factions-1921`[adopted-disciplinary-rule|1921起]: 十大统一决议限制有组织派别，后续运用与原初背景应区分
- **`ORG-democratic-centralists`**（民主集中派）: 民主集中派是1919年初结成的布尔什维克党内反对派，萨普罗诺夫、奥新斯基、弗·斯米尔诺夫等为重要代表，批评以任命和行政命令取代集体领导与基层参与。成员及立场随时间变化：1923年部分人联署《四十六人声明》；后期“十五人集团”须与早期派别区分。 ‖ `→POL-ban-on-factions-1921`[subject-to-disciplinary-rule|1921起]: 统一决议要求解散派别，限制持续组织活动 ； `←POL-ban-on-factions-1921`[并列受禁派别|1921起]: 因主张集体领导与反对委派制而在十大大体失去合法平台。
- **`ORG-left-and-united-opposition`**（1923–1927年左翼反对派与托季联合反对派）: 1923年剪刀差危机触发的托洛茨基—普列奥布拉任斯基“左翼反对派”，经1926年春与季诺维也夫—加米涅夫“新反对派”结盟为托季联合反对派；以《四十六人声明》与《1927年政纲》批判官僚体制与“一国社会主义”、主张价格—财政渠道的计划工业化，于1927年12月十五大被组织摧毁。 ‖ `→POL-ban-on-factions-1921`[legal-constraint|1923–1927]: 1921年十大派别禁令将政纲散发直接定性为非法地下反党活动 ； `←POL-ban-on-factions-1921`[制度约束对象|1923–1927]: 左翼与联合反对派的申诉和联合在反派别框架下被定性违纪。
- **`ORG-right-opposition-1928`**（1928–1929年右翼反对派（右倾集团））: 1928–1929年以布哈林、李可夫、托姆斯基为核心的联共（布）党内温和派联盟，并非严密地下派系，而是依托政府、工会与莫斯科市委抵制非常征粮常态化、“贡赋论”与超工业化冒进；受制于反派别党纪，各阵地逐一遭书记处拔除，1929年11月战败认错。 ‖ `→POL-ban-on-factions-1921`[self_paralyzing_constraint|1928–1929]: 右派自身曾拥护该反派别禁令，导致1928–1929受自我制约而避免公开串联地方党组织
- **`ORG-workers-opposition`**（工人反对派）: 俄共（布）党内以产业工人和工会干部为主体的左翼反对派（1920–1922），由什利亚普尼科夫、梅德韦杰夫及理论代言人柯伦泰领导。在1920–1921年工会争论中痛斥党政官僚化与专家“一长制”，主张由“全俄生产者代表大会”及工会自治管理国民经济；1921年十大被定性为无政府工团主义倾向并遭解散。 ‖ `→POL-ban-on-factions-1921`[primary-immediate-target|1921-03-16起]: 派别禁令直接针对工人反对派与民主集中派结成独立纲领集团的挑战而制定，但随后成为约束全党后续一切反对派的制度枷锁 ； `←POL-ban-on-factions-1921`[首要直接对象|1920–1922]: 草案直接点名批评的对象，其纲领与独立活动空间被取缔。
- **`PER-kollontai`**（亚历山德拉·柯伦泰）: 将军家庭出身的马克思主义女工运动家，1917年支持四月提纲，十月后任国家救济人民委员。主持妇女部并倡家务社会化，1921年为工人反对派撰写纲领，批判专家治厂与官僚委任。其解放理想遭遇福利紧缩、就业隔离及党内纪律的约束；1922年转入外交，历驻挪威、墨西哥、瑞典而幸存。 ‖ `→POL-ban-on-factions-1921`[sanctioned_internal_dissenter|1921–1922]: 申诉并未立即终止，但继续按纲领结社面临开除威胁
- **`PER-shlyapnikov`**（亚历山大·什利亚普尼科夫）: 金属车工出身的老布尔什维克，一战时主持北欧交通线与俄国局，1917年任首届劳动人民委员。1920—1922年领导工人反对派，主张生产者自治；十大落败后入中央，秘密处分动议又差一票未过。其反官僚诉求与维护一党政权并存，晚年回忆须与当时记录对读，1937年遇害。 ‖ `→POL-ban-on-factions-1921`[threatened_with_sanction|1921-08–1922-04]: 第7条开除动议差1票；次年申诉受警告，显示处分有程序与阶段
- **`PER-zinoviev`**（格里戈里·季诺维也夫）: 老布尔什维克、共产国际首任主席（1919–1926）。1917年十月公开反对武装起义；1920年哈雷演说力推二十一条与阶级恐怖，1923年豪赌“德国十月”并首倡社民党“法西斯羽翼”论；借“三驾马车”排托后于1925年发起新反对派，1926年7月首因秘密第7条被逐出政治局，1927年底被开除后屈服。 ‖ `→POL-ban-on-factions-1921`[first-politburo-target|1926-07-23]: 1926年7月全会借“拉斯舍维奇森林案”史上首次援引该决议秘密第7条，剥夺季诺维也夫政治局正式委员席位 ； `←POL-ban-on-factions-1921`[首例第7条靶标|1926-07-23]: 1926年7月联席全会首次正式援引秘密第7条将其逐出政治局。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←POL-ban-on-factions-1921`[起草与报告人|1921.03]: 起草《关于党的统一》及秘密第7条并作大会总结报告。
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←POL-ban-on-factions-1921`[双轨耦合|1921–1929]: 经济退却与政治收紧并行的十大“双轨结构”制度前提。
- **`MTG-1922-03-11th-party-congress`**（俄国共产党（布尔什维克）第十一次代表大会（1922年））: 1922-03-27至04-02[N.S.]，俄共十一大在莫斯科召开，为列宁最后出席的党代会。他宣布NEP退却结束，强调管理、文化与官僚主义；大会警告工人反对派。04-03新中央全会设总书记并选出斯大林，04-04《真理报》公布；任命、公布均须与大会决定区分。 ‖ `←POL-ban-on-factions-1921`[后续纪律升级|1922.03]: 审查工人反对派“二十二人声明”，持续重划派别纪律边界。
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←POL-ban-on-factions-1921`[制度运用者|1923–1927]: 借助书记处任命制与反派别武器逐步瓦解各级反对派联盟。
- **`POL-war-communism`**（战时共产主义）: 1918年夏至1921年3月苏维埃经济政策总称：余粮收集制、中小工业国有化、取缔私商、货币贬值与实物配给并举；因内战饥荒与国家能力崩溃而强化，却在1921年喀琅施塔得与坦波夫危机下为新经济政策实物税所取代；其性质是应急、乌托邦跃进还是国家统制传统延续，史家分歧剧烈。 ‖ `→POL-ban-on-factions-1921`[institutionalizes-post-crisis|1921-03-16起]: 十大在喀琅施塔得背景下通过派别禁令，经济退却与党组织封闭并行

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 2 项)
### `DEB-1921-trade-union-controversy-and-party-unity`：1921年工会争论、工人反对派与党内统一之争
## [T1] 核心问题定义
内战结束之际，工会应成为国家管理生产的传动机构，还是维护工人利益并参与管理的独立空间？工人反对派、托洛茨基和列宁的方案分歧，如何与第十次党代表大会禁止派别相互交织？喀琅施塔得危机既是决议援引的背景，也是有待独立考察的社会抗议，不能混同党内派别。

## [T2] 各学派立场对照矩阵
**经验基准**：核心论战发生在1920年11月至1921年3月16日十大闭幕（`era`延至1929年托姆斯基倒台及车间体制定型）。据 `DATA-04-party-membership-and-congress-votes-1903-1929`，十大694名表决代表中工会决议票型为“十人纲领” **336票**、托洛茨基—布哈林纲领 **50票**、工人反对派 **18票**（弃权2票；1月莫斯科预备会为 `57:33:21`），《关于党的统一》反对票不足30票；秘密第7条设定处分中央委员程序。喀琅施塔得决议并非工人反对派纲领。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 工人反对派 | 亚历山德拉·柯伦泰，《工人反对派》(1921) | 批评官僚和专家支配，要求由生产者代表大会组织国民经济。 | `CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists`；`CLM-kollontai-1921-all-russian-congress-of-producers-program` | 纲领是参与者政治介入，本身亦不反对排斥非共多数，不能直接代表全体工人。 |
| 列宁与“十人纲领” | 列宁与“十人纲领”（十大代表大会多数派）；Joseph Godson, *The Soviet Worker* (1981) | 工会既是“共产主义学校”与党群“传送带”，又借民主集中制、全厂单一产业工会及内部秘密党组锁死底层独立空间，否定抗议合法性。 | `CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions` | 教义与组织章程剖析偏重上层结构，对1920年代车间议价空间关注有限。 |
| 托洛茨基与劳动军事化 | Robert Service, *Trotsky: A Biography* (2009) | 托洛茨基推动劳动军事化与Tsektran，主张“工人职责是执行命令”，在专政与一党垄断上与列宁、斯大林共享更深共识。 | `CLM-service-2009-trotsky-authoritarian-consensus` | 传记解释不能替代1920—1921年中央全会逐次辩论原档，亦不否定其后民主诉求与垄断的结构悖论。 |
| 党内制度转折 | Robert V. Daniels, *The Conscience of the Revolution* (1960) | 禁派收缩组织化异议空间，但并未立即消灭一切分歧。 | `CLM-daniels-1960-tenth-congress-turning-point` | 制度后果不能等同当时所有代表预谋后来的镇压。 |
| 工会终结与家长制三方交锋 | Leonard Schapiro (1981)；Donald Filtzer (1986)；Maksim Lebsky (2021) | Schapiro 主张1920–21即已政治终结（1920-06逮捕莫斯科印刷工会、1921初捕约2,000名孟什维克、1921-05金属工会 `120:40` 否决中央名单遭强推）；Filtzer 论证RKK与车间讨价还价延至1928-12至1929-05托姆斯基免职及1929-03-06单方解雇令；Lebsky 揭示 ФУБР 75%住房与逐宿令塑造社会依附。 | `CLM-schapiro-1981-end-of-illusion-unions-1917-to-tomsky-fall`；`CLM-filtzer-1986-nep-unemployment-and-shopfloor-bargaining`；`CLM-filtzer-1986-1929-tomsky-purge-and-shock-work`；`CLM-lebsky-industrial-paternalism-origins-1917-1929` | 三方分别侧重党团压制、车间谈判与福利依附，且均受就业市场与宏观政策转轨影响。 |

### `DEB-1928-bukharin-alternative`：布哈林替代方案与新经济政策终结之争
## [T1] 核心问题定义
1927至1929年粮食危机与新经济政策的瓦解，是否意味着渐进工业化和工农联盟已无可行出路，还是党内权力与政策选择扼杀了布哈林的替代方案？投资、价格、农民供粮和政治动员之间的约束究竟有多强，必须把经济可行性、政治可行性与实际权力斗争分别检验。

## [T2] 各学派立场对照矩阵
**经验基准**：1928年粮食收购危机后领导层采用非常措施；布哈林同年批评征粮和工业化节奏，1929年四月及十一月中央全会使右派进一步失势，同年清党开除率达 `11%`（约17万人，`DATA-04-party-membership-and-congress-votes-1903-1929`）。各方都面对工业投资、粮食供给与工农社会结构约束。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 新经济政策替代论 | Stephen Cohen, *Bukharin and the Bolshevik Revolution* (1973) | 市场、合作社和渐进工业化提供可争论的替代路径；组织机器与政治斗争使该路线失败。 | `CLM-cohen-1973-nep-viability`；`CLM-cohen-1973-notes-of-an-economist`；`CLM-cohen-1973-bukharin-organizational-defeat` | 可构想的经济路径不自动证明可获得党内多数或满足高投资目标。 |
| 工业化经济思想史 | Alexander Erlich, *The Soviet Industrialization Debate* (1960) | 布哈林平衡增长与普列奥布拉任斯基积累方案共同面对投资约束；强制全盘集体化非各派原有共同结论。 | `CLM-erlich-1960-bukharin-balanced-growth`；`CLM-erlich-1960-preobrazhensky-dilemma`；`CLM-erlich-1960-stalin-overkill-turn` | 模型不能单独解决权力、执行和国际冲击问题。 |
| 经济结构与政策选择 | Alec Nove, *Was Stalin Really Necessary?* (1964) | 提出“条件性必然”与“1927年NEP死胡同（cul-de-sac）”：给定布尔什维克保住一党政权、拒绝斯托雷平式富农资本主义与高速重工业化三大前提，布哈林市场渐进路径存在内在政治经济不一致；但仍须区分发展目标与强制手段。 | `CLM-nove-1964-stalin-necessity-dilemma` | 反事实替代方案的实施条件难以在单线历史中完全检验（详见下栏 KAPROST 交锋）。 |
| 意识形态与政治能动性 | Stephen Kotkin, *Stalin*, Vol. 1 (2014)；Sheila Fitzpatrick, *The Russian Cultural Revolution (1928–1931)* (1978) | 市场发展与党内阶级政治构成张力，斯大林西伯利亚干预使危机转向不能仅由结构推导；“文化革命”动员更将政治局右派、教育人民委员部温和派与沙赫蒂案连成“右倾危险”连续体。 | `CLM-kotkin-2014-bukharin-dilemma`；`CLM-fitzpatrick-1978-anti-bukharin-ideological-offensive` | 科特金第一卷叙事止于1928年底；宣传建构的意识形态连续体亦不能直接等同右派成员一致的文化纲领。 |
| 组织与动员政治 | Oleg Khlevniuk, *Stalin* (2015)；David Priestland, *Stalinism and the Politics of Mobilization* (2007)；Catherine Merridale, *Moscow Politics and the Rise of Stalin* (1990) | 干部控制、反右“复兴主义”动员与乌格拉诺夫莫斯科地方权力瓦解共同决定布哈林集团败局。 | `CLM-khlevniuk-2015-defeat-of-right-opposition`；`CLM-priestland-2007-1928-mobilization-turn-against-bukharin`；`CLM-merridale-1990-uglanov-moscow-collapse` | 组织性胜利并不单独证明任一经济路线的长期优劣。 |
| 反事实计量与改革经济学 | Holland Hunter / R. W. Davies / 谷内融，*戴维斯纪念文集* (1995)；刘伟、平新乔，《平衡与非平衡：布哈林与普列奥布拉仁斯基之争》（1989，B级） | 亨特借 KAPROST 模型论证非集体化 NEP 本可成功，但戴维斯（1994）反驳1928年市场已遭行政扰乱，谷内融1929年1—6月政治局档案证实非常措施演变为全国体制；刘伟、平新乔将布氏重估为“短缺经济学”先驱，指出斯大林采纳了普氏非均衡配额内核。 | `CLM-davies-festschrift-1995-nep-statistics-and-planning-debates`；`CLM-bukharin-preobrazhensky-equilibrium-vs-accumulation-zh`（B级） | KAPROST 假设重工业高积累下农民仍配合市场；刘、平一文沿用中译“81亿金卢布”误植数字，引用须剔除该数。 |
| 后苏联档案重估 | Viktor Zemskov（维克托·泽姆斯科夫），《斯大林时代》（2018，B级）；Valentin Sakharov（瓦连京·萨哈罗夫），《站在十字路口》（2012） | 泽姆斯科夫指出布哈林渐进合作化在内战记忆塑造的党员群体中缺乏政治亲和力；萨哈罗夫从反布哈林修正派立场论证2,400万碎片化小农难以支撑工业国防，MTS 与集体化是避免“斯托雷平第二版”的战略决断。 | `CLM-zemskov-2018-archival-constraints-and-party-radicalism`（B级）；`CLM-sakharov-2012-nep-crossroads-1928` | 泽氏未提供党员心态系统统计且沿用中译稿（B级）；萨哈罗夫的国家理性辩护淡化了强制集体化后的农业灾难与清洗恶果。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/31 条)
- **`CLM-daniels-1960-tenth-congress-turning-point`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 146-153]: Daniels：1921年十大将党统一转化为压缩合法反对空间的组织制度
- **`CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists`** [`SCH-kollontai-alexandra`(亚历山德拉·柯伦泰 · participant-primary-text) | PDF pp. 2-11, 22-27]: 
- **`CLM-apalkov-2023-collective-to-personal-dictatorship`** [`SCH-apalkov-dmitry`(德米特里·阿帕尔科夫 · post-soviet-archival-party-history) | pp. 20-33, 124-127, 149-158, 191-195]: 
- **`CLM-khlevniuk-2015-secretariat-and-nomenklatura`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（In Lenin's Shadow，GENERAL SECRETARY 至 1923 年 9 月组织局安排）；制度总论见 ops/xhtml/ch01a.html。工作区文本无纸质页码。]: 
- **`CLM-khlevniuk-2015-collective-leadership-erosion`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（TRYING OUT COLLECTIVE LEADERSHIP 至 THE CHOICE）。工作区文本无纸质页码。]: 
- **`CLM-khlevniuk-2015-defeat-of-right-opposition`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch03.html（His Revolution 开篇至全盘集体化的 1929 年 11 月宣布）。工作区文本无纸质页码。]: 
- **`CLM-carr-1954-platform-of-46-economic-roots`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 113-115, 374-375]: 
- **`CLM-goldman-2011-1920s-oppositions-to-enemy-category`** [`SCH-goldman-wendy`(温迪·Z·戈德曼) | pp. 18, 34, 36–37, 56–57, 73–78]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-kollontai-1921-all-russian-congress-of-producers-program`** [`SCH-kollontai-alexandra`(亚历山德拉·柯伦泰 · participant-primary-text) | PDF pp. 11-21, 25-30]: 
- **`CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions`** [`SCH-godson-joseph`(约瑟夫·戈德森 · cold-war-labor-studies) | Book pp. 106–111, 121, 128–129 [PDF pp. 118–123, 133, 140–141]]: 
- **`CLM-service-2009-trotsky-authoritarian-consensus`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本第 23–24、28–29、37 章及引言]: 
- **`CLM-schapiro-1981-end-of-illusion-unions-1917-to-tomsky-fall`** [`SCH-schapiro-leonard`(伦纳德·沙皮罗) | Book pp. 1–14 [PDF pp. 13–26]]: 
- **`CLM-filtzer-1986-nep-unemployment-and-shopfloor-bargaining`** [`SCH-filtzer-donald`(唐纳德·费尔泽) | pp. 19–29, 44–45, 77–78, 274]: 
- **`CLM-filtzer-1986-1929-tomsky-purge-and-shock-work`** [`SCH-filtzer-donald`(唐纳德·费尔泽) | pp. 22–24, 68–72, 76–82, 96–108, 274, 280–282, 287]: 
- **`CLM-lebsky-industrial-paternalism-origins-1917-1929`** [`SCH-lebsky-maksim`(马克西姆·列布斯基) | PDF pp. 9–26, 29–36, 48–49]: 
- **`CLM-cohen-1973-nep-viability`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 270-276, 316-320]: 
- **`CLM-cohen-1973-notes-of-an-economist`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 295-296, 318-320]: 
- **`CLM-cohen-1973-bukharin-organizational-defeat`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 287-289, 297-301, 322-329]: 
- **`CLM-erlich-1960-bukharin-balanced-growth`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 21-23 (PDF pp. 38-40)]: 
- **`CLM-erlich-1960-preobrazhensky-dilemma`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 34-36, 40-41, 49-51, 170-171 (PDF pp. 51-53, 57-58, 66-68, 185-186)]: 
- **`CLM-erlich-1960-stalin-overkill-turn`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 161-169, 172-177, 183-184 (PDF pp. 176-184, 187-192, 198-199)]: 
- **`CLM-nove-1964-stalin-necessity-dilemma`** [`SCH-nove-alec`(亚历克·诺夫) | pp. 20-26, 32]: 
- **`CLM-kotkin-2014-bukharin-dilemma`** [`SCH-kotkin-stephen`(斯蒂芬·科特金) | EPUB Coda (OEBPS/9780698170100_EPUB_1-25.xhtml) & Ch. 14 (OEBPS/9780698170100_EPUB_1-24.xhtml)]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 4 条，另有 36 条 L3 逐日细节见 `timeline/L3_daily/`)
- **1921-03-08 [N.S.]** (`TL-W3-1921-03-08`, L2): **俄共（布）十大开幕** — 大会以实物税代替余粮收集，并通过《关于党的统一》。实物税不是新经济政策的全部。主账 TL-1921-03-08 把 DEB-1928 挂在本日，候选记录不沿用。会议卡写闭幕于3月16日，本批未在丹尼尔斯重读闭幕日。事件卡称政治局2月已因坦波夫讨论实物税，本批未重读 Service 原页。
- **1923-12-05 [N.S.]** (`TL-W15-L1-E09-05`, L1): **党内建设决议通过** — 政治局与中监委主席团承诺党内民主，托洛茨基参与妥协文本。
- **1924-01-16 [N.S.]** (`TL-W15-L1-E09-07`, L1): **十三次代表会议开幕** — 至18日会议谴责反对派，党内民主争论遭纪律定性；并非五月十三大。
- **1927-11-14 [N.S.]** (`TL-W15-L1-E09-17`, L1): **托季被开除党籍** — 中央与中监委处分把政策争论转为党籍排除；其余骨干在十五大继续被清除。
