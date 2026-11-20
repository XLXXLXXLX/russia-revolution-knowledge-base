# 俄国革命知识库 Benchmark 评测报告 (`v0_pre_refactor`)

- **评测时间**: `2026-11-19T23:21:56+08:00`
- **评测集划分 (`split`)**: `all`
- **Git HEAD**: `ce5a236` (工作区变更文件数: `109`)

## 一、五大套件总览记分板

| 套件 | 状态 | 核心指标摘要 |
| :--- | :---: | :--- |
| **B1 图谱/元数据/历法保真** | ❌ FAIL | YAML保真 `83.3%` (失真 `97`) · 多时段边保留 `0.0%` · 2.2边同步率 `62.8%` · 悬空目标 `3` · CLM->SCH外键 `74.1%` · 改历后误标 `1` |
| **B2 上下文预算与零盲区召回** | ❌ FAIL | 预算达标率 `30.0%` · `B2-01`三枢纽字符数 `199,233` · 一跳邻居最低召回 `94.3%` · 边缘人物金丝雀召回 `92.5%` · T1字数合规 `99.0%` |
| **B3 145本章节雷达与空书隔离** | ❌ FAIL | `locate-chapters`已实现 `False` · Hit@3 `0.0%` · Hit@5 `0.0%` · MRR `0.000` · 纯扫描空书隔离率 `69.2%` (`13` 本检出) |
| **B4 跨家族对抗史实金丝雀** | ❌ FAIL | 总题数 `36` (`B4A=18`, `B4B=18`) · 卡片字面陷阱清零率 `97.2%` · 目标卡多元定稿率 `100.0%` |
| **B5 模态A讲史散文就绪度** | ❌ FAIL | 题库 `12` 道 · 推荐包均值 `189,898` 字符 · 超 80k 字符过载题数 `12` |

## 二、关键诊断样本（Top Defects Exposed by Benchmark）

- **YAML 元数据解析失真样本** (`8` 条展示): `CON-constituent-assembly (dates.start_ns: kb='"1879-08-27" # 1879-08-15 [O.S.] / 1879-08-27 [N.S.] 土地与自由社正式分裂、民意党成立并将自由普选立宪会议确立为俄国革命派核心纲领诉求' != yaml='1879-08-27'; dates.end_ns: kb='"1918-11-18" # 1918-11-18 [N.S.，改历后] 高尔察克鄂木斯克政变推翻全俄临时政府并逮捕前立宪会议委员，终结立宪会议作为独立政权旗帜的历史周期' != yaml='1918-11-18')`, `CON-democratic-centralism-and-vanguard (dates.start_ns: kb='"1875-01-01" # 特卡乔夫《警钟》（Набат）1875年创刊、鼓吹“自觉少数”夺权；年内具体日期为占位值，待核' != yaml='1875-01-01'; dates.end_ns: kb='"1929-12-31" # 以1929年右派反对派失利为研究期界；任命制对民主原则的影响属于制度史解释' != yaml='1929-12-31')`, `CON-dual-power (dates.start_ns: kb='"1905-10-26" # 1905-10-13 [O.S.] / 1905-10-26 [N.S.] 圣彼得堡工人代表苏维埃成立，构成革命委员会与旧国家机器并存的制度原型' != yaml='1905-10-26'; dates.end_ns: kb='"1917-11-07" # 1917-10-25 [O.S.] / 1917-11-07 [N.S.] 十月武装起义推翻临时政府，结束二月以来政府与苏维埃并立周期（狭义制度并立止于七月事件后）' != yaml='1917-11-07')`, `CON-intelligentsia-and-vekhi (dates.start_ns: kb='"1868-01-01" # 1860年代平民知识分子（разночинцы）崛起，1868–1869年拉夫罗夫发表《历史信札》确立“批判思维的个人”伦理范式' != yaml='1868-01-01'; dates.end_ns: kb='"1931-06-23" # 经1909《路标》、1918–1927“资产阶级专家”妥协、1922“哲学船”驱逐与1928沙赫特案及“大提拔（выдвижение）”，至一五计划中后期苏维埃技术知识分子成形' != yaml='1931-06-23')`, `CON-kulak (dates.start_ns: kb='"1870-01-01" # 1870年代民粹派乡村调查与政论将村社贬词 кулак / мироед 引入俄国革命话语；具体日期为年代占位值，待核' != yaml='1870-01-01'; dates.end_ns: kb='"1930-01-30" # 1929-12-27斯大林公开宣布“把富农作为阶级消灭”，1930-01-30联共（布）中央政治局决议定型三类处置配额，完成概念向国家清洗标签的终极转化' != yaml='1930-01-30')`
- **卡片 2.2 悬空目标 ID** (`3` 条展示): `EVT-1922-sr-show-trial -> PER-gotz`, `MTG-1923-04-12th-party-congress -> EVT-1922-georgian-affair`, `PER-tsereteli -> PER-martov`
- **卡片 2.2 未同步至 edges.jsonl 样本** (`8` 条展示): `CON-narodnichestvo -> ORG-narodnaya-volya (1879–1887)`, `CON-narodnichestvo -> ORG-chernyi-peredel (1879起)`, `CON-smychka -> POL-nep (1921–1929)`, `CON-smychka -> PER-bukharin (1925–1929)`, `CON-smychka -> PER-preobrazhensky (1924–1927)`
- **CLM -> SCH 断链外键样本** (`8` 条展示): `CLM-apalkov-2023-collective-to-personal-dictatorship: SCH-apalkov-dmitry`, `CLM-berlin-1960-populism-moral-core: SCH-berlin-isaiah`, `CLM-boll-1979-factory-militia-autonomy: SCH-boll-michael-m`, `CLM-boll-1979-red-guards-radicalization-to-july: SCH-boll-michael-m`, `CLM-bonnell-1983-1912-1914-union-and-insurance-boards-bolshevik-capture: Victoria E. Bonnell`
- **1918-02-14 改历后误加深双历标签** (`1` 条展示): `cards/policies/POL-war-communism.md:25 -> `1918-05-09 [O.S.] / 1918-05-22 [N.S.]``
- **1918-02-14 改历后 YAML 伪构 *_os 字段** (`1` 条展示): `EVT-1918-03-brest-litovsk-treaty.end_os=1918-03-02`
- **卡片成品正文泄漏编纂提示词元话语** (`1` 条展示): `EVT-1918-03-brest-litovsk-treaty: `任务示例所称``
- **未隔离纯扫描空书 (`needs_ocr` 缺失, 共 4 本)**: `sources/monographs/cao_weian_new_russian_history_zh`, `sources/monographs/lelichuk_soviet_industrialization_zh`, `sources/monographs/october_socialist_rev_zh`, `sources/primary/short_course_1938_zh`
- **B4 卡片残留字面陷阱**: B4A-07: 目标卡命中陷阱字面量 `end_os: '1918-03-02'`
