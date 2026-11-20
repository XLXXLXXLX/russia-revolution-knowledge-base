#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通用电子书（PDF / EPUB / DOCX / DjVu）规整提取器 (供 source-extractor 与主控官调用)
可直接用系统 Python 运行（自动挂载本地 .venv/Lib/site-packages）：
  python scripts/extract_book.py --input "inbox/<书名>.pdf" --out-dir "sources/monographs/<slug>" --chunk-pages 25

功能:
  1. PDF: 使用 PyMuPDF (pymupdf) 逐页提取文本，强制注入原始纸书页码锚点 `## [PDF p. N]`；
     若原 PDF 带有书签目录 (TOC)，优先按一级书签切分章节；若无书签或单章过大，则按 `--chunk-pages` 分卷。
  2. EPUB: 按 OPF spine 顺序解析 HTML/XHTML/XML 文档；若遇到逐页切分的 EPUB（>80 个短 page_* 节点），
     自动按 `--chunk-pages` 合并为规范分章，避免产生数百个微碎文件。
  3. DjVu: 原生纯 Python 解析 IFF `FORM:DJVM` / `FORM:DJVU` 结构与 `TXTz`（ZP-Coder + Burrows-Wheeler `BZZ` 压缩层）/ `TXTa` 文本块，
     按 `--chunk-pages` 输出带 `## [DjVu p. N]` 锚点的俄/英/中文分章 Markdown。
  4. 自动汇总产出 `toc.md` 与 `manifest.yaml`（含 `needs_ocr` 自动隔离门禁）。
"""

from __future__ import annotations

import argparse
import re
import struct
import sys
import warnings
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
VENV_SITE = ROOT / ".venv" / "Lib" / "site-packages"
if VENV_SITE.exists() and str(VENV_SITE) not in sys.path:
    sys.path.insert(0, str(VENV_SITE))


def slugify(text: str, max_len: int = 40) -> str:
    text = text.replace("\x00", "")
    s = re.sub(r"[^\w\u4e00-\u9fff\u0400-\u04ff-]+", "_", text.strip())
    s = re.sub(r"_+", "_", s).strip("_").lower()
    return (s[:max_len].rstrip("_")) or "section"


# ============================================================================
# DjVu TXTz (ZPCodec + BSByteStream BWT) 纯 Python 解码器 (依据 DjVuLibre GPL 参考规范)
# ============================================================================

_ZPCODEC_TABLE: list[tuple[int, int, int, int]] = [
    (0x8000, 0x0000, 84, 145), (0x8000, 0x0000, 3, 4), (0x8000, 0x0000, 4, 3), (0x6BBD, 0x10A5, 5, 1),
    (0x6BBD, 0x10A5, 6, 2), (0x5D45, 0x1F28, 7, 3), (0x5D45, 0x1F28, 8, 4), (0x51B9, 0x2BD3, 9, 5),
    (0x51B9, 0x2BD3, 10, 6), (0x4813, 0x36E3, 11, 7), (0x4813, 0x36E3, 12, 8), (0x3FD5, 0x408C, 13, 9),
    (0x3FD5, 0x408C, 14, 10), (0x38B1, 0x48FD, 15, 11), (0x38B1, 0x48FD, 16, 12), (0x3275, 0x505D, 17, 13),
    (0x3275, 0x505D, 18, 14), (0x2CFD, 0x56D0, 19, 15), (0x2CFD, 0x56D0, 20, 16), (0x2825, 0x5C71, 21, 17),
    (0x2825, 0x5C71, 22, 18), (0x23AB, 0x615B, 23, 19), (0x23AB, 0x615B, 24, 20), (0x1F87, 0x65A5, 25, 21),
    (0x1F87, 0x65A5, 26, 22), (0x1BBB, 0x6962, 27, 23), (0x1BBB, 0x6962, 28, 24), (0x1845, 0x6CA2, 29, 25),
    (0x1845, 0x6CA2, 30, 26), (0x1523, 0x6F74, 31, 27), (0x1523, 0x6F74, 32, 28), (0x1253, 0x71E6, 33, 29),
    (0x1253, 0x71E6, 34, 30), (0x0FCF, 0x7404, 35, 31), (0x0FCF, 0x7404, 36, 32), (0x0D95, 0x75D6, 37, 33),
    (0x0D95, 0x75D6, 38, 34), (0x0B9D, 0x7768, 39, 35), (0x0B9D, 0x7768, 40, 36), (0x09E3, 0x78C2, 41, 37),
    (0x09E3, 0x78C2, 42, 38), (0x0861, 0x79EA, 43, 39), (0x0861, 0x79EA, 44, 40), (0x0711, 0x7AE7, 45, 41),
    (0x0711, 0x7AE7, 46, 42), (0x05F1, 0x7BBE, 47, 43), (0x05F1, 0x7BBE, 48, 44), (0x04F9, 0x7C75, 49, 45),
    (0x04F9, 0x7C75, 50, 46), (0x0425, 0x7D0F, 51, 47), (0x0425, 0x7D0F, 52, 48), (0x0371, 0x7D91, 53, 49),
    (0x0371, 0x7D91, 54, 50), (0x02D9, 0x7DFE, 55, 51), (0x02D9, 0x7DFE, 56, 52), (0x0259, 0x7E5A, 57, 53),
    (0x0259, 0x7E5A, 58, 54), (0x01ED, 0x7EA6, 59, 55), (0x01ED, 0x7EA6, 60, 56), (0x0193, 0x7EE6, 61, 57),
    (0x0193, 0x7EE6, 62, 58), (0x0149, 0x7F1A, 63, 59), (0x0149, 0x7F1A, 64, 60), (0x010B, 0x7F45, 65, 61),
    (0x010B, 0x7F45, 66, 62), (0x00D5, 0x7F6B, 67, 63), (0x00D5, 0x7F6B, 68, 64), (0x00A5, 0x7F8D, 69, 65),
    (0x00A5, 0x7F8D, 70, 66), (0x007B, 0x7FAA, 71, 67), (0x007B, 0x7FAA, 72, 68), (0x0057, 0x7FC3, 73, 69),
    (0x0057, 0x7FC3, 74, 70), (0x003B, 0x7FD7, 75, 71), (0x003B, 0x7FD7, 76, 72), (0x0023, 0x7FE7, 77, 73),
    (0x0023, 0x7FE7, 78, 74), (0x0013, 0x7FF2, 79, 75), (0x0013, 0x7FF2, 80, 76), (0x0007, 0x7FFA, 81, 77),
    (0x0007, 0x7FFA, 82, 78), (0x0001, 0x7FFF, 81, 79), (0x0001, 0x7FFF, 82, 80), (0x5695, 0x0000, 9, 85),
    (0x24EE, 0x0000, 86, 226), (0x8000, 0x0000, 5, 6), (0x0D30, 0x0000, 88, 176), (0x481A, 0x0000, 89, 143),
    (0x0481, 0x0000, 90, 138), (0x3579, 0x0000, 91, 141), (0x017A, 0x0000, 92, 112), (0x24EF, 0x0000, 93, 135),
    (0x007B, 0x0000, 94, 104), (0x1978, 0x0000, 95, 133), (0x0028, 0x0000, 96, 100), (0x10CA, 0x0000, 97, 129),
    (0x000D, 0x0000, 82, 98), (0x0B5D, 0x0000, 99, 127), (0x0034, 0x0000, 76, 72), (0x078A, 0x0000, 101, 125),
    (0x00A0, 0x0000, 70, 102), (0x050F, 0x0000, 103, 123), (0x0117, 0x0000, 66, 60), (0x0358, 0x0000, 105, 121),
    (0x01EA, 0x0000, 106, 110), (0x0234, 0x0000, 107, 119), (0x0144, 0x0000, 66, 108), (0x0173, 0x0000, 109, 117),
    (0x0234, 0x0000, 60, 54), (0x00F5, 0x0000, 111, 115), (0x0353, 0x0000, 56, 48), (0x00A1, 0x0000, 69, 113),
    (0x05C5, 0x0000, 114, 134), (0x011A, 0x0000, 65, 59), (0x03CF, 0x0000, 116, 132), (0x01AA, 0x0000, 61, 55),
    (0x0285, 0x0000, 118, 130), (0x0286, 0x0000, 57, 51), (0x01AB, 0x0000, 120, 128), (0x03D3, 0x0000, 53, 47),
    (0x011A, 0x0000, 122, 126), (0x05C5, 0x0000, 49, 41), (0x00BA, 0x0000, 124, 62), (0x08AD, 0x0000, 43, 37),
    (0x007A, 0x0000, 72, 66), (0x0CCC, 0x0000, 39, 31), (0x01EB, 0x0000, 60, 54), (0x1302, 0x0000, 33, 25),
    (0x02E6, 0x0000, 56, 50), (0x1B81, 0x0000, 29, 131), (0x045E, 0x0000, 52, 46), (0x24EF, 0x0000, 23, 17),
    (0x0690, 0x0000, 48, 40), (0x2865, 0x0000, 23, 15), (0x09DE, 0x0000, 42, 136), (0x3987, 0x0000, 137, 7),
    (0x0DC8, 0x0000, 38, 32), (0x2C99, 0x0000, 21, 139), (0x10CA, 0x0000, 140, 172), (0x3B5F, 0x0000, 15, 9),
    (0x0B5D, 0x0000, 142, 170), (0x5695, 0x0000, 9, 85), (0x078A, 0x0000, 144, 168), (0x8000, 0x0000, 141, 248),
    (0x050F, 0x0000, 146, 166), (0x24EE, 0x0000, 147, 247), (0x0358, 0x0000, 148, 164), (0x0D30, 0x0000, 149, 197),
    (0x0234, 0x0000, 150, 162), (0x0481, 0x0000, 151, 95), (0x0173, 0x0000, 152, 160), (0x017A, 0x0000, 153, 173),
    (0x00F5, 0x0000, 154, 158), (0x007B, 0x0000, 155, 165), (0x00A1, 0x0000, 70, 156), (0x0028, 0x0000, 157, 161),
    (0x011A, 0x0000, 66, 60), (0x000D, 0x0000, 81, 159), (0x01AA, 0x0000, 62, 56), (0x0034, 0x0000, 75, 71),
    (0x0286, 0x0000, 58, 52), (0x00A0, 0x0000, 69, 163), (0x03D3, 0x0000, 54, 48), (0x0117, 0x0000, 65, 59),
    (0x05C5, 0x0000, 50, 42), (0x01EA, 0x0000, 167, 171), (0x08AD, 0x0000, 44, 38), (0x0144, 0x0000, 65, 169),
    (0x0CCC, 0x0000, 40, 32), (0x0234, 0x0000, 59, 53), (0x1302, 0x0000, 34, 26), (0x0353, 0x0000, 55, 47),
    (0x1B81, 0x0000, 30, 174), (0x05C5, 0x0000, 175, 193), (0x24EF, 0x0000, 24, 18), (0x03CF, 0x0000, 177, 191),
    (0x2B74, 0x0000, 178, 222), (0x0285, 0x0000, 179, 189), (0x201D, 0x0000, 180, 218), (0x01AB, 0x0000, 181, 187),
    (0x1715, 0x0000, 182, 216), (0x011A, 0x0000, 183, 185), (0x0FB7, 0x0000, 184, 214), (0x00BA, 0x0000, 69, 61),
    (0x0A67, 0x0000, 186, 212), (0x01EB, 0x0000, 59, 53), (0x06E7, 0x0000, 188, 210), (0x02E6, 0x0000, 55, 49),
    (0x0496, 0x0000, 190, 208), (0x045E, 0x0000, 51, 45), (0x030D, 0x0000, 192, 206), (0x0690, 0x0000, 47, 39),
    (0x0206, 0x0000, 194, 204), (0x09DE, 0x0000, 41, 195), (0x0155, 0x0000, 196, 202), (0x0DC8, 0x0000, 37, 31),
    (0x00E1, 0x0000, 198, 200), (0x2B74, 0x0000, 199, 243), (0x0094, 0x0000, 72, 64), (0x201D, 0x0000, 201, 239),
    (0x0188, 0x0000, 62, 56), (0x1715, 0x0000, 203, 237), (0x0252, 0x0000, 58, 52), (0x0FB7, 0x0000, 205, 235),
    (0x0383, 0x0000, 54, 48), (0x0A67, 0x0000, 207, 233), (0x0547, 0x0000, 50, 44), (0x06E7, 0x0000, 209, 231),
    (0x07E2, 0x0000, 46, 38), (0x0496, 0x0000, 211, 229), (0x0BC0, 0x0000, 40, 34), (0x030D, 0x0000, 213, 227),
    (0x1178, 0x0000, 36, 28), (0x0206, 0x0000, 215, 225), (0x19DA, 0x0000, 30, 22), (0x0155, 0x0000, 217, 223),
    (0x24EF, 0x0000, 26, 16), (0x00E1, 0x0000, 219, 221), (0x320E, 0x0000, 20, 220), (0x0094, 0x0000, 71, 63),
    (0x432A, 0x0000, 14, 8), (0x0188, 0x0000, 61, 55), (0x447D, 0x0000, 14, 224), (0x0252, 0x0000, 57, 51),
    (0x5ECE, 0x0000, 8, 2), (0x0383, 0x0000, 53, 47), (0x8000, 0x0000, 228, 87), (0x0547, 0x0000, 49, 43),
    (0x481A, 0x0000, 230, 246), (0x07E2, 0x0000, 45, 37), (0x3579, 0x0000, 232, 244), (0x0BC0, 0x0000, 39, 33),
    (0x24EF, 0x0000, 234, 238), (0x1178, 0x0000, 35, 27), (0x1978, 0x0000, 138, 236), (0x19DA, 0x0000, 29, 21),
    (0x2865, 0x0000, 24, 16), (0x24EF, 0x0000, 25, 15), (0x3987, 0x0000, 240, 8), (0x320E, 0x0000, 19, 241),
    (0x2C99, 0x0000, 22, 242), (0x432A, 0x0000, 13, 7), (0x3B5F, 0x0000, 16, 10), (0x447D, 0x0000, 13, 245),
    (0x5695, 0x0000, 10, 2), (0x5ECE, 0x0000, 7, 1), (0x8000, 0x0000, 244, 83), (0x8000, 0x0000, 249, 250),
    (0x5695, 0x0000, 10, 2), (0x481A, 0x0000, 89, 143), (0x481A, 0x0000, 230, 246),
    (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
]

_ZP_P = [t[0] for t in _ZPCODEC_TABLE]
_ZP_M = [t[1] for t in _ZPCODEC_TABLE]
_ZP_UP = [t[2] for t in _ZPCODEC_TABLE]
_ZP_DN = [t[3] for t in _ZPCODEC_TABLE]
_FFZT = [0] * 256
for _i in range(256):
    _j = _i
    while _j & 0x80:
        _FFZT[_i] += 1
        _j = (_j << 1) & 0xFF


class _ZPDecoder:
    __slots__ = ("buf", "pos", "n", "a", "code", "fence", "delay", "scount", "buffer")

    def __init__(self, data: bytes) -> None:
        self.buf = data
        self.n = len(data)
        self.pos = 0
        self.a = 0
        b0 = data[0] if self.n > 0 else 0xFF
        b1 = data[1] if self.n > 1 else 0xFF
        self.pos = min(2, self.n)
        self.code = (b0 << 8) | b1
        self.delay = 25
        self.scount = 0
        self.buffer = 0
        self._preload()
        self.fence = 0x7FFF if self.code >= 0x8000 else self.code

    def _preload(self) -> None:
        buf = self.buf
        n = self.n
        pos = self.pos
        scount = self.scount
        buffer = self.buffer
        delay = self.delay
        while scount <= 24:
            if pos < n:
                byte = buf[pos]
                pos += 1
            else:
                byte = 0xFF
                delay -= 1
                if delay < 1:
                    raise EOFError("ZPCodec EOF")
            buffer = ((buffer << 8) | byte) & 0xFFFFFFFF
            scount += 8
        self.pos = pos
        self.scount = scount
        self.buffer = buffer
        self.delay = delay

    def decode_raw_bit(self) -> int:
        z = 0x8000 + (self.a >> 1)
        if z > self.code:
            z = 0x10000 - z
            a = self.a + z
            code = self.code + z
            shift = (_FFZT[a & 0xFF] + 8) if a >= 0xFF00 else _FFZT[(a >> 8) & 0xFF]
            scount = self.scount - shift
            self.scount = scount
            self.a = (a << shift) & 0xFFFF
            self.code = ((code << shift) & 0xFFFF) | ((self.buffer >> scount) & ((1 << shift) - 1))
            if scount < 16:
                self._preload()
            self.fence = 0x7FFF if self.code >= 0x8000 else self.code
            return 1
        else:
            scount = self.scount - 1
            self.scount = scount
            self.a = (z << 1) & 0xFFFF
            self.code = ((self.code << 1) & 0xFFFF) | ((self.buffer >> scount) & 1)
            if scount < 16:
                self._preload()
            self.fence = 0x7FFF if self.code >= 0x8000 else self.code
            return 0

    def decode_ctx(self, ctx_arr: bytearray, idx: int) -> int:
        c = ctx_arr[idx]
        z = self.a + _ZP_P[c]
        if z <= self.fence:
            self.a = z
            return c & 1
        bit = c & 1
        d = 0x6000 + ((z + self.a) >> 2)
        if z > d:
            z = d
        if z > self.code:
            z = 0x10000 - z
            a = self.a + z
            code = self.code + z
            ctx_arr[idx] = _ZP_DN[c]
            shift = (_FFZT[a & 0xFF] + 8) if a >= 0xFF00 else _FFZT[(a >> 8) & 0xFF]
            scount = self.scount - shift
            self.scount = scount
            self.a = (a << shift) & 0xFFFF
            self.code = ((code << shift) & 0xFFFF) | ((self.buffer >> scount) & ((1 << shift) - 1))
            if scount < 16:
                self._preload()
            self.fence = 0x7FFF if self.code >= 0x8000 else self.code
            return bit ^ 1
        else:
            if self.a >= _ZP_M[c]:
                ctx_arr[idx] = _ZP_UP[c]
            scount = self.scount - 1
            self.scount = scount
            self.a = (z << 1) & 0xFFFF
            self.code = ((self.code << 1) & 0xFFFF) | ((self.buffer >> scount) & 1)
            if scount < 16:
                self._preload()
            self.fence = 0x7FFF if self.code >= 0x8000 else self.code
            return bit


def _decode_bzz(comp: bytes) -> bytes:
    """Decompress DjVu BZZ (BSByteStream) payload into raw bytes."""
    zp = _ZPDecoder(comp)
    ctx = bytearray(300)
    out_chunks: list[bytes] = []
    decode_ctx = zp.decode_ctx
    decode_raw_bit = zp.decode_raw_bit

    while True:
        # decode_raw(zp, 24)
        n = 1
        while n < (1 << 24):
            n = (n << 1) | decode_raw_bit()
        size = n - (1 << 24)
        if size == 0:
            break
        if size > 4096 * 1024:
            raise ValueError(f"Invalid BZZ block size: {size}")

        fshift = 0
        if decode_raw_bit():
            fshift += 1
            if decode_raw_bit():
                fshift += 1

        mtf = bytearray(range(256))
        freq = [0, 0, 0, 0]
        fadd = 4
        mtfno = 3
        markerpos = -1
        data = bytearray(size)

        for i in range(size):
            ctxid = 2 if mtfno > 2 else mtfno
            if decode_ctx(ctx, ctxid):
                mtfno = 0
                ch = mtf[0]
                data[i] = ch
            elif decode_ctx(ctx, 3 + ctxid):
                mtfno = 1
                ch = mtf[1]
                data[i] = ch
            else:
                # Tree bins: (base_cx, bits, offset_val)
                # cx offsets from BSByteStream.cpp:
                # 6 (1 bit, +2), 8 (2b, +4), 12 (3b, +8), 20 (4b, +16), 36 (5b, +32), 68 (6b, +64), 132 (7b, +128)
                matched = False
                cx = 6
                for bits in range(1, 8):
                    if decode_ctx(ctx, cx):
                        val = 1
                        lim = 1 << bits
                        base = cx  # ctx_sub = (cx + 1) - 1 = cx
                        while val < lim:
                            val = (val << 1) | decode_ctx(ctx, base + val)
                        mtfno = lim + (val - lim)
                        ch = mtf[mtfno]
                        data[i] = ch
                        matched = True
                        break
                    cx += 1 << bits
                if not matched:
                    mtfno = 256
                    data[i] = 0
                    markerpos = i
                    continue

            # Rotate MTF according to empirical frequencies
            fadd = fadd + (fadd >> fshift)
            if fadd > 0x10000000:
                fadd >>= 24
                freq[0] >>= 24
                freq[1] >>= 24
                freq[2] >>= 24
                freq[3] >>= 24
            fc = fadd + (freq[mtfno] if mtfno < 4 else 0)
            k = mtfno
            if k >= 4:
                mtf[4 : k + 1] = mtf[3:k]
                k = 3
            while k > 0 and fc >= freq[k - 1]:
                mtf[k] = mtf[k - 1]
                freq[k] = freq[k - 1]
                k -= 1
            mtf[k] = ch
            freq[k] = fc

        if markerpos < 1 or markerpos >= size:
            raise ValueError("Corrupt BZZ markerpos")

        count = [0] * 256
        posn = [0] * size
        for i in range(markerpos):
            c = data[i]
            posn[i] = (c << 24) | (count[c] & 0xFFFFFF)
            count[c] += 1
        for i in range(markerpos + 1, size):
            c = data[i]
            posn[i] = (c << 24) | (count[c] & 0xFFFFFF)
            count[c] += 1

        last = 1
        for c in range(256):
            tmp = count[c]
            count[c] = last
            last += tmp

        out = bytearray(size - 1)
        idx = 0
        last = size - 1
        while last > 0:
            n_val = posn[idx]
            c = n_val >> 24
            last -= 1
            out[last] = c
            idx = count[c] + (n_val & 0xFFFFFF)
        if idx != markerpos:
            raise ValueError("Corrupt BZZ inverse BWT")
        out_chunks.append(bytes(out))

    return b"".join(out_chunks)


def _decode_djvu_text_chunk(chunk_id: bytes, payload: bytes) -> str:
    raw = _decode_bzz(payload) if chunk_id == b"TXTz" else payload
    if len(raw) < 3:
        return ""
    text_len = (raw[0] << 16) | (raw[1] << 8) | raw[2]
    utf8_bytes = raw[3 : 3 + text_len]
    txt = utf8_bytes.decode("utf-8", errors="replace")
    # Normalize DjVu zone control separators (VT=0x0b, GS=0x1d, US=0x1f)
    txt = txt.replace("\x00", "").replace("\x0b", "\n\n").replace("\x1d", "\n\n").replace("\x1f", "\n\n")
    txt = re.sub(r"[ \t]+\n", "\n", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt.strip()


def _iter_djvu_pages(buf: bytes) -> list[str]:
    """Walk IFF FORM:DJVM / FORM:DJVU chunks and return per-page extracted text."""
    mv = memoryview(buf)
    start = 4 if bytes(mv[:4]) == b"AT&T" else 0
    pages: list[str] = []

    def walk_iff(offset: int, limit: int) -> None:
        pos = offset
        while pos + 8 <= limit:
            cid = bytes(mv[pos : pos + 4])
            sz = struct.unpack(">I", mv[pos + 4 : pos + 8])[0]
            body_start = pos + 8
            body_end = min(body_start + sz, limit)
            if cid == b"FORM" and body_start + 4 <= body_end:
                form_type = bytes(mv[body_start : body_start + 4])
                if form_type == b"DJVM":
                    walk_iff(body_start + 4, body_end)
                elif form_type == b"DJVU":
                    # Single DjVu page: find TXTz or TXTa inside this page
                    p_pos = body_start + 4
                    page_txt = ""
                    while p_pos + 8 <= body_end:
                        sub_id = bytes(mv[p_pos : p_pos + 4])
                        sub_sz = struct.unpack(">I", mv[p_pos + 4 : p_pos + 8])[0]
                        sub_end = min(p_pos + 8 + sub_sz, body_end)
                        if sub_id in (b"TXTz", b"TXTa"):
                            page_txt = _decode_djvu_text_chunk(sub_id, bytes(mv[p_pos + 8 : sub_end]))
                            break
                        p_pos = sub_end + (sub_sz & 1)
                    pages.append(page_txt)
            pos = body_end + (sz & 1)

    walk_iff(start, len(buf))
    return pages


def extract_djvu(djvu_path: Path, out_dir: Path, chunk_pages: int) -> tuple[list[dict], dict]:
    buf = djvu_path.read_bytes()
    pages = _iter_djvu_pages(buf)
    total_pages = len(pages)
    empty_pages = 0
    written: list[dict] = []

    cur = 1
    idx = 0
    while cur <= total_pages:
        sub_end = min(cur + chunk_pages - 1, total_pages)
        title = f"Pages {cur}-{sub_end}"
        fn = f"ch{idx:02d}_{slugify(title)}.md"
        lines: list[str] = [
            f"# {title}",
            "",
            f"> 原书文件名: `{djvu_path.name}` | DjVu 页码区间: `pp. {cur}–{sub_end}` / 总 {total_pages} 页",
            "",
        ]
        for pno in range(cur, sub_end + 1):
            ptxt = pages[pno - 1]
            if not ptxt:
                empty_pages += 1
            lines.append(f"## [DjVu p. {pno}]")
            lines.append("")
            lines.append(ptxt if ptxt else "_[本页无嵌入式文本层，可能为空白页、插图或纯扫描图像]_")
            lines.append("")

        content = "\n".join(lines).strip() + "\n"
        (out_dir / fn).write_text(content, encoding="utf-8")
        written.append(
            {
                "file": fn,
                "title": title,
                "pdf_pages": f"djvu:{cur}-{sub_end}",
                "lines": content.count("\n"),
                "chars": len(content),
            }
        )
        cur = sub_end + 1
        idx += 1

    empty_ratio = empty_pages / max(total_pages, 1)
    return written, {"total_pages": total_pages, "empty_pages": empty_pages, "empty_ratio": round(empty_ratio, 4)}


def extract_pdf(pdf_path: Path, out_dir: Path, chunk_pages: int) -> tuple[list[dict], dict]:
    import pymupdf

    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    raw_toc = doc.get_toc()  # [[lvl, title, page_1based], ...]

    # 选取 L1 (或 L1+L2 当 L1 过少时) 书签切分
    l1 = [(t.strip(), max(1, min(p, total_pages))) for lvl, t, p in raw_toc if lvl == 1 and 1 <= p <= total_pages]
    if len(l1) < 3:
        l1 = [(t.strip(), max(1, min(p, total_pages))) for lvl, t, p in raw_toc if lvl in (1, 2) and 1 <= p <= total_pages]

    ranges: list[tuple[str, int, int]] = []
    if len(l1) >= 3:
        if l1[0][1] > 1:
            ranges.append(("frontmatter", 1, l1[0][1] - 1))
        for idx, (title, start_p) in enumerate(l1):
            end_p = l1[idx + 1][1] - 1 if idx + 1 < len(l1) else total_pages
            if end_p < start_p:
                end_p = start_p
            if (end_p - start_p + 1) > chunk_pages * 2:
                part_no = 1
                cur = start_p
                while cur <= end_p:
                    sub_end = min(cur + chunk_pages - 1, end_p)
                    ranges.append((f"{title} (Part {part_no})", cur, sub_end))
                    cur = sub_end + 1
                    part_no += 1
            else:
                ranges.append((title, start_p, end_p))
    else:
        cur = 1
        while cur <= total_pages:
            sub_end = min(cur + chunk_pages - 1, total_pages)
            ranges.append((f"Pages {cur}-{sub_end}", cur, sub_end))
            cur = sub_end + 1

    written: list[dict] = []
    empty_pages = 0
    for idx, (title, sp, ep) in enumerate(ranges):
        fn = f"ch{idx:02d}_{slugify(title)}.md"
        lines: list[str] = [
            f"# {title}",
            "",
            f"> 原书文件名: `{pdf_path.name}` | PDF 页码区间: `pp. {sp}–{ep}` / 总 {total_pages} 页",
            "",
        ]
        for pno in range(sp, ep + 1):
            page_txt = doc[pno - 1].get_text("text").replace("\x00", "").strip()
            if not page_txt:
                empty_pages += 1
            lines.append(f"## [PDF p. {pno}]")
            lines.append("")
            lines.append(page_txt if page_txt else "_[本页无嵌入式文本层，可能为空白页、插图或纯扫描图像]_")
            lines.append("")

        content = "\n".join(lines).strip() + "\n"
        dest = out_dir / fn
        dest.write_text(content, encoding="utf-8")
        written.append(
            {
                "file": fn,
                "title": title,
                "pdf_pages": f"{sp}-{ep}",
                "lines": content.count("\n"),
                "chars": len(content),
            }
        )

    doc.close()
    empty_ratio = empty_pages / max(total_pages, 1)
    return written, {"total_pages": total_pages, "empty_pages": empty_pages, "empty_ratio": round(empty_ratio, 4)}


def extract_docx(docx_path: Path, out_dir: Path) -> tuple[list[dict], dict]:
    with zipfile.ZipFile(docx_path, "r") as zf:
        xml_bytes = zf.read("word/document.xml")
    root = ET.fromstring(xml_bytes)
    paragraphs: list[str] = []
    for p in root.findall(".//{*}p"):
        texts = [t.text for t in p.findall(".//{*}t") if t.text]
        line = "".join(texts).strip()
        if line:
            paragraphs.append(line)
    body = "\n\n".join(paragraphs)
    fn = "ch00_full_document.md"
    content = f"# {docx_path.stem}\n\n> 原书文件名: `{docx_path.name}` | DOCX 提取\n\n{body}\n"
    (out_dir / fn).write_text(content, encoding="utf-8")
    written = [
        {
            "file": fn,
            "title": docx_path.stem,
            "pdf_pages": "docx:all",
            "lines": content.count("\n"),
            "chars": len(content),
        }
    ]
    return written, {"total_pages": 1, "empty_pages": 0 if body else 1, "empty_ratio": 0.0 if body else 1.0}


def extract_epub(epub_path: Path, out_dir: Path, chunk_pages: int = 25) -> tuple[list[dict], dict]:
    from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning

    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

    written: list[dict] = []
    with zipfile.ZipFile(epub_path, "r") as zf:
        names = set(zf.namelist())
        spine_files: list[str] = []

        if "META-INF/container.xml" in names:
            try:
                c_root = ET.fromstring(zf.read("META-INF/container.xml"))
                rf = c_root.find(".//{*}rootfile")
                if rf is not None and rf.attrib.get("full-path") in names:
                    opf_path = rf.attrib["full-path"]
                    opf_dir = Path(opf_path).parent.as_posix()
                    opf_root = ET.fromstring(zf.read(opf_path))
                    manifest_map: dict[str, str] = {}
                    for item in opf_root.findall(".//{*}manifest/{*}item"):
                        iid = item.attrib.get("id", "")
                        href = item.attrib.get("href", "")
                        full_href = f"{opf_dir}/{href}".lstrip("./") if opf_dir != "." else href
                        manifest_map[iid] = full_href
                    for itemref in opf_root.findall(".//{*}spine/{*}itemref"):
                        idref = itemref.attrib.get("idref", "")
                        target = manifest_map.get(idref, "")
                        if target in names:
                            spine_files.append(target)
            except Exception:
                spine_files = []

        if not spine_files:
            spine_files = sorted(
                n
                for n in names
                if n.lower().endswith((".xhtml", ".html", ".htm", ".xml"))
                and not n.lower().startswith("meta-inf/")
                and not n.lower().endswith(("toc.ncx", "container.xml", "content.opf", "package.opf"))
            )

        parsed_items: list[tuple[str, str, str]] = []
        for sp_file in spine_files:
            raw = zf.read(sp_file)
            soup = BeautifulSoup(raw, "lxml")
            body_root = soup.body if soup.body else soup
            h_tag = body_root.find(["h1", "h2", "h3", "h4"]) or soup.find("title")
            title = h_tag.get_text(" ", strip=True) if h_tag else Path(sp_file).stem
            txt = soup.get_text("\n", strip=True).replace("\x00", "")
            if len(txt) < 80:
                continue
            parsed_items.append((sp_file, title, txt))

        # 检测是否为逐页切分型 EPUB (如 content/page_001.xml，超过 80 个短节点)
        avg_chars = (sum(len(x[2]) for x in parsed_items) / len(parsed_items)) if parsed_items else 0
        is_per_page_epub = len(parsed_items) > 80 and avg_chars < 4000

        if is_per_page_epub:
            sec_idx = 0
            for start_i in range(0, len(parsed_items), chunk_pages):
                batch = parsed_items[start_i : start_i + chunk_pages]
                first_sp, first_title, _ = batch[0]
                last_sp = batch[-1][0]
                grp_title = f"Items {start_i + 1}-{start_i + len(batch)} ({first_title[:36]})"
                fn = f"ch{sec_idx:02d}_{slugify(f'pages_{start_i + 1}_{start_i + len(batch)}')}.md"
                lines = [
                    f"# {grp_title}",
                    "",
                    f"> 原书文件名: `{epub_path.name}` | EPUB 合并区间: `{first_sp}` – `{last_sp}`",
                    "",
                ]
                for sp_f, it_title, it_txt in batch:
                    lines.append(f"## [EPUB Item: {sp_f} | {it_title}]")
                    lines.append("")
                    lines.append(it_txt)
                    lines.append("")
                content = "\n".join(lines).strip() + "\n"
                (out_dir / fn).write_text(content, encoding="utf-8")
                written.append(
                    {
                        "file": fn,
                        "title": grp_title,
                        "pdf_pages": f"epub:{first_sp}..{last_sp}",
                        "lines": content.count("\n"),
                        "chars": len(content),
                    }
                )
                sec_idx += 1
        else:
            for sec_idx, (sp_file, title, txt) in enumerate(parsed_items):
                if len(txt) < 120:
                    continue
                fn = f"ch{sec_idx:02d}_{slugify(title)}.md"
                content = (
                    f"# {title}\n\n"
                    f"> 原书文件名: `{epub_path.name}` | EPUB 内部路径: `{sp_file}`\n\n"
                    f"{txt}\n"
                )
                (out_dir / fn).write_text(content, encoding="utf-8")
                written.append(
                    {
                        "file": fn,
                        "title": title,
                        "pdf_pages": f"epub:{sp_file}",
                        "lines": content.count("\n"),
                        "chars": len(content),
                    }
                )

    return written, {"total_pages": len(written), "empty_pages": 0, "empty_ratio": 0.0 if written else 1.0}


def write_master_toc_and_manifest(book_name: str, out_dir: Path, written: list[dict], stats: dict) -> bool:
    import yaml

    needs_ocr = stats.get("empty_ratio", 0.0) >= 0.85 or len(written) == 0
    total_lines = sum(w["lines"] for w in written)
    total_chars = sum(w["chars"] for w in written)
    guidance = (
        "⚠️ **纯图像扫描告警 (`needs_ocr: true`)**：本文件空白文本页占比高达 "
        f"`{stats.get('empty_ratio', 0.0):.1%}`，已自动隔离！`close-reader` 严禁读取空壳占位章节，待 OCR 后方可入库精读。"
        if needs_ocr
        else "请直接按下方文件名使用 `read` 工具（`offset=1, limit=1800` 翻页）连续顺读整章，严禁使用 `grep` 断章取义。"
    )
    toc_lines = [
        "# 文献分章与行号目录索引 (`toc.md`)",
        "",
        f"- **原始文件**: `{book_name}`",
        f"- **规整目录**: `{out_dir.relative_to(ROOT).as_posix() if out_dir.is_relative_to(ROOT) else out_dir.as_posix()}`",
        f"- **章节总数**: `{len(written)}` | **总行数**: `{total_lines}` | **总字符数**: `{total_chars}` | **needs_ocr**: `{str(needs_ocr).lower()}`",
        f"- **精读指引 (`close-reader`)**: {guidance}",
        "",
        "| 序号 | 章节文件 | 章节标题 | 页码/来源锚点 | 总行数 | 字符数 |",
        "| ---: | :--- | :--- | :--- | ---: | ---: |",
    ]
    for i, w in enumerate(written):
        toc_lines.append(
            f"| {i:02d} | `{w['file']}` | {w['title'].replace('|', '｜')} | `{w['pdf_pages']}` | `{w['lines']}` | `{w['chars']}` |"
        )
    (out_dir / "toc.md").write_text("\n".join(toc_lines) + "\n", encoding="utf-8")

    mf_path = out_dir / "manifest.yaml"
    mf_data = yaml.safe_load(mf_path.read_text(encoding="utf-8")) if mf_path.exists() else {}
    if not isinstance(mf_data, dict):
        mf_data = {}
    mf_data.setdefault("slug", out_dir.name)
    mf_data.setdefault("category", out_dir.parent.name)
    mf_data.setdefault("epistemic_tier", "S" if out_dir.parent.name == "primary" else "A")
    mf_data["source_file"] = book_name
    mf_data["chapter_count"] = len(written)
    mf_data["empty_page_ratio"] = stats.get("empty_ratio", 0.0)
    mf_data["needs_ocr"] = needs_ocr
    if needs_ocr:
        mf_data["ocr_note"] = "Auto-quarantined by extract_book.py: >=85% pages lack embedded text layer."
    elif "ocr_note" in mf_data:
        del mf_data["ocr_note"]
    mf_path.write_text(yaml.safe_dump(mf_data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return needs_ocr


def main() -> int:
    parser = argparse.ArgumentParser(description="提取 inbox/ 电子书为分章带页码 Markdown 与 toc.md")
    parser.add_argument("--input", required=True, help="输入电子书路径，如 inbox/xxx.pdf")
    parser.add_argument("--out-dir", required=True, help="输出目录，如 sources/monographs/cohen_1973_bukharin")
    parser.add_argument("--chunk-pages", type=int, default=25, help="无书签、DjVu 或逐页 EPUB 的分页粒度 (默认 25 页)")
    args = parser.parse_args()

    in_path = Path(args.input)
    if not in_path.is_absolute():
        in_path = ROOT / in_path
    if not in_path.exists():
        print(f"错误: 找不到输入文件 {in_path}", file=sys.stderr)
        return 1

    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = ROOT / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    # 清理旧 ch*.md 以避免重提时残留旧切片
    for old_ch in out_dir.glob("ch*.md"):
        old_ch.unlink()

    ext = in_path.suffix.lower()
    if ext == ".pdf":
        written, stats = extract_pdf(in_path, out_dir, args.chunk_pages)
    elif ext == ".epub":
        written, stats = extract_epub(in_path, out_dir, args.chunk_pages)
    elif ext == ".docx":
        written, stats = extract_docx(in_path, out_dir)
    elif ext == ".djvu":
        written, stats = extract_djvu(in_path, out_dir, args.chunk_pages)
    else:
        print(f"暂不支持自动提取后缀 {ext}，请使用专用脚本处理", file=sys.stderr)
        return 1

    needs_ocr = write_master_toc_and_manifest(in_path.name, out_dir, written, stats)
    ocr_flag = " [⚠️ 检出纯扫描无文字层，已自动标记 needs_ocr: true 隔离]" if needs_ocr else ""
    print(
        f"✅ 提取完成: `{in_path.name}` -> `{out_dir.relative_to(ROOT).as_posix()}` "
        f"(共 {len(written)} 章, 合计 {sum(w['chars'] for w in written)} 字符, 已生成 toc.md & manifest.yaml){ocr_flag}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
