# 1-Hop 去重平衡上下文包：`MTG-1919-03-8th-party-congress`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`MTG-1919-03-8th-party-congress`** (俄国共产党（布尔什维克）第八次代表大会 | `cards/meetings/MTG-1919-03-8th-party-congress.md` | `multi-perspective`): 已覆盖=`party-leadership, nationalities-carr, military-institutional, democratic-centralist, party-state-centralization`；待补=`complete-congress-stenogram, rural-delegate-voices`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 150字定性微摘要
1919年3月18日至23日，俄共（布）八大在内战中通过第二党纲，围绕民族自决、红军正规化与党内集中化激烈争辩，提出巩固与中农的联盟。大会及会后一中全会确立政治局、组织局和书记处常设框架，否定党组织联邦制并强化党团对苏维埃的控制；军事反对派与民主集中派的抗辩凸显集权并非无争议。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **出席规模、第二党纲与民族自决**：出席大会的有 **301** 名有表决权代表与 **102** 名有发言权代表，代表 **313,766** 名党员（[DATA-04](../../data/DATA-04-party-membership-and-congress-votes-1903-1929.md)）。列宁在党纲辩论中反对布哈林与皮亚塔科夫将帝国主义描绘为排除了前资本主义小生产关系的“纯粹帝国主义”，并围绕民族自决权展开激烈交锋。第二党纲在原则上保留民族自决条文，但形式承认与战时实际权力运行存在显著张力（Carr）。
- **军事问题秘密会议（`174 : 95`）**：因高尔察克春耕攻势爆发，托洛茨基赴东线未出席大会，由索科利尼科夫代作军事路线主报告，弗·米·斯米尔诺夫代表军事反对派作副报告，伏罗希洛夫、萨普罗诺夫等批评旧军官（军事专家）任用、过度集中与“游击习气”整治方式。在军事问题秘密全体会议表决中，支持托洛茨基现行正规军路线的多数派获 **`174` 票**，弗·米·斯米尔诺夫军事反对派决议获 **`95` 票**；大会随后通过折衷公开决议，并由季诺维也夫口头传达一项要求在军队中更重视共产党工作人员意见的秘密指示（[Daniels Ch. 4](../../sources/monographs/daniels_1960_conscience/ch04_pages_101-125.md) `[pp. 103–107]`）。[红军与军事专家精读](../../reading-notes/mawdsley_kakurin/RN-W20-civil-war-geopolitics-and-military-specialists.md)仅提供内战红军任用军事专家与政委双签制的宏观背景，八大秘密会议交锋以 Daniels 原书分卷为准。
- **常设中枢建立、否定党联邦制与党团统治**：在斯维尔德洛夫于大会开幕前两日（`1919-03-16`）病逝的背景下，奥新斯基在组织讨论中提议将中央扩编至 21 人并将人民委员会并入全俄中央执行委员会主席团，遭季诺维也夫反驳。大会最终将中央委员会由 15 人扩编为 **19 名正式委员 + 8 名候补委员**；**`1919-03-25`** 八届一中全会正式选举产生首届常设**政治局**（5 名正式委员：列宁、托洛茨基、斯大林、加米涅夫、克列斯廷斯基；3 名候补委员：季诺维也夫、布哈林、加里宁）、**组织局**（5 人）与**书记处**（尼·尼·克列斯廷斯基任责任书记）。同期通过的组织决议明确**否定党的联邦制**，宣布乌克兰、拉脱维亚、立陶宛和白俄罗斯共产党中央委员会仅享有俄共（布）区域委员会（`областные комитеты`）地位并无条件服从俄共（布）中央；同时规定党必须在苏维埃等一切非党组织中赢得“完全政治统治（undivided political mastery）”，强制设立严守党纪的共产党党团（`фракции`）。奥新斯基、萨普罗诺夫等对官僚集中的批评构成民主集中派的直接源头，但不能将所有组织批评者简单等同于军事反对派。
- **农村路线转向中农**：大会宣布由中立化中农转向巩固与中农的联盟，继续依靠贫农并限制富农剥削；但此举与战时余粮收集制并行，既不等于取消强制征粮，也不能倒填为预先开启新经济政策。

### 2.2 核心关系网络（结构化边表）
| 目标节点 ID | 关系类型 (Relation) | 适用时期 | 一句话关系摘要 | 证据锚点 |
| :--- | :--- | :--- | :--- | :--- |
| `INS-politburo-orgburo-secretariat` | institutionalized | 1919-03 | 大会组织决议与3月25日八届一中全会共同确立政治局、组织局、书记处常设中枢。 | CLM-carr-1950-politburo-orgburo-displacement-of-state-organs; Daniels ch05 |
| `INS-rkka-red-army-and-rvr` | military-policy | 1919-03 | 秘密会议以174:95票确认正规军与军事专家路线，同时折衷强调政委与党务监督。 | Daniels ch04; RN-W20-civil-war-geopolitics-and-military-specialists |
| `PER-lenin` | programmatic-leadership | 1919-03 | 主导第二党纲与中农联盟转向，在民族自决与军事路线上力压党内左翼与军事反对派。 | CLM-carr-1950-bolshevik-self-determination-vs-cultural-autonomy; Daniels ch04 |
| `PER-trotsky` | military-leader | 1919-03 | 因东线战事缺席大会，由索科利尼科夫代为捍卫其正规军路线并赢得174:95表决。 | Daniels ch04; DATA-04-party-membership-and-congress-votes-1903-1929 |
| `PER-bukharin` | programmatic-debate | 1919-03 | 围绕“纯粹帝国主义”与民族自决权同列宁辩论，会后当选首届常设政治局候补委员。 | CLM-carr-1950-bolshevik-self-determination-vs-cultural-autonomy; Daniels ch05 |
| `PER-pyatakov` | programmatic-debate | 1919-03 | 与布哈林在党纲辩论中反对民族自决原则，主张经济集中与世界无产阶级统一。 | RN-W32-carr-dispersal-and-reunion-nationalities-ussr-1917-1923; CLM-carr-1950-self-determination-to-federal-reunion |
| `PER-osinsky` | organizational-critic | 1919-03 | 提议扩编中央至21人并反对机关官僚集中，孕育民主集中派的党内民主诉求。 | Daniels ch05; CLM-carr-1950-politburo-orgburo-displacement-of-state-organs |
| `PER-sapronov` | opposition-critic | 1919-03 | 参与军事与组织双重批评，成为此后民主集中派反对过度集中的代表人物。 | Daniels ch04; Daniels ch05; DATA-04-party-membership-and-congress-votes-1903-1929 |
| `PER-voroshilov` | military-opposition | 1919-03 | 代表察里津派军政干部批评旧军官军事专家与过度集中指挥，支持军事反对派。 | Daniels ch04; RN-W20-civil-war-geopolitics-and-military-specialists |
| `ORG-democratic-centralists` | opposition-origin | 1919-03 | 奥新斯基、萨普罗诺夫在八大对党内集中化与官僚化的批评构成该派直接源头。 | Daniels ch05; CLM-carr-1950-politburo-orgburo-displacement-of-state-organs |
| `POL-war-communism` | rural-context | 1919-03 | 提出巩固中农联盟，但仍在战时余粮收集制与高度集中经济框架内运行。 | CLM-carr-1952-war-communism-internal-contradictions; DEB-1918-war-communism-ideology-or-emergency |

### 2.3 史学争鸣光谱
- **可核事实与解释边界**：出席代表规模（301+102）、军事秘密会议票数（174:95）、会后常设政治局与书记处设立以及否定党联邦制条款均可据档案与专著核实；这些战时集权条款如何一步步演变为1920年代末的一党官僚专政，则属制度史解释，并非八大当时各方已有共识的宿命结果。
- **E. H. Carr（制度与民族—党国视角）**：强调八大表面保留民族自决原则而组织上否定党联邦制（将乌、拉、立、白共降为俄共区域委员会），并在苏维埃内部强制建立严守党纪的共产党党团，奠定了政治局—组织局取代国家苏维埃机关的制度轨道；同时剖析中农路线与战时共产主义强征体制间的结构性矛盾。
- **Robert V. Daniels（反对派史视角）**：在《革命的良心》第 4–5 章中指出，八大军事反对派与奥新斯基—萨普罗诺夫组织批评首次将党内民主、集体领导与军事正规化的内在张力推上全党辩论台面；斯维尔德洛夫病逝后的机构重组成为后来书记处坐大的制度伏笔。
- **战时共产主义动因争鸣**：关于八大中农策略与集中体制究竟主要源于意识形态蓝图抑或内战紧急应变，参见[战时共产主义争鸣卡](../../historiography/debates/DEB-1918-war-communism-ideology-or-emergency.md)与[民族与帝国争鸣卡](../../historiography/debates/DEB-1923-nationality-and-empire.md)。

## 2. 一跳邻域全量微摘要目录 (去重后共 14 个节点，0 截断)
- **`INS-rkka-red-army-and-rvr`**（工农红军与共和国革命军事委员会（РККА 与 РВСР））: 工农红军由1918年初志愿建军转向征兵与集中指挥；共和国革命军事委员会依靠前沙俄军事专家、政治委员及铁路内线组织内战。战后大裁军和伏龙芝改革建立正规军与地方民兵混合体制，1925至1929年伏罗希洛夫主政与干部工农化在政治控制与训练效能间形成持久张力。 ‖ `→MTG-1919-03-8th-party-congress`[军事争论定调|1919.03]: 军事反对派挑战专家路线，大会确认正规军与政治监督并行。 ； `←MTG-1919-03-8th-party-congress`[military-policy|1919-03]: 秘密会议以174:95票确认正规军与军事专家路线，同时折衷强调政委与党务监督。
- **`MTG-1918-03-7th-party-congress`**（俄国共产党（布尔什维克）第七次紧急代表大会）: 1918年3月6—8日（纯公历），俄共（布）七大在法定人数不足下强行召开。列宁“喘息和约”与布哈林“左派共产主义者”革命战争路线激辩12小时后，大会以30∶12∶4（初计28∶9∶1）批准《布列斯特和约》，改党名为俄共（布）并设党纲起草委员会。 ‖ `→MTG-1919-03-8th-party-congress`[program_commission_culminated_in|1918-03 – 1919-03]: 七大设立党纲起草委员会并改名，直至1919年八大才正式辩论通过第二党纲与政治局常设体制。
- **`INS-politburo-orgburo-secretariat`**（联共（布）中央政治局—组织局—书记处与官职等级名册制）: 1919年3月俄共八大后常设政治局、组织局与书记处，分掌政治决策、组织行政及日常党务人事。1922年4月斯大林任总书记后逐步控制议程、秘密文件分发与干部名册调配。经1924年七人小组协调、1925—1929年联盟重组与纪律整肃，托洛茨基、季诺维也夫、布哈林先后退出决策核心。 ‖ `←MTG-1919-03-8th-party-congress`[institutionalized|1919-03]: 大会组织决议与3月25日八届一中全会共同确立政治局、组织局、书记处常设中枢。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←MTG-1919-03-8th-party-congress`[programmatic-leadership|1919-03]: 主导第二党纲与中农联盟转向，在民族自决与军事路线上力压党内左翼与军事反对派。
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←MTG-1919-03-8th-party-congress`[military-leader|1919-03]: 因东线战事缺席大会，由索科利尼科夫代为捍卫其正规军路线并赢得174:95表决。
- **`PER-bukharin`**（尼古拉·布哈林）: 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。 ‖ `←MTG-1919-03-8th-party-congress`[programmatic-debate|1919-03]: 围绕“纯粹帝国主义”与民族自决权同列宁辩论，会后当选首届常设政治局候补委员。
- **`PER-pyatakov`**（格奥尔基·皮达可夫）: 乌克兰布尔什维克左派与苏维埃工业金融干才（1890–1937，本卡至1929年）。列宁《遗嘱》点名的六位核心领袖之一；1923年任最高国民经济委员会副主席起草盈利令引发剪刀差争论，联署《四十六人声明》并任联合反对派骨干；1928年率先脱离托洛茨基复职执掌国家银行，支持一五工业化冲刺。 ‖ `←MTG-1919-03-8th-party-congress`[programmatic-debate|1919-03]: 与布哈林在党纲辩论中反对民族自决原则，主张经济集中与世界无产阶级统一。
- **`PER-osinsky`**（瓦列里安·奥博连斯基（N·奥新斯基））: 奥辛斯基为布尔什维克经济学家、最高国民经济委员会首任主席（1917.12–1918.03），左派共产主义者及民主集中派理论家。反对布列斯特和约、专家一长制与党机关官僚集中；1923年联署《四十六人声明》，1926–1928年掌中央统计局，因坚持客观粮食统计、抵制政治干预遭免职。 ‖ `←MTG-1919-03-8th-party-congress`[organizational-critic|1919-03]: 提议扩编中央至21人并反对机关官僚集中，孕育民主集中派的党内民主诉求。
- **`PER-sapronov`**（季莫费·萨普罗诺夫）: 油漆工人出身的老布尔什维克，1918–1919年任莫斯科省苏维埃执委会主席，民主集中派组织领袖。八大至十大批判垂直委派制把党员变为“顺从的留声机”；1923年签署《四十六人声明》，1926–1927年组十五人集团，称苏联蜕变为国家资本主义专政，十五大遭开除。 ‖ `←MTG-1919-03-8th-party-congress`[opposition-critic|1919-03]: 参与军事与组织双重批评，成为此后民主集中派反对过度集中的代表人物。
- **`PER-voroshilov`**（克利缅特·伏罗希洛夫）: 卢甘斯克工人布尔什维克。1918年察里津战役与斯大林结盟，抵制托洛茨基起用旧军官；1919年八大参与军事反对力量，后任第一骑兵军革军委委员。1925年11月继任苏联陆海军人民委员兼革命军事委员会主席，1926年入政治局，1928–1929年支持斯大林击败布哈林。 ‖ `←MTG-1919-03-8th-party-congress`[military-opposition|1919-03]: 代表察里津派军政干部批评旧军官军事专家与过度集中指挥，支持军事反对派。
- **`ORG-democratic-centralists`**（民主集中派）: 民主集中派是1919年初结成的布尔什维克党内反对派，萨普罗诺夫、奥新斯基、弗·斯米尔诺夫等为重要代表，批评以任命和行政命令取代集体领导与基层参与。成员及立场随时间变化：1923年部分人联署《四十六人声明》；后期“十五人集团”须与早期派别区分。 ‖ `←MTG-1919-03-8th-party-congress`[opposition-origin|1919-03]: 奥新斯基、萨普罗诺夫在八大对党内集中化与官僚化的批评构成该派直接源头。 ； `→MTG-1919-03-8th-party-congress`[party-congress-debate|1919-03]: 组织问题与军事反对派争论
- **`POL-war-communism`**（战时共产主义）: 1918年夏至1921年3月苏维埃经济政策总称：余粮收集制、中小工业国有化、取缔私商、货币贬值与实物配给并举；因内战饥荒与国家能力崩溃而强化，却在1921年喀琅施塔得与坦波夫危机下为新经济政策实物税所取代；其性质是应急、乌托邦跃进还是国家统制传统延续，史家分歧剧烈。 ‖ `←MTG-1919-03-8th-party-congress`[rural-context|1919-03]: 提出巩固中农联盟，但仍在战时余粮收集制与高度集中经济框架内运行。
- **`PER-sokolnikov`**（格里戈里·索科尔尼科夫）: 布尔什维克财政领袖与布列斯特和约签署代表，曾在内战中支持正规军建设。1922—1926年主持财政，以切尔文改革、预算和信贷纪律稳定新经济政策，却与工业扩张需求冲突。1925年参加新反对派，质疑总书记集权；撤换动议归加米涅夫。1928年陪同布哈林密会加米涅夫，后转外交，1939年狱中被害。 ‖ `→MTG-1919-03-8th-party-congress`[military_main_reporter|1919-03]: 代托洛茨基作军事报告，秘密会议174∶95支持正规军路线并保留监督妥协
- **`EVT-1918-1920-russian-civil-war`**（俄国内战（1918–1920））: 1918至1920年红白主战场的内战中，布尔什维克依托中央腹地、军火遗产与铁路机动击败分散白军；征粮和恐怖又激起工农反抗。乌克兰及外高加索的民族国家竞争不能归入简单红白对决，克里米亚撤离仅标志主要白军战线收束，边疆与农民战争仍在延续。 ‖ `←MTG-1919-03-8th-party-congress`[strategic-context|1919]: 1919决战年党政—军事体制在八大定型

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

### `DEB-1923-nationality-and-empire`：布尔什维克民族政策、格鲁吉亚事件与苏维埃“肯定性行动帝国”性质之争
## [T1] 核心问题定义
自1922年8月“自治化”方案与格鲁吉亚冲突起，至1923年4月俄共十二大闭幕，布尔什维克究竟是在建设“肯定性行动帝国”式的制度化本土化实践，还是以先锋队组织垄断维系大俄罗斯官僚集权？争论焦点是解密速记所示的制度妥协，以及各学派因果判断与价值判断之别。

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 列宁晚期斗争与反官僚论 | Moshe Lewin, *Lenin's Last Struggle* (1968) | 格鲁吉亚事件暴露大俄罗斯沙文主义“为整个政府机器所服务”并与官僚机构合流，列宁晚年警觉最高层专政退化风险，准备清算 *dzerzhimordy*；民族问题是撤换斯大林问责的实质切口之一。 | `CLM-lewin-1968-georgian-affair-bureaucracy`; `CLM-lewin-1968-testament-intent` | 易将列宁口述笔记重构为高度连贯的“遗嘱计划”；写于1990年代十二大特别会议速记解密之前。 |
| 自由主义—极权连续论 | Richard Pipes, *The Formation of the Soviet Union: Communism and Nationalism, 1917–1923* (1954; rev. ed. 1964) | 论证布尔什维克以红军武力征服外高加索与边疆，通过单一集权党中央架空形式上的联邦制；十二大被定性为斯大林行政中央集权对民族自治的彻底胜利（Smith 正面驳斥此说）。 | `CLM-carr-1950-self-determination-to-federal-reunion`；`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` 对勘引述 | 1991年解密的十二大民族问题特别会议速记显示边疆代表反击与中央制度让步远比“单方全胜”复杂。 |
| 解密档案民族妥协论 | Jeremy D. Smith, *The Bolsheviks and the National Question, 1917–1923* (1999) | 列宁—斯大林在集中制原则上确有共识，但 `1923-04` 十二大民族问题特别会议显示边疆代表迫使斯大林大幅退让，奠定1920年代本土化相对稳固期；格鲁吉亚危机不宜简化为列斯个人生死对决。 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`; `CLM-smith-jeremy-1999-georgian-affair-reassessed` | 本土化制度繁荣期止于1930年代逆转，分期边界须清晰。 |
| 帝国史学框架 | Ronald Grigor Suny, *The Red Flag Unfurled* (2017) 等 | 沙俄—苏联宜在“宗主—边缘不平等从属与差异治理”的帝国框架下理解民族建构；1991年后“苏联=帝国”共识含事后目的论归因风险。 | `CLM-suny-2017-empire-and-nationality-dimension` | 帝国理论有助于宏观比较定位，但不能替代十二大速记级制度考证。 |
| 乌克兰社会史与本土化悖论 | George Liber, *Soviet Nationality Policy, Urban Growth, and Identity Change in the Ukrainian SSR 1923–1934* (1992) | 本土化整合城乡乌克兰人、扩张乌克兰语公共领域的同时，制度化语言边界并孕育中央难以完全消化的地方民族诉求。 | `CLM-liber-1992-korenizatsiia-paradox-late-1920s`; `CLM-liber-1992-ukrainianization-and-urban-working-class` | 侧重乌克兰工业城市化案例，外高加索与中亚须分区域检验。 |
| “肯定性行动帝国”概念框架 | Terry Martin, *The Affirmative Action Empire* (2001) 等 | 1920年代苏联对非俄罗斯民族实施制度化优待（干部、语言、教育与领土配额），以党国政治垄断为前提整合多民族边缘——动员成效与潜在离心张力并存。 | （Martin 专著独立论断卡尚待 `close-reader` 入库；现阶段参看 `POL-korenizatsiia` 与 `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`） | 概念易被字面混同于当代西方多元主义平权政策，须严守一党专政前提。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/24 条)
- **`CLM-carr-1950-politburo-orgburo-displacement-of-state-organs`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | [PDF pp. 96, 100-105, 109-114]]: 
- **`CLM-carr-1950-bolshevik-self-determination-vs-cultural-autonomy`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 419, 421, 423 (printed); PDF pp. 430, 432, 434]: 
- **`CLM-carr-1950-self-determination-to-federal-reunion`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 253-285, 364-428]: 
- **`CLM-carr-1952-war-communism-internal-contradictions`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 70-120 (Chs. 17–18)]: 
- **`CLM-carr-1950-soviet-to-party-ascendancy-mechanism`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 148, 177, 193-232]: 
- **`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 56–58, 69, 185–188, 217–218, 283–284]: 
- **`CLM-kakurin-1928-red-army-interior-lines-strategy`** [`SCH-kakurin-nikolai`(尼古拉·叶夫根尼耶维奇·卡库林) | pp. xvi–xviii, 91–93, 101–103, 198–203, 210–229]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-smith-sa-1983-from-workers-control-to-nationalization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 155–156, 166–169, 177–179, 184–186, 192（即源文件标注 PDF pp. 160–161, 171–174, 182–184, 189–191, 197）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-daniels-1960-left-communists-1918`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 70-81]: Daniels：1918年左翼捍卫革命纲领，却在分裂关头受党统一约束
- **`CLM-figes-1996-peasant-wars-and-nep-retreat`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 775-785]: 
- **`CLM-zemskov-1929-dekulakization-demographic-baseline`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | PDF pp. 6-11, 15-19, 52, 218 (原书 pp. 4-9, 13-17, 50, 216)]: 
- **`CLM-lewin-1968-georgian-affair-bureaucracy`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.9、Ch.10 与 Appendixes I–III, VII–VIII]: 
- **`CLM-lewin-1968-testament-intent`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.10 'If Lenin Had Lived . . .'；列宁原文脚注见 Soch. XLV p. 392；XLIV p. 428]: 
- **`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`** [`SCH-smith-jeremy`(杰里米·史密斯) | pp. 311, 321-325, 327-331]: 
- **`CLM-smith-jeremy-1999-georgian-affair-reassessed`** [`SCH-smith-jeremy`(杰里米·史密斯) | pp. 252-253, 260-262, 266-268, 285-288, 296-297]: 
- **`CLM-suny-2017-empire-and-nationality-dimension`** [`SCH-suny-ronald-gregor`(罗纳德·格里戈尔·苏尼) | pp. 125-140 (approx. ch. 3 opening theory; see also Witte L322-328)]: 
- **`CLM-liber-1992-korenizatsiia-paradox-late-1920s`** [`SCH-liber-george`(乔治·O·利伯) | pp. 155–157; 180–186]: 
- **`CLM-liber-1992-ukrainianization-and-urban-working-class`** [`SCH-liber-george`(乔治·O·利伯) | pp. 75–76; 99–105]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
