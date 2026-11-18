#!/usr/bin/env python3
"""提取张建华《政治激进主义与近代俄国政治》与《斯大林与战争》并体检全库。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("政治激进主义与近代俄国政治*", "sources/monographs/zhang_jianhua_political_radicalism_zh", 30),
    ("斯大林与战争（1918-1953）*", "sources/monographs/stalin_and_war_1918_1953_zh", 25),
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
