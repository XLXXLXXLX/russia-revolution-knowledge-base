# AUD-18A｜第39波 Codex 升格 `DEB-*` 史学争鸣卡异源交叉审计报告（首批 6 张，1903—1918）

- **审计日期**：2026-11-19
- **审计角色**：`dialectic-auditor`（跨模型家族异源交叉审计：Google `gemini-4-neon` 审读 OpenAI `gpt-6.1-terra` 在 Wave 39 升格的 6 张 `DEB-*` 史学争鸣卡）。
- **唯一写入目标**：[`audits/AUD-18A-wave39-codex-deb-batch1-audit.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-18A-wave39-codex-deb-batch1-audit.md)；纯只读审计，未改动任何被审争鸣卡、实体卡、论断卡、札记或共享图谱文件。
- **审计对象（两阶段增量落盘）**：
  - **阶段一（01–03，本节已完成）**：
    1. [`DEB-1903-bolshevik-menshevik-split`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1903-bolshevik-menshevik-split.md)
    2. [`DEB-1914-haimson-thesis-stability`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md)
    3. [`DEB-1917-dual-power-and-february-origins`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md)
  - **阶段二（04–06 与全批汇总修复矩阵，本节已完成）**：
    4. [`DEB-1917-july-days-spontaneity-vs-conspiracy`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-july-days-spontaneity-vs-conspiracy.md)
    5. [`DEB-1917-october-coup-or-social-revolution`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md)
    6. [`DEB-1918-red-terror-and-civil-war-origins`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md)

---

## 一、审计方法、判级准则与全 6 卡机械体检基线

1. **判级准则**（沿用 [`AUD-16A`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-16A-wave32-33-codex-ins-mtg-pol-audit.md) 标准）：
   - **P0**：史实／双历换算硬伤、断链／悬空节点 ID、张冠李戴（学者姓名错写／主编误作作者／错挂无关 `CLM-*`）、无中生有歪曲学者原文立场；
   - **P1**：站内已有 S/A 级原典、统计数据卡、精读札记或核心实体卡漏引、把站内已可核事项笼统归入“外部待补核缺口”、学派矩阵失衡（遗漏关键对立学派或把核心交锋抹平）、将经验共识与价值／反事实判断混为一谈；
   - **P2**：Schema 字段细节、`[T1]` 字数或措辞／时间边界微瑕。
2. **核验手段**：
   - (a) 只读 Python 脚本全量扫描 6 张卡的 YAML 字段、`core_cards`、`[T1]` 字数（模板上限 `<= 150` 字）、全部反引号节点 ID 与 `.md` 相对路径；
   - (b) 调用 `python scripts/kb.py date <DATE> --from os` 逐项复算双历；
   - (c) **逐一打开每一张被引用及站内同主题未被引用的 `CLM-*`、`RN-*`、`sources/web-archive/*`、`data/DATA-*` 与新建 `EVT-*` 卡对读**。

### 1.1 全 6 张 `DEB-*` 卡机械体检总表（只读 Python 脚本实测）

| 序号 | 卡片 ID | YAML 必填键 | `core_cards` 命中/断链 | `[T1]` 字数（≤150） | 正文反引号 ID 命中/断链 | T3 `.md` 路径命中/断链 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| 01 | `DEB-1903-bolshevik-menshevik-split` | 齐全 | 8 / 0 | 113（合格） | 11 / 0 | 7 / 0 |
| 02 | `DEB-1914-haimson-thesis-stability` | 齐全 | 7 / 0 | 114（合格） | 11 / 0 | 5 / 0 |
| 03 | `DEB-1917-dual-power-and-february-origins` | 齐全 | 5 / 0 | 112（合格） | 10 / 0 | 6 / 0 |
| 04 | `DEB-1917-july-days-spontaneity-vs-conspiracy` | 齐全 | 8 / 0 | 115（合格） | 9 / 0 | 9 / 0 |
| 05 | `DEB-1917-october-coup-or-social-revolution` | 齐全 | 6 / 0 | 111（合格） | 13 / 0 | 5 / 0 |
| 06 | `DEB-1918-red-terror-and-civil-war-origins` | 齐全 | 6 / 0 | 111（合格） | 12 / 0 | 7 / 0 |

> **机械体检结论**：6 张卡**无任何断链 ID、无任何断链 `.md` 路径、`[T1]` 字数全部严格控制在 111–115 字之间**；但逐一打开所引 `CLM-*` 原文对读后，**全批 6 张卡共检出 7 处 P0 级学者名／作者归属／论断卡张冠李戴（分布于 5 张卡，仅 04 号卡为 0 P0）、12 处 P1 与 6 处 P2**（核心病灶高度集中于仅据文件名推断作者与时域，未逐一核读论断卡正文）。

---

## 二、阶段一（01–03）双历法与日期复核表

| 卡片 | 卡内日期（YAML／正文） | `kb.py` 复算与规则核查 | 判定 |
| :--- | :--- | :--- | :--- |
| 01 `DEB-1903-bolshevik-menshevik-split` | YAML：`start_ns: 1903-07-30`、`end_ns: 1903-08-23`（注释明示布鲁塞尔与伦敦会场采用当地公历）；`era: 1902-1904` | `1903-07-17 O.S.` → `07-30 N.S.`；`1903-08-10 O.S.` → `08-23 N.S.`（+13）✓；西欧会场用公历符合 `AGENTS.md` 规范 | **历法合规**；正文可补注俄历对照（P2） |
| 02 `DEB-1914-haimson-thesis-stability` | YAML：`1907-06-03 O.S. / 1907-06-16 N.S.` 至 `1914-07-18 O.S. / 1914-07-31 N.S.`；正文：`1912-04-04 O.S. / 1912-04-17 N.S.` | `06-03` → `06-16` ✓；`07-18` → `07-31` ✓；`04-04` → `04-17` ✓（均 +13） | **换算无误**；终点 `07-18 O.S.`（俄国总动员/战前夕）与新建 `EVT-1907-1914` 终点 `07-19 O.S. / 08-01 N.S.`（德国宣战）差 1 日，宜注释说明（P2） |
| 03 `DEB-1917-dual-power-and-february-origins` | YAML：`1917-02-23 O.S. / 03-08 N.S.` 至 `1917-03-03 O.S. / 03-16 N.S.`；正文：`02-27 / 03-12`、`03-01 / 03-14`、`03-02 / 03-15` | 全部 5 组日期 +13 复算全中 ✓ | **换算无误**；正文经验基准止于 3 月 2 日尼古拉二世退位，未交代 `end_os: 03-03` 对应的米哈伊尔大公拒位与临时政府首次内阁会议（P1/P2） |

---

## 三、阶段一逐卡深度审计与修复方案（01–03）

### 01｜《怎么办？》与1903年布尔什维克—孟什维克分裂实质之争（`DEB-1903-bolshevik-menshevik-split`）

**总体评价**：结构清楚，能明确区分“文本论战、表决序列与事后政治后果”，并准确把握布鲁塞尔—伦敦西欧公历规范。但存在 **1 项严重 P0 学者张冠李戴**（将 Robert Mayer 误写为 Arno Mayer、将主编 Reginald Zelnik 误作 Steve A. Smith 论文作者），以及学派矩阵偏向修正派一侧、漏引站内 1906 年斯德哥尔摩党章反证等 P1 问题。

#### 01-01｜P0｜学者姓名与作者归属双重张冠李戴：`Arno Mayer` 实为 `Robert Mayer`；`Reginald Zelnik` 实为主编而非该论断卡作者
- **定位**：[`DEB-1903-bolshevik-menshevik-split.md:29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1903-bolshevik-menshevik-split.md#L29)（矩阵第 5 行：“`Reginald Zelnik 与 Arno Mayer 的研究`”挂靠 `CLM-zelnik-1999-worker-intelligentsia-tutelage-tension` 与 `CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism`）。
- **核证**：
  1. 查阅 [`CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-mayer-1999-lenin-jacobin-metaphor-vs-blanquism.md#L4-L6)，该文作者为 **`Robert Mayer`**（`SCH-mayer-robert`，*"Lenin and the Jacobin Identity in Russia"*, *Studies in East European Thought*, 1999），绝非撰写《复仇女神》（*The Furies*）的著名比较革命史家 **`Arno Mayer`**（Arno J. Mayer）。此系典型模型幻觉导致的学者身份混淆。
  2. 查阅 [`CLM-zelnik-1999-worker-intelligentsia-tutelage-tension.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-zelnik-1999-worker-intelligentsia-tutelage-tension.md#L4-L6)，其 `scholar` 明确为 **`SCH-smith-steve`**（Steve A. Smith, *"Workers, the Intelligentsia and Marxist Parties: St Petersburg, 1895-1917 and Shanghai, 1921-1927"*, 1996；收入 **Reginald E. Zelnik, ed.**, *Workers and Intelligentsia in Late Imperial Russia*, 1999）。卡片仅凭文件名前缀 `CLM-zelnik-1999-...` 将论文集主编当作该论断卡作者，漏写了真正作者 Steve A. Smith（同书另张卡 [`CLM-zelnik-1999-kanatchikov-conscious-worker-formation.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-zelnik-1999-kanatchikov-conscious-worker-formation.md#L4-L6) 同样由 `SCH-smith-steve` 撰写，依托 Zelnik 译注的卡纳奇科夫自传）。
- **修复**：将第 5 行“代表学者与著作”改为 `S. A. Smith (1996/1999，收入 Reginald E. Zelnik 编论文集)；Robert Mayer (1999)`，并核准摘要：Robert Mayer 考证列宁的“雅各宾”自称直接承袭普列汉诺夫 1901 年的法国大革命修辞而非特卡乔夫布朗基传统；Smith 揭示 1895–1917 彼得堡工人与知识分子间的反监护张力。

#### 01-02｜P1｜`[T2]` 矩阵学派失衡：缺失与 Lih／Robert Mayer 直接交锋的冷战“雅各宾—特卡乔夫连续论”与当事人／苏联正统栏位
- **定位**：[`L12`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1903-bolshevik-menshevik-split.md#L12)、[`L23-29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1903-bolshevik-menshevik-split.md#L23-L29)、[`L32`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1903-bolshevik-menshevik-split.md#L32)。
- **核证**：
  1. `[T2]` 矩阵 5 行全部集中在 Haimson、Lih、Getzler、Blanc、Smith/Robert Mayer 等精细思想史／修正派／劳工史一侧，**完全没有给“雅各宾—特卡乔夫—列宁极权连续论”设立矩阵栏位**——而站内恰恰已有 A 级论断卡 [`CLM-jacobin-ancestry-tkachev-blanqui-and-leninism.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-jacobin-ancestry-tkachev-blanqui-and-leninism.md)（William Henry Chamberlin 1958，援引 Karpovich 与 Talmon 论证雅各宾→特卡乔夫→列宁谱系）及 [`CLM-pipes-1990-patrimonial-state-and-intelligentsia.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-pipes-1990-patrimonial-state-and-intelligentsia.md)（职业革命家知识分子论）。没有这一栏，Lih 批判的“教科书神话”和 Robert Mayer 反驳的“俄国雅各宾传统”在矩阵里形同对着空气靶开火。
  2. YAML `perspectives_present` 声明含 `"participant"`，但 `[T2]` 矩阵并无托洛茨基 1904《我们的政治任务》（“替代主义”批判）或列宁 1904《进一步，退两步》的对应栏位；同时，Lih [`CLM-lih-2006-textbook-myth-critique.md:27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-lih-2006-textbook-myth-critique.md#L27) 专门揭示了一个重要史学反讽——1938 年斯大林《简明教程》实际上**并未**把《怎么办？》称为“新型政党”起点（该称号归于 1912 年布拉格会议），而是按考茨基“结合公式”解读《怎么办？》；T3 L32 笼统将“苏联正统将分裂追认为正确建党的起点”一笔带过，忽略了站内 A 级文献已揭示的内部层次。
- **修复**：在 `[T2]` 增设“冷战自由派／雅各宾连续论”一行（William Henry Chamberlin 1958、Richard Pipes 1990，挂靠 `CLM-jacobin-ancestry-tkachev-blanqui-and-leninism`、`CLM-pipes-1990-patrimonial-state-and-intelligentsia`），并在 T3 简述《简明教程》1912 vs 1902 的分界与 1904 年当事人论战定位。

#### 01-03｜P1｜漏引站内 S 级最强反证原典（1906 斯德哥尔摩党章）、多篇 A 级札记、已核票数及新建事件卡
- **定位**：[`L10`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1903-bolshevik-menshevik-split.md#L10)、[`L21`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1903-bolshevik-menshevik-split.md#L21)、[`L34`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1903-bolshevik-menshevik-split.md#L34)、[`L36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1903-bolshevik-menshevik-split.md#L36)。
- **核证**：
  1. **漏引站内 S 级反证原典**：[`sources/web-archive/E03_E08_party_and_state_docs/1906-04_rsdlp-fourth-stockholm-congress-rules.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E03_E08_party_and_state_docs/1906-04_rsdlp-fourth-stockholm-congress-rules.md)（1906 年四大在孟什维克 62:46 占多数的条件下，**党章第 1 条直接改回了列宁 1903 年的“参加党的一个组织”公式**！这是站内检验“1903 年第 1 条是否构成永久意识形态鸿沟”的最硬反证，完全未引）。
  2. **漏引站内 A 级札记**：矩阵第 5 行所依托的 [`reading-notes/mayer_zelnik/RN-W22-lenin-jacobin-myth-and-worker-intelligentsia-relations.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/mayer_zelnik/RN-W22-lenin-jacobin-myth-and-worker-intelligentsia-relations.md) 未列入 T3 锚点；同主题的 [`reading-notes/jacobin_ancestry_soviet_communism/RN-W36-jacobin-ancestry-of-soviet-communism.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/jacobin_ancestry_soviet_communism/RN-W36-jacobin-ancestry-of-soviet-communism.md)、[`reading-notes/smith_sa_1996_irsh/RN-W32-smith-petersburg-workers-intelligentsia-and-marxist-parties-1895-1917.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/smith_sa_1996_irsh/RN-W32-smith-petersburg-workers-intelligentsia-and-marxist-parties-1895-1917.md) 与 [`CLM-haimson-1987-menshevik-party-ethos-and-family`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-haimson-1987-menshevik-party-ethos-and-family.md) 亦未纳入。
  3. **已核票数闲置与外部缺口界定偏宽**：[`1903-08-02_rsdlp-rules-paragraph-1.md:63-78`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E02_E07_foundational_docs/1903-08-02_rsdlp-rules-paragraph-1.md#L63-L78) 已完整录出第 23 次会议全部 51 票唱名名单（列宁案 `23:28` 败、马尔托夫案 `28:22:1` 胜、整条 `35:1:12`），[`MTG-1903-rsdlp-2nd-congress.md:53-58`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1903-rsdlp-2nd-congress.md#L53-L58) 已汇总《记录》与 Haimson 关于崩得退场（5 票 vs 4 票）及三人编委（`25:2:20` vs `22:20:2`）的两套口径。本卡 L21 经验基准未给出任何票数，且 L36 泛称“逐次代表资格与退出名单”为外部缺口，未区分第 23 次会议唱名已入库、待补者系全大会其余场次速记与中央选举完整票册。
  4. **`core_cards` 互链增补机会**：新建事件卡 [`EVT-1891-1903-witte-industrialization-and-marxist-labor-turn`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1891-1903-witte-industrialization-and-marxist-labor-turn.md)（已双向指向 `DEB-1903`）以及 [`MTG-1906-04-rsdlp-4th-stockholm-congress`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1906-04-rsdlp-4th-stockholm-congress.md)、[`ORG-bund`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-bund.md) 建议补入 `core_cards`。
- **修复**：T2 经验基准补入关键票数与口径差异；T3 锚点补入 `1906-04_rsdlp-fourth-stockholm-congress-rules.md` 与 `RN-W22`、`RN-W36`；收窄外部缺口表述；`core_cards` 增补上述 3 节点。

#### 01-04｜P2｜元数据与细节微瑕
- `dates` 仅标二大公历会期（`1903-07-30` 至 `1903-08-23`），建议在 L21 经验基准附注俄历对照（`1903-07-17` 至 `08-10 [O.S.]`）并说明 `era: "1902-1904"` 覆盖《怎么办？》至 1904 年派别论战；`perspectives_present` 中的 `"participant"` 宜在 `[T2]` 有对应依托或改注于 T3。

---

### 02｜海姆森命题：战前俄国的社会稳定与双重极化（`DEB-1914-haimson-thesis-stability`）

**总体评价**：核心问题界定敏锐（明确区分“可观察的危机”与“无法验证的无战争反事实”，且在 Gaida 栏自觉提醒进步集团属战时材料、不可倒灌战前）。但存在 **2 项严重 P0 硬伤**（Gaida 错名 + 将范围仅止于 1901/1903 年的洛吉诺夫早期列宁传记论断卡错挂入 Steinberg/Hoffmann 的“连续危机与战争治理”栏），同时漏用了站内已有的海姆森 2005 专著、霍根金属工人研究及 `DATA-01`/`DATA-07` 统计基线。

#### 02-01｜P0｜学者名张冠李戴：`Dmitrii Gaida (2003)` 实为 `Fedor Gaida`（Фёдор Александрович Гайда）
- **定位**：[`DEB-1914-haimson-thesis-stability.md:29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md#L29)。
- **核证**：查阅 [`CLM-gaida-2003-progressive-bloc-dilemma.md:4`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-gaida-2003-progressive-bloc-dilemma.md#L4)，`scholar` 为 **`SCH-gaida-fedor`**（俄罗斯历史学家费奥多尔·亚历山德罗维奇·盖达，Fedor / Fyodor A. Gaida）。写成 `Dmitrii Gaida` 属无中生有的姓名硬伤。
- **修复**：更正为 `Fedor Gaida (2003)`（费奥多尔·盖达）。

#### 02-02｜P0｜严重错挂无关论断卡：`CLM-lenin-leader-organizational-ascendancy-pre1914` 实为洛吉诺夫 1870–1901 年早期列宁传记，与“连续危机与战争治理”及 1907–1914 均无关
- **定位**：[`DEB-1914-haimson-thesis-stability.md:30`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md#L30)（第 5 行“代表学者”仅列 `Mark Steinberg (2017); David Hoffmann (2011)`，但“支撑论断卡”挂了 4 张卡，含 `CLM-lenin-leader-organizational-ascendancy-pre1914` 与 `CLM-yao-hai-1917-modernization-rupture-and-plebeian-radicalism`）。
- **核证**：
  1. 查阅 [`CLM-lenin-leader-organizational-ascendancy-pre1914.md:4,9,22`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-lenin-leader-organizational-ascendancy-pre1914.md#L4-L22)，该卡作者为 **Vladlen T. Loginov**（2005，《弗拉基米尔·列宁：如何成为领袖》），且第 9 行与第 22 行以粗体明示**【文献覆盖边界声明】**：*“全书实证叙事覆及 **1870–1901 年春**（终章仅附 1903 年 2 月巴黎讲座），**并未涉及 1903–1914 年的党内分裂与布拉格建党**”*。将其塞入 `Steinberg / Hoffmann` 的“连续危机与战争治理（1905–1929）”栏，既是作者张冠李戴，又是时域完全错配（显然仅望文生义读了文件名 `pre1914`）。
  2. 同行还静默塞入了 [`CLM-yao-hai-1917-modernization-rupture-and-plebeian-radicalism.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-yao-hai-1917-modernization-rupture-and-plebeian-radicalism.md)（作者：**姚海 Yao Hai**，2013，社科院《俄国革命史》），未在“代表学者与著作”栏署名，也未在 T3 列出其精读札记 [`RN-W36-yao-hai-cass-russian-revolution-synthesis.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/yao_hai_ussr_history_v1_russian_rev_zh/RN-W36-yao-hai-cass-russian-revolution-synthesis.md)。姚海该卡第 2 点确涉 1905–1914 改革窗口关闭与现代化断裂，具备相关性，但不应匿名混挂在 Steinberg/Hoffmann 名下。
- **修复**：彻底移除 `CLM-lenin-leader-organizational-ascendancy-pre1914`；将姚海单列或在对应栏显式署名并补挂 `RN-W36`。

#### 02-03｜P1｜核心学者立场失焦／漏用站内海姆森 2005 原著：Bonnell 对海姆森的关键修正被抹平，Pipes 反必然论与“乐观现代化派”对立极偏弱
- **定位**：[`L26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md#L26)、[`L27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md#L27)、[`L29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md#L29)、[`L35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md#L35)、[`L37`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md#L37)。
- **核证**：
  1. **漏用站内海姆森 2005 晚年专著**：L26 给 Haimson 行只借挂了 Steinberg 的比较脉络卡，L37 称待补 1964–65 原文与后续回应——却完全忽视站内**已有**海姆森晚年代表作 *Russia's Revolutionary Experience, 1905–1917* (2005) 的完整精读札记 [`RN-W29-haimson-lenin-1917-leap-and-kollontai-workers-opposition.md` §1.3（L48–70）](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/haimson2005_kollontai1921/RN-W29-haimson-lenin-1917-leap-and-kollontai-workers-opposition.md#L48-L70)！该书 Part II（`ch09–ch13, ch16`）正是海姆森对 1912–1914 勒拿后罢工潮、“礼貌相待”（*vezhlivoe obrashchenie*）、“羞耻与致耻”、“平等与分离并重”（*equality and separateness*）的深度续作，**并在 Appendix II（`pp. 250–251`）亲自修正了自己 1964–65 年关于“农村新移民怨恨”的早期假说**！
  2. **Bonnell 与 Haimson 的核心学术交锋被抹平**：[`CLM-bonnell-1983-1912-1914-union-and-insurance-boards-bolshevik-capture.md:22,52`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-bonnell-1983-1912-1914-union-and-insurance-boards-bolshevik-capture.md#L22) 明确标为同时 `supports` 与 `qualifies` `DEB-1914`——她一方面以工会与保险局选举数据证实战前布尔什维克化（如 1913 年 8 月彼得堡金属工盟老会员多达 3/4 倒戈、1914 年 3 月全市保险委 35:12），另一方面**正面反驳**海姆森 1964 年与孟什维克同时代人的“年轻半农民新兵”论，证明激进化主力是**长期城市化、识字熟练工与手工业工匠**。本卡 L27 仅笼统写“影响两派工人吸引力和组织竞争”，丢失了这场核心交锋。
  3. **Pipes 立场缩水且“乐观派”缺席**：[`CLM-pipes-1990-patrimonial-state-and-intelligentsia.md:35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-pipes-1990-patrimonial-state-and-intelligentsia.md#L35) 直引 Pipes 的核心反必然论命题（*"Nothing in early-twentieth-century Russia inexorably pushed the country toward revolution, except the presence of an unusually large and fanatical body of professional revolutionaries"*），卡片却将 Pipes 缩水为一句“Pipes 强调专制遗产”；同时整张矩阵未单列与海姆森辩论的**战前“乐观派／经济演进论”**（Gerschenkron、Gregory 等，即便站内缺专著亦应在矩阵或 `perspectives_missing` 中显式标明，而非完全隐形）。
- **修复**：海姆森行补引 `RN-W29` §1.3 并注明 2005 年自我修正；Bonnell 行补写“验证激进化、反驳半农民新兵论”；Pipes 行补齐“非必然性／职业革命家驱动”论点；`perspectives_missing` 增补 `optimistic-modernization-economic-history`（并在矩阵或 T3 明确交代 Gerschenkron／Pipes 战前演进论一极）。

#### 02-04｜P1｜站内已有核心 A 级论断卡、统计数据卡与新建事件卡漏引，且部分可核数据被泛化为外部缺口
- **定位**：[`L11`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md#L11)、[`L35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md#L35)、[`L37`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md#L37)。
- **核证**：
  1. **漏引核心 A 级论断卡与札记**：
     - [`CLM-hogan-1994-petersburg-metalworkers-1905-to-lena.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-hogan-1994-petersburg-metalworkers-1905-to-lena.md)（Heather Hogan 1994，札记 [`RN-W32-making-workers-soviet-class-formation-and-1920s-unmaking.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/siegelbaum_suny_1994_making_workers_soviet_zh/RN-W32-making-workers-soviet-class-formation-and-1920s-unmaking.md)）——专论 1905–1912 彼得堡金属工人、失业者委员会对抗市杜马（“他们 vs 我们”）、工人选民团（*workers' curia*）与泰勒制如何将工人推向勒拿爆发，与海姆森命题高度直接相关，全卡零引用；
     - 矩阵第 5 行所引 Steinberg 与 Hoffmann 对应的站内札记 [`RN-W10-worker-militias-and-emotional-history-revolution.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/boll_steinberg/RN-W10-worker-militias-and-emotional-history-revolution.md) 与 [`RN-W17-modernity-biopolitics-and-official-anti-trotskyism.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/hoffmann_modernity/RN-W17-modernity-biopolitics-and-official-anti-trotskyism.md) 均漏列于 T3 锚点；
     - 涉及斯托雷平时代社革党瘫痪与农村侧的 [`CLM-hildermeier-2000-azev-affair-and-stolypin-era-paralysis.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-hildermeier-2000-azev-affair-and-stolypin-era-paralysis.md)（[`RN-W29-hildermeier-psr-azev-crisis-and-modernization-dilemma.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/hildermeier_psr_full/RN-W29-hildermeier-psr-azev-crisis-and-modernization-dilemma.md)）及 `CLM-service-lenin-v1-bogdanov-vpered-rupture-and-prague-1912` 亦未提及。
  2. **站内定量数据卡漏引**：站内已有 [`data/DATA-01-1905-1917-strikes-and-petrograd-elections.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-01-1905-1917-strikes-and-petrograd-elections.md)（工厂视察官 1905–1917 年度罢工序列：1910 年 4.66 万 → 1914 年上半年 133.7 万）与 [`data/DATA-07-1905-1918-unions-moscow-swings-and-constituent-assembly-votes.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-07-1905-1918-unions-moscow-swings-and-constituent-assembly-votes.md)（1914 年 6 月彼得堡 18 个工会理事会约 14.5 个由布尔什维克或其盟友控制）。T3 L37 将罢工登记与工会保险选举底册统统划入外部缺口，却未先锚定站内已编译的 `DATA-01`、`DATA-07` 与 `RN-W35` 选举数据。
  3. **`core_cards` 互链增补机会**：刚新建且与本争鸣直接绑定的 [`EVT-1907-1914-june-third-regime-and-lena-to-july-strikes`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1907-1914-june-third-regime-and-lena-to-july-strikes.md) 与 [`EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc.md)（两者均在 `related_debates` 挂接 `DEB-1914`）尚未回链至本卡 `core_cards`。
- **修复**：T2 增补 Hogan (1994) 论断卡；T3 锚点增补 `RN-W29`（Haimson 2005）、`RN-W32`（Hogan）、`RN-W10`、`RN-W17`、`DATA-01`、`DATA-07`，并将外部缺口收窄为“分省/分行业原始底册与 Haimson 1964–65《Slavic Review》原文全篇”；`core_cards` 补挂上述两张新建事件卡。

#### 02-05｜P2｜终点日期口径微差
- 本卡 `end_os: "1914-07-18" / end_ns: "1914-07-31"`（俄国总动员／宣战前夜）与 [`EVT-1907-1914`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1907-1914-june-third-regime-and-lena-to-july-strikes.md#L12-L13) 的 `1914-07-19 [O.S.] / 1914-08-01 [N.S.]`（德国对俄宣战日）相差 1 天，建议在 YAML 注释中标明取“总动员前夜”或与 `EVT-1907-1914` 对齐为 `07-19 O.S. / 08-01 N.S.`。

---

### 03｜二月革命起源与“双重政权”宪制形成之争（`DEB-1917-dual-power-and-february-origins`）

**总体评价**：双历换算全部精确；在方法论上对斯皮岑“精英宫廷阴谋论”作出了颇具分寸的批判界定（区分“接触/倒沙皇计划”与“街头/兵营命令链”），并对苏汉诺夫回忆录作出清晰的 B 级文献分层提示。主要问题在于：再现了 `Dmitrii Gaida` 错名（P0）；未能精准提炼 Hasegawa (2018) 自我修正与 Gaida (2003) 之间的针锋相对，错用 Figes 论断卡时域；`core_cards` 竟漏掉了最核心的 `CON-dual-power` 及临时政府/苏维埃组织卡，T3 亦漏列 4 篇对应精读札记。

#### 03-01｜P0｜学者名张冠李戴：`Dmitrii Gaida (2003)` 实为 `Fedor Gaida`（Фёдор Александрович Гайда）
- **定位**：[`DEB-1917-dual-power-and-february-origins.md:27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md#L27)。
- **核证**：查阅 [`CLM-gaida-2003-liberals-in-february-1917.md:4`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-gaida-2003-liberals-in-february-1917.md#L4)，`scholar` 为 **`SCH-gaida-fedor`**，与 02-01 属同源姓名错误。
- **修复**：更正为 `Fedor Gaida (2003)`。

#### 03-02｜P1｜核心学术交锋失焦与论断卡时域错配：Hasegawa (2018) vs Gaida (2003) 的正面对立被抹平；Figes 论断卡实为 3–10 月军队解体而非 2 月哗变；Galili 第二章（2–3 月双重政权）被忽视
- **定位**：[`L26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md#L26)、[`L27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md#L27)、[`L30`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md#L30)、[`L31`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md#L31)。
- **核证**：
  1. **Hasegawa (2018) 与 Gaida (2003) 的直接分歧被抽象话语掩盖**：
     - [`CLM-hasegawa-2018-duma-committee-revision.md:18`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-hasegawa-2018-duma-committee-revision.md#L18) 与 [`CLM-hasegawa-2018-dual-power-origins.md:18`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-hasegawa-2018-dual-power-origins.md#L18) 的核心突破是：长谷川毅在 2018 年版推翻自己 1981 年的“不情愿革命者”旧论，论证杜马临时委员会自始具革命意图、先于苏维埃建军事委员会、2 月 27 日晚 11:30 夺权与苏维埃无关；且**双重政权并非托洛茨基所言“苏维埃自愿让权”（苏维埃根本无行政机器可让），而是米留可夫在 3 月 3 日 [O.S.] 首次内阁会议上蓄意废黜国家杜马、自断民选法统后，反使强势临时政府被迫仰赖虚弱苏维埃**。本卡 L26 仅轻描淡写“重新检视杜马委员会的先行作用”，漏掉了米留可夫废黜杜马这一宪制枢纽。
     - 与之针锋相对，[`CLM-gaida-2003-liberals-in-february-1917.md:18-26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-gaida-2003-liberals-in-february-1917.md#L18-L26) 论证自由派实为缺乏组织能力、因畏惧沙皇军法审判与暴民清洗才仓促接权的 **“叹着气的革命者／革命的俘虏”**，获胜的是作为物理场所的塔夫利达宫而非作为立宪机构的杜马——同时也直接证伪了自由派宫廷政变神话。本卡 L27 的概括（“其选择与革命压力塑造新政府的合法性和责任困境”）极其空泛，完全丢掉了 Gaida 的核心论点及其与 Hasegawa 2018 的正面交锋。
  2. **Figes 论断卡时域错配**：L31 把 [`CLM-figes-1996-soldier-mutiny-and-social-inversion.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-figes-1996-soldier-mutiny-and-social-inversion.md) 挂在“二月革命精英阴谋论及其批判”行，意在以“士兵哗变”反驳二月宫廷阴谋。但实际打开该论断卡可知，它出自 Figes 第九章（`ch16`, `pp. 404–412`），讨论的是 **1917 年 3–10 月《第一号命令》之后军队纪律瓦解、前线联欢与“战壕布尔什维主义”**，并非 2 月 27 日首都预备营哗变本身！未加时域限定即用于反驳二月起源阴谋论，属于轻度错配。
  3. **Galili 2–3 月双重政权论述被忽视**：L30 批评 Galili“联合政府主要是五月以后发展，不能直接充当二月起义的原因”——虽准确限定了 `CLM-galili-1989-coalition-government-trap`，但忽略了站内精读札记 [`RN-W5-menshevik-defensism-and-coalition.md` §2.1（L28–43）](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/galili_1989_menshevik_leaders/RN-W5-menshevik-defensism-and-coalition.md#L28-L43) 已完整精读 Galili 第二章 *The Origins of Dual Power*（`pp. 45–68`），从粮食铁路技术依赖、“士兵革命”疑虑与工人反专政心理正面解释了 **3 月初双重政权本身的形成**。
- **修复**：重写 Hasegawa 与 Gaida 两栏摘要以凸显“主动革命／废黜杜马悖论 vs 叹气革命者／塔夫利达宫场所胜利”的对立；对 `CLM-figes-1996-soldier-mutiny-and-social-inversion` 加注“主要涉及 3 月《第一号命令》后的社会逆转与军纪瓦解”，反驳二月街头/兵营阴谋论的实证锚点应收归 Hasegawa `CLM-hasegawa-2018-sub-elite-activists` 与 Gaida `CLM-gaida-2003-liberals-in-february-1917`（L21）；Galili 栏增引 `RN-W5` 第二章。

#### 03-03｜P1｜`core_cards` 竟漏挂 `CON-dual-power` 与临时政府/苏维埃卡，T3 漏引 4 篇对应札记与 3 月 3 日米哈伊尔拒位史实
- **定位**：[`L11`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md#L11)、[`L22`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md#L22)、[`L36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md#L36)。
- **核证**：
  1. **`core_cards` 严重缺项**：本卡题为“二月革命起源与‘双重政权’宪制形成之争”，但 `core_cards`（仅 5 项）竟然漏掉了概念母卡 [`CON-dual-power`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-dual-power.md) 本身，同时漏掉了两大主角机构 [`ORG-provisional-government`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-provisional-government.md)、[`ORG-petrograd-soviet`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-petrograd-soviet.md)、[`PER-nicholas-ii`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-nicholas-ii.md)，以及直接导向本争鸣的新建事件卡 [`EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc.md)。
  2. **T3 锚点漏引 4 篇站内已入库精读札记**：矩阵引用了 Galili、Trotsky、Figes、Spitsyn 四家论断卡，但 T3 L36 一律未列其精读札记——即 [`RN-W5-menshevik-defensism-and-coalition.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/galili_1989_menshevik_leaders/RN-W5-menshevik-defensism-and-coalition.md)（A 级）、[`RN-W5-peasant-soldier-revolution-and-tragedy.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/figes_1996_peoples_tragedy/RN-W5-peasant-soldier-revolution-and-tragedy.md)（A 级）、[`RN-W7-uneven-development-and-insurrection-art.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/trotsky_1930_history_rr_zh/RN-W7-uneven-development-and-insurrection-art.md)（B 级）、[`RN-W32-spitsyn-neo-traditionalist-synthesis-1917-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/spitsyn_russia_ussr_v3_zh/RN-W32-spitsyn-neo-traditionalist-synthesis-1917-1929.md)（B 级，且应如苏汉诺夫般显式标明 B 级教科书/新传统主义属性，不与 S/A 级混列）。
  3. **经验基准漏掉 3 月 3 日闭环**：T3 所引 [`1917-03-02_nicholas-ii-abdication-manifesto.md:45-49`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/W32_milestone_docs/1917-03-02_nicholas-ii-abdication-manifesto.md#L45-L49) 同时收录了 `1917-03-03 [O.S.] / 1917-03-16 [N.S.]` 米哈伊尔大公《拒绝即位宣言》（将最高权力移交立宪会议并号召服从临时政府），这正是 YAML `end_os: "1917-03-03"` 及长谷川毅所论 3 月 3 日临时政府首议废黜杜马的宪制闭环；但 L22 经验基准止步于 3 月 2 日尼古拉二世退位，未提 3 月 3 日。
- **修复**：`core_cards` 增补 `CON-dual-power`、`ORG-provisional-government`、`ORG-petrograd-soviet`、`PER-nicholas-ii`、`EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc`；L22 经验基准补入 3 月 3 日 [O.S.] / 3 月 16 日 [N.S.] 米哈伊尔拒位及临时政府首次会议；T3 补全上述 4 篇札记并单列 B 级分层说明（苏汉诺夫、托洛茨基、斯皮岑）。

#### 03-04｜P2｜文献对齐细节
- T3 L36 列出 `1917-04-04_april-theses.md` 作为双重政权锚点合理，但可顺注列宁直接专论双重政权的 1917 年 4 月 9 日 [O.S.]《论两个政权》（*О двоевластии*）尚属站内原典缺口（见 [`CON-dual-power.md:14`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-dual-power.md#L14)），与外部缺口清单衔接。

---

## 四、阶段一（01–03）审计小计

| 序号 | 卡片 ID | P0 | P1 | P2 | 核心问题要点 |
| :---: | :--- | :-: | :-: | :-: | :--- |
| 01 | `DEB-1903-bolshevik-menshevik-split` | 1 | 2 | 1 | `Arno Mayer` 误写（实为 `Robert Mayer`）且将主编 Zelnik 误作 Smith 论文作者（P0）；矩阵缺冷战雅各宾连续论/当事人栏；漏引 1906 斯德哥尔摩党章反证、`RN-W22`、`EVT-1891-1903` 与已核第 23 次唱名票数 |
| 02 | `DEB-1914-haimson-thesis-stability` | 2 | 2 | 1 | `Dmitrii Gaida` 误写（实为 `Fedor Gaida`）（P0）；范围止于 1901/1903 的洛吉诺夫卡被错塞入 Steinberg/Hoffmann 栏（P0）；漏用站内海姆森 2005 专著（`RN-W29`）、Hogan 金属工人卡及 `DATA-01`/`DATA-07`；Bonnell 反驳海姆森“半农民新兵论”的核心交锋被抹平；漏挂新建 `EVT-1907-1914` 与 `EVT-1914-1916` |
| 03 | `DEB-1917-dual-power-and-february-origins` | 1 | 2 | 1 | `Dmitrii Gaida` 误写（实为 `Fedor Gaida`）（P0）；Hasegawa 2018 废黜杜马悖论 vs Gaida 叹气革命者对立失焦；Figes 论断卡时域错配（实为 3–10 月）；`core_cards` 漏 `CON-dual-power`/临时政府/苏维埃/`EVT-1914-1916`；T3 漏 4 篇札记及 3 月 3 日米哈伊尔拒位闭环 |

---

## 五、阶段二（04–06）双历法与日期复核表

| 卡片 | 卡内日期（YAML／正文） | `kb.py` 复算与规则核查 | 判定 |
| :--- | :--- | :--- | :--- |
| 04 `DEB-1917-july-days-spontaneity-vs-conspiracy` | YAML：`1917-07-03 O.S. / 1917-07-16 N.S.` 至 `1917-07-05 O.S. / 1917-07-18 N.S.`；正文：`6月18日（公历7月1日）`、`7月2日（公历7月15日）`、`7月3–5日`（仅标俄历）、`7月4日深夜` | `07-03` → `07-16` ✓；`07-05` → `07-18` ✓；`06-18` → `07-01` ✓；`07-02` → `07-15` ✓（均 +13） | **换算无误**；但 L22 将佩列韦尔泽夫向报界释放德援材料记作“7月4日深夜”，按 Pipes `ch19_section.md#L688` 实为 **7 月 4 日下午约 5 时**（《活语言报》次晨刊出），且 7 月 3–5 日正文未附公历对照（P2） |
| 05 `DEB-1917-october-coup-or-social-revolution` | YAML：`1917-10-24 O.S. / 1917-11-06 N.S.` 至 `1917-10-26 O.S. / 1917-11-08 N.S.`；正文：`1917-10-25 [O.S.] / 1917-11-07 [N.S.]`、`10月26日 [O.S.] / 11月8日 [N.S.]` | `10-24` → `11-06` ✓；`10-25` → `11-07` ✓；`10-26` → `11-08` ✓（均 +13；与站内《和平法令》《土地法令》校勘注一致） | **换算无误**；YAML `era: "1917-1918"` 跨至 1918 年 1 月解散立宪会议，建议附注说明与 `dates` 起止的涵盖差异（P2） |
| 06 `DEB-1918-red-terror-and-civil-war-origins` | YAML：`start_ns: 1918-07-06`、`end_ns: 1918-09-05`（1918-02-14 后纯公历）；正文：`1917-12-07 [O.S.] / 1917-12-20 [N.S.]`、`1918年7月`、`7月10日`、`9月5日` | `1917-12-07 O.S.` → `12-20 N.S.`（+13）✓；1918-02-14 后均采用纯公历 ✓ | **历法合规**；但元数据三处时域口径脱节：`title` 为 `1918–1921`、`era` 为 `1917-1918`、`dates` 仅取 `1918-07-06` 至 `1918-09-05`（2 个月），正文又起自 1917-12-07 契卡成立、矩阵延伸至 1922/1929（P2） |

---

## 六、阶段二逐卡深度审计与修复方案（04–06）

### 04｜七月事变：基层自发风暴还是布尔什维克试探性政变？（`DEB-1917-july-days-spontaneity-vs-conspiracy`）

**总体评价**：**本批 6 张卡中质量最高的一张（0 P0）**。对 Pipes、Rabinowitch、Galili、Boll 四家的核心材料均有实质性原文对读——例如准确核出 Pipes 将七月事变比作“1923 年啤酒馆政变”的同时又承认“列宁在七月事前筹备中的直接作用无法证实、德国资金的具体去向亦未明且含十卢布假币”（实证见 [`sources/monographs/pipes_1990_russian_rev/ch19_section.md:389,407,545`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/pipes_1990_russian_rev/ch19_section.md#L389) 及 [`ch30_chronology.md:184`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/pipes_1990_russian_rev/ch30_chronology.md#L184)），精准再现了 Rabinowitch 的“三中心三派系”、7 月 3 日 16 时／19 时／午夜前时序、《真理报》留白与涅夫斯基自白。主要短板在于第 5 行匿名混挂苏汉诺夫四月卡且空心化洛吉诺夫的七月实质发现（P1），`core_cards` 与 T3 漏挂核心节点与 `DATA-01`（P1），以及 L28 人名笔误（`但`→`丹`）与 L22 佩列韦尔泽夫放风时间偏差（P2）。

#### 04-01｜P1｜第 5 行匿名混挂苏汉诺夫四月回忆录卡，且空心化洛吉诺夫在 `RN-W12B` 中的七月实质论证
- **定位**：[`DEB-1917-july-days-spontaneity-vs-conspiracy.md:30`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-july-days-spontaneity-vs-conspiracy.md#L30)、[`L35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-july-days-spontaneity-vs-conspiracy.md#L35)。
- **核证**：
  1. 矩阵第 5 行“代表学者与著作”仅写 `Vladlen Loginov 的列宁研究`，却在“支撑论断卡”中挂了 [`CLM-sukhanov-1922-lenin-april-arrival-shock.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-sukhanov-1922-lenin-april-arrival-shock.md)（作者为孟什维克国际派当事人 **N. N. Sukhanov**，B 级回忆录，该卡第 45 行明确限定“*本卡本身证的是 4 月 3–4 日的当场接受史*”）。由于 Codex 已加注 `（四月背景）` 并在 T3 L35 提醒其“不能作为七月命令的直接证据”，故本项不判 P0 而判 **P1**；但未在学者栏署名苏汉诺夫仍不规范。
  2. 更关键的是，第 5 行把洛吉诺夫压缩成一句空话（“考察列宁在 1917 年危机中的策略收缩、时机判断与党内博弈”），完全漏掉了站内已精读的 [`reading-notes/service_loginov/RN-W12B-service-trotsky-critique-and-loginov-1917.md:122-128`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/service_loginov/RN-W12B-service-trotsky-critique-and-loginov-1917.md#L122-L128) 中洛吉诺夫对七月事变的直接一手考证：列宁最初认为 7 月 3 日示威“不合时宜”（*inopportune*）；事变后列宁在 **7 月 10 日 [O.S.] 提纲**中宣布“全部政权归苏维埃”的和平发展期已终结；而 **7 月 13–14 日 [O.S.] 布尔什维克中央扩大会议竟明确否决了列宁的该提纲**——这一事实本身便是检验“列宁在 1917 年夏天能否单向发号施令”的极硬证据！
- **修复**：在第 5 行补入洛吉诺夫关于 7 月 3 日判断、7 月 10 日提纲与 7 月 13–14 日中央扩大会议否决列宁方案的核心证据；将苏汉诺夫四月卡移出洛吉诺夫行（或明示 `N. N. Sukhanov (1922，B 级当事人背景)`）。

#### 04-02｜P1｜`core_cards` 与 `[T3]` 漏引站内已有数据卡 `DATA-01`、双重政权母卡及孟什维克／社革党视角
- **定位**：[`L11`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-july-days-spontaneity-vs-conspiracy.md#L11)、[`L28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-july-days-spontaneity-vs-conspiracy.md#L28)、[`L35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-july-days-spontaneity-vs-conspiracy.md#L35)。
- **核证**：
  1. 矩阵 L28 明确引用了 `DATA-01`（56%／58.2% 比例与印刷工护国立场），但 T3 L35 的站内锚点清单却**漏列** [`data/DATA-01-1905-1917-strikes-and-petrograd-elections.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-01-1905-1917-strikes-and-petrograd-elections.md)。
  2. `core_cards` 漏掉了因七月事变而正式终结的 [`CON-dual-power`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-dual-power.md)，以及直接陷入危机（切尔诺夫 7 月 4 日遭喀琅施塔得水兵扣押、全俄苏维埃执委会拒接政权）的 [`ORG-mensheviks`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-mensheviks.md)、[`ORG-psr`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-psr.md)、[`PER-chernov`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-chernov.md)、[`PER-tsereteli`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-tsereteli.md)、[`PER-martov-l`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-martov-l.md)。
  3. 站内 [`reading-notes/davies_basil/RN-W18-1929-collectivization-takeoff-and-mensheviks-1917.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/davies_basil/RN-W18-1929-collectivization-takeoff-and-mensheviks-1917.md)（[`CLM-basil-1984-menshevik-three-way-paralysis.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-basil-1984-menshevik-three-way-paralysis.md)）分析孟什维克在七月事变中的三向瘫痪，[`RN-W29-haimson-lenin-1917-leap-and-kollontai-workers-opposition.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/haimson2005_kollontai1921/RN-W29-haimson-lenin-1917-leap-and-kollontai-workers-opposition.md) 分析七月前后彼得格勒工人的极化与情绪转向，均宜在 T3 补挂。
- **修复**：T3 补列 `DATA-01`、`RN-W18`、`RN-W29`；`core_cards` 增补 `CON-dual-power`、`ORG-mensheviks`、`ORG-psr`、`PER-chernov`、`PER-tsereteli`。

#### 04-03｜P2｜人名笔误（`但`→`丹`）与佩列韦尔泽夫放风时段偏差
- **定位**：[`L22`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-july-days-spontaneity-vs-conspiracy.md#L22)、[`L28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-july-days-spontaneity-vs-conspiracy.md#L28)。
- **核证**：
  1. L28 将孟什维克领袖费奥多尔·丹（F. I. Dan）误写为“**`但`与齐赫伊泽**”，属明显同音错字。
  2. L22 称“俄历 7 月 4 日**深夜**司法部长佩列韦尔泽夫向报界抛出列宁接受德国津贴的指控”；按 [`sources/monographs/pipes_1990_russian_rev/ch19_section.md:688`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/pipes_1990_russian_rev/ch19_section.md#L688) 记载，佩列韦尔泽夫系于 **7 月 4 日下午约 5 时（around 5 p.m.）** 向 80 余名军方代表与记者通报材料，右翼小报《活语言报》次日（7 月 5 日）清晨见报（午夜系部队清场塔夫利达宫之时刻）。此外 L22 的 7 月 3、4、5 日可顺附 `[N.S.]` 对照。
- **修复**：L28 `但与齐赫伊泽` 改为 `丹（F. I. Dan）与齐赫伊泽`；L22 改为 `俄历7月4日下午（约5时）……并于次晨见报`，并补公历对照。

---

### 05｜十月革命：少数派政变还是自下而上的社会革命？（`DEB-1917-october-coup-or-social-revolution`）

**总体评价**：双历换算准确、T1 对“武装夺权形态／工人社会动员／立宪会议合法性冲突”的三层区分切中要害。但存在 **1 项 P0 级学者归属错挂**（将俄罗斯史家洛吉诺夫的论断卡静默塞入拉比诺维奇行，且两者对“是否应等第二次全俄苏维埃代表大会”的评价存在直接张力），同时漏掉了孟什维克／维克热尔妥协史、立宪会议合法性冲突与帝国边疆三大站内 A 级论断卡组，T3 亦漏列 6 篇以上对应札记与站内定量数据卡 `DATA-01`/`DATA-07`。

#### 05-01｜P0｜学者归属张冠李戴：拉比诺维奇行匿名混挂弗拉德连·洛吉诺夫（Vladlen Loginov, 2017）论断卡，且掩盖二者实质分歧
- **定位**：[`DEB-1917-october-coup-or-social-revolution.md:27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md#L27)（矩阵第 2 行“代表学者与著作”仅写 `Alexander Rabinowitch, The Bolsheviks Come to Power (1976)`，却在“支撑论断卡”中并列挂了 `CLM-rabinowitch-1976-open-mass-party-and-trotsky-strategy` 与 `CLM-loginov-lenin-1917-fleeting-window-of-power`）。
- **核证**：
  1. 查阅 [`CLM-loginov-lenin-1917-fleeting-window-of-power.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-loginov-lenin-1917-fleeting-window-of-power.md#L4-L6)，该卡作者为 **`SCH-loginov-vladlen`**（俄罗斯史家弗拉德连·洛吉诺夫，*Ленин в 1917 году. На грани возможного*, 2017），既非拉比诺维奇著作，也未在 T3 列出其精读札记 [`RN-W12B-service-trotsky-critique-and-loginov-1917.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/service_loginov/RN-W12B-service-trotsky-critique-and-loginov-1917.md)。
  2. 更重要的是，**洛吉诺夫的论点与拉比诺维奇／托洛茨基路线存在直接张力**：[`CLM-rabinowitch-1976-open-mass-party-and-trotsky-strategy.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-rabinowitch-1976-open-mass-party-and-trotsky-strategy.md) 凸显托洛茨基以彼得格勒苏维埃军革委防卫姿态并将行动锚定于第二次全俄苏维埃代表大会的合法性策略；而 [`CLM-loginov-lenin-1917-fleeting-window-of-power.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-loginov-lenin-1917-fleeting-window-of-power.md) 则着重为**列宁反驳等待苏维埃大会（称等待是“犯罪”、拖延就是“死亡”）的紧急窗口判断**辩护。把洛吉诺夫匿名塞进拉比诺维奇行，不仅造成学者归属错误，还掩盖了布尔什维克党内及史学界关于“列宁先行夺权 vs 托洛茨基依托代表大会”的核心分歧。
- **修复**：将 `CLM-loginov-lenin-1917-fleeting-window-of-power` 移出拉比诺维奇行，单列或归入“俄罗斯当代修正派／政治时机论”（显式署名 `Vladlen Loginov (2017)` 并在 T3 补挂 `RN-W12B`），并写明其与拉比诺维奇在“等待大会 vs 先行出击”上的聚焦差异。

#### 05-02｜P1｜`[T2]` 矩阵遗漏站内已有的孟什维克／维克热尔妥协史、立宪会议合法性冲突与帝国边疆三组 A 级论断卡，且既有行摘要失焦
- **定位**：[`L13-14`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md#L13-L14)、[`L26-31`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md#L26-L31)、[`L34`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md#L34)。
- **核证**：
  1. **三组直接对应的站内 A 级论断卡被整体漏引**：
     - **维克热尔谈判与孟什维克／多党社会主义政府流产**：[`CLM-basil-1984-october-and-vikzhel-collapse.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-basil-1984-october-and-vikzhel-collapse.md)（John Basil 1984：孟什维克在十月危机中的组织瘫痪、维克热尔调停与 10 月 30 日士官生暴动撕裂和平妥协）与 [`CLM-yao-hai-post-october-coalition-failure-and-one-party-formation.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-yao-hai-post-october-coalition-failure-and-one-party-formation.md)（姚海 2013：十天维克热尔危机中加米涅夫／季诺维也夫／李可夫／诺金警告“纯布尔什维克政府只能靠政治恐怖维持”）。
     - **立宪会议 vs 苏维埃合法性冲突**：本卡 T1 与 T3 反复将“苏维埃代表大会授权 vs 制宪会议普选合法性”作为核心裁判轴，但 `[T2]` 矩阵竟未挂任何立宪会议论断卡——而站内恰有 [`CLM-yao-hai-constituent-assembly-vs-soviet-legitimacy-clash.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-yao-hai-constituent-assembly-vs-soviet-legitimacy-clash.md) 与 [`CLM-rabinowitch-2007-constituent-assembly.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-rabinowitch-2007-constituent-assembly.md)。
     - **帝国边疆视角**：[`CLM-blanc-2021-borderlands-in-1905-and-1917.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-blanc-2021-borderlands-in-1905-and-1917.md)（Eric Blanc 2021）在自身 YAML 中即直接挂接 `DEB-1917-october-coup-or-social-revolution`，T3 L34 也提到了“帝国研究”转向，却完全未引用该卡。
  2. **既有 6 行摘要多处抹平学者标志性论点**：
     - **Pipes（L26）**：漏掉了其最具标志性的两项概念——援引马拉帕尔泰“静默技术性政变”与**“针对全国苏维埃组织本身的政变”**（夺权抢在二大开幕前将全俄苏维埃置于既成事实之下）；
     - **Koenker（L28）**：[`CLM-koenker-1981-moscow-october-armed-struggle-vs-petrograd.md:31`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-koenker-1981-moscow-october-armed-struggle-vs-petrograd.md#L31) 与 [`CLM-koenker-1981-rational-incremental-radicalization.md:29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-koenker-1981-rational-incremental-radicalization.md#L29) 的核心贡献在于证明莫斯科多数工人虽在原则上拥护苏维埃政权，但**拒绝为党派之争冒内战风险**，其激进化遵循“政策先于党派”（*policy before party*）的理性渐进机制——L28 仅笼统写“不必然意味着群众盲从”，丢失了这一精细机制；
     - **Sukhanov（L29）**：[`CLM-sukhanov-1922-october-walkout-tragedy.md:18,35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-sukhanov-1922-october-walkout-tragedy.md#L18) 最核心的史学悖论是——苏汉诺夫虽痛斥布尔什维克政权缺乏民主合法性、认为温和派退场酿成悲剧，却**以亲历者身份断然反驳右翼“纯军事阴谋”说**，证言彼得格勒工人与驻军压倒性支持推翻临时政府。L29 漏掉了这一决定性的“反对者证言”。
- **修复**：补全上述 3 组 A 级论断卡（可增设“温和社会主义妥协流产与立宪合法性冲突”及“帝国边疆与记忆建构”行，并可补挂 Corney `CLM-corney-2004-istpart-and-institutionalizing-october-memory`）；充实 Pipes、Koenker、Sukhanov 三行摘要。

#### 05-03｜P1｜`[T3]` 漏引 6 篇以上直接对应札记与站内定量数据卡 `DATA-01`/`DATA-07`，将立宪会议统计笼统划入外部缺口；`core_cards` 缺核心节点
- **定位**：[`L11`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md#L11)、[`L36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md#L36)、[`L38`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md#L38)。
- **核证**：
  1. **T3 L36 锚点严重残缺（仅列 5 项）**：矩阵本身已引用 Koenker、Trotsky、Sukhanov、Figes、Loginov 等多张论断卡，但 T3 全数漏列其对应的站内精读札记——[`RN-W32-koenker-moscow-strikes-duma-votes-and-october-week.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/koenker_1981_moscow_workers/RN-W32-koenker-moscow-strikes-duma-votes-and-october-week.md)、[`RN-W7-uneven-development-and-insurrection-art.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/trotsky_1930_history_rr_zh/RN-W7-uneven-development-and-insurrection-art.md)（B 级）、[`RN-W6-sukhanov-eyewitness-1917.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/sukhanov_1922_notes/RN-W6-sukhanov-eyewitness-1917.md)（B 级）、[`RN-W5-peasant-soldier-revolution-and-tragedy.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/figes_1996_peoples_tragedy/RN-W5-peasant-soldier-revolution-and-tragedy.md)、[`RN-W12B-service-trotsky-critique-and-loginov-1917.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/service_loginov/RN-W12B-service-trotsky-critique-and-loginov-1917.md)，外加 `RN-W18`（Basil）、`RN-W36`（姚海）、`RN-W11`（Corney）。
  2. **把站内已编译的莫斯科与立宪会议选举汇总表划入外部缺口**：T3 L38 将“制宪会议地区选举底册”笼统列为外部缺口，却未锚定站内已建好的两大定量数据卡——[`data/DATA-01-1905-1917-strikes-and-petrograd-elections.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-01-1905-1917-strikes-and-petrograd-elections.md)（§4 彼得格勒 1917 年选举曲线）与 [`data/DATA-07-1905-1918-unions-moscow-swings-and-constituent-assembly-votes.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-07-1905-1918-unions-moscow-swings-and-constituent-assembly-votes.md)（§2.2 莫斯科 1917 年三次选举剧烈摇摆；§3 完整汇总 Radkey 1989、Protasov 1997、Figes、Haimson、Koenker 多源立宪会议选票统计）。
  3. **`core_cards`（仅 6 项）漏挂大批核心现存节点**：[`MTG-1917-10-2nd-congress-of-soviets`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1917-10-2nd-congress-of-soviets.md)、[`POL-decrees-on-peace-and-land-1917`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-decrees-on-peace-and-land-1917.md)、[`ORG-provisional-government`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-provisional-government.md)、[`CON-constituent-assembly`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-constituent-assembly.md)、[`EVT-1918-01-constituent-assembly-dispersal`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1918-01-constituent-assembly-dispersal.md)、[`ORG-vikzhel`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-vikzhel.md)、[`ORG-factory-committees-1917`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-factory-committees-1917.md)、[`CON-workers-control`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-workers-control.md) 均已入库而未关联。
- **修复**：T3 补全上述札记与 `DATA-01`/`DATA-07` 锚点，将外部缺口精准收窄为“分县／分前线原始选举底册与各省苏维埃 1917–1918 政权更迭逐日档案”；`core_cards` 增补上述关键节点。

#### 05-04｜P2｜元数据与 B 级当事人文献分层微瑕
- **定位**：[`L5`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md#L5)、[`L29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md#L29)、[`L36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md#L36)。
- **修复**：说明 `era: "1917-1918"` 为何延伸至 1918 年初立宪会议解散；在 T2/T3 中显式标明托洛茨基（1930）与苏汉诺夫（1922）属 **B 级当事人回忆／论战文献**，与 A 级学术专著分层呈现。

---

### 06｜红色恐怖、内战爆发与暴力制度化之争（`DEB-1918-red-terror-and-civil-war-origins`）

**总体评价**：方法论边界意识清晰（能明确反对将 1918 年镇压数据与 1937–1938 年大清洗直接等同，也反对把战时应急当作永久制度免责理由）。但本卡存在 **2 项严重 P0 级作者与编者张冠李戴**——再现了“仅凭文件名猜作者”的系统性病灶：既把论文集主编 Donald Raleigh 误作德拉诺·杜加姆（Delano Dugarm）章节作者，又把圣彼得堡国立大学史家伊·谢·拉特科夫斯基（Igor Ratkovsky）一个人凭两套文件名拆成两行、分别误作匿名“契卡编年史”和“A. M. Plekhanov”。此外，矩阵严重漏引被镇压社会主义对手（马尔托夫、拉德基／社革党、丘拉科夫工人抗议）及内战结构／定量校准派（Mawdsley、Zemskov），T3 竟漏引站内核心统计表 `DATA-06`，`core_cards` 也漏掉了红恐事件卡、内战事件卡与契卡机构卡本身。

#### 06-01｜P0｜主编误作作者：`Donald Raleigh (2001)` 实为论文集编者，所挂论断卡实际作者为德拉诺·杜加姆（`Delano Dugarm`）
- **定位**：[`DEB-1918-red-terror-and-civil-war-origins.md:27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L27)（矩阵第 4 行将 `CLM-raleigh-2001-local-bolshevik-violence-and-clientelism` 归于 `Donald Raleigh (2001)` 名下）。
- **核证**：打开 [`CLM-raleigh-2001-local-bolshevik-violence-and-clientelism.md:5-6,19,33`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-raleigh-2001-local-bolshevik-violence-and-clientelism.md#L5-L33)，YAML 明示 `chapter_author: "Delano Dugarm"`，第 19 行与第 33 行更以粗体专门警示：**“实际论证作者为德拉诺·杜加姆（Delano Dugarm，坦波夫省研究），文件名沿用用户指定的编者罗利及 2001 年书名”**。此错与第 01 号卡把主编 Zelnik 误作 S. A. Smith 作者（`01-01`）完全同源。
- **修复**：更正为 `Delano Dugarm (2001，收入 Donald J. Raleigh 编 Provincial Landscapes)`，并指明其坦波夫省个案属性。

#### 06-02｜P0｜同一学者被拆为两行且双重错名：伊·谢·拉特科夫斯基（`Igor Ratkovsky`, 2017）分别被误作匿名“契卡编年史”（L27）与“A. M. Plekhanov”（L29）
- **定位**：[`DEB-1918-red-terror-and-civil-war-origins.md:27,29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L27-L29)（第 4 行把 `CLM-cheka-chronicle-hostage-and-local-autonomy`、`CLM-cheka-chronicle-suppression-of-socialist-rivals` 称作 `契卡编年史`；第 6 行把 `CLM-plekhanov-am-dzerzhinsky-cheka-institutionalization` 归于 `A. M. Plekhanov`）。
- **核证**：
  1. 查阅 [`CLM-cheka-chronicle-hostage-and-local-autonomy.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-cheka-chronicle-hostage-and-local-autonomy.md#L4-L6) 与 [`CLM-cheka-chronicle-suppression-of-socialist-rivals.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-cheka-chronicle-suppression-of-socialist-rivals.md#L4-L6)，两卡 `scholar` 均明确为 **`SCH-ratkovsky-igor`**（伊·谢·拉特科夫斯基，Igor Ratkovsky），著作系其 2017 年专著 *Хроника красного террора ВЧК. Карающий меч революции*，绝非匿名一手编年史！
  2. 查阅 [`CLM-plekhanov-am-dzerzhinsky-cheka-institutionalization.md:5,41`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-plekhanov-am-dzerzhinsky-cheka-institutionalization.md#L5)，卡片明示：*“原书俄文版 Дзержинский. От «Астронома» до «Железного Феликса»（2017）**内页执笔人为圣彼得堡国立大学历史学家伊·谢·拉特科夫斯基（И. С. Ратьковский）**，而其重建契卡组织演进与捷尔任斯基书信批示的核心一手档案基石，系亚·米·普列汉诺夫与亚·亚·普列汉诺夫合编的《全俄肃反委员会与捷尔任斯基文献集》（2007）”*。
  3. 显然 Codex 未打开三张 `CLM-*` 正文，仅据文件名前缀 `cheka-chronicle-*` 和 `plekhanov-am-*` 望文生义，把**同一位当代俄罗斯史家（Igor Ratkovsky, 2017）**硬生生拆进矩阵两行且两处均未写出其本名！
- **修复**：合并并更正学者署名：将上述三张拉特科夫斯基论断卡归入 `Igor Ratkovsky (2017，依托 A. M. & A. A. Plekhanov 2007 档案集)`，清楚标注其关于 1918 年秋约 8,000 人处决估算、人质制与地方越权及捷尔任斯基机构化的完整观点，将 `O. B. Mozokhin` 单列或与 Ratkovsky 清晰区分。

#### 06-03｜P1｜`[T2]` 矩阵遗漏被镇压社会主义对手（马尔托夫、拉德基／社革党、丘拉科夫工人抗议）及内战结构／定量校准派（Mawdsley、Zemskov），且既有行摘要空泛
- **定位**：[`L11`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L11)、[`L24-29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L24-L29)、[`L32`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L32)。
- **核证**：
  1. **五组核心站内 S/A 级论断卡被整体漏引**：
     - **S 级当事人／左翼民主批判**：[`CLM-halle-1920-martov-critique-of-terror-and-21-conditions.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-halle-1920-martov-critique-of-terror-and-21-conditions.md)（马尔托夫 1920 年 10 月 15 日哈勒演说：控诉无差别红色恐怖、彼得格勒一次处决约 800 人，揭示恐怖如何反噬社会主义政党道德与内部治理）；
     - **A 级社革党／第三势力崩溃**：[`CLM-smith-scott-2011-psr-third-force-collapse.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-smith-scott-2011-psr-third-force-collapse.md)（注意：该卡实际精读著作为 **Oliver H. Radkey (1963), *The Sickle under the Hammer***，解析社革党／科穆奇“第三势力”的组织涣散与白军“保护色”如何挤压出红白两极暴力格局）；
     - **A 级 1918 年工人抗议与伊热夫斯克—沃特金斯克起义**：[`CLM-churakov-2004-soviet-worker-protest-dynamics-1918.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-churakov-2004-soviet-worker-protest-dynamics-1918.md) 与 [`CLM-churakov-2004-izhevsk-votkinsk-worker-insurrection.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-churakov-2004-izhevsk-votkinsk-worker-insurrection.md)（D. O. Churakov 2004：1918 年 210–220 家企业 10–25 万工人抗议，直接检验“镇压对象仅限于剥削阶级”的官方口径）；
     - **A 级内战军事化结构派**：[`CLM-mawdsley-1987-civil-war-militarized-regime.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-mawdsley-1987-civil-war-militarized-regime.md)（Evan Mawdsley 1987：内战与斯大林主义均是十月夺权的可能后果，“内战代价即革命代价”）；
     - **A 级档案定量校准派**：[`CLM-zemskov-1920s-archival-repression-scale-before-1930.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-zemskov-1920s-archival-repression-scale-before-1930.md)（V. N. Zemskov：1918–1920 登记反革命案判刑 62,231 人、处决 25,709 人，总上限 <10 万——与 Leggett 的约 14 万+14 万、Mozokhin 的登记约 1.75 万／全期上限 <5 万、Ratkovsky 1918 秋约 8,000 人构成站内最关键的跨口径统计对勘基准！）。
  2. **既有各行摘要丢失标志性实证细节**：
     - **Pipes（L24）** 未提其核心论断“法国大革命终结于恐怖，俄国革命始于恐怖”及“恐怖系民众支持的替代品”；
     - **Leggett（L25）** 未提契卡凭人民委员会非立法决议建置（类比尼古拉一世第三厅）及 1922 年 5 月列宁致库尔斯基密信；
     - **Rabinowitch（L26）** 未提彼得格勒党组织党员由 5 万骤降至约 6,000、8 月 30 日市委“自下而上”施压扩大恐怖、五大约 399 席伪造布尔什维克代表资格，以及 **1918 年 12 月彼得格勒契卡秘密撤销对左翼社革党“有组织武装起义”指控**等震撼档案发现；
     - **Mozokhin（L29）** 未揭示其核心的**国家主义二分法**（肯定 1918–1921 战时契卡必要性，却尖锐批判 1922 后和平时期 OGPU 垄断司法：1924 年 4,097 起反革命案仅 6 起移交法院，战时死刑率 6.9% vs 和平期 0.5%/0.94%）。
- **修复**：在 `[T2]` 增补“被镇压社会主义对手与工人抗议”（Martov、Radkey、Churakov）及“内战结构与档案定量校准”（Mawdsley、Zemskov），并充实 Pipes、Leggett、Rabinowitch、Mozokhin 四行核心论据与统计口径对比。

#### 06-04｜P1｜`[T3]` 漏引站内最核心契卡定量数据卡 `DATA-06` 及多篇对应札记；`core_cards` 漏挂红恐／内战事件卡与契卡机构卡
- **定位**：[`L9`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L9)、[`L20`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L20)、[`L34`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L34)、[`L36`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L36)。
- **核证**：
  1. **漏引站内核心统计数据卡 `DATA-06`**：[`data/DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md)（§A 完整收录莫佐欣依据 ЦА ФСБ РФ 整理的 1918–1930 契卡／OGPU 逐年立案、逮捕、判刑与死刑全表）竟然未被 T3 L34 引用，而 L36 反倒把“跨地区处决口径的细化”列作外部缺口却未先锚定 `DATA-06` 与 `Zemskov`。
  2. **漏引多篇直接支撑矩阵的精读札记**：[`RN-W4B-patrimonialism-and-october-coup.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/pipes_1990_russian_rev/RN-W4B-patrimonialism-and-october-coup.md)（Pipes）、[`RN-W32-provincial-smolensk-tambov-saratov-1917-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/raleigh_2001_provincial_landscapes/RN-W32-provincial-smolensk-tambov-saratov-1917-1929.md) / [`RN-W15-moscow-1917-and-provincial-soviet-power.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/koenker_raleigh/RN-W15-moscow-1917-and-provincial-soviet-power.md)（Dugarm/Raleigh）、[`RN-W17-modernity-biopolitics-and-official-anti-trotskyism.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/hoffmann_modernity/RN-W17-modernity-biopolitics-and-official-anti-trotskyism.md)（Hoffmann），外加 `RN-W9`（Martov）、`RN-W23`（Churakov）、`RN-W6`（Mawdsley）、`RN-W22`（Zemskov）。
  3. **已入库 S 级法令文本的关键校勘细节闲置**：[`sources/web-archive/E06_E09_state_and_comintern/1918-09-05_decree-on-red-terror.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E09_state_and_comintern/1918-09-05_decree-on-red-terror.md) 明确考证了 RGASPI 9 月 5 日打印原件与 9 月 10 日《消息报》文本之别（签署人为库尔斯基、彼得罗夫斯基、邦奇-布鲁耶维奇与福季耶娃，**而非捷尔任斯基**），并确认 9 月 5 日决议本身**并未出现“人质”一词**（扣押人质出自 9 月 4 日彼得罗夫斯基电令），L20 经验基准未利用这一站内原典硬核细节。
  4. **`core_cards`（仅 6 项）竟漏掉本争鸣最直接的母事件卡与机构卡**：[`EVT-1918-09-red-terror-and-left-sr-rupture`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1918-09-red-terror-and-left-sr-rupture.md)、[`EVT-1918-1920-russian-civil-war`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1918-1920-russian-civil-war.md)、[`INS-cheka-gpu-ogpu`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-cheka-gpu-ogpu.md)、[`MTG-1918-07-5th-congress-of-soviets`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1918-07-5th-congress-of-soviets.md)、[`EVT-1918-03-brest-litovsk-treaty`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1918-03-brest-litovsk-treaty.md)、[`EVT-1918-worker-protest-and-izhevsk-uprising`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1918-worker-protest-and-izhevsk-uprising.md)、[`PER-spiridonova`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-spiridonova.md)、[`ORG-psr`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-psr.md)、[`ORG-mensheviks`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-mensheviks.md) 全部现存却漏挂。
- **修复**：`core_cards` 优先补入 `EVT-1918-09-red-terror-and-left-sr-rupture`、`EVT-1918-1920-russian-civil-war`、`INS-cheka-gpu-ogpu`、`MTG-1918-07-5th-congress-of-soviets`、`EVT-1918-03-brest-litovsk-treaty`、`EVT-1918-worker-protest-and-izhevsk-uprising`、`PER-spiridonova`；T3 锚点补入 `DATA-06` 及上述精读札记；L20 补注 9 月 4 日彼得罗夫斯基电令与 9 月 5 日法令签署人区别。

#### 06-05｜P2｜YAML 元数据时域三处口径不一致
- **定位**：[`L4-8`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L4-L8)、[`L20`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md#L20)。
- **核证**：`title` 标 `（1918–1921）`，`era` 标 `"1917-1918"`，`dates` 仅取 `1918-07-06` 至 `1918-09-05`（两个月），而正文 L20 起于 1917-12-07 [O.S.] 契卡设立、矩阵又讨论至 1922/1929 年常态化。
- **修复**：统一口径：建议 `era` 改为 `"1917-1921"`（或明确在 `dates` 旁加注“本起止为左翼社革党决裂至红色恐怖法令颁布核心拐点，制度争鸣覆盖 1917-12 契卡建制至 1921/1922 战后改制”）。

---

## 七、全批 6 卡审计总计与系统性病灶诊断

### 7.1 全批 6 卡 P0 / P1 / P2 统计总表

| 序号 | 卡片 ID | P0 | P1 | P2 | 审计结论摘要 |
| :---: | :--- | :-: | :-: | :-: | :--- |
| 01 | [`DEB-1903-bolshevik-menshevik-split`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1903-bolshevik-menshevik-split.md) | 1 | 2 | 1 | `Arno Mayer`（实 `Robert Mayer`）+ 主编 Zelnik 误作 S. A. Smith 作者（P0）；缺冷战雅各宾连续论/当事人栏；漏引 1906 斯德哥尔摩党章反证、`RN-W22`、`EVT-1891-1903` 与已核第 23 次唱名票数 |
| 02 | [`DEB-1914-haimson-thesis-stability`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1914-haimson-thesis-stability.md) | 2 | 2 | 1 | `Dmitrii Gaida`（实 `Fedor Gaida`）（P0）；止于 1901/1903 的洛吉诺夫卡错塞入 Steinberg/Hoffmann 栏（P0）；漏用海姆森 2005 专著（`RN-W29`）、Hogan、`DATA-01`/`DATA-07` 与新建 `EVT-1907-1914`/`EVT-1914-1916` |
| 03 | [`DEB-1917-dual-power-and-february-origins`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-dual-power-and-february-origins.md) | 1 | 2 | 1 | `Dmitrii Gaida`（实 `Fedor Gaida`）（P0）；Hasegawa 2018 废黜杜马悖论 vs Gaida 叹气革命者交锋失焦；Figes 卡时域实为 3–10 月；`core_cards` 漏 `CON-dual-power`/临时政府/苏维埃/`EVT-1914-1916`；T3 漏 4 篇札记与 3 月 3 日闭环 |
| 04 | [`DEB-1917-july-days-spontaneity-vs-conspiracy`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-july-days-spontaneity-vs-conspiracy.md) | **0** | 2 | 1 | **全批最佳卡（0 P0）**：对 Pipes、Rabinowitch、Galili、Boll 均具实质原文对读；仅第 5 行匿名挂苏汉诺夫四月卡且空心化洛吉诺夫七月发现（P1），漏 `DATA-01`/`CON-dual-power`/孟什维克与社革党节点（P1），`但→丹` 笔误及 7 月 4 日下午 5 时偏差（P2） |
| 05 | [`DEB-1917-october-coup-or-social-revolution`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1917-october-coup-or-social-revolution.md) | 1 | 2 | 1 | 拉比诺维奇行匿名混挂洛吉诺夫 2017 卡并掩盖二者“等待大会 vs 先行出击”张力（P0）；漏引 Basil/姚海（维克热尔与立宪会议）、Blanc（边疆）；T3 漏 6+ 札记与 `DATA-01`/`DATA-07`；`core_cards` 缺二大/法令/立宪会议等核心节点 |
| 06 | [`DEB-1918-red-terror-and-civil-war-origins`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md) | 2 | 2 | 1 | 主编 Raleigh 误作德拉诺·杜加姆作者（P0）；圣彼得堡史家拉特科夫斯基（Igor Ratkovsky）被拆进两行并双重错名为“契卡编年史”和“A. M. Plekhanov”（P0）；矩阵漏马尔托夫/拉德基/丘拉科夫/Mawdsley/Zemskov；T3 漏 `DATA-06`；`core_cards` 漏红恐/内战事件卡与契卡机构卡 |
| **合计** | **Wave 39 `DEB-*` Batch 1（6 张）** | **7** | **12** | **6** | **全批共 25 项修复动作（7 P0 / 12 P1 / 6 P2）；机械链接与双历换算零失误，P0 高度集中于“望文件名猜作者／未打开 CLM 正文核读”** |

### 7.2 跨卡系统性病灶诊断（供 Wave 39 Batch 2 及后续修复参照）

1. **核心 P0 病灶：仅凭 `CLM-*` 文件名前缀推断作者与时域，未逐一打开论断卡 YAML 与正文**
   - 7 项 P0 竟有 **100%（7/7）** 源自同一工作流捷径：
     - **编者误作作者（2 例）**：`CLM-zelnik-1999-*`（实为 S. A. Smith）与 `CLM-raleigh-2001-*`（实为 Delano Dugarm）；
     - **俄国／西方学者错名与分身（4 例）**：`CLM-mayer-1999-*` 幻觉为 `Arno Mayer`（实 `Robert Mayer`）、`CLM-gaida-2003-*` 两度幻觉为 `Dmitrii Gaida`（实 `Fedor Gaida`）、`CLM-cheka-chronicle-*` 与 `CLM-plekhanov-am-*` 将同一作者 `Igor Ratkovsky (2017)` 拆成两个错误身份；
     - **跨作者／跨时域静默混挂（2 例，1 P0 + 1 P0 叠加）**：将止于 1901/1903 的洛吉诺夫卡 `CLM-lenin-leader-organizational-ascendancy-pre1914` 塞进 Steinberg/Hoffmann 栏（02-02），以及将洛吉诺夫 2017 卡匿名塞进拉比诺维奇栏（05-01）。
   - 反例印证：唯一明显真正逐章核读了单行本与 `CLM-*` 正文的 **04 号卡（七月事变）** 实现了 **0 P0**，证明问题并非能力上限而是写作节奏中跳过了“先读后挂”铁律。
2. **高频 P1 病灶（一）：站内已编译定量数据卡（`DATA-01`、`DATA-06`、`DATA-07`）与关键精读札记系统性漏引**
   - 6 张卡在 T3 锚点中竟然**零次完整挂载 `DATA-01`、`DATA-06`、`DATA-07`**（即便 04 号卡正文提到了 `DATA-01`、02/05/06 号卡把罢工、立宪会议选票、契卡处决统计列为“外部缺口”）。
   - 约 20 余篇已入库精读札记（如 `RN-W29` 海姆森 2005 晚年专著、`RN-W22` Mayer/Zelnik、`RN-W32` Hogan/Koenker/Spitsyn、`RN-W18` Basil、`RN-W36` 姚海与雅各宾谱系）均漏列于对应卡 T3。
3. **高频 P1 病灶（二）：矩阵摘要抽象化导致“学派间正面交锋”失焦，且屡屡遗漏温和社会主义／反证档案维度**
   - 例如 01 漏 1906 斯德哥尔摩党章反证与冷战雅各宾连续论、02 抹平 Bonnell 对海姆森“半农民新兵论”的直接反驳、03 抹平 Hasegawa 2018 废黜杜马悖论 vs Gaida 叹气革命者的正面对立、05 漏维克热尔与立宪会议合法性冲突、06 漏马尔托夫哈勒演说与丘拉科夫工人抗议。
4. **高频 P1 病灶（三）：`core_cards` 覆盖偏窄，与新建事件卡及母概念／母机构卡断联**
   - 03 漏 `CON-dual-power` 与临时政府／苏维埃卡、06 漏红恐／内战事件卡与 `INS-cheka-gpu-ogpu`；且刚新建的 `EVT-1891-1903`、`EVT-1907-1914`、`EVT-1914-1916` 虽已正向挂接 01–03 号 `DEB-*`，本批争鸣卡却均未双向回链。
5. **正面亮点（须保留）**：
   - 全批 6 卡**零断链 ID、零断链相对路径、`[T1]` 全部 111–115 字严守 ≤150 字红线、全部双历 `+13` 换算与西欧公历／1918-02-14 后纯公历规则 100% 精确**；
   - 方法论反思普遍克制清醒（如区分经验事实与反事实／价值判断、标出 B 级当事人回忆录局限、拒绝以 1937 大清洗倒推 1918 或将战时紧急措施合理化为常态）。

---

## 八、汇总修复动作矩阵（按 P0 → P1 → P2 优先级排程）

| 优先级 | 编号 | 目标卡片 | 定位行 | 具体修复动作（可直接派发给写入代理逐条销项） |
| :---: | :---: | :--- | :---: | :--- |
| **P0** | `01-01` | `DEB-1903-bolshevik-menshevik-split` | L29 | 将 `Reginald Zelnik 与 Arno Mayer 的研究` 更正为 `S. A. Smith (1996/1999，收入 Reginald E. Zelnik 编论文集)；Robert Mayer (1999)`，并按两卡原文修正摘要 |
| **P0** | `02-01` | `DEB-1914-haimson-thesis-stability` | L29 | 将 `Dmitrii Gaida (2003)` 更正为 `Fedor Gaida (2003)`（`SCH-gaida-fedor`） |
| **P0** | `02-02` | `DEB-1914-haimson-thesis-stability` | L30 | 从 Steinberg/Hoffmann 行彻底移除仅覆盖 1870–1901/1903 的 `CLM-lenin-leader-organizational-ascendancy-pre1914`；将姚海 `CLM-yao-hai-1917-modernization-rupture-and-plebeian-radicalism` 显式署名并补挂 `RN-W36` |
| **P0** | `03-01` | `DEB-1917-dual-power-and-february-origins` | L27 | 将 `Dmitrii Gaida (2003)` 更正为 `Fedor Gaida (2003)`（`SCH-gaida-fedor`） |
| **P0** | `05-01` | `DEB-1917-october-coup-or-social-revolution` | L27 | 将 `CLM-loginov-lenin-1917-fleeting-window-of-power` 从 Rabinowitch 行移出，单列 `Vladlen Loginov (2017)`（T3 补挂 `RN-W12B`），凸显“等待二大 vs 先行夺权窗口”的分歧 |
| **P0** | `06-01` | `DEB-1918-red-terror-and-civil-war-origins` | L27 | 将 `CLM-raleigh-2001-local-bolshevik-violence-and-clientelism` 署名由 `Donald Raleigh (2001)` 更正为 `Delano Dugarm (2001，收入 Donald J. Raleigh 编论文集)` |
| **P0** | `06-02` | `DEB-1918-red-terror-and-civil-war-origins` | L27, L29 | 合并并更正被拆成两行的同一学者：`CLM-cheka-chronicle-hostage-and-local-autonomy`、`CLM-cheka-chronicle-suppression-of-socialist-rivals` 与 `CLM-plekhanov-am-dzerzhinsky-cheka-institutionalization` 统一归入 `Igor Ratkovsky (2017，依托 A. M. & A. A. Plekhanov 2007 档案集)`，与 `O. B. Mozokhin` 清晰区分 |
| **P1** | `01-02` | `DEB-1903-bolshevik-menshevik-split` | L12, L23-29, L32 | `[T2]` 增设“冷战自由派／雅各宾连续论”行（Chamberlin 1958、Pipes 1990，挂靠 `CLM-jacobin-ancestry-tkachev-blanqui-and-leninism`、`CLM-pipes-1990-patrimonial-state-and-intelligentsia`）；T3 补充 1938《简明教程》将“新型政党”定于 1912 而非 1902 的史学层次 |
| **P1** | `01-03` | `DEB-1903-bolshevik-menshevik-split` | L10, L21, L34, L36 | L21 补入第 23 次会议唱名票数与崩得/三人编委口径差；T3 补引 `1906-04_rsdlp-fourth-stockholm-congress-rules.md`、`RN-W22`、`RN-W32`（Smith）、`RN-W36`；收窄外部缺口；`core_cards` 增补 `EVT-1891-1903-witte-industrialization-and-marxist-labor-turn`、`MTG-1906-04-rsdlp-4th-stockholm-congress`、`ORG-bund` |
| **P1** | `02-03` | `DEB-1914-haimson-thesis-stability` | L26-29, L35, L37 | 海姆森行补引 `RN-W29` §1.3（2005 晚年专著及 Appendix II 自我修正）；Bonnell 行补写“验证战前激进化、反驳半农民新兵论”；Pipes 行补齐“反必然论／职业革命家驱动”；增补“乐观现代化派”对照说明 |
| **P1** | `02-04` | `DEB-1914-haimson-thesis-stability` | L11, L35, L37 | 补引 `CLM-hogan-1994-petersburg-metalworkers-1905-to-lena`；T3 补列 `DATA-01`、`DATA-07`、`RN-W29`、`RN-W32`、`RN-W10`、`RN-W17` 并收窄外部缺口；`core_cards` 回链新建 `EVT-1907-1914-june-third-regime-and-lena-to-july-strikes` 与 `EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc` |
| **P1** | `03-02` | `DEB-1917-dual-power-and-february-origins` | L26-27, L30-31 | 重写 Hasegawa 2018（废黜杜马导致双重政权悖论）与 Gaida 2003（“叹着气的革命者”／塔夫利达宫物理场所胜利）对立；对 `CLM-figes-1996-soldier-mutiny-and-social-inversion` 加注“主论 3–10 月军纪瓦解”，反驳二月阴谋论归口 Hasegawa/Gaida；Galili 栏增引 `RN-W5` 第二章 |
| **P1** | `03-03` | `DEB-1917-dual-power-and-february-origins` | L11, L22, L36 | `core_cards` 增补 `CON-dual-power`、`ORG-provisional-government`、`ORG-petrograd-soviet`、`PER-nicholas-ii`、`EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc`；L22 补 3 月 3 日 [O.S.] 米哈伊尔拒位闭环；T3 补 `RN-W5`（Galili/Figes）、`RN-W7`（Trotsky, B 级）、`RN-W32`（Spitsyn, B 级） |
| **P1** | `04-01` | `DEB-1917-july-days-spontaneity-vs-conspiracy` | L30, L35 | 充实洛吉诺夫行：补入 `RN-W12B` 中列宁视 7 月 3 日“不合时宜”、7 月 10 日提纲及 7 月 13–14 日中央扩大会议否决列宁方案之硬证；将苏汉诺夫四月卡移出或显式署名并标 B 级 |
| **P1** | `04-02` | `DEB-1917-july-days-spontaneity-vs-conspiracy` | L11, L35 | T3 补列 `DATA-01`、`RN-W18`（Basil）、`RN-W29`（Haimson）；`core_cards` 增补 `CON-dual-power`、`ORG-mensheviks`、`ORG-psr`、`PER-chernov`、`PER-tsereteli` |
| **P1** | `05-02` | `DEB-1917-october-coup-or-social-revolution` | L26-31, L34 | `[T2]` 补挂 Basil (`CLM-basil-1984-october-and-vikzhel-collapse`)、姚海（维克热尔与立宪会议两卡）、Rabinowitch 立宪会议卡、Blanc (`CLM-blanc-2021-borderlands-in-1905-and-1917`)；充实 Pipes（马拉帕尔泰／针对全国苏维埃的政变）、Koenker（拒冒内战／政策先于党派）与 Sukhanov（反对者证言反驳纯军事阴谋）摘要 |
| **P1** | `05-03` | `DEB-1917-october-coup-or-social-revolution` | L11, L36, L38 | T3 补列 `DATA-01`、`DATA-07` 及 `RN-W32`（Koenker）、`RN-W7`、`RN-W6`、`RN-W5`、`RN-W12B`、`RN-W18`、`RN-W36`、`RN-W11` 并收窄立宪会议外部缺口；`core_cards` 补 `MTG-1917-10-2nd-congress-of-soviets`、`POL-decrees-on-peace-and-land-1917`、`ORG-provisional-government`、`CON-constituent-assembly`、`EVT-1918-01-constituent-assembly-dispersal`、`ORG-vikzhel`、`ORG-factory-committees-1917`、`CON-workers-control` |
| **P1** | `06-03` | `DEB-1918-red-terror-and-civil-war-origins` | L24-29, L32 | `[T2]` 补挂 Martov（`CLM-halle-1920-martov-critique-of-terror-and-21-conditions`, S 级）、Radkey（`CLM-smith-scott-2011-psr-third-force-collapse`）、Churakov（1918 工人抗议两卡）、Mawdsley（`CLM-mawdsley-1987-civil-war-militarized-regime`）、Zemskov（`CLM-zemskov-1920s-archival-repression-scale-before-1930`）；充实 Pipes、Leggett、Rabinowitch（5 万→6,000、12 月撤案）、Mozokhin（战时 vs 1922 后和平期二分法） |
| **P1** | `06-04` | `DEB-1918-red-terror-and-civil-war-origins` | L9, L20, L34, L36 | `core_cards` 补 `EVT-1918-09-red-terror-and-left-sr-rupture`、`EVT-1918-1920-russian-civil-war`、`INS-cheka-gpu-ogpu`、`MTG-1918-07-5th-congress-of-soviets`、`EVT-1918-03-brest-litovsk-treaty`、`EVT-1918-worker-protest-and-izhevsk-uprising`、`PER-spiridonova`；T3 补 `DATA-06` 及 `RN-W4B`/`RN-W32`/`RN-W15`/`RN-W17`/`RN-W9`/`RN-W23`/`RN-W6`/`RN-W22`；L20 补注 9 月 4 日人质令与 9 月 5 日法令签署人校勘 |
| **P2** | `01-04` | `DEB-1903-bolshevik-menshevik-split` | L4-8, L21 | L21 补二大会期俄历对照（`1903-07-17` 至 `08-10 [O.S.]`），注清 `era: 1902-1904` 范围与 `participant` 依托 |
| **P2** | `02-05` | `DEB-1914-haimson-thesis-stability` | L6-8 | 注释说明 `end_os: 07-18 / end_ns: 07-31`（总动员前夜）与 `EVT-1907-1914` 终点 `07-19 / 08-01` 的 1 日口径差，或直接对齐 |
| **P2** | `03-04` | `DEB-1917-dual-power-and-february-origins` | L36-38 | 顺注列宁 4 月 9 日 [O.S.]《论两个政权》尚属站内原典缺口，衔接外部补核清单 |
| **P2** | `04-03` | `DEB-1917-july-days-spontaneity-vs-conspiracy` | L22, L28 | 修正 L28 `但与齐赫伊泽` → `丹（F. I. Dan）与齐赫伊泽`；L22 佩列韦尔泽夫放风由“深夜”更正为“7 月 4 日下午约 5 时（次晨见报）”，并补 7 月 3–5 日公历对照 |
| **P2** | `05-04` | `DEB-1917-october-coup-or-social-revolution` | L5, L29, L36 | 注释 `era: 1917-1918` 延伸至立宪会议解散；显式标明托洛茨基（1930）与苏汉诺夫（1922）为 B 级当事人文献 |
| **P2** | `06-05` | `DEB-1918-red-terror-and-civil-war-origins` | L4-8, L20 | 统一 `title (1918–1921)`、`era (1917-1918)` 与 `dates (1918-07-06..09-05)` 三处时域口径 |

