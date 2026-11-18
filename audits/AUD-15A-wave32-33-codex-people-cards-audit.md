# AUD-15A｜第32—33波 Codex 编纂人物卡异源交叉审计报告（7张）

- **审计日期**：2026-11-18
- **审计角色**：`dialectic-auditor`（异源交叉审计：Google Gemini-4 审读 OpenAI `codex/gpt-6.1-terra` 撰写的 7 张人物卡）。
- **唯一写入目标**：[`audits/AUD-15A-wave32-33-codex-people-cards-audit.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-15A-wave32-33-codex-people-cards-audit.md)；严禁直接修改任何被审卡片、札记、时间线、上下文包或共享总表。
- **审计对象（共 7 张，分两批落盘）**：
  - **前半批（01–04）**：[`PER-struve.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-struve.md)、[`PER-guchkov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md)、[`PER-rodzianko.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md)、[`PER-savinkov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-savinkov.md)
  - **后半批（05–07）**：[`PER-sukhanov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sukhanov.md)、[`PER-yagoda.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md)、[`PER-mikoyan.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-mikoyan.md)

---

## 一、审计方法与判级准则

1. **方法论**：逐行审读各卡 YAML 头信息与 `[T1]`/`[T2]`/`[T3]` 正文，并对照三类独立核验源：(a) 图谱一致性检验（`python scripts/kb.py audit-graph`）与 1-hop 平衡上下文包（`graph/packs/PER-*.md`）；(b) 站内 S/A 级馆藏（`sources/monographs/`、`sources/web-archive/`、`reading-notes/`、`historiography/`、`timeline/L3_daily/` 与既有互链卡）；(c) 外部原始/权威文献与日期转换核验（`python scripts/kb.py date`、实测卡片外链可达性与原文匹配度）。
2. **双历法与发生地规则（依 `AGENTS.md` §2.5）**：
   - 19 世纪俄国本土事件（`1800-03-01` 至 `1900-02-28`）：`[O.S.]` 转 `[N.S.]` 严格 **`+12` 天**；
   - 20 世纪改历前俄国本土事件（`1900-03-01` 至 `1918-01-31 [O.S.]`）：严格 **`+13` 天**；
   - 西欧出版物/事件与流亡欧洲逝世（斯图加特《解放》、巴黎、贝尔格莱德/南斯拉夫）：使用当地公历 `[N.S.]`；
   - `1918-02-14` 苏俄改历后本土事件（莫斯科、卢比扬卡等）：纯公历（`[N.S.]` 或纯 ISO 公历）。
3. **严重度判级**：
   - **P0（硬伤）**：断链/失效或错域 URL、明确史实或年代错误、伪造或与原文不符的直引、历法换算硬伤、自相矛盾。
   - **P1（口径/任期/学派与馆藏失衡）**：绕开库内已有的 S/A 级一手原典/专著/L3 时间线却采用 C 级百科或泛称“待核查”、职务头衔或起止年月过粗/缺失、把事后辩护回忆或单一学派解释当成共识、引用未建卡争鸣 ID、关键转折缺环。
   - **P2（措辞与结构打磨）**：Frontmatter `dates` 字段与 [`docs/TEMPLATES.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/docs/TEMPLATES.md) 不一致（如 `start_year`/`end_year` 替代 `start_ns`/`end_ns`）、关系边表“核心依据”笼统、日期书写规范化。

---

## 二、历法与生卒日期复核表（前半批 01–04）

> 注：前 4 张卡的 Frontmatter `dates` **全部未按 [`docs/TEMPLATES.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/docs/TEMPLATES.md) 规范给出 `start_ns`/`end_ns` 精确日期**（仅填年份或混搭）。下表除验算卡内正文日期外，亦用 `python scripts/kb.py date` 核出应补的标准生卒双历/公历锚点。

| 人物（卡 ID） | 卡内 `dates` 原样 | 卡内正文日期验算 | 应补标准生卒日期（经 `kb.py date` 与外部档案核验） | 判定 |
| :--- | :--- | :--- | :--- | :--- |
| **司徒卢威**（`PER-struve`） | `start_year: 1870` / `end_year: 1944`（缺具体月日） | 正文无完整日级双历；1902《解放》斯图加特出版属西欧公历语境，不套俄历合规（L41） | 生于 `1870-01-26 [O.S.] / 1870-02-07 [N.S.]`（彼尔姆，+12 天）；卒于 `1944-02-22 [N.S.]`（巴黎，少数文献记 `02-26`，单公历） | **缺精准生卒锚点；斯图加特西欧口径合规** |
| **古契科夫**（`PER-guchkov`） | `start_year: 1862` / `end_year: 1936`（缺具体月日） | `1917-03-02 [O.S.] / 1917-03-15 [N.S.]`（+13，正确）；`1917-04-29 / 04-30 / 05-01 [O.S.]` 对 `05-12 / 05-13 / 05-14 [N.S.]`（+13，正确） | 生于 `1862-10-14 [O.S.] / 1862-10-26 [N.S.]`（莫斯科，+12 天）；卒于 `1936-02-14 [N.S.]`（巴黎，单公历） | **正文换算正确；缺生卒精准日期** |
| **罗将柯**（`PER-rodzianko`） | `start_year: 1859` / `end_year: 1924`（缺具体月日） | `1917-02-26 [O.S.] / 1917-03-11 [N.S.]`（+13）；`1917-02-27 [O.S.] / 1917-03-12 [N.S.]`（+13）；`1917-03-03 [O.S.] / 1917-03-16 [N.S.]`（+13） | 生于 `1859-02-09 [O.S.] / 1859-02-21 [N.S.]`（叶卡捷琳诺斯拉夫省，+12 天）；卒于 `1924-01-24 [N.S.]`（南斯拉夫别奥德拉，巴尔干/当地已用公历） | **正文换算正确；缺生卒精准日期** |
| **萨温科夫**（`PER-savinkov`） | `start_year: 1879` / `end_ns: "1925-05-07"`（字段混搭） | `1925-05-07 [N.S.]`（L28，改历后莫斯科卢比扬卡单公历，正确） | 生于 `1879-01-19 [O.S.] / 1879-01-31 [N.S.]`（哈尔科夫，+12 天）；卒于 `1925-05-07 [N.S.]`（莫斯科） | **死期公历合规；生期与 schema 须统一** |

---

## 三、前半批逐卡审计与修复方案（01–04）

### 01｜彼得·伯恩哈多维奇·司徒卢威（`PER-struve`）

**审计对象**：[`PER-struve.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-struve.md)（共 44 行）；关联包：[`graph/packs/PER-struve.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-struve.md)。
**外链实测**：巴登—符腾堡州档案馆 PDF（L41，[`AN66_Gesamtdatei_web_Einzelseiten.pdf`](https://www.landesarchiv-bw.de/sixcms/media.php/120/AN66_Gesamtdatei_web_Einzelseiten.pdf)）**真实有效**，确为 *Archivnachrichten 66 / März 2023* 专题文章 *"Der russische Politiker und Ökonom Peter Struve als Redakteur in Stuttgart (1902–1904)"*；未见伪直引（L43 声明未使用未核对直引）。

#### 01-01｜P1｜架空库内 S/A 级高权威馆藏，却以 C 级通用百科（`encyclopedia.com`）与“待核查”代替实证

- **定位**：[`PER-struve.md:13-15`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-struve.md#L13-L15)、[`L25-L38`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-struve.md#L25-L38)、[`L42-L43`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-struve.md#L42-L43)。
- **核证与判断**：
  1. 卡片将 `primary-text-close-reading` 与 `soviet-orthodox` 列为 `perspectives_missing`（L14），并依赖 C 级网络百科 `encyclopedia.com`（L42）支撑 1898 年《宣言》与弗兰格尔政府履历（违反 `AGENTS.md` §2.4“通用百科不得承担最终证据”原则），同时在 L43 将“1894年著作、1898年《宣言》…邓尼金特别会议的确切职衔与任期”全盘归入“待核查”。
  2. 实际上，知识库内已有大量直接涉及司徒卢威的 A 级札记、概念卡、人物卡与专著分章，完全被本卡忽略：
     - **合法马克思主义与 1894–1899 论战**：[`RN-W1B-populism-concept-and-marxism.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/walicki_1969_controversy/RN-W1B-populism-concept-and-marxism.md#L163-L179)（`pp. 165–179`）与 [`RN-W2-populism-concept-and-marxism.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/walicki_1969_controversy/RN-W2-populism-concept-and-marxism.md#L130) 已系统梳理 1894 年《俄国经济发展问题批判杂记》（含“承认缺乏文化，到资本主义学校去”命题、`p. 288`）、1898 年《宣言》与伯恩斯坦前瞻、以及列宁（CW 1:504; 21:222）和普列汉诺夫对“狭隘客观主义”的批判；
     - **《路标》论战与双向互链**：[`CON-intelligentsia-and-vekhi.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-intelligentsia-and-vekhi.md#L35-L36) 已在 L35–36 与 L52 双向对接 `PER-struve`，详析 1909 年《路标》中司徒卢威“反国家狂热”批判与基斯佳科夫斯基、格尔申宗的内部分歧，以及米留可夫切割、列宁 `1909-12-13 [O.S.] / 12-26 [N.S.]`《论〈路标〉》反击；
     - **战时立宪民主党内分裂**：[`gaida_2003_liberal_opposition_zh/ch04_pages_101-125.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/gaida_2003_liberal_opposition_zh/ch04_pages_101-125.md#L435)（`p. 119`）与 [`ch07_pages_176-200.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/gaida_2003_liberal_opposition_zh/ch07_pages_176-200.md#L226-L237) 明确记载司徒卢威在 **1915 年 6 月 8 日 [O.S.]** 因反对米留可夫妥协路线宣布退出立宪民主党中央委员会（此前边表 L32 笼统写 `1905后`，抹平了战时党内右翼分裂）；
     - **内战“九人团”→全国中心→邓尼金/弗兰格尔**：[`mawdsley_1987_civil_war_zh/ch12`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/mawdsley_1987_civil_war_zh/ch12_第二部分_1919_白军之年_part_4.md#L799-L826) 记录其 1918 年参加莫斯科地下“九人团”、退出右翼中心另组亲协约国“全国中心”（Национальный центр）、赴顿河任文职；[`ch13`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/mawdsley_1987_civil_war_zh/ch13_第二部分_1919_白军之年_part_5.md#L736) 记录 1919 年在罗斯托夫起草“民族党”章程；[`PER-wrangel.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-wrangel.md#L27-L68) 与 [`mawdsley ch15`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/mawdsley_1987_civil_war_zh/ch15_第三部分_1920_胜利之年_part_2.md#L868) 已给出其 1920 年南俄政府外长职务的原文直引。
- **修复方案**：
  1. 在 `[T3]` 撤除或降级 `encyclopedia.com` 为纯粹检索索引，补充引用上述库内 A 级札记、专著分章及 [`CON-intelligentsia-and-vekhi.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-intelligentsia-and-vekhi.md)、[`PER-wrangel.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-wrangel.md)；
  2. 在 `2.2` 边表增补 `PER-wrangel`（`foreign-minister-ally`, `1920.04–1920.11`）与 `CON-intelligentsia-and-vekhi`，并将 `ORG-kadets` 节点补充说明 `1915-06-08 [O.S.]` 退出中央委员会及内战期转向全国中心/民族党构想；
  3. 依据 `RN-W1B` 补入列宁（CW 1:504; 21:222）与《路标》反击方视角，校准 `perspectives_present` / `perspectives_missing`。

#### 01-02｜P1｜斯图加特《解放》刊期与“解放同盟”组织分期未拆清

- **定位**：[`PER-struve.md:26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-struve.md#L26)、[`L41`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-struve.md#L41)。
- **核证与判断**：卡片 L26 仅写“1902年在德国斯图加特主编《解放》”，且直接跳过至“后加入立宪民主党”；L41 自引的巴登—符腾堡州档案馆报告明确标定题目为 *als Redakteur in Stuttgart (1902–1904)*，并载明该半月刊于 **`1902-07 [N.S.]`** 在斯图加特 Dietz 出版社创刊、因受驱逐于 **1904 年秋（10月）** 迁往巴黎继续出版，且 1903–1904 年间据此形成了作为立宪民主党前身的“解放同盟”（*Союз освобождения*）。卡片既已引用该 PDF，却未标出 `1902–1904` 斯图加特办报起讫与 1903 年解放同盟组织化桥梁。
- **修复方案**：在 L26 写明“1902年7月 [N.S.] 起在德国斯图加特创刊主编半月刊《解放》（至1904年秋遭驱逐后迁往巴黎出版），并成为1903年成立的‘解放同盟’（立宪民主党核心前身）之舆论枢纽”；保留“海外出版只标公历”之正确提示。

#### 01-03｜P2｜Frontmatter 日期与关联依据表粒度不达标

- **定位**：[`PER-struve.md:9-11`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-struve.md#L9-L11)、[`L30-L34`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-struve.md#L30-L34)。
- **核证与判断**：`dates` 使用 `start_year: 1870` / `end_year: 1944`，偏离 [`docs/TEMPLATES.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/docs/TEMPLATES.md) 标准字段 `start_ns` / `end_ns`；边表 L32–34 的“核心依据”栏全部填“下列书目”，未落到具体论断卡或专著章节，形成“空指针式”索引。
- **修复方案**：Frontmatter `dates` 改为 `start_ns: "1870-02-07"`、`end_ns: "1944-02-22"`（加注俄历出生 `1870-01-26 [O.S.]` 与巴黎逝世少数文献记 `02-26` 之校记）；边表第 5 栏逐行写明具体卡片/章节锚点。

---

### 02｜亚历山大·伊万诺维奇·古契科夫（`PER-guchkov`）

**审计对象**：[`PER-guchkov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md)（共 47 行）；关联包：[`graph/packs/PER-guchkov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-guchkov.md)。
**外链实测**：Hasegawa《二月革命》L40 所引“第10章及第23章注66”经对照本地 [`ch33_chapter_23_the_duma_committee_and_the_mo.md:905-908`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/hasegawa_february_1917/ch33_chapter_23_the_duma_committee_and_the_mo.md#L905-L908) **真实准确**（note 66 确引用 Lyandres 2013 并指出尚不清楚捕获沙皇后的具体处置方案）；L44 所引美国国务院 FRUS 1918 Vol. I `d49`（Winship May 22, 1917 Despatch No. 306）经外部检索**真实存在**，内文确载 5 月 14 日辞职及临时政府声明。

#### 02-01｜P0｜`related_debates` 挂接尚未创建的孤立争鸣 ID（断链）

- **定位**：[`PER-guchkov.md:15`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md#L15)；另见 [`graph/packs/PER-guchkov.md:58`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-guchkov.md#L58)。
- **核证与判断**：L15 填 `related_debates: ["DEB-1917-february-liberal-role-and-dual-power"]`，但仓库内不存在该争鸣卡。库内主争鸣卡 [`DEB-1917-dual-power-and-february-origins.md:32`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md#L32) 已明确说明 `DEB-1917-february-liberal-role-and-dual-power` 仅为旧 CLM 遗留的未建别名，新卡应统一指向 `DEB-1917-dual-power-and-february-origins`。
- **修复方案**：将 L15 改为 `related_debates: ["DEB-1917-dual-power-and-february-origins"]`（若需涵盖战前与四月危机，可对照 `PER-milyukov` 审慎决定是否追加已建卡 `DEB-1914-haimson-thesis-stability` 等）。

#### 02-02｜P1｜架空站内 S 级退位诏书原件、L3 显微时间线与关键关联节点

- **定位**：[`PER-guchkov.md:27-28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md#L27-L28)、[`L31-L36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md#L31-L36)、[`L44-L45`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md#L44-L45)。
- **核证与判断**：
  1. **遗漏库内 S 级原典**：[`sources/web-archive/W32_milestone_docs/1917-03-02_nicholas-ii-abdication-manifesto.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/W32_milestone_docs/1917-03-02_nicholas-ii-abdication-manifesto.md#L38-L48) 已完整收录尼古拉二世《退位诏书》俄/英/中全文及普斯科夫之夜详考（古契科夫与舒尔金于 3 月 2 日晚 22 时抵普斯科夫、如何当场接受违反 1906 年《根本法》皇储继承条款的传位米哈伊尔改版、3 月 3 日晨在彼得格勒火车站宣读诏书险被工兵扣押、随后在百万街 12 号普特亚京寓所与米留可夫力劝米哈伊尔即位）。卡片 L27 对此全未索引。
  2. **未对齐库内 L3 四月辞职考证与未挂接核心节点**：[`timeline/L3_daily/1917-04_lenin_arrival_april_theses_and_milyukov_note.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-04_lenin_arrival_april_theses_and_milyukov_note.md)（`TL-W32-1917-05-12-02`）已将古契科夫辞职按 Galili 拆清为 `1917-04-29 [O.S.] / 05-12 [N.S.]` 公开宣布辞职、`1917-04-30 [O.S.] / 05-13 [N.S.]` 正式去职，并对勘 Trotsky 所记 `05-02 [O.S.]` 说。卡片仅引用美国领事事后综合报告（FRUS `d49`，5 月 22 日发、述及 5 月 14 日公报见报与 5 月 13 日外交电报），却漏引近在咫尺的库内 L3 考据，同时边表遗漏 `ORG-octobrists-and-progressive-bloc`、`ORG-provisional-government`、`PER-kerensky`（继任陆海军部长）及 `PER-nicholas-ii`。
- **修复方案**：在 `[T3]` 及正文挂接 `1917-03-02_nicholas-ii-abdication-manifesto.md` 与 `timeline/L3_daily/1917-04_...md`，将 FRUS 的“外交电报与公报见报日（5月13/14日 [N.S.]）”与 Galili 考证的“宣布/正式生效日（4月29/30日 [O.S.] = 5月12/13日 [N.S.]）”对照写明；边表增补 `ORG-octobrists-and-progressive-bloc`、`ORG-provisional-government` 与 `PER-nicholas-ii`。

#### 02-03｜P1｜杜马议长、战时军工委主席及政变计划细节过度笼统

- **定位**：[`PER-guchkov.md:25-26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md#L25-L26)、[`L40`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md#L40)。
- **核证与判断**：
  1. L25“1910–1911年主持第三届国家杜马”未给出准确起讫日期（实为 **`1910-03-10 [O.S.] / 1910-03-23 [N.S.]` 至 `1911-03-15 [O.S.] / 1911-03-28 [N.S.]`**，辞职后由罗将柯继任）；“一战期间任中央军事工业委员会主席”亦缺就职时间（`1915-07` 第一次全俄军事工业委员会代表大会当选，见 [`gaida ch04`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/gaida_2003_liberal_opposition_zh/ch04_pages_101-125.md#L115-L128)，Guchkov 是作为“无政党隶属的折衷强硬派”胜出，而此前 L25 仍并提十月党领袖未交待其此时已脱离议会党团束缚）。
  2. L26 评述“长谷川毅记述较具体计划”时，本库已有 [`hasegawa_february_1917/ch17`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/hasegawa_february_1917/ch17_chapter_10_the_tsarist_regime_on_the_eve.md) 与 [`ch33`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/hasegawa_february_1917/ch33_chapter_23_the_duma_committee_and_the_mo.md#L877-L981)（明载“五人委员会”成员古契科夫、涅克拉索夫、捷列先科、维亚泽姆斯基公爵、科西科夫斯基骑兵上尉；计划在克列切维齐截车并推举马尼科夫斯基将军实施军事独裁；2 月 26–27 日夜调近卫预备骑兵团两中队入京，28 日晨撤离却停留在楚多沃待命），卡片只浮泛带过，未能落实为可核查的史实锚点。
- **修复方案**：补齐第三届杜马议长（`1910-03-10`–`1911-03-15 [O.S.]`）与中央军事工业委员会主席（`1915-07`–`1917`）精确起讫，并用本地 `hasegawa ch17/ch33` 与 `gaida ch04` 补实五人委员会、楚多沃骑兵中队调动及马尼科夫斯基选项。

#### 02-04｜P2｜`dates` 字段格式与卒年精准度及边表微疵

- **定位**：[`PER-guchkov.md:9-11`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md#L9-L11)、[`L28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md#L28)、[`L34`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md#L34)。
- **核证与判断**：`dates` 应按模板改为 `start_ns: "1862-10-26"`、`end_ns: "1936-02-14"`；L28 “1936年卒于巴黎”补确切公历日 `1936-02-14 [N.S.]`；L34 与 `PER-milyukov` 关系时段标 `1917.03–05`“相继离职”，宜写清古契科夫先辞（4月底）、米留可夫后辞（`05-02 [O.S.] / 05-15 [N.S.]`）。

---

### 03｜米哈伊尔·弗拉基米罗维奇·罗将柯（`PER-rodzianko`）

**审计对象**：[`PER-rodzianko.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md)（共 47 行）；关联包：[`graph/packs/PER-rodzianko.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-rodzianko.md)。
**核验说明**：卡片无外文伪直引（L46 声明未作逐字外文直引）；所引 `CLM-hasegawa-2018-duma-committee-revision` 与 `CLM-gaida-2003-liberals-in-february-1917` 主旨吻合。

#### 03-01｜P0｜`related_debates` 挂接不存在的争鸣卡 ID（断链）

- **定位**：[`PER-rodzianko.md:15`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md#L15)；另见 [`graph/packs/PER-rodzianko.md:62`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-rodzianko.md#L62)。
- **核证与判断**：与 `PER-guchkov` 同病，引用未建卡 `DEB-1917-february-liberal-role-and-dual-power`。
- **修复方案**：改为库内标准主争鸣卡 `DEB-1917-dual-power-and-february-origins`。

#### 03-02｜P1｜重大二月履历断档：遗漏大公宪制宣言、拦截御列车与“卢加兵变”托辞、百万街会议及核心机构关联

- **定位**：[`PER-rodzianko.md:27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md#L27)、[`L31-L35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md#L31-L35)。
- **核证与判断**：
  1. 在 `1917-02-27` 成立杜马临时委员会（L26）与 `1917-03-03` 内阁路线受挫（L27）之间，L27 仅用一句话笼统交代“他支持通过尼古拉二世退位……”，完全遮蔽了长谷川毅（[`ch33_chapter_23_the_duma_committee_and_the_mo.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/hasegawa_february_1917/ch33_chapter_23_the_duma_committee_and_the_mo.md#L104-L240) 与 [`L458-L1118`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/hasegawa_february_1917/ch33_chapter_23_the_duma_committee_and_the_mo.md#L458-L1118)）重点考证的罗将柯二月行动全链条：
     - **02-27 至 03-01 [O.S.] 秘密推进《大公宪制宣言》**：联手律师 И. Н. 伊万诺夫与巴维尔、基里尔、米哈伊尔三位大公签就以自己出任负责内阁首脑的《宪制宣言》草案，直至 3 月 1 日草案送回杜马委员会遭米留可夫当场“没收”作废；
     - **指示截停御列车与德诺爽约及休斯电报托辞**：3 月 1 日指示布勃利科夫与罗蒙诺索夫在博洛戈耶/德诺（Dno）截停御列车并致电沙皇“恳请候驾”，后因苏维埃执委会阻挠及杜马委员会内部倒向退位而爽约；3 月 2 日凌晨 03:30 在与鲁兹斯基的休斯电报对话中以并不存在的“卢加兵变”与“民众只听从我”掩饰自身失势并推动高层迫使沙皇退位；
     - **03-03 [O.S.] 百万街 12 号会议立场反转**：同日上午在普特亚京公爵寓所会议上，罗将柯转而与克伦斯基一同警告米哈伊尔若强行即位将引发武装暴动、危及性命，实质站到了反对米留可夫/古契科夫保皇方案的一边（已见库内 S 级原件 [`1917-03-02_nicholas-ii-abdication-manifesto.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/W32_milestone_docs/1917-03-02_nicholas-ii-abdication-manifesto.md#L47)）。若忽略这一点，读者会误以为罗将柯到 3 月 3 日还在主张保皇即位。
  2. `2.2` 边表仅列 3 条边（`PER-guchkov`, `PER-milyukov`, `EVT-1917-02-february-revolution`），遗漏其制度母体 `INS-state-duma-1906-1917`（其长达六年余的杜马议长根基）、`ORG-provisional-government`、`PER-lvov`（二月前后负责/信任内阁头号竞争对手）及 `PER-nicholas-ii`。
- **修复方案**：在 2.1 补齐 2 月 28 日—3 月 3 日 [O.S.] 大公宣言、德诺爽约、3 月 2 日凌晨休斯电报转向与 3 月 3 日上午百万街 12 号劝阻米哈伊尔即位的完整因果；在边表补全 `INS-state-duma-1906-1917`、`PER-lvov`、`PER-nicholas-ii`、`ORG-provisional-government`，并引用库内 S 级退位文档与 `timeline/L3_daily/1917-02_february_eight_days.md`。

#### 03-03｜P1｜本地已藏文献误标“待核查”、议长起讫年份未锚定、回忆录缺具体书目

- **定位**：[`PER-rodzianko.md:20`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md#L20)、[`L25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md#L25)、[`L39`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md#L39)、[`L46`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md#L46)。
- **核证与判断**：
  1. L46 把“两封电报完整原件与发送时刻、罗将柯回忆录相关章节及其南斯拉夫具体逝世地点和日期”全列为“待核查”；但库内 [`hasegawa ch33`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/hasegawa_february_1917/ch33_chapter_23_the_duma_committee_and_the_mo.md#L88-L91) 与 [`L949`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/hasegawa_february_1917/ch33_chapter_23_the_duma_committee_and_the_mo.md#L949) fn. 68 及 `ch23`/`ch24` 已详细讨论两封电报（2 月 26 日夜发与 2 月 27 日正午古契科夫协撰），[`timeline/L3_daily/1917-02_february_eight_days.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-02_february_eight_days.md) 亦有逐日记录。
  2. L25 仅写“1911年起任第三届杜马议长”，未标精确接任日 **`1911-03-22 [O.S.] / 1911-04-04 [N.S.]`**；L20 与 L27 混用“1911–1917年国家杜马议长”与“杜马被政治边缘化，并非当日即在法律上解散”，却未交代第四届杜马究竟何时正式法律解散（`1917-10-06 [O.S.] / 1917-10-19 [N.S.]` 临时政府决议解散杜马以筹备立宪会议选举）。
  3. L39 讨论回忆录却连其代表作名称（*Крушение империи* / 英译 *The Reign of Rasputin: An Empire's Collapse*, 1927）都未给出。
- **修复方案**：补齐 `1911-03-22 [O.S.]` 上任与 `1917-10-06 [O.S.]` 杜马正式解散锚点；在 `[T2]`/`[T3]` 指明回忆录书名与本地 `hasegawa ch33`、`1917-02_february_eight_days.md` 锚点；补录南斯拉夫逝世准确时间地点 `1924-01-24 [N.S.]`（塞尔维亚—克罗地亚—斯洛文尼亚王国别奥德拉 Beodra）。

#### 03-04｜P2｜Frontmatter 日期格式与部分段落标示规范化

- **定位**：[`PER-rodzianko.md:9-11`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md#L9-L11)、[`L28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md#L28)。
- **核证与判断**：`dates` 应改为 `start_ns: "1859-02-21"`、`end_ns: "1924-01-24"`；L28 “1924年去世”补准确公历日期。

---

### 04｜鲍里斯·维克托罗维奇·萨温科夫（`PER-savinkov`）

**审计对象**：[`PER-savinkov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-savinkov.md)（共 49 行）；关联包：[`graph/packs/PER-savinkov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-savinkov.md)。
**外链实测**：
- L42 `nybooks.com`（Gary Saul Morson, *"Falling in Love with Terror"*, 2022-01-13）**可访问且真实存在**；
- L45 `historyrussia.org`（О. Б. Мозохин，《ВЧК-ГПУ外情处筹备“辛迪加-2”行动的作用》）**可访问且真实存在**；
- L46 `cambridge.org`（Brian D. Taylor, *Politics and the Russian Army*, 2003, Ch. 3 PDF）**可下载且真实存在**；
- **L46 `openstax.marxists.info` 失效错误（见下 P0-01）**。

#### 04-01｜P0｜编造/错域外链（`openstax.marxists.info` TLS 证书域名不匹配导致无法访问）

- **定位**：[`PER-savinkov.md:46`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-savinkov.md#L46)。
- **核证与判断**：L46 `[克伦斯基事后叙述](https://www.openstax.marxists.info/reference/archive/kerensky/1919/prelude/intro.htm)` 实测请求报错 `x509: certificate is valid for www.marxists.info, not www.openstax.marxists.info`——`openstax.` 属于凭空拼接的无效子域名，暴露了未实测 URL 即入卡的问题。克伦斯基《布尔什维克主义的前奏》（*The Prelude to Bolshevism: The Kornilov Rebellion*, New York, 1919）在线档案实际托管于 `marxists.org` 或 `archive.org`，且本库 [`sources/monographs/pipes_1990_russian_rev/ch20_section.md:1039`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/pipes_1990_russian_rev/ch20_section.md#L1039) 与 [`timeline/L3_daily/1917-07_july_days_and_kornilov_affair.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-07_july_days_and_kornilov_affair.md) 已包含该书及相关核勘。
- **修复方案**：删除失效的 `openstax.marxists.info` 链接，核实并替换为有效的 `marxists.org` / `archive.org` 真实 URL 或改指库内已有馆藏文献。

#### 04-02｜P1｜自引材料与本地馆藏双重脱节：漏掉 1919–1921 关键履历、NSZRiS 组织区分及 1924 公审认罪改判核心链条

- **定位**：[`PER-savinkov.md:27-28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-savinkov.md#L27-L28)、[`L37`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-savinkov.md#L37)、[`L45`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-savinkov.md#L45)。
- **核证与判断**：
  1. **1919–1921 关键组织与流亡转折整段跳空**：L27 写完“1918年7月雅罗斯拉夫尔起事”后直接跳到“1920年俄波战争在波兰组织反苏武装”，完全漏掉了卡片自己所引俄国历史学会（莫佐欣）网文及本库 [`leggett_1981_cheka/ch11_pages_331-360.md:107-169`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/leggett_1981_cheka/ch11_pages_331-360.md#L107-L169)（`pp. 295–296`）明确记载的四项重大史实：
     - (a) 1919 年在巴黎任高尔察克白军代表（负责筹款与军事使团）；
     - (b) 1920 年在华沙任流亡“俄罗斯政治委员会”（РПК / RPC）主席并协助在波兰指挥下组建“俄罗斯人民军”（Русская народная армия）；
     - (c) **1921 年 1 月在华沙（6 月开代表大会）重组“保卫祖国与自由人民同盟”（НСЗРиС / NSZRiS）**，这与 1918 年国内失败的“保卫祖国与自由同盟”（СЗРиС / SZRiS）属前后两代组织；
     - (d) 1921 年 10–11 月因苏俄外交抗议及《里加和约》条款遭波兰驱逐出境，此后辗转布拉格与巴黎继续策划跨境地下行动。
  2. **1924 年 8 月莫斯科公审的“戏剧性认罪与改判十年”被整段隐去**：L28 仅含糊一句“1924年8月…被捕，随后在莫斯科受审……1925-05-07 死于拘押中”。然而 L45 自引的俄国历史学会文本（及 L42 自引的 Morson 书评、本地 Leggett `p. 296`）均详载：萨温科夫于 **`1924-08-27`–`08-29`**（莫佐欣记 `08-25`–`08-29`）在苏联最高法院军事法庭受审时**当庭全面承认反苏罪责并公开呼吁流亡者“无条件向工农苏维埃政权俯首致敬”**，**8 月 29 日被判死刑后同日减刑为 10 年监禁**，并在狱中致信海外同僚劝降，在卢比扬卡享受优待期间于 1925 年 5 月 7 日突然坠亡——缺乏这一戏剧性公开转向，后续“流亡圈震惊与是否他杀/自杀”的争鸣就失去了最核心的史实前提。
  3. **未用库内 A 级安全史与政治史馆藏**：L37 对“1918–1920 反苏活动”竟写“待补专门研究”，却完全未调用站内 [`leggett_1981_cheka/ch10`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/leggett_1981_cheka/ch10_pages_301-330.md#L780-L812)（`p. 280` 详载 SZRiS 约 5,000 人规模及 `1918-07-06` 雅罗斯拉夫尔、`07-07` 雷宾斯克、`07-08` 穆罗姆起事）、`ch11`（`pp. 294–297`）、[`RN-W4-cheka-origins-and-red-terror.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/leggett_1981_cheka/RN-W4-cheka-origins-and-red-terror.md)、[`pipes_1990_russian_rev/ch20`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/pipes_1990_russian_rev/ch20_section.md#L219-L336) 与 [`timeline/L3_daily/1917-07_july_days_and_kornilov_affair.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-07_july_days_and_kornilov_affair.md#L83-L105)。
- **修复方案**：
  1. 依 `Leggett ch10–11` 及莫佐欣网文补齐 1918（SZRiS，雅罗斯拉夫尔 7 月 6 日）→ 1919（巴黎代表高尔察克）→ 1920（华沙 RPC 与俄罗斯人民军）→ 1921（NSZRiS 及 10–11 月被波兰驱逐）的组织演进链；
  2. 在 L28 明确写出 1924 年 8 月下旬苏联最高法院军事法庭公审认罪、死刑改判 10 年及狱中优待/劝降信，再引出 1925-05-07 [N.S.] 死亡争议（并说明对 Morson 评述 Alexandrov 传记 vs. Solzhenitsyn/Ignatiev 口述证言的史料分层）；
  3. 对 L28 末“与‘托拉斯’混称”之语加以精确化：依据 `Leggett ch11` (`pp. 294–298`) 指出，“辛迪加-2”（针对萨温科夫 NSZRiS，1922–1924）与“托拉斯”（针对流亡君主派 MOR，1921–1927）均由 OGPU 反间谍处（KRO，阿尔图佐夫主管）策划，且挑衅特工 Селянинов-Опперпут 先后深度介入两案，故属同一反间谍诱捕谱系下的两个平行行动而非同一行动。

#### 04-03｜P1｜1917 年职务头衔与社革党决裂节点模糊

- **定位**：[`PER-savinkov.md:26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-savinkov.md#L26)、[`L33-L35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-savinkov.md#L33-L35)。
- **核证与判断**：L26 仅写“夏季成为克伦斯基陆军部副部长……短暂出任彼得格勒军事总督”，未明确：(1) 其实际于 1917 年 7 月出任陆军部副部长并在 8 月危机的多份档案中以“陆军部代理部长（`Управляющий Военным министерством` / Acting Minister of War）”名义赴莫吉廖夫大本营谈判（如库内 `pipes ch20` 与 `L3` 时间线 L83）；(2) **`1917-08-27 [O.S.] / 1917-09-09 [N.S.]`** 兼任彼得格勒军事总督，数日内因同克伦斯基意见分歧辞职（由 П. И. 帕利钦斯基接任）；(3) 如站内 [`RN-W9-halle-1920-debate-and-tsereteli.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/galili_1989_menshevik_leaders/RN-W9-halle-1920-debate-and-tsereteli.md) 及 `Leggett p. 280` 所述，社革党在科尔尼洛夫事件后于 1917 年秋（仍处克伦斯基执政期）即正式开除其党籍，而非仅“加剧同党内关系的紧张”（L33）。
- **修复方案**：明确 1917 年 7 月副部长→8 月代理部长赴莫吉廖夫（`08-23`–`08-24 [O.S.]`）→ `08-27 [O.S.] / 09-09 [N.S.]` 任彼得格勒军事总督旋即辞职并遭社革党开除（1917 年秋）的时间锚点；在 `2.2` 边表增补 `PER-kornilov`、`ORG-provisional-government` 与 `RN-W4`/`Leggett`。

#### 04-04｜P2｜Frontmatter `dates` 字段混用与早年刺杀节点补双历

- **定位**：[`PER-savinkov.md:9-11`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-savinkov.md#L9-L11)、[`L25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-savinkov.md#L25)。
- **核证与判断**：L9–11 混搭 `start_year: 1879` 与 `end_ns: "1925-05-07"`，不合模板规范；L25 所提 1904 年刺杀普列维（`1904-07-15 [O.S.] / 1904-07-28 [N.S.]`）与 1905 年刺杀谢尔盖大公（`1905-02-04 [O.S.] / 1905-02-17 [N.S.]`）未标具体日期（补注时须注意 Leggett `p. 280` 误印 14 Feb 实系 4 Feb O.S. 之误写）。
- **修复方案**：L10 改为 `start_ns: "1879-01-31"`（加注 `1879-01-19 [O.S.]`）；如补充早年刺杀日须按俄历 `+13` 天双标。

---

## 四、历法与生卒日期复核表（后半批 05–07）

> 注：经 `python scripts/kb.py date --from os` 及俄文档案工具书核验，后半批在 `PER-sukhanov` 存在 **1 项致命双历双重换算 P0 硬伤**，在 `PER-yagoda` 存在 **出生月日缺失**；1917 年俄历双标及 1918-02-14 改历后纯公历标法总体合规。

| 人物（卡 ID） | 卡内 `dates` 原样 | 卡内正文日期验算 | 应补/订正标准生卒日期（经 `kb.py date` 与外部档案核验） | 判定 |
| :--- | :--- | :--- | :--- | :--- |
| **苏汉诺夫**（`PER-sukhanov`） | `start_ns: "1882-12-21"` / `end_ns: "1940-06-29"` | **L25 `1882-12-09 [O.S.] / 1882-12-21 [N.S.]` 为双重换算硬伤（见 05-01）**；1917 年诸日（`02-27`/`03-12`、`03-01`/`03-14`、`03-02`/`03-15`、`04-03`/`04-16`、`04-04`/`04-17`、`10-25`/`11-07`）均 `+13` 天，正确 | 生于 **`1882-11-27 [O.S.] / 1882-12-09 [N.S.]`**（莫斯科，+12 天）；卒于 `1940-06-29 [N.S.]`（鄂木斯克被处决，改历后单公历） | **P0：出生日期双历整整后移 12 天** |
| **雅戈达**（`PER-yagoda`） | `start_ns: "1891"`（缺月日） / `end_ns: "1938-03-15"` | 正文 `1927-07-06` 等均属 1918 年后纯公历，合规；L48 自称“出生精确日期未核” | 生于 **`1891-11-07 [O.S.] / 1891-11-19 [N.S.]`**（雷宾斯克，+12 天；少数二手文献作 `11-20` 系误套 20 世纪 `+13` 天之讹）；卒于 `1938-03-15 [N.S.]`（莫斯科） | **正文日期合规；缺精确出生月日锚点** |
| **米高扬**（`PER-mikoyan`） | `start_ns: "1895-11-25"` / `end_ns: "1978-10-21"` | L25 `1895-11-13 [O.S.] / 1895-11-25 [N.S.]`（+12 天，正确）；L28 `1928-02-10` 改历后纯公历，正确 | 生于 `1895-11-13 [O.S.] / 1895-11-25 [N.S.]`（萨纳欣，+12 天）；卒于 `1978-10-21 [N.S.]`（莫斯科） | **历法换算全部正确** |

---

## 五、后半批逐卡审计与修复方案（05–07）

### 05｜尼古拉·尼古拉耶维奇·苏汉诺夫（`PER-sukhanov`）

**审计对象**：[`PER-sukhanov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sukhanov.md)（共 50 行）；关联包：[`graph/packs/PER-sukhanov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-sukhanov.md)。

#### 05-01｜P0｜出生日期“双重换算”硬伤：误将公历 `1882-12-09` 当成俄历再加 12 天变成 `1882-12-21`

- **定位**：[`PER-sukhanov.md:10`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sukhanov.md#L10)、[`L25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sukhanov.md#L25)。
- **核证与判断**：
  1. 卡片 L10 写 `start_ns: "1882-12-21"`，L25 写 `生于 1882-12-09 [O.S.] / 1882-12-21 [N.S.]`。
  2. 核对俄文与英文权威传记及档案数据库（`Открытый список` 政治镇压受害者数据库、`Хронос / 1937god.info`、俄文维基百科引据及其本人户籍、英文维基百科引据 Israel Getzler, *Nikolai Sukhanov: Chronicler of the Russian Revolution*），苏汉诺夫（格伊默尔）生于俄历 **`1882-11-27`**、公历 **`1882-12-09`**（`27 ноября [9 декабря] 1882`，莫斯科）。
  3. 经 `python scripts/kb.py date --from os 1882-11-27` 实测，19 世纪俄历 `+12` 天确为 **`1882-11-27 [O.S.] / 1882-12-09 [N.S.]`**。Codex 显系误把百科条目中的公历 `12-09`（9 декабря）当成俄历并再次执行 `+12` 天换算，造成整卡生年锚点漂移 12 天。
- **修复方案**：将 L10 改为 `start_ns: "1882-12-09"`，并将 L25 改为 `生于 1882-11-27 [O.S.] / 1882-12-09 [N.S.]`。

#### 05-02｜P1｜错标“待补”并绕开库内已入藏的《第一号命令》《论我国革命》原文及 L3 每日时间线

- **定位**：[`PER-sukhanov.md:14`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sukhanov.md#L14)、[`L33-L37`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sukhanov.md#L33-L37)、[`L45-L47`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sukhanov.md#L45-L47)；关联包 [`graph/packs/PER-sukhanov.md:89`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-sukhanov.md#L89)。
- **核证与判断**：
  1. L14 将 `order-one-drafting-primary-record` 列入 `perspectives_missing`，L47 更明言“**待补：《第一号命令》……及《论我国革命》原文互校**”。实际上这两类原典均**已在库内**：
     - 《第一号命令》S 级俄/英/中三语对照全文已入库于 [`sources/web-archive/E03_E08_party_and_state_docs/1917-03-01_petrograd-soviet-order-no-1.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E03_E08_party_and_state_docs/1917-03-01_petrograd-soviet-order-no-1.md)（另见 `E06_E10_turning_points/1917-03-01_order-no-1.md`、[`WB-W1-1917-1929-primary-corpus.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/web-briefs/WB-W1-1917-1929-primary-corpus.md) 及加利利精读 [`RN-W5-menshevik-defensism-and-coalition.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/galili_1989_menshevik_leaders/RN-W5-menshevik-defensism-and-coalition.md#L36-L38)）；
     - 列宁 1923 年 1 月《论我国革命（评尼·苏汉诺夫的札记）》原文核心摘录已入库于 [`sources/primary/socialism_in_one_country_debate_docs_zh/ch11_如何评价_一国建成社会主义_理论_part_3.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/primary/socialism_in_one_country_debate_docs_zh/ch11_如何评价_一国建成社会主义_理论_part_3.md#L219-L239)（以及 [`spitsyn_textbook_zh/ch08_pages_201-225.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/spitsyn_textbook_zh/ch08_pages_201-225.md#L75-L94)、[`RN-W36-yao-hai-cass-russian-revolution-synthesis.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/yao_hai_ussr_history_v1_russian_rev_zh/RN-W36-yao-hai-cass-russian-revolution-synthesis.md#L84)）。
  2. **彻底忽略三条直接关联的 L3 每日时间线**：[`graph/packs/PER-sukhanov.md:89`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-sukhanov.md#L89) 显示关联时间线为 **`0` 条**，而库内 [`1917-02_february_eight_days.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-02_february_eight_days.md#L155-L201)、[`1917-04_lenin_arrival_april_theses_and_milyukov_note.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-04_lenin_arrival_april_theses_and_milyukov_note.md#L119-L135) 与 [`1917-10_october_insurrection.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-10_october_insurrection.md#L278-L301) 已专门单列“苏汉诺夫 (Sukhanov)”对勘栏，包括长谷川对其《第一号命令》“精英代笔叙事”的批评、其 10 月 25 日上午 10 时《告公民书》“过早发布”评论，以及卡迈克尔节本 `ch15#L1037` 将 4 月 4 日错印为 `April 14th` 的版本勘误。
  3. **边表缺建库人物节点**：L33–37 漏掉库内已有的 [`PER-guchkov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md)、[`PER-tsereteli.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-tsereteli.md)、[`PER-gorky.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-gorky.md)、[`PER-kerensky.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-kerensky.md) 与 [`PER-trotsky.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-trotsky.md)；同时 L47 仅旁记 `SCH-sukhanov-nn` 与 [`SCH-sukhanov-nikolai.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/scholars/SCH-sukhanov-nikolai.md) 命名冲突而未协调。
- **修复方案**：
  1. 在 `[T3]` 直接回链《第一号命令》三语对照文本（`1917-03-01_petrograd-soviet-order-no-1.md`）、《论我国革命》原文摘录（`ch11#L219-239`）及三卷 L3 时间线，仅保留真正尚待补充的“1919–1921 年及 1920 年代后期苏维埃经济机关任职原始档案”；
  2. 在 `2.2` 边表增补 `PER-gorky`（《新生活报》同人）、`PER-tsereteli`（执委会护国派对手）与 `PER-trotsky`（二大现场交锋对手）。

#### 05-03｜P1｜1917 年 5 月入党转折与 1931/1940 审判处决脉络过简

- **定位**：[`PER-sukhanov.md:25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sukhanov.md#L25)、[`L49`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sukhanov.md#L49)。
- **核证与判断**：L25 仅笼统说“政治上接近马尔托夫，但不宜将他的全部思想简化为正式党派职务”，反而漏掉了库内 [`RN-W6-sukhanov-eyewitness-1917.md:35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/sukhanov_1922_personal_record/RN-W6-sukhanov-eyewitness-1917.md#L35) 已明确考订的党籍分界：**2 月革命爆发时苏汉诺夫在土耳其斯坦灌溉部门任职且无党籍（齐美尔瓦尔德派国际主义者），直到 1917 年 5 月马尔托夫回国后才正式加入孟什维克国际主义派**（`ch07, p. 82`）。L49 一句“1931年他在孟什维克审判中被判刑，1940年被处决”亦过于简略，未区分 1930 年 7 月被捕、1931 年 3 月“孟什维克联盟局案”公审判刑 10 年并流放托博尔斯克，与 1937 年因“为纳粹德国从事间谍活动”再次被捕最终于 `1940-06-29` 在鄂木斯克被枪决的两阶段经历。
- **修复方案**：在 `2.1` 补清“1917.05 前无党籍国际主义者 → 1917.05 正式加入孟什维克国际主义派”的党籍节点，并将 L49 规范纳入 `2.1` 或 `[T3]`。

#### 05-04｜P2｜`[T3]` 结尾存在模板外无标题悬空尾句（后半批三卡共病）

- **定位**：[`PER-sukhanov.md:49`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sukhanov.md#L49)。
- **核证与判断**：`1931年他在孟什维克审判中被判刑，1940年被处决。` 脱离前面项目符号列表，单独悬于 `[T3]` 最末一行，与 [`docs/TEMPLATES.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/docs/TEMPLATES.md) 规范不符（`PER-yagoda.md:50` 与 `PER-mikoyan.md:49` 存在完全一致的结构异常，似系末轮机械追加的一句话收尾）。
- **修复方案**：并入 `2.1` 分期脉络或 `[T3]` 规范列表。

---

### 06｜亨里希·格里戈里耶维奇·雅戈达（`PER-yagoda`）

**审计对象**：[`PER-yagoda.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md)（共 51 行）；关联包：[`graph/packs/PER-yagoda.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-yagoda.md)。

#### 06-01｜P1｜架空站内已核实的 Kotkin、Lewin、Leggett、Mozokhin 原档线索，误将核心史实标为“细节待核 / 尚待原始命令核定”

- **定位**：[`PER-yagoda.md:14`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md#L14)、[`L26-L28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md#L26-L28)、[`L36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md#L36)、[`L47-L48`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md#L47-L48)。
- **核证与判断**：卡片多处声称关键细节“待核”，但经逐一检索，相关一手文献引证与页码**已在库内完整存在**：
  1. **1928–1929 年与布哈林的私交及向斯大林表态（L26、L36、L47）**：L36 写 `Kotkin、Khlevniuk，细节待核`，L47 写 `关于私人往来与个人态度须进一步定位原文`。但站内 [`kotkin_2014_stalin_v1/ch21_chapter_14.md#L751-L773`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/kotkin_2014_stalin_v1/ch21_chapter_14.md#L751-L773)、[`lewin_1968_peasants/ch14_12_the_last_opposition.md#L2193-L2196`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/lewin_1968_peasants/ch14_12_the_last_opposition.md#L2193-L2196)、[`leggett_1981_cheka/ch16_pages_481-510.md#L821-L824`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/leggett_1981_cheka/ch16_pages_481-510.md#L821-L824) 及 [`1928-1929_bukharin_stalin_final_showdown.md:128,142`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md#L128) 已明确记载：1928 年 7 月 11 日布哈林密会加米涅夫时声称 OGPU 的雅戈达与特里利塞尔“和我们在一起”，笔记泄露后（1929 年初），特里利塞尔被调离 OGPU，而**雅戈达被迫向斯大林提交书面解释**并迅速倒向斯大林多数派。
  2. **1929 年 10 月精简中央“三人小组”、清理 6,000 人积案与第 122、157 号电报（L28、L48）**：L28 写“将1929年10月某次积案清理或流放方案归为雅戈达个人主持，尚待原始命令核定”。然而本卡 L46 自己引用的 [`CLM-mozokhin-cheka-to-ogpu-extrajudicial-jurisdiction-1918-1929.md:29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-mozokhin-cheka-to-ogpu-extrajudicial-jurisdiction-1918-1929.md#L29) 及原书 [`mozokhin_extrajudicial_powers_zh/ch06#L137-L182`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/mozokhin_extrajudicial_powers_zh/ch06_国家政治保卫总局_联合国家政治保卫总局的_三人小组.md#L137-L182)（`[PDF pp. 47–48]`）明确记述：雅戈达批准并推动将 8 个中央“三人小组”合并为 3 个、限令 20 日内突击审结 **6,000 人**积案，且 **`1929-10-15` 第 122 号电报**与 **`1929-10-31` 第 157 号电报**规定地方全权代表处量定刑罚后**电报雅戈达本人批准执行**——这并非“待核传闻”，而是库内已有 `ЦА ФСБ РФ` 档案编号的制度实证（只是确实应与 1930 年初大规模流放加以分期区分）。
  3. **沙赫特案“绕开政府”与 1924/1928 档案节点遗漏**：[`kotkin ch21#L420-L439`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/kotkin_2014_stalin_v1/ch21_chapter_14.md#L420-L439) 与 [`1928-01_siberian_grain_expedition_and_shakhty_affair.md:84`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-01_siberian_grain_expedition_and_shakhty_affair.md#L84) 详载 **`1928-03-02`** 雅戈达向斯大林呈送沙赫特长篇报告附信并陪同叶夫多基莫夫面见斯大林、在缅任斯基赴马采斯塔疗养期间直接主导莫斯科侦办；此外，[`1928-1929_bukharin_stalin_final_showdown.md:32`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md#L32) 载 `1928-01-04` 雅戈达电令逮捕最大私营粮商送交“特别会议”，且本卡 1-hop 上下文包 [`graph/packs/PER-yagoda.md:96`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-yagoda.md#L96) 已有 `1924-01-23` 贝利亚经雅戈达密报托洛茨基动向的 L3 锚点。
- **修复方案**：删去对布哈林密谈笔记、1929 年 10 月“三人小组”合并/第 122、157 号电报的“待核”误标，直接回链上述 `Kotkin ch21`、`Lewin ch12`、`Mozokhin ch06`、`Leggett ch16` 与两条 L3 时间线。

#### 06-02｜P1｜生年缺月日、1923 年 OGPU 任职双节点合并失准、早年庇护链与 1934–1938 起止过粗

- **定位**：[`PER-yagoda.md:10`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md#L10)、[`L25-L26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md#L25-L26)、[`L48`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md#L48)、[`L50`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md#L50)。
- **核证与判断**：
  1. **生期缺失**：L10 仅写 `"1891"`、L48 称“出生精确日期未核”，实可核定为 **`1891-11-07 [O.S.] / 1891-11-19 [N.S.]`**（生于雷宾斯克）。
  2. **1918–1920 契卡履历与斯维尔德洛夫关系**：库内 [`leggett_1981_cheka/ch16_pages_481-510.md#L795-L815`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/leggett_1981_cheka/ch16_pages_481-510.md#L795-L815)（Appendix B）已给出清晰档案履历：早年依托斯维尔德洛夫（`PER-sverdlov`）关系网成长并娶其外甥女伊达·阿韦尔巴赫；1918 年任莫斯科警备司令，1919–1922 年兼任外贸人民委员部委员，最迟至 1920 年 1 月任全俄契卡特别处（OO）行政主任（Administrative Director），**`1920-07-29`** 获确认为全俄契卡委员会委员。
  3. **1923 年 OGPU 第二副主席日期不完整**：L26 仅写“1923年11月起任OGPU第二副主席”。据 `Leggett`（[`ch10#L575-577`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/leggett_1981_cheka/ch10_pages_301-330.md#L575-L577)、[`ch12#L1332-1336`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/leggett_1981_cheka/ch12_pages_361-390.md#L1332-L1336)）及俄联邦安全局机构沿革档：**`1923-09-18`** 苏联人民委员会即已任命捷尔任斯基为首脑、缅任斯基与雅戈达分别为第一/第二副主席；**`1923-11-02`** 苏联中执委主席团正式通过成立联盟级 OGPU 决议、**`1923-11-15`** 批准条例予以法制确认（见 [`INS-cheka-gpu-ogpu.md:26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-cheka-gpu-ogpu.md#L26)）；此外 **`1924-06-12`** 第 250 号令任命其为 OGPU 特别会议（ОСО）成员（`Mozokhin ch05#L421-422`）。
  4. **1929 第一副主席与 1934–1938 任职起止**：`1929-10-27` 升任 OGPU 第一副主席（1931–1932 年间因阿库洛夫调入曾短暂退居二副）；L50 一句带过 `1934–1938`，漏掉 `1934-05-10` 缅任斯基病逝后任 OGPU 主席 → `1934-07-10` 任新设苏联内务人民委员（NKVD） → `1936-09-26` 被叶若夫取代并贬任邮电人民委员 → `1937-03-28/29` 签发逮捕搜查令（`04-03` 中执委免职）→ 1938 年 3 月“二十一人案”公审 → `1938-03-15` 被处决的完整起止节点。
- **修复方案**：补入 `start_ns: "1891-11-19"`，厘清 `1920-07-29` 契卡委员、`1923-09-18 / 11-02` OGPU 二副、`1924-06-12` 特别会议、`1929-10-27` 第一副主席及 `1934-07-10–1936-09-26` NKVD 人民委员起止。

#### 06-03｜P2｜边表缺关联实卡、页码粗指及 `[T3]` 末悬空尾句

- **定位**：[`PER-yagoda.md:33-38`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md#L33-L38)、[`L50`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md#L50)。
- **核证与判断**：`2.2` 边表漏掉了已有卡片 [`PER-sverdlov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sverdlov.md)（早期庇护人）与 `ORG-united-opposition`（L27 正文已述其打击联合反对派）；L37 将 `Velikanova pp. 69–73, 80–84` 笼统并引（实际第 131 号指令在 `pp. 69–70`，逮捕估算在 `pp. 70–73`，`pp. 80–84` 系第 2 章结论与第 3 章表 3.1，宜改引 `RN-W8`）；L50 存在模板外悬空尾句。
- **修复方案**：增补 `PER-sverdlov` 与 `ORG-united-opposition` 边；精确核心依据至 `RN-W8` 及 `Mozokhin ch06`；将 L50 归位至 `2.1` 或 `[T3]`。

---

### 07｜阿纳斯塔斯·伊万诺维奇·米高扬（`PER-mikoyan`）

**审计对象**：[`PER-mikoyan.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-mikoyan.md)（共 50 行）；关联包：[`graph/packs/PER-mikoyan.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/packs/PER-mikoyan.md)。

#### 07-01｜P1｜1920–1922 下诺夫哥罗德关键履历整段漏失，1922–1926 党政职衔起止模糊

- **定位**：[`PER-mikoyan.md:25-27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-mikoyan.md#L25-L27)、[`L47`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-mikoyan.md#L47)。
- **核证与判断**：
  1. **缺漏 1920–1922 下诺夫哥罗德党务跃升阶段**：L25 写到“1918年巴库公社失败后他幸存”后，L26 直接跳跃至“东南与北高加索党务（1922–1926）”。事实上，米高扬进入中央政治层的关键跳板正在被漏掉的 1920–1922 年：1920 年任高加索第十一集团军革委会全权代表及阿塞拜疆工会理事会主席后，于 **`1920-10`** 奉调**下诺夫哥罗德**（Нижний Новгород），历任省委会宣教部长（`1920-11-05–1921-02`）与**下诺夫哥罗德省委员会书记（`1921-02-23–1922-04-29`）**，因在当地成功压制工人反对派与托洛茨基派、依托索尔莫沃工人稳住党组织，于 **1922 年 4 月（十一大）当选中央候补委员**（1923 年 4 月十二大转为正式委员），并获斯大林举荐南调。
  2. **1922–1926 职衔起止精准度不足**：应明确 **`1922-05–1924`** 任俄共（布）中央东南局书记（顿河畔罗斯托夫），**`1924–1926`** 任北高加索边疆区委第一书记兼北高加索军区革委会委员（后由奥尔忠尼启则接任）；L27 所写“1926年7月…同年8月”可依据俄苏档案及库内 [`kotkin_2014_stalin_v1/ch20#L168`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/kotkin_2014_stalin_v1/ch20_chapter_13.md#L168)、[`carr_davies_1969_foundations_v1p1/ch00#L998`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/carr_davies_1969_foundations_v1p1/ch00_pages_1-30.md#L998)（引 *Sobranie Zakonov*, 1926, ii, art. 151）精确锚定为 **`1926-07-23`** 当选联共（布）中央政治局候补委员（与奥尔忠尼启则、基洛夫、卡冈诺维奇、安德烈耶夫同批增补；直至 1935-02-01 转为正式委员）及 **`1926-08-14`** 接替加米涅夫出任苏联内外贸易人民委员（至 1930-11-22 部门拆分为止）。
- **修复方案**：在 `2.1` 补足 `1920.10–1922.04` 下诺夫哥罗德省委时期及进入中央委员会节点，并精确标注 `1922-05`、`1926-07-23`、`1926-08-14` 等官职起止。

#### 07-02｜P1｜架空库内 Carr–Davies、Lewin、Daniels、Velikanova 直接证据，且以未提及米高扬的《卡塔索诺夫札记》替代正统专著

- **定位**：[`PER-mikoyan.md:28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-mikoyan.md#L28)、[`L40-L42`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-mikoyan.md#L40-L42)、[`L45-L47`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-mikoyan.md#L45-L47)。
- **核证与判断**：
  1. **学术史/札记错配（`RN-W32` 并不讨论米高扬）**：L42 史学争鸣专列“**卡塔索诺夫**提供国家外贸垄断与外汇体制的解释性线索”，L46 在 `[T3]` 正式挂接 [`RN-W32-katasonov-trade-monopoly-chervonets-and-two-circuit-ruble.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/katasonov_stalin_economy_zh/RN-W32-katasonov-trade-monopoly-chervonets-and-two-circuit-ruble.md)。但核查 `RN-W32` 全文（L1–90），**全篇未出现“米高扬”一词**（该札记聚焦 1922 年列宁/布哈林/索科利尼科夫外贸垄断争论及货币双循环）；相反，库内直接以大量一手材料刻画米高扬 1926–1929 年决策的五组文献却几乎被架空：
     - **1926 年 9 月逆转加米涅夫压价路线**：[`carr_davies_1969_foundations_v1p1/ch00#L951-L974`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/carr_davies_1969_foundations_v1p1/ch00_pages_1-30.md#L951-L974)（`pp. 7–8`）载其上任伊始即废止加米涅夫“不惜一切代价压低粮价”方针；
     - **1927 年 12 月十五大与战争恐慌警报处置**：[`RN-W8-1927-war-scare-and-grassroots-svodki.md#L113-L122`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/velikanova_2013_popular_perception/RN-W8-1927-war-scare-and-grassroots-svodki.md#L113-L122)（`Velikanova pp. 87–88`）专录米高扬在十五大承认战争传言系“超经济因素”、耗尽国库储备并触发囤积，且 `1927-12-24` 政治局指派莫洛托夫与米高扬控制报刊警报；
     - **1928 年 1–2 月一线督粮与“法律界限”双面表态**：[`carr_davies ch02#L228-231, L284-287`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/carr_davies_1969_foundations_v1p1/ch02_pages_61-90.md#L228-L231) 载 **`1928-01-12`** 他亲赴北高加索边疆区委督催收购加快步伐、又于 **`1928-02-10`**（`L457`）在《真理报》坦承余粮主要在中农手中、复于 **`1928-02-12`**（`L284`）撰文呼吁“在苏维埃法制基础上”反富农并谴责单纯行政强迫（参见 [`RN-W3-grain-crisis-and-collectivization-turn.md:49,53`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/lewin_1968_peasants/RN-W3-grain-crisis-and-collectivization-turn.md#L49) 与 [`1928-1929_bukharin_stalin_final_showdown.md:78,82`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md#L78)）；
     - **1928 年 7 月全会妥协摇摆与 9 月受斯大林致信施压**：[`daniels_1960_conscience/ch13_pages_326-350.md#L982-L992`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/daniels_1960_conscience/ch13_pages_326-350.md#L982-L992)（`p. 329`）与 [`RN-W6-moscow-fall-and-party-struggle-rules.md:78`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/merridale_apalkov/RN-W6-moscow-fall-and-party-struggle-rules.md#L78) 证实米高扬与奥尔忠尼启则在 1928 年 7 月全会曾充当妥协派，由米高扬提出被布哈林称为“从我声明里偷去”的折中决议案；直到 **`1928-09-26`** 斯大林致信米高扬痛斥退让派系“空洞的布尔什维克自由派”（`timeline L156`）后方彻底倒向强硬路线——**卡片把他在 1927–1929 年直接写成静态“斯大林多数派”，抹去了 1928 年春夏这段关键摇摆**。
  2. **忽视库内已有出口分年数**：L28/L47 将 `1927–1929` 收购与出口数全列“待补”，而库内 [`carr_davies ch00#L989-994`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/carr_davies_1969_foundations_v1p1/ch00_pages_1-30.md#L989-L994) 已明列 1926–27 年度出口粮食 1.85 亿普特（300 万吨），[`RN-W32#L35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/katasonov_stalin_economy_zh/RN-W32-katasonov-trade-monopoly-chervonets-and-two-circuit-ruble.md#L35) 亦转引《苏维埃贸易》1928 年第 50 期所载 1928 年粮食仅占出口 7%（低于毛皮 17%、石油 16%、木材 13%）之比例。
- **修复方案**：
  1. 在 `2.3` 史学争鸣光谱中以 **Daniels / Lewin / Velikanova / Kotkin** 替换或限定对卡塔索诺夫的过度挂接，实写米高扬在 1928 年 2 月—7 月全会“从法制/折中妥协到 9 月以后紧跟斯大林”的动态移位；
  2. 回链 `Carr–Davies ch00/ch02`、`RN-W8`、`RN-W3 (Lewin)`、`1928-1929` L3 时间线及 `khlevniuk ch02_preface.md#L42-44` 对米高扬回忆录（其子塞尔戈未经标明擅自增改手稿）的史料层级警示。

#### 07-03｜P2｜边表漏连关键人物、米高扬回忆录史料警示缺失与 `[T3]` 末悬空尾句

- **定位**：[`PER-mikoyan.md:33-37`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-mikoyan.md#L33-L37)、[`L49`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-mikoyan.md#L49)。
- **核证与判断**：`2.2` 边表漏连北高加索/政治局盟友 [`PER-ordzhonikidze.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-ordzhonikidze.md) 与内外贸前任 [`PER-kamenev.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-kamenev.md)；`graph/packs/PER-mikoyan.md:76` 亦因未联动 L3 时间线显示为 `0` 条；L49 末句悬空置于 `[T3]` 外部。
- **修复方案**：补边 `PER-ordzhonikidze` 与 `PER-kamenev`；在 `[T3]` 加注 Khlevniuk 对米高扬回忆录经其子改写之史料警戒；合并 L49 尾句。

---

## 六、跨卡系统性问题总表与优先修复矩阵（7 张全盘对照）

通观 `codex/gpt-6.1-terra` 第 32—33 波所撰 7 张人物卡，呈现出一套高度一致的**“结构规整但脱离站内既有档案深度”**的通病特征：文字克制、不轻易捏造长段伪直引，但在**日期双历校勘、外链实测、站内 S/A 级精读调用、争鸣节点对齐与尾行结构**五个环节均出现系统性滑坡。

### 6.1 七卡系统性问题横向矩阵

| 人物卡 | P0 级问题 | P1 级问题 | P2 级问题 | 核心跨卡共病诊断 |
| :--- | :---: | :---: | :---: | :--- |
| [`PER-struve.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-struve.md) | 0 | **2** | 1 | 绕开 `RN-W1B/W2`、`CON-intelligentsia-and-vekhi`、`Gaida`、`Mawdsley`、`PER-wrangel`，反引 C 级 `encyclopedia.com`；1902–1904《解放》刊期未拆清 |
| [`PER-guchkov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-guchkov.md) | **1** | **2** | 1 | `related_debates` 挂接未建卡 `DEB-1917-february-liberal-role-and-dual-power` 断链（P0）；绕开《退位诏书》三语原文与 L3；第三届杜马/军工委起讫及政变方案过粗 |
| [`PER-rodzianko.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-rodzianko.md) | **1** | **2** | 1 | `related_debates` 挂接未建卡 `DEB-1917-february-liberal-role-and-dual-power` 断链（P0）；漏二月大公宪制宣言、德诺爽约与百万街反转；把库内 `Hasegawa` 已载电报线索标“待核查” |
| [`PER-savinkov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-savinkov.md) | **1** | **2** | 1 | 错域死链 `openstax.marxists.info`（P0）；漏 1919–1921 NSZRiS 演进及 1924 公审认罪改判；绕开 `Leggett ch10–11`、`Pipes ch20` |
| [`PER-sukhanov.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sukhanov.md) | **1** | **2** | 1 | **出生日期双重换算错移 12 天**（`12-09` 误当 O.S. 算出 `12-21`，P0）；错把库内已有《第一号命令》《论我国革命》原文及 3 条 L3 标为“待补”；`[T3]` 末悬空尾句 |
| [`PER-yagoda.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-yagoda.md) | 0 | **2** | 1 | 绕开库内 `Kotkin ch21`、`Lewin ch12`、`Mozokhin ch06`、`Leggett ch10/12/16` 将已有档案标为“待核”；缺出生月日与 `1923-09-18` / `1929-10-27` 任免节点；`[T3]` 末悬空尾句 |
| [`PER-mikoyan.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-mikoyan.md) | 0 | **2** | 1 | 漏 1920–1922 下诺夫哥罗德党职跃升；以未提米高扬的 `RN-W32` 替代 `Carr–Davies`/`Daniels`/`Kotkin`/`RN-W8`，抹平 1928 年 7 月全会摇摆；`[T3]` 末悬空尾句 |
| **合计（7 张）** | **4 项 P0** | **14 项 P1** | **7 项 P2** | **共发现 25 项可操作修订点** |

### 6.2 优先修复行动矩阵（建议执行顺序）

| 优先级 | 类别 | 具体修复清单（按影响面降序） | 涉及卡片 |
| :---: | :--- | :--- | :--- |
| **1（立即）** | **P0 史实/历法/死链/断链清零** | ① 修正 `PER-sukhanov` 生年为 `1882-11-27 [O.S.] / 1882-12-09 [N.S.]`（含 `start_ns`）；<br>② 清理 `PER-savinkov` 失效的 `openstax.marxists.info` 错域链接并替换真实档案 URL；<br>③ 将 `PER-guchkov` 与 `PER-rodzianko` 的 `related_debates` 从未建卡 `DEB-1917-february-liberal-role-and-dual-power` 改为库内主卡 `DEB-1917-dual-power-and-february-origins`。 | `PER-sukhanov`, `PER-savinkov`, `PER-guchkov`, `PER-rodzianko` |
| **2（紧接）** | **P1 站内 S/A 级馆藏与 L3 回链重织** | 逐卡把错标为“待核/待补”或用 `encyclopedia.com` 顶替的内容，改回对接库内既有《第一号命令》《退位诏书》《论我国革命》原文及 `Walicki`、`Gaida`、`Hasegawa`、`Pipes`、`Leggett`、`Mozokhin`、`Kotkin`、`Carr–Davies`、`Daniels`、`RN-W8` 与对应 L3 时间线；清理 `PER-mikoyan` 对 `RN-W32` 的错配引用。 | 全部 7 张卡 |
| **3（同批）** | **P1 职衔起止与关键转折补全** | 补全罗将柯二月大公宪制宣言、德诺爽约与百万街反转；古契科夫第三届杜马/军工委起讫及五人委员会政变细节；萨温科夫 1919–1921（RPC→NSZRiS→驱逐）及 1924.08 认罪改判；雅戈达 `1920-07-29`、`1923-09-18/11-02`、`1929-10-27`、`1934–1938` 任免；米高扬 1920–1922 下诺夫哥罗德、`1926-07-23`/`08-14` 及 1928.07 摇摆；苏汉诺夫 1917.05 入党与 1931/1940 分期；司徒卢威 1902–1904《解放》与 1915.06.08 退委。 | 全部 7 张卡 |
| **4（同批）** | **P1/P2 图谱关系边表补全** | 补齐 7 卡 `2.2` 边表漏连的库内实卡与事件节点（如 `PER-wrangel`, `CON-intelligentsia-and-vekhi`, `ORG-octobrists-and-progressive-bloc`, `ORG-provisional-government`, `PER-nicholas-ii`, `INS-state-duma-1906-1917`, `PER-lvov`, `PER-kornilov`, `PER-sverdlov`, `ORG-united-opposition`, `PER-ordzhonikidze`, `PER-kamenev`, `PER-gorky`, `PER-tsereteli`, `PER-trotsky`）。 | 全部 7 张卡 |
| **5（收尾）** | **P2 Schema 与尾部格式归一化** | 依 [`docs/TEMPLATES.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/docs/TEMPLATES.md) 将 `start_year`/`end_year` 及 `start_ns: "1891"` 全部补为标准 ISO 公历 `start_ns`/`end_ns`（正文附 `+12` 天双标）；消除 `PER-sukhanov:49`、`PER-yagoda:50`、`PER-mikoyan:49` 位于 `[T3]` 末尾的无标题悬空尾句；重跑 `python scripts/kb.py pack` 刷新 7 份 1-hop 上下文包。 | 全部 7 张卡 |
