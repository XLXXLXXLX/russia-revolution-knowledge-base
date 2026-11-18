#!/usr/bin/env python3
"""检测 Telling October 文件头并提取 Wave 12 的 4 部核心专著。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

corney = next(INBOX.glob("Telling October*"))
head = corney.read_bytes()[:16]
print("Telling October magic bytes:", head)

JOBS = [
    ("Lenin and his Rivals*", "sources/monographs/treadgold_1955_lenin_and_rivals", 30),
    ("俄国旧秩序的危机*", "sources/monographs/manning_1982_crisis_old_order_zh", 25),
    ("斯大林主义与动员政治*", "sources/monographs/priestland_2007_stalinism_mobilization_zh", 25),
    ("乌克兰苏维埃的苏维埃民族政策*", "sources/monographs/liber_1992_soviet_ukraine_zh", 25),
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
