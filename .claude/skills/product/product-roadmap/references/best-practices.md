# Product Roadmap Prioritization Frameworks — Best Practices

> Reference guide for the product-roadmap skill. Use these frameworks to make
> data-driven, defensible prioritization decisions when building or updating
> the product roadmap.

---

## Table of Contents

1. [RICE Scoring Model](#1-rice-scoring-model)
2. [ICE Scoring Model](#2-ice-scoring-model)
3. [MoSCoW Prioritization](#3-moscow-prioritization)
4. [Kano Model](#4-kano-model)
5. [Now / Next / Later Roadmap](#5-now--next--later-roadmap)
6. [Framework Selection Guide](#6-framework-selection-guide)
7. [Combining Frameworks](#7-combining-frameworks)
8. [Anti-Patterns to Avoid](#8-anti-patterns-to-avoid)
9. [Sources](#9-sources)

---

## 1. RICE Scoring Model

**Origin:** Developed by Intercom to improve internal decision-making for
product roadmaps.

**Best for:** Mid-to-large product teams that need a rigorous, quantitative
scoring model to compare many competing initiatives on a common scale.

### The Four Factors

| Factor | What It Measures | How to Estimate |
|--------|-----------------|-----------------|
| **Reach** | Number of users/customers affected within a defined time period | Count of people or events per quarter (e.g., "5,000 users/quarter") |
| **Impact** | Magnitude of effect on each person reached | Score on a scale: 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal |
| **Confidence** | How certain you are about Reach, Impact, and Effort estimates | Percentage: 100% = high certainty, 80% = reasonable, 50% = uncertain |
| **Effort** | Total resources required to deliver | Person-months (e.g., "2 person-months" = 1 person for 2 months or 2 people for 1 month) |

### Formula

```
RICE Score = (Reach x Impact x Confidence) / Effort
```

Higher scores indicate higher priority. Think of it as a cost-benefit ratio:
Reach, Impact, and Confidence represent the benefit side; Effort represents the
cost side.

### Example

| Initiative | Reach | Impact | Confidence | Effort | RICE Score |
|------------|-------|--------|------------|--------|------------|
| Feature A  | 5000  | 2      | 80%        | 4      | 2,000      |
| Feature B  | 800   | 3      | 100%       | 2      | 1,200      |
| Feature C  | 10000 | 0.5    | 50%        | 6      | 417        |

Feature A wins despite Feature C having the highest reach, because C has low
confidence and high effort.

### When to Use RICE

- Comparing 10+ initiatives that need objective ranking
- When stakeholders disagree and you need a defensible, numbers-based argument
- SaaS and digital products where user reach is measurable
- Quarterly planning and roadmap reviews

### Pitfalls

- Garbage in, garbage out: RICE is only as good as your estimates
- Impact scores are subjective unless you tie them to concrete metrics
- Can feel over-engineered for small teams with fewer than 5 initiatives

---

## 2. ICE Scoring Model

**Origin:** Created by Sean Ellis (coined the term "Growth Hacking"; early
growth at Dropbox and Eventbrite).

**Best for:** Fast-moving teams, growth experiments, and situations where speed
of decision matters more than precision.

### The Three Factors

| Factor | What It Measures | Scale |
|--------|-----------------|-------|
| **Impact** | How much this idea will move the key metric you are optimizing | 1-10 |
| **Confidence** | How sure you are about your Impact and Ease estimates | 1-10 |
| **Ease** | How easy it is to implement (inverse of effort) | 1-10 |

### Formula

```
ICE Score = Impact x Confidence x Ease
```

### ICE vs. RICE — Key Differences

| Dimension | RICE | ICE |
|-----------|------|-----|
| Factors | 4 (Reach, Impact, Confidence, Effort) | 3 (Impact, Confidence, Ease) |
| Reach | Explicit, quantified | Folded into Impact |
| Effort direction | Higher = more costly (denominator) | Inverted as "Ease" — higher = easier (multiplier) |
| Precision | Higher — uses real user counts | Lower — all 1-10 scales |
| Speed | Slower — requires data gathering | Faster — quick gut + data hybrid |
| Best context | Roadmap planning | Growth experiments, rapid iteration |

### When to Use ICE

- Growth experiments and A/B test prioritization
- Small teams that need a quick scoring pass
- Early-stage products with limited usage data (where RICE's "Reach" is hard to estimate)
- Hackathons, sprint planning, or brainstorm triage

### Pitfalls

- Very subjective: two people can score the same item very differently
- No explicit "Reach" factor can hide scale differences between initiatives
- Works best when one person or a small, aligned group does the scoring

---

## 3. MoSCoW Prioritization

**Origin:** Developed by Dai Clegg in 1994 for Rapid Application Development
(RAD). Widely adopted in DSDM, Scrum, and agile environments.

**Best for:** Scope negotiation within a fixed timebox — deciding what goes into
a release, sprint, or MVP.

### The Four Categories

#### Must Have (M)

- **Definition:** Non-negotiable requirements. If any Must Have is missing, the
  delivery is a failure.
- **Guideline:** Should represent no more than ~60% of total effort to leave
  room for Should/Could items.
- **Test question:** "Will the product/release be unusable or unsellable without
  this?"

#### Should Have (S)

- **Definition:** Important but not critical for this timebox. Often as valuable
  as Must Haves but with workarounds available or less time pressure.
- **Guideline:** Typically ~20% of total effort.
- **Test question:** "Is this painful to leave out, but survivable?"

#### Could Have (C)

- **Definition:** Desirable nice-to-haves. Improve user experience or polish but
  are the first to be dropped when time runs short.
- **Guideline:** Typically ~20% of total effort. Acts as a buffer — trim these
  first if the timebox is at risk.
- **Test question:** "Would users notice if this were missing? Would they
  forgive it?"

#### Won't Have (W)

- **Definition:** Explicitly out of scope for this timebox. Not dropped silently
  — consciously parked. May be reconsidered for future timeboxes.
- **Test question:** "Can this wait until next release without meaningful
  negative impact?"

### MoSCoW in Practice

```
Timebox: Q2 2026 Release

MUST HAVE
- [ ] User authentication revamp (security compliance deadline)
- [ ] Payment gateway migration (contract expiry)

SHOULD HAVE
- [ ] Dashboard redesign (validated via user research)
- [ ] Notification preferences (top support ticket driver)

COULD HAVE
- [ ] Dark mode
- [ ] CSV export for reports

WON'T HAVE (this release)
- [ ] Mobile app v2
- [ ] AI-powered recommendations
```

### When to Use MoSCoW

- Sprint or release planning with a fixed timebox
- MVP scoping — deciding what goes into v1
- Stakeholder alignment — getting everyone to agree on what is truly essential
- Vendor/contract negotiations with scope constraints

### Pitfalls

- Stakeholders tend to label everything "Must Have" — requires facilitation
- No built-in ranking within categories (all Must Haves are equal)
- Binary categorization can oversimplify — combine with a scoring model for
  intra-category ranking

---

## 4. Kano Model

**Origin:** Developed by Professor Noriaki Kano in the 1980s. Rooted in quality
management and customer satisfaction theory.

**Best for:** Understanding how features affect customer satisfaction and
identifying which features create delight vs. which merely prevent
dissatisfaction.

### Feature Categories

#### Basic / Must-Be Features

- **Customer expectation:** Taken for granted. Customers don't ask for them
  because they assume they exist.
- **Satisfaction curve:** Absent = high dissatisfaction. Present = neutral (no
  extra satisfaction). More investment beyond baseline yields diminishing returns.
- **Examples:** Login works, pages load in reasonable time, data doesn't get
  lost, basic security.
- **Implication:** Get these right first. They are table stakes, not
  differentiators.

#### Performance / One-Dimensional Features

- **Customer expectation:** Explicitly requested and consciously evaluated.
- **Satisfaction curve:** Linear — the better you execute, the more satisfied
  customers become. The worse, the less satisfied.
- **Examples:** Speed, storage space, number of integrations, report detail.
- **Implication:** Compete on execution quality. These are your benchmark
  features against competitors.

#### Excitement / Attractive Features

- **Customer expectation:** Not expected — customers don't know they want them.
- **Satisfaction curve:** Absent = no dissatisfaction. Present = disproportionate
  delight. Even small investments yield high satisfaction.
- **Examples:** Proactive suggestions, surprisingly beautiful UX, unexpected
  integrations, "magic" moments.
- **Implication:** These are your differentiators and competitive moat. They
  generate word-of-mouth.

#### Indifferent Features

- Features that customers neither care about nor notice.
- **Implication:** Stop investing here. These are waste.

#### Reverse Features

- Features that a segment of customers actively dislikes.
- **Implication:** Segment your audience. One user's delight is another's
  annoyance.

### The Kano Decay Effect

Feature categories shift over time:

```
Excitement feature (Year 1)
  -> Performance feature (Year 2-3)
    -> Basic/Must-Be feature (Year 4+)
```

What delights customers today becomes an expectation tomorrow. Example:
smartphone fingerprint unlock was an excitement feature in 2013, a performance
feature by 2016, and a basic expectation by 2020.

### Running a Kano Analysis

1. **List candidate features** from your backlog
2. **Create Kano questionnaire** — for each feature, ask two questions:
   - Functional: "If the product HAD this feature, how would you feel?"
   - Dysfunctional: "If the product DID NOT have this feature, how would you feel?"
   - Answer scale: Like it / Expect it / Neutral / Can live with it / Dislike it
3. **Map responses** to the Kano evaluation table to categorize each feature
4. **Plot on the Kano diagram** — x-axis = implementation level, y-axis =
   satisfaction
5. **Prioritize:** Must-Be first (table stakes) -> Performance (compete) ->
   Excitement (differentiate)

### When to Use Kano

- Planning a new product or major redesign
- Understanding customer needs beyond feature requests
- Deciding where to invest for competitive differentiation
- Balancing "customer asks" with "customer delights"

### Pitfalls

- Requires actual customer data (surveys, interviews) — cannot be done purely
  internally
- Time-consuming to execute properly
- Categories shift over time and across segments — revisit regularly
- Does not account for business viability or effort

---

## 5. Now / Next / Later Roadmap

**Origin:** Developed by Janna Bastow (co-founder of ProdPad, co-founder of
Mind the Product).

**Best for:** Communicating roadmap intent to stakeholders without committing to
specific dates. Replaces Gantt-chart-style roadmaps with a flexibility-first
approach.

### The Three Horizons

| Horizon | Timeframe | Commitment Level | Detail Level |
|---------|-----------|------------------|--------------|
| **Now** | Current sprint / next 30 days | High — actively being built | Detailed: specific features, assigned teams, clear scope |
| **Next** | 30-90 days | Medium — validated and queued | Moderate: defined problems, validated solutions, rough scope |
| **Later** | 90+ days | Low — directional intent | Light: themes, opportunity areas, hypotheses to validate |

### Optional Fourth Category: Icebox / Trash

Some teams add a fourth column for ideas that have been consciously parked or
rejected. This prevents "zombie ideas" from resurfacing and forces explicit
decision-making about what NOT to do.

### Key Principles

1. **Only "Now" has dates.** Next and Later represent priority order, not
   delivery commitments.
2. **Items flow left.** Ideas start in Later, get validated into Next, and
   graduate to Now when ready.
3. **Right-side items are cheap to change.** Pivoting a "Later" item costs
   nothing. Pivoting a "Now" item is expensive.
4. **Tie to outcomes, not outputs.** Each column should map to strategic
   objectives or OKRs, not just feature names.

### Now / Next / Later in Practice

```
NOW (Sprint 14 — March 2026)
- Onboarding flow redesign [Dept: Product + Design]
- API rate limiting [Dept: Engineering]
- Q1 content series launch [Dept: Content]

NEXT (April-May 2026)
- Self-serve analytics dashboard [validated via user interviews]
- Pricing tier restructure [pending financial modeling]
- Partner integration program [3 partners in pipeline]

LATER (Q3 2026+)
- Mobile app v2
- AI-assisted content generation
- International expansion (EMEA)

ICEBOX
- Blockchain-based verification (parked — no market demand)
- Gamification features (revisit after engagement baseline)
```

### When to Use Now / Next / Later

- Communicating roadmap to stakeholders who fixate on dates
- Agile teams that resist committing to long-term Gantt charts
- Early-stage products where the future is highly uncertain
- Aligning product work with OKRs or strategic themes

### Pitfalls

- "Later" can become a graveyard if not actively curated
- Stakeholders may still pressure you for dates on Next/Later items — hold the
  line
- Without a scoring model (RICE, ICE) within each column, ranking items inside
  a horizon can be arbitrary

---

## 6. Framework Selection Guide

No single framework is universally best. Choose based on your context:

| Situation | Recommended Framework | Why |
|-----------|----------------------|-----|
| **Quarterly roadmap planning with 10+ initiatives** | RICE | Quantitative ranking across many options |
| **Growth experiments and rapid iteration** | ICE | Fast scoring, designed for experimentation |
| **Sprint/release scoping with fixed timebox** | MoSCoW | Clear in/out decisions for a delivery window |
| **New product or major redesign** | Kano | Understand which features satisfy vs. delight |
| **Stakeholder communication** | Now/Next/Later | Flexible, date-free roadmap format |
| **MVP definition** | MoSCoW + Kano | MoSCoW for scope, Kano for feature-type balance |
| **Mature product with lots of data** | RICE + Kano | RICE for ranking, Kano for strategic balance |
| **Small team, few options** | ICE or simple Value/Effort | Don't over-engineer the process |

### Decision Tree

```
How many initiatives are you comparing?
  |
  |-- < 5 items --------> ICE (fast) or Value/Effort matrix
  |
  |-- 5-15 items -------> Do you have quantitative reach data?
  |                         |-- Yes -> RICE
  |                         |-- No  -> ICE or MoSCoW
  |
  |-- 15+ items --------> RICE (must have structured scoring at scale)

Are you scoping a fixed timebox (sprint/release)?
  |-- Yes -> MoSCoW (for in/out decisions)
  |-- No  -> Now/Next/Later (for ongoing roadmap)

Do you need to understand customer satisfaction drivers?
  |-- Yes -> Kano analysis first, then RICE/ICE for ranking
  |-- No  -> Skip Kano
```

---

## 7. Combining Frameworks

The most effective product teams layer frameworks rather than choosing just one.

### Recommended Combinations

**Kano + RICE (Strategic Roadmap)**
1. Run Kano analysis to categorize features (Basic / Performance / Excitement)
2. Ensure all Basic features are in the roadmap (non-negotiable)
3. Use RICE to rank Performance and Excitement features against each other
4. Result: a roadmap that covers table stakes AND is optimized for impact

**MoSCoW + Now/Next/Later (Release Planning)**
1. Use Now/Next/Later as the roadmap structure
2. Within each horizon, apply MoSCoW to scope specific releases
3. Result: flexible long-term view with disciplined short-term scoping

**ICE + Kano (Growth Teams)**
1. Use Kano to identify which Excitement features to experiment with
2. Use ICE to rank experiments by expected impact and ease
3. Result: experiments focused on delight, ranked by speed to learn

### Anti-Pattern: Framework Overload

Do not apply all five frameworks to every decision. Pick one primary framework
and optionally layer one more. Three or more frameworks on the same decision set
creates analysis paralysis.

---

## 8. Anti-Patterns to Avoid

| Anti-Pattern | What Happens | Fix |
|-------------|-------------|-----|
| **HiPPO prioritization** | Highest-Paid Person's Opinion overrides data | Use RICE/ICE scores to make debates evidence-based |
| **Everything is P0** | No real prioritization; team burns out | MoSCoW forces explicit trade-offs |
| **Feature factory** | Shipping features without validating impact | Kano analysis + outcome-based roadmap |
| **Date-driven roadmap** | False precision creates broken promises | Switch to Now/Next/Later |
| **Sunk cost bias** | Continuing failed initiatives because of past investment | Re-score with RICE/ICE quarterly; kill low scorers |
| **Recency bias** | Latest customer complaint jumps to top of backlog | Aggregate feedback into themes; score themes, not individual requests |
| **Scope creep in Must Haves** | MoSCoW Must Have grows to 90% of effort | Enforce the 60% rule for Must Haves |
| **Stale roadmap** | Roadmap created once, never updated | Schedule monthly roadmap reviews with fresh scoring |

---

## 9. Sources

1. Intercom — "RICE: Simple Prioritization for Product Managers"
   https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/

2. ProductPlan — "RICE Scoring Model"
   https://www.productplan.com/glossary/rice-scoring-model/

3. ProductPlan — "MoSCoW Prioritization"
   https://www.productplan.com/glossary/moscow-prioritization/

4. Agile Business Consortium — "MoSCoW Prioritisation (DSDM)"
   https://www.agilebusiness.org/dsdm-project-framework/moscow-prioritisation.html

5. ProductPlan — "Kano Model"
   https://www.productplan.com/glossary/kano-model/

6. ASQ — "What is the Kano Model?"
   https://asq.org/quality-resources/kano-model

7. ProdPad — "Why I Invented the Now-Next-Later Roadmap" (Janna Bastow)
   https://www.prodpad.com/blog/invented-now-next-later-roadmap/

8. Product School — "Now-Next-Later Roadmap"
   https://productschool.com/blog/product-strategy/now-next-later-roadmap

9. ProductPlan — "ICE Scoring Model"
   https://www.productplan.com/glossary/ice-scoring-model/

10. Itamar Gilad — "Product Discovery With ICE and The Confidence Meter"
    https://itamargilad.com/the-tool-that-will-help-you-choose-better-product-ideas/

11. monday.com — "Product Prioritization Frameworks: The Complete Guide for 2026"
    https://monday.com/blog/rnd/product-prioritization-frameworks/

12. Aha! — "Product Prioritization Frameworks: 12 Common Models"
    https://www.aha.io/roadmapping/guide/release-management/prioritization-framework
