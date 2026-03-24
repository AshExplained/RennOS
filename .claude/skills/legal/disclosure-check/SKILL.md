---
name: disclosure-check
user-invocable: false
description: Check content for proper FTC disclosures — sponsored content, affiliate links, gifted products.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Disclosure Check Playbook

## Inputs

- $ARGUMENTS — Content to check, relationship type (sponsored/affiliate/gifted/partnership)
- `data/brand/brand-dna.md` — Brand positioning

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for FTC disclosure requirements
2. Apply the platform-specific placement and language rules from the reference
3. Read the content to check
4. Research current FTC endorsement guidelines via web (these update periodically)
5. Check for required disclosures:
   - Is the material connection disclosed? (sponsorship, affiliate, gift)
   - Is the disclosure clear and conspicuous? (not buried, not in small print)
   - Is the disclosure in the same medium as the endorsement? (visual for video, text for text)
   - Does it use clear language? ("ad", "sponsored", "#ad" — not "#sp" or ambiguous)
   - Is it placed before the fold / above "more" button?
   - Platform-specific requirements met? (Instagram, YouTube, TikTok each have rules)
6. Check for truthful claims:
   - Any unsubstantiated claims about products/services?
   - Any misleading impressions?
   - Results claims with appropriate qualifiers?
7. Verdict: COMPLIANT / NEEDS FIXES (with specific fixes) / NON-COMPLIANT

## Output

- Write to `data/legal/disclosure-check-[content-name]-[date].md`
- Update your MEMORY.md with disclosure patterns
