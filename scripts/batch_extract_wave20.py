#!/usr/bin/env python3
"""批量提取 Wave 20 的 12 部高价值文献（含 1929.11 苏联农村的悲剧档案集、卡尔三卷本、共产国际卷、莫佐欣契卡统计等）。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("苏联农村的悲剧*第2卷*", "sources/primary/tragedy_soviet_village_v2_1929_zh", 25),
    ("The Industrialisation of Soviet Russia.epub", "sources/monographs/davies_industrialisation_en", 25),
    ("苏维埃俄国史——布尔什维克革命（1917-1923）第一卷*", "sources/monographs/carr_bolshevik_rev_v1_zh", 25),
    ("苏维埃俄国史——布尔什维克革命（1917-1923）第二卷*", "sources/monographs/carr_bolshevik_rev_v2_zh", 25),
    ("苏维埃俄国史——布尔什维克革命(1917-1923)第三卷*", "sources/monographs/carr_bolshevik_rev_v3_zh", 25),
    ("Foundations of a Planned Economy 1926–1929 Volume Three - II*", "sources/monographs/carr_1976_foundations_v3p2", 30),
    ("Lenin and the Jacobin Identity in Russia*", "sources/monographs/mayer_1999_lenin_jacobin", 25),
    ("workers-the-intelligentsia-and-marxist-parties*", "sources/monographs/zelnik_1999_workers_intelligentsia", 25),
    ("锤击镰刀：被布尔什维克镇压的社会革命党*", "sources/monographs/smith_scott_captives_of_rev_zh", 30),
    ("苏联国家安全机关 镇压的权利*", "sources/monographs/mozokhin_extrajudicial_powers_zh", 25),
    ("The Russian Civil War, 1918_*", "sources/primary/kakurin_1928_red_army_civil_war", 30),
    ("美国对抗布尔什维克主义的秘密战争*", "sources/monographs/foglesong_1995_secret_war_zh", 25),
    ("游牧民族与苏联统治*", "sources/monographs/central_asia_nomads_zh", 25),
]

for pat, out_dir, chunk in JOBS:
    matches = list(INBOX.glob(pat))
    if not matches:
        print(f"SKIP: {pat}")
        continue
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "extract_book.py"),
            "--input",
            str(matches[0]),
            "--out-dir",
            out_dir,
            "--chunk-pages",
            str(chunk),
        ],
        check=True,
    )
