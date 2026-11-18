# 1-Hop 平衡上下文包：`PER-denikin` (安东·邓尼金)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/people/PER-denikin.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `civil-war-military, white-structural-defeat, anti-bolshevik-memoir, intervention-diplomacy`
- **待补齐视角**: `ukrainian-polish-borderlands-local`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `ukrainian-polish-borderlands-local`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
邓尼金（1872–1947），南俄武装力量总司令；1919年夏秋挥师北进占奥廖尔直逼莫斯科；纵容“沙拉班”地主复辟与“统一不可分割俄罗斯”口号疏远农民、哥萨克与波兰，奥廖尔战败后全线崩溃；1920年起流亡，至死未再掌兵。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **禁卫军官与一战将领（1872–1917）**：生于 `1872-12-04 [O.S.] / 1872-12-16 [N.S.]` 华沙；出身贫职军官家庭，毕业于基辅士官学校；1915–1917年出任西南方面军第八集团军司令，以《关于贫苦土地》备忘录尝试笼络士兵，却难改大俄罗斯—军官团保守底色。
- **志愿军与白卫南俄（1918–1919春）**：1918年在库班组织“志愿军”（Volunteer Army），与阿列克谢耶夫、格森林承接北高加索—顿河白卫；冬春季巩固东南基地，宣称恢复“伟大、统一、不可分割的俄罗斯”，拒乌克兰、波兰民族自决。
- **1919夏秋莫斯科攻势（1919.05–10）**：7月颁布《莫斯科训令》三面（伏尔加—莫斯科—基辅）分散进攻；8–9月攻占库尔斯克、奥廖尔，兵锋距图拉不足200公里；红军自东线经铁路南调6万兵力，于9–10月沿奥廖尔—沃罗涅日中线以局部2:1密度反杀（`CLM-kakurin-1928-red-army-interior-lines-strategy`）。
- **后方崩溃与南撤（1919秋–1920）**：“沙拉班”地主马车随军复辟激起农民与马赫诺黑军大起义；拒波兰边界承认致毕苏斯基停攻；11月清洗库班哥萨克拉达导致骑兵主力溃散（`CLM-mawdsley-1987-white-movement-structural-defeat`）。1920年1月率残部退入新罗西斯克，后流亡法国、美国，1929年前仍任 abroad 白卫政治象征，1947年8月卒于密歇根安娜堡。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `EVT-1918-1920-russian-civil-war` | `white-commander` | 1918–1920 | 南俄武装力量最高统帅，1919年最大威胁莫斯科的白卫轴心 | Mawdsley；Kakurin |
| `PER-kolchak` | `uncoordinated-ally` | 1919 | 东西攻势时序错开，便利红军逐次歼灭 | `CLM-mawdsley-1987-white-movement-structural-defeat` |
| `PER-frunze` | `opponent-indirect` | 1919–1920 | 东线击溃高尔察克所释兵力南调参加对邓尼金决战 | Kakurin |
| `ORG-psr` | `parasitic-alliance` | 1918–1919 | 库班等地社革右翼以“保护色”拥戴志愿军，反农民政策终致离心 | `CLM-smith-scott-2011-psr-third-force-collapse` |
| `ORG-kadets` | `ideological-kin` | 1918–1919 | 土地与民族政策贴近立宪民主党“国家崇拜”右派 | Radkey 引述 |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：邓尼金1919年夏秋攻势抵达奥廖尔—图拉前线为史实；1920年初南俄白卫政权崩溃；其回忆录《俄国内战见闻录》是白方核心一手文献（属 B 级回忆录，须与档案对勘）。
- **主要解释分歧**：
  - **[Mawdsley 结构 defeat 论]**：邓尼金失败首要因土地“沙拉班”复辟、残部劫掠（“抢劫军”）与大俄罗斯民族主义孤立波兰、芬兰、哥萨克，而非单纯将领无能（`CLM-mawdsley-1987-white-movement-structural-defeat` `ch13` `pp. 212–218`）。
  - **[Kakurin 红军战略学]**：奥廖尔决战胜利系红军铁路内线机动与兵力密度优势，亦批判邓尼金《莫斯科训令》无配合的三面发散（`CLM-kakurin-1928-red-army-interior-lines-strategy` `pp. 198–199, 215–220`）。
  - **[Radkey / Smith 社革视角]**：库班等地社革知识分子已蜕变为隐性立宪民主党人，公开支持志愿军却无力约束其农民政策（`CLM-smith-scott-2011-psr-third-force-collapse`）。
  - **[白卫回忆录本位 / Denikin 自身]**：强调布尔什维克红色恐怖、德援中断与协约国援助不足——社会史修正派视为结构性语境而非主因。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `EVT-1918-1920-russian-civil-war`
- **时效关系边** (`PER-denikin` → `EVT-1918-1920-russian-civil-war` | `southern-white-commander` | 有效时段: `1918.04-1920.04`): 统率南俄武装力量于1919年秋推进至奥廖尔逼近莫斯科，因地主复辟、后方马赫诺起义及大俄罗斯沙文主义断送波兰与哥萨克配合而全军覆没。
- **节点定性微摘要 [T1]** (完备度 `draft`): 1918–1920年苏俄内战：布尔什维克依托“苏托邦”人口、军火与莫斯科铁路枢纽内线机动，先后粉碎高尔察克、邓尼金、弗兰格尔白军及马赫诺黑军，并压制社革党第三力量；协约国干涉与边疆民族武装相互牵制。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
- ⚠️ 引用了尚未创建的争鸣卡 `DEB-1918-democratic-counterrevolution-third-force`
## 4. 关联时间线锚点 (共 0 条)
