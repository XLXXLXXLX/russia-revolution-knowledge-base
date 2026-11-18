# 1-Hop 平衡上下文包：`ORG-right-opposition-1928` (1928–1929年右翼反对派（右倾集团）)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/organizations/ORG-right-opposition-1928.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `revisionist-cohen, peasant-social-lewin, biographical-kotkin, archival-khlevniuk, local-party-merridale, collective-leadership-apalkov`
- **待补齐视角**: `full-1929-plenum-stenograms-unified`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `full-1929-plenum-stenograms-unified`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1928–1929年以布哈林、李可夫、托姆斯基为首的俄共右派，在新经济政策末期反对斯大林非常征粮、“贡赋论”与强制工业化冒进，捍卫市场激励与工农动态平衡；在书记处机器、自我绑定的派别纪律与社会基础未动员下于1929年被组织击溃。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **粮食危机与政治局路线摊牌（1928.01–07）**：`1928-01-15` 起斯大林赴西伯利亚推行刑法第107条强制征粮，布哈林斥其为“军事封建剥削”（`CLM-kotkin-2014-siberian-grain-turn`）。`1928-07-04` 至 `07-12` 中央全会口头妥协取消部分非常措施，斯大林同时抛出“贡赋论”与阶级斗争尖锐化论断；布哈林 `1928-07-11` 密会加米涅夫，暴露后成为1929年定罪的炸弹（`CLM-cohen-1973-july-1928-plenum-and-kamenev`, `CLM-apalkov-2023-collective-to-personal-dictatorship`）。
- **公开理论抗争与组织阵地失守（1928.08–1929.04）**：
  - `1928-09-30` 布哈林在《真理报》发表 **《一个经济学家的札记》**，以寓言方式批判失衡工业化（`CLM-cohen-1973-notes-of-an-economist`）。
  - 1928年8–10月斯大林系夺取《真理报》《布尔什维克》编委会、击溃乌格拉诺夫莫斯科市委、改组工会领导层（`CLM-cohen-1973-bukharin-organizational-defeat`, `CLM-merridale-1990-uglanov-moscow-collapse`, `CLM-daniels-1960-bukharin-right-opposition-defeat`）。
  - `1929-04` 中央全会联合会议公开谴责右派，布哈林被撤共产国际职务（`MTG-1929-04-cc-joint-plenum`）。
- **公开认错与右派终结（1929.07–11）**：`1929-11-26` 布哈林、李可夫、托姆斯基共同认错；此前点名谴责由政治局内部逐级扩大至全党舆论（Daniels pp. 363–369）。1929年底斯大林推动全盘集体化，新经济政策实质终结（`POL-nep`, `EVT-1928-grain-procurement-crisis`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-bukharin` | `theoretical-leader` | 1928–1929 | 右派首席理论家，《经济学家札记》与动态平衡工业化论的实际代言人 | `CLM-cohen-1973-nep-viability`, `CLM-cohen-1973-notes-of-an-economist` |
| `PER-rykov` | `governmental-figurehead` | 1928–1929 | 人民委员会主席，在政治局捍卫取消非常措施与价格杠杆 | `CLM-cohen-1973-bukharin-organizational-defeat` |
| `PER-tomsky` | `trade-union-anchor` | 1928–1929 | 全苏工会领袖，1928年底工会八大后失去中央工会理事会 | `CLM-daniels-1960-bukharin-right-opposition-defeat` |
| `PER-stalin` | `defeats-organizational` | 1928–1929 | 以书记处“影子政府”、自我批评运动与五年计划项目分配瓦解右派封地 | `CLM-cohen-1973-bukharin-organizational-defeat`, `CLM-khlevniuk-2015-defeat-of-right-opposition` |
| `POL-nep` | `defends -> liquidated-with` | 1921–1929 | 右派视新经济政策为长期社会主义过渡道路；1929年随其败北被弃 | `DEB-1928-bukharin-alternative`, `POL-nep` |
| `POL-ural-siberian-method` | `opposes` | 1928.10–1929 | 反对以村社会操纵与刑法第61条包装的下乡征粮 | `CLM-lewin-peasants-1968-ural-siberian-method` |
| `PER-uglanov` | `organizational-casualty` | 1928.10 | 莫斯科市委右翼支点被中央改组，右派三巨头未公开救援 | `CLM-merridale-1990-uglanov-moscow-collapse` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1928–1929年存在以布哈林、李可夫、托姆斯基为核心的党内右派；反对斯大林征粮非常措施与超工业化跳跃；在组织上于1929年被击败并公开认错。
- **主要解释分歧**（详参 `DEB-1928-bukharin-alternative`）：
  - **[修正派政治传记 / Stephen Cohen]**（`CLM-cohen-1973-bukharin-organizational-defeat`, `CLM-cohen-1973-nep-viability`）：反对“斯大林1928年已不可战胜”的简化论；右派在官僚表面占势却自愿将冲突锁死在高层秘密场域，未转化农民、专家与基层工人的潜在同情；斯大林以“十五大路线捍卫者”而非“大转变狂人”形象赢得1929年多数。
  - **[农民社会史 / Moshe Lewin]**（`CLM-lewin-peasants-1968-ural-siberian-method`, `CLM-lewin-1968-cooperation-shift`）：从农村承受力视角揭示非常措施与乌拉尔—西伯利亚方法如何破坏市场信任并导向集体化，为理解右派政策主张的社会土壤提供底层维度。
  - **[思想—地缘政治传记 / Stephen Kotkin]**（`CLM-kotkin-2014-bukharin-dilemma`, `CLM-kotkin-2014-siberian-grain-turn`）：强调斯大林征粮—集体化转折的列宁主义阶级意识形态内核，同时记录布哈林在“两难”中的理论严肃性——不能将右派仅写成怀旧市场化保守派。
  - **[莫斯科地方政治史 / Catherine Merridale]**（`CLM-merridale-1990-uglanov-moscow-collapse`, `CLM-merridale-1990-grassroots-activist-radicalism`）：乌格拉诺夫莫斯科机器崩溃展示组织分配部（Orgraspred）与工人对“乌格拉诺夫统治”的疏离如何使右派失去首都支点。
  - **[良心系谱与组织拆解顺序 / Robert V. Daniels]**（`CLM-daniels-1960-bukharin-right-opposition-defeat`）：右派失败遵循“先夺宣传与地方机器、后扩大定罪受众”的渐进组织解除，加之右派自身否认分裂、认可打击自己的纪律话语。
  - **[后苏联集体领导解体论 / Oleg Khlevniuk, Dmitry Apalkov]**（`CLM-khlevniuk-2015-defeat-of-right-opposition`, `CLM-apalkov-2023-collective-to-personal-dictatorship`）：右派在1921年喀琅施塔得—十大创伤的话语框架下恐惧被控分裂，密会曝光坐实“暗中结党”，加速政治局从寡头集体领导滑向斯大林个人支配。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `PER-bukharin`
- **时效关系边** (`PER-bukharin` → `ORG-right-opposition-1928` | `theoretical-leader` | 有效时段: `1928.01-1929.11`): 与李可夫、托姆斯基联手抵制斯大林非常征粮与贡赋论，在1929年4月与11月两次中央全会上被击溃。
- **节点定性微摘要 [T1]** (完备度 `draft`): 布尔什维克核心理论家（列宁在“遗嘱”中称其为“全党的宠儿”与“最宝贵和最大的理论家”，同时指其理论观点“只能非常有保留地算作完全马克思主义的”）、《真理报》总编（1917–1929）及共产国际执委会政治书记处实际负责人（1926–1929）。思想历经从1918–1920年“左翼共产主义”向1921年后新经济政策与渐进社会主义路线首席理论家的转型；1925–1927年与斯大林结盟击败左派，1928–1929年因反对暴力征粮与超工业化被斯大林击败并逐出政治局。

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

## 4. 关联时间线锚点 (共 0 条)
