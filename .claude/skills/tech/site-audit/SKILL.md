---
name: site-audit
user-invocable: false
description: Audit the website for issues — broken links, UX problems, mobile issues, speed.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Site Audit Playbook

## Inputs

- $ARGUMENTS — Site URL(s) and any specific areas of concern
- `data/brand/brand-dna.md` — Brand standards to audit against

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for Core Web Vitals thresholds, WCAG 2.2 checklist, SEO audit standards, UX checklist, and scoring methodology
2. Read `data/brand/brand-dna.md` for brand alignment reference
3. Audit broken links — use Bash (curl) to test all internal and external links
4. Audit mobile responsiveness — check viewport meta, responsive breakpoints, touch targets
5. Audit page speed — run Lighthouse via Bash, check load times and Core Web Vitals
6. Audit SEO basics — meta titles, descriptions, heading hierarchy, alt tags, structured data
7. Audit UX — navigation clarity, CTA visibility, form usability, content readability
8. Audit security basics — HTTPS, security headers, mixed content, exposed sensitive paths
9. Score each area 1-10 with specific evidence for the rating
10. Prioritize all findings by severity (critical / high / medium / low)
11. Provide actionable fix recommendations for each issue found

## Output

- Write the full audit report to `data/tech/site-audit-[date].md` with: scores per category, issues found, priority rankings, recommended fixes
- Update your MEMORY.md with key findings and patterns discovered
