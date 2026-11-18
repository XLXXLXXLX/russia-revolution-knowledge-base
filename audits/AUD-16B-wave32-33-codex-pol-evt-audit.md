# AUD-16B｜Wave 32–33 Codex 政策与事件卡片异源对勘审计（7 张）

- 审计身份：dialectic-auditor（史学史对勘与反偏见），异源交叉审计（GPT-6.1-Terra 撰写 → Claude 审计）
- 审计日期：2026-11-18
- 审计性质：**纯只读**；本文件为唯一写入物，未改动任何被审卡片、札记、数据卡或共享总表
- 对照标准：[`AUD-15A-wave32-33-codex-people-cards-audit.md`](AUD-15A-wave32-33-codex-people-cards-audit.md)（P0 史实/历法/断链/挂错来源；P1 站内 S/A 漏引/口径失准/学派失衡；P2 Schema 与悬空尾句）
- 写盘进度：**阶段一（01–04 号）与阶段二（05–07 号 + 汇总修复矩阵）均已完成**

## 0. 方法与通用结论（01–04）

1. **断链核查**：用脚本抽取各卡全部 `ID` 样式节点与站内相对链接，逐一对库内文件名/路径比对。01–04 号卡 YAML `related_debates`、2.2 边表节点 ID、T3 路径**全部真实存在，无悬空断链**（`DEB-1914-haimson-thesis-stability`、`POL-october-manifesto-and-1906-fundamental-laws`、`ORG-psr`、`POL-war-communism`、`PER-sokolnikov`、`POL-nep`、`DATA-02-…` 均命中）。
2. **历法核查**：01–04 号 YAML `dates` 全用 `start_ns/end_ns`，符合 `docs/TEMPLATES.md`；正文双历对均满足 1905–1918.01 `+13` 天规则（见逐卡）。
3. **共性缺陷**：(a) T2 的“史学争鸣光谱”普遍以匿名学派（“现代化解释”“农民社会史”“工业投资视角”）代替具名学者与站内定位；(b) 多处把站内**已有**数字/原文误写成“待核”或误挂出处（01 号 Figes 数字、04 号 Pipes 官方伤亡数）；(c) 04 号边表未用节点 ID。

---

## 01｜[`POL-stolypin-agrarian-reform.md`](../cards/policies/POL-stolypin-agrarian-reform.md)

**总判**：历法与断链 ✅；核心统计口径 **出处错位（P1）**；学派偏窄（P1）。无 P0。

### 历法/节点核查
| 项 | 结果 |
| :--- | :--- |
| `1906-11-09 [O.S.] / 1906-11-22 [N.S.]`、`1910-06-14/06-27`、`1911-05-29/06-11` | `+13` ✅；`start_ns: 1906-11-22` 与第 9 日法令对应 ✅（Carr 卷二 ch03 L376 亦记 1906-11-09 法令） |
| `end_ns: 1917-11-08` | 对应 `1917-10-26 [O.S.]` 土地法令；T3 已声明仅为“转折锚”，可接受（P2 见下） |
| 边表 4 个节点 + `DEB-1914-haimson-thesis-stability` | 全部存在 ✅ |

### 发现
- **P1-01-1｜Figes 关键统计挂错章节，并绕开站内原文**
  - 卡片 L27 称“据Figes…27%–33%…约15%完成土地合并”，T3 L44–45 只挂 `figes…/ch16_9_…` 与**站外** OECD 报告引 Figes，称“需核其原始统计口径”。
  - 站内核实：该两数字实际在 [`ch13_6_last_hopes.md` L171](../sources/monographs/figes_1996_peoples_tragedy/ch13_6_last_hopes.md)：“*Between 1906 and the eve of the revolution something in the region of 15 per cent of all the peasant households in European Russia consolidated their land as private plots, either in groups or individually, bringing the total of peasant farms in hereditary tenure to somewhere between 27 and 33 per cent*”，并紧接说明实施“**1909–10 年后明显回落**”（同段前句）。`ch16` L78 仅有“up to one-third → less than 2 per cent”。
  - 影响：口径校准其实可在站内一步完成（分母＝欧俄农户；15% 为 1906 起新增“合并为私有地块（成组或个体）”，27–33% 为世袭持有总存量；并非 `khutor`）。卡片现写“其中约15%”易使读者误以为 15% 是 27–33% 内部的 `khutor`/`otrub` 子集。
  - **修复**：T2 L27 改引 `ch13 L171` 与 `ch16 L78` 双锚；补“1909–10 后回落”；OECD 链接降为“二手转引”备注；明确 15% 含“成组或个体”两类、不等同 `khutor`。
- **P1-01-2｜学派失衡：缺苏联—列宁式评价、缺贵族/政治维度、缺 L2 年表对勘**
  - 站内已有但未用：
    1. [`carr_bolshevik_rev_v2_zh/ch03_第四部分_经济秩序_part_1.md`](../sources/monographs/carr_bolshevik_rev_v2_zh/ch03_第四部分_经济秩序_part_1.md) L376–430：Carr 称改革是“农奴解放进程的逻辑延续”，并引列宁“普鲁士式 vs 美国式道路”及“对广大农民意味着毁灭”的判断（L399–430）——正是卡片 `perspectives_present` 所缺的**马克思主义/苏联正统**评价轴。
    2. `manning_1982_crisis_old_order_zh/ch18_12斯托雷平与两届杜马间歇期_右翼的政治巩固.md`（120 处提及，L827 论地主与村社土地）：贵族—右翼对土地改革的支持/抵触。
    3. [`timeline/L2_chronicles/E04_1907-1914_stolypin_and_labor_upsurge.md`](../timeline/L2_chronicles/E04_1907-1914_stolypin_and_labor_upsurge.md) L18：Pipes 年表把土地措施拆成 `1906-08-12/-08-27 [O.S.]`（最初土地措施）与 `1906-11-09`（村社土地），并明确“**8 月两项不并进这一天**”。卡片只立 11-09 为 `start_ns`，T2 未交代 8 月措施与 E04 的口径分野。
    4. `CLM-hildermeier-2000-azev-affair-and-stolypin-era-paralysis`：Stolypin 时代视角；卡片目前挂的 `CLM-hildermeier-2000-agrarian-socialism-modernization-dilemma` 的 `targets_cards` 为空，且主旨是社革党纲领而非改革绩效。
  - **修复**：T2 2.3 增“苏联/列宁式评价”一条（Carr 卷二 ch03 L399–430），“现代化解释”须给具名站内锚点（现无；若站内无专门现代化派专著，应在 T3 明示“该派未入库”，并保持 `perspectives_missing`）；补 E04 L18 的 8 月措施分野一句。
- **P2-01-3**：`related_debates: [DEB-1914-haimson-thesis-stability]` 但 T2/T3 **从未出现 Haimson 稳定论点**，属悬空关联；要么补一句“与 Haimson 1914 稳定论的关系：土地改革是否构成稳定基础”，要么删去。
- **P2-01-4**：T1 结尾“改革并未消除农民的土地渴求”为断言，未挂证据；建议挂 Figes ch12 L224（1905–6 年近 3,000 处庄园被毁，约占 15%）或 ch16。

---

## 02｜[`POL-decrees-on-peace-and-land-1917.md`](../cards/policies/POL-decrees-on-peace-and-land-1917.md)

**总判**：史实与历法 ✅（对勘 S 级原典无误）；L3 漏引与“待核”过度（P1）；`start_ns` 与 L3 时间规则有张力（P2）。无 P0。

### 与 S 级原典逐项对勘
对照 [`1917-10-26_decrees-on-peace-and-land.md`](../sources/web-archive/E02_E10_core_classics/1917-10-26_decrees-on-peace-and-land.md)（`epistemic_tier: S`）：

| 卡片断言 | 原典 | 结论 |
| :--- | :--- | :--- |
| 和平法令一致通过；土地法令 1 票反对 8 票弃权 | 原典编注 L19 同 | ✅ |
| 第 4 条纳入 242 份委托书汇编（《消息报》第 88 号） | L144/L214/L292 | ✅ |
| 和平法令载 `1917-10-27 [O.S.]/11-09`、土地法令载 `10-28/11-10` | 编注“《真理报》第170/171号” | ✅ |
| “1957 汇编标题为 26 日夜间 2 时” | L19、L30 同 | ✅ |
| 和平“建议停战不少于三个月、非最后通牒” | 同 | ✅ |

### 发现
- **P1-02-1｜站内 L3 已细化通过时刻，卡片仍写“具体钟点待核”（T2 L25、T3 L46）**
  - [`timeline/L3_daily/1917-10_october_insurrection.md`](../timeline/L3_daily/1917-10_october_insurrection.md) L235（21:00 第二次会议开幕、《和平法令》一致通过）、L241（约 23:00 起列宁报告土地法令）、L249（**凌晨 01:00 后表决通过**，署日按会议起始日写作“10 月 26 日”，实际物理表决在 27 日凌晨）；原典 L19 另记**闭幕于 27 日凌晨 5 时 15 分**。
  - 因此“26日夜间2时”并非与跨夜记述矛盾，而是**按会议起始日署日**的刊本标注；卡片把它写成“日期表达张力…待核”夸大了不确定性。
  - **修复**：T2 L25 改为“和平法令约 `1917-10-26 [O.S.]` 21 时后通过；土地法令在 `1917-10-27 [O.S.] / 1917-11-09 [N.S.]` 凌晨（L3 记 01:00 后；汇编题注‘26 日夜间 2 时’按会议日署）通过；闭幕约 05:15（原典编注）”。T3 L45–46 补挂 L3 L235–249 与 L303 的 Sukhanov ch30 指针。
- **P1-02-2｜匿名学派：三条光谱均无具名学者与站内页码**
  - L3 L241 已记录 Sukhanov 当场指出布尔什维克“照搬并兑现了长期嘲讽的民粹派/社革党土地纲领”（站内 `sukhanov_1922_personal_record/ch30_part_vi_the_october_insurrection_october.md`）；`lewin_1968_peasants`、`rabinowitch_1976_come_to_power_zh` 亦在库。卡片的“农民社会史/政党与思想史”可具名化为：Figes ch16（夺地先于法令）、Sukhanov（同时代批评者视角）、Rabinowitch/Lewin（待核章节）。
  - **修复**：2.3 每条至少挂 1 个站内定位；否则在 `perspectives_missing` 补 `soviet-orthodox`（现缺，Soviet 叙事把土地法令视为列宁“给农民的赠礼”的典型框架未被描述，只做“反向”修正）。
- **P2-02-3｜`start_ns: 1917-11-08` 与 L3 三原则不一致**：L3 L11 规定“物理执行入实际所属新日”，则土地法令通过日应记 `1917-11-09 [N.S.]`；和平法令为 `11-08`。建议在 T1/T3 明示 `start_ns` 取**会议开幕/和平法令日**，土地法令另注 `11-09` 凌晨，避免与 Stolypin 卡 `end_ns: 1917-11-08` 同口径误读为“土地法令于 11-08 通过”。
- **P2-02-4**：`related_debates: []`，建议核对是否有“土地法令吸收社革纲领”相关 DEB（见阶段二汇总）。
- **P2-02-5**：边表 `PER-lenin | proposed-and-defended | 1917` 的“核心依据”为“原档与列宁大会报告”，建议改为具体文件锚（原典 L19 / `1917-10_october_insurrection.md` L235–241）。

---

## 03｜[`POL-sokolnikov-chervonets-monetary-reform.md`](../cards/policies/POL-sokolnikov-chervonets-monetary-reform.md)

**总判**：站内数据核对**基本准确**；但存在 **站外百科承载日期（P1）、视角标签失实（P1）、分母链与 L3 未纳入（P1）**。无 P0。

### 与 DATA-02 / 札记逐项对勘
| 卡片断言 | 站内锚点 | 结论 |
| :--- | :--- | :--- |
| 25% 贵金属及稳定外币 + 其余商业资产担保 | DATA-02 L97；`RN-W32-katasonov…` L59 | ✅ |
| 储备 1923 初约 1,500 万 → 1924 初约 1.5 亿金卢布 | DATA-02 L97–98（15 → ≈150，Carr `p.140`） | ✅ |
| 1923 秋约 75% 切尔文集中于国营托拉斯与企业金库 | DATA-02 L91（Carr `p.41`） | ✅ |
| 1924 年 `50,000 枚 1923 式卢布 : 1 金卢布` 收兑 | DATA-02 L55（`pp.141–142`） | ✅ |
| 1、3、5 卢布国库券，10 卢布兑 1 切尔沃涅茨 | Katasonov RN L59；`CLM-katasonov-golden-chervonets-rise-and-demise` 论证链第 1 条（`ch54#L19-L26`）同 | ✅ |
| 1922-10-11 授权法令 | 站内仅有“1922 年 10 月获准”（RN L59） | ⚠ 见 P1-03-1 |

### 发现
- **P1-03-1｜`start_ns: 1922-10-11` 的精确日在站内无锚；T3 又以 encyclopedia.com 条目承载 1926-06-09 / 1930 日期**
  - 站内 Katasonov 札记只写“1922 年 10 月获准发行”。精确到日的 `1922-10-11` 来自卡片外（通行文献口径），而 T3 L45 自己写“授权法令…均待逐项核验”，却已把它写进 YAML `start_ns`——YAML 精度高于证据精度。
  - T3 L45 用 [encyclopedia.com 条目](https://www.encyclopedia.com/history/encyclopedias-almanacs-transcripts-and-maps/chervonets)作“1926年6月9日禁令/1930年进一步限制”的唯一出处。按 AGENTS.md 对通用百科“不得承担证据”的规则（15A 同标准），应降级为线索。
  - **修复**：`start_ns` 保留，但在 T3 加“站内仅 10 月，日期取自外部通行口径，待原令”；删去 6 月 9 日具体日期或写“外部线索，非证据”；结尾 L46 的 `end_ns: 1924-03-31` 建议对齐 DATA-02 L55 的“1924 年 2–3 月币制改革收口”表述（站内口径是月段而非月末）。
- **P1-03-2｜`perspectives_present: archival-post-soviet` 与实际来源不符**
  - 卡片实际承重来源为 Carr *Interregnum*（经 DATA-02）与 Katasonov（`source_tier: B`，国家主义—东正教—“斯大林经济”叙事，见 `CLM-katasonov-golden-chervonets-rise-and-demise`）。二者均非“后苏联档案史学”。卡片 2.3 已提醒 Katasonov 储备系列“内部口径和算术问题”，但 YAML 标签反向美化。
  - **修复**：改为 `["monetary-history", "fiscal-policy", "western-documentary-carr", "statist-nationalist-katasonov"]`；`perspectives_missing` 保留 `primary-decree-text`，增 `soviet-era-and-post-soviet-archival-monetary-studies`。
- **P1-03-3｜漏用站内“分母链”与剪刀差节点（统计口径核心）**
  - DATA-02 §2.1 给出**三量纲分离**：切尔文占全部流通纸币**价值**比重 `1923-01-01 ≈3%（3.5/116.5）→ 1923-07-01 ≈37%（70/188）`；DATA-02 L55 的面额重估链：`1 枚 1923 式卢布 = 100 万枚旧苏维埃卢布`，`1 金卢布 = 50,000 枚 1923 式 = 5×10¹⁰ 旧卢布`；`1 切尔文 = 10 金卢布 = 7.74234 克纯金`。卡片只用了 75% 与储备，未给“3%→37%”这一最关键的“并行过渡”量化，也没有把“汇率分母”三层写清。
  - DATA-02 L50–53：1923-08 末国家银行收缩信贷、1923-09 恢复无限制印发苏维埃卢布——说明“并行期”币制稳定并非单线；站内 L3 [`1923-10_scissors_and_new_course_crisis.md`](../timeline/L3_daily/1923-10_scissors_and_new_course_crisis.md) 为同期对应卷，卡片未挂。
  - **修复**：2.1 “从通胀到双币”补“3%→37%”及三量纲提示；T3 补 L3 1923-10 与 DATA-02 §1.3。
- **P1-03-4｜学派/来源未具名，缺 Preobrazhensky/Gosplan 一侧**
  - 2.3 “工业投资视角”无具名与站内锚点。站内有 `RN-W10-other-side-of-nep-and-zinoviev-arc.md` L28–30（Sokolnikov 紧缩 vs 计委/工业扩张）、`primary/preobrazhensky_1926_new_economics_zh`、`bukharin_preobrazhensky_debate_zh`、`CLM-other-nep-1923-sokolnikov-monetary-discipline`、`CLM-katasonov-golden-chervonets-rise-and-demise`（1925 初账面储备 3.44 亿、贵金属 1.806 亿）。
  - **修复**：2.3 具名化：财政稳定视角→Carr/DATA-02 与 RN-W10；工业投资视角→Preobrazhensky/Gosplan（先核对站内相应章节）；Katasonov 视角→CLM-katasonov 并引其 1925 初 3.44 亿账面数作“口径差异”例。
- **P2-03-5**：边表“核心依据”含 `AUD-14`（审计文件，非节点）；应替换为 DATA-02/RN 路径。`related_debates: []` 与 Sokolnikov–Gosplan 之争并存，阶段二汇总再核 DEB 存在性。
- **P2-03-6**：T3 L44 称“`AUD-14` 第16-03项明确警告不要把改革写为金币普遍流通”——属审计内部引用，不宜作历史证据来源。

---

## 04｜[`EVT-1905-01-bloody-sunday.md`](../cards/events/EVT-1905-01-bloody-sunday.md)

**总判**：历法 ✅；请愿书版本说明 ✅；**官方伤亡数“未核”与站内 Pipes 原文冲突（P1）**；**边表无节点 ID（P1）**；罢工人数时点错位（P1）。无 P0。

### 历法与 S 级原典
- `1905-01-03 [O.S.] / 01-16 [N.S.]`（罢工）、`1905-01-09 [O.S.] / 01-22 [N.S.]`（枪击）均 `+13` ✅；`start_ns 1905-01-16`、`end_ns 1905-01-22` ✅。
- 对照 [`1905-01-09_gapon-petition.md`](../sources/web-archive/E02_E07_foundational_docs/1905-01-09_gapon-petition.md)（`epistemic_tier: S`）：俄文为 1925 托洛茨基文集附录、英文为加邦 1906 回忆录且较短——**卡片 L51 版本说明与编注完全一致 ✅**。

### 发现
- **P1-04-1｜官方伤亡数“具体报告未核”，但站内 Pipes 已给出数字与脚注出处**
  - 卡片 L46：“另有约130死的官方数字流传，但具体报告、统计时点和适用范围未核”。
  - 站内：[`pipes_1990_russian_rev/ch09_section.md`](../sources/monographs/pipes_1990_russian_rev/ch09_section.md) L291：“*journalists spoke of 4,600 killed and wounded, the best estimate is 200 killed and 800 injured*”；L705 脚注 239：“*The official figure was **130 dead and 299 wounded**: A. N. Pankratova…*”。即官方数应写 **130 死 / 299 伤（Pipes 引 Pankratova）**。
  - 同时 [Figes `ch12_5_first_blood.md` L195](../sources/monographs/figes_1996_peoples_tragedy/ch12_5_first_blood.md) 原文为“*the true figures were **probably** in the region of 200 killed and 800 wounded*”——是**估计**，**并未**声称档案逐项核算。L3（`1905-01…` L72）与 DATA-01 L30 称其“据医院及官方档案核查”，属**L3 过度解读**；卡片 L47“其档案计算方法仍须回到原书”沿用了该预设。
  - **修复**：T3 3.1 改为四口径并列：`96死/333伤`（L3 记“官方初报”，原始出处站内未定位）；`130死/299伤`（Pipes n.239 引 Pankratova，苏联史学家的官方数）；`≈200死/≈800伤`（Figes“probably”、Pipes“best estimate”，二者为估计而非档案普查）；`4,600 死伤合计`（记者/Trotsky 转述，非死亡数）。并回写 DATA-01 L30（当前只有三口径，缺 130/299）——**数据卡漏项建议单列修复**。
- **P1-04-2｜2.2 边表使用中文名而非节点 ID**
  - L34–36 的“加邦与工人大会/尼古拉二世与军政机关/1905年革命”均为自然语言；站内已存在 `PER-gapon`、`PER-nicholas-ii`、`EVT-1905-revolution`（`cards/` 实测命中）。其他政策卡边表均用 ID，本卡图谱不可解析。
  - **修复**：改为 `PER-gapon | mobilizes`、`PER-nicholas-ii | suppresses`、`EVT-1905-revolution | catalyzes`，保留说明列；另可增 `EVT-1905-12-moscow-armed-uprising`（后续链）。
- **P1-04-3｜罢工人数时点错位**：L27 “1905-01-03 …罢工…迅速蔓延全城；托洛茨基事后记约14万人参加”。DATA-01 L26–30：1 月 3 日仅 Putilov 约 1.2–1.3 万工人企业罢工；`15,000–26,000`（1 月 4 日）→`100,000–150,000`（1 月 6 日，Trotsky 10.5–14 万）→`140,000`（**1 月 7 日 [O.S.]/01-20 [N.S.]**）→游行队伍约 `150,000`（1 月 9 日）。DATA-01 L33 明确“不同统计时刻，非矛盾”。卡片把 14 万挂在 1 月 3 日叙述句尾，易被读成起始日人数。
  - **修复**：改为“至 `1905-01-07 [O.S.] / 01-20 [N.S.]` 托洛茨基记约 14 万人罢工；游行当日约 15 万人（DATA-01）”，并补“全国一月近 50 万”（L3 L80、DATA-01 L31）。
- **P1-04-4｜学派/出处偏窄，且 Figes/Pipes 未直接链接**
  - `perspectives_present` 含 `revolutionary-memoir`（仅 Trotsky）与 `liberal-institutional`（卡片无自由派来源）；2.3 提到 Figes/Pipes 但 T3 只链 Trotsky 札记。
  - **修复**：T3 直挂 Figes ch12 L195、Pipes ch09 L291/L705；站内可补工人组织史背景（`bonnell_1983_roots_of_rebellion_zh`、`zelnik_1999_workers_intelligentsia`——章节待核）；`liberal-institutional` 若无来源应从 present 移至 missing（或以 L3 Gorky 集会一句为证）。
- **P2-04-5**：L27 “要求…普选产生的立宪会议”：原典编注/L3 L43 指明俄文附本列“**普遍、平等、秘密**”选举，加邦英文本仅“普选”；卡片 L51 已述版本差异，但 L27 正文未取俄文口径，建议统一。
- **P2-04-6**：普梯洛夫四名工人系 **1904-12 下旬**被解雇（其中一人稍后复职，L3 L27），卡片仅写“1905-01-03 因解雇四名工人而罢工”，可补一句时点，避免读者误为 1 月内解雇。

---

> 阶段一结束（01–04 号）。阶段二将追加 05–07 号及汇总修复矩阵。

---

# 阶段二（05–07 号）

> **阶段二补充的跨卡发现（回溯修正阶段一）**：
> 1. `historiography/debates/` 已有 **`DEB-1906-stolypin-wager-and-agrarian-viability`**（`core_cards` 即 `POL-stolypin-agrarian-reform`，含现代化乐观论 / 农民社会史 / **马克思主义道路论** 三栏矩阵）；01 号卡的 `related_debates` 却只挂了 `DEB-1914-haimson-thesis-stability`（该 DEB `core_cards: []`，主旨是战前劳工稳定/双重极化，`perspectives_missing` 反而列 `rural-social-history`）。→ **01 号追加 P1：debate 挂错、漏挂正主**（见矩阵 A-1）。阶段一 P2-01-3 的“补 Haimson 一句或删去”升级为“替换为 DEB-1906，Haimson 可作次要关联”。
> 2. 02/03 号无专属 DEB，不构成缺陷；04 号无专属 DEB（`DEB-1914` 同样不合适，不建议挂）。
> 3. 本阶段核实：站内**无**独立成文的“列宁 1922-03-19 致政治局（莫洛托夫转）信”原文，也**无**独立成文的《关于民族或“自治化”问题》S 级原典（`1922-12_letter-to-the-congress.md` 只收《给代表大会的信》及补充，仅在注释/清单中提及民族问题札记）。凡本卡称“信件原文待核”**属实**，但站内**间接引文与转述并不缺**（见 05、06 号）。

---

## 05｜[`EVT-1921-1922-volga-famine-and-church-valuables-crisis.md`](../cards/events/EVT-1921-1922-volga-famine-and-church-valuables-crisis.md)

**总判**：**存在 P0（T3 挂错无关札记并据以归属派普斯论点）**；站内 Figes / Loginov / 斯大林文献集已有的数字与时序被误标“未核”（P1）；边表无 ID、`dates` 为年界占位（P1/P2）。

### 历法
- 全部 1922 事件均为 **纯公历**（1918-02-14 后）：`1922-02-23`、`1922-03-19` 写法正确 ✅，无多余 `[O.S.]`。
- `start_ns: 1921-01-01` / `end_ns: 1922-12-31` 为**年界占位值**，不对应任何站内事件锚点（见 P2-05-6）。

### 发现
- **P0-05-1｜T3 L50 挂错无关札记，并据此把“政治史/意识形态敌意”归给派普斯（2.3 L41）**
  - 卡片 T3 列出 [`RN-W5-peasant-soldier-revolution-and-tragedy.md`](../reading-notes/figes_1996_peoples_tragedy/RN-W5-peasant-soldier-revolution-and-tragedy.md) 与 [`RN-W4B-patrimonialism-and-october-coup.md`](../reading-notes/pipes_1990_russian_rev/RN-W4B-patrimonialism-and-october-coup.md) 作为“广义革命与政策解释”出处。全文检索（`饥荒|教会|Pomgol|ARA|赈|饥|季洪|牧首`）：**两份札记均零命中**——前者讲 1917 农民/士兵革命，后者讲家产制与十月政变，均与 1921–22 饥荒、教会珍宝无关。
  - 站内 Pipes 原书（`pipes_1990_russian_rev`）只在 `ch07_introduction.md` L19 一句“the famine of 1921, which claimed the lives of over five million people”，**未见**教会珍宝战役论述。因此 2.3 L41“派普斯一类政治史解释强调意识形态敌意与国家打击教会的计划”**站内无依据**（卡片虽补了“不能扩大为灭绝计划”，但前提论点本身未落地）。
  - **修复**：删除两札记链接；把“派普斯”改为“政治史解释（站内以 Loginov/Service 类传记文本为证）”，或明确“该论点未在站内原文核得，仅保留为外部待核线索”。
- **P1-05-2｜“未能逐页核实菲格斯具体数字”——但站内 Figes 已有完整数字与时点**
  - [`figes_1996_peoples_tragedy/ch23_16_deaths_and_departures.md`](../sources/monographs/figes_1996_peoples_tragedy/ch23_16_deaths_and_departures.md) L27、L30、L39–48：饥荒致死 **约 500 万**（“single biggest killer of these years”）；1921 春“**四分之一农民**”挨饿；萨马拉省近 200 万人（四分之三人口）“被称将饿死”，**其中 70 万人实际死亡**；莫斯科直到 **1921 年 7 月**才承认饥荒，且乌克兰饥荒期间仍向伏尔加输出粮食；高尔基 **7 月 13 日**呼吁，**赈饥委员会（Pomgol）7 月 21 日**成立，是“共产党统治下第一个也是最后一个独立社会团体”，后被列宁下令解散；**ARA 1922 夏高峰日供 1,000 万人，总成本 6,100 万美元**。
  - Pipes `ch07_introduction.md` L19 亦给出“逾 500 万”；`reading-notes/…/RN-W6-civil-war-heartland-and-1923-scissors`（L94）记 1921–22 饥荒约 500 万并与 Lorimer 总超额死亡 1,600 万作分母对照。
  - **修复**：3.1 删“未能逐页核实菲格斯”，改为：“Figes 全国口径约 500 万死亡（ch23 L27）；萨马拉 70 万死亡（L30）；Pipes 同为‘逾 500 万’；受灾/挨饿/受援/死亡为不同量纲”，并把站内 `RN-W6` 的 1,600 万分母写入“分母”提示。
- **P1-05-3｜教会珍宝战役的时序已有站内文本，卡片仍写“信件原文及执行链待逐项核对”，且缺关键日期与执行数字**
  - [`loginov_lenin_bio_zh/ch08_第三部_以此胜之.md`](../sources/monographs/loginov_lenin_bio_zh/ch08_第三部_以此胜之.md)：L850 **`1922-03-16` 政治局在得知舒亚事件后决议“没收工作尚未准备好，至少有些地方需推迟”**；L857–865 **`1922-03-19` 信**：“正是现在、而且只有现在，当饥饿地区在吃人……我们能够（因此也应当）以最疯狂、最无情的精力进行教会贵重物品的没收”，目的是争取农民“同情或至少中立”，且**不触动牧首本人**，对象为“舒亚的叛乱者”及莫斯科等地“最有影响、最危险的黑色百人团分子”；L867 `1922-03-20` 政治局带修改通过托洛茨基 3 月 17 日指示草案，且否决 GPU 逮捕吉洪的提议；L890 `1922-04-12` 政治局表决吸收安东尼主教参与变现；**L886 处决数**：莫斯科 5、彼得格勒及省 4、舒亚 3、斯摩棱斯克 5（另新切尔卡斯克 5、托木斯克 7 等判死刑）。L844：牧首 `1922-02-28` 呼吁书。
  - [`sources/primary/stalin_major_documents_zh/ch03_pages_91-120.md`](../sources/primary/stalin_major_documents_zh/ch03_pages_91-120.md) L280–292（图注）：**3 月 15 日舒亚教堂数名守堂教民被杀后**，政治局开会，列宁与托洛茨基缺席，以斯大林为首多数**投票停止进一步没收**；一周后列宁与托洛茨基说服同志们继续——另给出 Stalin 1928-12-04 对工农通讯员讲话为间接证据。注意：该图注称“3 月 15 日后开会”，Loginov 记决议在 `03-16`，应并列处理，不宜混写。
  - 卡片的叙事（“舒亚冲突后列宁主张借机严厉打击”）方向正确，但**舒亚事件日期（`1922-03-15`）、`03-16` 暂缓决议、`03-20` 修改后指示、斯大林在 `03-16` 前后位置**均缺失；这些恰是“列宁个人意图 vs. 政治局集体决策”史学争议的核心（Loginov 明确站在“反对把信等同于消灭教会”一侧，Pipes 类叙述相反）。
  - **修复**：边表第 4 行 `1922-03` 改为 `1922-03-15 → 03-20`，补三个日期节点与 Loginov/Stalin-docs 双引；2.3 把“列宁信件证明政治意图”与 Loginov 的限定性解读并置，标明“以站内间接引文为据，原信全文未入库”。
- **P1-05-4｜2.2 边表使用自然语言节点，且站内已有可用 ID**：`战时征粮与乡村 / 高尔基、赈饥委员会与ARA / 全俄中执委与东正教会 / 列宁与党领导层`。可映射：`POL-war-communism`、`PER-gorky`、`PER-lenin`、`PER-trotsky`、`PER-stalin`、`POL-nep`、`PER-molotov`（均已存在）；`Pomgol/ARA/东正教会/季洪` **站内无卡片**，应在 `[T3]` 注明“节点缺口：建议新建 ORG/EVT 卡”，不要用悬空 ID 凑数。
- **P1-05-5｜统计口径**：T3 L47 罗利数字（`2,070,560 人 / 68%`、伏尔加德意志人区 `≥15 万死亡`）与 `RN-W32-provincial-smolensk-tambov-saratov-1917-1929.md` L118 一致 ✅；但该札记还记载“1920–1921 年近 90% 定额强征叠加干旱、播种面积仅及 1914 年 56%、1923 年 1 月仍 30% 人口挨饿”，卡片因果链“征粮、减种、战争与干旱的相对权重因地区而异”宜附此条作地方实证，避免只有中性措辞。
- **P2-05-6**：`start_ns/end_ns` 年界占位。建议锚定：`start_ns` 取 Figes 的“1921 年 7 月政府承认饥荒/高尔基呼吁/Pomgol 成立”节点之一（并说明“灾情自 1921 春已起”），`end_ns` 取 `1922-12`（ARA 业务收官日期站内未载，不应臆造）。
- **P2-05-7**：`related_debates: []`，建议关联 `DEB-1918-war-communism-ideology-or-emergency`（灾因中“征粮”权重）与 `DEB-1921-kronstadt-and-nep-origins`（粮食税与饥荒的时序），均已存在。
- **P2-05-8**：2.1 “全俄赈饥委员会…1921 年即被解散”✅（Figes ch23 L44–46），建议补其与列宁“因 ARA 谈成后下令解散”的因果链（L46），并注 Loginov L183（`1921-08-26` 列宁否决逮捕、转交材料）作对读。

---

## 06｜[`EVT-1922-georgian-affair-and-ussr-formation.md`](../cards/events/EVT-1922-georgian-affair-and-ussr-formation.md)

**总判**：核心历法、时序、学派呈现 **质量最好的一张**；但 `related_debates` 漏挂两个已有专属 DEB（P1）、**列宁口述文献“待核”可在站内部分闭合（P1）**、`start_ns` 无锚、边表无 ID（P1/P2）。无 P0。

### 历法与时序核对（站内锚点）
| 卡片断言 | 站内锚点 | 结论 |
| :--- | :--- | :--- |
| `1922-09-26` 列宁致加米涅夫、`1922-10-06` 中央全会 | L3 `1922-12…` L75、L25（“10 月 6 日中央全会”）；E08 L38 | ✅ |
| 1922-10 格共中央辞职（`10-21`/`10-22`） | Carr RN L63；Lewin CLM L25；E08 | ✅ |
| 殴打卡巴希泽在 **11 月**（辞职之后） | Smith CLM L24（1922 年 11 月）、Lewin CLM L25（“11 月底”）、E08 | ✅ 顺序正确；译名不一（卡巴希泽/卡巴尼泽/Kobakhidze），建议统一并注异写 |
| `1922-12-30` 首届全苏苏维埃大会通过宣言与条约 | L3 `1922-12…` L75 | ✅ |
| 口述 `1922-12-30` 至 `12-31` | L3 `1922-12…` L76；CLM-spitsyn（RN-W32 L60） | ✅ |
| Smith 派遣定于 `1922-11-24`，Carr 前置至夏季 | Carr RN L63；E08 记“11 月 25 日出发” | ✅ 并存；建议在 T3 注 E08 的 `11-25` |

### 发现
- **P1-06-1｜`related_debates: []`，漏挂两个已存在的专属 DEB**
  - [`DEB-1922-lenin-testament-and-stalin-rise`](../historiography/debates/DEB-1922-lenin-testament-and-stalin-rise.md)（`perspectives_present` 含 `archival-post-soviet / kotkin-source-skepticism / sakharov-pseudo-lenin-polemic`，缺 `soviet-orthodox`）与 [`DEB-1923-nationality-and-empire`](../historiography/debates/DEB-1923-nationality-and-empire.md)。卡片正文已涉口述真伪与民族政策分歧，应显式关联。
  - **反向断链（卡外，需同步修）**：`DEB-1923-nationality-and-empire.core_cards` 写的是 `EVT-1922-georgian-affair` 与 `EVT-1922-ussr-formation`——**这两个 ID 在库内均无对应文件**（实测 False），实际卡片 ID 为 `EVT-1922-georgian-affair-and-ussr-formation`。属 **P0 级悬空断链（位于 DEB 文件而非本卡）**，建议在修 06 号时一并把 DEB 的 `core_cards` 改为实 ID。
- **P1-06-2｜“口述材料作者身份/传抄链须核对”——站内已有可闭合证据**
  - [`1922-12_letter-to-the-congress.md`](../sources/web-archive/E06_E10_turning_points/1922-12_letter-to-the-congress.md)（`S` 级）编注：L14（六次口授定年，据《列宁全集》俄文第 5 版第 45 卷页码）、L150（`12-27~29` 记“关于民族问题和国际主义（从格鲁吉亚党内最近冲突谈起）”备忘）、**L160：克鲁普斯卡娅 `1924-05-18` 移交文件，记录“关于民族问题的札记未计算在内（目前在玛丽亚·伊里尼奇娜处）”**——这正是 Spitsyn/Sakharov 质疑所涉的**保管链断口**，应当在卡片明文提出，而非泛称“须核对秘书记录及传抄链”。
  - [`loginov_lenin_bio_zh/ch08…`](../sources/monographs/loginov_lenin_bio_zh/ch08_第三部_以此胜之.md) L1252（`12-23` 口授登记于《发出邮件登记簿》第 8628 号）、L1278（Kostin/Sakharov“后补伪造”论）与 L1292（Loginov 反驳：“自我审查模式”与事后补记≠伪造）——站内已存在**对 Spitsyn 类质疑的直接学术反驳**。
  - [`timeline/L3_daily/1922-12_lenins_last_struggle_diary.md`](../timeline/L3_daily/1922-12_lenins_last_struggle_diary.md) L71–76 对 `12-30/12-31` 口授、卡巴尼泽事件、“杰尔日莫尔达”引语已有完整条目；卡片 T3 **未链接该 L3**（P1 漏引）。
  - 另注：该 S 级文件**不含《关于民族或“自治化”问题》正文**，应在卡片 `perspectives_missing` 补 `primary-text-nationality-dictation-1922-12-30`（站内原典缺口）。
  - **修复**：2.1 末条与 2.3 Spitsyn 条各补 1 句并挂以上三处；T3 加 L3 `1922-12` 与 Loginov 引用。
- **P1-06-3｜`start_ns: 1921-02-01` 无站内锚点**：Carr RN L45 明确“**1921-02-21 越境、1921-02-25 攻占第比利斯**；2 月 21 日是 Carr 叙事的越境节点，不能据此确证整场战事起日”，并记 `1921-03-03` 列宁主张让步、`1921-05-21` 俄格条约。**修复**：`start_ns` 改为 `1921-02-21`（并注明“Carr 越境节点”），或保留 `1921-02` 并在 T3 声明占位。
- **P1-06-4｜漏记“外高加索联邦”两个制度动作日期**：Carr RN L47：`1922-03-12` 三共和国区域联盟条约；`1922-12-13` 外高加索代表大会通过单一联邦共和国宪法。卡片只说“格鲁吉亚经外高加索联邦入盟”，缺这两个定年；这正是格鲁吉亚领导人反对的“联邦化”所指。**修复**：在 2.1 第 1 条或边表第 3 行补两日期，避免与 `1922-12-30` 混淆（与 L3 `…L75` 对读）。
- **P1-06-5｜2.2 边表为自然语言（`格鲁吉亚共产党反对派 ↔ 高加索局`、`列宁 ↔ 斯大林`…）**：站内可用 ID：`PER-lenin`、`PER-stalin`、`PER-ordzhonikidze`、`PER-dzerzhinsky`、`PER-kamenev`；`姆季瓦尼/马哈拉泽/外高加索联邦`站内无卡，应标缺口。
- **P2-06-6**：卡片 T1/T2 未写 `1923-01-25 政治局为奥尔忠尼启则开脱 / 02-01 列宁取得卷宗 / 03-05–06 绝交与托付托洛茨基 / 03-14 党内协议`（E08 L38、Lewin CLM L25、Carr RN L63）；`end_ns` 取 `1922-12-31` 合理，但 T3 应说明“后续至 1923-03 的余波见 DEB-1922”。
- **P2-06-7**：`CLM-carr-1950-ukraine-and-georgia-military-treaty-reintegration` 已存在（Carr 军事接管与条约），卡片只挂 Smith/Lewin CLM；建议补入，使 `archival-revisionist`、`statist` 之外的“条约制度”视角有 CLM 锚点。

---

## 07｜[`EVT-1928-shakhty-affair-show-trial.md`](../cards/events/EVT-1928-shakhty-affair-show-trial.md)

**总判**：史实主干与历法 ✅；**漏挂专属 DEB 与 Kuromiya 学者卡（P1）**；站内 L3 已能**闭合**卡片多处“待复核”（被告数、终审时间、四月全会表决）（P1）；边表无 ID（P1/P2）。无 P0。

### 与站内锚点对勘
| 卡片断言 | 站内锚点 | 结论 |
| :--- | :--- | :--- |
| `1928-03-10` 《真理报》公开案件；叶夫多基莫夫绕过管理渠道 | Kotkin RN L140；L3 `1928-01…` L95–98 | ✅ |
| 53 名工程师（含 5 名德国专家）/ 55 名被控 | Kotkin RN L140；Cohen RN L37（`pp. 280–282`，55 名）；**L3 L98：“53 名本国及 3 名德国技术专家受审”，Cohen p.281 记公布时 55 人** | ⚠ 三口径并存，见 P1-07-1 |
| `1928-05-18` 开庭（工会大厦圆柱大厅）、维辛斯基/克雷连科 | L3 L98 | ✅ |
| 终审“常写 07-06，Kotkin 札记至 07-07，应复核” | **L3 L98：`07-06` 深夜至 `07-07` 凌晨 1:30 宣读判决**；Carr–Davies/Lewin 记审期 `05-18–07-05` | ⚠ 可闭合，见 P1-07-2 |
| 11 人死刑、5 人处决、`1928-07-09` | L3 L98、L113；Kotkin RN L144、L203 | ✅ |

### 发现
- **P1-07-1｜被告人数“两组数字…不能自行合并”——站内 L3 已并列并提供口径层次**
  - Kotkin RN：53 名矿业工程师“含 5 名德国专家”（引起德国 `03-15` 暂停 6 亿马克信贷谈判）；L3 L98：**53 名本国 + 3 名德国**受审、判决 4 人无罪（含两名德国技师）、4 人缓刑、其余 1–10 年、**11 死刑 → 6 人减刑 → 5 人执行**；检方要求 **22 人死刑**；审理 49 天；Cohen p.281：公布时 55 人。卡片只写前两个数字并宣告“须查起诉书”。
  - **修复**：T2 L27 / T3 L49 改为“Kotkin：53（含 5 德）；L3：53+3 德受审；Cohen：公布时 55；差异可能源自‘被捕/起诉/出庭’阶段与德国籍人数口径，原始起诉书站内未入库”，并增“检方要求 22 死刑 → 判 11 死刑 → 6 减刑 → 5 执行”的分母链。
- **P1-07-2｜终审日期口径可定为“`1928-07-06` 夜—`07-07` 01:30 宣判”**（L3 L98，对 Carr–Davies/Lewin 的 `07-05` 审期终点另注）；卡片 L29 “应依判决书复核”可保留“原始判决书未入库”，但不应把已有站内定年写成未知。同时 `end_ns: 1928-07-09` 为处决日，非审判终结日，T3 应声明含义。
- **P1-07-3｜漏挂专属 DEB 与 Kuromiya 学者卡，“Kuromiya 本次未核实”表述失准**
  - [`DEB-1928-shakhty-specialist-baiting-and-cultural-revolution`](../historiography/debates/DEB-1928-shakhty-specialist-baiting-and-cultural-revolution.md)：`core_cards` 已含本卡，且矩阵列有“高层政治（Khlevniuk/Kotkin/Cohen）/ 社会流动（Fitzpatrick）/ 工业现场与敌人建构（Kuromiya、Goldman、Bailes）”三取向与 `CLM-cohen-1973-july-1928-plenum-and-kamenev`、`CLM-priestland-2007-1928-mobilization-turn-against-bukharin`、`CLM-goldman-2011-great-turn-industrialization-and-wrecking` 锚点；本卡 `related_debates` 却只有 `DEB-1928-bukharin-alternative`——**反向链存在、正向链缺失**。
  - [`SCH-kuromiya-hiroaki`](../historiography/scholars/SCH-kuromiya-hiroaki.md)（`coverage_status: grounded`）已记其 1988 年《斯大林的工业革命》“spets-baiting”论与顿巴斯研究；站内 Siegelbaum–Suny `ch10_5_donbas_miners_…` 为其顿巴斯章节。卡片 L42 “本次未核实黑宫…不为其指定超出此范围的细节”的**克制本身合理**，但应改为“已读 SCH 卡与 `…ch10_5`，其沙赫特具体文本未读”，并挂链接。
  - **修复**：`related_debates` 增 `DEB-1928-shakhty-specialist-baiting-and-cultural-revolution`；2.3 第二、三条分别挂 `SCH-kuromiya-hiroaki` 与 DEB 矩阵。
- **P1-07-4｜四月全会内容遗漏与误导风险（L3 L95）**
  - L3：`1928-04-06~04-11` 联席全会，米高扬作粮食报告、**李可夫作沙赫特案报告**；`04-10` 斯大林将案件直接挂钩白俄流亡与外国干涉，全会逐字采纳其定性；斯大林提议将高等技术院校（VTUZ）从教育人民委员部划归 VSNKh，**遭近 2:1 多数否决**（夏季全会才部分突破）。卡片 L28 称“4 月全会讨论案件及培养工人、党员出身的技术干部”，未写**“斯大林教育归属提案遭否决”**，易让读者以为 4 月已在教育管辖上定论；T3 L48 的“4 月一般决议 vs 7 月具体配额”区分需补此事实。
  - **修复**：L28 补“4 月：阴谋定性被采纳，但 VTUZ 划转提案遭否决；7 月（`07-04~12`）才部分实现”。
- **P1-07-5｜Goldman 的用法需限定**：站内 `CLM-goldman-2011-great-turn-industrialization-and-wrecking` L38 与 `RN-W32-goldman-oppositions-vigilance-and…` L37 明确：Goldman 对沙赫特审判**仅在 `p. 44 n.33` 脚注**提及（被判流放三年的工程师佩舍霍诺夫 1936 年于凯梅罗沃再被按“破坏”罪处决）。卡片不引用 Goldman（未误用 ✅），但若修复时加入 Goldman，必须仅作“后续‘破坏’话语日常化的长时段比较”，**不得**当作沙赫特案证据（DEB-1928 T2 也提醒“后来大恐怖证据年代不可投射到 1928”）。
- **P1-07-6｜2.2 边表为自然语言**：站内可用 ID：`PER-stalin`、`PER-rykov`、`PER-kuibyshev`、`PER-bukharin`、`PER-tomsky`、`ORG-cheka-ogpu` 与 `INS-cheka-gpu-ogpu`（**两卡并存，需先统一**）、`POL-first-five-year-plan`、`EVT-1928-grain-procurement-crisis`、`INS-vsnkh-and-gosplan`、`ORG-right-opposition-1928`；`叶夫多基莫夫/维辛斯基/克雷连科`站内无人物卡，应标缺口。
- **P2-07-7**：站内 `DATA-06`（L58）给出 1928 年 OGPU 判决总数 `148,975`（含 `36,239`，24.3%）及社革党/孟什维克/联共党员分项，可作为“1928 年镇压背景量级”脚注，但**不得与沙赫特被告数混同**；非必需。
- **P2-07-8**：T1“11 人被判死刑，5 人被处决”✅，建议补“6 人获减刑”（L3 L98）。

---

# 汇总修复矩阵

| 编号 | 卡片 | 级别 | 位置 | 问题（一句话） | 可执行修复 |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **P0-05-1** | 05 饥荒/教会 | **P0** | T3 L50；2.3 L41 | 挂 `RN-W5`(Figes)/`RN-W4B`(Pipes) 两份**零命中无关札记**，并据此归属“派普斯强调打教会计划” | 删链接；改据 Loginov ch08 L850–890 与 `stalin_major_documents_zh ch03` L280–292；Pipes 论点降为“外部待核线索” |
| **P0-06-外** | 06（卡外） | **P0** | `DEB-1923-nationality-and-empire.core_cards` | 引用不存在的 `EVT-1922-georgian-affair`、`EVT-1922-ussr-formation`（实为 `EVT-1922-georgian-affair-and-ussr-formation`） | 改 DEB 的 `core_cards`；同时 06 号 `related_debates` 反向挂 DEB |
| P1-01-1 | 01 斯托雷平 | P1 | L27、T3 L44–45 | 27–33% / 15% 实在 Figes **ch13** L171，却挂 ch16 + OECD；15% 含“成组或个体”非 khutor | 改引 `figes…/ch13_6_last_hopes.md` L171 与 `ch16` L78；补“1909–10 后回落” |
| P1-01-2 | 01 | P1 | `related_debates` | 挂 `DEB-1914`（劳工稳定论，`core_cards: []`），漏挂 **`DEB-1906-stolypin-wager-and-agrarian-viability`** | 替换/并列；2.3 引入 DEB-1906 三栏（含 Marxist 道路论：Lenin “普鲁士/美国道路”，Carr 卷二 ch03 L376–430） |
| P1-01-3 | 01 | P1 | T2/T3 | 漏 L2 E04 L18（1906-08 两项土地措施 vs 11-09）、Manning ch18、`CLM-hildermeier…paralysis` | 补一句 8 月措施分野；贵族政治维度挂 Manning |
| P1-02-1 | 02 法令 | P1 | T2 L25、T3 L46 | “钟点待核”过度；L3 L235–249 与原典 L19（闭幕 05:15）可定为 `27 日 01:00 后`通过 | 改写为“和平法令 `10-26` 21 时后；土地法令 `10-27 [O.S.]/11-09 [N.S.]` 凌晨”，并挂 L3 |
| P1-02-2 | 02 | P1 | 2.3 | 三条光谱均匿名 | 挂 Sukhanov ch30、Figes ch16、Rabinowitch/Lewin（待核章）；`perspectives_missing` 补 `soviet-orthodox` |
| P1-03-1 | 03 切尔文 | P1 | YAML、T3 L45 | `1922-10-11` 日期站内无锚；用 encyclopedia.com 承载 1926-06-09/1930 | 站内仅“1922-10”，注明外部口径；删或降级百科日期 |
| P1-03-2 | 03 | P1 | `perspectives_present` | `archival-post-soviet` 与来源（Carr + Katasonov-B）不符 | 改为 `western-documentary-carr` + `statist-nationalist-katasonov`；missing 补苏联/后苏联档案货币研究 |
| P1-03-3 | 03 | P1 | 2.1 | 漏 DATA-02 “3%→37%” 价值占比、面额重估链、1923-08/09 信贷收缩与再发行；漏 L3 `1923-10` | 补三量纲与重估链；挂 `1923-10_scissors…` |
| P1-03-4 | 03 | P1 | 2.3 | “工业投资视角”匿名；漏 CLM-katasonov / CLM-other-nep-1923 / RN-W10 / Preobrazhensky | 具名化并挂锚点 |
| P1-04-1 | 04 流血星期日 | P1 | T3 L46–47 | “约 130 死官方数未核”——Pipes ch09 L705 n.239 已给 **130 死/299 伤（Pankratova）**；L3/DATA-01 把 Figes“probably”写成“档案核实” | 四口径并列（96/333；130/299；≈200/≈800 估计；4,600 死伤合计）；DATA-01 L30 补 130/299 |
| P1-04-2 | 04 | P1 | 2.2 | 边表无 ID，库内已有 `PER-gapon / PER-nicholas-ii / EVT-1905-revolution` | 改为 ID |
| P1-04-3 | 04 | P1 | 2.1 L27 | 14 万为 `01-07 [O.S.]` Trotsky 时点，被挂在 `01-03` 句尾 | 按 DATA-01 L26–31 分时点 |
| P1-04-4 | 04 | P1 | T3 | Figes ch12 L195、Pipes ch09 L291/L705 未直链；`liberal-institutional` 无来源 | 补直链；该标签移至 missing |
| P1-05-2 | 05 | P1 | 3.1 | “未核 Figes 数字”——Figes ch23 L27–48 已有 500 万、萨马拉 70 万、Pomgol 7/21、ARA 1,000 万人/6,100 万美元 | 改写 3.1，并加 RN-W6 的 1,600 万分母对照 |
| P1-05-3 | 05 | P1 | 2.1 L29、边表 | 漏 `03-15` 舒亚、`03-16` 暂缓、`03-20` 修改指示、处决数（Loginov L850–890）；漏斯大林多数停止没收 | 补日期/数字；并置 Loginov 与“消灭教会论”两种解读 |
| P1-05-4 | 05 | P1 | 2.2 | 边表无 ID | 映射 `POL-war-communism / PER-gorky / PER-lenin / PER-trotsky / PER-stalin`；缺口标注 |
| P1-06-1 | 06 格鲁吉亚 | P1 | `related_debates: []` | 漏 `DEB-1922-lenin-testament-and-stalin-rise`、`DEB-1923-nationality-and-empire` | 补挂 |
| P1-06-2 | 06 | P1 | 2.3 L44、T3 | 口述真伪“待核”——站内 S 级编注 L160（保管链断口）、Loginov L1252/L1278–1292、L3 `1922-12` L71–76 已可部分闭合 | 补三处；`perspectives_missing` 补原典缺口 |
| P1-06-3 | 06 | P1 | YAML | `start_ns 1921-02-01` 无锚；站内有 `1921-02-21/02-25`（Carr RN L45） | 改 `1921-02-21` 并注口径 |
| P1-06-4 | 06 | P1 | 2.1 | 漏 `1922-03-12` 区域联盟条约、`1922-12-13` 外高加索宪法（Carr RN L47） | 补两日期 |
| P1-06-5 | 06 | P1 | 2.2 | 边表无 ID | `PER-lenin/stalin/ordzhonikidze/dzerzhinsky/kamenev` |
| P1-07-1 | 07 沙赫特 | P1 | L27、T3 L49 | 被告“53/55”未并入 L3 的 53+3 德与 22→11→6→5 分母链 | 改写并挂 L3 L98 |
| P1-07-2 | 07 | P1 | L29 | 终审时间站内已定 `07-06` 夜—`07-07` 01:30 | 改写；`end_ns` 注明为处决日 |
| P1-07-3 | 07 | P1 | `related_debates`、L42 | 漏挂 `DEB-1928-shakhty-…`；Kuromiya 有 SCH 卡与 Donbas 章 | 补挂并改措辞 |
| P1-07-4 | 07 | P1 | L28 | 漏四月全会“VTUZ 划转提案遭否决（近 2:1）”及李可夫作案件报告 | 补事实，修订 T3 L48 区分 |
| P1-07-6 | 07 | P1 | 2.2 | 边表无 ID；`ORG-cheka-ogpu` 与 `INS-cheka-gpu-ogpu` 并存 | 先统一节点，再替换 |
| P2-01-3/4 | 01 | P2 | T2/T1 | Haimson 悬空（并入 P1-01-2）；T1 末句无证据 | 见 P1-01-2；挂 Figes ch12 L224 |
| P2-02-3/4/5 | 02 | P2 | YAML/边表 | `start_ns` 与 L3 “新日”原则张力；`related_debates` 空；`PER-lenin` 依据空泛 | 注明 `11-08` 为开幕/和平法令日，土地法令 `11-09`；核 DEB；改文件锚 |
| P2-03-5/6 | 03 | P2 | 边表、T3 | `AUD-14` 当依据；`end_ns 1924-03-31` 月末锚 | 换为 DATA-02/RN；改“1924 年 2–3 月” |
| P2-04-5/6 | 04 | P2 | L27 | “普选”应取俄文“普遍、平等、秘密”；四名工人系 1904-12 下旬解雇 | 小改 |
| P2-05-6/7/8 | 05 | P2 | YAML/DEB/因果 | 年界占位；`related_debates` 空；Pomgol 解散因果 | 见各条 |
| P2-06-6/7 | 06 | P2 | T3 | 1923 余波、CLM-carr 未挂 | 补 |
| P2-07-7/8 | 07 | P2 | 脚注 | DATA-06 背景量级；“6 人减刑” | 可选 |

## 总评与优先级

1. **先修 P0（2 项）**：05 号 T3 去除两份无关札记并重写“派普斯论点”；`DEB-1923-nationality-and-empire` 的 `core_cards` 断链。
2. **次修“绕开站内材料而标待核”（P1，最高性价比）**：04 号 Pipes 130/299；01 号 Figes ch13；05 号 Figes ch23 与 Loginov；06 号 L3 `1922-12`/Letter-to-Congress L160/Loginov L1252–1292；07 号 L3 `1928-01` L95–98。这些均为**纯加链接/改措辞**即可，不需新增史料。
3. **三修图谱规范**：04/05/06/07 四张事件卡边表统一改用库内 ID，缺口显式标“节点缺口”；`related_debates` 补挂（01→DEB-1906；06→DEB-1922/1923；07→DEB-1928-shakhty）。
4. **数据卡回写建议（卡外，另立任务）**：`DATA-01` L30 补 `130/299`；`DATA-02` 无需改；`ORG-cheka-ogpu` / `INS-cheka-gpu-ogpu` 合并或互链。
5. **站内原典缺口**（本次核实）：列宁 `1922-03-19` 致政治局信、《关于民族或“自治化”问题》（`1922-12-30/31`）、`1922-10-11` 币制授权法令、`1906-11-09` 斯托雷平敕令，均**无独立原典文件**；其中 Lenin 两件文本因卡片明确使用，建议列入下一轮 `web-archive` 补库清单（目前 05/06 号只能以 Loginov、Lewin、Smith 等二手引文为准）。

## 审计声明
- 本审计**未修改任何卡片、札记、数据卡或总表**，仅写入本文件。
- 所有“站内锚点”均经实际文本检索确认；凡属外部通行口径（如 `1922-10-11` 日期）已明示为外部口径且未当作证据。
- 未逐行精读的材料已标“待核”（Rabinowitch/Lewin 具体章节、Bonnell/Zelnik 章节、L3 `1923-10` 全卷），不作断言。
