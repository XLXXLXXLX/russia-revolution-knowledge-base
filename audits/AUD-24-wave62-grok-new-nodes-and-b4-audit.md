---
id: AUD-24-wave62-grok-new-nodes-and-b4-audit
type: audit
auditor_model: grok-4.7
target_wave: W62
role: dialectic-auditor
status: remediated
updated_at: "2026-11-23"
---

# AUD-24｜wave62｜新节点逐字引文、页码、双历与 B4 金丝雀｜异源对抗审计

审计日：2026-11-23。只核 Wave 62 当日新增的 19 张 `CLM-*`、10 张 `SCH-*`、1 张 `MTG-1928-04-cc-joint-plenum`，并回看 AUD-23A / AUD-23C 已改过的 `reader/ch09`、`reader/ch13`、`data/DATA-01..08` 抽查、`timeline/L0_macro_epochs.md`、`timeline/L2_chronicles/E10_1927-1929_grain_crisis_and_bukharin_defeat.md`、`glossary/CONCEPT_GENEALOGY_INDEX.md`。引文只打开卡片所引切片，不读全书。严重度沿用 AUD-23A：P0 为伪造逐字引文、错误数字或错误分母；P1 为把两个已核事实焊成一句，或把转述、表格复原写成引文，或页码错位；P2 为缺公历孪生日、路径边界与残余措辞。

本轮重开并读过的切片：Fitzpatrick `ch02_p_746.md`、`ch26_p_770.md`；Priestland `ch00_pages_1-25.md` 期刊页 40、43、50、56；Khlevniuk `ch01_p_535.md`、`ch02_p_536.md` 与 `manifest.yaml`；《如何打破》`ch01_pages_26-50.md`、`ch12_pages_301-325.md`；《悲剧》第 1 卷 `ch13_pages_326-350.md`、`ch02_pages_51-75.md`；陈爱茹 `ch00_pages_1-9.md`；伊利尤霍夫论断卡；会议卡与鲍曼学者卡的 `[T1]`。达维季安三节、高丹末页、鲍曼 `ch23_p_278.md` 的 `sixty pei-cent` 在上一轮已按行读过，本轮不把 OCR 断词或同形字母层的检索落空再立案。

## 已核、不立案

- **双历。** 新 `CLM-*` 里成对的 `[O.S.] / [N.S.]` 差值正确：1900-03-01 前为 +12，该日之后至 1918-02-14 为 +13。没有把 1918-02-14 之后的苏俄日期再写成 `[O.S.]`。陈爱茹的 `1917-10 [O.S.] / 1917-11 [N.S.]` 是月份标签，不是日差。日内瓦与改历后日期保持单公历。
- **`[T1]` 长度。** 10 张新 `SCH-*` 与 `MTG-1928-04` 的 `[T1]` 非空白字符分别为 107、127、124、112、112、108、113、110、113、120、126，全部 ≤150。
- **外键。** 新 `CLM` 的 `scholar`、`debate`、`targets_cards` 以及 `supports` / `rebuts` / `qualifies` 里的卡片号，在 `cards/`、`historiography/`、`data/`、`glossary/` 内都能解析。
- **书目身份没有写错的几张。** Melancon：*Soviet Studies* 40:3 (1988)；卡片已声明目录页比原刊多 1（期刊 p. 479 = `ch01_p_480.md`），三条英文引文对得上，不把目录错页再立案。Rieber：*AHR* 106:5 (2001)，三条引文对得上；`1908-03-02/03-15`、`1912-12-01/12-14` 为 +13；`1918-02-24` 与 `1922-09-22` 只有 `[N.S.]`。Priestland 的刊名、年、页界是对的：*Revolutionary Russia* 10:2 (1997), pp. 37–61。错的是下面 P0 的三句引文，不是题录。Khlevniuk 的 *Cahiers du Monde russe* 42:2/4、pp. 535–547，以及标题里的战后限定，与 `ch00` / `ch01` 页眉一致。Gregory：`publication_year: 1979` 是对的；文件夹名是 1976 年合著，卡片已说明脚注 1 摘要的是 Gregory & Sailors, *JEH* 36:4 (1976)。
- **引文对得上、不因断词或同形 OCR 立案。** Gaudin：66/95 与末页 “Practical marginalization…”（`ch27_p_773.md`）在去连字符后就是印出的句子。Bowman：直接税预算份额是 “from twenty percent in 1885 to sixty pei-cent in 1914”（`ch23_p_278.md`）；`pei-cent` 是 per cent 的 OCR。这是萎缩中的直接税预算份额，不是加拉霍夫所说的利润少报两成，也不是普拉根博格的消费税口径。`SCH-bowman-linda` 的 `[T1]` 把 60% 放在 1885–1914 这一句里，数字本身不是假的。达维季安三节是拉丁同形字母层上的俄文复原，行号与卡片所引 `ch01_p_117.md`、`ch03_p_119.md`、`ch08_p_124.md` 一致，不是编造。Sanborn 的 17 省与 51 / 9 / 136 / 216（合计 412）句、Hasegawa、Hatch、Hoch、Frank/Engelstein、Melancon、Rieber 的已对上引文，不重复立案。陈爱茹 p. 77 “是通过市场、价格及税务手段剥夺富农还是通过非常措施剥夺富农问题”与 p. 79 “他成了中农的坚决捍卫者，而中农又无法解决粮食问题”都在 `ch00_pages_1-9.md`（约 L575–576、L856–858），是断行后的原句，不立案。
- **第 107 条的格子是真的，页码和引文格式另案。** 《悲剧》第 1 卷 `ch13_pages_326-350.md` 在 `## [PDF p. 337]` 下印出司法部四月统计：5,597 = 3,691 + 601 + 1,038 + 61 + 18 + 188。中农 1,038 与 18,5% 是格子里的数字，不是编造。六类人数加总等于 5,597。
- **抗议与恐怖的两套分母不要焊。** 《悲剧》第 1 卷 `ch02_pages_51-75.md` 在 `## [PDF p. 59]` 的全年总计行是 `709 1307 1027 9093`（1928 年抗议 / 1929 年抗议 / 1928 年恐怖 / 1929 年恐怖）。`95 208` 逮捕与 8,278 / 1,190 属于《苏维埃农村》第 2 卷 1930-01-15 初步数，不在这张 1931 年 3 月定稿表上。悲剧卡没有把 95,208 写进这张表。
- **四月全会里已经钉住的程序事实。** 《如何打破》第 1 卷 `ch12` DjVu p. 314：决议“作为基础” `Принято единогласно`；随后单独表决把 ВТУЗ 条款从该决议删去并交下次全会，主席问“谁反对？少数。”多数删去成立，不得把“一致通过”安到 ВТУЗ 表决上，也不得写成移交案已通过。`ch01` L287–290：编者写“по-видимому, истек срок соглашения «не драться при всех»”；末次会议后，4 月 13 日斯大林在莫斯科、布哈林在列宁格勒作报告。同卷 `ch00` 里这句是布哈林自己的话（“Я сам не мог говорить, чтобы не драться при всех”），谈的是工业化速度，不是 303 人出席决议。
- **AUD-23A / 23C 已经补上、本轮不再打开的口径。** `reader/ch09`：第 0116 号不再写 1921-06-12，脚注也不再写“已为档案坐实”；喀琅施塔得是 17 日深夜约千余人撤往芬兰，累计约八千人是全战役踏冰人数。`reader/ch13`：25.4 万吨限定为冬麦主产区；1.4 亿普特跌至 500 万普特标明是斯大林 4 月 22 日演说；1929-03-20 批准的是村社自我摊派，五倍罚款分开写为西伯利亚约 4 月 10 日、全俄中央执行委员会 4 月 28 日、6 月底写入刑法典第 61 条。`DATA-04`：劳动解放社是 `1883-09-25 [N.S.]` 日内瓦事件，并禁止倒推 `1883-09-12 [O.S.]`；1929 年 4 月全会写明不得把赞成票回算成 232。术语表：民粹主义 1905–1914 格已是“社会革命党／劳动派”，不再放入劳动解放社；社会主义原始积累的 1924–26 已在 1921–1927 列；余粮收集制格把 1928-01 第 107 条和 1929-03 方法名分成两段；村社行有 1922 年土地社；苏维埃的 1860s–1904 格是空位。这些旧 P0 没有在抽查过的格子里复发。

## P0

### P0-01　Fitzpatrick 1993 三条“逐字引文”不是印出的句子

- 位置：[CLM-fitzpatrick-1993-ascribing-class-and-lishentsy-identity.md:32](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-fitzpatrick-1993-ascribing-class-and-lishentsy-identity.md:32)–[34](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-fitzpatrick-1993-ascribing-class-and-lishentsy-identity.md:34)
- 依据：抽取稿里没有 `uncanny resemblance`、`two friendly classes`、`kolkhozniki`、`classless`。p. 746 的原句在 [ch02_p_746.md:11](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/articles/fitzpatrick_1993_ascribing_class_social_identity_soviet_russia/ch02_p_746.md:11)–[14](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/articles/fitzpatrick_1993_ascribing_class_social_identity_soviet_russia/ch02_p_746.md:14)。期刊 p. 770 的原句在 [ch26_p_770.md:10](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/articles/fitzpatrick_1993_ascribing_class_social_identity_soviet_russia/ch26_p_770.md:10)–[24](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/articles/fitzpatrick_1993_ascribing_class_social_identity_soviet_russia/ch26_p_770.md:24)，说的是对国家的关系、`Stalinist soslovnost'` 和 latterday “service nobility”，不是 1936 年“两个友好阶级”。卡片把 p. 746 的 `sosloviia-classes` 写成了 `soslovie-classes`。题名、1993 年、pp. 745–770，以及 `1917-11-11 [O.S.] / 1917-11-24 [N.S.]`（+13）仍然成立，不要连这些一起改掉。

Target →

`p. 745` 的 “Instead of becoming a classless society… uncanny resemblance…”；`p. 746` 的 “In practice, class ascription… Soviet 'soslovie-classes'.”；`p. 769` 的 “two friendly classes (workers and kolkhozniki)…”。

Replacement →

删掉这三句“逐字引文”。若保留论点，只能改写成转述，并改用下面两处印出的句子：

p. 746：`The main thesis of this article is that the process of revolutionary ascription produced social entities that looked like classes in the Marxist sense, and were so described by contemporaries, but might more accurately be described as Soviet sosloviia. Whether, in addition to these "sosloviia-classes," ...`

p. 770：`the "classes" of Stalinist society should have been defined, like sosloviia, in terms of their relationship to the state rather than, like Marxist classes, in terms of their relationship to each other. ... Within the framework of "Stalinist soslovnost'," this class becomes a latterday "service nobility" ... and other soslovie-classes fall into place ...`

不要补写“两个友好阶级”或集体农庄庄员这句引文。1936 年 4 月 20 日《真理报》若仅出现在脚注，就保持脚注，不要升成斯大林的逐字引文。

### P0-02　Priestland 1997 三条英文“逐字引文”是拼出来的

- 位置：[CLM-priestland-1997-political-vs-businesslike-party-state-1918-1921.md:32](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-priestland-1997-political-vs-businesslike-party-state-1918-1921.md:32)–[34](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-priestland-1997-political-vs-businesslike-party-state-1918-1921.md:34)
- 依据：刊名、10:2、1997、pp. 37–61 正确，1928–29 延伸也已在限定句里标明。错的是三句引文和页码。期刊 p. 40（PDF p. 6，[ch00_pages_1-25.md:194](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/articles/priestland_1997_bolshevik_ideology_party_state_relations/ch00_pages_1-25.md:194)–[204](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/articles/priestland_1997_bolshevik_ideology_party_state_relations/ch00_pages_1-25.md:204)）的原句是 “and will argue that the apparent illogicality of the Left's position … was not primarily concerned with the demarcation of the power and competence of institutions.” 没有 “I will argue … division of labour … styles of leadership and administration.” 这句。期刊 p. 43（PDF p. 9）谈的是把民主理解成讨论和官员的 leadership 'style'，不是卡片那句政治工作对经济工作的词典定义。`businesslike` 出现在期刊 p. 50。“styles of leadership” 最近的原句也在 p. 50：[ch00_pages_1-25.md:674](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/articles/priestland_1997_bolshevik_ideology_party_state_relations/ch00_pages_1-25.md:674)–[676](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/articles/priestland_1997_bolshevik_ideology_party_state_relations/ch00_pages_1-25.md:676)。期刊 p. 56（PDF p. 22）写的是 “As one commentator put it, having planned to 'partyise' (opartiif) the state, the Bolsheviks came to 'statise (ogosudarstvif) the party'.” `ogosudarstvit'` 是 OCR `ogosudarstvif` 的校读，可以保留，但主语是 “one commentator”，不是领导层自己的动词，也没有卡片那句 “Paradoxically, while the leadership constantly warned…”。Glavpolitput' 与政治部的史实在 PDF pp. 21–22，可以留在论证链里，不能留在引文栏。

Target →

三条以 “I will argue” / “In the Bolshevik lexicon” / “Paradoxically” 开头、并标成 p. 39、p. 43、p. 51 的块引文。

Replacement →

引文栏只保留印出的句子，页码改为期刊页：

p. 40：`and will argue that the apparent illogicality of the Left's position, and indeed of that of the leadership, can be explained if we understand a particular rhetoric about institutions within Bolshevik political discourse, which was not primarily concerned with the demarcation of the power and competence of institutions.`

p. 50：`The party and the state were therefore often seen in these debates as institutions which had particular styles of leadership and approaches to authority.`

p. 56：`As one commentator put it, having planned to 'partyise' (opartiif) the state, the Bolsheviks came to 'statise (ogosudarstvif) the party'.`

论证链里的党政边界论点可以改成对这三句的转述，并写明 `statise` 是评论者的概括。

## P1

### P1-01　第 107 条四月表被写成一篇散文引文，而且页码、类别名和 10.7% 都偏了

- 位置：[CLM-tragedy-village-v1-1927-1929-emergency-measures-and-peasant-terror.md:29](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-tragedy-village-v1-1927-1929-emergency-measures-and-peasant-terror.md:29)、[:34](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-tragedy-village-v1-1927-1929-emergency-measures-and-peasant-terror.md:34)
- 依据：[ch13_pages_326-350.md:422](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/primary/tragedy_soviet_village_v1_1927_1929_zh/ch13_pages_326-350.md:422)–[447](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/primary/tragedy_soviet_village_v1_1927_1929_zh/ch13_pages_326-350.md:447)，节标是 `## [PDF p. 337]`，不是卡片写的 PDF p. 345。表头类别是“富农、富裕中农、中农、贫农、工人和其他职员”。OCR 把百分比印成 `66% 10% 1,1% 0,3% 3,4%` 和 `18,5%`。601 / 5,597 = 10.74%，卡片的 10.7% 是为了让六格凑成 100 而做的复原，不是印出的 `10%`。省略号丢掉了工人 18 人（0.3%）和其他职员 188 人（3.4%）。只加四个农民类别等于 5,391，不是 5,597。紧接着的 5–6 月 56 份判决是另一行：富农 13（23.2%）、富裕农民 27（48.2%）、中农 16（28.6%）。“富裕农民”只属于这 56 人样本。瑟尔佐夫 / 艾赫的“93% 富农”卡片已分开写，保持分开。1928→1929 的 709 / 1,307 与 1,027 / 9,093 在 [ch02_pages_51-75.md:320](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/sources/primary/tragedy_soviet_village_v1_1927_1929_zh/ch02_pages_51-75.md:320)，不在这张四月表上。布哈林“不可避免地更加严厉”和 1929-10-03“直至枪决”两句，本轮没有用连续字符串再次钉住，不升格为伪造，也不要在修订时顺便把它们写成新的逐字引文。

Target →

`4 月份根据《刑法典》第 107 条被起诉的 5,597 人中，富农占 3,691 人（66%），富裕农民 601 人（10.7%），中农 1,038 人（18.5%），贫农 61 人（1.1%）……`，并标注 PDF p. 345。

Replacement →

`Doc 115 所引司法人民委员部 1928 年 4 月统计在本卷 PDF p. 337，不是 PDF p. 345。印出的是一张表，不是下面这句散文。表头六类合计 5,597 人：富农 3,691（印作 66%）、富裕中农 601（印作 10%；601/5597≈10.7%，是复原值）、中农 1,038（18.5%）、贫农 61（1.1%）、工人 18（0.3%）、其他职员 188（3.4%）。不要把四月的 601 写成“富裕农民”。5–6 月另有 56 份判决：富农 13（23.2%）、富裕农民 27（48.2%）、中农 16（28.6%）。`

### P1-02　四月全会的 303 人分解、八次会议和星号密款还没有议事录页；“当众不打架”被说成了出席决议

- 位置：[CLM-kak-lomali-nep-1928-v1-april-joint-plenum-shakhty-and-grain.md:24](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-kak-lomali-nep-1928-v1-april-joint-plenum-shakhty-and-grain.md:24)、[:36](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-kak-lomali-nep-1928-v1-april-joint-plenum-shakhty-and-grain.md:36)–[:43](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-kak-lomali-nep-1928-v1-april-joint-plenum-shakhty-and-grain.md:43)；[MTG-1928-04-cc-joint-plenum.md:20](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1928-04-cc-joint-plenum.md:20)、[:25](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1928-04-cc-joint-plenum.md:25)–[:27](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1928-04-cc-joint-plenum.md:27)
- 依据：68+47+180+8=303 内部算术成立，但本轮在 `ch12` 的表决页、`ch20` 索引和 `ch00` 导言里没有找到这行出席名单。`ch20` 里的 303 是人名索引页码；同卷另有 30 万普特和 3 亿普特，不是 300 名代表。索引只有“Протокол №2 … от 6-11 ап-”一行，不能代替议事录正文。`нет таких крепостей`、`тенденция к перелету`、`личного состава специалистов` 三串本轮没有作为连续原文钉住，先降为待核，不要维持“逐字”状态。已经钉住、应留在已核的是：ВТУЗ 条款多数删去、基础决议一致通过、4 月 13 日双城报告。

Target →

导言被写成：最高层为了不在三百余名与会者面前当众内讧而保持沉默，并给这句安上议事录第 2 号的 303 人分解。`[T1]` 写“8 次会议、303 人出席”。星号密款写成已核的逐字条款。

Replacement →

`«не драться при всех» 是布哈林谈工业化速度时的原话。编者在全会结束后推论“по-видимому, истек срок соглашения «не драться при всех»”，并记下 4 月 13 日斯大林在莫斯科、布哈林在列宁格勒分别作报告。这不是一份写着 303 人的表决记录，也不是政治局通过的“不当众争吵”决议。中委 68、候补 47、中监委 180、中审委 8、合计 303，以及“8 次会议”，在所引切片里尚未钉住；钉住之前，[T1] 和 [T2] 不得把这组数字写成议事录第 2 号的已核原文。ВТУЗ 移交条款是在基础决议一致通过之后，被另一次表决以多数删去并推迟的，反对者是少数。星号密款和上述三条口号在连续原文钉住之前，移出逐字引文栏。`

### P1-03　Khlevniuk 2001 的四条 «» 是校读层上的概括，而且被接到了 1928 年沙赫蒂

- 位置：[CLM-khlevniuk-2001-stalin-and-ogpu-mechanism.md:23](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-khlevniuk-2001-stalin-and-ogpu-mechanism.md:23)–[:37](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-khlevniuk-2001-stalin-and-ogpu-mechanism.md:37)
- 依据：正文是拉丁同形字母 OCR。`ch02_p_536.md` 可以读出的骨架是：机构在实践中直接服从党的领导、首先是斯大林；斯大林借助 ОГПУ–НКВД 对党政机关做大规模清洗。这个意思在战后论文里。`«главная опора системы»`、`«обеспечение собственно диктаторских полномочий Сталина»`、`«контролировали ОГПУ»`、`«под контроль партии»` 四串没有作为印出的句子收回来。卡片括号已经承认实证主体是 1945–1953，却把“20 年代起源”写成 pp. 535–536 的论断，并把卡片挂到 `EVT-1928-shakhty-affair-show-trial` 和 `DEB-1922-lenin-testament-and-stalin-rise`。卷期、页码、战后标题不要改。

Target →

四条用 «» 标成“依据该刊 PDF 文本层校译”的逐字片段，以及“论文明确将动用契卡机关参与党内斗争追溯至 20 年代”这句。

Replacement →

`逐字栏在拿到可逐字核对的文本层之前先清空。可以保留的转述只有：该文讨论的是战后国家安全机关；第 536 页能够读出的是，机关名义上与人民委员会有关，实践中服从党的领导、首先是斯大林，并被用来清洗党政机关。1920 年代派系斗争和 1928 年沙赫蒂案不是这篇文章的实证范围。若仍要作结构类比，放到论证链的明确推论句里，不要写成 pp. 535–536 的原文，也不要让这张卡单独支撑沙赫蒂或 1922 年遗嘱辩论。`

### P1-04　E10 仍把五倍罚款写进 1929-03-20 政治局批准的方法

- 位置：[E10_1927-1929_grain_crisis_and_bukharin_defeat.md:33](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L2_chronicles/E10_1927-1929_grain_crisis_and_bukharin_defeat.md:33)
- 依据：同文件 L9、L32 已经把 1928 年 1 月西伯利亚之行和第 107 条，与后来才定名的方法分开，这一半保持。L33 后半仍写：以“贫中农自我摊派”与五倍罚款为核心的正式方法，在 1929 年 3 月 20 日政治局批准后定型。这与已经改过的 [ch13_grain_crisis_and_right_opposition_defeat.md:51](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch13_grain_crisis_and_right_opposition_defeat.md:51) 冲突。术语表余粮收集制行没有把五倍罚款写进 3 月 20 日，不要按 E10 这句改回去。

Target →

`而绕开村社法定人数、以“贫中农自我摊派”与五倍罚款为核心的正式“乌拉尔—西伯利亚方法”，则是在 1928 年底至 1929 年 3 月 20 日政治局批准后方才定型并推向全苏。`

Replacement →

`绕开村社法定人数、以贫中农自我摊派为内容的正式“乌拉尔—西伯利亚方法”，在 1928 年底至 1929 年 3 月 20 日政治局批准后定型。五倍罚款不是 3 月 20 日那条决议的内容：西伯利亚约自 4 月 10 日起执行，全俄中央执行委员会 4 月 28 日授权，6 月底写入《苏俄刑法典》第 61 条第 3 款。`

## P2

### P2-01　改历前若干 `[O.S.]` 没有公历孪生日

成对日期的日差没有算错。缺的是孪生日本身。抽到的孤日包括普拉根博格卡上的 `1884-06-05`、`1885-01-15`（同日另一处已正确写成 / `1885-01-27`）、`1885-04-30`、`1887-12-21`（+12 应为 `1888-01-02`），以及 Gaudin 的 `1893-06-08`（+12 应为 `1893-06-20`）。Hasegawa 与 Melancon 里还有一批不带年份、也不带 `[N.S.]` 的日次。19 世纪加 12 日，1900-03-01 之后加 13 日。不要为 1918-02-14 之后的日期补 `[O.S.]`。

### P2-02　Gregory 1979 的第二条引文不在 YAML 所写的那一页

[CLM-gregory-sailors-1976-witte-gold-standard-monetary-policy.md](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-gregory-sailors-1976-witte-gold-standard-monetary-policy.md) 的 `local_source_path` 只指向 `ch01_p_379.md#L23-L51`。第二条引文的词在 `ch15_p_393.md`，不在这条路径里。引文可以留，路径要扩到实际页，或者把第二条移出“该路径已核”的范围。1979 与 1976 的篇名区分保持现状。

### P2-03　ch09 已把 1.02 从 1918 年下跌上拆开，但仍把它写成实物配给的结果

- 位置：[ch09_war_communism_and_kronstadt_turn.md:15](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch09_war_communism_and_kronstadt_turn.md:15)
- 依据：[CLM-ilyukhov-war-communism-leveling-vs-nep-piecework.md:21](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-ilyukhov-war-communism-leveling-vs-nep-piecework.md:21)、[:25](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-ilyukhov-war-communism-leveling-vs-nep-piecework.md:25)。1.02:1 是 1920 年全国技工/杂工工资比。配给“众人同等”和工资比是相邻的两件事；1920 年收入 92.6% 为实物，不能因此把工资比本身叫做配给差距。1918 年秋 24%–60% 的下跌已经用分号隔开，旧 P0 的因果焊接不再成立，所以这里只降为 P2。

Target →

`即便如此，实物配给平均化仍使 1920 年全国熟练工与杂工的工资比被压缩至约 1.02 比 1。`

Replacement →

`1920 年全国熟练工与杂工的工资比约为 1.02 比 1。这是工资比，不是 1918 年秋那次生产率下跌的原因，也不要把这个比值本身写成实物配给差距。`

## B4 金丝雀（只写入本报告，不改套件文件）

下一空号：B4A-22–24（现有末号 B4A-21），B4B-25–27（现有末号 B4B-24）。B4B-25 不把尚未钉住的 303 人分解写成 gold。B4B-27 不重复 B4B-24 的 232 / 60 票陷阱。

```jsonl
{"id": "B4A-22", "era": "1861-1918.03", "category": "quantitative_denominator", "split": "dev", "origin": "audit_regression:AUD-24", "question": "1890–1901 年城乡消费税负担、城市工商界在全部税收中的份额，和 1885–1914 年工商业在直接税预算中的份额，能不能合成一个“农民或工商业负担了六七成”？1887 年赎回支付跳增，以及加拉霍夫所说企业至少少报两成利润，又分别是什么？", "target_cards": ["CLM-plaggenborg-1990-bowman-1993-tsarist-industrialization-tax-incidence", "SCH-bowman-linda", "CLM-hoch-1994-wheatcroft-1974-peasant-living-standards-and-grain-stats"], "source_anchors": ["historiography/claims/CLM-plaggenborg-1990-bowman-1993-tsarist-industrialization-tax-incidence.md", "historiography/scholars/SCH-bowman-linda.md", "sources/articles/bowman_1993_russia_business_tax_slr/ch23_p_278.md"], "gold_facts": ["普拉根博格给出的是两套分母：1901 年前后消费税约 35% 落在城市工商业、约 65% 落在农村；城市工商业缴纳的税款又约占全部税收的 70%。65% 与 70% 不能合成一个税种。", "鲍曼写的是萎缩中的直接税预算：工商业份额从 1885 年的 about twenty percent 升到 1914 年的 sixty per cent（抽取稿作 sixty pei-cent）。这不是全部税收的 60%，也不是 1901 年消费税的 65% 或 70%。", "加拉霍夫估计企业至少少报两成利润，是另一句话，不能拿去解释 1885 年那个 20% 的预算份额。赎回支付在 1887 年的跳增不是收成数字。"], "trap_assertions": ["65% 的农村消费税、70% 的全部税收和 60% 的直接税是同一个负担率", "1885 年工商业只承担直接税的 20%，是因为企业少报了 20% 的利润", "1887 年赎回支付跳增证明当年粮食歉收"], "required_perspectives": ["fiscal_history", "peasant_living_standards"], "created_at": "2026-11-23", "author": "dialectic-auditor:grok-4.7", "must_contain_any": [["35", "65"], ["70"], ["1885", "1914", "60", "直接税"]], "forbid_patterns": ["65%的农村消费税、70%的全部税收和60%的直接税是同一个负担率", "1885年那个20%是因为企业少报了20%的利润"]}
{"id": "B4A-23", "era": "1861-1918.03", "category": "chronology_trap", "split": "dev", "origin": "audit_regression:AUD-24", "question": "1914 年 7 月动员骚乱波及多少省，死伤如何分成军警与骚乱者，原因能不能收成酒类专卖，日期该用哪一种历差？", "target_cards": ["CLM-sanborn-2000-july-1914-mobilization-riots-and-nation", "SCH-sanborn-joshua"], "source_anchors": ["historiography/claims/CLM-sanborn-2000-july-1914-mobilization-riots-and-nation.md", "historiography/scholars/SCH-sanborn-joshua.md"], "gold_facts": ["桑伯恩统计的是 17 个省的动员骚乱，不是只有巴尔瑙尔一地。", "死亡按身份分开：军人 51、文职官员 9，骚乱者 136 人死亡、216 人受伤一类的分项合计为 412，不能把 412 写成清一色的平民死亡或清一色的军警死亡。", "1914 年 7 月仍在改历之前，俄历换公历用 +13。酒类专卖冲突只是骚乱场合之一，不能写成唯一原因。"], "trap_assertions": ["1914年7月动员骚乱只发生在巴尔瑙尔，而且完全是因为酒类专卖", "412名死者全部是平民，或者全部是军警", "1914年7月17日俄历只需加12天才是公历7月29日"], "required_perspectives": ["military_social_history", "dual_calendar"], "created_at": "2026-11-23", "author": "dialectic-auditor:grok-4.7", "must_contain_any": [["17"], ["51", "136", "412"], ["13", "公历"]], "forbid_patterns": ["动员骚乱只发生在巴尔瑙尔", "412名死者全部是平民"]}
{"id": "B4A-24", "era": "1861-1918.03", "category": "attribution_trap", "split": "dev", "origin": "audit_regression:AUD-24", "question": "1917 年 2 月末彼得格勒街头的社会主义传单，是布尔什维克地下印刷所已经印好的，还是区联派和社会革命党印的？Melancon 1988 的期刊页和抽取目录页差在哪里？", "target_cards": ["CLM-melancon-1988-february-1917-interparty-socialist-proclamations", "SCH-melancon-michael"], "source_anchors": ["historiography/claims/CLM-melancon-1988-february-1917-interparty-socialist-proclamations.md", "historiography/scholars/SCH-melancon-michael.md"], "gold_facts": ["Melancon 的考证是：布尔什维克印刷所在 1916 年 12 月被查封，二月底他们只印出一张传单；2 月 27–28 日（俄历）街上的大批传单来自区联派和社会革命党的印刷所。不能把明茨 / 布尔贾洛夫“布尔什维克早已印好”的旧说恢复成已核事实。", "期刊原页是 Soviet Studies 40:3 (1988) 的 pp. 479、481–496。抽取目录把页码加了 1，所以期刊 p. 479 对在 ch01 标成 p. 480 的文件。引用时要写明这是目录错位，不能把 ch01 的 480 当成期刊页。", "1917 年 2 月的俄历 / 公历差是 +13。"], "trap_assertions": ["1917年2月27日前布尔什维克地下印刷所已经印好并散发了街上的大部分社会主义传单", "Melancon原文的第479页就是抽取文件标注的第480个期刊页，无需声明目录加1"], "required_perspectives": ["socialist_interparty", "bibliographic_control"], "created_at": "2026-11-23", "author": "dialectic-auditor:grok-4.7", "must_contain_any": [["区联", "社会革命党"], ["479", "480"], ["1916", "12"]], "forbid_patterns": ["布尔什维克地下印刷所已经印好并散发了街上的大部分社会主义传单"]}
{"id": "B4B-25", "era": "1918.03-1929", "category": "archival_count_trap", "split": "dev", "origin": "audit_regression:AUD-24", "question": "1928 年 4 月 6–11 日联席全会：ВТУЗ 条款是怎样表决的，4 月 13 日谁在哪座城市作报告，“не драться при всех” 是什么性质的句子？68+47+180+8=303 能不能当作已经钉住的议事录原文？", "target_cards": ["MTG-1928-04-cc-joint-plenum", "CLM-kak-lomali-nep-1928-v1-april-joint-plenum-shakhty-and-grain"], "source_anchors": ["cards/meetings/MTG-1928-04-cc-joint-plenum.md", "historiography/claims/CLM-kak-lomali-nep-1928-v1-april-joint-plenum-shakhty-and-grain.md", "sources/primary/kak_lomali_nep_1928_v1_ru/ch12_pages_301-325.md", "sources/primary/kak_lomali_nep_1928_v1_ru/ch01_pages_26-50.md"], "gold_facts": ["沙赫蒂决议先被作为基础一致通过（Принято единогласно）。ВТУЗ 移交最高国民经济委员会的条款是另一次表决：主席宣布反对者为少数，条款被删去并推迟到下次全会。不能把“一致通过”安到 ВТУЗ 表决上，也不能写成移交案已经通过。", "«не драться при всех» 是布哈林自己的话，场合是工业化速度。编者用“по-видимому”推论，全会结束后这项默契到期。它不是点过 303 人的决议。", "4 月 13 日斯大林在莫斯科、布哈林在列宁格勒分别作报告。中委 68、候补 47、中监委 180、中审委 8、合计 303，以及“8 次会议”，在已核切片里还没有议事录页；索引里的 303 和 30 万普特都不是出席人数。"], "trap_assertions": ["1928年4月全会以一致通过的方式批准把高等技术院校移交最高国民经济委员会", "议事录第2号原文已经写明出席303人，即中委68、候补47、中监委180、中审委8", "政治局通过决议，要求不要在303名代表面前当众争吵"], "required_perspectives": ["post_soviet_archival", "stenographic"], "created_at": "2026-11-23", "author": "dialectic-auditor:grok-4.7", "must_contain_any": [["一致", "единогласно"], ["少数", "删"], ["4月13", "13 апреля", "列宁格勒"]], "forbid_patterns": ["一致通过的方式批准把高等技术院校移交", "议事录第2号原文已经写明出席303人"]}
{"id": "B4B-26", "era": "1918.03-1929", "category": "table_reconstruction_trap", "split": "dev", "origin": "audit_regression:AUD-24", "question": "1928 年 4 月按刑法第 107 条被追究的人里，中农占 18.5% 这张表在哪一页，六类人怎么加，10.7% 和 5–6 月的 48.2% 各是什么？", "target_cards": ["CLM-tragedy-village-v1-1927-1929-emergency-measures-and-peasant-terror", "POL-ural-siberian-method"], "source_anchors": ["historiography/claims/CLM-tragedy-village-v1-1927-1929-emergency-measures-and-peasant-terror.md", "sources/primary/tragedy_soviet_village_v1_1927_1929_zh/ch13_pages_326-350.md"], "gold_facts": ["表在《苏联农村的悲剧》第1卷 PDF p. 337，不是 PDF p. 345。四月合计 5,597 人：富农 3,691（印作 66%）、富裕中农 601（印作 10%）、中农 1,038（18.5%）、贫农 61（1.1%）、工人 18（0.3%）、其他职员 188（3.4%）。六类人数之和是 5,597。只算四个农民类别得到 5,391。", "10.7% 是 601/5597 的商，不是印出的百分数。印出的是 10%。“富裕农民”不是四月这 601 人的表头。", "5–6 月另有 56 份判决：富农 13（23.2%）、富裕农民 27（48.2%）、中农 16（28.6%）。瑟尔佐夫和艾赫电告的“约 93% 是富农”是地方口径，不能替换这张全苏四月表。"], "trap_assertions": ["四月5597人中的601名富裕农民占10.7%，四个农民类别已经把5597人算完", "这张18.5%的表印在PDF第345页", "5月至6月56人样本里的48.2%就是四月表里的富裕中农份额"], "required_perspectives": ["post_soviet_archival", "judicial_statistics"], "created_at": "2026-11-23", "author": "dialectic-auditor:grok-4.7", "must_contain_any": [["337"], ["5597", "5,597"], ["1038", "1,038", "18.5", "18,5"], ["56", "48.2"]], "forbid_patterns": ["这张18\\.5%的表印在PDF第345页", "四个农民类别已经把5597人算完"]}
{"id": "B4B-27", "era": "1918.03-1929", "category": "chronology_trap", "split": "dev", "origin": "audit_regression:AUD-24", "question": "1929 年 3 月 20 日政治局批准的“乌拉尔—西伯利亚方法”包不包括五倍罚款？95,208 次逮捕、8,278 起恐怖、1,190 起抗议，和 1,307 起抗议、9,093 起恐怖，各是哪一份文件？", "target_cards": ["CLM-tragedy-village-v1-1927-1929-emergency-measures-and-peasant-terror", "CLM-sovetskaya-derevnya-ogpu-v2-1923-1929-rural-moods-and-repression", "POL-ural-siberian-method"], "source_anchors": ["reader/ch13_grain_crisis_and_right_opposition_defeat.md", "timeline/L2_chronicles/E10_1927-1929_grain_crisis_and_bukharin_defeat.md", "sources/primary/tragedy_soviet_village_v1_1927_1929_zh/ch02_pages_51-75.md", "historiography/claims/CLM-sovetskaya-derevnya-ogpu-v2-1923-1929-rural-moods-and-repression.md"], "gold_facts": ["1929-03-20 政治局批准的是村社自我摊派这一套正式方法。五倍罚款的步骤在其后：西伯利亚约自 4 月 10 日起，全俄中央执行委员会 4 月 28 日授权，6 月写入刑法典第 61 条第 3 款。", "95,208 这一逮捕数，以及 8,278 起恐怖、1,190 起群众抗议，是《苏维埃农村》第 2 卷所载 1930-01-15 的初步数（Doc 364 一类）。卷内写法是 95 208，中间有空格。", "1,307 起抗议和 9,093 起恐怖是《悲剧》第 1 卷导言所引、内务人民委员部 1931 年 3 月定稿表上的 1929 年全年数；同一行里 1928 年是抗议 709、恐怖 1,027。这两套文件不能互相替代，也不能把五倍罚款的日期写成 1929-03-20。"], "trap_assertions": ["1929年3月20日政治局批准的乌拉尔—西伯利亚方法已经包含五倍罚款", "95,208是1931年3月定稿的全年恐怖事件数", "1929年抗议1307起、恐怖9093起就是1930年1月15日那份初步统计"], "required_perspectives": ["post_soviet_archival", "chronology"], "created_at": "2026-11-23", "author": "dialectic-auditor:grok-4.7", "must_contain_any": [["3月20", "1929-03-20"], ["4月10", "4月28", "61"], ["95208", "95,208", "95 208"], ["1307", "1,307", "9093", "9,093"]], "forbid_patterns": ["1929年3月20日政治局批准的乌拉尔—西伯利亚方法已经包含五倍罚款", "95,208是1931年3月定稿的全年恐怖事件数"]}
```
