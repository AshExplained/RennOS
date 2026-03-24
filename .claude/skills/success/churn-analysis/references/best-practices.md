# Churn Analysis — Best Practices Reference

> Reference material for the `churn-analysis` skill. Consult when analyzing churn patterns,
> running cohort analysis, identifying leading indicators, and designing intervention strategies.

---

## 1. Churn Frameworks

### Core Churn Metrics

| Metric | Formula | What It Tells You |
|--------|---------|-------------------|
| Customer Churn Rate | (Customers lost in period / Customers at start of period) x 100 | Basic attrition rate |
| Revenue Churn Rate | (MRR lost in period / MRR at start of period) x 100 | Financial impact of churn |
| Net Revenue Retention | ((MRR start + expansion - contraction - churn) / MRR start) x 100 | Growth vs. loss balance |
| Logo Churn | Count of customers who cancelled | Absolute loss volume |
| Gross Churn | Total revenue lost (before expansion) | Worst-case revenue loss |

### Industry Benchmarks

| Business Type | Good Churn Rate | Average | Concerning |
|--------------|----------------|---------|------------|
| SaaS (B2B) | < 5% annual | 5-7% annual | > 10% annual |
| SaaS (B2C) | < 5% monthly | 5-7% monthly | > 8% monthly |
| Subscription/membership | < 7% monthly | 7-10% monthly | > 12% monthly |
| Digital products/courses | < 10% (after first period) | 10-20% | > 25% |
| Creator/community | < 8% monthly | 8-15% monthly | > 15% monthly |

### Churn Categories

Understand the type of churn to address it correctly:

| Type | Definition | Example | Intervention |
|------|-----------|---------|-------------|
| Voluntary | Customer actively cancels | "I don't need this anymore" | Retention offer, feedback loop |
| Involuntary | Payment fails, card expires | Failed charge, expired card | Dunning emails, card update prompts |
| Seasonal | Churn spikes at predictable times | Post-holiday, end of school year | Anticipate and pre-engage |
| Competitive | Customer switches to competitor | "I found something better" | Differentiation, win-back campaigns |
| Value | Customer does not see enough value | Low engagement before cancel | Onboarding improvement, engagement nudges |

---

## 2. Cohort Analysis Methodology

### What Is Cohort Analysis?

Instead of looking at a single blended churn rate, cohort analysis tracks how groups of customers (segmented by a shared characteristic) retain over time. This reveals patterns that aggregate metrics hide.

### Types of Cohorts

| Cohort Type | Segmentation Basis | What It Reveals |
|-------------|-------------------|----------------|
| Acquisition cohort | Signup month/week | Is product retention improving over time? |
| Channel cohort | Acquisition source | Which channels bring the most retained customers? |
| Plan cohort | Pricing tier | Which plans have best retention? |
| Feature cohort | Feature adoption | Which features correlate with retention? |
| Behavior cohort | Usage patterns | What behaviors predict long-term retention? |

### Building a Cohort Retention Table

```
Signup Month | Month 0 | Month 1 | Month 2 | Month 3 | Month 6 | Month 12
-------------|---------|---------|---------|---------|---------|----------
Jan 2026     | 100%    | 82%     | 71%     | 65%     | 52%     | --
Feb 2026     | 100%    | 85%     | 74%     | 68%     | --      | --
Mar 2026     | 100%    | 88%     | 78%     | --      | --      | --
```

### Interpreting Cohort Data

- **Improving cohorts:** Later cohorts retain better = product/onboarding is improving
- **Declining cohorts:** Later cohorts retain worse = something degraded (quality, expectations, channel mix)
- **Cohort convergence:** All cohorts stabilize at similar rates = natural floor found
- **Steep early drop:** Big loss in Month 1 = onboarding or expectation mismatch
- **Gradual late decline:** Slow bleed after Month 3+ = value erosion over time

### Key Questions Cohort Analysis Answers

1. Is our product getting better at retaining customers?
2. Did pricing/product changes improve or worsen retention for specific cohorts?
3. Are customers from paid channels retaining differently than organic?
4. At what point do most customers churn (week 1? month 3? renewal?)?
5. Which customer segments have the best and worst retention curves?

---

## 3. Leading Churn Indicators

### Behavioral Warning Signs

These behaviors predict churn before it happens. Monitor them continuously.

| Indicator | Risk Level | Typical Timeline to Churn |
|-----------|-----------|--------------------------|
| Login frequency declining | Medium | 30-60 days |
| Feature usage dropping | Medium | 30-60 days |
| No login for 14+ days | High | 14-30 days |
| Support ticket volume increasing | Medium | 30-45 days |
| Negative NPS/CSAT score | High | 15-30 days |
| Billing page visits (checking price) | High | 7-14 days |
| Downgrade inquiry | Very High | 7-14 days |
| Export data / request data download | Very High | 3-7 days |
| Stopped opening emails | Medium | 30-60 days |
| Reduced purchase frequency | Medium | 30-60 days |

### Building a Churn Risk Score

Assign weights to each indicator and calculate a composite risk score:

```
CHURN RISK SCORE (0-100)
========================
Login frequency decline (last 30 days)        Weight: 20
Feature usage decline (last 30 days)           Weight: 15
Days since last login                          Weight: 15
Support sentiment (negative tickets)           Weight: 15
Email engagement decline                       Weight: 10
NPS/CSAT score (if recent)                     Weight: 10
Payment failure history                        Weight: 10
Contract/subscription age                      Weight: 5

Score 0-25:  LOW RISK    — Normal engagement
Score 26-50: MEDIUM RISK — Watch and nurture
Score 51-75: HIGH RISK   — Proactive intervention needed
Score 76-100: CRITICAL   — Immediate personal outreach
```

### The "Negative Event" Trigger List

Certain single events should trigger immediate intervention regardless of overall risk score:
- Customer submits a complaint or negative review
- Customer contacts support about cancellation
- Customer mentions a competitor
- Payment fails twice in a row
- Customer explicitly expresses dissatisfaction

---

## 4. Intervention Strategies

### Intervention Tiers

Match intervention intensity to risk level:

**Tier 1: Nurture (Low Risk — Score 0-25)**
- Automated engagement emails with tips and value reminders
- Feature spotlight emails showing underused capabilities
- Community invitations and content recommendations
- Purpose: maintain engagement, prevent drift

**Tier 2: Re-Engage (Medium Risk — Score 26-50)**
- Personalized check-in email from the brand
- Usage tips based on their specific behavior patterns
- Exclusive content or early access to new features
- Survey to understand their needs and satisfaction
- Purpose: reignite engagement, show you notice them

**Tier 3: Retain (High Risk — Score 51-75)**
- Personal outreach (not automated — genuinely personal)
- Special retention offer (discount, extended trial, bonus content)
- 1-on-1 onboarding or training session
- Direct ask: "What would make this valuable for you?"
- Purpose: prevent cancellation, address root cause

**Tier 4: Save (Critical Risk — Score 76-100)**
- Direct outreach from the user personally
- Custom solution or accommodation
- Honest conversation about fit and expectations
- If they are leaving: exit interview for learning
- Purpose: save if possible, learn if not

### Intervention Timing

| Trigger | Response Time | Channel |
|---------|--------------|---------|
| Risk score crosses 50 | Within 48 hours | Email |
| Risk score crosses 75 | Within 24 hours | Personal email or DM |
| Cancellation request | Within 4 hours | Personal message |
| Negative review/complaint | Within 2 hours | Direct response |
| Payment failure | Immediately (automated) | Email + in-app |

### Win-Back Campaigns

For customers who have already churned:

| Timing | Approach | Offer |
|--------|----------|-------|
| 1-7 days post-churn | "We miss you" | Address their specific reason for leaving |
| 14-30 days post-churn | "Here is what is new" | Show improvements since they left |
| 60-90 days post-churn | "Come back" offer | Discount or bonus to return |
| 6+ months post-churn | Re-introduction | Treat as new prospect, show evolution |

---

## 5. Churn Analysis Report Structure

```
CHURN ANALYSIS: [Product] — [Period]

EXECUTIVE SUMMARY
[2-3 sentences: churn rate, trend, top concern]

CHURN METRICS
- Customer churn rate: [X]% (vs [Y]% last period)
- Revenue churn rate: [X]% (vs [Y]% last period)
- Net revenue retention: [X]%
- Customers lost: [N]

COHORT ANALYSIS
[Retention table by acquisition cohort]
[Key finding: are newer cohorts retaining better or worse?]

CHURN REASONS (from cancellation surveys, support data, feedback)
1. [Reason] — [% of churned customers]
2. [Reason] — [% of churned customers]
3. [Reason] — [% of churned customers]

LEADING INDICATORS
- [Indicator] trending [up/down] — [implication]
- [Indicator] trending [up/down] — [implication]

AT-RISK CUSTOMERS
- High risk: [N] customers — [intervention plan]
- Medium risk: [N] customers — [intervention plan]

RECOMMENDED INTERVENTIONS
1. [Action] — Expected impact: [X]
2. [Action] — Expected impact: [X]
3. [Action] — Expected impact: [X]
```

---

## 6. Measuring Intervention Effectiveness

### Before/After Cohort Comparison

Compare cohorts before and after an intervention to isolate its effect:
- **Control:** Cohorts from before the intervention
- **Treatment:** Cohorts after the intervention
- **Metric:** Retention rate at the same point in customer lifecycle

### Key Success Metrics

| Metric | How to Measure |
|--------|---------------|
| Save rate | % of at-risk customers who were retained after intervention |
| Time to churn extension | Did intervention delay churn even if it did not prevent it? |
| Intervention ROI | Revenue saved / cost of intervention |
| Feedback quality | Did at-risk customers provide actionable feedback? |
| Win-back rate | % of churned customers who returned |

---

## Sources

- [Churn Analysis: The Complete Guide 2026 (UserIntuition)](https://www.userintuition.ai/posts/churn-analysis-complete-guide/)
- [Cohort Analysis: Your Secret Weapon to Reduce Churn (Peel Insights)](https://www.peelinsights.com/post/the-anti-churn-formula)
- [Customer Churn Analysis: Steps + Best Practices (Saras Analytics)](https://www.sarasanalytics.com/blog/customer-churn-analysis)
- [Churn Analysis: The Cohort Framework (Growth Terminal)](https://thegrowthterminal.com/blog/churn-analysis-the-cohort-framework-that-cuts-cac-payback-by-30/)
- [Cohort Analysis: Complete Guide (Improvado)](https://improvado.io/blog/cohort-analysis)
- [Churn Risk Analysis: Templates & Prevention (Count)](https://count.co/metric/churn-risk-analysis)
- [Customer Churn Analysis: Predict & Reduce (Yotpo)](https://www.yotpo.com/blog/customer-churn-analysis/)
