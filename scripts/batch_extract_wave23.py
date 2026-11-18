#!/usr/bin/env python3
"""批量提取 Wave 23 的 10 部专著与专题论文（法国大革命与俄国革命比较群、卡尔英文版、俄文劳工国家专著、斯皮岑俄国教科书等）。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("The Russian Revolution From Lenin to Stalin*", "sources/monographs/carr_1979_lenin_to_stalin", 25),
    ("The Bolshevik Revolution, 1917-1923, Vol. 1.pdf", "sources/monographs/carr_1950_bolshevik_rev_v1_en", 25),
    ("FRANCE AND THE RUSSIAN REVOLUTIONS*", "sources/monographs/shlapentokh_france_russian_revs", 25),
    ("Frenchmen, Their Revolutionary Heritage*", "sources/monographs/frenchmen_rev_heritage_russia", 25),
    ("The French Revolution and the Russian Revolution*", "sources/monographs/french_and_russian_rev_analogies", 25),
    ("The Jacobin Ancestry of Soviet Communism.pdf", "sources/monographs/jacobin_ancestry_soviet_communism", 25),
    ("The_nineteenth_century_Russian_intellige.pdf", "sources/monographs/nineteenth_c_russian_intelligentsia", 25),
    ("Революция, государство, раб*", "sources/monographs/ru_rev_state_working_class", 25),
    ("俄罗斯-苏联史1917-1945*.docx", "sources/monographs/spitsyn_russia_ussr_v3_zh", 25),
    ("原始的叛乱*", "sources/monographs/hobsbawm_1959_primitive_rebels_zh", 25),
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
