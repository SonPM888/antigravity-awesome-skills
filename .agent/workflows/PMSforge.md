---
description: Meta-Automation Factory - Turn manual/repetitive tasks into permanent tools, scripts, or skills
---

// turbo-all

# PMSforge — Meta-Automation Factory

> Run when Chairman identifies a manual/repetitive task that should be automated permanently.
> Typical trigger: /PMSkaizen finds Friction/Waste, or Chairman says "I keep doing X by hand".
> Output: A working script, skill, or workflow that eliminates the manual work forever.

---

## Step 1: Task Intake (Chairman describes the pain)

```text
"Chairman has invoked /PMSforge. 

Chairman, describe the manual task you want to automate:
1. What do you do? (step by step)
2. How often? (daily / per project / per video / etc.)
3. Where? (which folders, tools, apps involved)

Example: 'Every time I render a video, I manually copy files from output/ to archive/, 
rename them with the date, then update a spreadsheet.'"
```

[HARD STOP] Wait for Chairman to describe the task.

**Output**: Chairman provides the manual workflow description.

---

## Step 2: Analysis & Blueprint (Agent designs the tool)

```text
"Analyze Chairman's manual workflow. Use <thinking> to process internally.

Inside <thinking>:
1. DECOMPOSE: Break the manual task into atomic steps.
2. CLASSIFY each step:
   - FILE_OP (copy, move, rename, delete)
   - DATA_OP (read CSV, update spreadsheet, parse text)
   - API_OP (call external service, web request)
   - DECISION (requires human judgment — CANNOT automate)
3. IDENTIFY the automation type:
   - SCRIPT: One-off Python/Bash script (for simple file/data ops)
   - SKILL: Reusable .agent/skills/ module (for complex, multi-step ops)
   - WORKFLOW: New /PMS slash command (for ops that need Chairman interaction)
   - HYBRID: Script + Workflow trigger

Close </thinking>. Present the blueprint to Chairman:

### 🔨 FORGE BLUEPRINT

**Task:** [1-line summary of what Chairman described]
**Frequency:** [how often this runs]
**Automation Type:** [SCRIPT / SKILL / WORKFLOW / HYBRID]

**Steps to Automate:**
| # | Manual Step | Auto Method | Can Automate? |
|---|------------|-------------|---------------|
| 1 | [step]     | [how]       | ✅ / ❌ (needs human) |
| 2 | [step]     | [how]       | ✅ / ❌ |
| ...| ...       | ...         | ... |

**Option 1: [Full Auto]** — [Description] — Pros / Cons / Risk
**Option 2: [Semi Auto]** — [Description] — Pros / Cons / Risk  
(Option 2 keeps human-in-the-loop for steps marked ❌)

Chairman, pick an option. Or adjust the scope."
```

[HARD STOP] Wait for Chairman to pick.

**Output**: Blueprint approved → Agent proceeds to build.

---

## Step 3: Build & Register

```text
"Build the approved automation. Follow these rules strictly:

1. CODING STANDARDS (from Global Instructions):
   - Python 3.10+, UTF-8 encoding, pathlib.Path, logging module (no print).
   - Narrow exceptions only. snake_case functions, PascalCase classes.
   - File naming: [YYYYMMDD]_[Context_Tag]_[Description]_[Version].py

2. WHERE TO SAVE (based on automation type):
   - SCRIPT → save to project's `scripts/` folder.
   - SKILL → save to `.agent/skills/[skill_name]/SKILL.md` + supporting files.
   - WORKFLOW → save to `.agent/workflows/[PMSname].md`.

3. MUST INCLUDE:
   - Docstring explaining what it does, inputs, outputs.
   - Error handling with logging (narrow exceptions).
   - A '--dry-run' flag or confirmation prompt for destructive operations.

4. DEPENDENCIES (if any new packages needed):
   - Auto-update `requirements.txt` (or instruct Chairman to `pip install`).
   - Do NOT silently import uninstalled packages.

5. REGISTER THE TOOL:
   - Update project README.md: add the new tool to 'Available Tools/Scripts' section.
   - If SKILL: ensure SKILL.md has proper YAML frontmatter (name, description).
   - If WORKFLOW: ensure .md has proper YAML frontmatter (description).

6. TEST (SANDBOXED):
   - MUST create a temporary `tmp_test/` folder and generate dummy files/data inside it.
   - Run the tool ONLY on `tmp_test/`. NEVER test on real project files.
   - Show Chairman the output.
   - If PASS → delete `tmp_test/` and confirm registration.
   - If FAIL → fix and retest (max 3 attempts, then escalate).

Show Chairman:
- The created file(s) and their locations.
- A test run result.
- How to invoke it next time."
```

**Output**: Working tool + test result + usage instructions.

---

## Step 4: Verify & Log

```text
"Final checklist (run internally):

[ ] Tool runs without errors on test data?
[ ] Docstring and comments present?
[ ] Error handling implemented (no bare except)?
[ ] Registered in README.md or SKILL.md?
[ ] No hardcoded paths or secrets?
[ ] '--dry-run' or confirmation for destructive ops?

If all PASS → Tell Chairman:
'Tool forged successfully. Here is how to use it: [usage instruction].
Estimated time saved: [X manual steps] eliminated per [frequency].'

If tool is a new /PMS command → Remind Chairman:
'Add this to the WORKFLOW ROUTER in Global Instructions:
- IF [trigger condition] → Suggest: /[new command]'

Log to docs/CHANGELOG.md:
[YYYY-MM-DD HH:MM] [FORGE] Created [tool type]: [name] — [1-line description]"
```

**Output**: Chairman gets a working, registered, tested tool.

---

## Auto-Log

> Agent runs this AUTOMATICALLY at the end of this workflow. Do not skip.

```text
"Append one line to logs/kaizen/pms_usage.csv (create with header if missing):
Timestamp, Workflow, Duration, Outcome, Issues, Suggestion

Also append to logs/kaizen/kaizen_log.csv:
[Timestamp], Win, 'Forged [tool name]: [description]', H, '[manual steps eliminated]'"
```

---

## Quick Reference

| Input | Output |
| --- | --- |
| "I keep copying files manually" | Python script in `scripts/` |
| "I repeat these 5 steps every project" | Skill in `.agent/skills/` |
| "I need a new slash command for X" | Workflow in `.agent/workflows/` |

### Invoke: `/PMSforge [Describe the manual task you want to automate]`
