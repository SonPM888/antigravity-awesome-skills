---
description: Information disclosure (CBTT) - 24h countdown, draft, approve, send, compliance audit trail
---

// turbo-all

# BSCdisclosure — Công bố thông tin (24h Compliance)

> 24h countdown from trigger event → draft → approve → send → confirm
> Auto-triggered from /BSCboard or manual invocation
> Cross-links: /BSCboard (source NQ), /BSCbrief (alerts), /BSCdraft (CBTT document)

---

## Trigger Sources

- **Auto from /BSCboard:** NQ HĐQT flagged as requiring CBTT
- **Manual:** Chairman invokes `/BSCdisclosure [event]`
- **Proactive from /BSCbrief:** AG detects event requiring CBTT

---

## Phase 1: Classify & Countdown

```text
"Determine CBTT obligation:

1. CLASSIFY disclosure type:
   | Type | Deadline | Examples |
   |------|----------|---------|
   | Bất thường | 24h | NQ HĐQT, thay đổi nhân sự cấp cao, phát hành CK |
   | Định kỳ | Per schedule | BCTC quý/năm, BC thường niên |
   | Theo yêu cầu | As requested | UBCKNN/SGDCK requests |

2. If 24h deadline:
   - ⏰ START COUNTDOWN from event timestamp
   - Calculate deadline: event_time + 24h (business calendar)
   - Alert Chairman: 'NQ [X] requires CBTT. Deadline: [exact time]'

3. Cross-ref with regulations:
   - TT96/2020/TT-BTC (hướng dẫn CBTT)
   - Luật Chứng khoán 2019 (Điều 120-121)
   - Điều lệ BSC (nếu có quy định riêng)

4. Identify recipients: UBCKNN, SGDCK (HNX/HOSE), website BSC"
```

---

## Phase 2: Draft CBTT

```text
"Draft disclosure content:

1. SCAN SharePoint 07_CBTT/ → find matching template
   - If template found → apply format
   - If NOT found → use generic CBTT format + flag Chairman:
     'Chưa có mẫu CBTT cho loại sự kiện này. AG dùng format chung. Chairman review kỹ.'
2. AUTO-FILL from NQ, BB họp, financial data
3. HIGHLIGHT items needing Chairman confirmation (⚠️ markers)
4. SAVE draft: [YYYYMMDD]_AG_CBTT_[Topic]_v1.docx
5. Show remaining countdown time prominently

Present to Chairman with countdown timer."
```

[HARD STOP] Chairman reviews and approves.

---

## Phase 3: Send & Confirm

```text
"After Chairman approval:

1. Draft emails to:
   - UBCKNN (regulatory@ubcknn.gov.vn or via portal)
   - SGDCK (HNX/HOSE submission)
   - Internal: website BSC team (post on IR page)
2. Chairman approves → SEND

3. ARCHIVE:
   - Save to 07_CBTT/[YYYY]/
   - Save copy to AG_Output/Archive/

4. COMPLIANCE LOG:
   | Field | Value |
   |-------|-------|
   | Event timestamp | [when NQ was signed] |
   | CBTT drafted | [timestamp] |
   | CBTT sent | [timestamp] |
   | Time elapsed | [hours:minutes] |
   | Within 24h? | ✅ YES / ❌ NO |
   | Recipients | [list] |

5. CONFIRMATION LOOP — ASK Chairman: 'CBTT hoàn tất? Đã gửi đủ các bên? (y/n)'

If NOT confirmed by Chairman:
- 14:00 → 💬 Remind via Teams
- 15:00 → 📧 Remind via Email + Teams
- 15:15 → 🔴 ALERT ALL CHANNELS: 'CBTT deadline approaching! [Xh remaining]'
- 15:30 → 🚨 FINAL ALERT: 'CBTT DEADLINE IMMINENT'

DEADLINE OVERRUN PROCEDURE:
If 24h has passed without confirmation:
1. LOG INCIDENT: [YYYYMMDD]_AG_CBTT_Incident_[Topic].md
   - Event description, timeline, reason for delay
2. Alert Chairman immediately: 'CBTT deadline PASSED. Please confirm status.'
3. Option 1: CBTT was sent but not confirmed in system — Update log / Low risk
4. Option 2: CBTT was NOT sent — Send immediately + incident report / High risk
5. Option 3: CBTT not required (misclassified) — Update classification / Medium risk

Mark CONFIRMED only when Chairman explicitly confirms."
```

---

## State Management

> Agent runs this AUTOMATICALLY. Do not skip.

```text
"UPDATE BSC_STATE.json:

Phase 1: WRITE cbtt_countdowns[] — new countdown entry
         {
           'id': 'CBTT-[NNN]',
           'topic': '[description]',
           'event_time': '[timestamp]',
           'deadline': '[timestamp + 24h]',
           'status': 'countdown|draft_ready|sent|confirmed|overrun',
           'created': '[timestamp]'
         }
         UPDATE quick_status.active_cbtt count

Phase 3: UPDATE cbtt_countdowns[].status → 'sent' or 'confirmed'
         If overrun → status = 'overrun', log incident
         When confirmed → REMOVE from active, append to history[]
         UPDATE quick_status.active_cbtt count

Append to history[]: {timestamp, event, 'BSCdisclosure'}"
```

---

## Auto-Log

> Agent runs this AUTOMATICALLY at the end of this workflow. Do not skip.

```text
"DUAL LOG:
1. AG_Output/Logs/AG_Activity_Log_YYYYMM.csv:
   [timestamp], cbtt, [topic], event_time:[T], deadline:[T+24h], sent:[T_sent], compliant:[yes/no]

2. logs/kaizen/pms_usage.csv:
   Timestamp, BSCdisclosure, Duration, Outcome, Issues, Suggestion"
```

---

## Quick Reference

### Deadline rules

| CBTT type | Deadline | Calculated from |
|-----------|----------|-----------------|
| Bất thường | 24h | NQ signature / event occurrence |
| BCTC quý | 5 ngày | End of quarter |
| BCTC năm (chưa kiểm toán) | 20 ngày | End of fiscal year |
| BC thường niên | 20/04 hàng năm | Fixed date |

### Alert schedule (24h type)

| Time | Channel | Severity |
|------|---------|----------|
| Immediately | All | ⏰ Countdown started |
| 14:00 next day | Teams | 💬 Reminder |
| 15:00 | Email + Teams | 📧 Escalation |
| 15:15 | All channels | 🔴 Critical |
| 15:30 | All channels | 🚨 Deadline |
| After deadline | Incident log | 📋 Incident |

### Cross-workflow

| From | Trigger |
|------|---------|
| `/BSCboard` | NQ flagged as CBTT-required |
| `/BSCbrief` | AG detects CBTT event |
| Manual | Chairman invokes directly |

### Invoke: `/BSCdisclosure [event description]`
