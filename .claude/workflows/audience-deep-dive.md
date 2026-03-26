# Workflow: Audience Deep Dive

> Comprehensive audience research — who they are, where they are, what they need.

## Trigger
- "Research my audience"
- "Who is my audience really?"
- "I need to understand my audience better"
- "Update audience personas"

## Profile
Full RennOS, Brand & Business

## Steps

### 1. Quantitative Analysis
**Agent:** @audience-insights-analyst
**Skill:** audience-report
**Input:** `data/analytics/kpi-dashboard.md`, platform analytics (if connected)
**Output:** Demographics, growth rates, engagement metrics

### 2. Qualitative Research
**Agent:** @audience-researcher
**Skill:** audience-analysis
**Input:** Step 1 data + `data/strategy/audience-personas.md` (existing)
**Output:** Updated audience analysis — pain points, language, communities, JTBD

### 3. Competitive Audience Check
**Agent:** @competitive-intel-analyst
**Skill:** gap-analysis
**Input:** Step 2 output + `data/strategy/competitive-landscape.md`
**Output:** Audience gaps competitors aren't serving

### 4. Trend Overlay
**Agent:** @trend-scout
**Skill:** trend-scan
**Input:** Audience segment + industry
**Output:** Trending topics this audience cares about right now

### 5. Synthesize Personas
**Agent:** @audience-researcher
**Skill:** persona-builder
**Input:** All outputs from steps 1-4
**Output:** Refreshed `data/strategy/audience-personas.md`

### 6. Strategy Implications
**Agent:** @strategy-planner
**Skill:** strategy-review
**Input:** New personas + current roadmap
**Output:** Recommended roadmap adjustments based on audience insights

### 7. Brief User
**CEO agent presents:**
- Key audience insights (who, where, what they need)
- Gaps and opportunities
- Recommended strategy adjustments
- "Want me to update the roadmap based on these findings?"

## Data Flow
```
data/analytics/kpi-dashboard.md ← step 1 reads
data/strategy/audience-personas.md ← step 5 writes (refresh)
data/strategy/competitive-landscape.md ← step 3 reads
data/strategy/quarterly-roadmap.md ← step 6 may update
```
