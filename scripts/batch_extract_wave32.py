#!/usr/bin/env python3
"""提取 Wave 32 的真实文本层中外专著（斯皮岑俄罗斯教科书第3卷 docx、曹维安俄国史新论、温迪·戈德曼发明敌人等）。"""
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

for f in sorted(INBOX.iterdir()):
    name = f.name
    target = None
    if "斯皮岑" in name and name.endswith(".docx"):
        target = "sources/monographs/spitsyn_russia_ussr_v3_zh"
    elif "曹维" in name and name.endswith(".pdf"):
        target = "sources/monographs/cao_weian_new_russian_history_zh"
    elif "发明敌人" in name and name.endswith(".pdf"):
        target = "sources/monographs/goldman_inventing_enemy_zh"
    elif "姚海" in name and name.endswith(".pdf"):
        target = "sources/monographs/yao_hai_russian_rev_v1_zh"
    if target:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "extract_book.py"), "--input", str(f), "--out-dir", target, "--chunk-pages", "25"],
            check=True,
        )
