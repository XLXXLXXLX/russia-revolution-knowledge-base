# 1-Hop 平衡上下文包：`MTG-1918-07-5th-congress-of-soviets` (第五次全俄工农兵与哥萨克苏维埃代表大会（1918年7月）)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/meetings/MTG-1918-07-5th-congress-of-soviets.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `constitution-primary, archival-revisionist, soviet-government-contemporary`
- **待补齐视角**: `full-congress-proceedings, independent-left-sr-archive`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `full-congress-proceedings, independent-left-sr-archive`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1918-07-04 至 1918-07-10 [N.S.]，第五次全俄苏维埃大会在莫斯科召开。布尔什维克与左翼社革党围绕和约、粮食政策及代表资格尖锐冲突；7月6日米尔巴赫遇刺后，武装冲突和对左翼社革党的拘押使两党苏维埃合作崩溃。7月10日，留下的代表通过首部俄罗斯苏维埃联邦社会主义共和国宪法。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **争论与资格**：大会在莫斯科大剧院举行。斯皮里多诺娃和卡姆科夫等左翼社革党人猛烈批评布列斯特和约、粮食专政及贫农委员会。公布的党派统计为布尔什维克678人、左翼社革党269人；左翼社革党在资格审查委员会中质疑约399名布尔什维克代表的资格，并要求资格委员会双方人数相等而被否决。Rabinowitch认为存在人为制造布尔什维克多数的大量间接证据；这不是对399份证件逐一鉴定为伪造的证明，也不能从公布人数中机械扣减，算出合法代表数。
- **刺杀与拘押**：1918-07-06 [N.S.]，左翼社革党人布柳姆金和安德烈耶夫刺杀德国大使米尔巴赫，莫斯科随即发生武装冲突。大会会场内左翼社革党党团及来宾遭集体拘押：Rabinowitch记为400余人，包含来宾，故常见的约450人不能直接当成核实过的代表人数。部分人员获释，资格审查委员会中的左翼社革党人被关到大会结束。
- **宪法与联盟终结**：1918-07-10 [N.S.]，在左翼社革党代表被排除的情况下复会，通过首部《俄罗斯社会主义联邦苏维埃共和国宪法》。左翼社革党人民委员此前已于3月因和约退阁，7月的破裂则终结了其与布尔什维克作为主要合作伙伴的苏维埃政治联盟；这不等于所有地方异议者或全部社会主义者同日消失。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-left-srs` | `coalition_breakdown` | 1918年3–7月 | 3月退出人民委员会，7月刺杀及拘押后苏维埃合作瓦解。 | Rabinowitch pp. 287–296 |
| `PER-spiridonova` | `challenges_government` | 1918年夏 | 左翼社革党领袖批评和约及农村政策；资格异议须与已证事实分开。 | Rabinowitch pp. 284–288；`AUD-14` |
| `EVT-1918-03-brest-litovsk-treaty` | `contested_at` | 1918年7月 | 和约成为两党冲突及刺杀背景。 | Rabinowitch ch. 11 |
| `ORG-cheka-ogpu` | `entangled_in_conflict` | 1918年7月 | 刺客和参与武装冲突者与契卡机构相联系。 | Rabinowitch pp. 291–294 |
| `DEB-1918-constituent-assembly-and-soviet-democracy` | `illuminates` | 1918年 | 资格争议与宪法条款提供考察苏维埃代表性之不同证据。 | 宪法第25、64–65条 |

### 2.3 史学争鸣光谱
**经验层面**：大使遇刺、冲突、党团被拘押与7月10日通过宪法均有文献支持；有争议的代表资格不能一律认定造假。**行动目的**：苏维埃政府当时将事件定为反苏维埃政权的起义；Rabinowitch经档案研究认为主要目的是迫使政府改变政策，而非武力夺权，但对普罗相短暂占据电报局及其可能未经授权保留例外。其判断并不抹去刺杀和武装冲突本身。

## 2. 一跳邻域等权重微摘要 (共 4 个关联节点，严防大卡霸占上下文)
### 邻居节点: `ORG-left-srs`
- **时效关系边** (`MTG-1918-07-5th-congress-of-soviets` → `ORG-left-srs` | `coalition_breakdown` | 有效时段: `1918年3–7月`): 3月退出人民委员会，7月刺杀及拘押后苏维埃合作瓦解。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1917年底从社会革命党分裂出的激进民粹派政党（1917–1923），以斯皮里多诺娃、普罗相等为首。拥护苏维埃政权并于1917年12月加入人民委员会与布尔什维克联合执政；1918年3月因反《布列斯特和约》退阁但仍维持北方公社合作，7月6日刺杀德国大使米尔巴赫遭全面清洗而覆灭。

### 邻居节点: `PER-spiridonova`
- **时效关系边** (`MTG-1918-07-5th-congress-of-soviets` → `PER-spiridonova` | `challenges_government` | 有效时段: `1918年夏`): 左翼社革党领袖批评和约及农村政策；资格异议须与已证事实分开。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 左翼社会革命党核心领袖（1884–1941，本卡至1929年）。1906年枪击坦波夫镇压官卢热诺夫斯基致其重伤后死亡，经十一年苦役获全国革命声望；1917–1918年推动农民苏维埃合并，竞选立宪会议主席获153票对切尔诺夫244票；1918年7月苏维埃五大参与发起刺杀米尔巴赫行动并亲赴会场承担政治责任被捕。

### 邻居节点: `EVT-1918-03-brest-litovsk-treaty`
- **时效关系边** (`MTG-1918-07-5th-congress-of-soviets` → `EVT-1918-03-brest-litovsk-treaty` | `contested_at` | 有效时段: `1918年7月`): 和约成为两党冲突及刺杀背景。
- **节点定性微摘要 [T1]** (完备度 `draft`): 1917年12月停战谈判至1918年3月签约：党内列宁“割地喘息”派、托洛茨基“不战不和”与布哈林“革命战争”派激烈对决；2月18日德军恢复进攻并经2月18/19日夜 7:5:1 试探性电告后，2月23日（公历）中央委员会以 **7:4:4** 接受严苛最后通牒，3月3日签约并经俄共七大批准，左翼社革党遂退出人民委员会。

### 邻居节点: `ORG-cheka-ogpu`
- **时效关系边** (`MTG-1918-07-5th-congress-of-soviets` → `ORG-cheka-ogpu` | `entangled_in_conflict` | 有效时段: `1918年7月`): 刺客和参与武装冲突者与契卡机构相联系。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 苏俄与苏联早期政治警察机关（1917–1934），由捷尔任斯基创立。历经全俄肃反委员会（ВЧК，1917–1922）、国家政治保卫局（ГПУ，1922–1923）与国家政治保卫总局（ОГПУ，1923–1934）三阶段，从法外非常机构演变为直属政治局的常设宪制部门，执行红色恐怖与强制集体化。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
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

### `DEB-1918-constituent-assembly-and-soviet-democracy`：解散立宪会议与多党苏维埃民主的命运
## [T1] 核心问题定义
1918年立宪会议被武力解散，是否意味着一党统治已不可避免？争论涉及普选制宪与阶级性苏维埃两种合法性、群众动员和镇压，以及此后左翼多党合作与体制内反对派仍有多少政治空间。

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 修正派与地方档案 | Alexander Rabinowitch, *The Bolsheviks in Power* (2007) | 解散由布尔什维克党内温和派（加米涅夫等）败给列宁、左翼社革党配合及相当程度的工农冷漠共同促成；多党苏维埃空间是在1918年春夏危机中分阶段收缩的。 | `CLM-rabinowitch-2007-constituent-assembly`; `CLM-rabinowitch-2007-contingency-of-dictatorship`; `CLM-rabinowitch-2007-left-sr-coalition-collapse` | 彼得格勒经验能否推广全国、危机解释是否低估意识形态与主动镇压，均有争议。 |
| 社会革命党与选举史奠基派 | Oliver H. Radkey, *The Sickle under the Hammer* (1963) | 拆解社革党选票内部俄/乌与左右翼裂痕（299俄社革+81乌社革），揭示右翼社革党领导层因迷信合法议会程序、禁止武装保卫议会而自缚手脚，随后在萨马拉—西伯利亚沦为白卫军官“保护色”。 | `CLM-smith-scott-2011-psr-third-force-collapse`（馆藏真身 Radkey 1963）；`DATA-01` | 对精英策略失误的严厉道德批评有时低估了士兵厌战的结构性约束。 |
| 自由主义制度批判 | Richard Pipes, *The Russian Revolution* (1990) | 将1918年1月枪击保卫立宪会议游行与武力关闭议会视为列宁夺权意志与极权恐怖制度化的真正起点，认为布尔什维克借民众疲惫确立了不受制约的专政。 | `CLM-pipes-1990-october-classic-coup`; `CLM-pipes-1990-red-terror-leninist-logic` | 对地方苏维埃多党合作与1918年上半年布尔什维克党内争论关注不足。 |
| 孟什维克与议会民主传记派 | Israel Getzler, *Martov* (1967); W. H. Roobol, *Tsereteli* (1976) | 策烈铁里在 `1918-01-05 [O.S.]` 立宪会议讲坛作最后跨阶级议会民主抗辩；马尔托夫则在会后转入苏维埃体制内开展半合法反对（直至 `1918-06-14` 全俄中执委驱逐右社革与孟什维克）。 | `CLM-getzler-1967-martov-soviet-opposition`; `CLM-roobol-1976-tsereteli-tragedy-of-moderation` | 领袖政治伦理需与工厂全权代表会议（丘拉科夫 `CLM-churakov-2004-*`）实证规模对勘。 |

## 4. 关联时间线锚点 (共 0 条)
