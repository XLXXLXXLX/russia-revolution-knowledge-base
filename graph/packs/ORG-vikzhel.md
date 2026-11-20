# 1-Hop 去重平衡上下文包：`ORG-vikzhel`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`ORG-vikzhel`** (全俄铁路雇员与工人联合会执行委员会（维克热尔） | `cards/organizations/ORG-vikzhel.md` | `multi-perspective`): 已覆盖=`rabinowitch-contingency-thesis-via-CLM, moscow-social-history-koenker, menshevik-history-basil, carr-institutional-political-economy, pipes-power-concentration-via-CLM`；待补=`vikzhel-proceedings-original, railway-union-membership-and-vikzhedor-primary-records, revolutionary-left-structural-incompatibility-claim-cards`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
维克热尔是1917年夏产生的全国铁路工会执行机关。铁路连接军队、粮食与城市，十月革命后其运输杠杆使它试图调停各社会主义政党、推动广泛联合政府。布尔什维克内部为此严重分裂，谈判未能实现最广泛联合，新的铁路工会领导机关后与布党及左翼社革党合作。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **工会机关与运输杠杆**：1917年夏，全俄铁路职工工会形成全国执行委员会，成员政治倾向复杂。库内 L3 称其“由孟什维克与社革党主导”，右翼社革党与孟什维克在谈判中拒绝让步；Koenker 则记斡旋方含邮电工会、孟什维克、社革党等。左翼社革党在机关内的席次无库内出处，机关内各党派确切席次待核。铁路网络并非一台随时完全服从中央指令的机器。
- **十月起义与联合谈判**：彼得格勒起义主要节点为 `1917-10-25 [O.S.] / 1917-11-07 [N.S.]`。`1917-10-29 [O.S.] / 1917-11-11 [N.S.]` 维克热尔发出最后通牒，要求 10-30 午夜前启动清一色社会主义联合政府谈判，否则全国铁路总罢工，距起义四日而非次日（L3 `1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis`，#L54）。`11-02` 夜谈判中出现让出半数席位的方案，`11-03 [O.S.]` 梁赞诺夫赴维克热尔受阻、阿布拉莫维奇宣告“谈判已无意义”，列宁等十名中央多数派提出最后通牒。联合政府讨论中排除列宁与托洛茨基的要求是谈判条件，不是最终内阁方案。
- **党内分裂、表决与辞职**：加米涅夫、季诺维也夫、李可夫、米柳亭、诺金主张广泛联合。`1917-11-04 [O.S.] / 1917-11-17 [N.S.]` 中央委员会此五人宣布退出，部分人民委员另行辞职，两份名单不能画等号。同日中执委的几组表决，库内 L3 并列如下（各史源口径不一）：


| 议题 | 票数 | 备注 |
| :--- | :--- | :--- |
| 中执委确认人民委员会紧急立法权（乌里茨基决议） | `29:23:3` 通过；异文 `25:23` | L3 并列两种记录，`25:23` 为 Pipes 部分记录；两者是否为同一次表决的不同统计，库内未裁决 |
| 法令权相关表决（拉林出版法令动议） | `34:24`（1弃权）= `34:24:1` 否决 | L3 同时给出该口径 |
| 斯皮罗不信任动议 | `20:25`（12弃权）否决 | L3 |

  上列数字取自 L3 并列标注，本库不裁决 `29:23:3` 与 `25:23` 的差异，只并列呈现。辞职分母以 L3 所载“10名中央多数派联署对5名少数派中委”为准。

- **谈判流产与改组**：`11-05/06 [O.S.]` 谈判实际流产，季诺维也夫 `11-06/07` 认错。莫斯科方面停火在 L3 与 Koenker 间有 `11-02` / `11-03`（均 [O.S.]）异文，Koenker 记 `1917-10-28 [O.S.] / 1917-11-10 [N.S.]` 莫斯科调停停火，莫斯科停火与彼得格勒跨党派谈判不是同一会议。1917年12月布党与左翼社革党组成政府联盟，非维克热尔方案。1918年1月铁路工人代表会议产生接近布党的维克热多尔（Викжедор），削弱原执行委员会（Carr 将维克热多尔与1918年交通人民委员“独裁权力”法令连成一线，见 `RN-W23-carr-party-state-constitution-and-economic-order-1917-1923`）。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 关系实质 | 依据 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-bolsheviks-rcpb-vkpb` | `mediated-coalition-talks` | 1917.10–11 | 借铁路运输杠杆要求联合政府，并暴露布党内部严重分歧 | L3 `1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis`；`DEB-1917-all-socialist-coalition-vikzhel-missed-chance` |
| `ORG-mensheviks` | `negotiation-participant` | 1917 | 孟什维克内部对政府和抵抗方式并不一致，部分人参与调停 | `CLM-basil-1984-october-and-vikzhel-collapse`；`CLM-getzler-1967-martov-soviet-opposition` |
| `ORG-psr` | `negotiation-participant` | 1917 | 右翼社革党主导机关并拒绝让步，社革党分裂改变联盟可能 | L3 `1917-11_…`；`CLM-yao-hai-post-october-coalition-failure-and-one-party-formation` |
| `ORG-left-srs` | `coalition-partner-after-failure` | 1917.12–1918 | 谈判破裂后单独入阁，改变广泛联盟的可能性 | `CLM-rabinowitch-2007-left-sr-coalition-collapse` |
| `EVT-1917-10-october-revolution` | `post-insurrection-mediation` | 1917 | 起义后以罢工威胁促谈，莫斯科同时有停火斡旋 | `RN-W32-koenker-moscow-strikes-duma-votes-and-october-week` |
| `INS-sovnarkom-and-vtsik` | `legislative-power-dispute` | 1917-11 | 11-04 中执委表决人民委员会法令权 | L3 `1917-11_…` L102 |
| `PER-lenin` | `ultimatum-opponent` | 1917-11 | 反对排除自己与托洛茨基的联合方案，提出十人最后通牒 | L3 `1917-11_…` |
| `PER-kamenev` | `coalition-advocate` | 1917-11 | 布党内主张广泛联合的代表人物 | L3 `1917-11_…`；`PER-kamenev` 卡 |
| `PER-zinoviev` | `coalition-advocate-then-retreat` | 1917-11 | 辞职并于 11-06/07 认错 | L3 `1917-11_…` |
| `PER-rykov` | `coalition-advocate` | 1917-11 | 辞职者之一 | L3 `1917-11_…` |
| `PER-sverdlov` | `vtsik-chair` | 1917-11 | 11-08 [O.S.] 接任中执委主席 | L3 `1917-11_…` L126 |
| `PER-martov-l` | `negotiation-participant` | 1917-11 | 国际主义孟什维克，与谈判相关 | `CLM-getzler-1967-martov-soviet-opposition` |
| `PER-dan` | `negotiation-participant` | 1917-11 | 孟什维克领导人之一 | `PER-dan` 卡 |

### 2.3 史学争鸣光谱
库内辩题 `DEB-1917-all-socialist-coalition-vikzhel-missed-chance` 登记四派。Rabinowitch 强调早期社会主义多党政治的现实可能性及其在危机中受挫，布党内部并非一开始就有统一的一党专政计划（`CLM-rabinowitch-2007-left-sr-coalition-collapse`；`CLM-rabinowitch-2007-contingency-of-dictatorship`）。Pipes–Malia 一极强调意图与权力集中，把联合谈判视为列宁不愿分享权力的表现（`CLM-pipes-1990-october-classic-coup`）；Trotsky–Deutscher 一线的“革命左翼结构不相容论”库内尚无专门论断卡，作缺口登记。Koenker 以莫斯科工人及街头战斗为焦点（`RN-W32-koenker-moscow-strikes-duma-votes-and-october-week`）；Basil 则提示反对布尔什维克夺权者对武力与谈判也发生分裂（`CLM-basil-1984-october-and-vikzhel-collapse`）。广泛联合是否可行仍是反事实问题，铁路工会压力并不保证各方接受相同条件。

## 2. 一跳邻域全量微摘要目录 (去重后共 13 个节点，0 截断)
- **`INS-sovnarkom-and-vtsik`**（人民委员会与全俄、全苏中央执行委员会）: 苏维埃代表大会闭会期间，中执委在宪制上监督政府，人民委员会却迅速掌握施政与大量法令制定。苏俄与1922年成立的苏联各有中执委与人民委员会，不能混同。党内领导与国家机关关系不断变化，政治局权重日增，但1920年代仍须经政府落实决策。 ‖ `→ORG-vikzhel`[legislative_power_dispute|1917-11]: 11-04 表决与联合政府谈判背景 ； `←ORG-vikzhel`[legislative-power-dispute|1917-11]: 11-04 中执委表决人民委员会法令权
- **`ORG-bolsheviks-rcpb-vkpb`**（布尔什维克派—俄共（布）—联共（布））: 布尔什维克起于1903年社民工党二大后的党内多数派，经流亡、地下活动与1917年群众扩张成为执政党；1918年称俄共（布），1925年称联共（布）。它从地方主动性较强的革命党，演变为拥有任命网络与纪律制裁的党国核心，过程分阶段且存争议。 ‖ `→ORG-vikzhel`[coalition-negotiation|1917-10至11]: 铁路工会斡旋联合政府，暴露党内中央委员会多数与少数分歧 ； `←ORG-vikzhel`[mediated-coalition-talks|1917.10–11]: 借铁路运输杠杆要求联合政府，并暴露布党内部严重分歧
- **`ORG-mensheviks`**（孟什维克）: 俄国社会民主主义政党（1903–1924），源于1903年二大马尔托夫等与列宁围绕党章第一条及集中制的决裂，主张开放型群众政党与工人自主活动。1917年分化为策烈铁里、但恩主导的入阁“革命护国派”与马尔托夫领导的反战“国际主义派”；十月后开展苏维埃合法反对派抗争，1921年后遭取缔。 ‖ `←ORG-vikzhel`[negotiation-participant|1917]: 孟什维克内部对政府和抵抗方式并不一致，部分人参与调停
- **`ORG-psr`**（社会革命党）: 1901年末合并建立的俄国新民粹派政党，以土地社会化纲领与战斗组织暗杀闻名。1917年选民基数居全俄之冠却在战争、分地拖延与左翼分裂中失势；虽夺立宪会议多数仍遭解散，内战“第三条道路”溃于高尔察克政变，1922年莫斯科公审后在国内覆灭。 ‖ `←ORG-vikzhel`[negotiation-participant|1917]: 右翼社革党主导机关并拒绝让步，社革党分裂改变联盟可能
- **`ORG-left-srs`**（左翼社会革命党）: 1917年底从社会革命党分裂出的激进民粹派政党（1917–1923），以斯皮里多诺娃、普罗相等为首。拥护苏维埃政权并于1917年12月加入人民委员会与布尔什维克联合执政；1918年3月因反《布列斯特和约》退阁但仍维持北方公社合作，7月6日刺杀德国大使米尔巴赫遭全面清洗而覆灭。 ‖ `←ORG-vikzhel`[coalition-partner-after-failure|1917.12–1918]: 谈判破裂后单独入阁，改变广泛联盟的可能性
- **`EVT-1917-10-october-revolution`**（1917年十月革命）: 1917年10月24—27日（俄历；公历11月6—9日），军事革命委员会夺取彼得格勒中枢，冬宫陷落，苏维埃二大通过和平、土地法令并建立人民委员会。群众激进化、组织夺权与多党联合失败交织；首都迅速接管不代表全国无血革命。 ‖ `←ORG-vikzhel`[post-insurrection-mediation|1917]: 起义后以罢工威胁促谈，莫斯科同时有停火斡旋
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←ORG-vikzhel`[ultimatum-opponent|1917-11]: 反对排除自己与托洛茨基的联合方案，提出十人最后通牒
- **`PER-kamenev`**（列夫·加米涅夫）: 老布尔什维克、首任全俄中执委主席。1917年自四月至立宪会议一贯坚守温和宪政社会主义联盟路线并公开反对十月起义；1924年十三大联手季诺维也夫压下《列宁遗嘱》，1925年十四大公开发言反斯大林“领袖”集权后失势；1928年7月密会布哈林并留下外泄笔记，反成右派致命罪证。 ‖ `←ORG-vikzhel`[coalition-advocate|1917-11]: 布党内主张广泛联合的代表人物
- **`PER-zinoviev`**（格里戈里·季诺维也夫）: 老布尔什维克、共产国际首任主席（1919–1926）。1917年十月公开反对武装起义；1920年哈雷演说力推二十一条与阶级恐怖，1923年豪赌“德国十月”并首倡社民党“法西斯羽翼”论；借“三驾马车”排托后于1925年发起新反对派，1926年7月首因秘密第7条被逐出政治局，1927年底被开除后屈服。 ‖ `←ORG-vikzhel`[coalition-advocate-then-retreat|1917-11]: 辞职并于 11-06/07 认错
- **`PER-rykov`**（阿列克谢·李可夫）: 老布尔什维克与苏维埃经济组织家。1917年四月会议曾质疑《四月提纲》，十月后因维克热尔联合政府诉求辞职；两掌最高国民经济委员会，1924年继列宁任苏联人民委员会主席；1928–1929年协同布哈林抵制非常征粮并提“两年农业计划”遭撤职清洗，其名却在库班农民口号中回响。 ‖ `←ORG-vikzhel`[coalition-advocate|1917-11]: 辞职者之一
- **`PER-sverdlov`**（雅科夫·斯维尔德洛夫）: 布尔什维克地下组织与党国协调骨干。1917年四月会议后主持中央书记处，参与十月军革委，11月任全俄中执委主席；1918年干预立宪会议开幕、主持苏俄宪法起草。1919年3月早逝，在内战与党组织扩张背景下加速八大及会后全会常设政治局、组织局、书记处的分工。 ‖ `←ORG-vikzhel`[vtsik-chair|1917-11]: 11-08 [O.S.] 接任中执委主席
- **`PER-martov-l`**（尤利·马尔托夫）: 孟什维克核心领袖与国际主义左翼旗手。1903年二大凭党章第一条（28:22:1）与列宁分道；1917年七月夜倡“清一色社会主义政府”遭党内主流否决，十月二大率派退场；1918年工人抗议浪潮中坚持苏维埃合法反对派立场，1920年哈雷大会与季诺维也夫正面交锋痛斥恐怖与二十一条，后流亡柏林病逝。 ‖ `←ORG-vikzhel`[negotiation-participant|1917-11]: 国际主义孟什维克，与谈判相关
- **`PER-dan`**（费奥多尔·但）: 孟什维克核心组织领袖，马尔托夫挚友兼妹夫。1871年生于彼得堡医师家庭（原姓古尔维奇）。1917年与策烈铁里共掌彼得格勒苏维埃执委会“星室”推行“革命护国主义”（6月11日曾阻止策烈铁里解除布尔什维克武装）；十月后转向左翼中派并在苏俄境内坚持合法反对，直至1922年被驱逐出国。 ‖ `←ORG-vikzhel`[negotiation-participant|1917-11]: 孟什维克领导人之一

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 2 项)
### `DEB-1917-october-coup-or-social-revolution`：十月革命：少数派政变还是社会革命？
## [T1] 核心问题定义
十月武装夺权是少数派政变，还是工人、士兵与农民社会革命的政治表达？有组织的起义与广泛的基层动员能否同时成立，苏维埃多数又能否代表全国选民？这些问题涉及不同地区、不同时间的支持与合法性，不能以一次投票或一次攻占行动互相替代。

## [T2] 各学派立场对照矩阵
**经验基准**：彼得格勒苏维埃军事革命委员会组织行动，临时政府于1917-10-25 [O.S.] / 1917-11-07 [N.S.] 被推翻；第二次全俄工兵代表苏维埃代表大会当晚开幕，孟什维克与右派社革党抗议退场，大会于10月26日 [O.S.] / 11月8日 [N.S.] 通过《和平法令》《土地法令》并组建人民委员会。据站内选举统计（`DATA-01-1905-1917-strikes-and-petrograd-elections`、`DATA-07-1905-1918-unions-moscow-swings-and-constituent-assembly-votes`），布尔什维克在1917年9月莫斯科区杜马获51.5%选票、11月全俄立宪会议选举在大城市与北/西前线占优，但在全国立宪会议总票中仅占约22.5%–24%（社革党各单合占约37%–40%，且选票名册未反映10月左翼社革党独立分党）。苏维埃代表、立宪会议选民与农村夺地农民并非同一政治总体。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 自由主义“静默技术性政变”论 | Richard Pipes, *The Russian Revolution* (1990) | 援引马拉帕尔泰“静默技术性政变”概念，断言十月并非群众起义，而是列宁与军革委利用临时政府权威真空发动的少数派武装夺权，且本质上是**“针对全国苏维埃组织本身的政变”**——抢在苏维埃二大开幕前推翻临时政府，将全国苏维埃代表置于既成事实之下。 | `CLM-pipes-1990-october-classic-coup` | 将工人赤卫队与驻军顺从简化为阴谋家操纵，难以解释布尔什维克在9–11月两都市/区杜马及北方前线选票中的真实多数。 |
| 开放性群众政党与托洛茨基苏维埃合法性策略 | Alexander Rabinowitch, *The Bolsheviks Come to Power* (1976) | 1917年的彼得格勒布尔什维克并非铁板一块的密谋集团，而是吸收数万工人兵士、容忍加米涅夫—季诺维也夫公开异议的开放性群众政党；夺权成功关键在于**托洛茨基策略**——以彼得格勒苏维埃军革委“保卫苏维埃与卫戍部队”为名实施防御性展开，并将政权移交严格锚定于第二次全俄苏维埃代表大会开幕，以赢得无党派工兵的苏维埃合法性认同。 | `CLM-rabinowitch-1976-open-democratic-mass-party`；`CLM-rabinowitch-1976-october-three-factions-debate`；`CLM-rabinowitch-1976-trotsky-soviet-congress-strategy` | 首都党组织的战前民主开放性与苏维埃防卫策略，不能自动推及外省夺权或10月底维克热尔谈判破裂后的一党专政化。 |
| 列宁“稍纵即逝窗口”与先行夺权论（与托洛茨基路线之张力） | Vladlen T. Loginov, *Lenin in 1917: On the Brink of the Possible* (2017) | 与拉比诺维奇聚焦托洛茨基“等待并依托苏维埃二大”形成直接张力：洛吉诺夫论证列宁之所以痛斥“等待苏维埃代表大会是白痴行为或背叛、拖延就是死亡”，是因为洞察到10月中旬无政府浪潮与军事反革命夹击下存在“稍纵即逝的夺权窗口”，唯有在大会开幕前先行武装夺权、造成既成事实，才能迫使动摇的苏维埃大会接管政权。 | `CLM-loginov-lenin-1917-fleeting-window-of-power` | 高度认同列宁对紧急时机的政治直觉，但恰恰从反面印证了“先行夺权把苏维埃二大置于既成事实”的程序正当性争议。 |
| 工厂控制与莫斯科“政策先于党派”社会史 | S. A. Smith, *Red Petrograd* (1983); Diane P. Koenker, *Moscow Workers and the 1917 Revolution* (1981) | S. A. Smith证明彼得格勒工厂委员会推行“工人监督”最初是防止企业主关厂与经济崩溃的防御性自救，而非按意识形态蓝图消灭资本主义；Koenker证明莫斯科十月经历了与彼得格勒截然不同的惨烈炮战，且莫斯科多数工人虽在原则上拥护苏维埃政权，却**拒绝为党派垄断冒内战风险**（支持多党社会主义联合），其激进化遵循**“政策先于党派（policy before party）”**的理性渐进机制。 | `CLM-smith-sa-1983-defensive-workers-control`；`CLM-koenker-1981-moscow-october-armed-struggle-vs-petrograd`；`CLM-koenker-1981-rational-incremental-radicalization` | 两都工业工人的防御性/理性选择不能代表占人口八成的农村公社或边疆民族地区。 |
| 维克热尔妥协流产与立宪会议合法性冲突 | John D. Basil, *The Mensheviks in the Revolution of 1917* (1984); 姚海（主编）《俄国革命史》(2013); Alexander Rabinowitch, *The Bolsheviks in Power* (2007) | Basil与姚海剖析十月后全俄铁道工会（维克热尔）调停与清一色社会主义联合政府谈判：孟什维克内部分裂与10月29–30日士官生暴动撕裂妥协，布尔什维克中央内部加米涅夫、季诺维也夫、李可夫、诺金等辞职警告“纯布尔什维克政府只能靠政治恐怖维持”；姚海与Rabinowitch (2007) 进一步揭示苏维埃阶级专政逻辑与普选立宪会议（1918年1月5–6日被武力解散）之间不可调和的二元合法性冲突。 | `CLM-basil-1984-october-and-vikzhel-collapse`；`CLM-yao-hai-post-october-coalition-failure-and-one-party-formation`；`CLM-yao-hai-constituent-assembly-vs-soviet-legitimacy-clash`；`CLM-rabinowitch-2007-constituent-assembly` | 维克热尔谈判与立宪会议解散解释了十月向一党制滑落的制度拐点，但不能反过来否定10月25日临时政府已彻底丧失首都工兵支持的事实。 |
| 当事人革命解释与反对派在场反证（B级文献） | [B级当事人文献] Leon Trotsky, *History of the Russian Revolution* (1930–32); N. N. Sukhanov, *The Russian Revolution, 1917* (1922) | 托洛茨基将起义定性为“在苏维埃合法性掩护下实施的武装夺权艺术”；**苏汉诺夫的证言尤具史学张力**——他虽作为孟什维克国际派痛斥布尔什维克政权缺乏民主准备、悔恨温和派10月25日夜退场将苏维埃拱手让给列宁，却**以亲历反对者身份断然驳斥右翼“纯军事阴谋”说**，证言彼得格勒工人与驻军当时确以压倒性多数支持推翻临时政府。 | `CLM-trotsky-1930-art-of-insurrection-and-soviet-legality`；`CLM-sukhanov-1922-october-walkout-tragedy` | 两者均属B级当事人回忆与事后政治辩护（托洛茨基旨在反击斯大林并凸显自身军革委功绩，苏汉诺夫旨在检讨国际派失策），必须与当时会议速记对读。 |
| 农民道德经济、帝国边疆与十月记忆建构 | Orlando Figes (1996); Ronald Grigor Suny (2017); Eric Blanc (2021); Frederick C. Corney, *Telling October* (2004) | Figes揭示农民公社夺地遵循自身“道德经济”，利用《土地法令》将既成黑分土地合法化而非服从城市党令；Suny综合社会史与阶级话语极化；Blanc将1917年十月放入帝国边疆民族与阶级互动视野；Corney则考证党史委（Istpart）与1920年代庆典如何将原本混乱多中心的十月夺权事后重塑为宏大叙事神话。 | `CLM-figes-1996-peasant-moral-economy-1917`；`CLM-suny-2017-totalitarian-vs-social-history-turn`；`CLM-suny-2017-class-discourse-and-polarization`；`CLM-blanc-2021-borderlands-in-1905-and-1917`；`CLM-corney-2004-istpart-and-institutionalizing-october-memory` | 农民夺地与边疆动员支持推翻旧政权，但并不等于授权布尔什维克随后的余粮收集制与一党垄断；记忆建构研究不可消解1917年秋真实的社会崩溃。 |

### `DEB-1917-all-socialist-coalition-vikzhel-missed-chance`：维克热尔谈判与清一色社会主义联合政府之争
## [T1] 核心问题定义
十月起义后铁路工会维克热尔推动的社会主义政党联合政府，是多党苏维埃政治一度存在而后丧失的选择，还是各方对夺权合法性、政府构成和战争的分歧使之难以实现？谈判破裂的责任和一个可持续联盟的可行性是两个不同问题。

## [T2] 经验共识 + 各学派立场对照矩阵

**经验共识**：1917年俄历十月下旬至十一月初（公历十一月），维克热尔借铁路运输与罢工威胁推动协商；布尔什维克内部对让步有分歧，加米涅夫、李可夫等支持扩大联合，列宁与托洛茨基反对危及既得权力的条件。谈判最终未产生所设想的广泛联合政府；后来成立的布尔什维克—左翼社革党联合，范围较窄。

| 取向 | 代表与核心解释 | 盲点与待核问题 | 本地论断锚点 |
| :--- | :--- | :--- | :--- |
| 情境偶然与多元可能 | Rabinowitch (2007) 重视布尔什维克内部温和派及基层压力，强调一党专政并非十月自动写定。 | 支持谈判并不等于各派已同意同一内阁、纲领或权力分配；须区分首都证据和全国意见。 | `CLM-rabinowitch-2007-contingency-of-dictatorship`; `CLM-rabinowitch-2007-left-sr-coalition-collapse` |
| 意识形态与权力集中 | Pipes、Malia 强调列宁的政治观及其对权力垄断的追求；联合谈判可被解释为策略性周旋。 | 若把每次谈判都预设为幌子，便难解释党内真实争论和策略变化；两位作者对此次谈判的具体措辞仍须核原著。 | `CLM-pipes-1990-october-classic-coup` |
| 革命左翼的结构不相容 | Trotsky、Deutscher强调对十月合法性、权力归属和列宁、托洛茨基本人入阁的冲突，认为某些条件将削弱革命政府。 | 托洛茨基兼具参与者与事后论辩者身份；不能把反对党内部不同条件视作始终一致。 | `CLM-basil-1984-october-and-vikzhel-collapse` |
| 温和社会主义与地方政治 | Galili、Koenker、Hickey 的研究方向提示考察温和派及省城组织的分歧，不应只看首都领袖。 | 各作者对维克热尔及地方联盟的具体论断仍须逐项核实；地方个案不必然代表全国。 | `CLM-galili-1989-coalition-government-trap`; `CLM-hickey-2001-smolensk-moderate-socialists-collapse-1917`; `CLM-basil-1984-menshevik-three-way-paralysis` |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/25 条)
- **`CLM-basil-1984-october-and-vikzhel-collapse`** [`SCH-basil-john`(约翰·D·巴兹尔) | pp. 165–175（本地 PDF 同号）]: 
- **`CLM-getzler-1967-martov-soviet-opposition`** [`SCH-getzler-israel`(伊斯雷尔·格茨勒) | pp. 168-191]: 
- **`CLM-yao-hai-post-october-coalition-failure-and-one-party-formation`** [`SCH-yao-hai`(姚海) | [PDF pp. 532-535, 543-569]]: 
- **`CLM-rabinowitch-2007-left-sr-coalition-collapse`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 274-282, 287-309, 395-396]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-rabinowitch-1976-open-democratic-mass-party`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-rabinowitch-1976-october-three-factions-debate`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-rabinowitch-1976-trotsky-soviet-congress-strategy`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-loginov-lenin-1917-fleeting-window-of-power`** [`SCH-loginov-vladlen`(弗拉德连·洛吉诺夫) | pp. 523-524, 531-532, 560-561, 621-622, 656-658]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-koenker-1981-moscow-october-armed-struggle-vs-petrograd`** [`SCH-koenker-diane`(黛安·P·科恩克尔) | pp. 329–355 (local PDF pp. 345–371); p. 366 (PDF p. 382)]: 
- **`CLM-koenker-1981-rational-incremental-radicalization`** [`SCH-koenker-diane`(黛安·P·科恩克尔) | pp. 359–363 (local PDF pp. 375–379); p. 254 (PDF p. 270)]: 
- **`CLM-yao-hai-constituent-assembly-vs-soviet-legitimacy-clash`** [`SCH-yao-hai`(姚海) | [PDF pp. 574-596]]: 
- **`CLM-rabinowitch-2007-constituent-assembly`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 88-91, 105-110, 121-127]: 
- **`CLM-trotsky-1930-art-of-insurrection-and-soviet-legality`** [`SCH-trotsky-leon`(列夫·达维多维奇·托洛茨基 · participant-historian) | （中译 EPUB 无纸页；第三卷第二十—二十一章）]: 
- **`CLM-sukhanov-1922-october-walkout-tragedy`** [`SCH-sukhanov-nikolai`(尼古拉·苏汉诺夫) | pp. 631–647, 657–660 (PDF pp. 683–699, 709–711)]: 
- **`CLM-figes-1996-peasant-moral-economy-1917`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 343-352]: 
- **`CLM-suny-2017-totalitarian-vs-social-history-turn`** [`SCH-suny-ronald-gregor`(罗纳德·格里戈尔·苏尼) | pp. 87-95 (approx. ch. 2 sect. on totalitarianism and revision)]: 
- **`CLM-suny-2017-class-discourse-and-polarization`** [`SCH-suny-ronald-gregor`(罗纳德·格里戈尔·苏尼) | pp. 160-175 (approx. ch. 5 on class, strikes, discourse)]: 
- **`CLM-blanc-2021-borderlands-in-1905-and-1917`** [`SCH-blanc-eric`(埃里克·布兰克) | pp. 20–23, 338–436, 488–531, 457–543]: 
- **`CLM-corney-2004-istpart-and-institutionalizing-october-memory`** [`SCH-corney-frederick`(弗雷德里克·C·科尼 · memory-and-cultural-history) | 【待规整语料】]: 
- **`CLM-galili-1989-coalition-government-trap`** [`SCH-galili-ziva`(齐娃·加利利) | pp. 169-170, 177-181 (PDF pp. 195-196, 203-207)]: 
- **`CLM-hickey-2001-smolensk-moderate-socialists-collapse-1917`** [`SCH-raleigh-donald`(唐纳德·J·罗利) | Local PDF pp. 28–63; English print pagination not verified]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 9 条 L3 逐日细节见 `timeline/L3_daily/`)
