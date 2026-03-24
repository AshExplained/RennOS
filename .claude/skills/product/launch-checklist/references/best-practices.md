# Launch Checklist — Best Practices Reference

> Reference material for the `launch-checklist` skill. Consult when building pre-launch
> checklists, defining GO/NO-GO criteria, and assessing launch readiness.

---

## 1. Pre-Launch Methodology

### The Four Pillars of Launch Readiness

Launch readiness extends beyond product completion. Assess readiness across four core pillars:

| Pillar | What It Covers | Key Question |
|--------|---------------|--------------|
| Product | Functionality, quality, stability | Does the product work as promised? |
| Market | Positioning, messaging, channels | Do we know who we are selling to and how? |
| Operations | Support, infrastructure, processes | Can we handle the volume and issues? |
| Resources | People, budget, tools | Do we have what we need to execute? |

### Checklist Design Principles

1. **Categorize by function** — Group items by department/area (Product, Content, Marketing, PR, Operations, Tech)
2. **Distinguish critical vs. non-critical** — Not all items are launch blockers
3. **Assign owners** — Every item has exactly one person responsible
4. **Set deadlines** — Each item has a "must be done by" date, not just "before launch"
5. **Include verification method** — How do you confirm the item is truly ready?

### Master Checklist Categories

**Product Readiness:**
- [ ] Product is built, tested, and functional
- [ ] Pricing is finalized and payment processing verified
- [ ] Onboarding / welcome experience is tested end-to-end
- [ ] FAQ / support documentation is published
- [ ] Known bugs are documented with severity ratings
- [ ] Rollback plan exists if critical issues emerge

**Content Readiness:**
- [ ] Launch announcement post written and approved
- [ ] Social media posts created and scheduled for all platforms
- [ ] Email launch sequence loaded, tested, and ready to send
- [ ] Landing page / sales page live, tested, and tracking
- [ ] Visual assets (images, graphics, video) finalized

**Marketing Readiness:**
- [ ] Paid ad campaigns built and ready to activate
- [ ] Tracking pixels and analytics verified on all pages
- [ ] UTM parameters set for all campaign links
- [ ] Retargeting audiences configured
- [ ] Affiliate / partner promotions coordinated

**PR Readiness:**
- [ ] Press release drafted, reviewed, and approved
- [ ] Media list finalized and pitches prepared
- [ ] Embargo dates communicated (if applicable)
- [ ] Spokesperson briefed with talking points

**Operations Readiness:**
- [ ] Launch timeline confirmed with all departments
- [ ] Support team briefed on product and common questions
- [ ] Escalation paths defined for launch-day issues
- [ ] Contingency plans for common failures (site down, payment fail, etc.)
- [ ] Launch-day communication channels established (Slack, war room, etc.)

**Technical Readiness:**
- [ ] Server/infrastructure scaled for expected traffic
- [ ] SSL certificates valid and configured
- [ ] CDN caching configured properly
- [ ] Monitoring and alerting active
- [ ] Database backups verified

---

## 2. GO/NO-GO Decision Framework

### What Is a GO/NO-GO Decision?

A GO/NO-GO decision is a formal checkpoint where stakeholders evaluate whether all critical conditions are met to proceed with launch. It is not a rubber stamp — it must be a genuine decision point with the power to delay launch.

### Three-Outcome Model

| Decision | Criteria | Action |
|----------|----------|--------|
| **GO** | All critical items green. Known issues have documented mitigations. Rollback plan tested. | Proceed with launch as planned |
| **CONDITIONAL GO** | Minor items outstanding. Clear path to resolution before launch. Acceptable risk level documented. | Proceed with conditions — specify what must be resolved and by when |
| **NO-GO** | One or more critical items not ready. Unacceptable risk with no viable mitigation. | Delay launch. Define new target date and remediation plan. |

### Scoring Methodology

Rate each checklist category on a weighted scale:

| Category | Weight | Status Options |
|----------|--------|---------------|
| Product Readiness | 30% | GREEN (ready) / YELLOW (minor issues) / RED (blocker) |
| Content Readiness | 15% | GREEN / YELLOW / RED |
| Marketing Readiness | 15% | GREEN / YELLOW / RED |
| PR Readiness | 10% | GREEN / YELLOW / RED |
| Operations Readiness | 15% | GREEN / YELLOW / RED |
| Technical Readiness | 15% | GREEN / YELLOW / RED |

**Decision rules:**
- Any RED in Product or Technical = automatic NO-GO
- Two or more REDs in any category = NO-GO
- All GREEN = GO
- Mix of GREEN and YELLOW = CONDITIONAL GO (document conditions)

### GO/NO-GO Meeting Structure

**Before the meeting:**
- Each department lead completes their checklist section
- All items marked GREEN, YELLOW, or RED with notes
- Issues documented with severity, owner, and remediation plan

**Meeting agenda (30-60 minutes):**
1. **Category walkthrough** (20 min) — Each lead presents their section status
2. **Risk assessment** (10 min) — What are remaining risks? What is the mitigation plan?
3. **Blocker discussion** (10 min) — Can RED/YELLOW items be resolved? By when?
4. **Decision** (5 min) — GO / CONDITIONAL GO / NO-GO with clear reasoning
5. **Next steps** (5 min) — If GO: confirm launch sequence. If NO-GO: set new date.

**After the meeting:**
- Decision documented and shared with all stakeholders
- If CONDITIONAL GO: conditions tracked as action items with deadlines
- If NO-GO: post-mortem on what caused delay, revised timeline published

---

## 3. Launch Readiness Assessment

### The 36-Question Framework

A comprehensive readiness assessment covers nine sections with four questions each. Each question gets a YES/NO answer with adjustable weighting:

**Section 1: Product Quality**
1. Has the product passed all QA test cases?
2. Are known bugs classified and none are severity-critical?
3. Has the product been tested by real users (beta/UAT)?
4. Is the rollback/revert process documented and tested?

**Section 2: User Experience**
5. Is the onboarding flow complete and tested?
6. Can users accomplish the core value proposition within 5 minutes?
7. Are error messages clear and helpful (no technical jargon)?
8. Has the product been tested across target devices/browsers?

**Section 3: Infrastructure**
9. Can infrastructure handle 3x expected peak traffic?
10. Are monitoring dashboards and alerts configured?
11. Is the deployment pipeline tested and repeatable?
12. Are database backups running and verified?

**Section 4: Content and Messaging**
13. Is all launch content written, reviewed, and approved?
14. Are all links, CTAs, and forms tested and working?
15. Is content scheduled across all planned channels?
16. Do all materials align with Brand DNA?

**Section 5: Marketing and Sales**
17. Are paid campaigns built and ready to activate?
18. Is tracking (analytics, pixels, UTMs) verified?
19. Are landing pages converting above minimum threshold?
20. Is the sales/purchase flow tested end-to-end?

**Section 6: Support Readiness**
21. Is the support team briefed on the product?
22. Are FAQ and help documentation published?
23. Is the escalation path documented and communicated?
24. Are support tools and templates ready?

**Section 7: Communication**
25. Are all stakeholders informed of launch date and their roles?
26. Is the launch-day communication plan documented?
27. Are contingency communication templates prepared?
28. Is the post-launch communication cadence defined?

**Section 8: Legal and Compliance**
29. Are terms of service and privacy policy updated?
30. Is regulatory compliance verified (if applicable)?
31. Are required disclosures in place?
32. Is intellectual property protected?

**Section 9: Post-Launch Plan**
33. Is the feedback collection mechanism ready?
34. Is the post-launch monitoring plan defined?
35. Is the iteration/improvement backlog prepared?
36. Is the post-launch retrospective scheduled?

### Readiness Score Calculation

```
Total YES answers / 36 = Readiness Percentage

90-100% = Strong GO
75-89%  = Conditional GO (review NO items)
60-74%  = Weak — likely delay unless NO items are non-critical
Below 60% = NO-GO — significant gaps remain
```

### Critical vs. Non-Critical Items

Not all checklist items carry equal weight. Define upfront which items are:

- **Launch Blockers** (must be YES for GO): Product works, payments process, core content live, infrastructure stable
- **Important but not blocking** (should be YES): All social posts scheduled, all PR pitches sent, retargeting configured
- **Nice to have** (ideal but can launch without): Stretch content pieces, partner cross-promotions, advanced analytics

---

## 4. Contingency Planning

### Common Launch Failures and Mitigations

| Failure Scenario | Probability | Impact | Mitigation |
|-----------------|-------------|--------|------------|
| Website goes down | Medium | Critical | Load testing beforehand, CDN, auto-scaling, status page |
| Payment processing fails | Low | Critical | Test with real transactions, backup processor, manual workaround |
| Email sequence has errors | Medium | High | Send test to multiple accounts, have backup send mechanism |
| Negative press/social reaction | Low | High | Crisis communication template, monitoring alerts |
| Support volume overwhelms team | High | Medium | Pre-written responses, escalation tiers, temporary help |
| Low initial traction | Medium | Medium | Backup promotion plan, additional paid budget, influencer outreach |

### Rollback Criteria

Define conditions under which you would roll back the launch:
- Critical security vulnerability discovered
- Payment processing failure rate above 5%
- Server uptime below 95% in first 4 hours
- Major factual error in product or content

---

## Sources

- [Go/No Go Production Readiness Checklist (IPM)](https://instituteprojectmanagement.com/blog/go-no-go-production-readiness-checklist/)
- [Launch Readiness Checklist / Go/No-Go Framework (GitScrum)](https://docs.gitscrum.com/en/best-practices/launch-readiness-checklist)
- [Market Launch Readiness Assessment Framework (Incurvo)](https://www.incurvo.com/launch-readiness-framework)
- [Three Dimensions of Product Launch (Pragmatic Institute)](https://www.pragmaticinstitute.com/resources/articles/product/goals-readiness-and-constraints-the-three-dimensions-of-product-launch/)
- [Product Launch Checklist: 25 Steps (Christian Strunk)](https://www.christianstrunk.com/blog/product-launch-checklists)
- [Product Readiness Toolkit (ArcheSys)](https://www.archesys.io/toolkits/templates/product-readiness)
