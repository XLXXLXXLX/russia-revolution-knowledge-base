# 1-Hop 去重平衡上下文包：`MTG-1906-04-rsdlp-4th-stockholm-congress`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`MTG-1906-04-rsdlp-4th-stockholm-congress`** (俄国社会民主工党第四次（统一）代表大会（1906年） | `cards/meetings/MTG-1906-04-rsdlp-4th-stockholm-congress.md` | `multi-perspective`): 已覆盖=`party-rules-primary, factional-political-history, western-party-history, carr-duma-optimism, daniels-factional-discipline, menshevik-memoir`；待补=`full-congress-minutes, national-organizations-independent-archives, lenin-cw10-land-program-text`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1906-04-23至05-08[N.S.]，俄社民工党在斯德哥尔摩召开统一大会。基层统一诉求促两派会合，孟什维克占表决多数，土地地方自治化方案获胜。章程首次明定民主集中制，党员公式采用列宁“加入一个党组织”的表述，并重组民族组织关系；形式统一未消除派别网络。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **统一的压力与多数**：革命中的群众运动与工人要求党内统一，推动布尔什维克和孟什维克重新召开共同大会。Carr 的解释是：统一大会“在十月宪法和第一届杜马产生的乐观情绪达到高潮时召开，因此孟什维克占据了多数”（`carr_bolshevik_rev_v1_zh/ch04…` L994–998）。大会有112名有表决权代表、22名发言权代表；《列宁全集》第13卷注〔2〕给出的派别票数为孟什维克62票、布尔什维克46票。**分母提示**：62+46=108，与112差4票；波兰与立陶宛社会民主党、拉脱维亚社会民主党和崩得等民族社民组织代表是否计入112、62与46，站内档案未分项，待《代表大会记录》或《列宁全集》第13卷注〔2〕全文核对。本卡不得据 62:46 推断任何单项议题的比数，剩余票数亦不硬分给任何一派。
- **土地方案**：马斯洛夫及普列汉诺夫支持的地方自治化方案获得大会多数；它设想将地主土地交由民主化地方自治机关掌管。列宁主张土地国有化，认为革命政权应掌握土地所有权。两者都针对地主土地制度，但在处置主体与革命国家的权力上分歧明显；站内无一手决议文本，Lenin CW 10 土地纲领修订待入库，各项方案的具体例外和投票细目仍须对读大会记录；与土地制度后续走向相关的争论见 `DEB-1906-stolypin-wager-and-agrarian-viability`。
- **章程与多民族组织**：通过的章程第1条**改回列宁的成员公式**（承认纲领、物质上支持党并加入一个党组织），而1903年通过的是马尔托夫公式；这一回摆由孟什维克占多数的大会作出，且大会以“多余而不言自明”为由否决了布尔什维克附在第1条上的注释（S 级档案 L25、L29），是对 `DEB-1903-bolshevik-menshevik-split` 的重要站内反证。第2条首次把民主集中制明文写入党章。第3条同时保留组织内部活动自治，第8条规定大会为最高机关及代表选举的民主原则，不能把这一条自动等同于后来党国制度。大会与波兰和立陶宛社会民主党、拉脱维亚社会民主党及崩得达成加入统一党的安排；具体条款及各组织批准程序待查会议记录。
- **武装行动与“剥夺”决议**：Daniels 记斯德哥尔摩大会否决了布尔什维克对游击小组（partisan units）的无条件辩护，并谴责对私人公民的“剥夺”与暴力行为；布尔什维克以“不会让统一的观念在我们脖子上套上绞索”回应，并保有自己的秘密机关与财政（`daniels_1960_conscience/ch01_pages_26-50.md` L412–425）。这支撑了下条所述“形式统一未消除派别网络”。
- **统一的限度**：统一中央和党章并未消除战略与派别竞争；后续分歧与组织对抗持续，不能将1906年的形式统一误写成1903年分裂已永久消失。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `MTG-1903-rsdlp-2nd-congress` | `follows_and_reunifies` | 1903–1906 | 对1903年后派别分裂作组织性修复，未消除分歧；第1条由马尔托夫公式改回列宁公式。 | 1906年章程档案 L25；`DEB-1903-bolshevik-menshevik-split` |
| `PER-lenin` | `advocates_land_nationalization` | 1906 | 在土地问题上反对大会多数的地方自治化方案；参加党章起草委员会。 | 无站内一手文本；Lenin CW 10 待入库；章程档案 L125 |
| `ORG-mensheviks` | `holds_congress_majority` | 1906 | 注释统计62票，62+46=108≠112，差额及民族组织票的归属待核；不能视为每项议题完全一致。 | 章程档案 L125；Carr ch04 L994–998 |
| `ORG-bund` | `rejoins_united_party` | 1906 | 与统一党重新建立组织关系；其代表是否计入62/46/112待核。 | 大会民族组织决议待补 |
| `CON-democratic-centralism-and-vanguard` | `codifies_principle` | 1906 | 大会通过本第2条写入民主集中制，其他条款仍规定选举与内部自治。 | 1906年章程第2、3、8条（S 级档案） |

### 2.3 史学争鸣光谱
**可核事实**是章程文本及注释所载代表构成；统一对地方派别实践的实际约束仍须以地方档案和会议记录检验。具名视角如下：
- **Carr（杜马乐观主义）**：孟什维克多数源于十月宪法与第一届杜马带来的乐观情绪，使以议会与合法斗争为主的路线占优（A 级专著 ch04 L994–998）。
- **Daniels（派别纪律与财政裂缝）**：统一大会没有消除布尔什维克的双重纪律标准与秘密财政，在武装行动／剥夺问题上多数谴责之，裂缝仍在（ch01 L412–425）。
- **Getzler / Galili（孟什维克多数立场）**：以孟什维克自身逻辑解释1903年第1条与1906年统一，可对读 `CLM-getzler-1967-martov-1903-clause-one`，以及 `reading-notes/galili_1989_menshevik_leaders` 与 `reading-notes/getzler_1967_martov` 对孟什维克领导层统一诉求的描述。
- **Haimson 等对 1903 年分裂的长期思想分歧解释** 与 **把冲突置于共同社会民主主义传统及组织处境中的解释**，对1906年统一的持久性有不同预期（`CLM-haimson-1955-1903-second-congress-split`）；不应把后来的分裂倒写为大会当时注定失败。

## 2. 一跳邻域全量微摘要目录 (去重后共 6 个节点，0 截断)
- **`EVT-1905-12-moscow-armed-uprising`**（1905年12月莫斯科武装起义与普列斯尼亚街垒战）: 1905-12-07至12-18[O.S.]/12-20至12-31[N.S.]，莫斯科总罢工转为巷战。铁路未断使谢苗诺夫近卫团得以增援，重炮镇压普列斯尼亚，全城估死千人。败局引发普列汉诺夫反对起兵、列宁要求坚决进攻、托洛茨基强调争夺军队的战略分歧。 ‖ `→MTG-1906-04-rsdlp-4th-stockholm-congress`[polarizes_strategy|1906-01 至 1906-05-08 [N.S.]]: 莫斯科败局直接引爆1906年4月斯德哥尔摩四大上普列汉诺夫“本不该拿起武器”与列宁“本应更坚决进攻”的路线分水岭，并促成自由派立宪民主党（ORG-kadets）与街头暴力革命切割。
- **`MTG-1903-rsdlp-2nd-congress`**（俄国社会民主工党第二次代表大会（1903年7–8月））: `1903-07-30` 至 `08-23 [N.S.]` 俄社民工党二大先后在布鲁塞尔与伦敦召开。大会通过党纲；第23次会议马尔托夫党章第一条 `28:22:1` 胜列宁案。随后的崩得与经济派退场逆转了多数，列宁借微弱多数改组《火星报》三人编委，由此衍生布尔什维克与孟什维克之名。 ‖ `←MTG-1906-04-rsdlp-4th-stockholm-congress`[follows_and_reunifies|1903–1906]: 对1903年后派别分裂作组织性修复，未消除分歧；第1条由马尔托夫公式改回列宁公式。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←MTG-1906-04-rsdlp-4th-stockholm-congress`[advocates_land_nationalization|1906]: 在土地问题上反对大会多数的地方自治化方案；参加党章起草委员会。
- **`ORG-mensheviks`**（孟什维克）: 俄国社会民主主义政党（1903–1924），源于1903年二大马尔托夫等与列宁围绕党章第一条及集中制的决裂，主张开放型群众政党与工人自主活动。1917年分化为策烈铁里、但恩主导的入阁“革命护国派”与马尔托夫领导的反战“国际主义派”；十月后开展苏维埃合法反对派抗争，1921年后遭取缔。 ‖ `←MTG-1906-04-rsdlp-4th-stockholm-congress`[holds_congress_majority|1906]: 注释统计62票，62+46=108≠112，差额及民族组织票的归属待核；不能视为每项议题…
- **`ORG-bund`**（崩得（立陶宛、波兰和俄罗斯犹太工人总同盟））: 1897年维尔纽斯成立的帝俄最早群众性犹太工人社会民主党：1898年参与筹备俄社民工党一大，1903年二大因联邦制与“唯一代表权”被拒而退场，客观上促成列宁派组织多数；提出民族文化自治理论；内战后苏俄境内组织于1921年3月并入俄共（布），波兰崩得则作为独立犹太社会主义政党存续至二战时期。 ‖ `←MTG-1906-04-rsdlp-4th-stockholm-congress`[rejoins_united_party|1906]: 与统一党重新建立组织关系；其代表是否计入62/46/112待核。
- **`CON-democratic-centralism-and-vanguard`**（先锋队党与民主集中制）: 布尔什维克组织原则的跨期复合概念：从民意党集中制与特卡乔夫“自觉少数”，经1902年职业革命家论、1905–1906年成文的民主集中制及1917年群众政党，至1921年禁派令与斯大林书记处官职名册制，派别空间收缩；部分制度史研究强调干部任命权日益压过民主原则。 ‖ `←MTG-1906-04-rsdlp-4th-stockholm-congress`[codifies_principle|1906]: 大会通过本第2条写入民主集中制，其他条款仍规定选举与内部自治。

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 2 项)
### `DEB-1903-bolshevik-menshevik-split`：《怎么办？》与1903年布尔什维克—孟什维克分裂实质之争
## [T1] 核心问题定义
《怎么办？》的自发性与意识理论究竟体现精英代替工人，还是欧洲社会民主主义所共有的结合公式？1903年党章、领导机构选举和代表退会如何共同造成分裂，又能否把后来的一党统治直接追溯到当时？必须区分文本论战、组织选择和事后政治后果。

## [T2] 各学派立场对照矩阵
**经验基准**：二大在布鲁塞尔与伦敦举行（会场公历1903-07-30至08-23 [N.S.]，对应俄历07-17至08-10 [O.S.]）；`era`覆盖1902《怎么办？》至1904年论战。第23次会议（08-02 [N.S.] / 07-20 [O.S.]）党章第一条51票唱名表决中，列宁“参加党的一个组织”案以23:28被否、马尔托夫“在组织领导下经常亲自协助”案以28:22（1弃权）通过、整条以35:1（12弃权）通过；随后经济派（阿基莫夫、马尔丁诺夫，2票）与崩得（《记录》口径5人5票，Haimson口径5人4票）退场改变票基，在第31次会议《火星报》三人编委（普列汉诺夫、列宁、马尔托夫）选举中列宁派以25:2（20弃权，Haimson口径22:20:2）获胜而得名“多数派”。更硬的事后反证是：1906年斯德哥尔摩四大在孟什维克62:46占多数的条件下，党章第一条直接改回列宁1903年“参加党的一个组织”公式，证明1903年字句之争并非永久不可逾越的意识形态鸿沟。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 冷战自由派与雅各宾—特卡乔夫连续论（及1904当事人先声） | William Henry Chamberlin (1958, 援引 Karpovich 与 Talmon)；Richard Pipes, *The Russian Revolution* (1990)；[当事人 B 级论战] Leon Trotsky, *Our Political Tasks* (1904) | 将《怎么办？》与1903年建党方案置于法国雅各宾派—布朗基—特卡乔夫“少数密谋家夺权”及俄国激进知识分子职业革命家传统中，视之为一党专政的制度基因；托洛茨基1904年已从党内提出“党组织替代党、中央替代组织、独裁者替代中央”的“替代主义”警告。 | `CLM-jacobin-ancestry-tkachev-blanqui-and-leninism`；`CLM-pipes-1990-patrimonial-state-and-intelligentsia` | 以1917/1930年代结局倒推1902–1903年文本，忽视考茨基主流正统语境及1906年孟什维克自己采纳列宁党章第一条的事实。 |
| 思想史与组织张力 | Leopold H. Haimson, *The Russian Marxists and the Origins of Bolshevism* (1955)；Haimson (1987) | 俄国马克思主义知识分子内部长期存在“自觉性（意识）”与“自发性”的心理及认识论张力，在《怎么办？》、二大组织冲突及孟什维克“党内大家庭”伦理 vs 布尔什维克集中制中集中爆发。 | `CLM-haimson-1955-lenin-what-is-to-be-done`；`CLM-haimson-1955-consciousness-spontaneity`；`CLM-haimson-1955-1903-second-congress-split`；`CLM-haimson-1987-menshevik-party-ethos-and-family` | 知识分子群体心理连续性不能替代对二大逐场议程、崩得退席与编委改选偶然票序的制度分析。 |
| 爱尔福特语境重释 | Lars T. Lih, *Lenin Rediscovered: What Is to Be Done? in Context* (2006) | 《怎么办？》核心是考茨基《爱尔福特纲领》“社会主义与工人运动相结合”的欧洲社民主流公式，旨在以德国SPD模式激发地下工作者信心，绝非轻蔑工人的“担忧工联主义”密谋手册。 | `CLM-lih-2006-erfurtian-merger-formula`；`CLM-lih-2006-kautsky-and-spontaneity`；`CLM-lih-2006-textbook-myth-critique` | 强调1902年文本的爱尔福特共识，容易淡化1903年二大后在中央集权、编委人事与派别组织操作上的真实决裂。 |
| 孟什维克政治传记 | Israel Getzler, *Martov: A Political Biography of a Russian Social Democrat* (1967) | 从马尔托夫对党员资格弹性、老编委集体荣誉及党内自治的维护解释1903年决裂，指出马尔托夫拒任三人编委使组织微差升级为派别分野。 | `CLM-getzler-1967-martov-1903-clause-one` | 马尔托夫个人品格与后期民主社会主义立场不能简单投射为1903年全体“软派”火星派代表的既定纲领。 |
| 帝国边疆社会民主主义 | Eric Blanc, *Revolutionary Social Democracy* (2021) | 以帝国边疆非俄罗斯民族社会民主党（崩得、拉脱维亚、波兰、芬兰等）的群众性合法/半合法组织实践与共同的“革命考茨基主义”，打破仅以俄国中心流亡小报编委为轴的建党叙事。 | `CLM-blanc-2021-revolutionary-kautskyanism-in-empire`；`CLM-blanc-2021-beyond-russocentric-bolshevism` | 边疆宏观组织比较不能取代二大第23次与第31次会议具体党章文本、联邦制否决及唱名票序的微观因果。 |
| 工人能动性与政治修辞辨析 | S. A. Smith (1996/1999，收入 Reginald E. Zelnik 编论文集)；Robert Mayer (1999) | Smith（及Zelnik译注卡纳奇科夫自传）揭示1895–1917年彼得堡“觉悟工人”追求去监护化自治、排斥知识分子两派内斗；Robert Mayer考证列宁1903–1904年的“雅各宾”自称直接承袭普列汉诺夫1901年的法国大革命修辞以打击机会主义，而非效法特卡乔夫或布朗基密谋。 | `CLM-zelnik-1999-worker-intelligentsia-tutelage-tension`；`CLM-zelnik-1999-kanatchikov-conscious-worker-formation`；`CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism` | 概念史修辞澄清与基层工人心态史分属不同分析层面，需与中央党组织制度变迁互证。 |

### `DEB-1906-stolypin-wager-and-agrarian-viability`：村社生命力与斯托雷平土改前景之争
## [T1] 核心问题定义
如果没有世界大战，帝俄能否借私有农户与农业增长和平化解农村革命？争议同时涉及生产效率、村社制度的适应力与政治稳定，任何一项的改善都不能自动证明另外两项。反事实命题不能由改革中断的事实直接证成或证伪。

## [T2] 经验共识 + 各学派立场对照矩阵

**经验共识**：1906年11月9日俄历／11月22日公历的敕令允许农户申请巩固份地；确权、整合分散条田与迁居独立农庄是不同过程，地区和统计分母不可混同。大战妨碍实施，1917年许多分离土地重新进入村社分配，但地方经历并不一致。

| 取向 | 代表与问题 | 论证及局限 | 本地论断锚点 |
| :--- | :--- | :--- | :--- |
| 自由派与现代化乐观论 | Gerschenkron、Pipes、Ascher；和平与长期改革前景 | 私有地权、信贷与整田可能培育独立经营者并稳定秩序；“二十年和平”是一种政治期待，不是可验证的产出预测。各作者对前景的具体判断及其差异须回核原著。 | `POL-stolypin-agrarian-reform` |
| 农民社会史 | Shanin、Figes、Pallot、Hildermeier | 村社兼具资源分配、保障和协调功能；地方制度与土地压力影响农民选择，强制分离可能加深村内冲突。黑土核心区与边缘地区的差异须按省、年份和地权类别核对，不能把任何一地推广全国。 | `CLM-figes-1996-peasant-moral-economy-1917`; `CLM-hildermeier-2000-agrarian-socialism-modernization-dilemma` |
| 马克思主义道路论 | 列宁的“普鲁士道路”与“美国道路” | 土地集中和地主主导的资本主义转型，与农民革命清除地主土地的道路具有不同社会代价；这是政治经济学的道路比较，并非后见之明式预测。 | `CLM-service-lenin-v1-agrarian-marxism-and-1905-tactics` |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 18/18 条)
- **`CLM-getzler-1967-martov-1903-clause-one`** [`SCH-getzler-israel`(伊斯雷尔·格茨勒) | pp. 78-79]: 
- **`CLM-haimson-1955-1903-second-congress-split`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. 175-191]: 
- **`CLM-jacobin-ancestry-tkachev-blanqui-and-leninism`** [`SCH-chamberlin-william-henry`(威廉·亨利·钱伯林) | pp. 251–257 (PDF pp. 2–8)]: 
- **`CLM-pipes-1990-patrimonial-state-and-intelligentsia`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 2 (Official Russia); ch. 4 (The Intelligentsia); cf. Introduction]: 
- **`CLM-haimson-1955-lenin-what-is-to-be-done`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. 132-141]: 
- **`CLM-haimson-1955-consciousness-spontaneity`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. vi-viii, 7-11]: 
- **`CLM-haimson-1987-menshevik-party-ethos-and-family`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. 14–17]: 
- **`CLM-lih-2006-erfurtian-merger-formula`** [`SCH-lih-lars`(拉斯·T·利) | pp. 6-9, 41-49, 74-106, 113-121, 556-557]: 
- **`CLM-lih-2006-kautsky-and-spontaneity`** [`SCH-lih-lars`(拉斯·T·利) | pp. 35-37, 555, 613-667]: 
- **`CLM-lih-2006-textbook-myth-critique`** [`SCH-lih-lars`(拉斯·T·利) | pp. 5, 13-33, 555]: 
- **`CLM-blanc-2021-revolutionary-kautskyanism-in-empire`** [`SCH-blanc-eric`(埃里克·布兰克) | pp. 25–28, 569–578]: 
- **`CLM-blanc-2021-beyond-russocentric-bolshevism`** [`SCH-blanc-eric`(埃里克·布兰克) | pp. 15–16, 23–26]: 
- **`CLM-zelnik-1999-worker-intelligentsia-tutelage-tension`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | pp. 6-7, 13-15, 18-27, 51-52]: 
- **`CLM-zelnik-1999-kanatchikov-conscious-worker-formation`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | pp. 9-12, 26-27]: 
- **`CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism`** [`SCH-mayer-robert`(罗伯特·迈耶) | pp. 127-129, 140-146]: 
- **`CLM-figes-1996-peasant-moral-economy-1917`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 343-352]: 
- **`CLM-hildermeier-2000-agrarian-socialism-modernization-dilemma`** [`SCH-hildermeier-manfred`(曼弗雷德·希尔德迈尔) | EPUB版无稳定原书页码；以本地章节与行号定位（ch08 L75–232, ch09 L26–44, ch12 L204–282, ch13 L107–185, ch17 L115–310, ch20 L750–753, ch24 L180–285, ch26 L6–96；epub:main-8.xhtml, main-9.xhtml, main-12.xhtml, main-13.xhtml, main-21.xhtml, main-25.xhtml, main-27.xhtml）]: 
- **`CLM-service-lenin-v1-agrarian-marxism-and-1905-tactics`** [`SCH-service-robert`(罗伯特·瑟维斯) | pp. 74-80, 152-166, 169-185 (中译本 PDF 页码)]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
