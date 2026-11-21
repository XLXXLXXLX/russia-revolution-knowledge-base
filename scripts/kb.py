#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
俄国革命知识库（1860s–1929）核心辅助工具 CLI（Thin Wrapper）
委托执行通用子模块 `framework/engine/kb_core.py`，参数由 `kb_config.yaml` 声明。
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRAMEWORK_DIR = ROOT / "framework"
if str(FRAMEWORK_DIR) not in sys.path:
    sys.path.insert(0, str(FRAMEWORK_DIR))

from engine.kb_core import KBEngine, export_compat_symbols  # noqa: E402

_ENGINE = KBEngine(ROOT)
globals().update(export_compat_symbols(_ENGINE))

if __name__ == "__main__":
    raise SystemExit(_ENGINE.run_cli())
