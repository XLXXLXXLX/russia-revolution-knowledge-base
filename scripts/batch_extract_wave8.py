#!/usr/bin/env python3
"""批量提取 Wave 8 计划的 8 部核心文献。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("*Red Flag Unfurled*", "sources/monographs/suny_2017_red_flag_unfurled_zh", 25),
    ("*Popular Perception Of Soviet Politics*", "sources/monographs/velikanova_2013_popular_perception", 25),
    ("1905 (*佐仓绫奈*", "sources/monographs/trotsky_1905_zh", 30),
    ("Soviet State and Society between Revolutions*", "sources/monographs/siegelbaum_1992_state_and_society", 30),
    ("布尔什维克与民族问题*", "sources/monographs/smith_jeremy_1999_national_question_zh", 25),
    ("走向权力之路的自由主义反对派*", "sources/monographs/gaida_2003_liberal_opposition_zh", 25),
    ("革命何以关于一国建成社会主义*", "sources/primary/socialism_in_one_country_debate_docs_zh", 25),
    ("联共（布）党史简明教程*", "sources/primary/short_course_1938_zh", 30),
]

for pat, out_dir, chunk in JOBS:
    matches = list(INBOX.glob(pat))
    if not matches:
        print(f"SKIP (not found): {pat}")
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
