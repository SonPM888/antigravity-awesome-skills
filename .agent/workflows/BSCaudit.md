---
description: Internal control audit - process review, compliance check, risk assessment, action tracking
---

// turbo-all

# BSCaudit — Kiểm soát nội bộ

> Review processes, check compliance, assess risks, recommend improvements
> Cross-links: /BSCboard (NQ action tracking), /BSCwatch (reporting compliance), /BSCdraft (audit report)

---

## Step 1: Scope Definition

```text
"Chairman has invoked /BSCaudit.

Define audit scope:
1. Department/process to audit
2. Time period
3. Specific regulations/standards to check against
4. Audit type:
   | Type | Description |
   |------|-------------|
   | Process | Quy trình nội bộ (mua sắm, tuyển dụng, etc.) |
   | Compliance | Tuân thủ pháp luật / quy định UBCKNN |
   | Governance | NQ HĐQT execution, action item completion |
   | Financial | KTNB tài chính, chi phí, ngân sách |

AG will:
- Scan SharePoint 09_KTNB/ for existing audit materials
- Scan relevant department folders
- Review recent email threads about the scope
- Cross-ref /BSCboard: action items from HĐQT meetings → completion rate
- Cross-ref /BSCwatch: department reporting compliance"
```

[HARD STOP] Chairman defines scope.

---

## Step 2: Audit Checklist & Review

```text
"Execute audit:

1. BUILD checklist from:
   - Internal regulations (Điều lệ, Quy chế nội bộ)
   - Industry standards (TT96, Luật CK, UBCKNN guidelines)
   - Previous audit findings for comparison

2. For each checklist item:
   - COLLECT evidence from SharePoint, email, reports
   - ASSESS: ✅ Compliant / ⚠️ Needs improvement / ❌ Non-compliant
   - DOCUMENT evidence source

3. IDENTIFY risks: likelihood × impact matrix
   | Likelihood \ Impact | Low | Medium | High |
   |---------------------|-----|--------|------|
   | High | ⚠️ | 🔴 | 🔴 |
   | Medium | 🟢 | ⚠️ | 🔴 |
   | Low | 🟢 | 🟢 | ⚠️ |

4. CROSS-REF with previous audit findings (if available):
   - Were previous issues fixed?
   - Any recurring patterns?

ERROR HANDLING:
- If evidence insufficient → mark 'Inconclusive' + recommend deeper review
- If access denied to folder → flag to Chairman

Present findings to Chairman."
```

[HARD STOP] Chairman reviews findings before recommendations.

---

## Step 3: Report & Recommendations

```text
"Generate audit report:

1. CREATE report using BSC audit template (or /BSCdraft BC)
   Naming: [YYYYMMDD]_AG_BC_Audit_[Scope]_v1.docx

2. INCLUDE:
   - Executive summary (Pass/Warn/Fail overall)
   - Findings detail with evidence
   - Risk assessment matrix
   - Recommendations — ALWAYS use Options format:
     Option 1: [action] — Pros / Cons / Risk
     Option 2: [action] — Pros / Cons / Risk
   - Action plan with WHO, WHAT, WHEN

3. FAIL HANDLING (from PMSaudit pattern):
   - If any ❌ Non-compliant found:
     MANDATORY: Create fix task with deadline
     → Track until resolved
     → Re-audit ONLY the failed item after fix
     → PASS: close | Still FAIL: escalate to Chairman

4. [HARD STOP] Chairman review → approve

5. If sending to Ủy ban Kiểm toán/HĐQT:
   - Draft email + attach report
   - Chairman approves → send

6. ARCHIVE to AG_Output/Reports/"
```

---

## State Management

> Agent runs this AUTOMATICALLY. Do not skip.

```text
"UPDATE BSC_STATE.json:

Step 2: WRITE audit_findings[] for ⚠️ and ❌ items
        {
          'id': 'AUD-[NNN]',
          'scope': '[department/process]',
          'item': '[finding description]',
          'severity': '⚠️|❌',
          'fix_deadline': '[YYYY-MM-DD]',
          'status': 'open|fixing|re_audit|closed',
          'created': '[timestamp]'
        }
        UPDATE quick_status.open_findings count

Step 3: If re-audit passes → UPDATE status → 'closed'
        REMOVE closed items, append to history[]

Append to history[]: {timestamp, 'Audit [scope] completed: [N] findings', 'BSCaudit'}"
```

---

## Auto-Log

> Agent runs this AUTOMATICALLY at the end of this workflow. Do not skip.

```text
"DUAL LOG:
1. AG_Output/Logs/AG_Activity_Log_YYYYMM.csv:
   [timestamp], audit, [scope], [findings_count], [pass/warn/fail], [output_file]

2. logs/kaizen/pms_usage.csv:
   Timestamp, BSCaudit, Duration, Outcome, Issues, Suggestion"
```

---

## Quick Reference

### Audit types

| Type | Scope | Frequency | Source |
|------|-------|-----------|--------|
| Process | Quy trình nội bộ | Ad-hoc | Chairman request |
| Compliance | Pháp luật/UBCKNN | Quarterly | Regulatory calendar |
| Governance | NQ execution | Post-meeting | /BSCboard data |
| Financial | Chi phí/ngân sách | Quarterly | TCKT data |

### Severity levels

| Level | Meaning | Response |
|-------|---------|----------|
| ✅ Compliant | Meets all requirements | No action needed |
| ⚠️ Needs improvement | Minor gaps, no violation | Recommend fix, track |
| ❌ Non-compliant | Violation found | MANDATORY fix + re-audit |

### Cross-workflow

| From/To | Purpose |
|---------|---------|
| ← `/BSCboard` | NQ action items, completion rate |
| ← `/BSCwatch` | Reporting compliance data |
| → `/BSCdraft BC` | Generate audit report |
| → `/BSCboard` | Report findings to HĐQT |

### Invoke: `/BSCaudit [department/process]`
