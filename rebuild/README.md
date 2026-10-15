# Khôi phục source D:\Pet — Báo cáo tổng hợp

Ngày: 2026-10-12 | Máy: Windows 11 | Công cụ: pefile, Pillow, Ghidra-style strings

## 1. Kết luận nhanh

| File gốc | Bản chất | Source gốc lấy lại được? |
|---|---|---|
| `bird on desktop.exe` (= `BirdOnDesktop.exe`, cùng SHA256 `55BFD8CA…`) | SEGA DeskTopBird Kingfisher 1997, MFC4/VC++ native | Không 1:1. Đã trích resources + viết lại `python-pet/bird.py` |
| `fafa.exe` (SHA256 `ED094715…`) | FaFa Cat 2002, C.K.Tong / SilverMeow, VC++ native + engine INI | Không 1:1. Đã trích 6 bitmap + viết lại `python-pet/fafa.py` giữ nguyên schema action/ratio |
| `felix.exe` (SHA256 `06C07CE5…`) | Felix ScreenMate 1999, AdTools Inc, native + zlib, `scene.cpp` | Không 1:1. Đã giải mã 30/31 sprite FIG1 + viết lại `python-pet/felix.py` |
| `WinPenguinsPortable/` (`winpenguins.exe` 2011 MFC10 + launcher NSIS) | WinPenguins GPL-2.0 | **Có 100%** tại `rebuild/WinPenguins-src/` (clone từ `ricky65/WinPenguins`) |

> Lý do không thể “dịch ngược ra source C++ gốc”: cả 3 pet đều là PE32 native
> đã strip PDB (`Machine=0x14C`, `CLR dir=0`), không còn tên biến/comment.
> Decompiler (Ghidra/IDA) chỉ cho assembly. Cách đúng là clean-room remake
> + tái dùng tài nguyên đã trích cho mục đích cá nhân.

## 2. Cây thư mục khôi phục

```
D:\Pet\
  bird on desktop.exe  BirdOnDesktop.exe  fafa.exe  felix.exe   (gốc, giữ nguyên)
  rebuild\
    WinPenguins-src\      <- git clone https://github.com/ricky65/WinPenguins.git
        MainWnd.cpp/.h, Toon.cpp/.h, winpenguinsDlg.*, winpenguins.rc, *.vcxproj ...
    assets\
      bird_on_desktop\ bitmap_ALL_17_1.bmp (477x477) + .dib, wave .wav 49KB,
                       menu/dialog/version .bin, icon/cursor
      fafa\            bitmap_103/107/110/111/112/114 .bmp + .dib, menu/dialog/manifest
      felix\           None_301..329,1200 (FIG1+zlib, đã decode 30/31),
                       IDB_PAL, menu IDR_POPUP, dialog, string tables
    python-pet\
      pet_engine.py   <- khung chung (trong suốt/topmost/timer/menu/INI)
      bird.py         <- remake Kingfisher (bay/đậu/giả chết/kêu wave)
      fafa.py         <- remake FaFa (engine Action ratio/next/dislike/bound)
      felix.py        <- remake Felix (đi bộ/bóng thoại/registry Run)
      fig_decoder.py  <- decode FIG1 (header 18B + zlib), đã verify 30/31
      run_all.py      <- chạy cả 3 con cùng lúc
      requirements.txt (Pillow, pefile)
```

## 3. Chi tiết phân tích ngược (bằng chứng)

- PE: bird 6 sections (`.text 89KB, .rsrc 286KB`), fafa 4 sections
  (`.text 57KB, .rsrc 308KB`), felix 4 sections (`.text 86KB, .rsrc 189KB`).
- Import chung: `user32(SetTimer/KillTimer/TrackPopupMenu/LoadMenuA/LoadBitmapA)`,
  `gdi32(CreateBitmap/CreateCompatibleBitmap/BitBlt/StretchBlt)`,
  `kernel32, comdlg32, advapi32, shell32` (+ `winmm/sndPlaySoundA` ở bird,
  `zlib inflate 1.1.2` ở felix, manifest `<assembly>` ở fafa).
- Menu/Dialog trích nguyên văn bằng pefile (xem `assets/*/menu_*.bin`,
  `dialog_*.bin`): bird `Window/STOP/DTB[Kingfisher]/HELP`, fafa
  `&File/&Continue/&Option/&About FaFa Cat/&Exit` + dialog
  `FaFa Cat - Option (Display Mode/Boundary/Speed)`, felix `Stand Still/
  Run on Startup/About/Legal/Exit`.
- INI: `DeskTopBird_K.ini [SEGA DeskTopBird_Kingfisher] SOUND=%d`,
  `fafa.ini` qua `GetPrivateProfileIntA/WritePrivateProfileStringA`,
  `DeskToppers.ini` + `HKCU...\\Run`.
- FIG1 Felix: magic `46494731`, header 18 byte, payload zlib từ offset 18,
  giải nén ra 1024 byte/frame (xem `fig_decoder.py`).

## 4. Cách dùng

### 4.1 WinPenguins (source gốc xịn)
```cmd
cd D:\Pet\rebuild\WinPenguins-src
:: Mở winpenguins.sln bằng Visual Studio 2022, Ctrl+F5 để chạy
```
Bản này mới hơn exe 2011 của bạn (đã bỏ `winmon.dll`, vẽ overlay trong suốt,
hỗ trợ Win10/11). Muốn đúng bản 2011 thì xem thêm `kasper93/winpenguins`.

### 4.2 Pet Python (cần Python 3.10+)
```cmd
cd D:\Pet\rebuild\python-pet
pip install -r requirements.txt
python bird.py      :: chim SEGA
python fafa.py      :: mèo FaFa (đọc fafa.ini)
python felix.py     :: mèo Felix (đọc DeskToppers.ini)
python run_all.py   :: cả 3 con như "Nuôi 3 mèo con trên desktop"
pyinstaller --noconsole --onefile bird.py   :: đóng gói exe nếu muốn
```
Chuột phải mỗi con = menu gốc. Kéo-thả để di chuyển.
Bird thả gần taskbar sẽ giả chết (đúng bản gốc). Felix `Run on Startup`
ghi `HKCU\...\Run\FelixPet`.

## 5. Việc còn lại (nếu muốn giống pixel 1:1)

1. Mở `assets/*/*.bmp` xem sprite, cắt frame đúng kích thước nhân vật
   (hiện remake tự resize về 96–151px).
2. Dùng Resource Hacker mở exe gốc để xem dialog layout pixel rồi chỉnh
   `IDD_DIALOG/IDD_OPTION` cho khớp.
3. Nạp Ghidra với 3 exe để lấy state-machine chi tiết (tốc độ bay, bảng action),
   rồi port hằng số vào `bird.py/fafa.py/felix.py`.
4. Thay `PHRASES` trong `felix.py` bằng full string-table đã trích
   (`string_1_9_2.string.bin`).

## 6. Lưu ý bản quyền

- WinPenguins: GPL-2.0, tự do dùng/sửa với điều kiện giữ license (`COPYING.txt`).
- Bird (SEGA), FaFa (SilverMeow), Felix (AdTools): freeware đóng source,
  tài nguyên trong `assets/` chỉ nên dùng cá nhân/nghiên cứu tương thích,
  không phát hành lại thương mại.

## 7. Phát triển thêm: nhiều pet + nhiều tính năng (Python & Rust)

Đã dựng sẵn 2 stack dùng chung ý tưởng (1 process, N pet, config file):

### 7.1 Python — `rebuild/python-pet/` (dễ sửa, hợp prototype)
- Mới: `pet_framework.py` (Pet + PetManager: 1 root ẩn + N Toplevel),
  `multi_pet.py`, `pets/*.json` (4 mẫu), `test_no_gui.py`.
- 4 pet mẫu vẽ bằng code (không dính bản quyền):
  `robo-cat`, `pixel-bird`, `mini-penguin` (tri ân WinPenguins),
  `ghost-boo`. Thêm con mới = copy 1 file JSON + thêm hàm vẽ vào
  `DRAWERS` trong `pet_framework.py`.
- Tính năng mới so với exe gốc: chạy N con 1 lúc, va chạm đổi hướng +
  chào nhau (`PetManager._collide`), menu chuột phải từng con, ẩn/hiện.
- Chạy/kiểm thử:
```cmd
cd D:\Pet\rebuild\python-pet
pip install -r requirements.txt
python multi_pet.py                    :: cả 4 con
python multi_pet.py robo-cat ghost-boo :: chọn con
python test_no_gui.py                  :: test headless (đã pass)
pyinstaller --noconsole --onefile multi_pet.py
```
- File cũ `bird.py/fafa.py/felix.py` vẫn giữ nguyên để tham chiếu remake 1:1.

### 7.2 Rust — `rebuild/rust-pet/` (exe gọn ~MB, RAM thấp, không cần runtime)
- Stack: `eframe 0.31 + egui + serde + toml + rand`.
  Mỗi pet = 1 viewport riêng (borderless + always_on_top + transparent),
  chung 1 `App` quản lý + cửa sổ Pet Control.
- Config: `pets/*.toml` (cùng nội dung bản Python, đọc bằng `toml::from_str`).
- Logic `src/pet.rs` port từ Python: wander/bounce/sit_random + unit test.
- Chạy/kiểm thử:
```cmd
cd D:\Pet\rebuild\rust-pet
cargo check        :: đã pass (1 warning dead_code color, kệ được)
cargo test         :: đã pass 2/2 (bounce + hello)
cargo run -- --all :: tất cả pet
cargo run -- --pet robo-cat --pet ghost-boo
cargo build --release  :: ra exe duy nhất trong target/release/
```
- TODO v0.2: system tray (`tray-icon` + `muda`), bóng thoại egui Window,
  sprite PNG thay hình vẽ, lưu vị trí ra TOML, CLI `--count N` nhân bản pet.
