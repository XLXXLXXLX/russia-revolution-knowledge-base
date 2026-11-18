# 1-Hop 平衡上下文包：`EVT-1918-1920-russian-civil-war` (俄国内战（1918–1920）)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/events/EVT-1918-1920-russian-civil-war.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `military-structural, archival-soviet-military, social-history-green, democratic-counterrevolution`
- **待补齐视角**: `full-soldier-diary-corpus, intervention-force-comparative`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `full-soldier-diary-corpus, intervention-force-comparative`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1918–1920年苏俄内战：布尔什维克依托“苏托邦”人口、军火与莫斯科铁路枢纽内线机动，先后粉碎高尔察克、邓尼金、弗兰格尔白军及马赫诺黑军，并压制社革党第三力量；协约国干涉与边疆民族武装相互牵制。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **开局与阵营格局（1918）**：布列斯特和约后红军由志愿制转向普遍义务兵役（`1918-05-29`），托洛茨基在共和国革军委下强制起用逾4.8万前沙皇军官（военспецы）与政委双签制（`INS-rkka-red-army-and-rvr`）。反布尔什维克“联盟”分化：**白军**（高尔察克、邓尼金、尤登尼奇、弗兰格尔）据边疆外线进攻；**绿线/民主反革命**（社革党 Komuch、乌法国务会议等）试图填补红白真空却被右翼政变吞噬（`CLM-smith-scott-2011-psr-third-force-collapse`）；**黑军**（马赫诺）与**民族分离武装**（芬兰、波兰、波罗的海、乌克兰、格鲁吉亚等）各自为政，削弱反苏统一战线。
- **1919决战年（东—南线转折）**：伏龙芝东线南集群于4–6月击溃高尔察克；红军经铁路南调6万精锐后，于9–10月奥廖尔—沃罗涅日轴线以局部兵力密度优势粉碎邓尼金（`CLM-kakurin-1928-red-army-interior-lines-strategy`）。白军分进合击失序，马赫诺切入邓尼金后方加剧溃败（`CLM-mawdsley-1987-white-movement-structural-defeat`）。
- **1920收束（波苏战争与南线）**：红军追击邓尼金残部至克里米亚边界；1920年5–8月波苏战争延缓西线；南方面军于1920年11月歼灭弗兰格尔（`PER-frunze` 指挥南线关键战役）。至1920年11月主要对资内战战线大体停火，征粮—农民战争危机转入1921年坦波夫与喀琅施塔得阶段。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `INS-rkka-red-army-and-rvr` | `institutional-vehicle` | 1918–1920 | 红军专家—政委体制与突击战线铁路调配承载内线战略 | `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` |
| `ORG-psr` | `third-force-collapsed` | 1918夏 | Komuch 借捷克斯洛伐克军团起事却因战争狂热与无自有兵力遭白卫政变清扫 | `CLM-smith-scott-2011-psr-third-force-collapse` |
| `PER-trotsky` | `commanded-red-army` | 1918–1920 | 主持建军、起用военспецы并统筹多战线，奠定胜利组织框架 | `CLM-kakurin-1928-red-army-interior-lines-strategy` |
| `POL-war-communism` | `sustained-mobilization` | 1918–1920 | 余粮征集与强制征用支撑红军规模亦激化农村敌对 | `DEB-1918-war-communism-ideology-or-emergency` |
| `EVT-1918-03-brest-litovsk-treaty` | `enabled-pivot` | 1918.03起 | 退出大战释放兵力与政治注意力投入内战 | `POL-brest-litovsk-treaty` |
| `POL-brest-litovsk-treaty` | `context` | 1918 | 和约边界划定苏维埃初期战略纵深 | 同上 |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：布尔什维克控制旧帝国人口、军火库存最丰厚的中央地带；白军外线分散、总兵力峰值远低于红军；1919年是决定性战役年。
- **主要解释分歧**：
  - **[地缘—结构派 / Evan Mawdsley]**：胜利系苏托邦人口—工业—军火垄断与白军土地、民族政策破产的结构叠加（`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`、`CLM-mawdsley-1987-white-movement-structural-defeat`）。
  - **[红军官方战略史 / Nikolai Kakurin (1928)]**：内线“梯次累积突击”与突击战线供给机制将物质优势转化为战役胜势（`CLM-kakurin-1928-red-army-interior-lines-strategy`）；成书于个人崇拜篡改前，保留加米涅夫—统帅部争论原貌。
  - **[民主反革命—绿线史 / Radkey经 Smith 2011 文件名索引]**：社革党第三力量因1917后丧失农民武装基础与战争狂热自毁，非单纯军事不敌（`CLM-smith-scott-2011-psr-third-force-collapse`）。
  - **[苏联正统与托洛茨基辩护]**：前者强调革命人民性与党的领导；后者突出托洛茨基建军天才——须与 Mawdsley/Kakurin 结构性解释对勘，避免单因英雄史。

## 2. 一跳邻域等权重微摘要 (共 17 个关联节点，严防大卡霸占上下文)
### 邻居节点: `INS-rkka-red-army-and-rvr`
- **时效关系边** (`INS-rkka-red-army-and-rvr` → `EVT-1918-1920-russian-civil-war` | `won-interior-lines-war` | 有效时段: `1918-1920`): 依托苏维埃腹地6000万人口、沙皇中央军火库与莫斯科放射铁路网，以逾4.8万军事专家与政委双签制在多线内战中击溃分散白军。
- **时效关系边** (`EVT-1918-1920-russian-civil-war` → `INS-rkka-red-army-and-rvr` | `institutional-vehicle` | 有效时段: `1918–1920`): 红军专家—政委体制与突击战线铁路调配承载内线战略
- **节点定性微摘要 [T1]** (完备度 `draft`): 苏维埃武装中枢：1918年1月15日（公历1月28日）颁令组建志愿红军，3–9月托洛茨基出任陆海军人民委员暨共和国革军委（RVSR）主席，改行普遍义务兵役、征召逾4.8万前沙皇军官（военспецы）与政治委员双签制；1919八大击退军事反对派与察里津集团；1924–1925伏龙芝改革转向正规军与地方民兵混合体制。

### 邻居节点: `PER-kolchak`
- **时效关系边** (`PER-kolchak` → `EVT-1918-1920-russian-civil-war` | `eastern-white-supreme-ruler` | 有效时段: `1918.11-1920.02`): 1918年11月18日鄂木斯克政变推翻社革党督政府自任最高执政，1919春西进遭伏龙芝东线红军击溃并于伊尔库茨克被处决。
- **节点定性微摘要 [T1]** (完备度 `draft`): 高尔察克（1874–1920），极地探险家、黑海舰队司令；1918年11月18日鄂木斯克政变推翻社革党全俄临时政府，自封“全俄最高执政”；1919春攻势被伏龙芝率红军东线南集群击溃，1920年2月7日在伊尔库茨克被枪决。

### 邻居节点: `PER-denikin`
- **时效关系边** (`PER-denikin` → `EVT-1918-1920-russian-civil-war` | `southern-white-commander` | 有效时段: `1918.04-1920.04`): 统率南俄武装力量于1919年秋推进至奥廖尔逼近莫斯科，因地主复辟、后方马赫诺起义及大俄罗斯沙文主义断送波兰与哥萨克配合而全军覆没。
- **节点定性微摘要 [T1]** (完备度 `draft`): 邓尼金（1872–1947），南俄武装力量总司令；1919年夏秋挥师北进占奥廖尔直指莫斯科；纵容“沙拉班”地主复辟与“统一不可分割俄罗斯”口号疏远农民、哥萨克与波兰，奥廖尔战败后全线崩溃，1920年3月自新罗西斯克撤离；此后流亡，至死未再掌兵。

### 邻居节点: `ORG-makhnovshchina`
- **时效关系边** (`ORG-makhnovshchina` → `EVT-1918-1920-russian-civil-war` | `black-army-swing-force` | 有效时段: `1918-1921`): 以机枪马车高机动游击战重创邓尼金战略后方并助红军攻克克里米亚，旋即遭苏维埃政权清剿覆灭。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1918–1921年南俄乌克兰无政府共产主义农民—雇农武装：以古利亚伊波列为基地设“自由苏维埃”与公社，以机枪马车（тачанка）机动战术三度联红击白；红军背盟后于1921年覆灭。史学上既是内战地方变体，也是农民反叛与现代政党夺权模式的经典对照案例。

### 邻居节点: `ORG-psr`
- **时效关系边** (`EVT-1918-1920-russian-civil-war` → `ORG-psr` | `third-force-collapsed` | 有效时段: `1918夏`): Komuch 借捷克斯洛伐克军团起事却因战争狂热与无自有兵力遭白卫政变清扫
- **节点定性微摘要 [T1]** (完备度 `draft`): 俄国新民粹派政党（1901/02–1922），在切尔诺夫领导下确立“土地社会化”纲领，并曾设“战斗队”开展政治暗杀。1917年成为全俄最大政党并赢得立宪会议选举多数，但年底分裂出左翼社会革命党；内战中“第三条道路”溃败，经1922年莫斯科公审后在国内实质瓦解。

### 邻居节点: `PER-trotsky`
- **时效关系边** (`EVT-1918-1920-russian-civil-war` → `PER-trotsky` | `commanded-red-army` | 有效时段: `1918–1920`): 主持建军、起用военспецы并统筹多战线，奠定胜利组织框架
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。

### 邻居节点: `POL-war-communism`
- **时效关系边** (`EVT-1918-1920-russian-civil-war` → `POL-war-communism` | `sustained-mobilization` | 有效时段: `1918–1920`): 余粮征集与强制征用支撑红军规模亦激化农村敌对
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1918年夏至1921年3月苏维埃经济政策总称：余粮收集制、中小工业国有化、取缔私商、货币贬值与实物配给并举；因内战饥荒与国家能力崩溃而强化，却在1921年喀琅施塔得与坦波夫危机下为新经济政策实物税所取代；其性质是应急、乌托邦跃进还是国家统制传统延续，史家分歧剧烈。

### 邻居节点: `EVT-1918-03-brest-litovsk-treaty`
- **时效关系边** (`EVT-1918-1920-russian-civil-war` → `EVT-1918-03-brest-litovsk-treaty` | `enabled-pivot` | 有效时段: `1918.03起`): 退出大战释放兵力与政治注意力投入内战
- **节点定性微摘要 [T1]** (完备度 `draft`): 1917年12月停战谈判至1918年3月签约：党内列宁“割地喘息”派、托洛茨基“不战不和”与布哈林“革命战争”派激烈对决；2月18日德军恢复进攻并经2月18/19日夜 7:5:1 试探性电告后，2月23日（公历）中央委员会以 **7:4:4** 接受严苛最后通牒，3月3日签约并经俄共七大批准，左翼社革党遂退出人民委员会。

### 邻居节点: `POL-brest-litovsk-treaty`
- **时效关系边** (`EVT-1918-1920-russian-civil-war` → `POL-brest-litovsk-treaty` | `context` | 有效时段: `1918`): 和约边界划定苏维埃初期战略纵深
- **节点定性微摘要 [T1]** (完备度 `draft`): 苏俄与同盟国于1918年3月3日签署的和约使俄国退出第一次世界大战，承认重大领土损失；德国战败后苏俄于11月宣布废除。

### 邻居节点: `MTG-1919-03-8th-party-congress`
- **时效关系边** (`MTG-1919-03-8th-party-congress` → `EVT-1918-1920-russian-civil-war` | `strategic-context` | 有效时段: `1919`): 1919决战年党政—军事体制在八大定型
- **节点定性微摘要 [T1]** (完备度 `draft`): 1919年3月18–23日俄共（布）八大：斯维尔德洛夫逝世后通过第二党纲，正式常设政治局—组织局—书记处三元体制，列宁击败军事反对派关于反военспецy的激进主张，并宣告联合中农路线。

### 邻居节点: `ORG-komuch-and-democratic-counterrevolution`
- **时效关系边** (`ORG-komuch-and-democratic-counterrevolution` → `EVT-1918-1920-russian-civil-war` | `third-force-collapse-pivot` | 有效时段: `1918.06–11`): 科穆奇兴衰体现东部反布尔什维克阵营向军事独裁转变，其他地区仍有独立武装
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1918年6月8日社会革命党人在捷克军团占领萨马拉后建立“立宪会议成员委员会”（Комуч），9月23日在乌法合组五人全俄临时政府（乌法督政府），试图构建独立于红白之间的“民主反革命”。因强征农民、依赖旧军官“保护色”并遭左右夹击，终在1918年11月18日高尔察克政变中覆灭。

### 邻居节点: `PER-frunze`
- **时效关系边** (`PER-frunze` → `EVT-1918-1920-russian-civil-war` | `commanded-decisively` | 有效时段: `1919–1920`): 东线破高尔察克、南线灭弗兰格尔，为红军1919–20胜利的核心野战指挥官
- **节点定性微摘要 [T1]** (完备度 `draft`): 米哈伊尔·伏龙芝（1885–1925），内战红军名将：1919年东线击溃高尔察克，1920年南线攻克弗兰格尔克里米亚；1923年十二大迫斯大林民族政策让步，1924–1925主持军事改革接替托洛茨基，1925年10月手术后猝死。

### 邻居节点: `PER-kornilov`
- **时效关系边** (`PER-kornilov` → `EVT-1918-1920-russian-civil-war` | `white-founder` | 有效时段: `1917.11–1918.04`): 在顿河创建白卫志愿军并领导“冰雪行军”，奠定南俄白军军官团核心与“反政治军事专政”传统
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 哥萨克平民出身的俄军步兵上将、最高统帅与白卫志愿军缔造者。1917年7月接任最高统帅；临时政府恢复前线死刑，他要求扩大适用，8月底“科尔尼洛夫事件”中与克伦斯基决裂，派克雷莫夫第3骑兵军扑向首都溃败；11月逃赴顿河创建白卫志愿军，`1918-04-13` 强攻叶卡捷琳诺达尔时被红军炮弹击毙。

### 邻居节点: `PER-makhno`
- **时效关系边** (`PER-makhno` → `EVT-1918-1920-russian-civil-war` | `decisive_third_force_belligerent` | 有效时段: `1918–1921`): 1919年秋撕裂邓尼金战略后方、1920年11月参战锡瓦什渡海，深刻左右南线内战战局
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 乌克兰古利亚伊波列无政府共产主义农民统帅（1888–1934）。创建“革命起义军（黑军）”与自由苏维埃实验；内战中与红军多次合作、破裂，1919年秋破袭邓尼金后方，1920年11月其部队参加克里米亚战役，随即遭红军全面围剿，1921年越境流亡并客居巴黎。

### 邻居节点: `PER-savinkov`
- **时效关系边** (`PER-savinkov` → `EVT-1918-1920-russian-civil-war` | `anti-bolshevik-organizer` | 有效时段: `1918–1920`): 组织反苏地下网络与武装，支持雅罗斯拉夫尔起事和波兰战时活动
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 社会革命党战斗组织的重要组织者、作家与反布尔什维克活动家。早年参与策划暗杀沙皇高级官员；1917年任陆军部副部长（后为代理部长），卷入科尔尼洛夫事件并被社革党开除；1918年组建保卫祖国与自由同盟（SZRiS），1919–1921年在巴黎、华沙经营流亡反苏运动并于1921年重组为人民同盟（NSZRiS）。1924年被苏联国家政治保卫总局以“辛迪加-2”诱捕，当庭认罪后死刑改判十年；1925年拘押中死亡，官方自杀说和他杀疑云均需结合证据审慎评估。

### 邻居节点: `PER-struve`
- **时效关系边** (`PER-struve` → `EVT-1918-1920-russian-civil-war` | `white-government-diplomat` | 有效时段: `1918–1920`): 支持南俄白军并于1920年负责外交事务
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 经济学家、政论家与俄国自由派政治家。司徒卢威从1890年代的合法马克思主义者、1898年俄国社会民主工党《宣言》起草人，转向主张宪政与强大民族国家的自由主义；1902年在斯图加特创办《解放》，1909年参与《路标》，批判激进知识分子传统；1915年因反对米留可夫的妥协路线退出立宪民主党中央委员会。内战时从莫斯科“全国中心”转向南俄白军，1920年任弗兰格尔政府外交主管，后流亡并逝于巴黎。

### 邻居节点: `PER-wrangel`
- **时效关系边** (`PER-wrangel` → `EVT-1918-1920-russian-civil-war` | `final-white-commander` | 有效时段: `1918.08–1920.11`): 1919年夏攻克察里津，1920年4–11月在克里米亚领导白军最后一战并组织14.6万人海上撤离
- **节点定性微摘要 [T1]** (完备度 `draft`): 彼得·尼古拉耶维奇·弗兰格尔（1878–1928），人称“黑男爵”，南俄白军末代最高统帅。1919年夏率高加索集团军攻占察里津，因主张沿伏尔加河东进接应高尔察克、批评三面分兵而与邓尼金公开决裂；1920年4月在新罗西斯克惨败后接掌克里米亚残部，改组“俄罗斯军队”，联手克里沃舍因与司徒卢威推行承认农民有偿取得已占土地的土地法令（“用右翼手腕推行左翼政策”）并获法国事实承认；1920年11月彼列科普—锡瓦什战役战败后组织约14.6万人海上撤往君士坦丁堡，流亡期间创立“俄罗斯全军联盟（РОВС）”，1928年卒于布鲁塞尔。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1918-red-terror-and-civil-war-origins`：红色恐怖、契卡扩张与内战期一党专政起源之争（1918–1921）
## [T1] 核心问题定义
1918–1921年红色恐怖、契卡法外处决、对社会主义反对派的镇压，以及内战期间政党竞争被压缩为一党统治，应被解释为布尔什维克意识形态与列宁主义权力逻辑的宿命展开，还是多重危机（经济崩溃、联盟破裂、地方失控、内战动员）下可错链条上的制度选择？恐怖与一党制是同一过程还是须分时段因果？

## [T2] 各学派立场对照矩阵

**经验共识**：1917年12月契卡（全俄肃反委员会）成立；1918年7月左派社会革命党起义后左翼社会主义者被逐出权力结构；1918年9月5日人民委员会颁布《关于红色恐怖》决议；内战1918–1920在多条战线同时进行；1918–1921征粮与契卡行动在地方相互嵌合。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **意识形态宿命论** | Richard Pipes, *The Russian Revolution* (1990); Orlando Figes, *A People's Tragedy* (1996) | 强调反自由主义知识分子传统、列宁废法统治与阶级敌人话语，使恐怖成为夺取与巩固权力的内在逻辑；Figes 另重农民“悲剧”道德经济。 | `CLM-pipes-1990-red-terror-leninist-logic` | 时间线易前推到1917末，低估联盟期与反对派选项；Figes 与 Pipes 因果权重不一。 |
| **复合危机与联盟破裂论** | Alexander Rabinowitch, *The Bolsheviks in Power* (2007) 等 | 彼得格勒首年追踪与左派社革党联盟从执政到破裂；恐怖升级与粮食危机、暗杀、前线失败交织，而非单线预谋。 | `CLM-rabinowitch-2007-left-sr-coalition-collapse`, `CLM-rabinowitch-2007-contingency-of-dictatorship` | 首都政党政治详尽，偏远地方契卡实践待补。 |
| **制度史与阶段论** | George Leggett, *The Cheka: Lenin's Political Police* (1981); Ilya S. Ratkovsky（及契卡编年史学） | Leggett：契卡从法外 origin 到 GPU 连续体制化；Ratkovsky：1918 夏已有人质与处决规模，9月5日法令是公开化节点而非“零起点”。 | `CLM-leggett-1981-vecheka-extra-legal-origins`, `CLM-leggett-1981-red-terror-institutionalization`, `CLM-leggett-1981-cheka-to-gpu-continuity`, `CLM-cheka-chronicle-hostage-and-local-autonomy`, `CLM-cheka-chronicle-suppression-of-socialist-rivals` | Leggett 偏重中央法令；地方自治与契卡失控需档案对勘。 |
| **1914–1921 总体战治理连续论** | David G. Hoffmann, *Cultivating the Masses: Modern State Practices and Soviet Socialism, 1914–1939* (2011) | 征粮、动员、战备与“培养大众”技术沿袭一战国家实践；苏联社会主义是欧洲现代国家治理谱系的一极，而非凭空乌托邦。 | `CLM-hoffmann-2011-continuum-of-total-war-1914-1929`, `CLM-hoffmann-2011-enlightenment-and-coercion-duality`, `CLM-hoffmann-2011-soviet-socialism-as-european-modernity` | 连续性不等于免除布尔什维克政党特有选择责任。 |
| **内战军事—地理决定论（背景）** | Evan Mawdsley, *The Russian Civil War* (1987) | 红军人口—工业内线优势与白军结构性政策失败解释内战结局；为恐怖与征粮提供战略背景，不单独承担一党制意识形态解释。 | `CLM-mawdsley-1987-civil-war-militarized-regime`, `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` | 军事动员不等于党内反对派清洗因果。 |

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

## 4. 关联时间线锚点 (共 1 条)
- **1917-11-19 [O.S.] / 1917-12-02 [N.S.]** (`TL-W36-1917-12-02-01`, L3): **科尔尼洛夫、邓尼金等逃出贝霍夫监狱南下顿河；左翼社革党一大开幕** — 在克雷连科抵莫吉廖夫前一日，科尔尼洛夫、邓尼金、卢科姆斯基、马尔科夫等从贝霍夫修道院监狱越狱南逃顿河筹组志愿军；同日左翼社会革命党召开第一次全国代表大会（11-19至11-28），正式独立建党。
