# 1-Hop 平衡上下文包：`MTG-1927-12-15th-party-congress` (联共（布）第十五次代表大会)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/meetings/MTG-1927-12-15th-party-congress.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `trotskyist-biographical-deutscher, archival-post-soviet-khlevniuk, economic-foundations-carr-davies`
- **待补齐视角**: `rural-social-history, delegate-social-history`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `rural-social-history, delegate-social-history`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1927年12月2—19日莫斯科举行。大会追认11月对托洛茨基、季诺维也夫的开除党籍处分，并于12月18日另行开除加米涅夫等75名托季联合反对派骨干及萨普罗诺夫派；同时通过编制首个五年计划指示与渐进合作化—集体化决议，开启NEP末期转折前奏。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **会前开除与大会分批组织清洗的严格区分（1927.11.14 vs 1927.12.18）**：托洛茨基与季诺维也夫已于会前 `1927-11-14` 被中央委员会与中央监察委员会联席会议直接开除出党（此前 `1927-10-23` 被逐出中央委员会）。`1927-12-02` 十五大开幕时反对派已无正式表决权代表；`1927-12-03` 斯大林作中央政治报告，加米涅夫、拉柯夫斯基等发言遭全场打断；`1927-12-18` 大会正式追认对托、季二人的开除，并**另行宣布开除包括加米涅夫、皮达可夫、拉狄克、拉柯夫斯基、普列奥布拉任斯基在内的75名联合反对派积极分子**，同时开除萨普罗诺夫“民主集中派”（十月集团）23人名单（**严禁将大会开除的“75人”误计为包含会前已被开除的托、季二人在内的总数**；`CLM-deutscher-1959-united-opposition-defeat`）。
- **反对派阵营分裂与“六个月考察期”悔过处置（1927.12.10–19）**：`1927-12-10` 托派与季派因是否声明放弃宣传反对派观点正式破裂；`1927-12-18—19` 季诺维也夫、加米涅夫等提交放弃派别活动并承认违反党纪的悔过声明，但 `1927-12-19` 闭幕大会拒绝立即集体恢复其党籍，规定须以个人身份单独申请并经至少六个月考察；托洛茨基、拉柯夫斯基等拒绝投降，于1928年1月遭流放（`CLM-deutscher-1959-united-opposition-defeat`）。
- **五年计划编制指示、自愿集体化口径与粮食危机潜流（1927.12）**：大会通过李可夫、克尔日扎诺夫斯基主持的**关于编制国民经济第一个五年计划的指示**（系编制原则而非1929年4月最终批准的最高方案），并通过莫洛托夫农村工作报告，提出逐步扩大集体农庄与国营农场、限制富农剥削，但明文仍保留NEP市场交换与自愿入社原则——**不可目的论地混同于1929年底全盘强制集体化与“消灭富农阶级”**。与此同时，大会开会期间（`1927-12-14` 与 `12-24`）中央已两度向产粮区发出催征粮食紧急指示，预示 `1928-01` 非常措施与斯大林—布哈林决裂迫在眉睫。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-left-and-united-opposition` | `liquidated-at` | 1927-12-18 | 大会开除75名骨干并促发季—托两翼分裂，联合反对派作为党内有组织联盟终结 | `CLM-deutscher-1959-united-opposition-defeat`; `ORG-left-and-united-opposition` |
| `PER-trotsky` | `expulsion-ratified` | 1927-11-14开除；12-18追认 | 会前已被开除党籍，十五大予以追认并拒绝妥协，次年1月流放阿拉木图 | `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-zinoviev` | `expulsion-ratified -> recantation` | 1927-11至12-19 | 会前开除，大会闭幕际与加米涅夫提交悔过书，被勒令经六个月考察再个别审理 | `CLM-deutscher-1959-united-opposition-defeat`; ` Zhukov ch21` |
| `PER-kamenev` | `expelled -> recantation` | 1927-12-18至12-19 | 列入大会开除的75人名单，随即联署悔过声明与托洛茨基派决裂 | `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-stalin` | `leader` | 1927-12 | 主导彻底清除左翼反对派，会后一中全会以口头请辞总书记试探并强化政治局核心顺从 | `CLM-khlevniuk-2015-collective-leadership-erosion` |
| `POL-first-five-year-plan` | `directives-adopted-at` | 1927-12 | 大会通过编制首个五年计划的框架性指示，尚带工农平衡约束而非1929年高指标定稿 | `POL-first-five-year-plan`; `DEB-1928-bukharin-alternative` |
| `POL-nep` | `policy-context` | 1927-12 | 表面重申NEP框内渐进合作化，实则同期秋冬季粮食收购危机已在掏空市场交换基础 | `DEB-1928-bukharin-alternative`; `DEB-1929-collectivization-and-dekulakization-causes` |

### 2.3 史学争鸣光谱
- **经验共识**：大会追认开除托洛茨基与季诺维也夫、另行开除75名托季反对派及萨普罗诺夫集团，通过编制一五计划指示及渐进农业合作化/集体化决议。
- **主要解释分歧**（详参 `DEB-1928-bukharin-alternative`, `DEB-1929-collectivization-and-dekulakization-causes`）：
  - **[传记与社会气氛论 / Isaac Deutscher]**（`CLM-deutscher-1959-united-opposition-defeat`）：指出十五大对反对派的粉碎不仅靠代表遴选机器，更根源于革命疲惫下全国工农的“可怕寂静”与反对派自我束缚于一党纪律之内。
  - **[后苏联政治局制度史 / Oleg Khlevniuk]**（`CLM-khlevniuk-2015-collective-leadership-erosion`）：强调1927年12月清除左翼后，斯大林在 `1927-12-19` 新选中央一中全会上以“列宁遗嘱任务已履行、请求免去总书记”作试探获布哈林、李可夫一致挽留，但政治局寡头共治要到1928—1929年击溃右派后才最终瓦解。
  - **[计划经济与农村史分期论 / Carr & Davies; Cohen]**（`CLM-carr-davies-1969-nemchinov-table-critique`, `CLM-cohen-1973-nep-viability`）：反对苏联教科书将十五大直接等同于“全盘集体化代表大会”，强调十五大文本仍规定农业集体化须建立在自愿与机器物质技术基础之上，与1929年底行政强推存在重大政策断裂。

## 2. 一跳邻域等权重微摘要 (共 0 个关联节点，严防大卡霸占上下文)
- _当前 `graph/edges.jsonl` 中尚无关联边。_
## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1928-bukharin-alternative`：“布哈林替代方案”与新经济政策终结之争（1928–1929）
## [T1] 核心问题定义
1927–1929年新经济政策瓦解与斯大林击败布哈林集团，究竟源于小农低商品率与布尔什维克高工业化/价格管制目标之间无法调和的结构性死结，还是源于1926–1928年具体经济政策失误与党内权力机器垄断扼杀了布哈林所主张的市场-合作社均衡工业化替代路径？

## [T2] 各学派立场对照矩阵

| 学派/研究取向 | 代表学者与馆藏著作 | 核心论点摘要 | 已核实馆藏依据 | 主要受批评局限 |
| :--- | :--- | :--- | :--- | :--- |
| **政治传记“替代方案论”** | Stephen F. Cohen (`cohen_1973_bukharin`) | 新经济政策并未枯竭；布哈林基于列宁《论合作社》与《经济学家札记》（1928-09-30）提出了协调工农利益的可行渐进规划；但1928年1月政治局起初一致批准临时非常措施（p. 278），随后斯大林将其升级为常态路线并凭组织机器获胜。 | Cohen pp. 177, 278, `PDF p. 318` | 被批评高估了布哈林方案在重工业资本积累缺口与布尔什维克反市场意识形态下的政治可持续性。 |
| **农村社会史与长短周期分离论** | Moshe Lewin (`lewin_1968_peasants`) | 区分1927–28年粮食危机与1929–30年冬全盘强制集体化：同情渐进合作化，但直言布哈林部分理论“仅在短期有效”，而普列奥布拉任斯基对中长期工业投资瓶颈的诊断更具预见性（Preface `PDF p. 12`）。 | Lewin `PDF pp. 10, 12, 68` | — |
| **发展经济学与计划经济史派** | Alexander Erlich (`erlich_1960_industrialization`)、Carr & Davies (`carr_davies_1969_foundations_v1p1`)、Alec Nove (`nove_1964_was_stalin_necessary`) | Erlich 证明1924–28论战双方（含普列奥布拉任斯基，pp. 44, 177）均未预设暴力全盘集体化；Carr & Davies 与 Nove 揭示国家人为压低谷物收购价（相对于畜牧和经济作物）及工业品饥荒造成1927冬收购锐减。 | Erlich pp. 44, 177; Carr & Davies Vol.1 | 经济上本可通过调价与温和税收缓和，但与党领导层既定超高速军重工业目标直接冲突。 |
| **政治局体制与新经济政策死胡同论** | Oleg Khlevniuk (`khlevniuk_2015_stalin`) | 一方面指出1927年危机表明新经济政策发展模式受多重因素制约已难以为继（Ch. 3）；另一方面从中央书记处干部任命制（Nomenklatura）与政治局纪律剖析布哈林集团为何在组织上迅速瓦解。 | Khlevniuk EPUB Ch. 3 | 偏重高层权力与体制锁死，对非强制替代经济路径的计量效率讨论较少。 |
| **意识形态死结与能动性决断论** | Stephen Kotkin (`kotkin_2014_stalin_v1`, Ch. 13–14 & Coda) | “新经济政策若经济成功便在布尔什维克阶级政治上自我失败”（商品粮依赖大播户即潜伏“富农”）；但同时反对结构宿命论，指出若无斯大林1928年1月西伯利亚督粮的个人铁腕决断，强制全盘集体化概率极低。 | `CLM-kotkin-2014-siberian-grain-turn`, `CLM-kotkin-2014-bukharin-dilemma` | 第1卷叙事止于1928年底，1929年4月与11月全会交锋待补第2卷与全会速记。 |

### `DEB-1929-collectivization-and-dekulakization-causes`：1929年全盘集体化与消灭富农阶级动因总公案
## [T1] 核心问题定义
1929年秋斯大林体制性推进全盘集体化并宣布“消灭富农作为阶级”，究竟是因为新经济政策（NEP）道路在工农价格剪刀差与工业化投资缺口下已结构性破产、布哈林渐进方案被权力机器扼杀（还有何种替代仍可能），还是因为1927–28粮食统计失真、地方征粮竞速与所谓“战争恐慌”触发的螺旋，再叠加领袖对外备战焦虑与反市场意识形态而成为一种可被避免却未被避免的急转弯？

## [T2] 各学派立场对照矩阵

**经验共识**：1927冬—1928春出现严重粮食收购危机；1928年1月西伯利亚“非常措施”与乌拉尔-西伯利亚方法将行政强制包装为村社压力（`POL-ural-siberian-method`）；1929年4月与11月中央全会后集体化指标急剧跃升；1929年12月通过关于富农政策措施，公开的阶级清洗话语制度化。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **布哈林 NEP 可行替代论** | Stephen F. Cohen, *Bukharin and the Bolshevik Revolution* (1973); Moshe Lewin, *Russian Peasants and Soviet Power* (1968) | Cohen：1928年布哈林仍提出可调节市场—合作社渐进工业化；斯大林将临时征粮升级为路线并凭组织拳头获胜。Lewin：区分1927–28危机与1929–30暴力集体化，警告勿将“富农”范畴自然化。 | `CLM-cohen-1973-nep-viability`, `CLM-cohen-1973-bukharin-organizational-defeat`, `CLM-cohen-1973-notes-of-an-economist`, `CLM-lewin-peasants-1968-grain-procurement-crisis`, `CLM-lewin-peasants-1968-kulak-myth-and-serednyak`, `CLM-lewin-peasants-1968-ural-siberian-method` | 替代方案在政治意识形态与国防重工业目标下是否可赢得多数派，争议未终结。 |
| **统计失真与地方竞速螺旋论** | R. W. Davies, *The Socialist Offensive* (1980) 及集体化史系列；Nikolai Ivnitskii（富农消灭过程档案研究） | Davies：批判将1929秋单纯回溯为1928秋“大转变已定局”的史学叙事；地方各级党委在指标竞赛中层层加码。Ivnitskii：实际操作中“富农”划界高度政治化且地区差异巨大。 | `CLM-davies-1980-autumn-1929-great-turn-fabrication`, `CLM-davies-1980-november-plenum-to-dekulakization` | 计量史学与农村社会史接点仍薄；Ivnitskii 著作本库精读未完。 |
| **外部备战焦虑与意识形态死结论** | Stephen Kotkin, *Stalin*, vol. 1 (2014); David R. Shearer（警察国家与工业化）；Lynne Viola 等集体化执行史 | Kotkin：新经济政策在经济成功时亦在布尔什维克阶级政治上自我失败；1928斯大林个人决断打开全盘集体化概率。Shearer/Velikanova 补充高压执行与恐慌政治。 | `CLM-kotkin-2014-siberian-grain-turn`, `CLM-kotkin-2014-bukharin-dilemma`, `CLM-kotkin-2014-geopolitics-and-ideology`, `CLM-velikanova-2013-war-scare-hoarding-and-grain-crisis`, `CLM-velikanova-2013-leadership-manipulation-and-self-deception` | Kotkin 第1卷止1928底；1929全会细节待续卷与速记。 |
| **结构与投资缺口论** | Alexander Erlich (1960); Oleg Khlevniuk (2015) | Erlich：论战各方1924–28均未预设暴力全盘集体化，但工业投资瓶颈真实。Khlevniuk：政治局体制与新经济政策“死胡同”从组织面解释布哈林集团迅速溃败。 | `CLM-erlich-1960-preobrazhensky-dilemma`, `CLM-erlich-1960-stalin-overkill-turn`, `CLM-khlevniuk-2015-secretariat-and-nomenklatura` | 结构制约论易被误读为取消领袖能动性或农民抵抗作用。 |

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
