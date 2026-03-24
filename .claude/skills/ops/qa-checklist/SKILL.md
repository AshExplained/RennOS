---
name: qa-checklist
user-invocable: false
description: Run a quality checklist on any deliverable before it goes live — brand alignment, accuracy, formatting, and completeness.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# QA Checklist Playbook

## Inputs

- $ARGUMENTS — Path to deliverable, type (blog/email/social/press-release/landing-page/ad/outreach)
- `data/brand/brand-dna.md` — Brand positioning
- `data/brand/style-guide.md` — Style and formatting standards

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for QA checklists by deliverable type
2. Apply the relevant checklist from the reference based on the deliverable type
3. Read brand DNA and style guide
4. Read the deliverable to review
5. Run checklist based on deliverable type:

   **Universal checks (all types):**
   - Brand voice alignment — sounds like us?
   - No factual errors or unverified claims
   - No broken links or missing references
   - No sensitive information leaked
   - Spelling and grammar clean
   - CTA present and clear
   - Formatting correct for target platform

   **Type-specific checks:**
   - **Blog/article:** Meta title, meta description, headers, SEO basics, image alt text
   - **Email:** Subject line, preview text, mobile-friendly, unsubscribe link note, CAN-SPAM compliance
   - **Social post:** Platform character limits, hashtags, @mentions correct
   - **Press release:** AP style, dateline, boilerplate, contact info, inverted pyramid
   - **Landing page:** Headline, social proof, FAQ, above-the-fold CTA
   - **Ad:** Platform specs, targeting notes, A/B variants
   - **Outreach/pitch:** Personalization, value-first, concise, clear ask

6. Score: PASS / PASS WITH NOTES / FAIL
7. For each failed check: what's wrong, how to fix it

## Output

- Write to `data/operations/qa-[deliverable-type]-[date].md`
- Update your MEMORY.md with common quality issues found
