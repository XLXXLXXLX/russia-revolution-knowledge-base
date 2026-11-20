# 1-Hop 去重平衡上下文包：`ORG-petrograd-soviet`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`ORG-petrograd-soviet`** (彼得格勒工兵代表苏维埃 | `cards/organizations/ORG-petrograd-soviet.md` | `multi-perspective`): 已覆盖=`eyewitness-sukhanov, revisionist-hasegawa, menshevik-defensism-galili, bolshevik-grassroots-rabinowitch`；待补=`garrison-regiment-granular-votes, women-workers-soviet-election`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
二月革命后诞生于塔夫利达宫的工兵政权，颁布《第一号命令》。执委会主席为齐赫伊泽，策烈铁里是常务局核心并主导革命护国路线。1917-08-31[O.S.]/09-13[N.S.]首次通过布尔什维克决议，托洛茨基随后任主席；十月军事革命委员会成为推翻临时政府的枢纽。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **二月诞生与《第一号命令》（1917.02.27–03.14 [O.S.] / 1917-03-12–03.27 [N.S.]）**：`1917-02-27 [O.S.] / 1917-03-12 [N.S.]` 卫戍哗变当天，工人与士兵代表在塔夫利达宫选举第一届执行委员会（齐赫伊泽主席），与杜马临时委员会并行（`CLM-hasegawa-2018-sub-elite-activists`）。`1917-03-01 [O.S.] / 1917-03-14 [N.S.]` 苏汉诺夫见证士兵向索科洛夫口授的**《第一号命令》**全文，要求连队选举委员会、官兵一律服从苏维埃、武器不得交反动军官（`CLM-sukhanov-1922-dual-power-pact`）。苏维埃自承不掌行政部院，却掌握枪杆子效忠与运输节点。
- **执委会“星室”与护国多数（1917.03–08）**：策烈铁里归国后联合但恩、斯科别列夫确立**革命护国主义**与“全国生机力量”联盟，抵制立刻夺取全部政权，转以`контроль`（监督）与有条件承认临时政府（`CLM-galili-1989-revolutionary-defensism`）。四月起赤卫队在区苏维埃层面自行武装化，首都苏维埃精英拒绝背书，工人运动与苏维埃代表脱节（`CLM-boll-1979-red-guards-radicalization-to-july`）。
- **七月挫败与威信断裂（1917.07）**：七月示威期间执委会拒绝接管政权并支持临时政府镇压，激发驻军与工厂对“护国派”失望（`CLM-rabinowitch-1968-divided-bolshevik-party-july`, `CLM-galili-1989-menshevik-worker-alienation`）。科尔尼洛夫事件后布尔什维克辟谣自卫赢得士兵信任。
- **托洛茨基主席与军事革命委员会（1917.08–10）**：`1917-08-31 [O.S.] / 1917-09-13 [N.S.]` 夜苏维埃全体大会首次通过布尔什维克《关于政权问题》决议；`1917-09-09 [O.S.] / 1917-09-22 [N.S.]` 齐赫伊泽—策烈铁里主席团辞职，`1917-09-25 [O.S.] / 1917-10-08 [N.S.]` 托洛茨基当选苏维埃主席。`1917-10-16 [O.S.] / 1917-10-29 [N.S.]` 苏维埃批准成立**军事革命委员会（Milrevkom）**，以保卫苏维埃代表大会与审查前线调防为名组织夺权（`CLM-pipes-1990-october-classic-coup`；亦见 `CLM-rabinowitch-2007-contingency-of-dictatorship`）。`1917-10-25 [O.S.] / 1917-11-07 [N.S.]` 十月起义与全俄苏维埃二大开幕同日完成政权易手。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-provisional-government` | `dual-power-counterpart` | 1917.03–1917.10 | 苏维埃掌握武装与群众忠诚背书，却不入阁执政，形成“有意不接权的权力” | `CLM-hasegawa-2018-dual-power-origins`, `CLM-sukhanov-1922-dual-power-pact` |
| `ORG-mensheviks` | `executive-majority` | 1917.03–1917.09 | 孟什维克护国派操控执委会议程，推迟土地社会化与反战动员工具 | `CLM-galili-1989-revolutionary-defensism` |
| `ORG-psr` | `executive-coalition` | 1917.03–1917.10 | 与孟什维克构成苏维埃“革命民主派”多数，共同承担联立政府后果 | `CLM-galili-1989-coalition-government-trap` |
| `PER-tsereteli` | `star-chamber-leader` | 1917.03–1917.09 | 作为执委会常务局（“星室”）核心领袖（主席为齐赫伊泽）兼邮电、代理内务部长，主导革命护国与联立入阁路线 | `CLM-galili-1989-revolutionary-defensism` |
| `PER-trotsky` | `chairman -> insurrection-lever` | 1917.09–1917.10 | 以苏维埃主席身份统合军事革命委员会与卫戍部队，衔接大会程序 | `CLM-pipes-1990-october-classic-coup`, `DEB-1917-october-coup-or-social-revolution` |
| `PER-lenin` | `strategic-opponent -> tacit-beneficiary` | 1917.04–1917.10 | 《四月提纲》批判执委会路线，十月依托苏维埃机构完成夺权 | `CLM-loginov-lenin-vs-party-moderates-1917`, `POL-april-theses-1917` |
| `EVT-1917-07-july-days` | `refused-power` | 1917.07.03–05 [O.S.] / 07.16–18 [N.S.] | 执委会在武装群众逼宫下仍拒接掌政权，峰值后威信大跌 | `CLM-galili-1989-menshevik-worker-alienation` |
| `EVT-1917-10-october-revolution` | `institutional-vehicle` | 1917.10.25–26 [O.S.] / 11.07–08 [N.S.] | 军事革命委员会与二大共同构成起义合法性外壳 | `CLM-sukhanov-1922-october-walkout-tragedy` |
| `CON-soviet` | `reinstitutionalizes` | 1917.02起 | 复活1905年苏维埃传统并拓展至士兵代表与革命护国话语 | `EVT-1917-02-february-revolution` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1917年首都苏维埃自3月中旬至10月下旬为工兵代表最高协调机构；颁布《第一号命令》；夏秋经历从护国多数到布尔什维克领袖的转换；十月以军事革命委员会行动收场。
- **主要解释分歧**（详参 `DEB-1917-dual-power-and-february-origins`, `DEB-1917-october-coup-or-social-revolution`）：
  - **[亲历者“条件交权”叙事 / N. N. Sukhanov]** (`CLM-sukhanov-1922-dual-power-pact`, `CLM-sukhanov-1922-lenin-april-arrival-shock`)：苏维埃执委会有意识地把部院权力留给自由派，但保留军队与群众信任；四月列宁归国冲击这一“团结阵线”。
  - **[苏维埃“并非政权”修正 / Hasegawa]** (`CLM-hasegawa-2018-dual-power-origins`)：执行委员会领导人拒绝竞争行政机器，临时政府反而因缺乏群众依附而依赖苏维埃认可——纠正托洛茨基“自愿让权”简化论。
  - **[护国联盟社会学 / Galili]** (`CLM-galili-1989-revolutionary-defensism`, `CLM-galili-1989-menshevik-worker-alienation`)：策烈铁里“生机力量”话术真实动员外省小城知识分子，却因压制罢工丧失五金工人，苏维埃代表结构右倾化。
  - **[布尔什维克草根派 / Rabinowitch]** (`CLM-rabinowitch-1968-grassroots-soldier-sailor-radicalism`, `CLM-rabinowitch-2007-contingency-of-dictatorship`)：驻军与工厂支部激进化推动苏维埃左转，并非党中央密谋单独演出；1917年秋多数布尔什维克仍拥抱多元苏维埃理想，独裁并非预筑蓝图。

## 2. 一跳邻域全量微摘要目录 (去重后共 18 个节点，0 截断)
- **`CON-dual-power`**（双重政权（两个政权并存））: 萌芽于1905年苏维埃；1917-03-02[O.S.]/03-15[N.S.]至七月事件，临时政府名义主权与彼得格勒苏维埃工兵实力、“有条件支持”并存。列宁四月称两类阶级专政交织，七月宣布终结，九月再提苏维埃夺权；修正史学强调多中心失序与双方虚弱。 ‖ `→ORG-petrograd-soviet`[de-facto-veto-pole|1917-03-12–1917-11-07 [N.S.]]: 凭《第一号命令》掌握驻军与铁路通讯，从外部“有条件支持”演变为布尔什维克夺权载体
- **`CON-soviet`**（苏维埃：代表委员会与国家形式的系谱）: 苏维埃原为会议或委员会之意。1905年工人代表机构从罢工协调走向政治权力雏形；1917年工兵农苏维埃成为多党竞争与双重政权场域。十月后1918年宪法确立城乡五比一不等权与阶级剥权机制，二十年代“活跃苏维埃”实验仍受制于一党垄断，1921年喀琅施塔得亦曾诉诸苏维埃民主。 ‖ `→ORG-petrograd-soviet`[核心载体|1917.02–11]: 主导第一号命令并成为十月布尔什维克化核心平台。 ； `←ORG-petrograd-soviet`[reinstitutionalizes|1917.02起]: 复活1905年苏维埃传统并拓展至士兵代表与革命护国话语
- **`EVT-1905-12-moscow-armed-uprising`**（1905年12月莫斯科武装起义与普列斯尼亚街垒战）: 1905-12-07至12-18[O.S.]/12-20至12-31[N.S.]，莫斯科总罢工转为巷战。铁路未断使谢苗诺夫近卫团得以增援，重炮镇压普列斯尼亚，全城估死千人。败局引发普列汉诺夫反对起兵、列宁要求坚决进攻、托洛茨基强调争夺军队的战略分歧。 ‖ `→ORG-petrograd-soviet`[catalyzes|1905-12-03 [O.S.] / 1905-12-16 [N.S.] 至 1905-12-07 [O.S.] / ]: 杜尔诺沃逮捕圣彼得堡苏维埃260余名代表切断首都指挥中枢，迫使莫斯科苏维埃与各党地方组织独自扛起武装决战重担（RN-W32 [·236·–·251·]）。
- **`EVT-1917-02-february-revolution`**（1917年二月革命）: 1917年2月23日至3月3日（俄历；公历3月8—16日），彼得格勒女工罢工、跨厂动员与驻军兵变推翻帝制。杜马委员会接管行政，苏维埃代表工兵，临时政府在革命全权与旧宪制断裂中成立；双重政权并非简单的主动让权。 ‖ `→ORG-petrograd-soviet`[mass_authority|1917-02-27..03-03 [O.S.] / 03-12..16 [N.S.]]: 以工兵代表与第一号命令制约政府，不等同完整行政国家。
- **`EVT-1917-07-july-days`**（1917年七月事变）: 1917年7月3—5日（俄历；公历7月16—18日），机枪团、水兵与工人要求苏维埃接权。布尔什维克中央、军事组织与地方党委在劝阻和介入间分裂；德国经费指控与调兵镇压扭转局势。基层激进化、党内决策和资助指控须分别求证。 ‖ `→ORG-petrograd-soviet`[refused_power|1917-07-03..05 [O.S.] / 07-16..18 [N.S.]]: 与全俄中执委多数派一起拒绝武装群众的接权要求。 ； `←ORG-petrograd-soviet`[refused-power|1917.07.03–05 [O.S.] / 07.16–18 [N.S.]]: 执委会在武装群众逼宫下仍拒接掌政权，峰值后威信大跌
- **`EVT-1917-08-kornilov-affair`**（1917年科尔尼洛夫事件）: 1917-08-24至08-31[O.S.]/09-06至09-13[N.S.]，克伦斯基与科尔尼洛夫经萨文科夫调兵、李沃夫传话及电报对质后决裂。铁路工人、赤卫队与穆斯林代表瓦解第3骑兵军；末日夜彼得格勒苏维埃通过布尔什维克政权决议，主席团改选在后。 ‖ `→ORG-petrograd-soviet`[bolshevized_at|1917.09.13–09.14]: 通过“反革命斗争委员会”夺回武装动员权，并在8月31日夜通过布尔什维克政权决议；后续信任表决与主席改选另有节点。
- **`EVT-1917-10-october-revolution`**（1917年十月革命）: 1917年10月24—27日（俄历；公历11月6—9日），军事革命委员会夺取彼得格勒中枢，冬宫陷落，苏维埃二大通过和平、土地法令并建立人民委员会。群众激进化、组织夺权与多党联合失败交织；首都迅速接管不代表全国无血革命。 ‖ `→ORG-petrograd-soviet`[mrc_institutional_base|1917-10 [O.S.] / 10–11 [N.S.]]: 军革委的苏维埃身份争取非党驻军，并非单纯党中央下属番号。 ； `←ORG-petrograd-soviet`[institutional-vehicle|1917.10.25–26 [O.S.] / 11.07–08 [N.S.]]: 军事革命委员会与二大共同构成起义合法性外壳
- **`MTG-1917-06-1st-congress-of-soviets`**（全俄工兵代表苏维埃第一次代表大会）: 1917年6月3—24日[O.S.]/6月16日—7月7日[N.S.]，全俄工兵苏维埃一大在彼得格勒召开。护国派543∶126通过信任联合政府并设257席中执委；但列宁6月4日应战“有！”、6月10日流产示威与6月18日40万大游行反噬，彻底撕裂温和派街头合法性。 ‖ `→ORG-petrograd-soviet`[supplanted_local_hegemony|1917-06-17..24 [O.S.] / 06-30..07-07 [N.S.]]: 新选VTsIK接管全俄苏维埃代表权并压制彼得格勒基层左倾呼声，为秋后地方与中枢对立埋线。
- **`ORG-bund`**（崩得（立陶宛、波兰和俄罗斯犹太工人总同盟））: 1897年维尔纽斯成立的帝俄最早群众性犹太工人社会民主党：1898年参与筹备俄社民工党一大，1903年二大因联邦制与“唯一代表权”被拒而退场，客观上促成列宁派组织多数；提出民族文化自治理论；内战后苏俄境内组织于1921年3月并入俄共（布），波兰崩得则作为独立犹太社会主义政党存续至二战时期。 ‖ `→ORG-petrograd-soviet`[faction-in|1917.03–1917.10]: 埃尔利希等代表在十月二大随孟什维克退场
- **`ORG-provisional-government`**（1917年俄国临时政府）: 1917年3月至11月俄国最高行政机关：由自由主义杜马派在李沃夫公爵主持下组成，宣称继承沙皇“全部政权”，却在工兵苏维埃与前线《第一号命令》制约下陷入土地、军队与和平三重困局；经四届内阁（李沃夫首届、五月至九月三次资产阶级—社会主义联立内阁及九月短期五人执政内阁）未能稳住宪政民主，终为十月起义推翻。 ‖ `←ORG-petrograd-soviet`[dual-power-counterpart|1917.03–1917.10]: 苏维埃掌握武装与群众忠诚背书，却不入阁执政，形成“有意不接权的权力” ； `→ORG-petrograd-soviet`[dual-power-partner|1917.03–1917.10]: 苏维埃提供士兵效忠与集体背书，政府执掌正式部院却无独立强制力，双方“条件决斗”共存
- **`ORG-mensheviks`**（孟什维克）: 俄国社会民主主义政党（1903–1924），源于1903年二大马尔托夫等与列宁围绕党章第一条及集中制的决裂，主张开放型群众政党与工人自主活动。1917年分化为策烈铁里、但恩主导的入阁“革命护国派”与马尔托夫领导的反战“国际主义派”；十月后开展苏维埃合法反对派抗争，1921年后遭取缔。 ‖ `←ORG-petrograd-soviet`[executive-majority|1917.03–1917.09]: 孟什维克护国派操控执委会议程，推迟土地社会化与反战动员工具
- **`ORG-psr`**（社会革命党）: 1901年末合并建立的俄国新民粹派政党，以土地社会化纲领与战斗组织暗杀闻名。1917年选民基数居全俄之冠却在战争、分地拖延与左翼分裂中失势；虽夺立宪会议多数仍遭解散，内战“第三条道路”溃于高尔察克政变，1922年莫斯科公审后在国内覆灭。 ‖ `←ORG-petrograd-soviet`[executive-coalition|1917.03–1917.10]: 与孟什维克构成苏维埃“革命民主派”多数，共同承担联立政府后果
- **`PER-tsereteli`**（伊拉克利·策烈铁里）: 格鲁吉亚孟什维克领袖，1917年彼得格勒苏维埃“革命护国主义”总设计师。3月自西伯利亚流放归来后主导苏维埃执委会“星室”，力推联立政府与六月攻势以维系同自由派的同盟；因经济瘫痪与镇压布尔什维克而流失工人支持，十月革命后返格鲁吉亚并在流亡中著述。 ‖ `←ORG-petrograd-soviet`[star-chamber-leader|1917.03–1917.09]: 作为执委会常务局（“星室”）核心领袖（主席为齐赫伊泽）兼邮电、代理内务部长，主导革命护国… ； `→ORG-petrograd-soviet`[leads|1917.03–1917.09]: 主导苏维埃执委会“星室”，将“双重政权”从猜忌监督改造为同临时政府的体制内合作与联立。
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←ORG-petrograd-soviet`[chairman -> insurrection-lever|1917.09–1917.10]: 以苏维埃主席身份统合军事革命委员会与卫戍部队，衔接大会程序 ； `→ORG-petrograd-soviet`[chairman-and-insurrection-strategist|1917.09-11]: 科尔尼洛夫事件后当选彼得格勒苏维埃主席，依托军事革命委员会与全俄苏维埃二大衔接策略完成十月夺权。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←ORG-petrograd-soviet`[strategic-opponent -> tacit-beneficiary|1917.04–1917.10]: 《四月提纲》批判执委会路线，十月依托苏维埃机构完成夺权
- **`PER-lvov`**（格奥尔吉·叶夫根尼耶维奇·李沃夫）: 地方自治领袖、一战救济组织主席，临时政府首任总理兼内务部长。1917-03-02[O.S.]/03-15[N.S.]起主政，推公民自由与自治改革，反强制信念遭夺地、军队瓦解及双重政权挑战；07-07/08[O.S.]/07-20/21[N.S.]辞职，后流亡法国从事救济。 ‖ `→ORG-petrograd-soviet`[dual-power-counterpart|1917.03–1917.07]: 依赖苏维埃执委会政治背书维持合法性，四月危机后力邀策烈铁里等入阁共担统治责任
- **`PER-sukhanov`**（尼古拉·苏汉诺夫）: 苏汉诺夫（本姓格伊默尔）是1917年彼得格勒苏维埃创建者之一、国际主义社会主义者和《革命札记》作者。二月革命中他参与苏维埃与杜马人士的谈判，四月亲历列宁归国，十月随孟什维克国际主义派退出苏维埃二大。其回忆录既保存现场细节，又带有作者知道结局后形成的政治解释；两者须分开使用。 ‖ `→ORG-petrograd-soviet`[founder-and-executive|1917]: 从临时执委会到组阁磋商的参与者
- **`POL-april-theses-1917`**（《四月提纲：论无产阶级在这次革命中的任务》）: 1917年4月列宁归国后提出的十项纲领：宣布不给临时政府任何支持、批判“革命护国主义”、主张从资产阶级革命第一阶段向工兵苏维埃掌权第二阶段过渡，并倡议没收地主土地实现全部土地国有化、全国银行合并受苏维埃监督与更改党名；打破加米涅夫—斯大林有条件支持临时政府路线，经党内激烈辩论逐步重塑布尔什维克战略。 ‖ `→ORG-petrograd-soviet`[power-destination|1917.04–1917.10]: 主张自下而上苏维埃共和国取代议会制

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 2 项)
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


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/36 条)
- **`CLM-hasegawa-2018-sub-elite-activists`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. 643–645 (PDF pp. 664–666); cf. pp. 203–204, 218 (PDF pp. 224–225, 239)]: 
- **`CLM-sukhanov-1922-dual-power-pact`** [`SCH-sukhanov-nikolai`(尼古拉·苏汉诺夫) | pp. 117–126, 150, 153–158 (PDF pp. 163–172, 196, 199–204); cf. pp. 68, 104–108, 113–114]: 
- **`CLM-galili-1989-revolutionary-defensism`** [`SCH-galili-ziva`(齐娃·加利利) | pp. 134-140, 148-151 (PDF pp. 152-158, 174-177)]: 
- **`CLM-boll-1979-red-guards-radicalization-to-july`** [`SCH-boll-michael`(迈克尔·M·博尔) | pp. 129–144, 164–170, 174–175]: 
- **`CLM-rabinowitch-1968-divided-bolshevik-party-july`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | PDF pp. 12, 17, 79, 86-94, 121-123]: 
- **`CLM-galili-1989-menshevik-worker-alienation`** [`SCH-galili-ziva`(齐娃·加利利) | pp. 195-198, 295-303, 325-336, 398-399 (PDF pp. 221-224, 321-329, 351-362, 424-425)]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-hasegawa-2018-dual-power-origins`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. 626–638 (PDF pp. 647–659); cf. pp. 649, 660 (PDF pp. 670, 681)]: 
- **`CLM-galili-1989-coalition-government-trap`** [`SCH-galili-ziva`(齐娃·加利利) | pp. 169-170, 177-181 (PDF pp. 195-196, 203-207)]: 
- **`CLM-loginov-lenin-vs-party-moderates-1917`** [`SCH-loginov-vladlen`(弗拉德连·洛吉诺夫) | pp. 145-146, 165-167, 265, 272-273, 340-343, 527-528]: 
- **`CLM-sukhanov-1922-october-walkout-tragedy`** [`SCH-sukhanov-nikolai`(尼古拉·苏汉诺夫) | pp. 631–647, 657–660 (PDF pp. 683–699, 709–711)]: 
- **`CLM-sukhanov-1922-lenin-april-arrival-shock`** [`SCH-sukhanov-nikolai`(尼古拉·苏汉诺夫) | pp. 269–292 (PDF pp. 317–340)]: 
- **`CLM-rabinowitch-1968-grassroots-soldier-sailor-radicalism`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | PDF pp. 61-67, 80-87, 121-122]: 
- **`CLM-hasegawa-2018-duma-committee-revision`** [`SCH-hasegawa-tsuyoshi`(长谷川毅) | pp. xiii–xiv (PDF pp. 14–15); pp. 366–368, 377–378 (PDF pp. 387–389, 398–399); p. 652 (PDF p. 673)]: 
- **`CLM-rabinowitch-1976-open-democratic-mass-party`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-rabinowitch-1976-trotsky-soviet-congress-strategy`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-gaida-2003-liberals-in-february-1917`** [`SCH-gaida-fedor`(费奥多尔·盖达) | pp. 355-356, 433-439]: 
- **`CLM-trotsky-1930-dual-power-instability`** [`SCH-trotsky-leon`(列夫·达维多维奇·托洛茨基 · participant-historian) | （中译 EPUB 无纸页；第一卷第十一、十六章）]: 
- **`CLM-spitsyn-february-1917-elite-conspiracy-thesis`** [`SCH-spitsyn-yevgeny`(叶夫根尼·斯皮岑) | PDF pp. 11–15, 24, 28]: 
- **`CLM-figes-1996-soldier-mutiny-and-social-inversion`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 404-412]: 
- **`CLM-rabinowitch-1976-october-three-factions-debate`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-loginov-lenin-1917-fleeting-window-of-power`** [`SCH-loginov-vladlen`(弗拉德连·洛吉诺夫) | pp. 523-524, 531-532, 560-561, 621-622, 656-658]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 18 条 L3 逐日细节见 `timeline/L3_daily/`)
