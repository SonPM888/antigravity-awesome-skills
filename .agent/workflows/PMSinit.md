---
description: Initialize a new project with standard folder structure, README, git, and roadmap
---

// turbo-all

# PMSinit — New Project Setup

> Run once when starting a brand-new project.
> Chairman only needs to answer simple questions and pick options.
> Agent handles all technical decisions internally.

---

## Step 1: Project Brief (Chairman answers)

```text
"I'm starting a new project.

Answer these for me:

Q1. Project name?
Q2. What does this project do? (1-2 sentences is enough)
Q3. Project type — pick one:
    1. Python / automation script
    2. YouTube content pipeline (video, subtitle, footage)
    3. Research & analysis (stocks, market, data)
    4. Office document management
    5. Web application
    6. Other: [describe]
Q4. Will this project grow over time, or is it a one-time thing?
    1. Will grow (need archive, versioning)
    2. One-time (keep it simple)

That's it. I'll handle the rest."
```

**Output**: Chairman provides 4 answers → Agent takes over.

---

## Step 2: Agent Creates Everything

> Agent runs this internally — Chairman just waits.

```text
"Based on Chairman's answers, do ALL of the following:

A. FOLDER STRUCTURE
   - Create only the folders this project actually needs.
   - Use internal checklist:
     [ ] src/ — if project has code
     [ ] docs/ — always
      [ ] docs/archive/ — ALWAYS (ROADMAP version history)
     [ ] data/ — if project uses data/media/assets
     [ ] logs/ — if project generates logs
     [ ] logs/kaizen/ — ALWAYS (PMSkaizen CSV metrics)
     [ ] archive/ — if Chairman said 'will grow'
     [ ] config/ — if multiple config files needed
     [ ] tests/ — if project has testable code

B. STARTER FILES & SECURITY
   - Use internal checklist:
     [ ] .gitignore — MUST create immediately. Auto-detect project type AND always include: `.env`, `.tmp`, `__pycache__/`, `logs/`.
     [ ] .env.example — if project uses API keys or secrets. NEVER COMMIT REAL KEYS.
     [ ] README.md — project name, purpose, folder structure.
         -> MUST append this section: '## Core Rules: Python (UTF-8 only, narrow exception handling, pathlib over os.path).'
     [ ] src/utils/logger.py — IF Python project (1, 2, 3), create a standard logger using `logging` module (no prints alloweds).
     [ ] docs/ROADMAP.md — initial roadmap (CEO role: 3-5 first tasks)
     [ ] docs/PROGRESS.md — empty template with header
     [ ] docs/CHANGELOG.md — project changelog (append-only)

C. COPY PMS SYSTEM
   - Copy .agent/workflows/ and .shared_workflows/PMSrules.md from current workspace
     to the new project workspace (if different workspace).
   - If same workspace, skip this step.

D. VERIFY AND COMMIT
   Verify the new project setup. Run this checklist internally:
   [ ] All proposed folders exist?
   [ ] .gitignore exists AND explicitly blocks `.env` and `.tmp`?
   [ ] README.md contains: project name, purpose, folder structure, and Core Rules?
   [ ] (If Python) `src/utils/logger.py` created?
   [ ] docs/ROADMAP.md has 3-5 initial tasks with checkpoints?
   [ ] docs/PROGRESS.md exists?
   [ ] No sensitive data committed (.env, API keys)?

   If any item FAILS:
   - Fix it silently.
   - Only tell Chairman if a decision is needed. MUST provide options:
     'Option N: [Action] — [Pros] / [Cons] / [Risk level]' (Recommend Option 1).

   If all PASS:
   - git init
   - git add .
   - Propose initial commit message.

Show Chairman:
1. The created tree structure.
2. The proposed commit message.

[HARD STOP] Wait for Chairman approval before committing."
```
**Output**: Full scaffolding + tree + commit message → Chairman approves.

---

### Logging & Documentation Principles (MUST follow in ALL workflows)

> These rules apply across all PMS workflows to maintain the Single Source of Truth.

- **Append-only**: When updating logs or trackers, create new entries. NEVER delete or modify old entries.
- **Standardized format**: Every entry uses `[YYYY-MM-DD HH:MM] [TYPE] Description`
- **TYPE tags**: `[INIT]`, `[AUDIT]`, `[CLEANUP]`, `[REFACTOR]`, `[FEAT]`, `[FIX]`, `[HOTFIX]`, `[DEPLOY]`, `[DAILY]`
- **Audit reports**: Save as separate files `audit_NNN_[milestone].md` in `docs/`
- **Kaizen data**: CSV files saved to `logs/kaizen/`
- **Artifacts**: Any audit report, plan, or decision doc goes in `docs/` with sequential numbering
- **Git reference**: Every entry that changes code MUST include the commit hash

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

### Project type → suggested folders

| Type | Folders |
| --- | --- |
| Python / automation | `src/`, `docs/`, `logs/`, `config/`, `tests/` |
| YouTube pipeline | `src/`, `docs/`, `data/`, `logs/`, `archive/` |
| Research & analysis | `docs/`, `data/`, `logs/`, `archive/` |
| Office document mgmt | `docs/`, `data/`, `archive/` |
| Web application | `src/`, `docs/`, `config/`, `tests/` |

### After init, daily rhythm

```text
/PMSinit (once) → /PMSdaily (every session) → /PMSaudit (every milestone)
```

### Invoke: `/PMSinit`
