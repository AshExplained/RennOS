---
name: reputation-scan
user-invocable: false
description: Proactively scan for reputation threats, negative coverage, and emerging PR risks.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Reputation Scan Playbook

## Inputs

- $ARGUMENTS — Brand name/handles, specific concern if any
- `data/brand/brand-dna.md` — Brand context
- `data/social/` — Existing mention scans from Social Listener

## Steps

1. Read `data/brand/brand-dna.md` and any existing mention scans from `data/social/`
2. Search the web for:
   - Negative press mentions or articles
   - Negative reviews or complaints
   - Social media backlash or controversy
   - Competitor attacks or comparisons
   - Any content that misrepresents the brand
3. For each finding, assess:
   - **Threat level** (1-10)
   - **Reach** — How visible is this?
   - **Trend** — Growing or stable?
   - **Action needed** — Respond, monitor, or ignore?
4. Prioritize threats by severity and urgency
5. For high-severity items, draft a preliminary response recommendation

## Output

- Write to `data/pr/reputation-scan-[date].md`
- Update your MEMORY.md with reputation threat patterns and vulnerabilities
