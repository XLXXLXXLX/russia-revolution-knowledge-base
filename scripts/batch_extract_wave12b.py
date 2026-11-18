#!/usr/bin/env python3
"""提取 Wave 12B 的 3 部专著/一手回忆录并体检全库。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("The Russian Worker Life and Labor*", "sources/primary/bonnell_1983_russian_worker_memoirs", 30),
    ("列宁在1917年*", "sources/monographs/loginov_lenin_in_1917_zh", 25),
    ("罗伯特·瑟维斯 托洛茨基 一部传记*", "sources/monographs/service_2009_trotsky_zh", 25),
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
