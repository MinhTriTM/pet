# BỘ PROMPT TẠO TỪNG TỆP ASSET PIXEL ART TÁCH KHỚP: HỎA LONG (CRIMSON FIRE DRAKE)

**Loài:** Hỏa Long Phương Tây (Bạo Long Lửa Đỏ Cánh Dơi)  
**Chuẩn kỹ thuật chung:**  
- **Độ phân giải:** 100 DPI  
- **Nền:** Trong suốt hoàn toàn (Transparent Alpha RGBA - Tuyệt đối không có nền)  
- **Phong cách:** 16-bit / 32-bit Chibi Pixel Art phương Tây, giáp vảy đỏ dung nham rực rỡ, cánh dơi mạnh mẽ, viền nét rõ ràng.  
- **Định dạng xuất:** Mỗi câu Prompt dưới đây dùng để sinh ra **CHÍNH XÁC 1 TỆP ẢNH PNG ĐỘC LẬP**.  
- **Mục đích:** Ghép xương modular trong Spine 2D, Live2D, DragonBones hoặc Rust Engine cho chuyển động đập cánh, khạc lửa 120 FPS.

---

## 🎨 BẢNG MÃ MÀU CHUẨN (PALETTE HỎA LONG)
- **Vảy đỏ thẫm (Chính):** `#dc2626`, `#b91c1c`, `#991b1b`
- **Mảng giáp ngực / Bụng vàng đất:** `#ea580c`, `#f97316`, `#fed7aa`
- **Màng cánh dơi & Lửa dung nham:** `#f59e0b`, `#fbbf24`, `#fef08a`
- **Sừng nham thạch & Gai lưng:** `#451a03`, `#78350f`, `#1c1917`
- **Viền nét Pixel Outline:** `#450a0a` (Đỏ nâu đen thẫm)

---

## 📂 DANH SÁCH 12 TỆP ASSET ĐỘC LẬP & PROMPT CHI TIẾT

```
assets/dragons/parts/hoa_long/
├── 01_head_base.png          # Đầu rồng lửa phương Tây
├── 02_jaw_lower.png          # Hàm dưới khạc lửa
├── 03_eyes_fiery.png         # Mắt rực lửa dung nham
├── 04_horns_demon.png        # Cặp sừng quỷ nham thạch cong vút
├── 05_torso_chest.png        # Thân mình & ức ngực cơ bắp
├── 06_wing_arm_joint.png     # Xương cánh tay có mấu vuốt
├── 07_wing_membrane.png      # Màng cánh dơi đỏ cam
├── 08_foreleg_claw.png       # Chân trước & móng vuốt
├── 09_hindleg_thigh.png      # Chân sau cơ bắp & móng
├── 10_tail_segmented.png     # Thân đuôi có sống gai nhọn
├── 11_tail_blade_club.png    # Chùy gai nhọn chóp đuôi
└── 12_fire_breath_vfx.png    # Cột lửa bùng cháy dữ dội
```

---

### TỆP 01: `01_head_base.png` (Đầu Rồng Lửa Phương Tây)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Đáy cổ sau gáy `[40%, 85%]`
- **Z-Order Layer:** Layer 50
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Western Crimson Fire Dragon chibi head, reptilian predator snout with nostrils, armored scarlet crimson red scales (#dc2626), clean deep maroon pixel outline, centered on pure transparent background, no lower jaw, no horns, no neck, no eyes, pure isolated skull asset --no background, eyes, jaw, horns, blur, 3d, realistic --ar 1:1
```

---

### TỆP 02: `02_jaw_lower.png` (Hàm Dưới Khạc Lửa)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp hàm sau `[30%, 30%]`
- **Z-Order Layer:** Layer 45
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Western Fire Drake chibi lower jaw, open gaping mouth with glowing lava throat glow, sharp white reptile fangs, crimson scaled chin, crisp pixel art contours, centered on pure transparent background, modular piece for puppet rigging --no background, upper head, eyes, horns, blur --ar 1:1
```

---

### TỆP 03: `03_eyes_fiery.png` (Mắt Rực Lửa Dung Nham)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Trung tâm mắt `[50%, 50%]`
- **Z-Order Layer:** Layer 55
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of fierce cute dragon eyes, blazing magma golden-amber irises (#f59e0b) with bright vertical slit pupils, glowing hot flame reflections, centered on pure transparent background, standalone facial feature asset --no face, no skin, no background, blur --ar 1:1
```

---

### TỆP 04: `04_horns_demon.png` (Cặp Sừng Quỷ Nham Thạch)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Gốc chân sừng `[50%, 95%]`
- **Z-Order Layer:** Layer 48
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of curved demonic dragon horns sweeping backward, textured volcanic obsidian rock ridges (#451a03), sharp tips with red hot ember glow, crisp pixel contours, centered on pure transparent background, standalone headpiece --no head, no background, blur, 3d --ar 1:1
```

---

### TỆP 05: `05_torso_chest.png` (Thân Mình & Ức Ngực Cơ Bắp)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Tâm trọng tâm hông `[50%, 60%]`
- **Z-Order Layer:** Layer 35
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Western Fire Dragon torso and muscular chest, crimson back armor plates (#dc2626) and warm orange-yellow ribbed belly scutes (#f97316), dorsal ridge spikes, crisp pixel shading, centered on pure transparent background, standalone torso rig asset --no head, no wings, no legs, no tail, no background --ar 1:1
```

---

### TỆP 06: `06_wing_arm_joint.png` (Khớp Xương Cánh Tay Có Vuốt)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp vai `[15%, 85%]`
- **Z-Order Layer:** Layer 60 (Cánh trước) & Layer 20 (Cánh sau)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, muscular bat-like dragon wing arm bone structure, sharp thumb claw hook at elbow joint, scaled crimson red arm limb, 3 elongated finger struts, clean pixel outline, centered on pure transparent background, standalone wing skeleton piece --no wing membrane, no body, no background, blur --ar 1:1
```

---

### TỆP 07: `07_wing_membrane.png` (Màng Cánh Dơi Đỏ Cam)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Điểm bám vai `[15%, 85%]`
- **Z-Order Layer:** Layer 58 (Cánh trước) & Layer 18 (Cánh sau)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, leather bat wing skin membrane for fire dragon, semi-translucent glowing orange-amber webbing (#f59e0b) stretched between fingers, realistic scalloped edges, crisp pixel edges, centered on pure transparent background, standalone wing flap asset --no wing bones, no body, no background, blur --ar 1:1
```

---

### TỆP 08: `08_foreleg_claw.png` (Chân Trước & Móng Vuốt)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp vai trên `[50%, 15%]`
- **Z-Order Layer:** Layer 40 (Chân gần) & Layer 15 (Chân xa)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, cute chibi western dragon front leg, muscular crimson red forearm with 3 sharp black volcanic talons, clean pixel art contours, centered on pure transparent background, standalone limb joint --no body, no background, blur --ar 1:1
```

---

### TỆP 09: `09_hindleg_thigh.png` (Chân Sau Cơ Bắp & Móng)
- **Kích thước khuyến nghị:** 192x192 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp háng đùi `[50%, 20%]`
- **Z-Order Layer:** Layer 38 (Chân gần) & Layer 12 (Chân xa)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, powerful chibi dragon hind leg and thigh, muscular crimson thigh plate with digitized knee joint and sharp foot claws, crisp pixel lines, centered on pure transparent background, standalone leg joint --no body, no background, blur --ar 1:1
```

---

### TỆP 10: `10_tail_segmented.png` (Thân Đuôi Có Sống Gai Nhọn)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Gốc nối hông `[10%, 50%]`
- **Z-Order Layer:** Layer 25
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, tapered flexible dragon tail segment, crimson red reptile scales with sharp dorsal magma spikes along spine, gentle curve, crisp pixel outline, centered on pure transparent background, modular tail bone asset --no tail tip, no body, no background, blur --ar 1:1
```

---

### TỆP 11: `11_tail_blade_club.png` (Chùy Gai Nhọn Chóp Đuôi)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Gốc nối đuôi `[20%, 50%]`
- **Z-Order Layer:** Layer 26
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, spade-shaped arrow blade dragon tail tip, razor-sharp volcanic obsidian tail blade (#451a03) with glowing orange molten edges, crisp pixel edges, centered on pure transparent background, standalone tail accessory --no tail body, no background, blur --ar 1:1
```

---

### TỆP 12: `12_fire_breath_vfx.png` (Cột Lửa Bùng Cháy Dữ Dội)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Điểm phát hỏa tại miệng `[10%, 50%]`
- **Z-Order Layer:** Layer 70 (Phía trước nhất)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, roaring stream of blazing dragon fire breath, bright yellow-white core fireball surrounded by leaping orange flame tongues and flying ember sparks (#fef08a, #f97316), clean pixel art VFX, centered on pure transparent background, standalone magic breath effect --no dragon, no background, blur --ar 1:1
```

---

## ⚙️ HƯỚNG DẪN LẮP RÁP RIGGING 120 FPS
- Cơ chế cánh dơi 2 tầng: Ghép `06_wing_arm_joint.png` với `07_wing_membrane.png`, thiết lập biến dạng Mesh Deform / FFD trên màng cánh để tạo nhịp đập cánh 120 FPS phập phồng chân thực.
- Đầu và hàm dưới mở rộng kết hợp kích hoạt hạt hiệu ứng khạc lửa `12_fire_breath_vfx.png` khi người dùng nhấp chuột hoặc ra lệnh hành động chiến đấu.
