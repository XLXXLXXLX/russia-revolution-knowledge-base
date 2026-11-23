# W62 入库日志：1919–1929 论文与 Smele 内战辞书

日期：2026-11-23。本日志只记录下载、提取与扉页核验。未写 `reading-notes/`，未写 `CLM-*`，未改 `sources/LITERATURE_CATALOG.md`、`BIBLIOGRAPHY_WISHLIST.md`、`README.md`、`framework/`、`.gitmodules` 或已有卡片。

检索通道：`annas-mcp article_search`（`provider=anna`，`downloadable_only`）与 `article_download`（按 MD5）。OpenAlex 未配置 `OPENALEX_API_KEY`，本轮未用。14 篇新论文全部 `needs_ocr: false`，`empty_page_ratio: 0.0`。作者、篇名、年份与语种按各篇 `ch00` 扉页填写。

## 辞书

| 输出目录 | 扉页核定 | 提取 |
| :--- | :--- | :--- |
| `sources/monographs/smele_historical_dictionary_civil_wars/` | Jonathan D. Smele, *Historical Dictionary of the Russian Civil Wars, 1916–1926* (Lanham: Rowman & Littlefield, 2015). ISBN 978-1-4422-5280-6. LC DK265.S526 2015. 版权页在 PDF p. 6；作者小传在 PDF p. 1591。语种 en。等级 B。 | 输入 `inbox/Historical Dictionary of th_ (Z-Library).pdf`。77 章，4,022,179 字符，1591 页。`needs_ocr: false`（`empty_page_ratio: 0.0006`）。PDF p. 1 为无文字层封面，书名取自 PDF pp. 5–6。 |

## 已入库论文（14）

PDF 在 `inbox/articles/<slug>.pdf`，全文在 `sources/articles/<slug>/`。等级均为 A。

| Slug | 扉页 | 字符 / 章 | `cited_by` |
| :--- | :--- | ---: | :--- |
| `slezkine_1994_ussr_as_communal_apartment` | Yuri Slezkine, “The USSR as a Communal Apartment, or How a Socialist State Promoted Ethnic Particularism,” *Slavic Review* 53, no. 2 (Summer 1994): 414–452. | 137,901 / 40 | `martin_2001_affirmative_action_empire` |
| `martin_1998_russification_of_the_rsfsr` | Terry Martin, “The Russification of the RSFSR,” *Cahiers du Monde russe* 39, no. 1/2 (Jan.–Jun. 1998): 99–117. | 69,603 / 19 | `martin_2001_affirmative_action_empire` |
| `martin_1998_origins_soviet_ethnic_cleansing` | Terry Martin, “The Origins of Soviet Ethnic Cleansing,” *Journal of Modern History* 70, no. 4 (Dec. 1998): 813–861. DOI 10.1086/235168. | 157,285 / 2 | `martin_2001_affirmative_action_empire` |
| `smith_1998_georgian_affair_of_1922` | Jeremy Smith, “The Georgian affair of 1922—Policy failure, personality clash or power struggle?,” *Europe-Asia Studies* 50, no. 3 (1998): 519–544. DOI 10.1080/09668139808412550. | 96,111 / 2 | `martin_2001_affirmative_action_empire` |
| `wheatcroft_davies_cooper_1986_soviet_industrialization_reconsidered` | S. G. Wheatcroft, R. W. Davies, and J. M. Cooper, “Soviet Industrialization Reconsidered: Some Preliminary Conclusions about Economic Development between 1926 and 1941,” *Economic History Review*, 2nd ser., 39, no. 2 (1986): 264–294. | 112,241 / 2 | `allen_2003_farm_to_factory` |
| `edmondson_1977_politics_of_hunger_famine_1921` | Charles M. Edmondson, “The Politics of Hunger: The Soviet Response to Famine, 1921,” *Soviet Studies* 29, no. 4 (Oct. 1977): 506–518. | 43,965 / 13 | `douds_2018_inside_lenins_government` |
| `roslof_1996_heresy_of_bolshevik_christianity_nep` | Edward E. Roslof, “The Heresy of ‘Bolshevik’ Christianity: Orthodox Rejection of Religious Reform during NEP,” *Slavic Review* 55, no. 3 (Autumn 1996): 614–635. | 78,744 / 22 | `douds_2018_inside_lenins_government` |
| `ball_1984_lenin_and_private_trade` | Alan Ball, “Lenin and the Question of Private Trade in Soviet Russia,” *Slavic Review* 43, no. 3 (Autumn 1984): 399–412. | 56,930 / 15 | `ball_1987_nepmen_zh` |
| `barnett_1994_as_good_as_gold_chervonets` | Vincent Barnett, “As Good as Gold? A Note on the Chervonets,” *Europe-Asia Studies* 46, no. 4 (1994): 663–669. DOI 10.1080/09668139408412189. 正文引用 L. N. Yurovsky 与 Sokol'nikov。 | 25,537 / 1 | `carr_1954_interregnum` |
| `barnett_1995_soviet_commodity_markets_nep` | Vincent Barnett, “Soviet Commodity Markets during NEP,” *Economic History Review*, n.s., 48, no. 2 (May 1995): 329–352. | 78,247 / 24 | `ball_1987_nepmen_zh` |
| `klein_1999_kondratiev_slutsky_conjuncture_institute` | Judy L. Klein, “The Rise of ‘Non-October’ Econometrics: Kondratiev and Slutsky at the Moscow Conjuncture Institute,” *History of Political Economy* 31, no. 1 (1999): 137–168. | 78,696 / 2 | `cohen_1973_bukharin` |
| `heinzen_1998_professional_identity_nep_countryside` | James W. Heinzen, “Professional Identity and the Vision of the Modern Soviet Country Side: Local Agricultural Specialists at the End of the NEP, 1928–1929,” *Cahiers du Monde russe* 39, no. 1/2 (1998): 9–25. 扉页印作 Country Side。 | 73,670 / 18 | `mcdonald_2011_face_to_the_village` |
| `landis_2004_between_village_and_kremlin_tambov` | Erik-C. Landis, “Between Village and Kremlin: Confronting State Food Procurement in Civil War Tambov, 1919–20,” *Russian Review* 63 (Jan. 2004): 70–88. | 67,455 / 1 | `mcdonald_2011_face_to_the_village` |
| `mcdermott_1995_stalin_comintern_third_period` | Kevin McDermott, “Stalin and the Comintern during the ‘Third Period’, 1928–33,” *European History Quarterly* 25, no. 3 (1995): 409–429. 刊名由正文末 `ehq.sagepub.com` 与起止页 409/429 核定。 | 54,488 / 1 | `cohen_1973_bukharin` |

论文正文合计约 1,130,873 字符。

`cited_by` 只用了库内已有专著目录。`pirani_2008_russian_rev_in_retreat` 与 `rossman_2005_worker_resistance_zh` 两个目录名不存在，未写入。

## 点名方向里没有下到全文的项目

这些查询在 Anna's Archive 可下载期刊索引中没有合适的 1919–1929 全文，因此没有建目录。

- **谷物平衡表专文**：Wheatcroft 1974 年战前粮食统计已在 `sources/articles/wheatcroft_1974_reliability_prewar_grain_statistics/`。本轮下到的是 Wheatcroft、Davies、Cooper 1986 年文，范围是 1926–1941，含新经济政策末期。没有另检出一篇只做 1920 年代谷物平衡表的可下载期刊 PDF。
- **Heinzen 与 1920 年代反贿赂**：可下载的 Heinzen 贿赂/腐败论文是晚期斯大林时期，不在本窗口：*Slavic Review* 66, no. 3 (2007), “The Art of the Bribe”；*Comparative Economic Studies* 47 (2005), “Corruption in the Gulag”。入库的是他 1998 年关于 1928–1929 年地方农业专家的论文。
- **坦波夫第 0116 号毒气令**：`Тухачевский` / `0116` / Antonov 化学武器查询没有返回可下载史学论文。Landis 2004 写的是 1919–1920 年坦波夫粮食征集，不是 1921 年毒气令。
- **教会财物没收的中央政令论文**：Edmondson 1977 是 1921 年饥荒决策。Roslof 1996 是新经济政策时期对“布尔什维克基督教”革新运动的拒绝。以“изъятие церковных ценностей”能找到 2009–2015 年地方学院学报（如秋明教区），未当作核心期刊入库。
- **耐普曼税负专文**：Ball 1984 讨论列宁与私人贸易，不是税额归宿论文。
- **戈尔曼 / 巴扎罗夫、发生学派与目的论派**：Klein 1999 写莫斯科行情研究所的 Kondratiev 与 Slutsky。正文检索未见 Groman、Bazarov 或 Gosplan。Barnett 2002 年 “Which was the ‘Real’ Kondratiev: 1925 or 1928?” 是短书评式笔记，未再入库。
- **维托夫事件**：`Wittorf` 题名检索为 0。McDermott 1995 写第三时期 1928–1933，正文没有 Wittorf / Thälmann。
- **Хлевнюк / Данилов / Павлюченков / Ивницкий**：`Ивницкий`、`С. А. Павлюченков` 的可下载期刊检索为空。`Хлевнюк` 的可下载论文是战后国家安全（*Cahiers du Monde russe* 42, 2001，与库内 `khlevniuk_2001_stalin_and_state_security_organs_ru` 同题时段）、1930–1950 年代中央—地方关系，以及 1940 年代末内务部经济危机。均不在 1919–1929，未重复入库。

## 未覆盖

未跑 OCR。未把上述空缺写成替代性论断。目录与愿望单留给后续编目，本轮没有改它们。
