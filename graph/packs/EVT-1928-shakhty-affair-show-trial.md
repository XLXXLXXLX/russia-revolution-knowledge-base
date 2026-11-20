# 1-Hop 去重平衡上下文包：`EVT-1928-shakhty-affair-show-trial`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`EVT-1928-shakhty-affair-show-trial`** (沙赫特事件与技术专家公开审判 | `cards/events/EVT-1928-shakhty-affair-show-trial.md` | `multi-perspective`): 已覆盖=`political-institutional, social-history, education-cultural-revolution, industrial-site-and-enemy-construction`；待补=`complete-trial-transcript, independent-investigation-case-files`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1928年顿巴斯沙赫特矿区的事故与管理问题被秘密警察定性为经济破坏阴谋。莫斯科公开审判与宣传将旧技术专家的政治可靠性推上全国议程；检方求刑22人死刑，法庭判11人死刑，其中6人获减刑、5人被处决。案件既服务于高层政治动员，也与工人反专家情绪及培养工人出身新专家的政策相互作用。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **侦查与政治升级**：北高加索国家政治保卫总局（OGPU）负责人叶夫多基莫夫向斯大林报告矿区案件，绕过通常的工业管理渠道。`1928-03-10` 《真理报》公开案件；指控把工程事故、管理矛盾与矿主流亡者和外国势力的阴谋联系起来。**被告人数三口径并存**：科特金札记记53名工程师、其中5名德国专家（引发德国 `03-15` 暂停信贷谈判）；L3 记53名本国及3名德国技术专家受审；科恩（p. 281）记公布时为55人。差异可能源自“被捕/起诉/出庭”阶段与德国籍人数口径，原始起诉书站内未入库，三者不能自行合并。指控不是已经证实的集体阴谋。
- **全会与反专家运动**：`1928-04-06` 至 `04-11` 联共（布）中央与中监委联席全会上，米高扬作粮食报告、李可夫作沙赫特案报告；`04-10` 斯大林将案件直接挂钩白俄流亡与外国干涉，全会逐字采纳其阴谋定性。但斯大林同时提议将高等技术院校（VTUZ）自教育人民委员部划归 VSNKh，**遭全会近 2:1 多数否决**（直至夏季全会才部分实现）（L3 `1928-01…` L95，据 Cohen ch12、Kotkin ch21）。公开舆论激化了对旧专家的怀疑与迫害（спецеедство）；7月（`07-04~12`）全会进一步细化工科教育与工人提拔。新经济政策下对旧专家的依赖受到冲击，但国家并未立即停止使用旧专家。
- **公开审判与宣判链条**：`1928-05-18` 审判在莫斯科工会大厦圆柱大厅开始，维辛斯基主持，克雷连科担任公诉人。克雷连科要求判处 **22人**死刑；审理49天后，`1928-07-06` 深夜延续至 `1928-07-07` 凌晨 **1:30** 宣读判决（Carr–Davies/Lewin 记审期为 `05-18–07-05`）：4人无罪（含两名德国技师）、4人缓刑、余者1至10年监禁，**11人**判处死刑，随后 **6人**获减刑，**5人**于 `1928-07-09`（七月全会斯大林发表关键讲话同日）被执行枪决（L3 `1928-01…` L98）。分母链：22 → 11 → 6 → 5。原始判决书与庭审记录站内未入库。
- **后果**：案件为阶级警惕与文化革命提供强大宣传资源，也强化对技术管理部门的政治监督；它是1928—1929年转向的重要组成部分，而非某一天就单独终结新经济政策。

### 2.2 时效关系摘要边表
| 关联节点 | 关系类型 | 有效时段 | 关系实质与依据 |
| :--- | :--- | :--- | :--- |
| `ORG-cheka-ogpu` | `escalates_case` | 1928年春 | 地方 OGPU（叶夫多基莫夫）向最高层推动案件；见科特金札记。（注：库中另有 `INS-cheka-gpu-ogpu` 作机构档案，本卡统一取 ORG 节点。） |
| `PER-stalin` | `politicizes_case` | `1928-04-10` 前后 | 将案件挂钩白俄流亡与外国干涉，并提议VTUZ划转（遭否决）；见 L3 L95。 |
| `PER-rykov` ↔ `PER-kuibyshev` ↔ `INS-vsnkh-and-gosplan` | `challenges_management` | 1928年春夏 | 李可夫在四月全会作沙赫特案报告；侦查绕开管理体系，案件也冲击技术治理；不同领导人态度并不按党派简单排列。 |
| `PER-bukharin` ↔ `PER-tomsky` ↔ `ORG-right-opposition-1928` | `reconfigures_political_conflict` | 1928–1929 | 案件扩大敌情与右倾危险话语；科特金同时记布、托公开支持抓捕，不能写成一致反对。 |
| `EVT-1928-grain-procurement-crisis` | `parallel_political_track` | 1928年春 | 粮食危机与沙赫特案在四月全会并行处理，斯大林在两线上的得失不同（L3 L95）。 |
| `POL-first-five-year-plan` | `precondition_context` | 1928–1929 | 案件为随后的工业化动员与技术干部政策提供话语背景。 |

> 节点缺口：叶夫多基莫夫、维辛斯基、克雷连科以及“工人与新技术干部（vydvizhentsy）”站内暂无人物/群体卡片，已不以悬空 ID 代替。

### 2.3 史学争鸣光谱
- **政治与制度解释**：赫列夫纽克将捏造的破坏罪名及宣传置于斯大林孤立温和派、扩大阶级斗争话语的过程；科特金强调斯大林借秘密警察和组织工具推进，但也记录支持强硬粮政的古比雪夫等人反对迫害专家，而布哈林、托姆斯基曾公开支持抓捕。把案件说成一开始双方整齐对垒会抹平这一错位。
- **社会与教育解释**：菲茨帕特里克强调宣传如何放大既存反专家情绪，并将工人出身干部的教育与提拔制度化；这并不证明所有工人均支持审判。
- **工业现场与敌人建构**：[`SCH-kuromiya-hiroaki`](../../historiography/scholars/SCH-kuromiya-hiroaki.md)（站内 `grounded`）记黑宫1988年《斯大林的工业革命》的“spets-baiting”论与顿巴斯研究；站内另有其顿巴斯章节的 Siegelbaum–Suny 相关章（[ch10_5](../../sources/monographs/siegelbaum_suny_1994_making_workers_soviet_zh/ch10_5_donbas_miners_in_war_revolution_and_ci.md)）。本卡已读上述 SCH 卡与该章，但其沙赫特案具体文本未读，不为其指定超出此范围的细节。三种取向的矩阵见 [`DEB-1928-shakhty-specialist-baiting-and-cultural-revolution`](../../historiography/debates/DEB-1928-shakhty-specialist-baiting-and-cultural-revolution.md)。
- **共同边界**：矿业事故与管理困难的存在，不能证明公诉方所称跨国统一阴谋；审讯证言与公开庭审均须结合调查档案、取证条件及其他独立证据检验。Goldman 仅在其著作 p. 44 n.33 脚注提及沙赫特案，后来“破坏”话语日常化与1936年再处决等晚期证据不得投射回1928年，故本卡不引其作沙赫特案证据。

## 2. 一跳邻域全量微摘要目录 (去重后共 8 个节点，0 截断)
- **`CON-intelligentsia-and-vekhi`**（俄国知识分子阶层、《路标》论战与“资产阶级专家”）: 俄国知识分子从伦理异议共同体向苏维埃体制群体重构。1860年代平民知识分子与拉夫罗夫奠定反专制献身传统；1909年《路标》批判激进派反法制与政治狂热，遭列宁谴责。十月后“资产阶级专家”受监控，经历1922年“哲学船”驱逐、1928年沙赫特案整肃及工农干部提拔。 ‖ `→EVT-1928-shakhty-affair-show-trial`[rupture-of-nep-specialist-compromise|1928.03–07]: 将顿巴斯矿难政治化为旧技术专家勾结外国的阶级破坏阴谋，终结NEP专家妥协并直接触发工农干部“大提拔”
- **`EVT-1928-grain-procurement-crisis`**（1927冬–1929年粮食收购危机）: 1927年秋冬国家收粮锐减，相对价格、工业品荒与战争恐慌共同削弱售粮意愿。1928年非常措施及随后村社摊派把交换危机转为强制征购和党内路线冲突；布哈林等反对者逐步失势，至1929年底转向全盘集体化。粮食总产、商品粮与国家采购须分开衡量。 ‖ `→EVT-1928-shakhty-affair-show-trial`[parallel_political_track|1928.03—07]: 沙赫特案与粮食危机在四月、七月全会并行升级，重塑反右阵线 ； `←EVT-1928-shakhty-affair-show-trial`[parallel_political_track|1928年春]: 粮食危机与沙赫特案在四月全会并行处理，斯大林在两线上的得失不同（L3 L95）。
- **`ORG-cheka-ogpu`**（全俄肃反委员会—国家政治保卫局）: 苏俄与苏联早期政治警察机关（1917–1934），由捷尔任斯基创立。历经全俄肃反委员会（ВЧК，1917–1922）、国家政治保卫局（ГПУ，1922–1923）与国家政治保卫总局（ОГПУ，1923–1934）三阶段，从法外非常机构演变为直属政治局的常设宪制部门，执行红色恐怖与强制集体化。 ‖ `←EVT-1928-shakhty-affair-show-trial`[escalates_case|1928年春]: 地方 OGPU（叶夫多基莫夫）向最高层推动案件；见科特金札记。（注：库中另有 INS-c…
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←EVT-1928-shakhty-affair-show-trial`[politicizes_case|1928-04-10 前后]: 将案件挂钩白俄流亡与外国干涉，并提议VTUZ划转（遭否决）；见 L3 L95。
- **`PER-rykov`**（阿列克谢·李可夫）: 老布尔什维克与苏维埃经济组织家。1917年四月会议曾质疑《四月提纲》，十月后因维克热尔联合政府诉求辞职；两掌最高国民经济委员会，1924年继列宁任苏联人民委员会主席；1928–1929年协同布哈林抵制非常征粮并提“两年农业计划”遭撤职清洗，其名却在库班农民口号中回响。 ‖ `←EVT-1928-shakhty-affair-show-trial`[challenges_management|1928年春夏]: 李可夫在四月全会作沙赫特案报告；侦查绕开管理体系，案件也冲击技术治理；不同领导人态度并不…
- **`PER-bukharin`**（尼古拉·布哈林）: 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。 ‖ `←EVT-1928-shakhty-affair-show-trial`[reconfigures_political_conflict|1928–1929]: 案件扩大敌情与右倾危险话语；科特金同时记布、托公开支持抓捕，不能写成一致反对。
- **`POL-first-five-year-plan`**（第一个五年计划）: 苏联首部正式工业化纲领，1928–1929年在起点与最高方案争论中定案。1929-04-16至23日中央联席全会、04-23至29日十六次党代表会议及05-20至28日全苏苏维埃五大批准最高方案；下半年投资、钢铁与集体农庄指标加码，冲垮布哈林均衡路线，与NEP退场、强制集体化并进。 ‖ `←EVT-1928-shakhty-affair-show-trial`[precondition_context|1928–1929]: 案件为随后的工业化动员与技术干部政策提供话语背景。
- **`PER-yagoda`**（亨里希·雅戈达）: 苏联秘密警察组织者，1923年起任OGPU第二副主席；缅任斯基1926年任主席后因病少理日常事务，雅戈达影响渐增，职衔与实际权力须区分。其机关在战争恐慌、镇压反对派及1928–1929年控制社会中服务大转变；1934–1936年任内务人民委员，1938年公审后被处决。 ‖ `→EVT-1928-shakhty-affair-show-trial`[security-investigation|1928]: 1928-03-02 呈送报告并陪同面见斯大林；机关调查与打击专家的政治运动相连

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

### `DEB-1928-shakhty-specialist-baiting-and-cultural-revolution`：沙赫特事件、反专家运动与文化革命动力之争
## [T1] 核心问题定义
1928年沙赫特案件及其后围绕旧技术专家的政治攻势，是高层为改变新经济政策方向和打击党内对手而操纵的结果，还是青年、工人和新干部向上流动诉求与阶级动员的共振？工业失调、责任归咎和国家镇压如何连接二者？运动的动员效果并不能证明案件指控属实。

## [T2] 经验共识 + 各学派立场对照矩阵

**经验共识**：沙赫特审判发生于1928年，旧技术人员遭到破坏指控；专家问题与阶级警惕、干部提拔及工业化转向紧密相连。党和国家并未简单地抛弃一切专家：对旧专家的依赖、监督、攻击与培养新干部并存。

| 取向 | 代表与核心解释 | 盲点与待核问题 | 本地论断锚点 |
| :--- | :--- | :--- | :--- |
| 高层政治与路线斗争 | Khlevniuk、Kotkin、Cohen 的相关政治史提醒关注领导人、政治警察和右派之间的权力关系，以及案件对专家政策争论的用途。 | 政治利用不自动证明斯大林从侦查之初指挥制造全部证据；“联手绕过李可夫与布哈林设局”的具体机制须用侦查档案和各作者原文核实。 | `CLM-cohen-1973-july-1928-plenum-and-kamenev`; `CLM-priestland-2007-1928-mobilization-turn-against-bukharin` |
| 社会流动与上下互动 | Fitzpatrick 强调文化革命中的青年、工农出身干部和提拔者对旧等级与专家地位的挑战；上层号召与基层诉求相互作用。 | 不应把基层积极分子等同整个工人阶级，也不能忽视组织资源和强制权掌握在上层手中。红色教授学院与青年团在本案的具体作用需分开核查。 | `CLM-fitzpatrick-1979-1928-shakhty-and-vydvizhentsy`; `CLM-fitzpatrick-1978-cultural-revolution-from-below-and-above` |
| 工业现场与敌人建构 | Kuromiya、Goldman、Bailes 的相关研究提示，将生产压力、事故、管理矛盾和针对破坏者的动员放在同一过程考察。 | 不能将每一次事故、短缺或控告都还原成中央有意制造的替罪羊；Goldman 后续大恐怖研究的证据年代不能不加区分地投射至1928年。 | `CLM-goldman-2011-great-turn-industrialization-and-wrecking`; `CLM-goldman-2011-social-dynamics-of-vigilance-vs-totalitarian-model` |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 21/21 条)
- **`CLM-fitzpatrick-1979-1928-shakhty-and-vydvizhentsy`** [`SCH-fitzpatrick-sheila`(希拉·菲茨帕特里克) | pp. 113–119, 139]: 
- **`CLM-cohen-1973-nep-viability`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 270-276, 316-320]: 
- **`CLM-cohen-1973-notes-of-an-economist`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 295-296, 318-320]: 
- **`CLM-cohen-1973-bukharin-organizational-defeat`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 287-289, 297-301, 322-329]: 
- **`CLM-erlich-1960-bukharin-balanced-growth`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 21-23 (PDF pp. 38-40)]: 
- **`CLM-erlich-1960-preobrazhensky-dilemma`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 34-36, 40-41, 49-51, 170-171 (PDF pp. 51-53, 57-58, 66-68, 185-186)]: 
- **`CLM-erlich-1960-stalin-overkill-turn`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 161-169, 172-177, 183-184 (PDF pp. 176-184, 187-192, 198-199)]: 
- **`CLM-nove-1964-stalin-necessity-dilemma`** [`SCH-nove-alec`(亚历克·诺夫) | pp. 20-26, 32]: 
- **`CLM-kotkin-2014-bukharin-dilemma`** [`SCH-kotkin-stephen`(斯蒂芬·科特金) | EPUB Coda (OEBPS/9780698170100_EPUB_1-25.xhtml) & Ch. 14 (OEBPS/9780698170100_EPUB_1-24.xhtml)]: 
- **`CLM-fitzpatrick-1978-anti-bukharin-ideological-offensive`** [`SCH-fitzpatrick-sheila`(希拉·菲茨帕特里克) | pp. 11–14, 20–21]: 
- **`CLM-khlevniuk-2015-defeat-of-right-opposition`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch03.html（His Revolution 开篇至全盘集体化的 1929 年 11 月宣布）。工作区文本无纸质页码。]: 
- **`CLM-priestland-2007-1928-mobilization-turn-against-bukharin`** [`SCH-priestland-david`(大卫·普里斯特兰) | pp. 234–237; 291–296]: 
- **`CLM-merridale-1990-uglanov-moscow-collapse`** [`SCH-merridale-catherine`(凯瑟琳·梅里代尔) | pp. 53-64]: 
- **`CLM-davies-festschrift-1995-nep-statistics-and-planning-debates`** [`SCH-hunter-holland`(霍兰·亨特 · cliometrics) | pp. 18-21, 82-94, 218-226]: 
- **`CLM-bukharin-preobrazhensky-equilibrium-vs-accumulation-zh`** [`SCH-liu-wei-ping-xinqiao`(刘伟与平新乔 · chinese-political-economy) | 原刊 pp. 92–99 (PDF pp. 1–8；英文提要 pp. 127–128 / PDF pp. 9–10)]: 
- **`CLM-zemskov-2018-archival-constraints-and-party-radicalism`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | 馆藏中文PDF pp. 2–4, 7–10；非俄文原版纸页]: 
- **`CLM-sakharov-2012-nep-crossroads-1928`** [`SCH-sakharov-valentin`(瓦连京·萨哈罗夫) | EPUB Ch. 4.2 & Ch. 4.3]: 
- **`CLM-cohen-1973-july-1928-plenum-and-kamenev`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 289-291]: 
- **`CLM-fitzpatrick-1978-cultural-revolution-from-below-and-above`** [`SCH-fitzpatrick-sheila`(希拉·菲茨帕特里克) | pp. 11–15, 17–19]: 
- **`CLM-goldman-2011-great-turn-industrialization-and-wrecking`** [`SCH-goldman-wendy`(温迪·Z·戈德曼) | pp. 7, 11, 14, 43–47, 56, 87–90, 306–310]: 
- **`CLM-goldman-2011-social-dynamics-of-vigilance-vs-totalitarian-model`** [`SCH-goldman-wendy`(温迪·Z·戈德曼) | pp. 4–8, 20–22, 25–31, 60–66, 300–305, 312–314]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
