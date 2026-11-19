# AUD-18C｜第41波 Codex 升格概念／机构／政策枢纽卡异源交叉审计报告（7 张）

- **审计日期**：2026-11-19
- **审计角色**：`dialectic-auditor`（跨模型家族异源交叉审计：Google `gemini-4-neon` 审读 OpenAI `gpt-6.1-terra` 在 Wave 41 升格的 7 张 `CON-*` / `INS-*` / `POL-*` 枢纽卡）。
- **唯一写入目标**：[`audits/AUD-18C-wave41-codex-con-ins-pol-audit.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-18C-wave41-codex-con-ins-pol-audit.md)；纯只读审计，未改动任何被审卡片、论断卡、札记或共享图谱文件。
- **审计对象（两阶段增量落盘）**：
  - **阶段一（01–04，本节已完成）**：
    1. [`CON-narodnichestvo`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md)
    2. [`CON-smychka`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-smychka.md)
    3. [`CON-soviet`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-soviet.md)
    4. [`INS-rkka-red-army-and-rvr`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rkka-red-army-and-rvr.md)
  - **阶段二（05–07 与汇总修复动作矩阵，已完成）**：
    5. [`INS-vsnkh-and-gosplan`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md)
    6. [`POL-ban-on-factions-1921`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-ban-on-factions-1921.md)
    7. [`POL-brest-litovsk-treaty`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md)

---

## 一、审计方法、判级准则与全 7 卡机械体检基线

1. **判级准则**（严格沿用 [`AUD-18A`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-18A-wave39-codex-deb-batch1-audit.md) 与 [`AUD-18B`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-18B-wave40-codex-deb-batch2-audit.md) 标准）：
   - **P0**：史实／双历换算硬伤、断链／悬空节点 ID、望文件名猜作者名／隐去真实作者／把论文集主编误作单篇作者／凭空曲解或倒置所引 `CLM-*` 原旨、错配无关札记；
   - **P1**：站内已有 S/A 级原典、定量数据卡（`data/DATA-01..08`）、Wave 39 新增精读札记与列宁 1922–1923 原典漏引、将站内已可核事项误标为“待核查”或缺口、关键时段断档、挂名学者无 `CLM-*` 落地、§2.2 边表严重漏挂核心枢纽；
   - **P2**：Schema 细节、`[T1]` 字数、标题跳号（直接 `### 3.3` 无 `3.1`/`3.2`）、§2.2 边表缺标准模板第 5 列、锚文本漏合著者或措辞微瑕。
2. **机械校验结果（全 7 卡只读脚本实测）**：

| 序号 | 卡片 ID | 类型 | 相对路径链接（命中/断链） | 正文反引号 ID（命中/断链） | `related_debates`（命中/断链） | `[T1]` 字数（≤150） | `graph/edges.jsonl` 已有边数 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 01 | `CON-narodnichestvo` | concept | 11 / 0 | 5 / 0 | 1 / 0 | 119（合格） | 15 |
| 02 | `CON-smychka` | concept | 20 / 0 | 5 / 0 | 1 / 0 | 117（合格） | 9 |
| 03 | `CON-soviet` | concept | 12 / 0 | 4 / 0 | 2 / 0 | 121（合格） | 12 |
| 04 | `INS-rkka-red-army-and-rvr` | organization | 6 / 0 | 4 / 0 | 2 / 0 | 112（合格） | 18 |
| 05 | `INS-vsnkh-and-gosplan` | organization | 8 / 0 | 6 / 0 | 2 / 0 | 120（合格） | 19 |
| 06 | `POL-ban-on-factions-1921` | policy | 9 / 0 | 5 / 0 | 1 / 0 | 117（合格） | 14 |
| 07 | `POL-brest-litovsk-treaty` | policy | 7 / 0 | 5 / 0 | 1 / 0 | 113（合格） | 15 |

> **全 7 卡机械基线结论**：7 张卡**无任何断链相对路径、无任何悬空节点 ID、`[T1]` 字数全部严格控制在 112–121 字之间**。共通结构微瑕（统一归 P2）：全部 7 卡均在 `## [T3]` 下直接跳号至 `### 3.3 本地证据入口`（缺 `3.1`/`3.2`），且 §2.2 边表统一采用 4 列格式，缺少 [`docs/TEMPLATES.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/docs/TEMPLATES.md#L55-L58) 标准的第 5 列“核心依据/争鸣”。

---

## 二、阶段一（01–04）历法与时域核查表

| 卡片 | 卡内日期（YAML／正文） | 历法与时域复算核查 | 判定 |
| :--- | :--- | :--- | :--- |
| 01 `CON-narodnichestvo` | YAML：`1860-01-01`..`1929-12-31`（已注为研究窗口）；正文：1874、1879、1880—1890年代、1881 通信 | 全文仅用年份，无错历；所引 1881-03-08 马克思致查苏利奇信为伦敦公历（19 世纪俄历差 `+12` 天即 `1881-02-24 [O.S.]`） | **历法无硬伤** |
| 02 `CON-smychka` | YAML：`1921-01-01`..`1929-12-31`（已注为研究窗口）；正文：1921—1923、1923、1925、1928、1929 | 全段处 `1918-02-14` 后纯公历期，守住 `<= 1929` 分期上限 | **历法合规** |
| 03 `CON-soviet` | YAML：`1905-01-01`..`1929-12-31`（已注为研究窗口）；正文：`1917-03-01 [O.S.] / 1917-03-14 [N.S.]`、1918年6月、1918年7月10日、1921 | `1917-03-01 + 13 天 = 1917-03-14`（20 世纪 `+13` 天换算准确）；`1918-07-10` 改历后纯公历准确 | **历法合规**；1922–1929 时域正文断档（P1），1918年6月宜补精确日 `1918-06-14`（P2） |
| 04 `INS-rkka-red-army-and-rvr` | YAML：`start_os: 1918-01-15`、`start_ns: 1918-01-28`、`end_ns: 1929-12-31`；正文：`1918-01-15 [O.S.] / 1918-01-28 [N.S.]`、1918年9月、1919八大、1924—1925伏龙芝改革 | `1918-01-15 + 13 天 = 1918-01-28`（早于 1918-02-14 改历，换算准确）；1918-09 及 1920s 纯公历准确 | **历法合规**；1918年9月革军委成立站内可核精准日 `1918-09-02`（P2）；1925–1929 伏罗希洛夫时期正文缺位（P1） |

---

## 三、阶段一逐卡深度审计与修复方案（01–04）

### 01｜俄国民粹主义：运动、自我认知与论战范畴（`CON-narodnichestvo`）

**总体评价**：时间分期与多源并行意识清楚，所引 5 张 `CLM-*` 学者署名无误，但存在 **1 处 P0（倒置狭义／广义概念并曲解所引 `CLM-walicki-1969-narodnichestvo-definition` 核心原旨）**、**2 处 P1（站内已有原典群、Berlin 伦理人文主义卡、Hildermeier 两张 A 级 `CLM-*` 与 §2.2 核心实体漏挂）** 与 **1 处 P2（重复锚文本与格式跳号）**。

#### 01-01｜P0｜倒置“狭义／广义”概念并直接曲解所引 `CLM-walicki-1969-narodnichestvo-definition` 核心原旨
- **定位**：[`CON-narodnichestvo.md:21`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L21)（`[T1]`）、[`L27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L27)、[`L35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L35)、[`L38`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L38)、[`L40`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L40)、[`L52`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L52)。
- **核证**：
  1. 本卡在 `[T1]` 写“**列宁批判的狭义经济民粹派不能等同整个传统**”，在 L27 写“**列宁‘经济浪漫主义’所指的狭义经济论战对象不涵盖全部革命派**”，在 L35/L38 将列宁归结为“论战分类”“一手政治干预”，并在 L40、L52 直接援引 [`CLM-walicki-1969-narodnichestvo-definition.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-walicki-1969-narodnichestvo-definition.md) 作为依据。
  2. 打开 [`CLM-walicki-1969-narodnichestvo-definition.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-walicki-1969-narodnichestvo-definition.md#L18-L33) 及其母札记 [`RN-W1B`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/walicki_1969_controversy/RN-W1B-populism-concept-and-marxism.md#L40-L56) 与 [`RN-W2`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/walicki_1969_controversy/RN-W2-populism-concept-and-marxism.md#L24-L29) 逐字对勘，发现卡片**将 Walicki 与 Pipes 的核心概念界定完全颠倒**：
     - 在 Walicki 援引并回应 Richard Pipes (1964) 的经典二分中，**“狭义（历史义）”**指 1870 年代中期反对知识分子包办、主张群众凌驾受教育精英之上的短期反智主义插曲（在该狭义下连拉甫罗夫派、特卡乔夫与民意党都**不算**民粹派）；而**列宁**恰恰奠定了**“广义（历史社会学／马克思主义义）”**（“一整套世界观，其历史始于赫尔岑，终于丹尼尔逊”，反映小生产者抗拒资本主义摧残又要求废除封建残余的抗议，涵盖 70 年代革命者、80–90 年代合法民粹派乃至 20 世纪初农民政党与孙中山）。
     - 更关键的是，`CLM-walicki-1969-narodnichestvo-definition` 的核心命题正是**反驳 Pipes 将列宁／马克思主义广义民粹主义贬为“论战伎俩（mere ‘polemical device’）”**，明确肯定列宁的广义定义是“极其精准的方法论分析工具（methodological device, and a very good one）”，同时据此修正 Koz'min，将 1860 年代赫尔岑（贵族社会主义）与车尔尼雪夫斯基（启蒙遗产＋诞生状态的民粹主义）划为“前民粹主义”，而以 **1869 年**作为“古典民粹主义”成型的思想史标尺。
  3. 卡片一方面挂了 `CLM-walicki-1969-narodnichestvo-definition`，另一方面却把列宁针对 1880–1890 年代合法民粹派（沃龙佐夫、丹尼尔逊）的“经济浪漫主义”论战误称为列宁的“狭义定义”，又不加区分地复述 Pipes 的“论战分类／政治干预”定性而不提 Pipes 之名、更抹去 Walicki 对列宁广义社会学定义的辩护，构成典型的**概念倒置与曲解所引 `CLM-*` 原旨**。
- **修复**：重写 `[T1]` 末句及 L27、L35、L38、L40：明确区分（a）**Pipes（1964）所界定的 1870 年代中期“狭义历史义”**（反智群众至上）；（b）**列宁奠定的“广义社会学义”**（涵盖小生产者反封建＋非资本主义发展想象的完整思潮，既批判 1880–1890 年代合法民粹派的“经济浪漫主义”，亦承袭其反封建民主内核）；（c）**Walicki（1969）对列宁广义定义的方法论辩护**与“1860s 前民粹 vs. 1869 年后古典民粹”断代。

#### 01-02｜P1｜漏挂站内已有 S 级原典群、Berlin 伦理人文主义卡及 Hildermeier 两张 A 级 `CLM-*`
- **定位**：[`CON-narodnichestvo.md:14`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L14)、[`L38`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L38)、[`L40-53`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L40-L53)。
- **核证**：
  1. **T3 言行脱节、漏挂同目录 4 份 S 级原典与 1 份考证简报**：L40 强调“1881年马克思—查苏利奇通信须按各稿及往复双方立场区分，不能把草稿当最后复信”，但 §3.3 仅链接了 `1881-03-08_marx-to-zasulich_fr.md` 一份，漏挂同目录站内已有 S 级原典 [`1881-02-16_zasulich-to-marx_fr.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E01_narodniks/1881-02-16_zasulich-to-marx_fr.md)、[`1881_marx-to-zasulich_draft-1_fr.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E01_narodniks/1881_marx-to-zasulich_draft-1_fr.md)、[`1881-03-10_pismo-IK-Aleksandru-III_ru.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E01_narodniks/1881-03-10_pismo-IK-Aleksandru-III_ru.md)、[`1882-01-21_predislovie-russkoe-2e-izdanie.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E01_narodniks/1882-01-21_predislovie-russkoe-2e-izdanie.md) 与系统对校简报 [`WB-W1-narodnik-primary-corpus.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/web-briefs/WB-W1-narodnik-primary-corpus.md)。
  2. **漏挂 Isaiah Berlin 伦理人文主义视角与 Hildermeier 两张 A 级论断卡**：[`graph/edges.jsonl`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/graph/edges.jsonl) 中 `PER-herzen -> CON-narodnichestvo` 与 `PER-lavrov -> CON-narodnichestvo` 两条边均直接以 [`CLM-berlin-1960-populism-moral-core.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-berlin-1960-populism-moral-core.md)（以赛亚·伯林 1960 年《革命的根源》导论，反历史决定论与个人良知核心）为依据，但本卡只字未提伯林；同时，本卡在 L48 挂了 Hildermeier 札记 `RN-W29`，却漏挂其对应的两张 A 级论断卡 [`CLM-hildermeier-2000-agrarian-socialism-modernization-dilemma.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-hildermeier-2000-agrarian-socialism-modernization-dilemma.md) 与 [`CLM-hildermeier-2000-psr-terror-vs-mass-party-dualism.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-hildermeier-2000-psr-terror-vs-mass-party-dualism.md)。
- **修复**：在 §2.3 补入伯林（伦理人文主义／反决定论）与派普斯（语义怀疑论，参见 `CLM-pipes-1990-patrimonial-state-and-intelligentsia` 与 Walicki 商榷）视角；在 §3.3 补齐上述 4 份 S 级原典、`WB-W1`、`CLM-berlin-1960-populism-moral-core` 及 Hildermeier 两张 `CLM-*`。

#### 01-03｜P1｜§2.2 边表过瘦，漏挂 6 个正文高频且图谱已有反向边的核心节点
- **定位**：[`CON-narodnichestvo.md:29-36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L29-L36)。
- **核证**：`graph/edges.jsonl` 中共有 15 条边连接 `CON-narodnichestvo`，且本卡正文 L25–28 重点论述了赫尔岑、车尔尼雪夫斯基、1874 年“到民间去”、土地与自由社、社会革命党，但 §2.2 边表仅列 5 行，遗漏 [`ORG-zemlya-i-volya`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-zemlya-i-volya.md)、[`ORG-psr`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-psr.md)、[`PER-herzen`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-herzen.md)、[`PER-chernyshevsky`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-chernyshevsky.md)、[`EVT-1874-going-to-the-people`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1874-going-to-the-people.md)、[`EVT-1881-03-assassination-of-alexander-ii`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1881-03-assassination-of-alexander-ii.md)。
- **修复**：在 §2.2 补全上述核心节点边（并按模板补齐第 5 列“核心依据/争鸣”）。

#### 01-04｜P2｜§3.3 重复锚文本挂接两份 Walicki 札记，且 T3 标题跳号
- **定位**：[`CON-narodnichestvo.md:42`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L42)、[`L46-47`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md#L46-L47)。
- **核证**：L46–47 连续两条完全相同锚文本 `- [Walicki精读](...)` 分别指向 `RN-W1B` 与 `RN-W2`，未向读者说明两份同书精读札记的区别；`## [T3]` 下直接跳至 `### 3.3`；§2.2 缺第 5 列。
- **修复**：为 `RN-W1B` 与 `RN-W2` 标注各自编号/侧重（或择优主挂 `RN-W2` 详注版）；统一调整 T3 标题层级与边表列数。

---

### 02｜工农结合（`CON-smychka`）

**总体评价**：所引 12 张 `CLM-*`、4 份 `RN-*` 与 3 份原典均核对真实准确（**0 P0**），对 1923 年剪刀差与 1928–1929 年转折的脉络概括稳健。但存在 **3 处显著 P1**：一是将站内已完整入库的斯大林 1929-04-22 演说“生产性结合（производственная смычка）”双语原典**误标为 `perspectives_missing` 缺口**；二是**集中漏挂 Wave 39 新增列宁绝笔“换马隐喻”原典与泽姆斯科夫“贡税”论断卡、剪刀差定量卡 `DATA-02` 及列宁合作社转向论断卡**；三是 §2.2 边表竟漏挂 `PER-lenin` 等核心枢纽；另有 **1 处 P2**（锚文本漏合著者 Carr 及匿名链接）。

#### 02-01｜P1｜将站内已有 S 级双语原典误标为缺口（`production-smychka-primary-wording`）
- **定位**：[`CON-smychka.md:15`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-smychka.md#L15)、[`L27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-smychka.md#L27)。
- **核证**：
  - YAML L15 将 `"production-smychka-primary-wording"` 列为 `perspectives_missing`，暗示站内缺乏“生产性结合（производственная смычка）”的一手原始措辞。
  - 实查站内 S 级英俄双语全本 [`sources/web-archive/E02_E10_core_classics/1929-04-22_right-deviation-in-cpsu.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E10_core_classics/1929-04-22_right-deviation-in-cpsu.md)（斯大林 1929-04-22 在联共（布）中央与中监委联席全会演说《论联共（布）党内的右倾》），内设整节 **`f) The Rate of Development of Industry and the New Forms of the Bond`**（英文 [`L617-686`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E10_core_classics/1929-04-22_right-deviation-in-cpsu.md#L617-L686)，俄文 [`L1789-1845`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E10_core_classics/1929-04-22_right-deviation-in-cpsu.md#L1789-L1845)），在 [`L1841`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E10_core_classics/1929-04-22_right-deviation-in-cpsu.md#L1841) 明确出现俄文原词——`как средства установления производственной смычки между индустрией и сельским хозяйством`（对应英文 `L680`：`as means of establishing a bond between industry and agriculture in the sphere of production`），系统对比了“仅满足农民棉布鞋袜等个人消费需求的旧结合形式”与“依托集体农庄、国营农场、预购合同制（контрактация）与机器拖拉机站满足农业生产重建需求的生产性结合”。
- **修复**：从 `perspectives_missing` 移除 `"production-smychka-primary-wording"`；在 L27 与 §3.3 正式锚定 [`1929-04-22_right-deviation-in-cpsu.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E10_core_classics/1929-04-22_right-deviation-in-cpsu.md)（并注明该文献为斯大林反右倾政治演说，须与布哈林同期四月全会辩护词 [`1929-04-18_bukharin-april-plenum-speech-defense-of-nep.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/W32_milestone_docs/1929-04-18_bukharin-april-plenum-speech-defense-of-nep.md) 对读）。

#### 02-02｜P1｜漏挂 Wave 39 列宁《宁肯少些，但要好些》与泽姆斯科夫“贡税”论断卡、剪刀差数据卡 `DATA-02` 及多份核心原典／论断卡
- **定位**：[`CON-smychka.md:25-27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-smychka.md#L25-L27)、[`L37-61`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-smychka.md#L37-L61)。
- **核证**：
  1. **漏挂 Wave 39 列宁 1923 绝笔原典**：[`sources/web-archive/W39_lenin_1922_1923_docs/1923-03-02_lenin-better-fewer-but-better.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/W39_lenin_1922_1923_docs/1923-03-02_lenin-better-fewer-but-better.md)（及导读 [`WB-W39-lenin-1922-1923-final-writings-and-shuia.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/web-briefs/WB-W39-lenin-1922-1923-final-writings-and-shuia.md)）中著名的**“换马隐喻”**（保持工人阶级对小农的领导与信任＋极端节约国家机关，方能“从农民的、庄稼汉的、穷苦的马上……跨到大机器工业、电气化、沃尔霍夫水电站工程的马上”）是列宁晚年关于 `smychka` 存续与积累战略的最高原典锚点，本卡完全漏引。
  2. **漏挂 Wave 39 泽姆斯科夫“贡税”论断卡**：[`CLM-zemskov-2018-agrarian-tribute-and-coercive-turn.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-zemskov-2018-agrarian-tribute-and-coercive-turn.md)（B 级，配套 [`RN-W39-stalin-era-nep-to-great-turn-1924-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/stalin_era_economy_repression_1924_1954_zh/RN-W39-stalin-era-nep-to-great-turn-1924-1929.md)）直接辨析 1920 年代低价收购／高价工业品剪刀差及斯大林 1928-07-09 全会“贡税／特别税”话语，恰可与 Cohen、Erlich、Carr–Davies 对勘（须保留 B 级与证据层级边界标注）。
  3. **漏挂剪刀差数据卡与合作社转向论断卡**：正文 `[T1]` 与 L26 均以 1923 年剪刀差为关键分期，却只挂了 1926–1929 粮食数据卡 `DATA-03`，彻底漏挂站内专论 1922–1924 剪刀差与切尔文币的 [`DATA-02-1922-1924-scissors-crisis-and-chervonets.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-02-1922-1924-scissors-crisis-and-chervonets.md) 与 [`CLM-carr-1954-scissors-crisis-mechanics.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1954-scissors-crisis-mechanics.md)；同时漏挂 `targets_cards` 已明确指向 `CON-smychka` 的 [`CLM-lewin-1968-cooperation-shift.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-lewin-1968-cooperation-shift.md)（剖析列宁《论合作社》“完全教义转向”及其商业合作社局限）。
  4. **漏挂多项 S 级一手原典**：[`1921-03-21_decree-on-tax-in-kind-prodnalog.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E03_E08_party_and_state_docs/1921-03-21_decree-on-tax-in-kind-prodnalog.md)（实物税起点）、[`1928-05-28_stalin-on-the-grain-front.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E09_E10_party_debates/1928-05-28_stalin-on-the-grain-front.md)（涅姆奇诺夫表原演说）以及 [`1928-09-30_bukharin-notes-of-an-economist.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E09_state_and_comintern/1928-09-30_bukharin-notes-of-an-economist.md)（L56 挂了二手 `CLM-cohen-1973-notes-of-an-economist.md` 却漏挂原典本身）。
- **修复**：在 `[T2]` 与 §3.3 补齐上述 Wave 39 原典与论断卡、`DATA-02`、`CLM-carr-1954-scissors-crisis-mechanics`、`CLM-lewin-1968-cooperation-shift` 及 3 份 S 级原典。

#### 02-03｜P1｜§2.2 边表漏挂 `PER-lenin` 等关键枢纽，`related_debates` 漏挂 1929 集体化争鸣
- **定位**：[`CON-smychka.md:16`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-smychka.md#L16)、[`L28-35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-smychka.md#L28-L35)。
- **核证**：L25/L42 重点论述列宁建立实物税与合作社结合，但 §2.2 边表仅有 5 行，漏挂 `PER-lenin`、`EVT-1923-scissors-crisis`、`EVT-1928-grain-procurement-crisis`、`CON-primitive-socialist-accumulation`（`graph/edges.jsonl` 已有双向对应）与 `POL-first-five-year-plan`；`related_debates` 仅列 `DEB-1928-bukharin-alternative`，漏挂 [`DEB-1929-collectivization-and-dekulakization-causes`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md)。
- **修复**：补齐 §2.2 上述关键边及 `related_debates`。

#### 02-04｜P2｜§3.3 锚文本漏合著者 E. H. Carr、匿名 `[相关论断]` 与标题跳号
- **定位**：[`CON-smychka.md:41`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-smychka.md#L41)、[`L50-52`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-smychka.md#L50-L52)、[`L60-61`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-smychka.md#L60-L61)。
- **核证**：L60–61 两张合著论断卡（`scholar: SCH-carr-davies`，*Foundations of a Planned Economy, 1926–1929, Vol. 1, Part 1*, 1969）在锚文本中仅写 `[Davies论断]` 而隐去第一作者 E. H. Carr；L50–52 连续 3 条写匿名 `[相关论断]` 未注明作者 Alexander Erlich；T3 跳号 `### 3.3`、§2.2 缺第 5 列。
- **修复**：锚文本改为 `[Carr & Davies论断]`、`[Erlich论断]`，并统一修补 T3 层级与边表列数。

---

### 03｜苏维埃：代表委员会与国家形式的系谱（`CON-soviet`）

**总体评价**：双历换算（`1917-03-01 [O.S.] / 1917-03-14 [N.S.]`）与 6 张所引 `CLM-*` 署名全部准确（**0 P0**），且吸纳了 Churakov 地方工人抗议史视角。但存在 **2 处重要 P1**：一是虽然 YAML 时域覆盖至 `1929-12-31`，正文却在 1921 年喀琅施塔得处截断，**1922–1929 年 NEP 苏维埃选举、城乡 5:1 不等权与剥权者（лишенцы）完全空白**，同时漏挂多份站内已有核心原典（含正文点名要求“逐条阅读”的彼得罗巴甫洛夫斯克决议！）与定量卡 `DATA-01`/`DATA-07`；二是**淡化了 Avrich 对“不要布尔什维克的苏维埃”口号的明确证伪**，且 3 位已列入正文的学者有 `RN-*` 无 `CLM-*`、边表仅 4 行。另有 **1 处 P2**。

#### 03-01｜P1｜1922–1929 时域断档，漏挂 1918 宪法 5:1 不等权／剥权者／“活跃苏维埃”论断卡、原典决议与 `DATA-01`/`DATA-07`
- **定位**：[`CON-soviet.md:11-12`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-soviet.md#L11-L12)、[`L26-27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-soviet.md#L26-L27)、[`L40-52`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-soviet.md#L40-L52)。
- **核证**：
  1. **1918 宪法关键制度机制与 1922–1929 年 NEP 苏维埃演变双双空白**：§3.3 虽链接了 [`1918-07-10_rsfsr-constitution-franchise-and-power.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E03_E08_party_and_state_docs/1918-07-10_rsfsr-constitution-franchise-and-power.md)，正文却未交代该宪法最核心的苏维埃代表制结构——第 25 条“城市每 2.5 万选民 1 代表 vs. 省每 12.5 万居民 1 代表”的 **5:1 城乡不等权代表比例**、第 65 条阶级剥权者（**лишенцы**）以及立法行政合一原则；且在 1921 年后直接断档，完全漏掉 1924–1927 年“活跃苏维埃（оживление советов）”实验与多级间接选举悖论。站内已有对应的 [`CLM-carr-1950-1918-constitution-fusion-of-powers-and-class-franchise.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1950-1918-constitution-fusion-of-powers-and-class-franchise.md)、[`CLM-soviet-democracy-1918-1929-lishentsy-and-unequal-franchise.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-soviet-democracy-1918-1929-lishentsy-and-unequal-franchise.md) 与 [`CLM-soviet-democracy-1924-1927-ozhivlenie-sovetov-paradox.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-soviet-democracy-1924-1927-ozhivlenie-sovetov-paradox.md)（引后两卡时须显式标注 Michael Kubi 2015 为 B 级护教视角并与 Carr 宪制分析对勘）。
  2. **正文呼唤“逐条阅读原决议”却漏挂站内已有 S 级原典**：L27 提醒“不能替代逐条阅读原决议”，却漏挂 [`1921-03-01_petropavlovsk-resolution.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E07_foundational_docs/1921-03-01_petropavlovsk-resolution.md)，并漏挂 1905 年 [`1905-12-02_petersburg-soviet-financial-manifesto.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E01_E10_supplements/1905-12-02_petersburg-soviet-financial-manifesto.md) 与 1918 年 [`1918-01-03_declaration-rights-working-exploited.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E07_foundational_docs/1918-01-03_declaration-rights-working-exploited.md)。
  3. **漏挂定量数据卡 `DATA-01`/`DATA-07` 与法统冲突论断卡**：L26 论及“秋季大城市布党优势也不等于全国普选多数”，却未挂提供 1905 彼得堡苏维埃 562 代表构成、1917 彼得格勒／莫斯科苏维埃与杜马选举摆动及立宪会议全俄得票率的 [`DATA-01`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-01-1905-1917-strikes-and-petrograd-elections.md)、[`DATA-07`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-07-1905-1918-unions-moscow-swings-and-constituent-assembly-votes.md) 与 [`CLM-yao-hai-constituent-assembly-vs-soviet-legitimacy-clash.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-yao-hai-constituent-assembly-vs-soviet-legitimacy-clash.md)。
- **修复**：在 §2.1 补入 1918 年宪法第 25/65 条制度机制及 1924–1927 年“活跃苏维埃”与一党制边界；在 §3.3 补挂上述原典、数据卡与论断卡。

#### 03-02｜P1｜淡化 Avrich 对喀琅施塔得口号的证伪、3 位学者缺 `CLM-*` 落地，且 §2.2 边表过瘦
- **定位**：[`CON-soviet.md:27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-soviet.md#L27)、[`L28-36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-soviet.md#L28-L36)、[`L47-49`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-soviet.md#L47-L49)。
- **核证**：
  1. L27 仅将“不要布尔什维克的苏维埃”称作“常见概括”，而所引 [`CLM-avrich-1970-soviets-without-bolsheviks.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-avrich-1970-soviets-without-bolsheviks.md#L18-L33) 的实证结论要锋利得多：该口号**从未**为喀琅施塔得起义者采用（原为西伯利亚农民与马赫诺派口号，经米留科夫在巴黎《最新消息报》转述渲染），水兵真实标语为**“一切权力归苏维埃，而非政党”**，且代表会议中仍允许布尔什维克与左翼社会主义者并存参选。
  2. 苏汉诺夫、长谷川毅与 Rabinowitch 三家均列入 `perspectives_present` 与 §2.3，却仅在 §3.3 挂了 `RN-*` 而漏挂站内已有核心论断卡 [`CLM-sukhanov-1922-dual-power-pact.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-sukhanov-1922-dual-power-pact.md)、[`CLM-hasegawa-2018-dual-power-origins.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-hasegawa-2018-dual-power-origins.md)、[`CLM-rabinowitch-2007-contingency-of-dictatorship.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-rabinowitch-2007-contingency-of-dictatorship.md)、[`CLM-rabinowitch-2007-constituent-assembly.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-rabinowitch-2007-constituent-assembly.md)。
  3. §2.2 边表仅 4 行，漏挂已在 `graph/edges.jsonl` 指向本卡的 `EVT-1905-revolution`、`EVT-1917-02-february-revolution`、`EVT-1917-10-october-revolution`、`ORG-petrograd-soviet`、`ORG-makhnovshchina`。
- **修复**：按 Avrich 原旨写清口号证伪；补挂上述 `CLM-*` 与 §2.2 边表核心节点。

#### 03-03｜P2｜1918 年 6 月中执委开除决定可补精准日，T3 跳号与边表缺列
- **定位**：[`CON-soviet.md:27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-soviet.md#L27)、[`L40`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-soviet.md#L40)。
- **核证**：L27“1918年6月孟什维克及右派社革党被排除于全俄中执委”可精确标为 `1918-06-14`（改历后纯公历）；T3 跳号 `### 3.3`、§2.2 缺第 5 列。
- **修复**：补注 `1918-06-14` 精确日并统一结构格式。

---

### 04｜工农红军与共和国革命军事委员会（`INS-rkka-red-army-and-rvr`）

**总体评价**：双历换算（建军令 `1918-01-15 [O.S.] / 1918-01-28 [N.S.]`）准确，所引 Kakurin 与 Smirnov 3 张 `CLM-*` 署名及原旨准确（**0 P0**）。特别值得肯定的是，经全库（含 `cards/`、`reading-notes/`、`data/`、`timeline/` 与全部 `sources/monographs/`）专项检索核验，**战后红军裁军至“56.2 万”这一数字在站内任何札记、数据卡或专著文本中均无出处**（站内所有“562”仅指 1905 年彼得堡苏维埃 562 名代表及若干 56.2% 比例），因此 L27 对“约 56.2 万人……尚未在所引札记中核实，不宜作为确定值”的处理**属合规的认识论审慎，并非把站内已可核数字误标为待核**。但本卡仍存在 **2 处明显 P1**（3 位挂名学者在 §3.3 零 `CLM-*` 落地；1925–1929 伏罗希洛夫时代与 `DATA-05` 关键硬数据大段缺位，且抛出未经 `DATA-05` 核实的“约 500 万”）与 **1 处 P2**。

#### 04-01｜P1｜`perspectives_present` 与 §2.3 挂名的 Mawdsley、Deutscher、Service 在 §3.3 零 `CLM-*` 落地
- **定位**：[`INS-rkka-red-army-and-rvr.md:14`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rkka-red-army-and-rvr.md#L14)、[`L36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rkka-red-army-and-rvr.md#L36)、[`L40-46`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rkka-red-army-and-rvr.md#L40-L46)。
- **核证**：
  - `perspectives_present` 列了 `mawdsley-comparative`、`deutscher-trotsky`、`service-critical`，§2.3 L36 亦逐一点评了 Mawdsley、Deutscher、Service，但 §3.3 仅挂了 Kakurin（1 张）与 Smirnov（2 张），上述三家**无一张 `CLM-*` 落地**（Deutscher 与 Service 连 `RN-*` 也未列）！
  - 站内现成且已在 `graph/edges.jsonl` 挂于 `INS-rkka-red-army-and-rvr` 边上的核心论断卡包括：[`CLM-mawdsley-1987-sovdepia-demographic-industrial-base.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-mawdsley-1987-sovdepia-demographic-industrial-base.md)、[`CLM-mawdsley-1987-civil-war-militarized-regime.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-mawdsley-1987-civil-war-militarized-regime.md)、[`CLM-deutscher-1959-disarmed-prophet-paradox.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-deutscher-1959-disarmed-prophet-paradox.md)、[`CLM-service-2009-trotsky-authoritarian-consensus.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-service-2009-trotsky-authoritarian-consensus.md)、[`CLM-service-2009-trotsky-political-tactical-blunders.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-service-2009-trotsky-political-tactical-blunders.md)，以及直接涉及察里津抗命与反波拿巴主义猜忌的 [`CLM-stalin-docs-tsaritsyn-and-civil-war-command-style.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-stalin-docs-tsaritsyn-and-civil-war-command-style.md) 与 [`CLM-shlapentokh-bonapartism-fear-against-trotsky.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-shlapentokh-bonapartism-fear-against-trotsky.md)。
- **修复**：在 §3.3 补挂上述 Mawdsley、Deutscher、Service、Stalin-docs 与 Shlapentokh 论断卡，消除挂名悬空。

#### 04-02｜P1｜1925–1929 伏罗希洛夫时代与 `DATA-05` 核心硬数据缺位，且“约 500 万”未与 `DATA-05` 口径对齐；§2.2 边表过瘦
- **定位**：[`INS-rkka-red-army-and-rvr.md:12`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rkka-red-army-and-rvr.md#L12)、[`L26-34`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rkka-red-army-and-rvr.md#L26-L34)、[`L38`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rkka-red-army-and-rvr.md#L38)。
- **核证**：
  1. **1925–1929 整段失踪**：YAML `end_ns: "1929-12-31"`，但正文写到 1924–1925 年伏龙芝改革即止，完全未交代：1925-01-17 中央—中监委联席全会解除托洛茨基军职、1925-10-31 伏龙芝病逝后由 **`PER-voroshilov`** 接掌陆海军人民委员部与苏联革军委（`РВС СССР`，1923 年 8 月联盟建制后自 `РВСР` 更名）、1926 年 12 月 ОГПУ 警告农民“地域师”可能成为起义骨干、1928 年强制“指挥干部工农化”（工人兵员比例由 1926-04 的 18.1% 升至 1929-01 的 27.3%，步骑兵军校门槛降至 3 年级、伏龙芝学院初等学历新生由 56.6% 飙升至 81.5%），以及 1925–1928 年参谋长 **`PER-tukhachevsky`** 与伏罗希洛夫的职权摩擦——这些全部在卡片已引的 [`RN-W23`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/smirnov_davies_festschrift/RN-W23-1920s-red-army-militia-reform-and-davies-festschrift.md#L25-L50) 与 [`CLM-smirnov-red-army-commanders-vs-voenspetsy-1920s.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-smirnov-red-army-commanders-vs-voenspetsy-1920s.md) 及站内 `PER-voroshilov`/`PER-tukhachevsky` 中有精确页码支撑。
  2. **弃用 `DATA-05` 实证锚点而引入未核峰值**：L26 写“内战末红军在册人数达约 500 万”，但站内 [`DATA-05`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md#L121-L137) 所录 Mawdsley 核实序列为 1918 年底 ≈70 万 → 1919 年 6 月 ≈150 万（一线“刺刀与马刀”仅 **35.6 万**，齿比不足 1:4）→ 1919 年底至 1920 年 **>300 万**（Mawdsley 第 18 章 1920 年夏波兰战役时作 460 万，站内并无“500 万”锚点），同时漏引 `DATA-05` 最核心的建军量化指标：**>4.8 万**前沙皇军官、**≈21.5 万**前军士、**≈16 万**党团员“铁腰撑”及 1919 年 **≈170 万**逃兵与回收机制。
  3. **§2.2 边表仅 4 行**：漏挂 `EVT-1918-1920-russian-civil-war`、`PER-voroshilov`、`PER-tukhachevsky`、`PER-stalin`（察里津抗命与 1920 波兰战役）、`PER-dzerzhinsky`、`POL-first-five-year-plan`（均在 `graph/edges.jsonl` 有现有连接）。
- **修复**：在 §2.1 补齐 1925–1929 伏罗希洛夫掌军、地域师政治忧虑与 1928 工农化，以 `DATA-05` 已核兵力与专家序列替换/标注“500 万”口径差异；补全 §2.2 核心节点边。

#### 04-03｜P2｜革军委成立精准日期（`1918-09-02`）与更名（`РВС СССР`）未注，未核数字按语宜下沉 `[T3]`
- **定位**：[`INS-rkka-red-army-and-rvr.md:25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rkka-red-army-and-rvr.md#L25)、[`L27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rkka-red-army-and-rvr.md#L27)、[`L40`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rkka-red-army-and-rvr.md#L40)。
- **核证**：L25 仅写“1918年9月共和国革命军事委员会成立”，站内 [`PER-trotsky.md:26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-trotsky.md#L26) 与 [`timeline/L3_daily/1918-07_left_sr_uprising_and_red_terror_launch.md:69-73`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1918-07_left_sr_uprising_and_red_terror_launch.md#L69-L73) 已可核精准公历日 **`1918-09-02`**（且应补充 1923 年 8 月随苏联成立改称 `РВС СССР`）；L27 对“56.2 万未核实”的考证注记放于 `[T2]` 正文显得突兀，宜下沉至 `[T3]`；T3 跳号 `### 3.3`、§2.2 缺第 5 列。
- **修复**：L25 补注 `1918-09-02` 与 `РВС СССР` 更名；将 56.2 万口径待核说明移入 `[T3]` 并修补 T3 层级与边表列数。

---

## 四、阶段二（05–07）历法与时域核查表

| 卡片 | 卡内日期（YAML／正文） | 历法与时域复算核查 | 判定 |
| :--- | :--- | :--- | :--- |
| 05 `INS-vsnkh-and-gosplan` | YAML：`start_os: 1917-12-02`、`start_ns: 1917-12-15`、`end_ns: 1929-12-31`；正文：`1917-12-02 [O.S.] / 1917-12-15 [N.S.]`、`1921-02-22`、1924–1926、1926、1928–1929 | `1917-12-02 + 13 天 = 1917-12-15`（20 世纪 `+13` 天准确）；计委设立 `1921-02-22` 为改历后纯公历准确 | **历法合规**；但将站内 Carr 第二卷可核的 ВСНХ 成立三重日期（12-01/12-02/12-05 O.S.）误标为未明历法悬案（P1） |
| 06 `POL-ban-on-factions-1921` | YAML：`start_ns: 1921-03-16`、`end_ns: 1921-03-16`；正文：`1921-03-16`、1922 十一大、1923–1927、`1924-01-17` 十三次党代表会议 | 全部节点均处 `1918-02-14` 后纯公历期；`1921-03-16` 决议通过日与 `1924-01-17` 宣读日经站内 S 级原典双重核实准确 | **历法合规**；缺 `1926-07-23` 首次动用第 7 条关键节点（P1），L26“这不是1922年‘十三大’”指代错位（P2） |
| 07 `POL-brest-litovsk-treaty` | YAML：`start_ns: 1918-03-03`、`end_ns: 1918-11-13`；正文：`1917-12-02 [O.S.] / 1917-12-15 [N.S.]`、`1918年2月10日`、2月18日、2月23日、3月3日、3月6—8日、11月13日 | `1917-12-02 + 13 = 1917-12-15` 准确；`1918-02-18` 及之后均为改历后纯公历准确；**但 `1918年2月10日` 尚早于 `1918-02-14` 俄国改历 4 天（俄历 1918 年无 2 月 10 日），漏标旧历 `[O.S.] 1918-01-28`** | **跨改历临界点双历标注失范（P1）** |

---

## 五、阶段二逐卡深度审计与修复方案（05–07）

### 05｜最高国民经济委员会与国家计划委员会（`INS-vsnkh-and-gosplan`）

**总体评价**：双历换算（`1917-12-02 [O.S.] / 1917-12-15 [N.S.]`；计委 `1921-02-22`）准确；特别值得肯定的是，卡片**精准辨明了 `CLM-plekhanov-am-dzerzhinsky-vsnkh-nep-industrialism-1924-1926` 背后实为拉特科夫斯基（И. С. Ратьковский）著、普列汉诺夫（А. М. Плеханов）编档案的署名关系**，且未把 Davies 纪念论文集主编（Cooper / Perrie / Rees）误署为单篇作者（**0 P0**）。但存在 **3 处显著 P1**（将站内 Carr 第二卷已彻底拆解的 ВСНХ 成立三重日期误标为“待法令原件裁决悬案”；Smith / Erlich / Carr / Katasonov 四家点名学者在 §3.3 零 `CLM-*` 落地且漏引列宁 1922-12 计委立法职能原典与 `DATA-02`/`DATA-03`；§2.2 边表漏挂 10+ 图谱核心枢纽且把已挂 `RN-W23` 中 Gatrell / Rees / Hunter 匿名虚化）与 **1 处 P2**（§3.3 两条重复且错配锚文本）。

#### 05-01｜P1｜将站内 Carr 第二卷已可精确拆解的 ВСНХ 成立三重日期误标为“未明历法悬案”与缺口
- **定位**：[`INS-vsnkh-and-gosplan.md:15`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md#L15)、[`L25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md#L25)、[`L41`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md#L41)。
- **核证**：
  - L25 写：“库内Smith札记另记12月1日而未说明历法，此日期差异须待法令原件裁决，不能掩盖”，YAML L15 亦据此将 `"founding-decree-original"` 列入 `perspectives_missing`。
  - 实查站内已入库经典专著 [`sources/monographs/carr_bolshevik_rev_v2_zh/ch04_第四部分_经济秩序_part_2.md#L314-L318`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/carr_bolshevik_rev_v2_zh/ch04_%E7%AC%AC%E5%9B%9B%E9%83%A8%E5%88%86_%E7%BB%8F%E6%B5%8E%E7%A7%A9%E5%BA%8F_part_2.md#L314-L318)（`[PDF p. 36]`）及 [`smith_sa_1983_red_petrograd_zh/ch11_第九章_十月革命与工业组织.md#L460-L470`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/smith_sa_1983_red_petrograd_zh/ch11_%E7%AC%AC%E4%B9%9D%E7%AB%A0_%E5%8D%81%E6%9C%88%E9%9D%A9%E5%91%BD%E4%B8%8E%E5%B7%A5%E4%B8%9A%E7%BB%84%E7%BB%87.md#L460-L470)（`[PDF p. 171]`）与 [`timeline/L3_daily/1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md#L210`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md#L210)，**三个日期的历法与法律程序节点早已全部清晰可核**：
    1. **`1917-12-01 [O.S.] / 1917-12-14 [N.S.]`**：列宁在全俄中执委会议上力挺布哈林所拟 ВСНХ 成立法令草案并获中执委原则通过（即 Smith `ch11` `[PDF p. 171]` 与 `RN-W20` 所记俄历 12 月 1 日，全书 1917 年正文统一采用俄历）；
    2. **`1917-12-02 [O.S.] / 1917-12-15 [N.S.]`**：全俄中执委与人民委员会正式签署生效日（即通用建制日期）；
    3. **`1917-12-05 [O.S.] / 1917-12-18 [N.S.]`**：法令正式公开发表日（Carr 第二卷 `[PDF p. 36]` 详注；需顺带甄别中译本 L316 一处排印笔误“12月3日（12月18日）”，下一句 L318 即正为“12月5日（12月18日）”）。
- **修复**：删去 L25“未说明历法、待法令原件裁决”之误判，在 `[T3]` 如实写明“12-01 O.S. 草案通过 / 12-02 O.S. 正式签署 / 12-05 O.S. 公布”三节点并锚定 Carr 第二卷；将 YAML `perspectives_missing` 的 `"founding-decree-original"` 收窄为仅保留法令条文细则（如俄文全本条文核校）。

#### 05-02｜P1｜`perspectives_present` 与 §2.3 点名 4 家学者在 §3.3 零 `CLM-*` 落地，并漏引列宁 1922-12 计委原典、茹科夫／戴维斯论断与 `DATA-02`/`DATA-03`
- **定位**：[`INS-vsnkh-and-gosplan.md:14`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md#L14)、[`L39`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md#L39)、[`L43-51`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md#L43-L51)。
- **核证**：
  1. **挂名学者与 §3.3 严重脱钩**：§2.3 点评了 Smith、Carr、Erlich、Katasonov，`perspectives_present` 列了 `erlich-industrialization` 与 `katasonov-monetary`，但在 §3.3 中：
     - **Smith 零链接**（连 `RN-W20` 都未挂），漏挂 [`CLM-smith-sa-1983-from-workers-control-to-nationalization.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-smith-sa-1983-from-workers-control-to-nationalization.md) 与 [`CLM-nationalization-docs-1917-workers-control-to-june-1918-decree.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-nationalization-docs-1917-workers-control-to-june-1918-decree.md)；
     - **Erlich 零链接**，漏挂 [`CLM-erlich-1960-stalin-overkill-turn.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-erlich-1960-stalin-overkill-turn.md)；
     - **Katasonov 零 `CLM-*`**，漏挂 [`CLM-katasonov-golden-chervonets-rise-and-demise.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-katasonov-golden-chervonets-rise-and-demise.md) 与 [`CLM-katasonov-two-circuit-cash-noncash-ruble-dam.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-katasonov-two-circuit-cash-noncash-ruble-dam.md)；
     - **Carr 1952/1954 经济史主干零 `CLM-*`**，漏挂 [`CLM-carr-1952-war-communism-internal-contradictions.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1952-war-communism-internal-contradictions.md)（42 个以上总局的“总局制”与实物清算危机）、[`CLM-carr-1952-nep-retreat-and-commanding-heights.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1952-nep-retreat-and-commanding-heights.md) 与 [`CLM-carr-1954-scissors-crisis-mechanics.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1954-scissors-crisis-mechanics.md)。
  2. **漏挂三组高度契合机构博弈的站内硬核材料**：
     - **列宁 1922-12 赋予计委立法职能原典**：[`1922-12_letter-to-the-congress.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E10_turning_points/1922-12_letter-to-the-congress.md)（附 `1922-12-27`《关于赋予国家计划委员会以立法职能》脉络，见 [`timeline/L3_daily/1922-12_lenins_last_struggle_diary.md#L55-L69`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1922-12_lenins_last_struggle_diary.md#L55-L69)），这是计委与最高经委权限之争最重要的原典节点；
     - **财政人民委员部 vs 最高经委直接交锋实证**：[`CLM-other-nep-1923-sokolnikov-monetary-discipline.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-other-nep-1923-sokolnikov-monetary-discipline.md)（尤里·茹科夫：索科利尼科夫推动削减 12% 预算并硬约束信贷 vs 最高经委副主席皮亚塔科夫反击）及 [`CLM-davies-1980-autumn-1929-great-turn-fabrication.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-davies-1980-autumn-1929-great-turn-fabrication.md)（1929 年 8 月计委控制数字突增至 1300 万公顷）；
     - **定量数据卡**：[`DATA-02`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-02-1922-1924-scissors-crisis-and-chervonets.md) 与 [`DATA-03`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-03-1926-1929-grain-procurement-and-famine-indicators.md)。
- **修复**：在 §3.3 补挂上述 `CLM-*`、列宁 1922-12 原典及 `DATA-02`/`DATA-03`，使 `perspectives_present` 与 §2.3 全部有实证着落。

#### 05-03｜P1｜§2.2 边表仅 6 行（漏挂 10+ 图谱核心枢纽），且将已挂 `RN-W23` 单篇作者匿名虚化
- **定位**：[`INS-vsnkh-and-gosplan.md:29-37`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md#L29-L37)、[`L39`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md#L39)。
- **核证**：
  1. `graph/edges.jsonl` 中共有 **19 条边**连接 `INS-vsnkh-and-gosplan`，本卡 §2.2 却仅列 6 行，遗漏创建者与制度裁决者 **`PER-lenin`**、一五计划主导者 **`PER-stalin`**、最高经委实权副主席 **`PER-pyatakov`**（1923 年利润原则法令核心推手）、正文 L28 已点名的 **`PER-strumilin`** 及发生学代表 **`PER-kondratiev`**、直属目标政策 **`POL-first-five-year-plan`**、财政对手机构 **`INS-gosbank-and-narkomfin`**、前身与博弈对象 **`ORG-factory-committees-1917`** 以及 `EVT-1923-scissors-crisis`、`EVT-1929-great-turn-and-dekulakization-launch`。
  2. 本卡挂了 `RN-W23` 与 `CLM-davies-festschrift-1995-nep-statistics-and-planning-debates`，却在 L39 仅笼统称“Davies纪念论文集札记提示计划统计及概念的来源问题”，完全隐去 `RN-W23` 已精读提炼的三位关键单篇作者及其对本机构卡的直接贡献：**Peter Gatrell**（1917–1918 年最高经委与梅谢尔斯基混合托拉斯谈判）、**E. A. Rees**（1928–1929 年最高经委与交通人民委员部铁路投资博弈）与 **Holland Hunter**（1920 年代末统计体系失真与 KAPROST 模型对戴维斯之回应）。
- **修复**：扩充 §2.2 核心关系表至覆盖上述关键人物／机构／政策节点；在 §2.3 明确具名 Gatrell、Rees、Hunter 的具体制度洞见。

#### 05-04｜P2｜§3.3 两条重复且错配锚文本（涅姆奇诺夫表误作“价格论断”），T3 跳号与边表缺列
- **定位**：[`INS-vsnkh-and-gosplan.md:43`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md#L43)、[`L50-51`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md#L50-L51)。
- **核证**：L50–51 连续两条使用完全相同的锚文本 `- [Carr与Davies价格论断](...)`，但 L51 指向 [`CLM-carr-davies-1969-nemchinov-table-critique.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-davies-1969-nemchinov-table-critique.md)，其主题是对斯大林援引涅姆奇诺夫商品粮统计表的批判而非价格论断；另存在全批共通的 `### 3.3` 跳号与 §2.2 缺第 5 列。
- **修复**：L51 锚文本更正为 `[Carr与Davies涅姆奇诺夫表批判论断]`；统一修补 T3 层级与边表列数。

---

### 06｜《关于党的统一》派别禁令（`POL-ban-on-factions-1921`）

**总体评价**：**本批 7 卡中整体最稳健的一张（0 P0）**。经逐字对照站内 S 级原典 [`1921-03-16_on-party-unity.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E10_turning_points/1921-03-16_on-party-unity.md)（中文草案 [`L50`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E10_turning_points/1921-03-16_on-party-unity.md#L50) 与英文通过本 [`L86`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E10_turning_points/1921-03-16_on-party-unity.md#L86)），**秘密第 7 条的适用范围（中央委员、候补中央委员及中央监察委员会委员）与联席全会三分之二多数处分程序（降为候补或开除党籍）核验 100% 精准**，`1924-01-17` 十三次党代表会议公开宣读日与 5 张所引 `CLM-*`（Daniels、Khlevniuk ×3、Apalkov）及两份札记（`RN-W3`、`RN-W6`）均核对无误。主要失分集中在 **2 处 P1**（漏挂 `DATA-04` 投票硬数据、`1926-07-23` 首次动用第 7 条将季诺维也夫逐出政治局的标志性节点、柯伦泰／46人声明／托洛茨基／联合反对派原典及直接指向本卡的 `CLM-goldman-2011-1920s-oppositions-to-enemy-category`；§2.2 边表竟漏挂 `PER-lenin` 与 `EVT-1921-kronstadt`）与 **1 处 P2**。

#### 06-01｜P1｜漏挂 `DATA-04` 十大硬数据、首次正式援引第 7 条的 `1926-07-23` 节点，以及反对派一手原典与 Goldman 反目的论论断卡
- **定位**：[`POL-ban-on-factions-1921.md:15`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-ban-on-factions-1921.md#L15)、[`L24-26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-ban-on-factions-1921.md#L24-L26)、[`L40-49`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-ban-on-factions-1921.md#L40-L49)。
- **核证**：
  1. **漏写“首次正式援引秘密第 7 条”的制度分水岭**：L26 准确提醒“不能把所有后续处分都说成直接援引第 7 条”，却恰恰漏掉了**历史上第一次正式动用第 7 条**的标志性事件——**`1926-07-23` 中央与中监委联席全会**借“拉斯舍维奇林中密会事件”援引秘密第 7 条，将**季诺维也夫逐出政治局**并将**拉舍维奇开除出中央委员会**（站内 [`timeline/L3_daily/1926-07_united_opposition_and_dzerzhinsky_death.md#L92-L98`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1926-07_united_opposition_and_dzerzhinsky_death.md#L92-L98) 与 `graph/edges.jsonl` 边 `PER-zinoviev -> POL-ban-on-factions-1921` `first-politburo-target` 已有明确锚定）。
  2. **漏挂 `DATA-04` 投票量化数据**：[`DATA-04-party-membership-and-congress-votes-1903-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-04-party-membership-and-congress-votes-1903-1929.md) 已核实十大 694 名表决代表构成、工会纲领表决（`336:50:18`）、《关于党的统一》反对票（`<30/694`）及十四大（`559:65`）等连续表决序列，本卡全无引用。
  3. **漏挂直接对象与反目的论对勘卡**：
     - 反对派一手原典与论断：[`CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists.md)（S 级，即本决议草案直接点名的批评对象）、[`1923-10-15_declaration-of-the-forty-six.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E09_state_and_comintern/1923-10-15_declaration-of-the-forty-six.md)（及 [`CLM-carr-1954-platform-of-46-economic-roots.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1954-platform-of-46-economic-roots.md)）、[`1923-12-08_trotsky-new-course-open-letter.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E09_state_and_comintern/1923-12-08_trotsky-new-course-open-letter.md) 与 [`1927-09_platform-joint-opposition-core.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E09_state_and_comintern/1927-09_platform-joint-opposition-core.md)；
     - 直接指向本卡的反目的论论断：[`CLM-goldman-2011-1920s-oppositions-to-enemy-category.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-goldman-2011-1920s-oppositions-to-enemy-category.md)（其 `targets_cards` 显式列出 `POL-ban-on-factions-1921`，辨析 1920 年代党内纪律处分与 1937 年“人民敌人”肉体消灭之间的结构性跃迁而非线性自动滑坡）。
  4. **`related_debates` 不完整**：YAML L15 仅列 `DEB-1921-trade-union-controversy-and-party-unity`，漏挂 `DEB-1928-bukharin-alternative`（尽管 §3.3 所引 5 张 `CLM-*` 中有 4 张均归属后者）。
- **修复**：在 §2.1 补写 `1926-07-23` 首次援引第 7 条逐季诺维也夫出政治局节点；在 §3.3 补挂 `DATA-04`、上述反对派原典与 `CLM-goldman-2011-1920s-oppositions-to-enemy-category`；YAML 补入 `DEB-1928-bukharin-alternative`。

#### 06-02｜P1｜§2.2 边表过瘦（仅 5 行 vs. 图谱 14 条边），竟漏挂起草者 `PER-lenin` 与触发背景 `EVT-1921-kronstadt`
- **定位**：[`POL-ban-on-factions-1921.md:27-34`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-ban-on-factions-1921.md#L27-L34)。
- **核证**：`graph/edges.jsonl` 中共有 14 条边连接 `POL-ban-on-factions-1921`，但 §2.2 边表仅 5 行，遗漏决议起草与报告人 **`PER-lenin`**、直接危机背景 **`EVT-1921-kronstadt`**、与工人反对派并列的受禁派别 **`ORG-democratic-centralists`**、1923–1927 反对派 **`ORG-left-and-united-opposition`**、首例政治局第 7 条适用对象 **`PER-zinoviev`**、执行中枢 **`INS-politburo-orgburo-secretariat`**、学理母概念 **`CON-democratic-centralism-and-vanguard`** 以及十大同期经济退却 **`POL-nep`**（经济放宽＋政治收紧的“双轨结构”）。
- **修复**：补全 §2.2 上述核心节点边（并按模板补齐第 5 列）。

#### 06-03｜P2｜L26“这不是1922年‘十三大’”指代错位、YAML `aliases` 为空及 T3 跳号
- **定位**：[`POL-ban-on-factions-1921.md:8`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-ban-on-factions-1921.md#L8)、[`L26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-ban-on-factions-1921.md#L26)、[`L40`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-ban-on-factions-1921.md#L40)。
- **核证**：L26 写“1924年1月17日十三次党代表会议上斯大林宣读秘密条款；这不是1922年‘十三大’”——事实上俄共（布）十三大召开于 **`1924年5月`**，1922 年为十一大，写“这不是1922年‘十三大’”反而制造莫须有的错误参照；YAML `aliases: []` 缺常见检索词（如 `"秘密第7条"`, `"派别禁令"`, `"党的统一决议"`）；T3 跳号 `### 3.3`、§2.2 缺第 5 列。
- **修复**：L26 改为“（不同于 1924 年 5 月召开的俄共（布）十三大）”；补齐 `aliases` 及结构规范。

---

### 07｜布列斯特-立陶夫斯克和约（`POL-brest-litovsk-treaty`）

**总体评价**：**本批 7 卡中问题最集中、需优先重修的卡片，检出 2 处确凿 P0、2 处 P1 与 1 处 P2**。一是 L38 将 L41 所引列宁 1918 年 5 月名篇《论“左派”幼稚性和小资产阶级性》**误称为 1920 年完全不同的著作《左派幼稚病》**；二是 L36/L44 **错配与布列斯特和约零相关的 `RN-W12B-service-trotsky-critique-and-loginov-1917.md`**（全文 189 行对“布列斯特 / Brest / 不战不和”零命中！）；三是 L38 将站内 `DATA-04` 与 `ORG-left-communists-1918` 早已考证清晰版本出处的俄共七大票数（`28:9:1` vs `30:12:4`）误标为“冲突待核”；四是跨改历临界日 `1918年2月10日` 漏标俄历 `[O.S.] 1918-01-28`、`related_debates` 偏离核心争鸣、§2.2 边表过瘦。

#### 07-01｜P0｜重大书名混淆硬伤：将列宁 1918 年《论“左派”幼稚性和小资产阶级性》误称为 1920 年《左派幼稚病》
- **定位**：[`POL-brest-litovsk-treaty.md:38`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L38)、[`L41`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L41)。
- **核证**：
  - L38 原文：“**列宁《左派幼稚病》**将国家资本主义论战与和约辩护放在1918年具体语境”。
  - 核对 L41 所挂站内原典 [`sources/web-archive/W32_milestone_docs/1918-05_lenin-left-wing-childishness-state-capitalism.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/W32_milestone_docs/1918-05_lenin-left-wing-childishness-state-capitalism.md#L2)，该文确切篇名为**《论“左派”幼稚性和小资产阶级性》**（*“Left-Wing” Childishness and the Petty-Bourgeois Mentality* / *О «левом» ребячестве и о мелкобуржуазности*，写于 1918-05-05，5 月 9–11 日《真理报》连载），针对 1918 年俄国布哈林派“左派共产主义者”的布列斯特与国家资本主义论战。
  - 简称**《左派幼稚病》**在中文与国际学界专指列宁 1920 年 4–5 月面向共产国际西欧极左派撰写的小册子**《共产主义运动中的“左派”幼稚病》**（*“Left-Wing” Communism: An Infantile Disorder* / *Детская болезнь «левизны» в коммунизме*）。两者相差两年、对象与论题迥异，属于典型的**原典篇名混淆 P0 硬伤**。
- **修复**：立即将 L38 改为全称《论“左派”幼稚性和小资产阶级性》（1918 年 5 月），并在 `[T3]` 显式注明勿与 1920 年《共产主义运动中的“左派”幼稚病》混同。

#### 07-02｜P0｜错配与布列斯特和约零相关的精读札记 `RN-W12B`（望文件名拼接挂链）
- **定位**：[`POL-brest-litovsk-treaty.md:36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L36)、[`L44`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L44)。
- **核证**：
  - L36 泛称：“Service与Loginov对领袖决策和政治手腕的不同重视可互相校正”，并在 L44 挂接 [`reading-notes/service_loginov/RN-W12B-service-trotsky-critique-and-loginov-1917.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/service_loginov/RN-W12B-service-trotsky-critique-and-loginov-1917.md)。
  - 逐行通读并用正则全文检索 `RN-W12B`（共 189 行）：该札记的 Robert Service 部分仅覆盖第 23–25 章（1918 年 8 月喀山战役与内战）、第 28–32 章（1920–1923 劳动军与 NEP）、第 37–39 章（1926–1928），Vladlen Loginov 部分仅覆盖 **1917 年**（《列宁在 1917》四月至十月）——**全文对 `布列斯特`、`Brest`、`不战不和`、`1918年2月`、`1918年3月` 全部 0 命中（0 hits）**！
  - 这与 `AUD-18A`/`AUD-18B` 中发现的同源失误一致：作者未打开 `RN-W12B` 核验阅读范围，仅凭文件名含“Service / Loginov”便强行拼接挂入布列斯特卡；而站内真正有布列斯特和约专节的精读札记 [`RN-W22-lenin-formative-decisions-and-dzerzhinsky-cheka-to-vsnkh.md#L106-L115`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/loginov_dzerzhinsky/RN-W22-lenin-formative-decisions-and-dzerzhinsky-cheka-to-vsnkh.md#L106-L115)（拉特科夫斯基传记精读第 3 节：捷尔任斯基 1918-02-23 虽激烈反和却坚持弃权留任以维持党团统一）反遭遗漏。
- **修复**：立即删除 L44 对 `RN-W12B` 的错配链接及 L36 中无证据支撑的“Service与Loginov”空泛评语；改挂站内真正含布列斯特实证的 `RN-W22`（§3.3）及 `CLM-rabinowitch-2007-contingency-of-dictatorship`。

#### 07-03｜P1｜将站内 `DATA-04` 与 `ORG-left-communists-1918` 已考证清晰的七大票数版本差异误标为“冲突待核”，且漏挂全链条投票硬数据
- **定位**：[`POL-brest-litovsk-treaty.md:25-26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L25-L26)、[`L38`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L38)。
- **核证**：
  - L38 写：“Daniels札记记七大28比9，Rabinowitch札记列30比12、4弃权；两者记录及表决口径有冲突，不能拼接，待核原始速记再判。”
  - 实查站内 [`data/DATA-04-party-membership-and-congress-votes-1903-1929.md#L49`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-04-party-membership-and-congress-votes-1903-1929.md#L49) 与 [`cards/organizations/ORG-left-communists-1918.md#L26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-left-communists-1918.md#L26)（及 `L51-52`），**两套票数的史料来源差异在站内早已考证清楚**：
    - **`28 : 9 : 1`**（Daniels 1960 `p. 80 & p. 482 fn. 52`，简记 `28:9`）：取自 **1923 年版**俄共七大速记记录（*Sedmoi s'ezd RKP*, p. 139）的**当场初计口头/举手表决数**；
    - **`30 : 12 : 4`**（Rabinowitch 2007 `p. 198`）：取自 **1962 年莫斯科扩充校订版**七大速记记录计入**书面补投选票后的最终唱名表决数**。
  - 同时，本卡漏挂 `DATA-04`，并漏掉构成决策转折链的 4 个站内可核关键投票节点：`1918-01-08 [O.S.] / 01-21 [N.S.]` 63 人扩大会议（革命战争 32 : 不战不和 16 : 立即签和 15）、`1918-02-18/19` 夜间中央表决（**`7:5:1`**，托洛茨基转投赞成，可与 `02-23` 改投弃权的 `7:4:4` 对照）、`1918-02-23/24` 全俄中执委表决（**`116:85:26`**）以及 `1918-03-14..16` 第四次全俄苏维埃非常代表大会批准表决（**`784:261:115`**）。
- **修复**：在 §2.1 补齐上述投票链并挂接 `DATA-04`；在 `[T3]` 直接写出 1923 年初版速记（`28:9:1`）vs 1962 年修订版速记（`30:12:4`）的口径分叉，消除“待核”误判。

#### 07-04｜P1｜跨改历临界日 `1918年2月10日` 漏标旧历、`related_debates` 偏离主争鸣、§2.2 边表过瘦且未利用 Carr 第三卷布列斯特正文
- **定位**：[`POL-brest-litovsk-treaty.md:15`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L15)、[`L24`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L24)、[`L27-34`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L27-L34)、[`L47`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L47)。
- **核证**：
  1. **跨改历临界日漏标旧历**：L24 写托洛茨基“于1918年2月10日宣布‘不战不和’”。苏俄于 `1918-01-31 [O.S.]` 次日直接跳至 `1918-02-14 [N.S.]`，`1918-02-10` 尚在改历前 4 天，必须按规范双标为 **`1918-01-28 [O.S.] / 1918-02-10 [N.S.]`**，避免与不存在的“俄历 1918 年 2 月 10 日”混淆。
  2. **`related_debates` 漏挂主争鸣**：YAML L15 仅列 `DEB-1918-red-terror-and-civil-war-origins`，漏挂 `EVT-1918-03-brest-litovsk-treaty`、`CLM-daniels-1960-left-communists-1918` 与 `graph/edges.jsonl` 共同指向的主争鸣 **`DEB-1918-war-communism-ideology-or-emergency`**（和约“喘息时机”＋国家资本主义论战正是其起点）。
  3. **§2.2 边表仅 5 行（vs. 图谱 15 条边）**：漏挂 **`ORG-left-srs`**（联合政府破裂主角）、**`ORG-left-communists-1918`**（党内头号反对派）、**`CON-state-capitalism`**（和约后列宁经济路线）、**`EVT-1918-1920-russian-civil-war`**、**`MTG-1917-10-2nd-congress-of-soviets`**（《和平法令》源头）与 **`PER-dzerzhinsky`**。
  4. **L47 仅挂未读 `toc.md`**：站内 [`sources/monographs/carr_bolshevik_rev_v3_zh/ch03_第五部分_苏俄与世界_part_1.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/carr_bolshevik_rev_v3_zh/ch03_%E7%AC%AC%E4%BA%94%E9%83%A8%E5%88%86_%E8%8B%8F%E4%BF%84%E4%B8%8E%E4%B8%96%E7%95%8C_part_1.md) 与 `ch04_part_2.md` 合计出现 83 处布列斯特外交与条款论述，后续精读可先据此补核 Carr 外交史视角，不宜在 §3.3 长期以目录页充当证据入口。
- **修复**：补双历 `1918-01-28 [O.S.] / 1918-02-10 [N.S.]`；补挂 `DEB-1918-war-communism-ideology-or-emergency` 与 §2.2 缺失核心枢纽；明确将 Carr 第三卷 `ch03`–`ch04` 记为待精读专章而非直接用 `toc.md` 充证据。

#### 07-05｜P2｜YAML `aliases` 为空、T3 跳号与边表缺列
- **定位**：[`POL-brest-litovsk-treaty.md:8`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L8)、[`L40`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md#L40)。
- **核证**：YAML `aliases: []` 缺“不战不和 / 喘息时机（передышка）/ 布列斯特和约”等核心检索别名；T3 跳号 `### 3.3`、§2.2 缺第 5 列。
- **修复**：补齐 `aliases` 并统一修补 T3 层级与边表列数。

---

## 六、全批（01–07）P0/P1/P2 统计与汇总修复动作矩阵

### 6.1 分卡分级统计总表

| 序号 | 卡片 ID | 类型 | P0 | P1 | P2 | 核心问题一句话定性 |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | [`CON-narodnichestvo`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-narodnichestvo.md) | concept | **1** | 2 | 1 | **P0 倒置狭义／广义民粹主义定义并曲解 Walicki 原旨**；漏挂 4 份原典、Berlin 与 Hildermeier `CLM-*` |
| 02 | [`CON-smychka`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-smychka.md) | concept | 0 | 3 | 1 | **误将站内斯大林 1929-04-22 生产性结合原典标为缺口**；漏挂 Wave 39 列宁绝笔与泽姆斯科夫、`DATA-02`、Lewin |
| 03 | [`CON-soviet`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-soviet.md) | concept | 0 | 2 | 1 | 1922–1929 时域正文断档（漏 5:1 不等权、剥权者与“活跃苏维埃”）；漏挂彼得罗巴甫洛夫斯克原典、`DATA-01`/`DATA-07`；淡化 Avrich 证伪 |
| 04 | [`INS-rkka-red-army-and-rvr`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-rkka-red-army-and-rvr.md) | organization | 0 | 2 | 1 | （56.2 万标待核经全库复核合规）Mawdsley/Deutscher/Service 零 `CLM-*` 落地；1925–1929 伏罗希洛夫期断档、漏引 `DATA-05` |
| 05 | [`INS-vsnkh-and-gosplan`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md) | organization | 0 | 3 | 1 | （拉特科夫斯基署名考辨准确）**误将站内 Carr 第二卷已明晰的 ВСНХ 成立三重日期标为悬案**；4 家学者零 `CLM-*` 落地、漏列宁 1922-12 原典与 `DATA-02`/`DATA-03` |
| 06 | [`POL-ban-on-factions-1921`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-ban-on-factions-1921.md) | policy | 0 | 2 | 1 | （秘密第 7 条条文与程序 100% 精准）漏挂 `DATA-04`、`1926-07-23` 首次动用第 7 条逐季诺维也夫节点、反对派原典与 Goldman 卡；边表漏 `PER-lenin` |
| 07 | [`POL-brest-litovsk-treaty`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-brest-litovsk-treaty.md) | policy | **2** | 2 | 1 | **P0 将 1918《论“左派”幼稚性和小资产阶级性》误作 1920《左派幼稚病》**；**P0 错配零命中札记 `RN-W12B`**；误将站内已考清的七大两套票数标为待核；`1918-02-10` 漏标俄历 |
| **合计** | **7 张枢纽卡** | — | **3** | **16** | **7** | **共计 26 项审计发现（P0 集中在 01、07 两张卡；全批无断链／无悬空 ID）** |

### 6.2 跨模型系统性特征诊断（与 `AUD-18A`/`AUD-18B` 纵向对比）

1. **显著进步项（相较 Wave 39–40）**：
   - 7 张卡机械卫生优秀（0 断链、0 悬空 ID、`[T1]` 全部严控在 112–121 字）；
   - 俄文作者／档案编者署名失误大幅收敛（`INS-vsnkh-and-gosplan` 主动纠正拉特科夫斯基 vs 普列汉诺夫署名，未将 Davies 论文集主编当作者；`INS-rkka` 对全库无出处的“56.2 万”未硬编出处；`POL-ban-on-factions-1921` 对秘密第 7 条程序逐字忠实于原典）。
2. **尚未根除的 4 类结构性顽疾**：
   - **顽疾 A（未精读所引文件正文而凭印象概括／挂链）**：导致 `CON-narodnichestvo` 把 Walicki 反驳 Pipes、辩护列宁广义定义的论点完全说反（P0）；导致 `POL-brest-litovsk-treaty` 把 1918 篇名混成 1920《左派幼稚病》（P0）并盲挂零命中的 `RN-W12B`（P0）。
   - **顽疾 B（“伪审慎”——未检索站内已入库专著／数据卡／原典，误把站内已可核事实推作“待核查”或 `perspectives_missing`）**：集中出现在 3 处——`CON-smychka`（斯大林 1929-04-22 生产性结合全本在库）、`INS-vsnkh-and-gosplan`（Carr 第二卷已析清 12-01/12-02/12-05 O.S. 三节点）、`POL-brest-litovsk-treaty`（`DATA-04` 与 `ORG-left-communists-1918` 已考清七大 `28:9:1` vs `30:12:4` 速记版本源流）。
   - **顽疾 C（全批系统性遗漏 `data/DATA-01..08` 与 Wave 39 新增馆藏，且“挂名学者”零 `CLM-*` 落地）**：7 张卡几乎集体绕开 `DATA-01`、`DATA-02`、`DATA-04`、`DATA-05`、`DATA-07` 与 Wave 39 列宁绝笔／泽姆斯科夫卡，且多卡在 `perspectives_present` 与 §2.3 点名 3–4 位学者却在 §3.3 零 `CLM-*` 支撑。
   - **顽疾 D（§2.2 边表过瘦＋全批模板微瑕）**：7 张卡在 `graph/edges.jsonl` 共有 9–19 条既有关系，但 §2.2 仅写 4–6 行，屡屡漏掉 `PER-lenin` 等头号主角；且 7 张卡 100% 统一在 `## [T3]` 下跳号至 `### 3.3` 并省略 §2.2 第 5 列。

### 6.3 汇总修复动作矩阵（按 P0 → P1 → P2 优先序执行）

| 优先级 | 编号 | 目标卡片 | 具体修复动作（精确到字段／段落／挂接文件） |
| :---: | :---: | :--- | :--- |
| **P0** | `01-01` | `CON-narodnichestvo` | 重写 `[T1]`、L27、L35、L38、L40：正位 Pipes（1964）1870s 反智主义“狭义历史义” vs 列宁“广义社会学义” vs Walicki（1969）对列宁广义定义的方法论辩护与 1869 断代，消除与 `CLM-walicki-1969-narodnichestvo-definition` 反向冲突 |
| **P0** | `07-01` | `POL-brest-litovsk-treaty` | 将 L38“列宁《左派幼稚病》”更正为《论“左派”幼稚性和小资产阶级性》（1918 年 5 月），并注明勿与 1920 年《共产主义运动中的“左派”幼稚病》混同 |
| **P0** | `07-02` | `POL-brest-litovsk-treaty` | 删除 L44 错配的 `RN-W12B` 及 L36 空泛评语；改挂真正含布列斯特专节的 `RN-W22`（§3.3 捷尔任斯基弃权证言）与 `CLM-rabinowitch-2007-contingency-of-dictatorship` |
| **P1** | `02-01` | `CON-smychka` | 从 `perspectives_missing` 移除 `"production-smychka-primary-wording"`；L27 与 §3.3 锚定 `1929-04-22_right-deviation-in-cpsu.md`（L617–686/L1789–1845）并与布哈林 `1929-04-18` 四月全会演说对读 |
| **P1** | `05-01` | `INS-vsnkh-and-gosplan` | 依据 `carr_bolshevik_rev_v2_zh/ch04_part_2.md#L314-L318`（`[PDF p. 36]`）改写 L25/L41，拆明 12-01 O.S. 草案通过／12-02 O.S. 签署／12-05 O.S. 公布三节点，收窄 `perspectives_missing` |
| **P1** | `07-03` | `POL-brest-litovsk-treaty` | 依据 `DATA-04`（L49）与 `ORG-left-communists-1918` 改写 L38，写明七大 1923 年版速记（`28:9:1`）vs 1962 年扩充版（`30:12:4`）版本来源；补挂 `DATA-04` 与 `01-21`/`02-18`/`02-23`/`03-14..16` 投票链 |
| **P1** | `07-04` | `POL-brest-litovsk-treaty` | L24 补双历 `1918-01-28 [O.S.] / 1918-02-10 [N.S.]`；YAML 补 `DEB-1918-war-communism-ideology-or-emergency`；§2.2 补 `ORG-left-srs`、`ORG-left-communists-1918`、`CON-state-capitalism`、`EVT-1918-1920-russian-civil-war`、`MTG-1917-10-2nd-congress-of-soviets`、`PER-dzerzhinsky`；将 L47 `toc.md` 标为待精读专章（`ch03`–`ch04`） |
| **P1** | `02-02` | `CON-smychka` | 补挂 Wave 39 列宁《宁肯少些，但要好些》（换马隐喻）与 `CLM-zemskov-2018-agrarian-tribute-and-coercive-turn`、`DATA-02`、`CLM-carr-1954-scissors-crisis-mechanics`、`CLM-lewin-1968-cooperation-shift` 及 3 份 S 级原典（`prodnalog`、`on-the-grain-front`、`notes-of-an-economist`） |
| **P1** | `03-01` | `CON-soviet` | §2.1 补齐 1918 宪法第 25/65 条（5:1 不等权与剥权者）及 1924–1927“活跃苏维埃”；§3.3 补挂彼得罗巴甫洛夫斯克决议、1905 财政宣言、1918 权利宣言、`DATA-01`/`DATA-07`、Carr 1950 与 Kubi（标 B 级）论断卡及姚海卡 |
| **P1** | `04-02` | `INS-rkka-red-army-and-rvr` | §2.1 补齐 1925–1929 伏罗希洛夫掌军、地域师政治忧虑与 1928 工农化；以 `DATA-05` 核实序列（兵力、4.8 万旧军官、21.5 万军士、16 万党团员、170 万逃兵）校准“约 500 万”；§2.2 补 `EVT-1918-1920-russian-civil-war`、`PER-voroshilov`、`PER-tukhachevsky`、`PER-stalin`、`POL-first-five-year-plan` |
| **P1** | `06-01` | `POL-ban-on-factions-1921` | §2.1 补写 `1926-07-23` 首次动用第 7 条逐季诺维也夫出政治局节点；§3.3 补挂 `DATA-04`、柯伦泰 S 级卡、46 人声明与 Carr 1954 卡、托洛茨基《新方针》、1927 联合反对派纲领及 `CLM-goldman-2011-1920s-oppositions-to-enemy-category`；YAML 补 `DEB-1928-bukharin-alternative` |
| **P1** | `01-02`, `03-02`, `04-01`, `05-02` | `CON-narodnichestvo`、`CON-soviet`、`INS-rkka`、`INS-vsnkh` | 消除全部“挂名学者零 `CLM-*` 落地”：分别补挂 Berlin/Hildermeier 及 4 份马克思—查苏利奇原典（01）；Avrich 证伪原旨及 Sukhanov/Hasegawa/Rabinowitch `CLM-*`（03）；Mawdsley/Deutscher/Service/Stalin-docs/Shlapentokh `CLM-*`（04）；Smith/Erlich/Katasonov/Carr 1952–54/Zhukov/Davies 1980 `CLM-*`、列宁 1922-12 原典与 `DATA-02`/`DATA-03`（05） |
| **P1** | `01-03`, `02-03`, `05-03`, `06-02` | `CON-narodnichestvo`、`CON-smychka`、`INS-vsnkh`、`POL-ban-on-factions-1921` | 扩充 4 张卡过瘦的 §2.2 边表（特别补齐 02/05/06 共同遗漏的 `PER-lenin` 及各卡核心事件／组织节点）；02 的 `related_debates` 补 `DEB-1929-collectivization-and-dekulakization-causes`；05 正文具名呈现 Gatrell / Rees / Hunter |
| **P2** | `01-04`..`07-05`（全 7 卡） | 全批 7 张卡 | ① 全批统一修正 T3 标题跳号（去掉悬空 `### 3.3` 或补齐 `3.1`/`3.2`）并补全 §2.2 第 5 列“核心依据/争鸣”；② 清理错误或重复锚文本（01 两份 Walicki 札记区分、02 补 Carr 合著者与 Erlich 具名、05 L51 改为涅姆奇诺夫表批判）；③ 精准细节修正（03 补 `1918-06-14`、04 补 `1918-09-02` 与 `РВС СССР` 并将 56.2 万按语下沉 `[T3]`、06 改“不同于 1924 年 5 月十三大”并补 `aliases`、07 补 `aliases`） |

