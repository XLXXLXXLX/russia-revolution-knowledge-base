---
id: WB-W13
type: web-brief
title: "W13 核心一手文献入库清单：怎么办第二章、和平与土地法令、论合作社、论右倾"
retrieved_at: "2026-11-18"
epistemic_tier: S
scope: "E02–E10"
---

# WB-W13 核心一手文献入库清单

检索日 2026-11-18。四份都写入 `sources/web-archive/E02_E10_core_classics/`。每份 YAML 含 `source_url`、`written_date_os`、`written_date_ns`、`edition_note`、`epistemic_tier: S`。1918年2月改用公历之后的两篇，`written_date_os` 记 `null`。《怎么办？》在国外写成、在国外初版，英文目录不印俄历，`written_date_os` 也记 `null`。未改其他目录。

| # | 篇 | 俄历 / 公历 | 入库文件 | 语种 | 缺口 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 列宁《怎么办？》第二章 | 写作 1901年秋至1902年2月（公历）；成书初版 1902年3月 | `1902_witbd-ch2-spontaneity-and-consciousness.md` | 中、英、俄第二章全文，另附三处关键句对照 | 只收第二章；不发明第二章单独页码 |
| 2 | 全俄苏维埃二大《和平法令》《土地法令》 | 通过 1917-10-26 / 1917-11-08 | `1917-10-26_decrees-on-peace-and-land.md` | 中文法令、英文法令、1957年法令汇编俄文 | marxists.org 俄文库无这两条法令的独立全文；口头报告不收入 |
| 3 | 列宁《论合作社》 | 口授 1923-01-04 与 1923-01-06 | `1923-01-04_on-cooperation.md` | 中文全文、英文全文、维基文库俄文 | 俄文马克思主义文库无独立页；维基文库正文无 1月4日、1月6日署日期行 |
| 4 | 斯大林《论联共（布）党内的右倾》 | 演说 1929-04-22 | `1929-04-22_right-deviation-in-cpsu.md` | 英文全集全文、俄文全文 | 中文马克思主义文库无独立 HTML；英文注〔12〕在网页上被截断 |

## 1. 《怎么办？》第二章

- **篇名**：中文「二 群众的自发性和社会民主党的自觉性」。英文 The Spontaneity of the Masses and the Consciousness of the Social-Democrats。俄文 II. Стихийность масс и сознательность социал-демократии。全书俄文篇名《Что делать? Наболевшие вопросы нашего движения》。
- **日期**：英文目录原文 Written between the autumn of 1901 and February 1902；First published as a separate work in March 1902。`written_date_ns` 记 `1901-autumn/1902-02`。这本书在国外写成、在国外初版，目录没有俄历对照。
- **范围**：只收第二章。序言、第一章和第三章不在本文件。俄文第三章在 `6-13-2.htm`。
- **英文**：<https://www.marxists.org/archive/lenin/works/1901/witbd/ii.htm>。底本 Lenin’s Collected Works, Foreign Languages Publishing House, Moscow, 1961, Volume 5, pp. 347–530。这是全书页码。译者 Joe Fineberg 与 George Hanna，Victor Jerome 编。
- **俄文**：<https://www.marxists.org/russkij/lenin/1902/6-13-1.htm>，自锚点 `II.` 起。页眉：осень 1901 – февраль 1902 года；ПСС 第5版第6卷第1–192页，同样是全书页码。该 HTML 没有逐页 `[c.]`。本档不另造第二章页码。
- **中文**：<https://www.marxists.org/chinese/lenin-cworks/06/005.htm>，《列宁全集》中文第2版第6卷路径。这一页没有单独的「译自俄文第5版第×页」题记。篇末注一并入库。注〔57〕里的「斯图加特」是《新时代》（*Die Neue Zeit*，1883–1923）的出版地。英文目录没有为1902年3月的初版另写城市。
- **三处对照**放在全文之前：（1）工人本来不可能有社会民主主义意识，这种意识只能从外面灌输进去 / from without / извне；（2）所引考茨基：社会主义意识是从外面灌输进无产阶级阶级斗争的；（3）社会民主党的任务是反对自发性。
- **照录的破字**：俄文网页把通行的「у рабочих и не могло быть」印成「у рабочих м не могло быть」，已加 [sic]。「задача социал-демократий,」比通行的「социал-демократии」多一个 й，已加 [sic]。英文考茨基引文在 this consciousness 与 Judging 之间缺句号，已加 [sic]。俄文考茨基引文整段少句号，例如 «этому сознанию На основании»；«сознанию» 被空字体标签断成 «со знанию»。这两处已加 [sic]，未补句号，也未把词拼回。德文 von außen：中文页印成 von　auβen（希腊字母 β），俄文页印成 von auBen（大写 B）。中文注「列宁会集」写成「列宁会集〔sic〕」。页末通往下一章的「Продолжение」未收入。

## 2. 《和平法令》与《土地法令》

- **通过日**：俄历1917年10月26日 / 公历1917年11月8日。两道法令收在同一文件。收入的是法令条文。列宁的口头报告、总结发言和「关于成立工农政府的决定」不在正文里。
- **中文页注〔5〕**：第二次会议于10月26日（11月8日）晚9时开始；大会一致通过和平法令；土地法令以绝大多数票通过，1票反对，8票弃权；10月27日（11月9日）凌晨5时15分闭幕。1957年《苏维埃政权法令汇编》第1卷的土地法令标题行写「принят на заседании 26 октября в 2 час. ночи」。晚9时、次日凌晨5时15分、夜间2时，都按各页原文并列保留。
- **中文**：<https://www.marxists.org/chinese/lenin-cworks/33/003.htm>。和平法令自标题起，收到向英法德三国觉悟工人呼吁的那一段。下一段起句「应当立即开始和平谈判」是口头说明，已切除。土地法令收到「（5）普通农民和普通哥萨克的土地概不没收」。下一段「这里有人叫嚷」是口头说明，已切除。242份地方农民委托书的总纲在第4条之内。同页题记：和平法令载于1917年10月27日（11月9日）《真理报》第170号和《中央执行委员会消息报》第208号。土地问题报告连同土地法令的题记写载于1917年10月28日（11月10日）《真理报》第171号和《中央执行委员会消息报》第209号。页末写明和平问题报告译自俄文第5版第35卷第13–18页，土地问题报告译自第35卷第23–27页。这两行页码覆盖的是报告。题记写在口头说明之后，所以放在 `edition_note`，不放进法令正文。
- **英文**：和平法令 <https://www.marxists.org/archive/lenin/works/1917/oct/25-26/26b.htm>，自锚点 `decree-peace` 至 `hr class="section"`。土地法令 <https://www.marxists.org/archive/lenin/works/1917/oct/25-26/26d.htm>，自锚点 `decree-land` 至 Voices are being raised here 之前。第5条 ordinary peasants and ordinary Cossacks shall not be confiscated 留在法令内。两页属于 Collected Works Volume 26。破字留原词并加 [sic]：annexation of seizure（of 当为 or）、faciliate、competition of negotiations（当为 completion）、the present way（当为 war）、folowing。`the[aggressive]` 是该页原有的插入，方括号前没有空格。
- **俄文**：marxists.org/russkij 列宁目录（2026-11-18）没有这两条法令的独立全文。目录里与「法令」相关的另一页是「Выписки из ленинских декретов о РККА」。正文用莫斯科大学历史系电子文本，底本《Декреты Советской власти》第1卷，莫斯科，国家政治书籍出版社，1957年。和平法令 <http://www.hist.msu.ru/ER/Etext/DEKRET/o_mire.htm>。土地法令 <http://www.hist.msu.ru/ER/Etext/DEKRET/o_zemle.htm>。网页几乎没有空行，新段用行首缩进标出；行末有一至二位页码；另有栏眉「СТР.」。入库时按缩进分段，去掉页码和栏眉。标题、核对说明和「Председатель Совета Народных Комиссаров Владимир Ульянов-Ленин」保留。和平法令标题行写明 26 октября 1917 г. 一致通过。
- **用词差**，正文不改写成统一术语。法令第2条：英文 crown, monastery, and church lands；中文皇族、寺院和教会的土地；俄文 земли удельные, монастырские, церковные。委托书的土地清单：英文 state, crown, monastery, church, factory, entailed, private, public, peasant；中文国家、皇族、皇室、寺院、教会、工厂占有、长子继承、私有、公共、农民；俄文 государственная, удельная, кабинетская, монастырская, церковная, посессионная, майоратная, частновладельческая, общественная, крестьянская。英文的 crown 在清单里只占一个位置；中文在同一位置分成皇族与皇室，俄文分成 удельная 与 кабинетская。

## 3. 《论合作社》

- **日期**：1923年已用公历。`written_date_os` 为 null。`written_date_ns` 为 `1923-01-04/1923-01-06`。英文页 Written: January 4 & 6, 1923。正文另有 January 4, 1923 与 January 6, 1923 两行。中文篇题「（1923年1月4日和6日）」，分「一」「二」两节。首次发表：《真理报》第115–116号，1923年5月26–27日，署名 Н. Ленин。
- **英文**：<https://www.marxists.org/archive/lenin/works/1923/jan/06.htm>。Lenin’s Collected Works, 2nd English Edition, Progress Publishers, Moscow, 1965, Volume 33, pp. 467–475。转录 Brian Baggins。页内声明 Public Domain: Lenin Internet Archive (2000)，复制时须注明 Marxists Internet Archive。
- **中文**：<https://www.marxists.org/chinese/lenin-cworks/43/100.htm>，《列宁全集》中文第2版第43卷。页末：译自《列宁全集》俄文第5版第45卷第369–377页。注〔242〕、〔243〕一并入库。注〔242〕写明：娜·康·克鲁普斯卡娅于1923年5月把文章转交中央委员会；5月24日政治局决定尽快刊载，并在文后注明日期。标准篇名用《论合作社》。
- **俄文**：marxists.org/russkij 无这篇的独立全文。正文用维基文库 <https://ru.wikisource.org/wiki/О_кооперации_(Ленин)>，并在档案里标明这不是 MIA 页。页面分 I、II 两节，收到文化革命那一段。这一页正文没有「4 января 1923 года」和「6 января 1923 года」。口授日期用英、中两页。缺行只说明这一份维基文库转录未印日期。

## 4. 《论联共（布）党内的右倾》

- **日期**：联共（布）中央委员会与中央监察委员会联席全会，1929年4月16–23日。斯大林于4月22日作这篇演说。`written_date_os` 为 null。`written_date_ns` 为 `1929-04-22`。英文篇名 The Right Deviation in the C.P.S.U.(B.)，副题写明 Verbatim Report。俄文篇名《О правом уклоне в ВКП(б)》，副题写明全会速记（Стенограмма）。
- **英文**：<https://www.marxists.org/reference/archive/stalin/works/1929/04/22.htm>。J. V. Stalin, *Works*, Vol. 12, April 1929–June 1930, pp. 1–113, Foreign Languages Publishing House, Moscow, 1954。转录 Brian Reid。页内声明 Public Domain: Marxists Internet Archive (2008)，复制时须注明 Marxists Internet Archive。注〔*〕写明：现在这个文本有三十多页是当时报刊没有发表的。结构为 I One Line or Two Lines?、II Class Changes and Our Disagreements、III Disagreements in Regard to the Comintern、IV Disagreements in Regard to Internal Policy、V Questions of Party Leadership、VI Conclusions，以及注释。页上的脚注号是上标，档案写成 [1]、[2]，以免和年份连成 19291。注〔1〕在 Resolutions 前有破字 eee，正文作 eee [sic]。注〔12〕在网页上停在 Conferences 一词，后面就是页脚。档案停在同一处，没有补后半句。
- **俄文**：<https://www.marxists.org/russkij/stalin/t12/t12_01.htm>。页眉指向镜像 http://grachev62.narod.ru/stalin/index.htm 。段落在 HTML 里按短语换行，入库时按 `<p>` 合成段。页码标记 `[c.N]` 保留。镜像说明和站点导航行未收入。
- **中文**：<https://www.marxists.org/chinese/stalin/index.htm> （2026-11-18）没有这篇的独立 HTML。目录另列诸夏怀斯社版新编《斯大林全集》PDF。本轮不从该 PDF 拆中译。`source_url_zh` 为 null。主 `source_url` 用英文页。
- **关于加米涅夫的几段，都是这篇演说里的话**。第一节：布哈林跑到昨天的托洛茨基分子、以加米涅夫为首的人那里，要组织反对中央和中央政治局的派别集团；演说称布哈林在那里说到中央路线的 “fatal” / “гибельности”，说到布哈林、托姆斯基、李可夫与中央有原则分歧，并且要根本改变政治局的组成。同节引用1929年2月委员会交换意见的记录：布哈林承认与加米涅夫的谈判是政治错误。第五节把这次接触称为 behind the scenes / закулисные переговоры，内容包括组织派别集团、改变中央政策、改变政治局组成、利用粮食收购危机攻击中央。第六节结论要求谴责布哈林与加米涅夫集团的秘密谈判，称之为不忠诚和派别活动最露骨的表现。同一次演说里另有一段，讲的是十月革命次日加米涅夫、季诺维也夫拒绝任职、要求成立有孟什维克和社会革命党人参加的联合政府。那是1917年的辞职事例，和1928–1929年这次谈判不是同一件事。档案保存的是演说中的指控原文。

web-scout 撰写。只新增 `sources/web-archive/E02_E10_core_classics/` 下本清单四份档案与本简报。未改其他目录。
