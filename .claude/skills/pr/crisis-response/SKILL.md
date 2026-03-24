---
name: crisis-response
user-invocable: false
description: Draft a crisis response plan — assessment, messaging strategy, timeline, and communication channels.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Crisis Response Playbook

## Inputs

- $ARGUMENTS — The crisis situation: what happened, where, current reach
- `data/brand/brand-dna.md` — Brand identity
- `data/social/` — Mention scans, sentiment reports from Social Listener
- `data/pr/` — PR strategy for alignment

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for crisis communication methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read `data/brand/brand-dna.md` and all available context about the crisis
4. Read Social Listener's mention scans and sentiment data from `data/social/`
5. Assess the situation:
   - **Severity** — Low / Medium / High / Critical
   - **Reach** — How many people are aware?
   - **Trajectory** — Growing, stable, or dying down?
   - **Source** — Where did it originate? Is it coordinated?
6. Draft the crisis response plan:
   - **Immediate actions** (first 1-2 hours)
   - **Public response** — Statement/message (draft 2-3 variants: apologetic, explanatory, defensive — recommend the right one)
   - **Channel strategy** — Where to respond (social, blog, email, press)
   - **Timeline** — Response schedule over next 24-72 hours
   - **Monitoring plan** — What to track, when to escalate
   - **Do NOT do** — Common mistakes to avoid in this specific situation
7. Flag if legal review is needed before any public statement
8. Recommend whether to engage or ignore (sometimes silence is the best response)

## Output

- Write to `data/pr/crisis-response-[topic]-[date].md`
- **Note:** This is the highest-stakes output in RennOS. Be calm, measured, strategic. No knee-jerk reactions.
- Update your MEMORY.md with crisis patterns and response effectiveness
