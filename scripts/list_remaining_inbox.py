#!/usr/bin/env python3
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent

inv = [json.loads(x) for x in (ROOT / "sources/inbox_inventory.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
extracted_raw = set()
for toc in (ROOT / "sources").rglob("toc.md"):
    txt = toc.read_text(encoding="utf-8", errors="ignore")
    for line in txt.splitlines()[:8]:
        if "原始文件" in line and "`" in line:
            extracted_raw.add(line.split("`")[1])

rem = [r for r in inv if r["filename"] not in extracted_raw and not r["flags"]]
print(f"Already extracted: {len(extracted_raw)}, Remaining clean unextracted: {len(rem)}")
for r in rem:
    print(f"{r['seq']:03d} :: {r['size_kb']:9.1f} KB :: {r['filename']}")
