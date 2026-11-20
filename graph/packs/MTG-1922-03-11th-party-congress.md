# 1-Hop 去重平衡上下文包：`MTG-1922-03-11th-party-congress`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`MTG-1922-03-11th-party-congress`** (俄国共产党（布尔什维克）第十一次代表大会（1922年） | `cards/meetings/MTG-1922-03-11th-party-congress.md` | `multi-perspective`): 已覆盖=`daniels-opposition-institutional, nep-leadership, lewin-contingency, khlevniuk-archival, carr-party-state`；待补=`complete-congress-proceedings, cc-plenum-original-minutes`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1922-03-27至04-02[N.S.]，俄共十一大在莫斯科召开，为列宁最后出席的党代会。他宣布NEP退却结束，强调管理、文化与官僚主义；大会警告工人反对派。04-03新中央全会设总书记并选出斯大林，04-04《真理报》公布；任命、公布均须与大会决定区分。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **新经济政策与国家能力**：列宁在政治报告中宣布退却已经结束，要求在保留新经济政策的条件下组织经济管理；这不是宣布取消市场或立即结束新经济政策。他以汽车和司机的比喻指出国家机关的运行往往偏离共产党人的意图，并警告共产党员的文化及管理能力不足，容易被旧官僚文化所征服。他借路标转换派的乌斯特里亚洛夫之论，警惕新经济政策可能被解读为通向资本主义复辟的道路；列宁与乌斯特里亚洛夫的政治结论不能混为一谈。报告原文与对应段落尚待本地一手文本逐句对勘，上述均为中文转述。
- **《二十二人声明》与纪律**：据Daniels，工人反对派的二十二名签署者向共产国际申诉党和工会官僚压制工人民主；申诉被党领导人反击。十一大特别委员会调查后指控什利亚普尼科夫、梅德韦杰夫和柯伦泰维持非法派别，并提议将三人开除；大会认可对其活动的谴责，以继续派别活动将被开除作警告。Daniels另记大会开除了米京和库兹涅佐夫，不能说大会没有任何开除。
- **会后全会与总书记**：大会选出新中央；**任命日为 `1922-04-03` [N.S.]**：中央全会设总书记并选出斯大林，莫洛托夫、古比雪夫任书记（站内互证见 2.2 与 T3）。`1922-04-04` 是《真理报》公布日（Carr），不是任命日；Daniels“1922年5月”之说与上列各项不符，视为孤证。该职务后来的权力扩张不能简单等同于设职当天已形成个人独裁；仅决议逐字措辞与列宁修改笔迹尚待原件核验。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | `reports_and_warns` | 1922年3–4月 | 倡议稳定新经济政策并警告国家机关、文化能力及资本主义复辟风险。 | 大会报告待一手核对 |
| `MTG-1921-rcpb-10th-congress` | `disciplinary_precedent` | 1921–1922 | 十大禁派决议及其未公开第7点构成十一大指控反对派的背景，具体适用程序应分别核对。 | Daniels pp. 148–150、162–163；[《论党的统一》第7点](../../sources/web-archive/E06_E10_turning_points/1921-03-16_on-party-unity.md) |
| `ORG-workers-opposition` | `investigated_and_censured` | 1922年 | 向共产国际申诉后遭特别委员会调查及大会谴责。 | Daniels pp. 162–163 |
| `PER-stalin` | `elected_general_secretary` | 1922-04-03 起 | 会后新中央全会选出总书记（非大会直接选任）；04-03 为全会日，04-04 为《真理报》公布日。 | `CLM-stalin-docs-1920s-secretariat-correspondence-and-grain-turn`；`RN-W24`；Khlevniuk ch06；Carr（`RN-W23`） |
| `INS-politburo-orgburo-secretariat` | `institutional_framework_of_appointment` | 1922年4月起 | 总书记职位所处的政治局—组织局—书记处制度框架。 | Khlevniuk ch06（见该卡边表） |
| `INS-rabkrin-and-ccc` | `parallel_control_organ` | 1922年 | 中监委与工农检查院同期运作，斯大林同期仍兼掌工农检查院。 | `INS-rabkrin-and-ccc`；`PER-stalin` |
| `PER-molotov` / `PER-kuibyshev` | `co-appointed_secretaries` | 1922-04-03 | 与斯大林同批任书记。 | `CLM-stalin-docs-1920s-secretariat-correspondence-and-grain-turn`；`INS-politburo-orgburo-secretariat` |
| `MTG-1923-04-12th-party-congress` | `successor_congress` | 1923年4月 | 后继党代会，沿同一书记处—中监委框架推进组织改革。 | 对应会议卡 |
| `CON-democratic-centralism-and-vanguard` | `disciplinary_context` | 1921–1922 | 统一与纪律规则限制了有组织的反对派活动。 | Daniels pp. 148–150、162–163 |

### 2.3 史学争鸣光谱
**可核事实**：Daniels记载国际申诉、委员会建议、对三人的警告及另外两人的开除；其关于纪律与行政组织发展为反对派失势机制的分析，是制度史解释而非会议参与者共识。新经济政策既包含市场与经营上的调整，也伴随党内纪律收紧，不能仅据一项变化判断另一项立即完成。

**多流派对读（总书记设职）**：
- **Lewin**（[`CLM-lewin-1968-testament-intent`](../../historiography/claims/CLM-lewin-1968-testament-intent.md)；站内 [L2 E08](../../timeline/L2_chronicles/E08_1921-1924_nep_and_lenins_last_struggle.md) 年表）：设职时该职位分量有限，列宁接受、甚至可能是他本人提出由斯大林任职，不宜以后见之明读作夺权起点。
- **Khlevniuk**（[`CLM-khlevniuk-2015-secretariat-and-nomenklatura`](../../historiography/claims/CLM-khlevniuk-2015-secretariat-and-nomenklatura.md)；ch06）：档案视角强调书记处的实际运作与干部任免权如何在政治局日常中积累；04-03 设职，自 04-06 起政治局几乎总在周四全员出席（转引自《斯大林重要文献》编者评述）。
- **Carr**（[`CLM-carr-1950-politburo-orgburo-displacement-of-state-organs`](../../historiography/claims/CLM-carr-1950-politburo-orgburo-displacement-of-state-organs.md)；`RN-W23`）：党国融合视角，把书记处与政治局、组织局对国家机关的取代作为长期趋势，并记 04-04 的《真理报》低调公布。
- **Daniels**：把设职置于“秘书制等级体系在顶部完成”的制度性叙述，并另系设职于1922年5月（孤证，与上三派及站内文献不符）。
- 争点：设职的当日分量（Lewin）与书记处机制的累积效应（Khlevniuk／Carr／Daniels）并不冲突，但不应相互倒写；`DEB-1922-lenin-testament-and-stalin-rise` 为对应争鸣节点。

## 2. 一跳邻域全量微摘要目录 (去重后共 11 个节点，0 截断)
- **`INS-rabkrin-and-ccc`**（中央监察委员会与工农检查人民委员部（联合工作体制））: 工农检查人民委员部是国家监察机关，中监委是党的纪律监督机关。1923年改组后共同领导、联合办公，仍为两个机构，未在法律上合并；列宁的合并设想及Carr、Lewin的叙述用语须与此区分。改革旨在改善官僚机器、维护中央团结，联合机构随后参与党内审查处分，监督亦受权力关系制约。 ‖ `→MTG-1922-03-11th-party-congress`[context|1922.03–04]: 站内札记记十一大中监委与格别乌协作；斯大林同期兼掌 RKI 至1922年 ； `←MTG-1922-03-11th-party-congress`[parallel_control_organ|1922年]: 中监委与工农检查院同期运作，斯大林同期仍兼掌工农检查院。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←MTG-1922-03-11th-party-congress`[reports_and_warns|1922年3–4月]: 倡议稳定新经济政策并警告国家机关、文化能力及资本主义复辟风险。
- **`MTG-1921-rcpb-10th-congress`**（俄国共产党（布尔什维克）第十次代表大会）: 1921年3月8日至16日，俄共（布）十大在经济崩溃与喀琅施塔得起义交织下召开。大会决定以粮食税取代余粮收集制，开启新经济政策转向；同时终结工会大辩论，通过《关于党的统一》禁止派别活动并谴责工人反对派。经济退却与党内纪律收紧并行，会后中央与书记处改组重塑了组织权力格局。 ‖ `←MTG-1922-03-11th-party-congress`[disciplinary_precedent|1921–1922]: 十大禁派决议及其未公开第7点构成十一大指控反对派的背景，具体适用程序应分别核对。
- **`ORG-workers-opposition`**（工人反对派）: 俄共（布）党内以产业工人和工会干部为主体的左翼反对派（1920–1922），由什利亚普尼科夫、梅德韦杰夫及理论代言人柯伦泰领导。在1920–1921年工会争论中痛斥党政官僚化与专家“一长制”，主张由“全俄生产者代表大会”及工会自治管理国民经济；1921年十大被定性为无政府工团主义倾向并遭解散。 ‖ `←MTG-1922-03-11th-party-congress`[investigated_and_censured|1922年]: 向共产国际申诉后遭特别委员会调查及大会谴责。
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←MTG-1922-03-11th-party-congress`[elected_general_secretary|1922-04-03 起]: 会后新中央全会选出总书记（非大会直接选任）；04-03 为全会日，04-04 为《真理报…
- **`INS-politburo-orgburo-secretariat`**（联共（布）中央政治局—组织局—书记处与官职等级名册制）: 1919年3月俄共八大后常设政治局、组织局与书记处，分掌政治决策、组织行政及日常党务人事。1922年4月斯大林任总书记后逐步控制议程、秘密文件分发与干部名册调配。经1924年七人小组协调、1925—1929年联盟重组与纪律整肃，托洛茨基、季诺维也夫、布哈林先后退出决策核心。 ‖ `←MTG-1922-03-11th-party-congress`[institutional_framework_of_appointment|1922年4月起]: 总书记职位所处的政治局—组织局—书记处制度框架。
- **`PER-molotov`**（维亚切斯拉夫·莫洛托夫）: 莫洛托夫是布尔什维克党务骨干与斯大林主要副手。1917年二月在《真理报》及俄国局反对支持临时政府；1921年任中央责任书记，后以书记处工作协同斯大林掌权。1928年11月至1929年4月接掌莫斯科委员会，并加强斯大林阵营对共产国际的控制，推动集体化加速。 ‖ `←MTG-1922-03-11th-party-congress`[co-appointed_secretaries|1922-04-03]: 与斯大林同批任书记。
- **`PER-kuibyshev`**（瓦列里安·古比雪夫）: 苏联工业化关键操盘手（1888–1935）。1918年曾在萨马拉追随左派共产主义者并任东线政委；1922年任中央书记，1923–1926年兼掌中监委与工农检查院，将列宁监督构想转为打击反对派工具；1926年接掌最高国民经济委员会，力推重工业高指标并坚定支持斯大林。 ‖ `←MTG-1922-03-11th-party-congress`[co-appointed_secretaries|1922-04-03]: 与斯大林同批任书记。
- **`MTG-1923-04-12th-party-congress`**（俄国共产党（布尔什维克）第十二次代表大会）: 1923年4月17—25日莫斯科举行。列宁第三次中风后首次缺席党代会，代表团分组秘密传达其民族问题笔记；托洛茨基以“剪刀差”图主张计划化工业化；民族问题特别会议迫使斯大林退让并确立本土化妥协决议，但会后人事布局仍背离列宁清算官僚沙文主义的初衷。 ‖ `←MTG-1922-03-11th-party-congress`[successor_congress|1923年4月]: 后继党代会，沿同一书记处—中监委框架推进组织改革。
- **`CON-democratic-centralism-and-vanguard`**（先锋队党与民主集中制）: 布尔什维克组织原则的跨期复合概念：从民意党集中制与特卡乔夫“自觉少数”，经1902年职业革命家论、1905–1906年成文的民主集中制及1917年群众政党，至1921年禁派令与斯大林书记处官职名册制，派别空间收缩；部分制度史研究强调干部任命权日益压过民主原则。 ‖ `←MTG-1922-03-11th-party-congress`[disciplinary_context|1921–1922]: 统一与纪律规则限制了有组织的反对派活动。
- **`POL-ban-on-factions-1921`**（《关于党的统一》派别禁令）: 俄共十大于1921年3月16日通过《关于党的统一》，要求解散按纲领组成的派别，并保留规定渠道的批评。秘密第七条设中央领导成员的特殊处分程序；1924年1月公开宣读、1926年7月首次动用开除季诺维也夫出政治局，危机措置遂渐成约束反对派的工具，但不同年份执行不等同原条文。 ‖ `→MTG-1922-03-11th-party-congress`[后续纪律升级|1922.03]: 审查工人反对派“二十二人声明”，持续重划派别纪律边界。

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 4 项)
- **`DEB-1921-trade-union-controversy-and-party-unity`**（1921年工会争论、工人反对派与党内统一之争 | `historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md` | 流派 `lenin-ten, trotsky-militarization, workers-opposition, party-institutional-history, labor-social-history, industrial-paternalism`）：内战结束之际，工会应成为国家管理生产的传动机构，还是维护工人利益并参与管理的独立空间？工人反对派、托洛茨基和列宁的方案分歧，如何与第十次党代表大会禁止派别相互交织？喀琅施塔得危机既是决议援引的背景，也是有待独立考察的社会抗议，不能混同党内派别。
- **`DEB-1922-lenin-testament-and-stalin-rise`**（列宁晚年、格鲁吉亚事件与斯大林崛起机制 | `historiography/debates/DEB-1922-lenin-testament-and-stalin-rise.md` | 流派 `revisionist, nationalities-history, archival-post-soviet, kotkin-source-skepticism, trotskyist, service-critical-biography, sakharov-pseudo-lenin-polemic`）：列宁晚年口授文稿和格鲁吉亚冲突，是反官僚与反斯大林的总体“最后斗争”，还是对共同集权框架内具体做法的修正？《遗嘱》本身是否存在文本流转疑点？斯大林的上升又如何由个人策略、书记处机关、寡头集体领导与反对派失策共同解释？
- **`DEB-1921-kronstadt-and-nep-origins`**（喀琅施塔得起义与新经济政策的双轨转折 | `historiography/debates/DEB-1921-kronstadt-and-nep-origins.md` | 流派 `social-history, political-institutional, provincial-and-state-society, soviet-orthodox`）：喀琅施塔得是白卫阴谋、农民反抗，还是要求重建劳动者苏维埃民主的革命者起义？1921年实物税与禁止党内派别同期出现，如何解释经济退却和政治收紧的联系、彼此差异及长期后果？
- **`DEB-1918-war-communism-ideology-or-emergency`**（战时共产主义与早期一党制本质之争：内战应急、乌托邦跃进还是国家统制连续？ | `historiography/debates/DEB-1918-war-communism-ideology-or-emergency.md` | 流派 `emergency-carr-mawdsley, utopian-tragedy-malia-pipes, state-continuity-lih-smith, mixed-causation-rabinowitch-lewin`）：1918至1921年的全面国有化、余粮收集制、取缔私商、劳动军事化，以及多党苏维埃收为一党专政，究竟是内战与供给崩溃逼出的生存应急，还是反市场乌托邦的激进兑现，抑或一战以来国家统制与基层危机交互的结果？“战时共产主义”是1921年转向时的事后标签，须分清措施序列与事后总结。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/41 条)
- **`CLM-stalin-docs-1920s-secretariat-correspondence-and-grain-turn`** [`SCH-dolmatov-vladimir`(弗拉基米尔·多尔马托夫（编） · archival-documentary-edition)]: 
- **`CLM-lewin-1968-testament-intent`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.10 'If Lenin Had Lived . . .'；列宁原文脚注见 Soch. XLV p. 392；XLIV p. 428]: 
- **`CLM-khlevniuk-2015-secretariat-and-nomenklatura`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（In Lenin's Shadow，GENERAL SECRETARY 至 1923 年 9 月组织局安排）；制度总论见 ops/xhtml/ch01a.html。工作区文本无纸质页码。]: 
- **`CLM-carr-1950-politburo-orgburo-displacement-of-state-organs`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | [PDF pp. 96, 100-105, 109-114]]: 
- **`CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists`** [`SCH-kollontai-alexandra`(亚历山德拉·柯伦泰 · participant-primary-text) | PDF pp. 2-11, 22-27]: 
- **`CLM-kollontai-1921-all-russian-congress-of-producers-program`** [`SCH-kollontai-alexandra`(亚历山德拉·柯伦泰 · participant-primary-text) | PDF pp. 11-21, 25-30]: 
- **`CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions`** [`SCH-godson-joseph`(约瑟夫·戈德森 · cold-war-labor-studies) | Book pp. 106–111, 121, 128–129 [PDF pp. 118–123, 133, 140–141]]: 
- **`CLM-service-2009-trotsky-authoritarian-consensus`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本第 23–24、28–29、37 章及引言]: 
- **`CLM-daniels-1960-tenth-congress-turning-point`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 146-153]: Daniels：1921年十大将党统一转化为压缩合法反对空间的组织制度
- **`CLM-schapiro-1981-end-of-illusion-unions-1917-to-tomsky-fall`** [`SCH-schapiro-leonard`(伦纳德·沙皮罗) | Book pp. 1–14 [PDF pp. 13–26]]: 
- **`CLM-filtzer-1986-nep-unemployment-and-shopfloor-bargaining`** [`SCH-filtzer-donald`(唐纳德·费尔泽) | pp. 19–29, 44–45, 77–78, 274]: 
- **`CLM-filtzer-1986-1929-tomsky-purge-and-shock-work`** [`SCH-filtzer-donald`(唐纳德·费尔泽) | pp. 22–24, 68–72, 76–82, 96–108, 274, 280–282, 287]: 
- **`CLM-lebsky-industrial-paternalism-origins-1917-1929`** [`SCH-lebsky-maksim`(马克西姆·列布斯基) | PDF pp. 9–26, 29–36, 48–49]: 
- **`CLM-lewin-1968-georgian-affair-bureaucracy`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.9、Ch.10 与 Appendixes I–III, VII–VIII]: 
- **`CLM-lewin-1968-cooperation-shift`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.8 'Russia between West and East'；列宁原文脚注 Soch. XLV pp. 367, 370, 373, 387–88, 389]: 
- **`CLM-smith-jeremy-1999-georgian-affair-reassessed`** [`SCH-smith-jeremy`(杰里米·史密斯) | pp. 252-253, 260-262, 266-268, 285-288, 296-297]: 
- **`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`** [`SCH-smith-jeremy`(杰里米·史密斯) | pp. 311, 321-325, 327-331]: 
- **`CLM-khlevniuk-2015-collective-leadership-erosion`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（TRYING OUT COLLECTIVE LEADERSHIP 至 THE CHOICE）。工作区文本无纸质页码。]: 
- **`CLM-kotkin-2014-geopolitics-and-ideology`** [`SCH-kotkin-stephen`(斯蒂芬·科特金) | EPUB Ch. 13 (OEBPS/9780698170100_EPUB_1-23.xhtml) & Coda (OEBPS/9780698170100_EPUB_1-25.xhtml)]: 
- **`CLM-deutscher-1959-disarmed-prophet-paradox`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | （中译本无独立纸页；对应第二部 1923 年争论章）]: 
- **`CLM-service-2009-trotsky-political-tactical-blunders`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本引言及第 31–32、37–38 章]: 
- **`CLM-sakharov-2012-lenin-cooperative-plan-debates`** [`SCH-sakharov-valentin`(瓦连京·萨哈罗夫) | EPUB Ch. 1.3 & Ch. 4.2]: 
- **`CLM-sakharov-2012-nep-crossroads-1928`** [`SCH-sakharov-valentin`(瓦连京·萨哈罗夫) | EPUB Ch. 4.2 & Ch. 4.3]: 
- **`CLM-avrich-1970-sailor-social-composition`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 101-105]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
