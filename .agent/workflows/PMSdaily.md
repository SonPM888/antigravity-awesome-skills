---
description: Daily standup - Review progress, identify today's tasks, flag blockers
---

// turbo-all, YOLO

# PMSdaily — Daily Standup

> Run at the START of each work session.
> Chairman only picks options. Agent handles the rest.
> End-of-session is handled by /PMSquit (or /PMSaudit if milestone done).

---

## Step 1: Context Reload + Briefing

```text
"Start of session. Do the following:

1. CHECK if docs/PROGRESS.md and docs/ROADMAP.md exist.
   - If missing → tell Chairman: 'No project docs found. Run /PMSinit first?' and stop.
   - If exist → continue.

2. If this is a NEW CONVERSATION (no prior context in this chat):
   - State: 'New conversation. Rebuilding context from project files...'
   - Read all docs/ files thoroughly before proceeding.

3. Read: docs/PROGRESS.md (latest entry, especially 'Next Session Briefing' if exists),
   docs/ROADMAP.md, latest docs/MILESTONE_*.md (if exists).

4. WORKSPACE HYGIENE & SECURITY CHECK (MUST use Bash/File tools. Do not hallucinate. Use <thinking> to process):
   - Check git status. Quick scan for exposed API keys or stray temp files (e.g., in Desktop/tmp).
   - Flag warnings if any issues are found.

5. Show briefing in this EXACT table format:

   | Item               | Status                                                   |
   | ------------------ | -------------------------------------------------------- |
   | Last session       | [3-5 bullet points from PROGRESS.md]                     |
   | Hygiene & Security | [Clear, or 'WARNING: [Issue]']                           |
   | Current sprint     | [Sprint N: 'Name'] — [X of Y tasks done]                 |
   | Next task          | [S{N}.{X}: description — estimated Xh]                   |
   | Resume from        | [Task ID + file/task left in progress, or 'Fresh start'] |
   | Blockers           | [any, or 'None']                                         |
   | Open FAIL items    | [from audit, or 'None']                                  |
   | Suggest audit?     | [Yes: milestone nearly done / No]                        |

6. KAIZEN CHECK (MUST use Bash/File tools. Do not hallucinate. Use <thinking> to process):
   - If logs/kaizen/kaizen_log.csv exists and has 10+ entries since last RETRO:
     Add to briefing table: | 📊 Kaizen ready | [N] observations collected. Recommend: /PMSkaizen |
   - Otherwise: skip silently.

7. Then ask Chairman:

   Q1. Focus mode — pick one:
       1. Deep work (1 big task, full focus. Agent works silently, minimal interruptions)
       2. Multi-task (several small tasks, cleanup)
       3. Exploration (research, experiment. Agent MUST use internal tools/APIs first before asking for Browser)

   Q2. Which task to focus on?
       (list top 3 from roadmap for Chairman to pick)

[HARD STOP] Wait for Chairman to pick focus mode and task before proceeding to Step 2."

**Output**: Status table + Chairman picks focus mode and task.

---

## Step 2: Today's Plan

```text
"Based on Chairman's choices, create today's work plan:
- Reference the ROADMAP Task ID (e.g. S1.3) in every sub-step.
- Break the chosen task into 2-4 concrete, testable sub-modules.
- Estimate time for each sub-step.
- DECISION MAKING: If ANY step needs Chairman's decision (design choice, mitigation, setup), you MUST provide options in this format:
  'Option N: [Action] — [Pros] / [Cons] / [Risk level]' (Recommend Option 1).
- If roadmap is completed or outdated → suggest running /PMSaudit.
- If an emergency bug from yesterday needs fixing → suggest /PMShotfix.

Show the plan as a simple numbered list. Wait for Chairman to say 'go'."
```

**Output**: Action plan (with Decision Options if applicable) → Chairman says "go" → Start working.

---

## Auto-Log

> Agent runs this AUTOMATICALLY at the end of this workflow. Do not skip.

```text
"Append one line to logs/pms_usage.csv (create file with header row if missing):
Timestamp, Workflow, Duration, Outcome, Issues, Suggestion
Outcome: OK or ISSUE. Issues and Suggestion: max 10 words each."
```

---

## Quick Reference

### Daily rhythm

```text
Open IDE  →  /PMSdaily  →  Work  →  Milestone?  →  /PMSaudit (includes shutdown)
                                         ↓
                                    /PMSquit  →  Close IDE
```

### Focus modes

| Mode        | Best for                  | Agent behavior                                            |
| ----------- | ------------------------- | --------------------------------------------------------- |
| Deep work   | Big feature, complex task | 1 task only, work silently, report only when done/blocked |
| Multi-task  | Many small fixes, cleanup | Quick progress, brief updates                             |
| Exploration | Research, prototyping     | Flexible, prioritize internal tools over browser          |

### Invoke: `/PMSdaily`
