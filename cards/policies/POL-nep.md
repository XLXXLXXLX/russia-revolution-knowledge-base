---
id: POL-nep
type: policy
title: 新经济政策
names:
  ru: Новая экономическая политика (НЭП)
  en: New Economic Policy (NEP)
  aliases: ["НЭП", "NEP", "新经济政策体制"]
dates:
  start_ns: "1921-03-21" # 以全俄中执委颁布《关于以实物税代替粮食和原料收集制的法令》为法制起点锚（俄共十大决议为 1921-03-15，公布为 03-23）
  end_ns: "1929-11-17" # 以联共（布）十一月全会处分布哈林、确立“大转变”为政治分期锚（非单一法律废止令，私商与个体农户系1928–1930逐步消灭）
coverage_status: multi-perspective
perspectives_present: ["institutional-economic-carr-davies", "bukharinist-revisionist-cohen-lewin", "cliometric-counterfactual-allen", "labor-social-filtzer-siegelbaum-pirani", "private-entrepreneur-ball", "russian-archival-danilov-khlevniuk-spitsyn"]
perspectives_missing: ["central-asian-and-caucasus-nep-bazaars"]
related_debates: ["DEB-1921-kronstadt-and-nep-origins", "DEB-1918-war-communism-ideology-or-emergency", "DEB-1928-bukharin-alternative", "DEB-1929-collectivization-and-dekulakization-causes"]
updated_at: "2026-11-21"
---

## [T1] 60秒定性微摘要
1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **分步退却、币制稳定与战后恢复（1921.03–1925）**：`1921-03-15` 俄共（布）十大通过《关于以实物税代替余粮收集制》决议，`1921-03-21` 全俄中执委颁布法令（`03-23` 公布，见 `1921-03-21_decree-on-tax-in-kind-prodnalog.md`）。最初设想仅限“地方周转商品交换”，1921年秋被迫承认货币买卖与私商（耐普曼，参 Alan Ball），同时由国家掌控大工业、银行、铁路与外贸垄断等“制高点”（`CLM-carr-1952-nep-retreat-and-commanding-heights`）。`1922–1924` 年索科利尼科夫主持以黄金/硬通货及商品票据作准备的国家银行券**切尔沃涅茨（червонец）**及1924国库券币制改革（详参 `DATA-02`、`POL-sokolnikov-chervonets-monetary-reform`），克服1923年秋 **“剪刀差危机”**（`EVT-1923-scissors-crisis`），至20年代中期工农业显著恢复（但不同行业、价格基期与领土口径存异，不宜简化为单一1913等值）。
- **鼎盛妥协、失业暗流与价格/积累张力（1925–1927）**：`1925-04` 十四次代表会议有限放宽农村雇工租地，布哈林将 NEP 阐发为经市场与供销信贷合作社“和平长入社会主义”的长期通道（`1925-04_bukharin-road-to-socialism.md`、`CON-smychka`）。体制内潜伏三重张力：（1）在岗熟练工实际工资回升，但企业经济核算（`хозрасчёт`）与农村人口涌入造成严重城市结构性失业，激发基层党员与老工人对耐普曼与专家高薪的身份焦虑（`CLM-filtzer-1986-nep-unemployment-and-shopfloor-bargaining`、`CLM-fitzpatrick-1991-nep-bolshevik-identity-crisis`）；（2）旧设备利用率趋满后，重工业扩建引发普列奥布拉任斯基“社会主义原始积累”与布哈林“市场均衡积累”论战（`CON-primitive-socialist-accumulation`）；（3）人为压低国营工业品牌价叠加信贷扩张制造长期“商品荒”（`товарный голод`），并于1926/27年度压低谷物相对比价（`CLM-carr-davies-1969-grain-price-scissor-1927`）。
- **第107条非常措施、乌拉尔—西伯利亚方法与瓦解（1927冬–1929.11）**：1927年秋冬国家谷物收购骤降（叠加英苏断交“战争恐慌”），斯大林于 `1928-01` 赴西伯利亚动用《刑法典》**第107条**没收余粮、关闭集市；经七月全会短暂退让后，1928–1929年冬演变为操纵村社大会强派指标、五倍罚款及第61条苦役的 **“乌拉尔—西伯利亚方法”**（`CLM-lewin-peasants-1968-ural-siberian-method`、`POL-ural-siberian-method`）。随私商被挤垮、城市重回配给制及 `1929-11-17` 十一月全会将布哈林逐出政治局，NEP 在政治上终结。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | `initiated_by` | 1921.03–1923.01 | 在1921年春主导从余粮收集制向实物税战略退却，晚年口授《论合作社》重塑NEP长期定位 | `1921-03-21_decree-on-tax-in-kind-prodnalog.md`; `1923-01-04_on-cooperation.md` |
| `PER-bukharin` | `theorized_and_defended` | 1924–1929.11 | 将NEP发展为工农市场结合与渐进平衡工业化纲领，1928–1929反对将非常征粮常态化而败北 | `DEB-1928-bukharin-alternative`; `1928-09-30_bukharin-notes-of-an-economist.md` |
| `PER-sokolnikov` | `stabilized_currency` | 1922–1925 | 执掌财政人民委员部主持切尔沃涅茨与1924币制改革，以硬预算与外贸调节支撑NEP市场运行 | `POL-sokolnikov-chervonets-monetary-reform`; `DATA-02` |
| `PER-preobrazhensky` | `challenged_by` | 1923–1927 | 在《新经济学》提出“社会主义原始积累规律”与价值规律对抗，主张靠价格/关税杠杆而非暴力转移剩余 | `CON-primitive-socialist-accumulation`; `CLM-preobrazhensky-1926-primitive-socialist-accumulation-law` |
| `PER-stalin` | `co-defender -> dismantler` | 1925–1927 维护；1928–1929 瓦解 | 先联手布哈林维护NEP击败托季反对派；1928年初诉诸第107条非常措施，继而以乌拉尔—西伯利亚方法与大转变终结NEP | `CLM-lewin-peasants-1968-ural-siberian-method`; `DEB-1928-bukharin-alternative` |
| `MTG-1928-11-cc-plenum` | `compromise-erosion-milestone` | 1928-11-16–11-24 | 最终决议虽保留刺激农民经济利益为中心任务之一的表述，但未采纳废止个别课税要求，确认高工业投资与反右倾方针 | `CLM-kak-lomali-nep-1928-rykov-control-figures-dilemma`; `CLM-khlevniuk-danilov-2000-nov-1928-plenum-compromise-trap` |
| `EVT-1921-kronstadt` | `precipitated_by` | 1921.02–03 | 农村安东诺夫等农民起义、彼得格勒/萨拉托夫工潮与喀琅施塔得水兵起义共同倒逼经济退却 | `DEB-1921-kronstadt-and-nep-origins`; `CLM-dugarm-2001-tambov-grain-warfare-and-antonovshchina` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：NEP 迅速恢复了内战后濒临崩溃的农业播种与城市日常供给，建立了苏联早期最活跃的多元经济与学术空间；但在党内政治上始终伴随 1921 年派别禁令与对孟什维克/社革党的彻底取缔（“经济放宽、政治收紧”）。
- **主要解释分歧**（详参 `DEB-1928-bukharin-alternative`）：
  - **政治人为扼杀、价格失策与动态反事实可行论（Stephen Cohen、Moshe Lewin、Robert C. Allen）**：科恩与勒温论证1927冬收购危机源于压低谷物比价与投资过热而非小农枯竭；艾伦（`CLM-allen-2003-nep-continuation-vs-collectivization-counterfactual`）测出NEP农户农产品外销价格弹性达 **`0.7`**，其多部门反事实模拟显示“延续NEP市场农业+重工业投资+软预算约束”至1939年GDP可达 `3,483亿` 卢布（与实际值 `3,449亿` 相当，同时在注释中保留贸易条件恶化与政治约束限定），无需承受集体化饥荒。
  - **内在结构死胡同与地缘赶超论（E. H. Carr、R. W. Davies 部分限定、Alec Nove、Mark Harrison、叶·斯皮岑）**：强调1917土地均分已瓦解高商品率大农庄，在无外债与地缘围堵压力下，单靠自愿市场激励难以短期筹足重工业与国防积累（`CLM-nove-1964-stalin-necessity-dilemma`、`CLM-spitsyn-1920s-intraparty-struggle-and-great-turn`）。
  - **“政治剥夺社会契约”与基层焦虑论（Simon Pirani、Donald Filtzer、Sheila Fitzpatrick、Alan Ball）**：皮拉尼（`CLM-pirani-2008-moscow-workers-nep-social-contract`）揭示1921年春莫斯科非党派工代会选举遭压制后，NEP确立以物质工资恢复换取工人交出政治代表权的社会契约；菲尔策尔与菲茨帕特里克指出高失业与耐普曼分化使青年党员欢迎反市场进攻，而轻工业老工人则在1928–1929年契约破裂时罢工抗议（`CLM-rossman-2005-ivanovo-worker-strikes-1928-1929`）。

## [T3] 深度考证、分期细目与原文引证档案

### 3.1 定量序列与关键口径警示（对接 `data/`）
1. **货币稳定与剪刀差序列（`DATA-02-1922-1924-scissors-crisis-and-chervonets.md`）**：1923年10月1日零售/批发相对价格剪刀差达峰值后，经工业托拉斯降价、信贷收紧与1924年春币制改革收敛；注意区分作为国家银行纸质银行券流通的 `червонец` 与仅主要供对外结算探索而少量铸造的金切尔文硬币（`RN-W32-katasonov-trade-monopoly-chervonets-and-two-circuit-ruble.md`）。
2. **粮食收购与涅姆钦诺夫表口径陷阱（`DATA-03-1926-1929-grain-procurement-and-nemchinov-table.md`）**：
   - 严禁将**农业年度前9个月累计收购量**与**全年12个月总收购量**混同比较；
   - 斯大林 `1928-05-28`《在粮食战线上》（`1928-05-28_stalin-on-the-grain-front.md`）援引统计学家涅姆钦诺夫表称商品粮率由战前26%腰斩至1926/27年的13.3%，Carr & Davies（1969）考证指出该表混合了战前粗估与排除村内周转的口径，放大了结构危机感。
3. **1928–1929 强制征粮演进两阶段区分**：
   - **第一阶段（1928.01–04）**：主要援引《苏俄刑法典》第107条以“投机罪”由司法/OGPU机关没收存粮（25%低价贷给贫农）；
   - **第二阶段（1928冬–1929）**：演变为绕开法庭、操纵村社大会（无最低法定人数限制）由贫农积极分子对富裕户强派数倍定额、违者五倍罚款拍卖家产并按第61条第3款判处苦役流放的“乌拉尔—西伯利亚方法”（`CON-peasant-commune-obshchina`、`POL-ural-siberian-method`）。
4. **计量经济与劳工微观补充口径（Allen 2003; Pirani 2008; Rossman 2005）**：
   - 艾伦分解1928年农产品外销较1913年低 `24%` 的成因：其中四分之三源于农工交易贸易条件（TOT）恶化 `35%`（供给价格弹性 `0.7`）；同时重工业固定资产倾斜体现为1928年生产资料部门仅占**非农资本存量** `7%`，而1929–1934年获**非农总投资** `23%`（两分母不可混同，`CLM-allen-2003-soft-budget-constraints-and-heavy-industry-drive`）。
   - 皮拉尼记录1921年4月莫斯科阿莫汽车厂苏维埃选举中非党派名单曾以 `277:136` 击败布尔什维克名单；罗斯曼记录1929年3月伊万诺沃巴拉绍夫纺织厂600名织工反七小时强化罢工，以及1928–1929年间纺织工名义日均收入下降 `4.6%` 而食品涨价与黑市使实际生活水平跌幅更深。

### 3.2 本地已核 S/A 级文献锚点
- **S级原典**：`sources/web-archive/E03_E08_party_and_state_docs/1921-03-21_decree-on-tax-in-kind-prodnalog.md`、`sources/web-archive/E02_E10_core_classics/1923-01-04_on-cooperation.md`、`sources/web-archive/E09_E10_party_debates/1925-04_bukharin-road-to-socialism.md`、`sources/web-archive/E06_E09_state_and_comintern/1928-09-30_bukharin-notes-of-an-economist.md`。
- **A级专著与论断**：`CLM-carr-1952-nep-retreat-and-commanding-heights`、`CLM-carr-davies-1969-grain-price-scissor-1927`、`CLM-lewin-peasants-1968-ural-siberian-method`、`CLM-filtzer-1986-nep-unemployment-and-shopfloor-bargaining`、`CLM-fitzpatrick-1991-nep-bolshevik-identity-crisis`、`reading-notes/ball_1987_nepmen/`。
