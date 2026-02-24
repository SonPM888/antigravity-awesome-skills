---
description: Data-driven continuous improvement - collect metrics, detect patterns, propose unbiased kaizen
---

// turbo-all

# BSCkaizen — Continuous Improvement Engine

> Unbiased, data-driven. No opinions — only measurable facts.
> Runs every 2 weeks OR after 20 workflow invocations, whichever comes first.
> Cross-links: reads ALL BSC workflow logs, feeds improvements back to workflows

---

## Data Streams (5 sources — all append-only, immutable)

```
AG_Output/Logs/
├── workflow_log.csv        ← Every workflow invocation
├── decision_log.csv        ← Every Chairman decision at HARD STOP
├── correction_log.csv      ← Every Chairman edit to AG output
├── compliance_log.csv      ← CBTT timelines, reporting deadlines
└── action_tracker.csv      ← HĐQT action items lifecycle
```

> [!CAUTION]
> These logs are **IMMUTABLE**. AG MUST NEVER edit or delete past entries.
> Only append new rows. This ensures audit trail integrity and unbiased analysis.

---

## Step 1: Data Aggregation

```text
"BSCkaizen triggered. Aggregate data from last reporting period:

1. READ all 5 CSV log files
2. FILTER to reporting period (last 2 weeks or last 20 invocations)
3. CALCULATE scoreboard metrics:

   METRIC DEFINITIONS (all measurable, no subjective scoring):

   | Metric | Formula | Target | Source |
   |--------|---------|--------|--------|
   | First-pass rate | drafts_approved_no_revision / total_drafts × 100 | ≥ 80% | decision_log |
   | CBTT compliance | cbtt_sent_within_24h / total_cbtt × 100 | 100% | compliance_log |
   | Action completion | actions_done_on_time / total_actions × 100 | ≥ 90% | action_tracker |
   | Rework rate | drafts_with_change_ratio_gt_0.3 / total_drafts × 100 | ≤ 10% | correction_log |
   | Avg workflow duration | sum(duration_sec) / count(invocations) | Trending ↓ | workflow_log |
   | Report on-time rate | reports_received_on_time / total_expected × 100 | ≥ 90% | compliance_log |

4. COMPARE with previous period (trend: ↑ improving / ↓ declining / → stable)

ERROR HANDLING:
- If < 5 data points for a metric → mark 'Insufficient data'
- If log file missing → create with headers, mark 'No data yet'
- NEVER fabricate or estimate missing data"
```

---

## Step 2: Pattern Detection

```text
"Analyze data for recurring patterns:

1. CLUSTER correction_log by (workflow, doc_type, section_changed):
   - If same cluster appears 3+ times → SYSTEMATIC GAP
   - Calculate avg change_ratio per cluster

2. CLUSTER action_tracker by (department, status):
   - If department has 3+ overdue items → ACCOUNTABILITY ISSUE
   - If same action type repeats → PROCESS GAP

3. CLUSTER workflow_log by (workflow, outcome):
   - If workflow has > 20% ISSUE outcomes → WORKFLOW PROBLEM
   - If workflow avg duration increasing → EFFICIENCY CONCERN

4. CLUSTER decision_log by (option_chosen):
   - Which Options does Chairman consistently pick?
   - Any pattern in rejected Options? → Adjust default recommendations

5. CROSS-STREAM CORRELATION:
   - High rework in BSCdraft + low first-pass → Template quality issue
   - Low compliance + high action overdue → Enforcement gap
   - Frequent BSCboard governance FAIL → Training/process need

BIAS PREVENTION:
- Pattern must appear in 3+ independent data points
- AG reports RAW counts, not interpretations
- Chairman draws conclusions, AG provides evidence"
```

---

## Step 3: Scoreboard & Report

```text
"Generate BSCkaizen Report:

╔══════════════════════════════════════════════════╗
║ 📊 BSC KAIZEN REPORT — [Period]                 ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║ SCOREBOARD (vs previous period):                 ║
║ • First-pass rate:   [X]% (target 80%) [↑↓→]   ║
║ • CBTT compliance:   [X]% (target 100%) [↑↓→]  ║
║ • Action completion: [X]% (target 90%) [↑↓→]   ║
║ • Rework rate:       [X]% (target ≤10%) [↑↓→]  ║
║ • Avg duration:      [X]min [↑↓→]              ║
║ • Report on-time:    [X]% (target 90%) [↑↓→]   ║
║                                                  ║
║ PATTERNS DETECTED ([N] total):                   ║
║ P1: [description] — [N] occurrences             ║
║     Evidence: [log_source, entries]              ║
║ P2: [description] — [N] occurrences             ║
║     Evidence: [log_source, entries]              ║
║                                                  ║
║ STATUS vs TARGETS:                               ║
║ ✅ On target: [list]                             ║
║ ⚠️ Near target: [list]                          ║
║ 🔴 Below target: [list]                         ║
╚══════════════════════════════════════════════════╝

Present to Chairman."
```

[HARD STOP] Chairman reviews scoreboard before proposals.

---

## Step 4: Kaizen Proposals

```text
"For each pattern detected (prioritized by impact):

PROPOSAL FORMAT:
┌─────────────────────────────────────────────┐
│ K[N]: [Short title]                         │
│                                             │
│ Problem:  [description from data]           │
│ Evidence: [log_source], [N] entries,        │
│           [specific data points]            │
│ Impact:   [which metric improves, by how    │
│            much — estimated from data]      │
│                                             │
│ Option 1: [action] — Pros/Cons/Risk         │
│ Option 2: [action] — Pros/Cons/Risk         │
│ Option 3: Do nothing — monitor next cycle   │
└─────────────────────────────────────────────┘

RULES FOR PROPOSALS:
- Max 5 proposals per report (focus > volume)
- Each MUST have measurable expected impact
- Each MUST cite specific log entries as evidence
- 'Do nothing' is always a valid option
- AG does NOT pre-select — Chairman decides

After Chairman decides:
- Approved → AG implements immediately (edit workflow, create template, etc.)
- Rejected → LOG rejection reason (feeds next kaizen cycle)
- Deferred → Add to next cycle backlog"
```

---

## Step 5: Archive & Evolve

```text
"After Chairman review:

1. SAVE report: [YYYYMMDD]_AG_Report_Kaizen_[Period]_v1.md
   Location: AG_Output/Reports/

2. LOG decisions to kaizen_decisions.csv:
   timestamp, proposal_id, title, decision(approved/rejected/deferred), reason, implemented(yes/no)

3. UPDATE targets if Chairman approves:
   - Targets stored in AG_Output/Logs/kaizen_targets.json
   - Can be adjusted based on actual performance data

4. EVOLVE the engine:
   - After 3 cycles: add benchmark comparisons (this quarter vs last)
   - After 6 cycles: add predictive patterns
   - After 12 cycles: annual governance effectiveness report"
```

---

## State Management (Blockchain/Ledger)

> Agent runs this AUTOMATICALLY. Do not skip.

```text
"APPEND to BSC_STATE.json ledger[]:

For each proposal:
{
  'seq': [next_seq],
  'timestamp': '[ISO 8601]',
  'type': 'kaizen_proposal',
  'action': 'proposed',
  'workflow': 'BSCkaizen',
  'data': {
    'proposal_id': 'K[N]',
    'title': '[short title]',
    'evidence_source': '[log file + entry counts]',
    'expected_impact': '[metric + improvement %]',
    'status': 'proposed|approved|rejected|deferred|implemented'
  },
  'note': '[1-line summary]'
}

After Chairman decides:
{
  'seq': [next_seq],
  'timestamp': '[ISO 8601]',
  'type': 'kaizen_decision',
  'action': '[approved|rejected|deferred]',
  'workflow': 'BSCkaizen',
  'data': {
    'ref_seq': [proposal seq number],
    'proposal_id': 'K[N]',
    'decision': '[approved|rejected|deferred]',
    'chairman_reason': '[brief reason]'
  },
  'note': '[implementation plan if approved]'
}

UPDATE quick_status.kaizen_backlog (count approved but not implemented)
UPDATE quick_status.last_kaizen

IMMUTABILITY RULE:
- Proposal → decision → implementation = 3 separate entries
- Rejected proposals stay in ledger (learn from what didn't work)
- Full kaizen history always queryable"
```

---

## Auto-Log

> Agent runs this AUTOMATICALLY at the end of this workflow. Do not skip.

```text
"DUAL LOG:
1. AG_Output/Logs/AG_Activity_Log_YYYYMM.csv:
   [timestamp], kaizen, [period], [metrics_count], [patterns_found], [proposals_made]

2. logs/kaizen/pms_usage.csv:
   Timestamp, BSCkaizen, Duration, Outcome, Issues, Suggestion"
```

---

## Quick Reference

### Trigger conditions

| Trigger | Check |
|---------|-------|
| 2 weeks elapsed | Since last BSCkaizen run |
| 20 workflow invocations | Count in workflow_log.csv |
| Chairman manual | `/BSCkaizen` or `/BSCkaizen Q1/2026` |

### Metrics at a glance

| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| First-pass | ≥ 80% | 60-79% | < 60% |
| CBTT | 100% | 90-99% | < 90% |
| Actions | ≥ 90% | 70-89% | < 70% |
| Rework | ≤ 10% | 11-20% | > 20% |
| Reports | ≥ 90% | 70-89% | < 70% |

### Data integrity rules

| Rule | Detail |
|------|--------|
| Append-only | Never edit/delete past entries |
| Fact-based | Only measurable data, no opinions |
| Minimum sample | 3+ data points to flag pattern |
| Chairman decides | AG proposes, never implements without approval |

### Invoke: `/BSCkaizen` or `/BSCkaizen [period]`
