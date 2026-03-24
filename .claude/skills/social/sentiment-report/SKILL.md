---
name: sentiment-report
user-invocable: false
description: Analyze sentiment around brand mentions — quantify positive, negative, neutral, and identify drivers.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Sentiment Report Playbook

## Inputs

- $ARGUMENTS — Time period and specific topic/event to analyze (if any)
- `data/social/` — Existing mention scans
- `data/brand/brand-dna.md` — Brand context

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read recent mention scans from `data/social/`
3. If additional scanning needed, search web for brand mentions in the specified time period
4. Categorize all mentions by sentiment:
   - **Positive** — Praise, recommendations, shares, support
   - **Negative** — Complaints, criticism, frustration
   - **Neutral** — Mentions without strong sentiment
5. Quantify: total mentions, % positive/negative/neutral, trend vs previous period
6. Identify sentiment drivers:
   - What's driving positive sentiment? (specific content, interactions, events)
   - What's driving negative sentiment? (issues, gaps, controversies)
7. Provide recommendations for improving sentiment

## Output

- Write to `data/social/sentiment-report-[date].md`
- Update your MEMORY.md with sentiment trends over time
