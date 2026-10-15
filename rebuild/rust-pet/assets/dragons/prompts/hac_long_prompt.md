# BỘ PROMPT TẠO TỪNG TỆP ASSET PIXEL ART TÁCH KHỚP: HẮC LONG (SHADOW DRAGON)

**Loài:** Hắc Long Phương Đông (U Minh Thâm Uyên Ma Long)  
**Chuẩn kỹ thuật chung:**  
- **Độ phân giải:** 100 DPI  
- **Nền:** Trong suốt hoàn toàn (Transparent Alpha RGBA - Tuyệt đối không có nền đen/trắng)  
- **Phong cách:** 16-bit / 32-bit Chibi Pixel Art huyền bí, vảy đen bóng Obsidian phát ánh tím U Minh, viền sắc nét.  
- **Định dạng xuất:** Mỗi câu Prompt dưới đây dùng để sinh ra **CHÍNH XÁC 1 TỆP ẢNH PNG ĐỘC LẬP**.  
- **Mục đích:** Ghép xương modular trong Spine 2D, Live2D, DragonBones hoặc Rust Engine cho chuyển động 120 FPS.

---

## 🎨 BẢNG MÃ MÀU CHUẨN (PALETTE HẮC LONG)
- **Vảy đen Obsidian (Chính):** `#09090b`, `#18181b`, `#27272a`
- **Giáp bụng / Mảng bóng xám chì:** `#3f3f46`, `#52525b`, `#71717a`
- **Bờm ma khí & Tia lôi điện (Void Glow):** `#a855f7`, `#c084fc`, `#e9d5ff`
- **Sừng sấm sét & Móng vuốt:** `#1e1b4b`, `#6366f1`, `#e0e7ff`
- **Viền nét Pixel Outline:** `#020617` (Đen huyền bí)

---

## 📂 DANH SÁCH 12 TỆP ASSET ĐỘC LẬP & PROMPT CHI TIẾT

```
assets/dragons/parts/hac_long/
├── 01_head_base.png          # Hộp sọ đầu rồng đen obsidian
├── 02_jaw_lower.png          # Hàm dưới cử động
├── 03_eyes_open.png          # Mắt tím U Minh ma mị
├── 04_eyes_blink.png         # Mắt nhắm lạnh lùng
├── 05_horns_pair.png         # Cặp sừng hắc lôi nhọn hoắt
├── 06_whiskers_pair.png      # Cặp râu rồng khói đen tím
├── 07_body_front.png         # Đốt thân ngực ma giáp
├── 08_body_mid_segment.png   # Đốt thân giữa (nhân bản x8 đốt)
├── 09_shadow_mane.png        # Bờm khói tím dạ quang
├── 10_claws_front_back.png   # Bàn chân móng vuốt hắc kim
├── 11_tail_flame.png         # Đuôi khói u minh lượn sóng
└── 12_void_lightning_vfx.png # Tia sét tím U Lôi ma pháp
```

---

### TỆP 01: `01_head_base.png` (Hộp Sọ Đầu Rồng Đen Obsidian)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Đáy giữa sọ `[50%, 90%]`
- **Z-Order Layer:** Layer 50
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Abyssal Shadow Oriental Dragon chibi head, upper skull with cool fierce snout, sleek glossy black obsidian scales (#18181b) with subtle purple edge highlights, clean deep black pixel outline, centered on pure transparent background, no eyes, no lower jaw, no horns, no neck, pure isolated skull asset --no background, eyes, jaw, horns, blur, 3d, realistic --ar 1:1
```

---

### TỆP 02: `02_jaw_lower.png` (Hàm Dưới Cử Động)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp hàm sau `[50%, 20%]`
- **Z-Order Layer:** Layer 45
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Abyssal Shadow Dragon chibi lower jaw, open mouth interior with dark plum purple tongue, sharp ivory fangs, obsidian black chin, clean pixel contours, centered on pure transparent background, modular puppet piece --no background, upper head, eyes, horns, blur --ar 1:1
```

---

### TỆP 03: `03_eyes_open.png` (Mắt Tím U Minh Ma Mị)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Trung tâm mắt `[50%, 50%]`
- **Z-Order Layer:** Layer 55
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of glowing abyssal void dragon eyes, luminous electric violet irises (#c084fc), slit slit-like anime pupils, fierce cute expression with bright purple magical glare, centered on pure transparent background, standalone facial asset --no face, no skin, no background, blur --ar 1:1
```

---

### TỆP 04: `04_eyes_blink.png` (Mắt Nhắm Lạnh Lùng)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Trung tâm mắt `[50%, 50%]`
- **Z-Order Layer:** Layer 55
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of closed cool anime dragon eyes, calm curved arcs, dark violet eyelashes, crisp pixel art styling, centered on pure transparent background --no face, no background, open eyes, blur --ar 1:1
```

---

### TỆP 05: `05_horns_pair.png` (Cặp Sừng Hắc Lôi Nhọn Hoắt)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Chân gốc sừng `[50%, 95%]`
- **Z-Order Layer:** Layer 48
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of sharp jagged abyssal dragon horns, jet black crystal texture with glowing purple lightning rune veins (#a855f7), fierce silhouette, crisp pixel outline, centered on pure transparent background, standalone headpiece --no head, no background, blur, 3d --ar 1:1
```

---

### TỆP 06: `06_whiskers_pair.png` (Cặp Râu Khói Đen Tím)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Chân gốc râu bên mõm `[50%, 10%]`
- **Z-Order Layer:** Layer 60
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of flowing shadow dragon whiskers, ethereal smoky dark violet tendrils (#a855f7), mystic wavy curve, crisp pixel art styling, centered on pure transparent background, standalone facial asset --no head, no background, blur --ar 1:1
```

---

### TỆP 07: `07_body_front.png` (Đốt Thân Ngực Ma Giáp)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp cầu đỉnh đốt `[50%, 20%]`
- **Z-Order Layer:** Layer 40
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Shadow Dragon upper chest body segment, ball-and-socket modular piece, polished obsidian back scales (#18181b), dark charcoal underbelly armor plates (#3f3f46), purple rim light, centered on pure transparent background, modular spine piece --no head, no limbs, no tail, no background --ar 1:1
```

---

### TỆP 08: `08_body_mid_segment.png` (Đốt Thân Giữa Nối Tiếp)
- **Kích thước khuyến nghị:** 192x192 px @ 100 DPI (Sử dụng nhân bản x8 đốt)
- **Tâm xoay (Pivot):** Tâm đốt cầu `[50%, 50%]`
- **Z-Order Layer:** Layer 35 ➔ 20
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, single modular body segment bead for Shadow Dragon, spherical socket joint with midnight black scales and armored dark grey belly plate, clean pixel shading, centered on pure transparent background, standalone bone rig segment --no limbs, no head, no background, blur --ar 1:1
```

---

### TỆP 09: `09_shadow_mane.png` (Bờm Khói Tím Dạ Quang)
- **Kích thước khuyến nghị:** 192x192 px @ 100 DPI
- **Tâm xoay (Pivot):** Chân bờm gắn thân `[50%, 85%]`
- **Z-Order Layer:** Layer 42
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, tuft of ethereal shadow flame mane, dark violet and magenta smoky fur crest (#a855f7, #c084fc), ghost flame silhouette, crisp pixel edges, centered on pure transparent background, standalone dorsal fin piece --no dragon body, no background, blur --ar 1:1
```

---

### TỆP 10: `10_claws_front_back.png` (Bàn Chân Móng Vuốt Hắc Kim)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp cổ chân `[50%, 15%]`
- **Z-Order Layer:** Layer 30 (Trước) & Layer 10 (Sau)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, cute chibi shadow dragon paw, black scaled stubby foot with 4 razor-sharp silver talons, clean pixel art contour, centered on pure transparent background, standalone limb joint --no body, no background, blur --ar 1:1
```

---

### TỆP 11: `11_tail_flame.png` (Đuôi Khói U Minh Lượn Sóng)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Gốc nối đuôi `[15%, 50%]`
- **Z-Order Layer:** Layer 15
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, dark phantom flame tail tuft for Shadow Dragon, billowing violet-black ghost smoke plume (#a855f7, #18181b) with floating spark particles, crisp pixel styling, centered on pure transparent background, standalone tail asset --no body, no background, blur --ar 1:1
```

---

### TỆP 12: `12_void_lightning_vfx.png` (Tia Sét Tím U Lôi Ma Pháp)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Tâm phát xạ `[50%, 50%]`
- **Z-Order Layer:** Layer 70 (Phía trước)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, jagged dark purple electric lightning bolt arcs (U Lôi), glowing neon violet plasma discharge (#c084fc, #e9d5ff), crackling energy spark VFX, clean pixel contours, centered on pure transparent background, standalone magic effect --no dragon, no background, blur --ar 1:1
```

---

## ⚙️ HƯỚNG DẪN LẮP RÁP RIGGING 120 FPS
- Kết hợp chuỗi xương uốn lượn nhịp nhàng với hiệu ứng chớp tắt (alpha strobe) của tệp tia sét `12_void_lightning_vfx.png` tại 120 FPS để tạo cảm giác ma lôi tích tụ đầy uy lực.
