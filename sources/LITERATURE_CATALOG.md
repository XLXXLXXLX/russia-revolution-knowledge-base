# 俄国革命知识库（1860s–1929）馆藏文献总目 (`sources/LITERATURE_CATALOG.md`)

- **馆藏拆解目录总数**: `182` 部（`sources/primary/` 一手档案原典 `15` 部 + `sources/monographs/` 学术专著/回忆录 `167` 部）
- **嵌入式文本状态**: `✅ 可读全文 166 部` | `⚠️ 纯扫描/残卷自动隔离 (needs_ocr: true) 16 部`
- **支持格式**: `PDF`（PyMuPDF 页码锚点）、`EPUB`（自动合并逐页 XML 切片）、`DOCX`、`DjVu`（原生纯 Python `ZPCodec + BZZ` 提取 `TXTz` 俄文文本层）
- **检索协议**: 主控官通过 `python scripts/kb.py locate-chapters "<关键词>"` 毫秒级定位章节（自动隔离 `needs_ocr: true` 目录），再交 `close-reader` 整章顺读。

## 一、一手档案、会议速记与历史原典 (`sources/primary/`)

| 序号 | 目录 Slug | 信源等级 | 语种 | 题名 / 原始文件 | 编者/作者 | 章节数 | 文本体积 (KB) | 状态 |
| ---: | :--- | :---: | :---: | :--- | :--- | ---: | ---: | :--- |
| 1 | `bonnell_1983_russian_worker_memoirs` | `B` | `en` | The Russian Worker Life and Labor Under the Tsarist Regime (Victoria E. Bonnell (editor)) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 8 | 487.2 | ✅ 可读全文 |
| 2 | `bukharin_preobrazhensky_1919_abc_communism_zh` | `S` | `zh` | 共产主义ABC (Азбука коммунизма) | 尼·布哈林、叶·普列奥布拉任斯基 | 5 | 602.0 | ✅ 可读全文 |
| 3 | `cheka_red_terror_chronicle_zh` | `S` | `zh` | 全俄肃反委员会红色恐怖纪事革命的惩戒之剑 Хроника красного террора ВЧК. Карающий меч революции (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).epub | - | 72 | 440.0 | ✅ 可读全文 |
| 4 | `kak_lomali_nep_1928_v3_ru` | `S` | `ru` | Как ломали НЭП. Стенограммы пленумов ЦК ВКП(б) 1928–1929 гг. Том 3: Ноябрьский пленум 1928 г. | В. П. Данилов, О. В. Хлевнюк, А. Ю. Ватлин (сост.) | 26 | 3798.9 | ✅ 可读全文 |
| 5 | `kakurin_1928_red_army_civil_war` | `S` | `en` | The Russian Civil War, 1918_ (Z-Library).pdf | - | 32 | 1878.0 | ✅ 可读全文 |
| 6 | `kollontai_1921_workers_opposition` | `S` | `en` | The Workers' Opposition | Alexandra Kollontai | 2 | 115.5 | ✅ 可读全文 |
| 7 | `martov_zinoviev_1920_halle` | `S` | `en` | Martov and Zinoviev _ head to head in Halle -- Martov, L_;Zinovyev, Grigory Yevseyevich;Lewis, Ben;Lih, -- 1st ed, London, 2011 -- November -- 9781447809111 -- ccae95a16ee8482b139566b9aa8c77d0 -- Anna’s Archive.pdf | - | 10 | 655.1 | ✅ 可读全文 |
| 8 | `nationalization_docs_1917_1920_zh` | `S` | `en` | nationalization_docs_1917_1920_zh | - | 29 | 88.4 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 9 | `preobrazhensky_1926_new_economics_zh` | `S` | `zh` | 新经济学：对苏维埃经济进行理论分析的尝试 | Yevgeni Preobrazhensky (叶·普列奥布拉任斯基) | 19 | 33.8 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 10 | `short_course_1938_zh` | `S` | `zh` | 联共（布）党史简明教程（文字层补齐版） | 联共（布）中央特设委员会 | 30 | 1007.5 | ✅ 可读全文 |
| 11 | `socialism_in_one_country_debate_docs_zh` | `S` | `zh` | 革命何以关于一国建成社会主义的讨论 (Zerklora、红锲社、Levski、青山霁、Nekoist 等 编者 郑阑干) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 18 | 386.4 | ✅ 可读全文 |
| 12 | `stalin_major_documents_zh` | `S` | `zh` | 斯大林1878-1953(主要文献) (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 16 | 475.3 | ✅ 可读全文 |
| 13 | `stalin_works_v1_1901_1907_zh` | `S` | `zh` | 斯大林全集 第一卷（1901—1907） | 约·维·斯大林 | 41 | 1443.8 | ✅ 可读全文 |
| 14 | `tragedy_soviet_village_v2_1929_zh` | `S` | `zh` | 苏联农村的悲剧 集体化与消灭富农 文献和材料 第2卷 1929年11月 — 1930年12月 Трагедия_советской_деревни_Том_2 (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 54 | 2513.7 | ✅ 可读全文 |
| 15 | `trotsky_1905_zh` | `B` | `zh` | 1905 | 列夫·达维多维奇·托洛茨基 | 22 | 892.9 | ✅ 可读全文 |

## 二、学术专著与重要亲历者文献 (`sources/monographs/`)

| 序号 | 目录 Slug | 信源等级 | 语种 | 题名 / 原始文件 | 作者 | 章节数 | 文本体积 (KB) | 状态 |
| ---: | :--- | :---: | :---: | :--- | :--- | ---: | ---: | :--- |
| 1 | `allen_2003_farm_to_factory` | `A` | `en` | Farm to Factory: A Reinterpretation of the Soviet Industrial Revolution | Robert C. Allen | 13 | 753.0 | ✅ 可读全文 |
| 2 | `apalkov_intra_party_struggle_zh` | `A` | `zh` | 联共（布）党内斗争：从“集体领导”到斯大林个人统治 | Dmitrii I. Apalkov (德·伊·阿帕利科夫) | 12 | 355.3 | ✅ 可读全文 |
| 3 | `ascher_1988_revolution_of_1905_v1` | `A` | `en` | The Revolution of 1905: Russia in Disarray (Vol. 1) | Abraham Ascher | 9 | 64.4 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 4 | `ascher_2001_stolypin` | `A` | `en` | P. A. Stolypin: The Search for Stability in Late Imperial Russia | Abraham Ascher | 26 | 1304.2 | ✅ 可读全文 |
| 5 | `avrich_1970_kronstadt` | `A` | `en` | Kronstadt, 1921 | Paul Avrich | 12 | 545.0 | ✅ 可读全文 |
| 6 | `ball_1987_nepmen_zh` | `A` | `zh` | 俄国最后的资本家：新经济政策时期的新商人（1921-1929） | Alan M. Ball | 20 | 620.6 | ✅ 可读全文 |
| 7 | `basil_1984_mensheviks_1917` | `A` | `en` | The Mensheviks In The Revolution Of 1917 (John D. Basil) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 14 | 571.9 | ✅ 可读全文 |
| 8 | `blanc_2021_rev_sd` | `A` | `en` | 革命社会民主党：俄罗斯帝国全境的工人阶级政治（1882–1917） | 埃里克·布兰克 | 20 | 1243.5 | ✅ 可读全文 |
| 9 | `boll_1979_red_guards` | `A` | `en` | The Petrograd armed workers movement in the February Revolution (February-July, 1917)  a study in the radicalization of the… (Boll, Michael M., 1938-) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 8 | 517.6 | ✅ 可读全文 |
| 10 | `bonnell_1983_roots_of_rebellion_zh` | `A` | `zh` | 俄国工人运动和组织的根源 (Roots of Rebellion, 1900-1914) | Victoria E. Bonnell | 20 | 1094.0 | ✅ 可读全文 |
| 11 | `bonnell_1983_roots_rebellion` | `A` | `en` | 反叛的根源：圣彼得堡与莫斯科的工人政治与组织（1900–1914） | 维多利亚·E·邦内尔 | 32 | 66.9 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 12 | `bukharin_preobrazhensky_debate_zh` | `A` | `zh` | 平衡与非平衡：布哈林与普列奥布拉仁斯基之争 | 中文研究论文 | 1 | 37.1 | ✅ 可读全文 |
| 13 | `burds_1998_peasant_dreams` | `A` | `en` | Peasant Dreams and Market Politics: Labor Migration and the Russian Village, 1861–1905 | Jeffrey Burds | 13 | 834.0 | ✅ 可读全文 |
| 14 | `cao_weian_new_russian_history_zh` | `A` | `zh` | 俄国史新论：从基辅罗斯、莫斯科罗斯到彼得堡罗斯 | 曹维安 | 307 | 83.7 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 15 | `carr_1950_bolshevik_rev_v1_en` | `A` | `en` | The Bolshevik Revolution, 1917-1923, Vol. 1.pdf | - | 18 | 1113.4 | ✅ 可读全文 |
| 16 | `carr_1952_bolshevik_rev_v2_en` | `A` | `en` | The Bolshevik Revolution, 1917–1923, Vol. 2 (The Economic Order) | Edward Hallett Carr | 17 | 1028.7 | ✅ 可读全文 |
| 17 | `carr_1953_bolshevik_rev_v3_en` | `A` | `en` | The Bolshevik Revolution, 1917–1923, Vol. 3 (Soviet Russia and the World) | Edward Hallett Carr | 26 | 1611.8 | ✅ 可读全文 |
| 18 | `carr_1954_interregnum` | `A` | `en` | A History of Soviet Russia: The Interregnum, 1923-1924 | Edward Hallett Carr | 417 | 2134.3 | ✅ 可读全文 |
| 19 | `carr_1976_foundations_v3p2` | `A` | `en` | Foundations of a Planned Economy 1926–1929 Volume Three - II (Edward Hallett Carr (auth.)) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 12 | 859.4 | ✅ 可读全文 |
| 20 | `carr_1979_lenin_to_stalin` | `A` | `en` | The Russian Revolution From Lenin to Stalin (Edward Hallett Carr) (Z-Library).pdf | - | 9 | 448.0 | ✅ 可读全文 |
| 21 | `carr_bolshevik_rev_v1_zh` | `A` | `zh` | 苏维埃俄国史——布尔什维克革命（1917-1923）第一卷 (E. H. Carr) (Z-Library).pdf | - | 13 | 923.2 | ✅ 可读全文 |
| 22 | `carr_bolshevik_rev_v2_zh` | `A` | `zh` | 苏维埃俄国史——布尔什维克革命（1917-1923）第二卷 (E. H. Carr) (Z-Library).pdf | - | 11 | 811.4 | ✅ 可读全文 |
| 23 | `carr_bolshevik_rev_v3_zh` | `A` | `zh` | 苏维埃俄国史——布尔什维克革命(1917-1923)第三卷 (E. H. Carr) (Z-Library).pdf | - | 13 | 1143.7 | ✅ 可读全文 |
| 24 | `carr_davies_1969_foundations_v1p1` | `A` | `en` | Foundations of a Planned Economy, 1926-1929, Volume One, Part I | E. H. Carr & R. W. Davies | 16 | 1193.2 | ✅ 可读全文 |
| 25 | `central_asia_nomads_zh` | `A` | `zh` | 游牧民族与苏联统治：列宁和斯大林统治下的中亚.pdf | - | 22 | 679.8 | ✅ 可读全文 |
| 26 | `class_formation_comparative_2008` | `A` | `en` | Class Formation, Civil Society and the State: A Comparative Analysis of Russia, France, the US and England | 未核定（详见书名页） | 25 | 1459.5 | ✅ 可读全文 |
| 27 | `cohen_1973_bukharin` | `A` | `en` | 布哈林与布尔什维克革命：政治传记（1888–1938） | 斯蒂芬·F·科恩 | 22 | 1464.6 | ✅ 可读全文 |
| 28 | `cole_socialist_thought_v3p1_zh` | `B` | `zh` | 社会主义思想史 第三卷上：第二国际 1889–1914 | G. D. H. Cole | 22 | 56.6 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 29 | `cole_socialist_thought_v3p2_zh` | `A` | `zh` | 社会主义思想史 第三卷下 第二国际 1889-1914 | G. D. H. Cole | 28 | 72.6 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 30 | `cole_socialist_thought_v4p1_zh` | `A` | `zh` | 社会主义思想史 第四卷上 共产主义与社会民主主义 1914-1931 | G. D. H. Cole | 36 | 92.6 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 31 | `cole_socialist_thought_v4p2_zh` | `A` | `zh` | 社会主义思想史 第四卷下 共产主义与社会民主主义 1914-1931 | G. D. H. Cole | 15 | 44.3 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 32 | `cooper_perrie_1995_davies_festschrift_zh` | `A` | `zh` | 苏联历史 1917-53纪念 R.W. 戴维斯的论文集 Soviet History 1917-53 Essays in Honour of R. W. Davies (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 16 | 660.7 | ✅ 可读全文 |
| 33 | `corney_2004_telling_october` | `A` | `en` | Telling October: Memory and the Making of the Bolshevik Revolution | Frederick C. Corney | 0 | 0.0 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 34 | `daniels_1960_conscience` | `A` | `en` | The Conscience of the Revolution: Communist Opposition in Soviet Russia | Robert Vincent Daniels | 23 | 1603.2 | ✅ 可读全文 |
| 35 | `david_fox_1997_revolution_of_the_mind` | `A` | `en` | Revolution of the Mind: Higher Learning among the Bolsheviks, 1918–1929 | Michael David-Fox | 0 | 0.0 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 36 | `davies_1980_collective_farm_zh` | `A` | `zh` | 苏维埃俄国的工业化 2 苏联集体农庄,1929-1930The Industrialisation of Soviet Russia 2 THE SOVIET COLLECTIVE FARM, 1929-1930 (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 17 | 428.3 | ✅ 可读全文 |
| 37 | `davies_industrialisation_en` | `A` | `en` | The Industrialisation of Soviet Russia.epub | - | 508 | 1237.8 | ✅ 可读全文 |
| 38 | `deutscher_prophet_trilogy_zh` | `B` | `zh` | 先知三部曲：武装的先知；被解除武装的先知；流亡的先知 | 伊萨克·多伊彻 | 41 | 3523.3 | ✅ 可读全文 |
| 39 | `douds_2018_inside_lenins_government` | `A` | `en` | Inside Lenin's Government: Ideology, Power and Practice in the Early Soviet State | Lara Douds | 18 | 608.8 | ✅ 可读全文 |
| 40 | `emmons_1968_russian_landed_gentry_1861` | `A` | `en` | The Russian Landed Gentry and the Peasant Emancipation of 1861 | Terence Emmons | 21 | 1202.4 | ✅ 可读全文 |
| 41 | `erlich_1960_industrialization` | `A` | `en` | 苏联工业化争论（1924–1928） | 亚历山大·埃尔利赫 | 16 | 464.1 | ✅ 可读全文 |
| 42 | `figes_1996_peoples_tragedy` | `A` | `en` | A People's Tragedy: The Russian Revolution 1891-1924 | Orlando Figes | 32 | 2717.9 | ✅ 可读全文 |
| 43 | `filtzer_1986_soviet_workers` | `A` | `en` | Soviet Workers and Stalinist Industrialisation. The Formation of Modern Soviet Production Relations, 1928-1941 (Donald Filtzer) (Z-Library).pdf | - | 14 | 869.2 | ✅ 可读全文 |
| 44 | `fitzpatrick_1978_cultural_rev_zh` | `A` | `zh` | 俄国文化革命(1928-1931)The Russian Cultural Revolution (1928-1931) (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 17 | 684.7 | ✅ 可读全文 |
| 45 | `fitzpatrick_1979_education_mobility` | `A` | `en` | Education and Social Mobility in the Soviet Union 1921-1934.pdf | - | 13 | 911.7 | ✅ 可读全文 |
| 46 | `fitzpatrick_1991_russia_era_nep` | `A` | `en` | Russia in the Era of NEP Explorations in Soviet Society and Culture.pdf | - | 21 | 1047.1 | ✅ 可读全文 |
| 47 | `foglesong_1995_secret_war_zh` | `A` | `zh` | 美国对抗布尔什维克主义的秘密战争 1917—1920 年美国对俄国内战的干涉 (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 18 | 1040.3 | ✅ 可读全文 |
| 48 | `french_and_russian_rev_analogies` | `A` | `en` | The French Revolution and the Russian Revolution- Some Suggestive Analogies.pdf | - | 14 | 35.5 | ✅ 可读全文 |
| 49 | `frenchmen_rev_heritage_russia` | `A` | `en` | Frenchmen, Their Revolutionary Heritage, and the Russian Revolution .pdf | - | 20 | 64.5 | ✅ 可读全文 |
| 50 | `gaida_2003_liberal_opposition_zh` | `A` | `zh` | 走向权力之路的自由主义反对派(1914 年 —1917 年春) (Ф.А.盖达著 列宁格勒档案馆译) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 23 | 998.0 | ✅ 可读全文 |
| 51 | `galili_1989_menshevik_leaders` | `A` | `en` | 俄国革命中的孟什维克领袖：社会现实与政治策略 | 齐娃·加利利 | 20 | 1260.6 | ✅ 可读全文 |
| 52 | `getzler_1967_martov` | `A` | `en` | Martov: A Political Biography of a Russian Social Democrat | Israel Getzler | 11 | 846.5 | ✅ 可读全文 |
| 53 | `goldman_1993_women_state_rev_zh` | `A` | `zh` | 妇女、国家与革命苏联家庭政策和社会生活 1917~1936=Women, the State and Revolution Soviet Family Policy and Social Life, 1917–1936 (温迪·Z·戈德曼Wendy Z. Goldman 著 红... (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 13 | 711.9 | ✅ 可读全文 |
| 54 | `goldman_inventing_enemy_zh` | `A` | `zh` | 《发明敌人：斯大林时代苏联的告密与恐怖》温迪-戈德曼.pdf | - | 19 | 643.9 | ✅ 可读全文 |
| 55 | `grant_2022_soviet_nightingales` | `A` | `en` | Soviet Nightingales: Care under Communism | Susan Grant | 22 | 919.6 | ✅ 可读全文 |
| 56 | `haimson_1955_origins` | `A` | `en` | The Russian Marxists and the Origins of Bolshevism | Leopold H. Haimson | 11 | 701.2 | ✅ 可读全文 |
| 57 | `haimson_1987_three_revolutionaries` | `A` | `en` | The Making Of Three Russian Revolutionaries_  Voices From -- Haimson, Leopold H_ (author) -- 1988 feb 26 -- Cambridge University Press Éditions de la -- 9780511665165 -- 05ad0816038f805dd9704d22b2a1b207 -- Anna’s Arc.pdf | - | 25 | 1701.1 | ✅ 可读全文 |
| 58 | `haimson_2005_experience` | `A` | `en` | Russia's Revolutionary Experience, 1905-1917: Two Essays | Leopold H. Haimson | 19 | 768.3 | ✅ 可读全文 |
| 59 | `hasegawa_february_1917` | `A` | `en` | The February Revolution, Petrograd, 1917: The End of the Tsarist Regime and the Birth of Dual Power | Tsuyoshi Hasegawa (长谷川毅) | 44 | 1878.1 | ✅ 可读全文 |
| 60 | `heywood_1999_modernising_lenins_russia` | `A` | `en` | Modernising Lenin's Russia: Economic Reconstruction, Foreign Trade and the Railways, 1917–1924 | Anthony Heywood | 21 | 768.9 | ✅ 可读全文 |
| 61 | `hildermeier_psr` | `A` | `en` | The Russian Socialist Revolutionary Party Before the First World War | Manfred Hildermeier | 31 | 1121.8 | ✅ 可读全文 |
| 62 | `hirsch_2005_empire_of_nations_zh` | `A` | `zh` | 民族帝国：民族志知识与苏联的形成 (Empire of Nations) | Francine Hirsch (弗朗辛·赫希) | 14 | 2204.3 | ✅ 可读全文 |
| 63 | `hobsbawm_1959_primitive_rebels_zh` | `A` | `zh` | 原始的叛乱  十九至二十世纪社会运动的古朴形式 = Primitive Rebels Studies in Archaic Forms of Social Movement in the 19th and 20th Centuries ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).epub | - | 40 | 537.6 | ✅ 可读全文 |
| 64 | `hoffmann_2011_cultivating_masses_zh` | `A` | `zh` | 培养群众 现代国家实践与苏联社会主义,1914-1939 CULTIVATINGTHE MASSES Modern State Practices andSoviet Socialism, 1914–1939 (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 15 | 741.6 | ✅ 可读全文 |
| 65 | `ilyukhov_bolshevik_pay_zh` | `A` | `zh` | 布尔什维克如何发薪 (亚历山大·伊利尤霍夫 著 红锲社 译) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 26 | 895.4 | ✅ 可读全文 |
| 66 | `jacobin_ancestry_soviet_communism` | `A` | `en` | The Jacobin Ancestry of Soviet Communism.pdf | - | 8 | 17.6 | ✅ 可读全文 |
| 67 | `katasonov_stalin_economy_zh` | `A` | `zh` | 斯大林的经济 ([俄]卡塔索诺夫) (Z-Library).pdf | - | 92 | 571.2 | ✅ 可读全文 |
| 68 | `khalid_2015_making_uzbekistan_zh` | `A` | `zh` | 制造乌兹别克斯坦：民族、帝国和革命 (Making Uzbekistan) | Adeeb Khalid (阿迪卜·哈立德) | 23 | 1237.9 | ✅ 可读全文 |
| 69 | `khlevniuk_2015_stalin` | `A` | `en` | Stalin: New Biography of a Dictator | Oleg V. Khlevniuk | 21 | 1091.8 | ✅ 可读全文 |
| 70 | `klots_domestic_service_ussr_zh` | `A` | `zh` | 苏联的家政服务：妇女解放与性别化的劳动等级制度 (Domestic Service in the Soviet Union) | Alissa Klots | 12 | 715.1 | ✅ 可读全文 |
| 71 | `koenker_1981_moscow_workers_zh` | `A` | `zh` | 莫斯科工人和1917年革命.pdf | - | 15 | 1052.8 | ✅ 可读全文 |
| 72 | `kotkin_2014_stalin_v1` | `A` | `en` | Stalin, Volume I: Paradoxes of Power, 1878-1928 | Stephen Kotkin | 69 | 3382.5 | ✅ 可读全文 |
| 73 | `kotkin_2017_stalin_v2` | `A` | `en` | Stalin: Waiting for Hitler, 1929–1941 (Vol. 2) | Stephen Kotkin | 72 | 4776.2 | ✅ 可读全文 |
| 74 | `lebsky_working_class_paternalism_zh` | `A` | `zh` | 苏联的工人阶级：工业家长制下的生活（中译本） (Максим Лебский) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 14 | 320.8 | ✅ 可读全文 |
| 75 | `leggett_1981_cheka` | `A` | `en` | 契卡：列宁的政治警察——全俄肃清反革命及怠工非常委员会（1917年12月至1922年2月） | 乔治·莱格特 | 19 | 1494.8 | ✅ 可读全文 |
| 76 | `lelichuk_soviet_industrialization_zh` | `A` | `zh` | 苏联工业化 | V. S. Lelchuk | 16 | 41.2 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 77 | `lenin_how_became_leader_zh` | `A` | `zh` | 弗拉基米尔·列宁：如何成为领袖（中译本）.pdf | - | 28 | 1035.2 | ✅ 可读全文 |
| 78 | `levy_1987_socialism_intelligentsia` | `A` | `en` | Socialism-and-the-intelligentsia-1880-1914-Carl-Levy.pdf | - | 20 | 756.1 | ✅ 可读全文 |
| 79 | `lewin_1968_lenins_last_struggle` | `A` | `en` | Lenin's Last Struggle | Moshe Lewin | 22 | 335.8 | ✅ 可读全文 |
| 80 | `lewin_1968_peasants` | `A` | `en` | 俄国农民与苏维埃政权：农业集体化研究 | 莫希·莱文 | 23 | 1438.3 | ✅ 可读全文 |
| 81 | `liber_1992_soviet_ukraine_zh` | `A` | `zh` | 乌克兰苏维埃的苏维埃民族政策、城市发展与身份变迁 1923—1934 (乔治·O·利伯 著 红锲社 译) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 16 | 502.7 | ✅ 可读全文 |
| 82 | `liebich_1997_from_the_other_shore` | `A` | `en` | From the Other Shore: Russian Social Democracy after 1921 | André Liebich | 28 | 1345.7 | ✅ 可读全文 |
| 83 | `lih_2006_lenin_rediscovered` | `A` | `en` | Lenin Rediscovered: What Is to Be Done? in Context | Lars T. Lih | 28 | 2149.6 | ✅ 可读全文 |
| 84 | `lih_2006_lenin_rediscovered_zh` | `A` | `zh` | 列宁再发现：在此背景下《怎么办？》 | Lars T. Lih (拉尔斯·T·利赫) | 14 | 993.5 | ✅ 可读全文 |
| 85 | `loginov_lenin_bio_zh` | `A` | `zh` | 列宁全传 (弗拉德连·洛吉诺夫) (z-library.sk, 1lib.sk, z-lib.sk).epub | - | 10 | 2208.7 | ✅ 可读全文 |
| 86 | `loginov_lenin_in_1917_zh` | `A` | `zh` | 列宁在1917年：面对稍纵即逝的契机 (В.Т.洛吉诺夫（В.Т.Логинов）) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 35 | 1476.6 | ✅ 可读全文 |
| 87 | `making_soviet_citizen_education_zh` | `A` | `zh` | 苏维埃公民的塑造 苏维埃教育中的品格塑造与公民训练 The Making of the Soviet Citizen Character Formation and Civic Training in Soviet Education (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 7 | 490.5 | ✅ 可读全文 |
| 88 | `manning_1982_crisis_old_order_zh` | `A` | `zh` | 俄国旧秩序的危机 绅士与政府 The Crisis of the Old Order in Russia_ Gentry and Government (罗伯塔·汤普森 曼宁) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 41 | 1484.7 | ✅ 可读全文 |
| 89 | `martin_2001_affirmative_action_empire` | `A` | `en` | The Affirmative Action Empire: Nations and Nationalism in the Soviet Union, 1923–1939 | Terry Martin | 22 | 1413.9 | ✅ 可读全文 |
| 90 | `mawdsley_1987_civil_war` | `A` | `en` | The Russian Civil War | Evan Mawdsley | 33 | 941.8 | ✅ 可读全文 |
| 91 | `mawdsley_1987_civil_war_zh` | `A` | `zh` | 俄国内战 Evan Mawdsley (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 22 | 1438.4 | ✅ 可读全文 |
| 92 | `mayer_1999_lenin_jacobin` | `A` | `en` | Lenin and the Jacobin Identity in Russia.pdf | - | 29 | 78.4 | ✅ 可读全文 |
| 93 | `mckean_1990_st_petersburg_between_revolutions` | `A` | `en` | St. Petersburg Between the Revolutions: Workers and Revolutionaries, June 1907–February 1917 | Robert B. McKean | 26 | 1817.0 | ✅ 可读全文 |
| 94 | `merridale_1990_moscow_politics_zh` | `A` | `zh` | 莫斯科政治与斯大林崛起：首都的共产党（1925-1932） | Catherine Merridale | 18 | 747.2 | ✅ 可读全文 |
| 95 | `moore_1966_social_origins_zh` | `A` | `zh` | 专制与民主的社会起源 (【美】巴林顿·摩尔) (z-library.sk, 1lib.sk, z-lib.sk).epub | - | 16 | 1233.3 | ✅ 可读全文 |
| 96 | `mozokhin_extrajudicial_powers_zh` | `A` | `zh` | 苏联国家安全机关 镇压的权利 1918年至1953年 Право на репрессии Внесудебные полномочия органов государственной безопа... (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 19 | 448.1 | ✅ 可读全文 |
| 97 | `nineteenth_c_russian_intelligentsia` | `A` | `en` | The_nineteenth_century_Russian_intellige.pdf | - | 1 | 31.6 | ✅ 可读全文 |
| 98 | `nove_1964_was_stalin_necessary` | `A` | `en` | Was Stalin Really Necessary? Some Problems of Soviet Economic Policy | Alec Nove | 21 | 731.1 | ✅ 可读全文 |
| 99 | `october_socialist_rev_zh` | `A` | `zh` | 十月社会主义革命 | - | 7 | 17.7 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 100 | `other_side_of_nep_1923_1925_zh` | `A` | `zh` | 新经济政策的另一面1923-1925年苏联的经济与政治斗争 (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 14 | 907.8 | ✅ 可读全文 |
| 101 | `pinnow_2010_lost_to_the_collective_zh` | `A` | `zh` | 集体的失落：自杀与苏联社会主义的承诺（1921—1929） | Kenneth M. Pinnow | 12 | 737.3 | ✅ 可读全文 |
| 102 | `pipes_1990_russian_rev` | `A` | `en` | The Russian Revolution | Richard Pipes | 37 | 2697.8 | ✅ 可读全文 |
| 103 | `pirani_2008_russian_revolution_in_retreat` | `A` | `en` | The Russian Revolution in Retreat, 1920–24: Soviet Workers and the New Communist Elite | Simon Pirani | 13 | 908.2 | ✅ 可读全文 |
| 104 | `plekhanov_dzerzhinsky_zh` | `A` | `zh` | 捷尔任斯基从天文学家到钢铁费利克斯 Дзержинский. От «Астронома» до «Железного Феликса» (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 19 | 1107.9 | ✅ 可读全文 |
| 105 | `priestland_2007_stalinism_mobilization_zh` | `A` | `zh` | 斯大林主义与动员政治战间俄国的思想、权力与恐怖 (大卫·普里斯特兰) (Z-Library).pdf | - | 26 | 1121.6 | ✅ 可读全文 |
| 106 | `przeworski_class_formation_zh` | `A` | `zh` | 无产阶级的阶级形成历程：从《资本论》第一卷“原始积累”到最近的一些争议 | Adam Przeworski | 3 | 177.0 | ✅ 可读全文 |
| 107 | `psr_study_1901_1925_zh` | `A` | `en` | psr_study_1901_1925_zh | - | 438 | 95.6 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 108 | `rabinowitch_1968_prelude_zh` | `A` | `zh` | 革命的前奏：彼得格勒布尔什维克与1917年七月起义 | Alexander Rabinowitch (亚历山大·拉宾诺维奇) | 13 | 563.6 | ✅ 可读全文 |
| 109 | `rabinowitch_1976_come_to_power_zh` | `A` | `zh` | 布尔什维克掌权：1917年彼得格勒革命 | Alexander Rabinowitch (亚历山大·拉宾诺维奇) | 20 | 959.9 | ✅ 可读全文 |
| 110 | `rabinowitch_2007_bolsheviks_in_power_zh` | `A` | `ru` | 布尔什维克当权：彼得格勒苏维埃时代的第一年 | 亚历山大·拉比诺维奇 | 21 | 1151.2 | ✅ 可读全文 |
| 111 | `rabinowitch_2007_in_power` | `A` | `en` | The Bolsheviks in Power: The First Year of Soviet Rule in Petrograd | Alexander Rabinowitch (亚历山大·拉宾诺维奇) | 27 | 1422.7 | ✅ 可读全文 |
| 112 | `raleigh_2001_provincial_landscapes_zh` | `A` | `zh` | 地方风貌 苏联权力的地方纬度 1917—1953 PROVINCIAL LANDSCAPES Local Dimensions of Soviet Power, 1917-1953 (唐纳德·J·罗利 编 红锲社 译) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 18 | 1059.5 | ✅ 可读全文 |
| 113 | `rees_1995_stalinism_soviet_rail_transport_zh` | `A` | `zh` | 斯大林主义与苏联铁路运输（1928–1941） | E. A. Rees | 20 | 630.2 | ✅ 可读全文 |
| 114 | `roobol_1976_tsereteli` | `A` | `en` | Tsereteli — A Democrat in the Russian Revolution A Political Biography (W. H. Roobol (auth.)) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 10 | 744.0 | ✅ 可读全文 |
| 115 | `rossman_2005_worker_resistance_under_stalin_zh` | `A` | `zh` | 斯大林治下的工人抵抗运动：阶级和革命在车间（1928—1932） | Jeffrey J. Rossman | 8 | 629.0 | ✅ 可读全文 |
| 116 | `ru_rev_state_working_class` | `A` | `en` | Революция, государство, раб_ (Z-Library).pdf | - | 15 | 2078.8 | ✅ 可读全文 |
| 117 | `sakharov_2012_crossroads` | `A` | `en` | 在十字路口：关于苏联社会发展前景与道路的讨论（1921–1929） | 瓦连京·亚历山德罗维奇·萨哈罗夫 | 22 | 595.6 | ✅ 可读全文 |
| 118 | `service_2009_russian_rev` | `A` | `en` | The Russian Revolution, 1900-1927 (rev. expanded 4th ed. 2009) (Robert Service) (Z-Library).pdf | - | 6 | 321.8 | ✅ 可读全文 |
| 119 | `service_2009_trotsky_zh` | `A` | `zh` | 罗伯特·瑟维斯 托洛茨基 一部传记 Trotsky A Biography (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).epub | - | 11 | 1416.5 | ✅ 可读全文 |
| 120 | `service_lenin_v1_zh` | `A` | `zh` | 列宁政治生涯 第一卷 矛盾的力量 (罗伯特·瑟维斯) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 18 | 592.6 | ✅ 可读全文 |
| 121 | `shlapentokh_france_russian_revs` | `A` | `en` | FRANCE AND THE RUSSIAN REVOLUTIONS THE BURDEN OF FRENCH REVOLUTIONARY HISTORY.pdf | - | 11 | 36.2 | ✅ 可读全文 |
| 122 | `siegelbaum_1992_state_and_society` | `A` | `en` | Soviet State and Society between Revolutions, 1918-1929 (Cambridge Russian Paper.pdf | - | 10 | 787.8 | ✅ 可读全文 |
| 123 | `siegelbaum_suny_1994_making_workers_soviet` | `A` | `en` | Making Workers Soviet Power, Class, and Identity (Ronald Grigor Suny Lewis H. Siegelbaum) (Z-Library).pdf | - | 19 | 1186.1 | ✅ 可读全文 |
| 124 | `siegelbaum_suny_1994_making_workers_soviet_zh` | `A` | `en` | Making Workers Soviet: Power, Class, and Identity | Lewis H. Siegelbaum、Ronald Grigor Suny（编） | 21 | 1174.4 | ✅ 可读全文 |
| 125 | `siegelbaum_suny_1994_making_workers_zh` | `A` | `zh` | 塑造苏联工人权力、阶级与身份认同 (刘易斯·H·西格尔鲍姆,罗纳德·格里戈尔·苏尼 编 红锲社 译) (Z-Library).pdf | - | 21 | 1085.4 | ✅ 可读全文 |
| 126 | `smirnov_red_army_1917_1937_zh` | `A` | `zh` | 工农红军军队建设中的致命错误 1917—1937 (A.A.斯米尔诺夫 著 红锲社 译) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 40 | 1445.1 | ✅ 可读全文 |
| 127 | `smith_1983_red_petrograd` | `A` | `en` | Red Petrograd: Revolution in the Factories, 1917-1918 | S. A. Smith | 15 | 901.8 | ✅ 可读全文 |
| 128 | `smith_jeremy_1999_national_question_zh` | `A` | `zh` | 布尔什维克与民族问题 1917—1923 (杰里米·史密斯 著 红锲社 译) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 19 | 600.8 | ✅ 可读全文 |
| 129 | `smith_sa_1983_red_petrograd_zh` | `A` | `zh` | 红色彼得格勒：工厂中的革命，1917-18.pdf | - | 15 | 719.9 | ✅ 可读全文 |
| 130 | `smith_scott_2011_captives_of_revolution` | `A` | `en` | Captives of Revolution: The Socialist Revolutionaries and the Bolshevik Dictatorship, 1918–1923 | Scott B. Smith | 19 | 1220.2 | ✅ 可读全文 |
| 131 | `smith_scott_captives_of_rev_zh` | `A` | `en` | The Sickle under the Hammer: The Russian Socialist Revolutionaries in the Early Months of Soviet Rule | Oliver Henry Radkey | 19 | 1358.8 | ✅ 可读全文 |
| 132 | `sobolev_1899_russian_tariff_policy_zh` | `A` | `zh` | 19世纪下半叶俄国的关税政策 | М. Н. Соболев (米·尼·索博列夫) | 32 | 1680.3 | ✅ 可读全文 |
| 133 | `soviet_democracy_and_stalin_zh` | `A` | `zh` | 苏联民主与斯大林 1917年至1953年苏联的理论与实践 (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 11 | 533.1 | ✅ 可读全文 |
| 134 | `soviet_far_east_forced_migration_1920s_zh` | `A` | `zh` | 20世纪20年代和50年代苏联远东地区的强制移民 | 俄罗斯远东移民史研究译著 | 21 | 2402.2 | ✅ 可读全文 |
| 135 | `soviet_women_zh` | `A` | `zh` | 苏联妇女 Soviet Women (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 19 | 645.4 | ✅ 可读全文 |
| 136 | `soviet_workers_illusions_and_reality_zh` | `A` | `en` | The Soviet Worker: Illusions and Realities | Leonard Schapiro & Joseph Godson (eds.) | 13 | 726.2 | ✅ 可读全文 |
| 137 | `soviet_working_class_industrial_paternalism_zh` | `A` | `zh` | 苏联的工人阶级：工业家长制下的生活 | Максим Лебский (Maksim Lebsky) | 14 | 320.8 | ✅ 可读全文 |
| 138 | `spitsyn_russia_ussr_v3_zh` | `A` | `zh` | 俄罗斯-苏联在1917-1945：俄罗斯历史完整教科书第三卷 (叶夫根尼·尤里耶维奇·斯皮岑) (Z-Library).pdf | - | 20 | 1329.4 | ✅ 可读全文 |
| 139 | `spitsyn_textbook_zh` | `A` | `zh` | 【昨日苏联译丛04】苏联-俄罗斯历史教程 ([俄]叶夫根尼·斯皮岑) (Z-Library).pdf | - | 21 | 1091.2 | ✅ 可读全文 |
| 140 | `stalin_and_war_1918_1953_zh` | `A` | `zh` | 斯大林与战争（1918-1953）：镇压、动员和外部威胁的模式.pdf | - | 15 | 319.9 | ✅ 可读全文 |
| 141 | `stalin_era_economy_repression_1924_1954_zh` | `B` | `zh` | 斯大林时代：经济、镇压、工业化，1924–1954 | 维克托·尼古拉耶维奇·泽姆斯科夫 | 8 | 690.5 | ✅ 可读全文 |
| 142 | `starks_2018_smoking_under_tsars_zh` | `A` | `zh` | 沙皇统治下的吸烟：沙皇俄国烟草史 (Smoking under the Tsars) | Tricia Starks (特里西娅·斯塔克斯) | 14 | 842.3 | ✅ 可读全文 |
| 143 | `steinberg_2017_russian_rev` | `A` | `en` | The Russian Revolution, 1905-1921 (2017) [OXFORD HISTORIES] (Mark D. Steinberg) (Z-Library).pdf | - | 21 | 960.2 | ✅ 可读全文 |
| 144 | `stites_1989_revolutionary_dreams_zh` | `A` | `zh` | 革命的梦想：俄国革命中的乌托邦愿景与实验生活 (Revolutionary Dreams) | Richard Stites (理查德·斯泰茨) | 18 | 995.0 | ✅ 可读全文 |
| 145 | `struggle_against_trotskyism_zh` | `A` | `zh` | 布尔什维克党反对托洛茨基主义的斗争 The Bolshevik Party_s Struggle Against Trotskyism (一个普通的人) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 7 | 422.6 | ✅ 可读全文 |
| 146 | `sukhanov_1922_personal_record` | `S/B-dual` | `en` | The Russian Revolution 1917: A Personal Record | N. N. Sukhanov (ed. & trans. Joel Carmichael) | 32 | 1696.2 | ✅ 可读全文 |
| 147 | `suny_2017_red_flag_unfurled_zh` | `A` | `zh` | 红旗飘扬 历史、历史学家与俄国革命(Red Flag Unfurled history historians and the russian revolution 中译本) ([美]罗纳德·格里戈尔·苏尼 著一个普通的人 译) (z-library.sk, 1lib.sk, z-lib.sk).epub | - | 10 | 680.6 | ✅ 可读全文 |
| 148 | `swain_1996_origins_of_civil_war` | `A` | `en` | The Origins of the Russian Civil War | Geoffrey Swain | 19 | 750.0 | ✅ 可读全文 |
| 149 | `treadgold_1955_lenin_and_rivals` | `A` | `en` | Lenin and his Rivals. The Struggle for Russias Future, 1898-1906. (Donald W. Treadgold) (z-library.sk, 1lib.sk, z-lib.sk).pdf | - | 22 | 776.6 | ✅ 可读全文 |
| 150 | `trotsky_1905_zh` | `B` | `zh` | 1905 ([俄] 列夫·达维多维奇·托洛茨基 著, Uni 佐仓绫奈 译校) (Z-Library).pdf | - | 18 | 946.9 | ✅ 可读全文 |
| 151 | `trotsky_1930_history_rr_zh` | `S/B-dual` | `zh` | 俄国革命史（全三卷） | Leon Trotsky (列夫·托洛茨基) | 57 | 2540.0 | ✅ 可读全文 |
| 152 | `velikanova_2013_popular_perception` | `A` | `en` | 20世纪20年代苏联政治的大众认知Popular Perception Of Soviet Politics in the 1920s (O. Velikanova) (z-library.sk, 1lib.sk, z-lib.sk).epub | - | 10 | 1265.7 | ✅ 可读全文 |
| 153 | `venturi_1960_roots` | `A` | `en` | Roots of Revolution: A History of the Populist and Socialist Movements in Nineteenth Century Russia | Franco Venturi (Intro by Isaiah Berlin) | 30 | 2758.3 | ✅ 可读全文 |
| 154 | `voitikov_stalin_vs_zinoviev_zh` | `A` | `zh` | 斯大林对抗季诺维也夫 (Сталин против Зиновьева) | Сергей Сергеевич Войтиков (谢·谢·沃伊季科夫) | 28 | 1223.4 | ✅ 可读全文 |
| 155 | `wada_haruki_feb_1917_zh` | `A` | `zh` | 俄国革命：彼得格勒，1917年2月 | 和田春树 (Haruki Wada) | 31 | 1213.0 | ✅ 可读全文 |
| 156 | `walicki_1969_controversy` | `A` | `en` | The Controversy over Capitalism: Studies in the Social Philosophy of the Russian Populists | Andrzej Walicki | 8 | 458.3 | ✅ 可读全文 |
| 157 | `westwood_1964_history_russian_railways_zh` | `A` | `zh` | 俄罗斯铁路史 (A History of Russian Railways) | J. N. Westwood | 16 | 524.2 | ✅ 可读全文 |
| 158 | `white_2010_sr_alternative` | `A` | `en` | The Socialist Alternative to Bolshevik Russia The Socialist Revolutionary Party, 1921-39.pdf | - | 18 | 559.9 | ✅ 可读全文 |
| 159 | `women_labor_soviet_industry_zh` | `B` | `zh` | 苏联工业中的妇女劳动 | Н. Д. Араловец (阿拉洛维茨著，丁钱清译) | 6 | 264.2 | ✅ 可读全文 |
| 160 | `xu_tianxin_ussr_history_v4_stalin_model_zh` | `A` | `zh` | 苏联史 第四卷：斯大林模式的形成 | 徐天新 | 431 | 1155.0 | ✅ 可读全文 |
| 161 | `yao_hai_ussr_history_v1_russian_rev_zh` | `A` | `zh` | 苏联史 第一卷 俄国革命 | 姚海 | 503 | 3246.3 | ✅ 可读全文 |
| 162 | `zelnik_1999_workers_intelligentsia` | `A` | `en` | workers-the-intelligentsia-and-marxist-parties-st-petersburg-1895-1917-and-shanghai-1921-1927.pdf | - | 3 | 171.3 | ✅ 可读全文 |
| 163 | `zelnik_1999_workers_intelligentsia_marxist_parties` | `A` | `en` | Workers, the Intelligentsia and Marxist Parties: St Petersburg, 1895–1917 and Shanghai, 1921–1927 | Steve A. Smith | 3 | 180.0 | ✅ 可读全文 |
| 164 | `zemskov_stalin_era_zh` | `A` | `zh` | 《斯大林时代：经济，镇压，工业化》 ([俄]泽姆斯科夫) (Z-Library).pdf | - | 10 | 697.8 | ✅ 可读全文 |
| 165 | `zhang_jianhua_political_radicalism_zh` | `A` | `en` | zhang_jianhua_political_radicalism_zh | - | 44 | 43.6 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 166 | `zheng_yifan_nep_russia_zh` | `A` | `zh` | 苏联史 第三卷 新经济政策的俄国 | 郑异凡 | 75 | 88.2 | ⚠️ 待OCR/补档 (`needs_ocr`) |
| 167 | `zhukov_zinoviev_zh` | `A` | `zh` | 格里高利·季诺维也夫被遗忘的世界革命领袖-Григорий Зиновьев. Отвергнутый вождь мировой революции (尤里·茹科夫,Юрий Ник... (z-library.sk, 1lib.sk, z-lib.sk).epub | - | 35 | 1472.8 | ✅ 可读全文 |
