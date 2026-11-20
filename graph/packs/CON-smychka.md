# 1-Hop 去重平衡上下文包：`CON-smychka`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`CON-smychka`** (工农结合 | `cards/concepts/CON-smychka.md` | `multi-perspective`): 已覆盖=`lenin-late-strategy, cohen-gradualism, erlich-accumulation, lewin-peasant, carr-davies-economic, zemskov-tribute-b-tier`；待补=`peasant-grassroots-reception`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 150字定性微摘要
工农结合原指连接或接合，在新经济政策下指国营工业与农民经济通过商品交换、价格和合作社形成的纽带。1923年剪刀差暴露其脆弱性，布哈林与普列奥布拉任斯基提出不同工业化方案；1928至1929年强制征购和集体化使结合逐渐转向行政组织与“生产性结合”。

## [T2] 核心脉络与史学争鸣
### 2.1 词义与分期
- **1921—1923年奠基与合作社转向**：Смычка 有接合、联结之义，与一般政治联盟（союз）相关但不完全同义。列宁自 1921 年《粮食税法令》起以实物税与商品交换寻求国营工业与小农经济的持久纽带；1923年1月《论合作社》在承认国家资本主义受挫后完成重要教义转向，提出在国家掌握主要生产资料前提下通过商业合作社引导农民走向社会主义（`CLM-lewin-1968-cooperation-shift`）；同年3月绝笔《宁肯少些，但要好些》更以著名**“换马隐喻”**阐明，必须保持工人阶级对农民的领导与信任、极端节约国家机关，方能“从农民的、庄稼汉的、穷苦的马上跨到大机器工业与电气化的马上”。
- **1923年剪刀差与工业化大辩论（1924—1927）**：1923年工农业相对价格剧烈偏离（至1923-10-01工业零售/农业批发价剪刀差张开至峰顶，`DATA-02-1922-1924-scissors-crisis-and-chervonets`），暴露出工业效率、托拉斯垄断提价与信贷收缩对结合的冲击（`CLM-carr-1954-scissors-crisis-mechanics`）。1925年布哈林主张通过市场和合作社渐进平衡城乡需求；普列奥布拉任斯基则提出“社会主义原始积累”定律，质疑纯市场均衡足以支撑重工业投资，双方均受限于资本匮乏与农民供粮弹性。
- **1928—1929年危机与“生产性结合”转向**：1928年收购危机（斯大林5月28日演说引涅姆奇诺夫表）、非常措施及布哈林9月《一个经济学家的札记》抗辩后，斯大林在 **1929-04-22 联共（布）中央与中监委联席全会《论联共（布）党内的右倾》**（f节）正式提出**“生产性结合”（производственная смычка）**话语：指责旧形式仅满足棉布鞋袜等个人消费，主张依托集体农庄、国营农场、预购合同制（контрактация）与机器拖拉机站满足农业生产重建需求。该演说系反右倾政治动员文本，须与布哈林四天前（1929-04-18）全会辩护词对读。

### 2.2 核心关系网络（结构化边表）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | 概念奠基 | 1921–1923 | 以实物税、《论合作社》与“换马隐喻”确立核心路线。 | `CLM-lewin-1968-cooperation-shift` |
| `POL-nep` | 核心机制 | 1921–1929 | 以市场交换、货币稳定和合作社维系城乡经济纽带。 | `DEB-1928-bukharin-alternative` |
| `EVT-1923-scissors-crisis` | 机制受挫 | 1923 | 工业品相对高价滞销首次冲击城乡结合与货币流通。 | `CLM-carr-1954-scissors-crisis-mechanics` |
| `PER-bukharin` | 渐进方案 | 1925–1929 | 强调农民购买力、合作社与工业稳健增长的均衡互补。 | `CLM-cohen-1973-nep-viability` |
| `PER-preobrazhensky` | 积累质疑 | 1924–1927 | 以不等价交换和积累两难挑战单纯市场均衡方案。 | `CLM-erlich-1960-preobrazhensky-dilemma` |
| `CON-primitive-socialist-accumulation` | 结构张力 | 1924–1928 | 从非社会主义农业提取剩余资金与维系农民激励的冲突。 | `CLM-erlich-1960-preobrazhensky-dilemma` |
| `EVT-1928-grain-procurement-crisis` | 危机转折 | 1927–1928 | 收购锐减与非常措施动摇市场结合的政治前提。 | `CLM-lewin-peasants-1968-grain-procurement-crisis` |
| `PER-stalin` | 概念重构 | 1928–1929 | 借“贡税”论与 1929-04-22 演说将结合转向集体化生产。 | `CLM-erlich-1960-stalin-overkill-turn` |
| `POL-first-five-year-plan` | 制度替代 | 1928–1929 | 高指标重工业优先战略重塑城乡资源转移与收购体制。 | `CLM-zemskov-2018-agrarian-tribute-and-coercive-turn` |
| `DEB-1928-bukharin-alternative` | 核心争鸣 | 1928–1929 | 渐进替代方案的经济可行性与党内政治空间之争。 | `CLM-cohen-1973-bukharin-organizational-defeat` |
| `DEB-1929-collectivization-and-dekulakization-causes` | 核心争鸣 | 1928–1929 | 收购危机如何演变为强制集体化与消灭富农的因果链。 | `CLM-lewin-peasants-1968-ural-siberian-method` |

### 2.3 史学争鸣
- **渐进可能 vs. 结构两难**：Stephen Cohen（1973）强调布哈林平衡路线在经济上的渐进潜力及其政治败北；Alexander Erlich（1960）对比布哈林与普列奥布拉任斯基的积累模型，揭示工业投资瓶梴与斯大林过度转向的结构渊源；Moshe Lewin（1968）既指出列宁《论合作社》转向的商业合作社局限（`CLM-lewin-1968-cooperation-shift`），也从国家—农民冲突说明非常措施与乌拉尔—西伯利亚方法的螺旋升级。
- **价格数据 vs. “贡税”积累**：E. H. Carr 与 R. W. Davies 以 1923 年剪刀差（`CLM-carr-1954-scissors-crisis-mechanics`）及 1927 年粮价剪刀差、涅姆奇诺夫表批判检验政策主张；维克托·泽姆斯科夫（**B 级文献**，`CLM-zemskov-2018-agrarian-tribute-and-coercive-turn`）则结合斯大林 1928-07-09 全会“贡税／特别税”话语，将低价收购解释为工业化积累渠道，但该书属转引且缺 1924–1929 分年净转移实证模型，须严守其与 1930 年强制安置之间的证据边界。农民基层是否认同官方结合话语仍缺充分一线草根材料。

## 2. 一跳邻域全量微摘要目录 (去重后共 15 个节点，0 截断)
- **`CON-kulak`**（富农（作为社会阶层与政治定罪标签））: “富农”兼具农村阶层与政治定罪含义：19世纪原指高利贷盘剥者，列宁称农村资产阶级；斯托雷平改革分离户也遭村社如此指斥。1918年为贫农委员会征粮对象，1925年NEP放宽而农村趋向中农化；1928–1929年经刑法107条与雅科夫列夫委员会转为阶级清洗标签。 ‖ `→CON-smychka`[structural-tension-pole|1921–1929]: 如何区分“须团结的中农”与“须限制的富农”，构成NEP工农结合路线无解的政策边界难题
- **`CON-primitive-socialist-accumulation`**（社会主义原始积累）: 苏联工业化论战核心概念（1920–1929）。由斯米尔诺夫首创、普列奥布拉任斯基1924–1926年确立为“社会主义原始积累规律”，主张在市场框架内压制价值规律，借外贸保护与工业垄断价格从私有小农汲取工业化资金；遭布哈林斥为破坏工农结合，1928年后与斯大林“贡赋论”及暴力集体化形成方法论分野。 ‖ `→CON-smychka`[structural-tension-with|1924–1928]: 揭示了在固定资本集中更新与农民“强制销售”消失的条件下，若不借助价格剪刀差向农业抽取超额积累，城乡商品结合同样会因“工业品饥荒”而断裂 ； `←CON-smychka`[结构张力|1924–1928]: 从非社会主义农业提取剩余资金与维系农民激励的冲突。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←CON-smychka`[概念奠基|1921–1923]: 以实物税、《论合作社》与“换马隐喻”确立核心路线。
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←CON-smychka`[核心机制|1921–1929]: 以市场交换、货币稳定和合作社维系城乡经济纽带。
- **`EVT-1923-scissors-crisis`**（1923年剪刀差危机与四十六人声明）: 1923年工业品高价、农产品低价与信贷收缩叠加，造成滞销、欠薪及工人抗议，动摇新经济政策的城乡交换。托洛茨基致中央信与四十六人声明分别把经济失衡同党内机关体制相联；价格随后收拢，民主改革争论却在列宁缺席和继承权竞争中转成纪律斗争。 ‖ `←CON-smychka`[机制受挫|1923]: 工业品相对高价滞销首次冲击城乡结合与货币流通。 ； `→CON-smychka`[exchange_conditions_strained|1922—1924]: 工农结合取决于价格、商品和购买力，不只是政治口号
- **`PER-bukharin`**（尼古拉·布哈林）: 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。 ‖ `←CON-smychka`[渐进方案|1925–1929]: 强调农民购买力、合作社与工业稳健增长的均衡互补。
- **`PER-preobrazhensky`**（叶夫根尼·普列奥布拉任斯基）: 老布尔什维克经济理论家，1920–1921年任中央书记。1923年起草《四十六人声明》批判书记等级制；1924–1926年提出社会主义原始积累，以价格税收而非行政暴力向私营部门筹资，与布哈林论战。1928–1929年误判斯大林工业化转向而脱离托派求和，1937年被处决。 ‖ `←CON-smychka`[积累质疑|1924–1927]: 以不等价交换和积累两难挑战单纯市场均衡方案。
- **`EVT-1928-grain-procurement-crisis`**（1927冬–1929年粮食收购危机）: 1927年秋冬国家收粮锐减，相对价格、工业品荒与战争恐慌共同削弱售粮意愿。1928年非常措施及随后村社摊派把交换危机转为强制征购和党内路线冲突；布哈林等反对者逐步失势，至1929年底转向全盘集体化。粮食总产、商品粮与国家采购须分开衡量。 ‖ `←CON-smychka`[危机转折|1927–1928]: 收购锐减与非常措施动摇市场结合的政治前提。
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←CON-smychka`[概念重构|1928–1929]: 借“贡税”论与 1929-04-22 演说将结合转向集体化生产。
- **`POL-first-five-year-plan`**（第一个五年计划）: 苏联首部正式工业化纲领，1928–1929年在起点与最高方案争论中定案。1929-04-16至23日中央联席全会、04-23至29日十六次党代表会议及05-20至28日全苏苏维埃五大批准最高方案；下半年投资、钢铁与集体农庄指标加码，冲垮布哈林均衡路线，与NEP退场、强制集体化并进。 ‖ `←CON-smychka`[制度替代|1928–1929]: 高指标重工业优先战略重塑城乡资源转移与收购体制。
- **`CON-socialism-in-one-country`**（一国建成社会主义）: 苏联核心战略概念（1924–1930s）。1924年底由斯大林反击“不断革命论”时首次提出，1925–1926年经布哈林充实为区分“国内建成可能”与“免除外部颠覆之最终胜利”的理论，支撑新经济政策工农市场渐进建设；1928–1929年后内涵剧变为自给自足备战超工业化与强制集体化的动员纲领。 ‖ `→CON-smychka`[internal-class-premise-in-1925|1925–1928]: 在布哈林1925–1927年理论体系中，国内工农市场结合（Смычка）的牢不可破是苏联能够无需西方无产阶级国家援助而独立建成社会主义的唯一阶级前提
- **`CON-state-capitalism`**（国家资本主义（苏维埃政权下的））: 布尔什维克过渡经济概念。列宁1917–1918年以德国战时统制经济为蓝本，将“苏维埃政权下的国家资本主义”定为通向社会主义的进步阶梯，遭左派共产主义者斥为向资本投降；1921年重定义为租让制、租赁与合作社，1923年《论合作社》悄然转向；1925年新反对派反用此词攻击布哈林—斯大林。 ‖ `→CON-smychka`[superseded-by-cooperative-route|1923–1925]: 《论合作社》后，工农结合 + 合作社取代国家资本主义成为NEP社会主义论证核心
- **`EVT-1929-great-turn-and-dekulakization-launch`**（1929年秋大转变与全盘集体化、消灭富农启动）: 1929年夏秋集体化指标跃升，征粮压力、工业化动员与击败右派相互强化。十一月全会推动工人下乡，十二月委员会草案仍有保留，继被斯大林否决；二十七日公开宣布消灭富农阶级。政治发动、名义入庄与实际生产改组有别，大规模驱逐制度在次年定型。 ‖ `→CON-smychka`[transformation_of_worker_peasant_link|1928—1929]: 商品交换意义上的结合转向组织化资源提取，政治口号仍延续
- **`INS-vsnkh-and-gosplan`**（最高国民经济委员会与国家计划委员会（ВСНХ 与 Госплан））: 最高国民经济委员会与国家计划委员会分别承担工业管理与总体计划职能。前者从1917年12月吸纳工人监督演变为内战总局制，新经济政策下改组为经济核算托拉斯；后者自1921年协调预测，二十年代中期后卷入财政纪律、投资速度与第一个五年计划指标的激烈博弈。 ‖ `→CON-smychka`[价格中介|1923–1927]: 工业定价、投资配比与农产比价直接牵动城乡结合稳定性。
- **`PER-kalinin`**（米哈伊尔·加里宁）: 特维尔贫农与彼得堡车工出身的苏维埃名义元首（1875–1946）。1919年接替斯维尔德洛夫任全俄（后苏联）中执委主席，借粮食税与农村巡讲维系“工农联盟”门面；1926年入政治局，1928年私下同情布哈林，据布哈林述称在七月斗争中转附斯大林，保住其“全苏家长”象征地位。 ‖ `→CON-smychka`[public_embodiment_of|1919–1929]: 以“工农双重出身”及《真理报》农村通信、巡回列车向农民宣讲粮食税与工农联盟正当性

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


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/35 条)
- **`CLM-lewin-1968-cooperation-shift`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.8 'Russia between West and East'；列宁原文脚注 Soch. XLV pp. 367, 370, 373, 387–88, 389]: 
- **`CLM-carr-1954-scissors-crisis-mechanics`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 17, 29-30, 95-96, 100-101, 105-107, 127]: 
- **`CLM-cohen-1973-nep-viability`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 270-276, 316-320]: 
- **`CLM-erlich-1960-preobrazhensky-dilemma`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 34-36, 40-41, 49-51, 170-171 (PDF pp. 51-53, 57-58, 66-68, 185-186)]: 
- **`CLM-lewin-peasants-1968-grain-procurement-crisis`** [`SCH-lewin-moshe`(摩西·莱文) | pp. 221, 228-229, 242-243]: 
- **`CLM-erlich-1960-stalin-overkill-turn`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 161-169, 172-177, 183-184 (PDF pp. 176-184, 187-192, 198-199)]: 
- **`CLM-zemskov-2018-agrarian-tribute-and-coercive-turn`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | 馆藏中文PDF pp. 7–8, 10–12；后续比较仅pp. 5–6]: 
- **`CLM-cohen-1973-bukharin-organizational-defeat`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 287-289, 297-301, 322-329]: 
- **`CLM-lewin-peasants-1968-ural-siberian-method`** [`SCH-lewin-moshe`(摩西·莱文) | pp. 386-390, 395]: 
- **`CLM-erlich-1960-bukharin-balanced-growth`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 21-23 (PDF pp. 38-40)]: 
- **`CLM-cohen-1973-july-1928-plenum-and-kamenev`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 289-291]: 
- **`CLM-cohen-1973-notes-of-an-economist`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 295-296, 318-320]: 
- **`CLM-lewin-peasants-1968-kulak-myth-and-serednyak`** [`SCH-lewin-moshe`(摩西·莱文) | pp. 76-78]: 
- **`CLM-carr-davies-1969-grain-price-scissor-1927`** [`SCH-davies-rw`(R·W·戴维斯) | pp. 44-47 (esp. p. 46)]: 
- **`CLM-carr-davies-1969-nemchinov-table-critique`** [`SCH-davies-rw`(R·W·戴维斯) | pp. 55, 72-73, 117, 244-246]: 
- **`CLM-nove-1964-stalin-necessity-dilemma`** [`SCH-nove-alec`(亚历克·诺夫) | pp. 20-26, 32]: 
- **`CLM-kotkin-2014-bukharin-dilemma`** [`SCH-kotkin-stephen`(斯蒂芬·科特金) | EPUB Coda (OEBPS/9780698170100_EPUB_1-25.xhtml) & Ch. 14 (OEBPS/9780698170100_EPUB_1-24.xhtml)]: 
- **`CLM-fitzpatrick-1978-anti-bukharin-ideological-offensive`** [`SCH-fitzpatrick-sheila`(希拉·菲茨帕特里克) | pp. 11–14, 20–21]: 
- **`CLM-khlevniuk-2015-defeat-of-right-opposition`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch03.html（His Revolution 开篇至全盘集体化的 1929 年 11 月宣布）。工作区文本无纸质页码。]: 
- **`CLM-priestland-2007-1928-mobilization-turn-against-bukharin`** [`SCH-priestland-david`(大卫·普里斯特兰) | pp. 234–237; 291–296]: 
- **`CLM-merridale-1990-uglanov-moscow-collapse`** [`SCH-merridale-catherine`(凯瑟琳·梅里代尔) | pp. 53-64]: 
- **`CLM-davies-festschrift-1995-nep-statistics-and-planning-debates`** [`SCH-hunter-holland`(霍兰·亨特 · cliometrics) | pp. 18-21, 82-94, 218-226]: 
- **`CLM-bukharin-preobrazhensky-equilibrium-vs-accumulation-zh`** [`SCH-liu-wei-ping-xinqiao`(刘伟与平新乔 · chinese-political-economy) | 原刊 pp. 92–99 (PDF pp. 1–8；英文提要 pp. 127–128 / PDF pp. 9–10)]: 
- **`CLM-zemskov-2018-archival-constraints-and-party-radicalism`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | 馆藏中文PDF pp. 2–4, 7–10；非俄文原版纸页]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 1 条，另有 46 条 L3 逐日细节见 `timeline/L3_daily/`)
- **1923-10-01 [N.S.]** (`TL-W15-L1-E09-02`, L1): **剪刀差统计峰值** — 卡尔零售价工业187、农业58（1913=100）；与其他口径指数不可混用。
