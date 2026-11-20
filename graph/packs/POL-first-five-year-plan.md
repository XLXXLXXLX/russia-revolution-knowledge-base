# 1-Hop 去重平衡上下文包：`POL-first-five-year-plan`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`POL-first-five-year-plan`** (第一个五年计划 | `cards/policies/POL-first-five-year-plan.md` | `multi-perspective`): 已覆盖=`quantitative-davies, political-erlich, institutional-carr, shopfloor-filtzer`；待补=`republican-gosplan-variant-plans, foreign-trade-constraints-narkomvneshtorg`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
苏联首部正式工业化纲领，1928–1929年在起点与最高方案争论中定案。1929-04-16至23日中央联席全会、04-23至29日十六次党代表会议及05-20至28日全苏苏维埃五大批准最高方案；下半年投资、钢铁与集体农庄指标加码，冲垮布哈林均衡路线，与NEP退场、强制集体化并进。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **授权编制与双方案博弈（1927.12–1928）**：`1927-12` 十五大指示编制首个五年计划并主张扩大集体化（`MTG-1927-12-15th-party-congress`）。`1928` 年春 **Gosplan** 内部 **发生学派**（格罗曼、巴扎罗夫）与 **目的论派**（斯特鲁米林）就增长率、粮源与市场约束激烈争辩，同时 **VSNKh**（古比雪夫）提出更激进重工业方案（`INS-vsnkh-and-gosplan`, `CLM-erlich-1960-stalin-overkill-turn`）。`1928` 年冬粮食危机与 **乌拉尔—西伯利亚方法** 突破征粮僵局，政治气氛倒向“超速工业化”。
- **四月联席全会、十六次党代表会议与最高方案批准（1929.04–05）**：`1929-04-16` 至 `23` **联共（布）中央委员会与中央监察委员会四月联席全会** 击败布哈林右派（`MTG-1929-04-cc-joint-plenum`），紧接着 `1929-04-23` 至 `29` **联共（布）第十六次代表会议（XVI конференция ВКП(б)）** 与 `1929-05-20` 至 `28` **苏联第五次全国苏维埃代表大会（全苏苏维埃五大）** 正式批准五年计划 **最高方案（оптимальный вариант）**，投资与产出指标显著高于原“起点方案”（`CLM-erlich-1960-stalin-overkill-turn`、`CLM-davies-1980-autumn-1929-great-turn-fabrication`）。布哈林集团在同会周期内遭组织性致命打击（`CLM-cohen-1973-bukharin-organizational-defeat`）。
- **下半年指标失控与“大转变”合流（1929.06–12）**：批准后 **Gosplan** 与地方竞赛进一步抬高集体化播种面积与钢产量；`1929-08` 集体化控制数字从800万公顷级跳升至1300万公顷级（`CLM-davies-1980-autumn-1929-great-turn-fabrication`）。斯大林11月7日《大转变的一年》社论与11月中央全会解除布哈林政治局职务，将五年计划雄心与消灭富农阶级语言绑定（`EVT-1929-great-turn-and-dekulakization-launch`）。车间层面突击工、竞赛与工会清洗同步强化劳动强度（`CLM-filtzer-1986-1929-tomsky-purge-and-shock-work`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `INS-vsnkh-and-gosplan` | `drafted-by` | 1928–1929 | Gosplan/VSNKh 竞争性地抬升控制数字，政治局择高方案 | `CLM-erlich-1960-stalin-overkill-turn`, `CLM-carr-1952-nep-retreat-and-commanding-heights` |
| `MTG-1927-12-15th-party-congress` | `mandated` | 1927.12 | 联共（布）十五大通过关于编制第一个五年计划的指示并宣示扩大农业集体化方向 | `MTG-1927-12-15th-party-congress` |
| `MTG-1929-04-cc-joint-plenum` | `ratified-strategy` | 1929.04.16–23 | 四月中央联席全会击败右倾；最高方案由4月23–29日第十六次党代表会议通过，5月第五次全苏苏维埃代表大会批准 | `CLM-khlevniuk-2015-defeat-of-right-opposition` |
| `PER-bukharin` | `defeated-alternative` | 1928–1929 | 主张工农市场结合（смычка）与兼顾消费平衡的渐进工业化方案，被最高方案与非常措施排挤 | `CLM-erlich-1960-bukharin-balanced-growth`, `CLM-cohen-1973-bukharin-organizational-defeat` |
| `PER-stalin` | `imposed-escalation` | 1928–1929 | 以书记处、社论与电报否决温和草案，推动指标跃升 | `CLM-stalin-docs-1920s-secretariat-correspondence-and-grain-turn` |
| `EVT-1928-grain-procurement-crisis` | `political-precipitant` | 1928.01–1929 | 征粮危机证明市场协调整合失败论，为超速方案铺路 | `CLM-carr-davies-1969-grain-price-scissor-1927`, `CLM-nove-1964-stalin-necessity-dilemma` |
| `EVT-1929-great-turn-and-dekulakization-launch` | `accelerated-into` | 1929.07–12 | 已批五年计划在实践中被再次抬高，通向全盘集体化 | `CLM-davies-1980-autumn-1929-great-turn-fabrication` |
| `POL-nep` | `superseded` | 1929 | 最高方案批准与政治斗争终结 NEP 再生产逻辑 | `CLM-nove-1964-collectivization-economic-disaster` |
| `ORG-right-opposition-1928` | `opposed` | 1928–1929.05 | 右派警告剪刀差与强征恶果，组织上败北 | `CLM-cohen-1973-bukharin-organizational-defeat` |
| `PER-tomsky` | `purged-during` | 1929 | 工会阵地随计划劳动强化遭清洗 | `CLM-filtzer-1986-1929-tomsky-purge-and-shock-work` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1929年4–5月苏联批准第一个五年计划 **最高方案**；指标显著高于前一年草案；1929年下半年集体化与工业指标再度加码；与布哈林失败及新经济政策终结同年发生。
- **主要解释分歧**（详参 `DEB-1928-bukharin-alternative`, `DEB-1929-collectivization-and-dekulakization-causes`）：
  - **[“过量转弯”与国防恐吓论 / Alexander Erlich]** (`CLM-erlich-1960-stalin-overkill-turn`, `CLM-erlich-1960-bukharin-balanced-growth`)：最高方案投资率远超可行边界；若把斯大林战争恐吓当字面，计划近乎“恐惧死亡引发的自杀”。
  - **[档案计量史学 / R. W. Davies, E. H. Carr]** (`CLM-davies-1980-autumn-1929-great-turn-fabrication`, `CLM-davies-1980-november-plenum-to-dekulakization`, `CLM-carr-davies-1969-grain-price-scissor-1927`)：强调控制数字编制、信贷与价格政策的衔接失灵；1929年秋统计“混乱矛盾”，反映竞赛政治而非纯粹理性计划。
  - **[修正派政治传记 / Stephen Cohen, Moshe Lewin]** (`CLM-cohen-1973-bukharin-organizational-defeat`, `CLM-nove-1964-stalin-necessity-dilemma`)：1929年春布哈林路线仍具经济合理性，失败是书记处权力与非常措施而非技术必然。
  - **[车间社会史 / Donald Filtzer]** (`CLM-filtzer-1986-1929-tomsky-purge-and-shock-work`, `CLM-filtzer-1986-atomized-worker-control-over-labor-process`)：计划批准后即伴随突击工、定额加码与高流动率，工人以离职谈判抵抗——宏观指标有微观妥协成本。

## 2. 一跳邻域全量微摘要目录 (去重后共 15 个节点，0 截断)
- **`CON-smychka`**（工农结合）: 工农结合原指连接或接合，在新经济政策下指国营工业与农民经济通过商品交换、价格和合作社形成的纽带。1923年剪刀差暴露其脆弱性，布哈林与普列奥布拉任斯基提出不同工业化方案；1928至1929年强制征购和集体化使结合逐渐转向行政组织与“生产性结合”。 ‖ `→POL-first-five-year-plan`[制度替代|1928–1929]: 高指标重工业优先战略重塑城乡资源转移与收购体制。
- **`EVT-1928-grain-procurement-crisis`**（1927冬–1929年粮食收购危机）: 1927年秋冬国家收粮锐减，相对价格、工业品荒与战争恐慌共同削弱售粮意愿。1928年非常措施及随后村社摊派把交换危机转为强制征购和党内路线冲突；布哈林等反对者逐步失势，至1929年底转向全盘集体化。粮食总产、商品粮与国家采购须分开衡量。 ‖ `→POL-first-five-year-plan`[industrial_demand_and_policy_acceleration|1928—1929]: 投资及供给约束与农业资源提取相连，不证明特定手段不可替代 ； `←POL-first-five-year-plan`[political-precipitant|1928.01–1929]: 征粮危机证明市场协调整合失败论，为超速方案铺路
- **`EVT-1928-shakhty-affair-show-trial`**（沙赫特事件与技术专家公开审判）: 1928年顿巴斯沙赫特矿区的事故与管理问题被秘密警察定性为经济破坏阴谋。莫斯科公开审判与宣传将旧技术专家的政治可靠性推上全国议程；检方求刑22人死刑，法庭判11人死刑，其中6人获减刑、5人被处决。案件既服务于高层政治动员，也与工人反专家情绪及培养工人出身新专家的政策相互作用。 ‖ `→POL-first-five-year-plan`[precondition_context|1928–1929]: 案件为随后的工业化动员与技术干部政策提供话语背景。
- **`EVT-1929-great-turn-and-dekulakization-launch`**（1929年秋大转变与全盘集体化、消灭富农启动）: 1929年夏秋集体化指标跃升，征粮压力、工业化动员与击败右派相互强化。十一月全会推动工人下乡，十二月委员会草案仍有保留，继被斯大林否决；二十七日公开宣布消灭富农阶级。政治发动、名义入庄与实际生产改组有别，大规模驱逐制度在次年定型。 ‖ `→POL-first-five-year-plan`[accelerated_beyond_spring_baseline|1929年夏冬]: 正式春季计划的有限目标在实践中被不断突破 ； `←POL-first-five-year-plan`[accelerated-into|1929.07–12]: 已批五年计划在实践中被再次抬高，通向全盘集体化
- **`INS-rkka-red-army-and-rvr`**（工农红军与共和国革命军事委员会（РККА 与 РВСР））: 工农红军由1918年初志愿建军转向征兵与集中指挥；共和国革命军事委员会依靠前沙俄军事专家、政治委员及铁路内线组织内战。战后大裁军和伏龙芝改革建立正规军与地方民兵混合体制，1925至1929年伏罗希洛夫主政与干部工农化在政治控制与训练效能间形成持久张力。 ‖ `→POL-first-five-year-plan`[工业化军备重塑|1928–1929]: 重工业五年计划与阶级配额重塑红军后勤现代化与干部构成。
- **`INS-vsnkh-and-gosplan`**（最高国民经济委员会与国家计划委员会（ВСНХ 与 Госплан））: 最高国民经济委员会与国家计划委员会分别承担工业管理与总体计划职能。前者从1917年12月吸纳工人监督演变为内战总局制，新经济政策下改组为经济核算托拉斯；后者自1921年协调预测，二十年代中期后卷入财政纪律、投资速度与第一个五年计划指标的激烈博弈。 ‖ `→POL-first-five-year-plan`[编制与实施主体|1927–1929]: 最高经委与计委反复改写“最优方案”并陷入1929年高指标竞赛。 ； `←POL-first-five-year-plan`[drafted-by|1928–1929]: Gosplan/VSNKh 竞争性地抬升控制数字，政治局择高方案
- **`MTG-1927-12-15th-party-congress`**（联共（布）第十五次代表大会）: 1927年12月2—19日莫斯科举行。大会追认11月对托洛茨基、季诺维也夫的开除党籍处分，并于12月18日另行开除加米涅夫等75名托季联合反对派骨干及萨普罗诺夫派；同时通过编制首个五年计划指示与渐进合作化—集体化决议，开启NEP末期转折前奏。 ‖ `→POL-first-five-year-plan`[directives-adopted-at|1927-12]: 大会通过编制首个五年计划的框架性指示，尚带工农平衡约束而非1929年高指标定稿 ； `←POL-first-five-year-plan`[mandated|1927.12]: 联共（布）十五大通过关于编制第一个五年计划的指示并宣示扩大农业集体化方向
- **`MTG-1929-04-cc-joint-plenum`**（联共（布）中央委员会与中央监察委员会四月联席全会）: 1929年4月16日至23日，联共（布）中央与中监委联席全会围绕征粮危机、工业化与新经济政策展开高层摊牌。布哈林痛斥“贡赋”与强制，斯大林以“右倾”与密谈案反击；全会秘密解除布哈林与托姆斯基关键职务但暂留三人政治局席位，随后十六次代表会议批准的一五计划仍维持有限集体化目标。 ‖ `→POL-first-five-year-plan`[subsequent-approval|1929-04]: 4月15日右派投弃权票，全会闭幕后十六次代表会议（4月23–29日）正式批准最优方案。 ； `←POL-first-five-year-plan`[ratified-strategy|1929.04.16–23]: 四月中央联席全会击败右倾；最高方案由4月23–29日第十六次党代表会议通过，5月第五次全…
- **`MTG-1929-11-cc-plenum`**（联共（布）中央委员会十一月全会（1929））: 1929年11月10日至17日，联共（布）中央全会将布哈林逐出政治局、警告李可夫与托姆斯基等，并宣布宣传右倾与留党不相容。全会动员“二万五千人”下乡并推动集体化加速，但正式决议对富农处置仍留空白；经12月政治局委员会博弈与斯大林否决温和草案，年底演说最终引向消灭富农阶级转向。 ‖ `→POL-first-five-year-plan`[agrarian-radicalization|1929-11起]: 全会控制数字决议与集体化加速彻底突破四月十六次代表会议17.5%的温和指标边界。
- **`PER-strumilin`**（斯坦尼斯拉夫·斯特鲁米林）: 苏联经济统计学家与计划方法论家，1921年起任职国家计委，1923年入俄共；早年属孟什维克之说据俄科学院条目，仍待名册核验。二十年代计划论争中被视为目的论代表，主张计划主动重塑经济比例，有别于从既有约束出发的发生论，不能简化为否认一切规律。 ‖ `→POL-first-five-year-plan`[planning-contributor|1928–1929]: 参与计划论证，集体起草与政治批准需区分
- **`PER-bukharin`**（尼古拉·布哈林）: 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。 ‖ `←POL-first-five-year-plan`[defeated-alternative|1928–1929]: 主张工农市场结合（смычка）与兼顾消费平衡的渐进工业化方案，被最高方案与非常措施排挤
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←POL-first-five-year-plan`[imposed-escalation|1928–1929]: 以书记处、社论与电报否决温和草案，推动指标跃升
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←POL-first-five-year-plan`[superseded|1929]: 最高方案批准与政治斗争终结 NEP 再生产逻辑
- **`ORG-right-opposition-1928`**（1928–1929年右翼反对派（右倾集团））: 1928–1929年以布哈林、李可夫、托姆斯基为核心的联共（布）党内温和派联盟，并非严密地下派系，而是依托政府、工会与莫斯科市委抵制非常征粮常态化、“贡赋论”与超工业化冒进；受制于反派别党纪，各阵地逐一遭书记处拔除，1929年11月战败认错。 ‖ `←POL-first-five-year-plan`[opposed|1928–1929.05]: 右派警告剪刀差与强征恶果，组织上败北
- **`PER-tomsky`**（米哈伊尔·托姆斯基）: 印刷工出身的布尔什维克工会领袖，长期主持全俄及全苏工会中央理事会，1922年进入政治局。工会争论中支持列宁，既限制生产者自治，又在新经济政策下维护集体合同和劳动保护。1928—1929年与布哈林、李可夫抵制激进转轨，遭干部改组夺去工会阵地，1936年自杀。 ‖ `←POL-first-five-year-plan`[purged-during|1929]: 工会阵地随计划劳动强化遭清洗

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 2 项)
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


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/37 条)
- **`CLM-erlich-1960-stalin-overkill-turn`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 161-169, 172-177, 183-184 (PDF pp. 176-184, 187-192, 198-199)]: 
- **`CLM-davies-1980-autumn-1929-great-turn-fabrication`** [`SCH-davies-rw`(R·W·戴维斯) | Vol. 1 printed pp. 121–123, 128, 133, 147, 151–156, 165, 179–182；Vol. 2 本地 PDF pp. 34, 45, 60–61]: 
- **`CLM-cohen-1973-bukharin-organizational-defeat`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 287-289, 297-301, 322-329]: 
- **`CLM-filtzer-1986-1929-tomsky-purge-and-shock-work`** [`SCH-filtzer-donald`(唐纳德·费尔泽) | pp. 22–24, 68–72, 76–82, 96–108, 274, 280–282, 287]: 
- **`CLM-carr-1952-nep-retreat-and-commanding-heights`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 118-166 (Chs. 18–20)]: 
- **`CLM-khlevniuk-2015-defeat-of-right-opposition`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch03.html（His Revolution 开篇至全盘集体化的 1929 年 11 月宣布）。工作区文本无纸质页码。]: 
- **`CLM-erlich-1960-bukharin-balanced-growth`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 21-23 (PDF pp. 38-40)]: 
- **`CLM-stalin-docs-1920s-secretariat-correspondence-and-grain-turn`** [`SCH-dolmatov-vladimir`(弗拉基米尔·多尔马托夫（编） · archival-documentary-edition)]: 
- **`CLM-carr-davies-1969-grain-price-scissor-1927`** [`SCH-davies-rw`(R·W·戴维斯) | pp. 44-47 (esp. p. 46)]: 
- **`CLM-nove-1964-stalin-necessity-dilemma`** [`SCH-nove-alec`(亚历克·诺夫) | pp. 20-26, 32]: 
- **`CLM-nove-1964-collectivization-economic-disaster`** [`SCH-nove-alec`(亚历克·诺夫) | pp. 27-29, 53-55, 139]: 
- **`CLM-davies-1980-november-plenum-to-dekulakization`** [`SCH-davies-rw`(R·W·戴维斯) | Vol. 1 printed pp. 159–167, 182–202；Vol. 2 本地 PDF pp. 50–55, 101–102]: 
- **`CLM-filtzer-1986-atomized-worker-control-over-labor-process`** [`SCH-filtzer-donald`(唐纳德·费尔泽) | pp. 1–2, 8–9, 27–29, 44–63, 80–89, 92–93, 107–115]: 
- **`CLM-zemskov-2018-agrarian-tribute-and-coercive-turn`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | 馆藏中文PDF pp. 7–8, 10–12；后续比较仅pp. 5–6]: 
- **`CLM-smirnov-red-army-commanders-vs-voenspetsy-1920s`** [`SCH-smirnov-andrei`(安德烈·阿纳托利耶维奇·斯米尔诺夫) | pp. 628-634, 670-672, 680-694]: 
- **`CLM-davies-festschrift-1995-nep-statistics-and-planning-debates`** [`SCH-hunter-holland`(霍兰·亨特 · cliometrics) | pp. 18-21, 82-94, 218-226]: 
- **`CLM-cohen-1973-nep-viability`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 270-276, 316-320]: 
- **`CLM-cohen-1973-notes-of-an-economist`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 295-296, 318-320]: 
- **`CLM-erlich-1960-preobrazhensky-dilemma`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 34-36, 40-41, 49-51, 170-171 (PDF pp. 51-53, 57-58, 66-68, 185-186)]: 
- **`CLM-kotkin-2014-bukharin-dilemma`** [`SCH-kotkin-stephen`(斯蒂芬·科特金) | EPUB Coda (OEBPS/9780698170100_EPUB_1-25.xhtml) & Ch. 14 (OEBPS/9780698170100_EPUB_1-24.xhtml)]: 
- **`CLM-fitzpatrick-1978-anti-bukharin-ideological-offensive`** [`SCH-fitzpatrick-sheila`(希拉·菲茨帕特里克) | pp. 11–14, 20–21]: 
- **`CLM-priestland-2007-1928-mobilization-turn-against-bukharin`** [`SCH-priestland-david`(大卫·普里斯特兰) | pp. 234–237; 291–296]: 
- **`CLM-merridale-1990-uglanov-moscow-collapse`** [`SCH-merridale-catherine`(凯瑟琳·梅里代尔) | pp. 53-64]: 
- **`CLM-bukharin-preobrazhensky-equilibrium-vs-accumulation-zh`** [`SCH-liu-wei-ping-xinqiao`(刘伟与平新乔 · chinese-political-economy) | 原刊 pp. 92–99 (PDF pp. 1–8；英文提要 pp. 127–128 / PDF pp. 9–10)]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
