#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
单进程图谱与译名表同步脚本（Thin Wrapper）
委托执行通用子模块 `framework/engine/sync_graph.py`。
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRAMEWORK_DIR = ROOT / "framework"
if str(FRAMEWORK_DIR) not in sys.path:
    sys.path.insert(0, str(FRAMEWORK_DIR))

from engine.kb_core import KBEngine  # noqa: E402
from engine.sync_graph import main  # noqa: E402

ID_REMAP = KBEngine(ROOT).id_remap

if __name__ == "__main__":
    raise SystemExit(main(ROOT))
