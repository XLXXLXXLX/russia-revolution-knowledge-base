#!/usr/bin/env python3
"""批量提取 Wave 9 的 5 部重要专著与史料集。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("Russia in the Era of NEP*", "sources/monographs/fitzpatrick_1991_russia_era_nep", 30),
    ("Making Workers Soviet*", "sources/monographs/siegelbaum_suny_1994_making_workers_soviet", 30),
    ("Martov and Zinoviev*", "sources/primary/martov_zinoviev_1920_halle", 25),
    ("The Socialist Alternative to Bolshevik Russia*", "sources/monographs/white_2010_sr_alternative", 30),
    ("Tsereteli*", "sources/monographs/roobol_1976_tsereteli", 30),
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
