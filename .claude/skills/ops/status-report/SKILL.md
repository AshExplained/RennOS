---
name: status-report
user-invocable: false
description: Generate a status report across all active projects — what's on track, at risk, and blocked.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Status Report Playbook

## Inputs

- $ARGUMENTS — Report scope: "all" or specific project/department
- `.claude/ceo-memory/active_projects.md` — Current project status
- `data/operations/task-tracker.md` — Task tracking data
- `data/strategy/quarterly-roadmap.md` — Strategic milestones

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/project_status_scan.py` to gather current data
3. Read active projects, task tracker, and quarterly roadmap
4. Scan recent activity across `data/` directories (check file modification dates)
5. For each active project/initiative:
   - **Status** — On Track / At Risk / Blocked / Complete
   - **Progress** — What's been done since last report
   - **Next steps** — What needs to happen next
   - **Blockers** — What's preventing progress (if any)
   - **Decisions needed** — What requires the user's input
6. Provide overall summary:
   - Projects on track vs at risk vs blocked
   - Key wins since last report
   - Top priorities for this week
   - Decisions waiting on the user

## Output

- Write to `data/operations/status-report-[date].md`
- Update your MEMORY.md with status patterns
