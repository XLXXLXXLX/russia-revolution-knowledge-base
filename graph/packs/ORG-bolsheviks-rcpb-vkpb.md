# 1-Hop 去重平衡上下文包：`ORG-bolsheviks-rcpb-vkpb`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`ORG-bolsheviks-rcpb-vkpb`** (布尔什维克派—俄共（布）—联共（布） | `cards/organizations/ORG-bolsheviks-rcpb-vkpb.md` | `multi-perspective`): 已覆盖=`social-history-rabinowitch, opposition-history-daniels, institutional-history-khlevniuk, political-economy-carr, totalitarian-political-history-pipes`；待补=`rigby-membership-statistical-audit, soviet-official-party-history, provincial-non-capital-party-organizations`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
布尔什维克起于1903年社民工党二大后的党内多数派，经流亡、地下活动与1917年群众扩张成为执政党；1918年称俄共（布），1925年称联共（布）。它从地方主动性较强的革命党，演变为拥有任命网络与纪律制裁的党国核心，过程分阶段且存争议。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **派别分立（1903–1916）**：二大第一条表决中列宁草案被否决、马尔托夫案通过（`WEB-1903-08-02-rsdlp-rules-p1`，俄历08-02 / 公历08-15）；其后中央机构选举中的多数使“布尔什维克”之名出现（`MTG-1903-rsdlp-2nd-congress`）。多数与少数并非此后永久不变的社会集团。
- **布拉格会议（1912）**：列宁派召集并选出中央委员会、排斥取消派（`MTG-1912-01-prague-conference`），但其对全党的代表性遭对手争议，自称不等于共识。
- **群众党与内部争论（1917）**：党员数的通行说法为二月前后约2.4万、十月前后约35万，但该数字未入库一手出处，只作量级（见下表）。Rabinowitch 对彼得格勒的研究强调地方委员会、军事组织及新党员相对开放的参与，党内对临时政府、起义时机与社会主义联合政府均有分歧（`CLM-rabinowitch-1976-open-democratic-mass-party`；`CLM-rabinowitch-1976-october-three-factions-debate`；`MTG-1917-04-7th-april-party-conference`；`MTG-1917-07-rsdlp-6th-congress`）。地方证据不宜推广为全国均一状况。
- **党员数口径并列**：

| 时点 | 范围 | 数字 | 口径 / 来源 |
| :--- | :--- | :--- | :--- |
| 二月前后 → 十月前后 | 全国 | 约2.4万 → 约35万 | 通行近似，库内无一手出处，待 Rigby 核对 |
| 1917-04 七次代表会议 | 全国 | 代表约8万党员 | 代表所代表党员数（`MTG-1917-04-7th-april-party-conference`） |
| 1917-07 六大 | 全国 / 彼得格勒 | 代表约20–24万党员；彼得格勒约3.2万 | 代表所代表数；彼得格勒数引 Rabinowitch 1976（`MTG-1917-07-rsdlp-6th-congress`） |
| 1917 → 1918 | 彼得格勒 | 约4.3万 → 约1.35万 | Smith 1983（`CLM-smith-sa-1983-from-workers-control-to-nationalization`） |
| 1917 → 1918 | 彼得格勒 | 约5万 → 约6千 | Rabinowitch 2007 转引 Strumilin 统计（`RN-W2-first-year-soviet-rule`，pp. 390–401；参 `PER-strumilin`） |

  最后两行时段与统计口径是否同一，库内尚未调和，只能并列，不得相减或合并成单一“萎缩比例”。
- **执政、布列斯特与内战（1918–1920）**：1918年围绕布列斯特和约形成最大的党内分裂，左派共产主义者主张革命战争（`ORG-left-communists-1918`；`EVT-1918-03-brest-litovsk-treaty`；`CLM-daniels-1960-left-communists-1918`）。1918年3月七大更名俄国共产党（布尔什维克）。内战、经济崩溃与军政动员促使集中指挥与干部委派扩张；老工人党员进入军队与行政机关，基层社会基础也受饥荒与迁移冲击。Rabinowitch 认为危机及应对而非预定蓝图对转变至关重要（`RN-W2-first-year-soviet-rule`）；Carr 则把党、苏维埃与国家三者关系的重组视为制度主线（`RN-W35-carr-lenin-party-instrument-and-soviet-constitution-1917-1923`；`RN-W23-carr-party-state-constitution-and-economic-order-1917-1923`；`INS-sovnarkom-and-vtsik`）。列宁1918年5月对“左派幼稚病”的批评见 `sources/web-archive/W32_milestone_docs/1918-05_lenin-left-wing-childishness-state-capitalism.md`。意识形态、强制选择与地方差异仍须单独考察。
- **统一规则与党员再造（1921–1925）**：1921-03-16十大通过《关于党的统一》（`WEB-1921-03-16-on-party-unity`，含秘密第7条），全国表决为336:50:18（见 `ORG-workers-opposition` 所引 `CLM-daniels-1960-tenth-congress-turning-point`）；`POL-ban-on-factions-1921` 要求解散派别，清党与党员审查并行。规则未立即消灭党内争论，却为以后的制裁提供重要工具。1924年列宁逝世后的“列宁号召”吸收数十万新党员，工人比例名义上提高，新老党员经验差距也扩大；新党员并非整齐一致的选票集团。1925年十四大更名全联盟共产党（布尔什维克）。
- **权力集中与1929观察截点**：书记处的任命、纪律与代表产生机制同政策联盟共同塑造权力；1927年左翼反对派遭排斥（`ORG-left-and-united-opposition`；`PER-stalin`），1928–1929年布哈林、李可夫、托姆斯基的反对逐步失败。赫列夫纽克强调任命权、联盟与对手失误共同侵蚀集体领导（`RN-W3-politburo-apparatus-and-1929-victory`）。不能说1929年一切制度已定型，也不能把后来结局倒推为必然。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 关系实质 | 依据 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | `faction-leader` | 1903–1924 | 派别与执政党的核心领袖，党章草案、1912年布拉格会议与执政纪律均与其相关 | `WEB-1903-08-02-rsdlp-rules-p1`；`MTG-1912-01-prague-conference` |
| `ORG-mensheviks` | `factional-rival` | 1903–1920年代 | 同源社民党派反复分合，1917年后围绕政府与苏维埃权力对立 | `DEB-1903-bolshevik-menshevik-split` |
| `MTG-1903-rsdlp-2nd-congress` | `founding-split-event` | 1903 | 党章第一条与中央机构选举形成多数—少数标签 | `WEB-1903-08-02-rsdlp-rules-p1`；L3 `1903-07_rsdlp_second_congress_split` |
| `MTG-1917-04-7th-april-party-conference` | `party-conference` | 1917-04 | 代表约8万党员的口径，路线转向后的党内讨论 | `MTG-1917-04-7th-april-party-conference` 卡内口径 |
| `MTG-1917-07-rsdlp-6th-congress` | `party-congress` | 1917-07 | 代表约20–24万党员的口径 | `MTG-1917-07-rsdlp-6th-congress` 卡内口径 |
| `ORG-vikzhel` | `coalition-negotiation` | 1917-10至11 | 铁路工会斡旋联合政府，暴露党内中央委员会多数与少数分歧 | L3 `1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis`；`DEB-1917-all-socialist-coalition-vikzhel-missed-chance` |
| `ORG-left-communists-1918` | `internal-opposition` | 1918.01–05 | 布列斯特和约引发的党内分裂，主张革命战争 | `CLM-daniels-1960-left-communists-1918` |
| `EVT-1918-03-brest-litovsk-treaty` | `party-split-trigger` | 1918.01–03 | 和约表决暴露执政后党内路线分歧 | `CLM-daniels-1960-left-communists-1918` |
| `INS-sovnarkom-and-vtsik` | `party-state-nexus` | 1917–1929 | 党组织与政府、中执委的权限交叠和领导关系变化 | `RN-W35-carr-lenin-party-instrument-and-soviet-constitution-1917-1923` |
| `ORG-democratic-centralists` | `internal-opposition` | 1919–1927 | 集团反对党政任命和官僚化，后遭纪律制裁 | `PER-sapronov`；`PER-osinsky` |
| `ORG-workers-opposition` | `internal-opposition` | 1920–1922 | 工会管理经济方案遭十大否决，派别被要求解散 | `CLM-daniels-1960-tenth-congress-turning-point` |
| `MTG-1921-rcpb-10th-congress` | `party-congress` | 1921-03 | 通过《关于党的统一》，限制有组织派别 | `WEB-1921-03-16-on-party-unity` |
| `POL-ban-on-factions-1921` | `adopted-disciplinary-rule` | 1921起 | 十大统一决议限制有组织派别，后续运用与原初背景应区分 | `WEB-1921-03-16-on-party-unity`；`RN-W1C-communist-oppositions-1918-1929` |
| `ORG-left-and-united-opposition` | `internal-opposition` | 1923–1927 | 1927年遭十五大排斥 | `WEB-1927-09-platform-joint-opposition` |
| `PER-stalin` | `secretariat-leader` | 1922–1929 | 书记处的任命与纪律网络对权力集中起作用 | `CLM-khlevniuk-2015-secretariat-and-nomenklatura` |

### 2.3 史学争鸣光谱
经验上，1917年组织扩张、1918年执政与内战动员、1921年统一决议及1924年招募均可分期辨认。Rabinowitch 从彼得格勒基层材料强调1917年相对开放和1918年危机的偶然性；Daniels 从党内反对派追踪革命原则与执政纪律的冲突；Carr 的制度政治经济路径把党视为联结苏维埃与国家机关的工具；赫列夫纽克看重1920年代机关任命及高层联盟变化。另一端的 Pipes 将布尔什维克的权力垄断追溯到列宁主义的内在逻辑（`CLM-pipes-1990-october-classic-coup`；`CLM-pipes-1990-red-terror-leninist-logic`），而修正派强调偶然与环境约束。各家尺度不同，不能只用“必然独裁”或“纯粹环境所迫”取代比较；苏联官方党史口径与 Rigby 统计库内尚缺。

## 2. 一跳邻域全量微摘要目录 (去重后共 22 个节点，0 截断)
- **`EVT-1905-12-moscow-armed-uprising`**（1905年12月莫斯科武装起义与普列斯尼亚街垒战）: 1905-12-07至12-18[O.S.]/12-20至12-31[N.S.]，莫斯科总罢工转为巷战。铁路未断使谢苗诺夫近卫团得以增援，重炮镇压普列斯尼亚，全城估死千人。败局引发普列汉诺夫反对起兵、列宁要求坚决进攻、托洛茨基强调争夺军队的战略分歧。 ‖ `→ORG-bolsheviks-rcpb-vkpb`[leads_jointly|1905-12-06 [O.S.] / 1905-12-19 [N.S.] 至 1905-12-18 [O.S.] / ]: 基层打破教派藩篱协同作战（约700–800名党战斗队员加铁路、印刷工志愿射手），以三四人游击战术及普列斯尼亚街垒牵制1.5万卫戍军（ch11_1905_part_11 [·255·, ·261·]）。
- **`EVT-1907-1914-june-third-regime-and-lena-to-july-strikes`**（1907–1914年六三体制、斯托雷平反动与勒拿至七月工潮）: 1907年6月3日[O.S.]六三政变至1914年7月一战爆发间的战前危机年代。前五年呈现土地缙绅杜马优势、斯托雷平土改与地下党受挫蛰伏；1912年4月勒拿金矿惨案引爆《真理报》创刊、工会与保险会转向及1914年7月圣彼得堡街垒工潮，引发战前稳定与否之争。 ‖ `→ORG-bolsheviks-rcpb-vkpb`[captured_unions_and_insurance|1912–1914]: 借《真理报》、1912保险法委员会选举与金属/手工业工会整批名单竞选在圣彼得堡取代孟什维克优势
- **`EVT-1917-07-july-days`**（1917年七月事变）: 1917年7月3—5日（俄历；公历7月16—18日），机枪团、水兵与工人要求苏维埃接权。布尔什维克中央、军事组织与地方党委在劝阻和介入间分裂；德国经费指控与调兵镇压扭转局势。基层激进化、党内决策和资助指控须分别求证。 ‖ `→ORG-bolsheviks-rcpb-vkpb`[divided_response|1917-07-03..05 [O.S.] / 07-16..18 [N.S.]]: 中央、军事组织、地方党委不同节奏使劝阻转为介入。
- **`EVT-1918-1921-transcaucasian-republics-baku-commune-and-sovietization`**（外高加索独立共和国、巴库公社与苏维埃化（1918—1921））: 1918—1921年外高加索独立建国与苏维埃化进程。布列斯特割地与俄土前线瓦解后，巴库公社兴亡，外高加索联邦解体为格、阿、亚三国并陷领土冲突。红军击败邓尼金后，高加索局配合红十一军团与苏土外交契机于1920—1921年苏维埃化三国，铁路整合与集权体制随即牵动1922年建盟与格鲁吉亚危机。 ‖ `→ORG-bolsheviks-rcpb-vkpb`[caucasus-bureau-and-eleventh-army|1920.02–1921.05]: 先于阿、格、亚设立名义独立共产党，再以第11红军配合当地地下力量与少数民族反抗完成全区军事整合
- **`MTG-1917-04-7th-april-party-conference`**（俄国社会民主工党（布尔什维克）第七次全国代表会议（四月会议））: 1917-04-24至04-29[O.S.]/05-07至05-12[N.S.]，布尔什维克四月会议以71:39:8通过列宁当前形势决议，拒绝信任临时政府，支持土地国有化与苏维埃夺权；但民族自决、中央规模及齐美尔瓦尔德会议问题上列宁遭多数反对，党内分歧鲜明。 ‖ `→ORG-bolsheviks-rcpb-vkpb`[elects_leadership|1917年春]: 在公开的内部路线分歧中，以 109 人无记名投票选举九人中央委员会。 ； `←ORG-bolsheviks-rcpb-vkpb`[party-conference|1917-04]: 代表约8万党员的口径，路线转向后的党内讨论
- **`MTG-1917-06-1st-congress-of-soviets`**（全俄工兵代表苏维埃第一次代表大会）: 1917年6月3—24日[O.S.]/6月16日—7月7日[N.S.]，全俄工兵苏维埃一大在彼得格勒召开。护国派543∶126通过信任联合政府并设257席中执委；但列宁6月4日应战“有！”、6月10日流产示威与6月18日40万大游行反噬，彻底撕裂温和派街头合法性。 ‖ `→ORG-bolsheviks-rcpb-vkpb`[internal_three_tier_tension|1917-06-06..23 [O.S.] / 06-19..07-06 [N.S.]]: 仅105席但借6月18日游行夺取街头话语；CC、PK与MO在6月10日取消与拉齐斯条款间反复分歧。
- **`MTG-1917-07-rsdlp-6th-congress`**（俄国社会民主工党（布尔什维克）第六次代表大会）: 1917-07-26至08-03[O.S.]/08-08至08-16[N.S.]，布尔什维克六大在彼得格勒半地下召开，列宁、托洛茨基缺席，斯维尔德洛夫主持。大会批准区联派并入，暂撤“一切政权归苏维埃”口号；普列奥布拉任斯基与斯大林就俄国率先开辟社会主义道路交锋。 ‖ `→ORG-bolsheviks-rcpb-vkpb`[merges_into|1917-07-26 至 08-03 [O.S.] / 1917-08-08 至 08-16 [N.S.]]: 约4,000名区联派成员正式并入布尔什维克党，托洛茨基、乌里茨基、越飞当选中央委员，完成十月起义核心领导层拼图（Carr 1950, ch04 p. 91）。 ； `←ORG-bolsheviks-rcpb-vkpb`[party-congress|1917-07]: 代表约20–24万党员的口径
- **`MTG-1918-03-7th-party-congress`**（俄国共产党（布尔什维克）第七次紧急代表大会）: 1918年3月6—8日（纯公历），俄共（布）七大在法定人数不足下强行召开。列宁“喘息和约”与布哈林“左派共产主义者”革命战争路线激辩12小时后，大会以30∶12∶4（初计28∶9∶1）批准《布列斯特和约》，改党名为俄共（布）并设党纲起草委员会。 ‖ `→ORG-bolsheviks-rcpb-vkpb`[rebranded_party_identity|1918-03-08 起]: 正式由“社会民主工党（布）”更名为“俄国共产党（布尔什维克）”，宣示与第二国际彻底决裂。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[faction-leader|1903–1924]: 派别与执政党的核心领袖，党章草案、1912年布拉格会议与执政纪律均与其相关
- **`ORG-mensheviks`**（孟什维克）: 俄国社会民主主义政党（1903–1924），源于1903年二大马尔托夫等与列宁围绕党章第一条及集中制的决裂，主张开放型群众政党与工人自主活动。1917年分化为策烈铁里、但恩主导的入阁“革命护国派”与马尔托夫领导的反战“国际主义派”；十月后开展苏维埃合法反对派抗争，1921年后遭取缔。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[factional-rival|1903–1920年代]: 同源社民党派反复分合，1917年后围绕政府与苏维埃权力对立
- **`MTG-1903-rsdlp-2nd-congress`**（俄国社会民主工党第二次代表大会（1903年7–8月））: `1903-07-30` 至 `08-23 [N.S.]` 俄社民工党二大先后在布鲁塞尔与伦敦召开。大会通过党纲；第23次会议马尔托夫党章第一条 `28:22:1` 胜列宁案。随后的崩得与经济派退场逆转了多数，列宁借微弱多数改组《火星报》三人编委，由此衍生布尔什维克与孟什维克之名。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[founding-split-event|1903]: 党章第一条与中央机构选举形成多数—少数标签
- **`ORG-vikzhel`**（全俄铁路雇员与工人联合会执行委员会（维克热尔））: 维克热尔是1917年夏产生的全国铁路工会执行机关。铁路连接军队、粮食与城市，十月革命后其运输杠杆使它试图调停各社会主义政党、推动广泛联合政府。布尔什维克内部为此严重分裂，谈判未能实现最广泛联合，新的铁路工会领导机关后与布党及左翼社革党合作。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[coalition-negotiation|1917-10至11]: 铁路工会斡旋联合政府，暴露党内中央委员会多数与少数分歧 ； `→ORG-bolsheviks-rcpb-vkpb`[mediated-coalition-talks|1917.10–11]: 借铁路运输杠杆要求联合政府，并暴露布党内部严重分歧
- **`ORG-left-communists-1918`**（1918年左翼共产主义者）: 1918年初俄共（布）内以布哈林、奥新斯基、拉狄克、普列奥布拉任斯基为首的极左集团，借《共产党人》（`Коммунист`）杂志反对《布列斯特和约》与列宁“国家资本主义”一长制；俄共七大批准和约后作为有组织派别逐步消解，但其国际主义与反官僚化诉求深刻塑造此后党内反对派谱系。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[internal-opposition|1918.01–05]: 布列斯特和约引发的党内分裂，主张革命战争
- **`EVT-1918-03-brest-litovsk-treaty`**（1918年布列斯特-里托夫斯克和约危机与签约）: 1917年12月停战至1918年3月签约，列宁主和、托洛茨基“不战不和”与布哈林革命战争路线交锋。德军进逼后，中央2月23日以7赞成、4反对、4弃权接受最后通牒；和约保存政权，也加深党内裂痕并促使左翼社革党退阁。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[party-split-trigger|1918.01–03]: 和约表决暴露执政后党内路线分歧
- **`INS-sovnarkom-and-vtsik`**（人民委员会与全俄、全苏中央执行委员会）: 苏维埃代表大会闭会期间，中执委在宪制上监督政府，人民委员会却迅速掌握施政与大量法令制定。苏俄与1922年成立的苏联各有中执委与人民委员会，不能混同。党内领导与国家机关关系不断变化，政治局权重日增，但1920年代仍须经政府落实决策。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[party-state-nexus|1917–1929]: 党组织与政府、中执委的权限交叠和领导关系变化
- **`ORG-democratic-centralists`**（民主集中派）: 民主集中派是1919年初结成的布尔什维克党内反对派，萨普罗诺夫、奥新斯基、弗·斯米尔诺夫等为重要代表，批评以任命和行政命令取代集体领导与基层参与。成员及立场随时间变化：1923年部分人联署《四十六人声明》；后期“十五人集团”须与早期派别区分。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[internal-opposition|1919–1927]: 集团反对党政任命和官僚化，后遭纪律制裁 ； `→ORG-bolsheviks-rcpb-vkpb`[internal-opposition-to-apparatus|1919–1927]: 争取党和苏维埃机关的集体领导，后与中央公开决裂
- **`ORG-workers-opposition`**（工人反对派）: 俄共（布）党内以产业工人和工会干部为主体的左翼反对派（1920–1922），由什利亚普尼科夫、梅德韦杰夫及理论代言人柯伦泰领导。在1920–1921年工会争论中痛斥党政官僚化与专家“一长制”，主张由“全俄生产者代表大会”及工会自治管理国民经济；1921年十大被定性为无政府工团主义倾向并遭解散。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[internal-opposition|1920–1922]: 工会管理经济方案遭十大否决，派别被要求解散
- **`MTG-1921-rcpb-10th-congress`**（俄国共产党（布尔什维克）第十次代表大会）: 1921年3月8日至16日，俄共（布）十大在经济崩溃与喀琅施塔得起义交织下召开。大会决定以粮食税取代余粮收集制，开启新经济政策转向；同时终结工会大辩论，通过《关于党的统一》禁止派别活动并谴责工人反对派。经济退却与党内纪律收紧并行，会后中央与书记处改组重塑了组织权力格局。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[party-congress|1921-03]: 通过《关于党的统一》，限制有组织派别
- **`POL-ban-on-factions-1921`**（《关于党的统一》派别禁令）: 俄共十大于1921年3月16日通过《关于党的统一》，要求解散按纲领组成的派别，并保留规定渠道的批评。秘密第七条设中央领导成员的特殊处分程序；1924年1月公开宣读、1926年7月首次动用开除季诺维也夫出政治局，危机措置遂渐成约束反对派的工具，但不同年份执行不等同原条文。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[adopted-disciplinary-rule|1921起]: 十大统一决议限制有组织派别，后续运用与原初背景应区分
- **`ORG-left-and-united-opposition`**（1923–1927年左翼反对派与托季联合反对派）: 1923年剪刀差危机触发的托洛茨基—普列奥布拉任斯基“左翼反对派”，经1926年春与季诺维也夫—加米涅夫“新反对派”结盟为托季联合反对派；以《四十六人声明》与《1927年政纲》批判官僚体制与“一国社会主义”、主张价格—财政渠道的计划工业化，于1927年12月十五大被组织摧毁。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[internal-opposition|1923–1927]: 1927年遭十五大排斥
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←ORG-bolsheviks-rcpb-vkpb`[secretariat-leader|1922–1929]: 书记处的任命与纪律网络对权力集中起作用
- **`PER-bogdanov`**（亚历山大·波格丹诺夫）: 俄国马克思主义思想家、医生、经验一元论与组织学创立者（1873—1928）。1904—1907年任布尔什维克国内核心二号领袖；1908—1909年因召回主义与哲学论战遭列宁开除后另组前进派并办卡普里、博洛尼亚党校；1917—1920年领导无产阶级文化协会遭收编，1928年死于输血实验。 ‖ `→ORG-bolsheviks-rcpb-vkpb`[early-core-leader -> expelled-dissident|1904–1909.06]: 1904–1907实质掌控国内组织与财政网络，1909年6月12日被《无产者报》扩大编委会清除出布尔什维克派系，十月后始终保持党外独立批判立场

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 5 项)
- **`DEB-1903-bolshevik-menshevik-split`**（《怎么办？》与1903年布尔什维克—孟什维克分裂实质之争 | `historiography/debates/DEB-1903-bolshevik-menshevik-split.md` | 流派 `participant, cold-war-jacobin-continuity, intellectual-history, erfurt-reinterpretation, menshevik, borderland-social-democracy, labor-history`）：《怎么办？》的自发性与意识理论究竟体现精英代替工人，还是欧洲社会民主主义所共有的结合公式？1903年党章、领导机构选举和代表退会如何共同造成分裂，又能否把后来的一党统治直接追溯到当时？必须区分文本论战、组织选择和事后政治后果。
- **`DEB-1917-october-coup-or-social-revolution`**（十月革命：少数派政变还是社会革命？ | `historiography/debates/DEB-1917-october-coup-or-social-revolution.md` | 流派 `liberal-coup, party-social-history, russian-revisionist-timing, labor-local-history, moderate-socialist-and-constitutional-legitimacy, participant-marxist, peasant-social-history, borderland-and-memory-historiography`）：十月武装夺权是少数派政变，还是工人、士兵与农民社会革命的政治表达？有组织的起义与广泛的基层动员能否同时成立，苏维埃多数又能否代表全国选民？这些问题涉及不同地区、不同时间的支持与合法性，不能以一次投票或一次攻占行动互相替代。
- **`DEB-1918-war-communism-ideology-or-emergency`**（战时共产主义与早期一党制本质之争：内战应急、乌托邦跃进还是国家统制连续？ | `historiography/debates/DEB-1918-war-communism-ideology-or-emergency.md` | 流派 `emergency-carr-mawdsley, utopian-tragedy-malia-pipes, state-continuity-lih-smith, mixed-causation-rabinowitch-lewin`）：1918至1921年的全面国有化、余粮收集制、取缔私商、劳动军事化，以及多党苏维埃收为一党专政，究竟是内战与供给崩溃逼出的生存应急，还是反市场乌托邦的激进兑现，抑或一战以来国家统制与基层危机交互的结果？“战时共产主义”是1921年转向时的事后标签，须分清措施序列与事后总结。
- **`DEB-1928-bukharin-alternative`**（布哈林替代方案与新经济政策终结之争 | `historiography/debates/DEB-1928-bukharin-alternative.md` | 流派 `nep-alternative, economic-growth, structural-dilemma, apparatus, ideology-and-mobilization, cliometrics-and-archival-reassessment`）：1927至1929年粮食危机与新经济政策的瓦解，是否意味着渐进工业化和工农联盟已无可行出路，还是党内权力与政策选择扼杀了布哈林的替代方案？投资、价格、农民供粮和政治动员之间的约束究竟有多强，必须把经济可行性、政治可行性与实际权力斗争分别检验。
- **`DEB-1917-all-socialist-coalition-vikzhel-missed-chance`**（维克热尔谈判与清一色社会主义联合政府之争 | `historiography/debates/DEB-1917-all-socialist-coalition-vikzhel-missed-chance.md` | 流派 `contingency-rabinowitch, ideological-pipes-malia, structural-revolutionary-left, provincial-socialists`）：十月起义后铁路工会维克热尔推动的社会主义政党联合政府，是多党苏维埃政治一度存在而后丧失的选择，还是各方对夺权合法性、政府构成和战争的分歧使之难以实现？谈判破裂的责任和一个可持续联盟的可行性是两个不同问题。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/69 条)
- **`CLM-rabinowitch-1976-open-democratic-mass-party`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-rabinowitch-1976-october-three-factions-debate`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-smith-sa-1983-from-workers-control-to-nationalization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 155–156, 166–169, 177–179, 184–186, 192（即源文件标注 PDF pp. 160–161, 171–174, 182–184, 189–191, 197）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-daniels-1960-left-communists-1918`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 70-81]: Daniels：1918年左翼捍卫革命纲领，却在分裂关头受党统一约束
- **`CLM-daniels-1960-tenth-congress-turning-point`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 146-153]: Daniels：1921年十大将党统一转化为压缩合法反对空间的组织制度
- **`CLM-khlevniuk-2015-secretariat-and-nomenklatura`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（In Lenin's Shadow，GENERAL SECRETARY 至 1923 年 9 月组织局安排）；制度总论见 ops/xhtml/ch01a.html。工作区文本无纸质页码。]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-bonnell-1983-1912-1914-union-and-insurance-boards-bolshevik-capture`** [`SCH-bonnell-victoria`(维多利亚·E·邦内尔) | Book pp. 366–371, 390–438 [PDF pp. 389–394, 413–461]]: 
- **`CLM-rabinowitch-1968-divided-bolshevik-party-july`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | PDF pp. 12, 17, 79, 86-94, 121-123]: 
- **`CLM-service-lenin-v1-bogdanov-vpered-rupture-and-prague-1912`** [`SCH-service-robert`(罗伯特·瑟维斯) | pp. 188-206 (重要边界提示：馆藏第一卷时间止于1910年1月中央全会；1910–1912年《前进》派后期演化及1912年1月布拉格代表会议属《列宁政治生涯》第二卷，本卷未覆盖)]: 
- **`CLM-jacobin-ancestry-tkachev-blanqui-and-leninism`** [`SCH-chamberlin-william-henry`(威廉·亨利·钱伯林) | pp. 251–257 (PDF pp. 2–8)]: 
- **`CLM-pipes-1990-patrimonial-state-and-intelligentsia`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 2 (Official Russia); ch. 4 (The Intelligentsia); cf. Introduction]: 
- **`CLM-haimson-1955-lenin-what-is-to-be-done`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. 132-141]: 
- **`CLM-haimson-1955-consciousness-spontaneity`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. vi-viii, 7-11]: 
- **`CLM-haimson-1955-1903-second-congress-split`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. 175-191]: 
- **`CLM-haimson-1987-menshevik-party-ethos-and-family`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. 14–17]: 
- **`CLM-lih-2006-erfurtian-merger-formula`** [`SCH-lih-lars`(拉斯·T·利) | pp. 6-9, 41-49, 74-106, 113-121, 556-557]: 
- **`CLM-lih-2006-kautsky-and-spontaneity`** [`SCH-lih-lars`(拉斯·T·利) | pp. 35-37, 555, 613-667]: 
- **`CLM-lih-2006-textbook-myth-critique`** [`SCH-lih-lars`(拉斯·T·利) | pp. 5, 13-33, 555]: 
- **`CLM-getzler-1967-martov-1903-clause-one`** [`SCH-getzler-israel`(伊斯雷尔·格茨勒) | pp. 78-79]: 
- **`CLM-blanc-2021-revolutionary-kautskyanism-in-empire`** [`SCH-blanc-eric`(埃里克·布兰克) | pp. 25–28, 569–578]: 
- **`CLM-blanc-2021-beyond-russocentric-bolshevism`** [`SCH-blanc-eric`(埃里克·布兰克) | pp. 15–16, 23–26]: 
- **`CLM-zelnik-1999-worker-intelligentsia-tutelage-tension`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | pp. 6-7, 13-15, 18-27, 51-52]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 36 条 L3 逐日细节见 `timeline/L3_daily/`)
