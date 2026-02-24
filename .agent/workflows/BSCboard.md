---
description: Board meeting lifecycle - prep, governance check, BIDV escalation, minutes, NQ, CBTT trigger, follow-up
---

// turbo-all

# BSCboard — Board Meeting Lifecycle + Governance

> Full lifecycle: Prepare → Validate → Meet → Minutes → NQ → CBTT → Follow-up
> Includes: authority check, BIDV pre-approval, 24h CBTT trigger
> Cross-links: /BSCdraft (TTr), /BSCdisclosure (CBTT), /BSCbrief (alerts)

---

## Phase 1: Preparation (T-7 to T-1)

```text
"Board meeting preparation:

1. Scan SharePoint 01_HDQT/ + email for related materials
2. Build draft Agenda from template + previous meeting patterns
3. Create checklist — for each agenda item:
   [ ] Tờ trình ready?
   [ ] Dự thảo NQ ready?
   [ ] Supporting documents attached?
   [ ] BIDV pre-approval needed?
4. If TTr missing → suggest: 'Invoke /BSCdraft TTr — [topic]?'
5. Send Calendar invite + remind attendees

Output: Agenda draft + document checklist → Chairman review."
```

[HARD STOP] Chairman approves Agenda.

---

## Phase 1.5: Governance Validation (MANDATORY before meeting)

```text
"For EACH Tờ trình on the Agenda, validate:

| # | Check | Description | Result |
|---|-------|-------------|--------|
| 1 | THẨM QUYỀN | Content belongs to HĐQT scope? (vs TGĐ/ĐHCĐ) | ☐ PASS / ☐ FAIL |
| 2 | CẤU PHẦN | Complete set: TTr + Draft NQ + Supporting docs? | ☐ PASS / ☐ FAIL |
| 3 | NỘI DUNG KHỚP | TTr ↔ NQ ↔ Docs consistent? (numbers, names, dates) | ☐ PASS / ☐ FAIL |
| 4 | BIDV PRE-APPROVAL | Requires NĐD BIDV approval first? (phân cấp) | ☐ YES / ☐ NO |

FAILURE HANDLING:
- If CẤU PHẦN FAIL (TTr missing):
  Option 1: Invoke /BSCdraft to create TTr now — Fast / May delay meeting / Low risk
  Option 2: Remove item from Agenda — Clean / Postpone topic / Low risk
  Option 3: Proceed with note — Quick / Governance gap / Medium risk

- If THẨM QUYỀN FAIL:
  Option 1: Redirect to TGĐ/ĐHCĐ — Correct / Delay / Low risk
  Option 2: Adjust scope to fit HĐQT authority — May work / Partial / Medium risk

- If BIDV PRE-APPROVAL = YES:
  1. Draft report/request to NĐD BIDV (reference 02_NDD_BIDV/)
  2. Chairman review → send to BIDV
  3. Wait for response → record result
  4. Only then add to HĐQT Agenda

  If BIDV REJECTS:
  Option 1: Revise TTr per BIDV feedback → resubmit — Thorough / Slow / Low risk
  Option 2: Escalate to Chairman for direct discussion with NĐD — Fast / Political / Medium risk
  Option 3: Remove from Agenda → postpone to next meeting — Safe / Delay / Low risk

Present validation matrix to Chairman."
```

[HARD STOP] Chairman confirms all items validated.

---

## Phase 2: During Meeting (T)

```text
"AG standby mode:
- Chairman provides bullet points / voice notes
- AG expands into structured minutes
- Track: action items, deadlines, assignments (WHO does WHAT by WHEN)
- Record: voting results, ratios, member opinions
- Flag: any item requiring CBTT → mark for Phase 3"
```

---

## Phase 3: Post-Meeting (T+1 to T+3)

```text
"Post-meeting processing:

1. CREATE Biên bản họp HĐQT (from BSC template) → Chairman review
   [HARD STOP] Chairman approves BB.

2. CREATE Nghị quyết HĐQT (from BSC template) → Chairman review
   [HARD STOP] Chairman approves NQ.

3. CBTT CHECK for each NQ:
   - Analyze NQ content (AI context-aware, not just keywords)
   - Cross-ref with CBTT obligations (TT96, Luật CK, Điều lệ)
   - If CBTT required → ⏰ START 24H COUNTDOWN → auto-trigger /BSCdisclosure
   - Alert Chairman: 'NQ [X] requires CBTT. Deadline: [exact time]'
   - If uncertain → present to Chairman:
     Option 1: Yes, CBTT required — Safe / Extra work / Low risk
     Option 2: No, not required — Fast / Potential violation / High risk

4. SEND action item emails to responsible parties
   - For each action: WHO, WHAT, DEADLINE
   - Draft email → Chairman approves → send

5. ARCHIVE to 01_HDQT/[YYYY]/[Session]/
   File naming: [YYYYMMDD]_AG_Minutes_HDQT_[Session]_v1.docx
                [YYYYMMDD]_AG_NQ_HDQT_[Topic]_v1.docx"
```

---

## Phase 4: Follow-up (T+7, T+14, ongoing)

```text
"Track action items from this meeting:
- Check progress via email/Teams
- Remind assignees approaching deadline
- Report to Chairman: done / pending / overdue
- Update master tracker

Escalation ladder:
- D+7: Gentle reminder to assignee
- D+14: CC Chairman on reminder
- D+21: Flag in /BSCbrief daily until resolved

If all items done → mark meeting CLOSED in tracker."
```

---

## State Management

> Agent runs this AUTOMATICALLY after each phase. Do not skip.

```text
"UPDATE BSC_STATE.json after each phase:

Phase 1: WRITE pending_decisions[] if BIDV pre-approval needed
Phase 3: WRITE action_items[] — WHO, WHAT, WHEN for each NQ action
         WRITE cbtt_countdowns[] — if CBTT triggered
         UPDATE quick_status counts
Phase 4: UPDATE action_items[].status when completed/overdue
         REMOVE closed items, append to history[]

State entry format for action_items:
{
  'id': 'ACT-[NNN]',
  'from_meeting': '[Session]',
  'who': '[department/person]',
  'what': '[description]',
  'deadline': '[YYYY-MM-DD]',
  'status': 'open|in_progress|done|overdue',
  'created': '[timestamp]'
}

Append to history[]: {timestamp, event description, 'BSCboard'}"
```

---

## Auto-Log

> Agent runs this AUTOMATICALLY at the end of this workflow. Do not skip.

```text
"DUAL LOG:
1. AG_Output/Logs/AG_Activity_Log_YYYYMM.csv:
   [timestamp], board_meeting, [session_id], [phase], [description], [output_files], [status]

2. logs/kaizen/pms_usage.csv:
   Timestamp, BSCboard, Duration, Outcome, Issues, Suggestion"
```

---

## Quick Reference

### Timeline

| When | Phase | Key output |
|------|-------|-----------|
| T-7 | Preparation | Agenda, checklist |
| T-3 | Governance | Validation matrix |
| T | Meeting | Bullet notes |
| T+1 | Post-meeting | BB, NQ, CBTT check |
| T+7 | Follow-up | Action item tracking |

### Output files

| File | Template | Location |
|------|----------|----------|
| Biên bản | BSC BB template | `01_HDQT/[YYYY]/` |
| Nghị quyết | BSC NQ template | `01_HDQT/[YYYY]/` |
| CBTT | via `/BSCdisclosure` | `07_CBTT/[YYYY]/` |

### Cross-workflow

| Trigger | Action |
|---------|--------|
| TTr missing | → `/BSCdraft TTr` |
| NQ needs CBTT | → `/BSCdisclosure` |
| Action overdue | → flag in `/BSCbrief` |

### Invoke: `/BSCboard` or `/BSCboard [session: Kỳ X/2026]`
