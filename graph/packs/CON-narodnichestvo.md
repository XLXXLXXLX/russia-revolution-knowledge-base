# 1-Hop 去重平衡上下文包：`CON-narodnichestvo`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`CON-narodnichestvo`** (俄国民粹主义：运动、自我认知与论战范畴 | `cards/concepts/CON-narodnichestvo.md` | `multi-perspective`): 已覆盖=`intellectual-history-venturi-walicki, berlin-moral-humanism, pipes-patrimonial-skepticism, marxist-polemical, psr-hildermeier`；待补=`peasant-voices, gender-history`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 150字定性微摘要
俄国民粹主义以人民特别是农民及村社为变革依托，却非单一教义。赫尔岑、车尔尼雪夫斯基开启先声，一八六九年形成古典民粹派；七十年代分化出政治恐怖与土地宣传两支，后经八九十年代合法论争与社革党改造。学界历来并存派普斯界定的七十年代反智“狭义”与列宁—瓦利茨基的“广义”世界观界定。

## [T2] 核心脉络与史学争鸣
### 2.1 词源、定义谱系与语义分期
- **狭义（历史义）与广义（社会学义）之辨**：Richard Pipes（1964）将 1870 年代中期反对知识分子包办、主张群众凌驾受教育精英的短期反智浪潮界定为**狭义历史义**（按此界定，连拉甫罗夫派、特卡乔夫与民意党均不算民粹派），并将广义用法贬为马克思主义者的“论战伎俩”。与之相对，**列宁**正式奠定了民粹主义的**广义历史社会学义**（“始于赫尔岑，终于丹尼尔逊”）：将其视为小生产者抗议资本主义摧残并要求废除农奴制残余的完整世界观；**瓦利茨基**（Walicki, 1969）直接驳斥 Pipes 的“论战伎俩说”，论证列宁的广义定义是极其精准的方法论分析工具，容许不同流派在同一意识形态框架内对称分化。
- **1860年代前史（“前民粹主义”）**：“народ”指人民；народничество 是后起的分析范畴，不能以当代泛称“民粹主义”替代。瓦利茨基据此修正科兹明过宽划界，指出赫尔岑（“贵族社会主义”）与车尔尼雪夫斯基（兼具西化启蒙遗产与“诞生状态的民粹主义”二重性）依托村社设想非资本主义发展，属于先驱而非统一政党；直至 **1869年**（拉甫罗夫《历史书简》、米哈伊洛夫斯基《什么是进步？》、弗列罗夫斯基《俄国工人阶级状况》同年问世）才标志**古典民粹主义**正式成型。
- **1870年代**：拉夫罗夫强调知识分子启发与道德宣传，巴枯宁强调群众自发起义，特卡乔夫突出少数职业革命者夺取国家；1874年“到民间去”遭农村现实与警察镇压挫败后，地下骨干重组为“土地与自由社”（`ORG-zemlya-i-volya`）。1879年该社经利佩茨克与沃罗涅日会议分裂为`ORG-narodnaya-volya`（诉诸政治斗争与暗杀，纲领兼含宪制与立宪会议诉求，不能简化为专政蓝图）与`ORG-chernyi-peredel`（坚持土地宣传与社会革命）。
- **1880—1890年代**：沃龙佐夫与丹尼尔逊等“合法民粹派”讨论资本主义市场局限与村社前途；普列汉诺夫与列宁则依俄国资本主义发展与农村阶级分化展开批判。列宁一方面严厉批判 1880—1890 年代合法民粹派的“经济浪漫主义”，另一方面在其广义定义中同时肯定民粹主义反对农奴制残余的民主内核，并非用论战标签抹杀全部革命传统。马克思与查苏利奇 1881 年通信及《共产党宣言》1882 年俄文版序言亦表明，村社跳过资本主义的可能性在马克思晚年是附带条件的历史开放问题。
- **20世纪**：社会革命党（`ORG-psr`）整合“土地社会化”纲领与农民动员传统（通常称“新民粹主义”），在 20 世纪现代化与政党竞争条件下重组遗产，同时面临村社解体与“战斗组织—群众政党二元撕裂”的结构困境，不能视为 1870 年代组织的原样复活。

### 2.2 核心关系网络（结构化边表）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-herzen` | 思想先驱 | 1848–1870 | 以贵族社会主义与村社设想开启“前民粹主义”源流。 | `CLM-berlin-1960-populism-moral-core`; `CLM-walicki-1969-narodnichestvo-definition` |
| `PER-chernyshevsky` | 二重先驱 | 1860s–1880s | 兼具西化启蒙立场与“诞生状态的民粹主义”二重性。 | `CLM-walicki-1969-narodnichestvo-definition` |
| `PER-lavrov` | 理论支柱 | 1869–1900 | 《历史书简》标志古典民粹派成型并奠定道德宣传派。 | `CLM-berlin-1960-populism-moral-core`; `CLM-walicki-1969-narodnichestvo-definition` |
| `PER-bakunin` | 激进翼奠基 | 1860s–1870s | 主张否定国家与依托农民自发暴动的无政府民粹路线。 | `CLM-walicki-1969-narodnichestvo-definition` |
| `EVT-1874-going-to-the-people` | 运动转折 | 1874–1878 | 知识青年下乡宣传遇挫并推动地下组织与策略重整。 | `CLM-walicki-1969-narodnichestvo-definition` |
| `ORG-zemlya-i-volya` | 运动载体 | 1876–1879 | 整合 1870 年代地下民粹派，并于 1879 年一分为二。 | `CLM-venturi-1960-lipetsk-voronezh-split` |
| `ORG-narodnaya-volya` | 组织分化 | 1879–1887 | 转向政治恐怖与沙皇暗杀，同时保留宪制代表制纲领。 | `CLM-venturi-1960-narodnaya-volya-constitutionalism` |
| `ORG-chernyi-peredel` | 组织分化 | 1879起 | 坚持土地宣传与经济—社会革命，反对民意党政治恐怖。 | `CLM-venturi-1960-lipetsk-voronezh-split` |
| `EVT-1881-03-assassination-of-alexander-ii` | 历史枢轴 | 1881.03–05 | 刺杀亚历山大二世后政权反扑与民粹派地下组织解体。 | `DEB-1879-narodnaya-volya-to-bolshevism` |
| `PER-plekhanov` | 马克思主义批评者 | 1883–1895 | 从黑土重分派转向马克思主义，借“现实理性”批判民粹派。 | `CLM-walicki-1969-plekhanov-rational-reality` |
| `PER-lenin` | 广义界定与论战者 | 1890s起 | 奠定“广义社会学义”界定并批判合法民粹派“经济浪漫主义”。 | `CLM-walicki-1969-narodnichestvo-definition` |
| `ORG-psr` | 20世纪继承 | 1901–1922 | 整合土地社会化与政治恐怖的“新民粹主义”现代政党。 | `CLM-hildermeier-2000-agrarian-socialism-modernization-dilemma` |
| `DEB-1879-narodnaya-volya-to-bolshevism` | 核心争鸣 | 1879之后 | 民意党职业密谋遗产与列宁主义组织原则的连续与断裂。 | `CLM-berlin-1960-populism-moral-core` |

### 2.3 多视角史学争鸣
- **伦理人文主义视角（Isaiah Berlin）**：在《革命的根源》导论（1960）中，伯林强调俄国民粹主义并非经济决定论的附庸，而是一场以道德团结、社会正义和个人良知至上为核心的伦理运动；即使恐怖分子亦拒绝以“历史必然律”豁免暴行，这构成了民粹派与列宁主义党国决定论的根本断裂（参见 `CLM-berlin-1960-populism-moral-core`）。
- **语义怀疑与家产制视角（Richard Pipes）**：Pipes（1964）将真正的民粹主义限定于 1870 年代中期反智主义“狭义历史义”，把广义民粹主义斥为马克思主义的“论战伎俩”；在其 1990 年《俄国革命》中则从家产制专制与激进知识分子“渴求权力”的二元断层剖析革命起源（参见 `CLM-pipes-1990-patrimonial-state-and-intelligentsia`）。
- **思想史结构与方法论辩护（Andrzej Walicki）**：Walicki（1969）明确**反驳 Pipes**，肯定列宁奠定的广义民粹主义定义具有高度方法论效力，并以 1869 年区分“前民粹主义”与“古典民粹主义”；他同时以“后进农民国家对西方资本主义与西方社会主义的双重反应”重估市场论争与马克思对民粹派的亲和与张力（参见 `CLM-walicki-1969-narodnichestvo-definition`、`CLM-walicki-1969-marx-populist-affinity`）。
- **组织行动史与现代政党困境（Franco Venturi / Manfred Hildermeier）**：Venturi（1960）详考地下网络与民意党宪制诉求（`CLM-venturi-1960-lipetsk-voronezh-split`、`CLM-venturi-1960-narodnaya-volya-constitutionalism`）；Hildermeier（2000）揭示 20 世纪社革党陷入工业化下“土地社会化乌托邦”与“恐怖组织—群众政党互为反题”的双重危机（`CLM-hildermeier-2000-agrarian-socialism-modernization-dilemma`、`CLM-hildermeier-2000-psr-terror-vs-mass-party-dualism`）。农民自述与性别经验仍有待更多区域基层材料补充。

## 2. 一跳邻域全量微摘要目录 (去重后共 16 个节点，0 截断)
- **`CON-intelligentsia-and-vekhi`**（俄国知识分子阶层、《路标》论战与“资产阶级专家”）: 俄国知识分子从伦理异议共同体向苏维埃体制群体重构。1860年代平民知识分子与拉夫罗夫奠定反专制献身传统；1909年《路标》批判激进派反法制与政治狂热，遭列宁谴责。十月后“资产阶级专家”受监控，经历1922年“哲学船”驱逐、1928年沙赫特案整肃及工农干部提拔。 ‖ `→CON-narodnichestvo`[revolutionary-martyr-crucible|1870s–1881]: 民粹运动使平民知识分子从启蒙沙龙走向农村宣传与地下密谋献身，同时种下重社会平等而轻形式法治的传统
- **`CON-kulak`**（富农（作为社会阶层与政治定罪标签））: “富农”兼具农村阶层与政治定罪含义：19世纪原指高利贷盘剥者，列宁称农村资产阶级；斯托雷平改革分离户也遭村社如此指斥。1918年为贫农委员会征粮对象，1925年NEP放宽而农村趋向中农化；1928–1929年经刑法107条与雅科夫列夫委员会转为阶级清洗标签。 ‖ `→CON-narodnichestvo`[pre-marxist-pejorative-framer|1870s–1890s]: 以村社道德经济视角将 кулак / мироед 界定为侵蚀公社的高利贷与商业寄生者
- **`PER-herzen`**（亚历山大·赫尔岑）: 19世纪俄国革命民主派思想家、“俄国社会主义”奠基人与流亡出版家。1847年永居西欧，目睹1848革命退潮后批判西方资产阶级市侩制度与历史决定论，转向依托俄国农村公社的自主发展构想。1853年设伦敦自由俄罗斯印刷所，1857年创办《钟声》，在废奴改革与青年激进派之间搭建流亡舆论枢纽。 ‖ `←CON-narodnichestvo`[思想先驱|1848–1870]: 以贵族社会主义与村社设想开启“前民粹主义”源流。 ； `→CON-narodnichestvo`[intellectual-progenitor|1848–1870]: 提出依托村社跨越西方资本主义的“俄国社会主义”愿景，但瓦利茨基强调其“贵族社会主义”与1869年后古典民粹主义存在代际与结构界限
- **`PER-chernyshevsky`**（尼古拉·车尔尼雪夫斯基）: 19世纪俄国革命民主派理论家与《现代人》主笔。以唯物主义伦理与“合理利己主义”批判农奴制，1859年有条件论证农村公社可借先进成果跨过资本主义。1862年被捕，狱中著《怎么办？》以拉赫美托夫“新人”伦理深塑民粹派与青年列宁；1864年经民事处决服苦役继而流放西伯利亚，1889年病逝萨拉托夫。 ‖ `←CON-narodnichestvo`[二重先驱|1860s–1880s]: 兼具西化启蒙立场与“诞生状态的民粹主义”二重性。 ； `→CON-narodnichestvo`[dual-status-precursor|1860s–1880s]: 瓦利茨基界定其兼具60年代西化启蒙（*prosvetitel'stvo*）与“诞生状态民粹主义”二重性，门徒分化为民粹派与皮萨列夫虚无主义两翼
- **`PER-lavrov`**（彼得·拉夫罗夫）: 俄国民粹派“宣传准备派（lavristy）”宗师与主观社会学奠基人。1868–1869年著《历史信札》，倡“批判思维的个人”须向人民清偿历史道德债务，感召1874年“到民间去”。1873年流亡主编《前进！》，批巴枯宁盲动并以“雅各宾社会主义者”批特卡乔夫夺权论，晚年合编《民意党通报》。 ‖ `←CON-narodnichestvo`[理论支柱|1869–1900]: 《历史书简》标志古典民粹派成型并奠定道德宣传派。 ； `→CON-narodnichestvo`[theoretical-pillar|1869–1900]: 1868–1869《历史信札》标志古典民粹主义成型，与米海洛夫斯基共筑“主观社会学”与伦理个人主义哲学支柱
- **`PER-bakunin`**（米哈伊尔·巴枯宁）: 国际无政府主义与俄国民粹派“造反派（buntari）”宗师。1848年投身欧洲起义后囚流西伯利亚，1861年越狱流亡西欧，在第一国际与马克思决裂并著《国家制度和无政府状态》。断言俄国村社与农民暴动传统具天然革命潜能，感召1874年“到民间去”造反派，曾与涅恰耶夫合作旋即痛斥断交。 ‖ `←CON-narodnichestvo`[激进翼奠基|1860s–1870s]: 主张否定国家与依托农民自发暴动的无政府民粹路线。 ； `→CON-narodnichestvo`[revolutionary-wing-founder|1860s–1870s]: 为古典革命民粹主义注入反国家主义、反知识分子精英主义与农民直接行动的“造反派”基因
- **`EVT-1874-going-to-the-people`**（1874年“到民间去”运动与“193人案”大审判）: 1874年夏，数千受巴枯宁（即时起义）与拉夫罗夫（长期宣传）感召的青年知识分子奔赴俄国乡村，遭遇农民同情、听取、戒备或告发等不同反应，也遭警方大规模搜捕；“193人案”于1877年10月至1878年初审理。受挫与审判推动多种组织反思，既有秘密组织与政治恐怖，也有定居宣传和反恐怖路线。 ‖ `←CON-narodnichestvo`[运动转折|1874–1878]: 知识青年下乡宣传遇挫并推动地下组织与策略重整。 ； `→CON-narodnichestvo`[exemplifies|1874–1878]: 1874年运动标志狭义与广义民粹主义在“知识分子向农民赎罪并遭现实否证”中的历史碰撞。
- **`ORG-zemlya-i-volya`**（土地与自由社）: 本卡聚焦1876—1879年第二代土地与自由社（纳坦松、米海洛夫、普列汉诺夫等组建），须与1861—1864年无法人承续的同名第一代严格区分。该社借农村定居宣传吸纳“到民间去”挫败教训，后在政府镇压下因恐怖路线与农村工作之争于1879年夏秋分裂为民意党与黑土重分派。 ‖ `←CON-narodnichestvo`[运动载体|1876–1879]: 整合 1870 年代地下民粹派，并于 1879 年一分为二。 ； `→CON-narodnichestvo`[movement_carrier|1876–1879]: 狭义“向农民学习”转向组织化秘密社团的过渡载体，体现民粹派内部路线多极性
- **`ORG-narodnaya-volya`**（民意党）: 1879年夏秋自土地与自由社分裂产生的俄国激进民粹派秘密政党，由执行委员会实行集中地下领导。该党虽以政治刺杀挑战沙皇专制并在1881年3月炸死亚历山大二世，其1879年纲领与致新皇信仍明确诉诸立宪会议与普选自由，绝非纯虚无暗杀团伙；1883年前后国内中枢瓦解。 ‖ `←CON-narodnichestvo`[组织分化|1879–1887]: 转向政治恐怖与沙皇暗杀，同时保留宪制代表制纲领。 ； `→CON-narodnichestvo`[radical-political-turn|1879-1887]: 突破古典民粹派“反政治”教条，将推翻专制与召开立宪会议纳入民粹社会主义纲领。
- **`ORG-chernyi-peredel`**（黑土重分派）: 1879年沃罗涅日分裂后由普列汉诺夫、查苏利奇、阿克雪里罗得、捷伊奇等组建的民粹派组织，反对以刺杀沙皇取代群众农村工作，主张村社经济鼓动与地方“经济恐怖”。1880年初彼得堡印刷所被抄后骨干流亡瑞士，成为1880—1883年间俄国部分民粹派向马克思主义过渡的关键桥梁。 ‖ `←CON-narodnichestvo`[组织分化|1879起]: 坚持土地宣传与经济—社会革命，反对民意党政治恐怖。 ； `→CON-narodnichestvo`[orthodox_populist_wing|1879–1881]: 保留古典民粹派反政治主义与“向群众学习”传统，但很快因国内崩溃而向工人转向
- **`EVT-1881-03-assassination-of-alexander-ii`**（1881年刺杀亚历山大二世与“三月一日案”）: 1881年3月1日[O.S.]/13日[N.S.]，民意党在叶卡捷琳娜运河炸死亚历山大二世，未引发起义。3月8日[O.S.]/20日[N.S.]有限咨询改革被否决；执委会3月10日[O.S.]/22日[N.S.]致信新沙皇后网络覆灭，五人4月3日[O.S.]/15日[N.S.]被绞死。 ‖ `←CON-narodnichestvo`[历史枢轴|1881.03–05]: 刺杀亚历山大二世后政权反扑与民粹派地下组织解体。 ； `→CON-narodnichestvo`[pivots_through|1881.03–05]: “三月一日”宣告依靠少数派暗杀推动社会与农民起义的传统民粹战略触及物理与政治极限。
- **`PER-plekhanov`**（格奥尔基·普列汉诺夫）: “俄国马克思主义之父”。1879年拒恐怖另立土地平分社，1883年在日内瓦创劳动解放社奠定两阶段革命论；1901年首创社民“山岳派”隐喻，1903二大助列宁裁撤老编委又于11月倒向马尔托夫，1905后斥“不该拿起武器”；一战与1917办《统一报》极右护国并坚决反对十月夺权。 ‖ `←CON-narodnichestvo`[马克思主义批评者|1883–1895]: 从黑土重分派转向马克思主义，借“现实理性”批判民粹派。 ； `→CON-narodnichestvo`[chief-marxist-critic|1883-1895]: 以斯宾诺莎—黑格尔式“合理现实”必然论系统批判民粹派跨越资本主义空想，建构正统两阶段革命论。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←CON-narodnichestvo`[广义界定与论战者|1890s起]: 奠定“广义社会学义”界定并批判合法民粹派“经济浪漫主义”。
- **`ORG-psr`**（社会革命党）: 1901年末合并建立的俄国新民粹派政党，以土地社会化纲领与战斗组织暗杀闻名。1917年选民基数居全俄之冠却在战争、分地拖延与左翼分裂中失势；虽夺立宪会议多数仍遭解散，内战“第三条道路”溃于高尔察克政变，1922年莫斯科公审后在国内覆灭。 ‖ `←CON-narodnichestvo`[20世纪继承|1901–1922]: 整合土地社会化与政治恐怖的“新民粹主义”现代政党。
- **`ORG-osvobozhdenie-truda`**（劳动解放社）: 1883年9月（西欧公历）于日内瓦创立的俄国首个马克思主义团体，由普列汉诺夫、查苏利奇、阿克雪里罗得、捷伊奇与伊格纳托夫发起。其译介马恩著作，提出反对布朗基密谋、依托资本主义发展与工人运动的“两阶段革命”正统；1900年底合办《火星报》，1903年二大闭幕并入统一政党。 ‖ `→CON-narodnichestvo`[polemical_antithesis|1883–1900]: 将广义民粹主义（涵盖从70年代革命派到沃龙佐夫、丹尼尔逊）树立为主要论战他者
- **`PER-nechayev`**（谢尔盖·根纳季耶维奇·涅恰耶夫）: 极端密谋革命家。1869年结识巴枯宁，携《革命者教义问答》返俄组建人民惩治社，11-21[O.S.]/12-03[N.S.]伙同社员杀害异议学生伊万诺夫。1871年追随者受审反促革命群体伦理自省；1872年自瑞士引渡回俄，遭沙皇法外敕令终身秘密幽禁，1882年死于要塞。 ‖ `→CON-narodnichestvo`[negative-catalyst|1871–1874]: 1871年审判曝光其欺诈谋杀手段，反向激发柴可夫斯基小组以伦理纯洁性和公开宣传开启“到民间去”运动

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 1 项)
### `DEB-1879-narodnaya-volya-to-bolshevism`：民意党与布尔什维主义：密谋传统的连续性与异质性
## [T1] 核心问题定义
民意党的秘密纪律、职业革命与政治暴力，同后来的布尔什维克组织之间有何关系？争论必须分别考察组织手段、革命目标、道德论证和具体传承链条：相似的地下技术本身不能证明永久党专政或思想一脉相承。

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 自由主义思想史 | Isaiah Berlin, Venturi 英译本导论 (1960) | 承认职业密谋组织形态的先例，强调民粹伦理、个人良知与后来的党专政存在断裂。 | `CLM-berlin-1960-populism-moral-core` | 理想型可能淡化民意党内部的强制与雅各宾倾向。 |
| 政治思想与运动史 | Franco Venturi, *Roots of Revolution* (1960) | 1879年组织分裂源自农村工作困境与策略冲突；民意党融合社会革命和制宪目标，同时保留临时专政的张力。 | `CLM-venturi-1960-lipetsk-voronezh-split`; `CLM-venturi-1960-narodnaya-volya-constitutionalism` | 运动史不等同于完整的思想史；立宪主张的实际执行仍需检验。 |
| 观念社会史与晚年马克思互动 | Andrzej Walicki, *The Controversy over Capitalism* (1969) | 区分民粹主义思潮与组织；1881年马克思复查苏利奇信及草稿承认俄国村社有条件充当社会再生支点，普列汉诺夫的反少数派夺权传统则展示另一条转化路径。 | `CLM-walicki-1969-narodnichestvo-definition`; `CLM-walicki-1969-marx-populist-affinity`; `CLM-walicki-1969-plekhanov-rational-reality` | 思想结构不直接证明组织传承，且对基层参与者关注有限。 |
| 爱尔福特正统重审与雅各宾概念史 | Lars T. Lih, *Lenin Rediscovered* (2006); Robert Mayer (1999) | 正面证伪“特卡乔夫/民意党密谋传统→列宁《怎么办？》”直线谱系：列宁以德国社民党（SPD）公开群众党为理想模板，因警察国家才借用秘密外壳；其“社会民主党雅各宾派”隐喻直接承自普列汉诺夫1901年反机会主义修辞而非特卡乔夫。 | `CLM-lih-2006-erfurtian-merger-formula`; `CLM-lih-2006-textbook-myth-critique`; `CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism` | 还原1901–1902年正统语境并不能消解1903年后真实发生的组织集权裂变。 |
| 自由主义制度批判 | Richard Pipes, *The Russian Revolution* (1990) | 其关于激进知识分子与家产专制国家对立、布尔什维克夺权及恐怖的论证，提供长期政治文化比较视角。 | `CLM-pipes-1990-patrimonial-state-and-intelligentsia`; `CLM-pipes-1990-october-classic-coup` | 将不同年代政治目标与组织条件回溯拉平的风险。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 13/13 条)
- **`CLM-berlin-1960-populism-moral-core`** [`SCH-berlin-isaiah`(以赛亚·伯林 · liberal-intellectual-history) | pp. vii-xxvi]: 
- **`CLM-walicki-1969-narodnichestvo-definition`** [`SCH-walicki-andrzej`(安杰伊·瓦利茨基) | pp. 1-9, 23-28 [PDF pp. 13-21, 35-40]]: 
- **`CLM-venturi-1960-lipetsk-voronezh-split`** [`SCH-venturi-franco`(弗朗科·文图里) | pp. 647-663]: 
- **`CLM-venturi-1960-narodnaya-volya-constitutionalism`** [`SCH-venturi-franco`(弗朗科·文图里) | pp. 649, 655, 667-681, 716]: 
- **`CLM-walicki-1969-plekhanov-rational-reality`** [`SCH-walicki-andrzej`(安杰伊·瓦利茨基) | pp. 153-165 [PDF pp. 165-177]]: 
- **`CLM-hildermeier-2000-agrarian-socialism-modernization-dilemma`** [`SCH-hildermeier-manfred`(曼弗雷德·希尔德迈尔) | EPUB版无稳定原书页码；以本地章节与行号定位（ch08 L75–232, ch09 L26–44, ch12 L204–282, ch13 L107–185, ch17 L115–310, ch20 L750–753, ch24 L180–285, ch26 L6–96；epub:main-8.xhtml, main-9.xhtml, main-12.xhtml, main-13.xhtml, main-21.xhtml, main-25.xhtml, main-27.xhtml）]: 
- **`CLM-pipes-1990-patrimonial-state-and-intelligentsia`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 2 (Official Russia); ch. 4 (The Intelligentsia); cf. Introduction]: 
- **`CLM-walicki-1969-marx-populist-affinity`** [`SCH-walicki-andrzej`(安杰伊·瓦利茨基) | pp. 132-133, 179-194 [PDF pp. 144-145, 191-206]]: 
- **`CLM-hildermeier-2000-psr-terror-vs-mass-party-dualism`** [`SCH-hildermeier-manfred`(曼弗雷德·希尔德迈尔) | EPUB版无稳定原书页码；以本地章节与行号定位（ch07 L10–141, ch10 L92–96, ch11 L1–70, ch15, ch21 L12–39, ch24 L86–176；epub:main-7.xhtml, main-10.xhtml, main-11.xhtml, main-25.xhtml）]: 
- **`CLM-lih-2006-erfurtian-merger-formula`** [`SCH-lih-lars`(拉斯·T·利) | pp. 6-9, 41-49, 74-106, 113-121, 556-557]: 
- **`CLM-lih-2006-textbook-myth-critique`** [`SCH-lih-lars`(拉斯·T·利) | pp. 5, 13-33, 555]: 
- **`CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism`** [`SCH-mayer-robert`(罗伯特·迈耶) | pp. 127-129, 140-146]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 4 条，另有 1 条 L3 逐日细节见 `timeline/L3_daily/`)
- **1861-02-19 [O.S.] / 1861-03-03 [N.S.]** (`TL-W15-L1-E01-01`, L1): **废除农奴制宣言** — 人身解放与赎买、村社安排并存，土地问题成为革命政治的长期轴心。
- **1863-01-13 [N.S.]** (`TL-W15-L1-E01-02`, L1): **《怎么办？》连载** — 车尔尼雪夫斯基的新人伦理影响激进知识界；思想传播不能直接等同组织继承。
- **1869-11-21 [O.S.] / 1869-12-03 [N.S.]** (`TL-W15-L1-E01-03`, L1): **伊万诺夫被杀** — 涅恰耶夫案暴露密谋纪律与革命伦理的冲突。
- **1874-01-13 [N.S.]** (`TL-W15-L1-E01-04`, L1): **到民间去运动** — 春夏农村宣传及大规模逮捕促成策略反思，各地农民反应不宜一概而论。
