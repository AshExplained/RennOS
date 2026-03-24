# Sentiment Report Best Practices Reference

> Last updated: 2026-03-24
> Purpose: Reference material for the sentiment-report skill — sentiment analysis methodology, scoring scales, trend identification, and reporting best practices.

---

## 1. Sentiment Analysis Methodology

### 1.1 The 4-Step Sentiment Analysis Process

1. **Data Collection** — Gather mentions from social media platforms, online reviews, forums, blogs, and news sites. Cover all relevant channels where the brand is discussed.

2. **Language Analysis** — AI and NLP models examine context, phrasing, emojis, tone, and intent. This goes beyond simple keyword matching to understand meaning.

3. **Sentiment Classification** — Each mention is labeled by sentiment (positive, negative, neutral) and scored for intensity. Multiple classification methods can be applied (see Section 2).

4. **Insight Generation** — Raw sentiment data is transformed into actionable insights: what happened, why it matters, what to do about it.

**Source:** Sprout Social, "Social Media Sentiment Analysis: Benefits and Guide for 2026"

### 1.2 Four Types of Sentiment Analysis

| Type | What It Measures | When to Use |
|------|-----------------|-------------|
| **Fine-Grained** | 5-point scale (very positive to very negative) | When nuance matters — understanding intensity, not just direction |
| **Emotion Detection** | Specific emotions (happiness, anger, sadness, frustration, excitement) | When you need to understand *why* people feel a certain way |
| **Aspect-Based** | Sentiment toward specific features, topics, or attributes | When analyzing product feedback or feature-specific reactions |
| **Intent Analysis** | Purpose behind the mention (purchase, complaint, recommendation, question) | When routing mentions for response or understanding conversion signals |

### 1.3 Hybrid Analysis Approach

The most accurate sentiment analysis combines:
- **Lexicon-based methods:** Matching known positive/negative words and phrases
- **Machine learning models:** Understanding context, sarcasm, and nuance
- **Rule-based systems:** Catching domain-specific language and industry jargon
- **Human validation:** Spot-checking automated results against manual review

**Source:** Hootsuite, "12 Social Media Sentiment Analysis Tools for 2026"; Sprinklr, "Social Media Sentiment Analysis for Enterprises"

---

## 2. Sentiment Scoring Scales

### 2.1 Common Scoring Systems

**System 1 — Bipolar Scale (-1 to +1):**
| Score Range | Sentiment | Description |
|-------------|-----------|-------------|
| +0.6 to +1.0 | Very Positive | Strong praise, enthusiasm, recommendation |
| +0.2 to +0.5 | Positive | Favorable, satisfied, appreciative |
| -0.1 to +0.1 | Neutral | Factual, no emotional charge |
| -0.5 to -0.2 | Negative | Disappointed, frustrated, complaining |
| -1.0 to -0.6 | Very Negative | Hostile, outraged, actively discouraging others |

**System 2 — Percentage Scale (0-100):**
| Score Range | Sentiment | Action Level |
|-------------|-----------|-------------|
| 80-100% | Excellent | Maintain strategy, amplify what works |
| 60-79% | Good | Monitor trends, optimize messaging |
| 40-59% | Neutral/Mixed | Investigate negative drivers, look for patterns |
| 20-39% | Concerning | Immediate response needed, root cause analysis |
| 0-19% | Crisis | Emergency protocol, leadership involved |

**System 3 — Net Sentiment Score:**
Calculated as: (Positive mentions - Negative mentions) / Total mentions x 100
- Range: -100 to +100
- Above +50: Strong positive sentiment
- 0 to +50: Mixed-positive
- Below 0: Net negative — requires intervention

### 2.2 Calculating the Sentiment Score

**Method 1 — Positive Percentage:**
(Positive mentions / Total mentions) x 100
Example: 250 positive out of 1,000 total = 25% sentiment score

**Method 2 — Weighted Score:**
Assign weights based on reach/influence:
- High-influence mention (10K+ followers): Weight 3x
- Medium-influence mention (1K-10K): Weight 2x
- Low-influence mention (<1K): Weight 1x

**Method 3 — Net Promoter-Style Score:**
(% Very Positive + % Positive) - (% Negative + % Very Negative)
- Ignores neutrals to focus on the polarized opinions

**Source:** Sprout Social, "How to Calculate a Sentiment Score for Your Brand"; Khoros, "How to Perform Social Media Sentiment Analysis"

---

## 3. Trend Identification

### 3.1 Trend Analysis Framework

Track sentiment across three time horizons:

| Horizon | Frequency | Purpose |
|---------|-----------|---------|
| **Daily** | Check daily during campaigns or crises | Spot sudden spikes or drops |
| **Weekly** | Standard reporting cadence | Identify emerging patterns |
| **Monthly/Quarterly** | Strategic review | Confirm long-term trajectory |

### 3.2 Key Trend Signals

**Positive Trend Indicators:**
- Sentiment score consistently rising over 4+ weeks
- Increasing volume of positive mentions without paid amplification
- Growing share of "very positive" mentions vs. just "positive"
- Positive sentiment expanding to new platforms/audiences
- User-generated content and organic advocacy increasing

**Negative Trend Indicators:**
- Sentiment score declining for 2+ consecutive weeks
- Spike in negative mentions correlated with a specific event or change
- Negative sentiment spreading from one platform to multiple
- Increase in "very negative" intensity (not just volume)
- Rising negative mentions from high-influence accounts

**Anomaly Indicators (Investigate Immediately):**
- 30%+ engagement rate change vs. recent average
- Negative sentiment spike above 20% of total mentions
- Sudden shift in sentiment without an obvious external cause
- Unusual volume increase from a specific platform or demographic

### 3.3 Sentiment Driver Analysis

For each reporting period, identify the top 3 drivers in each direction:

**What's driving positive sentiment?**
- Specific content pieces that resonated
- Product features or updates that received praise
- Customer interactions that were shared positively
- External events or trends that benefited the brand

**What's driving negative sentiment?**
- Product issues, bugs, or outages
- Customer service gaps
- Pricing or policy changes
- Competitor actions or unfavorable comparisons
- External controversies or associations

**Source:** Sprout Social (2026); Hootsuite (2026); InfluenceFlow, "Content Performance Analytics" (2026)

---

## 4. Reporting Best Practices

### 4.1 Standard Sentiment Report Structure

```
# Sentiment Report — [Period]

## Executive Summary
- One-line sentiment status: [Improving / Stable / Declining]
- Net sentiment score: [X] (vs. [Y] previous period)
- Key driver: [Primary factor influencing sentiment]

## Sentiment Breakdown
| Metric | This Period | Previous Period | Change |
|--------|------------|-----------------|--------|
| Total mentions | X | Y | +/-% |
| Positive | X% | Y% | +/-pp |
| Neutral | X% | Y% | +/-pp |
| Negative | X% | Y% | +/-pp |
| Net sentiment score | X | Y | +/-pts |

## Sentiment by Platform
[Table: Platform | Volume | Sentiment Score | Trend]

## Top Positive Drivers
1. [Driver] — [Evidence / examples]
2. [Driver] — [Evidence / examples]
3. [Driver] — [Evidence / examples]

## Top Negative Drivers
1. [Driver] — [Evidence / examples]
2. [Driver] — [Evidence / examples]
3. [Driver] — [Evidence / examples]

## Trend Analysis
[Visual sentiment trend over time]
[Week-over-week or month-over-month comparison]

## Recommendations
1. [Action to amplify positive sentiment]
2. [Action to address negative sentiment]
3. [Strategic opportunity identified]
```

### 4.2 Visualization Best Practices

- Use visual representations of sentiment trends — line charts showing score over time
- Color-code sentiment: green (positive), gray (neutral), red (negative)
- Show distribution (pie/donut chart) alongside trends (line chart)
- Include volume alongside sentiment — a high score on low volume means less than a moderate score on high volume
- Always show the comparison period for context

### 4.3 SMART Goal Setting for Sentiment

Set sentiment goals that are:
- **Specific:** "Increase net sentiment score from 42 to 55"
- **Measurable:** Track with consistent methodology each period
- **Achievable:** Based on historical improvement rates
- **Relevant:** Connected to brand strategy and business goals
- **Time-bound:** "Within Q2 2026"

### 4.4 Report Cadence Recommendations

| Report Type | Frequency | Audience | Depth |
|-------------|-----------|----------|-------|
| Real-time dashboard | Continuous | Social team | Metrics only |
| Weekly snapshot | Every Monday | Marketing team | Summary + key mentions |
| Monthly deep-dive | End of month | Leadership | Full analysis + recommendations |
| Quarterly strategic | End of quarter | Executive team | Trends, strategy alignment, competitive context |
| Crisis report | As needed | Leadership + PR | Immediate, focused, action-oriented |

**Source:** Sprout Social (2026); Getthematic, "Social Media Sentiment Analysis: Simple Guide"; AWS, "What is Sentiment Analysis?"

---

## 5. Platform-Specific Considerations

### 5.1 Platform Sentiment Nuances

| Platform | Tone Norm | Watch For |
|----------|-----------|-----------|
| Twitter/X | Casual, fast, often sarcastic | Sarcasm misclassification, thread context |
| LinkedIn | Professional, measured | Lower volume but higher influence per mention |
| Instagram | Visual-first, emotional | Comment sentiment vs. post engagement disconnect |
| Reddit | Candid, often critical | Subreddit culture variations, upvote/downvote context |
| YouTube | Mixed, comment quality varies | Comments may not reflect view sentiment |
| TikTok | Trend-driven, Gen-Z coded | Slang, irony, and meme references |
| Review sites | Structured, decision-stage | Star ratings provide built-in scoring |

### 5.2 Cross-Platform Aggregation

When combining sentiment across platforms:
- Weight by platform relevance to your audience (not just volume)
- Account for different baseline sentiment norms per platform
- Flag platform-specific anomalies separately from overall trends
- Reddit and Twitter tend to skew more negative than LinkedIn or Instagram

---

## 6. Common Pitfalls

1. **Treating all mentions equally** — A mention from a journalist with 500K followers matters more than one from an account with 12 followers. Weight by influence.
2. **Ignoring context** — "This is sick" can be very positive (slang) or very negative (literal). Context matters.
3. **Over-indexing on volume** — 100 mentions at 80% positive is better than 1,000 mentions at 51% positive, depending on reach.
4. **Comparing across platforms** — LinkedIn sentiment norms are different from Reddit. Compare within platforms, not across.
5. **Reporting without recommendations** — A sentiment report that only shows numbers without saying what to do about them is not useful.
6. **Ignoring neutral mentions** — A shift from positive to neutral is still a signal worth investigating, even if nothing is "negative."
7. **Single-point-in-time analysis** — Trends matter more than snapshots. Always show the trajectory.

**Source:** Sprout Social (2026); Rival IQ, "Social Media Sentiment Analysis"; Hex, "Social Media Sentiment Analysis"
