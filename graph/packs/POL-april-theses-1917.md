# 1-Hop 平衡上下文包：`POL-april-theses-1917` (《四月提纲：论无产阶级在这次革命中的任务》)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/policies/POL-april-theses-1917.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `lenin-text-lih, party-moderates-loginov, eyewitness-sukhanov, bolshevik-grassroots-rabinowitch`
- **待补齐视角**: `factory-committee-reception-polls, provincial-soviet-debates`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `factory-committee-reception-polls, provincial-soviet-debates`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1917年4月列宁归国后提出的十项纲领：宣布不给临时政府任何支持、批判“革命护国主义”、主张从资产阶级革命第一阶段向工兵苏维埃掌权第二阶段过渡，并倡议银行国有化、土地社会化与改党名；打破加米涅夫—斯大林有条件支持临时政府路线，经党内激烈辩论逐步重塑布尔什维克战略。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **宣读与发表（1917.04.04–07 [O.S.] / 1917-04-17–20 [N.S.]）**：`1917-04-04 [O.S.] / 1917-04-17 [N.S.]` 列宁在出席全俄工兵苏维埃会议的布尔什维克代表会及布尔什维克—孟什维克联席会上宣读提纲；`1917-04-07 [O.S.] / 1917-04-20 [N.S.]` 《真理报》第26号刊出，编辑部声明仅代表列宁个人观点（S级：`sources/web-archive/E06_E10_turning_points/1917-04-04_april-theses.md`）。核心命题：**不给临时政府任何支持**；**全部政权归工人、士兵和雇农苏维埃**；革命正处在从第一阶段向第二阶段过渡（`CLM-loginov-lenin-vs-party-moderates-1917`）。
- **党内反弹与渐进吸收（1917.04–06）**：彼得格勒委员会 **`13:2:1`** 否决提纲；加米涅夫在《真理报》坚称革命仍是资产阶级民主革命，斯大林附和“有模式无事实”（`CLM-loginov-lenin-vs-party-moderates-1917`）。列宁在《论策略书》中批判“老布尔什维克档案”公式，四月会议后提纲要点逐步进入党决议，但未立即推翻苏维埃多数派的对外政策。
- **与七月、十月的张力（1917.07–10）**：七月危机中列宁要求放弃和平口号“全部政权归苏维埃”，主张在军事独裁与工人武装起义间抉择，扩大会议仍未接受（同上 CLM）。九月以来重新把苏维埃夺权与十月军事革命委员会实践衔接（`CLM-rabinowitch-1968-divided-bolshevik-party-july`, `CLM-loginov-lenin-early-synthesis-and-1917-strategy`）。提纲本身未规定武装起义日期，却设定了“不向临时政府委托信任”的道德—政治底线。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | `authored` | 1917.04 | 归国后以个人名义宣读，后转化为党的战略目标 | `1917-04-04_april-theses.md`; `CLM-loginov-lenin-vs-party-moderates-1917` |
| `PER-kamenev` | `opposed-then-qualified` | 1917.04–1917.10 | 批判提纲“越阶段”，十月前仍犹豫武装起义 | `CLM-loginov-lenin-vs-party-moderates-1917`, `CLM-sukhanov-1922-lenin-april-arrival-shock` |
| `PER-stalin` | `initially-cautious` | 1917.04 | 与加米涅夫一道守旧阶段论，四月后才左转 | `CLM-loginov-lenin-vs-party-moderates-1917` |
| `ORG-provisional-government` | `no-confidence` | 1917.04起 | 提纲第3条要求不给任何支持并揭露其兼并诺言 | S级提纲第3、7条 |
| `ORG-petrograd-soviet` | `power-destination` | 1917.04–1917.10 | 主张自下而上苏维埃共和国取代议会制 | 提纲第4–5条；`CLM-sukhanov-1922-lenin-april-arrival-shock` |
| `ORG-mensheviks` | `debated-against` | 1917.04 | 联席会上把列宁方案斥为巴枯宁式呓语 | `CLM-sukhanov-1922-lenin-april-arrival-shock` |
| `CON-permanent-revolution` | `strategic-convergence` | 1917.04起 | 界定第二阶段为向社会主义过渡，与不断革命论实践交汇但文本未点名托洛茨基 | `CON-permanent-revolution` 卡；`CLM-lih-2006-erfurtian-merger-formula` |
| `EVT-1917-10-october-revolution` | `strategic-prelude` | 1917.04–10 | “不给临时政府支持”底线为十月非委托信任夺权奠定合法性 | `DEB-1917-october-coup-or-social-revolution` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1917年4月列宁提出十项提纲；反对支持临时政府与革命护国主义；主张苏维埃掌权与向社会主义阶段过渡；党内初期遭遇强烈反对，后逐渐被布尔什维克吸收为战略方向。
- **主要解释分歧**（详参 `DEB-1917-october-coup-or-social-revolution`）：
  - **[党内民主与节奏论 / Vladlen Loginov]** (`CLM-loginov-lenin-vs-party-moderates-1917`, `CLM-loginov-lenin-early-synthesis-and-1917-strategy`)：提纲打破温和派路线，但列宁本人同时声明“不是布朗基主义者”，四月、七月、九月三次遭中央多数否决，反驳“列宁四月一来党即铁板一块”神话。
  - **[现场震惊与护国阵线 / Sukhanov]** (`CLM-sukhanov-1922-lenin-april-arrival-shock`)：亲历者记录士兵欲用刺刀对付列宁、加米涅夫耸肩“等着”，《真理报》一周后才拒收全文——强调四月提纲在左翼民主派眼中的突兀与危险。
  - **[草根吸收曲线 / Rabinowitch]** (`CLM-rabinowitch-1968-divided-bolshevik-party-july`, `CLM-rabinowitch-2007-contingency-of-dictatorship`)：工厂与驻军支部比中央委员会更快左转，七月分裂显示纲领传播并非自上而下灌输。
  - **[埃尔福特正统语境 / Lars T. Lih, Eric Blanc]** (`CLM-lih-2006-erfurtian-merger-formula`, `CLM-blanc-2021-revolutionary-kautskyanism-in-empire`)：反对把提纲说成突然改宗托洛茨基主义；列宁仍处考茨基式“合并公式”语义场，战时应变与苏维埃公式是俄国特殊条件下的战略重排。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `PER-lenin`
- **时效关系边** (`PER-lenin` → `POL-april-theses-1917` | `author` | 有效时段: `1917.04`): 返抵彼得格勒即抛出《四月提纲》，扭转国内布尔什维克温和路线，确立不给临时政府任何支持与“全部政权归苏维埃”的战略方向。
- **节点定性微摘要 [T1]** (完备度 `draft`): 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1917-october-coup-or-social-revolution`：十月革命：少数派政变还是社会革命？
## [T1] 核心问题定义
1917年十月彼得格勒的武装夺权，如何与工人、士兵及农民的社会革命联系起来？争议同时涉及夺权方式、支持的范围及政治合法性；城市苏维埃多数、全国选民多数和全国社会诉求不能互相替代。

## [T2] 各学派立场对照矩阵

**经验共识**：彼得格勒军事革命委员会组织武装行动，临时政府于1917-10-25 [O.S.] / 1917-11-07 [N.S.] 被推翻；同一时期苏维埃、军队、工厂和乡村的政治动员有不同节奏。第二次全俄苏维埃代表大会的组成与后续制宪会议选举反映不同选举机制和时点。

| 取向与代表著作 | 解释及依据 | 争议与检验 |
| :--- | :--- | :--- |
| 少数派政变：Richard Pipes, *The Russian Revolution* | 强调列宁领导的组织利用国家崩解、武装力量和政治时机夺权，质疑以苏维埃多数等同全国民主授权。 | 注重夺权机制和强制，但被批评低估支持和平、土地及苏维埃权力的群众动员；武装行动的组织性本身不能证明社会支持不存在。 |
| 社会史与开放性政党：Alexander Rabinowitch, *The Bolsheviks Come to Power*；S. A. Smith, *Red Petrograd*；Diane P. Koenker, *Moscow Workers and the 1917 Revolution* | 分别从彼得格勒政党与驻军、工厂政治及莫斯科工人研究基层激进化。Rabinowitch强调布党在1917年的地方主动性和内部争论及其与群众诉求的互动。 | 城市、行业、驻军与地方不能代表全部农民或全国；支持苏维埃权力、某项政策与支持单党统治也不是同一指标。三位作者的解释重点并不完全相同。 |
| 托洛茨基的双重政权：Leon Trotsky, *The History of the Russian Revolution* | 将临时政府与苏维埃并存视为社会力量分裂的暂时均衡，并把十月解释为群众革命与有领导的起义结合。 | 是重要的一手参与者及事后政治史解释，不能将其自我辩护视为独立证据；需对照其他政党、地方与农村记录。 |

### `DEB-1917-dual-power-and-february-origins`：二月革命起源与“双重政权”宪制形成之争（1917）
## [T1] 核心问题定义
1917年2月彼得格勒政权更迭，究竟是自发性群众行动（妇女罢工—哗变链）几乎没有预定领导，还是由跨党派次精英网络与杜马—苏维埃宪制抉择共同塑形？随之而来的“双重政权”，应被理解为苏维埃对临时政府的有条件让步，还是自由派废除杜马法统后形成的结构性双弱与合法性赤字？

## [T2] 各学派立场对照矩阵

**经验共识**：`1917-02-23 [O.S.] / 1917-03-08 [N.S.]` 前后彼得格勒发生大规模罢工与军队哗变；塔夫利达宫同日出现国家杜马临时委员会与工兵苏维埃两个权力中心；3月2–3日[O.S.]苏维埃批准组建资产阶级临时政府，米留可夫内阁随后宣称不受杜马制约之“全部完满权力”。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **次精英网络与社会史** | Tsuyoshi Hasegawa, *The February Revolution: Petrograd, 1917* (2018) | 约三千名跨党派基层积极分子在高层犹豫时引导罢工扩展；革命非“无人领导”，但领导分散在工厂—兵营网络。 | `CLM-hasegawa-2018-sub-elite-activists` | 偏重首都；对其他大城市自发性差异讨论有限。 |
| **杜马—苏维埃宪制三角** | Hasegawa (同上); Dmitrii Gaida, *Liberal'naia Rossiia v 1914–1917 gg.* 等 | 杜马委员会先于苏维埃设立军事委员会；3月3日[O.S.]米留可夫废除《基本法》使临时政府失去杜马制衡，只能依赖分裂的苏维埃，构成“双弱”结构性双重政权。 | `CLM-hasegawa-2018-duma-committee-revision`, `CLM-hasegawa-2018-dual-power-origins`, `CLM-gaida-2003-liberals-in-february-1917`, `CLM-gaida-2003-progressive-bloc-dilemma` | 自由派能动性与群众压力孰轻孰重，各家权重不同。 |
| **自由派尴尬的护国主义** | Gaida; James D. White, *The Russian Revolution, 1917–1921: A Short History* | 战时自由派要求“信任内阁”却拒担政权责任，二月接掌后战争承诺迅速引爆合法性危机（四月危机）。 | `CLM-gaida-2003-progressive-bloc-dilemma` | 短篇通史概括性强，首都以外质疑。 |
| **亲历者：协定悲剧** | N. N. Sukhanov, *The Russian Revolution, 1917: A Personal Record* (1922) | 2月28日—3月2日谈判描绘苏维埃执委会以“只要临时政府做……就支持”有条件认可资产阶级内阁；强调社会主义者内部的妥协政治。 | `CLM-sukhanov-1922-dual-power-pact` | B级在场回忆录+政治阐释；须与3月3日全权决议对照。 |
| **阶级分析双重政权** | Leon Trotsky, *History of the Russian Revolution* (1930–32) | 资产阶级临时政府与苏维埃代表两种阶级统治的并存，不可调和性决定革命将继续至十月。 | `CLM-trotsky-1930-dual-power-instability` | 事后理论化；不宜单独充当2月事件因果证据。 |
| **社革党—工人复合史** | Michael Melancon（社革工人面向研究）; White（1917 简史） | 强调社革党与新都工人动员工人的交织，批判将2月仅归为“农民党+自发性”之简化。 | （A级；本库 `CLM-*` 待补） | Melancon 证据主要在战前—1917政党工人网络。 |

## 4. 关联时间线锚点 (共 0 条)
