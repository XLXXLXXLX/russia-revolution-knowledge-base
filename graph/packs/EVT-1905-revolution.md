# 1-Hop 平衡上下文包：`EVT-1905-revolution` (1905–1907年俄国第一次革命)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/events/EVT-1905-revolution.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `marxist-revolutionary, gentry-social-history, multi-party-intellectual, borderlands-comparative`
- **待补齐视角**: `imperial-army-specialist, peasant-revolt-quantitative`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `imperial-army-specialist, peasant-revolt-quantitative`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1905年1月9日（公历1月22日）“血腥星期日”至1907年6月3日（公历6月16日）斯托雷平政变之间，帝俄经历和平请愿遭屠杀、十月总罢工、水兵士兵哗变、农民夺地与两届立宪杜马的全面革命。催生圣彼得堡苏维埃原型与《十月宣言》，最终被保守选举法锁入六三体制。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **起点与全国性动员（1905.01–10 [O.S.] / 1905.01.22–1905.11）**：`1905-01-09 [O.S.] / 1905-01-22 [N.S.]` 格奥尔基·加邦神父率十余万工人向冬宫和平请愿遭军警排枪射杀（现代档案核定约200死、800伤，当时舆论传闻高达4,600死伤），击碎“慈父沙皇”神话并触发全俄抗议浪潮。`1905-10-13 [O.S.] / 1905-10-26 [N.S.]` 起圣彼得堡工人代表苏维埃在铁路与全城政治总罢工中承担准市政职能五十余日（赫鲁斯塔廖夫-诺萨尔任主席，托洛茨基任执委会核心文告起草人并在11月26日[O.S.]赫氏被捕后进入三人主席团），托洛茨基称其为革命政府“胚胎”（`CLM-trotsky-1905-petersburg-soviet-embryo-government`）。沙皇被迫于 `1905-10-17 [O.S.] / 1905-10-30 [N.S.]` 颁布《十月宣言》承诺公民自由与杜马立法权。
- **四党类型学竞争与战术摊牌（1905 秋–1906）**：血腥星期日爆发后，列宁、马尔托夫、切尔诺夫、米留可夫对革命性质给出互斥命名，却均否认“即刻社会主义革命”（`CLM-treadgold-1955-four-party-competition-1905`, `[pp. 138–139]`）。立宪民主党入杜马、布尔什维克主张工农民主专政、孟什维克推动资产阶级掌握政权、社革党坚持劳动者政治革命——联盟在土地与暴力问题上迅速撕裂（`CLM-treadgold-1955-kadet-agrarian-and-tactical-failure`）。
- **缙绅立宪攻势与右转（1904 冬–1905 秋）**：革命高潮前，1904年11月地方自治局代表大会以71:27通过要求立法权的宪政决议，士绅借内阁分裂施压专制（`CLM-manning-1982-gentry-fronde-to-reaction`, `[pp. 54–55, 122–124]`）。但1905年10–11月农民袭击庄园触发缙绅“法律与秩序”反动，为保守反扑预备社会基础（同卡, `[p. 132]`）。
- **制度结局：议会+镇压（1906–1907）**：1906–1907年两届杜马遭遇斯托雷平野战法庭与土地法令；`1907-06-03 [O.S.] / 1907-06-16 [N.S.]` 解散第二届杜马并以新选举法把缙绅变成杜马主人（`CLM-manning-1982-june-third-coup-social-basis`, `[pp. 238–239]`），革命在法律意义上被收编进“六三体制”。边疆地区（芬兰、波罗的海、高加索等）在1905年往往达至更高动员度，1917–18年政府形态分化（`CLM-blanc-2021-borderlands-in-1905-and-1917`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `CON-soviet` | `proto-institution` | 1905-10至12 | 圣彼得堡苏维埃在总罢工中行使事实上的城市治理权，奠定1917年苏维埃复辟范式 | `CLM-trotsky-1905-petersburg-soviet-embryo-government` |
| `ORG-kadets` | `emergence` | 1905-10起 | 从解放同盟政纲升格为议会政党，主导前两届杜马 | `CLM-treadgold-1955-kadet-agrarian-and-tactical-failure` |
| `ORG-mensheviks` / `PER-lenin` | `factional-mobilization` | 1905–1906 | 布尔什维克与孟什维克在革命阶段论与临时政府公式上摊牌 | `CLM-treadgold-1955-four-party-competition-1905` |
| `PER-stolypin` | `counter-revolution-institutionalization` | 1906–1907 | 土地法令、野战法庭与六三选举法将革命成果转化为保守秩序 | `CLM-manning-1982-*`, `PER-stolypin` |
| `PER-milyukov` | `constitutional-pole` | 1905–1907 | 以杜马中心路线与有偿征地对抗社会主义土地夺地 | `CLM-treadgold-1955-*` |
| `EVT-1917-02-february-revolution` | `rehearsal-precursor` | 1905–1917 | 苏维埃、总罢工与军人倒戈经验为1917年彼得格勒模式提供模板 | 多元学派；海姆森双重极化见 `DEB-1914-haimson-thesis-stability` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1905年革命终结了1905年前不经沙皇恩准即不可想象的全国政治动员；苏维埃、工会与国家杜马均为其后行动的核心制度词汇。
- **主要解释分歧**：
  - **[托洛茨基革命政府 embryology / Leon Trotsky]** (`CLM-trotsky-1905-petersburg-soviet-embryo-government`, `CLM-trotsky-1905-hypertrophied-tsarist-state`)：把苏维埃视作为政权而斗争的革命政府萌芽，并把沙皇国家概括为超前于社会经济基础的军事—财政畸形体，为后来“不断革命论”提供前瞻（著作1922年定稿，须区分1908–09现场书写与事后总括）。
  - **[Treadgold 四党竞争 / Donald W. Treadgold]** (`CLM-treadgold-1955-four-party-competition-1905`)：强调精英话语预设的联盟边界，而非对群众动员度的直接度量。
  - **[Manning 缙绅双面性 / Roberta Thompson Manning]** (`CLM-manning-1982-gentry-fronde-to-reaction`, `CLM-manning-1982-june-third-coup-social-basis`)：认为革命主要由省缙绅启动宪政攻势，却由同一群体在农民暴力面前促成六月三日反动。
  - **[Blanc 帝国边疆比较 / Eric Blanc]** (`CLM-blanc-2021-borderlands-in-1905-and-1917`)：反对俄中心主义，指出1905在边疆常达局部夺权高峰，其激进/温和谱系影响1917–18政府分化；不可把中央俄区布尔什维克经验普遍化。
  - **[海姆森稳定论入口 / Leopold H. Haimson]**（`DEB-1914-haimson-thesis-stability`）：1905后有限改革与工潮再起并存，1912–1914城市冲突是否证明“稳定”破裂，须与战前罢工统计交叉检验（本事件不先行判决）。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `PER-stolypin`
- **时效关系边** (`PER-stolypin` → `EVT-1905-revolution` | `suppressed-and-reformed` | 有效时段: `1906-1911`): 以战地军事法庭铁腕平息1905–07城乡暴动，发动1907六三政变修改杜马选举法，并推行允许农民退社私有化的土地改革。
- **节点定性微摘要 [T1]** (完备度 `draft`): 帝俄末年内务大臣（1906）暨大臣会议主席（1906–1911）。以野战法庭、1907年6月3日选举法镇压1905革命余波，并推行农户脱离村社的土地改革；被左翼定为“反革命支柱”，亦被视为市场农业国家试验。1911年9月在基辅遇刺身亡。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1914-haimson-thesis-stability`：海姆森命题：战前俄国的社会稳定与双重极化
## [T1] 核心问题定义
一战前俄国工业增长与有限政治改革能否导向持久稳定，还是1912—1914年的城市冲突暴露了难以调和的危机？争论涉及对罢工、政治制度及社会变化的解释，也涉及无法直接验证的无战争反事实。

## [T2] 各学派立场对照矩阵

**经验共识**：1905年革命后帝国出现杜马和有限政治改革，工业恢复增长；1912年后罢工再次高涨。增长、工潮和制度持续并存，均不能单独证明革命必然或稳定必然。

| 取向与代表著作 | 核心论点及依据 | 局限与待检验问题 |
| :--- | :--- | :--- |
| 经济现代化：Alexander Gerschenkron, *Economic Backwardness in Historical Perspective* | 后发工业化和国家、金融机构的作用提供了研究增长与制度适应的视角；增长可成为讨论战前转型潜力的依据。 | 不能由工业增长直接推出宪政稳固，也不宜未经逐文核对把作者笼统归为“必然稳定论”。 |
| 自由派政治史：Richard Pipes, *The Russian Revolution* | 重视国家制度、精英和革命政治，并讨论战前发展及战争的破坏作用。 | 不等于主张沙皇制度已经实现稳固宪政；其对专制遗产和革命行动者的判断与经济乐观论须分开核对。 |
| 城市社会危机：Leopold H. Haimson, “The Problem of Social Stability in Urban Russia, 1905–1917” | 战前城市存在工人与有产社会之间、以及城市社会各阶层与专制官僚之间的双重极化，工潮重燃与政治僵局相互作用。 | 城市材料不自动代表农村与边疆；战前危机严重并不证明无战争也会出现同一种1917年革命。 |
| 劳工组织社会史：Victoria E. Bonnell, *Roots of Rebellion*；Heather Hogan 的彼得堡工人研究 | 将工人的组织、政治身份与车间关系放回地方和职业网络，检验冲突如何形成，避免把工人当作同质人群。 | 两人的地方研究不能直接等同海姆森的全部反事实结论；Hogan具体论证和书目待逐项复核。 |

## 4. 关联时间线锚点 (共 0 条)
