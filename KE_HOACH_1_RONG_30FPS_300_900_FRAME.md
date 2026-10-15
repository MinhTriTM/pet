# KẾ HOẠCH SẢN XUẤT 1 RỒNG PIXEL ART 2D — 30 FPS, 300–900 FRAME

## 0. Phạm vi và nguồn
- **Nguồn dự án:** 5 bản prompt phân tách asset của Thanh Long, Hoàng Long, Hắc Long, Hỏa Long, Băng Long; và quy chuẩn xoay 8 hướng, micro-motion, xương khớp.
- **Phần được đề xuất mới:** số biểu cảm, clip, ba cấp ngân sách frame, biến thể skin, cấu trúc trạng thái, kiểm thử và định dạng manifest.
- **Mỗi loài hiện có danh mục 12 loại PNG** trong tài liệu, chưa đồng nghĩa đã có bộ hoàn chỉnh để rig; cần kiểm toán asset thực tế và phân tách thêm các thành phần bị gộp.

## 1. Quy đổi frame và chiến lược kỹ thuật
- FPS biên soạn: **30 khung hình/giây**. Mỗi khung tương ứng 33,333 ms.
- Ngân sách 300 / 600 / 900 frame = 10 / 20 / 30 giây **tổng thời lượng gốc cộng các clip**; có thể tái sử dụng loop vô hạn.
- Có 8 hướng hiển thị: 0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°; dựng bộ ảnh gốc cho 5 hướng rồi lật gương 3 hướng nếu giải phẫu/đổ bóng đối xứng. Góc xoay 2D ở đây là **8 hướng rời rạc**, không phải true 3D turnaround liên tục.
- Lưu rig/bones và keyframe để diễn hoạt runtime, không bắt buộc vẽ từng frame. Nếu *bake* 30 FPS: 300/600/900 frame mỗi hướng. Nếu xuất 5 hướng gốc: 1.500/3.000/4.500 ảnh frame; đủ 8 góc độc lập thì 2.400/4.800/7.200 ảnh (chưa tính skin, tách VFX, biến thể biểu cảm).
- Mục tiêu engine 60/120 FPS có thể render nội suy chuyển động 30 FPS, không đảm bảo chạy 120 FPS trên mọi phần cứng. Nearest-neighbor / pixel snapping với hướng camera, hiệu ứng khớp méo phải kiểm thử trực quan.

## 2. Bộ 16 trạng thái biểu cảm (parameterized, không phải 16 full sprites)
| ID | Biểu cảm | Mắt/mí/đồng tử | Miệng/hàm | Cơ thể phụ trợ |
|---|---|---|---|---|
| E00 | Bình thường | Mở trung tính, nhìn mục tiêu | Khép | Thở |
| E01 | Vui vẻ | Cười, cong mí | Cười nhẹ | Đuôi vẫy |
| E02 | Phấn khích | Mở to, đồng tử sáng | Cười rộng | Nhún thân |
| E03 | Tò mò | Nhìn lệch, một mí cao | Hơi hé | Nghiêng đầu |
| E04 | Ngạc nhiên | Mở tròn | Há nhanh | Ngửa đầu |
| E05 | Tức giận | Nheo, lông mày ép | Nhe răng | Hạ trọng tâm |
| E06 | Cuồng nộ | Mắt sáng, nhìn khóa | Hàm gầm | VFX nguyên tố |
| E07 | Buồn bã | Mí trễ, nhìn xuống | Khép méo | Cúi cổ |
| E08 | Đau đớn | Nhắm siết | Nghiến răng | Co thân |
| E09 | Sợ hãi | Mở lớn, con ngươi nhỏ | Run hé | Lùi đuôi |
| E10 | Buồn ngủ | Mí nửa khép | Ngáp | Chậm nhịp |
| E11 | Ngủ say | Mí đóng | Khép | Nhịp thở sâu |
| E12 | Ngượng ngùng | Đảo mắt, chớp | Cười mím | Quay đầu |
| E13 | Tinh nghịch | Một mắt nheo | Cười lệch | Ve đuôi |
| E14 | Kiêu hãnh | Nhìn ngang / híp | Cười tự tin | Ưỡn ngực |
| E15 | Kiệt sức | Mí trễ, nhìn mờ | Thở gấp | Hạ đầu |

Để không nhân đôi asset vô ích, dùng nhóm slot: mắt trái/phải (mở, nửa khép, nhắm, nheo); đồng tử trái/phải (các vị trí nội suy); lông mày trái/phải (bình thường, nâng, hạ); miệng/hàm (khép, hé, cười, nhe răng, mở gầm, ngáp); VFX má/họng có thể bật/tắt. 16 trạng thái được ghép từ slot và tham số, không cần 16 bộ 8 hướng vẽ nguyên con.

## 3. 3 biến thể ngoại hình (skins dùng chung rig)
1. **Classic:** đúng màu sắc/giải phẫu gốc từng loài; là bản mặc định.
2. **Awakened:** vảy sáng, rìa phát quang, mắt và nguyên tố cường hóa; chỉ đổi texture/VFX/đôi khi lớp giáp, giữ xương và collision.
3. **Battle-worn:** vết nứt/vảy sứt, dấu chiến đấu, mắt mệt; cần kiểm tra không che mắt hoặc làm hỏng outline pixel.

Skin = ngoại hình; emotion = cảm xúc; clip = động tác; direction = hướng; chúng có thể tổ hợp **theo điều kiện tương thích**. 16×37×8×3 = **14.208 tổ hợp lý thuyết**, KHÔNG đồng nghĩa cần sản xuất 14.208 tệp ảnh hay mọi tổ hợp đều hợp lệ.

## 4. Danh sách clip và ngân sách chính xác
Các frame `F000…` tính theo phạm vi **riêng từng giai đoạn**; 3 giai đoạn nối tiếp nhau về tổng ngân sách nhưng clip chạy độc lập, không phải một cutscene liên tục.

### Giai đoạn 1 — Cấp 300: vận động cơ bản

| Clip | Frame | Giây | Loop | Bộ phận chính |
|---|---:|---:|---|---|
| `IdleBreath` — Thở nhẹ khi đứng yên | 60 | 2.00 | Có | Thân, hàm, bụng, đuôi |
| `Blink` — Chớp mắt | 12 | 0.40 | Không | Mí mắt trái/phải |
| `LookAround` — Quan sát xung quanh | 24 | 0.80 | Không | Mắt, đồng tử, cổ |
| `HeadTilt` — Nghiêng đầu | 18 | 0.60 | Không | Đầu, sừng, râu |
| `TailSway` — Ve vẩy đuôi | 24 | 0.80 | Có | Các đốt đuôi |
| `Walk` — Đi bộ | 24 | 0.80 | Có | Chân, thân, hông |
| `Run` — Chạy | 18 | 0.60 | Có | Chân, thân, hông |
| `Turn45` — Đổi hướng 45 độ | 18 | 0.60 | Không | Swap hướng sprite, xoay đầu |
| `Turn90` — Đổi hướng 90 độ | 24 | 0.80 | Không | Swap hướng sprite, cập nhật che khuất |
| `AirMove` — Bay lượn / lơ lửng | 24 | 0.80 | Có | Đập cánh (Tây) / uốn thân (Đông) |
| `Takeoff` — Cất cánh | 30 | 1.00 | Không | Chân, thân, cánh hoặc thân dài |
| `Landing` — Hạ cánh | 24 | 0.80 | Không | Giảm độ cao, chân, đuôi |

**Tổng GĐ1: 300 frame = 10 giây.**

### Giai đoạn 2 — Nâng lên 600: cảm xúc và chiến đấu

| Clip | Frame | Giây | Loop | Bộ phận chính |
|---|---:|---:|---|---|
| `Happy` — Vui vẻ | 18 | 0.60 | Không | Mắt, miệng, đuôi |
| `Curious` — Tò mò | 18 | 0.60 | Không | Đầu, lông mày, con ngươi |
| `Surprised` — Ngạc nhiên | 12 | 0.40 | Không | Mắt mở, hàm |
| `Angry` — Tức giận | 18 | 0.60 | Không | Mắt, lông mày, sừng |
| `Sad` — Buồn bã | 18 | 0.60 | Không | Mắt, đầu, đuôi |
| `Drowsy` — Buồn ngủ | 24 | 0.80 | Không | Mí mắt, cổ |
| `Hurt` — Nhăn mặt đau | 12 | 0.40 | Không | Mắt, hàm |
| `Bite` — Cắn | 24 | 0.80 | Không | Hàm, đầu, cổ |
| `ClawAttack` — Cào | 24 | 0.80 | Không | Chân, cổ tay/móng |
| `Dodge` — Né đòn | 18 | 0.60 | Không | Thân, chân, đuôi |
| `Roar` — Gầm | 36 | 1.20 | Không | Hàm, cổ, ngực, VFX |
| `BreathCharge` — Tích tụ nguyên tố | 30 | 1.00 | Không | Họng, đầu, VFX |
| `BreathRelease` — Phóng nguyên tố | 30 | 1.00 | Không | Hàm, đầu, VFX |
| `React` — Phản ứng khi tương tác | 18 | 0.60 | Không | Đầu, mắt, đuôi |

**Tổng GĐ2: 300 frame = 10 giây.**

### Giai đoạn 3 — Nâng lên 900: sinh hoạt và tình huống mở rộng

| Clip | Frame | Giây | Loop | Bộ phận chính |
|---|---:|---:|---|---|
| `Victory` — Chiến thắng | 30 | 1.00 | Không | Thân, đầu, chân, cánh/bờm |
| `Playful` — Tinh nghịch | 24 | 0.80 | Không | Đầu, chân, đuôi |
| `Fear` — Sợ hãi | 18 | 0.60 | Không | Mắt, đuôi, tư thế |
| `SleepLoop` — Ngủ sâu | 36 | 1.20 | Có | Thở, mắt nhắm, co cơ |
| `WakeUp` — Thức dậy | 24 | 0.80 | Không | Mắt, đầu, chân |
| `Eat` — Ăn | 30 | 1.00 | Không | Hàm, cổ, lưỡi |
| `Grab` — Nhặt hoặc ôm vật | 24 | 0.80 | Không | Móng, cánh tay, đầu |
| `CastSpell` — Thi triển phép | 36 | 1.20 | Không | Tay/chân, đầu, VFX |
| `Knockback` — Bị đánh bật lùi | 18 | 0.60 | Không | Thân, chân, đầu |
| `Death` — Chết / gục xuống | 36 | 1.20 | Không | Toàn thân, VFX mờ dần |
| `Respawn` — Hồi sinh | 24 | 0.80 | Không | Toàn thân, hiệu ứng tái xuất hiện |

**Tổng GĐ3: 300 frame = 10 giây.**

## 5. Hệ xương và điều khiển vi mô
- `root`, `body_center`, `head`, `jaw` và neck chain; mắt trái/phải, pupil trái/phải, eyelid trái/phải, eyebrow trái/phải.
- **Rồng phương Đông:** `body_01..10` (dây xương có distance constraint), 4 chi/chân, râu trái/phải mỗi bên 3–5 khớp, bờm chia 4–8 cụm, sừng trái/phải, chóp đuôi, Long Châu/VFX.
- **Rồng phương Tây:** torso, neck 2–3 đốt, tail 4–8 đốt, mỗi cánh vai/khuỷu/cổ tay/3 nan, các lưới màng cánh, 4 chân, móng, sừng trái/phải, VFX hơi thở.
- Gợi ý thiết kế **khoảng 40–80 bones** và **30–70 PNG/slots độc lập** cho 1 con tùy loài, chi tiết và phương pháp vẽ. Đây là **ước lượng sản xuất**, không phải số trích từ tài liệu gốc.
- Khớp pivot tại đầu/hàm/cánh/chân/đuôi phải hiệu chỉnh theo tọa độ **sau khi crop, scale**; pivot % trong prompt là tham chiếu ban đầu, không tự khớp khi import.
- Layer Z cần đổi theo góc nhìn trước/sau, không chỉ dùng một thứ tự cố định cho tất cả 8 hướng. Hệ thống pixel snapped phải giữ outline ổn định khi biến dạng và quay.

## 6. Animation state machine (ưu tiên và quy tắc)
```text
ROOT_STATE
├─ Locomotion (Idle / Walk / Run / AirMove / Takeoff / Landing / Turn)
├─ UpperBody (Look / HeadTilt / Bite / Claw / Roar / CastSpell)
├─ FaceOverlay (E00..E15 / Blink / LookAt)
├─ Secondary (Tail / Mane / Whiskers / HornInertia / WingMembrane)
└─ VFX (BreathCharge / BreathRelease / Aura / Orb)
```
- `Death` chiếm ưu tiên cao nhất: khóa vận động, không được đồng thời ngủ/chạy/chiến đấu.
- `SleepLoop` không được kích hoạt khi `Run`, `Takeoff`, `BreathRelease`.
- `Bite`, `Roar`, `BreathRelease` điều khiển hàm độc quyền; FaceOverlay chỉ điều khiển mắt/lông mày khi clip chiến đấu đang điều khiển hàm.
- `LookAt` chỉ áp dụng cho góc nhìn mà mắt được phép hiện và có vùng mask phù hợp; tránh đồng tử bay ra ngoài tròng khi nhìn lưng.
- Clip `Turn45`, `Turn90` phải cập nhật directional slot/culling, có thể kết hợp chuyển lớp occlusion và pose bù trừ.
- Fade / crossfade 2–6 frame cho chuyển trạng thái chính, có thể 0 frame cho động tác va đập/cắn cần dứt khoát.

## 7. File tree đề nghị
```text
assets/dragons/<species>/
  source_prompts/
  reference/                 # turnarounds, color/style sheet
  parts/master/              # sprite alpha đã QC, tên cố định
  parts/directions/{000,045,090,135,180}/
  skins/{classic,awakened,battle_worn}/
  rigs/skeleton.json
  rigs/pivots.json
  animations/phase_300/
  animations/phase_600/
  animations/phase_900/
  faces/emotions.json
  vfx/
  atlases/
  exports/spritesheets/
  manifests/animations_30fps.json
  tests/
```

## 8. Kế hoạch triển khai và cổng kiểm thử
**P0 — Thiết kế mẫu:** chọn một loài đại diện; chuẩn hóa góc mặt/đổ bóng/palette/độ lớn; 1 pose nguyên con cho 5 góc gốc.

**P1 — Kiểm toán ảnh:** phân lớp PNG thật, kiểm alpha, không bị cụt nét, không gộp xương/cánh vào thân; làm mẫu `idle` trước khi nhân chi tiết.

**P2 — Rig:** 1 hướng 90° để ráp, kiểm pivot, chiều dài nối, không lộ khe giữa các đốt; sau đó hoàn chỉnh hướng 0/45/135/180 và thử mirror.

**P3 — Gói 300 frame:** xuất 12 clip, test loop thở/đi/chạy/bay và các biến đổi hướng; không cần vẽ đầy đủ 300 ảnh thủ công nếu runtime rig.

**P4 — Gói 600 frame:** xuất 14 clip tăng cường, điều khiển 12–16 cảm xúc theo overlay, chiến đấu và VFX riêng; kiểm âm thanh và collision/hitbox nếu có.

**P5 — Gói 900 frame:** xuất 11 clip nâng cao và 3 skins; kiểm state machine, mọi góc, chế độ ngủ, hồi sinh và chuyển vùng.

**QA bắt buộc:** 5 góc gốc ghép thành 8 hướng; khi mirror không lật chữ/dấu bất đối xứng; alpha thật; không lộ nền; không hở khớp; nhịp loop không giật; thứ tự Z khi quay; không méo pixel; biểu cảm không xung đột hành động; memory atlas và VRAM được profiling ở kích thước game thật.

**Thành quả:** 16 biểu cảm hỗn hợp, 37 clip, 3 biến thể skin, 8 hướng, 900 frame ở 30 FPS cộng dồn; 5 góc quay nguồn và 3 góc mirror có điều kiện.
