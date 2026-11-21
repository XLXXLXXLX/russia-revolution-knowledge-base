#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
电子书与期刊论文提取器（Thin Wrapper）
委托执行通用子模块 `framework/engine/extract_book.py`。
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRAMEWORK_DIR = ROOT / "framework"
if str(FRAMEWORK_DIR) not in sys.path:
    sys.path.insert(0, str(FRAMEWORK_DIR))

from engine.extract_book import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main(ROOT))
