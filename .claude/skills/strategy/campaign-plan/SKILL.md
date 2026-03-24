---
name: campaign-plan
user-invocable: false
description: Design a specific campaign — objective, target audience, timeline, deliverables by department, KPIs, and execution plan.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Campaign Plan Playbook

## Inputs

- $ARGUMENTS — Campaign topic, goal, or brief
- `data/brand/brand-dna.md` — Brand foundation
- `data/strategy/quarterly-roadmap.md` — Current roadmap context
- `data/strategy/audience-personas.md` — Target audience

## Current State
!`head -50 data/strategy/quarterly-roadmap.md 2>/dev/null`

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for campaign planning methodology
2. Apply the KPI selection and measurement frameworks from the reference
3. Read all input files
4. Define the campaign:
   - **Objective** — What are we trying to achieve?
   - **Target persona(s)** — Which audience segment(s)?
   - **Key message** — What's the one thing we want them to remember?
   - **Unique angle** — What makes this campaign distinctly "us"?
5. Set the timeline:
   - Start date → End date
   - Key milestones within the campaign
6. List deliverables by department:
   - Strategy: positioning brief
   - Content: blog posts, social posts, scripts
   - Social: distribution plan
   - Marketing: promotion plan
   - Design: visual assets
7. Define KPIs and success criteria:
   - Primary metric (the one number that matters)
   - Secondary metrics
   - What does "success" look like?
8. Create an execution timeline with specific dates and owners

## Output

- Write to `data/strategy/campaigns/[campaign-name].md` (use lowercase, hyphenated name)
- Update your MEMORY.md with key decisions
