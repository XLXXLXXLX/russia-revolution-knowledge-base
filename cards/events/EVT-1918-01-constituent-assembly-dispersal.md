---
id: EVT-1918-01-constituent-assembly-dispersal
type: event
title: 1918年1月全俄立宪会议召开与解散
names:
  ru: Российское учредительное собрание (роспуск 6 (19) января 1918 г.)
  en: Convocation and Dispersal of the All-Russian Constituent Assembly
  aliases: ["立宪会议解散", "塔夫利达宫立宪会议", "1918年立宪会议"]
dates:
  start_ns: "1918-01-18"
  end_ns: "1918-01-19"
coverage_status: draft
perspectives_present: ["archival-rabinowitch", "liberal-totalitarian-pipes", "populist-structural-hildermeier", "soviet-orthodox"]
perspectives_missing: ["provincial-deputy-networks", "ukrainian-assembly-parallel"]
related_debates: ["DEB-1918-constituent-assembly-and-soviet-democracy", "DEB-1917-october-coup-or-social-revolution"]
updated_at: "2026-11-18"
---

## [T1] 60秒定性微摘要
1918年1月5–6日（俄历）/1月18–19日（公历），全俄立宪会议在塔夫利达宫召开唯一常会，社革党切尔诺夫以244:153当选主席。5日白天保卫立宪会议游行在利捷伊内大街遭枪击（15至21人死亡），6日凌晨水兵卫队勒令清场关闭，西方式多党议会制尝试终结。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **延宕选举与布尔什维克党内斗争（1917.11–12）**：1917年11—12月完成的立宪会议普选中，各派社会革命党（含乌克兰等民族社革党）合计得票过半（俄国社革党本党约38%–40%居第一，布尔什维克约24%获约175席，立宪民主党约4.7%获约17席，`DATA-01`）。1917年12月加米涅夫等布尔什维克立宪会议党团临时局温和派主张尊重议会权威，遭列宁《关于立宪会议的提纲》压服改组（`CLM-rabinowitch-2007-constituent-assembly`, `[pp. 89–91, 127]`）。
- **1月5日（O.S.）白天的议会与利捷伊内大街枪击（1918-01-05 [O.S.] / 1918-01-18 [N.S.]）**：保卫立宪会议联盟组织无武装游行，多数工厂工人与士兵留在驻地；赤卫队与水兵在利捷伊内大街北段（与施帕列尔纳亚、基罗奇纳亚街口）通往塔夫利达宫的街垒向游行队伍开火，造成15人（高尔基《新生活报》医院调查）至21人（斯维尔德洛夫1月11日报告）死亡（同卡, `[pp. 106, 109]`）。议会大厅内切尔诺夫以244票对左翼社革党斯皮里多诺娃153票当选主席，在否决苏维埃《被剥削劳动人民权利宣言》后连夜通过土地社会化与和平呼吁，孟什维克策烈铁里发表长篇抗辩。
- **强制清场与解散（1918-01-06 [O.S.] / 1918-01-19 [N.S.]）**：布尔什维克与左翼社革党代表先后退席后，凌晨4时许无政府主义水兵警卫队长热列兹尼亚科夫以“警卫累了”勒令切尔诺夫休会清场；同日深夜全俄中央执行委员会正式颁布解散立宪会议法令（同卡, `[pp. 113–126]`），随后于 `1918-01-10 [O.S.] / 1918-01-23 [N.S.]` 召开的全俄苏维埃第三次代表大会宣告苏维埃联邦制取代立宪会议法统。场外因社革党中央禁止武装政变、卫戍部队冷漠观望而未爆发军事抵抗（Pipes, `ch21_section.md`）。
- **后果链条（1918年1月后）**：派普斯认为大众对立宪会议命运表现疲惫式冷漠，布尔什维克暴力驱散反而巩固了“真实政府”感知（`sources/monographs/pipes_1990_russian_rev/ch21_section.md`, §“dissolution met with surprising indifference”）。社会革命党右翼后来在科穆奇等处试图以“立宪会议成员委员会”延续合法性（`PER-chernov`）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-chernov` | `chair -> dispersed assembly` | 1918-01-05/06 [O.S.] | 凭借社革党选举多数主持唯一常会，却拒绝军事自卫路线 | `CLM-rabinowitch-2007-constituent-assembly`, Hildermeier on SR political naivety |
| `PER-lenin` | `dissolver` | 1917-12至1918-01 | 12月清洗党内尊重议会的温和派，1月下令武力终结立宪会议 | `CLM-rabinowitch-2007-constituent-assembly` |
| `ORG-psr` | `parliamentary-majority` | 1917-11至1918-01 | 赢得全国普选却在核心时刻缺乏保卫议会制度的武力决断 | `CLM-rabinowitch-2007-constituent-assembly`；`CLM-rabinowitch-2007-left-sr-coalition-collapse` |
| `ORG-kadets` | `demonstration-ally` | 1917-11至1918-01 | 保卫立宪会议联盟成员，1月5日游行主体为职员与学生而非工厂多数 | Pipes `ch21_section.md` |
| `EVT-1917-10-october-revolution` | `legitimacy-duel` | 1917-10至1918-01 | 十月后的苏维埃政权与 delayed 普选结果在立宪会议厅内正面冲突 | `DEB-1917-october-coup-or-social-revolution` |
| `ORG-mensheviks` | `defense-speech -> walkout` | 1918-01-05/06 | 策烈铁里在塔夫利达宫的发言成为议会社会主义最后广播 | `CLM-rabinowitch-2007-constituent-assembly` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：1918年1月5–6日（O.S.）/18–19日（N.S.）的立宪会议只开会一次即遭武力关闭；彼得格勒街头发生致死性枪击；苏维埃政权自该日起无需再认真对待选举授权反对派。
- **主要解释分歧**：
  - **[Rabinowitch 档案综合派 / Alexander Rabinowitch]** (`CLM-rabinowitch-2007-constituent-assembly`)：强调因果多重性——列宁镇压、布尔什维克街头暴力、社革党拒绝军事自卫与大众根本冷漠共同推动结局；保留党内温和派（加米涅夫、梁赞诺夫）抗争细节。
  - **[Pipes 自由—极权连续性 / Richard Pipes]**（`sources/monographs/pipes_1990_russian_rev/ch21_section.md`, `ch27_section.md`）：将关闭立宪会议与屠杀游行者与1917年11月逮捕卡德特一并纳入列宁主义恐怖制度化起点；主张民众疲惫与欠缺武装反对铸就布尔什维克1月后“真实政府”地位，甚至超过十月政变意义。
  - **[Hildermeier 社革党结构论 / Manfred Hildermeier]**（`sources/monographs/hildermeier_psr/`, `BIB-005`；`PER-chernov` 卡引）: 社革党制度上倚重合法议会神话却长期弱化军事组织，1918年切尔诺夫路线体现新民粹主义领袖在暴力门槛前的政治天真，与其1917年入阁时土地立法困境一体。
  - **[苏联正统 / 列宁《关于立宪会议的提纲》]**：视立宪会议为“曾经落后于无产阶级和贫农苏维埃运动”的资产阶级形式，解散是更高苏维埃民主的体现——须与 `CLM-rabinowitch-2007-constituent-assembly` 对照，避免单源定论。

## [T3] 深度考证、分期细目与原文引证档案
- **双历核号**（sort用 `date_ns`）：
  - 开会：`1918-01-05 [O.S.] / 1918-01-18 [N.S.]`
  - 驱散：`1918-01-06 [O.S.] / 1918-01-19 [N.S.]`
  - 全俄苏维埃三大开幕（并行节点）：`1918-01-10 [O.S.] / 1918-01-23 [N.S.]`（通行速记会期；注：Pipes 年表误印单日 Jan. 8）
- **Rabinowitch**（`sources/monographs/rabinowitch_2007_in_power/ch08_4_the_fate_of_the_constituent_assembly.md`, `CLM-rabinowitch-2007-constituent-assembly`）：
  > "The day had arrived, 5 January 1918, that was to mark the end of efforts to establish a Western-style, multiparty democratic system in Russia for most of the twentieth century." `[p. 104 / PDF p. 127]`
  > "...twenty-one demonstrators were killed." `[pp. 106, 109 / PDF pp. 129, 132]`
  > "...the Russian people's fundamental indifference to the fate of the Constituent Assembly..." `[p. 127 / PDF p. 150]`
- **Pipes**（`sources/monographs/pipes_1990_russian_rev/ch21_section.md`）：
  > "The dissolution of the Assembly met with surprising indifference..."
  > "In a sense the Bolsheviks may be said to have become the government of Russia not so much in October 1917 as in January 1918."
  > closing the Assembly and shooting marchers as terror from the day power was seized (`ch27_section.md`, cf. `[pp. 360]`)
- **Hildermeier**（`sources/monographs/hildermeier_psr/ch26_the_psr_and_modernization_was_there_a_po.md` 等）：1905年社革党曾想不等待立宪会议即实现权利，1917–18年又退回纯议会合法主义，形成党策略内在矛盾（结构评述，待 `close-reader` 钉页码引文）。
- **一手待提取**：
  1. 立宪会议秘书维什尼亚克（Vishniak）回忆录对已植入立宪会议的白卫著名段落；
  2. 1月5日彼得格勒苏维埃与契卡禁止游行命令；
  3. 梁赞诺夫、洛佐夫斯基在全俄中央执行委员会反对解散的发言记录（Rabinowitch `[pp. 125–126]`）。