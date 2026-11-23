# W62B 入库日志：中文马克思主义文库（Grok Web-3）

日期：2026-11-23。只做检索、抓取、编码清洗和出处核验。未写 `reading-notes/`，未写 `CLM-*`，未改 `framework/`、`.gitmodules`、`cards/`、`timeline/`、`README.md`、`sources/LITERATURE_CATALOG.md`。

全文目录：`sources/web-archive/W62B_mia_chinese_corpus/`。每篇除 YAML 和标题外是网页正文（含原注）。抓取前扫过 `sources/web-archive/` 已有篇目。同篇同语种已有全文的不重复抓；库内只有英或俄文本、文库又有中文全文的，作为语种互补入库。

本批入库 **21** 篇。正文汉字合计 **561663**（不含 YAML）。`epistemic_tier` 与 `source_tier` 均为 S，`language` 均为 zh。1918-02-14 改历之后 `written_date_os` 留空。卢森堡在德国写作，不另造俄历。页上只有年份的，公历写到年。

| 文件 | 汉字 | 俄历 | 公历 | 标题 |
| --- | ---: | --- | --- | --- |
| `1904-07_luxemburg_organizational-questions-of-russian-social-democracy_zh.md` | 13281 |  | 1904-07 | 俄国社会民主党的组织问题 |
| `1905-11-13_lenin_party-organisation-and-party-literature_zh.md` | 3374 | 1905-11-13 | 1905-11-26 | 党的组织和党的出版物 |
| `1906_trotsky_results-and-prospects_zh.md` | 48522 | 1906 | 1906 | 总结与前瞻 |
| `1917-03-07_lenin_letters-from-afar-1_zh.md` | 9914 | 1917-03-07 | 1917-03-20 | 远方来信·第一封 |
| `1917-03-11_lenin_letters-from-afar-3_zh.md` | 7742 | 1917-03-11 | 1917-03-24 | 远方来信·第三封 |
| `1917-04-08_lenin_dual-power_zh.md` | 1839 | 1917-04-08 | 1917-04-21 | 论两个政权 |
| `1917-09-13_lenin_marxism-and-insurrection_zh.md` | 3512 | 1917-09-13 | 1917-09-26 | 马克思主义和起义 |
| `1917-09-29_lenin_crisis-has-matured_zh.md` | 5350 | 1917-09-29 | 1917-10-12 | 危机成熟了 |
| `1917-10-01_lenin_can-bolsheviks-retain-state-power_zh.md` | 28362 | 1917-10-01 | 1917-10-14 | 布尔什维克能保持国家政权吗？ |
| `1918-04_lenin_immediate-tasks-of-soviet-power_zh.md` | 24174 |  | 1918-04 | 苏维埃政权的当前任务 |
| `1918_luxemburg_the-russian-revolution_zh.md` | 22188 |  | 1918 | 论俄国革命 |
| `1920_trotsky_terrorism-and-communism-ch8_zh.md` | 32082 |  | 1920 | 恐怖主义与共产主义·第八章 |
| `1921-03-15_lenin_tax-in-kind-report-tenth-congress_zh.md` | 15382 |  | 1921-03-15 | 关于以实物税代替余粮收集制的报告 |
| `1921-04-21_lenin_tax-in-kind_zh.md` | 24941 |  | 1921-04-21 | 论粮食税 |
| `1921-10-14_lenin_fourth-anniversary-of-october_zh.md` | 5221 |  | 1921-10-14 | 十月革命四周年 |
| `1921_kollontai_workers-opposition_zh.md` | 27617 |  | 1921 | 工人反对派 |
| `1922-03-27_lenin_eleventh-congress-political-report_zh.md` | 44424 |  | 1922-03-27 | 十一大中央委员会政治报告 |
| `1923-12_trotsky_new-course_zh.md` | 64009 |  | 1923-12 | 新路向 |
| `1924-04_stalin_foundations-of-leninism_zh.md` | 56909 |  | 1924-04 | 论列宁主义基础 |
| `1924-09-15_trotsky_lessons-of-october_zh.md` | 66712 |  | 1924-09-15 | 十月的教训 |
| `1927_trotsky_platform-of-the-joint-opposition_zh.md` | 56108 |  | 1927 | 俄国局势的真相和共产党的任务 |

汉字按去掉 YAML 之后的正文计，含原注。最短的《论两个政权》1839 字，是《真理报》短论全文，篇末有「译自《列宁全集》俄文第5版第31卷第145—148页」，不是残缺摘要。

## 底本与 URL

列宁各篇是中文马克思主义文库《列宁全集》中文第2版文字页，卷次与俄文第5版不同：第12卷（1905）、第29卷（1917年3—4月）、第32卷（1917年7—10月）、第34卷（1918年3—7月）、第41卷（1921年3—6月）、第42卷（1921年6月—1922年3月）、第43卷（1922年3月—1923年1月）。

- 《党的组织和党的出版物》：https://www.marxists.org/chinese/lenin-cworks/12/019.htm
- 《远方来信》第一封、第三封：同一页 https://www.marxists.org/chinese/lenin-cworks/29/003.htm ，按锚点 `#1`–`#2`、`#3`–`#4` 抽出。第2、4、5封未收录。第一封补回注释 [6]–[13]，第三封补回 [32]–[35]。
- 《论两个政权》：https://www.marxists.org/chinese/lenin-cworks/29/023.htm 。篇首俄历 1917-04-08，页末刊于《真理报》1917年4月9日。
- 《马克思主义和起义》：https://www.marxists.org/chinese/lenin-cworks/32/030.htm 。篇首日期跨 9月13—14日 / 9月26—27日，YAML 取起始日。
- 《危机成熟了》：https://www.marxists.org/chinese/lenin-cworks/32/035.htm
- 《布尔什维克能保持国家政权吗？》：https://www.marxists.org/chinese/lenin-cworks/32/037.htm 。YAML 取完成日 10月1日 / 10月14日。
- 《苏维埃政权的当前任务》：https://www.marxists.org/chinese/lenin-cworks/34/011.htm
- 十大实物税报告：https://www.marxists.org/chinese/lenin-cworks/41/001.htm 只收第5、6节（3月15日报告和当日总结发言）及这两节引用的注释 [34][35][36]。同页其余议程，包括已另档入库的党的统一决议，未重复。
- 《论粮食税》：https://www.marxists.org/chinese/lenin-cworks/41/018.htm 。篇内对 1918 年《论“左派”幼稚性和小资产阶级性》的原文摘录保留。
- 《十月革命四周年》：https://www.marxists.org/chinese/lenin-cworks/42/045.htm 。注释 [106][107] 在文末。
- 十一大政治报告：https://www.marxists.org/chinese/lenin-cworks/43/019.htm 只收第2、3节（3月27日报告、3月28日总结发言）及这两节引用的注释。开幕词、闭幕词和其他议程未收。

托洛茨基：

- 《总结与前瞻》全本（1919年序、九章、附录《为政权而斗争》）：目录 https://www.marxists.org/chinese/trotsky/1906book/trotsky-1906bookindex.htm ，`source_urls` 另列 01–11。蔡汉敖译，陈泰编校。正文年 1906，序言 1919。
- 《恐怖主义与共产主义》第八章《劳动组织的问题》：https://www.marxists.org/chinese/trotsky/1920/08.htm 。Uni 佐仓绫奈译校，据彼得格勒国家出版社 1920 年版。其余各章未收。
- 《新路向》全本（译者前记、序言、七章、附录一至四）：目录 https://www.marxists.org/chinese/trotsky/1923book/trotsky-1923bookindex.htm ，`source_urls` 另列 01–13。附录一是 1923年12月8日公开信。
- 《十月的教训》九节加目录所附 1924年11月《我们的意见分歧》：目录 https://www.marxists.org/chinese/trotsky/192409/index.htm 。篇首日期 1924-09-15。
- 《俄国局势的真相和共产党的任务》（反对派政纲）：https://www.marxists.org/chinese/trotsky/marxist.org-chinese-trotsky-1927b.htm

卢森堡、柯伦泰、斯大林：

- 卢森堡 1904：https://www.marxists.org/chinese/rosa-luxemburg/marxist.org-chinese-rosa-1904.htm 。原载《新时代》1904年7月。
- 卢森堡 1918《论俄国革命》：https://www.marxists.org/chinese/rosa-luxemburg/marxist.org-chinese-rosa-1918.htm 。页内说明据 1974 年德意志民主共和国文集。
- 柯伦泰《工人反对派》：https://www.marxists.org/chinese/kollontai/marxist.org-chinese-kollontai-1921.htm 。1921年莫斯科版，译者李星。同站另有商务印书馆 1981 年版链接，本档未收那一版。
- 斯大林《论列宁主义基础》：https://www.marxists.org/chinese/stalin/mia-chinese-stalin-192404.htm 。页末写连载于 1924年4月26、30日和5月9、11、14、15、18日《真理报》。整理者注保留；页脚「感谢 闲汉 收集、整理」已删。

## 入库前改过的网页残片

这些改动只去掉导航或还原被网页嵌进词中的标题残片，不改句子。

- 十一大总结发言的源 HTML 把「的总结发言」嵌进七个词：无产阶级、允许、党的机关和苏维埃、领导人、影响、意见书、减少了。已按词界还原。节标题「关于俄共（布）中央政治报告的总结发言」和注释 [90]「组织工作报告的总结发言里」是原文，未改。同批其他全集页用标题末几字做词中检索，没有第二处这种嵌字。「退却已经结束」和莫斯科 4700 名负责共产党员、征服民族与被征服民族文化的段落都在第2节。
- 《远方来信》和十大实物税报告初稿漏了文末注释。来信各封的注在全页末尾，切片时把正文里的 `[n]` 当成了已经附上的注。十大页的「注释：」前面有两个全角空格，按行首「注释：」切分时切空。已只补这两封和第5、6节实际引用的注，没有把全页其余注释倒进来。注 [34]「1921年，3月15日」的逗号是源页原文。
- 《总结与前瞻》删了 22 处章末「<< 托洛茨基：总结与前瞻 >>」。1915年托洛茨基自注仍在附录末。
- 《十月的教训》删了章间「上一篇 / 回目录 / 下一篇」和重复面包屑。《恐怖主义与共产主义》第八章删了文末同一行导航。各篇页首「-> 作者 -> 卷次」面包屑已删。

## 已有同篇或同范围全文，未再抓

- 《社会民主党在民主革命中的两种策略》序言、第6、10、13章中文全集正文已在 `sources/web-archive/W32_milestone_docs/1905-07_lenin-two-tactics-of-social-democracy.md`。本批改收同月尚未入库的《党的组织和党的出版物》。
- 《论“左派”幼稚性和小资产阶级性》中文五节全文已在 `sources/web-archive/W32_milestone_docs/1918-05_lenin-left-wing-childishness-state-capitalism.md`。《论粮食税》里的大段摘录是该小册子原文的一部分，保留。
- W39 五篇不重复：`1922-03-19_lenin-secret-letter-to-molotov-shuia-church-valuables.md`、`1922-12-30_lenin-question-of-nationalities-or-autonomisation.md`、`1923-01-16_lenin-our-revolution-sukhanov-notes.md`、`1923-01-23_lenin-how-we-should-reorganise-rabkrin.md`、`1923-03-02_lenin-better-fewer-but-better.md`。
- 《新路向》：`sources/web-archive/W32_milestone_docs/` 里已有 1923年12月8日公开信、跋、序言和第一章的中英俄对照摘录。本档是同一中译系统的全书。
- 反对派政纲：`sources/web-archive/` 的 E09 已有英文核心摘录。本档是中文全文。
- 布哈林 1925年4月17日莫斯科积极分子会议报告的中文摘要，以及《到社会主义之路》俄文小册子，已在 `sources/web-archive/E09_E10_party_debates/1925-04_bukharin-road-to-socialism.md`。中文布哈林目录没有这两篇的 HTML。
- 《一个经济学家的札记》中俄全文已在 `sources/web-archive/E06_E09_state_and_comintern/1928-09-30_bukharin-notes-of-an-economist.md`（中文来自南京大学「实践与文本」，底本是 1967 年纽约俄文选集，不是《布哈林文选》）。中文文库目录没有这篇 HTML。
- 布哈林 1928年7月10日七月全会发言、1929年4月18日四月全会发言的中文全文已在 `sources/web-archive/W32_milestone_docs/1928-07-10_bukharin-july-plenum-speech-grain-and-smychka.md` 和 `1929-04-18_bukharin-april-plenum-speech-defense-of-nep.md`。
- 十大《关于党的统一的决议》中文草案已在 `sources/web-archive/E06_E10_turning_points/1921-03-16_on-party-unity.md`，与本批抽出的实物税报告不是同一件。

## 清单上没有收成中文全文的项目

中文布哈林目录没有《走向社会主义的道路》、《发财吧》、《一个经济学家的札记》、《列宁的政治遗嘱》（1929年1月纪念列宁逝世五周年演说）。猜的单篇 URL 返回 404，未再请求。文库 PDF `buhalin/3.pdf`、`4.pdf`、`5.pdf`（文选上册、中册、专辑）抽文本为空，是扫描图，未做 OCR，不入库。1929年1月这篇演说不是列宁《给代表大会的信》；后者已在 `sources/web-archive/E06_E10_turning_points/1922-12_letter-to-the-congress.md`。

中文斯大林目录里，1924–1929 指定篇中只有《论列宁主义基础》是独立 HTML。下列各篇没有单篇 HTML，未下载目录上的全集 PDF，也未改抓其他站点：

- 1928-05-28《在粮食战线上》：英俄全文在 `sources/web-archive/E09_E10_party_debates/1928-05-28_stalin-on-the-grain-front.md`。
- 1928-07-09《论工业化和粮食问题》：中文文库无单篇。布哈林次日发言里引用了这篇，发言本身已在 W32，不是斯大林演说全文。
- 1928-10-19《论联共（布）党内的右倾危险》：中文文库无单篇，本库也没有这篇的独立全文。
- 1929-04《论联共（布）党内的右倾》：英文全集全文在 `sources/web-archive/E02_E10_core_classics/1929-04-22_right-deviation-in-cpsu.md`。
- 1929-11-07《大转变的一年》：英文全集全文在 `sources/web-archive/E06_E10_turning_points/1929-11-07_year-of-great-turn.md`。该档已记明中文目录无独立 HTML。
- 1929-12-27《论苏联土地政策的几个问题》：俄文全文在 `sources/web-archive/E01_E10_supplements/1929-12-27_stalin-agrarian-marxists-speech-dekulakization.md`。中文文库无单篇 HTML。

普列汉诺夫目录和共产国际目录能打开。本批写明要收的是卢森堡两篇和柯伦泰《工人反对派》，都已入库。没有另抓短文凑满 22 篇。

托洛茨基 1928年7月23日《七月全会和右倾危险》的英文全文已在 `sources/web-archive/W62B_mia_intra_party_oppositions/1928-07-23_trotsky_july-plenum-and-the-right-danger.md`。1927年反对派政纲是清单上的另一选择，本批收了它的中文全文。

## 编码与完整性

- 中文文库页面的 charset 是 gb2312，按 gb18030 解码后存 UTF-8。21 篇都没有 U+FFFD，也没有「锟」。
- 抓取用 Python `urllib`。没有遇到验证码、Cloudflare 人机验证或 403。404 的目录页和猜的布哈林单篇没有入库。
- 每篇汉字多于 1500。抽段的来信、十大第5–6节、十一大第2–3节都停在该节署名或总结发言的「（鼓掌）」之后，再接该节引用的注释，没有把同页下一篇议程接进来。
- 多章书按目录顺序拼接。`source_url` 用目录页，`source_urls` 列入各章。
- 没有把导航、下载链接和收集者致谢写入正文。全集编者注和译者注保留。
