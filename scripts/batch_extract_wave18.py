#!/usr/bin/env python3
"""提取 Wave 18 的 4 部专著并编译新增 6 张早期革命卡上下文包。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

for pat, out_dir in [
    ("The Mensheviks In The Revolution Of 1917*", "sources/monographs/basil_1984_mensheviks_1917"),
    ("The Russian Revolution, 1900-1927*Service*", "sources/monographs/service_2009_russian_rev"),
    ("苏维埃俄国的工业化 2 苏联集体农庄*", "sources/monographs/davies_1980_collective_farm_zh"),
    ("列宁政治生涯 第一卷*", "sources/monographs/service_lenin_v1_zh"),
]:
    m = list(INBOX.glob(pat))
    if m:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "extract_book.py"), "--input", str(m[0]), "--out-dir", out_dir, "--chunk-pages", "25"],
            check=True,
        )

for cid in ["PER-herzen", "PER-chernyshevsky", "PER-tkachev", "PER-zhelyabov", "ORG-zemlya-i-volya", "ORG-osvobozhdenie-truda"]:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "kb.py"), "pack", cid, "--write"], check=True)

subprocess.run([sys.executable, str(ROOT / "scripts" / "kb.py"), "audit-graph"], check=True)
