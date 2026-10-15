# -*- coding: utf-8 -*-
"""
generate_dragon_images.py — Xuất bộ ảnh PNG độ nét cao (nền trong suốt) cho 5 loài rồng.
"""
import os
import math
from PIL import Image, ImageDraw

OUTPUT_DIR = r"D:\Pet\rebuild\rust-pet\assets\dragons"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def draw_oriental_dragon(filename, name, main_rgb, sec_rgb, eye_rgb, horn_rgb):
    w, h = 420, 320
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    base_x, base_y = 90, 160
    n = 12

    # 1. Vẽ 12 đốt thân uốn lượn hình sin
    for i in range(n - 1, 0, -1):
        frac = i / n
        radius = max(14, int(36 * (1.0 - frac * 0.45)))
        wave = int(math.sin(i * 0.6) * 32)
        cx = base_x + (i * 26)
        cy = base_y + wave

        # Bờm rồng / Gai sống lưng
        fin_y = cy - radius - 16
        d.polygon([(cx - 8, cy - radius + 4), (cx, fin_y), (cx + 8, cy - radius + 4)], fill=sec_rgb)

        # Đốt thân
        d.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=main_rgb, outline=(20, 20, 25, 230), width=3)
        # Vảy rồng
        d.ellipse([cx - radius + 6, cy - radius + 6, cx + radius - 6, cy + radius - 6], outline=sec_rgb, width=2)

    # Đuôi rồng xòe lửa
    tail_x = base_x + ((n - 1) * 26) + 24
    tail_y = base_y + int(math.sin(n * 0.6) * 32)
    d.polygon([(tail_x - 20, tail_y), (tail_x + 35, tail_y - 20), (tail_x + 55, tail_y), (tail_x + 35, tail_y + 20)], fill=sec_rgb)

    # 2. Đầu rồng
    d.ellipse([base_x - 45, base_y - 45, base_x + 45, base_y + 45], fill=main_rgb, outline=(20, 20, 25, 240), width=4)

    # Mõm rồng
    d.rounded_rectangle([base_x - 75, base_y - 25, base_x - 25, base_y + 25], radius=12, fill=main_rgb, outline=(20, 20, 25, 240), width=3)

    # Sừng Hươu
    d.line([(base_x + 5, base_y - 35), (base_x + 30, base_y - 85), (base_x + 55, base_y - 110)], fill=horn_rgb, width=7)
    d.line([(base_x + 30, base_y - 85), (base_x + 10, base_y - 105)], fill=horn_rgb, width=5)

    # Râu Rồng dài uốn lượn
    d.line([(base_x - 65, base_y + 8), (base_x - 110, base_y + 28), (base_x - 145, base_y + 16)], fill=horn_rgb, width=5)

    # Mắt rồng rực sáng
    d.ellipse([base_x - 30, base_y - 20, base_x - 8, base_y + 2], fill=eye_rgb)
    d.ellipse([base_x - 22, base_y - 14, base_x - 14, base_y - 6], fill=(0, 0, 0, 255))

    # Long châu phát quang
    d.ellipse([base_x - 95, base_y + 40, base_x - 65, base_y + 70], fill=(255, 255, 220, 240), outline=(255, 215, 0, 200), width=3)

    out_path = os.path.join(OUTPUT_DIR, filename)
    im.save(out_path, "PNG")
    print(f"Đã tạo ảnh: {out_path}")

def draw_western_dragon(filename, name, skin_rgb, wing_rgb, eye_rgb, horn_rgb):
    w, h = 420, 320
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    cx, cy = 200, 170

    # 1. Thân rồng cơ bắp
    d.rounded_rectangle([cx - 55, cy - 45, cx + 55, cy + 50], radius=28, fill=skin_rgb, outline=(20, 20, 25, 240), width=4)
    # Ức rồng
    d.rounded_rectangle([cx - 40, cy - 20, cx, cy + 40], radius=14, fill=(255, 240, 210, 230))

    # 2. Đôi Cánh Dơi Khổng Lồ
    wing_left = [(cx - 20, cy - 25), (cx - 100, cy - 120), (cx - 165, cy - 90), (cx - 125, cy + 10), (cx - 55, cy + 20)]
    d.polygon(wing_left, fill=wing_rgb, outline=skin_rgb)
    d.line([(cx - 20, cy - 25), (cx - 165, cy - 90)], fill=skin_rgb, width=6)
    d.line([(cx - 20, cy - 25), (cx - 125, cy + 10)], fill=skin_rgb, width=4)

    wing_right = [(cx + 20, cy - 25), (cx + 100, cy - 120), (cx + 165, cy - 90), (cx + 125, cy + 10), (cx + 55, cy + 20)]
    d.polygon(wing_right, fill=wing_rgb, outline=skin_rgb)
    d.line([(cx + 20, cy - 25), (cx + 165, cy - 90)], fill=skin_rgb, width=6)
    d.line([(cx + 20, cy - 25), (cx + 125, cy + 10)], fill=skin_rgb, width=4)

    # 3. Đuôi rồng gai nhọn
    d.line([(cx + 45, cy + 25), (cx + 110, cy + 45), (cx + 155, cy + 30)], fill=skin_rgb, width=9)
    # Chóp đuôi gai tam giác
    d.polygon([(cx + 150, cy + 15), (cx + 185, cy + 30), (cx + 150, cy + 45)], fill=(30, 30, 35, 255))

    # 4. Đầu rồng & Sừng nhọn
    d.ellipse([cx - 95, cy - 55, cx - 35, cy + 5], fill=skin_rgb, outline=(20, 20, 25, 240), width=4)
    # Sừng quỷ
    d.line([(cx - 65, cy - 45), (cx - 45, cy - 95)], fill=horn_rgb, width=8)

    # Mắt rồng hung hãn
    d.ellipse([cx - 85, cy - 35, cx - 65, cy - 15], fill=eye_rgb)
    d.ellipse([cx - 78, cy - 30, cx - 72, cy - 20], fill=(0, 0, 0, 255))

    out_path = os.path.join(OUTPUT_DIR, filename)
    im.save(out_path, "PNG")
    print(f"Đã tạo ảnh: {out_path}")

# Render 5 loài rồng
draw_oriental_dragon("thanh_long.png", "Thanh Long", (0, 229, 163, 255), (0, 180, 216, 255), (255, 230, 0, 255), (250, 240, 210, 255))
draw_oriental_dragon("hoang_long.png", "Hoàng Long", (255, 215, 0, 255), (255, 69, 0, 255), (0, 255, 200, 255), (255, 245, 180, 255))
draw_oriental_dragon("hac_long.png", "Hắc Long", (138, 43, 226, 255), (75, 0, 130, 255), (255, 30, 80, 255), (200, 180, 255, 255))
draw_western_dragon("hoa_long.png", "Hỏa Long", (255, 59, 48, 255), (255, 140, 50, 230), (255, 220, 0, 255), (45, 45, 55, 255))
draw_western_dragon("bang_long.png", "Băng Long", (90, 200, 250, 255), (180, 235, 255, 230), (255, 255, 255, 255), (220, 245, 255, 255))
print("Hoàn tất xuất 5 ảnh rồng!")
