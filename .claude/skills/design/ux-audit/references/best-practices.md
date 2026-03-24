# UX Audit Best Practices Reference

> Comprehensive reference for conducting UX audits using established heuristics,
> accessibility standards, cognitive load theory, and structured scoring methodology.

---

## Table of Contents

1. [Nielsen's 10 Usability Heuristics](#nielsens-10-usability-heuristics)
2. [WCAG 2.2 Accessibility Requirements](#wcag-22-accessibility-requirements)
3. [Cognitive Load Theory](#cognitive-load-theory)
4. [UX Audit Scoring Methodology](#ux-audit-scoring-methodology)
5. [Sources](#sources)

---

## Nielsen's 10 Usability Heuristics

Originally developed by Jakob Nielsen in 1994, these 10 general principles for interaction
design remain the industry standard for heuristic evaluation. Each heuristic below includes
its definition, practical examples, application tips, and severity rating guidance.

### Severity Rating Scale (Applied Per Heuristic)

| Rating | Label | Description |
|--------|-------|-------------|
| 0 | No issue | No usability problem detected |
| 1 | Cosmetic | Minor issue; fix only if extra time is available |
| 2 | Minor | Low priority; causes slight user friction |
| 3 | Major | High priority; significantly impacts usability |
| 4 | Critical | Must fix before release; blocks users from completing tasks |

---

### H1: Visibility of System Status

**Principle:** The design should always keep users informed about what is going on,
through appropriate feedback within a reasonable amount of time.

**Why it matters:** When users know the current system state, they can predict the
outcome of their interactions and make informed decisions about next steps. Lack of
feedback creates uncertainty and erodes trust.

**Examples:**
- Progress bars during file uploads or multi-step forms
- "You are here" indicators in navigation breadcrumbs
- Real-time character counts in text fields with limits
- Loading spinners or skeleton screens during data fetches
- Order tracking status in e-commerce flows

**Application tips:**
- Communicate system state clearly before consequential actions
- Present feedback as quickly as possible (ideally immediately)
- Build trust through open and continuous communication
- Use appropriate feedback types: visual, auditory, or haptic

**Common violations:**
- Forms that submit without any confirmation or loading state
- Background processes with no progress indication
- State changes that happen silently without user awareness

---

### H2: Match Between System and the Real World

**Principle:** The design should speak the users' language. Use words, phrases, and
concepts familiar to the user, rather than internal jargon. Follow real-world conventions,
making information appear in a natural and logical order.

**Why it matters:** When interfaces use language and concepts that match user expectations,
users can transfer existing knowledge to the interface, reducing learning time.

**Examples:**
- Stovetop controls that match the spatial layout of heating elements
- Shopping cart metaphor in e-commerce
- Folder and file metaphors in file management systems
- Calendar interfaces that mirror physical calendar layouts

**Application tips:**
- Never assume your understanding of terms matches your users'
- Conduct user research to uncover familiar terminology and mental models
- Use language that matches the audience's domain expertise level
- Order information in a way that mirrors real-world expectations

**Common violations:**
- Technical error codes shown to non-technical users
- Internal product names exposed in the UI
- Navigation structures that reflect org charts rather than user tasks

---

### H3: User Control and Freedom

**Principle:** Users often perform actions by mistake. They need a clearly marked
"emergency exit" to leave the unwanted action without having to go through an
extended process.

**Why it matters:** When users feel in control and can easily reverse mistakes, they
explore more confidently and trust the system. Feeling trapped increases frustration
and abandonment.

**Examples:**
- Undo/Redo functionality in editors
- Clearly labeled Cancel buttons on forms and modals
- "Back" navigation that preserves form state
- Gmail's "Undo Send" feature with a brief grace period
- Easy account deletion or subscription cancellation flows

**Application tips:**
- Support Undo and Redo wherever destructive actions occur
- Show clear exit paths labeled with descriptive text (not just "X")
- Allow users to back out of multi-step processes without losing progress
- Provide confirmation dialogs for irreversible actions

**Common violations:**
- Multi-step wizards with no back button
- Modal dialogs that are difficult to dismiss
- Irreversible delete actions without confirmation or undo

---

### H4: Consistency and Standards

**Principle:** Users should not have to wonder whether different words, situations, or
actions mean the same thing. Follow platform and industry conventions.

**Why it matters:** Consistency reduces the learning curve by letting users transfer
knowledge from one part of the interface to another, and from other products they
already know.

**Examples:**
- Consistent button styles and placement across all pages
- Standard icon usage (magnifying glass for search, gear for settings)
- Uniform terminology throughout the product
- Platform-native UI patterns (iOS vs Android conventions)

**Application tips:**
- Maintain internal consistency within your product
- Maintain consistency across product families and sub-brands
- Follow established industry conventions (external consistency)
- Create and follow a design system or style guide

**Common violations:**
- Same action labeled differently across pages ("Save" vs "Submit" vs "Done")
- Inconsistent navigation patterns between sections
- Custom controls that don't behave like their platform equivalents

---

### H5: Error Prevention

**Principle:** Good error messages are important, but the best designs carefully prevent
problems from occurring in the first place. Either eliminate error-prone conditions, or
check for them and present users with a confirmation option before they commit to the
action.

**Why it matters:** Preventing errors is always better than recovering from them.
Error prevention reduces user frustration, support costs, and data quality issues.

**Two types of errors to prevent:**
- **Slips:** Unconscious errors caused by inattention (typos, misclicks)
- **Mistakes:** Conscious errors caused by mental model mismatch

**Examples:**
- Inline form validation before submission
- Confirmation dialogs before destructive actions ("Delete 23 files?")
- Disabling the submit button until all required fields are valid
- Smart defaults that reduce the need for manual input
- Date pickers instead of free-text date entry

**Application tips:**
- Prioritize preventing high-cost errors first, then address minor frustrations
- Provide helpful constraints (input masks, dropdown menus)
- Supply good defaults to reduce decision burden
- Use inline validation to catch errors early

**Common violations:**
- Allowing form submission with invalid data then showing errors after
- No confirmation before deleting or overwriting data
- Free-text fields where structured input would prevent formatting errors

---

### H6: Recognition Rather Than Recall

**Principle:** Minimize the user's memory load by making elements, actions, and options
visible. The user should not have to remember information from one part of the interface
to another. Information required to use the design should be visible or easily retrievable.

**Why it matters:** Human short-term memory is limited (approximately 7 plus or minus 2 items).
Interfaces that demand recall force users to hold information in working memory, increasing
cognitive load and error rates.

**Examples:**
- Recent search history and suggestions in search bars
- Persistent navigation showing current location in the hierarchy
- Tooltip hints on icon-only buttons
- Auto-complete fields that suggest options as users type
- "Recently viewed items" in e-commerce

**Application tips:**
- Let people recognize information rather than forcing recall
- Offer help in context instead of requiring memorization of tutorials
- Reduce the information users must remember across steps
- Keep important actions and options visible, not hidden in menus

**Common violations:**
- Reference numbers that users must remember across screens
- Icon-only toolbars with no labels or tooltips
- Instructions shown once then never accessible again

---

### H7: Flexibility and Efficiency of Use

**Principle:** Shortcuts, hidden from novice users, may speed up interaction for expert
users so that the design can cater to both inexperienced and experienced users. Allow
users to tailor frequent actions.

**Why it matters:** A one-size-fits-all interface frustrates both novices (overwhelmed
by options) and experts (slowed by unnecessary steps). Flexible designs serve both.

**Examples:**
- Keyboard shortcuts for power users (Ctrl+S, Cmd+K)
- Customizable toolbars and dashboards
- Touch gestures as alternatives to button taps
- Saved templates for frequently repeated tasks
- Quick actions and command palettes

**Application tips:**
- Provide accelerators like keyboard shortcuts and touch gestures
- Enable personalization to tailor content for individual users
- Allow customization so users control how the product functions
- Progressively reveal advanced features as users gain expertise

**Common violations:**
- No keyboard shortcuts for frequent actions
- Inability to save preferences or customize workflows
- Forcing experienced users through tutorial flows on every visit

---

### H8: Aesthetic and Minimalist Design

**Principle:** Interfaces should not contain information that is irrelevant or rarely
needed. Every extra unit of information in an interface competes with the relevant units
of information and diminishes their relative visibility.

**Why it matters:** Visual clutter increases cognitive load and makes it harder for users
to find what they need. Minimalism is not about removing features but about prioritizing
the right content.

**Examples:**
- Google's homepage: search bar dominates, everything else is secondary
- Progressive disclosure: showing advanced options only when requested
- Card-based layouts that chunk related information
- Clean data tables with the ability to show/hide columns

**Application tips:**
- Keep UI content and visual design focused on the essentials
- Prevent unnecessary elements from distracting users
- Prioritize content and features that support primary user goals
- Use progressive disclosure to reveal complexity on demand

**Common violations:**
- Dashboards that show every metric simultaneously
- Marketing banners competing with primary content
- Dense forms that could be broken into logical steps

---

### H9: Help Users Recognize, Diagnose, and Recover from Errors

**Principle:** Error messages should be expressed in plain language (no error codes),
precisely indicate the problem, and constructively suggest a solution.

**Why it matters:** When errors inevitably occur, clear recovery guidance prevents
user frustration, reduces support requests, and keeps users on track.

**Examples:**
- "Your password must be at least 8 characters" vs "Invalid password"
- 404 pages with search functionality and navigation links
- Form validation that highlights the specific field and explains the fix
- Suggested corrections for misspelled search queries

**Application tips:**
- Use traditional error message visuals (bold, red text) for recognition
- Explain what went wrong in user-friendly language, avoiding technical jargon
- Offer constructive solutions or shortcuts that immediately resolve the error
- Place error messages near the source of the problem

**Common violations:**
- Generic "Something went wrong" messages with no guidance
- Error codes displayed without human-readable explanation
- Error messages shown in locations far from the problem source

---

### H10: Help and Documentation

**Principle:** It is best if the system does not need any additional explanation.
However, it may be necessary to provide documentation to help users understand how
to complete their tasks.

**Why it matters:** Even the most intuitive interfaces have moments where users need
guidance. Effective help documentation bridges the gap between user knowledge and
task requirements.

**Examples:**
- Contextual tooltips and inline help text
- Searchable FAQ and knowledge base
- Onboarding tutorials and interactive walkthroughs
- Chatbot assistance for common questions
- Empty states with guidance on how to get started

**Application tips:**
- Ensure help documentation is easy to search
- Present documentation in context at the moment users need it
- List concrete, actionable steps to carry out
- Keep help content concise and task-focused, not exhaustive

**Common violations:**
- No help documentation at all
- Documentation that is outdated or inaccurate
- Help content that cannot be searched or filtered
- Onboarding that cannot be revisited after initial setup

---

## WCAG 2.2 Accessibility Requirements

The Web Content Accessibility Guidelines (WCAG) 2.2 are organized around four principles
known as POUR: Perceivable, Operable, Understandable, and Robust. Level AA conformance
is the recommended standard for legal compliance and practical accessibility.

### Principle 1: Perceivable

Information and UI components must be presentable in ways users can perceive.
Content cannot be invisible to all senses.

#### 1.1 Text Alternatives
- **1.1.1 Non-text Content (A):** All images, icons, and non-text elements must have
  equivalent alternative text that serves the same purpose.

#### 1.2 Time-Based Media
- **1.2.1 Audio-only/Video-only (A):** Provide transcripts for audio-only; provide
  either transcripts or audio descriptions for video-only content.
- **1.2.2 Captions -- Prerecorded (A):** Synchronized captions for all prerecorded video
  with audio.
- **1.2.3 Audio Description or Alternative (A):** Transcript or audio description for
  prerecorded video.
- **1.2.4 Captions -- Live (AA):** Synchronized captions for live video with audio.
- **1.2.5 Audio Description -- Prerecorded (AA):** Audio descriptions for all prerecorded
  video content.

#### 1.3 Adaptable
- **1.3.1 Info and Relationships (A):** Use semantic markup to convey structure
  (headings, lists, tables, form labels).
- **1.3.2 Meaningful Sequence (A):** Reading and navigation order must be logical and
  intuitive.
- **1.3.3 Sensory Characteristics (A):** Instructions must not rely solely on shape,
  size, visual location, or sound.
- **1.3.4 Orientation (AA):** Content must not be restricted to a single display
  orientation (portrait or landscape) unless essential.
- **1.3.5 Identify Input Purpose (AA):** Form fields collecting personal data must use
  proper autocomplete attributes.

#### 1.4 Distinguishable
- **1.4.1 Use of Color (A):** Color alone must not convey meaning or distinguish
  visual elements.
- **1.4.2 Audio Control (A):** Audio playing longer than 3 seconds must have pause,
  stop, or volume controls.
- **1.4.3 Contrast Minimum (AA):** Text and images of text must have a contrast ratio
  of at least 4.5:1 (3:1 for large text).
- **1.4.4 Resize Text (AA):** Text must be resizable up to 200% without loss of
  content or functionality.
- **1.4.5 Images of Text (AA):** Use actual text instead of images of text wherever
  possible.
- **1.4.10 Reflow (AA):** Content must reflow at 320px width without horizontal
  scrolling (responsive design).
- **1.4.11 Non-text Contrast (AA):** UI components and graphical objects must have a
  contrast ratio of at least 3:1.
- **1.4.12 Text Spacing (AA):** No loss of content or functionality when users adjust
  line height, letter spacing, word spacing, or paragraph spacing.
- **1.4.13 Content on Hover or Focus (AA):** Additional content triggered by hover or
  focus must be dismissible, hoverable, and persistent.

### Principle 2: Operable

UI components and navigation must be operable by all users. The interface must not
require interactions that a user cannot perform.

#### 2.1 Keyboard Accessible
- **2.1.1 Keyboard (A):** All functionality must be available via keyboard.
- **2.1.2 No Keyboard Trap (A):** Keyboard focus must never become trapped; users must
  be able to navigate away from any component.
- **2.1.4 Character Key Shortcuts (A):** Single character key shortcuts must be
  remappable or disableable.

#### 2.2 Enough Time
- **2.2.1 Timing Adjustable (A):** Users must be able to turn off, adjust, or extend
  time limits.
- **2.2.2 Pause, Stop, Hide (A):** Auto-moving or auto-updating content must be
  pausable, stoppable, or hideable.

#### 2.3 Seizures and Physical Reactions
- **2.3.1 Three Flashes or Below Threshold (A):** Content must not flash more than
  3 times per second.

#### 2.4 Navigable
- **2.4.1 Bypass Blocks (A):** Provide skip navigation links to bypass repeated
  content blocks.
- **2.4.2 Page Titled (A):** Pages must have descriptive, informative titles.
- **2.4.3 Focus Order (A):** Focus order must be logical and intuitive.
- **2.4.4 Link Purpose in Context (A):** The purpose of each link must be determinable
  from the link text or its context.
- **2.4.5 Multiple Ways (AA):** Provide multiple ways to find pages (search, sitemap,
  table of contents).
- **2.4.6 Headings and Labels (AA):** Headings and labels must be descriptive and
  informative.
- **2.4.7 Focus Visible (AA):** Keyboard focus indicator must be visible on all
  interactive elements.
- **2.4.11 Focus Not Obscured (AA):** Focused elements must not be entirely hidden by
  other content (new in WCAG 2.2).

#### 2.5 Input Modalities
- **2.5.1 Pointer Gestures (A):** Multipoint or path-based gestures must have
  single-pointer alternatives.
- **2.5.2 Pointer Cancellation (A):** Actions must complete on up-event, not
  down-event, allowing cancellation.
- **2.5.3 Label in Name (A):** Accessible names must include the visible label text.
- **2.5.4 Motion Actuation (A):** Motion-activated functions must have UI alternatives
  and be disableable.
- **2.5.7 Dragging Movements (AA):** Drag operations must have non-dragging
  alternatives (new in WCAG 2.2).
- **2.5.8 Target Size Minimum (AA):** Touch/click targets must be at least 24x24 CSS
  pixels (new in WCAG 2.2).

### Principle 3: Understandable

Information and UI operation must be understandable. Content and interactions must not
be beyond the user's ability to comprehend.

#### 3.1 Readable
- **3.1.1 Language of Page (A):** The default language of the page must be identified
  in markup (lang attribute).
- **3.1.2 Language of Parts (AA):** Content in a different language must be identified
  with a lang attribute.

#### 3.2 Predictable
- **3.2.1 On Focus (A):** Receiving focus must not trigger unexpected context changes.
- **3.2.2 On Input (A):** Changing a form input must not cause unexpected context
  changes without prior notice.
- **3.2.3 Consistent Navigation (AA):** Repeated navigation must appear in the same
  order across pages.
- **3.2.4 Consistent Identification (AA):** Components with the same functionality
  must be identified consistently.
- **3.2.6 Consistent Help (A):** Help mechanisms must be in consistent locations
  across pages (new in WCAG 2.2).

#### 3.3 Input Assistance
- **3.3.1 Error Identification (A):** Errors must be clearly identified and described
  in text.
- **3.3.2 Labels or Instructions (A):** Form inputs must have labels or instructions.
- **3.3.3 Error Suggestion (AA):** Error messages must suggest how to fix the input.
- **3.3.4 Error Prevention -- Legal/Financial/Data (AA):** Submissions must be
  reversible, verifiable, or confirmable.
- **3.3.7 Redundant Entry (A):** Previously-entered info must be auto-populated or
  selectable (new in WCAG 2.2).
- **3.3.8 Accessible Authentication Minimum (AA):** Authentication must not require
  cognitive function tests unless alternatives are provided (new in WCAG 2.2).

### Principle 4: Robust

Content must be robust enough to be reliably interpreted by a wide variety of user
agents, including assistive technologies.

#### 4.1 Compatible
- **4.1.2 Name, Role, Value (A):** All UI components must have proper names, roles,
  states, and values exposed to assistive technology.
- **4.1.3 Status Messages (AA):** Status messages must be programmatically determinable
  via ARIA roles without receiving focus.

### Quick Accessibility Checklist for UX Audits

Use this during audits to quickly verify the most impactful accessibility criteria:

- [ ] All images have meaningful alt text (or empty alt for decorative)
- [ ] Color contrast meets 4.5:1 for normal text, 3:1 for large text
- [ ] All functionality is keyboard accessible with visible focus indicators
- [ ] Focus order is logical and follows visual layout
- [ ] Form fields have associated labels and clear error messages
- [ ] No content relies solely on color to convey meaning
- [ ] Touch targets are at least 24x24 CSS pixels
- [ ] Content reflows at 320px without horizontal scroll
- [ ] Video has captions; audio has transcripts
- [ ] Page language is specified in HTML
- [ ] Headings follow a logical hierarchy (h1, h2, h3...)
- [ ] ARIA attributes are used correctly and not redundantly

---

## Cognitive Load Theory

Cognitive load theory, developed by John Sweller in the 1980s, describes how the human
brain's limited working memory capacity affects the processing of new information. In UX
design, managing cognitive load is essential for creating interfaces that users can
navigate effectively without feeling overwhelmed.

**Core principle:** Human brains have a limited amount of processing power. When the
information presented exceeds this capacity, users experience slower comprehension,
miss important details, or abandon tasks entirely.

### The Three Types of Cognitive Load

#### 1. Intrinsic Cognitive Load

**Definition:** The inherent difficulty of the task or content itself. This load depends
on the complexity of the material and the user's prior knowledge.

**Characteristics:**
- Cannot be eliminated -- it is inherent to the task
- Varies by user expertise (experts have schemas that reduce intrinsic load)
- Determined by element interactivity (how many elements must be processed simultaneously)

**UX implications:**
- Simplify complex tasks by breaking them into smaller steps
- Provide progressive disclosure for advanced features
- Offer different paths for novice vs expert users
- Use wizards or step-by-step flows for inherently complex processes

**Examples:**
- Filing taxes (inherently complex) vs checking the weather (inherently simple)
- A beginner learning a new software tool vs an expert using keyboard shortcuts

#### 2. Extraneous Cognitive Load

**Definition:** Mental processing caused by poor design or presentation that does not
contribute to understanding. This is the load designers should minimize.

**Characteristics:**
- Caused by how information is presented, not the information itself
- Entirely under the designer's control
- The primary target for reduction in UX optimization

**UX implications:**
- Eliminate visual clutter and decorative-only elements
- Remove redundant or irrelevant content from the interface
- Ensure layout and information architecture are intuitive
- Use consistent patterns to reduce learning overhead

**Examples:**
- Different font styles that convey no unique meaning
- Irrelevant images or animations that distract from the task
- Complex navigation structures that obscure the content
- Inconsistent button placement across different screens

#### 3. Germane Cognitive Load

**Definition:** The mental effort dedicated to processing, understanding, and integrating
new information into long-term memory. Unlike the other two types, germane load is
beneficial and should be optimized (not reduced).

**Characteristics:**
- Represents productive mental effort that aids learning
- Supports schema construction and pattern recognition
- Should be maintained or enhanced, not minimized

**UX implications:**
- Use meaningful grouping and categorization
- Provide clear conceptual models and metaphors
- Encourage exploration through safe, reversible interactions
- Build on users' existing mental models

**Examples:**
- A well-organized settings page that helps users build a mental model of the system
- Consistent use of color coding that teaches users to associate meaning with colors
- Onboarding flows that build understanding progressively

### Cognitive Load Reduction Techniques for UX

#### Technique 1: Avoid Visual Clutter
- Remove redundant links, images, and decorative typography
- Maintain generous whitespace to separate content groups
- Limit the number of visible actions and choices at any given moment
- Use clear visual hierarchy to direct attention

#### Technique 2: Leverage Existing Mental Models
- Use standard UI patterns (hamburger menus, search bars, shopping carts)
- Follow platform conventions (iOS, Android, web standards)
- Use familiar terminology from the user's domain
- Position elements where users expect to find them

#### Technique 3: Offload Tasks from Working Memory
- Use auto-complete and smart suggestions
- Display previously entered data rather than requiring re-entry
- Provide intelligent defaults for form fields
- Show contextual information (tooltips, inline help) instead of requiring memorization

#### Technique 4: Chunk Information
- Break content into digestible sections with clear headings
- Use multi-step forms instead of single long forms
- Group related options visually (card layouts, sections, tabs)
- Limit choices per view (Hick's Law: decision time increases with options)

#### Technique 5: Use Progressive Disclosure
- Show only essential information initially
- Reveal advanced options on demand ("Show more", "Advanced settings")
- Layer complexity so users encounter it only when ready
- Use accordions, expandable sections, and drill-down navigation

#### Technique 6: Provide External Memory Aids
- Breadcrumb navigation showing the user's path
- Persistent search with recent queries
- Shopping carts and wishlists that remember selections
- Comparison tools that hold multiple options side by side

---

## UX Audit Scoring Methodology

### Overview

A UX audit is a systematic evaluation of a product's user experience against established
heuristics and best practices. The methodology below combines heuristic evaluation with
accessibility review and cognitive load assessment into a structured, repeatable process.

### Phase 1: Preparation

1. **Define scope** -- Which pages, flows, or features to audit
2. **Identify user goals** -- What tasks are users trying to accomplish
3. **Gather context** -- Brand guidelines, audience personas, analytics data
4. **Assemble evaluators** -- 3-5 independent evaluators for best coverage
   (a single evaluator finds ~35% of issues; 3-5 evaluators find ~75%)

### Phase 2: Heuristic Evaluation

For each page or flow, evaluate against all 10 Nielsen heuristics using the severity
rating scale:

| Rating | Label | Description | Action |
|--------|-------|-------------|--------|
| 0 | None | No usability problem | No action needed |
| 1 | Cosmetic | Minor visual or text issue | Fix if time allows |
| 2 | Minor | Causes slight friction for some users | Schedule fix |
| 3 | Major | Significantly impairs usability | Prioritize fix |
| 4 | Critical | Blocks users from completing tasks | Fix immediately |

**Per-heuristic scoring template:**

```
Heuristic: [Name]
Score: [0-4]
Location: [Page/screen/component]
Issue: [Description of the problem]
Impact: [How it affects users]
Recommendation: [Specific fix]
```

### Phase 3: Accessibility Review

Evaluate against the WCAG 2.2 AA checklist (see above). For each criterion:
- **Pass** -- Meets the requirement
- **Fail** -- Does not meet the requirement (note severity)
- **N/A** -- Criterion does not apply to this content

### Phase 4: Cognitive Load Assessment

Evaluate each key user flow for cognitive load issues:
- Is the intrinsic load appropriate for the target audience?
- What extraneous load can be eliminated?
- Is germane load supported through good information architecture?

### Phase 5: Scoring and Reporting

#### Overall UX Score (1-10)

Calculate the overall score using weighted category scores:

| Category | Weight | Score Range | Description |
|----------|--------|-------------|-------------|
| Usability (Heuristics) | 35% | 1-10 | Nielsen's 10 heuristics composite |
| Accessibility | 25% | 1-10 | WCAG 2.2 AA compliance level |
| Cognitive Load | 15% | 1-10 | Information architecture and mental effort |
| Visual Design | 10% | 1-10 | Aesthetics, consistency, brand alignment |
| Mobile Usability | 10% | 1-10 | Responsive design, touch targets, performance |
| Conversion Path | 5% | 1-10 | CTA clarity, friction in conversion flow |

**Overall Score = Sum of (Category Score x Weight)**

#### Score Interpretation

| Score | Rating | Meaning |
|-------|--------|---------|
| 9-10 | Excellent | Industry-leading UX; minor refinements only |
| 7-8 | Good | Solid UX with room for improvement |
| 5-6 | Fair | Noticeable usability issues affecting some users |
| 3-4 | Poor | Significant problems impacting most users |
| 1-2 | Critical | Fundamental UX failures requiring redesign |

#### Report Structure

1. **Executive Summary** -- Overall score, top 3 strengths, top 3 critical issues
2. **Heuristic Evaluation** -- Per-heuristic scores with evidence
3. **Accessibility Audit** -- WCAG pass/fail with specific violations
4. **Cognitive Load Analysis** -- Load type assessment per key flow
5. **Issue Log** -- All issues ranked by severity with recommendations
6. **Prioritized Roadmap** -- Fixes organized by impact and effort

### Best Practices for Conducting Audits

- Evaluate independently before group discussion to avoid bias
- Walk through actual user flows, not just individual screens
- Document issues with screenshots or specific element references
- Focus on patterns of issues, not just individual occurrences
- Combine heuristic evaluation with real user testing for deeper insights
- Re-audit after fixes to verify improvements and prevent regression

---

## Sources

1. Nielsen, J. (1994). "10 Usability Heuristics for User Interface Design."
   Nielsen Norman Group. https://www.nngroup.com/articles/ten-usability-heuristics/

2. W3C Web Accessibility Initiative (2023). "Web Content Accessibility Guidelines
   (WCAG) 2.2." W3C Recommendation. https://www.w3.org/TR/WCAG22/

3. WebAIM (2024). "WebAIM's WCAG 2 Checklist." https://webaim.org/standards/wcag/checklist

4. Nielsen Norman Group. "Minimize Cognitive Load to Maximize Usability."
   https://www.nngroup.com/articles/minimize-cognitive-load/

5. Sweller, J. (1988). "Cognitive Load During Problem Solving: Effects on Learning."
   Cognitive Science, 12(2), 257-285.

6. LogRocket (2024). "How to conduct a heuristic evaluation for UX/UI designs."
   https://blog.logrocket.com/ux-design/conduct-heuristic-evaluation-tutorial/

7. Laws of UX. "Cognitive Load." https://lawsofux.com/cognitive-load/
