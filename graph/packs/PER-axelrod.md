# 1-Hop 平衡上下文包：`PER-axelrod` (帕维尔·阿克雪里罗得)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/people/PER-axelrod.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `consciousness-history-haimson, menshevik-biographical-getzler, intellectual-history-walicki`
- **待补齐视角**: `full-ascher-biography-systematic, post-soviet-archival-personal`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `full-ascher-biography-systematic, post-soviet-archival-personal`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
帕维尔·阿克雪里罗得（约1850–1928），俄国马克思主义与孟什维克思想奠基人之一。早年投身民粹活动并经由基辅巴枯宁派转入土地平分社，1883年参与创立劳动解放社，1903年二大与马尔托夫共同批判列宁超集中制；晚年提出“工人代表大会”构想，成为孟什维克群众工人政党路线的理论象征。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **民粹青年期与基辅巴枯宁派转向（1870s–1882）**：生于犹太家庭（通行传记生年作1850年8月25日前后，具体日序及俄/公历归属待 Ascher 传记或名册核实），早年投身“到民间去”潮流，曾接触 **尼·瓦·柴可夫斯基** 小组网络（成员身份未获 Ascher 逐页核实前暂记为接触），主要实践重心在基辅巴枯宁派；1879年分裂后参与 **土地平分社（Чёрный передел）** 路线，反对刺杀沙皇的集中恐怖，主张村社土地重分（`ORG-chernyi-peredel`, Venturi; Walicki pp. 107, 188–189）。
- **劳动解放社与俄国马克思主义播火（1883–1903）**：`1883-09-25 [N.S., 日内瓦]` 与普列汉诺夫、查苏利奇、捷伊奇、伊格纳托夫创立 **劳动解放社（Освобождение труда）** ，以阶段论批判民粹公社空想，向俄国内输送马克思主义文献（`ORG-osvobozhdenie-truda`, `CLM-walicki-1969-marx-populist-affinity`）。查苏利奇 `1881-02-16 [N.S.]` 日内瓦致信马克思询问村社问题、马克思 `1881-03-08 [N.S.]` 复信肯定公社潜在支点（发出稿至1924年方公布，且须与四份未定草稿区分），反映当时小组仍处民粹—马克思主义交叉带。
- **1903年分裂与“自主活动”理论（1903–1905）**：二大上支持马尔托夫党章第一条，遭列宁以微弱多数改组中央机构与《火星报》编委后，在新《火星报》上揭出 **工人阶级自主活动（`самодеятельность`）** 与知识分子密谋监护之间的结构性矛盾（`CLM-haimson-1955-1903-second-congress-split`, `CLM-getzler-1967-martov-1903-clause-one`）。Haimson 将此举视为意识—自发性世界观分裂的首次理论自觉。
- **“工人代表大会”构想与晚年国际主义（1905–1928）**：1905年革命前后力倡以 **全俄工人代表大会** 整合阶级组织、推动革命民主自治，影响孟什维克广泛工人政党战术及后来策烈铁里一派苏维埃策略（Service *Lenin* 译注；Haimson 1987 访谈文献）。一战参加齐美尔瓦尔德和平运动；1917年后留在国外，与马尔托夫共同维系孟什维克国际主义批判；`1928-04-16 [N.S.]` 病逝柏林。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-osvobozhdenie-truda` | `co-founder` | 1883–1903 | 俄国首个马克思主义团体的共同创办人之一 | `ORG-osvobozhdenie-truda`, Walicki |
| `ORG-chernyi-peredel` | `member-precursor` | 1879–1881 | 土地平分社核心成员，反恐怖民粹路线代表 | `ORG-chernyi-peredel` |
| `ORG-mensheviks` | `intellectual-father-figure` | 1903–1928 | 与马尔托夫并列奠定孟什维克群众党与工人自主活动伦理 | `ORG-mensheviks`, `CLM-haimson-1955-1903-second-congress-split` |
| `PER-martov-l` | `lifelong-ally` | 1890s–1923 | 1903年党章之争与编委会危机中的主要政治—理论同盟 | `CLM-getzler-1967-martov-1903-clause-one` |
| `PER-plekhanov` | `co-founder -> divergent` | 1883–1903 | 共同创建劳动解放社，1903年底普列汉诺夫短暂倒向列宁致阿克雪里罗得疏离 | `CLM-haimson-1955-consciousness-spontaneity` |
| `PER-lenin` | `factional-rival` | 1903–1928 | 二大起终生论敌，阿克雪里罗得诠释列宁先锋队观为知识分子对工人监护的工具论 | `CLM-haimson-1955-lenin-what-is-to-be-done`, `DEB-1903-bolshevik-menshevik-split` |
| `PER-herzen` | `intellectual-continuity` | 1860s–1883 | 从赫尔岑—民粹人道传统走向普列汉诺夫马克思主义，Walicki 强调观念系谱连续性 | `CLM-walicki-1969-narodnichestvo-definition` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：阿克雪里罗得是1883年劳动解放社创始人、1903年孟什维克分裂关键人物、孟什维克“工人代表大会”思想的重要提案者；一生坚守西欧式群众工人政党与反密谋专政立场。
- **主要解释分歧**：
  - **[意识与自发性思想史 / Leopold Haimson]**（`CLM-haimson-1955-consciousness-spontaneity`, `CLM-haimson-1955-1903-second-congress-split`, `CLM-haimson-1955-lenin-what-is-to-be-done`）：将阿克雪里罗得置于俄国马克思主义理解无产阶级意识如何生成的长时段辩论中——他相信意识在政治自由与阶级斗争自我活动中成熟，从而抗拒列宁式自觉注入与纪律机器。
  - **[政治传记实证 / Israel Getzler]**（`CLM-getzler-1967-martov-1903-clause-one`）：通过马尔托夫传记精细还原二大党章措辞之争，证明阿克雪里罗得—马尔托夫心目的是类似崩得嵌入群众的开放性工人党，而非抽象议会多元主义。
  - **[观念史与民粹—马克思主义综合 / Andrzej Walicki]**（`CLM-walicki-1969-marx-populist-affinity`, `CLM-walicki-1969-narodnichestvo-definition`）：强调从土地平分社到劳动解放社的系谱中，阿克雪里罗得参与完成“民粹人道主义—马克思资本主义必然论”的艰难综合；1881年马克思—查苏利奇通信反讽地预兆了后来普列汉诺夫路线的转折。
  - **[孟什维克实践政治史]**：1917年策烈铁里苏维埃策略可溯至阿克雪里罗得工人代表大会方案（Basil 1984; Haimson 1987 Dan interviews）——但1917年孟什维克丧失工人多数之责不能单独归咎于其个人，须与 Galili/Getzler 对护国派路线的社会史分析并读。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `ORG-osvobozhdenie-truda`
- **时效关系边** (`PER-axelrod` → `ORG-osvobozhdenie-truda` | `co-founder` | 有效时段: `1883-1903`): 历经柴可夫斯基小组与土地平分社后与普列汉诺夫共建劳动解放社，1903后成为孟什维克“工人自主活动”理念教父。
- **节点定性微摘要 [T1]** (完备度 `draft`): `1883-09-25 [N.S.]` 于日内瓦创立的俄国首个马克思主义革命团体，由普列汉诺夫、阿克雪里罗得、查苏利奇、捷伊奇与瓦西里·伊格纳托夫创立。以唯物史观与阶段论批判民粹派，向俄国内输送理论著作；1903年俄国社民工党二大闭幕后正式宣告解散并将职能移交统一政党。

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

## 4. 关联时间线锚点 (共 1 条)
- **1903-08-07 [O.S.] / 1903-08-20 [N.S.]** (`TL-W21-1903-08-20-01`, L3): **《火星报》编委会六人缩为三人** — 25比2比20通过；普列汉诺夫支持列宁淘汰三老编委，马尔托夫拒任。
