# 1-Hop 平衡上下文包：`ORG-bund` (崩得（立陶宛、波兰和俄罗斯犹太工人总同盟）)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/organizations/ORG-bund.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `party-split-getzler-haimson, imperial-borderlands-blanc, soviet-nationality-liber, carr-institutional`
- **待补齐视角**: `yiddish-press-circulation-quantitative, women-bund-activists`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `yiddish-press-circulation-quantitative, women-bund-activists`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1897年维尔纽斯成立的帝俄最早群众性犹太工人社会民主党：1898年参与筹备俄社民工党一大，1903年二大因联邦制与“唯一代表权”被拒而退场，客观上促成列宁派组织多数；提出民族文化自治理论，内战后再度分裂，最终并入俄共（布）及波兰社民党与立宪路线。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **维尔纽斯成立与一大筹备（1897–1898）**：`1897-09-25 [O.S.] / 1897-10-07 [N.S.]` 崩得在维尔纽斯（当时属俄罗斯帝国，今立陶宛维尔纽斯）宣布成立，以意第绪语和俄语开展工会、自卫与文化教育工作，成为帝俄犹太人群众性工人组织先导。`1898` 年俄社民工党一大筹备中崩得以独立族自治州形式与会，推动将民族问题写入建党议程（Carr 第一卷 ch.5；见 `CLM-haimson-1955-1903-second-congress-split` 语境）。
- **1903年二大退场与组织后果（1903.08）**：伦敦二大将崩得自治权与“唯一代表犹太无产阶级”条款付表决，崩得以**5:38–41**左右败北后退场，客观上消除部分反对派票源，使列宁派在随后中央机构选举中取得五票多数（`CLM-haimson-1955-1903-second-congress-split`, `CLM-getzler-1967-martov-1903-clause-one`）。马尔托夫虽亦反对崩得联邦制，却与列宁在党员范围论战上分裂；崩得退场被后世认为促成布尔什维克“多数”定型。
- **1905–1917：民族文化自治与护国派光谱（1905–1917）**：崩得参与1905年里加等地苏维埃实验与自卫武装（`CLM-blanc-2021-borderlands-in-1905-and-1917`）；党的领导层（如年甸、利别尔）在1914年后分化为护国与反战；`1917` 年坚持 **民族文化自治**（`культурно-национальная автономия`）——由全俄议会为各民族划出文化基金与学校语文预算——与列宁区域自治及“民族自决”拉开距离。
- **革命、内战与并入布尔什维克（1917–1921）**：二月后崩得在彼得格勒、华沙、基辅苏维埃中派代表；十月后多数反对武装政变而逐步边缘化。`1918–1920` 内战期间一部分崩得成员参加红军、另一部分流亡波兰第二共和国；`1921` 年前后俄共（布）取缔独立派别，崩得组织并入地方党务网络，波兰侧则续存于改组后的波兰社民工党（`CLM-liber-1992-korenizatsiia-paradox-late-1920s` 语境；乌克兰本土化与犹太文教政策张力另参 Liber）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `MTG-1903-rsdlp-2nd-congress` | `walked-out` | 1903.08 | 联邦制与代表权条款败北后退场，改变后续选举算术 | `CLM-haimson-1955-1903-second-congress-split`, `CLM-getzler-1967-martov-1903-clause-one` |
| `PER-martov-l` | `factional-counterpoint` | 1903 | 同列宁联手驱逐崩得，却在党章第一条上与列宁分裂 | `CLM-getzler-1967-martov-1903-clause-one` |
| `PER-lenin` | `organizational-rival` | 1903–1917 | 批判民族文化自治，坚持崩得不得独占犹太工人代表权 | `CLM-lih-2006-erfurtian-merger-formula`, Carr Bolshevik Revolution v.1 |
| `ORG-mensheviks` | `electoral-ally` | 1905–1917 | 在1905里加联邦委员会与1917苏维埃中与孟什维克协同，共享护国派争议 | `CLM-blanc-2021-borderlands-in-1905-and-1917` |
| `ORG-petrograd-soviet` | `faction-in` | 1917.03–1917.10 | 埃尔利希等代表在十月二大随孟什维克退场 | `CLM-sukhanov-1922-october-walkout-tragedy` |
| `POL-korenizatsiia` | `policy-tension` | 1923–1929 | 苏联本土化与意第绪文教资源分配部分回应崩得旧诉求，却排斥自治议会模式 | `CLM-liber-1992-korenizatsiia-paradox-late-1920s` |
| `EVT-1917-02-february-revolution` | `regional-mobilizer` | 1917.02起 | 边疆工人动员网络延续1905自卫传统 | `CLM-blanc-2021-borderlands-in-1905-and-1917` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：崩得是1890年代末俄国最早的大规模犹太工人政党；1903年因民族自治条款退出俄社民工党二大；主张民族文化自治；1917年后作为独立政党迅速解体或被并入共党体系。
- **主要解释分歧**（详参 `DEB-1903-bolshevik-menshevik-split`）：
  - **[组织分裂后果论 / Leopold Haimson, Israel Getzler]** (`CLM-haimson-1955-1903-second-congress-split`, `CLM-getzler-1967-martov-1903-clause-one`)：崩得退场改变二大后半议程投票结构；同时揭示列宁—马尔托夫裂痕与“飞轮—拳头”两党模型对决。
  - **[帝国边疆工人民主经验 / Eric Blanc]** (`CLM-blanc-2021-borderlands-in-1905-and-1917`)：1905年里加等地区崩得—社民联合政府实践表明“工人霸权+拒自由派”在边疆早有根源，1917年崩得护国转向须放回1905后失败后的联盟抉择。
  - **[民族政策比较 / George Liber]** (`CLM-liber-1992-korenizatsiia-paradox-late-1920s`)：苏联 `кorenizatsiya` 在扩大意第绪公共领域同时拒绝崩得式超领土文化自治，制造无法被中央完全消化的民族诉求。
  - **[制度连续论 / E. H. Carr]** (`CLM-carr-1952-nep-retreat-and-commanding-heights` 等_nationality语境_)：崩得并入标志布尔什维克对社会主义少民组织的吞并逻辑，与孟什维克、乌克兰社民党命运同构。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `ORG-mensheviks`
- **时效关系边** (`ORG-bund` → `ORG-mensheviks` | `walkout-catalyst-to-federal-debater` | 有效时段: `1903-1920`): 1903二大因联邦制与唯一代表权遭拒退场客观促成列宁派多数，此后长期活跃于西部犹太工运，内战中左翼分裂并入俄共。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 俄国社会民主主义政党（1903–1924），源于1903年二大马尔托夫等与列宁围绕党章第一条及集中制的决裂，主张开放型群众政党与工人自主活动。1917年分化为策烈铁里、但恩主导的入阁“革命护国派”与马尔托夫领导的反战“国际主义派”；十月后开展苏维埃合法反对派抗争，1921年后遭取缔。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1903-bolshevik-menshevik-split`：《怎么办？》与1903年布尔什维克—孟什维克分裂实质之争
## [T1] 核心问题定义
《怎么办？》中的组织与意识理论是否预示了列宁式精英统治，1903年党内分裂是否由此必然产生？争论涉及文本语境、代表大会的具体冲突与后来派别政治的连续性，不能把它们当成同一个问题。

## [T2] 各学派立场对照矩阵

**经验共识**：《怎么办？》发表于1902年；1903年俄国社会民主工党二大围绕党章第一条、中央机构选举等发生冲突。列宁与马尔托夫都主张有组织的党；“多数派/少数派”的称谓来自特定表决，派系边界和多数并非始终固定。

| 取向与代表著作 | 解释及依据 | 争议与检验 |
| :--- | :--- | :--- |
| 冷战时期组织连续性：Leonard H. Haimson, *The Russian Marxists and the Origins of Bolshevism*；Richard Pipes, *The Russian Revolution* | 强调地下革命知识分子、集中组织与群众之间的紧张，追索革命前组织文化和后来的专断政治之间的联系。 | “精英先锋队密谋论”是对部分传统叙事的概括，不宜把海姆森等不同作者的细致论证视为完全相同；须分别检验其具体主张，不能由后果直接证明1902年有一党专政计划。 |
| 爱尔福特模式再解释：Lars T. Lih, *Lenin Rediscovered: What Is to Be Done? in Context* | 将列宁置于考茨基及德国社民党爱尔福特纲领的社会民主主义语境：有组织的社会主义运动与工人运动结合；强调列宁对工人接受政治教育能力的信心。 | 解释1902年论战不等于证明1903年组织斗争无实质分歧，也不能单凭文本排除后来的威权演变。 |
| 孟什维克视角：Israel Getzler, *Martov: A Political Biography of a Russian Social Democrat* | 从马尔托夫与党内民主、组织成员资格和领导机构冲突出发，追踪孟什维克对列宁集中主义的批评。 | 马尔托夫本人的回忆与论战兼具当事人见证及事后政治辩护属性；应与二大记录及对手文本对读，不能把事后派别身份投回全部代表。 |

## 4. 关联时间线锚点 (共 0 条)
