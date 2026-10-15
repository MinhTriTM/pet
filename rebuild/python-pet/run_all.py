# -*- coding: utf-8 -*-
"""run_all.py — Chạy cả 3 pet cùng lúc (mô phỏng 'Nuôi 3 mèo con trên desktop')."""
import subprocess, sys, os
BASE = os.path.dirname(os.path.abspath(__file__))
for script in ["bird.py", "fafa.py", "felix.py"]:
    subprocess.Popen([sys.executable, os.path.join(BASE, script)])
print("Đã khởi động bird + fafa + felix. Chuột phải mỗi con để thoát.")
