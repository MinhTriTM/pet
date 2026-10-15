//! main.rs — Động Cơ Desktop Pets & 5 Loài Rồng Thần Thoại 120 FPS.
//! Hỗ trợ: Thanh Long, Hoàng Long, Hắc Long, Hỏa Long, Băng Long + 10 Hành vi tương tác.
mod pet;

use eframe::egui::{self, Color32, Pos2, Rect, Stroke, Vec2};
use pet::{DragonAction, Pet, PetSpec};
use std::collections::HashMap;

fn default_specs() -> Vec<PetSpec> {
    vec![
        // 1. Thanh Long Phương Đông
        PetSpec {
            id: "thanh-long".into(),
            name: "Thanh Long (Azure Dragon)".into(),
            size: (210.0, 160.0),
            speed_ms: 8,
            behaviors: vec!["all".into()],
            phrases: vec![
                "Hô phong hoán vũ, thiên hạ thái bình!".into(),
                "Thanh Long xuất thế, vạn mộc sinh sôi!".into(),
                "Long châu chiếu rọi cõi nhân gian!".into(),
            ],
            color: "#00e5a3".into(),
        },
        // 2. Hoàng Long Phương Đông
        PetSpec {
            id: "hoang-long".into(),
            name: "Hoàng Long (Golden Celestial Dragon)".into(),
            size: (210.0, 160.0),
            speed_ms: 8,
            behaviors: vec!["all".into()],
            phrases: vec![
                "Thần uy cái thế, hoàng kim vạn trượng!".into(),
                "Chân long giáng thế, nhật nguyệt quy tâm!".into(),
                "Mây lành ngũ sắc nâng bước ta đi!".into(),
            ],
            color: "#ffd700".into(),
        },
        // 3. Hắc Long Phương Đông
        PetSpec {
            id: "hac-long".into(),
            name: "Hắc Long (Abyssal Shadow Dragon)".into(),
            size: (210.0, 160.0),
            speed_ms: 8,
            behaviors: vec!["all".into()],
            phrases: vec![
                "U minh bóng tối, lôi đình giáng lâm!".into(),
                "Bóng đêm nuốt trọn ánh tà dương!".into(),
                "Gầm thét rách toạc hư không!".into(),
            ],
            color: "#8a2be2".into(),
        },
        // 4. Hỏa Long Phương Tây
        PetSpec {
            id: "hoa-long".into(),
            name: "Hỏa Long (Crimson Fire Drake)".into(),
            size: (210.0, 160.0),
            speed_ms: 8,
            behaviors: vec!["all".into()],
            phrases: vec![
                "Ngọn lửa vĩnh hằng thiêu rụi màn đêm!".into(),
                "Cánh lửa sải rộng rực sáng bầu trời!".into(),
                "ROOOAARRR! Biển lửa thức tỉnh!".into(),
            ],
            color: "#ff3b30".into(),
        },
        // 5. Băng Long Phương Tây
        PetSpec {
            id: "bang-long".into(),
            name: "Băng Long (Frost Wyvern)".into(),
            size: (210.0, 160.0),
            speed_ms: 8,
            behaviors: vec!["all".into()],
            phrases: vec![
                "Hơi thở hàn băng đóng băng vạn vật!".into(),
                "Bão tuyết bắc cực vâng lệnh ta!".into(),
                "Pha lê tuyết giá đẹp nhưng sắc lạnh!".into(),
            ],
            color: "#5ac8fa".into(),
        },
    ]
}

fn load_specs(want: &[String], all: bool) -> Vec<PetSpec> {
    let mut out = Vec::new();
    let dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("pets");
    if let Ok(rd) = std::fs::read_dir(&dir) {
        for e in rd.flatten() {
            if e.path().extension().map(|x| x == "toml").unwrap_or(false) {
                if let Ok(txt) = std::fs::read_to_string(e.path()) {
                    if let Ok(sp) = toml::from_str::<PetSpec>(&txt) {
                        if all || want.iter().any(|w| w == &sp.id) {
                            out.push(sp);
                        }
                    }
                }
            }
        }
    }
    if out.is_empty() {
        out = default_specs()
            .into_iter()
            .filter(|s| all || want.iter().any(|w| w == &s.id))
            .collect();
    }
    out
}

struct App {
    pets: Vec<Pet>,
    hidden: HashMap<String, bool>,
}

impl App {
    fn new(specs: Vec<PetSpec>, cc: &eframe::CreationContext<'_>) -> Self {
        let (sw, sh) = (
            cc.egui_ctx.screen_rect().width(),
            cc.egui_ctx.screen_rect().height(),
        );
        let pets = specs
            .into_iter()
            .map(|s| Pet::new(s, sw.max(800.0), sh.max(600.0)))
            .collect();
        Self {
            pets,
            hidden: HashMap::new(),
        }
    }
}

// =============================================================================
// ĐỒ HỌA VECTOR NGHỆ THUẬT: RỒNG PHƯƠNG ĐÔNG (Serpentine Dragon - 120 FPS)
// =============================================================================
fn draw_oriental_dragon(
    ui: &mut egui::Ui,
    w: f32,
    _h: f32,
    p: &Pet,
) {
    let painter = ui.painter();
    let tick = p.tick;
    let rgb = p.spec.parse_color();
    let primary_col = Color32::from_rgb(rgb.0, rgb.1, rgb.2);
    let secondary_col = match p.spec.id.as_str() {
        "hoang-long" => Color32::from_rgb(255, 69, 0),    // Bờm đỏ cam
        "hac-long" => Color32::from_rgb(75, 0, 130),      // Tím đậm
        _ => Color32::from_rgb(0, 180, 216),              // Xanh dương nhạt
    };

    // Xác định hướng nhìn 360 độ: Quay mặt sang trái (1.0) hoặc sang phải (-1.0)
    let flip_x = if p.facing_angle.cos() >= 0.0 { -1.0 } else { 1.0 };
    let base_x = if flip_x > 0.0 { 45.0 } else { w - 45.0 };
    let base_y = 65.0;

    // 0. Quỹ đạo Dạ Minh Châu 3D (Lớp phía sau: khi orb_z < 0 thì vẽ trước thân rồng)
    let orb_z = p.orb_orbit.sin();
    let orb_rx = 38.0;
    let orb_ry = 18.0;
    let orb_cx = base_x - flip_x * 20.0;
    let orb_cy = base_y + 15.0;
    let orb_x = orb_cx + p.orb_orbit.cos() * orb_rx * flip_x;
    let orb_y = orb_cy + orb_z * orb_ry;

    if orb_z < 0.0 {
        // Long Châu đang ở phía sau lưng rồng (Layer chìm Z-buffer)
        painter.circle_filled(Pos2::new(orb_x, orb_y), 6.5, Color32::from_rgba_premultiplied(255, 255, 200, 130));
        painter.circle_stroke(
            Pos2::new(orb_x, orb_y),
            9.0,
            Stroke::new(1.2, Color32::from_rgba_premultiplied(255, 215, 0, 90)),
        );
    }

    // 1. Thân Rồng uốn lượn 10 đốt động học (Follower Spine 360 độ)
    let n = 10;
    for i in (1..n).rev() {
        let frac = i as f32 / n as f32;
        let radius = (18.0 * (1.0 - frac * 0.45)).max(7.0);
        let wave = ((tick as f32 * 0.12 - i as f32 * 0.65).sin()) * 14.0;
        let seg_x = base_x + flip_x * (i as f32 * 14.0);
        let seg_y = base_y + wave;

        // Đốt thân
        painter.circle_filled(Pos2::new(seg_x, seg_y), radius, primary_col);
        painter.circle_stroke(
            Pos2::new(seg_x, seg_y),
            radius,
            Stroke::new(1.8, Color32::from_rgba_premultiplied(20, 20, 20, 180)),
        );

        // Vảy rồng lấp lánh ở 120 FPS
        if i % 2 == 0 {
            painter.circle_filled(
                Pos2::new(seg_x - flip_x * 2.0, seg_y - 2.0),
                radius * 0.45,
                secondary_col,
            );
        }

        // Bờm rồng / Vi cá dọc sống lưng uốn sóng mềm mại
        let fin_tip_y = seg_y - radius - 5.0 - ((tick as f32 * 0.15 + i as f32).cos().abs() * 4.0);
        painter.add(egui::Shape::line(
            vec![
                Pos2::new(seg_x - flip_x * 4.0, seg_y - radius + 2.0),
                Pos2::new(seg_x, fin_tip_y),
                Pos2::new(seg_x + flip_x * 4.0, seg_y - radius + 2.0),
            ],
            Stroke::new(2.0, secondary_col),
        ));
    }

    // Đuôi rồng (chùm lông đuôi thần thoại uốn sóng số 8)
    let tail_x = base_x + flip_x * (((n - 1) as f32 * 14.0) + 12.0);
    let tail_wave = ((tick as f32 * 0.12 - (n as f32) * 0.65).sin()) * 16.0;
    painter.add(egui::Shape::line(
        vec![
            Pos2::new(tail_x - flip_x * 12.0, base_y + tail_wave),
            Pos2::new(tail_x + flip_x * 10.0, base_y + tail_wave - 8.0),
            Pos2::new(tail_x + flip_x * 18.0, base_y + tail_wave),
            Pos2::new(tail_x + flip_x * 10.0, base_y + tail_wave + 8.0),
        ],
        Stroke::new(3.0, secondary_col),
    ));

    // 2. Đầu Rồng Uy Nghi (Xoay 360 độ theo hướng nhìn)
    let head_pos = Pos2::new(base_x, base_y);
    painter.circle_filled(head_pos, 22.0, primary_col);
    painter.circle_stroke(head_pos, 22.0, Stroke::new(2.5, Color32::BLACK));

    // Mõm rồng & Hàm dưới chuyển động mở/ngậm (Jaw Open 120 FPS)
    let snout_min_x = if flip_x > 0.0 { base_x - 28.0 } else { base_x + 4.0 };
    let snout_rect = Rect::from_min_size(Pos2::new(snout_min_x, base_y - 12.0), Vec2::new(24.0, 22.0));
    painter.rect_filled(snout_rect, 6.0, primary_col);
    painter.rect_stroke(snout_rect, 6.0, Stroke::new(2.0, Color32::BLACK), egui::StrokeKind::Inside);

    // Hàm dưới cử động há ra khi gầm thét / phun phép
    if p.jaw_open > 0.05 {
        let jaw_y = base_y + 4.0 + p.jaw_open * 7.0;
        let jaw_rect = Rect::from_min_size(Pos2::new(snout_min_x + 2.0, jaw_y), Vec2::new(20.0, 10.0));
        painter.rect_filled(jaw_rect, 3.0, primary_col);
        painter.rect_stroke(jaw_rect, 3.0, Stroke::new(1.5, Color32::BLACK), egui::StrokeKind::Inside);
        // Răng nanh trắng sắc bén
        let fang_x = snout_min_x + if flip_x > 0.0 { 4.0 } else { 16.0 };
        painter.circle_filled(Pos2::new(fang_x, jaw_y + 1.0), 2.0, Color32::WHITE);
    }

    // Mắt rồng thần uy: Chớp mắt vi mô (Blink) + Con ngươi đảo 360 độ theo chuột
    let eye_center_x = base_x - flip_x * 10.0;
    let eye_center_y = base_y - 8.0;
    let eye_col = match p.spec.id.as_str() {
        "hac-long" => Color32::from_rgb(255, 30, 80),
        "hoang-long" => Color32::from_rgb(0, 255, 200),
        _ => Color32::from_rgb(255, 230, 0),
    };

    if p.blink_state > 0.5 {
        // Mắt nhắm cười dễ thương (Cung arc)
        painter.add(egui::Shape::line(
            vec![
                Pos2::new(eye_center_x - 5.0, eye_center_y - 1.0),
                Pos2::new(eye_center_x, eye_center_y - 4.0),
                Pos2::new(eye_center_x + 5.0, eye_center_y - 1.0),
            ],
            Stroke::new(2.2, Color32::BLACK),
        ));
    } else {
        // Mắt mở to long lanh
        painter.circle_filled(Pos2::new(eye_center_x, eye_center_y), 6.0, eye_col);
        // Con ngươi đen đảo 360 độ dõi theo con trỏ chuột
        let pupil_x = eye_center_x + (p.eye_look.0 * flip_x).clamp(-3.2, 3.2);
        let pupil_y = eye_center_y + p.eye_look.1.clamp(-3.2, 3.2);
        painter.circle_filled(Pos2::new(pupil_x, pupil_y), 2.6, Color32::BLACK);
        // Đốm sáng phản chiếu sparkle
        painter.circle_filled(Pos2::new(pupil_x - 1.0, pupil_y - 1.0), 1.0, Color32::WHITE);
    }

    // Sừng Hươu Thần Thoại (Antler Horns)
    let horn_col = Color32::from_rgb(250, 240, 210);
    painter.add(egui::Shape::line(
        vec![
            Pos2::new(base_x + flip_x * 2.0, base_y - 18.0),
            Pos2::new(base_x + flip_x * 12.0, base_y - 36.0),
            Pos2::new(base_x + flip_x * 22.0, base_y - 48.0),
        ],
        Stroke::new(3.5, horn_col),
    ));
    painter.add(egui::Shape::line(
        vec![
            Pos2::new(base_x + flip_x * 12.0, base_y - 36.0),
            Pos2::new(base_x + flip_x * 4.0, base_y - 44.0),
        ],
        Stroke::new(2.5, horn_col),
    ));

    // Râu Rồng mềm mại 2 tầng uốn lượn trong gió (Soft-wave physics)
    let w_wave = p.whisker_wave;
    painter.add(egui::Shape::line(
        vec![
            Pos2::new(base_x - flip_x * 26.0, base_y + 4.0),
            Pos2::new(base_x - flip_x * 46.0, base_y + 12.0 + w_wave),
            Pos2::new(base_x - flip_x * 62.0, base_y + 8.0 - w_wave),
        ],
        Stroke::new(2.2, horn_col),
    ));
    // Sợi râu phụ thứ hai
    painter.add(egui::Shape::line(
        vec![
            Pos2::new(base_x - flip_x * 24.0, base_y + 10.0),
            Pos2::new(base_x - flip_x * 42.0, base_y + 20.0 - w_wave * 0.8),
            Pos2::new(base_x - flip_x * 56.0, base_y + 18.0 + w_wave * 0.6),
        ],
        Stroke::new(1.6, secondary_col),
    ));

    // 3. Dạ Minh Châu (Lớp phía trước khi z >= 0: Sáng rực rỡ đè lên thân)
    if orb_z >= 0.0 {
        painter.circle_filled(Pos2::new(orb_x, orb_y), 8.5, Color32::from_rgb(255, 255, 200));
        painter.circle_stroke(
            Pos2::new(orb_x, orb_y),
            12.0,
            Stroke::new(2.0, Color32::from_rgba_premultiplied(255, 215, 0, 180)),
        );
        // Hào quang tỏa sáng lấp lánh
        painter.circle_filled(Pos2::new(orb_x - 2.0, orb_y - 2.0), 3.0, Color32::WHITE);
    }

    // 4. Hiệu ứng kỹ năng (10 Actions Effects 120 FPS)
    match p.current_action {
        DragonAction::BreatheElement => {
            // Phun Lôi quang / Mộc khí / Hắc lôi theo hướng mõm
            let breath_w = 45.0 * p.breath_progress;
            let emit_x = base_x - flip_x * 30.0;
            let bolt = vec![
                Pos2::new(emit_x, base_y + 2.0),
                Pos2::new(emit_x - flip_x * (15.0 + breath_w), base_y - 6.0),
                Pos2::new(emit_x - flip_x * (25.0 + breath_w), base_y + 8.0),
                Pos2::new(emit_x - flip_x * (45.0 + breath_w * 1.5), base_y + 2.0),
            ];
            painter.add(egui::Shape::line(bolt, Stroke::new(4.5, eye_col)));
        }
        DragonAction::Roar => {
            // Sóng âm gầm thét lan tỏa 360 độ
            let r_size = (tick % 30) as f32 * 2.0;
            painter.circle_stroke(
                Pos2::new(base_x - flip_x * 28.0, base_y),
                r_size,
                Stroke::new(2.2, primary_col),
            );
        }
        DragonAction::SleepZzz => {
            painter.text(
                Pos2::new(base_x - 10.0, base_y - 32.0),
                egui::Align2::CENTER_CENTER,
                "Zzz...",
                egui::FontId::proportional(14.0),
                Color32::WHITE,
            );
        }
        _ => {}
    }
}

// =============================================================================
// ĐỒ HỌA VECTOR NGHỆ THUẬT: RỒNG PHƯƠNG TÂY (Winged Wyvern / Drake - 120 FPS)
// =============================================================================
fn draw_western_dragon(
    ui: &mut egui::Ui,
    w: f32,
    _h: f32,
    p: &Pet,
) {
    let painter = ui.painter();
    let tick = p.tick;
    let rgb = p.spec.parse_color();
    let skin_col = Color32::from_rgb(rgb.0, rgb.1, rgb.2);
    let wing_membrane = match p.spec.id.as_str() {
        "hoa-long" => Color32::from_rgb(255, 120, 50),
        _ => Color32::from_rgb(180, 230, 255), // Băng tuyết trong suốt
    };

    // Hướng nhìn 360 độ: flip_x (1.0 là sang trái, -1.0 là sang phải)
    let flip_x = if p.facing_angle.cos() >= 0.0 { -1.0 } else { 1.0 };
    let cx = if flip_x > 0.0 { 100.0 } else { w - 100.0 };
    let cy = 85.0;

    // 1. Thân rồng cơ bắp nở nang (Độ nghiêng 3D theo góc bay)
    let body_rect = Rect::from_center_size(Pos2::new(cx, cy), Vec2::new(56.0, 48.0));
    painter.rect_filled(body_rect, 16.0, skin_col);
    painter.rect_stroke(body_rect, 16.0, Stroke::new(2.5, Color32::BLACK), egui::StrokeKind::Inside);

    // Ức rồng (Chest scales)
    let chest_col = Color32::from_rgba_premultiplied(255, 240, 200, 220);
    painter.rect_filled(
        Rect::from_center_size(Pos2::new(cx - flip_x * 10.0, cy + 4.0), Vec2::new(24.0, 30.0)),
        8.0,
        chest_col,
    );

    // 2. Đôi Cánh Dơi Khổng Lồ (Phối cảnh Pseudo-3D Perspective 360 độ & vỗ 120 FPS)
    let wing_flap = p.wing_angle * 22.0;
    let wing_tip_y = cy - 45.0 + wing_flap;
    // Cánh gần (Foreground Wing) và Cánh xa (Background Wing) co giãn theo góc quay
    let wing_scale_far = 0.72; // Cánh phía xa thu nhỏ 28%

    // Cánh xa (Lớp nền sau lưng)
    let wing_far = vec![
        Pos2::new(cx + flip_x * 10.0, cy - 15.0),
        Pos2::new(cx + flip_x * (50.0 * wing_scale_far), wing_tip_y - 8.0),
        Pos2::new(cx + flip_x * (75.0 * wing_scale_far), wing_tip_y + 4.0),
        Pos2::new(cx + flip_x * (55.0 * wing_scale_far), cy - 2.0),
        Pos2::new(cx + flip_x * 30.0, cy + 5.0),
    ];
    painter.add(egui::Shape::convex_polygon(
        wing_far,
        Color32::from_rgba_premultiplied(wing_membrane.r(), wing_membrane.g(), wing_membrane.b(), 180),
        Stroke::new(2.0, skin_col),
    ));

    // Cánh gần (Lớp phía trước)
    let wing_near = vec![
        Pos2::new(cx - flip_x * 10.0, cy - 15.0),
        Pos2::new(cx - flip_x * 50.0, wing_tip_y - 12.0),
        Pos2::new(cx - flip_x * 75.0, wing_tip_y),
        Pos2::new(cx - flip_x * 55.0, cy - 5.0),
        Pos2::new(cx - flip_x * 30.0, cy + 5.0),
    ];
    painter.add(egui::Shape::convex_polygon(
        wing_near,
        wing_membrane,
        Stroke::new(2.5, skin_col),
    ));

    // 3. Đuôi rồng có gai nhọn (Spike Tail uốn lượn 120 FPS)
    let tail_swing = ((tick as f32 * 0.14).sin()) * 12.0;
    painter.add(egui::Shape::line(
        vec![
            Pos2::new(cx + flip_x * 25.0, cy + 10.0),
            Pos2::new(cx + flip_x * 55.0, cy + 18.0 + tail_swing),
            Pos2::new(cx + flip_x * 78.0, cy + 12.0 + tail_swing * 1.5),
        ],
        Stroke::new(4.0, skin_col),
    ));
    // Gai chóp đuôi / Lưỡi dao băng
    let spike = vec![
        Pos2::new(cx + flip_x * 76.0, cy + 6.0 + tail_swing * 1.5),
        Pos2::new(cx + flip_x * 92.0, cy + 12.0 + tail_swing * 1.5),
        Pos2::new(cx + flip_x * 76.0, cy + 18.0 + tail_swing * 1.5),
    ];
    painter.add(egui::Shape::convex_polygon(
        spike,
        Color32::from_rgb(40, 40, 40),
        Stroke::NONE,
    ));

    // 4. Đầu rồng hung hãn & Hàm dưới mở/ngậm (Jaw Open)
    let head_pos = Pos2::new(cx - flip_x * 35.0, cy - 15.0);
    painter.circle_filled(head_pos, 20.0, skin_col);
    painter.circle_stroke(head_pos, 20.0, Stroke::new(2.2, Color32::BLACK));

    // Hàm dưới cử động há to khi gầm hoặc khạc lửa/băng
    if p.jaw_open > 0.05 {
        let jaw_open_y = cy - 6.0 + p.jaw_open * 8.0;
        let jaw_rect = Rect::from_center_size(Pos2::new(cx - flip_x * 40.0, jaw_open_y), Vec2::new(18.0, 10.0));
        painter.rect_filled(jaw_rect, 3.0, skin_col);
        painter.rect_stroke(jaw_rect, 3.0, Stroke::new(1.5, Color32::BLACK), egui::StrokeKind::Inside);
        // Răng nanh sắc nhọn
        painter.circle_filled(Pos2::new(cx - flip_x * 45.0, jaw_open_y - 2.0), 2.0, Color32::WHITE);
    }

    // Sừng quỷ nhọn hoắt
    let horn_tip = Pos2::new(cx - flip_x * 24.0, cy - 42.0);
    painter.add(egui::Shape::line(
        vec![Pos2::new(cx - flip_x * 32.0, cy - 28.0), horn_tip],
        Stroke::new(4.0, Color32::from_rgb(45, 45, 55)),
    ));

    // Mắt rồng rực lửa / băng: Chớp mắt vi mô + con ngươi theo dõi chuột 360 độ
    let eye_center_x = cx - flip_x * 42.0;
    let eye_center_y = cy - 18.0;
    let eye_col = if p.spec.id == "hoa-long" {
        Color32::from_rgb(255, 220, 0)
    } else {
        Color32::from_rgb(255, 255, 255)
    };

    if p.blink_state > 0.5 {
        // Mắt nhắm
        painter.add(egui::Shape::line(
            vec![
                Pos2::new(eye_center_x - 4.0, eye_center_y),
                Pos2::new(eye_center_x + 4.0, eye_center_y),
            ],
            Stroke::new(2.0, Color32::BLACK),
        ));
    } else {
        painter.circle_filled(Pos2::new(eye_center_x, eye_center_y), 5.0, eye_col);
        // Con ngươi slit khe dọc đảo theo chuột
        let pupil_x = eye_center_x + (p.eye_look.0 * flip_x).clamp(-2.6, 2.6);
        let pupil_y = eye_center_y + p.eye_look.1.clamp(-2.6, 2.6);
        painter.rect_filled(
            Rect::from_center_size(Pos2::new(pupil_x, pupil_y), Vec2::new(2.2, 5.0)),
            1.0,
            Color32::BLACK,
        );
    }

    // 5. Hiệu ứng kỹ năng (10 Actions Effects)
    match p.current_action {
        DragonAction::BreatheElement => {
            // Hỏa Long phun bão lửa / Băng Long phun bão tuyết theo hướng đầu
            let flame_len = 65.0 * p.breath_progress;
            let (c1, c2) = if p.spec.id == "hoa-long" {
                (Color32::from_rgb(255, 60, 0), Color32::from_rgb(255, 200, 0))
            } else {
                (Color32::from_rgb(100, 210, 255), Color32::from_rgb(220, 245, 255))
            };

            for idx in 0..4 {
                let p_y = cy - 15.0 + ((idx as f32 - 1.5) * 8.0);
                painter.circle_filled(
                    Pos2::new(cx - flip_x * (55.0 + (idx as f32 * 12.0) + flame_len), p_y),
                    8.0 + (idx as f32 * 3.5),
                    if idx % 2 == 0 { c1 } else { c2 },
                );
            }
        }
        DragonAction::Roar => {
            // Chấn động gầm thét
            painter.text(
                Pos2::new(cx - flip_x * 55.0, cy - 35.0),
                egui::Align2::CENTER_CENTER,
                "🔥 ROAR!! 🔥",
                egui::FontId::monospace(14.0),
                Color32::from_rgb(255, 200, 50),
            );
        }
        DragonAction::SleepZzz => {
            painter.text(
                Pos2::new(cx - flip_x * 30.0, cy - 38.0),
                egui::Align2::CENTER_CENTER,
                "Zzz...",
                egui::FontId::proportional(14.0),
                Color32::WHITE,
            );
        }
        _ => {}
    }
}

// =============================================================================
// BÓNG THOẠI TRÒ CHUYỆN (Speech Bubble)
// =============================================================================
fn draw_speech_bubble(ui: &mut egui::Ui, w: f32, text: &str) {
    let p = ui.painter();
    let font = egui::FontId::proportional(13.0);
    let galley = p.layout_no_wrap(text.to_string(), font, Color32::WHITE);
    let bw = (galley.size().x + 22.0).max(70.0);
    let bh = 26.0;

    let b_rect = Rect::from_center_size(Pos2::new(w / 2.0, 16.0), Vec2::new(bw, bh));
    p.rect_filled(b_rect, 6.0, Color32::from_rgba_premultiplied(20, 24, 34, 235));
    p.rect_stroke(
        b_rect,
        6.0,
        Stroke::new(1.8, Color32::from_rgb(0, 229, 255)),
        egui::StrokeKind::Inside,
    );

    // Mũi nhọn trỏ xuống
    let arrow = vec![
        Pos2::new(w / 2.0 - 6.0, 16.0 + bh / 2.0),
        Pos2::new(w / 2.0, 16.0 + bh / 2.0 + 6.0),
        Pos2::new(w / 2.0 + 6.0, 16.0 + bh / 2.0),
    ];
    p.add(egui::Shape::convex_polygon(
        arrow,
        Color32::from_rgba_premultiplied(20, 24, 34, 235),
        Stroke::NONE,
    ));

    p.galley(
        Pos2::new(w / 2.0 - galley.size().x / 2.0, 16.0 - galley.size().y / 2.0),
        galley,
        Color32::WHITE,
    );
}

// =============================================================================
// VÒNG LẶP EFRAME: 120 FPS ENGINE
// =============================================================================
impl eframe::App for App {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        let (sw, sh) = (
            ctx.screen_rect().width().max(800.0),
            ctx.screen_rect().height().max(600.0),
        );

        // Lấy vị trí con trỏ chuột trên toàn màn hình để phục vụ hành động ChaseCursor
        let mouse_pos = ctx.input(|i| i.pointer.hover_pos()).map(|p| (p.x, p.y));

        // Va chạm giữa các rồng: đổi hướng và chào nhau
        let n = self.pets.len();
        for i in 0..n {
            for j in (i + 1)..n {
                let dist_x = (self.pets[i].x - self.pets[j].x).abs();
                let dist_y = (self.pets[i].y - self.pets[j].y).abs();
                if dist_x < 90.0 && dist_y < 90.0 && rand::random::<f32>() < 0.05 {
                    let (adx, ady) = (self.pets[i].dx, self.pets[i].dy);
                    self.pets[i].dx = self.pets[j].dx;
                    self.pets[i].dy = self.pets[j].dy;
                    self.pets[j].dx = adx;
                    self.pets[j].dy = ady;

                    let h1 = self.pets[i].hello();
                    let h2 = self.pets[j].hello();
                    if let Some(m1) = h1 {
                        self.pets[i].say(m1);
                    }
                    if let Some(m2) = h2 {
                        self.pets[j].say(m2);
                    }
                }
            }
        }

        // BẢNG ĐIỀU KHIỂN TRUNG TÂM (Dragon Control Dashboard)
        egui::Window::new("🐉 Bảng Điều Khiển Rồng Thần 120 FPS")
            .default_width(320.0)
            .show(ctx, |ui| {
                ui.heading("🐉 5 Loài Rồng Thần Thoại (120 FPS)");
                ui.separator();
                ui.label(format!("⚡ Tần số: 120 FPS (~8ms) | Số rồng: {}", self.pets.len()));
                ui.add_space(4.0);

                // Danh sách rồng & trạng thái hành vi hiện tại
                for p in &mut self.pets {
                    let mut show = !self.hidden.get(&p.spec.id).copied().unwrap_or(false);
                    ui.horizontal(|ui| {
                        ui.checkbox(&mut show, format!("{}", p.spec.name));
                        ui.small(format!("[{}]", p.current_action.name_vi()));
                    });
                    self.hidden.insert(p.spec.id.clone(), !show);
                }

                ui.separator();
                ui.label("🎯 Kích hoạt tức thì 10 Hành Vi:");

                // Lưới nút bấm 10 hành động
                ui.horizontal_wrapped(|ui| {
                    if ui.button("🔥 Phun Phép").clicked() {
                        for p in &mut self.pets {
                            p.trigger_action(DragonAction::BreatheElement);
                        }
                    }
                    if ui.button("⚡ Lướt Siêu Tốc").clicked() {
                        for p in &mut self.pets {
                            p.trigger_action(DragonAction::DashSprint);
                        }
                    }
                    if ui.button("🦁 Gầm Thét").clicked() {
                        for p in &mut self.pets {
                            p.trigger_action(DragonAction::Roar);
                        }
                    }
                    if ui.button("💤 Đi Ngủ").clicked() {
                        for p in &mut self.pets {
                            p.trigger_action(DragonAction::SleepZzz);
                        }
                    }
                    if ui.button("🐭 Đuổi Chuột").clicked() {
                        for p in &mut self.pets {
                            p.trigger_action(DragonAction::ChaseCursor);
                        }
                    }
                    if ui.button("📜 Sấm Ngôn").clicked() {
                        for p in &mut self.pets {
                            p.trigger_action(DragonAction::TalkMythic);
                        }
                    }
                    if ui.button("🦅 Sà Xuống").clicked() {
                        for p in &mut self.pets {
                            p.trigger_action(DragonAction::HoverDive);
                        }
                    }
                    if ui.button("✨ Tinh Nghịch").clicked() {
                        for p in &mut self.pets {
                            p.trigger_action(DragonAction::PlayfulScratch);
                        }
                    }
                    if ui.button("☁️ Lơ Lửng").clicked() {
                        for p in &mut self.pets {
                            p.trigger_action(DragonAction::Idle);
                        }
                    }
                    if ui.button("🧭 Tuần Tra").clicked() {
                        for p in &mut self.pets {
                            p.trigger_action(DragonAction::FlyWander);
                        }
                    }
                });

                ui.separator();
                ui.small("• Chuột phải vào rồng: Nghe sấm ngôn");
                ui.small("• Di chuột gần rồng: Rồng sẽ đuổi theo nếu ở mode Chase");

                ui.add_space(8.0);
                if ui.button("❌ Đóng toàn bộ Rồng").clicked() {
                    ctx.send_viewport_cmd(egui::ViewportCommand::Close);
                }
            });

        // VẼ TỪNG CON RỒNG TRÊN VIEWPORT RIÊNG BIỆT (120 FPS TRANSPARENT)
        for p in &mut self.pets {
            if self.hidden.get(&p.spec.id).copied().unwrap_or(false) {
                continue;
            }

            p.target_mouse = mouse_pos;
            p.step(sw, sh);

            let pos = Pos2::new(p.x, p.y);
            let (w, h) = p.spec.size;
            let vid = egui::ViewportId::from_hash_of(p.spec.id.clone());

            let pet_name = p.spec.name.clone();
            let pet_bubble = p.bubble_text.clone();
            let is_oriental = p.is_oriental_dragon();

            // Clone snapshot pet để vẽ an toàn trong viewport 120 FPS
            let p_snapshot = p.clone();

            ctx.show_viewport_immediate(
                vid,
                egui::ViewportBuilder::default()
                    .with_title(&pet_name)
                    .with_inner_size([w, h])
                    .with_position(pos)
                    .with_decorations(false)
                    .with_always_on_top()
                    .with_transparent(true)
                    .with_mouse_passthrough(false),
                |vctx, _cls| {
                    egui::CentralPanel::default()
                        .frame(egui::Frame::NONE.fill(Color32::TRANSPARENT))
                        .show(vctx, |ui| {
                            // 1. Vẽ Rồng theo chủng loại
                            if is_oriental {
                                draw_oriental_dragon(ui, w, h, &p_snapshot);
                            } else {
                                draw_western_dragon(ui, w, h, &p_snapshot);
                            }

                            // 2. Vẽ bóng thoại sấm ngôn nếu có
                            if let Some(ref text) = pet_bubble {
                                draw_speech_bubble(ui, w, text);
                            }

                            // 3. Yêu cầu vẽ lại đúng nhịp 8ms (~120 FPS)
                            vctx.request_repaint_after(std::time::Duration::from_millis(8));
                        });
                },
            );

            // Chuột phải: kích hoạt sấm ngôn
            if ctx.input(|i| i.pointer.secondary_clicked()) {
                p.trigger_action(DragonAction::TalkMythic);
            }
        }

        // Tần số repaint chính 120 FPS
        ctx.request_repaint_after(std::time::Duration::from_millis(8));
    }
}

fn main() -> eframe::Result<()> {
    let args: Vec<String> = std::env::args().collect();
    let all = args.iter().any(|a| a == "--all") || args.len() <= 1;
    let want: Vec<String> = args
        .windows(2)
        .filter_map(|w| (w[0] == "--pet").then(|| w[1].clone()))
        .collect();

    let specs = load_specs(&want, all);
    println!(
        "🐉 Khởi động Động Cơ Rồng Thần 120 FPS: {} loài: {:?}",
        specs.len(),
        specs.iter().map(|s| &s.id).collect::<Vec<_>>()
    );

    eframe::run_native(
        "Bảng Điều Khiển Rồng Thần 120 FPS",
        eframe::NativeOptions {
            viewport: egui::ViewportBuilder::default()
                .with_title("🐉 Bảng Điều Khiển Rồng Thần 120 FPS")
                .with_inner_size([340.0, 360.0]),
            ..Default::default()
        },
        Box::new(|cc| Ok(Box::new(App::new(specs, cc)))),
    )
}
