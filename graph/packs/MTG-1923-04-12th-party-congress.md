# 1-Hop 平衡上下文包：`MTG-1923-04-12th-party-congress` (俄国共产党（布尔什维克）第十二次代表大会)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/meetings/MTG-1923-04-12th-party-congress.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `nationalities-archival-smith, economic-interregnum-carr, party-opposition-trotsky`
- **待补齐视角**: `full-stenogram-economic-commission`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `full-stenogram-economic-commission`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1923年4月17—25日莫斯科举行。列宁病重首次缺席全会，托洛茨基报告“剪刀差”并主张计划化工业化；大会秘密传达列宁民族问题笔记，民族特别会议通过本土化妥协决议，同时维持党的统一垄断。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **开幕背景与列宁缺席（1923.04.17起）**：大病后的列宁无法到会，十二大成为他生前最后一次党代会受到间接遥控的场合；克鲁普斯卡娅等受托在闭 door 分组会上传达其关于大国沙文主义与联盟体制的最后忧虑（与1922—1923年格鲁吉亚争论连贯，见 `DEB-1923-nationality-and-empire`）。
- **经济与“剪刀差”辩论（四月全会场）**：托洛茨基展示工农业价格指数分歧图，论证流通危机源于交换条件失衡，呼吁加强国家计划委员会职能、推进工业合理化（参见 `CLM-carr-1954-scissors-crisis-mechanics`）。多数派（斯大林、季诺维也夫等）倾向行政限价与信贷调节，未采纳反对派式系统计划化方案；会后国家银行信贷收缩成为合拢剪刀的关键杠杆，卡尔的“十二大以来最重要经济政策行动”判断指向这一后续而非大会决议条文本身。
- **民族问题特别分组会议与本土化决议（1923-04-25前后）**：斯大林提交民族政策论纲，在解密速记中遭拉柯夫斯基、伏龙芝及中亚、鞑靼、克里米亚代表围攻，被迫接受大幅提高民族院立法否决权、语言法定保障、边疆工业化承诺及反大俄罗斯沙文主义主调等修正案，奠定 **本土化（korenizatsiia）** 体制（`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`）。闭幕后不久苏丹-加利耶夫案标示：民族宽容以不破坏党的组织垄断为红线。
- **组织与派别余波**：大会在列宁缺席条件下巩固“三驾马车”对书记处的掌控，托洛茨基虽在剪刀差议题上亮相，1923年秋“46人声明”反对派危机仍待数月后爆发（十二大本身并非反对派被清洗的节点）。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | `absent-influence` | 1923-04 | 病重缺席但经笔记与信函左右民族问题讨论与干部信任布局 | `DEB-1922-lenin-testament-and-stalin-rise` |
| `PER-trotsky` | `reports-scissors-crisis` | 1923-04 | 以价格剪刀图主张工业计划化与流通改革，未获纲领性采纳 | `CLM-carr-1954-scissors-crisis-mechanics` |
| `PER-stalin` | `reports-nations-then-retreats` | 1923-04 | 民族论纲遭边疆代表围攻后全面让步，塑造本土化妥协 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` |
| `POL-korenizatsiia` | `institutionalized-at` | 1923-04起 | 民族问题决议将本土化写入苏联早期联邦运作框架 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` |
| `POL-nep` | `economic-context` | 1923 | 新经济政策流通危机在大会公开化，行政应对与信贷杠杆并行 | `CLM-carr-1954-scissors-crisis-mechanics` |

### 2.3 史学争鸣光谱
- **经验共识**：十二大是列宁缺席下的党代会；托洛茨基公开报告剪刀差；民族特别会议通过大幅修正斯大林原提纲的本土化决议；1923年秋信贷收缩缓解比价危机。
- **主要解释分歧**（详参 `DEB-1923-nationality-and-empire`）：
  - **[Jeremy D. Smith / 解密档案派]**（`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`）：驳斥“十二大=斯大林彻底胜利”旧说，强调少数民族代表迫使中央退让的历史性妥协。
  - **[E. H. Carr / 过渡时期经济史]**（`CLM-carr-1954-scissors-crisis-mechanics`）：剪刀差机制解释流通—生产失衡；真正合拢杠杆是大会后的信贷收缩而非大会决议的清晰路线图。
  - **[Richard Pipes 等传统叙事]**（经 Smith 引述对勘）：曾将十二大读作行政中央集权对自治一边倒的胜利——与1990年代后档案研究显著冲突。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `POL-korenizatsiia`
- **时效关系边** (`MTG-1923-04-12th-party-congress` → `POL-korenizatsiia` | `institutionalized` | 有效时段: `1923.04`): 十二大民族问题特别会议经拉柯夫斯基、伏龙芝与少数民族代表施压，确立本土化路线与民族院立法保障。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1923年俄共（布）十二大确立的苏维埃早期民族政策：在党垄断政权前提下推动边疆非俄罗斯地区干部、语言、教育与文化的“本土化”，提升加盟共和国宪法地位；1920年代与工业化、乌克兰化交织，至1928年前后张力外溢。

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
