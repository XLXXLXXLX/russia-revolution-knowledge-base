# W62B 入库日志：书评、俄文讲座与中文专栏（Grok Web-6）

日期：2026-11-23。本日志只记录检索、抓取、清洗与首尾核验。未写 `reading-notes/`，未写 `historiography/claims/CLM-*`，未写导读或论点摘要。未改 `framework/`、`.gitmodules`、`cards/`、`timeline/`、`README.md`、`sources/LITERATURE_CATALOG.md`。

全文目录：`sources/web-archive/W62B_reviews_and_zh_ru_web_essays/`。共 20 篇。正文（去掉 YAML 与标题行、去掉空白）合计 450,231 字符。每篇均不少于 1,500 字符，首尾为书评引用、注释、参考文献、访谈最后一轮或文章末段，不是验证码页或目录页。

抓取方式：公开 HTML，`requests` + BeautifulSoup。H-Net 只取 `p.revtext`、`p.center` 与 `table.revtext`，购书条（showpdf / Amazon / Powell’s）未入库。爱思想只取 `div.article-content`。回声莫斯科只取逐字稿段落。网页错字、OCR 残字与页面插入的署名栏按原文保留。

## 英文书评（7，等级 A）

| 文件 | 作者 / 日期 | 正文汉字与字母数 | 首尾 |
| :--- | :--- | ---: | :--- |
| `2004-10_murphy_rabinowitch-bolsheviks-come-to-power.md` | Kevin J. Murphy，2004-10。H-Russia 评 Rabinowitch, *The Bolsheviks Come to Power*（2004 重印）。https://www.h-net.org/reviews/showrev.php?id=9856 | 14,061 | 书目起句至 H-Net 版权段；注 [1]–[12] 在引用之前收束 |
| `2004-05_sunderland_sanborn-drafting-the-russian-nation.md` | Willard Sunderland，2004-05。评 Sanborn, *Drafting the Russian Nation*（1905–1925）。https://www.h-net.org/reviews/showrev.php?id=9337 | 9,765 | 同上，至 H-Net 版权段。此篇不是 *Imperial Apocalypse* |
| `2006-05_allen_murphy-revolution-and-counterrevolution.md` | Barbara C. Allen，2006-05。评 Kevin Murphy, *Revolution and Counterrevolution*。https://www.h-net.org/reviews/showrev.php?id=11752 | 29,382 | 至 H-Net 版权段 |
| `2003-07_stolberg_harris-great-urals.md` | Eva M. Stolberg，2003-07。评 Harris, *The Great Urals*。https://www.h-net.org/reviews/showrev.php?id=7848 | 8,226 | 至 H-Net 版权段 |
| `2010-03_savage_halfin-intimate-enemies.md` | Rowan Savage，2010-03。H-Genocide 评 Halfin, *Intimate Enemies*（1918–1928）。https://www.h-net.org/reviews/showrev.php?id=25933 | 17,104 | 至 CC BY-NC-ND 4.0 许可句 |
| `2024-11_fraunholtz_odonnell-power-and-possession.md` | Peter Fraunholtz，2024-11。评 O'Donnell, *Power and Possession in the Russian Revolution*。https://www.h-net.org/reviews/showrev.php?id=61398 | 9,437 | 至 CC BY-NC-ND 4.0 许可句 |
| `2016-04-05_h-diplo_kotkin-stalin-vol1-roundtable.md` | Westad 导言；Carley、Haslam、Pons、Pipes 书评；Kotkin 作者回应。2016-04-05。https://networks.h-net.org/node/28443/discussions/118756/h-diplo-roundtable-xvii-19-stalin-volume-i-paradoxes-power-1878 | 82,589 | 目录五篇加作者回应均在；末注为 *The Maisky Diaries* (Yale, 2015), p. 279 |

## 俄文全文（6）

| 文件 | 作者 / 日期 / 等级 | 字符 | 首尾 |
| :--- | :--- | ---: | :--- |
| `2017_kolonitskii_antimonarchist-revolution-cult-of-leader.md` | Колоницкий，2017，A。https://cyberleninka.ru/article/n/antimonarhicheskaya-revolyutsiya-1917-goda-i-nachalo-formirovaniya-kulta-vozhdya-naroda | 49,986 | 题录与摘要起，参考文献止于 Kotkin, *Magnetic Mountain* (1995)。邮箱一行是网页 OCR，未改 |
| `2018_solovyov_ideya-samoderzhaviya.md` | Кирилл Соловьев（俄国史研究所，不是哲学家弗拉基米尔·索洛维约夫），2018，A。https://cyberleninka.ru/article/n/ideya-samoderzhaviya-konets-xix-nachalo-xx-vv | 48,623 | 题录起，译成英文的参考文献末条止 |
| `2017-03-03_kolonitskii_ploho-organizovannyi-golod.md` | Колоницкий，2017-03-03，B。https://scepsis.net/library/id_3790.html | 10,220 | 斯克普西斯编者导语起，文末《Ведомости》原址止 |
| `2013-06-26_khlevniuk_istochniki-biografii-stalina.md` | Хлевнюк，2013-06-26，B。https://gefter.ru/archive/9192 | 18,871 | 正文起，末注指向 perspectivia.net 上的赫列夫纽克文章 |
| `2014-10-26_shubin_makhno-gulyai-pole-interview.md` | Шубин / Соколов，2014-10-26，B。https://echofm.online/archive/cenapobedy/44053 | 35,524 | 首轮 **М.Соколов** 起，末轮「Спасибо.」止。页题作「Гуляийполя」，正文另作「Гуляйполе」，均未改。播放器与「Скачать」未收入 |
| `2007_davydov_stolypin-zemleustroistvo.md` | Давыдов，2007，B（会议讲演刊印本）。https://cyberleninka.ru/article/n/vystuplenie-na-nauchno-prakticheskoy-konferentsii-stolypinskaya-model-modernizatsii-rossii-1906-2006-6 | 47,159 | 「Уважаемые коллеги」起，「И реформа начала это делать.」止 |

## 中文全文（7）

| 文件 | 作者 / 日期 / 等级 | 字符 | 首尾与出处 |
| :--- | :--- | ---: | :--- |
| `1994_shen-zhihua_nep-kulak.md` | 沈志华，1994，A。https://www.aisixiang.com/data/2509.html | 20,999 | 末行写明发表于《世界历史》1994年第5期、1995年第1期 |
| `2009_zheng-yifan_stalin-model-origins.md` | 郑异凡，2009，A。https://www.aisixiang.com/data/25201.html | 2,899 | 参考文献 [1]–[4] 收束。原载《探索与争鸣》2009年第2期。网页错字（「斯人林模式」「客砚」等）保留 |
| `2011_zheng-yifan_lenin-reform-attempt.md` | 郑异凡，2011，B。https://www.aisixiang.com/data/41750.html | 4,854 | 「（作者单位：中央编译局）」收束。来源行作同舟共进。正文中插入的署名栏「恢复□郑异凡……」保留 |
| `2016_wen-yi_nep-ideology-policy.md` | 闻一，2016，B。https://www.aisixiang.com/data/101513.html | 6,134 | 末句落在教育人民委员部与格普乌、宣传鼓动部的问题上。来源行作腾讯思享会 |
| `2016_yao-hai_populism-in-transition.md` | 姚海，2016，A。https://www.aisixiang.com/data/99256.html | 3,901 | 论证段之后只有页下注①，注的最后一句停在「有狭义和广义之分。」`article-content` 在此结束，其后是空段；「文章来源：探索与争鸣 2016年第4期」在容器外，只写入 `edition_note`。未补写期刊可能更长的注释 |
| `2012_zuo-fengrong_kronstadt-mutiny.md` | 左凤荣，2012，B。https://www.aisixiang.com/data/55048.html | 7,944 | 末句为史学界不再称之为「叛乱」。原载《炎黄春秋》2012年第6期 |
| `2021_zhang-guangxiang_bai-fan_pro-nobility-policy.md` | 张广翔、白帆，2021，A。https://www.aisixiang.com/data/130209.html | 22,553 | 注释与作者单位（吉林大学）收束。原载《江汉论坛》2021年第11期 |

## 本轮没有入库的地址

- `polit.ru` 达维多夫两讲（斯托雷平土地改革，2007-02-08；饥饿出口，2012-06-26）返回 Cloudflare「Just a moment...」，HTTP 403。未绕过。改用 CyberLeninka 上的 2007 年会议讲演刊印本。
- *New Left Review* 上 Steve Smith 评 Rabinowitch *The Bolsheviks in Power* 的页面带有摘要类标记，探针同时报出验证页特征，未入库。
- H-Soz-u-Kult 上 Holquist、Sanborn *Imperial Apocalypse*、Heinzen、Badcock 的德文书评：语种不在 en / ru / zh，未入库。
- H-Russia 评 Stone, *Hammer and Rifle*（https://www.h-net.org/reviews/showrev.php?id=5805）：时段偏到 1926–1933，本批未收。
- 郑异凡《〈联共（布）党史简明教程〉诞生记》（https://www.aisixiang.com/data/78570.html）：爱思想更新时间是 2026-07-13，页上没有可核对的原刊年份，未入库。
- 左凤荣、沈志华《俄国民粹派与斯托雷平改革》（https://www.aisixiang.com/data/51794.html）：去掉导航后不足入库长度，未收。
- 刘显忠访谈（https://www.aisixiang.com/data/102920.html）：叙述延伸到 1991 年，未收。
- 曹维安相关的抄袭争议帖未收。
- litresp、yakniga 上的舒宾、伊兹莫济克书稿是受版权保护的扫描，未收。
- Arzamas 的赫列夫纽克课程是订阅音频；Postnauka《Свертывание НЭПа》是视频，没有抓到全文稿。
- Academia.edu 与 *Foreign Affairs* 摘录不是开放全文。

## 站点清单

已把本轮实测畅通的 `scepsis.net`、`gefter.ru`、`aisixiang.com`、`echofm.online` 写入 `sources/WEB_REPOSITORIES.md` 第二节附。H-Net 旧书评页与 H-Diplo 圆桌的实测结果补在原有 H-Russia 条目下。`polit.ru` 未写入。
