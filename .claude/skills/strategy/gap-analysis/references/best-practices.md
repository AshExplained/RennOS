# Gap Analysis Best Practices Reference

> Compiled from industry frameworks and methodologies (2026).
> For use by the gap-analysis skill when evaluating competitive gaps and opportunities.

---

## 1. Opportunity Scoring Rubric

Use this rubric to score every gap identified during analysis.
Each dimension is rated 1-5, then multiplied by its weight.

### Scoring Dimensions

| # | Dimension | Description | Weight |
|---|-----------|-------------|--------|
| 1 | **Opportunity Size** | How large is the underserved audience? How many people experience this gap? | 3 |
| 2 | **Brand Fit** | Does filling this gap align with the user's Brand DNA, mission, and positioning? | 3 |
| 3 | **Feasibility** | How realistic is it to fill this gap given current skills, resources, and capacity? | 2 |
| 4 | **Urgency / Timing** | Is there a time-sensitive window? Will the gap close naturally or widen? | 2 |
| 5 | **Competitive Advantage** | Would filling this gap create meaningful differentiation from competitors? | 2 |
| 6 | **Audience Demand** | Is there expressed or latent demand from the target audience for this? | 3 |
| 7 | **Strategic Alignment** | Does this gap connect to the current quarterly roadmap and strategic priorities? | 2 |
| 8 | **Effort-to-Impact Ratio** | What is the expected return relative to the effort required? | 1 |

### Rating Scale (1-5)

| Score | Label | Definition |
|-------|-------|------------|
| 5 | Exceptional | Extremely strong fit; clear, large opportunity with low barriers |
| 4 | Strong | Above-average opportunity; minor limitations |
| 3 | Moderate | Reasonable opportunity; notable trade-offs or unknowns |
| 2 | Weak | Below average; significant barriers or misalignment |
| 1 | Poor | Minimal opportunity; major misalignment or infeasibility |

### Calculating the Composite Score

```
Composite Score = SUM(rating_i * weight_i) / SUM(weight_i)
```

Maximum possible score: 5.0
Minimum possible score: 1.0

### Decision Thresholds

| Composite Score | Action |
|-----------------|--------|
| 4.0 - 5.0 | **Pursue immediately** — high-priority gap, recommend to the user |
| 3.0 - 3.9 | **Strong candidate** — include in top recommendations with caveats |
| 2.5 - 2.9 | **Monitor** — worth tracking but not a current priority |
| Below 2.5 | **Deprioritize** — low opportunity or poor fit |

> Source: Adapted from McKinley Advisors' Revenue Opportunity Evaluation Rubric
> (mckinley-advisors.com/blog/evaluating-new-revenue-opportunities) which uses a
> weight x rating methodology with a 2.5 minimum threshold for pursuit.

---

## 2. Gap Identification Methodology

### Phase 1: Define Scope and Inputs

Before identifying gaps, establish clear boundaries:

- **Focus area**: Specific domain (content, product, platform, format) or "general" broad scan
- **Current state data**: Competitive landscape, existing content/offerings, brand positioning
- **Target state data**: Audience needs, persona pain points, market trends
- **Time horizon**: Near-term (0-3 months), mid-term (3-12 months), long-term (12+ months)

### Phase 2: Four-Lens Gap Identification

Examine gaps through four distinct lenses to ensure comprehensive coverage:

#### Lens 1 — Content & Topic Gaps
- What subjects does the audience care about that competitors ignore or underserve?
- What questions go unanswered in the current landscape?
- Where do competitors provide shallow coverage that could be deepened?

#### Lens 2 — Format & Medium Gaps
- What content formats are missing (long-form, video, audio, interactive, visual)?
- Are there delivery mechanisms the audience prefers that nobody uses?
- What modalities would make existing content more accessible or engaging?

#### Lens 3 — Platform & Distribution Gaps
- Which platforms does the audience inhabit where competitors have no presence?
- Are there emerging channels where early entry would yield advantage?
- Where is distribution weak despite strong content?

#### Lens 4 — Experience & Value Gaps
- What pain points remain unaddressed across the competitive landscape?
- Where is the audience underserved in terms of depth, personalization, or community?
- What premium or differentiated experience could be offered that does not exist today?

### Phase 3: Root Cause Analysis

For each identified gap, apply the **Five Whys** technique:

1. State the gap clearly
2. Ask "Why does this gap exist?" — record the answer
3. Ask "Why?" again for the answer — repeat five times total
4. The final answer reveals the root cause, not just the symptom
5. Determine whether the root cause is structural (hard to change) or situational (opportunity window)

> Source: ClearPoint Strategy's gap analysis guide
> (clearpointstrategy.com/blog/gap-analysis-template) recommends the Five Whys
> as a core technique for understanding gap root causes.

### Phase 4: Gap Validation

Before scoring, validate each gap:

- **Evidence check**: Is there data (search volume, audience feedback, engagement metrics) supporting this gap?
- **Competitor check**: Confirm competitors genuinely underserve this area (not just less visible)
- **Audience check**: Does persona data confirm this is a real need, not an assumed one?
- **Recency check**: Is this gap current, or has it been recently addressed by a competitor?

---

## 3. Prioritization Frameworks

### Framework A: Impact-Effort Matrix

Plot validated and scored gaps on a 2x2 matrix:

```
                    HIGH IMPACT
                        |
         Quick Wins     |    Big Bets
        (Do First)      |   (Plan Carefully)
                        |
  LOW EFFORT -----------+------------ HIGH EFFORT
                        |
         Fill-Ins       |    Avoid / Defer
        (Do If Easy)    |   (Deprioritize)
                        |
                    LOW IMPACT
```

- **Quick Wins** (high impact, low effort): Pursue immediately; these build momentum
- **Big Bets** (high impact, high effort): Worth doing but need planning and resources
- **Fill-Ins** (low impact, low effort): Nice-to-have; do when capacity allows
- **Avoid / Defer** (low impact, high effort): Not worth the investment right now

> Source: Smartsheet's gap analysis guide (smartsheet.com/gap-analysis-method-examples)
> and LinkedIn's competitive gap prioritization framework both recommend
> impact-feasibility matrices for gap prioritization.

### Framework B: RICE Scoring

For more granular prioritization, apply the RICE framework to each gap:

| Factor | Definition | Scale |
|--------|-----------|-------|
| **R**each | How many people will this impact in a defined time period? | Estimated number |
| **I**mpact | How much will this move the needle per person reached? | 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal |
| **C**onfidence | How confident are you in the reach, impact, and effort estimates? | 100% = high, 80% = medium, 50% = low |
| **E**ffort | How many person-months of work is required? | Estimated number |

```
RICE Score = (Reach * Impact * Confidence) / Effort
```

Rank gaps by RICE score from highest to lowest. The top-scoring gaps represent the best combination of large audience, high impact, confident estimates, and low effort.

> Source: Blitzllama's gap analysis frameworks guide
> (blitzllama.com/blog/gap-analysis-tools-frameworks) recommends RICE scoring
> as a best practice for "prioritizing mercilessly."

### Framework C: MoSCoW Classification

After scoring, classify the top gaps:

- **Must-have**: Gaps that align directly with quarterly roadmap goals and brand positioning — these are non-negotiable priorities
- **Should-have**: High-scoring gaps that strengthen the brand but are not time-critical
- **Could-have**: Moderate-scoring gaps worth pursuing if resources allow
- **Won't-have (this cycle)**: Gaps that scored below threshold or are strategically premature

> Source: Blitzllama's frameworks guide identifies MoSCoW as an effective method
> for translating scored gaps into actionable priority tiers.

---

## 4. Supporting Frameworks for Context

These established frameworks provide additional analytical lenses when deeper
context is needed during gap analysis:

### SWOT Analysis
- **Strengths**: Internal advantages the user has for filling identified gaps
- **Weaknesses**: Internal limitations that may prevent filling certain gaps
- **Opportunities**: External conditions that make gap-filling timely
- **Threats**: External risks that could undermine gap-filling efforts

### McKinsey 7-S Model
When gaps appear to be organizational rather than content-related, examine alignment across:
Strategy, Structure, Systems, Shared Values, Skills, Style, Staff

### Kano Model for Feature/Content Gaps
Classify gap-filling opportunities by audience expectation:
- **Basic needs**: Gaps the audience expects to be filled (table stakes)
- **Performance needs**: Gaps where more = better (linear satisfaction)
- **Excitement needs**: Gaps the audience does not know they have yet (delight factors)

### PESTLE for External Gap Context
When evaluating whether a gap is structural or temporary, examine:
Political, Economic, Social, Technological, Legal, Environmental factors

> Sources: Blitzllama (blitzllama.com/blog/gap-analysis-tools-frameworks) and
> Smartsheet (smartsheet.com/gap-analysis-method-examples) both catalog these
> as standard gap analysis companion frameworks.

---

## 5. Recommended Process (End-to-End)

Putting it all together, the recommended sequence for gap analysis:

```
1. SCOPE      → Define focus area, time horizon, inputs
2. IDENTIFY   → Apply four-lens framework (content, format, platform, experience)
3. VALIDATE   → Evidence check, competitor check, audience check, recency check
4. ROOT CAUSE → Five Whys on each validated gap
5. SCORE      → Apply opportunity scoring rubric (Section 1)
6. PRIORITIZE → Impact-Effort matrix, then RICE for top candidates
7. CLASSIFY   → MoSCoW the final ranked list
8. RECOMMEND  → Present top 3-5 gaps with scores, rationale, and suggested actions
```

### Quality Checklist

Before finalizing the gap analysis output, verify:

- [ ] All four lenses were applied (not just content gaps)
- [ ] Each gap has a composite score with all 8 dimensions rated
- [ ] Root causes are identified, not just symptoms
- [ ] Validation evidence is cited for each gap
- [ ] Gaps are ranked by composite score AND positioned on impact-effort matrix
- [ ] Top 3-5 recommendations include specific, actionable next steps
- [ ] All recommendations align with Brand DNA
- [ ] Findings are compared against previous gap analyses if available

---

## Sources

1. ClearPoint Strategy — "Gap Analysis: A Simple Guide for Strategic Growth"
   https://www.clearpointstrategy.com/blog/gap-analysis-template

2. Smartsheet — "Guide to Gap Analysis with Examples"
   https://www.smartsheet.com/gap-analysis-method-examples

3. Blitzllama — "Gap Analysis Frameworks: Build Successful Products"
   https://www.blitzllama.com/blog/gap-analysis-tools-frameworks

4. McKinley Advisors — "Evaluating New and Innovative Revenue Opportunities"
   https://www.mckinley-advisors.com/blog/evaluating-new-revenue-opportunities

5. Product Frameworks — "Product Opportunity Evaluation Matrix (POEM)"
   https://www.product-frameworks.com/Poem-Framework.html

6. Jotform Blog — "7 Gap Analysis Tools in 2026"
   https://www.jotform.com/blog/gap-analysis-tools/

7. TechTarget — "What Is Gap Analysis and How Does It Work?"
   https://www.techtarget.com/searchcio/definition/gap-analysis
