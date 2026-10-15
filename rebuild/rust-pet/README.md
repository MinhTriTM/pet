# 🐉 Động Cơ Rồng Thần Thoại 120 FPS (Phương Đông & Phương Tây)

Động cơ thú cưng desktop thần thoại xây dựng bằng **Rust + eframe (egui 0.31)** — mô phỏng 5 đại thần long Á - Âu uốn lượn và bay lượn ở tần số quét cao **120 FPS** (~8ms mỗi khung hình) trên màn hình Windows.

---

## 🌟 5 Loài Rồng Thần Thoại

### 🏯 3 Rồng Phương Đông (Serpentine Dragons — Động học 10 Đốt Thân)
1. **Thanh Long (Azure Dragon)** (`thanh-long`):
   - Mộc long xanh ngọc lục bảo, thân dài uốn lượn mềm mại theo thuật toán *Kinematic Follow Chain*.
   - Râu rồng dài phất phơ trong gió, sừng hươu thần thoại, ngậm Dạ Minh Châu phát quang.
2. **Hoàng Long (Golden Celestial Dragon)** (`hoang-long`):
   - Thần long hoàng gia tôn quý, thân vàng óng ánh, bờm đỏ rực lửa, mây ngũ sắc phiêu dật.
3. **Hắc Long (Abyssal Shadow Dragon)** (`hac-long`):
   - Ma long bóng đêm u minh phương Bắc, vảy đen ánh tím ma thuật, sấm sét lôi đình bao quanh.

### 🏰 2 Rồng Phương Tây (Winged Wyverns — Vỗ Cánh 120 FPS)
4. **Hỏa Long (Crimson Fire Drake)** (`hoa-long`):
   - Vảy đỏ rực rỡ, đôi cánh dơi khổng lồ sải rộng đập liên hồi ở 120 FPS, sừng quỷ nhọn hoắt, đuôi có chùy gai tam giác.
5. **Băng Long (Frost Wyvern)** (`bang-long`):
   - Rồng tuyết bắc cực với lớp màng cánh pha lê xanh băng giá, sừng băng sắc lạnh, thở ra hơi lạnh cực hàn.

---

## 🎯 10 Hành Động Độc Bản (10 Behaviors & Actions)

| STT | Tên Hành Động | Tên Tiếng Anh | Mô Tả Hiệu Ứng Trực Quan (120 FPS) |
| :---: | :--- | :--- | :--- |
| **1** | **Lơ Lửng** | `Idle` | Bay dao động nhẹ nhàng tại chỗ theo hàm sin, râu/cánh đung đưa nhịp nhàng. |
| **2** | **Tuần Tra** | `FlyWander` | Thân rồng uốn lượn liên hoàn hình sóng sin tuần tra quanh màn hình desktop. |
| **3** | **Lướt Siêu Tốc** | `DashSprint` | Phóng nhanh gấp 2.5 lần tốc độ bình thường kèm vệt sáng hào quang linh khí. |
| **4** | **Phun Phép** | `BreatheElement` | Hỏa Long phun bão lửa đỏ cam; Băng Long phun bão tuyết; Rồng Đông phóng lôi điện long châu. |
| **5** | **Gầm Thét** | `Roar` | Sóng âm chấn động lan tỏa từ miệng rồng, rung chuyển nhẹ màn hình (`ROAR!!`). |
| **6** | **Đi Ngủ** | `SleepZzz` | Nằm im lìm phập phồng thư giãn, bong bóng chữ `Zzz...` bay lên nhẹ nhàng. |
| **7** | **Tinh Nghịch** | `PlayfulScratch` | Quay đầu, vuốt râu, lắc đuôi qua lại tinh nghịch và đáng yêu. |
| **8** | **Sà Xuống** | `HoverDive` | Bay vút lên cao rồi sà cánh xuống bắt mồi theo quỹ đạo hình parabol. |
| **9** | **Đuổi Chuột** | `ChaseCursor` | Đuổi theo con trỏ chuột của người dùng theo thời gian thực (real-time tracking). |
| **10**| **Sấm Ngôn** | `TalkMythic` | Bật bóng thoại phát sấm ngôn cổ ngữ thần thoại ngẫu nhiên. |

---

## 🚀 Cách Chạy & Trải Nghiệm

1. **Chạy tức thì toàn bộ 5 loài rồng**:
   - Nhấp đúp vào: [`D:\Pet\rebuild\Chay_Rong_120FPS.bat`](file:///D:/Pet/rebuild/Chay_Rong_120FPS.bat)
   - Hoặc gõ lệnh:
     ```powershell
     D:\Pet\rebuild\rust-pet\target\release\rust-pet.exe --all
     ```

2. **Tương tác**:
   - **Click chuột phải vào rồng**: Nghe sấm ngôn cổ ngữ qua bóng thoại.
   - **Di chuột trên màn hình**: Khi rồng ở chế độ `Đuổi Chuột (Chase)`, rồng sẽ bơi theo con trỏ chuột của bạn!
   - **Bảng điều khiển**: Cho phép kích hoạt đồng loạt bất kỳ hành vi nào trong 10 hành động cho toàn bộ rồng!
