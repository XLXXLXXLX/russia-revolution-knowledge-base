# 1-Hop 平衡上下文包：`MTG-1927-12-15th-party-congress` (联共（布）第十五次代表大会)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/meetings/MTG-1927-12-15th-party-congress.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `trotskyist-biographical-deutscher, archival-post-soviet-khlevniuk, economic-foundations-carr-davies`
- **待补齐视角**: `rural-social-history, delegate-social-history`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `rural-social-history, delegate-social-history`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1927年12月2—19日莫斯科举行。大会追认11月对托洛茨基、季诺维也夫的开除党籍处分，并于12月18日另行开除加米涅夫等75名托季联合反对派骨干及萨普罗诺夫派；同时通过编制首个五年计划指示与渐进合作化—集体化决议，开启NEP末期转折前奏。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **会前开除与大会分批组织清洗的严格区分（1927.11.14 vs 1927.12.18）**：托洛茨基与季诺维也夫已于会前 `1927-11-14` 被中央委员会与中央监察委员会联席会议直接开除出党（此前 `1927-10-23` 被逐出中央委员会）。`1927-12-02` 十五大开幕时反对派已无正式表决权代表；`1927-12-03` 斯大林作中央政治报告，加米涅夫、拉柯夫斯基等发言遭全场打断；`1927-12-18` 大会正式追认对托、季二人的开除，并**另行宣布开除包括加米涅夫、皮达可夫、拉狄克、拉柯夫斯基、普列奥布拉任斯基在内的75名联合反对派积极分子**，同时开除萨普罗诺夫“民主集中派”（十月集团）23人名单（**严禁将大会开除的“75人”误计为包含会前已被开除的托、季二人在内的总数**；`CLM-deutscher-1959-united-opposition-defeat`）。
- **反对派阵营分裂与“六个月考察期”悔过处置（1927.12.10–19）**：`1927-12-10` 托派与季派因是否声明放弃宣传反对派观点正式破裂；`1927-12-18—19` 季诺维也夫、加米涅夫等提交放弃派别活动并承认违反党纪的悔过声明，但 `1927-12-19` 闭幕大会拒绝立即集体恢复其党籍，规定须以个人身份单独申请并经至少六个月考察；托洛茨基、拉柯夫斯基等拒绝投降，于1928年1月遭流放（`CLM-deutscher-1959-united-opposition-defeat`）。
- **五年计划编制指示、自愿集体化口径与粮食危机潜流（1927.12）**：大会通过李可夫、克尔日扎诺夫斯基主持的**关于编制国民经济第一个五年计划的指示**（系编制原则而非1929年4月最终批准的最高方案），并通过莫洛托夫农村工作报告，提出逐步扩大集体农庄与国营农场、限制富农剥削，但明文仍保留NEP市场交换与自愿入社原则——**不可目的论地混同于1929年底全盘强制集体化与“消灭富农阶级”**。与此同时，大会开会期间（`1927-12-14` 与 `12-24`）中央已两度向产粮区发出催征粮食紧急指示，预示 `1928-01` 非常措施与斯大林—布哈林决裂迫在眉睫。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-left-and-united-opposition` | `liquidated-at` | 1927-12-18 | 大会开除75名骨干并促发季—托两翼分裂，联合反对派作为党内有组织联盟终结 | `CLM-deutscher-1959-united-opposition-defeat`; `ORG-left-and-united-opposition` |
| `PER-trotsky` | `expulsion-ratified` | 1927-11-14开除；12-18追认 | 会前已被开除党籍，十五大予以追认并拒绝妥协，次年1月流放阿拉木图 | `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-zinoviev` | `expulsion-ratified -> recantation` | 1927-11至12-19 | 会前开除，大会闭幕际与加米涅夫提交悔过书，被勒令经六个月考察再个别审理 | `CLM-deutscher-1959-united-opposition-defeat`; ` Zhukov ch21` |
| `PER-kamenev` | `expelled -> recantation` | 1927-12-18至12-19 | 列入大会开除的75人名单，随即联署悔过声明与托洛茨基派决裂 | `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-stalin` | `leader` | 1927-12 | 主导彻底清除左翼反对派，会后一中全会以口头请辞总书记试探并强化政治局核心顺从 | `CLM-khlevniuk-2015-collective-leadership-erosion` |
| `POL-first-five-year-plan` | `directives-adopted-at` | 1927-12 | 大会通过编制首个五年计划的框架性指示，尚带工农平衡约束而非1929年高指标定稿 | `POL-first-five-year-plan`; `DEB-1928-bukharin-alternative` |
| `POL-nep` | `policy-context` | 1927-12 | 表面重申NEP框内渐进合作化，实则同期秋冬季粮食收购危机已在掏空市场交换基础 | `DEB-1928-bukharin-alternative`; `DEB-1929-collectivization-and-dekulakization-causes` |

### 2.3 史学争鸣光谱
- **经验共识**：大会追认开除托洛茨基与季诺维也夫、另行开除75名托季反对派及萨普罗诺夫集团，通过编制一五计划指示及渐进农业合作化/集体化决议。
- **主要解释分歧**（详参 `DEB-1928-bukharin-alternative`, `DEB-1929-collectivization-and-dekulakization-causes`）：
  - **[传记与社会气氛论 / Isaac Deutscher]**（`CLM-deutscher-1959-united-opposition-defeat`）：指出十五大对反对派的粉碎不仅靠代表遴选机器，更根源于革命疲惫下全国工农的“可怕寂静”与反对派自我束缚于一党纪律之内。
  - **[后苏联政治局制度史 / Oleg Khlevniuk]**（`CLM-khlevniuk-2015-collective-leadership-erosion`）：强调1927年12月清除左翼后，斯大林在 `1927-12-19` 新选中央一中全会上以“列宁遗嘱任务已履行、请求免去总书记”作试探获布哈林、李可夫一致挽留，但政治局寡头共治要到1928—1929年击溃右派后才最终瓦解。
  - **[计划经济与农村史分期论 / Carr & Davies; Cohen]**（`CLM-carr-davies-1969-nemchinov-table-critique`, `CLM-cohen-1973-nep-viability`）：反对苏联教科书将十五大直接等同于“全盘集体化代表大会”，强调十五大文本仍规定农业集体化须建立在自愿与机器物质技术基础之上，与1929年底行政强推存在重大政策断裂。

## 2. 一跳邻域等权重微摘要 (共 12 个关联节点，严防大卡霸占上下文)
### 邻居节点: `CON-thermidor-and-bureaucracy`
- **时效关系边** (`CON-thermidor-and-bureaucracy` → `MTG-1927-12-15th-party-congress` | `expelled-anti-thermidor-opposition-at` | 有效时段: `1927-12-02–12-19`): 十五大正式开除联合反对派，党内公开讨论“苏维埃热月”的空间终结
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 借法国大革命雅各宾衰亡隐喻诊断苏维埃政权变质的核心概念。1921–1923年列宁晚年痛斥国家机关实质承袭沙皇旧机器、仅涂苏维埃油漆；路标转换派乌斯特里亚洛夫从右翼欢呼NEP为民族布尔什维克“热月”；1923–1927年左翼与联合反对派则以“党国官僚中间派与热月危险”批判斯大林—布哈林体制。

### 邻居节点: `EVT-1927-war-scare-and-opposition-expulsion`
- **时效关系边** (`EVT-1927-war-scare-and-opposition-expulsion` → `MTG-1927-12-15th-party-congress` | `culminates_at` | 有效时段: `1927.12.02–19`): 十五大正式完成对联合反对派的组织清洗，并在秋冬购粮危机已发生之际通过首个五年计划编制指示与农业集体化方针。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1927年英苏断交与沃伊科夫遇刺引爆“战争恐慌”，伴随城乡抢购囤粮潮与OGPU“六月行动”（维诺格拉多夫转述仅6月至少9,000人被捕，韦利卡诺娃拼合6—7月下限估至少13,345人）。夏秋间党内多数派强化纪律与治安压制：反对派九月《政纲》遭禁、`11-07` 游行被冲散，托季 `11-14` 被开除党籍；12月十五大在秋冬购粮危机已发生之际完成对联合反对派的组织清除。

### 邻居节点: `ORG-left-and-united-opposition`
- **时效关系边** (`MTG-1927-12-15th-party-congress` → `ORG-left-and-united-opposition` | `liquidated-at` | 有效时段: `1927-12-18`): 大会开除75名骨干并促发季—托两翼分裂，联合反对派作为党内有组织联盟终结
- **时效关系边** (`ORG-left-and-united-opposition` → `MTG-1927-12-15th-party-congress` | `defeated-at` | 有效时段: `1927-12`): 十五大追认开除托、季并另开除75名骨干，终结联合反对派组织存在
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1923年剪刀差危机触发的托洛茨基—普列奥布拉任斯基“左翼反对派”，经1926年春与季诺维也夫—加米涅夫“新反对派”结盟为托季联合反对派；以《四十六人声明》与《1927年政纲》批判官僚体制与“一国社会主义”、主张价格—财政渠道的计划工业化，于1927年12月十五大被组织摧毁。

### 邻居节点: `PER-trotsky`
- **时效关系边** (`MTG-1927-12-15th-party-congress` → `PER-trotsky` | `expulsion-ratified` | 有效时段: `1927-11-14开除；12-18追认`): 会前已被开除党籍，十五大予以追认并拒绝妥协，次年1月流放阿拉木图
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。

### 邻居节点: `PER-zinoviev`
- **时效关系边** (`MTG-1927-12-15th-party-congress` → `PER-zinoviev` | `expulsion-ratified -> recantation` | 有效时段: `1927-11至12-19`): 会前开除，大会闭幕际与加米涅夫提交悔过书，被勒令经六个月考察再个别审理
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 老布尔什维克、共产国际首任主席（1919–1926）。1917年十月公开反对武装起义；1920年哈雷演说力推二十一条与阶级恐怖，1923年豪赌“德国十月”并首倡社民党“法西斯羽翼”论；借“三驾马车”排托后于1925年发起新反对派，1926年7月首因秘密第7条被逐出政治局，1927年底被开除后屈服。

### 邻居节点: `PER-kamenev`
- **时效关系边** (`MTG-1927-12-15th-party-congress` → `PER-kamenev` | `expelled -> recantation` | 有效时段: `1927-12-18至12-19`): 列入大会开除的75人名单，随即联署悔过声明与托洛茨基派决裂
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 老布尔什维克、首任全俄中执委主席。1917年自四月至立宪会议一贯坚守温和宪政社会主义联盟路线并公开反对十月起义；1924年十三大联手季诺维也夫压下《列宁遗嘱》，1925年十四大公开发言反斯大林“领袖”集权后失势；1928年7月密会布哈林并留下外泄笔记，反成右派致命罪证。

### 邻居节点: `PER-stalin`
- **时效关系边** (`MTG-1927-12-15th-party-congress` → `PER-stalin` | `leader` | 有效时段: `1927-12`): 主导彻底清除左翼反对派，会后一中全会以口头请辞总书记试探并强化政治局核心顺从
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。

### 邻居节点: `POL-first-five-year-plan`
- **时效关系边** (`MTG-1927-12-15th-party-congress` → `POL-first-five-year-plan` | `directives-adopted-at` | 有效时段: `1927-12`): 大会通过编制首个五年计划的框架性指示，尚带工农平衡约束而非1929年高指标定稿
- **时效关系边** (`POL-first-five-year-plan` → `MTG-1927-12-15th-party-congress` | `mandated` | 有效时段: `1927.12`): 联共（布）十五大通过关于编制第一个五年计划的指示并宣示扩大农业集体化方向
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1928–1929年定案的苏联首部正式工业化纲领：国家计委“起点方案”与“最高方案”之争，经 `1929-04-16` 至 `23` 中央联席全会、`04-23` 至 `29` 第十六次党代表会议与 `05-20` 至 `28` 第五次全苏苏维埃代表大会批准最高方案；下半年工业投资、钢铁与集体农庄指标连环加码，冲垮布哈林“蜗牛般速度”均衡路线，标志新经济政策体制退场与强制集体化并进。

### 邻居节点: `POL-nep`
- **时效关系边** (`MTG-1927-12-15th-party-congress` → `POL-nep` | `policy-context` | 有效时段: `1927-12`): 表面重申NEP框内渐进合作化，实则同期秋冬季粮食收购危机已在掏空市场交换基础
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。

### 邻居节点: `PER-kalinin`
- **时效关系边** (`PER-kalinin` → `MTG-1927-12-15th-party-congress` | `presided-and-blessed-majority` | 有效时段: `1927-12`): 作为中执委主席在十五大框架内为反托—季多数路线提供宪制外观
- **节点定性微摘要 [T1]** (完备度 `draft`): 特维尔农民出身的布尔什维克“和蔼面孔”：1919年起任全俄及苏联中央执行委员会主席（国家名义元首），1926年1月入政治局。1920年代中期因亲近农民与布哈林富裕农民路线闻名；1928年七月全会关键时刻倒向斯大林，使右派失去政治局多数，1929年仍留多数派未与布哈林集团一同出局。

### 邻居节点: `ORG-democratic-centralists`
- **时效关系边** (`ORG-democratic-centralists` → `MTG-1927-12-15th-party-congress` | `expulsion-context` | 有效时段: `1927-12`): 十五大扩大开除反对派
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 民主集中派是1919年初结成的布尔什维克党内反对派，萨普罗诺夫、奥新斯基、弗·斯米尔诺夫等为重要代表，批评以任命和行政命令取代集体领导与基层参与。成员及立场随时间变化：1923年部分人联署《四十六人声明》；后期“十五人集团”须与早期派别区分。

### 邻居节点: `PER-rakovsky`
- **时效关系边** (`PER-rakovsky` → `MTG-1927-12-15th-party-congress` | `expelled-at` | 有效时段: `1927-12`): 作为联合反对派核心被十五大开除中央与党籍，转入流放抗争与理论著述期
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 巴尔干国际主义者与苏维埃政治家（1873—1941）。1919—1923年任乌克兰人民委员会主席，由反对单定乌语为国语转向力捍共和国自治，1923年十二大推动“本土化”妥协。后任驻英法大使与联合反对派核心，1928年流放撰《论职业危险》剖析执政异化风险，1941年在奥廖尔被处决。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1928-bukharin-alternative`：布哈林替代方案与新经济政策终结之争
## [T1] 核心问题定义
1927至1929年粮食危机与新经济政策的瓦解，是否意味着渐进工业化和工农联盟已无可行出路，还是党内权力与政策选择扼杀了布哈林的替代方案？投资、价格、农民供粮和政治动员之间的约束究竟有多强，必须把经济可行性、政治可行性与实际权力斗争分别检验。

## [T2] 各学派立场对照矩阵
**经验基准**：1928年粮食收购危机后领导层采用非常措施；布哈林同年批评征粮和工业化节奏，1929年四月及十一月中央全会使右派进一步失势，同年清党开除率达 `11%`（约17万人，`DATA-04-party-membership-and-congress-votes-1903-1929`）。各方都面对工业投资、粮食供给与工农社会结构约束。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 新经济政策替代论 | Stephen Cohen, *Bukharin and the Bolshevik Revolution* (1973) | 市场、合作社和渐进工业化提供可争论的替代路径；组织机器与政治斗争使该路线失败。 | `CLM-cohen-1973-nep-viability`；`CLM-cohen-1973-notes-of-an-economist`；`CLM-cohen-1973-bukharin-organizational-defeat` | 可构想的经济路径不自动证明可获得党内多数或满足高投资目标。 |
| 工业化经济思想史 | Alexander Erlich, *The Soviet Industrialization Debate* (1960) | 布哈林平衡增长与普列奥布拉任斯基积累方案共同面对投资约束；强制全盘集体化非各派原有共同结论。 | `CLM-erlich-1960-bukharin-balanced-growth`；`CLM-erlich-1960-preobrazhensky-dilemma`；`CLM-erlich-1960-stalin-overkill-turn` | 模型不能单独解决权力、执行和国际冲击问题。 |
| 经济结构与政策选择 | Alec Nove, *Was Stalin Really Necessary?* (1964) | 提出“条件性必然”与“1927年NEP死胡同（cul-de-sac）”：给定布尔什维克保住一党政权、拒绝斯托雷平式富农资本主义与高速重工业化三大前提，布哈林市场渐进路径存在内在政治经济不一致；但仍须区分发展目标与强制手段。 | `CLM-nove-1964-stalin-necessity-dilemma` | 反事实替代方案的实施条件难以在单线历史中完全检验（详见下栏 KAPROST 交锋）。 |
| 意识形态与政治能动性 | Stephen Kotkin, *Stalin*, Vol. 1 (2014)；Sheila Fitzpatrick, *The Russian Cultural Revolution (1928–1931)* (1978) | 市场发展与党内阶级政治构成张力，斯大林西伯利亚干预使危机转向不能仅由结构推导；“文化革命”动员更将政治局右派、教育人民委员部温和派与沙赫蒂案连成“右倾危险”连续体。 | `CLM-kotkin-2014-bukharin-dilemma`；`CLM-fitzpatrick-1978-anti-bukharin-ideological-offensive` | 科特金第一卷叙事止于1928年底；宣传建构的意识形态连续体亦不能直接等同右派成员一致的文化纲领。 |
| 组织与动员政治 | Oleg Khlevniuk, *Stalin* (2015)；David Priestland, *Stalinism and the Politics of Mobilization* (2007)；Catherine Merridale, *Moscow Politics and the Rise of Stalin* (1990) | 干部控制、反右“复兴主义”动员与乌格拉诺夫莫斯科地方权力瓦解共同决定布哈林集团败局。 | `CLM-khlevniuk-2015-defeat-of-right-opposition`；`CLM-priestland-2007-1928-mobilization-turn-against-bukharin`；`CLM-merridale-1990-uglanov-moscow-collapse` | 组织性胜利并不单独证明任一经济路线的长期优劣。 |
| 反事实计量与改革经济学 | Holland Hunter / R. W. Davies / 谷内融，*戴维斯纪念文集* (1995)；刘伟、平新乔，《平衡与非平衡：布哈林与普列奥布拉仁斯基之争》（1989，B级） | 亨特借 KAPROST 模型论证非集体化 NEP 本可成功，但戴维斯（1994）反驳1928年市场已遭行政扰乱，谷内融1929年1—6月政治局档案证实非常措施演变为全国体制；刘伟、平新乔将布氏重估为“短缺经济学”先驱，指出斯大林采纳了普氏非均衡配额内核。 | `CLM-davies-festschrift-1995-nep-statistics-and-planning-debates`；`CLM-bukharin-preobrazhensky-equilibrium-vs-accumulation-zh`（B级） | KAPROST 假设重工业高积累下农民仍配合市场；刘、平一文沿用中译“81亿金卢布”误植数字，引用须剔除该数。 |
| 后苏联档案重估 | Viktor Zemskov（维克托·泽姆斯科夫），《斯大林时代》（2018，B级）；Valentin Sakharov（瓦连京·萨哈罗夫），《站在十字路口》（2012） | 泽姆斯科夫指出布哈林渐进合作化在内战记忆塑造的党员群体中缺乏政治亲和力；萨哈罗夫从反布哈林修正派立场论证2,400万碎片化小农难以支撑工业国防，MTS 与集体化是避免“斯托雷平第二版”的战略决断。 | `CLM-zemskov-2018-archival-constraints-and-party-radicalism`（B级）；`CLM-sakharov-2012-nep-crossroads-1928` | 泽氏未提供党员心态系统统计且沿用中译稿（B级）；萨哈罗夫的国家理性辩护淡化了强制集体化后的农业灾难与清洗恶果。 |

### `DEB-1929-collectivization-and-dekulakization-causes`：1929年集体化与消灭富农政策的动因之争
## [T1] 核心问题定义
1929年集体化加速与消灭富农政策的出现，究竟源于粮食收购和工业投资的结构约束，还是统计误判、地方竞速、战争恐慌与领导层选择的叠加？农民如何应对，中央内部何时形成强制方案？应把1928年非常征粮、1929年秋冬升级与次年全面执行分开考察。

## [T2] 各学派立场对照矩阵
**经验基准**：1927年冬至1928年春发生粮食收购危机，随后推行非常征粮；全苏农户入庄率在 1929-06-01 为 `3.9%`（约100万户）、1929-10-01 升至 `7.5%`（约190万户），1929年十一月全会后集体化加速，12月11日俄联邦春播集体化目标较10月计划骤增 `60%` 至 2,400 万公顷，“二万五千人”实际选拔 27,519 名工人，同年 OGPU 征粮农村专项逮捕 49,068 人（`DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge`）；12月委员会讨论方案，斯大林12月27日公开宣布转向消灭富农作为阶级。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 农民社会史 | Moshe Lewin, *Russian Peasants and Soviet Power* (1968) | 征粮危机和村庄利益结构不可简化为富农囤粮；乌拉尔—西伯利亚方法使强制扩展到村庄。 | `CLM-lewin-peasants-1968-grain-procurement-crisis`；`CLM-lewin-peasants-1968-kulak-myth-and-serednyak`；`CLM-lewin-peasants-1968-ural-siberian-method` | 农户分化和地区差异须借更细的地方档案检验。 |
| 统计与决策史 | R. W. Davies, *The Socialist Offensive* (1980)；E. H. Carr & R. W. Davies, *Foundations of a Planned Economy*, Vol. 1, Part 1 (1969) | 秋季大转变的事后宣传归纳、十一月决议及涅姆奇诺夫谷物商品率表批判（中贫农占 74% 商品粮、农户裂变至 2,558.6 万户，戳穿“只打富农”神话）与1927年价格剪刀差须分别检验，不能把升级说成早已完整拟定。 | `CLM-davies-1980-autumn-1929-great-turn-fabrication`；`CLM-davies-1980-november-plenum-to-dekulakization`；`CLM-carr-davies-1969-nemchinov-table-critique`；`CLM-carr-davies-1969-grain-price-scissor-1927` | 统计本身的口径和地方上报偏差仍待交叉核验。 |
| 档案与地方升级 | V. P. Danilov, R. Manning, L. Viola & N. A. Ivnitsky (eds.), 《苏联农村的悲剧》第2卷（1929年11月—1930年12月，2000） | 中央委员会内部曾讨论不同速度和处置方案，地方强制及农民逃离、变卖牲畜与政策升级交织。 | `CLM-tragedy-village-1929-november-plenum-escalation`；`CLM-tragedy-village-1929-politburo-dekulakization-commission`；`CLM-tragedy-village-1929-peasant-self-liquidation-and-flight` | 政治警察报告中的阶级归因须与地方材料对勘；译文需回核俄文。 |
| 战争恐慌与地缘政治 | Olga Velikanova, *Popular Perceptions of Soviet Politics in the 1920s* (2013)；Stephen Kotkin, *Stalin*, Vol. 1 (2014)；David R. Shearer, *Stalin and War, 1918–1953* (2024) | 战争恐慌、囤积与西伯利亚征粮选择叠加推进高压路径；希勒进一步论证斯大林对迫近英波战争与军粮储备的判断直接决定了1928—1929年强制征粮与集体化的时间及病理性强度。 | `CLM-velikanova-2013-war-scare-hoarding-and-grain-crisis`；`CLM-kotkin-2014-siberian-grain-turn`；`CLM-stalin-war-1927-1929-threat-and-collectivization` | 外部安全威胁想象不能单独解释各地实施差异或证明强制不可避免。 |
| 工业化结构约束 | Alexander Erlich, *The Soviet Industrialization Debate* (1960)；Alec Nove, *Was Stalin Really Necessary?* (1964) | 工业投资与农业剩余之间确有矛盾，但发展目标不等同暴力全盘集体化的必然性。 | `CLM-erlich-1960-preobrazhensky-dilemma`；`CLM-nove-1964-collectivization-economic-disaster` | 后果评价不能直接充作1929年决策者的动机。 |
| 后苏联贡税论与治安联动 | Viktor Zemskov（维克托·泽姆斯科夫），《斯大林时代》（2018，B级）；Wendy Z. Goldman, *Inventing the Enemy* (2011) | 泽姆斯科夫把20年代低价收购解释为工业化农业“贡税”，并区分1929年底地方跨区驱逐与1930年1月制度化安置；高德曼追踪1929—1930年去富农化治安镇压与一五计划工业短缺、“破坏”话语的联动。 | `CLM-zemskov-2018-agrarian-tribute-and-coercive-turn`（B级）；`CLM-goldman-2011-great-turn-industrialization-and-wrecking` | 泽氏贡税解释缺分年净转移实证且严守1929/1930界线；高德曼核心厂区微观实证延伸至1930年代，不应前移为1929年既定图景。 |

### `DEB-1924-socialism-in-one-country`：一国建成社会主义与不断革命论
## [T1] 核心问题定义
欧洲革命迟滞后，苏联能否凭国内力量建成社会主义，还是生产力与世界市场的联系使最终完成有赖国际革命？争论中的建设、建成和免于复辟并非同一问题；工农联盟、外部安全及党内联盟变化又如何改变这些概念的政治意义？各方均主张建设，分歧在条件、界限与国际前景。

## [T2] 各学派立场对照矩阵
**经验基准**：1924年4月斯大林《论列宁主义基础》初版仍沿用“一国不够组织社会主义生产”旧公式，1924年12月《十月革命和俄国共产党人的策略》正式改口，1925年4月俄共（布）十四次代表会议确认为全党方针；1925年斯大林与布哈林结盟，季诺维也夫转向反对派，十四大批准斯大林中央政治报告路线决议案以 **`559 : 65`** 获胜（反对票主要来自列宁格勒代表团，`DATA-04-party-membership-and-congress-votes-1903-1929`）；1926年联合反对派形成，1927年十五大后遭到组织性排斥。各方都讨论国内建设和国际环境。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 党内多数派 | 斯大林、布哈林，1925年论战（直核布哈林 `1925-04_bukharin-road-to-socialism.md`） | 国内力量可建设社会主义，但免于外部干涉与复辟的最终保障仍有国际条件；布哈林1925年4月原文侧重工农合作渐进增长，须与斯大林表述分别核对。 | `CLM-bukharin-stalin-1925-one-country-internal-forces` | 该卡斯大林引文经2026年汇编转引，不能代替布哈林 S 级原文或十四次代表会议正式通过本。 |
| 联合反对派与不断革命论 | 托洛茨基《1905》（1909/1922）；托洛茨基、季诺维也夫，1925—1927 | 不断革命论原典论证无产阶级夺权后无法止步于民主阶段且依赖西欧联合；1926年季诺维也夫区分建设可能与最终胜利，托洛茨基强调世界生产力、贸易和廉价商品压力。 | `CLM-trotsky-1905-december-uprising-lessons-and-permanent-revolution-defense`（B级）；`CLM-zinoviev-trotsky-1926-world-economy-critique` | 1926年汇编中部分托洛茨基段落未标确切单行本年份；不应把不断革命论简述为反对国内建设。 |
| 反对派政治史与战术/波拿巴反思 | Isaac Deutscher, *The Prophet Unarmed* (1959) & 1952年比较论文（检索ID沿用 `CLM-shlapentokh-*`）；Robert Service, *Trotsky: A Biography* (2009) | 德伊舍尔把理论分歧放回反对派失势轨迹，并指出全党囿于法国“红色拿破仑”迷思围剿托洛茨基，反助斯大林依托书记处文官集权；瑟维斯反驳官僚必然论，归因托洛茨基拒任要职、误判斯大林与战术僵化。 | `CLM-deutscher-1959-disarmed-prophet-paradox`；`CLM-deutscher-1959-united-opposition-defeat`；`CLM-shlapentokh-bonapartism-fear-against-trotsky`；`CLM-service-2009-trotsky-political-tactical-blunders` | 德伊舍尔1959/1952年著述对主人公及工业化“历史进步”带有同情滤镜（库内尚无 Shlapentokh 原著）；瑟维斯则相对低估书记处任命制的结构权重。 |
| 制度与国际史 | E. H. Carr, *The Russian Revolution From Lenin to Stalin, 1917–1929* (1979)；*Foundations of a Planned Economy, 1926–1929*, Vol. 3-II (1976) | 以落后、工业化与国际关系的交织解释政策与理论综合；1927年中国革命失败与战争恐慌加剧共产国际路线及派别争执。 | `CLM-carr-1979-stalin-synthesis-of-russian-backwardness-and-industrialism`；`CLM-carr-1976-china-1927-defeat-and-comintern-factionalism` | 宏观制度综合不能代替逐版文本、会议程序与表决史。 |
| 列宁思想解释 | Valentin Sakharov（瓦连京·萨哈罗夫）, *На распутье... 1921–1929 гг.*（《站在十字路口》，2012） | 论证列宁《论合作社》两份口述稿存在根本理论断裂（放弃初稿“商贩式”流通合作社，第二稿转向国有土地与生产资料上的生产合作社/集体农庄），指斥布哈林偷换概念，并论证斯大林工业化与 MTS 集体农庄路线是第二稿的正统继承人。 | `CLM-sakharov-2012-lenin-cooperative-plan-debates` | 具鲜明后苏联亲斯大林/反布哈林倾向；“列宁晚期生产合作社逻辑”不能直接等同于 1929–1930 年暴力全盘强制集体化，亦非 1925 年党内表决裁决。 |
| 列宁格勒反对派 | Yuri Zhukov（尤里·茹科夫）, 《格里高利·季诺维也夫：被遗忘的世界革命领袖》(2011) | 季诺维也夫1925年发难植根列宁格勒地方权力与共产国际世界革命经验（含1923年德国失败），并非托洛茨基路线的简单副本。 | `CLM-zhukov-zinoviev-1925-leningrad-opposition`；`CLM-zhukov-zinoviev-comintern-and-1923-germany` | 带有后苏联民族国家现实主义倾向（赞斯大林1923年审慎、贬季氏盲动），其叙事仍须与会议速记与文本版本对勘。 |

## 4. 关联时间线锚点 (共 0 条)
