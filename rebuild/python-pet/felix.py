# -*- coding: utf-8 -*-
"""
felix.py — Tái dựng Felix the ScreenMate (AdTools Inc 1999).
Nguồn suy ra từ felix.exe:
- INI DeskToppers.ini, menu IDR_POPUP:
  Stand Still, Run on Startup, About, Legal Disclaimer, Exit
- Dialog About: 'The Felix ScreenMate is produced by AdTools, Inc.'
  'Sales contact:sales@adtoolsinc.com'
- Customize: 'Musician you like/respect', 'Musician who you don't like'
- Câu thoại mèo (speech): các chuỗi trong binary
- Registry Run: Software\\Microsoft\\Windows\\CurrentVersion\\Run
- Sprite FIG1 nén zlib -> fig_decoder.py
"""
import os
import random
import tkinter as tk
from pet_engine import PetEngine, load_ini

BASE = os.path.dirname(os.path.abspath(__file__))
INI_PATH = os.path.join(BASE, "DeskToppers.ini")

PHRASES = [
    "Click me with the right mouse button to see some cool stunts!",
    "are we gonna do a sound check or what?",
    "heh-heh, you know this place remind me of an old desktop in liverpool I useta 'ang around.",
    "see that bird over there - she fancies me rotten.",
    "i'd like to dedicate this song my mate %l who couldn't be here today.",
    "Screen Mates are dead cool and you can find them at www.codehammer.com",
]

DEFAULTS = {
    "Felix": {"StandStill": "0", "RunOnStartup": "0",
              "LikeMusician": "", "DislikeMusician": ""},
}


class FelixPet(PetEngine):
    def __init__(self):
        cfg = load_ini(INI_PATH, DEFAULTS)
        self.opts = cfg["Felix"]
        self.stand_still = self.opts.get("StandStill", "0") == "1"
        super().__init__(title="Felix", w=120, h=120, speed_ms=120)
        self._bubble = None
        self._phrase_tick = 0
        self.menu.delete(0, tk.END)
        self.menu.add_command(label="Stand Still", command=self._toggle_still)
        self.menu.add_command(label="Run on Startup", command=self._toggle_startup)
        self.menu.add_command(label="About", command=self._about)
        self.menu.add_command(label="Legal Disclaimer", command=self._legal)
        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=self.on_exit)
        self._face = "normal"

    def update_frame(self):
        if not self.stand_still:
            sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
            self._x += self._dx * 2
            self._y += self._dy
            if self._x < 0 or self._x + self.pet_w > sw:
                self._dx *= -1
            if self._y < 0 or self._y + self.pet_h > sh - 60:
                self._dy *= -1
            self.geometry(f"+{self._x}+{self._y}")
        # Vẽ mặt mèo đơn giản (sprite FIG1 gốc cần decoder đầy đủ)
        self.canvas.delete("all")
        self.canvas.create_oval(20, 20, 100, 100, fill="black", outline="gray")
        self.canvas.create_polygon(25, 30, 35, 5, 50, 25, fill="black", outline="gray")
        self.canvas.create_polygon(70, 25, 85, 5, 95, 30, fill="black", outline="gray")
        self.canvas.create_oval(40, 55, 50, 65, fill="yellow")
        self.canvas.create_oval(70, 55, 80, 65, fill="yellow")
        self.canvas.create_text(60, 90, text="Felix", fill="white", font=("Arial", 10, "bold"))
        # Thỉnh thoảng nói (như bản gốc)
        self._phrase_tick += 1
        if self._phrase_tick > 80 and random.random() < 0.05:
            self._phrase_tick = 0
            self._speak(random.choice(PHRASES))

    def _speak(self, text):
        if self._bubble:
            try:
                self._bubble.destroy()
            except Exception:
                pass
        self._bubble = tk.Toplevel(self)
        self._bubble.overrideredirect(True)
        self._bubble.attributes("-topmost", True)
        tk.Label(self._bubble, text=text, bg="lightyellow", relief="solid",
                 wraplength=200, justify="left").pack()
        self._bubble.geometry(f"+{self._x}+{self._y - 80}")
        self.after(4000, lambda: self._bubble.destroy() if self._bubble else None)

    def on_grab(self):
        self._speak("hey! put me down!")

    def _toggle_still(self):
        self.stand_still = not self.stand_still
        print("[felix] Stand Still =", self.stand_still)

    def _toggle_startup(self):
        # Ghi HKCU\\...\\Run như bản gốc (DeskToppers.ini + registry)
        try:
            import winreg, sys
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r"Software\Microsoft\Windows\CurrentVersion\Run",
                                 0, winreg.KEY_SET_VALUE)
            if self.opts.get("RunOnStartup", "0") == "1":
                winreg.DeleteValue(key, "FelixPet")
                self.opts["RunOnStartup"] = "0"
            else:
                winreg.SetValueEx(key, "FelixPet", 0, winreg.REG_SZ, sys.executable + " " + __file__)
                self.opts["RunOnStartup"] = "1"
            winreg.CloseKey(key)
        except Exception as e:
            print(f"[felix] Không ghi được Run key: {e}")

    def _about(self):
        print("The Felix ScreenMate is produced by AdTools, Inc. "
              "Sales contact:sales@adtoolsinc.com (bản tái dựng)")

    def _legal(self):
        print("[felix] Legal Disclaimer: bản remake học tập, sprite/nhãn gốc thuộc AdTools.")


if __name__ == "__main__":
    if not os.path.exists(INI_PATH):
        with open(INI_PATH, "w", encoding="utf-8-sig") as f:
            f.write("[Felix]\nStandStill=0\nRunOnStartup=0\n")
    FelixPet().start_timer()
    tk.mainloop()
