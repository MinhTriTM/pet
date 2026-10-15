# 🐾 Hệ Sinh Thái Desktop Pet & Động Cơ Rồng Thần Thoại 120 FPS

Kho lưu trữ tổng hợp các ứng dụng thú cưng màn hình (Desktop Pets) từ cổ điển đến hiện đại, bao gồm các phần mềm di sản và động cơ rồng thần thoại thế hệ mới viết bằng **Rust**.

---

## 📂 Cấu Trúc Kho Lưu Trữ

```text
D:\Pet/
├── rebuild/                              # Dự án tái cấu trúc hiện đại
│   ├── rust-pet/                         # 🐉 Động cơ Rồng Thần Thoại 120 FPS (Rust + eframe)
│   │   ├── src/                          # Mã nguồn Rust (main.rs, pet.rs)
│   │   ├── assets/dragons/               # Spritesheet, frame, GIF và prompt ngũ đại long
│   │   ├── pets/                         # File cấu hình rồng (.toml)
│   │   └── Cargo.toml
│   ├── python-pet/                       # Thử nghiệm Pet Engine bằng Python
│   ├── WinPenguins-src/                  # Mã nguồn gốc WinPenguins C
│   ├── Chay_Rong_120FPS.bat              # Script khởi chạy nhanh 5 loài rồng
│   └── Chay_Rust_Pet.bat                 # Script chạy nhanh ứng dụng Rust Pet
├── WinPenguinsPortable/                  # Bản portable của WinPenguins
├── docs/                                 # Tài liệu & hình ảnh nghiên cứu
│   └── screenshots/chatgpt/              # Ảnh chụp trao đổi và thiết kế kiến trúc
├── Golden Crimson Roaring Dragon Sprite.png
├── Golden Pixel Dragon Head Sprite.png
├── KE_HOACH_1_RONG_30FPS_300_900_FRAME.md # Kế hoạch chi tiết hoạt họa rồng
├── bird on desktop.exe                   # Chim đậu desktop cổ điển
├── BirdOnDesktop.exe                     # Phiên bản chim desktop nâng cấp
├── fafa.exe                              # Chú chó FaFa cổ điển
├── felix.exe                             # Chú mèo Felix cổ điển
├── Nuoi 3_meo_con tren desktop.zip       # Gói nuôi 3 mèo con desktop
└── WinPenguinsPortable_0.76_English.paf.exe
```

---

## 🐉 Điểm Nhấn: Động Cơ Rồng Thần Thoại 120 FPS (`rebuild/rust-pet`)

Được xây dựng trên nền tảng **Rust + eframe (egui 0.31)**, động cơ đạt hiệu năng cực cao ở tần số quét **120 FPS** (~8ms/frame), hỗ trợ trong suốt xuyên màn hình (transparent click-through/drag window).

### 🌟 Ngũ Đại Thần Long
- **🏯 Rồng Phương Đông (Serpentine - Thuật toán Kinematic Follow Chain 10 đốt thân):**
  1. **Thanh Long (`thanh-long`)**: Mộc long ngọc bích, râu dài phất phơ, sừng hươu, ngậm Dạ Minh Châu.
  2. **Hoàng Long (`hoang-long`)**: Thần long hoàng gia, vảy vàng kim, bờm đỏ rực lửa.
  3. **Hắc Long (`hac-long`)**: Ma long bóng đêm u minh phương Bắc, ánh tím lôi điện.
- **🏰 Rồng Phương Tây (Winged Wyverns - Vỗ cánh 120 FPS):**
  4. **Hỏa Long (`hoa-long`)**: Cánh dơi khổng lồ rực lửa, sừng nhọn, chùy gai đuôi.
  5. **Băng Long (`bang-long`)**: Cánh màng pha lê xanh tuyết phủ, hơi thở cực hàn.

### 🎯 10 Hành Động Độc Bản
1. **Lơ Lửng (`Idle`)**: Dao động sóng sin êm dịu tại chỗ.
2. **Tuần Tra (`FlyWander`)**: Bơi lượn tự do quanh màn hình.
3. **Lướt Siêu Tốc (`DashSprint`)**: Tăng tốc 2.5x kèm linh khí.
4. **Phun Phép (`BreatheElement`)**: Hỏa Long phun lửa, Băng Long phun tuyết, Rồng Đông phóng lôi điện.
5. **Gầm Thét (`Roar`)**: Rung chuyển nhẹ màn hình và hiệu ứng sóng âm.
6. **Đi Ngủ (`SleepZzz`)**: Nằm im thư giãn, bong bóng Zzz bay lên.
7. **Tinh Nghịch (`PlayfulScratch`)**: Gãi đầu, lắc mình đáng yêu.
8. **Sà Xuống (`HoverDive`)**: Liệng cánh bắt mồi theo quỹ đạo parabol.
9. **Đuổi Chuột (`ChaseCursor`)**: Bám đuổi theo con trỏ chuột thời gian thực.
10. **Sấm Ngôn (`TalkMythic`)**: Phát thoại cổ ngữ thần thoại qua bóng thoại.

---

## 🚀 Hướng Dẫn Khởi Chạy

### 1. Chạy Động Cơ Rồng Rust (120 FPS)
- **Cách 1**: Chạy qua file batch [`rebuild/Chay_Rong_120FPS.bat`](file:///D:/Pet/rebuild/Chay_Rong_120FPS.bat).
- **Cách 2**: Chạy bằng Cargo:
  ```powershell
  cd D:\Pet\rebuild\rust-pet
  cargo run --release -- --all
  ```

### 2. Chạy Các Pet Cổ Điển
- Nhấp đúp trực tiếp vào các file thực thi tương ứng: `felix.exe`, `fafa.exe`, `BirdOnDesktop.exe`, hoặc mở `WinPenguinsPortable/WinPenguinsPortable.exe`.

---

## 📜 Giấy Phép & Bản Quyền
Dự án được duy trì cho mục đích học tập, hoài niệm và phát triển công nghệ đồ họa hiệu năng cao trên Windows.
