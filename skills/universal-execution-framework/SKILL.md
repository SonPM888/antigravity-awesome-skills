---
name: Universal Execution Framework (UEF)
description: A 4-step protocol for complex multi-step tasks. Audits tools, decomposes work, coordinates execution, and enforces quality standards.
---

# UEF Protocol

> This skill is invoked by the agent when handling Tier 3 tasks.
> Tier routing logic lives in each project's `.agent/instructions.md`, NOT here.

## Step 1 — Audit & Route
- Identify which active MCPs are relevant to this task.
- Scan `C:\Users\SonPM\antigravity-awesome-skills\skills\` for specialized skills.
- If a matching skill exists, read its `SKILL.md` before proceeding.
- Announce selected tools/skills to the user before executing.

## Step 2 — Deconstruct
- Break the task into the smallest independent sub-tasks.
- Tag each sub-task as parallelizable or sequential.
- Estimate complexity: if any sub-task is itself multi-step, recurse.

## Step 3 — Execute & Coordinate
- Dispatch sub-tasks to the best-fit tool:
  - `exa-cloud` / `perplexity` → research & fact-checking.
  - `browser_subagent` → live web interaction.
  - `filesystem` → local file read/write.
  - `run_command` → scripts, CLI, build tools.
  - `runware-cloud` → AI image generation.
  - `rube` → YouTube API operations.
- Run independent sub-tasks in parallel where possible.
- After each sub-task completes, verify output before proceeding.

## Step 4 — Quality Gate
- **Compression:** Tighten all text output by ≥10%. Remove fluff.
- **Actionability:** Every output must be ready-to-use, not just informational.
- **Consistency:** Cross-check outputs against project context (`.agent/knowledge/`).
- **Learning:** If a new reusable pattern was discovered, note it for future KI updates.
