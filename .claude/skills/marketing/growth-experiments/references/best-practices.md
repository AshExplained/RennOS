# Growth Experiment Design — Best Practices Reference

> Reference material for the Growth Experiments skill.
> Last updated: 2026-03-24

---

## Table of Contents

1. [ICE Scoring Framework](#1-ice-scoring-framework)
2. [RICE Scoring Framework](#2-rice-scoring-framework)
3. [ICE vs RICE — When to Use Which](#3-ice-vs-rice--when-to-use-which)
4. [Experiment Design Methodology](#4-experiment-design-methodology)
5. [Statistical Significance Basics](#5-statistical-significance-basics)
6. [Common Experiment Types for Creators](#6-common-experiment-types-for-creators)
7. [Minimum Viable Tests](#7-minimum-viable-tests)
8. [Sources](#8-sources)

---

## 1. ICE Scoring Framework

Created by Sean Ellis (who coined "growth hacking") to help teams at LogMeIn and Dropbox decide which experiments to run first.

### Components (each scored 1–10)

| Factor | Question | Scoring Guidance |
|--------|----------|-----------------|
| **Impact** | If this works, how big is the effect on our focus metric? | 10 = transformative change to core metric; 1 = barely measurable |
| **Confidence** | How much evidence do we have that this will work? | 10 = strong data/past results; 5 = informed guess; 1 = pure speculation |
| **Ease** | How quickly and cheaply can we execute this? | 10 = done in an afternoon; 5 = a few days of work; 1 = weeks of engineering |

### Calculation

```
ICE Score = (Impact + Confidence + Ease) / 3
```

Result: a score from 1.0 to 10.0. Higher = run first.

### Worked Example

| Experiment | Impact | Confidence | Ease | ICE Score |
|-----------|--------|-----------|------|-----------|
| Homepage headline rewrite | 8 | 7 | 9 | **8.0** |
| Exit-intent popup | 6 | 6 | 8 | **6.7** |
| Referral programme | 9 | 5 | 4 | **6.0** |
| Onboarding redesign | 9 | 6 | 3 | **6.0** |

The headline rewrite wins despite lower raw impact because high confidence and ease mean faster execution and more reliable results.

### ICE Best Practices

- **Define your scale first.** Before scoring, agree as a team on what 1 vs 10 means for each factor. Without calibration, scores are meaningless.
- **Score independently.** Have each person score alone before discussion to prevent anchoring bias.
- **Discuss divergent scores.** When assessments vary widely, the underlying assumptions are the real conversation.
- **Re-score periodically.** Market conditions shift; revisit scores quarterly.
- **Use for ranking, not precision.** A score of 7.3 vs 7.1 is noise. Focus on tiers (high/medium/low).

### Common ICE Pitfalls

1. **Subjectivity creep** — Without calibration data, two people can score the same idea very differently. Mitigate by establishing scoring rubrics.
2. **Missing reach context** — ICE ignores audience size. A high-impact change affecting 100 visitors differs from one affecting 100,000. Use RICE when reach varies widely.
3. **Ease ambiguity** — Teams conflate effort, time, and cost. Pick one definition and stick with it.
4. **Anchoring effects** — First scorer influences everyone else. Independent scoring before discussion fixes this.

---

## 2. RICE Scoring Framework

Developed by Sean McBride at Intercom. Extends ICE by adding a Reach component, making it more rigorous for teams with audience data.

### Components

| Factor | Definition | How to Measure |
|--------|-----------|---------------|
| **Reach** | Number of people affected in a given time period | Monthly visitors, quarterly subscribers, annual signups — pick the unit that matches your goal |
| **Impact** | Effect on each individual reached | 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal |
| **Confidence** | Certainty in your estimates | 100% = high (strong data), 80% = medium (some data), 50% = low (gut feel) |
| **Effort** | Total person-days to launch | Include all dependent teams; be honest |

### Calculation

```
RICE Score = (Reach x Impact x Confidence) / Effort
```

Higher score = higher priority.

### Worked Example

**Experiment A — SEO article targeting a 300-search/month keyword:**
- Reach: 100 people/month
- Impact: 1 (medium)
- Confidence: 80%
- Effort: 0.5 days
- **Score: (100 x 1 x 0.8) / 0.5 = 160**

**Experiment B — Onboarding flow redesign:**
- Reach: 2,000 people/month
- Impact: 2 (high)
- Confidence: 50%
- Effort: 10 days
- **Score: (2000 x 2 x 0.5) / 10 = 200**

Despite lower confidence, Experiment B scores higher because of its massive reach and high impact.

### RICE Best Practices

- Use RICE when experiments vary widely in how many people they affect.
- Be conservative with Confidence — if you only have a hunch, use 50%.
- Measure Effort in person-days, not calendar days.
- Data-rich teams get the most value from RICE because Reach and Confidence are grounded in real numbers.

---

## 3. ICE vs RICE — When to Use Which

| Situation | Use |
|-----------|-----|
| Early-stage, moving fast, limited data | **ICE** |
| Multiple experiments per week needed | **ICE** |
| Experiments affect very different audience sizes | **RICE** |
| Data-rich team with user analytics | **RICE** |
| Solo creator or small team | **ICE** |
| Cross-functional team with engineers | **RICE** |

**Rule of thumb:** Start with ICE to build the prioritization habit. Graduate to RICE when you have reliable reach and effort data.

### Other Frameworks (for awareness)

| Framework | Best For |
|-----------|----------|
| **PIE** (Potential, Importance, Ease) | Conversion rate optimization |
| **PXL** | Reducing subjectivity with binary yes/no questions |
| **HIPE** | Teams with strong historical data |
| **G.R.O.W.S.** | Full growth process (brainstorm to learn) |

---

## 4. Experiment Design Methodology

### The 6-Step Growth Experiment Process

Based on the repeatable framework used by high-velocity growth teams.

#### Step 1: Brainstorm

- Maintain a **living backlog** of all growth ideas.
- Organize ideas around your current Objectives and Key Results (OKRs).
- Track each idea through a pipeline: Brainstorm > Planning > Testing > Analyzing > Complete.
- Never lose an idea — even rejected ones may become relevant later.

#### Step 2: Hypothesize

Every experiment must have a clear, falsifiable hypothesis. Use this template:

```
HYPOTHESIS TEMPLATE:

We know that: [quantitative or qualitative data point]
We believe that: [specific change/lever] for [target audience]
Will result in: [measurable outcome with a number]
We'll know this by: testing [concept] and observing [KPI]
```

**Example:**
- We know that: 60% of visitors leave the homepage within 5 seconds
- We believe that: a benefit-driven headline for first-time visitors
- Will result in: a 15% increase in time-on-page
- We'll know this by: testing the new headline for 2 weeks and observing average session duration

**Rules for good hypotheses:**
- Must be **specific** — include a number ("increase by 15%", not "improve")
- Must be **testable** — you can actually run the experiment
- Must be **falsifiable** — you can prove it wrong
- Must be **time-bound** — specify how long the test runs

#### Step 3: Prioritize

Use ICE or RICE scoring (see sections 1-2 above) to rank your backlog. Ask:

> "What is the one thing we can do right now to drive the biggest impact on our growth curve?"

Avoid the trap of working on low-impact, high-effort experiments just because they are interesting.

#### Step 4: Test

- Execute the highest-priority experiment.
- Define your **control** (unchanged version) and **variant** (changed version) clearly.
- Document everything: what changed, what stayed the same, start date, planned end date, sample size target.
- Track your primary hypothesis metric AND secondary metrics for unexpected insights.

**Control vs Variant Rules:**
- Change only ONE variable at a time (unless running a multivariate test).
- The control must remain truly unchanged during the test period.
- Run both simultaneously, not sequentially, to avoid time-based confounders.
- Randomly assign participants to control or variant.

#### Step 5: Analyze

- Did the results support or reject your hypothesis?
- Look beyond the primary metric for unexpected effects.
- Calculate statistical significance (see section 5).
- Document the result even if it failed — failed experiments are data.
- Ask: "What did we learn that we didn't expect?"

#### Step 6: Iterate

- **Winner:** Scale the successful variant and brainstorm follow-up experiments to amplify the effect.
- **Loser:** Analyze why, adjust the hypothesis, and consider a modified retest.
- **Inconclusive:** Check if sample size was sufficient. If so, the variable may not matter — move on.
- Feed all learnings back into the brainstorm backlog.
- Meet regularly to debrief and review progress toward OKRs.

### Experiment Documentation Template

For every experiment, record:

```
EXPERIMENT CARD:

Name:           [descriptive name]
Hypothesis:     [from template above]
Owner:          [who is running this]
ICE/RICE Score: [from prioritization]
Type:           [A/B test, multivariate, pre/post, etc.]
Channel:        [where it runs]
Control:        [what stays the same]
Variant:        [what changes]
Primary Metric: [the KPI you are testing]
Secondary:      [other metrics to watch]
Sample Size:    [target number needed]
Duration:       [planned runtime]
Start Date:     [when it begins]
End Date:       [when to analyze]
Result:         [win / loss / inconclusive]
Learning:       [what you now know]
Next Step:      [scale / iterate / abandon]
```

---

## 5. Statistical Significance Basics

### Core Concepts

**Statistical significance** measures how confident you can be that a difference between control and variant is real, not random chance.

**Null hypothesis (H0):** There is no difference between control and variant. The goal of an A/B test is to gather enough evidence to reject this hypothesis.

**Alternative hypothesis (H1):** There IS a meaningful difference (usually: the variant performs better).

### Key Terms

| Term | Definition | Typical Threshold |
|------|-----------|-------------------|
| **P-value** | Probability of seeing results this extreme if there is actually no difference | < 0.05 (95% confidence) |
| **Confidence level** | 1 minus the significance level; how sure you are the result is real | 95% standard, 90% acceptable for fast tests |
| **Confidence interval** | Range of plausible effect sizes | Narrower = more precise estimate |
| **Statistical power** | Probability of detecting a real effect when one exists | 80% minimum recommended |
| **Minimum Detectable Effect (MDE)** | Smallest improvement you want to reliably detect | Set based on what would be business-meaningful |
| **Sample size** | Number of observations needed for valid results | Determined by power, MDE, and significance level |

### Error Types

| Error | Name | What Happens | Risk |
|-------|------|-------------|------|
| **Type I** | False positive | You declare a winner when there is not one | Controlled by significance level (typically 5%) |
| **Type II** | False negative | You miss a real winner | Controlled by statistical power (typically 20%) |

### How to Interpret Results

1. **P-value < 0.05:** The difference is statistically significant at 95% confidence. You can be reasonably sure the effect is real.
2. **P-value 0.05-0.10:** Suggestive but not conclusive. Consider running longer or with more traffic.
3. **P-value > 0.10:** No evidence of a difference. The change likely does not matter (or your sample was too small).

**Always check the confidence interval too.** A p-value tells you IF there is a difference; the confidence interval tells you HOW BIG the difference probably is.

### Sample Size Guidelines

Sample size depends on three trade-offs:

```
More certainty (lower p-value threshold)  -> Need MORE samples
More sensitivity (smaller MDE)            -> Need MORE samples
More power (fewer false negatives)         -> Need MORE samples
```

**Practical rules for creators:**

| Your Monthly Traffic | Realistic MDE | Approximate Test Duration |
|---------------------|---------------|--------------------------|
| 100,000+ visitors | 2-5% | 1-2 weeks |
| 10,000-100,000 | 5-10% | 2-4 weeks |
| 1,000-10,000 | 10-20% | 4-8 weeks |
| Under 1,000 | 20%+ | Use qualitative methods instead |

### Common Statistical Mistakes

1. **Peeking and stopping early.** Checking results daily and stopping when you see significance inflates your false positive rate dramatically. Set a sample size target BEFORE starting and wait.
2. **Ignoring practical significance.** A 0.1% improvement can be "statistically significant" with huge samples but worthless in practice. Always ask: "Is this effect big enough to matter?"
3. **Running too many variants.** Testing 5 variants without adjusting your significance threshold means you will get false positives. Use Bonferroni correction: divide 0.05 by the number of comparisons.
4. **Confusing "not significant" with "no effect."** A non-significant result might just mean your sample was too small. Check your statistical power.
5. **Ignoring segment effects.** An overall null result can hide a big win in one segment and a big loss in another.

### When Statistics Do Not Apply

For creators with small audiences (under 1,000 per test group), formal statistical testing is unreliable. Instead:

- Use **qualitative feedback** (polls, DMs, comments) as your signal.
- Run **pre/post comparisons** with awareness that confounders exist.
- Look for **large directional effects** (2x or more) rather than small percentage changes.
- Use **sequential testing** approaches that allow flexible stopping with adjusted calculations.

---

## 6. Common Experiment Types for Creators

### Content Experiments

| Experiment | What to Test | Metric | Difficulty |
|-----------|-------------|--------|-----------|
| **Headline/hook testing** | 2-3 headline variants for the same content | CTR, engagement rate | Low |
| **Content format** | Long-form vs short-form, video vs text, carousel vs single image | Engagement, saves, shares | Low |
| **Posting time** | Same content posted at different times/days | Reach, impressions | Low |
| **CTA variation** | Different calls-to-action at end of content | Click-through, conversion | Low |
| **Topic testing** | Different topic angles for same audience | Engagement, follower growth | Low |

### Audience Growth Experiments

| Experiment | What to Test | Metric | Difficulty |
|-----------|-------------|--------|-----------|
| **Lead magnet variants** | Different free resources as opt-in incentives | Email signup rate | Medium |
| **Collaboration/cross-promo** | Partnering with complementary creators | New followers, email subs | Medium |
| **Referral mechanics** | Incentivized sharing (give/get rewards) | Viral coefficient, new subs | Medium |
| **Platform expansion** | Repurposing content for a new platform | Cross-platform followers | Medium |
| **SEO content** | Creating search-optimized content for discovery | Organic traffic, rankings | Medium |

### Conversion Experiments

| Experiment | What to Test | Metric | Difficulty |
|-----------|-------------|--------|-----------|
| **Landing page variants** | Different layouts, copy, or social proof | Conversion rate | Medium |
| **Pricing/offer structure** | Different price points, bundles, or tiers | Revenue per visitor | High |
| **Email sequence variants** | Different nurture sequences | Open rate, click rate, conversion | Medium |
| **Checkout flow** | Reduced steps, different payment options | Cart completion rate | High |
| **Onboarding flow** | Different welcome sequences for new subscribers | Activation rate, retention | High |

### Engagement Experiments

| Experiment | What to Test | Metric | Difficulty |
|-----------|-------------|--------|-----------|
| **Community interaction** | Response style, Q&A formats, polls | Comments, DMs, replies | Low |
| **Content series vs standalone** | Series (part 1/2/3) vs individual posts | Return rate, saves | Low |
| **Personalization** | Segmented content for different audience groups | Engagement per segment | Medium |
| **Gamification** | Challenges, streaks, leaderboards | Participation rate, retention | High |

---

## 7. Minimum Viable Tests

### What Is a Minimum Viable Test (MVT)?

A Minimum Viable Test is an experiment designed at the **smallest possible scale** to validate an assumption before investing more resources. The goal is speed of learning, not perfection of execution.

### MVT Design Principles

1. **Test the riskiest assumption first.** What is the one thing that, if wrong, kills the whole idea?
2. **Use the cheapest possible method.** Before building, try a landing page, a poll, a DM, or a social post.
3. **Set clear pass/fail criteria BEFORE running.** "If we get X responses in Y days, we proceed."
4. **Time-box aggressively.** Most MVTs should run 1-7 days, not weeks.
5. **Accept imperfection.** "Good enough" data now beats perfect data in 3 months.

### MVT Templates for Creators

#### Demand Test
- **Question:** Will people want this thing?
- **Method:** Post about it and include a signup link or waitlist.
- **Pass criteria:** X signups in Y days.
- **Time:** 2-3 days.
- **Cost:** Free.

#### Price Sensitivity Test
- **Question:** Will people pay $X for this?
- **Method:** Pre-sale or "pay what you want" offer to a small segment.
- **Pass criteria:** X purchases at target price.
- **Time:** 3-5 days.
- **Cost:** Free (you deliver the thing if people buy).

#### Content Angle Test
- **Question:** Does this topic resonate?
- **Method:** Post 2-3 variations of the same core idea with different angles.
- **Pass criteria:** One variant outperforms others by 2x+ on engagement.
- **Time:** 1-3 days per variant.
- **Cost:** Free.

#### Channel Test
- **Question:** Should we invest in this platform/channel?
- **Method:** Repurpose 5 pieces of existing content for the new channel.
- **Pass criteria:** Engagement rate comparable to primary channel within 2 weeks.
- **Time:** 2 weeks.
- **Cost:** Time only.

#### Partnership Test
- **Question:** Will collaborations drive growth?
- **Method:** Do 1-2 small collaborations (guest posts, joint lives, swaps).
- **Pass criteria:** Measurable follower/subscriber lift from each collab.
- **Time:** 1-2 weeks per test.
- **Cost:** Time only.

### MVT Decision Framework

After running an MVT, you have three options:

```
PASS  -> Scale up. Invest more resources. Run a full experiment.
FAIL  -> Pivot the approach or abandon. Do not throw good effort after bad.
MIXED -> Refine the hypothesis and run a modified MVT.
```

---

## 8. Sources

1. **Growth Method** — "ICE Framework: The Original Prioritisation Framework for Marketers" and "The RICE Framework: A Prioritisation for Growth Marketing"
   - https://growthmethod.com/ice-framework/
   - https://growthmethod.com/rice-framework/

2. **Airtable Engineering Blog** — "The 6-Step Method for Repeatable Growth Experiments"
   - https://blog.airtable.com/the-6-step-method-for-repeatable-growth-experiments/

3. **Analytics Toolkit** — "Statistical Significance in A/B Testing: A Complete Guide"
   - https://blog.analytics-toolkit.com/2017/statistical-significance-ab-testing-complete-guide/

4. **Gust de Backer** — "What is Growth Hacking? (2026): Best Strategy to Grow Your Business"
   - https://gustdebacker.com/what-is-growth-hacking/

5. **Ward van Gasteren** — "ICE Framework: How (NOT) to Score/Prioritize Growth Experiments"
   - https://growwithward.com/ice-prioritization-framework/

6. **ProductPlan** — "RICE Scoring Model" and "ICE Scoring Model"
   - https://www.productplan.com/glossary/rice-scoring-model/
   - https://www.productplan.com/glossary/ice-scoring-model/
