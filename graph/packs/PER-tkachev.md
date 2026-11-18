# 1-Hop 平衡上下文包：`PER-tkachev` (彼得·特卡乔夫)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/people/PER-tkachev.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `movement-history-venturi, marx-engels-critique, jacobin-lenin-genealogy-debate`
- **待补齐视角**: `post-soviet-biographical`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `post-soviet-biographical`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
俄国革命民粹派政论家、《警钟》（*Nabat*）主编。系统阐述落后国由纪律化少数派密谋夺权、革命后党临时专政的“俄国雅各宾主义”；1870年代与恩格斯公开论战；其是否构成列宁主义组织与专政观念之“直系先驱”在东西方马克思主义史学中长期存在激烈争鸣。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **早年激进与狱中学说（1844–1870）**：生于 `1844-06-29 [O.S.] / 1844-07-11 [N.S.]`（通行校正，具体日序待核教区记录）**普斯科夫省大卢基县锡夫佐沃村**小贵族家庭；在**圣彼得堡大学在学期间**即因参与学生抗议与革命地下活动多次被捕并遭拘押流放（非毕业后始入革命）；在狱中及流放期间持续写作，把法国大革命雅各宾派与布朗基主义经验移植为沙皇俄国落后社会的夺权模型。
- **《警钟》与组织铁律（1875年起，1879年后仍继续刊行）**：1875年底起在日内瓦主笔刊物《警钟》（*Nabat*），提出革命须由与外界隔绝、高度纪律的“有觉悟少数派”先行夺取国家机器，再以专政教育群众、废除私有制——被同时代人与后世称为“俄国雅各宾主义”；该刊成为连接土地与自由社革新派（含奥沙尼娜传统）与民意党密谋集中制的重要理论资源；需注意《警钟》在1879年土地与自由社分裂后**并未停刊**，而是延至1880年代初继续出版（具体续刊期数待核）。
- **与恩格斯论战（1874–1875）**：恩格斯在《流亡者文献》（*Flüchtlingsliteratur*）中的**《论俄国的社会问题》**（“On Social Relations in Russia”，1875）等文中批判特卡乔夫否认西方工人运动主导权、把落后俄国密谋夺权夸大为普遍解放路径；特卡乔夫反驳称俄国国家悬浮于社会之上且资本主义尚未根深蒂固，俄国革命党须抢先以国家政权自上而下完成社会主义改造——论战成为界定马恩与俄国民粹派分歧的经典文本（Walicki 兼论其对普列汉诺夫反布朗基立场的对照，`CLM-walicki-1969-plekhanov-rational-reality`）。
- **晚年与身后影响（1879–1886及以后）**：1879年前后与民意党执委会策略存在张力——文图里记执委会纲领抨击其“专制乌托邦”（*despotic Utopia*），拒绝将党永久专政常态化（`CLM-venturi-1960-narodnaya-volya-constitutionalism`）；`1886-01-04 [N.S.]`（巴黎当地公历）病逝巴黎；20世纪苏联部分史学将其与列宁职业革命家党类比，西方冷战史学亦有“特卡乔夫—列宁直系论”，但伯林强调列宁主义决定论世界观与民粹道德人文主义存在断裂（`CLM-berlin-1960-populism-moral-core`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-narodnaya-volya` | `theoretical-precursor-critical-reception` | 1879–1881 | 其雅各宾专政论为执委会所熟悉，但正式纲领明确排斥“专制乌托邦”，与奥沙尼娜—列别捷娃应急条款张力并存 | `CLM-venturi-1960-narodnaya-volya-constitutionalism` |
| `ORG-zemlya-i-volya` | `press-theorist` | 1876–1879 | 第二代土地与自由社时期以《警钟》为革新派提供少数派夺权理论弹药 | `CLM-venturi-1960-lipetsk-voronezh-split` |
| `PER-plekhanov` | `polemical-opposite` | 1879–1883 | 普列汉诺夫自沃罗涅日分裂起坚守反布朗基—反少数派夺权，转向阶段革命论与社会民主主义 | `CLM-walicki-1969-plekhanov-rational-reality` |
| `PER-lenin` | `genealogy-disputed` | 1902– | 苏联史学常把列宁《怎么办？》职业革命家党与特卡乔夫并置；伯林与部分西方史家质疑其道德哲学根基的亲缘度 | `CLM-berlin-1960-populism-moral-core` |
| `PER-zhelyabov` | `indirect-influence` | 1879–1881 | 热利亚博夫参与利佩茨克集中制章程，但民意党纲领对特卡乔夫式永久专政保持距离 | `CLM-venturi-1960-lipetsk-voronezh-split` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：特卡乔夫是19世纪俄国革命思想中少数派密谋夺权与革命党专政理论最系统阐发者之一，并与恩格斯发生直接公开论战。
- **主要解释分歧**（相关待建争鸣母题卡：`DEB-populism-morality-and-leninism`、`DEB-narodnichestvo-concept`）：
  - **[文图里运动史]**（`CLM-venturi-1960-narodnaya-volya-constitutionalism`）：民意党并非特卡乔夫主义的简单化身，而是在国家社会学与立宪会议纲领中对雅各宾专政论加以限制与“应急化”。
  - **[伯林道德人文主义谱系]**（`CLM-berlin-1960-populism-moral-core`）：民粹派秘密政党是高压下的临时工具，个人良知仍是最终审查官；列宁党的专政观念“源于截然不同的世界观”，不宜与特卡乔夫作线性同一化（同时承认组织技艺上的历史债务）。
  - **[苏联正统“列宁主义前史”]**：强调特卡乔夫—列宁在职业革命家党与专政问题上的积极继承，淡化民意党纲领对其的批判。
  - **[瓦利茨基反布朗基连续性]**（`CLM-walicki-1969-plekhanov-rational-reality`）：通过普列汉诺夫个案说明俄国马克思主义正道以**排斥**特卡乔夫式少数派夺权为内在起点，而非在其延长线上。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `ORG-narodnaya-volya`
- **时效关系边** (`PER-tkachev` → `ORG-narodnaya-volya` | `jacobin-pole` | 有效时段: `1875-1881`): 主张趁沙皇国家悬浮于薄弱资产阶级之上由少数密谋家立即夺权，但民意党执委会最终以立宪会议纲领拒绝了其纯粹少数派专政方案。
- **节点定性微摘要 [T1]** (完备度 `draft`): 1879年8月由第二代“土地与自由社”分裂产生的俄国激进民粹派秘密政党，由执行委员会（热利亚博夫、佩罗夫斯卡娅、菲格涅尔等）实行集中地下领导，将推翻沙皇专制、争取立宪会议的政治斗争置于首位；1881年刺杀亚历山大二世后遭严酷镇压，经1883年杰加耶夫叛变至1887年乌里扬诺夫密谋失败而瓦解。

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
