# 1-Hop 去重平衡上下文包：`POL-war-communism`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`POL-war-communism`** (战时共产主义 | `cards/policies/POL-war-communism.md` | `multi-perspective`): 已覆盖=`emergency-civil-war, ideological-continuity, institutional-carr, revisionist-social-history`；待补=`regional-implementation-granular, full-primary-decree-corpora`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1918年夏至1921年3月苏维埃经济政策总称：余粮收集制、中小工业国有化、取缔私商、货币贬值与实物配给并举；因内战饥荒与国家能力崩溃而强化，却在1921年喀琅施塔得与坦波夫危机下为新经济政策实物税所取代；其性质是应急、乌托邦跃进还是国家统制传统延续，史家分歧剧烈。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **危机叠加与措施集群化（1918.06–1919）**：`1918-05-09 [N.S.]`（苏俄已于1918-02-14改行公历，全俄中执委通过赋予粮食人民委员部非常权力的 **粮食专政／粮食垄断令** 雏形；部分史书按签署/刊布记 `1918-05-13 [N.S.]`），夏秋颁布征收办法，**1919年初** 形成制度化 **余粮收集制（продразвёрстка）**，由国家按定量强征农村“余粮”供应红军与城市（地方执行差异极大）。同期 **大中小企业普遍国有化**、取消大部分私营贸易、废止按劳取酬的多元工资形态，代之以 **实物配给、无偿征用与劳动军事化** 命令；货币急剧贬值使“无货币”经济表面化，但黑市一直存在。
- **内战高峰与“战时共产主义”名目（1919–1920）**：红军以阶级战争形态扩大，交通、燃料与冶金由国家单一调配；托洛茨基推动 **劳动军** 与 **一长制** 强化工厂纪律；苏维埃政权在乡村呈“军事—行政”外在于农民之态（Mawdsley 引坦波夫密报，`CLM-mawdsley-1987-civil-war-militarized-regime`）。史家后称此期为 **战时共产主义（Военный коммунизм）**，但当时布尔什维克亦用“共产主义的仓促实践”“过渡模式”等多种表述，并无唯一法令界定起讫。
- **农民战争、喀琅施塔得与退却（1921.02–03）**：坦波夫等地农民武装反抗征粮；`1921-03-02` **喀琅施塔得起义** 呼唤“没有共产党人的苏维埃”；列宁在俄共十大承认农民战争威胁超过白军（Figes, `CLM-figes-1996-peasant-wars-and-nep-retreat`）。`1921-03-15`–16 **十大** 通过以 **粮食税** 取代余粮收集制、恢复有限贸易的决定框架；`1921-03-21` 人民委员会颁布 **关于以实物税取代征收制** 法令，标志向新经济政策转型的法律节点（详参 `POL-nep`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `POL-nep` | `replaced-by` | 1921-03–12 | 实物税与贸易恢复逐步 dismantle 余粮收集制与全面国有化贯彻强度 | `CLM-figes-1996-peasant-wars-and-nep-retreat` |
| `EVT-1921-kronstadt` | `precipitated-retreat` | 1921-03 | 起义与农村战争共振，促使列宁在十大宣布新经济政策退却 | `DEB-1918-war-communism-ideology-or-emergency` |
| `ORG-workers-opposition` | `simultaneous-crisis-of` | 1920–1921 | 城市工人反对一长制与官僚化，与战时共产主义劳动军事化同场争论 | `CLM-daniels-1960-tenth-congress-turning-point` |
| `POL-ban-on-factions-1921` | `institutionalizes-post-crisis` | 1921-03-16起 | 十大在喀琅施塔得背景下通过派别禁令，经济退却与党组织封闭并行 | `CLM-mawdsley-1987-civil-war-militarized-regime` |
| `PER-trotsky` | `militarized-labor-architect` | 1918–1921 | 劳动军、交通工会军事化与工会国家化主张，代表战时共产主义劳动纪律极点 | Daniels (1960), Service (2009) |
| `ORG-cheka-ogpu` | `enforces-requisition` | 1918–1921 | 契卡/格乌系统镇压拒征与投机，红色恐怖与征粮相互嵌合 | `CLM-pipes-1990-red-terror-leninist-logic`, `CLM-leggett-1981-red-terror-institutionalization` |
| `PER-lenin` | `debated-then-retreated` | 1918–1921 | 先是强调国家资本主义过渡可能，后在危机中批准激进措施；1921年主动宣布退却 | Carr; Lih 批判“乌托邦计划”叙事 |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1918–1921年苏联经历强制征粮、广泛国有化、市场压制与实物配给；1921年3月后粮食税与新经济政策标志着部分核心措施的撤回；政策名称“战时共产主义”为史家归纳，各措施出台时间与地区强度并不整齐划一。
- **主要解释分歧**（详参 `DEB-1918-war-communism-ideology-or-emergency`）：
  - **[内战军事求生应急论 / Evan Mawdsley, Sheila Fitzpatrick 部分论述]** (`CLM-mawdsley-1987-civil-war-militarized-regime`, `CLM-mawdsley-1987-sovdepia-heartland-advantage`): 强调经济崩溃、补给断裂与红军生存需要如何把政权锁进军事—行政形态；Mawdsley 明确指出内战与斯大林主义同为夺权后果，但拒绝“没有内战就不会有斯大林主义”的简单反事实，亦承认内战方法在1920年代末被选择性复活。
  - **[意识形态乌托邦跃进论 / Richard Pipes, Martin Malia]** (`CLM-pipes-1990-red-terror-leninist-logic`; Malia, *The Soviet Tragedy*, 见 `DEB-1918-war-communism-ideology-or-emergency`): 将余粮收集制、恐怖与废法统治解释为布尔什维克反市场社会主义与先锋队权力观的先定展开，而非纯粹外生战争产物；Pipes 尤其强调1917年末契卡与废法的开端早于大规模内战。Malia 从“乌托邦悲剧”长时段论证，危机为激进蓝图扫清障碍——须注意其与 Pipes 论证焦点并不相同，不能合并为单一时间表。
  - **[战时国家统制连续论 / E. H. Carr, Lars T. Lih]** (Carr, *The Bolshevik Revolution*; Lih, “Bukharin’s Illusion”及列宁再发现系列，`CLM-lih-2006-textbook-myth-critique`): Carr 追踪1918–1921年法令序列与国家机构如何在压力下“非计划地”相互牵引，反对把战时共产主义说成列宁事先写定的乌托邦总蓝图；Lih 批判把新经济政策简单定义为对“乌托邦式战时共产主义”的醒悟，强调布尔什维克始终谈“过渡”与俄国落后现实，战时措施应回到当时用语与选项集理解，而非套用后设的“共产主义试验”标签。
  - **[修正派社会史 / Moshe Lewin, S. A. Smith]** (`BIB-021`, `CLM-smith-1983-post-october-centralization`): 从农民抗征、工人车间监督退化与中心城市饥饿出发，论证物质崩溃与阶级结构变动如何迫使政权选择更极端的汲取与监督手段；与纯粹意识形态决定论构成经验性制衡。

## 2. 一跳邻域全量微摘要目录 (去重后共 25 个节点，0 截断)
- **`CON-kulak`**（富农（作为社会阶层与政治定罪标签））: “富农”兼具农村阶层与政治定罪含义：19世纪原指高利贷盘剥者，列宁称农村资产阶级；斯托雷平改革分离户也遭村社如此指斥。1918年为贫农委员会征粮对象，1925年NEP放宽而农村趋向中农化；1928–1929年经刑法107条与雅科夫列夫委员会转为阶级清洗标签。 ‖ `→POL-war-communism`[first-state-requisition-weaponization|1918-06–1921-03]: 以“打击富农投机”为余粮收集制正名，实践中大面积剥夺中农余粮
- **`CON-peasant-commune-obshchina`**（农村公社（米尔 / 村社））: 村社是帝俄至苏俄的乡村自治与土地重分制度。1861年改革保留连环保与重分地；民粹派视为社会主义胚胎，1881年马克思有条件认可其前景，列宁强调资本主义分化，斯托雷平立法拆解。1917–1918年土地重分使其复兴，1922年获法典承认，1929–1930年遭集体化摧毁。 ‖ `→POL-war-communism`[defensive-shell-against|1918-06–1921-03]: 复兴后的村社团结一致抵制贫农委员会分化与余粮收集制，迫使政权转向NEP
- **`CON-state-capitalism`**（国家资本主义（苏维埃政权下的））: 布尔什维克过渡经济概念。列宁1917–1918年以德国战时统制经济为蓝本，将“苏维埃政权下的国家资本主义”定为通向社会主义的进步阶梯，遭左派共产主义者斥为向资本投降；1921年重定义为租让制、租赁与合作社，1923年《论合作社》悄然转向；1925年新反对派反用此词攻击布哈林—斯大林。 ‖ `→POL-war-communism`[displaced-by|1918-06–1921-03]: 内战与全面国有化使和解型国家资本主义作废
- **`CON-workers-control`**（工人监督（工厂委员会与生产者自治））: 工人监督源自1905年车间行动；1917年彼得格勒工厂委员会为保就业、维持生产实行防御性监督，十月后写入《工人监督条例》。1918年起经济崩溃与国有化推动部分委员会并入工会，中央管理与劳动纪律强化；1921年生产者自治方案遭党内否决，但基层实践与合议管理并未骤然消失。 ‖ `→POL-war-communism`[absorbed-into-centralized-glavki-and-piecework-under|1918-06–1921-02]: 全面国有化并未带来工人自治，反而将委员会并入工会、纳入总管理局集权与1919年强制计件制
- **`EVT-1918-09-red-terror-and-left-sr-rupture`**（1918年夏左翼社革党决裂与红色恐怖制度化）: 1918年7月左翼社革党刺杀米尔巴赫，其意在逼废和约抑或夺权存史学争议，随后遭布党镇压并被逐出苏维埃权力核心。8月30日乌里茨基遇害、列宁遇刺后，9月5日红色恐怖法令将集中营隔离与枪决制度化。一党垄断与暴力升级须分别追踪，登记死亡数非全部受害者。 ‖ `→POL-war-communism`[food_conflict_context|1918春夏]: 粮食专政与贫农委员会破坏联盟，非抽象意识形态独自触发。
- **`EVT-1918-1920-russian-civil-war`**（俄国内战（1918–1920））: 1918至1920年红白主战场的内战中，布尔什维克依托中央腹地、军火遗产与铁路机动击败分散白军；征粮和恐怖又激起工农反抗。乌克兰及外高加索的民族国家竞争不能归入简单红白对决，克里米亚撤离仅标志主要白军战线收束，边疆与农民战争仍在延续。 ‖ `→POL-war-communism`[mobilization_and_social_conflict|1918—1921.03]: 征粮与统制支撑战争，也激化城乡矛盾，性质仍有争议
- **`EVT-1918-worker-protest-and-izhevsk-uprising`**（1918年苏俄工人抗议、工厂全权代表会议运动与伊热夫斯克—沃特金斯克大起义）: 1918年春夏，失业、饥荒与基层组织国家化引发工人抗议，丘拉科夫估涉及210—220家企业、10万—25万人。彼得格勒形成非常代表会议，莫斯科局部让步；卡马河军工镇在强征等冲突下起义，伊热夫斯克与沃特金斯克组成人民军，最高约2.5万人，终遭红军反攻瓦解。 ‖ `→POL-war-communism`[social-pressure-and-channeling|1918.03–11]: 工潮暴露复员与断粮危机，促使政权通过征粮队（продотряды）吸纳部分工人并加速向集中军事配给体制演进
- **`EVT-1920-1921-tambov-and-peasant-revolts`**（坦波夫安东诺夫起义与1920–1921年农民绿军风暴）: 1920年坦波夫抗征粮冲突扩大为安东诺夫领导的农民战争，与其他省份起义及城市工潮共振，暴露苏维埃农村统治危机。1921年粮食税让步与重兵围剿、人质及集中营政策并行；主力在夏季受挫，零星抵抗延续，不能把新经济政策视为农村随即恢复和解。 ‖ `→POL-war-communism`[procurement_conflict|1918—1921.03]: 余粮征集、地方配额与暴力促使村社武装反抗
- **`EVT-1921-1922-volga-famine-and-church-valuables-crisis`**（伏尔加—乌拉尔饥荒、国际救济与教会珍宝冲突）: 内战、征粮与生产运输崩溃叠加1920—1921年歉收旱灾，酿成大饥荒；Figes估全国死亡约500万。ARA与国家救济并行，独立赈济遭压制。1922年征收教会财物引发冲突；列宁3月19日信主张利用饥荒推进没收，其目标是反动神职人员还是教会本身，史家有分歧。 ‖ `→POL-war-communism`[intensifies_vulnerability|1918–1921]: 长期征收消耗储备，旱灾又重创收成；Figes ch23 L27–28；地方征粮差异见罗利编著札记。
- **`EVT-1921-kronstadt`**（喀琅施塔得水兵起义）: 1921年二月底至三月，喀琅施塔得水兵与居民以十五条决议要求改选苏维埃、开放劳动者及左翼政治自由，并成立临时革命委员会。红军跨冰夺回要塞，镇压与实物税、禁派决议交叠；经济退却早已酝酿，起义加剧其紧迫性，却未带来政治权力的开放。 ‖ `→POL-war-communism`[social_and_economic_background|1920—1921.03]: 征粮、配给、阻击队及军事化统制形成反抗对象 ； `←POL-war-communism`[precipitated-retreat|1921-03]: 起义与农村战争共振，促使列宁在十大宣布新经济政策退却
- **`INS-rkka-red-army-and-rvr`**（工农红军与共和国革命军事委员会（РККА 与 РВСР））: 工农红军由1918年初志愿建军转向征兵与集中指挥；共和国革命军事委员会依靠前沙俄军事专家、政治委员及铁路内线组织内战。战后大裁军和伏龙芝改革建立正规军与地方民兵混合体制，1925至1929年伏罗希洛夫主政与干部工农化在政治控制与训练效能间形成持久张力。 ‖ `→POL-war-communism`[动员体制耦合|1918–1921]: 余粮征集、军工配给与部队动员形成相互锁定的军事化体制。
- **`MTG-1919-03-8th-party-congress`**（俄国共产党（布尔什维克）第八次代表大会）: 1919年3月18日至23日，俄共（布）八大在内战中通过第二党纲，围绕民族自决、红军正规化与党内集中化激烈争辩，提出巩固与中农的联盟。大会及会后一中全会确立政治局、组织局和书记处常设框架，否定党组织联邦制并强化党团对苏维埃的控制；军事反对派与民主集中派的抗辩凸显集权并非无争议。 ‖ `→POL-war-communism`[rural-context|1919-03]: 提出巩固中农联盟，但仍在战时余粮收集制与高度集中经济框架内运行。
- **`ORG-cheka-ogpu`**（全俄肃反委员会—国家政治保卫局）: 苏俄与苏联早期政治警察机关（1917–1934），由捷尔任斯基创立。历经全俄肃反委员会（ВЧК，1917–1922）、国家政治保卫局（ГПУ，1922–1923）与国家政治保卫总局（ОГПУ，1923–1934）三阶段，从法外非常机构演变为直属政治局的常设宪制部门，执行红色恐怖与强制集体化。 ‖ `→POL-war-communism`[coercive-enforcement-pillar|1918–1921]: 承担武装征粮督导、打击黑市投机、镇压工人罢工与农民起义（坦波夫、喀琅施塔得）及管理强制劳动营的全面专政职能 ； `←POL-war-communism`[enforces-requisition|1918–1921]: 契卡/格乌系统镇压拒征与投机，红色恐怖与征粮相互嵌合
- **`ORG-left-communists-1918`**（1918年左翼共产主义者）: 1918年初俄共（布）内以布哈林、奥新斯基、拉狄克、普列奥布拉任斯基为首的极左集团，借《共产党人》（`Коммунист`）杂志反对《布列斯特和约》与列宁“国家资本主义”一长制；俄共七大批准和约后作为有组织派别逐步消解，但其国际主义与反官僚化诉求深刻塑造此后党内反对派谱系。 ‖ `→POL-war-communism`[ideological-precursor-debate|1918–1921]: 1918年春国有化与工人管理之争构成战时共产主义“意识形态抑或应急”争鸣的关键前史
- **`ORG-makhnovshchina`**（马赫诺运动（乌克兰革命起义军））: 1918–1921年南俄乌克兰无政府共产主义农民—雇农武装：以古利亚伊波列为基地设“自由苏维埃”与公社，以机枪马车（тачанка）机动战术三度联红击白；红军背盟后于1921年覆灭。史学上既是内战地方变体，也是农民反叛与现代政党夺权模式的经典对照案例。 ‖ `→POL-war-communism`[resisted|1919–1921]: 拒斥余粮收集制与契卡恐怖，迫使红军暂与叛军妥协
- **`PER-antonov`**（亚历山大·安东诺夫）: 社会革命党出身的坦波夫农民大起义军事统帅（1889–1922）。沙俄苦役犯，1917年后任基尔萨诺夫县民警局长，1918年夏因抗拒征粮转入地下。1920年8月卡缅卡暴动后任游击集团军参谋长，依托“劳动农民联盟”建立平行农村政权并倒逼新经济政策退却，1922年6月战死。 ‖ `→POL-war-communism`[rebelled_against|1918-08–1921-02]: 外来征粮专员的暴力配额与连坐滥捕迫使其从县民警局长转入地下并点燃全省起义
- **`PER-makhno`**（涅斯托尔·马赫诺）: 乌克兰古利亚伊波列无政府共产主义农民统帅（1888–1934）。创建“革命起义军（黑军）”与自由苏维埃实验；内战中与红军多次合作、破裂，1919年秋破袭邓尼金后方，1920年11月其部队参加克里米亚战役，随即遭红军全面围剿，1921年越境流亡并客居巴黎。 ‖ `→POL-war-communism`[armed_peasant_resister|1919–1921]: 高举“拥护苏维埃但反对共产党人”口号，武装处决征粮队员与契卡人员、抵制国营农场制度
- **`POL-decrees-on-peace-and-land-1917`**（1917年和平法令与土地法令）: 苏维埃二大1917-10-26[O.S.]/11-08[N.S.]晚约21时后通过和平法令，倡公开谈判、不兼并不赔款；土地法令于10-27[O.S.]/11-09[N.S.]凌晨1时后表决，无偿废地主所有制并收入242份农民委托书编成的纲领。回应士兵农民诉求，落实仍历冲突。 ‖ `→POL-war-communism`[subsequent-tension|1918–1921]: 战时征粮与基层权力冲突使和平、土地承诺形成的支持受到侵蚀
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←POL-war-communism`[replaced-by|1921-03–12]: 实物税与贸易恢复逐步 dismantle 余粮收集制与全面国有化贯彻强度
- **`ORG-workers-opposition`**（工人反对派）: 俄共（布）党内以产业工人和工会干部为主体的左翼反对派（1920–1922），由什利亚普尼科夫、梅德韦杰夫及理论代言人柯伦泰领导。在1920–1921年工会争论中痛斥党政官僚化与专家“一长制”，主张由“全俄生产者代表大会”及工会自治管理国民经济；1921年十大被定性为无政府工团主义倾向并遭解散。 ‖ `←POL-war-communism`[simultaneous-crisis-of|1920–1921]: 城市工人反对一长制与官僚化，与战时共产主义劳动军事化同场争论
- **`POL-ban-on-factions-1921`**（《关于党的统一》派别禁令）: 俄共十大于1921年3月16日通过《关于党的统一》，要求解散按纲领组成的派别，并保留规定渠道的批评。秘密第七条设中央领导成员的特殊处分程序；1924年1月公开宣读、1926年7月首次动用开除季诺维也夫出政治局，危机措置遂渐成约束反对派的工具，但不同年份执行不等同原条文。 ‖ `←POL-war-communism`[institutionalizes-post-crisis|1921-03-16起]: 十大在喀琅施塔得背景下通过派别禁令，经济退却与党组织封闭并行
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←POL-war-communism`[militarized-labor-architect|1918–1921]: 劳动军、交通工会军事化与工会国家化主张，代表战时共产主义劳动纪律极点
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←POL-war-communism`[debated-then-retreated|1918–1921]: 先是强调国家资本主义过渡可能，后在危机中批准激进措施；1921年主动宣布退却
- **`PER-dzerzhinsky`**（费利克斯·捷尔任斯基）: 波兰立陶宛社民党与布尔什维克领导人。1917年建全俄肃反委员会（契卡）并续掌GPU/OGPU至逝世，奠定苏维埃安全与法外镇压体制；1924–1926年兼任最高国民经济委员会主席，力挺新经济政策市场均衡、保护技术专家并反对超工业化，1926年7月预警“红色独裁者”后猝逝于中央全会。 ‖ `→POL-war-communism`[security-enforcer|1917.12-1921]: 主持创立全俄肃反委员会(契卡)并在内战期执行红色恐怖；1924年后任最高国民经济委员会主席转而支持新经济政策财政平衡。
- **`EVT-1918-03-brest-litovsk-treaty`**（1918年布列斯特-里托夫斯克和约危机与签约）: 1917年12月停战至1918年3月签约，列宁主和、托洛茨基“不战不和”与布哈林革命战争路线交锋。德军进逼后，中央2月23日以7赞成、4反对、4弃权接受最后通牒；和约保存政权，也加深党内裂痕并促使左翼社革党退阁。 ‖ `→POL-war-communism`[precursor_to|1918.03–1918夏]: 和约后疏散工业、征用粮食，内战经济体制成型。

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 1 项)
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


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 23/23 条)
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-figes-1996-peasant-wars-and-nep-retreat`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 775-785]: 
- **`CLM-daniels-1960-tenth-congress-turning-point`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 146-153]: Daniels：1921年十大将党统一转化为压缩合法反对空间的组织制度
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-leggett-1981-red-terror-institutionalization`** [`SCH-leggett-george`(乔治·莱格特) | pp. 56-59, 102-115, 144-145 (PDF pp. 94-97, 140-153, 182-183)]: 
- **`CLM-mawdsley-1987-sovdepia-heartland-advantage`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 93, 329-331, 337]: 
- **`CLM-lih-2006-textbook-myth-critique`** [`SCH-lih-lars`(拉斯·T·利) | pp. 5, 13-33, 555]: 
- **`CLM-smith-1983-post-october-centralization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | pp. 208, 239–263 (PDF pp. 220, 251–275)]: 
- **`CLM-ilyukhov-war-communism-leveling-vs-nep-piecework`** [`SCH-ilyukhov-alexander`(亚历山大·伊利尤霍夫) | pp. 43–50]: 
- **`CLM-churakov-2004-soviet-worker-protest-dynamics-1918`** [`SCH-churakov-dmitry`(德米特里·奥列戈维奇·丘拉科夫) | pp. 84-88, 352-355]: 
- **`CLM-dugarm-2001-tambov-grain-warfare-and-antonovshchina`** [`SCH-raleigh-donald`(唐纳德·J·罗利) | Local PDF pp. 103–138; English print pagination not verified]: 
- **`CLM-carr-1952-war-communism-internal-contradictions`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 70-120 (Chs. 17–18)]: 
- **`CLM-raleigh-2001-local-bolshevik-violence-and-clientelism`** [`SCH-raleigh-donald`(唐纳德·J·罗利) | Local PDF pp. 104, 112–130; English print pagination not verified]: 
- **`CLM-avrich-1970-soviets-without-bolsheviks`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 198-201, 179-180]: 
- **`CLM-leggett-1981-vecheka-extra-legal-origins`** [`SCH-leggett-george`(乔治·莱格特) | pp. 17-22, 47-49 (PDF pp. 55-60, 85-87)]: 
- **`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 56–58, 69, 185–188, 217–218, 283–284]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-smith-sa-1983-from-workers-control-to-nationalization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 155–156, 166–169, 177–179, 184–186, 192（即源文件标注 PDF pp. 160–161, 171–174, 182–184, 189–191, 197）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-daniels-1960-left-communists-1918`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 70-81]: Daniels：1918年左翼捍卫革命纲领，却在分裂关头受党统一约束
- **`CLM-zemskov-1929-dekulakization-demographic-baseline`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | PDF pp. 6-11, 15-19, 52, 218 (原书 pp. 4-9, 13-17, 50, 216)]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 6 条，另有 6 条 L3 逐日细节见 `timeline/L3_daily/`)
- **1918-05-25 [N.S.]** (`TL-W15-L1-E07-07`, L1): **捷克军团冲突扩大** — 铁路沿线冲突与地方反布尔什维克政权兴起，内战战线迅速扩展。
- **1918-06-08 [N.S.]** (`TL-W3-1918-06-08`, L2): **颁布贫农委员会法令** — 拉宾诺维奇写6月8日。派普斯写6月11日。征粮队政策亦有5月9日（拉宾诺维奇）与5月13日、5月20日（派普斯）的差别，不并入本日。
- **1918-11-18 [N.S.]** (`TL-W15-L1-E07-10`, L1): **高尔察克鄂木斯克政变** — 白军权威重组与反布尔什维克阵营内部冲突同时显现。
- **1919-01 [N.S.]** (`TL-W3-1919-01`, L2): **余粮收集制法令** — 莫兹利把 Food Levy (prodrazverstka) 法令放在1919年1月，按省分摊、强制交出剩余。派普斯年表把同月写成实物税，那是误标；实物税是1921年3月的决定。官方征收量他印为1918–1919年度1.08亿普特（195,000吨），与普特换算不一致，保留原印。没有日号。
- **1919-01-01 [N.S.]** (`TL-W15-L1-E07-11`, L1): **余粮收集制制度化** — 征粮配额机制成为战时经济核心，不能与1921年粮食税混称。
- **1920-11-14 [N.S.]** (`TL-W15-L1-E07-13`, L1): **弗兰格尔撤离克里米亚** — 南俄白军主要战场结束，农民战争、边疆战争与经济危机仍继续。
