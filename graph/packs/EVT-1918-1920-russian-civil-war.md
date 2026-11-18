# 1-Hop 平衡上下文包：`EVT-1918-1920-russian-civil-war` (俄国内战（1918–1920）)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/events/EVT-1918-1920-russian-civil-war.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `military-structural, archival-soviet-military, social-history-green, democratic-counterrevolution`
- **待补齐视角**: `full-soldier-diary-corpus, intervention-force-comparative`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `full-soldier-diary-corpus, intervention-force-comparative`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1918–1920年苏俄内战：布尔什维克依托“苏托邦”人口、军火与莫斯科铁路枢纽内线机动，先后粉碎高尔察克、邓尼金、弗兰格尔白军及马赫诺黑军，并压制社革党第三力量；协约国干涉与边疆民族武装相互牵制。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **开局与阵营格局（1918）**：布列斯特和约后红军由志愿制转向普遍义务兵役（`1918-05-29`），托洛茨基在共和国革军委下强制起用逾4.8万前沙皇军官（военспецы）与政委双签制（`INS-rkka-red-army-and-rvr`）。反布尔什维克“联盟”分化：**白军**（高尔察克、邓尼金、尤登尼奇、弗兰格尔）据边疆外线进攻；**绿线/民主反革命**（社革党 Komuch、乌法国务会议等）试图填补红白真空却被右翼政变吞噬（`CLM-smith-scott-2011-psr-third-force-collapse`）；**黑军**（马赫诺）与**民族分离武装**（芬兰、波兰、波罗的海、乌克兰、格鲁吉亚等）各自为政，削弱反苏统一战线。
- **1919决战年（东—南线转折）**：伏龙芝东线南集群于4–6月击溃高尔察克；红军经铁路南调6万精锐后，于9–10月奥廖尔—沃罗涅日轴线以局部兵力密度优势粉碎邓尼金（`CLM-kakurin-1928-red-army-interior-lines-strategy`）。白军分进合击失序，马赫诺切入邓尼金后方加剧溃败（`CLM-mawdsley-1987-white-movement-structural-defeat`）。
- **1920收束（波苏战争与南线）**：红军追击邓尼金残部至克里米亚边界；1920年5–8月波苏战争延缓西线；南方面军于1920年11月歼灭弗兰格尔（`PER-frunze` 指挥南线关键战役）。至1920年11月主要对资内战战线大体停火，征粮—农民战争危机转入1921年坦波夫与喀琅施塔得阶段。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `INS-rkka-red-army-and-rvr` | `institutional-vehicle` | 1918–1920 | 红军专家—政委体制与突击战线铁路调配承载内线战略 | `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` |
| `ORG-psr` | `third-force-collapsed` | 1918夏 | Komuch 借捷克斯洛伐克军团起事却因战争狂热与无自有兵力遭白卫政变清扫 | `CLM-smith-scott-2011-psr-third-force-collapse` |
| `PER-trotsky` | `commanded-red-army` | 1918–1920 | 主持建军、起用военспецы并统筹多战线，奠定胜利组织框架 | `CLM-kakurin-1928-red-army-interior-lines-strategy` |
| `POL-war-communism` | `sustained-mobilization` | 1918–1920 | 余粮征集与强制征用支撑红军规模亦激化农村敌对 | `DEB-1918-war-communism-ideology-vs-emergency` |
| `EVT-1918-03-brest-litovsk-treaty` | `enabled-pivot` | 1918.03起 | 退出大战释放兵力与政治注意力投入内战 | `POL-brest-litovsk-treaty` |
| `POL-brest-litovsk-treaty` | `context` | 1918 | 和约边界划定苏维埃初期战略纵深 | 同上 |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：布尔什维克控制旧帝国人口、军火库存最丰厚的中央地带；白军外线分散、总兵力峰值远低于红军；1919年是决定性战役年。
- **主要解释分歧**：
  - **[地缘—结构派 / Evan Mawdsley]**：胜利系苏托邦人口—工业—军火垄断与白军土地、民族政策破产的结构叠加（`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`、`CLM-mawdsley-1987-white-movement-structural-defeat`）。
  - **[红军官方战略史 / Nikolai Kakurin (1928)]**：内线“梯次累积突击”与突击战线供给机制将物质优势转化为战役胜势（`CLM-kakurin-1928-red-army-interior-lines-strategy`）；成书于个人崇拜篡改前，保留加米涅夫—统帅部争论原貌。
  - **[民主反革命—绿线史 / Radkey经 Smith 2011 文件名索引]**：社革党第三力量因1917后丧失农民武装基础与战争狂热自毁，非单纯军事不敌（`CLM-smith-scott-2011-psr-third-force-collapse`）。
  - **[苏联正统与托洛茨基辩护]**：前者强调革命人民性与党的领导；后者突出托洛茨基建军天才——须与 Mawdsley/Kakurin 结构性解释对勘，避免单因英雄史。

## 2. 一跳邻域等权重微摘要 (共 4 个关联节点，严防大卡霸占上下文)
### 邻居节点: `INS-rkka-red-army-and-rvr`
- **时效关系边** (`INS-rkka-red-army-and-rvr` → `EVT-1918-1920-russian-civil-war` | `won-interior-lines-war` | 有效时段: `1918-1920`): 依托苏维埃腹地6000万人口、沙皇中央军火库与莫斯科放射铁路网，以逾4.8万军事专家与政委双签制在多线内战中击溃分散白军。
- **节点定性微摘要 [T1]** (完备度 `draft`): 苏维埃武装中枢：1918年1月15日（公历1月28日）颁令组建志愿红军，3–9月托洛茨基出任陆海军人民委员暨共和国革军委（RVSR）主席，改行普遍义务兵役、征召逾4.8万前沙皇军官（военспецы）与政治委员双签制；1919八大击退军事反对派与察里津集团；1924–1925伏龙芝改革转向正规军与地方民兵混合体制。

### 邻居节点: `PER-kolchak`
- **时效关系边** (`PER-kolchak` → `EVT-1918-1920-russian-civil-war` | `eastern-white-supreme-ruler` | 有效时段: `1918.11-1920.02`): 1918年11月18日鄂木斯克政变推翻社革党督政府自任最高执政，1919春西进遭伏龙芝东线红军击溃并于伊尔库茨克被处决。
- **节点定性微摘要 [T1]** (完备度 `draft`): 高尔察克（1874–1920），极地探险家、黑海舰队司令；1918年11月18日鄂木斯克政变推翻社革党全俄临时政府，自封“全俄最高执政”；1919春攻势被伏龙芝率红军东线南集群击溃，1920年2月7日在伊尔库茨克被枪决。

### 邻居节点: `PER-denikin`
- **时效关系边** (`PER-denikin` → `EVT-1918-1920-russian-civil-war` | `southern-white-commander` | 有效时段: `1918.04-1920.04`): 统率南俄武装力量于1919年秋推进至奥廖尔逼近莫斯科，因地主复辟、后方马赫诺起义及大俄罗斯沙文主义断送波兰与哥萨克配合而全军覆没。
- **节点定性微摘要 [T1]** (完备度 `draft`): 邓尼金（1872–1947），南俄武装力量总司令；1919年夏秋挥师北进占奥廖尔直指莫斯科；纵容“沙拉班”地主复辟与“统一不可分割俄罗斯”口号疏远农民、哥萨克与波兰，奥廖尔战败后全线崩溃，1920年3月自新罗西斯克撤离；此后流亡，至死未再掌兵。

### 邻居节点: `ORG-makhnovshchina`
- **时效关系边** (`ORG-makhnovshchina` → `EVT-1918-1920-russian-civil-war` | `black-army-swing-force` | 有效时段: `1918-1921`): 以机枪马车高机动游击战重创邓尼金战略后方并助红军攻克克里米亚，旋即遭苏维埃政权清剿覆灭。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 1918–1921年南俄乌克兰无政府共产主义农民—雇农武装：以古利亚伊波列为基地设“自由苏维埃”与公社，以机枪马车（тачанка）机动战术三度联红击白；红军背盟后于1921年覆灭。史学上既是内战地方变体，也是农民反叛与现代政党夺权模式的经典对照案例。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1918-red-terror-and-civil-war-origins`：红色恐怖、契卡扩张与内战期一党专政起源之争（1918–1921）
## [T1] 核心问题定义
1918–1921年红色恐怖、契卡法外处决、对社会主义反对派的镇压，以及内战期间政党竞争被压缩为一党统治，应被解释为布尔什维克意识形态与列宁主义权力逻辑的宿命展开，还是多重危机（经济崩溃、联盟破裂、地方失控、内战动员）下可错链条上的制度选择？恐怖与一党制是同一过程还是须分时段因果？

## [T2] 各学派立场对照矩阵

**经验共识**：1917年12月契卡（全俄肃反委员会）成立；1918年7月左派社会革命党起义后左翼社会主义者被逐出权力结构；1918年9月5日人民委员会颁布《关于红色恐怖》决议；内战1918–1920在多条战线同时进行；1918–1921征粮与契卡行动在地方相互嵌合。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **意识形态宿命论** | Richard Pipes, *The Russian Revolution* (1990); Orlando Figes, *A People's Tragedy* (1996) | 强调反自由主义知识分子传统、列宁废法统治与阶级敌人话语，使恐怖成为夺取与巩固权力的内在逻辑；Figes 另重农民“悲剧”道德经济。 | `CLM-pipes-1990-red-terror-leninist-logic` | 时间线易前推到1917末，低估联盟期与反对派选项；Figes 与 Pipes 因果权重不一。 |
| **复合危机与联盟破裂论** | Alexander Rabinowitch, *The Bolsheviks in Power* (2007) 等 | 彼得格勒首年追踪与左派社革党联盟从执政到破裂；恐怖升级与粮食危机、暗杀、前线失败交织，而非单线预谋。 | `CLM-rabinowitch-2007-left-sr-coalition-collapse`, `CLM-rabinowitch-2007-contingency-of-dictatorship` | 首都政党政治详尽，偏远地方契卡实践待补。 |
| **制度史与阶段论** | George Leggett, *The Cheka: Lenin's Political Police* (1981); Ilya S. Ratkovsky（及契卡编年史学） | Leggett：契卡从法外 origin 到 GPU 连续体制化；Ratkovsky：1918 夏已有人质与处决规模，9月5日法令是公开化节点而非“零起点”。 | `CLM-leggett-1981-vecheka-extra-legal-origins`, `CLM-leggett-1981-red-terror-institutionalization`, `CLM-leggett-1981-cheka-to-gpu-continuity`, `CLM-cheka-chronicle-hostage-and-local-autonomy`, `CLM-cheka-chronicle-suppression-of-socialist-rivals` | Leggett 偏重中央法令；地方自治与契卡失控需档案对勘。 |
| **1914–1921 总体战治理连续论** | David G. Hoffmann, *Cultivating the Masses: Modern State Practices and Soviet Socialism, 1914–1939* (2011) | 征粮、动员、战备与“培养大众”技术沿袭一战国家实践；苏联社会主义是欧洲现代国家治理谱系的一极，而非凭空乌托邦。 | `CLM-hoffmann-2011-continuum-of-total-war-1914-1929`, `CLM-hoffmann-2011-enlightenment-and-coercion-duality`, `CLM-hoffmann-2011-soviet-socialism-as-european-modernity` | 连续性不等于免除布尔什维克政党特有选择责任。 |
| **内战军事—地理决定论（背景）** | Evan Mawdsley, *The Russian Civil War* (1987) | 红军人口—工业内线优势与白军结构性政策失败解释内战结局；为恐怖与征粮提供战略背景，不单独承担一党制意识形态解释。 | `CLM-mawdsley-1987-civil-war-militarized-regime`, `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` | 军事动员不等于党内反对派清洗因果。 |

## 4. 关联时间线锚点 (共 0 条)
