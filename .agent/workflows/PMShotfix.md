---
description: Emergency bugfix workflow - Find, fix, test, commit fast
---

// turbo-all

# PMShotfix — Emergency Bugfix

> Run when something is broken and needs immediate fixing.
> Fast-track: skip planning overhead, go straight to fix.
> Agent handles debugging. Chairman only approves the commit.
> ITERATION-BOXED: Max 3 tool calls/attempts. If unresolved, escalate to Chairman.

---

## Step 1: Report the Problem (Chairman)

```text
"Something is broken.

Q1. What's wrong? (describe what you see — error message, wrong output, crash, etc.)
Q2. Where? Pick one:
    1. I know which file — [file name or path]
    2. I don't know — agent, find it
Q3. How urgent?
    1. Blocking — can't do anything until fixed
    2. Important — need to fix today
    3. Annoying — works but not right"
```

**Output**: Chairman describes the problem → Agent takes over.

---

## Step 2: Diagnose

> Agent runs this internally — Chairman just waits.
> ITERATION LIMIT: If agent can't find root cause within 3 tool calls,
> stop and ask Chairman: "Can't pinpoint the issue. Options:
> 1. Keep searching (give me 3 more attempts)
> 2. Skip this for now, add to ROADMAP for later
> 3. Describe the problem differently"

```text
"Based on Chairman's report:

1. CLASSIFY the issue:
   - Code bug (logic error, crash, wrong output)
   - Config issue (.env, API key, settings)
   - Missing/corrupted file
   → Pick the fastest diagnosis path based on type.

2. REPRODUCE the bug:
   - Run the failing command/script to confirm the error.
   - If cannot reproduce → ask Chairman for more details.
   - If reproduced → capture the exact error output.

3. LOCATE root cause (First Principles):
   - If Chairman pointed to a file → start there.
   - If not → check logs, git diff (recent changes), error patterns.
   - Trace to exact line/function/config AND EXPLAIN WHY it failed (Root cause analysis, not just symptom patching).

4. REPORT to Chairman (brief):

   | Item | Detail |
   |------|--------|
   | Bug type | Code / Config / File |
   | Root cause | [1 sentence explaining WHY it happened] |
   | Reproduced? | Yes / No |
   | Affected files | [list] |
   | Risk level | Low / Medium / High |

   Provide options for fix:
   Option 1: [Action] — [Pros] / [Cons] / [Risk level] (Safest)
   Option 2: [Action] — [Pros] / [Cons] / [Risk level] (Fastest - if different)

   'Chairman, pick an option. Or say: just fix it (I'll pick the safest).'

[HARD STOP] Wait for Chairman to reply before fixing."
```

**Output**: Diagnosis table + options → Chairman picks.

---

## Step 3: Fix + Test

```text
"Apply the chosen fix:

1. SAFETY NET: Backup the file logically before changing anything (e.g., `cp target.py target.py.bak`).
   → Do NOT use `git stash`. If fix fails, restore with `cp target.py.bak target.py`.

2. FIX & PREVENT REGRESSION:
   - Apply the change.
   - MUST add a `logger` output or `narrow exception` wrapper around the fixed logic so if it breaks again, the log will clearly state what failed.

3. TEST: Run the same reproduce step from diagnosis.
   - PASS → show Chairman the working result.
   - FAIL → restore backup (`cp target.py.bak target.py`), try alternative approach.
   - FAIL twice → escalate to Chairman:
     'Fix didn't work after 2 attempts. Options:
      1. Try a completely different approach
      2. Revert and add to ROADMAP for deeper investigation
      3. Chairman describes a workaround they have in mind'

4. SIDE EFFECTS CHECK:
   - Did the fix break anything else?
   - Related files need updating? (imports, configs, README)

Show Chairman:

   | Item | Status |
   |------|--------|
   | Fix applied | ✅ / ❌ |
   | Test passed | ✅ / ❌ |
   | Side effects | None / [list] |
   | Files changed | [list] |"
```

**Output**: Fix result table → Chairman confirms it works.

---

## Step 4: Commit + Log

```text
"Fix verified. Do the following:

1. Propose git commit:
   - Format: fix(scope): brief description
   - Example: fix(srt): handle missing subtitle file gracefully

2. Log to docs/PROGRESS.md:
   - [HOTFIX] tag + date/time
   - First Principles: What broke, Root Cause (Why?), Fix & Prevention strategy.
   - Files changed
   - Append under '## Hotfix History': Date | Bug type | Root cause | Fix | Files changed
   - This ensures the next /PMSaudit sees all hotfixes.

3. Log to BUGS.md:
   - If RESOLVED: Add entry under 'Resolved Bugs': BUG-NNN | severity | root cause | fix | date
   - If NOT fully fixed: Add to 'Known Issues' with workaround and sprint target
   - Increment bug number from last entry in file

Wait for Chairman to approve commit."
```

**Output**: Commit message → Chairman approves → Done.

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

### When to use /PMShotfix vs normal workflow

| Situation | Use |
| --- | --- |
| Something broken RIGHT NOW | `/PMShotfix` |
| Bug found during audit (not urgent) | Add to ROADMAP, fix in normal flow |
| Want to improve code (not broken) | Normal workflow + `/PMSaudit` |

### Hotfix flow

```text
Report → Classify → Reproduce → Diagnose → Fix + Test → Commit
  ↑                                              ↓
  └──────── Still broken after 2 tries? ─────────┘
            → Escalate to Chairman (revert or defer)
```

### Invoke: `/PMShotfix`
