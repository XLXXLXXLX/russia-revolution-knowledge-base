# 1-Hop 平衡上下文包：`MTG-1922-03-11th-party-congress` (俄国共产党（布尔什维克）第十一次代表大会（1922年）)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/meetings/MTG-1922-03-11th-party-congress.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `daniels-opposition-institutional, nep-leadership, lewin-contingency, khlevniuk-archival, carr-party-state`
- **待补齐视角**: `complete-congress-proceedings, cc-plenum-original-minutes`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `complete-congress-proceedings, cc-plenum-original-minutes`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1922-03-27 至 1922-04-02 [N.S.]，俄共（布）十一大在莫斯科召开，是列宁生前出席的最后一次党代会。列宁宣布新经济政策的退却结束，强调经济管理、文化能力和官僚主义问题；大会审议工人反对派申诉并予以警告。闭幕次日，**1922-04-03 [N.S.]** 新中央全会设总书记并选出斯大林（任命日）；《真理报》于 **04-04** 低调公布（公布日），二者须与大会本身的决定区分。

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

## 2. 一跳邻域等权重微摘要 (共 10 个关联节点，严防大卡霸占上下文)
### 邻居节点: `PER-lenin`
- **时效关系边** (`MTG-1922-03-11th-party-congress` → `PER-lenin` | `reports_and_warns` | 有效时段: `1922年3–4月`): 倡议稳定新经济政策并警告国家机关、文化能力及资本主义复辟风险。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。

### 邻居节点: `MTG-1921-rcpb-10th-congress`
- **时效关系边** (`MTG-1922-03-11th-party-congress` → `MTG-1921-rcpb-10th-congress` | `disciplinary_precedent` | 有效时段: `1921–1922`): 十大禁派决议构成十一大指控反对派的背景，具体适用程序应分别核对。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1921年3月8日至16日，俄共（布）十大在经济崩溃与喀琅施塔得起义交织下召开。大会决定以粮食税取代余粮收集制，开启新经济政策转向；同时终结工会大辩论，通过《关于党的统一》禁止派别活动并谴责工人反对派。经济退却与党内纪律收紧并行，会后中央与书记处改组重塑了组织权力格局。

### 邻居节点: `ORG-workers-opposition`
- **时效关系边** (`MTG-1922-03-11th-party-congress` → `ORG-workers-opposition` | `investigated_and_censured` | 有效时段: `1922年`): 向共产国际申诉后遭特别委员会调查及大会谴责。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 俄共（布）党内以产业工人和工会干部为主体的左翼反对派（1920–1922），由什利亚普尼科夫、梅德韦杰夫及理论代言人柯伦泰领导。在1920–1921年工会争论中痛斥党政官僚化与专家“一长制”，主张由“全俄生产者代表大会”及工会自治管理国民经济；1921年十大被定性为无政府工团主义倾向并遭解散。

### 邻居节点: `PER-stalin`
- **时效关系边** (`MTG-1922-03-11th-party-congress` → `PER-stalin` | `appointed_general_secretary` | 有效时段: `1922年4月起`): 会后新中央全会任命总书记；不是大会直接选任。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。

### 邻居节点: `CON-democratic-centralism-and-vanguard`
- **时效关系边** (`MTG-1922-03-11th-party-congress` → `CON-democratic-centralism-and-vanguard` | `disciplinary_context` | 有效时段: `1921–1922`): 统一与纪律规则限制了有组织的反对派活动。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克组织原则的跨期复合概念。从民意党执委会集中制与特卡乔夫“自觉少数”，经1902年《怎么办？》职业革命家组织、1905–1906年首次成文的“民主集中制”与1917年开放竞争的群众政党，至1921年禁派令与斯大林书记处—官职名册制，合法派别活动空间大幅收缩；一些制度史研究认为干部任命权日益压过民主原则。

### 邻居节点: `INS-rabkrin-and-ccc`
- **时效关系边** (`INS-rabkrin-and-ccc` → `MTG-1922-03-11th-party-congress` | `context` | 有效时段: `1922.03–04`): 站内札记记十一大中监委与格别乌协作；斯大林同期兼掌 RKI 至1922年
- **时效关系边** (`MTG-1922-03-11th-party-congress` → `INS-rabkrin-and-ccc` | `parallel_control_organ` | 有效时段: `1922年`): 中监委与工农检查院同期运作，斯大林同期仍兼掌工农检查院。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 工农检查人民委员部（RKI）是国家监察机关，中央监察委员会（中监委）是党的纪律与监督机关。1923年二者经改组实行共同领导与联合办公，**仍是两个机构，并未法律合并为一个机构**（“合并”是列宁1923年1月的设想，也是 Carr、Lewin 的叙述用语；法律与实践层面的合署须分开标注）。列宁希望借此改善官僚机器并支持中央团结；随后联合工作机构在党内斗争中也参与审查与纪律处分，形成监督者受制于党内权力关系的悖论。

### 邻居节点: `INS-politburo-orgburo-secretariat`
- **时效关系边** (`MTG-1922-03-11th-party-congress` → `INS-politburo-orgburo-secretariat` | `institutional_framework_of_appointment` | 有效时段: `1922年4月起`): 总书记职位所处的政治局—组织局—书记处制度框架。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1919年3月俄共八大在斯维尔德洛夫逝世后常设分置政治局（政治决策）、组织局（组织行政）与书记处（日常党务与人事）。1922年4月斯大林出任总书记后，逐步掌握政治局议程截稿、秘密文件分发与干部等级名册（Номенклатура）调配杠杆；历经1924年“七人小组”协调与1925—1929年多轮联盟重组及纪律整肃，托洛茨基、季诺维也夫与布哈林等先后被逐出中央决策核心。

### 邻居节点: `PER-molotov`
- **时效关系边** (`MTG-1922-03-11th-party-congress` → `PER-molotov` | `co-appointed_secretaries` | 有效时段: `1922-04-03`): 与斯大林同批任书记。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克核心党务官僚与斯大林头号副手（1890–1986，本卡至1929年）。1917二月在《真理报》与俄国局持反临时政府强硬立场；1921任中央责任书记，后长期作为书记处大总管协同斯大林操盘；1928年11月至1929年4月接掌莫斯科委员会（MK），并代表斯大林阵营加强对共产国际领导工作的控制，推动集体化加速。

### 邻居节点: `MTG-1923-04-12th-party-congress`
- **时效关系边** (`MTG-1922-03-11th-party-congress` → `MTG-1923-04-12th-party-congress` | `successor_congress` | 有效时段: `1923年4月`): 后继党代会，沿同一书记处—中监委框架推进组织改革。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1923年4月17—25日莫斯科举行。列宁第三次中风后首次缺席党代会，代表团分组秘密传达其民族问题笔记；托洛茨基以“剪刀差”图主张计划化工业化；民族问题特别会议迫使斯大林退让并确立本土化妥协决议，但会后人事布局仍背离列宁清算官僚沙文主义的初衷。

### 邻居节点: `POL-ban-on-factions-1921`
- **时效关系边** (`POL-ban-on-factions-1921` → `MTG-1922-03-11th-party-congress` | `后续纪律升级` | 有效时段: `1922.03`): 审查工人反对派“二十二人声明”，持续重划派别纪律边界。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 俄共十大于1921年3月16日通过《关于党的统一》，要求解散按纲领组成的派别，并保留规定渠道的批评。秘密第七条设中央领导成员的特殊处分程序；1924年1月公开宣读、1926年7月首次动用开除季诺维也夫出政治局，危机措置遂渐成约束反对派的工具，但不同年份执行不等同原条文。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
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

### `DEB-1922-lenin-testament-and-stalin-rise`：列宁晚年、格鲁吉亚事件与斯大林崛起机制
## [T1] 核心问题定义
列宁晚年口授文稿和格鲁吉亚冲突，是反官僚与反斯大林的总体“最后斗争”，还是对共同集权框架内具体做法的修正？《遗嘱》本身是否存在文本流转疑点？斯大林的上升又如何由个人策略、书记处机关、寡头集体领导与反对派失策共同解释？

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 反官僚最后斗争论 | Moshe Lewin, *Lenin's Last Struggle* (1968) | 将晚年口授群读为反大国沙文主义、改组监察院及撤换斯大林的连贯政治改革方案；但指出列宁始终未废除派别禁令与一党垄断。 | `CLM-lewin-1968-testament-intent`; `CLM-lewin-1968-georgian-affair-bureaucracy`; `CLM-lewin-1968-cooperation-shift` | 写于苏联全开档案前，连贯“总体计划”程度及12月22日电话定年受后续考据挑战。 |
| 民族政策修正 | Jeremy Smith, *The Bolsheviks and the National Question* (1999) | 强调列斯在集中制大原则上的长期共识，并据十二大特别会议解密速记揭示斯大林被迫作出的本土化妥协。 | `CLM-smith-jeremy-1999-georgian-affair-reassessed`; `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` | 行政协调解释须与列宁1923年3月5–6日对斯大林绝交信的激烈措辞并观。 |
| 后苏联档案与寡头共治论 | Oleg Khlevniuk, *Stalin* (2015) | 以斯大林1923–1927年多次亲口承认遗嘱存在及3月7日复函驳斥伪造论；指出1月4日补遗重在“权力再平衡”而非逐出高层，且1920年代寡头集体领导真实存在。 | `CLM-khlevniuk-2015-secretariat-and-nomenklatura`; `CLM-khlevniuk-2015-collective-leadership-erosion` | 需注意勿将1920年代末成熟名册规模倒推回1922年。 |
| 文献流转质疑与重定年派 | Stephen Kotkin, *Stalin, Vol. 1* (2014, Ch. 11) | 指出《给代表大会的信》缺失列宁亲签与原始速记底本、打字件经克鲁普斯卡娅与秘书圈流转存有加工疑窦，并据斯大林3月7日复函“约五周前”将电话冲突重定年于1923年1月下旬；同时强调斯大林不可替代的机关功能使其难因一纸信函下台。 | `CLM-kotkin-2014-geopolitics-and-ideology`; `L3 1922-12` 专章对勘 | 尚无直接物证证明秘书团凭空捏造，且难以解释斯大林本人在十三大与1927全会从未质疑文件真伪。 |
| 左翼悲剧论 vs 政治失误批判 | Isaac Deutscher (1959) vs Robert Service, *Trotsky* (2009) | 多伊彻痛惜托洛茨基3月6日拒绝落井下石错失良机且受困一党纪律；瑟维斯则据档案批评托洛茨基共享威权前提、两拒人民委员会副主席职务并在十二大傲慢避战，纯属政治判断失误。 | `CLM-deutscher-1959-disarmed-prophet-paradox`; `CLM-service-2009-trotsky-authoritarian-consensus`; `CLM-service-2009-trotsky-political-tactical-blunders` | 需将个人性格失误置于书记处与三驾马车结构结盟中评估。 |
| 俄国“伪列宁文本”极端派 | V. A. Sakharov (2003 遗嘱专著; 2012《十字路口》) | 其2003年专著极端断言遗嘱与民族札记系克鲁普斯卡娅—托派伪造；库内已入库的2012年著作则聚焦《论合作社》两稿差异与1920年代路线争夺（两书议题边界须严格区分）。 | `CLM-sakharov-2012-lenin-cooperative-plan-debates`; `CLM-sakharov-2012-nep-crossroads-1928` | 全盘伪造说遭赫列夫纽克、洛吉诺夫等主流俄罗斯档案学者一致否证。 |

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

### `DEB-1918-war-communism-ideology-or-emergency`：战时共产主义与早期一党制本质之争：内战应急、乌托邦跃进还是国家统制连续？
## [T1] 核心问题定义
1918–1921年的全面工业国有化、余粮收集制（`продразвёрстка`）、取缔私商、劳动军事化及多党苏维埃向一党专政的收缩，究竟是内战与供给崩溃逼迫的生存应急反应，还是布尔什维克反市场乌托邦蓝图的激进兑现，抑或一战以来国家统制与基层危机交互演化的结果？“战时共产主义”系1921年新经济政策转向时的事后追赋标签，须严格区分措施出台序列与事后总结。

## [T2] 各学派立场对照矩阵

**经验共识**：1917年底至1918年春尚存布尔什维克—左翼社革党联合执政与“国家资本主义”探索；1918年夏起全面国有化与强制征粮随内战升级扩展；1920年达至劳动军事化与无货币幻想顶峰；1921年3月俄共十大在农村起义与喀琅施塔得危机下转向实物税（NEP）与党内派别禁令。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **内战军事应急与双元矛盾论** | E. H. Carr, *The Bolshevik Revolution*, Vol. 2 (1952); Evan Mawdsley, *The Russian Civil War* (1987) | 强调工业瓦解、封锁与300万红军补给迫使政权诉诸垂直“总局主义”与强制征粮；但Carr同时指出1920年后期确曾滋生把战时自然经济奉为直接通往共产主义捷径的意识形态幻象。 | `CLM-carr-1952-war-communism-internal-contradictions`; `CLM-mawdsley-1987-civil-war-militarized-regime`; `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` | 单靠军事紧急状态难以完全解释1920年底内战大局已定后为何仍出台小手工业全面国有化令。 |
| **意识形态乌托邦与废法专政论** | Martin Malia, *The Soviet Tragedy* (1994); Richard Pipes, *The Russian Revolution* (1990) | 认为消灭私有产权与市场交换本就是马克思主义核心诉求，内战只是扫除了渐进障碍、催化乌托邦跃进；Pipes强调契卡与排斥反对派早于大规模内战爆发。 | `CLM-pipes-1990-red-terror-leninist-logic`; `CLM-pipes-1990-october-classic-coup` | 易将不同阶段的应急妥协（如1918春列宁国家资本主义方案）回溯拉平为单一既定时间表。 |
| **战时国家统制连续与自下而上倒逼论** | Lars T. Lih; S. A. Smith, *Red Petrograd* (1983); David Hoffmann (2011) | 揭示沙皇与临时政府在一战中已启动粮食专卖与国家统制；Smith证明1917–1918春77%早期企业没收源自基层工厂委员会应对关厂危机的自下而上压力，而非中央乌托邦指令。 | `CLM-smith-sa-1983-defensive-workers-control`; `CLM-smith-sa-1983-from-workers-control-to-nationalization`; `CLM-hoffmann-2011-continuum-of-total-war-1914-1929` | 总体战技术连续性不能替代对布尔什维克消灭整个有产阶级政治权利之独特意识形态动力的解释。 |
| **复合危机、党内张力与农村社会钳制论** | Alexander Rabinowitch (2007); Robert V. Daniels (1960); Moshe Lewin (1968/1985) | 追踪布列斯特和约、左翼社革党决裂及左翼共产主义者/工人反对派论战如何一步步锁死多党与党内多元空间，同时揭示小农汪洋的反抗最终迫使政权在1921年退却但保留了战时强制记忆。 | `CLM-rabinowitch-2007-contingency-of-dictatorship`; `CLM-daniels-1960-left-communists-1918`; `CLM-figes-1996-peasant-wars-and-nep-retreat`; `CLM-zemskov-1929-dekulakization-demographic-baseline` | 首都与萨拉托夫、坦波夫、乌拉尔等外省的时间差与暴力烈度须结合地方档案（Raleigh、Churakov）细化。 |

## 4. 关联时间线锚点 (共 0 条)
