# Escalation Plan — Best Practices Reference

> Reference material for the `escalation-plan` skill. Consult when designing escalation tiers,
> setting response time standards, classifying severity, and applying de-escalation techniques.

---

## 1. Escalation Tier Design

### Standard Tier Structure

A well-designed escalation framework uses 4-5 tiers, each with increasing authority and expertise:

| Tier | Handler | Scope | Authority |
|------|---------|-------|-----------|
| Tier 0 | Self-Service | FAQ, knowledge base, chatbot | Automated resolution |
| Tier 1 | Front-Line Support | Common questions, how-to, account issues | Standard responses, basic troubleshooting |
| Tier 2 | Specialist | Technical bugs, billing disputes, complex issues | Access to tools, authority to escalate |
| Tier 3 | Leadership / Expert | Unhappy customers, retention risks, PR issues | Authority to make exceptions, offer compensation |
| Tier 4 | Owner (the user) | Legal threats, major partnerships, personal requests | Full authority |

### Tier Design Principles

1. **Clear boundaries** — Each tier has explicit criteria for what it handles vs. what it escalates
2. **No gaps** — Every possible issue type maps to a tier
3. **No dead ends** — Every issue has a path to resolution, even if it requires escalation
4. **Minimal hand-offs** — Resolve at the lowest tier possible to reduce customer effort
5. **Information flows up** — Each escalation includes full context so customers do not repeat themselves

### Mapping Issues to Tiers

| Issue Type | Starting Tier | Escalation Path |
|-----------|--------------|-----------------|
| How-to / getting started | Tier 0 (self-service) -> Tier 1 | Tier 0 -> 1 |
| Account access / password | Tier 1 | Tier 1 -> 2 if complex |
| Product bug / error | Tier 1 (log) -> Tier 2 | Tier 1 -> 2 -> 3 if critical |
| Billing / refund request | Tier 1 -> Tier 2 | Tier 1 -> 2 -> 3 for disputes |
| Feature request | Tier 1 (log) | No escalation — logged for product |
| Negative experience / complaint | Tier 2 | Tier 2 -> 3 if risk of churn |
| Cancellation threat | Tier 2 -> Tier 3 | Tier 2 -> 3 -> 4 for high-value |
| Legal / compliance issue | Tier 4 immediately | Skip tiers |
| PR / public reputation risk | Tier 3 -> Tier 4 | Fast-track to leadership |
| Partnership / collaboration inquiry | Tier 3 | Tier 3 -> 4 for decisions |

### Tier Staffing Considerations

- **Tier 0:** Fully automated (FAQ, knowledge base, chatbot)
- **Tier 1:** Largest team, handles highest volume. Train for empathy and efficiency.
- **Tier 2:** Smaller team with specialized knowledge. Cross-train across product, billing, and technical domains.
- **Tier 3:** 1-2 experienced team members or the user's direct support. Authority to make exceptions.
- **Tier 4:** the user only. Reserved for high-stakes situations.

---

## 2. Response Time Standards

### SLA Framework by Tier and Severity

| Severity | First Response | Update Frequency | Resolution Target |
|----------|---------------|-----------------|-------------------|
| Critical (service down, data loss) | 15 minutes | Every 30 minutes | 4 hours |
| High (major functionality broken) | 1 hour | Every 2 hours | 24 hours |
| Medium (partial issue, workaround exists) | 4 hours | Every 8 hours | 48 hours |
| Low (minor issue, cosmetic, feature request) | 24 hours | Every 24 hours | 5 business days |

### Response Time by Channel

| Channel | First Response Target | Notes |
|---------|--------------------|-------|
| Email | 4-8 hours | Acknowledge within 1 hour if possible |
| Live chat | 2-5 minutes | If offered, must be staffed |
| Social media (public) | 1-2 hours | Public visibility increases urgency |
| Social media (DM) | 4-8 hours | Same as email |
| Phone/call | Immediate (if offered) | Voicemail return within 2 hours |
| In-app support | 4-8 hours | Acknowledge immediately with auto-response |

### Auto-Escalation Triggers

Set automatic escalation when approaching SLA thresholds:

```
At 50% of SLA time:  Alert assigned agent
At 80% of SLA time:  Auto-escalate to next tier
At 100% of SLA time: Alert tier lead + auto-escalate
At 150% of SLA time: Alert the user directly
```

Organizations with well-defined escalation policies resolve incidents 40% faster.

---

## 3. Severity Classification

### Severity Level Definitions

| Level | Name | Business Impact | Customer Impact | Examples |
|-------|------|----------------|----------------|---------|
| SEV-1 | Critical | Service outage, revenue loss | All customers affected, no workaround | Complete product down, payment system failure, data breach |
| SEV-2 | High | Major feature broken | Many customers affected, limited workaround | Core feature broken, significant performance degradation |
| SEV-3 | Medium | Partial issue | Some customers affected, workaround available | Secondary feature broken, intermittent errors, slow performance |
| SEV-4 | Low | Minor issue | Few customers affected, easy workaround | Cosmetic bugs, documentation errors, minor UX issues |
| SEV-5 | Informational | No immediate impact | Enhancement request or question | Feature requests, general inquiries, nice-to-have improvements |

### Severity Assessment Criteria

Ask these questions to determine severity:

1. **How many customers are affected?** (All / Many / Some / Few)
2. **Is there a workaround?** (No / Partial / Full)
3. **Is revenue being lost?** (Yes, actively / Yes, potentially / No)
4. **Is data at risk?** (Yes, compromised / Yes, at risk / No)
5. **Is brand reputation at risk?** (Public issue / Private issue / No)

### Severity Decision Matrix

```
             No Workaround    Partial Workaround    Full Workaround
All Users       SEV-1               SEV-1                SEV-2
Many Users      SEV-1               SEV-2                SEV-3
Some Users      SEV-2               SEV-3                SEV-3
Few Users       SEV-3               SEV-3                SEV-4
```

### Tier-Skip Triggers

Certain situations skip the normal escalation path:

| Trigger | Action | Rationale |
|---------|--------|-----------|
| Legal threat received | Tier 4 immediately | Legal risk requires owner involvement |
| Data breach suspected | Tier 4 + security response | Privacy and compliance obligations |
| Public social media crisis | Tier 3 + PR team | Brand reputation at stake |
| VIP / high-value customer complaint | Start at Tier 2 minimum | Higher stakes require faster resolution |
| Physical safety concern | Tier 4 + emergency services | Duty of care |

---

## 4. De-Escalation Techniques

### The HEARD Framework

Use this framework when dealing with upset customers:

| Step | Action | Example |
|------|--------|---------|
| **H** — Hear | Listen actively, do not interrupt | "I want to understand exactly what happened" |
| **E** — Empathize | Acknowledge their frustration | "I completely understand why this is frustrating" |
| **A** — Apologize | Take responsibility (even if not at fault) | "I am sorry you had this experience" |
| **R** — Resolve | Offer a concrete solution | "Here is what I can do right now to fix this" |
| **D** — Diagnose | Prevent recurrence | "I will make sure this does not happen again by..." |

### Communication Dos and Don'ts

| Do | Don't |
|----|-------|
| Use the customer's name | Use generic greetings |
| Acknowledge their feelings | Dismiss or minimize their frustration |
| Explain what you CAN do | Focus on what you CANNOT do |
| Give specific timelines | Use vague promises ("soon", "shortly") |
| Follow up proactively | Wait for them to follow up |
| Own the issue personally | Pass blame to other teams/people |
| Be honest about limitations | Overpromise and underdeliver |

### Tone Guidelines by Severity

| Severity | Tone | Key Phrases |
|----------|------|-------------|
| Critical | Urgent, reassuring, authoritative | "We are treating this as our top priority" |
| High | Serious, empathetic, action-oriented | "I understand the impact. Here is our plan" |
| Medium | Helpful, professional, clear | "Let me walk you through the solution" |
| Low | Friendly, informative, supportive | "Great question! Here is how to do that" |

### Compensation Guidelines

| Severity | Impact Duration | Compensation Range |
|----------|----------------|-------------------|
| Critical | > 4 hours | Full refund + bonus/credit + personal apology |
| Critical | 1-4 hours | Partial refund or credit + apology |
| High | Extended | Service credit or extended access |
| Medium | Resolved quickly | Thank-you note, small gesture |
| Low | Minimal | Acknowledgment and fix |

### De-Escalation Scripts

**For angry customers:**
"I hear you, and your frustration is completely valid. I take this seriously and I want to fix it right now. Here is exactly what I am going to do..."

**For customers threatening to leave:**
"I do not want you to leave, and I want to understand what would make this right for you. Can you share what would need to change for this to work?"

**For customers comparing to competitors:**
"Thank you for being honest. I want to make sure [product] is the best option for you. What specifically would you need from us?"

---

## 5. Escalation Plan Documentation

### Standard Escalation Plan Template

```
ESCALATION PLAN: [Product/Service Name]
Last Updated: [Date]
Owner: [Name]

TIER STRUCTURE
[Table of tiers with handlers, scope, authority]

SEVERITY LEVELS
[Table of severity definitions with examples]

RESPONSE TIME SLAs
[Table of SLAs by severity and channel]

ESCALATION MATRIX
[Issue type -> Starting tier -> Escalation path]

TIER-SKIP TRIGGERS
[Situations that bypass normal escalation]

COMMUNICATION TEMPLATES
[Pre-written responses for common scenarios]

CONTACTS
[Who to reach at each tier, including backup contacts]

REVIEW SCHEDULE
[When this plan is reviewed and updated]
```

### Plan Maintenance

- Review escalation plan quarterly
- Update after every major incident or process failure
- Collect feedback from support team on what is working and what is not
- Track escalation metrics: volume by tier, resolution time, customer satisfaction post-escalation
- Refine severity definitions as new issue types emerge

---

## Sources

- [Proven Escalation Policy Framework (Hyperping)](https://hyperping.com/blog/escalation-policies-guide)
- [Customer Escalation Management: Frameworks & Best Practices (GigaBPO)](https://gigabpo.com/customer-escalation-management/)
- [The Escalation Matrix: Best Practices (SupportLogic)](https://www.supportlogic.com/resources/blog/the-escalation-matrix-best-practices-and-going-beyond/)
- [Escalation Management: Strategies, Tools, and Best Practices (Apizee)](https://www.apizee.com/escalation-management.php)
- [Mastering Escalation Management Best Practices (Supportman)](https://supportman.io/articles/escalation-management-best-practices/)
- [Escalation Matrix: Step by Step Guide (Kapture)](https://www.kapture.cx/blog/ultimate-guide-design-customer-support-escalation-matrix/)
- [Escalation Management: Best Practices for Support (PartnerHero)](https://www.partnerhero.com/blog/escalation-management)
