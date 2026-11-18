# 1-Hop 平衡上下文包：`PER-frunze` (米哈伊尔·伏龙芝)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/people/PER-frunze.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `military-institutional, nationalities-archival-smith, critical-military-social-history`
- **待补齐视角**: `frunze-death-investigation-archival`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `frunze-death-investigation-archival`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
米哈伊尔·伏龙芝（1885–1925），内战红军名将：1919年东线击溃高尔察克，1920年南线攻克弗兰格尔克里米亚；1923年十二大迫斯大林民族政策让步，1924–1925主持军事改革接替托洛茨基，1925年10月手术后猝死。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **革命早年与内战将领（1885–1918）**：生于 `1885-01-21 [O.S.] / 1885-02-02 [N.S.]` 比什凯克（当时俄属中亚）；1904年加入俄国社会民主工党，1905–1907年参与地方武装斗争，多次被捕流放。1917年支持布尔什维克，任莫斯科苏维埃军事委员。**俄国内战**中率东线南集群于 **1919年4–6月** 击败 **高尔察克** 西伯利亚政府，成为卡库林所称1919年铁路战略机动关键指挥官（`CLM-kakurin-1928-red-army-interior-lines-strategy`）。**1920年** 出任 **南方面军** 司令，在 **克里米亚战役** 歼灭 **弗兰格尔** 白军（`CLM-mawdsley-1987-white-movement-structural-defeat` 南线结语）。
- **民族问题与十二大（1923）**：任 **共和国革命军事委员会驻乌克兰全权代表兼乌克兰及克里米亚武装力量司令员、乌克兰人民委员会副主席** 等要职期间，在 **1923年4月十二大** 民族问题特别会议上与拉柯夫斯基联手批判斯大林论纲的行政中央集权倾向，迫使议案写入边疆工业化、民族院否决权与反大俄罗斯沙文主义条款（`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`）。
- **接班托洛茨基与军事改革（1924–1925）**：`1925-01` 接替托洛茨基出任 **陆海军人民委员兼共和国革军委主席**（三驾马车安排）。主持 **伏龙芝军事改革**：正规常备师与领土民兵混合体制、推进党员指挥员“一长制”、整顿政治部与参谋现代化学；亦延续对过分“民主化”军纪的批判（`CLM-smirnov-1920s-territorial-militia-and-combat-training-deficit`；`CLM-smirnov-red-army-commanders-vs-voenspetsy-1920s`）。
- **逝世与后继（1925.10）**：`1925-10-31` 在莫斯科手术后因并发症猝逝（斯大林指派的托洛茨基昔日对手 **伏罗希洛夫** 随后接任革军委主席）。逝世使军界权力再平衡，托洛茨基彻底失去军事杠杆。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `EVT-1918-1920-russian-civil-war` | `commanded-decisively` | 1919–1920 | 东线破高尔察克、南线灭弗兰格尔，为红军1919–20胜利的核心野战指挥官 | `CLM-kakurin-1928-red-army-interior-lines-strategy` |
| `PER-trotsky` | `succeeded-in-rvsr` | 1925.01 | 接掌革军委完成对托洛茨基军权的制度化接替 | `CLM-deutscher-1959-disarmed-prophet-paradox` |
| `PER-stalin` | `alliance-then-succession-politics` | 1923–1925 | 十二大上伏龙芝抨击斯大林民族政策；1925年改革与任命符合三驾马车去托方针 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` |
| `MTG-1923-04-12th-party-congress` | `co-forced-compromise` | 1923-04 | 民族特别会议上代表乌克兰—边疆利益迫斯大林让步 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` |
| `INS-rkka-red-army-and-rvr` | `reformed` | 1924–1925 | 伏龙芝改革标志红军从内战动员军向党国常规军过渡 | `CLM-smirnov-1920s-territorial-militia-and-combat-training-deficit` |
| `POL-korenizatsiia` | `advocated-at-congress` | 1923 | 要求共和国财政权力与边疆工业化写入民族决议 | Smith `pp. 324–325` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：伏龙芝是1919—1920年内战最重要红军统帅之一；1925年初接掌革军委；1923年十二大民族 compromise 有其实名发言记录；1925年10月去世。
- **主要解释分歧**：
  - **[Mawdsley / Kakurin 军事史]**：强调伏龙芝东线胜利与铁路调兵在结构性优势中的战役功能，而非个人英雄孤立解释（`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`、`CLM-kakurin-1928-red-army-interior-lines-strategy`）。
  - **[Jeremy Smith 解密档案派]**：突出伏龙芝作为 **非俄罗斯边疆布尔什维克** 对斯大林民族集中化的制衡，警告勿将十二大读成斯大林单方面胜利（`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`）。
  - **[批判性红军社会史 / Smirnov]**：伏龙芝改革试图恢复命令权威与一长制，却面对八大以来反队列主义遗产与政治课挤压战术训练之矛盾（`CLM-smirnov-1920s-territorial-militia-and-combat-training-deficit`；其对военспецy清洗表述见 `CLM-smirnov-red-army-commanders-vs-voenspetsy-1920s`）。
  - **[托洛茨基系传记 / Deutscher]**：伏龙芝接班是托洛茨基“被解除武装”链条的一环；改革既是专业化也是去托洛茨基化（`CLM-deutscher-1959-disarmed-prophet-paradox`）。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `INS-rkka-red-army-and-rvr`
- **时效关系边** (`PER-frunze` → `INS-rkka-red-army-and-rvr` | `reformer-chairman` | 有效时段: `1924.03-1925.10`): 接替托洛茨基主持1924-1925军事改革，确立正规军与领土民兵混合体制并加强党对指挥系统垄断。
- **节点定性微摘要 [T1]** (完备度 `multi-perspective`): 苏维埃武装中枢：1918年1月15日（公历1月28日）颁令组建志愿红军，3–9月托洛茨基出任陆海军人民委员暨共和国革军委（RVSR）主席，改行普遍义务兵役、征召逾4.8万前沙皇军官（военспецы）与政治委员双签制；1919八大击退军事反对派；1924–1925伏龙芝改革转向正规军与地方民兵混合体制。

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
