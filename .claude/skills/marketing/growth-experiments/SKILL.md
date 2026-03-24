---
name: growth-experiments
user-invocable: false
description: Propose growth experiments and A/B tests — hypothesis, method, expected impact, and measurement plan.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Growth Experiments Playbook

## Inputs

- $ARGUMENTS — Growth goal, channel focus, current metrics
- `data/brand/brand-dna.md` — Brand identity (guardrail)
- `data/analytics/kpi-dashboard.md` — Performance data
- `data/content/top-performers.md` — What content works
- `data/marketing/` — Existing marketing data and past experiments

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for experiment design methodology
2. Apply the ICE/RICE scoring and experiment frameworks from the reference
3. Read brand DNA, available analytics, top performers, and existing marketing data
4. Research current growth tactics and experiments via web
5. Propose 3-5 experiments:
   - For each experiment:
     - **Hypothesis** — "If we [change], then [metric] will [improve] because [reason]"
     - **Method** — What to do, step-by-step
     - **Control vs. variant** — What changes, what stays the same
     - **Metric to track** — Primary metric + secondary metrics
     - **Timeline** — How long to run
     - **Expected impact** — Conservative and optimistic estimates
     - **Effort** — Low/medium/high
     - **Brand risk** — Does this compromise brand integrity? (must be no)
6. Prioritize by expected impact ÷ effort (ICE score: Impact × Confidence × Ease)
7. Recommend which 1-2 experiments to run first

## Output

- Write to `data/marketing/growth-experiments-[date].md`
- Update your MEMORY.md with experiment results and growth patterns
