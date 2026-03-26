# Workflow: Content Repurpose

> Turn one piece of content into multiple formats across platforms.

## Trigger
- "Repurpose this [article/post/video] into [formats]"
- "Turn this blog post into social content"
- "I wrote this — make it work everywhere"

## Profile
Full RennOS, Brand & Business

## Steps

### 1. Analyze Source Content
**Agent:** @content-repurposer
**Skill:** content-matrix
**Input:** Source content (URL, file path, or pasted text)
**Output:** Content matrix — what formats this source can become, with priority ranking
**Notes:** Reads `data/content/content-matrix.md` to avoid duplicating existing derivatives.

### 2. Create Derivatives (parallel where possible)
CEO agent delegates based on the content matrix. Common paths:

**Thread/Posts:**
**Agent:** @short-form-writer
**Skill:** thread, social-post
**Output:** `data/content/drafts/[slug]-thread.md`, `data/content/drafts/[slug]-posts.md`

**Newsletter Section:**
**Agent:** @long-form-writer
**Skill:** newsletter
**Output:** `data/content/drafts/[slug]-newsletter.md`

**Carousel:**
**Agent:** @visual-content-creator
**Skill:** carousel
**Output:** `data/content/drafts/[slug]-carousel.md`

**Video Script:**
**Agent:** @script-writer
**Skill:** video-script
**Output:** `data/content/drafts/[slug]-video.md`

### 3. Editorial Review
**Agent:** @content-editor
**Skill:** edit-review
**Input:** All derivatives from step 2
**Output:** Reviewed versions with feedback
**Notes:** Batch review — editor checks all derivatives in one pass.

### 4. Platform Adaptation
**Agent:** @platform-manager
**Skill:** platform-adapt
**Input:** Reviewed derivatives
**Output:** Platform-native versions (character limits, hashtags, formatting)

### 5. User Approval Gate
**CEO agent presents:** All derivatives in a summary view.
**User approves all, some, or requests changes.**

### 6. Schedule
**Agent:** @content-scheduler
**Skill:** content-calendar
**Input:** Approved derivatives
**Output:** Staggered schedule in `data/content/content-calendar.md`
**Notes:** Don't publish all at once — stagger across days/weeks for maximum reach.

## Data Flow
```
Source → data/content/drafts/[slug]-[format].md (one file per derivative)
data/content/content-calendar.md ← scheduling
data/content/content-matrix.md ← derivative tracking
```
