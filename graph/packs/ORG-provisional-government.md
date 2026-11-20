# 1-Hop 去重平衡上下文包：`ORG-provisional-government`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`ORG-provisional-government`** (1917年俄国临时政府 | `cards/organizations/ORG-provisional-government.md` | `multi-perspective`): 已覆盖=`constitutional-liberal-gaida, revisionist-dual-power-hasegawa, menshevik-coalition-galili, bolshevik-local-rabinowitch`；待补=`provincial-governor-general-network, orthodox-church-apparatus`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1917年3月至11月俄国最高行政机关：由自由主义杜马派在李沃夫公爵主持下组成，宣称继承沙皇“全部政权”，却在工兵苏维埃与前线《第一号命令》制约下陷入土地、军队与和平三重困局；经四届内阁（李沃夫首届、五月至九月三次资产阶级—社会主义联立内阁及九月短期五人执政内阁）未能稳住宪政民主，终为十月起义推翻。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **诞生、全权宣言与自愿枷锁（1917.03.02–05 [O.S.] / 1917-03-15–18 [N.S.]）**：`1917-03-02 [O.S.] / 1917-03-15 [N.S.]` 国家杜马临时委员会推举李沃夫为总理，米留可夫任外交部长；同日夜与苏维埃执委会达成协议，苏维埃不入阁但予其存在以政治背书（`CLM-sukhanov-1922-dual-power-pact`）。`1917-03-03 [O.S.] / 1917-03-16 [N.S.]` 临时政府首次正式内阁会议排挤罗将柯，宣布政府掌握不受杜马制约的**全部完满权力（вся полнота власти）**并切断与第四届国家杜马机制性联系，代议制根基反被自由派亲手削弱（`CLM-hasegawa-2018-dual-power-origins`）。土地改革拖延、军队民主化与和平外交均受制于苏维埃与士兵委员会。
- **四月危机与首届联立内阁（1917.04–07）**：`1917-04-18 [O.S.] / 1917-05-01 [N.S.]` 米留科夫照会坚持协约国战争目标引发首都大规模示威，李沃夫内阁被迫改组；`1917-05-05 [O.S.] / 1917-05-18 [N.S.]` **策烈铁里、斯科别列夫**等孟什维克与社会革命党人入阁组建首届联合政府，克伦斯基任陆海军部长（`CLM-galili-1989-coalition-government-trap`）。六月攻势失败与列宁政府“德国间谍”指控点燃七月危机。
- **克伦斯基接任总理与第二届联立内阁（1917.07–08）**：`1917-07-08 [O.S.] / 1917-07-21 [N.S.]` 克伦斯基接任总理，并于 `1917-07-24 [O.S.] / 1917-08-06 [N.S.]` 组成第二届联立内阁；临时政府试图恢复前线军纪与死刑，却无法满足工兵诉求，权威加速流失（`CLM-rabinowitch-1968-grassroots-soldier-sailor-radicalism`）。八月科尔尼洛夫事件挫败后，自由派阁员辞职、临时政府威信崩塌，苏维埃左翼决议首次占上风。
- **五人执政内阁、第三届联立内阁与终局（1917.09–10）**：`1917-09-01 [O.S.] / 1917-09-14 [N.S.]` 克伦斯基一度设五人“执政内阁（Директория）”，旋于 `1917-09-25 [O.S.] / 1917-10-08 [N.S.]` 再度吸纳立宪民主党人与 **6 名温和派社会主义部长**（孟什维克格沃兹杰夫任劳工、尼基京任内务兼邮电、马良托维奇任司法，以及普罗科波维奇、利韦罗夫斯基（A. V. Liverovsky）等）组成第三届联立内阁（第四届政府），全俄民主会议与预备议会均未能挽回局势；`1917-10-26 [O.S.] / 1917-11-08 [N.S.]` 彼得格勒军事革命委员会攻占冬宫，留守阁员被捕，正式终结。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-petrograd-soviet` | `dual-power-partner` | 1917.03–1917.10 | 苏维埃提供士兵效忠与集体背书，政府执掌正式部院却无独立强制力，双方“条件决斗”共存 | `CLM-sukhanov-1922-dual-power-pact`, `CLM-hasegawa-2018-dual-power-origins` |
| `ORG-mensheviks` | `coalition-partner` | 1917.05–1917.07 | 革命护国派阁员以少数入阁换取国防与秩序，反而使社会主义者站到群众对立面 | `CLM-galili-1989-revolutionary-defensism`, `CLM-galili-1989-coalition-government-trap` |
| `ORG-psr` | `coalition-partner` | 1917.05–1917.09 | 社革党土地部长切尔诺夫在议会路线内推动土地社会化，被战争财政与内阁分裂牵制 | `CLM-galili-1989-coalition-government-trap` |
| `ORG-kadets` | `ministerial-backbone` | 1917.03–1917.10 | 立宪民主党人把持外交、财政关键部院，米留可夫照会定义战争主义基调 | `CLM-gaida-2003-progressive-bloc-dilemma`, `CLM-hasegawa-2018-duma-committee-revision` |
| `PER-kerensky` | `chairman-premier` | 1917.07–1917.11 | 自陆海军部长升总理，象征个人魅力政权却无力调和前线、后方与苏维埃三重重压 | `CLM-rabinowitch-1968-grassroots-soldier-sailor-radicalism` |
| `EVT-1917-07-july-days` | `repression-trigger` | 1917.07.03–05 [O.S.] / 07.16–18 [N.S.] | 调兵镇压后通缉列宁，加速自由派与激进左翼决裂 | `CLM-rabinowitch-1968-divided-bolshevik-party-july` |
| `EVT-1917-10-october-revolution` | `overthrown-by` | 1917.10.25–26 [O.S.] / 11.07–08 [N.S.] | 军事革命委员会行动与苏维埃二大程序衔接，临时政府丧失首都控制 | `CLM-pipes-1990-october-classic-coup`, `CLM-rabinowitch-2007-contingency-of-dictatorship` |
| `EVT-1917-02-february-revolution` | `successor-regime` | 1917.03起 | 承接沙皇退位后的行政真空，却未能在宪政框架内兑现自由派长期诉求 | `CLM-gaida-2003-liberals-in-february-1917` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1917年3–11月存在以部长会议为形式的全国统一政府；经历至少四次重大改组；在土地、和平与军队指挥权问题上始终无法摆脱苏维埃与前线委员会约束；十月下旬在彼得格勒失去实际权力。
- **主要解释分歧**（详参 `DEB-1917-dual-power-and-february-origins`）：
  - **[自由派“被迫革命”叙事 / Fedor Gaida]** (`CLM-gaida-2003-liberals-in-february-1917`)：杜马自由派并非精心策划的政变赢家，而是在士兵哗变与群众占领下“叹着气”接掌政权；获胜的是塔夫利达宫**场所**而非杜马**机构**，先天拄杖苏维埃。
  - **[双重政权结构论 / Tsuyoshi Hasegawa]** (`CLM-hasegawa-2018-dual-power-origins`, `CLM-hasegawa-2018-duma-committee-revision`)：临时政府宣称独裁权却无兵工群众忠诚；米留可夫废杜马连续性后，合法性的唯一支点变成苏维埃执委会制裁——“悖论”在于强势宣言与弱势根基并存。
  - **[联合政府陷阱论 / Ziva Galili]** (`CLM-galili-1989-coalition-government-trap`, `CLM-galili-1989-revolutionary-defensism`)：社会主义阁员清醒预知入阁会破坏苏维埃监督，却在国家崩溃恐惧下跳入；维护战争努力与经济压制使护国派迅速丧失产业工人。
  - **[首都基层动员视角 / Alexander Rabinowitch]** (`CLM-rabinowitch-1968-grassroots-soldier-sailor-radicalism`, `CLM-rabinowitch-1968-divided-bolshevik-party-july`)：七月与夏秋危机需从驻军、工厂布尔什维克基层组织理解，不能把临时政府失败单纯归因为自由派“软弱”。

## 2. 一跳邻域全量微摘要目录 (去重后共 18 个节点，0 截断)
- **`CON-constituent-assembly`**（立宪会议（全俄立宪会议））: 自1879年民意党起，立宪会议成为反对派共享的民主合法性象征。1917年临时政府拖延选举；11月社革党获多数，布尔什维克掌两京与近卫战线优势。1918-01-05/06[O.S.]/01-18/19[N.S.]开会一夜即遭武力解散，夏秋成为萨马拉立宪会议委员委员会的内战旗帜。 ‖ `→ORG-provisional-government`[procrastinating-trustee|1917-03-15–1917-11-07 [N.S.]]: 以等待立宪会议为由冻结土地与和战改革，却两度推迟选举而掏空自身过渡合法性
- **`CON-dual-power`**（双重政权（两个政权并存））: 萌芽于1905年苏维埃；1917-03-02[O.S.]/03-15[N.S.]至七月事件，临时政府名义主权与彼得格勒苏维埃工兵实力、“有条件支持”并存。列宁四月称两类阶级专政交织，七月宣布终结，九月再提苏维埃夺权；修正史学强调多中心失序与双方虚弱。 ‖ `→ORG-provisional-government`[de-jure-executive-pole|1917-03-15–1917-11-07 [N.S.]]: 承接形式国家主权但自断杜马法统，丧失强制工具而仰赖苏维埃合法性中介
- **`EVT-1917-02-february-revolution`**（1917年二月革命）: 1917年2月23日至3月3日（俄历；公历3月8—16日），彼得格勒女工罢工、跨厂动员与驻军兵变推翻帝制。杜马委员会接管行政，苏维埃代表工兵，临时政府在革命全权与旧宪制断裂中成立；双重政权并非简单的主动让权。 ‖ `→ORG-provisional-government`[successor_government|1917-03-02..03 [O.S.] / 03-15..16 [N.S.]]: 在组阁协商与帝制终结中取得行政权，合法性依赖革命认可。 ； `←ORG-provisional-government`[successor-regime|1917.03起]: 承接沙皇退位后的行政真空，却未能在宪政框架内兑现自由派长期诉求
- **`EVT-1917-07-july-days`**（1917年七月事变）: 1917年7月3—5日（俄历；公历7月16—18日），机枪团、水兵与工人要求苏维埃接权。布尔什维克中央、军事组织与地方党委在劝阻和介入间分裂；德国经费指控与调兵镇压扭转局势。基层激进化、党内决策和资助指控须分别求证。 ‖ `→ORG-provisional-government`[allegation_and_repression|1917-07-04..06 [O.S.] / 07-17..19 [N.S.]]: 释放经费指控，调前线部队收缴武装。 ； `←ORG-provisional-government`[repression-trigger|1917.07.03–05 [O.S.] / 07.16–18 [N.S.]]: 调兵镇压后通缉列宁，加速自由派与激进左翼决裂
- **`EVT-1917-08-kornilov-affair`**（1917年科尔尼洛夫事件）: 1917-08-24至08-31[O.S.]/09-06至09-13[N.S.]，克伦斯基与科尔尼洛夫经萨文科夫调兵、李沃夫传话及电报对质后决裂。铁路工人、赤卫队与穆斯林代表瓦解第3骑兵军；末日夜彼得格勒苏维埃通过布尔什维克政权决议，主席团改选在后。 ‖ `→ORG-provisional-government`[collapses_into_directory|1917.09.09–09.14]: 立宪民主党部长辞职后权威尽失，临时政府沦为五人督政府并在首都部分工人与卫戍部队中严重丧失信任。
- **`EVT-1917-10-october-revolution`**（1917年十月革命）: 1917年10月24—27日（俄历；公历11月6—9日），军事革命委员会夺取彼得格勒中枢，冬宫陷落，苏维埃二大通过和平、土地法令并建立人民委员会。群众激进化、组织夺权与多党联合失败交织；首都迅速接管不代表全国无血革命。 ‖ `→ORG-provisional-government`[overthrown|1917-10-24..26 [O.S.] / 11-06..08 [N.S.]]: 失去中枢及驻军保护，部长在冬宫被捕。 ； `←ORG-provisional-government`[overthrown-by|1917.10.25–26 [O.S.] / 11.07–08 [N.S.]]: 军事革命委员会行动与苏维埃二大程序衔接，临时政府丧失首都控制
- **`MTG-1917-06-1st-congress-of-soviets`**（全俄工兵代表苏维埃第一次代表大会）: 1917年6月3—24日[O.S.]/6月16日—7月7日[N.S.]，全俄工兵苏维埃一大在彼得格勒召开。护国派543∶126通过信任联合政府并设257席中执委；但列宁6月4日应战“有！”、6月10日流产示威与6月18日40万大游行反噬，彻底撕裂温和派街头合法性。 ‖ `→ORG-provisional-government`[granted_vote_of_confidence|1917-06-08 [O.S.] / 06-21 [N.S.]]: 大会以543∶126∶52投票信任第一届联合临时政府，确认“双重政权”下的合作框架。
- **`ORG-kadets`**（立宪民主党（卡德特党））: 1905年10月从解放同盟诞生的俄国自由主义核心政党，主张四尾制宪、有偿征地与议会道路，曾主导前两届杜马与战时进步同盟。1917年二月主导首届临时政府并切断对杜马从属关系，旋因战争、土地危机及科尔尼洛夫事件退阁丧失民心，十月后被定为“人民公敌”并在内战与流亡中分裂。 ‖ `→ORG-provisional-government`[founding_pillar|1917-03–1917-10]: 垄断首届内阁核心席位，但在战争赔款、土改延宕与7月/8月撤阁中迅速耗尽政治信誉 ； `←ORG-provisional-government`[ministerial-backbone|1917.03–1917.10]: 立宪民主党人把持外交、财政关键部院，米留可夫照会定义战争主义基调
- **`ORG-petrograd-soviet`**（彼得格勒工兵代表苏维埃）: 二月革命后诞生于塔夫利达宫的工兵政权，颁布《第一号命令》。执委会主席为齐赫伊泽，策烈铁里是常务局核心并主导革命护国路线。1917-08-31[O.S.]/09-13[N.S.]首次通过布尔什维克决议，托洛茨基随后任主席；十月军事革命委员会成为推翻临时政府的枢纽。 ‖ `→ORG-provisional-government`[dual-power-counterpart|1917.03–1917.10]: 苏维埃掌握武装与群众忠诚背书，却不入阁执政，形成“有意不接权的权力” ； `←ORG-provisional-government`[dual-power-partner|1917.03–1917.10]: 苏维埃提供士兵效忠与集体背书，政府执掌正式部院却无独立强制力，双方“条件决斗”共存
- **`ORG-mensheviks`**（孟什维克）: 俄国社会民主主义政党（1903–1924），源于1903年二大马尔托夫等与列宁围绕党章第一条及集中制的决裂，主张开放型群众政党与工人自主活动。1917年分化为策烈铁里、但恩主导的入阁“革命护国派”与马尔托夫领导的反战“国际主义派”；十月后开展苏维埃合法反对派抗争，1921年后遭取缔。 ‖ `←ORG-provisional-government`[coalition-partner|1917.05–1917.07]: 革命护国派阁员以少数入阁换取国防与秩序，反而使社会主义者站到群众对立面
- **`ORG-psr`**（社会革命党）: 1901年末合并建立的俄国新民粹派政党，以土地社会化纲领与战斗组织暗杀闻名。1917年选民基数居全俄之冠却在战争、分地拖延与左翼分裂中失势；虽夺立宪会议多数仍遭解散，内战“第三条道路”溃于高尔察克政变，1922年莫斯科公审后在国内覆灭。 ‖ `←ORG-provisional-government`[coalition-partner|1917.05–1917.09]: 社革党土地部长切尔诺夫在议会路线内推动土地社会化，被战争财政与内阁分裂牵制
- **`PER-kerensky`**（亚历山大·克伦斯基）: 杜马劳动派律师、1917年临时政府司法部长、陆海军部长与总理（07-08[O.S.]/07-21[N.S.]起）。二月率先筹建杜马军事委员会，兼任苏维埃副主席入阁；六月攻势受阻、调防与退阁触发七月危机（07-06/19转全面溃败），八月与科尔尼洛夫决裂，十月离冬宫反扑失败流亡。 ‖ `←ORG-provisional-government`[chairman-premier|1917.07–1917.11]: 自陆海军部长升总理，象征个人魅力政权却无力调和前线、后方与苏维埃三重重压 ； `→ORG-provisional-government`[minister_then_premier|1917-03–1917-11]: 由首届唯一社会主义司法部长升任陆海军部长及末两届联合与五人督政府总理
- **`PER-guchkov`**（亚历山大·伊万诺维奇·古契科夫）: 十月十七日同盟领袖、第三届杜马前议长与战时军事工业委员会负责人。1917年他同舒尔金赴普斯科夫接收尼古拉二世退位文书，出任临时政府陆海军部长；军队权威危机和四月政治危机中辞职。战前宫廷政变计划真实存在，但未实际发动，不能将其当作二月起义的成熟指挥方案。 ‖ `→ORG-provisional-government`[war-and-navy-minister|1917.03–05]: 首届临时政府陆海军部长，因军队权威与四月危机辞职
- **`PER-lvov`**（格奥尔吉·叶夫根尼耶维奇·李沃夫）: 地方自治领袖、一战救济组织主席，临时政府首任总理兼内务部长。1917-03-02[O.S.]/03-15[N.S.]起主政，推公民自由与自治改革，反强制信念遭夺地、军队瓦解及双重政权挑战；07-07/08[O.S.]/07-20/21[N.S.]辞职，后流亡法国从事救济。 ‖ `→ORG-provisional-government`[minister-president|1917-03-02 [O.S.] / 03-15 [N.S.]–07-07/08 [O.S.] / 07-20/21 ]: 连任首届与第一届联合政府总理兼内务部长，以超党派声望维系脆弱内阁，拒绝诉诸暴力专政
- **`PER-rodzianko`**（米哈伊尔·弗拉基米罗维奇·罗将柯）: 十月党人，1911–1917年杜马议长，二月革命时主持临时委员会，谋以信任内阁、君主立宪应变，曾推大公宪制方案，后劝阻米哈伊尔即位。临时政府成立后，面对起义士兵、苏维埃与自由派内部分歧，其杜马中心方案败于米留可夫等；回忆录的领袖形象须与会议记录及同时代证据互校。 ‖ `→ORG-provisional-government`[failed-parliamentary-oversight-proposal|1917.03]: 主张政府对杜马/临时委员会负责，被不受杜马约束的全权方案否决
- **`PER-savinkov`**（鲍里斯·维克托罗维奇·萨温科夫）: 社革党战斗组织者、作家，参与刺杀沙皇高官。1917年任陆军部副部长及代理部长，涉科尔尼洛夫事件遭开除；1918年组反布同盟，后经营流亡运动。1924年被OGPU“辛迪加-2”诱捕，认罪后死刑改十年；1925年羁押中死亡，官方自杀说与他杀疑云均须审慎核证。 ‖ `→ORG-provisional-government`[deputy-war-minister-and-governor-general|1917.07–09]: 陆军部副部长/代理部长，08-27 [O.S.] 兼任彼得格勒军事总督
- **`PER-tsereteli`**（伊拉克利·策烈铁里）: 格鲁吉亚孟什维克领袖，1917年彼得格勒苏维埃“革命护国主义”总设计师。3月自西伯利亚流放归来后主导苏维埃执委会“星室”，力推联立政府与六月攻势以维系同自由派的同盟；因经济瘫痪与镇压布尔什维克而流失工人支持，十月革命后返格鲁吉亚并在流亡中著述。 ‖ `→ORG-provisional-government`[member_of|1917.05–1917.07]: 任第一届联立政府邮电部长及代理内务部长，坚持社会主义阁员占少数以维系自由派留任。
- **`POL-april-theses-1917`**（《四月提纲：论无产阶级在这次革命中的任务》）: 1917年4月列宁归国后提出的十项纲领：宣布不给临时政府任何支持、批判“革命护国主义”、主张从资产阶级革命第一阶段向工兵苏维埃掌权第二阶段过渡，并倡议没收地主土地实现全部土地国有化、全国银行合并受苏维埃监督与更改党名；打破加米涅夫—斯大林有条件支持临时政府路线，经党内激烈辩论逐步重塑布尔什维克战略。 ‖ `→ORG-provisional-government`[no-confidence|1917.04起]: 提纲第3条要求不给任何支持并揭露其兼并诺言

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 3 项)
- **`DEB-1917-dual-power-and-february-origins`**（二月革命起源与“双重政权”宪制形成之争（1917） | `historiography/debates/DEB-1917-dual-power-and-february-origins.md` | 流派 `social-history, liberal-constitutional, participant, trotskyist, menshevik-coalition, elite-conspiracy-critique`）：二月革命是无领导的群众爆发，还是工厂与兵营中分散的积极分子推动的起义？沙皇退位后，杜马临时委员会、苏维埃与临时政府如何谈判并形成彼此制约的权力格局？群众压力、精英选择和战时危机的因果权重仍有争议，不能以宫廷阴谋代替街头革命。
- **`DEB-1917-october-coup-or-social-revolution`**（十月革命：少数派政变还是社会革命？ | `historiography/debates/DEB-1917-october-coup-or-social-revolution.md` | 流派 `liberal-coup, party-social-history, russian-revisionist-timing, labor-local-history, moderate-socialist-and-constitutional-legitimacy, participant-marxist, peasant-social-history, borderland-and-memory-historiography`）：十月武装夺权是少数派政变，还是工人、士兵与农民社会革命的政治表达？有组织的起义与广泛的基层动员能否同时成立，苏维埃多数又能否代表全国选民？这些问题涉及不同地区、不同时间的支持与合法性，不能以一次投票或一次攻占行动互相替代。
- **`DEB-1918-constituent-assembly-and-soviet-democracy`**（解散立宪会议与多党苏维埃民主的命运 | `historiography/debates/DEB-1918-constituent-assembly-and-soviet-democracy.md` | 流派 `liberal-totalitarian, revisionist, sr-electoral-political-history, menshevik-history, security-legal-history`）：1918年立宪会议被武力解散，是否意味着一党统治已不可避免？争论涉及普选制宪与阶级性苏维埃两种合法性、群众动员和镇压，以及此后左翼多党合作与体制内反对派仍有多少政治空间。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/40 条)
- **`CLM-sukhanov-1922-dual-power-pact`** [`SCH-sukhanov-nikolai`(尼古拉·苏汉诺夫) | pp. 117–126, 150, 153–158 (PDF pp. 163–172, 196, 199–204); cf. pp. 68, 104–108, 113–114]: 
- **`CLM-hasegawa-2018-dual-power-origins`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. 626–638 (PDF pp. 647–659); cf. pp. 649, 660 (PDF pp. 670, 681)]: 
- **`CLM-galili-1989-coalition-government-trap`** [`SCH-galili-ziva`(齐娃·加利利) | pp. 169-170, 177-181 (PDF pp. 195-196, 203-207)]: 
- **`CLM-rabinowitch-1968-grassroots-soldier-sailor-radicalism`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | PDF pp. 61-67, 80-87, 121-122]: 
- **`CLM-galili-1989-revolutionary-defensism`** [`SCH-galili-ziva`(齐娃·加利利) | pp. 134-140, 148-151 (PDF pp. 152-158, 174-177)]: 
- **`CLM-gaida-2003-progressive-bloc-dilemma`** [`SCH-gaida-fedor`(费奥多尔·盖达) | pp. 135-136, 162-168]: 
- **`CLM-hasegawa-2018-duma-committee-revision`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. xiii–xiv (PDF pp. 14–15); pp. 366–368, 377–378 (PDF pp. 387–389, 398–399); p. 652 (PDF p. 673)]: 
- **`CLM-rabinowitch-1968-divided-bolshevik-party-july`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | PDF pp. 12, 17, 79, 86-94, 121-123]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-gaida-2003-liberals-in-february-1917`** [`SCH-gaida-fedor`(费奥多尔·盖达) | pp. 355-356, 433-439]: 
- **`CLM-hasegawa-2018-sub-elite-activists`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. 643–645 (PDF pp. 664–666); cf. pp. 203–204, 218 (PDF pp. 224–225, 239)]: 
- **`CLM-trotsky-1930-dual-power-instability`** [`SCH-trotsky-leon`(列夫·达维多维奇·托洛茨基 · participant-historian) | （中译 EPUB 无纸页；第一卷第十一、十六章）]: 
- **`CLM-spitsyn-february-1917-elite-conspiracy-thesis`** [`SCH-spitsyn-yevgeny`(叶夫根尼·斯皮岑) | PDF pp. 11–15, 24, 28]: 
- **`CLM-figes-1996-soldier-mutiny-and-social-inversion`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 404-412]: 
- **`CLM-rabinowitch-1976-open-democratic-mass-party`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-rabinowitch-1976-october-three-factions-debate`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-rabinowitch-1976-trotsky-soviet-congress-strategy`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-loginov-lenin-1917-fleeting-window-of-power`** [`SCH-loginov-vladlen`(弗拉德连·洛吉诺夫) | pp. 523-524, 531-532, 560-561, 621-622, 656-658]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-koenker-1981-moscow-october-armed-struggle-vs-petrograd`** [`SCH-koenker-diane`(黛安·P·科恩克尔) | pp. 329–355 (local PDF pp. 345–371); p. 366 (PDF p. 382)]: 
- **`CLM-koenker-1981-rational-incremental-radicalization`** [`SCH-koenker-diane`(黛安·P·科恩克尔) | pp. 359–363 (local PDF pp. 375–379); p. 254 (PDF p. 270)]: 
- **`CLM-basil-1984-october-and-vikzhel-collapse`** [`SCH-basil-john`(约翰·D·巴兹尔) | pp. 165–175（本地 PDF 同号）]: 
- **`CLM-yao-hai-post-october-coalition-failure-and-one-party-formation`** [`SCH-yao-hai`(姚海) | [PDF pp. 532-535, 543-569]]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 13 条 L3 逐日细节见 `timeline/L3_daily/`)
