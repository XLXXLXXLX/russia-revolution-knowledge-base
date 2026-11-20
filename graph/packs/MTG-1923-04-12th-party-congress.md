# 1-Hop 去重平衡上下文包：`MTG-1923-04-12th-party-congress`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`MTG-1923-04-12th-party-congress`** (俄国共产党（布尔什维克）第十二次代表大会 | `cards/meetings/MTG-1923-04-12th-party-congress.md` | `multi-perspective`): 已覆盖=`revisionist-lewin, nationalities-archival-smith, economic-interregnum-carr, party-opposition-trotsky`；待补=`full-stenogram-economic-commission`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1923年4月17—25日莫斯科举行。列宁第三次中风后首次缺席党代会，代表团分组秘密传达其民族问题笔记；托洛茨基以“剪刀差”图主张计划化工业化；民族问题特别会议迫使斯大林退让并确立本土化妥协决议，但会后人事布局仍背离列宁清算官僚沙文主义的初衷。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **开幕背景、列宁缺席与民族笔记秘密传达（`1923-04-17` 起）**：`1923-03` 第三次中风使列宁失语缺席，十二大成为其生前最后一次受其口述文稿间接震慑的党代会。会前 `1923-04-16` 福季耶娃致函加米涅夫披露列宁托付托洛茨基捍卫格鲁吉亚共产党人之意，政治局遂决定仅在各代表团闭门分组会上宣读列宁《关于民族或“自治化”问题》笔记而不列入全会公开报告，化解了针对斯大林、奥尔忠尼启则、捷尔任斯基（*dzerzhimordy*）的直接政治清算（`CLM-lewin-1968-georgian-affair-bureaucracy`, `DEB-1923-nationality-and-empire`）。
- **经济与“剪刀差”辩论（四月全会场）**：托洛茨基在工业报告中展示工农业价格指数分歧图，论证流通危机源于交换条件失衡，呼吁强化国家计划委员会（Gosplan）统筹职能与工业合理化（`CLM-carr-1954-scissors-crisis-mechanics`）。多数派（季诺维也夫主作政治报告、斯大林掌控组织报告）排斥赋予计委超部委指令权；会后 `1923-08` 末国家银行收缩工业信贷成为合拢剪刀的关键杠杆。
- **民族问题特别分组会议与本土化决议（截至 `1923-04-25`）**：斯大林提交民族政策论纲，在特别会议解密速记中遭拉柯夫斯基、伏龙芝、姆迪瓦尼、马哈拉泽及中亚、鞑靼、克里米亚代表围攻，被迫接受提高民族院立法地位、法定保障本土语言、承诺边疆工业化并以反大俄罗斯沙文主义为主调等修正案，制度化奠定 **本土化（korenizatsiia）** 框架（`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`）。但闭幕后不久苏丹-加利耶夫案标示：民族让步以严守党中央组织垄断为刚性红线。
- **组织与派别余波**：季诺维也夫—加米涅夫—斯大林“三驾马车”借大会扩大中央委员会与工农检查院—中监委编制、巩固书记处干部调配权；奥尔忠尼启则执掌党国监察机器、捷尔任斯基继掌最高国民经济委员会、斯大林稳居总书记（`CLM-lewin-1968-georgian-affair-bureaucracy`）。托洛茨基在格鲁吉亚问题上避让妥协，`1923-10`“四十六人声明”反对派危机待半年后剪刀差达峰时方全面爆发。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-lenin` | `absent-influence` | 1923-04 | 病重失语缺席，其格鲁吉亚—民族问题口述笔记仅在代表团闭门传达而未能触发人事清算 | `CLM-lewin-1968-georgian-affair-bureaucracy`; `DEB-1922-lenin-testament-and-stalin-rise` |
| `PER-trotsky` | `reports-scissors-crisis` | 1923-04 | 以价格剪刀图主张工业计划化与流通改革，但在格鲁吉亚议题上对“三驾马车”妥协 | `CLM-carr-1954-scissors-crisis-mechanics`; `CLM-lewin-1968-georgian-affair-bureaucracy` |
| `PER-stalin` | `reports-nations-then-retreats` | 1923-04 | 民族论纲在特别会议遭边疆代表围攻后作条文让步，同时稳固书记处与扩编中委优势 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`; `CLM-lewin-1968-georgian-affair-bureaucracy` |
| `EVT-1922-georgian-affair-and-ussr-formation` | `addressed-behind-closed-doors` | 1923-04 | 格鲁吉亚冲突卷宗与列宁笔记促成反大俄罗斯沙文主义条文，但涉事中央大员未受处分 | `CLM-lewin-1968-georgian-affair-bureaucracy`; `CLM-smith-jeremy-1999-georgian-affair-reassessed` |
| `POL-korenizatsiia` | `institutionalized-at` | 1923-04起 | 民族问题决议将干部与语言本土化写入苏联早期联邦运作框架 | `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` |
| `POL-nep` | `economic-context` | 1923 | 新经济政策剪刀差流通危机在大会公开化，行政调节与后续信贷杠杆并行 | `CLM-carr-1954-scissors-crisis-mechanics` |

### 2.3 史学争鸣光谱
- **经验共识**：十二大是列宁在世但首次缺席的党代会；列宁民族问题笔记未公开宣读于大会全会而限于代表团闭门传达；托洛茨基公开报告剪刀差；民族问题特别会议通过大幅修正斯大林原提纲的本土化决议。
- **主要解释分歧**（详参 `DEB-1923-nationality-and-empire`, `DEB-1922-lenin-testament-and-stalin-rise`）：
  - **[列宁晚期反官僚斗争论 / Moshe Lewin]**（`CLM-lewin-1968-georgian-affair-bureaucracy`）：强调民族与格鲁吉亚危机是列宁察觉最高层权力蜕变与大俄罗斯官僚机器合流的唯一实质切口；十二大后奥尔忠尼启则、捷尔任斯基、斯大林不仅未被清算反而分掌监察、经济与党务中枢，凸显列宁晚期意图与历史结果间的“巨大鸿沟”。
  - **[解密档案民族妥协论 / Jeremy D. Smith]**（`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`）：依据1991年后解密的民族问题特别会议速记，驳斥“十二大=斯大林彻底胜利”旧说，论证少数民族与边疆代表迫使中央实质退让，开启1920年代本土化稳固期。
  - **[过渡时期经济史 / E. H. Carr]**（`CLM-carr-1954-scissors-crisis-mechanics`）：指出十二大虽聚焦剪刀差，但真正促成1923年底比价合拢的杠杆是会后8月末国家银行信贷紧缩而非大会决议条文本身。
  - **[自由主义极权连续论 / Richard Pipes]**（经 Smith 引述对勘）：将十二大定性为行政中央集权对地方自治的一边倒胜利，与特别会议解密速记存在明显张力。

## 2. 一跳邻域全量微摘要目录 (去重后共 10 个节点，0 截断)
- **`INS-rabkrin-and-ccc`**（中央监察委员会与工农检查人民委员部（联合工作体制））: 工农检查人民委员部是国家监察机关，中监委是党的纪律监督机关。1923年改组后共同领导、联合办公，仍为两个机构，未在法律上合并；列宁的合并设想及Carr、Lewin的叙述用语须与此区分。改革旨在改善官僚机器、维护中央团结，联合机构随后参与党内审查处分，监督亦受权力关系制约。 ‖ `→MTG-1923-04-12th-party-congress`[implemented_reorganization|1923.04]: 扩大中央委员会与中监委，建立 CCC–RKI 共同领导
- **`MTG-1922-03-11th-party-congress`**（俄国共产党（布尔什维克）第十一次代表大会（1922年））: 1922-03-27至04-02[N.S.]，俄共十一大在莫斯科召开，为列宁最后出席的党代会。他宣布NEP退却结束，强调管理、文化与官僚主义；大会警告工人反对派。04-03新中央全会设总书记并选出斯大林，04-04《真理报》公布；任命、公布均须与大会决定区分。 ‖ `→MTG-1923-04-12th-party-congress`[successor_congress|1923年4月]: 后继党代会，沿同一书记处—中监委框架推进组织改革。
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←MTG-1923-04-12th-party-congress`[absent-influence|1923-04]: 病重失语缺席，其格鲁吉亚—民族问题口述笔记仅在代表团闭门传达而未能触发人事清算
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←MTG-1923-04-12th-party-congress`[reports-scissors-crisis|1923-04]: 以价格剪刀图主张工业计划化与流通改革，但在格鲁吉亚议题上对“三驾马车”妥协
- **`PER-stalin`**（约瑟夫·斯大林）: 布尔什维克高加索地下组织者、民族事务人民委员（1917–1923）及中央总书记（1922起）。依托书记处任命权与安全危机叙事，先联季-加压制托洛茨基，再联布哈林击溃联合反对派；1927–1929年以战备恐慌与“自上而下革命”击败布哈林集团，1929年12月拍板“把富农作为阶级消灭”并终结新经济政策。 ‖ `←MTG-1923-04-12th-party-congress`[reports-nations-then-retreats|1923-04]: 民族论纲在特别会议遭边疆代表围攻后作条文让步，同时稳固书记处与扩编中委优势
- **`EVT-1922-georgian-affair-and-ussr-formation`**（格鲁吉亚事件、自治化之争与苏联成立）: 1921年红军进入格鲁吉亚后，地方共产党领导人与高加索局就外高加索联邦化激烈冲突。1922年斯大林主张各共和国自治化并入苏俄，列宁提出共和国平等组成新联盟；`1922-12-30` 首届全联盟苏维埃代表大会通过建盟宣言和条约。形式平等、党的集中领导与地区权力实际分配之间的张力并未消失。 ‖ `←MTG-1923-04-12th-party-congress`[addressed-behind-closed-doors|1923-04]: 格鲁吉亚冲突卷宗与列宁笔记促成反大俄罗斯沙文主义条文，但涉事中央大员未受处分
- **`POL-korenizatsiia`**（本土化政策（Коренизация））: 1923年俄共十二大系统确立的民族政策，在一党垄断与组织集权下推进非俄干部录用、行政司法母语化和民族文教。斯大林在语言、边疆发展及第二院否决权上让步，守住代表结构；乌克兰等地深入推行，1926、1928年引发文化经济自主争论。1929年底只是本卡观察截点，并非政策废止。 ‖ `←MTG-1923-04-12th-party-congress`[institutionalized-at|1923-04起]: 民族问题决议将干部与语言本土化写入苏联早期联邦运作框架 ； `→MTG-1923-04-12th-party-congress`[institutionalized-at|1923-04]: 十二大民族问题决议将语言保障与民族干部培养写入联盟早期建构纲领，但条文承诺不等于行政权限全盘下放
- **`POL-nep`**（新经济政策）: 1921年春在农村起义、城市工潮与喀琅施塔得危机倒逼下逐步确立、取代战时共产主义的混合经济体制。以固定实物税（后改货币税）取代余粮收集制，渐次放开城乡市场与小私营商业（耐普曼），由国家掌控大工业、银行、运输与外贸“制高点”；1928–1929年在收购危机与政治转向中逐步瓦解。 ‖ `←MTG-1923-04-12th-party-congress`[economic-context|1923]: 新经济政策剪刀差流通危机在大会公开化，行政调节与后续信贷杠杆并行
- **`PER-rakovsky`**（克里斯蒂安·拉柯夫斯基）: 巴尔干国际主义者与苏维埃政治家（1873—1941）。1919—1923年任乌克兰人民委员会主席，由反对单定乌语为国语转向力捍共和国自治，1923年十二大推动“本土化”妥协。后任驻英法大使与联合反对派核心，1928年流放撰《论职业危险》剖析执政异化风险，1941年在奥廖尔被处决。 ‖ `→MTG-1923-04-12th-party-congress`[anti-centralist-challenger|1923-04]: 在全会与04-25特别会议谴责大俄罗斯机关“掠夺共和国财富”，主张剥夺联盟人民委员部十分之九权力
- **`PER-frunze`**（米哈伊尔·伏龙芝）: 米哈伊尔·伏龙芝（1885–1925），红军内战名将与军事改革家。1919年东线重创高尔察克、1920年南线攻克克里米亚并肃清马赫诺部；1923年十二大迫斯大林民族政策让步；1925年1月接替托洛茨基掌陆海军人民委员部，推行基干与民兵混合军改及一长制，10月手术后猝逝。 ‖ `→MTG-1923-04-12th-party-congress`[co-forced-compromise|1923-04]: 民族特别会议上代表乌克兰—边疆利益迫斯大林让步

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 3 项)
- **`DEB-1923-nationality-and-empire`**（布尔什维克民族政策、格鲁吉亚事件与苏维埃“肯定性行动帝国”性质之争 | `historiography/debates/DEB-1923-nationality-and-empire.md` | 流派 `revisionist-lewin, liberal-cold-war-pipes, archival-nationalities-smith, imperial-history-suny, ukrainian-social-history-liber`）：自1922年8月“自治化”方案与格鲁吉亚冲突起，至1923年4月俄共十二大闭幕，布尔什维克究竟是在建设“肯定性行动帝国”式的制度化本土化实践，还是以先锋队组织垄断维系大俄罗斯官僚集权？争论焦点是解密速记所示的制度妥协，以及各学派因果判断与价值判断之别。
- **`DEB-1922-lenin-testament-and-stalin-rise`**（列宁晚年、格鲁吉亚事件与斯大林崛起机制 | `historiography/debates/DEB-1922-lenin-testament-and-stalin-rise.md` | 流派 `revisionist, nationalities-history, archival-post-soviet, kotkin-source-skepticism, trotskyist, service-critical-biography, sakharov-pseudo-lenin-polemic`）：列宁晚年口授文稿和格鲁吉亚冲突，是反官僚与反斯大林的总体“最后斗争”，还是对共同集权框架内具体做法的修正？《遗嘱》本身是否存在文本流转疑点？斯大林的上升又如何由个人策略、书记处机关、寡头集体领导与反对派失策共同解释？
- **`DEB-1928-bukharin-alternative`**（布哈林替代方案与新经济政策终结之争 | `historiography/debates/DEB-1928-bukharin-alternative.md` | 流派 `nep-alternative, economic-growth, structural-dilemma, apparatus, ideology-and-mobilization, cliometrics-and-archival-reassessment`）：1927至1929年粮食危机与新经济政策的瓦解，是否意味着渐进工业化和工农联盟已无可行出路，还是党内权力与政策选择扼杀了布哈林的替代方案？投资、价格、农民供粮和政治动员之间的约束究竟有多强，必须把经济可行性、政治可行性与实际权力斗争分别检验。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/33 条)
- **`CLM-lewin-1968-georgian-affair-bureaucracy`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.9、Ch.10 与 Appendixes I–III, VII–VIII]: 
- **`CLM-carr-1954-scissors-crisis-mechanics`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 17, 29-30, 95-96, 100-101, 105-107, 127]: 
- **`CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia`** [`SCH-smith-jeremy`(杰里米·史密斯) | pp. 311, 321-325, 327-331]: 
- **`CLM-smith-jeremy-1999-georgian-affair-reassessed`** [`SCH-smith-jeremy`(杰里米·史密斯) | pp. 252-253, 260-262, 266-268, 285-288, 296-297]: 
- **`CLM-lewin-1968-testament-intent`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.10 'If Lenin Had Lived . . .'；列宁原文脚注见 Soch. XLV p. 392；XLIV p. 428]: 
- **`CLM-carr-1950-self-determination-to-federal-reunion`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | pp. 253-285, 364-428]: 
- **`CLM-suny-2017-empire-and-nationality-dimension`** [`SCH-suny-ronald-gregor`(罗纳德·格里戈尔·苏尼) | pp. 125-140 (approx. ch. 3 opening theory; see also Witte L322-328)]: 
- **`CLM-liber-1992-korenizatsiia-paradox-late-1920s`** [`SCH-liber-george`(乔治·O·利伯) | pp. 155–157; 180–186]: 
- **`CLM-liber-1992-ukrainianization-and-urban-working-class`** [`SCH-liber-george`(乔治·O·利伯) | pp. 75–76; 99–105]: 
- **`CLM-lewin-1968-cooperation-shift`** [`SCH-lewin-moshe`(摩西·莱文) | n/a（EPUB 无页码锚点）；Ch.8 'Russia between West and East'；列宁原文脚注 Soch. XLV pp. 367, 370, 373, 387–88, 389]: 
- **`CLM-khlevniuk-2015-secretariat-and-nomenklatura`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（In Lenin's Shadow，GENERAL SECRETARY 至 1923 年 9 月组织局安排）；制度总论见 ops/xhtml/ch01a.html。工作区文本无纸质页码。]: 
- **`CLM-khlevniuk-2015-collective-leadership-erosion`** [`SCH-khlevniuk-oleg`(奥列格·赫列夫纽克) | EPUB ops/xhtml/ch02.html（TRYING OUT COLLECTIVE LEADERSHIP 至 THE CHOICE）。工作区文本无纸质页码。]: 
- **`CLM-kotkin-2014-geopolitics-and-ideology`** [`SCH-kotkin-stephen`(斯蒂芬·科特金) | EPUB Ch. 13 (OEBPS/9780698170100_EPUB_1-23.xhtml) & Coda (OEBPS/9780698170100_EPUB_1-25.xhtml)]: 
- **`CLM-deutscher-1959-disarmed-prophet-paradox`** [`SCH-isaac-deutscher`(艾萨克·多伊彻) | （中译本无独立纸页；对应第二部 1923 年争论章）]: 
- **`CLM-service-2009-trotsky-authoritarian-consensus`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本第 23–24、28–29、37 章及引言]: 
- **`CLM-service-2009-trotsky-political-tactical-blunders`** [`SCH-service-robert`(罗伯特·瑟维斯) | 中译 EPUB 无纸页码；对应英文本引言及第 31–32、37–38 章]: 
- **`CLM-sakharov-2012-lenin-cooperative-plan-debates`** [`SCH-sakharov-valentin`(瓦连京·萨哈罗夫) | EPUB Ch. 1.3 & Ch. 4.2]: 
- **`CLM-sakharov-2012-nep-crossroads-1928`** [`SCH-sakharov-valentin`(瓦连京·萨哈罗夫) | EPUB Ch. 4.2 & Ch. 4.3]: 
- **`CLM-cohen-1973-nep-viability`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 270-276, 316-320]: 
- **`CLM-cohen-1973-notes-of-an-economist`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 295-296, 318-320]: 
- **`CLM-cohen-1973-bukharin-organizational-defeat`** [`SCH-cohen-stephen`(斯蒂芬·F·科恩) | pp. 287-289, 297-301, 322-329]: 
- **`CLM-erlich-1960-bukharin-balanced-growth`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 21-23 (PDF pp. 38-40)]: 
- **`CLM-erlich-1960-preobrazhensky-dilemma`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 34-36, 40-41, 49-51, 170-171 (PDF pp. 51-53, 57-58, 66-68, 185-186)]: 
- **`CLM-erlich-1960-stalin-overkill-turn`** [`SCH-erlich-alexander`(亚历山大·埃利希) | pp. 161-169, 172-177, 183-184 (PDF pp. 176-184, 187-192, 198-199)]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
