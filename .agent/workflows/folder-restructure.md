---
description: Quy trình tái cấu trúc thư mục (Folder Restructuring Workflow) - 5 bước
---
// turbo-all

# Folder Restructuring Workflow

> Chuẩn mực: ISO 9001 (Document Control), IEEE Std 1471 (Architecture Description)
> Đối tượng: Personal workspace / Small team

---

## Bước 1: Phân tích & Đề xuất (PLANNING — chỉ đọc, không sửa)

```
Prompt:
"Máy là một Senior Solution Architect. Hãy phân tích cấu trúc của thư mục [ĐƯỜNG_DẪN].

Mục tiêu: Tái cấu trúc lại thư mục sao cho khoa học, kết hợp giữa quản lý file văn phòng và project [NGÔN_NGỮ].

Yêu cầu phân tích:
1. Đề xuất một cấu trúc folder phân cấp (ví dụ: docs/, src/, archive/, data/).
2. Áp dụng bộ Naming Convention sau: [YYYYMMDD]_[Context_Tag]_[Description]_[Version].
   - File code dạng snake_case.
   - File văn phòng dạng dấu gạch dưới _ thay cho khoảng trắng.
3. Chỉ ra những file nào đang đặt sai chỗ hoặc cần xóa/lưu trữ.
4. Phân loại file theo mức độ: Active (đang dùng), Archive (lưu trữ), Delete (nên xóa).

Lưu ý: Chỉ đưa ra sơ đồ cây (Tree structure) dự kiến. KHÔNG thực hiện thay đổi nào vào lúc này."
```

**Kết quả kỳ vọng**: Nhận được implementation plan với tree diagram, bảng phân loại file, naming convention.

---

## Bước 2: Review & Phê duyệt kế hoạch

```
Prompt (nếu cần chỉnh sửa):
"Điều chỉnh kế hoạch:
- [Yêu cầu thay đổi cụ thể, ví dụ: 'Giữ lại file X ở root', 'Gộp folder A và B']
Cập nhật lại sơ đồ cây và gửi lại để review."

Prompt (nếu đồng ý):
"LGTM. Chuyển sang bước thực hiện."
```

**Kết quả kỳ vọng**: Plan được phê duyệt, sẵn sàng thực thi.

---

## Bước 3: Thực thi tái cấu trúc (EXECUTION)

```
Prompt:
"Bây giờ hãy thực hiện thay đổi thật sự theo kế hoạch đã duyệt.

Yêu cầu kỹ thuật:
1. Tạo cấu trúc thư mục mới trước, sau đó di chuyển file.
2. Metadata ngày tháng trong tên file lấy từ CreationTime thực tế trên hệ thống.
3. Ghi log toàn bộ thao tác vào file changelog (CSV hoặc Markdown).
4. Nếu đổi tên file code, đảm bảo các file liên quan trỏ đúng đường dẫn mới.
5. Sau khi hoàn thành, liệt kê danh sách các thay đổi đã thực hiện."
```

**Kết quả kỳ vọng**: Toàn bộ file được di chuyển, đổi tên, changelog được tạo.

---

## Bước 4: Kiểm tra kết quả (VERIFICATION)

```
Prompt:
"Hiển thị cấu trúc thư mục mới bằng lệnh tree hoặc danh sách file.
So sánh kết quả thực tế với kế hoạch đã đề ra, đánh giá theo các tiêu chí:
- Root có sạch không?
- Naming convention có nhất quán không?
- Có file nào bị sót hoặc đặt sai vị trí không?
- Changelog có đầy đủ không?"
```

**Kết quả kỳ vọng**: Bảng so sánh Plan vs Actual, xác nhận pass/fail từng tiêu chí.

---

## Bước 5: Viết tài liệu (DOCUMENTATION)

```
Prompt:
"Viết file README.md chuẩn cho thư mục này với nội dung:
1. Sơ đồ cây đầy đủ (full tree) liệt kê mọi file.
2. Giải thích Naming Convention đang áp dụng.
3. Hướng dẫn tra cứu file gốc (kèm lệnh PowerShell/Bash mẫu).
4. Bảng ánh xạ các file quan trọng (tên cũ → tên mới).
5. Tóm tắt refactoring (before/after)."
```

**Kết quả kỳ vọng**: README.md hoàn chỉnh, tự chứa đủ thông tin để truy vết.

---

## Tham chiếu nhanh

### Cấu trúc folder chuẩn (tùy chỉnh theo nhu cầu)

| Folder | Mục đích | Ví dụ nội dung |
| --- | --- | --- |
| `src/` | Code đang active | Script chính, modules |
| `archive/` | Phiên bản cũ, chỉ đọc | Tất cả version lịch sử |
| `docs/` | Tài liệu, template | README, guides, notes |
| `data/` | Dữ liệu, media, assets | Images, videos, CSV |
| `logs/` | Log & changelog | Session logs, changelogs |
| `config/` | Cấu hình | .env, settings files |
| `tests/` | Unit test, integration test | test_*.py |

### Naming Convention cheat sheet

```
[YYYYMMDD]_[Context]_[Description]_[Version/Tag]

Ví dụ:
  20250810_srt_processor_stable_v3558.py    # Archive có ngày + tag
  srt_main.py                                # Active: tên ngắn, rõ ràng
  AI_Image_Prompt_Template.txt               # Văn phòng: underscore thay space
```

### Tag phổ biến

| Tag | Ý nghĩa |
| --- | --- |
| `_stable` | Đã kiểm tra, hoạt động tốt |
| `_draft` | Bản nháp |
| `_beta` | Đang thử nghiệm |
| `_final` | Phiên bản cuối |
| `_archive` | Đã lưu trữ |
| `_deprecated` | Không còn sử dụng |
