# 1-Hop 去重平衡上下文包：`PER-kollontai`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`PER-kollontai`** (亚历山德拉·柯伦泰 | `cards/people/PER-kollontai.md` | `multi-perspective`): 已覆盖=`workers-opposition-primary, party-institutional-daniels, gender-social-history-goldman, women-mobilization-mandel-mediated, soviet-orthodoxy-arapovich`；待补=`clements-biography-full-text, stites-womens-liberation-full-text, diplomatic-and-zhenotdel-original-archives`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 150字定性微摘要
将军家庭出身的马克思主义女工运动家，1917年支持四月提纲，十月后任国家救济人民委员。主持妇女部并倡家务社会化，1921年为工人反对派撰写纲领，批判专家治厂与官僚委任。其解放理想遭遇福利紧缩、就业隔离及党内纪律的约束；1922年转入外交，历驻挪威、墨西哥、瑞典而幸存。

## [T2] 核心脉络、关系网络与史学争鸣

### 2.1 核心历史脉络
- **将门之女走向女工运动（1872–1916）**：1872-03-19 [O.S.] / 1872-03-31 [N.S.]生于彼得堡多蒙托维奇将军家庭。脱离上层家庭生活，转向马克思主义和女工组织，长期在俄国社会民主党不同倾向间活动，不能倒写成自1903年起始终属于布尔什维克。1914年大战后坚持反战国际主义，1915年归入布尔什维克，参与国际妇女社会主义与反战宣传。
- **四月提纲、十月与女性人民委员（1917–1918）**：1917-04-04 [O.S.] / 1917-04-17 [N.S.]列宁阐述《四月提纲》时，她是最早公开支持者之一；七月事变后被捕，缺席当选中央委员。1917-10-26 [O.S.] / 1917-11-08 [N.S.]出任国家救济人民委员，通常被视为世界首位女性内阁成员；这一称谓指国家政府内阁职务，不意味着此前没有女性政治领袖。1918年作为左派共产主义者反对布列斯特和约，3月辞去人民委员职位；不能把辞去政府职务等同退出党。
- **妇女部与日常生活革命（1919–1923）**：参与党内妇女工作，1920年阿尔曼德逝世后接掌中央妇女部（Zhenotdel，至1922年）。公共食堂、洗衣房、托儿设施、母婴保护与女性工资劳动，在她的理论中是削弱家庭经济依附的物质前提；1923年《给有翼的爱神让路》把性爱、责任和同志团结相联系，不宜压成任意性关系的口号。妇女部的代表会议、教育与基层动员亦不能只当成性道德理论的附属。
- **1921年《工人反对派》：生产与主体性（1920–1921）**：她为十大撰写的纲领小册子把官僚主义界定为对群众自我活动的否定，批判“一长制”、专家特权与委任制，认为社会主义生产关系必须由工人集体通过实践创造。主张由产业工会组成全俄生产者代表大会，选举最高经济管理机关，技术专家担任参谋和执行者；移交管理权也提出准备程度与工会同意等步骤，并非简单要求立即解雇一切专家。两张站内原典论断分别锚定批判与制度方案。1921年3月十大工会票型336∶50∶18，反对派落败，纲领遭谴责，派别被勒令解散。
- **申诉、转入外交与幸存（1922–1952）**：1922年2月与施略普尼科夫等联署《二十二人声明》向共产国际申诉，十一大最终未开除她。1922年起赴挪威商务代表机构，1923年升任代表；继而驻墨西哥、再驻挪威，1930–1945年驻瑞典，1943年获大使衔。早期商务代表、全权代表与后期大使名衔不可混用。驻外和退出公开反对派活动与她幸存相伴，但“因为外交职位所以必然免于清洗”只是过强因果推断。1952-03-09 [N.S.]卒于莫斯科；后期履历作为人物结局，不回填为1929年前的解释证据。

### 2.2 核心关系网络（结构化边表）
| 目标节点 ID | 关系类型 | 有效时段 | 关系实质摘要 | 核心依据 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | ally_then_programmatic_critic | 1915–1922 | 反战与四月路线盟友，后在布列斯特、生产管理与党内纪律上分歧 | `ORG-left-communists-1918`, `MTG-1921-rcpb-10th-congress` |
| `PER-shlyapnikov` | opposition_ally | 1920–1922 | 为金属工会领袖的生产者自治诉求提供理论表述，共同向共产国际申诉 | `ORG-workers-opposition` |
| `ORG-workers-opposition` | programmatic_author | 1921–1922 | 小册子批判专家治理和官僚委任，提出经济管理与党内改革方案 | `CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists` |
| `CON-workers-control` | theorist_of_collective_self_activity | 1920–1921 | 将工人参与由监督扩展到创造社会主义生产组织，仍受一党政治框架限制 | `CLM-kollontai-1921-all-russian-congress-of-producers-program` |
| `MTG-1921-rcpb-10th-congress` | defeated_spokesperson | 1921-03 | 散发纲领并参战工会争论，生产者大会方案获18票而被拒 | `DEB-1921-trade-union-controversy-and-party-unity` |
| `POL-ban-on-factions-1921` | sanctioned_internal_dissenter | 1921–1922 | 申诉并未立即终止，但继续按纲领结社面临开除威胁 | `CLM-daniels-1960-tenth-congress-turning-point` |
| `DEB-1920s-gender-family-and-everyday-life` | central_programmatic_case | 1918–1929 | 家庭消亡与福利社会化承诺，须同NEP预算、离婚保障和就业隔离对读 | `CLM-goldman-1993-1918-family-code-and-nep-reality`, `CLM-arapovich-nep-female-employment-recovery-and-segregation` |

### 2.3 主要史学争鸣与阐释边界
- **经验事实共识**：女性人民委员、妇女部领导、反对派小册子作者和外交使节是不同阶段，不能把性别解放、工会自治、外交妥协压成单一政治立场。小册子是1921年当时介入的S级政论，并非事后回忆；其中对国家机关阶级构成的数字仍须独立核查。
- **参与者自我解放论与列宁派答辩**：柯伦泰把生产组织本身看作共产主义内容，列宁派强调贫困、技术稀缺、农民多数与党的统一。双方争的是谁有权决定过渡，不能把党大会多数直接当作全国工人民意，亦不能因她反官僚就把她等同主张多党议会制的自由主义者（工会争鸣卡）。
- **制度与性别社会史（Wendy Z. Goldman）**：家务社会化依赖真实预算、托育与就业。NEP经济核算和地方福利缩减使“自由结合”的风险重新落在妇女与子女身上；1926年事实婚姻财产保障又同农村家庭生产单位冲突。某些工业中心女性占失业者六成以上，是失业者构成，不能外推为全国女性失业率，也不能把所有家庭法条文归于柯伦泰亲笔。
- **妇女组织动员与苏联正统解释的对读**：站内RN-W28与性别争鸣卡据William M. Mandel等材料，呈现妇女代表网络及基层男干部抵制，须把组织动员与资源、实际受益分开；Richard Stites的妇女解放史是后续专门对勘方向，原著未在本轮已核馆藏中确认，不虚拟其书页或结论。N. D. Arapovich《苏联工业中的妇女劳动》（馆藏B级）倾向把政策进步归于党领导，却也保留NEP初女工被裁、1925–1929年女工份额约28%及行业、技能隔离的材料。人数回升不等于解除家庭负担，更不能拿这一后出著作证明柯伦泰任内方案已充分兑现。
- **党内制度史（Daniels）**：十大后申诉与最终退场体现禁派纪律的逐步落实；外交幸存不能反证其1921年批评虚假，也不能据此把她后来的所有沉默解释成可直接读取的私人心理。

## 2. 一跳邻域全量微摘要目录 (去重后共 6 个节点，0 截断)
- **`CON-workers-control`**（工人监督（工厂委员会与生产者自治））: 工人监督源自1905年车间行动；1917年彼得格勒工厂委员会为保就业、维持生产实行防御性监督，十月后写入《工人监督条例》。1918年起经济崩溃与国有化推动部分委员会并入工会，中央管理与劳动纪律强化；1921年生产者自治方案遭党内否决，但基层实践与合议管理并未骤然消失。 ‖ `→PER-kollontai`[theorized-proletarian-self-activity-in|1921-01–1921-03]: 撰写《工人反对派》小册子，从阶级主体性高度批判官僚委派制与资产阶级专家特权 ； `←PER-kollontai`[theorist_of_collective_self_activity|1920–1921]: 将工人参与由监督扩展到创造社会主义生产组织，仍受一党政治框架限制
- **`MTG-1921-rcpb-10th-congress`**（俄国共产党（布尔什维克）第十次代表大会）: 1921年3月8日至16日，俄共（布）十大在经济崩溃与喀琅施塔得起义交织下召开。大会决定以粮食税取代余粮收集制，开启新经济政策转向；同时终结工会大辩论，通过《关于党的统一》禁止派别活动并谴责工人反对派。经济退却与党内纪律收紧并行，会后中央与书记处改组重塑了组织权力格局。 ‖ `→PER-kollontai`[workers-opposition-theorist|1921-03]: 撰写《工人反对派》纲领批判官僚化与旧专家治厂，主张全俄生产者代表大会管理经济。 ； `←PER-kollontai`[defeated_spokesperson|1921-03]: 散发纲领并参战工会争论，生产者大会方案获18票而被拒
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←PER-kollontai`[ally_then_programmatic_critic|1915–1922]: 反战与四月路线盟友，后在布列斯特、生产管理与党内纪律上分歧
- **`PER-shlyapnikov`**（亚历山大·什利亚普尼科夫）: 金属车工出身的老布尔什维克，一战时主持北欧交通线与俄国局，1917年任首届劳动人民委员。1920—1922年领导工人反对派，主张生产者自治；十大落败后入中央，秘密处分动议又差一票未过。其反官僚诉求与维护一党政权并存，晚年回忆须与当时记录对读，1937年遇害。 ‖ `←PER-kollontai`[opposition_ally|1920–1922]: 为金属工会领袖的生产者自治诉求提供理论表述，共同向共产国际申诉 ； `→PER-kollontai`[political_ally|1920–1922]: 她撰纲领小册子，两人共同申诉；理论代言与工会组织领导互补
- **`ORG-workers-opposition`**（工人反对派）: 俄共（布）党内以产业工人和工会干部为主体的左翼反对派（1920–1922），由什利亚普尼科夫、梅德韦杰夫及理论代言人柯伦泰领导。在1920–1921年工会争论中痛斥党政官僚化与专家“一长制”，主张由“全俄生产者代表大会”及工会自治管理国民经济；1921年十大被定性为无政府工团主义倾向并遭解散。 ‖ `←PER-kollontai`[programmatic_author|1921–1922]: 小册子批判专家治理和官僚委任，提出经济管理与党内改革方案
- **`POL-ban-on-factions-1921`**（《关于党的统一》派别禁令）: 俄共十大于1921年3月16日通过《关于党的统一》，要求解散按纲领组成的派别，并保留规定渠道的批评。秘密第七条设中央领导成员的特殊处分程序；1924年1月公开宣读、1926年7月首次动用开除季诺维也夫出政治局，危机措置遂渐成约束反对派的工具，但不同年份执行不等同原条文。 ‖ `←PER-kollontai`[sanctioned_internal_dissenter|1921–1922]: 申诉并未立即终止，但继续按纲领结社面临开除威胁

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 2 项)
### `DEB-1921-trade-union-controversy-and-party-unity`：1921年工会争论、工人反对派与党内统一之争
## [T1] 核心问题定义
内战结束之际，工会应成为国家管理生产的传动机构，还是维护工人利益并参与管理的独立空间？工人反对派、托洛茨基和列宁的方案分歧，如何与第十次党代表大会禁止派别相互交织？喀琅施塔得危机既是决议援引的背景，也是有待独立考察的社会抗议，不能混同党内派别。

## [T2] 各学派立场对照矩阵
**经验基准**：核心论战发生在1920年11月至1921年3月16日十大闭幕（`era`延至1929年托姆斯基倒台及车间体制定型）。据 `DATA-04-party-membership-and-congress-votes-1903-1929`，十大694名表决代表中工会决议票型为“十人纲领” **336票**、托洛茨基—布哈林纲领 **50票**、工人反对派 **18票**（弃权2票；1月莫斯科预备会为 `57:33:21`），《关于党的统一》反对票不足30票；秘密第7条设定处分中央委员程序。喀琅施塔得决议并非工人反对派纲领。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 工人反对派 | 亚历山德拉·柯伦泰，《工人反对派》(1921) | 批评官僚和专家支配，要求由生产者代表大会组织国民经济。 | `CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists`；`CLM-kollontai-1921-all-russian-congress-of-producers-program` | 纲领是参与者政治介入，本身亦不反对排斥非共多数，不能直接代表全体工人。 |
| 列宁与“十人纲领” | 列宁与“十人纲领”（十大代表大会多数派）；Joseph Godson, *The Soviet Worker* (1981) | 工会既是“共产主义学校”与党群“传送带”，又借民主集中制、全厂单一产业工会及内部秘密党组锁死底层独立空间，否定抗议合法性。 | `CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions` | 教义与组织章程剖析偏重上层结构，对1920年代车间议价空间关注有限。 |
| 托洛茨基与劳动军事化 | Robert Service, *Trotsky: A Biography* (2009) | 托洛茨基推动劳动军事化与Tsektran，主张“工人职责是执行命令”，在专政与一党垄断上与列宁、斯大林共享更深共识。 | `CLM-service-2009-trotsky-authoritarian-consensus` | 传记解释不能替代1920—1921年中央全会逐次辩论原档，亦不否定其后民主诉求与垄断的结构悖论。 |
| 党内制度转折 | Robert V. Daniels, *The Conscience of the Revolution* (1960) | 禁派收缩组织化异议空间，但并未立即消灭一切分歧。 | `CLM-daniels-1960-tenth-congress-turning-point` | 制度后果不能等同当时所有代表预谋后来的镇压。 |
| 工会终结与家长制三方交锋 | Leonard Schapiro (1981)；Donald Filtzer (1986)；Maksim Lebsky (2021) | Schapiro 主张1920–21即已政治终结（1920-06逮捕莫斯科印刷工会、1921初捕约2,000名孟什维克、1921-05金属工会 `120:40` 否决中央名单遭强推）；Filtzer 论证RKK与车间讨价还价延至1928-12至1929-05托姆斯基免职及1929-03-06单方解雇令；Lebsky 揭示 ФУБР 75%住房与逐宿令塑造社会依附。 | `CLM-schapiro-1981-end-of-illusion-unions-1917-to-tomsky-fall`；`CLM-filtzer-1986-nep-unemployment-and-shopfloor-bargaining`；`CLM-filtzer-1986-1929-tomsky-purge-and-shock-work`；`CLM-lebsky-industrial-paternalism-origins-1917-1929` | 三方分别侧重党团压制、车间谈判与福利依附，且均受就业市场与宏观政策转轨影响。 |

### `DEB-1920s-gender-family-and-everyday-life`：1917—1929年妇女解放、家庭与日常生活之争
## [T1] 核心问题定义
革命后的法律平等、家务社会化与妇女就业承诺，为何在新经济政策下遭遇失业、照护资源匮乏和家庭财产纠纷？这种落差主要来自财政约束、父权关系与劳动市场，还是现代国家同时实施福利和规训的制度逻辑？不同地区的妇女如何回应，又有哪些经验被官方统计和男性论战遮蔽？

## [T2] 各学派立场对照矩阵
**经验基准**：1917年12月民事婚姻与离婚法令启动改革（1918年法典成文化），1920年堕胎合法化，1926年婚姻法承认事实婚姻并引发城乡财产争论；据 `DATA-08-1921-1929-nep-social-classes-unemployment-and-gender-labor`，1926年莫斯科离婚率升至 `477.1‰`，1925—1929年大工业女工占比停滞在 `28.2%–28.6%`，1926年全苏全职家政工达 `452,258` 人，1927年女性仍占登记失业者近半数，托幼与就业均受财政及市场约束。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 家庭法社会史 | Wendy Z. Goldman, Women, the State and Revolution (1993) | 家庭消亡与家务社会化理想遭遇托育萎缩（1922年全俄学前覆盖仅 `1.8%`）、女工失业与城乡家户财产冲突。 | `CLM-goldman-1993-1918-family-code-and-nep-reality`；`CLM-goldman-1993-1926-marriage-code-peasant-worker-clash` | 全国法规与中央辩论不能自动代表各省法院实践；84%未曾务工女性未入失业登记。 |
| 妇女组织与政治动员 | William M. Mandel, Soviet Women (1975)（转引 Elena D. Emelyanova 1971、Sofia N. Smidovich 1927） | 妇女部依托列宁脱产津贴令建成6万名民选妇女代表、辐射约200万城市妇女的网络，对抗基层男干部“反性别划分”抵制。 | `CLM-soviet-women-zhenotdel-mobilization-and-liquidation-1919-1930` | **亲苏左翼立场警示**：Mandel 轻信1930年官方“已完成平等任务”而撤部的说辞；组织统计亦不能推算农村覆盖率。 |
| 家庭雇佣劳动史 | Alissa Klots, Domestic Service in the Soviet Union (2024) | 驳斥托洛茨基与Goldman“全体双重负担”范式：城市白领（莫斯科雇主占 `77.8%`）与女干部将家务转嫁给 `452,258` 名农村进城家政女工，国家更补贴公职雇主 `1/3` 薪资；1926-02-08专项法降格其保障，却借 *Narpit* 工会启蒙反讽催生女仆“逃离厨房”通道。 | `CLM-klots-prisluga-to-domrabotnitsa-nep-reclassification`；`CLM-klots-communist-employers-and-gendered-labor-hierarchy`；`CLM-klots-narpit-unionization-and-1926-labor-law-paradox` | 城市有偿家政劳动与识字积极分子档案不能代表全部农村妇女及沉默大多数。 |
| 企业家长制社会背景 | Maksim Lebsky, 《苏联的工人阶级：工业家长制下的生活》(2021) | 分析全体工业工人去阶级化与半农退路（拥地率1918年 `31.3%`→1928年 `25%`），企业依托 ФУБР 基金（`75%` 建住房）与1920/1928逐宿令建立生计依附，为理解家庭再生产所处企业控制背景提供参照。 | `CLM-lebsky-industrial-paternalism-origins-1917-1929` | 该卡聚焦一般工人阶层，非专论性别托育；企业福利绑定须与家庭内部权力对读。 |
| 苏联正统工业女工史（对照基线） | Н. Д. Арапович（馆藏扉页署名）, 《苏联工业中的妇女劳动》（`publication_year: null`；B级） | 将1924年后女工回升归功于党和保护法令，但内部统计承认1925—1929年大工业女工比重锁死在 `28.2%–28.6%`、1929年金属业女工近 `3/4` 非熟练且托育不足；1929-04-15决议与高校 `≥20%` 配额仅属政策起点。 | `CLM-arapovich-nep-female-employment-recovery-and-segregation`；`CLM-arapovich-1929-skills-quotas-and-heavy-industry-mobilization` | B级正统叙事缺出版年且无1921—1928完整失业序列；指标不等于1929年底已实现实质平等。 |
| 性别教育实验与现代治理比较 | George Avis (ed.) / Lynne Attwood, The Making of the Soviet Citizen (1987)；David Hoffmann, Cultivating the Masses (2011) | Attwood 揭示克鲁普斯卡娅在1920年代推动男女童共学手工与家务的去性别化教育（1929年后遭父权逆转）；Hoffmann 将福利、卫生与规训放入欧洲现代国家治理比较。 | `CLM-soviet-citizen-lunacharsky-progressive-pedagogy-1920s`；`CLM-hoffmann-2011-soviet-socialism-as-european-modernity`；`CLM-hoffmann-2011-enlightenment-and-coercion-duality` | 教育纲领与宏观现代性比较均易模糊地方执行与不同阶层女性的具体处境。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 20/20 条)
- **`CLM-kollontai-1921-workers-opposition-critique-of-bureaucracy-and-specialists`** [`SCH-kollontai-alexandra`(亚历山德拉·柯伦泰 · participant-primary-text) | PDF pp. 2-11, 22-27]: 
- **`CLM-kollontai-1921-all-russian-congress-of-producers-program`** [`SCH-kollontai-alexandra`(亚历山德拉·柯伦泰 · participant-primary-text) | PDF pp. 11-21, 25-30]: 
- **`CLM-daniels-1960-tenth-congress-turning-point`** [`SCH-daniels-robert`(罗伯特·V·丹尼尔斯) | pp. 146-153]: Daniels：1921年十大将党统一转化为压缩合法反对空间的组织制度
- **`CLM-goldman-1993-1918-family-code-and-nep-reality`** [`SCH-goldman-wendy`(温迪·Z·戈德曼) | pp. 60–65]: 
- **`CLM-arapovich-nep-female-employment-recovery-and-segregation`** [`SCH-arapovich-n-d`(阿拉洛维茨（馆藏扉页署Н. Д. Арапович，身份待书目复核） · soviet-orthodoxy) | 馆藏中文PDF pp. 30–37；非俄文原版页码]: 
- **`CLM-goldman-1993-1926-marriage-code-peasant-worker-clash`** [`SCH-goldman-wendy`(温迪·Z·戈德曼) | pp. 242–248]: 
- **`CLM-godson-1981-tenth-congress-to-1929-transmission-belt-unions`** [`SCH-godson-joseph`(约瑟夫·戈德森 · cold-war-labor-studies) | Book pp. 106–111, 121, 128–129 [PDF pp. 118–123, 133, 140–141]]: 
- **`CLM-service-2009-trotsky-authoritarian-consensus`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本第 23–24、28–29、37 章及引言]: 
- **`CLM-schapiro-1981-end-of-illusion-unions-1917-to-tomsky-fall`** [`SCH-schapiro-leonard`(伦纳德·沙皮罗) | Book pp. 1–14 [PDF pp. 13–26]]: 
- **`CLM-filtzer-1986-nep-unemployment-and-shopfloor-bargaining`** [`SCH-filtzer-donald`(唐纳德·费尔泽) | pp. 19–29, 44–45, 77–78, 274]: 
- **`CLM-filtzer-1986-1929-tomsky-purge-and-shock-work`** [`SCH-filtzer-donald`(唐纳德·费尔泽) | pp. 22–24, 68–72, 76–82, 96–108, 274, 280–282, 287]: 
- **`CLM-lebsky-industrial-paternalism-origins-1917-1929`** [`SCH-lebsky-maksim`(马克西姆·列布斯基) | PDF pp. 9–26, 29–36, 48–49]: 
- **`CLM-soviet-women-zhenotdel-mobilization-and-liquidation-1919-1930`** [`SCH-mandel-william`(威廉·M·曼德尔 · social-history-synthesis) | PDF pp. 31, 34-47, 154-155, 218-219, 241]: 
- **`CLM-klots-prisluga-to-domrabotnitsa-nep-reclassification`** [`SCH-klots-alissa`(阿莉萨·克洛茨) | PDF pp. 12, 23–27]: 
- **`CLM-klots-communist-employers-and-gendered-labor-hierarchy`** [`SCH-klots-alissa`(阿莉萨·克洛茨) | PDF pp. 7–10, 29–36, 95, 179–180]: 
- **`CLM-klots-narpit-unionization-and-1926-labor-law-paradox`** [`SCH-klots-alissa`(阿莉萨·克洛茨) | PDF pp. 41–51, 58–69, 85–88]: 
- **`CLM-arapovich-1929-skills-quotas-and-heavy-industry-mobilization`** [`SCH-arapovich-n-d`(阿拉洛维茨（馆藏扉页署Н. Д. Арапович，身份待书目复核） · soviet-orthodoxy) | 馆藏中文PDF pp. 36–40, 47–48, 58–60, 71, 74]: 
- **`CLM-soviet-citizen-lunacharsky-progressive-pedagogy-1920s`** [`SCH-avis-george`(乔治·阿维斯（编） · education-social-history) | PDF pp. 41, 63-64, 80, 86, 94, 100-102 (原书 pp. 32, 54-55, 71, 77, 85, 91-93)]: 
- **`CLM-hoffmann-2011-soviet-socialism-as-european-modernity`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 8–10]: 
- **`CLM-hoffmann-2011-enlightenment-and-coercion-duality`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 8–9, 112, 184]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 4 条 L3 逐日细节见 `timeline/L3_daily/`)
