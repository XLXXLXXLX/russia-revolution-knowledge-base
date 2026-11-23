---
id: AUD-23A-wave62-grok-reader-and-prose-audit
type: audit
auditor_model: grok-4.7
target_wave: W62
role: dialectic-auditor
status: remediated
updated_at: "2026-11-23"
---

# AUD-23A｜wave62｜`reader/` 第九、十三章、十五章大纲与 B5 模态 A 长文｜异源对抗审计

审计日：2026-11-23。只读对照 `cards/`、`historiography/claims/`、`historiography/debates/`、`data/DATA-01..08`、`timeline/L3_daily/`、`benchmarks/suites/b4b_historiography_1918_1929.jsonl`。抽查长文的实际路径是 `benchmarks/samples/b5_holdout/`。`B5-PROSE-03` 与 `B5-PROSE-06` 未撞上 AUD-19–22 已修正口径，下面不单列。章末 `<details>` 相对链接均能打开，不单列。

严重度：P0 为错误数字、错误分母或被基准题明文禁止的已核日期；P1 为把两个已核事实焊成一句，或把演说原话写成叙述者的统计；P2 为日期动词、月份窗口、大纲漏卡与时代字段。

## P0

### P0-01　第 0116 号写成 1921-06-12 且“已为档案坐实”

- 位置：[ch09_war_communism_and_kronstadt_turn.md:33](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch09_war_communism_and_kronstadt_turn.md:33)、[:81](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch09_war_communism_and_kronstadt_turn.md:81)
- 依据：[b4b_historiography_1918_1929.jsonl](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/benchmarks/suites/b4b_historiography_1918_1929.jsonl) `B4B-12` 的 `gold_facts` 写明馆藏没有 `1921-06-12` 这一已核签发日，不得把站外通行日期补进已核事实。[PER-tukhachevsky.md:76](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-tukhachevsky.md:76)、[EVT-1920-1921-tambov-and-peasant-revolts.md:88](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md:88) 均将确切签发日列为待核。命令存在、是否投放、覆盖范围、致死人数是四个问题。

Target（正文）→

`甚至在 6 月签发第 0116 号命令批准使用窒息性毒气清剿森林据点。`

Replacement →

`另有第 0116 号使用窒息性毒气驱赶森林藏匿武装的命令。确切签发日、是否施放、覆盖范围和致死人数均未核验，不得写成 1921 年 6 月或 6 月 12 日。第 130 号与第 171 号是人质和集中营令。`

Target（尾注 `[^5]`）→

`图哈切夫斯基司令部于 1921 年 6 月 12 日签发第 0116 号使用窒息性毒气清剿森林游击队的命令已为档案坐实，但实际施放次数与直接致死人数尚无精确档案定论。`

Replacement →

`第 0116 号是化学武器命令，馆藏未核确切签发日，不得写 1921-06-12，也不得写“已为档案坐实”。是否投放、覆盖范围与致死人数仍是三个未核问题，不能给出毒气致死总数。人质与在营农民分开计：Leggett 记至 7 月 20 日人质约 5,000 人；Figes 另估 6 月底约 50,000 农民入营。后一个数字不是人质数，也不是毒气致死数。游击队由 5 月约 21,000 人降至 7 月中旬约 1,200 人，这条可以保留。`

### P0-02　把 1920 年的 1.02:1 工资比写成 1918 年秋生产率下跌的原因

- 位置：[ch09_war_communism_and_kronstadt_turn.md:15](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch09_war_communism_and_kronstadt_turn.md:15)
- 依据：[CLM-ilyukhov-war-communism-leveling-vs-nep-piecework.md:21](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-ilyukhov-war-communism-leveling-vs-nep-piecework.md:21) 全国技工/杂工工资比在 1920 年约为 1.02:1。同卡 [:26](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-ilyukhov-war-communism-leveling-vs-nep-piecework.md:26)：1918 年秋彼得格勒取消计件，生产率降 24%–60%；1919 年 2 月法规把计件—奖金定为原则。

Target →

`而 1918 年秋一度废除计件制、将熟练工与杂工实物配给差距压缩至 1.02 比 1 后，生产率旋即下跌 24% 至 60%，迫使当局自 1919 年春起重新全面恢复计件工资制。`

Replacement →

`1918 年秋彼得格勒取消计件后，生产率下降 24% 至 60%。1919 年 2 月法规把计件—奖金定为原则、计时为例外。熟练工与杂工收入比约 1.02:1 是 1920 年的全国工资比，不是 1918 年秋那次下跌的原因，也不是当时的实物配给差距。`

### P0-03　把 1.28 亿普特同比缺口写成低于 5 亿普特底线的那个量

- 位置：[ch13_grain_crisis_and_right_opposition_defeat.md:5](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch13_grain_crisis_and_right_opposition_defeat.md:5)
- 依据：[1928-1929_bukharin_stalin_final_showdown.md:42](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md:42)。勒温：到 12 月底收购绝对量仅约 3 亿普特，低于城市、军队与经济作物区所需的约 5 亿普特。1.28 亿普特是较上年的累计短缺，约合 210 万吨。短缺额本身小于 5 亿，但这不是底线所衡量的量。

Target →

`截至 1927 年底，国家收购较上年累计短缺约 1.28 亿普特（约 210 万吨），远低于维持城市口粮、红军给养、产棉区调拨与外贸出口所需的约 5 亿普特安全底线。`

Replacement →

`截至 1927 年底，国家收购较上年累计短缺约 1.28 亿普特（约 210 万吨）。低于约 5 亿普特城市、军队与经济作物区底线的，是到 12 月底的收购绝对量，约 3 亿普特。不要把同比缺口写成那个绝对量。`

### P0-04　冬麦主产区 4 月的 25.4 万吨接在全国 2 月的 190 万吨后面

- 位置：[ch13_grain_crisis_and_right_opposition_defeat.md:13](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch13_grain_crisis_and_right_opposition_defeat.md:13)
- 依据：[DATA-03-1926-1929-grain-procurement-and-nemchinov-table.md:111](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/data/DATA-03-1926-1929-grain-procurement-and-nemchinov-table.md:111)；[1928-01_siberian_grain_expedition_and_shakhty_affair.md:97](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-01_siberian_grain_expedition_and_shakhty_affair.md:97)。25.4 万吨是 4 月冬麦主产区收购，不足 3 月冬麦区的三分之一。2 月 190 万吨是全国数。同卷 [1928-1929 摊牌卷:112](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md:112) 丢掉了“冬麦区”限定，不要跟着它写。馆藏没有可与 190 万吨直接相减的全国 4 月总吨数。

Target →

`4 月中央全会刚承诺终止非常措施，当月收购便跌回 25.4 万吨`

Replacement →

`4 月中央全会刚承诺终止非常措施，当月冬麦主产区收购降至 25.4 万吨，不足 3 月冬麦区的三分之一。这不是 2 月全国 190 万吨的全国后续月度。`

### P0-05　B5-PROSE-08 把第 107 条、乌拉尔—西伯利亚方法与全盘集体化焊进 1927–1928 年冬

- 位置：[B5-PROSE-08.md:95](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/benchmarks/samples/b5_holdout/B5-PROSE-08.md:95)
- 依据：[1928-01_siberian_grain_expedition_and_shakhty_affair.md:27](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-01_siberian_grain_expedition_and_shakhty_affair.md:27) 禁止把 1928 年 1–2 月的第 107 条非常措施倒填为“乌拉尔—西伯利亚方法”。该方法在 1929-03-20 由政治局批准；五倍罚款的全俄中央执委会授权是 1929-04-28（[摊牌卷:223](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md:223)）。全盘集体化是 1929 年末的转折。

Target →

`当1927—1928年冬粮食收购危机爆发、斯大林亲自挥起《刑法典》第107条与“乌拉尔—西伯利亚方法”强行征粮并启动全面集体化时`

Replacement →

`当 1927–1928 年冬粮食收购危机爆发时，斯大林动用的是《刑法典》第 107 条非常措施。乌拉尔—西伯利亚方法是 1929 年 3 月 20 日政治局批准的村社摊派；全盘集体化是 1929 年末的转折。三者不要写进同一个“当”字句。`

## P1

### P1-01　安东诺夫的领导权被写成 1920 年 11 月才开始

- 位置：[ch09_war_communism_and_kronstadt_turn.md:25](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch09_war_communism_and_kronstadt_turn.md:25)
- 依据：[PER-antonov.md:26](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-antonov.md:26)（AUD-20D 之后的人物卡，优先于事件卡里“11 月出任统一军事总指挥”的旧压缩）。8 月 19 日卡缅卡揭开起义；安东诺夫约于 8 月 24 日取得领导地位；11 月组成统一指挥部，托克马科夫任司令员，安东诺夫任总参谋长并是实际最高统帅。

Target →

`当年 11 月，出身社会革命党、曾任基尔萨诺夫县民警局长的亚历山大·安东诺夫出任起义军总参谋长兼实际统帅`

Replacement →

`安东诺夫于 1920 年 8 月 24 日前后取得领导地位。11 月组成坦波夫游击集团军统一指挥部：前军官托克马科夫任司令员，安东诺夫任总参谋长，并是实际最高统帅`

### P1-02　17 日夜的“约千余”被写成指挥成员一次带走八千人

- 位置：[ch09_war_communism_and_kronstadt_turn.md:51](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch09_war_communism_and_kronstadt_turn.md:51)
- 依据：[1921-03_kronstadt_and_10th_congress.md:169](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1921-03_kronstadt_and_10th_congress.md:169) 记 17 日夜 11 名临时革命委员会核心委员带领约千余人撤往芬兰。同卷 [:176](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1921-03_kronstadt_and_10th_congress.md:176) 的累计约 8,000 人是另一近似量，多在 18 日前后离岛。[EVT-1921-kronstadt.md:32](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1921-kronstadt.md:32) 也要求这 8,000 人不得反推起义总人数或死亡数。尾注 `[^4]` 把 8,000 人单列为撤离估计，可以保留。

Target →

`17 日深夜，弹尽援绝的彼得里琴科等指挥成员率约八千军民越冰撤往芬兰`

Replacement →

`17 日深夜，彼得里琴科等 11 名临时革命委员会核心委员带领约千余人员越冰撤往芬兰。累计约 8,000 名水兵、士兵与平民撤入芬兰是另一近似量，不能写成 17 日夜由指挥成员一次带走的人数`

### P1-03　斯大林演说里的黑土区 1.4 亿→500 万被写成已核收购数

- 位置：[ch13_grain_crisis_and_right_opposition_defeat.md:51](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch13_grain_crisis_and_right_opposition_defeat.md:51)
- 依据：[1928-1929_bukharin_stalin_final_showdown.md:205](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md:205)：到 1929 年 4 月 1 日，乌克兰由约 2 亿普特降到 2,670 万普特，北高加索降至约四分之一，中央黑土区降至约八分之一。1.4 亿→500 万只出现在斯大林 4 月 22 日演说（[RN-W61-july1928-april1929-nov1929-stenograms.md:119](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/kak_lomali_nep_1928_1929_plenums/RN-W61-july1928-april1929-nov1929-stenograms.md:119)）。5/140 不是八分之一。乌克兰 2 亿→2,670 万可以保留。

Target →

`乌克兰国家交粮量从往年约 2 亿普特暴跌至 2,670 万普特，中央黑土区从 1.4 亿普特跌至 500 万普特`

Replacement →

`乌克兰国家交粮量从往年约 2 亿普特降到 2,670 万普特，北高加索降至约四分之一，中央黑土区降至约八分之一。若保留“1.4 亿普特跌至 500 万普特”，须标明这是斯大林 4 月 22 日演说原话，不能与勒温的“约八分之一”当成同一统计`

### P1-04　五倍罚款被系在 1929 年 3 月 20 日政治局批准上

- 位置：[ch13_grain_crisis_and_right_opposition_defeat.md:51](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch13_grain_crisis_and_right_opposition_defeat.md:51)
- 依据：[POL-ural-siberian-method.md:29](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-ural-siberian-method.md:29)：五倍罚款授权在 1929 年 4 月，刑法第 61 条第 3 款修订在 1929 年 6 月。[摊牌卷:223](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md:223)：全俄中央执委会 4 月 28 日授权。西伯利亚地方约自 4 月 10 日起已在执行（[RN-W62](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reading-notes/class_ideology_and_ogpu_village/RN-W62-fitzpatrick-priestland-tragedy-v1-and-ogpu-v2.md) 第 64 行）。3 月 20 日批准的是村社大会自我摊派。同段后文布哈林在四月全会上讨论五倍罚款，可以保留。

Target →

`违者断供日用工业品、拍卖家产并处以五倍罚款——1929 年 3 月 20 日政治局不顾右派三人反对正式批准了这一“乌拉尔—西伯利亚方法”。`

Replacement →

`违者断供日用工业品并拍卖家产。1929 年 3 月 20 日政治局不顾右派三人反对，批准的是村社大会自我摊派这一乌拉尔—西伯利亚方法。五倍罚款不是 3 月 20 日的条款：西伯利亚约自 4 月 10 日起执行，全俄中央执委会于 4 月 28 日授权，刑法第 61 条第 3 款的修订在 6 月。`

## P2

### P2-01　50 克面包被放在布列斯特和约之后

- 位置：[ch09_war_communism_and_kronstadt_turn.md:11](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch09_war_communism_and_kronstadt_turn.md:11)
- 依据：[CLM-smith-1983-post-october-centralization.md:22](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-smith-1983-post-october-centralization.md:22)。50 克是 1918 年 2 月底、德军逼近时的定量。和约在 3 月 3 日。逾百万人离开首都是 1918 年上半年。35.1 万→14.87 万、金属工人 16.7 万→4.3 万的窗口（1917-01-01 至 1918-04-01）不用改。

Target →

`布列斯特停战后军工订单骤停，燃料与粮食动脉受阻，彼得格勒每日面包配给一度跌至 50 克，逾百万居民逃离首都。`

Replacement →

`停战复员与燃料断绝之中，1918 年 2 月底彼得格勒每日面包配给跌至 50 克，德军逼近引发恐慌。布列斯特和约签于 3 月 3 日，50 克定量不是和约之后才出现的。1918 年上半年逾百万人离开彼得格勒。`

### P2-02　总局数“逾 40”少了卡片上的“逾 42”

- 位置：[ch09_war_communism_and_kronstadt_turn.md:13](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch09_war_communism_and_kronstadt_turn.md:13)
- 依据：[INS-vsnkh-and-gosplan.md:25](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/institutions/INS-vsnkh-and-gosplan.md:25)。

Target →

`该机构演化为逾 40 个垂直行业总局（главкизм）构成的庞大金字塔`

Replacement →

`该机构演化为逾 42 个垂直行业总局（главкизм）构成的庞大金字塔`

### P2-03　选出的三分之一被写成“基层工会与工人”

- 位置：[ch09_war_communism_and_kronstadt_turn.md:13](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch09_war_communism_and_kronstadt_turn.md:13)
- 依据：[CLM-duval-oppenheim-vtsik-and-vsnkh-consolidation.md:30](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-duval-oppenheim-vtsik-and-vsnkh-consolidation.md:30)。1918-05-26 至 06-04 的代表大会上，列宁—李可夫—魏因贝格推翻奥新斯基草案：三分之二由大区经委或最高国民经济委员会委派，三分之一由工人选举。二分之一以上的方向是对的；工会不在选出的那三分之一里。

Target →

`反转为上级经委机关委派三分之二、基层工会与工人仅选三分之一`

Replacement →

`反转为企业管理委员会三分之二由大区经委或最高国民经济委员会委派，仅三分之一由工人选举`

### P2-04　粮食专政令的 5 月 9 日用了“颁布”

- 位置：[ch09_war_communism_and_kronstadt_turn.md:17](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch09_war_communism_and_kronstadt_turn.md:17)
- 依据：[POL-war-communism.md:25](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-war-communism.md:25)。全俄中央执行委员会 1918-05-09 通过该令；部分史书按签署或刊布记 1918-05-13。

Target →

`全俄中央执行委员会于 5 月 9 日颁布赋予粮食人民委员部非常权力的粮食专政令`

Replacement →

`全俄中央执行委员会于 1918 年 5 月 9 日通过粮食专政令，授予粮食人民委员部非常权力。部分史书把签署或刊布记在 5 月 13 日`

### P2-05　图哈切夫斯基到任后的兵力仍停在 3 月初的四万余人

- 位置：[ch09_war_communism_and_kronstadt_turn.md:33](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch09_war_communism_and_kronstadt_turn.md:33)
- 依据：[EVT-1920-1921-tambov-and-peasant-revolts.md:32](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/events/EVT-1920-1921-tambov-and-peasant-revolts.md:32)：3 月 1 日为 32,500 名步兵加 8,000 名骑兵；4 月 27 日受命，5 月 6 日抵达。[PER-tukhachevsky.md:27](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-tukhachevsky.md:27) 与 [PER-antonov.md:27](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/people/PER-antonov.md:27)：6 月高峰逾十万，并配火炮、装甲与飞机。

Target →

`至 1921 年春，红军在坦波夫集结逾四万正规部队，并于 4 月底改派刚刚平定喀琅施塔得的米哈伊尔·图哈切夫斯基出任全权司令。`

Replacement →

`1921 年 3 月 1 日，红军在坦波夫已有 32,500 名步兵与 8,000 名骑兵。4 月 27 日图哈切夫斯基受命为全权司令，5 月 6 日抵达；6 月高峰期兵力逾十万，并配有火炮、装甲与飞机。`

### P2-06　进口粮食与黄金流失都写成“1928 年夏”

- 位置：[ch13_grain_crisis_and_right_opposition_defeat.md:33](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch13_grain_crisis_and_right_opposition_defeat.md:33)
- 依据：[1928-1929_bukharin_stalin_final_showdown.md:138](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md:138)。6–8 月进口约 25 万吨；7–9 月黄金流失 1.45 亿卢布。两个数本身不用改。

Target →

`1928 年夏政府被迫进口 25 万吨粮食、流失 1.45 亿卢布黄金`

Replacement →

`1928 年 6–8 月进口约 25 万吨粮食，7–9 月黄金流失 1.45 亿卢布`

### P2-07　“轻纺工人入党率不足 5%”扩大了哈奇的分母

- 位置：[ch13_grain_crisis_and_right_opposition_defeat.md:45](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch13_grain_crisis_and_right_opposition_defeat.md:45)
- 依据：[CLM-hatch-1989-lenin-levy-moscow-cells-and-stalinism.md:27](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-hatch-1989-lenin-levy-moscow-cells-and-stalinism.md:27)。低于 5% 的是 1925 年中以前、外县女工为主的纺织厂。莫斯科产业工人入党率已由 4% 升至 13%。同句“五六万名”对应 1924–1925 年莫斯科新增逾 5 万名列宁征召党员，可以保留。

Target →

`但轻纺工人入党率不足 5%`

Replacement →

`但外县、女工为主的纺织厂到 1925 年中入党率仍低于 5%。这不是 1928 年全体轻纺工人的入党率`

### P2-08　十六次代表会议“批准”最优方案，漏掉五月苏维埃代表大会

- 位置：[ch13_grain_crisis_and_right_opposition_defeat.md:57](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch13_grain_crisis_and_right_opposition_defeat.md:57)
- 依据：[POL-first-five-year-plan.md:34](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-first-five-year-plan.md:34) 与 [:59](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/policies/POL-first-five-year-plan.md:59)：十六次代表会议通过，第五次全苏苏维埃代表大会（1929-05-20 至 05-28）正式批准。[摊牌卷:223](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/timeline/L3_daily/1928-1929_bukharin_stalin_final_showdown.md:223) 用的动词也是“通过”。17.5% 仍属于代表会议方案，不要改成当年全盘集体化。会议卡 [MTG-1929-04-cc-joint-plenum.md:28](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/cards/meetings/MTG-1929-04-cc-joint-plenum.md:28) 把代表会议也写成“批准”，正文改跟政策卡和 L3。

Target →

`紧接全会召开的第十六次党代表会议（4 月 23 日至 29 日）批准的一五计划最优方案，仍预设到 1932/33 年度期末集体农庄与国营农场仅占全国播种面积的 17.5%`

Replacement →

`紧接全会召开的第十六次党代表会议（4 月 23 日至 29 日）通过的一五计划最优方案，仍预设到 1932/33 年度期末集体农庄与国营农场仅占全国播种面积的 17.5%。正式批准在 5 月 20 日至 28 日第五次全苏苏维埃代表大会`

### P2-09　正文把 KAPROST 的全要素生产率杠杆写成“剔除清洗损耗”

- 位置：[ch13_grain_crisis_and_right_opposition_defeat.md:63](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/ch13_grain_crisis_and_right_opposition_defeat.md:63)
- 依据：[CLM-hunter-szyrmer-1991-kaprost-early-soviet-alternatives.md:19](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-hunter-szyrmer-1991-kaprost-early-soviet-alternatives.md:19)。取消集体化的四个情景，1941-01-01 固定资本比历史实际的 1,140 亿（1928 年卢布）高 29.6%、34.0%、35.9%、40.1%。同卡 [:30](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/historiography/claims/CLM-hunter-szyrmer-1991-kaprost-early-soviet-alternatives.md:30)：全要素生产率外生 +10% 或 +20% 是单独杠杆，对应 +14.1% 或 +25.7%，用来代理清洗与恐怖的效率损失。尾注 `[^6]` 的 10%–20% 与 29.6%–40.1% 不用改。“约三至四成”可以留下，只要不再写成单独扣除被清洗人数。

Target →

`在取消强制集体化、放缓城市化挤占并剔除清洗损耗的联合假设下，1941 年初苏联固定资本存量反可比历史实际高出约三至四成`

Replacement →

`在取消强制集体化、放缓城镇人口增长，并以全要素生产率外生提高 10%–20% 代理清洗与恐怖的效率损失这一联合假设下，1941 年 1 月 1 日固定资本存量可比历史实际的 1,140 亿（1928 年卢布）高出约三至四成（29.6% 至 40.1%）`

### P2-10　第 4 章罢工节没有 `DATA-01`

- 位置：[book_manifest.yaml:167](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:167)
- 依据：第四节写 1912 年后政治罢工与海姆森命题。`DATA-01` 已挂在第 3、5、7 章，第 4 章的 `reference_files` 只有编年与海姆森札记。

Target →

`reference_files` 止于 `reading-notes/late_imperial_fiscal_and_haimson/RN-W61-kotsonis-hoch-plaggenborg-burbank-haimson.md`，无 `DATA-01`。

Replacement →

在该列表补 `data/DATA-01-1905-1917-strikes-and-petrograd-elections.md`。

### P2-11　第 5 章标题止于 1917.02，`era` 止于 1917.03

- 位置：[book_manifest.yaml:196](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:196)、[:198](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:198)
- 依据：二月革命的公历终点在 1917 年 3 月上旬。`era` 已是 `1914.08–1917.03`，第 6 章从 `1917.03` 起。标题 `（1914–1917.02）` 在公历上把本章提前一个月关上。

Target →

`title: "总体战的重压与沙皇政权的瓦解（1914–1917.02）"`

Replacement →

`title: "总体战的重压与沙皇政权的瓦解（1914.08–1917.03）"`

### P2-12　1917 年 12 月落在第 7 章与第 8 章的 `era` 之外

- 位置：[book_manifest.yaml:277](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:277)、[:320](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:320)
- 依据：第 7 章 `era` 为 `1917.08–1917.11`，第 8 章为 `1918.01–1920.11`。契卡法令（公历 1917-12-20）与最高国民经济委员会正式签署（公历 1917-12-15）没有任何一章的时代字段接住。

Target →

`ch08.era: "1918.01–1920.11"`

Replacement →

`ch08.era: "1917.12–1920.11"`

### P2-13　第 8 章红白内战节未挂红色恐怖、民主反革命、波苏战争与兵力表

- 位置：[book_manifest.yaml:330](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:330)
- 依据：第三节写捷克斯洛伐克军团、萨马拉、红色恐怖与契卡；第四节写波苏战争。这三张争鸣卡与 `DATA-05`、`DATA-06` 都在库内。现有 `reference_files` 止于 `DATA-07`，`pack_cards` 只有立宪会议争鸣。

Target →

`reference_files` 末项为 `data/DATA-07-1905-1918-unions-moscow-swings-and-constituent-assembly-votes.md`。

Replacement →

补入：

- `historiography/debates/DEB-1918-red-terror-and-civil-war-origins.md`
- `historiography/debates/DEB-1918-democratic-counterrevolution-third-force.md`
- `historiography/debates/DEB-1920-polish-war-and-revolutionary-export.md`
- `data/DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md`
- `data/DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md`

`pack_cards` 同步补这三张 `DEB-*`。`DATA-06` 已在第 14 章；第 8 章只用它的 1918 年契卡量刑，不把 1929 年集体化冲高写进内战章。

### P2-14　第 9 章 `era` 晚于自己的第一节，且未挂工人与兵力表

- 位置：[book_manifest.yaml:361](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:361)、[:371](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:371)
- 依据：`era` 为 `1918.05–1921.03`。第一节要点与已写正文从 1917 年 11 月工人监督写到 1918 年春的工业崩盘。`DEB-1918-working-class-and-bolsheviks` 与 `DATA-05` 未进 `reference_files`。全稿没有任何一章引用 `DATA-05`。

Target →

`era: "1918.05–1921.03"`，且 `reference_files` 无工人争鸣卡与 `DATA-05`。

Replacement →

`era` 改为 `1917.11–1921.03`。`reference_files` 补：

- `historiography/debates/DEB-1918-working-class-and-bolsheviks.md`
- `data/DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md`

### P2-15　第 10 章格鲁吉亚节未挂民族争鸣卡

- 位置：[book_manifest.yaml:420](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:420)
- 依据：第三节是自治化、格鲁吉亚事件与联盟国家。`DEB-1923-nationality-and-empire` 在库内，未进 `pack_cards` 或 `reference_files`。切尔文节已有 `POL-sokolnikov-chervonets-monetary-reform` 与 `DATA-02`，不必再为索科利尼科夫单补人物卡。

Target →

`reference_files` 末项为 `data/DATA-02-1922-1924-scissors-crisis-and-chervonets.md`。

Replacement →

补 `historiography/debates/DEB-1923-nationality-and-empire.md`，并列入 `pack_cards`。

### P2-16　第 13 章写了沙赫特案与 3 月 20 日方法，两张枢纽卡在第 14 章才出现

- 位置：[book_manifest.yaml:534](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:534)、[:542](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:542)
- 依据：正文有沙赫特审判，也有 1929-03-20 的乌拉尔—西伯利亚方法。`DEB-1928-shakhty-specialist-baiting-and-cultural-revolution` 未进本章。`POL-ural-siberian-method` 只在第 14 章 [book_manifest.yaml:586](C:/Users/lsaax/.t3/projects/russian-revolution-knowledge-base/reader/book_manifest.yaml:586)，而第 14 章 `era` 从 `1929.05` 起，接不住 3 月 20 日。事件卡 `EVT-1928-shakhty-affair-show-trial` 已在 `pack_cards`，缺的是争鸣卡与政策卡。

Target →

`pack_cards` 止于 `MTG-1929-04-cc-joint-plenum`；`reference_files` 止于 `DATA-03`。

Replacement →

`pack_cards` 补 `POL-ural-siberian-method`。`reference_files` 补 `historiography/debates/DEB-1928-shakhty-specialist-baiting-and-cultural-revolution.md` 与 `cards/policies/POL-ural-siberian-method.md`。第 14 章保留该方法卡，供 1929 年夏秋的全国推广使用。
