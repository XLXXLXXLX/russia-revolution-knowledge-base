# 1-Hop 去重平衡上下文包：`ORG-komuch-and-democratic-counterrevolution`

> 由 `python scripts/kb.py pack` 动态编译：保留 **100% 一跳邻居与多时段关系边**，跨卡自动去重争鸣与时间线，并关联学者学派 (`SCH-*`)。

## 0. 认知完备度与反偏斜仪表盘
- **`ORG-komuch-and-democratic-counterrevolution`** (萨马拉立宪会议成员委员会（Комуч）与乌法督政府 | `cards/organizations/ORG-komuch-and-democratic-counterrevolution.md` | `multi-perspective`): 已覆盖=`democratic-socialist-radkey, military-structural-mawdsley, bolshevik-local-archive-rabinowitch`；待补=`volga-peasant-oral-history, czechoslovak-legion-czech-archives`

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
1918年6月8日社会革命党人在捷克军团占领萨马拉后建立“立宪会议成员委员会”（Комуч），9月23日在乌法合组五人全俄临时政府（乌法督政府），试图构建独立于红白之间的“民主反革命”。因强征农民、依赖旧军官“保护色”并遭左右夹击，终在1918年11月18日高尔察克政变中覆灭。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **捷克军团兵变与萨马拉科穆奇建立（`1918-05` 至 `1918-06-08`）**：`1918-05` 下旬捷克斯洛伐克军团沿西伯利亚大铁路暴动并迅速控制伏尔加河重镇。`1918-06-08` 军团攻占萨马拉后，以沃尔斯基（V. K. Volsky）等5名社革党立宪会议议员为核心成立**立宪会议成员委员会（Комуч）**（成员后扩至百余人，绝大部分为社革党人，含极少数孟什维克）。科穆奇宣布废除人民委员会政令、解散革命法庭与苏维埃，恢复新闻集会自由、地方自治局（*zemstva*）、8小时工作制与银行商业运转，同时表面保留农民对既得土地的占有，一度控制萨马拉、辛比尔斯克、喀山（`08-07` 攻克，内藏帝国黄金储备）与乌法等省区。
- **重建东线、军官“保护色”与农民疏离（`1918-06` 至 `1918-09`）**：科穆奇虽因布尔什维克征粮队与贫农委员会（*комбеды*）的农村政策而获得暂时的农民中立或同情，却随即颁令重启对德“东线”并依靠旧沙皇军官团（如卡佩尔等“人民军”指挥官）实行带有“亚历山大三世时代心态”的强制征兵与惩罚性军纪，瞬间抵消了农民对红军的反感。因自身在十月后丧失士兵基础，科穆奇不得不依赖图谋“保护色”的右翼军官（秘密军官网中保皇派远超亲民主派），一旦战局吃紧即在 `1918-09-10` 失守喀山、`09-12` 失守辛比尔斯克，且与保守派主导的鄂木斯克**西伯利亚临时政府**（PSG，6月23日成立）爆发关税与主权内耗。
- **乌法国务会议与五人督政府的双重撕裂（`1918-09-08` 至 `1918-11-18`）**：在协约国及捷克军团调停施压下，反布尔什维克各派于 `1918-09-08` 至 `09-23` 召开乌法国务会议，达成妥协组建五人**全俄临时政府（乌法督政府）**：两名社革党人（阿夫克森齐耶夫、津季诺夫）与三名非社会主义右翼/中间派（西伯利亚总理沃洛戈茨基、军官博尔德列夫及立宪民主党人维诺格拉多夫），并被迫迁往右翼武装盘踞的鄂木斯克。随后切尔诺夫发表公开信（*Chernov's circular*）号召重归“委员会统治”并严厉抨击右翼，激起西伯利亚哥萨克与反动军官团极度恐慌；而左翼又痛恨督政府迁就右派且背离立宪会议纯洁性。
- **高尔察克鄂木斯克政变与“民主反革命”终结（`1918-11-18`）**：`1918-11-04` 刚出任督政府陆海军部长的原黑海舰队司令高尔察克（A. V. Kolchak），在地方右翼文官、哥萨克与驻鄂木斯克军官团策动下（据Mawdsley，英军于11月18日护卫部长会议以阻止反政变；诺克斯似已知情而未阻止，作者未发现协约国直接参与政变的证据），于 `1918-11-17` 夜间至 `11-18` 晨逮捕两名社革党执政官阿夫克森齐耶夫与津季诺夫并强行推举高尔察克为“最高执政”（*Верховный правитель*），博尔德列夫抗议离职，逃往叶卡捷琳堡企图复会的科穆奇残部亦遭军队驱散。伏尔加—西伯利亚反布尔什维克阵营的民主联合政府实验遭军事独裁取代；其他地区的非红白力量并未因此消失。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-psr` | `main-political-sponsor` | 1918.06–11 | 科穆奇为正统社革党在伏尔加河建立的最重要政权实验，同时暴露该党右翼保守化与切尔诺夫中派领袖瘫痪的深层病灶 | `CLM-smith-scott-2011-psr-third-force-collapse` (Radkey 1963) |
| `PER-chernov` | `nominal-leader-then-spoiler` | 1918.09–10 | 作为立宪会议主席在乌法会议后发表激烈通告抨击右翼合作派，无意中为鄂木斯克军官集团发动反社会主义政变提供了口实 | Mawdsley 1987 `ch12#L353-L364`; Radkey 1963 |
| `ORG-kadets` | `uneasy-coalition-to-coup-ally` | 1918.06–11 | 在东线与乌法督政府中与右翼社革党勉强合作，旋即因厌恶“委员会政治”与社革党纲领而配合高尔察克右翼军事独裁 | `CLM-smith-scott-2011-psr-third-force-collapse`; Mawdsley 1987 `ch12` |
| `PER-kolchak` | `war-minister-to-coup-usurper` | 1918.11 | 11月4日入阁任督政府陆海军部长，11月18日借鄂木斯克哥萨克与军官政变取代督政府出任白军“最高执政” | Mawdsley 1987 `ch12#L374-L453`; `CLM-mawdsley-1987-white-movement-structural-defeat` |
| `EVT-1918-01-constituent-assembly-dispersal` | `legitimacy-charter` | 1918.06–11 | 科穆奇以1917年11月普选产生的立宪会议唯一合法继承者自居，但农民因已得土地且畏惧重启战端并未起兵响应其号召 | `CLM-smith-scott-2011-psr-third-force-collapse` (Radkey 1963) |
| `EVT-1918-worker-protest-and-izhevsk-uprising` | `allied-regional-insurgency` | 1918.08–11 | 卡马河畔伊热夫斯克起义建制与萨马拉科穆奇/乌法督政府并轨后，9月起废除苏维埃、实施强征减薪，反向疏离当地军工群众 | `CLM-churakov-2004-izhevsk-votkinsk-worker-insurrection` |
| `EVT-1918-1920-russian-civil-war` | `third-force-collapse-pivot` | 1918.06–11 | 科穆奇兴衰体现东部反布尔什维克阵营向军事独裁转变，其他地区仍有独立武装 | Mawdsley 1987 `ch09`, `ch12`; `CLM-mawdsley-1987-civil-war-militarized-regime` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：科穆奇并非由社革党独立军事起义建立，而是依托捷克斯洛伐克军团沿铁路线夺权建立的文官政权；其在农民动员上未能兑现民主选票优势，1918年11月高尔察克政变终结了伏尔加—西伯利亚的民主联合政府实验。
- **主要解释分歧**（详参 `DEB-1918-constituent-assembly-and-soviet-democracy`, `DEB-1918-red-terror-and-civil-war-origins` 及 `DEB-1918-democratic-counterrevolution-third-force` `(待建)`）：
  - **[民粹主义政党内因批判 / Oliver H. Radkey (1963)]**（馆藏误标为 `CLM-smith-scott-2011-psr-third-force-collapse`，实为 Radkey 1963 *The Sickle under the Hammer*）：论证科穆奇并非死于外敌强大，而死于社革党自身的结构性异化——农民关心土地而非抽象宪政，科穆奇重开东线并纵容旧沙皇军官用“亚历山大三世式”粗暴方式强征农民，以“战争狂热”抵消了苏维埃征粮队的恶感；自身无兵使“保护色”寄生其下的白卫军官一俟羽翼丰满便踢开社革党东道主。
  - **[内战军事—制度结构派 / Evan Mawdsley (1987)]**（`CLM-mawdsley-1987-white-movement-structural-defeat`, `CLM-mawdsley-1987-civil-war-militarized-regime`, `mawdsley_1987_civil_war/ch09, ch12`）：指出1918年夏红白双方的野战动员都极端薄弱，是 **1917年“拒绝妥协的教训”**（右翼视社革党无异于布尔什维克、社革党视右翼为纯粹反革命）与俄国文官政治传统脆弱，使民主联合内阁在严酷内战中面临驾驭旧军官团和抵御红军的重大制约；这不能证明未发生政变时的必然结局。
  - **[苏联正统叙事]**：将科穆奇与乌法督政府定性为充当英法美协约国帝国主义与捷克干涉军附庸、替白军军阀清场的“反革命小资产阶级屏风（ширма）”，认为其从第一天起即注定让位于公开的高尔察克军事独裁。

## 2. 一跳邻域全量微摘要目录 (去重后共 8 个节点，0 截断)
- **`CON-constituent-assembly`**（立宪会议（全俄立宪会议））: 自1879年民意党起，立宪会议成为反对派共享的民主合法性象征。1917年临时政府拖延选举；11月社革党获多数，布尔什维克掌两京与近卫战线优势。1918-01-05/06[O.S.]/01-18/19[N.S.]开会一夜即遭武力解散，夏秋成为萨马拉立宪会议委员委员会的内战旗帜。 ‖ `→ORG-komuch-and-democratic-counterrevolution`[civil-war-afterlife-banner|1918-06-08–1918-11-18]: 萨马拉立宪会议委员试图开辟反布反白“第三条道路”，终在农民冷漠与高尔察克政变中覆亡
- **`EVT-1918-1920-russian-civil-war`**（俄国内战（1918–1920））: 1918至1920年红白主战场的内战中，布尔什维克依托中央腹地、军火遗产与铁路机动击败分散白军；征粮和恐怖又激起工农反抗。乌克兰及外高加索的民族国家竞争不能归入简单红白对决，克里米亚撤离仅标志主要白军战线收束，边疆与农民战争仍在延续。 ‖ `→ORG-komuch-and-democratic-counterrevolution`[democratic_third_force|1918.06—11]: 立宪会议路线受红白夹击，并在高尔察克政变中丧失独立执政空间 ； `←ORG-komuch-and-democratic-counterrevolution`[third-force-collapse-pivot|1918.06–11]: 科穆奇兴衰体现东部反布尔什维克阵营向军事独裁转变，其他地区仍有独立武装
- **`EVT-1918-worker-protest-and-izhevsk-uprising`**（1918年苏俄工人抗议、工厂全权代表会议运动与伊热夫斯克—沃特金斯克大起义）: 1918年春夏，失业、饥荒与基层组织国家化引发工人抗议，丘拉科夫估涉及210—220家企业、10万—25万人。彼得格勒形成非常代表会议，莫斯科局部让步；卡马河军工镇在强征等冲突下起义，伊热夫斯克与沃特金斯克组成人民军，最高约2.5万人，终遭红军反攻瓦解。 ‖ `→ORG-komuch-and-democratic-counterrevolution`[allied-then-alienating-patron|1918.08–11]: 卡马河畔起义政权与萨马拉科穆奇/乌法督政府并轨后废除苏维埃、实施强征与减薪，导致工人自治诉求在军事极化中瓦解 ； `←ORG-komuch-and-democratic-counterrevolution`[allied-regional-insurgency|1918.08–11]: 卡马河畔伊热夫斯克起义建制与萨马拉科穆奇/乌法督政府并轨后，9月起废除苏维埃、实施强征减…
- **`ORG-psr`**（社会革命党）: 1901年末合并建立的俄国新民粹派政党，以土地社会化纲领与战斗组织暗杀闻名。1917年选民基数居全俄之冠却在战争、分地拖延与左翼分裂中失势；虽夺立宪会议多数仍遭解散，内战“第三条道路”溃于高尔察克政变，1922年莫斯科公审后在国内覆灭。 ‖ `←ORG-komuch-and-democratic-counterrevolution`[main-political-sponsor|1918.06–11]: 科穆奇为正统社革党在伏尔加河建立的最重要政权实验，同时暴露该党右翼保守化与切尔诺夫中派领… ； `→ORG-komuch-and-democratic-counterrevolution`[third_force_regime|1918-06–1918-11]: 在萨马拉重建民主宪政政府抗衡红白两极，因征兵失民心且受白军军官架空而亡
- **`PER-chernov`**（维克托·切尔诺夫）: 俄国社会革命党创始人兼首席理论家，“土地社会化”纲领制定者。早期纵容阿泽夫战斗组织并在1909年丑闻后陷于党务瘫痪；1917年任联合内阁农业部长进退维谷，1918年1月以244:153当选全俄立宪会议一日主席即遭驱散，萨马拉—乌法“第三力量”亦破产，后流亡欧美。 ‖ `←ORG-komuch-and-democratic-counterrevolution`[nominal-leader-then-spoiler|1918.09–10]: 作为立宪会议主席在乌法会议后发表激烈通告抨击右翼合作派，无意中为鄂木斯克军官集团发动反社… ； `→ORG-komuch-and-democratic-counterrevolution`[party-patriarch-and-critic|1918.06–11]: 依托全俄立宪会议法统维系“第三力量”，但未在萨马拉—乌法压住右翼党僚与白军，终遭 PER-kolchak 政变倾覆
- **`ORG-kadets`**（立宪民主党（卡德特党））: 1905年10月从解放同盟诞生的俄国自由主义核心政党，主张四尾制宪、有偿征地与议会道路，曾主导前两届杜马与战时进步同盟。1917年二月主导首届临时政府并切断对杜马从属关系，旋因战争、土地危机及科尔尼洛夫事件退阁丧失民心，十月后被定为“人民公敌”并在内战与流亡中分裂。 ‖ `←ORG-komuch-and-democratic-counterrevolution`[uneasy-coalition-to-coup-ally|1918.06–11]: 在东线与乌法督政府中与右翼社革党勉强合作，旋即因厌恶“委员会政治”与社革党纲领而配合高尔…
- **`PER-kolchak`**（亚历山大·高尔察克）: 俄国海军上将与西伯利亚白军最高统帅（1874—1920）。曾任黑海舰队司令；1918年11月18日鄂木斯克政变推翻社革党督政府自任“全俄最高执政”，终结民主反革命第三条道路；1919年春攻遭伏龙芝红军击溃，后方游击战与腐败加剧总崩溃，1920年2月7日在伊尔库茨克被处决。 ‖ `←ORG-komuch-and-democratic-counterrevolution`[war-minister-to-coup-usurper|1918.11]: 11月4日入阁任督政府陆海军部长，11月18日借鄂木斯克哥萨克与军官政变取代督政府出任白… ； `→ORG-komuch-and-democratic-counterrevolution`[regime-terminator|1918.11]: 以军事独裁终结伏尔加—乌法“民主反革命”第三条道路，使社革“保护色”政治彻底破产
- **`EVT-1918-01-constituent-assembly-dispersal`**（1918年1月全俄立宪会议召开与解散）: 1918年1月5—6日（俄历；公历1月18—19日），立宪会议召开唯一常会，切尔诺夫以244∶153当选主席。议会拒认苏维埃最高权，布党与左社退场，水兵勒令散会，中执委正式解散。全国普选与两京武装核心的政治支持结构由此正面断裂。 ‖ `←ORG-komuch-and-democratic-counterrevolution`[legitimacy-charter|1918.06–11]: 科穆奇以1917年11月普选产生的立宪会议唯一合法继承者自居，但农民因已得土地且畏惧重启…

## 3. 关联史学争鸣与学者论断索引 (主卡外关联争鸣 3 项)
- **`DEB-1918-constituent-assembly-and-soviet-democracy`**（解散立宪会议与多党苏维埃民主的命运 | `historiography/debates/DEB-1918-constituent-assembly-and-soviet-democracy.md` | 流派 `liberal-totalitarian, revisionist, sr-electoral-political-history, menshevik-history, security-legal-history`）：1918年立宪会议被武力解散，是否意味着一党统治已不可避免？争论涉及普选制宪与阶级性苏维埃两种合法性、群众动员和镇压，以及此后左翼多党合作与体制内反对派仍有多少政治空间。
- **`DEB-1918-red-terror-and-civil-war-origins`**（红色恐怖、契卡扩张与内战期一党专政起源之争（1918–1921） | `historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md` | 流派 `liberal-continuity, institutional-cheka, contingency-coalition, local-violence-and-chronicle, repressed-socialists-and-worker-protest, civil-war-structure-and-total-war, post-soviet-archival-quantitative`）：红色恐怖和契卡法外权力是列宁主义政治逻辑的必然结果，还是内战、粮食危机、联盟破裂与地方暴力交织下的制度选择？中央命令与地方自主行动怎样互相强化？恐怖升级、社会主义对手遭镇压和一党统治形成各有不同时间线，不能压缩成同一事件。
- **`DEB-1918-democratic-counterrevolution-third-force`**（科穆奇、乌法督政府与民主反革命何以覆灭 | `historiography/debates/DEB-1918-democratic-counterrevolution-third-force.md` | 流派 `radkey-party-dilemma, military-geopolitical-structure, worker-third-force, soviet-orthodoxy`）：1918年伏尔加—西伯利亚的科穆奇与乌法督政府，何以未能维持一条独立于布尔什维克与军事右翼的道路？“民主反革命”指向其反布尔什维克及立宪代表制的政治组合，并不意味着这些政府内部、其社会支持者或所有反红力量均有相同目标。

### 3.1 关联核心论断与史学家学派坐标 (`CLM-*` → `SCH-*`, 展示前 24/24 条)
- **`CLM-smith-scott-2011-psr-third-force-collapse`** [`SCH-radkey-oliver`(奥利弗·亨利·拉德基) | pp. 452-455, 467-473, 490-493 (PDF pp. 468-471, 483-489, 506-509)]: 
- **`CLM-mawdsley-1987-white-movement-structural-defeat`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 212–218, 272–276, 286–289]: 
- **`CLM-churakov-2004-izhevsk-votkinsk-worker-insurrection`** [`SCH-churakov-dmitry`(德米特里·奥列戈维奇·丘拉科夫) | pp. 258-285, 290-298, 304-325]: 
- **`CLM-mawdsley-1987-civil-war-militarized-regime`** [`SCH-mawdsley-evan`(埃文·莫兹利) | pp. 328, 331, 346-347]: 
- **`CLM-rabinowitch-2007-constituent-assembly`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 88-91, 105-110, 121-127]: 
- **`CLM-rabinowitch-2007-contingency-of-dictatorship`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. xi-xii, 390-398]: 
- **`CLM-rabinowitch-2007-left-sr-coalition-collapse`** [`SCH-rabinowitch-alexander`(亚历山大·拉比诺维奇) | pp. 274-282, 287-309, 395-396]: 
- **`CLM-pipes-1990-october-classic-coup`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 11 (The October Coup); cf. Introduction]: 
- **`CLM-pipes-1990-red-terror-leninist-logic`** [`SCH-pipes-richard`(理查德·派普斯) | ch. 18 (The Red Terror)]: 
- **`CLM-getzler-1967-martov-soviet-opposition`** [`SCH-getzler-israel`(伊斯雷尔·格茨勒) | pp. 168-191]: 
- **`CLM-roobol-1976-tsereteli-tragedy-of-moderation`** [`SCH-roobol-wh`(W·H·罗博尔) | pp. 39, 253–257 (printed page = PDF page − 10). Narrative evidence for 1907 and 1917 runs through pp. 32–65 and pp. 81–182; those pages are not all quoted here.]: 
- **`CLM-mozokhin-cheka-to-ogpu-extrajudicial-jurisdiction-1918-1929`** [`SCH-mozokhin-oleg`(奥列格·莫佐欣) | PDF pp. 8-36, 44-49, 117-136]: 
- **`CLM-leggett-1981-vecheka-extra-legal-origins`** [`SCH-leggett-george`(乔治·莱格特) | pp. 17-22, 47-49 (PDF pp. 55-60, 85-87)]: 
- **`CLM-leggett-1981-red-terror-institutionalization`** [`SCH-leggett-george`(乔治·莱格特) | pp. 56-59, 102-115, 144-145 (PDF pp. 94-97, 140-153, 182-183)]: 
- **`CLM-leggett-1981-cheka-to-gpu-continuity`** [`SCH-leggett-george`(乔治·莱格特) | pp. 339-352, 355-363 (PDF pp. 377-390, 393-401)]: 
- **`CLM-raleigh-2001-local-bolshevik-violence-and-clientelism`** [`SCH-raleigh-donald`(唐纳德·J·罗利) | Local PDF pp. 104, 112–130; English print pagination not verified]: 
- **`CLM-cheka-chronicle-hostage-and-local-autonomy`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | EPUB OPS/ch1-6.xhtml; OPS/ch1-10.xhtml; OPS/ch1-14.xhtml; OPS/ch1-15.xhtml; OPS/ch1-16.xhtml; OPS/ch1-19.xhtml（提取文本无印刷页码）]: 
- **`CLM-cheka-chronicle-suppression-of-socialist-rivals`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | EPUB OPS/ch1-4.xhtml; OPS/ch1-5.xhtml; OPS/ch1-9.xhtml; OPS/ch1-10.xhtml; OPS/ch1-15.xhtml; OPS/ch1-16.xhtml（提取文本无印刷页码）]: 
- **`CLM-plekhanov-am-dzerzhinsky-cheka-institutionalization`** [`SCH-ratkovsky-ilya`(伊利亚·拉特科夫斯基) | pp. 55-56, 97-106, 118-123, 147-155, 209-211, 228]: 
- **`CLM-halle-1920-martov-critique-of-terror-and-21-conditions`** [`SCH-martov-iulii`(尤利·奥西波维奇·马尔托夫 · participant-primary-text) | pp. 167–170, 173, 175–176, 179 (Lih translation in the 2011 Lewis/Lih edition; printed page = PDF page − 1). Full speech pp. 167–179, delivered 15 October 1920 [N.S.]]: 
- **`CLM-churakov-2004-soviet-worker-protest-dynamics-1918`** [`SCH-churakov-dmitry`(德米特里·奥列戈维奇·丘拉科夫) | pp. 84-88, 352-355]: 
- **`CLM-hoffmann-2011-continuum-of-total-war-1914-1929`** [`SCH-hoffmann-david`(大卫·L·霍夫曼) | pp. 12–13, 38, 127–128]: 
- **`CLM-zemskov-1920s-archival-repression-scale-before-1930`** [`SCH-zemskov-viktor`(维克托·尼古拉耶维奇·泽姆斯科夫) | PDF pp. 199-200, 210-214, 220-221 (原书 pp. 197-198, 208-212, 218-219)]: 

## 4. 关联时间线骨干锚点 (L0–L2 展示 0 条)
