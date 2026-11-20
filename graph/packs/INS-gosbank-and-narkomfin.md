# 1-Hop 去重平衡上下文包：`INS-gosbank-and-narkomfin`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`INS-gosbank-and-narkomfin`** (财政人民委员部与国家银行（革命财政、货币与信贷） | `cards/institutions/INS-gosbank-and-narkomfin.md` | `multi-perspective`): 已覆盖=`economic-institutional, monetary-history, economic-nationalist-interpretation, carr-davies-statistical-institutional, erlich-industrialization-constraints, katasonov-state-autonomy`；待补=`annual-branch-balance-sheets, regional-cash-clearing, gosbank-annual-reports-primary`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
革命政权接管国家银行并国有化私行，内战期撤销人民银行、业务归财政机关。NEP重建银行预算，1922–1924年切尔沃涅茨与贬值苏维埃纸币先并行后统一。二十年代末信贷与工业投资争论引发银行领导更替；1930年后现金与非现金结算之分，不可回填为1929年已完善的封闭双循环。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **接管与银行国有化（1917–1918）**：`start_ns 1917-11-08` 对应 `1917-10-26 [O.S.]` 的接管起点：站内 L3 记该日约 02:00 起国家银行与车站、发电站等被赤卫队接替（`timeline/L3_daily/1917-10_october_insurrection.md` L174）；Katasonov（B 级二手）则把银行总部被攻占系于 10月24日 [O.S.]（ch48 p. 98），二者日序不同，本卡采 L3 并标注差异。权力接管不等于日常运作恢复：L3 记国家银行宣告已向原临时政府划拨 6.1 亿卢布并拒绝与苏维埃合作（`1917-11_vikzhel…` L108，据 Rabinowitch 2007 / Pipes），Carr 记国有化法令后银行职员罢工延长抵抗，直到1918年1月中旬银行才在新管理层下运作（Carr 卷2 ch05 part_3 L378–379）。`1917-12-14 [O.S.] / 1917-12-27 [N.S.]` 法令宣布银行业为国家垄断、私人股份银行并入国家银行（Carr 卷2 ch05 part_3 L370–372；Katasonov ch48 L23–29）；原国家银行及私人银行业务逐步纳入苏俄人民银行与财政人民委员部框架，Katasonov 称合并至1919年末才完成。机构重组的具体实施日期须按分行及法令核验。
- **内战财政与撤销银行（1918–1920）**：发行纸币、实物征集、预算紊乱和货币贬值共同影响财政，部分理论家曾设想向无货币核算和直接分配过渡，但货币与交易并未因此完全消失。`1920-01-19` 法令撤销苏俄人民银行：站内有两项互证——Carr 记人民委员会法令称工业国有化已将全部工业与贸易置于统一预算之下，“排除了进一步利用国家银行作为以前意义上的国家信贷机构的任何必要性”，其职能交财政人民委员部的新的中央与地方机构，并标注出处 *Sobranie Uzakonenii*, 1920, No. 4–5, art. 25（Carr 卷2 ch07 part_5 L364–370、注 495）；Katasonov 写“1920年1月人民银行被解散，其职能机构转归财政人民委员部中央预算结算管理机关”（ch48 L30–32）。**具体日期 `01-19` 仅见于 istmat.org 转录，站内 Carr 与 Katasonov 只给到“1920年1月”**；部门正式俄文全称与财产转移程序待核原令。不可把纸币退化单因归结为理论选择。
- **NEP与稳币（1921–1924）**：1921年10月苏俄国家银行重建（Carr 卷2 ch08 注 585 记其至 `1921-11-16` 才开业）；沙因曼任行长，1923年改组为苏联国家银行，仍需区分共和国内机构与联盟层级。财政人民委员部首长：1918年1月起古科夫斯基任职，后由克列斯廷斯基取代（Carr 卷2 ch07 part_5 L195–197，取代日期与确切职名待核；站内尚无 `PER-krestinsky` 卡）；`PER-sokolnikov` 记 `1922-01` 任苏俄财政副人民委员并实际主持部务，`1922-11` 任苏俄财政人民委员，`1923-07-06` 至 `1926-01-16` 任苏联财政人民委员。索科利尼科夫吸纳尤罗夫斯基等货币金融专家，强调税收、预算约束、有限信贷和稳定货币。1922年起发行切尔沃涅茨银行券，与持续贬值的苏维埃纸币并行；`1924-02/03` 停印苏维埃纸币，国库券与切尔文固定为 `10 卢布国库券 = 1 切尔文`，并以 `50,000:1`（折合 500 亿旧卢布 : 1 金卢布）收兑1923年版纸币（Carr *Interregnum* pp. 141–142；`DATA-02`；`timeline/L3_daily/1924-01_lenin_death_testament_and_lessons_of_october.md` L79）。法定黄金含量与实际向公众自由兑换是不同问题。
- **信贷与工业化的争论（1923–1928）**：工业托拉斯要求周转资金、扩大投资，财政与银行部门关注预算平衡、货币信用及外汇支付约束；最高国民经济委员会领导层包括捷尔任斯基（1924–1926）及古比雪夫（1926年起）。1923年8月底工业信贷收缩的后果即有争论：Carr 将其置于剪刀差纠正，皮达可夫批评流通和生产受损（`DATA-02`）。黄金外汇储备据 Carr p. 140：`1923-01-01` 约 1,500 万金卢布，`1924-01-01` 约 1.5 亿金卢布（`DATA-02` §2.2）。1925–1928年的具体争端与外汇账应逐案核定，避免将整个工业部门或金融部门视为意见一致的集团。
- **政策转向与两类循环（1926–1929及其后）**：索科利尼科夫 `1926-01-16` 离任财政人民委员，不能称其一直任至1929年；沙因曼担任国银行长的第二任期至1929年4月，其后皮达可夫接任。1929年加速工业化、资金集中与银行清洗改变金融政策；1930年信贷改革进一步集中银行信贷和企业结算。企业账户非现金支付与居民现金工资、零售交换的区分逐渐制度化，但企业仍通过工资、采购等渠道与居民市场发生联系，不能描述为完全不透水的隔离。卡塔索诺夫所谓“双循环大坝”是作者解释性比喻；1922–1924年两种纸币并行是不同意义上的“双轨”。`end_ns 1929-12-31` 为本卡范围终点，不是机构终止日。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 关系实质 | 核心依据 |
| :--- | :--- | :--- | :--- | :--- |
| `POL-sokolnikov-chervonets-monetary-reform` | `implemented_monetary_reform` | 1922–1924 | 财政与国银协调预算、发行及旧纸币收兑；`50,000:1` 收兑、`10:1` 固定 | `DATA-02-1922-1924-scissors-crisis-and-chervonets`；Carr *Interregnum* pp. 141–142 |
| `PER-sokolnikov` | `led_finance` | 1922.11–1926.01.16（苏联部分自1923.07.06） | 担任财政人民委员（1922.01起实际主持部务），强调稳币及预算纪律；1926-01-16 离职 | `PER-sokolnikov` L26；`CLM-other-nep-1923-sokolnikov-monetary-discipline` |
| `INS-vsnkh-and-gosplan` | `contested_credit_and_investment` | 1923–1929 | 工业周转及投资要求与财政、货币约束交锋，具体争端须逐案考证 | Carr *Interregnum* pp. 105–107；`reading-notes/erlich_1960_industrialization/RN-W3-industrialization-models-and-constraints.md` |
| `POL-nep` | `financed_and_regulated` | 1921–1929 | 重建国家银行与财政税收，市场交易与国有经济并存 | Carr；银行年度报告待补 |
| `DEB-1928-bukharin-alternative` | `informed_by_credit_conflict` | 1928–1929 | 投资速度、外汇与物资约束影响政策替代方案的评价 | Carr–Davies；Katasonov 札记 |

### 2.3 史学争鸣光谱
**可确认的经验框架**：国家银行先撤销后重建；稳币经历两种纸币并行；1929年银行领导更替，1930年改革改变信贷和结算制度。**解释分歧**：
- **Carr / Davies（统计与制度框架）**：将信贷、工业价格和农业供给放入可检验的统计与制度背景，Carr 把1920年1月撤销国家银行看作战时共产主义“预算原则取代商业信贷原则”的逻辑后果（卷2 ch07 L362–365）。
- **Erlich 一派（工业化的信贷与资源约束）**：把银行信贷、投资与消费品供给放入工业化模型的约束条件中比较（`RN-W3`），补充 Carr 的价格—信贷叙述；站内尚未形成本卡的专门论断卡。
- **皮达可夫等当事人（论战立场）**：同期批评是政策参与者对紧缩后果的论战判断，不是无争议事实。
- **卡塔索诺夫（国家自主与工业化评价）**：以国家自主及工业化为评价尺度解释外贸垄断和现金／非现金区分，其“大坝”叙事有助提出问题，但其时间划分、隔离程度及因果关系须以银行规章、企业账户和居民收支交叉核验；其著作按本库札记口径列为B级二手解释，不能单独作硬数据定论（`CLM-katasonov-two-circuit-cash-noncash-ruble-dam`）。

## 2. 一跳邻域全量微摘要目录 (去重后共 4 个节点，0 截断)
- **`POL-sokolnikov-chervonets-monetary-reform`**（索科利尼科夫与切尔沃涅茨币制改革）: 1922–1924年索科利尼科夫与尤罗夫斯基、库特列尔等稳定货币：国行发行有黄金、商业资产准备的切尔沃涅茨，先与贬值苏维埃纸币并行，1924年以国库券和收兑统一计价。稳定依赖财政、信贷与商品供给；1925–1926年工业融资及外汇压力又构成约束。 ‖ `←INS-gosbank-and-narkomfin`[implemented_monetary_reform|1922–1924]: 财政与国银协调预算、发行及旧纸币收兑；50,000:1 收兑、10:1 固定 ； `→INS-gosbank-and-narkomfin`[issuing-institution|1922–1924]: 国家银行发行切尔文，财政人民委员部主导预算与货币纪律
- **`PER-sokolnikov`**（格里戈里·索科尔尼科夫）: 布尔什维克财政领袖与布列斯特和约签署代表，曾在内战中支持正规军建设。1922—1926年主持财政，以切尔文改革、预算和信贷纪律稳定新经济政策，却与工业扩张需求冲突。1925年参加新反对派，要求撤换斯大林总书记；1928年陪同布哈林密会加米涅夫，后转外交，1939年狱中被害。 ‖ `←INS-gosbank-and-narkomfin`[led_finance|1922.11–1926.01.16（苏联部分自1923.07.06）]: 担任财政人民委员（1922.01起实际主持部务），强调稳币及预算纪律；1926-01-1…
- **`INS-vsnkh-and-gosplan`**（最高国民经济委员会与国家计划委员会（ВСНХ 与 Госплан））: 最高国民经济委员会与国家计划委员会分别承担工业管理与总体计划职能。前者从1917年12月吸纳工人监督演变为内战总局制，新经济政策下改组为经济核算托拉斯；后者自1921年协调预测，二十年代中期后卷入财政纪律、投资速度与第一个五年计划指标的激烈博弈。 ‖ `←INS-gosbank-and-narkomfin`[contested_credit_and_investment|1923–1929]: 工业周转及投资要求与财政、货币约束交锋，具体争端须逐案考证 ； `→INS-gosbank-and-narkomfin`[信贷与预算博弈|1923–1929]: 围绕切尔文稳定、预算削减与重工业放贷持续发生部门冲突。
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←INS-gosbank-and-narkomfin`[financed_and_regulated|1921–1929]: 重建国家银行与财政税收，市场交易与国有经济并存

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 2 项)
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


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/30 条)
- **`CLM-other-nep-1923-sokolnikov-monetary-discipline`** [`SCH-zhukov-yuri`(尤里·茹科夫) | pp. 151-158, 208-212]: 
- **`CLM-katasonov-two-circuit-cash-noncash-ruble-dam`** [`SCH-katasonov-valentin`(瓦连京·尤里耶维奇·卡塔索诺夫) | pp. 152–153（馆藏中译本 PDF）]: 
- **`CLM-carr-1952-war-communism-internal-contradictions`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | Vol. 2 Chinese PDF pp. 70-120 (Chs. 17–18)]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 56–58, 69, 185–188, 217–218, 283–284]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-smith-sa-1983-from-workers-control-to-nationalization`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 155–156, 166–169, 177–179, 184–186, 192（即源文件标注 PDF pp. 160–161, 171–174, 182–184, 189–191, 197）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-daniels-1960-left-communists-1918`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 70-81]: Daniels：1918年左翼捍卫革命纲领，却在分裂关头受党统一约束
- **`CLM-figes-1996-peasant-wars-and-nep-retreat`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 775-785]: 
- **`CLM-zemskov-1929-dekulakization-demographic-baseline`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | PDF pp. 6-11, 15-19, 52, 218 (原书 pp. 4-9, 13-17, 50, 216)]: 
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

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 4 条 L3 逐日细节见 `timeline/L3_daily/`)
