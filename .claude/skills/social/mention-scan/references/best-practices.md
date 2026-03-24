# Mention Scan Best Practices Reference

> Last updated: 2026-03-24
> Purpose: Reference material for the mention-scan skill — categorization frameworks, urgency scoring, sentiment indicators, and response decision criteria.

---

## 1. Mention Categorization Framework

### 1.1 Three-Tier Classification

Every mention falls into one of three primary categories:

| Category | Definition | Action Required |
|----------|-----------|-----------------|
| **Opportunity** | Positive mentions to amplify, collaboration requests, PR moments, purchase intent signals | Engage, amplify, or route to appropriate team |
| **Threat** | Negative sentiment, complaints, reputation risks, unauthorized IP use, crisis signals | Flag urgently, route to response team |
| **Neutral** | Informational mentions, casual references, tool lists, no strong sentiment | Log for tracking, no immediate action |

### 1.2 Topic-Based Sub-Categories

Within each tier, classify mentions by business topic:

| Sub-Category | Examples | Routing |
|-------------|----------|---------|
| Product feedback | Reviews, feature praise/complaints | Product team |
| Customer service issues | Operational complaints, broken features | Support team |
| Competitive comparisons | "X vs Y" discussions, switching signals | Marketing / Strategy |
| Feature requests | "I wish X could do..." | Product roadmap |
| Pricing discussions | Value perception, cost comparisons | Marketing |
| Partnership opportunities | Collaboration offers, joint venture signals | Business development |
| Media coverage | Journalist mentions, publication features | PR team |
| Thought leadership | Industry conversations where brand has authority | Content team |
| Purchase intent | "Considering switching from [competitor]" | Sales |

**Key insight:** Negative sentiment about pricing requires different handling than negative sentiment about customer service. Always categorize by topic, not just sentiment.

**Source:** TrySight AI, "How to Monitor Brand Mentions: Complete 2026 Guide"

---

## 2. Urgency Scoring Methodology

### 2.1 Three-Tier Alert Structure

| Tier | Urgency Level | Response Window | Routing | Trigger Criteria |
|------|--------------|-----------------|---------|-----------------|
| **1 — Critical** | Immediate | Within 1 hour | SMS/Slack to decision-makers | PR crises, major negative spikes, high-value opportunities, viral negative content |
| **2 — Important** | Same-day | Within 4 hours | Notification to relevant team | Customer service issues, media mentions, competitive intelligence, moderate negative sentiment |
| **3 — Routine** | Standard | Daily/weekly digest | Compiled in regular reports | Informational mentions, neutral references, general brand awareness signals |

### 2.2 Urgency Scoring Criteria

Score each mention on these factors (1-5 scale each):

| Factor | Weight | Scoring Guide |
|--------|--------|---------------|
| **Sentiment intensity** | High | 1=mildly negative, 5=extremely negative/hostile |
| **Reach / influence** | High | 1=<100 followers, 3=1K-10K, 5=100K+ or journalist/influencer |
| **Virality potential** | Medium | 1=no engagement, 5=rapidly gaining shares/replies |
| **Response expectation** | Medium | 1=general comment, 5=direct @mention demanding response |
| **Business impact** | High | 1=no commercial impact, 5=direct revenue/reputation threat |
| **Time sensitivity** | Medium | 1=evergreen, 5=developing crisis or time-limited opportunity |

**Urgency calculation:**
- Sum of weighted scores >= 20: **Critical** (Tier 1)
- Sum of weighted scores 12-19: **Important** (Tier 2)
- Sum of weighted scores < 12: **Routine** (Tier 3)

### 2.3 Response Time Targets by Context

| Context | Target Response Time |
|---------|---------------------|
| Urgent negative mentions | 1 hour maximum |
| Media inquiries | Immediate acknowledgment, even if full response is pending |
| Positive high-influence mentions | Same-day engagement (thank, amplify) |
| Customer complaints | Within 4 hours |
| Forum discussions | 1-2 day investigation window before engaging |
| Routine positive mentions | Same-day or next-day acknowledgment |

**Source:** TrySight AI, "How to Monitor Brand Mentions" (2026); Sprout Social, "Social Media Sentiment Analysis" (2026)

---

## 3. Sentiment Analysis Indicators

### 3.1 Sentiment Classification

Use NLP-informed analysis to classify each mention:

| Sentiment Level | Indicators | Examples |
|----------------|------------|----------|
| **Very Positive** | Enthusiastic praise, recommendations, sharing | "Absolutely love this!", "Best tool I've ever used" |
| **Positive** | Favorable mentions, mild praise, appreciation | "Really helpful content", "Good recommendation" |
| **Neutral** | Factual references, no emotional charge | "They offer X service", tool lists, informational mentions |
| **Negative** | Complaints, frustration, disappointment | "Disappointed with the response time", "Expected more" |
| **Very Negative** | Hostility, outrage, public attacks | "Terrible experience", "Avoid at all costs", "Scam" |

### 3.2 Sentiment Indicator Words

**Positive signals:** love, amazing, best, perfect, helpful, excellent, recommend, impressive, grateful, outstanding, innovative

**Negative signals:** worst, hate, disappointed, bad, avoid, terrible, broken, frustrated, scam, misleading, overpriced

**Amplifiers (intensify sentiment):** absolutely, extremely, incredibly, completely, totally, utterly

**Diminishers (reduce sentiment):** somewhat, slightly, kind of, a bit, fairly

### 3.3 Context-Sensitive Analysis

Important calibration considerations:
- **Industry-specific language:** "Disruptive" is positive in tech, negative in healthcare
- **Sarcasm detection:** "Oh great, another outage" is negative despite positive-sounding words
- **Cultural context:** Tone indicators vary by platform (Twitter vs. LinkedIn vs. Reddit)
- **Emoji interpretation:** Can reverse or amplify text sentiment
- **Maintain 80%+ accuracy** by testing automated classifications against manual review of 50-100 sample mentions

**Source:** Sprout Social, "Social Media Sentiment Analysis" (2026); TrySight AI (2026)

---

## 4. Response Decision Criteria

### 4.1 Response Decision Matrix

| Mention Type | Respond? | How | Priority |
|-------------|----------|-----|----------|
| Direct @mention with question | Yes | Reply directly | High |
| Direct @mention with complaint | Yes | Acknowledge + resolve | Critical |
| Positive public review | Yes | Thank + amplify | Medium |
| Negative public review | Yes | Acknowledge + take offline | High |
| Casual brand mention (positive) | Optional | Like/repost if appropriate | Low |
| Casual brand mention (neutral) | No | Log only | Routine |
| Competitor comparison (favorable) | Optional | Amplify if authentic | Medium |
| Competitor comparison (unfavorable) | Rarely | Only if factually incorrect | Low |
| Media/journalist mention | Yes | Engage professionally | High |
| Influencer mention | Yes | Engage + explore collaboration | High |

### 4.2 When NOT to Respond

- Casual mentions in tool lists or generic roundups — no meaningful engagement value
- Troll accounts seeking to provoke — responding amplifies them
- Mentions in private groups where you were not invited to participate
- Old mentions (>7 days) unless they resurface with new engagement
- Negative mentions that are factually correct and already resolved

### 4.3 Routing Logic

| Signal | Route To |
|--------|----------|
| Media coverage / press mentions | PR team |
| Complaints / product issues | Customer support |
| Purchase intent / positive recommendations | Sales |
| Campaign-related engagement | Marketing |
| Feature requests / product ideas | Product team |
| Reputation threats / crisis signals | PR + Leadership |
| Unauthorized IP use | Legal |
| Partnership / collaboration opportunities | Business development |

**Source:** TrySight AI (2026); Sprinklr, "Social Mentions" (2026)

---

## 5. Monitoring Setup

### 5.1 Keyword Organization

Track 15-30 terms across 3-5 logical groupings:

1. **Brand terms:** Brand name, common misspellings, abbreviations, domain name
2. **Product terms:** Product names, feature names, service names
3. **People terms:** Founder/executive names, spokesperson names
4. **Campaign terms:** Hashtags, campaign slogans, event names
5. **Competitive terms:** Competitor brand names (for context, not stalking)

### 5.2 Channel Priority

| Priority | Channel | Monitoring Frequency |
|----------|---------|---------------------|
| 1 | Twitter/X, LinkedIn | Real-time / hourly |
| 2 | Instagram, Facebook | Multiple times daily |
| 3 | Reddit, forums | Daily |
| 4 | News / media outlets | Hourly during active campaigns, daily otherwise |
| 5 | Review platforms (G2, Capterra, etc.) | Daily |
| 6 | AI platforms (ChatGPT, Claude, Perplexity, Gemini) | Weekly AI visibility checks |
| 7 | Blogs, podcasts | Weekly |

### 5.3 AI Visibility Tracking (2026 Addition)

Monitor brand presence in LLM-generated responses:
- **AI visibility score:** Frequency and favorability of mentions across varied prompts
- **Prompt appearance rate:** Percentage of relevant queries that include your brand
- **Recommendation frequency:** How often models actively endorse vs. merely mention

**Source:** TrySight AI, "How to Monitor Brand Mentions" (2026)

---

## 6. Report Format

### 6.1 Standard Mention Scan Report Structure

```
# Mention Scan — [Date]

## Urgent / Action Required
[Critical items flagged at top]

## Summary
- Total mentions found: [N]
- Sentiment breakdown: [X]% positive, [Y]% neutral, [Z]% negative
- Trend vs. previous scan: [up/down/stable]

## Opportunities
[Positive mentions, PR moments, collaboration requests]

## Threats
[Negative sentiment, complaints, reputation risks]

## Neutral / Informational
[Brand mentions without strong sentiment]

## Recommended Actions
[Specific next steps for each flagged item]
```

---

## 7. Performance Validation

A well-functioning mention monitoring system should meet these benchmarks:

- **Categorization accuracy:** 80%+ correct classification on a random 20-mention sample
- **Alert appropriateness:** Fewer than 5 critical alerts per week during normal operations
- **Dashboard usability:** Anyone can answer "Is sentiment improving?" within 30 seconds
- **Response protocols:** Team has clear playbooks for 10+ common mention scenarios
- **Response rate:** 80%+ of mentions requiring response are handled within target windows

**Source:** TrySight AI, "How to Monitor Brand Mentions: Complete 2026 Guide"
