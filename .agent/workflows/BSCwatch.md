---
description: Periodic reporting tracker - monitor department submissions, alert delays, compliance dashboard
---

// turbo-all

# BSCwatch — Theo dõi Báo cáo Định kỳ

> Monitor department periodic reports → track on-time/late/missing → auto-remind → dashboard
> Reporting matrix learned from SharePoint data + Chairman input
> Cross-links: feeds /BSCkpi (data), /BSCaudit (compliance), /BSCbrief (alerts)

---

## Step 1: Check Reporting Status

```text
"Scan all sources for department periodic reports:

1. CHECK email inbox for reports received this period
2. CHECK SharePoint department folders for uploaded files
3. COMPARE against Reporting Matrix (stored in AG_Output/Logs/reporting_matrix.json):

   | Phòng ban | Loại BC | Kỳ | Deadline | Status |
   |-----------|---------|-----|----------|--------|
   | [dept]    | [type]  | [period] | [date] | ✅/⚠️/🔴 |

4. CLASSIFY each:
   - ✅ On-time + complete content
   - ⚠️ Late or incomplete (missing attachments, wrong format, partial data)
   - 🔴 Not received

5. Present dashboard:

╔══════════════════════════════════════════════════╗
║ 📊 BSC REPORTING TRACKER — [Period]              ║
╠══════════════════════════════════════════════════╣
║ Phòng ban    | Status      | Nhận    | Đủ?      ║
║ ────────────+─────────────+─────────+────────── ║
║ [dept]       | ✅/⚠️/🔴    | [date]  | [Y/N]    ║
╠══════════════════════════════════════════════════╣
║ Summary: [N] on-time, [N] late, [N] missing     ║
║ Data ready for /BSCkpi: [Yes/No — N pending]     ║
╚══════════════════════════════════════════════════╝

ERROR HANDLING:
- If cannot access email/SharePoint → partial scan + flag
- If reporting_matrix.json missing → ask Chairman to define matrix

Ask Chairman: 'Send reminders to late/missing departments?'"
```

[HARD STOP] Chairman approves reminder actions.

---

## Step 2: Remind & Escalate

```text
"Based on Chairman's approval:

Escalation ladder:
- T+3 days: Gentle reminder via email
  'Nhắc nhở: BC [type] kỳ [period] chưa nhận được. Vui lòng gửi trước [date].'
  Draft → Chairman approves → send

- T+5 days: Escalate to Chairman
  'Phòng [X] chưa nộp BC sau 5 ngày. Cần Chairman can thiệp?'
  Option 1: Send direct reminder from Chairman — Authority / May strain relations / Low risk
  Option 2: CC Ban TGĐ on next reminder — Escalation / Effective / Medium risk
  Option 3: Wait 2 more days — Patient / Further delay / Low risk

- T+7 days: Flag in /BSCbrief daily
  Persistent alert until received.

All reminders:
- Draft email → Chairman approves → send
- CC Chairman on escalation emails
- LOG all actions to AG_Activity_Log"
```

---

## Step 3: Content Review

```text
"For received reports:

1. CHECK completeness:
   - Required sections present?
   - Data filled (not blank/placeholder)?
   - Attachments included?
   - Format correct?

2. FLAG issues to Chairman:
   'BC from [dept] received but missing [item]'
   Option 1: Request supplement — Complete / Delay / Low risk
   Option 2: Accept as-is, note gap — Fast / Incomplete data / Medium risk

3. If OK → mark complete in tracker

4. CROSS-WORKFLOW CHECK:
   - All departments submitted? → Flag to Chairman: 'Data ready for /BSCkpi evaluation'
   - Department consistently late? → Flag to Chairman: 'Consider /BSCaudit for [dept] reporting process'"
```

---

## Auto-Evolve

```text
"The Reporting Matrix is a living document:
- AG learns from email patterns: who sends what, when
- AG learns from SharePoint: which folders get updated
- Chairman can manually add/modify requirements
- Matrix stored in AG_Output/Logs/reporting_matrix.json

After 3 months of data:
- AG can predict which departments will be late
- AG can suggest deadline adjustments
- AG can recommend process improvements → /PMSkaizen"
```

---

## State Management

> Agent runs this AUTOMATICALLY. Do not skip.

```text
"UPDATE BSC_STATE.json:

Step 1: WRITE overdue_reports[] — departments missing/late
        {
          'dept': '[department]',
          'report_type': '[BC type]',
          'period': '[T01/2026]',
          'deadline': '[YYYY-MM-DD]',
          'days_overdue': [N],
          'status': 'missing|late|received|complete'
        }
        UPDATE quick_status.overdue_reports count

Step 3: When report received → UPDATE status → 'received' or 'complete'
        If all depts complete → SET quick_status.overdue_reports = 0
        REMOVE completed items, append to history[]

Append to history[]: {timestamp, 'BSCwatch [period]: [N] on-time, [N] late, [N] missing', 'BSCwatch'}"
```

---

## Auto-Log

> Agent runs this AUTOMATICALLY at the end of this workflow. Do not skip.

```text
"DUAL LOG:
1. AG_Output/Logs/AG_Activity_Log_YYYYMM.csv:
   [timestamp], watch, [period], [on_time]/[late]/[missing], [reminders_sent]

2. logs/kaizen/pms_usage.csv:
   Timestamp, BSCwatch, Duration, Outcome, Issues, Suggestion"
```

---

## Quick Reference

### Escalation ladder

| Day | Action | Channel | Approval |
|-----|--------|---------|----------|
| T+3 | Gentle reminder | Email | Chairman approves |
| T+5 | Escalate options | Chairman review | Chairman decides |
| T+7 | Daily flag | /BSCbrief | Auto |

### Dashboard status codes

| Icon | Meaning |
|------|---------|
| ✅ | On-time, complete |
| ⚠️ | Late or incomplete |
| 🔴 | Not received |

### Cross-workflow

| To | Trigger |
|----|---------|
| → `/BSCkpi` | All reports received → ready for analysis |
| → `/BSCaudit` | Department consistently late → audit process |
| → `/BSCbrief` | Overdue items → daily alerts |
| → `/PMSkaizen` | After 3 months → process improvement proposals |

### Invoke: `/BSCwatch` or `/BSCwatch [period: T01/2026]`
