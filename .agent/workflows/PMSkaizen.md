---
description: Continuous improvement engine - Analyze workflow data, find problems, propose fixes
---

// turbo-all

# PMSkaizen — Continuous Improvement Engine

> Data is collected AUTOMATICALLY by /PMSquit and /PMSaudit.
> /PMSdaily will notify Chairman when enough data has accumulated.
> Chairman just runs /PMSkaizen and picks options from the report.
>
> Philosophy:
> - Elon Musk: Question → Delete → Simplify → Accelerate → Automate
> - Bill Gates: Measure → Systematize → Automate efficient operations

---

## Step 1: Data Health Check

```text
"Check data availability:
1. Read logs/kaizen/kaizen_log.csv — count entries since last RETRO row.
2. Read logs/kaizen/pms_usage.csv — count total entries.

If kaizen_log has < 5 new entries since last RETRO → tell Chairman:
'Not enough new data. Need [X] more sessions. Keep working, come back later.'
→ Stop here.

If >= 5 new entries → proceed."
```

---

## Step 2: Generate Kaizen Report

> Agent generates the full report internally, shows Chairman the final result only.

```text
"Analyze BOTH CSVs in logs/kaizen/ (kaizen_log.csv + pms_usage.csv). Generate report:

PART 1 — FREQUENCY TABLE:
Count each kaizen Type:

   | Type | Count | % | Most common example |
   |------|-------|---|---------------------|
   | Rework | [n] | [%] | [description] |
   | Friction | [n] | [%] | [description] |
   | Waste | [n] | [%] | [description] |
   | Win | [n] | [%] | [description] |
   | Tool | [n] | [%] | [description] |

PART 2 — TOP 3 PROBLEMS (sorted by estimated weekly waste):
For each, apply Elon's 5-step internally, then present:

   ╔══════════════════════════════════════════════════╗
   ║ 🔍 KAIZEN REPORT — [Date]                        ║
   ║ Data: [N] observations from [X] sessions          ║
   ╠══════════════════════════════════════════════════╣
   ║                                                    ║
   ║ #1: [Problem] — Occurred [N] times this cycle     ║
   ║     Root Cause (First Principles): [Tại sao?]     ║
   ║     Option 1: [Action] — [Pros] / [Cons] / [Risk]  ║
   ║     Option 2: [Action] — [Pros] / [Cons] / [Risk]  ║
   ║                                                    ║
   ║ #2: [Problem] — Occurred [N] times this cycle     ║
   ║     Root Cause (First Principles): [Tại sao?]     ║
   ║     Option 1: [Action] — [Pros] / [Cons] / [Risk]  ║
   ║     Option 2: [Action] — [Pros] / [Cons] / [Risk]  ║
   ║                                                    ║
   ║ #3: [Problem] — Occurred [N] times this cycle     ║
   ║     Root Cause (First Principles): [Tại sao?]     ║
   ║     Option 1: [Action] — [Pros] / [Cons] / [Risk]  ║
   ║     Option 2: [Action] — [Pros] / [Cons] / [Risk]  ║
   ║                                                    ║
   ╠══════════════════════════════════════════════════╣
   ║ TREND: [↑ Better / → Same / ↓ Worse]              ║
   ║ compared to previous period                        ║
   ║                                                    ║
   ║ 🏆 WINS TO KEEP:                                   ║
   ║ 1. [thing that's working well]                     ║
   ║ 2. [thing that's working well]                     ║
   ╠══════════════════════════════════════════════════╣
   ║ Chairman: Pick fixes to implement.                 ║
   ║ Reply: '1.Option1, 2.Option2, 3 skip' or similar ║
   ╚══════════════════════════════════════════════════╝

PART 3 — SOLUTION RESEARCH (for each proposed fix):
If solution involves new tools or approaches:
- Search GitHub, free tools, market solutions.
- Compare: current approach vs proposed (time, cost, quality).
- Only recommend: free/cheap, maintained, proven.

Solution types to consider:
- NEW WORKFLOW — create a new PMS workflow
- FIX WORKFLOW — modify existing [name]
- NEW TOOL — [specific tool/repo/service]
- NEW MODEL — switch AI model (cheaper/faster/better)
- AUTOMATE — write a script to handle repetitive task
- DELETE — stop doing this entirely

Wait for Chairman to pick options.

[HARD STOP] Wait for Chairman to reply before implementing."
```

**Output**: Full report → Chairman replies: `1.Option1, 2.Option2, 3 skip` (or similar).

---

## Step 3: Implement Approved Fixes

```text
"For each fix Chairman approved:

1. EXECUTE the change:
   - If NEW/FIX WORKFLOW → edit/create the .md file.
   - If NEW TOOL → install and configure (ask Chairman if cost involved).
   - If AUTOMATE → write the script.
   - If DELETE → remove the step from workflow.

2. LOG the change to logs/kaizen/kaizen_log.csv:
   [Timestamp], Improvement, '[what changed]', H, '[workflow/tool affected]'

3. SET CHECKPOINT — after 5 sessions, agent will auto-compare:
   Before: [old metric from CSV data]
   After: [new metric]
   Verdict: Effective / No change / Made worse
   → Log verdict to logs/kaizen/kaizen_log.csv

Tell Chairman: 'Changes applied. Will track effectiveness over next 5 sessions.'"
```

**Output**: Changes implemented + tracking set.

---

## Step 4: Archive Report

```text
"Save this report to logs/kaizen/kaizen_NNN_YYYYMMDD_report.md:
- Append-only: NEVER overwrite existing reports.
- Include: problems found, solutions chosen, pending checkpoints.
- This creates a history of all improvements over time.

Also append a CHANGELOG entry to docs/CHANGELOG.md:
[YYYY-MM-DD HH:MM] [KAIZEN] Kaizen Report #[N] — [summary of improvements]

Mark this analysis as RETRO in logs/kaizen/pms_usage.csv:
[Timestamp], RETRO, [duration], OK, '[N] improvements approved', 'Report #[N]'"
```

---

## Auto-Log

> Agent runs this AUTOMATICALLY at the end of this workflow. Do not skip.

```text
"Append one line to logs/kaizen/pms_usage.csv (create with header if missing):
Timestamp, Workflow, Duration, Outcome, Issues, Suggestion"
```

---

## Quick Reference

### How the system works (Chairman does NOTHING except pick options)

```text
              AUTOMATIC                           ON-DEMAND
    ╔════════════════════════╗          ╔═══════════════════════╗
    ║ /PMSquit or /PMSaudit    ║          ║ /PMSkaizen            ║
    ║ → agent self-reviews     ║          ║ → reads accumulated   ║
    ║ → writes kaizen_log.csv  ║    ──→   ║   data                ║
    ║ (Chairman unaware)       ║          ║ → generates report    ║
    ╚════════════════════════╝          ║ → Chairman picks 1A,  ║
                                          ║   2B, 3skip           ║
    /PMSdaily checks:                     ║ → agent implements    ║
    "10+ entries? → recommend"            ║ → tracks results      ║
                                          ╚═══════════════════════╝
```

### Invoke: `/PMSkaizen`
