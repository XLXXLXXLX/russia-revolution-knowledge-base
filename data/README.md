# 社会经济与政治定量微序列库（`data/`）

本目录用于存放支撑或检验史学论断的定量时间序列（Markdown 表格或 CSV/JSON，必须附精确出处、统计分母、采样时点与口径警示），涵盖：
- 1905–1917 两京罢工人次、行业工会密度、莫斯科/彼得格勒选举与全俄立宪会议多口径得票；
- 1917–1929 工业工人构成、内战兵力、契卡—OGPU 司法外镇压、工农业价格“剪刀差”与切尔文币制、粮食收购与涅姆奇诺夫表、党建与表决；
- 1921–1929 NEP 城乡阶层、登记失业、女工与家政工劳动、职员构成及 *ФУБР* 工业家长制指标。

## 目录索引表（`DATA-01` 至 `DATA-08`）

| 序列编号 | 文件与核心主题 | 时间跨度 | 核心定量序列 / 指标 | 主要文献口径 | 关键口径警示与缺口 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`DATA-01`** | [`DATA-01-1905-1917-strikes-and-petrograd-elections.md`](DATA-01-1905-1917-strikes-and-petrograd-elections.md) | `1905–1917.12` | 1905 首都与铁路罢工节点；1917-02 彼得格勒四口径逐日罢工；5–6 月 12 区杜马与苏维埃改选；全俄立宪会议总票结构 | Hasegawa (2018)、Galili (1989)、Trotsky《1905》、Figes / Haimson / Koenker | **严禁**将 1917-02-23/24 巴尔克约计与含闭厂普梯洛夫工人的列伊别罗夫重构首尾焊接；缺 1905-10 警察逐日罢工表 |
| **`DATA-02`** | [`DATA-02-1922-1924-scissors-crisis-and-chervonets.md`](DATA-02-1922-1924-scissors-crisis-and-chervonets.md) | `1922.09–1924.01` | 工农业相对价格“剪刀差”锚点（1913=100）；切尔沃涅茨（*chervonets*）发行与货币稳定对比 | Carr (1954)、茹科夫《新经济政策的另一面》 | 仅含锚点与政策月，无逐月六列零售/批发完整连续表；区分银行券流通与极少量铸造金币 |
| **`DATA-03`** | [`DATA-03-1926-1929-grain-procurement-and-nemchinov-table.md`](DATA-03-1926-1929-grain-procurement-and-nemchinov-table.md) | `1926–1929` | 斯大林 1928-05-28 所引涅姆奇诺夫表（战前 vs 1926/27 产粮/商品粮）；国家收购波动与 Carr–Davies 校正 | 斯大林《在粮食战线上》（S 级）、Carr & Davies (1969)、Nove (1964) | 严禁混同农业年度前 9 个月累计收购与 12 个月全年度量；涅姆奇诺夫表仅计运出农村部分并混用战前粗估 |
| **`DATA-04`** | [`DATA-04-party-membership-and-congress-votes-1903-1929.md`](DATA-04-party-membership-and-congress-votes-1903-1929.md) | `1903–1929` | 1903 二大党章第 1 条表决；1917–1929 党员总数、阶级构成、历次党代会关键表决与反对派联署（如 1923-10-15《四十六人声明》） | `WB-W3`、Haimson、Daniels、Carr、Rabinowitch、Pipes、Zhukov | 区分“重新登记后”与会议时点党员口径；1883 日内瓦与 1918-02-14 后仅标单公历 |
| **`DATA-05`** | [`DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md`](DATA-05-1917-1920-factory-demographics-and-civil-war-forces.md) | `1917–1920` | 1917 彼得格勒工厂工人总量、行业与技能结构、工人监督覆盖；内战苏维埃腹地—红军在册兵力/一线战力、武器库存与铁路机动 | S. A. Smith (1983)、Mawdsley (1987)、Kakurin (1928) | 区分“城市工人”与“含郊区”、Strumilin 1918 技能表 vs 1917 产业比、红军“在册总兵力” vs “一线刺刀马刀” |
| **`DATA-06`** | [`DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md`](DATA-06-1918-1929-cheka-ogpu-sentencing-and-1929-collectivization-surge.md) | `1918–1930` | 契卡 1918–1921 处决（34/35 省下限与 5 万上限）；1924–1925 OGPU vs 省法院移送与死刑率；1926–1929 逮捕与 1929 集体化/征粮跃升 | 莫佐欣 ЦА ФСБ (2006/2011)、《苏联农村的悲剧》、Davies (1980) | VChK 34–35 省汇总漏计克里米亚/喀琅施塔得；法院分母为全案定罪 vs OGPU 按条款结案；区分农户% 与“区”达标率 |
| **`DATA-07`** | [`DATA-07-1905-1918-unions-moscow-swings-and-constituent-assembly-votes.md`](DATA-07-1905-1918-unions-moscow-swings-and-constituent-assembly-votes.md) | `1905–1918.01` | 1906–1907 两京手艺工匠 vs 大厂工会密度与 1912–1914 布尔什维克夺权；1917 莫斯科罢工倾向指数与三次选举摇摆（含 `r` 值）；全俄立宪会议多口径总票/席位/两京与战线对照 | Bonnell (1983)、Koenker (1981)、Radkey (1989) / Rabinowitch (2007)、普罗塔索夫 (1997) 经姚海、Figes / Haimson / 黑宫 | 1906–07 密度用 1897/1900/1902 旧普查且多数工会缴费率 `≤1/6`；莫斯科 6 月市杜马 7 党（`58%`）vs 4 党（`61%`）分母微差；SR 合一选票未分左右派 |
| **`DATA-08`** | [`DATA-08-1921-1929-nep-social-classes-unemployment-and-gender-labor.md`](DATA-08-1921-1929-nep-social-classes-unemployment-and-gender-labor.md) | `1921–1929` | Lewin 1927 税务中农（1,430 万户）/富农与产粮比；Filtzer 1922–29 登记失业与罢工衰减；Goldman 女工失业（表 7/8）、托幼萎缩（`1.8%`）与莫斯科离婚率；Klots 1926 家政工（452,258）与 *Narpit*；Orlovsky 职员、Schapiro/Wiles 党化与十分位比（`3.8`）、Lebsky 拥地率与 *ФУБР* | Lewin (1968)、Filtzer (1986)、Goldman (1993)、Klots (2024)、Orlovsky (1994)、Schapiro/Wiles (1981)、Lebsky (2021)、Rittersporn (1994) | 职业介绍所登记漏计 84% 未务工求职女性且 1924-07 清册断层；1929 女性失业 `45%`（年中）vs `49.9%`（7 月）双口径；区分全苏 2,560 万农户 vs 1,430 万中农；*Narpit* 会员占城市 318,770 人而非全苏 452,258 人 |

## 通用校验铁律
1. **历法规则**：`1918-02-14` 改历前俄国本土日期一律并列 `[O.S.] / [N.S.]`（1900–1918.01 固定加 13 日）；改历后及西欧流亡地事件仅标单公历 `[N.S.]`。
2. **禁止焊接与越界**：竞争性统计口径必须分列，严禁将不同边界或不同基期数据首尾拼成单一区间；涉及 1930 年代初“大转变”数据仅可作 1929 年底结构对照，并须显式声明越界边界。

