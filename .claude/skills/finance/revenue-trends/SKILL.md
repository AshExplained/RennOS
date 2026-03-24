---
name: revenue-trends
user-invocable: false
description: Analyze revenue trends and flag changes — what's growing, declining, or at risk.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Revenue Trends Playbook

## Inputs

- $ARGUMENTS — Time period to analyze, specific stream focus
- `data/finance/revenue-history.md` — Historical revenue data
- `data/finance/revenue-dashboard.md` — Current dashboard

## Steps

1. Read revenue history and current dashboard
2. Analyze trends across all streams:
   - **Growing streams** — Which are trending up? Growth rate? Sustainable?
   - **Declining streams** — Which are trending down? Why? Recoverable?
   - **Stable streams** — Reliable base revenue
   - **Seasonal patterns** — Revenue spikes or dips tied to time of year
   - **Concentration risk** — Is too much revenue from one stream/client?
3. Project forward — at current trajectory, where will each stream be in 3/6/12 months?
4. Flag risks:
   - Streams that are declining without intervention
   - Over-reliance on a single client or stream (>40% of revenue)
   - Upcoming contract expirations that will impact revenue
5. Recommend actions per stream (invest more, maintain, sunset)

## Output

- Write to `data/finance/revenue-trends-[date].md`
- Update your MEMORY.md with trend patterns
