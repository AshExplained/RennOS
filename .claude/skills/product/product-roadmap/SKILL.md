---
name: product-roadmap
user-invocable: false
description: Create or update the product roadmap — what to build, when, and in what order.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Product Roadmap Playbook

## Inputs

- $ARGUMENTS — Time horizon, priorities, or "review current"
- `data/product/product-roadmap.md` — Current product roadmap
- `data/strategy/quarterly-roadmap.md` — Business roadmap
- `data/finance/revenue-strategy-*.md` — Revenue strategy
- `data/product/feedback-themes.md` — Customer feedback themes

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for product prioritization frameworks
2. Apply the appropriate prioritization framework from the reference
3. Read existing product roadmap, quarterly roadmap, revenue strategy, and feedback themes
4. Define or update the roadmap:
   - **Now** (next 30 days) — What's being built/launched right now
   - **Next** (30-90 days) — What's validated and queued
   - **Later** (90+ days) — Ideas validated but not yet prioritized
   - **Icebox** — Ideas captured but not yet validated
5. For each item on the roadmap:
   - Product name/concept
   - Status (ideation / validation / design / build / beta / launch / live)
   - Target launch date
   - Revenue target
   - Dependencies (which departments/agents involved)
   - Next milestone
6. Align with quarterly roadmap — product launches should map to strategic themes
7. Flag items that are behind schedule or blocked

## Output

- Update `data/product/product-roadmap.md` (living document — overwrite)
- Update your MEMORY.md with roadmap decisions
