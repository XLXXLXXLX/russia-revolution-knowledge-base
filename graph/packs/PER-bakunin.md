# 1-Hop 平衡上下文包：`PER-bakunin` (米哈伊尔·巴枯宁)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/people/PER-bakunin.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `movement-history-venturi, berlin-moral-humanism, intellectual-history-walicki, conceptual-history-mayer`
- **待补齐视角**: `post-soviet-biographical`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `post-soviet-biographical`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
国际无政府主义与俄国民粹派“造反派/暴动派（*buntari*）”宗师。1814年生于特维尔省贵族家庭，1861年自西伯利亚越狱流亡西欧，在第一国际与马克思激烈论战并撰《国家制度和无政府状态》（1873）。笃信俄国农民天生具社会主义造反本能，深刻驱动1874年“到民间去”运动，并与拉夫罗夫、特卡乔夫论战。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **青年黑格尔派、1848欧洲街垒与西伯利亚越狱（1814–1861）**：生于 `1814-05-18 [O.S.] / 1814-05-30 [N.S.]` 特维尔省普里亚穆希诺贵族庄园；早年与别林斯基、赫尔岑共组莫斯科哲学圈，1840年赴德并发表名言“破坏的激情同时就是创造的激情”（1842）。1848–1849年投身布拉格与德累斯顿起义被捕，先后引渡奥地利、沙俄，囚禁于彼得保罗要塞与什吕瑟尔堡（期间向尼古拉一世呈交《忏悔书》），1857年流放西伯利亚；1861年夏经日本、美国成功越狱抵达伦敦，与赫尔岑、奥加辽夫重聚。
- **第一国际分裂与《国家制度和无政府状态》（1864–1873）**：在瑞士组建“国际社会主义民主同盟”并加入第一国际，围绕无产阶级政党夺取国家政权抑或自下而上废除一切国家权威，与马克思、恩格斯展开总决战（1872年海牙代表大会被开除）。1869–1870年曾短暂迷恋谢尔盖·涅恰也夫（S. G. Nechaev）的极端密谋意志，旋即决裂；1873年出版俄文代表作《国家制度和无政府状态》（*Gosudarstvennost' i anarkhiia*），批判马克思的“国家社会主义/学者专政”，系统阐发无政府集产主义与自下而上的自由公社联邦论。
- **民粹派“造反派（*buntari*）”纲领与1874“到民间去”（1873–1876及以后）**：在《国家制度和无政府状态》附录〈甲〉中，巴枯宁断言俄国农民无须长期启蒙，其历史积淀的共同体村社（*obshchina*）与斯捷潘·拉辛、普加乔夫式的“强盗与暴动传统”已使其成为天生的社会主义者，青年知识分子只需深入民间点燃零星暴动并将之联结为全俄总起义。这一号召与拉夫罗夫的“准备派”并立，直接驱动了1874年“狂飙之夏”的“到民间去”运动，并在运动受挫后催生了基辅“南方起义派”（德博戈里-莫克里耶维奇、斯捷潘诺维奇、杰伊奇、查苏利奇等）及1876年契吉林“伪诏密谋”（`RN-W2-zemlya-to-march-first.md`, `pp. 565, 581–584`）。`1876-07-01 [N.S.]` 病逝于瑞士伯尔尼。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-herzen` | `friend -> tactical-divergence` | 1840s–1870 | 早年莫斯科哲学挚友与伦敦《钟声》伙伴，晚年赫尔岑对其盲目暴动冒险与涅恰也夫纠葛持严厉保留 | `CLM-berlin-1960-populism-moral-core` |
| `PER-lavrov` | `populist-rival-pole` | 1873–1876 | 巴枯宁“立即鼓动暴动派（*buntari*）”与拉夫罗夫“长期知识与道德准备派（*lavristy*）”构成1870年代民粹运动双极，但共享“自下而上解放”反国家底色 | `CLM-berlin-1960-populism-moral-core`, `RN-W2-zemlya-to-march-first` |
| `PER-tkachev` | `anti-statist-opponent` | 1869–1876 | 巴枯宁在1869–1870年率先区分“雅各宾派”与“布朗基派”，坚决排斥少数派夺取并维持革命国家专政的路线 | `CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism` |
| `ORG-zemlya-i-volya` | `ideological-inspiration` | 1876–1879 | 第二代土地与自由社（及此前基辅南方起义派）将巴枯宁农村暴动理想转化为定居点鼓动与契吉林农民武装试验 | `CLM-venturi-1960-lipetsk-voronezh-split`, `RN-W2-zemlya-to-march-first` |
| `PER-zasulich` | `disciple-circle` | 1875–1879 | 查苏利奇与杰伊奇、斯捷潘诺维奇早年同属基辅巴枯宁主义“起义派（*buntari*）”核心圈 | `RN-W2-zemlya-to-march-first` |
| `CON-narodnichestvo` | `revolutionary-wing-founder` | 1860s–1870s | 为古典革命民粹主义注入反国家主义、村社本能论与农民直接行动的“造反派”基因 | `CLM-walicki-1969-narodnichestvo-definition` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：巴枯宁是19世纪国际无政府主义与俄国民粹派“造反派/暴动派（*buntari*）”的核心理论奠基人；其1873年《国家制度和无政府状态》对1874年“到民间去”及南方起义派产生了决定性动员作用。
- **主要解释分歧**（详参 `DEB-1879-narodnaya-volya-to-bolshevism`）：
  - **[伯林道德人文主义与反决定论谱系 / Isaiah Berlin]**（`CLM-berlin-1960-populism-moral-core`）：将巴枯宁与拉夫罗夫共同置于“自下而上解放”的民粹主义正统之中，强调其敌视一切将抽象历史必然性、技术官僚或国家强权凌驾于活生生个体自由之上的教条（`pp. x–xi, xix–xxvi`）。
  - **[文图里运动史与组织演进 / Franco Venturi]**（`CLM-venturi-1960-lipetsk-voronezh-split`, `RN-W2-zemlya-to-march-first`）：揭示巴枯宁主义的“即时农村起义”在遭遇农民皇权崇拜与无动于衷后，如何迫使基辅“起义派（*buntari*）”走向契吉林“伪造沙皇密诏”的权谋实验，最终在与国家机器正面碰撞中促成第二代土地与自由社向集中制与政治恐怖分化（`pp. 565, 581–584, 647–648`）。
  - **[瓦利茨基概念史与马克思论战 / Andrzej Walicki]**（`CLM-walicki-1969-narodnichestvo-definition`, `CLM-walicki-1969-marx-populist-affinity`）：区分狭义民粹主义（1870年代中期巴枯宁派主张“知识分子向人民学习、群众霸权高于受教育精英”的短暂反智倾向）与广义非资本主义发展理论；同时指出马恩对巴枯宁（及特卡乔夫）将俄国村社奉为“天选社会主义民族”的严厉批判（`pp. 3–5, 144, 182–183`）。
  - **[梅耶概念史考据 / Robert Mayer]**（`CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism`）：考证巴枯宁（1869–1870）是首位将“雅各宾派”引入俄文政治语境的思想家，但他严格按法国政治现实区分“雅各宾派”（罗伯斯庇尔式资产阶级纯政治共和派）与“布朗基派”（社会主义密谋派），从未发明所谓“俄国雅各宾主义”标签，哪怕与涅恰也夫决裂后亦未称其为雅各宾派（`pp. 132–133, 149 n.26`）。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `EVT-1874-going-to-the-people`
- **时效关系边** (`PER-bakunin` → `EVT-1874-going-to-the-people` | `insurrectionary-inspiration` | 有效时段: `1873-1874`): 主张俄国农民天生具有社会主义造反本能，驱动1874年“造反派”青年深入伏尔加与南方农村鼓动即时起义。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1874年夏，数千受巴枯宁（即时起义）与拉夫罗夫（长期宣传）感召的青年知识分子奔赴俄国乡村，却遭遇村社冷漠、保守沙皇崇拜及警方大规模搜捕（1877.10–1878.01 [O.S.] 审结“193人案”）。和平方针破产直接促成第二代土地与自由社（1876）向严密地下集中组织转型。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1879-narodnaya-volya-to-bolshevism`：民意党与布尔什维主义：密谋传统的连续性与异质性
## [T1] 核心问题定义
民意党的秘密纪律、职业革命与政治暴力，同后来的布尔什维克组织之间有何关系？争论必须分别考察组织手段、革命目标、道德论证和具体传承链条：相似的地下技术本身不能证明永久党专政或思想一脉相承。

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 自由主义思想史 | Isaiah Berlin, Venturi 英译本导论 (1960) | 承认职业密谋组织形态的先例，强调民粹伦理、个人良知与后来的党专政存在断裂。 | `CLM-berlin-1960-populism-moral-core` | 理想型可能淡化民意党内部的强制与雅各宾倾向。 |
| 政治思想与运动史 | Franco Venturi, *Roots of Revolution* (1960) | 1879年组织分裂源自农村工作困境与策略冲突；民意党融合社会革命和制宪目标，同时保留临时专政的张力。 | `CLM-venturi-1960-lipetsk-voronezh-split`; `CLM-venturi-1960-narodnaya-volya-constitutionalism` | 运动史不等同于完整的思想史；立宪主张的实际执行仍需检验。 |
| 观念社会史 | Andrzej Walicki, *The Controversy over Capitalism* (1969) | 区分民粹主义思潮与组织；马克思和民粹派存在理论互动，普列汉诺夫的反少数派夺权传统则展示另一条转化路径。 | `CLM-walicki-1969-narodnichestvo-definition`; `CLM-walicki-1969-marx-populist-affinity`; `CLM-walicki-1969-plekhanov-rational-reality` | 思想结构不直接证明组织传承，且对基层参与者关注有限。 |
| 自由主义制度批判 | Richard Pipes, *The Russian Revolution* (1990) | 其关于激进知识分子与专制制度对立、布尔什维克夺权及恐怖的论证，可提供长期政治文化比较；现有卡并未直接证明民意党至布党的一条传承线。 | `CLM-pipes-1990-patrimonial-state-and-intelligentsia`; `CLM-pipes-1990-october-classic-coup`; `CLM-pipes-1990-red-terror-leninist-logic` | 将不同年代政治目标与组织条件视为同一现象的风险；具体谱系须另核原文。 |

## 4. 关联时间线锚点 (共 0 条)
