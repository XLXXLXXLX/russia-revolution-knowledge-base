# 俄国革命史公开互联网史料库与学术站点导航

本清单供 `web-scout` 与编排者在进行开放网络检索时优先调用，按信源等级与语种分类。

## 一、S级：在线一手文献与数字档案库

1. **Marxists Internet Archive (MIA / 马克思主义文库)**
   - **英文主站**：`https://www.marxists.org/history/ussr/` 及人物文集（Lenin, Trotsky, Bukharin, Preobrazhensky, Luxemburg, Plekhanov, Martov, Kollontai, Stalin, Vera Figner, Lavrov 等）。
   - **俄文分站**：`https://www.marxists.org/russkij/`（核对译文关键术语原文的利器）。
   - **中文分站**：`https://www.marxists.org/chinese/`（含《列宁全集》《托洛茨基文集》《布哈林文选》《普列汉诺夫哲学著作选集》《卢森堡文选》等大量现成中译篇目，抓取时须与俄/英原文核对关键概念译法）。
2. **Исторические материалы (IstMat / 历史文献网，俄文)**
   - 网址：`https://istmat.org/`
   - 价值：收录海量苏联早期统计年鉴、联共（布）全会与代表大会决议汇编、1920年代国家计委及粮食收购原始档案文献。
3. **Электронная библиотека ГПИБ России (俄罗斯国家公共历史图书馆数字馆藏，俄文)**
   - 网址：`http://elib.shpl.ru/`
   - 价值：公开大量 19 世纪民粹派书刊（《钟声》《前进！》《民意报》史料汇编）、1905 与 1917 年各党派小册子、苏维埃早期速记报告扫描与文本。
4. **Seventeen Moments in Soviet History (密歇根州立大学苏联史专题文献库，英文)**
   - 网址：`https://soviethistory.msu.edu/`
   - 价值：按关键年份（`1917`, `1921`, `1924`, `1929`）组织的精选英译一手档案、法令、报刊摘录、历史图像与学者导读。
5. **Документы советской эпохи (苏维埃时代文献门户 / 俄罗斯联邦档案署 Росархив，俄文)**
   - 网址：`http://sovdoc.rusarchives.ru/`
   - 价值：包含 РГАСПИ（俄罗斯国家社会政治史档案馆）部分数字化全宗目录与斯大林、政治局档案扫描索引。
6. **Internet Archive (`https://archive.org/`) & HathiTrust (`https://www.hathitrust.org/`)**
   - 价值：检索公版期一手英/俄/法/德文早期回忆录（如克鲁泡特金、维拉·菲格涅尔、萨温科夫、克伦斯基、米留科夫、切尔诺夫早期英译本）及早期学术期刊。

## 二、A级：开放获取学术期刊、书评与研究网络

1. **CyberLeninka (`https://cyberleninka.ru/`)**：俄罗斯最大开放获取学术论文库，可免费检索下载当代俄罗斯历史学家关于民粹派、社会革命党、1917 地方苏维埃、新经济政策与 1928–1929 党内斗争的最新俄文同行评议论文。
2. **H-Russia / H-Net Reviews (`https://networks.h-net.org/h-russia`)**：欧美俄国史学界权威长篇学术书评库，适合快速了解某部专著在学界受到的赞誉与方法论批评（辅助 `dialectic-auditor` 定位学术争鸣点，但不能替代阅读原书）。
3. **Russia's Great War and Revolution (`https://russiasgreatwar.org/`)**：国际学者合作项目，聚焦 1914–1922 帝国危机、一战与内战连续统研究。

## 三、抓取入库规范
凡从上述网站抓取全文存入 `sources/web-archive/` 时，必须在文件顶部附上 YAML Frontmatter：
- `source_url`（精确链接）
- `retrieved_at`（抓取日期）
- `written_date_os` / `written_date_ns`（写作或发表日期）
- `edition_note`（底本与译本信息，如《列宁全集》中文第2版 vs MIA 英译本）
- `epistemic_tier`（`S` / `A` / `B` / `C`）
