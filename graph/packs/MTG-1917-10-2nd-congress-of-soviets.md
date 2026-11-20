# 1-Hop 去重平衡上下文包：`MTG-1917-10-2nd-congress-of-soviets`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`MTG-1917-10-2nd-congress-of-soviets`** (第二届全俄工兵代表苏维埃代表大会 | `cards/meetings/MTG-1917-10-2nd-congress-of-soviets.md` | `multi-perspective`): 已覆盖=`participant-memoir, social-history, menshevik-internationalist, soviet-orthodox, liberal-totalitarian`；待补=`peasant-delegate-voice`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1917-10-25至10-27[O.S.]/11-07至11-09[N.S.]，全俄苏维埃二大在斯莫尔尼召开。孟什维克、右翼社革党退场，左派社革党留场；大会宣告苏维埃掌权，通过和平、土地法令，成立列宁领导的纯布尔什维克政府及加米涅夫任主席的中执委，合法性与联合政府之争公开化。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **开幕与温和派退场（`1917-10-25 [O.S.] / 1917-11-07 [N.S.]` 深夜至跨午夜）**：约 `22:40–23:00` 旧中央执委会代表丹宣布开会后交棒，布尔什维克与左派社会革命党人组成大会主席团（加米涅夫主持，孟什维克国际主义派声明暂不入主席团）。马尔托夫动议优先停火、和平协商组建全民主政权，获卢那察尔斯基附议及全会无异议表决先议；旋即孟什维克（欣丘克）、右派社会革命党（格尔德曼）、崩得（埃尔利希、阿布拉莫维奇）等代表抗议“背着大会发动军事阴谋”并宣布退出大会。托洛茨基（时任彼得格勒苏维埃主席、军革委核心领导人）登台拒绝妥协并斥退场者“到历史的垃圾堆里去”；随后孟什维克国际主义派在走廊党团会议上经激烈争论（据苏汉诺夫回忆党团内表决约为 **14票对12票**，非大会计票）决定追随马尔托夫退场（苏汉诺夫1922年撰书时追悔未当场决裂留会是自己“最大的罪过”），而左派社会革命党人等留场参会。
- **冬宫陷落通报与第一次会议通过夺权宣言（`1917-10-26 [O.S.] / 1917-11-08 [N.S.]` 凌晨）**：加米涅夫在会场宣读冬宫已被攻占、临时政府部长（克伦斯基除外）被捕的通报；约凌晨 `05:00` 后，大会以仅2票反对、12票弃权的压倒多数通过由**卢那察尔斯基宣读的《告工人、士兵和农民书》**，正式宣告临时政府与旧执委会权力终结、一切全国与地方政权转归苏维埃，第一次会议遂休会（人民委员会此时尚未提出，系次日日间由布尔什维克高层商拟，左派社革党婉拒即刻入阁）。
- **第二次会议通过《和平法令》《土地法令》及批准成立人民委员会（`1917-10-26 [O.S.] / 1917-11-08 [N.S.]` 晚至 `10-27 [O.S.] / 11-09 [N.S.]` 凌晨）**：第二次会议于 `10-26 [O.S.] / 11-08 [N.S.]` 约 `21:00` 开幕。列宁首先宣读 **《和平法令》（Декрет о мире）**，提议各交战国立即就“不兼并、不赔款”的民主和约展开公开谈判并停战至少三个月，获全场一致通过；随后列宁报告 **《土地法令》（Декрет о земле）**，经跨午夜辩论后于 `10-27 [O.S.] / 11-09 [N.S.]` 凌晨表决通过（1957年《苏维埃政权法令汇编》第1卷标题记“10月26日会议夜间2时通过”，传统法令刊本统一署会议起始日 `10-26 [O.S.] / 11-08 [N.S.]`；中文全集注记1票反对、8票弃权）。法令正文宣布立即无偿废除地主土地所有制，将地主田庄及皇族、修道院、教会土地连同耕畜农具交乡土地委员会和县农民苏维埃支配直至立宪会议召开，同时第5条明确规定**普通农民和普通哥萨克的土地概不没收**；第4条将《全俄农民代表苏维埃消息报》编辑部据 **242份地方农民委托书** 汇编的《农民的土地问题委托书》纳为过渡期指导性临时法律。第二次会议末段（`10-27 [O.S.] / 11-09 [N.S.]` 凌晨，编年研究定时约 `04:00`）正式批准成立临时工农政府——**人民委员会（Sovnarkom）**（列宁任主席，由纯布尔什维克组成，在立宪会议召开前向苏维埃大会及中央执委会负责），并选出新一届**全俄中央执行委员会**（加米涅夫任主席，约百人中布尔什维克约62席、左派社革党约29席及若干小派别），于清晨约 `05:00–05:15` 闭幕。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `EVT-1917-10-october-revolution` | `ratifies-power-transfer` | 1917-10-25~27 [O.S.] / 11-07~09 [N.S.] | 大会通过《告工人、士兵和农民书》追认推翻临时政府并宣告一切政权归苏维埃，其全国代表性合法性构成核心史学争鸣 | `DEB-1917-october-coup-or-social-revolution` |
| `PER-lenin` | `drafts-decrees-and-chairs-sovnarkom` | 1917-10-26~27 [O.S.] / 11-08~09 [N.S.]起 | 在第二次会议报告《和平法令》《土地法令》，并于10-27 [O.S.] / 11-09 [N.S.]凌晨获准出任首届人民委员会主席 | `WEB-1917-10-26-decrees-peace-land`; `1917-10_october_insurrection.md` |
| `PER-trotsky` | `insurrection-congress-linchpin` | 1917-10-25~27 [O.S.] / 11-07~09 [N.S.] | 以彼得格勒苏维埃主席兼军革委核心领导身份在大会发表拒绝向退场派妥协的演说（会末任外交人民委员；大会主持与新全俄中执委主席则为加米涅夫） | `CLM-sukhanov-1922-october-walkout-tragedy`; `1917-10_october_insurrection.md` |
| `PER-kamenev` | `presides-and-chairs-vtsik` | 1917-10-25~27 [O.S.] / 11-07~09 [N.S.] | 主持二大主席团议程并通报冬宫陷落，闭幕时当选新一届全俄中央执行委员会（VTsIK）主席 | `1917-10_october_insurrection.md#L205-L257` |
| `PER-martov-l` | `walkout-leader` | 1917-10-25~26 [O.S.] / 11-07~08 [N.S.] | 停火协商动议获先议通过后因武装夺权既成事实及托洛茨基强硬回击，在党团约14:12表决后率国际主义派退场 | `CLM-sukhanov-1922-october-walkout-tragedy` |
| `PER-chernov` | `absent-rival` | 1917-10 [O.S.] / 11 [N.S.] | 右翼社革党退场且切尔诺夫未在场，布尔什维克在《土地法令》中直接采纳农民苏维埃消息报汇总的242份地方委托书纲领以争取农村与左派社革党支持 | `WEB-1917-10-26-decrees-peace-land` |
| `POL-brest-litovsk-treaty` | `policy-prefigured` | 1917-10-26 [O.S.] / 11-08 [N.S.]起 | 《和平法令》确立公开外交与退出世界大战原则，1918年3月布列斯特和约则在极端不利条件下被迫有偿割地停战 | `WEB-1917-10-26-decrees-peace-land` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：大会在彼得格勒武装起义进行当夜开幕；马尔托夫停火与民主协商程序动议先获无异议通过，随后孟什维克、右翼社革党、崩得及马尔托夫国际主义派相继退出，左派社革党等留场；第一次会议凌晨通过卢那察尔斯基宣读的《告工人、士兵和农民书》；第二次会议跨夜通过《和平法令》《土地法令》，并于 `10-27 [O.S.] / 11-09 [N.S.]` 凌晨批准成立列宁为首的纯布尔什维克人民委员会及布尔什维克—左派社革党为主的新全俄中央执委会。
- **主要解释分歧**（详参 `DEB-1917-october-coup-or-social-revolution`, `DEB-1918-constituent-assembly-and-soviet-democracy`）：
  - **[当事人批判回忆视角 / N. N. Sukhanov (1922)]**（`CLM-sukhanov-1922-october-walkout-tragedy`）：作为反对退场的孟什维克国际主义派亲历者，既在事后回望中痛责温和派与国际主义派退场解除了大会内部对列宁派的制度约束，同时明确反驳右翼将 `10-25 [O.S.]` 说成脱离工兵群众之“纯军事阴谋”的自我安慰，但也怀疑布尔什维克单独执政的正当性与前景。
  - **[自由派“政变包装论” / Richard Pipes (1990) 等]**：认为列宁与托洛茨基蓄意在二大开幕前造成推翻临时政府的武力既成事实以逼走温和社会主义各党，退场后的斯莫尔尼会场已丧失全国代表性，沦为替少数派武装政变披上“苏维埃合法外衣”的橡皮图章。
  - **[社会史与政治修正派 / Alexander Rabinowitch (1976), S. A. Smith (1983)]**：强调“一切权力归苏维埃”及和平、土地两项法令精准回应了1917年秋彼得格勒工兵与农村基层激进化的核心诉求，大会是底层社会革命能量与布尔什维克纲领接合的制度化枢纽；温和派退场与左派社革党暂拒入阁则共同促成了最初纯布尔什维克人民委员会的形成。

## 2. 一跳邻域全量微摘要目录 (去重后共 9 个节点，0 截断)
- **`EVT-1917-10-october-revolution`**（1917年十月革命）: 1917年10月24—27日（俄历；公历11月6—9日），军事革命委员会夺取彼得格勒中枢，冬宫陷落，苏维埃二大通过和平、土地法令并建立人民委员会。群众激进化、组织夺权与多党联合失败交织；首都迅速接管不代表全国无血革命。 ‖ `→MTG-1917-10-2nd-congress-of-soviets`[contested_authorization|1917-10-25..27 [O.S.] / 11-07..09 [N.S.]]: 退场削弱联合动议，大会追认苏维埃政权并组建政府。 ； `←MTG-1917-10-2nd-congress-of-soviets`[ratifies-power-transfer|1917-10-25~27 [O.S.] / 11-07~09 [N.S.]]: 大会通过《告工人、士兵和农民书》追认推翻临时政府并宣告一切政权归苏维埃，其全国代表性合法…
- **`INS-sovnarkom-and-vtsik`**（人民委员会与全俄、全苏中央执行委员会）: 苏维埃代表大会闭会期间，中执委在宪制上监督政府，人民委员会却迅速掌握施政与大量法令制定。苏俄与1922年成立的苏联各有中执委与人民委员会，不能混同。党内领导与国家机关关系不断变化，政治局权重日增，但1920年代仍须经政府落实决策。 ‖ `→MTG-1917-10-2nd-congress-of-soviets`[constituting_event|1917-10-26 [O.S.]]: 选出中执委并成立工农政府
- **`PER-lenin`**（弗拉基米尔·列宁）: 布尔什维克党缔造者、苏俄人民委员会主席（1917–1924）。1893年投身马克思主义运动，1903年促成布尔什维克分化；1917年发表《四月提纲》并领导十月夺权，历经布列斯特和约、内战与战时共产主义；1921年主持转向新经济政策，晚年（1922–1923）就官僚化与接班人同斯大林冲突。 ‖ `←MTG-1917-10-2nd-congress-of-soviets`[drafts-decrees-and-chairs-sovnarkom|1917-10-26~27 [O.S.] / 11-08~09 [N.S.]起]: 在第二次会议报告《和平法令》《土地法令》，并于10-27 [O.S.] / 11-09 …
- **`PER-trotsky`**（列夫·托洛茨基）: 俄国革命家、“不断革命论”提出者，1905年彼得堡苏维埃实际领袖与1917年彼得格勒苏维埃主席；借军革委与苏维埃二大衔接统筹十月夺权，内战期起用4.8万军事专家缔造红军。1923–1927年领衔左翼与联合反对派抗衡斯大林集权并受“红色波拿巴”污名围剿，1927年被开除出党，1929年被驱逐出境。 ‖ `←MTG-1917-10-2nd-congress-of-soviets`[insurrection-congress-linchpin|1917-10-25~27 [O.S.] / 11-07~09 [N.S.]]: 以彼得格勒苏维埃主席兼军革委核心领导身份在大会发表拒绝向退场派妥协的演说（会末任外交人民…
- **`PER-kamenev`**（列夫·加米涅夫）: 老布尔什维克、首任全俄中执委主席。1917年自四月至立宪会议一贯坚守温和宪政社会主义联盟路线并公开反对十月起义；1924年十三大联手季诺维也夫压下《列宁遗嘱》，1925年十四大公开发言反斯大林“领袖”集权后失势；1928年7月密会布哈林并留下外泄笔记，反成右派致命罪证。 ‖ `←MTG-1917-10-2nd-congress-of-soviets`[presides-and-chairs-vtsik|1917-10-25~27 [O.S.] / 11-07~09 [N.S.]]: 主持二大主席团议程并通报冬宫陷落，闭幕时当选新一届全俄中央执行委员会（VTsIK）主席
- **`PER-martov-l`**（尤利·马尔托夫）: 孟什维克核心领袖与国际主义左翼旗手。1903年二大凭党章第一条（28:22:1）与列宁分道；1917年七月夜倡“清一色社会主义政府”遭党内主流否决，十月二大率派退场；1918年工人抗议浪潮中坚持苏维埃合法反对派立场，1920年哈雷大会与季诺维也夫正面交锋痛斥恐怖与二十一条，后流亡柏林病逝。 ‖ `←MTG-1917-10-2nd-congress-of-soviets`[walkout-leader|1917-10-25~26 [O.S.] / 11-07~08 [N.S.]]: 停火协商动议获先议通过后因武装夺权既成事实及托洛茨基强硬回击，在党团约14:12表决后率…
- **`PER-chernov`**（维克托·切尔诺夫）: 俄国社会革命党创始人兼首席理论家，“土地社会化”纲领制定者。早期纵容阿泽夫战斗组织并在1909年丑闻后陷于党务瘫痪；1917年任联合内阁农业部长进退维谷，1918年1月以244:153当选全俄立宪会议一日主席即遭驱散，萨马拉—乌法“第三力量”亦破产，后流亡欧美。 ‖ `←MTG-1917-10-2nd-congress-of-soviets`[absent-rival|1917-10 [O.S.] / 11 [N.S.]]: 右翼社革党退场且切尔诺夫未在场，布尔什维克在《土地法令》中直接采纳农民苏维埃消息报汇总的…
- **`POL-brest-litovsk-treaty`**（布列斯特-立陶夫斯克和约）: 布列斯特和约路线是在军事崩溃与世界革命期待之间作出的单独媾和选择。列宁主张割地换取喘息，布哈林主张革命战争，托洛茨基“不战不和”随德军进逼破产。1918年3月签约虽保住苏维埃政权，却造成重大领土与工业损失，引发党内激烈分裂并推动左派社革党退出联合政府。 ‖ `←MTG-1917-10-2nd-congress-of-soviets`[policy-prefigured|1917-10-26 [O.S.] / 11-08 [N.S.]起]: 《和平法令》确立公开外交与退出世界大战原则，1918年3月布列斯特和约则在极端不利条件下… ； `→MTG-1917-10-2nd-congress-of-soviets`[政策源头|1917-10-26 [O.S.] / 11-08 [N.S.]]: 《和平法令》开启退出一战外交议程并埋下单独媾和伏笔。
- **`EVT-1918-09-red-terror-and-left-sr-rupture`**（1918年夏左翼社革党决裂与红色恐怖制度化）: 1918年7月左翼社革党刺杀米尔巴赫，其意在逼废和约抑或夺权存史学争议，随后遭布党镇压并被逐出苏维埃权力核心。8月30日乌里茨基遇害、列宁遇刺后，9月5日红色恐怖法令将集中营隔离与枪决制度化。一党垄断与暴力升级须分别追踪，登记死亡数非全部受害者。 ‖ `→MTG-1917-10-2nd-congress-of-soviets`[contrasted_with|1917.10 vs 1918.09]: 从1917年10月建政转向1918年9月制度化恐怖行政执法。

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 3 项)
- **`DEB-1917-october-coup-or-social-revolution`**（十月革命：少数派政变还是社会革命？ | `historiography/debates/DEB-1917-october-coup-or-social-revolution.md` | 流派 `liberal-coup, party-social-history, russian-revisionist-timing, labor-local-history, moderate-socialist-and-constitutional-legitimacy, participant-marxist, peasant-social-history, borderland-and-memory-historiography`）：十月武装夺权是少数派政变，还是工人、士兵与农民社会革命的政治表达？有组织的起义与广泛的基层动员能否同时成立，苏维埃多数又能否代表全国选民？这些问题涉及不同地区、不同时间的支持与合法性，不能以一次投票或一次攻占行动互相替代。
- **`DEB-1918-constituent-assembly-and-soviet-democracy`**（解散立宪会议与多党苏维埃民主的命运 | `historiography/debates/DEB-1918-constituent-assembly-and-soviet-democracy.md` | 流派 `liberal-totalitarian, revisionist, sr-electoral-political-history, menshevik-history, security-legal-history`）：1918年立宪会议被武力解散，是否意味着一党统治已不可避免？争论涉及普选制宪与阶级性苏维埃两种合法性、群众动员和镇压，以及此后左翼多党合作与体制内反对派仍有多少政治空间。
- **`DEB-1918-red-terror-and-civil-war-origins`**（红色恐怖、契卡扩张与内战期一党专政起源之争（1918–1921） | `historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md` | 流派 `liberal-continuity, institutional-cheka, contingency-coalition, local-violence-and-chronicle, repressed-socialists-and-worker-protest, civil-war-structure-and-total-war, post-soviet-archival-quantitative`）：红色恐怖和契卡法外权力是列宁主义政治逻辑的必然结果，还是内战、粮食危机、联盟破裂与地方暴力交织下的制度选择？中央命令与地方自主行动怎样互相强化？恐怖升级、社会主义对手遭镇压和一党统治形成各有不同时间线，不能压缩成同一事件。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/40 条)
- **`CLM-sukhanov-1922-october-walkout-tragedy`** [`SCH-sukhanov-nikolai`(尼古拉·苏汉诺夫) | pp. 631–647, 657–660 (PDF pp. 683–699, 709–711)]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-rabinowitch-1976-open-democratic-mass-party`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-rabinowitch-1976-october-three-factions-debate`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-rabinowitch-1976-trotsky-soviet-congress-strategy`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | 未核：EPUB 章节及行号]: 
- **`CLM-loginov-lenin-1917-fleeting-window-of-power`** [`SCH-loginov-vladlen`(弗拉德连·洛吉诺夫) | pp. 523-524, 531-532, 560-561, 621-622, 656-658]: 
- **`CLM-smith-sa-1983-defensive-workers-control`** [`SCH-smith-sa`(斯蒂芬·A·史密斯（S. A. Smith）) | 中译本 pp. 106–112, 133, 135, 137, 191（即源文件标注 PDF pp. 111–117, 138, 140, 142, 196）；注意：均为中译本页码，非英文原版页码]: 
- **`CLM-koenker-1981-moscow-october-armed-struggle-vs-petrograd`** [`SCH-koenker-diane`(黛安·P·科恩克尔) | pp. 329–355 (local PDF pp. 345–371); p. 366 (PDF p. 382)]: 
- **`CLM-koenker-1981-rational-incremental-radicalization`** [`SCH-koenker-diane`(黛安·P·科恩克尔) | pp. 359–363 (local PDF pp. 375–379); p. 254 (PDF p. 270)]: 
- **`CLM-basil-1984-october-and-vikzhel-collapse`** [`SCH-basil-john`(约翰·D·巴兹尔) | pp. 165–175（本地 PDF 同号）]: 
- **`CLM-yao-hai-post-october-coalition-failure-and-one-party-formation`** [`SCH-yao-hai`(姚海) | [PDF pp. 532-535, 543-569]]: 
- **`CLM-yao-hai-constituent-assembly-vs-soviet-legitimacy-clash`** [`SCH-yao-hai`(姚海) | [PDF pp. 574-596]]: 
- **`CLM-rabinowitch-2007-constituent-assembly`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 88-91, 105-110, 121-127]: 
- **`CLM-trotsky-1930-art-of-insurrection-and-soviet-legality`** [`SCH-trotsky-leon`(列夫·达维多维奇·托洛茨基 · participant-historian) | （中译 EPUB 无纸页；第三卷第二十—二十一章）]: 
- **`CLM-figes-1996-peasant-moral-economy-1917`** [`SCH-figes-orlando`(奥兰多·费吉斯) | pp. 343-352]: 
- **`CLM-suny-2017-totalitarian-vs-social-history-turn`** [`SCH-suny-ronald-gregor`(罗纳德·格里戈尔·苏尼) | pp. 87-95 (approx. ch. 2 sect. on totalitarianism and revision)]: 
- **`CLM-suny-2017-class-discourse-and-polarization`** [`SCH-suny-ronald-gregor`(罗纳德·格里戈尔·苏尼) | pp. 160-175 (approx. ch. 5 on class, strikes, discourse)]: 
- **`CLM-blanc-2021-borderlands-in-1905-and-1917`** [`SCH-blanc-eric`(埃里克·布兰克) | pp. 20–23, 338–436, 488–531, 457–543]: 
- **`CLM-corney-2004-istpart-and-institutionalizing-october-memory`** [`SCH-corney-frederick`(弗雷德里克·C·科尼 · memory-and-cultural-history) | 【待规整语料】]: 
- **`CLM-rabinowitch-2007-left-sr-coalition-collapse`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 274-282, 287-309, 395-396]: 
- **`CLM-smith-scott-2011-psr-third-force-collapse`** [`SCH-radkey-oliver`(奥利弗·亨利·拉德基) | pp. 452-455, 467-473, 490-493 (PDF pp. 468-471, 483-489, 506-509)]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-getzler-1967-martov-soviet-opposition`** [`SCH-getzler-israel`(伊斯雷尔·格茨勒) | pp. 168-191]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
