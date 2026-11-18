#!/usr/bin/env python3
"""提取莫斯科工人1917、地方风貌与契卡纪事 3 部文献并体检全库。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("莫斯科工人和1917年革命*", "sources/monographs/koenker_1981_moscow_workers_zh", 30),
    ("地方风貌 苏联权力的地方纬度*", "sources/monographs/raleigh_2001_provincial_landscapes_zh", 25),
    ("全俄肃反委员会红色恐怖纪事*", "sources/primary/cheka_red_terror_chronicle_zh", 25),
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
