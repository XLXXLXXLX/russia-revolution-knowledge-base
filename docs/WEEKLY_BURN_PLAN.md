# 周订阅额度饱和式推进总计划（Weekly Subscription Burn Master Plan）

> **战略目标**：充分利用 `codex`（GPT 订阅）、`grok`（Grok 订阅）与 `antigravity_2`（Antigravity 订阅）三大周订阅池，通过**多波次、6角色流水线并发**，将 `inbox/` 中的 205 部文献宝藏与开放互联网一手档案系统转化为覆盖 **1861年农奴制改革与民粹派兴起 → 1929年斯大林击败布哈林** 的全尺度双历法编年、反偏斜知识图谱与多学派论断库，持续运转直至周订阅额度耗尽（或触发 OpenCode 兜底池）。

---

## 一、算力分配与波次流水线原则（Quota Burn Mechanics）

1. **小步稳态并发限流器（Paced Concurrency Governor：总并发 ≤ 4 路，严防打穿 5 小时滑动窗口！）**：
   - 实战教训：高并发洪峰会瞬间撞上 ChatGPT/Codex 等订阅池的 **5小时滑动窗口限额**（而非周总额度）。
   - **硬性限流铁律**：必须等上一批在途任务排空后再发下一批，**每批总并发严格控制在 3–4 个任务以内**（例如：`codex` ≤ 1–2 路、`grok` ≤ 1 路、`antigravity_2` Gemini ≤ 2 路），细水长流吃满周额度。
   - **Antigravity 配额结构**：`antigravity_2` 的 Claude 池极小（已耗尽停用）；同实例下的 **Gemini 池（`gemini-4-hydrogen` / `argon` / `3.8-flash`）** 充足，作为精读与建卡主力。
2. **配额耗尽自动探测与平滑转移**：
   - 状态实时记录于 [`config/campaign_state.json`](../config/campaign_state.json)。
   - 若某订阅 Provider 返回周额度耗尽报错（`weekly usage` / `quota exceeded` / `rate limit`），立即将该 Provider 标记为 `exhausted`：优先将任务分流至其余尚有余量的订阅 Provider；当三大订阅池均耗尽时，按规则简单任务切 `opencode / deepseek-flash#high` (`ds4.1f`)、复杂任务切 `opencode / google/gemini-4-argon#high`（极难升 `carbon`）。
3. **四阶滚动流水线（Pipelined Waves）**：
   - `Wave N` 提取书籍分章文本与一手档案 → `Wave N+1` 整章精读产出 `RN-*` 札记与 `CLM-*` 原子论断卡 → `Wave N+2` 织入 `L1–L3` 时间线、扩建 `cards/` 与 `DEB-*` 争鸣卡并编译 `pack` → `Wave N+3` 异源 `dialectic-auditor` 挑刺审计并修订落 Git 提交！

---

## 二、十大历史战役与波次执行排期表（1861–1929 全覆盖）

### 战役集群 A：革命前史——民粹派、马克思主义传入与 1905 风暴（E01–E04，1861–1914）
- **核心入库专著（`source-extractor`）**：
  1. `venturi_1960_roots`：文图里《革命的根源》(`BIB-001`)
  2. `walicki_1969_controversy`：瓦利茨基《资本主义论战》(`BIB-002`)
  3. `haimson_1955_origins` & `haimson_2005_experience`：海姆森《布尔什维主义起源》与《1905–1917革命经验》(`BIB-003/007`)
  4. `lih_2008_lenin_rediscovered`：Lars T. Lih《列宁再发现》(`inbox/` 中英双版)
  5. `getzler_1967_martov` & `hildermeier_psr`：格茨勒《马尔托夫传》(`BIB-004`)、希尔德迈尔《一战前俄国社革党》(`BIB-005`)
  6. `trotsky_1905` & `bonnell_1983_roots_rebellion` & `blanc_2021_rev_sd`：托洛茨基《1905》、邦内尔《叛乱的根源 1900–1914》、Eric Blanc《边疆革命社会民主主义 1882–1917》
- **外网一手抓取（`web-scout`）**：民意党《执委会纲领》(1879)、《致亚历山大三世信》(1881)、查苏利奇-马克思通信、1903 二大党章第一条争论原文、1905《十月宣言》与彼得堡苏维埃文件。
- **核心产出目标**：
  - 时间线：`L2_chronicles/E01`、`E02`、`E03`、`E04` + `L3_daily/1881-03_assassination.md` + `L3_daily/1905-01_bloody_sunday.md`；
  - 卡片与争鸣：赫尔岑、车尔尼雪夫斯基、拉甫罗夫、特卡乔夫、热利亚博夫、佩罗夫斯卡娅、菲格涅尔、普列汉诺夫、查苏利奇、阿克雪里罗得、列宁、切尔诺夫、斯托雷平；土地与自由社、劳动解放社、社会革命党、立宪民主党；`DEB-1903-bolshevik-menshevik-split`（海姆森 vs Lih）、`DEB-haimson-thesis-1914`（战前俄国稳定与否之争）。

### 战役集群 B：帝国崩解、1917 双重政权与十月夺权（E05–E06，1914–1917）
- **核心入库专著（`source-extractor`）**：
  7. `hasegawa_1981_february`：长谷川毅《1917年彼得格勒二月革命》(`BIB-008`)
  8. `rabinowitch_1968_prelude` & `rabinowitch_1976_come_to_power`：拉比诺维奇《革命前奏：七月事变》与《布尔什维克掌权》(`BIB-009`)
  9. `trotsky_1930_history_rr` & `sukhanov_1922_personal_record`：托洛茨基《俄国革命史》三卷(`BIB-010`)、苏汉诺夫《1917个人札记》(`BIB-011`)
  10. `pipes_1990_russian_rev` & `figes_1996_peoples_tragedy`：派普斯《俄国革命》(`BIB-012`)、费吉斯《人民的悲剧》(`BIB-014`)
  11. `smith_1983_red_petrograd` & `koenker_moscow_workers_1917` & `galili_menshevik_leaders` & `roobol_tsereteli`：史密斯《红色彼得格勒》(`BIB-013`)、科恩克尔《莫斯科工人与1917革命》、加利利《孟什维克领袖》、策烈铁里传、盖达《走向权力之路的自由主义反对派》
- **外网一手抓取（`web-scout`）**：彼得格勒苏维埃《第一号命令》、列宁《四月提纲》、七月事变与科尔尼洛夫事件通电、1917年10月10日与16日布尔什维克中央会议记录、加米涅夫-季诺维也夫《新生活报》声明、全俄苏维埃二大《和平法令》《土地法令》。
- **核心产出目标**：
  - 时间线：`L2_chronicles/E05`、`E06` + **四大 L3 逐日/逐小时显微镜卷**（`1917-02_february_eight_days.md`、`1917-07_july_days.md`、`1917-08_kornilov_affair.md`、`1917-10_october_insurrection_hours.md`）；
  - 卡片与争鸣：克伦斯基、米留科夫、策烈铁里、科尔尼洛夫、苏汉诺夫、加米涅夫、季诺维也夫、斯维尔德洛夫、安东诺夫-奥夫谢延科；彼得格勒苏维埃、军事革命委员会、工厂委员会；`DEB-1917-february-spontaneity`、`DEB-1917-october-coup-or-social-revolution`。

### 战役集群 C：执政第一年、内战、战时共产主义与党内早期反对派（E07–E08，1917.11–1923）
- **核心入库专著（`source-extractor`）**：
  12. `rabinowitch_2007_in_power`：拉比诺维奇《布尔什维克执政》(`BIB-015`)
  13. `mawdsley_1987_civil_war` & `carr_bolshevik_rev_1_3`：莫兹利《俄国内战》(`BIB-016`)、卡尔《布尔什维克革命》1–3卷(`BIB-026`)
  14. `leggett_1981_cheka` & `white_sr_alternative`：莱格特《契卡》、怀特《社革党替代方案》
  15. `daniels_1960_conscience` & `kollontai_workers_opposition`：丹尼尔斯《革命的良心：共产主义反对派》(`BIB-017`)、柯伦泰《工人反对派》
  16. `avrich_1970_kronstadt` & `lewin_1968_lenins_last_struggle`：阿夫里奇《1921喀琅施塔得》(`BIB-018`)、莱文《列宁的最后斗争》(`BIB-019`)
- **外网一手抓取（`web-scout`）**：维克热尔谈判记录、解散立宪会议法令、布列斯特和约党内七大速记摘要、俄共（布）十大《关于党的统一》与《关于以实物税代替余粮收集制》、列宁最后口授书信（“政治遗嘱”、《论合作社》、《宁肯少些，但要好些》）。
- **核心产出目标**：
  - 时间线：`L2_chronicles/E07`、`E08` + `L3_daily/1918-01_constituent_assembly_and_brest.md` + `L3_daily/1921-03_kronstadt_and_10th_congress.md` + `L3_daily/1922-12_lenins_last_struggle.md`；
  - 卡片与争鸣：捷尔任斯基、左翼社会革命党（玛丽亚·斯皮里多诺娃）、柯伦泰、什利亚普尼科夫、奥新斯基（民主集中派）、高尔察克、邓尼金、马赫诺；战时共产主义、余粮收集制、立宪会议、布列斯特和约、俄共（布）十大；`DEB-1918-war-communism-ideology-or-emergency`、`DEB-1921-kronstadt-nature`。

### 战役集群 D：新经济政策、工业化大论战与斯大林击败布哈林（E09–E10，1923–1929 收官决战！）
- **核心入库专著（`source-extractor`）**：
  17. `cohen_1973_bukharin`：斯蒂芬·科恩《布哈林与布尔什维克革命》(`BIB-020`)
  18. `lewin_1968_peasants`：摩西·莱文《俄国农民与苏维埃政权》(`BIB-021`)
  19. `erlich_1960_industrialization` & `preobrazhensky_1926_new_economics`：埃利希《苏联工业化大论战》(`BIB-025`)、普列奥布拉任斯基《新经济学》、郑异凡《新经济政策的俄国》与《平衡与非平衡》
  20. `deutscher_prophet_trilogy`：多伊彻《先知三部曲（重点第2卷：被解除武装的先知 1921–1929）》(`BIB-024`)
  21. `kotkin_2014_stalin_v1` & `khlevniuk_2015_stalin`：科特金《斯大林》第1卷(`BIB-023`)、赫列夫纽克《斯大林新传》(`BIB-027`)
  22. `carr_interregnum` & `carr_davies_foundations` & `nove_was_stalin_necessary`：卡尔《过渡时期 1923–1924》、卡尔&戴维斯《计划经济的基础 1926–1929》、诺夫《斯大林真的必要吗？》
  23. `sakharov_2012_crossroads` & `apalkov_intra_party_struggle` & `merridale_moscow_politics` & `ball_nepmen`：萨哈罗夫《在十字路口(1921-1929)》、阿帕利科夫《联共(布)党内斗争》、梅里代尔《莫斯科政治与斯大林崛起 1925–32》、鲍尔《耐普曼 1921–1929》
- **外网一手抓取（`web-scout`）**：1923《四十六人声明》、托洛茨基《新方针》与《十月的教训》、斯大林《十月革命与俄国共产党人的策略》（“一国建成社会主义”）、1927《联合反对派政纲》、斯大林1928《在粮食战线上》（含涅姆奇诺夫表）、1928.07《布哈林-加米涅夫谈话纪要》、布哈林《经济学家札记》与1929.01《列宁的政治遗嘱》、斯大林1929.04《论联共（布）党内的右倾》与1929.11《大转变的一年》。
- **核心产出目标**：
  - 时间线：`L2_chronicles/E09`、`E10` + `L3_daily/1923-10_scissors_and_46.md` + `L3_daily/1927-11_tenth_anniversary_expulsion.md` + **终极收官卷 `L3_daily/1928-1929_bukharin_stalin_final_showdown.md`**；
  - 卡片与争鸣：斯大林、托洛茨基、李可夫、托姆斯基、乌格兰诺夫、索科尔尼科夫、莫洛托夫、卡冈诺维奇、古比雪夫、奥尔忠尼启则、拉狄克；三驾马车、新反对派、联合反对派、右翼反对派、一国建成社会主义、社会主义原始积累、剪刀差危机、乌拉尔-西伯利亚方法；联共（布）十四大、十五大、1928七月全会、1929四月全会、1929十一月全会；`DEB-socialism-in-one-country`、`DEB-1924-industrialization-accumulation`、`DEB-stalin-rise-apparatus-vs-ideas`、升级定稿 `DEB-1928-bukharin-alternative`！

---

## 三、波次推进路线图（Waves 1 → N 持续循环）

- **Wave 1（立即启动，12 路并发）**：提取首批 9 部横跨 1860s–1929 的 P0 基石专著 + 抓取 3 大时期一手文献集 + 创建列宁/斯大林/托洛茨基/社革党及 3 大核心争鸣卡、3 张核心概念系谱卡 + 编织 `E01/E02` L2 编年与 `1917 二月/十月` L3 逐时微距卷。
- **Wave 2**：基于 Wave 1 已提取的文图里、瓦利茨基、海姆森、拉比诺维奇、科恩、莱文、萨哈罗夫全章文本，派出 **8 路 `close-reader` 整章精读**（产出首批 `CLM-*` 原子论断与页码直引） + **4 路 `source-extractor`** 提取第二批 10 部专著（长谷川毅、苏汉诺夫、派普斯、史密斯、丹尼尔斯、阿夫里奇、莱文《列宁最后斗争》、埃利希、普列奥布拉任斯基《新经济学》、多伊彻）。
- **Wave 3**：吸收 Wave 2 精读论断进入卡片 `[T3]` 与 `timeline/events_ledger.jsonl` + 启动第二批专著整章精读 + 提取第三批专著（科特金、赫列夫纽克、卡尔&戴维斯、莫兹利、费吉斯、梅里代尔、阿帕利科夫、Lih、格茨勒） + 首轮异源 `dialectic-auditor` 批量挑刺审计。
- **Wave 4 → Wave K（循环推进直至烧穿周额度）**：按专题深度（民粹派→社民党分裂→1905→1917工厂与兵营→内战与反对派→1923–27论战→1928–29击败布哈林）逐章推进 `close-reader` 精读、`CLM-*` 论断落库、`L2/L3` 时间线加密、会议投票卡 `MTG-*` 与学者卡 `SCH-*` 扩建、以及跨家族审计闭环，每波次结算后执行 `kb.py audit-graph` 与 Git 提交！
