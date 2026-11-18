# 1-Hop 平衡上下文包：`POL-korenizatsiia` (本土化政策（Коренизация）)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/policies/POL-korenizatsiia.md`
- **完备度等级**: `multi-perspective`
- **已覆盖视角**: `nationality-compromise-smith, ukrainian-urban-history-liber, debate-1923-archival`
- **待补齐视角**: `caucasus-korenizatsiia-granular, 1930s-reversal-full-study`
- **偏斜风险提示**:
  - ⚠️ 主卡显式声明尚缺以下视角待补: `caucasus-korenizatsiia-granular, 1930s-reversal-full-study`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1923年俄共（布）十二大确立的苏维埃早期民族政策：在党垄断政权前提下推动边疆非俄罗斯地区干部、语言、教育与文化的“本土化”，提升加盟共和国宪法地位；1920年代与工业化、乌克兰化交织，至1928年前后张力外溢。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **制度奠基：十二大民族妥协（1923.04）**：`1923-04-25` 民族问题特别分组会议速记显示，斯大林原提纲遭拉柯夫斯基、伏龙芝及中亚、鞑靼、克里米亚代表围攻；大会决议大幅提升民族院否决权、语言法定地位与边疆工业化承诺，确立 **本土化** 作为多元文化整合机制（`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`）。同一大会后苏丹-加利耶夫案标示民族宽容红线：不得破坏党的组织统一。
- **1920年代实施高峰（1923–1927）**：各加盟共和国推进母语教育、干部按比例任用与语言扫盲；乌克兰等地 **乌克兰化（українізація）** 与农民大规模入城叠加，逆转帝俄时代城市俄罗斯化格局（`CLM-liber-1992-ukrainianization-and-urban-working-class`）。
- **迟1920年代悖论与政治反弹（1927–1929）**：工业化加速催生城乡心理断裂与民族公共领域扩大；赫维廖维、沃洛布耶夫等发出“两种文化/两种经济”警告，斯大林1926年已警惕乌克兰化偏离“全苏联文化”（`CLM-liber-1992-korenizatsiia-paradox-late-1920s`）。1928–1929年征粮危机与反“民族主义”口号升温预示1930年代政策急转，但本卡止于1929年体制张力状态。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `MTG-1923-04-12th-party-congress` | `institutionalized-at` | 1923-04 | 十二大民族问题决议将本土化写入苏联早期民族国家建构基本格局 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` |
| `PER-stalin` | `initial-drafter -> constrained-by-compromise` | 1923 | 起草集中化倾向论纲却在大会上被迫全面让步 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`, `CLM-smith-jeremy-1999-georgian-affair-reassessed` |
| `CON-soviet` | `constitutive-mechanism` | 1923–1929 | 多民族苏维埃联邦通过本土化维持非俄罗斯边疆忠诚与市场整合 | `CLM-liber-1992-korenizatsiia-paradox-late-1920s` |
| `POL-nep` | `coexists-with` | 1923–1929 | 新经济政策期市场化与民族干部扩张并行，1927–1929社会分化加剧语言政治 | `CLM-liber-1992-ukrainianization-and-urban-working-class` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1923年十二大正式确立本土化路线；1920年代多数边疆地区语言、教育与干部政策实质性扩张；政策始终服从党的政治垄断与反分裂红线。
- **主要解释分歧**（详参 `DEB-1923-nationality-and-empire`）：
  - **[解密档案修正派 / Jeremy D. Smith]**（`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`）：驳斥“十二大等于斯大林彻底胜利”的旧说；揭示少数民族代表与乌克兰领导人迫使斯大林退让，塑造1920年代民族权利相对稳固期。
  - **[乌克兰社会史 / George Liber]**（`CLM-liber-1992-korenizatsiia-paradox-late-1920s`, `CLM-liber-1992-ukrainianization-and-urban-working-class`）：本土化在整合城乡乌克兰人、培育乌克兰语工人—知识阶层的同时，制度化语言分裂并孕育难以中央控制的民族自我主张——“悖论”在于成功整合与潜在离心并存。
  - **[苏联正统与大俄罗斯沙文主义批判叙事]**：强调反大俄罗斯沙文主义为十二大政治定调；1930年代逆转则被正统史学解释为必要纠偏，受修正派强烈质疑。
  - **[后苏联民族冲突追溯论]**：将迟1920年代张力视为1932–1933年饥荒与大清洗民族政策的远因——须与1923–1927年实际成果分期，避免目的论倒推（Liber 语境说明已警示）。

## 2. 一跳邻域等权重微摘要 (共 2 个关联节点，严防大卡霸占上下文)
### 邻居节点: `PER-stalin`
- **时效关系边** (`PER-stalin` → `POL-korenizatsiia` | `institutional-compromise` | 有效时段: `1923-1929`): 在1923十二大接纳民族语言与干部本土化以换取边疆精英对党中央政治集权的服从，二十年代末渐因工业化集权与乌克兰民族文化崛起转向猜忌。
- **节点定性微摘要 [T1]** (完备度 `draft`): 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托中央书记处人事任命权纵横政治联盟：先联季-加压制托洛茨基，再联布哈林击溃联合反对派，最终于1928–1929.11击败布哈林集团，终结新经济政策并开启强制集体化与五年计划体制。

### 邻居节点: `MTG-1923-04-12th-party-congress`
- **时效关系边** (`MTG-1923-04-12th-party-congress` → `POL-korenizatsiia` | `institutionalized` | 有效时段: `1923.04`): 十二大民族问题特别会议经拉柯夫斯基、伏龙芝与少数民族代表施压，确立本土化路线与民族院立法保障。
- **节点定性微摘要 [T1]** (完备度 `draft`): 1923年4月17—25日莫斯科举行。列宁病重首次缺席全会，托洛茨基报告“剪刀差”并主张计划化工业化；大会秘密传达列宁民族问题笔记，民族特别会议通过本土化妥协决议，同时维持党的统一垄断。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1923-nationality-and-empire`：布尔什维克民族政策、格鲁吉亚事件与苏维埃“肯定性行动帝国”性质之争
## [T1] 核心问题定义
1922—1923年格鲁吉亚冲突与十二大民族妥协，布尔什维克是在建设多民族“帝国”内的肯定性本土化福利国，还是以先锋队垄断维系的大俄罗斯官僚集权？争论焦点是经验制度成果与各派因果—价值判断之分。

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 列宁晚期斗争论 | Moshe Lewin, *Lenin's Last Struggle* (1968) | 格鲁吉亚事件暴露大国沙文主义与官僚机器合流，列宁晚年誓以政治清算对抗 *dzerzhimordy*；民族问题是撤换斯大林问责的实质切口之一。 | `CLM-lewin-1968-georgian-affair-bureaucracy`; `CLM-lewin-1968-testament-intent` | 易将散落笔记读成连贯“遗嘱计划”；未充分吸纳1990年代解密全会速记。 |
| 自由主义—极权连续论 | Richard Pipes, *Russia under the Bolshevik Regime* 等 | 苏联民族政策是先锋队专政逻辑的延伸；十二大被写作斯大林中央集权对自治的胜利（Smith 正面驳斥此说）。 | （经 `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` 对勘引述） | 档案研究显示十二大民族妥协比“一方全胜”叙事更复杂。 |
| 解密档案民族妥协论 | Jeremy D. Smith, *The Bolsheviks and the National Question, 1917–1923* (1999) | 列宁—斯大林在集权原则上确有共识，但十二大特别会议显示边疆代表迫使中央退让，奠定1920年代本土化相对稳固期；格鲁吉亚危机不宜简化为二人生死对决。 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`; `CLM-smith-jeremy-1999-georgian-affair-reassessed` | 本土化繁荣期止于1930年代逆转，分期须清晰。 |
| 帝国史学框架 | Ronald Grigor Suny, *The Red Flag Unfurled* (2017) 等 | 沙俄—苏联宜在“宗主—边缘不平等从属”的帝国框架下理解民族建构；1991年后“苏联=帝国”共识含事后归因风险。 | `CLM-suny-2017-empire-and-nationality-dimension` | 帝国理论有助于宏观定位，但不能替代全代会速记级制度考证。 |
| 乌克兰社会史与本土化悖论 | George Liber, *Soviet Nationality Policy, Urban Growth, and Identity Change in the Ukrainian SSR 1923–1934* (1992) | 本土化整合城乡乌克兰人、扩张乌克兰语公共领域的同时，制度化语言分裂并孕育难以中央完全消化的地方民族诉求。 | `CLM-liber-1992-korenizatsiia-paradox-late-1920s`; `CLM-liber-1992-ukrainianization-and-urban-working-class` | 侧重乌克兰案例，外高加索与中亚须分区域检验。 |
| “肯定性行动帝国”概念（史学界常用语） | Terry Martin, *The Affirmative Action Empire* (2001) 等 | 1920年代苏联对“前发达”民族实施制度化优待（干部、语言、教育配额），以党国垄断为前提整合帝国边缘——成功与潜在离心并存。 | （本库待补 `CLM-martin-2001-affirmative-action-empire`；可 interim 参照 `reading-notes/` 与 `POL-korenizatsiia`） | 术语易与美式种族平权政策混同，须严守苏联党国语境。 |

## 4. 关联时间线锚点 (共 0 条)
