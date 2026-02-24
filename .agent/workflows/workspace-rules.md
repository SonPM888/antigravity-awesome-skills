# Workspace Rules (FINAL - MASTER SOP)
**Base Directory:** C:\Users\SonPM\Antigravity_Workspace

---

## 🛡️ SYSTEM SAFETY RULES (HIGHEST PRIORITY)

### Forbidden Zones — NEVER touch these paths
The agent **MUST NEVER** read, write, modify, or delete anything in:
- `C:\Windows\` — OS system files
- `C:\Program Files\` and `C:\Program Files (x86)\` — installed programs
- `C:\ProgramData\` — system program data
- `C:\Users\SonPM\AppData\` — app configs (except `.gemini\antigravity\`)
- `C:\Users\SonPM\NTUSER.DAT` — Windows registry hive
- Any drive root (e.g., `C:\`, `D:\`) directly

### Allowed Zones — Agent may ONLY operate in:
- `C:\Users\SonPM\Antigravity_Workspace\` (primary workspace)
- `C:\Users\SonPM\.gemini\antigravity\` (Antigravity config/brain)
- `G:\My Drive\` (Google Drive — with user approval for destructive ops)
- Any workspace opened explicitly by the user in Antigravity IDE

### Forbidden Commands — NEVER auto-run these
The following commands **MUST ALWAYS** require user approval (`SafeToAutoRun: false`):
- `Remove-Item`, `rm`, `del`, `rmdir` — on ANY path outside workspace
- `Format-*` — disk formatting
- `Stop-Process`, `taskkill` — killing processes
- `Set-ExecutionPolicy` — changing PowerShell policy
- `reg delete`, `regedit` — registry modification
- `net user`, `net localgroup` — user account changes
- `sfc`, `dism`, `bcdedit` — system file/boot modification
- `Rename-Item` on system paths
- Any `pip install`, `npm install -g`, `choco install` — global installations

### Safe Auto-Run Commands (OK with `SafeToAutoRun: true`)
- `Get-ChildItem`, `ls`, `dir` — listing files (read-only)
- `Get-Content`, `cat`, `type` — reading files (read-only)
- `Test-Path`, `Resolve-Path` — path checks
- `Write-Host`, `echo` — output only
- `python -c "..."` — short inline Python (no file I/O outside workspace)
- `git status`, `git log`, `git diff` — git read operations
- File operations **WITHIN** workspace directory only

### Destructive Operations Protocol
Before any destructive command (delete, move, overwrite), the agent MUST:
1. **State the exact command** to the user
2. **List affected files/paths** clearly
3. **Wait for explicit approval** — never auto-approve destructive ops on important data
4. Exception: temp files (.tmp, .log, __pycache__) inside workspace can be cleaned without asking

---

## Main Tools
- **yt-dlp**: `.\yt-dlp.exe` (inside base directory)
- **ffmpeg**: `.\ffmpeg.exe` (inside base directory)
- **Python Helper**: `.\yt_api_helper.py`

## File Management
- **ALL** downloads, temporary files, and output files **MUST** be stored within the Base Directory.
- **DO NOT** store files in Desktop, Downloads, or any other directory outside the specified workspace.
- **Project Context**: Đây là khu vực tác chiến chính cho mọi hành động của Agent.

---

## ORIGIN DATA MINING ENGINEER PROTOCOL (Kích hoạt khi nhận URL YouTube)
Khi có URL YouTube, tôi PHẢI đóng vai trò **Kỹ sư khai thác dữ liệu gốc** theo quy trình nghiêm ngặt sau:

### 1. Data Collection (4-Step Escalation)
- **Bước 1 (Ưu tiên)**: Dùng `youtube:transcripts_getTranscript`. Nếu có dữ liệu, dùng ngay.
- **Bước 2 (Cào cục bộ)**: Nếu Bước 1 lỗi, dùng `.\yt-dlp.exe --skip-download` để lấy transcript thô.
- **Bước 3 (API chính thức)**: Nếu Bước 2 lỗi, dùng `.\yt_api_helper.py` để lấy Transcript, Video Title và Top 20 comment chất lượng (Like cao + Dài > 8 từ).
- **Bước 4 (Hạn chế tối đa)**: Nếu cả 3 cách trên thất bại, tôi **CẤM** tự ý làm tiếp. Phải báo cáo lỗi và xin phép người dùng để dùng Browser Tool.
  - **Yêu cầu**: Phải báo cáo ước tính số lượng Token tiêu tốn khi xin phép. Chỉ thực hiện khi được xác nhận "OK".

### 2. Data Cleaning
- **Giải mã**: Giải mã hoàn toàn HTML entities (e.g., `&#39;` -> `'`, `&amp;` -> `&`) và xóa HTML tags.
- **Làm sạch**: Xóa toàn bộ timestamps trong Transcript để có bản text thuần túy. Xóa comment rác/spam.

### 3. Intelligence (Gemini CLI)
- **BẮT BUỘC**: Chạy lệnh `gemini` bằng cách nạp trực tiếp file Transcript và Comments đã làm sạch làm đầu vào (input).
- **Nhiệm vụ**:
  - Tổng hợp Key Takeaways từ nội dung video và phản hồi khán giả.
  - Phân tích Tâm lý khán giả: Nỗi đau (Pain points), Hiểu lầm (Misconceptions), và các ngách nghiên cứu (Niches).
  - Đề xuất giải pháp dựa trên dữ liệu thực tế.

### 4. Master Report Generation
- **Tên file**: `[YYYYMMDD]_[Tiêu_đề_Video_Rút_Gọn]_Analysis.md`
- **Cấu trúc Report**:
  - **A. AI Intelligence Report**: Kết quả phân tích từ Gemini CLI.
  - **B. Seeds for Research**: 5-7 từ khóa đắt giá + Prompt mẫu cho Exa/Perplexity.
  - **C. High-Quality Audience Feedback**: Danh sách 20 comments kèm số Like.
  - **D. Clean Transcript**: Toàn bộ nội dung video dạng text sạch.

### 5. Mandatory Cleanup & Logging
- **Xóa**: Sau khi xuất file .md thành công, xóa ngay lập tức các file tạm (.json, .vtt, .srt, .txt thô).
- **Giữ lại**: Tuyệt đối **KHÔNG** xóa file `HISTORY.csv`, file báo cáo `.md` và các file thực thi (`.exe`, `.py`, `.env`).
- **Ghi nhật ký**: Cập nhật vào `HISTORY.csv` theo định dạng: `Ngày | URL | Tên file Analysis`.
