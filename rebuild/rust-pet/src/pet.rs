//! pet.rs — Logic Động Cơ Desktop Pets & 5 Loài Rồng Thần Thoại 120 FPS.
//! Quản lý 10 hành vi: Idle, Wander, Dash, Breathe, Roar, Sleep, Scratch, Dive, Chase, Talk.
use rand::seq::SliceRandom;
use rand::Rng;
use serde::Deserialize;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum DragonAction {
    Idle,            // 1. Bay lơ lửng ngắm cảnh
    FlyWander,       // 2. Bay tuần tra uốn lượn
    DashSprint,      // 3. Phóng siêu tốc tạo vệt sáng
    BreatheElement,  // 4. Phun nguyên tố (Lửa / Băng / Lôi châu)
    Roar,            // 5. Gầm thét uy phong
    SleepZzz,        // 6. Cuộn tròn ngủ say
    PlayfulScratch,  // 7. Gãi đầu vuốt râu tinh nghịch
    HoverDive,       // 8. Bay vút lên rồi sà xuống bắt mồi
    ChaseCursor,     // 9. Đuổi theo con trỏ chuột
    TalkMythic,      // 10. Phát sấm ngôn cổ ngữ thần thoại
}

impl DragonAction {
    pub fn name_vi(&self) -> &'static str {
        match self {
            Self::Idle => "Lơ Lửng (Idle)",
            Self::FlyWander => "Tuần Tra (Wander)",
            Self::DashSprint => "Lướt Nhanh (Dash)",
            Self::BreatheElement => "Phun Phép (Breathe)",
            Self::Roar => "Gầm Thét (Roar)",
            Self::SleepZzz => "Ngủ Say (Sleep)",
            Self::PlayfulScratch => "Tinh Nghịch (Scratch)",
            Self::HoverDive => "Sà Xuống (Dive)",
            Self::ChaseCursor => "Đuổi Chuột (Chase)",
            Self::TalkMythic => "Sấm Ngôn (Talk)",
        }
    }
}

#[derive(Debug, Clone, Deserialize)]
pub struct PetSpec {
    pub id: String,
    pub name: String,
    #[serde(default = "d128")]
    pub size: (f32, f32),
    #[serde(default = "d8")]
    #[allow(dead_code)]
    pub speed_ms: u64,
    #[serde(default)]
    #[allow(dead_code)]
    pub behaviors: Vec<String>,
    #[serde(default)]
    pub phrases: Vec<String>,
    #[serde(default = "dcolor")]
    pub color: String,
}

fn d128() -> (f32, f32) { (180.0, 150.0) }
fn d8() -> u64 { 8 } // Mặc định 8ms (~120 FPS)
fn dcolor() -> String { "#00e5a3".into() }

impl PetSpec {
    pub fn parse_color(&self) -> (u8, u8, u8) {
        let hex = self.color.trim_start_matches('#');
        if hex.len() == 6 {
            if let Ok(num) = u32::from_str_radix(hex, 16) {
                return (
                    ((num >> 16) & 0xFF) as u8,
                    ((num >> 8) & 0xFF) as u8,
                    (num & 0xFF) as u8,
                );
            }
        }
        match self.id.as_str() {
            "thanh-long" => (0, 229, 163),   // Xanh ngọc lục bảo
            "hoang-long" => (255, 215, 0),   // Vàng hoàng gia
            "hac-long" => (138, 43, 226),    // Tím bóng đêm
            "hoa-long" => (255, 59, 48),     // Đỏ hỏa diệm
            "bang-long" => (90, 200, 250),   // Xanh băng giá
            "pixel-bird" => (255, 213, 74),
            "mini-penguin" => (34, 34, 34),
            "ghost-boo" => (240, 240, 255),
            _ => (0, 229, 255),
        }
    }
}

#[derive(Clone)]
pub struct Pet {
    pub spec: PetSpec,
    pub x: f32, pub y: f32,
    pub dx: f32, pub dy: f32,
    pub tick: u64,
    pub current_action: DragonAction,
    pub action_timer: u32,
    pub spine_nodes: Vec<(f32, f32)>, // 10 đốt thân rồng uốn lượn 120 FPS
    pub wing_angle: f32,              // Góc đập cánh rồng phương Tây
    pub breath_progress: f32,         // 0.0 -> 1.0 hiệu ứng phun lửa/băng
    pub bubble_text: Option<String>,
    pub bubble_timer: u32,
    pub target_mouse: Option<(f32, f32)>,
    // Các trường vi mô chi tiết 360 độ (120 FPS Micro-motion):
    pub facing_angle: f32,            // Hướng mặt/bay xoay 360 độ (0 -> 2pi radian)
    pub eye_look: (f32, f32),         // Độ lệch con ngươi mắt theo chuột 360 độ [-3.5, 3.5]
    pub blink_state: f32,             // 0.0: mở to, 1.0: nhắm mắt cười
    pub whisker_wave: f32,            // Biên độ sóng râu rồng
    pub jaw_open: f32,                // Độ mở hàm dưới (0.0 -> 1.0)
    pub orb_orbit: f32,               // Góc quỹ đạo 3D của Long Châu (0 -> 2pi)
}

impl Pet {
    pub fn new(spec: PetSpec, sw: f32, sh: f32) -> Self {
        let mut r = rand::thread_rng();
        let init_x = r.gen_range(60.0..(sw - 220.0).max(70.0));
        let init_y = r.gen_range(60.0..(sh - 220.0).max(70.0));

        // Khởi tạo 10 đốt thân xếp nối đuôi nhau
        let spine_nodes = (0..10).map(|i| (init_x + (i as f32) * 12.0, init_y)).collect();

        Self {
            x: init_x,
            y: init_y,
            dx: *[-2.5, -1.8, 1.8, 2.5].choose(&mut r).unwrap_or(&2.0),
            dy: *[-1.5, -0.8, 0.8, 1.5].choose(&mut r).unwrap_or(&1.0),
            tick: r.gen_range(0..1000),
            current_action: DragonAction::FlyWander,
            action_timer: r.gen_range(120..360),
            spine_nodes,
            wing_angle: 0.0,
            breath_progress: 0.0,
            bubble_text: None,
            bubble_timer: 0,
            target_mouse: None,
            facing_angle: 0.0,
            eye_look: (0.0, 0.0),
            blink_state: 0.0,
            whisker_wave: 0.0,
            jaw_open: 0.0,
            orb_orbit: 0.0,
            spec,
        }
    }

    #[allow(dead_code)]
    pub fn is_dragon(&self) -> bool {
        matches!(
            self.spec.id.as_str(),
            "thanh-long" | "hoang-long" | "hac-long" | "hoa-long" | "bang-long"
        )
    }

    pub fn is_oriental_dragon(&self) -> bool {
        matches!(self.spec.id.as_str(), "thanh-long" | "hoang-long" | "hac-long")
    }

    #[allow(dead_code)]
    pub fn is_western_dragon(&self) -> bool {
        matches!(self.spec.id.as_str(), "hoa-long" | "bang-long")
    }

    pub fn say(&mut self, text: impl Into<String>) {
        self.bubble_text = Some(text.into());
        self.bubble_timer = 240; // 240 frame ở 120 FPS = 2 giây hiển thị
    }

    pub fn trigger_action(&mut self, action: DragonAction) {
        self.current_action = action;
        let mut r = rand::thread_rng();
        self.action_timer = match action {
            DragonAction::Idle => r.gen_range(100..200),
            DragonAction::FlyWander => r.gen_range(180..360),
            DragonAction::DashSprint => 80,
            DragonAction::BreatheElement => 90,
            DragonAction::Roar => 70,
            DragonAction::SleepZzz => 240,
            DragonAction::PlayfulScratch => 100,
            DragonAction::HoverDive => 110,
            DragonAction::ChaseCursor => 200,
            DragonAction::TalkMythic => 120,
        };
        if action == DragonAction::TalkMythic {
            if let Some(msg) = self.hello() {
                self.say(msg);
            }
        }
    }

    /// Một bước mô phỏng tần số cao 120 FPS
    pub fn step(&mut self, sw: f32, sh: f32) {
        self.tick += 1;

        // 1. Quản lý bóng thoại
        if self.bubble_timer > 0 {
            self.bubble_timer -= 1;
            if self.bubble_timer == 0 {
                self.bubble_text = None;
            }
        }

        // 2. Chuyển đổi trạng thái 10 hành động
        if self.action_timer > 0 {
            self.action_timer -= 1;
        } else {
            let mut r = rand::thread_rng();
            let next = match r.gen_range(0..10) {
                0 => DragonAction::Idle,
                1 => DragonAction::FlyWander,
                2 => DragonAction::DashSprint,
                3 => DragonAction::BreatheElement,
                4 => DragonAction::Roar,
                5 => DragonAction::SleepZzz,
                6 => DragonAction::PlayfulScratch,
                7 => DragonAction::HoverDive,
                8 => DragonAction::ChaseCursor,
                _ => DragonAction::TalkMythic,
            };
            self.trigger_action(next);
        }

        // 3. Thực thi hành vi cụ thể ở 120 FPS
        let mut r = rand::thread_rng();
        match self.current_action {
            DragonAction::Idle => {
                // Dao động bồng bềnh tại chỗ
                self.y += ((self.tick as f32 * 0.08).sin()) * 0.4;
            }
            DragonAction::FlyWander => {
                self.x += self.dx;
                self.y += self.dy + ((self.tick as f32 * 0.06).sin()) * 0.8;
            }
            DragonAction::DashSprint => {
                // Lao vút siêu tốc x2.5
                self.x += self.dx * 2.5;
                self.y += self.dy * 2.0;
            }
            DragonAction::BreatheElement => {
                // Phun phép nguyên tố: tăng dần tiến trình
                self.breath_progress = (1.0 - (self.action_timer as f32 / 90.0)).clamp(0.0, 1.0);
            }
            DragonAction::Roar => {
                // Rung lắc nhẹ mô phỏng tiếng gầm
                self.x += r.gen_range(-1.2..1.2);
                self.y += r.gen_range(-1.2..1.2);
            }
            DragonAction::SleepZzz => {
                // Nằm ngủ im lìm, phập phồng nhẹ
                self.y += ((self.tick as f32 * 0.04).sin()) * 0.2;
            }
            DragonAction::PlayfulScratch => {
                // Gãi đầu, lắc qua lại
                self.x += ((self.tick as f32 * 0.15).sin()) * 0.6;
            }
            DragonAction::HoverDive => {
                // Bay sà xuống
                self.x += self.dx * 1.5;
                self.y += 2.8;
            }
            DragonAction::ChaseCursor => {
                // Đuổi theo con trỏ chuột nếu có tọa độ
                if let Some((mx, my)) = self.target_mouse {
                    let diff_x = mx - (self.x + self.spec.size.0 / 2.0);
                    let diff_y = my - (self.y + self.spec.size.1 / 2.0);
                    let dist = (diff_x * diff_x + diff_y * diff_y).sqrt();
                    if dist > 30.0 {
                        self.dx = (diff_x / dist) * 3.2;
                        self.dy = (diff_y / dist) * 3.2;
                        self.x += self.dx;
                        self.y += self.dy;
                    }
                } else {
                    self.x += self.dx;
                    self.y += self.dy;
                }
            }
            DragonAction::TalkMythic => {
                self.x += self.dx * 0.8;
                self.y += self.dy * 0.8;
            }
        }

        // Đập cánh rồng phương Tây (120 FPS mượt mà)
        self.wing_angle = (self.tick as f32 * 0.18).sin();

        // 4. CẬP NHẬT GÓC XOAY 360 ĐỘ & CHUYỂN ĐỘNG VI MÔ CHI TIẾT
        // a. Hướng nhìn 360 độ (Facing Angle) xoay theo vector vận tốc hoặc con trỏ chuột
        let target_angle = if let Some((mx, my)) = self.target_mouse {
            let cx = self.x + self.spec.size.0 * 0.35;
            let cy = self.y + self.spec.size.1 * 0.45;
            (my - cy).atan2(mx - cx)
        } else {
            self.dy.atan2(self.dx)
        };
        // Nội suy mượt góc xoay (Lerp Angle) để rồng quay đầu uyển chuyển
        let diff = (target_angle - self.facing_angle + std::f32::consts::PI) % std::f32::consts::TAU - std::f32::consts::PI;
        self.facing_angle += diff * 0.12;

        // b. Mắt dõi theo con trỏ chuột 360 độ (Pupil Eye Tracking)
        if let Some((mx, my)) = self.target_mouse {
            let ex = mx - (self.x + 45.0);
            let ey = my - (self.y + 65.0);
            let edist = (ex * ex + ey * ey).sqrt();
            if edist > 1.0 {
                self.eye_look = ((ex / edist) * 3.2, (ey / edist) * 3.2);
            } else {
                self.eye_look = (0.0, 0.0);
            }
        } else {
            // Nhìn theo hướng rồng đang bay
            self.eye_look = (self.facing_angle.cos() * 2.2, self.facing_angle.sin() * 2.2);
        }

        // c. Chu kỳ chớp mắt ngẫu nhiên tự nhiên (Blinking Cycle)
        let blink_mod = self.tick % 360;
        self.blink_state = if blink_mod < 14 {
            ((blink_mod as f32 / 14.0) * std::f32::consts::PI).sin()
        } else {
            0.0
        };

        // d. Sóng mềm mại của Râu Rồng (2-layer Soft Sine Wave)
        self.whisker_wave = (self.tick as f32 * 0.15).sin() * 7.5;

        // e. Khớp mở hàm dưới (Jaw open) theo hành động
        self.jaw_open = match self.current_action {
            DragonAction::BreatheElement => 0.85 + 0.15 * (self.tick as f32 * 0.25).sin(),
            DragonAction::Roar => 1.0,
            _ => ((self.tick as f32 * 0.06).sin() * 0.12).max(0.0), // Nhịp thở nhẹ
        };

        // f. Quỹ đạo elip 3D không gian 360 độ của Dạ Minh Châu
        self.orb_orbit = (self.tick as f32 * 0.07) % std::f32::consts::TAU;

        // 5. Giới hạn biên màn hình (Bounce)
        let (w, h) = self.spec.size;
        if self.x < 0.0 {
            self.x = 0.0;
            self.dx = self.dx.abs();
        } else if self.x + w > sw {
            self.x = sw - w;
            self.dx = -self.dx.abs();
        }

        if self.y < 0.0 {
            self.y = 0.0;
            self.dy = self.dy.abs();
        } else if self.y + h > sh - 60.0 {
            self.y = sh - 60.0 - h;
            self.dy = -self.dy.abs();
        }

        // 6. Thuật toán bám đuôi động học (Kinematic Follow Chain) cho Rồng Phương Đông
        if !self.spine_nodes.is_empty() {
            self.spine_nodes[0] = (self.x + w * 0.35, self.y + h * 0.45);
            for i in 1..self.spine_nodes.len() {
                let prev = self.spine_nodes[i - 1];
                let curr = self.spine_nodes[i];
                let vx = prev.0 - curr.0;
                let vy = prev.1 - curr.1;
                let target_dist = 11.0;
                let len = (vx * vx + vy * vy).sqrt();
                if len > 0.001 {
                    let nx = prev.0 - (vx / len) * target_dist;
                    let ny = prev.1 - (vy / len) * target_dist;
                    // Làm mượt ở 120 FPS
                    self.spine_nodes[i] = (
                        curr.0 + (nx - curr.0) * 0.35,
                        curr.1 + (ny - curr.1) * 0.35,
                    );
                }
            }
        }
    }

    pub fn hello(&self) -> Option<String> {
        let mut r = rand::thread_rng();
        self.spec.phrases.choose(&mut r).cloned()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    fn dragon_spec() -> PetSpec {
        PetSpec {
            id: "thanh-long".into(),
            name: "Thanh Long".into(),
            size: (200.0, 160.0),
            speed_ms: 8,
            behaviors: vec!["all".into()],
            phrases: vec!["Gầm vang!".into()],
            color: "#00e5a3".into(),
        }
    }

    #[test]
    fn dragon_has_10_actions() {
        let mut d = Pet::new(dragon_spec(), 1920.0, 1080.0);
        assert!(d.is_dragon());
        assert!(d.is_oriental_dragon());
        d.trigger_action(DragonAction::BreatheElement);
        assert_eq!(d.current_action, DragonAction::BreatheElement);
        d.step(1920.0, 1080.0);
        assert_eq!(d.spine_nodes.len(), 10);
    }
}
