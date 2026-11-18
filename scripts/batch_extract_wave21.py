#!/usr/bin/env python3
"""批量提取 Wave 21 的 10 部核心专著与档案汇编（S.A. Smith《红色彼得格勒》、Mawdsley《俄国内战》、Filtzer《苏联工人与斯大林工业化》、捷尔任斯基传、工业国有化档案等）。"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"

JOBS = [
    ("红色彼得格勒：工厂中的革命*", "sources/monographs/smith_sa_1983_red_petrograd_zh", 25),
    ("俄国内战 Evan Mawdsley*", "sources/monographs/mawdsley_1987_civil_war_zh", 25),
    ("Soviet Workers and Stalinist Industrialisation*", "sources/monographs/filtzer_1986_soviet_workers", 25),
    ("塑造苏联工人*", "sources/monographs/siegelbaum_suny_1994_making_workers_zh", 25),
    ("捷尔任斯基从天文学家到钢铁费利克斯*", "sources/monographs/plekhanov_dzerzhinsky_zh", 25),
    ("列宁全传 (弗拉德连·洛吉诺夫)*", "sources/monographs/loginov_lenin_bio_zh", 25),
    ("苏联历史 1917-53纪念 R.W. 戴维斯的论文集*", "sources/monographs/cooper_perrie_1995_davies_festschrift_zh", 25),
    ("苏联工业国有化：1917-1920年文件资料汇编*", "sources/primary/nationalization_docs_1917_1920_zh", 30),
    ("斯大林1878-1953(主要文献)*", "sources/primary/stalin_major_documents_zh", 30),
    ("Socialism-and-the-intelligentsia-1880-1914-Carl-Levy.pdf", "sources/monographs/levy_1987_socialism_intelligentsia", 25),
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
