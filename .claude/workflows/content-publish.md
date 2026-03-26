# Workflow: Content Publish

> End-to-end blog post or article — from idea to published.

## Trigger
- "Write a blog post about [topic]"
- "Publish an article on [topic]"
- "Turn this idea into a blog post: [idea]"

## Profile
Full RennOS, Brand & Business

## Steps

### 1. Research & Outline
**Agent:** @long-form-writer
**Skill:** blog-post
**Input:** Topic from user + `data/brand/brand-dna.md` + `data/strategy/audience-personas.md`
**Output:** Draft saved to `data/content/drafts/[slug].md`
**Notes:** Writer reads brand voice and audience before drafting. If the topic needs research, the CEO agent runs `/deep-research` first and passes findings to the writer.

### 2. Editorial Review
**Agent:** @content-editor
**Skill:** edit-review
**Input:** Draft from step 1
**Output:** Annotated feedback + revised draft
**Decision:** If major issues → return to step 1 with edit notes. If minor/clean → proceed.

### 3. SEO Optimization
**Agent:** @seo-specialist
**Skill:** seo-optimize
**Input:** Edited draft from step 2
**Output:** SEO-optimized version with meta title, description, keywords, internal links
**Notes:** Reads `data/analytics/kpi-dashboard.md` for current top-performing keywords if available.

### 4. Brand Voice Check
**Agent:** @content-editor
**Skill:** voice-check
**Input:** Final draft from step 3
**Output:** Pass/fail with notes
**Decision:** If fail → minor edits and re-check. Usually passes after editorial review.

### 5. Schedule
**Agent:** @content-scheduler
**Skill:** content-calendar
**Input:** Final approved draft
**Output:** Scheduled slot in `data/content/content-calendar.md`

### 6. User Approval Gate
**CEO agent presents:** Final draft + scheduled time to the user.
**User approves → proceed to publish.**
**User requests changes → back to relevant step.**

### 7. Publish
**Agent:** @platform-manager
**Skill:** post-publish
**Input:** Approved draft + platform target
**Output:** Published confirmation

### 8. Repurpose (Optional)
**Agent:** @content-repurposer
**Skill:** repurpose
**Input:** Published blog post
**Output:** Thread, social posts, newsletter section saved to `data/content/drafts/`
**Notes:** CEO agent asks user: "Want me to repurpose this into social posts?" If yes, kick off this step.

## Data Flow
```
data/content/drafts/[slug].md  ← all steps read/write here
data/content/content-calendar.md ← step 5 writes here
data/brand/brand-dna.md ← steps 1, 4 read
data/strategy/audience-personas.md ← step 1 reads
```

## Failure Handling
- If @long-form-writer produces a weak draft → CEO agent gives specific feedback and re-delegates
- If SEO conflicts with brand voice → brand voice wins, SEO adapts
- If user rejects at approval gate → CEO agent identifies which step needs rework
