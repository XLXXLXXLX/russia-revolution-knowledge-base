# 1-Hop 去重平衡上下文包：`ORG-bund`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`ORG-bund`** (崩得（立陶宛、波兰和俄罗斯犹太工人总同盟） | `cards/organizations/ORG-bund.md` | `multi-perspective`): 已覆盖=`party-split-getzler-haimson, imperial-borderlands-blanc, soviet-nationality-liber, carr-institutional`；待补=`yiddish-press-circulation-quantitative, women-bund-activists`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1897年维尔纽斯成立的帝俄最早群众性犹太工人社会民主党：1898年参与筹备俄社民工党一大，1903年二大因联邦制与“唯一代表权”被拒而退场，客观上促成列宁派组织多数；提出民族文化自治理论；内战后苏俄境内组织于1921年3月并入俄共（布），波兰崩得则作为独立犹太社会主义政党存续至二战时期。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **维尔纽斯成立与一大筹备（1897–1898）**：`1897-09-25 [O.S.] / 1897-10-07 [N.S.]` 崩得在维尔纽斯（当时属俄罗斯帝国，今立陶宛维尔纽斯）宣布成立，以意第绪语和俄语开展工会、自卫与文化教育工作，成为帝俄犹太人群众性工人组织先导。`1898` 年俄社民工党一大筹备与召开中，崩得以“仅在专门涉及犹太无产阶级的问题上独立的自治组织”形式入党，推动将民族问题写入建党议程（Carr 第一卷 ch.5；见 `CLM-haimson-1955-1903-second-congress-split` 语境）。
- **1903年二大退场与组织后果（1903.08）**：伦敦二大将崩得自治权与“唯一代表犹太无产阶级”条款付表决，崩得五名代表（大会记录作 5 票，Haimson 记作 4 票）在联邦制与唯一代表权条款败北后退场，连同经济派 2 票退场客观上改变大会算术，使列宁派从党章第一条的少数（22:28）反转为后续中央机构选举的多数（`CLM-haimson-1955-1903-second-congress-split`, `CLM-getzler-1967-martov-1903-clause-one`）。马尔托夫虽亦反对崩得联邦制，却与列宁在党员范围论战上分裂；崩得退场被后世认为促成布尔什维克“多数”定型。
- **1905–1917：民族文化自治与护国派光谱（1905–1917）**：崩得参与1905年里加等地苏维埃实验与自卫武装（`CLM-blanc-2021-borderlands-in-1905-and-1917`）；党的领导层（如弗拉基米尔·梅杰姆 Vladimir Medem、马克·利别尔 Mark Liber）在1914年后分化为国际主义反战派与护国派；`1917` 年坚持 **民族文化自治**（`культурно-национальная автономия`）——由全俄议会为各民族划出文化基金与学校语文预算——与列宁区域自治及“民族自决”拉开距离。
- **革命、内战与并入布尔什维克（1917–1921）**：二月后崩得在彼得格勒、华沙、基辅苏维埃中派代表；十月后多数反对武装政变而逐步边缘化。`1918–1920` 内战期间一部分崩得成员参加红军、另一部分流亡波兰第二共和国；`1921` 年 3 月俄国共产崩得（Komfarband）与俄国崩得多数派在明斯克会议上解散并入俄共（布）（设犹太部 Yevsektsiya），而波兰境内的崩得则作为独立政党在波兰第二共和国持续活动至 1940 年代（`CLM-liber-1992-korenizatsiia-paradox-late-1920s` 语境；乌克兰本土化与犹太文教政策张力另参 Liber）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `MTG-1903-rsdlp-2nd-congress` | `walked-out` | 1903.08 | 联邦制与代表权条款败北后退场，改变后续选举算术 | `CLM-haimson-1955-1903-second-congress-split`, `CLM-getzler-1967-martov-1903-clause-one` |
| `PER-martov-l` | `factional-counterpoint` | 1903 | 同列宁联手驱逐崩得，却在党章第一条上与列宁分裂 | `CLM-getzler-1967-martov-1903-clause-one` |
| `PER-lenin` | `organizational-rival` | 1903–1917 | 批判民族文化自治，坚持崩得不得独占犹太工人代表权 | `CLM-lih-2006-erfurtian-merger-formula`, Carr Bolshevik Revolution v.1 |
| `ORG-mensheviks` | `electoral-ally` | 1905–1917 | 在1905里加联邦委员会与1917苏维埃中与孟什维克协同，共享护国派争议 | `CLM-blanc-2021-borderlands-in-1905-and-1917` |
| `ORG-petrograd-soviet` | `faction-in` | 1917.03–1917.10 | 埃尔利希等代表在十月二大随孟什维克退场 | `CLM-sukhanov-1922-october-walkout-tragedy` |
| `POL-korenizatsiia` | `policy-tension` | 1923–1929 | 苏联本土化与意第绪文教资源分配部分回应崩得旧诉求，却排斥自治议会模式 | `CLM-liber-1992-korenizatsiia-paradox-late-1920s` |
| `EVT-1917-02-february-revolution` | `regional-mobilizer` | 1917.02起 | 边疆工人动员网络延续1905自卫传统 | `CLM-blanc-2021-borderlands-in-1905-and-1917` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：崩得是1890年代末俄国最早的大规模犹太工人政党；1903年因民族自治条款退出俄社民工党二大；主张民族文化自治；1921年3月苏俄境内组织并入俄共（布），波兰崩得则作为独立犹太社会主义政党存续至二战。
- **主要解释分歧**（详参 `DEB-1903-bolshevik-menshevik-split`）：
  - **[组织分裂后果论 / Leopold Haimson, Israel Getzler]** (`CLM-haimson-1955-1903-second-congress-split`, `CLM-getzler-1967-martov-1903-clause-one`)：崩得退场改变二大后半议程投票结构；同时揭示列宁—马尔托夫裂痕与“飞轮—拳头”两党模型对决。
  - **[帝国边疆工人民主经验 / Eric Blanc]** (`CLM-blanc-2021-borderlands-in-1905-and-1917`)：1905年里加等地区崩得—社民联合政府实践表明“工人霸权+拒自由派”在边疆早有根源，1917年崩得护国转向须放回1905后失败后的联盟抉择。
  - **[民族政策比较 / George Liber]** (`CLM-liber-1992-korenizatsiia-paradox-late-1920s`)：苏联本土化政策（`коренизация` / `korenizatsiia`）在扩大意第绪语公共领域的同时拒绝崩得式超领土民族文化自治，改以领土苏维埃制吸纳民族诉求。
  - **[制度吸纳论 / E. H. Carr]**（`sources/monographs/carr_1950_bolshevik_rev_v1_en/ch05_pages_126-150.md`）：崩得在苏俄境内的分裂与并入标志布尔什维克对少数民族社会主义政党的制度化吸收逻辑，与乌克兰借道左翼独立派并党的轨迹同构。

## 2. 一跳邻域全量微摘要目录 (去重后共 9 个节点，0 截断)
- **`EVT-1891-1903-witte-industrialization-and-marxist-labor-turn`**（1891–1903年维特工业化与俄国马克思主义工运转向）: 1891–1903年维特国家工业化与俄国马克思主义工运转向。1891–1892年饥荒触发民粹派与马克思主义大论战，1896–1897年彼得堡纺织工潮迫使沙皇颁布11.5小时工时法；历经经济派与“警察社会主义”博弈，1903年二大引发持续派争。 ‖ `→ORG-bund`[pioneer_and_secessionist|1897–1903]: 率先实践维尔纽斯群众鼓动与有组织罢工基金，1903年二大因民族自治诉求遭否而暂退党
- **`MTG-1903-rsdlp-2nd-congress`**（俄国社会民主工党第二次代表大会（1903年7–8月））: `1903-07-30` 至 `08-23 [N.S.]` 俄社民工党二大先后在布鲁塞尔与伦敦召开。大会通过党纲；第23次会议马尔托夫党章第一条 `28:22:1` 胜列宁案。随后的崩得与经济派退场逆转了多数，列宁借微弱多数改组《火星报》三人编委，由此衍生布尔什维克与孟什维克之名。 ‖ `→ORG-bund`[walks_out|1903.08]: 因联邦制与唯一代表权要求遭否决率团退席（5票/4票），客观改变了后续多数算术。 ； `←ORG-bund`[walked-out|1903.08]: 联邦制与代表权条款败北后退场，改变后续选举算术
- **`MTG-1906-04-rsdlp-4th-stockholm-congress`**（俄国社会民主工党第四次（统一）代表大会（1906年））: 1906-04-23至05-08[N.S.]，俄社民工党在斯德哥尔摩召开统一大会。基层统一诉求促两派会合，孟什维克占表决多数，土地地方自治化方案获胜。章程首次明定民主集中制，党员公式采用列宁“加入一个党组织”的表述，并重组民族组织关系；形式统一未消除派别网络。 ‖ `→ORG-bund`[rejoins_united_party|1906]: 与统一党重新建立组织关系；其代表是否计入62/46/112待核。
- **`PER-martov-l`**（尤利·马尔托夫）: 孟什维克核心领袖与国际主义左翼旗手。1903年二大凭党章第一条（28:22:1）与列宁分道；1917年七月夜倡“清一色社会主义政府”遭党内主流否决，十月二大率派退场；1918年工人抗议浪潮中坚持苏维埃合法反对派立场，1920年哈雷大会与季诺维也夫正面交锋痛斥恐怖与二十一条，后流亡柏林病逝。 ‖ `←ORG-bund`[factional-counterpoint|1903]: 同列宁联手驱逐崩得，却在党章第一条上与列宁分裂
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←ORG-bund`[organizational-rival|1903–1917]: 批判民族文化自治，坚持崩得不得独占犹太工人代表权
- **`ORG-mensheviks`**（孟什维克）: 俄国社会民主主义政党（1903–1924），源于1903年二大马尔托夫等与列宁围绕党章第一条及集中制的决裂，主张开放型群众政党与工人自主活动。1917年分化为策烈铁里、但恩主导的入阁“革命护国派”与马尔托夫领导的反战“国际主义派”；十月后开展苏维埃合法反对派抗争，1921年后遭取缔。 ‖ `←ORG-bund`[electoral-ally|1905–1917]: 在1905里加联邦委员会与1917苏维埃中与孟什维克协同，共享护国派争议
- **`ORG-petrograd-soviet`**（彼得格勒工兵代表苏维埃）: 二月革命后诞生于塔夫利达宫的工兵政权，颁布《第一号命令》。执委会主席为齐赫伊泽，策烈铁里是常务局核心并主导革命护国路线。1917-08-31[O.S.]/09-13[N.S.]首次通过布尔什维克决议，托洛茨基随后任主席；十月军事革命委员会成为推翻临时政府的枢纽。 ‖ `←ORG-bund`[faction-in|1917.03–1917.10]: 埃尔利希等代表在十月二大随孟什维克退场
- **`POL-korenizatsiia`**（本土化政策（Коренизация））: 1923年俄共十二大系统确立的民族政策，在一党垄断与组织集权下推进非俄干部录用、行政司法母语化和民族文教。斯大林在语言、边疆发展及第二院否决权上让步，守住代表结构；乌克兰等地深入推行，1926、1928年引发文化经济自主争论。1929年底只是本卡观察截点，并非政策废止。 ‖ `←ORG-bund`[policy-tension|1923–1929]: 苏联本土化与意第绪文教资源分配部分回应崩得旧诉求，却排斥自治议会模式
- **`EVT-1917-02-february-revolution`**（1917年二月革命）: 1917年2月23日至3月3日（俄历；公历3月8—16日），彼得格勒女工罢工、跨厂动员与驻军兵变推翻帝制。杜马委员会接管行政，苏维埃代表工兵，临时政府在革命全权与旧宪制断裂中成立；双重政权并非简单的主动让权。 ‖ `←ORG-bund`[regional-mobilizer|1917.02起]: 边疆工人动员网络延续1905自卫传统

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 1 项)
### `DEB-1903-bolshevik-menshevik-split`：《怎么办？》与1903年布尔什维克—孟什维克分裂实质之争
## [T1] 核心问题定义
《怎么办？》的自发性与意识理论究竟体现精英代替工人，还是欧洲社会民主主义所共有的结合公式？1903年党章、领导机构选举和代表退会如何共同造成分裂，又能否把后来的一党统治直接追溯到当时？必须区分文本论战、组织选择和事后政治后果。

## [T2] 各学派立场对照矩阵
**经验基准**：二大在布鲁塞尔与伦敦举行（会场公历1903-07-30至08-23 [N.S.]，对应俄历07-17至08-10 [O.S.]）；`era`覆盖1902《怎么办？》至1904年论战。第23次会议（08-02 [N.S.] / 07-20 [O.S.]）党章第一条51票唱名表决中，列宁“参加党的一个组织”案以23:28被否、马尔托夫“在组织领导下经常亲自协助”案以28:22（1弃权）通过、整条以35:1（12弃权）通过；随后经济派（阿基莫夫、马尔丁诺夫，2票）与崩得（《记录》口径5人5票，Haimson口径5人4票）退场改变票基，在第31次会议《火星报》三人编委（普列汉诺夫、列宁、马尔托夫）选举中列宁派以25:2（20弃权，Haimson口径22:20:2）获胜而得名“多数派”。更硬的事后反证是：1906年斯德哥尔摩四大在孟什维克62:46占多数的条件下，党章第一条直接改回列宁1903年“参加党的一个组织”公式，证明1903年字句之争并非永久不可逾越的意识形态鸿沟。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 冷战自由派与雅各宾—特卡乔夫连续论（及1904当事人先声） | William Henry Chamberlin (1958, 援引 Karpovich 与 Talmon)；Richard Pipes, *The Russian Revolution* (1990)；[当事人 B 级论战] Leon Trotsky, *Our Political Tasks* (1904) | 将《怎么办？》与1903年建党方案置于法国雅各宾派—布朗基—特卡乔夫“少数密谋家夺权”及俄国激进知识分子职业革命家传统中，视之为一党专政的制度基因；托洛茨基1904年已从党内提出“党组织替代党、中央替代组织、独裁者替代中央”的“替代主义”警告。 | `CLM-jacobin-ancestry-tkachev-blanqui-and-leninism`；`CLM-pipes-1990-patrimonial-state-and-intelligentsia` | 以1917/1930年代结局倒推1902–1903年文本，忽视考茨基主流正统语境及1906年孟什维克自己采纳列宁党章第一条的事实。 |
| 思想史与组织张力 | Leopold H. Haimson, *The Russian Marxists and the Origins of Bolshevism* (1955)；Haimson (1987) | 俄国马克思主义知识分子内部长期存在“自觉性（意识）”与“自发性”的心理及认识论张力，在《怎么办？》、二大组织冲突及孟什维克“党内大家庭”伦理 vs 布尔什维克集中制中集中爆发。 | `CLM-haimson-1955-lenin-what-is-to-be-done`；`CLM-haimson-1955-consciousness-spontaneity`；`CLM-haimson-1955-1903-second-congress-split`；`CLM-haimson-1987-menshevik-party-ethos-and-family` | 知识分子群体心理连续性不能替代对二大逐场议程、崩得退席与编委改选偶然票序的制度分析。 |
| 爱尔福特语境重释 | Lars T. Lih, *Lenin Rediscovered: What Is to Be Done? in Context* (2006) | 《怎么办？》核心是考茨基《爱尔福特纲领》“社会主义与工人运动相结合”的欧洲社民主流公式，旨在以德国SPD模式激发地下工作者信心，绝非轻蔑工人的“担忧工联主义”密谋手册。 | `CLM-lih-2006-erfurtian-merger-formula`；`CLM-lih-2006-kautsky-and-spontaneity`；`CLM-lih-2006-textbook-myth-critique` | 强调1902年文本的爱尔福特共识，容易淡化1903年二大后在中央集权、编委人事与派别组织操作上的真实决裂。 |
| 孟什维克政治传记 | Israel Getzler, *Martov: A Political Biography of a Russian Social Democrat* (1967) | 从马尔托夫对党员资格弹性、老编委集体荣誉及党内自治的维护解释1903年决裂，指出马尔托夫拒任三人编委使组织微差升级为派别分野。 | `CLM-getzler-1967-martov-1903-clause-one` | 马尔托夫个人品格与后期民主社会主义立场不能简单投射为1903年全体“软派”火星派代表的既定纲领。 |
| 帝国边疆社会民主主义 | Eric Blanc, *Revolutionary Social Democracy* (2021) | 以帝国边疆非俄罗斯民族社会民主党（崩得、拉脱维亚、波兰、芬兰等）的群众性合法/半合法组织实践与共同的“革命考茨基主义”，打破仅以俄国中心流亡小报编委为轴的建党叙事。 | `CLM-blanc-2021-revolutionary-kautskyanism-in-empire`；`CLM-blanc-2021-beyond-russocentric-bolshevism` | 边疆宏观组织比较不能取代二大第23次与第31次会议具体党章文本、联邦制否决及唱名票序的微观因果。 |
| 工人能动性与政治修辞辨析 | S. A. Smith (1996/1999，收入 Reginald E. Zelnik 编论文集)；Robert Mayer (1999) | Smith（及Zelnik译注卡纳奇科夫自传）揭示1895–1917年彼得堡“觉悟工人”追求去监护化自治、排斥知识分子两派内斗；Robert Mayer考证列宁1903–1904年的“雅各宾”自称直接承袭普列汉诺夫1901年的法国大革命修辞以打击机会主义，而非效法特卡乔夫或布朗基密谋。 | `CLM-zelnik-1999-worker-intelligentsia-tutelage-tension`；`CLM-zelnik-1999-kanatchikov-conscious-worker-formation`；`CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism` | 概念史修辞澄清与基层工人心态史分属不同分析层面，需与中央党组织制度变迁互证。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 18/18 条)
- **`CLM-haimson-1955-1903-second-congress-split`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. 175-191]: 
- **`CLM-getzler-1967-martov-1903-clause-one`** [`SCH-getzler-israel`(伊斯雷尔·格茨勒) | pp. 78-79]: 
- **`CLM-blanc-2021-borderlands-in-1905-and-1917`** [`SCH-blanc-eric`(埃里克·布兰克) | pp. 20–23, 338–436, 488–531, 457–543]: 
- **`CLM-liber-1992-korenizatsiia-paradox-late-1920s`** [`SCH-liber-george`(乔治·O·利伯) | pp. 155–157; 180–186]: 
- **`CLM-lih-2006-erfurtian-merger-formula`** [`SCH-lih-lars`(拉斯·T·利) | pp. 6-9, 41-49, 74-106, 113-121, 556-557]: 
- **`CLM-sukhanov-1922-october-walkout-tragedy`** [`SCH-sukhanov-nikolai`(尼古拉·苏汉诺夫) | pp. 631–647, 657–660 (PDF pp. 683–699, 709–711)]: 
- **`CLM-blanc-2021-beyond-russocentric-bolshevism`** [`SCH-blanc-eric`(埃里克·布兰克) | pp. 15–16, 23–26]: 
- **`CLM-jacobin-ancestry-tkachev-blanqui-and-leninism`** [`SCH-chamberlin-william-henry`(威廉·亨利·钱伯林) | pp. 251–257 (PDF pp. 2–8)]: 
- **`CLM-pipes-1990-patrimonial-state-and-intelligentsia`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 2 (Official Russia); ch. 4 (The Intelligentsia); cf. Introduction]: 
- **`CLM-haimson-1955-lenin-what-is-to-be-done`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. 132-141]: 
- **`CLM-haimson-1955-consciousness-spontaneity`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. vi-viii, 7-11]: 
- **`CLM-haimson-1987-menshevik-party-ethos-and-family`** [`SCH-haimson-leopold`(利奥波德·海姆森) | pp. 14–17]: 
- **`CLM-lih-2006-kautsky-and-spontaneity`** [`SCH-lih-lars`(拉斯·T·利) | pp. 35-37, 555, 613-667]: 
- **`CLM-lih-2006-textbook-myth-critique`** [`SCH-lih-lars`(拉斯·T·利) | pp. 5, 13-33, 555]: 
- **`CLM-blanc-2021-revolutionary-kautskyanism-in-empire`** [`SCH-blanc-eric`(埃里克·布兰克) | pp. 25–28, 569–578]: 
- **`CLM-zelnik-1999-worker-intelligentsia-tutelage-tension`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | pp. 6-7, 13-15, 18-27, 51-52]: 
- **`CLM-zelnik-1999-kanatchikov-conscious-worker-formation`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | pp. 9-12, 26-27]: 
- **`CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism`** [`SCH-mayer-robert`(罗伯特·迈耶) | pp. 127-129, 140-146]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 2 条 L3 逐日细节见 `timeline/L3_daily/`)
