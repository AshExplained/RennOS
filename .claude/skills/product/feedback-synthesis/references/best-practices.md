# Feedback Synthesis — Best Practices Reference

> Reference material for the `feedback-synthesis` skill. Consult when categorizing feedback,
> extracting themes, counting frequency, and prioritizing insights.

---

## 1. Feedback Categorization Framework

### Multi-Dimensional Categorization

Categorize each piece of feedback across three dimensions simultaneously:

**Dimension 1: Sentiment**
| Sentiment | Definition | Signal Words |
|-----------|-----------|--------------|
| Positive | Customer expresses satisfaction, delight, or praise | "love", "great", "amazing", "easy", "helpful" |
| Negative | Customer expresses frustration, dissatisfaction, or complaint | "hate", "broken", "frustrating", "confusing", "terrible" |
| Neutral | Factual observation, question, or suggestion without strong emotion | "wondering", "could you", "it would be nice if" |
| Mixed | Contains both positive and negative elements | "I love X but Y is frustrating" |

**Dimension 2: Topic Category**
| Category | Examples |
|----------|---------|
| Feature Request | "I wish it could do X", "Can you add Y?" |
| Bug Report | "X is broken", "I get an error when..." |
| UX / Usability | "Hard to find", "Confusing navigation", "Too many steps" |
| Pricing / Value | "Too expensive", "Worth every penny", "Should be free" |
| Content Quality | "Loved the module on X", "Content was outdated" |
| Performance | "Slow loading", "Crashes often", "Works great on mobile" |
| Support Experience | "Got help quickly", "Never heard back" |
| Onboarding | "Easy to get started", "Didn't know where to begin" |
| Competitor Comparison | "Better/worse than X", "Switched from Y" |

**Dimension 3: Customer Segment**
- New customer (< 30 days)
- Active customer (30+ days, engaged)
- At-risk customer (declining engagement)
- Churned customer (cancelled/left)
- Power user (high engagement, advocates)
- Free tier / trial user

### Tagging Best Practices

- Apply multiple tags when feedback spans topics ("I love the content but the app is slow" = Content Quality + Performance)
- Use consistent tag names across all feedback rounds for trend tracking
- Create a feedback taxonomy document and keep it updated as new categories emerge
- Tag the source channel (survey, review, support ticket, social, interview)

---

## 2. Theme Extraction Methodology

### The Affinity Grouping Process

1. **Collect** — Gather all feedback into a single view
2. **Code** — Apply initial tags/codes to each piece of feedback
3. **Cluster** — Group similarly-coded items together
4. **Name** — Give each cluster a descriptive theme name
5. **Validate** — Check that each item in a theme truly belongs there
6. **Rank** — Order themes by frequency and impact

### Theme Naming Standards

Good theme names are:
- **Specific:** "Checkout flow has too many steps" not "UX issues"
- **Actionable:** "Users want dark mode" not "Feature feedback"
- **Customer-voiced:** Use their language, not internal jargon

### Theme Hierarchy

Organize themes in a two-level hierarchy:

```
Level 1: Category (broad)
  Level 2: Specific Theme (actionable)

Example:
Onboarding
  - Users don't know where to start after signup
  - Welcome email lacks clear next steps
  - Tutorial is too long, users drop off midway

Pricing
  - Monthly price feels too high for solo users
  - Users want a free trial before committing
  - Annual discount not visible enough
```

### Quote Extraction

For each theme, extract 2-3 representative quotes:
- One that captures the theme most clearly
- One from a high-value or power-user customer (if available)
- One that adds nuance or a different angle

Format quotes with source attribution:
```
"I signed up but had no idea what to do next. The dashboard was empty."
— Survey respondent, new customer, 3 days after signup
```

---

## 3. Frequency Counting and Trend Analysis

### Counting Methodology

| Metric | How to Calculate | Why It Matters |
|--------|-----------------|----------------|
| Absolute frequency | Count of mentions per theme | Raw volume — what comes up most |
| Relative frequency | Theme mentions / total feedback items | Proportional importance |
| Trend direction | Compare to previous period | Is this getting better or worse? |
| Segment frequency | Theme mentions per customer segment | Who cares about this most? |

### Frequency Table Template

| Theme | Count | % of Total | Trend vs. Last Period | Top Segment |
|-------|-------|-----------|----------------------|-------------|
| Checkout too complex | 47 | 23% | UP (+8%) | New customers |
| Want dark mode | 31 | 15% | STABLE | Power users |
| Content outdated | 28 | 14% | UP (+5%) | Active customers |
| Pricing too high | 22 | 11% | DOWN (-3%) | Free tier users |
| App crashes on mobile | 19 | 9% | NEW | All segments |

### Trend Signals

- **Emerging theme:** New topic not seen in previous periods — investigate immediately
- **Growing theme:** Frequency increasing period-over-period — address before it escalates
- **Stable theme:** Consistent frequency — important but not urgent (unless it is a persistent pain point)
- **Declining theme:** Frequency decreasing — previous fix working, or customers giving up

---

## 4. Insight Prioritization Framework

### The Impact-Effort Matrix

Prioritize insights using a 2x2 matrix:

```
                    HIGH IMPACT
                        |
        QUICK WINS      |     BIG BETS
       (Do first)       |   (Plan carefully)
                        |
  LOW EFFORT -----------+------------ HIGH EFFORT
                        |
       FILL-INS         |     AVOID
    (Do if capacity)    |   (Not worth it)
                        |
                    LOW IMPACT
```

### Prioritization Scoring

Score each theme on four dimensions (1-5 scale):

| Dimension | Weight | Question |
|-----------|--------|----------|
| Frequency | 25% | How many customers mention this? |
| Severity | 25% | How much does this hurt the experience? |
| Business Impact | 30% | Does this affect revenue, retention, or growth? |
| Feasibility | 20% | Can we realistically address this? |

**Priority Score = (Frequency x 0.25) + (Severity x 0.25) + (Business Impact x 0.30) + (Feasibility x 0.20)**

### Prioritize by Impact, Not Volume

A critical insight from research: a theme mentioned by 5% of customers might cost more NPS points than one mentioned by 25%. Consider:

- **Revenue impact:** Does this theme correlate with churn or downgrades?
- **Segment value:** Are high-value customers disproportionately affected?
- **Competitive risk:** Could customers leave for a competitor that solves this?
- **Brand alignment:** Does this conflict with core brand promises?

### Actionability Classification

| Classification | Definition | Action |
|---------------|-----------|--------|
| **Act Now** | High frequency + high severity + feasible | Assign to sprint, set deadline |
| **Plan** | High impact but requires significant effort | Add to roadmap with timeline |
| **Monitor** | Moderate frequency, unclear severity | Continue tracking, revisit next cycle |
| **Acknowledge** | Low frequency, low impact, or not feasible | Respond to customers but deprioritize |
| **Investigate** | Surprising or unclear — needs more data | Run follow-up research or interviews |

---

## 5. Feedback Synthesis Report Structure

### Standard Report Format

```
FEEDBACK SYNTHESIS: [Product Name] — [Date Range]
Sources: [Survey (N=X), Reviews (N=Y), Support tickets (N=Z)]
Total feedback items analyzed: [N]

EXECUTIVE SUMMARY
[2-3 sentences: top takeaway, biggest shift, recommended action]

TOP LOVES (what to keep doing)
1. [Theme] — [frequency] mentions — [representative quote]
2. [Theme] — [frequency] mentions — [representative quote]
3. [Theme] — [frequency] mentions — [representative quote]

TOP FRUSTRATIONS (what to fix)
1. [Theme] — [frequency] mentions — [representative quote]
2. [Theme] — [frequency] mentions — [representative quote]
3. [Theme] — [frequency] mentions — [representative quote]

TOP REQUESTS (what to build)
1. [Theme] — [frequency] mentions — [representative quote]
2. [Theme] — [frequency] mentions — [representative quote]
3. [Theme] — [frequency] mentions — [representative quote]

SURPRISE INSIGHTS
[Unexpected findings that change perspective]

TREND ANALYSIS
[Comparison to previous period — what improved, what worsened, what is new]

RECOMMENDED ACTIONS
1. [Specific action] — Owner: [who] — Timeline: [when]
2. [Specific action] — Owner: [who] — Timeline: [when]
3. [Specific action] — Owner: [who] — Timeline: [when]

CRITICAL ALERTS
[Issues needing immediate attention]
```

---

## 6. Advanced Techniques

### Sentiment Scoring Scale

Go beyond positive/negative/neutral with a 5-point sentiment scale:
- **5 — Delighted:** Enthusiastic praise, would recommend
- **4 — Satisfied:** Positive but not effusive
- **3 — Neutral:** No strong feeling either way
- **2 — Frustrated:** Clear dissatisfaction, specific complaints
- **1 — Angry:** Strong negative emotion, may churn or leave public negative review

### Cross-Referencing Feedback with Behavior

When possible, correlate feedback themes with behavioral data:
- Customers who mention "onboarding confusion" — what is their activation rate?
- Customers who praise "content quality" — what is their retention rate?
- Customers who complain about "pricing" — what is their usage level?

### Feedback Loop Closure

Track whether feedback leads to action:
1. **Feedback received** — logged and categorized
2. **Insight generated** — theme identified and prioritized
3. **Action taken** — change made based on insight
4. **Result measured** — did the change improve the metric?
5. **Customer notified** — tell customers their feedback mattered

---

## Sources

- [From Feedback to Impact (Dovetail)](https://dovetail.com/customer-research/how-to-organize-customer-feedback/)
- [Customer Feedback Analysis: How To Analyze & Act (Rapidr)](https://rapidr.io/blog/customer-feedback-analysis/)
- [Customer Feedback Analysis: Step-by-Step Guide (SentiSum)](https://www.sentisum.com/customer-feedback-analysis)
- [Customer Feedback Analysis: How To & Examples (Usersnap)](https://usersnap.com/blog/customer-feedback-analysis-guide/)
- [How to Build a Customer Feedback Taxonomy (Painboard)](https://usepainboard.com/blog/how-to-build-a-customer-feedback-taxonomy)
- [Customer Feedback Analysis (Airtable)](https://www.airtable.com/articles/customer-feedback-analysis)
- [Unlocking Insights: Analyzing Customer Feedback (Help Scout)](https://www.helpscout.com/blog/customer-feedback-analysis/)
