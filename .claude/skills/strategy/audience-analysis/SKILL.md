---
name: audience-analysis
user-invocable: false
description: Analyze engagement data to understand what resonates with the audience and what flops. Identifies content-audience fit.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Audience Analysis Playbook

## Inputs

- $ARGUMENTS — Engagement data, analytics exports, or performance metrics
- `data/strategy/audience-personas.md` — Current personas
- `data/content/top-performers.md` — Known top-performing content

## Steps

1. Read existing personas from `data/strategy/audience-personas.md`
2. Read top performers from `data/content/top-performers.md`
3. Analyze the provided engagement data looking for patterns:
   - **Topics** — Which topics get the most engagement?
   - **Formats** — Which formats perform best (video, text, carousel, etc.)?
   - **Tones** — Does casual outperform professional? Educational vs. entertaining?
   - **Timing** — Any patterns in when content performs best?
   - **Platform** — Performance differences across platforms?
4. Identify content-audience fit gaps (where content isn't matching audience needs)
5. Recommend specific adjustments to content strategy

## Output

- Write analysis to `data/strategy/audience-analysis-[date].md` (use today's date in YYYY-MM-DD format)
- Update `data/content/top-performers.md` if new insights warrant it
- Update your MEMORY.md with key findings
