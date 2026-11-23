# W62B 入库日志：布尔什维克党内争论与反对派一手文献（Grok Web-2）

日期：2026-11-23。本日志只记录抓取、清洗、原文提取与出处核验。

未写 `reading-notes/`，未写 `historiography/claims/CLM-*`，未改 `sources/LITERATURE_CATALOG.md`、`README.md`、`framework/`、`.gitmodules`、`cards/`、`timeline/`。全文只写入 `sources/web-archive/W62B_mia_intra_party_oppositions/`。

抓取通道：`urllib` + BeautifulSoup。未遇到 CAPTCHA、Cloudflare Turnstile 或 403。未把 404 页、目录页或不足 1,500 字符的残页入库。20 篇正文合计 962,314 字符。每篇正文均无 HTML 标签、无未解析实体、无 “Works Index” / “Last updated” 页脚。等级一律 `epistemic_tier: S`、`source_tier: S`。1918-02-14 改历之后以及非俄国文献的 `written_date_os` 留空。

中文马克思主义文库的正文大量是 `<body>` / `<div>` 下由 `<br>` 隔开的文本节点。第一遍提取只保住了标题和少数 `<p>`，米亚斯尼科夫页被拒（1,328 字符），布哈林 1925 年中文只留下约 4,900 字符。修正提取器后重抓这两页。英文各篇按页内段落核对，正文与页面纯文本同量级。

## 已入库（20）

| 文件 | 日期（公历） | 语种 | 正文字符 | 起止 |
| :--- | :--- | :--- | ---: | :--- |
| `1917-10-24_kamenev-zinoviev_on-the-present-situation.md` | 1917-10-24（俄历 1917-10-11） | en | 10,901 | 起于页题 *On the Present Situation* 与 “(Extracts)”。止于署名 G. ZINOVIEV、U. KAMENEV。 |
| `1917-10-31_lenin_letter-to-bolshevik-party-members.md` | 1917-10-31（俄历 1917-10-18） | en | 7,389 | 起于 “Comrades,”。止于 “N. Lenin”。全集注保留。 |
| `1917-11-01_lenin_letter-to-the-central-committee.md` | 1917-11-01（俄历 1917-10-19） | en | 10,548 | 写给俄国社会民主工党（布）中央委员会的信。止于关于将来公布材料的句子。 |
| `1917-11-17_nogin-rykov-et-al_resignation-from-sovnarkom.md` | 1917-11-17（俄历 1917-11-04） | en | 2,123 | 人民委员退出政府声明。署名含 V. NOGIN、A. RYKOV、V. MILIUTIN、I. TEODOROVICH、A. SHLIAPNIKOV，以及 D. RIAZANOV、N. DERBYSHEV、I. ARBUZOV、YURENEV、G. FEDOROV、Yu. LARIN。注 [2] 为施略普尼科夫同意估价但不辞职。 |
| `1917-11-17_kamenev-zinoviev-et-al_resignation-from-cc.md` | 1917-11-17（俄历 1917-11-04） | en | 3,005 | 中央委员辞职书，与上一件不是同一文件。止于署名 Yu. KAMENEV、A. I. RYKOV、V. MILIUTIN、G. ZINOVIEV、V. NOGIN。 |
| `1917-11-17_lozovsky_letter-to-bolshevik-cec-group.md` | 1917-11-17（俄历 1917-11-04） | en | 5,229 | 起于 “Dear comrades:”。止于署名 A. Lozovsky 与注 1（Popov, *Oktiabrskii perevorot*, 1918, p. 289）。 |
| `1918-04-20_left-communists_theses-on-the-current-situation.md` | 1918-04-20 | en | 41,399 | 《共产主义者》第 1 期提纲。止于 “active and responsible proletarian opposition.” |
| `1918-04-20_osinsky_on-the-construction-of-socialism.md` | 1918-04-20 | en | 88,822 | 同一页含第 1、第 2 部分。页内译者注保留。止于关于既有分配网的句子。 |
| `1918_luxemburg_the-russian-revolution.md` | 1918 | en | 88,375 | ch01–ch08 八章。止于 “the future everywhere belongs to “Bolshevism.”” |
| `1921-01-25_shliapnikov_theses-of-the-workers-opposition.md` | 1921-01-25 | en | 17,316 | 《真理报》提纲。文末署 December 18 1920。 |
| `1921-07-27_myasnikov_press-freedom-documents_zh.md` | 1921-07-27 | zh | 10,968 | 页内依次为编者按、5 月 2 日给中央的报告、7 月 27 日《伤脑筋的问题》（页上自标“节选”）、8 月 6 日两封回信、8 月 22/23 日组织局决定、莫托维利哈大会决议。止于 “感谢 佐仓绫奈 收集、录入和校对”。 |
| `1921-08-05_lenin_letter-to-myasnikov.md` | 1921-08-05 | en | 11,204 | *Collected Works* vol. 32, pp. 504–509。注保留，注 [1] 写到 1922 年 2 月 20 日政治局批准开除。 |
| `1921_kollontai_the-workers-opposition.md` | 1921 | en | 115,672 | ch01–ch03。各章内部小节齐全。止于 “the Communist epoch.” |
| `1921_preobrazhensky_from-nep-to-socialism.md` | 1921 | en | 276,772 | 文库所刊 Introduction 与第 5–12 讲，含脚注。止于第 12 讲末句。 |
| `1922-02_shliapnikov-et-al_appeal-of-the-22.md` | 1922-02 | en | 3,304 | 二十二名党员署名，另有 A. Kollontai（1898）与 Zoya Shadurskaia 附署。英文页未印日，日期只记到月。 |
| `1924_trotsky_lessons-of-october.md` | 1924 | en | 155,475 | ch1–ch8 与作者后记 ch9。止于关于 M. S. Glazman 的句子。 |
| `1925_bukharin_critique-of-the-opposition-economic-platform_zh.md` | 1925 | zh | 29,457 | 1981 年《布哈林文选》中译。节次一至六齐全，注 [1]–[15] 在文末。止于 “感谢 黄胜利 录入并校对”。 |
| `1928-06-02_trotsky_letter-from-alma-ata.md` | 1928-06-02 | en | 20,066 | 阿拉木图信。页首 1941 年 *Fourth International* 编者框是该页原文，予以保留。 |
| `1928-07-23_trotsky_july-plenum-and-the-right-danger.md` | 1928-07-23 | en | 25,942 | 阿拉木图，1928 年 7 月 23 日。注保留。 |
| `1928-08-06_rakovsky_professional-dangers-of-power.md` | 1928-08-06 | en | 38,347 | 致瓦连季诺夫。止于落款 *Astrakhan, 6 August 1928*。 |

## 出处

1. 加米涅夫、季诺维也夫《On the Present Situation》：https://www.marxists.org/archive/zinoviev/works/1917/10/11.htm 。Bunyan and Fisher, pp. 59–62。页题标明 Extracts，不是未删节俄文原信。
2. 列宁《Letter to Bolshevik Party Members》：https://www.marxists.org/archive/lenin/works/1917/oct/18.htm 。*Collected Works*, vol. 26 (1972), pp. 216–219。
3. 列宁《Letter to the Central Committee》：https://www.marxists.org/archive/lenin/works/1917/oct/19.htm 。*Collected Works*, vol. 26, pp. 223–227。首次发表于 1927 年 11 月 1 日《真理报》第 250 号。
4. 诺根等退出人民委员会：https://www.marxists.org/history/ussr/publications/novaya-zhizn/1917/11/resignations.htm 。《新生活报》1917 年 11 月 5/18 日第 173 号第 3 版。Bunyan and Fisher, pp. 202–203。译者 Emanuel Aronsberg。
5. 加米涅夫等退出中央委员会：https://www.marxists.org/archive/zinoviev/works/1917/11/04.htm 。《人民事业报》1917 年 11 月 6/19 日第 201 号。Bunyan and Fisher, pp. 203–204。
6. 洛佐夫斯基致中央执行委员会布尔什维克党团：https://www.marxists.org/archive/lozovsky/1917/letter.htm 。《新生活报》1917 年 11 月 4/17 日第 172 号第 1–2 版。Bunyan and Fisher, pp. 204–206。
7. 左派共产主义者《Theses on the Current Situation》：https://www.marxists.org/history/ussr/publications/kommunist/april01/theses.htm 。1918 年 4 月 4 日宣读，刊于《共产主义者》第 1 期（1918 年 4 月 20 日）。
8. 奥辛斯基《On the Construction of Socialism》：https://www.marxists.org/archive/osinsky/1918/construction-socialism.htm 。《共产主义者》第 1 期第 5–11 页与第 2 期。英译转自 Kool / Oberländer 德文文集的西班牙文译本。
9. 卢森堡《The Russian Revolution》：https://www.marxists.org/archive/luxemburg/1918/russian-revolution/ 的 ch01.htm–ch08.htm。Bertram Wolfe 译，Workers Age Publishers, New York, 1940。手稿 1918 年布累斯劳狱中，未完成；1922 年保罗·列维首次刊布。目录页未并入。
10. 柯伦泰《The Workers' Opposition》：https://www.marxists.org/archive/kollonta/1921/workers-opposition/ 的 ch01.htm–ch03.htm。未并入 intro.htm（Solidarity 1961/1968 编者导论）。
11. 施略普尼科夫《Theses of the Workers Opposition》：https://www.marxists.org/archive/shliapnikov/1921/workers-opposition.htm 。《真理报》1921 年 1 月 25 日。Barbara C. Allen 2004 年英译。
12. 《Appeal of the 22》：https://www.marxists.org/archive/shliapnikov/1922/appeal.htm 。Allen 据第十一次代表大会速记记录（莫斯科，1961，第 749–750 页）英译。法文文库记为 1922 年 2 月 26 日；本英文页没有印出日，文件名与 `written_date_ns` 只到 `1922-02`。
13. 米亚斯尼科夫出版自由文件（中文）：https://www.marxists.org/chinese/reference-books/mia-chinese-russia-publishing-freedom-1920s.htm 。字符集 gb2312。编者按属于该页原文。《伤脑筋的问题》页上自标“节选”，未补写成全文。
14. 列宁《A Letter to G. Myasnikov》：https://www.marxists.org/archive/lenin/works/1921/aug/05.htm 。*Collected Works*, vol. 32 (1965), pp. 504–509。Yuri Sdobnikov 译。
15. 普列奥布拉任斯基《From N.E.P. to Socialism》：https://www.marxists.org/archive/preobrazhensky/1921/fromnep/ 的 lecture05.html–lecture12.html。Brian Pearce 译，New Park Publications, 1973。文库说明只重刊第五讲及以后各讲。本轮对 lecture01.html–lecture04.html 做了 HEAD，四者均为 HTTP 404，未编造缺失各讲。
16. 布哈林《对反对派经济纲领的批判——1923年10月的教训》：https://www.marxists.org/chinese/bukharin/mia-chinese-bukhrin-1925.htm 。第一次发表于 1925 年。中译文来自 1981 版《布哈林文选》。英文布哈林目录没有这篇的独立 HTML。
17. 托洛茨基《The Lessons of October》：https://www.marxists.org/archive/trotsky/1924/lessons/ 的 ch1.htm–ch9.htm。John G. Wright 译，Pioneer Publishers, 1937。David Walters 1996 年转录，Chris Clayton 2006 年校对。
18. 托洛茨基《The July Plenum and the Right Danger》：https://www.marxists.org/archive/trotsky/1928/07/rightdanger.htm 。*The Militant*, vol. 1, no. 3 (15 September 1928), pp. 1–3。
19. 托洛茨基《A Letter from Exile in Alma-Ata》：https://www.marxists.org/archive/trotsky/1928/06/alma-ata.htm 。*The Fourth International*, July 1941, pp. 186–188。
20. 拉科夫斯基《The “Professional Dangers” of Power》：https://www.marxists.org/archive/rakovsky/1928/08/prodanger.htm 。《反对派公报》第 6 期（1929）第 14–20 页。Gus Fagan 编 *Selected Writings on Opposition in the USSR 1923–30*（Allison & Busby, 1980）。落款阿斯特拉罕，1928 年 8 月 6 日。

## 清洗

- 诺根声明注 [2] 句末原被同一表格里的页脚链接粘上（Novaya Zhizn、October Revolution Archive、Marxists’ Internet Archive）。注文本来自 `<p class="footer">`，已删。刊名与页码仍在篇首出版信息里。
- 两篇加米涅夫/季诺维也夫页面文末的 Zinoviev Archive、Kamenev Archive、October Revolution Subject Archive、Marxist Writers Archive 链接块已删。
- 《十月的教训》各章末的 “The Lessons of October Index” 导航共 9 处已删。正文里对 *Archives of the Revolution 1917* 的引文保留。
- 洛佐夫斯基页的 HTML 用回车做行内折行，折行处没有空格，第一遍把 “party” 与 “discipline” 等词粘在一起，并把页脚档案链接粘在注末。已按段落重切，折行处补回空格，页脚未入库。文库原页的拼写（如 “I intrust”）照录。
- 列宁 1917 年 10 月 18 日信里的文库拼写 “will not loin” 照录，未改。
- 中文页的录入者致谢（佐仓绫奈、黄胜利）留在正文末，与页内原文一致。

## 未入库

- **同语种已在库内、本轮不重复**：1928-09-30 布哈林《一个经济学家的札记》的中文加俄文节录已在 `sources/web-archive/E06_E09_state_and_comintern/1928-09-30_bukharin-notes-of-an-economist.md`。该页说明马克思主义文库没有完整英译。本轮没有另造英文本。1927 年联合反对派政纲、1923 年四十六人声明、列宁《论“左派”幼稚性和小资产阶级性》、托洛茨基《新方针》公开信、布哈林《到社会主义之路》俄文，以及布哈林 1928 年七月与 1929 年四月发言的中文，均已在其他 `web-archive` 目录。
- **《新经济学》扫描 PDF**：马克思主义文库上的 1926 年英译是坏文本层，未入库。清单允许的替代是《从新经济政策到社会主义》的 HTML 各讲，已入库。
- **民主集中派纲领**：没有找到可入库的完整纲领 URL。奥辛斯基 1918 年《论社会主义建设》是左派共产主义者文献，不是 1920–1921 年民主集中派纲领。未建残篇。
- **编者后出文字**：柯伦泰小册子的 Solidarity 导论（intro.htm），以及普列奥布拉任斯基 1973 年版的出版者导言与传记注，未并入。
- **加米涅夫/季诺维也夫 10 月声明**：页面自己标明 Extracts。未把摘录写成全信。
- **米亚斯尼科夫《伤脑筋的问题》**：页面自己标明节选。同页的报告、回信、组织局决定和莫托维利哈决议按该页全文录入。
- **普列奥布拉任斯基第 1–4 讲**：HEAD 返回 404。
- **拉科夫斯基中译**（https://www.marxists.org/chinese/reference-books/mia-chinese-rakovsky-192808.htm）：英文全文已入库，未再抓语种互补，以免超出 20 篇上限。
- **列宁 1921 年 8 月 1 日附函**（aug/01b.htm）：不是清单点名的 8 月 5 日信，未抓。
