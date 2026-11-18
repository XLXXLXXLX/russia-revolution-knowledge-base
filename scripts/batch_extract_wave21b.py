#!/usr/bin/env python3
"""批量提取 Wave 21B 的 10 部专著（含泽姆斯科夫档案统计、柯尔《社会主义思想史》3-4卷、社革党研究、列利丘克工业化史、红军建军史、巴林顿·摩尔比较革命史等）。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("俄国社会革命党研究1901-1925.pdf", "sources/monographs/psr_study_1901_1925_zh", 25),
    ("*泽姆斯科夫*", "sources/monographs/zemskov_stalin_era_zh", 25),
    ("工农红军军队建设中的致命错误*", "sources/monographs/smirnov_red_army_1917_1937_zh", 25),
    ("苏联的工业化 历史、经验、问题*", "sources/monographs/lelichuk_soviet_industrialization_zh", 25),
    ("苏联民主与斯大林*", "sources/monographs/soviet_democracy_and_stalin_zh", 25),
    ("弗拉基米尔·列宁：如何成为领袖*", "sources/monographs/lenin_how_became_leader_zh", 25),
    ("专制与民主的社会起源*", "sources/monographs/moore_1966_social_origins_zh", 25),
    ("社会主义思想史 第三卷下*", "sources/monographs/cole_socialist_thought_v3p2_zh", 30),
    ("社会主义思想史 第四卷上*", "sources/monographs/cole_socialist_thought_v4p1_zh", 30),
    ("社会主义思想史 第四卷下*", "sources/monographs/cole_socialist_thought_v4p2_zh", 30),
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
