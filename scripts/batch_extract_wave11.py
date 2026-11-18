#!/usr/bin/env python3
"""批量提取 Wave 11 的 4 部核心专著并体检全库。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("The Making Of Three Russian Revolutionaries*", "sources/monographs/haimson_1987_three_revolutionaries", 30),
    ("Telling October*", "sources/monographs/corney_2004_telling_october", 25),
    ("俄国文化革命(1928-1931)*", "sources/monographs/fitzpatrick_1978_cultural_rev_zh", 25),
    ("布尔什维克如何发薪*", "sources/monographs/ilyukhov_bolshevik_pay_zh", 25),
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

subprocess.run([sys.executable, str(ROOT / "scripts" / "kb.py"), "audit-graph"], check=True)
