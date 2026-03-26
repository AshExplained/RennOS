# Workflow: Crisis Response

> Negative press, controversy, or reputation threat — fast, coordinated response.

## Trigger
- @social-listener flags a negative trend or mention spike
- "There's a controversy about [topic]"
- "I'm getting negative feedback about [thing]"
- "We need damage control"

## Profile
Full RennOS, Brand & Business

## Priority: HIGH — This workflow takes precedence over all other work.

## Steps

### 1. Assess Severity
**Agent:** @crisis-manager
**Skill:** reputation-scan
**Input:** The flagged content/situation
**Output:** Severity assessment (LOW / MEDIUM / HIGH / CRITICAL) + recommended response level
**Decision:**
- LOW → Monitor only, no public response (skip to step 6)
- MEDIUM → Prepare response, don't publish yet (steps 2-5)
- HIGH/CRITICAL → Fast-track response (all steps, expedited)

### 2. Gather Context
**Agent:** @social-listener
**Skill:** mention-scan, sentiment-report
**Input:** Brand name + controversy keywords
**Output:** Full picture — who's saying what, volume, sentiment trend, key voices

### 3. Draft Response
**Agent:** @crisis-manager
**Skill:** crisis-response
**Input:** Severity assessment + context from step 2 + `data/brand/brand-dna.md`
**Output:** Draft public statement aligned with brand voice
**Notes:** Response must be honest, empathetic, and on-brand. Never defensive or dismissive.

### 4. Legal Check
**Agent:** @compliance-monitor
**Skill:** disclosure-check
**Input:** Draft response
**Output:** Legal risk flags, recommended changes

### 5. User Approval Gate (MANDATORY)
**CEO agent presents:** Draft response + context + legal notes.
**User approves exact wording → publish.**
**No exceptions — crisis responses NEVER auto-publish.**

### 6. Monitor & Follow-up
**Agent:** @social-listener
**Action:** Increased monitoring frequency for 48-72 hours
**Agent:** @crisis-manager
**Action:** Track sentiment recovery, prepare follow-up if needed

## Data Flow
```
data/pr/crisis-log.md ← document the incident and response
data/brand/brand-dna.md ← response must align
```

## Rules
- Speed matters but accuracy matters more
- Never respond emotionally — wait for the assessment
- If in doubt, say less, not more
- One spokesperson (the user) — agents draft, user speaks
