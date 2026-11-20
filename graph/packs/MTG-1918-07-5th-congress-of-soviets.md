# 1-Hop 去重平衡上下文包：`MTG-1918-07-5th-congress-of-soviets`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`MTG-1918-07-5th-congress-of-soviets`** (第五次全俄工农兵与哥萨克苏维埃代表大会（1918年7月） | `cards/meetings/MTG-1918-07-5th-congress-of-soviets.md` | `multi-perspective`): 已覆盖=`constitution-primary, archival-revisionist, soviet-government-contemporary, pipes-figes-exclusionary-logic, leggett-cheka-institutionalization, carr-constitutional-fusion`；待补=`full-congress-proceedings, independent-left-sr-archive, regional-credentials-materials`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1918-07-04 至 1918-07-10 [N.S.]，第五次全俄苏维埃大会在莫斯科召开。布尔什维克与左翼社革党围绕和约、粮食政策及代表资格尖锐冲突；7月6日米尔巴赫遇刺后，武装冲突和对左翼社革党的拘押使两党苏维埃合作崩溃。7月10日，留下的代表通过首部俄罗斯苏维埃联邦社会主义共和国宪法。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **争论与资格**：大会在莫斯科大剧院举行。斯皮里多诺娃和卡姆科夫等左翼社革党人猛烈批评布列斯特和约、粮食专政及贫农委员会。开幕会上宣布的党派预报分布为：布尔什维克 678 人、左翼社革党 269 人，**其余 88 人**分属最高纲领派社革党人（约 30）、社民党国际主义者（5–6）及无党派代表（约 48），**表决权代表合计 1,035 人**（Rabinowitch，*The Bolsheviks in Power*，p. 288；作者称这些选举“从未被独立调查过，现在也大概无法调查”）。据 Rabinowitch 原书数字换算，678/1,035 约 65.5%，269/1,035 约 26.0%（本库换算，非原书数字）。左翼社革党在资格审查委员会中质疑约 399 名布尔什维克代表的资格，并要求资格委员会双方人数相等而被否决。**原书措辞是：会前各报的预报统计“未包含”这约 399 名被质疑的布尔什维克代表**（p. 288 后文），而 678 是开幕会的预报数；这批被质疑代表与 678 的集合关系须核原书页码，不得据站内 L3 写作“678 含 399”。Rabinowitch 认为存在人为制造布尔什维克多数的大量间接证据；这不是对 399 份证件逐一鉴定为伪造的证明，也不能从公布人数中机械扣减，算出合法代表数。
- **刺杀与拘押**：1918-07-06 [N.S.]，左翼社革党人布柳姆金和安德烈耶夫刺杀德国大使米尔巴赫，莫斯科随即发生武装冲突；L3 记当日捷尔任斯基曾被波波夫的契卡战斗支队扣押。大会会场内左翼社革党党团及来宾遭集体拘押：Rabinowitch 记为 400 余人被捕，包含来宾，其中不确定数量者被就地枪决（亚历山德罗维奇在内），故常见的约 450 人不能直接当成核实过的代表人数。左翼社革党党团被挤进大剧院楼上两间屋数日，**13 名“主犯”被送往克里姆林牢房，约 100 人获释，余者羁押于亚历山德罗夫军校并陆续释放**；资格审查委员会中的左翼社革党人至大会结束才获释，此时其对布尔什维克代表的异议已无意义（ch17 L462–474）。
- **宪法与联盟终结**：1918-07-10 [N.S.]，在左翼社革党代表被排除的情况下复会，通过首部《俄罗斯社会主义联邦苏维埃共和国宪法》。左翼社革党人民委员此前已于3月因和约退阁，7月的破裂则终结了其与布尔什维克作为主要合作伙伴的苏维埃政治联盟；这不等于所有地方异议者或全部社会主义者同日消失。宪法并无“一党”条款；Rabinowitch 只说宪法延续了苏维埃大会为最高机关的“虚构”，而人民委员会在实践中占上风，并在中央执委会中排除了孟什维克、右翼社革党与左翼社革党。
- **后果链（制度层面）**：左翼社革党被清出契卡，参与契卡的左翼成员被处决，使契卡内部的左翼否决机制消失；这一制度后果不应只被当作议会层面的“联盟终结”（见 2.3 与 `EVT-1918-09-red-terror-and-left-sr-rupture`）。

### 2.2 时效关系摘要边表
| 关联节点 ID | 关系类型 | 有效时段 | 关系实质摘要 | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-left-srs` | `coalition_breakdown` | 1918年3–7月 | 3月退出人民委员会，7月刺杀及拘押后苏维埃合作瓦解。 | Rabinowitch pp. 287–296 |
| `PER-spiridonova` | `challenges_government` | 1918年夏 | 左翼社革党领袖批评和约及农村政策；资格异议须与已证事实分开；刺杀后到大剧院解释时被捕。 | Rabinowitch pp. 284–288，ch17 L475；`AUD-14` |
| `EVT-1918-03-brest-litovsk-treaty` | `contested_at` | 1918年7月 | 和约成为两党冲突及刺杀背景。 | Rabinowitch ch. 11 |
| `ORG-cheka-ogpu` | `entangled_in_conflict` | 1918年7月 | 刺杀与武装冲突涉及波波夫的契卡战斗支队，事后契卡内部左翼成员被清除。 | Rabinowitch pp. 291–294；`CLM-leggett-1981-red-terror-institutionalization` |
| `DEB-1918-constituent-assembly-and-soviet-democracy` | `illuminates` | 1918年 | 资格争议与宪法条款提供考察苏维埃代表性之不同证据。 | 宪法第25、64–65条 |
| `EVT-1918-09-red-terror-and-left-sr-rupture` | `consequence_in` | 1918年7–9月 | 7月破裂的后续：红色恐怖与左翼社革党制度性出局。 | `DEB-1918-red-terror-and-civil-war-origins` |
| `CLM-rabinowitch-2007-left-sr-coalition-collapse` | `supported_by` | 1918年3–7月 | 档案修正派对联盟崩溃与资格争议的解释。 | Rabinowitch 2007 |
| `CLM-carr-1950-1918-constitution-fusion-of-powers-and-class-franchise` | `compared_with` | 1918年7月 | Carr 对宪法权力融合与阶级选举权的判断；其“城乡 1:5”表述的分母口径须与宪法档案核对。 | 宪法 S 级档案 L28 |

### 2.3 史学争鸣光谱
**经验层面**：大使遇刺、冲突、党团被拘押与7月10日通过宪法均有文献支持；有争议的代表资格不能一律认定造假。**行动目的与性质**：
- **苏维埃政府当时的定性**：事件为反苏维埃政权的起义。
- **Rabinowitch（档案修正派）**：经档案研究认为主要目的是迫使政府改变政策，而非武力夺权，但对普罗相短暂占据电报局及其可能未经授权保留例外。其判断并不抹去刺杀和武装冲突本身（`CLM-rabinowitch-2007-left-sr-coalition-collapse`）。
- **Pipes / Figes 一派**：把7月事件置于布尔什维克一贯排除对手、清除竞争性社会主义政党的逻辑中（`CLM-pipes-1990-red-terror-leninist-logic`）。
- **Leggett 一派**：以契卡内部左翼被清除视为制度转折，契卡由此失去来自盟友的内部制衡（`CLM-leggett-1981-red-terror-institutionalization`）。
- **Carr（宪法层面的权力融合）**：把宪法视为党—苏维埃—行政权力融合的法典化（`CLM-carr-1950-1918-constitution-fusion-of-powers-and-class-franchise`）。
- 站内 `DEB-1918-red-terror-and-civil-war-origins` 另含 Hoffmann、Mawdsley 等视角，可作延伸。

## 2. 一跳邻域全量微摘要目录 (去重后共 6 个节点，0 截断)
- **`EVT-1918-09-red-terror-and-left-sr-rupture`**（1918年夏左翼社革党决裂与红色恐怖制度化）: 1918年7月左翼社革党刺杀米尔巴赫，其意在逼废和约抑或夺权存史学争议，随后遭布党镇压并被逐出苏维埃权力核心。8月30日乌里茨基遇害、列宁遇刺后，9月5日红色恐怖法令将集中营隔离与枪决制度化。一党垄断与暴力升级须分别追踪，登记死亡数非全部受害者。 ‖ `→MTG-1918-07-5th-congress-of-soviets`[political_rupture_arena|1918-07-04..10]: 大会争执、代表拘押与宪法通过构成两党苏维埃合作转折。 ； `←MTG-1918-07-5th-congress-of-soviets`[consequence_in|1918年7–9月]: 7月破裂的后续：红色恐怖与左翼社革党制度性出局。
- **`INS-sovnarkom-and-vtsik`**（人民委员会与全俄、全苏中央执行委员会）: 苏维埃代表大会闭会期间，中执委在宪制上监督政府，人民委员会却迅速掌握施政与大量法令制定。苏俄与1922年成立的苏联各有中执委与人民委员会，不能混同。党内领导与国家机关关系不断变化，政治局权重日增，但1920年代仍须经政府落实决策。 ‖ `→MTG-1918-07-5th-congress-of-soviets`[constitution_adoption|1918-07-10]: 通过苏俄宪法
- **`ORG-left-srs`**（左翼社会革命党）: 1917年底从社会革命党分裂出的激进民粹派政党（1917–1923），以斯皮里多诺娃、普罗相等为首。拥护苏维埃政权并于1917年12月加入人民委员会与布尔什维克联合执政；1918年3月因反《布列斯特和约》退阁但仍维持北方公社合作，7月6日刺杀德国大使米尔巴赫遭全面清洗而覆灭。 ‖ `←MTG-1918-07-5th-congress-of-soviets`[coalition_breakdown|1918年3–7月]: 3月退出人民委员会，7月刺杀及拘押后苏维埃合作瓦解。
- **`PER-spiridonova`**（玛丽亚·斯皮里多诺娃）: 左翼社革党领袖。1906年枪击镇压官卢热诺夫斯基致死，历十一年苦役获革命声望。1917–1918年推动农民苏维埃合并，竞选立宪会议主席以153票负于切尔诺夫244票；1918年7月苏维埃五大期间参与发起刺杀米尔巴赫，亲赴会场承担政治责任并被捕。 ‖ `←MTG-1918-07-5th-congress-of-soviets`[challenges_government|1918年夏]: 左翼社革党领袖批评和约及农村政策；资格异议须与已证事实分开；刺杀后到大剧院解释时被捕。
- **`EVT-1918-03-brest-litovsk-treaty`**（1918年布列斯特-里托夫斯克和约危机与签约）: 1917年12月停战至1918年3月签约，列宁主和、托洛茨基“不战不和”与布哈林革命战争路线交锋。德军进逼后，中央2月23日以7赞成、4反对、4弃权接受最后通牒；和约保存政权，也加深党内裂痕并促使左翼社革党退阁。 ‖ `←MTG-1918-07-5th-congress-of-soviets`[contested_at|1918年7月]: 和约成为两党冲突及刺杀背景。
- **`ORG-cheka-ogpu`**（全俄肃反委员会—国家政治保卫局）: 苏俄与苏联早期政治警察机关（1917–1934），由捷尔任斯基创立。历经全俄肃反委员会（ВЧК，1917–1922）、国家政治保卫局（ГПУ，1922–1923）与国家政治保卫总局（ОГПУ，1923–1934）三阶段，从法外非常机构演变为直属政治局的常设宪制部门，执行红色恐怖与强制集体化。 ‖ `←MTG-1918-07-5th-congress-of-soviets`[entangled_in_conflict|1918年7月]: 刺杀与武装冲突涉及波波夫的契卡战斗支队，事后契卡内部左翼成员被清除。

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

### `DEB-1918-constituent-assembly-and-soviet-democracy`：解散立宪会议与多党苏维埃民主的命运
## [T1] 核心问题定义
1918年立宪会议被武力解散，是否意味着一党统治已不可避免？争论涉及普选制宪与阶级性苏维埃两种合法性、群众动员和镇压，以及此后左翼多党合作与体制内反对派仍有多少政治空间。

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 修正派与地方档案 | Alexander Rabinowitch, *The Bolsheviks in Power* (2007) | 解散由布尔什维克党内温和派（加米涅夫等）败给列宁、左翼社革党配合及相当程度的工农冷漠共同促成；多党苏维埃空间是在1918年春夏危机中分阶段收缩的。 | `CLM-rabinowitch-2007-constituent-assembly`; `CLM-rabinowitch-2007-contingency-of-dictatorship`; `CLM-rabinowitch-2007-left-sr-coalition-collapse` | 彼得格勒经验能否推广全国、危机解释是否低估意识形态与主动镇压，均有争议。 |
| 社会革命党与选举史奠基派 | Oliver H. Radkey, *The Sickle under the Hammer* (1963) | 拆解社革党选票内部俄/乌与左右翼裂痕（299俄社革+81乌社革），揭示右翼社革党领导层因迷信合法议会程序、禁止武装保卫议会而自缚手脚，随后在萨马拉—西伯利亚沦为白卫军官“保护色”。 | `CLM-smith-scott-2011-psr-third-force-collapse`（馆藏真身 Radkey 1963）；`DATA-01` | 对精英策略失误的严厉道德批评有时低估了士兵厌战的结构性约束。 |
| 自由主义制度批判 | Richard Pipes, *The Russian Revolution* (1990) | 将1918年1月枪击保卫立宪会议游行与武力关闭议会视为列宁夺权意志与极权恐怖制度化的真正起点，认为布尔什维克借民众疲惫确立了不受制约的专政。 | `CLM-pipes-1990-october-classic-coup`; `CLM-pipes-1990-red-terror-leninist-logic` | 对地方苏维埃多党合作与1918年上半年布尔什维克党内争论关注不足。 |
| 孟什维克与议会民主传记派 | Israel Getzler, *Martov* (1967); W. H. Roobol, *Tsereteli* (1976) | 策烈铁里在 `1918-01-05 [O.S.]` 立宪会议讲坛作最后跨阶级议会民主抗辩；马尔托夫则在会后转入苏维埃体制内开展半合法反对（直至 `1918-06-14` 全俄中执委驱逐右社革与孟什维克）。 | `CLM-getzler-1967-martov-soviet-opposition`; `CLM-roobol-1976-tsereteli-tragedy-of-moderation` | 领袖政治伦理需与工厂全权代表会议（丘拉科夫 `CLM-churakov-2004-*`）实证规模对勘。 |


### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/24 条)
- **`CLM-leggett-1981-red-terror-institutionalization`** [`SCH-leggett-george`(乔治·莱格特) | pp. 56-59, 102-115, 144-145 (PDF pp. 94-97, 140-153, 182-183)]: 
- **`CLM-rabinowitch-2007-left-sr-coalition-collapse`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 274-282, 287-309, 395-396]: 
- **`CLM-carr-1950-1918-constitution-fusion-of-powers-and-class-franchise`** [`SCH-carr-eh`(爱德华·霍列特·卡尔) | [PDF pp. 67, 72-74]]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-leggett-1981-vecheka-extra-legal-origins`** [`SCH-leggett-george`(乔治·莱格特) | pp. 17-22, 47-49 (PDF pp. 55-60, 85-87)]: 
- **`CLM-leggett-1981-cheka-to-gpu-continuity`** [`SCH-leggett-george`(乔治·莱格特) | pp. 339-352, 355-363 (PDF pp. 377-390, 393-401)]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-raleigh-2001-local-bolshevik-violence-and-clientelism`** [`SCH-raleigh-donald`(唐纳德·J·罗利) | Local PDF pp. 104, 112–130; English print pagination not verified]: 
- **`CLM-cheka-chronicle-hostage-and-local-autonomy`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | EPUB OPS/ch1-6.xhtml; OPS/ch1-10.xhtml; OPS/ch1-14.xhtml; OPS/ch1-15.xhtml; OPS/ch1-16.xhtml; OPS/ch1-19.xhtml（提取文本无印刷页码）]: 
- **`CLM-cheka-chronicle-suppression-of-socialist-rivals`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | EPUB OPS/ch1-4.xhtml; OPS/ch1-5.xhtml; OPS/ch1-9.xhtml; OPS/ch1-10.xhtml; OPS/ch1-15.xhtml; OPS/ch1-16.xhtml（提取文本无印刷页码）]: 
- **`CLM-plekhanov-am-dzerzhinsky-cheka-institutionalization`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | pp. 55-56, 97-106, 118-123, 147-155, 209-211, 228]: 
- **`CLM-halle-1920-martov-critique-of-terror-and-21-conditions`** [`SCH-martov-iulii`(尤利·奥西波维奇·马尔托夫 · participant-primary-text) | pp. 167–170, 173, 175–176, 179 (Lih translation in the 2011 Lewis/Lih edition; printed page = PDF page − 1). Full speech pp. 167–179, delivered 15 October 1920 [N.S.]]: 
- **`CLM-smith-scott-2011-psr-third-force-collapse`** [`SCH-radkey-oliver`(奥利弗·亨利·拉德基) | pp. 452-455, 467-473, 490-493 (PDF pp. 468-471, 483-489, 506-509)]: 
- **`CLM-churakov-2004-soviet-worker-protest-dynamics-1918`** [`SCH-churakov-dmitry`(德米特里·奥列戈维奇·丘拉科夫) | pp. 84-88, 352-355]: 
- **`CLM-churakov-2004-izhevsk-votkinsk-worker-insurrection`** [`SCH-churakov-dmitry`(德米特里·奥列戈维奇·丘拉科夫) | pp. 258-285, 290-298, 304-325]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-mozokhin-cheka-to-ogpu-extrajudicial-jurisdiction-1918-1929`** [`SCH-mozokhin-oleg`(奥列格·莫佐欣) | PDF pp. 8-36, 44-49, 117-136]: 
- **`CLM-zemskov-1920s-archival-repression-scale-before-1930`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | PDF pp. 199-200, 210-214, 220-221 (原书 pp. 197-198, 208-212, 218-219)]: 
- **`CLM-rabinowitch-2007-constituent-assembly`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 88-91, 105-110, 121-127]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-getzler-1967-martov-soviet-opposition`** [`SCH-getzler-israel`(伊斯雷尔·格茨勒) | pp. 168-191]: 
- **`CLM-roobol-1976-tsereteli-tragedy-of-moderation`** [`SCH-roobol-wh`(W·H·罗博尔) | pp. 39, 253–257 (printed page = PDF page − 10). Narrative evidence for 1907 and 1917 runs through pp. 32–65 and pp. 81–182; those pages are not all quoted here.]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
