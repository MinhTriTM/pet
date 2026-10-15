# QUY CHUẨN THIẾT KẾ: ẢNH 360 ĐỘ & CHUYỂN ĐỘNG TỪNG CHI TIẾT (5 LOÀI RỒNG 120 FPS)

Tài liệu này cung cấp giải pháp toàn diện về **đồ họa xoay 360 độ (8-Directional Turnaround)** và **chuyển động vi mô độc lập của từng chi tiết (Micro-Motion Skeletal Rigging)** cho 5 loài rồng thần thoại:
1. **Thanh Long Phương Đông** (Mộc Long Ngọc Bích)
2. **Hoàng Long Phương Đông** (Hoàng Kim Thần Long)
3. **Hắc Long Phương Đông** (U Minh Ma Long)
4. **Hỏa Long Phương Tây** (Crimson Fire Drake)
5. **Băng Long Phương Tây** (Frost Wyvern)

---

## PHẦN 1: HỆ QUY CHIẾU XOAY 360 ĐỘ (8-DIRECTIONAL TURNAROUND SETUP)

Để một nhân vật 2D/Pixel Art xoay được 360 độ mượt mà mà không bị méo mó, ta chuẩn hóa theo **8 hướng xoay cơ bản (bước nhảy 45°)**:

```
                  [180° - North] (Lưng sau)
                         ▲
       [135° - NW]       │       [225° - NE]
    (Chéo sau trái)      │      (Chéo sau phải)
             ↖           │           ↗
 [90° - West] ◄──────────┼──────────► [270° - East]
(Ngang trái 90°)         │         (Ngang phải 90°)
             ↙           │           ↘
       [45° - SW]        │       [315° - SE]
   (Chéo trước trái)     │     (Chéo trước phải)
                         ▼
                  [0° - South] (Chính diện)
```

### 1.1 Nguyên Tắc Đối Xứng Gương (Mirroring Optimization)
Trong game 2D chuyên nghiệp, không cần vẽ cả 8 hướng riêng lẻ mà chỉ cần vẽ **5 góc chuẩn**, 3 góc còn lại lật gương theo trục X (`ScaleX = -1`):
1. **Góc 0° (South):** Nhìn thẳng chính diện mặt trước.
2. **Góc 45° (South-West):** Nghiêng chéo 3/4 mặt trước bên trái. (Lật gương $\rightarrow$ Góc 315° SE).
3. **Góc 90° (West):** Góc nhìn ngang nhìn sang trái. (Lật gương $\rightarrow$ Góc 270° East).
4. **Góc 135° (North-West):** Nghiêng chéo 3/4 nhìn từ phía sau lưng. (Lật gương $\rightarrow$ Góc 225° NE).
5. **Góc 180° (North):** Nhìn thẳng lưng từ phía sau.

---

## PHẦN 2: CHUYỂN ĐỘNG VI MÔ CỦA TỪNG CHI TIẾT (MICRO-MOTION DETAILS)

Mỗi loài rồng được cấu tạo từ các chi tiết độc lập. Dưới đây là quy chuẩn chuyển động của từng chi tiết ở tốc độ **120 FPS**:

### 2.1 Cặp Mắt (Eye Tracking 360° & Blinking)
- **Con ngươi (Pupil):** Di chuyển tự do theo bán kính elip 360 độ dõi theo con trỏ chuột:
  $$\Delta x_{\text{pupil}} = r_x \cdot \cos(\theta_{\text{mouse}}), \quad \Delta y_{\text{pupil}} = r_y \cdot \sin(\theta_{\text{mouse}})$$
- **Chu kỳ chớp mắt (Blink Cycle - 120 FPS):**
  - Frame 0-100: Mắt mở to long lanh (`eyes_open.png`).
  - Frame 101-105: Mí mắt khép một nửa (Half-blink).
  - Frame 106-112: Mắt nhắm hoàn toàn hình vòng cung cười (`eyes_blink.png`).
  - Frame 113-118: Mở lại một nửa.
  - Frame 119-120: Mở to hoàn toàn.

### 2.2 Hàm Dưới & Miệng (Jaw & Roar Animation)
- **Hô hấp (Idle Breathing):** Hàm dưới nhấp nhô biên độ nhẹ $\pm 1.5\text{ px}$ theo nhịp thở 1.2 Hz.
- **Gầm thét (Roar):** Hàm dưới mở rộng $35^\circ$, cổ họng phát ánh sáng nguyên tố (Lửa / Băng / Lôi), phát ra các vòng sóng âm xung kích.

### 2.3 Cặp Râu Rồng & Sừng (Whisker Wave & Antler Wobble)
- **Râu rồng (Rồng phương Đông):** Mô phỏng vật lý mềm (Soft-body Verlet):
  - Gốc râu gắn mép mõm $\rightarrow$ Đốt giữa trễ 4 frame $\rightarrow$ Đuôi râu trễ 8 frame.
  - Chuyển động lượn sóng tự do theo gió: $y(t) = A_1 \sin(\omega_1 t) + A_2 \sin(\omega_2 t + \phi)$.
- **Sừng:** Dao động quán tính (Inertia Wobble) khi rồng quay đầu đổi hướng đột ngột.

### 2.4 Chuỗi 10 Đốt Thân Rồng (Inverse Kinematics Snake Orbit 360°)
- Đầu rồng (`HEAD`) làm vật dẫn đường (Target Lead).
- Mỗi đốt thân từ 1 đến 10 tuân thủ thuật toán ràng buộc khoảng cách (Distance Constraint):
  $$\vec{p}_{i} = \vec{p}_{i-1} - \text{normalize}(\vec{p}_{i-1} - \vec{p}_i) \cdot L$$
- Bổ sung dao động sóng uốn lượn ngang vuông góc với vectơ vận tốc:
  $$\vec{offset}_i = \vec{n} \cdot A \cdot \sin(\omega t - i \cdot \delta)$$
- Nhờ công thức này, rồng có thể lượn vòng tròn 360 độ hoặc xoắn ốc mà thân không bao giờ bị đứt gãy hay biến dạng.

### 2.5 Đôi Cánh Rồng Phương Tây (Perspective 3D Flap Cycle 120 FPS)
- **4 Pha đập cánh chuẩn giải phẫu:**
  1. **Glide (Lượn):** Sải cánh mở phẳng, màng cánh hơi cong đón gió.
  2. **Upstroke (Vỗ lên):** Cổ tay gập lại, diện tích màng cánh thu hẹp $40\%$ để giảm lực cản.
  3. **Apex (Điểm đỉnh):** Đầu cánh vươn cao nhất, màng cánh căng hết cỡ.
  4. **Downstroke (Quạt xuống):** Cánh mở rộng tối đa đập mạnh xuống dưới, đẩy thân rồng nảy lên $\Delta y = -4\text{ px}$.
- **Góc xoay 360° (Pseudo-3D):** Khi rồng nhìn nghiêng 45° hoặc 90°, cánh phía xa tự động thu nhỏ tỷ lệ `ScaleX = 0.65`, cánh phía gần mở rộng `ScaleX = 1.0` tạo chiều sâu không gian chân thực.

### 2.6 Dạ Minh Châu / Long Châu (Pseudo-3D Orbital VFX 360°)
- Viên ngọc bay quanh thân rồng theo quỹ đạo elip không gian 3D:
  $$x_{\text{orb}} = x_0 + R_x \cdot \cos(\alpha), \quad y_{\text{orb}} = y_0 + R_y \cdot \sin(\alpha) \cdot \sin(\beta)$$
- **Z-Buffering:**
  - Khi $\sin(\alpha) > 0$: Long Châu ở phía trước rồng $\rightarrow$ Vẽ đè lên thân rồng, độ sáng $100\%$.
  - Khi $\sin(\alpha) \le 0$: Long Châu ở phía sau rồng $\rightarrow$ Vẽ dưới lớp thân rồng, giảm độ sáng còn $65\%$ và thu nhỏ nhẹ.

---

## PHẦN 3: BỘ PROMPT AI SINH ẢNH 360 ĐỘ (TURNAROUND ASSET PROMPTS)

Sử dụng trực tiếp các câu prompt sau vào Midjourney v6.1 / SDXL / ComfyUI / DALL-E để sinh bảng xoay 360 độ cho từng chi tiết.

### 3.1 Prompt Sinh Bảng Xoay 360 Độ Cho Đầu Rồng Phương Đông (Thanh Long)
```text
masterpiece, best quality, retro game asset, 16-bit pixel art, 100 dpi, 2D character puppet rig turnaround sheet, 8-directional rotation views in a clean row: Front (0°), Front-Quarter (45°), Side Profile (90°), Back-Quarter (135°), Back View (180°).
Subject: Oriental Azure Dragon chibi head, emerald green jade scales (#00e5a3), cute snout, golden deer antlers, isolated on pure transparent background.
Each angle perfectly aligned horizontally with consistent eye-level and uniform scale, crisp pixel contours, no anti-aliasing blur --no background, merged body, human, 3d, realistic --ar 16:9 --v 6.1
```

### 3.2 Prompt Sinh Bảng Xoay 360 Độ Cho Đôi Cánh Rồng Phương Tây (Hỏa Long)
```text
masterpiece, best quality, retro game asset, 16-bit pixel art, 100 dpi, 2D dragon wing turnaround and flap animation sheet, isolated on pure transparent background.
Subject: Crimson Fire Drake bat wing, muscular crimson forearm with thumb claw, stretched translucent molten orange wing membrane (#f59e0b).
Components in 5 directional viewing angles (0°, 45°, 90°, 135°, 180°) and 4 flapping keyframe poses (glide, upstroke, apex, downstroke).
Clean pixel edges, uniform lighting, ready for 120fps skeletal rigging --no background, body, head, blur, 3d render --ar 16:9 --v 6.1
```

### 3.3 Prompt Sinh Bảng Xoay 360 Độ Của Khớp Đuôi & Chùy Gai (Băng Long)
```text
masterpiece, best quality, retro game asset, 16-bit pixel art, 100 dpi, 2D modular dragon tail turnaround sheet, 8 rotation angles around vertical axis.
Subject: Frost Wyvern ice crystal tail segment and diamond ice blade tip (#38bdf8, #e0f2fe), sharp crystalline facets.
Horizontally aligned standalone puppet piece on pure transparent background, crisp pixel contours --no background, dragon body, blur, 3d render --ar 16:9 --v 6.1
```

---

## PHẦN 4: THÔNG SỐ TÍCH HỢP TRONG ENGINE RUST 120 FPS
- **Chu kỳ cập nhật:** 8.33 ms (Chuẩn 120 Hz).
- **Trục xoay hướng mặt:** `facing_angle` tự nội suy (Lerp) theo góc di chuyển:
  $$\theta_{t} = \text{lerp\_angle}(\theta_{t-1}, \text{atan2}(v_y, v_x), 0.12)$$
- **Chớp mắt ngẫu nhiên:** Mỗi 3 - 6 giây kích hoạt chuỗi nháy mắt 10 frame.
- **Râu & Bờm:** Cập nhật 120 lần/giây theo phương trình sóng sin đa tầng.
