---
description: Extract patterns from successful YouTube videos and add them to the Content Bank (_bank/)
---

# Framework Extractor Workflow

Workflow phân tích video YouTube thành công → trích xuất patterns → bổ sung vào `_bank/`.

## Prerequisites
- Video URL hoặc transcript có sẵn
- `_bank/` đã được seed (Batch 2 hoàn thành)

## Steps

### 1. Thu thập transcript

Nếu user cung cấp YouTube URL, khai thác transcript:

// turbo
```
python collector.py "[YOUTUBE_URL]" --transcript-only
```

Nếu transcript đã có sẵn, bỏ qua bước này.

### 2. Đọc operator prompt

Đọc file `AI_YOUTUBE_SYSTEM/_system/framework_extractor.md` để nắm format phân tích.

### 3. Đọc _bank/ hiện tại

Đọc lướt qua các file trong `_bank/` để biết patterns NÀO đã có, tránh ghi trắng:
- `_bank/hooks/` — 6 file
- `_bank/frameworks/` — 7 file
- `_bank/retention/` — 5 file
- `_bank/transitions/` — 3 file
- `_bank/cta/` — 3 file
- `_bank/metaphors/` — 1 file

### 4. Phân tích 7 chiều

Theo format trong `framework_extractor.md`, phân tích video trên 7 chiều:
1. Hook Analysis (15 giây đầu)
2. Framework/Structure Analysis
3. Retention Techniques
4. Transition Patterns
5. CTA & Engagement
6. Metaphors & Analogies
7. Rhythm & Emotional Arc

Output: trình bày trong chat, kèm bảng phân tích và scorecard.

### 5. Đề xuất bổ sung

Tổng hợp patterns MỚI (chưa có trong `_bank/`) thành danh sách đề xuất.
Mỗi đề xuất ghi rõ: file target + nội dung + annotation nguồn.

**⏸️ CHECKPOINT:** Chờ user duyệt trước khi ghi.

### 6. Ghi vào _bank/

Sau khi user duyệt:
- Append patterns được chấp nhận vào file tương ứng trong `_bank/`
- Thêm annotation nguồn: `> 📌 Extracted from: "Video Title" (Channel) — Date`
- KHÔNG ghi đè nội dung hiện có

### 7. (Optional) Batch extraction

Nếu user muốn extract nhiều video cùng lúc:
- Lặp lại steps 1-6 cho mỗi video
- Cuối cùng tổng hợp: common patterns xuất hiện >2 lần → patterns mạnh nhất
- Chỉ ghi common patterns vào `_bank/`

## Notes
- Workflow này bổ sung cho pipeline chính, KHÔNG thay thế
- Chạy định kỳ (2-4 lần/tháng) trên top-performing videos trong niche
- Patterns từ video EN vẫn extract được, nhưng ví dụ nên adapt sang VN khi ghi vào _bank/
