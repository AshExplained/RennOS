---
name: trend-scan
user-invocable: false
description: Scan for trending topics, news, viral moments, and emerging narratives in the relevant space. Categorizes by lifecycle stage.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Trend Scan Playbook

## Inputs

- $ARGUMENTS — Industry/niche to scan, optional time window (e.g., "last 7 days")
- `data/brand/brand-dna.md` — Brand context for relevance filtering
- `data/strategy/audience-personas.md` — Audience context

## Current State
!`ls -1t data/strategy/trend-scan-* data/inbox/trend-scan-* 2>/dev/null | head -5`

## Steps

1. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
2. Search for trending topics in the industry via web:
   - Industry news and publications
   - Social media trending topics (X, LinkedIn, Reddit)
   - Viral content in the space
   - Platform algorithm changes or updates
   - Cultural moments relevant to the brand
3. For each trend found, document:
   - **What** — Description of the trend
   - **Where** — Which platforms/sources
   - **Lifecycle stage** — Emerging, Peaking, or Declining
   - **Relevance** — How relevant to the user's brand (1-10)
   - **Urgency** — Time-sensitive? How long is the window?
4. Filter aggressively — only include trends scoring 6+ on relevance
5. For top trends, suggest a potential angle for the user

## Output

- Write to `data/strategy/trend-scan-[date].md` (use today's date in YYYY-MM-DD format)
- For scheduled/automated runs, write to `data/inbox/trend-scan-[date].md` instead
- Update your MEMORY.md with key findings
