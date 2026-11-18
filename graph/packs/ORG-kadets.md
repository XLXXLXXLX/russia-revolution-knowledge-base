# 1-Hop 平衡上下文包：`ORG-kadets` (立宪民主党（卡德特党）)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/organizations/ORG-kadets.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `liberal-constitutional, political-biographical-treadgold, gentry-social-history, war-opposition-gaida`
- **待补齐视角**: `provincial-kadet-networks, jewish-cadet-wing`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `provincial-kadet-networks, jewish-cadet-wing`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1905年10月从“解放同盟”蜕变的俄国自由主义核心政党。主张四尾制宪、有偿征地与议会中心路线，主导1906–1907年前两届杜马；一战时组建进步同盟。1917年二月主导首届临时政府，5月后在战争与土地危机中流失社会基础；十月后被宣布为“人民公敌”并在内战与流亡分裂中瓦解。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **从解放同盟到卡德特党（1904–1905）**：1904年10月解放同盟政纲确立四尾制宪、强制征地（公正估价）与八小时工作制，`1905-10-12 [O.S.] / 1905-10-25 [N.S.]` 在莫斯科召开建党大会正式成立立宪民主党（`CLM-treadgold-1955-kadet-agrarian-and-tactical-failure`, `[p. 144]`），在纲领上拒绝对革命暴力的原则性背书（`[p. 216]`）。
- **杜马中心主义、维堡宣言与六三边缘化（1905–1907）**：米留可夫派反对抵制布里根杜马及第一届杜马选举，坚持“抵制即政治自杀”（`[pp. 201–202]`）。`1906-07-09/10 [O.S.]` 第一届杜马被解散后，大批卡德特议员签署号召抗税抗征兵的《维堡宣言》，结果遭判监并剥夺被选举权，使党在第二届杜马丧失大批骨干。`1907-06-03 [O.S.] / 1907-06-16 [N.S.]` 六三政变后，党内部分缙绅右翼拥抱新选举法，中央杜马党团沦为少数反对派（`CLM-manning-1982-june-third-coup-social-basis`, `[p. 239]`）。
- **战前第三届—第四届杜马与进步同盟（1907–1917.02）**：在斯托雷平体制下以法治改革、地方自治扩张和大国自由民族主义维系议会反对形象。1915年8月组建以米留可夫为核心的“进步同盟”，陷入“信任内阁”口号与害怕战时担责之间的结构性两难（`CLM-gaida-2003-progressive-bloc-dilemma`, `[pp. 135–136, 166–168]`）。
- **二月执政、人民公敌令与流亡分裂（1917–1921）**：二月革命后成为首届临时政府主导党，米留可夫于 `1917-03-03 [O.S.] / 1917-03-16 [N.S.]` 推动临时政府脱离国家杜马监督、自承“全部完满权力”（`CLM-hasegawa-2018-dual-power-origins`）。5–7月及 `1917-09-25 [O.S.]` 第三届联合内阁（基什金、柯诺瓦洛夫等入阁）多次参政；1917年11月立宪会议选举中获约4.7%选票（主要集中于彼得格勒、莫斯科城市选区，约17席，`DATA-01`）。`1917-11-28 [O.S.] / 1917-12-11 [N.S.]` 人民委员会颁令宣布立宪民主党为“人民公敌党”予以取缔逮捕，领袖科科什金、欣加廖夫在医院遇害（Pipes, `ch27_section.md`）。内战期间依附白卫政权，1920–1921年流亡巴黎后围绕米留可夫“新策略”（новая тактика）正式分裂。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-milyukov` | `founder-chief-leader` | 1905–1921 | 从思想宗师到外交部长与白卫外交代表，是卡德特党核心政治符号 | `CLM-treadgold-1955-*`, `CLM-gaida-2003-*` |
| `EVT-1905-revolution` | `parliamentary-pole` | 1905–1907 | 坚持杜马宪法斗争路线，在土地与暴力议题上与社会主义者联盟破裂 | `CLM-treadgold-1955-four-party-competition-1905` |
| `PER-stolypin` | `failed-negotiator -> opponent` | 1906–1911 | 1906年夏入阁谈判无果而终，六三政变后党中央转入反对派，部分缙绅右翼则倒向斯托雷平选举体制 | `CLM-manning-1982-june-third-coup-social-basis` |
| `EVT-1917-02-february-revolution` | `provisional-government-backbone` | 1917.02–10 | 在“叹着气的革命者”修辞下接管政权，却政治架空国家杜马自断代议制法统 | `CLM-gaida-2003-liberals-in-february-1917` |
| `EVT-1918-01-constituent-assembly-dispersal` | `defense-league` | 1917-11至1918-01 | 组成保卫立宪会议联盟，11月后遭布尔什维克压制；城市选票无法对抗苏维埃政权 | `CLM-rabinowitch-2007-constituent-assembly`, Pipes `ch21_section.md` |
| `PER-lenin` | `counter-revolutionary foil` | 1905–1918 | 列宁叙事中的“资产阶级叛卖”典型；1917年11月起逮捕卡德特议员 | `CLM-treadgold-1955-kadet-agrarian-and-tactical-failure` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：卡德特党是1905–1917年俄国城市中产阶级与知识分子自由主义向往的政党代名词；其议会路线与有偿征地纲领在农民土地运动面前始终处于结构性弱势。
- **主要解释分歧**：
  - **[Treadgold 1905思想史 / Donald W. Treadgold]** (`CLM-treadgold-1955-four-party-competition-1905`, `CLM-treadgold-1955-kadet-agrarian-and-tactical-failure`)：将卡德特置于四党革命类型学较量中，解释其土地赎买与拒暴力如何同时拉开与社革党及布尔什维克距离。
  - **[Gaida 战争自由派研究 / Fedor Gaida]** (`CLM-gaida-2003-progressive-bloc-dilemma`, `CLM-gaida-2003-liberals-in-february-1917`)：揭示进步同盟组织废墟、米留可夫“信任内阁”三重博弈，以及二月被动接权的怯懦与霸权悖论。
  - **[Hasegawa 宪政三角论 / Tsuyoshi Hasegawa]** (`CLM-hasegawa-2018-dual-power-origins`)：强调卡德特领袖废黜杜马使自由派赢得行政寡头权却失去对苏维埃的宪制抗衡能力。
  - **[Manning 缙绅社会史 / Roberta Thompson Manning]** (`CLM-manning-1982-june-third-coup-social-basis`)：六三后卡德特缙绅右翼与贵族会香槟庆祝斯托雷平政变，提示党的阶级复合性不能化约为“城市自由主义”。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `PER-milyukov`
- **时效关系边** (`PER-milyukov` → `ORG-kadets` | `chief-leader` | 有效时段: `1905-1918`): 创立并领导立宪民主党，1915年组建杜马“进步同盟”，1917年3月任首届临时政府外交部长并因四月照会危机辞职。
- **节点定性微摘要 [T1]** (完备度 `draft`): 俄国历史学家、立宪民主党（卡德特党）核心领袖。曾主持“解放同盟”并提出四尾制宪与有偿征地纲领；1915年组建战时“进步同盟”；1917年二月后任首届临时政府外交部长，在3月3日（俄历）/3月16日（公历）会议上架空国家杜马、宣称“全部完满权力”，5月因坚持参战照会下野。

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

### `DEB-1918-constituent-assembly-and-soviet-democracy`：解散立宪会议与多党苏维埃民主的命运
## [T1] 核心问题定义
1918年立宪会议被武力解散，是否意味着一党统治已不可避免？争论涉及普选制宪与阶级性苏维埃两种合法性、群众动员和镇压，以及此后左翼多党合作与体制内反对派仍有多少政治空间。

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 修正派与地方档案 | Alexander Rabinowitch, *The Bolsheviks in Power* (2007) | 解散由党内斗争、布尔什维克与左翼社革派行动及相当程度的民众冷漠共同促成；多党苏维埃空间在危机中逐步收缩。 | `CLM-rabinowitch-2007-constituent-assembly`; `CLM-rabinowitch-2007-contingency-of-dictatorship`; `CLM-rabinowitch-2007-left-sr-coalition-collapse` | 彼得格勒经验能否推广全国、危机解释是否低估意识形态与主动镇压，均有争议。 |
| 自由主义制度批判 | Richard Pipes, *The Russian Revolution* (1990) | 其政变及早期恐怖论强调夺权意志和强制逻辑；相关卡为比较性依据，并非解散会议的专项证据。 | `CLM-pipes-1990-october-classic-coup`; `CLM-pipes-1990-red-terror-leninist-logic` | 对地方苏维埃、多党合作与党内分歧的解释有待对照。 |
| 孟什维克政治史 | Israel Getzler, *Martov* (1967) | 马尔托夫先谋求社会主义联合政府，后在苏维埃内开展合法或半合法反对，表明反对白军与反对一党恐怖可以并存。 | `CLM-getzler-1967-martov-soviet-opposition` | 传记视角须结合基层选举和代表权记录。 |
| 比较社会与政治史 | Manfred Hildermeier | 是需对读的相关学者；目前未找到本库针对该议题的 CLM，尚不代其归纳具体判断。 | 待建 | 需先核对具体著作、版本和页码。 |

## 4. 关联时间线锚点 (共 0 条)
