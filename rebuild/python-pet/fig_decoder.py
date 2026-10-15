# -*- coding: utf-8 -*-
"""
fig_decoder.py — Giải mã sprite FIG1 của Felix ScreenMate (AdTools 1999).
Phát hiện từ phân tích ngược felix.exe:
- 31 resource custom (id 301..329, 1200) đều bắt đầu bằng b'FIG1'
- Sau header 16 byte là dữ liệu zlib (khớp chuỗi 'inflate 1.1.2')
- IDB_PAL (1334 byte) là palette
Định dạng FIG1 (suy đoán từ header):
  0-3: 'FIG1', 4-5: 0xFFFF, 6: version, 7-..: w,h,x,y + size nén
Hàm decode_fig() trả về bytes đã giải nén để bản remake dùng dần.
"""
import struct
import zlib


def decode_fig(data, header_len=18):
    """Trả về dict {header, payload} hoặc None nếu không phải FIG1."""
    if data[:4] != b"FIG1":
        return None
    header = data[:header_len]
    comp = data[header_len:]
    try:
        raw = zlib.decompress(comp)
    except Exception as e:
        return {"header": header, "error": str(e), "raw": b""}
    return {"header": header, "raw": raw}


if __name__ == "__main__":
    import glob, os
    for p in sorted(glob.glob(r"D:\Pet\rebuild\assets\felix\None_*.bin"))[:5]:
        d = open(p, "rb").read()
        r = decode_fig(d)
        print(os.path.basename(p), "header=", d[:16].hex(), "raw_len=", len(r["raw"]) if r else 0)
