# Workflow: Partnership Deal

> End-to-end sponsorship or collaboration — from inbound/outbound to signed deal.

## Trigger
- "We got a sponsorship inquiry from [brand]"
- "I want to reach out to [brand] for a partnership"
- "Evaluate this deal: [details]"

## Profile
Full RennOS, Brand & Business

## Steps

### 1. Research Partner
**Agent:** @partnership-scout
**Skill:** partner-research
**Input:** Partner name/URL from user
**Output:** Partner brief — audience overlap, brand fit, reach, risk flags
**Notes:** Checks brand alignment against `data/brand/brand-dna.md`

### 2. Evaluate Fit
**Agent:** @sponsorship-manager
**Skill:** sponsorship-eval
**Input:** Partner brief from step 1
**Output:** Fit score + recommendation (pursue / pass / negotiate terms)
**Decision:** If pass → CEO agent tells user why. If pursue → continue.

### 3. Structure Deal
**Agent:** @deal-negotiator
**Skill:** deal-structure
**Input:** Partner brief + fit evaluation
**Output:** Proposed terms — deliverables, timeline, pricing, exclusivity
**Notes:** Reads `data/finance/rate-card.md` for pricing benchmarks.

### 4. User Approval Gate (Terms)
**CEO agent presents:** Proposed deal terms.
**User approves terms → proceed.**
**User adjusts → back to step 3 with changes.**

### 5. Draft Proposal
**Agent:** @deal-negotiator
**Skill:** proposal-draft
**Input:** Approved terms
**Output:** Formal proposal document

### 6. Contract Review
**Agent:** @contract-reviewer
**Skill:** contract-review
**Input:** Proposal or incoming contract
**Output:** Risk flags, missing terms, recommended changes
**Notes:** If the partner sends their contract, this step reviews THEIR terms.

### 7. User Approval Gate (Contract)
**CEO agent presents:** Contract review summary + flagged items.
**User signs off → execute.**

### 8. Post-Deal Setup
**Agent:** @content-scheduler
**Skill:** content-calendar
**Action:** Schedule sponsored content deliverables
**Agent:** @invoice-payments-manager
**Skill:** invoice-draft
**Action:** Create invoice for the deal

## Data Flow
```
data/partnerships/[partner-name].md ← partner brief + deal terms
data/partnerships/media-kit.md ← shared with partner if needed
data/finance/rate-card.md ← pricing reference
data/content/content-calendar.md ← deliverable scheduling
```
