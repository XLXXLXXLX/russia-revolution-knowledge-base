# 1-Hop 去重平衡上下文包：`MTG-1927-12-15th-party-congress`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`MTG-1927-12-15th-party-congress`** (联共（布）第十五次代表大会 | `cards/meetings/MTG-1927-12-15th-party-congress.md` | `multi-perspective`): 已覆盖=`trotskyist-biographical-deutscher, archival-post-soviet-khlevniuk, economic-foundations-carr-davies`；待补=`rural-social-history, delegate-social-history`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1927年12月2—19日莫斯科举行。大会追认11月对托洛茨基、季诺维也夫的开除党籍处分，并于12月18日另行开除加米涅夫等75名托季联合反对派骨干及萨普罗诺夫派；同时通过编制首个五年计划指示与渐进合作化—集体化决议，开启NEP末期转折前奏。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **会前开除与大会分批组织清洗的严格区分（1927.11.14 vs 1927.12.18）**：托洛茨基与季诺维也夫已于会前 `1927-11-14` 被中央委员会与中央监察委员会联席会议直接开除出党（此前 `1927-10-23` 被逐出中央委员会）。`1927-12-02` 十五大开幕时反对派已无正式表决权代表；`1927-12-03` 斯大林作中央政治报告，加米涅夫、拉柯夫斯基等发言遭全场打断；`1927-12-18` 大会正式追认对托、季二人的开除，并**另行宣布开除包括加米涅夫、皮达可夫、拉狄克、拉柯夫斯基、普列奥布拉任斯基在内的75名联合反对派积极分子**，同时开除萨普罗诺夫“民主集中派”（十月集团）23人名单（**严禁将大会开除的“75人”误计为包含会前已被开除的托、季二人在内的总数**；`CLM-deutscher-1959-united-opposition-defeat`）。
- **反对派阵营分裂与“六个月考察期”悔过处置（1927.12.10–19）**：`1927-12-10` 托派与季派因是否声明放弃宣传反对派观点正式破裂；`1927-12-18—19` 季诺维也夫、加米涅夫等提交放弃派别活动并承认违反党纪的悔过声明，但 `1927-12-19` 闭幕大会拒绝立即集体恢复其党籍，规定须以个人身份单独申请并经至少六个月考察；托洛茨基、拉柯夫斯基等拒绝投降，于1928年1月遭流放（`CLM-deutscher-1959-united-opposition-defeat`）。
- **五年计划编制指示、自愿集体化口径与粮食危机潜流（1927.12）**：大会通过李可夫、克尔日扎诺夫斯基主持的**关于编制国民经济第一个五年计划的指示**（系编制原则而非1929年4月最终批准的最高方案），并通过莫洛托夫农村工作报告，提出逐步扩大集体农庄与国营农场、限制富农剥削，但明文仍保留NEP市场交换与自愿入社原则——**不可目的论地混同于1929年底全盘强制集体化与“消灭富农阶级”**。与此同时，大会开会期间（`1927-12-14` 与 `12-24`）中央已两度向产粮区发出催征粮食紧急指示，预示 `1928-01` 非常措施与斯大林—布哈林决裂迫在眉睫。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-left-and-united-opposition` | `liquidated-at` | 1927-12-18 | 大会开除75名骨干并促发季—托两翼分裂，联合反对派作为党内有组织联盟终结 | `CLM-deutscher-1959-united-opposition-defeat`; `ORG-left-and-united-opposition` |
| `PER-trotsky` | `expulsion-ratified` | 1927-11-14开除；12-18追认 | 会前已被开除党籍，十五大予以追认并拒绝妥协，次年1月流放阿拉木图 | `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-zinoviev` | `expulsion-ratified -> recantation` | 1927-11至12-19 | 会前开除，大会闭幕际与加米涅夫提交悔过书，被勒令经六个月考察再个别审理 | `CLM-deutscher-1959-united-opposition-defeat`; ` Zhukov ch21` |
| `PER-kamenev` | `expelled -> recantation` | 1927-12-18至12-19 | 列入大会开除的75人名单，随即联署悔过声明与托洛茨基派决裂 | `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-stalin` | `leader` | 1927-12 | 主导彻底清除左翼反对派，会后一中全会以口头请辞总书记试探并强化政治局核心顺从 | `CLM-khlevniuk-2015-collective-leadership-erosion` |
| `POL-first-five-year-plan` | `directives-adopted-at` | 1927-12 | 大会通过编制首个五年计划的框架性指示，尚带工农平衡约束而非1929年高指标定稿 | `POL-first-five-year-plan`; `DEB-1928-bukharin-alternative` |
| `POL-nep` | `policy-context` | 1927-12 | 表面重申NEP框内渐进合作化，实则同期秋冬季粮食收购危机已在掏空市场交换基础 | `DEB-1928-bukharin-alternative`; `DEB-1929-collectivization-and-dekulakization-causes` |

### 2.3 史学争鸣光谱
- **经验共识**：大会追认开除托洛茨基与季诺维也夫、另行开除75名托季反对派及萨普罗诺夫集团，通过编制一五计划指示及渐进农业合作化/集体化决议。
- **主要解释分歧**（详参 `DEB-1928-bukharin-alternative`, `DEB-1929-collectivization-and-dekulakization-causes`）：
  - **[传记与社会气氛论 / Isaac Deutscher]**（`CLM-deutscher-1959-united-opposition-defeat`）：指出十五大对反对派的粉碎不仅靠代表遴选机器，更根源于革命疲惫下全国工农的“可怕寂静”与反对派自我束缚于一党纪律之内。
  - **[后苏联政治局制度史 / Oleg Khlevniuk]**（`CLM-khlevniuk-2015-collective-leadership-erosion`）：强调1927年12月清除左翼后，斯大林在 `1927-12-19` 新选中央一中全会上以“列宁遗嘱任务已履行、请求免去总书记”作试探获布哈林、李可夫一致挽留，但政治局寡头共治要到1928—1929年击溃右派后才最终瓦解。
  - **[计划经济与农村史分期论 / Carr & Davies; Cohen]**（`CLM-carr-davies-1969-nemchinov-table-critique`, `CLM-cohen-1973-nep-viability`）：反对苏联教科书将十五大直接等同于“全盘集体化代表大会”，强调十五大文本仍规定农业集体化须建立在自愿与机器物质技术基础之上，与1929年底行政强推存在重大政策断裂。

## 2. 一跳邻域全量微摘要目录 (去重后共 12 个节点，0 截断)
- **`CON-thermidor-and-bureaucracy`**（苏维埃热月与官僚主义蜕变）: 借法国大革命雅各宾衰亡隐喻诊断苏维埃政权变质的核心概念。1921–1923年列宁晚年痛斥国家机关实质承袭沙皇旧机器、仅涂苏维埃油漆；路标转换派乌斯特里亚洛夫从右翼欢呼NEP为民族布尔什维克“热月”；1923–1927年左翼与联合反对派则以“党国官僚中间派与热月危险”批判斯大林—布哈林体制。 ‖ `→MTG-1927-12-15th-party-congress`[expelled-anti-thermidor-opposition-at|1927-12-02–12-19]: 十五大正式开除联合反对派，党内公开讨论“苏维埃热月”的空间终结
- **`EVT-1927-war-scare-and-opposition-expulsion`**（1927年“战争恐慌”危机与联合反对派溃败）: 1927年英苏断交、沃伊科夫遇刺引发战争恐慌与抢购囤粮，OGPU六月行动大捕人：两项研究分别估6月至少9,000人、6—7月至少13,345人。反对派九月《政纲》遭禁，11月7日游行被冲散，14日托季被开除；十五大在购粮危机已发生时完成组织清除。 ‖ `→MTG-1927-12-15th-party-congress`[culminates_at|1927.12.02–19]: 十五大正式完成对联合反对派的组织清洗，并在秋冬购粮危机已发生之际通过首个五年计划编制指示与农业集体化方针。
- **`ORG-left-and-united-opposition`**（1923–1927年左翼反对派与托季联合反对派）: 1923年剪刀差危机触发的托洛茨基—普列奥布拉任斯基“左翼反对派”，经1926年春与季诺维也夫—加米涅夫“新反对派”结盟为托季联合反对派；以《四十六人声明》与《1927年政纲》批判官僚体制与“一国社会主义”、主张价格—财政渠道的计划工业化，于1927年12月十五大被组织摧毁。 ‖ `←MTG-1927-12-15th-party-congress`[liquidated-at|1927-12-18]: 大会开除75名骨干并促发季—托两翼分裂，联合反对派作为党内有组织联盟终结 ； `→MTG-1927-12-15th-party-congress`[defeated-at|1927-12]: 十五大追认开除托、季并另开除75名骨干，终结联合反对派组织存在
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←MTG-1927-12-15th-party-congress`[expulsion-ratified|1927-11-14开除；12-18追认]: 会前已被开除党籍，十五大予以追认并拒绝妥协，次年1月流放阿拉木图
- **`PER-zinoviev`**（格里戈里·季诺维也夫）: 老布尔什维克、共产国际首任主席（1919–1926）。1917年十月公开反对武装起义；1920年哈雷演说力推二十一条与阶级恐怖，1923年豪赌“德国十月”并首倡社民党“法西斯羽翼”论；借“三驾马车”排托后于1925年发起新反对派，1926年7月首因秘密第7条被逐出政治局，1927年底被开除后屈服。 ‖ `←MTG-1927-12-15th-party-congress`[expulsion-ratified -> recantation|1927-11至12-19]: 会前开除，大会闭幕际与加米涅夫提交悔过书，被勒令经六个月考察再个别审理
- **`PER-kamenev`**（列夫·加米涅夫）: 老布尔什维克、首任全俄中执委主席。1917年自四月至立宪会议一贯坚守温和宪政社会主义联盟路线并公开反对十月起义；1924年十三大联手季诺维也夫压下《列宁遗嘱》，1925年十四大公开发言反斯大林“领袖”集权后失势；1928年7月密会布哈林并留下外泄笔记，反成右派致命罪证。 ‖ `←MTG-1927-12-15th-party-congress`[expelled -> recantation|1927-12-18至12-19]: 列入大会开除的75人名单，随即联署悔过声明与托洛茨基派决裂
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←MTG-1927-12-15th-party-congress`[leader|1927-12]: 主导彻底清除左翼反对派，会后一中全会以口头请辞总书记试探并强化政治局核心顺从
- **`POL-first-five-year-plan`**（第一个五年计划）: 苏联首部正式工业化纲领，1928–1929年在起点与最高方案争论中定案。1929-04-16至23日中央联席全会、04-23至29日十六次党代表会议及05-20至28日全苏苏维埃五大批准最高方案；下半年投资、钢铁与集体农庄指标加码，冲垮布哈林均衡路线，与NEP退场、强制集体化并进。 ‖ `←MTG-1927-12-15th-party-congress`[directives-adopted-at|1927-12]: 大会通过编制首个五年计划的框架性指示，尚带工农平衡约束而非1929年高指标定稿 ； `→MTG-1927-12-15th-party-congress`[mandated|1927.12]: 联共（布）十五大通过关于编制第一个五年计划的指示并宣示扩大农业集体化方向
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←MTG-1927-12-15th-party-congress`[policy-context|1927-12]: 表面重申NEP框内渐进合作化，实则同期秋冬季粮食收购危机已在掏空市场交换基础
- **`ORG-democratic-centralists`**（民主集中派）: 民主集中派是1919年初结成的布尔什维克党内反对派，萨普罗诺夫、奥新斯基、弗·斯米尔诺夫等为重要代表，批评以任命和行政命令取代集体领导与基层参与。成员及立场随时间变化：1923年部分人联署《四十六人声明》；后期“十五人集团”须与早期派别区分。 ‖ `→MTG-1927-12-15th-party-congress`[expulsion-context|1927-12]: 十五大扩大开除反对派
- **`PER-rakovsky`**（克里斯蒂安·拉柯夫斯基）: 巴尔干国际主义者与苏维埃政治家（1873—1941）。1919—1923年任乌克兰人民委员会主席，由反对单定乌语为国语转向力捍共和国自治，1923年十二大推动“本土化”妥协。后任驻英法大使与联合反对派核心，1928年流放撰《论职业危险》剖析执政异化风险，1941年在奥廖尔被处决。 ‖ `→MTG-1927-12-15th-party-congress`[expelled-at|1927-12]: 作为联合反对派核心被十五大开除中央与党籍，转入流放抗争与理论著述期
- **`PER-kalinin`**（米哈伊尔·加里宁）: 特维尔贫农与彼得堡车工出身的苏维埃名义元首（1875–1946）。1919年接替斯维尔德洛夫任全俄（后苏联）中执委主席，借粮食税与农村巡讲维系“工农联盟”门面；1926年入政治局，1928年私下同情布哈林，据布哈林述称在七月斗争中转附斯大林，保住其“全苏家长”象征地位。 ‖ `→MTG-1927-12-15th-party-congress`[presided-and-blessed-majority|1927-12]: 作为中执委主席在十五大框架内为反托—季多数路线提供宪制外观

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 3 项)
- **`DEB-1928-bukharin-alternative`**（布哈林替代方案与新经济政策终结之争 | `historiography/debates/DEB-1928-bukharin-alternative.md` | 流派 `nep-alternative, economic-growth, structural-dilemma, apparatus, ideology-and-mobilization, cliometrics-and-archival-reassessment`）：1927至1929年粮食危机与新经济政策的瓦解，是否意味着渐进工业化和工农联盟已无可行出路，还是党内权力与政策选择扼杀了布哈林的替代方案？投资、价格、农民供粮和政治动员之间的约束究竟有多强，必须把经济可行性、政治可行性与实际权力斗争分别检验。
- **`DEB-1929-collectivization-and-dekulakization-causes`**（1929年集体化与消灭富农政策的动因之争 | `historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md` | 流派 `peasant-social-history, statistical-economic-history, archival-local-escalation, geopolitics-and-scare, industrialization-constraints, agrarian-tribute-and-policing`）：1929年集体化加速与消灭富农政策的出现，究竟源于粮食收购和工业投资的结构约束，还是统计误判、地方竞速、战争恐慌与领导层选择的叠加？农民如何应对，中央内部何时形成强制方案？应把1928年非常征粮、1929年秋冬升级与次年全面执行分开考察。
- **`DEB-1924-socialism-in-one-country`**（一国建成社会主义与不断革命论 | `historiography/debates/DEB-1924-socialism-in-one-country.md` | 流派 `stalin-bukharin, united-opposition, political-intellectual-history, institutional-geopolitics, lenin-cooperative-plan, bonapartism-and-tactical-critique`）：欧洲革命迟滞后，苏联能否凭国内力量建成社会主义，还是生产力与世界市场的联系使最终完成有赖国际革命？争论中的建设、建成和免于复辟并非同一问题；工农联盟、外部安全及党内联盟变化又如何改变这些概念的政治意义？各方均主张建设，分歧在条件、界限与国际前景。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/46 条)
- **`CLM-deutscher-1959-united-opposition-defeat`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | （中译本；对应第二部 1926–1927 年）]: 
- **`CLM-khlevniuk-2015-collective-leadership-erosion`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（TRYING OUT COLLECTIVE LEADERSHIP 至 THE CHOICE）。工作区文本无纸质页码。]: 
- **`CLM-carr-davies-1969-nemchinov-table-critique`** [`SCH-davies-rw`(R·W·戴维斯) | pp. 55, 72-73, 117, 244-246]: 
- **`CLM-cohen-1973-nep-viability`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 270-276, 316-320]: 
- **`CLM-cohen-1973-notes-of-an-economist`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 295-296, 318-320]: 
- **`CLM-cohen-1973-bukharin-organizational-defeat`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 287-289, 297-301, 322-329]: 
- **`CLM-erlich-1960-bukharin-balanced-growth`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 21-23 (PDF pp. 38-40)]: 
- **`CLM-erlich-1960-preobrazhensky-dilemma`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 34-36, 40-41, 49-51, 170-171 (PDF pp. 51-53, 57-58, 66-68, 185-186)]: 
- **`CLM-erlich-1960-stalin-overkill-turn`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 161-169, 172-177, 183-184 (PDF pp. 176-184, 187-192, 198-199)]: 
- **`CLM-nove-1964-stalin-necessity-dilemma`** [`SCH-nove-alec`(亚历克·诺夫) | pp. 20-26, 32]: 
- **`CLM-kotkin-2014-bukharin-dilemma`** [`SCH-kotkin-stephen`(斯蒂芬·科特金) | EPUB Coda (OEBPS/9780698170100_EPUB_1-25.xhtml) & Ch. 14 (OEBPS/9780698170100_EPUB_1-24.xhtml)]: 
- **`CLM-fitzpatrick-1978-anti-bukharin-ideological-offensive`** [`SCH-fitzpatrick-sheila`(希拉·菲茨帕特里克) | pp. 11–14, 20–21]: 
- **`CLM-khlevniuk-2015-defeat-of-right-opposition`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch03.html（His Revolution 开篇至全盘集体化的 1929 年 11 月宣布）。工作区文本无纸质页码。]: 
- **`CLM-priestland-2007-1928-mobilization-turn-against-bukharin`** [`SCH-priestland-david`(大卫·普里斯特兰) | pp. 234–237; 291–296]: 
- **`CLM-merridale-1990-uglanov-moscow-collapse`** [`SCH-merridale-catherine`(凯瑟琳·梅里代尔) | pp. 53-64]: 
- **`CLM-davies-festschrift-1995-nep-statistics-and-planning-debates`** [`SCH-hunter-holland`(霍兰·亨特 · cliometrics) | pp. 18-21, 82-94, 218-226]: 
- **`CLM-bukharin-preobrazhensky-equilibrium-vs-accumulation-zh`** [`SCH-liu-wei-ping-xinqiao`(刘伟与平新乔 · chinese-political-economy) | 原刊 pp. 92–99 (PDF pp. 1–8；英文提要 pp. 127–128 / PDF pp. 9–10)]: 
- **`CLM-zemskov-2018-archival-constraints-and-party-radicalism`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | 馆藏中文PDF pp. 2–4, 7–10；非俄文原版纸页]: 
- **`CLM-sakharov-2012-nep-crossroads-1928`** [`SCH-sakharov-valentin`(瓦连京·萨哈罗夫) | EPUB Ch. 4.2 & Ch. 4.3]: 
- **`CLM-lewin-peasants-1968-grain-procurement-crisis`** [`SCH-lewin-moshe`(摩西·莱文) | pp. 221, 228-229, 242-243]: 
- **`CLM-lewin-peasants-1968-kulak-myth-and-serednyak`** [`SCH-lewin-moshe`(摩西·莱文) | pp. 76-78]: 
- **`CLM-lewin-peasants-1968-ural-siberian-method`** [`SCH-lewin-moshe`(摩西·莱文) | pp. 386-390, 395]: 
- **`CLM-davies-1980-autumn-1929-great-turn-fabrication`** [`SCH-davies-rw`(R·W·戴维斯) | Vol. 1 printed pp. 121–123, 128, 133, 147, 151–156, 165, 179–182；Vol. 2 本地 PDF pp. 34, 45, 60–61]: 
- **`CLM-davies-1980-november-plenum-to-dekulakization`** [`SCH-davies-rw`(R·W·戴维斯) | Vol. 1 printed pp. 159–167, 182–202；Vol. 2 本地 PDF pp. 50–55, 101–102]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
