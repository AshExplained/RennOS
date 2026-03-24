---
name: income-streams
user-invocable: false
description: Map and evaluate all current and potential income streams — what's working, what's not, what's untapped.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Income Streams Playbook

## Inputs

- $ARGUMENTS — Scope ("current streams" or "explore new")
- `data/finance/revenue-history.md` — Historical revenue data
- `data/partnerships/` — Deal and sponsorship data
- `data/marketing/` — Ad revenue and campaign data
- `data/strategy/audience-personas.md` — Audience segments

## Steps

1. Read revenue history, partnerships data, and audience personas
2. Research income stream options via web for the user's niche
3. Map all current income streams:
   - For each: stream name, revenue (monthly/annual), trend (growing/stable/declining), effort level, scalability
4. Evaluate potential new streams:
   - Courses / digital products
   - Memberships / communities
   - Consulting / coaching
   - Sponsorships / brand deals
   - Affiliate / referral income
   - Speaking fees
   - Licensing / IP deals
   - Ad revenue (YouTube, podcast)
5. For each potential stream: estimated revenue, effort to launch, time to first revenue, audience fit
6. Rank all streams (current + potential) by revenue × scalability × brand fit

## Output

- Write to `data/finance/income-streams-[date].md`
- Update your MEMORY.md with income stream patterns
