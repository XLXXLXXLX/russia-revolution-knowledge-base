# 1-Hop 去重平衡上下文包：`EVT-1921-kronstadt`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`EVT-1921-kronstadt`** (喀琅施塔得水兵起义 | `cards/events/EVT-1921-kronstadt.md` | `multi-perspective`): 已覆盖=`anarchist-social-history, soviet-orthodox, trotskyist, western-political-history`；待补=`post-soviet-archival-1999, gendered-social-history`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 150字定性微摘要
1921年二月底至三月，喀琅施塔得水兵与居民以十五条决议要求改选苏维埃、开放劳动者及左翼政治自由，并成立临时革命委员会。红军跨冰夺回要塞，镇压与实物税、禁派决议交叠；经济退却早已酝酿，起义加剧其紧迫性，却未带来政治权力的开放。

## [T2] 核心脉络、关系网络与史学争鸣

### 2.1 核心历史脉络

**从农村战争与工潮到舰上抗议**。坦波夫等地农民战争、复员和饥馑，以及1921年2月彼得格勒工潮，共同侵蚀内战胜利后的政权基础。舰上代表赴彼得格勒了解工人处境后提出改革要求。粮食税并非等到舰队起义才被想到：Carr所引列宁2月8日农民问题初步提纲及政治局讨论、2月24日提交中央的方案均在前；本卡以A 级转引确认这一时序，不把酝酿写成完整NEP在2月已经决定实施（`CLM-carr-1952-nep-retreat-and-commanding-heights`）。Raleigh的萨拉托夫工潮案例也表明，政治权利与供给诉求并非首都海军基地独有。

**十五条决议与临时革命委员会（2月28日—3月2日）**。2月28日“彼得罗巴甫洛夫斯克”号舰上通过决议，3月1日支队与全要塞大会再行确认；3月2日代表会议成立以彼得里琴科为首的临时革命委员会，扣押库兹明等人员，形成公开武装对抗。站内实存原典文件名为 `1921-03-01_petropavlovsk-resolution.md`，载3月1日文本，2月28日先行通过另有政府通报旁证；没有独立入藏一份2月28日异文，不能凭任务中的建议文件名造出链接。

十五条要求无记名改选苏维埃，给工人、农民、无政府派和左翼社会主义者言论出版及集会空间，释放相关政治犯，取消政党宣传特权和阻击队，平等配给，并允许不雇工的农户自主经营及个人手工业。它争取的是劳动者和左翼的苏维埃民主，不是无限制的资产阶级政党自由。支队大会“全票、两票弃权”与卫戍大会“压倒多数、瓦西里耶夫和加里宁反对”是两次表决，不合并为一个票数。政治文本既是一手诉求证据，也有动员目的，不能自动证明所有居民态度一致。

**最后通牒与跨冰进攻（3月5—18日）**。3月5日最后通牒由托洛茨基署名发布，并与红军总司令谢·谢·卡梅涅夫（S. S. Kamenev，区别于列·鲍·加米涅夫）及新任第七集团军司令图哈切夫斯基联合签发（Avrich ch06 p.161 fn.25；1921年3月微距卷）。3月7日炮击后，8日第一次跨冰强攻失利；16日炮火准备、17日凌晨总攻，18日政府军控制要塞和两艘主力舰。约300名十大代表赴前线与约8,000名军民撤入芬兰都是各自的近似量，不能由此推出起义总人数或死亡数。战斗死亡、溺亡、攻陷后的处决、后续判刑和流亡人口应分别统计；现有材料不宜合成一个未经分母说明的总伤亡数字。

**经济退却与政治封闭相伴**。俄共十大3月8—16日在战事中召开，3月15日批准以粮食税替代余粮征集的方向，16日通过《关于党的统一》，21日国家法令落实实物税。镇压由前线指挥机关实施，托洛茨基承担最后通牒和路线辩护的政治责任；不据其后来自辩免除责任，也不把现场指挥虚归其个人。水兵危机加强了让步和统一纪律的紧迫性，却未换取分享苏维埃权力；工人反对派同样反对官僚化，但与水兵无已证直接组织联系，并仍处于一党政治前提内（Daniels，RN-W1C）。

### 2.2 核心关系网络（结构化边表）

| 目标节点 ID | 关系类型 | 有效时段（公历） | 关系实质摘要 | 核心依据 |
| :--- | :--- | :--- | :--- | :--- |
| `EVT-1920-1921-tambov-and-peasant-revolts` | `parallel_crisis` | 1920—1921.03 | 农民战争和城市／舰队抗议并发，不能合并为统一组织 | Figes；Raleigh；Avrich |
| `POL-war-communism` | `social_and_economic_background` | 1920—1921.03 | 征粮、配给、阻击队及军事化统制形成反抗对象 | 十五条决议；`DEB-1918-war-communism-ideology-or-emergency` |
| `POL-nep` | `accelerated_existing_retreat` | 1921.02—03 | 粮食税酝酿在起义前，战事增强十大批准转向的压力 | `CLM-carr-1952-nep-retreat-and-commanding-heights` |
| `MTG-1921-rcpb-10th-congress` | `concurrent_decisions` | 1921.03.08—16 | 大会与攻岛并行，经济与组织决议不能混为一次表决 | `DATA-04-party-membership-and-congress-votes-1903-1929` |
| `POL-ban-on-factions-1921` | `political_closure` | 1921.03.16起 | 危机背景下限制党内组织化异议，未给予水兵的多左翼苏维埃方案合法空间 | `CLM-daniels-1960-tenth-congress-turning-point` |
| `PER-trotsky` | `ultimatum_and_political_responsibility` | 1921.03 | 签发通牒并捍卫镇压路线，与前线战术指挥分列 | Avrich；RN-W3 |
| `PER-tukhachevsky` | `operational_command` | 1921.03 | 指挥第七集团军跨冰进攻 | 1921年3月微距卷；Avrich |
| `INS-rkka-red-army-and-rvr` | `military_assault` | 1921.03.07—18 | 正规军、军校学员与党代表参加攻岛，参战人数不等于伤亡 | Avrich；DATA-04 |
| `INS-cheka-gpu-ogpu` | `post_capture_repression` | 1921.03以后 | 契卡处理俘虏与后续镇压；判刑、处决及流亡须分统计管道 | Avrich；机构沿革卡 |

### 2.3 主要史学争鸣与多流派解释

**可核事实与解释分歧**：十五条、3月2日委员会成立、政府进攻与3月18日要塞失守有文本与研究支持。外部白卫阴谋是否事前发动起义、军人社会构成能否解释其政治性质、镇压是否必要，以及NEP与禁派的因果关系，均须保留具名解释与证据限制。

- **Paul Avrich的反阴谋论与水兵社会史**：流亡者确有计划及事后援助企图，但他未找到这些计划在起义前已控制舰上领导的可信证据；事后求援不构成事前操纵证明（`CLM-avrich-1970-white-plot-refutation`）。他承认1921年舰队四分之三以上海员为农民出身，却指出老水兵和技师仍领导起义，新老人员都受乡村苦难影响；“农民成分”不是“新兵取代革命者”的同义词；站内 Figes（ch22）与微距卷转引 Israel Getzler 记“《彼得罗巴甫洛夫斯克》与《塞瓦斯托波尔》号两艘主力舰94%舰员于1918年前入伍”，但该口径仅覆盖两舰且 Getzler 原书未入藏，不能外推代表全要塞驻军（`CLM-avrich-1970-sailor-social-composition`）。
- **Avrich对口号的校勘**：“苏维埃不要共产党人”见于别处农民武装及流亡自由派的转述，不能写成喀琅施塔得决议自身的口号。水兵反对党独占而容许左翼布尔什维克在改选苏维埃中参加；米留科夫把运动描述成排除共产党、进而恢复立宪会议，属于外部政治解释（`CLM-avrich-1970-soviets-without-bolsheviks`）。
- **布尔什维克当事人及托洛茨基的保卫专政论**：要塞地位、融冰风险和外国干涉记忆构成其真实安全焦虑；以白卫反革命定性则同时具有宣传和镇压正当化作用。1921年通告、发令行为与托洛茨基1930年代事后辩护有不同史料属性，“悲剧性必要”不是已经验证的军事反事实。
- **Robert V. Daniels、Orlando Figes与Donald J. Raleigh的分层解释**：Daniels以十大为党内组织史关键转折，也保留规则当时的程序限制；Figes把水兵危机放入普遍农民战争，Raleigh以萨拉托夫说明物质让步未立刻恢复地方同意。三者共同反对把NEP写成一日完成的和解，但不能把经济抗议、党内派别和基地临时革命委员会归为同一运动。相关争议以喀琅施塔得／NEP起源、战时共产主义及工会／党内统一三张母题卡分工承接。

## 2. 一跳邻域全量微摘要目录 (去重后共 14 个节点，0 截断)
- **`CON-soviet`**（苏维埃：代表委员会与国家形式的系谱）: 苏维埃原为会议或委员会之意。1905年工人代表机构从罢工协调走向政治权力雏形；1917年工兵农苏维埃成为多党竞争与双重政权场域。十月后1918年宪法确立城乡五比一不等权与阶级剥权机制，二十年代“活跃苏维埃”实验仍受制于一党垄断，1921年喀琅施塔得亦曾诉诸苏维埃民主。 ‖ `→EVT-1921-kronstadt`[竞争性诉求|1921.03]: 起义水兵要求不记名自由重选苏维埃、打破一党垄断。
- **`EVT-1920-1921-tambov-and-peasant-revolts`**（坦波夫安东诺夫起义与1920–1921年农民绿军风暴）: 1920年坦波夫抗征粮冲突扩大为安东诺夫领导的农民战争，与其他省份起义及城市工潮共振，暴露苏维埃农村统治危机。1921年粮食税让步与重兵围剿、人质及集中营政策并行；主力在夏季受挫，零星抵抗延续，不能把新经济政策视为农村随即恢复和解。 ‖ `→EVT-1921-kronstadt`[overlapping_regime_crisis|1921.02—03]: 农民反征粮与水兵争取自由苏维埃并发，口号和组织不可直接等同 ； `←EVT-1921-kronstadt`[parallel_crisis|1920—1921.03]: 农民战争和城市／舰队抗议并发，不能合并为统一组织
- **`POL-war-communism`**（战时共产主义）: 1918年夏至1921年3月苏维埃经济政策总称：余粮收集制、中小工业国有化、取缔私商、货币贬值与实物配给并举；因内战饥荒与国家能力崩溃而强化，却在1921年喀琅施塔得与坦波夫危机下为新经济政策实物税所取代；其性质是应急、乌托邦跃进还是国家统制传统延续，史家分歧剧烈。 ‖ `←EVT-1921-kronstadt`[social_and_economic_background|1920—1921.03]: 征粮、配给、阻击队及军事化统制形成反抗对象 ； `→EVT-1921-kronstadt`[precipitated-retreat|1921-03]: 起义与农村战争共振，促使列宁在十大宣布新经济政策退却
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←EVT-1921-kronstadt`[accelerated_existing_retreat|1921.02—03]: 粮食税酝酿在起义前，战事增强十大批准转向的压力 ； `→EVT-1921-kronstadt`[precipitated_by|1921.02–03]: 农村安东诺夫等农民起义、彼得格勒/萨拉托夫工潮与喀琅施塔得水兵起义共同倒逼经济退却
- **`MTG-1921-rcpb-10th-congress`**（俄国共产党（布尔什维克）第十次代表大会）: 1921年3月8日至16日，俄共（布）十大在经济崩溃与喀琅施塔得起义交织下召开。大会决定以粮食税取代余粮收集制，开启新经济政策转向；同时终结工会大辩论，通过《关于党的统一》禁止派别活动并谴责工人反对派。经济退却与党内纪律收紧并行，会后中央与书记处改组重塑了组织权力格局。 ‖ `←EVT-1921-kronstadt`[concurrent_decisions|1921.03.08—16]: 大会与攻岛并行，经济与组织决议不能混为一次表决 ； `→EVT-1921-kronstadt`[concurrent-crisis|1921-03]: 水兵起义与政府镇压同大会交织，近300名代表离会赴芬兰湾参战。
- **`POL-ban-on-factions-1921`**（《关于党的统一》派别禁令）: 俄共十大于1921年3月16日通过《关于党的统一》，要求解散按纲领组成的派别，并保留规定渠道的批评。秘密第七条设中央领导成员的特殊处分程序；1924年1月公开宣读、1926年7月首次动用开除季诺维也夫出政治局，危机措置遂渐成约束反对派的工具，但不同年份执行不等同原条文。 ‖ `←EVT-1921-kronstadt`[political_closure|1921.03.16起]: 危机背景下限制党内组织化异议，未给予水兵的多左翼苏维埃方案合法空间 ； `→EVT-1921-kronstadt`[危机催化剂|1921.03]: 起义震撼催化代表大会迅速收紧党内派别活动空间。
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←EVT-1921-kronstadt`[ultimatum_and_political_responsibility|1921.03]: 签发通牒并捍卫镇压路线，与前线战术指挥分列 ； `→EVT-1921-kronstadt`[suppressor|1921-03]: 下令并统筹图哈切夫斯基部强攻平息水兵起义，事后掩盖决策过程并向外国媒体归咎白军阴谋，成为后期民主诉求的最大道德软肋
- **`PER-tukhachevsky`**（米哈伊尔·图哈切夫斯基）: 红军统帅、军事理论家，前近卫军少尉，历掌第5集团军与高加索方面军。1920年率西方面军攻华沙失败，与斯大林及西南方面军就利沃夫调兵和败责长期争执；1921年镇压喀琅施塔得起义，指挥坦波夫清剿重创安东诺夫主力，1925–1928年任红军参谋长。 ‖ `←EVT-1921-kronstadt`[operational_command|1921.03]: 指挥第七集团军跨冰进攻 ； `→EVT-1921-kronstadt`[assault_commander|1921.03.05–03.18]: 奉命统率第7集团军踏冰强攻平定喀琅施塔得水兵起义
- **`INS-rkka-red-army-and-rvr`**（工农红军与共和国革命军事委员会（РККА 与 РВСР））: 工农红军由1918年初志愿建军转向征兵与集中指挥；共和国革命军事委员会依靠前沙俄军事专家、政治委员及铁路内线组织内战。战后大裁军和伏龙芝改革建立正规军与地方民兵混合体制，1925至1929年伏罗希洛夫主政与干部工农化在政治控制与训练效能间形成持久张力。 ‖ `←EVT-1921-kronstadt`[military_assault|1921.03.07—18]: 正规军、军校学员与党代表参加攻岛，参战人数不等于伤亡
- **`INS-cheka-gpu-ogpu`**（全俄肃反委员会—国家政治保卫局与总局（ВЧК–ГПУ–ОГПУ 制度档案））: 苏维埃政治警察谱系：1917年12月人民委员会内部决议创立契卡，1918年红色恐怖中央地行刑权演变；1922年改为苏俄内务部GPU，1923年设联盟OGPU，随后重建法外特别会议。机关兼事工农情绪监测与镇压，在1927年战争恐慌、沙赫特案及1928—1929年强征中作用关键。 ‖ `←EVT-1921-kronstadt`[post_capture_repression|1921.03以后]: 契卡处理俘虏与后续镇压；判刑、处决及流亡须分统计管道
- **`ORG-workers-opposition`**（工人反对派）: 俄共（布）党内以产业工人和工会干部为主体的左翼反对派（1920–1922），由什利亚普尼科夫、梅德韦杰夫及理论代言人柯伦泰领导。在1920–1921年工会争论中痛斥党政官僚化与专家“一长制”，主张由“全俄生产者代表大会”及工会自治管理国民经济；1921年十大被定性为无政府工团主义倾向并遭解散。 ‖ `→EVT-1921-kronstadt`[ideological-resonance-without-org-link|1921-03]: 水兵对“委员专制”与工会官僚化的控诉与工人反对派高度共鸣，但双方毫无组织联系，工人反对派代表更参与了武装平叛
- **`PER-makhno`**（涅斯托尔·马赫诺）: 乌克兰古利亚伊波列无政府共产主义农民统帅（1888–1934）。创建“革命起义军（黑军）”与自由苏维埃实验；内战中与红军多次合作、破裂，1919年秋破袭邓尼金后方，1920年11月其部队参加克里米亚战役，随即遭红军全面围剿，1921年越境流亡并客居巴黎。 ‖ `→EVT-1921-kronstadt`[ideological_affinity|1921.03]: 喀琅施塔得“自由苏维埃”诉求与马赫诺派遥相呼应，但Avrich考证黑军“不要共产党人”口号比水兵更为排他
- **`PER-shlyapnikov`**（亚历山大·什利亚普尼科夫）: 金属车工出身的老布尔什维克，一战时主持北欧交通线与俄国局，1917年任首届劳动人民委员。1920—1922年领导工人反对派，主张生产者自治；十大落败后入中央，秘密处分动议又差一票未过。其反官僚诉求与维护一党政权并存，晚年回忆须与当时记录对读，1937年遇害。 ‖ `→EVT-1921-kronstadt`[no_direct_organizational_alliance|1921-03]: 反官僚语言相近不等于组织联手；Daniels明确区分二者并记党内反对派支持镇压
- **`ORG-psr`**（社会革命党）: 1901年末合并建立的俄国新民粹派政党，以土地社会化纲领与战斗组织暗杀闻名。1917年选民基数居全俄之冠却在战争、分地拖延与左翼分裂中失势；虽夺立宪会议多数仍遭解散，内战“第三条道路”溃于高尔察克政变，1922年莫斯科公审后在国内覆灭。 ‖ `→EVT-1921-kronstadt`[echo-and-alleged-link|1921.03]: 水兵起义与坦波夫农民运动虽提出重选自由苏维埃与反对征粮，但布尔什维克指控社革党（及契卡在1922审判中借题发挥）居中策动

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 3 项)
- **`DEB-1918-war-communism-ideology-or-emergency`**（战时共产主义与早期一党制本质之争：内战应急、乌托邦跃进还是国家统制连续？ | `historiography/debates/DEB-1918-war-communism-ideology-or-emergency.md` | 流派 `emergency-carr-mawdsley, utopian-tragedy-malia-pipes, state-continuity-lih-smith, mixed-causation-rabinowitch-lewin`）：1918至1921年的全面国有化、余粮收集制、取缔私商、劳动军事化，以及多党苏维埃收为一党专政，究竟是内战与供给崩溃逼出的生存应急，还是反市场乌托邦的激进兑现，抑或一战以来国家统制与基层危机交互的结果？“战时共产主义”是1921年转向时的事后标签，须分清措施序列与事后总结。
- **`DEB-1921-kronstadt-and-nep-origins`**（喀琅施塔得起义与新经济政策的双轨转折 | `historiography/debates/DEB-1921-kronstadt-and-nep-origins.md` | 流派 `social-history, political-institutional, provincial-and-state-society, soviet-orthodox`）：喀琅施塔得是白卫阴谋、农民反抗，还是要求重建劳动者苏维埃民主的革命者起义？1921年实物税与禁止党内派别同期出现，如何解释经济退却和政治收紧的联系、彼此差异及长期后果？
- **`DEB-1921-trade-union-controversy-and-party-unity`**（1921年工会争论、工人反对派与党内统一之争 | `historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md` | 流派 `lenin-ten, trotsky-militarization, workers-opposition, party-institutional-history, labor-social-history, industrial-paternalism`）：内战结束之际，工会应成为国家管理生产的传动机构，还是维护工人利益并参与管理的独立空间？工人反对派、托洛茨基和列宁的方案分歧，如何与第十次党代表大会禁止派别相互交织？喀琅施塔得危机既是决议援引的背景，也是有待独立考察的社会抗议，不能混同党内派别。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/28 条)
- **`CLM-carr-1952-nep-retreat-and-commanding-heights`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 118-166 (Chs. 18–20)]: 
- **`CLM-daniels-1960-tenth-congress-turning-point`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 146-153]: Daniels：1921年十大将党统一转化为压缩合法反对空间的组织制度
- **`CLM-avrich-1970-white-plot-refutation`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 143-147, 816-818]: 
- **`CLM-avrich-1970-sailor-social-composition`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 101-105]: 
- **`CLM-avrich-1970-soviets-without-bolsheviks`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 198-201, 179-180]: 
- **`CLM-figes-1996-peasant-wars-and-nep-retreat`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 775-785]: 
- **`CLM-raleigh-2001-center-periphery-weak-state-nep`** [`SCH-raleigh-donald`(唐纳德·J·罗利) | Local PDF pp. 16–18, 139–173; English print pagination not verified]: 
- **`CLM-service-2009-trotsky-authoritarian-consensus`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本第 23–24、28–29、37 章及引言]: 
- **`CLM-dugarm-2001-tambov-grain-warfare-and-antonovshchina`** [`SCH-raleigh-donald`(唐纳德·J·罗利) | Local PDF pp. 103–138; English print pagination not verified]: 
- **`CLM-carr-1952-war-communism-internal-contradictions`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 70-120 (Chs. 17–18)]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 56–58, 69, 185–188, 217–218, 283–284]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-smith-sa-1983-from-workers-control-to-nationalization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 155–156, 166–169, 177–179, 184–186, 192（即源文件标注 PDF pp. 160–161, 171–174, 182–184, 189–191, 197）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-daniels-1960-left-communists-1918`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 70-81]: Daniels：1918年左翼捍卫革命纲领，却在分裂关头受党统一约束
- **`CLM-zemskov-1929-dekulakization-demographic-baseline`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | PDF pp. 6-11, 15-19, 52, 218 (原书 pp. 4-9, 13-17, 50, 216)]: 
- **`CLM-siegelbaum-1992-nep-fragile-social-compromise`** [`SCH-siegelbaum-lewis`(刘易斯·H·西格尔鲍姆) | pp. 84, 91-93, 102-117, 136-144, 180-186 (PDF pp. 98, 105-107, 116-131, 150-158, 194-200)]: 
- **`CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists`** [`SCH-kollontai-alexandra`(亚历山德拉·柯伦泰 · participant-primary-text) | PDF pp. 2-11, 22-27]: 
- **`CLM-kollontai-1921-all-russian-congress-of-producers-program`** [`SCH-kollontai-alexandra`(亚历山德拉·柯伦泰 · participant-primary-text) | PDF pp. 11-21, 25-30]: 
- **`CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions`** [`SCH-godson-joseph`(约瑟夫·戈德森 · cold-war-labor-studies) | Book pp. 106–111, 121, 128–129 [PDF pp. 118–123, 133, 140–141]]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 5 条，另有 16 条 L3 逐日细节见 `timeline/L3_daily/`)
- **1921-02-28 [N.S.]** (`TL-W3-1921-02-28`, L2): **彼得罗巴甫洛夫斯克号通过决议** — 2月26日水兵代表自彼得格勒返回。2月28日舰上会议通过决议，要求无记名改选苏维埃，并在选举前给予全体工人和农民鼓动自由。3月1日群众大会确认。这是公历，不是俄历。
- **1921-03-02 [N.S.]** (`TL-W15-L1-E08-01`, L1): **喀琅施塔得临时革命委员会成立** — 水兵和居民提出苏维埃、经济与公民权利诉求，政权判其为反革命叛乱。
- **1921-03-02 [N.S.]** (`TL-W3-1921-03-02`, L2): **喀琅施塔得公开反叛，成立临时革命委员会** — 丹尼尔斯写公开反叛于3月2日爆发，官方公报称之为法国白卫军预谋。临时革命委员会是这一天的机构，不是3月1日大会。
- **1921-03-08 [N.S.]** (`TL-W3-1921-03-08-assault`, L2): **对喀琅施塔得的初次强攻** — 阿夫里奇写布尔什维克于3月8日发动初次进攻，水兵同一天提出第三次革命。第五章3月16日的 final blow 是英苏贸易协定，不是要塞陷落。
- **1921-03-18 [N.S.]** (`TL-W3-1921-03-18`, L2): **政府军控制喀琅施塔得要塞** — 3月17日晚革命委员会主要成员撤往芬兰。3月18日凌晨军校学员占领两艘主力舰，中午要塞、舰船和几乎全城已被控制，下午最后抵抗停止。约8000人退入芬兰。与事件卡 end_ns 一致。
