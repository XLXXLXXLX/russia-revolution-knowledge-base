---
id: AUD-27-paseo-pilot-reader-ch09
type: audit
auditor_model: antigravity/gemini-4-argon
target_wave: W63-paseo-pilot
role: dialectic-auditor
target_files:
  - reader/ch09_war_communism_and_kronstadt_turn.md
status: closed
updated_at: "2026-11-25"
remediated_at: "2026-11-25"
---

# AUD-27｜`reader/ch09_war_communism_and_kronstadt_turn.md` 跨家族 Defect-Only 精简审计

- **审计对象**：[ch09_war_communism_and_kronstadt_turn.md](../reader/ch09_war_communism_and_kronstadt_turn.md)
- **对照基准**：`cards/`（`POL-war-communism`、`CON-workers-control`、`INS-vsnkh-and-gosplan`、`EVT-1920-1921-tambov-and-peasant-revolts`、`EVT-1921-kronstadt`、`MTG-1921-rcpb-10th-congress`、`POL-ban-on-factions-1921`、`POL-nep`、`PER-shlyapnikov`、`PER-tukhachevsky`、`PER-antonov`）、`data/DATA-04..05`、`timeline/L3_daily/1921-03_kronstadt_and_10th_congress.md`、`historiography/debates/DEB-*`、`historiography/claims/CLM-*`、`sources/web-archive/` 三篇 S 级原典及 `benchmarks/suites/b4b_historiography_1918_1929.jsonl`。
- **零缺陷审查项（一行带过）**：
  - **P0 史实/历法/引文硬伤**：无 P0 缺陷（1918-02-14 改历前 `1917-11-14 / 11-27`、`1917-12-02 / 12-15` 双历换算 `+13` 天准确，改历后 1918.02–1921.03 全用单公历且无伪造旧历；`AUD-23A`/`AUD-24` 已修毕的第 0116 号毒气令签发日留白、1.02:1 工资比、安东诺夫领导权时点、喀琅施塔得 17 日夜千余人撤离与全战役约八千人入芬分列均未复发）。
  - **零内部脚手架泄漏与模态 A1 语体**：无 P0/P1 缺陷（正文与注释零 `[T1]/[T2]/[T3]`、`CLM-*`、`PER-*`、`1-Hop`、`[O.S.]/[N.S.]`、`S级/A级` 内部标签泄漏，全文保持冷静克制的现代学术史分析语体，章末 `<details>` 折叠索引链接均有效）。

---

## P1 缺陷清单与精确替换矩阵

### P1-01｜将 1921 年 3 月 28 日人民委员会法令核定的粮食税普特数直接归入 3 月 21 日全俄中执委法令正文

- **位置**：[ch09_war_communism_and_kronstadt_turn.md:63](../reader/ch09_war_communism_and_kronstadt_turn.md#L63)
- **依据**：馆藏 S 级原典 [1921-03-21_decree-on-tax-in-kind-prodnalog.md:33-64, 179](../sources/web-archive/E03_E08_party_and_state_docs/1921-03-21_decree-on-tax-in-kind-prodnalog.md#L179) 核实，1921 年 3 月 21 日全俄中央执行委员会《关于以粮食和原料实物税代替余粮收集制的法令》（《法令汇编》1921 年第 26 号第 147 条，3 月 23 日公布）第 2 条仅规定税额须小于原收集制负担，**全文未写任何具体普特数**；将 1921–1922 年度全国粮食税总额从原余粮收集制的 4.23 亿普特核减至 2.4 亿普特，系**人民委员会于 1921 年 3 月 28 日另行颁布的决定**（《法令汇编》1921 年第 26 号第 148 条）。现文以“新法令……将 1921 至 1922 年度全国粮食税总额从原余粮收集制的 4.23 亿普特大幅核减至 2.4 亿普特”将两道法令焊成同一文本。

Target →

`3 月 21 日，全俄中央执行委员会正式颁布《关于以粮食和原料实物税代替余粮收集制的法令》。新法令废除了农村连环保，在春耕前预先公布税额，将 1921 至 1922 年度全国粮食税总额从原余粮收集制的 4.23 亿普特大幅核减至 2.4 亿普特，并允许农户在完税后自由支配剩余产品、在地方流转中换取所需的工农商品。`

Replacement →

`3 月 21 日，全俄中央执行委员会正式颁布《关于以粮食和原料实物税代替余粮收集制的法令》（3 月 23 日公布），确立了废除农村连环保、在春耕前预先公布累进税额，以及允许农户完税后自由支配剩余产品并在地方经济流转中交换的法律原则；3 月 28 日人民委员会随即颁布具体税额决定，将 1921 至 1922 年度全国粮食税总额从原余粮收集制的 4.23 亿普特大幅核减至 2.4 亿普特。`

---

### P1-02｜将 3 月 16 日闭幕日通过的《关于我们党内的工团主义和无政府主义倾向》决议置于 3 月 14 日段，并与 3 月 15 日“次日”形成错误日序

- **位置**：[ch09_war_communism_and_kronstadt_turn.md:61-63](../reader/ch09_war_communism_and_kronstadt_turn.md#L61-L63)
- **依据**：[MTG-1921-rcpb-10th-congress.md:27-28](../cards/meetings/MTG-1921-rcpb-10th-congress.md#L27-L28)、[CON-workers-control.md:56](../cards/concepts/CON-workers-control.md#L56) 及 [1921-03_kronstadt_and_10th_congress.md:142, 155](../timeline/L3_daily/1921-03_kronstadt_and_10th_congress.md#L155)。列宁于 3 月 13–14 日起草《关于党的统一》与《关于我们党内的工团主义和无政府主义倾向》两份决议草案，两项决议均于 **3 月 16 日大会闭幕日**表决通过（反对票均不足 30 票）。正文第 61 行在“3 月 14 日工会决议表决”后直接写“随后大会更专门通过决议，宣布宣传工团主义与无政府主义倾向同共产党员身份不相容”，第 63 行又以“在压服党内车间自治诉求的次日……3 月 15 日”承接，把 3 月 16 日闭幕日通过的反工团主义倾向决议错置到 3 月 15 日实物税报告之前。

Target →

`3 月 14 日工会决议表决中，列宁“十人纲领”以 336 票压倒性胜出，托洛茨基—布哈林纲领得 50 票，工人反对派仅得 18 票（另有 2 票弃权）；随后大会更专门通过决议，宣布宣传工团主义与无政府主义倾向同共产党员身份不相容。`

Replacement →

`3 月 14 日工会决议表决中，列宁“十人纲领”以 336 票压倒性胜出，托洛茨基—布哈林纲领得 50 票，工人反对派仅得 18 票（另有 2 票弃权）；至 3 月 16 日闭幕日，大会更专门通过《关于我们党内的工团主义和无政府主义倾向》决议，宣布宣传工团主义与无政府主义倾向同共产党员身份不相容。`

---

### P1-03｜1917–1918 年彼得格勒“35.1 万 → 14.87 万”漏标 773 家受调查工厂样本分母（与 `DATA-05` 全市口径冲突），且章末将皮拉尼 1921 年“隐性社会契约”命题与菲尔策混署

- **位置**：[ch09_war_communism_and_kronstadt_turn.md:11, 69](../reader/ch09_war_communism_and_kronstadt_turn.md#L11)
- **依据**：
  1. [smith_1983_red_petrograd/ch10_pages_251-275.md:283-350](../sources/monographs/smith_1983_red_petrograd/ch10_pages_251-275.md#L283-L350)（Table 15, `p. 245 / PDF p. 257`）、[CLM-smith-1983-post-october-centralization.md:22](../historiography/claims/CLM-smith-1983-post-october-centralization.md#L22)、[CON-workers-control.md:47, 81](../cards/concepts/CON-workers-control.md#L47) 与 [DATA-05:32-34, 85](../data/DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md#L32-L34)。`351,010 人（1917-01-01）→ 148,710 人（1918-04-01）` 及金属工 `167,192 人 → 43,129 人` 系史密斯表 15 中 **773 家受调查工厂样本（其中 231 家关闭，含 213 家金属厂）** 的统计；而 `DATA-05` §A.1 所录 1917 年初彼得格勒全市 1,011 家企业工厂工人（城市口径）为 **`392,828` 人**（含郊区约 `41.7` 万人）、金属工人为 **`237,369` 人**（另 §A.6 录 1918 年 1–5 月彼得格勒省百人以上金属厂工人由 `197,686` 人降至 `57,995` 人）。正文直接写“全市产业工人从 1917 年初的 35.1 万人……金属工人更从 16.7 万人……”，遗漏“773 家受调查工厂样本”分母，与 `DATA-05` 全市口径冲突。
  2. [CLM-pirani-2008-moscow-workers-nep-social-contract.md:22](../historiography/claims/CLM-pirani-2008-moscow-workers-nep-social-contract.md#L22)、[CLM-filtzer-1986-nep-unemployment-and-shopfloor-bargaining.md:19, 23-25](../historiography/claims/CLM-filtzer-1986-nep-unemployment-and-shopfloor-bargaining.md#L19)、[CLM-lebsky-industrial-paternalism-origins-1917-1929.md:19](../historiography/claims/CLM-lebsky-industrial-paternalism-origins-1917-1929.md#L19) 及 [DEB-1921-trade-union-controversy-and-party-unity.md:28](../historiography/debates/DEB-1921-trade-union-controversy-and-party-unity.md#L28)。“1921 年春压制独立工潮与非党工代会后确立以改善物质生活换取工人让渡政治代表权的隐性‘社会契约’”系 **西蒙·皮拉尼（Simon Pirani, 2008）** 的核心论断；而 **唐纳德·菲尔策（Donald Filtzer, 1986）** 论证的是新经济政策时期高失业率对公开集体抗争的抑制，以及在岗工人通过工资定额争议委员会（RKK）与工序控制保留的车间议价空间（直至 1928–1929 年托姆斯基被清洗后终结）。第 69 行将皮拉尼的“1921 年隐性社会契约”直接混署于皮拉尼与菲尔策两人名下。

Target（第 11 行）→

`全市产业工人从 1917 年初的 35.1 万人骤减至 1918 年 4 月的 14.87 万人，降幅达 58%，作为布尔什维克核心社会支柱的金属工人更从 16.7 万人萎缩至 4.3 万人，大批熟练骨干被抽调入红军与苏维埃行政机关。`

Replacement（第 11 行）→

`据史密斯所引彼得格勒 773 家受调查工厂样本（全市 1,011 家企业 1917 年初总计约 39.28 万工人），在岗工人从 1917 年 1 月初的 35.1 万人骤减至 1918 年 4 月初的 14.87 万人，降幅达 58%，其中作为布尔什维克核心社会支柱的受调查金属厂工人更从 16.7 万人萎缩至 4.3 万人，大批熟练骨干被抽调入红军与苏维埃行政机关。`

Target（第 69 行）→

`西蒙·皮拉尼与唐纳德·菲尔策等劳工史学者则进一步揭示，1921 年春压制独立工潮与非党工代会之后，新经济政策在城市确立了一种隐性的“社会契约”——以逐步恢复计件工资和物质供给，换取工人阶级让渡独立的政治代表权。`

Replacement（第 69 行）→

`劳工史学者亦从不同维度剖析了这一转型：西蒙·皮拉尼揭示，1921 年春压制独立工潮与非党工代会之后，新经济政策在城市确立了一种隐性的“社会契约”——以逐步恢复物质生活供给，换取工人阶级让渡独立的政治代表权；唐纳德·菲尔策与马克西姆·列布斯基则分别指出，新经济政策时期在岗工人虽仍能依托工资定额争议委员会（RKK）就车间定额与劳动保护展开微观博弈，却同时受制于高失业率风险与企业住房福利绑定（“工业家长制”）的深层依附。`

---

## P2 缺陷清单与精确替换矩阵

### P2-01｜尾注 `[^2]` 将《消息报》创刊号所载 3 月 1 日战列舰支队大会“全票赞成、2 票弃权”计票直接系于 2 月 28 日，未交代馆藏 S 级底本题头

- **位置**：[ch09_war_communism_and_kronstadt_turn.md:75](../reader/ch09_war_communism_and_kronstadt_turn.md#L75)
- **依据**：[1921-03-01_petropavlovsk-resolution.md:15, 21, 27, 61-73](../sources/web-archive/E02_E07_foundational_docs/1921-03-01_petropavlovsk-resolution.md#L61-L73) 与 [EVT-1921-kronstadt.md:28, 30, 66](../cards/events/EVT-1921-kronstadt.md#L28-L30)。馆藏 S 级《临时革命委员会消息报》第 1 期（1921 年 3 月 3 日）所载十五条决议题头为“1921 年 3 月 1 日第一、第二战列舰支队船员大会决议”，文末分记**支队大会“全票通过、2 票弃权”**与**全要塞卫戍大会“压倒多数通过（瓦西里耶夫与加里宁反对）”**两次表决；2 月 28 日《彼得罗巴甫洛夫斯克》号舰上先行通过另有政府通报及专著旁证（馆藏无独立 2 月 28 日异文）。

Target →

`[^2]: **《彼得罗巴甫洛夫斯克号决议》两阶段表决与口号校勘**：十五条决议先于 1921 年 2 月 28 日在战列舰水兵大会上通过（全票赞成、2 票弃权），3 月 1 日再经铁锚广场约 1.5 万军民大会以压倒多数确认（仅加里宁、瓦西里耶夫等极少数人反对），3 月 3 日刊于《临时革命委员会消息报》创刊号。`

Replacement →

`[^2]: **《彼得罗巴甫洛夫斯克号决议》表决记录与口号校勘**：十五条决议先于 1921 年 2 月 28 日在《彼得罗巴甫洛夫斯克》号舰上通过（有政府通报与阿夫里奇、盖茨勒专著旁证，馆藏无独立 2 月 28 日异文）；3 月 3 日《临时革命委员会消息报》创刊号所刊馆藏文本题为“1921 年 3 月 1 日第一、第二战列舰支队船员大会决议”，文末分记支队大会“全票通过、2 票弃权”（主席彼得里琴科、秘书佩列佩尔金）与铁锚广场约 1.5 万全要塞军民大会“压倒多数通过（仅瓦西里耶夫与加里宁等极少数人反对）”两次表决。`

---

### P2-02｜第 39 行将 2 月 26 日两舰紧急会议决定派团与 2 月 27 日赴彼得格勒工厂查访压入 2 月 26 日单日

- **位置**：[ch09_war_communism_and_kronstadt_turn.md:39](../reader/ch09_war_communism_and_kronstadt_turn.md#L39)
- **依据**：[getzler_1983_kronstadt/ch08_pages_201-225.md:1041-1048, 1091-1095](../sources/monographs/getzler_1983_kronstadt/ch08_pages_201-225.md#L1041-L1048)（`pp. 212–213`）与 [avrich_1970_kronstadt/ch03_pages_76-100.md:356-389](../sources/monographs/avrich_1970_kronstadt/ch03_pages_76-100.md#L356-L389)（`pp. 71–72`）。2 月 26 日两舰官兵召开紧急会议选派调查代表团（32 人），2 月 27 日前往彼得格勒各工厂查访，2 月 28 日返舰汇报。

Target →

`2 月 26 日，停泊在喀琅施塔得的波罗的海舰队主力战列舰《彼得罗巴甫洛夫斯克》号与《塞瓦斯托波尔》号官兵派出代表团前往彼得格勒工厂核实罢工真相。`

Replacement →

`2 月 26 日，停泊在喀琅施塔得的波罗的海舰队主力战列舰《彼得罗巴甫洛夫斯克》号与《塞瓦斯托波尔》号官兵召开紧急会议，选派三十二人代表团于次日前往彼得格勒工厂核实罢工真相。`

---

### P2-03｜第 13 行跨内战长句后的“至 9 月”漏标年份“1918 年”

- **位置**：[ch09_war_communism_and_kronstadt_turn.md:13](../reader/ch09_war_communism_and_kronstadt_turn.md#L13)
- **依据**：[CLM-duval-oppenheim-vtsik-and-vsnkh-consolidation.md:31](../historiography/claims/CLM-duval-oppenheim-vtsik-and-vsnkh-consolidation.md#L31)（Oppenheim 1973, `p. 19`）。最高经委演化为逾 42 个（1920 年底达 50 余个）垂直行业总局系 1918–1920 年内战全程演进，而中央机关 861 名技术专家中布尔什维克仅占 3.5%（30 人）的时点严格为 **1918 年 9 月**（当时设 18 个行业总局）。

Target →

`随着内战战线铺开，该机构演化为逾 42 个垂直行业总局（главкизм）构成的庞大金字塔，在燃料、冶金与军工领域实行集中调拨，至 9 月其中央机关聘用的 861 名技术专家中布尔什维克仅占 3.5%，部门割据与实物清算紊乱亦随之蔓延。`

Replacement →

`随着内战战线铺开，该机构逐步演化为逾 42 个垂直行业总局（главкизм）构成的庞大金字塔，在燃料、冶金与军工领域实行集中调拨；早在 1918 年 9 月，其中央机关聘用的 861 名技术专家中布尔什维克便仅占 3.5%，部门割据与实物清算紊乱亦随总局膨胀而不断蔓延。`

---

### P2-04｜第 47 行与第 67 行细节口径补正（阿夫里奇水兵农民出身与老兵领导层区分；十大书记处改组与 1923 年名册制创立年份区分）

- **位置**：[ch09_war_communism_and_kronstadt_turn.md:47, 67](../reader/ch09_war_communism_and_kronstadt_turn.md#L47)
- **依据**：
  1. [B4B-17](../benchmarks/suites/b4b_historiography_1918_1929.jsonl#L17) 与 [CLM-avrich-1970-sailor-social-composition.md:18, 22](../historiography/claims/CLM-avrich-1970-sailor-social-composition.md#L18)：第 47 行并提阿夫里奇与盖茨勒，但仅写出盖茨勒的入伍年份数据，宜补入阿夫里奇关于“虽 1921 年逾四分之三海员系农民出身，但农村青年历来是舰队激进主力且起义由资深水兵与技师领衔”的区分。
  2. [CLM-ali-rigby-secretariat-and-1923-nomenklatura-origins.md:27, 29](../historiography/claims/CLM-ali-rigby-secretariat-and-1923-nomenklatura-origins.md#L27) 与 [DATA-04:118-121](../data/DATA-04-party-membership-and-congress-votes-1903-1929.md#L118-L121)：原三位中央书记在十大不仅退出书记处，而且一并落选中央委员与组织局委员，改由莫洛托夫（任责任书记）、雅罗斯拉夫斯基与米哈伊洛夫接任；斯大林出任总书记在 1922 年 4 月（“一年后”），而组织局创立第 1、2 号官职等级名册制则在 **1923 年 6 月至 10 月**。

Target（第 47 行）→

`而在水兵构成上，盖茨勒据海军人事档案考证，《彼得罗巴甫洛夫斯克》号与《塞瓦斯托波尔》号两艘起义先锋战列舰中，超过九成水兵系 1917 年及以前入伍的资深老兵，整个波罗的海舰队在 1921 年初亦很大比例由 1918 年前入伍的老兵组成，临时革命委员会核心成员如彼得里琴科、佩列佩尔金更是早在 1912 年便已服役的老水兵。[^1]`

Replacement（第 47 行）→

`而在水兵构成上，阿夫里奇指出，尽管 1921 年舰队逾四分之三海员系农民出身，但农村青年历来是喀琅施塔得激进主义的温床，且起义由资深海员与战列舰技师领衔；盖茨勒更据海军人事档案考证，《彼得罗巴甫洛夫斯克》号与《塞瓦斯托波尔》号两艘起义先锋战列舰中，超过九成水兵系 1917 年及以前入伍的资深老兵，整个波罗的海舰队在 1921 年初亦很大比例由 1918 年前入伍的老兵组成，临时革命委员会核心成员如彼得里琴科、佩列佩尔金更是早在 1912 年便已服役的老水兵。[^1]`

Target（第 67 行）→

`在工会争论中支持托洛茨基的三名原中央书记——克列斯廷斯基、普列奥布拉任斯基与谢列布里亚科夫——悉数退出书记处，改由莫洛托夫出任中央责任书记，为一年后斯大林出任总书记并依托书记处建立官职等级名册制铺平了道路。`

Replacement（第 67 行）→

`在工会争论中支持托洛茨基的三名原中央书记——克列斯廷斯基、普列奥布拉任斯基与谢列布里亚科夫——悉数落选中央委员并退出书记处与组织局，改由莫洛托夫（任责任书记）、雅罗斯拉夫斯基与米哈伊洛夫接掌书记处，为 1922 年 4 月斯大林出任总书记及 1923 年夏秋组织局创立官职等级名册制铺平了道路。`
