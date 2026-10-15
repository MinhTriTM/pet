# -*- coding: utf-8 -*-
"""
bird.py — Tái dựng DeskTopBird_Kingfisher (SEGA 1997).
Nguồn suy ra từ strings/resources gốc:
- INI: DeskTopBird_K.ini, section [SEGA DeskTopBird_Kingfisher], key SOUND=%d
- Menu IDR_MENU: DEBUG Option, Window, STOP, DTB[Kingfisher], HELP
- Wave IDR_WAVE (49KB tiếng chim) -> assets/bird_on_desktop
- Hành vi: bay vòng quanh, đậu lên mép cửa sổ/taskbar, kéo-thả,
  thả gần taskbar thì rơi dần rồi nằm im (giả chết), double-click tray Close.
Dùng sprite BMP đã trích (bitmap_ALL_17_1.bmp 477x477, 8bpp).
"""
import os
import random
import tkinter as tk
from pet_engine import PetEngine, load_ini, TRANSPARENT_KEY

BASE = os.path.dirname(os.path.abspath(__file__))
INI_PATH = os.path.join(BASE, "DeskTopBird_K.ini")
ASSET_BMP = os.path.abspath(os.path.join(BASE, "..", "assets", "bird_on_desktop", "bitmap_ALL_17_1.bmp"))
ASSET_WAV = os.path.abspath(os.path.join(BASE, "..", "assets", "bird_on_desktop", "None_IDR_WAVE_17_1.bin.wav"))

DEFAULTS = {
    "SEGA DeskTopBird_Kingfisher": {"SOUND": "1", "AlwaysOnTop": "1"},
}

STATE_FLY = "fly"
STATE_SIT = "sit"
STATE_DEAD = "dead"


class BirdPet(PetEngine):
    def __init__(self):
        cfg = load_ini(INI_PATH, DEFAULTS)
        sec = cfg["SEGA DeskTopBird_Kingfisher"]
        self.want_sound = sec.get("SOUND", "1") == "1"
        super().__init__(title="DTB[Kingfisher]", w=96, h=96, speed_ms=80)
        self.state = STATE_FLY
        self.sit_ticks = 0
        self.frames = self._load_frames()
        self._fi = 0
        self._img = None
        # Menu đúng chữ gốc
        self.menu.delete(0, tk.END)
        self.menu.add_command(label="Window", command=self._show_window_opt)
        self.menu.add_command(label="STOP", command=self._toggle_stop)
        self.menu.add_command(label="DTB[Kingfisher]", command=self._about)
        self.menu.add_command(label="HELP", command=self._help)
        self.menu.add_separator()
        self.menu.add_command(label="Close", command=self.on_exit)
        self._stopped = False

    def _load_frames(self):
        """Cắt sprite-sheet 477x477 thành frame vuông. Nếu thiếu file thì vẽ chim ASCII."""
        frames = []
        try:
            from PIL import Image, ImageTk
            im = Image.open(ASSET_BMP).convert("RGBA")
            # Đoán sheet 4x4 frame (bản gốc nhiều bitmap chim vỗ cánh)
            n = 4
            fw, fh = im.width // n, im.height // n
            for r in range(n):
                for c in range(n):
                    f = im.crop((c * fw, r * fh, (c + 1) * fw, (r + 1) * fh))
                    f = f.resize((self.pet_w, self.pet_h))
                    frames.append(ImageTk.PhotoImage(f))
            print(f"[bird] Nạp {len(frames)} frame từ {ASSET_BMP}")
        except Exception as e:
            print(f"[bird] Không nạp được BMP ({e}), dùng hình vẽ thay thế")
        return frames

    def _play_sound(self):
        if not self.want_sound or not os.path.exists(ASSET_WAV):
            return
        try:
            import winsound
            winsound.PlaySound(ASSET_WAV, winsound.SND_FILENAME | winsound.SND_ASYNC)
        except Exception:
            pass

    def update_frame(self):
        if self._stopped:
            return
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        taskbar_y = sh - 60  # Giả lập taskbar dưới cùng
        if self.state == STATE_FLY:
            # Bay lượn sine như chim thật
            self._x += self._dx * 3
            self._y += self._dy * 2 + random.randint(-2, 2)
            if self._x < 0 or self._x + self.pet_w > sw:
                self._dx *= -1
            if self._y < 0 or self._y + self.pet_h > taskbar_y:
                self._dy *= -1
            # Thỉnh thoảng đậu xuống mép trên (giả cửa sổ) hoặc taskbar
            if random.random() < 0.005:
                self.state = STATE_SIT
                self.sit_ticks = random.randint(30, 120)
                self._y = random.choice([0, taskbar_y - self.pet_h])
            if random.random() < 0.002:
                self._play_sound()  # Kêu như bản gốc
        elif self.state == STATE_SIT:
            self.sit_ticks -= 1
            if self.sit_ticks <= 0:
                self.state = STATE_FLY
                self._dy = -abs(self._dy)
        elif self.state == STATE_DEAD:
            return  # Nằm im dưới đáy
        self.geometry(f"+{self._x}+{self._y}")
        # Vẽ frame vỗ cánh
        if self.frames:
            self._fi = (self._fi + 1) % len(self.frames)
            self._img = self.frames[self._fi]
            self.canvas.delete("all")
            self.canvas.create_image(self.pet_w // 2, self.pet_h // 2, image=self._img)
        else:
            self.canvas.delete("all")
            self.canvas.create_text(self.pet_w // 2, self.pet_h // 2, text="><))'>",
                                    font=("Consolas", 20), fill="blue")

    def on_drop(self):
        # Thả gần taskbar -> rơi dần rồi giả chết (đúng поведение gốc!)
        sh = self.winfo_screenheight()
        if self._y + self.pet_h > sh - 80:
            self.state = STATE_DEAD
            self._y = sh - self.pet_h
            self.geometry(f"+{self._x}+{self._y}")

    def _show_window_opt(self):
        print("[bird] Window option (luôn nổi):", bool(self.attributes("-topmost")))

    def _toggle_stop(self):
        self._stopped = not self._stopped

    def _about(self):
        print("DeskTopBird_Kingfisher 1.0 — Copyright (C) SEGA 1997 (bản tái dựng)")

    def _help(self):
        print("Kéo chim đi chỗ khác. Thả gần taskbar sẽ giả chết. Chuột phải -> Close để thoát.")


if __name__ == "__main__":
    # Ghi INI mặc định nếu chưa có (giữ tương thích bản gốc)
    if not os.path.exists(INI_PATH):
        with open(INI_PATH, "w", encoding="utf-8-sig") as f:
            f.write("[SEGA DeskTopBird_Kingfisher]\nSOUND=1\n")
    BirdPet().start_timer()
    tk.mainloop()
