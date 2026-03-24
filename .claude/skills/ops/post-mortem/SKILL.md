---
name: post-mortem
user-invocable: false
description: Run a post-mortem on a completed campaign or project — what worked, what didn't, root causes, and action items for next time.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Post-Mortem Playbook

## Inputs

- $ARGUMENTS — Campaign/project name, results data if available
- `data/operations/` — Task tracker, project data
- `data/analytics/kpi-dashboard.md` — Performance metrics
- `data/content/top-performers.md` — Content performance data

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for post-mortem methodology
2. Apply the blameless analysis frameworks from the reference
3. Read all available data about the campaign/project (task tracker, analytics, content performance)
4. Structure the post-mortem:
   - **Overview** — What was the campaign/project? Goal? Timeline? Team involved?
   - **Results** — Did we hit our KPIs? Metrics vs targets
   - **Timeline review** — Was the schedule realistic? Did we ship on time?
   - **What worked** — Specific wins with evidence (not vague praise)
   - **What didn't work** — Specific failures with honest assessment
   - **Root cause analysis** — Why did the failures happen? (5 Whys methodology)
   - **Surprises** — What was unexpected (positive or negative)?
   - **Action items** — Specific, assignable changes for next time
5. Keep it blameless — focus on systems and processes, not individuals
6. Be honest — a post-mortem that only says nice things is useless
7. Each action item must have: what, who (which department/agent), and when

## Output

- Write to `data/operations/post-mortem-[project]-[date].md`
- Update your MEMORY.md with post-mortem learnings and patterns
