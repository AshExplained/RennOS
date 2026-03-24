---
name: launch-plan
user-invocable: false
description: Create a full product launch plan — timeline, channels, department assignments, and execution sequence.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Launch Plan Playbook

## Inputs

- $ARGUMENTS — Product name, launch date, scope
- `data/brand/brand-dna.md` — Core brand identity
- `data/product/` — Product spec, roadmap
- `data/content/content-calendar.md` — Content schedule
- `data/strategy/quarterly-roadmap.md` — Business roadmap

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read brand DNA, product spec, roadmap, and content calendar
4. Design the launch plan:
   - **Launch date** — Fixed or flexible?
   - **Pre-launch phase** (4-6 weeks before):
     - Teaser content (@short-form-writer, @long-form-writer)
     - Email waitlist/pre-sale (@email-marketing-manager)
     - PR story angles (@pr-strategist)
     - Community buzz (@community-manager)
   - **Launch week:**
     - Launch content (blog, social, video) — assign to Content agents
     - Press release / media outreach — assign to PR agents
     - Email launch sequence — assign to Email Marketing Manager
     - Paid amplification — assign to Paid Ads Manager
     - Social blitz — assign to Platform Manager + Content Scheduler
   - **Post-launch phase** (2-4 weeks after):
     - Follow-up content (testimonials, case studies, FAQs)
     - Re-engagement for non-converters
     - Feedback collection
5. For each task: what, who (department/agent), when (date), deliverable, status
6. Identify critical path — what must happen in sequence vs what can run in parallel
7. Define launch KPIs and success criteria

## Output

- Write to `data/product/launch-plan-[product]-[date].md`
- Update your MEMORY.md with launch patterns
