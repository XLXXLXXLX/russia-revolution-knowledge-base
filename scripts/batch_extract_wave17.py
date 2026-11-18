#!/usr/bin/env python3
"""提取大卫·霍夫曼《培养群众 1914-1939》并重编新增 13 张卡片上下文包与全库体检。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

for pat, out_dir in [
    ("培养群众 现代国家实践与苏联社会主义*", "sources/monographs/hoffmann_2011_cultivating_masses_zh"),
    ("布尔什维克党反对托洛茨基主义的斗争*", "sources/monographs/struggle_against_trotskyism_zh"),
]:
    m = list(INBOX.glob(pat))
    if m:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "extract_book.py"), "--input", str(m[0]), "--out-dir", out_dir, "--chunk-pages", "25"],
            check=True,
        )

new_cids = [
    "PER-milyukov", "PER-stolypin", "PER-kerensky", "PER-tsereteli",
    "PER-kollontai", "PER-sokolnikov", "PER-uglanov",
    "ORG-kadets", "EVT-1905-revolution", "EVT-1917-07-july-days",
    "EVT-1918-01-constituent-assembly-dispersal", "EVT-1928-grain-procurement-crisis",
    "MTG-1917-10-2nd-congress-of-soviets",
]
for cid in new_cids:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "kb.py"), "pack", cid, "--write"], check=True)

subprocess.run([sys.executable, str(ROOT / "scripts" / "kb.py"), "audit-graph"], check=True)
