# 1-Hop 平衡上下文包：`MTG-1919-03-8th-party-congress` (俄国共产党（布尔什维克）第八次代表大会)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/meetings/MTG-1919-03-8th-party-congress.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `party-leadership, military-institutional, war-communism-debate`
- **待补齐视角**: `full-stenogram-rural-delegates`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `full-stenogram-rural-delegates`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1919年3月18–23日俄共（布）八大：斯维尔德洛夫逝世后通过第二党纲，正式常设政治局—组织局—书记处三元体制，列宁击败军事反对派关于反военспецy的激进主张，并宣告联合中农路线。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **制度重组（1919-03-18至23日）**：中央委员雅科夫·斯维尔德洛夫于 `1919-03-16` 病逝后，八大不得不将原先由斯维尔德洛夫一人统筹协调的党政机制作制度化拆分。3月23日闭幕后 **`1919-03-25` 一届中央全会** 选出常设 **政治局**（政治决策）、**组织局**（组织行政）与重组 **书记处**（日常党务与人事）（`INS-politburo-orgburo-secretariat`）。
- **第二党纲（1919）**：大会通过内战条件下的新纲领，将政权任务表述为无产阶级专政、国际革命与国内“红军—契卡”动员并行；农村政策措辞从单纯贫农支柱转向 **联合中农（середняк）** 、限制富农并巩固征粮体制，为战时共产主义在农村的再谈判打开话语空间。
- **军事分组与“军事反对派”（1919-03）**：由 **弗·米·斯米尔诺夫**、**季·弗·萨普罗诺夫**（`PER-sapronov`）及察里津系（伏罗希洛夫等）形成的 **军事反对派** 抨击托洛茨基大规模留用 **4.8万余名军事专家（военспецы）** 、恢复沙皇式军纪、枪毙逃兵与契卡特别部监控，主张工会—苏维埃对军队的更高主导权。列宁在军事分组支持托洛茨基 **正规红军** 路线，同时决议加强政治部与党中央对军队的监督，反对派未获组织性胜利。
- **内战中外背景**：大会召开时红军正于东线承受高尔察克春季攻势、南线酝酿邓尼金大_push；八大制度成果与军事路线为1919年“突击战线”反攻奠定党政框架（`EVT-1918-1920-russian-civil-war`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `INS-politburo-orgburo-secretariat` | `institutionalized-at` | 1919.03起 | 八大—中央全会创设三元常设中枢，标志党务从斯维尔德洛夫个人记忆转向官僚分工 | `INS-politburo-orgburo-secretariat` §2.1 |
| `INS-rkka-red-army-and-rvr` | `policy-confirmed` | 1919.03 | 击败军事反对派，确认военспецy—政委红军体制 | `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` |
| `PER-trotsky` | `defended-reform` | 1919.03 | 在八大为起用旧军官与建设正规军辩护并获胜 | `INS-rkka-red-army-and-rvr`；Smirnov 专著注 |
| `PER-lenin` | `chair-key-speeches` | 1919.03 | 主导纲领与中农政策表述，裁决军事争论 | 八大速记（待逐页核对） |
| `POL-war-communism` | `ideologically-framed` | 1919 | 第二党纲为战时征粮与劳动动员提供党的正式表述 | `DEB-1918-war-communism-ideology-or-emergency` |
| `EVT-1918-1920-russian-civil-war` | `strategic-context` | 1919 | 1919决战年党政—军事体制在八大定型 | `CLM-kakurin-1928-red-army-interior-lines-strategy` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：八大通过第二党纲；1919年3月25日一届全会常设政治局、组织局与书记处；军事反对派围绕военспецy与军纪问题激烈辩论但未 overturn 托洛茨基路线。
- **主要解释分歧**：
  - **[军事建制作战派 / Mawdsley + Kakurin]**：48,000 военспецy 与铁路内线战略是1919年胜利的物质—组织前提，八大确认而非创立该路线，但排除了工会军事化的替代方案（`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`、`CLM-kakurin-1928-red-army-interior-lines-strategy`）。
  - **[批判性红军社会史 / A. Smirnov 等]**：八大反“堡垒主义”话语长期影响1920年代纪律松弛与反队列主义文化，伏龙芝1924年改革须与此遗产斗争（`CLM-smirnov-1920s-territorial-militia-and-combat-training-deficit` 引八大军事反对派立场）。
  - **[战时共产主义争论]**：第二党纲究竟将征粮体系 **理念化** 还是 **应急合法化**，见 `DEB-1918-war-communism-ideology-or-emergency`；八大农村“联合中农”措辞不能简单读成对 NEP 的预叙，应置于1921年实物税转向前史。

## 2. 一跳邻域等权重微摘要 (共 7 个关联节点，严防大卡霸占上下文)
### 邻居节点: `INS-politburo-orgburo-secretariat`
- **时效关系边** (`MTG-1919-03-8th-party-congress` → `INS-politburo-orgburo-secretariat` | `institutionalized` | 有效时段: `1919.03`): 因斯维尔德洛夫病逝，俄共八大正式决议在中央委员会下分设常设政治局、组织局与书记处，奠定党国权力中枢架构。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1919年3月俄共八大在斯维尔德洛夫逝世后常设分置政治局（政治决策）、组织局（组织行政）与书记处（日常党务与人事）。1922年4月斯大林出任总书记后，逐步掌握政治局议程截稿、秘密文件分发与干部等级名册（Номенклатура）调配杠杆；历经1924年“七人小组”协调与1925—1929年多轮联盟重组及纪律整肃，托洛茨基、季诺维也夫与布哈林等先后被逐出中央决策核心。

### 邻居节点: `INS-rkka-red-army-and-rvr`
- **时效关系边** (`MTG-1919-03-8th-party-congress` → `INS-rkka-red-army-and-rvr` | `policy-confirmed` | 有效时段: `1919.03`): 击败军事反对派，确认военспецy—政委红军体制
- **节点定性微摘要 [T1]** (完备度 `draft`): 苏维埃武装中枢：1918年1月15日（公历1月28日）颁令组建志愿红军，3–9月托洛茨基出任陆海军人民委员暨共和国革军委（RVSR）主席，改行普遍义务兵役、征召逾4.8万前沙皇军官（военспецы）与政治委员双签制；1919八大击退军事反对派与察里津集团；1924–1925伏龙芝改革转向正规军与地方民兵混合体制。

### 邻居节点: `PER-trotsky`
- **时效关系边** (`MTG-1919-03-8th-party-congress` → `PER-trotsky` | `defended-reform` | 有效时段: `1919.03`): 在八大为起用旧军官与建设正规军辩护并获胜
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。

### 邻居节点: `PER-lenin`
- **时效关系边** (`MTG-1919-03-8th-party-congress` → `PER-lenin` | `chair-key-speeches` | 有效时段: `1919.03`): 主导纲领与中农政策表述，裁决军事争论
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。

### 邻居节点: `POL-war-communism`
- **时效关系边** (`MTG-1919-03-8th-party-congress` → `POL-war-communism` | `ideologically-framed` | 有效时段: `1919`): 第二党纲为战时征粮与劳动动员提供党的正式表述
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1918年夏至1921年3月苏维埃经济政策总称：余粮收集制、中小工业国有化、取缔私商、货币贬值与实物配给并举；因内战饥荒与国家能力崩溃而强化，却在1921年喀琅施塔得与坦波夫危机下为新经济政策实物税所取代；其性质是应急、乌托邦跃进还是国家统制传统延续，史家分歧剧烈。

### 邻居节点: `EVT-1918-1920-russian-civil-war`
- **时效关系边** (`MTG-1919-03-8th-party-congress` → `EVT-1918-1920-russian-civil-war` | `strategic-context` | 有效时段: `1919`): 1919决战年党政—军事体制在八大定型
- **节点定性微摘要 [T1]** (完备度 `draft`): 1918–1920年苏俄内战：布尔什维克依托“苏托邦”人口、军火与莫斯科铁路枢纽内线机动，先后粉碎高尔察克、邓尼金、弗兰格尔白军及马赫诺黑军，并压制社革党第三力量；协约国干涉与边疆民族武装相互牵制。

### 邻居节点: `ORG-democratic-centralists`
- **时效关系边** (`ORG-democratic-centralists` → `MTG-1919-03-8th-party-congress` | `party-congress-debate` | 有效时段: `1919-03`): 组织问题与军事反对派争论
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 民主集中派是1919年初结成的布尔什维克党内反对派，萨普罗诺夫、奥新斯基、弗·斯米尔诺夫等为重要代表，批评以任命和行政命令取代集体领导与基层参与。成员及立场随时间变化：1923年部分人联署《四十六人声明》；后期“十五人集团”须与早期派别区分。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
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

### `DEB-1918-red-terror-and-civil-war-origins`：红色恐怖、契卡扩张与内战期一党专政起源之争（1918–1921）
## [T1] 核心问题定义
1918–1921年红色恐怖、契卡法外处决、对社会主义反对派的镇压，以及内战期间政党竞争被压缩为一党统治，应被解释为布尔什维克意识形态与列宁主义权力逻辑的宿命展开，还是多重危机（经济崩溃、联盟破裂、地方失控、内战动员）下可错链条上的制度选择？恐怖与一党制是同一过程还是须分时段因果？

## [T2] 各学派立场对照矩阵

**经验共识**：1917年12月契卡（全俄肃反委员会）成立；1918年7月左派社会革命党起义后左翼社会主义者被逐出权力结构；1918年9月5日人民委员会颁布《关于红色恐怖》决议；内战1918–1920在多条战线同时进行；1918–1921征粮与契卡行动在地方相互嵌合。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **意识形态宿命论** | Richard Pipes, *The Russian Revolution* (1990); Orlando Figes, *A People's Tragedy* (1996) | 强调反自由主义知识分子传统、列宁废法统治与阶级敌人话语，使恐怖成为夺取与巩固权力的内在逻辑；Figes 另重农民“悲剧”道德经济。 | `CLM-pipes-1990-red-terror-leninist-logic` | 时间线易前推到1917末，低估联盟期与反对派选项；Figes 与 Pipes 因果权重不一。 |
| **复合危机与联盟破裂论** | Alexander Rabinowitch, *The Bolsheviks in Power* (2007) 等 | 彼得格勒首年追踪与左派社革党联盟从执政到破裂；恐怖升级与粮食危机、暗杀、前线失败交织，而非单线预谋。 | `CLM-rabinowitch-2007-left-sr-coalition-collapse`, `CLM-rabinowitch-2007-contingency-of-dictatorship` | 首都政党政治详尽，偏远地方契卡实践待补。 |
| **制度史与阶段论** | George Leggett, *The Cheka: Lenin's Political Police* (1981); Ilya S. Ratkovsky（及契卡编年史学） | Leggett：契卡从法外 origin 到 GPU 连续体制化；Ratkovsky：1918 夏已有人质与处决规模，9月5日法令是公开化节点而非“零起点”。 | `CLM-leggett-1981-vecheka-extra-legal-origins`, `CLM-leggett-1981-red-terror-institutionalization`, `CLM-leggett-1981-cheka-to-gpu-continuity`, `CLM-cheka-chronicle-hostage-and-local-autonomy`, `CLM-cheka-chronicle-suppression-of-socialist-rivals` | Leggett 偏重中央法令；地方自治与契卡失控需档案对勘。 |
| **1914–1921 总体战治理连续论** | David G. Hoffmann, *Cultivating the Masses: Modern State Practices and Soviet Socialism, 1914–1939* (2011) | 征粮、动员、战备与“培养大众”技术沿袭一战国家实践；苏联社会主义是欧洲现代国家治理谱系的一极，而非凭空乌托邦。 | `CLM-hoffmann-2011-continuum-of-total-war-1914-1929`, `CLM-hoffmann-2011-enlightenment-and-coercion-duality`, `CLM-hoffmann-2011-soviet-socialism-as-european-modernity` | 连续性不等于免除布尔什维克政党特有选择责任。 |
| **内战军事—地理决定论（背景）** | Evan Mawdsley, *The Russian Civil War* (1987) | 红军人口—工业内线优势与白军结构性政策失败解释内战结局；为恐怖与征粮提供战略背景，不单独承担一党制意识形态解释。 | `CLM-mawdsley-1987-civil-war-militarized-regime`, `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` | 军事动员不等于党内反对派清洗因果。 |

## 4. 关联时间线锚点 (共 0 条)
