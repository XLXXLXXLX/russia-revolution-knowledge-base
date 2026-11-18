# 1-Hop 平衡上下文包：`PER-rakovsky` (克里斯蒂安·拉柯夫斯基)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/people/PER-rakovsky.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `nationalities-archival-smith, left-opposition, deutscher-tragedy, balkan-internationalism`
- **待补齐视角**: `full-romanian-period-archival`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `full-romanian-period-archival`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
拉柯夫斯基（1873–1941），巴尔干国际社会主义者，1919–1923任乌克兰人民委员会主席；1923年十二大同伏龙芝猛批斯大林大俄罗斯沙文主义；1927年起为左翼与联合反对派核心，1928流放中撰《“职业危险”与苏维埃权力》拒向斯大林投降。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **巴尔干社会主义与国际主义（1873–1917）**：生于 `1873-08-01 [O.S.] / 1873-08-13 [N.S.]` 奥斯曼帝国保加利亚科特伦，成长于罗马尼亚社会主义运动；长期活跃于第二国际巴尔干与俄国流亡革命圈，十月革命后加入俄共（布）。
- **乌克兰苏维埃政府（1919–1923）**：1919–1923年任乌克兰苏维埃人民委员会主席兼国防委员，主持饥荒战争与征粮危机中的共和国行政，同时代表乌克兰语文化与自治诉求进入俄共民族辩论中心。
- **十二大民族妥协（1923）**：`1923-04` 俄共十二大民族问题特别会议上，拉柯夫斯基联合伏龙芝猛烈批评斯大林论纲的财政—行政掠夺边疆倾向，迫使决议写入本土化（Korenizatsiia）、民族院否决权与反大俄罗斯沙文主义条款（`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`）。
- **左翼—联合反对派（1923–1927）**：1923年民族辩论后继续与托洛茨基、季诺维也夫阵营合流；1926–1927年联合反对派要求恢复党内民主与计划改革，在1927年十五大路线摊牌中被开除中央并驱逐出莫斯科。
- **流放、著述与拒绝投降（1928–1941）**：1928年发配中亚后撰写《“职业危险”与苏维埃权力》，以保加利亚语、法语原文剖析苏维埃官僚等级形成“新资产阶级”与权力异化，拒绝斯大林要求的公开悔过；多次流放升级，1941年斯大林大清洗中在奥伦堡监狱被处决。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `MTG-1923-04-12th-party-congress` | `co-forced-compromise` | 1923-04 | 指责中央掠夺加盟共和国，逼斯大林民族政策让步 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` |
| `PER-frunze` | `allied-critic` | 1923 | 十二大民族特别会议同声批判大俄罗斯行政集权 | Smith `pp. 321–325` |
| `PER-stalin` | `rival` | 1923–1928 | 民族战线 compromise 后转入派别清洗目标 | Smith；Deutscher |
| `ORG-left-and-united-opposition` | `core-leader` | 1926–1927 | 与托洛茨基、季诺维也夫共建最后合法反对派联盟 | `CLM-deutscher-1959-united-opposition-defeat` |
| `POL-korenizatsiia` | `architect-debater` | 1923–1927 | 作为乌克兰领袖推动 1920 年代本土化制度化辩论 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：拉柯夫斯基 1919–1923 年任乌克兰苏维埃政府首脑；1923 年十二大速记有其攻击斯大林集权的实录发言；1927 年反对派失败后遭流放；1941 年被处决。
- **主要解释分歧**：
  - **[Jeremy Smith 解密档案派]**：十二大不宜读作斯大林民族政策完胜，拉柯夫斯基—伏龙芝一带边疆领袖曾实质性改写决议（`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`）。
  - **[Isaac Deutscher 反对派悲剧史]**：拉柯夫斯基与托洛茨基同陷“先知被解除武装”困局——既反对官僚化又无法脱离一党专政前提寻找制度出口（`CLM-deutscher-1959-disarmed-prophet-paradox`；`CLM-deutscher-1959-united-opposition-defeat`）。
  - **[苏联正史与后苏联民族史学]**：旧版党史将其塑造为“托派—孟什维克间谍”，1990 年代档案转向强调其 1923 年民族妥协推动者身份，却仍较少整合其 1928 官僚阶级异化理论。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `ORG-left-and-united-opposition`
- **时效关系边** (`PER-rakovsky` → `ORG-left-and-united-opposition` | `unyielding-theorist` | 有效时段: `1923-1929`): 1923十二大批判大俄罗斯集权后成为左翼与联合反对派二号领袖，1928在流放地撰写《“职业危险”与苏维埃权力》剖析官僚阶层异化并拒不投降。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1923年剪刀差危机触发的托洛茨基—普列奥布拉任斯基等“左翼反对派”，经1926年春与季诺维也夫—加米涅夫“新反对派”合并为托季联合反对派；以《四十六人声明》与1927年政纲挑战党内官僚化与“一国社会主义”，在机关机器、社会冷漠与派别禁令下于1927年十五大前后溃败。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1923-nationality-and-empire`：布尔什维克民族政策、格鲁吉亚事件与苏维埃“肯定性行动帝国”性质之争
## [T1] 核心问题定义
1922—1923年格鲁吉亚冲突与十二大民族妥协，布尔什维克是在建设多民族“帝国”内的肯定性本土化福利国，还是以先锋队垄断维系的大俄罗斯官僚集权？争论焦点是经验制度成果与各派因果—价值判断之分。

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 列宁晚期斗争论 | Moshe Lewin, *Lenin's Last Struggle* (1968) | 格鲁吉亚事件暴露大国沙文主义与官僚机器合流，列宁晚年誓以政治清算对抗 *dzerzhimordy*；民族问题是撤换斯大林问责的实质切口之一。 | `CLM-lewin-1968-georgian-affair-bureaucracy`; `CLM-lewin-1968-testament-intent` | 易将散落笔记读成连贯“遗嘱计划”；未充分吸纳1990年代解密全会速记。 |
| 自由主义—极权连续论 | Richard Pipes, *Russia under the Bolshevik Regime* 等 | 苏联民族政策是先锋队专政逻辑的延伸；十二大被写作斯大林中央集权对自治的胜利（Smith 正面驳斥此说）。 | （经 `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` 对勘引述） | 档案研究显示十二大民族妥协比“一方全胜”叙事更复杂。 |
| 解密档案民族妥协论 | Jeremy D. Smith, *The Bolsheviks and the National Question, 1917–1923* (1999) | 列宁—斯大林在集权原则上确有共识，但十二大特别会议显示边疆代表迫使中央退让，奠定1920年代本土化相对稳固期；格鲁吉亚危机不宜简化为二人生死对决。 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`; `CLM-smith-jeremy-1999-georgian-affair-reassessed` | 本土化繁荣期止于1930年代逆转，分期须清晰。 |
| 帝国史学框架 | Ronald Grigor Suny, *The Red Flag Unfurled* (2017) 等 | 沙俄—苏联宜在“宗主—边缘不平等从属”的帝国框架下理解民族建构；1991年后“苏联=帝国”共识含事后归因风险。 | `CLM-suny-2017-empire-and-nationality-dimension` | 帝国理论有助于宏观定位，但不能替代全代会速记级制度考证。 |
| 乌克兰社会史与本土化悖论 | George Liber, *Soviet Nationality Policy, Urban Growth, and Identity Change in the Ukrainian SSR 1923–1934* (1992) | 本土化整合城乡乌克兰人、扩张乌克兰语公共领域的同时，制度化语言分裂并孕育难以中央完全消化的地方民族诉求。 | `CLM-liber-1992-korenizatsiia-paradox-late-1920s`; `CLM-liber-1992-ukrainianization-and-urban-working-class` | 侧重乌克兰案例，外高加索与中亚须分区域检验。 |
| “肯定性行动帝国”概念（史学界常用语） | Terry Martin, *The Affirmative Action Empire* (2001) 等 | 1920年代苏联对“前发达”民族实施制度化优待（干部、语言、教育配额），以党国垄断为前提整合帝国边缘——成功与潜在离心并存。 | （本库待补 `CLM-martin-2001-affirmative-action-empire`；可 interim 参照 `reading-notes/` 与 `POL-korenizatsiia`） | 术语易与美式种族平权政策混同，须严守苏联党国语境。 |

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

## 4. 关联时间线锚点 (共 0 条)
