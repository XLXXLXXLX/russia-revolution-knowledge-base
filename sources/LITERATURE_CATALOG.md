# 俄国革命知识库（1860s–1929）馆藏文献总目 (`sources/LITERATURE_CATALOG.md`)

- **馆藏拆解目录总数**: `283` 部/篇（`sources/primary/` 一手档案原典 `25` 部 + `sources/monographs/` 学术专著/辞书/回忆录 `179` 部 + `sources/articles/` 中英俄同行评议期刊论文 `79` 篇）
- **在线数字原典与史学文库 (`sources/web-archive/`)**: `207` 篇完整多语种全文（合计 `12,637.9 KB`，自动纳入章节级 FTS5 索引）
- **全文状态**: `✅ 可读全文 283 项` | `⚠️ 纯扫描/残卷隔离 (needs_ocr: true) 0 项`
- **支持格式**: `PDF`（PyMuPDF 页码锚点）、`EPUB`（自动合并逐页 XML 切片）、`DOCX/DOC`、`DjVu`（原生纯 Python `ZPCodec + BZZ` 提取 `TXTz` 俄文文本层）、`HTML -> Markdown`（去噪全文归档）。
- **检索协议**: 编排者通过 `python scripts/kb.py locate-chapters "<关键词>"` 毫秒级跨专著、一手档案、三语期刊论文与在线文库定位章节（自动隔离 `needs_ocr: true` 目录），再交 `close-reader` 整章顺读。

## 一、一手档案、会议速记与历史原典 (`sources/primary/`)

| 序号 | 目录 Slug | 信源等级 | 语种 | 题名 | 编者/作者 | 章节数 | 文本体积 (KB) | 状态 |
| ---: | :--- | :---: | :---: | :--- | :--- | ---: | ---: | :--- |
| 1 | `babushkin_memoirs_zh` | `B` | `zh-Hant` | 巴布什金回忆录 | 伊万·瓦西里耶维奇·巴布什金 | 8 | 260.8 | ✅ 可读全文 |
| 2 | `bonnell_1983_russian_worker_memoirs` | `B` | `en` | The Russian Worker: Life and Labor under the Tsarist Regime | Victoria E. Bonnell (ed.) | 8 | 487.2 | ✅ 可读全文 |
| 3 | `bukharin_historical_materialism_zh` | `S` | `zh` | 历史唯物主义理论 | 尼古拉·伊万诺维奇·布哈林 | 16 | 767.5 | ✅ 可读全文 |
| 4 | `bukharin_preobrazhensky_1919_abc_communism_zh` | `S` | `zh` | 共产主义ABC (Азбука коммунизма) | 尼·布哈林、叶·普列奥布拉任斯基 | 5 | 602.0 | ✅ 可读全文 |
| 5 | `cheka_red_terror_chronicle_zh` | `S` | `zh` | 全俄肃反委员会红色恐怖纪事：革命的惩戒之剑 | 未署作者 | 72 | 440.0 | ✅ 可读全文 |
| 6 | `kak_lomali_nep_1928_v1_ru` | `S` | `ru` | Как ломали НЭП. Том 1: Объединенный пленум ЦК и ЦКК ВКП(б) 6–11 апреля 1928 г. | В. П. Данилов, О. В. Хлевнюк (сост.) | 21 | 2918.0 | ✅ 可读全文 |
| 7 | `kak_lomali_nep_1928_v2_ru` | `S` | `ru` | Как ломали НЭП. Том 2: Пленум ЦК ВКП(б) 4–12 июля 1928 г. | В. П. Данилов, О. В. Хлевнюк, А. Ю. Ватлин (сост.) | 32 | 4373.7 | ✅ 可读全文 |
| 8 | `kak_lomali_nep_1928_v3_ru` | `S` | `ru` | Как ломали НЭП. Стенограммы пленумов ЦК ВКП(б) 1928–1929 гг. Том 3: Ноябрьский пленум 1928 г. | В. П. Данилов, О. В. Хлевнюк, А. Ю. Ватлин (сост.) | 26 | 3798.9 | ✅ 可读全文 |
| 9 | `kak_lomali_nep_1929_v4_ru` | `S` | `ru` | Как ломали НЭП. Том 4: Объединенный пленум ЦК и ЦКК ВКП(б) 16–23 апреля 1929 г. | В. П. Данилов, О. В. Хлевнюк (сост.) | 31 | 4571.4 | ✅ 可读全文 |
| 10 | `kak_lomali_nep_1929_v5_ru` | `S` | `ru` | Как ломали НЭП. Том 5: Пленум ЦК ВКП(б) 10–17 ноября 1929 г. | В. П. Данилов, О. В. Хлевнюк (сост.) | 28 | 4259.7 | ✅ 可读全文 |
| 11 | `kakurin_1928_red_army_civil_war` | `S` | `en` | The Russian Civil War, 1918–1921: An Operational-Strategic Sketch of the Red Army’s Combat Operations | A. S. Bubnov, S. S. Kamenev, M. N. Tukhachevskii and R. P. Eideman (general editors); Richard W. Harrison (ed. and trans.) | 32 | 1878.0 | ✅ 可读全文 |
| 12 | `kollontai_1921_workers_opposition` | `S` | `en` | The Workers' Opposition | Alexandra Kollontai | 2 | 115.5 | ✅ 可读全文 |
| 13 | `martov_zinoviev_1920_halle` | `S` | `en` | Martov and Zinoviev: Head to Head in Halle | L. Martov and G. E. Zinoviev; Ben Lewis and Lars T. Lih (introductory essays) | 10 | 655.1 | ✅ 可读全文 |
| 14 | `nationalization_docs_1917_1920_zh` | `S` | `zh` | 苏联工业国有化：1917–1920年文件资料汇编 | 未署编者 | 29 | 1215.7 | ✅ 可读全文 |
| 15 | `preobrazhensky_1926_new_economics_zh` | `S` | `zh` | 新经济学：对苏维埃经济进行理论分析的尝试 | Yevgeni Preobrazhensky (叶·普列奥布拉任斯基) | 19 | 626.1 | ✅ 可读全文 |
| 16 | `short_course_1938_zh` | `S` | `zh` | 联共（布）党史简明教程（文字层补齐版） | 联共（布）中央特设委员会 | 30 | 1007.5 | ✅ 可读全文 |
| 17 | `socialism_in_one_country_debate_docs_zh` | `S` | `zh` | 关于“一国建成社会主义”的讨论 | 郑阑干（编） | 18 | 386.4 | ✅ 可读全文 |
| 18 | `sovetskaya_derevnya_vchk_ogpu_v1_ru` | `S` | `ru` | Советская деревня глазами ВЧК–ОГПУ–НКВД. Том 1: 1918–1922 | А. Берелович, В. П. Данилов (ред.) | 30 | 4195.0 | ✅ 可读全文 |
| 19 | `sovetskaya_derevnya_vchk_ogpu_v2_ru` | `S` | `ru` | Советская деревня глазами ВЧК–ОГПУ–НКВД. Том 2: 1923–1929 | А. Берелович, В. П. Данилов (ред.) | 44 | 6192.0 | ✅ 可读全文 |
| 20 | `sovetskaya_derevnya_vchk_ogpu_v3p1_ru` | `S` | `ru` | Советская деревня глазами ВЧК–ОГПУ–НКВД. Том 3, Книга 1: 1930–1931 | А. Берелович, В. П. Данилов (ред.) | 31 | 4290.5 | ✅ 可读全文 |
| 21 | `stalin_major_documents_zh` | `S` | `zh` | 斯大林，1878–1953（主要文献） | 未署编者 | 16 | 475.3 | ✅ 可读全文 |
| 22 | `stalin_works_v1_1901_1907_zh` | `S` | `zh` | 斯大林全集 第一卷（1901—1907） | 约·维·斯大林 | 41 | 1443.8 | ✅ 可读全文 |
| 23 | `tragedy_soviet_village_v1_1927_1929_zh` | `S` | `zh` | 苏联农村的悲剧：集体化与富农驱逐 文献与资料 第1卷（1927年5月—1929年11月） | 维·彼·达尼洛夫、罗·曼宁、林·维奥拉 编 | 40 | 2760.8 | ✅ 可读全文 |
| 24 | `tragedy_soviet_village_v2_1929_zh` | `S` | `zh` | 苏联农村的悲剧：集体化与消灭富农 文献和材料 第2卷（1929年11月—1930年12月） | 维·达尼洛夫、罗·曼宁、林·维奥拉（主编）；Н. 伊夫尼茨基（责任编辑） | 54 | 2513.7 | ✅ 可读全文 |
| 25 | `trotsky_1905_zh` | `B` | `zh` | 1905 | 列夫·达维多维奇·托洛茨基 | 22 | 892.9 | ✅ 可读全文 |

## 二、学术专著、专业辞书与重要亲历者文献 (`sources/monographs/`)

| 序号 | 目录 Slug | 信源等级 | 语种 | 题名 | 作者/编者 | 章节数 | 文本体积 (KB) | 状态 |
| ---: | :--- | :---: | :---: | :--- | :--- | ---: | ---: | :--- |
| 1 | `allen_2003_farm_to_factory` | `A` | `en` | Farm to Factory: A Reinterpretation of the Soviet Industrial Revolution | Robert C. Allen | 13 | 753.0 | ✅ 可读全文 |
| 2 | `apalkov_intra_party_struggle_zh` | `A` | `zh` | 联共（布）党内斗争：从“集体领导”到斯大林个人统治 | Dmitrii I. Apalkov (德·伊·阿帕利科夫) | 12 | 355.3 | ✅ 可读全文 |
| 3 | `ascher_1988_revolution_of_1905_v1` | `A` | `en` | The Revolution of 1905: Russia in Disarray (Vol. 1) | Abraham Ascher | 9 | 1141.5 | ✅ 可读全文 |
| 4 | `ascher_1992_revolution_1905_v2` | `A` | `en` | The Revolution of 1905: Authority Restored (Vol. 2) | Abraham Ascher | 22 | 1296.3 | ✅ 可读全文 |
| 5 | `ascher_2001_stolypin` | `A` | `en` | P. A. Stolypin: The Search for Stability in Late Imperial Russia | Abraham Ascher | 26 | 1304.2 | ✅ 可读全文 |
| 6 | `avrich_1970_kronstadt` | `A` | `en` | Kronstadt, 1921 | Paul Avrich | 12 | 545.0 | ✅ 可读全文 |
| 7 | `ball_1987_nepmen_zh` | `A` | `zh` | 俄国最后的资本家：新经济政策时期的新商人（1921-1929） | Alan M. Ball | 20 | 620.6 | ✅ 可读全文 |
| 8 | `basil_1984_mensheviks_1917` | `A` | `en` | The Mensheviks in the Revolution of 1917 | John D. Basil | 14 | 571.9 | ✅ 可读全文 |
| 9 | `blanc_2021_rev_sd` | `A` | `en` | 革命社会民主党：俄罗斯帝国全境的工人阶级政治（1882–1917） | 埃里克·布兰克 | 20 | 1243.5 | ✅ 可读全文 |
| 10 | `boll_1979_red_guards` | `A` | `en` | The Petrograd Armed Workers Movement in the February Revolution (February–July, 1917): A Study in the Radicalization of the Petrograd Proletariat | Michael M. Boll | 8 | 517.6 | ✅ 可读全文 |
| 11 | `bonnell_1983_roots_of_rebellion_zh` | `A` | `zh` | 俄国工人运动和组织的根源 (Roots of Rebellion, 1900-1914) | Victoria E. Bonnell | 20 | 1094.0 | ✅ 可读全文 |
| 12 | `bonnell_1983_roots_rebellion` | `A` | `en` | 反叛的根源：圣彼得堡与莫斯科的工人政治与组织（1900–1914） | 维多利亚·E·邦内尔 | 28 | 1383.5 | ✅ 可读全文 |
| 13 | `bonnell_1997_iconography_of_power` | `A` | `en` | Iconography of Power: Soviet Political Posters under Lenin and Stalin | Victoria E. Bonnell | 8 | 706.0 | ✅ 可读全文 |
| 14 | `bukharin_preobrazhensky_debate_zh` | `A` | `zh` | 平衡与非平衡：布哈林与普列奥布拉仁斯基之争 | 刘伟、平新乔 | 1 | 37.1 | ✅ 可读全文 |
| 15 | `burds_1998_peasant_dreams` | `A` | `en` | Peasant Dreams and Market Politics: Labor Migration and the Russian Village, 1861–1905 | Jeffrey Burds | 13 | 834.0 | ✅ 可读全文 |
| 16 | `cao_weian_new_russian_history_zh` | `A` | `zh` | 俄国史新论：从基辅罗斯、莫斯科罗斯到彼得堡罗斯 | 曹维安 | 307 | 876.6 | ✅ 可读全文 |
| 17 | `carr_1950_bolshevik_rev_v1_en` | `A` | `en` | A History of Soviet Russia: The Bolshevik Revolution, 1917–1923, Volume One | Edward Hallett Carr | 18 | 1113.4 | ✅ 可读全文 |
| 18 | `carr_1952_bolshevik_rev_v2_en` | `A` | `en` | The Bolshevik Revolution, 1917–1923, Vol. 2 (The Economic Order) | Edward Hallett Carr | 17 | 1028.7 | ✅ 可读全文 |
| 19 | `carr_1953_bolshevik_rev_v3_en` | `A` | `en` | The Bolshevik Revolution, 1917–1923, Vol. 3 (Soviet Russia and the World) | Edward Hallett Carr | 26 | 1611.8 | ✅ 可读全文 |
| 20 | `carr_1954_interregnum` | `A` | `en` | A History of Soviet Russia: The Interregnum, 1923-1924 | Edward Hallett Carr | 417 | 2134.3 | ✅ 可读全文 |
| 21 | `carr_1958_socialism_in_one_country_v1` | `A` | `en` | Socialism in One Country, 1924–1926, Vol. 1 | Edward Hallett Carr | 23 | 1452.5 | ✅ 可读全文 |
| 22 | `carr_1959_socialism_in_one_country_v2` | `A` | `en` | Socialism in One Country, 1924–1926, Vol. 2 | Edward Hallett Carr | 20 | 1266.8 | ✅ 可读全文 |
| 23 | `carr_1964_socialism_in_one_country_v3p1` | `A` | `en` | Socialism in One Country, 1924–1926, Vol. 3, Part I | Edward Hallett Carr | 25 | 1554.8 | ✅ 可读全文 |
| 24 | `carr_1964_socialism_in_one_country_v3p2` | `A` | `en` | Socialism in One Country, 1924–1926, Vol. 3, Part II | Edward Hallett Carr | 19 | 1213.8 | ✅ 可读全文 |
| 25 | `carr_1976_foundations_v3p2` | `A` | `en` | A History of Soviet Russia: Foundations of a Planned Economy, 1926–1929, Volume Three, Part II | Edward Hallett Carr | 12 | 859.4 | ✅ 可读全文 |
| 26 | `carr_1979_lenin_to_stalin` | `A` | `en` | The Russian Revolution: From Lenin to Stalin | Edward Hallett Carr | 9 | 448.0 | ✅ 可读全文 |
| 27 | `carr_bolshevik_rev_v1_zh` | `A` | `zh` | 苏维埃俄国史：布尔什维克革命（1917–1923）第一卷 | E. H. Carr（爱德华·哈利特·卡尔） | 13 | 923.2 | ✅ 可读全文 |
| 28 | `carr_bolshevik_rev_v2_zh` | `A` | `zh` | 苏维埃俄国史：布尔什维克革命（1917–1923）第二卷 | E. H. Carr（爱德华·哈利特·卡尔） | 11 | 811.4 | ✅ 可读全文 |
| 29 | `carr_bolshevik_rev_v3_zh` | `A` | `zh` | 苏维埃俄国史：布尔什维克革命（1917–1923）第三卷 | E. H. Carr（爱德华·哈利特·卡尔） | 13 | 1143.7 | ✅ 可读全文 |
| 30 | `carr_davies_1969_foundations_v1p1` | `A` | `en` | Foundations of a Planned Economy, 1926-1929, Volume One, Part I | E. H. Carr & R. W. Davies | 16 | 1193.2 | ✅ 可读全文 |
| 31 | `central_asia_nomads_zh` | `A` | `en` | Nomads and Soviet Rule: Central Asia under Lenin and Stalin | Alun Thomas | 22 | 679.8 | ✅ 可读全文 |
| 32 | `class_formation_comparative_2008` | `A` | `en` | Class Formation, Civil Society and the State: A Comparative Analysis of Russia, France, the US and England | Michael Burrage | 25 | 1459.5 | ✅ 可读全文 |
| 33 | `cohen_1973_bukharin` | `A` | `en` | 布哈林与布尔什维克革命：政治传记（1888–1938） | 斯蒂芬·F·科恩 | 22 | 1464.6 | ✅ 可读全文 |
| 34 | `cole_socialist_thought_v3p1_zh` | `B` | `zh` | 社会主义思想史 第三卷上：第二国际 1889–1914 | G. D. H. Cole | 22 | 1142.9 | ✅ 可读全文 |
| 35 | `cole_socialist_thought_v3p2_zh` | `A` | `zh` | 社会主义思想史 第三卷下 第二国际 1889-1914 | G. D. H. Cole | 28 | 1370.3 | ✅ 可读全文 |
| 36 | `cole_socialist_thought_v4p1_zh` | `A` | `zh` | 社会主义思想史 第四卷上 共产主义与社会民主主义 1914-1931 | G. D. H. Cole | 36 | 1809.2 | ✅ 可读全文 |
| 37 | `cole_socialist_thought_v4p2_zh` | `A` | `zh` | 社会主义思想史 第四卷下 共产主义与社会民主主义 1914-1931 | G. D. H. Cole | 15 | 888.1 | ✅ 可读全文 |
| 38 | `cooper_perrie_1995_davies_festschrift_zh` | `A` | `zh` | 苏联历史，1917–1953：纪念 R. W. 戴维斯论文集 | 未署编者 | 16 | 660.7 | ✅ 可读全文 |
| 39 | `corney_2004_telling_october` | `A` | `en` | Telling October: Memory and the Making of the Bolshevik Revolution | Frederick C. Corney | 17 | 854.6 | ✅ 可读全文 |
| 40 | `daniels_1960_conscience` | `A` | `en` | The Conscience of the Revolution: Communist Opposition in Soviet Russia | Robert Vincent Daniels | 23 | 1603.2 | ✅ 可读全文 |
| 41 | `david_fox_1997_revolution_of_the_mind` | `A` | `en` | Revolution of the Mind: Higher Learning among the Bolsheviks, 1918–1929 | Michael David-Fox | 12 | 859.8 | ✅ 可读全文 |
| 42 | `davies_1980_collective_farm_zh` | `A` | `zh` | 苏维埃俄国的工业化 第2卷：苏联集体农庄，1929–1930 | R. W. Davies（R. W. 戴维斯） | 17 | 428.3 | ✅ 可读全文 |
| 43 | `davies_industrialisation_en` | `A` | `en` | The Industrialisation of Soviet Russia, Vol. 1: The Socialist Offensive. The Collectivisation of Soviet Agriculture, 1929–1930 | R. W. Davies | 508 | 1237.8 | ✅ 可读全文 |
| 44 | `deutscher_prophet_trilogy_zh` | `B` | `zh` | 先知三部曲：武装的先知；被解除武装的先知；流亡的先知 | 伊萨克·多伊彻 | 41 | 3523.3 | ✅ 可读全文 |
| 45 | `douds_2018_inside_lenins_government` | `A` | `en` | Inside Lenin's Government: Ideology, Power and Practice in the Early Soviet State | Lara Douds | 18 | 608.8 | ✅ 可读全文 |
| 46 | `emmons_1968_russian_landed_gentry_1861` | `A` | `en` | The Russian Landed Gentry and the Peasant Emancipation of 1861 | Terence Emmons | 21 | 1202.4 | ✅ 可读全文 |
| 47 | `erlich_1960_industrialization` | `A` | `en` | 苏联工业化争论（1924–1928） | 亚历山大·埃尔利赫 | 16 | 464.1 | ✅ 可读全文 |
| 48 | `figes_1996_peoples_tragedy` | `A` | `en` | A People's Tragedy: The Russian Revolution 1891-1924 | Orlando Figes | 32 | 2717.9 | ✅ 可读全文 |
| 49 | `filtzer_1986_soviet_workers` | `A` | `en` | Soviet Workers and Stalinist Industrialization: The Formation of Modern Soviet Production Relations, 1928–1941 | Donald Filtzer | 14 | 869.2 | ✅ 可读全文 |
| 50 | `fitzpatrick_1978_cultural_rev_zh` | `A` | `zh` | 俄国的文化革命，1928–1931 | 希拉·菲茨帕特里克（编） | 17 | 684.7 | ✅ 可读全文 |
| 51 | `fitzpatrick_1979_education_mobility` | `A` | `en` | Education and Social Mobility in the Soviet Union, 1921–1934 | Sheila Fitzpatrick | 13 | 911.7 | ✅ 可读全文 |
| 52 | `fitzpatrick_1991_russia_era_nep` | `A` | `en` | Russia in the Era of NEP: Explorations in Soviet Society and Culture | Sheila Fitzpatrick, Alexander Rabinowitch and Richard Stites (eds.) | 21 | 1047.1 | ✅ 可读全文 |
| 53 | `foglesong_1995_secret_war_zh` | `A` | `zh` | 美国对抗布尔什维克主义的秘密战争：1917–1920年美国对俄国内战的干涉 | 戴维·S·福格尔松 | 18 | 1040.3 | ✅ 可读全文 |
| 54 | `french_and_russian_rev_analogies` | `A` | `en` | The French Revolution and the Russian Revolution: Some Suggestive Analogies | Isaac Deutscher | 14 | 35.5 | ✅ 可读全文 |
| 55 | `frenchmen_rev_heritage_russia` | `A` | `en` | Frenchmen, Their Revolutionary Heritage, and the Russian Revolution | Ioannis Sinanoglou | 20 | 64.5 | ✅ 可读全文 |
| 56 | `gaida_2003_liberal_opposition_zh` | `A` | `zh` | 走向权力之路的自由主义反对派（1914年—1917年春） | Ф. А. 盖达 | 23 | 998.0 | ✅ 可读全文 |
| 57 | `galili_1989_menshevik_leaders` | `A` | `en` | 俄国革命中的孟什维克领袖：社会现实与政治策略 | 齐娃·加利利 | 20 | 1260.6 | ✅ 可读全文 |
| 58 | `getzler_1967_martov` | `A` | `en` | Martov: A Political Biography of a Russian Social Democrat | Israel Getzler | 11 | 846.5 | ✅ 可读全文 |
| 59 | `getzler_1983_kronstadt` | `A` | `en` | Kronstadt 1917–1921: The Fate of a Soviet Democracy | Israel Getzler | 13 | 764.3 | ✅ 可读全文 |
| 60 | `goldman_1993_women_state_rev_zh` | `A` | `zh` | 妇女、国家与革命：苏联家庭政策和社会生活，1917–1936 | 温迪·Z·戈德曼 | 13 | 711.9 | ✅ 可读全文 |
| 61 | `goldman_inventing_enemy_zh` | `A` | `en` | Inventing the Enemy: Denunciation and Terror in Stalin’s Russia | Wendy Z. Goldman | 19 | 643.9 | ✅ 可读全文 |
| 62 | `grant_2022_soviet_nightingales` | `A` | `en` | Soviet Nightingales: Care under Communism | Susan Grant | 22 | 919.6 | ✅ 可读全文 |
| 63 | `haimson_1955_origins` | `A` | `en` | The Russian Marxists and the Origins of Bolshevism | Leopold H. Haimson | 11 | 701.2 | ✅ 可读全文 |
| 64 | `haimson_1987_three_revolutionaries` | `A` | `en` | The Making of Three Russian Revolutionaries: Voices from the Menshevik Past | Leopold H. Haimson, in collaboration with Ziva Galili y Garcia and Richard Wortman | 25 | 1701.1 | ✅ 可读全文 |
| 65 | `haimson_2005_experience` | `A` | `en` | Russia's Revolutionary Experience, 1905-1917: Two Essays | Leopold H. Haimson | 19 | 768.3 | ✅ 可读全文 |
| 66 | `hasegawa_february_1917` | `A` | `en` | The February Revolution, Petrograd, 1917: The End of the Tsarist Regime and the Birth of Dual Power | Tsuyoshi Hasegawa (长谷川毅) | 44 | 1878.1 | ✅ 可读全文 |
| 67 | `heywood_1999_modernising_lenins_russia` | `A` | `en` | Modernising Lenin's Russia: Economic Reconstruction, Foreign Trade and the Railways, 1917–1924 | Anthony Heywood | 21 | 768.9 | ✅ 可读全文 |
| 68 | `hildermeier_psr` | `A` | `en` | The Russian Socialist Revolutionary Party Before the First World War | Manfred Hildermeier | 31 | 1121.8 | ✅ 可读全文 |
| 69 | `hirsch_2005_empire_of_nations_zh` | `A` | `zh` | 民族帝国：民族志知识与苏联的形成 (Empire of Nations) | Francine Hirsch (弗朗辛·赫希) | 14 | 2204.3 | ✅ 可读全文 |
| 70 | `hobsbawm_1959_primitive_rebels_zh` | `A` | `zh` | 原始的叛乱：十九至二十世纪社会运动的古朴形式 | 艾瑞克·霍布斯鲍姆 | 40 | 537.6 | ✅ 可读全文 |
| 71 | `hoffmann_2011_cultivating_masses_zh` | `A` | `zh` | 培养群众：现代国家实践与苏联社会主义，1914–1939 | 大卫·L·霍夫曼 | 15 | 741.6 | ✅ 可读全文 |
| 72 | `ilyukhov_bolshevik_pay_zh` | `A` | `zh` | 布尔什维克如何发薪：1917–1941年苏维埃政权的工资制度 | 亚历山大·伊利尤霍夫 | 26 | 895.4 | ✅ 可读全文 |
| 73 | `jacobin_ancestry_soviet_communism` | `A` | `en` | The Jacobin Ancestry of Soviet Communism | William Henry Chamberlin | 8 | 17.6 | ✅ 可读全文 |
| 74 | `katasonov_stalin_economy_zh` | `A` | `zh` | 斯大林的经济 | 瓦·卡塔索诺夫 | 92 | 571.2 | ✅ 可读全文 |
| 75 | `khalid_2015_making_uzbekistan_zh` | `A` | `zh` | 制造乌兹别克斯坦：民族、帝国和革命 (Making Uzbekistan) | Adeeb Khalid (阿迪卜·哈立德) | 23 | 1237.9 | ✅ 可读全文 |
| 76 | `khlevniuk_2015_stalin` | `A` | `en` | Stalin: New Biography of a Dictator | Oleg V. Khlevniuk | 21 | 1091.8 | ✅ 可读全文 |
| 77 | `klots_domestic_service_ussr_zh` | `A` | `zh` | 苏联的家政服务：妇女解放与性别化的劳动等级制度 (Domestic Service in the Soviet Union) | Alissa Klots | 12 | 715.1 | ✅ 可读全文 |
| 78 | `koenker_1981_moscow_workers_zh` | `A` | `zh` | 莫斯科工人与1917年革命 | 黛安·P·肯克 | 15 | 1052.8 | ✅ 可读全文 |
| 79 | `kotkin_2014_stalin_v1` | `A` | `en` | Stalin, Volume I: Paradoxes of Power, 1878-1928 | Stephen Kotkin | 69 | 3382.5 | ✅ 可读全文 |
| 80 | `kotkin_2017_stalin_v2` | `A` | `en` | Stalin: Waiting for Hitler, 1929–1941 (Vol. 2) | Stephen Kotkin | 72 | 4776.2 | ✅ 可读全文 |
| 81 | `kotsonis_2014_states_of_obligation` | `A` | `en` | States of Obligation: Taxes and Citizenship in the Russian Empire and Early Soviet Republic | Yanni Kotsonis | 33 | 1345.3 | ✅ 可读全文 |
| 82 | `lebsky_working_class_paternalism_zh` | `A` | `zh` | 苏联的工人阶级：工业家长制下的生活 | 马克西姆·莱布斯基 | 14 | 320.8 | ✅ 可读全文 |
| 83 | `leggett_1981_cheka` | `A` | `en` | 契卡：列宁的政治警察——全俄肃清反革命及怠工非常委员会（1917年12月至1922年2月） | 乔治·莱格特 | 19 | 1494.8 | ✅ 可读全文 |
| 84 | `lelichuk_soviet_industrialization_zh` | `A` | `zh` | 苏联工业化 | V. S. Lelchuk | 16 | 722.6 | ✅ 可读全文 |
| 85 | `lenin_how_became_leader_zh` | `A` | `zh` | 弗拉基米尔·列宁：如何成为领袖 | 弗拉德连·洛吉诺夫 | 28 | 1035.2 | ✅ 可读全文 |
| 86 | `levy_1987_socialism_intelligentsia` | `A` | `en` | Socialism and the Intelligentsia, 1880–1914 | Carl Levy (ed.) | 20 | 756.1 | ✅ 可读全文 |
| 87 | `lewin_1968_lenins_last_struggle` | `A` | `en` | Lenin's Last Struggle | Moshe Lewin | 22 | 335.8 | ✅ 可读全文 |
| 88 | `lewin_1968_peasants` | `A` | `en` | 俄国农民与苏维埃政权：农业集体化研究 | 莫希·莱文 | 23 | 1438.3 | ✅ 可读全文 |
| 89 | `liber_1992_soviet_ukraine_zh` | `A` | `zh` | 乌克兰苏维埃的苏维埃民族政策、城市发展与身份变迁，1923–1934 | 乔治·O·利伯 | 16 | 502.7 | ✅ 可读全文 |
| 90 | `liebich_1997_from_the_other_shore` | `A` | `en` | From the Other Shore: Russian Social Democracy after 1921 | André Liebich | 28 | 1345.7 | ✅ 可读全文 |
| 91 | `lih_2006_lenin_rediscovered` | `A` | `en` | Lenin Rediscovered: What Is to Be Done? in Context | Lars T. Lih | 28 | 2149.6 | ✅ 可读全文 |
| 92 | `lih_2006_lenin_rediscovered_zh` | `A` | `zh` | 列宁再发现：在此背景下《怎么办？》 | Lars T. Lih (拉尔斯·T·利赫) | 14 | 993.5 | ✅ 可读全文 |
| 93 | `loginov_lenin_bio_zh` | `A` | `zh` | 列宁全传 | 弗拉德连·洛吉诺夫 | 10 | 2208.7 | ✅ 可读全文 |
| 94 | `loginov_lenin_in_1917_zh` | `A` | `zh` | 列宁在1917年：面对稍纵即逝的契机 | В. Т. 洛吉诺夫 | 35 | 1476.6 | ✅ 可读全文 |
| 95 | `making_soviet_citizen_education_zh` | `A` | `zh` | 苏维埃公民的塑造：苏维埃教育中的品格塑造与公民训练 | 未署编者 | 7 | 490.5 | ✅ 可读全文 |
| 96 | `manning_1982_crisis_old_order_zh` | `A` | `zh` | 俄国旧秩序的危机：绅士与政府 | 罗伯塔·汤普森·曼宁 | 41 | 1484.7 | ✅ 可读全文 |
| 97 | `martin_2001_affirmative_action_empire` | `A` | `en` | The Affirmative Action Empire: Nations and Nationalism in the Soviet Union, 1923–1939 | Terry Martin | 22 | 1413.9 | ✅ 可读全文 |
| 98 | `mawdsley_1987_civil_war` | `A` | `en` | The Russian Civil War | Evan Mawdsley | 33 | 941.8 | ✅ 可读全文 |
| 99 | `mawdsley_1987_civil_war_zh` | `A` | `zh` | 俄国内战 | Evan Mawdsley（伊万·莫兹利） | 22 | 1438.4 | ✅ 可读全文 |
| 100 | `mayer_1999_lenin_jacobin` | `A` | `en` | Lenin and the Jacobin Identity in Russia | Robert Mayer | 29 | 78.4 | ✅ 可读全文 |
| 101 | `mcdonald_2011_face_to_the_village` | `A` | `en` | Face to the Village: The Riazan Countryside Under Soviet Rule, 1921–1930 | Tracy McDonald | 27 | 1075.1 | ✅ 可读全文 |
| 102 | `mckean_1990_st_petersburg_between_revolutions` | `A` | `en` | St. Petersburg Between the Revolutions: Workers and Revolutionaries, June 1907–February 1917 | Robert B. McKean | 26 | 1817.0 | ✅ 可读全文 |
| 103 | `merridale_1990_moscow_politics_zh` | `A` | `zh` | 莫斯科政治与斯大林崛起：首都的共产党（1925-1932） | Catherine Merridale | 18 | 747.2 | ✅ 可读全文 |
| 104 | `moore_1966_social_origins_zh` | `A` | `zh` | 专制与民主的社会起源 | 巴林顿·摩尔 | 16 | 1233.3 | ✅ 可读全文 |
| 105 | `mozokhin_extrajudicial_powers_zh` | `A` | `zh` | 苏联国家安全机关：镇压的权利，1918年至1953年 | 奥列格·鲍里索维奇·莫佐欣 | 19 | 448.1 | ✅ 可读全文 |
| 106 | `nineteenth_c_russian_intelligentsia` | `A` | `en` | The Nineteenth-Century Russian Intelligentsia and the Future of Russia | N. G. O. Pereira | 1 | 31.6 | ✅ 可读全文 |
| 107 | `nove_1964_was_stalin_necessary` | `A` | `en` | Was Stalin Really Necessary? Some Problems of Soviet Economic Policy | Alec Nove | 21 | 731.1 | ✅ 可读全文 |
| 108 | `october_socialist_rev_zh` | `A` | `zh` | 俄国十月社会主义革命 | 徐天新（选译） | 7 | 272.8 | ✅ 可读全文 |
| 109 | `other_side_of_nep_1923_1925_zh` | `A` | `zh` | 新经济政策的另一面：1923–1925年苏联的经济与政治斗争 | 尤里·茹科夫 | 14 | 907.8 | ✅ 可读全文 |
| 110 | `pinnow_2010_lost_to_the_collective_zh` | `A` | `zh` | 集体的失落：自杀与苏联社会主义的承诺（1921—1929） | Kenneth M. Pinnow | 12 | 737.3 | ✅ 可读全文 |
| 111 | `pipes_1990_russian_rev` | `A` | `en` | The Russian Revolution | Richard Pipes | 37 | 2697.8 | ✅ 可读全文 |
| 112 | `pirani_2008_russian_revolution_in_retreat` | `A` | `en` | The Russian Revolution in Retreat, 1920–24: Soviet Workers and the New Communist Elite | Simon Pirani | 13 | 908.2 | ✅ 可读全文 |
| 113 | `plekhanov_dzerzhinsky_zh` | `A` | `zh` | 捷尔任斯基：从“天文学家”到“钢铁费利克斯” | 伊利亚·拉特科夫斯基 | 19 | 1107.9 | ✅ 可读全文 |
| 114 | `priestland_2007_stalinism_mobilization_zh` | `A` | `zh` | 斯大林主义与动员政治：战间俄国的思想、权力与恐怖 | 大卫·普里斯特兰 | 26 | 1121.6 | ✅ 可读全文 |
| 115 | `przeworski_class_formation_zh` | `A` | `zh` | 无产阶级的阶级形成历程：从《资本论》第一卷“原始积累”到最近的一些争议 | Adam Przeworski | 3 | 177.0 | ✅ 可读全文 |
| 116 | `psr_study_1901_1925_zh` | `A` | `zh` | 俄国社会革命党研究（1901–1925） | 解国良 | 438 | 1243.8 | ✅ 可读全文 |
| 117 | `rabinowitch_1968_prelude_zh` | `A` | `zh` | 革命的前奏：彼得格勒布尔什维克与1917年七月起义 | Alexander Rabinowitch (亚历山大·拉宾诺维奇) | 13 | 563.6 | ✅ 可读全文 |
| 118 | `rabinowitch_1976_come_to_power_zh` | `A` | `zh` | 布尔什维克掌权：1917年彼得格勒革命 | Alexander Rabinowitch (亚历山大·拉宾诺维奇) | 20 | 959.9 | ✅ 可读全文 |
| 119 | `rabinowitch_2007_bolsheviks_in_power_zh` | `A` | `ru` | 布尔什维克当权：彼得格勒苏维埃时代的第一年 | 亚历山大·拉比诺维奇 | 21 | 1151.2 | ✅ 可读全文 |
| 120 | `rabinowitch_2007_in_power` | `A` | `en` | The Bolsheviks in Power: The First Year of Soviet Rule in Petrograd | Alexander Rabinowitch (亚历山大·拉宾诺维奇) | 27 | 1422.7 | ✅ 可读全文 |
| 121 | `raleigh_2001_provincial_landscapes_zh` | `A` | `zh` | 地方风貌：苏联权力的地方纬度，1917–1953 | 唐纳德·J·罗利（编） | 18 | 1059.5 | ✅ 可读全文 |
| 122 | `rees_1995_stalinism_soviet_rail_transport_zh` | `A` | `zh` | 斯大林主义与苏联铁路运输（1928–1941） | E. A. Rees | 20 | 630.2 | ✅ 可读全文 |
| 123 | `roobol_1976_tsereteli` | `A` | `en` | Tsereteli — A Democrat in the Russian Revolution: A Political Biography | W. H. Roobol | 10 | 744.0 | ✅ 可读全文 |
| 124 | `rossman_2005_worker_resistance_under_stalin_zh` | `A` | `zh` | 斯大林治下的工人抵抗运动：阶级和革命在车间（1928—1932） | Jeffrey J. Rossman | 8 | 629.0 | ✅ 可读全文 |
| 125 | `ru_rev_state_working_class` | `A` | `ru` | Революция, государство, рабочий протест: Формы, динамика и природа массовых выступлений рабочих в Советской России, 1917–1918 годы | Димитрий Чураков | 15 | 2078.8 | ✅ 可读全文 |
| 126 | `sakharov_2012_crossroads` | `A` | `en` | 在十字路口：关于苏联社会发展前景与道路的讨论（1921–1929） | 瓦连京·亚历山德罗维奇·萨哈罗夫 | 22 | 595.6 | ✅ 可读全文 |
| 127 | `service_2009_russian_rev` | `A` | `en` | The Russian Revolution (fourth edition) | Robert Service | 6 | 321.8 | ✅ 可读全文 |
| 128 | `service_2009_trotsky_zh` | `A` | `zh` | 托洛茨基：一部传记 | 罗伯特·瑟维斯 | 11 | 1416.5 | ✅ 可读全文 |
| 129 | `service_lenin_v1_zh` | `A` | `zh` | 列宁：政治生涯 第一卷 矛盾的力量 | 罗伯特·瑟维斯 | 18 | 592.6 | ✅ 可读全文 |
| 130 | `shlapentokh_france_russian_revs` | `A` | `en` | France and the Russian Revolutions: The Burden of French Revolutionary History | Ioannis Sinanoglou | 11 | 36.2 | ✅ 可读全文 |
| 131 | `siegelbaum_1992_state_and_society` | `A` | `en` | Soviet State and Society between Revolutions, 1918–1929 | Lewis H. Siegelbaum | 10 | 787.8 | ✅ 可读全文 |
| 132 | `siegelbaum_suny_1994_making_workers_soviet` | `A` | `en` | Making Workers Soviet: Power, Class, and Identity | Lewis H. Siegelbaum and Ronald Grigor Suny (eds.) | 19 | 1186.1 | ✅ 可读全文 |
| 133 | `siegelbaum_suny_1994_making_workers_soviet_zh` | `A` | `en` | Making Workers Soviet: Power, Class, and Identity | Lewis H. Siegelbaum、Ronald Grigor Suny（编） | 21 | 1174.4 | ✅ 可读全文 |
| 134 | `siegelbaum_suny_1994_making_workers_zh` | `A` | `zh` | 塑造苏联工人：权力、阶级与身份认同 | 刘易斯·H·西格尔鲍姆、罗纳德·格里戈尔·苏尼（编） | 21 | 1085.4 | ✅ 可读全文 |
| 135 | `skocpol_1979_states_and_social_revolutions_zh` | `A` | `zh` | 国家与社会革命：对法国、俄国和中国的比较分析 | 西达·斯考切波 | 17 | 1055.7 | ✅ 可读全文 |
| 136 | `smele_historical_dictionary_civil_wars` | `B` | `en` | Historical Dictionary of the Russian Civil Wars, 1916–1926 | Jonathan D. Smele | 77 | 4032.9 | ✅ 可读全文 |
| 137 | `smirnov_red_army_1917_1937_zh` | `A` | `zh` | 工农红军：军队建设中的致命错误，1917–1937 | A. A. 斯米尔诺夫 | 40 | 1445.1 | ✅ 可读全文 |
| 138 | `smith_1983_red_petrograd` | `A` | `en` | Red Petrograd: Revolution in the Factories, 1917-1918 | S. A. Smith | 15 | 901.8 | ✅ 可读全文 |
| 139 | `smith_jeremy_1999_national_question_zh` | `A` | `zh` | 布尔什维克与民族问题，1917–1923 | 杰里米·史密斯 | 19 | 600.8 | ✅ 可读全文 |
| 140 | `smith_sa_1983_red_petrograd_zh` | `A` | `zh` | 红色彼得格勒：工厂中的革命，1917–18 | S. A. Smith | 15 | 719.9 | ✅ 可读全文 |
| 141 | `smith_scott_2011_captives_of_revolution` | `A` | `en` | Captives of Revolution: The Socialist Revolutionaries and the Bolshevik Dictatorship, 1918–1923 | Scott B. Smith | 19 | 1220.2 | ✅ 可读全文 |
| 142 | `smith_scott_captives_of_rev_zh` | `A` | `en` | The Sickle under the Hammer: The Russian Socialist Revolutionaries in the Early Months of Soviet Rule | Oliver Henry Radkey | 19 | 1358.8 | ✅ 可读全文 |
| 143 | `sobolev_1899_russian_tariff_policy_zh` | `A` | `zh` | 19世纪下半叶俄国的关税政策 | М. Н. Соболев (米·尼·索博列夫) | 32 | 1680.3 | ✅ 可读全文 |
| 144 | `soviet_democracy_and_stalin_zh` | `A` | `zh` | 苏联民主与斯大林：1917年至1953年苏联的理论与实践 | 迈克尔·库比 | 11 | 533.1 | ✅ 可读全文 |
| 145 | `soviet_far_east_forced_migration_1920s_zh` | `A` | `ru` | Принудительные миграции на советском Дальнем Востоке в 1920–1950-е гг. | Е. Н. Чернолуцкая | 21 | 2402.2 | ✅ 可读全文 |
| 146 | `soviet_grain_production_1913_1944` | `A` | `ru` | 苏联粮食生产 1913–1944 | - | 8 | 588.6 | ✅ 可读全文 |
| 147 | `soviet_women_zh` | `A` | `zh` | 苏联妇女 | 威廉·M·曼德尔 | 19 | 645.4 | ✅ 可读全文 |
| 148 | `soviet_workers_illusions_and_reality_zh` | `A` | `en` | The Soviet Worker: Illusions and Realities | Leonard Schapiro & Joseph Godson (eds.) | 13 | 726.2 | ✅ 可读全文 |
| 149 | `soviet_working_class_industrial_paternalism_zh` | `A` | `zh` | 苏联的工人阶级：工业家长制下的生活 | Максим Лебский (Maksim Lebsky) | 14 | 320.8 | ✅ 可读全文 |
| 150 | `spitsyn_russia_ussr_v3_zh` | `A` | `zh` | 俄罗斯—苏联在1917–1945：俄罗斯历史完整教科书第三卷 | 叶夫根尼·尤里耶维奇·斯皮岑 | 20 | 1329.4 | ✅ 可读全文 |
| 151 | `spitsyn_textbook_zh` | `A` | `zh` | 苏联—俄罗斯历史教程第三卷：二战前夜的苏联简史 | 叶夫根尼·斯皮岑 | 21 | 1091.2 | ✅ 可读全文 |
| 152 | `stalin_and_war_1918_1953_zh` | `A` | `en` | Stalin and War, 1918–1953: Patterns of Repression, Mobilization, and External Threat | David R. Shearer | 15 | 319.9 | ✅ 可读全文 |
| 153 | `stalin_era_economy_repression_1924_1954_zh` | `B` | `zh` | 斯大林时代：经济、镇压、工业化，1924–1954 | 维克托·尼古拉耶维奇·泽姆斯科夫 | 8 | 690.5 | ✅ 可读全文 |
| 154 | `starks_2018_smoking_under_tsars_zh` | `A` | `zh` | 沙皇统治下的吸烟：沙皇俄国烟草史 (Smoking under the Tsars) | Tricia Starks (特里西娅·斯塔克斯) | 14 | 842.3 | ✅ 可读全文 |
| 155 | `steinberg_2017_russian_rev` | `A` | `en` | The Russian Revolution, 1905–1921 | Mark D. Steinberg | 21 | 960.2 | ✅ 可读全文 |
| 156 | `stites_1989_revolutionary_dreams_zh` | `A` | `zh` | 革命的梦想：俄国革命中的乌托邦愿景与实验生活 (Revolutionary Dreams) | Richard Stites (理查德·斯泰茨) | 18 | 995.0 | ✅ 可读全文 |
| 157 | `struggle_against_trotskyism_zh` | `A` | `zh` | 布尔什维克党反对托洛茨基主义的斗争 | 未署作者 | 7 | 422.6 | ✅ 可读全文 |
| 158 | `sukhanov_1922_personal_record` | `S/B-dual` | `en` | The Russian Revolution 1917: A Personal Record | N. N. Sukhanov (ed. & trans. Joel Carmichael) | 32 | 1696.2 | ✅ 可读全文 |
| 159 | `suny_2017_red_flag_unfurled_zh` | `A` | `zh` | 红旗飘扬：历史、历史学家与俄国革命 | 罗纳德·格里戈尔·苏尼 | 10 | 680.6 | ✅ 可读全文 |
| 160 | `swain_1996_origins_of_civil_war` | `A` | `en` | The Origins of the Russian Civil War | Geoffrey Swain | 19 | 750.0 | ✅ 可读全文 |
| 161 | `treadgold_1955_lenin_and_rivals` | `A` | `en` | Lenin and His Rivals: The Struggle for Russia’s Future, 1898–1906 | Donald W. Treadgold | 22 | 776.6 | ✅ 可读全文 |
| 162 | `trotsky_1905_zh` | `B` | `zh` | 1905 | 列夫·达维多维奇·托洛茨基 | 18 | 946.9 | ✅ 可读全文 |
| 163 | `trotsky_1930_history_rr_zh` | `S/B-dual` | `zh` | 俄国革命史（全三卷） | Leon Trotsky (列夫·托洛茨基) | 57 | 2540.0 | ✅ 可读全文 |
| 164 | `velikanova_2013_popular_perception` | `A` | `en` | Popular Perceptions of Soviet Politics in the 1920s: Disenchantment of the Dreamers | Olga Velikanova | 10 | 1265.7 | ✅ 可读全文 |
| 165 | `venturi_1960_roots` | `A` | `en` | Roots of Revolution: A History of the Populist and Socialist Movements in Nineteenth Century Russia | Franco Venturi (Intro by Isaiah Berlin) | 30 | 2758.3 | ✅ 可读全文 |
| 166 | `voitikov_stalin_vs_zinoviev_zh` | `A` | `zh` | 斯大林对抗季诺维也夫 (Сталин против Зиновьева) | Сергей Сергеевич Войтиков (谢·谢·沃伊季科夫) | 28 | 1223.4 | ✅ 可读全文 |
| 167 | `wada_haruki_feb_1917_zh` | `A` | `zh` | 俄国革命：彼得格勒，1917年2月 | 和田春树 (Haruki Wada) | 31 | 1213.0 | ✅ 可读全文 |
| 168 | `walicki_1969_controversy` | `A` | `en` | The Controversy over Capitalism: Studies in the Social Philosophy of the Russian Populists | Andrzej Walicki | 8 | 458.3 | ✅ 可读全文 |
| 169 | `westwood_1964_history_russian_railways_zh` | `A` | `zh` | 俄罗斯铁路史 (A History of Russian Railways) | J. N. Westwood | 16 | 524.2 | ✅ 可读全文 |
| 170 | `white_2010_sr_alternative` | `A` | `en` | The Socialist Alternative to Bolshevik Russia: The Socialist Revolutionary Party, 1921–1939 | Elizabeth White | 18 | 559.9 | ✅ 可读全文 |
| 171 | `women_labor_soviet_industry_zh` | `B` | `zh` | 苏联工业中的妇女劳动 | Н. Д. Араловец (阿拉洛维茨著，丁钱清译) | 6 | 264.2 | ✅ 可读全文 |
| 172 | `xu_tianxin_ussr_history_v4_stalin_model_zh` | `A` | `zh` | 苏联史 第四卷：斯大林模式的形成 | 徐天新 | 431 | 1155.0 | ✅ 可读全文 |
| 173 | `yao_hai_ussr_history_v1_russian_rev_zh` | `A` | `zh` | 苏联史 第一卷 俄国革命 | 姚海 | 503 | 3246.3 | ✅ 可读全文 |
| 174 | `zelnik_1999_workers_intelligentsia` | `A` | `en` | Workers, the Intelligentsia and Marxist Parties: St Petersburg, 1895–1917 and Shanghai, 1921–1927 | Steve A. Smith | 3 | 171.3 | ✅ 可读全文 |
| 175 | `zelnik_1999_workers_intelligentsia_marxist_parties` | `A` | `en` | Workers, the Intelligentsia and Marxist Parties: St Petersburg, 1895–1917 and Shanghai, 1921–1927 | Steve A. Smith | 3 | 180.0 | ✅ 可读全文 |
| 176 | `zemskov_stalin_era_zh` | `A` | `zh` | 斯大林时代：经济、镇压、工业化 | 维克托·尼古拉耶维奇·泽姆斯科夫 | 10 | 697.8 | ✅ 可读全文 |
| 177 | `zhang_jianhua_political_radicalism_zh` | `A` | `zh` | 政治激进主义与近代俄国政治 | 张建华 等 | 44 | 809.6 | ✅ 可读全文 |
| 178 | `zheng_yifan_nep_russia_zh` | `A` | `zh` | 苏联史 第三卷 新经济政策的俄国 | 郑异凡 | 75 | 1715.9 | ✅ 可读全文 |
| 179 | `zhukov_zinoviev_zh` | `A` | `zh` | 格里高利·季诺维也夫：被遗忘的世界革命领袖 | 尤里·茹科夫 | 35 | 1472.8 | ✅ 可读全文 |

## 三、中英俄同行评议核心期刊论文 (`sources/articles/`)

| 序号 | 目录 Slug | 信源等级 | 语种 | 题名 | 作者 | 章节数 | 文本体积 (KB) | 状态 |
| ---: | :--- | :---: | :---: | :--- | :--- | ---: | ---: | :--- |
| 1 | `ali_1974_aspects_of_rkpb_secretariat_1919_1922` | `A` | `en` | Aspects of the RKP(B) Secretariat, March 1919 to April 1922 (Soviet Studies, 26:3, 1974) | Janice Ali | 21 | 63.0 | ✅ 可读全文 |
| 2 | `avrich_1963_workers_control_russian_industry` | `A` | `en` | The Bolshevik Revolution and Workers' Control in Russian Industry (Slavic Review, 22:1, 1963) | Paul H. Avrich | 18 | 61.2 | ✅ 可读全文 |
| 3 | `ball_1984_lenin_and_private_trade` | `A` | `en` | Lenin and the Question of Private Trade in Soviet Russia (Slavic Review, 43:3, 1984) | Alan Ball | 15 | 57.6 | ✅ 可读全文 |
| 4 | `barnett_1994_as_good_as_gold_chervonets` | `A` | `en` | As Good as Gold? A Note on the Chervonets (Europe-Asia Studies, 46:4, 1994) | Vincent Barnett | 1 | 25.5 | ✅ 可读全文 |
| 5 | `barnett_1995_soviet_commodity_markets_nep` | `A` | `en` | Soviet Commodity Markets during NEP (Economic History Review, 48:2, 1995) | Vincent Barnett | 24 | 78.3 | ✅ 可读全文 |
| 6 | `bazarov_thinker_gosplan` | `A` | `ru` | В. А. Базаров – мыслитель, ученый, гражданин (Проблемы прогнозирования, № 6, 2004) | В. С. Клебанер | 1 | 42.6 | ✅ 可读全文 |
| 7 | `berk_1975_izhevsk_class_tragedy` | `A` | `en` | The "Class-Tragedy" of Izhevsk: Working-Class Opposition to Bolshevism in 1918 (Russian History, 2, 1975) | Stephen M. Berk | 1 | 54.4 | ✅ 可读全文 |
| 8 | `bowman_1993_russias_first_income_taxes_1885_1914` | `A` | `en` | Russia's First Income Taxes: The Effects of Modernized Taxes on Commerce and Industry, 1885–1914 (Slavic Review, 52:2, 1993) | Linda Bowman | 28 | 97.7 | ✅ 可读全文 |
| 9 | `boyd_1968_origins_of_order_no_1` | `A` | `en` | The Origins of Order No. 1 (Soviet Studies, 19:3, 1968) | John R. Boyd | 1 | 45.7 | ✅ 可读全文 |
| 10 | `burbank_2000_code_versus_custom_volost_court_appeals` | `A` | `en` | Code versus Custom? Norms and Tactics in Peasant Volost Court Appeals, 1889–1917 (Russian Review, 59:3, 2000) | Gareth Popkins | 1 | 62.2 | ✅ 可读全文 |
| 11 | `causes_west_siberian_uprising_1921` | `A` | `ru` | О причинах Западно-Сибирского крестьянского восстания 1921 г. (Вестник Вятского государственного университета, № 9, 2017) | В. В. Цысь | 1 | 61.0 | ✅ 可读全文 |
| 12 | `davidian_1997_military_censorship_civil_war_1918_1920_ru` | `A` | `ru` | Военная цензура в России в годы гражданской войны 1918–1920 гг. (Cahiers du Monde russe, 38:1–2, 1997) | Ирина Давидян | 10 | 34.3 | ✅ 可读全文 |
| 13 | `davydov_khutsieva_1921_kronstadt_grain_policy` | `A` | `ru` | «Льготнический» фактор экономической политики большевиков и Кронштадтский мятеж (Научный диалог, № 10, 2021) | А. Ю. Давыдов, В. В. Хуциева | 1 | 70.8 | ✅ 可读全文 |
| 14 | `duval_1979_sverdlov_and_vtsik_october_1917_july_1918` | `A` | `en` | Yakov M. Sverdlov and the All-Russian Central Executive Committee of Soviets (VTsIK), October 1917–July 1918 (Soviet Studies, 31:1, 1979) | Charles Duval | 20 | 65.4 | ✅ 可读全文 |
| 15 | `early_gosplan_groman_school_1920s` | `A` | `ru` | Ранний Госплан и научно-методологическая школа В. Г. Громана в 1920–1930-е гг. (Russian Journal of Economic History, 18:3, 2022) | О. Н. Кузнецова | 1 | 76.3 | ✅ 可读全文 |
| 16 | `edmondson_1977_politics_of_hunger_famine_1921` | `A` | `en` | The Politics of Hunger: The Soviet Response to Famine, 1921 (Soviet Studies, 29:4, 1977) | Charles M. Edmondson | 13 | 44.0 | ✅ 可读全文 |
| 17 | `engelstein_1993_combined_underdevelopment_discipline_law` | `A` | `en` | Combined Underdevelopment: Discipline and the Law in Imperial and Soviet Russia (American Historical Review, 98:2, 1993) | Laura Engelstein | 17 | 62.6 | ✅ 可读全文 |
| 18 | `eshn_1928_urals_grain_crisis` | `A` | `ru` | Единый сельскохозяйственный налог 1928 года как инструмент решения хлебозаготовительного кризиса (на материалах Урала) (Бизнес в законе, № 1, 2009) | А. Н. Глебов | 1 | 20.6 | ✅ 可读全文 |
| 19 | `fallows_1978_zemstvo_food_supply_1914_1916` | `A` | `en` | Politics and the War Effort in Russia: The Union of Zemstvos and the Organization of the Food Supply, 1914-1916 (Slavic Review, 37:1, 1978) | Thomas Fallows | 22 | 85.7 | ✅ 可读全文 |
| 20 | `figes_1990_red_army_mass_mobilization` | `A` | `en` | The Red Army and Mass Mobilization during the Russian Civil War 1918-1920 (Past & Present, 129, 1990) | Orlando Figes | 45 | 136.6 | ✅ 可读全文 |
| 21 | `fitzpatrick_1993_ascribing_class_social_identity_soviet_russia` | `A` | `en` | Ascribing Class: The Construction of Social Identity in Soviet Russia (Journal of Modern History, 65:4, 1993) | Sheila Fitzpatrick | 27 | 88.0 | ✅ 可读全文 |
| 22 | `frank_1987_popular_justice_russian_peasantry_1870_1900` | `A` | `en` | Popular Justice, Community, and Culture among the Russian Peasantry, 1870–1900 (Russian Review, 46:3, 1987) | Frank, Stephen P. | 28 | 100.1 | ✅ 可读全文 |
| 23 | `gaida_1917_provisional_government_principles` | `A` | `ru` | Временное правительство: принципы политики в контексте развития революционных процессов в России весной-летом 1917 г. (Исторические исследования, № 6, 2017) | Ф. А. Гайда | 1 | 99.5 | ✅ 可读全文 |
| 24 | `gaudin_1998_no_place_to_lay_my_head_stolypin` | `A` | `en` | No Place to Lay My Head: Marginalization and the Right to Land during the Stolypin Reforms (Slavic Review, 57:4, 1998) | Gaudin, Corinne | 28 | 101.2 | ✅ 可读全文 |
| 25 | `gorbatov_1922_church_valuables_trials_western_siberia` | `A` | `ru` | Судебные процессы по делам о противодействии изъятию церковных ценностей в Западной Сибири (1922–1923) (Новейшая история России, 13:4, 2023) | А. В. Горбатов | 4 | 126.5 | ✅ 可读全文 |
| 26 | `gregory_sailors_1976_russian_monetary_policy_1861_1913` | `A` | `en` | The Russian Balance of Payments, the Gold Standard, and Monetary Policy: A Historical Example of Foreign Capital Movements (Journal of Economic History, 39:2, 1979) | Paul R. Gregory | 23 | 75.6 | ✅ 可读全文 |
| 27 | `guthier_1979_ukrainian_nationalism_1917` | `A` | `en` | The Popular Base of Ukrainian Nationalism in 1917 (Slavic Review, 38:1, 1979) | Steven L. Guthier | 19 | 65.4 | ✅ 可读全文 |
| 28 | `hafner_1991_mirbach_left_sr_uprising` | `A` | `en` | The Assassination of Count Mirbach and the "July Uprising" of the Left Socialist Revolutionaries in Moscow, 1918 (Russian Review, 50:3, 1991) | Lutz Hafner | 22 | 80.6 | ✅ 可读全文 |
| 29 | `haimson_1964_social_stability_urban_russia_pt1` | `A` | `en` | The Problem of Social Stability in Urban Russia, 1905–1917 (Part One) (Slavic Review, 23:4, 1964) | Leopold Haimson | 25 | 84.4 | ✅ 可读全文 |
| 30 | `haimson_1965_social_stability_urban_russia_pt2` | `A` | `en` | The Problem of Social Stability in Urban Russia, 1905–1917 (Part Two) (Slavic Review, 24:1, 1965) | Leopold Haimson | 23 | 73.7 | ✅ 可读全文 |
| 31 | `hasegawa_1973_militia_february_revolution_dual_power` | `A` | `en` | The Formation of the Militia in the February Revolution: An Aspect of the Origins of Dual Power (Slavic Review, 32:2, 1973) | Tsuyoshi Hasegawa | 21 | 72.0 | ✅ 可读全文 |
| 32 | `hatch_1987_working_class_politics_moscow_mensheviks_1921_22` | `A` | `en` | Working-Class Politics in Moscow During the Early NEP: Mensheviks and Workers Organizations, 1921–22 (Soviet Studies, 39:4, 1987) | John B. Hatch | 19 | 70.1 | ✅ 可读全文 |
| 33 | `hatch_1989_lenin_levy_workers_moscow_1921_1928` | `A` | `en` | The Lenin Levy and the Social Origins of Stalinism: Workers and the Communist Party in Moscow, 1921–1928 (Slavic Review, 48:4, 1989) | John B. Hatch | 21 | 92.6 | ✅ 可读全文 |
| 34 | `heinzen_1998_professional_identity_nep_countryside` | `A` | `en` | Professional Identity and the Vision of the Modern Soviet Country Side: Local Agricultural Specialists at the End of the NEP, 1928-1929 (Cahiers du Monde russe, 39:1/2, 1998) | James W. Heinzen | 18 | 76.6 | ✅ 可读全文 |
| 35 | `hoch_1994_on_good_numbers_and_bad_peasant_living` | `A` | `en` | On Good Numbers and Bad: Malthus, Population Trends and Peasant Standard of Living in Late Imperial Russia (Slavic Review, 53:1, 1994) | Steven L. Hoch | 36 | 118.3 | ✅ 可读全文 |
| 36 | `hoch_2004_did_emancipated_serfs_pay_too_much` | `A` | `en` | Did Russia's Emancipated Serfs Really Pay Too Much for Too Little Land? Statistical Anomalies and Long-Tailed Distributions (Slavic Review, 63:2, 2004) | Steven L. Hoch | 29 | 88.9 | ✅ 可读全文 |
| 37 | `holquist_1997_bolshevik_surveillance_pan_european` | `A` | `en` | "Information Is the Alpha and Omega of Our Work": Bolshevik Surveillance in Its Pan-European Context (Journal of Modern History, 69:3, 1997) | Peter Holquist | 36 | 133.9 | ✅ 可读全文 |
| 38 | `hunter_szyrmer_1991_testing_early_soviet_economic_alternatives` | `A` | `en` | Testing Early Soviet Economic Alternatives (Slavic Review, 50:2, 1991) | Holland Hunter & Janusz M. Szyrmer | 16 | 42.6 | ✅ 可读全文 |
| 39 | `keep_1955_social_democracy_first_duma` | `A` | `en` | Russian Social-Democracy and the First State Duma (Slavonic and East European Review, 34:82, 1955) | J. L. H. Keep | 20 | 76.2 | ✅ 可读全文 |
| 40 | `khlevniuk_2001_stalin_and_state_security_organs_ru` | `A` | `ru` | Сталин и органы государственной безопасности (Cahiers du Monde russe, 42:2–4, 2001) | Олег Хлевнюк | 14 | 49.5 | ✅ 可读全文 |
| 41 | `klein_1999_kondratiev_slutsky_conjuncture_institute` | `A` | `en` | The Rise of "Non-October" Econometrics: Kondratiev and Slutsky at the Moscow Conjuncture Institute (History of Political Economy, 31:1, 1999) | Judy L. Klein | 2 | 79.3 | ✅ 可读全文 |
| 42 | `kotsonis_2011_problem_of_individual_stolypin_reforms` | `A` | `en` | The Problem of the Individual in the Stolypin Reforms (Kritika, 12:1, 2011) | Yanni Kotsonis | 2 | 85.6 | ✅ 可读全文 |
| 43 | `landis_2004_between_village_and_kremlin_tambov` | `A` | `en` | Between Village and Kremlin: Confronting State Food Procurement in Civil War Tambov, 1919-20 (Russian Review, 63:1, 2004) | Erik-C. Landis | 1 | 67.3 | ✅ 可读全文 |
| 44 | `left_sr_bolshevik_vtsik_presidium` | `A` | `ru` | Опыт двухпартийности: большевики и левые эсеры в Президиуме ВЦИК II–IV созывов (Вестник Томского государственного университета. История, № 45, 2017) | И. А. Концевой | 1 | 71.5 | ✅ 可读全文 |
| 45 | `lih_2000_bukharins_illusion_war_communism_and_nep` | `A` | `en` | Bukharin's "Illusion": War Communism and the Meaning of NEP (Russian History, 27:1–4, 2000) | Lars T. Lih | 2 | 127.0 | ✅ 可读全文 |
| 46 | `martin_1998_origins_soviet_ethnic_cleansing` | `A` | `en` | The Origins of Soviet Ethnic Cleansing (Journal of Modern History, 70:4, 1998) | Terry Martin | 2 | 158.3 | ✅ 可读全文 |
| 47 | `martin_1998_russification_of_the_rsfsr` | `A` | `en` | The Russification of the RSFSR (Cahiers du Monde russe, 39:1/2, 1998) | Terry Martin | 19 | 72.4 | ✅ 可读全文 |
| 48 | `mcdermott_1995_stalin_comintern_third_period` | `A` | `en` | Stalin and the Comintern during the 'Third Period', 1928-33 (European History Quarterly, 25:3, 1995) | Kevin McDermott | 1 | 55.0 | ✅ 可读全文 |
| 49 | `melancon_1988_who_wrote_what_february_1917_proclamations` | `A` | `en` | Who Wrote What and When?: Proclamations of the February Revolution in Petrograd, 23 February – 1 March 1917 (Soviet Studies, 40:3, 1988) | Michael Melancon | 22 | 87.5 | ✅ 可读全文 |
| 50 | `nep_early_grain_policy_peasant_resistance_zh` | `A` | `zh` | 新经济政策前期苏联粮食政策的负面效应与农民反抗（《俄罗斯研究》2013年第4期） | 赵旭黎 | 1 | 49.1 | ✅ 可读全文 |
| 51 | `oppenheim_1973_supreme_economic_council_1917_1921` | `A` | `en` | The Supreme Economic Council 1917–21 (Soviet Studies, 25:1, 1973) | Samuel A. Oppenheim | 25 | 84.8 | ✅ 可读全文 |
| 52 | `peasant_organs_agrarian_question_1917` | `A` | `ru` | Представительные органы крестьянского и казачьего самоуправления в решении аграрного вопроса в 1917 году (Вестник МГЛУ. Общественные науки, вып. 2 (843), 2021) | С. Н. Артёмов, Л. В. Артёмова | 1 | 53.5 | ✅ 可读全文 |
| 53 | `perrie_1972_peasant_movement_1905_1907` | `A` | `en` | The Russian Peasant Movement of 1905-1907: Its Social Composition and Revolutionary Significance (Past & Present, 57, 1972) | Maureen Perrie | 34 | 98.3 | ✅ 可读全文 |
| 54 | `pipes_1964_narodnichestvo_semantic_inquiry` | `A` | `en` | Narodnichestvo: A Semantic Inquiry (Slavic Review, 23:3, 1964) | Richard Pipes | 19 | 60.3 | ✅ 可读全文 |
| 55 | `plaggenborg_1990_who_paid_industrialisation_tsarist_russia` | `A` | `en` | Who Paid for the Industrialisation of Tsarist Russia? (Revolutionary Russia, 3:2, 1990) | Stefan Plaggenborg | 2 | 78.0 | ✅ 可读全文 |
| 56 | `plaggenborg_1995_tax_policy_peasant_poverty_1881_1905` | `A` | `en` | Tax Policy and the Question of Peasant Poverty in Tsarist Russia, 1881–1905 (Cahiers du Monde russe, 36:1–2, 1995) | Stefan Plaggenborg | 18 | 70.8 | ✅ 可读全文 |
| 57 | `priestland_1997_bolshevik_ideology_party_state_relations` | `A` | `en` | Bolshevik Ideology and the Debate Over Party-State Relations, 1918–21 (Revolutionary Russia, 10:2, 1997) | David Priestland | 2 | 72.3 | ✅ 可读全文 |
| 58 | `rieber_2001_stalin_man_of_the_borderlands` | `A` | `en` | Stalin, Man of the Borderlands (American Historical Review, 106:5, 2001) | Alfred J. Rieber | 41 | 168.2 | ✅ 可读全文 |
| 59 | `rigby_1988_origins_of_nomenklatura_system` | `A` | `en` | Staffing USSR Incorporated: The Origins of the Nomenklatura System (Soviet Studies, 40:4, 1988) | Rigby, T. H. | 1 | 56.5 | ✅ 可读全文 |
| 60 | `right_deviation_1928_krokodil` | `A` | `ru` | Борьба с «правым уклоном» в 1928 г. и сатирический журнал «Крокодил» (Россия и современный мир, № 1, 2022) | А. Л. Юрганов | 4 | 90.5 | ✅ 可读全文 |
| 61 | `rosenberg_1985_labor_bolshevik_power_after_october` | `A` | `en` | Russian Labor and Bolshevik Power after October (Slavic Review, 44:2, 1985) | William G. Rosenberg | 26 | 113.2 | ✅ 可读全文 |
| 62 | `roslof_1996_heresy_of_bolshevik_christianity_nep` | `A` | `en` | The Heresy of "Bolshevik" Christianity: Orthodox Rejection of Religious Reform during NEP (Slavic Review, 55:3, 1996) | Edward E. Roslof | 22 | 78.8 | ✅ 可读全文 |
| 63 | `rynkov_1918_komuch_social_policy` | `A` | `ru` | Путь в никуда: социальная политика Комитета членов Всероссийского учредительного собрания (июнь — ноябрь 1918 г.) (Новейшая история России, 9:1, 2019) | В. М. Рынков | 1 | 126.4 | ✅ 可读全文 |
| 64 | `sanborn_2000_mobilization_of_1914_russian_nation` | `A` | `en` | The Mobilization of 1914 and the Question of the Russian Nation: A Reexamination (Slavic Review, 59:2, 2000) | Josh Sanborn | 24 | 86.8 | ✅ 可读全文 |
| 65 | `senin_vikzhel_vikzhedor_1917_1918` | `A` | `ru` | Борьба за власть на российских железных дорогах: Викжель, Викжедор, Всопрофжель… (1917–1918 гг.) (Новый исторический вестник, вып. 13, 2005) | А. С. Сенин | 2 | 185.9 | ✅ 可读全文 |
| 66 | `seregny_1988_peasant_unions_1905` | `A` | `en` | A Different Type of Peasant Movement: The Peasant Unions in the Russian Revolution of 1905 (Slavic Review, 47:1, 1988) | Scott J. Seregny | 18 | 72.4 | ✅ 可读全文 |
| 67 | `shanin_1981_marx_peasant_commune` | `A` | `en` | Marx, Marxism and the Agrarian Question: I Marx and the Peasant Commune (History Workshop Journal, 12, 1981) | Teodor Shanin | 1 | 80.5 | ✅ 可读全文 |
| 68 | `slezkine_1994_ussr_as_communal_apartment` | `A` | `en` | The USSR as a Communal Apartment, or How a Socialist State Promoted Ethnic Particularism (Slavic Review, 53:2, 1994) | Yuri Slezkine | 40 | 138.3 | ✅ 可读全文 |
| 69 | `smith_1998_georgian_affair_of_1922` | `A` | `en` | The Georgian affair of 1922—Policy failure, personality clash or power struggle? (Europe-Asia Studies, 50:3, 1998) | Jeremy Smith | 2 | 95.3 | ✅ 可读全文 |
| 70 | `stalin_vs_bukharin_rykov_nep_debate_zh` | `A` | `zh` | 废除还是坚持新经济政策——斯大林同以布哈林、李可夫为首的“右派”的争论（《俄罗斯东欧中亚研究》2013年第2期） | 陈爱茹 | 1 | 45.2 | ✅ 可读全文 |
| 71 | `stefanenko_2020_leningrad_opposition_1926_1928` | `A` | `ru` | Внутрипартийная борьба в Ленинградской организации ВКП(б) (1926–1928 гг.): структура и практики деятельности оппозиционных групп (Петербургский исторический журнал, № 4, 2020) | А. Ю. Стефаненко | 1 | 74.3 | ✅ 可读全文 |
| 72 | `ufa_state_conference_1918` | `A` | `ru` | Уфимское государственное совещание 1918 года (Вестник Башкирского университета, 17:1(I), 2012) | Р. О. Багаутдинов | 1 | 26.8 | ✅ 可读全文 |
| 73 | `weissman_1986_prohibition_alcohol_control_1920s_nep` | `A` | `en` | Prohibition and Alcohol Control in the USSR: The 1920s Campaign against Illegal Spirits (Soviet Studies, 38:3, 1986) | Weissman, Neil | 1 | 71.2 | ✅ 可读全文 |
| 74 | `west_siberia_grain_to_peasant_revolt` | `A` | `ru` | «…В хлебном районе Западной Сибири»: от пролетарской революции к крестьянскому мятежу (Вестник Томского государственного университета. История, № 4(16), 2011) | В. А. Логачев | 1 | 84.9 | ✅ 可读全文 |
| 75 | `wheatcroft_1974_reliability_prewar_grain_statistics` | `A` | `en` | The Reliability of Russian Prewar Grain Output Statistics (Soviet Studies, 26:2, 1974) | S. G. Wheatcroft | 2 | 77.1 | ✅ 可读全文 |
| 76 | `wheatcroft_davies_cooper_1986_soviet_industrialization_reconsidered` | `A` | `en` | Soviet Industrialization Reconsidered: Some Preliminary Conclusions about Economic Development between 1926 and 1941 (Economic History Review, 39:2, 1986) | S. G. Wheatcroft, R. W. Davies, and J. M. Cooper | 2 | 112.2 | ✅ 可读全文 |
| 77 | `wildman_1970_february_revolution_russian_army` | `A` | `en` | The February Revolution in the Russian Army (Soviet Studies, 22:1, 1970) | Allan Wildman | 22 | 75.1 | ✅ 可读全文 |
| 78 | `yaney_1964_stolypin_land_reform` | `A` | `en` | The Concept of the Stolypin Land Reform (Slavic Review, 23:2, 1964) | George L. Yaney | 20 | 71.7 | ✅ 可读全文 |
| 79 | `yurev_1917_bolshevik_split_sovnarkom` | `A` | `ru` | Раскол в рядах большевиков и завершение формирования первого советского правительства (начало ноября – декабрь 1917 года) (Вестник МГПУ. Серия «Исторические науки», 2018) | А. И. Юрьев | 1 | 33.5 | ✅ 可读全文 |

## 四、多语种在线历史原典与学术专栏归档 (`sources/web-archive/`)

| 序号 | 专题子目录 | 篇数 | 文本体积 (KB) | 覆盖范围说明 |
| ---: | :--- | ---: | ---: | :--- |
| 1 | `E01_E10_supplements` | 4 | 314.8 | 专题在线文献归档 |
| 2 | `E01_narodniks` | 6 | 93.8 | 专题在线文献归档 |
| 3 | `E02_E07_foundational_docs` | 5 | 74.0 | 专题在线文献归档 |
| 4 | `E02_E10_core_classics` | 4 | 835.3 | 专题在线文献归档 |
| 5 | `E03_E08_party_and_state_docs` | 4 | 80.1 | 专题在线文献归档 |
| 6 | `E06_E09_state_and_comintern` | 4 | 283.3 | 专题在线文献归档 |
| 7 | `E06_E10_turning_points` | 5 | 106.7 | 专题在线文献归档 |
| 8 | `E09_E10_party_debates` | 4 | 638.5 | 专题在线文献归档 |
| 9 | `W32_milestone_docs` | 8 | 1843.9 | 专题在线文献归档 |
| 10 | `W39_lenin_1922_1923_docs` | 5 | 353.7 | 专题在线文献归档 |
| 11 | `W62B_mia_chinese_corpus` | 21 | 1873.3 | 中文马克思主义文库（列宁、托洛茨基、卢森堡、斯大林、布哈林、普列汉诺夫全文 21 篇） |
| 12 | `W62B_mia_intra_party_oppositions` | 20 | 1039.0 | 布尔什维克党内争论与反对派原典 1918–1929（左共、工反、四十六人、联合反对派、布哈林、拉科夫斯基 20 篇） |
| 13 | `W62B_mia_nonbolshevik_socialists` | 20 | 1382.1 | 非布尔什维克社会主义谱系原典（民粹派、孟什维克、社会革命党、无政府主义与马赫诺 20 篇） |
| 14 | `W62B_reviews_and_zh_ru_web_essays` | 20 | 824.4 | H-Russia / H-Diplo 权威书评圆桌与中俄具名史家公开学术长文（20 篇） |
| 15 | `W62B_russian_web_archives` | 17 | 653.1 | 俄文开放数字档案（1861 诏书、1906 基本法、斯托雷平敕令、1918 宪法、喀琅施塔得、十大秘密第7条等 17 篇） |
| 16 | `W62B_scholarly_blogs_and_debates` | 20 | 575.8 | 英语史学界专题研究博客与深度访谈（John Riddell, Lars Lih 等 20 篇） |
| 17 | `W62C_comintern_and_foreign_eyewitnesses` | 22 | 1019.7 | 共产国际一至六大/十次全会提纲与在俄外国亲历者经典（兰塞姆、里德、谢尔日、蔡特金等 22 篇） |
| 18 | `W62C_culture_women_law_everyday_docs` | 18 | 646.6 | 苏俄法学（帕舒卡尼斯/斯图奇卡）、妇女解放（柯伦泰/1918法典/1920流产令）、日常生活与无产阶级文化（18 篇） |
