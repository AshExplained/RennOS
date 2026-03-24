---
name: brand-review
user-invocable: false
description: Strategic brand alignment check — does this content or campaign fit our positioning, messaging pillars, and brand direction?
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Brand Review Playbook

## Inputs

- $ARGUMENTS — Content, campaign plan, or initiative to review
- `data/brand/brand-dna.md` — Brand identity and positioning

## Steps

1. Read `data/brand/brand-dna.md` thoroughly
2. Read the content or campaign being reviewed
3. Check alignment across these dimensions:
   - **Voice** — Does it sound like us?
   - **Tone** — Is the tone appropriate for the context?
   - **Messaging pillars** — Does it map to one or more of our core themes?
   - **Positioning** — Does it reinforce our market position?
   - **Audience fit** — Would our target audience connect with this?
4. Flag specific misalignments with concrete recommendations for fixing them
5. Give an overall alignment score (1-10) with justification
6. Provide a clear PASS / NEEDS REVISION / REJECT recommendation

## Output

- Write review to `data/brand/brand-review-[date].md` (use today's date in YYYY-MM-DD format)
- Update your MEMORY.md with key findings
