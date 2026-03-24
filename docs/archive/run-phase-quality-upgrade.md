## RennOS — Skill Quality Upgrade: References, Templates, Scripts & Context Injection

**One doc, one implementation.** Upgrades 98 skills from bare SKILL.md files to domain-expert playbooks with best-practices references, output templates, Python scripts, and dynamic context injection.

**Current state:** 257 skill files. Only Google's Stitch skills have supporting files. All custom skills are bare SKILL.md.

**What this changes:** Agents go from "generalist following instructions" to "domain expert applying frameworks with consistent output."

---

### CRITICAL: Research Before Writing

**Before writing ANY reference file, do web research for that domain's current best practices (2026).** Do NOT rely on training data alone. Each domain evolves — frameworks get updated, new methodologies emerge, benchmarks change.

For each skill's reference file:
1. Search web for "[domain] best practices 2026" (e.g., "brand audit best practices 2026", "SCCT crisis communication framework 2026")
2. Cross-reference 3+ authoritative sources
3. Include current industry benchmarks (not outdated numbers)
4. Note any recent methodology changes or emerging frameworks
5. Cite sources at the bottom of each reference file

This ensures agents have expert-level, CURRENT domain knowledge — not stale textbook content.

### Key Files to Read First

1. `claude-code-meta.md` — Skill file structure (template.md, references/, scripts/)
2. A few existing SKILL.md files — Understand the Inputs/Steps/Output structure to extend, not replace

### Architecture

| File type | Purpose | Format | How agent uses it |
|---|---|---|---|
| `references/best-practices.md` | Domain expertise, frameworks, rubrics | Markdown | Agent reads before executing: `Read ${CLAUDE_SKILL_DIR}/references/best-practices.md` |
| `template.md` | Output structure with placeholders | Markdown with `[FIELD]` | Agent fills in placeholders for consistent output |
| `examples/example-*.md` | Gold-standard input→output | Markdown | Agent learns what "great" looks like |
| `scripts/*.py` | Data aggregation, file management | Python 3 | Injected via `!`python3 ${CLAUDE_SKILL_DIR}/scripts/name.py`` or called by agent |

**Update each SKILL.md** to reference its new files in Step 1:
```
1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
```

---

## Phase A: Top 10 (Start Here — Highest Impact)

Build these first. They affect the most-read files and highest-stakes outputs.

### 1. `strategy/brand-dna`
*Everything downstream reads this. Quality here compounds everywhere.*

```
references/best-practices.md:
  - Brand archetype framework (12 Jungian archetypes with examples)
  - Positioning frameworks (perceptual mapping, category design, blue ocean)
  - Voice spectrum methodology (formality scale, energy scale, humor scale)
  - Messaging pillar development (how to identify and validate pillars)
  - How to write anti-examples (what the brand does NOT sound like)

template.md:
  Core Identity (who/what/why), Voice (adjectives, examples, anti-examples),
  Messaging Pillars (3-5 themes), Positioning Statement,
  Visual Identity Summary, Audience Summary

examples/example-brand-dna.md:
  One complete, fictional brand DNA showing what a filled-in template looks like
```

### 2. `pr/crisis-response`
*Highest stakes output in the system.*

```
references/best-practices.md:
  - Situational Crisis Communication Theory (SCCT)
  - Crisis typology (victim, accidental, preventable)
  - Stakeholder mapping methodology
  - Response strategies by type (deny, diminish, rebuild, bolster)
  - When silence is the right move
  - Common mistakes per crisis type
  - Timeline templates for 24-72 hour response

template.md:
  Severity assessment, reach analysis, trajectory, immediate actions,
  public response (3 variants), channel strategy, 72-hour timeline,
  monitoring plan, "Do NOT do" section, legal flag
```

### 3. `strategy/brand-audit`
*Needs scoring rubric — without it, scores are arbitrary.*

```
references/best-practices.md:
  - 8-dimension scoring rubric with what 1, 5, and 10 look like for each
  - Brand audit methodology (brand equity models, perception mapping)
  - Common gap patterns and how to identify them
  - How to gather evidence per dimension (what to look for on each platform)

template.md:
  Audit scorecard: 8 dimensions, 1-10 scale, evidence field per dimension,
  gap analysis section, recommendations section
```

### 4. `strategy/persona-builder`
*Personas feed every content and marketing agent.*

```
references/best-practices.md:
  - Jobs-to-be-Done framework (JTBD)
  - Empathy mapping methodology
  - How to extract personas from data vs interviews
  - Common persona mistakes (too generic, too many, fictional demographics)
  - Behavioral segmentation principles

template.md:
  Persona card: name, demographics, psychographics, pain points, goals,
  platforms, language patterns, content preferences, influencers, JTBD

examples/example-persona.md:
  One complete persona showing depth expected
```

### 5. `strategy/quarterly-roadmap`
*The plan everything executes on.*

```
references/best-practices.md:
  - OKR methodology (Objectives and Key Results)
  - Theme-based roadmapping
  - How to balance ambition with ADHD-friendly sustainability
  - Cross-department dependency mapping
  - Risk assessment and mitigation frameworks

template.md:
  Quarter overview, 3-4 themes, monthly breakdown (theme, campaigns,
  milestones, KPIs), cross-dept dependencies, risks, resource needs

examples/example-roadmap.md:
  One complete quarterly roadmap showing structure
```

### 6. `content/edit-review`
*Quality gate for all content.*

```
references/best-practices.md:
  - 3-pass editing checklist (structural, line, voice)
  - Common writing mistakes and fixes
  - Readability scoring (Flesch-Kincaid targets by content type)
  - Brand voice checklist (specific to ashexplained from brand DNA)
  - Editor's note format standards

template.md:
  Editor's note format: changes summary, flags,
  pass/needs-revision/reject, specific edits log
```

### 7. `legal/contract-review`
*Real money at stake.*

```
references/best-practices.md:
  - Common contract red flags by deal type
  - Missing clauses checklist (termination, IP, liability, exclusivity, payment, dispute)
  - Unfavorable terms to watch for
  - Risk rating methodology (LOW/MEDIUM/HIGH criteria)
  - Industry-standard terms by contract type

template.md:
  Review report with risk ratings per clause, summary verdict (sign/negotiate/walk)
```

### 8. `legal/compliance-audit`
*Regulatory risk.*

```
references/best-practices.md:
  - GDPR requirements summary (consent, rights, DPA, breach notification)
  - CAN-SPAM rules (unsubscribe, physical address, honest subject lines, 10-day opt-out)
  - FTC endorsement guidelines (material connection, clear disclosure, truthful claims)
  - CCPA requirements summary (disclosure, opt-out, deletion rights)
  - Platform ToS key points (Twitter, YouTube, Instagram, Medium, Reddit)
```

### 9. `analytics/kpi-dashboard`
*Most-read data file in the system.*

```
references/best-practices.md:
  - KPI definitions (each metric: what it is, formula, benchmark, data source)
  - Dashboard design principles (hierarchy, scanability, actionability)
  - Metric categories (vanity vs actionable, leading vs lagging)
  - Industry benchmarks by platform and niche (Twitter, YouTube, email, blog)

template.md:
  Dashboard sections per dept with metric slots, current/previous/change/trend format
```

### 10. `marketing/funnel-design`
*Revenue infrastructure.*

```
references/best-practices.md:
  - AIDA framework (Attention, Interest, Desire, Action)
  - Value ladder methodology
  - Common funnel architectures (tripwire, webinar, challenge, free trial)
  - Conversion rate benchmarks per funnel stage
  - Lead magnet effectiveness by type

template.md:
  Funnel stages (TOFU/MOFU/BOFU), per-stage: content, conversion metric,
  benchmark, owner. Post-purchase section.
```

---

## Phase B: Remaining Tier 1 References (28 more skills)

Build after Phase A is proven. Same format: `references/best-practices.md` with domain frameworks.

### Strategy & Research
| Skill | Reference content |
|---|---|
| `competitive-landscape` | Porter's Five Forces, perceptual mapping, SWOT, strategic group mapping, how to choose matrix axes |
| `gap-analysis` | Opportunity scoring rubric, gap identification methodology |
| `opportunity-brief` | Brief structure standards, timeliness assessment framework |
| `campaign-plan` | Campaign planning methodology, KPI selection framework |

### Content Creation
| Skill | Reference content |
|---|---|
| `voice-check` | Voice analysis methodology, formality/energy spectrum, before/after rewrite techniques |
| `hooks` | Hook psychology (curiosity gap, pattern interrupt), hook types with examples, platform-specific conventions |

### Social Media
| Skill | Reference content |
|---|---|
| `platform-audit` | Platform-specific audit dimensions, engagement benchmarks by platform/niche |
| `engagement-playbook` | Scenario-specific playbooks (viral, controversy, collaboration, launch), escalation decision trees |

### PR & Communications
| Skill | Reference content |
|---|---|
| `press-release` | AP-style conventions, inverted pyramid, quote best practices |
| `pitch-draft` | Pitch anatomy, journalist preferences, length benchmarks, follow-up etiquette |

### Digital Marketing
| Skill | Reference content |
|---|---|
| `keyword-research` | Search intent types, difficulty assessment, long-tail strategy, clustering methodology |
| `seo-audit` | Core Web Vitals, on-page SEO checklist, technical SEO checklist, E-E-A-T guidelines |
| `landing-page` | PAS/AIDA copywriting, social proof hierarchy, objection handling, CTA best practices |
| `growth-experiments` | ICE/RICE scoring, experiment design, statistical significance basics |

### Partnerships
| Skill | Reference content |
|---|---|
| `deal-structure` | Deal term glossary, common structures by type, BATNA, anchoring, concession strategy |
| `sponsorship-eval` | Evaluation scorecard rubric, red flags, pricing benchmarks, FTC requirements |
| `media-kit` | Media kit structure, metrics that matter to sponsors, tiered package design |

### Operations
| Skill | Reference content |
|---|---|
| `qa-checklist` | Quality checklists per deliverable type (blog, email, social, landing page, press release, ad, pitch) |
| `post-mortem` | Blameless methodology, 5 Whys, anti-patterns |

### Analytics
| Skill | Reference content |
|---|---|
| `campaign-roi` | ROI formulas (ROAS, CAC, LTV), attribution models, indirect return calculation |
| `benchmark` | Industry benchmarks by platform (Twitter, email, YouTube, blog, ads) |

### Legal
| Skill | Reference content |
|---|---|
| `contract-draft` | Contract section templates, plain language principles |
| `privacy-policy` | Required sections by regulation, data inventory methodology |
| `disclosure-check` | FTC rules, platform-specific placement, acceptable language |

### Finance
| Skill | Reference content |
|---|---|
| `forecast` | Forecasting methods (bottom-up, top-down, run-rate, cohort), scenario planning |
| `pricing-analysis` | Pricing frameworks (value-based, cost-plus, competitive, tiered), anchoring psychology |
| `cashflow-check` | Cashflow methodology, buffer recommendations, warning thresholds |

### Product
| Skill | Reference content |
|---|---|
| `product-roadmap` | Prioritization frameworks (RICE, ICE, MoSCoW, Kano), Now/Next/Later methodology |
| `market-validation` | Lean Canvas, Value Proposition Canvas, demand testing methods |
| `course-design` | Backward design, Bloom's Taxonomy, module structure, assessment design |

### UI/UX Design
| Skill | Reference content |
|---|---|
| `ux-audit` | Nielsen's 10 Heuristics (each with examples and severity), WCAG accessibility, cognitive load |
| `visual-identity` | Color theory, typography pairing, spacing systems, design principles methodology |
| `conversion-review` | Cialdini's 6 Principles, CRO checklist, attention hierarchy, friction identification |

### Personal Finance
| Skill | Reference content |
|---|---|
| `portfolio-review` | Asset allocation by risk profile, rebalancing rules, diversification, fee analysis |

---

## Phase C: Tier 2 — Templates Only (35 skills)

These skills produce good work but output format varies. Adding `template.md` makes output consistent.

### Templates for existing skills (20)
| Skill | Template contents |
|---|---|
| `content/blog-post` | Meta title, meta description, tags, hook, H2 sections, CTA, word count target |
| `content/newsletter` | Subject line options, preview text, personal opener, main section, resources, CTA |
| `content/video-script` | Two-column: timing \| spoken dialogue \| visual cues — per section |
| `content/carousel` | Slide #, headline, body text, visual direction, color notes — per slide |
| `social/platform-audit` | 6-dimension scorecard (1-10, evidence, recommendation per dimension) |
| `social/community-roundup` | Volume, sentiment, notable interactions, themes, health, actions |
| `social/mention-scan` | Urgent flags, opportunities, threats, neutral — per mention |
| `pr/pitch-draft` | Subject line variants, hook, story, why Ash, the ask, logistics |
| `pr/interview-prep` | Key messages (headline + evidence + soundbite), Q&A, bridges |
| `pr/media-list` | Table: name, outlet, beat, contact, reach, relevance, approach |
| `pr/outreach-tracker` | Table: journalist, outlet, angle, date, subject, status, follow-up |
| `pr/pr-calendar` | Table: date, PR moment, angle, media, deliverables, lead time |
| `marketing/email-campaign` | Campaign map: email #, purpose, subject, preview, timing, CTA |
| `marketing/ad-campaign` | Brief: objective, platforms, targeting, budget, creative, KPIs |
| `marketing/keyword-research` | Keyword cluster table: keyword, volume, difficulty, intent, priority |
| `marketing/seo-audit` | SEO checklist scorecard: element, current state, score, fix |
| `partnerships/partner-brief` | Profile: audience overlap, brand fit, reach, risk, recommendation |
| `partnerships/proposal-draft` | Proposal: intro, mutual value, deliverables, timeline, terms |
| `ops/status-report` | Per-project status table, blockers, next steps, decisions needed |
| `ops/budget-tracker` | Table: category, budgeted, actual, variance, notes |

### Templates for additional skills (15)
| Skill | Template contents |
|---|---|
| `ops/vendor-eval` | Scorecard: features, pricing, support, integration, security, verdict |
| `analytics/performance-report` | Per-channel metrics, trends, highlights, concerns |
| `analytics/audience-report` | Demographics, behavior, growth, segment analysis |
| `analytics/content-performance` | Table: piece, format, platform, engagement, reach, takeaway |
| `analytics/weekly-digest` | Fixed sections: highlights, metrics, content, social, priorities |
| `finance/revenue-dashboard` | Income streams: stream, current, previous, trend, YTD |
| `finance/rate-card` | Services: service, description, price, includes, delivery |
| `finance/invoice-draft` | Invoice: from, to, date, items, subtotal, tax, total, terms |
| `product/product-spec` | Spec: problem, solution, user stories, requirements, metrics |
| `product/launch-plan` | Launch timeline with dept assignments, pre/during/post phases |
| `product/launch-checklist` | GO/NO-GO checklist by category (product, content, marketing, PR, ops) |
| `product/beta-report` | Bugs, UX issues, feature requests, NPS, go/no-go |
| `success/feedback-report` | Themes: theme, frequency, sentiment, quotes, action |
| `success/churn-analysis` | Cohort table, leading indicators, at-risk, interventions |
| `design/wireframe` | Page sections, hierarchy, components, interaction, responsive notes |

---

## Phase D: Tier 2 References (25 skills)

These benefit from methodology references but are less critical than Phase A/B.

| Skill | Reference content |
|---|---|
| `strategy/campaign-plan` | Campaign planning methodology, KPI selection |
| `content/blog-post` | Blog structure best practices, SEO-aware writing |
| `content/newsletter` | Newsletter structure, subject line psychology, open rates |
| `content/video-script` | Script structure for spoken delivery, pacing, visual cues |
| `social/mention-scan` | Mention categorization (opportunity/threat/neutral), urgency scoring |
| `social/sentiment-report` | Sentiment analysis methodology, trend identification |
| `pr/pr-strategy` | PR strategy frameworks, media tiers, narrative building |
| `pr/interview-prep` | Interview prep methodology, message bridging, tough questions |
| `marketing/email-campaign` | Email sequence patterns, timing, drip campaigns |
| `marketing/ad-campaign` | Campaign structure, targeting methodology, budget allocation |
| `marketing/lead-magnet` | Lead magnet types ranked by conversion, effort assessment |
| `analytics/content-performance` | Content analysis dimensions, pattern identification |
| `analytics/weekly-digest` | Digest structure, metric selection for weekly vs monthly |
| `product/launch-plan` | Launch timeline best practices, cross-dept coordination |
| `product/launch-checklist` | Pre-launch methodology, GO/NO-GO criteria |
| `product/feedback-synthesis` | Feedback categorization, theme extraction, frequency counting |
| `success/churn-analysis` | Churn frameworks, cohort analysis, leading indicators |
| `success/onboarding-design` | Onboarding flow best practices, activation metrics, time-to-value |
| `success/escalation-plan` | Escalation tier design, response time standards, severity |
| `health/workout-plan` | Exercise programming (periodization, progressive overload, rest) |
| `health/meal-plan` | Nutrition frameworks (macros by goal, meal timing, guidelines) |
| `health/wellness-check` | Evidence-based wellness dimensions (stress, sleep, energy, mood, connection) |
| `tech/security-audit` | OWASP Top 10, security header checklist, dependency audit |
| `tech/site-audit` | Site audit checklist (performance, accessibility, mobile, SEO, UX) |
| `deep-research` | Research methodology (source evaluation, synthesis, report structure) |

---

## Phase E: Python Scripts (14 skills)

All in `.claude/skills/<dept>/<skill>/scripts/`. Python 3.

### Data Aggregation Scripts

| Skill | Script | Purpose |
|---|---|---|
| `social/content-calendar` | `list_available_content.py` | Scan `data/content/drafts/` + `data/social/` for files ready to schedule |
| `content/content-matrix` | `scan_content_inventory.py` | Scan content pieces, cross-reference with derivatives |
| `pr/outreach-tracker` | `outreach_stats.py` | Parse tracker table, calculate response rates |
| `analytics/kpi-dashboard` | `aggregate_metrics.py` | Scan all `data/*/` for latest metrics |
| `analytics/weekly-digest` | `compile_weekly_data.py` | Pull most recent files from each dept |
| `ops/status-report` | `project_status_scan.py` | Scan active_projects + data/ for recent changes |
| `finance/revenue-dashboard` | `revenue_summary.py` | Aggregate income by stream |
| `finance/payment-tracker` | `payment_status.py` | List outstanding/overdue invoices |
| `admin/subscription-audit` | `subscription_summary.py` | List subscriptions, total monthly spend |

### File Management Scripts

| Skill | Script | Purpose |
|---|---|---|
| `ops/master-calendar` | `merge_calendars.py` | Merge dates from all dept calendars |
| `ops/deadline-check` | `deadline_scanner.py` | Flag items due within 7/30 days |
| `ops/conflict-check` | `calendar_conflict_check.py` | Find overlapping dates across calendars |
| `admin/renewal-tracker` | `renewal_check.py` | Flag renewals due within 7/30 days |

### Script invocation
```yaml
# Dynamic context injection (runs before agent sees prompt):
!`python3 ${CLAUDE_SKILL_DIR}/scripts/name.py`

# Agent calls during execution:
python3 .claude/skills/<dept>/<skill>/scripts/name.py
```

---

## Phase F: Dynamic Context Injection (9 skills)

Add `## Current State` with `!`command`` to SKILL.md files so agents see live data before executing.

| Skill | Injection |
|---|---|
| `social/content-calendar` | `!`ls -1 data/content/drafts/ data/social/ 2>/dev/null \| grep -v '.gitkeep'`` |
| `social/mention-scan` | `!`ls -1t data/social/mention-scan-* data/inbox/mention-scan-* 2>/dev/null \| head -5`` |
| `strategy/trend-scan` | `!`ls -1t data/strategy/trend-scan-* data/inbox/trend-scan-* 2>/dev/null \| head -5`` |
| `strategy/strategy-review` | `!`cat data/strategy/quarterly-roadmap.md 2>/dev/null`` |
| `strategy/campaign-plan` | `!`head -50 data/strategy/quarterly-roadmap.md 2>/dev/null`` |
| `content/content-matrix` | `!`ls -1 data/content/drafts/ 2>/dev/null \| grep -v '.gitkeep'`` |
| `content/edit-review` | `!`cat data/brand/brand-dna.md 2>/dev/null`` |
| `pr/outreach-tracker` | `!`cat data/pr/outreach-tracker.md 2>/dev/null`` |
| `pr/pr-calendar` | `!`cat data/pr/pr-calendar-*.md 2>/dev/null \| tail -60`` |

---

## Implementation Order

| Phase | What | Skills | Files created | Priority |
|---|---|---|---|---|
| **A** | Top 10 references + templates + examples | 10 | ~25 | Do first |
| **B** | Remaining Tier 1 references | 28 | ~28 | After UAT confirms which need depth |
| **C** | Tier 2 templates | 35 | ~35 | After Phase A proves the pattern |
| **D** | Tier 2 references | 25 | ~25 | When specific agents need improvement |
| **E** | Python scripts | 14 | ~14 | When data aggregation becomes a bottleneck |
| **F** | Dynamic context injection | 9 | 0 (edits to SKILL.md) | Quick wins — do anytime |
| **Total** | | **~98 skills** | **~127 files** | |

---

## Testing Checklist

- [ ] **Reference loading:** Agent reads `best-practices.md` and applies frameworks (output quality noticeably improves)
- [ ] **Template compliance:** Agent output matches `template.md` structure
- [ ] **Example influence:** Agent output approaches quality of `examples/*.md`
- [ ] **Script execution:** Python scripts produce correct output standalone
- [ ] **Context injection:** `!`command`` data appears in agent context
- [ ] **No regression:** Skills that worked before still work after upgrades
- [ ] **Context budget:** Adding references doesn't cause context overflow (keep each under 1000 lines)

---

## File Naming Convention

```
.claude/skills/<dept>/<skill>/
├── SKILL.md                          # Already exists
├── references/
│   └── best-practices.md             # Domain frameworks (one file per skill)
├── template.md                       # Output format with [FIELD] placeholders
├── examples/
│   └── example-<type>.md             # Gold-standard output
└── scripts/
    └── <name>.py                     # Python data scripts
```

Single `best-practices.md` per skill. If multiple topics, use sections within one file rather than multiple reference files. Keep under 1000 lines for context budget.
