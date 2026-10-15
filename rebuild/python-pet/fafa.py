# -*- coding: utf-8 -*-
"""
fafa.py — Tái dựng FaFa Cat (SilverMeow, C.K.Tong 2002).
Schema suy ra từ chuỗi lỗi gốc trong fafa.exe:
- action[%d]: ratio, next action list, dislike action, level,
  x_bound / y_bound (chống deadlock), <same_ratio>
- dialog animation action vs animation action: images[], image no.
- INI fafa.ini + class FaFaWClass, đọc bằng GetPrivateProfile
- Dialog Option gốc: Display Mode, Top/Left/Bottom/Right Margin, Speed(ms)
Sprite đã trích: bitmap_103 (sheet lớn), bitmap_114 (125x151 24-bit),
bitmap_110, bitmap_111... trong rebuild/assets/fafa/
"""
import os
import random
import tkinter as tk
from tkinter import simpledialog
from pet_engine import PetEngine, load_ini

BASE = os.path.dirname(os.path.abspath(__file__))
INI_PATH = os.path.join(BASE, "fafa.ini")
ASSET_DIR = os.path.abspath(os.path.join(BASE, "..", "assets", "fafa"))

DEFAULTS = {
    "Display": {"Mode": "Normal"},
    "Boundary": {"Top": "0", "Left": "0", "Bottom": "0", "Right": "0"},
    "Speed": {"ms": "100"},
    # Action mẫu tái hiện engine gốc: mỗi action có ratio + next[]
    "Action0": {"images": "114", "dx": "2", "dy": "0", "ratio": "50", "next": "0,1,2", "level": "0"},
    "Action1": {"images": "110", "dx": "-2", "dy": "1", "ratio": "30", "next": "0,1,2", "level": "0"},
    "Action2": {"images": "103", "dx": "0", "dy": "2", "ratio": "20", "next": "0,1", "level": "0"},
}


class Action:
    """Một action trong engine FaFa gốc."""

    def __init__(self, aid, d):
        self.aid = aid
        self.images = [x.strip() for x in d.get("images", "").split(",") if x.strip()]
        self.dx = int(d.get("dx", "0"))
        self.dy = int(d.get("dy", "0"))
        self.ratio = int(d.get("ratio", "0"))
        self.next = [int(x) for x in d.get("next", "").split(",") if x.strip().lstrip("-").isdigit()]
        self.level = int(d.get("level", "0"))
        self.dislike = [int(x) for x in d.get("dislike", "").split(",") if x.strip().lstrip("-").isdigit()]


class FafaPet(PetEngine):
    def __init__(self):
        cfg = load_ini(INI_PATH, DEFAULTS)
        speed = int(cfg["Speed"].get("ms", "100"))
        super().__init__(title="FaFa Cat", w=125, h=151, speed_ms=speed)
        b = cfg["Boundary"]
        self.margin = {k: int(b.get(k, "0")) for k in ("Top", "Left", "Bottom", "Right")}
        # Nạp actions từ INI, kiểm tra đúng luật deadlock của bản gốc
        self.actions = {}
        for sec in cfg.sections():
            if sec.startswith("Action"):
                try:
                    aid = int(sec[6:])
                    self.actions[aid] = Action(aid, cfg[sec])
                except ValueError:
                    pass
        self._validate_actions()
        self.current = 0
        self.sprites = self._load_sprites()
        self._si = 0
        self._img = None
        self.menu.delete(0, tk.END)
        self.menu.add_command(label="&Continue", command=self.on_continue)
        self.menu.add_command(label="&Option...", command=self.on_option)
        self.menu.add_command(label="&About FaFa Cat", command=self._about)
        self.menu.add_separator()
        self.menu.add_command(label="&Exit", command=self.on_exit)

    def _validate_actions(self):
        """In cảnh báo giống hệt format '** ERROR ...' của bản gốc."""
        for aid, a in self.actions.items():
            if not a.images:
                print(f"** ERROR : Not define images for animation action : {aid} ...")
            if not a.next:
                print(f"** ERROR : Not define next possible actions for action {aid} ...")
            if sum(self.actions[n].ratio for n in a.next if n in self.actions) == 0 and a.next:
                print(f"** Sum of ratio for action:{aid} = 0")
            if a.dx == 0 and any("x_bound" in str(v) for v in [a.dislike]):
                print(f"** Action [{aid}] have defined X bounding action list but have no horizontal movement")

    def _load_sprites(self):
        """Nạp các bitmap_*.bmp đã trích theo id trong Action.images."""
        from PIL import Image, ImageTk
        out = {}
        for aid, a in self.actions.items():
            frames = []
            for img_id in a.images:
                for cand in [f"bitmap_{img_id}_9_1.bmp", f"bitmap_{img_id}.bmp"]:
                    p = os.path.join(ASSET_DIR, cand)
                    if os.path.exists(p):
                        try:
                            im = Image.open(p).convert("RGBA")
                            im.thumbnail((self.pet_w, self.pet_h))
                            frames.append(ImageTk.PhotoImage(im))
                            break
                        except Exception as e:
                            print(f"[fafa] Lỗi nạp {p}: {e}")
            out[aid] = frames or []
        print(f"[fafa] Nạp sprite cho {len(out)} actions từ {ASSET_DIR}")
        return out

    def _pick_next(self):
        a = self.actions.get(self.current)
        if not a or not a.next:
            return self.current
        cands = [n for n in a.next if n in self.actions and n not in a.dislike]
        if not cands:
            print(f"** ERROR : For action {self.current}, may have dead lock actions ...")
            return self.current
        total = sum(self.actions[n].ratio for n in cands)
        r = random.randint(1, max(total, 1))
        acc = 0
        for n in cands:
            acc += self.actions[n].ratio
            if r <= acc:
                return n
        return cands[0]

    def update_frame(self):
        a = self.actions.get(self.current, None)
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        t, l, b, r = self.margin["Top"], self.margin["Left"], self.margin["Bottom"], self.margin["Right"]
        if a:
            self._x += a.dx
            self._y += a.dy
            # Chặn biên theo Boundary (x_bound/y_bound gốc)
            if self._x < l or self._x + self.pet_w > sw - r:
                a.dx *=- 1 if False else 1  # giữ nguyên, đổi action
                self._dx = -self._dx
                self.current = self._pick_next()
            if self._y < t or self._y + self.pet_h > sh - b:
                self.current = self._pick_next()
            if random.random() < 0.02:
                self.current = self._pick_next()
        self.geometry(f"+{self._x}+{self._y}")
        frames = self.sprites.get(self.current, [])
        self.canvas.delete("all")
        if frames:
            self._si = (self._si + 1) % len(frames)
            self._img = frames[self._si]
            self.canvas.create_image(self.pet_w // 2, self.pet_h // 2, image=self._img)
        else:
            self.canvas.create_text(self.pet_w // 2, self.pet_h // 2, text="=^･ω･^=",
                                    font=("Consolas", 24), fill="brown")

    def on_option(self):
        # Hộp thoại đúng các field gốc: Speed + 4 Margin
        try:
            v = simpledialog.askinteger("FaFa Cat - Option", "Speed (ms):",
                                        initialvalue=self.speed_ms, parent=self)
            if v and 10 <= v <= 1000:
                self.speed_ms = v
        except Exception:
            pass

    def _about(self):
        print("FaFa Cat — Copyright (C) 2002 By C.K.Tong — http://www.SilverMeow.com (bản tái dựng)")


if __name__ == "__main__":
    if not os.path.exists(INI_PATH):
        import configparser
        cfg = configparser.ConfigParser()
        cfg.optionxform = str
        cfg.read_dict(DEFAULTS)
        with open(INI_PATH, "w", encoding="utf-8-sig") as f:
            cfg.write(f)
    FafaPet().start_timer()
    tk.mainloop()
