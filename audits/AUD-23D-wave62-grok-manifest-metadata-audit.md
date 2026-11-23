---
id: AUD-23D-wave62-grok-manifest-metadata-audit
type: audit
auditor_model: grok-4.7
target_wave: W62
role: source-extractor + dialectic-auditor
status: remediated
updated_at: "2026-11-23"
scope: "启动时已存在的 sources/primary（25）、sources/monographs（178）、sources/articles（34），共 237 份 manifest.yaml。只改 title、author、year / publication_year / pub_year、language。未改 slug、source_file、toc、章节正文、LITERATURE_CATALOG、cards，也未改任务启动后新建的 articles 子目录与 smele_historical_dictionary_civil_wars。"
---

# AUD-23D｜馆藏扉页元数据核查（237 份既有目录）

只读每个文献目录前部切片的书名页、版权页或期刊眉头。正文没有通读。年份取这一册版权页；原书年份与重印年份同时出现时，写入这一册的出版年，并在下面注明另一年。书名页没有署名的，写成「未署作者」或「未署编者」，不补目录外的编者名。`source_file` 里的路径、哈希和 z-library / Anna's Archive 后缀原样保留。

启动快照：primary 25，monographs 178，articles 34，合计 237。当时没有 `smele_historical_dictionary_civil_wars`。快照之后 `sources/articles/` 又出现 29 个新目录，专著侧也出现了 `smele_historical_dictionary_civil_wars`。这些都不在允许名单里，没有打开、没有改。

## 修复统计

| 项 | 数 |
|---|---|
| 启动时目录 | 237（25 + 178 + 34） |
| 写入 `manifest.yaml` | 94（primary 8，monographs 79，articles 7） |
| 启动目录中未改 | 143 |
| 既有论文逐篇核对 | 34 |
| 论文实际改写 | 7 |
| 论文核对后保持原文 | 27 |
| 书名页无署名、作者写成「未署」 | 6 |
| 书名页缺失、作者保持空白 | 1（`soviet_grain_production_1913_1944`） |
| 语种新写或改正 | 8 |
| 目录名改名 | 0 |

写入后用启动清单重载全部 237 份 YAML：原有键都还在（`slug`、`source_file`、`epistemic_tier`、`chunk_count` / `chapter_count`、`needs_ocr`、`cited_by_monographs`、`note`、`sha`、`quality_check` 等）。工作区 diff 只有这 94 个 `manifest.yaml`（233 行插入，25 行删除）。

启动时绝大多数缺陷是 `title` / `author` 为空，或作者写成「未核定」「中文研究论文」「俄罗斯远东移民史研究译著」。脏文件名在 `source_file`，不在 `title`。本次把书名页上的标准书名写入 `title`，没有改 `source_file`。缺年份但作者和书名已经正确的记录没有批量补 `year`。已有 `publication_year` 或 `pub_year` 的，沿用该键，不另加 `year`。

## 任务点名的四条，以及相邻的张冠李戴

### `class_formation_comparative_2008`

书名页与版权页：Michael Burrage，*Class Formation, Civil Society and the State: A Comparative Analysis of Russia, France, the US and England*，© Michael Burrage 2008，Palgrave。原 `author` 为「未核定（详见书名页）」。现为 Michael Burrage。书名与 `pub_year: 2008` 原本已对，没有改。

### `bukharin_preobrazhensky_debate_zh`

首页署名刘伟、平新乔（北京大学经济学院讲师）。篇名「平衡与非平衡：布哈林与普列奥布拉仁斯基之争」。页眉「1989年第2期」，页码 92。DOI `10.16158/j.cnki.51-1312/f.1989.02.013`。这一页没有印出期刊名，所以 `title` 不补刊名。原 `author`「中文研究论文」、`year` 2000 是错的。现为刘伟、平新乔，`year: 1989`。篇名原文已是「仁」，未改字。

### `nep_early_grain_policy_peasant_resistance_zh`

首页即赵旭黎，《俄罗斯研究》2013年第4期总第182期，篇名「新经济政策前期苏联粮食政策的负面效应与农民反抗」。作者与篇名原本已对。未改，也没有另加年份键。

### `stalin_vs_bukharin_rykov_nep_debate_zh`

首页即陈爱茹，《俄罗斯东欧中亚研究》2013年第2期，篇名「废除还是坚持新经济政策——斯大林同以布哈林、李可夫为首的“右派”的争论」。作者与篇名原本已对。未改。

### 远东强制移民不是「译著」占位

`soviet_far_east_forced_migration_1920s_zh` 原作者「俄罗斯远东移民史研究译著」，书名是中文转写，`publication_year: 2015`，`language: zh`。书名页是俄文：Е. Н. Чернолуцкая，*Принудительные миграции на советском Дальнем Востоке в 1920–1950-е гг.*，Владивосток: Дальнаука，© Е. Н. Чернолуцкая, 2011。英文并列题 *The Forced Migrations in the Soviet Far East in the 1920s–1950s*。已把 `publication_year` 改为 2011（没有另加 `year`），`language` 改为 `ru`。目录名里的 `_zh` 和「1920s」未改。

### Gregory / Sailors 1976 目录里装的是另一篇

`gregory_sailors_1976_russian_monetary_policy_1861_1913` 的 PDF 是 Paul R. Gregory，*The Russian Balance of Payments, the Gold Standard, and Monetary Policy: A Historical Example of Foreign Capital Movements*，*Journal of Economic History* 39:2（1979年6月），pp. 379–400。脚注把 Gregory and Sailors，*Russian Monetary Policy and Industrialization, 1861–1913*，JEH 36（1976年12月），836–51，引作另一篇文章。作者仍是 Paul R. Gregory，不加入 Joel Sailors。篇名与 `year: 1979` 已按这一 PDF 改写。目录名保留。

### `burbank_2000` 的执笔人是 Popkins

奇偶页眉是 Gareth Popkins。脚注引用 Jane Burbank。原作者「Gareth Popkins (builds on Jane Burbank 1997)」收成 Gareth Popkins。篇名与 *Russian Review* 59（2000年7月）: 408–24 一致，未改。目录名保留。

### Shlapentokh 目录下是 Sinanoglou

`shlapentokh_france_russian_revs` 首页：Ioannis Sinanoglou（Council for European Studies, Columbia University），*France and the Russian Revolutions: The Burden of French Revolutionary History*，*French Politics and Society* 5:3（1987年6月），pp. 30–39。作者改为 Ioannis Sinanoglou，`year: 1987`。目录名保留。

### Zelnik 空目录其实是 Steve A. Smith，1996

`zelnik_1999_workers_intelligentsia` 启动时 title/author 为空。正文首页是 Steve A. Smith，*Workers, the Intelligentsia and Marxist Parties: St Petersburg, 1895–1917 and Shanghai, 1921–1927*，*International Review of Social History* 41（1996），pp. 1–56。已写入，`year: 1996`。同题的 `zelnik_1999_workers_intelligentsia_marxist_parties` 原本已是 Steve A. Smith、IRSH 41（1996），未改。两个目录都没有改名，也没有合并。

### Radkey 已经在「Smith / Captives」目录里，且原本正确

`smith_scott_captives_of_rev_zh` 的书名页是 Oliver Henry Radkey，*The Sickle under the Hammer: The Russian Socialist Revolutionaries in the Early Months of Soviet Rule*（Columbia University Press, 1963），语种 en。中文文件名「锤击镰刀」与 Scott Smith / *Captives* 的目录名都不对应这一册。元数据原本已对，未改，也未改目录名。

## 作者被译者、上传者或占位词挡住的记录

这些记录的 `author` 现为书名页或版权页上的著者。译者和上传者不入作者栏。

- `cheka_red_terror_chronicle_zh`：上传者「一个普通的人」不是作者。书名页无署名。作者「未署作者」。书名「全俄肃反委员会红色恐怖纪事：革命的惩戒之剑」。
- `stalin_major_documents_zh`：同上，上传者不是编者。作者「未署编者」。书名「斯大林，1878–1953（主要文献）」。
- `struggle_against_trotskyism_zh`：上传者不是作者。前部只有目录。作者「未署作者」。书名「布尔什维克党反对托洛茨基主义的斗争」。
- `nationalization_docs_1917_1920_zh`：原先没有 title/author。书名页《苏联工业国有化：1917–1920年文件资料汇编》，生活·读书·新知三联书店，一九五八年·北京。俄文原版版权页 OCR 为 1954 年 Госполитиздат。这一册是 1958 年中文版，`year: 1958`，`language: zh`，作者「未署编者」。没有把未印出的汇编者姓名写进去。Windows 路径仍在 `source_file`；`note`、`sha256`、`quality_check` 未动。
- `socialism_in_one_country_debate_docs_zh`：编者是郑阑干。书名「关于“一国建成社会主义”的讨论」，书名页 2026年5月，`year: 2026`。Zerklora、红锲社、Levski、青山霁、Nekoist 是供稿人。前言署「路人丙」。
- `making_soviet_citizen_education_zh`：书名「苏维埃公民的塑造：苏维埃教育中的品格塑造与公民训练」。前部没有编者名。上传者「一个普通的人」不是编者。作者「未署编者」。没有写入 George Avis。
- `cooper_perrie_1995_davies_festschrift_zh`：书名「苏联历史，1917–1953：纪念 R. W. 戴维斯论文集」。中文目录和作者简介里有 Julian Cooper、莫琳·佩里、E. A. 里斯，身份是供稿人和 CREES 同事，书名页没有把他们印成「编」。作者「未署编者」。slug 里的 1995 没有写成版权年。
- 红锲社、文渊亭、真知子、gourd、列宁格勒档案馆、历史资料搬运组、夏宁、老胡、校对者 Uni / 佐仓绫奈，都留在文件名或译校位置，没有写入 `author`。对应著者见文末总表（戈德曼、伊利尤霍夫、利伯、普里斯特兰、罗利、西格尔鲍姆与苏尼、斯米尔诺夫、杰里米·史密斯、S. A. Smith、斯皮岑、苏尼、卡尔中译本等）。

## 书名、卷次和年份与目录名不一致（目录名未改）

- `kakurin_1928_red_army_civil_war`：这一册是 Richard W. Harrison 编订并英译，Casemate，版权 2020。总编辑为 A. S. Bubnov、S. S. Kamenev、M. N. Tukhachevskii、R. P. Eideman。书名 *The Russian Civil War, 1918–1921: An Operational-Strategic Sketch of the Red Army’s Combat Operations*。书名页不署卡库林。俄文原版是莫斯科—列宁格勒 1930。`year: 2020`。
- `davies_industrialisation_en`：书名页是丛书第 1 卷 *The Socialist Offensive: The Collectivisation of Soviet Agriculture, 1929–1930*，R. W. Davies，Macmillan。版权页 © R. W. Davies 1980，1980 年初版，1989 年重印。`year: 1980`。IA 包装页在 `ch00`，书名页在 `ch03`，版权页在 `ch04`。
- `davies_1980_collective_farm_zh`：中文书名页是《苏维埃俄国的工业化》第 2 卷《苏联集体农庄，1929–1930》。这一中文前部没有印出作者姓名。「作者其他著作」页与馆藏英文本第 1 卷的同名书目一致，英文本版权页署 R. W. Davies。作者据此写成 R. W. Davies（R. W. 戴维斯）。这是丛书对照，不是中文书名页上的署名行。中文前部没有版权年，故未写年份。
- `carr_1976_foundations_v3p2`：书名页 *Foundations of a Planned Economy, 1926–1929, Volume Three, Part II*，BY EDWARD HALLETT CARR，© E. H. Carr 1976。这一册不是 Carr 与 Davies 合著（合著的是第 1 卷）。
- `white_2010_sr_alternative`：Elizabeth White，*The Socialist Alternative to Bolshevik Russia: The Socialist Revolutionary Party, 1921–1939*。`ch02`：First published 2011，© 2011 Elizabeth White。同页 LCCN 与 Taylor & Francis e-library 为 2010。`year` 取 2011。目录名里的 2010 保留。
- `treadgold_1955_lenin_and_rivals`：Donald W. Treadgold，*Lenin and His Rivals: The Struggle for Russia’s Future, 1898–1906*。初版 Methuen 1955，© 1955。这一册是 2017 年 Routledge 重印，下载戳 2017-05-13。`year: 1955`。
- `moore_1966_social_origins_zh`：上海译文出版社版权页，巴林顿·摩尔，《专制与民主的社会起源》，2013年1月，ISBN 9787532758593。`year: 2013`。导言提到 1966 年英文原版，那不是这一册的版权年。
- `basil_1984_mensheviks_1917`：John D. Basil，*The Mensheviks in the Revolution of 1917*。版权 © 1983，出版说明为 1984，ISBN 0-89357-109-1。`year: 1984`。
- `steinberg_2017_russian_rev`：Mark D. Steinberg，*The Russian Revolution, 1905–1921*，Oxford Histories。`ch02` 版权页 © Mark D. Steinberg 2017，First Edition published in 2017。`year: 2017`。
- `central_asia_nomads_zh`：Alun Thomas，*Nomads and Soviet Rule: Central Asia under Lenin and Stalin*，I.B. Tauris 2018，© 2018 Alun Thomas（版权页在 `ch04`）。正文是英文。`language` 由 zh 改为 en。
- `goldman_inventing_enemy_zh`：Wendy Z. Goldman，*Inventing the Enemy: Denunciation and Terror in Stalin’s Russia*，© 2011，初版 2011。正文是英文。`language` 由 zh 改为 en。中文文件名未改。
- `stalin_and_war_1918_1953_zh`：David R. Shearer，*Stalin and War, 1918–1953: Patterns of Repression, Mobilization, and External Threat*，© 2024 David R. Shearer，Routledge（书名页 `ch03`，版权页 `ch04`）。`language` 由 zh 改为 en。`year: 2024`。
- `ru_rev_state_working_class`：Димитрий Чураков，*Революция, государство, рабочий протест*，Москва: РОССПЭН, 2004。`language` 由 en 改为 ru。
- `mawdsley_1987_civil_war_zh`：中文书名页印「Pegasus 图书公司，纽约，2007 年」，作者 Evan Mawdsley（伊万·莫兹利），书名「俄国内战」。译者不是作者。slug 的 1987 没有印在这一前部，故未写年份。2007 是这一中文题页上的版本年，也没有另建字段。
- `plekhanov_dzerzhinsky_zh`：书是伊利亚·拉特科夫斯基，《捷尔任斯基：从“天文学家”到“钢铁费利克斯”》。目录名里的 Plekhanov 与这一册不符。未改目录名。
- `raleigh_2001_provincial_landscapes_zh`：封面印「地方风貌 / 苏联权力的地方纬度1917—1953 / 唐纳德·J·罗利编 / 红锲社译」。英文并列题是 *Provincial Landscapes: Local Dimensions of Soviet Power, 1917–1953*。中文题页用的是「纬」。`title` 按中文题页作「地方风貌：苏联权力的地方纬度，1917–1953」，冒号是两行书名的编目连接。红锲社是译者。前部没有版权年。
- `gaida_2003_liberal_opposition_zh`：前两切片是目录和导言，没有重印署名。作者「Ф. А. 盖达」来自文件名括号中的「Ф.А.盖达著」，不是版权行。书名「走向权力之路的自由主义反对派（1914年—1917年春）」。译者「列宁格勒档案馆」不是作者。slug 的 2003 未写成版权年。
- `october_socialist_rev_zh`：选译者徐天新，书名「俄国十月社会主义革命」（页上亦作「十月社会主义革命」，商务印书馆，世界史资料丛刊）。切片说明里的「1997」是抽取注记，OCR 版权行不可读，故未写年份。
- `zhang_jianhua_political_radicalism_zh`：封面「张建华 等/著」「政治激进主义与近代俄国政治」。`language` 补为 zh。前言「2009年1月」不是版权页，未写年份。
- `psr_study_1901_1925_zh`：解国良，《俄国社会革命党研究（1901–1925）》。`language` 由空补为 zh。封面 OCR 没有版权年。
- `spitsyn_russia_ussr_v3_zh` 与 `spitsyn_textbook_zh` 都是叶夫根尼·斯皮岑的第三卷中译本，题名不同（完整教科书第三卷 / 昨日苏联译丛【04】）。两份都补了作者和书名。没有合并目录。
- `carr_bolshevik_rev_v1_zh` / `v2_zh` / `v3_zh`：作者 E. H. Carr（爱德华·哈利特·卡尔）。书名「苏维埃俄国史：布尔什维克革命（1917–1923）」第一、二、三卷。夏宁与「历史资料搬运组」（2024-12-17）是译者。中文前部没有印 1950/1951/1953，英文本姐妹卷才有这些年，故中译本未写年份。v1 第一页是空白图，书名来自文件名与译者前言。

## 既有 34 篇论文

7 篇改了署名清洁度、篇名或年份，见上及总表：Gregory 1979 错装、Hoch 去掉 `(Author: )` 并补全副题与所有格、Priestland 去掉单位括号、Kotsonis 去掉 `(author)`、Popkins 去掉括注、Rieber 的 AHR 卷期由 106:4 改为首页所印的 Vol. 106, No. 5（Dec. 2001），pp. 1651–1691、Bowman 的 `Russias` 改为 `Russia's`。Kotsonis 首页编码损坏，干净署名在 PDF 第 2 页：*Kritika* 12, 1（Winter 2011）: 25–52，Yanni Kotsonis。Hoch 页为 *Slavic Review* 63:2（Summer 2004），pp. 247–274。这些篇名里已经带年份的，没有再加 `year` 键。Gregory 原无年份键，补了 `year: 1979`。

其余 27 篇首页或页眉与原 `author` / `title` 相符，未改。其中包括赵旭黎、陈爱茹两篇。目录式姓名（Frank, Stephen P.；Gaudin, Corinne；Weissman, Neil；Rigby, T. H.）与首页是同一人，保持原顺序。Hunter & Szyrmer 的 & / and、Duval 篇名的细微标点、Frank 篇名里多出的逗号，都没有为了排版去改。

未改的 27 篇：`ali_1974_aspects_of_rkpb_secretariat_1919_1922`，`davidian_1997_military_censorship_civil_war_1918_1920_ru`，`duval_1979_sverdlov_and_vtsik_october_1917_july_1918`，`engelstein_1993_combined_underdevelopment_discipline_law`，`fitzpatrick_1993_ascribing_class_social_identity_soviet_russia`，`frank_1987_popular_justice_russian_peasantry_1870_1900`，`gaudin_1998_no_place_to_lay_my_head_stolypin`，`haimson_1964_social_stability_urban_russia_pt1`，`haimson_1965_social_stability_urban_russia_pt2`，`hasegawa_1973_militia_february_revolution_dual_power`，`hatch_1987_working_class_politics_moscow_mensheviks_1921_22`，`hatch_1989_lenin_levy_workers_moscow_1921_1928`，`hoch_1994_on_good_numbers_and_bad_peasant_living`，`holquist_1997_bolshevik_surveillance_pan_european`，`hunter_szyrmer_1991_testing_early_soviet_economic_alternatives`，`khlevniuk_2001_stalin_and_state_security_organs_ru`，`lih_2000_bukharins_illusion_war_communism_and_nep`，`melancon_1988_who_wrote_what_february_1917_proclamations`，`nep_early_grain_policy_peasant_resistance_zh`，`oppenheim_1973_supreme_economic_council_1917_1921`，`plaggenborg_1990_who_paid_industrialisation_tsarist_russia`，`plaggenborg_1995_tax_policy_peasant_poverty_1881_1905`，`rigby_1988_origins_of_nomenklatura_system`，`sanborn_2000_mobilization_of_1914_russian_nation`，`stalin_vs_bukharin_rykov_nep_debate_zh`，`weissman_1986_prohibition_alcohol_control_1920s_nep`，`wheatcroft_1974_reliability_prewar_grain_statistics`。

## 看见了前部、仍不补作者或年份的记录

- `soviet_grain_production_1913_1944`：前两切片是俄文统计表，没有书名页。原书名「苏联粮食生产 1913–1944」、`language: ru` 保留。作者保持空白。
- `cohen_1973_bukharin`、`erlich_1960_industrialization`、`lewin_1968_peasants`：中文书名、作者和 `pub_year` 原本已有，只缺 `language`。这一轮没有打开它们的书名页，所以没有补语种。
- 卡尔中译三卷、戴维斯中文第 2 卷、盖达、毛德斯利、十月资料、张建华、社会革命党研究：见上文，年份或作者的依据不够印成版权行的，没有写成确定年。

## 总表（94 份写入后的值）

「年份」列是这一记录上实际存在的年份键。`class_formation_comparative_2008` 的 `pub_year: 2008` 是原有值，本轮只改了 `author`。

| 目录 | 改动字段 | 作者 | 书名 / 篇名 | 年份 |
|---|---|---|---|---|
| `primary/bonnell_1983_russian_worker_memoirs` | title, author, year | Victoria E. Bonnell (ed.) | The Russian Worker: Life and Labor under the Tsarist Regime | year=1983 |
| `primary/cheka_red_terror_chronicle_zh` | title, author | 未署作者 | 全俄肃反委员会红色恐怖纪事：革命的惩戒之剑 | — |
| `primary/kakurin_1928_red_army_civil_war` | title, author, year | A. S. Bubnov, S. S. Kamenev, M. N. Tukhachevskii and R. P. Eideman (general editors); Richard W. Harrison (ed. and trans.) | The Russian Civil War, 1918–1921: An Operational-Strategic Sketch of the Red Army’s Combat Operations | year=2020 |
| `primary/martov_zinoviev_1920_halle` | title, author, year | L. Martov and G. E. Zinoviev; Ben Lewis and Lars T. Lih (introductory essays) | Martov and Zinoviev: Head to Head in Halle | year=2011 |
| `primary/nationalization_docs_1917_1920_zh` | title, author, year, language | 未署编者 | 苏联工业国有化：1917–1920年文件资料汇编 | year=1958 |
| `primary/socialism_in_one_country_debate_docs_zh` | title, author, year | 郑阑干（编） | 关于“一国建成社会主义”的讨论 | year=2026 |
| `primary/stalin_major_documents_zh` | title, author | 未署编者 | 斯大林，1878–1953（主要文献） | — |
| `primary/tragedy_soviet_village_v2_1929_zh` | title, author, year | 维·达尼洛夫、罗·曼宁、林·维奥拉（主编）；Н. 伊夫尼茨基（责任编辑） | 苏联农村的悲剧：集体化与消灭富农 文献和材料 第2卷（1929年11月—1930年12月） | year=2000 |
| `monographs/basil_1984_mensheviks_1917` | title, author, year | John D. Basil | The Mensheviks in the Revolution of 1917 | year=1984 |
| `monographs/boll_1979_red_guards` | title, author, year | Michael M. Boll | The Petrograd Armed Workers Movement in the February Revolution (February–July, 1917): A Study in the Radicalization of the Petrograd Proletariat | year=1979 |
| `monographs/carr_1950_bolshevik_rev_v1_en` | title, author, year | Edward Hallett Carr | A History of Soviet Russia: The Bolshevik Revolution, 1917–1923, Volume One | year=1950 |
| `monographs/carr_1976_foundations_v3p2` | title, author, year | Edward Hallett Carr | A History of Soviet Russia: Foundations of a Planned Economy, 1926–1929, Volume Three, Part II | year=1976 |
| `monographs/carr_1979_lenin_to_stalin` | title, author, year | Edward Hallett Carr | The Russian Revolution: From Lenin to Stalin | year=1979 |
| `monographs/carr_bolshevik_rev_v1_zh` | title, author | E. H. Carr（爱德华·哈利特·卡尔） | 苏维埃俄国史：布尔什维克革命（1917–1923）第一卷 | — |
| `monographs/carr_bolshevik_rev_v2_zh` | title, author | E. H. Carr（爱德华·哈利特·卡尔） | 苏维埃俄国史：布尔什维克革命（1917–1923）第二卷 | — |
| `monographs/carr_bolshevik_rev_v3_zh` | title, author | E. H. Carr（爱德华·哈利特·卡尔） | 苏维埃俄国史：布尔什维克革命（1917–1923）第三卷 | — |
| `monographs/central_asia_nomads_zh` | title, author, year, language | Alun Thomas | Nomads and Soviet Rule: Central Asia under Lenin and Stalin | year=2018 |
| `monographs/class_formation_comparative_2008` | author | Michael Burrage | Class Formation, Civil Society and the State: A Comparative Analysis of Russia, France, the US and England | pub_year=2008（原有，未改） |
| `monographs/cooper_perrie_1995_davies_festschrift_zh` | title, author | 未署编者 | 苏联历史，1917–1953：纪念 R. W. 戴维斯论文集 | — |
| `monographs/davies_1980_collective_farm_zh` | title, author | R. W. Davies（R. W. 戴维斯） | 苏维埃俄国的工业化 第2卷：苏联集体农庄，1929–1930 | — |
| `monographs/davies_industrialisation_en` | title, author, year | R. W. Davies | The Industrialisation of Soviet Russia, Vol. 1: The Socialist Offensive. The Collectivisation of Soviet Agriculture, 1929–1930 | year=1980 |
| `monographs/filtzer_1986_soviet_workers` | title, author, year | Donald Filtzer | Soviet Workers and Stalinist Industrialization: The Formation of Modern Soviet Production Relations, 1928–1941 | year=1986 |
| `monographs/fitzpatrick_1978_cultural_rev_zh` | title, author | 希拉·菲茨帕特里克（编） | 俄国的文化革命，1928–1931 | — |
| `monographs/fitzpatrick_1979_education_mobility` | title, author, year | Sheila Fitzpatrick | Education and Social Mobility in the Soviet Union, 1921–1934 | year=1979 |
| `monographs/fitzpatrick_1991_russia_era_nep` | title, author, year | Sheila Fitzpatrick, Alexander Rabinowitch and Richard Stites (eds.) | Russia in the Era of NEP: Explorations in Soviet Society and Culture | year=1991 |
| `monographs/foglesong_1995_secret_war_zh` | title, author | 戴维·S·福格尔松 | 美国对抗布尔什维克主义的秘密战争：1917–1920年美国对俄国内战的干涉 | — |
| `monographs/french_and_russian_rev_analogies` | title, author, year | Isaac Deutscher | The French Revolution and the Russian Revolution: Some Suggestive Analogies | year=1952 |
| `monographs/frenchmen_rev_heritage_russia` | title, author, year | Ioannis Sinanoglou | Frenchmen, Their Revolutionary Heritage, and the Russian Revolution | year=1980 |
| `monographs/gaida_2003_liberal_opposition_zh` | title, author | Ф. А. 盖达 | 走向权力之路的自由主义反对派（1914年—1917年春） | — |
| `monographs/goldman_1993_women_state_rev_zh` | title, author | 温迪·Z·戈德曼 | 妇女、国家与革命：苏联家庭政策和社会生活，1917–1936 | — |
| `monographs/goldman_inventing_enemy_zh` | title, author, year, language | Wendy Z. Goldman | Inventing the Enemy: Denunciation and Terror in Stalin’s Russia | year=2011 |
| `monographs/haimson_1987_three_revolutionaries` | title, author, year | Leopold H. Haimson, in collaboration with Ziva Galili y Garcia and Richard Wortman | The Making of Three Russian Revolutionaries: Voices from the Menshevik Past | year=1987 |
| `monographs/hobsbawm_1959_primitive_rebels_zh` | title, author, year | 艾瑞克·霍布斯鲍姆 | 原始的叛乱：十九至二十世纪社会运动的古朴形式 | year=1959 |
| `monographs/hoffmann_2011_cultivating_masses_zh` | title, author | 大卫·L·霍夫曼 | 培养群众：现代国家实践与苏联社会主义，1914–1939 | — |
| `monographs/ilyukhov_bolshevik_pay_zh` | title, author | 亚历山大·伊利尤霍夫 | 布尔什维克如何发薪：1917–1941年苏维埃政权的工资制度 | — |
| `monographs/jacobin_ancestry_soviet_communism` | title, author, year | William Henry Chamberlin | The Jacobin Ancestry of Soviet Communism | year=1958 |
| `monographs/katasonov_stalin_economy_zh` | title, author | 瓦·卡塔索诺夫 | 斯大林的经济 | — |
| `monographs/koenker_1981_moscow_workers_zh` | title, author, year | 黛安·P·肯克 | 莫斯科工人与1917年革命 | year=1981 |
| `monographs/lebsky_working_class_paternalism_zh` | title, author | 马克西姆·莱布斯基 | 苏联的工人阶级：工业家长制下的生活 | — |
| `monographs/lenin_how_became_leader_zh` | title, author | 弗拉德连·洛吉诺夫 | 弗拉基米尔·列宁：如何成为领袖 | — |
| `monographs/levy_1987_socialism_intelligentsia` | title, author, year | Carl Levy (ed.) | Socialism and the Intelligentsia, 1880–1914 | year=1987 |
| `monographs/liber_1992_soviet_ukraine_zh` | title, author | 乔治·O·利伯 | 乌克兰苏维埃的苏维埃民族政策、城市发展与身份变迁，1923–1934 | — |
| `monographs/loginov_lenin_bio_zh` | title, author | 弗拉德连·洛吉诺夫 | 列宁全传 | — |
| `monographs/loginov_lenin_in_1917_zh` | title, author | В. Т. 洛吉诺夫 | 列宁在1917年：面对稍纵即逝的契机 | — |
| `monographs/making_soviet_citizen_education_zh` | title, author | 未署编者 | 苏维埃公民的塑造：苏维埃教育中的品格塑造与公民训练 | — |
| `monographs/manning_1982_crisis_old_order_zh` | title, author | 罗伯塔·汤普森·曼宁 | 俄国旧秩序的危机：绅士与政府 | — |
| `monographs/mawdsley_1987_civil_war_zh` | title, author | Evan Mawdsley（伊万·莫兹利） | 俄国内战 | — |
| `monographs/mayer_1999_lenin_jacobin` | title, author, year | Robert Mayer | Lenin and the Jacobin Identity in Russia | year=1999 |
| `monographs/moore_1966_social_origins_zh` | title, author, year | 巴林顿·摩尔 | 专制与民主的社会起源 | year=2013 |
| `monographs/mozokhin_extrajudicial_powers_zh` | title, author | 奥列格·鲍里索维奇·莫佐欣 | 苏联国家安全机关：镇压的权利，1918年至1953年 | — |
| `monographs/nineteenth_c_russian_intelligentsia` | title, author, year | N. G. O. Pereira | The Nineteenth-Century Russian Intelligentsia and the Future of Russia | year=1979 |
| `monographs/october_socialist_rev_zh` | title, author | 徐天新（选译） | 俄国十月社会主义革命 | — |
| `monographs/other_side_of_nep_1923_1925_zh` | title, author | 尤里·茹科夫 | 新经济政策的另一面：1923–1925年苏联的经济与政治斗争 | — |
| `monographs/plekhanov_dzerzhinsky_zh` | title, author | 伊利亚·拉特科夫斯基 | 捷尔任斯基：从“天文学家”到“钢铁费利克斯” | — |
| `monographs/priestland_2007_stalinism_mobilization_zh` | title, author | 大卫·普里斯特兰 | 斯大林主义与动员政治：战间俄国的思想、权力与恐怖 | — |
| `monographs/psr_study_1901_1925_zh` | title, author, language | 解国良 | 俄国社会革命党研究（1901–1925） | — |
| `monographs/raleigh_2001_provincial_landscapes_zh` | title, author | 唐纳德·J·罗利（编） | 地方风貌：苏联权力的地方纬度，1917–1953 | — |
| `monographs/roobol_1976_tsereteli` | title, author, year | W. H. Roobol | Tsereteli — A Democrat in the Russian Revolution: A Political Biography | year=1976 |
| `monographs/ru_rev_state_working_class` | title, author, year, language | Димитрий Чураков | Революция, государство, рабочий протест: Формы, динамика и природа массовых выступлений рабочих в Советской России, 1917–1918 годы | year=2004 |
| `monographs/service_2009_russian_rev` | title, author, year | Robert Service | The Russian Revolution (fourth edition) | year=2009 |
| `monographs/service_2009_trotsky_zh` | title, author | 罗伯特·瑟维斯 | 托洛茨基：一部传记 | — |
| `monographs/service_lenin_v1_zh` | title, author | 罗伯特·瑟维斯 | 列宁：政治生涯 第一卷 矛盾的力量 | — |
| `monographs/shlapentokh_france_russian_revs` | title, author, year | Ioannis Sinanoglou | France and the Russian Revolutions: The Burden of French Revolutionary History | year=1987 |
| `monographs/siegelbaum_1992_state_and_society` | title, author, year | Lewis H. Siegelbaum | Soviet State and Society between Revolutions, 1918–1929 | year=1992 |
| `monographs/siegelbaum_suny_1994_making_workers_soviet` | title, author, year | Lewis H. Siegelbaum and Ronald Grigor Suny (eds.) | Making Workers Soviet: Power, Class, and Identity | year=1994 |
| `monographs/siegelbaum_suny_1994_making_workers_zh` | title, author | 刘易斯·H·西格尔鲍姆、罗纳德·格里戈尔·苏尼（编） | 塑造苏联工人：权力、阶级与身份认同 | — |
| `monographs/smirnov_red_army_1917_1937_zh` | title, author | A. A. 斯米尔诺夫 | 工农红军：军队建设中的致命错误，1917–1937 | — |
| `monographs/smith_jeremy_1999_national_question_zh` | title, author | 杰里米·史密斯 | 布尔什维克与民族问题，1917–1923 | — |
| `monographs/smith_sa_1983_red_petrograd_zh` | title, author | S. A. Smith | 红色彼得格勒：工厂中的革命，1917–18 | — |
| `monographs/soviet_democracy_and_stalin_zh` | title, author | 迈克尔·库比 | 苏联民主与斯大林：1917年至1953年苏联的理论与实践 | — |
| `monographs/soviet_far_east_forced_migration_1920s_zh` | title, author, publication_year, language | Е. Н. Чернолуцкая | Принудительные миграции на советском Дальнем Востоке в 1920–1950-е гг. | publication_year=2011 |
| `monographs/soviet_women_zh` | title, author | 威廉·M·曼德尔 | 苏联妇女 | — |
| `monographs/spitsyn_russia_ussr_v3_zh` | title, author | 叶夫根尼·尤里耶维奇·斯皮岑 | 俄罗斯—苏联在1917–1945：俄罗斯历史完整教科书第三卷 | — |
| `monographs/spitsyn_textbook_zh` | title, author | 叶夫根尼·斯皮岑 | 苏联—俄罗斯历史教程第三卷：二战前夜的苏联简史 | — |
| `monographs/stalin_and_war_1918_1953_zh` | title, author, year, language | David R. Shearer | Stalin and War, 1918–1953: Patterns of Repression, Mobilization, and External Threat | year=2024 |
| `monographs/steinberg_2017_russian_rev` | title, author, year | Mark D. Steinberg | The Russian Revolution, 1905–1921 | year=2017 |
| `monographs/struggle_against_trotskyism_zh` | title, author | 未署作者 | 布尔什维克党反对托洛茨基主义的斗争 | — |
| `monographs/suny_2017_red_flag_unfurled_zh` | title, author, year | 罗纳德·格里戈尔·苏尼 | 红旗飘扬：历史、历史学家与俄国革命 | year=2017 |
| `monographs/treadgold_1955_lenin_and_rivals` | title, author, year | Donald W. Treadgold | Lenin and His Rivals: The Struggle for Russia’s Future, 1898–1906 | year=1955 |
| `monographs/trotsky_1905_zh` | title, author | 列夫·达维多维奇·托洛茨基 | 1905 | — |
| `monographs/velikanova_2013_popular_perception` | title, author, year | Olga Velikanova | Popular Perceptions of Soviet Politics in the 1920s: Disenchantment of the Dreamers | year=2013 |
| `monographs/white_2010_sr_alternative` | title, author, year | Elizabeth White | The Socialist Alternative to Bolshevik Russia: The Socialist Revolutionary Party, 1921–1939 | year=2011 |
| `monographs/zelnik_1999_workers_intelligentsia` | title, author, year | Steve A. Smith | Workers, the Intelligentsia and Marxist Parties: St Petersburg, 1895–1917 and Shanghai, 1921–1927 | year=1996 |
| `monographs/zemskov_stalin_era_zh` | title, author | 维克托·尼古拉耶维奇·泽姆斯科夫 | 斯大林时代：经济、镇压、工业化 | — |
| `monographs/zhang_jianhua_political_radicalism_zh` | title, author, language | 张建华 等 | 政治激进主义与近代俄国政治 | — |
| `monographs/zhukov_zinoviev_zh` | title, author, year | 尤里·茹科夫 | 格里高利·季诺维也夫：被遗忘的世界革命领袖 | year=2021 |
| `monographs/bukharin_preobrazhensky_debate_zh` | author, year | 刘伟、平新乔 | 平衡与非平衡：布哈林与普列奥布拉仁斯基之争 | year=1989 |
| `articles/gregory_sailors_1976_russian_monetary_policy_1861_1913` | title, year | Paul R. Gregory | The Russian Balance of Payments, the Gold Standard, and Monetary Policy: A Historical Example of Foreign Capital Movements (Journal of Economic History, 39:2, 1979) | year=1979 |
| `articles/hoch_2004_did_emancipated_serfs_pay_too_much` | title, author | Steven L. Hoch | Did Russia's Emancipated Serfs Really Pay Too Much for Too Little Land? Statistical Anomalies and Long-Tailed Distributions (Slavic Review, 63:2, 2004) | — |
| `articles/priestland_1997_bolshevik_ideology_party_state_relations` | author | David Priestland | Bolshevik Ideology and the Debate Over Party-State Relations, 1918–21 (Revolutionary Russia, 10:2, 1997) | — |
| `articles/kotsonis_2011_problem_of_individual_stolypin_reforms` | author | Yanni Kotsonis | The Problem of the Individual in the Stolypin Reforms (Kritika, 12:1, 2011) | — |
| `articles/burbank_2000_code_versus_custom_volost_court_appeals` | author | Gareth Popkins | Code versus Custom? Norms and Tactics in Peasant Volost Court Appeals, 1889–1917 (Russian Review, 59:3, 2000) | — |
| `articles/rieber_2001_stalin_man_of_the_borderlands` | title | Alfred J. Rieber | Stalin, Man of the Borderlands (American Historical Review, 106:5, 2001) | — |
| `articles/bowman_1993_russias_first_income_taxes_1885_1914` | title | Linda Bowman | Russia's First Income Taxes: The Effects of Modernized Taxes on Commerce and Industry, 1885–1914 (Slavic Review, 52:2, 1993) | — |
