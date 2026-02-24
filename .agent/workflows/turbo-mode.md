---
description: Terminal auto-run policy — giảm xác nhận khi phương hướng đã rõ
---

// turbo-all

# Turbo Mode Policy

## ✅ AUTO-RUN (SafeToAutoRun = true)

### Read-only commands
- `git status`, `git log`, `git diff`
- `ls`, `dir`, `Get-ChildItem`, `cat`, `type`, `head`, `tail`
- `python -c "import ast; ast.parse(...)"` (syntax check)
- `grep`, `find`, `rg`, `fd`

### File operations (khi plan đã approved)
- `mkdir`, `New-Item -ItemType Directory`
- `move`, `Move-Item`, `mv` → move vào `_archive/` hoặc đích đã xác định
- `copy`, `Copy-Item`, `cp`
- `git add`, `git commit` (khi user đã confirm phương hướng)

### Dev commands
- `npm run dev`, `npm start`, `python script.py` (khi đang test)
- `pip list`, `npm list`, `node -v`, `python --version`

## 🛑 HỎI TRƯỚC (SafeToAutoRun = false)

### Destructive operations — LUÔN HỎI
- `rm`, `del`, `Remove-Item`, `git rm` → **ƯU TIÊN move vào `_archive/` thay vì xóa**
- `git push`, `git reset`, `git rebase`
- `git checkout --` (discard changes)

### Install / System changes — LUÔN HỎI
- `pip install`, `npm install`, `choco install`
- Bất kỳ lệnh nào thay đổi system-level config
- Registry edits, environment variable changes

### External requests — LUÔN HỎI
- `curl`, `wget`, API calls
- Bất kỳ lệnh nào gửi data ra ngoài

## 📋 QUY TẮC CHUNG

1. **Khi user đã ra quyết định rõ** (ví dụ: "chạy đi", "commit đi", "option 1") → auto-run luôn, không hỏi lại
2. **Khi đang trong plan đã approved** → auto-run các bước trong plan
3. **File delete = FORBIDDEN by default** → luôn hỏi, luôn đề xuất `_archive/` trước
4. **Nếu không chắc** → hỏi, nhưng gom nhiều câu hỏi thành 1 lần hỏi
