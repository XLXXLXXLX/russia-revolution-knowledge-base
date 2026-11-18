# AUD-15B｜第32—33波 Codex 编纂人物/组织/机构卡异源交叉审计报告（7张）

- **审计日期**：2026-11-18
- **审计角色**：`dialectic-auditor`（异源交叉审计：Anthropic Claude 审读 OpenAI `codex/gpt-6.1-terra` 撰写的 7 张卡）。
- **唯一写入目标**：[`audits/AUD-15B-wave32-33-codex-org-ins-cards-audit.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-15B-wave32-33-codex-org-ins-cards-audit.md)；本轮纯只读，未修改任何被审卡片、札记、时间线或共享总表。
- **审计对象（分两阶段落盘）**：
  - **阶段一（01–04）**：[`PER-strumilin`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-strumilin.md)、[`ORG-bolsheviks-rcpb-vkpb`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-bolsheviks-rcpb-vkpb.md)、[`ORG-octobrists-and-progressive-bloc`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-octobrists-and-progressive-bloc.md)、[`ORG-democratic-centralists`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-democratic-centralists.md)
  - **阶段二（05–07）**：见本文件后半（追加）

---

## 一、审计方法与判级准则

1. **方法**：逐行审读 YAML 与 `[T1]/[T2]/[T3]`；对全库 `.md` 做 ID 存在性扫描（`PER|ORG|INS|POL|EVT|CLM|DEB|CON|MTG|RN-*`）；用关键词对 `reading-notes/`、`historiography/claims/`、`timeline/L1–L3`、`sources/web-archive/`、`sources/monographs/` 反查站内已有 S/A 级材料；对卡内外链做可达性检测。
2. **双历法与发生地规则**（`AGENTS.md` §2.5）：19 世纪 `+12`；1900-03-01 至 1918-01-31 俄国本土 `+13`；西欧会场/流亡事件单公历 `[N.S.]`；1918-02-14 后本土纯公历。
3. **判级**：**P0** = 史实/历法/断链/失效外链硬伤，或卡内引证与被引文本不符；**P1** = 站内 S/A 漏引、口径/任期/统计分母失准、学派失衡、`coverage_status`/`perspectives_*` 标签与实际不符；**P2** = Schema 规范（T1 字数、`dates`、边表列用法）与悬空尾句。

> **断链扫描总结果（7 张卡全部 ID）**：全库仅 **1 处悬空 ID**——`ORG-octobrists-and-progressive-bloc` 的 `related_debates` 中的 `DEB-1914-haimson-thesis-stability-or-crisis`（实际文件名为 `DEB-1914-haimson-thesis-stability`）。其余 `PER/ORG/INS/POL/EVT/CLM/DEB/CON/RN` 引用（含 T3 的 `RN-*` 与 `CLM-*`）均能解析到真实文件。

---

## 二、历法与 YAML `dates` 复核表（前半批 01–04）

| 卡 | YAML `dates` | 卡内日期验算 | 站内/一手对照 | 判定 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-strumilin` | `start_ns: "1877-01-29"`、`end_ns: "1974-01-25"`（ISO 合规） | `1877-01-17 [O.S.] / 01-29 [N.S.]`：19 世纪 `+12`，**正确**；T3 自带“仍须核对历法标注”的保留 | 卒日 1974-01-25 属苏联期纯公历，无需双标；RAS 外链 `ras.ru/nappelbaum/…` 实测 **HTTP 200**，可达 | **日期合规**；仅出生地“波多利亚省”无逐字核验（P2） |
| `ORG-bolsheviks-rcpb-vkpb` | `start_ns: "1903-08-21"`（注释未标历法）；`end_ns: "1929-12-31"`（观察截点，已声明） | 正文无日级日期；`1918年3月七大`“更名”、`1925年十四大`均无日但无误 | 二大在布鲁塞尔→伦敦举行，**应单公历 `[N.S.]`**；[`L3 1903-07`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1903-07_rsdlp_second_congress_split.md#L76-L86) 记编委会/中央机构选举窗口为 **`1903-08-07 [O.S.] / 1903-08-20 [N.S.]`**，闭幕 `08-23 [N.S.]`，**库内没有 `08-21` 这一节点** | `08-21` 与库内 L3 差 1 天且无标注 → **P2**（见 2 号卡） |
| `ORG-octobrists-and-progressive-bloc` | `start_ns: "1905-10-30"`、`end_ns: "1917-12-31"` | `1905-10-17 [O.S.] / 10-30`（+13）✓；`1907-06-03 [O.S.] / 06-16`（+13）✓；`1917-02-27 [O.S.] / 03-12`（+13）✓ | 与 `WEB-1905-10-17-october-manifesto` 的 `written_date_ns: 1905-10-30` 一致；“1915年8月”“1911年”**无日级、无历法**，而 L1 [`TL-W15-L1-E05-05`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L1_milestones/1861-1929_backbone.md#L81) 记 **`1915-08-25 [O.S.] / 1915-09-07 [N.S.]` 进步同盟纲领公布** | 历法换算无误；进步同盟月份易被读成公历 8 月 → **P2**；相关辩题 ID **悬空** → **P0** |
| `ORG-democratic-centralists` | `start_ns: "1919-01-01"`、`end_ns: "1927-12-31"`（均为近似注释） | `1923-10-15 [N.S.]`（苏俄改历后纯公历）✓，与 `WEB-1923-10-15-declaration-of-the-forty-six.written_date_ns` 一致 | 十五大开除：[`L3 1927-10`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1927-10_tenth_anniversary_and_15th_congress.md#L127) 记 `1927-12-18 [N.S.]`；卡内“逐人核对”过于保守 | 历法合规；**“十五大开除”日期库内已有**（P1 漏引） |

---

## 三、前半批逐卡审计与修复方案（01–04）

### 01. `PER-strumilin`（斯特鲁米林）

**总判**：事实表述克制、对“目的论/发生论”标签的限定良好，无硬性史实错误；主要问题是**把站内已有的 S/A 级专章当成“本地未找到”**，且存在尾部悬空句与身份描述待核。

- **P0**：无。（生卒历法 ✓；外链 200 ✓；`related_debates: DEB-1928-bukharin-alternative` 真实存在；2.2 边表 5 个节点 ID 全部可解析。）
- **P1**
  1. **“未在本地找到可靠逐字原文与语境”与库内事实不符（`L28`、`L47`）**：库内已有对“计划即规律”的**二手转述链**——[`RN-W36-bukharin-preobrazhensky-equilibrium-debate-zh.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/bukharin_preobrazhensky_debate_zh/RN-W36-bukharin-preobrazhensky-equilibrium-debate-zh.md#L94)（斯特鲁米林“计划即规律”论）与 [`CLM-bukharin-preobrazhensky-equilibrium-vs-accumulation-zh.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-bukharin-preobrazhensky-equilibrium-vs-accumulation-zh.md#L10)（其 `targets_cards` **已含 `PER-strumilin`**，L30 把“计划即规律”并入斯大林体制的理论来源）。本卡未回链该 CLM，造成“被指向却不回指”的单向图谱。建议：T3 改为“**本地仅有中文二手转述（刘伟、平新乔 1989 经 `CLM-bukharin-preobrazhensky-…` 转引），无逐字原文**”，并把该 CLM 加入 2.2 边表（`PER-preobrazhensky`/`CON-primitive-socialist-accumulation` 关系）。
  2. **漏引 Daniels 对“发生派对目的派”二分的修正**：[`RN-W1C` L89](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/daniels_1960_conscience/RN-W1C-communist-oppositions-1918-1929.md#L89)（Daniels 原书 `p.359`）明确写“作者最后修正‘发生派对目的派’的表面二分；目的派也随后被边缘化”。这恰是本卡 2.1 自行强调“标签不能简化”的最佳 A 级背书，本卡却只引 Erlich/Davies。建议在 2.3 增补“Daniels：分歧最终变为专业经济学家的条件约束 vs. 政治当局命令”，使学派光谱含**制度/反对派史**一极。
  3. **漏引 1917–1918 年劳动统计实证**：[`RN-W3-factory-committees…`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/smith_1983_red_petrograd/RN-W3-factory-committees-and-workers-control.md#L108)（Smith 1983, `p.248`）记斯特鲁米林对 27 家彼得格勒工厂的调查：劳动生产率下降近一半源于体力衰竭、仅 21% 源于纪律动机；[`RN-W2-first-year-soviet-rule`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/rabinowitch_2007_in_power/RN-W2-first-year-soviet-rule.md#L110)（Rabinowitch 2007, `pp.390–401`）使用其党员统计（彼得格勒党员约 5 万→6 千）。本卡 2.1 仅泛称“十月革命后从事劳动统计与经济工作”，是站内现成的**最具体一手关联证据**未用。
  4. **“早年属孟什维克”与“参加1906年第四次、1907年第五次代表大会”（T1、2.1）为未核验的断言**：本卡 T3 自承“待补 1906/1907 年代表名单”，但 T1 与 2.1 却以肯定句书写政治归属。库内 [`WEB-1906-04-rsdlp-fourth-stockholm-congress-rules`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E03_E08_party_and_state_docs/1906-04_rsdlp-fourth-stockholm-congress-rules.md) 只给规则不含名单。建议降为“据 RAS 人物条目…（待与代表名单核对）”，并在 `perspectives_missing` 增 `rsdlp-delegate-lists-1906-1907`。（此条为“口径风险”，非已证错误。）
  5. **`perspectives_missing` 写的是“文献”而非“视角”**：`strumilin-original-planning-text`、`first-plan-drafting-responsibilities` 是待补材料而非缺失的学派；真正缺失的是**苏联官方/计划经济史叙述**与**新斯大林主义经济史**（库内 `katasonov_stalin_economy_zh` 有，对“目的论派”评价与 Davies/Erlich 取向相反）。建议改为 `soviet-official-planning-historiography`、`neo-stalinist-economic-history-katasonov`。
- **P2**
  1. **尾部悬空句（`L49`）**：T3 列表之后孤立一行“此后他继续从事经济统计与学术研究，成为苏联科学院院士，1974年去世。”位于 `[T3]` 之外且无来源、与全卡其他事实不同口径（院士年份缺）。建议并入 2.1 末项并标注年份（院士 1931）或直接删除。
  2. `PER-stalin`、`POL-first-five-year-plan` 两条边的“核心依据”仅写“Erlich；Davies”，未指明 `CLM-*`；[`RN-W3-industrialization-models-and-constraints`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/erlich_1960_industrialization/RN-W3-industrialization-models-and-constraints.md) 全文**无“斯特鲁米林/目的/发生”字样**（实测 0 命中），应将其定位为“宏观约束背景”，勿暗示 Erlich 直接论述此人。
  3. 出生地“波多利亚省”无逐字出处，建议在 T3 一并标明依据。

---

### 02. `ORG-bolsheviks-rcpb-vkpb`（布尔什维克—俄共（布）—联共（布））

**总判**：框架稳健、对“必然独裁/环境所迫”两种单线叙事的反制到位；但（a）**S 级一手原典与 Carr 专著札记完全缺席**，（b）**统计分母未与库内多个冲突口径对齐**，（c）**学派覆盖偏单一**，以及（d）边表缺关键节点。

- **P0**：无硬伤。（ID 全部可解析；`DEB-*` 4 个均存在；边表 5 个节点真实。）
- **P1**
  1. **党员统计的分母与口径未与库内既有数字对齐**（本卡 2.1 “约2.4万→约35万”，T3 称“尚须以 Rigby 统计核对”）。库内已有互相**并不一致**的口径，卡片却一概未碰：
     - [`MTG-1917-04-7th-april-party-conference` L20](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1917-04-7th-april-party-conference.md)：七次代表会议代表**约 8 万**党员；
     - [`MTG-1917-07-rsdlp-6th-congress` L32](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1917-07-rsdlp-6th-congress.md)：六大代表**约 20–24 万**党员；彼得格勒组织约 3.2 万（Rabinowitch 1976）；
     - [`CLM-smith-sa-1983-from-workers-control-to-nationalization` L30](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-smith-sa-1983-from-workers-control-to-nationalization.md#L30)：彼得格勒布尔什维克党员 **4.3 万→1.35 万**（1918）；
     - [`RN-W2-first-year-soviet-rule` L110](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/rabinowitch_2007_in_power/RN-W2-first-year-soviet-rule.md#L110)：同一问题引 Strumilin 统计 **约 5 万→6 千**。

     建议在 T3 增一张“党员数分母表”（时点 / 全国或彼得格勒 / 口径=党员或代表所代表数 / 来源），明说 4.3 万→1.35 万与 5 万→6 千**是否为同一时段、同一统计口径尚未调和**，并把本卡“2.4 万/35 万”标为“未入库一手出处的通行数字”。同时 2.1 所写“许多老工人党员离开生产岗位……基层工人社会基础受损”应挂上述两条站内证据，而非只引 Rabinowitch 单书。
  2. **站内 S 级一手原典漏引**：全卡正文只引二手札记，无一条 `WEB-*`。库内已有：[`WEB-1903-08-02-rsdlp-rules-p1`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E07_foundational_docs/1903-08-02_rsdlp-rules-paragraph-1.md)（第一条表决，俄历 08-02 / 公历 **08-15**；证明“列宁草案被否决、马尔托夫案通过”）、[`WEB-1921-03-16-on-party-unity`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E10_turning_points/1921-03-16_on-party-unity.md)（十大《关于党的统一》，通过日 **1921-03-16**，含**秘密第 7 条**）、`WEB-1918-05 lenin-left-wing-childishness-state-capitalism`、`WEB-1927-09-platform-joint-opposition`、`WEB-1923-10-15-declaration-of-the-forty-six`。2.1 应把“被否决”“十大统一”分别锚到这些 S 级文本，T3 补“十大表决 336:50:18”（见 [`ORG-workers-opposition` L65](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-workers-opposition.md#L65) 所引 `CLM-daniels-1960-tenth-congress-turning-point`）。
  3. **漏引 Carr《布尔什维克革命》专著札记**：库内 [`RN-W35-carr-lenin-party-instrument-and-soviet-constitution-1917-1923`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr_bolshevik_rev_v1_zh/RN-W35-carr-lenin-party-instrument-and-soviet-constitution-1917-1923.md) 与 [`RN-W23-carr-party-state-constitution-and-economic-order-1917-1923`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr_bolshevik_rev_v1_v2/RN-W23-carr-party-state-constitution-and-economic-order-1917-1923.md) 正是“党—苏维埃—国家三者关系”最直接的 A 级材料，本卡“执政与内战/统一规则”两段无一处使用，`perspectives_present` 也无 Carr 取向（制度-政治经济派）。建议新增 `political-economy-carr` 并在 2.1 第 3、4 段与 2.3 引入。
  4. **1918 年“左派共产主义者”缺席**：库内已有 [`ORG-left-communists-1918`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-left-communists-1918.md) 与 `CLM-daniels-1960-left-communists-1918`，而本卡“执政与内战”段与 2.2 边表（`internal-opposition` 仅列 `ORG-democratic-centralists`、`ORG-workers-opposition`）**完全未提 1918 年布列斯特和约引发的最大党内分裂**，使“内部争论”叙述从 1917 年直接跳到 1919 年。应在边表补 `ORG-left-communists-1918`（`internal-opposition`，1918.01–05）与 `EVT-1918-03-brest-litovsk-treaty`。
  5. **学派覆盖失衡**：`perspectives_present` 三项（Rabinowitch 社会史、Daniels 反对派史、Khlevniuk 制度史）基本同属修正派/社会史—制度史谱系；**缺失极权论—政治史取向**（Pipes，库内有 [`RN-W4B-patrimonialism-and-october-coup`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/pipes_1990_russian_rev/RN-W4B-patrimonialism-and-october-coup.md)）、**苏联官方党史口径**与 **Rigby 统计**，而 `coverage_status: multi-perspective` 与 2.3 中“不能以一条‘必然独裁’叙述取代”的措辞，实际上只比较了修正派内部尺度。建议要么降为 `grounded`，要么补入 Pipes（“必然论”一极）并在 `perspectives_missing` 保留 Rigby。
  6. **`perspectives_missing: regional-party-studies` 已过时**：库内已有 Koenker 莫斯科（[`RN-W32-koenker-moscow-strikes-duma-votes-and-october-week`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/koenker_1981_moscow_workers_zh/RN-W32-koenker-moscow-strikes-duma-votes-and-october-week.md)）、Smith 彼得格勒、Churakov 地方工厂专使等地方党组织材料，此“缺口”应改写为“省级/非首都党组织（Rigby 未入库）”。
  7. **2.2 边表过窄且缺关键节点**：仅 5 条且一半指向札记/辩题而非节点；缺 `PER-lenin`、`MTG-1903-rsdlp-2nd-congress`、`MTG-1912-01-prague-conference`、`MTG-1917-04-7th-april-party-conference`、`MTG-1917-07-rsdlp-6th-congress`、`MTG-1921-rcpb-10th-congress`、`ORG-left-and-united-opposition`、`PER-stalin`、`INS-sovnarkom-and-vtsik`。其中 `ORG-democratic-centralists` 边所列依据 `RN-W1C-communist-oppositions-1918-1929` **正文零提及“民主集中派/萨普罗诺夫”**（见 04 号卡 P1-1），属“依据与被引文本不符”，应换为 `PER-sapronov`/`PER-osinsky`/`ORG-workers-opposition` L27。
- **P2**
  1. `start_ns: "1903-08-21"`：库内 L3 无此节点（编委会/中央机构选举为 `1903-08-07 [O.S.] / 08-20 [N.S.]`，闭幕 `08-23 [N.S.]`）。建议改为 `1903-08-20` 并注释“`[N.S.]`，伦敦二大，西欧单公历”，或直接对齐 `MTG-1903-rsdlp-2nd-congress`。
  2. **T1 字数刚好触线**：脚本实测去空白后 **150 字**，无余量；后续任何补写都会超限，建议先把“1929年底是本库观察终点”一句移入 `dates` 注释。
  3. **文件尾 `L48–L50` 三行空行**，无悬空文字，但应清理。
  4. T2 2.1 第 1 段、第 4 段多处“……不能……”长句堆叠，单段承载多个论点；建议拆分，便于 `kb.py pack` 切片。

---

### 03. `ORG-octobrists-and-progressive-bloc`（十月十七日同盟与进步同盟）

**总判**：对“十月党≠进步同盟”“进步同盟≠政府”的区分很好，且 `1905-10-17/10-30`、`1907-06-03/06-16`、`1917-02-27/03-12` 三个双历日期换算全部正确；**但有 1 处 P0 悬空 ID，并绕开库内 S 级宣言、Manning 社会基础论断与 L1/L2/L3 时间线**。

- **P0**
  1. **悬空 ID**：YAML `related_debates: ["DEB-1914-haimson-thesis-stability-or-crisis"]` 在库内**不存在**；实际文件为 [`DEB-1914-haimson-thesis-stability.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md)。**修复**：改为 `DEB-1914-haimson-thesis-stability`，并建议增补 `DEB-1917-dual-power-and-february-origins`（对应 2.1 第 4 段、2.3 Hasegawa/Gaida 争论）与 `DEB-1906-stolypin-wager-and-agrarian-viability`（对应 2.1 第 2 段“支持斯托雷平但非无条件”）。
- **P1**
  1. **站内 S 级原典漏引**：本卡以《十月宣言》为起点与起算日，但全文**未回链** [`WEB-1905-10-17-october-manifesto`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E07_foundational_docs/1905-10-17_october-manifesto.md)（S 级，已含 `written_date_ns: 1905-10-30` 与签署地彼得戈夫）；2.1 末段写“古契科夫成为首届临时政府陆海军部长”“罗将科任主席”，库内另有 [`WEB-1917-03-02 nicholas-ii-abdication-manifesto`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/W32_milestone_docs/1917-03-02_nicholas-ii-abdication-manifesto.md) 与 [`PER-guchkov`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md)（1917-03-02 [O.S.] / 03-15 的普斯科夫退位使命），卡片完全未使用。建议在 T3 补 `WEB-1905-10-17-october-manifesto`、`WEB-…abdication-manifesto`。
  2. **漏引库内关于十月党“社会基础/六三体制”的专著材料**：2.1 第 1、2 段断言“温和地主、工商界与部分专业人士，并非阶级成分完全整齐”，却未引库内专门论证——[`CLM-manning-1982-june-third-coup-social-basis`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-manning-1982-june-third-coup-social-basis.md)、[`RN-W12-gentry-reaction-and-four-party-rivalry-1905`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/manning_treadgold/RN-W12-gentry-reaction-and-four-party-rivalry-1905.md)（Manning 的贵族地主与四党竞争）、`timeline/L2_chronicles/E04_1907-1914_stolypin_and_labor_upsurge.md`、`timeline/L3_daily/1912-04_lena_goldfields_and_pravda_upsurge.md`，以及 [`L2 E05`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L2_chronicles/E05_1914-1917_great_war_crisis.md) 与 L1 `TL-W15-L1-E05-05`。T3 自称“进步同盟成立会议日…待查杜马速记”，而 L1 已给出 **`1915-08-25 [O.S.] / 09-07 [N.S.]`（纲领公布）**。
  3. **边表缺少全部实体节点**：2.2 三行节点列分别是 `EVT-…`、`CLM-…`、`CLM-…`——**两条 `CLM` 被当作“关联节点 ID”**，且缺 [`ORG-kadets`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-kadets.md)、`PER-guchkov`、`PER-rodzianko`、`PER-milyukov`、`PER-lvov`、`PER-stolypin`、`INS-state-duma-1906-1917`、`POL-stolypin-agrarian-reform`（库内均已建卡）。这会让 1-hop 上下文包拿不到最核心的邻居。
  4. **`perspectives_present` 标签与证据不符**：`liberal-critique-pipes` 的 T3 证据（`RN-W4B-patrimonialism-and-october-coup`）自注“作为宏观政治史比较，而非对1911年细节的直接核证”，且该札记标题就是十月政变；把 Pipes 登记为本卡“已覆盖视角”属**标签膨胀**。同时缺少 **苏联史学（Avrekh，“六三体制”）**、**Haimson 稳定/危机论**（`related_debates` 本身就指向它却无 CLM）、**Manning**。建议：移除 `liberal-critique-pipes`（或改为 `pipes-macro-comparison-only`），补 `social-basis-manning`，`perspectives_missing` 写 `soviet-historiography-june-third-system`。
  5. **2.3 对 Pipes 的概括过空**：“更强调旧制度及革命政权的政治制度和领导人选择”无法落到任何本库 CLM 页码，建议要么补库内 Pipes 的相关论断卡，要么删去该句以免产生未证学派归属。
- **P2**
  1. `dates.end_ns: "1917-12-31"` 与正文“二月革命与边缘化（1917）”之间缺转折点：杜马实际在 1917 年秋被临时政府解散，建议注释所依据的库内节点（见阶段二 `INS-state-duma-1906-1917` 的对应行）以保持两卡自洽。
  2. 2.1 第 3 段“1915年8月”应补历法，建议 `1915-08-25 [O.S.] / 09-07 [N.S.]`（纲领公布）并区分“组建谈判”与“纲领公布”。
  3. **T1 实测 135 字，合规**（无需处理）；但 T1 未点明“两个组织”的具体日期锚点，可在 150 字内补“1905 / 1915”。
  4. T3 末句“卡片叙述两组织关联而不抹去组织边界”属元叙述，应删或改为可核验的出处说明。

---

### 04. `ORG-democratic-centralists`（民主集中派）

**总判**：对“成员非连续、非工人反对派、十五人集团≠联合反对派”的限定很好，但**核心背景札记不含该组织**（引证与被引文本不符），且**站内已有的 S 级声明全文、PER 卡与 L3 时间线被写成“待补”**，生成起点遗漏 1918 年左派共产主义者。

- **P0**
  1. **引证与被引文本不符**：卡内 T3 第 1 条及 2.2 第 3 行（`POL-ban-on-factions-1921` 依据）把 [`RN-W1C-communist-oppositions-1918-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/daniels_1960_conscience/RN-W1C-communist-oppositions-1918-1929.md) 作为“内战、十大与党内反对派的制度背景”依据，并在 2.1 借 Daniels 立论；但对该札记全文检索 `民主集中|Democratic Central|Decist|Sapronov|萨普罗诺夫|Osinsk|奥新斯基` **0 命中**。该札记只讲到工人反对派、禁派别与 NEP 路线，对 `POL-ban-on-factions-1921` 的关联成立（见其 L71–L75），对**民主集中派本体并不成立**。卡内自注“不完整覆盖十五人集团”，实际是“**完全不覆盖 DC**”。**修复**：把 DC 本体的依据改为库内已逐页核对的 [`PER-sapronov`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sapronov.md)（Daniels 1960 pp. 95、116、138、140）、[`PER-osinsky`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-osinsky.md)（p. 95）、[`ORG-workers-opposition` L27/L65](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-workers-opposition.md#L27)（1920-11 莫斯科省代表会议三派共 124 席 vs 154；1921-01 基层投票萨普罗诺夫 7 票），并直接回到 `sources/monographs/daniels_1960_conscience/`（`ch05` 命中 14 次、`ch09` 8 次、`ch19` 7 次、`ch21` 12 次）。
- **P1**
  1. **站内 S 级一手文本被写成“待补”**：T3 末条“待补……《四十六人声明》签名全文”——库内已有 [`WEB-1923-10-15-declaration-of-the-forty-six`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E09_E10_party_debates/1923-10-15_declaration-of-the-forty-six.md)（S 级，中俄英三版，`written_date_ns: 1923-10-15`）；“十五人政纲及十五大开除名单”亦有库内线索：[`L3 1927-10`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1927-10_tenth_anniversary_and_15th_congress.md#L127) 的 `1927-12-18 [N.S.]` 十五大批准扩大开除，`WEB-1927-09-platform-joint-opposition`，`MTG-1927-12-15th-party-congress`。
  2. **起源叙述遗漏 1918 年左派共产主义者与 1919 年八大军事反对派**：库内 [`PER-osinsky` L57](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-osinsky.md) 明写 DC 由奥新斯基、萨普罗诺夫、弗·米·斯米尔诺夫、马克西莫夫斯基于 **1919 年初**结成；奥新斯基同为 1918 年左派共产主义者（[`ORG-left-communists-1918`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-left-communists-1918.md#L57) 已写明“民主集中派承袭部分反官僚议题，但组织实体已非同一派别”）；[`MTG-1919-03-8th-party-congress` L27](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1919-03-8th-party-congress.md) 记军事反对派。卡内 2.1 “形成与1919年八大”未指向上述任一站内节点，边表也无 `ORG-left-communists-1918`、`PER-sapronov`、`PER-osinsky`、`MTG-1919-03-8th-party-congress`、`MTG-1921-rcpb-10th-congress`、`MTG-1927-12-15th-party-congress`、`ORG-left-and-united-opposition`、`CON-democratic-centralism-and-vanguard`。
  3. **“十五人集团”身份有库内冲突线索，须核对而非直接断言**：`WEB-1927-09-platform-joint-opposition` 的 `edition_note` 把《15人政纲》系于 **1927-06-27**，称其为联合反对派 9 月政纲的前序；而本卡与 `PER-sapronov` 把“十五人集团”（萨普罗诺夫、弗·斯米尔诺夫）描述为独立于联合反对派的极左 DC 集团。二者是同一文件、同一群体还是名称巧合，**库内尚无结论**。建议在 T3 列为“待核：1927-06-27 《15人政纲》是否即 Sapronov–Smirnov 集团文本”，并避免在正文无条件使用“1926–1927 十五人集团”的起止年份。
  4. **学派覆盖失衡 / 标签无出处**：`perspectives_present` 声称含 `party-leadership-official`，2.3 末段也有“党领导层则以战争破坏、协调生产和维护政权安全辩护集中管理”，但**全卡无任何站内 CLM/WEB 作为该论点的出处**（可对接 [`WEB-1921-03-16-on-party-unity`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E10_turning_points/1921-03-16_on-party-unity.md)、`WEB-1918-05 lenin-left-wing-childishness`），属“无证归属”；库内 [`levy RN-W23-makhaevism-intelligentsia-and-soviet-democracy`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/levy_soviet_democracy/RN-W23-makhaevism-intelligentsia-and-soviet-democracy-1917-1929.md) 与 `CLM-soviet-democracy-1924-1927-ozhivlenie-sovetov-paradox` 对 DC 的苏维埃民主解释**完全缺席**，同样 `deutscher RN-W6`、`CON-thermidor-and-bureaucracy`（十五人集团“热月/国家资本主义”判断）可用于展开 2.3，使“集团的政权性质判断”与“后来史家的热月类比”对勘。
- **P2**
  1. **边表“依据”列自引**：2.2 第 2 行 `ORG-workers-opposition` 的“依据”写的仍是 `ORG-workers-opposition`；第 4 行以 `CLM-*` 作“关联节点 ID”。
  2. **译名不一致**：本卡正文用“奥辛斯基”，库内 `PER-osinsky` 用“奥新斯基”；建议统一。
  3. **T1 实测 166 字，超出 150 字约束 16 字**；`start_ns: "1919-01-01"` 为近似起点，已写注释，建议补“依 `PER-osinsky` 1919 年初结成”。
  4. **附带发现（不属本卡，建议另案）**：[`MTG-1919-03-8th-party-congress` L27](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1919-03-8th-party-congress.md) 把萨普罗诺夫写作“列·基·萨普罗诺夫”，而 `PER-sapronov` 为“季莫费·弗拉基米罗维奇”；[`PER-osinsky` L31](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-osinsky.md) 引用 `MTG-1920-03-9th-party-congress` / `MTG-1921-03-10th-party-congress` 两个 ID，库内实际为 `MTG-1921-rcpb-10th-congress`（九大卡未见），可能有悬空。

---

## 四、阶段一小结（01–04）

| 卡 | P0 | P1 | P2 | 一句话判词 |
| :--- | :-: | :-: | :-: | :--- |
| `PER-strumilin` | 0 | 5 | 3 | 限定得当；“本地无原文”与库内二手转述链矛盾，漏 Daniels 对“发生/目的二分”的修正，尾部悬空句 |
| `ORG-bolsheviks-rcpb-vkpb` | 0 | 7 | 4 | 党员统计分母与库内 4 组口径未对齐；无 `WEB-*` 原典；Carr 与 Left Communists 缺席；学派偏修正派 |
| `ORG-octobrists-and-progressive-bloc` | **1** | 5 | 4 | 悬空 DEB；绕开十月宣言 S 级原典、Manning、L1 `1915-08-25 [O.S.]`；边表无实体节点 |
| `ORG-democratic-centralists` | **1** | 4 | 4 | 核心依据札记 0 命中 DC；`WEB` 1923 声明全文已入库却写“待补”；“十五人集团”身份待核 |

---

<!-- 阶段二（05–07）与跨卡汇总矩阵将追加于此 -->

## 五、历法与 YAML `dates` 复核表（后半批 05–07）

| 卡 | YAML `dates` | 卡内日期验算 | 站内/一手对照 | 判定 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-vikzhel` | `start_ns: "1917-08-01"`（“夏季近似”）；`end_ns: "1918-01-31"`（“非断言法律解散”） | `1917-10-25 [O.S.] / 11-07`（+13）✓；`10-29 / 11-11` ✓（“距起义四日”✓）；`11-04 / 11-17` ✓；莫斯科 `10-28 / 11-10` ✓（与 [`Koenker RN-W32 L115–L116`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/koenker_1981_moscow_workers_zh/RN-W32-koenker-moscow-strikes-duma-votes-and-october-week.md#L115-L116) 一致） | L3 [`1917-11`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md#L54) 同给 `10-29 [O.S.]` 最后通牒、`11-02/03/05–06 [O.S.]` 谈判崩溃序列 | **正文日期换算全对**；`end_ns` **`1918-01-31` 恰为旧历末日**（次日即 `02-14` 改历），`_ns` 字段语义应为公历，此值既不是 N.S.，也未标 O.S.（**P2 歧义**）；`1917-08-01` 同样未标历法 |
| `INS-state-duma-1906-1917` | `start_ns: "1906-05-10"`、`end_ns: "1917-10-06"` | 一至四届开幕日：`1906-04-27 [O.S.] / 05-10`、`1907-02-20 / 03-05`、`1907-11-01 / 11-14`、`1912-11-15 / 11-28`，全部 `+13` ✓；`1907-06-03 / 06-16` ✓；`1917-02-27 / 03-12` ✓；`1906-07-08 / 07-21` 与 `07-09 / 07-22` 并存，卡已自陈“须核原件” ✓ | 终结日 `1917-09-23 [O.S.] / 10-06 [N.S.]`：库内**无任何节点**可对勘；`1917-10-06` 为 `_ns`，与卡内“常见日期”换算自洽 | **历法换算无误**；终结日口径无库内锚点（**P1：见 06 号卡**） |
| `INS-sovnarkom-and-vtsik` | `start_ns: "1917-11-08"`、`end_ns: "1929-12-31"` | `1917-10-26 [O.S.] / 11-08` ✓；`10-27 / 11-09` ✓；`11-04 / 11-17` ✓；`1917-12`、`1918-03`、`1923年7月`、`1924年1月` 均无日级、改历后无需双标 | 与 [`L3 1917-11`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md#L126) 的 `1917-11-08 [O.S.] / 11-21 [N.S.]`（斯维尔德洛夫接任）、`11-15 [O.S.] / 11-28`（农民苏维埃执委会合并）**不冲突但全缺** | **历法合规**；`1918-07-10` 宪法日、`1917-11-21` 易帅日均未出现（**P1**） |

---

## 六、后半批逐卡审计与修复方案（05–07）

### 05. `ORG-vikzhel`（维克热尔）

**总判**：日期全部正确，且对“莫斯科停火≠彼得格勒谈判”“辞职名单不等于人民委员名单”等易混点有清晰边界；但**绕开了库内专门为本主题编写的 L3 时间线、专题辩题卡与 Basil/Carr 原书章节，并把 T3“待核一手证据”写在了站内已有的日级证据之上**。

- **P0**：无。（日期 ✓；`CLM-basil-1984-october-and-vikzhel-collapse`、`CLM-rabinowitch-2007-left-sr-coalition-collapse`、`RN-W32-koenker-…`、`EVT-1917-10-october-revolution`、`ORG-psr` 全部真实存在，无断链。）
- **P1**
  1. **漏引站内专题 L3 与专题辩题卡**：本卡 `related_debates` 仅 `DEB-1917-october-coup-or-social-revolution`，**未登记** [`DEB-1917-all-socialist-coalition-vikzhel-missed-chance`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-all-socialist-coalition-vikzhel-missed-chance.md)（其 `core_cards` 第一项即 `ORG-vikzhel`），T3 与边表也**零引用** [`timeline/L3_daily/1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md)。该 L3 已给出本卡自称“待核”的全部逐日节点：`10-29 [O.S.]` 最后通牒（要求 `10-30` 午夜前启动清一色社会主义联合政府谈判，否则全国铁路总罢工）、`11-02 [O.S.]` 夜中执委“让出半数席位”方案、`11-03` 梁赞诺夫赴维克热尔受阻与阿布拉莫维奇宣告“谈判已无意义”及列宁十人最后通牒、`11-04` 中执委 `34:24` 与 `29:23:3`（异文 `25:23`）、`11-05/06` 谈判实际流产、季诺维也夫 `11-06/07` 认错。**修复**：T3 末条“待核一手证据……先后顺序应结合这些材料逐项校对”应改为“逐日顺序见 L3 `…#L54–L124`；该 L3 内部异文（`25:23` / `29:23:3`；莫斯科停火 `11-02` / `11-03`）已并列标注”，并把 DEB 与 L3 写入 `related_debates` 与 2.2 边表。
  2. **“依据”与被引札记不符**：2.2 第 1 行 `ORG-bolsheviks-rcpb-vkpb` 以 [`RN-W2-first-year-soviet-rule`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/rabinowitch_2007_in_power/RN-W2-first-year-soviet-rule.md#L41) 为依据，且 `perspectives_present` 登记 `soviet-political-history-rabinowitch`；但该札记全文对“维克热尔/Vikzhel”**仅有 1 处命中（L41，切尔诺夫施政演说被右翼社革党讥为“维克热尔式的”这一修辞）**，并无对铁路工会谈判的论述。本卡 T3 首条虽自述“不能冒称它直接证明全部维克热尔谈判细节”，但**边表与 `perspectives_present` 仍把它当作直接依据**，内部口径矛盾。**修复**：改引 L3 脚注所载 Rabinowitch 2007 对应章节（L3 脚注 `RAB2007_1/2`）与 `sources/monographs/rabinowitch_2007_*` 的实际页码；若无法回溯，则把 `soviet-political-history-rabinowitch` 降为 `rabinowitch-contingency-thesis-via-CLM`。
  3. **站内 A 级专著原文已有 Vikzhel 章节，却写成“待核读”**：库内 [`sources/monographs/basil_1984_mensheviks_1917/ch09_chapter_vii_the_final_collapse.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/basil_1984_mensheviks_1917/ch09_chapter_vii_the_final_collapse.md)、`carr_1950_bolshevik_rev_v1_en/ch04_pages_101-125.md`、`ch17_pages_426-443.md`、`carr_bolshevik_rev_v1_zh/ch05_第二部分_宪法结构_part_1.md` 均含 Vikzhel；`RN-W23-carr-party-state-…` L81 已把 Vikzhel/Vikzhedor 与 1918 年交通人民委员“独裁权力”法令连成一线（Carr `ch09`，`PDF pp.172–173`）。T3 对 Basil、Carr 都没有页码，也无 Carr 取向。
  4. **学派覆盖低于本卡所挂辩题的实际光谱**：`DEB-1917-all-socialist-coalition-vikzhel-missed-chance` 登记 4 派（Rabinowitch 偶然论、**Pipes–Malia 意识形态与权力集中论**、**Trotsky–Deutscher 革命左翼结构不相容论**、地方社会主义者）；本卡 `perspectives_present` 仅 3 项且**无 Pipes–Malia 与革命左翼**，而 2.3 也只比较 Rabinowitch/Koenker/Basil。`CLM-pipes-1990-october-classic-coup`、`CLM-yao-hai-post-october-coalition-failure-and-one-party-formation`、`CLM-getzler-1967-martov-soviet-opposition`（Martov 与 Vikzhel 谈判）在库内已有，却不见于本卡。`coverage_status: multi-perspective` 与“广泛联合是否可行仍是反事实问题”的结论，因缺“意图-权力垄断”一极而**对修正派一侧倾斜**。建议补入 Pipes–Malia、Trotsky–Deutscher 两类，或降级为 `grounded`。
  5. **组织构成归属未证（2.1 第 1 段）**：卡称“左翼社革党和孟什维克国际主义派等温和或倾向妥协者在斡旋中重要”。库内 L3 L54 明写维克热尔“**由孟什维克与社革党主导**”，右翼社革党与孟什维克拒绝让步（L96、L114）；Koenker L116 则称斡旋方含邮电工会、孟什维克、社革党和东正教大主教。把“左翼社革党”写为机关内关键调停方无库内出处，应改为“成员以右翼社革党与孟什维克为主，**机关内席次待核**”。
  6. **2.2 边表过窄、节点缺位**：仅 4 行且 `ORG-psr` 行的依据是 `CLM-rabinowitch-2007-left-sr-coalition-collapse`（讲左翼社革党），应对应 [`ORG-left-srs`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-left-srs.md)；缺 `PER-kamenev`、`PER-rykov`、`PER-zinoviev`、`PER-sverdlov`、`PER-martov-l`、`PER-dan`、`INS-sovnarkom-and-vtsik`、`PER-lenin`（均已建卡且卡内正文已涉及）。
  7. **统计分母缺失**：2.1 对中执委“让出半数席位”方案、`11-04` 表决、辞职人数无任何分母；L3 已给 `34:24:1`、`20:25（12 弃权）`、`29:23:3`（异文 `25:23`）、10 名中央多数派联署对 5 名少数派中委（L96、L102）。建议在 T3 增“表决口径对照表”并把异文来源写明。
- **P2**
  1. `end_ns: "1918-01-31"`：见上表，应改为 `1918-01`（月级）并注明“`[O.S.]`/“`_ns` 取公历则为 `1918-02-13`”，或改用库内维克热多尔成立的具体节点日期（目前库内 L3 止于 `12-12 [O.S.]`，**无 1918 年 1 月维克热多尔节点**，应在 `perspectives_missing` 写明）。`start_ns: "1917-08-01"` 同样补“近似、历法不明”。
  2. T1 实测 **150 字**，刚好触线。
  3. 2.1 最末段“具体代表资格、选举程序及旧机关终止日期需查铁路工会原始记录”与 T3 末条重复；建议 2.1 只保留事实，把“待核”集中到 T3。

---

### 06. `INS-state-duma-1906-1917`（国家杜马）

**总判**：制度描述严谨，**日期换算与“须核原件”的自我设限都很到位**，一二两届、三四届开幕日与解散日全部正确；但**把站内已有的 Pipes 议席数据、Manning 六三社会基础论断、L2/L3 时间线及十月宣言原典写成“尚待查核/暂不编造”**，且 `perspectives_present` 有标签膨胀。

- **P0**：无硬伤。（`POL-october-manifesto-and-1906-fundamental-laws`、`CON-dual-power`、`DEB-1914-haimson-thesis-stability`、`CLM-gaida-2003-liberals-in-february-1917` 等全部真实存在；全部 O.S./N.S. 对应 `+13` 正确。）
- **P1**
  1. **“议员人数……暂不编造统一数字”与“Pipes 具体判断……尚待查核”（T3 `3.2`）与库内事实不符**：
     - [`timeline/L2_chronicles/E03_1905-1907_first_revolution.md` L38](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L2_chronicles/E03_1905-1907_first_revolution.md#L38) 已入库 Pipes 的**第二届杜马席位结构：社会党人合计 222（社民 65、社革 37、人民社会党 16、劳动派 104），立宪民主党 98，低于第一届的 179**，并写明“这是派普斯的议席归类，边界党团如何计数仍可复核”，另载两届杜马存续约 **72 天与 105 天**；
     - [`E04_1907-1914` L76](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L2_chronicles/E04_1907-1914_stolypin_and_labor_upsurge.md#L76)：第三届杜马 `11 月 1 日` 与 **422 席**结构（A 级，指向 `sources/monographs/pipes_1990_russian_rev/ch13_section.md`）；
     - 对照 [`RN-W29 Hildermeier`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/hildermeier_psr_full/RN-W29-hildermeier-psr-azev-crisis-and-modernization-dilemma.md#L36) 称第二届杜马社革党议员为 **34 名**（vs Pipes 的 37）、土地社会化法案获 **104 票**——**两组分母在库内并存且不一致**，正是 P1 应“并列呈现”的统计口径冲突。
     **修复**：删去“暂不编造统一数字”，改为一张“议席与存续口径表”（届别 / 开幕与终止 [O.S.]/[N.S.] / 席位 / 来源 / 口径差异），明确“Pipes 222 与 Hildermeier 的社革党 34 vs 37 为不同口径，待回核”，并在 `perspectives_missing` 的 `legislative-roll-call` 之外补 `seat-count-reconciliation`。
  2. **终结日 `1917-09-23 [O.S.] / 10-06 [N.S.]` 无库内锚点、且方向易混**：卡内对该日期写“原始法令及日期口径仍待核”，自我设限正确，但 YAML `end_ns: "1917-10-06"` 已硬写入。库内 L1/L2/L3（`E06`、`1917-10_october_insurrection`）**均未收录杜马正式解散节点**（本轮对 `杜马…解散` 检索，仅命中 L1 的 `1907-06-03` 一条与 Gaida 的泛称，无 1917 年节点）。本审计人未取得可核的外部原件，**不判对错**，仅指出：此日期若误把“旧历 10-06”写成“新历 10-06”将错位 13 天，须在 `dates` 注释写明“依据：待核法令；`_ns` 口径=`1917-10-06`”并回补 L1 节点；与 `ORG-octobrists-and-progressive-bloc.end_ns: 1917-12-31` 并存的“杜马终结”口径也应互相对照。
  3. **站内 S/A 漏引**：全卡无 `WEB-*`。库内 [`WEB-1905-10-17-october-manifesto`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E07_foundational_docs/1905-10-17_october-manifesto.md)（S，`written_date_ns: 1905-10-30`）可作为第 2.2 边表 `POL-october-manifesto-and-1906-fundamental-laws` 行“基本法原文待对照”的一半证据（宣言文本，但不含 1906 基本法本文，需注明）；`CLM-manning-1982-june-third-coup-social-basis` 与 `RN-W12-gentry-reaction-and-four-party-rivalry-1905` 正对应 2.1 第 1 段“1907 年法进一步提高地主及有产阶层权重”，库内已有，卡内未引；`timeline/L3_daily/1917-02_february_eight_days.md`（L121–L125：停会敕令、杜马私人会议、`23:30` 前后临时委员会决定掌权）可替代泛称“面对停会诏令”；Hasegawa 札记 `RN-W1C-february-insurrection-and-dual-power` 虽在 CLM 层被引，札记本身未列入 T3。
  4. **学派标签膨胀与失衡**：`perspectives_present` 登记 `social-history`，但全卡无社会史论证；`constitutional-institutional` 也无任何库内 CLM 页码。同时 `related_debates` 仅 `DEB-1914-haimson-thesis-stability`，漏 [`DEB-1917-dual-power-and-february-origins`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md)（对应 2.1 末段与 2.2 `CON-dual-power` 行）、[`DEB-1906-stolypin-wager-and-agrarian-viability`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1906-stolypin-wager-and-agrarian-viability.md)（对应第三届杜马与斯托雷平）。2.3 中 Pipes–Haimson“对读”一句无页码，T3 也承认“Pipes 对各届的具体判断尚待查核”，应改为库内 Pipes 议席归类这一**唯一可核**的 Pipes 论点。
  5. **任期口径缺失**：卡为制度卡却未写**各届杜马主席与任期**，而库内人物卡已有交叉锚点：`PER-guchkov`（“1910–1911年主持第三届杜马”）、`PER-rodzianko`（1911 起；`1917-02-27 [O.S.]` 临时委员会主席）。2.2 边表仅列 `PER-rodzianko`，漏 `PER-guchkov`、`PER-milyukov`、`ORG-kadets`、`PER-stolypin`、`POL-stolypin-agrarian-reform`、`EVT-1917-02-february-revolution`、`ORG-octobrists-and-progressive-bloc` 的**反向互链**已有，但 `ORG-kadets` 缺。建议补“杜马主席表”（穆罗姆采夫、戈洛文、霍米亚科夫、古契科夫、罗将柯；仅在库内已有节点范围内填，其余标待核）。
  6. 2.2 边表“核心依据”两行写“基本法原文待对照”“Hasegawa；Gaida”，未指向 `CLM-*`；`CON-dual-power` 行“Hasegawa；Gaida”应落到 `CLM-hasegawa-2018-dual-power-origins`（库内存在）。
- **P2**
  1. **T1 实测 169 字**，超 150 字约束 19 字。
  2. **Schema**：正文 `L19` 多出一行 H1（`# 俄罗斯帝国国家杜马（1906–1917）`），不在 `docs/TEMPLATES.md` 的卡片模板内；T3 使用 `### 3.1 / 3.2` 子标题，与模板“T3 无子结构”略异，但不影响 `kb.py pack` 的 `## [T*]` 锚点，可保留；`type: organization` 配 `INS-` 前缀属全库既有做法。
  3. 2.1“第一届”条同时给 `07-08` 与 `07-09`，已自陈须核原件，**建议在 T3 补一行“库内无对应 L3 节点”**以免读者误以为库内已核。
  4. 2.3 以加粗“**经验共识**/**解释分歧**”段落替代模板的列表式光谱，可保留，但建议补 CLM 链接。

---

### 07. `INS-sovnarkom-and-vtsik`（人民委员会与中执委）

**总判**：宪制分层（苏俄/苏联、中执委/人民委员会）书写准确，**所有日期换算正确，Carr 的“1,615 对 375”与库内札记完全吻合**，两处外链实测均 **HTTP 200**；主要缺陷是**站内 S 级文本与专题 L3 缺席、关键表决数字与易帅日期缺失、辩题选择偏**。

- **P0**：无。（日期 ✓；`RN-W23`/`RN-W32-carr-…`/`RN-W2-first-year-soviet-rule` 等存在；外链两条 200。）
- **P1**
  1. **库内 S 级原典漏引，且 1918 年宪法完全无出处**：2.1 第 3 段写“1918年苏俄宪制”，但全卡没有指向本地 [`WEB-1918-07-10 rsfsr-constitution-franchise-and-power`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E03_E08_party_and_state_docs/1918-07-10_rsfsr-constitution-franchise-and-power.md)（S 级，`written_date_ns: 1918-07-10`，含第五次苏维埃代表大会通过日与第 43 条印刷错误考证）；T3 `3.1` 第一、二条仅给 `marxists.org` 外链，而库内已收 `1917-10-26 decrees-on-peace-and-land`、`1918-01-03 declaration-of-rights-of-working-and-exploited-people`、`MTG-1917-10-2nd-congress-of-soviets`、`MTG-1918-07-5th-congress-of-soviets`。建议：外链保留为参照，**主出处改为库内 WEB/MTG**，并把 1918 年宪法日期写入 2.1（`1918-07-10`，改历后纯公历）。
  2. **表决数字缺失，而库内 L3 已逐项并列异文**：2.1 第 2 段“`1917-11-04` 中执委决议承认人民委员会可对紧急事项先颁布法令”，T3 又称“1917年冬每次政府法令争执的动议及表决……待核”。库内 [`L3 1917-11` L102、L243](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md#L102) 已记：出版法令之拉林动议被 **34:24（1 弃权）** 否决，斯皮罗不信任动议 **20:25（12 弃权）** 被否决，乌里茨基决议 **29:23:3** 通过（异文 **`25:23`**，派普斯部分记录），且特别写明“四名身为人民委员的布尔什维克代表亲自投票”才使其勉强过关——这是**判断“承认紧急立法权”是否具备代议机关多数支持的关键分母**。**修复**：2.1 第 2 段补三组表决与异文，T3 `3.2` 改为“库内 L3 已列；速记原件待核”。
  3. **易帅、扩编等关键节点缺日期**：2.1 第 1 段写“中执委主席先为加米涅夫，继为斯维尔德洛夫”，2.2 `PER-sverdlov` 行依据竟为“二大后中执委档案待核”；库内 L3 L126 已给 **`1917-11-08 [O.S.] / 11-21 [N.S.]` 斯维尔德洛夫接替**，L158 给 **`1917-11-15 [O.S.] / 11-28 [N.S.]` 工兵与农民苏维埃中执委合并**（原 101 名 + 农民执委 108 + 陆海军代表 100 + 工会代表 50）。本卡称“新中执委包括左翼社革党人”，却**不提 11-15 后中执委的构成扩张**，使“中执委 ≈ 苏维埃议会”的分母被默认为二大选出的原班人马。
  4. **边表缺失关键节点**：缺 [`PER-kamenev`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-kamenev.md)、[`PER-kalinin`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-kalinin.md)、`PER-rykov`、`ORG-vikzhel`、`ORG-left-srs`、`CON-constituent-assembly`、`EVT-1918-01-constituent-assembly-dispersal`、`MTG-1917-10-2nd-congress-of-soviets`、`MTG-1918-07-5th-congress-of-soviets`、`POL-brest-litovsk-treaty`（左翼社革党 1918-03 退出）；2.1 末段点名李可夫，但边表仅挂 `ORG-right-opposition-1928`，无 `PER-rykov`。
  5. **漏引 Carr 另一份核心札记与出处归因**：卡引 `RN-W23` 与 `RN-W32-carr-dispersal…`，但漏 [`RN-W35-carr-lenin-party-instrument-and-soviet-constitution-1917-1923`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr_bolshevik_rev_v1_zh/RN-W35-carr-lenin-party-instrument-and-soviet-constitution-1917-1923.md#L67)（L67：中执委扩编 200→300 人、会期缩至每年三次、STO/计委/小型人民委员会增设；“1,615 对 375”由 **Carr 转引韦尔纳茨基统计**）。本卡写作“Carr 所引……”但未说明**统计源头与统计期**，应在 T3 补“Vernadsky 经 Carr 转引，页码 pp. 148、216（库内札记 `ch09 p.216`）；`p.148` 未在库内札记中核到，待核”。
  6. **辩题选择偏**：`related_debates` 仅 `DEB-1922-lenin-testament-and-stalin-rise`，该公案与 Sovnarkom 的交点仅在格鲁吉亚事件，而库内更对口的 [`DEB-1917-all-socialist-coalition-vikzhel-missed-chance`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-all-socialist-coalition-vikzhel-missed-chance.md)（`11-04` 法令权之争）、[`DEB-1918-constituent-assembly-and-soviet-democracy`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-constituent-assembly-and-soviet-democracy.md)（中执委与代议权）、[`DEB-1923-nationality-and-empire`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1923-nationality-and-empire.md)（联盟宪制）全缺。
  7. **学派光谱缺“极权论/意识形态一极”与“苏维埃民主论”**：2.3 仅 Carr、Rabinowitch、Khlevniuk；库内 `RN-W23-makhaevism-intelligentsia-and-soviet-democracy`（Levy）与 `CLM-soviet-democracy-1924-1927-ozhivlenie-sovetov-paradox` 直接讨论苏维埃机关“活跃化”悖论，Pipes 一极亦缺；`perspectives_present: archival-revisionist` 对一张全卡无任何档案原件的机构卡而言**标签偏重**。建议补 Levy 与 Pipes，并把 `archival-revisionist` 改为 `revisionist-contingency-via-secondary`。
- **P2**
  1. **T1 实测 151 字**，超 1 字。
  2. **Schema**：`L19` 多一行 H1；T3 使用 `3.1/3.2` 子标题（可保留）。
  3. 2.2 第 2 行 `PER-sverdlov` 的“二大后中执委档案待核”属“待核”占位而非依据；第 5 行 `EVT-1922-georgian-affair-and-ussr-formation` 的依据“Carr vol. 1, pp. 402–409”应落到 `CLM-*` 或 `RN-W32-carr-dispersal…`。
  4. 全卡缺全苏中执委“主席团集体主席”（加里宁、彼得罗夫斯基、纳里曼诺夫、切尔维亚科夫）与联盟院/民族院席额，**已在 `perspectives_missing` 标 `union-presidium-minutes`，但未提供库内已有的最小信息**，建议至少给出主席团构成的“待核”标识。

---

## 七、跨卡汇总矩阵（7 张）

| 卡 | P0 | P1 | P2 | 断链 | 双历法 | S/A 漏引 | 统计分母/口径 | 学派覆盖 | 悬空尾句/Schema |
| :--- | :-: | :-: | :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| `PER-strumilin` | 0 | 5 | 3 | 无 | ✓（`+12`） | RN-W36、CLM-B-P、Daniels RN-W1C L89、Smith RN-W3 L108、RN-W2 L110 | “计划即规律”转述链未回链；27 厂 21% 未用 | 缺 Daniels 修正与苏联/新斯大林一极 | **有悬空尾句 `L49`** |
| `ORG-bolsheviks-rcpb-vkpb` | 0 | 7 | 4 | 无 | 起点 `08-21` 未标且与 L3 差 1 日 | WEB-1903、WEB-1921、Carr RN-W35/W23、Left Comm | 党员数：4.3 万→1.35 万 vs 5 万→6 千 vs 80k vs 200–240k 未对齐 | 缺 Pipes、官方、Rigby | T1=150 临界；尾部空行 |
| `ORG-octobrists-and-progressive-bloc` | **1** | 5 | 4 | **`DEB-1914-haimson-thesis-stability-or-crisis`** | ✓；“1915年8月”缺历法 | WEB-1905、WEB-abdication、Manning CLM/RN、L1/L2 | 无席位与成员分母 | Pipes 标签膨胀；缺 Avrekh、Manning | T3 末句元叙述 |
| `ORG-democratic-centralists` | **1** | 4 | 4 | 无 | ✓ | WEB-1923 声明、PER-sapronov/osinsky、L3 1927、MTG-1927 | 莫斯科 124:154、7 票 未用 | “党领导层”无出处；Levy/Thermidor 缺 | T1=166 超限 |
| `ORG-vikzhel` | 0 | 7 | 3 | 无 | `end_ns` 取旧历末日歧义 | L3 1917-11、DEB-vikzhel、Basil ch09、Carr ch04/17/05 | 表决 `34:24:1` 等缺 | 缺 Pipes–Malia、Trotsky–Deutscher | RN-W2 引证不实 |
| `INS-state-duma-1906-1917` | 0 | 6 | 4 | 无 | ✓；终结日无锚点 | WEB-1905、Manning、L2 E03/E04、L3 1917-02 | **“暂不编造数字” vs 库内 222/98/179/422；社革党 34 vs 37** | `social-history` 标签膨胀 | T1=169 超限；H1 |
| `INS-sovnarkom-and-vtsik` | 0 | 7 | 4 | 无 | ✓；外链均 200 | WEB-1918-07-10、MTG 二大/五大、L3 1917-11、RN-W35 | 表决 `34:24`/`29:23:3`/`20:25` 与 11-15 扩编缺 | 缺 Pipes、Levy；辩题错配 | T1=151；H1 |
| **合计** | **2** | **41** | **26** | **1 处悬空 ID** | **0 处换算错误** | 全部 7 卡均有 | 5 卡有口径冲突 | 全部 7 卡 | 3 卡 T1 超限 |

> **总体结论**：7 张卡**无一处 O.S./N.S. 换算错误**，外链 3 条（RAS、两条 marxists.org）全部可达；Codex 的优点是对“标签—个体差异”“文献边界”的自我限定普遍到位。系统性缺陷集中在两处：(1) **“待核/待补”与站内已建 S/A 材料不同步**（4、5、6、7 号卡尤甚），(2) **依据列所引札记并不覆盖卡内被支撑的命题**（4 号：`RN-W1C` 0 命中民主集中派；5 号：`RN-W2` 仅 1 处修辞性提及）。

---

## 八、修复优先级清单

### P0（须在下一轮提交前修复，共 2 项）

| # | 卡 | 位置 | 修复 |
| :-: | :--- | :--- | :--- |
| P0-1 | `ORG-octobrists-and-progressive-bloc` | YAML `related_debates` | `DEB-1914-haimson-thesis-stability-or-crisis` → `DEB-1914-haimson-thesis-stability`；并补 `DEB-1917-dual-power-and-february-origins`、`DEB-1906-stolypin-wager-and-agrarian-viability` |
| P0-2 | `ORG-democratic-centralists` | T3 第 1 条、2.2 第 3 行、2.3 | 把 `RN-W1C` 从“DC 本体依据”降为仅 `POL-ban-on-factions-1921` 依据；DC 本体改引 `PER-sapronov`、`PER-osinsky`、`ORG-workers-opposition` L27/L65 与 `daniels_1960_conscience` ch05/09/19/21 实页 |

### P1（建议下一轮一次性修，按“投入小/收益大”排序）

1. **改“待补/待核”为已入库 S 级链接**：`ORG-democratic-centralists`（`WEB-1923-10-15` 声明全文、`L3 1927-10` 的 `1927-12-18`）、`ORG-vikzhel`（L3 1917-11 + DEB）、`INS-sovnarkom-and-vtsik`（`WEB-1918-07-10`、L3 表决数）。
2. **统一补“口径对照表”**：党员数（`ORG-bolsheviks`）、议席数（`INS-state-duma`，含 Pipes 222/98/179/422 与 Hildermeier 34 vs 37）、中执委表决与扩编数（`INS-sovnarkom`/`ORG-vikzhel`）。
3. **补缺位节点**：`ORG-left-communists-1918`（Bolsheviks、DC）、`ORG-kadets`/`PER-guchkov`/`PER-milyukov`/`INS-state-duma`（Octobrists）、`PER-kamenev`/`PER-kalinin`/`PER-rykov`/`ORG-vikzhel`（Sovnarkom）、`PER-kamenev`/`PER-rykov`/`ORG-left-srs`（Vikzhel）。
4. **学派补全**：Pipes（Bolsheviks、Vikzhel、Sovnarkom）、Manning（Octobrists、Duma）、Levy/Soviet democracy（DC、Sovnarkom）、Daniels 对“发生/目的”二分的修正（Strumilin）、Carr RN-W35（Bolsheviks、Sovnarkom）。
5. **降标签**：`liberal-critique-pipes`（Octobrists）、`social-history`（Duma）、`archival-revisionist`（Sovnarkom）、`soviet-political-history-rabinowitch`（Vikzhel，直到补回对应章节）、`party-leadership-official`（DC）。
6. **未证归属改“待核”**：Strumilin“早年属孟什维克/IV、V 大会代表”；Vikzhel“左翼社革党在机关内重要”；DC“十五人集团”与 `1927-06-27《15人政纲》`同一性。

### P2（可随手修）

- T1 字数：`ORG-democratic-centralists`（166）、`INS-state-duma-1906-1917`（169）、`INS-sovnarkom-and-vtsik`（151）超限；`ORG-bolsheviks`、`ORG-vikzhel`（均 150）无余量。
- `PER-strumilin` 文末悬空句（`L49`）；`ORG-bolsheviks` 尾部三行空行；两张 `INS-` 卡的多余 H1。
- `dates`：`ORG-bolsheviks.start_ns` 对齐 L3 `1903-08-20 [N.S.]`；`ORG-vikzhel.end_ns` 改月级并标历法；`ORG-octobrists` “1915年8月”补 `1915-08-25 [O.S.] / 09-07 [N.S.]`。
- 边表列使用：`ORG-octobrists`、`ORG-democratic-centralists` 把 `CLM-*` 当“关联节点 ID”；`ORG-democratic-centralists` 第 2 行依据自引。
- 译名统一：“奥辛斯基”/“奥新斯基”。
- **库外附带缺陷（非本批被审，另案）**：`MTG-1919-03-8th-party-congress` 将萨普罗诺夫误写作“列·基·萨普罗诺夫”；`PER-osinsky` 的 `MTG-1920-03-9th-party-congress` / `MTG-1921-03-10th-party-congress` 两个 ID 在库内未见（库内为 `MTG-1921-rcpb-10th-congress`）。

---

## 九、审计边界与未决事项

1. **未能独立核验**：`INS-state-duma-1906-1917` 的终结日 `1917-09-23 [O.S.] / 10-06 [N.S.]`（库内无原件，外部检索工具未返回可引证页面，仅得无出处的背景记忆，不予采信）；`PER-strumilin` 的 1906/1907 年大会代表资格与出生地；`ORG-vikzhel` 的成立日与维克热多尔产生日。
2. **库内数据自身存在冲突，审计未裁决，仅要求并列**：党员数 4.3 万→1.35 万（Smith）与 5 万→6 千（Rabinowitch 引 Strumilin）；第二届杜马社革党 34 / 37 名；`11-04` 中执委表决 `29:23:3` / `25:23`；莫斯科停火 `11-02` / `11-03`。
3. 报告中以 `WEB-…` 称呼的站内原典，其标识取自对应文件名或 frontmatter `id`（如 `WEB-1923-10-15-declaration-of-the-forty-six`、`WEB-1921-03-16-on-party-unity`、`WEB-1905-10-17-october-manifesto`），个别以文件名代称者，落盘修复前应回查实际 `id`。
4. 本轮纯只读：未修改被审卡片、札记、时间线与共享总表；唯一写入文件为本报告。
