# -*- coding: utf-8 -*-
"""
generate_120fps_dragon_frames.py — Tạo 300 khung hình Pixel Art Chibi động cho 5 loài rồng (60 frame/loài).
Bao gồm:
1. Thư mục frame PNG trong suốt: assets/dragons/frames/<tên_rồng>/frame_000.png ... frame_059.png
2. File GIF xem trước chuyển động mượt mà: assets/dragons/gifs/<tên_rồng>_anim.gif
3. File Sprite Sheet tổng hợp 10x6 ô cho game engine.
"""
import os
import math
from PIL import Image, ImageDraw

BASE_DIR = r"D:\Pet\rebuild\rust-pet\assets\dragons"
FRAMES_DIR = os.path.join(BASE_DIR, "frames")
GIFS_DIR = os.path.join(BASE_DIR, "gifs")
SHEETS_DIR = os.path.join(BASE_DIR, "spritesheets")

os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(GIFS_DIR, exist_ok=True)
os.makedirs(SHEETS_DIR, exist_ok=True)

TOTAL_FRAMES = 60 # 60 frame cho 1 chu kỳ chuyển động mượt mà lặp lại

def render_oriental_dragon_frame(t, palette):
    """
    t: float từ 0.0 đến 1.0 (chu kỳ thời gian)
    """
    w, h = 320, 260
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    base_x, base_y = 100, 130
    phase = t * 2.0 * math.pi

    # 1. Thân rồng uốn lượn S-Curve với sóng sin động học theo thời gian
    body_points = []
    radii = []
    num_nodes = 9
    for i in range(num_nodes):
        frac = i / (num_nodes - 1)
        node_angle = phase - i * 0.55
        wave_y = math.sin(node_angle) * (34.0 * (1.0 - frac * 0.3))
        wave_x = math.cos(node_angle) * 8.0
        bx = base_x + int(frac * 155 + wave_x)
        by = base_y + int(wave_y) + int(frac * 12)
        body_points.append((bx, by))
        radii.append(int(26 * (1.0 - frac * 0.45)))

    # Vẽ từ đuôi lên đầu (Back to Front)
    for i in range(num_nodes - 1, 0, -1):
        cx, cy = body_points[i]
        r = radii[i]

        # Bờm lưng bồng bềnh uốn theo sóng
        fin_wave = math.sin(phase * 1.5 + i) * 6.0
        for off in [-4, 0, 4]:
            d.polygon([
                (cx + off, cy - r + 3),
                (cx + off + 3, cy - r - 16 + int(fin_wave)),
                (cx + off + 10, cy - r + 3)
            ], fill=palette["mane_col"], outline=palette["bg_out"])

        # Viền ngoài
        d.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], fill=palette["bg_out"])
        # Đốt thân (3 tầng màu)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=palette["body_dark"])
        d.ellipse([cx - r + 3, cy - r + 1, cx + r - 3, cy + r - 3], fill=palette["body_mid"])
        d.ellipse([cx - r + 6, cy - r + 2, cx + r - 10, cy + r - 10], fill=palette["body_light"])

        # Vảy rồng lấp lánh
        if i % 2 == 0:
            d.arc([cx - r + 8, cy - 4, cx + r - 8, cy + 10], start=0, end=180, fill=palette["mane_col"], width=2)

    # Đuôi rồng xòe lửa uốn lượn
    tx, ty = body_points[-1]
    tail_swing = math.sin(phase - (num_nodes - 1) * 0.55) * 12.0
    tail_pts = [
        (tx - 5, ty - 5), (tx + 25, ty - 22 + int(tail_swing)),
        (tx + 45, ty - 10 + int(tail_swing * 1.2)),
        (tx + 60, ty + int(tail_swing * 1.5)),
        (tx + 40, ty + 18 + int(tail_swing * 1.2)),
        (tx + 20, ty + 12 + int(tail_swing))
    ]
    d.polygon(tail_pts, fill=palette["mane_col"], outline=palette["bg_out"])
    d.polygon([(tx + 5, ty - 2), (tx + 35, ty - 8 + int(tail_swing)), (tx + 25, ty + 6)], fill=palette["body_light"])

    # 2. Đầu Rồng Chibi Anime nhấp nhô nhẹ theo nhịp thở
    head_bob = int(math.sin(phase) * 5.0)
    hx, hy = base_x - 10, base_y - 15 + head_bob
    hr = 46

    # Viền và khối đầu
    d.ellipse([hx - hr - 4, hy - hr - 4, hx + hr + 4, hy + hr + 4], fill=palette["bg_out"])
    d.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=palette["body_mid"])
    d.ellipse([hx - hr + 12, hy - hr + 6, hx + hr - 14, hy - 4], fill=palette["body_light"])

    # Mõm rồng bầu bĩnh
    d.rounded_rectangle([hx - 58, hy - 8, hx - 12, hy + 32], radius=14, fill=palette["body_mid"], outline=palette["bg_out"], width=3)
    d.ellipse([hx - 48, hy + 2, hx - 30, hy + 18], fill=palette["body_light"])
    d.ellipse([hx - 52, hy + 8, hx - 48, hy + 14], fill=palette["bg_out"])

    # Sừng hươu thần thoại
    horn = palette["horn_col"]
    d.polygon([(hx + 5, hy - 25), (hx + 28, hy - 65), (hx + 38, hy - 60), (hx + 15, hy - 20)], fill=horn, outline=palette["bg_out"])
    d.polygon([(hx + 22, hy - 48), (hx + 42, hy - 58), (hx + 44, hy - 52), (hx + 24, hy - 42)], fill=horn, outline=palette["bg_out"])

    # Bờm rồng
    for bx, by, r_circ in [(hx + 20, hy - 15, 18), (hx + 28, hy + 5, 20), (hx + 18, hy + 25, 16)]:
        d.ellipse([bx - r_circ, by - r_circ, bx + r_circ, by + r_circ], fill=palette["mane_col"], outline=palette["bg_out"], width=2)

    # Râu rồng bay lượn trong gió (Sóng sin kép)
    whisker_w1 = math.sin(phase * 2.0) * 8.0
    whisker_w2 = math.cos(phase * 2.0) * 12.0
    d.line([(hx - 45, hy + 16), (hx - 75, hy + 38 + int(whisker_w1)), (hx - 105, hy + 32 + int(whisker_w2))], fill=horn, width=4)
    d.line([(hx - 75, hy + 38 + int(whisker_w1)), (hx - 95, hy + 50 + int(whisker_w2 * 1.2))], fill=horn, width=3)

    # 3. Mắt Anime Chibi (Chớp mắt tự nhiên ở t = 0.70..0.80)
    ex, ey = hx - 18, hy - 6
    is_blink = 0.72 <= t <= 0.80
    if is_blink:
        # Nhắm mắt chữ ^ cute
        d.arc([ex - 12, ey - 6, ex + 12, ey + 10], start=180, end=360, fill=palette["bg_out"], width=4)
    else:
        d.ellipse([ex - 15, ey - 18, ex + 15, ey + 18], fill=(255, 255, 255, 255), outline=palette["bg_out"], width=3)
        d.ellipse([ex - 12, ey - 15, ex + 12, ey + 15], fill=palette["eye_col"])
        d.ellipse([ex - 9, ey - 10, ex + 9, ey + 12], fill=(15, 15, 25, 255))
        d.ellipse([ex - 6, ey - 8, ex + 2, ey], fill=(255, 255, 255, 255))
        d.ellipse([ex + 2, ey + 4, ex + 7, ey + 9], fill=(255, 255, 255, 255))

    # Má hồng
    d.ellipse([hx - 36, hy + 16, hx - 20, hy + 26], fill=(255, 130, 150, 160))

    # 4. Dạ Minh Châu xoay tròn 360 độ phát quang
    orb_rot = phase
    ox = hx - 70 + int(math.cos(orb_rot) * 10.0)
    oy = hy + 50 + int(math.sin(orb_rot) * 10.0)
    for gr in range(20, 10, -3):
        d.ellipse([ox - gr, oy - gr, ox + gr, oy + gr], fill=(255, 245, 180, 40))
    d.ellipse([ox - 12, oy - 12, ox + 12, oy + 12], fill=palette["orb_col"], outline=palette["bg_out"], width=2)
    d.ellipse([ox - 7, oy - 7, ox - 1, oy - 1], fill=(255, 255, 255, 240))

    return im

def render_western_dragon_frame(t, palette):
    """
    Rồng Phương Tây Chibi: Đập cánh 120 FPS, đuôi gai lắc lư, phập phồng nhịp thở.
    """
    w, h = 320, 260
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    phase = t * 2.0 * math.pi
    body_bob = int(math.sin(phase) * 6.0)
    cx, cy = 160, 145 + body_bob

    w_col = palette["wing_col"]
    sk_dark = palette["body_dark"]
    sk_mid = palette["body_mid"]
    bg_out = palette["bg_out"]

    # 1. Đôi Cánh Dơi Vỗ Nhịp (Wing Flapping)
    wing_flap = math.sin(phase) * 32.0
    wing_tip_y = cy - 85.0 + int(wing_flap)

    # Cánh Trái
    wing_l = [(cx - 20, cy - 20), (cx - 95, wing_tip_y - 20), (cx - 150, wing_tip_y + 15), (cx - 120, cy + 10), (cx - 50, cy + 15)]
    d.polygon(wing_l, fill=w_col, outline=bg_out)
    d.line([(cx - 20, cy - 20), (cx - 95, wing_tip_y - 20)], fill=sk_mid, width=6)
    d.line([(cx - 95, wing_tip_y - 20), (cx - 150, wing_tip_y + 15)], fill=sk_mid, width=4)
    d.line([(cx - 20, cy - 20), (cx - 120, cy + 10)], fill=sk_dark, width=3)

    # Cánh Phải
    wing_r = [(cx + 20, cy - 20), (cx + 95, wing_tip_y - 20), (cx + 150, wing_tip_y + 15), (cx + 120, cy + 10), (cx + 50, cy + 15)]
    d.polygon(wing_r, fill=w_col, outline=bg_out)
    d.line([(cx + 20, cy - 20), (cx + 95, wing_tip_y - 20)], fill=sk_mid, width=6)
    d.line([(cx + 95, wing_tip_y - 20), (cx + 150, wing_tip_y + 15)], fill=sk_mid, width=4)
    d.line([(cx + 20, cy - 20), (cx + 120, cy + 10)], fill=sk_dark, width=3)

    # 2. Đuôi gai quẫy đuôi nhịp nhàng
    tail_swing = math.sin(phase - 0.6) * 16.0
    tail_pts = [(cx + 25, cy + 30), (cx + 70, cy + 45 + int(tail_swing * 0.5)), (cx + 105, cy + 30 + int(tail_swing)), (cx + 130, cy + 45 + int(tail_swing * 1.4))]
    for idx in range(len(tail_pts) - 1):
        d.line([tail_pts[idx], tail_pts[idx + 1]], fill=sk_mid, width=12)
        d.line([tail_pts[idx], tail_pts[idx + 1]], fill=palette["body_light"], width=4)
    # Chóp đuôi gai tam giác
    d.polygon([
        (cx + 125, cy + 30 + int(tail_swing * 1.4)),
        (cx + 152, cy + 45 + int(tail_swing * 1.4)),
        (cx + 125, cy + 60 + int(tail_swing * 1.4))
    ], fill=palette["horn_col"], outline=bg_out)

    # 3. Thân rồng Chibi tròn trịa
    d.rounded_rectangle([cx - 48, cy - 28, cx + 48, cy + 54], radius=26, fill=sk_mid, outline=bg_out, width=4)
    d.rounded_rectangle([cx - 28, cy - 6, cx + 22, cy + 46], radius=16, fill=palette["chest_col"])
    for ly in [cy + 8, cy + 22, cy + 36]:
        d.line([(cx - 20, ly), (cx + 14, ly)], fill=palette["body_dark"], width=2)

    # Hai chân Chibi bụ bẫm
    d.ellipse([cx - 48, cy + 42, cx - 18, cy + 64], fill=sk_mid, outline=bg_out, width=3)
    d.ellipse([cx + 14, cy + 42, cx + 44, cy + 64], fill=sk_mid, outline=bg_out, width=3)
    for claw_x in [cx - 44, cx - 33, cx - 22]:
        d.polygon([(claw_x, cy + 58), (claw_x + 4, cy + 68), (claw_x + 8, cy + 58)], fill=palette["horn_col"])
    for claw_x in [cx + 18, cx + 29, cx + 40]:
        d.polygon([(claw_x, cy + 58), (claw_x + 4, cy + 68), (claw_x + 8, cy + 58)], fill=palette["horn_col"])

    # 4. Đầu Rồng Chibi bướng bỉnh
    hx, hy = cx - 18, cy - 35
    hr = 40
    d.ellipse([hx - hr - 3, hy - hr - 3, hx + hr + 3, hy + hr + 3], fill=bg_out)
    d.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=sk_mid)
    d.ellipse([hx - hr + 10, hy - hr + 6, hx + hr - 12, hy - 4], fill=palette["body_light"])

    # Mõm
    d.rounded_rectangle([hx - 48, hy - 12, hx - 12, hy + 24], radius=12, fill=sk_mid, outline=bg_out, width=3)
    d.ellipse([hx - 42, hy - 2, hx - 36, hy + 4], fill=bg_out)

    # Sừng quỷ
    horn = palette["horn_col"]
    d.polygon([(hx - 15, hy - 25), (hx - 32, hy - 68), (hx - 18, hy - 32)], fill=horn, outline=bg_out)
    d.polygon([(hx + 12, hy - 25), (hx + 28, hy - 68), (hx + 24, hy - 32)], fill=horn, outline=bg_out)

    # 5. Mắt Rồng Anime (Chớp mắt ở t = 0.65..0.75)
    ex, ey = hx - 16, hy - 8
    is_blink = 0.65 <= t <= 0.75
    if is_blink:
        d.arc([ex - 12, ey - 6, ex + 12, ey + 10], start=180, end=360, fill=bg_out, width=4)
    else:
        d.ellipse([ex - 14, ey - 16, ex + 14, ey + 16], fill=(255, 255, 255, 255), outline=bg_out, width=3)
        d.ellipse([ex - 11, ey - 13, ex + 11, ey + 13], fill=palette["eye_col"])
        d.ellipse([ex - 7, ey - 9, ex + 7, ey + 10], fill=(15, 15, 25, 255))
        d.ellipse([ex - 5, ey - 7, ex + 2, ey], fill=(255, 255, 255, 255))
        d.ellipse([ex + 2, ey + 3, ex + 6, ey + 8], fill=(255, 255, 255, 255))

    # Hơi thở nguyên tố phả nhịp nhàng
    if "breath_fx" in palette:
        fx_col = palette["breath_fx"]
        breath_wave = math.sin(phase * 2.0) * 8.0
        for p_idx in range(4):
            d.ellipse([
                hx - 60 - p_idx * 10 - int(breath_wave),
                hy + 2 + p_idx * 4,
                hx - 48 - p_idx * 10 - int(breath_wave),
                hy + 14 + p_idx * 4
            ], fill=fx_col)

    return im

# Bảng màu chuẩn
PALETTES = {
    "thanh_long": {
        "is_oriental": True,
        "name_vi": "Thanh Long",
        "bg_out": (6, 40, 32, 255),
        "body_dark": (0, 143, 93, 255),
        "body_mid": (0, 214, 143, 255),
        "body_light": (102, 255, 204, 255),
        "mane_col": (0, 180, 216, 255),
        "horn_col": (255, 224, 102, 255),
        "eye_col": (255, 215, 0, 255),
        "orb_col": (255, 255, 200, 255),
    },
    "hoang_long": {
        "is_oriental": True,
        "name_vi": "Hoàng Long",
        "bg_out": (55, 40, 0, 255),
        "body_dark": (204, 153, 0, 255),
        "body_mid": (255, 204, 0, 255),
        "body_light": (255, 255, 128, 255),
        "mane_col": (230, 46, 0, 255),
        "horn_col": (255, 240, 190, 255),
        "eye_col": (0, 230, 168, 255),
        "orb_col": (255, 235, 150, 255),
    },
    "hac_long": {
        "is_oriental": True,
        "name_vi": "Hắc Long",
        "bg_out": (26, 5, 38, 255),
        "body_dark": (77, 25, 115, 255),
        "body_mid": (138, 43, 226, 255),
        "body_light": (195, 128, 255, 255),
        "mane_col": (65, 0, 120, 255),
        "horn_col": (220, 200, 255, 255),
        "eye_col": (255, 26, 83, 255),
        "orb_col": (210, 160, 255, 255),
    },
    "hoa_long": {
        "is_oriental": False,
        "name_vi": "Hỏa Long",
        "bg_out": (51, 10, 5, 255),
        "body_dark": (180, 30, 20, 255),
        "body_mid": (255, 59, 48, 255),
        "body_light": (255, 128, 120, 255),
        "wing_col": (255, 133, 51, 235),
        "chest_col": (255, 230, 179, 255),
        "horn_col": (46, 46, 56, 255),
        "eye_col": (255, 220, 0, 255),
        "breath_fx": (255, 100, 20, 200),
    },
    "bang_long": {
        "is_oriental": False,
        "name_vi": "Băng Long",
        "bg_out": (10, 34, 51, 255),
        "body_dark": (50, 150, 210, 255),
        "body_mid": (90, 200, 250, 255),
        "body_light": (200, 240, 255, 255),
        "wing_col": (179, 230, 255, 220),
        "chest_col": (240, 250, 255, 255),
        "horn_col": (230, 247, 255, 255),
        "eye_col": (255, 255, 255, 255),
        "breath_fx": (180, 235, 255, 200),
    },
}

def generate_all():
    total_images_generated = 0
    print(f"🚀 Bắt đầu tạo {TOTAL_FRAMES * len(PALETTES)} khung hình động Pixel Art 120 FPS...")

    for key, pinfo in PALETTES.items():
        dragon_dir = os.path.join(FRAMES_DIR, key)
        os.makedirs(dragon_dir, exist_ok=True)
        is_oriental = pinfo["is_oriental"]
        frames_list = []

        print(f"👉 Đang kết xuất 60 frames cho: {pinfo['name_vi']} ({key})...")
        for i in range(TOTAL_FRAMES):
            t = i / float(TOTAL_FRAMES)
            if is_oriental:
                frame_img = render_oriental_dragon_frame(t, pinfo)
            else:
                frame_img = render_western_dragon_frame(t, pinfo)

            # Lưu từng frame PNG nền trong suốt
            frame_path = os.path.join(dragon_dir, f"frame_{i:03d}.png")
            frame_img.save(frame_path, "PNG")
            frames_list.append(frame_img)
            total_images_generated += 1

        # 1. Tạo Animated GIF xem trước (Chuẩn 60 FPS, duration=16ms mỗi frame)
        gif_path = os.path.join(GIFS_DIR, f"{key}_anim.gif")
        frames_list[0].save(
            gif_path,
            save_all=True,
            append_images=frames_list[1:],
            duration=16, # 16ms ~ 60 FPS trong player
            loop=0,
            disposal=2,
            transparency=0
        )
        print(f"  🎬 Đã tạo file GIF: {gif_path}")

        # 2. Tạo Sprite Sheet tổng hợp (Lưới 10 cột x 6 hàng = 60 frame)
        cols = 10
        rows = 6
        fw, fh = 320, 260
        sheet_w = cols * fw
        sheet_h = rows * fh
        sheet_img = Image.new("RGBA", (sheet_w, sheet_h), (0, 0, 0, 0))

        for idx, fimg in enumerate(frames_list):
            gx = (idx % cols) * fw
            gy = (idx // cols) * fh
            sheet_img.paste(fimg, (gx, gy))

        sheet_path = os.path.join(SHEETS_DIR, f"{key}_spritesheet_10x6.png")
        sheet_img.save(sheet_path, "PNG")
        print(f"  📜 Đã tạo Sprite Sheet: {sheet_path}")

    print(f"\n🎉 HOÀN TẤT THÀNH CÔNG: Đã sinh ra tổng cộng {total_images_generated} khung hình PNG + 5 Animated GIF + 5 Sprite Sheets!")

if __name__ == "__main__":
    generate_all()
