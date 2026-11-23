---
id: AUD-23B-wave62-grok-card-scars-and-hygiene-audit
type: audit
auditor_model: grok-4.7
target_wave: W62
role: dialectic-auditor
status: remediated
updated_at: "2026-11-23"
scope: "cards/** 191 张实体卡；historiography/debates/** 23 张争鸣卡；timeline/L3_daily/*.md 28 卷。只读扫描。未改任何卡片、争鸣、时间线或台账。唯一写入本文件。"
---

# AUD-23B｜全库卡片可读性疤痕与规范体检（Defect-Only）

普查范围是全部 191 张实体卡、23 张争鸣卡、28 卷 L3。替换用的中文专名以各卡 YAML `title:` 为准。皮达可夫卡的题名是**格奥尔基·皮达可夫**。

级别：P0 是句子里用实体 ID 充当人名／机构名（尤其加粗）、读者正在读的句子里漏出任务指令，以及点进去即 404 的相对链接。P1 是会议、政策、事件 ID 充当专名，改历前俄国本土日次缺少双历，以及 `[T2]`／L3 题头里的工程批注。P2 是 `[T3]` 书目里的单侧旧历、中文名已经写出之后的第二次 ID、句末悬挂锚点。

## 已核、不立案

- `### 2.2` 边表第一列的 ID 是图谱锚点。中文专名之后的括号锚点（`列宁（`PER-lenin`）`、`（`CLM-*`）`、`参见`／`详参`）不立案。`PER-osinsky.md:27`、`PER-sapronov.md:27`、`ORG-democratic-centralists.md:25`、`ORG-workers-opposition.md:33`、`PER-spiridonova.md:27` 的 `EVT-*`、`EVT-1920-1921-tambov-and-peasant-revolts.md:32` 的句末括号、`INS-sovnarkom-and-vtsik.md:28` 与 `PER-sverdlov.md:28` 里已经写出中文会议名之后的 `（`MTG-*`）`，都属于这一类。
- 严格成对的 `YYYY-MM-DD [O.S.] / YYYY-MM-DD [N.S.]` 在本范围里算术错误 0 条，1918-02-14 之后未加白名单的苏俄旧历对 0 条。没有发现改历后苏俄日期被误标成这种严格 `[O.S.]` 孪生对。
- `公历日期`（俄历／旧历 `YYYY-MM-DD [O.S.]`）是合格双历。`PER-kirov.md:25`、`PER-makhno.md:25`、`PER-pyatakov.md:25`、`PER-spiridonova.md:25–26`、`PER-tukhachevsky.md:25`、`PER-voroshilov.md:25` 不立案。
- 西欧发文只标 `[N.S.]` 不立案：马克思 1881-03-08 伦敦复信、赫尔岑《钟声》、巴枯宁信件、1903 年伦敦会场当地时间、瑞士《社会民主党人报》。白军、教会、流亡机构在改历后继续用俄历的不立案。`PER-wrangel` 的 `1920-05-25 [O.S.] / 1920-06-07 [N.S.]` 是发文历（+13），不是苏俄官方旧历回潮。
- 纠正句（“禁止写作 `1905-12-19 [N.S.]`”、误写、不得沿用）不立案。
- 下列链接解析后文件存在，不报 404：百分号编码的中文书名、`file:///` 本地原件、`<https://...>` 脚注、姚海《俄国革命史》`ch497`／`ch498`／`ch502`（`1917-11` 卷里的长中文文件名解码后与磁盘文件名一致）。`<../../inbox/……>` 带空格的角括号路径同样指向实文件，不报。
- “里程碑”作史学术语的不立案：`MTG-1912-01-prague-conference.md:46`、`1917-10` 卷 `:280`“修正派里程碑”、`1918-07` 卷 `:13` 与 `:96`“体制化里程碑”、`1920-07` 卷 `:38`“政治局里程碑决议”。`DEB-1917-july-days-spontaneity-vs-conspiracy.md:19` 的“不能凭其中一项推定其他结论”是证据分离，不是任务话术。
- 28 卷里没有“编排角色”的是 `1923-10_scissors_and_new_course_crisis.md`、`1927-10_tenth_anniversary_and_15th_congress.md`、`1928-01_siberian_grain_expedition_and_shakhty_affair.md`。前两卷的断链见 C 节。

---

## A. 正文把实体 ID 当专名

判定：ID 占着主谓宾里的人名、机构名、会议名或政策名，读者看不见中文专名。中文名已经在前、ID 只在括号里的，不在本节。

### A-P0｜加粗或主位上没有中文专名

| 位置 | 原文片段 | 替换 |
|---|---|---|
| `cards/institutions/INS-vsnkh-and-gosplan.md:26` | 最高经委副主席 **`PER-pyatakov`** 主导 | 最高经委副主席 **格奥尔基·皮达可夫**主导 |
| 同句 | 财政人民委员 **`PER-sokolnikov`** 捍卫 | 财政人民委员 **格里戈里·索科尔尼科夫**捍卫 |
| 同句 | **`PER-dzerzhinsky`** 兼任最高经委主席 | **费利克斯·捷尔任斯基**兼任最高经委主席 |
| `cards/institutions/INS-vsnkh-and-gosplan.md:27` | 以 **`PER-kondratiev`**、格罗曼、巴扎罗夫 | 以 **尼古拉·康德拉季耶夫**、格罗曼、巴扎罗夫 |
| 同句 | 以 **`PER-strumilin`** 为代表 | 以 **斯坦尼斯拉夫·斯特鲁米林**为代表 |
| `cards/institutions/INS-rkka-red-army-and-rvr.md:27` | 由 **`PER-voroshilov`** 接掌 | 由 **克利缅特·伏罗希洛夫**接掌 |
| 同句 | 参谋长 **`PER-tukhachevsky`** | 参谋长 **米哈伊尔·图哈切夫斯基** |
| `cards/policies/POL-ban-on-factions-1921.md:26` | 将 **`PER-zinoviev`** 逐出政治局 | 将 **格里戈里·季诺维也夫**逐出政治局 |
| `cards/organizations/ORG-osvobozhdenie-truda.md:25` | `` `ORG-chernyi-peredel` `` 国内网络崩溃后，五名流亡前成员——`` `PER-plekhanov`、`PER-zasulich`、`PER-axelrod` ``、列夫·捷伊奇 | 黑土重分派国内网络崩溃后，五名流亡前成员——格奥尔基·普列汉诺夫、维拉·查苏利奇、帕维尔·阿克雪里罗得、列夫·捷伊奇。首次出现可在中文名后各加一次括号锚点 |
| `cards/organizations/ORG-osvobozhdenie-truda.md:27` | 新一代代表 `` `PER-lenin`、`PER-martov-l` ``、波特列索夫 | 新一代代表弗拉基米尔·列宁、尤利·马尔托夫、波特列索夫 |
| `cards/organizations/ORG-osvobozhdenie-truda.md:28` | 最初在大会上支持列宁的 `` `PER-plekhanov` `` ……与被逐出编委的 `` `PER-axelrod`、`PER-zasulich` `` ……成为 `` `ORG-mensheviks` `` | 格奥尔基·普列汉诺夫……帕维尔·阿克雪里罗得、维拉·查苏利奇……成为孟什维克。同句 `` `MTG-1903-rsdlp-2nd-congress` `` 已在“第二次代表大会”括号内，保留 |
| `cards/organizations/ORG-psr.md:26` | `` `PER-chernov` `` 与阿·戈茨；`` `PER-savinkov` `` 亦为其核心执行 | 维克托·切尔诺夫与阿·戈茨；鲍里斯·维克托罗维奇·萨温科夫亦为其核心执行人 |
| `cards/organizations/ORG-psr.md:27` | `` `PER-lenin` `` 在《土地法令》；选举 `` `PER-chernov` `` 为主席 | 弗拉基米尔·列宁在《土地法令》；选举维克托·切尔诺夫为主席。同句“克伦斯基（`` `PER-kerensky` ``）”保留 |
| `cards/organizations/ORG-zemlya-i-volya.md:26` | 米海洛夫（A. D. Mikhailov）、`` `PER-plekhanov` `` 等人 | 米海洛夫（A. D. Mikhailov）、格奥尔基·普列汉诺夫等人 |
| `cards/organizations/ORG-zemlya-i-volya.md:48` | 裂变为 `` `ORG-narodnaya-volya` `` 与 `` `ORG-chernyi-peredel` `` | 裂变为民意党与黑土重分派 |
| `cards/people/PER-axelrod.md:25` | 加入 `` `ORG-chernyi-peredel` ``，与 `` `PER-plekhanov`、`PER-zasulich` `` | 加入黑土重分派，与格奥尔基·普列汉诺夫、维拉·查苏利奇 |
| `cards/organizations/ORG-kadets.md:26` | `` `PER-milyukov` `` 坚决反对；夏初与 `` `PER-stolypin` `` 谈判入阁破裂 | 帕维尔·米留可夫坚决反对；夏初与彼得·斯托雷平谈判入阁破裂 |
| `cards/organizations/ORG-kadets.md:28` | 由 `` `PER-lvov` `` 主持、排除了 `` `PER-rodzianko` `` ……`` `PER-milyukov` `` 一派；依附 `` `PER-denikin`、`PER-kolchak` `` | 由格奥尔吉·叶夫根尼耶维奇·李沃夫主持、排除了米哈伊尔·弗拉基米罗维奇·罗将柯……帕维尔·米留可夫一派；依附安东·邓尼金、亚历山大·高尔察克 |
| `cards/events/EVT-1891-1903-witte-industrialization-and-marxist-labor-turn.md:27` | `` `PER-witte` `` 出任财政大臣 | 谢尔盖·维特出任财政大臣。同句的普列汉诺夫、阿克雪里罗得、查苏利奇、司徒卢威、列宁同样先写中文名 |
| `cards/events/EVT-1907-1914-june-third-regime-and-lena-to-july-strikes.md:28` | 与 `` `PER-lenin` `` 的决裂 | 与弗拉基米尔·列宁的决裂。同句“波格丹诺夫 `` `PER-bogdanov` ``”已有中文名，ID 放进括号即可 |
| `cards/events/EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc.md:27` | 以 `` `PER-plekhanov` `` ……为代表的护国派、以 `` `PER-martov-l` `` 与 `` `PER-chernov` `` 为代表……以及 `` `PER-lenin` `` 提出 | 以格奥尔基·普列汉诺夫……为代表的护国派、以尤利·马尔托夫与维克托·切尔诺夫为代表……以及弗拉基米尔·列宁提出 |
| `cards/events/EVT-1918-1921-transcaucasian-republics-baku-commune-and-sovietization.md:27` | 以 `` `PER-ordzhonikidze` `` 为首；`` `PER-ordzhonikidze`、`PER-kirov` `` 与米高扬主政 | 以格里戈里·“谢尔戈”·奥尔忠尼启则为首；奥尔忠尼启则、谢尔盖·基洛夫与米高扬主政 |
| `cards/people/PER-ustryalov.md:27` | `` `PER-lenin` `` 在俄共（布）十一大；`` `PER-stalin` `` 与 `` `PER-bukharin` `` 倡行；击败 `` `PER-trotsky` ``；猛轰李可夫（`` `PER-rykov` ``）及非党专家（`` `PER-kondratiev`、`PER-chayanov` ``） | 弗拉基米尔·列宁在俄共（布）十一大；约瑟夫·斯大林与尼古拉·布哈林倡行；击败列夫·托洛茨基；李可夫、尼古拉·康德拉季耶夫、亚历山大·恰亚诺夫写中文名。同句十一大的 `` `MTG-1922-03-11th-party-congress` `` 已是括号锚点，保留 |
| `cards/organizations/ORG-right-opposition-1928.md:25` | `` `PER-bukharin` ``（《真理报》与共产国际）、`` `PER-rykov` ``（人民委员会）、`` `PER-tomsky` ``（全苏工会中央理事会）、`` `PER-uglanov` ``（莫斯科市委） | 尼古拉·布哈林（《真理报》与共产国际）、阿列克谢·李可夫（人民委员会）、米哈伊尔·托姆斯基（全苏工会中央理事会）、尼古拉·乌格拉诺夫（莫斯科市委）。同句“斯大林（`` `PER-stalin` ``）”保留 |
| `cards/organizations/ORG-right-opposition-1928.md:28` | `` `PER-bukharin` `` 虽成功阻挡 | 尼古拉·布哈林虽成功阻挡。会议名见 A-P1 |
| `cards/organizations/ORG-right-opposition-1928.md:29` | 扩大了对 `` `PER-uglanov` `` 班底；由 `` `PER-molotov` `` 接替；`` `PER-tomsky` `` 与梅尔尼昌斯基 | 尼古拉·乌格拉诺夫班底；由维亚切斯拉夫·莫洛托夫接替；米哈伊尔·托姆斯基与梅尔尼昌斯基 |
| `cards/organizations/ORG-right-opposition-1928.md:31` | `` `PER-stalin` `` 则于；将 `` `PER-bukharin` `` 逐出政治局；警告 `` `PER-rykov` `` 与 `` `PER-tomsky` `` | 约瑟夫·斯大林则于；将尼古拉·布哈林逐出政治局；警告阿列克谢·李可夫与米哈伊尔·托姆斯基 |
| `cards/people/PER-kalinin.md:27` | 同情 `` `PER-bukharin` `` 与 `` `PER-rykov` ``；加里宁与 `` `PER-voroshilov` `` 未按右派预期 | 同情尼古拉·布哈林与阿列克谢·李可夫；加里宁与克利缅特·伏罗希洛夫未按右派预期 |
| `cards/people/PER-frunze.md:29` | 对阵 `` `PER-wrangel` `` 约 3.7 万白军；与 `` `PER-makhno` `` 黑军分遣队协同 | 对阵彼得·弗兰格尔约 3.7 万白军；与涅斯托尔·马赫诺黑军分遣队协同 |
| `cards/people/PER-chayanov.md:28` | `` `ORG-left-and-united-opposition` ``《政纲》亦将恰亚诺夫与 `` `PER-kondratiev` `` 并指为盘踞在 `` `PER-rykov` `` 周围；`` `PER-stalin` `` 于 | 1923–1927年左翼反对派与托季联合反对派《政纲》亦将恰亚诺夫与尼古拉·康德拉季耶夫并指为盘踞在阿列克谢·李可夫周围；约瑟夫·斯大林于。同句若已写“斯大林（`` `PER-stalin` ``）”，括号锚点保留，不要再让 ID 当主语 |
| `cards/people/PER-kuibyshev.md:27` | 病危中的 `` `PER-dzerzhinsky` `` 致信古比雪夫；触发 `` `PER-bukharin` `` 于 | 病危中的费利克斯·捷尔任斯基致信古比雪夫；触发尼古拉·布哈林于。同句“最高国民经济委员会（`` `INS-vsnkh-and-gosplan` ``）”“十五大（`` `MTG-1927-12-15th-party-congress` ``）”“沙赫特事件（`` `EVT-1928-shakhty-affair-show-trial` ``）”保留 |
| `cards/people/PER-rakovsky.md:27` | 而 `` `PER-lenin` `` 在1922年12月30—31日口授……惩处 `` `PER-ordzhonikidze` ``……追究 `` `PER-stalin` `` 与 `` `PER-dzerzhinsky` `` 政治责任；联合 `` `PER-frunze` ``、斯克里普尼克 | 而弗拉基米尔·列宁在1922年12月30—31日口授……惩处格里戈里·“谢尔戈”·奥尔忠尼启则……追究约瑟夫·斯大林与费利克斯·捷尔任斯基的政治责任；联合米哈伊尔·伏龙芝、斯克里普尼克 |
| `cards/organizations/ORG-chernyi-peredel.md:27` | `` `PER-zasulich` `` 自日内瓦致信 | 维拉·查苏利奇自日内瓦致信。同句 `1881-03-08 [N.S.]` 是伦敦发文，保持单侧公历 |
| `cards/institutions/INS-gosbank-and-narkomfin.md:29` | `` `PER-sokolnikov` `` 记 `1922-01` 任 | 格里戈里·索科尔尼科夫于 `1922-01` 任。库内没有 `PER-krestinsky` 这张卡，不要造链接；“站内尚无卡”一句移到 `[T3]` |
| `cards/people/PER-gapon.md:28` | 链接可见文字是 `` `EVT-1905-01-bloody-sunday` `` | 可见文字改为“1905年流血星期日”，href `../events/EVT-1905-01-bloody-sunday.md` 不动 |

### A-P1｜会议、政策、机构、事件 ID 充当专名

中文名放在前面，ID 只留一次括号。

| 位置 | 原文片段 | 替换 |
|---|---|---|
| `cards/people/PER-kaganovich.md:26` | 强力推进 **`POL-korenizatsiia`（本土化/乌克兰化）** | 强力推进 **本土化政策（Коренизация）**（`POL-korenizatsiia`） |
| `cards/people/PER-kaganovich.md:28` | 属 **`POL-ural-siberian-method`（乌拉尔—西伯利亚…）** | 属 **乌拉尔—西伯利亚方法**（`POL-ural-siberian-method`）。同句两处全会若已写“联席全会（`` `MTG-1929-04-cc-joint-plenum` ``）”，括号保留 |
| `cards/concepts/CON-democratic-centralism-and-vanguard.md:42` | **场合**：`` `MTG-1903-rsdlp-2nd-congress` `` | **场合**：俄国社会民主工党第二次代表大会（`MTG-1903-rsdlp-2nd-congress`） |
| `cards/concepts/CON-democratic-centralism-and-vanguard.md:59` | **场合**：`` `MTG-1921-rcpb-10th-congress` `` | **场合**：俄国共产党（布尔什维克）第十次代表大会（`MTG-1921-rcpb-10th-congress`）。同句《关于党的统一》（`` `POL-ban-on-factions-1921` ``）、喀琅施塔得起义（`` `EVT-1921-kronstadt` ``）、工人反对派（`` `ORG-workers-opposition` ``）已是括号锚点，保留 |
| `cards/concepts/CON-democratic-centralism-and-vanguard.md:69` | 在 `` `MTG-1925-12-14th-party-congress` ``、`` `MTG-1927-12-15th-party-congress` `` 与 `` `MTG-1929-04-cc-joint-plenum` `` 依次击败 | 在联共（布）第十四次代表大会、第十五次代表大会与四月联席全会依次击败。ID 各留一次括号 |
| `cards/concepts/CON-kulak.md:55` | **场合**：`` `MTG-1929-11-cc-plenum` `` | **场合**：联共（布）中央委员会十一月全会（1929）（`MTG-1929-11-cc-plenum`） |
| `cards/concepts/CON-state-capitalism.md:37` | 在 `` `EVT-1921-kronstadt` `` 后为 `` `POL-nep` `` 退却 | 在喀琅施塔得水兵起义后为新经济政策退却。后面的“参 `DEB-…`”保留 |
| `cards/people/PER-kalinin.md:26` | `` `Всесоюзный староста` ``；`` `INS-sovnarkom-and-vtsik` `` | 全联盟村长；机构名写“人民委员会与全俄、全苏中央执行委员会”（`INS-sovnarkom-and-vtsik`）。同句八大、十大、十四大的括号 `MTG-*` 保留 |
| `cards/people/PER-kondratiev.md:27` | 同 `` `INS-vsnkh-and-gosplan` ``（国家计委与最高 | 同最高国民经济委员会与国家计划委员会（`INS-vsnkh-and-gosplan`） |
| `cards/people/PER-kondratiev.md:28` | `` `ORG-left-and-united-opposition` ``《政纲》；随 `` `EVT-1928-grain-procurement-crisis` `` 爆发 | 联合反对派《政纲》；随1927冬–1929年粮食收购危机爆发。ID 放括号 |
| `cards/organizations/ORG-right-opposition-1928.md:25` | 与此前 `` `ORG-left-and-united-opposition` `` 设地下；保卫 `` `POL-nep` ``；严守 `` `POL-ban-on-factions-1921` `` | 与此前的联合反对派设地下印刷所；保卫新经济政策；严守《关于党的统一》派别禁令 |
| `cards/organizations/ORG-right-opposition-1928.md:28` | `` `MTG-1928-07-comintern-6th-congress` `` 上 | 共产国际第六次代表大会上 |
| `cards/organizations/ORG-right-opposition-1928.md:29` | `` `MTG-1928-11-cc-plenum` `` 前夕 | 联共（布）1928年11月中央委员会全会前夕 |
| `cards/organizations/ORG-right-opposition-1928.md:31` | `` `MTG-1929-04-cc-joint-plenum` ``；`` `MTG-1929-11-cc-plenum` ``；农民在 `` `EVT-1929-great-turn-and-dekulakization-launch` `` 抗议中 | 四月联席全会；十一月全会；农民在1929年秋大转变与全盘集体化抗议中 |
| `cards/people/PER-ustryalov.md:27` | 倡行 `` `CON-socialism-in-one-country` ``；成为 `` `ORG-left-and-united-opposition` `` | 倡行一国建成社会主义；成为1923–1927年左翼反对派与托季联合反对派 |
| `cards/people/PER-ustryalov.md:28` | `` `EVT-1929-great-turn-and-dekulakization-launch` `` 爆发 | 1929年秋大转变与全盘集体化、消灭富农启动 |
| `cards/organizations/ORG-psr.md:28` | 成立 `` `ORG-komuch-and-democratic-counterrevolution` ``；借 `` `PER-kolchak` `` 鄂木斯克政变；引发的 `` `EVT-1918-09-red-terror-and-left-sr-rupture` ``；`` `EVT-1920-1921-tambov-and-peasant-revolts` `` 后；举行 `` `EVT-1922-sr-show-trial` ``；扩大 `` `INS-cheka-gpu-ogpu` `` | 成立萨马拉立宪会议成员委员会（Комуч）；借亚历山大·高尔察克鄂木斯克政变；引发的1918年夏左翼社革党决裂与红色恐怖制度化；坦波夫安东诺夫起义与1920–1921年农民绿军风暴之后；举行1922年莫斯科社会革命党公开大审判；扩大全俄肃反委员会—国家政治保卫局的法外权力 |
| `cards/organizations/ORG-kadets.md:27` | 组成跨党派 `` `ORG-octobrists-and-progressive-bloc` ``；`` `PER-milyukov` `` 策略性撤回；阻遏 `` `PER-guchkov` `` | 组成跨党派的十月十七日同盟与进步同盟；帕维尔·米留可夫策略性撤回；阻遏亚历山大·伊万诺维奇·古契科夫 |
| `cards/organizations/ORG-kadets.md:28` | `` `ORG-provisional-government` `` 亦从未；仰赖 `` `ORG-petrograd-soviet` ``；科尔尼洛夫事件（`` `EVT-1917-08-kornilov-affair` ``）若 ID 在专名位置 | 1917年俄国临时政府；彼得格勒工兵代表苏维埃。事件中文名在前时，ID 留在括号 |
| `cards/events/EVT-1891-1903-witte-industrialization-and-marxist-labor-turn.md:27` | 应依托 `` `CON-peasant-commune-obshchina` ``；海外 `` `ORG-osvobozhdenie-truda` ``（`` `PER-plekhanov` `` 等）及国内的 `` `PER-struve` ``、`` `PER-lenin` `` | 应依托农村公社；海外劳动解放社（普列汉诺夫、阿克雪里罗得、查苏利奇）及国内的彼得·伯恩哈多维奇·司徒卢威、弗拉基米尔·列宁 |
| `cards/organizations/ORG-chernyi-peredel.md:27` | 询问俄国 `` `CON-peasant-commune-obshchina` `` 是注定 | 询问俄国农村公社是注定 |
| `cards/organizations/ORG-osvobozhdenie-truda.md:28` | 后三人悉数成为 `` `ORG-mensheviks` `` | 后三人悉数成为孟什维克 |
| `cards/organizations/ORG-bolsheviks-rcpb-vkpb.md:40` | `` `POL-ban-on-factions-1921` `` 要求解散派别 | 《关于党的统一》派别禁令要求解散派别。同句“见 `` `ORG-workers-opposition` `` 所引”是引证，保留 |
| `cards/organizations/ORG-democratic-centralists.md:47` | 库内由 `` `PER-sapronov`、`PER-osinsky` `` 与 `` `ORG-workers-opposition` `` 经 Daniels 页码承载 | 库内由季莫费·萨普罗诺夫、瓦列里安·奥博连斯基（N·奥新斯基）与工人反对派经 Daniels 页码承载 |
| `cards/meetings/MTG-1918-03-7th-party-congress.md:41` | `` `POL-brest-litovsk-treaty` `` 考证指出 | 布列斯特-立托夫斯克和约卡的考证指出 |
| `cards/people/PER-krupskaya.md:29` | `` `1925-12` `` `` `MTG-1925-12-14th-party-congress` `` 前后 | `1925-12` 联共（布）第十四次代表大会前后。同句“索科利尼科夫（`` `PER-sokolnikov` ``）”“斯大林—布哈林（`` `PER-bukharin` ``）”保留 |
| `cards/people/PER-chicherin.md:28` | 在 `` `EVT-1927-war-scare-and-opposition-expulsion` `` 危机中 | 在1927年“战争恐慌”危机中。同句“斯大林（`` `PER-stalin` ``）”保留 |
| `cards/people/PER-rakovsky.md:27` | 俄共（布）`` `MTG-1923-04-12th-party-congress` `` 期间；`` `POL-korenizatsiia` `` 方针 | 俄共（布）第十二次代表大会期间；本土化政策方针 |
| `cards/people/PER-kuibyshev.md:27` | 与 `` `POL-first-five-year-plan` `` 制定中 | 与第一个五年计划的制定中 |
| `cards/people/PER-frunze.md:29` | 与 `` `PER-wrangel` `` 卡口径一致 | 与弗兰格尔卡口径一致 |

### A-P2｜中文名已在，ID 仍裸在句末

| 位置 | 原文片段 | 替换 |
|---|---|---|
| `cards/institutions/INS-state-duma-1906-1917.md:28` | 进步同盟……（Gaida，pp. 134–175；`` `ORG-octobrists-and-progressive-bloc` ``；`` `ORG-kadets` ``） | 进步同盟（十月十七日同盟与立宪民主党；Gaida，pp. 134–175）。同句“斯托雷平政府的议案（`` `PER-stolypin` ``；…）”保留 |
| `cards/institutions/INS-rabkrin-and-ccc.md:30` | 奥尔忠尼启则接任中监委之后又写 `` `PER-ordzhonikidze` `` 记；古比雪夫离任（`` `PER-kuibyshev` `` 记…） | 第二次用中文名。`` `AUD-14` `` 这个审计号移到 `[T3]` |
| `cards/events/EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc.md:29` | 尼古拉二世……（`` `PER-nicholas-ii` `` 另以大本营发布手谕日并记 `08-23 [O.S.]`） | 尼古拉二世……（另以大本营发布手谕日并记 `1915-08-23 [O.S.] / 1915-09-05 [N.S.]`） |
| `cards/people/PER-gorky.md:28` | 忧虑俄国底层缺乏现代公民文化（Steinberg；`` `CON-dual-power` ``） | 忧虑双重政权时期俄国底层缺乏现代公民文化（Steinberg）。同句二月革命、加米涅夫、立宪会议的括号锚点保留 |
| `cards/concepts/CON-revolutionary-defensism-and-defeatism.md:68` | Cohen `` `CON-state-capitalism` `` | Cohen 论国家资本主义（`CON-state-capitalism`） |
| `cards/concepts/CON-revolutionary-defensism-and-defeatism.md:69` | Rabinowitch …… `` `EVT-1918-03-brest-litovsk-treaty` `` | 把事件 ID 改成“布列斯特危机（`EVT-1918-03-brest-litovsk-treaty`）”，不要让 ID 单独顶在引证位 |
| `cards/events/EVT-1907-1914-june-third-regime-and-lena-to-july-strikes.md:28` | 造成 `` `ORG-psr` `` 道德与组织双重瘫痪（社革党已在同句出现） | 造成该党道德与组织双重瘫痪 |

---

## B. 建库话术与审计补丁腔

### B-P0｜读者句子里的任务指令

| 位置 | 原文片段 | 替换 |
|---|---|---|
| `cards/events/EVT-1921-kronstadt.md:28`（`### 2.1`） | 没有独立入藏一份2月28日异文，不能凭任务中的建议文件名造出链接。 | 站内实存原典是 3月1日文本 `1921-03-01_petropavlovsk-resolution.md`；2月28日先行通过另有政府通报旁证，库内没有单独的2月28日异文。不要新造链接。2月28日舰上通过、3月1日大会确认、3月2日临时革命委员会这三步留下 |
| `timeline/L3_daily/1918-01_constituent_assembly_and_brest_crisis.md:3` | （用户任务所称 `RN-W9-soviet-first-year-and-party-conscience` 本地未检出，以 W2 同书精读札记代锚） | 删掉这整句括号。精读对接只留已经存在的 [`RN-W2-first-year-soviet-rule`](../../reading-notes/rabinowitch_2007_in_power/RN-W2-first-year-soviet-rule.md) |

### B-P1｜同一条题头疤：`编排角色：chronicle-weaver；`

25 卷的第 3 行都有这句。删掉 `编排角色：chronicle-weaver；`，并删掉紧随的 `状态：Wnn 候选／正式／显微编年`。日期范围、日历规则、以及已经指向真实文件的精读链接留下。

`timeline/L3_daily/` 下这些文件的第 3 行：

- `1878-01_zasulich_trial_and_zemlya_volya_split.md`
- `1881-03_march_first_assassination.md`
- `1903-07_rsdlp_second_congress_split.md`
- `1905-01_bloody_sunday_and_october_soviet.md`
- `1905-12_petersburg_arrest_and_moscow_uprising.md`
- `1912-04_lena_goldfields_and_pravda_upsurge.md`
- `1914-07_petrograd_barricades_and_war_credits_rupture.md`
- `1917-02_february_eight_days.md`
- `1917-04_lenin_arrival_april_theses_and_milyukov_note.md`
- `1917-06_first_soviet_congress_and_june_crisis.md`
- `1917-07_july_days_and_kornilov_affair.md`
- `1917-10_october_insurrection.md`
- `1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md`
- `1918-01_constituent_assembly_and_brest_crisis.md`
- `1918-05_food_dictatorship_and_czechoslovak_revolt.md`
- `1918-07_left_sr_uprising_and_red_terror_launch.md`
- `1919-10_civil_war_southern_and_petrograd_climax.md`
- `1920-07_polish_war_warsaw_and_2nd_comintern.md`
- `1921-03_kronstadt_and_10th_congress.md`
- `1922-12_lenins_last_struggle_diary.md`
- `1924-01_lenin_death_testament_and_lessons_of_october.md`
- `1925-12_fourteenth_congress_new_opposition_clash.md`
- `1926-07_united_opposition_and_dzerzhinsky_death.md`
- `1928-1929_bukharin_stalin_final_showdown.md`
- `1929-11_november_plenum_to_dekulakization_decree.md`

同句若还写着“本卷只写入本 Markdown，不另立侧车 JSONL，也不改 events_ledger”，连这句一起删。已核对的是 `1881-03`、`1921-03`、`1928-1929` 三卷的第 3 行。`1918-01` 第 3 行里的 `python scripts/kb.py date` 也删，日历规则本身（1918-02-14 前双标、+13、2 月 1–13 日在俄国官方日历中跳过）留下。

### B-P1｜向读者宣布“不改台账／未写入边界”

删掉权限声明。史实校正留下。

| 位置 | 原文片段 | 替换 |
|---|---|---|
| `timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md:11` | 主台账有一条把方法的确立写在 1928-01-15，本卷不沿用这一并日，也不改台账。 | 1月西伯利亚之行使用的是非常措施与第107条。勒温所称“乌拉尔—西伯利亚方法”是1928–29年冬、七月全会已承诺不再重复非常措施之后的伪装征粮。两件事不并日、不并名 |
| `timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md:13` | **未建卡的人不造 ID**：乌格拉诺夫、鲍曼、莫洛托夫……在正文写全名，不发明 `PER-*` | 删掉这条禁令。乌格拉诺夫、莫洛托夫、奥尔忠尼启则、索科尔尼科夫已有人物卡，正文写中文名。仍然没有卡片的人只写中文全名 |
| `timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md:301` | 主台账未改。……留待以后的台账修订，不在本次改账。 | 正文已把西伯利亚之行与“乌拉尔—西伯利亚方法”拆开。删掉“未改台账／留待修订” |
| `timeline/L3_daily/1881-03_march_first_assassination.md:148` | 主台账保持完全未动，不另写侧车 JSONL。抽核 `python scripts/kb.py date --from os`：… | 删整条。+12 的双历已经写在正文日期里 |
| `timeline/L3_daily/1921-03_kronstadt_and_10th_congress.md:212` | 主台账保持完全未动，不另写侧车 JSONL | 删这句。1921 年日期在改历之后、只用公历，这句日历说明若还在 `:211`，留下 |
| `timeline/L3_daily/1878-01_zasulich_trial_and_zemlya_volya_split.md:203` | 依本轮写入边界规定……**未修改** `events_ledger.jsonl` | 删权限句 |
| `timeline/L3_daily/1914-07_petrograd_barricades_and_war_credits_rupture.md:176` | 同上，“依本轮写入边界规定……未修改” | 删权限句 |
| `timeline/L3_daily/1905-01_bloody_sunday_and_october_soviet.md:193` | 主台账协调，并链向不存在的侧车 | 删“不改主台账”。断链按 C 节去掉 |
| `timeline/L3_daily/1912-04_lena_goldfields_and_pravda_upsurge.md:14` | 主台账协调／不沿用 | 删权限句。历史日期留下 |
| `timeline/L3_daily/1917-02_february_eight_days.md:209` | 候选台账写入 `_w3_1917_events.jsonl` | 删该条。文件不存在，见 C 节 |
| `timeline/L3_daily/1917-04_lenin_arrival_april_theses_and_milyukov_note.md:294` | 候选台账写入 `staging_w32_1917_04.jsonl` | 删该条 |
| `timeline/L3_daily/1917-10_october_insurrection.md:295` | 候选台账写入 `_w3_1917_events.jsonl` | 删该条 |
| `timeline/L3_daily/1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md:273` | 候选台账写入 `_w36_1917_11_events.jsonl` | 删该条 |
| `timeline/L3_daily/1922-12_lenins_last_struggle_diary.md:177` | 主台账协调 | 删权限句 |
| `timeline/L3_daily/1926-07_united_opposition_and_dzerzhinsky_death.md:13` | 地点校正，并带“不改主台账／不越权” | 留下地点校正：集会地是多尔戈普鲁德纳亚，不要写成“拉兹古利亚伊树林”。删权限分句 |
| `timeline/L3_daily/1926-07_united_opposition_and_dzerzhinsky_death.md:16` | 主台账协调，并链向不存在的 `_w25` | 删权限句与死链 |
| `timeline/L3_daily/1929-11_november_plenum_to_dekulakization_decree.md:120` | 编排目标：将 L3 显微卷推至 20 卷里程碑；本批新增第 19–20 卷，全目录以 `glob` 计数为准。 | 删这句。留下：叙事以 **1930-01-05** 指令性文本为 1861–1929 时间轴封口，并保留指向 `1920-07` 卷、L1 骨干和主台账的真实链接 |
| `timeline/L3_daily/1918-07_left_sr_uprising_and_red_terror_launch.md:3` | 布尔什维克—契卡Summer克制 | 契卡夏季的相对克制。同句的编排角色按上面的 25 卷通例删除 |

### B-P1｜子代理名字写进读者要读的格子

| 位置 | 原文片段 | 替换 |
|---|---|---|
| `historiography/debates/DEB-1923-nationality-and-empire.md:27`（`[T2]` 表） | Martin 专著独立论断卡尚待 `close-reader` 入库 | Martin 专著的独立论断卡尚未立卡。现阶段参看本土化政策卡与 `CLM-smith-jeremy-1999-twelfth-congress-korenizatsiia` |
| `cards/organizations/ORG-workers-opposition.md:57` | 待 `source-extractor` 入库，规划路径 `sources/primary/shliapnikov_1921_workers_opposition_theses/…` | 1921-01-25《真理报》提纲原件待补。现可互证的是 Daniels 1960 英译与柯伦泰小册子。删角色名；规划路径若磁盘上没有这个文件，不要写成链接 |
| `cards/organizations/ORG-bund.md:69` | 待 `close-reader` 入库 | 1901 年比亚韦斯托克四大、1905 年苏黎世六大决议与 1917–1921 年大会记录待补原件 |
| `cards/organizations/ORG-makhnovshchina.md:68` | `CLM-*` 待 `source-extractor` 专案 | 马赫诺回忆录与契卡南线审讯卷待补原件 |

### B-P2｜`[T3]` 里的行号腔，以及文末对账节

| 位置 | 原文片段 | 替换 |
|---|---|---|
| `cards/events/EVT-1921-kronstadt.md:72`（`[T3]` §3.1） | `original_pages` 混入 RN-W3 行号（816-818）……不沿用那些异常数字 | 删 `original_pages`／行号这句工程话。留下：2月28日舰上通过与3月1日大会确认是两个阶段；1921年日期都是公历，不是旧历换算 |
| `cards/organizations/ORG-vikzhel.md:36` | 本库不裁决 `29:23:3` 与 `25:23` | 两套票数口径不同，本段并列，不合成一个总数。数字留下 |
| L3 文末「日期核验与候选台账说明」 | 各卷把 `TL-*` 与主台账的对照写成给读者的一节 | P2：每卷收成一条维护脚注。不要删掉其中真正的日期校正。已见到标题行的卷包括 `1881-03:145`、`1903-07:117`、`1905-01:190`、`1905-12:148`、`1912-04:161`、`1917-02:206`、`1917-04:291`、`1917-07:171`、`1917-10:292`、`1917-11:270`、`1918-01:159`、`1918-07:114`、`1919-10:124`、`1920-07:124`、`1921-03:209`、`1922-12:174`、`1925-12:142`、`1926-07:177`、`1929-11:124` |

---

## C. 相对链接 404

全库侧车文件名 `_w8_candidate_events.jsonl`、`_w25_candidate_events.jsonl`、`_w3_1917_events.jsonl`、`staging_w32_1917_04.jsonl`、`_w36_1917_11_events.jsonl`、`_w15_candidate_events.jsonl`、`_w36_1924_events.jsonl` 在仓库里不存在。处理：删掉死链。句子里若已经说明条目并入主台账，只留 [`events_ledger.jsonl`](../events_ledger.jsonl)。不要补造这些 JSONL。

下面替换列给出从该 Markdown 所在目录出发的正确相对路径。

### C-P0｜目录写错，目标文件存在

| 位置 | 现在的 href | 改为 |
|---|---|---|
| `timeline/L3_daily/1917-02_february_eight_days.md:13` | `../../cards/CLM-hasegawa-2018-sub-elite-activists.md` | `../../historiography/claims/CLM-hasegawa-2018-sub-elite-activists.md` |
| 同行 | `../../cards/CLM-hasegawa-2018-duma-committee-revision.md` | `../../historiography/claims/CLM-hasegawa-2018-duma-committee-revision.md` |
| 同行 | `../../cards/CLM-hasegawa-2018-dual-power-origins.md` | `../../historiography/claims/CLM-hasegawa-2018-dual-power-origins.md` |
| 同行 | `../../cards/CON-soviet.md` | `../../cards/concepts/CON-soviet.md` |
| 同行 | `../../cards/PER-trotsky.md` | `../../cards/people/PER-trotsky.md` |
| `timeline/L3_daily/1917-02_february_eight_days.md:127` | `../../cards/CLM-hasegawa-2018-duma-committee-revision.md` | `../../historiography/claims/CLM-hasegawa-2018-duma-committee-revision.md` |
| `timeline/L3_daily/1917-02_february_eight_days.md:196` | 同上 | 同上 |
| `timeline/L3_daily/1917-02_february_eight_days.md:198` | `../../cards/CLM-hasegawa-2018-dual-power-origins.md` | `../../historiography/claims/CLM-hasegawa-2018-dual-power-origins.md` |
| `timeline/L3_daily/1917-10_october_insurrection.md:13` | `../../cards/PER-lenin.md` | `../../cards/people/PER-lenin.md` |
| 同行 | `../../cards/PER-trotsky.md` | `../../cards/people/PER-trotsky.md` |
| 同行 | `../../cards/PER-kamenev.md` | `../../cards/people/PER-kamenev.md` |
| 同行 | `../../cards/PER-zinoviev.md` | `../../cards/people/PER-zinoviev.md` |
| 同行 | `../../cards/PER-martov-l.md` | `../../cards/people/PER-martov-l.md` |
| 同行 | `../../cards/PER-stalin.md` | `../../cards/people/PER-stalin.md` |
| 同行 | `../../cards/ORG-psr.md` | `../../cards/organizations/ORG-psr.md` |
| 同行 | `../../cards/CON-soviet.md` | `../../cards/concepts/CON-soviet.md` |
| 同行 | `../../debates/DEB-1917-october-coup-or-social-revolution.md` | `../../historiography/debates/DEB-1917-october-coup-or-social-revolution.md` |
| `timeline/L3_daily/1917-10_october_insurrection.md:280` | `../../debates/DEB-1917-october-coup-or-social-revolution.md` | `../../historiography/debates/DEB-1917-october-coup-or-social-revolution.md` |

### C-P0｜侧车 JSONL 不存在

| 死链 | 出现位置 | 替换 |
|---|---|---|
| `./_w8_candidate_events.jsonl` | `1905-01_bloody_sunday_and_october_soviet.md:3`、`:13`、`:193`；`1917-07_july_days_and_kornilov_affair.md:3`、`:174`；`1922-12_lenins_last_struggle_diary.md:3`、`:176` | 删除该链接 |
| `./_w25_candidate_events.jsonl` | `1912-04_lena_goldfields_and_pravda_upsurge.md:3`、`:14`、`:164`；`1926-07_united_opposition_and_dzerzhinsky_death.md:3`、`:16`、`:180` | 删除该链接 |
| `./_w3_1917_events.jsonl` | `1917-02_february_eight_days.md:3`、`:209`；`1917-10_october_insurrection.md:3`、`:295` | 删除该链接 |
| `../staging_w32_1917_04.jsonl` | `1917-04_lenin_arrival_april_theses_and_milyukov_note.md:3`、`:294` | 删除该链接 |
| `./_w36_1917_11_events.jsonl` | `1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md:3`、`:18`、`:273` | 删除该链接 |
| `_w15_candidate_events.jsonl` | `1923-10_scissors_and_new_course_crisis.md:3`；`1927-10_tenth_anniversary_and_15th_congress.md:3` | 删除“候选账本”链接。L1／L2 链接是好的，留下 |
| `_w36_1924_events.jsonl` | `1924-01_lenin_death_testament_and_lessons_of_october.md:3`、`:12`、`:176` | 删除该链接 |

---

## D. 双历

19 世纪差 12 天。1900-03-01 至 1918-02-14 差 13 天。最后一天俄国旧历是 1918-01-31 [O.S.]＝1918-02-13 [N.S.]，下一天官方日期是 1918-02-14 [N.S.]。改历后的苏俄日期不要补 `[O.S.]`。

### D-P1｜读者直接看到的旧历，同行没有新历

缩写区间 `08-12 / 08-27 [O.S.]`、幕标题 `03-12 至 03-31 [O.S.]` 躲过了“完整 ISO 旧历”正则，下面按日次补上。

| 位置 | 原文片段 | 替换 |
|---|---|---|
| `cards/policies/POL-stolypin-agrarian-reform.md:25` | `` `1906-08-12 / 08-27 [O.S.]` `` | `` `1906-08-12 [O.S.] / 1906-08-25 [N.S.]` `` 与 `` `1906-08-27 [O.S.] / 1906-09-09 [N.S.]` ``。同句 11月9日、6月14日、5月29日三对已经是完整双历，不动 |
| `cards/concepts/CON-constituent-assembly.md:72`（`### 2.3`） | `` `1918-01-05 [O.S.]` `` 向手无寸铁的红旗游行者开枪 | `` `1918-01-05 [O.S.] / 1918-01-18 [N.S.]` `` |
| `cards/concepts/CON-revolutionary-defensism-and-defeatism.md:25` | `` `1917-04-04 [O.S.]` `` 返俄后 | `` `1917-04-04 [O.S.] / 1917-04-17 [N.S.]` `` 返俄后 |
| `cards/events/EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc.md:45` | 伊万诺沃-沃兹涅先斯克枪杀案（`` `1915-08-10 [O.S.]` ``） | 补 `` `/ 1915-08-23 [N.S.]` `` |
| `cards/institutions/INS-state-duma-1906-1917.md:29` | 罗将科 `` `1917-02-27 [O.S.]` `` 任临时委员会主席 | 补 `` `/ 1917-03-12 [N.S.]` `` |
| `cards/people/PER-martov-l.md:47` | `` `1917-10-25 [O.S.]` `` 未能违抗马尔托夫 | 补 `` `/ 1917-11-07 [N.S.]` `` |
| `cards/people/PER-nicholas-ii.md:44` | 早在 `` `1917-02-24 [O.S.]` `` 晚即收到 | 补 `` `/ 1917-03-09 [N.S.]` `` |
| `historiography/debates/DEB-1914-haimson-thesis-stability.md:27` | 科诺瓦洛夫 `` `1914-04-19 [O.S.]` `` | 补 `` `/ 1914-05-02 [N.S.]` `` |
| `historiography/debates/DEB-1918-constituent-assembly-and-soviet-democracy.md:22` | 策烈铁里在 `` `1918-01-05 [O.S.]` `` 立宪会议讲坛 | 补 `` `/ 1918-01-18 [N.S.]` ``。同卡 `:25` 已有完整一对，照它写 |
| `timeline/L3_daily/1905-01_bloody_sunday_and_october_soviet.md:19` | 上篇（1905-01-03 至 1905-01-10 [O.S.]） | 1905-01-03 [O.S.]／1905-01-16 [N.S.] 至 1905-01-10 [O.S.]／1905-01-23 [N.S.] |
| 同卷 `:84` | 下篇（1905-10-07 至 1905-10-21 [O.S.]） | 1905-10-07 [O.S.]／1905-10-20 [N.S.] 至 1905-10-21 [O.S.]／1905-11-03 [N.S.] |
| `timeline/L3_daily/1905-12_petersburg_arrest_and_moscow_uprising.md:17` | `[T2]`（1905-12-02 至 1905-12-19 [O.S.]） | 1905-12-02 [O.S.]／1905-12-15 [N.S.] 至 1905-12-19 [O.S.]／1906-01-01 [N.S.] |
| `timeline/L3_daily/1912-04_lena_goldfields_and_pravda_upsurge.md:18` | `[T2]`（1912-04-04 至 1912-05-01 [O.S.]） | 1912-04-04 [O.S.]／1912-04-17 [N.S.] 至 1912-05-01 [O.S.]／1912-05-14 [N.S.] |
| 同卷 `:71` | **1912-04-11 [O.S.]** 晚间 | 补 `/ 1912-04-24 [N.S.]` |
| `timeline/L3_daily/1917-04_lenin_arrival_april_theses_and_milyukov_note.md:21` | 03-12 至 03-31 [O.S.] | 03-12 [O.S.]／03-25 [N.S.] 至 03-31 [O.S.]／04-13 [N.S.] |
| 同卷 `:101` | 04-02 至 04-17 [O.S.] | 04-02 [O.S.]／04-15 [N.S.] 至 04-17 [O.S.]／04-30 [N.S.] |
| 同卷 `:135` | **1917-04-04 [O.S.]** | 补 `/ 1917-04-17 [N.S.]` |
| 同卷 `:163` | 04-18 至 04-22 [O.S.] | 04-18 [O.S.]／05-01 [N.S.] 至 04-22 [O.S.]／05-05 [N.S.] |
| 同卷 `:205` | 04-24 至 05-05 [O.S.] | 04-24 [O.S.]／05-07 [N.S.] 至 05-05 [O.S.]／05-18 [N.S.] |
| 同卷 `:300` | 1917-04-04/05 [O.S.] 宣读，1917-04-07 [O.S.] 刊于《真理报》 | 04-04/05 [O.S.]＝04-17/18 [N.S.]；04-07 [O.S.]＝04-20 [N.S.] |
| `timeline/L3_daily/1917-07_july_days_and_kornilov_affair.md:19` | 07-02 至 07-07 [O.S.] | 07-02 [O.S.]／07-15 [N.S.] 至 07-07 [O.S.]／07-20 [N.S.] |
| 同卷 `:77` | 08-24 至 08-31 [O.S.] | 08-24 [O.S.]／09-06 [N.S.] 至 08-31 [O.S.]／09-13 [N.S.] |
| `timeline/L3_daily/1917-11_vikzhel_coalition_talks_and_sovnarkom_crisis.md:24` | 10-27 至 11-06 [O.S.] | 10-27 [O.S.]／11-09 [N.S.] 至 11-06 [O.S.]／11-19 [N.S.] |
| 同卷 `:124` | 11-08 至 11-17 [O.S.] | 11-08 [O.S.]／11-21 [N.S.] 至 11-17 [O.S.]／11-30 [N.S.] |
| 同卷 `:164` | 11-17 至 12-09 [O.S.] | 11-17 [O.S.]／11-30 [N.S.] 至 12-09 [O.S.]／12-22 [N.S.] |
| 同卷 `:168` | 11-19 至 12-12 [O.S.] | 11-19 [O.S.]／12-02 [N.S.] 至 12-12 [O.S.]／12-25 [N.S.] |

同卷已经写成完整双历的日次小标题（约 `:144`、`:160`、`:170`、`:180`、`:202`、`:225`、`:231`）不动。

### D-P2｜书目、脚注、文件名里的单侧旧历

可见文字补新历。href 和文件名不要改，否则链接会断。19 世纪 +12，20 世纪至改历前 +13。`[T3]` 里这一类共 41 处；下面每行是一处。同行若已经写出公历或缩写新历，只补标签，不要再加一天。

| 位置 | 旧历 | 补上的新历 |
|---|---|---|
| `cards/concepts/CON-dual-power.md:84` | 1917-03-09 | 1917-03-22 |
| `cards/concepts/CON-dual-power.md:86` | 1917-07-10 | 1917-07-23 |
| `cards/concepts/CON-revolutionary-defensism-and-defeatism.md:81` | 1917-04-04 | 1917-04-17 |
| `cards/concepts/CON-revolutionary-defensism-and-defeatism.md:103` | 1917-04-04 | 1917-04-17 |
| `cards/concepts/CON-soviet.md:56`（`[T3]` §3.2 链接文字） | 1918-01-03 | 1918-01-16。文件名保持旧历 |
| `cards/events/EVT-1861-02-emancipation-of-the-serfs.md:98` | 1861-02-19 | 1861-03-03 |
| `cards/events/EVT-1891-1903-witte-industrialization-and-marxist-labor-turn.md:57` | 1891-01-01 | 1891-01-13 |
| 同卡 `:58` | 1897-06-02 | 1897-06-14 |
| `cards/events/EVT-1905-12-moscow-armed-uprising.md:80` | 1906-04-27 | 1906-05-10 |
| `cards/events/EVT-1914-1916-wwi-mobilization-shell-crisis-and-progressive-bloc.md:52` | 文件名 `1917-03-02_nicholas-ii-abdication-manifesto.md` | 可见文字写 1917-03-02 [O.S.]／1917-03-15 [N.S.]。不改文件名 |
| 同卡 `:57` | 1916-11-01 | 1916-11-14 |
| 同卡 `:58` | 1916-11-29 | 1916-12-12 |
| `cards/meetings/MTG-1917-10-2nd-congress-of-soviets.md:71` | 1917-08-19 | 1917-09-01 |
| `cards/organizations/ORG-kadets.md:55` | 1917-11-28 | 1917-12-11 |
| `cards/organizations/ORG-zemlya-i-volya.md:59` | 1876-12-06 | 1876-12-18 |
| `cards/people/PER-alexander-ii.md:58` | 1881-03-01 | 1881-03-13 |
| 同卡 `:76` | 1861-02-19 | 1861-03-03 |
| 同卡 `:78` | 1881-03-08 | 1881-03-20 |
| `cards/people/PER-axelrod.md:54` | 1917-05-09 | 1917-05-22 |
| `cards/people/PER-chayanov.md:59` | 1888-01-17 | 1888-01-29 |
| `cards/people/PER-chernyshevsky.md:56` | 1864-05-19 | 1864-05-31 |
| 同卡 `:57` | 1828-07-12；1889-10-17 | 1828-07-24；1889-10-29 |
| `cards/people/PER-dan.md:50` | 1917-04-29 | 1917-05-12 |
| 同卡 `:59` | 1917-09-01；1917-10-24 | 1917-09-14；1917-11-06 |
| `cards/people/PER-denikin.md:66` | 1872-12-04 | 1872-12-16 |
| `cards/people/PER-figner.md:53` | 1852-06-25 | 1852-07-07 |
| `cards/people/PER-kondratiev.md:56` | 1892-03-04 | 1892-03-16 |
| `cards/people/PER-lunacharsky.md:56` | 1917-11-02 | 1917-11-15 |
| `cards/people/PER-stolypin.md:55` | 1906-11-09；1910-06-14；1911-03-14；1911-05-29 | 1906-11-22；1910-06-27；1911-03-27；1911-06-11 |
| `cards/people/PER-struve.md:49` | 1915-06-08 | 1915-06-21 |
| `cards/people/PER-tkachev.md:58` | 1844-06-29 | 1844-07-11 |
| `cards/people/PER-witte.md:57` | 1905-10-24；1906-04-22 | 1905-11-06；1906-05-05 |
| `cards/people/PER-zasulich.md:60` | 1878-03-31 | 1878-04-12 |
| `cards/policies/POL-1889-land-captains-and-vyshnegradsky-fiscal-regime.md:51` | 1894-06-03 | 1894-06-15 |
| `cards/policies/POL-stolypin-agrarian-reform.md:51` | 1917-10-26 | 1917-11-08 |
| `timeline/L3_daily/1912-04_lena_goldfields_and_pravda_upsurge.md:177` | 《真理报》1912-04-22 [O.S.] | 补 `/ 1912-05-05 [N.S.]` |
| `timeline/L3_daily/1917-02_february_eight_days.md:236` | 第一号命令 1917-03-01 [O.S.] | 补 `/ 1917-03-14 [N.S.]` |
| `timeline/L3_daily/1917-10_october_insurrection.md:310` | *Pravda* No. 170，1917-10-27 [O.S.] | 补 `/ 1917-11-09 [N.S.]` |
| `timeline/L3_daily/1881-03_march_first_assassination.md:173` | 1881-03-10 [O.S.] 签署、1881-03-12 [O.S.] 印行 | 03-22 [N.S.]；03-24 [N.S.] |
| `timeline/L3_daily/1878-01_zasulich_trial_and_zemlya_volya_split.md:212` | 1879-11-18 [O.S.] | 1879-11-30 [N.S.] |
| `cards/people/PER-gapon.md:28` | `` `1905-03 [O.S.]` `` 褫夺神职 | 这是月份不是日次。写成“1905年3月［旧历，约当公历 3 月下旬至 4 月］”，不要假造某一个日次 |

---

## E. `[T2]` 校勘喧宾夺主：需下沉到 `[T3]` 的 15 张卡

计分只看 `2.1`+`2.3` 里叠床架屋的否定句（“不是／不并成／不可反推／不能写成”）相对这两节正文的密度。`2.2` 不计入。第 16 名 `EVT-1918-1920-russian-civil-war`（密度低于第 15 名）不列入。

总原则：`2.1` 留一句肯定的史实，加一个 `CLM`／`DEB`／`DATA` 锚点。同一事实上的第二句、第三句否定，整段搬到 `[T3]`。下面点名的 B4 事实留在 `[T2]`，不要为了瘦身删掉。

1. `cards/events/EVT-1928-grain-procurement-crisis.md`（密度最高）。`[T2]` 留下：`1927-10-01` 是观察窗口，不是农业年度起点，也不是单一爆发日，更不是“1927 年全面丰收”；产量、商品粮、国家收购、出口是四套分母；收购失败不等于乡下没有粮食，也不等于有组织的政治罢售；Velikanova／OGPU svodki 是保密言论，不是农民投票。B4B-18 留下：Lewin（不只是富农囤积；乌拉尔—西伯利亚方法打到中农）、Carr–Davies 的价格与流量、涅姆钦诺夫（商品粮约 74% 来自中农和贫农；收购量不是产量）、Cohen 论右派的组织失败，以及 1929 年 4 月五年计划、11 月全会、12 月委员会草案三件不能并成一件。`:75`“不以未入藏书目阻断状态升级”整句删除，缺口改放 `[T3]`。

2. `cards/people/PER-sokolnikov.md`。B4B-03、B4B-21 的否定事实必须留在 `2.1`，各留一句：1918-02-23 [N.S.] 他对接受德国条件投了赞成票，不是弃权；不要把 2月23日和 3月3日再加 13 天；1922–1926 年任财政人民委员至 1926-01-16；1925 年要求斯大林去职的新反对派发言是索科尔尼科夫的；1928-07-11 他是传话人，不是布哈林—李可夫—托姆斯基三人团的一员。“亦不能同大会代表总数混算”这类链式否定搬到 `[T3]`。

3. `cards/people/PER-radek.md`。B4A-21 留在 `2.1`：他穿过德国，但作为奥匈臣民被拒绝入境，1917 年春夏留在斯德哥尔摩，十月革命后才到彼得格勒。“不能把监狱会谈直接写成已缔结军事同盟或拉帕洛条约”留一句。其余叠句进 `[T3]`。

4. `cards/events/EVT-1918-09-red-terror-and-left-sr-rupture.md`。留下：开幕代表 678／269／88（合计 1,035）；Rabinowitch p.288 把约 399 人的资格异议当作认真的挑战，但不是已经证明的舞弊总数；左翼社革党中央的计划、刺客、莫斯科支队、外省组织要分开；1918 年粮食独裁不是 1919 年已经制度化的余粮收集制。其余“不能／不得”堆进 `[T3]`。

5. `cards/events/EVT-1918-01-constituent-assembly-dispersal.md`。B4A-04 留在 `2.1`：1918-01-05 [O.S.]／01-18 [N.S.] 开幕，切尔诺夫 244:153，议程 237:146；会议延续到 01-06 [O.S.]／01-19 [N.S.]；热列兹尼亚科夫约 04:00“卫兵累了”是现场强制；同日晚些时候的全俄中执委法令才是制度上的解散，不是 5 日已经存在的法令；梁赞诺夫和洛佐夫斯基是在布尔什维克党团会议上反对，第六次全俄中执委上的抗议是梁赞诺夫和左翼社革党人施泰因贝格。选票表收成一句，指向 `DATA-07`：选举多数不能把选票、席位和党派混用。斯维亚季茨基／Radkey 的 703 席明细搬到 `[T3]`。15 名与 21 名死者不要并成一个区间。

6. `cards/events/EVT-1929-great-turn-and-dekulakization-launch.md`。B4B-18 留下：4 月计划、11 月全会、12 月委员会草案不是“年底已经写好的集体化”。具体数字留下：12月11日苏俄春播计划从 1,500 万公顷提到 2,400 万公顷（+60%），这和全苏约 3,000 万公顷的窗口不是同一个数；截至 12月25日的收购 13,616,151 吨对上年 6,345,277 吨。“不能写成委员会要恢复新经济政策”和“入库增长不证明自愿”各留一句，放进 `[T3]`。

7. `cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md`。B4B-12 留在 `2.1`：第 0116 号令是对森林藏匿点使用窒息性毒气的命令；第 130、171 号是人质／集中营命令，不是毒气令；俄文原件未入藏；不要补一个未经核对的 1921-06-12 签发日；“命令发出”不能写成已经证实的大规模化学伤亡。数字分开留：1921-04-27 图哈切夫斯基受命，05-06 抵达；Leggett 约 21,000（5月）到约 1,200（7月中），7月20日人质约 5,000；Figes 的约 50,000／100,000／15,000 是镇压规模的估计，不是毒气统计。“不能外推全国征收比例”“社革党背景不等于党中央统一指挥，也不等于左翼社革现役部队”“西伯利亚、伏尔加、马赫诺不能并人数”三条短句放 `[T3]`。

8. `cards/people/PER-kollontai.md`。`2.1` 各留一句：1918 年辞去人民委员职务不是退党；早期商务代表／全权代表和后来的大使职名不同；妇女人民委员、妇女部、反对派小册子、外交职务是四段。其余进 `[T3]`。

9. `cards/events/EVT-1923-scissors-crisis.md`。B4B-04 留下：托洛茨基没有在《四十六人声明》上签名；34+12 份正文签名＝46 人，戈尔茨曼再签一次不是第 47 人；他 1923-10-08 的信是平行文本，不是连署。`DATA-02` 留下，并留一句：不要把斯特鲁米林的序列接到国家计委 276／89 的批发指数上，也不要把工业零售 187、农业批发 49 叫成“零售比”。普列奥布拉任斯基的价格税和 1924–28 年理论不是四十六人 1923 年的纲领，也不是后来的强制集体化——这一句放 `[T3]`。

10. `cards/people/PER-tomsky.md`。B4B-21 各留一句：土耳其斯坦之后，他先回到全苏工会中央理事会当书记（1922），不是一口气同时当上主席和政治局委员；1918–1929 是一段跨度，不是连续十一年主席；336:50:18 不是独立工会主义的表决；后来反对左派，也不是“一向反对一党制”。1936 年的死亡日期若写出，保持公历，不要搬家。

11. `cards/events/EVT-1917-10-october-revolution.md`。B4A-10、B4A-18 留下：1917-10-10 [O.S.] 中央委员会开会时苏汉诺夫不在房间里；科尔尼洛夫期间托洛茨基在狱中；十月不要收成“纯粹政变”或“第一天已经不可逆转的一党制”（维克热尔是另一场争论）。留下：派普斯写的冬宫约 5 名死者不是全俄死亡数；马尔托夫约 14:12 的退场不是全体孟什维克退场；左翼社革党留在会场还不等于加入政府。其余瘦掉。

12. `cards/people/PER-uglanov.md`。B4B-01、B4B-23 的三个日期不能并：1924–27 年他是斯大林—布哈林的莫斯科机器（1924年10月起；十四大后为政治局候补委员和组织局委员，1926年1月），并用它对付列宁格勒反对派和联合反对派；1928年夏秋他转向反对把非常措施永久化，维护轻工业和工农结合；1928-10-18/19 全会是已经核对的节点（斯大林的反右倾发言），不是他丢掉全部莫斯科职务的那一天——莫洛托夫正式接手在 11月，Cohen 和 L3 把交接放在 11月27日，任命原件仍未核对；1929年4月他失去中央书记、政治局候补委员和组织局。“温和经济主张不等于基层民主”以及 1932／1937 的结局边界放 `[T3]`。1937-05-31 [N.S.] 的处决是边界；审讯文件不能证明真有一个阴谋，这一句留在 `[T3]`。

13. `cards/events/EVT-1917-02-february-revolution.md`。B4A-11 留在 `2.1`：1917-02-23 [O.S.]／03-08 [N.S.] 的罢工数是暗探局 78,444 人／43 厂、警察 87,534 人／50 厂、列别罗夫 128,388 人／49 厂；43 和 50 不能对调；巴尔克的 `Gradonachal'nik` 不是民选市长。02-24 的三套分母（行政 197,000／131 厂、巴尔克约 200,000、214,111 与 214,112）写成“三套分母”，不要收成“20万至21.4万”。“26日局部哗变，27日才是全面兵变”留一句。第87条“不等于临时政府已经正式废止第87条”搬到 `[T3]`。

14. `cards/people/PER-yagoda.md`。留下两个日期：1928-01-04 对最大私商的逮捕令；1928-03-02 沙赫特报告。“官方履历称 1907 年入党但不能当作定论”、OGPU svodka 不是社会意见总体、“不证明反革命集团”放 `[T3]`。不要替他发明一个入党日。

15. `cards/people/PER-shlyapnikov.md`。B4A-21、B4B-21 留成短句：长谷川 p.251 的原意是“给工人们一块面包，这场运动就会烟消云散”，以及他在 1917-02-25 [O.S.]／03-10 [N.S.] 拒绝发武器，不是一套成熟的亲军队战略。十大在 1921年3月选他进中央是安抚；指派工会领导人和他的辞职抗议发生在 1921年5月的五金工会代表大会，不是 3月的大会会场；1922年的开除动议在三分之二多数上以一票之差未通过（Daniels p.161）。工会表决 336／50／18 另有 2 票弃权，不是全部 694 名有表决权代表，也不是全国工人阶级。“巴库书信”是梅德韦杰夫的，1926年用来同时指控两人；它不是施略普尼科夫的个人文本，也不是 1928年的右派。出生“1885-08-30”的历法未核对，卡上只保留年份是对的，不要加 12 天。重复句搬到 `[T3]`。
