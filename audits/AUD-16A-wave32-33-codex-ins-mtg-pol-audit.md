# AUD-16A｜第32—33波 Codex 编纂制度／会议／政策卡异源交叉审计报告（7张）

- **审计日期**：2026-11-18
- **审计角色**：`dialectic-auditor`（异源交叉审计：Anthropic Claude Sonnet 5.5 审读 OpenAI `gpt-6.1-terra` 撰写的 7 张制度、会议与政策卡）。
- **唯一写入目标**：[`audits/AUD-16A-wave32-33-codex-ins-mtg-pol-audit.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-16A-wave32-33-codex-ins-mtg-pol-audit.md)；纯只读审计，未改动任何被审卡片、札记、时间线或共享总表。
- **审计对象（分两阶段落盘）**：
  - **阶段一（01–04，本节）**：[`INS-rabkrin-and-ccc`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rabkrin-and-ccc.md)、[`INS-gosbank-and-narkomfin`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-gosbank-and-narkomfin.md)、[`MTG-1906-04-rsdlp-4th-stockholm-congress`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1906-04-rsdlp-4th-stockholm-congress.md)、[`MTG-1917-04-7th-april-party-conference`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1917-04-7th-april-party-conference.md)
  - **阶段二（05–07 与汇总修复矩阵）**：见本文件后续追加部分。

---

## 一、审计方法与判级准则

1. **标准**：沿用 [`AUD-15A`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-15A-wave32-33-codex-people-cards-audit.md) 判级——**P0**＝史实／历法／断链／失效外链硬伤；**P1**＝站内 S/A 漏引、票数与统计分母失准、学派失衡、把“待核”挂在站内已可核的事项上；**P2**＝Schema 规范、悬空尾句、措辞。
2. **核验手段**：(a) `python scripts/kb.py date --from os` 复算双历；(b) 逐一检查 7 张卡正文中全部 `PER-/ORG-/INS-/MTG-/POL-/CON-/DEB-/DATA-/CLM-` 节点 ID 是否真实存在（`cards/`、`historiography/`、`data/`）；(c) 对卡内全部 http(s) 外链做 GET 实测；(d) 与站内 `sources/web-archive/`、`sources/monographs/`、`reading-notes/`、`timeline/L3_daily/` 对读。
3. **双历法规则**（`AGENTS.md` §2.5）：1900-03-01—1918-01-31 [O.S.] 俄国本土事件 `+13` 天；西欧会场（斯德哥尔摩）用当地公历；1918-02-14 改历后纯公历。

### 1.1 全 7 张卡节点 ID 与外链总体结果（阶段一已完成的前置检查）

| 检查 | 结果 |
| :--- | :--- |
| 节点 ID 存在性（边表 + `related_debates` + 正文反引号 ID） | **全部命中**：`PER-lenin/stalin/kuibyshev/ordzhonikidze/kamenev/sokolnikov`、`ORG-*`、`INS-politburo-orgburo-secretariat`、`INS-vsnkh-and-gosplan`、`MTG-1903-rsdlp-2nd-congress`、`CON-democratic-centralism-and-vanguard`、`CON-dual-power`、`POL-nep`、`POL-sokolnikov-chervonets-monetary-reform`、`DEB-1903/1922/1918/1928…`、`CLM-other-nep-1923-sokolnikov-monetary-discipline` 等均存在。`DATA-02-1922-1924-scissors-crisis-and-chervonets` 位于 [`data/`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-02-1922-1924-scissors-crisis-and-chervonets.md)（非 `cards/`，属合规，但图谱 ID 解析器须确认已索引 `data/`）。**阶段一四卡无断链。** |
| 外链实测（阶段一四卡） | 200 通过：[marxists.org 1923/jan/23](https://www.marxists.org/archive/lenin/works/1923/jan/23.htm)、[marxists.org 1923/mar/02](https://www.marxists.org/archive/lenin/works/1923/mar/02.htm)、[cbr.ru 历史页](https://www.cbr.ru/eng/about_br/history/)、[cbr.ru ArchivalFonds_017.pdf](https://www.cbr.ru/Content/Document/File/48217/ArchivalFonds_017.pdf)。**未能通过：[`istmat.org/node/40879`](https://www.istmat.org/node/40879)（SSL 握手失败，见 02-02）。** |

---

## 二、历法与日期复核表（前半批 01–04）

| 卡片 | 卡内日期（YAML／正文） | `kb.py` 复算 | 判定 |
| :--- | :--- | :--- | :--- |
| `INS-rabkrin-and-ccc` | `start_ns 1920-02-07`；列宁文 `1923年1月23日`、`3月2日`；`1926年11月3日` | 全部在 1918-02-14 改历后，纯公历；`1920-02-07` 与 Carr《布尔什维克革命》卷1 所记“VTsIK 1920年2月7日法令”一致 | **历法合规**；起始日并非“待核”，见 01-01 |
| `INS-gosbank-and-narkomfin` | `1917-12-14 [O.S.] / 1917-12-27 [N.S.]`；`1920-01-19`；YAML `1917-11-08` | `12-14 O.S.` → `12-27 N.S.` ✓（+13）；`1920-01-19`、1921—1929 均纯公历；`start_ns 1917-11-08` = `1917-10-26 [O.S.]`（军革委 10 月 25—26 日夜接管国家银行，见 L3 `1917-10_october_insurrection` L174） | **换算无误**；YAML 起点可补一句 O.S. 锚点（P2） |
| `MTG-1906-04-rsdlp-4th-stockholm-congress` | `start_ns 1906-04-23`／`end_ns 1906-05-08`；T3 称俄历 `4月10—25日` | `1906-04-10 O.S.` → `04-23 N.S.`；`1906-04-25 O.S.` → `05-08 N.S.`（+13）✓；会场在斯德哥尔摩，使用当地公历 | **历法完全合规，无换算错位**；已与站内 S 级档案 [`1906-04_rsdlp-fourth-stockholm-congress-rules.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E03_E08_party_and_state_docs/1906-04_rsdlp-fourth-stockholm-congress-rules.md) 前言一致 |
| `MTG-1917-04-7th-april-party-conference` | `1917-04-24 [O.S.] / 05-07 [N.S.]` 至 `04-29 [O.S.] / 05-12 [N.S.]`；YAML `1917-05-07 → 05-12` | `04-24 O.S.` → `05-07 N.S.` ✓；`04-29` → `05-12` ✓（+13）；会场彼得格勒，机器起止用公历 | **历法合规** |

---

## 三、前半批逐卡审计与修复方案（01–04）

### 01｜中央监察委员会与工农检查人民委员部（`INS-rabkrin-and-ccc`）

**结论**：框架稳健（明确区分“联合办公”与“法律合并”、拒绝把列宁两文夸大为反斯大林机关）。主要问题是把站内 A 级专著已能核实的锚点挂为“待核”，并漏引 3 个站内一等互链卡与 Carr 的合并叙事。

#### 01-01｜P1｜`1920-02-07` 起始日被标成“暂作待核工作锚点”，但站内 A 级 Carr 已直接给出该法令
- **定位**：[`INS-rabkrin-and-ccc.md:10`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rabkrin-and-ccc.md#L10)、[`L27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rabkrin-and-ccc.md#L27)、[`L53`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rabkrin-and-ccc.md#L53)。
- **核证**：Carr 卷1英文本 [`ch09_pages_226-250.md` L578–586](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/carr_1950_bolshevik_rev_v1_en/ch09_pages_226-250.md#L578-L586) 原文：“By a decree of VTsIK of February 7, 1920, it was transformed into a People's Commissariat of Workers' and Peasants' Inspection (Rabkrin or RKI)… While the People's Commissar remained unchanged”；中译同见 [`carr_bolshevik_rev_v1_zh/ch07…part_3.md` L247–252](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/carr_bolshevik_rev_v1_zh/ch07_第二部分_宪法结构_part_3.md#L247-L252)，札记 [`RN-W23` L48](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr_bolshevik_rev_v1_v2/RN-W23-carr-party-state-constitution-and-economic-order-1917-1923.md#L48)。因此：①“VTsIK 1920-02-07 法令”可降级为**已核**，T3.2 中“署日与施行日待核原件”应收窄为“公布与施行日待核”；②Carr 同时证明“人民委员未换”（国家监察人民委员部→工农检查人民委员部由同一人领导），与卡内“斯大林首任人民委员”需消歧：站内 [`PER-stalin` L26](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-stalin.md#L26) 写“1920–1922兼掌工农检查院”，卡内应写“RKI 首任人民委员，自前身国家监察人民委员部延续而来”。
- **修复**：T3.1 增补 Carr ch09/ch07 与 `RN-W23` 定位；T3.2 将“起始日不能视为已验证”改写为“起始日据 Carr 记 VTsIK 1920-02-07 法令；仅公布与施行细节待核”。

#### 01-02｜P1｜“1920年中央监察机构初步设立”表述超前，且与站内可核材料不对位
- **定位**：[`L27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rabkrin-and-ccc.md#L27)。
- **核证**：站内 Carr `RN-W35`（[L71](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr_bolshevik_rev_v1_zh/RN-W35-carr-lenin-party-instrument-and-soviet-constitution-1917-1923.md#L71)）把“十一大（1922）中监委与格别乌协作→十二大（1923-04）扩大至 50 人并与工农检察院合并”列为时间线，未支持“1920年已设**中央**监察机构”。依通行党史（需外部核对，站内无强锚点），1920年九次代表会议（9月）只决定设**地方**监察委员会，中央监委由1921年十大选出。卡内“1920年中央监察机构初步设立”易让读者把 1920-02-07 的**国家**法令与党内机关同源化——这恰是卡自己反对的“同一次法律创设”。
- **修复**：改为“1920年九次代表会议提出党内监察委员会设想（地方层级）；中央监察委员会的制度化以1921年十大与1923年十二大为节点，具体条文待核”，并在边表增加 `MTG-1921-rcpb-10th-congress`。

#### 01-03｜P1｜漏接站内会议卡与概念卡，且回避 Carr/Lewin 的“合并”叙事（学派／术语失衡）
- **定位**：[`L22`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rabkrin-and-ccc.md#L22)、[`L33–40`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rabkrin-and-ccc.md#L33-L40)、[`L43`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rabkrin-and-ccc.md#L43)。
- **核证**：
  1. 列宁原文（marxists.org，已实测 200）明言：“The Central Control Commission should be combined with the main body of the reorganised Workers' and Peasants' Inspection… I propose that the Congress should elect 75 to 100 new members… such a union of the Workers' and Peasants' Inspection with the Central Control Commission…”，并主张中央全会与中监委联席、每两月一次——这是**列宁自己提出的“合并/联合”设想**。卡内只写“紧密结合”，未给出“75–100名”“联席全会”这两个可核数字，也未交代“设想合并 vs. 实际合署不合并”之间的落差。
  2. 站内 Carr（[`RN-W23` L48](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr_bolshevik_rev_v1_v2/RN-W23-carr-party-state-constitution-and-economic-order-1917-1923.md#L48)、`RN-W35` L71）、Lewin（[`RN-W1` L100](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/lewin_1968_last_struggle/RN-W1-testament-and-cooperation.md#L100)：“unique super-commissariat”）、[`CON-thermidor-and-bureaucracy` L44](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-thermidor-and-bureaucracy.md#L44) 均用“合并”表述；而 [`PER-ordzhonikidze` L26](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-ordzhonikidze.md#L26) 与本卡强调“合署、未合并”。库内**同一制度在不同卡里“合并／合署”并存**，本卡 2.3 只说“共识”而未显式标注 Carr/Lewin 用法与“法律上未合并”的分层。
  3. 站内已有但本卡未链接：[`MTG-1923-04-12th-party-congress` L28](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1923-04-12th-party-congress.md#L28)（十二大扩大中央委员会与 CCC–RKI 编制）、[`MTG-1922-03-11th-party-congress`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1922-03-11th-party-congress.md)、`CON-thermidor-and-bureaucracy`，以及 Carr 论断卡 [`CLM-carr-1950-politburo-orgburo-displacement-of-state-organs`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1950-politburo-orgburo-displacement-of-state-organs.md)（“党吸收国家”）。2.3 光谱仅 Lewin／Khlevniuk／Apalkov，缺 Carr 的“党国融合”论与托洛茨基—德意志派“官僚化”论（`DEB-1922-lenin-testament-and-stalin-rise` 中已有）。
- **修复**：
  1. 2.1 第三条增补：“列宁设想中监委新增 75–100 人并与改组后的 RKI 主体合并、全会与中监委联席（marxists.org 1923/jan/23）；十二大实行的是扩大中监委、共同领导、负责人兼任，二者仍为党／国两套法定机构（组织合并说见 Carr、Lewin 用语，需分开标注）”。
  2. 2.2 边表增加：`MTG-1923-04-12th-party-congress`（`implemented_reorganization`，1923.04）、`MTG-1922-03-11th-party-congress`（`context`，1922.03–04）、`CON-thermidor-and-bureaucracy`（`diagnosed_in`）；2.3 光谱补入 Carr 一栏并链接 CLM。

#### 01-04｜P1｜边表任职窗口与站内人物卡口径不齐，且“待核”仍挂在站内已有锚点上
- **定位**：[`L36–38`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rabkrin-and-ccc.md#L36-L38)、[`L14`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rabkrin-and-ccc.md#L14)。
- **核证**：`PER-ordzhonikidze` 已记 `1926-11-03` 联席全会任命并至 1930 年底分项卸任；`PER-kuibyshev` L20 记 1923–1926 执掌，且 `1926年8月` 转任 VSNKh（与 `INS-gosbank-and-narkomfin` “古比雪夫1926年起”口径一致）。因此古比雪夫离任（1926-08）与奥尔忠尼启则接任（1926-11-03）之间存在约三个月交接期，边表 “1923–1926 / 1926–1929” 掩盖了这一缝隙；`perspectives_missing` 里的 `precise-dual-office-appointments` 在站内已有半数答案。边表 `PER-stalin` “早期任命档案待核”亦可直接引 Carr（01-01）。
- **修复**：边表改为 `PER-kuibyshev 1923.04–1926.08`、`PER-ordzhonikidze 1926.11.03–1930.11（本卡截至1929）`，并在注中写明交接期未覆盖；`perspectives_missing` 调整为 `regional-inspection-case-files`、`rabkrin-staff-statistics`。

#### 01-05｜P2｜外链与 Schema
- 站内 `sources/web-archive/` **没有**《怎样改组工农检查院》《宁肯少些，但要好些》（仅有 [`1923-01-04_on-cooperation.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E10_core_classics/1923-01-04_on-cooperation.md)），本卡正确地使用了 marxists.org 两个外链（实测 200，Written: January 23, 1923；*Pravda* No. 16, January 25, 1923）。建议将两篇入库为 S 级 web-archive 条目（卡内同时标注“口述1月23日，刊发1月25日”，现卡仅写口述日）。
- 边表“核心依据”仍有 `列宁两篇文章`“早期任命档案待核”等笼统写法，宜落到 `Carr ch09`、`Apalkov ch07` 页码。
- `related_debates` 仅 `DEB-1922-lenin-testament-and-stalin-rise`，可增 `DEB-1923-nationality-and-empire`（十二大／格鲁吉亚事件背景，经 [`MTG-1923-04`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1923-04-12th-party-congress.md) 已用）。

---

### 02｜财政人民委员部与国家银行（`INS-gosbank-and-narkomfin`）

**结论**：币值统计口径严谨——明确“价值占比≠张数占比”，且与 DATA-02 数据卡逐项吻合；反对把 1930 年结算制度回填 1929，也把 Katasonov 的“大坝”标为作者比喻，学派自觉良好。问题集中在：一个无法校验的外链、站内 L3／数据卡中更硬的锚点未被利用、统计口径的“分母混用”风险。

#### 02-01｜统计口径复核（通过，附口径提示）
- **核验**：卡 L48 “约1923年1月3%、7月37%、11月80%”与 [`DATA-02` L87–89](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-02-1922-1924-scissors-crisis-and-chervonets.md#L87-L89) 一致：`3.5/116.5 = 3.0%`、`70/188 = 37.2%`、`1923-11` “four-fifths”（Carr p.140）。`1切尔沃涅茨 = 10金卢布 = 7.74234 克纯金` 与 DATA-02 L83、Katasonov `RN-W32` 一致。**数值无误。**
- **P1｜分母不一致未提示**：1月、7月两档是 Yurovsky 口径“折合金卢布的总值占比”（分母＝切尔文＋苏维埃纸币的金卢布折值，DATA-02 L87–88），而 11 月“约 80%”是 Carr 的 *four-fifths* 叙述性表述（L89 自注“月度张数未单列”）。卡 L48 把三点写成同一系列的“占流通纸币总价值”，易让读者当作同一分母的三点时间序列。**修复**：卡 L48 改为“1923-01、1923-07 为 Yurovsky/Carr 折金卢布总值占比；1923-11 为 Carr 叙述性‘约五分之四’，不可与前两档算同一分母的增幅”。

#### 02-02｜P1｜`istmat.org/node/40879` 无法完成 TLS 握手，且是“1920-01-19 撤销人民银行”唯一实证锚点
- **定位**：[`L28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-gosbank-and-narkomfin.md#L28)、[`L50`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-gosbank-and-narkomfin.md#L50)。
- **核证**：本审计环境 GET 返回 “The SSL connection could not be established”，其余 7 个外链均 200。无法证实站点失效，但**该日期（1920-01-19）与“业务移交财政人民委员部所属中央预算结算机关”在站内无任何 S/A 级交叉印证**（站内 Carr 卷1／卷2 与 Katasonov 札记未收该法令）。**升级条件**：若人工复核确认 404／长期不可达，则升格为 P0（失效外链）。
- **修复**：①复核 istmat 链接；②为该法令另配一个备用档案（如 `consultant.ru`／俄罗斯央行史页），或在 T3.2 明示“日期据 istmat 转录，站内无独立印证”；③在 `sources/web-archive/` 补入该法令（S/A 化）。

#### 02-03｜P1｜漏用站内 L3 与 DATA-02 中更硬的锚点（1917 接管、1924 币改比率、黄金储备）
- **定位**：[`L27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-gosbank-and-narkomfin.md#L27)、[`L29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-gosbank-and-narkomfin.md#L29)、[`L54`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-gosbank-and-narkomfin.md#L54)。
- **核证**：
  1. **1917 接管**：卡称“逐日过程待查原始法令”。站内 L3 已有：[`1917-10_october_insurrection` L174](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-10_october_insurrection.md#L174)（`1917-10-26 [O.S.]` 约 02:00 起国家银行与车站、发电站等被赤卫队接替）与 [`1917-11_vikzhel…` L108](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md#L108)（国家银行宣告已向原临时政府划拨 6.1 亿卢布并拒绝与苏维埃合作，Rabinowitch 2007 / Pipes 为据）。这正是“权力接管≠日常运作恢复”的站内实证，卡内却只作泛述。
  2. **1924 币改硬数据**：[`L3 1924-01` L79](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1924-01_lenin_death_testament_and_lessons_of_october.md#L79) 与 DATA-02 L55 给出 `1924-02/03` 停印苏维埃纸币、1/3/5 卢布国库券、`10 卢布国库券 = 1 切尔文涅茨`、`50,000:1` 收兑 1923 年版纸币（= 500 亿旧卢布:1，Carr pp.141–142）。卡 L29 仅写“1924年改革收兑旧纸币”。
  3. **黄金／外汇储备**：DATA-02 L97–98 `1923-01-01 ≈ 1500 万金卢布 → 1924-01-01 ≈ 1.5 亿金卢布`（Carr p.140）；Katasonov 札记 [`RN-W32`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/katasonov_stalin_economy_zh/RN-W32-katasonov-trade-monopoly-chervonets-and-two-circuit-ruble.md) 提供 `1922-04-04`、`1922-07-27` 居民与机构上缴贵金属外汇规则，`1925-01` 总储备 3.44 亿（其中贵金属账值 1.806 亿）、`1927-07-01` 2.691 亿、`1929-10-01` 信贷机构 1,312 家，并自带**内部不一致警示**（1924 年初 1.95 亿 vs 2.13 亿 vs 2.135 亿；1926-01 售金币 7,600 万折约 58.8 吨 vs 书称约 6 吨）。卡 L43 虽称“Katasonov 不能单独作硬数据”，但未把这些**札记已标出的口径冲突**搬进 T3，读者无从判断“稳币”与“储备走低”的量级。
- **修复**：T3.1 增补以上 3 组站内锚点与页码；L29 改为“`1924-02/03` 停印苏维埃纸币，国库券与切尔文固定为 10:1，50,000:1 收兑 1923 年版纸币（Carr pp.141–142；DATA-02）”；T3.1 另列一行“储备数字口径冲突（RN-W32）”。

#### 02-04｜P1｜Narkomfin 人事链条缺 1917–1921 段，边表窗口与 `PER-sokolnikov` 不一致
- **定位**：[`L29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-gosbank-and-narkomfin.md#L29)、[`L37`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-gosbank-and-narkomfin.md#L37)。
- **核证**：[`PER-sokolnikov` L26](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sokolnikov.md#L26)：`1922-01` 任苏俄财政副人民委员并实际主持部务（克列斯廷斯基驻外），`1922-11` 任苏俄财政人民委员，`1923-07-06` 至 `1926-01-16` 任苏联财政人民委员。本卡边表仅写“1922–1926”，且正文自 1917 至 1922 完全不出现任何 Narkomfin 首长（站内 `PER-sokolnikov` 已点名克列斯廷斯基）。对一张以“财政人民委员部”为名的机构卡，这是**制度史主线缺口**。另本卡 L31 “索科利尼科夫1926年离任”与 `1926-01-16` 一致，但 YAML／边表建议写具体日。
- **修复**：2.1 第一段补 1917–1921 年历任首长（须据 `PER-krestinsky` 若已建卡或外部权威名录核实，当前站内仅有 Krestinsky 驻外一句，标“待核”）；边表窗口改为 `1922.11–1926.01.16`（苏俄/苏联分段 `1923-07-06`）。

#### 02-05｜P2｜Schema 与措辞
- YAML `start_ns: 1917-11-08` 实为 `1917-10-26 [O.S.]` 接管起点，建议在 T3 用 O.S./N.S. 并列注明；`end_ns: 1929-12-31` 为本卡范围终点，宜在 T3.2 再声明一次（卡内仅在 3.2 末句隐含）。
- `perspectives_missing` 中 `bank-balance-sheet-archival` 实际可由 DATA-02 与 RN-W32 部分补足，宜改为“年度分行资产负债表”。
- 学派光谱仅 Carr／Davies／Katasonov；缺 Nove、Erlich（站内 [`reading-notes/erlich_1960_industrialization`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/erlich_1960_industrialization/RN-W3-industrialization-models-and-constraints.md)）的工业化信贷约束视角，以及 Gosbank 自身年报（S 级一手）。可作 P2 补充。

---

### 03｜俄社民工党第四次（统一）代表大会（`MTG-1906-04-rsdlp-4th-stockholm-congress`）

**结论**：历法与票数口径**全部正确**，并明确不把“剩余票数硬分给两派”、不把“党章第8条”等同于后来党国制度；T3 一手章程档案精准。主要问题是史学多元性几乎空白（光谱无具名学者），且遗漏站内 A 级专著中更关键的“大会决议内容”。

#### 03-01｜核验通过项（无需修复）
1. **双历**：`1906-04-23—05-08 [N.S.]` 与俄历 `04-10—04-25`（+13）无误，会场瑞典用公历的说明（T3 L44）合规；
2. **票数**：`112 有表决权 + 22 发言权`、`孟什维克62／布尔什维克46` 与站内 S 级档案 [`1906-04…rules.md` L125](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E03_E08_party_and_state_docs/1906-04_rsdlp-fourth-stockholm-congress-rules.md#L125)（转引 `《列宁全集》第13卷注〔2〕`）一致；`62+46=108≠112`，卡正确声明“剩余票数不硬分”；
3. **章程条款**：§1、§2、§3、§8 对照档案 L37–L55 全部一致；T3 对“通过本 vs 列宁会前草案”的区分（档案 L121）转述准确。

#### 03-02｜P1｜票数“分母”仍缺一层：108 与 112 之间的 4 票及民族组织票的归属未说明
- **定位**：[`L25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1906-04-rsdlp-4th-stockholm-congress.md#L25)、[`L35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1906-04-rsdlp-4th-stockholm-congress.md#L35)。
- **核证**：卡在 L27 又称波兰、拉脱维亚社民党与崩得“达成加入统一党的安排”，但未说明这些组织的表决权代表是否已计入 112、以及“孟62／布46”是否含崩得等民族组织代表。站内档案亦只给 62/46，没有分项明细。**该口径冲突是 112 的分母问题，不是计算错误**。
- **修复**：T3 增一条“**分母提示**：62+46=108，与 112 差 4；民族社民组织（波社民、拉社民、崩得）代表是否计入 112/62/46，站内档案未分项，待《代表大会记录》或 Lenin CW 13 注〔2〕全文核对；本卡不得据 62:46 推断任何单项议题的比数”。2.2 边表 `ORG-mensheviks` 行同步注明。

#### 03-03｜P1｜漏接站内 A 级专著中的大会决议内容（武装行动／“剥夺”决议），并遗漏 §1 恢复列宁公式的反直觉事实
- **定位**：[`L25–28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1906-04-rsdlp-4th-stockholm-congress.md#L25-L28)、[`L45–46`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1906-04-rsdlp-4th-stockholm-congress.md#L45-L46)。
- **核证**：
  1. [`daniels_1960_conscience/ch01_pages_26-50.md` L416–423](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/daniels_1960_conscience/ch01_pages_26-50.md#L416-L423)：“The Stockholm congress voted down the Bolsheviks' unconditional defense of the partisan units and condemned the expropriations and acts of violence against private citizens”，并引布尔什维克“不会让统一的观念在我们脖子上套上绞索”的回应——这直接支撑卡内“形式统一并未消除派别网络”，但卡内**零引用**；
  2. 站内 S 级档案 L25：1906 年第1条“改回列宁的成员公式”（承认纲领、物质支持、加入一个组织），**由孟什维克占多数的大会通过**，而 1903 年通过的是马尔托夫公式。此事是对 `DEB-1903-bolshevik-menshevik-split` 的最强站内反证，卡内只写“第1条要求党员加入党的一个组织”，却没有点出这一回摆；档案 L29 还记大会以“多余而不言自明”为由否决了布尔什维克附在第1条的注释，亦未被利用；
  3. [`carr_bolshevik_rev_v1_zh/ch04…` L994–998](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/carr_bolshevik_rev_v1_zh/ch04_第一部分_列宁与_工具.md#L994-L998)（A 级）：斯德哥尔摩统一大会“在十月宪法和第一届杜马产生的乐观情绪达到高潮时召开，因此孟什维克占据了多数”，是对 62:46 多数成因的 A 级解释，卡内无；
  4. [`haimson_2005_experience/ch04…` L149](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/haimson_2005_experience/ch04_part_i_lenin_martov_and_the_issue_of_pow.md#L149)（A 级）记 Dan、Martynov 在斯德哥尔摩被普列汉诺夫与阿克雪里罗德训斥后公开悔过“革命的过激”——**但原文把大会时间误写为 “June 1906”**（实为 4 月 23 日—5 月 8 日 [N.S.]）。此错误**不在卡内**，但将来若据 Haimson 增补，必须标注该书时间有误，不可连带污染 YAML。
- **修复**：T2 增一条“**武装行动与剥夺决议**”（引 Daniels ch01 L416–423）、一条“**第1条回到列宁公式**”（引档案 L25/L29，并链接 `DEB-1903-bolshevik-menshevik-split`）；2.3 增列“Carr：杜马乐观主义成就孟什维克多数”与“Daniels：统一的纪律与财政裂缝”两个具名视角；T3.2 增加“Haimson 2005 ch04 误作 1906 年 6 月”提示。

#### 03-04｜P1｜2.3 史学光谱无任何具名学者，且土地方案无站内锚点
- **定位**：[`L26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1906-04-rsdlp-4th-stockholm-congress.md#L26)、[`L40`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1906-04-rsdlp-4th-stockholm-congress.md#L40)。
- **核证**：2.3 只对立“长期思想分歧解释 vs 共同社民传统解释”，却不指名任何学派（苏联党史、孟什维克流亡史家 Dan/Getzler、西方 Daniels／Carr／Haimson）；`perspectives_present` 仅有 `party-rules-primary`、`factional-political-history` 两个标签而无任何论断卡。土地方案（马斯洛夫／普列汉诺夫的地方自治化 vs 列宁国有化）L26 同时没有任何注或引文——卡内自白“具体投票细目仍须对读大会记录”，但没有给出 Lenin CW 10 等站内可及文本。站内已有 [`galili`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/galili_1989_menshevik_leaders)、[`getzler_1967_martov`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/getzler_1967_martov) 札记可补孟什维克视角。
- **修复**：2.3 增 3 个具名视角（Daniels 的派别纪律、Carr 的杜马乐观主义、Getzler/Galili 的孟什维克多数立场），`perspectives_present` 增 `western-party-history`、`menshevik-memoir`；土地议案增加“无站内一手文本；Lenin CW 10 土地纲领修订待入库”的显式提示，并考虑把 `DEB-1906-stolypin-wager-and-agrarian-viability` 作为 `related_debates` 第二项。

#### 03-05｜P2｜Schema 与措辞
- T3 L44 “仅作印刷口径说明”宜改为“俄历对照：1906-04-10—04-25 [O.S.]（印刷文献口径）”，避免被读者当成另一套机器日期。
- 卡无 H1 标题行，且与 01/02 号卡（CRLF）相比为 LF 换行——不影响解析，但应与同批卡统一。
- 边表中 `PER-lenin` “土地议案细票待核”为悬空尾句，可改为“无站内一手文本；Lenin CW 10 待入库”。

---

### 04｜俄共（布）第七次全国代表会议（`MTG-1917-04-7th-april-party-conference`）

**结论**：双历正确、结构上不把会议路线等同于“立即武装夺权”、也不把《四月提纲》当作会议决议——这些都对。最大问题是：**站内 A 级一手汇编（Loginov）与 L3 时间线已有精确票数和代表数，卡内却全部写成“待复核”**；且对 Zimmerwald 表决的描述含糊，掩盖了列宁在会上败北的关键事实。

#### 04-01｜P1｜表决票数、代表数、中央选票全部“待核”，但站内 Loginov（A 级）与 L3 已有完整数字
- **定位**：[`L20`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1917-04-7th-april-party-conference.md#L20)、[`L27–28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1917-04-7th-april-party-conference.md#L27-L28)、[`L46`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1917-04-7th-april-party-conference.md#L46)。
- **核证**（站内 A 级，中译待核校；均转引会议记录）：
  - [`loginov…ch09_part_3` L590](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/loginov_lenin_in_1917_zh)：约 **8 万党员、152 名代表**；
  - [`ch10_part_4` L73–74](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/loginov_lenin_in_1917_zh)：民族自决议案 **56 赞成／16 反对／18 弃权**；
  - 同章 L376：列宁《关于当前形势》决议 **71 赞成／39 反对／8 弃权**；另据 L94，针对临时政府态度的决议**仅 3 票反对、8 人弃权**，加米涅夫的“监督”方案被否决；
  - 同章 L575–579（**109 名代表无记名投票**）：列宁 104、季诺维也夫 101、斯大林 97、加米涅夫 95、米柳京 82、诺根 76、斯维尔德洛夫 71、斯米尔加 53、费奥多罗夫 48；候补首位 Fedorovich 41、Bubnov 32；
  - L3 [`1917-04_lenin_arrival…` L264、L280](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-04_lenin_arrival_april_theses_and_milyukov_note.md#L264)（`71:39:8`、`56:16:18`、`1:8`、“九人中央仍留四名温和派”）与脚注 `[^LOG9][^LOG10]`。
- **内部矛盾**：T1 已把“约8万党员”写成事实，T3 L46 却又将其降级为“待复核的编纂线索，不冒称已由一手文本确认”。站内 Loginov 已确认代表数（152），应上调为 **A 级（Loginov 转引会议记录）**。
- **修复**：
  1. T1 / T2 2.1 将“约8万党员”改为“约8万党员、152名代表（Loginov，转引会议记录）”；
  2. 2.1 增补：当前形势决议 71:39:8、对临时政府态度仅3票反对8人弃权、民族自决 56:16:18、九人中央选票（上列数字）；
  3. T3 L46 改为“票数与选票据 Loginov（A级，中译待核校）与 L3；原始速记仍待核，数字口径为转引”，并链接 L3 与 Loginov ch09/ch10 定位。

#### 04-02｜P1｜Zimmerwald／国际问题表述含糊，掩盖“列宁在会上败北”这一多元性的最硬证据
- **定位**：[`L27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1917-04-7th-april-party-conference.md#L27)。
- **核证**：卡写“代表对立即创立新社会主义国际亦有保留”。Loginov [`ch10_part_4` L59–63](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/loginov_lenin_in_1917_zh) 实际记载：列宁坚决反对俄社民工党参加有欧洲“中派”的齐美尔瓦尔德派国际会议，**该主张被代表们否决，“决议以全票反对（仅列宁一人赞成）”通过**；L3 L280 称之为 `1:8` 孤立。这与卡内“列宁路线取得多数”的总叙述有重要差异——卡 2.3 自称强调 `intraparty-pluralism`，却没有把这一最直接的反例写出来；“对立即创立新国际有保留”的措辞也容易与列宁“建立第三国际”的另一议题混淆。
- **修复**：改为“在齐美尔瓦尔德国际会议参加问题上，列宁主张退出／不与中派同席，但多数代表否决（据 Loginov，仅列宁一人赞成；L3 记 `1:8`），说明会议并非‘投票机器’”，并注明二手口径差异待速记核。

#### 04-03｜P1｜史学光谱失衡：2.3 用稻草人式“传统党史”，具名学派未用站内 A/B 级对读
- **定位**：[`L40`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1917-04-7th-april-party-conference.md#L40)。
- **核证**：2.3 把“传统党史强调列宁路线取得统一”与 Rabinowitch 对立，但前者无任何具名来源；站内 L3 [L280](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-04_lenin_arrival_april_theses_and_milyukov_note.md#L280) 已建成的五学派对照（Trotsky ch17 “列宁以超凡意志压倒温和派”；Haimson 2005 对列宁—加米涅夫—李可夫的理论对峙；**Loginov 以会议记录反驳“投票机器”**；Rabinowitch 的 CC/PK/MO 并行；Sukhanov/Pipes 的“海外精神中心／离开列宁便失魂”）可直接改写为卡内光谱。本卡仅用 Rabinowitch 一个具名学者，且其论断（`CLM-rabinowitch-1976-open-democratic-mass-party`）关注的是 1917 年全年而非本会议；站内 [`rabinowitch_1968_prelude_zh/ch04_2斗争开始.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/rabinowitch_1968_prelude_zh/ch04_2%E6%96%97%E4%BA%89%E5%BC%80%E5%A7%8B.md)（A 级，彼得格勒 PK 与四月危机）完全未引。
- **修复**：2.3 改写为 Trotsky／Haimson（列宁主导论）—Loginov／Rabinowitch（多元论）—Pipes／Sukhanov（列宁中心论）的三栏对照，并链接 L3 `L280`；`perspectives_missing` 增 `post-soviet-minutes-based`。

#### 04-04｜P1｜漏接“四月危机”（米留可夫照会）前置语境，且 `related_debates` 为空
- **定位**：[`L15`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1917-04-7th-april-party-conference.md#L15)、[`L25–26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1917-04-7th-april-party-conference.md#L25-L26)。
- **核证**：会议开幕（`04-24 [O.S.] / 05-07 [N.S.]`）距米留可夫照会引发的“四月危机”（`04-18—04-21 [O.S.]`，L3 `L281`）仅 3 日；L3 记载列宁在 24 日会上斥 PK 左翼 21 日“打倒临时政府”传单为冒险主义，并自称“和平侦察”（反驳 Pipes 的“未遂政变”论）。卡 2.1 称“不能等同于会议已决定立即武装夺权”，却没有给出这一最直接的同时期证据。`related_debates: []` 空缺，站内 [`DEB-1917-dual-power-and-february-origins`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md) 与 [`DEB-1917-october-coup-or-social-revolution`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md) 均直接相关。
- **修复**：`related_debates` 增上述两项；2.1 第一条补“会议紧随米留可夫照会危机（04-18—04-21 [O.S.]），列宁在会上斥责‘冒险主义’并提‘和平侦察’”，并在 T3 链接 L3 与 [`1917-04_lenin_arrival…`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-04_lenin_arrival_april_theses_and_milyukov_note.md)。

#### 04-05｜P2｜Schema 与措辞
- 中央委员会五人名单后的“九人名单及票次仍应复核”已可用 04-01 的 Loginov 数字补全为完整九人；候补委员亦可写。
- `perspectives_present: ["april-theses-primary","intraparty-pluralism"]` 实际无任何具名学者论断卡（仅 Rabinowitch 一张），标签应与实际可链条目对齐。
- 边表 `PER-kamenev` 行“会议速记待核”可改为“Loginov ch10 L94：监督方案被否；加米涅夫自认与列宁仅一处分歧”。
- 卡缺 H1 标题行且换行符为 LF（同 03-05）。

---

## 四、阶段一汇总

| 卡 | P0 | P1 | P2 | 要点 |
| :--- | :--: | :--: | :--: | :--- |
| 01 `INS-rabkrin-and-ccc` | 0 | 4（01-01 至 01-04） | 1 | Carr 已核 `1920-02-07`；“1920中央监察机构”表述超前；漏接十二大/十一大卡；“合并”术语分歧未标注 |
| 02 `INS-gosbank-and-narkomfin` | 0（istmat 如确认失效升 P0） | 3（02-01 分母、02-02 外链、02-03、02-04 实为 4 项中 3 项 P1 + 02-01 子项） | 1 | 币值数字全部与 DATA-02 吻合；漏用 L3 1917/1924 与储备数据；缺 1917–21 Narkomfin 首长 |
| 03 `MTG-1906-04` | 0 | 3（03-02 至 03-04） | 1 | 历法与 62:46 完全正确；缺武装行动决议、§1 回到列宁公式、具名史家；Haimson 2005 误作 6 月 |
| 04 `MTG-1917-04` | 0 | 4（04-01 至 04-04） | 1 | 历法正确；71:39:8 / 56:16:18 / 九人票次 / 152 代表站内均有，却写“待核”；Zimmerwald 列宁败北被掩盖 |

> 阶段二（05–07 与汇总修复矩阵）将追加于本文件之后。

---

## 五、历法与日期复核表（后半批 05–07）

| 卡片 | 卡内日期（YAML／正文） | 复算 | 判定 |
| :--- | :--- | :--- | :--- |
| `MTG-1918-07-5th-congress-of-soviets` | `1918-07-04—07-10 [N.S.]`；米尔巴赫遇刺 `07-06`；宪法通过 `07-10` | 全部在 1918-02-14 改历后，纯公历；与 S 级档案 [`1918-07-10_rsfsr-constitution…`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E03_E08_party_and_state_docs/1918-07-10_rsfsr-constitution-franchise-and-power.md) 的 `written_date_os: null` 及“1918年2月1日（14日）已改用公历”一致 | **合规** |
| `MTG-1922-03-11th-party-congress` | `1922-03-27—04-02 [N.S.]`；总书记 `1922-04-03` | 纯公历；站内 L2 [`E08` L36](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L2_chronicles/E08_1921-1924_nep_and_lenins_last_struggle.md#L36) 同样记 `03-27—04-02` | **合规**；但 `04-03` 被卡自标“待核”而站内多处已证实，见 06-01 |
| `POL-october-manifesto-and-1906-fundamental-laws` | `1905-10-17 [O.S.] / 10-30 [N.S.]`；`1906-04-23 [O.S.] / 05-06 [N.S.]`；`04-26 / 05-09`；`1907-06-03 [O.S.] / 06-16 [N.S.]`；`1917-03-02 [O.S.] / 03-15 [N.S.]` | 5 组全部 +13，换算无误；YAML `1905-10-30` 与 `1917-03-15` 为公历机器日期 | **换算合规**；`1907-06-02/03` 站内口径有一日之差，见 07-02 |

> 节点 ID 与 `related_debates` 在 7 张卡中**全部真实存在**（1.1 节）。后半批三卡无断链；外链：`prlib.ru/history/619222`（标题“Утверждены «Основные государственные законы Российской империи»”）、`nnov.hse.ru/…fundgoszak1906`（含第 87 条原文）与 Cambridge 页均 200，内容与卡内引用吻合。

---

## 六、后半批逐卡审计与修复方案（05–07）

### 05｜第五次全俄苏维埃代表大会（`MTG-1918-07-5th-congress-of-soviets`）

**结论**：全卡最严谨的一张——明确拒绝把“399”当作伪造证据、拒绝把拘押人数硬写成 450、不把宪法第25条算成“五倍票值”，且 S 级宪法档案逐点吻合。主要问题：①站内 L3 与论断卡仍带着本卡已纠正的旧口径，本卡未标注这一库内冲突；②统计分母缺失；③史学光谱只有 Rabinowitch 一家。

#### 05-01｜P1｜统计分母缺 1,035 与“其余 88”；“399”与“678”的集合关系需精确表述
- **定位**：[`L25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1918-07-5th-congress-of-soviets.md#L25)。
- **核证**：Rabinowitch [`ch17` L214–222](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/rabinowitch_2007_in_power/ch17_11_the_suicide_of_the_left_srs.md#L214-L222)：“Bolsheviks, 678, and Left SRs, 269. The remaining 88 delegates were divided among [SR] Maximalists (roughly 30), Social-Democratic Internationalists (5–6), and unaffiliated delegates (about 48), for a total of 1,035 delegates with full voting rights”；并写明这批数字“have never been independently investigated”。L243：这些统计“did not include roughly 399 Bolshevik delegates whose right to be seated was challenged”。可见：
  1. 卡只给 678/269，**遗漏 88 与总数 1,035**（678/1,035 ≈ 65.5%，269/1,035 ≈ 26.0%——此为审计员按原书数字换算，卡内可标“据 Rabinowitch 数字换算”）；
  2. Rabinowitch 的措辞是“**统计未包含**约399名被质疑者”，而 L3 [`L24`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1918-07_left_sr_uprising_and_red_terror_launch.md#L24) 写成“**布尔什维克突增约 399 张问题证书达 678 席**”（即 399 被当作 678 的子集），两者集合关系相反。本卡写“质疑约399名布尔什维克代表的资格”并声明“不能从公布人数中机械扣减”，**与 Rabinowitch 兼容，但没有交代 399 与 678 是否重叠**。
- **修复**：L25 增补：“预报分布：布 678、左 269、其余 88（最高纲领派约 30、社民国际派 5–6、无党派约 48），表决权代表合计 1,035（Rabinowitch p.288；作者自称从未经独立核查）；约 399 名被质疑的布尔什维克代表**不在上述预报统计之内**（原书措辞），其与 678 的集合关系须核原书页码，不得据 L3 写作‘678 含 399’。”

#### 05-02｜P1｜库内旧口径未标注：L3 与 Carr 论断卡同“城乡 1:5”“舞弊格局”“一党专政法典化”冲突
- **定位**：[`L25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1918-07-5th-congress-of-soviets.md#L25)、[`L43–44`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1918-07-5th-congress-of-soviets.md#L43-L44)。
- **核证**：卡 T3 已自述“部分旧札记将399人强化为伪造证件，须按原书与审计纠正”，但未指明哪些库内文件仍留有旧口径。本审计定位：
  - [`L3 1918-07` L7、L24、L40](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1918-07_left_sr_uprising_and_red_terror_launch.md)：“舞弊格局”“问题证书达 678 席”“城乡 **5:1** 不等选举权写入；**一党专政法典化**”。S 级档案 L28 明示：城市分母是**选民**、农村分母是**居民**，不是同口径比；Rabinowitch p.296 表述亦为“electors”（与宪法条文“居民”略有出入，以宪法原文为准）；宪法并无“一党”条款，Rabinowitch（L492–502）只说宪法“perpetuated the fiction”苏维埃大会是最高机关而 Sovnarkom 在实践中占上风、并在 CEC 中“排除”孟/社/左翼社革党；
  - [`CLM-carr-1950-1918-constitution-fusion-of-powers-and-class-franchise` L18](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1950-1918-constitution-fusion-of-powers-and-class-franchise.md#L18)：“城乡 **1:5** 不平等代表权”。
  这些文件均为站内 A/B 级材料，**不在本次写入范围**，但本卡引文冲突会被读者在图谱 1-hop 中同时看到。
- **修复**：①本卡 T3 增列“库内待统一口径”小节，点名 L3 L7/L24/L40 与 CLM-carr 的 1:5 表述，指向宪法 S 档案 L28 与 Rabinowitch L492–532；②向 L3 与 CLM 的维护者另行提交修订（由编纂线执行，非本审计写入）；③边表增列 `CLM-carr-1950-1918-constitution-fusion-of-powers-and-class-franchise`（`compared_with`）与 `CLM-rabinowitch-2007-left-sr-coalition-collapse`。

#### 05-03｜P1｜史学光谱单极化（仅 Rabinowitch 修正派），漏接站内 Pipes／Leggett／Carr 与现成论断卡
- **定位**：[`L13`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1918-07-5th-congress-of-soviets.md#L13)、[`L38–39`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1918-07-5th-congress-of-soviets.md#L38-L39)。
- **核证**：2.3 只有“苏维埃政府当时定性为起义”与“Rabinowitch：目的是迫使改变政策而非夺权”两极；`perspectives_present` 的 `archival-revisionist` 实指一人。站内 [`DEB-1918-red-terror-and-civil-war-origins`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L8) 的五派（Pipes/Figes、Rabinowitch、Leggett/Ratkovsky、Hoffmann、Mawdsley）与 `CLM-pipes-1990-red-terror-leninist-logic`、`CLM-leggett-1981-*` 均可对读；L3 脚注 `[^PIP27][^LEG71][^RAT07]` 已涉及：左翼社革党被清出契卡、Aleksandrovich 等 12 名参变契卡人员被处决、彼得格勒 161 人皆无阴谋（L3 L38、L54）。本卡对这些**同一事件的后果链**（契卡内部左翼否决机制消失）全无着墨，导致“联盟终结”只剩议会层面。
- **修复**：2.3 增“**Pipes／Figes 一派**：把 7 月事件置于布尔什维克一贯排除对手的逻辑中（`CLM-pipes-1990-red-terror-leninist-logic`）”与“**Leggett 一派**：以契卡内部左翼被清除视为制度转折（`CLM-leggett-1981-red-terror-institutionalization`）”两行，并将 `EVT-1918-09-red-terror-and-left-sr-rupture` 加入边表（`consequence_in`）；`perspectives_present` 与实际可链论断卡对齐。

#### 05-04｜P2｜拘押人数细节、Schema 与措辞
- 拘押细节：Rabinowitch L466–472：左翼社革党党团被塞进大剧院楼上两间屋，**13 名“主犯”送克里姆林牢房，约 100 人获释，余者羁押于亚历山德罗夫军校并陆续释放**；资格委员会中的左翼社革党人至大会结束才获释。卡 L26 只写“部分人员获释”，可补入这三个可核数字（“400 余”与“450”的区分继续保留）。
- 刺杀当日的“捷尔任斯基被波波夫支队扣押”（L3 L32）卡内未写；作为武装冲突的关键细节可补一句。
- 边表 `PER-spiridonova` 行“`AUD-14`”依据可落到 Rabinowitch 页码；`ORG-cheka-ogpu` 行“刺客…与契卡机构相联系”建议具体写成“波波夫的契卡战斗支队”。
- 卡缺 H1 标题行、LF 换行（同 03-05）。

---

### 06｜俄共（布）第十一次代表大会（`MTG-1922-03-11th-party-congress`）

**结论**：对 Daniels 的使用极为审慎（正确区分 1921 年中委会“差一票”与 1922 年大会；指出 Daniels 把总书记任命误系于 1922 年 5 月），历法无误。**但“待核”标签被系统性地挂在站内已有 A/S 级证据的事项上**，且史学来源单一（Daniels 一家）。

#### 06-01｜P1｜`1922-04-03` 总书记任命被标“待核”，站内已有至少 4 处互证；Carr `04-04` 与 Daniels `5月` 的冲突可以一次性裁定
- **定位**：[`L20`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1922-03-11th-party-congress.md#L20)、[`L27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1922-03-11th-party-congress.md#L27)、[`L35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1922-03-11th-party-congress.md#L35)、[`L44`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1922-03-11th-party-congress.md#L44)。
- **核证**（站内，均可点开）：
  1. [`CLM-stalin-docs-1920s-secretariat-correspondence-and-grain-turn` L31](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-stalin-docs-1920s-secretariat-correspondence-and-grain-turn.md#L31)：转引《斯大林重要文献》编者评述（`PDF p.101`）“4月3日，他被选为中央委员会总书记，同时仍兼任两人民委员部首脑……自4月6日起，政治局几乎总在周四全员出席”；L21、L45：莫洛托夫、古比雪夫为书记；
  2. [`reading-notes/stalin_docs_hobsbawm/RN-W24` L105–106、L187](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/stalin_docs_hobsbawm/RN-W24-stalin-pre1930-archival-docs-and-archaic-rebellion.md#L105-L106)：`1922-04-03` 全会设职并选出；
  3. [`INS-politburo-orgburo-secretariat` L56](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-politburo-orgburo-secretariat.md#L56)：`1922-04-03` 设总书记，莫洛托夫、古比雪夫任书记，据 Khlevniuk ch06；
  4. [`RN-W23 (Carr) L45`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr_bolshevik_rev_v1_v2/RN-W23-carr-party-state-constitution-and-economic-order-1917-1923.md#L45)：“1922.4.4《真理报》低调公布”——**这是公布日而非任命日**，据此 `RN-W35` L71 所写“`1922-04-04` 斯大林任总书记”应视为公布日误作任命日的**库内口径冲突**；
  5. Daniels（`ch07` L558“appointed to the new office of general secretary in May 1922”）是孤证且与 4 项相反。
  站内 [`L2 E08` L36](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L2_chronicles/E08_1921-1924_nep_and_lenins_last_struggle.md#L36)（Lewin 年表）还记“列宁接受、甚至可能是他本人提出让斯大林任总书记”及 `1922-05-25` 列宁首次中风——这可解释 Daniels 误系“5月”的来源（以首次中风节点为叙事重心）。
- **修复**：①T2/T3 把“待核”改写为：“**任命日 1922-04-03 [N.S.]**（站内 Stalin 文献编者评述、Khlevniuk、`INS-politburo-orgburo-secretariat` 互证；`04-04` 为《真理报》公布日，据 Carr；Daniels 之‘1922年5月’与前四者不符，视为孤证）；仅‘决议逐字措辞与列宁修改笔迹’待查原件（`CLM-stalin-docs…` L45）”；②边表 `PER-stalin` 行“日期待原始会议记录复核”改为上述依据；③**向 `RN-W35` L71 维护者提示 `04-04` 公布日/任命日混用**（非本审计写入）。

#### 06-02｜P1｜T3 的“三分之二”论证漏接站内 S 级原典《论党的统一》第7点
- **定位**：[`L43`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1922-03-11th-party-congress.md#L43)。
- **核证**：站内 [`1921-03-16_on-party-unity.md` L50、L94](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E10_turning_points/1921-03-16_on-party-unity.md#L50)（S 级）给出规则全文：对中央委员、候补中央委员和**中央监察委员**采取降级／开除的“极端措施”，须召开中央委员会全会并邀请候补委员与中央监察委员，**“三分之二票数”**即生效；列宁 1921-03-16 报告称此点“**not for publication**”。这一规则恰好说明：①Daniels 所述 1921 年 8 月什利亚普尼科夫案“差一票”适用的正是第7点门槛（他是中央委员）；②梅德韦杰夫、柯伦泰不是中央委员，且 1922 年案由**代表大会**而非中央全会处理，**不适用该 2/3 门槛**——这正是卡想表达但缺乏原典支撑的区分。卡 T3 只能写“待十一大速记核定”，而站内一手文本已可核定规则本身。
- **修复**：T3 增补《论党的统一》第7点定位（L50、L94），将“某种表决门槛及其票数待核”改写为“**第7点 2/3 门槛适用于中央全会对中委／候补／中监委成员，不适用于代表大会的纪律决议；十一大对三人的警告决议之表决数仍待速记**”。

#### 06-03｜P1｜`related_debates` 主题错位，且漏接站内 4 张直接相关节点
- **定位**：[`L15`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1922-03-11th-party-congress.md#L15)、[`L30–36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1922-03-11th-party-congress.md#L30-L36)。
- **核证**：`DEB-1918-war-communism-ideology-or-emergency` 的主题是 1918—1921 战时共产主义成因，而 11 大的主线是 NEP 退却终止、党内纪律与总书记设职。站内更对口：[`DEB-1921-trade-union-controversy-and-party-unity`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md)、[`DEB-1922-lenin-testament-and-stalin-rise`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1922-lenin-testament-and-stalin-rise.md)、[`DEB-1921-kronstadt-and-nep-origins`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1921-kronstadt-and-nep-origins.md)。边表缺：`INS-politburo-orgburo-secretariat`（任命的制度框架）、`INS-rabkrin-and-ccc`（`RN-W35` L71：十一大中监委与格别乌协作；Stalin 同期兼掌 RKI，PER-stalin L26）、`PER-molotov`／`PER-kuibyshev`（同批书记，见 06-01）、`MTG-1923-04-12th-party-congress`（后继）。
- **修复**：`related_debates` 改为上述三项（或保留原项并追加）；边表增补 4 行。

#### 06-04｜P1｜学派失衡：单一依赖 Daniels（1960），缺 Lewin／Khlevniuk／Carr 的站内论断
- **定位**：[`L13`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1922-03-11th-party-congress.md#L13)、[`L38–39`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1922-03-11th-party-congress.md#L38-L39)。
- **核证**：2.3 将总书记的“后来权力扩张”留作待研究，却不引站内已建的三派论断：[`CLM-lewin-1968-testament-intent`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-lewin-1968-testament-intent.md)（列宁的意图）、[`CLM-khlevniuk-2015-secretariat-and-nomenklatura`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-khlevniuk-2015-secretariat-and-nomenklatura.md)（档案视角的书记处实际运行）、[`CLM-carr-1950-politburo-orgburo-displacement-of-state-organs`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1950-politburo-orgburo-displacement-of-state-organs.md)（党国融合）；Lewin 的“职位当时没有后来那样的分量”（L2 E08 L36）与 Daniels 的“制度性顶点”（`ch07` L438：“secretarial hierarchy completed at the top”）恰构成一组直接对立的解释，却未入卡。
- **修复**：2.3 增“Lewin：设职时分量有限且列宁接受甚至可能提出”“Khlevniuk：书记处实际运作与干部权”“Daniels／Carr：设职完成秘书制等级金字塔”三栏，并链接上述 CLM；`perspectives_present` 增 `lewin-contingency`、`khlevniuk-archival`。

#### 06-05｜P2｜统计与数字缺口、Schema
- **票数／分母**：卡无代表数、党员总数、新中央委员会规模等任何分母；站内未检出可核数字（外部通行记载为约 500 余名有表决权代表、约 53 万党员，需外部权威核对后再入卡）。建议在 T3.2 显式声明“代表数与党员基数站内无数据，本卡不推算”，避免读者误以为该会无统计。
- 列宁政治报告（“汽车与司机”“退却结束”）T3 称“中文转述、待本地一手文本逐句对勘”。该报告位于 *Lenin CW* vol. 33，MIA 有英文页；站内 web-archive 无收录，建议入库（S 级）后再升级 T2 转述。
- `ORG-workers-opposition`（`end_ns: 1922-04-02`）已在边表 L34 中、节点存在，无缺；可再补 `PER-kollontai`、`PER-shliapnikov`（若已建卡，本审计未逐一核其存在）并在正文列明被处分三人。
- 卡缺 H1、LF 换行（同 03-05）。

---

### 07｜十月宣言、国家根本法与六三体制（`POL-october-manifesto-and-1906-fundamental-laws`）

**结论**：日期、条文与站内 S 级宣言档案吻合，外链实测有效且内容匹配（prlib 标题确为“Утверждены «Основные государственные законы…»”，HSE 页载第 87 条）；对第 87 条的限制与“六三”性质的界定准确。**主要问题是图谱孤立**——边表只有 4 个节点，站内至少 8 个直接相关节点未接入；以及 2.3 光谱缺具名学者与苏联—左翼视角。

#### 07-01｜P1｜边表与站内一等节点严重脱节（图谱孤立）
- **定位**：[`L30–35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-october-manifesto-and-1906-fundamental-laws.md#L30-L35)、[`L15`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-october-manifesto-and-1906-fundamental-laws.md#L15)。
- **核证**（站内均已存在，且部分已与本卡主题互相引用）：
  - [`INS-state-duma-1906-1917`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-state-duma-1906-1917.md#L29)：杜马各届起止与“六三政变”，本卡最直接的制度对象，却未链；
  - [`PER-nicholas-ii`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-nicholas-ii.md#L20)（签署者）、[`ORG-kadets`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-kadets.md#L26)（杜马中心主义、维堡宣言）、[`ORG-octobrists-and-progressive-bloc`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-octobrists-and-progressive-bloc.md#L10)（以宣言命名）、[`PER-milyukov`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-milyukov.md)、[`PER-guchkov`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md)；
  - [`EVT-1905-revolution`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1905-revolution.md#L20)、[`EVT-1905-12-moscow-armed-uprising`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1905-12-moscow-armed-uprising.md#L65)；
  - 争鸣卡 [`DEB-1906-stolypin-wager-and-agrarian-viability`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1906-stolypin-wager-and-agrarian-viability.md)（与第87条土地敕令直接相关）；
  - 论断卡 [`CLM-manning-1982-gentry-fronde-to-reaction`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-manning-1982-gentry-fronde-to-reaction.md)、`CLM-treadgold-1955-kadet-agrarian-and-tactical-failure`；站内 L3 [`1905-12_petersburg_arrest_and_moscow_uprising` L135](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1905-12_petersburg_arrest_and_moscow_uprising.md#L135)（“自由五十天后的反弹”）与 L2 [`E03_1905-1907` L10](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L2_chronicles/E03_1905-1907_first_revolution.md#L10)、L1 [`backbone` L56](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L1_milestones/1861-1929_backbone.md#L56)。
- **修复**：边表增 7–9 行（`INS-state-duma-1906-1917`、`PER-nicholas-ii`、`ORG-kadets`、`ORG-octobrists-and-progressive-bloc`、`EVT-1905-revolution`、`EVT-1905-12-moscow-armed-uprising`、`PER-guchkov`/`PER-milyukov`），`related_debates` 增 `DEB-1906-stolypin-wager-and-agrarian-viability`，T3 增 L1/L2/L3 时间线定位。

#### 07-02｜P1｜“1907-06-03 解散第二届杜马”与站内 L2 口径差一日，须在卡内显式对照
- **定位**：[`L27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-october-manifesto-and-1906-fundamental-laws.md#L27)。
- **核证**：本卡与 [`INS-state-duma` L29](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-state-duma-1906-1917.md#L29)、[`ORG-kadets` L26](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-kadets.md#L26)、`EVT-1905-revolution` L20 一致作 `1907-06-03 [O.S.] / 06-16 [N.S.]`；而 L2 [`E03` L10](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L2_chronicles/E03_1905-1907_first_revolution.md#L10) 写作“`1907-06-02 [O.S.] / 06-15 [N.S.]` 解散第二届杜马，**次日公布**新选举法”（据 Pipes）。两日的+13 换算都正确，问题是**事件语义不同**（解散令签署／发布 vs. 选举法公布）。本卡把“解散”和“新选举法”写成同日。
- **修复**：L27 改为“`1907-06-02 [O.S.] / 06-15 [N.S.]`夜社民党团遭逮捕、解散令颁行；`06-03 [O.S.] / 06-16 [N.S.]` 公布新选举法（‘六三’得名于此日）；二日区分据 Pipes（L2 E03）与官方《法令汇编》原册待核”，并要求 INS-state-duma 与 ORG-kadets 同步（编纂线执行）。另需补第一届杜马解散（`1906-07-09 [O.S.] / 07-22 [N.S.]`，据 ORG-kadets L26 的 `07-09/10`）及维堡宣言，否则“六三”与第87条的因果链缺前端。

#### 07-03｜P1｜史学光谱缺具名学者、缺苏联—列宁派与右翼视角，且 Weber 一环仅靠一个付费摘要页
- **定位**：[`L38–40`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-october-manifesto-and-1906-fundamental-laws.md#L38-L40)、[`L45`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-october-manifesto-and-1906-fundamental-laws.md#L45)。
- **核证**：
  1. “渐进演进的解释……强调议会委员会、预算审查和政党协商积累的学者”**无任何具名**，且卡内也没有对应站内论断卡；站内 [`DEB-1914-haimson-thesis-stability`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md#L23) 矩阵已有“Pipes 自由派政治史”“Hogan／Bonnell／Gerschenkron”等具名条目（L23、L32），可替代匿名“学者”；
  2. 2.3 无**苏联—列宁派**解释（十月宣言是沙皇的策略性让步、制宪幻想）与**右翼君主派**视角——站内可对读材料有：Pipes 对第87条违反根本法的承认（L2 E03 L10）、Manning 的“缙绅右翼与六三”论断、Lenin 1905 年两种策略（`sources/web-archive/W32_milestone_docs/1905-07_lenin-two-tactics…`，写于宣言之前，只可作策略语境，不可当宣言评论）；
  3. Weber 一环（L38、L45）仅链接 Cambridge 的《Max Weber and Russia》摘要页（Pipes 1955 *World Politics* 对 Weber 的二手阐释），**既非 Weber 原文，也非站内资料**；“伪立宪主义”标题需指 Weber 1906 年两篇原文（Archiv für Sozialwissenschaft und Sozialpolitik 本年所刊），卡内未给标题；
  4. `perspectives_missing` 仅写 `regional-electoral-experience`，未承认上述缺口。
- **修复**：2.3 把“学者”换成 DEB-1914 矩阵中的具名（Pipes／Hogan／Bonnell 等）并链 DEB-1914 L23–32；增列“Pipes：违反根本法但不等于取消杜马立法权”“Manning：缙绅右翼与六三选举法社会基础”（链 CLM）；明示“苏联—列宁派与君主右翼视角暂缺，待入库”；Weber 行改为“Weber 1906 原文标题待补；当前仅二手阐释（Pipes 1955）”。

#### 07-04｜P2｜Schema 与措辞
- T2 L26 同一句内同时写“批准 `1906-04-23`”和“公布 `04-26`”，已做区分且合规；建议在 T3.2 把“4月26日公布口径尚待核”改为一个可执行动作（核《Собрание узаконений》1906 年相应号，S 级入库）。
- 边表“核心依据”如 `十月宣言原档`、`土地改革卡` 偏笼统，应落到 `WEB-1905-10-17-october-manifesto` 与 `POL-stolypin-agrarian-reform` ID。
- 卡缺 H1、CRLF 换行（与 03/04/05/06 的 LF 并存）。

---

## 七、汇总修复矩阵（7 张卡）

> 图例：优先级 P0＝史实／历法／断链／失效外链硬伤；P1＝站内 S/A 漏引、票数与统计分母失准、学派失衡；P2＝Schema／悬空尾句。

### 7.1 逐卡问题计数

| 卡 | P0 | P1 | P2 | 历法 | ID／外链 | 核心判断 |
| :--- | :--: | :--: | :--: | :--: | :--: | :--- |
| 01 `INS-rabkrin-and-ccc` | 0 | 4 | 1 | ✓ | ✓（2 外链 200） | “待核”标在 Carr 已核事项；漏接 12/11 大卡；“合并”术语分歧 |
| 02 `INS-gosbank-and-narkomfin` | 0\*（条件） | 4 | 1 | ✓ | ✓ID；`istmat` TLS 失败 | 币值数字全对；分母口径提示；L3/DATA-02 锚点漏用；1917–21 首长缺 |
| 03 `MTG-1906-04` | 0 | 3 | 1 | ✓（无错位） | ✓ | 62:46 正确；缺 108/112 分母说明、决议内容、具名史家；Haimson 误作 6 月 |
| 04 `MTG-1917-04` | 0 | 4 | 1 | ✓ | ✓ | 71:39:8 / 56:16:18 / 九人票次 / 152 代表站内已有却写“待核”；Zimmerwald 列宁败北被掩盖 |
| 05 `MTG-1918-07` | 0 | 3 | 1 | ✓ | ✓ | 分母 1,035/88；库内 L3、CLM-carr 旧口径冲突；Rabinowitch 单极 |
| 06 `MTG-1922-03` | 0 | 4 | 1 | ✓ | ✓ | 04-03 已可裁定；站内原典第7点 2/3 未用；related_debates 错位；Daniels 单极 |
| 07 `POL-october-manifesto…` | 0 | 3 | 1 | ✓ | ✓ | 边表孤立（缺 8+ 节点）；06-02/03 一日差；光谱匿名、Weber 仅二手 |
| **合计** | **0** | **25** | **7** | 7/7 合规 | 0 断链；1 外链待人工复核 | |

\* 02-02：`istmat.org/node/40879` 在本审计环境无法完成 TLS 握手；若人工确认长期失效，则 02-02 **升格为 P0**，其余 P0 数不变。

> 更正：阶段一 §四 汇总表第 02 行因手误把“4 项”写成含糊表述，以本表为准：02 号卡共 P1 × 4（02-01 分母口径、02-02 外链、02-03 站内锚点漏用、02-04 人事链条缺口），P2 × 1（02-05）。

### 7.2 可执行修复清单（按落地优先级）

| # | 卡／文件 | 问题 ID | 动作 | 优先级 |
| :-- | :--- | :--- | :--- | :--: |
| 1 | `INS-gosbank-and-narkomfin` | 02-02 | 复核 `istmat.org/node/40879`；补备用档案或 T3 声明“据转录、无独立印证”；最好入库该法令（S 级） | P1（条件升 P0） |
| 2 | `MTG-1917-04` | 04-01、04-02 | 写入 152 代表、71:39:8、56:16:18、3 票反对 8 弃权、九人 109 票明细；明写列宁在 Zimmerwald 议题上败北；去除 T3 “待复核编纂线索” | P1 |
| 3 | `MTG-1922-03` | 06-01、06-02 | 把 `1922-04-03` 改为多源互证日期；声明 `04-04` 为公布日、Daniels 5 月为孤证；加入《论党的统一》第7点 2/3 规则定位 | P1 |
| 4 | `INS-rabkrin-and-ccc` | 01-01、01-02、01-03 | 引 Carr 核实 `1920-02-07` VTsIK 法令；修正“1920 中央监察机构”；补列宁 75–100 名、联席全会、合并设想；链接 `MTG-1923-04`、`MTG-1922-03`、`CON-thermidor-and-bureaucracy`、Carr CLM | P1 |
| 5 | `INS-gosbank-and-narkomfin` | 02-01、02-03、02-04 | 切尔文占比三点补分母提示；补 1917 接管（L3 两处）、1924 币改 50,000:1 与 10:1、黄金储备 15→150 百万金卢布、RN-W32 口径冲突；补 1917–21 首长（待核）及 `1922-11 / 1923-07-06 / 1926-01-16` | P1 |
| 6 | `MTG-1918-07` | 05-01、05-02、05-03 | 补 1,035/88 分母，澄清 399 与 678 集合关系；标出 L3 L7/L24/L40 与 CLM-carr 的旧口径；增 Pipes／Leggett 视角及 `EVT-1918-09-red-terror-and-left-sr-rupture` | P1 |
| 7 | `POL-october-manifesto…` | 07-01、07-02、07-03 | 边表接 `INS-state-duma-1906-1917` 等 8+ 节点；二日（06-02/06-03）语义区分并补第一届杜马解散与维堡宣言；光谱具名化、承认苏联—右翼视角缺口、Weber 原文标题待补 | P1 |
| 8 | `MTG-1906-04` | 03-02、03-03、03-04 | 注明 62+46=108 与 112 的 4 票差及民族组织代表归属待核；补 Daniels（武装行动／剥夺决议）、§1 回归列宁公式、Carr 的杜马乐观主义；标注 Haimson 2005 误作 1906 年 6 月 | P1 |
| 9 | 全部 7 张卡 | P2 | 统一 H1 标题行与换行符（01/02/07 为 CRLF，03–06 为 LF）；边表“核心依据”落到具体 ID／页码；清理悬空“待核”尾句 | P2 |

### 7.3 库内跨文件冲突备忘（不属本次写入范围，请编纂线另案处理）

| 冲突 | 位置 | 与哪一方冲突 | 建议裁定依据 |
| :--- | :--- | :--- | :--- |
| 斯大林任总书记 `04-03` vs `04-04` | [`RN-W35` L71](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr_bolshevik_rev_v1_zh/RN-W35-carr-lenin-party-instrument-and-soviet-constitution-1917-1923.md#L71) | `INS-politburo-orgburo-secretariat` L56、`RN-W24`、`CLM-stalin-docs…`、`RN-W23` L45 | Carr 自述 `04-04` 为《真理报》公布日；任命日 `04-03` |
| “678 含 399”“舞弊格局”“城乡 5:1”“一党专政法典化” | [`L3 1918-07` L7/L24/L40](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1918-07_left_sr_uprising_and_red_terror_launch.md#L24) | 宪法 S 档案 L28；Rabinowitch L243、L492–532 | 399 不在预报统计内；125,000 为居民对 25,000 为选民；宪法无一党条款 |
| “城乡 1:5 不平等代表权” | [`CLM-carr-1950-1918-constitution…` L18](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1950-1918-constitution-fusion-of-powers-and-class-franchise.md#L18) | 宪法 S 档案 L28 | 加注分母口径 |
| 解散第二届杜马 `06-02` vs `06-03` | [`L2 E03` L10](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L2_chronicles/E03_1905-1907_first_revolution.md#L10) | `INS-state-duma`、`ORG-kadets`、`EVT-1905-revolution`、本卡 | 区分解散令与选举法公布日，核《法令汇编》 |
| “合并”vs“合署” | `RN-W23`/`RN-W35`/`RN-W1`（Lewin）/`CON-thermidor-and-bureaucracy` | `PER-ordzhonikidze` L26 与 `INS-rabkrin-and-ccc` | 统一术语：列宁设想＝合并；十二大实践＝共同领导、负责人兼任、法律上仍为两机构 |
| 站内 web-archive 缺《怎样改组工农检查院》《宁肯少些，但要好些》《十一大政治报告》 | `sources/web-archive/` | 审计任务描述假设其已入库；实际仅有《论合作制》 | 以 marxists.org（已实测 200）为准入库为 S 级 |

### 7.4 总体评价

1. **事实层面**：7 张卡**未发现 P0 史实／历法硬伤**。7 组双历换算（含 1906 斯德哥尔摩西欧会场、1918 改历后纯公历）、62:46 与 1,035/678/269 等数字、切尔文 3%/37%/80%、宪法第25／64–65 条均核实无误。
2. **共同症状**：编纂线对“站内已有 S/A 证据”的利用不足——把可核事项（04 号 71:39:8 与九人票次、06 号 `04-03` 与 2/3 门槛、01 号 `1920-02-07`、02 号 L3 与 DATA-02 锚点）标成“待核”，而对**真实未核事项**（Gosbank 1920 法令链接、两篇列宁文的入库）反而较少提示。
3. **反偏见表现**：各卡普遍克制（不把“后来结果”倒推为设计、不把单一学派当共识），但 3 张会议卡（03、04、06）的史学光谱缺具名学者，1 张政策卡（07）图谱接入过少。修复以“补链接、补分母、补具名”为主，无需重写主叙事。

---
*AUD-16A 完。阶段一与阶段二均已落盘；全程只读，未触碰任何被审卡片或共享总表。*
