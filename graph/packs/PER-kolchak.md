# 1-Hop 平衡上下文包：`PER-kolchak` (亚历山大·高尔察克)

> 本文件由 `python scripts/kb.py pack` 自动编译，旨在将失控的 `1+N` 随机读取压缩为**等权重、带时效边实质与史学盲区告警**的单次全景读取。

## 0. 认知完备度与反偏斜仪表盘 (Epistemic & Skew Warnings)
- **主卡路径**: `cards/people/PER-kolchak.md`
- **完备度等级**: `draft`
- **已覆盖视角**: `civil-war-military, white-structural-defeat, radkey-sr-collapse, intervention-diplomacy`
- **待补齐视角**: `post-soviet-memory-politics`
- **偏斜风险提示**:
  - ⚠️ 主卡当前完备度为 `draft`，尚未达到多源交叉核实定稿状态。
  - ⚠️ 主卡显式声明尚缺以下视角待补: `post-soviet-memory-politics`。

## 1. 主卡核心层 ([T1] + [T2])
## [T1] 60秒定性微摘要
高尔察克（1874–1920），极地探险家、黑海舰队司令；1918年11月18日鄂木斯克政变推翻社革党全俄临时政府，自封“全俄最高执政”；1919春攻势被伏龙芝红军粉碎，1920年2月7日在伊尔库茨克被枪决。

## [T2] 核心脉络、时效关系边表与史学争鸣光谱

### 2.1 核心历史脉络
- **海军军官与科学探险（1874–1917）**：生于 `1874-11-04 [O.S.] / 1874-11-16 [N.S.]` 圣彼得堡；日俄战争旅顺海战与极地水文探险成名；1916–1917年任黑海舰队司令，二月革命后因不堪水兵委员会夺权愤而折剑辞职，奉派赴美英军事考察后于1918年秋经远东抵达鄂木斯克。
- **鄂木斯克政变与“最高执政”（1918.11）**：`1918-11-18 [N.S.，西伯利亚临时政府已于1918年10月改行格里高利公历；对应俄历11月5日]` 在英国军事代表团与哥萨克军官支持下于鄂木斯克发动军事政变，推翻社会革命党人主导的“全俄临时政府（乌法督政府）”，自封“全俄最高执政（Верховный правитель）”；Radkey 将此举视为社革党让右翼军官披上民主“保护色”后的必然反噬（`CLM-smith-scott-2011-psr-third-force-collapse`）。
- **1919年春攻势与崩溃（1919）**：1919年初沿西伯利亚铁路发动对苏维埃腹地的春季进攻，一度威胁彼尔姆—维亚特卡方向；伏龙芝率东线红军于4–6月实施反突击，沿铁路内线歼灭其主力（`CLM-kakurin-1928-red-army-interior-lines-strategy`）；兵败后退，丧失鄂木斯克，政权西迁。
- **兵败伊尔库茨克与处决（1919–1920）**：退守伊尔库茨克后因粮债与捷克军团摩擦遭当地政工委员会推翻；`1920-02-07` 不经审判枪决于伊尔库茨克岸边（邻近日期 `1920-01-26 [O.S.] / 1920-02-08 [N.S.]` 异说待档核对）。

### 2.2 时效关系摘要边表（Typed & Temporalized Edges）
| 关联节点 ID | 关系类型 | 有效时段 | 一句话关系实质摘要（防 N+1 盲跳） | 核心依据/争鸣 |
| :--- | :--- | :--- | :--- | :--- |
| `ORG-psr` | `coup-against` | 1918.11 | 取代 Siberian Directory，终结社革“第三力量”幻象 | `CLM-smith-scott-2011-psr-third-force-collapse` |
| `PER-frunze` | `defeated-by` | 1919.04–06 | 东线南集群铁路机动击溃春攻 | `CLM-kakurin-1928-red-army-interior-lines-strategy` |
| `EVT-1918-1920-russian-civil-war` | `white-commander` | 1918–1920 | 西伯利亚白卫政权最高军事—政治象征 | `CLM-mawdsley-1987-white-movement-structural-defeat` |
| `PER-denikin` | `strategic-uncoordinated-ally` | 1919 | 与白军各战线错时进攻致红军逐一击破 | Kakurin；Mawdsley |
| `ORG-komuch` | `successor-regime` | 1918 | 政变吞噬伏尔加—西伯利亚民主反革命残余 | Radkey 叙事 |

### 2.3 史学争鸣光谱（Historiographical Spectrum）
- **经验共识**：高尔察克1918年11月政变、1919年春攻及同年兵败为史实；伊尔库茨克处决终结西伯利亚白卫中央政权。
- **主要解释分歧**：
  - **[Mawdsley 结构 defeat 论]**：即便将领能力尚可，高尔察克亦受_white_土地政策、大俄罗斯民族主义与外线兵力分散三重结构性锁死，且1919战役在红军十比一兵力与苏托邦军火垄断下难胜（`CLM-mawdsley-1987-white-movement-structural-defeat`；`CLM-mawdsley-1987-sovdepia-demographic-industrial-base`）。
  - **[Kakurin 红军战略学]**：伏龙芝东线胜利系红军沿西伯利亚铁路内线调兵与“突击战线”供给之产物，高尔察克将预备队投入次要北翼属战略过度延伸（`CLM-kakurin-1928-red-army-interior-lines-strategy`）。
  - **[Radkey 社革悲剧史]**：高尔察克政变显露社革党丧失自有兵源后只能让右翼军官以民主“保护色”夺权（`CLM-smith-scott-2011-psr-third-force-collapse`，Scholar: `SCH-radkey-oliver`）。

## 2. 一跳邻域等权重微摘要 (共 1 个关联节点，严防大卡霸占上下文)
### 邻居节点: `EVT-1918-1920-russian-civil-war`
- **时效关系边** (`PER-kolchak` → `EVT-1918-1920-russian-civil-war` | `eastern-white-supreme-ruler` | 有效时段: `1918.11-1920.02`): 1918年11月18日鄂木斯克政变推翻社革党督政府自任最高执政，1919春西进遭伏龙芝东线红军击溃并于伊尔库茨克被处决。
- **节点定性微摘要 [T1]** (完备度 `draft`): 1918–1920年苏俄内战：布尔什维克依托“苏托邦”人口、军火与莫斯科铁路枢纽内线机动，先后粉碎高尔察克、邓尼金、弗兰格尔白军及马赫诺黑军，并压制社革党第三力量；协约国干涉与边疆民族武装相互牵制。

## 3. 关联史学争鸣光谱 (Historiographical Debates)
### `DEB-1918-red-terror-and-civil-war-origins`：红色恐怖、契卡扩张与内战期一党专政起源之争（1918–1921）
## [T1] 核心问题定义
1918–1921年红色恐怖、契卡法外处决、对社会主义反对派的镇压，以及内战期间政党竞争被压缩为一党统治，应被解释为布尔什维克意识形态与列宁主义权力逻辑的宿命展开，还是多重危机（经济崩溃、联盟破裂、地方失控、内战动员）下可错链条上的制度选择？恐怖与一党制是同一过程还是须分时段因果？

## [T2] 各学派立场对照矩阵

**经验共识**：1917年12月契卡（全俄肃反委员会）成立；1918年7月左派社会革命党起义后左翼社会主义者被逐出权力结构；1918年9月5日[O.S.]人民委员会颁布《关于红色恐怖》决议；内战1918–1920在多条战线同时进行；1918–1921征粮与契卡行动在地方相互嵌合。

| 学派/取向 | 代表学者与著作 | 核心论点摘要 | 支撑论断卡 | 主要受批评盲点 |
| :--- | :--- | :--- | :--- | :--- |
| **意识形态宿命论** | Richard Pipes, *The Russian Revolution* (1990); Orlando Figes, *A People's Tragedy* (1996) | 强调反自由主义知识分子传统、列宁废法统治与阶级敌人话语，使恐怖成为夺取与巩固权力的内在逻辑；Figes 另重农民“悲剧”道德经济。 | `CLM-pipes-1990-red-terror-leninist-logic` | 时间线易前推到1917末，低估联盟期与反对派选项；Figes 与 Pipes 因果权重不一。 |
| **复合危机与联盟破裂论** | Alexander Rabinowitch, *The Bolsheviks in Power* (2007) 等 | 彼得格勒首年追踪与左派社革党联盟从执政到破裂；恐怖升级与粮食危机、暗杀、前线失败交织，而非单线预谋。 | `CLM-rabinowitch-2007-left-sr-coalition-collapse`, `CLM-rabinowitch-2007-contingency-of-dictatorship` | 首都政党政治详尽，偏远地方契卡实践待补。 |
| **制度史与阶段论** | George Leggett, *The Cheka: Lenin's Political Police* (1981); Ilya S. Ratkovsky（及契卡编年史学） | Leggett：契卡从法外 origin 到 GPU 连续体制化；Ratkovsky：1918 夏已有人质与处决规模，9月5日法令是公开化节点而非“零起点”。 | `CLM-leggett-1981-vecheka-extra-legal-origins`, `CLM-leggett-1981-red-terror-institutionalization`, `CLM-leggett-1981-cheka-to-gpu-continuity`, `CLM-cheka-chronicle-hostage-and-local-autonomy`, `CLM-cheka-chronicle-suppression-of-socialist-rivals` | Leggett 偏重中央法令；地方自治与契卡失控需档案对勘。 |
| **1914–1921 总体战治理连续论** | David G. Hoffmann, *Cultivating the Masses: Modern State Practices and Soviet Socialism, 1914–1939* (2011) | 征粮、动员、战备与“培养大众”技术沿袭一战国家实践；苏联社会主义是欧洲现代国家治理谱系的一极，而非凭空乌托邦。 | `CLM-hoffmann-2011-continuum-of-total-war-1914-1929`, `CLM-hoffmann-2011-enlightenment-and-coercion-duality`, `CLM-hoffmann-2011-soviet-socialism-as-european-modernity` | 连续性不等于免除布尔什维克政党特有选择责任。 |
| **内战军事—地理决定论（背景）** | Evan Mawdsley, *The Russian Civil War* (1987) | 红军人口—工业内线优势与白军结构性政策失败解释内战结局；为恐怖与征粮提供战略背景，不单独承担一党制意识形态解释。 | `CLM-mawdsley-1987-civil-war-militarized-regime`, `CLM-mawdsley-1987-sovdepia-demographic-industrial-base` | 军事动员不等于党内反对派清洗因果。 |

## 4. 关联时间线锚点 (共 0 条)
