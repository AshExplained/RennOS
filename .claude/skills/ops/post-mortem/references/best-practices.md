# Post-Mortem Best Practices Reference

> A comprehensive reference for running effective, blameless post-mortems.
> Covers methodology, facilitation, root cause analysis, anti-patterns, meeting structure, and action item tracking.

---

## Table of Contents

1. [Blameless Post-Mortem Methodology](#1-blameless-post-mortem-methodology)
2. [5 Whys Root Cause Analysis](#2-5-whys-root-cause-analysis)
3. [Anti-Patterns to Avoid](#3-anti-patterns-to-avoid)
4. [Post-Mortem Meeting Structure](#4-post-mortem-meeting-structure)
5. [Action Item Tracking](#5-action-item-tracking)
6. [Sources](#6-sources)

---

## 1. Blameless Post-Mortem Methodology

### 1.1 Core Philosophy

A blameless post-mortem treats human error as a **symptom of systemic problems**, not an individual failure. The goal is to understand what systemic factors led to the outcome and identify actions that prevent the same class of failure from recurring.

Key principle: *"A blamelessly written postmortem assumes that everyone involved had good intentions and did the right thing with the information they had."* — Google SRE

Blameless does **not** mean "nobody made mistakes." It means treating mistakes as signals that the system allowed failure — and improving the system so the same scenario becomes harder to repeat.

### 1.2 Culture: Building Psychological Safety

For blameless post-mortems to work, the team must have psychological safety — the confidence that raising problems, admitting mistakes, or challenging assumptions will not result in punishment or humiliation.

**How to build it:**

- **Leadership models vulnerability first.** If leaders admit their own mistakes openly, the team follows.
- **Separate post-mortem findings from performance reviews.** If post-mortem participation can hurt someone's career, people will hide information.
- **Celebrate thorough post-mortems.** Google uses monthly highlighted post-mortems shared organization-wide, reading clubs, and peer bonuses for exceptional incident handling.
- **"Wheel of Misfortune" exercises.** Role-playing past incidents normalizes failure discussion before real incidents happen.
- **Regular feedback surveys.** Ask teams whether the post-mortem process feels safe and useful. Iterate on the process itself.

### 1.3 Blame Awareness vs. Blame Elimination

The concept of a perfectly blameless post-mortem has been challenged (notably by J. Paul Reed). The tendency to blame is neurologically hardwired — evolutionary biology makes us seek someone to hold accountable. Trying to eliminate blame entirely is unrealistic.

The more practical approach is **blame awareness**: recognize cognitive biases as they arise and actively redirect.

**Cognitive biases to watch for:**

| Bias | What happens | Countermeasure |
|------|-------------|----------------|
| **Fundamental attribution error** | Attributing the incident to someone's character ("they were careless") rather than circumstances | Refocus on situational and systemic causes |
| **Confirmation bias** | Seeking evidence that supports a pre-existing blame assumption | Appoint a devil's advocate; invite outside perspectives |
| **Hindsight bias** | Seeing the incident as obvious and preventable after the fact ("they should have known") | Build the timeline forward from before the incident, reconstructing what was known at each decision point |
| **Negativity bias** | Magnifying the negative aspects disproportionately | Frame incidents as learning opportunities; explicitly acknowledge what went well |

### 1.4 Facilitation: Language and Questioning

The facilitator's language shapes the entire post-mortem tone.

**Do use:**
- **"What" questions** — ground analysis in contributing factors: *"What did you observe at that point?" "What information were you working with?"*
- **"How" questions** — explore conditions: *"How did the system behave?" "How was the decision communicated?"*
- **"How might we..." framing** — shifts from blame to solution-oriented thinking: *"How might we detect this earlier next time?"*

**Avoid:**
- **"Why did you..." questions** — forces justification and triggers defensiveness: *"Why didn't you check the logs?"* becomes an interrogation, not an analysis.
- **Counterfactual blame** — *"If only X had done Y..."* is not analysis, it is finger-pointing in disguise.

**De-escalation technique:** When defensiveness emerges, restore mutual purpose by restating the shared goal: *"We are here to improve the system, not to judge anyone. Let me reframe that question."* Use contrasting statements to clarify intent vs. interpretation.

### 1.5 Documentation Standards

A complete post-mortem document should include:

- **Incident summary** — one-paragraph description accessible to someone outside the team
- **Impact assessment** — business and customer impact, quantified where possible (users affected, revenue impact, duration)
- **Timeline** — chronological sequence from detection through resolution, with timestamps
- **Root cause analysis** — using structured methodology (5 Whys, fishbone, etc.)
- **Contributing factors** — conditions that enabled the root cause to manifest
- **What went well** — specific wins with evidence, not vague praise
- **What went poorly** — honest failures with systemic framing
- **Action items** — each with owner, description, deadline, and priority
- **Lessons learned** — distilled insights for broader organizational learning

---

## 2. 5 Whys Root Cause Analysis

### 2.1 Overview

The 5 Whys is an iterative interrogative technique for exploring cause-and-effect relationships. Developed by Sakichi Toyoda at Toyota in the 1930s, it works by repeatedly asking "why?" — typically five times — to peel back layers of symptoms and reach the underlying root cause.

The number five is a guideline, not a rule. Some problems require three levels; some require seven. The point is to keep asking until you reach a cause that, if addressed, would prevent recurrence.

### 2.2 How to Apply It

**Step 1:** Define the problem clearly and specifically.
**Step 2:** Ask "Why did this happen?" and write the answer.
**Step 3:** For each answer, ask "Why?" again.
**Step 4:** Continue until you reach a systemic or process-level root cause.
**Step 5:** Verify the causal chain by reading it in reverse — each "because" should logically follow.

### 2.3 Example: Campaign Missed Its Launch Date

```
Problem: The Q1 campaign launched 2 weeks late.

Why #1: The final assets were not approved in time.
  -> Why #2: The review cycle took 3 rounds instead of the planned 1.
    -> Why #3: The brief was not clear on brand guidelines, so the first drafts missed the mark.
      -> Why #4: The brief was written without consulting the Brand DNA document.
        -> Why #5: There is no checklist requiring Brand DNA review before brief sign-off.

Root cause: No mandatory Brand DNA alignment step in the briefing process.
Action: Add Brand DNA review as a required checklist item before any brief is approved.
```

### 2.4 Example: Content Performance Below Target

```
Problem: Blog post series averaged 40% below traffic targets.

Why #1: The posts were not ranking for target keywords.
  -> Why #2: The keyword research was based on assumptions, not data.
    -> Why #3: The content team did not have access to the SEO analytics tool.
      -> Why #4: The tool license was only assigned to one person who left.
        -> Why #5: There is no process for reassigning tool access when team changes happen.

Root cause: No offboarding/access-transfer checklist for tools and subscriptions.
Action: Create a tool-access transfer protocol triggered by any team change.
```

### 2.5 Example: Classic Manufacturing (Toyota)

```
Problem: The machine stopped functioning.

Why #1: There was an overload and the fuse blew.
  -> Why #2: The bearing was not sufficiently lubricated.
    -> Why #3: The lubrication pump was not pumping sufficiently.
      -> Why #4: The shaft of the pump was worn and rattling.
        -> Why #5: There was no strainer attached, and metal scrap got in.

Root cause: No strainer in the lubrication system to filter debris.
Action: Install a strainer on the lubrication pump intake.
```

### 2.6 Common Pitfalls

**Pitfall 1: Stopping too early.**
Teams often stop after two or three "whys" once they feel they have a plausible answer. This frequently leaves the real root cause buried. If the answer is still describing a symptom rather than a systemic cause, keep going.

**Pitfall 2: Single-track thinking.**
The 5 Whys can funnel you into a single causal chain when multiple independent causes contributed. For complex, multi-factor incidents, supplement with fishbone diagrams (Ishikawa) or Failure Mode and Effects Analysis (FMEA) to map multiple causal branches.

**Pitfall 3: Blaming individuals.**
If any "Why?" answer is a person's name or a judgment about someone's competence, you have left the systemic analysis track. Redirect: *"Why was it possible for that mistake to happen?"* — this shifts focus back to the system.

**Pitfall 4: Accepting vague answers.**
Answers like "communication breakdown" or "lack of alignment" are symptoms, not causes. Push for specifics: *"What specific information was not communicated? Through what channel should it have been? Why was that channel not used?"*

**Pitfall 5: Skipping verification.**
After completing the chain, read it in reverse as a "therefore" chain. If any link does not logically follow, the analysis has a gap. Example: "There was no strainer, therefore the shaft wore out, therefore the pump failed, therefore the bearing was not lubricated, therefore the fuse blew, therefore the machine stopped." Each link should be testable.

**Pitfall 6: Omitting contributing context.**
The 5 Whys can miss important environmental or contextual factors that do not fit neatly into the causal chain. Document contributing factors separately even if they are not the direct root cause — they often reveal systemic weaknesses worth addressing.

### 2.7 When 5 Whys Is Not Enough

Use 5 Whys for:
- Single-thread problems with a clear causal chain
- Quick analysis during or immediately after an incident
- Problems where the team has direct experience and context

Escalate to more sophisticated methods when:
- Multiple independent root causes are suspected
- The system is highly complex with many interacting components
- Previous 5 Whys analyses on the same topic have not prevented recurrence
- The incident involves cross-team or cross-system interactions

Complementary methods: Fishbone/Ishikawa diagrams, Fault Tree Analysis, FMEA, Causal Factor Charting.

---

## 3. Anti-Patterns to Avoid

### 3.1 Finger-Pointing and Blame

**The pattern:** The post-mortem becomes an arena for assigning personal blame. Statements like "If X had just done their job..." or "This happened because Y was careless" dominate.

**Why it is destructive:** People stop sharing information. Future incidents get hidden or downplayed. The post-mortem produces a scapegoat instead of systemic improvements.

**The fix:**
- Facilitator sets blameless ground rules at the start of every session
- Redirect blame language immediately: *"Let us focus on what the system allowed to happen, not on who was involved"*
- Use "inspecific responder" framing — acknowledge that anyone in the same situation with the same information could have made the same decision
- Establish "Vegas rules" for psychological safety — what is discussed stays in the room

### 3.2 Shallow Analysis (Surface-Level Fixes)

**The pattern:** The team identifies symptoms and jumps straight to solutions without tracing root causes. The "fixes" are band-aids that do not prevent recurrence. This is sometimes called the "Wheel of Fortune" anti-pattern — spinning the wheel of quick fixes hoping one sticks.

**Why it is destructive:** The same class of failure keeps recurring because the underlying cause was never addressed. Team morale drops as people feel the post-mortem process is pointless.

**The fix:**
- Mandate structured root cause analysis (5 Whys minimum) before any action items are proposed
- Generate insights before deciding what to do — separate the analysis phase from the action phase
- Test proposed actions against the root cause: *"Would this fix have prevented the incident? Or just the symptom?"*

### 3.3 No Follow-Through on Action Items

**The pattern:** The post-mortem produces a list of action items. Nobody tracks them. Nobody is accountable. The same issues surface in the next post-mortem.

**Why it is destructive:** It teaches the team that post-mortems are performative — a box to check rather than a driver of improvement. Engagement drops sharply after a few cycles of wasted effort.

**The fix:**
- Every action item must have a single named owner (not "the team"), a specific description of what "done" looks like, and a deadline
- Integrate post-mortem action items into the regular work tracking system (task tracker, sprint backlog, etc.)
- Review status of previous post-mortem actions at the start of each new post-mortem
- Schedule 30-day follow-ups for complex items

### 3.4 Extensive Whining Without Solutions

**The pattern:** The team spends the entire session complaining about what went wrong but never transitions to constructive analysis or action planning. Participants adopt a victim mindset.

**Why it is destructive:** Emotional venting without structure does not produce improvements. It reinforces helplessness and drains energy.

**The fix:**
- Time-box the "what went wrong" section and enforce transition to analysis
- Use structured prompts: *"Given that this happened, what systemic change would make it less likely?"*
- The facilitator's job is to redirect venting into inquiry

### 3.5 Groundhog Day (Same Issues Recurring)

**The pattern:** The same problems appear in post-mortem after post-mortem. The team discusses them, writes the same action items, and nothing changes.

**Why it is destructive:** It signals a fundamental breakdown in either action item execution or root cause analysis depth. Team trust in the process erodes completely.

**The fix:**
- When a recurring issue surfaces, escalate the root cause analysis — the previous analysis clearly did not go deep enough
- Audit previous action items: were they completed? Were they effective? If completed but ineffective, the root cause was misidentified
- Consider whether the issue requires structural/organizational change rather than process tweaks

### 3.6 Skipping the Post-Mortem Entirely

**The pattern:** The team is too busy, too tired, or too demoralized to hold a post-mortem. The incident is "resolved" and everyone moves on.

**Why it is destructive:** Every skipped post-mortem is a missed learning opportunity and an implicit message that improvement does not matter.

**The fix:**
- Establish clear triggers for when a post-mortem is mandatory (missed targets by X%, timeline slipped by Y days, any unplanned escalation, etc.)
- Keep the bar low for simpler incidents — even a 15-minute structured review is better than nothing
- Schedule the post-mortem immediately upon resolution, before calendars fill up

### 3.7 The Dominated Room

**The pattern:** One or two people (usually the most senior or most vocal) control the conversation. Quieter team members do not contribute, even though they may have critical perspectives.

**Why it is destructive:** Key information goes unheard. The post-mortem reflects one perspective instead of the full picture.

**The fix:**
- Use written input before discussion — have everyone write observations independently first
- Round-robin contributions to ensure every voice is heard
- The facilitator should actively invite input: *"We have not heard from X yet — what was your experience?"*
- Consider anonymous input channels for sensitive observations

### 3.8 No Positive Analysis

**The pattern:** The post-mortem focuses exclusively on what went wrong, ignoring what went well or what prevented the situation from being worse.

**Why it is destructive:** It creates a relentlessly negative association with post-mortems. People dread them. It also misses the opportunity to reinforce and systematize effective practices.

**The fix:**
- Include a dedicated "What went well" section in every post-mortem
- Be specific — *"The monitoring alert fired within 2 minutes"* is useful; *"Good teamwork"* is not
- Identify practices worth codifying or extending to other areas

---

## 4. Post-Mortem Meeting Structure

### 4.1 Timing

Hold the post-mortem **24-72 hours** after resolution. This balances:
- **Memory freshness** — details fade quickly after 72 hours
- **Emotional readiness** — holding it immediately after a stressful incident can produce reactive, blame-heavy discussion

For campaigns or projects (as opposed to incidents), hold the post-mortem within one week of completion while the work is still fresh.

### 4.2 Participants

- **Facilitator** — neutral party who manages the process (ideally not someone deeply involved in the incident)
- **Key contributors** — everyone directly involved in the project/incident
- **Stakeholders** — those affected by the outcome (optional, depending on scope)
- **Note-taker** — dedicated person (not the facilitator) to capture discussion

### 4.3 Recommended Agenda

| Phase | Duration | Purpose |
|-------|----------|---------|
| **1. Set the stage** | 5 min | State blameless principles, review agenda, establish ground rules |
| **2. Review timeline** | 15 min | Walk through what happened chronologically — detection, escalation, actions taken, resolution |
| **3. What went well** | 10 min | Identify specific wins and effective practices |
| **4. Contributing factors analysis** | 20 min | Apply 5 Whys or other RCA methodology to understand root causes |
| **5. Action items** | 15 min | Define specific, owned, time-bound improvements |
| **6. Close and share** | 5 min | Summarize key learnings, confirm action item owners, set follow-up date |

**Total: ~70 minutes.** Adjust based on complexity — simple projects may need 30 minutes; major incidents may need 90+.

### 4.4 Facilitator Checklist

**Before the meeting:**
- [ ] Gather all available data (metrics, timelines, communications, artifacts)
- [ ] Pre-distribute data to participants so they can review before the session
- [ ] Prepare the post-mortem document template
- [ ] Confirm attendance of all key contributors

**During the meeting:**
- [ ] Open with blameless principles and ground rules
- [ ] Maintain neutral facilitation — redirect blame, keep discussion constructive
- [ ] Ensure all voices are heard, not just the loudest
- [ ] Time-box each section to prevent rabbit holes
- [ ] Capture action items in real-time with owners and deadlines

**After the meeting:**
- [ ] Finalize and distribute the post-mortem document within 24 hours
- [ ] Ensure action items are entered into the task tracking system
- [ ] Schedule a follow-up review (30 days for complex items)
- [ ] Share key learnings with the broader organization where relevant

### 4.5 Senior Review

Adapted from Google's practice: before broad distribution, have a senior team member review the post-mortem for:
- Completeness of incident/project data
- Depth of impact assessment
- Rigor of root cause analysis
- Appropriateness and specificity of action items
- Blameless tone throughout

---

## 5. Action Item Tracking

### 5.1 What Makes a Good Action Item

Every action item must answer five questions:

1. **What** — specific, concrete description of the change (not vague: "improve communication")
2. **Who** — single named owner (a department or agent in RennOS context), never "the team"
3. **When** — realistic deadline
4. **Why** — which root cause or contributing factor it addresses
5. **Done means** — clear definition of completion (what does "done" look like?)

### 5.2 Action Item Categories

| Category | Description | Example |
|----------|-------------|---------|
| **Process change** | Modify an existing workflow or create a new one | Add Brand DNA review step to briefing checklist |
| **Tooling improvement** | Add, fix, or configure tools | Set up automated alerts for KPI threshold breaches |
| **Documentation** | Create or update docs, runbooks, checklists | Write a handoff protocol for tool access during team changes |
| **Training** | Knowledge transfer or skill development | Run a workshop on the new content review process |
| **Monitoring** | Add or improve detection capabilities | Create a dashboard tracking brief-to-launch cycle time |

### 5.3 Tracking Discipline

- **Treat action items as formal work.** They go into the task tracker alongside regular tasks, not into a forgotten post-mortem document.
- **Review in regular planning.** Include post-mortem actions in sprint planning or weekly reviews.
- **Previous actions audit.** At the start of every new post-mortem, review the status of actions from the last one. This creates accountability and surfaces patterns.
- **30-day follow-up.** For structural or complex changes, schedule a dedicated check-in to verify the change is working as intended.
- **Escalation path.** If an action item is blocked or deprioritized repeatedly, escalate. Persistent deprioritization of post-mortem actions is itself an anti-pattern worth examining.

### 5.4 Measuring Post-Mortem Effectiveness

Track these meta-metrics to evaluate whether your post-mortem practice is working:

- **Action item completion rate** — percentage of action items completed by deadline
- **Recurrence rate** — how often the same root cause appears across multiple post-mortems
- **Time to post-mortem** — how quickly after resolution the post-mortem is held
- **Participation quality** — are all relevant people attending and contributing?
- **Sentiment** — does the team find post-mortems useful? (periodic survey)

---

## 6. Sources

1. [Google SRE Book — Postmortem Culture: Learning from Failure](https://sre.google/sre-book/postmortem-culture/) — Google's foundational guide to building a blameless postmortem culture in engineering organizations. Covers triggers, writing standards, review processes, and cultural reinforcement techniques.

2. [PagerDuty — The Blameless Postmortem](https://postmortems.pagerduty.com/culture/blameless/) — Detailed guide on blameless methodology including cognitive bias awareness, facilitation language, and the "blame aware" framework from J. Paul Reed.

3. [Rootly — How to Run Postmortem Meetings: 2026 Guide](https://rootly.com/incident-postmortems/meeting-guide) — Comprehensive meeting structure, facilitation tips, timing recommendations, and action item tracking best practices.

4. [Scrum.org — 21 Sprint Retrospective Anti-Patterns](https://www.scrum.org/resources/blog/21-sprint-retrospective-anti-patterns) — Catalog of retrospective anti-patterns including blame dynamics, shallow analysis, lack of follow-through, and facilitation failures.

5. [Atlassian — How to Run a Blameless Postmortem](https://www.atlassian.com/incident-management/postmortem/blameless) — Practical guide covering blameless culture, meeting facilitation, and documentation standards.

6. [FlowFuse — Five Whys Root Cause Analysis: Definition, Steps & Examples (2026)](https://flowfuse.com/blog/2025/12/five-whys-root-cause-analysis-definition-examples/) — Detailed breakdown of the 5 Whys technique with examples, common pitfalls, and guidance on when to use complementary methods.

7. [Martin Fowler — Retrospectives Antipatterns](https://martinfowler.com/articles/retrospective-antipatterns.html) — Analysis of common retrospective failure modes and how to address them.
