# Workflow: Weekly Review

> Sunday check-in — what shipped, what's next, system health.

## Trigger
- "Weekly review"
- "Sunday review"
- "What happened this week?"

## Profile
Full RennOS, Brand & Business, Life OS (adapts per profile)

## Steps

### 1. Gather Data
**Agent:** CEO agent (direct — no delegation)
**Action:** Run `python3 -m scripts.ops.project_status_scan` to get recent file activity
**Input:** Last 7 days of `data/` changes
**Output:** Activity summary by department

### 2. Content Performance (Brand & Business / Full only)
**Agent:** @content-analyst
**Skill:** content-performance
**Input:** `data/analytics/kpi-dashboard.md`, `data/content/content-calendar.md`
**Output:** What performed well, what underperformed, patterns

### 3. Financial Pulse
**Agent:** CEO agent (direct)
**Action:** Run `python3 -m scripts.finance.revenue_summary`
**Input:** `data/finance/`
**Output:** Revenue snapshot

### 4. Personal Check-in (Life OS / Full only)
**Agent:** @habit-tracker
**Skill:** habit-review
**Input:** `data/personal/health/`, `data/personal/growth/`
**Output:** Habit streaks, breaks, trends

### 5. Deadline Scan
**Agent:** CEO agent (direct)
**Action:** Run `python3 -m scripts.ops.deadline_scanner`
**Input:** All `data/` files
**Output:** Overdue items, upcoming deadlines

### 6. Compile Report
**Agent:** @report-builder
**Skill:** weekly-digest
**Input:** Outputs from steps 1-5
**Output:** Compiled weekly digest

### 7. Brief User
**Agent:** CEO agent
**Action:** Present the digest as a concise briefing:
- What shipped this week
- What's in motion
- What needs attention next week
- Content buffer health (if applicable)
- Habit/health status (if applicable)
- Upcoming deadlines

End with: "What do you want to adjust for next week?"

### 8. Update Roadmap
**Agent:** CEO agent
**Action:** Based on user's input, update `data/strategy/quarterly-roadmap.md` and `ceo-memory/active_projects.md`

## Data Flow
```
Scripts → stdout (scanned by CEO agent)
data/analytics/ ← step 2 reads
data/finance/ ← step 3 reads
data/personal/ ← step 4 reads
ceo-memory/active_projects.md ← step 8 writes
```
