# 1-Hop 平衡上下文包：`PER-lavrov` (彼得·拉夫罗夫)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/people/PER-lavrov.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `movement-history-venturi, berlin-moral-humanism, intellectual-history-walicki, conceptual-history-mayer`
- **待补齐视角**: `post-soviet-biographical`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `post-soviet-biographical`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
俄国民粹派“准备派/宣传派（*lavristy*）”思想宗师与主观社会学奠基人。1823年生于普斯科夫省贵族家庭，1868–1869年发表《历史信札》，提出“批判思维的个人”对劳动人民负有沉重道德历史债务；1873年起主编《前进！》杂志，倡知识启蒙准备并发起对特卡乔夫“俄国雅各宾主义”的批判。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **炮兵学院数学教授、流放与《历史信札》（1823–1870）**：生于 `1823-06-02 [O.S.] / 1823-06-14 [N.S.]` 普斯科夫省梅列霍沃庄园；早年任圣彼得堡米哈伊洛夫炮兵学院数学教授（上校军衔），接近车尔尼雪夫斯基与第一代“土地与自由社”。1866年卡拉科佐夫刺杀亚历山大二世案后被捕，流放沃洛格达省；1868–1869年在《周报》（*Nedelia*）以笔名“米尔托夫（P. Mirtov）”连载《历史信札》（*Istoricheskie pis'ma*，1870年结集出版），提出人类文明与知识分子的智力特权皆以历代劳动大众的血汗牺牲为代价，故“批判思维的个人（*kriticheski mysliashchie lichnosti*）”必须以献身人民解放来清偿这笔沉重的道德历史债务——该书成为1870年代俄国青年投身“到民间去”运动的“福音书”（`CLM-berlin-1960-populism-moral-core`; `CLM-zelnik-1999-worker-intelligentsia-tutelage-tension`）。
- **巴黎公社洗礼与主编《前进！》的“准备派”路线（1870–1876）**：1870年2月在赫尔曼·洛帕廷协助下逃往巴黎，加入第一国际并亲历1871年巴黎公社（期间与蒲鲁东派少数派结盟并赴伦敦、布鲁塞尔为公社求援）。1873–1876年在苏黎世与伦敦主编《前进！》（*Vpered!*）杂志及双周报，确立与巴枯宁“造反派”并立的民粹主义“准备派/宣传派（*lavristy*）”路线：反对未经准备的盲目暴动与密谋政变，主张革命知识分子必须先深入民间开展耐心的科学宣传与社会主义意识启蒙，坚持社会革命只能“通过人民自己、而非仅仅为了人民”来完成。
- **铸造“俄国雅各宾主义”论战标签与晚年民意党外围领袖（1874–1900）**：1874–1876年与脱离《前进！》的特卡乔夫爆发激烈论战；拉夫罗夫在《致俄国社会革命青年》（1874）及《前进！》第34期（1876）上，借鉴巴黎公社蒲鲁东派话语，首次将特卡乔夫的少数人夺权专政论贴上“雅各宾理论 / 雅各宾社会主义者”的污名化标签（`CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism`）。1881年“三月一日事件”后，拉夫罗夫逐渐抛弃早期反政治斗争成见，与流亡的民意党人（季霍米罗夫等）合编《民意党通报》（*Vestnik Narodnoi Voli*，1883–1886），1889年作为俄国代表出席第二国际巴黎成立大会，`1900-02-06 [N.S.]` 在巴黎逝世。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-tkachev` | `polemical-opponent` | 1874–1876 | 围绕“长期启蒙准备”与“少数派密谋夺权”激烈交锋，拉夫罗夫首次发明“俄国雅各宾主义”标签批判特卡乔夫 | `CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism` |
| `PER-bakunin` | `populist-rival-pole` | 1873–1876 | 拉夫罗夫“准备派（*lavristy*）”与巴枯宁“造反派（*buntari*）”共同主导1874“到民间去”运动，分别强调理性启蒙与本能暴动 | `CLM-berlin-1960-populism-moral-core`, `RN-W2-zemlya-to-march-first` |
| `PER-chernyshevsky` | `intellectual-successor` | 1860s–1900 | 继承车尔尼雪夫斯基60年代激进启蒙精神，并将其转化为以“向人民偿还历史债务”为核心的主观社会学 | `CLM-walicki-1969-narodnichestvo-definition` |
| `ORG-narodnaya-volya` | `critic -> emigré-co-editor` | 1879–1886 | 早期警惕密谋专政，1881年后作为流亡元老与季霍米罗夫合编《民意党通报》支撑残余组织 | `RN-W2-zemlya-to-march-first`, `CLM-berlin-1960-populism-moral-core` |
| `CON-narodnichestvo` | `theoretical-pillar` | 1869–1900 | 与米海洛夫斯基共同构建古典民粹主义的“主观社会学”与伦理个人主义哲学支柱 | `CLM-berlin-1960-populism-moral-core`, `CLM-walicki-1969-narodnichestvo-definition` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：拉夫罗夫的《历史信札》（1868–1869）为1870年代俄国激进知识分子提供了最核心的道德动员话语（“批判思维的个人”与“向人民偿债”），其主编的《前进！》代表了民粹运动中重宣传、反密谋的“准备派”一翼。
- **主要解释分歧**（详参 `DEB-1879-narodnaya-volya-to-bolshevism`）：
  - **[伯林道德人文主义与反历史决定论 / Isaiah Berlin]**（`CLM-berlin-1960-populism-moral-core`）：高度评价拉夫罗夫（与赫尔岑、米海洛夫斯基）的“主观社会学”内核——坚持历史并无预设的客观必然性，社会理想源于人的道德选择，且绝不能以未来乌托邦或“历史规律”为由牺牲当下个体的自由与良知（`pp. xviii–xxvi`）。
  - **[梅耶概念史解构 / Robert Mayer]**（`CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism`）：考证“俄国雅各宾传统”并非密谋派的自我认同，而是拉夫罗夫在1874–1876年受巴黎公社蒲鲁东派影响，为污名化论敌特卡乔夫而混淆“雅各宾派”与“布朗基派”所铸造的论战武器（`pp. 133–136`）。
  - **[瓦利茨基马克思主义与民粹主义比较 / Andrzej Walicki]**（`CLM-walicki-1969-narodnichestvo-definition`, `CLM-walicki-1969-plekhanov-rational-reality`）：指出在狭义“群众高于知识精英”定义下拉夫罗夫派甚至不算典型民粹派，但在广义反资本主义与“主观社会学”维度上，拉夫罗夫与米海洛夫斯基构成了普列汉诺夫、斯特鲁维和列宁在1880–1890年代批判“历史唯心主义”的首要理论靶子（`pp. 3–4, 16, 146–147, 160–164`）。
  - **[劳工社会史视角 / Reginald E. Zelnik & Steve A. Smith]**（`CLM-zelnik-1999-worker-intelligentsia-tutelage-tension`）：指出拉夫罗夫“批判思维的个人”与“忏悔贵族向人民偿债”的心态，在1870年代至1905年塑造了俄国知识分子（*intelligentsia*）的文化启蒙使命感，但同时也埋下了对“黑暗群众”的家长式监护（tutelage）张力，最终招致圣彼得堡“觉悟工人”对“知识分子替罪良心”的激烈反抗（`pp. 3–4, 19`）。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `EVT-1874-going-to-the-people`
- **时效关系边** (`PER-lavrov` → `EVT-1874-going-to-the-people` | `moral-debt-theorist` | 有效时段: `1869-1876`): 以《历史信札》号召“批判思维的个人”向劳动人民偿还历史道德债务，塑造民粹派长期宣传准备路线。
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
