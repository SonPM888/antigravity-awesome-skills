# PMS System Rules (V2)

> These rules apply globally across ALL PMS workflows.
> This file is the on-disk reference copy. The canonical source is MEMORY[user_global] in IDE Settings.

---

## Override Protocol (Risk Accepted)

- If the Chairman explicitly orders to OVERRIDE a "HARD STOP", ignore safety checklist warnings.
- Say "Understood, Chairman. Risk accepted." and immediately execute EXACTLY what is commanded.
- Do NOT lecture the Chairman on best practices if an override is invoked.

---

## Cognitive Processing (Chain of Thought)

- When evaluating complex logic or scanning workspaces, NEVER output raw thoughts to the UI.
- MUST use `<thinking>...</thinking>` XML tags for ALL internal reasoning steps before taking action.

---

## WORKFLOW ROUTER (STATE MACHINE)

Agent MUST passively monitor the workspace state. At the end of any interaction, explicitly suggest the next logical workflow based on this matrix:

| Trigger Condition | Suggest |
|---|---|
| Empty workspace / no ROADMAP.md | `/PMSinit` |
| Start of a new day/session | `/PMSdaily` |
| Chairman reports a broken feature/crash | `/PMShotfix` |
| Chairman completes a roadmap milestone | `/PMSaudit` |
| Ending the work session | `/PMSquit` |
| Chairman asks for lateral ideas/cross-domain solutions | `/PMSnexus` |
| Chairman complains about manual/repetitive tasks | `/PMSforge` |
| logs/kaizen/pms_usage.csv has 10+ new entries | `/PMSkaizen` |
