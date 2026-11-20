# 1-Hop 去重平衡上下文包：`POL-brest-litovsk-treaty`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`POL-brest-litovsk-treaty`** (布列斯特-立陶夫斯克和约 | `cards/policies/POL-brest-litovsk-treaty.md` | `multi-perspective`): 已覆盖=`lenin-pragmatic, left-communist, trotsky-diplomatic, daniels-organizational, rabinowitch-archival, dzerzhinsky-party-unity`；待补=`treaty-original-clause-comparison, regional-consequences`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 150字定性微摘要
布列斯特和约路线是在军事崩溃与世界革命期待之间作出的单独媾和选择。列宁主张割地换取喘息，布哈林主张革命战争，托洛茨基“不战不和”随德军进逼破产。1918年3月签约虽保住苏维埃政权，却造成重大领土与工业损失，引发党内激烈分裂并推动左派社革党退出联合政府。

## [T2] 革命外交路线与争鸣
### 2.1 决策投票链、代价与后果
- **三种路线与改历前后的决策升级**：本卡聚焦外交路线、投票链与制度后果，具体谈判经过见 `EVT-1918-03-brest-litovsk-treaty`。`1917-12-02 [O.S.] / 1917-12-15 [N.S.]` 停战后，列宁判断旧军已失去作战能力，主张立即签和换取“喘息时机”（передышка）；布哈林与左派共产主义者呼吁开展国际革命战争；托洛茨基折衷提出退出战争而不签约。`1918-01-08 [O.S.] / 1918-01-21 [N.S.]` 约 63 名中央与地方干部扩大会议非正式表决中，革命战争获 **32** 票、不战不和 **16** 票、立即签和仅 **15** 票（`DATA-04-party-membership-and-congress-votes-1903-1929`）。**`1918-01-28 [O.S.] / 1918-02-10 [N.S.]`**（尚早于苏俄 2 月 14 日改历 4 天），托洛茨基宣布“不战不和”，德军旋于 `1918-02-18`（改历后纯公历）恢复全线进攻。
- **表决逆转与签约**：`1918-02-18/19` 夜间中央委员会表决中托洛茨基转投赞成，以 **7:5:1** 决定重开和谈；德方提出更严苛最后通牒后，**`1918-02-23`** 中央委员会在列宁以辞职发出最后通牒下，由托洛茨基、捷尔任斯基等 4 人投下决定性弃权票（捷尔任斯基声明党团统一高于路线分歧，`RN-W22-lenin-formative-decisions-and-dzerzhinsky-cheka-to-vsnkh`），以 **7 赞成、4 反对、4 弃权** 接受条件；次晨全俄中执委以 **116:85:26** 通过（`DATA-04-party-membership-and-congress-votes-1903-1929`）。`1918-03-03` 正式签约：俄国放弃对波兰、波罗的海地区与芬兰的主张，承认乌克兰独立并撤军；各地区法律地位、德军占领与后续边界变动并非单一过程。
- **代表大会批准与联盟破裂**：`1918-03-06—08` 俄共（布）七大批准和约（速记版本差异见 `[T3]`）；`1918-03-14—16` 第四次全俄苏维埃非常代表大会以 **784:261:115** 正式批准条约。左派社会革命党（`ORG-left-srs`）投反对票并退出人民委员会，联合政府实质破裂，分歧随后因农村征粮与七月危机进一步演变为武装决裂。德国十一月革命与战败后，全俄中执委于 `1918-11-13` 宣布废约，但西部领土与边界问题并未随之自动解决。

### 2.2 核心关系网络（结构化边表）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `EVT-1918-03-brest-litovsk-treaty` | 事件载体 | 1917.12–1918.11 | 完整记录谈判停战、德军二月进攻与签约废约全过程。 | `CLM-rabinowitch-2007-left-sr-coalition-collapse` |
| `MTG-1917-10-2nd-congress-of-soviets` | 政策源头 | 1917-10-26 [O.S.] / 11-08 [N.S.] | 《和平法令》开启退出一战外交议程并埋下单独媾和伏笔。 | `CLM-rabinowitch-2007-contingency-of-dictatorship` |
| `PER-lenin` | 主和首席推手 | 1918.01–03 | 以辞职威胁压服党内反对派，以“喘息时机”换取政权生存。 | `CLM-daniels-1960-left-communists-1918` |
| `PER-bukharin` | 革命战争反对派 | 1918.01–03 | 领导左派共产主义者反对单独媾和，并在《共产党人》批列宁妥协。 | `CLM-daniels-1960-left-communists-1918` |
| `ORG-left-communists-1918` | 党内最大反对派 | 1918.01–05 | 因反和约及反国家资本主义形成1918年春党内组织性挑战。 | `CLM-daniels-1960-left-communists-1918` |
| `PER-trotsky` | 折衷外交执行者 | 1918.01–02 | 提出“不战不和”，2月18日后改投赞成并在2月23日关键弃权。 | `DATA-04-party-membership-and-congress-votes-1903-1929` |
| `PER-dzerzhinsky` | 弃权留任关键者 | 1918.02–06 | 虽强烈反对和约却以“党团统一”为重在2月23日弃权并留任契卡。 | `RN-W22-lenin-formative-decisions-and-dzerzhinsky-cheka-to-vsnkh` |
| `ORG-left-srs` | 联合政府决裂方 | 1918.03–07 | 反对和约退出人民委员会，7月起义刺杀米尔巴赫彻底破裂。 | `CLM-rabinowitch-2007-left-sr-coalition-collapse` |
| `INS-sovnarkom-and-vtsik` | 国家批准与废约主体 | 1918.02–11 | 中执委2月表决、四次苏维埃大会批准并于11月13日宣布废约。 | `CLM-rabinowitch-2007-left-sr-coalition-collapse` |
| `CON-state-capitalism` | 内部经济姊妹路线 | 1918.03–05 | 列宁在和约后提出“国家资本主义”喘息建设，同遭左派共产主义批判。 | `DEB-1918-war-communism-ideology-or-emergency` |
| `EVT-1918-1920-russian-civil-war` | 历史后果环境 | 1918–1920 | 签约释放内战空间同时触发协约国干涉与东线捷克军团冲突。 | `DEB-1918-red-terror-and-civil-war-origins` |
| `DEB-1918-war-communism-ideology-or-emergency` | 核心争鸣 | 1918 | 和约“喘息时机”及国家资本主义论战构成战时共产主义前夜起点。 | `CLM-daniels-1960-left-communists-1918` |
| `DEB-1918-red-terror-and-civil-war-origins` | 关联争鸣 | 1918 | 联合政府解体与内战全面爆发如何重塑苏维埃镇压体制。 | `CLM-rabinowitch-2007-left-sr-coalition-collapse` |

### 2.3 史学争鸣
- **党内派别分裂 vs. 联合政体偶发破裂**：R. V. Daniels（1960）重建三条路线与中央表决变化，强调列宁的胜利仰赖德军进逼压力与关键弃权（`CLM-daniels-1960-left-communists-1918`）；Alexander Rabinowitch（2007）依托彼得格勒档案揭示基层工人对签约与退约的复杂反应、左派社革党退出人民委员会的过程及一党专政定型的高度偶然性（`CLM-rabinowitch-2007-left-sr-coalition-collapse`、`CLM-rabinowitch-2007-contingency-of-dictatorship`）。
- **党团统一的政治优先性**：拉特科夫斯基《捷尔任斯基传》档案精读（`RN-W22-lenin-formative-decisions-and-dzerzhinsky-cheka-to-vsnkh`）补充了左派内部的关键分化——不同于退出中央岗位的布哈林派或退阁的左派社革党，捷尔任斯基选择弃权留任契卡，以防止布尔什维克党分裂为最高原则。列宁 1918 年 5 月《论“左派”幼稚性和小资产阶级性》则属于为和约与国家资本主义辩护的一手论战文本，不可当作对其对手的中立定论；和约是否是唯一可行出路亦仍属反事实争论。

## 2. 一跳邻域全量微摘要目录 (去重后共 15 个节点，0 截断)
- **`CON-revolutionary-defensism-and-defeatism`**（革命护国主义与革命失败主义）: 1914–1918年社会主义者的战争路线分歧：普列汉诺夫护国、马尔托夫主张国际主义和平，列宁倡本国政府战败与变外战为内战。1917年策烈铁里主导“革命护国主义”，遭四月照会与六月攻势削弱；1918年布列斯特危机又分出左派“革命战争”与列宁“喘息和约”。 ‖ `→POL-brest-litovsk-treaty`[realpolitik-outcome|1918-03-03–1918-11-13]: 以丧失大片西部边疆换取苏维埃政权存续，标志国家生存逻辑压倒早期革命战争口号
- **`CON-state-capitalism`**（国家资本主义（苏维埃政权下的））: 布尔什维克过渡经济概念。列宁1917–1918年以德国战时统制经济为蓝本，将“苏维埃政权下的国家资本主义”定为通向社会主义的进步阶梯，遭左派共产主义者斥为向资本投降；1921年重定义为租让制、租赁与合作社，1923年《论合作社》悄然转向；1925年新反对派反用此词攻击布哈林—斯大林。 ‖ `→POL-brest-litovsk-treaty`[external-twin-of-internal-retreat|1918-03–1918-05]: 对外“喘息”与对内国家资本主义构成同一退让战略的两面，同遭左派共产主义者反对 ； `←POL-brest-litovsk-treaty`[内部经济姊妹路线|1918.03–05]: 列宁在和约后提出“国家资本主义”喘息建设，同遭左派共产主义批判。
- **`EVT-1917-1920-ukrainian-revolution-rada-hetmanate-and-sovietization`**（乌克兰革命：中央拉达、盖特曼政权、执政内阁与苏维埃化（1917—1920））: 1917—1920年乌克兰多政权角逐与苏维埃化进程。中央拉达、德扶盖特曼政权、执政内阁与苏维埃政权交替据守基辅。1918年首轮苏维埃政权迫于德奥军推进撤离，1919年次轮因征粮、国营农场与俄化作风激发农村起义及白军攻势而溃败；1919年底列宁调向并吸纳斗争派，1920年底缔结俄乌盟约。 ‖ `→POL-brest-litovsk-treaty`[german-occupation-framework|1918.02–1918.11]: 1918年2月拉达单独缔和并求援引致德奥军推进，直接迫使首轮苏维埃政权于3月2日撤离基辅
- **`EVT-1918-03-brest-litovsk-treaty`**（1918年布列斯特-里托夫斯克和约危机与签约）: 1917年12月停战至1918年3月签约，列宁主和、托洛茨基“不战不和”与布哈林革命战争路线交锋。德军进逼后，中央2月23日以7赞成、4反对、4弃权接受最后通牒；和约保存政权，也加深党内裂痕并促使左翼社革党退阁。 ‖ `→POL-brest-litovsk-treaty`[treaty_policy_counterpart|1918-03至11 [N.S.]]: 条款、批准与废止的政策对应物，须与本事件决策链互校。 ； `←POL-brest-litovsk-treaty`[事件载体|1917.12–1918.11]: 完整记录谈判停战、德军二月进攻与签约废约全过程。
- **`EVT-1918-1921-transcaucasian-republics-baku-commune-and-sovietization`**（外高加索独立共和国、巴库公社与苏维埃化（1918—1921））: 1918—1921年外高加索独立建国与苏维埃化进程。布列斯特割地与俄土前线瓦解后，巴库公社兴亡，外高加索联邦解体为格、阿、亚三国并陷领土冲突。红军击败邓尼金后，高加索局配合红十一军团与苏土外交契机于1920—1921年苏维埃化三国，铁路整合与集权体制随即牵动1922年建盟与格鲁吉亚危机。 ‖ `→POL-brest-litovsk-treaty`[territorial-severance-trigger|1918.03–1918.06]: 未经外高加索同意割让巴统、卡尔斯予土耳其，直接迫使TDFR宣布独立并引发土军入侵与联邦解体
- **`INS-sovnarkom-and-vtsik`**（人民委员会与全俄、全苏中央执行委员会）: 苏维埃代表大会闭会期间，中执委在宪制上监督政府，人民委员会却迅速掌握施政与大量法令制定。苏俄与1922年成立的苏联各有中执委与人民委员会，不能混同。党内领导与国家机关关系不断变化，政治局权重日增，但1920年代仍须经政府落实决策。 ‖ `→POL-brest-litovsk-treaty`[coalition_exit_trigger|1918.03]: 左翼社革党退出政府 ； `←POL-brest-litovsk-treaty`[国家批准与废约主体|1918.02–11]: 中执委2月表决、四次苏维埃大会批准并于11月13日宣布废约。
- **`MTG-1917-10-2nd-congress-of-soviets`**（第二届全俄工兵代表苏维埃代表大会）: 1917-10-25至10-27[O.S.]/11-07至11-09[N.S.]，全俄苏维埃二大在斯莫尔尼召开。孟什维克、右翼社革党退场，左派社革党留场；大会宣告苏维埃掌权，通过和平、土地法令，成立列宁领导的纯布尔什维克政府及加米涅夫任主席的中执委，合法性与联合政府之争公开化。 ‖ `→POL-brest-litovsk-treaty`[policy-prefigured|1917-10-26 [O.S.] / 11-08 [N.S.]起]: 《和平法令》确立公开外交与退出世界大战原则，1918年3月布列斯特和约则在极端不利条件下被迫有偿割地停战 ； `←POL-brest-litovsk-treaty`[政策源头|1917-10-26 [O.S.] / 11-08 [N.S.]]: 《和平法令》开启退出一战外交议程并埋下单独媾和伏笔。
- **`MTG-1918-03-7th-party-congress`**（俄国共产党（布尔什维克）第七次紧急代表大会）: 1918年3月6—8日（纯公历），俄共（布）七大在法定人数不足下强行召开。列宁“喘息和约”与布哈林“左派共产主义者”革命战争路线激辩12小时后，大会以30∶12∶4（初计28∶9∶1）批准《布列斯特和约》，改党名为俄共（布）并设党纲起草委员会。 ‖ `→POL-brest-litovsk-treaty`[ratified_within_party|1918-03-06..08]: 大会在法定人数不足下经12小时激辩以30∶12∶4（初计28∶9∶1）批准和约，为苏维埃四大奠定党团约束。
- **`ORG-left-communists-1918`**（1918年左翼共产主义者）: 1918年初俄共（布）内以布哈林、奥新斯基、拉狄克、普列奥布拉任斯基为首的极左集团，借《共产党人》（`Коммунист`）杂志反对《布列斯特和约》与列宁“国家资本主义”一长制；俄共七大批准和约后作为有组织派别逐步消解，但其国际主义与反官僚化诉求深刻塑造此后党内反对派谱系。 ‖ `→POL-brest-litovsk-treaty`[opposed|1918.01–03]: 视德国强加《布列斯特和约》为损害世界革命与苏维埃政权阶级实质的致命妥协 ； `←POL-brest-litovsk-treaty`[党内最大反对派|1918.01–05]: 因反和约及反国家资本主义形成1918年春党内组织性挑战。
- **`ORG-left-srs`**（左翼社会革命党）: 1917年底从社会革命党分裂出的激进民粹派政党（1917–1923），以斯皮里多诺娃、普罗相等为首。拥护苏维埃政权并于1917年12月加入人民委员会与布尔什维克联合执政；1918年3月因反《布列斯特和约》退阁但仍维持北方公社合作，7月6日刺杀德国大使米尔巴赫遭全面清洗而覆灭。 ‖ `→POL-brest-litovsk-treaty`[fierce-opponent-and-resignation-trigger|1918.02–1918.07]: 痛斥割地和约为向德国帝国主义投降并背叛国际革命，3月15日为抗议和约批准集体辞去中央人民委员职务，7月6日更借刺杀德国大使企图撕毁和约 ； `←POL-brest-litovsk-treaty`[联合政府决裂方|1918.03–07]: 反对和约退出人民委员会，7月起义刺杀米尔巴赫彻底破裂。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←POL-brest-litovsk-treaty`[主和首席推手|1918.01–03]: 以辞职威胁压服党内反对派，以“喘息时机”换取政权生存。 ； `→POL-brest-litovsk-treaty`[chief-proponent|1918-01至03]: 以辞职相威胁力排布哈林“左翼共产主义者”与托洛茨基“不战不和”方案，强行签订割地和约换取政权喘息空间。
- **`PER-bukharin`**（尼古拉·布哈林）: 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。 ‖ `←POL-brest-litovsk-treaty`[革命战争反对派|1918.01–03]: 领导左派共产主义者反对单独媾和，并在《共产党人》批列宁妥协。 ； `→POL-brest-litovsk-treaty`[left-communist-opponent|1918-01至03]: 领衔党内“左翼共产主义者”激烈反对对德妥协签约，主张开展革命游击战争推动欧洲革命。
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←POL-brest-litovsk-treaty`[折衷外交执行者|1918.01–02]: 提出“不战不和”，2月18日后改投赞成并在2月23日关键弃权。
- **`PER-dzerzhinsky`**（费利克斯·捷尔任斯基）: 波兰立陶宛社民党与布尔什维克领导人。1917年建全俄肃反委员会（契卡）并续掌GPU/OGPU至逝世，奠定苏维埃安全与法外镇压体制；1924–1926年兼任最高国民经济委员会主席，力挺新经济政策市场均衡、保护技术专家并反对超工业化，1926年7月预警“红色独裁者”后猝逝于中央全会。 ‖ `←POL-brest-litovsk-treaty`[弃权留任关键者|1918.02–06]: 虽强烈反对和约却以“党团统一”为重在2月23日弃权并留任契卡。
- **`EVT-1918-1920-russian-civil-war`**（俄国内战（1918–1920））: 1918至1920年红白主战场的内战中，布尔什维克依托中央腹地、军火遗产与铁路机动击败分散白军；征粮和恐怖又激起工农反抗。乌克兰及外高加索的民族国家竞争不能归入简单红白对决，克里米亚撤离仅标志主要白军战线收束，边疆与农民战争仍在延续。 ‖ `←POL-brest-litovsk-treaty`[历史后果环境|1918–1920]: 签约释放内战空间同时触发协约国干涉与东线捷克军团冲突。 ； `→POL-brest-litovsk-treaty`[context|1918]: 和约边界划定苏维埃初期战略纵深

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 2 项)
### `DEB-1918-war-communism-ideology-or-emergency`：战时共产主义与早期一党制本质之争：内战应急、乌托邦跃进还是国家统制连续？
## [T1] 核心问题定义
1918至1921年的全面国有化、余粮收集制、取缔私商、劳动军事化，以及多党苏维埃收为一党专政，究竟是内战与供给崩溃逼出的生存应急，还是反市场乌托邦的激进兑现，抑或一战以来国家统制与基层危机交互的结果？“战时共产主义”是1921年转向时的事后标签，须分清措施序列与事后总结。

## [T2] 各学派立场对照矩阵

**经验共识**：1917年底至1918年春尚存布尔什维克—左翼社革党联合执政与“国家资本主义”探索；1918年夏起全面国有化与强制征粮随内战升级扩展；1920年达至劳动军事化与无货币幻想顶峰；1921年3月俄共十大在农村起义与喀琅施塔得危机下转向实物税（NEP）与党内派别禁令。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **内战军事应急与双元矛盾论** | E. H. Carr, *The Bolshevik Revolution*, Vol. 2 (1952); Evan Mawdsley, *The Russian Civil War* (1987) | 强调工业瓦解、封锁与300万红军补给迫使政权诉诸垂直“总局主义”与强制征粮；但Carr同时指出1920年后期确曾滋生把战时自然经济奉为直接通往共产主义捷径的意识形态幻象。 | `CLM-carr-1952-war-communism-internal-contradictions`; `CLM-mawdsley-1987-civil-war-militarized-regime`; `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` | 单靠军事紧急状态难以完全解释1920年底内战大局已定后为何仍出台小手工业全面国有化令。 |
| **意识形态乌托邦与废法专政论** | Martin Malia, *The Soviet Tragedy* (1994); Richard Pipes, *The Russian Revolution* (1990) | 认为消灭私有产权与市场交换本就是马克思主义核心诉求，内战只是扫除了渐进障碍、催化乌托邦跃进；Pipes强调契卡与排斥反对派早于大规模内战爆发。 | `CLM-pipes-1990-red-terror-leninist-logic`; `CLM-pipes-1990-october-classic-coup` | 易将不同阶段的应急妥协（如1918春列宁国家资本主义方案）回溯拉平为单一既定时间表。 |
| **战时国家统制连续与自下而上倒逼论** | Lars T. Lih; S. A. Smith, *Red Petrograd* (1983); David Hoffmann (2011) | 揭示沙皇与临时政府在一战中已启动粮食专卖与国家统制；Smith证明1917–1918春77%早期企业没收源自基层工厂委员会应对关厂危机的自下而上压力，而非中央乌托邦指令。 | `CLM-smith-sa-1983-defensive-workers-control`; `CLM-smith-sa-1983-from-workers-control-to-nationalization`; `CLM-hoffmann-2011-continuum-of-total-war-1914-1929` | 总体战技术连续性不能替代对布尔什维克消灭整个有产阶级政治权利之独特意识形态动力的解释。 |
| **复合危机、党内张力与农村社会钳制论** | Alexander Rabinowitch (2007); Robert V. Daniels (1960); Moshe Lewin (1968/1985) | 追踪布列斯特和约、左翼社革党决裂及左翼共产主义者/工人反对派论战如何一步步锁死多党与党内多元空间，同时揭示小农汪洋的反抗最终迫使政权在1921年退却但保留了战时强制记忆。 | `CLM-rabinowitch-2007-contingency-of-dictatorship`; `CLM-daniels-1960-left-communists-1918`; `CLM-figes-1996-peasant-wars-and-nep-retreat`; `CLM-zemskov-1929-dekulakization-demographic-baseline` | 首都与萨拉托夫、坦波夫、乌拉尔等外省的时间差与暴力烈度须结合地方档案（Raleigh、Churakov）细化。 |

### `DEB-1918-red-terror-and-civil-war-origins`：红色恐怖、契卡扩张与内战期一党专政起源之争（1918–1921）
## [T1] 核心问题定义
红色恐怖和契卡法外权力是列宁主义政治逻辑的必然结果，还是内战、粮食危机、联盟破裂与地方暴力交织下的制度选择？中央命令与地方自主行动怎样互相强化？恐怖升级、社会主义对手遭镇压和一党统治形成各有不同时间线，不能压缩成同一事件。

## [T2] 各学派立场对照矩阵
**经验基准**：全俄肃反委员会（契卡）于1917-12-07 [O.S.] / 1917-12-20 [N.S.] 凭人民委员会非立法决议成立；1918年3月《布列斯特和约》后左翼社革党退出人民委员会，7月4–10日第五次全俄苏维埃代表大会期间爆发7月6日刺杀德国大使米尔巴赫事件，布尔什维克与左翼社革党彻底决裂并于7月10日通过1918年苏俄宪法；8月30日乌里茨基遇刺、列宁遇刺重伤。据站内入库S级档案校勘（`sources/web-archive/E06_E09_state_and_comintern/1918-09-05_decree-on-red-terror.md`），广泛扣押人质指令首先出自9月4日内务人民委员彼得罗夫斯基电令，而9月5日人民委员会《关于红色恐怖的决议》（RGASPI打印原件由司法人民委员库尔斯基、内务人民委员彼得罗夫斯基、办公厅主任邦奇-布鲁耶维奇与秘书福季耶娃签署，**并非捷尔任斯基签署，且9月5日决议正文中并未出现“人质”一词**）将集中营隔离与就地枪决正式法制化。跨口径处决统计（`DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge`）须严格区分中央登记案卷与地方未登记法外处决。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 自由主义意识形态连续论 | Richard Pipes, *The Russian Revolution* (1990) | 提出“法国大革命终结于恐怖，而俄国革命始于恐怖”：布尔什维克因缺乏多数民众授权，将系统性恐怖用作“民众支持的替代品”，阶级敌人话语与列宁的雅各宾法律观使红色恐怖成为十月少数派政变的必然逻辑延伸。 | `CLM-pipes-1990-red-terror-leninist-logic` | 将1918年夏内战升级与暗杀危机前后的制度突变全部还原为先验意识形态蓝图，低估了战时生存危机与基层压力。 |
| 契卡制度史与法外基因论 | George Leggett, *The Cheka: Lenin's Political Police* (1981) | 追踪契卡从1917年12月仅具侦查权、凭人民委员会行政决议（类比沙皇尼古拉一世第三厅）建置，在1918年春夏突破司法人民委员部（斯泰因伯格）制约、借9月红色恐怖法令将法外处决权制度化，直至1922年改组为GPU并由列宁5月致库尔斯基密信将恐怖写入刑法典的制度连续性（估算1917–1922年契卡直接处决约14万人、镇压起义另致约14万人死亡）。 | `CLM-leggett-1981-vecheka-extra-legal-origins`；`CLM-leggett-1981-red-terror-institutionalization`；`CLM-leggett-1981-cheka-to-gpu-continuity` | 1981年尚未能利用后苏联解密的FSB中央与地方卷宗，其高层估算数字需与莫佐欣、泽姆斯科夫档案统计对勘。 |
| 联盟破裂、党组织萎缩与专政偶然论 | Alexander Rabinowitch, *The Bolsheviks in Power: The First Year of Soviet Rule in Petrograd* (2007) | 论证一党专政与大规模恐怖并非十月既定方案：1918年春彼得格勒布尔什维克党员从约5万人骤降至约6,000人，为保住苏维埃五大多数竟伪造约399席代表资格；左翼社革党7月刺杀米尔巴赫旨在逼停布列斯特和约而非推翻苏维埃（**1918年12月彼得格勒契卡甚至秘密撤销了对左翼社革党“有组织武装起义”的指控**）；8月30日乌里茨基遇刺后，彼得格勒各区委“自下而上”施压扩大报复，与中央危机共振催生红色恐怖。 | `CLM-rabinowitch-2007-contingency-of-dictatorship`；`CLM-rabinowitch-2007-left-sr-coalition-collapse` | 彼得格勒在季诺维也夫与乌里茨基初期相对克制及随后失控的个案，不能直接代表伏尔加河或南方前线各省的暴力烈度。 |
| 地方庇护网络、红色恐怖编年史与捷尔任斯基机构化 | Delano Dugarm (2001，收入 Donald J. Raleigh 编 *Provincial Landscapes*)；Igor Ratkovsky (伊·谢·拉特科夫斯基 2017两部专著，依托 A. M. & A. A. Plekhanov 2007 档案集) | Dugarm以坦波夫省个案揭示地方布尔什维克宗派庇护网、溃兵与契卡自主滥权常偏离莫斯科指令，甚至以“虚构暴动”掩盖征粮失败；圣彼得堡国立大学史家拉特科夫斯基（2017《契卡红色恐怖编年史》与《捷尔任斯基传》）依托普列汉诺夫父子2007年档案集，重构人质制度、地方契卡对孟什维克与社革党的压制、1918年秋约8,000人处决估算，以及捷尔任斯基如何将分散的革命暴力收编为垂直集权的契卡—内务—最高国民经济委员会官僚机器。 | `CLM-raleigh-2001-local-bolshevik-violence-and-clientelism`；`CLM-cheka-chronicle-hostage-and-local-autonomy`；`CLM-cheka-chronicle-suppression-of-socialist-rivals`；`CLM-plekhanov-am-dzerzhinsky-cheka-institutionalization` | 地方报刊编年史与契卡内部通报存在漏报或战绩夸大双向偏差，须与独立受害者名册及省级法院档案交叉核验。 |
| 被镇压社会主义对手、第三势力崩溃与1918年工人抗议 | [S级当事人演说] L. Martov (1920年10月哈勒大会演说)；Oliver H. Radkey, *The Sickle under the Hammer* (1963)；D. O. Churakov (丘拉科夫, 2004) | 马尔托夫在1920年德国独立社民党哈勒大会上痛斥无差别红色恐怖（如彼得格勒一次处决约800人）与“二十一条”如何摧毁社会主义道德与苏维埃民主；Radkey剖析社革党与科穆奇（Komuch）“民主第三势力”因内部分裂及白军借其作“保护色”而崩溃，将政局推入红白恐怖两极；丘拉科夫以档案证明1918年苏维埃辖区210–220家大中型企业爆发10–25万工人罢工抗议，直至8月伊热夫斯克—沃特金斯克武装工人起义，直接证伪“镇压对象仅限于资产阶级和地主”的官方叙事。 | `CLM-halle-1920-martov-critique-of-terror-and-21-conditions`；`CLM-smith-scott-2011-psr-third-force-collapse`；`CLM-churakov-2004-soviet-worker-protest-dynamics-1918`；`CLM-churakov-2004-izhevsk-votkinsk-worker-insurrection` | 反对派控诉与工人起义证明了恐怖对劳动阶级自身的反噬，但对白军战区白色恐怖与外国干涉的对称比较需另行展开。 |
| 内战军事化结构与总体战现代治理 | Evan Mawdsley, *The Russian Civil War* (1987); David L. Hoffmann, *Cultivating the Masses* (2011) | Mawdsley从军事地理与政权生存结构出发，指出内战与政治高度军事化均是十月夺权方式的直接代价（“内战代价即革命代价”）；Hoffmann将契卡监控、集中营与粮食强制置于1914年一战以来欧洲列强总体战人口治理与国家暴力技术的连续谱中。 | `CLM-mawdsley-1987-civil-war-militarized-regime`；`CLM-hoffmann-2011-continuum-of-total-war-1914-1929` | 欧洲总体战技术共性或军事地理决定论，不能消解布尔什维克在1921年内战结束后仍保留并制度化法外警察权力的政治选择责任。 |
| 后苏联FSB/GARF档案定量校准与莫佐欣“战时/和平期二分法” | O. B. Mozokhin (莫佐欣, 2006/2016)；V. N. Zemskov (泽姆斯科夫, 2010s) | 莫佐欣据俄罗斯联邦安全局中央档案馆（ЦА ФСБ РФ）统计表（`DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge`），确认1918–1921年有案可查契卡处决约1.75万人（计入缺省全期上限不超过5万），并提出鲜明的**国家主义二分法**——肯定1918–1921年战时契卡镇压武装叛乱的应急必要性，却**尖锐批判1922年后和平时期GPU/OGPU继续垄断法外司法**（如1924年4,097起反革命案仅6起移交法院，战时死刑率6.9% vs 和平期0.5%/0.94%）；泽姆斯科夫据GARF档案校准1918–1920年登记反革命案判刑62,231人、处决25,709人（含未登记上限<10万），共同驳斥百万级夸大数字。 | `CLM-mozokhin-cheka-to-ogpu-extrajudicial-jurisdiction-1918-1929`；`CLM-zemskov-1920s-archival-repression-scale-before-1930` | 中央汇总报表未涵盖1918–1920年前线红军革命军事法庭、征粮队及地方县契卡未上报的就地处决，档案下限不等于实际死亡总数。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/26 条)
- **`CLM-rabinowitch-2007-left-sr-coalition-collapse`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 274-282, 287-309, 395-396]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-daniels-1960-left-communists-1918`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 70-81]: Daniels：1918年左翼捍卫革命纲领，却在分裂关头受党统一约束
- **`CLM-carr-1952-war-communism-internal-contradictions`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 70-120 (Chs. 17–18)]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 56–58, 69, 185–188, 217–218, 283–284]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-smith-sa-1983-from-workers-control-to-nationalization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 155–156, 166–169, 177–179, 184–186, 192（即源文件标注 PDF pp. 160–161, 171–174, 182–184, 189–191, 197）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-figes-1996-peasant-wars-and-nep-retreat`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 775-785]: 
- **`CLM-zemskov-1929-dekulakization-demographic-baseline`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | PDF pp. 6-11, 15-19, 52, 218 (原书 pp. 4-9, 13-17, 50, 216)]: 
- **`CLM-leggett-1981-vecheka-extra-legal-origins`** [`SCH-leggett-george`(乔治·莱格特) | pp. 17-22, 47-49 (PDF pp. 55-60, 85-87)]: 
- **`CLM-leggett-1981-red-terror-institutionalization`** [`SCH-leggett-george`(乔治·莱格特) | pp. 56-59, 102-115, 144-145 (PDF pp. 94-97, 140-153, 182-183)]: 
- **`CLM-leggett-1981-cheka-to-gpu-continuity`** [`SCH-leggett-george`(乔治·莱格特) | pp. 339-352, 355-363 (PDF pp. 377-390, 393-401)]: 
- **`CLM-raleigh-2001-local-bolshevik-violence-and-clientelism`** [`SCH-raleigh-donald`(唐纳德·J·罗利) | Local PDF pp. 104, 112–130; English print pagination not verified]: 
- **`CLM-cheka-chronicle-hostage-and-local-autonomy`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | EPUB OPS/ch1-6.xhtml; OPS/ch1-10.xhtml; OPS/ch1-14.xhtml; OPS/ch1-15.xhtml; OPS/ch1-16.xhtml; OPS/ch1-19.xhtml（提取文本无印刷页码）]: 
- **`CLM-cheka-chronicle-suppression-of-socialist-rivals`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | EPUB OPS/ch1-4.xhtml; OPS/ch1-5.xhtml; OPS/ch1-9.xhtml; OPS/ch1-10.xhtml; OPS/ch1-15.xhtml; OPS/ch1-16.xhtml（提取文本无印刷页码）]: 
- **`CLM-plekhanov-am-dzerzhinsky-cheka-institutionalization`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | pp. 55-56, 97-106, 118-123, 147-155, 209-211, 228]: 
- **`CLM-halle-1920-martov-critique-of-terror-and-21-conditions`** [`SCH-martov-iulii`(尤利·奥西波维奇·马尔托夫 · participant-primary-text) | pp. 167–170, 173, 175–176, 179 (Lih translation in the 2011 Lewis/Lih edition; printed page = PDF page − 1). Full speech pp. 167–179, delivered 15 October 1920 [N.S.]]: 
- **`CLM-smith-scott-2011-psr-third-force-collapse`** [`SCH-radkey-oliver`(奥利弗·亨利·拉德基) | pp. 452-455, 467-473, 490-493 (PDF pp. 468-471, 483-489, 506-509)]: 
- **`CLM-churakov-2004-soviet-worker-protest-dynamics-1918`** [`SCH-churakov-dmitry`(德米特里·奥列戈维奇·丘拉科夫) | pp. 84-88, 352-355]: 
- **`CLM-churakov-2004-izhevsk-votkinsk-worker-insurrection`** [`SCH-churakov-dmitry`(德米特里·奥列戈维奇·丘拉科夫) | pp. 258-285, 290-298, 304-325]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 5 条，另有 12 条 L3 逐日细节见 `timeline/L3_daily/`)
- **1918-01-28 [O.S.] / 1918-02-10 [N.S.]** (`TL-W15-L1-E07-04`, L1): **布列斯特“不战不和”声明** — 托洛茨基拒绝签约并宣布退出战争，随后德军恢复攻势。
- **1918-01-28 [O.S.] / 1918-02-10 [N.S.]** (`TL-W3-1918-02-10`, L2): **托洛茨基拒绝在布列斯特签字并离开会场** — 俄历1月28日，公历2月10日。政策卡 POL-brest-litovsk-treaty 把拒绝签字的公历2月10日误标成俄历并配到2月23日，与本次核验相反，本条不沿用。反向命令 kb.py date 1918-02-10 --from ns 给出同一对日期。
- **1918-02-14 [N.S.]** (`TL-W15-L1-E07-05`, L1): **苏俄实行公历** — 俄历1月31日之后改称2月14日；此后苏俄官方日格以公历为准。
- **1918-03-03 [N.S.]** (`TL-W15-L1-E07-06`, L1): **签署布列斯特和约** — 苏俄接受严苛条件；左翼共产主义者与左翼社革党反对。
- **1918-03-03 [N.S.]** (`TL-W3-1918-03-03`, L2): **签署布列斯特-立陶夫斯克和约** — 公历3月3日签约。主账已有 TL-1918-03-03，date_os 为空，合并时并入该条，不补俄历。第七次党代表大会3月6–8日批准。政府3月10/11日迁莫斯科。第四次苏维埃代表大会拉宾诺维奇写3月15–16日，派普斯写3月14日。左翼社会革命党退出人民委员会，派普斯写3月14日，拉宾诺维奇写3月18日。布哈林领衔的左派共产主义者反对和约。
