# AUD-18D：Wave 42 OpenAI `gpt-6.1-terra` 党代表大会与中央全会卡（`MTG-*`，5 张）跨模型家族史学史对勘与反偏见审计报告

- **审计官（Auditor）**：`dialectic-auditor`（Google `gemini-4-argon`, `thinking_level: "high"`）
- **被审对象（Target Scope）**：OpenAI `gpt-6.1-terra`（Codex）在 Wave 42 升格的 5 张党代表大会与中央全会卡（`MTG-*`）
  1. `cards/meetings/MTG-1919-03-8th-party-congress.md`（俄共（布）第八次代表大会，1919年3月）
  2. `cards/meetings/MTG-1921-rcpb-10th-congress.md`（俄共（布）第十次代表大会，1921年3月）
  3. `cards/meetings/MTG-1924-05-13th-party-congress.md`（俄共（布）第十三次代表大会，1924年5月）
  4. `cards/meetings/MTG-1929-04-cc-joint-plenum.md`（联共（布）中央委员会与中央监察委员会四月联席全会，1929年4月）
  5. `cards/meetings/MTG-1929-11-cc-plenum.md`（联共（布）中央委员会十一月全会，1929年11月）
- **审计基准**：`CLAUDE.md`、`SCHEMA.md`、`audits/AUD-18A-wave40-codex-deb-batch1-audit.md`、`audits/AUD-18B-wave40-codex-deb-batch2-audit.md`、站内 `historiography/claims/CLM-*.md`、`reading-notes/`、`sources/monographs/`、`sources/web-archive/`（含 `W32_milestone_docs/` 与 `W39_lenin_1922_1923_docs/`）、`data/DATA-03*`/`DATA-04*`/`DATA-06*` 及 `timeline/L3_daily/*`。
- **写盘状态**：阶段一（01–03 号卡）与阶段二（04–05 号卡及汇总修复动作矩阵）已全部完成落盘。

---

## 一、五卡全局审计统计与基线总表

| 序号 | 卡片 ID | 文件路径 | 行数 | `[T1]` 字数 | 断链 / 悬空 ID | 所挂 `CLM-*` 数 | 所挂 `DATA-*` 数 | P0 数 | P1 数 | P2 数 | 审计结论 |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 01 | `MTG-1919-03-8th-party-congress` | `cards/meetings/MTG-1919-03-8th-party-congress.md` | 46 | 109 字 | 0 / 0 | 1 | 0 | **1** | **2** | **1** | **需返工修复（P0 错配 0 命中札记 + P1 漏秘会票数/机构名单/党集中化条款）** |
| 02 | `MTG-1921-rcpb-10th-congress` | `cards/meetings/MTG-1921-rcpb-10th-congress.md` | 46 | 115 字 | 0 / 0 | **0** | **0** | **0** | **2** | **1** | **需补强修复（P1 全漏 `DATA-04` 票数/代表人数 + P1 全漏 `CLM-*` 及 Godson/Kollontai 署名）** |
| 03 | `MTG-1924-05-13th-party-congress` | `cards/meetings/MTG-1924-05-13th-party-congress.md` | 46 | 127 字 | 0 / 0 | 2 | **0** | **0** | **2** | **1** | **需补强修复（P1 全漏 `W39_lenin_1922_1923_docs/` 遗嘱文献群 + P1 漏 `DATA-04`/`L3` 票数与列宁征召数据）** |
| 04 | `MTG-1929-04-cc-joint-plenum` | `cards/meetings/MTG-1929-04-cc-joint-plenum.md` | 47 | 114 字 | 0 / 0 | **0** | **0** | **1** | **1** | **1** | **需返工修复（P0 错配 0 命中札记 `RN-W18` 且点名 Erlich 未挂源 + P1 全漏 `CLM-*`/`DATA-03`/`RN-W39`）** |
| 05 | `MTG-1929-11-cc-plenum` | `cards/meetings/MTG-1929-11-cc-plenum.md` | 48 | 119 字 | 0 / 0 | 3 | **0** | **1** | **2** | **1** | **需返工修复（P0 隐去《苏联农村的悲剧》四主编 Danilov/Ivnitsky 等署名 + P1 漏 `RN-W39` 泽姆斯科夫/`DATA-06`/Cohen与Khlevniuk `CLM-*`）** |
| **合计** | **5 张 `MTG-*`** | — | **233** | **均 `<= 150` 字** | **0 / 0** | **6** | **0** | **3** | **9** | **5** | **3 张含 P0、2 张含 P1，均须按矩阵精准返工** |

### 核心共性诊断（`gpt-6.1-terra` Wave 42 `MTG-*` 批次特征）
1. **机械链接与行文克制达标，但全部 5 张会议卡竟然 `0` 挂接 `data/DATA-*` 定量数据卡**：
   - 5 张卡片的相对路径链接（48 条）与反引号节点 ID（28 个）全部机械有效（0 断链、0 悬空 ID），`[T1]` 均控制在 109–127 字之间；
   - 然而，尽管站内已建有专门针对历届党代会代表人数、党员规模与关键表决票数的 `DATA-04-party-membership-and-congress-votes-1903-1929.md`，以及针对 1928–1929 粮食危机与集体化跃进的 `DATA-03`、`DATA-06`，**全部 5 张会议卡均未挂接任何一张 `DATA-*` 卡，且在八大、十大、十三大正文中未写出哪怕一个具体表决票数或出席代表人数**！
2. **错配 0 命中札记与“点名学者却不挂其札记/主张卡”（P0）**：
   - `MTG-1919-03-8th-party-congress` 将八大军事反对派与民主集中派锚定到明确跳过第 4–5 章、对八大 0 命中的 `RN-W1C` 和 `RN-W20`，反而漏掉馆藏 `sources/monographs/daniels_1960_conscience/ch04_pages_101-125.md` 与 `ch05_pages_126-150.md`；
   - `MTG-1929-04-cc-joint-plenum` 将 1929 年 4 月联席全会挂到只讲 1929 年秋冬集体化与 1917 年孟什维克、对四月全会 0 命中的 `RN-W18`，且正文点名 `Erlich` 却不挂 `RN-W3-great-industrialization-debate-1924-1928.md`；
   - `MTG-1921-rcpb-10th-congress` 与 `MTG-1929-04-cc-joint-plenum` 全卡挂接 `CLM-*` 数为 **0**。
3. **档案集主编与论文集专章作者匿名化（P0/P1）**：
   - `MTG-1929-11-cc-plenum` 挂接了《苏联农村的悲剧》第 2 卷札记与两张 `CLM-tragedy-village-1929-*`，但在正文中仅写书名《苏联农村的悲剧》，完全隐去了四位主编 **V. P. Danilov（丹尼洛夫）、R. T. Manning（曼宁）、L. Viola（维奥拉）、N. A. Ivnitsky（伊夫尼茨基，兼第2卷长篇导言作者）** 的姓名；
   - `MTG-1921-rcpb-10th-congress` 引用 `RN-W35` 讨论十大工会“共产主义学校/传动带”定位时，只提 Schapiro 与 Lebsky，遗漏了该书联合主编兼第 4 章专章作者 **Joseph Godson（1981）**。
4. **Wave 39 新增馆藏（`W39_lenin_1922_1923_docs/` 与泽姆斯科夫 `RN-W39` / `CLM-zemskov-2018-*`）全面漏挂（P1）**：
   - 十三大卡漏挂与《给代表大会的信》一并由克鲁普斯卡娅于 `1924-05-18` 移交、共同构成“列宁遗嘱”改革纲领的 `W39_lenin_1922_1923_docs/`（《关于民族或“自治化”问题》《我们怎样改组工农检查院》《宁肯少些，但要好些》）；
   - 1929 年四月与十一月两张全会卡均漏挂 Wave 39 新增的泽姆斯科夫 `RN-W39` 与 `CLM-zemskov-2018-*`。

---

## 二、五大会议会期、出席规模与核心表决/决议基准核验表

| 会议卡 ID | 站内核定会期（公历 N.S.） | 出席代表 / 参会规模（`DATA-04` / `L3`） | 站内已锁定的核心表决票数与制度决议锚点 | 卡片当前覆盖状态 |
| :--- | :--- | :--- | :--- | :--- |
| `MTG-1919-03-8th-party-congress` | `1919-03-18` 至 `1919-03-23` | **301** 名表决权代表 + **102** 名发言权代表（代表 **313,766** 名党员） | ① 军事问题秘密会议表决：支持托洛茨基路线（索科利尼科夫主报告）**`174` 票** vs. 弗·米·斯米尔诺夫军事反对派决议 **`95` 票**；② 中央扩至 **19 正式 + 8 候补**，`03-25` 设首届常设政治局（5正式：**列宁、托洛茨基、斯大林、加米涅夫、克列斯廷斯基**；3候补：**季诺维也夫、布哈林、加里宁**）、组织局（5人）与书记处（克列斯廷斯基任责任书记）；③ 组织决议否定党联邦制，宣布乌、拉、立、白共产党中央仅为俄共区域委员会（`областные комитеты`），强制在苏维埃设严守党纪的共产党党团（`фракции`）。 | **漏代表人数、漏 `174:95` 票数、漏首届政治局名单、漏否定党联邦制条款** |
| `MTG-1921-rcpb-10th-congress` | `1921-03-08` 至 `1921-03-16` | **694** 名表决权代表 + **296** 名发言权代表（代表 **732,521** 名党员；近 **300** 名代表赴喀琅施塔得参战） | ① 工会争论表决（`03-14`）：列宁等《十人纲领》**`336` 票** vs. 托洛茨基—布哈林纲领 **`50` 票** vs. 工人反对派 **`18` 票**（弃权 `2` 票）；② `03-15` 通过以粮食税取代余粮收集制（1921–22 征额从 4.23 亿普特减至 **2.4 亿普特**）；③ `03-16` 通过《关于党的统一》（含秘而不宣、至 `1924-01-17` 才由斯大林公开的第 7 条三分之二开除中央委员条款）与反工团主义决议，反对票均**不足 `30` 票**；④ 中央扩至 **25 正式委员**（列宁派 `20:5`，莫洛托夫任责任书记，吸纳施略普尼科夫与库图佐夫入中央）。 | **漏代表人数、漏 `336:50:18` 及 `<30` 票数、漏第7条首次公开日期、漏中央改选细节** |
| `MTG-1924-05-13th-party-congress` | `1924-05-23` 至 `1924-05-31` | **748** 名表决权代表 + **416** 名发言权代表（共 **1,164** 人，代表 **735,881** 名党员/候补党员） | ① “列宁征召”突击吸纳 **20万–24万**工人，组织局破例允许候补党员参加十三大初选投票，致 748 名表决权代表中**左翼反对派 `0` 席**；② `05-18` 克鲁普斯卡娅移交列宁最后 13 份口授文件，`05-21` 中央全会与 `05-22` 长老会议由加米涅夫主持宣读《给代表大会的信》，季、加提议留任斯大林，禁止速记只按代表团分团口头传达；③ 中央扩至 **53 正式 + 34 候补**、中监委 **151 人**，`06-02` 一中全会斯大林连任总书记、**布哈林升任政治局正式委员**。 | **漏 `05-18` 移交日、漏 748 代表中反对派 `0` 席、漏列宁征召人数及候补党员初选投票权、漏会后政治局改组名单** |
| `MTG-1929-04-cc-joint-plenum` | `1929-04-16` 至 `1929-04-23` | 约 **300 余名**中央委员与中监委委员围攻约 **13 名**右派支持者（Cohen `pp. 308–313`） | ① 会前 `04-15` 布、李、托对五年计划投弃权票；② `04-18` 布哈林横跨晨晚两会抗辩（宣读 `1928-06-01/02` 致斯大林私信与农业笔记，痛斥 `02-09` 决议替“贡赋”辩护及“赤裸裸的肉体拳头政策”）；③ `04-22` 斯大林作《论联共（布）党内的右倾》演说（当时报刊删 30 余页）；④ 解除布哈林《真理报》/共产国际及托姆斯基工会职务但**对外保密、保留三人政治局席位**（6月洗工会、7月共产国际十中全会免职、`08-21/24`《真理报》首次公开点名）；⑤ 紧接十六次代表会议（`04-23/29`）一五计划仍设五年后集体/国营农场仅占播种面积 **`17.5%`**。 | **漏 300 对 13 规模、漏 `04-15` 弃权与 6/7/8 月执行日、漏十六次代表会议 `17.5%` 基准** |
| `MTG-1929-11-cc-plenum` | `1929-11-10` 至 `1929-11-17` | 联共（布）中央委员会全体会议 | ① `11-07`（11-03完稿）斯大林发表《大转变的一年》；② `11-12` 布、李、托提交最后抗辩声明；③ `11-17` 通过《关于布哈林同志集团》（将布哈林逐出政治局，警告李可夫、托姆斯基、**乌加罗夫**）并在《控制数字》决议第六节写入“宣传右倾机会主义与留在联共（布）内不相容”（`11-18`《真理报》刊布）；④ 批准动员**“二万五千人”**（`12-18` 核定控制额 **26,380 人**、实选 **27,519 人**）与设全苏农业人民委员部（`12-07` 成立）；⑤ `11-25` 签署（`11-26` 见报）三人公开检讨声明；⑥ `12-05` 设雅科夫列夫 18 人委员会 → `≤12-14` 鲍曼组三类富农方案 → `12-18` 一致草案保留奶牛/小农具与退社权 → `12-25` 斯大林亲笔信否决 → `12-27` 演说 → `1930-01-05` 决议删净保护条款。 | **漏 `11-12` 声明与乌加罗夫、漏“二万五千人” `26,380/27,519` 定数、漏 `12-18` 草案内容与 `12-25` 斯大林否决信** |

---

## 三、阶段一逐卡深度对勘与分级问题清单（01–03 号会议卡）

### 01. `cards/meetings/MTG-1919-03-8th-party-congress.md`（俄共（布）第八次代表大会（1919年3月））

- **机械与格式核验**：46 行，`[T1]` 109 字（`<= 150` 字，合规），全卡 5 个反引号 ID 与 8 条相对路径链接均存在（0 断链、0 悬空 ID）。
- **史源逐一对读与问题清单**：

  1. **[P0-01] 错配与八大、军事反对派及民主集中派完全无关的两份精读札记（`RN-W1C` 与 `RN-W20`），且漏引馆藏 Daniels 第 4–5 章原书分页文本**
     - **位置**：`1.2 [T2]` L26、`**[T2] 史学位置与争鸣**` L41、`1.3 [T3]` L44。
     - **现象**：
       - L41 写“Daniels指出民主集中派与军事反对派在八大首次把党内机关集中和军队正规化提上全党辩论台面”，并在 L44 将唯一的 Daniels 史源锚定到 `[Daniels反对派精读](../../reading-notes/daniels_1960_conscience/RN-W1C-communist-oppositions-1918-1929.md)`；
       - L26 将八大关于军事专家、政委制度、游击习气与集中指挥的辩论锚定到 `[红军与军事专家精读](../../reading-notes/mawdsley_kakurin/RN-W20-civil-war-geopolitics-and-military-specialists.md)`。
     - **核实证据**：
       - 核查 `reading-notes/daniels_1960_conscience/RN-W1C-communist-oppositions-1918-1929.md#L30-L37` 的阅读范围声明表：该札记**仅精读了 `ch00`、`ch03`（1918 布列斯特）、`ch06`（1921 十大）、`ch14` 与 `ch15`（1928–1929）**，明确标注跳过 `ch04` 与 `ch05`；全文检索 `RN-W1C` 对“八大 / Eighth Congress / 军事反对派 / Military Opposition / 萨普罗诺夫 / Sapronov / 奥新斯基 / Osinsky / 斯米尔诺夫 / Smirnov”**命中数为 0**！站内 `cards/organizations/ORG-democratic-centralists.md#L50` 早已明文警示：“`本卡不再以 RN-W1C-communist-oppositions-1918-1929 作 DC 本体依据（该札记对民主集中派、萨普罗诺夫、奥新斯基无命中）`”。
       - 核查 `reading-notes/mawdsley_kakurin/RN-W20-civil-war-geopolitics-and-military-specialists.md`：全文对“八大 / Eighth Congress / 军事反对派 / 斯米尔诺夫 / 伏罗希洛夫”同样**命中数为 0**。
       - 相反，八大军事反对派与奥新斯基—萨普罗诺夫组织辩论的真实一手馆藏出处在 `sources/monographs/daniels_1960_conscience/ch04_pages_101-125.md#L649-L1066`（`[pp. 93–107 / PDF pp. 111–125]`）与 `ch05_pages_126-150.md#L106-L230`（`[pp. 110–113 / PDF pp. 128–131]`）。
     - **整改要求**：将 L41/L44 的 Daniels 出处替换为 `sources/monographs/daniels_1960_conscience/ch04_pages_101-125.md`（`[pp. 93–107]`）与 `ch05_pages_126-150.md`（`[pp. 110–113]`）；在 L26 区分 `RN-W20` 仅提供内战红军任用军事专家与政委双签制的宏观背景，八大军事问题秘密会议的直接史源应锚定 Daniels Ch. 4 `[pp. 103–107]`。

  2. **[P1-01] 漏引站内可核的八大军事问题秘密会议表决票数（`174 : 95`）、八大会后中央/政治局/组织局/书记处具体名单，且在 `[T3]` 将站内已核实的会后机构名单误标为“仍需逐页对勘”**
     - **位置**：`1.2 [T2]` L25–27、`1.3 [T3]` L46。
     - **现象**：
       - L26 叙述八大军事问题交锋时，完全未写明代表人数（301名有表决权代表、102名有发言权代表，代表 313,766 名党员，见 `data/DATA-04-party-membership-and-congress-votes-1903-1929.md#L19`）与军事问题秘密会议的表决票数；
       - L25 与 L46 称“正式把政治局、组织局、书记处设为常设中枢”“具体组织决议与会后机构名单原件仍需逐页对勘”，既未写出八大选出的第一届常设政治局名单，又将站内已可精确核实的机构构成与 Carr vs. Daniels 史学分歧笼统推给“待对勘”。
     - **核实证据**：
       - **军事问题秘密会议表决票数**：据 `sources/monographs/daniels_1960_conscience/ch04_pages_101-125.md#L1046-L1066`（`[pp. 105–106 / PDF pp. 123–124]`），因高尔察克春耕攻势爆发，托洛茨基本人赴前线未能出席八大，由索科利尼科夫（G. Y. Sokolnikov）代为作军事路线主报告，弗·米·斯米尔诺夫（V. M. Smirnov）代表军事反对派作副报告；在秘密全体会议（secret session）表决中，**支持托洛茨基现行军事路线的多数派获 `174` 票，斯米尔诺夫军事反对派决议获 `95` 票**（随后大会通过折衷公开决议，并由季诺维也夫口头传达一项要求在军队中更重视共产党工作人员意见的秘密指示）。
       - **中央委员会扩编与三大常设机构名单**：据 `ch05_pages_126-150.md#L140-L230`（`[pp. 110–113]`）、`cards/institutions/INS-politburo-orgburo-secretariat.md#L25` 与 `historiography/claims/CLM-carr-1950-politburo-orgburo-displacement-of-state-organs.md`：
         1. 在斯维尔德洛夫于大会开幕前两日（`1919-03-16`）病逝的背景下，奥新斯基在组织问题会议上提议将中央委员会扩编至 21 人、把人民委员会并入全俄中央执行委员会主席团；季诺维也夫作组织报告反驳。大会最终将中央委员会从 15 人扩编为 **19 名正式委员、8 名候补委员**；
         2. 1919年3月25日八届一中全会选出**第一届常设政治局（5名正式委员：列宁、托洛茨基、斯大林、加米涅夫、克列斯廷斯基；3名候补委员：季诺维也夫、布哈林、加里宁）**；
         3. 设立**组织局（Orgburo，5人）**与由一名中央组织局委员领导、配 5 名技术书记的**书记处（Secretariat，由尼·尼·克列斯廷斯基任责任书记）**；
         4. **站内史家分歧需诚实标明**：Carr（`CLM-carr-1950-politburo-orgburo-displacement-of-state-organs.md` / `RN-W23` `[p. 201]`）记斯大林自 1919 年 3 月起即为唯一同时担任政治局与组织局正式委员之人；而 Daniels（`ch05_pages_126-150.md#L219-L224` `[p. 112]`）则记斯大林最初未入组织局、直至 1920 年初才进入组织局。
     - **整改要求**：在 `[T2]` 补入 `DATA-04` 代表与党员基数、军事问题秘密会议 `174 : 95` 票数（及索科利尼科夫 vs. 弗·米·斯米尔诺夫）、中央委员会 19 正式 + 8 候补及政治局 5 正式 + 3 候补名单；在 `[T3]` 将“会后机构名单原件仍需逐页对勘”修正为对 Carr（1950）与 Daniels（1960）关于 1919 年首届组织局名单记载差异的精确说明。

  3. **[P1-02] 漏写八大组织决议否定党组织联邦制（宣布乌克兰、拉脱维亚、立陶宛、白俄罗斯共产党中央仅享有俄共区域委员会地位）与强制党团控制苏维埃条款，且漏挂 4 张核心 `CLM-*` 主张卡**
     - **位置**：`1.2 [T2]` L25–28、`**[T2] 史学位置与争鸣**` L41–42、`1.3 [T3]` L44。
     - **现象**：
       - 全卡仅挂接了 1 张 `CLM-carr-1950-bolshevik-self-determination-vs-cultural-autonomy.md`，遗漏了八大组织决议中影响最为深远的两条制度硬条款：
         1. **否定党的联邦制**：针对建立独立民族共产党的压力，八大组织决议明确裁定“必须存在一个拥有统一中央委员会的集中化共产党”，宣布**乌克兰、拉脱维亚、立陶宛和白俄罗斯共产党中央委员会仅享有俄共（布）区域委员会（`областные комитеты`）的地位，无条件服从俄共（布）中央**（见 `reading-notes/carr_bolshevik_rev_v1_v2/RN-W23-carr-party-state-constitution-and-economic-order-1917-1923.md#L211` `[p. 370]`、`RN-W32#L186` `[p. 176]` 及 Daniels `ch04_pages_101-125.md#L786-L794` `[p. 100]`）；
         2. **党对苏维埃的“完全政治统治”与党团纪律**：八大决议明确规定党必须在苏维埃等一切非党组织中赢得“完全的政治统治（undivided political mastery）”并对其实行日常实际控制，在所有苏维埃组织中强制建立严守党纪的共产党党团（`фракции`，见 Daniels `ch04#L814-L824` `[pp. 100–101]` 及 `CLM-carr-1950-soviet-to-party-ascendancy-mechanism.md`）。
     - **整改要求**：在 `[T2]` 与 `[T3]` 补入上述两项八大组织决议核心条款，并补挂 `data/DATA-04-party-membership-and-congress-votes-1903-1929.md` 及 4 张直接关联的 `CLM-*` 卡：
       - `historiography/claims/CLM-carr-1950-politburo-orgburo-displacement-of-state-organs.md`
       - `historiography/claims/CLM-carr-1950-soviet-to-party-ascendancy-mechanism.md`
       - `historiography/claims/CLM-carr-1950-self-determination-to-federal-reunion.md`
       - `historiography/claims/CLM-carr-1952-war-communism-internal-contradictions.md`

  4. **[P2-01] `2.2 关系边表` 核心参与者与前件节点覆盖不全**
     - **位置**：`2.2 关系边表（Edges）` L33–39。
     - **现象**：边表仅列出 5 条边，遗漏了在正文点名且站内已有专门人物卡的核心辩论参与者：`PER-lenin`、`PER-bukharin`、`PER-pyatakov`、`PER-osinsky`、`PER-sapronov`、`PER-voroshilov`。
     - **整改要求**：在 `2.2` 边表中补齐上述人物节点。

---

### 02. `cards/meetings/MTG-1921-rcpb-10th-congress.md`（俄共（布）第十次代表大会（1921年3月））

- **机械与格式核验**：46 行，`[T1]` 115 字（`<= 150` 字，合规），全卡 5 个反引号 ID 与 10 条相对路径链接均存在（0 断链、0 悬空 ID）。
- **史源逐一对读与问题清单**：

  1. **[P1-01] 完全漏引 `DATA-04` 定量数据卡，导致十大出席代表人数、工会争论三大纲领表决票数（`336 : 50 : 18`）、《关于党的统一》反对票数与粮食税减征幅度全部缺失**
     - **位置**：`1.2 [T2]` L25–28、`1.3 [T3]` L44–46。
     - **现象**：作为知识库中制度转折权重最高的党代会卡之一，`MTG-1921-rcpb-10th-congress.md` 全文**未出现任何一个表决票数或代表人数**，也未挂接 `data/DATA-04-party-membership-and-congress-votes-1903-1929.md`！
     - **核实证据**：据 `data/DATA-04-party-membership-and-congress-votes-1903-1929.md#L19, #L54-L62`、`timeline/L3_daily/1921-03_kronstadt_and_10th_congress.md#L113-L259`、`sources/web-archive/E06_E10_turning_points/1921-03-16_on-party-unity.md#L54-L58` 及 `reading-notes/daniels_1960_conscience/RN-W1C-communist-oppositions-1918-1929.md#L70-L79`：
       1. **代表与党员规模**：**694 名有表决权代表**（另 296 名有发言权代表，合计 990 人），代表 **732,521 名党员**；其间近 **300 名代表**（含工人反对派与军事反对派骨干）响应动员踏上芬兰湾冰面参加镇压喀琅施塔得起义；
       2. **工会问题三大纲领最终表决票数（`1921-03-14`）**：列宁—托姆斯基—季诺维也夫《十人纲领》获 **`336` 票**，托洛茨基—布哈林联合纲领获 **`50` 票**，施略普尼科夫—柯伦泰“工人反对派”纲领获 **`18` 票**，弃权 **`2` 票**（可对比 1921 年 1 月莫斯科党委预选时的 `57 : 33 : 21`）；
       3. **《关于党的统一》与《关于我们党内的工团主义和无政府主义倾向》表决（`1921-03-16`）**：两项决议均仅遭遇**不到 `30` 张反对/修正票**（约 25–30 票）；审议期间阿·谢·基谢廖夫（A. S. Kiselyov）警告列宁把第7条“机关枪”架在同志面前；第7条秘密条款授权中央委员会与中央监察委员会联席会议以三分之二多数将违纪中央委员降为候补委员直至开除出党，**该条款在十大闭幕时秘而不宣，直至 `1924-01-17` 俄共（布）第十三次代表会议上才由斯大林首次公开宣读**；
       4. **中央委员会改选与怀柔吸纳**：大会将中央委员会从 19 人扩编至 **25 名正式委员**（列宁派占 `20 : 5` 绝对多数，托洛茨基派减少 3 席，克列斯廷斯基、普列奥布拉任斯基、谢列布里亚科夫三名中央书记全部落选，莫洛托夫出任责任书记并升任政治局候补委员），同时将工人反对派领袖施略普尼科夫与库图佐夫（I. I. Kutuzov）吸纳入中央委员会，并否决了施略普尼科夫当场提出的辞职请求；
       5. **以粮食税取代余粮收集制（`1921-03-15`）**：需点明列宁早于喀琅施塔得起义爆发前的 `1921-02-08` 已在政治局起草《农民问题提纲初稿》、`02-24` 提交中央委员会；3月15日十大通过决议并在 `03-21` 由全俄中央执行委员会颁布法令，将 1921–1922 年度全国粮食征集额从 4.23 亿普特削减至 **2.4 亿普特**（减幅约 43%）。
     - **整改要求**：在 `[T2]` 补齐上述 5 组精确票数、日期与机构改选细节，并在 `[T3]` 挂接 `data/DATA-04-party-membership-and-congress-votes-1903-1929.md`。

  2. **[P1-02] 全卡漏挂所有 `CLM-*` 史学主张卡（0 张 `CLM-*`），且在引用 `RN-W35` 时遗漏合编者兼专章作者 Joseph Godson（1981）及柯伦泰《工人反对派》原典与精读札记**
     - **位置**：`**[T2] 史学位置与争鸣**` L42–43、`1.3 [T3]` L44–46。
     - **现象**：
       - L42 写“Schapiro与Lebsky围绕工会路线展开的比较则提醒，十大既保留工会的保护职能修辞，又把其更紧地嵌入国家与党的传动体系”，L46 挂接 `RN-W35-schapiro-vs-lebsky-soviet-trade-unions-and-industrial-paternalism-1917-1929.md`；但全卡**未挂接任何一张 `CLM-*` 主张卡**！
       - 更关键的是，核查 `RN-W35` 与 `historiography/claims/CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions.md` 可知：《The Soviet Worker: Illusions and Realities》（1981）一书中专门剖析**1921年十大确立工会“共产主义学校/传动带”双重职能及其向1929年单向国家生产机器蜕变**的第 4 章（`pp. 106–113`），作者是该书联合主编 **Joseph Godson**（而 Leonard Schapiro 撰写的是第 1 章导论 `CLM-schapiro-1981-end-of-illusion-unions-1917-to-tomsky-fall.md`）。卡片在 `[T2]` 只提 Schapiro 与 Lebsky 而完全隐去了 **Joseph Godson** 的署名与论断。
       - 同时，卡片完全漏挂了站内已有的柯伦泰 1921 年向十大提交的《工人反对派》纲领精读札记（`reading-notes/kollontai_1921_workers_opposition/RN-W29-kollontai-workers-opposition-1921.md`）及其两张 `CLM-kollontai-1921-*` 主张卡，以及 Daniels 与 Avrich 的核心 `CLM-*` 卡。
     - **整改要求**：
       - 在 `**[T2] 史学位置与争鸣**` 中补入 **Joseph Godson（1981）** 关于十大工会“双重职能（保护工人利益 vs. 提高生产）”在 NEP 时期尚存有限空间、至 1929 年被彻底改造成单向“传动带”的论断，以及 **柯伦泰（1921）**《工人反对派》对“全俄生产者代表大会”与官僚化专家治厂的批判；
       - 在 `1.3 [T3]` 补挂以下核心 `CLM-*` 与 `RN-*`：
         - `historiography/claims/CLM-daniels-1960-tenth-congress-turning-point.md`
         - `historiography/claims/CLM-schapiro-1981-end-of-illusion-unions-1917-to-tomsky-fall.md`
         - `historiography/claims/CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions.md`
         - `historiography/claims/CLM-lebsky-2021-nep-red-director-union-party-triangle.md`
         - `historiography/claims/CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists.md`
         - `historiography/claims/CLM-kollontai-1921-all-russian-congress-of-producers-program.md`
         - `historiography/claims/CLM-avrich-1970-soviets-without-bolsheviks.md`
         - `reading-notes/kollontai_1921_workers_opposition/RN-W29-kollontai-workers-opposition-1921.md`

  3. **[P2-01] `2.2 关系边表` 遗漏关键机构与辩论主角节点**
     - **位置**：`2.2 关系边表（Edges）` L33–39。
     - **现象**：边表仅列 5 条边，遗漏了十大工会争论与反派别斗争的核心人物与机构节点：`PER-trotsky`、`PER-bukharin`、`PER-shlyapnikov`、`PER-kollontai`、`PER-tomsky`、`PER-zinoviev`、`INS-politburo-orgburo-secretariat`、`ORG-democratic-centralists`。
     - **整改要求**：在 `2.2` 边表中补入上述核心节点。

---

### 03. `cards/meetings/MTG-1924-05-13th-party-congress.md`（俄共（布）第十三次代表大会（1924年5月））

- **机械与格式核验**：46 行，`[T1]` 127 字（`<= 150` 字，合规），全卡 6 个反引号 ID 与 10 条相对路径链接均存在（0 断链、0 悬空 ID）。
- **史源逐一对读与问题清单**：

  1. **[P1-01] 漏挂 Wave 39 新入库的 `sources/web-archive/W39_lenin_1922_1923_docs/` 列宁最后口授文献群（与《给代表大会的信》共同构成“列宁遗嘱”整体纲领并由克鲁普斯卡娅于 `1924-05-18` 一并移交的 S 级原典）**
     - **位置**：`1.2 [T2]` L25–26、`**[T2] 史学位置与争鸣**` L42、`1.3 [T3]` L45。
     - **现象**：
       - L42 明确写道：“Lewin把遗嘱放入列宁对官僚主义、民族问题及领导机制的更广泛批评，认为十三大接受了扩充中央等形式，却抽空了制衡总书记权力的精神”（对应 `CLM-lewin-1968-testament-intent.md` 的“三诫”：反大俄罗斯沙文主义、反官僚主义并改组工农检查院—中监委、撤换斯大林）；
       - 然而在 L45 的 `[T3]` 原典挂接中，卡片仅挂了 `1922-12_letter-to-the-congress.md` 与托洛茨基《新方针》公开信，**完全漏挂了 Wave 39 专门入库的 `sources/web-archive/W39_lenin_1922_1923_docs/` 系列原典**（以及 `1923-01-04_on-cooperation.md` 与 `1923-10-15_declaration-of-the-forty-six.md`）！
     - **核实证据**：据 `timeline/L3_daily/1924-01_lenin_death_testament_and_lessons_of_october.md#L94` 与 `W39_lenin_1922_1923_docs/` 馆藏导读，克鲁普斯卡娅于 **`1924-05-18`** 向中央遗嘱委员会正式移交的是列宁 1922 年 12 月至 1923 年 3 月口授的 **13 份文件整体**（含 7 篇已发表文章与 6 封未公开密件）；其中《关于民族或“自治化”问题》（1922-12-30/31）同样在各代表团内部宣读而未载入正式记录，而《我们怎样改组工农检查院》（1923-01-23）与《宁肯少些，但要好些》（1923-03-02）正是十三大将中央委员会扩编至 53 正式 + 34 候补、将中央监察委员会扩编至 151 人的直接制度蓝本。
     - **整改要求**：在 `1.3 [T3]` 补挂 Wave 39 入库的列宁最后口授文献群及 1923 年反对派关键原典：
       - `sources/web-archive/W39_lenin_1922_1923_docs/1922-12-30_lenin-question-of-nationalities-or-autonomisation.md`（《关于民族或“自治化”问题》）
       - `sources/web-archive/W39_lenin_1922_1923_docs/1923-01-23_lenin-how-we-should-reorganise-rabkrin.md`（《我们怎样改组工农检查院》）
       - `sources/web-archive/W39_lenin_1922_1923_docs/1923-03-02_lenin-better-fewer-but-better.md`（《宁肯少些，但要好些》）
       - `sources/web-archive/E02_E10_core_classics/1923-01-04_on-cooperation.md`（《论合作制》）
       - `sources/web-archive/E01_E10_supplements/1923-10-15_declaration-of-the-forty-six.md`（《四十六人声明》）

  2. **[P1-02] 漏引 `DATA-04` 与 `L3` 已核实的十三大代表票数结构（748名表决权代表中反对派0席）、“列宁征召”具体人数及破例赋予候补党员初选投票权、克鲁普斯卡娅 `1924-05-18` 移交日期与会后中枢改组数据，且在 `[T3]` 将部分已可核事实笼统归入“待结合代表大会速记记录继续校订”**
     - **位置**：`1.2 [T2]` L25–28、`1.3 [T3]` L44–46。
     - **现象**：
       - L25 仅写“1924年5月21日中央全会决定不在大会全体会议公开宣读《给代表大会的信》，改由5月22日长老会议和各代表团分团宣读”，遗漏了 **`1924-05-18` 克鲁普斯卡娅移交 13 份口授文件**的前置节点，以及长老会议上**加米涅夫主持宣读、季诺维也夫与加米涅夫以“列宁的忧虑已被实践证明不再存在”为由提议留任斯大林、克鲁普斯卡娅当场抗议但规定不得作速记、不得外传**的闭门操作细节（见 `timeline/L3_daily/1924-01_lenin_death_testament_and_lessons_of_october.md#L94-L101`）；
       - L27–28 提到“借助‘列宁征召’新入党的大批工人党员与既有委派网络”，却完全未给出站内 `DATA-04` 与 `L3` 已精确锁定的定量数据！
     - **核实证据**：据 `data/DATA-04-party-membership-and-congress-votes-1903-1929.md#L19, #L87` 与 `timeline/L3_daily/1924-01_lenin_death_testament_and_lessons_of_october.md#L71, #L103-L105`：
       1. **“列宁征召（Ленинский призыв）”与破例初选投票权**：1924年1月29日—31日中央全会启动“列宁征召”，至 5 月十三大召开前突击吸纳 **20 万—24 万**名工厂一线工人入党（1924–1925年累计达 63.8 万人，使全党规模从 1924 年初的 47.2 万猛增至 **735,881 人**）；更关键的是，**中央组织局破例允许尚无正式表决权的“列宁征召”新入党候补党员直接参加十三大代表基层初选投票**（Daniels `ch09`），从源头上稀释了老党员与知识分子对反对派的支持；
       2. **十三大代表结构**：出席大会代表共 **1,164 人**，其中**有表决权代表 748 人**、有发言权代表 416 人；在 748 名有表决权代表中，**左翼反对派未获哪怕 1 个有表决权席位（`0` 席）**，托洛茨基、普列奥布拉任斯基、拉狄克仅以有发言权代表身份列席；5月26日托洛茨基在大会发言重申“不论党是对是错，这是我的党”，大会全票确认一月十三次代表会议将反对派定性为“小资产阶级倾向”的决议；
       3. **会后中枢改组（`1924-05-31`—`06-02`）**：大会表面按列宁遗愿将中央委员会扩编至 **53 名正式委员、34 名候补委员**，将中央监察委员会扩编至 **151 人**；6月2日十三届一中全会确认斯大林连任总书记，**布哈林递补列宁遗缺升任政治局正式委员**（政治局 7 正式委员：季诺维也夫、加米涅夫、斯大林、托洛茨基、李可夫、托姆斯基、布哈林），捷尔任斯基、伏龙芝、索科利尼科夫任政治局候补委员，卡冈诺维奇进入书记处与组织局（并可衔接 `CLM-khlevniuk-2015-collective-leadership-erosion.md` 所述 1924 年 8 月由除托洛茨基外 6 名政治局委员 + 中监委主席古比雪夫组成的“七人小组 Седьмица”影子政治局）。
     - **整改要求**：在 `[T2]` 补入上述 3 组定量与制度细节，并在 `[T3]` 补挂 `data/DATA-04-party-membership-and-congress-votes-1903-1929.md` 与 `historiography/claims/CLM-daniels-1960-october-1923-bureaucratic-freeze.md`。

  3. **[P2-01] `2.2 关系边表` 遗漏关键机构与人物节点**
     - **位置**：`2.2 关系边表（Edges）` L33–40。
     - **现象**：边表未纳入 `INS-politburo-orgburo-secretariat`、`ORG-left-and-united-opposition`、`PER-bukharin`（十三大后升任政治局正式委员）。
     - **整改要求**：在 `2.2` 边表补入 `INS-politburo-orgburo-secretariat`、`ORG-left-and-united-opposition`、`PER-bukharin`。

---

## 四、阶段二逐卡深度对勘与分级问题清单（04–05 号会议卡）

### 04. `cards/meetings/MTG-1929-04-cc-joint-plenum.md`（联共（布）中央委员会与中央监察委员会四月联席全会）

- **机械与格式核验**：47 行，`[T1]` 114 字（`<= 150` 字，合规），全卡 5 个反引号 ID 与 8 条相对路径链接均存在（0 断链、0 悬空 ID）。
- **史源逐一对读与问题清单**：

  1. **[P0-01] 错配与 1929 年 4 月联席全会毫无交集的精读札记（`RN-W18`），在 `[T2]` 点名 Erlich 与 Davies 却漏挂 `RN-W3-great-industrialization-debate-1924-1928` 与 `RN-W6-agricultural-crisis-and-was-stalin-necessary`，且全卡挂接 `CLM-*` 数为 `0`**
     - **位置**：`2.3 史学争鸣光谱` L42、`[T3]` L46。
     - **现象**：
       - L42 写：“Cohen强调布哈林在新经济政策框架内所构想的替代道路；Khlevniuk重视政治局联盟、干部任命和组织权力；Davies与Erlich的经济研究提示粮食、投资及工业能力约束”；
       - L46 却把唯一的经济史札记挂接到了 `[Davies精读](../../reading-notes/davies_basil/RN-W18-1929-collectivization-takeoff-and-mensheviks-1917.md)`，对正文点名的 **Erlich** 完全未挂接任何札记或 `CLM-*`，且全卡**未挂接任何一张 `CLM-*` 史学主张卡（0 张 `CLM-*`）**！
     - **核实证据**：
       - 核查 `reading-notes/davies_basil/RN-W18-1929-collectivization-takeoff-and-mensheviks-1917.md`：该札记前半部分仅覆盖 **1929 年夏秋至 1930 年 1 月**的集体农庄跃进、十一月全会与十二月委员会，后半部分覆盖 **1917 年孟什维克组织崩解（John D. Basil, 1984）**，全文对 **1929 年 4 月中央与中监委联席全会、布哈林 4 月 18 日演说、斯大林 4 月 22 日报告命中数为 0**！
       - 真正讨论 1928–1929 年春粮食收购价格剪刀差、涅姆奇诺夫表与工业化投资约束的经济史札记是 **Carr & Davies (1969) / Nove (1964)** 的 `reading-notes/carr_davies_nove/RN-W6-agricultural-crisis-and-was-stalin-necessary.md`（对应 `CLM-carr-davies-1969-nemchinov-table-critique.md`、`CLM-carr-davies-1969-grain-price-scissor-1927.md`）以及 **Alexander Erlich (1960)** 的 `reading-notes/erlich_1960_industrialization/RN-W3-great-industrialization-debate-1924-1928.md`（对应 `CLM-erlich-1960-bukharin-dynamic-equilibrium.md`）。
     - **整改要求**：
       - 将 L46 错配的 `RN-W18` 替换为 `reading-notes/carr_davies_nove/RN-W6-agricultural-crisis-and-was-stalin-necessary.md` 与 `reading-notes/erlich_1960_industrialization/RN-W3-great-industrialization-debate-1924-1928.md`，并补挂 Lewin《俄国农民与苏维埃政权》札记 `reading-notes/lewin_1968_peasants/RN-W3-grain-crisis-and-collectivization-turn.md`、Kotkin 札记 `reading-notes/kotkin_2014_stalin_v1/RN-W1C-1928-siberian-turn-and-bukharin.md`、Merridale/Apalkov 札记 `reading-notes/merridale_apalkov/RN-W6-moscow-fall-and-party-struggle-rules.md` 及 Wave 39 新增的泽姆斯科夫札记 `reading-notes/stalin_era_economy_repression_1924_1954_zh/RN-W39-stalin-era-nep-to-great-turn-1924-1929.md`；
       - 在 `[T3]` 补挂核心 `CLM-*` 卡：
         - `historiography/claims/CLM-cohen-1973-nep-viability.md`
         - `historiography/claims/CLM-cohen-1973-bukharin-organizational-defeat.md`
         - `historiography/claims/CLM-cohen-1973-july-1928-plenum-and-kamenev.md`
         - `historiography/claims/CLM-khlevniuk-2015-defeat-of-right-opposition.md`
         - `historiography/claims/CLM-carr-davies-1969-nemchinov-table-critique.md`
         - `historiography/claims/CLM-erlich-1960-bukharin-dynamic-equilibrium.md`
         - `historiography/claims/CLM-lewin-peasants-1968-ural-siberian-method.md`
         - `historiography/claims/CLM-kotkin-2014-bukharin-dilemma.md`
         - `historiography/claims/CLM-apalkov-2023-collective-to-personal-dictatorship.md`
         - `historiography/claims/CLM-zemskov-2018-archival-constraints-and-party-radicalism.md`
         - `historiography/claims/CLM-zemskov-2018-agrarian-tribute-and-coercive-turn.md`

  2. **[P1-01] 漏引 `DATA-03` 定量数据卡及四月联席全会会场规模（300 余人围攻约 13 人）、会前 `1929-04-15` 弃权票、十六次代表会议一五计划集体化真实指标（`17.5%`），且将站内已可核的 6–8 月职务解除与公开点名时序误标为“确切日期仍需进一步核查”**
     - **位置**：`2.1 核心历史脉络` L25–28、`[T3]` L46。
     - **现象与核实证据**：
       1. **会前危机定量与 `1929-04-15` 五年计划弃权票**：据 `timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md#L199-L212` 与 `data/DATA-03-1926-1929-grain-procurement-and-nemchinov-table.md`，1929 年 2 月 9 日李可夫宣读布哈林起草的《三人纲领》（控诉个人专断取代集体领导、秘密清洗及自 1928 年 7 月起对农民实行“军事封建剥削”），遭政治局与中监委主席团秘密决议谴责；至 `1929-04-01`，乌克兰交粮从上年约 2 亿普特暴跌至 **2,670 万普特**，自由市场粮价高于官价 **190%–365%**，城市实行面包配给；3–4 月李可夫的两年农业补救计划被否，**`1929-04-15` 布哈林、李可夫、托姆斯基在政治局对五年计划投弃权票**；
       2. **四月联席全会会场规模与控辩交锋细节（`1929-04-16` 至 `04-23`）**：据 `RN-W3-bukharin-stalin-1928-1929-showdown.md#L49`（Cohen `pp. 308–313`）与 `sources/web-archive/W32_milestone_docs/1929-04-18_bukharin-april-plenum-speech-defense-of-nep.md#L38-L41`，全会呈现**约 300 余名中央委员与中监委委员围攻约 13 名右派支持者**的悬殊局面；布哈林在 **`1929-04-18`（第 5 次晨会与第 6 次晚会）**长篇发言中，不仅宣读 **`1928-06-01/02` 致斯大林私信**与农业积累笔记（“用一千张木犁也拼不出一台拖拉机”），而且明确指斥把“乌拉尔—西伯利亚方法”常态化使“粮食出卖者变成了粮食交纳者，买卖变成了国家贡赋（`государственная дань`）”，痛斥“不要跑到加米涅夫那里去，但也不要用赤裸裸的肉体拳头政策（`голая политика физического кулака`）来代替思想和思考！”；斯大林在 **`1929-04-22`**《论联共（布）党内的右倾》（当时报刊删去 30 余页未发表，后收入《斯大林全集》第 12 卷）中除揭露加米涅夫密谈外，还恶毒影射布哈林 1918 年布列斯特争论期间曾密谋“监禁列宁”；
       3. **职务解除与对外公开点名的确切分期（站内已核，非“待核查”）**：四月联席全会决定解除布哈林在《真理报》与共产国际、托姆斯基在全苏工会的职务，但**对外严格保密、未公开点名决裂，且保留三人的政治局席位**；具体执行时序在站内 `L3#L227-L235` 与 `RN-W3#L50-L51` 已核清：**1929 年 6 月**全苏工会中央理事会正式免去托姆斯基职务并清洗其派系，同月布哈林改任最高国民经济委员会（VSNKh）科技管理局主任；**1929 年 7 月**共产国际执委会第十次全会（莫洛托夫主持）正式解除布哈林共产国际执委会主席团职务并确立“第三时期”极左路线；**`1929-08-21` 与 `08-24`**《真理报》才首次向全党全国公开点名批判布哈林；
       4. **十六次党代表会议（`1929-04-23` 至 `04-29`）一五计划的真实集体化基准**：L28 写“紧接着十六次党代表会议批准一五计划最优方案”，必须标明该“最优方案”**仍预设到五年计划期末（1932/33 年）集体农庄与国营农场仅占全国播种面积的 `17.5%`**，整体仍留在新经济政策框架内（Cohen `p. 329`）。
     - **整改要求**：在 `2.1` 补入上述 4 项精确史实与定量基准，在 `[T3]` 挂接 `data/DATA-03-1926-1929-grain-procurement-and-nemchinov-table.md`（及 `DATA-04`），并删去 L46 将站内已核实的 6/7/8 月职务执行时序泛化为“仍需进一步核查”的表述。

  3. **[P2-01] 章节标题格式统一与 `2.2 关系边表` 补充**
     - **位置**：L19、L22、L30–39、L44。
     - **现象**：04–05 号卡采用 `## [T1] 150字定性微摘要` / `## [T2]` / `## [T3]` 标题，与 01–03 号卡的 `## 一、核心档案内容` + `### 1.1 [T1] 核心定义` 格式不一致；`2.2` 边表漏挂 `INS-politburo-orgburo-secretariat`、`PER-kamenev`、`PER-molotov`、`EVT-1928-grain-procurement-crisis`。
     - **整改要求**：统一章节标题规范，并在 `2.2` 边表补入上述节点。

---

### 05. `cards/meetings/MTG-1929-11-cc-plenum.md`（联共（布）中央委员会十一月全会（1929））

- **机械与格式核验**：48 行，`[T1]` 119 字（`<= 150` 字，合规），全卡 7 个反引号 ID 与 12 条相对路径链接均存在（0 断链、0 悬空 ID）。
- **史源逐一对读与问题清单**：

  1. **[P0-01] 引用《苏联农村的悲剧》第 2 卷札记与两张 `CLM-tragedy-village-1929-*` 时完全隐去四位主编（维·彼·丹尼洛夫 V. P. Danilov、罗·曼宁 R. T. Manning、琳达·维奥拉 L. Viola、尼·阿·伊夫尼茨基 N. A. Ivnitsky）及卷首长篇导言作者伊夫尼茨基的学者署名**
     - **位置**：`2.3 史学争鸣光谱` L43、`[T3]` L47。
     - **现象**：
       - L47 挂接了 `reading-notes/tragedy_village_1929/RN-W20-nov-dec-1929-politburo-commission-and-ogpu-archives.md`、`historiography/claims/CLM-tragedy-village-1929-november-plenum-escalation.md` 与 `historiography/claims/CLM-tragedy-village-1929-politburo-dekulakization-commission.md`；
       - 然而在 L43 的 `2.3 史学争鸣光谱` 中，卡片在点名 `Cohen`、`Khlevniuk`、`Davies` 之后，仅以匿名书名写道：“《苏联农村的悲剧》提供政治局及地方档案，揭示行政动员和农民承受的压力”，**完全隐去了该档案集第 2 卷的四位主编（维·彼·丹尼洛夫 `В. П. Данилов`、罗·曼宁 `R. T. Manning`、琳达·维奥拉 `L. Viola`、尼·阿·伊夫尼茨基 `Н. А. Ивницкий`）以及撰写第 2 卷 A 级学术导言（`ch01_引言_展开_全面_集体化_н_а_ивницкий.md`）的伊夫尼茨基的真实署名**！
     - **核实证据**：核查 `RN-W20-nov-dec-1929-politburo-commission-and-ogpu-archives.md#L7-L11` 与 `CLM-tragedy-village-1929-november-plenum-escalation.md#L4`，明确标注 `editors: ["В. П. Данилов", "Р. Т. Маннинг", "Л. Виола", "Н. А. Ивницкий"]`、`scholar: SCH-danilov-ivnitsky-eds` 以及卷首伊夫尼茨基长篇导言。只写书名《苏联农村的悲剧》而抹去 Danilov、Manning、Viola、Ivnitsky 的署名，违反了知识库史学史卡片“严禁隐去真实作者/主编署名”的 P0 铁律。
     - **整改要求**：在 `2.3 史学争鸣光谱` 与 `[T3]` 中明确补入 **Danilov、Manning、Viola、Ivnitsky（丹尼洛夫、曼宁、维奥拉、伊夫尼茨基）** 四位主编及导言作者 **伊夫尼茨基（N. A. Ivnitsky）** 的署名，并补挂同源的第 3 张论断卡 `historiography/claims/CLM-tragedy-village-1929-peasant-self-liquidation-and-flight.md`。

  2. **[P1-01] 漏挂 Wave 39 新增的泽姆斯科夫精读札记（`RN-W39`）与 `CLM-zemskov-*` 主张卡，漏挂 `DATA-06` / `DATA-03` 定量数据卡，且在 `[T2]` 点名 Cohen 与 Khlevniuk 却未在 `[T3]` 挂接其札记与 `CLM-*`**
     - **位置**：`2.3 史学争鸣光谱` L43、`[T3]` L46–47。
     - **现象**：
       1. **漏挂 Wave 39 泽姆斯科夫馆藏**：未挂接 `reading-notes/stalin_era_economy_repression_1924_1954_zh/RN-W39-stalin-era-nep-to-great-turn-1924-1929.md` 及 `historiography/claims/CLM-zemskov-2018-archival-constraints-and-party-radicalism.md`、`historiography/claims/CLM-zemskov-2018-agrarian-tribute-and-coercive-turn.md`、`historiography/claims/CLM-zemskov-1929-dekulakization-demographic-baseline.md`；
       2. **正文点名 Cohen 与 Khlevniuk 却在 `[T3]` 漏挂其札记与 `CLM-*`**：L43 正文点名了 Cohen 与 Khlevniuk，但 L46–47 的 `[T3]` 仅挂接了《苏联农村的悲剧》与 Davies，完全未挂接 `reading-notes/cohen_1973_bukharin/RN-W3-bukharin-stalin-1928-1929-showdown.md`、`historiography/claims/CLM-cohen-1973-bukharin-organizational-defeat.md`、`reading-notes/khlevniuk_2015_stalin/RN-W3-politburo-apparatus-and-1929-victory.md`、`historiography/claims/CLM-khlevniuk-2015-defeat-of-right-opposition.md`，亦漏挂了 Davies 关于 1929 年秋《大转变的一年》统计争议的 `historiography/claims/CLM-davies-1980-autumn-1929-great-turn-fabrication.md`；
       3. **漏挂 `DATA-06` 定量数据卡**：未挂接专门收录 1929 年 6–12 月集体化跃升、粮食征购翻倍（`1,361.6 万吨` vs. 上年同期 `634.5 万吨`）与 OGPU 征粮专项逮捕（`49,068 人`）的 `data/DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md`。
     - **整改要求**：在 `2.3` 补入泽姆斯科夫（Viktor Zemskov）关于执政党内战干部激进心态及 1929 年末地方驱逐与 1930-01-30 制度化分期的视角，并在 `[T3]` 补齐上述 `RN-W39`、`CLM-zemskov-*`、`DATA-06` 及 Cohen/Khlevniuk/Davies 的 `RN-*` 与 `CLM-*`。

  3. **[P1-02] 漏写十一月全会与十二月委员会博弈的若干核心日期、决议双层结构与定量锚点（`1929-11-12` 三人抗辩声明、乌加罗夫受警告、“二万五千人” `26,380 / 27,519` 定数、科西奥尔承认乌克兰虚报、鲍曼三类富农方案与 `12-18` 一致草案在 `12-25` 遭斯大林亲笔信否决）**
     - **位置**：`2.1 核心历史脉络` L25–28。
     - **现象与核实证据**：
       1. **`1929-11-12` 三人抗辩声明与 `1929-11-17` 两份不同决议的精确区分**：据 `sources/web-archive/W32_milestone_docs/1929-11-17_cpsu-november-plenum-resolution-right-deviation.md#L18-L52`，布哈林、李可夫、托姆斯基于 **`1929-11-12`** 向全会提交最后抗辩声明；**`1929-11-17`** 全会通过专项决议《关于布哈林同志集团》（`РГАСПИ. Ф. 17. Оп. 2. Д. 422. Л. 5–6`，将布哈林开除出政治局，对李可夫、托姆斯基及**乌加罗夫 Ф. Я. Угаров** 发出警告），同时依据斯大林致莫洛托夫亲笔便条（`РГАСПИ. Ф. 558. Оп. 1. Д. 5279`）及鲁祖塔克动议，在全会主决议《关于 1929/30 年度国民经济控制数字》第六节写入“宣布宣传右倾机会主义观点及对它的调和态度与留在联共（布）队伍内不相容”（次日 **`1929-11-18`** 载于《真理报》第 268 号）；全会闭幕 8 天后，托姆斯基、布哈林、李可夫于 **`1929-11-25`** 签署公开检讨声明，次日（**`1929-11-26`**）载于《真理报》第 278 号；
       2. **“二万五千人”下乡与全苏农业人民委员部（НКЗем）**：全会决定动员 **2.5 万名**工业工人长期赴农村领导集体化（逾 7 万人报名，`1929-12-18` 中央批准控制额 **26,380 人**、实际选拔 **27,519 人**，见 `RN-W20#L80` / `DATA-06`），并决定设立全苏农业人民委员部（**`1929-12-07`** 成立，雅科夫列夫任人民委员）；会上除锡尔佐夫（Syrtsov）宣读霍皮奥尔专区（Khoper）调查外，乌克兰书记科西奥尔（Kosior）亦当场承认部分乌克兰村庄所谓“全面集体化”系居民不知情的虚报（Davies `Vol. 1 p. 165`），而莫洛托夫与下伏尔加书记谢博尔达耶夫（Sheboldaev）则在全会与会后（`11-24/25` 萨拉托夫联席会议 Doc 1）率先推动下伏尔加于 1930 年内全面集体化；
       3. **12月5日雅科夫列夫 18 人委员会内部博弈的完整转折链**：L28 仅写“12月5日政治局设雅科夫列夫主持的集体化委员会，富农政策由其分组研究；12月27日斯大林农业演说公开提出转向消灭富农阶级”，遗漏了 `CLM-tragedy-village-1929-politburo-dekulakization-commission.md` 的核心论证——**`1929-12-08` 设 8 个分委员会，鲍曼（K. Ya. Bauman）富农政策分委员会（`≤12-14`，Doc 4）鉴于全苏富农达 500 万–600 万人认为“全体迁徙是绝望的”，提出三类差别化处置（拟将大多数富农剥夺生产资料后留在集体农庄无选举权试用 3–5 年）；`1929-12-18` 委员会一致草案（Doc 12，`12-22` 呈政治局）设定主产粮区 2–3 年完成、以农业劳动组合为主体、保留奶牛/小畜/小农具私有权及自愿退社退股；但 `1929-12-25` 斯大林致信莫洛托夫（Doc 16）明确否决（“这个草案，我认为不合适”），随即在 `12-27` 马克思主义土地学家会议上公开宣布“把富农作为阶级消灭”，并在 `1930-01-01` 至 `01-05` 政治局第 112 号会议最终决议（Docs 23–24）中删净全部保护条款**。
     - **整改要求**：在 `2.1` 中补入上述 3 组关键日期、定量数字与委员会博弈转折链。

  4. **[P2-01] 章节标题格式统一与 `2.2 关系边表` 补充**
     - **位置**：L19、L22、L30–40、L45。
     - **现象**：标题层级同 04 号卡；`2.2` 边表可补充 `INS-politburo-orgburo-secretariat`、`POL-first-five-year-plan`。

---

## 五、汇总修复动作矩阵（Action Matrix for Remediation）

| 优先级 | 目标卡片 | 具体问题定位 | 强制修复动作（精确到文件路径、数据与署名） |
| :---: | :--- | :--- | :--- |
| **P0-1** | `cards/meetings/MTG-1919-03-8th-party-congress.md` | L26, L41, L44 错配对八大/军事反对派/民主集中派 **0 命中**的 `RN-W1C` 与 `RN-W20` | 将 Daniels 出处改为馆藏原书分卷 `sources/monographs/daniels_1960_conscience/ch04_pages_101-125.md`（`[pp. 93–107]`）与 `ch05_pages_126-150.md`（`[pp. 110–113]`）；明确 `RN-W20` 仅作红军军事专家制度背景，八大军事秘密会议交锋以 Daniels Ch. 4 为准。 |
| **P0-2** | `cards/meetings/MTG-1929-04-cc-joint-plenum.md` | L42, L46 错配对 1929 年 4 月全会 **0 命中**的 `RN-W18`，点名 Erlich 却未挂其札记/主张卡 | 移除错配的 `RN-W18`，改挂 `reading-notes/carr_davies_nove/RN-W6-agricultural-crisis-and-was-stalin-necessary.md`、`reading-notes/erlich_1960_industrialization/RN-W3-great-industrialization-debate-1924-1928.md`、`reading-notes/lewin_1968_peasants/RN-W3-grain-crisis-and-collectivization-turn.md`、`reading-notes/kotkin_2014_stalin_v1/RN-W1C-1928-siberian-turn-and-bukharin.md`、`reading-notes/merridale_apalkov/RN-W6-moscow-fall-and-party-struggle-rules.md`。 |
| **P0-3** | `cards/meetings/MTG-1929-11-cc-plenum.md` | L43, L47 引用《苏联农村的悲剧》第 2 卷及两张 `CLM-tragedy-village-1929-*` 时完全隐去四位主编及导言作者署名 | 在 `2.3` 与 `[T3]` 明确写出四位主编 **V. P. Danilov（维·彼·丹尼洛夫）、R. T. Manning（罗·曼宁）、L. Viola（琳达·维奥拉）、N. A. Ivnitsky（尼·阿·伊夫尼茨基）** 及第 2 卷长篇导言作者 **伊夫尼茨基（N. A. Ivnitsky）** 署名，并补挂 `historiography/claims/CLM-tragedy-village-1929-peasant-self-liquidation-and-flight.md`。 |
| **P1-1** | `cards/meetings/MTG-1919-03-8th-party-congress.md` | L25–27, L46 漏引 `DATA-04` 代表数、军事问题秘会票数（`174 : 95`）、首届常设政治局名单，并将会后机构名单误标为“仍需逐页对勘” | 补入 `DATA-04`（301 表决权代表 + 102 发言权代表，313,766 党员）、军事秘密会议支持托洛茨基路线（索科利尼科夫报告）**`174` 票** vs. 弗·米·斯米尔诺夫军事反对派 **`95` 票**、中央 19 正式 + 8 候补、首届常设政治局（5正式：列宁、托洛茨基、斯大林、加米涅夫、克列斯廷斯基；3候补：季诺维也夫、布哈林、加里宁）与责任书记克列斯廷斯基；标明 Carr（1950）与 Daniels（1960）关于斯大林是否自 1919 年 3 月起即入首届组织局的记载差异。 |
| **P1-2** | `cards/meetings/MTG-1919-03-8th-party-congress.md` | L25–28, L44 漏写八大否定党联邦制（乌/拉/立/白共中央降为区域委员会）与苏维埃强制党团条款，漏挂 4 张 `CLM-carr-*` | 补入八大组织决议宣布乌克兰、拉脱维亚、立陶宛、白俄罗斯共产党中央仅为俄共区域委员会（`областные комитеты`）及党在苏维埃实行“完全政治统治”条款；补挂 `CLM-carr-1950-politburo-orgburo-displacement-of-state-organs.md`、`CLM-carr-1950-soviet-to-party-ascendancy-mechanism.md`、`CLM-carr-1950-self-determination-to-federal-reunion.md`、`CLM-carr-1952-war-communism-internal-contradictions.md` 及 `data/DATA-04-party-membership-and-congress-votes-1903-1929.md`。 |
| **P1-3** | `cards/meetings/MTG-1921-rcpb-10th-congress.md` | L25–28, L44–46 全漏 `DATA-04`、出席代表人数、工会三大纲领票数（`336 : 50 : 18`）、禁派令票数（`<30`）、第 7 条首次公开日期（`1924-01-17`）及粮食税减幅 | 挂接 `data/DATA-04-party-membership-and-congress-votes-1903-1929.md`；补入 694 表决权代表 + 296 发言权代表（732,521 党员，近 300 代表赴喀琅施塔得）、工会表决 **`336 : 50 : 18`（弃权 2）**、《关于党的统一》反对票 `<30` 张及第 7 条至 `1924-01-17` 才由斯大林公开、中央扩至 25 正式委员（列宁派 `20:5`，莫洛托夫任责任书记，吸纳施略普尼科夫与库图佐夫入中央）、粮食税从 4.23 亿普特减至 **2.4 亿普特**（列宁 `1921-02-08` 初稿早于喀琅施塔得起义）。 |
| **P1-4** | `cards/meetings/MTG-1921-rcpb-10th-congress.md` | L42–46 全卡 `0` 挂接 `CLM-*`，引用 `RN-W35` 漏掉专章作者 **Joseph Godson (1981)**，且漏挂柯伦泰《工人反对派》札记 `RN-W29` | 在 `[T2]` 补入 **Joseph Godson（1981）** 与 **柯伦泰（1921）** 署名及论点；在 `[T3]` 补挂 `RN-W29-kollontai-workers-opposition-1921.md` 及 7 张 `CLM-*`（`CLM-daniels-1960-tenth-congress-turning-point`、`CLM-schapiro-1981-end-of-illusion-unions-1917-to-tomsky-fall`、`CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions`、`CLM-lebsky-2021-nep-red-director-union-party-triangle`、`CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists`、`CLM-kollontai-1921-all-russian-congress-of-producers-program`、`CLM-avrich-1970-soviets-without-bolsheviks`）。 |
| **P1-5** | `cards/meetings/MTG-1924-05-13th-party-congress.md` | L25–26, L42, L45 漏挂 Wave 39 新入库的 `W39_lenin_1922_1923_docs/` 列宁最后口授文献群及《论合作制》《四十六人声明》 | 在 `[T3]` 补挂 `sources/web-archive/W39_lenin_1922_1923_docs/1922-12-30_lenin-question-of-nationalities-or-autonomisation.md`、`1923-01-23_lenin-how-we-should-reorganise-rabkrin.md`、`1923-03-02_lenin-better-fewer-but-better.md` 以及 `1923-01-04_on-cooperation.md`、`1923-10-15_declaration-of-the-forty-six.md`。 |
| **P1-6** | `cards/meetings/MTG-1924-05-13th-party-congress.md` | L25–28, L44–46 漏引 `DATA-04` 与 `L3` 中十三大代表票数（748表决权代表中反对派0席）、列宁征召人数与候补党员破例初选投票权、`1924-05-18` 移交日及会后中枢改组名单 | 挂接 `data/DATA-04-party-membership-and-congress-votes-1903-1929.md` 与 `CLM-daniels-1960-october-1923-bureaucratic-freeze.md`；补入 `1924-05-18` 克鲁普斯卡娅移交 13 份口授文件、“列宁征召”吸纳 20万–24万工人且组织局破例准许候补党员参加十三大初选投票、1,164 代表（**748 表决权代表中反对派 `0` 席**）、中央扩至 53 正式 + 34 候补及中监委 151 人、`06-02` 布哈林升任政治局正式委员。 |
| **P1-7** | `cards/meetings/MTG-1929-04-cc-joint-plenum.md` | L25–28, L42–46 全卡 `0` 挂接 `CLM-*` 与 `DATA-03`，漏挂 Wave 39 泽姆斯科夫 `RN-W39` / `CLM-zemskov-2018-*`，漏写 300 对 13 会场规模、十六次代表会议 `17.5%` 集体化指标及 6/7/8 月职务执行时序 | 补挂 `data/DATA-03-1926-1929-grain-procurement-and-nemchinov-table.md`、`RN-W39-stalin-era-nep-to-great-turn-1924-1929.md` 及 11 张 `CLM-*`（Cohen 3 张、Khlevniuk、Carr-Davies、Erlich、Lewin、Kotkin、Apalkov、Zemskov 2 张）；补入 `04-15` 五年计划弃权票、约 300 对 13 会场围攻、6月洗工会/7月共产国际十中全会免职/`08-21,24`《真理报》首次公开点名、十六次代表会议一五计划仍设五年后集体/国营农场仅占播种面积 **`17.5%`**。 |
| **P1-8** | `cards/meetings/MTG-1929-11-cc-plenum.md` | L43, L46–47 漏挂 Wave 39 泽姆斯科夫 `RN-W39` 与 `CLM-zemskov-*`、漏挂 `DATA-06`、正文点名 Cohen 与 Khlevniuk 却未在 `[T3]` 挂其 `RN-*` 与 `CLM-*` | 在 `[T3]` 补挂 `RN-W39-stalin-era-nep-to-great-turn-1924-1929.md`、`CLM-zemskov-2018-archival-constraints-and-party-radicalism.md`、`CLM-zemskov-2018-agrarian-tribute-and-coercive-turn.md`、`CLM-zemskov-1929-dekulakization-demographic-baseline.md`、`data/DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md`、`RN-W3-bukharin-stalin-1928-1929-showdown.md`、`CLM-cohen-1973-bukharin-organizational-defeat.md`、`RN-W3-politburo-apparatus-and-1929-victory.md`、`CLM-khlevniuk-2015-defeat-of-right-opposition.md`、`CLM-davies-1980-autumn-1929-great-turn-fabrication.md`。 |
| **P1-9** | `cards/meetings/MTG-1929-11-cc-plenum.md` | L25–28 漏写 `1929-11-12` 三人抗辩声明、乌加罗夫受警告、“二万五千人”（`26,380 / 27,519`）与全苏农业人民委员部（`12-07`）、鲍曼组三类富农方案与 `12-18` 一致草案在 `12-25` 遭斯大林亲笔信否决 | 补入 `11-12` 抗辩声明、`11-17`《关于布哈林同志集团》（逐出布哈林，警告李可夫、托姆斯基、乌加罗夫）与《控制数字》第六节“右倾与留党不相容”双决议（`11-18` 见报）、“二万五千人”（`12-18` 核定 26,380、实选 27,519）与 `12-07` 成立全苏农业人民委员部、科西奥尔在全会承认部分乌克兰村虚报、`≤12-14` 鲍曼组三类富农方案 → `12-18` 一致草案保留奶牛/小农具私有与退社权 → `12-25` 斯大林致莫洛托夫信否决（“我认为不合适”）→ `12-27` 演说 → `1930-01-05` 决议删净保护条款。 |
| **P2-1..5** | 全部 5 张 `MTG-*` 卡 | `2.2 关系边表` 核心参与者与机构节点遗漏；04–05 号卡标题层级与 01–03 号卡不一致 | 补齐各卡 `2.2` 边表中的核心辩论人物与 `INS-politburo-orgburo-secretariat` 节点；将 04–05 号卡的章节标题格式与 01–03 号卡统一。 |
