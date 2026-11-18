# 1-Hop 平衡上下文包：`ORG-provisional-government` (1917年俄国临时政府)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/organizations/ORG-provisional-government.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `constitutional-liberal-gaida, revisionist-dual-power-hasegawa, menshevik-coalition-galili, bolshevik-local-rabinowitch`
- **待补齐视角**: `provincial-governor-general-network, orthodox-church-apparatus`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `provincial-governor-general-network, orthodox-church-apparatus`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1917年3月至11月俄国最高行政机关：由自由主义杜马派在李沃夫公爵主持下组成，宣称继承沙皇“全部政权”，却在工兵苏维埃与前线《第一号命令》制约下陷入土地、军队与和平三重困局；经四届内阁（李沃夫首届、五月至九月三次资产阶级—社会主义联立内阁及九月短期五人执政内阁）未能稳住宪政民主，终为十月起义推翻。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **诞生、全权宣言与自愿枷锁（1917.03.02–05 [O.S.] / 1917-03-15–18 [N.S.]）**：`1917-03-02 [O.S.] / 1917-03-15 [N.S.]` 国家杜马临时委员会推举李沃夫为总理，米留可夫任外交部长；同日夜与苏维埃执委会达成协议，苏维埃不入阁但予其存在以政治背书（`CLM-sukhanov-1922-dual-power-pact`）。`1917-03-03 [O.S.] / 1917-03-16 [N.S.]` 临时政府首次正式内阁会议排挤罗将柯，宣布政府掌握不受杜马制约的**全部完满权力（вся полнота власти）**并切断与第四届国家杜马机制性联系，代议制根基反被自由派亲手削弱（`CLM-hasegawa-2018-dual-power-origins`）。土地改革拖延、军队民主化与和平外交均受制于苏维埃与士兵委员会。
- **四月危机与首届联立内阁（1917.04–07）**：`1917-04-18 [O.S.] / 1917-05-01 [N.S.]` 米留科夫照会坚持协约国战争目标引发首都大规模示威，李沃夫内阁被迫改组；`1917-05-05 [O.S.] / 1917-05-18 [N.S.]` **策烈铁里、斯科别列夫**等孟什维克与社会革命党人入阁组建首届联合政府，克伦斯基任陆海军部长（`CLM-galili-1989-coalition-government-trap`）。六月攻势失败与列宁政府“德国间谍”指控点燃七月危机。
- **克伦斯基接任总理与第二届联立内阁（1917.07–08）**：`1917-07-08 [O.S.] / 1917-07-21 [N.S.]` 克伦斯基接任总理，并于 `1917-07-24 [O.S.] / 1917-08-06 [N.S.]` 组成第二届联立内阁；临时政府试图恢复前线军纪与死刑，却无法满足工兵诉求，权威加速流失（`CLM-rabinowitch-1968-grassroots-soldier-sailor-radicalism`）。八月科尔尼洛夫事件挫败后，自由派阁员辞职、临时政府威信崩塌，苏维埃左翼决议首次占上风。
- **五人执政内阁、第三届联立内阁与终局（1917.09–10）**：`1917-09-01 [O.S.] / 1917-09-14 [N.S.]` 克伦斯基一度设五人“执政内阁（Директория）”，旋于 `1917-09-25 [O.S.] / 1917-10-08 [N.S.]` 再度吸纳立宪民主党人与 **6 名温和派社会主义部长**（孟什维克格沃兹杰夫任劳工、尼基京任内务兼邮电、马良托维奇任司法，以及普罗科波维奇、利韦罗夫斯基（A. V. Liverovsky）等）组成第三届联立内阁（第四届政府），全俄民主会议与预备议会均未能挽回局势；`1917-10-26 [O.S.] / 1917-11-08 [N.S.]` 彼得格勒军事革命委员会攻占冬宫，留守阁员被捕，正式终结。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-petrograd-soviet` | `dual-power-partner` | 1917.03–1917.10 | 苏维埃提供士兵效忠与集体背书，政府执掌正式部院却无独立强制力，双方“条件决斗”共存 | `CLM-sukhanov-1922-dual-power-pact`, `CLM-hasegawa-2018-dual-power-origins` |
| `ORG-mensheviks` | `coalition-partner` | 1917.05–1917.07 | 革命护国派阁员以少数入阁换取国防与秩序，反而使社会主义者站到群众对立面 | `CLM-galili-1989-revolutionary-defensism`, `CLM-galili-1989-coalition-government-trap` |
| `ORG-psr` | `coalition-partner` | 1917.05–1917.09 | 社革党土地部长切尔诺夫在议会路线内推动土地社会化，被战争财政与内阁分裂牵制 | `CLM-galili-1989-coalition-government-trap` |
| `ORG-kadets` | `ministerial-backbone` | 1917.03–1917.10 | 立宪民主党人把持外交、财政关键部院，米留可夫照会定义战争主义基调 | `CLM-gaida-2003-progressive-bloc-dilemma`, `CLM-hasegawa-2018-duma-committee-revision` |
| `PER-kerensky` | `chairman-premier` | 1917.07–1917.11 | 自陆海军部长升总理，象征个人魅力政权却无力调和前线、后方与苏维埃三重重压 | `CLM-rabinowitch-1968-grassroots-soldier-sailor-radicalism` |
| `EVT-1917-07-july-days` | `repression-trigger` | 1917.07.03–05 [O.S.] / 07.16–18 [N.S.] | 调兵镇压后通缉列宁，加速自由派与激进左翼决裂 | `CLM-rabinowitch-1968-divided-bolshevik-party-july` |
| `EVT-1917-10-october-revolution` | `overthrown-by` | 1917.10.25–26 [O.S.] / 11.07–08 [N.S.] | 军事革命委员会行动与苏维埃二大程序衔接，临时政府丧失首都控制 | `CLM-pipes-1990-october-classic-coup`, `CLM-rabinowitch-2007-contingency-of-dictatorship` |
| `EVT-1917-02-february-revolution` | `successor-regime` | 1917.03起 | 承接沙皇退位后的行政真空，却未能在宪政框架内兑现自由派长期诉求 | `CLM-gaida-2003-liberals-in-february-1917` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1917年3–11月存在以部长会议为形式的全国统一政府；经历至少四次重大改组；在土地、和平与军队指挥权问题上始终无法摆脱苏维埃与前线委员会约束；十月下旬在彼得格勒失去实际权力。
- **主要解释分歧**（详参 `DEB-1917-dual-power-and-february-origins`）：
  - **[自由派“被迫革命”叙事 / Fedor Gaida]** (`CLM-gaida-2003-liberals-in-february-1917`)：杜马自由派并非精心策划的政变赢家，而是在士兵哗变与群众占领下“叹着气”接掌政权；获胜的是塔夫利达宫**场所**而非杜马**机构**，先天拄杖苏维埃。
  - **[双重政权结构论 / Tsuyoshi Hasegawa]** (`CLM-hasegawa-2018-dual-power-origins`, `CLM-hasegawa-2018-duma-committee-revision`)：临时政府宣称独裁权却无兵工群众忠诚；米留可夫废杜马连续性后，合法性的唯一支点变成苏维埃执委会制裁——“悖论”在于强势宣言与弱势根基并存。
  - **[联合政府陷阱论 / Ziva Galili]** (`CLM-galili-1989-coalition-government-trap`, `CLM-galili-1989-revolutionary-defensism`)：社会主义阁员清醒预知入阁会破坏苏维埃监督，却在国家崩溃恐惧下跳入；维护战争努力与经济压制使护国派迅速丧失产业工人。
  - **[首都基层动员视角 / Alexander Rabinowitch]** (`CLM-rabinowitch-1968-grassroots-soldier-sailor-radicalism`, `CLM-rabinowitch-1968-divided-bolshevik-party-july`)：七月与夏秋危机需从驻军、工厂布尔什维克基层组织理解，不能把临时政府失败单纯归因为自由派“软弱”。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `ORG-petrograd-soviet`
- **时效关系边** (`ORG-petrograd-soviet` → `ORG-provisional-government` | `dual-power-dyarchy` | 有效时段: `1917.03-1917.11`): 从二月有条件支持与《第一号命令》掌控驻军，经5-7月联立内阁危机，至9月布尔什维克夺取首都苏维埃多数并在10月通过军革委推翻临时政府。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1917年二月革命后在塔夫利达宫诞生的首都工兵政权：执委会主席始终为齐赫伊泽，策烈铁里是执委会常务局核心领袖并主导“革命护国”路线，颁布《第一号命令》重塑军队纪律；夏秋左翼浪潮下于俄历8月31日（公历9月13日）全体大会首次通过布尔什维克决议，托洛茨基随后当选主席，十月以军事革命委员会夺权枢纽终结临时政府。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1917-dual-power-and-february-origins`：二月革命起源与“双重政权”宪制形成之争（1917）
## [T1] 核心问题定义
1917年2月彼得格勒政权更迭，究竟是自发性群众行动（妇女罢工—哗变链）几乎没有预定领导，还是由跨党派次精英网络与杜马—苏维埃宪制抉择共同塑形？随之而来的“双重政权”，应被理解为苏维埃对临时政府的有条件让步，还是自由派拒绝向国家杜马负责、主张临时政府握有革命赋予的“全部权力”以切断杜马法统约束后形成的结构性双弱与合法性赤字？

## [T2] 各学派立场对照矩阵

**经验共识**：`1917-02-23 [O.S.] / 1917-03-08 [N.S.]` 前后彼得格勒发生大规模罢工与军队哗变；塔夫利达宫同日出现国家杜马临时委员会与工兵苏维埃两个权力中心；3月2–3日[O.S.]苏维埃批准组建资产阶级临时政府，米留可夫内阁随后宣称不受杜马制约之“全部完满权力”。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **次精英网络与社会史** | Tsuyoshi Hasegawa, *The February Revolution: Petrograd, 1917* (2018) | 约三千名跨党派基层积极分子在高层犹豫时引导罢工扩展；革命非“无人领导”，但领导分散在工厂—兵营网络。 | `CLM-hasegawa-2018-sub-elite-activists` | 偏重首都；对其他大城市自发性差异讨论有限。 |
| **杜马—苏维埃宪制三角** | Hasegawa (同上); Dmitrii Gaida, *Liberal'naia Rossiia v 1914–1917 gg.* 等 | 杜马委员会先于苏维埃设立军事委员会；3月3日[O.S.]米留可夫拒绝临时政府向国家杜马负责、主张临时政府握有革命赋予的“全部权力”从而切断杜马法统约束，使临时政府失去杜马制衡，只能依赖分裂的苏维埃，构成“双弱”结构性双重政权。 | `CLM-hasegawa-2018-duma-committee-revision`, `CLM-hasegawa-2018-dual-power-origins`, `CLM-gaida-2003-liberals-in-february-1917`, `CLM-gaida-2003-progressive-bloc-dilemma` | 自由派能动性与群众压力孰轻孰重，各家权重不同。 |
| **自由派尴尬的护国主义** | Gaida; James D. White, *The Russian Revolution, 1917–1921: A Short History* | 战时自由派要求“信任内阁”却拒担政权责任，二月接掌后战争承诺迅速引爆合法性危机（四月危机）。 | `CLM-gaida-2003-progressive-bloc-dilemma` | 短篇通史概括性强，首都以外质疑。 |
| **亲历者：协定悲剧** | N. N. Sukhanov, *The Russian Revolution, 1917: A Personal Record* (1922) | 2月28日—3月2日谈判描绘苏维埃执委会以“只要临时政府做……就支持”有条件认可资产阶级内阁；强调社会主义者内部的妥协政治。 | `CLM-sukhanov-1922-dual-power-pact` | B级在场回忆录+政治阐释；须与3月3日全权决议对照。 |
| **阶级分析双重政权** | Leon Trotsky, *History of the Russian Revolution* (1930–32) | 资产阶级临时政府与苏维埃代表两种阶级统治的并存，不可调和性决定革命将继续至十月。 | `CLM-trotsky-1930-dual-power-instability` | 事后理论化；不宜单独充当2月事件因果证据。 |
| **社革党—工人复合史** | Michael Melancon（社革工人面向研究）; White（1917 简史） | 强调社革党与新都工人动员工人的交织，批判将2月仅归为“农民党+自发性”之简化。 | （A级；本库 `CLM-*` 待补） | Melancon 证据主要在战前—1917政党工人网络。 |

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

## 4. 关联时间线锚点 (共 0 条)
