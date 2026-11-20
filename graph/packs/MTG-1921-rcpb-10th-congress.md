# 1-Hop 去重平衡上下文包：`MTG-1921-rcpb-10th-congress`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`MTG-1921-rcpb-10th-congress`** (俄国共产党（布尔什维克）第十次代表大会 | `cards/meetings/MTG-1921-rcpb-10th-congress.md` | `multi-perspective`): 已覆盖=`party-leadership, workers-opposition, kronstadt-social-history, institutional, trade-union-godson-schapiro-lebsky`；待补=`rural-delegate-voices, full-congress-stenogram`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 150字定性微摘要
1921年3月8日至16日，俄共（布）十大在经济崩溃与喀琅施塔得起义交织下召开。大会决定以粮食税取代余粮收集制，开启新经济政策转向；同时终结工会大辩论，通过《关于党的统一》禁止派别活动并谴责工人反对派。经济退却与党内纪律收紧并行，会后中央与书记处改组重塑了组织权力格局。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **出席规模与喀琅施塔得危机**：大会出席 **694** 名有表决权代表与 **296** 名有发言权代表（合计 990 人），代表 **732,521** 名党员（[DATA-04](../../data/DATA-04-party-membership-and-congress-votes-1903-1929.md)）。会议全程与喀琅施塔得水兵起义同步，近 **300** 名代表（含工人反对派与军事反对派骨干）响应动员踏上芬兰湾冰面参加镇压。[彼得罗巴甫洛夫斯克号决议](../../sources/web-archive/E02_E07_foundational_docs/1921-03-01_petropavlovsk-resolution.md)表达起义水兵重选苏维埃、取消粮食征发与恢复革命政党自由的诉求，不能以大会多数派的“白卫阴谋”定性替代；[Avrich 札记](../../reading-notes/avrich_1970_kronstadt/RN-W3-kronstadt-sailors-and-ideology.md)还原了水兵的社会构成与战时危机背景。
- **以粮食税取代余粮收集制（`1921-03-15`）**：需区分政策动因与起义时间差——列宁早于喀琅施塔得起义爆发前的 **`1921-02-08`** 已在政治局起草《农民问题提纲初稿》（`02-24` 提交中央）。`1921-03-15` 十大几近全票通过以粮食税取代余粮收集制，随即由全俄中执委于 `03-21` 颁布[实物税法令](../../sources/web-archive/E03_E08_party_and_state_docs/1921-03-21_decree-on-tax-in-kind-prodnalog.md)，将 1921–1922 年度全国粮食征额从 4.23 亿普特削减至 **2.4 亿普特**（降幅约 43%）。新经济政策自此起步，但国家仍紧握重工业、外贸“制高点”与一党政治垄断。
- **工会大辩论终局表决（`1921-03-14`）**：大会围绕工会在苏维埃国家中的地位进行终局表决：列宁、托姆斯基、季诺维也夫等人的《十人纲领》获 **`336` 票**，托洛茨基—布哈林“工会国家化”联合纲领获 **`50` 票**，施略普尼科夫—柯伦泰“工人反对派”（主张由“全俄生产者代表大会”管理国民经济）获 **`18` 票**，弃权 **`2` 票**（较 1921 年 1 月莫斯科省预选 `57 : 33 : 21` 差距进一步拉大）。决议将工会确立为党通向群众的“共产主义学校”与“传动带”。
- **《关于党的统一》、秘密第 7 条与中央改组（`1921-03-16`）**：大会通过[《关于党的统一》](../../sources/web-archive/E06_E10_turning_points/1921-03-16_on-party-unity.md)与《关于我们党内的工团主义和无政府主义倾向》，两项决议均仅遭遇**不足 `30` 张**反对/修正票（约 25–30 票）。审议中阿·谢·基谢廖夫（A. S. Kiselyov）警告列宁第 7 条无异于把“机关枪”架在同志面前；第 7 条秘密条款授权中央委员会与中央监察委员会联席会议以三分之二多数将违纪中央委员降格为候补委员直至开除出党——**该条款闭幕时秘而不宣，直至 `1924-01-17` 俄共（布）第十三次代表会议才由斯大林首次公开宣读**。会后中央委员会由 19 人扩编至 **25 名正式委员**（列宁派占 `20 : 5` 绝对多数，原三书记克列斯廷斯基、普列奥布拉任斯基、谢列布里亚科夫因在工会论争中支持托洛茨基而全部落选，**莫洛托夫**出任责任书记并升任政治局候补委员），同时出于怀柔吸纳工人反对派领袖施略普尼科夫与库图佐夫入中央，并否决了施略普尼科夫当场提出的辞职请求。

### 2.2 核心关系网络（结构化边表）
| 目标节点 ID | 关系类型 (Relation) | 适用时期 | 一句话关系摘要 | 证据锚点 |
| :--- | :--- | :--- | :--- | :--- |
| `EVT-1921-kronstadt` | concurrent-crisis | 1921-03 | 水兵起义与政府镇压同大会交织，近300名代表离会赴芬兰湾参战。 | CLM-avrich-1970-soviets-without-bolsheviks; RN-W3-kronstadt-sailors-and-ideology |
| `POL-nep` | policy-turn | 1921-03起 | 3月15日通过以粮食税取代余粮收集制，1921–22征额由4.23亿普特减至2.4亿普特。 | DATA-04-party-membership-and-congress-votes-1903-1929; DEB-1921-kronstadt-and-nep-origins |
| `POL-ban-on-factions-1921` | resolution | 1921-03-16 | 以不足30张反对票通过《关于党的统一》，内含秘而不宣的第7条三分之二除名机制。 | CLM-daniels-1960-tenth-congress-turning-point; DATA-04-party-membership-and-congress-votes-1903-1929 |
| `INS-politburo-orgburo-secretariat` | apparatus-reshuffle | 1921-03起 | 中央扩至25正式委员，原三书记全部落选，莫洛托夫接掌书记处重塑党务控制权。 | CLM-daniels-1960-tenth-congress-turning-point; RN-W1C-communist-oppositions-1918-1929 |
| `PER-lenin` | advocated | 1921-03 | 2月8日即草拟粮食税提纲，3月凭336票赢得工会辩论并主导禁派令与反工团主义决议。 | CLM-daniels-1960-tenth-congress-turning-point; DATA-04-party-membership-and-congress-votes-1903-1929 |
| `PER-trotsky` | union-debate-defeated | 1921-03 | 与布哈林所提联合纲领仅获50票，支持其路线的三名中央书记在改选中全部落选。 | DATA-04-party-membership-and-congress-votes-1903-1929; RN-W1C-communist-oppositions-1918-1929 |
| `PER-bukharin` | union-debate-defeated | 1921-03 | 在工会辩论后期与托洛茨基形成缓冲联合纲领，终局仅获50票。 | DATA-04-party-membership-and-congress-votes-1903-1929 |
| `PER-tomsky` | union-platform-ally | 1921-03 | 与列宁、季诺维也夫共推《十人纲领》，维系工会在NEP时期的有限保护与调适职能。 | CLM-schapiro-1981-end-of-illusion-unions-1917-to-tomsky-fall; CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions |
| `PER-zinoviev` | union-platform-ally | 1921-03 | 作为《十人纲领》主要推手之一在工会争论中联合列宁压制托洛茨基路线。 | DATA-04-party-membership-and-congress-votes-1903-1929 |
| `PER-molotov` | secretariat | 1921-03起 | 会后改组中接任中央责任书记并升任政治局候补委员，开启书记处新阶段。 | RN-W1C-communist-oppositions-1918-1929 |
| `PER-shlyapnikov` | workers-opposition-leader | 1921-03 | 工人反对派纲领仅获18票并遭谴责，但被怀柔吸纳入中央且辞职请求遭否决。 | CLM-kollontai-1921-all-russian-congress-of-producers-program; RN-W1C-communist-oppositions-1918-1929 |
| `PER-kollontai` | workers-opposition-theorist | 1921-03 | 撰写《工人反对派》纲领批判官僚化与旧专家治厂，主张全俄生产者代表大会管理经济。 | CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists; CLM-kollontai-1921-all-russian-congress-of-producers-program |
| `ORG-workers-opposition` | condemned | 1921-03-16 | 其“生产者代表大会”主张被定性为工团主义与无政府主义倾向，勒令解散派别组织。 | CLM-kollontai-1921-all-russian-congress-of-producers-program; CLM-daniels-1960-tenth-congress-turning-point |
| `ORG-democratic-centralists` | constrained | 1921-03 | 虽强调党内民主与集体原则，仍被全面纳入禁派纪律红线约束之下。 | CLM-daniels-1960-tenth-congress-turning-point |

### 2.3 史学争鸣光谱
- **经验共识**：大会以压倒性多数通过粮食税转向、十人纲领（336:50:18）与《关于党的统一》（反对票 `<30`），在经济放开的同时永久性收紧了党内派别红线；起义水兵、工人反对派与农民抗粮各有独立诉求，不可合并为单一反苏组织。
- **Robert V. Daniels（反对派与制度转折视角）**：视十大为俄国革命的根本转折点——列宁虽将禁派令与第 7 条定位为内战末期的紧急防御措施并保留“建设性批评”措辞，但书记处改组与组织铁律最终将其固化为官僚压制一切异见的永久机器。
- **Paul Avrich（社会史与喀琅施塔得视角）**：还原“没有布尔什维克的苏维埃”背后的战争创伤与饥荒现实，指出水兵诉求植根于 1917 年苏维埃民主传统而非白军复辟，且列宁早于起义前（2月8日）即已着手筹划粮食税。
- **亚历山德拉·柯伦泰（Alexandra Kollontai，1921，在场亲历者兼反对派论战视角）**：在向十大提交的《工人反对派》小册子中痛斥党政官僚体系与旧资产阶级专家凌驾于车间工人之上，提出由工会推举的“全俄生产者代表大会”接管生产；引用其文本时须严分“1921年现场工人异化见证”与“派别政治纲领”双重属性。
- **Leonard Schapiro（1981）、Joseph Godson（1981）与 Maxim Lebsky（列布斯基，2021）的工会史对照**：Schapiro 剖析党政机关从 1917 年到 1929 年托姆斯基倒台逐步剥夺工会独立性的政治路径；合编者兼第 4 章专章作者 **Joseph Godson（1981）** 进一步指出，十大将工会定型为兼顾“保护工人利益”与“提高生产”双重职能的“共产主义学校/传动带”，在 NEP 时期尚保留有限调适空间与集体合同余晖，直至 1929 年托姆斯基被罢免后才彻底蜕变为单向国家生产“传动带”；当代俄罗斯左翼社会史家 **Lebsky（2021）** 则从内战工业无产阶级“去阶级化”与 1920–1929 企业部门住房/福利基金（ФУБР）绑定切入，指出工人政治去主体化并非仅由自上而下的党禁造成，而是社会结构瓦解与“工业家长制”福利契约双向塑形的结果。

## 2. 一跳邻域全量微摘要目录 (去重后共 20 个节点，0 截断)
- **`CON-democratic-centralism-and-vanguard`**（先锋队党与民主集中制）: 布尔什维克组织原则的跨期复合概念：从民意党集中制与特卡乔夫“自觉少数”，经1902年职业革命家论、1905–1906年成文的民主集中制及1917年群众政党，至1921年禁派令与斯大林书记处官职名册制，派别空间收缩；部分制度史研究强调干部任命权日益压过民主原则。 ‖ `→MTG-1921-rcpb-10th-congress`[site-of-institutional-turning-point|1921-03]: 禁派令与秘密第7条把“统一”置于“民主”之上
- **`CON-workers-control`**（工人监督（工厂委员会与生产者自治））: 工人监督源自1905年车间行动；1917年彼得格勒工厂委员会为保就业、维持生产实行防御性监督，十月后写入《工人监督条例》。1918年起经济崩溃与国有化推动部分委员会并入工会，中央管理与劳动纪律强化；1921年生产者自治方案遭党内否决，但基层实践与合议管理并未骤然消失。 ‖ `→MTG-1921-rcpb-10th-congress`[condemned-as-anarcho-syndicalist-deviation-at|1921-03-08–03-16]: 工会问题三方案分别获多数派336、托洛茨基50、工人反对派18票；另有工团主义倾向决议，不能混为同一表决
- **`EVT-1920-1921-tambov-and-peasant-revolts`**（坦波夫安东诺夫起义与1920–1921年农民绿军风暴）: 1920年坦波夫抗征粮冲突扩大为安东诺夫领导的农民战争，与其他省份起义及城市工潮共振，暴露苏维埃农村统治危机。1921年粮食税让步与重兵围剿、人质及集中营政策并行；主力在夏季受挫，零星抵抗延续，不能把新经济政策视为农村随即恢复和解。 ‖ `→MTG-1921-rcpb-10th-congress`[economic_and_political_response|1921.03.08—16]: 十大在危机中批准实物税方向并禁止党内派别
- **`EVT-1921-kronstadt`**（喀琅施塔得水兵起义）: 1921年二月底至三月，喀琅施塔得水兵与居民以十五条决议要求改选苏维埃、开放劳动者及左翼政治自由，并成立临时革命委员会。红军跨冰夺回要塞，镇压与实物税、禁派决议交叠；经济退却早已酝酿，起义加剧其紧迫性，却未带来政治权力的开放。 ‖ `→MTG-1921-rcpb-10th-congress`[concurrent_decisions|1921.03.08—16]: 大会与攻岛并行，经济与组织决议不能混为一次表决 ； `←MTG-1921-rcpb-10th-congress`[concurrent-crisis|1921-03]: 水兵起义与政府镇压同大会交织，近300名代表离会赴芬兰湾参战。
- **`INS-rabkrin-and-ccc`**（中央监察委员会与工农检查人民委员部（联合工作体制））: 工农检查人民委员部是国家监察机关，中监委是党的纪律监督机关。1923年改组后共同领导、联合办公，仍为两个机构，未在法律上合并；列宁的合并设想及Carr、Lewin的叙述用语须与此区分。改革旨在改善官僚机器、维护中央团结，联合机构随后参与党内审查处分，监督亦受权力关系制约。 ‖ `→MTG-1921-rcpb-10th-congress`[institutionalized_party_control_functions|1921.03]: 党内监察与纪律职能进一步制度化的节点（条文待核）
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←MTG-1921-rcpb-10th-congress`[policy-turn|1921-03起]: 3月15日通过以粮食税取代余粮收集制，1921–22征额由4.23亿普特减至2.4亿普特。
- **`POL-ban-on-factions-1921`**（《关于党的统一》派别禁令）: 俄共十大于1921年3月16日通过《关于党的统一》，要求解散按纲领组成的派别，并保留规定渠道的批评。秘密第七条设中央领导成员的特殊处分程序；1924年1月公开宣读、1926年7月首次动用开除季诺维也夫出政治局，危机措置遂渐成约束反对派的工具，但不同年份执行不等同原条文。 ‖ `←MTG-1921-rcpb-10th-congress`[resolution|1921-03-16]: 以不足30张反对票通过《关于党的统一》，内含秘而不宣的第7条三分之二除名机制。 ； `→MTG-1921-rcpb-10th-congress`[通过场合|1921-03-16]: 大会以压倒多数通过公开条款与秘密第7条，同步开启NEP。
- **`INS-politburo-orgburo-secretariat`**（联共（布）中央政治局—组织局—书记处与官职等级名册制）: 1919年3月俄共八大后常设政治局、组织局与书记处，分掌政治决策、组织行政及日常党务人事。1922年4月斯大林任总书记后逐步控制议程、秘密文件分发与干部名册调配。经1924年七人小组协调、1925—1929年联盟重组与纪律整肃，托洛茨基、季诺维也夫、布哈林先后退出决策核心。 ‖ `←MTG-1921-rcpb-10th-congress`[apparatus-reshuffle|1921-03起]: 中央扩至25正式委员，原三书记全部落选，莫洛托夫接掌书记处重塑党务控制权。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←MTG-1921-rcpb-10th-congress`[advocated|1921-03]: 2月8日即草拟粮食税提纲，3月凭336票赢得工会辩论并主导禁派令与反工团主义决议。
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←MTG-1921-rcpb-10th-congress`[union-debate-defeated|1921-03]: 与布哈林所提联合纲领仅获50票，支持其路线的三名中央书记在改选中全部落选。
- **`PER-bukharin`**（尼古拉·布哈林）: 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。 ‖ `←MTG-1921-rcpb-10th-congress`[union-debate-defeated|1921-03]: 在工会辩论后期与托洛茨基形成缓冲联合纲领，终局仅获50票。
- **`PER-tomsky`**（米哈伊尔·托姆斯基）: 印刷工出身的布尔什维克工会领袖，长期主持全俄及全苏工会中央理事会，1922年进入政治局。工会争论中支持列宁，既限制生产者自治，又在新经济政策下维护集体合同和劳动保护。1928—1929年与布哈林、李可夫抵制激进转轨，遭干部改组夺去工会阵地，1936年自杀。 ‖ `←MTG-1921-rcpb-10th-congress`[union-platform-ally|1921-03]: 与列宁、季诺维也夫共推《十人纲领》，维系工会在NEP时期的有限保护与调适职能。
- **`PER-zinoviev`**（格里戈里·季诺维也夫）: 老布尔什维克、共产国际首任主席（1919–1926）。1917年十月公开反对武装起义；1920年哈雷演说力推二十一条与阶级恐怖，1923年豪赌“德国十月”并首倡社民党“法西斯羽翼”论；借“三驾马车”排托后于1925年发起新反对派，1926年7月首因秘密第7条被逐出政治局，1927年底被开除后屈服。 ‖ `←MTG-1921-rcpb-10th-congress`[union-platform-ally|1921-03]: 作为《十人纲领》主要推手之一在工会争论中联合列宁压制托洛茨基路线。
- **`PER-molotov`**（维亚切斯拉夫·莫洛托夫）: 莫洛托夫是布尔什维克党务骨干与斯大林主要副手。1917年二月在《真理报》及俄国局反对支持临时政府；1921年任中央责任书记，后以书记处工作协同斯大林掌权。1928年11月至1929年4月接掌莫斯科委员会，并加强斯大林阵营对共产国际的控制，推动集体化加速。 ‖ `←MTG-1921-rcpb-10th-congress`[secretariat|1921-03起]: 会后改组中接任中央责任书记并升任政治局候补委员，开启书记处新阶段。
- **`PER-shlyapnikov`**（亚历山大·什利亚普尼科夫）: 金属车工出身的老布尔什维克，一战时主持北欧交通线与俄国局，1917年任首届劳动人民委员。1920—1922年领导工人反对派，主张生产者自治；十大落败后入中央，秘密处分动议又差一票未过。其反官僚诉求与维护一党政权并存，晚年回忆须与当时记录对读，1937年遇害。 ‖ `←MTG-1921-rcpb-10th-congress`[workers-opposition-leader|1921-03]: 工人反对派纲领仅获18票并遭谴责，但被怀柔吸纳入中央且辞职请求遭否决。 ； `→MTG-1921-rcpb-10th-congress`[defeated_and_coopted|1921-03]: 纲领获18票，本人入中央且辞职被否决，不能把禁派等同当场开除
- **`PER-kollontai`**（亚历山德拉·柯伦泰）: 将军家庭出身的马克思主义女工运动家，1917年支持四月提纲，十月后任国家救济人民委员。主持妇女部并倡家务社会化，1921年为工人反对派撰写纲领，批判专家治厂与官僚委任。其解放理想遭遇福利紧缩、就业隔离及党内纪律的约束；1922年转入外交，历驻挪威、墨西哥、瑞典而幸存。 ‖ `←MTG-1921-rcpb-10th-congress`[workers-opposition-theorist|1921-03]: 撰写《工人反对派》纲领批判官僚化与旧专家治厂，主张全俄生产者代表大会管理经济。 ； `→MTG-1921-rcpb-10th-congress`[defeated_spokesperson|1921-03]: 散发纲领并参战工会争论，生产者大会方案获18票而被拒
- **`ORG-workers-opposition`**（工人反对派）: 俄共（布）党内以产业工人和工会干部为主体的左翼反对派（1920–1922），由什利亚普尼科夫、梅德韦杰夫及理论代言人柯伦泰领导。在1920–1921年工会争论中痛斥党政官僚化与专家“一长制”，主张由“全俄生产者代表大会”及工会自治管理国民经济；1921年十大被定性为无政府工团主义倾向并遭解散。 ‖ `←MTG-1921-rcpb-10th-congress`[condemned|1921-03-16]: 其“生产者代表大会”主张被定性为工团主义与无政府主义倾向，勒令解散派别组织。 ； `→MTG-1921-rcpb-10th-congress`[condemned-and-dissolved-at|1921-03-08–03-16]: 在俄共十大上作为工会争论三派之一参辩，最终被《关于党内工团主义和无政府主义倾向》及《关于党的统一》决议定性并勒令解散
- **`ORG-democratic-centralists`**（民主集中派）: 民主集中派是1919年初结成的布尔什维克党内反对派，萨普罗诺夫、奥新斯基、弗·斯米尔诺夫等为重要代表，批评以任命和行政命令取代集体领导与基层参与。成员及立场随时间变化：1923年部分人联署《四十六人声明》；后期“十五人集团”须与早期派别区分。 ‖ `←MTG-1921-rcpb-10th-congress`[constrained|1921-03]: 虽强调党内民主与集体原则，仍被全面纳入禁派纪律红线约束之下。 ； `→MTG-1921-rcpb-10th-congress`[subject-to-congress-resolution|1921-03]: 十大统一决议限制有组织派别
- **`MTG-1922-03-11th-party-congress`**（俄国共产党（布尔什维克）第十一次代表大会（1922年））: 1922-03-27至04-02[N.S.]，俄共十一大在莫斯科召开，为列宁最后出席的党代会。他宣布NEP退却结束，强调管理、文化与官僚主义；大会警告工人反对派。04-03新中央全会设总书记并选出斯大林，04-04《真理报》公布；任命、公布均须与大会决定区分。 ‖ `→MTG-1921-rcpb-10th-congress`[disciplinary_precedent|1921–1922]: 十大禁派决议及其未公开第7点构成十一大指控反对派的背景，具体适用程序应分别核对。
- **`ORG-bolsheviks-rcpb-vkpb`**（布尔什维克派—俄共（布）—联共（布））: 布尔什维克起于1903年社民工党二大后的党内多数派，经流亡、地下活动与1917年群众扩张成为执政党；1918年称俄共（布），1925年称联共（布）。它从地方主动性较强的革命党，演变为拥有任命网络与纪律制裁的党国核心，过程分阶段且存争议。 ‖ `→MTG-1921-rcpb-10th-congress`[party-congress|1921-03]: 通过《关于党的统一》，限制有组织派别

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 3 项)
- **`DEB-1921-trade-union-controversy-and-party-unity`**（1921年工会争论、工人反对派与党内统一之争 | `historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md` | 流派 `lenin-ten, trotsky-militarization, workers-opposition, party-institutional-history, labor-social-history, industrial-paternalism`）：内战结束之际，工会应成为国家管理生产的传动机构，还是维护工人利益并参与管理的独立空间？工人反对派、托洛茨基和列宁的方案分歧，如何与第十次党代表大会禁止派别相互交织？喀琅施塔得危机既是决议援引的背景，也是有待独立考察的社会抗议，不能混同党内派别。
- **`DEB-1921-kronstadt-and-nep-origins`**（喀琅施塔得起义与新经济政策的双轨转折 | `historiography/debates/DEB-1921-kronstadt-and-nep-origins.md` | 流派 `social-history, political-institutional, provincial-and-state-society, soviet-orthodox`）：喀琅施塔得是白卫阴谋、农民反抗，还是要求重建劳动者苏维埃民主的革命者起义？1921年实物税与禁止党内派别同期出现，如何解释经济退却和政治收紧的联系、彼此差异及长期后果？
- **`DEB-1918-war-communism-ideology-or-emergency`**（战时共产主义与早期一党制本质之争：内战应急、乌托邦跃进还是国家统制连续？ | `historiography/debates/DEB-1918-war-communism-ideology-or-emergency.md` | 流派 `emergency-carr-mawdsley, utopian-tragedy-malia-pipes, state-continuity-lih-smith, mixed-causation-rabinowitch-lewin`）：1918至1921年的全面国有化、余粮收集制、取缔私商、劳动军事化，以及多党苏维埃收为一党专政，究竟是内战与供给崩溃逼出的生存应急，还是反市场乌托邦的激进兑现，抑或一战以来国家统制与基层危机交互的结果？“战时共产主义”是1921年转向时的事后标签，须分清措施序列与事后总结。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/27 条)
- **`CLM-avrich-1970-soviets-without-bolsheviks`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 198-201, 179-180]: 
- **`CLM-daniels-1960-tenth-congress-turning-point`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 146-153]: Daniels：1921年十大将党统一转化为压缩合法反对空间的组织制度
- **`CLM-schapiro-1981-end-of-illusion-unions-1917-to-tomsky-fall`** [`SCH-schapiro-leonard`(伦纳德·沙皮罗) | Book pp. 1–14 [PDF pp. 13–26]]: 
- **`CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions`** [`SCH-godson-joseph`(约瑟夫·戈德森 · cold-war-labor-studies) | Book pp. 106–111, 121, 128–129 [PDF pp. 118–123, 133, 140–141]]: 
- **`CLM-kollontai-1921-all-russian-congress-of-producers-program`** [`SCH-kollontai-alexandra`(亚历山德拉·柯伦泰 · participant-primary-text) | PDF pp. 11-21, 25-30]: 
- **`CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists`** [`SCH-kollontai-alexandra`(亚历山德拉·柯伦泰 · participant-primary-text) | PDF pp. 2-11, 22-27]: 
- **`CLM-lebsky-industrial-paternalism-origins-1917-1929`** [`SCH-lebsky-maksim`(马克西姆·列布斯基) | PDF pp. 9–26, 29–36, 48–49]: 
- **`CLM-service-2009-trotsky-authoritarian-consensus`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本第 23–24、28–29、37 章及引言]: 
- **`CLM-filtzer-1986-nep-unemployment-and-shopfloor-bargaining`** [`SCH-filtzer-donald`(唐纳德·费尔泽) | pp. 19–29, 44–45, 77–78, 274]: 
- **`CLM-filtzer-1986-1929-tomsky-purge-and-shock-work`** [`SCH-filtzer-donald`(唐纳德·费尔泽) | pp. 22–24, 68–72, 76–82, 96–108, 274, 280–282, 287]: 
- **`CLM-avrich-1970-sailor-social-composition`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 101-105]: 
- **`CLM-avrich-1970-white-plot-refutation`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 143-147, 816-818]: 
- **`CLM-siegelbaum-1992-nep-fragile-social-compromise`** [`SCH-siegelbaum-lewis`(刘易斯·H·西格尔鲍姆) | pp. 84, 91-93, 102-117, 136-144, 180-186 (PDF pp. 98, 105-107, 116-131, 150-158, 194-200)]: 
- **`CLM-carr-1952-nep-retreat-and-commanding-heights`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 118-166 (Chs. 18–20)]: 
- **`CLM-figes-1996-peasant-wars-and-nep-retreat`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 775-785]: 
- **`CLM-raleigh-2001-center-periphery-weak-state-nep`** [`SCH-raleigh-donald`(唐纳德·J·罗利) | Local PDF pp. 16–18, 139–173; English print pagination not verified]: 
- **`CLM-carr-1952-war-communism-internal-contradictions`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 70-120 (Chs. 17–18)]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 56–58, 69, 185–188, 217–218, 283–284]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-smith-sa-1983-from-workers-control-to-nationalization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 155–156, 166–169, 177–179, 184–186, 192（即源文件标注 PDF pp. 160–161, 171–174, 182–184, 189–191, 197）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 2 条，另有 6 条 L3 逐日细节见 `timeline/L3_daily/`)
- **1921-03-08 [N.S.]** (`TL-W15-L1-E08-02`, L1): **俄共（布）十大开幕** — 大会与围攻水兵同时进行，经济转向和党内纪律收紧在此相接。
- **1921-03-08 [N.S.]** (`TL-W3-1921-03-08`, L2): **俄共（布）十大开幕** — 大会以实物税代替余粮收集，并通过《关于党的统一》。实物税不是新经济政策的全部。主账 TL-1921-03-08 把 DEB-1928 挂在本日，候选记录不沿用。会议卡写闭幕于3月16日，本批未在丹尼尔斯重读闭幕日。事件卡称政治局2月已因坦波夫讨论实物税，本批未重读 Service 原页。
