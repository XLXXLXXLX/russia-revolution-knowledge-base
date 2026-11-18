# 史学史对勘与反偏见审计报告（AUD-09）：第 21–23 波 L3 微距编年、实体卡、定量微序列与概念/争鸣卡跨家族异源审计

- **审计角色**：`dialectic-auditor`（史学史对勘与反偏见审计官，纯只读异源对勘）
- **被审对象**（共 21 份文件，由 Cursor Composer 撰写）：
  1. **4 卷 L3 微距编年**：[`1903-07_rsdlp_second_congress_split.md`](../timeline/L3_daily/1903-07_rsdlp_second_congress_split.md)、[`1918-01_constituent_assembly_and_brest_crisis.md`](../timeline/L3_daily/1918-01_constituent_assembly_and_brest_crisis.md)、[`1918-07_left_sr_uprising_and_red_terror_launch.md`](../timeline/L3_daily/1918-07_left_sr_uprising_and_red_terror_launch.md)、[`1919-10_civil_war_southern_and_petrograd_climax.md`](../timeline/L3_daily/1919-10_civil_war_southern_and_petrograd_climax.md)
  2. **10 张实体卡**：[`PER-tomsky.md`](../cards/persons/PER-tomsky.md)、[`PER-kalinin.md`](../cards/persons/PER-kalinin.md)、[`PER-kuibyshev.md`](../cards/persons/PER-kuibyshev.md)、[`PER-kaganovich.md`](../cards/persons/PER-kaganovich.md)、[`PER-frunze.md`](../cards/persons/PER-frunze.md)、[`PER-krupskaya.md`](../cards/persons/PER-krupskaya.md)、[`EVT-1918-1920-russian-civil-war.md`](../cards/events/EVT-1918-1920-russian-civil-war.md)、[`EVT-1920-1921-tambov-and-peasant-revolts.md`](../cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md)、[`MTG-1919-03-8th-party-congress.md`](../cards/meetings/MTG-1919-03-8th-party-congress.md)、[`MTG-1924-05-13th-party-congress.md`](../cards/meetings/MTG-1924-05-13th-party-congress.md)
  3. **2 份定量微序列**：[`DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md`](../data/DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md)、[`DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md`](../data/DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md)
  4. **1 份概念谱系总表与 4 张争鸣卡**：[`CONCEPT_GENEALOGY_INDEX.md`](../glossary/CONCEPT_GENEALOGY_INDEX.md)、[`DEB-1917-dual-power-and-february-origins.md`](../historiography/debates/DEB-1917-dual-power-and-february-origins.md)、[`DEB-1918-red-terror-and-civil-war-origins.md`](../historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md)、[`DEB-1918-war-communism-ideology-vs-emergency.md`](../historiography/debates/DEB-1918-war-communism-ideology-vs-emergency.md)、[`DEB-1929-collectivization-and-dekulakization-causes.md`](../historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md)
- **对勘基准**：`python scripts/kb.py date` 儒略/公历与 JDN 星期计算器、`python scripts/kb.py audit-graph`、库内原始 `reading-notes/RN-W*`（重点 `RN-W20*`、`RN-W2`、`RN-W4B`、`RN-W16`）及 `historiography/claims/CLM-*`。
- **审计总结论**：**有条件通过（需按下方清单执行 8 项 P0 级硬伤修复与 12 项 P1 级规范校准）**。图谱结构校验（`audit-graph` 381 卡/95 边/543 账本事件）整体闭环，`DATA-05` 与 `DATA-06` 的核心统计序列与 `RN-W20*` 达到高吻合度；但异源交叉检验暴露出 **1918.02.14 改历后伪造双历/误标 `[O.S.]`**、**L3 星期按旧历日数字直接套算公历星期**、**1918-02-18 与 02-23 布列斯特两次中央表决票数与托洛茨基投票行为揉合错位**、**多处人物职务与入局年份张冠李戴**、以及 **个别幻觉错字（如“临汾组织系统”“分裂症派”“贝纳巴夫”）与断链**。

---

## 一、 专项核查 A：历法转换与星期纪律（`kb.py date` 逐项验算）

### 1.1 19 世纪人物生辰（+12 天规则）核查
| 卡片 ID | YAML `start_ns` | 正文旧历 `[O.S.]` | 正文新历 `[N.S.]` | 差值 | 核查结论 |
|---|---|---|---|---|---|
| `PER-tomsky` | `1880-10-31` | `1880-10-19` | `1880-10-31` | +12 天 | **PASS**（零差错） |
| `PER-kalinin` | `1875-11-19` | `1875-11-07` | `1875-11-19` | +12 天 | **PASS**（生辰零差错，但 1919 年存在伪双历，见 1.2） |
| `PER-kuibyshev` | `1888-06-06` | `1888-05-25` | `1888-06-06` | +12 天 | **PASS**（零差错） |
| `PER-kaganovich` | `1893-11-22` | `1893-11-10` | `1893-11-22` | +12 天 | **PASS**（零差错） |
| `PER-krupskaya` | `1869-02-26` | `1869-02-14` | `1869-02-26` | +12 天 | **PASS**（零差错） |
| `PER-frunze` | `1885-02-02` | **未标注**（应为 `1885-01-21`） | `1885-02-02` | +12 天 | **WARN（P1）**：`start_ns` 换算正确，但 T2 §2.1 L25 仅写 `生于 1885-02-02`，漏标 `1885-01-21 [O.S.] / 1885-02-02 [N.S.]` 双历。 |

### 1.2 1900–1918.02.13（+13 天规则）与 1918.02.14 后纯公历纪律核查（发现 5 处 P0 硬伤）

1. **【P0 伪造改历后双历】`cards/persons/PER-kalinin.md`（L26）**
   - **原文**：`` `1919-03-30 [O.S.] / 1919-04-12 [N.S.]` 起任全俄中央执行委员会（ВЦИК）主席``。
   - **审计裁定**：苏俄自 `1918-02-14` 起已全面实行格里历（新历）。斯维尔德洛夫于 `1919-03-16`（新历）病逝，俄共（布）八大于 `1919-03-18` 至 `03-23`（新历）召开，加里宁于 **`1919-03-30`（新历）** 接任全俄中执委主席。撰写者将公历 `1919-03-30` 误当成旧历并强行 +13 天捏造出不存在的 `1919-04-12 [N.S.]`。必须删去 `[O.S.] / 1919-04-12 [N.S.]`，直接写 `1919-03-30`。

2. **【P0 改历后日期误标 `[O.S.]`】`historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md`（L18）**
   - **原文**：`1918年9月5日[O.S.]人民委员会颁布《关于红色恐怖》决议`。
   - **审计裁定**：1918 年 9 月 5 日已是改历后半年多的纯公历（`[N.S.]`）日期（同卷 L3 `1918-07_left_sr_uprising_and_red_terror_launch.md` 亦按公历编排）。此处标注 `[O.S.]` 严重违反 1918-02-14 后纯公历规则，应删去 `[O.S.]`。

3. **【P0 星期套算错误（误用公历同月同日数算星期）】`timeline/L3_daily/1918-01_constituent_assembly_and_brest_crisis.md`（L19、L29）**
   - **原文 L19**：`### 1918-01-05 [O.S.] / 1918-01-18 [N.S.]（星期六）`
   - **原文 L29**：`### 1918-01-06 [O.S.] / 1918-01-19 [N.S.]（星期日）`
   - **审计裁定**：经 `python scripts/kb.py date 1918-01-05 os` 与 `1918-01-06 os` 验算：
     - `1918-01-05 [O.S.] / 1918-01-18 [N.S.]`（JDN `2421612`）实为 **星期五（Friday）**；
     - `1918-01-06 [O.S.] / 1918-01-19 [N.S.]`（JDN `2421613`）实为 **星期六（Saturday）**。
     - 致错原因：撰写者直接拿旧历数字 `1918-01-05`、`1918-01-06` 当作格里历日期去查星期（格里历 1918 年 1 月 5 日、6 日恰为周六、周日），造成立宪会议召开与解散两天的星期整体顺延一天！

4. **【P0 星期算错】`timeline/L3_daily/1918-07_left_sr_uprising_and_red_terror_launch.md`（L81）**
   - **原文 L75 vs L81**：L75 为 `### 1918-09-04（星期三）`，紧接着 L81 写 `### 1918-09-05（星期五）`。
   - **审计裁定**：经 `python scripts/kb.py date 1918-09-05 ns` 验算（JDN `2421842`），`1918-09-05` 为 **星期四（Thursday）**，不可能从 9 月 4 日星期三直接跳到 9 月 5 日星期五。

5. **【P1 编年体时序倒置】`timeline/L3_daily/1918-01_constituent_assembly_and_brest_crisis.md`（L43–L83）**
   - **审计发现**：T2 日历条目出现两处明显的时序倒装：
     - 第一处：L43 `1918-01-10 [O.S.] / 01-23 [N.S.]` 至 `01-18 [O.S.] / 01-31 [N.S.]`（苏维埃三大）排在了 L49 `1918-01-08 [O.S.] / 01-21 [N.S.]` 与 L55 `1918-01-11 [O.S.] / 01-24 [N.S.]` 之前；
     - 第二处：L71 `1918-02-14（星期四）`（改历锚点）排在了 L77 `1918-01-28 [O.S.] / 1918-02-10 [N.S.]（星期日）`（托洛茨基“不战不和”声明）之前。应按 JDN 严格升序重排。

---

## 二、 专项核查 B：`DATA-05` 与 `DATA-06` 对照 `RN-W20*` 逐字核查

### 2.1 `DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md` 对勘结果
对照 [`RN-W20-red-petrograd-factory-committees-1917-1918.md`](../reading-notes/RN-W20-red-petrograd-factory-committees-1917-1918.md) 与 [`RN-W20-civil-war-geopolitics-and-military-specialists.md`](../reading-notes/RN-W20-civil-war-geopolitics-and-military-specialists.md)：
- **逐字一致项（38 组核心数据全部零误差）**：
  - 彼得格勒工厂人口：战前 `242,600`、1917-01-01 `392,828`（帝国 `340 万` 之约 `12%`；加上首都郊区 `1,011` 家工厂达 `417,000`）；金属业 `237,369`（`60.4%`）、化学品 `44,115`（`11.2%`），合计 `67.9%`（1914 年为 `50.2%`）；平均厂模 `409` 人；维堡区 `68,932` 人，加瓦西里岛、彼得格勒侧共 `134,464`（`34%`）；国有厂 31 家约 `1/3` 劳力，13 家军火厂 `97,109` 人，普梯洛夫厂 `3 万`。
  - 工人结构：新进劳力约 `190,000`；女工 1914 年 `25.3%`（约 `61,000`）升至 1917 初 `33.3%`（`129,800`）；新增成年工中女性占 `68.6%`；核心无产者 `40%`、新进农民/妇女 `60%`；年龄段 1897 vs 1918（`≤15`: `6.4%→3.2%`, `16-20`: `22.7%→21.1%`, `21-40`: `56.6%→53.6%`, `>40`: `14.3%→22.1%`）；识字率男 `80%→89%`、女 `53%→65%`、金属工 `88–92%`；普梯洛夫车间工资膨胀（炮架 `22.7`、枪炮 `23.1`、新炮弹 `21.1`、平炉 `29.0` vs 铸铁 `6.0`、机车 `72.0`）。
  - 复员与萎缩：军需占产值 `80–85%`；燃料占产出比 `63%→106%`；第一工区停工原由（燃料 `20`、原料 `11`、两缺 `27`、缺订单 `2`、改修 `1`）；1918.04 关闭 `568` 家；在岗人数 1918-01-01 至 04-01：`339,641 → 148,703`（`43.8%`），其中金属 `197,686 → 57,995`（`29.3%`）、化学 `41,852 → 8,159`（`19.5%`）、食品 `22,571 → 19,218`（`85.1%`）；春末存留约 `120,000` 人（1917.01 的 `30–40%`），失业率 `60%`。
  - 内战军力与腹地：苏维埃腹地 `>250 万 km²`、人口 `6,000 万` vs 各白军区 `800 万–900 万`（人口比 `>6:1`）、红军峰值 `300 万` vs 单一白军 `20 万`（兵力比 `>15:1`）。
  - 沙皇遗产拨付（表 B.2）：步枪 `1,100 万 / 132.1 万 / 60 万 / 46 万 / 35%`、机枪 `7.6 万 / 11,072 / 8,000 / 6,256 / 57%`、火炮 `1.7 万 / 8,208 / 1,700 / 152 / 2%`、枪弹 `14.82 亿 / 3.4006 亿 / 23%`、炮弹 `3,300 万 / 184,998 / <1%`。
  - 军官分流（表 B.3）：总军官 `250,000`（职业 `15,000`、战时 `220,000+`）；自愿入红军 `8,000`、被征召 `>48,000`（指挥岗 `22,000`）、含军医文职 `215,000`；高尔察克职业 `2,000` / 战时 `11,000`（总 `13,000`），邓尼金总 `25,000`；参谋学院 `2,000` 人入红军 `500–600`。
  - 红军扩张、逃兵与战役兵力：总规模 `70 万 → 150 万 → >300 万`；东线 `100,000`、南线 `100,000–150,000`；编制比 `356,000 / 53.8 万 / 89.9 万`；逃兵 `170 万`；政治部人员 `20,290 / 8,910 / 4,231`；党员 `563,000 / 258,000 / 43,000 (16.6%)`；契卡特别处+内卫军 `60,000`；东线推进 `1,100 km`（1919.04 乌拉尔白军 `104,000` vs 红军 `100,000`；7 月末高尔察克剩 `50,000`；大西伯利亚冰上行军 `30,000`）；南线 `100–104` 万配给、`39–43` 万战斗兵、白军 `25 万`；十月决战红军 `97,000–99,000` vs 志愿军 `20,500`（近 `5:1`）。
- **发现 1 处口径转述歧义（P1）**：
  - **`DATA-05` §A.5（L78）**：写 `委员会中实施控制者: 244 家委员会，占 39%`。
  - **对勘 `RN-W20-red-petrograd` §3.3（L77）与 `CLM-smith-sa-1983-defensive-workers-control.md`（L26）**：原文为 `仅 39%（244 家工委会）积极实施控制` / `仅 39%/244 家委员会实施`（源出 Itkin 对 244 家工厂委员会的统计：244 家工委会中有 96 家——即 $96 / 244 = 39.3\%$——积极实施工人控制，或全城约 620 家工委会中 244 家占 39%）。`DATA-05` L77 与 L78 分拆成“积极实施某种工人控制的企业 96 家 / 1,011 家”与“委员会中实施控制者 244 家委员会，占 39%”，建议注明 `（244 家工委会，占工委会总数 39%，其中大中型企业 96 家）` 以免读者误以为 96 与 244 矛盾。

### 2.2 `DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md` 对勘结果
对照 [`RN-W20-psr-civil-war-tragedy-and-cheka-ogpu-extrajudicial-powers.md`](../reading-notes/RN-W20-psr-civil-war-tragedy-and-cheka-ogpu-extrajudicial-powers.md) 与 [`RN-W20-nov-dec-1929-politburo-commission-and-ogpu-archives.md`](../reading-notes/RN-W20-nov-dec-1929-politburo-commission-and-ogpu-archives.md)：
- **逐字一致项（所有已录入数字与源札记 100% 吻合）**：
  - 1918–1920 处决数据：`6,300`（平叛 `1,637`）、20 省 `2,089`（彼得格勒 `387`，另 `RN-W16` 莫斯科 `119`）、Latsis `9,701`、Melgunov 等估算 `17,500`、Ryan 综合上限 `<50,000`。
  - 司法与法外双轨：1918 下半年革命法庭审结 `14,204` 案、仅 `6` 起枪决（其余多在 `4,097` 起契卡案件中执行）；1919 年法庭判处枪决约 `60` 起（`2,328` 审结案）、1920 年 `650` 起（`9,362` 案，占 `6.9%`）；普通人民法院 1919 年死刑 `615` 起（`65,109` 案，占 `0.5%`）。
  - 1922 年 PSR 大审判：`334` 人在押（中央委员与积极分子 `89`、全俄中执委派 `77`、前党员 `35`）、1922.02.28 拟起诉 `47` 人、最终受审 `34` 人、1922.08.07 判处 `12` 名第一组被告死刑缓期作人质。
  - 1923–1925 OGPU 法外流放与处决：1924.01 在押政治犯 `246` 人；1924 年经内务人民委员部委员会法外流放 `308` 人、1925 年 `319` 人；表 A.3（1921–1930 案件审理总人数 `71,435 → 399,445`、农民人数及占比 `22.4% → 55.7%`、极刑与集中营人数）；1929 年反革命罪定罪细分 `137 (4,462) + 3,464 (20,922) + 23,684 = 49,068`（括号内 `25,384`）。
  - 1929 集体化狂飙（表 B.1–B.4）：五年计划目标 vs 实际入社农庄数与农户比例（`100 万 / 3.9% → 190 万 / 7.5% → 310 万 → 500 万`）；机器拖拉机站 `800 / 1,300 / 1,500 / 2,400 (+60%) / 3,000`；跨村巨型农庄平均规模 `147` 户 vs 普通 `39` 户；二万五千人下乡 `>70,000` 报名、派出 `27,519`（乌克兰等三区计划 `16,100` 实派 `17,869`）；霍皮奥尔专区虚报 `26%→61%`、萨马拉 `59.7%→27%`、全俄集体农庄中心在册 `13,616,151` 户 vs 实际在社 `6,345,277`（`2.15` 倍）与 5 月 `5,203,799`（`2.62` 倍）；北高加索等四区原统计 `4,636,850` 户 vs 5 月留存 `920,764` 户；全面集体化区核减（乌拉尔 `96→51 / 53.1%`、中央黑土 `97→8 / 8.2%`、莫斯科 `147→4`、列宁格勒 `117→4 / 3.4%`）；下诺夫哥罗德 `16` 个村苏维埃 `26%→82.4%`、逮捕 `144` 人。
- **发现 2 处遗漏/简写问题（P1）**：
  1. **表 A.3 漏收农民阶层与党派细分行**：`RN-W20-nov-dec-1929` §3.3（L169–176）原始档案表中极关键的 **富农（1925: `1,116`, 1926: `2,137`, 1927: `8,280`, 1930: `148,297`）**、**中农（`6,750 / 10,069 / 14,934 / 56,770`）**、**贫农（`8,167 / 10,919 / 13,025 / 17,143`）**、以及 **右派/左派社革党人、孟什维克、布尔什维克党员获罪人数** 和 **1930 年三人小组（`179,620`）/ 院务会（`10,212`）/ 特别会议（`18,237`）分流数据** 在 `DATA-06` 表 A.3 中被略去。补入这几行能直接支撑“1925–1927 年契卡打击的农民中贫中农远多于富农，而 1930 年富农定罪暴增至 14.8 万”的档案洞见。
  2. **卡片 ID 简写**：`DATA-06` L94、L97 将 [`CLM-davies-1980-autumn-1929-great-turn-fabrication`](../historiography/claims/CLM-davies-1980-autumn-1929-great-turn-fabrication.md) 简写为 `CLM-davies`，应补全标准 ID。

---

## 三、 专项核查 C：L3 微距编年、10 张新卡与 5 份概念/争鸣卡的史实、票数、职务与断链审计

### 3.1 4 卷 L3 微距编年专项问题

1. **【P0 票数与投票立场张冠李戴】`timeline/L3_daily/1918-01_constituent_assembly_and_brest_crisis.md`（L7、L91）**
   - **原文 L7（T1）**：`2 月 18 日德军恢复全面推进，中央委员会同日两度表决：早间列宁立即求和动议 6 : 7 败北，夜间第三次托洛茨基弃权助列宁 7 : 5 : 4 逆转。`
   - **原文 L91（T2）**：`第三次 托洛茨基改投弃权，列宁案以 7 : 5 : 4 通过——决定立即向柏林发电请求和谈。`
   - **对勘 `RN-W2-first-year-soviet-rule.md`（§3.2 L60、L63，引自 Rabinowitch 2007 pp. 163–164, 174–175）与 `EVT-1918-03-03-brest-litovsk-treaty.md`**：
     - **1918 年 2 月 18 日晚（第三次表决）**：面对德军占领德文斯克，**托洛茨基从反对转为投票支持列宁**（因为德国已以行动证明确实会进攻），列宁关于立即致电柏林求和的提案以 **7 票赞成、5 票反对、1 票弃权（7 : 5 : 1）** 通过！
     - **1918 年 2 月 23 日下午（第五次表决）**：面对德方极其苛刻的 48 小时最后通牒及列宁以辞去党政一切职务相威胁，**托洛茨基（连同捷尔任斯基、克列斯廷斯基、越飞）才改投弃权票**，使接受德方条件的决议以 **7 票赞成、4 票反对、4 票弃权（7 : 4 : 4）** 通过！
     - **审计裁定**：撰写者将 2 月 18 日晚（`7:5:1`，托洛茨基投赞成票）与 2 月 23 日（`7:4:4`，托洛茨基等 4 人弃权）强行揉合成一个历史上不存在的“2 月 18 日夜托洛茨基弃权、`7 : 5 : 4`（共 16 票！）通过”，且漏掉了 2 月 23 日中央全会生与死的关键表决条目。必须拆清 2 月 18 日（`7:5:1`）与 2 月 23 日（`7:4:4`）两次表决！

2. **【P0 四卷 L3 底部候选事件账本全部断链】**
   - `1903-07_rsdlp_second_congress_split.md`（L93）与 `1919-10_civil_war_southern_and_petrograd_climax.md`（L96）链接至 `[`_w21_candidate_events.jsonl`](./_w21_candidate_events.jsonl)`；
   - `1918-01_constituent_assembly_and_brest_crisis.md`（L116）与 `1918-07_left_sr_uprising_and_red_terror_launch.md`（L116）链接至 `[`_w20_candidate_events.jsonl`](./_w20_candidate_events.jsonl)`；
   - **核查结果**：`timeline/L3_daily/` 目录下**根本不存在** `_w20_candidate_events.jsonl` 与 `_w21_candidate_events.jsonl`（相关事件已直接合入 [`timeline/events_ledger.jsonl`](../timeline/events_ledger.jsonl)）。应将断链修正为指向 `../events_ledger.jsonl`。

3. **【P1 票数异文未交代与标题错字】**
   - `1903-07_rsdlp_second_congress_split.md`（L7、L12、L55、L80）：L55 写崩得 `5` 票退场（与 `MTG-1903` 一致），L80 写中央机关报三人编委会以 `25 赞成、2 反对、20 弃权` 通过并挂靠脚注 `[^H180]`。但查对 [`RN-W4B-consciousness-spontaneity-1903.md`](../reading-notes/RN-W4B-consciousness-spontaneity-1903.md)（L128–130）与 [`CLM-haimson-1955-1903-second-congress-split.md`](../historiography/claims/CLM-haimson-1955-1903-second-congress-split.md)（L26），Haimson 原书 pp. 180–181 记为“崩得 4 票退场”及编委会“22 票赞成、20 票弃权、2 票空白”。应在 T3 §3.1 校勘栏明确说明大会记录（5 票退场；25:2:20）与 Haimson（4 票；22:20:2）的统计口径差异，勿将 `25:2:20` 直接归于 `[^H180]`。
   - `1919-10_civil_war_southern_and_petrograd_climax.md`：
     - **L1 标题错字**：`西北尤登尼奇彼得的格勒“双危机”` → 多出一字，应改为 `西北尤登尼奇彼得格勒“双危机”`。
     - **L7、L36、L66 日期异文**：奥廖尔失守日期 Mawdsley 记为 `10月14日`，而 `RN-W20-civil-war-geopolitics`（L107，引卡库林）记为 `10月13日`；布琼尼骑兵军重夺沃罗涅日，卡库林明确记为 `10月24日`（L3 中 L66 仅笼统锚在 `10月20日（中旬综合锚点）`）。建议在 T2/T3 中补注 `10月13日/14日` 与沃罗涅日 `10月24日` 精确日期。

---

### 3.2 10 张新增实体卡专项问题（职务错位、生平硬伤与幻觉词）

1. **【P0 人物职务与入局年份张冠李戴】`cards/persons/PER-kalinin.md`（L25、L26、L48）**
   - **职务错位（L25）**：写 `十月革命后任彼得格勒苏维埃主席`。**史实错误**！十月革命后加里宁当选的是 **彼得格勒市杜马主席 / 市长（Городской голова）**；当时的**彼得格勒苏维埃主席**是托洛茨基（1917.09–12），继任者是季诺维也夫（1917.12 起）！
   - **入局年份错误（L26）**：写 `1925年1月当选政治局委员`。**史实错误**！加里宁自 1919 年八大起为政治局候补委员，是在 **1925 年 12 月联共（布）十四大后的 1926 年 1 月 1 日一中全会** 上才升任政治局正式委员（而非 1925 年 1 月）！
   - **伪双历（L26）**：`1919-03-30 [O.S.] / 1919-04-12 [N.S.]`（已见 §1.2）。
   - **章节页码错配（L48）**：脚注引用 Cohen p. 289 却指向 `ch19_pages_476-500.md`；查 [`CLM-cohen-1973-july-1928-plenum-and-kamenev.md`](../historiography/claims/CLM-cohen-1973-july-1928-plenum-and-kamenev.md)，加里宁与沃罗希洛夫 1928 年 7 月转向位于 **`ch12_pages_301-325.md#L499-L615`**。

2. **【P0 出生地、入局年份与任职时段三重硬伤】`cards/persons/PER-kuibyshev.md`（L25、L26、L27、L57）**
   - **出生地错误（L25）**：写 `生于 1888-05-25 [O.S.] / 1888-06-06 [N.S.] 奥伦堡`。**史实错误**！古比雪夫生于西伯利亚草原总督区首府 **鄂木斯克（Омск / Omsk）**，而非奥伦堡（Оренбург）！
   - **入局年份错误（L26）**：写 `1923–1926 年任中央监察委员会（ЦКК）主席兼工农检查院（Рабкрин）人民委员，1925年同时进入政治局`。**史实与党章双重错误**！按俄共（布）党章，中监委（ЦКК）主席不得兼任中央委员或政治局委员；古比雪夫是在 1926 年 8 月卸任中监委主席改任最高国民经济委员会（ВСНХ）主席后，于 **1927 年 12 月 19 日（联共十五大后）** 才当选政治局委员！
   - **职务时段混淆（L27、L57）**：写 `1926–1935 ВСНХ 主席兼 Госплан 领导`。**史实错误**！古比雪夫任 **最高国民经济委员会（ВСНХ）主席为 1926 年 8 月至 1930 年 11 月**（1930 年 11 月由奥尔忠尼启则接任），随后于 **1930 年 11 月至 1934 年 5 月转任国家计划委员会（Госплан）主席**（且 ВСНХ 本身于 1932 年 1 月即被撤销改组为重工业、轻工业、森林工业三人民委员部，根本不可能任职至 1935 年！）。

3. **【P0 幻觉词与双卡免职日期冲突】`cards/persons/PER-kaganovich.md`（L8、L25、L28、L58）与 `PER-tomsky.md`（L27）**
   - **严重幻觉词（L8、L25）**：
     - `PER-kaganovich.md` L8 YAML `aliases` 赫然写着 `"第二号书记 (临汾组织系统)"`——**“临汾”系中国山西省地名（疑为“斯大林组织系统”或拼音输入法乱码幻觉）**！
     - L25 写 `早年为腾格里诺工人`——卡冈诺维奇生于基辅省切尔诺贝利附近的卡巴尼村（Кабаны），早年在基辅当鞋匠/制革工人，“腾格里诺”系无据乱码！
   - **托姆斯基去职日期双卡自相矛盾**：
     - `PER-kaganovich.md` L28 与 L58 称：`1928-12-23` 卡冈诺维奇将托姆斯基排挤出工会领导层（`迫使托姆斯基 12 月 23 日辞职`），又在 L28 写 `1929-06-02 全苏工会中央理事会第二次全会正式解除托姆斯基主席职务`；
     - `PER-tomsky.md` L27 则写：`1929年4月中央全会秘密决定将其撤职，1929-06-02 全苏工会中央理事会全会正式解除其主席职务`。
     - **对勘史实与 `CLM-filtzer-1986-1929-tomsky-purge-and-shock-work.md`**：1928 年 12 月全苏工会八大期间，托姆斯基为抗议政治局强塞卡冈诺维奇进入工会主席团而**提出辞呈，但政治局当时拒绝批准其辞职**（改令其“休假”架空）；直到 **1929 年 4 月联共（布）中央与中监委联席全会** 才作出撤销其职务的政治决定，并由 **1929 年 5 月底至 6 月初的全苏工会中央理事会第二次全会**（6 月 2 日《劳动报》公布）正式解除其主席职务。`PER-kaganovich.md` 应明确区分“1928 年 12 月托姆斯基抗议辞职被拒但遭休假架空”与“1929 年 4 月中央全会/5–6 月工会全会正式撤职”。

4. **【P0 部队番号张冠李戴】`cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md`（L20）**
   - **原文 L20（T1）**：`图哈切夫斯基率第7集团军与契卡人质手段镇压`。
   - **审计裁定**：图哈切夫斯基率领 **第 7 集团军（7-я армия）** 镇压的是 1921 年 3 月的 **喀琅施塔得起义**！而在 1921 年 5–7 月镇压坦波夫安东诺夫起义时，他被任命为 **坦波夫省部队司令员（Командующий войсками Тамбовской губернии）**，麾下主力为骑兵部队、库尔斯克军校学员及内卫部队，并非驻彼得格勒的第 7 集团军（正文 L35 写“调集约 10 万正规军”，唯独 T1 L20 误植了喀琅施塔得的“第 7 集团军”）。

5. **【P0 争鸣卡 ID 断链】`cards/meetings/MTG-1924-05-13th-party-congress.md`（L15、L43）**
   - **原文**：YAML `debates` 与正文 L43 引用 `DEB-1923-lenin-testament-and-succession`。
   - **审计裁定**：库内不存在该 ID！正确的争鸣卡 ID 为 [`DEB-1922-lenin-testament-and-stalin-rise`](../historiography/debates/DEB-1922-lenin-testament-and-stalin-rise.md)（同批 `PER-krupskaya.md` L15 引用正确）。

6. **【P1 其余实体卡微瑕】**
   - `PER-frunze.md`（L26）：写 `任乌克兰国防人民委员等要职期间`。1920–1924 年乌克兰苏维埃共和国并无独立的“乌克兰国防人民委员”一职，伏龙芝的实际职务为 **共和国革命军事委员会驻乌克兰全权代表兼乌克兰及克里米亚武装力量司令员、乌克兰人民委员会副主席**。
   - `EVT-1918-1920-russian-civil-war.md`（L5）：`start_ns: "1918-01-01"` 为纯机械占位符，建议锚定于 `1918-05-25`（捷克斯洛伐克军团起义/全面内战爆发）或 `1918-02-23`（红军建军/国内战争总动员起点）并在正文说明分期争议。

---

### 3.3 概念总表 `CONCEPT_GENEALOGY_INDEX.md` 与 4 张新争鸣卡专项问题

1. **【P0 俄语语法错误、乱码幻觉与断链】`glossary/CONCEPT_GENEALOGY_INDEX.md`**
   - **断链 Claim ID（L87）**：引用 `CLM-smith-sa-1983-workers-control-pragmatism`（同见 `DEB-1918-war-communism-ideology-vs-emergency.md` L24）。库内该文件**不存在**！实际存在的是 [`CLM-smith-1983-workers-control-pragmatism.md`](../historiography/claims/CLM-smith-1983-workers-control-pragmatism.md) 与 [`CLM-smith-sa-1983-defensive-workers-control.md`](../historiography/claims/CLM-smith-sa-1983-defensive-workers-control.md)。
   - **俄语性数格语法错误（L19 序号 7）**：`Революционный оборончество` —— 名词 `оборончество`（护国主义）为**中性**，形容词词尾必须用中性 **`Революционное оборончество`**（而非阳性 `-ый`）。
   - **专名与文字乱码（5 处）**：
     - L47（表二序号 1）：`党领导干部垄净化` → 乱码，应为 **`党领导干部垄断化/寡头化`**；
     - L52（表二序号 6）：`分裂症派世界革命期待` → 极其刺眼的机翻幻觉词（疑似将“齐美尔瓦尔德左派/失败主义派/分裂派 schismatic”机翻为精神医学名词“分裂症派”），必须改为 **`齐美尔瓦尔德左派 / 革命失败主义派的世界革命期待`**；
     - L56（表二序号 10）：`1921 年辞赋 retrospect 标签` → 乱码（“追赋”误作“辞赋”），应改为 **`1921 年事后追赋（retrospective）标签`**；
     - L57（表二序号 11）与 `DEB-1929-collectivization-and-dekulakization-causes.md`（L18）：将 [`POL-ural-siberian-method`](../cards/policies/POL-ural-siberian-method.md)（乌拉尔-西伯利亚方法）误写为 **`乌里-西伯利亚方法`**，应统一改为 **`乌拉尔-西伯利亚方法`**；
     - L111（第四节）：`如互相指责“民粹”“贝纳巴夫”` → “贝纳巴夫”系无意义音译乱码（疑为“波拿巴主义 Бонапартизм”或“伯恩施坦主义 Бернштейнианство”之讹），应改为 **`“民粹派”“波拿巴主义/伯恩施坦主义”`**。
   - **DATA 卡片 ID 简写（L27、L61、L93）**：将 `DATA-02-1922-1924-scissors-crisis-and-chervonets` 简写为 `DATA-02`（同理 `DEB-1929` L32 将 `DATA-03-1926-1929-grain-procurement-and-nemchinov-table` 简写为 `DATA-03`），建议补全标准 ID。

2. **【P1 历史遗留错误表述复发】`historiography/debates/DEB-1917-dual-power-and-february-origins.md`（L14、L23、L33）**
   - **审计发现**：L14、L23、L33 三次出现 `3月3日[O.S.]米留可夫废除《基本法》约束` / `废除杜马法统`。
   - **对勘前序审计 `AUD-05` 与 `AUD-06`**：库内早已裁定，“废除 1906 年《基本法》”系对 Burdzhalov / Hasegawa 的误读；史实是 3 月 3 日临时政府与执委会联席会议上，米留可夫等人宣布临时政府系革命产物、拥有“全部权力（полнота власти）”，**拒绝向由旧选举法产生的第四届国家杜马负责**（而非正式颁布法令废除整部《基本法》）。应将该表述修正为“拒绝向国家杜马负责、主张临时政府握有‘全部权力’从而切断杜马法统约束”。

3. **【P1 争鸣卡双卡并存的引文分流说明】`DEB-1918-war-communism-ideology-vs-emergency.md`**
   - 库内此前已存在 [`DEB-1918-war-communism-ideology-or-emergency.md`](../historiography/debates/DEB-1918-war-communism-ideology-or-emergency.md)。新卡 T3 §1 已主动说明新卡聚焦 W16–W20（Smith 1983 工厂委员会与卡库林/Mawdsley 军事专家维度）并与旧卡 `or-emergency` 互补，但建议在旧卡 `or-emergency` 的 `see_also` 中双向回链新卡，以免图谱检索分裂。

---

## 四、 可执行整改清单（Actionable Checklist）

> 请后续可写权限 Agent 按以下清单逐条定位修复，完成后复跑 `python scripts/kb.py audit-graph`：

### P0 级（史实、历法、票数、职务与断链硬伤，必须修复）
- [ ] **1. [`timeline/L3_daily/1918-01_constituent_assembly_and_brest_crisis.md`](../timeline/L3_daily/1918-01_constituent_assembly_and_brest_crisis.md)**
  - **L19**：将 `### 1918-01-05 [O.S.] / 1918-01-18 [N.S.]（星期六）` 改为 `（星期五）`。
  - **L29**：将 `### 1918-01-06 [O.S.] / 1918-01-19 [N.S.]（星期日）` 改为 `（星期六）`。
  - **L7、L91**：修正 1918-02-18 夜间第三次表决票数与托洛茨基立场——**2 月 18 日夜托洛茨基改投赞成票，列宁提案以 `7 : 5 : 1`（7 赞成、5 反对、1 弃权）通过**；并补入 **1918-02-23（星期六）** 中央委员会表决德方 48 小时最后通牒条目（列宁以辞职相逼，**托洛茨基等 4 人弃权，以 `7 : 4 : 4` 通过**）。
  - **L43–L83**：修正编年体时序倒置（将 `01-08 [O.S.]` 移至 `01-10 [O.S.]` 之前；将 `01-28 [O.S.] / 02-10 [N.S.]` 移至 `1918-02-14` 之前）。
  - **L116**：将断链 `[`_w20_candidate_events.jsonl`](./_w20_candidate_events.jsonl)` 改为指向 `[`events_ledger.jsonl`](../events_ledger.jsonl)`。
- [ ] **2. [`timeline/L3_daily/1918-07_left_sr_uprising_and_red_terror_launch.md`](../timeline/L3_daily/1918-07_left_sr_uprising_and_red_terror_launch.md)**
  - **L81**：将 `### 1918-09-05（星期五）` 改为 `### 1918-09-05（星期四）`。
  - **L116**：将断链 `[`_w20_candidate_events.jsonl`](./_w20_candidate_events.jsonl)` 改为指向 `[`events_ledger.jsonl`](../events_ledger.jsonl)`。
- [ ] **3. [`cards/persons/PER-kalinin.md`](../cards/persons/PER-kalinin.md)**
  - **L25**：将 `十月革命后任彼得格勒苏维埃主席` 改为 `十月革命后任彼得格勒市杜马主席（市长）`。
  - **L26**：将伪双历 `` `1919-03-30 [O.S.] / 1919-04-12 [N.S.]` `` 改为纯公历 `` `1919-03-30` ``；将 `1925年1月当选政治局委员` 改为 `1926年1月1日（十四大后）当选政治局正式委员`。
  - **L48**：将 `ch19_pages_476-500.md` 修正为 `ch12_pages_301-325.md#L499-L615`。
- [ ] **4. [`cards/persons/PER-kuibyshev.md`](../cards/persons/PER-kuibyshev.md)**
  - **L25**：将出生地 `奥伦堡` 改为 `鄂木斯克（Омск）`。
  - **L26**：将 `1925年同时进入政治局` 改为 `1927年12月（十五大后）进入政治局`。
  - **L27、L57**：将 `1926–1935 ВСНХ 主席兼 Госплан 领导` 修正为 `1926年8月—1930年11月任最高国民经济委员会（ВСНХ）主席，1930年11月—1934年5月转任国家计划委员会（Госплан）主席兼人民委员会副主席`。
- [ ] **5. [`cards/persons/PER-kaganovich.md`](../cards/persons/PER-kaganovich.md)**
  - **L8**：删除 `aliases` 中的幻觉词 `"第二号书记 (临汾组织系统)"`，改为 `"斯大林的头号组织干将"` 或仅保留 `"卡冈诺维奇"`。
  - **L25**：将乱码 `早年为腾格里诺工人` 改为 `生于基辅省卡巴尼村，早年为基辅制革与制鞋工人`。
  - **L28、L58**：将 `迫使托姆斯基 12 月 23 日辞职` 修正为 `迫使托姆斯基 12 月提出抗议辞呈（政治局未予批准但令其休假架空），并于 1929 年 4 月中央全会及 6 月 2 日全苏工会中央理事会全会正式解除其职务`，与 `PER-tomsky.md` 保持一致。
- [ ] **6. [`cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md`](../cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md)**
  - **L20**：将 `图哈切夫斯基率第7集团军与契卡人质手段镇压` 中的 `第7集团军`（喀琅施塔得平叛部队）改为 `坦波夫省作战集团（约10万正规军）`。
- [ ] **7. [`cards/meetings/MTG-1924-05-13th-party-congress.md`](../cards/meetings/MTG-1924-05-13th-party-congress.md)**
  - **L15、L43**：将不存在的 `DEB-1923-lenin-testament-and-succession` 修正为 `DEB-1922-lenin-testament-and-stalin-rise`。
- [ ] **8. [`historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md`](../historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md) 与 [`glossary/CONCEPT_GENEALOGY_INDEX.md`](../glossary/CONCEPT_GENEALOGY_INDEX.md)、[`DEB-1918-war-communism-ideology-vs-emergency.md`](../historiography/debates/DEB-1918-war-communism-ideology-vs-emergency.md)**
  - **`DEB-1918-red-terror` L18**：删去 `1918年9月5日[O.S.]` 中的错误标签 `[O.S.]`。
  - **`CONCEPT_GENEALOGY_INDEX.md` L87 与 `DEB-1918-war-communism-ideology-vs-emergency.md` L24**：将断链 ID `CLM-smith-sa-1983-workers-control-pragmatism` 修正为 `CLM-smith-sa-1983-defensive-workers-control`（及 `CLM-smith-1983-workers-control-pragmatism`）。
  - **`CONCEPT_GENEALOGY_INDEX.md` L19、L47、L52、L56、L57、L111**：修正俄语中性词尾 `Революционное оборончество`；修正乱码词 `党领导干部垄断化`（L47）、`齐美尔瓦尔德左派/失败主义派`（L52，替掉“分裂症派”）、`事后追赋`（L56，替掉“辞赋”）、`乌拉尔-西伯利亚方法`（L57 及 `DEB-1929` L18，替掉“乌里”）、`“波拿巴主义/伯恩施坦主义”`（L111，替掉“贝纳巴夫”）。

### P1 级（口径细化、双历补标与规范对齐）
- [ ] **9. [`timeline/L3_daily/1903-07_rsdlp_second_congress_split.md`](../timeline/L3_daily/1903-07_rsdlp_second_congress_split.md)**：在 T3 校勘栏补注崩得退场票数（大会记录 `5` 票 vs Haimson 记 `4` 票）与编委会改选票数（`25:2:20` vs Haimson p.180 记 `22:20:2`）的口径差异；L93 断链 `_w21_candidate_events.jsonl` 改为 `../events_ledger.jsonl`。
- [ ] **10. [`timeline/L3_daily/1919-10_civil_war_southern_and_petrograd_climax.md`](../timeline/L3_daily/1919-10_civil_war_southern_and_petrograd_climax.md)**：L1 标题 `彼得的格勒` 改为 `彼得格勒`；L36 补注卡库林记奥廖尔失守为 `10月13日`、L66 补注布琼尼重夺沃罗涅日为 `10月24日`；L96 断链 `_w21_candidate_events.jsonl` 改为 `../events_ledger.jsonl`。
- [ ] **11. [`cards/persons/PER-frunze.md`](../cards/persons/PER-frunze.md)**：L25 生辰补齐双历 `1885-01-21 [O.S.] / 1885-02-02 [N.S.]`；L26 将 `乌克兰国防人民委员` 修正为 `乌克兰及克里米亚武装力量司令员兼乌克兰人民委员会副主席`。
- [ ] **12. [`data/DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md`](../data/DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md)**：L78 明确 `244 家工委会（占工委会总数 39%，其中大中型企业 96 家）`。
- [ ] **13. [`data/DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md`](../data/DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md)**：表 A.3 建议增补 `RN-W20-nov-dec-1929` §3.3 中的富农/中农/贫农与各党派被告细分行及 1930 年三轨审判分流数据；L94、L97 将 `CLM-davies` 展开为完整 ID `CLM-davies-1980-autumn-1929-great-turn-fabrication`。
- [ ] **14. [`historiography/debates/DEB-1917-dual-power-and-february-origins.md`](../historiography/debates/DEB-1917-dual-power-and-february-origins.md)**：L14、L23、L33 将 `米留可夫废除《基本法》约束` 修正为 `米留可夫拒绝临时政府向国家杜马负责、主张临时政府握有革命赋予的“全部权力”`。
