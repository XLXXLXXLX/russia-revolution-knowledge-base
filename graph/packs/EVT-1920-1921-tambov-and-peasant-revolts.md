# 1-Hop 平衡上下文包：`EVT-1920-1921-tambov-and-peasant-revolts` (坦波夫安东诺夫起义与1920–1921年农民绿军风暴)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `peasant-social-history, soviet-military-history, provincial-power-archival`
- **待补齐视角**: `partisan-women-gendered`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `partisan-women-gendered`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1920–1921年坦波夫等地农民反抗余粮征集，亚历山大·安东诺夫组建准正规“绿军”，口号含“苏维埃政权不要共产党人”；图哈切夫斯基执掌坦波夫省剿匪部队司令部（作战集团约10万正规军）与契卡人质手段镇压，与喀琅施塔得一并倒逼1921年十大与实物税转向。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **危机链（1918–1920）**：战时共产主义下征粮队配额竞争、地方代理人庇护与农村暴力（坦波夫马尔戈林案等）削弱苏维埃社会基础（`CLM-raleigh-2001-local-bolshevik-violence-and-clientelism`）。1920年征收量超过实际收成，村镇自卫武装连锁扩大。
- **安东诺夫与“绿军”正规化（1920秋–1921春）**：左派社会革命党人安东诺夫接管坦波夫起义领导，到1920年底形成列宁后来承认的政权最大威胁之一（`CLM-figes-1996-peasant-wars-and-nep-retreat`）。起义军并非单纯富农叛乱，社会构成含流民、底层青年与部分前苏维埃干部；政治语义上区分“列宁/土地”与“共产党人/征粮专政”，常见口号变体为“苏维埃政权不要共产党人”。
- **军事镇压（1921）**：红军调集重兵；**米哈伊尔·图哈切夫斯基**任方面军司令，动用航空、装甲列车、毒气等非常手段，并实施**人质令**（亲属连坐等人质政策，与契卡肃反网络配合）瓦解农村支持。镇压与转战并行，至1921年上半年起义核心区被粉碎。
- **政策后果（1921）**：列宁在俄共十大开幕称农民战争危险超过邓尼金、尤登尼奇与高尔察克之和；坦波夫持续危机与2–3月喀琅施塔得水兵起义共同加深了立即以实物税取代余粮征集制的紧迫感（`EVT-1921-kronstadt`、`POL-nep`、`MTG-1921-rcpb-10th-congress`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `POL-war-communism` | `triggered-revolt` | 1920–1921 | 余粮征集与征粮队暴力为起义直接导火索 | `CLM-figes-1996-peasant-wars-and-nep-retreat` |
| `POL-nep` | `forced-retreat` | 1921.03起 | 农民战争威胁促成实物税与新经济政策框架 | `CLM-figes-1996-peasant-wars-and-nep-retreat`；`EVT-1921-kronstadt` |
| `EVT-1921-kronstadt` | `concurrent-crisis` | 1921.02–03 | 水陆兵变与农民战争并列震动政权，十大期间决定经济退却 | `CLM-avrich-1970-soviets-without-bolsheviks`（语境对勘） |
| `PER-trotsky` | `political-accountability` | 1921 | 作为革军委主席对征粮—军事化路线负政治责任；喀琅施塔得镇压与坦波夫同属危机弧 | Avrich；Figes |
| `ORG-cheka-ogpu` | `counter-insurgency` | 1920–1921 | 肃反与人质机制支援图哈切夫斯基方面作战 | `CLM-cheka-chronicle-hostage-and-local-autonomy`（待延伸引用） |
| `ORG-left-srs` | `ideological-lineage` | 1920–1921 | 安东诺夫等左翼社革党将领把征粮反抗包装为苏维埃话语下的反党专政 | Radkey/Smith 绿线传统 |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1920–1921坦波夫起义规模大、组织度高，是战胜白军后苏维埃政权面临的首要国内武装威胁之一；1921年3月十大确立实物税。
- **主要解释分歧**：
  - **[农民悲剧史 / Orlando Figes]**：起义军并非白军勾结，而是恢复1917–18村社自治幻象的“农民战争”，其威胁超过白将，迫使布尔什维克对农村战略性退却（`CLM-figes-1996-peasant-wars-and-nep-retreat`）。
  - **[外省权力执行史 / Dugarm in Raleigh ed. 2001]**：征粮强度由地方官员博弈与配额庇护塑造，中央指令在坦波夫被变形，不能读成单一自上而下的命令链（`CLM-raleigh-2001-local-bolshevik-violence-and-clientelism`；与 `CLM-raleigh-2001-center-periphery-weak-state-nep` 的萨拉托夫案例并读）。
  - **[布尔什维克与托洛茨基辩护叙事]**：强调 Antonov 阵线含前白军官、在协约国撤离前必须不惜代价恢复粮食垄断与城市供应；压制农民战争与喀琅施塔得被描绘为“悲剧性必要”。
  - **[Avrich 与喀琅施塔得研究]**：虽主研水兵起义，但其对白军策动论证伪与水兵社会构成统计，为理解1921年“双危机”中政权话语策略提供对照（`CLM-avrich-1970-white-plot-refutation` 等）。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `POL-nep`
- **时效关系边** (`EVT-1920-1921-tambov-and-peasant-revolts` → `POL-nep` | `forced-policy-retreat` | 有效时段: `1920.08-1921.03`): 坦波夫与西西伯利亚大规模农民起义连同喀琅施塔得兵变震动政权根基，倒逼列宁在1921年3月废除余粮收集制、转向新经济政策。
- **节点定性微摘要 [T1]** (完备度 `draft`): 1921年3月俄共（布）十大在农村暴动与喀琅施塔得起义危机下确立、取代战时共产主义的混合经济体制：核心是以固定粮食税取代余粮收集制，允许农民自由支配余粮并恢复城乡商品贸易与小私营企业，同时国家掌握大工业、银行、铁路与外贸“制高点”；1928–1929年在粮食收购危机与斯大林击败布哈林集团后终结。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1918-war-communism-ideology-vs-emergency`：战时共产主义本质之争：内战应急、乌托邦跃进还是国家统制连续？
## [T1] 核心问题定义
1918–1921年国有化浪潮、余粮收集制、市场取缔、劳动军事化与工资平均化，究竟是内战与供应崩溃逼迫的应急措施簇，还是布尔什维克反市场社会主义与先锋队权力的乌托邦实验在内战中的激进展开？抑或应置于一战以来国家统制与俄国落后现实的“过渡”话语内理解？“战时共产主义”作为术语在1921年后才定型，争论须区分 **措施序列** 与 **事后标签**。

## [T2] 各学派立场对照矩阵

**经验共识**：1918年春夏国有化扩大；1918–1921 `prodrazvyorstka` 强制征粮；1920–1921劳动军事化与工会国家化高峰；1921年3月党的十大与新经济政策宣布经济“退却”；“военный коммунизм”在1921年党内外论战中作为回顾性概括流传。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **内战军事应急论** | E. H. Carr, *The Bolshevik Revolution, 1917–1923*; Evan Mawdsley, *The Russian Civil War* (1987) | Carr 按法令与机构演进追踪，强调崩溃、战线与物流使强制措施成为可行集合中的选项；Mawdsley 提供军需与行政区背景。 | `CLM-mawdsley-1987-civil-war-militarized-regime`（背景）；Carr（本库 `CLM-*` 待系统入库） | 单以战争不能解释每项选择的意识形态过滤器与党内争论。 |
| **乌托邦跃进幻觉论** | Martin Malia, *The Soviet Tragedy* (1994); Richard Pipes, *The Russian Revolution* (1990) | Malia：马克思主义乌托邦内在悲剧，危机清除障碍使激进蓝图兑现；Pipes：反市场社会主义与废法专政逻辑先行。 | `CLM-pipes-1990-red-terror-leninist-logic`（交叉） | 易由结果倒推单一意图时间表；Malia 长时段，Pipes 偏重1917–18起点。 |
| **战时国家统制连续论** | Lars T. Lih, *Lenin Rediscovered* 系列；S. A. Smith, *Red Petrograd* (1983) 及工人监督研究 | Lih：布尔什维克一贯谈“过渡”与俄国现实，战后共产主义标签是后设；“新经济政策醒悟论”简化了当时选项集。Smith：1917–18工人监督与国有化是社会冲突中的务实演化。 | `CLM-lih-2006-textbook-myth-critique`, `CLM-smith-sa-1983-defensive-workers-control`, `CLM-smith-1983-workers-control-pragmatism`, `CLM-smith-sa-1983-from-workers-control-to-nationalization`, `CLM-smith-sa-1983-factory-committees-vs-trade-unions` | 连续论须与1921年公开承认“过度”文献对读。 |
| **社会结构与退却论** | Moshe Lewin, *The Making of the Soviet System* (1985); *Russian Peasants and Soviet Power* (1968) | 农民反抗、战时村社战争与喀琅施塔得信号促成1921退却；区分危机与“农民社会”结构的钳制。 | `CLM-lewin-peasants-1968-grain-procurement-crisis` | 农村 violence 与首都决策链连接待档案深化。 |

## 4. 关联时间线锚点 (共 0 条)
