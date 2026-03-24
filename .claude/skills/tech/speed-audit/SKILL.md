---
name: speed-audit
user-invocable: false
description: Audit site speed and recommend optimizations — Core Web Vitals, load time, bottlenecks.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Speed Audit Playbook

## Inputs

- $ARGUMENTS — Site URL(s) and any specific performance concerns
- Previous speed audits from `data/tech/speed-audit-*.md` if available

## Steps

1. Run performance tests via Bash — Lighthouse CLI, curl timing, or similar tools
2. Research current Core Web Vitals standards and thresholds via WebSearch
3. Analyze key metrics:
   - **LCP** (Largest Contentful Paint) — target < 2.5s
   - **INP** (Interaction to Next Paint) — target < 200ms
   - **CLS** (Cumulative Layout Shift) — target < 0.1
   - **TTFB** (Time to First Byte) — target < 800ms
   - **Total page size** and request count
4. Identify specific bottlenecks:
   - Large unoptimized images
   - Render-blocking CSS/JS
   - Slow API calls or third-party scripts
   - Excessive JavaScript bundle size
   - Missing caching headers
   - Uncompressed assets
5. Prioritize fixes by impact on user experience and implementation effort
6. Compare against previous audits if available to track trends

## Output

- Write the audit report to `data/tech/speed-audit-[date].md` with: metric scores, bottleneck analysis, prioritized optimization recommendations, before/after estimates for each fix
- Update your MEMORY.md with key findings and patterns discovered
