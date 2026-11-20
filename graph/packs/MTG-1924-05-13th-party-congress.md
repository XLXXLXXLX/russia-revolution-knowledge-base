# 1-Hop 去重平衡上下文包：`MTG-1924-05-13th-party-congress`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`MTG-1924-05-13th-party-congress`** (俄国共产党（布尔什维克）第十三次代表大会 | `cards/meetings/MTG-1924-05-13th-party-congress.md` | `multi-perspective`): 已覆盖=`collective-leadership-archival, opposition-history, economic-carr, lenin-testament-lewin, daniels-bureaucratic-freeze`；待补=`regional-delegate-voting-behavior, closed-delegation-minutes`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 150字定性微摘要
1924年5月23日至31日，列宁逝世后的首次党代会召开。会前中央全会与长老会议限制列宁最后口授文件传达方式并留任斯大林；大会依托“列宁征召”与组织筛选压倒左翼反对派，托洛茨基公开宣示对党忠诚。会后中央与中监委扩编、布哈林升入政治局，集体领导联盟暂时稳固。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **列宁最后 13 份口授文件移交与程序封锁（`05-18` 至 `05-22`）**：**`1924-05-18`**，克鲁普斯卡娅向中央遗嘱委员会正式移交列宁 1922 年 12 月至 1923 年 3 月口授的 **13 份文件整体**（包含 7 篇已发表文章与 6 封未公开密件：核心为[《给代表大会的信》](../../sources/web-archive/E06_E10_turning_points/1922-12_letter-to-the-congress.md)及 1923-01-04 建议把斯大林调离总书记的附言、以及[《关于民族或“自治化”问题》](../../sources/web-archive/W39_lenin_1922_1923_docs/1922-12-30_lenin-question-of-nationalities-or-autonomisation.md)，并与[《论合作制》](../../sources/web-archive/E02_E10_core_classics/1923-01-04_on-cooperation.md)、[《我们怎样改组工农检查院》](../../sources/web-archive/W39_lenin_1922_1923_docs/1923-01-23_lenin-how-we-should-reorganise-rabkrin.md)和[《宁肯少些，但要好些》](../../sources/web-archive/W39_lenin_1922_1923_docs/1923-03-02_lenin-better-fewer-but-better.md)共同构成反官僚与制衡总书记的整体改革蓝本）。**`05-21`** 中央全会讨论留任，季诺维也夫与加米涅夫以“列宁关于分裂的忧虑已被实践证明不再存在”为由提议留任斯大林，压倒托洛茨基孤立的公开印行主张；**`05-22`** 长老会议由加米涅夫主持宣读，决定不在大会全体会议公开宣读，改按各代表团分组由中央大员口头传达（含《关于民族或“自治化”问题》），**严禁作速记、严禁外传、不列入大会正式议程**。
- **“列宁征召”与代表票仓重塑（反对派 `0` 席）**：`1924-01-29`—`31` 中央全会启动“列宁征召”，至 5 月十三大前突击吸纳 **20 万—24 万**名在职工人入党（1924–1925 年累计 63.8 万人），使全党规模迅速增至 **735,881** 名党员与候补党员（[DATA-04](../../data/DATA-04-party-membership-and-congress-votes-1903-1929.md)；[逐日卷](../../timeline/L3_daily/1924-01_lenin_death_testament_and_lessons_of_october.md)）。更关键的是，**中央组织局破例准许尚无正式表决权的“列宁征召”新入党候补党员直接参加十三大代表基层初选投票**（[Daniels Ch. 10](../../sources/monographs/daniels_1960_conscience/ch10_pages_251-275.md)），从源头上彻底稀释了老党员与城市知识分子对反对派的支持。最终出席大会的 **1,164 名代表**（**748 名有表决权代表 + 416 名有发言权代表**）中，**左翼反对派获 `0` 个有表决权席位**，托洛茨基、普列奥布拉任斯基、拉狄克仅以有发言权代表身份列席。
- **大会讲坛交锋、克鲁普斯卡娅抗议与托洛茨基的纪律困境**：季诺维也夫代表中央作政治报告，持续批判[《四十六人声明》](../../sources/web-archive/E01_E10_supplements/1923-10-15_declaration-of-the-forty-six.md)与托洛茨基[《新方针》公开信](../../sources/web-archive/W32_milestone_docs/1923-12-08_trotsky-new-course-open-letter.md)，并强硬要求反对派公开认错悔过。**克鲁普斯卡娅**当场抗议（须区分证据口径：她在会前反对封锁遗嘱，而在大会公开讲坛的明确抗议据[逐日卷](../../timeline/L3_daily/1924-01_lenin_death_testament_and_lessons_of_october.md)系针对季诺维也夫逼迫少数派违心认错）。**`1924-05-26`**，托洛茨基全程未触及遗嘱，发表“归根到底，党永远是正确的……不论党是对是错，这是我的党”之演说，既表达对党忠诚也暴露反对派在一党铁律下的失语困境；大会全票追认一月十三次党代表会议将反对派定性为“小资产阶级倾向”的决议。
- **经济制约与会后中枢改组（`05-31` 至 `06-02`）**：剪刀差危机、币制改革与工农商品交换制约仍是大会底色，十三大不能单纯化约为人事密谋。大会表面按列宁遗愿将中央委员会扩编至 **53 名正式委员 + 34 名候补委员**、将中央监察委员会扩编至 **151 人**；**`1924-06-02`** 十三届一中全会确认斯大林连任总书记，**布哈林递补列宁遗缺升任政治局正式委员**（政治局 7 正式委员：季诺维也夫、加米涅夫、斯大林、托洛茨基、李可夫、托姆斯基、布哈林；候补委员：捷尔任斯基、伏龙芝、索科利尼科夫），卡冈诺维奇进入书记处与组织局。至 1924 年 8 月，除托洛茨基外 6 名政治局正式委员与中监委主席古比雪夫组成非正式“七人小组（Семёрка）”，在政治局正式会议前先期密商并实质架空托洛茨基。

### 2.2 核心关系网络（结构化边表）
| 目标节点 ID | 关系类型 (Relation) | 适用时期 | 一句话关系摘要 | 证据锚点 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | posthumous-program | 1924-05 | 遗嘱及最后13份口授文件提出撤换总书记、反沙文主义与改组中监委—工农检查院蓝本。 | CLM-lewin-1968-testament-intent; CLM-lewin-1968-georgian-affair-bureaucracy |
| `PER-krupskaya` | transmitted-and-protested | 1924-05 | 5月18日移交列宁最后13份文件整体，并在大会讲坛抗议逼迫反对派公开认错。 | RN-W1-testament-and-cooperation |
| `PER-stalin` | retained-general-secretary | 1924-05起 | 在季诺维也夫与加米涅夫力保下留任，6月2日十三届一中全会正式确认连任总书记。 | CLM-khlevniuk-2015-collective-leadership-erosion; CLM-khlevniuk-2015-secretariat-and-nomenklatura |
| `PER-zinoviev` | triumvirate-leader | 1924-05 | 主持大会政治报告，力保斯大林留任并要求左翼反对派公开认错。 | CLM-khlevniuk-2015-collective-leadership-erosion |
| `PER-kamenev` | triumvirate-ally | 1924-05 | 主持5月22日长老会议宣读遗嘱并背书留任斯大林，主导分组口头传达程序。 | CLM-khlevniuk-2015-collective-leadership-erosion |
| `PER-trotsky` | opposition-isolated | 1924-05 | 748表决权代表中反对派0席，5月26日发表“不论党是对是错，这是我的党”发言。 | CLM-deutscher-1959-disarmed-prophet-paradox; DATA-04-party-membership-and-congress-votes-1903-1929 |
| `PER-bukharin` | promoted-politburo | 1924-06-02起 | 十三届一中全会递补列宁遗缺升任政治局正式委员，加入后来的“七人小组”。 | CLM-khlevniuk-2015-collective-leadership-erosion |
| `INS-politburo-orgburo-secretariat` | expanded-and-locked | 1924-05至08 | 中央扩至53正式+34候补、中监委151人，组织局以破例初选投票权锁死代表结构并衍生“七人小组”。 | CLM-khlevniuk-2015-secretariat-and-nomenklatura; CLM-khlevniuk-2015-collective-leadership-erosion |
| `ORG-left-and-united-opposition` | excluded-from-voting-seats | 1924-05 | 在十三大748名有表决权代表中获0席，被全票追认定性为“小资产阶级倾向”。 | DATA-04-party-membership-and-congress-votes-1903-1929; Daniels ch10 |
| `POL-nep` | economic-context | 1924 | 剪刀差危机、币制改革与工农商品流通问题制约大会政策议程。 | RN-W23-carr-party-state-constitution-and-economic-order-1917-1923 |

### 2.3 史学争鸣光谱
- **经验共识**：5月18日移交13份口授文件、5月21–22日压制公开宣读并留任斯大林、748名表决权代表中反对派0席与6月2日布哈林升入政治局均为可核事实；但“若当时公开宣读遗嘱是否足以改变苏联历史走向”属反事实解释，学界并无共识。
- **Moshe Lewin（列宁最后斗争整体论）**：将《给代表大会的信》与《关于民族或“自治化”问题》《我们怎样改组工农检查院》《宁肯少些，但要好些》视为一体化的反官僚“三诫”，指出十三大只采纳了扩充中央与中监委的外壳形式，却抽空了列宁制衡总书记权力的政治灵魂。
- **Oleg Khlevniuk（后苏联档案与集体领导博弈视角）**：强调政治局同事清楚斯大林权力的风险，却因畏惧托洛茨基威望与维持反托联盟而主动留任斯大林；随后 1924 年 8 月形成的“七人小组（Семёрка）”表明，正是集体领导自身的密室排斥机制为斯大林借书记处与干部任免网（nomenklatura）坐大创造了温床。
- **Robert V. Daniels 与 Isaac Deutscher（反对派与纪律悖论视角）**：Daniels 揭示自 1923 年秋官僚冻结起，书记处委派网叠加组织局破例赋予“列宁征召”候补党员初选投票权，已在程序上消灭了党代会代表的多元可能；Deutscher 聚焦托洛茨基 5 月 26 日的“解除武装的先知”困境——认同布尔什维克一党垄断的托洛茨基无法在党外诉诸社会力量，最终只能向党纪屈服。
- **E. H. Carr（结构与经济视角）**：提醒剪刀差危机、财政稳健（切尔文涅茨币制改革）与农业复苏压力同样决定了代表团对稳定领导层的迫切需求，十三大不宜完全化约为纯粹的人事权谋史。

## 2. 一跳邻域全量微摘要目录 (去重后共 10 个节点，0 截断)
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←MTG-1924-05-13th-party-congress`[posthumous-program|1924-05]: 遗嘱及最后13份口授文件提出撤换总书记、反沙文主义与改组中监委—工农检查院蓝本。
- **`PER-krupskaya`**（娜杰日达·克鲁普斯卡娅）: 娜杰日达·克鲁普斯卡娅（1869–1939），布尔什维克元老、列宁夫人兼秘密通信枢纽；1918年后主持教育人民委员部成人政教与扫盲，1922–1923年守护列宁病榻口授并于1924年5月移交十三份文件。1925–1926年短暂参与反对派后脱离，晚年转入教育制度工作。 ‖ `←MTG-1924-05-13th-party-congress`[transmitted-and-protested|1924-05]: 5月18日移交列宁最后13份文件整体，并在大会讲坛抗议逼迫反对派公开认错。 ； `→MTG-1924-05-13th-party-congress`[testament-custodian|1924.05]: 5月18日移交列宁最后13份口授文件，5月22日长老会议反对其被压制，大会上反对强迫反对派公开检讨
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←MTG-1924-05-13th-party-congress`[retained-general-secretary|1924-05起]: 在季诺维也夫与加米涅夫力保下留任，6月2日十三届一中全会正式确认连任总书记。
- **`PER-zinoviev`**（格里戈里·季诺维也夫）: 老布尔什维克、共产国际首任主席（1919–1926）。1917年十月公开反对武装起义；1920年哈雷演说力推二十一条与阶级恐怖，1923年豪赌“德国十月”并首倡社民党“法西斯羽翼”论；借“三驾马车”排托后于1925年发起新反对派，1926年7月首因秘密第7条被逐出政治局，1927年底被开除后屈服。 ‖ `←MTG-1924-05-13th-party-congress`[triumvirate-leader|1924-05]: 主持大会政治报告，力保斯大林留任并要求左翼反对派公开认错。
- **`PER-kamenev`**（列夫·加米涅夫）: 老布尔什维克、首任全俄中执委主席。1917年自四月至立宪会议一贯坚守温和宪政社会主义联盟路线并公开反对十月起义；1924年十三大联手季诺维也夫压下《列宁遗嘱》，1925年十四大公开发言反斯大林“领袖”集权后失势；1928年7月密会布哈林并留下外泄笔记，反成右派致命罪证。 ‖ `←MTG-1924-05-13th-party-congress`[triumvirate-ally|1924-05]: 主持5月22日长老会议宣读遗嘱并背书留任斯大林，主导分组口头传达程序。 ； `→MTG-1924-05-13th-party-congress`[testament-presiding-suppressor|1924-05-23–31]: 主持代表团闭门宣读《列宁遗嘱》并否决全会公开与撤换斯大林动议，促成三驾马车权力巩固
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←MTG-1924-05-13th-party-congress`[opposition-isolated|1924-05]: 748表决权代表中反对派0席，5月26日发表“不论党是对是错，这是我的党”发言。
- **`PER-bukharin`**（尼古拉·布哈林）: 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。 ‖ `←MTG-1924-05-13th-party-congress`[promoted-politburo|1924-06-02起]: 十三届一中全会递补列宁遗缺升任政治局正式委员，加入后来的“七人小组”。
- **`INS-politburo-orgburo-secretariat`**（联共（布）中央政治局—组织局—书记处与官职等级名册制）: 1919年3月俄共八大后常设政治局、组织局与书记处，分掌政治决策、组织行政及日常党务人事。1922年4月斯大林任总书记后逐步控制议程、秘密文件分发与干部名册调配。经1924年七人小组协调、1925—1929年联盟重组与纪律整肃，托洛茨基、季诺维也夫、布哈林先后退出决策核心。 ‖ `←MTG-1924-05-13th-party-congress`[expanded-and-locked|1924-05至08]: 中央扩至53正式+34候补、中监委151人，组织局以破例初选投票权锁死代表结构并衍生“七…
- **`ORG-left-and-united-opposition`**（1923–1927年左翼反对派与托季联合反对派）: 1923年剪刀差危机触发的托洛茨基—普列奥布拉任斯基“左翼反对派”，经1926年春与季诺维也夫—加米涅夫“新反对派”结盟为托季联合反对派；以《四十六人声明》与《1927年政纲》批判官僚体制与“一国社会主义”、主张价格—财政渠道的计划工业化，于1927年12月十五大被组织摧毁。 ‖ `←MTG-1924-05-13th-party-congress`[excluded-from-voting-seats|1924-05]: 在十三大748名有表决权代表中获0席，被全票追认定性为“小资产阶级倾向”。
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←MTG-1924-05-13th-party-congress`[economic-context|1924]: 剪刀差危机、币制改革与工农商品流通问题制约大会政策议程。

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 1 项)
### `DEB-1922-lenin-testament-and-stalin-rise`：列宁晚年、格鲁吉亚事件与斯大林崛起机制
## [T1] 核心问题定义
列宁晚年口授文稿和格鲁吉亚冲突，是反官僚与反斯大林的总体“最后斗争”，还是对共同集权框架内具体做法的修正？《遗嘱》本身是否存在文本流转疑点？斯大林的上升又如何由个人策略、书记处机关、寡头集体领导与反对派失策共同解释？

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 反官僚最后斗争论 | Moshe Lewin, *Lenin's Last Struggle* (1968) | 将晚年口授群读为反大国沙文主义、改组监察院及撤换斯大林的连贯政治改革方案；但指出列宁始终未废除派别禁令与一党垄断。 | `CLM-lewin-1968-testament-intent`; `CLM-lewin-1968-georgian-affair-bureaucracy`; `CLM-lewin-1968-cooperation-shift` | 写于苏联全开档案前，连贯“总体计划”程度及12月22日电话定年受后续考据挑战。 |
| 民族政策修正 | Jeremy Smith, *The Bolsheviks and the National Question* (1999) | 强调列斯在集中制大原则上的长期共识，并据十二大特别会议解密速记揭示斯大林被迫作出的本土化妥协。 | `CLM-smith-jeremy-1999-georgian-affair-reassessed`; `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` | 行政协调解释须与列宁1923年3月5–6日对斯大林绝交信的激烈措辞并观。 |
| 后苏联档案与寡头共治论 | Oleg Khlevniuk, *Stalin* (2015) | 以斯大林1923–1927年多次亲口承认遗嘱存在及3月7日复函驳斥伪造论；指出1月4日补遗重在“权力再平衡”而非逐出高层，且1920年代寡头集体领导真实存在。 | `CLM-khlevniuk-2015-secretariat-and-nomenklatura`; `CLM-khlevniuk-2015-collective-leadership-erosion` | 需注意勿将1920年代末成熟名册规模倒推回1922年。 |
| 文献流转质疑与重定年派 | Stephen Kotkin, *Stalin, Vol. 1* (2014, Ch. 11) | 指出《给代表大会的信》缺失列宁亲签与原始速记底本、打字件经克鲁普斯卡娅与秘书圈流转存有加工疑窦，并据斯大林3月7日复函“约五周前”将电话冲突重定年于1923年1月下旬；同时强调斯大林不可替代的机关功能使其难因一纸信函下台。 | `CLM-kotkin-2014-geopolitics-and-ideology`; `L3 1922-12` 专章对勘 | 尚无直接物证证明秘书团凭空捏造，且难以解释斯大林本人在十三大与1927全会从未质疑文件真伪。 |
| 左翼悲剧论 vs 政治失误批判 | Isaac Deutscher (1959) vs Robert Service, *Trotsky* (2009) | 多伊彻痛惜托洛茨基3月6日拒绝落井下石错失良机且受困一党纪律；瑟维斯则据档案批评托洛茨基共享威权前提、两拒人民委员会副主席职务并在十二大傲慢避战，纯属政治判断失误。 | `CLM-deutscher-1959-disarmed-prophet-paradox`; `CLM-service-2009-trotsky-authoritarian-consensus`; `CLM-service-2009-trotsky-political-tactical-blunders` | 需将个人性格失误置于书记处与三驾马车结构结盟中评估。 |
| 俄国“伪列宁文本”极端派 | V. A. Sakharov (2003 遗嘱专著; 2012《十字路口》) | 其2003年专著极端断言遗嘱与民族札记系克鲁普斯卡娅—托派伪造；库内已入库的2012年著作则聚焦《论合作社》两稿差异与1920年代路线争夺（两书议题边界须严格区分）。 | `CLM-sakharov-2012-lenin-cooperative-plan-debates`; `CLM-sakharov-2012-nep-crossroads-1928` | 全盘伪造说遭赫列夫纽克、洛吉诺夫等主流俄罗斯档案学者一致否证。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 13/13 条)
- **`CLM-lewin-1968-testament-intent`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.10 'If Lenin Had Lived . . .'；列宁原文脚注见 Soch. XLV p. 392；XLIV p. 428]: 
- **`CLM-lewin-1968-georgian-affair-bureaucracy`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.9、Ch.10 与 Appendixes I–III, VII–VIII]: 
- **`CLM-khlevniuk-2015-collective-leadership-erosion`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（TRYING OUT COLLECTIVE LEADERSHIP 至 THE CHOICE）。工作区文本无纸质页码。]: 
- **`CLM-khlevniuk-2015-secretariat-and-nomenklatura`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（In Lenin's Shadow，GENERAL SECRETARY 至 1923 年 9 月组织局安排）；制度总论见 ops/xhtml/ch01a.html。工作区文本无纸质页码。]: 
- **`CLM-deutscher-1959-disarmed-prophet-paradox`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | （中译本无独立纸页；对应第二部 1923 年争论章）]: 
- **`CLM-lewin-1968-cooperation-shift`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.8 'Russia between West and East'；列宁原文脚注 Soch. XLV pp. 367, 370, 373, 387–88, 389]: 
- **`CLM-smith-jeremy-1999-georgian-affair-reassessed`** [`SCH-smith-jeremy`(杰里米·史密斯) | pp. 252-253, 260-262, 266-268, 285-288, 296-297]: 
- **`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`** [`SCH-smith-jeremy`(杰里米·史密斯) | pp. 311, 321-325, 327-331]: 
- **`CLM-kotkin-2014-geopolitics-and-ideology`** [`SCH-kotkin-stephen`(斯蒂芬·科特金) | EPUB Ch. 13 (OEBPS/9780698170100_EPUB_1-23.xhtml) & Coda (OEBPS/9780698170100_EPUB_1-25.xhtml)]: 
- **`CLM-service-2009-trotsky-authoritarian-consensus`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本第 23–24、28–29、37 章及引言]: 
- **`CLM-service-2009-trotsky-political-tactical-blunders`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本引言及第 31–32、37–38 章]: 
- **`CLM-sakharov-2012-lenin-cooperative-plan-debates`** [`SCH-sakharov-valentin`(瓦连京·萨哈罗夫) | EPUB Ch. 1.3 & Ch. 4.2]: 
- **`CLM-sakharov-2012-nep-crossroads-1928`** [`SCH-sakharov-valentin`(瓦连京·萨哈罗夫) | EPUB Ch. 4.2 & Ch. 4.3]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 2 条 L3 逐日细节见 `timeline/L3_daily/`)
