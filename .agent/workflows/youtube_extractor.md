---
description: Workflow tự động khai thác dữ liệu YouTube (Transcript & Comments)
---
// turbo-all

Quy trình tự động hóa tuyệt đối:

1. Chặn rút yt-dlp sẽ lấy transcript và video info:
   - .\yt-dlp.exe --js-runtimes deno --write-auto-subs --skip-download -o "transcript_raw" [URL]
   - .\yt-dlp.exe --js-runtimes deno --write-info-json --skip-download --extractor-args "youtube:max-comments=20" -o "video_data" [URL]

2. Xử lý dữ liệu thô bằng PowerShell (để tránh giới hạn Token của Gemini):
   - Làm sạch transcript và loại bỏ lặp lại.
   - Trích xuất 20 comments kèm số like.

3. Điều phối Gemini CLI thực hiện phân tích dựa trên dữ liệu đã làm sạch.

4. Tổng hợp Master Report và dọn dẹp Workspace.
