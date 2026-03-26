# Workflow: Product Launch

> From product idea to live launch — spec, design, build, market, ship.

## Trigger
- "Launch [product name]"
- "I want to build and launch [product idea]"
- "Let's plan a product launch"

## Profile
Full RennOS, Brand & Business

## Steps

### Phase 1: Validate & Spec

#### 1. Market Validation
**Agent:** @product-strategist
**Skill:** market-validation
**Input:** Product idea from user + `data/strategy/audience-personas.md`
**Output:** Validation report — demand signal, competitive gap, audience fit

#### 2. Product Spec
**Agent:** @product-designer
**Skill:** product-spec
**Input:** Validation report + user's vision
**Output:** Product spec document → `data/product/[product-name]-spec.md`

#### 3. User Approval Gate (Spec)
**CEO agent presents:** Product spec for review.
**User approves → Phase 2.**

### Phase 2: Design & Build (Dept 10 + 14)

#### 4. UI/UX Design
**Agent:** @ux-designer
**Skill:** stitch-design (if applicable), user-flow, wireframe
**Input:** Product spec
**Output:** Screens/wireframes in Stitch or text specs

#### 5. Design Freeze Gate
**CEO agent presents:** Designs to user.
**User approves designs → coding begins.**
**This is a hard gate per ceo-memory/workflows.md.**

#### 6. Sprint Planning & Build
**Agent:** @scrum-master
**Skills:** sprint-planning
**Action:** Breaks spec into stories, plans sprint in Asana
**Team:** @full-stack-developer, @qa-engineer, @devops-engineer execute

#### 7. UAT Gate
**CEO agent presents:** Staging build + Asana task summary.
**User tests and approves → production deploy.**

### Phase 3: Launch

#### 8. Launch Plan
**Agent:** @launch-manager
**Skill:** launch-plan
**Input:** Product spec + launch date
**Output:** Cross-department launch plan with timeline

#### 9. Launch Content (parallel)
**Agent:** @long-form-writer → launch blog post
**Agent:** @short-form-writer → social announcements
**Agent:** @script-writer → launch video script
**Agent:** @email-marketing-manager → launch email sequence

#### 10. PR Push
**Agent:** @pr-strategist
**Skill:** story-angle
**Input:** Product details + launch plan
**Agent:** @media-outreach-specialist → pitch to relevant media

#### 11. Launch Checklist
**Agent:** @launch-manager
**Skill:** launch-checklist
**Action:** Final pre-launch verification across all departments

#### 12. User Approval Gate (Go Live)
**CEO agent presents:** Launch readiness summary.
**User says go → deploy + publish all content.**

### Phase 4: Post-Launch

#### 13. Monitor
**Agent:** @social-listener → mention/sentiment tracking
**Agent:** @performance-analyst → early metrics

#### 14. Post-Launch Review
**Agent:** @launch-manager
**Skill:** post-launch-review
**Input:** First 7 days of data
**Output:** What worked, what didn't, next iteration

## Data Flow
```
data/product/[product-name]-spec.md ← spec
data/product/[product-name]-launch.md ← launch plan
data/content/drafts/ ← launch content
data/content/content-calendar.md ← launch schedule
```
