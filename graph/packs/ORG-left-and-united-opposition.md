# 1-Hop 去重平衡上下文包：`ORG-left-and-united-opposition`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`ORG-left-and-united-opposition`** (1923–1927年左翼反对派与托季联合反对派 | `cards/organizations/ORG-left-and-united-opposition.md` | `multi-perspective`): 已覆盖=`biographical-deutscher, institutional-carr, economic-history-erlich, conscience-daniels, archival-khlevniuk, leningrad-worker-social-zhukov`；待补=`factory-grassroots-opposition-networks`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1923年剪刀差危机触发的托洛茨基—普列奥布拉任斯基“左翼反对派”，经1926年春与季诺维也夫—加米涅夫“新反对派”结盟为托季联合反对派；以《四十六人声明》与《1927年政纲》批判官僚体制与“一国社会主义”、主张价格—财政渠道的计划工业化，于1927年12月十五大被组织摧毁。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **1923年《四十六人声明》与左翼反对派成型（1923.10–1925.04）**：
  - `1923-10-08` 托洛茨基致信中央委员会与中监委，指控经济失调与书记处官僚体制恶化（`CLM-carr-1954-platform-of-46-economic-roots`）。
  - `1923-10-15` **《四十六人声明》** 递交政治局：中央党务档案馆藏俄文两份打字稿原本共载 **47人次签名**（因 **阿·戈尔茨曼 A. Goltsman** 在两份打字稿重复联署，实际为皮达可夫、普列奥布拉任斯基、谢列布里亚科夫、奥新斯基等 **46位独立联署干部**；托洛茨基本人未签署），先诊断切尔文危机、信贷紧缩与剪刀差滞销，继而批判“多数派派别专政”压制党内讨论（Carr `pp. 113–115`）。1924年普列奥布拉任斯基提出“社会主义原始积累规律”，主张在NEP市场框架下靠价格与税收杠杆加速国营工业投资（`CLM-erlich-1960-preobrazhensky-dilemma`）。
- **1925年列宁格勒转向与1926年托季联合反对派（1925.09–1927.06）**：
  - 1925年十四大季诺维也夫—加米涅夫“新反对派”战败并失去列宁格勒基地（`MTG-1925-12-14th-party-congress`, `CLM-zhukov-zinoviev-1925-leningrad-opposition`）；`1926-04` 托派与季加派正式结成 **联合反对派**，围绕工业化资金积累、富农分化、党内民主、中国革命及“一国建成社会主义”与斯大林—布哈林多数派展开全线论战（`CLM-deutscher-1959-united-opposition-defeat`, `CON-socialism-in-one-country`）。
- **《1927年政纲》、十周年街头抗争与十五大终结（1927.07–12）**：
  - `1927-09` 反对派拟定《布尔什维克列宁主义者政纲》（《1927年政纲》）遭政治局禁止印发后转入地下油印；`1927-11-07` 十周年纪念日在莫斯科、列宁格勒街头独立游行遭冲散；`1927-11-14` 托洛茨基、季诺维也夫被开除党籍；`1927-12-18—19` 联共十五大另行开除加米涅夫、普列奥布拉任斯基等75名骨干，季、加一翼递交悔过书而托洛茨基一翼拒降流放，联合反对派就此瓦解（`MTG-1927-12-15th-party-congress`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-trotsky` | `principal-leader` | 1923–1927 | 左翼反对派政治核心，1926年起与季诺维也夫共领联合反对派，拒签悔过书后流放 | `CLM-deutscher-1959-united-opposition-defeat`; `CLM-carr-1954-platform-of-46-economic-roots` |
| `PER-preobrazhensky` | `chief-economic-theorist` | 1923–1927 | 《四十六人声明》起草主力与《新经济学》作者，论证靠价格—税收而非暴力剥夺积累工业资本 | `CLM-erlich-1960-preobrazhensky-dilemma`; `PER-preobrazhensky` |
| `PER-zinoviev` | `adversary-1923 -> co-leader-1926` | 1923–1925反托；1926–1927结盟 | 十四大失守列宁格勒后携残余组织网络与托洛茨基结盟，十五大闭幕际悔过拆伙 | `CLM-zhukov-zinoviev-1925-leningrad-opposition`; `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-stalin` | `organizational-adversary` | 1923–1927 | 凭书记处干部任命权、报刊垄断与反派别纪律逐级剥夺反对派合法空间 | `CLM-khlevniuk-2015-secretariat-and-nomenklatura`; `CLM-khlevniuk-2015-collective-leadership-erosion` |
| `PER-bukharin` | `theoretical-adversary-1924-1927` | 1924–1927 | 代表多数派批判普列奥布拉任斯基“超工业化”危及工农市场联盟 | `CLM-erlich-1960-preobrazhensky-dilemma`; `DEB-1928-bukharin-alternative` |
| `CON-socialism-in-one-country` | `central-ideological-target` | 1925–1927 | 联合反对派批判该口号割裂世界革命并掩盖民族官僚保守化 | `DEB-1924-socialism-in-one-country` |
| `POL-ban-on-factions-1921` | `legal-constraint` | 1923–1927 | 1921年十大派别禁令将政纲散发直接定性为非法地下反党活动 | `POL-ban-on-factions-1921`; `CLM-apalkov-2023-collective-to-personal-dictatorship` |
| `MTG-1927-12-15th-party-congress` | `defeated-at` | 1927-12 | 十五大追认开除托、季并另开除75名骨干，终结联合反对派组织存在 | `MTG-1927-12-15th-party-congress` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1923–1927年存在自《四十六人声明》至托季结盟的党内左翼—联合反对派；主张计划工业化、累进抽取富农余力、恢复党内民主并批判“一国社会主义”；1927年底在组织上被彻底清除。
- **主要解释分歧**（详参 `DEB-1924-socialism-in-one-country`, `DEB-1922-lenin-testament-and-stalin-rise`, `DEB-1928-bukharin-alternative`）：
  - **[工业化经济思想史 / Alexander Erlich]**（`CLM-erlich-1960-preobrazhensky-dilemma`）：严格划清普列奥布拉任斯基工业化方案与1929年斯大林强制集体化的制度边界——普氏理论预设NEP个体小农市场混合经济存续数十年，仅靠国营工业不等价定价与税收调节积累，并受农民罢卖退回自然经济的弹性硬约束，绝非斯大林式暴力没收与流放。
  - **[托派传记与社会心理论 / Isaac Deutscher]**（`CLM-deutscher-1959-united-opposition-defeat`, `CLM-deutscher-1959-disarmed-prophet-paradox`）：失败主因在于内战后全国工农的疲惫沉寂（“可怕的寂静”）及反对派自身效忠一党垄断、不敢诉诸党外群众。
  - **[经济—政治结构史 / E. H. Carr]**（`CLM-carr-1954-platform-of-46-economic-roots`, `CLM-carr-1954-scissors-crisis-mechanics`）：强调《四十六人声明》首先是对1923年剪刀差与信贷危机的严肃政策诊断，党内民主诉求从属于经济路线转向需求。
  - **[反对派良心系谱 / Robert V. Daniels]**（`RN-W1C-communist-oppositions-1918-1929`）：将1923–1927年反对派归入布尔什维克内部理想主义原则派对官僚实用主义的周期性抗争。
  - **[后苏联档案制度派 / Oleg Khlevniuk; Dmitry Apalkov]**（`CLM-khlevniuk-2015-collective-leadership-erosion`, `CLM-apalkov-2023-collective-to-personal-dictatorship`）：指出反分裂戒律使党内合法反对派成为制度悖论，但1927年底胜利仍属政治局多数联盟而非斯大林个人独裁终局。

## 2. 一跳邻域全量微摘要目录 (去重后共 30 个节点，0 截断)
- **`CON-democratic-centralism-and-vanguard`**（先锋队党与民主集中制）: 布尔什维克组织原则的跨期复合概念：从民意党集中制与特卡乔夫“自觉少数”，经1902年职业革命家论、1905–1906年成文的民主集中制及1917年群众政党，至1921年禁派令与斯大林书记处官职名册制，派别空间收缩；部分制度史研究强调干部任命权日益压过民主原则。 ‖ `→ORG-left-and-united-opposition`[targeted-under-label "factionalism"|1923–1927]: “四十六人”与联合反对派均以“派别活动、违反民主集中制”被定罪、开除
- **`CON-kulak`**（富农（作为社会阶层与政治定罪标签））: “富农”兼具农村阶层与政治定罪含义：19世纪原指高利贷盘剥者，列宁称农村资产阶级；斯托雷平改革分离户也遭村社如此指斥。1918年为贫农委员会征粮对象，1925年NEP放宽而农村趋向中农化；1928–1929年经刑法107条与雅科夫列夫委员会转为阶级清洗标签。 ‖ `→ORG-left-and-united-opposition`[advocate-of-forced-grain-loan-and-progressive-tax|1926–1927]: 主张向约10%富裕富农阶层强制征借1.5亿普特粮食资助工业化，但未主张192…
- **`CON-thermidor-and-bureaucracy`**（苏维埃热月与官僚主义蜕变）: 借法国大革命雅各宾衰亡隐喻诊断苏维埃政权变质的核心概念。1921–1923年列宁晚年痛斥国家机关实质承袭沙皇旧机器、仅涂苏维埃油漆；路标转换派乌斯特里亚洛夫从右翼欢呼NEP为民族布尔什维克“热月”；1923–1927年左翼与联合反对派则以“党国官僚中间派与热月危险”批判斯大林—布哈林体制。 ‖ `→ORG-left-and-united-opposition`[systematized-class-sociology-of-party-apparatus-in|1926-04–1927-12]: 在1927年政纲中以车间工人仅占31%的数据论证“党被自身机关取代”，要求恢… ； `←ORG-left-and-united-opposition`[diagnosed-and-shattered-by|1923-1929]
- **`EVT-1923-scissors-crisis`**（1923年剪刀差危机与四十六人声明）: 1923年工业品高价、农产品低价与信贷收缩叠加，造成滞销、欠薪及工人抗议，动摇新经济政策的城乡交换。托洛茨基致中央信与四十六人声明分别把经济失衡同党内机关体制相联；价格随后收拢，民主改革争论却在列宁缺席和继承权竞争中转成纪律斗争。 ‖ `→ORG-left-and-united-opposition`[early_opposition_formation|1923.10—1924.01]: 反对派开始集结，不等于1926—1927年联合反对派已成立
- **`EVT-1927-war-scare-and-opposition-expulsion`**（1927年“战争恐慌”危机与联合反对派溃败）: 1927年英苏断交、沃伊科夫遇刺引发战争恐慌与抢购囤粮，OGPU六月行动大捕人：两项研究分别估6月至少9,000人、6—7月至少13,345人。反对派九月《政纲》遭禁，11月7日游行被冲散，14日托季被开除；十五大在购粮危机已发生时完成组织清除。 ‖ `→ORG-left-and-united-opposition`[expelled|1927.09–12]: 在发布九月《政纲》和十周年街头抗议受挫后遭到全盘开除，随即于12月10日分裂…
- **`INS-politburo-orgburo-secretariat`**（联共（布）中央政治局—组织局—书记处与官职等级名册制）: 1919年3月俄共八大后常设政治局、组织局与书记处，分掌政治决策、组织行政及日常党务人事。1922年4月斯大林任总书记后逐步控制议程、秘密文件分发与干部名册调配。经1924年七人小组协调、1925—1929年联盟重组与纪律整肃，托洛茨基、季诺维也夫、布哈林先后退出决策核心。 ‖ `→ORG-left-and-united-opposition`[isolated_and_expelled_by|1923–1927.12]: 先后遭1924年“七人小组”与1926–1927年重组后政治局多数援引十大统…
- **`INS-rabkrin-and-ccc`**（中央监察委员会与工农检查人民委员部（联合工作体制））: 工农检查人民委员部是国家监察机关，中监委是党的纪律监督机关。1923年改组后共同领导、联合办公，仍为两个机构，未在法律上合并；列宁的合并设想及Carr、Lewin的叙述用语须与此区分。改革旨在改善官僚机器、维护中央团结，联合机构随后参与党内审查处分，监督亦受权力关系制约。 ‖ `→ORG-left-and-united-opposition`[investigated_and_disciplined|1926–1927]: 中监委参与党纪调查，重大处分由相关党机关决定
- **`MTG-1924-05-13th-party-congress`**（俄国共产党（布尔什维克）第十三次代表大会）: 1924年5月23日至31日，列宁逝世后的首次党代会召开。会前中央全会与长老会议限制列宁最后口授文件传达方式并留任斯大林；大会依托“列宁征召”与组织筛选压倒左翼反对派，托洛茨基公开宣示对党忠诚。会后中央与中监委扩编、布哈林升入政治局，集体领导联盟暂时稳固。 ‖ `→ORG-left-and-united-opposition`[excluded-from-voting-seats|1924-05]: 在十三大748名有表决权代表中获0席，被全票追认定性为“小资产阶级倾向”。
- **`MTG-1925-12-14th-party-congress`**（联共（布）第十四次代表大会）: 1925年12月18—31日莫斯科举行。斯大林—布哈林中央多数派以559:65通过批准中央政治报告决议案，击败以列宁格勒产业工人党员为后盾、批判富农分化与“国家资本主义”的季诺维也夫—加米涅夫“新反对派”；大会确立社会主义工业化总方针并改党名为联共（布）。 ‖ `→ORG-left-and-united-opposition`[precursor-convergence|1925-12 -> 1926-04]: 列宁格勒新反对派在十四大溃败直接促成1926年春与托洛茨基派合并为托季联合反对派
- **`MTG-1927-12-15th-party-congress`**（联共（布）第十五次代表大会）: 1927年12月2—19日莫斯科举行。大会追认11月对托洛茨基、季诺维也夫的开除党籍处分，并于12月18日另行开除加米涅夫等75名托季联合反对派骨干及萨普罗诺夫派；同时通过编制首个五年计划指示与渐进合作化—集体化决议，开启NEP末期转折前奏。 ‖ `→ORG-left-and-united-opposition`[liquidated-at|1927-12-18]: 大会开除75名骨干并促发季—托两翼分裂，联合反对派作为党内有组织联盟终结 ； `←ORG-left-and-united-opposition`[defeated-at|1927-12]
- **`ORG-bolsheviks-rcpb-vkpb`**（布尔什维克派—俄共（布）—联共（布））: 布尔什维克起于1903年社民工党二大后的党内多数派，经流亡、地下活动与1917年群众扩张成为执政党；1918年称俄共（布），1925年称联共（布）。它从地方主动性较强的革命党，演变为拥有任命网络与纪律制裁的党国核心，过程分阶段且存争议。 ‖ `→ORG-left-and-united-opposition`[internal-opposition|1923–1927]: 1927年遭十五大排斥
- **`ORG-democratic-centralists`**（民主集中派）: 民主集中派是1919年初结成的布尔什维克党内反对派，萨普罗诺夫、奥新斯基、弗·斯米尔诺夫等为重要代表，批评以任命和行政命令取代集体领导与基层参与。成员及立场随时间变化：1923年部分人联署《四十六人声明》；后期“十五人集团”须与早期派别区分。 ‖ `→ORG-left-and-united-opposition`[distinct-oppositions|1926–1927]: 判断政权性质与托洛茨基等联合反对派不同
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←ORG-left-and-united-opposition`[principal-leader|1923–1927] ； `→ORG-left-and-united-opposition`[principal-leader|1923-10–1927-12]: 1923-10-08独立致信中央与10-15《四十六人声明》同步发难；192…
- **`PER-preobrazhensky`**（叶夫根尼·普列奥布拉任斯基）: 老布尔什维克经济理论家，1920–1921年任中央书记。1923年起草《四十六人声明》批判书记等级制；1924–1926年提出社会主义原始积累，以价格税收而非行政暴力向私营部门筹资，与布哈林论战。1928–1929年误判斯大林工业化转向而脱离托派求和，1937年被处决。 ‖ `←ORG-left-and-united-opposition`[chief-economic-theorist|1923–1927]
- **`PER-zinoviev`**（格里戈里·季诺维也夫）: 老布尔什维克、共产国际首任主席（1919–1926）。1917年十月公开反对武装起义；1920年哈雷演说力推二十一条与阶级恐怖，1923年豪赌“德国十月”并首倡社民党“法西斯羽翼”论；借“三驾马车”排托后于1925年发起新反对派，1926年7月首因秘密第7条被逐出政治局，1927年底被开除后屈服。 ‖ `←ORG-left-and-united-opposition`[adversary-1923 -> co-leader-1926|1923–1925反托；1926–1927结盟]
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←ORG-left-and-united-opposition`[organizational-adversary|1923–1927]
- **`PER-bukharin`**（尼古拉·布哈林）: 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。 ‖ `←ORG-left-and-united-opposition`[theoretical-adversary-1924-1927|1924–1927]
- **`CON-socialism-in-one-country`**（一国建成社会主义）: 苏联核心战略概念（1924–1930s）。1924年底由斯大林反击“不断革命论”时首次提出，1925–1926年经布哈林充实为区分“国内建成可能”与“免除外部颠覆之最终胜利”的理论，支撑新经济政策工农市场渐进建设；1928–1929年后内涵剧变为自给自足备战超工业化与强制集体化的动员纲领。 ‖ `←ORG-left-and-united-opposition`[central-ideological-target|1925–1927]
- **`POL-ban-on-factions-1921`**（《关于党的统一》派别禁令）: 俄共十大于1921年3月16日通过《关于党的统一》，要求解散按纲领组成的派别，并保留规定渠道的批评。秘密第七条设中央领导成员的特殊处分程序；1924年1月公开宣读、1926年7月首次动用开除季诺维也夫出政治局，危机措置遂渐成约束反对派的工具，但不同年份执行不等同原条文。 ‖ `←ORG-left-and-united-opposition`[legal-constraint|1923–1927] ； `→ORG-left-and-united-opposition`[制度约束对象|1923–1927]: 左翼与联合反对派的申诉和联合在反派别框架下被定性违纪。
- **`PER-chayanov`**（亚历山大·恰亚诺夫）: 苏俄农业经济学家、“组织—生产学派”领袖（1888–1937）。提出家庭小农“劳动—消费均衡”与“人口分化”模型，主张以“纵向合作化”而非强制集体化整合小农。1923年1月送交列宁的合作社书目包含其著作；1929年12月遭斯大林点名痛批，后陷“劳动农民党”冤案，1937年被处决。 ‖ `→ORG-left-and-united-opposition`[targeted_as_kulak_agent_by|1925–1927]: 在1927-09《联合反对派政纲》中被指控为围绕右倾领导层宣扬乌斯特里亚洛夫…
- **`PER-kalinin`**（米哈伊尔·加里宁）: 特维尔贫农与彼得堡车工出身的苏维埃名义元首（1875–1946）。1919年接替斯维尔德洛夫任全俄（后苏联）中执委主席，借粮食税与农村巡讲维系“工农联盟”门面；1926年入政治局，1928年私下同情布哈林，据布哈林述称在七月斗争中转附斯大林，保住其“全苏家长”象征地位。 ‖ `→ORG-left-and-united-opposition`[labeled_rightist_protector_by|1927-09]: 在1927-09《联合反对派政纲》中被明确点名为李可夫周围传导富裕中农利益的…
- **`PER-kirov`**（谢尔盖·基洛夫）: 基洛夫是北高加索与巴库布尔什维克领导人，早年主政阿斯特拉罕及巴库。1926年1月十四大后奉斯大林之命赴列宁格勒，逐厂辩论，夺取党机关与报刊控制，1926–1927年持续争夺基层；1926年7月成为政治局候补委员，1928–1929年反右倾斗争中稳控西北工业重镇。 ‖ `→ORG-left-and-united-opposition`[suppressor_in_leningrad|1926.01–1927.12]: 粉碎列宁格勒反对派基层支部串联及1927年11月7日十周年庆典街头公开抗议
- **`PER-kondratiev`**（尼古拉·康德拉季耶夫）: 苏俄农业经济学家与长波周期理论创立者（1892–1938）。1917年10月任临时政府粮食部副部长；1920年起执掌财政部景气研究所，在计划方法论战中代表“发生学派”反对高指标目的论，主张依托市场均衡与农产出口推进工业化。1928年被打为“康德拉季耶夫主义”撤职，1938年遇害。 ‖ `→ORG-left-and-united-opposition`[targeted_as_ustryalovite_by|1925–1927]: 被1927-09《联合反对派政纲》指认为在各州县享有实权并替富裕农民代言的头…
- **`PER-krupskaya`**（娜杰日达·克鲁普斯卡娅）: 娜杰日达·克鲁普斯卡娅（1869–1939），布尔什维克元老、列宁夫人兼秘密通信枢纽；1918年后主持教育人民委员部成人政教与扫盲，1922–1923年守护列宁病榻口授并于1924年5月移交十三份文件。1925–1926年短暂参与反对派后脱离，晚年转入教育制度工作。 ‖ `→ORG-left-and-united-opposition`[brief-signatory|1926.07–1926.10]: 签署1926年7月《十三人声明》，随即因忌惮党内公开分裂于同年秋退出反对派
- **`PER-lunacharsky`**（阿纳托利·卢那察尔斯基）: 俄国革命文艺理论家、首任苏俄教育人民委员（1875—1933）。早年与波格丹诺夫、高尔基共倡“造神说”并组前进派党校；1917年随区联派入布尔什维克，十月后长期主持教育与文化事业，在保护旧知识分子、实验教育与激进派间力求平衡；1929年大转变高潮中辞职，1933年病逝法国。 ‖ `→ORG-left-and-united-opposition`[ambiguous-cultural-interlocutor|1923–1927]: 未加入党内政治反对派，但在1920年代宽容多元文艺空间内与托洛茨基等人在反对…
- **`PER-ordzhonikidze`**（格里戈里·“谢尔戈”·奥尔忠尼启则）: 外高加索布尔什维克领导人，1912年任中委，1922年格鲁吉亚事件中殴打党员引列宁震怒。1926年11月兼任中监委主席与工农检查人民委员，两机构联合办公而非合并，主持处分托季派；1928–1929年农业政策倾向斯大林，仍求集体领导调和，密会传单曝光后转而追责右派。 ‖ `→ORG-left-and-united-opposition`[lenient_mediator -> expeller|1926.11–1927.12]: 初任中监委主席时复审恢复57名被开除党员党籍，联合反对派逾越公开示威红线后遂…
- **`PER-radek`**（卡尔·拉狄克）: 加利西亚犹太社会主义者与多语政论家，活动横跨波兰、德国和俄国。参与齐美尔瓦尔德左派、布列斯特争论与德国革命，后任共产国际要员，推动统一战线并卷入德国十月失败问责。作为左翼反对派及中国革命论战骨干，1927年遭开除，1929年转向妥协归队；1937年获刑，1939年狱中被害。 ‖ `→ORG-left-and-united-opposition`[writer_and_organizer|1923–1927]: 为左翼及联合反对派辩护，十五大遭开除并流放
- **`PER-rakovsky`**（克里斯蒂安·拉柯夫斯基）: 巴尔干国际主义者与苏维埃政治家（1873—1941）。1919—1923年任乌克兰人民委员会主席，由反对单定乌语为国语转向力捍共和国自治，1923年十二大推动“本土化”妥协。后任驻英法大使与联合反对派核心，1928年流放撰《论职业危险》剖析执政异化风险，1941年在奥廖尔被处决。 ‖ `→ORG-left-and-united-opposition`[core-leader|1926–1929]: 联合反对派关键领袖，十五大开除后在阿斯特拉罕—巴尔瑙尔流放地领导不妥协派（至…
- **`PER-ustryalov`**（尼古拉·乌斯特里亚洛夫）: 俄国法学家、“路标转换派”与民族布尔什维主义创立者（1890–1937）。曾任高尔察克政府新闻局长，流亡后盛赞新经济政策为革命“热月演进”（外红内白萝卜），号召专家归国促成国家常态化。列宁十一大引述示警，反对派以“乌斯特里亚洛夫主义”攻讦右倾；1935年返苏，1937年遇害。 ‖ `→ORG-left-and-united-opposition`[polemical_foil_used_by|1925–1927]: 联合反对派以“鼓吹乌斯特里亚洛夫学说”把李可夫、布哈林同非党农业专家康德拉季…
- **`PER-yagoda`**（亨里希·雅戈达）: 苏联秘密警察组织者，1923年起任OGPU第二副主席；缅任斯基1926年任主席后因病少理日常事务，雅戈达影响渐增，职衔与实际权力须区分。其机关在战争恐慌、镇压反对派及1928–1929年控制社会中服务大转变；1934–1936年任内务人民委员，1938年公审后被处决。 ‖ `→ORG-left-and-united-opposition`[surveillance-and-suppression|1927]: 对联合反对派的监视、地下印刷所打击

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 3 项)
- **`DEB-1924-socialism-in-one-country`**（一国建成社会主义与不断革命论 | `historiography/debates/DEB-1924-socialism-in-one-country.md` | 流派 `stalin-bukharin, united-opposition, political-intellectual-history, institutional-geopolitics, lenin-cooperative-plan, bonapartism-and-tactical-critique`）：欧洲革命迟滞后，苏联能否凭国内力量建成社会主义，还是生产力与世界市场的联系使最终完成有赖国际革命？争论中的建设、建成和免于复辟并非同一问题；工农联盟、外部安全及党内联盟变化又如何改变这些概念的政治意义？各方均主张建设，分歧在条件、界限与国际前景。
- **`DEB-1922-lenin-testament-and-stalin-rise`**（列宁晚年、格鲁吉亚事件与斯大林崛起机制 | `historiography/debates/DEB-1922-lenin-testament-and-stalin-rise.md` | 流派 `revisionist, nationalities-history, archival-post-soviet, kotkin-source-skepticism, trotskyist, service-critical-biography, sakharov-pseudo-lenin-polemic`）：列宁晚年口授文稿和格鲁吉亚冲突，是反官僚与反斯大林的总体“最后斗争”，还是对共同集权框架内具体做法的修正？《遗嘱》本身是否存在文本流转疑点？斯大林的上升又如何由个人策略、书记处机关、寡头集体领导与反对派失策共同解释？
- **`DEB-1928-bukharin-alternative`**（布哈林替代方案与新经济政策终结之争 | `historiography/debates/DEB-1928-bukharin-alternative.md` | 流派 `nep-alternative, economic-growth, structural-dilemma, apparatus, ideology-and-mobilization, cliometrics-and-archival-reassessment`）：1927至1929年粮食危机与新经济政策的瓦解，是否意味着渐进工业化和工农联盟已无可行出路，还是党内权力与政策选择扼杀了布哈林的替代方案？投资、价格、农民供粮和政治动员之间的约束究竟有多强，必须把经济可行性、政治可行性与实际权力斗争分别检验。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/43 条)
- **`CLM-carr-1954-platform-of-46-economic-roots`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 113-115, 374-375]: 
- **`CLM-erlich-1960-preobrazhensky-dilemma`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 34-36, 40-41, 49-51, 170-171 (PDF pp. 51-53, 57-58, 66-68, 185-186)]: 
- **`CLM-zhukov-zinoviev-1925-leningrad-opposition`** [`SCH-zhukov-yuri`(尤里·茹科夫) | EPUB OPS/ch1-20.xhtml, OPS/ch1-21.xhtml (Notes 434-462)]: 
- **`CLM-deutscher-1959-united-opposition-defeat`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | （中译本；对应第二部 1926–1927 年）]: 
- **`CLM-khlevniuk-2015-secretariat-and-nomenklatura`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（In Lenin's Shadow，GENERAL SECRETARY 至 1923 年 9 月组织局安排）；制度总论见 ops/xhtml/ch01a.html。工作区文本无纸质页码。]: 
- **`CLM-khlevniuk-2015-collective-leadership-erosion`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（TRYING OUT COLLECTIVE LEADERSHIP 至 THE CHOICE）。工作区文本无纸质页码。]: 
- **`CLM-apalkov-2023-collective-to-personal-dictatorship`** [`SCH-apalkov-dmitry`(德米特里·阿帕尔科夫 · post-soviet-archival-party-history) | pp. 20-33, 124-127, 149-158, 191-195]: 
- **`CLM-deutscher-1959-disarmed-prophet-paradox`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | （中译本无独立纸页；对应第二部 1923 年争论章）]: 
- **`CLM-carr-1954-scissors-crisis-mechanics`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 17, 29-30, 95-96, 100-101, 105-107, 127]: 
- **`CLM-deutscher-1959-alma-ata-bukharin-stalin-split`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | （中译本；对应第二部 1928 年阿拉木图章）]: 
- **`CLM-shlapentokh-french-revolution-burden-jacobin-thermidor`** [`SCH-sinanoglou-ioannis`(约安尼斯·西纳诺格鲁) | pp. 30-31, 35-38 (cf. Sinanoglou 1980, pp. 580-583; Deutscher 1959, ch25-ch26)]: 
- **`CLM-bukharin-stalin-1925-one-country-internal-forces`** [`SCH-stalin-iosif`(约瑟夫·维萨里奥诺维奇·斯大林 · participant-primary-text) | 汇编 PDF pp. 38–40、85–90、113–115；《斯大林全集》页码仅按宿主转引，本卡未回核]: 
- **`CLM-trotsky-1905-december-uprising-lessons-and-permanent-revolution-defense`** [`SCH-trotsky-leon`(列夫·达维多维奇·托洛茨基 · participant-historian) | 中译书页 ·225·、·278·、·281·–·282·、·292·、·308·、·325·–·328·、·330·、·406·（1922 年俄文第 2 版系统，PDF pp. 229–410）]: 
- **`CLM-zinoviev-trotsky-1926-world-economy-critique`** [`SCH-trotsky-leon`(列夫·达维多维奇·托洛茨基 · participant-historian) | 汇编 PDF pp. 67–68、82–91；季诺维也夫引文自标 1925 年问题，托洛茨基诸段在汇编中无单行本年份与页码]: 
- **`CLM-shlapentokh-bonapartism-fear-against-trotsky`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | p. 370, p. 374 (cf. The Prophet Unarmed ch21#L49-L50, ch22#L114-L175, ch27#L245-L260)]: 
- **`CLM-service-2009-trotsky-political-tactical-blunders`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本引言及第 31–32、37–38 章]: 
- **`CLM-carr-1979-stalin-synthesis-of-russian-backwardness-and-industrialism`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 74–76, 169–172, 186–191]: 
- **`CLM-carr-1976-china-1927-defeat-and-comintern-factionalism`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 345, 348-349, 356, 427-429, 490-491, 497, 620, 623, 626-627]: 
- **`CLM-sakharov-2012-lenin-cooperative-plan-debates`** [`SCH-sakharov-valentin`(瓦连京·萨哈罗夫) | EPUB Ch. 1.3 & Ch. 4.2]: 
- **`CLM-zhukov-zinoviev-comintern-and-1923-germany`** [`SCH-zhukov-yuri`(尤里·茹科夫) | EPUB OPS/ch1-16.xhtml (Notes 338-352)]: 
- **`CLM-lewin-1968-testament-intent`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.10 'If Lenin Had Lived . . .'；列宁原文脚注见 Soch. XLV p. 392；XLIV p. 428]: 
- **`CLM-lewin-1968-georgian-affair-bureaucracy`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.9、Ch.10 与 Appendixes I–III, VII–VIII]: 
- **`CLM-lewin-1968-cooperation-shift`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.8 'Russia between West and East'；列宁原文脚注 Soch. XLV pp. 367, 370, 373, 387–88, 389]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 11 条 L3 逐日细节见 `timeline/L3_daily/`)
