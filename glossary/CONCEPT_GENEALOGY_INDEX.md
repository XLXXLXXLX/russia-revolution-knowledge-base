# 概念系谱总索引（Concept Genealogy Index）

> **暂缓向量化铁律（AGENTS.md §五）**：本索引与 [`cards/concepts/CON-*`](../cards/concepts/)、[`graph/aliases.yaml`](../graph/aliases.yaml) 共同承担**跨期语义漂移**与**论战反讽引述**的消歧责任。检索或写作前应先读本表分期栏，再运行 `python scripts/kb.py pack <CON-ID>` 编译 1-Hop 上下文包；**严禁**用向量相似度替代时段精读。

**覆盖时段**：1860s（民粹派萌芽）— 1929（斯大林在十一月全会后确立“大转变”路线）；俄历事件在叙事中须双历法标注，本表排序以公历 `date_ns` 为准。

---

## 一、27 核心概念对照总表

| # | 俄语 | 英语惯用译 | 中文标准译 | 已建 `CON-*` / 关联卡 | 首要争鸣 / 政策接口 |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | Совет | Soviet / council | 苏维埃 | `CON-soviet` | `DEB-1917-october-coup-or-social-revolution` |
| 2 | Народничество | Narodnichestvo / populism (careful) | 民粹主义（俄国） | `CON-narodnichestvo` | `DEB-1879-narodnaya-volya-to-bolshevism` |
| 3 | Община / Мир | Commune / mir (village commune) | 农村公社 / 米尔 | `CON-peasant-commune-obshchina` | `DEB-1906-stolypin-wager-and-agrarian-viability` |
| 4 | Учредительное собрание | Constituent Assembly | 立宪会议 | `CON-constituent-assembly`；`EVT-1918-01-constituent-assembly-dispersal` | `DEB-1918-constituent-assembly-and-soviet-democracy` |
| 5 | Демократическая диктатура пролетариата и крестьянства | Democratic dictatorship of proletariat and peasantry | 工农民主专政 | `POL-april-theses-1917`（参 `1905-07_lenin-two-tactics`） | `DEB-1903-bolshevik-menshevik-split` |
| 6 | Перманентная революция | Permanent revolution | 不断革命 | `CON-permanent-revolution` | `DEB-1924-socialism-in-one-country` |
| 7 | Революционное оборончество / пораженчество | Revolutionary defensism & defeatism | 革命护国主义与革命失败主义 | `CON-revolutionary-defensism-and-defeatism` | `DEB-1917-dual-power-and-february-origins` |
| 8 | Двоевластие | Dual power | 双重政权 | `CON-dual-power` | `DEB-1917-dual-power-and-february-origins` |
| 9 | Рабочий контроль | Workers’ control | 工人监督 | `CON-workers-control`；`ORG-factory-committees-1917` | `POL-war-communism`；`CLM-smith-sa-1983-defensive-workers-control` |
| 10 | Военный коммунизм | War Communism | 战时共产主义 | `POL-war-communism` | `DEB-1918-war-communism-ideology-or-emergency` |
| 11 | Продразвёрстка | Surplus-grain appropriation / prodrazvyorstka | 余粮收集制 | `POL-war-communism` | `DEB-1918-war-communism-ideology-or-emergency` |
| 12 | НЭП / Новая экономическая политика | NEP / New Economic Policy | 新经济政策 | `POL-nep` | `DEB-1928-bukharin-alternative` |
| 13 | Государственный капитализм | State capitalism | 国家资本主义 | `CON-state-capitalism` | `DEB-1918-war-communism-ideology-or-emergency`；`DEB-1921-kronstadt-and-nep-origins` |
| 14 | Смычка | Smychka / worker-peasant alliance | 工农联盟（结合） | `CON-smychka` | `DEB-1928-bukharin-alternative` |
| 15 | Ножницы (цен) | Price scissors | 剪刀差 | `EVT-1923-scissors-crisis` | `DEB-1928-bukharin-alternative`；`DATA-02-1922-1924-scissors-crisis-and-chervonets` |
| 16 | Первоначальное социалистическое накопление | Primitive socialist accumulation | 社会主义原始积累 | `CON-primitive-socialist-accumulation` | `DEB-1928-bukharin-alternative` |
| 17 | Социализм в одной стране | Socialism in one country | 一国建成社会主义 | `CON-socialism-in-one-country` | `DEB-1924-socialism-in-one-country` |
| 18 | Демократический централизм | Democratic centralism | 民主集中制与先锋队 | `CON-democratic-centralism-and-vanguard` | `DEB-1903-bolshevik-menshevik-split`；`DEB-1921-trade-union-controversy-and-party-unity` |
| 19 | Номенклатура | Nomenklatura | 官职等级名册制 | `INS-politburo-orgburo-secretariat` | `CLM-khlevniuk-2015-secretariat-and-nomenklatura` |
| 20 | Коренизация | Korenizatsiia / indigenization | 本土化政策 | `POL-korenizatsiia` | `DEB-1923-nationality-and-empire` |
| 21 | Кулак | Kulak | 富农 | `CON-kulak` | `DEB-1929-collectivization-and-dekulakization-causes` |
| 22 | Середняк | Seredniak / middle peasant | 中农 | `CON-kulak`；`DATA-08` | `CLM-lewin-peasants-1968-kulak-myth-and-serednyak` |
| 23 | Правый уклон | Right deviation | 右倾 | `ORG-right-opposition-1928` | `DEB-1928-bukharin-alternative` |
| 24 | Советский Термидор / Бюрократизм | Soviet Thermidor & bureaucracy | 苏维埃热月与官僚主义 | `CON-thermidor-and-bureaucracy`；`PER-ustryalov` | `DEB-1922-lenin-testament-and-stalin-rise` |
| 25 | Великий перелом | Great Break / Great Turn | 大转变 | `EVT-1929-great-turn-and-dekulakization-launch` | `DEB-1929-collectivization-and-dekulakization-causes` |
| 26 | Интеллигенция / «Вехи» / Спецы | Intelligentsia, Vekhi & bourgeois specialists | 知识分子、《路标》与资产阶级专家 | `CON-intelligentsia-and-vekhi` | `DEB-1928-shakhty-specialist-baiting-and-cultural-revolution` |
| 27 | Единый фронт / Третий период / Социал-фашизм | United Front, Third Period & social-fascism | 统一战线、第三时期与社会法西斯论 | `CON-united-front-and-third-period` | `MTG-1928-07-comintern-6th-congress`；`ORG-comintern` |

---

## 二、分期语义裂变矩阵（1860s → 1929）

**图例**：每格为该时段内**主导政治用法**（非普适词典义）；同一格内多义用 `｜` 分隔。空白格表示该词尚未成为公共政治关键词。

| 概念 | 1860s–1904 | 1905–1914 | 1914–1916 | 1917 二月–十月 | 1918–1921 | 1921–1927 | 1927–1929 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **苏维埃** | 偶发工人代表会议（1905） | 1905 革命地方委员会；偶发用法 | 前线士兵委员会萌芽 | **双权力机构**：工兵代表苏维埃 vs 临时政府 | 夺权后国家代表机制｜内战地方苏维埃行政化 | 正式宪制机关名；竞争性政党退出 | 党领导干部垄断化/寡头化；“苏维埃”趋向仪式名 |
| **民粹主义** | 知识分子“走向人民”｜农村社会主义理论 | 社会革命党/劳动解放社谱系 | 战争冲击下社革党“护国”分裂 | 与马克思主义、温和派护国主义并置 | 布尔什维克指控对手“小资产阶级民粹” | 新经济政策论战中“民粹包袱”互骂 | 对抗布哈林“富农路线”的意识形态标签 |
| **村社** | 法制改革与地方自治争论核心 | 斯托雷平改革冲击分配权 | 征兵与收割队动员单元 | 土地指令与农民自我管理想象 | 征粮队与村会（`skhod`）强制摊派战场 | 合作化与中农拉拢的基层单位 | 集体农庄筹建｜富农划界与驱逐的地理单元 |
| **立宪会议** | — | 自由派核心诉求（国家杜马延伸） | 战争强化“代会制”想象 | 全俄民主授权竞赛｜与苏维埃合法性对照 | 1918-01 解散｜剩余代表流亡 | 记忆政治中“民主终结”象征 | 史学公案：选票 vs 社会革命现实 |
| **工农民主专政** | 普列汉诺夫革命阶段论 | 1905 布尔什维克“农民手指”隐喻 | — | 列宁《四月提纲》前旧公式｜革命后迅速让位于无产阶级专政措辞 | 宪法与外交辞令中偶现 | 被“向社会主义过渡”话语取代 | 史书写作 1905–1917 布尔什维克纲领化石 |
| **不断革命** | — | 托洛茨基 1906 结果推论萌芽 | 齐美尔瓦尔德左派 / 革命失败主义派的世界革命期待 | 与“公使们不能结束战争”动员交叉 | 左翼共产主义者反对布列斯特｜第三国际建成 | 反对派反对“一国”路线 | 1927 后托洛茨基被逐，词成为清洗标签 |
| **革命护国主义** | — | — | 孟什维克/社革党主流（`CLM-galili-1989-revolutionary-defensism`） | 苏维埃与临时政府战争口号公约数 | 布列斯特和约撕裂左派社革党 | 退入史学与托派批判 | — |
| **双重政权** | — | — | — | **1917 结构性并存**（非 1918 后法律术语） | 托洛茨基史学理论化（阶级两政府） | 回忆录与史学模型 | 切忌外推至全俄均势 |
| **工人监督** | — | 工厂委员会萌芽 | 军工区监督实践 | 临时政府条例 vs 工厂委员会夺权 | 与企业国有化、一家经营管理并轨 | 新经济政策下削弱｜“建设社会主义”再提 | 计件与突击制下名存实亡 |
| **战时共产主义** | — | — | — | 个别措施先行（国有化浪潮） | **1918–1921 政策簇**；1921 年事后追赋（retrospective）标签 | 斯大林时期史学＝“实验乌托邦” | 与“大转变”对比的“第一次冒进”叙事 |
| **余粮收集制** | — | — | — | 公平分配争论 | **1918–1921 强制摊派**（`prodrazvyorstka`） | 新经济政策 `prodnalog` 取代 | 乌拉尔-西伯利亚方法＝征粮逻辑残留 |
| **新经济政策** | — | — | — | — | 1921 十大宣布“退却” | **市场-合作社混合体制** | 1927–28 收购危机｜非常措施侵蚀 |
| **国家资本主义** | — | 托洛茨基“监督资本主义” | — | 列宁 April–1918：**无产阶级国家规训资本** | 布哈林与列宁短暂和解话术 | 被“向社会主义过渡”替代 | 西方马克思主义对苏联官僚的批判性挪用 |
| **工农联盟（смычка）** | — | — | 战时农村联盟宣传 | “自愿联合” vs 粮食恐怖张力 | 征粮与乡村战争撕裂联盟修辞 | 布哈林“骑在农民背上工业化”辩论 | 联盟修辞让位于“消灭富农阶级” |
| **剪刀差** | — | — | — | — | 他山统计术语引入迟缓 | **工业品贵、粮价相对低**（`DATA-02-1922-1924-scissors-crisis-and-chervonets`） | 布哈林批判加剧｜加速原始积累争论 |
| **社会主义原始积累** | — | — | — | — | 普列奥布拉任斯基 **1924–26 理论战** | 与布哈林“蜗牛般速度”对撞 | 1928 后成为强制集体化正当化话语 |
| **一国建成社会主义** | — | — | — | 世界革命期待仍占上风 | 布列斯特后思辨 | **1924–27 斯大林-托洛茨基论战高峰** | 写入党章｜反对派被告外国代理人 |
| **民主集中制** | — | 1905–06 公式（广泛讨论+执行统一） | — | 党内临时开放与七月纪律 | 十月后指挥链收紧｜**1921 十大禁派别** | 干部自下而上选举名存实亡 | 与官职名册制捆绑 |
| **官职名册制** | — | — | — | 干部指派萌芽 | 契卡-党内任命扩展 | 书记处集中人事权（`CLM-khlevniuk-2015-secretariat-and-nomenklatura`） | 1929 干部大换血与集体化督阵 |
| **本土化** | — | — | — | 边疆民族自决许诺 | 沙俄帝国遗产再编 | **1923 十二大系统化（korenizatsiia）** | 1928–29 俄罗斯化回摆与清洗 |
| **富农（кулак）** | — | 统计-社会学富农户（德语借贷） | — | “播户”与粮食投机者混称 | **阶级敌人**｜农村的资本主义代表 | 新经济政策宽容**勤劳富裕农民** | **1929“消灭富农阶级”**｜政治划界大于统计 |
| **中农** | — | 村社分配中间层 | — | “迟钝多数”动员对象 | 征粮优待与摊派焦点 | 布哈林联盟核心｜合作化依靠对象 | 被迫入社｜“看风使舵”污名化 |
| **右倾** | — | 孟什维克右翼统一派 | — | — | 工人反对派｜“左派”标签更常见 | **1928 布哈林集团**＝右倾代名词 | 清洗话语标准化 |
| **苏维埃热月** | — | — | — | — | — | 托洛茨基论 **1921 新经济政策=热月**：革命纪律退潮｜官僚再生产 | 西方托派史学延伸；苏联官方拒斥 |
| **大转变** | — | — | — | — | — | 1926 个别预言 | **1929 秋**斯大林话语：从新经济政策到五年计划强制轨；collectivization & dekulakization |

---

## 三、反讽引述与常见误读排雷总表

| 概念 | 典型误读 / 后设投射 | 当时人实际用法线索 | 排雷动作 |
| :--- | :--- | :--- | :--- |
| 苏维埃 | 将 1917 苏维埃等同于后来一党国家议会 | 1905/1917 多党竞争代表机构；术语意为“会议” | 分时区分 `CON-soviet` 四阶段；禁 1924 宪法回溯 1917 |
| 民粹主义 | 英文 populism 套入反精英选民动员 | 指俄国知识界—农村社会主义思潮谱系 | 用 `CON-narodnichestvo`；社革党≠ generic populists |
| 村社 | 浪漫化“原始社会主义” | 义务摊派、户籍、税费与当兵单位 | 区分 **mir/община** 与集体农庄（`kolkhoz`） |
| 立宪会议 | 把 1917-11 选票当作十月后政策公投 | 名单在分裂前制定；农民社革党多数 | 见 `DEB-1918-constituent-assembly-and-soviet-democracy` |
| 工农民主专政 | 当作 1917–18 实际宪法标题 | 1918 后迅速为 **无产阶级专政** 取代 | 标为 **1905–1917 纲领公式**，勿写实际政体名 |
| 不断革命 | 当作托洛茨基 1917 公开夺权口号 | 1906 预测与 1920s 反对派论战构件 | 分 **1905–07 理论 / 1917 实践 / 1924–27 论战** 三层 |
| 革命护国主义 | 当作布尔什维克 4 月前立场 | 孟什维克/社革党 **1914–17** 主流自卫战争论 | 布尔什维克早期反战；4 月后“革命防御”分化 |
| 双重政权 | 外推至省县机械均势 | 托洛茨基 **分析范畴** + 1917 彼得格勒经验 | 见 `DEB-1917-dual-power-and-february-origins` |
| 工人监督 | 等同工人政权或全面国有化 | 1917–18 **账目/供货监督**，非普遍自我管理 | 对照 `CLM-smith-sa-1983-defensive-workers-control` 与 `CLM-smith-1983-workers-control-pragmatism` |
| 战时共产主义 | 当作 1918 列宁既定总蓝图名 | **1921 年** retrospective 标签；措施分批演进 | `DEB-1918-war-communism-ideology-or-emergency` |
| 余粮收集制 | 与 1929 统购统销混为一谈 | **1918–21 `prodrazvyorstka`**；1921 后为 `prodnalog` | 挂钩 `POL-war-communism`，禁外延至集体化 |
| 新经济政策 | “恢复资本主义”=背叛社会主义（斯大林后设） | 列宁 **国家调控市场** 过渡论 | `POL-nep` + 布哈林 debates |
| 国家资本主义 | 用后来官僚国家一语概括 1918 列宁 | 1918 **雇工+无产阶级国家租让** 特定公式 | `CON-state-capitalism` 分期栏 |
| 工农联盟 | 当作永远和谐的执政神话 | **смычка**＝策略性联盟修辞，内战期多次破裂 | `CON-smychka`；征粮档案 |
| 剪刀差 | 当作单一固定比率 | 相对 **工农产品价格趋势**；统计构建争议 | `DATA-02-1922-1924-scissors-crisis-and-chervonets`；Erlich/Carr-Davies |
| 社会主义原始积累 | 当作 1928 斯大林发明 | 普列奥布拉任斯基 **1924–26** 论战术语 | `CON-primitive-socialist-accumulation` |
| 一国建成社会主义 | 当作 1917 十月目标 | **1924 后** 正式论战口号 | `CON-socialism-in-one-country` |
| 民主集中制 | 用 1921 禁派别回溯证明 1903 分裂必然 | 1906 公式含 **选举与批评** | `CON-democratic-centralism-and-vanguard` |
| 官职名册制 | 当作 1917 即成熟制度 | 1920s 书记处 **人事权集中** 渐进结晶 | Khlevniuk；勿前推到契卡时代全称 |
| 本土化 | 等同于后来 Russification 否定边疆 | **1923–27** 民族干部与文化政策 | `POL-korenizatsiia`；格鲁吉亚事件 |
| 富农 | 用苏联 1929 标准套 1917 农村 | 术语 **贷款词 ku'laq**；统计 vs 政治划界 | `CLM-lewin-peasants-1968-kulak-myth-and-serednyak` |
| 中农 | 当作天然布尔什维克盟友 | **середняк** 在征粮中承受最大压力 | 与富农划界同步考察 |
| 右倾 | 把一切党内批评统称右倾 | 1928 后 **专指布哈林路线** | 1921 工人反对派是“左”非“右” |
| 苏维埃热月 | 当作党史官方分期 | 托洛茨基 **马克思主义史学隐喻**（1793） | 新经济政策退却≠热月政变史实类比 |
| 大转变 | 把 1928 收购战等同于已集体化 | **velikiy perelom** 多见于 **1929–30 话语** | `CLM-davies-1980-autumn-1929-great-turn-fabrication` |

---

## 四、维护与扩展规程

1. **新建概念系谱卡**：当某概念在 ≥3 个时段出现不可通约语义时，在 `cards/concepts/` 建档并在上表“建议 CON-*”栏回填链接。
2. **别名**：人名、党名、旧译统一写入 `graph/aliases.yaml`，本表只保留概念层译名。
3. **引述标注**：论战文本中的反讽（如互相指责“民粹派”“波拿巴主义/伯恩施坦主义”）须在 `CLM-*` 中保留俄文原词并关联本表行号。
4. **与向量检索关系**：本阶段 **禁止** 用语义检索替代本索引时段栏；待 glossary 与 `edges.jsonl` 成熟期再评估向量化（见 AGENTS.md）。

*最后更新：2026-11-18（graph-curator 初建）*