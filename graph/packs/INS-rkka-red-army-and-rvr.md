# 1-Hop 去重平衡上下文包：`INS-rkka-red-army-and-rvr`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`INS-rkka-red-army-and-rvr`** (工农红军与共和国革命军事委员会（РККА 与 РВСР） | `cards/institutions/INS-rkka-red-army-and-rvr.md` | `multi-perspective`): 已覆盖=`military-institutional, kakurin-strategic, mawdsley-comparative, deutscher-trotsky, service-critical, smirnov-training`；待补=`soldier-experience-micro, reform-primary-orders`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 150字定性微摘要
工农红军由1918年初志愿建军转向征兵与集中指挥；共和国革命军事委员会依靠前沙俄军事专家、政治委员及铁路内线组织内战。战后大裁军和伏龙芝改革建立正规军与地方民兵混合体制，1925至1929年伏罗希洛夫主政与干部工农化在政治控制与训练效能间形成持久张力。

## [T2] 核心脉络与史学争鸣
### 2.1 制度脉络（1918—1929）
- **建军、军事专家体制与内战动员（1918—1920）**：1918-01-15 [O.S.] / 1918-01-28 [N.S.] 人民委员会颁令组建志愿红军；德军进逼与内战爆发迫使其转向义务征兵。1918年托洛茨基取消指挥员选举，大规模吸收并征用前沙俄军事专家（военспецы），建立政委双签制并以监视与家属人质约束忠诚。**1918-09-02**（公历）共和国革命军事委员会（РВСР）正式成立（1923年8月随苏联建制更名为苏联革命军事委员会，РВС СССР），不能与1月建军混为一事。据 `DATA-05-1917-1920-factory-demographics-and-civil-war-forces` 核实序列，红军在册兵力由1918年底约70万增至1919年6月约150万（其中一线“刺刀与马刀”战斗兵力仅 **35.6万**，作战与总兵力比不足 1:4），1919年底至1920年逾300万（Mawdsley 第18章记1920年夏波兰战役时作460万）；全内战期间累计服役前沙俄军官逾 **4.8万**、前军士约 **21.5万**、1919年秋党团员“铁腰撑”约 **16万**，而1919年登记逃兵达约 **170万**。1919年3月俄共八大上，军事反对派质疑正规军与专家路线，斯大林等亦流露对占主体的农民兵员的深层戒心；列宁支持使用专家的同时强化政治监督，并于察里津冲突期间调和斯大林抗命与中央军委统辖权。
- **战后裁军与伏龙芝改革（1921—1925）**：战后大裁军剧烈压缩常备规模（具体数字口径辨析见 `[T3]`）。1924—1925年伏龙芝改革在财政约束下确立精简正规野战军与地方民兵（地域师，территориальные дивизии）混合体制。Smirnov 指出，地方部队团校学制仅 5–6 个月、1924年《内务条例》与1925年《暂行纪律条例》限制长官强制权且政治/社会工作挤占战术训练时间，造成基层指挥员长期资质赤字；同时1924年一次性清洗近700名忠实旧军官，已拉低指挥员整体学历水准。
- **伏罗希洛夫掌军与强制“工农化”（1925—1929）**：1925-01-17 中央—中监委联席全会解除托洛茨基军委主席与陆海军人民委员职务；1925-10-31 伏龙芝病逝后由 **`PER-voroshilov`** 接掌陆海军人民委员部与苏联革军委（РВС СССР）。面对农村反抗风险，1925年夏伏罗希洛夫警示农民地域师的“小资产阶级反抗危险”，1926年12月 ОГПУ 更向军委发出“地域师可能成为起义现成骨干”的正式警报，1928年10月总部遂停止继续扩编地域部队。1928年起，苏联革军委推行强制“指挥干部工农化”与阶级配额（军校80%须招收无产者与半无产者），红军工人兵员比例由 1926-04 的 18.1% 升至 1929-01 的 27.3%，代价是步骑兵军校入学门槛降至3年级、伏龙芝军事学院初等学历新生比例在 1928—1929 年间由 56.6% 飙升至 81.5%。同期参谋长 **`PER-tukhachevsky`**（1925—1928）与伏罗希洛夫围绕军备现代化与指挥权持续摩擦，并于 1928 年 11 月直言新晋指挥员缺乏连排实战技能。

### 2.2 核心关系网络（结构化边表）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-trotsky` | 缔造与统帅 | 1918.03–1925.01 | 任革军委主席并主导征兵、军事专家与政委体制，1925年被免职。 | `CLM-deutscher-1959-disarmed-prophet-paradox`; `CLM-service-2009-trotsky-authoritarian-consensus` |
| `EVT-1918-1920-russian-civil-war` | 作战载体 | 1918–1920 | 依托铁路内线与苏维埃腹地人口工业底座打赢内战。 | `CLM-mawdsley-1987-sovdepia-demographic-industrial-base`; `CLM-kakurin-1928-red-army-interior-lines-strategy` |
| `PER-stalin` | 战线抗命与政治摩擦 | 1918–1920；1925–1929 | 察里津排斥旧专家并对革军委抗命，后借反波拿巴猜忌取代托派。 | `CLM-stalin-docs-tsaritsyn-and-civil-war-command-style` |
| `PER-dzerzhinsky` | 后方保卫协同 | 1918–1920 | 契卡协同红军清剿逃兵、保障铁路运输与后方稳定。 | `CLM-mawdsley-1987-civil-war-militarized-regime` |
| `MTG-1919-03-8th-party-congress` | 军事争论定调 | 1919.03 | 军事反对派挑战专家路线，大会确认正规军与政治监督并行。 | `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` |
| `POL-war-communism` | 动员体制耦合 | 1918–1921 | 余粮征集、军工配给与部队动员形成相互锁定的军事化体制。 | `DEB-1918-war-communism-ideology-or-emergency` |
| `PER-frunze` | 体制改革 | 1924.03–1925.10 | 在财政紧缩下主导正规军与地方民兵混合改制及一长制过渡。 | `CLM-smirnov-1920s-territorial-militia-and-combat-training-deficit` |
| `PER-voroshilov` | 继任掌军 | 1925.11–1929.12 | 接任革军委主席，防范农民地域师并推行1928年干部“工农化”。 | `CLM-smirnov-red-army-commanders-vs-voenspetsy-1920s` |
| `PER-tukhachevsky` | 参谋长与建军摩擦 | 1918–1929 | 历任方面军司令及1925–1928年总参谋长，与伏罗希洛夫产生职权与训战分歧。 | `CLM-smirnov-1920s-territorial-militia-and-combat-training-deficit` |
| `POL-first-five-year-plan` | 工业化军备重塑 | 1928–1929 | 重工业五年计划与阶级配额重塑红军后勤现代化与干部构成。 | `CLM-smirnov-red-army-commanders-vs-voenspetsy-1920s` |

### 2.3 史学争鸣
- **内线战略 vs. 地缘工业底座**：Kakurin（1928）从红军内线机动与战役指挥解释内战胜利（`CLM-kakurin-1928-red-army-interior-lines-strategy`）；Evan Mawdsley（1987）则以苏维埃中心腹地约 6000 万人口、工业库存及内战政权军事化体制校准纯军事决定论（`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`、`CLM-mawdsley-1987-civil-war-militarized-regime`）。
- **托洛茨基建军角色与去职争议**：Isaac Deutscher（1952/1959）将托洛茨基视作被一党制武器解除武装的组织者，并剖析老布尔什维克用法国大革命“红色波拿巴”先例围剿红军统帅的政治心理（`CLM-deutscher-1959-disarmed-prophet-paradox`、Deutscher 1952/1959 法国革命类比论断）；Robert Service（2009）则反驳“民主派托洛茨基”叙事，指出其在就地枪决、十一抽杀、劳动军事化及镇压喀琅施塔得上与列宁—斯大林共享威权共识，且因战术失策放弃政府实权（`CLM-service-2009-trotsky-authoritarian-consensus`、`CLM-service-2009-trotsky-political-tactical-blunders`）；多尔马托夫编斯大林档案选编（2018）呈现察里津前线斯大林抗命与反专家倾向的原始电报（`CLM-stalin-docs-tsaritsyn-and-civil-war-command-style`）。
- **1920年代军制病灶**：A. A. Smirnov 依托 РГВА 档案把红军战术与指挥赤字溯源至 1918–1929 年“去军事化”条令、排斥旧专家与阶级配额（`CLM-smirnov-1920s-territorial-militia-and-combat-training-deficit`、`CLM-smirnov-red-army-commanders-vs-voenspetsy-1920s`），阅读时须注意其回溯 1941 年惨败并淡化 1937—1938 年大清洗的立场局限。士兵日常经验与原始调令全本仍待补充。

## 2. 一跳邻域全量微摘要目录 (去重后共 14 个节点，0 截断)
- **`EVT-1918-1920-russian-civil-war`**（俄国内战（1918–1920））: 1918至1920年红白主战场的内战中，布尔什维克依托中央腹地、军火遗产与铁路机动击败分散白军；征粮和恐怖又激起工农反抗。乌克兰及外高加索的民族国家竞争不能归入简单红白对决，克里米亚撤离仅标志主要白军战线收束，边疆与农民战争仍在延续。 ‖ `→INS-rkka-red-army-and-rvr`[mobilized_and_coordinated|1918—1920]: 征兵、军事专家与政委监督把人口资源转为常规军及内线调动能力 ； `←INS-rkka-red-army-and-rvr`[作战载体|1918–1920]: 依托铁路内线与苏维埃腹地人口工业底座打赢内战。
- **`EVT-1920-1921-tambov-and-peasant-revolts`**（坦波夫安东诺夫起义与1920–1921年农民绿军风暴）: 1920年坦波夫抗征粮冲突扩大为安东诺夫领导的农民战争，与其他省份起义及城市工潮共振，暴露苏维埃农村统治危机。1921年粮食税让步与重兵围剿、人质及集中营政策并行；主力在夏季受挫，零星抵抗延续，不能把新经济政策视为农村随即恢复和解。 ‖ `→INS-rkka-red-army-and-rvr`[concentrated_force|1921]: 白军主要战线收束后正规军投入国内清剿
- **`EVT-1921-kronstadt`**（喀琅施塔得水兵起义）: 1921年二月底至三月，喀琅施塔得水兵与居民以十五条决议要求改选苏维埃、开放劳动者及左翼政治自由，并成立临时革命委员会。红军跨冰夺回要塞，镇压与实物税、禁派决议交叠；经济退却早已酝酿，起义加剧其紧迫性，却未带来政治权力的开放。 ‖ `→INS-rkka-red-army-and-rvr`[military_assault|1921.03.07—18]: 正规军、军校学员与党代表参加攻岛，参战人数不等于伤亡
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←INS-rkka-red-army-and-rvr`[缔造与统帅|1918.03–1925.01]: 任革军委主席并主导征兵、军事专家与政委体制，1925年被免职。 ； `→INS-rkka-red-army-and-rvr`[architect-and-chair|1918-03–1925-01]: 强征逾4.8万旧军官与21.5万旧军士并推行政委双重签署制，借铁路内线突击建成300万正规红军，1925年1月15日和平交权
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←INS-rkka-red-army-and-rvr`[战线抗命与政治摩擦|1918–1920；1925–1929]: 察里津排斥旧专家并对革军委抗命，后借反波拿巴猜忌取代托派。
- **`PER-dzerzhinsky`**（费利克斯·捷尔任斯基）: 波兰立陶宛社民党与布尔什维克领导人。1917年建全俄肃反委员会（契卡）并续掌GPU/OGPU至逝世，奠定苏维埃安全与法外镇压体制；1924–1926年兼任最高国民经济委员会主席，力挺新经济政策市场均衡、保护技术专家并反对超工业化，1926年7月预警“红色独裁者”后猝逝于中央全会。 ‖ `←INS-rkka-red-army-and-rvr`[后方保卫协同|1918–1920]: 契卡协同红军清剿逃兵、保障铁路运输与后方稳定。
- **`MTG-1919-03-8th-party-congress`**（俄国共产党（布尔什维克）第八次代表大会）: 1919年3月18日至23日，俄共（布）八大在内战中通过第二党纲，围绕民族自决、红军正规化与党内集中化激烈争辩，提出巩固与中农的联盟。大会及会后一中全会确立政治局、组织局和书记处常设框架，否定党组织联邦制并强化党团对苏维埃的控制；军事反对派与民主集中派的抗辩凸显集权并非无争议。 ‖ `←INS-rkka-red-army-and-rvr`[军事争论定调|1919.03]: 军事反对派挑战专家路线，大会确认正规军与政治监督并行。 ； `→INS-rkka-red-army-and-rvr`[military-policy|1919-03]: 秘密会议以174:95票确认正规军与军事专家路线，同时折衷强调政委与党务监督。
- **`POL-war-communism`**（战时共产主义）: 1918年夏至1921年3月苏维埃经济政策总称：余粮收集制、中小工业国有化、取缔私商、货币贬值与实物配给并举；因内战饥荒与国家能力崩溃而强化，却在1921年喀琅施塔得与坦波夫危机下为新经济政策实物税所取代；其性质是应急、乌托邦跃进还是国家统制传统延续，史家分歧剧烈。 ‖ `←INS-rkka-red-army-and-rvr`[动员体制耦合|1918–1921]: 余粮征集、军工配给与部队动员形成相互锁定的军事化体制。
- **`PER-frunze`**（米哈伊尔·伏龙芝）: 米哈伊尔·伏龙芝（1885–1925），红军内战名将与军事改革家。1919年东线重创高尔察克、1920年南线攻克克里米亚并肃清马赫诺部；1923年十二大迫斯大林民族政策让步；1925年1月接替托洛茨基掌陆海军人民委员部，推行基干与民兵混合军改及一长制，10月手术后猝逝。 ‖ `←INS-rkka-red-army-and-rvr`[体制改革|1924.03–1925.10]: 在财政紧缩下主导正规军与地方民兵混合改制及一长制过渡。 ； `→INS-rkka-red-army-and-rvr`[chief-reformer|1924–1925]: 主持伏龙芝军事改革，奠定NEP时期基干—民兵混合制与一长制基础，同时显著削减旧军事专家比例
- **`PER-voroshilov`**（克利缅特·伏罗希洛夫）: 卢甘斯克工人布尔什维克。1918年察里津战役与斯大林结盟，抵制托洛茨基起用旧军官；1919年八大参与军事反对力量，后任第一骑兵军革军委委员。1925年11月继任苏联陆海军人民委员兼革命军事委员会主席，1926年入政治局，1928–1929年支持斯大林击败布哈林。 ‖ `←INS-rkka-red-army-and-rvr`[继任掌军|1925.11–1929.12]: 接任革军委主席，防范农民地域师并推行1928年干部“工农化”。 ； `→INS-rkka-red-army-and-rvr`[peoples_commissar_head|1925.11–1929.12]: 执掌陆海军人民委员部与苏联革军委（РВС СССР），警惕农民地域师政治风险、推进干部工农化并争取一五计划军工拨款
- **`PER-tukhachevsky`**（米哈伊尔·图哈切夫斯基）: 红军统帅、军事理论家，前近卫军少尉，历掌第5集团军与高加索方面军。1920年率西方面军攻华沙失败，与斯大林及西南方面军就利沃夫调兵和败责长期争执；1921年镇压喀琅施塔得起义，指挥坦波夫清剿重创安东诺夫主力，1925–1928年任红军参谋长。 ‖ `←INS-rkka-red-army-and-rvr`[参谋长与建军摩擦|1918–1929]: 历任方面军司令及1925–1928年总参谋长，与伏罗希洛夫产生职权与训战分歧。 ； `→INS-rkka-red-army-and-rvr`[front-commander-and-strategist|1918-1929]: 统率红军东线与高加索战线获胜，1920年夏指挥西方面军进攻华沙受挫并与斯大林结怨，1921年主持镇压喀琅施塔得与坦波夫起义。
- **`POL-first-five-year-plan`**（第一个五年计划）: 苏联首部正式工业化纲领，1928–1929年在起点与最高方案争论中定案。1929-04-16至23日中央联席全会、04-23至29日十六次党代表会议及05-20至28日全苏苏维埃五大批准最高方案；下半年投资、钢铁与集体农庄指标加码，冲垮布哈林均衡路线，与NEP退场、强制集体化并进。 ‖ `←INS-rkka-red-army-and-rvr`[工业化军备重塑|1928–1929]: 重工业五年计划与阶级配额重塑红军后勤现代化与干部构成。
- **`EVT-1918-03-brest-litovsk-treaty`**（1918年布列斯特-里托夫斯克和约危机与签约）: 1917年12月停战至1918年3月签约，列宁主和、托洛茨基“不战不和”与布哈林革命战争路线交锋。德军进逼后，中央2月23日以7赞成、4反对、4弃权接受最后通牒；和约保存政权，也加深党内裂痕并促使左翼社革党退阁。 ‖ `←INS-rkka-red-army-and-rvr`[enabled_survival|1918.03]: 退出大战释放机动兵力投入内战。
- **`ORG-workers-opposition`**（工人反对派）: 俄共（布）党内以产业工人和工会干部为主体的左翼反对派（1920–1922），由什利亚普尼科夫、梅德韦杰夫及理论代言人柯伦泰领导。在1920–1921年工会争论中痛斥党政官僚化与专家“一长制”，主张由“全俄生产者代表大会”及工会自治管理国民经济；1921年十大被定性为无政府工团主义倾向并遭解散。 ‖ `←INS-rkka-red-army-and-rvr`[criticized|1920–1921]: 工人反对派批评工会军事化与官僚指挥。

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 2 项)
### `DEB-1918-red-terror-and-civil-war-origins`：红色恐怖、契卡扩张与内战期一党专政起源之争（1918–1921）
## [T1] 核心问题定义
红色恐怖和契卡法外权力是列宁主义政治逻辑的必然结果，还是内战、粮食危机、联盟破裂与地方暴力交织下的制度选择？中央命令与地方自主行动怎样互相强化？恐怖升级、社会主义对手遭镇压和一党统治形成各有不同时间线，不能压缩成同一事件。

## [T2] 各学派立场对照矩阵
**经验基准**：全俄肃反委员会（契卡）于1917-12-07 [O.S.] / 1917-12-20 [N.S.] 凭人民委员会非立法决议成立；1918年3月《布列斯特和约》后左翼社革党退出人民委员会，7月4–10日第五次全俄苏维埃代表大会期间爆发7月6日刺杀德国大使米尔巴赫事件，布尔什维克与左翼社革党彻底决裂并于7月10日通过1918年苏俄宪法；8月30日乌里茨基遇刺、列宁遇刺重伤。据站内入库S级档案校勘（`sources/web-archive/E06_E09_state_and_comintern/1918-09-05_decree-on-red-terror.md`），广泛扣押人质指令首先出自9月4日内务人民委员彼得罗夫斯基电令，而9月5日人民委员会《关于红色恐怖的决议》（RGASPI打印原件由司法人民委员库尔斯基、内务人民委员彼得罗夫斯基、办公厅主任邦奇-布鲁耶维奇与秘书福季耶娃签署，**并非捷尔任斯基签署，且9月5日决议正文中并未出现“人质”一词**）将集中营隔离与就地枪决正式法制化。跨口径处决统计（`DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge`）须严格区分中央登记案卷与地方未登记法外处决。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 自由主义意识形态连续论 | Richard Pipes, *The Russian Revolution* (1990) | 提出“法国大革命终结于恐怖，而俄国革命始于恐怖”：布尔什维克因缺乏多数民众授权，将系统性恐怖用作“民众支持的替代品”，阶级敌人话语与列宁的雅各宾法律观使红色恐怖成为十月少数派政变的必然逻辑延伸。 | `CLM-pipes-1990-red-terror-leninist-logic` | 将1918年夏内战升级与暗杀危机前后的制度突变全部还原为先验意识形态蓝图，低估了战时生存危机与基层压力。 |
| 契卡制度史与法外基因论 | George Leggett, *The Cheka: Lenin's Political Police* (1981) | 追踪契卡从1917年12月仅具侦查权、凭人民委员会行政决议（类比沙皇尼古拉一世第三厅）建置，在1918年春夏突破司法人民委员部（斯泰因伯格）制约、借9月红色恐怖法令将法外处决权制度化，直至1922年改组为GPU并由列宁5月致库尔斯基密信将恐怖写入刑法典的制度连续性（估算1917–1922年契卡直接处决约14万人、镇压起义另致约14万人死亡）。 | `CLM-leggett-1981-vecheka-extra-legal-origins`；`CLM-leggett-1981-red-terror-institutionalization`；`CLM-leggett-1981-cheka-to-gpu-continuity` | 1981年尚未能利用后苏联解密的FSB中央与地方卷宗，其高层估算数字需与莫佐欣、泽姆斯科夫档案统计对勘。 |
| 联盟破裂、党组织萎缩与专政偶然论 | Alexander Rabinowitch, *The Bolsheviks in Power: The First Year of Soviet Rule in Petrograd* (2007) | 论证一党专政与大规模恐怖并非十月既定方案：1918年春彼得格勒布尔什维克党员从约5万人骤降至约6,000人，为保住苏维埃五大多数竟伪造约399席代表资格；左翼社革党7月刺杀米尔巴赫旨在逼停布列斯特和约而非推翻苏维埃（**1918年12月彼得格勒契卡甚至秘密撤销了对左翼社革党“有组织武装起义”的指控**）；8月30日乌里茨基遇刺后，彼得格勒各区委“自下而上”施压扩大报复，与中央危机共振催生红色恐怖。 | `CLM-rabinowitch-2007-contingency-of-dictatorship`；`CLM-rabinowitch-2007-left-sr-coalition-collapse` | 彼得格勒在季诺维也夫与乌里茨基初期相对克制及随后失控的个案，不能直接代表伏尔加河或南方前线各省的暴力烈度。 |
| 地方庇护网络、红色恐怖编年史与捷尔任斯基机构化 | Delano Dugarm (2001，收入 Donald J. Raleigh 编 *Provincial Landscapes*)；Igor Ratkovsky (伊·谢·拉特科夫斯基 2017两部专著，依托 A. M. & A. A. Plekhanov 2007 档案集) | Dugarm以坦波夫省个案揭示地方布尔什维克宗派庇护网、溃兵与契卡自主滥权常偏离莫斯科指令，甚至以“虚构暴动”掩盖征粮失败；圣彼得堡国立大学史家拉特科夫斯基（2017《契卡红色恐怖编年史》与《捷尔任斯基传》）依托普列汉诺夫父子2007年档案集，重构人质制度、地方契卡对孟什维克与社革党的压制、1918年秋约8,000人处决估算，以及捷尔任斯基如何将分散的革命暴力收编为垂直集权的契卡—内务—最高国民经济委员会官僚机器。 | `CLM-raleigh-2001-local-bolshevik-violence-and-clientelism`；`CLM-cheka-chronicle-hostage-and-local-autonomy`；`CLM-cheka-chronicle-suppression-of-socialist-rivals`；`CLM-plekhanov-am-dzerzhinsky-cheka-institutionalization` | 地方报刊编年史与契卡内部通报存在漏报或战绩夸大双向偏差，须与独立受害者名册及省级法院档案交叉核验。 |
| 被镇压社会主义对手、第三势力崩溃与1918年工人抗议 | [S级当事人演说] L. Martov (1920年10月哈勒大会演说)；Oliver H. Radkey, *The Sickle under the Hammer* (1963)；D. O. Churakov (丘拉科夫, 2004) | 马尔托夫在1920年德国独立社民党哈勒大会上痛斥无差别红色恐怖（如彼得格勒一次处决约800人）与“二十一条”如何摧毁社会主义道德与苏维埃民主；Radkey剖析社革党与科穆奇（Komuch）“民主第三势力”因内部分裂及白军借其作“保护色”而崩溃，将政局推入红白恐怖两极；丘拉科夫以档案证明1918年苏维埃辖区210–220家大中型企业爆发10–25万工人罢工抗议，直至8月伊热夫斯克—沃特金斯克武装工人起义，直接证伪“镇压对象仅限于资产阶级和地主”的官方叙事。 | `CLM-halle-1920-martov-critique-of-terror-and-21-conditions`；`CLM-smith-scott-2011-psr-third-force-collapse`；`CLM-churakov-2004-soviet-worker-protest-dynamics-1918`；`CLM-churakov-2004-izhevsk-votkinsk-worker-insurrection` | 反对派控诉与工人起义证明了恐怖对劳动阶级自身的反噬，但对白军战区白色恐怖与外国干涉的对称比较需另行展开。 |
| 内战军事化结构与总体战现代治理 | Evan Mawdsley, *The Russian Civil War* (1987); David L. Hoffmann, *Cultivating the Masses* (2011) | Mawdsley从军事地理与政权生存结构出发，指出内战与政治高度军事化均是十月夺权方式的直接代价（“内战代价即革命代价”）；Hoffmann将契卡监控、集中营与粮食强制置于1914年一战以来欧洲列强总体战人口治理与国家暴力技术的连续谱中。 | `CLM-mawdsley-1987-civil-war-militarized-regime`；`CLM-hoffmann-2011-continuum-of-total-war-1914-1929` | 欧洲总体战技术共性或军事地理决定论，不能消解布尔什维克在1921年内战结束后仍保留并制度化法外警察权力的政治选择责任。 |
| 后苏联FSB/GARF档案定量校准与莫佐欣“战时/和平期二分法” | O. B. Mozokhin (莫佐欣, 2006/2016)；V. N. Zemskov (泽姆斯科夫, 2010s) | 莫佐欣据俄罗斯联邦安全局中央档案馆（ЦА ФСБ РФ）统计表（`DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge`），确认1918–1921年有案可查契卡处决约1.75万人（计入缺省全期上限不超过5万），并提出鲜明的**国家主义二分法**——肯定1918–1921年战时契卡镇压武装叛乱的应急必要性，却**尖锐批判1922年后和平时期GPU/OGPU继续垄断法外司法**（如1924年4,097起反革命案仅6起移交法院，战时死刑率6.9% vs 和平期0.5%/0.94%）；泽姆斯科夫据GARF档案校准1918–1920年登记反革命案判刑62,231人、处决25,709人（含未登记上限<10万），共同驳斥百万级夸大数字。 | `CLM-mozokhin-cheka-to-ogpu-extrajudicial-jurisdiction-1918-1929`；`CLM-zemskov-1920s-archival-repression-scale-before-1930` | 中央汇总报表未涵盖1918–1920年前线红军革命军事法庭、征粮队及地方县契卡未上报的就地处决，档案下限不等于实际死亡总数。 |

### `DEB-1918-war-communism-ideology-or-emergency`：战时共产主义与早期一党制本质之争：内战应急、乌托邦跃进还是国家统制连续？
## [T1] 核心问题定义
1918至1921年的全面国有化、余粮收集制、取缔私商、劳动军事化，以及多党苏维埃收为一党专政，究竟是内战与供给崩溃逼出的生存应急，还是反市场乌托邦的激进兑现，抑或一战以来国家统制与基层危机交互的结果？“战时共产主义”是1921年转向时的事后标签，须分清措施序列与事后总结。

## [T2] 各学派立场对照矩阵

**经验共识**：1917年底至1918年春尚存布尔什维克—左翼社革党联合执政与“国家资本主义”探索；1918年夏起全面国有化与强制征粮随内战升级扩展；1920年达至劳动军事化与无货币幻想顶峰；1921年3月俄共十大在农村起义与喀琅施塔得危机下转向实物税（NEP）与党内派别禁令。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **内战军事应急与双元矛盾论** | E. H. Carr, *The Bolshevik Revolution*, Vol. 2 (1952); Evan Mawdsley, *The Russian Civil War* (1987) | 强调工业瓦解、封锁与300万红军补给迫使政权诉诸垂直“总局主义”与强制征粮；但Carr同时指出1920年后期确曾滋生把战时自然经济奉为直接通往共产主义捷径的意识形态幻象。 | `CLM-carr-1952-war-communism-internal-contradictions`; `CLM-mawdsley-1987-civil-war-militarized-regime`; `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` | 单靠军事紧急状态难以完全解释1920年底内战大局已定后为何仍出台小手工业全面国有化令。 |
| **意识形态乌托邦与废法专政论** | Martin Malia, *The Soviet Tragedy* (1994); Richard Pipes, *The Russian Revolution* (1990) | 认为消灭私有产权与市场交换本就是马克思主义核心诉求，内战只是扫除了渐进障碍、催化乌托邦跃进；Pipes强调契卡与排斥反对派早于大规模内战爆发。 | `CLM-pipes-1990-red-terror-leninist-logic`; `CLM-pipes-1990-october-classic-coup` | 易将不同阶段的应急妥协（如1918春列宁国家资本主义方案）回溯拉平为单一既定时间表。 |
| **战时国家统制连续与自下而上倒逼论** | Lars T. Lih; S. A. Smith, *Red Petrograd* (1983); David Hoffmann (2011) | 揭示沙皇与临时政府在一战中已启动粮食专卖与国家统制；Smith证明1917–1918春77%早期企业没收源自基层工厂委员会应对关厂危机的自下而上压力，而非中央乌托邦指令。 | `CLM-smith-sa-1983-defensive-workers-control`; `CLM-smith-sa-1983-from-workers-control-to-nationalization`; `CLM-hoffmann-2011-continuum-of-total-war-1914-1929` | 总体战技术连续性不能替代对布尔什维克消灭整个有产阶级政治权利之独特意识形态动力的解释。 |
| **复合危机、党内张力与农村社会钳制论** | Alexander Rabinowitch (2007); Robert V. Daniels (1960); Moshe Lewin (1968/1985) | 追踪布列斯特和约、左翼社革党决裂及左翼共产主义者/工人反对派论战如何一步步锁死多党与党内多元空间，同时揭示小农汪洋的反抗最终迫使政权在1921年退却但保留了战时强制记忆。 | `CLM-rabinowitch-2007-contingency-of-dictatorship`; `CLM-daniels-1960-left-communists-1918`; `CLM-figes-1996-peasant-wars-and-nep-retreat`; `CLM-zemskov-1929-dekulakization-demographic-baseline` | 首都与萨拉托夫、坦波夫、乌拉尔等外省的时间差与暴力烈度须结合地方档案（Raleigh、Churakov）细化。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/36 条)
- **`CLM-deutscher-1959-disarmed-prophet-paradox`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | （中译本无独立纸页；对应第二部 1923 年争论章）]: 
- **`CLM-service-2009-trotsky-authoritarian-consensus`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本第 23–24、28–29、37 章及引言]: 
- **`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 56–58, 69, 185–188, 217–218, 283–284]: 
- **`CLM-kakurin-1928-red-army-interior-lines-strategy`** [`SCH-kakurin-nikolai`(尼古拉·叶夫根尼耶维奇·卡库林) | pp. xvi–xviii, 91–93, 101–103, 198–203, 210–229]: 
- **`CLM-stalin-docs-tsaritsyn-and-civil-war-command-style`** [`SCH-dolmatov-vladimir`(弗拉基米尔·多尔马托夫（编） · archival-documentary-edition)]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-smirnov-1920s-territorial-militia-and-combat-training-deficit`** [`SCH-smirnov-andrei`(安德烈·阿纳托利耶维奇·斯米尔诺夫) | pp. 102, 761-764, 779-783, 792-794, 817]: 
- **`CLM-smirnov-red-army-commanders-vs-voenspetsy-1920s`** [`SCH-smirnov-andrei`(安德烈·阿纳托利耶维奇·斯米尔诺夫) | pp. 628-634, 670-672, 680-694]: 
- **`CLM-service-2009-trotsky-political-tactical-blunders`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本引言及第 31–32、37–38 章]: 
- **`CLM-shlapentokh-bonapartism-fear-against-trotsky`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | p. 370, p. 374 (cf. The Prophet Unarmed ch21#L49-L50, ch22#L114-L175, ch27#L245-L260)]: 
- **`CLM-stalin-war-1920-polish-war-lessons`** [`SCH-shearer-david`(戴维·R·希勒) | pp. 4, 11–15 (PDF pp. 11, 17–22)]: 
- **`CLM-avrich-1970-white-plot-refutation`** [`SCH-avrich-paul`(保罗·阿夫里奇) | pp. 143-147, 816-818]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-leggett-1981-vecheka-extra-legal-origins`** [`SCH-leggett-george`(乔治·莱格特) | pp. 17-22, 47-49 (PDF pp. 55-60, 85-87)]: 
- **`CLM-leggett-1981-red-terror-institutionalization`** [`SCH-leggett-george`(乔治·莱格特) | pp. 56-59, 102-115, 144-145 (PDF pp. 94-97, 140-153, 182-183)]: 
- **`CLM-leggett-1981-cheka-to-gpu-continuity`** [`SCH-leggett-george`(乔治·莱格特) | pp. 339-352, 355-363 (PDF pp. 377-390, 393-401)]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-rabinowitch-2007-left-sr-coalition-collapse`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 274-282, 287-309, 395-396]: 
- **`CLM-raleigh-2001-local-bolshevik-violence-and-clientelism`** [`SCH-raleigh-donald`(唐纳德·J·罗利) | Local PDF pp. 104, 112–130; English print pagination not verified]: 
- **`CLM-cheka-chronicle-hostage-and-local-autonomy`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | EPUB OPS/ch1-6.xhtml; OPS/ch1-10.xhtml; OPS/ch1-14.xhtml; OPS/ch1-15.xhtml; OPS/ch1-16.xhtml; OPS/ch1-19.xhtml（提取文本无印刷页码）]: 
- **`CLM-cheka-chronicle-suppression-of-socialist-rivals`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | EPUB OPS/ch1-4.xhtml; OPS/ch1-5.xhtml; OPS/ch1-9.xhtml; OPS/ch1-10.xhtml; OPS/ch1-15.xhtml; OPS/ch1-16.xhtml（提取文本无印刷页码）]: 
- **`CLM-plekhanov-am-dzerzhinsky-cheka-institutionalization`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | pp. 55-56, 97-106, 118-123, 147-155, 209-211, 228]: 
- **`CLM-halle-1920-martov-critique-of-terror-and-21-conditions`** [`SCH-martov-iulii`(尤利·奥西波维奇·马尔托夫 · participant-primary-text) | pp. 167–170, 173, 175–176, 179 (Lih translation in the 2011 Lewis/Lih edition; printed page = PDF page − 1). Full speech pp. 167–179, delivered 15 October 1920 [N.S.]]: 
- **`CLM-smith-scott-2011-psr-third-force-collapse`** [`SCH-radkey-oliver`(奥利弗·亨利·拉德基) | pp. 452-455, 467-473, 490-493 (PDF pp. 468-471, 483-489, 506-509)]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条，另有 5 条 L3 逐日细节见 `timeline/L3_daily/`)
