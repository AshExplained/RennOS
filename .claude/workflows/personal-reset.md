# Workflow: Personal Reset

> When energy is low, habits have slipped, or things feel overwhelming — a structured reset.

## Trigger
- "I need a reset"
- "Things have slipped"
- "I'm overwhelmed"
- "Help me get back on track"

## Profile
Full RennOS, Life OS

## Steps

### 1. Check-in
**Agent:** @mental-health-guide
**Skill:** wellness-check
**Input:** Direct conversation with user
**Output:** Current state assessment — energy, stress, sleep, mood
**Notes:** Be gentle. No productivity pressure. Just listen.

### 2. Habit Audit
**Agent:** @habit-tracker
**Skill:** habit-review
**Input:** `data/personal/health/`, recent activity
**Output:** Which habits held, which slipped, streak status

### 3. Calendar Triage
**Agent:** @schedule-manager
**Skill:** master-calendar
**Input:** `data/operations/master-calendar.md`
**Output:** What's truly urgent vs what can be rescheduled
**Action:** CEO agent presents a simplified next-3-days view

### 4. One Thing
**CEO agent asks:** "What's the ONE thing that would make you feel better if it got done today?"
**Action:** Create a single task. Just one. Not a list.

### 5. Rebuild Gradually
**Agent:** @habit-tracker
**Skill:** habit-setup
**Input:** User's current energy level
**Output:** Stripped-down habit list — only essentials until energy returns
**Notes:** Reduce, don't add. "Do less, better" until the reset takes hold.

### 6. Schedule Follow-up
**CEO agent:** "I'll check in on this tomorrow during wake-up. No pressure — just a gentle nudge."
**Action:** Add a note to `ceo-memory/active_projects.md` to check reset progress next session.

## Data Flow
```
data/personal/health/ ← steps 1, 2 read/write
data/operations/master-calendar.md ← step 3 reads
ceo-memory/active_projects.md ← step 6 writes
```

## Rules
- This is not a productivity workflow — it's a recovery workflow
- No guilt, no "you should have" — only forward motion
- If the user needs to vent, let them. Don't rush to solutions.
- One action item, not ten. Progress compounds from small wins.
