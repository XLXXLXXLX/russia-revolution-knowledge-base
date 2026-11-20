---
id: POL-war-communism
type: policy
title: 战时共产主义
names:
  ru: Военный коммунизм
  en: War Communism
  aliases: ["战时共产", "军事共产主义"]
dates:
  start_ns: "1918-06-01"
  end_ns: "1921-03-21"
coverage_status: multi-perspective
perspectives_present: ["emergency-civil-war", "ideological-continuity", "institutional-carr", "revisionist-social-history"]
perspectives_missing: ["regional-implementation-granular", "full-primary-decree-corpora"]
related_debates: ["DEB-1918-war-communism-ideology-or-emergency"]
updated_at: "2026-11-19"
---

## [T1] 60秒定性微摘要
1918年夏至1921年3月苏维埃经济政策总称：余粮收集制、中小工业国有化、取缔私商、货币贬值与实物配给并举；因内战饥荒与国家能力崩溃而强化，却在1921年喀琅施塔得与坦波夫危机下为新经济政策实物税所取代；其性质是应急、乌托邦跃进还是国家统制传统延续，史家分歧剧烈。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **危机叠加与措施集群化（1918.06–1919）**：`1918-05-09 [N.S.]`（苏俄已于1918-02-14改行公历，全俄中执委通过赋予粮食人民委员部非常权力的 **粮食专政／粮食垄断令** 雏形；部分史书按签署/刊布记 `1918-05-13 [N.S.]`），夏秋颁布征收办法，**1919年初** 形成制度化 **余粮收集制（продразвёрстка）**，由国家按定量强征农村“余粮”供应红军与城市（地方执行差异极大）。同期 **大中小企业普遍国有化**、取消大部分私营贸易、废止按劳取酬的多元工资形态，代之以 **实物配给、无偿征用与劳动军事化** 命令；货币急剧贬值使“无货币”经济表面化，但黑市一直存在。
- **内战高峰与“战时共产主义”名目（1919–1920）**：红军以阶级战争形态扩大，交通、燃料与冶金由国家单一调配；托洛茨基推动 **劳动军** 与 **一长制** 强化工厂纪律；苏维埃政权在乡村呈“军事—行政”外在于农民之态（Mawdsley 引坦波夫密报，`CLM-mawdsley-1987-civil-war-militarized-regime`）。史家后称此期为 **战时共产主义（Военный коммунизм）**，但当时布尔什维克亦用“共产主义的仓促实践”“过渡模式”等多种表述，并无唯一法令界定起讫。
- **农民战争、喀琅施塔得与退却（1921.02–03）**：坦波夫等地农民武装反抗征粮；`1921-03-02` **喀琅施塔得起义** 呼唤“没有共产党人的苏维埃”；列宁在俄共十大承认农民战争威胁超过白军（Figes, `CLM-figes-1996-peasant-wars-and-nep-retreat`）。`1921-03-15`–16 **十大** 通过以 **粮食税** 取代余粮收集制、恢复有限贸易的决定框架；`1921-03-21` 人民委员会颁布 **关于以实物税取代征收制** 法令，标志向新经济政策转型的法律节点（详参 `POL-nep`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `POL-nep` | `replaced-by` | 1921-03–12 | 实物税与贸易恢复逐步 dismantle 余粮收集制与全面国有化贯彻强度 | `CLM-figes-1996-peasant-wars-and-nep-retreat` |
| `EVT-1921-kronstadt` | `precipitated-retreat` | 1921-03 | 起义与农村战争共振，促使列宁在十大宣布新经济政策退却 | `DEB-1918-war-communism-ideology-or-emergency` |
| `ORG-workers-opposition` | `simultaneous-crisis-of` | 1920–1921 | 城市工人反对一长制与官僚化，与战时共产主义劳动军事化同场争论 | `CLM-daniels-1960-tenth-congress-turning-point` |
| `POL-ban-on-factions-1921` | `institutionalizes-post-crisis` | 1921-03-16起 | 十大在喀琅施塔得背景下通过派别禁令，经济退却与党组织封闭并行 | `CLM-mawdsley-1987-civil-war-militarized-regime` |
| `PER-trotsky` | `militarized-labor-architect` | 1918–1921 | 劳动军、交通工会军事化与工会国家化主张，代表战时共产主义劳动纪律极点 | Daniels (1960), Service (2009) |
| `ORG-cheka-ogpu` | `enforces-requisition` | 1918–1921 | 契卡/格乌系统镇压拒征与投机，红色恐怖与征粮相互嵌合 | `CLM-pipes-1990-red-terror-leninist-logic`, `CLM-leggett-1981-red-terror-institutionalization` |
| `PER-lenin` | `debated-then-retreated` | 1918–1921 | 先是强调国家资本主义过渡可能，后在危机中批准激进措施；1921年主动宣布退却 | Carr; Lih 批判“乌托邦计划”叙事 |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1918–1921年苏联经历强制征粮、广泛国有化、市场压制与实物配给；1921年3月后粮食税与新经济政策标志着部分核心措施的撤回；政策名称“战时共产主义”为史家归纳，各措施出台时间与地区强度并不整齐划一。
- **主要解释分歧**（详参 `DEB-1918-war-communism-ideology-or-emergency`）：
  - **[内战军事求生应急论 / Evan Mawdsley, Sheila Fitzpatrick 部分论述]** (`CLM-mawdsley-1987-civil-war-militarized-regime`, `CLM-mawdsley-1987-sovdepia-heartland-advantage`): 强调经济崩溃、补给断裂与红军生存需要如何把政权锁进军事—行政形态；Mawdsley 明确指出内战与斯大林主义同为夺权后果，但拒绝“没有内战就不会有斯大林主义”的简单反事实，亦承认内战方法在1920年代末被选择性复活。
  - **[意识形态乌托邦跃进论 / Richard Pipes, Martin Malia]** (`CLM-pipes-1990-red-terror-leninist-logic`; Malia, *The Soviet Tragedy*, 见 `DEB-1918-war-communism-ideology-or-emergency`): 将余粮收集制、恐怖与废法统治解释为布尔什维克反市场社会主义与先锋队权力观的先定展开，而非纯粹外生战争产物；Pipes 尤其强调1917年末契卡与废法的开端早于大规模内战。Malia 从“乌托邦悲剧”长时段论证，危机为激进蓝图扫清障碍——须注意其与 Pipes 论证焦点并不相同，不能合并为单一时间表。
  - **[战时国家统制连续论 / E. H. Carr, Lars T. Lih]** (Carr, *The Bolshevik Revolution*; Lih, “Bukharin’s Illusion”及列宁再发现系列，`CLM-lih-2006-textbook-myth-critique`): Carr 追踪1918–1921年法令序列与国家机构如何在压力下“非计划地”相互牵引，反对把战时共产主义说成列宁事先写定的乌托邦总蓝图；Lih 批判把新经济政策简单定义为对“乌托邦式战时共产主义”的醒悟，强调布尔什维克始终谈“过渡”与俄国落后现实，战时措施应回到当时用语与选项集理解，而非套用后设的“共产主义试验”标签。
  - **[修正派社会史 / Moshe Lewin, S. A. Smith]** (`BIB-021`, `CLM-smith-1983-post-october-centralization`): 从农民抗征、工人车间监督退化与中心城市饥饿出发，论证物质崩溃与阶级结构变动如何迫使政权选择更极端的汲取与监督手段；与纯粹意识形态决定论构成经验性制衡。

## [T3] 深度考证、分期细目与原文引证档案

### 3.1 核心制度组件对照（1918–1921）
| 组件 | 典型措施 | 经验性转折 |
| :--- | :--- | :--- |
| 农村汲取 | 余粮收集制（1919起强化） | 1921年3月改为粮食税，农民可出售税后余粮 |
| 工业与贸易 | 大中小企业国有化、私营贸易取缔、中央分配 | 1921年起租让制与小工业局部恢复（新经济政策） |
| 劳动与分配 | 实物配给、劳动义务、军事化劳动、废除计件工资 | 1921–1922年逐步恢复工资与有限罢工通道 |
| 政治强制 | 契卡征粮护法、红色恐怖、一党垄断巩固 | 恐怖机构未随新经济政策废除（与 `ORG-cheka-ogpu` 分读） |

### 3.2 论断卡与专著锚点
- **应急—军事政权形态**（`CLM-mawdsley-1987-civil-war-militarized-regime`）：
  > "the 'Military-Administrative character of the Soviet Regime'; 'the peasantry, in their majority, have become accustomed to regarding the Soviet regime as something extraneous to themselves, something that issues only commands'." `[p. 328]`
- **意识形态—恐怖内生论（比较用）**（`CLM-pipes-1990-red-terror-leninist-logic`）：恐怖作为缺乏民意的 **surrogate for popular support**，与征粮行政强制同属废法专政逻辑——该命题解释力较强，但时间线覆盖1917末，不能单独充当每一征粮条例的因果证明。
- **农民战争与新经济政策退却链**（`CLM-figes-1996-peasant-wars-and-nep-retreat`）：坦波夫起义“恢复1917–18村级自治”口号与实物税决策的关联。
- **1921年十大组织—经济并列转折**（`CLM-daniels-1960-tenth-congress-turning-point`）：经济退却与派别禁令同一会议周期完成。
- **工资形态社会史**（`CLM-ilyukhov-war-communism-leveling-vs-nep-piecework`）：战时共产主义平均化薪酬与新经济政策计件复兴的对照。

### 3.3 本地文献与待归档案
- `sources/monographs/mawdsley_1987_civil_war/`（`CLM-mawdsley-1987-civil-war-militarized-regime`）；
- `sources/monographs/carr_bolshevik_rev/`（战时共产法令年表卷，待专案 toc 切片）；
- `sources/monographs/pipes_1990_russian_rev/`（`CLM-pipes-1990-red-terror-leninist-logic`）；
- `sources/monographs/lih_2006_lenin_rediscovered/`（战时共产主义—新经济政策语义辩论，见 ch27 书目引 Lih 2000 文）；
- `reading-notes/daniels_1960_conscience/RN-W1C-communist-oppositions-1918-1929.md`（1920–1921危机与十大工会争论语境）。
- **S级待核**：1918–1919征粮法令、`1921-03-21` 实物税法令及地方执行统计；严禁凭记忆编造页码直引。

### 3.4 分期边界说明
frontmatter `1918-06-01`–`1921-03-21` 为机器检索包络：起点取粮食国家垄断政策集群化，终点取实物税法令颁布日；个别国有化法令可追溯至1917年底，全面转型亦延续至1921年下半年。叙事在1918-02-14改历后统一采用 **公历**（仅溯及改历前法令时并列双历），地方执行差异单独考证，不可把史家战后命名当作当时当事人统一自称。