# 1-Hop 平衡上下文包：`ORG-left-and-united-opposition` (1923–1927年左翼反对派与托季联合反对派)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/organizations/ORG-left-and-united-opposition.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `biographical-deutscher, institutional-carr, conscience-daniels, archival-khlevniuk`
- **待补齐视角**: `factory-grassroots-opposition-networks`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `factory-grassroots-opposition-networks`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1923年剪刀差危机触发的托洛茨基—普列奥布拉任斯基等“左翼反对派”，经1926年春与季诺维也夫—加米涅夫“新反对派”合并为托季联合反对派；以《四十六人声明》与1927年政纲挑战党内官僚化与“一国社会主义”，在机关机器、社会冷漠与派别禁令下于1927年十五大前后溃败。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **1923年“四十六人声明”与左翼反对派成型（1923.10–1925.04）**：
  - `1923-10-08` 托洛茨基致信中央委员会，将工农不满与党内体制不健康并列指控（`CLM-carr-1954-platform-of-46-economic-roots`）。
  - `1923-10-15` **《四十六人声明》** 由皮达可夫、普列奥布拉任斯基、奥新斯基等46名干部签署，先诊断切尔文券、信贷、工业品滞销与农产品低价等新经济政策危机症状，再批判书记处专横（Carr pp. 113–115）。1924年列宁逝世后斯大林—布哈林—季诺维也夫“三驾马车”在“托洛茨基主义”问题上结阵反击。
- **1925年秋季诺维也夫转向与1926年联合反对派（1925.04–1927.06）**：
  - 1925年粮食紧张与秋季论治使季诺维也夫由“一国社会主义”共同起草者转为猛烈批判者；`1926-04` 托洛茨基与季诺维也夫—加米涅夫派系正式结盟组成 **联合反对派**，在十四次代表会议至十五大筹备期间就工业化速度、工农联盟、党内民主与“一国建成社会主义”展开全线论战（`CLM-deutscher-1959-united-opposition-defeat`, `CON-socialism-in-one-country`）。
- **1927年政纲、街头抗争与组织毁灭（1927.07–12）**：
  - 反对派秘密印制 **《1927年政纲》**（工业民主、无产阶级国际主义、反对官僚特权与非常措施），全签名者仅数千人规模；`1927-11-07` 十月革命十周年街头示威在列宁格勒与莫斯科遭驱散羞辱；`1927-11-14` 托洛茨基、季诺维也夫被开除党籍，加米涅夫等人随后悔过仍难翻盘；`1927-12` **十五大** 确认处分（`MTG-1927-12-15th-party-congress`, `CLM-deutscher-1959-united-opposition-defeat`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-trotsky` | `principal-leader` | 1923–1927 | 左翼反对派灵魂人物，1926年起与季诺维也夫并列联合反对派领袖 | `CLM-deutscher-1959-united-opposition-defeat`, `CLM-carr-1954-platform-of-46-economic-roots` |
| `PER-zinoviev` | `ally-1926 -> defeated-1927` | 1925 批判一国社会主义；1926–1927 与托结盟 | 从反托核心转为联合反对派的组织与宣传资源提供者 | `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-stalin` | `organizational-adversary` | 1923–1927 | 以书记处、报刊与选举机器压制反对派，将论战定性为托洛茨基主义分裂活动 | `CLM-khlevniuk-2015-secretariat-and-nomenklatura`, `CLM-khlevniuk-2015-collective-leadership-erosion` |
| `PER-bukharin` | `theoretical-adversary-1926-1927` | 1926–1927 | 新经济政策鼎盛期与斯大林联手在理论上批判不断革命论与反对派工业化方案 | `CLM-deutscher-1959-alma-ata-bukharin-stalin-split` |
| `CON-socialism-in-one-country` | `central-ideological-target` | 1925–1927 | 联合反对派将斯大林口号定性为背弃国际主义与掩盖官僚保守利益 | `DEB-1924-socialism-in-one-country` |
| `POL-ban-on-factions-1921` | `legal-constraint` | 1921起延续适用 | 1921年十大派别禁令使反对派只能在党纪框架内秘密串联传单 | `POL-ban-on-factions-1921`, `CLM-apalkov-2023-collective-to-personal-dictatorship` |
| `MTG-1927-12-15th-party-congress` | `defeated-at` | 1927-12 | 十五大确认开除与组织瓦解，开启1928年后斯大林对右派摊牌窗口 | `MTG-1927-12-15th-party-congress` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1923–1927年存在经《四十六人声明》与1926年结盟串联的党内左翼—托季联合反对派；其核心诉求包括纠正新经济政策危机、反对官僚特权、批判“一国社会主义”及主张更有计划的工业化与党内民主；1927年底在组织上被摧毁。
- **主要解释分歧**（详参 `DEB-1924-socialism-in-one-country`, `DEB-1922-lenin-testament-and-stalin-rise`）：
  - **[托派传记与社会心理论 / Isaac Deutscher]**（`CLM-deutscher-1959-united-opposition-defeat`, `CLM-deutscher-1959-disarmed-prophet-paradox`）：失败首要非政纲被经验证伪，而是全国“可怕寂静”与书记处舆论垄断；反对派自禁党外工人动员，在群众消极与恐惧安宁中耗尽。
  - **[经济—政治结构史 / E. H. Carr]**（`CLM-carr-1954-platform-of-46-economic-roots`, `CLM-carr-1954-scissors-crisis-mechanics`）：强调《四十六人声明》根植于1923年剪刀差与信贷危机的客观诊断，将党内专横批判置于经济政策失误之后，非纯粹权力野心。
  - **[反对派良心系谱 / Robert V. Daniels]**（`RN-W1C-communist-oppositions-1918-1929`）：将1923–1927年派别置于1918年以来“Leftist vs Leninist”连续体，突出其理想主义对权力实用主义的道德挑战（具体论断待独立CLM补卡）。
  - **[后苏联档案制度派 / Oleg Khlevniuk]**（`CLM-khlevniuk-2015-collective-leadership-erosion`, `CLM-khlevniuk-2015-secretariat-and-nomenklatura`）：1927年底斯大林组织优势显著，但政治局集体领导最终瓦解仍经历1928–1929右转全过程，不宜将1927年失败等同于个人独裁已定。
  - **[近年集体领导论 / Dmitry Apalkov]**（`CLM-apalkov-2023-collective-to-personal-dictatorship`）：反对派民主辞令与布尔什维克反分裂戒律结构性矛盾，使任何公开多政纲斗争注定失败。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `PER-trotsky`
- **时效关系边** (`PER-trotsky` → `ORG-left-and-united-opposition` | `principal-leader` | 有效时段: `1923.10-1927.12`): 从1923《新方针》到1926与季诺维也夫、加米涅夫结成联合反对派，要求恢复党内民主与加快计划工业化，于1927年底被彻底清洗。
- **节点定性微摘要 [T1]** (完备度 `draft`): 俄国马克思主义革命家、“不断革命论”提出者，曾任1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；主导十月军事革命委员会夺权，内战期任陆海军人民委员缔造正规红军。1923–1927年领衔左翼与联合反对派对抗斯大林书记处集权，1927年被开除出党，1929年2月被驱逐出苏联。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1924-socialism-in-one-country`：一国建成社会主义与不断革命论
## [T1] 核心问题定义
欧洲革命迟滞后，苏联能否凭国内资源建成社会主义，还是其完成须依赖国际革命？1924—1927年的论战同时涉及农民联盟、经济发展、国际安全与党内权力，不能把不同意义的“胜利”等同起来。

## [T2] 各学派立场对照矩阵

**经验共识**：斯大林与布哈林在反对左翼反对派时形成理论和政治联盟；季诺维也夫在1925年前后转而批评斯大林，1926年与托洛茨基等结成联合反对派。各方均以国际环境为问题，并非一方支持革命、另一方完全放弃国际事务。

| 立场或研究 | 核心论点及依据 | 争议和限制 |
| :--- | :--- | :--- |
| 斯大林、布哈林 | 苏联可以依靠工农联盟及国内建设发展社会主义；1925年党内文件区分国内建设的胜利与免受资本主义复辟和外部干预的最终保障。 | 两人论述及政策侧重点不完全相同，不能把1928年之后的分歧倒投到整个联盟时期。 |
| 托洛茨基及联合反对派 | 不断革命论强调革命发展跨越民主与社会主义任务、国内阶级关系与世界经济的相互依赖；孤立国家的社会主义完成依赖国际革命。 | 不等于主张等待外国革命而停止苏联经济建设；季诺维也夫的立场有自身演变。 |
| E. H. Carr, *Socialism in One Country*；Isaac Deutscher, *The Prophet Unarmed* | Carr把理论置于制度和国际关系发展的综合叙事中；Deutscher重视托洛茨基及党内政治斗争与国际革命前景。 | 各自叙事规模与政治解释不同，不应合并为统一学派；其具体论证仍需按章节细读。 |
| Stephen Kotkin, *Stalin*, vol. 1；萨哈罗夫（Sakharov）的相关研究待核 | Kotkin利用党内文本与档案追踪理论措辞及权力联盟；本地 Sakharov 文献可供核查党内权力机制。 | 不将萨哈罗夫预先归入任何确定立场：其本地著作的准确书目信息及与本争论的直接关系须核实。 |

### `DEB-1922-lenin-testament-and-stalin-rise`：列宁晚年、格鲁吉亚事件与斯大林崛起机制
## [T1] 核心问题定义
列宁晚年口授文稿和格鲁吉亚冲突，是反官僚与反斯大林的总体“最后斗争”，还是对共同集权框架内具体做法的修正？斯大林的上升又如何由个人策略、干部机关、集体领导与反对派困境共同解释？

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 修正派 | Moshe Lewin, *Lenin's Last Struggle* (1968) | 将晚年文稿读为反大国沙文主义、官僚主义及撤换斯大林的政治计划；但列宁未明确放弃禁派或强制。 | `CLM-lewin-1968-testament-intent`; `CLM-lewin-1968-georgian-affair-bureaucracy`; `CLM-lewin-1968-cooperation-shift` | 连贯“总体计划”的程度与其实施机会有争议。 |
| 民族政策修正 | Jeremy Smith, *The Bolsheviks and the National Question* (1999) | 强调列斯对集权原则的共识、地方利益及具体冲突，并据十二大特别会议材料揭示本土化妥协。 | `CLM-smith-jeremy-1999-georgian-affair-reassessed`; `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` | 行政协调解释需与民族代表对胁迫和权力不平等的证词对照。 |
| 后苏联档案与制度 | Oleg Khlevniuk, *Stalin* (2015) | 书记处议程和干部权带来优势；1920年代集体领导真实存在，其瓦解并非1922年已注定。 | `CLM-khlevniuk-2015-secretariat-and-nomenklatura`; `CLM-khlevniuk-2015-collective-leadership-erosion` | 不能将成熟时期干部名册规模倒推到1922年。 |
| 左翼传记与政治史 | Isaac Deutscher, *The Prophet Unarmed* (1959) | 反对派要求党内民主却维护党对政权的垄断，纪律机器成为其组织性困境。 | `CLM-deutscher-1959-disarmed-prophet-paradox`; `CLM-deutscher-1959-united-opposition-defeat` | 侧重托洛茨基与反对派，须结合机关和地方档案。 |
| 俄国政治思想史 | V. A. Sakharov (2012) | 将《论合作社》读为含有重要文本变化的遗产争夺；其关于后续集体化的判断是一种有争议解释，并非遗嘱真伪或格鲁吉亚事件的直接证据。 | `CLM-sakharov-2012-lenin-cooperative-plan-debates`; `CLM-sakharov-2012-nep-crossroads-1928` | 对布哈林及强制集体化的解释需要与其他史家交叉检验。 |

## 4. 关联时间线锚点 (共 0 条)
