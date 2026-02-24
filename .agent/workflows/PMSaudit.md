---
description: Project checkpoint workflow - Audit, Roadmap, Git Commit after each milestone
---

// turbo-all

# PMSaudit — Project Milestone Checkpoint

> Run after major milestones or at the end of long work sessions.
> Universal: works across any project and workspace.
> Agent acts as System Architect — unified assessment in one pass.

---

## Phase 1: Assessment (System Architect)

```text
"Act as System Architect. Execute a unified checkpoint assessment covering Progress, Tech, Quality, and Planning.
You will write ONE consolidated report to `docs/MILESTONE_[Date].md`.

1. PROGRESS SUMMARY:
   - Tasks completed this session.
   - Files added/modified/deleted.

2. TECHNICAL AUDIT (Pass/Warn/Fail):
   - LOGGING / ERROR HANDLING: Narrow exceptions? Valid logger?
   - SECURITY: No exposed secrets? API fallbacks active?
   - HYGIENE: No unauthorized temp files?
   - AUTOMATION: Repetitive tasks identified for /PMSkaizen?

3. QUALITY AUDIT (Pass/Warn/Fail):
   - FIRST PRINCIPLES (Root Cause): Did we solve the disease or just the symptoms?
   - MODULARITY: Is logic properly decoupled?
   - I/O MATCHING: Valid input/output formatting?

4. CEO ROADMAP & DIAGNOSIS:
   - What is the immediate Status?
   - List completed milestones.
   - Define Next Steps (3-5 top priority tasks).
   - DECISION MAKING: For Risks & Mitigations, ALWAYS propose options using this format:
     'Option N: [Action] — [Pros] / [Cons] / [Risk level]' (Recommend Option 1).
   - HANDLING FAILS: If any Audit items failed, create a mandatory Fix Task before moving forward.

Write the entire assessment to `docs/MILESTONE_[Date].md`.

5. SYNC ROADMAP (MANDATORY):
   - ARCHIVE FIRST: Copy current `docs/ROADMAP.md` to `docs/archive/ROADMAP_[YYYY-MM-DD].md` (create `docs/archive/` if missing).
   - Then update `docs/ROADMAP.md` to reflect the CEO's Next Steps above.
   - Mark completed milestones as [x].
   - Add new tasks from the assessment.
   - This ensures /PMSdaily reads the latest plan tomorrow.

6. SYNC ALL DOCS (MANDATORY after every audit):
   a. README.md — Update the Status line at top with:
      current version, test count, milestone count, current sprint name.
   b. BUGS.md — If audit found issues:
      - WARN/FAIL → add to 'Known Issues' section with sprint fix target
      - Resolved items → move to 'Resolved Bugs' with date
   c. ROADMAP.md Quick Status header — Update (or create if missing):
      ## 0. QUICK STATUS
      - **Current Sprint**: [Sprint N 'Name'] — [X of Y tasks done]
      - **Next Task**: [task ID + description]
      - **Last Audit**: [date] — [PASS/WARN/FAIL summary]
      - **Blockers**: [any, or 'None']
   d. PROGRESS.md — Already logged via MILESTONE ✅

Submit to Chairman for approval."
```

**Output**: `docs/MILESTONE_[Date].md` → Awaiting Chairman approval.

---

## Phase 2: Git Commit

```text
"Propose git commits for current changes.
- English messages, format: type(scope): description
  Example: feat(srt): add error handling for missing subtitle files
- Split large changes into multiple small commits.
- List all proposed commits for my approval before executing."
```

**Output**: Commit list → Chairman approves → Agent executes.

---

## Phase 3: Chairman Review

```text
Pick one:

(A) "LGTM. Commit and continue per roadmap."
(B) "Adjust: [specific changes]. Update MILESTONE.md and resubmit."
(C) "Pause. Commit current state."
(D) "Done for today. Commit, log, and shut down."
    → Agent commits. Safe to close IDE. (Run /PMSquit to execute Kaizen logging next session).
```

---

## Definition of Done

A milestone is COMPLETE only when ALL of the following are true:

| Criteria | Required |
| --- | --- |
| Code runs without errors | ✅ |
| README.md reflects current state | ✅ |
| Git committed | ✅ |
| MILESTONE_[Date].md logged | ✅ |
| No unresolved FAIL in audit | ✅ |
| Task checklist updated | ✅ |

---

## Rollback (when audit has FAIL)

```text
FAIL found → Fix task created in MILESTONE.md → Agent fixes & writes test/log to prove regression prevention →
Re-audit ONLY the failed item → PASS: continue | Still FAIL: escalate to Chairman
```

## Quick Reference

### When to run?

| Situation | Phases |
| --- | --- |
| Completed a major feature | Full 1→3 |
| End of long session | 1 + 2 (or pick D in Phase 3) |
| Feeling lost / off track | 1 |
| Just want to save progress | 1 + 2 |
| Audit then go home | Full 1→3, pick (D) |
| After fixing a FAIL | Re-audit failed item |

### Invoke: `/PMSaudit`

### Output files

| File | Content | Author |
| --- | --- | --- |
| `docs/MILESTONE_[Date].md` | Consolidated Audit, Progress, & Roadmap | System Architect |

### Git commit types

```text
feat(scope):     New feature
fix(scope):      Bug fix
refactor(scope): Restructure without changing logic
docs(scope):     Documentation update
chore(scope):    Cleanup, config, CI/CD
```
