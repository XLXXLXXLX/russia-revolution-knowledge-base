# 1-Hop 平衡上下文包：`MTG-1924-05-13th-party-congress` (俄国共产党（布尔什维克）第十三次代表大会)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/meetings/MTG-1924-05-13th-party-congress.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `collective-leadership-archival, opposition-history, economic-transition-carr`
- **待补齐视角**: `regional-delegate-voting-behavior`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `regional-delegate-voting-behavior`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1924年5月23–31日列宁逝世后首次党代会：各代表团闭门宣读《给代表大会的信（列宁遗嘱）》；季诺维也夫与加米涅夫担保斯大林留任总书记，多数派围剿托洛茨基《新方针》，巩固三驾马车对书记处的掌控。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **开幕语境（1924.05）**：列宁于 `1924-01-21` 逝世后，新经济政策流通危机余波未平（1923年剪刀差及信贷杠杆争论延续至1924年初），党内围绕工业化节奏、工农联盟与国家计划化路线分歧表面化。
- **列宁遗嘱的封闭式宣读（1924.05）**：克鲁普斯卡娅向大会转交列宁1922–1923年口授的 **《给代表大会的信》**，其中批评斯大林粗鲁并建议撤换总书记职务。据多数党史叙述，**季诺维也夫** 与 **加米涅夫** 在代表团闭门会议上出面为斯大林担保，指摘公开遗嘱将有利反对派分裂党，决定不在全会公开宣读全文，仅向各代表团分别传达（`CLM-khlevniuk-2015-collective-leadership-erosion`；`CLM-lewin-1968-testament-intent`）。斯大林由此保住总书记职位，并为1924年8月“七人小组”寡头制续命。
- **对托洛茨基《新方针》的围剿（1924.05）**：斯大林—季诺维也夫—加米涅夫多数派利用托洛茨基仍在场这一政治样式，把公开挑战斯大林与“帮助托洛茨基”捆绑，在代表大会上发动针对托洛茨基 **《新方针》**（1923年秋党内民主与计划化主张）的批判。托洛茨基政治上进一步孤立，却尚未在十三大当即被开除（大规模清洗在1925–1927年反对派阶段展开）。
- **经济与组织决议（1924.05）**：大会在多数派框架内讨论收购价、合作社与信贷政策；代表会议争论为1924年后信贷收缩与工业合理化提供党内语境（与 `CLM-carr-1954-scissors-crisis-mechanics` 十三大速记参照）。组织上，总书记领导下的书记处名册人事权继续巩固。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | `posthumous-testament` | 1924.05 | 遗嘱批评斯大林粗暴与权力集中；实际处理方式是限制传播而非执行撤换 | `CLM-lewin-1968-testament-intent` |
| `PER-krupskaya` | `entrusted-testament` | 1924.05 | 转交并主张尊重遗嘱精神，遭多数派封存处理 | `CLM-lewin-1968-testament-intent`；timeline TL-W4-E09-1924-05-23 |
| `PER-stalin` | `reconfirmed-gs` | 1924.05 | 赖季诺维也夫—加米涅夫担保及托洛茨基在场的反对样式障碍连任 | `CLM-khlevniuk-2015-collective-leadership-erosion` |
| `PER-zinoviev` | `shielded-stalin` | 1924.05 | 与加米涅夫阻止遗嘱公开化，换取对托洛茨基的政治清算联盟 | Khlevniuk `ch06#L298–L331` |
| `PER-kamenev` | `shielded-stalin` | 1924.05 | 同上；1925年十四大才公开反对斯大林个人领导 | `MTG-1925-12-14th-party-congress` |
| `PER-trotsky` | `targeted-opponent` | 1924.05 | 《新方针》遭围剿，政治上失势但未在十三大立即开除 | `CLM-deutscher-1959-disarmed-prophet-paradox` |
| `CLM-carr-1954-scissors-crisis-mechanics` | `economic-backdrop` | 1923–1924 | 十三大代表会议讨论1923流通危机与李可夫“生产过剩”定性之争 | Carr `pp. 95–96` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：十三大是列宁死后首次代表大会；遗嘱以非公开、分团宣读方式处理；多数派在大会上压制托洛茨基反对派言论；斯大林留任总书记。
- **主要解释分歧**（详参 `DEB-1922-lenin-testament-and-stalin-rise`）：
  - **[遗嘱总体政治纲领派 / Moshe Lewin]**：遗嘱非单纯人事点评，而是反大国沙文主义、反官僚化与撤换斯大林的三重纲领；未被贯彻因寡头已无“无可争议领袖”执行政变式改组（`CLM-lewin-1968-testament-intent`）。
  - **[寡头集体领导档案派 / Oleg Khlevniuk]**：政治局同事深知列宁对斯大林担忧并曾试图限制书记处，但1924年5月选择以封闭遗嘱维系反托统一战线；此为集体领导的理性算计，非“低估庸人”（`CLM-khlevniuk-2015-collective-leadership-erosion`）。
  - **[悲剧先知叙事 / Isaac Deutscher]**：托洛茨基在十三大前后处于“被解除武装的先知”阶段——仍具英雄声誉却无法在派别禁令与书记处机器前组织有效反击（`CLM-deutscher-1959-disarmed-prophet-paradox`；与 `CLM-deutscher-1959-united-opposition-defeat` 衔接）。
  - **[经济史修正 / E. H. Carr]**：应把十三大放进1923剪刀差与销售危机辩论，而非仅读权力斗争戏曲（`CLM-carr-1954-scissors-crisis-mechanics`；`CLM-carr-1954-platform-of-46-economic-roots` 作1923—1924反对派经济根源前奏）。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `PER-krupskaya`
- **时效关系边** (`PER-krupskaya` → `MTG-1924-05-13th-party-congress` | `submitted-lenin-testament` | 有效时段: `1924.05`): 在十三大前向中央移交列宁《给代表大会的信》，但遭季诺维也夫、加米涅夫与斯大林限制在代表团闭门宣读而未撤换总书记。
- **节点定性微摘要 [T1]** (完备度 `draft`): 娜杰日达·克鲁普斯卡娅（1869–1939，本卡至1929）：列宁终生伴侣与1901年起《火星报》秘密通信总干事，苏俄政治启蒙总局主任；1922–1923守护并移交《列宁遗嘱》，1925年十四大加盟季诺维也夫—加米涅夫新反对派，1926年秋退出联合反对派。

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
