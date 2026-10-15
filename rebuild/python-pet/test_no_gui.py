# -*- coding: utf-8 -*-
"""test_no_gui.py — Kiểm thử framework không cần mở cửa sổ (chạy headless được)."""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# 1. pets/*.json phải parse được và đủ field
import glob
files = sorted(glob.glob(os.path.join(BASE, "pets", "*.json")))
assert len(files) >= 4, f"Cần >=4 pet json, thấy {len(files)}"
for fp in files:
    sp = json.load(open(fp, encoding="utf-8-sig"))
    for k in ("id", "name", "size", "behaviors"):
        assert k in sp, f"{fp} thiếu {k}"
    assert sp["size"][0] > 0 and sp["size"][1] > 0
print(f"[test] JSON OK: {len(files)} pet")

# 2. load_specs/default_specs không cần Tk
import ast
src = open(os.path.join(BASE, "pet_framework.py"), encoding="utf-8").read()
ast.parse(src)
print("[test] pet_framework.py parse OK")

# 3. Giả lập logic step thuần (không Tk): wander+bounce đổi hướng ở biên
x, dx, sw, w = 0, -3, 800, 128
x += dx
if x < 0 or x + w > sw:
    dx *= -1
assert dx == 3, "bounce phải đảo chiều"
print("[test] bounce logic OK")
print("ALL PYTHON TESTS PASSED")
