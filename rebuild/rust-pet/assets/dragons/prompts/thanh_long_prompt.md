# BỘ PROMPT TẠO TỪNG TỆP ASSET PIXEL ART TÁCH KHỚP: THANH LONG (AZURE DRAGON)

**Loài:** Thanh Long Phương Đông (Mộc Long Ngọc Bích Thần Thoại)  
**Chuẩn kỹ thuật chung:**  
- **Độ phân giải:** 100 DPI  
- **Nền:** Trong suốt hoàn toàn (Transparent Alpha RGBA - Không nền trắng/đen)  
- **Phong cách:** 16-bit / 32-bit Chibi Pixel Art đỉnh cao, viền pixel sắc nét (Crisp outline), không nhòe khử răng cưa (No anti-aliasing blur).  
- **Định dạng xuất:** Mỗi câu Prompt dưới đây dùng để sinh ra **CHÍNH XÁC 1 TỆP ẢNH PNG ĐỘC LẬP**.  
- **Mục đích:** Nhập trực tiếp vào Spine 2D, Live2D, DragonBones hoặc Rust Engine (Bevy/Macroquad) để làm diễn hoạt 120 FPS uốn lượn mượt mà.

---

## 🎨 BẢNG MÃ MÀU CHUẨN (PALETTE THANH LONG)
- **Vảy ngọc lục bảo (Chính):** `#00e5a3`, `#00b87a`, `#008f5d`
- **Mảng sáng / Bụng / Highlight:** `#a7f3d0`, `#6ee7b7`, `#ecfdf5`
- **Bờm tóc & Khí mộc:** `#00b4d8`, `#0077b6`, `#90e0ef`
- **Sừng hươu & Móng vuốt:** `#fbbf24`, `#f59e0b`, `#b45309`
- **Viền nét Pixel Outline:** `#062820` (Xanh đen thẫm)

---

## 📂 DANH SÁCH 12 TỆP ASSET ĐỘC LẬP & PROMPT CHI TIẾT

```
assets/dragons/parts/thanh_long/
├── 01_head_base.png         # Hộp sọ đầu rồng
├── 02_jaw_lower.png         # Hàm dưới cử động
├── 03_eyes_open.png         # Cặp mắt mở lấp lánh
├── 04_eyes_blink.png        # Cặp mắt nhắm dễ thương
├── 05_antlers_pair.png      # Cặp sừng hươu hoàng kim
├── 06_whiskers_pair.png     # Cặp râu rồng uốn lượn
├── 07_body_front.png        # Đốt thân ngực trước
├── 08_body_mid_segment.png  # Đốt thân giữa (nhân bản x8 đốt)
├── 09_dorsal_mane.png       # Bờm lông lưng ngọc bích
├── 10_claws_front_back.png  # Bàn chân 4 móng vuốt
├── 11_tail_fan.png          # Đuôi lông xòe mộc linh
└── 12_celestial_orb_vfx.png # Dạ Minh Châu thần khí
```

---

### TỆP 01: `01_head_base.png` (Hộp Sọ Đầu Rồng)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Đáy giữa sọ `[50%, 90%]`
- **Z-Order Layer:** Layer 50
- **Prompt AI (Copy vào Midjourney / SDXL / ComfyUI / DALL-E):**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Oriental Azure Dragon chibi head, upper skull with cute snout and nose, vibrant emerald green jade scales (#00e5a3), gentle chubby cheeks, clean dark green pixel outline, centered on transparent background, no eyes, no lower jaw, no antlers, no neck, pure isolated skull asset --no background, eyes, jaw, horns, blur, 3d, realistic --ar 1:1
```

---

### TỆP 02: `02_jaw_lower.png` (Hàm Dưới Cử Động)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp hàm sau `[50%, 20%]`
- **Z-Order Layer:** Layer 45
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Oriental Azure Dragon chibi lower jaw, open mouth interior with soft pink tongue, tiny cute white fang teeth, jade green chin, crisp pixel contours, centered on pure transparent background, isolated piece for puppet rigging --no background, upper head, eyes, horns, blur --ar 1:1
```

---

### TỆP 03: `03_eyes_open.png` (Cặp Mắt Anime Mở Lấp Lánh)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Trung tâm mắt `[50%, 50%]`
- **Z-Order Layer:** Layer 55
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of cute anime dragon eyes, glowing amber gold irises (#fbbf24), large pupils with sparkling white light reflections, friendly desktop pet expression, centered on pure transparent background, standalone facial asset --no face, no skin, no background, blur, realistic --ar 1:1
```

---

### TỆP 04: `04_eyes_blink.png` (Cặp Mắt Nhắm Dễ Thương)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Trung tâm mắt `[50%, 50%]`
- **Z-Order Layer:** Layer 55
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of closed blinking cute chibi anime dragon eyes, curved happy arc lines (^ ^), dark emerald eyelashes, clean pixel art lines, centered on pure transparent background --no face, no background, open eyes, blur --ar 1:1
```

---

### TỆP 05: `05_antlers_pair.png` (Cặp Sừng Hươu Hoàng Kim)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Chân gốc sừng `[50%, 95%]`
- **Z-Order Layer:** Layer 48
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, majestic pair of golden deer antlers for Oriental dragon, branch-shaped mythical horns, polished shining gold (#fbbf24) with warm amber shading, crisp pixel edges, centered on pure transparent background, standalone headgear asset --no head, no face, no background, 3d render, blur --ar 1:1
```

---

### TỆP 06: `06_whiskers_pair.png` (Cặp Râu Rồng Uốn Lượn)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Chân gốc râu bên mõm `[50%, 10%]`
- **Z-Order Layer:** Layer 60
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, pair of long flowing mythical oriental dragon whiskers, soft curved wavy mustache filaments, bright turquoise cyan gradient (#00b4d8), dynamic fluid curve, crisp pixel art outline, centered on pure transparent background --no head, no background, blur, realistic --ar 1:1
```

---

### TỆP 07: `07_body_front.png` (Đốt Thân Ngực Trước)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp cầu đỉnh đốt `[50%, 20%]`
- **Z-Order Layer:** Layer 40
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, Oriental Azure Dragon upper chest body segment, ball-and-socket modular sphere, jade scales on back (#00e5a3) and soft mint cream belly plates (#a7f3d0), clean pixel shading, centered on pure transparent background, modular spine piece --no head, no limbs, no tail, no background --ar 1:1
```

---

### TỆP 08: `08_body_mid_segment.png` (Đốt Thân Giữa Nối Tiếp)
- **Kích thước khuyến nghị:** 192x192 px @ 100 DPI (Sử dụng nhân bản cho 8-10 đốt xương)
- **Tâm xoay (Pivot):** Tâm đốt cầu `[50%, 50%]`
- **Z-Order Layer:** Layer 35 ➔ 20
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, single modular body segment bead for Oriental snake-like dragon, round overlapping jade dragon scales (#00e5a3), curved underbelly scute plate (#6ee7b7), perfectly symmetrical socket joint, centered on pure transparent background, standalone bone rig segment --no background, limbs, head, tail, blur --ar 1:1
```

---

### TỆP 09: `09_dorsal_mane.png` (Bờm Lông Lưng Ngọc Bích)
- **Kích thước khuyến nghị:** 192x192 px @ 100 DPI
- **Tâm xoay (Pivot):** Chân bờm gắn thân `[50%, 85%]`
- **Z-Order Layer:** Layer 42
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, tuft of flowing celestial dragon mane, wavy turquoise cyan fur crest (#00b4d8), fluffy anime wind-blown hair chunk, crisp pixel art styling, centered on pure transparent background, standalone spine fin asset --no body, no head, no background, blur --ar 1:1
```

---

### TỆP 10: `10_claws_front_back.png` (Bàn Chân & Móng Vuốt)
- **Kích thước khuyến nghị:** 128x128 px @ 100 DPI
- **Tâm xoay (Pivot):** Khớp cổ chân `[50%, 15%]`
- **Z-Order Layer:** Layer 30 (Chân trước) & Layer 10 (Chân sau)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, cute chibi oriental dragon foot paw with 4 sharp golden eagle talons/claws (#fbbf24), emerald scaled ankle, crisp pixel outlines, centered on pure transparent background, standalone limb joint asset --no body, no background, blur, realistic --ar 1:1
```

---

### TỆP 11: `11_tail_fan.png` (Chùm Lông Đuôi Thần Thoại)
- **Kích thước khuyến nghị:** 256x256 px @ 100 DPI
- **Tâm xoay (Pivot):** Gốc nối đuôi `[15%, 50%]`
- **Z-Order Layer:** Layer 15
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, magical flowing tail tuft for Oriental dragon, fan-shaped flame-like turquoise mane feather plume (#00b4d8) with emerald highlights, wind motion sweep, crisp pixel edges, centered on pure transparent background, standalone tail end asset --no body, no background, blur, 3d --ar 1:1
```

---

### TỆP 12: `12_celestial_orb_vfx.png` (Dạ Minh Châu Thần Khí)
- **Kích thước khuyến nghị:** 192x192 px @ 100 DPI
- **Tâm xoay (Pivot):** Tâm viên ngọc `[50%, 50%]`
- **Z-Order Layer:** Layer 70 (Phía trước nhất)
- **Prompt AI:**
```text
masterpiece, best quality, single isolated 2D game asset, 16-bit pixel art, 100 dpi, glowing celestial dragon pearl (Dạ Minh Châu), luminous cyan orb (#67e8f9) radiating soft magical halo aura, ethereal spiraling energy wisps, crystal highlight sparkles, centered on pure transparent background, standalone prop item --no dragon, no hands, no background, blur --ar 1:1
```

---

## ⚙️ HƯỚNG DẪN LẮP RÁP RIGGING 120 FPS
1. **Chuỗi xương phân tầng (Bone Hierarchy):**
   - `ROOT_ORIGIN` ➔ `SPINE_01` (ngực `07_body_front.png`)
   - `SPINE_01` ➔ `SPINE_02` ... ➔ `SPINE_10` (`08_body_mid_segment.png` nhân bản x8) ➔ `TAIL_BONE` (`11_tail_fan.png`)
   - `SPINE_01` ➔ `NECK_BONE` ➔ `HEAD_BONE` (`01_head_base.png`)
   - `HEAD_BONE` chứa các con: `JAW` (`02`), `EYES` (`03`/`04`), `HORNS` (`05`), `WHISKERS` (`06`).
2. **Dao động hàm Sin uốn lượn 120 FPS:**
   - Mỗi khớp xương lệch góc: $\Delta \theta_k = A \cdot \sin(2\pi f \cdot t - k \cdot \phi)$ với biên độ $A = 12^\circ$, tần số $f = 2.0\text{ Hz}$, độ lệch pha $\phi = 0.35\text{ rad}$.
   - Tốc độ tick 120 FPS bảo đảm không hề có giật lag (stutter) giữa các mấu nối hình cầu.
