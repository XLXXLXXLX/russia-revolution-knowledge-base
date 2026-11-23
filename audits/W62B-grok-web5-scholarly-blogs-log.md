# W62B 入库日志：学者博客与专题站长文（Grok Web-5）

日期：2026-11-23。本日志只记录抓取、清洗与出处核验。未写导读，未写 `reading-notes/`，未写 `CLM-*`。未改 `framework/`、`.gitmodules`、`cards/`、`timeline/`、`README.md`、`sources/LITERATURE_CATALOG.md`。

全文只写入 `sources/web-archive/W62B_scholarly_blogs_and_debates/`。每篇为 YAML Frontmatter、标题与网页正文（含原注）。正文未缩写。20 篇正文合计 553,547 字符，均超过 1,500 字符。

## 通道

- `johnriddell.com` 返回 Account Suspended（`cgi-sys/suspendedpage.cgi`）。未保存该页，未绕过。`johnriddell.wordpress.com` 返回 403。开放全文改从 `links.org.au` 抓取。`source_url` 是实际取文的 URL；原博客 URL 写在 `source_urls` 与 `edition_note`。
- `encyclopedia.1914-1918-online.net` 返回 Anubis 人机验证页，未破解。`web.archive.org` 的 CDX 查询返回 503 Temporarily Offline；更早一次快照请求为 429。本批没有百科词条，因此没有 A 级百科全文。未自拟 Holquist、Lohr、Badcock、Khalid 的词条 URL。
- `soviethistory.msu.edu` 开放，CC BY-SA 4.0。导读在 `.sh-main-col`。单篇不署日期。`written_date_ns: "2002"` 取 NEH 项目结束年（von Geldern 与 Siegelbaum，1999–2002），不是单篇写作日。抓取文本是密歇根州立大学 MATRIX 现行站（项目组记 2015 年改版）。已查的 1917、1921、1924、1929 导读未见 Amy Nelson 或 Aaron Retish 署名。
- `isreview.org/issues/57/feat-russianrev/` 开放，声明字符集为 iso-8859-1，弯引号按 Windows-1252 解码。页面用嵌套表格重复主栏。首次按 Drupal 正文选择器提取为空。改从主栏提取，并在第一次 “This is the end of the MAIN COLUMN content” 处截断，其后重复栏目未入库。一处 `&#150;` 式控制符改为 en dash（January–February）。
- 未点击 CAPTCHA 或 Turnstile，未过付费墙。不足 1,500 字符的页面、404 与目录页未入库。

## 已入库（20）

等级：19 篇 B，1 篇 S。Links 与 ISR 上的 Historical Materialism 转载仍标 B，因为入库的是开放网页，不是期刊 PDF。页内若写明期刊卷期，记在 `edition_note`。1918-02-14 之后的俄历日期不另填；喀琅施塔得 1921 年文献 `written_date_os` 留空。

| 文件 | 作者 / 公历 / 等级 | 正文字符 | 完整性（首约 80 字 / 末约 80 字） |
| :--- | :--- | ---: | :--- |
| `1921-03-08_kronstadt_what-are-we-fighting-for.md` | 喀琅施塔得起义者；1921-03-08；S | 5,982 | 起：What Are We Fighting For? March 8, 1921，底本 *Pravda o Kronshtadte*。止：Voline, *The Unknown Revolution* (London: Freedom Press, 1955), pp. 241–243。与库内 1921-03-01 彼得罗巴甫洛夫斯克号决议不是同一篇。原页 “for the, purchase” 保留。 |
| `2002_siegelbaum_october-revolution.md` | Lewis Siegelbaum（刘易斯·西格尔鲍姆）；2002；B | 3,107 | 起：Subject essay，布尔什维克在彼得格勒夺权。止：托洛茨基对退出苏维埃代表大会者所说 “the rubbish heap of history.” 已去掉 Texts / Images 标签行。 |
| `2002_von-geldern_kronstadt-uprising.md` | James von Geldern（詹姆斯·冯·盖尔登）；2002；B | 5,161 | 起：喀琅施塔得海军基地位于 Kotlin。止：起义对无政府主义传统的关系。已去掉标签行。 |
| `2002_siegelbaum_new-economic-policy.md` | Siegelbaum；2002；B | 2,612 | 起：列宁在十大提出新经济政策。止：1929 年放弃新经济政策。已去掉标签行。 |
| `2002_siegelbaum_industrialization-debate.md` | Siegelbaum；2002；B | 4,090 | 起：1920 年代中期工业化争论。止：原 HTML 在 “abandonment of NEP” 处结束，`anti-kulak measures` 链接后缺少右括号，不是抓取截断。已去掉标签行。 |
| `2002_siegelbaum_liquidation-of-the-kulaks.md` | Siegelbaum；2002；B | 6,298 | 页题 Liquidation of the Kulaks as a Class，路径 `/1929/collectivization/`。止：死亡估计至少五百万人，农民离村进城。已去掉标签行与文末 CC 许可证句；许可证留在 `edition_note`。 |
| `2008-01_murphy_can-we-write-the-history-of-the-russian-revolution.md` | Kevin Murphy（凯文·墨菲）；2008-01；B | 45,378 | 起：*ISR* Issue 57, January–February 2008，Deutscher Lecture。止：参考文献 Lynne Viola, *Peasant Rebels Under Stalin* (1996)。注 1–55 在。注 1 写明 2006 年 11 月伦敦演讲，并注明首发 *Historical Materialism* 15, no. 2 (2007)。与库内 2004 年 H-Net 书评不是同一篇。 |
| `2010-06_lih_we-must-dream-echoes-of-what-is-to-be-done.md` | Lars T. Lih（拉尔斯·利赫）；2010-06；B | 33,612 | 起：2010 年 6 月芝加哥 Socialism 2010 讲稿，经 Lih 同意由 Links 刊出。止：作者书目句，Reaktion Books 的 *Lenin* 将于当年稍后出版。已从作者框删去 “special offer / read more” 推广句，保留会议与授权说明。`[*bogatyrskii*]` 与 strength 之间的空格已按原页补回。 |
| `2011-08-14_riddell_comintern-workers-governments.md` | John Riddell（约翰·里德尔）；2011-08-14；B | 15,754 | 起：Gustavs Klucis 的 “Workers of the World, Unite!”。止：书目 *Toward the United Front* (Leiden: Brill, 2011)。 |
| `2011-12-04_riddell_comintern-1922-periphery-pushes-back.md` | Riddell；2011-12-04；B | 15,798 | 起：Paul Levi。止：注 15，*Briefe Deutscher an Lenin*。2015-01-05 修订篇 “How front-line parties took the lead” 未并收。 |
| `2013-10-02_lih_marxism-and-melodrama-interview.md` | Lih，采访者 Dario Cankovic；2013-10-02；B | 41,424 | 正文署 October 2, 2013，*The North Star*，访谈在当年 6 月。文件名曾误作 2014-01-02，已按正文署期改正。止：关于合并公式与 “tire going flat” 的回答。原页笔误 “thel eft” 保留。`One way`、`Renewal by`、`Rediscovered focused`、`Rediscovered, one` 的空格是原页在空 `<strong>`/`<em>` 或链接内的空格，已补回。 |
| `2014-05-20_blanc_national-liberation-bolshevism-borderlands.md` | Eric Blanc（埃里克·布兰克）；2014-05-20；B | 58,937 | 起：敖德萨的崩得成员与 pogrom 受害者。止：注 85 所引 Trotsky, *The Challenge of the Left Opposition (1923–25)*。已补 `the National`、`ed. (Rīga`、`, in Jānis`、`see Karl Marx` 的空格。 |
| `2015-04-22_lih_bolshevism-was-fully-armed.md` | Lih；2015-04-22；B | 37,612 | 起：*Pravda* 编辑加米涅夫。止：文末 “– JR”。含加米涅夫 1917 年 3 月社论的英译与俄文。已删独立的 Click HERE 行。 |
| `2015-05-05_riddell_lenin-comintern-compromise-1921.md` | Riddell；2015-05-05；B | 16,844 | 起：By John Riddell，1921 年三大与 “To the masses”。止：注 10，ECCI 与美国党、Pogány。已删 “click HERE” 推广段。 |
| `2015-06-01_lih_ironic-triumph-of-old-bolshevism.md` | Lih；2015-06-01；B | 30,555 | 起：2015-06-01，经同意转载。止：注 7，Mandel 1984。文内说明更完整的期刊文本是 *Russian History* 38 (2011)。已删两处 Click HERE 行。未再收 *Weekly Worker* 843 的同题演讲稿。 |
| `2017-02-25_lih_workers-and-intellectuals-witbd.md` | Lih；2017-02-25；B | 46,230 | 起：In place of an introduction。止：Marot 附录末句，要求如实转述其解释并接受质疑。文内写明 2011 年写成。 |
| `2017-03-01_blanc_before-lenin-february-1917.md` | Blanc；2017-03-01；B | 49,133 | 起：1917 年 2 月 23 日彼得格勒抗议。止：注 50，Sukhanov 1955 [1922], p. 43。Links 转载 Historical Materialism 网站文本。 |
| `2017-03-23_lih_all-power-to-the-soviets-biography-of-a-slogan.md` | Lih；2017-03-23；B | 38,475 | 系列第 1 篇。Links 记转载日 2017-03-24，`written_date_ns` 用 John Riddell 站原日期 2017-03-23。止：注 6，Dune 回忆录。未再收 2014 年同题较早文本。 |
| `2017-03-31_blanc_revolutionary-line-of-march-old-bolshevism.md` | Blanc；2017-03-31；B | 75,913 | 起：加米涅夫读 *Pravda*。止：注 77，Бурджалов 1971, p. 286。与 2017-03-01 那篇不是同一文。 |
| `2017-06-04_blanc_finlands-forgotten-revolution.md` | Blanc；2017-06-04；B | 20,632 | 起：1905 年赫尔辛基总罢工人群。止：作者介绍 *Anti-Colonial Marxism*。Links 转载 Jacobin；John Riddell 站 2017-06-11 同文未另存。 |

## 清洗

从正文去掉的只有站点部件：`##### Texts | Images | …`、独立的 “Click HERE for more…” 行、富农导读文末的许可证句、Murphy 主栏结束标记及其后的重复栏目。会议说明、转载授权、原注、书目与出处句保留。

## 未入库

这些 URL 没有写成替代性论断，也没有用搜索摘要充数。

- **John Riddell 主站与 WordPress 子域**：停用页与 403。上表 Riddell / Lih / Blanc 各篇用 Links 开放全文。
- **1914-1918-online**：Anubis。Internet Archive 本轮不可用（CDX 503；早先快照 429）。`russiasgreatwar.org` 上查到的 Eric Lohr 条目是视频，不是全文。
- **付费墙或预览**：未收 Brill、Cambridge 只显示开头的预览页。Lih 期刊版 “Ironic Triumph”（*Russian History* 38, 2011）不在开放页上，入库的是 Links 上的开放文本，文内已指向该期刊篇。
- **同篇已有**：`sources/web-archive/W62B_reviews_and_zh_ru_web_essays/2004-10_murphy_rabinowitch-bolsheviks-come-to-power.md`；同目录 `2016-04-05_h-diplo_kotkin-stalin-vol1-roundtable.md`；`sources/web-archive/E02_E07_foundational_docs/1921-03-01_petropavlovsk-resolution.md`。2014 年 “All Power” 较早文本、*Weekly Worker* 843 的 ironic-triumph 演讲稿、Riddell 2015 年对 1922 年一文的修订篇、Blanc 西班牙文转载，均未重复抓取。
- **已满 20 篇后未再抓的开放长文**：Lih, “The proletariat and its ally”；Blanc, “Socialists should take the right lessons”（2021-08-09）；*Weekly Worker* 838, “Scotching the myths”（2010-10-20）；von Geldern 的 1917 culture-and-revolution 导读；Riddell 2020-07-02 统一战线采纳记。
- **非全文**：Suny 的康奈尔音频未当文本入库。

未跑第二轮付费墙重试。目录与愿望单未改。
