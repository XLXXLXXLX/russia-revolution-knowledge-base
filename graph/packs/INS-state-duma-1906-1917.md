# 1-Hop 去重平衡上下文包：`INS-state-duma-1906-1917`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`INS-state-duma-1906-1917`** (俄罗斯帝国国家杜马（第一至第四届） | `cards/institutions/INS-state-duma-1906-1917.md` | `multi-perspective`): 已覆盖=`constitutional-institutional-via-CLM, liberal-opposition-gaida, february-hasegawa, social-basis-manning, pipes-seat-classification`；待补=`electoral-curia-regional-comparison, legislative-roll-call, seat-count-reconciliation, soviet-historiography-june-third-system`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1905年革命使君主制接受立法性国家杜马，但1906年基本法仍保留皇帝任免政府、解散杜马与紧急立法权。头两届因土地与政治责任问题短命；1907年选举法后第三、四届趋保守。1915年进步同盟施压，1917年二月杜马临时委员会参与接管政权，须与苏维埃共析。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **制度与选举**：国家杜马和国务会议共同参与立法，并非对内阁拥有完整责任制的议会。主要选举路径按地主、城市、农民和工人等等级团分组，多级间接产生选举人，财产、性别、族群和地域限制造成代表权高度不均。1907年法进一步提高地主及有产阶层权重并压缩部分边疆代表（`CLM-manning-1982-june-third-coup-social-basis`；`RN-W12-gentry-reaction-and-four-party-rivalry-1905`），不能把四个等级团理解为每人一票的四个等额选区。1905年的宣言文本见 `WEB-1905-10-17-october-manifesto`（仅含宣言，不含1906年基本法本文）。
- **第一届**：`1906-04-27 [O.S.] / 1906-05-10 [N.S.]` 开幕，通常以 `1906-07-08 [O.S.] / 1906-07-21 [N.S.]` 标为最后会期；解散诏令与公布亦有 `1906-07-09 [O.S.] / 1906-07-22 [N.S.]` 的记载，须核原件区分日期，库内无对应 L3 节点。立宪民主党为最大党团（Pipes 席位归类179席），劳动派与农民代表推动强制征收地主土地等方案；土地、政治犯赦免与内阁责任制冲突使宫廷与杜马破裂。部分代表赴维堡发表不合作宣言，不能把解散归为单一法案的直接结果。
- **第二届**：`1907-02-20 [O.S.] / 1907-03-05 [N.S.]` 开幕，`1907-06-03 [O.S.] / 1907-06-16 [N.S.]` 解散。政府以社民党团被指密谋为借口，解散杜马并在未经议会同意下修改选举法，构成“六三政变”。
- **第三、四届**：第三届于 `1907-11-01 [O.S.] / 1907-11-14 [N.S.]` 开幕，库内 L2 记其结构为422席（A 级，源自 Pipes ch13；`timeline/L2_chronicles/E04_1907-1914_stolypin_and_labor_upsurge.md`），1912年届满；十月党与民族主义及温和右翼形成不同组合，支持斯托雷平政府的议案（`PER-stolypin`；`POL-stolypin-agrarian-reform`；`DEB-1906-stolypin-wager-and-agrarian-viability`），仍有议会内部竞争。第四届于 `1912-11-15 [O.S.] / 1912-11-28 [N.S.]` 开幕。1915年战时危机催生跨党派进步同盟，要求能获公众信任的内阁，这与明确要求对杜马负责的内阁并不完全相同（Gaida，pp. 134–175；`ORG-octobrists-and-progressive-bloc`；`ORG-kadets`）。
- **杜马主席（库内已有节点）**：古契科夫 `1910–1911` 主持第三届杜马（`PER-guchkov`）；罗将科 1911年起任主席，`1917-02-27 [O.S.]` 任临时委员会主席（`PER-rodzianko`）。第一届穆罗姆采夫、第二届戈洛文、第三届霍米亚科夫等主席及完整任期，库内无专卡，待核。
- **二月与终结**：`1917-02-27 [O.S.] / 1917-03-12 [N.S.]` 杜马领导人面对停会敕令，在私人会议后于晚间 23:30 前后决定成立临时委员会（`timeline/L3_daily/1917-02_february_eight_days.md`；`EVT-1917-02-february-revolution`），随后参与建立临时政府；这不等于杜马正式复会掌握全部权力。临时政府后来正式解散第四届杜马，常见日期为 `1917-09-23 [O.S.] / 1917-10-06 [N.S.]`，原始法令日期待核，且 `_ns` 取 N.S.，不得与旧历 10-06 混用。

### 议席与存续口径对照
| 届别 | 开幕 / 终止 | 席位口径 | 来源 | 口径差异 |
| :--- | :--- | :--- | :--- | :--- |
| 第一届 | `05-10` / `07-21` [N.S.] | 立宪民主党179席 | Pipes 席位归类（L2 `E03`） | 存续约72天；边界党团计数可复核 |
| 第二届 | `03-05` / `06-16` [N.S.] | 社会党人合计222：社民65、社革37、人民社会党16、劳动派104；立宪民主党98 | Pipes（L2 `E03`#L38） | 存续约105天（按卡内开闭日期推算约103天，待回核） |
| 第二届 | 同上 | 社革党议员34名；土地社会化法案获104票 | Hildermeier（`RN-W29-hildermeier-psr-azev-crisis-and-modernization-dilemma`#L36） | 社革党席位 Pipes **37** vs Hildermeier **34**，两组分母在库内并存，口径不一致，若取34则社会党人合计相应为219 |
| 第三届 | `11-14` [N.S.] 开幕 | 422席 | L2 `E04`#L76（源自 Pipes ch13） | 补选与党团变动使席位随时间变化 |

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 关系实质 | 核心依据 |
| :--- | :--- | :--- | :--- | :--- |
| `POL-october-manifesto-and-1906-fundamental-laws` | `constituted_and_limited_by` | 1906–1917 | 杜马享有立法参与权，君主与上院仍有关键否决及行政权 | `WEB-1905-10-17-october-manifesto`（仅宣言；基本法本文待对照） |
| `ORG-octobrists-and-progressive-bloc` | `parliamentary_coalition` | 1907–1917 | 十月党影响第三届杜马，1915年跨派同盟要求信任内阁 | `CLM-gaida-2003-progressive-bloc-dilemma` |
| `ORG-kadets` | `largest_faction_first_duma` | 1906–1917 | 第一届最大党团，进步同盟成员 | Pipes 席位归类（L2 `E03`） |
| `PER-rodzianko` | `chaired_and_led_committee` | 1911–1917 | 杜马主席在二月主持临时委员会；其权威受起义和苏维埃制约 | `CLM-hasegawa-2018-duma-committee-revision` |
| `PER-guchkov` | `chaired_third_duma` | 1910–1911 | 主持第三届杜马 | `PER-guchkov` 卡 |
| `PER-milyukov` | `opposition_leader` | 1906–1917 | 议会反对派策略代表 | `CLM-gaida-2003-progressive-bloc-dilemma` |
| `PER-stolypin` | `government_counterpart` | 1906–1911 | 与第二、三届杜马互动 | `DEB-1906-stolypin-wager-and-agrarian-viability` |
| `POL-stolypin-agrarian-reform` | `legislative_context` | 1907–1911 | 第三届杜马土地改革议案 | `DEB-1906-stolypin-wager-and-agrarian-viability` |
| `EVT-1917-02-february-revolution` | `committee_formation` | 1917.03 | 临时委员会形成与停会敕令 | L3 `1917-02_february_eight_days`；`CLM-hasegawa-2018-duma-committee-revision` |
| `CON-dual-power` | `participated_in_origins` | 1917.03 | 临时委员会、苏维埃和街头动员共同塑造政权转移 | `CLM-hasegawa-2018-dual-power-origins`；`DEB-1917-dual-power-and-february-origins` |

### 2.3 史学争鸣光谱
**经验共识**：君主制保留广泛权力，1907年选举法向有产者倾斜（Manning），1915年议会反对派和王朝关系恶化。**解释分歧**：Gaida 强调自由派在争取政权与恐惧大众动员之间的策略困境（`CLM-gaida-2003-liberals-in-february-1917`）；Hasegawa 增订研究重审临时委员会和次级精英的主动性，不能只用“群众迫使被动议员”概括（`CLM-hasegawa-2018-duma-committee-revision`）。库内可核的 Pipes 论点是其对前两届议席的归类（见上表），Haimson 对城市社会分化与政治稳定难题的长期分析（`DEB-1914-haimson-thesis-stability`）并未提供四届杜马全部议事的直接证据。

## 2. 一跳邻域全量微摘要目录 (去重后共 12 个节点，0 截断)
- **`EVT-1907-1914-june-third-regime-and-lena-to-july-strikes`**（1907–1914年六三体制、斯托雷平反动与勒拿至七月工潮）: 1907年6月3日[O.S.]六三政变至1914年7月一战爆发间的战前危机年代。前五年呈现土地缙绅杜马优势、斯托雷平土改与地下党受挫蛰伏；1912年4月勒拿金矿惨案引爆《真理报》创刊、工会与保险会转向及1914年7月圣彼得堡街垒工潮，引发战前稳定与否之争。 ‖ `→INS-state-duma-1906-1917`[institutional_arena|1907–1914]: 第三、四届杜马作为六三选制下的贵族—温和自由派妥协舞台，仍因政府否决地方改革而受困
- **`EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc`**（1914–1916年一战总动员、弹药危机与杜马进步同盟危机）: 1914年7月德国宣战至1916年末帝俄总体战危机演化。1915年大撤退与弹药短缺催生战时工业委员会及杜马进步同盟；沙皇亲征并放任内阁“部长走马灯”，军工扩招、里季希粮食摊派受挫与恶性通胀加剧精英离心和城市工潮，将政权推向1917年二月危机门槛。 ‖ `→INS-state-duma-1906-1917`[institutional_battleground|1914–1916]: 杜马讲坛成为揭露后方行政失序与宫廷丑闻的扩音器，1916年11月米留可夫演说重创内阁声誉
- **`POL-october-manifesto-and-1906-fundamental-laws`**（十月宣言、国家根本法与六三体制）: 1905年革命迫使沙皇签署《十月宣言》，承诺公民自由、杜马立法同意权。1906年《国家根本法》使代议立法制度化，同时保留皇权、上院否决与休会紧急立法；1907年未经议会同意改选举法，形成延至1917年的六三体制。它并非议会责任内阁，亦不能视为纯粹装饰。 ‖ `←INS-state-duma-1906-1917`[constituted_and_limited_by|1906–1917]: 杜马享有立法参与权，君主与上院仍有关键否决及行政权 ； `→INS-state-duma-1906-1917`[created-and-reshaped|1906–1917]: 宣言承诺的立法同意权经根本法落实为杜马；1907年选举法重组后形成第三、四届杜马
- **`ORG-octobrists-and-progressive-bloc`**（十月十七日同盟与进步同盟）: 1905年十月宣言后形成的十月十七日同盟是拥护君主立宪的温和自由主义政党；1915年的进步同盟是跨党派杜马联盟，二者并非同一组织。两者既要求改善政府与社会关系，又忧惧群众革命；1917年部分杜马领袖成为临时政权支点，却不能独掌街头、军队与苏维埃。 ‖ `←INS-state-duma-1906-1917`[parliamentary_coalition|1907–1917]: 十月党影响第三届杜马，1915年跨派同盟要求信任内阁 ； `→INS-state-duma-1906-1917`[parliamentary-coalition|1907–1917]: 十月党影响第三届杜马，1915年跨派同盟要求信任内阁
- **`ORG-kadets`**（立宪民主党（卡德特党））: 1905年10月从解放同盟诞生的俄国自由主义核心政党，主张四尾制宪、有偿征地与议会道路，曾主导前两届杜马与战时进步同盟。1917年二月主导首届临时政府并切断对杜马从属关系，旋因战争、土地危机及科尔尼洛夫事件退阁丧失民心，十月后被定为“人民公敌”并在内战与流亡中分裂。 ‖ `←INS-state-duma-1906-1917`[largest_faction_first_duma|1906–1917]: 第一届最大党团，进步同盟成员 ； `→INS-state-duma-1906-1917`[parliamentary_arena|1906–1917]: 第一、二届杜马主导力量，六三后退居少数反对派，1917-03-03由卡德特主导切断对杜马问责
- **`PER-rodzianko`**（米哈伊尔·弗拉基米罗维奇·罗将柯）: 十月党人，1911–1917年杜马议长，二月革命时主持临时委员会，谋以信任内阁、君主立宪应变，曾推大公宪制方案，后劝阻米哈伊尔即位。临时政府成立后，面对起义士兵、苏维埃与自由派内部分歧，其杜马中心方案败于米留可夫等；回忆录的领袖形象须与会议记录及同时代证据互校。 ‖ `←INS-state-duma-1906-1917`[chaired_and_led_committee|1911–1917]: 杜马主席在二月主持临时委员会；其权威受起义和苏维埃制约 ； `→INS-state-duma-1906-1917`[duma-speaker|1911-03-22 [O.S.]–1917]: 第三、第四届杜马议长；其杜马中心方案的制度母体，杜马于 1917-10-06 [O.S.] 被正式决议解散
- **`PER-guchkov`**（亚历山大·伊万诺维奇·古契科夫）: 十月十七日同盟领袖、第三届杜马前议长与战时军事工业委员会负责人。1917年他同舒尔金赴普斯科夫接收尼古拉二世退位文书，出任临时政府陆海军部长；军队权威危机和四月政治危机中辞职。战前宫廷政变计划真实存在，但未实际发动，不能将其当作二月起义的成熟指挥方案。 ‖ `←INS-state-duma-1906-1917`[chaired_third_duma|1910–1911]: 主持第三届杜马 ； `→INS-state-duma-1906-1917`[third-duma-speaker|1910-03-10–1911-03-15 [O.S.]]: 第三届杜马议长，辞职后由罗将柯继任
- **`PER-milyukov`**（帕维尔·米留可夫）: 俄国历史学家、卡德特党核心领袖（1859–1943）。主持解放同盟确立四尾制宪与有偿征地纲领；一战任进步同盟舵手，1916年发表“愚蠢还是叛国”演说；1917年任首届临时政府外长，03-03/03-16架空杜马，因04-18[O.S.]/05-01[N.S.]照会下野，流亡提“新策略”。 ‖ `←INS-state-duma-1906-1917`[opposition_leader|1906–1917]: 议会反对派策略代表
- **`PER-stolypin`**（彼得·斯托雷平）: 帝俄内务大臣（1906–1911）暨大臣会议主席（1906.07–1911.09）。以野战法庭与1907年六三选举法平定革命余波，借土地法令允许农户脱社确权、培植私有小农；1911年3月因西部六省地方自治法案第87条危机失势，同年9月在基辅遇刺，成为晚期的改革路径争议核心。 ‖ `←INS-state-duma-1906-1917`[government_counterpart|1906–1911]: 与第二、三届杜马互动 ； `→INS-state-duma-1906-1917`[dissolver_and_partner_then_bypassed|1906–1911]: 任内解散第一、二届杜马并以六三选举法重塑第三届杜马，虽保留议会立法与预算权并试图合作，却在1911年3月以第87条自毁议会联盟
- **`POL-stolypin-agrarian-reform`**（斯托雷平土地改革）: 1906年起，斯托雷平政府试图通过农户份地私有化、土地整理、农民银行贷款和移民，创造较自主的农民经营者并稳定农村。退出重分村社、确权、合并土地和迁居独立农庄是不同步骤，成功率及地区差异很大。大战减缓实施，1917年土地革命中许多分离土地重新进入村社分配；改革并未消除农民的土地渴求。 ‖ `←INS-state-duma-1906-1917`[legislative_context|1907–1911]: 第三届杜马土地改革议案
- **`EVT-1917-02-february-revolution`**（1917年二月革命）: 1917年2月23日至3月3日（俄历；公历3月8—16日），彼得格勒女工罢工、跨厂动员与驻军兵变推翻帝制。杜马委员会接管行政，苏维埃代表工兵，临时政府在革命全权与旧宪制断裂中成立；双重政权并非简单的主动让权。 ‖ `←INS-state-duma-1906-1917`[committee_formation|1917.03]: 临时委员会形成与停会敕令
- **`CON-dual-power`**（双重政权（两个政权并存））: 萌芽于1905年苏维埃；1917-03-02[O.S.]/03-15[N.S.]至七月事件，临时政府名义主权与彼得格勒苏维埃工兵实力、“有条件支持”并存。列宁四月称两类阶级专政交织，七月宣布终结，九月再提苏维埃夺权；修正史学强调多中心失序与双方虚弱。 ‖ `←INS-state-duma-1906-1917`[participated_in_origins|1917.03]: 临时委员会、苏维埃和街头动员共同塑造政权转移

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 3 项)
- **`DEB-1914-haimson-thesis-stability`**（海姆森命题：战前俄国的社会稳定与双重极化 | `historiography/debates/DEB-1914-haimson-thesis-stability.md` | 流派 `urban-polarization, labor-social-history, elite-political-history, liberal-institutional-and-contingent, crisis-and-war`）：一战前的工业增长、土地改革与杜马政治，能否使帝国逐步稳定，还是工人与有产社会、社会与专制国家的双重极化已侵蚀统治基础？1912年后罢工回升和改革受阻如何与战争冲击相互作用，须区分可观察的危机与无法验证的无战争反事实及其解释限度。
- **`DEB-1917-dual-power-and-february-origins`**（二月革命起源与“双重政权”宪制形成之争（1917） | `historiography/debates/DEB-1917-dual-power-and-february-origins.md` | 流派 `social-history, liberal-constitutional, participant, trotskyist, menshevik-coalition, elite-conspiracy-critique`）：二月革命是无领导的群众爆发，还是工厂与兵营中分散的积极分子推动的起义？沙皇退位后，杜马临时委员会、苏维埃与临时政府如何谈判并形成彼此制约的权力格局？群众压力、精英选择和战时危机的因果权重仍有争议，不能以宫廷阴谋代替街头革命。
- **`DEB-1906-stolypin-wager-and-agrarian-viability`**（村社生命力与斯托雷平土改前景之争 | `historiography/debates/DEB-1906-stolypin-wager-and-agrarian-viability.md` | 流派 `modernization-optimism, peasant-social-history, marxist-agrarian-roads`）：如果没有世界大战，帝俄能否借私有农户与农业增长和平化解农村革命？争议同时涉及生产效率、村社制度的适应力与政治稳定，任何一项的改善都不能自动证明另外两项。反事实命题不能由改革中断的事实直接证成或证伪。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/25 条)
- **`CLM-manning-1982-june-third-coup-social-basis`** [`SCH-manning-roberta`(罗伯塔·T·曼宁) | pp. 238–239]: 
- **`CLM-gaida-2003-progressive-bloc-dilemma`** [`SCH-gaida-fedor`(费奥多尔·盖达) | pp. 135-136, 162-168]: 
- **`CLM-hasegawa-2018-duma-committee-revision`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. xiii–xiv (PDF pp. 14–15); pp. 366–368, 377–378 (PDF pp. 387–389, 398–399); p. 652 (PDF p. 673)]: 
- **`CLM-hasegawa-2018-dual-power-origins`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. 626–638 (PDF pp. 647–659); cf. pp. 649, 660 (PDF pp. 670, 681)]: 
- **`CLM-gaida-2003-liberals-in-february-1917`** [`SCH-gaida-fedor`(费奥多尔·盖达) | pp. 355-356, 433-439]: 
- **`CLM-steinberg-2017-continuum-of-crisis-1905-1921`** [`SCH-steinberg-mark`(马克·D·斯坦伯格) | pp. 19, 61–62, 107–108]: 
- **`CLM-bonnell-1983-1912-1914-union-and-insurance-boards-bolshevik-capture`** [`SCH-bonnell-victoria`(维多利亚·E·邦内尔) | Book pp. 366–371, 390–438 [PDF pp. 389–394, 413–461]]: 
- **`CLM-bonnell-1983-state-employer-repression-undermining-menshevik-reformism`** [`SCH-bonnell-victoria`(维多利亚·E·邦内尔) | Book pp. 292–305, 316–323, 336–352, 372–389, 450–452 [PDF pp. 315–328, 339–346, 359–375, 395–412, 473–475]]: 
- **`CLM-hogan-1994-petersburg-metalworkers-1905-to-lena`** [`SCH-hogan-heather`(希瑟·霍根 · labor-social-history) | pp. 85–112]: 
- **`CLM-smith-sa-1996-petersburg-bolshevik-vs-menshevik-worker-appeal`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | International Review of Social History, vol. 41 (1996), pp. 12–15, 19–25]: 
- **`CLM-manning-1982-gentry-fronde-to-reaction`** [`SCH-manning-roberta`(罗伯塔·T·曼宁) | pp. 54–60, 122–124]: 
- **`CLM-hildermeier-2000-azev-affair-and-stolypin-era-paralysis`** [`SCH-hildermeier-manfred`(曼弗雷德·希尔德迈尔) | EPUB版无稳定原书页码；以本地章节与行号定位（ch14 L24–91, ch18 L112–150, ch22 L6–108, ch23 L81–217, ch24 L8–285, ch25 L6–33, ch26 L6–62；epub:main-14.xhtml, main-23.xhtml, main-24.xhtml, main-25.xhtml, main-26.xhtml, main-27.xhtml）]: 
- **`CLM-pipes-1990-patrimonial-state-and-intelligentsia`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 2 (Official Russia); ch. 4 (The Intelligentsia); cf. Introduction]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-yao-hai-1917-modernization-rupture-and-plebeian-radicalism`** [`SCH-yao-hai`(姚海) | [PDF pp. 47-55, 57-64, 68-72, 75-81, 87-88]]: 
- **`CLM-hasegawa-2018-sub-elite-activists`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. 643–645 (PDF pp. 664–666); cf. pp. 203–204, 218 (PDF pp. 224–225, 239)]: 
- **`CLM-sukhanov-1922-dual-power-pact`** [`SCH-sukhanov-nikolai`(尼古拉·苏汉诺夫) | pp. 117–126, 150, 153–158 (PDF pp. 163–172, 196, 199–204); cf. pp. 68, 104–108, 113–114]: 
- **`CLM-trotsky-1930-dual-power-instability`** [`SCH-trotsky-leon`(列夫·达维多维奇·托洛茨基 · participant-historian) | （中译 EPUB 无纸页；第一卷第十一、十六章）]: 
- **`CLM-galili-1989-revolutionary-defensism`** [`SCH-galili-ziva`(齐娃·加利利) | pp. 134-140, 148-151 (PDF pp. 152-158, 174-177)]: 
- **`CLM-galili-1989-coalition-government-trap`** [`SCH-galili-ziva`(齐娃·加利利) | pp. 169-170, 177-181 (PDF pp. 195-196, 203-207)]: 
- **`CLM-spitsyn-february-1917-elite-conspiracy-thesis`** [`SCH-spitsyn-yevgeny`(叶夫根尼·斯皮岑) | PDF pp. 11–15, 24, 28]: 
- **`CLM-figes-1996-soldier-mutiny-and-social-inversion`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 404-412]: 
- **`CLM-figes-1996-peasant-moral-economy-1917`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 343-352]: 
- **`CLM-hildermeier-2000-agrarian-socialism-modernization-dilemma`** [`SCH-hildermeier-manfred`(曼弗雷德·希尔德迈尔) | EPUB版无稳定原书页码；以本地章节与行号定位（ch08 L75–232, ch09 L26–44, ch12 L204–282, ch13 L107–185, ch17 L115–310, ch20 L750–753, ch24 L180–285, ch26 L6–96；epub:main-8.xhtml, main-9.xhtml, main-12.xhtml, main-13.xhtml, main-21.xhtml, main-25.xhtml, main-27.xhtml）]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
