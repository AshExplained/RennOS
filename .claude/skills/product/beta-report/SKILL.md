---
name: beta-report
user-invocable: false
description: Compile beta testing results — bugs, UX issues, feature requests, NPS, and go/no-go recommendation.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Beta Report Playbook

## Inputs

- $ARGUMENTS — Product name, beta feedback data
- `data/product/beta-plan-*.md` — Beta plan
- `data/product/product-spec-*.md` — Product spec

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read beta plan and product spec for context
3. Compile beta results:
   - **Participation** — How many testers, completion rate, engagement level
   - **Bugs found** — Severity (critical/major/minor), status (fixed/open)
   - **UX issues** — Pain points, confusion, friction areas
   - **Feature requests** — What testers want added or changed
   - **NPS score** — Net Promoter Score if collected
   - **Testimonials** — Positive quotes for marketing use
   - **Usage patterns** — How testers actually used the product vs how we expected
4. Assess against success criteria from beta plan
5. Provide go/no-go recommendation:
   - **GO** — Ready to launch (may have minor issues to address post-launch)
   - **GO with conditions** — Launch if specific fixes are made first
   - **NO-GO** — Not ready, specify what needs to change and re-test timeline
6. Save any strong testimonials to `data/customers/testimonials.md`

## Output

- Write to `data/product/beta-report-[product]-[date].md`
- Update your MEMORY.md with beta testing patterns
