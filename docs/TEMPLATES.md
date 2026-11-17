# 俄国革命知识库：标准卡片与文献模板集

所有子 Agent 在创建或更新卡片、论断、阅读札记时，必须严格遵守以下标准结构，以保证 `scripts/kb.py` 能准确解析元数据、校验图谱并编译防偏斜上下文包。

---

## 一、ID 命名规范

| 类别 | 目录 | ID 前缀示例 | 说明 |
| :--- | :--- | :--- | :--- |
| 人物（Person） | `cards/people/` | `PER-bukharin` | 统一使用标准英文拉丁化姓氏（重名加教名首字母，如 `PER-martov-l`） |
| 组织/派别/机构（Org） | `cards/organizations/` | `ORG-narodnaya-volya` | 政党、秘密社团、党内反对派集团、国家机关 |
| 历史事件（Event） | `cards/events/` | `EVT-1921-kronstadt` | 附带公历年份前缀便于时序识别 |
| 会议/全会（Meeting） | `cards/meetings/` | `MTG-1929-04-cc-plenum` | 代表大会、代表会议、中央全会、秘密会议 |
| 概念系谱（Concept） | `cards/concepts/` | `CON-smychka` | 具有跨期语义演变的政治/社会经济核心概念 |
| 制度/法令/路线（Policy） | `cards/policies/` | `POL-nep` | 重大法令、经济体制、战略路线 |
| 史学家（Scholar） | `historiography/scholars/` | `SCH-cohen-stephen` | 历史学家方法论与代表作档案 |
| 史学争鸣（Debate） | `historiography/debates/` | `DEB-1928-bukharin-alternative` | 多流派交锋的核心史学公案 |
| 原子论断（Claim） | `historiography/claims/` | `CLM-cohen-1973-nep-viability` | 单条学者论断 + 原文直引 + 页码锚点 |

---

## 二、实体/概念/事件卡片标准模板（`cards/**/*.md`）

> **注意**：`## [T1]`、`## [T2]`、`## [T3]` 三个二级标题前缀是 `scripts/kb.py pack` 自动切片编译器的识别锚点，请勿改写前缀格式！

```markdown
---
id: PER-example
type: person # person | organization | event | meeting | concept | policy
title: 中文标准译名
names:
  ru: Русское имя
  en: English Name
  aliases: ["别名1", "化名2"]
dates:
  start_ns: "1888-10-09"
  end_ns: "1938-03-15"
coverage_status: draft # stub | draft | grounded | multi-perspective
perspectives_present: ["revisionist", "archival-post-soviet"]
perspectives_missing: ["trotskyist", "liberal-totalitarian"]
related_debates: ["DEB-xxx"]
updated_at: "2026-11-18"
---

## [T1] 60秒定性微摘要
（严格控制在 150 字以内。不带流派偏见地交代该实体的核心历史身份、关键活跃期、最具决定性的制度/思想坐标，供邻居卡片生成等权重 1-Hop 上下文包使用。）

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **阶段一（年份区间）**：简明事实演化。
- **阶段二（年份区间）**：关键转折与政治/社会位置变化。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `PER-xxx` | `ally -> rival` | 1925–1927 结盟；1928–1929 决裂 | 围绕新经济政策与非常措施从联手反左派转向路线摊牌 | `DEB-xxx` |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：各派公认的基本事实。
- **主要解释分歧**（详参 `DEB-xxx`）：
  - **[流派A / 代表学者]**：核心判断（参见 `CLM-xxx`）。
  - **[流派B / 代表学者]**：对立或修正判断（参见 `CLM-yyy`）。

## [T3] 深度考证、分期细目与原文引证档案
（此处展开详尽考据、数据表格、会议发言细节与带 `[p. xx]` 页码锚点的一手/二手原文摘录，长度不限。）
```

---

## 三、史学争鸣母题卡模板（`historiography/debates/DEB-*.md`）

```markdown
---
id: DEB-example
type: debate
title: 争鸣公案中文标题
era: "1921-1929"
core_cards: ["POL-nep", "PER-bukharin", "PER-stalin"]
coverage_status: draft
perspectives_present: ["revisionist", "archival-post-soviet", "trotskyist"]
perspectives_missing: []
updated_at: "2026-11-18"
---

## [T1] 核心问题定义
（用 100–150 字精确界定该史学公案争论的焦点问题是什么，避免把经验事实问题与价值判断混为一谈。）

## [T2] 各学派立场对照矩阵
| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| 修正派/替代方案论 | Stephen Cohen, Moshe Lewin | 认为新经济政策具备渐进工业化潜力，危机源于政策失误与强行转向 | `CLM-...` | 被批评低估了1927年后工业投资瓶颈与国防压力 |
| 后苏联档案/制度派 | Oleg Khlevniuk, R. W. Davies | 基于政治局与全会速记指出价格机制失衡与政治局权力结构的双重锁死 | `CLM-...` | — |

## [T3] 争鸣演进史与待核查关键史料
（梳理学术史演变脉络，并列出可进一步检验各方假说的一手档案或定量数据。）
```

---

## 四、原子论断卡模板（`historiography/claims/CLM-*.md`）

```markdown
---
id: CLM-author-year-slug
type: claim
scholar: SCH-author
work_title: "Book or Article Title"
publication_year: 1973
source_tier: A # S | A | B
local_source_path: "sources/monographs/slug/ch09.md#L120-L185"
original_pages: "pp. 270-273"
targets_cards: ["PER-bukharin", "EVT-1928-grain-crisis"]
debate: DEB-1928-bukharin-alternative
supports: []
rebuts: []
qualifies: []
---

## 核心论断命题（Thesis）
（准确提炼作者在此处提出的具体历史解释或因果论断。）

## 论证链条与依据（Reasoning & Evidence）
（作者使用了哪些档案、统计数字或逻辑推演支撑该命题？）

## 原文直引（Verbatim Quote）
> "保留原书语言一字不差的精确引文……" `[p. 271]`

## 语境说明与局限提示
（交代该段文字所在的整章讨论背景，防止脱离上下文误读。）
```
