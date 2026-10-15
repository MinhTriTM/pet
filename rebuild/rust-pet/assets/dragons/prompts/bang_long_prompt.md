# BỘ PROMPT TẠO TỪNG TỆP ASSET PIXEL ART TÁCH KHỚP: BĂNG LONG (FROST WYVERN)

**Loài:** Băng Long Phương Tây (Băng Tinh Phi Long Bắc Cực)  
**Chuẩn kỹ thuật chung:**  
- **Độ phân giải:** 100 DPI  
- **Nền:** Trong suốt hoàn toàn (Transparent Alpha RGBA - Tuyệt đối không dính nền)  
- **Phong cách:** 16-bit / 32-bit Chibi Pixel Art phương Tây, vảy băng pha lê trong suốt óng ánh, cánh thủy tinh băng tuyết, viền nét sắc lạnh.  
- **Định dạng xuất:** Mỗi câu Prompt dưới đây dùng để sinh ra **CHÍNH XÁC 1 TỆP ẢNH PNG ĐỘC LẬP**.  
- **Mục đích:** Ghép xương modular trong Spine 2D, Live2D, DragonBones hoặc Rust Engine cho chuyển động đập cánh băng lướt gió 120 FPS.

---

## 🎨 BẢNG MÃ MÀU CHUẨN (PALETTE BĂNG LONG)
- **Vảy xanh băng tuyết (Chính):** `#38bdf8`, `#0284c7`, `#0369a1`
- **Ánh kim cương / Bụng tuyết / Highlight:** `#e0f2fe`, `#f0f9ff`, `#ffffff`
- **Màng cánh pha lê & Băng tinh:** `#bae6fd`, `#7dd3fc`, `#a5f3fc`
- **Sừng băng thạch nhũ & Móng vuốt:** `#0c4a6e`, `#0284c7`, `#e0f2fe`
- **Viền nét Pixel Outline:** `#082f49` (Xanh hải quân thẫm cực hàn)

---

## 📂 DANH SÁCH 12 TỆP ASSET ĐỘC LẬP & PROMPT CHI TIẾT

```
assets/dragons/parts/bang_long/
├── 01_head_base.png              # Đầu rồng băng pha lê
├── 02_jaw_lower.png              # Hàm dưới răng nanh băng
├── 03_eyes_frost.png             # Mắt kim cương xanh lam cực quang
├── 04_horns_glacier.png          # Cặp sừng thạch nhũ băng nhọn hoắt
├── 05_torso_chest.png            # Thân mình & ức ngực vảy tuyết
├── 06_wing_arm_joint.png         # Xương cánh băng tinh
├── 07_wing_membrane_crystal.png  # Màng cánh pha lê trong suốt
├── 08_foreleg_claw.png           # Chân trước & móng vuốt băng
├── 09_hindleg_thigh.png          # Chân sau cơ bắp & móng vuốt
├── 10_tail_segmented.png         # Thân đuôi gai băng sống lưng
├── 11_tail_ice_blade.png         # Lưỡi kiếm băng tinh chóp đuôi
└── 12_frost_breath_vfx.png       # Luồng sương tuyết cực hàn đóng băng
```

---

### TỆP 01: `01_head_base.png` (Đầu Rồng Băng Pha Lê)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Đáy cổ sau gáy `[40%, 85%]`
- **Z-Order Layer:** Layer 50
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Western Frost Wyvern dragon chibi head, sleek icy predator snout with delicate frost ridges, shimmering glacial ice-blue scales (#38bdf8) with sparkling white diamond highlights, clean deep navy pixel outline, centered on pure transparent background, no lower jaw, no horns, no neck, no eyes, pure isolated skull asset --no background, eyes, jaw, horns, blur, 3d, realistic --ar 1:1
```

---

### TỆP 02: `02_jaw_lower.png` (Hàm Dưới Răng Nanh Băng)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp hàm sau `[30%, 30%]`
- **Z-Order Layer:** Layer 45
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Western Frost Wyvern chibi lower jaw, open mouth with icy mist breath glow, sharp translucent icicle fang teeth, pale cyan ice chin, crisp pixel contours, centered on pure transparent background, modular piece for puppet rigging --no background, upper head, eyes, horns, blur --ar 1:1
```

---

### TỆP 03: `03_eyes_frost.png` (Mắt Kim Cương Xanh Lam Cực Quang)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Trung tâm mắt `[50%, 50%]`
- **Z-Order Layer:** Layer 55
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of cute cold anime dragon eyes, glowing aurora cyan irises (#7dd3fc) with sharp frost crystal pupils, diamond star light glints, centered on pure transparent background, standalone facial asset --no face, no skin, no background, blur --ar 1:1
```

---

### TỆP 04: `04_horns_glacier.png` (Cặp Sừng Thạch Nhũ Băng Nhọn Hoắt)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Gốc chân sừng `[50%, 95%]`
- **Z-Order Layer:** Layer 48
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of sharp translucent glacier ice horns, crystalline stalactite texture (#e0f2fe) with deep arctic blue core shadows, crisp faceted pixel edges, centered on pure transparent background, standalone headpiece --no head, no background, blur, 3d --ar 1:1
```

---

### TỆP 05: `05_torso_chest.png` (Thân Mình & Ức Ngực Vảy Tuyết)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Tâm trọng tâm hông `[50%, 60%]`
- **Z-Order Layer:** Layer 35
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Western Frost Dragon torso and sleek chest, glinting cyan-blue back scales (#38bdf8), pristine snow-white underbelly armor plates (#f0f9ff), frosty dorsal ridges, clean pixel shading, centered on pure transparent background, standalone torso rig asset --no head, no wings, no legs, no tail, no background --ar 1:1
```

---

### TỆP 06: `06_wing_arm_joint.png` (Xương Cánh Băng Tinh)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp vai `[15%, 85%]`
- **Z-Order Layer:** Layer 60 (Cánh trước) & Layer 20 (Cánh sau)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, slender frost wyvern wing arm bone structure, sharp icicle hook claw at elbow, scaled sky-blue limb, 3 elongated ice crystal finger struts, clean pixel outline, centered on pure transparent background, standalone wing skeleton piece --no wing membrane, no body, no background, blur --ar 1:1
```

---

### TỆP 07: `07_wing_membrane_crystal.png` (Màng Cánh Pha Lê Trong Suốt)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Điểm bám vai `[15%, 85%]`
- **Z-Order Layer:** Layer 58 (Cánh trước) & Layer 18 (Cánh sau)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, semi-translucent crystal ice wing membrane, pale frosty cyan glass texture (#bae6fd) with subtle snowflake lattice refraction patterns, sharp scalloped edges, crisp pixel edges, centered on pure transparent background, standalone wing flap asset --no wing bones, no body, no background, blur --ar 1:1
```

---

### TỆP 08: `08_foreleg_claw.png` (Chân Trước & Móng Vuốt Băng)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp vai trên `[50%, 15%]`
- **Z-Order Layer:** Layer 40 (Chân gần) & Layer 15 (Chân xa)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, cute chibi frost dragon front leg, slender cyan-blue scaled forearm with 3 sharp translucent ice crystal talons, clean pixel art contours, centered on pure transparent background, standalone limb joint --no body, no background, blur --ar 1:1
```

---

### TỆP 09: `09_hindleg_thigh.png` (Chân Sau Cơ Bắp & Móng Vuốt)
- **Kích thước khuyến nghị:** 192x192 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp háng đùi `[50%, 20%]`
- **Z-Order Layer:** Layer 38 (Chân gần) & Layer 12 (Chân xa)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, chibi frost dragon hind leg and thigh, muscular arctic blue scaled thigh plate with sharp knee spike and icy foot talons, crisp pixel lines, centered on pure transparent background, standalone leg joint --no body, no background, blur --ar 1:1
```

---

### TỆP 10: `10_tail_segmented.png` (Thân Đuôi Gai Băng Sống Lưng)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Gốc nối hông `[10%, 50%]`
- **Z-Order Layer:** Layer 25
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, tapered flexible frost dragon tail segment, icy cyan scales with row of sharp crystalline frost spikes along dorsal spine, graceful curve, crisp pixel outline, centered on pure transparent background, modular tail bone asset --no tail tip, no body, no background, blur --ar 1:1
```

---

### TỆP 11: `11_tail_ice_blade.png` (Lưỡi Kiếm Băng Tinh Chóp Đuôi)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Gốc nối đuôi `[20%, 50%]`
- **Z-Order Layer:** Layer 26
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, diamond ice blade dragon tail tip, razor-sharp elongated glacier crystal dagger (#e0f2fe) with glowing cyan edge highlights, crisp faceted pixel edges, centered on pure transparent background, standalone tail weapon piece --no tail body, no background, blur --ar 1:1
```

---

### TỆP 12: `12_frost_breath_vfx.png` (Luồng Sương Tuyết Cực Hàn)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Điểm phát xạ tại miệng `[10%, 50%]`
- **Z-Order Layer:** Layer 70 (Phía trước nhất)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, freezing blast stream of blizzard frost breath, churning white and pale blue ice vapor mist, floating sharp snowflake crystal particles (#ffffff, #a5f3fc), crisp pixel art particle VFX, centered on pure transparent background, standalone magic effect --no dragon, no background, blur --ar 1:1
```

---

## ⚙️ HƯỚNG DẪN LẮP RÁP RIGGING 120 FPS
- Cánh pha lê băng có thể chỉnh độ mờ đục Alpha (opacity: 85%) trong engine để tạo độ trong suốt khúc xạ ánh sáng khi vỗ cánh.
- Luồng hơi thở sương tuyết `12_frost_breath_vfx.png` chạy hiệu ứng trượt texture (UV Scroll) hoặc hệ thống hạt (Particle Emitter) tại 120 FPS để tạo luồng bão tuyết đóng băng mặt đất.
