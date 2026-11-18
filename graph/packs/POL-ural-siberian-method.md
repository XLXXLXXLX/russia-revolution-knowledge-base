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

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `EVT-1928-grain-procurement-crisis`
- **时效关系边** (`POL-ural-siberian-method` → `EVT-1928-grain-procurement-crisis` | `coercive-escalation` | 有效时段: `1928-1929`): 以操纵村社大会摊派、五倍罚款与刑法第107/61条入刑强征余粮，导致播面萎缩并直接通向1929年底全盘集体化。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1927年秋至1929年底引发新经济政策（NEP）终结的体制性危机。工业品荒、谷物与畜牧收购比价失衡及1927年战争恐慌引发农民惜售，国家收购量暴跌；斯大林定性为“富农罢卖”，借刑法第107条与“乌拉尔—西伯利亚方法”推行强制征粮，击败布哈林右派并在1929年底转向全盘集体化。

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

- ⚠️ 引用了尚未创建的争鸣卡 `DEB-collectivization-and-kulak-question`
## 4. 关联时间线锚点 (共 0 条)
