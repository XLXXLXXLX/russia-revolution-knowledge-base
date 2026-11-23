# W62 入库日志：1861–1918 期刊论文（Grok）

日期：2026-11-23。角色只做找文献、下载、提取与扉页核验。未写 `reading-notes/`，未写 `CLM-*`，未改书目总表、愿望单、README、`framework/` 或已有卡片。

入库前 `sources/articles/` 已有 34 个目录，本批 15 个 slug 均不在其中，也未覆盖任何已有目录。15 篇 PDF 均在 `inbox/articles/<slug>.pdf`，提取文本 `needs_ocr: false`、`empty_page_ratio: 0.0`，抽读扉页与正文页可连成句子。作者、篇名、年份、语种按扉页写回各篇 `manifest.yaml`。这些文件来自 Sci-Hub / JSTOR 存档，不是开放获取，因此没有写入 `sources/web-archive/W62_1861_1918/`。

合计提取字符 **1,163,891**。

| slug | 作者 | 年 | 篇名 | 期刊 | 字符 | 引文来源专著 |
| --- | --- | --- | --- | --- | ---: | --- |
| `pipes_1964_narodnichestvo_semantic_inquiry` | Richard Pipes | 1964 | Narodnichestvo: A Semantic Inquiry | *Slavic Review* 23:3, 441–458 | 60,088 | `walicki_1969_controversy` |
| `shanin_1981_marx_peasant_commune` | Teodor Shanin | 1981 | Marx, Marxism and the Agrarian Question: I Marx and the Peasant Commune | *History Workshop Journal* 12, 108–128 | 81,282 | `white_2010_sr_alternative` |
| `perrie_1972_peasant_movement_1905_1907` | Maureen Perrie | 1972 | The Russian Peasant Movement of 1905–1907: Its Social Composition and Revolutionary Significance | *Past & Present* 57, 123–155 | 96,446 | `ascher_1992_revolution_1905_v2` |
| `seregny_1988_peasant_unions_1905` | Scott J. Seregny | 1988 | A Different Type of Peasant Movement: The Peasant Unions in the Russian Revolution of 1905 | *Slavic Review* 47:1, 51–67 | 72,019 | `ascher_1992_revolution_1905_v2` |
| `yaney_1964_stolypin_land_reform` | George L. Yaney | 1964 | The Concept of the Stolypin Land Reform | *Slavic Review* 23:2, 275–293 | 71,499 | `ascher_1992_revolution_1905_v2` |
| `keep_1955_social_democracy_first_duma` | J. L. H. Keep | 1955 | Russian Social-Democracy and the First State Duma | *Slavonic and East European Review* 34:82, 180–199 | 72,344 | `ascher_1992_revolution_1905_v2` |
| `fallows_1978_zemstvo_food_supply_1914_1916` | Thomas Fallows | 1978 | Politics and the War Effort in Russia: The Union of Zemstvos and the Organization of the Food Supply, 1914–1916 | *Slavic Review* 37:1, 70–90 | 85,520 | `hasegawa_february_1917` |
| `wildman_1970_february_revolution_russian_army` | Allan Wildman | 1970 | The February Revolution in the Russian Army | *Soviet Studies* 22:1, 3–23 | 75,107 | `rabinowitch_1976_come_to_power_zh` |
| `boyd_1968_origins_of_order_no_1` | John R. Boyd | 1968 | The Origins of Order No. 1 | *Soviet Studies* 19:3, 359–372 | 45,984 | `hasegawa_february_1917`；`rabinowitch_1976_come_to_power_zh` |
| `avrich_1963_workers_control_russian_industry` | Paul H. Avrich | 1963 | The Bolshevik Revolution and Workers' Control in Russian Industry | *Slavic Review* 22:1, 47–63 | 60,968 | `rabinowitch_1976_come_to_power_zh` |
| `guthier_1979_ukrainian_nationalism_1917` | Steven L. Guthier | 1979 | The Popular Base of Ukrainian Nationalism in 1917 | *Slavic Review* 38:1, 30–47 | 64,585 | `figes_1996_peoples_tragedy`；`white_2010_sr_alternative` |
| `hafner_1991_mirbach_left_sr_uprising` | Lutz Hafner | 1991 | The Assassination of Count Mirbach and the "July Uprising" of the Left Socialist Revolutionaries in Moscow, 1918 | *Russian Review* 50:3, 324–344 | 80,792 | `rabinowitch_2007_in_power`；`swain_1996_origins_of_civil_war` |
| `rosenberg_1985_labor_bolshevik_power_after_october` | William G. Rosenberg | 1985 | Russian Labor and Bolshevik Power after October | *Slavic Review* 44:2, 213–238 | 110,137 | `rabinowitch_2007_in_power`；`swain_1996_origins_of_civil_war` |
| `berk_1975_izhevsk_class_tragedy` | Stephen M. Berk | 1975 | The "Class-Tragedy" of Izhevsk: Working-Class Opposition to Bolshevism in 1918 | *Russian History* 2 (1975): 176–190 | 54,803 | `mawdsley_1987_civil_war_zh`；`swain_1996_origins_of_civil_war` |
| `figes_1990_red_army_mass_mobilization` | Orlando Figes | 1990 | The Red Army and Mass Mobilization during the Russian Civil War 1918–1920 | *Past & Present* 129, 168–211 | 132,317 | `mawdsley_1987_civil_war_zh` |

## 扉页核对要点

- Boyd 的页码以 Taylor & Francis 扉页为准：*Soviet Studies* 19:3 (1968): 359–372。长谷川书目写成 395–417，与该 PDF 不符。
- Yaney 页码以 JSTOR 扉页为准：275–293。Ascher 书目作 273–293。
- Keep 篇名以扉页为准：*Russian Social-Democracy and the First State Duma*。Ascher 书目作 “in the First State Duma”。
- Rosenberg 正文起页以扉页为准：213–238。Rabinowitch 2007 书目作 205–238，205 起的页不属于这篇正文。同名短篇 “REPLY”（251–256）未入库。
- Berk 的 PDF 页眉页码为 176–190，与 Mawdsley、Swain 所记 *Russian History* 第 2 卷（1975）一致。期号两书目不一致（Swain 作 no. 2，存档记录作 no. 1），manifest 只写卷、年与页码。
- Guthier 正文多次使用立宪会议选举与省别得票，不是杂志封面或书评汇编。
- Figes 正文讨论 1918–1920 红军大规模征兵，并出现 officer / specialist；Mawdsley 补编将其放在红军与军事专家一节。篇名不是军事专家专论。
- Rosenberg 正文是十月后工厂劳动与布尔什维克权力（factory、union，并有 coalition）。全文未见 Vikzhel / railway。它不是维克热尔谈判专文。

## 书目中有、本批未能下载的相邻论文

- Stephen M. Berk, “The Democratic Counterrevolution: Komuch and the Civil War on the Volga,” *Canadian-American Slavic Studies* 7 (1973)。Mawdsley 与 Swain 都引用。Anna's Archive 无可用 PDF。1918 年工人反布尔什维克暴动改用已下载的 Izhevsk 一文。
- Geoffrey A. Hosking, “P. A. Stolypin and the Octobrists,” *Slavonic and East European Review* 47 (1969)。Ascher 第 2 卷书目引用。检索无命中。杜马宪政改用 Keep 1955。

语种均为英语。
