# Product Launch Plan — Best Practices Reference

> Reference material for the `launch-plan` skill. Consult when designing launch timelines,
> coordinating across departments, and structuring phased launches.

---

## 1. Launch Timeline Best Practices

### Standard Timeline Framework

A robust product launch operates across three major phases with a total planning horizon of 6-12 months before launch day.

| Phase | Timing | % of Effort | Focus |
|-------|--------|-------------|-------|
| Pre-Launch | T-12 to T-2 weeks | 70-80% | Research, planning, asset creation, testing |
| Launch Week | T-1 to T+1 week | 10-15% | Execution, monitoring, rapid response |
| Post-Launch | T+1 to T+8 weeks | 10-15% | Optimization, feedback, iteration |

### Pre-Launch Phase (T-12 to T-2 Weeks)

**T-12 to T-8 weeks (Strategic Foundation):**
- Finalize product positioning and messaging
- Define target audience segments and personas
- Establish launch KPIs and success criteria
- Identify all departments and agents involved
- Create master timeline with dependencies mapped

**T-8 to T-4 weeks (Asset Creation):**
- Content creation: blog posts, social media, email sequences, video
- Landing page / sales page design and development
- PR materials: press release, media kit, story angles
- Paid advertising creative and campaign setup
- Support documentation: FAQ, help articles, onboarding materials

**T-4 to T-2 weeks (Testing and Readiness):**
- QA all launch assets (links, tracking, forms, payment)
- Test email sequences end-to-end
- Rehearse launch day operations
- Conduct GO/NO-GO readiness assessment
- Brief all teams on launch day responsibilities

### Launch Week (T-1 to T+1 Week)

**Day of Launch:**
- Execute launch sequence per timeline
- Monitor all channels in real-time
- Rapid response to issues, questions, feedback
- Track KPIs hourly (traffic, signups, conversions, errors)

**Rest of Launch Week:**
- Daily check-ins across all departments
- Adjust paid spend based on performance
- Respond to media coverage and social mentions
- Address early customer feedback immediately

### Post-Launch Phase (T+1 to T+8 Weeks)

- Collect and synthesize customer feedback
- Publish follow-up content (testimonials, case studies, FAQs)
- Run re-engagement campaigns for non-converters
- Conduct post-launch retrospective
- Document lessons learned for future launches

---

## 2. Cross-Department Coordination

### The Coordination Challenge

Product launches fail more often from coordination gaps than from product quality issues. Every department must know their role, timeline, and dependencies.

### RACI Matrix for Launch Tasks

Use a RACI matrix (Responsible, Accountable, Consulted, Informed) for every launch task:

| Task | Product | Content | Marketing | PR | Support | Tech |
|------|---------|---------|-----------|-----|---------|------|
| Product readiness | R/A | I | I | I | C | R |
| Launch content | C | R/A | C | I | I | I |
| Email sequences | I | R | A | I | I | I |
| Paid campaigns | I | C | R/A | I | I | I |
| Press outreach | I | C | I | R/A | I | I |
| Support readiness | C | I | I | I | R/A | C |
| Technical deploy | C | I | I | I | I | R/A |

### Coordination Cadences

| Phase | Meeting Type | Frequency | Attendees |
|-------|-------------|-----------|-----------|
| Pre-Launch (early) | Planning sync | Weekly | All department leads |
| Pre-Launch (final 2 weeks) | Readiness check | Daily | All department leads |
| Launch Week | War room | Continuous / 2x daily | Core team |
| Post-Launch | Debrief | Weekly for 4 weeks | All department leads |

### Communication Standards

- **Single source of truth:** One shared document tracks all tasks, owners, and statuses
- **Status updates:** Use consistent RED / YELLOW / GREEN status indicators
- **Escalation path:** Issues that block other departments escalate within 2 hours
- **Decision authority:** Product Manager owns the launch timeline; CEO owns GO/NO-GO
- **Async updates:** All decisions and changes documented in shared launch tracker

### Dependency Mapping

Map task dependencies explicitly:

```
Content Creation --> Content Review --> Content Approval --> Schedule/Publish
                                                              ^
Landing Page Design --> Landing Page Dev --> QA Testing -------+
                                                              ^
Email Sequence Write --> Email Review --> Email Load/Test -----+
```

Identify critical path items (tasks where delays cascade) vs. parallel workstreams.

---

## 3. Phased Launch Methodology

### Why Phase Your Launch

- Reduces risk by validating with smaller audiences first
- Creates multiple "moments" of buzz rather than a single spike
- Allows iteration based on early feedback
- Builds social proof progressively

### Phase Structure

**Phase 1: Soft Launch / Beta (2-4 weeks before public launch)**
- Release to a controlled group (existing customers, waitlist, beta testers)
- Objective: validate product, collect feedback, identify bugs
- Success criteria: activation rate, NPS, critical bug count
- Gate: fix showstoppers before proceeding

**Phase 2: Early Access / VIP Launch (1 week before public launch)**
- Open to email list, social followers, community members
- Objective: generate testimonials, early revenue, social proof
- Tactics: limited-time pricing, exclusive bonuses, early bird incentives
- Success criteria: conversion rate, revenue target, testimonial count

**Phase 3: Public Launch (Launch Day)**
- Full public release across all channels simultaneously
- Objective: maximum visibility, traffic, and conversions
- Tactics: coordinated content blitz, PR push, paid amplification
- Success criteria: traffic volume, signup/purchase targets, media coverage

**Phase 4: Sustained Launch (2-8 weeks post-launch)**
- Ongoing promotion for those who missed launch
- Objective: long-tail conversions, community building
- Tactics: case studies, evergreen content, retargeting, partnerships
- Success criteria: cumulative revenue, customer satisfaction, retention

### Phased Launch Decision Framework

| Factor | Single Big Launch | Phased Launch |
|--------|------------------|---------------|
| Product maturity | Battle-tested | Needs validation |
| Audience size | Large existing audience | Building audience |
| Risk tolerance | High confidence | Need safety net |
| Content capacity | Can produce everything at once | Need time to create |
| Budget | Large launch budget | Limited / iterative budget |

---

## 4. Launch KPIs and Success Criteria

### Pre-Launch KPIs
- Waitlist / pre-registration count
- Email open rates for teaser content
- Social engagement on pre-launch content
- Landing page conversion rate (visit to signup)

### Launch Day KPIs
- Traffic volume (unique visitors, page views)
- Conversion rate (visitor to customer)
- Revenue / units sold
- Email click-through rates
- Social shares and mentions
- Media coverage count

### Post-Launch KPIs
- Customer activation rate (% who complete onboarding)
- Day-7 and Day-30 retention
- Net Promoter Score (NPS)
- Customer support ticket volume
- Refund / cancellation rate
- Customer Acquisition Cost (CAC)

### Success Criteria Template

Define before launch:

```
LAUNCH SUCCESS CRITERIA for [Product Name]
+-- Minimum Viable Launch (must hit):
|   +-- [X] customers/signups in first [Y] days
|   +-- Conversion rate above [Z]%
|   +-- No critical bugs unresolved
+-- Target Launch (aiming for):
|   +-- [X] customers/signups in first [Y] days
|   +-- [Z]% activation rate
|   +-- NPS above [score]
+-- Stretch Goals:
    +-- [X] media mentions
    +-- [Y] social shares
    +-- Revenue of $[Z]
```

---

## 5. Common Launch Pitfalls

### Planning Pitfalls
- Starting too late (less than 4 weeks for a significant launch)
- No dependency mapping — one late deliverable derails everything
- Unclear ownership — "someone will handle it" means no one handles it
- Skipping the GO/NO-GO checkpoint

### Execution Pitfalls
- No real-time monitoring on launch day
- No escalation process for launch-day issues
- Overwhelming support team with no preparation
- Launching on a Friday or before a holiday

### Post-Launch Pitfalls
- Declaring victory too early (Day 1 metrics do not equal long-term success)
- Not collecting feedback while excitement is high
- Abandoning the launch after the first week
- Not documenting lessons learned

---

## 6. Launch Communication Templates

### Internal Launch Brief (Share with all departments)

```
LAUNCH BRIEF: [Product Name]
Launch Date: [Date]
Launch Type: [Soft/Phased/Big Bang]

WHAT: [One-sentence product description]
WHO: [Target audience]
WHY NOW: [Why this timing matters]

KEY MESSAGES:
1. [Primary message]
2. [Supporting message]
3. [Supporting message]

EACH DEPARTMENT'S ROLE:
- Content: [tasks and deadlines]
- Marketing: [tasks and deadlines]
- PR: [tasks and deadlines]
- Support: [tasks and deadlines]
- Tech: [tasks and deadlines]

TIMELINE: [Link to master timeline]
TRACKER: [Link to task tracker]
```

---

## Sources

- [Product Launch Strategy Templates (Monday.com)](https://monday.com/blog/rnd/product-launch-strategy-template/)
- [Product Launch Timeline: Stages, Checklist, & Tips (Atlassian)](https://www.atlassian.com/agile/product-management/product-launch-timeline)
- [The GTM Product Launch Strategy Checklist (Highspot)](https://www.highspot.com/blog/product-launch-guide/)
- [How to Create a Product Launch Plan Roadmap (ProductPlan)](https://www.productplan.com/learn/product-launch-plan-roadmap/)
- [Build a Product Launch Plan That Works (Product School)](https://productschool.com/blog/product-marketing/product-launch-plan)
- [Product Launch Checklist (Aha!)](https://www.aha.io/roadmapping/guide/release-management/what-is-a-good-product-launch-checklist)
