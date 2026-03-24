---
name: launch-checklist
user-invocable: false
description: Pre-launch checklist — everything that must be ready before launch day. The final gate.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Launch Checklist Playbook

## Inputs

- $ARGUMENTS — Product name
- `data/product/launch-plan-*.md` — Launch plan
- `data/product/product-spec-*.md` — Product spec

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read the launch plan and product spec
4. Run the pre-launch checklist:
   **Product:**
   - [ ] Product is built and functional
   - [ ] Pricing is set and payment processing works
   - [ ] Onboarding/welcome experience is ready
   - [ ] FAQ / support documentation exists
   **Content:**
   - [ ] Launch blog post / announcement written and reviewed
   - [ ] Social posts scheduled across all platforms
   - [ ] Email launch sequence loaded and tested
   - [ ] Landing page / sales page live and tested
   **Marketing:**
   - [ ] Paid ad campaigns ready to activate
   - [ ] Tracking pixels / analytics in place
   - [ ] UTM parameters set for all links
   **PR:**
   - [ ] Press release drafted and approved
   - [ ] Media list ready, pitches queued
   **Operations:**
   - [ ] Launch timeline confirmed with all departments
   - [ ] Contingency plan for common issues (site down, payment fail, etc.)
5. Mark each item: READY / NOT READY / N/A
6. If any critical items are NOT READY — flag as launch blocker
7. Final verdict: GO / NO-GO with reasoning

## Output

- Write to `data/product/launch-checklist-[product]-[date].md`
- Update your MEMORY.md with checklist patterns
