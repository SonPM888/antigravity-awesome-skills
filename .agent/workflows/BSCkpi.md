---
description: Department performance evaluation - collect KPIs, analyze, compare, report to HĐQT/Ban TGĐ
---

// turbo-all

# BSCkpi — Đánh giá hiệu quả bộ phận

> Collect department reports → extract KPIs → analyze → compare → report
> Cross-links: /BSCwatch (reporting data), /BSCdraft (output report), /BSCboard (HĐQT reporting)

---

## Step 1: Data Collection

```text
"Collect performance data:

1. CHECK /BSCwatch reporting tracker:
   - Which departments have submitted reports this period?
   - Any missing? → Flag to Chairman before proceeding

2. SCAN SharePoint + email for department reports (monthly/quarterly/annual)

3. EXTRACT KPIs per department:
   | Category | Metrics |
   |----------|---------|
   | Financial | Revenue, cost, profit margin, fee income |
   | Business | Market share, trading volume, new accounts |
   | Risk | VaR, NPL ratio, margin utilization |
   | HR | Headcount, turnover, training completion |
   | Project | Completion rate, on-time delivery |
   | Compliance | Audit findings, regulatory penalties |

4. BUILD comparison table: this period vs previous period vs target

ERROR HANDLING:
- If department data incomplete → flag specific gaps
- If format inconsistent → normalize + note assumptions
- If no data available → mark N/A, DO NOT fabricate

Present collected data summary to Chairman."
```

[HARD STOP] Chairman confirms data is sufficient before analysis.

---

## Step 2: Analysis Dashboard

```text
"Generate KPI dashboard:

╔══════════════════════════════════════════════════╗
║ 📊 BSC KPI DASHBOARD — [Period]                 ║
╠══════════════════════════════════════════════════╣
║ Department    | Target | Actual | %   | Trend   ║
║ ─────────────+────────+────────+─────+──────── ║
║ [dept 1]      | [T]    | [A]    | [%] | [↑↓→]  ║
║ ...           | ...    | ...    | ... | ...     ║
╠══════════════════════════════════════════════════╣
║ 🔴 Underperform: [list with root cause]         ║
║ 🟢 Outperform: [list — what went right?]        ║
║ ⚠️ Watch: [trending down but still OK]          ║
╚══════════════════════════════════════════════════╝

For underperforming departments, provide:
  Option 1: [corrective action] — Pros / Cons / Risk
  Option 2: [alternative action] — Pros / Cons / Risk

Cross-department insights:
- Any correlation between departments? (e.g., Brokerage up + Risk up)
- Period-over-period trend analysis
- Benchmark vs industry average (if data available)"
```

[HARD STOP] Chairman reviews analysis before report generation.

---

## Step 3: Report & Distribute

```text
"Generate evaluation report:

1. CREATE report using BSC template (or invoke /BSCdraft BC)
   Naming: [YYYYMMDD]_AG_Report_KPI_[Period]_v1.xlsx

2. INCLUDE sections:
   - Executive summary (1 page)
   - Department scorecards (detail)
   - Trend analysis (charts if possible)
   - Recommendations with Options format
   - Action items for underperforming departments

3. [HARD STOP] Chairman review → approve

4. If sending to Ban TGĐ/HĐQT:
   - Draft email + attach report
   - Chairman approves → send

5. ARCHIVE to AG_Output/Reports/"
```

---

## State Management (Blockchain/Ledger)

> Agent runs this AUTOMATICALLY. Do not skip.

```text
"APPEND to BSC_STATE.json ledger[]:
{
  'seq': [next_seq],
  'timestamp': '[ISO 8601]',
  'type': 'kpi_snapshot',
  'action': 'evaluation_completed',
  'workflow': 'BSCkpi',
  'data': {
    'period': '[Q1/2026]',
    'departments_evaluated': [N],
    'underperformers': ['[dept1]', '[dept2]'],
    'top_performers': ['[dept1]'],
    'overall_score': '[X/10]',
    'report_path': '[file location]',
    'data_source_ref': [BSCwatch ledger seq if used]
  },
  'note': '[key finding summary]'
}

UPDATE quick_status.last_updated

IMMUTABILITY RULE:
- Each evaluation period creates its OWN entry (never overwrites previous)
- Historical comparison = read previous kpi_snapshot entries from ledger
- Full trend analysis possible by querying all type='kpi_snapshot' entries"
```

---

## Auto-Log

> Agent runs this AUTOMATICALLY at the end of this workflow. Do not skip.

```text
"DUAL LOG:
1. AG_Output/Logs/AG_Activity_Log_YYYYMM.csv:
   [timestamp], kpi_evaluation, [period], [departments_count], [output_file], [status]

2. logs/kaizen/pms_usage.csv:
   Timestamp, BSCkpi, Duration, Outcome, Issues, Suggestion"
```

---

## Quick Reference

### Evaluation periods

| Period | Typical deadline | Source |
|--------|-----------------|--------|
| Monthly | T+10 ngày | Department reports via /BSCwatch |
| Quarterly | Q+15 ngày | Aggregated from monthly |
| Annual | Y+30 ngày | Full year review |

### KPI categories

| Category | Key metrics |
|----------|-----------|
| Financial | Revenue, margins, ROE |
| Business | Volume, market share |
| Risk | VaR, NPL, concentration |
| HR | Headcount, turnover |
| Compliance | Audit score, penalties |

### Cross-workflow

| From/To | Purpose |
|---------|---------|
| ← `/BSCwatch` | Reporting compliance data |
| → `/BSCdraft BC` | Generate formal report |
| → `/BSCboard` | Report to HĐQT |

### Invoke: `/BSCkpi [period: Q1/2026]`
