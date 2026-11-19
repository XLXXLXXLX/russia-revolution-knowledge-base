# AUD-18B｜第40波 Codex 升格 `DEB-*` 史学争鸣卡异源交叉审计报告（第二批 6 张，1920—1929）

- **审计日期**：2026-11-19
- **审计角色**：`dialectic-auditor`（跨模型家族异源交叉审计：Google `gemini-4-neon` 审读 OpenAI `gpt-6.1-terra` 在 Wave 40 升格的第二批 6 张 `DEB-*` 史学争鸣卡，1920—1929）。
- **唯一写入目标**：[`audits/AUD-18B-wave40-codex-deb-batch2-audit.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-18B-wave40-codex-deb-batch2-audit.md)；纯只读审计，未改动任何被审争鸣卡、实体卡、论断卡、札记或共享图谱文件。
- **审计对象（两阶段增量落盘）**：
  - **阶段一（01–03，本节已完成）**：
    1. [`DEB-1920-polish-war-and-revolutionary-export`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920-polish-war-and-revolutionary-export.md)
    2. [`DEB-1920s-gender-family-and-everyday-life`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920s-gender-family-and-everyday-life.md)
    3. [`DEB-1921-trade-union-controversy-and-party-unity`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md)
  - **阶段二（04–06 与全批汇总修复矩阵，本节已完成）**：
    4. [`DEB-1924-socialism-in-one-country`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1924-socialism-in-one-country.md)
    5. [`DEB-1928-bukharin-alternative`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1928-bukharin-alternative.md)
    6. [`DEB-1929-collectivization-and-dekulakization-causes`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md)

---

## 一、审计方法、判级准则与全 6 卡机械体检基线

1. **判级准则**（严格沿用 [`AUD-18A`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-18A-wave39-codex-deb-batch1-audit.md) 标准）：
   - **P0**：史实／日期硬伤、断链／悬空节点 ID、张冠李戴（望文件名猜作者名／把论文集主编或匿名汇编误作单篇作者／错植书名卷号／跨作者静默混挂 `CLM-*`）、无中生有歪曲或杜撰学者论断卡中并不存在的论点；
   - **P1**：站内已有 S/A 级原典、定量数据卡（`data/DATA-01..08`）或 Wave 39 新增精读札记漏引、把站内已可核事项笼统归入“外部待补核缺口”、学派矩阵失衡或抹平关键交锋、`core_cards` 核心节点及双向互链漏挂；
   - **P2**：Schema 字段细节、`era` 与 `dates` 边界注释、`[T1]` 字数或措辞微瑕。
2. **核验手段**：
   - (a) 只读 Python 脚本全量扫描 6 张卡的 YAML 字段、`core_cards` 存在性及双向互链、`[T1]` 字数（模板上限 `<= 150` 字）、全部正文反引号节点 ID 与 T3 `.md` 相对路径；
   - (b) 核验 1918 年后公历日期规范与 `<= 1929` 知识库分期红线；
   - (c) **逐一打开每一张被挂接的 `CLM-*` 及对应 `RN-*`、原典档案、Wave 39 新增馆藏与 `data/DATA-01..08` 数据卡逐字对勘**。

### 1.1 全 6 张 `DEB-*` 卡机械体检总表（只读 Python 脚本实测）

| 序号 | 卡片 ID | YAML 必填键 | `core_cards` 命中/断链 | `[T1]` 字数（≤150） | 正文反引号 ID 命中/断链 | T3 `.md` 路径命中/断链 | `era` / `dates` |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 01 | `DEB-1920-polish-war-and-revolutionary-export` | 齐全 | 7 / 0 | 126（合格） | 5 / 0 | 5 / 0 | `1920-1921` / `1920-04-25`..`1921-03-18` |
| 02 | `DEB-1920s-gender-family-and-everyday-life` | 齐全 | 3 / 0 | 125（合格） | 9 / 0 | 4 / 0 | `1917-1929` / `1918-01-01`..`1929-12-31` |
| 03 | `DEB-1921-trade-union-controversy-and-party-unity` | 齐全 | 9 / 0 | 122（合格） | 6 / 0 | 6 / 0 | `1920-1929` / `1920-11-01`..`1921-03-16` |
| 04 | `DEB-1924-socialism-in-one-country` | 齐全 | 8 / 0 | 123（合格） | 9 / 0 | 6 / 0 | `1924-1927` / `1924-01-01`..`1927-12-19` |
| 05 | `DEB-1928-bukharin-alternative` | 齐全 | 10 / 0 | 121（合格） | 12 / 0 | 8 / 0 | `1927-1929` / `1927-10-01`..`1929-11-17` |
| 06 | `DEB-1929-collectivization-and-dekulakization-causes` | 齐全 | 7 / 0 | 119（合格） | 13 / 0 | 7 / 0 | `1927-1929` / `1927-10-01`..`1929-12-31` |

> **全批机械体检结论**：6 张卡**无任何断链 ID、无任何断链 `.md` 路径、`[T1]` 字数全部严格落在 119–126 字之间**，全段处于 `1918-02-14` 后纯公历阶段且严格守住 `<= 1929` 分期上限；但逐一打开全部 53 次引用的 `CLM-*` 原文对勘后，**全批共检出 4 处 P0（分布于 02、04、06 三张卡；01、03、05 三张卡为 0 P0）、13 处 P1 与 6 处 P2**。相比首批 [`AUD-18A`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-18A-wave39-codex-deb-batch1-audit.md)（7 P0 / 5 卡），Codex 的硬伤密度已明显下降，但“望文件名猜书名／卷号／编者”及“为贴合卡片主题而改写或拉平论断卡原旨”仍是复发核心病灶。

---

## 二、阶段一（01–03）历法、时域与 `<= 1929` 分期边界核查表

| 卡片 | 卡内日期（YAML／正文） | 历法与 `<= 1929` 边界核查 | 判定 |
| :--- | :--- | :--- | :--- |
| 01 `DEB-1920-polish-war-and-revolutionary-export` | YAML：`start_ns: 1920-04-25`（波军基辅攻势）、`end_ns: 1921-03-18`（里加和约）；`era: 1920-1921`；正文：1920-07-24 斯大林信、1920-08 华沙败退 | 全段属 1918-02-14 后纯公历，日期准确，无越界 | **历法合规**；L26 援引季诺维也夫哈雷演说（1920-10-14）未注明其发生于华沙战败两月后（P2） |
| 02 `DEB-1920s-gender-family-and-everyday-life` | YAML：`start_ns: 1918-01-01`、`end_ns: 1929-12-31`；`era: 1917-1929`；正文：1918 与 1926 婚姻法、1920 堕胎合法化 | 主体属 1918—1929 纯公历且守住 `<= 1929` 边界（未把 1930-01 妇女部撤销或 1936 禁堕胎写成本期事实） | **存在 `era` 与 `start_ns` 错位**：标题与 `era` 写作 `1917-1929`，但 `start_ns: 1918-01-01` 排除了 1917-12 民事婚姻与离婚法令及二月女工罢工，宜注释或对齐（P2） |
| 03 `DEB-1921-trade-union-controversy-and-party-unity` | YAML：`start_ns: 1920-11-01`、`end_ns: 1921-03-16`；`era: 1920-1929`；正文：1920 年底工会争论、1921 年 3 月十大、1928—1929 年工会转向 | 全段属纯公历，日期无误，守住 `<= 1929` 边界 | **`era` 与 `dates` 跨度差异宜补注**：`dates` 锚定 1920-11 至 1921-03-16 十大闭幕，`era` 涵盖至 1929 托姆斯基倒台（P2） |

---

## 三、阶段一逐卡深度审计与修复方案（01–03）

### 01｜1920年苏波战争与武装输出革命之争（`DEB-1920-polish-war-and-revolutionary-export`）

**总体评价**：所引 5 张 `CLM-*` 的学者姓名与出版年份**全部核对准确（0 P0）**——尤其正确识别出 `CLM-stalin-war-1920-polish-war-lessons` 背后作者为 **David R. Shearer (2024)** 而未落入望文件名生义的陷阱。但存在 **2 项重要 P1**：一是漏引站内已有且与 Shearer 针锋相对的 **Oleg Khlevniuk (2015)** 对斯大林 1920 年 7 月 13 日与 24 日电报的档案拆穿，并错把 `RN-W6`/`RN-W20` 当作 T3 锚点而漏掉真正对应的 `RN-W22`/`RN-W1C`/`RN-W24` 与 `DATA-05`；二是 5 张挂接 `CLM-*` 中有 4 张系宏观外延卡而非 1920 年波兰战役直击材料（漏引 Mawdsley 专著第 18 章），且简写托洛茨基立场并漏挂 4 张相关核心卡。

#### 01-01｜P1｜漏引站内 Khlevniuk（2015）对斯大林 1920-07 电报的直接反证、错配 T3 札记锚点，并漏引 `RN-W24` 与 `DATA-05`
- **定位**：[`DEB-1920-polish-war-and-revolutionary-export.md:25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920-polish-war-and-revolutionary-export.md#L25)、[`L31`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920-polish-war-and-revolutionary-export.md#L31)、[`L33`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920-polish-war-and-revolutionary-export.md#L33)。
- **核证**：
  1. **漏引与 Shearer (2024) 针锋相对的站内 A 级反证（Khlevniuk 2015）**：矩阵第 2 行（L25）仅呈现 David Shearer (2024) 强调斯大林在 7 月 24 日信中预警过度扩张、偏向以地缘防御吸取教训的解读（[`CLM-stalin-war-1920-polish-war-lessons.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-stalin-war-1920-polish-war-lessons.md)）；而站内已有专著原文 [`sources/monographs/khlevniuk_2015_stalin/ch06_2_in_lenin_s_shadow.md:138-175`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/khlevniuk_2015_stalin/ch06_2_in_lenin_s_shadow.md#L138-L175)（亦已在 [`PER-tukhachevsky.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-tukhachevsky.md) 摘要）证明：斯大林 1920 年 7 月 13 日致列宁电报与 7 月 24 日后续电报其实热烈鼓吹以红军刺刀在意大利、匈牙利、捷克斯洛伐克掀起起义并粉碎罗马尼亚，只是在 9 月 23 日第九次党代表会议上为了推卸华沙失利责任才**谎称自己一贯审慎**！两组权威档案解读的正面碰撞正是“斯大林究竟是现实主义谨慎派还是事后甩锅者”的核心争点，本卡完全未提。
  2. **T3 锚点存在“错配对应札记”**：
     - 矩阵挂了 `CLM-carr-1953-dual-foreign-policy-rapallo-comintern`（来自 `RN-W22`）与 `CLM-kotkin-2014-geopolitics-and-ideology`（来自 `RN-W1C`），但 T3 L33 **两者对应的源札记均未列入**，反而列了只讲 1923–1924 *The Interregnum* 的 `RN-W6-interregnum-and-nep-crisis.md` 和只讲 1919 年内线作战的 `RN-W20-red-army-interior-lines-and-civil-war-logistics.md`；
     - 同时漏引站内已有斯大林 1920-08-19 政治局密信与内战指挥风格论断卡 [`CLM-stalin-docs-tsaritsyn-and-civil-war-command-style.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-stalin-docs-tsaritsyn-and-civil-war-command-style.md)（[`RN-W24-stalin-pre1930-archival-docs-and-archaic-rebellion.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/stalin_docs_hobsbawm/RN-W24-stalin-pre1930-archival-docs-and-archaic-rebellion.md)）及站内军力基线数据卡 [`DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md)。
- **修复**：在 `[T2]` 斯大林／战略教训一行（或新增“档案传记与甩锅叙事解构”一行）并列 Oleg Khlevniuk (2015) 与 David Shearer (2024) 对 7 月 13 日／24 日电报的对立解读；在 T3 补挂 `RN-W22-soviet-dual-diplomacy-and-comintern-sixth-congress-turn.md`、`RN-W1C-1928-siberian-turn-and-bukharin.md`、`RN-W24-stalin-pre1930-archival-docs-and-archaic-rebellion.md`、`ch06_2_in_lenin_s_shadow.md` 与 `DATA-05`，移除或说明 `RN-W6`/`RN-W20` 仅作外围背景。

#### 01-02｜P1｜5 张所引 `CLM-*` 中 4 张为间接外延卡（漏引 Mawdsley 第 18 章战役硬数据）、托洛茨基立场被单线化，且 `core_cards` 漏挂 4 节点
- **定位**：[`L9`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920-polish-war-and-revolutionary-export.md#L9)、[`L24-28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920-polish-war-and-revolutionary-export.md#L24-L28)、[`L31`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920-polish-war-and-revolutionary-export.md#L31)。
- **核证**：
  1. **间接代挂过多而漏引站内直击战役原文**：除 `CLM-stalin-war-1920-polish-war-lessons` 外，其余 4 张卡（`CLM-mawdsley-1987-civil-war-militarized-regime`、`CLM-halle-1920-zinoviev-world-revolution-speech`、`CLM-carr-1953-dual-foreign-policy-rapallo-comintern`、`CLM-kotkin-2014-geopolitics-and-ideology`）均未专门讨论 1920 年波兰战役的作战序列与政治局表决。而站内已完整收有 Mawdsley 专著第 18 章 [`sources/monographs/mawdsley_1987_civil_war/ch24_18_the_polish_campaign_april_october_192.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/monographs/mawdsley_1987_civil_war/ch24_18_the_polish_campaign_april_october_192.md)，内含关键经验硬指标：波兰正规军达 74 万人而图哈切夫斯基西方面军推进至维斯瓦河时一线兵力由 10.8 万跌至约 4 万人（全红军纸面 460 万却深陷后勤与弗兰格尔双线牵制）；7 月 17 日政治局表决越过寇松线时仅李可夫一人公开反对；7 月 23 日总司令 С. С. 加米涅夫指令西南方面军转攻利沃夫；8 月 13 日斯大林拒签移交骑兵第 1 集团军命令；8 月 19 日政治局转而优先歼灭弗兰格尔。
  2. **托洛茨基立场被单线化**：L31 笼统称“列宁与托洛茨基支持继续作战”，未体现学界关于托洛茨基真实态度的长期争议（托洛茨基本人在 1920 年代末流亡回忆中宣称自己一开始反对跨过寇松线，而 Mawdsley 与 Service 等学者考证其在 7 月 17 日政治局决议后实际配合执行并在 8 月下旬华沙惨败后力主尽快议和）。
  3. **`core_cards` 漏挂**：已有双向回链的 [`EVT-1917-1920-ukrainian-revolution-rada-hetmanate-and-sovietization`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1917-1920-ukrainian-revolution-rada-hetmanate-and-sovietization.md) 与 [`PER-wrangel`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-wrangel.md) 未列入 `core_cards`；波兰临时革命委员会成员及 1926 年波兰安全论证核心 [`PER-dzerzhinsky`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-dzerzhinsky.md)、以及战败直接催生的 [`CON-socialism-in-one-country`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-socialism-in-one-country.md) 亦建议补入。
- **修复**：在经验基准与 T3 补充 Mawdsley 第 18 章兵力与 7 月 17 日／23 日／8 月 13 日／19 日决策节点；细化托洛茨基“事后自述反对 vs 战时执行与 8 月主和”的史料分歧；补齐 `core_cards`。

#### 01-03｜P2｜哈雷演说时间定位与斯大林 7 月 24 日信件分歧提示不足
- **定位**：[`L26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920-polish-war-and-revolutionary-export.md#L26)、[`L31`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920-polish-war-and-revolutionary-export.md#L31)。
- **核证**：L26 引用季诺维也夫哈雷演说（1920-10-14）时未点明它发生于华沙惨败之后两个月、说明布尔什维克领导层即使在波兰受挫后仍试图在德国独立社会民主党大会上动员西欧革命；L31 提及斯大林 7 月 24 日信件时未标注 Shearer 与 Khlevniuk 对同一组电报截然相反的解释。
- **修复**：在 L26 与 L31 各补一句限定说明。

---

### 02｜1920年代性别政策、家庭改革与日常生活史（`DEB-1920s-gender-family-and-everyday-life`）

**总体评价**：Goldman（1993）与 Wood（1997）的经典双峰框架搭建清楚，但**出现了本批阶段一唯一且最典型的 P0 病灶**：矩阵第 3–5 行连续三行“望文件名生义”漏写三位真实学者全名与书名，更严重的是把 Maksim Lebsky 关于“工业家长制与厂房福利绑定”的一般劳工史论断卡**凭空改写成了“妇女托育与就业需求受工作场所权力制约”的性别论点**！同时漏挂了 Wave 39 刚精读入库的苏联正统工业女工专著 `RN-W39-arapovich`（2 张直指本卡的 `CLM-*`）、定量中枢 `DATA-08` 以及克鲁普斯卡娅的去性别化教育卡，且 `core_cards` 仅 3 项，系全批最单薄。

#### 02-01｜P0｜连续 3 行“望文件名生义”隐去真实作者／书名，且为 Maksim Lebsky 凭空杜撰论断卡中并不存在的性别托育论点
- **定位**：[`DEB-1920s-gender-family-and-everyday-life.md:25-27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920s-gender-family-and-everyday-life.md#L25-L27)（矩阵第 3、4、5 行）。
- **核证**：逐一打开三行对应的 `CLM-*` 原文：
  1. **L25（第 3 行）**：卡片仅据文件名 `CLM-soviet-women-zhenotdel-mobilization-and-liquidation-1919-1930` 笼统写作“**`Soviet Women 相关研究；妇女部史`**”，隐去了真实作者与著作——[`CLM-soviet-women-zhenotdel-mobilization-and-liquidation-1919-1930.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-soviet-women-zhenotdel-mobilization-and-liquidation-1919-1930.md#L4-L6) 明确标明作者为 **`William M. Mandel`**（1975，*Soviet Women*，转引 Elena D. Emelyanova 1971 与 Sofia N. Smidovich 1927 统计）。更要紧的是，该卡第 48 行明确警告“Mandel 系 1970 年代亲苏美国左翼学者，毫无批判地采信了 1930 年官方撤销妇女部的‘任务已完成’说辞”，本卡矩阵不仅未标出 Mandel 的作者身份与史学倾向，反而把它标作中性“组织与动员史”。
  2. **L26（第 4 行）**：仅据文件名 `CLM-klots-*` 简写为“**`Klots, 苏联家务劳动研究`**”，遗漏了作者全名、出版年与原书名——[`CLM-klots-narpit-unionization-and-1926-labor-law-paradox.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-klots-narpit-unionization-and-1926-labor-law-paradox.md#L4-L6)（及同组 [`CLM-klots-communist-employers-and-gendered-labor-hierarchy.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-klots-communist-employers-and-gendered-labor-hierarchy.md)）明确为 **`Alissa Klots (2024), Domestic Service in the Soviet Union: Women's Emancipation and the Gendered Hierarchy of Labor`**。
  3. **L27（第 5 行，最严重：无中生有杜撰论点）**：仅据文件名 `CLM-lebsky-*` 简写为“**`Lebsky，工业家长主义研究`**”，既漏写全名与原书（**`Maksim Lebsky (2021), 《苏联的工人阶级：工业家长制下的生活》`**），又在“核心论点摘要”中硬写“**`企业福利与住房供给构成工业家长主义框架，妇女对托育与就业的需求受到工作场所权力关系制约`**”。查阅 [`CLM-lebsky-industrial-paternalism-origins-1917-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-lebsky-industrial-paternalism-origins-1917-1929.md) 全文（及源札记 [`RN-W35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/schapiro_1981_and_lebsky_workers/RN-W35-schapiro-vs-lebsky-soviet-trade-unions-and-industrial-paternalism-1917-1929.md)）可见：该论断卡讨论的是**全体工业工人的去阶级化、半农半工土地纽带（1918 年 31.3% → 1928 年 25%）、企业福利基金（ФУБР 75% 用于住房）以及 1920-07-13 与 1928-01-04 解雇即逐出宿舍法令**，全文**完全没有分析“妇女对托育与就业的需求”**（仅在一处列举“食堂、保育、公用住房”时顺带出现两字“保育”）。这属于为了迁就本卡性别主题而对所引论断卡进行的**跨主题杜撰**。
- **修复**：
  1. 第 3 行更正作者为 `William M. Mandel (1975), Soviet Women（援引 Emelyanova 1971、Smidovich 1927）`，并明确标示其亲苏左翼立场盲点（轻信 1930 年官方撤销妇女部说辞）；
  2. 第 4 行补全为 `Alissa Klots (2024), Domestic Service in the Soviet Union`；
  3. 第 5 行补全 `Maksim Lebsky (2021), 《苏联的工人阶级：工业家长制下的生活》`，将摘要如实改为“企业依托 ФУБР 福利基金（75% 投向住房）与解雇逐宿法令重塑工人生计依附，为理解 1920 年代家庭再生产与性别劳动所处的企业社会控制背景提供参照（该卡本身聚焦一般工人阶层，非专论性别托育）”。

#### 02-02｜P1｜漏挂 Wave 39 新增苏联正统女工专著 `RN-W39-arapovich`（2 张直指本卡 `CLM-*`）、定量中枢 `DATA-08`、Lynne Attwood 教育卡及 `RN-W35`
- **定位**：[`L11-12`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920s-gender-family-and-everyday-life.md#L11-L12)、[`L22-27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920s-gender-family-and-everyday-life.md#L22-L27)、[`L32`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920s-gender-family-and-everyday-life.md#L32)。
- **核证**：
  1. **漏挂 Wave 39 新增 `soviet-orthodoxy` 对照基线**：Wave 39 刚精读入库的 [`RN-W39-arapovich-women-industrial-labor-1917-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/women_labor_soviet_industry_zh/RN-W39-arapovich-women-industrial-labor-1917-1929.md) 及其 2 张直指本卡（`related_debates: ["DEB-1920s-gender-family-and-everyday-life"]`）的论断卡——[`CLM-arapovich-nep-female-employment-recovery-and-segregation.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-arapovich-nep-female-employment-recovery-and-segregation.md) 与 [`CLM-arapovich-1929-skills-quotas-and-heavy-industry-mobilization.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-arapovich-1929-skills-quotas-and-heavy-industry-mobilization.md)（B 级，扉页作者 `Н. Д. Арапович`，`publication_year: null`）完全未挂入本卡。该专著既提供正统叙事对照，又在内部统计中诚实承认：1925—1929 年女工占大工业比例停滞在 28.2%—28.6%、金属业女工约 3/4 属无技能工种、1929-04-15 决议及高校 ≥20% 配额启动重工业技能动员——与 Goldman、Klots 形成极佳的跨学派统计对勘！
  2. **漏引定量数据卡 `DATA-08`**：[`DATA-08-1921-1929-nep-social-classes-unemployment-and-gender-labor.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-08-1921-1929-nep-social-classes-unemployment-and-gender-labor.md) 的 §3（Goldman 表 7–8、莫斯科离婚率飙升至 `477.1‰`）、§4（Klots 452,258 名家政女工与 1926 年法令崩塌）、§5.2（ФУБР 福利）正是本争鸣的直接定量底座，本卡全文只字未提。
  3. **漏引 `RN-W28` 中的 Lynne Attwood（1987）与 `RN-W35`**：`core_cards` 挂了 `PER-krupskaya`，正文却未引站内已有的 [`CLM-soviet-citizen-lunacharsky-progressive-pedagogy-1920s.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-soviet-citizen-lunacharsky-progressive-pedagogy-1920s.md)（[`RN-W28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/paternalism_gender_education/RN-W28-industrial-paternalism-zhenotdel-and-soviet-pedagogy-1917-1929.md)，Lynne Attwood 论克鲁普斯卡娅 1920 年代去性别化教育与混合编班），使 `PER-krupskaya` 悬空；同时 `CLM-lebsky-industrial-paternalism-origins-1917-1929` 的真正母札记 [`RN-W35-schapiro-vs-lebsky-soviet-trade-unions-and-industrial-paternalism-1917-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/schapiro_1981_and_lebsky_workers/RN-W35-schapiro-vs-lebsky-soviet-trade-unions-and-industrial-paternalism-1917-1929.md) 也漏列入 T3。
- **修复**：在 `[T2]` 增设“苏联正统工业女工史（对照基线）”一行挂接 Arapovich 两张 `CLM-*`（须明确注记 B 级与 `publication_year: null`）；在 T3 补挂 `DATA-08`、`RN-W39-arapovich-women-industrial-labor-1917-1929.md`、`RN-W35` 及 Attwood 教育论断卡。

#### 02-03｜P1｜`core_cards` 仅 3 项（全批最薄），且抹平了 Klots 对托洛茨基与 Goldman 的尖锐史学反驳
- **定位**：[`L9`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920s-gender-family-and-everyday-life.md#L9)、[`L26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920s-gender-family-and-everyday-life.md#L26)。
- **核证**：
  1. `core_cards` 仅有 `["PER-kollontai", "PER-krupskaya", "POL-nep"]` 三张卡，漏挂了 1928—1929 年女工配额与重工业动员核心政策卡 [`POL-first-five-year-plan`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-first-five-year-plan.md)、以及参与 1920 年代家庭法／女工工会政策争论的 [`PER-tomsky`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-tomsky.md)（工会与女工组织）、[`PER-kalinin`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-kalinin.md)（1926 婚姻法辩论）。
  2. L26 对 Klots（2024）的摘要平淡泛化，漏掉了她对托洛茨基《被背叛的革命》与 Goldman“双重负担”范式的最锋利反驳：1920 年代城市知识女性与共产党员白领家庭（莫斯科家政雇主中白领占 77.8%，国家还以税率／社保倾斜相当于补贴了 2/3 雇佣成本）实际是把家务负担转嫁给了 **452,258 名农村进城家政女工**；1926-02-08 家政劳动法虽将其降格出普通劳动法保护，却通过工会与女工动员反讽地催生了女仆“逃离厨房”进入工厂的通道。
- **修复**：在 `core_cards` 增补 `POL-first-five-year-plan`、`PER-tomsky`、`PER-kalinin`；在 L26 精准浓缩 Klots 的“家务阶级转嫁”与“逃离厨房悖论”。

#### 02-04｜P2｜`era: "1917-1929"` 与 `dates.start_ns: "1918-01-01"` 存在一年缺口
- **定位**：[`L4-8`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1920s-gender-family-and-everyday-life.md#L4-L8)。
- **核证**：`era` 标为 `"1917-1929"`，但 `start_ns` 定为 `"1918-01-01"`，未将 1917-12-18/31 民事婚姻法令与 1917-12-19/1918-01-01 离婚法令纳入时间范围，也未在正文注明起点取 1918 年法典的原因。
- **修复**：建议将 `start_ns` 提前至 `"1917-12-31"`（首个民事婚姻法令公历日），或在经验基准明确注明“1917 年 12 月法令起草、1918 年法典成文化”。

---

### 03｜1921年工会争论、工人反对派与党内团结决议（`DEB-1921-trade-union-controversy-and-party-unity`）

**总体评价**：所引 6 张 `CLM-*` 的作者名、著作年份与引文口径**全部核对准确（0 P0）**，且 T3 L31 精准区分了《关于党的统一》第 7 条的“大会通过本”与“拟案提及派别名称之别”，颇具史料警觉。但存在 **2 项 P1**：一是矩阵第 2–4 行连着三行重复挂同一张 `CLM-daniels-1960-tenth-congress-turning-point`，漏挂了同在 T3 已引札记 `RN-W35` 中的 **Joseph Godson (1981)** 与 **Maksim Lebsky (2021)** 以及 **Robert Service (2009)** 的托洛茨基劳动军事化卡，削弱了 Schapiro—Filtzer—Lebsky 三方交锋；二是漏引 `DATA-04`（十大核心投票数据）与 `DATA-08`（全苏工会中央理事会党员化率），且 `core_cards` 漏挂 4 张已有回链的实体卡。

#### 03-01｜P1｜矩阵连续 3 行复用同一张 Daniels 卡，却漏挂 `RN-W35` 内的 Godson (1981) 与 Lebsky (2021) 以及 Service (2009)，抹平 Schapiro—Filtzer—Lebsky 三方交锋
- **定位**：[`DEB-1921-trade-union-controversy-and-party-unity.md:25-29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md#L25-L29)、[`L33`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md#L33)。
- **核证**：
  1. 矩阵第 2、3、4 行（L25–L27）竟然把同一张 [`CLM-daniels-1960-tenth-congress-turning-point`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-daniels-1960-tenth-congress-turning-point.md) 连续粘贴了三次，而 T3 L33 自己已经挂了 [`RN-W35-schapiro-vs-lebsky-soviet-trade-unions-and-industrial-paternalism-1917-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/schapiro_1981_and_lebsky_workers/RN-W35-schapiro-vs-lebsky-soviet-trade-unions-and-industrial-paternalism-1917-1929.md)，却遗漏了该札记产出的两张直击本主题的 A 级论断卡：
     - [`CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions.md)（**Joseph Godson 1981**，系统拆解列宁“共产主义学校／传动带”理论、民主集中制、工会内秘密党组与生产原则重组，正是第 2 行列宁多数派与工会职能定型的直接制度分析！）；
     - [`CLM-lebsky-industrial-paternalism-origins-1917-1929`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-lebsky-industrial-paternalism-origins-1917-1929.md)（**Maksim Lebsky 2021**，揭示企业福利／住房家长制如何构成 1920 年代工会与厂方关系的社会基底）；
     - 以及托洛茨基派路线的传记分析卡 [`CLM-service-2009-trotsky-authoritarian-consensus`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-service-2009-trotsky-authoritarian-consensus.md)（直接剖析托洛茨基 1920 年劳动军事化与工会国家化主张）。
  2. **三方制度史交锋被弱化**：Schapiro（1981，断言 1920-06 逮捕莫斯科印刷工会、1921 年初逮捕约 2,000 名孟什维克、1921-05 金属工会党团 `120:40` 否决中央名单却被强行推翻，独立工会早在 1920–1921 年即遭政治消灭）与 Filtzer（1986，论证基层评议冲突委员会 RKK 与车间讨价还价持续至 1928-12 至 1929-05 托姆斯基倒台及 1929-03-06 厂长单方解雇令）、Lebsky（2021，企业家长制住房绑定）之间的“1921 终结论 vs 1928–29 断裂论 vs 福利依附论”本是极具穿透力的三足鼎立，目前矩阵仅把 Schapiro 与 Filtzer 轻轻并排而丢掉了核心经验节点与 Lebsky 第三维。
- **修复**：第 2 行补挂 `CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions`；第 3 行补挂 `CLM-service-2009-trotsky-authoritarian-consensus`；在劳工制度史部分纳入 `CLM-lebsky-industrial-paternalism-origins-1917-1929` 并显化 Schapiro（1920–21 政治终结）vs Filtzer（1928–29 车间终结）vs Lebsky（企业家长制依附）三方交锋。

#### 03-02｜P1｜漏引定量数据卡 `DATA-04`（十大实证票数）与 `DATA-08`（工会党员化率），且 `core_cards` 漏挂 4 张双向回链卡与 3 张关键节点卡
- **定位**：[`L9`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md#L9)、[`L20`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md#L20)、[`L33`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md#L33)。
- **核证**：
  1. **漏引 `DATA-04` 与 `DATA-08`**：[`DATA-04-party-membership-and-congress-votes-1903-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-04-party-membership-and-congress-votes-1903-1929.md) §4 已系统录入俄共（布）十大 694 名表决代表中工会决议的精确票数——“十人纲领” **336 票**、托洛茨基—布哈林纲领 **50 票**、工人反对派 **18 票**（弃权 2 票），《关于党的统一》反对票不足 30 票，以及 1921 年 1 月莫斯科党委前期表决（`57:33:21`）；[`DATA-08`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-08-1921-1929-nep-social-classes-unemployment-and-gender-labor.md) §5.2 录有全苏工会中央理事会 1924 年党员占比 100%、1926 年 99.6% 的组织化指标。本卡经验基准（L20）未给出任何一项票数数据，且两张数据卡均未引用。
  2. **`core_cards` 漏挂**：已有双向回链指向本卡的 [`MTG-1922-03-11th-party-congress`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1922-03-11th-party-congress.md)（十大决议的首次惩戒检验与二十二人宣言）、[`ORG-right-opposition-1928`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-right-opposition-1928.md)、[`PER-osinsky`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-osinsky.md) 与 [`PER-sapronov`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-sapronov.md)（民主集中派领袖）均漏出 `core_cards`；另有直接决定十大政治氛围的 [`EVT-1921-kronstadt`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1921-kronstadt.md)、缓冲派核心 [`PER-bukharin`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-bukharin.md) 及同步出台的 [`POL-nep`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-nep.md) 建议补入。
- **修复**：在 L20 补入 `336:50:18` 等十大实证票数并在 T3 挂接 `DATA-04`、`DATA-08`；扩充 `core_cards` 完成双向闭环。

#### 03-03｜P2｜`era` 与 `dates` 跨度说明、第 7 条首次公开宣读时间及 L25 措辞微瑕
- **定位**：[`L5-8`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md#L5-L8)、[`L25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md#L25)、[`L31`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md#L31)。
- **核证**：`era: "1920-1929"` 而 `dates` 止于 `1921-03-16`（十大闭幕），宜注明系“核心论战 1920–1921，制度后续延至 1929”；L25“列宁及十大多数派”读来略生硬，宜写作“列宁与‘十人纲领’（十大代表大会多数派）”；T3 L31 提及秘密第 7 条时，可补充站内原典 [`1921-03-16_on-party-unity.md:54`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E06_E10_turning_points/1921-03-16_on-party-unity.md#L54) 已核实该条首次由斯大林于 `1924-01-17` 第十三次党代表会议公开宣读。
- **修复**：微调上述三处表述与注释。

---

> **阶段一（01–03）小计**：**P0 = 1 项**（`02-01`）、**P1 = 6 项**（`01-01`、`01-02`、`02-02`、`02-03`、`03-01`、`03-02`）、**P2 = 3 项**（`01-03`、`02-04`、`03-03`）。

---

## 四、阶段二（04–06）历法、时域与 `<= 1929` 分期边界核查表

| 卡片 | 卡内日期（YAML／正文） | 历法与 `<= 1929` 边界核查 | 判定 |
| :--- | :--- | :--- | :--- |
| 04 `DEB-1924-socialism-in-one-country` | YAML：`start_ns: 1924-01-01`、`end_ns: 1927-12-19`（十五大闭幕）；`era: 1924-1927`；正文：1923 列宁合作社文章、1924—1925 多数派提出、1926 联合反对派、1927 十五大 | 全段属纯公历，终点准确吻合十五大闭幕日 `1927-12-19`，无越界 | **历法合规**；正文未区分斯大林 1924-04 初版旧公式与 1924-12 改口时间差（P2） |
| 05 `DEB-1928-bukharin-alternative` | YAML：`start_ns: 1927-10-01`、`end_ns: 1929-11-17`（十一月全会闭幕、布哈林被逐出政治局）；`era: 1927-1929`；正文：1928-07、1928-09、1929-04、1929-11 | 全段属纯公历，关键会议节点全部精确无误，严守 `<= 1929` 边界 | **完全合规** |
| 06 `DEB-1929-collectivization-and-dekulakization-causes` | YAML：`start_ns: 1927-10-01`、`end_ns: 1929-12-31`；`era: 1927-1929`；正文：1929-12-18 草案、12-25 斯大林否决、12-27 公开转向 | 全段属纯公历；经对勘 [`CLM-tragedy-village-1929-politburo-dekulakization-commission.md:26-29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-tragedy-village-1929-politburo-dekulakization-commission.md#L26-L29)（Doc 12 12-18、Doc 16 12-25、12-27 讲话），三日精准无误；且 T3 L31 清晰划界“1930年正式指令、大规模驱逐及1930—1933年饥荒属后续后果，不压入1929年” | **分期与日期把控极佳**（唯 L26 错把第 2 卷标为“1929年卷”，另归 P0 处理） |

---

## 五、阶段二逐卡深度审计与修复方案（04–06）

### 04｜一国建成社会主义与不断革命论（`DEB-1924-socialism-in-one-country`）

**总体评价**：对斯大林／季诺维也夫／托洛茨基 2026 年二次汇编引文的史料局限提示相当清醒（L24–25 准确消化了 `CLM-bukharin-stalin-1925` 与 `CLM-zinoviev-trotsky-1926` 的版本边界）。但全卡存在 **2 项严重 P0**（顺着辩论卡名把 E. H. Carr 1976 与 1979 两部不同著作错植为 *Socialism in One Country*；望文件名省略 Sakharov 与 Zhukov 真实姓名书名且将萨哈罗夫强烈的“亲斯大林／批布哈林两稿断裂论”洗白改写为中立文本学），以及 **2 项 P1**（两个同名核心概念卡 `CON-socialism-in-one-country` 与 `CON-permanent-revolution` 竟然双双漏出 `core_cards`！另漏引 `DATA-04` 十四大 `559:65` 表决、Wave 39 列宁两篇绝笔 S 级原典及托洛茨基不断革命论原文卡）。

#### 04-01｜P0｜“望题生书名”著作归属硬伤：把 E. H. Carr 1976 与 1979 年两部著作错植为 *Socialism in One Country*
- **定位**：[`DEB-1924-socialism-in-one-country.md:27`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1924-socialism-in-one-country.md#L27)（矩阵第 4 行：“`E. H. Carr, Socialism in One Country`”，挂接 `CLM-carr-1979-stalin-synthesis-of-russian-backwardness-and-industrialism` 与 `CLM-carr-1976-china-1927-defeat-and-comintern-factionalism`）。
- **核证**：
  1. 打开 [`CLM-carr-1979-stalin-synthesis-of-russian-backwardness-and-industrialism.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1979-stalin-synthesis-of-russian-backwardness-and-industrialism.md#L4-L6)，其 `work_title` 为 ***`The Russian Revolution From Lenin to Stalin, 1917–1929`***（**1979**），而非卡尔 1958–1964 年出版的三卷本 *Socialism in One Country, 1924–1926*！
  2. 打开 [`CLM-carr-1976-china-1927-defeat-and-comintern-factionalism.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-1976-china-1927-defeat-and-comintern-factionalism.md#L4-L6)，其 `work_title` 为 ***`Foundations of a Planned Economy, 1926-1929, Volume Three - II`***（**1976**），同样绝非 *Socialism in One Country*！
  3. 核查 `sources/monographs/` 馆藏目录可知，本库虽收有 14 卷本全集 EPUB，但并未单卷拆读产出任何一张源自 *Socialism in One Country* 的 `CLM-*`。此处系典型“看到 `DEB-1924-socialism-in-one-country` 标题＋`CLM-carr-*` 前缀便想当然填写 *Socialism in One Country*”的著作幻觉。
- **修复**：将 L27“代表学者与著作”更正为 `E. H. Carr, The Russian Revolution From Lenin to Stalin (1979)；Foundations of a Planned Economy, Vol. 3-II (1976)`，并在 T3 同步挂接二者对应的站内源札记 [`RN-W24-lenin-to-stalin-revolution-from-below-to-above.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr1979_service2009/RN-W24-lenin-to-stalin-revolution-from-below-to-above.md) 与 [`RN-W22-soviet-dual-diplomacy-and-comintern-sixth-congress-turn.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr_comintern/RN-W22-soviet-dual-diplomacy-and-comintern-sixth-congress-turn.md)。

#### 04-02｜P0｜望文件名省略两位俄罗斯学者全名／原书名，且严重曲解／洗白 Valentin Sakharov（2012）的“两稿断裂—批布哈林—护斯大林”核心论断
- **定位**：[`DEB-1924-socialism-in-one-country.md:28-29`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1924-socialism-in-one-country.md#L28-L29)（矩阵第 5、6 行）。
- **核证**：
  1. **L28（Sakharov，严重曲解原旨）**：仅据文件名写作“**`Sakharov，列宁合作社计划研究`**”，漏写了真实全名、年份与原书名——[`CLM-sakharov-2012-lenin-cooperative-plan-debates.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-sakharov-2012-lenin-cooperative-plan-debates.md#L4-L6) 为 **`Valentin Sakharov / 瓦连京·萨哈罗夫 (2012), На распутье: Дискуссии о путях и перспективах развития советского общества. 1921–1929 гг.（《站在十字路口》）`**。更严重的是，L28 把他的论点写成温和中立的“列宁晚期合作社文本成为相互竞争的解释资源，其具体语境不能直接等同后来的派别公式”——而打开 [`CLM-sakharov-2012-lenin-cooperative-plan-debates.md:18,40`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-sakharov-2012-lenin-cooperative-plan-debates.md#L18-L40) 可见，萨哈罗夫的真实论点截然相反且极具攻击性：他论证列宁《论合作社》两份口述稿存在根本理论断裂（放弃第一稿“商贩式流通合作社”，在第二稿转向“国有土地＋国有生产资料上的生产合作社／集体农庄”），**直指布哈林偷换概念曲解列宁，并公开论证斯大林的机器拖拉机站（MTS）＋集体农庄路线才是列宁第二稿的理论正统继承人**！把一位鲜明的后苏联亲斯大林／反布哈林修正派学者改写成“反对把列宁等同派别公式”的中立文本学家，构成了对所引论断卡原旨的严重歪曲。
  2. **L29（Zhukov，望目录名猜书名＋遮蔽立场）**：仅据目录名 `nep_1923_and_zinoviev` 写作“**`Zhukov，季诺维也夫与新经济政策研究`**”，隐去了真实作者全名、年份与著作名——[`CLM-zhukov-zinoviev-1925-leningrad-opposition.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-zhukov-zinoviev-1925-leningrad-opposition.md#L4-L6) 明确为 **`Yuri Zhukov / 尤里·茹科夫 (2011), 《格里高利·季诺维也夫：被遗忘的世界革命领袖》`**；同时完全略去了茹科夫在 [`CLM-zhukov-zinoviev-comintern-and-1923-germany.md:35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-zhukov-zinoviev-comintern-and-1923-germany.md#L35) 鲜明的后苏联民族国家现实主义倾向（盛赞斯大林 1923-08-07 审慎洞察、贬抑季诺维也夫狂热盲动）。
- **修复**：
  1. 第 5 行更正为 `Valentin Sakharov (2012), На распутье...（《站在十字路口》）`，如实概括其“《论合作社》两稿断裂论＋批判布哈林偷换概念＋恢复列宁与斯大林生产合作社路线连续性”，并在盲点栏照录该卡第 40 行的核心警惕（不能将列宁生产合作社逻辑直接等同 1929–1930 暴力全盘强制集体化）；
  2. 第 6 行更正为 `Yuri Zhukov (2011), 《格里高利·季诺维也夫：被遗忘的世界革命领袖》`，并注明其后苏联现实主义视角盲点。

#### 04-03｜P1｜两个同名核心概念卡双双漏出 `core_cards`，且漏引 `DATA-04`（十四大 `559:65`）、Wave 39 列宁两篇绝笔原典与站内直接源札记
- **定位**：[`L9`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1924-socialism-in-one-country.md#L9)、[`L20`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1924-socialism-in-one-country.md#L20)、[`L34`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1924-socialism-in-one-country.md#L34)。
- **核证**：
  1. **同名核心概念卡全漏**：本卡标题即《一国建成社会主义与不断革命论》，但 `core_cards`（L9）竟把站内已双向回链的两张核心概念卡 [`CON-socialism-in-one-country`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-socialism-in-one-country.md) 与 [`CON-permanent-revolution`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-permanent-revolution.md) **双双漏掉**！同时漏挂 [`ORG-comintern`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/organizations/ORG-comintern.md)、[`EVT-1927-war-scare-and-opposition-expulsion`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1927-war-scare-and-opposition-expulsion.md)、[`PER-lenin`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-lenin.md) 与 [`CON-state-capitalism`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-state-capitalism.md)。
  2. **漏引 `DATA-04` 十四大实证票数**：[`DATA-04-party-membership-and-congress-votes-1903-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-04-party-membership-and-congress-votes-1903-1929.md) §5 已精准界定 1925 年十四大批准斯大林中央政治报告决议案表决为 **`559 : 65`**（反对票主要来自列宁格勒代表团）及 1927 年党员结构，本卡经验基准（L20）未引一字。
  3. **漏引 Wave 39 新增列宁晚期 S 级原典**：除《论合作社》外，Wave 39 刚精读入库的 [`1923-01-16_lenin-our-revolution-sukhanov-notes.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/W39_lenin_1922_1923_docs/1923-01-16_lenin-our-revolution-sukhanov-notes.md)（逆转第二国际生产力决定论，论证落后俄国先夺政权再建文明前提）与 [`1923-03-02_lenin-better-fewer-but-better.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/W39_lenin_1922_1923_docs/1923-03-02_lenin-better-fewer-but-better.md)（俄印中世界人口多数论与“换马”战略）同属 1924–1927 双方争夺列宁思想遗产的核心原典，宜补挂 T3。
  4. **T3 漏列源札记**：矩阵引了 Sakharov（2012）与 Carr（1976、1979），但 T3 L34 漏列三者真正的站内精读札记 [`RN-02-sakharov-crossroads.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/RN-02-sakharov-crossroads.md)、[`RN-W24-lenin-to-stalin-revolution-from-below-to-above.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr1979_service2009/RN-W24-lenin-to-stalin-revolution-from-below-to-above.md) 与 [`RN-W22-soviet-dual-diplomacy-and-comintern-sixth-congress-turn.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr_comintern/RN-W22-soviet-dual-diplomacy-and-comintern-sixth-congress-turn.md)。
- **修复**：将 `CON-socialism-in-one-country`、`CON-permanent-revolution`、`ORG-comintern`、`EVT-1927-war-scare-and-opposition-expulsion`、`PER-lenin` 补入 `core_cards`；在 L20 与 T3 补入 `DATA-04`（`559:65`）、Wave 39 列宁两篇原典及三篇缺失 `RN-*`。

#### 04-04｜P1｜`[T2]` 矩阵漏挂“不断革命论”原始锚点卡、波拿巴主义恐惧分析卡，且未把站内已有的布哈林 1925 年 4 月原文纳入第 1 行对照
- **定位**：[`L24-25`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1924-socialism-in-one-country.md#L24-L25)。
- **核证**：
  1. 本卡标题并列“一国建成社会主义”与“不断革命论”，但 `[T2]` 矩阵全无托洛茨基 1905/1922 不断革命论原典卡 [`CLM-trotsky-1905-december-uprising-lessons-and-permanent-revolution-defense`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-trotsky-1905-december-uprising-lessons-and-permanent-revolution-defense.md)（已双向回链本卡），致使“不断革命论”在矩阵中只剩 1926 年世界市场商品压力的局部转引；
  2. 站内已回链本卡的 [`CLM-service-2009-trotsky-political-tactical-blunders`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-service-2009-trotsky-political-tactical-blunders.md) 与 [`CLM-shlapentokh-bonapartism-fear-against-trotsky`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-shlapentokh-bonapartism-fear-against-trotsky.md)（反驳 Deutscher 同情视角的党内“波拿巴主义恐惧”与战术失误解释）亦未纳入，使第 3 行仅存 Deutscher 一家传记视角；
  3. L24 盲点栏强调 `CLM-bukharin-stalin-1925` 不能代替布哈林原文，却未在该行直接指向 T3 已经列出的站内 S 级原文 [`1925-04_bukharin-road-to-socialism.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/E09_E10_party_debates/1925-04_bukharin-road-to-socialism.md)。
- **修复**：第 1 行注明对照站内布哈林 `1925-04_bukharin-road-to-socialism.md`；第 2 行补挂 `CLM-trotsky-1905-december-uprising-lessons-and-permanent-revolution-defense`；第 3 行并列 Service (2009) 与 Shlapentokh 同 Deutscher 形成正反对勘。

#### 04-05｜P2｜`dates.start_ns: "1924-01-01"` 宜在经验基准补注斯大林 1924-04 初版旧公式与 1924-12 改口的时间节点
- **定位**：[`L6-8`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1924-socialism-in-one-country.md#L6-L8)、[`L20`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1924-socialism-in-one-country.md#L20)。
- **核证**：斯大林 1924 年 4 月《论列宁主义基础》初版仍沿用“一国不够组织社会主义生产”的旧公式，直到 1924 年 12 月《十月革命和俄国共产党人的策略》才正式转向并在 1926 年再版改写该句。
- **修复**：在 L20 经验基准补入“1924-04 旧公式 → 1924-12 改口 → 1925-04 十四次代表会议确认”的三步时序。

---

### 05｜布哈林替代方案与新经济政策终结之争（`DEB-1928-bukharin-alternative`）

**总体评价**：**本批学术准确度与平衡度最好的一张卡（0 P0）**！全部 11 张被挂接的 `CLM-*`（Cohen 1973 ×3、Erlich 1960 ×3、Nove 1964、Kotkin 2014、Khlevniuk 2015、Priestland 2007、Merridale 1990）的学者姓名、书名、出版年份与核心论点全部核验准确，且主动挂接了 `DATA-03` 并区分了“经济可行性、政治可行性与实际权力斗争”。但仍存在 **3 项 P1**：一是漏挂 Wave 39 刚入库的泽姆斯科夫专著（`RN-W39-stalin-era-nep-to-great-turn-1924-1929.md` / `CLM-zemskov-2018-archival-constraints-and-party-radicalism`）、Wave 39 列宁绝笔《宁肯少些，但要好些》以及站内重磅计量—档案交锋卡 `CLM-davies-festschrift-1995`（Hunter KAPROST vs Davies 1994 + 谷内融）与 `CLM-bukharin-preobrazhensky-equilibrium-vs-accumulation-zh`（刘伟、平新乔 1989）；二是 T3 漏列矩阵所引 Nove、Kotkin、Khlevniuk、Priestland、Merridale 5 位学者在站内的全部对应 `RN-*` 以及 `DATA-02`/`DATA-04`/`DATA-08`；三是 `core_cards` 漏挂沙赫特案、粮食危机与一五计划等 5 张核心节点，且 L26 弱化了 Nove 的“NEP 死胡同”锋芒。

#### 05-01｜P1｜漏挂 Wave 39 泽姆斯科夫专著、Wave 39 列宁绝笔《宁肯少些，但要好些》，以及站内重磅计量—改革经济学争鸣卡（Hunter/Davies 1995、刘伟/平新乔 1989、Sakharov 2012、Fitzpatrick 1978）
- **定位**：[`DEB-1928-bukharin-alternative.md:22-28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1928-bukharin-alternative.md#L22-L28)、[`L33`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1928-bukharin-alternative.md#L33)。
- **核证**：
  1. **Wave 39 泽姆斯科夫专著漏挂**：[`CLM-zemskov-2018-archival-constraints-and-party-radicalism.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-zemskov-2018-archival-constraints-and-party-radicalism.md)（`debate: DEB-1928-bukharin-alternative`，直接 `qualifies: ["CLM-cohen-1973-nep-viability"]`，B 级，母札记 [`RN-W39-stalin-era-nep-to-great-turn-1924-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/stalin_era_economy_repression_1924_1954_zh/RN-W39-stalin-era-nep-to-great-turn-1924-1929.md)）直击“布哈林渐进路线在内战记忆塑造的党员革命心态中缺乏政治亲和力”，是连结经济替代性与执政党社会心理的重要俄罗斯档案学者视角；
  2. **Wave 39 列宁绝笔原典漏挂**：[`1923-03-02_lenin-better-fewer-but-better.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/web-archive/W39_lenin_1922_1923_docs/1923-03-02_lenin-better-fewer-but-better.md)（S 级，确立“宁可慢些、精简官僚节约积累、从穷苦庄稼汉的马跨到大机器工业的马”）是布哈林 1928 年《一个经济学家的札记》的经典合法性源头，本卡 T3 未挂；
  3. **计量反事实与改革经济学交锋卡漏挂**：
     - [`CLM-davies-festschrift-1995-nep-statistics-and-planning-debates.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-davies-festschrift-1995-nep-statistics-and-planning-debates.md)（A 级，[`RN-W23`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/smirnov_davies_festschrift/RN-W23-1920s-red-army-militia-reform-and-davies-festschrift.md)）：包含 **Holland Hunter (1995)** 用 KAPROST 反事实模型支持非集体化 NEP 替代路径、**R. W. Davies (1994)** 以 1928 年市场已遭行政扰乱予以尖锐反驳、以及 **谷内融（Yuzuru Taniuchi）** 1929 年 1–6 月政治局档案实证——直接回应本卡 L26 所谓“反事实替代方案难以检验”；
     - [`CLM-bukharin-preobrazhensky-equilibrium-vs-accumulation-zh.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-bukharin-preobrazhensky-equilibrium-vs-accumulation-zh.md)（B 级，**刘伟、平新乔 1989**，中国改革经济学视野下的“均衡 vs 非均衡”及布哈林作为短缺经济学先驱之重估）；
     - 以及俄国反布哈林修正派 [`CLM-sakharov-2012-nep-crossroads-1928.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-sakharov-2012-nep-crossroads-1928.md) 与文化革命反右攻势 [`CLM-fitzpatrick-1978-anti-bukharin-ideological-offensive.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-fitzpatrick-1978-anti-bukharin-ideological-offensive.md)。
- **修复**：在 `[T2]` 增设“反事实计量与后苏联档案重估”一行（并列 Holland Hunter / R. W. Davies 1995、Viktor Zemskov 2018 [B 级]、刘伟与平新乔 1989 [B 级] / Valentin Sakharov 2012）；在 T3 补挂 `RN-W39-stalin-era-nep-to-great-turn-1924-1929.md`、`RN-W23` 与 `1923-03-02_lenin-better-fewer-but-better.md`。

#### 05-02｜P1｜T3 漏列矩阵所引 5 位学者在站内的全部对应 `RN-*`，且漏引 `DATA-02`、`DATA-04`、`DATA-08`
- **定位**：[`L31`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1928-bukharin-alternative.md#L31)、[`L33`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1928-bukharin-alternative.md#L33)。
- **核证**：
  1. 矩阵挂接了 Nove（1964）、Kotkin（2014）、Khlevniuk（2015）、Priestland（2007）、Merridale（1990）的 5 张 `CLM-*`，但 T3 L33 仅列了 Cohen 与 Erlich 两篇札记，**漏列上述 5 位学者对应的全部站内精读札记**：[`RN-W6-agricultural-crisis-and-was-stalin-necessary.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/carr_davies_nove/RN-W6-agricultural-crisis-and-was-stalin-necessary.md)、[`RN-W1C-1928-siberian-turn-and-bukharin.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/kotkin_2014_stalin_v1/RN-W1C-1928-siberian-turn-and-bukharin.md)、[`RN-W3-politburo-apparatus-and-1929-victory.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/khlevniuk_2015_stalin/RN-W3-politburo-apparatus-and-1929-victory.md)、[`RN-W12-revivalist-mobilization-and-ukrainianization-1920s.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/priestland_liber/RN-W12-revivalist-mobilization-and-ukrainianization-1920s.md) 与 [`RN-W6-moscow-fall-and-party-struggle-rules.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/merridale_apalkov/RN-W6-moscow-fall-and-party-struggle-rules.md)。
  2. T3 L31 主动挂接了 `DATA-03`（优良实践！），但同时漏挂了同样高度相关的 [`DATA-02-1922-1924-scissors-crisis-and-chervonets.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-02-1922-1924-scissors-crisis-and-chervonets.md)（剪刀差与币制前史）、[`DATA-04-party-membership-and-congress-votes-1903-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-04-party-membership-and-congress-votes-1903-1929.md)（1929 清党 11%/17 万人开除率）与 [`DATA-08-1921-1929-nep-social-classes-unemployment-and-gender-labor.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-08-1921-1929-nep-social-classes-unemployment-and-gender-labor.md)（NEP 晚期登记失业与工人群体结构）。
- **修复**：在 T3 补齐 5 篇直接源札记及 `DATA-02`/`DATA-04`/`DATA-08`。

#### 05-03｜P1｜`core_cards` 漏挂 5 张直接关联的核心节点，且 L26 弱化了 Nove（1964）“NEP 死胡同”的尖锐论证
- **定位**：[`L9`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1928-bukharin-alternative.md#L9)、[`L26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1928-bukharin-alternative.md#L26)。
- **核证**：
  1. `core_cards` 漏挂了直接构成本争鸣核心现场的 [`EVT-1928-grain-procurement-crisis`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1928-grain-procurement-crisis.md)、[`EVT-1928-shakhty-affair-show-trial`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1928-shakhty-affair-show-trial.md)、[`POL-first-five-year-plan`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-first-five-year-plan.md)、[`CON-primitive-socialist-accumulation`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-primitive-socialist-accumulation.md) 与莫斯科市委倒台核心人物 [`PER-uglanov`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-uglanov.md)；
  2. L26 把 Nove（1964）压缩为过于中性的“必须区分发展目标、速度和强制手段”，淡化了 [`CLM-nove-1964-stalin-necessity-dilemma.md:18`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-nove-1964-stalin-necessity-dilemma.md#L18) 的核心锋芒——即给定布尔什维克保住少数派政权、拒走斯托雷平富农资本主义与快速重工业化三大前提，NEP 至 1927 年已陷入结构性“死胡同（cul-de-sac）”，布哈林的市场渐进路径存在内在政治经济不一致。
- **修复**：扩充 `core_cards`；在 L26 点出 Nove 的“条件性必然”与“1927 年 NEP 死胡同”核心命题。

#### 05-04｜P2｜L28 三位学者省略全名与书名，体例与前四行不统一
- **定位**：[`L28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1928-bukharin-alternative.md#L28)。
- **核证**：写作 `Khlevniuk (2015)；Priestland (2007)；Merridale (1990)`，缺少全名与书名。
- **修复**：补全为 `Oleg Khlevniuk, Stalin (2015)；David Priestland, Stalinism and the Politics of Mobilization (2007)；Catherine Merridale, Moscow Politics and the Rise of Stalin (1990)`。

---

### 06｜1929年集体化与消灭富农政策的动因之争（`DEB-1929-collectivization-and-dekulakization-causes`）

**总体评价**：分期意识极佳——精准把握了 1929 年 12 月 18 日、25 日、27 日三日转折，并清晰拒绝将 1930 年正式指令与 1930–1933 大饥荒压入 1929 年已完成事实。但存在 **1 项 P0**（矩阵第 3 行仅据文件名 `tragedy-village-1929` 隐去达尼洛夫、曼宁、维奥拉、伊夫尼茨基四位主编与 2000 出版年，并杜撰出并不存在的卷号“1929年卷”；同卡第 2 行还把 `CLM-carr-davies-1969-nemchinov-table-critique` 的谷物商品率／涅姆奇诺夫表批判误述为“价格统计”），以及 **2 项重要 P1**：全卡竟**一张定量数据卡都没引**（站内最直接对应的 `DATA-03`、`DATA-06`、`DATA-08` 全部缺席！），并漏挂 Wave 39 泽姆斯科夫直指本卡的论断卡 `CLM-zemskov-2018-agrarian-tribute-and-coercive-turn`、David Shearer (2024)、Wendy Goldman (2011) 及多张核心回链节点。

#### 06-01｜P0｜望文件名生义隐去四位档案主编并杜撰卷名“1929年卷”，且错将 `nemchinov-table-critique` 摘要为“价格统计”
- **定位**：[`DEB-1929-collectivization-and-dekulakization-causes.md:25-26`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md#L25-L26)（矩阵第 2、3 行）。
- **核证**：
  1. **L26（第 3 行，隐去四位权威主编＋望文件名杜撰不存在卷名）**：卡片写作“**`苏联农村悲剧档案集，1929年卷`**”。打开其所引三张论断卡 [`CLM-tragedy-village-1929-politburo-dekulakization-commission.md:4-6`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-tragedy-village-1929-politburo-dekulakization-commission.md#L4-L6) 及母札记 [`RN-W20-nov-dec-1929-politburo-commission-and-ogpu-archives.md:5-8`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/tragedy_village_1929/RN-W20-nov-dec-1929-politburo-commission-and-ogpu-archives.md#L5-L8) 可见：
     - 真实编者与年份为 **В. П. Данилов（V. P. Danilov）、Р. Т. Маннинг（Roberta Manning）、Л. Виола（Lynne Viola）、Н. А. Ивницкий（N. A. Ivnitsky）主编（2000）**（`SCH-danilov-ivnitsky-eds`）；
     - 真实卷次为 **《苏联农村的悲剧》第 2 卷（*Том 2: Ноябрь 1929 — декабрь 1930*）**！原书 5 卷本中根本不存在“1929年卷”（第 1 卷为 1927 年 5 月—1929 年 11 月，第 2 卷为 1929 年 11 月—1930 年 12 月），所谓“1929年卷”纯系从文件名 `tragedy-village-1929` 硬猜出来的虚构卷名！
  2. **L25（第 2 行，错述所引 Carr–Davies 论断卡内容＋漏书名年份）**：L25 仅写 `Carr 与 Davies`（漏书名 `Foundations of a Planned Economy, 1926–1929, Vol. 1, Part 1 (1969)`），更把其核心论点写成“秋季大转变的事后表述、十一月决议与**价格统计**须分别检验”。但打开 [`CLM-carr-davies-1969-nemchinov-table-critique.md:18-23`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-carr-davies-1969-nemchinov-table-critique.md#L18-L23) 可知，该卡根本**不是价格统计卡**（价格剪刀差系另一张未被本卡引用的 `CLM-carr-davies-1969-grain-price-scissor-1927`），它剖析的是**斯大林 1928-05-28 引用的涅姆奇诺夫谷物商品率表**（战前 26% → 1926/27 年 13.3%，农户由 1600 万裂变至 2558.6 万户，中贫农占 74% 商品粮从而戳穿“只打富农”神话）。
- **修复**：
  1. L26 更正为 `V. P. Danilov, R. Manning, L. Viola & N. A. Ivnitsky (eds.), 《苏联农村的悲剧》第2卷（1929年11月—1930年12月，2000）`；
  2. L25 补全 `E. H. Carr & R. W. Davies, Foundations of a Planned Economy, Vol. 1, Part 1 (1969)`，将“价格统计”更正为“涅姆奇诺夫谷物商品率表（中贫农占 74% 商品粮、农户分家裂变）”——若欲兼论价格，则同步补挂 `CLM-carr-davies-1969-grain-price-scissor-1927`。

#### 06-02｜P1｜全卡未引用任何一张站内核心定量数据卡（`DATA-03`、`DATA-06`、`DATA-08` 全缺席），却把已入库统计泛归外部缺口
- **定位**：[`L20`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md#L20)、[`L31-35`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md#L31-L35)。
- **核证**：
  1. [`DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md) 的 §B 专节即《1929年6月—12月：集体化入庄比例、播种面积指标跳变与“二万五千人”》，且 §A 含莫佐欣 ЦА ФСБ 征粮逮捕与 OGPU 司法外镇压序列——堪称本争鸣卡的“亲生数据底座”，本卡只字未提！
  2. [`DATA-03-1926-1929-grain-procurement-and-nemchinov-table.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-03-1926-1929-grain-procurement-and-nemchinov-table.md) 完整录有涅姆奇诺夫表、Carr–Davies 五重批判及 1926–1929 国家谷物收购波动序列；[`DATA-08`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-08-1921-1929-nep-social-classes-unemployment-and-gender-labor.md) §1 录有 Lewin 1927 税务农村阶层分化表。三张高度对口的数据卡全数闲置，而 L35 却笼统把“农户产量及收购口径的地区对照”列为外部缺口，未区分站内已核全国口径与待补地区细分口径。
- **修复**：在 L20 经验基准补入 `DATA-06` 关键入庄率节点（1929-06-01 3.9% → 10-01 7.5% → 12-11 俄联邦春播目标增幅 60%）；在 T3 显式挂接 `DATA-03`、`DATA-06` 与 `DATA-08` §1，并精准界定 L35 外部缺口仅针对未入库的地区级细分统计与全会完整俄文速记。

#### 06-03｜P1｜漏挂 Wave 39 泽姆斯科夫直指本卡的论断卡、Shearer (2024)、Goldman (2011)、3 篇直接源札记，且 `core_cards` 漏挂 6 张核心节点
- **定位**：[`L9`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md#L9)、[`L27-28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md#L27-L28)、[`L33`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md#L33)。
- **核证**：
  1. **Wave 39 泽姆斯科夫直指本卡的论断卡漏挂**：[`CLM-zemskov-2018-agrarian-tribute-and-coercive-turn.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-zemskov-2018-agrarian-tribute-and-coercive-turn.md)（`debate: DEB-1929-collectivization-and-dekulakization-causes`，直接 `qualifies: ["CLM-davies-1980-autumn-1929-great-turn-fabrication"]`，B 级，母札记 [`RN-W39-stalin-era-nep-to-great-turn-1924-1929.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/stalin_era_economy_repression_1924_1954_zh/RN-W39-stalin-era-nep-to-great-turn-1924-1929.md)）聚焦 1920 年代低价收购的农业“贡税”积累机制及 1929 年底地方跨区驱逐向 1930-01-30 制度化安置的分期过渡，本卡未挂；
  2. **战争威胁与工业化破坏论断卡漏挂**：矩阵第 4 行“战争恐慌与地缘政治”漏挂了站内直击“1927–1929 外部威胁想象如何直接决定集体化动员时间与强度”的 **David Shearer (2024)** [`CLM-stalin-war-1927-1929-threat-and-collectivization.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-stalin-war-1927-1929-threat-and-collectivization.md)（A 级）；且双向回链本卡的 **Wendy Goldman (2011)** [`CLM-goldman-2011-great-turn-industrialization-and-wrecking.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-goldman-2011-great-turn-industrialization-and-wrecking.md) 亦未纳入；
  3. **T3 漏列 3 篇已引学者源札记**：矩阵挂了 Velikanova (2013)、Kotkin (2014)、Erlich (1960)，但 T3 L33 漏列了三者对应的站内札记 [`RN-W8-1927-war-scare-and-grassroots-svodki.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/velikanova_2013_popular_perception/RN-W8-1927-war-scare-and-grassroots-svodki.md)、[`RN-W1C-1928-siberian-turn-and-bukharin.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/kotkin_2014_stalin_v1/RN-W1C-1928-siberian-turn-and-bukharin.md) 与 [`RN-W3-industrialization-models-and-constraints.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/erlich_1960_industrialization/RN-W3-industrialization-models-and-constraints.md)；
  4. **`core_cards` 漏挂 6 张核心节点**：站内直接指向本争鸣的 [`CON-kulak`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-kulak.md)（富农概念本身！）、[`POL-first-five-year-plan`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-first-five-year-plan.md)、[`EVT-1927-war-scare-and-opposition-expulsion`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1927-war-scare-and-opposition-expulsion.md)、[`INS-cheka-gpu-ogpu`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-cheka-gpu-ogpu.md)（OGPU 基层情报与驱逐执行主体）、[`CON-peasant-commune-obshchina`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/concepts/CON-peasant-commune-obshchina.md) 与 [`PER-molotov`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-molotov.md)（11 月全会激进主推者及 12 月底删改草案核心）均漏出 `core_cards`。
- **修复**：在矩阵第 4 行补挂 `CLM-stalin-war-1927-1929-threat-and-collectivization`、第 5 行（或新增后苏联档案对照）补挂 `CLM-zemskov-2018-agrarian-tribute-and-coercive-turn`（注明 B 级与分期界线）；T3 补齐 `RN-W39` 与上述 3 篇源札记；`core_cards` 补入上述 6 张核心卡。

#### 06-04｜P2｜L27–L28 省略学者全名与书名，体例不统一
- **定位**：[`L27-28`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md#L27-L28)。
- **核证**：仅写 `Velikanova (2013)；Kotkin (2014)` 与 `Erlich (1960)；Nove (1964)`，缺少全名与完整书名。
- **修复**：补全 `Olga Velikanova, Popular Perceptions of Soviet Politics in the 1920s (2013)`、`Stephen Kotkin, Stalin, Vol. I (2014)`、`Alexander Erlich, The Soviet Industrialization Debate (1960)`、`Alec Nove, Was Stalin Really Necessary? (1964)`。

---

## 六、全批 6 卡审计总览与跨卡系统性病灶诊断

### 6.1 全 6 卡 P0 / P1 / P2 统计总表

| 序号 | 卡片 ID | P0 | P1 | P2 | 核心问题一句话定性 |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 01 | `DEB-1920-polish-war-and-revolutionary-export` | **0** | **2** | **1** | 学者名全准；但漏引站内 Khlevniuk (2015) 对斯大林 7 月电报的直接反证、错配 T3 札记且 4/5 CLM 为间接代挂 |
| 02 | `DEB-1920s-gender-family-and-everyday-life` | **1** | **2** | **1** | **P0 望文件名隐去 3 位作者且为 Lebsky 凭空杜撰性别托育论点**；漏挂 Wave 39 Arapovich 正统专著与 `DATA-08` |
| 03 | `DEB-1921-trade-union-controversy-and-party-unity` | **0** | **2** | **1** | 学者名与第 7 条文本史精准；但连续 3 行复用 Daniels 卡，漏挂 `RN-W35` 内的 Godson 与 Lebsky 及 `DATA-04`/`DATA-08` |
| 04 | `DEB-1924-socialism-in-one-country` | **2** | **2** | **1** | **双重 P0**：把 Carr 1976/1979 著作错标 *Socialism in One Country*；省略 Sakharov/Zhukov 真名书名并洗白歪曲 Sakharov 亲斯大林论断；同名概念卡双漏 |
| 05 | `DEB-1928-bukharin-alternative` | **0** | **3** | **1** | **全批最稳（0 P0）**；待补 Wave 39 泽姆斯科夫与列宁绝笔、Hunter/Davies 1995、5 篇已引学者源札记及 `DATA-02/04/08` |
| 06 | `DEB-1929-collectivization-and-dekulakization-causes` | **1** | **2** | **1** | 分期精准；但 **P0 望文件名隐去 Danilov 等 4 主编并杜撰“1929年卷”**、误述 `nemchinov-table-critique` 为“价格统计”；全卡漏引 `DATA-03`/`DATA-06` 与 Wave 39 泽姆斯科夫 |
| **合计** | **Wave 40 第二批 6 张 `DEB-*` 卡** | **4** | **13** | **6** | **3 卡为 0 P0（01/03/05），3 卡检出 4 处 P0（02/04/06）** |

### 6.2 跨卡系统性病灶诊断（对比 [`AUD-18A`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-18A-wave39-codex-deb-batch1-audit.md) 与本次 `AUD-18B`）

1. **显著进步项**：
   - 机械规范达 100%（零断链 ID、零断链 `.md` 路径、全部 `[T1]` 字数控制在 119–126 字）；
   - `<= 1929` 分期边界与高危史料版本意识明显增强（如 03 号卡准确区分十大第 7 条通过本与拟案、04 号卡对 2026 年二次汇编引文保持清醒、06 号卡精准卡住 12 月 18/25/27 日三日转折并拒绝把 1930 事实压入 1929）；
   - P0 密度由首批 `AUD-18A` 的 **7 处 / 5 卡**降至本批的 **4 处 / 3 卡**，且 01、03、05 三张卡实现了 **0 P0**。
2. **四大复发性顽疾（下轮修复与编纂必须设硬门禁）**：
   - **病灶 A｜“望文件名／目录名猜作者、书名与卷号”**：本批 4 处 P0 全数由此引发——`CLM-soviet-women-*` 隐去 William M. Mandel (1975)、`CLM-klots-*` / `CLM-lebsky-*` / `CLM-sakharov-*` / `CLM-zhukov-*` 省略全名与原书名、`CLM-carr-1976/1979` 望辩论卡标题错标为 *Socialism in One Country*、`CLM-tragedy-village-1929-*` 隐去 Danilov/Manning/Viola/Ivnitsky 四位主编并虚构不存在的“1929年卷”。
   - **病灶 B｜“为凑卡片主题而改写或中和论断卡原旨”**：02 号卡把一般劳工史卡 `CLM-lebsky-industrial-paternalism-origins-1917-1929` 硬改写为“妇女托育与就业受制”；04 号卡把 Valentin Sakharov (2012) 旗帜鲜明的“《论合作社》两稿断裂—批布哈林—护斯大林”论断洗白成中立文本学；06 号卡把 `CLM-carr-davies-1969-nemchinov-table-critique` 误述为“价格统计”。
   - **病灶 C｜Wave 39 新增馆藏与 `data/DATA-01..08` 系统性漏接**：全批 6 卡仅 05 号卡引用了 1 张数据卡（`DATA-03`），其余 5 张卡**对 `DATA-02`、`DATA-03`、`DATA-04`、`DATA-05`、`DATA-06`、`DATA-08` 零引用**（尤以 06 号卡漏引 `DATA-03` 与 `DATA-06`、03 号卡漏引 `DATA-04`、02 号卡漏引 `DATA-08` 最为可惜）；同时 Wave 39 刚精读入库的 3 组重磅馆藏（`RN-W39-arapovich`、`RN-W39-stalin-era-nep-to-great-turn-1924-1929`、`W39_lenin_1922_1923_docs/`）全批一处未挂。
   - **病灶 D｜`[T2]` 所引 `CLM-*` 与 `[T3]` 所列 `RN-*` 脱节＋核心概念卡漏出 `core_cards`**：01、02、04、05、06 五张卡均存在“矩阵挂了某学者的 `CLM-*`，T3 却漏列该 `CLM-*` 在站内的源 `RN-*`（甚至错列其他时期的 `RN-*`）”现象；04 号卡更把两个同名概念卡 `CON-socialism-in-one-country` 与 `CON-permanent-revolution` 双双漏出 `core_cards`。

---

## 七、全批 6 卡汇总修复动作矩阵（按 P0 → P1 → P2 优先级排布）

| 优先级 | 编号 | 目标卡片 | 具体缺陷与核证依据 | 精准修复动作（单步可执行） |
| :---: | :---: | :--- | :--- | :--- |
| **P0** | `02-01` | `DEB-1920s-gender-family-and-everyday-life` | L25–27 望文件名隐去 Mandel (1975)、Klots (2024)、Lebsky (2021) 真名与原书名；**凭空为 Lebsky 杜撰“妇女托育与就业”论点** | L25 补 `William M. Mandel (1975), Soviet Women` 并注亲苏左翼盲点；L26 补 `Alissa Klots (2024), Domestic Service in the Soviet Union`；L27 补 `Maksim Lebsky (2021), 《苏联的工人阶级：工业家长制下的生活》` 并如实改写为一般工业家长制／ФУБР 住房背景参照 |
| **P0** | `04-01` | `DEB-1924-socialism-in-one-country` | L27 错把 `CLM-carr-1979` 与 `CLM-carr-1976` 标为 `E. H. Carr, Socialism in One Country` | L27 改为 `E. H. Carr, The Russian Revolution From Lenin to Stalin (1979)；Foundations of a Planned Economy, Vol. 3-II (1976)` |
| **P0** | `04-02` | `DEB-1924-socialism-in-one-country` | L28–29 省略 Sakharov (2012) 与 Zhukov (2011) 真名书名；**严重洗白／曲解 Sakharov“两稿断裂—批布哈林—护斯大林”论断** | L28 改为 `Valentin Sakharov (2012), 《站在十字路口》（На распутье...）` 并如实还原“两稿断裂论＋批布哈林＋恢复列宁—斯大林生产合作社连续性”及其局限；L29 改为 `Yuri Zhukov (2011), 《格里高利·季诺维也夫：被遗忘的世界革命领袖》` 并注后苏联现实主义视角 |
| **P0** | `06-01` | `DEB-1929-collectivization-and-dekulakization-causes` | L26 隐去 Danilov 等 4 主编并虚构“1929年卷”；L25 漏 Carr–Davies 1969 书名且把 `nemchinov-table-critique` 误述为“价格统计” | L26 改为 `V. P. Danilov, R. Manning, L. Viola & N. A. Ivnitsky (eds.), 《苏联农村的悲剧》第2卷（1929.11–1930.12，2000）`；L25 补书名年份并更正为“涅姆奇诺夫谷物商品率表批判（中贫农占 74% 商品粮）” |
| **P1** | `01-01` | `DEB-1920-polish-war-and-revolutionary-export` | 漏引站内 Khlevniuk (2015) `ch06_2` 对斯大林 7 月 13/24 日电报的档案拆穿；T3 错配 `RN-W6`/`RN-W20` 而漏 `RN-W22`/`RN-W1C`/`RN-W24`/`DATA-05` | 在 `[T2]` 并列 Khlevniuk (2015) 与 Shearer (2024) 针锋相对的电报解读；T3 补挂 `RN-W22`、`RN-W1C`、`RN-W24`、`ch06_2_in_lenin_s_shadow.md` 与 `DATA-05` |
| **P1** | `01-02` | `DEB-1920-polish-war-and-revolutionary-export` | 4/5 CLM 为间接代挂（漏 Mawdsley Ch. 18 兵力与政治局表决硬数据）；单线化托洛茨基立场；`core_cards` 漏 4 节点 | 补 Mawdsley `ch24_18` 兵力与 7.17/7.23/8.13/8.19 节点；细化托洛茨基战时执行 vs 事后回忆争议；`core_cards` 补 `EVT-1917-1920-ukrainian-revolution-rada-hetmanate-and-sovietization`、`PER-wrangel`、`PER-dzerzhinsky`、`CON-socialism-in-one-country` |
| **P1** | `02-02` | `DEB-1920s-gender-family-and-everyday-life` | 漏挂 Wave 39 `RN-W39-arapovich`（2 张 B 级正统女工卡）、`DATA-08`、Attwood 克鲁普斯卡娅教育卡及 `RN-W35` | `[T2]` 增设苏联正统工业女工对照行挂 Arapovich 两卡（标明 B 级与 `publication_year: null`）；T3 补挂 `RN-W39-arapovich`、`DATA-08`、`RN-W35` 及 `CLM-soviet-citizen-lunacharsky-progressive-pedagogy-1920s` |
| **P1** | `02-03` | `DEB-1920s-gender-family-and-everyday-life` | `core_cards` 仅 3 项；抹平 Klots 对托洛茨基／Goldman 的“家务阶级转嫁与逃离厨房悖论”反驳 | `core_cards` 增补 `POL-first-five-year-plan`、`PER-tomsky`、`PER-kalinin`；L26 浓缩 Klots 核心数据（452,258 名家政女工、莫斯科白领雇主占 77.8%） |
| **P1** | `03-01` | `DEB-1921-trade-union-controversy-and-party-unity` | 连续 3 行复用 Daniels 卡，漏挂 `RN-W35` 中的 Godson (1981) 与 Lebsky (2021) 及 Service (2009) | 第 2 行补 `CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions`；第 3 行补 `CLM-service-2009-trotsky-authoritarian-consensus`；劳工史行补 `CLM-lebsky-industrial-paternalism-origins-1917-1929` 并显化三方交锋 |
| **P1** | `03-02` | `DEB-1921-trade-union-controversy-and-party-unity` | 漏引 `DATA-04`（十大 `336:50:18` 票数）与 `DATA-08` §5.2；`core_cards` 漏 7 节点 | L20 补十大票数；T3 挂 `DATA-04`、`DATA-08`；`core_cards` 补 `MTG-1922-03-11th-party-congress`、`ORG-right-opposition-1928`、`PER-osinsky`、`PER-sapronov`、`EVT-1921-kronstadt`、`PER-bukharin`、`POL-nep` |
| **P1** | `04-03` | `DEB-1924-socialism-in-one-country` | 同名概念卡 `CON-socialism-in-one-country` 与 `CON-permanent-revolution` 双漏出 `core_cards`；漏 `DATA-04`（`559:65`）、Wave 39 列宁两篇原典与 3 篇源 `RN-*` | `core_cards` 补两张同名概念卡＋`ORG-comintern`、`EVT-1927-war-scare-and-opposition-expulsion`、`PER-lenin`；L20/T3 补 `DATA-04`、Wave 39《论我国革命》与《宁肯少些，但要好些》及 `RN-02-sakharov`、`RN-W22`、`RN-W24` |
| **P1** | `04-04` | `DEB-1924-socialism-in-one-country` | `[T2]` 缺“不断革命论”原始卡与 Service/Shlapentokh 反证；第 1 行未直连站内布哈林 1925 原文 | 补挂 `CLM-trotsky-1905-december-uprising-lessons-and-permanent-revolution-defense`、`CLM-service-2009-trotsky-political-tactical-blunders`、`CLM-shlapentokh-bonapartism-fear-against-trotsky` 与 `1925-04_bukharin-road-to-socialism.md` |
| **P1** | `05-01` | `DEB-1928-bukharin-alternative` | 漏挂 Wave 39 泽姆斯科夫与列宁绝笔《宁肯少些，但要好些》、Hunter/Davies (1995)、刘伟/平新乔 (1989)、Sakharov (2012)、Fitzpatrick (1978) | `[T2]` 增补反事实计量与后苏联／改革经济学行；T3 补 `RN-W39-stalin-era-nep-to-great-turn-1924-1929.md`、`RN-W23`、`1923-03-02_lenin-better-fewer-but-better.md` |
| **P1** | `05-02` | `DEB-1928-bukharin-alternative` | T3 漏列矩阵所引 Nove/Kotkin/Khlevniuk/Priestland/Merridale 全部 5 篇源 `RN-*` 及 `DATA-02`/`DATA-04`/`DATA-08` | T3 补挂 `RN-W6-agricultural-crisis`、`RN-W1C`、`RN-W3-politburo`、`RN-W12-revivalist`、`RN-W6-moscow-fall` 与 `DATA-02`/`DATA-04`/`DATA-08` |
| **P1** | `05-03` | `DEB-1928-bukharin-alternative` | `core_cards` 漏 5 张核心卡；L26 弱化 Nove“1927 NEP 死胡同”论断 | `core_cards` 补 `EVT-1928-grain-procurement-crisis`、`EVT-1928-shakhty-affair-show-trial`、`POL-first-five-year-plan`、`CON-primitive-socialist-accumulation`、`PER-uglanov`；L26 点明 Nove 条件性必然与死胡同命题 |
| **P1** | `06-02` | `DEB-1929-collectivization-and-dekulakization-causes` | 全卡未引 `DATA-03`、`DATA-06`、`DATA-08` 任一数据卡，却把已核全国口径混入外部缺口 | L20 补 `DATA-06` 1929.06–12 入庄率节点；T3 挂 `DATA-03`、`DATA-06`、`DATA-08` §1 并收窄 L35 外部缺口界定 |
| **P1** | `06-03` | `DEB-1929-collectivization-and-dekulakization-causes` | 漏挂 Wave 39 泽姆斯科夫直指卡、Shearer (2024)、Goldman (2011)、3 篇源 `RN-*` 及 6 张 `core_cards`（含 `CON-kulak`） | 补挂 `CLM-zemskov-2018-agrarian-tribute-and-coercive-turn`、`CLM-stalin-war-1927-1929-threat-and-collectivization`、`CLM-goldman-2011-great-turn-industrialization-and-wrecking`、`RN-W39`、`RN-W8`、`RN-W1C`、`RN-W3-industrialization`；`core_cards` 补 `CON-kulak` 等 6 卡 |
| **P2** | `01-03` | `DEB-1920-polish-war-and-revolutionary-export` | 哈雷演说时间定位与斯大林 7.24 信件分歧提示不足 | L26 注哈雷演说在华沙败退两月后；L31 注 Shearer vs Khlevniuk 对 7 月电报的对立解读 |
| **P2** | `02-04` | `DEB-1920s-gender-family-and-everyday-life` | `era: "1917-1929"` 与 `start_ns: "1918-01-01"` 差一年 | 将 `start_ns` 调至 `"1917-12-31"` 或正文注明起于 1918 法典成文 |
| **P2** | `03-03` | `DEB-1921-trade-union-controversy-and-party-unity` | `era` 与 `dates` 跨度说明、第 7 条首次公开日及 L25 措辞 | 注明制度延至 1929；L25 改“列宁与‘十人纲领’”；T3 补第 7 条于 `1924-01-17` 十三次代表会议首次公开 |
| **P2** | `04-05` | `DEB-1924-socialism-in-one-country` | 未标明斯大林 1924-04 旧公式与 1924-12 改口时差 | L20 补三步文本转向时序 |
| **P2** | `05-04` | `DEB-1928-bukharin-alternative` | L28 三学者缺全名与书名 | 补全 Khlevniuk、Priestland、Merridale 全名与书名 |
| **P2** | `06-04` | `DEB-1929-collectivization-and-dekulakization-causes` | L27–28 四学者缺全名与书名 | 补全 Velikanova、Kotkin、Erlich、Nove 全名与书名 |

---

*审计完毕（纯只读审计，仅写入本报告文件 [`audits/AUD-18B-wave40-codex-deb-batch2-audit.md`](file:///C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/audits/AUD-18B-wave40-codex-deb-batch2-audit.md)）。*

