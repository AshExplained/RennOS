---
name: benchmark
user-invocable: false
description: Benchmark current metrics against past performance or industry standards — are we ahead or behind?
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Benchmark Playbook

## Inputs

- $ARGUMENTS — Metric area to benchmark, or "all"
- `data/analytics/kpi-dashboard.md` — Current metrics
- `data/analytics/benchmarks.md` — Existing benchmarks

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for current industry benchmarks
2. Apply the platform-specific benchmarks from the reference when comparing performance
3. Read current KPI dashboard and existing benchmarks
4. Research industry benchmarks via web:
   - Average engagement rates by platform and niche
   - Email open/click rates by industry
   - Typical follower growth rates
   - Ad performance benchmarks (CTR, CPC, ROAS)
   - Content performance benchmarks (reach per post, shares)
5. Compare the user's metrics against:
   - **Industry average** — How do we compare to typical performers?
   - **Top performers** — How do we compare to the best in the space?
   - **Past performance** — How do we compare to ourselves 30/60/90 days ago?
6. For each metric: current value, industry avg, top performer, the user's trend, gap analysis
7. Identify where the user is beating benchmarks (strengths) and where below (opportunities)
8. Recommend specific actions to close benchmark gaps

## Output

- Update `data/analytics/benchmarks.md` with latest comparisons
- Update your MEMORY.md with benchmark findings
