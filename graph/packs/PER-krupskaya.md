# 1-Hop 平衡上下文包：`PER-krupskaya` (娜杰日达·康斯坦丁诺夫娜·克鲁普斯卡娅)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/people/PER-krupskaya.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `bolshevik-women-leadership, enlightenment-institutional, opposition-history, archival-post-soviet`
- **待补齐视角**: `krupskaya-full-memoir-critical-edition`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `krupskaya-full-memoir-critical-edition`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
娜杰日达·克鲁普斯卡娅（1869–1939，本卡至1929）：列宁终生伴侣与1901年起《火星报》秘密通信总干事，苏俄政治启蒙总局主任；1922–1923守护并移交《列宁遗嘱》，1925年十四大加盟季诺维也夫—加米涅夫新反对派，1926年秋退出联合反对派。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **新型革命知识分子与《火星报》网络（1890s–1903）**：生于 `1869-02-14 [O.S.] / 1869-02-26 [N.S.]` 圣彼得堡；中学教员出身，1890年代参加彼得堡工人阶级解放斗争协会。1898年与列宁在西伯利亚舒申斯科耶流放地结婚；**1901年春刑满赴慕尼黑后**出任《火星报》编辑部秘密通信总干事，执掌密码联络与俄国境内代办员网络，是布尔什维克早期地下机器的组织中枢（其《列宁回忆录》须严格区分 **[B级在场见证]** 与 **[1920年代末政治阐释]**）。
- **十月前后与启蒙体制（1917–1922）**：布尔什维克掌权后任 **教育人民委员部政治启蒙总局（Главполитпросвет）** 主任，推动扫盲、工人夜校、政治教育与社会文化机构，体现“教养—组织”并行的革命文化政策（`CLM-hoffmann-2011-enlightenment-and-coercion-duality` 引克鲁普斯卡娅—杜威式个人教养话语为文化革命维度之一）。
- **列宁病重、遗嘱与斯大林冲突（1922–1923）**：1922年12月斯大林因克鲁普斯卡娅代列宁致托洛茨基通信事宜 **电话斥责** 并威胁中监委处分（timeline `TL-W8-1922-12-22-01` 等，日期考证见 Kotkin 对1923年1月重定争论）；列宁 `1923-03-05` 致函要求斯大林道歉否则断交。克鲁普斯卡娅参与保存并推动落实列宁 **《给代表大会的信》**（`CLM-lewin-1968-testament-intent`：莱文强调遗嘱是反官僚与撤换斯大林之总体纲领，不仅是人性品评）。
- **继承斗争与反对派（1924–1926）**：`1924-05` **十三大** 克鲁普斯卡娅转交遗嘱，遭季诺维也夫—加米涅夫封闭宣读、力保斯大林（`MTG-1924-05-13th-party-congress`）。`1925-12` **十四大** 她站在 **季诺维也夫—加米涅夫“新反对派”** 一边，反对斯大林个人独裁化（`CLM-zhukov-zinoviev-1925-leningrad-opposition` 列宁格勒反对派背景）。`1926` 与托洛茨基等人组建 **联合反对派** 后又 **`1926` 脱离** 该联盟，未再承担反对派领导角色（至1929年仍任中央委员，但政治边缘化）。
- **1927–1929余波（断代注）**：1927年后未主导反对派运动；1929年仍居正式职务但不再构成权力枢纽——本卡断代至1929年斯大林击败布哈林集团与“大转变”定局之知识库边界。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | `partner-organizer` | 1890s–1924 | 火星报联络与党内组织互补列宁政治领袖角色 | Carr 革命史；Krupskaya *Memories* [B级] |
| `PER-stalin` | `conflict-then-opposition` | 1922–1926 | 1922–23电话辱骂事件与遗嘱守护框定终身对立 | `CLM-lewin-1968-testament-intent`；timeline 1922-12 |
| `PER-trotsky` | `temporary-alignment` | 1925–1926 | 十四大—联合反对派阶段短期合流，1926年退出 | `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-zinoviev` | `ally` | 1925 | 新反对派中共同挑战斯大林 | `CLM-zhukov-zinoviev-1925-leningrad-opposition` |
| `PER-kamenev` | `ally` | 1924–1925 | 1924年十三大与其共同封存遗嘱政治后果相连；1925反对斯大林 | `CLM-khlevniuk-2015-collective-leadership-erosion` |
| `MTG-1924-05-13th-party-congress` | `entrusted-testament` | 1924.05 | 转交列宁遗嘱而遭分团宣读、非罢免斯大林 | `MTG-1924-05-13th-party-congress` |
| `MTG-1925-12-14th-party-congress` | `opponent` | 1925.12 | 加入反斯大林—布哈林多数派的新反对派阵营 | `MTG-1925-12-14th-party-congress` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：克鲁普斯卡娅是布尔什维克最早一批职业革命家；《火星报》秘密通信网由其实际运转；启蒙总局体现革命政权文化政策；她是列宁遗嘱文本保存与递交的关键参与者；1925—1926年曾是反对派名人之一，1926年后退出联合反对派。
- **主要解释分歧**：
  - **[遗嘱与篡权史 / Moshe Lewin]**：通过克鲁普斯卡娅递交的文本应读作列宁试图理性化专政、防官僚专政的总体方案，斯大林主义在精神上与之相反（`CLM-lewin-1968-testament-intent`）。
  - **[斯大林权力考古 / Oleg Khlevniuk, Stephen Kotkin]**：1922—1924年斯大林斥责克鲁普斯卡娅事件是书记处私自监控列宁私人通信与寡头封口遗嘱的制度链条一环，非孤立礼仪冲突（`CLM-khlevniuk-2015-collective-leadership-erosion`；Kotkin 传记中的日期—动机争论待专卡）。
  - **[启蒙—强制双重性 / David Hoffman]**：克鲁普斯卡娅启蒙网展示苏联“培养群众”冲动，与契卡清除暴力同属现代国家治理谱系，不宜浪漫化为纯粹人道主义教育（`CLM-hoffmann-2011-enlightenment-and-coercion-duality`）。
  - **[列宁格勒反对派史 / Zhukov 等]**：1925年克鲁普斯卡娅与季诺维也夫结盟须放回列宁格勒机器与 industrialization 争论，而非个人恩怨剧（`CLM-zhukov-zinoviev-1925-leningrad-opposition`）。

## 2. 一跳邻域等权重微摘要 (共 2 个关联节点，严防大卡霸占上下文)
### 邻居节点: `MTG-1924-05-13th-party-congress`
- **时效关系边** (`PER-krupskaya` → `MTG-1924-05-13th-party-congress` | `submitted-lenin-testament` | 有效时段: `1924.05`): 在十三大前向中央移交列宁《给代表大会的信》，但遭季诺维也夫、加米涅夫与斯大林限制在代表团闭门宣读而未撤换总书记。
- **节点定性微摘要 [T1]** (完备度 `draft`): 1924年5月23–31日列宁逝世后首次党代会：各代表团闭门宣读《给代表大会的信（列宁遗嘱）》；季诺维也夫与加米涅夫担保斯大林留任总书记，多数派围剿托洛茨基《新方针》，巩固三驾马车对书记处的掌控。

### 邻居节点: `MTG-1925-12-14th-party-congress`
- **时效关系边** (`PER-krupskaya` → `MTG-1925-12-14th-party-congress` | `new-opposition-speaker` | 有效时段: `1925.12`): 在十四大与季诺维也夫、加米涅夫、索科尔尼科夫结盟反对对富农过度退让，并在大会讲坛提醒“多数派未必永远正确”。
- **节点定性微摘要 [T1]** (完备度 `draft`): 1925年12月莫斯科十四大上，斯大林—布哈林多数派击败季诺维也夫、加米涅夫的“新反对派”；大会强调工业化，并将党名改为全联盟共产党（布尔什维克）。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
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

## 4. 关联时间线锚点 (共 0 条)
