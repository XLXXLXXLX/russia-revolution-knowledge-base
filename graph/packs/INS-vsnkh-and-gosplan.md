# 1-Hop 去重平衡上下文包：`INS-vsnkh-and-gosplan`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`INS-vsnkh-and-gosplan`** (最高国民经济委员会与国家计划委员会（ВСНХ 与 Госплан） | `cards/institutions/INS-vsnkh-and-gosplan.md` | `multi-perspective`): 已覆盖=`institutional-economic, smith-workers-control, carr-davies-quantitative, erlich-industrialization, zhukov-archival, ratkovsky-archival-biography, katasonov-monetary-b-tier`；待补=`regional-implementation, founding-decree-russian-fulltext-clauses`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 150字定性微摘要
最高国民经济委员会与国家计划委员会分别承担工业管理与总体计划职能。前者从1917年12月吸纳工人监督演变为内战总局制，新经济政策下改组为经济核算托拉斯；后者自1921年协调预测，二十年代中期后卷入财政纪律、投资速度与第一个五年计划指标的激烈博弈。

## [T2] 核心脉络与史学争鸣
### 2.1 制度分期
- **创立、工人监督吸收与战时总局制（1917—1920）**：最高国民经济委员会（ВСНХ）建制经历明确的三重俄历法律程序（Carr 第二卷详析）：`1917-12-01 [O.S.] / 1917-12-14 [N.S.]` 列宁在全俄中执委力挺布哈林所拟法令草案获原则通过（Smith 第11章所记12月1日即此俄历节点）；`1917-12-02 [O.S.] / 1917-12-15 [N.S.]` 全俄中执委与人民委员会正式签署生效；`1917-12-05 [O.S.] / 1917-12-18 [N.S.]` 公开发表。该机构初设即统合并逐步取代分散的工厂委员会，1918年6月全面国有化后在“制高点”工业形成逾 42 个行业总局垂直支配的体制（главкизм），引致实物清算紊乱与部门割据（`CLM-smith-sa-1983-from-workers-control-to-nationalization`、`CLM-carr-1952-war-communism-internal-contradictions`）。
- **计委设立、权限之争与财政制衡（1921—1926）**：1921-02-22 国家计划委员会（Госплан）在劳动国防委员会下设立，由克尔日扎诺夫斯基主持。新经济政策下，最高经委将大企业编组为按经济核算制（хозрасчёт）运作的托拉斯；计委所编“控制数字”起初偏预测协调，列宁在 1922-12-27 建议赋予计委某种“立法职能”（见 `1922-12_letter-to-the-congress`），但十二大遭多数压制。1923年最高经委副主席 **`PER-pyatakov`** 主导盈利原则命令并要求宽松信贷，与财政人民委员 **`PER-sokolnikov`** 捍卫切尔文金本位、削减预算（一度在劳动国防委员会砍掉重工业申请预算12%）爆发激烈交锋，构成1923年剪刀差与信贷紧缩危机的制度背景（`DATA-02-1922-1924-scissors-crisis-and-chervonets`、`CLM-other-nep-1923-sokolnikov-monetary-discipline`）。1924—1926年 **`PER-dzerzhinsky`** 兼任最高经委主席，据拉特科夫斯基所编档案，其着力成本集约与新经济政策平衡。
- **高速度转向与五年计划升级（1926—1929）**：1926年古比雪夫接任最高经委主席后，工业扩张冲动加剧。计委内部以 **`PER-kondratiev`**、格罗曼、巴扎罗夫为代表的“发生学派”强调经济均衡推演，以 **`PER-strumilin`** 为代表的“目的论派”突出计划目标与主动改造，但两派分类是分析标签而非铁板一块。1928—1929年第一个五年计划初始方案、最优方案及 1929 年 8 月计委控制数字突增至 1300 万公顷等层层加码过程（`CLM-davies-1980-autumn-1929-great-turn-fabrication`），显示指标是在政治压力下连续改写而非一次定型。

### 2.2 核心关系网络（结构化边表）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | 创立与拟权 | 1917.12–1923 | 力挺成立最高经委，1922年12月又倡议赋予计委立法职能。 | `CLM-smith-sa-1983-from-workers-control-to-nationalization` |
| `ORG-factory-committees-1917` | 吸收与集中化 | 1917.11–1918.06 | 将分散工人监督纳入“企业—区—市—国”垂直国有化体系。 | `CLM-smith-sa-1983-from-workers-control-to-nationalization` |
| `POL-nep` | 制度共存与退却 | 1921–1929 | 托拉斯核算、控制数字与市场货币体制在“制高点”内并存。 | `CLM-carr-1952-nep-retreat-and-commanding-heights` |
| `EVT-1923-scissors-crisis` | 政策诱因 | 1923 | 最高经委盈利原则与商业托拉斯提价促发工农业比价危机。 | `CLM-carr-1954-scissors-crisis-mechanics` |
| `CON-smychka` | 价格中介 | 1923–1927 | 工业定价、投资配比与农产比价直接牵动城乡结合稳定性。 | `CLM-carr-davies-1969-grain-price-scissor-1927` |
| `INS-gosbank-and-narkomfin` | 信贷与预算博弈 | 1923–1929 | 围绕切尔文稳定、预算削减与重工业放贷持续发生部门冲突。 | `CLM-other-nep-1923-sokolnikov-monetary-discipline` |
| `PER-sokolnikov` | 财政制衡 | 1922–1926 | 以紧缩预算和币值稳定制约最高经委与计委投资冲动。 | `CLM-other-nep-1923-sokolnikov-monetary-discipline` |
| `PER-pyatakov` | 工业集权推手 | 1923–1929 | 最高经委副主席，推动1923年盈利命令与重工业信贷扩张。 | `CLM-carr-1954-scissors-crisis-mechanics` |
| `PER-dzerzhinsky` | 经委主席 | 1924.02–1926.07 | 兼掌最高经委，主张降低工业成本与保持市场货币平衡。 | `CLM-plekhanov-am-dzerzhinsky-vsnkh-nep-industrialism-1924-1926` |
| `PER-kuibyshev` | 经委主席 | 1926.08–1930 | 推动工业加速扩张并压低计委保守派的平衡限制。 | `CLM-erlich-1960-stalin-overkill-turn` |
| `PER-kondratiev` | 方法论对手 | 1924–1928 | 主张农业均衡与发生学规律，反对脱离市场条件的强行计划。 | `CLM-davies-festschrift-1995-nep-statistics-and-planning-debates` |
| `PER-strumilin` | 计划理论家 | 1921–1929 | 主张目的论计划改造并编制早期剪刀差指数与工业指标。 | `CLM-carr-1954-scissors-crisis-mechanics` |
| `PER-stalin` | 政治驯化与加码 | 1928–1929 | 依托机关改组和反右倾动员强行拉升五年计划与控制数字。 | `CLM-davies-1980-autumn-1929-great-turn-fabrication` |
| `POL-first-five-year-plan` | 编制与实施主体 | 1927–1929 | 最高经委与计委反复改写“最优方案”并陷入1929年高指标竞赛。 | `CLM-erlich-1960-stalin-overkill-turn` |
| `EVT-1929-great-turn-and-dekulakization-launch` | 指标引爆 | 1929.08–12 | 1929年8月计委控制数字跃升直接衔接秋季全面加速转折。 | `CLM-davies-1980-autumn-1929-great-turn-fabrication` |
| `DEB-1928-bukharin-alternative` | 核心争鸣 | 1928–1929 | 工业积累速度、平衡计划与农业条件制约的路线分歧。 | `CLM-erlich-1960-stalin-overkill-turn` |
| `DEB-1929-collectivization-and-dekulakization-causes` | 核心争鸣 | 1928–1929 | 高指标工业化对粮食征收与集体化加速的反向挤压。 | `CLM-davies-1980-autumn-1929-great-turn-fabrication` |

### 2.3 史学争鸣
- **基层动力 vs. 制度退却**：S. A. Smith（1983）证明国有化压力最初很大程度来自工人要求国家接管关厂企业的“自下而上”诉求，并非预设蓝图（`CLM-smith-sa-1983-from-workers-control-to-nationalization`）；E. H. Carr（1952/1954）则剖析战时“总局制”危机、NEP “制高点”控制以及计委在 1922–1923 年沦为测算“真空”的政制过程（`CLM-carr-1952-war-communism-internal-contradictions`、`CLM-carr-1952-nep-retreat-and-commanding-heights`、`CLM-carr-1954-scissors-crisis-mechanics`）。
- **部门博弈、统计失真与大转折**：Alexander Erlich（1960）揭示高速度投资模型与“过度转向”的两难（`CLM-erlich-1960-stalin-overkill-turn`）；尤里·茹科夫（2006）依据全会档案还原索科尔尼科夫与最高经委的预算信贷交锋（`CLM-other-nep-1923-sokolnikov-monetary-discipline`）；R. W. Davies（1980）追踪 1929 年秋计委指标急剧膨胀的体制机制（`CLM-davies-1980-autumn-1929-great-turn-fabrication`）。Davies 纪念论文集（`RN-W23-1920s-red-army-militia-reform-and-davies-festschrift`）中三位作者更分别揭示关键侧面：**Peter Gatrell**（第1章）考证 1917–1918 年最高经委拉林与梅谢尔斯基混合托拉斯谈判及最终强行国有化；**E. A. Rees**（第5章）剖析 1928–1929 年最高经委与交通人民委员部围绕铁路“重建 vs. 合理化”投资的博弈与专家整肃；**Holland Hunter**（第11章）则以 1920 年代末统计透明度终结及 KAPROST 反事实模型与戴维斯展开辩论。
- **档案传记与货币金融补充视角**：И. С. 拉特科夫斯基的捷尔任斯基传记（由 А. М. 普列汉诺夫任档案编者）呈现最高经委领导层的成本平衡思路；Valentin Katasonov（**B 级文献**，`CLM-katasonov-golden-chervonets-rise-and-demise`、`CLM-katasonov-two-circuit-cash-noncash-ruble-dam`）侧重切尔文外贸储备转向与“现金—非现金”双循环大坝，其论点须与财政部及国家银行原始档案互校。

## 2. 一跳邻域全量微摘要目录 (去重后共 18 个节点，0 截断)
- **`EVT-1923-scissors-crisis`**（1923年剪刀差危机与四十六人声明）: 1923年工业品高价、农产品低价与信贷收缩叠加，造成滞销、欠薪及工人抗议，动摇新经济政策的城乡交换。托洛茨基致中央信与四十六人声明分别把经济失衡同党内机关体制相联；价格随后收拢，民主改革争论却在列宁缺席和继承权竞争中转成纪律斗争。 ‖ `→INS-vsnkh-and-gosplan`[industrial_and_planning_tension|1923]: 工业核算、定价与综合协调权的分配构成争议制度背景 ； `←INS-vsnkh-and-gosplan`[政策诱因|1923]: 最高经委盈利原则与商业托拉斯提价促发工农业比价危机。
- **`EVT-1929-great-turn-and-dekulakization-launch`**（1929年秋大转变与全盘集体化、消灭富农启动）: 1929年夏秋集体化指标跃升，征粮压力、工业化动员与击败右派相互强化。十一月全会推动工人下乡，十二月委员会草案仍有保留，继被斯大林否决；二十七日公开宣布消灭富农阶级。政治发动、名义入庄与实际生产改组有别，大规模驱逐制度在次年定型。 ‖ `→INS-vsnkh-and-gosplan`[planning_and_target_escalation|1929.07—12]: 工业需求、控制数字及地方申报推动目标上调 ； `←INS-vsnkh-and-gosplan`[指标引爆|1929.08–12]: 1929年8月计委控制数字跃升直接衔接秋季全面加速转折。
- **`INS-gosbank-and-narkomfin`**（财政人民委员部与国家银行（革命财政、货币与信贷））: 革命政权接管国家银行并国有化私行，内战期撤销人民银行、业务归财政机关。NEP重建银行预算，1922–1924年切尔沃涅茨与贬值苏维埃纸币先并行后统一。二十年代末信贷与工业投资争论引发银行领导更替；1930年后现金与非现金结算之分，不可回填为1929年已完善的封闭双循环。 ‖ `→INS-vsnkh-and-gosplan`[contested_credit_and_investment|1923–1929]: 工业周转及投资要求与财政、货币约束交锋，具体争端须逐案考证 ； `←INS-vsnkh-and-gosplan`[信贷与预算博弈|1923–1929]: 围绕切尔文稳定、预算削减与重工业放贷持续发生部门冲突。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←INS-vsnkh-and-gosplan`[创立与拟权|1917.12–1923]: 力挺成立最高经委，1922年12月又倡议赋予计委立法职能。
- **`ORG-factory-committees-1917`**（1917–1918年彼得格勒及全俄工厂委员会（Фабзавкомы））: 二月革命后兴起的企业工人自治与监督组织，先在彼得格勒国有军工大厂成形。十月前开四次市级及一次全俄代表会议，至1918年初市级共六次；从保生产、防失业转向政治激进。1918年初经济瓦解与政党生产主义推动其并入产业工会，管理趋于国家集中，但合议制与自主诉求仍存。 ‖ `←INS-vsnkh-and-gosplan`[吸收与集中化|1917.11–1918.06]: 将分散工人监督纳入“企业—区—市—国”垂直国有化体系。 ； `→INS-vsnkh-and-gosplan`[progenitor-and-absorbed|1917.10–1918.06]: 工厂委员会中央理事会于 1917-10-26–27 [O.S.] / 11-08–09 [N.S.] 率先倡议创设该机构并推动基层接管，后反被纳入其集权管理体系
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←INS-vsnkh-and-gosplan`[制度共存与退却|1921–1929]: 托拉斯核算、控制数字与市场货币体制在“制高点”内并存。
- **`CON-smychka`**（工农结合）: 工农结合原指连接或接合，在新经济政策下指国营工业与农民经济通过商品交换、价格和合作社形成的纽带。1923年剪刀差暴露其脆弱性，布哈林与普列奥布拉任斯基提出不同工业化方案；1928至1929年强制征购和集体化使结合逐渐转向行政组织与“生产性结合”。 ‖ `←INS-vsnkh-and-gosplan`[价格中介|1923–1927]: 工业定价、投资配比与农产比价直接牵动城乡结合稳定性。
- **`PER-sokolnikov`**（格里戈里·索科尔尼科夫）: 布尔什维克财政领袖与布列斯特和约签署代表，曾在内战中支持正规军建设。1922—1926年主持财政，以切尔文改革、预算和信贷纪律稳定新经济政策，却与工业扩张需求冲突。1925年参加新反对派，要求撤换斯大林总书记；1928年陪同布哈林密会加米涅夫，后转外交，1939年狱中被害。 ‖ `←INS-vsnkh-and-gosplan`[财政制衡|1922–1926]: 以紧缩预算和币值稳定制约最高经委与计委投资冲动。
- **`PER-pyatakov`**（格奥尔基·皮达可夫）: 乌克兰布尔什维克左派与苏维埃工业金融干才（1890–1937，本卡至1929年）。列宁《遗嘱》点名的六位核心领袖之一；1923年任最高国民经济委员会副主席起草盈利令引发剪刀差争论，联署《四十六人声明》并任联合反对派骨干；1928年率先脱离托洛茨基复职执掌国家银行，支持一五工业化冲刺。 ‖ `←INS-vsnkh-and-gosplan`[工业集权推手|1923–1929]: 最高经委副主席，推动1923年盈利命令与重工业信贷扩张。 ； `→INS-vsnkh-and-gosplan`[deputy_chair_industrializer|1923–1926]: 任最高国民经济委员会副主席起草1923年7月托拉斯盈利指令，代表大工业部门抗衡财政部紧缩路线
- **`PER-dzerzhinsky`**（费利克斯·捷尔任斯基）: 波兰立陶宛社民党与布尔什维克领导人。1917年建全俄肃反委员会（契卡）并续掌GPU/OGPU至逝世，奠定苏维埃安全与法外镇压体制；1924–1926年兼任最高国民经济委员会主席，力挺新经济政策市场均衡、保护技术专家并反对超工业化，1926年7月预警“红色独裁者”后猝逝于中央全会。 ‖ `←INS-vsnkh-and-gosplan`[经委主席|1924.02–1926.07]: 兼掌最高经委，主张降低工业成本与保持市场货币平衡。 ； `→INS-vsnkh-and-gosplan`[vsnkh-chairman|1924.02–1926.07]: 掌管最高国民经济委员会期间坚持降本增效、硬预算约束与护卫技术专家，反对盲目重工业跃进
- **`PER-kuibyshev`**（瓦列里安·古比雪夫）: 苏联工业化关键操盘手（1888–1935）。1918年曾在萨马拉追随左派共产主义者并任东线政委；1922年任中央书记，1923–1926年兼掌中监委与工农检查院，将列宁监督构想转为打击反对派工具；1926年接掌最高国民经济委员会，力推重工业高指标并坚定支持斯大林。 ‖ `←INS-vsnkh-and-gosplan`[经委主席|1926.08–1930]: 推动工业加速扩张并压低计委保守派的平衡限制。 ； `→INS-vsnkh-and-gosplan`[chair_and_hyperindustrializer|1926-08–1934-02]: 先后主政VSNKh（1926.08–1930.11）与国家计委（1930.11–1934.02），压制“发生学派”均衡测算，推动“目的论派”高指标五年计划制度化
- **`PER-kondratiev`**（尼古拉·康德拉季耶夫）: 苏俄农业经济学家与长波周期理论创立者（1892–1938）。1917年10月任临时政府粮食部副部长；1920年起执掌财政部景气研究所，在计划方法论战中代表“发生学派”反对高指标目的论，主张依托市场均衡与农产出口推进工业化。1928年被打为“康德拉季耶夫主义”撤职，1938年遇害。 ‖ `←INS-vsnkh-and-gosplan`[方法论对手|1924–1928]: 主张农业均衡与发生学规律，反对脱离市场条件的强行计划。 ； `→INS-vsnkh-and-gosplan`[methodological_opponent|1924–1928]: 作为“发生学派”领袖反对计委/VSNKh“目的论派”脱离农业积累基础的跃进式重工业方案
- **`PER-strumilin`**（斯坦尼斯拉夫·斯特鲁米林）: 苏联经济统计学家与计划方法论家，1921年起任职国家计委，1923年入俄共；早年属孟什维克之说据俄科学院条目，仍待名册核验。二十年代计划论争中被视为目的论代表，主张计划主动重塑经济比例，有别于从既有约束出发的发生论，不能简化为否认一切规律。 ‖ `←INS-vsnkh-and-gosplan`[计划理论家|1921–1929]: 主张目的论计划改造并编制早期剪刀差指数与工业指标。 ； `→INS-vsnkh-and-gosplan`[planner-and-theorist|1921–1929]: 在计委从事统计、计划和方法论工作
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←INS-vsnkh-and-gosplan`[政治驯化与加码|1928–1929]: 依托机关改组和反右倾动员强行拉升五年计划与控制数字。
- **`POL-first-five-year-plan`**（第一个五年计划）: 苏联首部正式工业化纲领，1928–1929年在起点与最高方案争论中定案。1929-04-16至23日中央联席全会、04-23至29日十六次党代表会议及05-20至28日全苏苏维埃五大批准最高方案；下半年投资、钢铁与集体农庄指标加码，冲垮布哈林均衡路线，与NEP退场、强制集体化并进。 ‖ `←INS-vsnkh-and-gosplan`[编制与实施主体|1927–1929]: 最高经委与计委反复改写“最优方案”并陷入1929年高指标竞赛。 ； `→INS-vsnkh-and-gosplan`[drafted-by|1928–1929]: Gosplan/VSNKh 竞争性地抬升控制数字，政治局择高方案
- **`PER-bogdanov`**（亚历山大·波格丹诺夫）: 俄国马克思主义思想家、医生、经验一元论与组织学创立者（1873—1928）。1904—1907年任布尔什维克国内核心二号领袖；1908—1909年因召回主义与哲学论战遭列宁开除后另组前进派并办卡普里、博洛尼亚党校；1917—1920年领导无产阶级文化协会遭收编，1928年死于输血实验。 ‖ `→INS-vsnkh-and-gosplan`[conceptual-precursor|1913–1928]: 《组织学》的系统均衡与组织规划框架在1920年代被部分经济学家与规划者引为苏维埃计划科学的方法论先声（思想史评估存争）
- **`PER-lunacharsky`**（阿纳托利·卢那察尔斯基）: 俄国革命文艺理论家、首任苏俄教育人民委员（1875—1933）。早年与波格丹诺夫、高尔基共倡“造神说”并组前进派党校；1917年随区联派入布尔什维克，十月后长期主持教育与文化事业，在保护旧知识分子、实验教育与激进派间力求平衡；1929年大转变高潮中辞职，1933年病逝法国。 ‖ `→INS-vsnkh-and-gosplan`[jurisdictional-rival|1928–1929]: 1928–1929年间与古比雪夫领导的最高国民经济委员会围绕高等技术院校（VTUZ）归属与狭隘专业化展开激烈部门争夺并最终失守
- **`PER-mikoyan`**（阿纳斯塔斯·米高扬）: 亚美尼亚裔布尔什维克干部，从下诺夫哥罗德转任东南与北高加索党务，1926年任政治局候补委员、掌苏联内外贸易。1928年春夏在法制限度与妥协间摇摆，9月受斯大林施压转向强硬，成为多数派骨干；其部门联系粮食采购、城乡交换与外贸，但强征与出口并非个人或单一部门决策。 ‖ `→INS-vsnkh-and-gosplan`[interagency-counterpart|1926–1929]: 贸易、出口外汇与工业投资计划相互依赖

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


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/43 条)
- **`CLM-smith-sa-1983-from-workers-control-to-nationalization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 155–156, 166–169, 177–179, 184–186, 192（即源文件标注 PDF pp. 160–161, 171–174, 182–184, 189–191, 197）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-carr-1952-war-communism-internal-contradictions`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 70-120 (Chs. 17–18)]: 
- **`CLM-other-nep-1923-sokolnikov-monetary-discipline`** [`SCH-zhukov-yuri`(尤里·茹科夫) | pp. 151-158, 208-212]: 
- **`CLM-davies-1980-autumn-1929-great-turn-fabrication`** [`SCH-davies-rw`(R·W·戴维斯) | Vol. 1 printed pp. 121–123, 128, 133, 147, 151–156, 165, 179–182；Vol. 2 本地 PDF pp. 34, 45, 60–61]: 
- **`CLM-carr-1952-nep-retreat-and-commanding-heights`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 118-166 (Chs. 18–20)]: 
- **`CLM-carr-1954-scissors-crisis-mechanics`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 17, 29-30, 95-96, 100-101, 105-107, 127]: 
- **`CLM-carr-davies-1969-grain-price-scissor-1927`** [`SCH-davies-rw`(R·W·戴维斯) | pp. 44-47 (esp. p. 46)]: 
- **`CLM-plekhanov-am-dzerzhinsky-vsnkh-nep-industrialism-1924-1926`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | pp. 227-230, 236-246, 251-256]: 
- **`CLM-erlich-1960-stalin-overkill-turn`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 161-169, 172-177, 183-184 (PDF pp. 176-184, 187-192, 198-199)]: 
- **`CLM-davies-festschrift-1995-nep-statistics-and-planning-debates`** [`SCH-hunter-holland`(霍兰·亨特 · cliometrics) | pp. 18-21, 82-94, 218-226]: 
- **`CLM-katasonov-golden-chervonets-rise-and-demise`** [`SCH-katasonov-valentin`(瓦连京·尤里耶维奇·卡塔索诺夫) | pp. 112–113（馆藏中译本 PDF）]: 
- **`CLM-katasonov-two-circuit-cash-noncash-ruble-dam`** [`SCH-katasonov-valentin`(瓦连京·尤里耶维奇·卡塔索诺夫) | pp. 152–153（馆藏中译本 PDF）]: 
- **`CLM-nationalization-docs-1917-workers-control-to-june-1918-decree`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | nationalization_docs PDF pp. 1-841 (PDF-I pending OCR); Zemskov PDF p. 11 (原书 p. 9)]: 
- **`CLM-carr-davies-1969-nemchinov-table-critique`** [`SCH-davies-rw`(R·W·戴维斯) | pp. 55, 72-73, 117, 244-246]: 
- **`CLM-smith-1983-post-october-centralization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | pp. 208, 239–263 (PDF pp. 220, 251–275)]: 
- **`CLM-fitzpatrick-1979-1928-shakhty-and-vydvizhentsy`** [`SCH-fitzpatrick-sheila`(希拉·菲茨帕特里克) | pp. 113–119, 139]: 
- **`CLM-cohen-1973-nep-viability`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 270-276, 316-320]: 
- **`CLM-cohen-1973-notes-of-an-economist`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 295-296, 318-320]: 
- **`CLM-cohen-1973-bukharin-organizational-defeat`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 287-289, 297-301, 322-329]: 
- **`CLM-erlich-1960-bukharin-balanced-growth`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 21-23 (PDF pp. 38-40)]: 
- **`CLM-erlich-1960-preobrazhensky-dilemma`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 34-36, 40-41, 49-51, 170-171 (PDF pp. 51-53, 57-58, 66-68, 185-186)]: 
- **`CLM-nove-1964-stalin-necessity-dilemma`** [`SCH-nove-alec`(亚历克·诺夫) | pp. 20-26, 32]: 
- **`CLM-kotkin-2014-bukharin-dilemma`** [`SCH-kotkin-stephen`(斯蒂芬·科特金) | EPUB Coda (OEBPS/9780698170100_EPUB_1-25.xhtml) & Ch. 14 (OEBPS/9780698170100_EPUB_1-24.xhtml)]: 
- **`CLM-fitzpatrick-1978-anti-bukharin-ideological-offensive`** [`SCH-fitzpatrick-sheila`(希拉·菲茨帕特里克) | pp. 11–14, 20–21]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 11 条 L3 逐日细节见 `timeline/L3_daily/`)
