---
description: End-of-day shutdown - Save state, commit, prepare handover for next session
---

// turbo-all

# PMSquit — End-of-Day Shutdown

> Run at the END of each work session before closing.
> Saves your exact position so tomorrow's /PMSdaily picks up seamlessly.
> NOTE: PMSaudit does NOT include Kaizen logging. Always run /PMSquit at end of day.

---

## Step 1: Session Summary (Agent auto-generates)

```text
"Session ending. Generate a complete shutdown report:

1. WHAT GOT DONE — bullet points of completed tasks.
   MUST use ROADMAP Task IDs: 'Completed S1.3: meta_pipeline.py orchestrator'
   (not generic descriptions like 'worked on pipeline')
2. WHAT'S IN PROGRESS — any task started but not finished.
   Include: Task ID, which file, what was the last change, what's left to do.
3. WHAT'S NEXT — Read ROADMAP.md, find current sprint/milestone.
   List the SPECIFIC next unchecked task from ROADMAP. Include:
   - Sprint name + number (e.g. Sprint 1 'First Real Video')
   - Task ID (e.g. 'S1.3: meta_pipeline.py')
   - File to open first
4. ISSUES DISCOVERED — any bugs, blockers. MUST state ROOT CAUSE (First Principles) if known, not just symptoms.
5. DECISIONS PENDING — anything that needs Chairman's thinking overnight.
6. SYSTEMATIZATION (Gates-style) — Did any manual workflow succeed today? Propose turning it into a new Slash Command.
7. LESSON LEARNED (1 line) — anything useful discovered today that's worth remembering.

Write to docs/PROGRESS.md with format:
   ## [Date] — Session End
   [above content]

Keep it concise. Max 30 lines."
```

**Output**: `docs/PROGRESS.md` updated with session-end entry.

---

## Step 2: Git Commit

```text
"Check for ALL uncommitted changes AND Session Hygiene:
1. HYGIENE: Check for temp files (`.tmp`), massive logs, or stray files. Ask Chairman to delete them or add to `.gitignore`.
2. Run 'git status' — check for both modified AND untracked files.
3. If untracked files exist → ask Chairman:
   'These files are new and not tracked by git: [list].
    1. Add and commit all
    2. Add some, ignore others (I'll list which)
    3. Ignore all for now'
4. If modified files exist → propose commit(s). MUST use format: `type: short description` (feat, fix, refactor, docs, chore, test).
5. If nothing to commit → tell Chairman 'All committed, nothing pending.'

Do NOT leave uncommitted or untracked work overnight."
```

**Output**: Commits proposed → Chairman approves → Agent commits.

---

## Step 3: Tomorrow's Briefing Card

```text
"Create a briefing card for the next session's /PMSdaily to read.
Append to the PROGRESS.md session-end entry:

   ### Next Session Briefing
   - **Current sprint**: [Sprint N: 'Name'] — [X of Y tasks done]
   - **Next task**: [Sprint N.X: description — estimated Xh]
   - **File to open**: [specific file path to start working on]
   - **Resume from**: [file/task in progress, or 'Fresh start']
   - **Blockers to check**: [any, or 'None']
   - **Suggest audit?**: Yes (milestone nearly done) / No

Also update ROADMAP.md Quick Status header (if exists):
   - **Last Session**: [date + time] — [1-line summary]

If Chairman worked on multiple workspaces today, remind:
'You also worked on [other projects] today — run /PMSquit there too if you haven't.'

This is what /PMSdaily will read first thing tomorrow."
```

**Output**: Briefing card appended → Ready for next session.

---

## Step 4: Shutdown Confirmation

```text
Agent tells Chairman:

"✅ Session saved. Summary:
- [X] tasks completed, [Y] in progress
- Git: [committed / nothing to commit]
- Lesson: [1-line takeaway from today]
- Next session: start with /PMSdaily
- Top priority tomorrow: [task name]

Safe to close. See you next time."
```

**Output**: Chairman reads confirmation → Closes IDE.

## Auto-Capture: Kaizen + Log

> Agent runs this AUTOMATICALLY after Step 4. Chairman does NOT need to do anything.

```text
"STEP A — KAIZEN SELF-REVIEW:
Review this entire session objectively. Ask yourself:

1. REWORK — How many times did Chairman correct my output or ask me to redo?
   (count: 0 = great, 1-2 = normal, 3+ = problem)
2. FRICTION — What took longer than expected? Any clunky steps?
3. WASTE — Did I do anything unnecessary? Over-explain? Ask pointless questions?
4. WINS — What went smoothly? What should be repeated?
5. TOOLS — Did I use the best tool for each task? Faster/cheaper alternative?

Append to logs/kaizen_log.csv (create with header if missing):
Timestamp, Type, Description, Impact(H/M/L), Suggestion
- One row per finding. Type: Rework / Friction / Waste / Win / Tool.
- Be honest and specific. Max 10 words per field.

STEP B — USAGE LOG:
Append one line to logs/pms_usage.csv (create with header if missing):
Timestamp, Workflow, Duration, Outcome, Issues, Suggestion

STEP C — RETRO CHECK (every 20 pms_usage entries):
If logs/pms_usage.csv has 20+ new entries since last retro (or never done):

1. ANALYZE both CSVs (pms_usage + kaizen_log):
   - Which workflow has most ISSUE outcomes?
   - Which kaizen Type (Rework/Friction/Waste) appears most?
   - Any pattern repeating 3+ times?
   - Which workflow takes the longest on average?

2. REPORT to Chairman:

   | Insight | Detail |
   |---------|--------|
   | Most problematic workflow | [name] — [X] issues out of [Y] runs |
   | Top recurring friction | [description] — happened [N] times |
   | Rework rate | [X] corrections per session on average |
   | Top suggestion | [most repeated suggestion] |

3. PROPOSE 1-3 changes. ALWAYS propose options using this format:
   'Option N: [Action] — [Pros] / [Cons] / [Risk level]' (Recommend Option 1).

4. If approved → agent edits workflow directly and logs to pms_usage.csv.

If less than 20 new entries → skip retro, just do Steps A + B."
```

---

## Quick Reference

### Daily rhythm (complete)

```text
Open IDE  →  /PMSdaily  →  Work  →  Milestone?  →  /PMSaudit
                                         ↓
                                    /PMSquit (includes kaizen)  →  Close IDE
```

### Invoke: `/PMSquit`
