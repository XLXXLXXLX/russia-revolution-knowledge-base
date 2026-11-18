#!/usr/bin/env python3
"""批量提取 Wave 27 的馆藏文献（含 E. H. Carr 十四卷全集 EPUB、列布斯基工业家长制下的苏联工人阶级、苏联妇女史、梁赞诺夫斯基俄国通史等）。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("苏联的工人阶级：工业家长制下的生活（中译本） (Максим Лебский)*", "sources/monographs/lebsky_working_class_paternalism_zh", 25),
    ("苏联妇女 Soviet Women*", "sources/monographs/soviet_women_zh", 25),
    ("苏维埃公民的塑造*", "sources/monographs/making_soviet_citizen_education_zh", 25),
    ("俄罗斯史(第8版)*", "sources/monographs/riasanovsky_steinberg_history_russia_zh", 30),
    ("A History of Soviet Russia.epub", "sources/monographs/carr_complete_14vol_epub", 25),
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
