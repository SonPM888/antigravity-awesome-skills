---
description: Daily morning briefing - email, calendar, Teams, tasks, alerts, pending items, focus mode
---

// turbo-all

# BSCbrief — Morning Briefing

> Run at the START of each workday. 2-minute read to grasp everything.
> Data sources: Outlook, Calendar, Teams, SharePoint, To Do.
> Cross-links: triggers /BSCboard, /BSCdraft, /BSCdisclosure, /BSCwatch

---

## Step 0: READ Internal State (BEFORE M365)

```text
"READ AG_Output/Logs/BSC_STATE.json FIRST:

Show QUICK STATUS from previous sessions:
╔══════════════════════════════════════════════════╗
║ 📌 BSC PENDING FROM PREVIOUS SESSIONS           ║
╠══════════════════════════════════════════════════╣
║ ⏰ Active CBTT: [N] (deadlines: [list])          ║
║ 📋 Open actions: [N] ([overdue] overdue)         ║
║ 🔍 Audit findings: [N] open                     ║
║ 📊 Overdue reports: [N] departments              ║
║ ⏳ Pending decisions: [N]                        ║
║ 💡 Kaizen backlog: [N] approved, not implemented ║
╚══════════════════════════════════════════════════╝

If any CBTT countdown is active → highlight with remaining time.
If any action item is overdue → highlight with age.

THEN proceed to M365 scan."
```

---

## Step 1: Collect & Analyze

```text
"Start of day. Collect data from all Microsoft 365 sources:

1. OUTLOOK INBOX:
   - Count unread, flagged, VIP senders (CEO, BIDV, UBCKNN, SGDCK)
   - Categorize: ⚡ Urgent (needs reply today) / 📌 Action needed / 📨 FYI
   - Highlight: emails about HĐQT, NQ, CBTT, deadline-sensitive items

2. CALENDAR:
   - Today's meetings (time, location, attendees, prep needed?)
   - Tomorrow's meetings (any prep required today?)
   - Upcoming HĐQT sessions within 7 days

3. TEAMS:
   - Unread chats, @mentions
   - Important channel messages

4. SHAREPOINT:
   - New/modified files in 01_HDQT/, 07_CBTT/, 09_KTNB/
   - Files shared with me in last 24h

5. TASKS (To Do):
   - Overdue items
   - Due today

6. PENDING CHECKS (cross-workflow state):
   - Any CBTT countdown active? (from /BSCboard) → ⏰ show remaining time
   - Any phòng ban chưa nộp BC? (from /BSCwatch) → list overdue
   - Any BIDV pre-approval pending? (from /BSCboard) → show status
   - Any action items overdue from previous meetings? → list with age

ERROR HANDLING:
   - If any M365 service fails → retry 2x → show partial briefing with ⚠️ flag
   - Tell Chairman: '[Service] unavailable. Showing [N] of 6 data sources.'
   - Continue with whatever data is available.

Present briefing in this format:

╔══════════════════════════════════════════════════╗
║ 📋 BSC DAILY BRIEFING — [Date]                  ║
╠══════════════════════════════════════════════════╣
║ 📧 EMAIL ([N] unread)                            ║
║ ⚡ Urgent: [list]                                ║
║ 📌 Action needed: [list]                         ║
║ 📨 FYI: [count]                                  ║
║                                                  ║
║ 📅 CALENDAR                                      ║
║ [today's schedule]                               ║
║ [tomorrow's first event — prep needed?]          ║
║                                                  ║
║ 💬 TEAMS ([N] unread)                            ║
║ [important messages / @mentions]                 ║
║                                                  ║
║ ⚠️ ALERTS                                        ║
║ [CBTT: ⏰ Xh left / overdue BC / pending BIDV]   ║
║                                                  ║
║ ✅ TASKS — [overdue] overdue, [today] due today   ║
╠══════════════════════════════════════════════════╣
║ 🎯 AG ĐỀ XUẤT HÔM NAY:                         ║
║ 1. [top priority — with workflow suggestion]     ║
║ 2. [second priority]                             ║
║ 3. [third priority]                              ║
╚══════════════════════════════════════════════════╝

Then ask Chairman to pick Focus mode and actions."
```

---

## Step 2: Chairman Picks Focus Mode

```text
"Q1. Focus mode — pick one:
    1. Deep work (1 big task, AG works silently, minimal interruptions)
    2. Multi-task (several small tasks, quick progress)
    3. Review mode (review documents, approve drafts, clear queue)

Q2. Which actions? (pick from AG recommendations or specify own)

Cross-workflow triggers (suggest if conditions met):
- HĐQT within 7 days? → 'Suggest: /BSCboard to prepare'
- CBTT countdown active? → 'Suggest: /BSCdisclosure to draft'
- BC overdue from departments? → 'Suggest: /BSCwatch to send reminders'
- Need to draft a document? → 'Suggest: /BSCdraft [type]'"
```

[HARD STOP] Wait for Chairman to pick focus mode and actions.

---

## Step 3: Execute

```text
"Based on Chairman's choices:
- Draft email replies if requested
- Prepare meeting materials if needed
- Trigger /BSCboard, /BSCdraft, /BSCdisclosure, /BSCwatch as appropriate
- Update To Do with today's priorities
- Adjust behavior based on Focus mode:
  - Deep work: work silently, only report when done/blocked
  - Multi-task: brief updates after each task
  - Review mode: present items one by one for Chairman's decision"
```

---

## State Management

> Agent runs this AUTOMATICALLY. Do not skip.

```text
"UPDATE BSC_STATE.json:
  - quick_status.last_briefing = [timestamp]
  - MERGE any new items discovered from M365 into active categories
  - If new CBTT detected → add to cbtt_countdowns[]
  - If new overdue report detected → add to overdue_reports[]
  - Append to history[]: {timestamp, 'BSCbrief completed', 'BSCbrief'}"
```

---

## Auto-Log

> Agent runs this AUTOMATICALLY at the end of this workflow. Do not skip.

```text
"DUAL LOG:
1. Append to AG_Output/Logs/AG_Activity_Log_YYYYMM.csv:
   [timestamp], briefing, Outlook+Calendar+Teams+SharePoint, [summary], completed, [duration]

2. Append to logs/kaizen/pms_usage.csv (create with header if missing):
   Timestamp, Workflow, Duration, Outcome, Issues, Suggestion
   Outcome: OK or ISSUE. Max 10 words each."
```

---

## Quick Reference

### BSC Daily Rhythm

```text
Open IDE  →  /BSCbrief  →  Work  →  /BSCboard /BSCdraft /BSCdisclosure etc.
                                          ↓
                                     /PMSquit (includes kaizen)  →  Close IDE
```

### Focus modes

| Mode | Best for | AG behavior |
|------|----------|-------------|
| Deep work | Complex task, board prep | Work silently, report when done |
| Multi-task | Email replies, small fixes | Quick updates after each task |
| Review mode | Approve drafts, clear queue | Present items one by one |

### When to cross-trigger

| Condition | Suggest |
|-----------|---------|
| HĐQT meeting T-7 | `/BSCboard` |
| CBTT countdown active | `/BSCdisclosure` |
| BC overdue | `/BSCwatch` |
| Document needed | `/BSCdraft [type]` |

### Invoke: `/BSCbrief`
