# BỘ PROMPT TẠO TỪNG TỆP ASSET PIXEL ART TÁCH KHỚP: HOÀNG LONG (GOLDEN DRAGON)

**Loài:** Hoàng Long Phương Đông (Thần Long Đế Vương Hoàng Kim)  
**Chuẩn kỹ thuật chung:**  
- **Độ phân giải:** 100 DPI  
- **Nền:** Trong suốt hoàn toàn (Transparent Alpha RGBA - Không nền trắng/đen)  
- **Phong cách:** 16-bit / 32-bit Chibi Pixel Art hoàng gia, vảy vàng dát sáng rực, viền sắc nét, không mờ nhòe.  
- **Định dạng xuất:** Mỗi câu Prompt dưới đây dùng để sinh ra **CHÍNH XÁC 1 TỆP ẢNH PNG ĐỘC LẬP**.  
- **Mục đích:** Khớp nối trực tiếp trong Spine 2D, Live2D, DragonBones hoặc Rust Engine cho chuyển động 120 FPS.

---

## 🎨 BẢNG MÃ MÀU CHUẨN (PALETTE HOÀNG LONG)
- **Vảy vàng hoàng kim (Chính):** `#ffd700`, `#f59e0b`, `#d97706`
- **Ánh kim vương giả / Bụng / Giáp ngực:** `#fef08a`, `#fde047`, `#ffffff`
- **Bờm lửa chu sa (Mane):** `#ef4444`, `#dc2626`, `#f97316`
- **Sừng ngọc bạch kim / Móng vuốt:** `#fef3c7`, `#ffffff`, `#b45309`
- **Viền nét Pixel Outline:** `#451a03` (Nâu thẫm đế vương)

---

## 📂 DANH SÁCH 12 TỆP ASSET ĐỘC LẬP & PROMPT CHI TIẾT

```
assets/dragons/parts/hoang_long/
├── 01_head_base.png          # Hộp sọ đầu rồng vàng
├── 02_jaw_lower.png          # Hàm dưới cử động
├── 03_eyes_open.png          # Mắt rồng hồng ngọc đế vương
├── 04_eyes_blink.png         # Mắt nhắm thư thái
├── 05_antlers_pair.png       # Sừng rồng vương giả bạch kim
├── 06_whiskers_pair.png      # Cặp râu rồng vàng óng ả
├── 07_body_front.png         # Đốt thân ngực hoàng bào
├── 08_body_mid_segment.png   # Đốt thân giữa (nhân bản x8 đốt)
├── 09_flame_mane.png         # Bờm lửa chu sa đỏ cam
├── 10_claws_front_back.png   # Bàn chân ngũ trảo đế vương (5 móng)
├── 11_tail_flame.png         # Đuôi bốc lửa chu sa
└── 12_auspicious_cloud_vfx.png # Mây tường vân ngũ sắc phong thủy
```

---

### TỆP 01: `01_head_base.png` (Hộp Sọ Đầu Rồng Vàng)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Đáy giữa sọ `[50%, 90%]`
- **Z-Order Layer:** Layer 50
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Imperial Golden Oriental Dragon chibi head, upper skull with noble cute snout, glowing rich 24k gold scales (#ffd700) with warm orange shading, clean dark brown pixel outline, centered on pure transparent background, no eyes, no lower jaw, no horns, no neck, pure isolated skull asset --no background, eyes, jaw, horns, blur, 3d, realistic --ar 1:1
```

---

### TỆP 02: `02_jaw_lower.png` (Hàm Dưới Cử Động)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp hàm sau `[50%, 20%]`
- **Z-Order Layer:** Layer 45
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Imperial Golden Dragon chibi lower jaw, open mouth interior with soft ruby red tongue, tiny ivory white fangs, gold chin, crisp pixel lines, centered on pure transparent background, modular piece for puppet rigging --no background, upper head, eyes, horns, blur --ar 1:1
```

---

### TỆP 03: `03_eyes_open.png` (Mắt Hồng Ngọc Đế Vương)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Trung tâm mắt `[50%, 50%]`
- **Z-Order Layer:** Layer 55
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of cute majestic anime dragon eyes, glowing ruby red irises (#ef4444) with fiery inner sparks, sharp noble anime pupils, white star reflections, centered on pure transparent background, standalone facial feature asset --no face, no background, skin, blur --ar 1:1
```

---

### TỆP 04: `04_eyes_blink.png` (Mắt Nhắm Thư Thái)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Trung tâm mắt `[50%, 50%]`
- **Z-Order Layer:** Layer 55
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of closed happy blinking anime dragon eyes, curved serene arcs (^ ^), dark amber eyelashes, clean pixel art contours, centered on pure transparent background --no face, no background, open eyes, blur --ar 1:1
```

---

### TỆP 05: `05_antlers_pair.png` (Sừng Rồng Vương Giả Bạch Kim)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Chân gốc sừng `[50%, 95%]`
- **Z-Order Layer:** Layer 48
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, magnificent pair of imperial dragon horns, platinum jade crystal with golden tips, multi-branched deer antler silhouette, shining luster highlights (#ffffff), crisp pixel outline, centered on pure transparent background, standalone headpiece --no head, no background, blur, 3d --ar 1:1
```

---

### TỆP 06: `06_whiskers_pair.png` (Cặp Râu Rồng Vàng Óng Ả)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Chân gốc râu bên mõm `[50%, 10%]`
- **Z-Order Layer:** Layer 60
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of long undulating royal golden dragon whiskers, glowing golden strands (#fde047), serpentine curve, crisp pixel art styling, centered on pure transparent background, standalone facial filament piece --no head, no background, blur --ar 1:1
```

---

### TỆP 07: `07_body_front.png` (Đốt Thân Ngực Hoàng Bào)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp cầu đỉnh đốt `[50%, 20%]`
- **Z-Order Layer:** Layer 40
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Imperial Golden Dragon chest body segment, ball-and-socket modular piece, gleaming yellow-gold back scales (#ffd700), radiant pale-gold ventral plates (#fef08a), clean pixel shading, centered on pure transparent background, modular spine piece --no head, no limbs, no tail, no background --ar 1:1
```

---

### TỆP 08: `08_body_mid_segment.png` (Đốt Thân Giữa Nối Tiếp)
- **Kích thước khuyến nghị:** 192x192 px @ 100 DPI (Sử dụng nhân bản x8 đốt)
- **Tâm xoay (Pivot):** Tâm đốt cầu `[50%, 50%]`
- **Z-Order Layer:** Layer 35 ➔ 20
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, single modular body segment bead for Golden Dragon, perfectly symmetrical sphere joint with golden dragon scales and ribbed underbelly plate, centered on pure transparent background, standalone bone rig segment --no limbs, no head, no background, blur --ar 1:1
```

---

### TỆP 09: `09_flame_mane.png` (Bờm Lửa Chu Sa Đỏ Cam)
- **Kích thước khuyến nghị:** 192x192 px @ 100 DPI
- **Tâm xoay (Pivot):** Chân bờm gắn thân `[50%, 85%]`
- **Z-Order Layer:** Layer 42
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, tuft of blazing cinnabar red and orange dragon mane (#ef4444, #f97316), divine flame-shaped celestial fur tuft, billowing wind style, crisp pixel edges, centered on pure transparent background, standalone dorsal fin piece --no dragon body, no background, blur --ar 1:1
```

---

### TỆP 10: `10_claws_front_back.png` (Bàn Chân Ngũ Trảo Đế Vương)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp cổ chân `[50%, 15%]`
- **Z-Order Layer:** Layer 30 (Trước) & Layer 10 (Sau)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Imperial 5-clawed dragon paw (Ngũ Trảo Hoàng Kim), short stubby chibi golden scaled leg with 5 polished ivory talons, crisp pixel art contours, centered on pure transparent background, standalone limb joint --no body, no background, blur --ar 1:1
```

---

### TỆP 11: `11_tail_flame.png` (Đuôi Bốc Lửa Chu Sa)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Gốc nối đuôi `[15%, 50%]`
- **Z-Order Layer:** Layer 15
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, majestic flowing cinnabar fire tail plume for Golden Dragon, vivid crimson-orange fire plume (#ef4444, #f59e0b) with golden ember sparks, sweeping motion curve, centered on pure transparent background, standalone tail asset --no body, no background, blur --ar 1:1
```

---

### TỆP 12: `12_auspicious_cloud_vfx.png` (Mây Tường Vân Ngũ Sắc)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Tâm cụm mây `[50%, 50%]`
- **Z-Order Layer:** Layer 05 (Lớp nền mờ bay dưới chân)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, traditional oriental auspicious cloud swirl (Tường Vân), swirling stylized rainbow-pastel cloud puff (rose pink, pastel gold, soft cyan), spiritual mist, clean pixel art outline, centered on pure transparent background, standalone floating VFX prop --no dragon, no background, blur --ar 1:1
```

---

## ⚙️ HƯỚNG DẪN LẮP RÁP RIGGING 120 FPS
- Cấu trúc khớp tương đồng Thanh Long nhưng trang bị chuyển động bay bồng bềnh trên đám mây `12_auspicious_cloud_vfx.png`.
- Tốc độ dao động thân rồng Hoàng Long trang nghiêm, đầm hơn: tần số $f = 1.5\text{ Hz}$, biên độ $A = 10^\circ$, kết hợp đuôi lửa `11_tail_flame.png` co giãn co bóp nhẹ theo nhịp thở.
