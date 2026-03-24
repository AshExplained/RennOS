---
name: engagement-playbook
user-invocable: false
description: Create playbooks for specific social scenarios — viral moment, controversy, collaboration, product launch, etc.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Engagement Playbook Playbook

## Inputs

- $ARGUMENTS — Scenario type or specific situation (e.g., "viral moment", "product launch", "controversy response")
- `data/brand/brand-dna.md` — Brand identity and voice
- `data/strategy/audience-personas.md` — Audience context

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for engagement scenarios and decision frameworks
2. Apply the scenario playbooks and escalation criteria from the reference
3. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
4. Identify the scenario and research best practices via web
5. Build a step-by-step playbook for the scenario:
   - **Viral moment:** How to ride it — timing, content formats, engagement approach, follow-up strategy
   - **Controversy/crisis:** How to respond — acknowledge, address, timeline, what NOT to do
   - **Collaboration opportunity:** How to engage — evaluation criteria, outreach template, negotiation points
   - **Product launch:** Social launch plan — teaser sequence, launch day, post-launch engagement
   - **Milestone celebration:** How to mark it — content ideas, community involvement, gratitude
   - Adapt based on $ARGUMENTS scenario
6. Include do's and don'ts specific to the scenario
7. Include template responses/posts for quick use
8. Define success metrics for the scenario

## Output

- Write to `data/social/playbook-[scenario]-[date].md`
- Update your MEMORY.md with scenario patterns and what approaches work
