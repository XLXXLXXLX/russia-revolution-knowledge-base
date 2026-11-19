# 1-Hop 平衡上下文包：`PER-kaganovich` (拉扎尔·卡冈诺维奇)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/people/PER-kaganovich.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `organizational-history, nationality-policy, archival-post-soviet`
- **待补齐视角**: `full-biography-liberal-totalitarian`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `full-biography-liberal-totalitarian`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
犹太裔出身、斯大林最亲信的组织型干部：1920年代在组织局与书记处负责人事调配与机关整肃；1925–1928任乌共（布）总书记推进并监控乌克兰化；1928年调回莫斯科介入工会整肃，1929年投身集体化与一五计划行政动员，以铁腕执行弥补意识形态干部短缺。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **制革制鞋工人与党的组织机器学徒（1911–1922）**：生于 `1893-11-10 [O.S.] / 1893-11-22 [N.S.]` 基辅省切尔诺贝利附近的卡巴尼村（Кабаны），早年为基辅制革与制鞋工人（кожевник）；1911年加入布尔什维克，内战前后在乌克兰、突厥斯坦与中央机关从事组织、人事与交通党务；以残酷高效、无条件服从斯大林著称，被同僚称为“从党的地下室爬上来的”组织天才。
- **斯大林干部系统核心与书记处要员（1922–1925）**：1922年进入中央组织局，1924年后在斯大林主导的书记处—人事任命（номенклатура）体系中成长为 **负责人事清洗、干部调配与下级党组织整肃的第一干将**；参与1923–1927年击溃托洛茨基、季诺维也夫及“联合反对派”的串联机动，善于以组织决议代替公开辩论（Khlevniuk, Cohen）。
- **乌克兰第一书记与乌克兰化监控（1925–1928）**：`1925-12` 至 `1928-07` 任 **乌克兰共产党（布）总书记** 兼乌克兰苏维埃政府要职；表面上执行 twenties **本土化/乌克兰化（українізація）** 干部与教育政策，扩大乌克兰语公共领域（`CLM-liber-1992-ukrainianization-and-urban-working-class`），同时向莫斯科密报民族政策过激迹象。科恩指出，1928年7月全会前夕斯大林将遭乌克兰代表团怨恨的卡冈诺维奇 **调回中央**，以换取后者在关键表决中满意（`CLM-cohen-1973-july-1928-plenum-and-kamenev`）——组织换票的典型手法。
- **工会夺权与大转变动员（1928–1929）**：`1928-12-10` 至24日 **第八次全苏工会代表大会** 期间，斯大林违反事先承诺强行派卡冈诺维奇嵌入全苏工会中央理事会主席团，镇压捍卫工人福利与集体谈判自主的领导人，迫使托姆斯基于 1928 年 12 月提出抗议辞呈（政治局当时拒绝批准但令其“休假”架空），并于 1929 年 4 月中央与中监委联席全会作出撤职决定、1929 年 6 月 2 日全苏工会中央理事会第二次全会正式解除托姆斯基主席职务（timeline；`CLM-filtzer-1986-1929-tomsky-purge-and-shock-work`）。调回莫斯科后他在中央书记处主持对工会、市委与农村经济机关的 **并行整肃**，1929年与莫洛托夫、米高扬等推动 **全盘集体化舆论准备与基层执行**，成为“大转变”冷战式快速动员的行政酷吏之一。至1929年底仍是斯大林身边最可倚重的组织执行人之一。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-stalin` | `personnel-chief-for` | 1922–1929 | 书记处人事与组织镇压的首要执行者，以任命权为斯大林瓦解反对派地盘 | `CLM-khlevniuk-2015-defeat-of-right-opposition`, `BIB-027` |
| `PER-tomsky` | `purged-via-union-takeover` | 1928-12–1929-06 | 空降全苏工会八大主席团，架空托姆斯基并于1929年4–6月正式撤换，完成工会依附化 | `CLM-filtzer-1986-1929-tomsky-purge-and-shock-work` |
| `POL-korenizatsiia` | `implemented-and-monitored` | 1925–1928 | 在乌克兰推进乌克兰化与干部本土化，同时向中央报告“民族主义”风险 | `CLM-liber-1992-ukrainianization-and-urban-working-class`, `POL-korenizatsiia` |
| `PER-bukharin` | `organizational-adversary` | 1928–1929 | 七月全会前调离乌克兰换取莫斯科关键票；此后参与报刊与机关战线围攻右派 | `CLM-cohen-1973-july-1928-plenum-and-kamenev` |
| `MTG-1929-04-cc-joint-plenum` | `enforcer-at` | 1929-04 | 在联席全会组织工作中配合批判“右倾”并改组经济宣传机关 | `CLM-daniels-1960-bukharin-right-opposition-defeat` |
| `POL-nep` | `liquidates-labor-and-market-autonomy` | 1928–1929 | 工会整肃与行政突击并列，摧毁新经济政策晚期工人集体谈判残余空间 | `CLM-filtzer-1986-1929-tomsky-purge-and-shock-work`, `CLM-davies-1980-november-plenum-to-dekulakization` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：卡冈诺维奇是斯大林体制中最早成型的“纯组织派”人物：不下基层写作，却以人事换票、机关夺权和并行整肃改变力量对比；1928–1929年工会与农村经济机关的突变与其姓名密不可分。
- **主要解释分歧**：
  - **[乌克兰社会史 / George Liber]** (`CLM-liber-1992-ukrainianization-and-urban-working-class`, `CLM-liber-1992-korenizatsiia-paradox-late-1920s`): 强调卡冈诺维奇在乌克兰任内既推动乌克兰化扩大城市与农村乌克兰语公共领域，又充当莫斯科监控器；1927–1928年“两种文化”悖论在其职权范围内积累，为日后反转埋下组织基础。
  - **[修正派与政治局过程史 / Stephen F. Cohen, Robert V. Davies]** (`CLM-cohen-1973-july-1928-plenum-and-kamenev`, `CLM-davies-1980-november-plenum-to-dekulakization`): Cohen 聚焦其 **调职—换票** 交易对右派七月挫败的机制意义；Davies 将1929年11月后集体化命令链上的铁路、征粮与报纸节奏与其行政角色并置，质疑“秋后意外转弯”神话。
  - **[后苏联斯大林传记派 / Oleg Khlevniuk]** (`CLM-khlevniuk-2015-defeat-of-right-opposition`): 把卡冈诺维奇归入斯大林“朋友集团”核心，强调1928年起依靠其在工会与莫斯科党组织制造“下层反叛”夺走托姆斯基、乌格拉诺夫世袭领地，是以秘密机关调动替代公开政治摊牌的范本。

## 2. 一跳邻域等权重微摘要 (共 7 个关联节点，严防大卡霸占上下文)
### 邻居节点: `PER-tomsky`
- **时效关系边** (`PER-kaganovich` → `PER-tomsky` | `apparatus-purger` | 有效时段: `1928-1929`): 1928年自乌克兰调回莫斯科中央书记处，亲自操盘对全苏工会中央理事会托姆斯基派的组织接管与清洗。
- **时效关系边** (`PER-tomsky` → `PER-kaganovich` | `purged-by-sent` | 有效时段: `1928-12–1929-06`): 斯大林派卡冈诺维奇空降全苏工会八大书记处，配合共青团激进分子瓦解托姆斯基主席团，促成其1929年5–6月被正式罢免。
- **节点定性微摘要 [T1]** (完备度 `draft`): 工人出身老布尔什维克，1919–1929年执掌全苏工会并任政治局委员。1920–21年工会争论支持列宁抵制托洛茨基“工会国家化”；新经济政策时期捍卫工会集体谈判自主；1928–29年与布哈林、李可夫结成“右翼三巨头”抗斯大林激进路线，后遭清洗自尽。

### 邻居节点: `PER-stalin`
- **时效关系边** (`PER-kaganovich` → `PER-stalin` | `personnel-chief-for` | 有效时段: `1922–1929`): 书记处人事与组织镇压的首要执行者，以任命权为斯大林瓦解反对派地盘
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。

### 邻居节点: `POL-korenizatsiia`
- **时效关系边** (`PER-kaganovich` → `POL-korenizatsiia` | `implemented-and-monitored` | 有效时段: `1925–1928`): 在乌克兰推进乌克兰化与干部本土化，同时向中央报告“民族主义”风险
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1923年俄共（布）十二大系统确立的苏联早期民族政策：在一党垄断政权与组织集权前提下，推进非俄罗斯地区干部录用、行政司法母语化及民族文教建设。十二大上斯大林在语言权利、边疆发展与第二院立法否决权上作实质让步，但守住第二院代表结构方案；1920年代在乌克兰等地深度推进，1926与1928年相继引发文化与经济自主论争（本卡止于1929年底观察截点，非政策废止日）。

### 邻居节点: `PER-bukharin`
- **时效关系边** (`PER-kaganovich` → `PER-bukharin` | `organizational-adversary` | 有效时段: `1928–1929`): 七月全会前调离乌克兰换取莫斯科关键票；此后参与报刊与机关战线围攻右派
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。

### 邻居节点: `MTG-1929-04-cc-joint-plenum`
- **时效关系边** (`PER-kaganovich` → `MTG-1929-04-cc-joint-plenum` | `enforcer-at` | 有效时段: `1929-04`): 在联席全会组织工作中配合批判“右倾”并改组经济宣传机关
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1929年4月16日至23日，联共（布）中央与中监委联席全会围绕征粮危机、工业化与新经济政策展开高层摊牌。布哈林痛斥“贡赋”与强制，斯大林以“右倾”与密谈案反击；全会秘密解除布哈林与托姆斯基关键职务但暂留三人政治局席位，随后十六次代表会议批准的一五计划仍维持有限集体化目标。

### 邻居节点: `POL-nep`
- **时效关系边** (`PER-kaganovich` → `POL-nep` | `liquidates-labor-and-market-autonomy` | 有效时段: `1928–1929`): 工会整肃与行政突击并列，摧毁新经济政策晚期工人集体谈判残余空间
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。

### 邻居节点: `ORG-right-opposition-1928`
- **时效关系边** (`ORG-right-opposition-1928` → `PER-kaganovich` | `union_purge_enforcer` | 有效时段: `1928-12–1929-05`): 1928.12工会八大空降 VTsSPS 替换托姆斯基人马，将工会转型为生产动员“传送带”
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1928–1929年以布哈林、李可夫、托姆斯基为核心的联共（布）党内温和派联盟，并非严密地下派系，而是依托政府、工会与莫斯科市委抵制非常征粮常态化、“贡赋论”与超工业化冒进；受制于反派别党纪，各阵地逐一遭书记处拔除，1929年11月战败认错。

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

### `DEB-1923-nationality-and-empire`：布尔什维克民族政策、格鲁吉亚事件与苏维埃“肯定性行动帝国”性质之争
## [T1] 核心问题定义
`1922-08` 至 `1923-04-25`（自“自治化”方案、格鲁吉亚冲突至俄共十二大民族问题特别会议闭幕）及其后1920年代本土化实践，布尔什维克是在建设多民族“肯定性行动帝国”内的制度化本土化体制，还是以先锋队组织垄断维系的大俄罗斯官僚集权？争论焦点在于解密速记揭示的制度妥协与各学派因果—价值判断之分。

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 列宁晚期斗争与反官僚论 | Moshe Lewin, *Lenin's Last Struggle* (1968) | 格鲁吉亚事件暴露大俄罗斯沙文主义“为整个政府机器所服务”并与官僚机构合流，列宁晚年警觉最高层专政退化风险，准备清算 *dzerzhimordy*；民族问题是撤换斯大林问责的实质切口之一。 | `CLM-lewin-1968-georgian-affair-bureaucracy`; `CLM-lewin-1968-testament-intent` | 易将列宁口述笔记重构为高度连贯的“遗嘱计划”；写于1990年代十二大特别会议速记解密之前。 |
| 自由主义—极权连续论 | Richard Pipes, *The Formation of the Soviet Union: Communism and Nationalism, 1917–1923* (1954; rev. ed. 1964) | 论证布尔什维克以红军武力征服外高加索与边疆，通过单一集权党中央架空形式上的联邦制；十二大被定性为斯大林行政中央集权对民族自治的彻底胜利（Smith 正面驳斥此说）。 | `CLM-carr-1950-self-determination-to-federal-reunion`；`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` 对勘引述 | 1991年解密的十二大民族问题特别会议速记显示边疆代表反击与中央制度让步远比“单方全胜”复杂。 |
| 解密档案民族妥协论 | Jeremy D. Smith, *The Bolsheviks and the National Question, 1917–1923* (1999) | 列宁—斯大林在集中制原则上确有共识，但 `1923-04` 十二大民族问题特别会议显示边疆代表迫使斯大林大幅退让，奠定1920年代本土化相对稳固期；格鲁吉亚危机不宜简化为列斯个人生死对决。 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`; `CLM-smith-jeremy-1999-georgian-affair-reassessed` | 本土化制度繁荣期止于1930年代逆转，分期边界须清晰。 |
| 帝国史学框架 | Ronald Grigor Suny, *The Red Flag Unfurled* (2017) 等 | 沙俄—苏联宜在“宗主—边缘不平等从属与差异治理”的帝国框架下理解民族建构；1991年后“苏联=帝国”共识含事后目的论归因风险。 | `CLM-suny-2017-empire-and-nationality-dimension` | 帝国理论有助于宏观比较定位，但不能替代十二大速记级制度考证。 |
| 乌克兰社会史与本土化悖论 | George Liber, *Soviet Nationality Policy, Urban Growth, and Identity Change in the Ukrainian SSR 1923–1934* (1992) | 本土化整合城乡乌克兰人、扩张乌克兰语公共领域的同时，制度化语言边界并孕育中央难以完全消化的地方民族诉求。 | `CLM-liber-1992-korenizatsiia-paradox-late-1920s`; `CLM-liber-1992-ukrainianization-and-urban-working-class` | 侧重乌克兰工业城市化案例，外高加索与中亚须分区域检验。 |
| “肯定性行动帝国”概念框架 | Terry Martin, *The Affirmative Action Empire* (2001) 等 | 1920年代苏联对非俄罗斯民族实施制度化优待（干部、语言、教育与领土配额），以党国政治垄断为前提整合多民族边缘——动员成效与潜在离心张力并存。 | （Martin 专著独立论断卡尚待 `close-reader` 入库；现阶段参看 `POL-korenizatsiia` 与 `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`） | 概念易被字面混同于当代西方多元主义平权政策，须严守一党专政前提。 |

## 4. 关联时间线锚点 (共 4 条)
- **1924-05-23 [N.S.]** (`TL-W36-1924-05-23-01`, L3): **俄共（布）第十三次代表大会召开，托洛茨基宣称“党永远正确”** — 1924-05-23至31日俄共（布）十三大召开（748名表决代表，无一反对派）。季诺维也夫要求反对派公开认错遭克鲁普斯卡娅反驳，托洛茨基全程缄默“遗嘱”并声称“不能反对党，归根到底党永远是正确的”。会后斯大林全票连任总书记，布哈林升入政治局，卡冈诺维奇入书记处。（对接TL-W4-E09-1924-02）
- **1926-07-23 [N.S.]** (`TL-W25-1926-07-23-01`, L3): **七月联席全会首次动用十大第7条，将季诺维也夫逐出政治局** — 全会闭幕前首次援引俄共（布）十大《关于党的统一》秘密第7条开除季诺维也夫政治局席位、开除拉斯舍夫中央委员并革去革军委副职外放中东路，增补鲁祖塔克及奥尔忠尼启则、基洛夫、卡冈诺维奇等五名候补。
- **1928-07-04 [N.S.]** (`TL-W32-1928-07-04-01`, L3): **联共（布）七月中央全会开幕（07-04–12），奥新斯基、索科利尼科夫与产粮区大员告警“破裂”危机** — 7月4日全会开幕，首议共产国际事务后转入米高扬粮食报告激辩。奥新斯基、索科利尼科夫痛陈价格剪刀差与城乡“破裂（razmychka）”，主张提价与放缓工业化；产粮区首脑安德烈耶夫、彼得罗夫斯基及斯捷茨基惊呼中农乃至贫农广泛不满（担忧红军内爆发“新喀琅施塔得”）；而加里宁与伏罗希洛夫则在关键时刻倒向斯大林。
- **1929-11-10 [N.S.]** (`TL-W26-1929-11-10-01`, L3): **1929年11月中央全会开幕** — 联共（布）中央全会（11月10—17日）开幕，清算右派并法定推进全盘集体化、二万五千人下乡与非常征购；莫洛托夫、卡冈诺维奇鼓吹立即集体化。
