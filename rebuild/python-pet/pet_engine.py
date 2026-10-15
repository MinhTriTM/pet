# -*- coding: utf-8 -*-
"""
pet_engine.py — Khung chung cho pet desktop (tái dựng từ bird/fafa/felix gốc).
Hành vi suy ra từ phân tích ngược:
- Cửa sổ trong suốt, luôn nổi (topmost), không viền
- Timer SetTimer/KillTimer -> Tk.after()
- Vẽ sprite bằng BitBlt/StretchBlt -> Tk.Canvas + PhotoImage
- Chuột phải -> TrackPopupMenu -> Tk.Menu
- Kéo-thả -> CreateWindowEx/SetWindowPos
- Cấu hình .ini qua GetPrivateProfile... -> configparser
"""
import configparser
import os
import random
import tkinter as tk

TRANSPARENT_KEY = "#ff00ff"  # Màu trong suốt (thay cho TransparentBlt gốc)


class PetEngine(tk.Tk):
    """Cửa sổ pet cơ bản: trong suốt, kéo được, menu phải, timer."""

    def __init__(self, title="Pet", w=128, h=128, speed_ms=100):
        super().__init__()
        self.title(title)
        self.pet_w, self.pet_h = w, h
        self.speed_ms = speed_ms
        # Không viền, luôn nổi — tương đương WS_EX_LAYERED|TOPMOST gốc
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        try:
            self.attributes("-transparentcolor", TRANSPARENT_KEY)
        except tk.TclError:
            pass  # Linux/WM không hỗ trợ thì bỏ qua
        self.configure(bg=TRANSPARENT_KEY)
        self.canvas = tk.Canvas(self, width=w, height=h, bg=TRANSPARENT_KEY,
                                highlightthickness=0)
        self.canvas.pack()
        self._drag = None
        self._timer_id = None
        self.running = True
        # Kéo-thả như bản gốc (drag & drop quanh desktop)
        self.canvas.bind("<ButtonPress-1>", self._on_drag_start)
        self.canvas.bind("<B1-Motion>", self._on_drag_move)
        self.canvas.bind("<ButtonRelease-1>", self._on_drag_end)
        self.canvas.bind("<Button-3>", self._on_right_click)
        # Đặt giữa màn hình lúc khởi động
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self._x, self._y = sw // 2, sh // 2
        self._dx, self._dy = 2, 1
        self.geometry(f"{w}x{h}+{self._x}+{self._y}")
        self.menu = tk.Menu(self, tearoff=0)
        self._build_menu(self.menu)
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    # -- Menu: bản gốc dùng LoadMenuA/TrackPopupMenu, ở đây dùng Tk.Menu --
    def _build_menu(self, menu):
        menu.add_command(label="&Continue", command=self.on_continue)
        menu.add_command(label="&Option...", command=self.on_option)
        menu.add_separator()
        menu.add_command(label="E&xit", command=self.on_exit)

    def _on_right_click(self, ev):
        try:
            self.menu.tk_popup(ev.x_root, ev.y_root)
        finally:
            self.menu.grab_release()

    # -- Kéo thả --
    def _on_drag_start(self, ev):
        self._drag = (ev.x, ev.y)
        self.on_grab()

    def _on_drag_move(self, ev):
        if self._drag:
            dx = ev.x - self._drag[0]
            dy = ev.y - self._drag[1]
            self._x += dx
            self._y += dy
            self.geometry(f"+{self._x}+{self._y}")

    def _on_drag_end(self, ev):
        self._drag = None
        self.on_drop()

    # -- Vòng lặp timer (SetTimer gốc) --
    def start_timer(self):
        self._tick()

    def _tick(self):
        if not self.running:
            return
        try:
            self.update_frame()
        except Exception as e:  # Không để crash như bản gốc (Runtime Error!)
            print(f"[PetEngine] Lỗi frame: {e}")
        self._timer_id = self.after(self.speed_ms, self._tick)

    def stop_timer(self):
        self.running = False
        if self._timer_id:
            self.after_cancel(self._timer_id)

    # -- Các hook cho lớp con ghi đè --
    def update_frame(self):
        """Một bước animation + di chuyển. Lớp con override."""
        self._x += self._dx
        self._y += self._dy
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        if self._x < 0 or self._x + self.pet_w > sw:
            self._dx *= -1
        if self._y < 0 or self._y + self.pet_h > sh:
            self._dy *= -1
        self.geometry(f"+{self._x}+{self._y}")

    def on_continue(self):
        self.running = True
        self.start_timer()

    def on_option(self):
        pass

    def on_grab(self):
        pass

    def on_drop(self):
        pass

    def on_exit(self):
        self.stop_timer()
        self.destroy()


def load_ini(path, defaults=None):
    """Đọc .ini kiểu GetPrivateProfileIntA/WritePrivateProfileStringA."""
    cfg = configparser.ConfigParser()
    cfg.optionxform = str  # Giữ nguyên hoa/thường như Win32
    if defaults:
        cfg.read_dict(defaults)
    if os.path.exists(path):
        cfg.read(path, encoding="utf-8-sig")
    return cfg
