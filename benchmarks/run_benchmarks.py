#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
俄国革命知识库（1860s–1929）基准评测与维护 CLI（Thin Wrapper）
委托执行通用子模块 `framework/engine/benchmarks_core.py`，参数由 `kb_config.yaml` 声明。
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRAMEWORK_DIR = ROOT / "framework"
if str(FRAMEWORK_DIR) not in sys.path:
    sys.path.insert(0, str(FRAMEWORK_DIR))

from engine.benchmarks_core import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main(ROOT))
