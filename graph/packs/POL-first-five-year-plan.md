# 1-Hop 平衡上下文包：`POL-first-five-year-plan` (第一个五年计划)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/policies/POL-first-five-year-plan.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `quantitative-davies, political-erlich, institutional-carr, shopfloor-filtzer`
- **待补齐视角**: `republican-gosplan-variant-plans, foreign-trade-constraints-narkomvneshtorg`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `republican-gosplan-variant-plans, foreign-trade-constraints-narkomvneshtorg`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1928–1929年定案的苏联首部正式工业化纲领：国家计委“起点方案”与“最高方案”之争，经 `1929-04-16` 至 `23` 中央联席全会、`04-23` 至 `29` 第十六次党代表会议与 `05-20` 至 `28` 第五次全苏苏维埃代表大会批准最高方案；下半年工业投资、钢铁与集体农庄指标连环加码，冲垮布哈林“蜗牛般速度”均衡路线，标志新经济政策体制退场与强制集体化并进。

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

## 2. 一跳邻域等权重微摘要 (共 11 个关联节点，严防大卡霸占上下文)
### 邻居节点: `INS-vsnkh-and-gosplan`
- **时效关系边** (`INS-vsnkh-and-gosplan` → `POL-first-five-year-plan` | `drafted-optimal-variant` | 有效时段: `1927-1929`): 古比雪夫主持的最高国民经济委员会与国家计委目的论派击败发生学派，推动1929年春季通过一五计划最高方案并在下半年失控加码。
- **时效关系边** (`POL-first-five-year-plan` → `INS-vsnkh-and-gosplan` | `drafted-by` | 有效时段: `1928–1929`): Gosplan/VSNKh 竞争性地抬升控制数字，政治局择高方案
- **节点定性微摘要 [T1]** (完备度 `draft`): 苏维埃俄国经济指挥双中枢：1917年12月设立最高国民经济委员会（VSNKh）统辖国有化工业，内战期形成垂直“总局主义”；1921年2月设立国家计划委员会（Gosplan）创制年度“控制数字”，1927–1929年VSNKh（古比雪夫）与Gosplan目的论派（斯特鲁米林）联手以高指标一五计划压倒发生学派。

### 邻居节点: `MTG-1927-12-15th-party-congress`
- **时效关系边** (`MTG-1927-12-15th-party-congress` → `POL-first-five-year-plan` | `directives-adopted-at` | 有效时段: `1927-12`): 大会通过编制首个五年计划的框架性指示，尚带工农平衡约束而非1929年高指标定稿
- **时效关系边** (`POL-first-five-year-plan` → `MTG-1927-12-15th-party-congress` | `mandated` | 有效时段: `1927.12`): 联共（布）十五大通过关于编制第一个五年计划的指示并宣示扩大农业集体化方向
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1927年12月2—19日莫斯科举行。大会追认11月对托洛茨基、季诺维也夫的开除党籍处分，并于12月18日另行开除加米涅夫等75名托季联合反对派骨干及萨普罗诺夫派；同时通过编制首个五年计划指示与渐进合作化—集体化决议，开启NEP末期转折前奏。

### 邻居节点: `PER-strumilin`
- **时效关系边** (`PER-strumilin` → `POL-first-five-year-plan` | `planning-contributor` | 有效时段: `1928–1929`): 参与计划论证，集体起草与政治批准需区分
- **节点定性微摘要 [T1]** (完备度 `draft`): 斯特鲁米林是统计学家和计划经济理论家，早年属孟什维克，1921年起在国家计划委员会任职，1923年加入共产党。1920年代计划方法论争中，他主张计划主动改变既有经济比例，通常被视为目的论取向的主要代表；这一立场与从现存趋势和约束出发的发生论有区别，但不能简化为他否认一切经济规律。

### 邻居节点: `MTG-1929-04-cc-joint-plenum`
- **时效关系边** (`POL-first-five-year-plan` → `MTG-1929-04-cc-joint-plenum` | `ratified-strategy` | 有效时段: `1929.04.16–23`): 四月中央联席全会击败右倾；最高方案由4月23–29日第十六次党代表会议通过，5月第五次全苏苏维埃代表大会批准
- **节点定性微摘要 [T1]** (完备度 `draft`): 1929年4月中央与中监委联席全会谴责布哈林、李可夫和托姆斯基的“右倾”。布哈林作系统抗辩，斯大林作《论联共（布）党内的右倾》报告；处分削弱反对派，相关职务处理延续至同年夏秋。

### 邻居节点: `PER-bukharin`
- **时效关系边** (`POL-first-five-year-plan` → `PER-bukharin` | `defeated-alternative` | 有效时段: `1928–1929`): 主张工农市场结合（смычка）与兼顾消费平衡的渐进工业化方案，被最高方案与非常措施排挤
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。

### 邻居节点: `PER-stalin`
- **时效关系边** (`POL-first-five-year-plan` → `PER-stalin` | `imposed-escalation` | 有效时段: `1928–1929`): 以书记处、社论与电报否决温和草案，推动指标跃升
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。

### 邻居节点: `EVT-1928-grain-procurement-crisis`
- **时效关系边** (`POL-first-five-year-plan` → `EVT-1928-grain-procurement-crisis` | `political-precipitant` | 有效时段: `1928.01–1929`): 征粮危机证明市场协调整合失败论，为超速方案铺路
- **节点定性微摘要 [T1]** (完备度 `draft`): 以 `1927-10-01`（1927/28粮食收购统计年度期界起点，非单日突发事件）至 `1929-12-27`（斯大林宣布“消灭富农阶级”演说日）为期界的引发新经济政策（NEP）终结的体制性危机。工业品荒、农牧收购比价失衡及1927年战争恐慌引发农民惜售，国家收购量在11–12月暴跌；斯大林定性为“富农罢卖”，借刑法第107条与“乌拉尔—西伯利亚方法”推行强制征粮，击败布哈林右派并在1929年底转向全盘集体化。

### 邻居节点: `EVT-1929-great-turn-and-dekulakization-launch`
- **时效关系边** (`POL-first-five-year-plan` → `EVT-1929-great-turn-and-dekulakization-launch` | `accelerated-into` | 有效时段: `1929.07–12`): 已批五年计划在实践中被再次抬高，通向全盘集体化
- **节点定性微摘要 [T1]** (完备度 `draft`): 1929年夏秋，征粮危机、五年计划指标跃升与布哈林集团战败交汇：斯大林11月7日发表《大转变的一年》，11月10–17日中央全会解除布哈林政治局委员职务；12月雅科夫列夫委员会方案遭斯大林否决加码，12月27日正式宣布“把富农作为阶级消灭”，终结新经济政策体制。

### 邻居节点: `POL-nep`
- **时效关系边** (`POL-first-five-year-plan` → `POL-nep` | `superseded` | 有效时段: `1929`): 最高方案批准与政治斗争终结 NEP 再生产逻辑
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。

### 邻居节点: `ORG-right-opposition-1928`
- **时效关系边** (`POL-first-five-year-plan` → `ORG-right-opposition-1928` | `opposed` | 有效时段: `1928–1929.05`): 右派警告剪刀差与强征恶果，组织上败北
- **节点定性微摘要 [T1]** (完备度 `draft`): 1928–1929年以布哈林、李可夫、托姆斯基为首的联共（布）党内右派，在NEP末期反对斯大林非常征粮常态化、“贡赋论”、超工业化冒进及剥夺工会防卫职能；在书记处机器、工会与莫斯科市委遭改组及反分裂党纪自缚下于1929年11月战败，随之开启全盘集体化。

### 邻居节点: `PER-tomsky`
- **时效关系边** (`POL-first-five-year-plan` → `PER-tomsky` | `purged-during` | 有效时段: `1929`): 工会阵地随计划劳动强化遭清洗
- **节点定性微摘要 [T1]** (完备度 `draft`): 工人出身老布尔什维克，1919–1929年执掌全苏工会并任政治局委员。1920–21年工会争论支持列宁抵制托洛茨基“工会国家化”；新经济政策时期捍卫工会集体谈判自主；1928–29年与布哈林、李可夫结成“右翼三巨头”抗斯大林激进路线，后遭清洗自尽。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1928-bukharin-alternative`：“布哈林替代方案”与新经济政策终结之争（1928–1929）
## [T1] 核心问题定义
1927–1929年新经济政策瓦解与斯大林击败布哈林集团，究竟源于小农低商品率与布尔什维克高工业化/价格管制目标之间无法调和的结构性死结，还是源于1926–1928年具体经济政策失误与党内权力机器垄断扼杀了布哈林所主张的市场-合作社均衡工业化替代路径？

## [T2] 各学派立场对照矩阵

| 学派/研究取向 | 代表学者与馆藏著作 | 核心论点摘要 | 已核实馆藏依据 | 主要受批评局限 |
| :--- | :--- | :--- | :--- | :--- |
| **政治传记“替代方案论”** | Stephen F. Cohen (`cohen_1973_bukharin`) | 新经济政策并未枯竭；布哈林基于列宁《论合作社》与《经济学家札记》（1928-09-30）提出了协调工农利益的可行渐进规划；但1928年1月政治局起初一致批准临时非常措施（p. 278），随后斯大林将其升级为常态路线并凭组织机器获胜。 | Cohen pp. 177, 278, `PDF p. 318` | 被批评高估了布哈林方案在重工业资本积累缺口与布尔什维克反市场意识形态下的政治可持续性。 |
| **农村社会史与长短周期分离论** | Moshe Lewin (`lewin_1968_peasants`) | 区分1927–28年粮食危机与1929–30年冬全盘强制集体化：同情渐进合作化，但直言布哈林部分理论“仅在短期有效”，而普列奥布拉任斯基对中长期工业投资瓶颈的诊断更具预见性（Preface `PDF p. 12`）。 | Lewin `PDF pp. 10, 12, 68` | — |
| **发展经济学与计划经济史派** | Alexander Erlich (`erlich_1960_industrialization`)、Carr & Davies (`carr_davies_1969_foundations_v1p1`)、Alec Nove (`nove_1964_was_stalin_necessary`) | Erlich 证明1924–28论战双方（含普列奥布拉任斯基，pp. 44, 177）均未预设暴力全盘集体化；Carr & Davies 与 Nove 揭示国家人为压低谷物收购价（相对于畜牧和经济作物）及工业品饥荒造成1927冬收购锐减。 | Erlich pp. 44, 177; Carr & Davies Vol.1 | 经济上本可通过调价与温和税收缓和，但与党领导层既定超高速军重工业目标直接冲突。 |
| **政治局体制与新经济政策死胡同论** | Oleg Khlevniuk (`khlevniuk_2015_stalin`) | 一方面指出1927年危机表明新经济政策发展模式受多重因素制约已难以为继（Ch. 3）；另一方面从中央书记处干部任命制（Nomenklatura）与政治局纪律剖析布哈林集团为何在组织上迅速瓦解。 | Khlevniuk EPUB Ch. 3 | 偏重高层权力与体制锁死，对非强制替代经济路径的计量效率讨论较少。 |
| **意识形态死结与能动性决断论** | Stephen Kotkin (`kotkin_2014_stalin_v1`, Ch. 13–14 & Coda) | “新经济政策若经济成功便在布尔什维克阶级政治上自我失败”（商品粮依赖大播户即潜伏“富农”）；但同时反对结构宿命论，指出若无斯大林1928年1月西伯利亚督粮的个人铁腕决断，强制全盘集体化概率极低。 | `CLM-kotkin-2014-siberian-grain-turn`, `CLM-kotkin-2014-bukharin-dilemma` | 第1卷叙事止于1928年底，1929年4月与11月全会交锋待补第2卷与全会速记。 |

### `DEB-1929-collectivization-and-dekulakization-causes`：1929年全盘集体化与消灭富农阶级动因总公案
## [T1] 核心问题定义
1929年秋斯大林体制性推进全盘集体化并宣布“消灭富农作为阶级”，究竟是因为新经济政策（NEP）道路在工农价格剪刀差与工业化投资缺口下已结构性破产、布哈林渐进方案被权力机器扼杀（还有何种替代仍可能），还是因为1927–28粮食统计失真、地方征粮竞速与所谓“战争恐慌”触发的螺旋，再叠加领袖对外备战焦虑与反市场意识形态而成为一种可被避免却未被避免的急转弯？

## [T2] 各学派立场对照矩阵

**经验共识**：1927冬—1928春出现严重粮食收购危机；1928年1月西伯利亚“非常措施”与乌拉尔-西伯利亚方法将行政强制包装为村社压力（`POL-ural-siberian-method`）；1929年4月与11月中央全会后集体化指标急剧跃升；1929年12月通过关于富农政策措施，公开的阶级清洗话语制度化。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **布哈林 NEP 可行替代论** | Stephen F. Cohen, *Bukharin and the Bolshevik Revolution* (1973); Moshe Lewin, *Russian Peasants and Soviet Power* (1968) | Cohen：1928年布哈林仍提出可调节市场—合作社渐进工业化；斯大林将临时征粮升级为路线并凭组织拳头获胜。Lewin：区分1927–28危机与1929–30暴力集体化，警告勿将“富农”范畴自然化。 | `CLM-cohen-1973-nep-viability`, `CLM-cohen-1973-bukharin-organizational-defeat`, `CLM-cohen-1973-notes-of-an-economist`, `CLM-lewin-peasants-1968-grain-procurement-crisis`, `CLM-lewin-peasants-1968-kulak-myth-and-serednyak`, `CLM-lewin-peasants-1968-ural-siberian-method` | 替代方案在政治意识形态与国防重工业目标下是否可赢得多数派，争议未终结。 |
| **统计失真与地方竞速螺旋论** | R. W. Davies, *The Socialist Offensive* (1980) 及集体化史系列；Nikolai Ivnitskii（富农消灭过程档案研究） | Davies：批判将1929秋单纯回溯为1928秋“大转变已定局”的史学叙事；地方各级党委在指标竞赛中层层加码。Ivnitskii：实际操作中“富农”划界高度政治化且地区差异巨大。 | `CLM-davies-1980-autumn-1929-great-turn-fabrication`, `CLM-davies-1980-november-plenum-to-dekulakization` | 计量史学与农村社会史接点仍薄；Ivnitskii 著作本库精读未完。 |
| **外部备战焦虑与意识形态死结论** | Stephen Kotkin, *Stalin*, vol. 1 (2014); David R. Shearer（警察国家与工业化）；Lynne Viola 等集体化执行史 | Kotkin：新经济政策在经济成功时亦在布尔什维克阶级政治上自我失败；1928斯大林个人决断打开全盘集体化概率。Shearer/Velikanova 补充高压执行与恐慌政治。 | `CLM-kotkin-2014-siberian-grain-turn`, `CLM-kotkin-2014-bukharin-dilemma`, `CLM-kotkin-2014-geopolitics-and-ideology`, `CLM-velikanova-2013-war-scare-hoarding-and-grain-crisis`, `CLM-velikanova-2013-leadership-manipulation-and-self-deception` | Kotkin 第1卷止1928底；1929全会细节待续卷与速记。 |
| **结构与投资缺口论** | Alexander Erlich (1960); Oleg Khlevniuk (2015) | Erlich：论战各方1924–28均未预设暴力全盘集体化，但工业投资瓶颈真实。Khlevniuk：政治局体制与新经济政策“死胡同”从组织面解释布哈林集团迅速溃败。 | `CLM-erlich-1960-preobrazhensky-dilemma`, `CLM-erlich-1960-stalin-overkill-turn`, `CLM-khlevniuk-2015-secretariat-and-nomenklatura` | 结构制约论易被误读为取消领袖能动性或农民抵抗作用。 |

## 4. 关联时间线锚点 (共 0 条)
