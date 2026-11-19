# 1-Hop 平衡上下文包：`POL-ural-siberian-method` (乌拉尔—西伯利亚方法与强制征粮配套法制)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/policies/POL-ural-siberian-method.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `peasant-social-lewin, biographical-ideological-kotkin, grain-crisis-synthesis`
- **待补齐视角**: `siberian-local-archive-quantitative`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `siberian-local-archive-quantitative`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1928–1929年冬季斯大林集团在规避“不再重复非常措施”承诺下，于乌拉尔与西伯利亚推广的征粮套路：借无法定人数之村社会“民主表决”摊派超额交粮，辅以合作社断供、五倍罚款（pyatikratka）及刑法第107/61条制裁；收购仍减产约20%，却直接通向1929年底强制集体化。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **1928年初第107条非常措施前史（1928.01–07）**：斯大林西伯利亚之行动用 **苏俄刑法第107条**（反投机）没收余粮、关闭集市，被布哈林右派斥为军事封建剥削（`CLM-kotkin-2014-siberian-grain-turn`, `EVT-1928-grain-procurement-crisis`）。`1928-07` 全会斯大林口头承诺克制非常措施。
- **“乌拉尔—西伯利亚方法”定型（1928.10–1929.06）**：
  - 因1928年减产与乌克兰收购暴跌，当局少直接动用第107条，改将措施包装为“有贫中农支持的自下而上压力”（`CLM-lewin-peasants-1968-ural-siberian-method`）。
  - 法令规定全村交粮额由 **村社会（village society / skhod）** “民主决定”，因无出席法定人数（quorum），地方官员、党支部与贫农小组即可代行全村表决通过中央超额指标（Lewin p. 387）。
  - 配套：**合作社断供**紧缺品；`1929-04` 授权 **五倍粮食罚款（pyatikratka）**；`1929-06` 修订 **刑法第61条第3款**，将拒交村社会“自愿”承担的任务定为最重两年监禁、没收与流放（Lewin pp. 389–390）。
- **失灵与集体化跃迁（1929.07–12）**：虽清洗82%村苏维埃主席并引发怠交（`volynka`）， **1928–29 收购总量仍比上年减20%**（Lewin p. 395）。莫斯科干部痛斥强臂手段无效，僵局推动1929年底全盘集体化决策（Kotkin 强调意识形态—阶级死结与此并行）（`CLM-kotkin-2014-siberian-grain-turn`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-stalin` | `architect-and-promoter` | 1928–1929 | 宣称“自下而上压力”原则，同时承认当局额外施压 | `CLM-lewin-peasants-1968-ural-siberian-method` (`[p. 386]`) |
| `ORG-right-opposition-1928` | `opposed-by` | 1928–1929 | 布哈林集团视其为破坏新经济政策信任与工农联盟的非常措施变体 | `CLM-cohen-1973-notes-of-an-economist`, `ORG-right-opposition-1928` |
| `POL-nep` | `undermines` | 1928–1929 | 市场激励与自愿售粮机制被行政强制与刑事制裁侵蚀 | `DEB-1928-bukharin-alternative`, `POL-nep` |
| `EVT-1928-grain-procurement-crisis` | `escalation-within` | 1927–1929 | 本方法是该危机第三—四阶段核心操作手段之一 | `EVT-1928-grain-procurement-crisis` |
| `PER-molotov` | `executed-on-ground` | 1928–1929 | 作为斯大林派地方督战与组织清洗的执行枢纽（旁证详见粮食危机事件卡） | `CLM-lewin-peasants-1968-ural-siberian-method` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1928–29冬季存在被称作“乌拉尔—西伯利亚方法”的征粮程序组合；其核心机制是操纵村社会表决加经济—刑事制裁；未能挽回收购量，却推进农村政体改造压力。
- **主要解释分歧**（详参 `DEB-1928-bukharin-alternative`）：
  - **[农民社会史 / Moshe Lewin]**（`CLM-lewin-peasants-1968-ural-siberian-method`, `CLM-lewin-peasants-1968-grain-procurement-crisis`）：揭示该方法是对1928年7月“不再非常措施”承诺的修辞规避；“民主村社表决”是程序虚构，穷乡缺乏正规贫农组织却被假定存在；收购失败直接构成1929年底集体化政治逻辑的前因。
  - **[意识形态—权力传记 / Stephen Kotkin]**（`CLM-kotkin-2014-siberian-grain-turn`）：将1928年1月西伯利亚讲话与本方法置于列宁主义“阶级恶性循环”意识形态框架——非单纯粮食技术问题；集体化在共产主义反资本主义前提下呈现为“必然”，尽管经济绩效失败。
  - **[修正派与右派视角]**：布哈林—李可夫路线认为该方法摧毁农民售粮激励，以政治命令替代专业经济约束（Cohen/Daniels 右派叙事与此一致，详见 `ORG-right-opposition-1928`）。
  - **定量经济史（Carr-Davies 传统）**：收购量、播面与畜头损失的宏观序列须与 Lewin 地方机制叙述交叉核验（`CLM-carr-davies-1969-grain-price-scissor-1927` 提供价格结构背景）。

## 2. 一跳邻域等权重微摘要 (共 6 个关联节点，严防大卡霸占上下文)
### 邻居节点: `EVT-1928-grain-procurement-crisis`
- **时效关系边** (`POL-ural-siberian-method` → `EVT-1928-grain-procurement-crisis` | `coercive-escalation` | 有效时段: `1928-1929`): 以操纵村社大会摊派、五倍罚款与刑法第107/61条入刑强征余粮，导致播面萎缩并直接通向1929年底全盘集体化。
- **节点定性微摘要 [T1]** (完备度 `draft`): 以 `1927-10-01`（1927/28粮食收购统计年度期界起点，非单日突发事件）至 `1929-12-27`（斯大林宣布“消灭富农阶级”演说日）为期界的引发新经济政策（NEP）终结的体制性危机。工业品荒、农牧收购比价失衡及1927年战争恐慌引发农民惜售，国家收购量在11–12月暴跌；斯大林定性为“富农罢卖”，借刑法第107条与“乌拉尔—西伯利亚方法”推行强制征粮，击败布哈林右派并在1929年底转向全盘集体化。

### 邻居节点: `CON-kulak`
- **时效关系边** (`CON-kulak` → `POL-ural-siberian-method` | `penal-administrative-instrument` | 有效时段: `1928-01–1929-11`): 借刑法第107条、第61条与村社“社会摊派”将拒交余粮农户批量司法定罪为富农
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 俄国农村阶层与政治定罪复合概念。原系19世纪村社对高利贷盘剥者的贬称，列宁定性为农村资产阶级，斯托雷平改革试图培育独立私有农户，部分村社成员将分离户斥为富农；1918年成贫农委员会征粮对象，1925年NEP放宽下农村实呈中农化；1928–1929年经刑法第107条与雅科夫列夫委员会武器化为“作为阶级消灭”的清洗标签。

### 邻居节点: `ORG-right-opposition-1928`
- **时效关系边** (`ORG-right-opposition-1928` → `POL-ural-siberian-method` | `opposes` | 有效时段: `1928.10–1929`): 反对借村社舆论包装刑法第61/107条实施强制下乡征粮与剥夺
- **时效关系边** (`POL-ural-siberian-method` → `ORG-right-opposition-1928` | `opposed-by` | 有效时段: `1928–1929`): 布哈林集团视其为破坏新经济政策信任与工农联盟的非常措施变体
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1928–1929年以布哈林、李可夫、托姆斯基为核心的联共（布）党内温和派联盟，并非严密地下派系，而是依托政府、工会与莫斯科市委抵制非常征粮常态化、“贡赋论”与超工业化冒进；受制于反派别党纪，各阵地逐一遭书记处拔除，1929年11月战败认错。

### 邻居节点: `PER-stalin`
- **时效关系边** (`POL-ural-siberian-method` → `PER-stalin` | `architect-and-promoter` | 有效时段: `1928–1929`): 宣称“自下而上压力”原则，同时承认当局额外施压
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。

### 邻居节点: `POL-nep`
- **时效关系边** (`POL-ural-siberian-method` → `POL-nep` | `undermines` | 有效时段: `1928–1929`): 市场激励与自愿售粮机制被行政强制与刑事制裁侵蚀
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。

### 邻居节点: `PER-molotov`
- **时效关系边** (`POL-ural-siberian-method` → `PER-molotov` | `executed-on-ground` | 有效时段: `1928–1929`): 作为斯大林派地方督战与组织清洗的执行枢纽（旁证详见粮食危机事件卡）
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 布尔什维克核心党务官僚与斯大林头号副手（1890–1986，本卡至1929年）。1917二月在《真理报》与俄国局持反临时政府强硬立场；1921任中央责任书记，后长期作为书记处大总管协同斯大林操盘；1928年11月至1929年4月接掌莫斯科委员会（MK），并代表斯大林阵营加强对共产国际领导工作的控制，推动集体化加速。

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

- ⚠️ 引用了尚未创建的争鸣卡 `DEB-collectivization-and-kulak-question`
## 4. 关联时间线锚点 (共 1 条)
- **1928-01-15 [N.S.]** (`TL-W32-1928-01-15-01`, L3): **斯大林自莫斯科秘密启程赴西伯利亚督粮（公开报刊秘而不宣）** — 斯大林罕见离开莫斯科乘专列东赴丰收却大面积惜售的西伯利亚（《社会主义通报》称莫洛托夫随行）。三周巡视期间苏联公开报刊完全未予报道；此行旨在强力推行《苏俄刑法典》第107条反投机没收条款，属于“第107条非常措施/乌拉尔—西伯利亚督粮实践”，严禁按AUD-14规范倒填为1929年3月方定型的成熟“乌拉尔—西伯利亚方法”。
