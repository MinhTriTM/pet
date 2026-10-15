# -*- coding: utf-8 -*-
"""
generate_pixel_dragons.py — Tạo bộ ảnh Pixel Art Chibi Anime tinh xảo cho 5 loài rồng.
Phong cách: Shimeji Desktop Pet / Game Retro JRPG cao cấp, viền rõ nét, đổ bóng 3D, mắt anime lấp lánh.
"""
import os
import math
from PIL import Image, ImageDraw, ImageFilter

OUTPUT_DIR = r"D:\Pet\rebuild\rust-pet\assets\dragons"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def draw_chibi_oriental_dragon(filename, name, palette):
    """
    palette: dict chứa các màu:
    bg_out, body_dark, body_mid, body_light, mane_col, horn_col, eye_col, orb_col
    """
    w, h = 320, 260
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    base_x, base_y = 100, 130

    # 1. Vẽ thân rồng uốn lượn S-Curve mềm mại (8 đốt thân to tròn Chibi)
    body_points = []
    radii = []
    for i in range(9):
        t = i / 8.0
        angle = t * math.pi * 1.8
        bx = base_x + int(t * 150)
        by = base_y + int(math.sin(angle) * 35) + int(t * 15)
        body_points.append((bx, by))
        radii.append(int(26 * (1.0 - t * 0.45)))

    # Vẽ từ đuôi lên đầu để tạo chiều sâu lớp (z-index)
    for i in range(8, 0, -1):
        cx, cy = body_points[i]
        r = radii[i]

        # Bờm lưng / Vi cá bồng bềnh
        for off in [-4, 0, 4]:
            d.polygon([
                (cx + off, cy - r + 3),
                (cx + off + 3, cy - r - 16),
                (cx + off + 10, cy - r + 3)
            ], fill=palette["mane_col"], outline=palette["bg_out"])

        # Viền ngoài đậm
        d.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], fill=palette["bg_out"])
        # Đốt thân chính (Shading bóng dưới)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=palette["body_dark"])
        # Midtone thân
        d.ellipse([cx - r + 3, cy - r + 1, cx + r - 3, cy + r - 3], fill=palette["body_mid"])
        # Highlight sáng phía trên
        d.ellipse([cx - r + 6, cy - r + 2, cx + r - 10, cy + r - 10], fill=palette["body_light"])

        # Vảy rồng hình bán nguyệt
        if i % 2 == 0:
            d.arc([cx - r + 8, cy - 4, cx + r - 8, cy + 10], start=0, end=180, fill=palette["mane_col"], width=2)

    # Đuôi xòe lửa Chibi thần thoại
    tx, ty = body_points[-1]
    tail_pts = [
        (tx - 5, ty - 5), (tx + 25, ty - 22), (tx + 45, ty - 10),
        (tx + 60, ty), (tx + 40, ty + 18), (tx + 20, ty + 12)
    ]
    d.polygon(tail_pts, fill=palette["mane_col"], outline=palette["bg_out"])
    d.polygon([(tx + 5, ty - 2), (tx + 35, ty - 8), (tx + 25, ty + 6)], fill=palette["body_light"])

    # 2. Đầu Rồng Chibi Anime siêu dễ thương
    hx, hy = base_x - 10, base_y - 15
    hr = 46

    # Viền đầu
    d.ellipse([hx - hr - 4, hy - hr - 4, hx + hr + 4, hy + hr + 4], fill=palette["bg_out"])
    # Nền đầu rồng
    d.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=palette["body_mid"])
    # Highlight trán
    d.ellipse([hx - hr + 12, hy - hr + 6, hx + hr - 14, hy - 4], fill=palette["body_light"])

    # Mõm rồng Chibi tròn bầu bĩnh
    d.rounded_rectangle([hx - 58, hy - 8, hx - 12, hy + 32], radius=14, fill=palette["body_mid"], outline=palette["bg_out"], width=3)
    d.ellipse([hx - 48, hy + 2, hx - 30, hy + 18], fill=palette["body_light"])
    # Lỗ mũi rồng xinh xắn
    d.ellipse([hx - 52, hy + 8, hx - 48, hy + 14], fill=palette["bg_out"])

    # Sừng hươu quý phái phân nhánh
    horn = palette["horn_col"]
    d.polygon([(hx + 5, hy - 25), (hx + 28, hy - 65), (hx + 38, hy - 60), (hx + 15, hy - 20)], fill=horn, outline=palette["bg_out"])
    d.polygon([(hx + 22, hy - 48), (hx + 42, hy - 58), (hx + 44, hy - 52), (hx + 24, hy - 42)], fill=horn, outline=palette["bg_out"])

    # Bờm tóc rồng bồng bềnh
    for bx, by, r in [(hx + 20, hy - 15, 18), (hx + 28, hy + 5, 20), (hx + 18, hy + 25, 16)]:
        d.ellipse([bx - r, by - r, bx + r, by + r], fill=palette["mane_col"], outline=palette["bg_out"], width=2)

    # Râu rồng dài mềm mại
    d.line([(hx - 45, hy + 16), (hx - 75, hy + 38), (hx - 100, hy + 32)], fill=horn, width=4)
    d.line([(hx - 75, hy + 38), (hx - 95, hy + 50)], fill=horn, width=3)

    # 3. MẮT ANIME CHIBI LONG LANH
    ex, ey = hx - 18, hy - 6
    # Tròng trắng
    d.ellipse([ex - 15, ey - 18, ex + 15, ey + 18], fill=(255, 255, 255, 255), outline=palette["bg_out"], width=3)
    # Tròng màu mắt
    d.ellipse([ex - 12, ey - 15, ex + 12, ey + 15], fill=palette["eye_col"])
    # Con ngươi đen
    d.ellipse([ex - 9, ey - 10, ex + 9, ey + 12], fill=(15, 15, 25, 255))
    # 2 đốm sáng phản chiếu (Anime Sparkle)
    d.ellipse([ex - 6, ey - 8, ex + 2, ey], fill=(255, 255, 255, 255))
    d.ellipse([ex + 2, ey + 4, ex + 7, ey + 9], fill=(255, 255, 255, 255))

    # Má hồng Chibi đáng yêu
    d.ellipse([hx - 36, hy + 16, hx - 20, hy + 26], fill=(255, 130, 150, 160))

    # 4. DẠ MINH CHÂU (Long Châu phát quang huyền ảo)
    ox, oy = hx - 72, hy + 58
    # Hào quang mờ
    for gr in range(22, 10, -3):
        d.ellipse([ox - gr, oy - gr, ox + gr, oy + gr], fill=(255, 245, 180, 40))
    # Viên ngọc chính
    d.ellipse([ox - 12, oy - 12, ox + 12, oy + 12], fill=palette["orb_col"], outline=palette["bg_out"], width=2)
    d.ellipse([ox - 7, oy - 7, ox - 1, oy - 1], fill=(255, 255, 255, 240))

    out_path = os.path.join(OUTPUT_DIR, filename)
    im.save(out_path, "PNG")
    print(f"✅ Hoàn thành Pixel Art: {out_path}")

def draw_chibi_western_dragon(filename, name, palette):
    """
    Rồng Phương Tây Chibi: Cánh dơi uy lực, đầu sừng cute, đuôi gai, vảy rực rỡ.
    """
    w, h = 320, 260
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    cx, cy = 160, 145

    # 1. Đôi Cánh Dơi Khổng Lồ (Vẽ lớp sau lưng)
    w_col = palette["wing_col"]
    sk_dark = palette["body_dark"]
    sk_mid = palette["body_mid"]
    bg_out = palette["bg_out"]

    # Cánh Trái
    wing_l = [(cx - 20, cy - 20), (cx - 95, cy - 105), (cx - 145, cy - 70), (cx - 120, cy + 10), (cx - 50, cy + 15)]
    d.polygon(wing_l, fill=w_col, outline=bg_out)
    d.line([(cx - 20, cy - 20), (cx - 95, cy - 105)], fill=sk_mid, width=6)
    d.line([(cx - 95, cy - 105), (cx - 145, cy - 70)], fill=sk_mid, width=4)
    d.line([(cx - 20, cy - 20), (cx - 120, cy + 10)], fill=sk_dark, width=3)

    # Cánh Phải
    wing_r = [(cx + 20, cy - 20), (cx + 95, cy - 105), (cx + 145, cy - 70), (cx + 120, cy + 10), (cx + 50, cy + 15)]
    d.polygon(wing_r, fill=w_col, outline=bg_out)
    d.line([(cx + 20, cy - 20), (cx + 95, cy - 105)], fill=sk_mid, width=6)
    d.line([(cx + 95, cy - 105), (cx + 145, cy - 70)], fill=sk_mid, width=4)
    d.line([(cx + 20, cy - 20), (cx + 120, cy + 10)], fill=sk_dark, width=3)

    # 2. Đuôi rồng uốn lượn có chùy gai
    tail_pts = [(cx + 25, cy + 30), (cx + 70, cy + 45), (cx + 105, cy + 30), (cx + 125, cy + 45)]
    for idx in range(len(tail_pts) - 1):
        d.line([tail_pts[idx], tail_pts[idx + 1]], fill=sk_mid, width=12)
        d.line([tail_pts[idx], tail_pts[idx + 1]], fill=palette["body_light"], width=4)
    # Chóp đuôi gai tam giác
    d.polygon([(cx + 120, cy + 30), (cx + 148, cy + 45), (cx + 120, cy + 60)], fill=palette["horn_col"], outline=bg_out)

    # 3. Thân rồng Chibi tròn trịa
    d.rounded_rectangle([cx - 48, cy - 28, cx + 48, cy + 54], radius=26, fill=sk_mid, outline=bg_out, width=4)
    # Ức bụng vàng mềm
    d.rounded_rectangle([cx - 28, cy - 6, cx + 22, cy + 46], radius=16, fill=palette["chest_col"])
    # Ngấn bụng rồng
    for ly in [cy + 8, cy + 22, cy + 36]:
        d.line([(cx - 20, ly), (cx + 14, ly)], fill=palette["body_dark"], width=2)

    # Hai chân rồng Chibi bụ bẫm
    d.ellipse([cx - 48, cy + 42, cx - 18, cy + 64], fill=sk_mid, outline=bg_out, width=3)
    d.ellipse([cx + 14, cy + 42, cx + 44, cy + 64], fill=sk_mid, outline=bg_out, width=3)
    # Móng vuốt
    for claw_x in [cx - 44, cx - 33, cx - 22]:
        d.polygon([(claw_x, cy + 58), (claw_x + 4, cy + 68), (claw_x + 8, cy + 58)], fill=palette["horn_col"])
    for claw_x in [cx + 18, cx + 29, cx + 40]:
        d.polygon([(claw_x, cy + 58), (claw_x + 4, cy + 68), (claw_x + 8, cy + 58)], fill=palette["horn_col"])

    # 4. Đầu Rồng Chibi bướng bỉnh siêu ngầu
    hx, hy = cx - 18, cy - 35
    hr = 40
    d.ellipse([hx - hr - 3, hy - hr - 3, hx + hr + 3, hy + hr + 3], fill=bg_out)
    d.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=sk_mid)
    d.ellipse([hx - hr + 10, hy - hr + 6, hx + hr - 12, hy - 4], fill=palette["body_light"])

    # Mõm rồng góc cạnh
    d.rounded_rectangle([hx - 48, hy - 12, hx - 12, hy + 24], radius=12, fill=sk_mid, outline=bg_out, width=3)
    d.ellipse([hx - 42, hy - 2, hx - 36, hy + 4], fill=bg_out) # Lỗ mũi

    # Sừng Quỷ Nhọn hoắt
    horn = palette["horn_col"]
    d.polygon([(hx - 15, hy - 25), (hx - 32, hy - 68), (hx - 18, hy - 32)], fill=horn, outline=bg_out)
    d.polygon([(hx + 12, hy - 25), (hx + 28, hy - 68), (hx + 24, hy - 32)], fill=horn, outline=bg_out)

    # 5. MẮT RỒNG ANIME RỰC SÁNG
    ex, ey = hx - 16, hy - 8
    d.ellipse([ex - 14, ey - 16, ex + 14, ey + 16], fill=(255, 255, 255, 255), outline=bg_out, width=3)
    d.ellipse([ex - 11, ey - 13, ex + 11, ey + 13], fill=palette["eye_col"])
    d.ellipse([ex - 7, ey - 9, ex + 7, ey + 10], fill=(15, 15, 25, 255))
    d.ellipse([ex - 5, ey - 7, ex + 2, ey], fill=(255, 255, 255, 255))
    d.ellipse([ex + 2, ey + 3, ex + 6, ey + 8], fill=(255, 255, 255, 255))

    # Hơi thở nguyên tố phả nhẹ ra mõm
    if "breath_fx" in palette:
        fx_col = palette["breath_fx"]
        for p_idx in range(4):
            d.ellipse([hx - 60 - p_idx * 8, hy + 2 + p_idx * 4, hx - 50 - p_idx * 8, hy + 12 + p_idx * 4], fill=fx_col)

    out_path = os.path.join(OUTPUT_DIR, filename)
    im.save(out_path, "PNG")
    print(f"✅ Hoàn thành Pixel Art: {out_path}")

# =============================================================================
# THIẾT LẬP BẢNG MÀU CHUYÊN NGHIỆP CHO 5 LOÀI RỒNG
# =============================================================================

# 1. Thanh Long
palette_thanh_long = {
    "bg_out": (6, 40, 32, 255),
    "body_dark": (0, 143, 93, 255),
    "body_mid": (0, 214, 143, 255),
    "body_light": (102, 255, 204, 255),
    "mane_col": (0, 180, 216, 255),
    "horn_col": (255, 224, 102, 255),
    "eye_col": (255, 215, 0, 255),
    "orb_col": (255, 255, 200, 255),
}

# 2. Hoàng Long
palette_hoang_long = {
    "bg_out": (55, 40, 0, 255),
    "body_dark": (204, 153, 0, 255),
    "body_mid": (255, 204, 0, 255),
    "body_light": (255, 255, 128, 255),
    "mane_col": (230, 46, 0, 255),
    "horn_col": (255, 240, 190, 255),
    "eye_col": (0, 230, 168, 255),
    "orb_col": (255, 235, 150, 255),
}

# 3. Hắc Long
palette_hac_long = {
    "bg_out": (26, 5, 38, 255),
    "body_dark": (77, 25, 115, 255),
    "body_mid": (138, 43, 226, 255),
    "body_light": (195, 128, 255, 255),
    "mane_col": (65, 0, 120, 255),
    "horn_col": (220, 200, 255, 255),
    "eye_col": (255, 26, 83, 255),
    "orb_col": (210, 160, 255, 255),
}

# 4. Hỏa Long
palette_hoa_long = {
    "bg_out": (51, 10, 5, 255),
    "body_dark": (180, 30, 20, 255),
    "body_mid": (255, 59, 48, 255),
    "body_light": (255, 128, 120, 255),
    "wing_col": (255, 133, 51, 235),
    "chest_col": (255, 230, 179, 255),
    "horn_col": (46, 46, 56, 255),
    "eye_col": (255, 220, 0, 255),
    "breath_fx": (255, 100, 20, 200),
}

# 5. Băng Long
palette_bang_long = {
    "bg_out": (10, 34, 51, 255),
    "body_dark": (50, 150, 210, 255),
    "body_mid": (90, 200, 250, 255),
    "body_light": (200, 240, 255, 255),
    "wing_col": (179, 230, 255, 220),
    "chest_col": (240, 250, 255, 255),
    "horn_col": (230, 247, 255, 255),
    "eye_col": (255, 255, 255, 255),
    "breath_fx": (180, 235, 255, 200),
}

# Kết xuất 5 bức tranh Chibi Pixel Art
draw_chibi_oriental_dragon("thanh_long.png", "Thanh Long", palette_thanh_long)
draw_chibi_oriental_dragon("hoang_long.png", "Hoàng Long", palette_hoang_long)
draw_chibi_oriental_dragon("hac_long.png", "Hắc Long", palette_hac_long)
draw_chibi_western_dragon("hoa_long.png", "Hỏa Long", palette_hoa_long)
draw_chibi_western_dragon("bang_long.png", "Băng Long", palette_bang_long)

print("🎉 Hoàn tất 100% bộ ảnh Pixel Art Chibi siêu đẹp!")
