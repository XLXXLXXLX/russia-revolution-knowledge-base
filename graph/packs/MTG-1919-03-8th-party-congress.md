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
- **军事分组与“军事反对派”（1919-03）**：由 **维·米·斯米尔诺夫**、**列·基·萨普罗诺夫** 及察里津系（伏罗希洛夫等）形成的 **军事反对派** 抨击托洛茨基大规模留用 **4.8万余名军事专家（военспецы）** 、恢复沙皇式军纪、枪毙逃兵与契卡特别部监控，主张工会—苏维埃对军队的更高主导权。列宁在军事分组支持托洛茨基 **正规红军** 路线，同时决议加强政治部与党中央对军队的监督，反对派未获组织性胜利。
- **内战中外背景**：大会召开时红军正于东线承受高尔察克春季攻势、南线酝酿邓尼金大_push；八大制度成果与军事路线为1919年“突击战线”反攻奠定党政框架（`EVT-1918-1920-russian-civil-war`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `INS-politburo-orgburo-secretariat` | `institutionalized-at` | 1919.03起 | 八大—中央全会创设三元常设中枢，标志党务从斯维尔德洛夫个人记忆转向官僚分工 | `INS-politburo-orgburo-secretariat` §2.1 |
| `INS-rkka-red-army-and-rvr` | `policy-confirmed` | 1919.03 | 击败军事反对派，确认военспецy—政委红军体制 | `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` |
| `PER-trotsky` | `defended-reform` | 1919.03 | 在八大为起用旧军官与建设正规军辩护并获胜 | `INS-rkka-red-army-and-rvr`；Smirnov 专著注 |
| `PER-lenin` | `chair-key-speeches` | 1919.03 | 主导纲领与中农政策表述，裁决军事争论 | 八大速记（待逐页核对） |
| `POL-war-communism` | `ideologically-framed` | 1919 | 第二党纲为战时征粮与劳动动员提供党的正式表述 | `DEB-1918-war-communism-ideology-vs-emergency` |
| `EVT-1918-1920-russian-civil-war` | `strategic-context` | 1919 | 1919决战年党政—军事体制在八大定型 | `CLM-kakurin-1928-red-army-interior-lines-strategy` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：八大通过第二党纲；1919年3月25日一届全会常设政治局、组织局与书记处；军事反对派围绕военспецy与军纪问题激烈辩论但未 overturn 托洛茨基路线。
- **主要解释分歧**：
  - **[军事建制作战派 / Mawdsley + Kakurin]**：48,000 военспецy 与铁路内线战略是1919年胜利的物质—组织前提，八大确认而非创立该路线，但排除了工会军事化的替代方案（`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`、`CLM-kakurin-1928-red-army-interior-lines-strategy`）。
  - **[批判性红军社会史 / A. Smirnov 等]**：八大反“堡垒主义”话语长期影响1920年代纪律松弛与反队列主义文化，伏龙芝1924年改革须与此遗产斗争（`CLM-smirnov-1920s-territorial-militia-and-combat-training-deficit` 引八大军事反对派立场）。
  - **[战时共产主义争论]**：第二党纲究竟将征粮体系 **理念化** 还是 **应急合法化**，见 `DEB-1918-war-communism-ideology-vs-emergency`；八大农村“联合中农”措辞不能简单读成对 NEP 的预叙，应置于1921年实物税转向前史。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `INS-politburo-orgburo-secretariat`
- **时效关系边** (`MTG-1919-03-8th-party-congress` → `INS-politburo-orgburo-secretariat` | `institutionalized` | 有效时段: `1919.03`): 因斯维尔德洛夫病逝，俄共八大正式决议在中央委员会下分设常设政治局、组织局与书记处，奠定党国权力中枢架构。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1919年俄共八大因斯维尔德洛夫骤逝常设分置政治局（决策）、组织局（行政）与书记处（人事）。1922年4月斯大林任总书记后，借议程控制、秘密分发网、一致对外纪律及名册任免权（Номенклатура），于1923–1929年瓦解寡头共治，先后击败托洛茨基、季诺维也夫与布哈林。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1918-war-communism-ideology-vs-emergency`：战时共产主义本质之争：内战应急、乌托邦跃进还是国家统制连续？
## [T1] 核心问题定义
1918–1921年国有化浪潮、余粮收集制、市场取缔、劳动军事化与工资平均化，究竟是内战与供应崩溃逼迫的应急措施簇，还是布尔什维克反市场社会主义与先锋队权力的乌托邦实验在内战中的激进展开？抑或应置于一战以来国家统制与俄国落后现实的“过渡”话语内理解？“战时共产主义”作为术语在1921年后才定型，争论须区分 **措施序列** 与 **事后标签**。

## [T2] 各学派立场对照矩阵

**经验共识**：1918年春夏国有化扩大；1918–1921 `prodrazvyorstka` 强制征粮；1920–1921劳动军事化与工会国家化高峰；1921年3月党的十大与新经济政策宣布经济“退却”；“военный коммунизм”在1921年党内外论战中作为回顾性概括流传。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **内战军事应急论** | E. H. Carr, *The Bolshevik Revolution, 1917–1923*; Evan Mawdsley, *The Russian Civil War* (1987) | Carr 按法令与机构演进追踪，强调崩溃、战线与物流使强制措施成为可行集合中的选项；Mawdsley 提供军需与行政区背景。 | `CLM-mawdsley-1987-civil-war-militarized-regime`（背景）；Carr（本库 `CLM-*` 待系统入库） | 单以战争不能解释每项选择的意识形态过滤器与党内争论。 |
| **乌托邦跃进幻觉论** | Martin Malia, *The Soviet Tragedy* (1994); Richard Pipes, *The Russian Revolution* (1990) | Malia：马克思主义乌托邦内在悲剧，危机清除障碍使激进蓝图兑现；Pipes：反市场社会主义与废法专政逻辑先行。 | `CLM-pipes-1990-red-terror-leninist-logic`（交叉） | 易由结果倒推单一意图时间表；Malia 长时段，Pipes 偏重1917–18起点。 |
| **战时国家统制连续论** | Lars T. Lih, *Lenin Rediscovered* 系列；S. A. Smith, *Red Petrograd* (1983) 及工人监督研究 | Lih：布尔什维克一贯谈“过渡”与俄国现实，战后共产主义标签是后设；“新经济政策醒悟论”简化了当时选项集。Smith：1917–18工人监督与国有化是社会冲突中的务实演化。 | `CLM-lih-2006-textbook-myth-critique`, `CLM-smith-sa-1983-defensive-workers-control`, `CLM-smith-1983-workers-control-pragmatism`, `CLM-smith-sa-1983-from-workers-control-to-nationalization`, `CLM-smith-sa-1983-factory-committees-vs-trade-unions` | 连续论须与1921年公开承认“过度”文献对读。 |
| **社会结构与退却论** | Moshe Lewin, *The Making of the Soviet System* (1985); *Russian Peasants and Soviet Power* (1968) | 农民反抗、战时村社战争与喀琅施塔得信号促成1921退却；区分危机与“农民社会”结构的钳制。 | `CLM-lewin-peasants-1968-grain-procurement-crisis` | 农村 violence 与首都决策链连接待档案深化。 |

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
