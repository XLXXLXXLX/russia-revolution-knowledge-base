# 1-Hop 去重平衡上下文包：`EVT-1927-war-scare-and-opposition-expulsion`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`EVT-1927-war-scare-and-opposition-expulsion`** (1927年“战争恐慌”危机与联合反对派溃败 | `cards/events/EVT-1927-war-scare-and-opposition-expulsion.md` | `multi-perspective`): 已覆盖=`revisionist-social, archival-post-soviet, trotskyist-biographical`；待补=`rural-peasant-oral-archive`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1927年英苏断交、沃伊科夫遇刺引发战争恐慌与抢购囤粮，OGPU六月行动大捕人：两项研究分别估6月至少9,000人、6—7月至少13,345人。反对派九月《政纲》遭禁，11月7日游行被冲散，14日托季被开除；十五大在购粮危机已发生时完成组织清除。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络（1927年纯格里高利公历 `[N.S.]`）
- **阶段一：外交破裂、沃伊科夫遇刺与OGPU“六月行动”（1927.01–07 [N.S.]）**：继1月13日布哈林、李可夫与伏罗希洛夫公开预警战争及英国 `05-12` 搜查伦敦阿尔科斯公司后，`05-27` 英国正式对苏断交；`06-07` 苏联驻波兰公使沃伊科夫在华沙遭白卫流亡者刺杀。尽管外交人民委员契切林主张苏联面临的是政治孤立而非迫在眉睫的战争，斯大林 `06-08` 致电莫洛托夫将其定性为英国挑衅并要求“肃清后方”；截至 `06-10`，OGPU即决处决20名前朝贵族要人并发动内战结束以来规模空前的搜捕行动。据维诺格拉多夫转述7月21日缅任斯基报告（韦利卡诺娃本人未获准查阅FSB原件），仅6月搜查至少20,000次、逮捕至少9,000人；韦利卡诺娃另将挪威公使馆所报6月最低10,000人与7月乌克兰、北高加索、白俄罗斯上报的3,345人拼合，推算两月至少13,345人被捕（丹尼洛夫估计受打击者中约十分之九为农民，属研究估算而非逐人身份核对）。`06-30` 政治局以逮捕上报数“过多”为由下令停止大规模行动（格鲁吉亚除外），但乌克兰、北高加索等地农村搜捕在7月仍延续。
- **阶段二：恐慌抢购、价格与商品失衡及秋冬购粮危机（1927.01–12 [N.S.]）**：战争宣传与谣言在城乡激起“战争将至、纸币作废、商店关门”的恐慌心理，春夏间食盐、火柴、布匹与面粉抢购蔓延（`CLM-velikanova-2013-war-scare-hoarding-and-grain-crisis`）。1927–28年度谷物总收成虽仅比前一丰年微降约 **6%**，但春季恐慌购买提前消耗了原拟秋季下乡换粮的工业品库存；叠加国家工业投资倾斜、官定粮价偏低（9月再降3%–5%）、私商高价竞争以及农民因战争预期惜售，1927年秋季农民售给国家的粮食骤减为上年同期一半（西伯利亚7–12月仅完成计划三分之一）。10–12月国家购粮已陷入严重危机，中央遂于12月14日、24日连续发出紧急收购通函，转向行政施压选项。
- **阶段三：反对派绝境反击、“十周年”街头镇压与十五大彻底开除（1927.09–12.19 [N.S.]）**：在国际路线（中国革命挫败）与工业化争论受压之下，以托洛茨基、季诺维也夫、加米涅夫为核心的联合反对派编定《布尔什维克列宁主义者政纲》（`WEB-1927-09-platform-joint-opposition`，中文编年作 `09-03`）。遭政治局禁印后，反对派转入秘密油印传播，在 `09-12–13` 夜“地下印刷所案”中遭OGPU突袭并与前白卫军官线人指控捆绑。`10-23` 联席全会将托洛茨基、季诺维也夫逐出中央委员会；`11-07` 十月革命十周年庆典期间，反对派在莫斯科与列宁格勒试图打出独立口号横幅，遭党政积极分子与警力当街冲散；`11-14` 两人被开除党籍（`11-16` 阿·越飞自杀并留政治遗书）。`12-02–19` **联共（布）十五大**在购粮危机已全面显露的背景下召开，确认开除托季并另将加米涅夫等75名联合反对派骨干（及萨普龙诺夫“民主集中派”23人）开除出党；`12-10` 季诺维也夫—加米涅夫派宣布服从决议与托派分道，但 `12-18–19` 大会仍拒绝立即恢复其党籍。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-stalin` | `exploits_and_triumphs` | 1927.06–12 | 6月8日电令发动“肃清后方”搜捕，夏秋后将战备与安全危机转化为压制党内反对派的政治杠杆，在十五大确立组织压倒优势。 | `CLM-stalin-war-1927-1929-threat-and-collectivization`; `CLM-khlevniuk-2015-collective-leadership-erosion` |
| `PER-bukharin` | `allies_with_stalin` | 1927.01–12 | 年初参与预警战争风险并在政治局与斯大林联手击败联合反对派，7月曾推动缓和报刊军事宣传但收效短暂。 | `CLM-velikanova-2013-leadership-manipulation-and-self-deception`; `MTG-1927-12-15th-party-congress` |
| `PER-chicherin` | `moderates_threat` | 1927.05–06 | 在6月辞职抗议信与联席会议上指出苏联面临的是外交孤立与经济封锁而非迫在眉睫的战争，呼吁停止大规模镇压。 | `CLM-velikanova-2013-leadership-manipulation-and-self-deception`; `CLM-stalin-war-1927-1929-threat-and-collectivization` |
| `ORG-left-and-united-opposition` | `expelled` | 1927.09–12 | 在发布九月《政纲》和十周年街头抗议受挫后遭到全盘开除，随即于12月10日分裂为投降派与坚持派。 | `L3 1927-10`; `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-trotsky` | `expelled` | 1927.10–12 | 10月23日逐出中委、11月14日开除党籍，拒不悔过并在十五大后成为流放与驱逐目标。 | `MTG-1927-12-15th-party-congress`; `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-zinoviev` | `expelled -> recants` | 1927.11–12 | 与托洛茨基同日被开除党籍后于12月10日转向停止反对并认错求复籍，终致联合反对派解体。 | `L3 1927-10`; `CLM-deutscher-1959-united-opposition-defeat` |
| `PER-kamenev` | `expelled -> recants` | 1927.12 | 列入十五大新开除75人名单，在12月选择向大会决议妥协屈服以求重新入党。 | `MTG-1927-12-15th-party-congress` |
| `PER-preobrazhensky` | `implicated_in_printshop` | 1927.09–12 | 在9月“地下印刷所案”后主动出面承担《政纲》秘密印行之政治责任并遭十五大清除。 | `L3 1927-10` |
| `PER-rakovsky` | `refuses_capitulation` | 1927.12 | 十二月分裂中与拉狄克、穆拉洛夫拒绝随季诺维也夫投降，坚定维护反对派观点至被开除。 | `L3 1927-10` |
| `PER-radek` | `refuses_capitulation` | 1927.12 | 十五大前后在12月10日分化节点上坚持托派阵线（迟至1929年方才屈服）。 | `L3 1927-10` |
| `ORG-cheka-ogpu` | `conducts_mass_operation` | 1927.06–09 | 执行“六月行动”、三场间谍公审及9月地下印刷所搜捕与前白卫军官案捆绑，标志着秘密警察介入最高层党争的显著升级（此前对党内异议监控已存在）。 | `CLM-stalin-war-1927-1929-threat-and-collectivization`; `CLM-khlevniuk-2015-collective-leadership-erosion` |
| `MTG-1927-12-15th-party-congress` | `culminates_at` | 1927.12.02–19 | 十五大正式完成对联合反对派的组织清洗，并在秋冬购粮危机已发生之际通过首个五年计划编制指示与农业集体化方针。 | `MTG-1927-12-15th-party-congress`; `L3 1927-10` |
| `POL-nep` | `destabilized_by` | 1927.05–12 | 韦利卡诺娃等指出，战争恐慌引发的抢购潮与农民惜售作为超经济冲击，叠加既有工农业价格剪刀差与商品荒，剧烈动摇新经济政策市场运行。 | `CLM-velikanova-2013-war-scare-hoarding-and-grain-crisis` |
| `EVT-1928-grain-procurement-crisis` | `triggers_prelude_to` | 1927.11–1928.01 | 1927年秋季国家购粮减半（11–12月急降）后，中央于12月发出紧急通函并在1928年初选择西伯利亚“非常措施”路径。 | `CLM-velikanova-2013-war-scare-hoarding-and-grain-crisis`; `L3 1927-10` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1927年并无外国军队实际入侵苏联，但英苏断交与沃伊科夫遇刺与国内官方战争宣传、OGPU夏季大规模搜捕、城乡抢购潮相继并发；同年秋冬季，国家谷物收购较上年同期减半，而党内多数派通过中央全会与十二月十五大将联合反对派彻底逐出党组织。至于高层战争警报究竟源于真实恐惧抑或政治操控、购粮下跌在多大程度上由恐慌或定价/投资政策所致，则构成核心史学争鸣。
- **主要解释分歧**（详参 `DEB-1928-bukharin-alternative`、`DEB-1929-collectivization-and-dekulakization-causes`）：
  - **“起源于认知不安全感—夏季后常规化利用”与超经济冲击论（Olga Velikanova, 2013）**：回应托洛茨基当时指控及维奥拉（Lynne Viola）、丹尼洛夫（V. P. Danilov）等强调“高层明知无迫切战争却借机打击反对派”的操纵论。韦利卡诺娃指出，现有已见新档案（含1927年6月斯大林—莫洛托夫秘密通信）**未发现**高层不信战争将至或蓄意编造骗局清洗反对派的直接证据（尽管未见直接文件本身亦不能绝对排除策略算计，故她结合6月8日电令的仓促与无视1923年贸易/市场损失先例作综合推断）：在红军情报局（别尔津）与契切林均评估无立即开战危险的情况下，围困堡垒心态与基层败战谣言使统治者自陷焦虑；及至1927年夏既无外国干涉亦无国内暴动后，战争警报才被**常规化（routinized）**并最大限度用于粉碎党内对手与推进工业化。在经济层面，她在既有粮价偏低与工业品不足解释之外，强调春季恐慌抢购提前耗空换粮商品储备，构成加重1927–1928年购粮危机的重要“超经济因素”（参见 `CLM-velikanova-2013-leadership-manipulation-and-self-deception`、`CLM-velikanova-2013-war-scare-hoarding-and-grain-crisis`）。
  - **军事安全焦虑与战时镇压延续论（David Shearer, 2024）**：侧重安全与镇压体制连续性，主张斯大林真切担忧波兰在英国支持下干涉，6月8日电令标志着重启内战式预防性“大规模行动”；“六月行动”的20人即决处决、逾9,000人逮捕与随后将购粮短缺视作危及军粮及后方“第五纵队”直接相连，为1928–1929年强制转向铺路（参见 `CLM-stalin-war-1927-1929-threat-and-collectivization`）。
  - **组织机器压制、“可怕的寂静”与反对派自我束缚论（Isaac Deutscher, 1959）**：聚焦党内组织权力对比与社会心理，指出联合反对派仅数千活跃骨干，面对垄断报刊与人事任免的书记处机器及政治警察介入，而疲惫于内战的工人群众对派系争论保持“可怕的寂静”；反对派受制于一党制忠诚而不敢越出党外动员罢工，`11-07` 街头行动进退失据，终致溃败与分化（参见 `CLM-deutscher-1959-united-opposition-defeat`）。
  - **集体领导侵蚀与权力过渡论（Oleg Khlevniuk, 2015）**：提醒不可将1927年底直接等同于已定型的个人独裁：至1927年夏莫洛托夫信件仍反映政治局内部存在分歧表决；但斯大林借反左派斗争升级了OGPU对党内事务的介入（如9月印刷所与前白卫军官捆绑案），清除了政治局内最具竞争野心的托洛茨基与季诺维也夫——赫列夫纽克将1927年12月十五大后全会上斯大林的“策略性请辞”试探解读为其迈向个人独裁进程中的关键试金石（参见 `CLM-khlevniuk-2015-collective-leadership-erosion`）。
  - **十周年公共记忆重构论（Frederick Corney 2004，经 Velikanova 二手转引）**：认为1927年十周年庆典通过“权力戏剧”（重演攻占冬宫、受导引的回忆晚会等）将十月革命塑造成现领导层的合法性叙事，从公共记忆空间排挤反对派历史位置（参见 `CLM-corney-2004-1927-jubilee-and-opposition-erasure`；注：原书页码待补核原件）。

## 2. 一跳邻域全量微摘要目录 (去重后共 16 个节点，0 截断)
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[exploits_and_triumphs|1927.06–12]: 6月8日电令发动“肃清后方”搜捕，夏秋后将战备与安全危机转化为压制党内反对派的政治杠杆，…
- **`PER-bukharin`**（尼古拉·布哈林）: 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[allies_with_stalin|1927.01–12]: 年初参与预警战争风险并在政治局与斯大林联手击败联合反对派，7月曾推动缓和报刊军事宣传但收…
- **`PER-chicherin`**（格奥尔基·契切林）: 格奥尔基·契切林（1872–1936），沙俄贵族外交档案官出身的苏俄/苏联外交人民委员（1918–1930）。签署布列斯特和约，主导1921年英苏贸易协定与东方诸约及1922年拉帕洛条约，以欧洲均势塑造相对共产国际的二元外交；1927年战争恐慌中力阻孤立与清洗，后因病卸任。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[moderates_threat|1927.05–06]: 在6月辞职抗议信与联席会议上指出苏联面临的是外交孤立与经济封锁而非迫在眉睫的战争，呼吁停… ； `→EVT-1927-war-scare-and-opposition-expulsion`[dissenting-realist|1927.05–07]: 论证欧洲邻国并无开战意图，警告恐慌动员与处决浪潮加剧外交孤立，与军情局及李维诺夫同处审慎一侧
- **`ORG-left-and-united-opposition`**（1923–1927年左翼反对派与托季联合反对派）: 1923年剪刀差危机触发的托洛茨基—普列奥布拉任斯基“左翼反对派”，经1926年春与季诺维也夫—加米涅夫“新反对派”结盟为托季联合反对派；以《四十六人声明》与《1927年政纲》批判官僚体制与“一国社会主义”、主张价格—财政渠道的计划工业化，于1927年12月十五大被组织摧毁。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[expelled|1927.09–12]: 在发布九月《政纲》和十周年街头抗议受挫后遭到全盘开除，随即于12月10日分裂为投降派与坚…
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[expelled|1927.10–12]: 10月23日逐出中委、11月14日开除党籍，拒不悔过并在十五大后成为流放与驱逐目标。
- **`PER-zinoviev`**（格里戈里·季诺维也夫）: 老布尔什维克、共产国际首任主席（1919–1926）。1917年十月公开反对武装起义；1920年哈雷演说力推二十一条与阶级恐怖，1923年豪赌“德国十月”并首倡社民党“法西斯羽翼”论；借“三驾马车”排托后于1925年发起新反对派，1926年7月首因秘密第7条被逐出政治局，1927年底被开除后屈服。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[expelled -> recants|1927.11–12]: 与托洛茨基同日被开除党籍后于12月10日转向停止反对并认错求复籍，终致联合反对派解体。
- **`PER-kamenev`**（列夫·加米涅夫）: 老布尔什维克、首任全俄中执委主席。1917年自四月至立宪会议一贯坚守温和宪政社会主义联盟路线并公开反对十月起义；1924年十三大联手季诺维也夫压下《列宁遗嘱》，1925年十四大公开发言反斯大林“领袖”集权后失势；1928年7月密会布哈林并留下外泄笔记，反成右派致命罪证。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[expelled -> recants|1927.12]: 列入十五大新开除75人名单，在12月选择向大会决议妥协屈服以求重新入党。
- **`PER-preobrazhensky`**（叶夫根尼·普列奥布拉任斯基）: 老布尔什维克经济理论家，1920–1921年任中央书记。1923年起草《四十六人声明》批判书记等级制；1924–1926年提出社会主义原始积累，以价格税收而非行政暴力向私营部门筹资，与布哈林论战。1928–1929年误判斯大林工业化转向而脱离托派求和，1937年被处决。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[implicated_in_printshop|1927.09–12]: 在9月“地下印刷所案”后主动出面承担《政纲》秘密印行之政治责任并遭十五大清除。
- **`PER-rakovsky`**（克里斯蒂安·拉柯夫斯基）: 巴尔干国际主义者与苏维埃政治家（1873—1941）。1919—1923年任乌克兰人民委员会主席，由反对单定乌语为国语转向力捍共和国自治，1923年十二大推动“本土化”妥协。后任驻英法大使与联合反对派核心，1928年流放撰《论职业危险》剖析执政异化风险，1941年在奥廖尔被处决。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[refuses_capitulation|1927.12]: 十二月分裂中与拉狄克、穆拉洛夫拒绝随季诺维也夫投降，坚定维护反对派观点至被开除。
- **`PER-radek`**（卡尔·拉狄克）: 加利西亚犹太社会主义者与多语政论家，活动横跨波兰、德国和俄国。参与齐美尔瓦尔德左派、布列斯特争论与德国革命，后任共产国际要员，推动统一战线并卷入德国十月失败问责。作为左翼反对派及中国革命论战骨干，1927年遭开除，1929年转向妥协归队；1937年获刑，1939年狱中被害。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[refuses_capitulation|1927.12]: 十五大前后在12月10日分化节点上坚持托派阵线（迟至1929年方才屈服）。
- **`ORG-cheka-ogpu`**（全俄肃反委员会—国家政治保卫局）: 苏俄与苏联早期政治警察机关（1917–1934），由捷尔任斯基创立。历经全俄肃反委员会（ВЧК，1917–1922）、国家政治保卫局（ГПУ，1922–1923）与国家政治保卫总局（ОГПУ，1923–1934）三阶段，从法外非常机构演变为直属政治局的常设宪制部门，执行红色恐怖与强制集体化。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[conducts_mass_operation|1927.06–09]: 执行“六月行动”、三场间谍公审及9月地下印刷所搜捕与前白卫军官案捆绑，标志着秘密警察介入…
- **`MTG-1927-12-15th-party-congress`**（联共（布）第十五次代表大会）: 1927年12月2—19日莫斯科举行。大会追认11月对托洛茨基、季诺维也夫的开除党籍处分，并于12月18日另行开除加米涅夫等75名托季联合反对派骨干及萨普罗诺夫派；同时通过编制首个五年计划指示与渐进合作化—集体化决议，开启NEP末期转折前奏。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[culminates_at|1927.12.02–19]: 十五大正式完成对联合反对派的组织清洗，并在秋冬购粮危机已发生之际通过首个五年计划编制指示…
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[destabilized_by|1927.05–12]: 韦利卡诺娃等指出，战争恐慌引发的抢购潮与农民惜售作为超经济冲击，叠加既有工农业价格剪刀差…
- **`EVT-1928-grain-procurement-crisis`**（1927冬–1929年粮食收购危机）: 1927年秋冬国家收粮锐减，相对价格、工业品荒与战争恐慌共同削弱售粮意愿。1928年非常措施及随后村社摊派把交换危机转为强制征购和党内路线冲突；布哈林等反对者逐步失势，至1929年底转向全盘集体化。粮食总产、商品粮与国家采购须分开衡量。 ‖ `←EVT-1927-war-scare-and-opposition-expulsion`[triggers_prelude_to|1927.11–1928.01]: 1927年秋季国家购粮减半（11–12月急降）后，中央于12月发出紧急通函并在1928年…
- **`PER-mikoyan`**（阿纳斯塔斯·米高扬）: 亚美尼亚裔布尔什维克干部，从下诺夫哥罗德转任东南与北高加索党务，1926年任政治局候补委员、掌苏联内外贸易。1928年春夏在法制限度与妥协间摇摆，9月受斯大林施压转向强硬，成为多数派骨干；其部门联系粮食采购、城乡交换与外贸，但强征与出口并非个人或单一部门决策。 ‖ `→EVT-1927-war-scare-and-opposition-expulsion`[press-alarm-controller|1927-12]: 十五大承认战争传言的超经济影响，并受命与莫洛托夫控制报刊警报
- **`PER-yagoda`**（亨里希·雅戈达）: 苏联秘密警察组织者，1923年起任OGPU第二副主席；缅任斯基1926年任主席后因病少理日常事务，雅戈达影响渐增，职衔与实际权力须区分。其机关在战争恐慌、镇压反对派及1928–1929年控制社会中服务大转变；1934–1936年任内务人民委员，1938年公审后被处决。 ‖ `→EVT-1927-war-scare-and-opposition-expulsion`[repression-executor|1927]: 第131号指令针对被界定为农村失败主义的言论

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 3 项)
- **`DEB-1924-socialism-in-one-country`**（一国建成社会主义与不断革命论 | `historiography/debates/DEB-1924-socialism-in-one-country.md` | 流派 `stalin-bukharin, united-opposition, political-intellectual-history, institutional-geopolitics, lenin-cooperative-plan, bonapartism-and-tactical-critique`）：欧洲革命迟滞后，苏联能否凭国内力量建成社会主义，还是生产力与世界市场的联系使最终完成有赖国际革命？争论中的建设、建成和免于复辟并非同一问题；工农联盟、外部安全及党内联盟变化又如何改变这些概念的政治意义？各方均主张建设，分歧在条件、界限与国际前景。
- **`DEB-1928-bukharin-alternative`**（布哈林替代方案与新经济政策终结之争 | `historiography/debates/DEB-1928-bukharin-alternative.md` | 流派 `nep-alternative, economic-growth, structural-dilemma, apparatus, ideology-and-mobilization, cliometrics-and-archival-reassessment`）：1927至1929年粮食危机与新经济政策的瓦解，是否意味着渐进工业化和工农联盟已无可行出路，还是党内权力与政策选择扼杀了布哈林的替代方案？投资、价格、农民供粮和政治动员之间的约束究竟有多强，必须把经济可行性、政治可行性与实际权力斗争分别检验。
- **`DEB-1929-collectivization-and-dekulakization-causes`**（1929年集体化与消灭富农政策的动因之争 | `historiography/debates/DEB-1929-collectivization-and-dekulakization-causes.md` | 流派 `peasant-social-history, statistical-economic-history, archival-local-escalation, geopolitics-and-scare, industrialization-constraints, agrarian-tribute-and-policing`）：1929年集体化加速与消灭富农政策的出现，究竟源于粮食收购和工业投资的结构约束，还是统计误判、地方竞速、战争恐慌与领导层选择的叠加？农民如何应对，中央内部何时形成强制方案？应把1928年非常征粮、1929年秋冬升级与次年全面执行分开考察。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/48 条)
- **`CLM-velikanova-2013-war-scare-hoarding-and-grain-crisis`** [`SCH-velikanova-olga`(奥尔加·韦利卡诺娃) | pp. 86-88, 106-107]: 
- **`CLM-stalin-war-1927-1929-threat-and-collectivization`** [`SCH-shearer-david`(戴维·R·希勒) | pp. 18–24 (PDF pp. 25–31)]: 
- **`CLM-khlevniuk-2015-collective-leadership-erosion`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（TRYING OUT COLLECTIVE LEADERSHIP 至 THE CHOICE）。工作区文本无纸质页码。]: 
- **`CLM-velikanova-2013-leadership-manipulation-and-self-deception`** [`SCH-velikanova-olga`(奥尔加·韦利卡诺娃) | pp. 45-47, 51-55, 78-81]: 
- **`CLM-deutscher-1959-united-opposition-defeat`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | （中译本；对应第二部 1926–1927 年）]: 
- **`CLM-corney-2004-1927-jubilee-and-opposition-erasure`** [`SCH-corney-frederick`(弗雷德里克·C·科尼 · memory-and-cultural-history) | 【待规整语料；Velikanova 脚注指向 pp. 208–217】]: 
- **`CLM-bukharin-stalin-1925-one-country-internal-forces`** [`SCH-stalin-iosif`(约瑟夫·维萨里奥诺维奇·斯大林 · participant-primary-text) | 汇编 PDF pp. 38–40、85–90、113–115；《斯大林全集》页码仅按宿主转引，本卡未回核]: 
- **`CLM-trotsky-1905-december-uprising-lessons-and-permanent-revolution-defense`** [`SCH-trotsky-leon`(列夫·达维多维奇·托洛茨基 · participant-historian) | 中译书页 ·225·、·278·、·281·–·282·、·292·、·308·、·325·–·328·、·330·、·406·（1922 年俄文第 2 版系统，PDF pp. 229–410）]: 
- **`CLM-zinoviev-trotsky-1926-world-economy-critique`** [`SCH-trotsky-leon`(列夫·达维多维奇·托洛茨基 · participant-historian) | 汇编 PDF pp. 67–68、82–91；季诺维也夫引文自标 1925 年问题，托洛茨基诸段在汇编中无单行本年份与页码]: 
- **`CLM-deutscher-1959-disarmed-prophet-paradox`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | （中译本无独立纸页；对应第二部 1923 年争论章）]: 
- **`CLM-shlapentokh-bonapartism-fear-against-trotsky`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | p. 370, p. 374 (cf. The Prophet Unarmed ch21#L49-L50, ch22#L114-L175, ch27#L245-L260)]: 
- **`CLM-service-2009-trotsky-political-tactical-blunders`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本引言及第 31–32、37–38 章]: 
- **`CLM-carr-1979-stalin-synthesis-of-russian-backwardness-and-industrialism`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 74–76, 169–172, 186–191]: 
- **`CLM-carr-1976-china-1927-defeat-and-comintern-factionalism`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 345, 348-349, 356, 427-429, 490-491, 497, 620, 623, 626-627]: 
- **`CLM-sakharov-2012-lenin-cooperative-plan-debates`** [`SCH-sakharov-valentin`(瓦连京·萨哈罗夫) | EPUB Ch. 1.3 & Ch. 4.2]: 
- **`CLM-zhukov-zinoviev-1925-leningrad-opposition`** [`SCH-zhukov-yuri`(尤里·茹科夫) | EPUB OPS/ch1-20.xhtml, OPS/ch1-21.xhtml (Notes 434-462)]: 
- **`CLM-zhukov-zinoviev-comintern-and-1923-germany`** [`SCH-zhukov-yuri`(尤里·茹科夫) | EPUB OPS/ch1-16.xhtml (Notes 338-352)]: 
- **`CLM-cohen-1973-nep-viability`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 270-276, 316-320]: 
- **`CLM-cohen-1973-notes-of-an-economist`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 295-296, 318-320]: 
- **`CLM-cohen-1973-bukharin-organizational-defeat`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 287-289, 297-301, 322-329]: 
- **`CLM-erlich-1960-bukharin-balanced-growth`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 21-23 (PDF pp. 38-40)]: 
- **`CLM-erlich-1960-preobrazhensky-dilemma`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 34-36, 40-41, 49-51, 170-171 (PDF pp. 51-53, 57-58, 66-68, 185-186)]: 
- **`CLM-erlich-1960-stalin-overkill-turn`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 161-169, 172-177, 183-184 (PDF pp. 176-184, 187-192, 198-199)]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
