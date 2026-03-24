---
name: ux-audit
user-invocable: false
description: Audit an existing page or product for UX issues — usability, accessibility, friction, and improvement opportunities.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# UX Audit Playbook

## Inputs

- $ARGUMENTS — URL or page description, user goal
- `data/brand/brand-dna.md` — Core brand identity
- `data/strategy/audience-personas.md` — Audience segments

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for UX audit methodology and heuristics
2. Apply Nielsen's heuristics and WCAG guidelines from the reference
3. Read brand DNA and audience personas
4. Research current UX best practices and heuristics via web
5. Audit against Nielsen's 10 usability heuristics:
   - Visibility of system status
   - Match between system and real world
   - User control and freedom
   - Consistency and standards
   - Error prevention
   - Recognition rather than recall
   - Flexibility and efficiency of use
   - Aesthetic and minimalist design
   - Help users recognize, diagnose, and recover from errors
   - Help and documentation
6. Additionally check:
   - **Accessibility** — Color contrast, alt text, keyboard navigation, screen reader compatibility
   - **Mobile usability** — Touch targets, responsive layout, loading speed
   - **Conversion path** — Is the path to CTA clear and frictionless?
   - **Cognitive load** — Is the page overwhelming or confusing?
7. For each issue: what's wrong, severity (critical/major/minor), where it occurs, how to fix it
8. Score overall UX: 1-10 with category breakdown

## Output

- Write to `data/design/ux-audit-[page]-[date].md`
- Update your MEMORY.md with UX patterns
