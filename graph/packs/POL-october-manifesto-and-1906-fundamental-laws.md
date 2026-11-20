# 1-Hop 去重平衡上下文包：`POL-october-manifesto-and-1906-fundamental-laws`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`POL-october-manifesto-and-1906-fundamental-laws`** (十月宣言、国家根本法与六三体制 | `cards/policies/POL-october-manifesto-and-1906-fundamental-laws.md` | `multi-perspective`): 已覆盖=`constitutional-history, social-history, conservative-social-history, liberal-party-politics, pipes-political-history`；待补=`regional-electoral-experience, soviet-leninist-evaluation, monarchist-right`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1905年革命迫使沙皇签署《十月宣言》，承诺公民自由、杜马立法同意权。1906年《国家根本法》使代议立法制度化，同时保留皇权、上院否决与休会紧急立法；1907年未经议会同意改选举法，形成延至1917年的六三体制。它并非议会责任内阁，亦不能视为纯粹装饰。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **革命与宣言**：`1905-10-17 [O.S.] / 1905-10-30 [N.S.]`，尼古拉二世签署维特参与拟定的宣言，承诺人身不可侵犯和良心、言论、集会、结社自由，扩大杜马选举参与，并规定法律未经杜马同意不得生效。原文没有确立普选或内阁对杜马负责；自由的实践受到镇压和后续限制（同年12月莫斯科武装起义为“自由五十天后的反弹”）。
- **根本法的双重结构**：`1906-04-23 [O.S.] / 1906-05-06 [N.S.]` 批准修订《国家根本法》；部分目录以 `1906-04-26 [O.S.] / 1906-05-09 [N.S.]` 记公布，须与批准日期及具体官方刊布版本区分，不将两日当作两个法令。皇帝保留“最高专制权力”的称号、任免大臣及军队外交大权；改组后的国务会议作为上院与杜马共同参与立法，并可否决议案。第87条允许杜马休会期间在紧急情况下颁布临时措施，但规定不能用于修改根本法或杜马、国务会议及其选举规定，且须依程序提交议会。具体适用与滥用须分案检验。
- **六三转折**：`1907-06-03 [O.S.] / 1907-06-16 [N.S.]` 沙皇解散第二届杜马，政府未经立法机关同意改变选举法，违反根本法的立法程序及第87条限制。站内 L2 E03 L10（据Pipes）则把解散令记在 `1907-06-02 [O.S.] / 06-15 [N.S.]`、新选举法次日公布；两日换算均为+13，差异在事件语义（解散令发布与选举法公布），本卡沿用多数节点（`INS-state-duma-1906-1917`、`ORG-kadets`）的“06-03”口径，并保留此分野待官方《法令汇编》核对。新规则强化地主与富裕阶层的代表权，压缩工人、农民及部分非俄民族代表权；第三、第四届杜马仍能审议预算、推动立法和质询，却不能决定内阁命运。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-witte` | `architect` | 1905 | 维特主张以宣言和统一政府应对革命危机，最终由皇帝签署 | `1905-10-17_october-manifesto.md`；`PER-witte` |
| `PER-nicholas-ii` | `signed-and-reserved-autocratic-powers` | 1905–1917 | 签署宣言，又在1906年根本法中保留“最高专制权力”称号、任免与军政大权 | 宣言原档；`PER-nicholas-ii` |
| `INS-state-duma-1906-1917` | `created-and-reshaped` | 1906–1917 | 宣言承诺的立法同意权经根本法落实为杜马；1907年选举法重组后形成第三、四届杜马 | `INS-state-duma-1906-1917`（含各届起止与六三政变） |
| `ORG-kadets` | `liberal-centrist-reaction` | 1905–1917 | 立宪民主党以杜马为中心参与政治，宣言与根本法的不足是其反对与受挫的背景 | `ORG-kadets` |
| `PER-milyukov` | `leading-liberal-critic` | 1905–1917 | 立宪民主党领袖，对宣言兑现程度与杜马权限作政治评估 | `PER-milyukov`（待补具体论断页码） |
| `ORG-octobrists-and-progressive-bloc` | `named-after-manifesto` | 1905–1917 | 十月党以宣言命名，接受其为立宪底线，为第三、四届杜马多数力量之一 | `ORG-octobrists-and-progressive-bloc` |
| `PER-guchkov` | `octobrist-leader` | 1905–1917 | 十月党领袖，体现拥护宣言的温和右翼自由派路线 | `PER-guchkov` |
| `EVT-1905-revolution` | `produced-by` | 1905 | 十月总罢工和革命压力迫使沙皇签署宣言 | `EVT-1905-revolution` |
| `EVT-1905-12-moscow-armed-uprising` | `followed-by-reaction` | 1905-12 | 宣言后的“自由五十天”以十二月起义及镇压收束 | `EVT-1905-12-moscow-armed-uprising` |
| `PER-stolypin` | `reconfigured-by` | 1906–1911 | 斯托雷平政府利用紧急立法并促成六三选举改制 | `PER-stolypin`; `CLM-manning-1982-june-third-coup-social-basis` |
| `POL-stolypin-agrarian-reform` | `enabled-by` | 1906–1917 | 1906年土地敕令以第87条为程序基础，后经立法机关处理 | `POL-stolypin-agrarian-reform` |
| `DEB-1906-stolypin-wager-and-agrarian-viability` | `related-debate` | 1906–1917 | 第87条土地敕令与农业前景之争 | 争鸣卡 |
| `DEB-1914-haimson-thesis-stability` | `debated-in` | 1907–1914 | 杜马制度的适应能力与社会冲突是否趋于失控存在争议 | 争鸣卡 |

### 2.3 史学争鸣光谱
- **韦伯的“伪立宪主义”**：韦伯在1906年分析形式上的立宪转变与皇权、官僚和社会权力延续之间的裂缝；这是当时的诊断，不能直接当作对后续全部杜马运作的经验总结。站内仅有二手阐释（Pipes 1955），韦伯1906年原文标题待补。
- **海姆森的双重极化**：其社会史解释关注工人与有产社会、社会与专制国家之间的紧张，认为战前工潮表明稳定脆弱；罢工高潮本身并不能证明革命在1914年已不可避免（见 `DEB-1914-haimson-thesis-stability` 矩阵）。
- **Pipes的自由派政治史**：承认1907年选举法违反根本法，但这不等于取消杜马立法权（站内 L2 E03 L10 年表据Pipes）；与 `DEB-1914` 矩阵中Hogan／Bonnell等具名条目对读，可把匿名的“渐进演进”解释落实为具名学者，但这种反事实前景必须面对不平等选举、内阁不负责以及宫廷多次绕开议会的限制。
- **Manning的缙绅右翼**：[`CLM-manning-1982-june-third-coup-social-basis`](../../historiography/claims/CLM-manning-1982-june-third-coup-social-basis.md) 与 [`CLM-manning-1982-gentry-fronde-to-reaction`](../../historiography/claims/CLM-manning-1982-gentry-fronde-to-reaction.md) 揭示选举重组背后的地主政治联盟。
- **尚缺视角**：苏联—列宁派（宣言为策略性让步）与君主右翼评价站内尚未建卡；Lenin 1905年策略文献写于宣言之前，只可作策略语境，不可当宣言评论。

## 2. 一跳邻域全量微摘要目录 (去重后共 11 个节点，0 截断)
- **`EVT-1905-revolution`**（1905–1907年俄国第一次革命）: 1905年1月9日[O.S.]“血腥星期日”至1907年6月3日[O.S.]六三新选举法间的帝俄首次全民革命。涵盖十月总罢工、彼得堡苏维埃、水兵哗变、莫斯科起义与黑土区农村暴动；迫使沙皇颁布《十月宣言》与杜马体制，随革命退潮，有限代议制度保留并受保守选举法约束。 ‖ `→POL-october-manifesto-and-1906-fundamental-laws`[forced_concession_and_containment|1905.10–1906.04]: 十月罢工逼出公民自由承诺与立法杜马，1906年《国家根本法》则以皇室保留特权、两院制和第87条框定其边界 ； `←POL-october-manifesto-and-1906-fundamental-laws`[produced-by|1905]: 十月总罢工和革命压力迫使沙皇签署宣言
- **`INS-state-duma-1906-1917`**（俄罗斯帝国国家杜马（第一至第四届））: 1905年革命使君主制接受立法性国家杜马，但1906年基本法仍保留皇帝任免政府、解散杜马与紧急立法权。头两届因土地与政治责任问题短命；1907年选举法后第三、四届趋保守。1915年进步同盟施压，1917年二月杜马临时委员会参与接管政权，须与苏维埃共析。 ‖ `→POL-october-manifesto-and-1906-fundamental-laws`[constituted_and_limited_by|1906–1917]: 杜马享有立法参与权，君主与上院仍有关键否决及行政权 ； `←POL-october-manifesto-and-1906-fundamental-laws`[created-and-reshaped|1906–1917]: 宣言承诺的立法同意权经根本法落实为杜马；1907年选举法重组后形成第三、四届杜马
- **`ORG-octobrists-and-progressive-bloc`**（十月十七日同盟与进步同盟）: 1905年十月宣言后形成的十月十七日同盟是拥护君主立宪的温和自由主义政党；1915年的进步同盟是跨党派杜马联盟，二者并非同一组织。两者既要求改善政府与社会关系，又忧惧群众革命；1917年部分杜马领袖成为临时政权支点，却不能独掌街头、军队与苏维埃。 ‖ `→POL-october-manifesto-and-1906-fundamental-laws`[founding-document|1905–1906]: 十月党以宣言为政治起点 ； `←POL-october-manifesto-and-1906-fundamental-laws`[named-after-manifesto|1905–1917]: 十月党以宣言命名，接受其为立宪底线，为第三、四届杜马多数力量之一
- **`PER-witte`**（谢尔盖·维特）: 帝俄财政大臣（1892–1903）暨首任统一大臣会议主席（1905.10–1906.04）。主持铁路国有化、1897年金本位及外资驱动的重工业化，引发农业税负与官僚派系之争；1905年签《朴茨茅斯和约》并促成《十月宣言》，借镇压与22.5亿法郎国际借款缓解皇室即时财政压力。 ‖ `→POL-october-manifesto-and-1906-fundamental-laws`[co_architect_of|1905.10–1906.04]: 推动 1905-10-17 [O.S.] 宪政退却文本，并在离任前参与1906年《国家根本法》框架定型与财政过渡 ； `←POL-october-manifesto-and-1906-fundamental-laws`[architect|1905]: 维特主张以宣言和统一政府应对革命危机，最终由皇帝签署
- **`PER-nicholas-ii`**（尼古拉二世）: 末代沙皇（1894–1917在位），固守东正教君权与家产制专制。1905年经历血腥星期日，被迫签署《十月宣言》；1915年赴莫吉廖夫兼任最高统帅，宫廷趋于孤立。1917-03-02[O.S.]/03-15[N.S.]在普斯科夫退位，1918-07-17于叶卡捷琳堡被处决。 ‖ `←POL-october-manifesto-and-1906-fundamental-laws`[signed-and-reserved-autocratic-powers|1905–1917]: 签署宣言，又在1906年根本法中保留“最高专制权力”称号、任免与军政大权
- **`ORG-kadets`**（立宪民主党（卡德特党））: 1905年10月从解放同盟诞生的俄国自由主义核心政党，主张四尾制宪、有偿征地与议会道路，曾主导前两届杜马与战时进步同盟。1917年二月主导首届临时政府并切断对杜马从属关系，旋因战争、土地危机及科尔尼洛夫事件退阁丧失民心，十月后被定为“人民公敌”并在内战与流亡中分裂。 ‖ `←POL-october-manifesto-and-1906-fundamental-laws`[liberal-centrist-reaction|1905–1917]: 立宪民主党以杜马为中心参与政治，宣言与根本法的不足是其反对与受挫的背景
- **`PER-milyukov`**（帕维尔·米留可夫）: 俄国历史学家、卡德特党核心领袖（1859–1943）。主持解放同盟确立四尾制宪与有偿征地纲领；一战任进步同盟舵手，1916年发表“愚蠢还是叛国”演说；1917年任首届临时政府外长，03-03/03-16架空杜马，因04-18[O.S.]/05-01[N.S.]照会下野，流亡提“新策略”。 ‖ `←POL-october-manifesto-and-1906-fundamental-laws`[leading-liberal-critic|1905–1917]: 立宪民主党领袖，对宣言兑现程度与杜马权限作政治评估
- **`PER-guchkov`**（亚历山大·伊万诺维奇·古契科夫）: 十月十七日同盟领袖、第三届杜马前议长与战时军事工业委员会负责人。1917年他同舒尔金赴普斯科夫接收尼古拉二世退位文书，出任临时政府陆海军部长；军队权威危机和四月政治危机中辞职。战前宫廷政变计划真实存在，但未实际发动，不能将其当作二月起义的成熟指挥方案。 ‖ `←POL-october-manifesto-and-1906-fundamental-laws`[octobrist-leader|1905–1917]: 十月党领袖，体现拥护宣言的温和右翼自由派路线
- **`EVT-1905-12-moscow-armed-uprising`**（1905年12月莫斯科武装起义与普列斯尼亚街垒战）: 1905-12-07至12-18[O.S.]/12-20至12-31[N.S.]，莫斯科总罢工转为巷战。铁路未断使谢苗诺夫近卫团得以增援，重炮镇压普列斯尼亚，全城估死千人。败局引发普列汉诺夫反对起兵、列宁要求坚决进攻、托洛茨基强调争夺军队的战略分歧。 ‖ `←POL-october-manifesto-and-1906-fundamental-laws`[followed-by-reaction|1905-12]: 宣言后的“自由五十天”以十二月起义及镇压收束
- **`PER-stolypin`**（彼得·斯托雷平）: 帝俄内务大臣（1906–1911）暨大臣会议主席（1906.07–1911.09）。以野战法庭与1907年六三选举法平定革命余波，借土地法令允许农户脱社确权、培植私有小农；1911年3月因西部六省地方自治法案第87条危机失势，同年9月在基辅遇刺，成为晚期的改革路径争议核心。 ‖ `←POL-october-manifesto-and-1906-fundamental-laws`[reconfigured-by|1906–1911]: 斯托雷平政府利用紧急立法并促成六三选举改制
- **`POL-stolypin-agrarian-reform`**（斯托雷平土地改革）: 1906年起，斯托雷平政府试图通过农户份地私有化、土地整理、农民银行贷款和移民，创造较自主的农民经营者并稳定农村。退出重分村社、确权、合并土地和迁居独立农庄是不同步骤，成功率及地区差异很大。大战减缓实施，1917年土地革命中许多分离土地重新进入村社分配；改革并未消除农民的土地渴求。 ‖ `←POL-october-manifesto-and-1906-fundamental-laws`[enabled-by|1906–1917]: 1906年土地敕令以第87条为程序基础，后经立法机关处理 ； `→POL-october-manifesto-and-1906-fundamental-laws`[authorized-under|1906]: 首次敕令借第87条休会立法，后续正式法律须区分

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 3 项)
- **`DEB-1914-haimson-thesis-stability`**（海姆森命题：战前俄国的社会稳定与双重极化 | `historiography/debates/DEB-1914-haimson-thesis-stability.md` | 流派 `urban-polarization, labor-social-history, elite-political-history, liberal-institutional-and-contingent, crisis-and-war`）：一战前的工业增长、土地改革与杜马政治，能否使帝国逐步稳定，还是工人与有产社会、社会与专制国家的双重极化已侵蚀统治基础？1912年后罢工回升和改革受阻如何与战争冲击相互作用，须区分可观察的危机与无法验证的无战争反事实及其解释限度。
- **`DEB-1906-stolypin-wager-and-agrarian-viability`**（村社生命力与斯托雷平土改前景之争 | `historiography/debates/DEB-1906-stolypin-wager-and-agrarian-viability.md` | 流派 `modernization-optimism, peasant-social-history, marxist-agrarian-roads`）：如果没有世界大战，帝俄能否借私有农户与农业增长和平化解农村革命？争议同时涉及生产效率、村社制度的适应力与政治稳定，任何一项的改善都不能自动证明另外两项。反事实命题不能由改革中断的事实直接证成或证伪。
- ⚠️ 引用了尚未创建的争鸣卡 `DEB-1914`

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 15/15 条)
- **`CLM-manning-1982-june-third-coup-social-basis`** [`SCH-manning-roberta`(罗伯塔·T·曼宁) | pp. 238–239]: 
- **`CLM-manning-1982-gentry-fronde-to-reaction`** [`SCH-manning-roberta`(罗伯塔·T·曼宁) | pp. 54–60, 122–124]: 
- **`CLM-steinberg-2017-continuum-of-crisis-1905-1921`** [`SCH-steinberg-mark`(马克·D·斯坦伯格) | pp. 19, 61–62, 107–108]: 
- **`CLM-bonnell-1983-1912-1914-union-and-insurance-boards-bolshevik-capture`** [`SCH-bonnell-victoria`(维多利亚·E·邦内尔) | Book pp. 366–371, 390–438 [PDF pp. 389–394, 413–461]]: 
- **`CLM-bonnell-1983-state-employer-repression-undermining-menshevik-reformism`** [`SCH-bonnell-victoria`(维多利亚·E·邦内尔) | Book pp. 292–305, 316–323, 336–352, 372–389, 450–452 [PDF pp. 315–328, 339–346, 359–375, 395–412, 473–475]]: 
- **`CLM-hogan-1994-petersburg-metalworkers-1905-to-lena`** [`SCH-hogan-heather`(希瑟·霍根 · labor-social-history) | pp. 85–112]: 
- **`CLM-smith-sa-1996-petersburg-bolshevik-vs-menshevik-worker-appeal`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | International Review of Social History, vol. 41 (1996), pp. 12–15, 19–25]: 
- **`CLM-hildermeier-2000-azev-affair-and-stolypin-era-paralysis`** [`SCH-hildermeier-manfred`(曼弗雷德·希尔德迈尔) | EPUB版无稳定原书页码；以本地章节与行号定位（ch14 L24–91, ch18 L112–150, ch22 L6–108, ch23 L81–217, ch24 L8–285, ch25 L6–33, ch26 L6–62；epub:main-14.xhtml, main-23.xhtml, main-24.xhtml, main-25.xhtml, main-26.xhtml, main-27.xhtml）]: 
- **`CLM-pipes-1990-patrimonial-state-and-intelligentsia`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 2 (Official Russia); ch. 4 (The Intelligentsia); cf. Introduction]: 
- **`CLM-gaida-2003-progressive-bloc-dilemma`** [`SCH-gaida-fedor`(费奥多尔·盖达) | pp. 135-136, 162-168]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-yao-hai-1917-modernization-rupture-and-plebeian-radicalism`** [`SCH-yao-hai`(姚海) | [PDF pp. 47-55, 57-64, 68-72, 75-81, 87-88]]: 
- **`CLM-figes-1996-peasant-moral-economy-1917`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 343-352]: 
- **`CLM-hildermeier-2000-agrarian-socialism-modernization-dilemma`** [`SCH-hildermeier-manfred`(曼弗雷德·希尔德迈尔) | EPUB版无稳定原书页码；以本地章节与行号定位（ch08 L75–232, ch09 L26–44, ch12 L204–282, ch13 L107–185, ch17 L115–310, ch20 L750–753, ch24 L180–285, ch26 L6–96；epub:main-8.xhtml, main-9.xhtml, main-12.xhtml, main-13.xhtml, main-21.xhtml, main-25.xhtml, main-27.xhtml）]: 
- **`CLM-service-lenin-v1-agrarian-marxism-and-1905-tactics`** [`SCH-service-robert`(罗伯特·瑟维斯) | pp. 74-80, 152-166, 169-185 (中译本 PDF 页码)]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
