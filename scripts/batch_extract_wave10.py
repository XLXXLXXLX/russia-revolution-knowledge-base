#!/usr/bin/env python3
"""批量提取 Wave 10 的 6 部重要专著 + 重编 6 个新建卡片上下文包。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("The Russian Revolution, 1905-1921*Steinberg*", "sources/monographs/steinberg_2017_russian_rev", 30),
    ("妇女、国家与革命*", "sources/monographs/goldman_1993_women_state_rev_zh", 25),
    ("新经济政策的另一面1923-1925*", "sources/monographs/other_side_of_nep_1923_1925_zh", 25),
    ("格里高利·季诺维也夫*", "sources/monographs/zhukov_zinoviev_zh", 25),
    ("The Petrograd armed workers movement*", "sources/monographs/boll_1979_red_guards", 30),
    ("Education and Social Mobility in the Soviet Union 1921-1934*", "sources/monographs/fitzpatrick_1979_education_mobility", 30),
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

for cid in [
    "ORG-mensheviks",
    "ORG-cheka-ogpu",
    "ORG-left-srs",
    "ORG-workers-opposition",
    "CON-socialism-in-one-country",
    "CON-primitive-socialist-accumulation",
]:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "kb.py"), "pack", cid, "--write"], check=True)

subprocess.run([sys.executable, str(ROOT / "scripts" / "kb.py"), "audit-graph"], check=True)
