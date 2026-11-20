# 1-Hop 去重平衡上下文包：`EVT-1922-sr-show-trial`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`EVT-1922-sr-show-trial`** (1922年莫斯科社会革命党公开大审判 | `cards/events/EVT-1922-sr-show-trial.md` | `multi-perspective`): 已覆盖=`archival-post-soviet-mozokhin, liberal-institutional-pipes, democratic-socialist-radkey, bolshevik-prosecution-discourse`；待补=`scott-b-smith-2011-monograph-unextracted, second-international-archives`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1922年6月8日至8月7日苏俄最高革命法庭在莫斯科圆柱大厅公审戈茨等社革党中央委员，卢那察尔斯基、波克罗夫斯基与布哈林出庭控诉，第二国际辩护团遭扰退庭。法院判处死刑但由全俄中央执委会“缓期执行”人质化，三日后设立行政流放特别委员会，形成公开剧场与秘密法外镇压的双钳联动。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **审判筹备、政治局控制与“双重历史时刻”（`1922-02` 至 `1922-06-08`）**：`1922-02-06` 契卡改组格别乌（GPU）仅九日后（`02-15`），俄共（布）中央政治局即确立对 GPU 重大案件与最终判决的控制权。柏林三国国际会议上布尔什维克代表虽口头承诺不判死刑且允许外国社会主义律师出庭辩护，但列宁事后痛批让步过多。`1922-06-08` 最高革命法庭在莫斯科工会大厦圆柱大厅正式开庭（审判由皮亚塔科夫主持，克雷连科与卢那察尔斯基、波克罗夫斯基、布哈林等任公诉人）；**同日**政治局通过温什利赫特起草的全面管制令，禁止未经批准召开医生、农艺师、律师等“专家”全俄代表大会并启动筹建行政流放“特别会议”（`Mozokhin`）。
- **第二国际辩护团风波与控辩话语交锋（`1922-06` 至 `1922-08`）**：比利时社会党领袖埃米尔·王德威尔得（Émile Vandervelde）、德国独立社民党人库尔特·罗森菲尔德（Kurt Rosenfeld）与特奥多尔·李卜克内西（Theodor Liebknecht）赴莫斯科为戈茨（A. R. Gotz）、季莫费耶夫（E. M. Timofeev）、根德尔曼（M. Ia. Gendelman）、拉科夫（D. F. Rakov）、叶夫根尼娅·拉特纳（Eugenia Ratner）等第一组12名社革党中央委员辩护；但面对当局在庭内外组织的群众示威、“伪工人代表团”冲击法庭与限制辩护权，外国律师于6月中旬抗议退庭。庭上控方借转为污点证人的前战斗组织成员 G. I. 谢苗诺夫（Semenov）与格里戈里·拉特纳（Gregory Ratner）指控社革党在1918—1921年策划暗杀、白卫兵变与暴动；布哈林把社革党领袖比附为法国大革命的“百万富翁吉伦特派”，波克罗夫斯基则断言其自1917年起已非革命政党。
- **“暂缓执行死刑人质化”与法外流放机器无缝衔接（`1922-08-07` 至 `1924-03`）**：`1922-08-07` 法庭宣布判处戈茨等12名核心被告死刑（另有若干被告获减刑或赦免，倒戈证人获轻判），随即在**次日**（`08-08`）由全俄中央执委会（VTsIK）宣布**“暂缓执行死刑”**——明确声明若国内外社革党继续任何武装颠覆或恐怖活动，立即执行枪决，从而把在押中委集体人质化。仅仅**三天后**（`1922-08-10`），VTsIK 主席团正式颁布仿自沙皇亚历山大三世 `1881` 年《保卫国家秩序法》第34条的行政流放特别委员会法令（首先用于秋日“哲学家船”驱逐学者与医生农艺师异议者），并于 `1922-10-16` 与 `12-08` 授权 GPU 绕过法院直接将反苏政党积极分子（《刑法典》第60—63条）关入强制劳动营3年，最终制度化为 `1924-03-28` 的 OGPU 特别会议（ОСО）。国内有组织社会革命党随之终结。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-psr` | `organizational-liquidation` | 1922.06–08 | 审判剥夺其国内外革命道义合法性并拘禁/人质化全部国内核心中委，标志国内有组织社革党走向终结 | `CLM-smith-scott-2011-1922-sr-trial-discourse` (Radkey 1963) |
| `INS-cheka-gpu-ogpu` | `twin-pincer-extrajudicial-partner` | 1922.06–1924 | 公开公审制造舆论并“只办一次”，中下层社革党人与知识分子同步由08-10/10-16法令转交GPU秘密行政流放与关押 | `CLM-mozokhin-cheka-to-ogpu-extrajudicial-jurisdiction-1918-1929` |
| `INS-politburo-orgburo-secretariat` | `behind-scenes-director` | 1922.02–08 | 政治局自1922-02-15起垄断GPU大案方向，幕后统筹公审口径、群众游行压力及“死刑缓期人质化”政治裁决 | `CLM-mozokhin-cheka-to-ogpu-extrajudicial-jurisdiction-1918-1929`; Pipes ch23 |
| `PER-bukharin` | `ideological-prosecutor` | 1922.08 | 在公诉词（*Pravda* 08-04）中用经济决定论将戈茨、津季诺夫等打成“百万富翁操纵的吉伦特派与协约国傀儡” | `CLM-smith-scott-2011-1922-sr-trial-discourse` (Radkey 1963) |
| `PER-lunacharsky` | `prosecutor-debater` | 1922.08 | 在8月4日公诉中当庭驳斥戈茨“缺乏组党备战时间”的辩词，指出社革党比布尔什维克建党更早且在十月前掌权八月 | `CLM-smith-scott-2011-1922-sr-trial-discourse` (Radkey 1963) |
| `ORG-psr` | `chief-defendant-hostage` | 1922.06-08+ | 戈茨（A. R. Gotz）、季莫费耶夫等社革党中央被告为第一组主被告；戈茨将1918年萨马拉败绩归因于“缺少时间”，被判死缓并作为人质长期监禁 | `CLM-smith-scott-2011-1922-sr-trial-discourse` (Radkey 1963) |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1922年社革党审判是苏维埃政权首次举行的大型国际瞩目政治公审；被告方确曾在1918年内战期间组织或资助反布尔什维克武装（包括科穆奇），但审判程序与量刑完全服从布尔什维克最高政治考量，“缓期执行”兼具对境外社革党的威慑人质效应，并与同年8—10月行政流放法制相辅相成。
- **主要解释分歧**（详参 `DEB-1918-red-terror-and-civil-war-origins` 及 `DEB-1922-sr-trial-and-opposition-repression` / `DEB-cheka-to-stalinist-terror-continuity` `(待建)`）：
  - **[民主社会主义史学批判 / Oliver H. Radkey (1963)]**（馆藏误标为 `CLM-smith-scott-2011-1922-sr-trial-discourse`，实为 Radkey 1963 *The Sickle under the Hammer*）：既逐条戳穿被告戈茨、拉科夫、根德尔曼掩饰1917年背弃土地与和平承诺的自我欺骗辩护，又批驳布哈林“百万富翁吉伦特派”指控的粗鄙经济决定论（举证维索茨基、加夫龙斯基家族实属反战切尔诺夫派），指出右翼社革党真正动力源自地方自治局与合作社受薪知识分子的地位危机感与民族主义情结；同时肯定波克罗夫斯基“社革党1917年后不再革命”之论。
  - **[后苏联安全档案制度史 / Oleg Mozokhin (2006)]**（`CLM-mozokhin-cheka-to-ogpu-extrajudicial-jurisdiction-1918-1929`）：依据 `ЦА ФСБ РФ` 与 `АП РФ` 档案揭示 **1922-06-08（开庭）与 08-07/08-10（闭庭与流放令）的“双钳联动”**——苏联领导层（尤其是缅任斯基）深知公开审讯反易提高反抗者声望，故只以高规格公审摧毁社革党领袖道统，而将成千上万中小党徒与专家（如全俄医生代表大会）交由 GPU/OGPU 特别会议与“减六”机制无声清除，令法院沦为政治局的“遮羞布”。
  - **[自由-极权连续性学派 / Richard Pipes (1990)]**（`pipes_1990_russian_rev/ch23`）：强调该案是“苏维埃历史上首次政治作秀公审（show trial）”，开创了由最高政治权威预先定性、组织群众街垒请愿施压、利用变节证人、迫使外国辩护人离席并为1936—1938年莫斯科大审判提供全套剧本范式的先河。
  - **[苏维埃官方辩护叙事]**：将公审视为针对1918—1921年投靠白卫军、暗杀列宁与沃洛达尔斯基并勾结帝国主义干涉者的反革命恐怖集团的正当革命正义，称缓刑体现了胜利无产阶级政权的宽大与人道。

## 2. 一跳邻域全量微摘要目录 (去重后共 6 个节点，0 截断)
- **`ORG-psr`**（社会革命党）: 1901年末合并建立的俄国新民粹派政党，以土地社会化纲领与战斗组织暗杀闻名。1917年选民基数居全俄之冠却在战争、分地拖延与左翼分裂中失势；虽夺立宪会议多数仍遭解散，内战“第三条道路”溃于高尔察克政变，1922年莫斯科公审后在国内覆灭。 ‖ `←EVT-1922-sr-show-trial`[organizational-liquidation|1922.06–08]: 审判剥夺其国内外革命道义合法性并拘禁/人质化全部国内核心中委，标志国内有组织社革党走向终结 ； `←EVT-1922-sr-show-trial`[chief-defendant-hostage|1922.06-08+]: 戈茨（A. R. Gotz）、季莫费耶夫等社革党中央被告为第一组主被告；戈茨将1918年… ； `→EVT-1922-sr-show-trial`[domestically_liquidated_at|1922-06–1922-08]: 布尔什维克首场大型政治作秀公审，以“人质缓死”机制彻底瘫痪国内社革党残余中枢
- **`INS-cheka-gpu-ogpu`**（全俄肃反委员会—国家政治保卫局与总局（ВЧК–ГПУ–ОГПУ 制度档案））: 苏维埃政治警察谱系：1917年12月人民委员会内部决议创立契卡，1918年红色恐怖中央地行刑权演变；1922年改为苏俄内务部GPU，1923年设联盟OGPU，随后重建法外特别会议。机关兼事工农情绪监测与镇压，在1927年战争恐慌、沙赫特案及1928—1929年强征中作用关键。 ‖ `←EVT-1922-sr-show-trial`[twin-pincer-extrajudicial-partner|1922.06–1924]: 公开公审制造舆论并“只办一次”，中下层社革党人与知识分子同步由08-10/10-16法令… ； `→EVT-1922-sr-show-trial`[staged-and-supplemented|1922.06-10]: 在莫斯科公开审判社革党中委并判处缓期死刑充当人质的同时，于8月与10月同步建立GPU法外行政流放与劳改营特别委员会。
- **`INS-politburo-orgburo-secretariat`**（联共（布）中央政治局—组织局—书记处与官职等级名册制）: 1919年3月俄共八大后常设政治局、组织局与书记处，分掌政治决策、组织行政及日常党务人事。1922年4月斯大林任总书记后逐步控制议程、秘密文件分发与干部名册调配。经1924年七人小组协调、1925—1929年联盟重组与纪律整肃，托洛茨基、季诺维也夫、布哈林先后退出决策核心。 ‖ `←EVT-1922-sr-show-trial`[behind-scenes-director|1922.02–08]: 政治局自1922-02-15起垄断GPU大案方向，幕后统筹公审口径、群众游行压力及“死刑…
- **`PER-bukharin`**（尼古拉·布哈林）: 布尔什维克核心理论家、《真理报》主编及共产国际书记处负责人。列宁遗嘱誉其“全党宠儿”但质疑其辩证法；1918年领衔左翼共产主义，1921年后转向新经济政策均衡路线，1925–1927联斯大林击溃左派，1928–1929因反对暴力征粮与超工业化遭击败并逐出政治局。 ‖ `←EVT-1922-sr-show-trial`[ideological-prosecutor|1922.08]: 在公诉词（*Pravda* 08-04）中用经济决定论将戈茨、津季诺夫等打成“百万富翁操… ； `→EVT-1922-sr-show-trial`[prosecutor|1922.06–08]: 作为布尔什维克控方理论家撰写并宣讲社革党“百万富翁操纵的伪革命吉伦特派”阶级还原论控词
- **`PER-lunacharsky`**（阿纳托利·卢那察尔斯基）: 俄国革命文艺理论家、首任苏俄教育人民委员（1875—1933）。早年与波格丹诺夫、高尔基共倡“造神说”并组前进派党校；1917年随区联派入布尔什维克，十月后长期主持教育与文化事业，在保护旧知识分子、实验教育与激进派间力求平衡；1929年大转变高潮中辞职，1933年病逝法国。 ‖ `←EVT-1922-sr-show-trial`[prosecutor-debater|1922.08]: 在8月4日公诉中当庭驳斥戈茨“缺乏组党备战时间”的辩词，指出社革党比布尔什维克建党更早且… ； `→EVT-1922-sr-show-trial`[prosecution-ideologue|1922.06–08]: 在社革党中央公开审判中任布尔什维克控方理论家与政治发言人（非首席公诉人克雷连科），在审判中驳斥戈茨（相关言论见1922年8月4日《真理报》）
- **`PER-chernov`**（维克托·切尔诺夫）: 俄国社会革命党创始人兼首席理论家，“土地社会化”纲领制定者。早期纵容阿泽夫战斗组织并在1909年丑闻后陷于党务瘫痪；1917年任联合内阁农业部长进退维谷，1918年1月以244:153当选全俄立宪会议一日主席即遭驱散，萨马拉—乌法“第三力量”亦破产，后流亡欧美。 ‖ `→EVT-1922-sr-show-trial`[absent-targeted-leader|1922]: 时已流亡布拉格，在1922年莫斯科社革党公审中缺席成为布哈林等控方“百万富翁吉伦特派”叙事的核心靶子

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 4 项)
- **`DEB-1918-red-terror-and-civil-war-origins`**（红色恐怖、契卡扩张与内战期一党专政起源之争（1918–1921） | `historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md` | 流派 `liberal-continuity, institutional-cheka, contingency-coalition, local-violence-and-chronicle, repressed-socialists-and-worker-protest, civil-war-structure-and-total-war, post-soviet-archival-quantitative`）：红色恐怖和契卡法外权力是列宁主义政治逻辑的必然结果，还是内战、粮食危机、联盟破裂与地方暴力交织下的制度选择？中央命令与地方自主行动怎样互相强化？恐怖升级、社会主义对手遭镇压和一党统治形成各有不同时间线，不能压缩成同一事件。
- **`DEB-1918-constituent-assembly-and-soviet-democracy`**（解散立宪会议与多党苏维埃民主的命运 | `historiography/debates/DEB-1918-constituent-assembly-and-soviet-democracy.md` | 流派 `liberal-totalitarian, revisionist, sr-electoral-political-history, menshevik-history, security-legal-history`）：1918年立宪会议被武力解散，是否意味着一党统治已不可避免？争论涉及普选制宪与阶级性苏维埃两种合法性、群众动员和镇压，以及此后左翼多党合作与体制内反对派仍有多少政治空间。
- ⚠️ 引用了尚未创建的争鸣卡 `DEB-1922-sr-trial-and-opposition-repression`
- ⚠️ 引用了尚未创建的争鸣卡 `DEB-cheka-to-stalinist-terror-continuity`

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/24 条)
- **`CLM-smith-scott-2011-1922-sr-trial-discourse`** [`SCH-radkey-oliver`(奥利弗·亨利·拉德基) | pp. 466-469, 477-480, 494-495, 500-506 (PDF pp. 482-485, 493-496, 510-511, 516-522)]: 
- **`CLM-mozokhin-cheka-to-ogpu-extrajudicial-jurisdiction-1918-1929`** [`SCH-mozokhin-oleg`(奥列格·莫佐欣) | PDF pp. 8-36, 44-49, 117-136]: 
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
- **`CLM-churakov-2004-soviet-worker-protest-dynamics-1918`** [`SCH-churakov-dmitry`(德米特里·奥列戈维奇·丘拉科夫) | pp. 84-88, 352-355]: 
- **`CLM-churakov-2004-izhevsk-votkinsk-worker-insurrection`** [`SCH-churakov-dmitry`(德米特里·奥列戈维奇·丘拉科夫) | pp. 258-285, 290-298, 304-325]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-zemskov-1920s-archival-repression-scale-before-1930`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | PDF pp. 199-200, 210-214, 220-221 (原书 pp. 197-198, 208-212, 218-219)]: 
- **`CLM-rabinowitch-2007-constituent-assembly`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 88-91, 105-110, 121-127]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-getzler-1967-martov-soviet-opposition`** [`SCH-getzler-israel`(伊斯雷尔·格茨勒) | pp. 168-191]: 
- **`CLM-roobol-1976-tsereteli-tragedy-of-moderation`** [`SCH-roobol-wh`(W·H·罗博尔) | pp. 39, 253–257 (printed page = PDF page − 10). Narrative evidence for 1907 and 1917 runs through pp. 32–65 and pp. 81–182; those pages are not all quoted here.]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
