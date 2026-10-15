# -*- coding: utf-8 -*-
"""
pet_framework.py — Framework đa-pet thế hệ 2.
Khác v1 (mỗi pet = 1 process Tk): v2 dùng 1 Tk root ẩn + N Toplevel,
quản lý tập trung bởi PetManager. Thêm pet mới chỉ cần 1 file JSON
trong pets/ + hàm vẽ, không cần sửa engine.

Định dạng pets/<id>.json:
{
  "id": "robo-cat", "name": "Robo Cat", "kind": "code",
  "size": [128, 128], "speed_ms": 100,
  "behaviors": ["wander", "bounce", "sit_random"],
  "phrases": ["xin chào!"],
  "color": "#00e5ff"
}
"""
import glob
import json
import os
import random
import tkinter as tk

BASE = os.path.dirname(os.path.abspath(__file__))
PETS_DIR = os.path.join(BASE, "pets")
TRANSPARENT_KEY = "#ff00ff"

# -- Các hàm vẽ pet mẫu bằng canvas (không cần asset, tránh bản quyền) --
def _draw_robo_cat(cv, w, h, tick, color="#00e5ff"):
    cv.create_rectangle(30, 40, w - 30, h - 20, fill="#222", outline=color, width=3)
    cv.create_rectangle(40, 15, w - 40, 45, fill="#222", outline=color, width=3)
    cv.create_polygon(40, 18, 48, 2, 58, 16, fill=color)
    cv.create_polygon(w - 40, 18, w - 48, 2, w - 58, 16, fill=color)
    eye = 3 + (tick % 3)
    cv.create_oval(48, 25, 48 + eye * 3, 35, fill="red")
    cv.create_oval(w - 48 - eye * 3, 25, w - 48, 35, fill="red")
    cv.create_text(w // 2, h - 35, text="><(((*>", fill=color, font=("Consolas", 14, "bold"))


def _draw_pixel_bird(cv, w, h, tick, color="#ffd54a"):
    flap = (tick % 4) * 6
    cv.create_oval(30, 40, w - 30, h - 30, fill=color, outline="#a86200", width=2)
    cv.create_polygon(25, 55 - flap, 8, 45 - flap, 25, 40 - flap, fill="#ff9d00")
    cv.create_polygon(w - 45, 50, w - 25, 50 - flap, w - 30, 65, fill="#fff", outline="#999")
    cv.create_oval(w // 2 - 5, 55, w // 2 + 5, 65, fill="black")
    cv.create_oval(w // 2 - 2, 57, w // 2 + 2, 61, fill="white")
    cv.create_text(w // 2, h - 18, text="~ chirp ~" if tick % 50 < 6 else "", fill="#666")


def _draw_penguin(cv, w, h, tick, color="#222"):
    wob = (tick % 6) - 3
    cv.create_oval(35 + wob, 25, w - 35 + wob, h - 15, fill=color, outline="black")
    cv.create_oval(48 + wob, 40, w - 48 + wob, h - 25, fill="white")
    cv.create_polygon(w // 2 - 8 + wob, 50, w // 2 + 8 + wob, 50, w // 2 + wob, 60, fill="orange")
    cv.create_oval(w // 2 - 14 + wob, 42, w // 2 - 4 + wob, 50, fill="white")
    cv.create_oval(w // 2 + 4 + wob, 42, w // 2 + 14 + wob, 50, fill="white")
    cv.create_oval(w // 2 - 10 + wob, 44, w // 2 - 6 + wob, 48, fill="black")
    cv.create_oval(w // 2 + 6 + wob, 44, w // 2 + 10 + wob, 48, fill="black")


def _draw_ghost(cv, w, h, tick, color="white"):
    bob = int(6 * (1 if (tick // 8) % 2 == 0 else -1))
    cv.create_arc(30, 30 + bob, w - 30, h - 30 + bob, start=0, extent=180,
                  fill=color, outline="#bbb", width=2, style="pieslice")
    cv.create_rectangle(30, (30 + h - 30) // 2 + bob, w - 30, h - 30 + bob, fill=color, outline=color)
    for i, x in enumerate(range(30, w - 30, 16)):
        cv.create_oval(x, h - 42 + bob, x + 16, h - 26 + bob, fill=color, outline=color)
    cv.create_oval(w // 2 - 14, 60 + bob, w // 2 - 2, 74 + bob, fill="black")
    cv.create_oval(w // 2 + 2, 60 + bob, w // 2 + 14, 74 + bob, fill="black")


DRAWERS = {"robo-cat": _draw_robo_cat, "pixel-bird": _draw_pixel_bird,
           "mini-penguin": _draw_penguin, "ghost-boo": _draw_ghost}


class Pet:
    """Một con pet = 1 Toplevel trong suốt + state machine behaviors."""

    def __init__(self, manager, spec):
        self.m = manager
        self.spec = spec
        self.id = spec["id"]
        self.w, self.h = spec.get("size", [128, 128])
        self.speed = spec.get("speed_ms", 100)
        self.phrases = spec.get("phrases", [])
        self.color = spec.get("color", "#00e5ff")
        self.behaviors = spec.get("behaviors", ["wander"])
        self.win = tk.Toplevel(manager.root)
        self.win.overrideredirect(True)
        self.win.attributes("-topmost", True)
        try:
            self.win.attributes("-transparentcolor", TRANSPARENT_KEY)
        except tk.TclError:
            pass
        self.win.configure(bg=TRANSPARENT_KEY)
        self.cv = tk.Canvas(self.win, width=self.w, height=self.h,
                            bg=TRANSPARENT_KEY, highlightthickness=0)
        self.cv.pack()
        sw, sh = manager.sw, manager.sh
        self.x = random.randint(50, max(60, sw - self.w - 50))
        self.y = random.randint(50, max(60, sh - self.h - 100))
        self.dx = random.choice([-3, -2, 2, 3])
        self.dy = random.choice([-2, -1, 1, 2])
        self.tick = random.randint(0, 100)
        self.sitting = 0
        self._drag = None
        self._bubble = None
        self.win.geometry(f"{self.w}x{self.h}+{self.x}+{self.y}")
        self.cv.bind("<ButtonPress-1>", self._dstart)
        self.cv.bind("<B1-Motion>", self._dmove)
        self.cv.bind("<ButtonRelease-1>", self._dend)
        self.cv.bind("<Button-3>", self._rclick)
        self.menu = tk.Menu(self.win, tearoff=0)
        self.menu.add_command(label=f"Chào {spec.get('name', self.id)}!", command=self.say_hello)
        self.menu.add_command(label="Ẩn con này", command=self.hide)
        self.menu.add_separator()
        self.menu.add_command(label="Thoát tất cả", command=manager.quit_all)

    # -- Tương tác chuột --
    def _dstart(self, ev):
        self._drag = (ev.x, ev.y)

    def _dmove(self, ev):
        if self._drag:
            self.x += ev.x - self._drag[0]
            self.y += ev.y - self._drag[1]
            self.win.geometry(f"+{self.x}+{self.y}")

    def _dend(self, ev):
        self._drag = None

    def _rclick(self, ev):
        try:
            self.menu.tk_popup(ev.x_root, ev.y_root)
        finally:
            self.menu.grab_release()

    def hide(self):
        self.win.withdraw()
        self.m.hidden.append(self)

    def show(self):
        self.win.deiconify()

    def say_hello(self):
        if self.phrases:
            self.speak(random.choice(self.phrases))

    def speak(self, text, ms=3500):
        if self._bubble:
            try:
                self._bubble.destroy()
            except Exception:
                pass
        self._bubble = tk.Toplevel(self.win)
        self._bubble.overrideredirect(True)
        self._bubble.attributes("-topmost", True)
        tk.Label(self._bubble, text=text, bg="lightyellow",
                 relief="solid", wraplength=200).pack()
        self._bubble.geometry(f"+{self.x}+{self.y - 70}")
        self.win.after(ms, lambda: self._bubble.destroy() if self._bubble else None)

    # -- State machine mỗi tick --
    def step(self):
        self.tick += 1
        if "sit_random" in self.behaviors and self.sitting > 0:
            self.sitting -= 1
        else:
            if "sit_random" in self.behaviors and random.random() < 0.004:
                self.sitting = random.randint(30, 120)
            else:
                if "wander" in self.behaviors:
                    self.x += self.dx
                    # Chim/ma bay sine, mèo/robot đi thẳng
                    self.y += self.dy + (random.randint(-2, 2) if self.id in ("pixel-bird", "ghost-boo") else 0)
                if "bounce" in self.behaviors:
                    if self.x < 0 or self.x + self.w > self.m.sw:
                        self.dx *= -1
                    if self.y < 0 or self.y + self.h > self.m.sh - 60:
                        self.dy *= -1
        self.win.geometry(f"+{self.x}+{self.y}")
        self.cv.delete("all")
        fn = DRAWERS.get(self.id)
        if fn:
            fn(self.cv, self.w, self.h, self.tick, self.color)


class PetManager:
    """Quản lý N pet + va chạm + tray + settings."""

    def __init__(self, pet_ids=None):
        self.root = tk.Tk()
        self.root.withdraw()  # Root ẩn, chỉ dùng Toplevel
        self.sw, self.sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.pets = []
        self.hidden = []
        specs = load_specs(pet_ids)
        for sp in specs:
            try:
                self.pets.append(Pet(self, sp))
            except Exception as e:
                print(f"[manager] Bỏ qua {sp.get('id')}: {e}")
        print(f"[manager] Đang chạy {len(self.pets)} pet: {[p.id for p in self.pets]}")

    def loop(self):
        for p in self.pets:
            if p.win.winfo_viewable():
                try:
                    p.step()
                except Exception as e:
                    print(f"[manager] Lỗi {p.id}: {e}")
        self._collide()
        self.root.after(80, self.loop)

    def _collide(self):
        """Hai pet chạm nhau -> đổi hướng + chào (tính năng mới)."""
        vis = [p for p in self.pets if p.win.winfo_viewable()]
        for i in range(len(vis)):
            for j in range(i + 1, len(vis)):
                a, b = vis[i], vis[j]
                if abs(a.x - b.x) < 60 and abs(a.y - b.y) < 60 and random.random() < 0.05:
                    a.dx, b.dx = b.dx, a.dx
                    a.dy, b.dy = b.dy, a.dy
                    if random.random() < 0.5:
                        a.say_hello()

    def quit_all(self):
        try:
            self.root.destroy()
        except Exception:
            pass

    def run(self):
        self.loop()
        self.root.mainloop()


def load_specs(pet_ids=None):
    """Đọc pets/*.json. Không có folder thì dùng 4 mẫu mặc định."""
    out = []
    if os.path.isdir(PETS_DIR):
        for fp in sorted(glob.glob(os.path.join(PETS_DIR, "*.json"))):
            try:
                with open(fp, encoding="utf-8-sig") as f:
                    sp = json.load(f)
                if pet_ids is None or sp.get("id") in pet_ids:
                    out.append(sp)
            except Exception as e:
                print(f"[spec] Lỗi {fp}: {e}")
    if not out and pet_ids is None:
        out = default_specs()
    elif not out:
        out = [s for s in default_specs() if s["id"] in (pet_ids or [])]
    return out


def default_specs():
    return [
        {"id": "robo-cat", "name": "Robo Cat", "kind": "code", "size": [128, 128],
         "speed_ms": 100, "behaviors": ["wander", "bounce", "sit_random"],
         "phrases": ["bíp bíp! tao là mèo máy", "pin 99%, đi chơi tiếp!"], "color": "#00e5ff"},
        {"id": "pixel-bird", "name": "Pixel Bird", "kind": "code", "size": [128, 128],
         "speed_ms": 80, "behaviors": ["wander", "bounce"],
         "phrases": ["chíp chíp!", "gió trên này mát quá!"], "color": "#ffd54a"},
        {"id": "mini-penguin", "name": "Mini Penguin", "kind": "code", "size": [120, 130],
         "speed_ms": 110, "behaviors": ["wander", "bounce", "sit_random"],
         "phrases": ["lạch bạch... lạnh quá!", "cá đâu rồi nhỉ?"], "color": "#222222"},
        {"id": "ghost-boo", "name": "Ghost Boo", "kind": "code", "size": [120, 130],
         "speed_ms": 90, "behaviors": ["wander", "bounce"],
         "phrases": ["boo! sợ chưa?", "tao bay chứ không đi bộ nhé"], "color": "white"},
    ]
