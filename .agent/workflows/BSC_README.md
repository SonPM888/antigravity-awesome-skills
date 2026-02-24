# BSC Workflow Suite

**AI-powered corporate governance system for BIDV Securities JSC (BSC)**

| | |
|---|---|
| **Platform** | Antigravity IDE + Microsoft 365 |
| **Engine** | Microsoft Graph API via `microsoft-mcp` |
| **Author** | AG (Antigravity AI Assistant) |
| **Owner** | SonPM — Chairman of the Board, BSC |
| **Version** | 1.0.0 |
| **Last updated** | 2026-02-22 |

---

## Table of Contents

1. [What is this?](#what-is-this)
2. [Architecture](#architecture)
3. [Quick Start](#quick-start)
4. [Workflows](#workflows)
5. [Use Cases](#use-cases)
6. [Design Principles](#design-principles)
7. [Capabilities & Maturity](#capabilities--maturity)
8. [Roadmap](#roadmap)
9. [Limitations](#limitations)
10. [Dependencies](#dependencies)
11. [File Structure](#file-structure)

---

## What is this?

A suite of **7 AI workflows + 1 operating policy** that transforms the Antigravity IDE into a corporate assistant for the Chairman of the Board at BSC. It automates the full governance lifecycle:

```
Morning briefing → Board meetings → Document drafting → Information disclosure
                                                              ↕
Reporting compliance ← KPI evaluation ← Internal audit ← Data collection
```

**Key value propositions:**
- ⏰ **CBTT 24h compliance** — countdown timer, multi-channel alerts, incident logging
- 🏛️ **HĐQT governance** — authority validation, BIDV pre-approval, document consistency checks
- 📊 **Department monitoring** — automated report tracking with escalation ladder
- 📝 **Document drafting** — 6 document types using BSC templates learned from SharePoint
- 🔄 **Closed-loop system** — 5 feedback loops with cross-workflow triggers

---

## Architecture

```
                          ┌─────────────────────────────────────────┐
                          │            /BSCbrief (Daily)            │
                          │   Email · Calendar · Teams · Alerts    │
                          └──────┬──────────┬──────────┬───────────┘
                                 │          │          │
                    ┌────────────▼──┐  ┌────▼────┐  ┌──▼──────────┐
                    │  /BSCboard    │  │/BSCwatch│  │/BSCdisclosure│
                    │  HĐQT Meeting │  │Report   │  │CBTT 24h     │
                    │  Governance   │  │Tracking │  │Compliance   │
                    └──┬─────┬─────┘  └────┬────┘  └─────────────┘
                       │     │             │
                  ┌────▼──┐  │        ┌────▼────┐
                  │/BSCdraft│ │        │ /BSCkpi │
                  │Documents│ │        │  KPI    │
                  └────────┘  │        └─────────┘
                              │
                         ┌────▼─────┐
                         │/BSCaudit │
                         │Internal  │
                         │Control   │
                         └──────────┘
                              │
              ┌───────────────▼────────────────┐
              │  DUAL LOG → /PMSkaizen         │
              │  AG_Activity_Log + pms_usage   │
              └────────────────────────────────┘
```

**Cross-workflow triggers:**

| From → To | Condition |
|-----------|-----------|
| `brief` → `board` | HĐQT meeting within 7 days |
| `brief` → `disclosure` | CBTT deadline detected |
| `brief` → `watch` | Reporting deadline approaching |
| `board` → `draft` | TTr/NQ missing from agenda |
| `board` → `disclosure` | NQ requires CBTT (AI context analysis) |
| `watch` → `kpi` | All department reports received |
| `audit` → `board` | Audit findings for HĐQT reporting |

---

## Quick Start

### Prerequisites

1. Azure AD app registered (Client ID: `b9655c88-...`)
2. IT admin consent granted for 19 delegated permissions
3. `microsoft-mcp` authenticated via device flow
4. MCP server enabled in `mcp_config.json`

### Daily Rhythm

```
Open IDE  →  /BSCbrief  →  Work  →  /PMSquit  →  Close
```

### Command Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `/BSCbrief` | Morning briefing | `/BSCbrief` |
| `/BSCboard` | Board meeting cycle | `/BSCboard Kỳ 3/2026` |
| `/BSCdraft` | Draft corporate doc | `/BSCdraft TTr — mua sắm CNTT` |
| `/BSCdisclosure` | CBTT compliance | `/BSCdisclosure NQ bổ nhiệm` |
| `/BSCkpi` | Performance evaluation | `/BSCkpi Q1/2026` |
| `/BSCaudit` | Internal control | `/BSCaudit Phòng Tự doanh` |
| `/BSCwatch` | Report tracking | `/BSCwatch T02/2026` |

### Document Types (`/BSCdraft`)

```
BB = Biên bản    TTr = Tờ trình    NQ = Nghị quyết
PLY = Phiếu LYK  BC = Báo cáo     CV = Công văn
```

### Focus Modes (`/BSCbrief`)

| Mode | Behavior |
|------|----------|
| **Deep work** | AG works silently, reports when done/blocked |
| **Multi-task** | Brief updates after each task |
| **Review** | Items presented one by one for approval |

---

## Workflows

### `/BSCbrief` — Morning Briefing

**Frequency:** Daily | **Duration:** ~2 min | **HARD STOPs:** 1

Scans 6 M365 sources (Outlook, Calendar, Teams, SharePoint, To Do, cross-workflow state) and presents a prioritized dashboard. Suggests actions and workflow triggers based on detected conditions.

### `/BSCboard` — Board Meeting Lifecycle

**Frequency:** Per meeting | **Duration:** Multi-day | **HARD STOPs:** 4 | **Phases:** 5

| Phase | Timing | Key actions |
|-------|--------|-------------|
| Preparation | T-7 → T-1 | Agenda, checklist, invite |
| Governance | T-3 | Thẩm quyền, cấu phần, BIDV pre-approval |
| Meeting | T | Live minute-taking, action tracking |
| Post-meeting | T+1 → T+3 | BB, NQ, CBTT check, action emails |
| Follow-up | T+7+ | Progress tracking, escalation |

**Governance matrix per TTr:**
1. **Thẩm quyền** — HĐQT scope vs TGĐ/ĐHCĐ
2. **Cấu phần** — TTr + NQ draft + supporting docs
3. **Nội dung khớp** — Cross-document consistency
4. **BIDV pre-approval** — Phân cấp NĐD check

### `/BSCdraft` — Document Drafting

**Frequency:** On demand | **HARD STOPs:** 3

Accepts context from calling workflow or standalone invocation. Scans SharePoint for similar templates, applies BSC format, cross-checks consistency. Falls back to generic format with Options if no template found.

### `/BSCdisclosure` — CBTT 24h Compliance

**Frequency:** Event-driven | **HARD STOPs:** 1

**Alert schedule (bất thường type):**

| Time | Channel | Severity |
|------|---------|----------|
| T+0 | All | ⏰ Countdown started |
| 14:00 D+1 | Teams | 💬 Reminder |
| 15:00 | Email + Teams | 📧 Escalation |
| 15:15 | All | 🔴 Critical |
| 15:30 | All | 🚨 Deadline |
| After 24h | Incident log | 📋 Post-mortem |

### `/BSCkpi` — KPI Evaluation

**Frequency:** Monthly/Quarterly/Annual | **HARD STOPs:** 3

Six KPI categories: Financial, Business, Risk, HR, Project, Compliance. Cross-references `/BSCwatch` data. Outputs dashboard + report with Options for underperformers.

### `/BSCaudit` — Internal Control

**Frequency:** Ad-hoc/Quarterly | **HARD STOPs:** 3

Four audit types: Process, Compliance, Governance, Financial. Includes likelihood × impact risk matrix. FAIL items create mandatory fix tasks with re-audit loop.

### `/BSCwatch` — Reporting Tracker

**Frequency:** Continuous | **HARD STOPs:** 1

Evolving reporting matrix learned from SharePoint + email patterns. Escalation: T+3 gentle → T+5 Options → T+7 daily flag. Auto-triggers `/BSCkpi` when all data received.

---

## Use Cases

### UC1: Full HĐQT Meeting Cycle

```
/BSCbrief detects HĐQT in 5 days
  → /BSCboard Phase 1: build agenda, scan SharePoint
  → Governance check: TTr thiếu → /BSCdraft TTr
  → BIDV pre-approval: draft báo cáo NĐD → send → wait
  → Meeting day: Chairman notes bullets → AG expands to BB
  → Post-meeting: BB + NQ created → CBTT detected
  → /BSCdisclosure: 24h countdown → draft → send → confirm
  → Follow-up: action items tracked, reminders sent
```

### UC2: CBTT Bất thường

```
NQ ký → AG classifies as CBTT bất thường (AI context, not keywords)
  → ⏰ 24h countdown
  → Draft from 07_CBTT/ template → Chairman review
  → Send to UBCKNN + SGDCK
  → If no confirm: escalating alerts → incident log if overrun
```

### UC3: Department Accountability Loop

```
/BSCwatch: 2 departments missed monthly report
  → T+3: gentle email reminder (Chairman approves)
  → T+5: escalation Options to Chairman
  → Reports received → /BSCkpi analysis
  → Phòng X consistently late → /BSCaudit recommended
  → Audit findings → /BSCboard for HĐQT agenda
```

---

## Design Principles

| # | Principle | Origin | Implementation |
|---|-----------|--------|---------------|
| 1 | Structured phases | PMSaudit | Every workflow has numbered phases/steps |
| 2 | Chairman gates | PMSdaily | `[HARD STOP]` before critical actions |
| 3 | Options format | PMSnexus | `Option N: Action — Pros / Cons / Risk` |
| 4 | Dual logging | PMSkaizen | AG_Activity_Log + pms_usage.csv |
| 5 | Template learning | PMSforge | Learn from SharePoint, improve with use |
| 6 | Archive-only | AG Policy | Never delete, only move to Archive/ |
| 7 | Kaizen observer | PMSkaizen | Weekly insight log, pattern detection |
| 8 | Graceful degradation | New | M365 down → partial results + flag |
| 9 | Cross-workflow triggers | New | 7 automated trigger paths |
| 10 | Governance validation | New | Authority, completeness, consistency, BIDV |

---

## Capabilities & Maturity

### Maturity Model

| Level | Status | Description |
|-------|--------|-------------|
| **L0: Designed** | ✅ Now | Workflow files created, patterns applied |
| **L1: Connected** | ⏳ Blocked | M365 authenticated, live data flowing |
| **L2: Learning** | 🔜 Week 1-4 | Templates, reporting matrix, sender profiles |
| **L3: Predictive** | 🔮 Month 2-3 | Predict late departments, auto-classify NQ |
| **L4: Autonomous** | 🚀 Month 3-6 | Background daemon, Power Automate, Teams bot |

### Capability Matrix

| Capability | L0 | L1 | L2 | L3 | L4 |
|-----------|----|----|----|----|-----|
| Email triage | — | ✅ | ✅ | ✅ | ✅ |
| Calendar management | — | ✅ | ✅ | ✅ | ✅ |
| Document drafting | — | ⚠️ | ✅ | ✅ | ✅ |
| CBTT compliance | — | ✅ | ✅ | ✅ | ✅ |
| Report tracking | — | ⚠️ | ✅ | ✅ | ✅ |
| Predictive alerts | — | — | — | ✅ | ✅ |
| Background monitoring | — | — | — | — | ✅ |

⚠️ = functional but limited (cold-start, no templates yet)

---

## Roadmap

### Phase 1: Foundation *(current → admin consent)*
- [x] Workflow suite (7 files)
- [x] AG Operating Policy
- [x] Folder structure + initial logs
- [ ] **IT admin consent** ← blocker
- [ ] First `/BSCbrief` live run

### Phase 2: Learn & Adapt *(weeks 1-4)*
- [ ] SharePoint template library scan
- [ ] `reporting_matrix.json` from real data
- [ ] First full `/BSCboard` cycle
- [ ] VIP sender calibration
- [ ] First CBTT live processing

### Phase 3: Automate *(months 2-3)*
- [ ] Power Automate: keyword safety net (24/7)
- [ ] Python daemon: AI-powered CBTT classifier
- [ ] Teams bot: action item reminders
- [ ] Auto meeting invite from `/BSCboard`
- [ ] Scheduled `/BSCwatch` scans

### Phase 4: Intelligence *(months 3-6)*
- [ ] Predictive department compliance scoring
- [ ] NQ → CBTT auto-classification with confidence %
- [ ] Cross-meeting action correlation
- [ ] Automated quarterly governance report
- [ ] Board performance web dashboard

---

## Limitations

### Critical

| Limitation | Impact | Mitigation | ETA |
|-----------|--------|-----------|-----|
| IT admin consent pending | **All M365 tools blocked** | Follow up with IT | ASAP |
| Conversation-based only | No background monitoring | `/BSCbrief` daily sweep | Phase 3 |
| No real-time alerts | CBTT depends on AG online | Power Automate layer | Phase 3 |

### Functional

| Limitation | Impact | Mitigation |
|-----------|--------|-----------|
| Template cold-start | First docs need heavy editing | Improves after each use |
| No voice transcription | Meeting notes require typing | Bullet points → AG expands |
| Single user (Chairman) | Staff cannot invoke directly | Future Teams integration |
| Markdown output only | Documents need DOCX conversion | Chairman exports for signing |
| CBTT classification | May miss edge cases | Power Automate keyword backup |
| SharePoint visibility | May not see all folders | IT grants broader read access |
| No offline mode | Requires internet | Archive-only ensures no data loss |

---

## Dependencies

| Component | Version | Status | Purpose |
|-----------|---------|--------|---------|
| Antigravity IDE | Latest | ✅ | AI runtime |
| `microsoft-mcp` | Latest | ✅ Installed | M365 bridge (48 tools) |
| Azure AD App | `b9655c88-...` | ✅ Registered | Auth (19 permissions) |
| `uv` | 0.10.4 | ✅ | Python env manager |
| Microsoft Graph API | v1.0 | ⏳ Needs auth | M365 data access |
| MSAL | Latest | ✅ | Token management |
| PMS Workflows | 6 files | ✅ | Foundation patterns |

---

## File Structure

```
.agent/workflows/
├── BSC_README.md             ← This file
├── AG_policy.md              ← Operating rules (naming, logging, safety)
├── BSCbrief.md               ← Morning briefing
├── BSCboard.md               ← Board meeting lifecycle
├── BSCdraft.md               ← Document drafting
├── BSCdisclosure.md          ← CBTT compliance
├── BSCkpi.md                 ← KPI evaluation
├── BSCaudit.md               ← Internal audit
├── BSCwatch.md               ← Report tracking
├── PMSaudit.md               ← [PMS] Milestone audit
├── PMSdaily.md               ← [PMS] Daily standup
├── PMSinit.md                ← [PMS] Project init
├── PMSquit.md                ← [PMS] Session shutdown
├── PMSforge.md               ← [PMS] Automation factory
├── PMSkaizen.md              ← [PMS] Continuous improvement
└── PMSnexus.md               ← [PMS] Cross-domain problem solving

01_WORK_BSC/AG_Output/
├── Reports/                  ← Completed reports
├── Drafts/                   ← Pending review
├── Analysis/                 ← Data analysis
├── Extracts/                 ← Data extraction
├── Templates/                ← BSC templates (learned)
├── Archive/                  ← Permanent storage (NEVER DELETE)
└── Logs/
    ├── AG_Activity_Log_YYYYMM.csv
    ├── AG_Insight_Log_YYYYMM.md
    └── reporting_matrix.json
```

---

## Contributing

This system is maintained by AG under the supervision of SonPM (Chairman). All changes follow the PMS workflow:

1. Propose changes via `/PMSkaizen` insights
2. Chairman approves → AG implements
3. Test in next workflow invocation
4. Log results → iterate

---

*Built with PMS principles: First Principles (Musk) × Systematic Process (Gates) × Kaizen (Toyota)*
