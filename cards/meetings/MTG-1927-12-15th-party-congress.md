---
id: MTG-1927-12-15th-party-congress
type: meeting
title: 联共（布）第十五次代表大会
names:
  ru: XV съезд ВКП(б)
  en: Fifteenth Congress of the All-Union Communist Party (Bolsheviks)
  aliases: ["十五大", "集体化代表大会"]
dates:
  start_ns: "1927-12-02"
  end_ns: "1927-12-19"
coverage_status: multi-perspective
perspectives_present: ["trotskyist-biographical-deutscher", "archival-post-soviet-khlevniuk", "economic-foundations-carr-davies"]
perspectives_missing: ["rural-social-history", "delegate-social-history"]
related_debates: ["DEB-1928-bukharin-alternative", "DEB-1929-collectivization-and-dekulakization-causes", "DEB-1924-socialism-in-one-country"]
updated_at: "2026-11-18"
---

## [T1] 60秒定性微摘要
1927年12月2—19日莫斯科举行。大会追认11月对托洛茨基、季诺维也夫的开除党籍处分，并于12月18日另行开除加米涅夫等75名托季联合反对派骨干及萨普罗诺夫派；同时通过编制首个五年计划指示与渐进合作化—集体化决议，开启NEP末期转折前奏。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **会前开除与大会分批组织清洗的严格区分（1927.11.14 vs 1927.12.18）**：托洛茨基与季诺维也夫已于会前 `1927-11-14` 被中央委员会与中央监察委员会联席会议直接开除出党（此前 `1927-10-23` 被逐出中央委员会）。`1927-12-02` 十五大开幕时反对派已无正式表决权代表；`1927-12-03` 斯大林作中央政治报告，加米涅夫、拉柯夫斯基等发言遭全场打断；`1927-12-18` 大会正式追认对托、季二人的开除，并**另行宣布开除包括加米涅夫、皮达可夫、拉狄克、拉柯夫斯基、普列奥布拉任斯基在内的75名联合反对派积极分子**，同时开除萨普罗诺夫“民主集中派”（十月集团）23人名单（**严禁将大会开除的“75人”误计为包含会前已被开除的托、季二人在内的总数**；`CLM-deutscher-1959-united-opposition-defeat`）。
- **反对派阵营分裂与“六个月考察期”悔过处置（1927.12.10–19）**：`1927-12-10` 托派与季派因是否声明放弃宣传反对派观点正式破裂；`1927-12-18—19` 季诺维也夫、加米涅夫等提交放弃派别活动并承认违反党纪的悔过声明，但 `1927-12-19` 闭幕大会拒绝立即集体恢复其党籍，规定须以个人身份单独申请并经至少六个月考察；托洛茨基、拉柯夫斯基等拒绝投降，于1928年1月遭流放（`CLM-deutscher-1959-united-opposition-defeat`）。
- **五年计划编制指示、自愿集体化口径与粮食危机潜流（1927.12）**：大会通过李可夫、克尔日扎诺夫斯基主持的**关于编制国民经济第一个五年计划的指示**（系编制原则而非1929年4月最终批准的最高方案），并通过莫洛托夫农村工作报告，提出逐步扩大集体农庄与国营农场、限制富农剥削，但明文仍保留NEP市场交换与自愿入社原则——**不可目的论地混同于1929年底全盘强制集体化与“消灭富农阶级”**。与此同时，大会开会期间（`1927-12-14` 与 `12-24`）中央已两度向产粮区发出催征粮食紧急指示，预示 `1928-01` 非常措施与斯大林—布哈林决裂迫在眉睫。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-left-and-united-opposition` | `liquidated-at` | 1927-12-18 | 大会开除75名骨干并促发季—托两翼分裂，联合反对派作为党内有组织联盟终结 | `CLM-deutscher-1959-united-opposition-defeat`; `ORG-left-and-united-opposition` |
| `PER-trotsky` | `expulsion-ratified` | 1927-11-14开除；12-18追认 | 会前已被开除党籍，十五大予以追认并拒绝妥协，次年1月流放阿拉木图 | `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-zinoviev` | `expulsion-ratified -> recantation` | 1927-11至12-19 | 会前开除，大会闭幕际与加米涅夫提交悔过书，被勒令经六个月考察再个别审理 | `CLM-deutscher-1959-united-opposition-defeat`; ` Zhukov ch21` |
| `PER-kamenev` | `expelled -> recantation` | 1927-12-18至12-19 | 列入大会开除的75人名单，随即联署悔过声明与托洛茨基派决裂 | `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-stalin` | `leader` | 1927-12 | 主导彻底清除左翼反对派，会后一中全会以口头请辞总书记试探并强化政治局核心顺从 | `CLM-khlevniuk-2015-collective-leadership-erosion` |
| `POL-first-five-year-plan` | `directives-adopted-at` | 1927-12 | 大会通过编制首个五年计划的框架性指示，尚带工农平衡约束而非1929年高指标定稿 | `POL-first-five-year-plan`; `DEB-1928-bukharin-alternative` |
| `POL-nep` | `policy-context` | 1927-12 | 表面重申NEP框内渐进合作化，实则同期秋冬季粮食收购危机已在掏空市场交换基础 | `DEB-1928-bukharin-alternative`; `DEB-1929-collectivization-and-dekulakization-causes` |

### 2.3 史学争鸣光谱
- **经验共识**：大会追认开除托洛茨基与季诺维也夫、另行开除75名托季反对派及萨普罗诺夫集团，通过编制一五计划指示及渐进农业合作化/集体化决议。
- **主要解释分歧**（详参 `DEB-1928-bukharin-alternative`, `DEB-1929-collectivization-and-dekulakization-causes`）：
  - **[传记与社会气氛论 / Isaac Deutscher]**（`CLM-deutscher-1959-united-opposition-defeat`）：指出十五大对反对派的粉碎不仅靠代表遴选机器，更根源于革命疲惫下全国工农的“可怕寂静”与反对派自我束缚于一党纪律之内。
  - **[后苏联政治局制度史 / Oleg Khlevniuk]**（`CLM-khlevniuk-2015-collective-leadership-erosion`）：强调1927年12月清除左翼后，斯大林在 `1927-12-19` 新选中央一中全会上以“列宁遗嘱任务已履行、请求免去总书记”作试探获布哈林、李可夫一致挽留，但政治局寡头共治要到1928—1929年击溃右派后才最终瓦解。
  - **[计划经济与农村史分期论 / Carr & Davies; Cohen]**（`CLM-carr-davies-1969-nemchinov-table-critique`, `CLM-cohen-1973-nep-viability`）：反对苏联教科书将十五大直接等同于“全盘集体化代表大会”，强调十五大文本仍规定农业集体化须建立在自愿与机器物质技术基础之上，与1929年底行政强推存在重大政策断裂。

## [T3] 深度考证、分期细目与原文引证档案
- **本库已核 A 级支撑与时间线锚点**（替代低可信预览摘编）：
  - `CLM-deutscher-1959-united-opposition-defeat`（Deutscher *The Prophet Unarmed*, `ch05`：1927年11月开除 vs 12月十五大开除75人与季、加投降分化）。
  - `CLM-khlevniuk-2015-collective-leadership-erosion`（Khlevniuk *Stalin*, `pp. 92–98`：十五大组织胜利与会后全会请辞博弈）。
  - 逐日系年交叉核对见 `timeline/L3_daily/1927-10_tenth_anniversary_and_15th_congress.md`（`1927-11-14` 联席会议开除托、季；`1927-12-02—19` 十五大议程、`12-18` 开除75人＋萨普罗诺夫派、`12-19` 六个月考察决议）。
- **Deutscher 原文直引（大会场外社会沉寂）**：
  > “但是这场重大的争论却是在一片可怕的寂静中发生的。双方都只有一小部分人卷入争论。整个国家都是沉默的。” `[deutscher_1959_prophet_unarmed_zh, via CLM-deutscher-1959-united-opposition-defeat]`
- **一手文献与待核标记 [S级]**：斯大林十五大中央政治报告与《关于农村工作》《关于编制国民经济五年计划的指示》决议（英译本附有后出官方党史编者注，须剥离“早已预见全盘集体化”的事后粉饰）；1928年版俄文《XV съезд ВКП(б). Стенографический отчет》中75人与萨普罗诺夫派完整名单页码、以及 `1927-12-18` 季诺维也夫—加米涅夫声明原文页码待补 S 级核定。
