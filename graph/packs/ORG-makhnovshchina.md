# 1-Hop 平衡上下文包：`ORG-makhnovshchina` (马赫诺运动（乌克兰革命起义军）)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/organizations/ORG-makhnovshchina.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `military-structural-mawdsley, comparative-rebellion-hobsbawm, anarchist-avrich, soviet-official-banditry`
- **待补齐视角**: `makhno-memoir-vs-archive, german-mennonite-village-perspective`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `makhno-memoir-vs-archive, german-mennonite-village-perspective`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1918–1921年南俄乌克兰无政府共产主义农民—雇农武装：以古利亚伊波列为基地设“自由苏维埃”与公社，以机枪马车（тачанка）机动战术三度联红击白；红军背盟后于1921年覆灭。史学上既是内战地方变体，也是农民反叛与现代政党夺权模式的经典对照案例。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **起源与古利亚伊波列公社集群（1918）**：中央拉达与德奥占领撤走后，涅斯托尔·马赫诺（Nestor Makhno）在**古利亚伊波列（Huliaipole）**组织雇农与贫农夺取地主庄园，建立地方苏维埃与集体农庄实验，拒斥“都市政治病毒”却仍自称苏维埃框架（Hobsbawm 附录；Mawdsley 南俄战线）。这一时期运动亦称 **Махновщина**。
- **黑军、тачанка 与三方回旋（1918–1920）**：起义军改编为 **乌克兰革命起义军（РПАУ，“黑军”）**，以马匹拖拽机枪车的 **тачанка（机枪马车）** 在乌克兰东南部第聂伯河左岸黑土草原实现高机动突袭。`1918–1919` 先后抗击德奥占领军、彼得留拉督政府与白军；1919年秋邓尼金进逼莫斯科最危急时刻，马赫诺突破白军后方防线连克梅利托波尔、别尔江斯克、叶卡捷琳诺斯拉夫，迫使邓尼金抽调前线精锐回援（`CLM-mawdsley-1987-white-movement-structural-defeat`）。`1920` 年夏马赫诺断然拒绝并处决弗兰格尔派来的求盟使者，于同年 10 月与红军签订《斯塔罗别利斯克政治与军事协定》结盟，派主力协同红军强渡锡瓦什海湾攻克克里米亚击败弗兰格尔；11 月下旬克里米亚战事甫定，红军南方面军司令 **伏龙芝（M. V. Frunze）** 即下令背盟围剿黑军。
- **“要苏维埃，不要共产党人”与终结（1920–1921）**：口号反映对苏维埃机构形式与布尔什维克一党专政的区分（对比 `CLM-avrich-1970-soviets-without-bolsheviks` 论喀琅施塔得口实差异）。`1921` 年夏红军仆从战线恢复粮食征发与契卡镇压，黑军在罗马尼亚边境覆灭，马赫诺流亡巴黎（`1921-08` 前后）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `EVT-1918-1920-russian-civil-war` | `regional-belligerent` | 1918–1921 | 南乌克兰独立武装同时对抗白军、外军与红军征粮机器 | `CLM-mawdsley-1987-civil-war-militarized-regime` |
| `EVT-1920-1921-tambov-and-peasant-revolts` | `parallel-peasant-war` | 1920–1921 | 与坦波夫等农民抗征构成反战时共产主义农民战争弧，但以无政府共产主义公社与自由苏维埃为独特纲领标志 | `CLM-hobsbawm-1959-archaic-peasant-rebellion-vs-modern-party` |
| `POL-war-communism` | `resisted` | 1919–1921 | 拒斥余粮收集制与契卡恐怖，迫使红军暂与叛军妥协 | Mawdsley; Hobsbawm |
| `ORG-cheka-ogpu` | `repressed` | 1920–1921 | 与红军协同后翻脸，契卡系统清剿南俄无政府据点 | `CLM-leggett-1981-red-terror-institutionalization` |
| `PER-frunze` | `final-campaign-commander` | 1920–1921 | 红军南方面军司令伏龙芝于克里米亚战役后下令围剿黑军 | `sources/monographs/mawdsley_1987_civil_war_zh/` ch15–ch16 |
| `CON-soviet` | `reclaimed-signifier` | 1918–1921 | 以“自由苏维埃”反设布尔什维克党中央苏维埃模式 | Avrich; Hobsbawm |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1918–1921年南俄存在以马赫诺为核心的较大规模农民—雇农武装；多次与红军结盟又决裂；1921年被消灭；采用高度机动的 тачанка（tachanka，机枪马车）战术与地方自由苏维埃自治实验。
- **主要解释分歧**：
  - **[白军结构性失败论中的马赫诺变量 / Evan Mawdsley]** (`CLM-mawdsley-1987-white-movement-structural-defeat`, `CLM-mawdsley-1987-civil-war-militarized-regime`)：马赫诺对邓尼金后方补给线的打击是1919年白军失败关键因素之一；同时强调红军最终凭劳动力与政治组织优势再造国家机器。
  - **[“前政治”农民反叛 vs 先锋党 / Eric Hobsbawm]** (`CLM-hobsbawm-1959-archaic-peasant-rebellion-vs-modern-party`)：马赫诺运动是原始农民社会反叛与现代革命政党冲突的典型案例，注定败于有纪律政治组织——理论框架强势，需与乌克兰地方社会史材料对勘以免过度类型化。
  - **[无政府主义与苏维埃口号策略 / Paul Avrich]** (`CLM-avrich-1970-soviets-without-bolsheviks`)：“要苏维埃不要共产党人”口号在南俄与西伯利亚农民起义中出现，与喀琅施塔得水兵口号源流不同，须分语境。
  - **[苏联正统“匪帮化”叙事]**：官方史学将马赫诺定性为富农–土匪联盟，80–90年代后档案研究强调征粮、自卫与民族—土地复合动因（本地 `sources/monographs/mawdsley_1987_civil_war/` 与乌克兰社会史待深化）。

## 2. 一跳邻域等权重微摘要 (共 7 个关联节点，严防大卡霸占上下文)
### 邻居节点: `EVT-1918-1920-russian-civil-war`
- **时效关系边** (`ORG-makhnovshchina` → `EVT-1918-1920-russian-civil-war` | `black-army-swing-force` | 有效时段: `1918-1921`): 以机枪马车高机动游击战重创邓尼金战略后方并助红军攻克克里米亚，旋即遭苏维埃政权清剿覆灭。
- **节点定性微摘要 [T1]** (完备度 `draft`): 1918–1920年苏俄内战：布尔什维克依托“苏托邦”人口、军火与莫斯科铁路枢纽内线机动，先后粉碎高尔察克、邓尼金、弗兰格尔白军及马赫诺黑军，并压制社革党第三力量；协约国干涉与边疆民族武装相互牵制。

### 邻居节点: `PER-makhno`
- **时效关系边** (`PER-makhno` → `ORG-makhnovshchina` | `founder-commander` | 有效时段: `1918-1921`): 在乌克兰东南部创立无政府共产主义农民起义军，三度与红军结盟重创邓尼金与弗兰格尔白军后遭苏维埃政权消灭。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 乌克兰古利亚伊波列无政府共产主义农民统帅（1888–1934）。创建“革命起义军（黑军）”与自由苏维埃实验；内战中与红军多次合作、破裂，1919年秋破袭邓尼金后方，1920年11月其部队参加克里米亚战役，随即遭红军全面围剿，1921年越境流亡并客居巴黎。

### 邻居节点: `EVT-1920-1921-tambov-and-peasant-revolts`
- **时效关系边** (`ORG-makhnovshchina` → `EVT-1920-1921-tambov-and-peasant-revolts` | `parallel-peasant-war` | 有效时段: `1920–1921`): 与坦波夫等农民抗征构成反战时共产主义农民战争弧，但以无政府共产主义公社与自由苏维埃为独特纲领标志
- **节点定性微摘要 [T1]** (完备度 `draft`): 1920–1921年坦波夫等地农民反抗余粮征集，亚历山大·安东诺夫组建准正规“绿军”，口号含“苏维埃政权不要共产党人”；图哈切夫斯基执掌坦波夫省剿匪部队司令部（作战集团约10万正规军）与契卡人质手段镇压，与喀琅施塔得一并倒逼1921年十大与实物税转向。

### 邻居节点: `POL-war-communism`
- **时效关系边** (`ORG-makhnovshchina` → `POL-war-communism` | `resisted` | 有效时段: `1919–1921`): 拒斥余粮收集制与契卡恐怖，迫使红军暂与叛军妥协
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1918年夏至1921年3月苏维埃经济政策总称：余粮收集制、中小工业国有化、取缔私商、货币贬值与实物配给并举；因内战饥荒与国家能力崩溃而强化，却在1921年喀琅施塔得与坦波夫危机下为新经济政策实物税所取代；其性质是应急、乌托邦跃进还是国家统制传统延续，史家分歧剧烈。

### 邻居节点: `ORG-cheka-ogpu`
- **时效关系边** (`ORG-makhnovshchina` → `ORG-cheka-ogpu` | `repressed` | 有效时段: `1920–1921`): 与红军协同后翻脸，契卡系统清剿南俄无政府据点
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 苏俄与苏联早期政治警察机关（1917–1934），由捷尔任斯基创立。历经全俄肃反委员会（ВЧК，1917–1922）、国家政治保卫局（ГПУ，1922–1923）与国家政治保卫总局（ОГПУ，1923–1934）三阶段，从法外非常机构演变为直属政治局的常设宪制部门，执行红色恐怖与强制集体化。

### 邻居节点: `PER-frunze`
- **时效关系边** (`ORG-makhnovshchina` → `PER-frunze` | `final-campaign-commander` | 有效时段: `1920–1921`): 红军南方面军司令伏龙芝于克里米亚战役后下令围剿黑军
- **节点定性微摘要 [T1]** (完备度 `draft`): 米哈伊尔·伏龙芝（1885–1925），内战红军名将：1919年东线击溃高尔察克，1920年南线攻克弗兰格尔克里米亚；1923年十二大迫斯大林民族政策让步，1924–1925主持军事改革接替托洛茨基，1925年10月手术后猝死。

### 邻居节点: `CON-soviet`
- **时效关系边** (`ORG-makhnovshchina` → `CON-soviet` | `reclaimed-signifier` | 有效时段: `1918–1921`): 以“自由苏维埃”反设布尔什维克党中央苏维埃模式
- **时效关系边** (`CON-soviet` → `ORG-makhnovshchina` | `自由苏维埃口号` | 有效时段: `1918–1921`): 提出“拥护苏维埃、反对共产党”的非党苏维埃实践。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 苏维埃原为会议或委员会之意。1905年工人代表机构从罢工协调走向政治权力雏形；1917年工兵农苏维埃成为多党竞争与双重政权场域。十月后1918年宪法确立城乡五比一不等权与阶级剥权机制，二十年代“活跃苏维埃”实验仍受制于一党垄断，1921年喀琅施塔得亦曾诉诸苏维埃民主。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1918-war-communism-ideology-or-emergency`：战时共产主义与早期一党制本质之争：内战应急、乌托邦跃进还是国家统制连续？
## [T1] 核心问题定义
1918–1921年的全面工业国有化、余粮收集制（`продразвёрстка`）、取缔私商、劳动军事化及多党苏维埃向一党专政的收缩，究竟是内战与供给崩溃逼迫的生存应急反应，还是布尔什维克反市场乌托邦蓝图的激进兑现，抑或一战以来国家统制与基层危机交互演化的结果？“战时共产主义”系1921年新经济政策转向时的事后追赋标签，须严格区分措施出台序列与事后总结。

## [T2] 各学派立场对照矩阵

**经验共识**：1917年底至1918年春尚存布尔什维克—左翼社革党联合执政与“国家资本主义”探索；1918年夏起全面国有化与强制征粮随内战升级扩展；1920年达至劳动军事化与无货币幻想顶峰；1921年3月俄共十大在农村起义与喀琅施塔得危机下转向实物税（NEP）与党内派别禁令。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **内战军事应急与双元矛盾论** | E. H. Carr, *The Bolshevik Revolution*, Vol. 2 (1952); Evan Mawdsley, *The Russian Civil War* (1987) | 强调工业瓦解、封锁与300万红军补给迫使政权诉诸垂直“总局主义”与强制征粮；但Carr同时指出1920年后期确曾滋生把战时自然经济奉为直接通往共产主义捷径的意识形态幻象。 | `CLM-carr-1952-war-communism-internal-contradictions`; `CLM-mawdsley-1987-civil-war-militarized-regime`; `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` | 单靠军事紧急状态难以完全解释1920年底内战大局已定后为何仍出台小手工业全面国有化令。 |
| **意识形态乌托邦与废法专政论** | Martin Malia, *The Soviet Tragedy* (1994); Richard Pipes, *The Russian Revolution* (1990) | 认为消灭私有产权与市场交换本就是马克思主义核心诉求，内战只是扫除了渐进障碍、催化乌托邦跃进；Pipes强调契卡与排斥反对派早于大规模内战爆发。 | `CLM-pipes-1990-red-terror-leninist-logic`; `CLM-pipes-1990-october-classic-coup` | 易将不同阶段的应急妥协（如1918春列宁国家资本主义方案）回溯拉平为单一既定时间表。 |
| **战时国家统制连续与自下而上倒逼论** | Lars T. Lih; S. A. Smith, *Red Petrograd* (1983); David Hoffmann (2011) | 揭示沙皇与临时政府在一战中已启动粮食专卖与国家统制；Smith证明1917–1918春77%早期企业没收源自基层工厂委员会应对关厂危机的自下而上压力，而非中央乌托邦指令。 | `CLM-smith-sa-1983-defensive-workers-control`; `CLM-smith-sa-1983-from-workers-control-to-nationalization`; `CLM-hoffmann-2011-continuum-of-total-war-1914-1929` | 总体战技术连续性不能替代对布尔什维克消灭整个有产阶级政治权利之独特意识形态动力的解释。 |
| **复合危机、党内张力与农村社会钳制论** | Alexander Rabinowitch (2007); Robert V. Daniels (1960); Moshe Lewin (1968/1985) | 追踪布列斯特和约、左翼社革党决裂及左翼共产主义者/工人反对派论战如何一步步锁死多党与党内多元空间，同时揭示小农汪洋的反抗最终迫使政权在1921年退却但保留了战时强制记忆。 | `CLM-rabinowitch-2007-contingency-of-dictatorship`; `CLM-daniels-1960-left-communists-1918`; `CLM-figes-1996-peasant-wars-and-nep-retreat`; `CLM-zemskov-1929-dekulakization-demographic-baseline` | 首都与萨拉托夫、坦波夫、乌拉尔等外省的时间差与暴力烈度须结合地方档案（Raleigh、Churakov）细化。 |

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

## 4. 关联时间线锚点 (共 0 条)
