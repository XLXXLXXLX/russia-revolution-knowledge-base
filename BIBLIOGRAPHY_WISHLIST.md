# 待寻电子书与一手文献需求清单（Bibliography Wishlist）

> **最新盘点状态（2026-11-18）**：
> - 您已向 [`inbox/`](./inbox/) 投递 **205 个文献文件（共 4.24 GB）**！原始二进制大文件已在 `.gitignore` 中排除以免撑爆 Git 仓库，文件元数据清单由 Git 追踪在 [`sources/inbox_inventory.jsonl`](./sources/inbox_inventory.jsonl)。
> - 首批 27 项核心书单中，**高达 25 项（含大量中英文双版本！）已成功命中并进入 `inbox/`** 🎉！
> - **当前仅剩 3 项缺口待寻**：
>   1. `BIB-006`：Abraham Ascher, *The Revolution of 1905* (Vol. 1 & 2)（阿舍尔两卷本《1905年俄国革命》，已完成中译本规范拆解：[`sources/primary/trotsky_1905_zh/`](./sources/primary/trotsky_1905_zh/)；仍缺西方现代综合专著对照）；
>   2. `BIB-022`：*Как ломали НЭП. Стенограммы пленумов ЦК ВКП(б) 1928–1929 гг.*（5卷本俄文解密档案：《新经济政策是如何被打破的：1928–1929年联共（布）中央全会速记记录》，目前 `inbox/` 已有丹尼洛夫主编姊妹篇《苏联农村的悲剧》第2卷 1929.11–1930.12）；
>   3. `BIB-023b`：Stephen Kotkin, *Stalin, Vol. II: Waiting for Hitler, 1929–1941*（科特金《斯大林》第2卷，覆盖 1929 年四月与十一月全会收官；第1卷 `1878–1928` 已在 `inbox/` 中）。

---

## 本次规范提取登记（2026-11-18）

以下六份来源均已完成分章 Markdown、`toc.md` 与书目 `manifest.yaml`。库存检查显示它们已存在于 `sources/inbox_inventory.jsonl`（该文件当前有 205 条记录），因此未重复追加。

| 文献 | 规范化目录 | 书目核验备注 |
| :--- | :--- | :--- |
| 拉比诺维奇，《布尔什维克当权》 | [`rabinowitch_2007_bolsheviks_in_power_zh`](./sources/monographs/rabinowitch_2007_bolsheviks_in_power_zh/) | EPUB 实际为俄文文本；2007 年英文原版 |
| 多伊彻，《先知三部曲》 | [`deutscher_prophet_trilogy_zh`](./sources/monographs/deutscher_prophet_trilogy_zh/) | 三卷原版年份 1954、1959、1963；中文 EPUB 未载版权页版次 |
| 托洛茨基，《1905》中文译校本 | [`trotsky_1905_zh`](./sources/primary/trotsky_1905_zh/) | 扉页署 Uni 佐仓绫奈译校；文件未标现代译本出版项；3 页无文本层 |
| Steve A. Smith, “Workers, the Intelligentsia and Marxist Parties” | [`zelnik_1999_workers_intelligentsia_marxist_parties`](./sources/monographs/zelnik_1999_workers_intelligentsia_marxist_parties/) | 原 PDF 核实为 1996 年期刊论文（非 Zelnik 著作）；目录沿用指定路径 |
| Siegelbaum 与 Suny 编，《Making Workers Soviet》 | [`siegelbaum_suny_1994_making_workers_soviet_zh`](./sources/monographs/siegelbaum_suny_1994_making_workers_soviet_zh/) | Cornell University Press 1994 年英文版；7 页无文本层 |
| 泽姆斯科夫，《斯大林时代》 | [`stalin_era_economy_repression_1924_1954_zh`](./sources/monographs/stalin_era_economy_repression_1924_1954_zh/) | 俄文原版 2018；中文文件标注老胡译、2024 年 6 月校对 |

---

## 一、早期民粹派、马克思主义传入与政党形成（1860s–1904）

| 编号 | 优先级 | 常用中文书名/译名 | 原书名 / 检索名 | 作者 | 状态 / `inbox/` 对应文件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `BIB-001` | 🔴 P0 | 《革命的根源：19世纪俄国民粹派与社会主义运动史》 | *Roots of Revolution* | Franco Venturi | 📥 **已在 inbox**（`Roots of Revolution A History of the Populist... (Franco Venturi).pdf`） |
| `BIB-002` | 🟠 P1 | 《资本主义论战：俄国民粹派社会哲学研究》 | *The Controversy over Capitalism* | Andrzej Walicki | 📥 **已在 inbox**（`The controversy over capitalism... (Walicki, Andrzej).pdf`） |
| `BIB-003` | 🔴 P0 | 《俄国马克思主义者与布尔什维主义的起源》 | *The Russian Marxists and the Origins of Bolshevism* | Leopold H. Haimson | 📥 **已在 inbox**（`Russian Marxists and the Origins of Bolshevism (Leopold H. Haimson).pdf`，另附海姆森访谈录 *The Making of Three Russian Revolutionaries* 及 Lars Lih *Lenin Rediscovered* 中英双版） |
| `BIB-004` | 🟠 P1 | 《马尔托夫：一位俄国社会民主党人的政治传记》 | *Martov: A Political Biography* | Israel Getzler | 📥 **已在 inbox**（`Martov a political biography... (Getzler, Israel).pdf`，另附 *Martov and Zinoviev: Head to Head in Halle*） |
| `BIB-005` | 🟠 P1 | 《一战前的俄国社会革命党》及相关社革党专著 | *The Russian Socialist Revolutionary Party Before WWI* | Manfred Hildermeier 等 | 🌓 **主体已在 inbox，待补 Scott Smith (2011)**（已有 `Hildermeier.epub` + `俄国社会革命党研究1901-1925.pdf` + Elizabeth White 专著；经扉页核实 `锤击镰刀.pdf` 真身为 Oliver H. Radkey 1963 *The Sickle under the Hammer*，待补寻 Scott B. Smith, *Captives of Revolution*, 2011） |

---

## 二、1905年革命、立宪试验与帝国晚期危机（1905–1916）

| 编号 | 优先级 | 常用中文书名/译名 | 原书名 / 检索名 | 作者 | 状态 / `inbox/` 对应文件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `BIB-006` | 🔴 P0 | 《1905年俄国革命》（上下两卷） | *The Revolution of 1905: Russia in Disarray* & *Authority Restored* | Abraham Ascher | ⏳ **待寻找** *(注：`inbox/` 已有托洛茨基《1905》两个中译本及 Victoria Bonnell 1900–1914 劳工组织专著)* |
| `BIB-007` | 🟠 P1 | 《俄国的革命经验（1905–1917）》 | *Russia's Revolutionary Experience, 1905–1917: Two Essays* | Leopold H. Haimson | 📥 **已在 inbox**（`Russias Revolutionary Experience, 1905-1917 Two Essays (Leopold H. Haimson...).pdf`） |

---

## 三、1917年革命：从二月到十月的多视角显微镜（1917）

| 编号 | 优先级 | 常用中文书名/译名 | 原书名 / 检索名 | 作者 | 状态 / `inbox/` 对应文件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `BIB-008` | 🔴 P0 | 《1917年彼得格勒二月革命》 | *The February Revolution, Petrograd, 1917* | Tsuyoshi Hasegawa | 📥 **已在 inbox**（1981版与新版双本齐备：`The February Revolution, Petrograd, 1917... (Hasegawa Tsuyoshi).pdf`） |
| `BIB-009` | 🔴 P0 | 《革命前奏》与《布尔什维克掌权》 | *Prelude to Revolution* & *The Bolsheviks Come to Power* | Alexander Rabinowitch | 📥 **已在 inbox**（`革命的前奏...Prelude to Revolution.pdf` + `布尔什维克掌权1917年彼得格勒革命.epub`） |
| `BIB-010` | 🔴 P0 | 《俄国革命史》（全三卷） | *The History of the Russian Revolution* | Leon Trotsky | 📥 **已在 inbox**（`俄国革命史（全三卷） (托洛茨基).epub`） |
| `BIB-011` | 🟠 P1 | 《1917年俄国革命：个人札记》 | *The Russian Revolution 1917: A Personal Record* | N. N. Sukhanov | 📥 **已在 inbox**（`The Russian Revolution 1917 A Personal Record by N.N. Sukhanov.pdf`） |
| `BIB-012` | 🟠 P1 | 《俄国革命》 | *The Russian Revolution* | Richard Pipes | 📥 **已在 inbox**（`The Russian Revolution (Richard Pipes).epub`） |
| `BIB-013` | 🟠 P1 | 《红色彼得格勒：工厂中的革命，1917–1918》 | *Red Petrograd: Revolution in the Factories, 1917–1918* | S. A. Smith | 📥 **已在 inbox**（英文原版 `Red Petrograd...pdf` + 中文版 `红色彼得格勒：工厂中的革命，1917-18.pdf`，另附科恩克尔《莫斯科工人和1917年革命》） |
| `BIB-014` | 🔵 P2 | 《人民的悲剧：俄国革命 1891–1924》 | *A People's Tragedy: The Russian Revolution 1891–1924* | Orlando Figes | 📥 **已在 inbox**（`A peoples tragedy the Russian Revolution 1891-1924 (Figes, Orlando).epub`） |

---

## 四、内战、战时共产主义与党内早期反对派（1918–1923）

| 编号 | 优先级 | 常用中文书名/译名 | 原书名 / 检索名 | 作者 | 状态 / `inbox/` 对应文件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `BIB-015` | 🟠 P1 | 《布尔什维克执政：彼得格勒苏维埃政权第一年》 | *The Bolsheviks in Power* | Alexander Rabinowitch | 📚 **已规范拆解**（英文原版 PDF 另有收存；本次 EPUB 实际为俄文文本，见 [`rabinowitch_2007_bolsheviks_in_power_zh`](./sources/monographs/rabinowitch_2007_bolsheviks_in_power_zh/)） |
| `BIB-016` | 🟠 P1 | 《俄国内战》 | *The Russian Civil War* | Evan Mawdsley | 📥 **已在 inbox**（英文原版 `The Russian Civil War (Evan...pdf` + 中文版 `俄国内战 Evan Mawdsley.pdf`） |
| `BIB-017` | 🔴 P0 | 《革命的良心：苏维埃俄国的共产主义反对派》 | *The Conscience of the Revolution* | Robert V. Daniels | 📥 **已在 inbox**（`The conscience of the revolution Communist opposition in Soviet Russia (Daniels).pdf`，另附柯伦泰 *The Workers' Opposition*） |
| `BIB-018` | 🟠 P1 | 《1921年喀琅施塔得》 | *Kronstadt, 1921* | Paul Avrich | 📥 **已在 inbox**（`Kronstadt, 1921 (Paul Avrich).pdf`） |
| `BIB-019` | 🔴 P0 | 《列宁的最后斗争》 | *Lenin's Last Struggle* | Moshe Lewin | 📥 **已在 inbox**（`Lenins Last Struggle.epub`） |

---

## 五、新经济政策、工业化大论战与斯大林击败布哈林（1921–1929）

| 编号 | 优先级 | 常用中文书名/译名 | 原书名 / 检索名 | 作者 | 状态 / `inbox/` 对应文件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `BIB-020` | 🔴 P0 | 《布哈林与布尔什维克革命：政治传记（1888–1938）》 | *Bukharin and the Bolshevik Revolution* | Stephen F. Cohen | 📥 **已在 inbox**（`Bukharin and the Bolshevik Revolution... (Stephen F. Cohen).pdf`） |
| `BIB-021` | 🔴 P0 | 《俄国农民与苏维埃政权：集体化研究》 | *Russian Peasants and Soviet Power* | Moshe Lewin | 📥 **已在 inbox**（`Russian Peasants and Soviet Power... (Moshe Lewin).pdf`） |
| `BIB-022` | 🔴 P0 | 《新经济政策是如何被打破的：1928–1929年联共（布）中央全会速记记录》（5卷本） | *Как ломали НЭП. Стенограммы пленумов ЦК ВКП(б) 1928–1929 гг.* | В. П. Данилов, О. В. Хлевнюк 编 | ⏳ **待寻找** *(最硬核俄文一手全会速记档案；目前 `inbox/` 已有同系列后续卷《苏联农村的悲剧》第2卷 1929.11–1930.12)* |
| `BIB-023` | 🔴 P0 | 《斯大林（第1卷：权力的悖论 1878–1928；第2卷：等待希特勒 1929–1941）》 | *Stalin, Vol. I & Vol. II* | Stephen Kotkin | 🌓 **第1卷已在 inbox，待补第2卷**（已有 `Stalin, Volume 1 Paradoxes of Power, 1878–1928.epub`；1929年决战下半场在第2卷开篇） |
| `BIB-024` | 🔴 P0 | 《先知三部曲（武装的先知 / 被解除武装的先知 / 流亡的先知）》 | *The Prophet Armed / Unarmed / Outcast* | Isaac Deutscher | 📚 **已规范拆解**（本次套装 EPUB：[`deutscher_prophet_trilogy_zh`](./sources/monographs/deutscher_prophet_trilogy_zh/)；另有全新插图修订本） |
| `BIB-025` | 🟠 P1 | 《苏联工业化大论战（1924–1928）》 | *The Soviet Industrialization Debate, 1924–1928* | Alexander Erlich | 📥 **已在 inbox**（`The Soviet Industrialization Debate, 1924–1928 (Alexander Erlich).pdf`，另附普列奥布拉任斯基《新经济学》与《平衡与非平衡》） |
| `BIB-026` | 🟠 P1 | 《苏维埃俄国史（含过渡期 1923–24、一国社会主义 1924–26、计划经济基础 1926–29）》 | *A History of Soviet Russia* (14 vols.) | E. H. Carr & R. W. Davies | 🌓 **大部分已在 inbox，待补缺卷**（已有《布尔什维克革命》1–3卷中英本 + `The Interregnum` + `Foundations Vol. 1-I & Vol. 3-II` + 1979总括本；经扉页核实 `A History of Soviet Russia.epub` 仅为第2卷扫描版，待补寻 *Socialism in One Country, 1924–1926* Vols. 1–3 与 *Foundations* Vol. 2 / Vol. 3-I & III） |
| `BIB-027` | 🟠 P1 | 《斯大林：独裁者新传》 | *Stalin: New Biography of a Dictator* | Oleg V. Khlevniuk | 📥 **已在 inbox**（`Stalin New Biography of a Dictator (Oleg V. Khlevniuk).epub`，另附阿帕利科夫《联共(布)党内斗争》、梅里代尔《莫斯科政治与斯大林崛起 1925–32》） |
| `BIB-028` | 🔵 P2 | 《列宁政治生涯（第二、三卷）》 | *Lenin: A Political Life, Vols. 2–3* | Robert Service | ⏳ **待寻找**（第1卷 `1870–1910.01` 已在 `inbox/`，覆盖 1910–1924 的第2–3卷待补，目前已有洛吉诺夫《列宁全传》互补） |
