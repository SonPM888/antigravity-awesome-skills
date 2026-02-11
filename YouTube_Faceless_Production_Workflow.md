# QUY TRÌNH SẢN XUẤT YOUTUBE FACELESS (CHUẨN V7.0 - UNIVERSAL CORE)

**Phiên bản:** 1.0
**Ngày cập nhật:** 10/02/2026
**Hệ thống:** Antigravity Master Concepts

---

## 🎯 GIAI ĐOẠN 1: ĐỊNH HÌNH CHIẾN LƯỢC (STRATEGY)

Trước khi viết bất kỳ chữ nào, phải xác định rõ **3 yếu tố cốt lõi**:

### 1. Chọn Đối Tượng (Audience Profile)
Xác định video này dành cho ai để chọn **Profile Skill** tương ứng:
- **Seniors (60+):** Người già, cần tâm giao, hoài niệm.
- **Gen Z (18-25):** Người trẻ, khủng hoảng tuổi 20, cần triết lý/vibe.
- **Office Warriors:** Dân văn phòng, cần chiến lược/thăng tiến.
- **Entrepreneurs:** Doanh nhân, cần bài học xương máu/hệ thống.
- **Homemakers:** Nội trợ, cần sự công nhận/chia sẻ.
- **Rural Friend:** Nông dân, cần kinh nghiệm thực tế/mộc mạc.
- **Bedtime:** Người mất ngủ, cần sự an toàn/ru ngủ.
- **Heartbroken:** Người thất tình, cần sự chữa lành/đồng cảm.
- **Introverts:** Người hướng nội, cần sự thấu hiểu/yên tĩnh.

### 2. Xác Định Mode (Tự động theo Profile)
Không cần chỉnh tay, nhưng cần hiểu cơ chế:
- **Hook Mode:** *Viral (H.S.O)* hay *Comfort (Invitation)*?
- **Rhythm Mode:** *Staccato (Nhanh/Đanh)* hay *Legato (Chậm/Mượt)*?
- **Module:** *Mirror Story*, *Direct Experience*, hay *Case Study*?

### 3. Tìm Core Insight (Sự Thật Cốt Lõi)
- Với Viral Profile: Tìm một **Straw Man** (Niềm tin sai lầm) để đập tan.
  - *Ví dụ:* "Khách hàng luôn đúng" là sai.
- Với Comfort Profile: Tìm một **Silent Pain** (Nỗi đau thầm kín) để xoa dịu.
  - *Ví dụ:* "Cảm giác cô đơn dù đang ở cạnh chồng con."

---

## 📝 GIAI ĐOẠN 2: VIẾT KỊCH BẢN (SCRIPTING)

Sử dụng AI Agent với câu lệnh chuẩn:

> **PROMPT:**
> "Sử dụng `youtube-script-master` V7.0 và Profile `[TÊN_PROFILE]` để viết kịch bản về chủ đề: `[CHỦ_ĐỀ]`.
> Mục tiêu: `[MỤC_TIÊU_CỤ_THỂ]`.
> Đảm bảo tuân thủ đúng Hook Mode và Rhythm Mode của Profile."

**Đầu ra tiêu chuẩn (Required Output):**
1. **Strategy Card:** Tóm tắt thông số kỹ thuật.
2. **Dual Titles:** 1 Title cho Thumbnail (Gây tò mò), 1 Title cho Search (Chuẩn SEO).
3. **Voicescript:** Kịch bản đọc (1500+ từ) có đánh dấu nhịp điệu.
4. **Shorts Script:** Kịch bản video ngắn bổ trợ.

---

## 🎧 GIAI ĐOẠN 3: XỬ LÝ ÂM THANH (AUDIO ENGINEERING)

Tham khảo file `skills/audio-strategy/GUIDE.md` để chọn đúng thông số.

### 1. Giọng Đọc (Voiceover) - Ưu tiên Google Chirp 3 (2026)
- **Seniors:** `vi-VN-Chirp3-HD-D` (Nam trầm, kể chuyện).
- **Gen Z:** `vi-VN-Chirp3-HD-A` (Nữ nhẹ, podcast vibe).
- **Entrepreneurs:** `vi-VN-Chirp3-HD-C` (Nam đanh thép).
- **Bedtime:** `vi-VN-Chirp3-HD-Whisper` (Thì thầm) hoặc Neural2 Pitch -4.
- *(Chi tiết xem bảng GUIDE.md)*

### 2. Nhạc Nền (Ambient Music)
- **Quy tắc vàng:** Nhạc là "Emotional Container". Không được lấn át giọng đọc.
- **Seniors/Homemakers:** Acoustic, Piano, Warm.
- **Gen Z/Heartbroken:** Lo-fi, Rain, Cello.
- **Entrepreneurs/Office:** Industrial, Tech, Deep House.
- **Bedtime:** Theta Waves, Drone (Không giai điệu).

---

## 🎨 GIAI ĐOẠN 4: HÌNH ẢNH & VIDEO (VISUALIZATION)

*(Đang phát triển Skill `youtube-visual-prompt`)*

**Hướng sơ bộ:**
- **Gen Z:** Dark Academia, Neon, Rain, Cinematic.
- **Seniors:** Warm sunlight, Garden, Slow motion, Close-up hands.
- **Entrepreneurs:** Black & White, High contrast, Skyline, Architecture.
- **Bedtime:** Abstract, Space, Deep Ocean, Slow loops.

---

## ✅ GIAI ĐOẠN 5: KIỂM DUYỆT (QUALITY AUDIT)

Trước khi sản xuất, chạy Skill Audit:

> **PROMPT:**
> "Dùng `youtube-script-quality-auditor` để kiểm tra kịch bản vừa tạo."

**Checklist Kiểm Duyệt:**
1. [ ] **Đúng Hook Mode chưa?** (H.S.O hay Invitation).
2. [ ] **Đúng Nhịp điệu (Rhythm) chưa?** (Câu ngắn hay câu dài).
3. [ ] **Có dùng P-A-S-T Sensory không?** (Place, Action, Speech, Thought).
4. [ ] **Có Retention Bridges không?** (Câu cuối chương này nối sang chương kia).
5. [ ] **Có vi phạm "Non-Negotiable Rules" của Profile không?** (Ví dụ: Dùng từ "toxic" với người già).

---

## 📂 CẤU TRÚC THƯ MỤC DỰ ÁN

```
/production
  /scripts          (Lưu file .txt kịch bản)
  /audio            (Lưu file voice và nhạc)
  /visuals          (Lưu file ảnh/video)
  /final_renders    (Video hoàn chỉnh)
/skills
  /youtube-script-master  (V7.0 Core)
  /profiles               (9 Profiles)
  /audio-strategy         (Guide V2.0)
```
