# 1-Hop 去重平衡上下文包：`POL-april-theses-1917`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`POL-april-theses-1917`** (《四月提纲：论无产阶级在这次革命中的任务》 | `cards/policies/POL-april-theses-1917.md` | `multi-perspective`): 已覆盖=`lenin-text-lih, party-moderates-loginov, eyewitness-sukhanov, bolshevik-grassroots-rabinowitch`；待补=`factory-committee-reception-polls, provincial-soviet-debates`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1917年4月列宁归国后提出的十项纲领：宣布不给临时政府任何支持、批判“革命护国主义”、主张从资产阶级革命第一阶段向工兵苏维埃掌权第二阶段过渡，并倡议没收地主土地实现全部土地国有化、全国银行合并受苏维埃监督与更改党名；打破加米涅夫—斯大林有条件支持临时政府路线，经党内激烈辩论逐步重塑布尔什维克战略。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **宣读与发表（1917.04.04–07 [O.S.] / 1917-04-17–20 [N.S.]）**：`1917-04-04 [O.S.] / 1917-04-17 [N.S.]` 列宁在出席全俄工兵苏维埃会议的布尔什维克代表会及布尔什维克—孟什维克联席会上宣读提纲；`1917-04-07 [O.S.] / 1917-04-20 [N.S.]` 《真理报》第26号刊出，编辑部声明仅代表列宁个人观点（S级：`sources/web-archive/E06_E10_turning_points/1917-04-04_april-theses.md`）。核心命题：**不给临时政府任何支持**；**全部政权归工人、士兵和雇农苏维埃**；革命正处在从第一阶段向第二阶段过渡（`CLM-loginov-lenin-vs-party-moderates-1917`）。
- **党内反弹与渐进吸收（1917.04–06）**：彼得格勒委员会 **`13:2:1`** 否决提纲；加米涅夫在《真理报》坚称革命仍是资产阶级民主革命，斯大林附和“有模式无事实”（`CLM-loginov-lenin-vs-party-moderates-1917`）。列宁在《论策略书》中批判“老布尔什维克档案”公式，四月会议后提纲要点逐步进入党决议，但未立即推翻苏维埃多数派的对外政策。
- **与七月、十月的张力（1917.07–10）**：七月危机中列宁要求放弃和平口号“全部政权归苏维埃”，主张在军事独裁与工人武装起义间抉择，扩大会议仍未接受（同上 CLM）。九月以来重新把苏维埃夺权与十月军事革命委员会实践衔接（`CLM-rabinowitch-1968-divided-bolshevik-party-july`, `CLM-loginov-lenin-early-synthesis-and-1917-strategy`）。提纲本身未规定武装起义日期，却设定了“不向临时政府委托信任”的道德—政治底线。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | `authored` | 1917.04 | 归国后以个人名义宣读，后转化为党的战略目标 | `1917-04-04_april-theses.md`; `CLM-loginov-lenin-vs-party-moderates-1917` |
| `PER-kamenev` | `opposed-then-qualified` | 1917.04–1917.10 | 批判提纲“越阶段”，十月前仍犹豫武装起义 | `CLM-loginov-lenin-vs-party-moderates-1917`, `CLM-sukhanov-1922-lenin-april-arrival-shock` |
| `PER-stalin` | `initially-cautious` | 1917.04 | 与加米涅夫一道守旧阶段论，四月后才左转 | `CLM-loginov-lenin-vs-party-moderates-1917` |
| `ORG-provisional-government` | `no-confidence` | 1917.04起 | 提纲第3条要求不给任何支持并揭露其兼并诺言 | S级提纲第3、7条 |
| `ORG-petrograd-soviet` | `power-destination` | 1917.04–1917.10 | 主张自下而上苏维埃共和国取代议会制 | 提纲第4–5条；`CLM-sukhanov-1922-lenin-april-arrival-shock` |
| `ORG-mensheviks` | `debated-against` | 1917.04 | 联席会上把列宁方案斥为巴枯宁式呓语 | `CLM-sukhanov-1922-lenin-april-arrival-shock` |
| `CON-permanent-revolution` | `strategic-convergence` | 1917.04起 | 界定第二阶段为向社会主义过渡，与不断革命论实践交汇但文本未点名托洛茨基 | `CON-permanent-revolution` 卡；`CLM-lih-2006-erfurtian-merger-formula` |
| `EVT-1917-10-october-revolution` | `strategic-prelude` | 1917.04–10 | “不给临时政府支持”底线为十月非委托信任夺权奠定合法性 | `DEB-1917-october-coup-or-social-revolution` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1917年4月列宁提出十项提纲；反对支持临时政府与革命护国主义；主张苏维埃掌权与向社会主义阶段过渡；党内初期遭遇强烈反对，后逐渐被布尔什维克吸收为战略方向。
- **主要解释分歧**（详参 `DEB-1917-october-coup-or-social-revolution`）：
  - **[党内民主与节奏论 / Vladlen Loginov]** (`CLM-loginov-lenin-vs-party-moderates-1917`, `CLM-loginov-lenin-early-synthesis-and-1917-strategy`)：提纲打破温和派路线，但列宁本人同时声明“不是布朗基主义者”，四月、七月、九月三次遭中央多数否决，反驳“列宁四月一来党即铁板一块”神话。
  - **[现场震惊与护国阵线 / Sukhanov]** (`CLM-sukhanov-1922-lenin-april-arrival-shock`)：亲历者记录士兵闻言欲用刺刀对付列宁、加米涅夫耸肩称“等着瞧”，《真理报》于4月7日[O.S.]刊出提纲全文后次日即由加米涅夫撰文公开声明编辑部认为列宁的总公式“令人无法接受”——突显四月提纲在左翼民主派与党内温和派眼中的突兀与震动。
  - **[草根吸收曲线 / Rabinowitch]** (`CLM-rabinowitch-1968-divided-bolshevik-party-july`, `CLM-rabinowitch-2007-contingency-of-dictatorship`)：工厂与驻军支部比中央委员会更快左转，七月分裂显示纲领传播并非自上而下灌输。
  - **[埃尔福特正统语境 / Lars T. Lih, Eric Blanc]** (`CLM-lih-2006-erfurtian-merger-formula`, `CLM-blanc-2021-revolutionary-kautskyanism-in-empire`)：反对把提纲说成突然改宗托洛茨基主义；列宁仍处考茨基式“合并公式”语义场，战时应变与苏维埃公式是俄国特殊条件下的战略重排。

## 2. 一跳邻域全量微摘要目录 (去重后共 10 个节点，0 截断)
- **`CON-dual-power`**（双重政权（两个政权并存））: 萌芽于1905年苏维埃；1917-03-02[O.S.]/03-15[N.S.]至七月事件，临时政府名义主权与彼得格勒苏维埃工兵实力、“有条件支持”并存。列宁四月称两类阶级专政交织，七月宣布终结，九月再提苏维埃夺权；修正史学强调多中心失序与双方虚弱。 ‖ `→POL-april-theses-1917`[theoretical-redefinition|1917-04-17 [N.S.]]: 列宁将双重政权定性为资产阶级政府与工农革命民主专政的交织，提出政权和平转归苏维埃
- **`MTG-1917-04-7th-april-party-conference`**（俄国社会民主工党（布尔什维克）第七次全国代表会议（四月会议））: 1917-04-24至04-29[O.S.]/05-07至05-12[N.S.]，布尔什维克四月会议以71:39:8通过列宁当前形势决议，拒绝信任临时政府，支持土地国有化与苏维埃夺权；但民族自决、中央规模及齐美尔瓦尔德会议问题上列宁遭多数反对，党内分歧鲜明。 ‖ `→POL-april-theses-1917`[debates_and_develops|1917年春]: 会议围绕提纲的政府、土地和政权方向讨论并形成决议，不等于照单逐条通过全文。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←POL-april-theses-1917`[authored|1917.04]: 归国后以个人名义宣读，后转化为党的战略目标 ； `→POL-april-theses-1917`[author|1917.04]: 返抵彼得格勒即抛出《四月提纲》，扭转国内布尔什维克温和路线，确立不给临时政府任何支持与“全部政权归苏维埃”的战略方向。
- **`PER-kamenev`**（列夫·加米涅夫）: 老布尔什维克、首任全俄中执委主席。1917年自四月至立宪会议一贯坚守温和宪政社会主义联盟路线并公开反对十月起义；1924年十三大联手季诺维也夫压下《列宁遗嘱》，1925年十四大公开发言反斯大林“领袖”集权后失势；1928年7月密会布哈林并留下外泄笔记，反成右派致命罪证。 ‖ `←POL-april-theses-1917`[opposed-then-qualified|1917.04–1917.10]: 批判提纲“越阶段”，十月前仍犹豫武装起义
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←POL-april-theses-1917`[initially-cautious|1917.04]: 与加米涅夫一道守旧阶段论，四月后才左转
- **`ORG-provisional-government`**（1917年俄国临时政府）: 1917年3月至11月俄国最高行政机关：由自由主义杜马派在李沃夫公爵主持下组成，宣称继承沙皇“全部政权”，却在工兵苏维埃与前线《第一号命令》制约下陷入土地、军队与和平三重困局；经四届内阁（李沃夫首届、五月至九月三次资产阶级—社会主义联立内阁及九月短期五人执政内阁）未能稳住宪政民主，终为十月起义推翻。 ‖ `←POL-april-theses-1917`[no-confidence|1917.04起]: 提纲第3条要求不给任何支持并揭露其兼并诺言
- **`ORG-petrograd-soviet`**（彼得格勒工兵代表苏维埃）: 二月革命后诞生于塔夫利达宫的工兵政权，颁布《第一号命令》。执委会主席为齐赫伊泽，策烈铁里是常务局核心并主导革命护国路线。1917-08-31[O.S.]/09-13[N.S.]首次通过布尔什维克决议，托洛茨基随后任主席；十月军事革命委员会成为推翻临时政府的枢纽。 ‖ `←POL-april-theses-1917`[power-destination|1917.04–1917.10]: 主张自下而上苏维埃共和国取代议会制
- **`ORG-mensheviks`**（孟什维克）: 俄国社会民主主义政党（1903–1924），源于1903年二大马尔托夫等与列宁围绕党章第一条及集中制的决裂，主张开放型群众政党与工人自主活动。1917年分化为策烈铁里、但恩主导的入阁“革命护国派”与马尔托夫领导的反战“国际主义派”；十月后开展苏维埃合法反对派抗争，1921年后遭取缔。 ‖ `←POL-april-theses-1917`[debated-against|1917.04]: 联席会上把列宁方案斥为巴枯宁式呓语
- **`CON-permanent-revolution`**（不断革命论）: 源于马克思1850年通告，1905–1906年帕尔乌斯与托洛茨基发展为无产阶级夺权并联动欧洲革命之论，与列宁“工农民主专政”相异。1917年《四月提纲》与托氏入党、十月夺权，被Deutscher解释为实践合流，学界有异议；1924年后被定为“低估农民”的托派异端。 ‖ `←POL-april-theses-1917`[strategic-convergence|1917.04起]: 界定第二阶段为向社会主义过渡，与不断革命论实践交汇但文本未点名托洛茨基
- **`EVT-1917-10-october-revolution`**（1917年十月革命）: 1917年10月24—27日（俄历；公历11月6—9日），军事革命委员会夺取彼得格勒中枢，冬宫陷落，苏维埃二大通过和平、土地法令并建立人民委员会。群众激进化、组织夺权与多党联合失败交织；首都迅速接管不代表全国无血革命。 ‖ `←POL-april-theses-1917`[strategic-prelude|1917.04–10]: “不给临时政府支持”底线为十月非委托信任夺权奠定合法性

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

### `DEB-1917-dual-power-and-february-origins`：二月革命起源与“双重政权”宪制形成之争（1917）
## [T1] 核心问题定义
二月革命是无领导的群众爆发，还是工厂与兵营中分散的积极分子推动的起义？沙皇退位后，杜马临时委员会、苏维埃与临时政府如何谈判并形成彼此制约的权力格局？群众压力、精英选择和战时危机的因果权重仍有争议，不能以宫廷阴谋代替街头革命。

## [T2] 各学派立场对照矩阵
**经验基准**：1917-02-23 [O.S.] / 1917-03-08 [N.S.] 国际妇女节罢工扩大；27日 [O.S.] / 3月12日 [N.S.] 首都预备营哗变，国家杜马临时委员会与彼得格勒工兵代表苏维埃在塔夫利达宫东西两翼同日成立；3月1日 [O.S.] / 3月14日 [N.S.] 苏维埃发布《第一号命令》；3月2日 [O.S.] / 3月15日 [N.S.] 尼古拉二世在普斯科夫退位并传位米哈伊尔大公；3月3日 [O.S.] / 3月16日 [N.S.] 米哈伊尔大公签署《拒绝即位宣言》（将最高政权形制交由普选立宪会议决定并呼吁服从临时政府），同日临时政府举行首次内阁会议。各机构的正式法统主张与实际暴力和行政控制力并不重合。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 社会史、次精英网络与2018年宪制自我修正 | Tsuyoshi Hasegawa, *The February Revolution: Petrograd, 1917* (1981; rev. ed. 2018) | 街头起义既非纯粹盲目自发也非布尔什维克中央指挥，而是跨党派工厂与兵营“中下层积极分子（sub-elite activists）”在各党上层犹豫时串联引爆；2018年新版更推翻自己1981年“杜马自由派系不情愿革命者”旧论，证明杜马临时委员会先于苏维埃建立军事委员会、于2月27日晚11:30主动夺权，且“双重政权”并非苏维埃自愿让权（苏维埃并无国家行政机器可让），而是米留可夫在3月3日首次内阁会议上蓄意废黜国家杜马、自断民选法统后，反使强势临时政府沦为需仰赖虚弱苏维埃合法性的无根政权。 | `CLM-hasegawa-2018-sub-elite-activists`；`CLM-hasegawa-2018-duma-committee-revision`；`CLM-hasegawa-2018-dual-power-origins` | 高度聚焦首都彼得格勒五日决战，对外省政权接收与农村公社反应需结合地方档案补充。 |
| 自由派困境与“叹着气的革命者” | Fedor Gaida, *Liberal Opposition in Russia, 1914–1917* (2003) | 与Hasegawa 2018年版针锋相对：论证杜马自由派缺乏基层组织，在二月并非胸有成竹的主动夺权者，而是因畏惧沙皇军法审判与街头暴民清洗才仓促接权的“叹着气的革命者／革命的俘虏”；二月获胜的不是作为立宪机构的第四届杜马，而是作为群众集会物理场所的塔夫利达宫，这一事实同样从档案层面直接证伪了“自由派预先策划二月革命”的阴谋论。 | `CLM-gaida-2003-liberals-in-february-1917` | 偏重杜马自由派上层书信与内阁心态，不能单独解释2月27日驻军哗变的兵营微观动因。 |
| 当事人夜间妥协见证（B级文献） | N. N. Sukhanov, *The Russian Revolution, 1917* (1922) | 以苏维埃执委会亲历者视角记录3月1–2日夜与米留可夫、古契科夫的谈判：苏维埃多数派因惧怕“资产阶级退缩导致军事反革命镇压”，以“不入阁、有条件支持、保留士兵控制权”达成双重政权契约。 | `CLM-sukhanov-1922-dual-power-pact` | 属B级当事人回忆录，兼具在场见证与孟什维克国际派事后自我辩护，须与双方会议速记互证。 |
| 革命马克思主义阶级主权论（B级文献） | Leon Trotsky, *History of the Russian Revolution* (1930–32) | 将双重政权界定为一切伟大革命中“两个不可调和统治阶级（资产阶级与无产阶级/兵农）分掌正式政权与实际武装”的过渡性主权分裂，断言其内在结构不稳定性必然通向十月二次革命或反革命专政。 | `CLM-trotsky-1930-dual-power-instability` | 属B级十月领导人事后理论化，将二月的多党协商张力嵌入通向十月布尔什维克夺权的目的论轨道。 |
| 孟什维克“革命护国主义”与联合政府陷阱 | Ziva Galili, *The Menshevik Leaders in the Russian Revolution* (1989) | 第二章从粮食与铁路技术依赖、对失控“士兵革命”的疑虑及工人反专政心理正面解释3月初双重政权的诞生；随后以“革命护国主义”和5月入阁解释苏维埃社会权威与联合政府行政责任之间的致命撕裂。 | `CLM-galili-1989-revolutionary-defensism`；`CLM-galili-1989-coalition-government-trap` | 5月以后的联合政府危机属双重政权中后期演变，应与2月底3月初的政权创生机制分段考察。 |
| 精英宫廷阴谋论及其社会史反证 | 叶夫根尼·斯皮岑（E. Yu. Spitsyn）《俄罗斯帝国与苏联通史》第3卷（B级新传统主义综合）；Orlando Figes, *A People's Tragedy* (1996) | 斯皮岑渲染军方高层、杜马自由派与协约国驻俄使团的“精英倒沙皇阴谋”；Figes（注：所引论断卡主论3月《第一号命令》后至10月的军纪瓦解、社会等级逆转与“战壕布尔什维主义”）与Hasegawa、Fedor Gaida共同证明基层士兵拒绝向人群开火及社会反威权爆发具有完全独立于精英接触的动力。 | `CLM-spitsyn-february-1917-elite-conspiracy-thesis`；`CLM-figes-1996-soldier-mutiny-and-social-inversion` | 上层倒沙皇接触或普斯科夫劝退绝不等于指挥2月23–27日街头罢工与预备营哗变；混淆精英善后与起义命令链违反证据等级铁律。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/36 条)
- **`CLM-loginov-lenin-vs-party-moderates-1917`** [`SCH-loginov-vladlen`(弗拉德连·洛吉诺夫) | pp. 145-146, 165-167, 265, 272-273, 340-343, 527-528]: 
- **`CLM-rabinowitch-1968-divided-bolshevik-party-july`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | PDF pp. 12, 17, 79, 86-94, 121-123]: 
- **`CLM-loginov-lenin-early-synthesis-and-1917-strategy`** [`SCH-loginov-vladlen`(弗拉德连·洛吉诺夫) | 第一部 ch02-ch04（EPUB ch003-ch005：#L231-L391, #L140-L256, #L20-L45）；第二部 ch07（EPUB ch008：#L442-L527, #L610-L621, #L867-L885, #L1025-L1062, #L1403-L1434, #L1739-L1765）]: 
- **`CLM-sukhanov-1922-lenin-april-arrival-shock`** [`SCH-sukhanov-nikolai`(尼古拉·苏汉诺夫) | pp. 269–292 (PDF pp. 317–340)]: 
- **`CLM-lih-2006-erfurtian-merger-formula`** [`SCH-lih-lars`(拉斯·T·利) | pp. 6-9, 41-49, 74-106, 113-121, 556-557]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-blanc-2021-revolutionary-kautskyanism-in-empire`** [`SCH-blanc-eric`(埃里克·布兰克) | pp. 25–28, 569–578]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-rabinowitch-1976-open-democratic-mass-party`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-rabinowitch-1976-october-three-factions-debate`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-rabinowitch-1976-trotsky-soviet-congress-strategy`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-loginov-lenin-1917-fleeting-window-of-power`** [`SCH-loginov-vladlen`(弗拉德连·洛吉诺夫) | pp. 523-524, 531-532, 560-561, 621-622, 656-658]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-koenker-1981-moscow-october-armed-struggle-vs-petrograd`** [`SCH-koenker-diane`(黛安·P·科恩克尔) | pp. 329–355 (local PDF pp. 345–371); p. 366 (PDF p. 382)]: 
- **`CLM-koenker-1981-rational-incremental-radicalization`** [`SCH-koenker-diane`(黛安·P·科恩克尔) | pp. 359–363 (local PDF pp. 375–379); p. 254 (PDF p. 270)]: 
- **`CLM-basil-1984-october-and-vikzhel-collapse`** [`SCH-basil-john`(约翰·D·巴兹尔) | pp. 165–175（本地 PDF 同号）]: 
- **`CLM-yao-hai-post-october-coalition-failure-and-one-party-formation`** [`SCH-yao-hai`(姚海) | [PDF pp. 532-535, 543-569]]: 
- **`CLM-yao-hai-constituent-assembly-vs-soviet-legitimacy-clash`** [`SCH-yao-hai`(姚海) | [PDF pp. 574-596]]: 
- **`CLM-rabinowitch-2007-constituent-assembly`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 88-91, 105-110, 121-127]: 
- **`CLM-trotsky-1930-art-of-insurrection-and-soviet-legality`** [`SCH-trotsky-leon`(列夫·达维多维奇·托洛茨基 · participant-historian) | （中译 EPUB 无纸页；第三卷第二十—二十一章）]: 
- **`CLM-sukhanov-1922-october-walkout-tragedy`** [`SCH-sukhanov-nikolai`(尼古拉·苏汉诺夫) | pp. 631–647, 657–660 (PDF pp. 683–699, 709–711)]: 
- **`CLM-figes-1996-peasant-moral-economy-1917`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 343-352]: 
- **`CLM-suny-2017-totalitarian-vs-social-history-turn`** [`SCH-suny-ronald-gregor`(罗纳德·格里戈尔·苏尼) | pp. 87-95 (approx. ch. 2 sect. on totalitarianism and revision)]: 
- **`CLM-suny-2017-class-discourse-and-polarization`** [`SCH-suny-ronald-gregor`(罗纳德·格里戈尔·苏尼) | pp. 160-175 (approx. ch. 5 on class, strikes, discourse)]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 8 条 L3 逐日细节见 `timeline/L3_daily/`)
