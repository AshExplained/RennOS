# RennOS — Brainstorm Scratchpad

> A company of AI agents whose sole purpose is to manage and improve your personal brand.

---

## Company Structure — 19 Departments (14 Professional + 5 Personal)

### 1. Strategy & Research
- **Purpose:** Brand positioning, audience analysis, competitive landscape, long-term roadmap
- **Potential Agents:**
  1. **Brand Strategist** — Owns core positioning: who you are, what you stand for, voice/tone, messaging pillars. The "north star" agent that other departments reference.
  2. **Audience Researcher** — Qualitative audience understanding. Builds personas, maps who the audience is, what they care about, where they hang out, what language they use. Answers: "who is our audience?"
  3. **Competitive Intel Analyst** — Monitors peers, competitors, and people in your space. Tracks what's working for them, gaps they're missing, and opportunities to differentiate.
  4. **Trend Scout** — Scans industry news, social trends, viral topics, and emerging narratives. Flags timely opportunities to insert your brand into relevant conversations.
  5. **Strategy Planner** — Turns insights from the other four agents into quarterly/monthly roadmaps: themes, campaigns, content pillars, and milestones.
- **Internal Workflow:**
  - Audience Researcher + Competitive Intel Analyst + Trend Scout → feed insights into Strategy Planner
  - Brand Strategist → acts as guardrail, every plan gets checked against brand positioning
  - Strategy Planner → outputs the roadmap that downstream departments (Content, Social, Marketing) execute on
- **Skill Files (14):**

  **Brand Strategist**
  1. `/strategy/brand-audit.md` — Analyze current brand presence and identify gaps
  2. `/strategy/brand-dna.md` — Create/update the brand guide (voice, tone, values, messaging pillars)
  3. `/strategy/brand-review.md` — Strategic brand alignment check: does this campaign/initiative fit our positioning, messaging pillars, and brand direction?

  **Audience Researcher**
  4. `/strategy/persona-builder.md` — Build and refine audience personas from data
  5. `/strategy/audience-analysis.md` — Analyze engagement data — what resonates, what flops
  6. `/strategy/audience-scan.md` — Discover where your audience hangs out, what they talk about

  **Competitive Intel Analyst**
  7. `/strategy/competitor-profile.md` — Deep-dive profile on a specific competitor/peer
  8. `/strategy/competitive-landscape.md` — Map the broader competitive landscape and positioning
  9. `/strategy/gap-analysis.md` — Identify gaps competitors are missing that you can own

  **Trend Scout**
  10. `/strategy/trend-scan.md` — Scan for trending topics, news, viral moments in your space
  11. `/strategy/opportunity-brief.md` — Package a trend into an actionable brief (what, why, how to jump in)

  **Strategy Planner**
  12. `/strategy/quarterly-roadmap.md` — Build a quarterly plan from all department inputs
  13. `/strategy/campaign-plan.md` — Design a specific campaign (theme, timeline, deliverables, KPIs)
  14. `/strategy/strategy-review.md` — Review progress against the roadmap, recommend adjustments

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 2. Content Creation
- **Purpose:** Writing, video production, graphic design, photography
- **Potential Agents:**
  1. **Long-Form Writer** — Blog posts, articles, newsletters, essays, deep dives
  2. **Short-Form Writer** — Social posts, threads, captions, hooks, one-liners
  3. **Script Writer** — Video scripts, podcast outlines, talking points, webinar prep
  4. **Visual Content Creator** — Graphics, carousels, infographics, thumbnails
  5. **Content Editor** — Quality control, proofreading, brand voice consistency check
  6. **Content Repurposer** — Transforms one piece of content into many formats (blog → thread → carousel → script)
- **Internal Workflow:**
  - Long-Form / Short-Form / Script Writer → produce drafts
  - Content Editor → reviews everything before publishing
  - Content Repurposer → takes top-performing or pillar content and multiplies it
  - Visual Content Creator → pairs visuals with any written content
  - All agents reference Brand DNA from Department 1
- **Skill Files (16):**

  **Long-Form Writer**
  1. `/content/blog-post.md` — Draft a blog post from topic or brief
  2. `/content/newsletter.md` — Write a newsletter edition
  3. `/content/article.md` — Write a long-form article or essay

  **Short-Form Writer**
  4. `/content/social-post.md` — Craft a single platform post
  5. `/content/thread.md` — Write a multi-part thread (X, LinkedIn, etc.)
  6. `/content/hooks.md` — Generate attention-grabbing opening lines/hooks

  **Script Writer**
  7. `/content/video-script.md` — Write a video script with structure and timing
  8. `/content/podcast-outline.md` — Create podcast episode outline and talking points
  9. `/content/talking-points.md` — Prep talking points for interviews, webinars, panels

  **Visual Content Creator**
  10. `/content/carousel.md` — Design slide-by-slide carousel content
  11. `/content/infographic.md` — Structure an infographic layout and copy
  12. `/content/thumbnail.md` — Generate thumbnail concepts and text overlays

  **Content Editor**
  13. `/content/edit-review.md` — Edit and polish any content piece for quality
  14. `/content/voice-check.md` — Tactical voice/tone check: does this content sound like us? Fix wording, tone, and style at the line level.

  **Content Repurposer**
  15. `/content/repurpose.md` — Take one content piece and transform it into multiple formats
  16. `/content/content-matrix.md` — Map out all derivative content from a single source piece

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 3. Social Media Management
- **Purpose:** Platform management, posting schedules, community engagement, DMs
- **Potential Agents:**
  1. **Platform Manager** — Adapts and manages content for each platform's format, culture, and best practices
  2. **Content Scheduler** — Timing optimization, content calendar management, posting cadence
  3. **Community Manager** — Replies, comments, DMs, relationship building, fostering conversations
  4. **Social Listener** — Monitors brand mentions, tags, sentiment, and relevant conversations
  5. **Engagement Strategist** — Growth tactics, hashtag strategy, engagement optimization
- **Internal Workflow:**
  - Content Scheduler → pulls from Strategy Planner's roadmap (Dept 1) and Content Creation output (Dept 2)
  - Platform Manager → adapts content per platform before scheduling
  - Community Manager + Social Listener → monitor and engage daily
  - Engagement Strategist → feeds growth insights back to Strategy & Research (Dept 1)
- **Skill Files (13):**

  **Platform Manager**
  1. `/social/platform-adapt.md` — Adapt content for a specific platform's format and culture
  2. `/social/post-publish.md` — Prepare and format a post for publishing
  3. `/social/platform-audit.md` — Audit presence and performance on a specific platform

  **Content Scheduler**
  4. `/social/content-calendar.md` — Build/update the weekly or monthly content calendar
  5. `/social/optimal-timing.md` — Analyze and recommend best posting times per platform

  **Community Manager**
  6. `/social/reply-draft.md` — Draft replies to comments and mentions
  7. `/social/dm-response.md` — Draft DM responses
  8. `/social/community-roundup.md` — Summarize community activity, sentiment, notable interactions

  **Social Listener**
  9. `/social/mention-scan.md` — Scan for brand mentions, tags, and relevant conversations
  10. `/social/sentiment-report.md` — Analyze sentiment around brand mentions

  **Engagement Strategist**
  11. `/social/growth-tactics.md` — Recommend engagement and growth strategies
  12. `/social/hashtag-strategy.md` — Research and recommend hashtag strategies
  13. `/social/engagement-playbook.md` — Create playbooks for different scenarios (viral moment, controversy, collaboration, etc.)

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 4. PR & Communications
- **Purpose:** Media outreach, press releases, interview prep, crisis management
- **Potential Agents:**
  1. **Media Outreach Specialist** — Pitching to journalists, bloggers, podcasters, building media lists
  2. **Press Release Writer** — Press releases, public statements, official messaging
  3. **Interview Prep Coach** — Preparing for interviews, media appearances, Q&A prep
  4. **Crisis Manager** — Handling negative press, controversies, reputation defense
  5. **PR Strategist** — Overall PR strategy, story angles, narrative building
- **Internal Workflow:**
  - PR Strategist → sets the narrative direction, informed by Brand Strategist (Dept 1)
  - Media Outreach Specialist → executes pitches based on PR Strategist's angles
  - Press Release Writer → drafts official comms, reviewed by Content Editor (Dept 2)
  - Interview Prep Coach → activates before any media appearance
  - Crisis Manager → on standby, triggered by Social Listener (Dept 3) or reputation threats
- **Skill Files (12):**

  **Media Outreach Specialist**
  1. `/pr/media-list.md` — Build/update a targeted media contact list
  2. `/pr/pitch-draft.md` — Draft a media pitch for a specific story/angle
  3. `/pr/outreach-tracker.md` — Track outreach status and follow-ups

  **Press Release Writer**
  4. `/pr/press-release.md` — Write a press release
  5. `/pr/media-statement.md` — Draft a public statement or response

  **Interview Prep Coach**
  6. `/pr/interview-prep.md` — Prepare talking points and Q&A for an interview
  7. `/pr/media-brief.md` — Create a brief on the interviewer/outlet and their audience

  **Crisis Manager**
  8. `/pr/crisis-response.md` — Draft a crisis response plan and messaging
  9. `/pr/reputation-scan.md` — Scan for reputation threats and negative coverage

  **PR Strategist**
  10. `/pr/pr-strategy.md` — Develop overall PR strategy and story angles
  11. `/pr/story-angle.md` — Identify compelling story angles from brand activities
  12. `/pr/pr-calendar.md` — Plan PR activities around key dates, launches, events

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 5. Digital Marketing & Growth
- **Purpose:** SEO, paid ads, email marketing, funnel optimization, analytics
- **Potential Agents:**
  1. **SEO Specialist** — Keyword research, on-page SEO, content optimization for search
  2. **Email Marketing Manager** — Email campaigns, sequences, list building, segmentation
  3. **Paid Ads Manager** — Ad copy, targeting, campaign design across paid platforms
  4. **Funnel Strategist** — Lead magnets, landing pages, conversion funnels, opt-in flows
  5. **Growth Hacker** — Experimentation, A/B testing, viral loops, unconventional growth tactics
- **Internal Workflow:**
  - SEO Specialist → works closely with Long-Form Writer (Dept 2) to optimize content for search
  - Email Marketing Manager → pulls content from Content Creation (Dept 2), follows Strategy Planner's roadmap (Dept 1)
  - Paid Ads Manager → amplifies top-performing organic content identified by Analytics (Dept 8)
  - Funnel Strategist → connects marketing efforts to conversion, works with Web & Tech (Dept 10)
  - Growth Hacker → runs experiments across all channels, feeds results back to Strategy & Research (Dept 1)
- **Skill Files (14):**

  **SEO Specialist**
  1. `/marketing/keyword-research.md` — Research and recommend target keywords
  2. `/marketing/seo-audit.md` — Audit content/site for SEO improvements
  3. `/marketing/seo-optimize.md` — Optimize a piece of content for search

  **Email Marketing Manager**
  4. `/marketing/email-campaign.md` — Design an email campaign (sequence, timing, copy)
  5. `/marketing/email-draft.md` — Write a single email
  6. `/marketing/list-strategy.md` — Plan list building and segmentation strategy

  **Paid Ads Manager**
  7. `/marketing/ad-copy.md` — Write ad copy for a specific platform
  8. `/marketing/ad-campaign.md` — Design an ad campaign (targeting, budget, creative brief)

  **Funnel Strategist**
  9. `/marketing/funnel-design.md` — Design a conversion funnel (lead magnet → nurture → offer)
  10. `/marketing/landing-page.md` — Write landing page copy and structure
  11. `/marketing/lead-magnet.md` — Ideate and outline a lead magnet

  **Growth Hacker**
  12. `/marketing/growth-experiments.md` — Propose growth experiments and A/B tests
  13. `/marketing/viral-loop.md` — Design referral/viral mechanics
  14. `/marketing/channel-analysis.md` — Analyze which channels are driving the most growth

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 6. Partnerships & Business Development
- **Purpose:** Sponsorship deals, collaborations, speaking engagements, licensing
- **Potential Agents:**
  1. **Partnership Scout** — Identifies potential collaboration partners, brands, creators
  2. **Deal Negotiator** — Structures deals, terms, pricing, deliverables
  3. **Sponsorship Manager** — Manages inbound/outbound sponsorship opportunities, media kit
  4. **Speaking & Events Manager** — Secures speaking gigs, panels, conferences, event appearances
  5. **Licensing & IP Manager** — Licensing deals, digital products, IP monetization
- **Internal Workflow:**
  - Partnership Scout → uses Audience Researcher (Dept 1) data to find high-fit partners
  - Deal Negotiator → works with Legal & Compliance (Dept 9) on terms
  - Sponsorship Manager → coordinates with Brand Strategist (Dept 1) to ensure brand alignment
  - Speaking & Events Manager → triggers Interview Prep Coach (Dept 4) before appearances
  - Licensing & IP Manager → works with Funnel Strategist (Dept 5) to monetize digital products
- **Skill Files (12):**

  **Partnership Scout**
  1. `/partnerships/partner-research.md` — Research and identify potential collaboration partners
  2. `/partnerships/partner-brief.md` — Create a brief on a potential partner (audience overlap, brand fit, reach)
  3. `/partnerships/outreach-draft.md` — Draft partnership outreach message

  **Deal Negotiator**
  4. `/partnerships/deal-structure.md` — Structure a deal (terms, deliverables, pricing, timeline)
  5. `/partnerships/proposal-draft.md` — Write a partnership/sponsorship proposal

  **Sponsorship Manager**
  6. `/partnerships/sponsorship-eval.md` — Evaluate an inbound sponsorship opportunity (brand fit, value, audience alignment)
  7. `/partnerships/sponsor-pitch.md` — Create an outbound sponsorship pitch doc
  8. `/partnerships/media-kit.md` — Create/update the brand media kit

  **Speaking & Events Manager**
  9. `/partnerships/speaking-pitch.md` — Pitch for a speaking slot at an event/conference
  10. `/partnerships/event-brief.md` — Prep brief for an upcoming event (audience, key contacts, goals)

  **Licensing & IP Manager**
  11. `/partnerships/licensing-eval.md` — Evaluate a licensing opportunity
  12. `/partnerships/monetization-ideas.md` — Brainstorm IP monetization opportunities (courses, templates, digital products)

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 7. Operations & Project Management
- **Purpose:** Scheduling, coordination across departments, budgets, vendor management
- **Potential Agents:**
  1. **Project Coordinator** — Tracks tasks, deadlines, deliverables across all departments

  2. **Resource Manager** — Operational spend tracking. Monitors tool costs, vendor invoices, contractor payments. Answers: "are we within budget on this project?"
  3. **Schedule Manager** — Master calendar, coordinates timelines, prevents conflicts
  4. **Quality Assurance** — Ensures all outputs meet standards before they go live
- **Internal Workflow:**
  - Project Coordinator → central hub, receives inputs from all departments and tracks delivery
  - Resource Manager → tracks spend across Paid Ads (Dept 5), vendor tools, sponsorships
  - Schedule Manager → syncs Content Calendar (Dept 3), PR Calendar (Dept 4), and campaign timelines
  - Quality Assurance → final gate before any content, campaign, or outreach goes live
- **Skill Files (9):**

  **Project Coordinator**
  1. `/ops/task-tracker.md` — Create/update task lists and track progress across departments
  2. `/ops/status-report.md` — Generate a status report across all active projects
  3. `/ops/deadline-check.md` — Check upcoming deadlines and flag at-risk items

  **Resource Manager**
  4. `/ops/budget-tracker.md` — Track spending and budget allocation
  5. `/ops/vendor-eval.md` — Evaluate and compare vendors/tools/services

  **Schedule Manager**
  6. `/ops/master-calendar.md` — Maintain the master calendar across all departments
  7. `/ops/conflict-check.md` — Check for scheduling conflicts and resource overlaps

  **Quality Assurance**
  8. `/ops/qa-checklist.md` — Run a quality checklist on any deliverable before it goes live
  9. `/ops/post-mortem.md` — Run a post-mortem on a completed campaign or project

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 8. Analytics & Reporting
- **Purpose:** Performance tracking, ROI measurement, audience insights, data-driven recommendations
- **Potential Agents:**
  1. **Performance Analyst** — Tracks KPIs across all channels — followers, engagement, reach, impressions
  2. **Content Analyst** — Analyzes which content performs best and why
  3. **Audience Insights Analyst** — Quantitative audience analysis. Reads the numbers — demographics, growth rates, engagement metrics, platform analytics. Answers: "what are the numbers saying?"
  4. **ROI Analyst** — Measures return on investment across campaigns, sponsorships, paid ads
  5. **Report Builder** — Compiles data into digestible reports and summaries
- **Internal Workflow:**
  - Performance Analyst → feeds data to every department for informed decision-making
  - Content Analyst → informs Content Creation (Dept 2) and Content Repurposer on what to double down on
  - Audience Insights Analyst → feeds into Audience Researcher (Dept 1) to refine personas
  - ROI Analyst → informs Paid Ads Manager (Dept 5) and Resource Manager (Dept 7) on spend efficiency
  - Report Builder → delivers regular reports to you (the human) for oversight and decisions
- **Skill Files (12):**

  **Performance Analyst**
  1. `/analytics/kpi-dashboard.md` — Generate a KPI snapshot across all channels
  2. `/analytics/performance-report.md` — Detailed performance report for a specific time period
  3. `/analytics/benchmark.md` — Benchmark current metrics against past performance or industry standards

  **Content Analyst**
  4. `/analytics/content-performance.md` — Analyze which content pieces performed best and why
  5. `/analytics/content-recommendations.md` — Recommend content types/topics based on performance data

  **Audience Insights Analyst**
  6. `/analytics/audience-report.md` — Deep dive into audience demographics and behavior
  7. `/analytics/growth-report.md` — Track and analyze audience growth patterns

  **ROI Analyst**
  8. `/analytics/campaign-roi.md` — Measure ROI on a specific campaign
  9. `/analytics/channel-roi.md` — Compare ROI across channels (organic, paid, email, etc.)

  **Report Builder**
  10. `/analytics/weekly-digest.md` — Compile a weekly digest of key metrics and highlights
  11. `/analytics/executive-summary.md` — Create an executive summary for personal review
  12. `/analytics/custom-report.md` — Build a custom report based on specific questions or data points

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 9. Legal & Compliance
- **Purpose:** Contracts, IP protection, FTC disclosure compliance
- **Potential Agents:**
  1. **Contract Reviewer** — Reviews contracts, agreements, flags risks and red flags
  2. **Compliance Monitor** — Ensures FTC disclosure, platform ToS, GDPR, CAN-SPAM compliance
  3. **IP Protector** — Trademark, copyright, protecting your content and digital products
  4. **Privacy Advisor** — Data collection policies, privacy policies, cookie compliance
- **Internal Workflow:**
  - Contract Reviewer → triggered by Deal Negotiator (Dept 6) before any deal is signed
  - Compliance Monitor → triggered by Content Editor (Dept 2) and Sponsorship Manager (Dept 6) for sponsored content
  - IP Protector → triggered by Social Listener (Dept 3) spotting unauthorized use, or before publishing original IP
  - Privacy Advisor → triggered by Email Marketing Manager (Dept 5) and Web & Tech (Dept 10) when handling user data
- **Skill Files (11):**

  **Contract Reviewer**
  1. `/legal/contract-review.md` — Review a contract and flag risks, missing terms, red flags
  2. `/legal/contract-draft.md` — Draft a basic contract or agreement
  3. `/legal/terms-summary.md` — Summarize key terms of a deal in plain language

  **Compliance Monitor**
  4. `/legal/disclosure-check.md` — Check content for proper FTC disclosures
  5. `/legal/platform-compliance.md` — Verify content meets platform ToS requirements
  6. `/legal/compliance-audit.md` — Audit current practices against regulations (GDPR, CAN-SPAM, etc.)

  **IP Protector**
  7. `/legal/ip-scan.md` — Scan for unauthorized use of your content/brand
  8. `/legal/trademark-guide.md` — Guide on protecting your brand name, logos, catchphrases
  9. `/legal/content-rights.md` — Check if you can legally use specific content (images, music, quotes)

  **Privacy Advisor**
  10. `/legal/privacy-policy.md` — Draft/update privacy policy for website or app
  11. `/legal/data-audit.md` — Audit what data you're collecting and how it's stored

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 10. Web & Tech
- **Purpose:** Website management, app development, tooling/automation
- **Potential Agents:**
  1. **Web Developer** — Website management, updates, new pages, landing pages
  2. **Automation Engineer** — Designs and builds automations, workflows between tools, platforms, and departments
  3. **Tech Stack Manager** — Evaluates, maintains, and recommends tools and platforms
  4. **Performance Optimizer** — Site speed, uptime, technical SEO, mobile optimization
  5. **Security Specialist** — Website security, vulnerability audits, backups
- **Internal Workflow:**
  - Web Developer → executes landing pages from Funnel Strategist (Dept 5) and site updates
  - Automation Engineer → designs and builds workflows across departments and tools
  - Tech Stack Manager → advises Resource Manager (Dept 7) on tool spend and consolidation
  - Performance Optimizer → works with SEO Specialist (Dept 5) on technical SEO
  - Security Specialist → coordinates with Privacy Advisor (Dept 9) on data protection
- **Skill Files (14):**

  **Web Developer**
  1. `/tech/site-update.md` — Make updates to the website (new pages, edits, design tweaks)
  2. `/tech/landing-page-build.md` — Build a landing page from copy and design specs
  3. `/tech/site-audit.md` — Audit the website for issues (broken links, UX, mobile, speed)

  **Automation Engineer**
  4. `/tech/automation-build.md` — Build an automation workflow between tools/platforms
  5. `/tech/integration-setup.md` — Set up a new integration between platforms
  6. `/tech/automation-audit.md` — Audit existing automations for reliability and efficiency
  7. `/tech/workflow-design.md` — Design an automated workflow between departments
  8. `/tech/process-audit.md` — Audit existing processes for bottlenecks and inefficiencies

  **Tech Stack Manager**
  9. `/tech/tool-eval.md` — Evaluate a new tool or platform for the stack
  10. `/tech/stack-review.md` — Review the current tech stack and recommend changes

  **Performance Optimizer**
  11. `/tech/speed-audit.md` — Audit site speed and recommend optimizations
  12. `/tech/uptime-monitor.md` — Set up or check uptime/health monitoring

  **Security Specialist**
  13. `/tech/security-audit.md` — Audit website/tools for security vulnerabilities
  14. `/tech/backup-plan.md` — Create/review backup and recovery plan

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 11. Finance
- **Purpose:** Revenue growth, income tracking, pricing, forecasting, invoicing
- **Potential Agents:**
  1. **Revenue Strategist** — Sets revenue goals, identifies income streams, plans monetization strategy
  2. **Income Tracker** — Tracks all revenue across streams (sponsorships, courses, consulting, ads, etc.)
  3. **Pricing Strategist** — Optimizes pricing for products, services, sponsorship rates
  4. **Financial Planner** — Strategic money planning. Revenue forecasting, cash flow, budget allocation across the business. Answers: "how should we allocate money next quarter?"
  5. **Invoice & Payments Manager** — Invoicing, payment tracking, follow-ups on outstanding payments
- **Internal Workflow:**
  - Revenue Strategist → works with Strategy Planner (Dept 1) to align brand growth with revenue goals
  - Income Tracker → pulls data from Sponsorship Manager (Dept 6), Licensing & IP Manager (Dept 6), Paid Ads (Dept 5)
  - Pricing Strategist → informs Deal Negotiator (Dept 6) and Sponsorship Manager (Dept 6) on rates
  - Financial Planner → feeds into Resource Manager (Dept 7) for budget allocation
  - Invoice & Payments Manager → triggered after Deal Negotiator (Dept 6) closes a deal
- **Skill Files (13):**

  **Revenue Strategist**
  1. `/finance/revenue-strategy.md` — Define revenue goals and income stream strategy
  2. `/finance/income-streams.md` — Map and evaluate all current/potential income streams
  3. `/finance/monetization-plan.md` — Create a monetization plan for a specific asset (audience, content, IP)

  **Income Tracker**
  4. `/finance/revenue-dashboard.md` — Generate a revenue snapshot across all income streams
  5. `/finance/income-report.md` — Detailed income report for a specific time period
  6. `/finance/revenue-trends.md` — Analyze revenue trends and flag changes

  **Pricing Strategist**
  7. `/finance/pricing-analysis.md` — Analyze and recommend pricing for a product or service
  8. `/finance/rate-card.md` — Create/update rate card for sponsorships, consulting, speaking

  **Financial Planner**
  9. `/finance/forecast.md` — Revenue forecast for upcoming quarter/year
  10. `/finance/budget-plan.md` — Create a budget plan aligned with revenue goals
  11. `/finance/cashflow-check.md` — Analyze cash flow and flag potential issues

  **Invoice & Payments Manager**
  12. `/finance/invoice-draft.md` — Draft an invoice
  13. `/finance/payment-tracker.md` — Track outstanding payments and follow-ups

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 12. Product
- **Purpose:** Product ideation, validation, design, launch, and iteration
- **Potential Agents:**
  1. **Product Strategist** — Product ideation, validation, product-market fit
  2. **Product Designer** — Structures the product (course curriculum, community architecture, SaaS features)
  3. **Launch Manager** — Coordinates cross-department product launches
  4. **Product Feedback Analyst** — Collects and synthesizes user feedback into actionable improvements
  5. **Beta Coordinator** — Manages beta testing, early access programs, user testing
- **Internal Workflow:**
  - Product Strategist → uses Audience Researcher (Dept 1) + Revenue Strategist (Dept 11) to decide what to build
  - Product Designer → hands specs to Web Developer (Dept 10) and Long-Form Writer (Dept 2) for execution
  - Launch Manager → orchestrates Content (Dept 2), Social (Dept 3), PR (Dept 4), Marketing (Dept 5) for launch
  - Product Feedback Analyst → receives input from Customer Success (Dept 13), feeds into Product Designer for iteration
  - Beta Coordinator → works with Community Manager (Dept 3) and Email Marketing (Dept 5) to recruit and manage testers
- **Skill Files (13):**

  **Product Strategist**
  1. `/product/product-ideation.md` — Brainstorm and validate product ideas based on audience data
  2. `/product/market-validation.md` — Validate product-market fit before building
  3. `/product/product-roadmap.md` — Create/update the product roadmap

  **Product Designer**
  4. `/product/course-design.md` — Design course curriculum (modules, lessons, outcomes)
  5. `/product/community-design.md` — Design a paid community structure (tiers, content, engagement)
  6. `/product/product-spec.md` — Write a product spec/brief for any digital product

  **Launch Manager**
  7. `/product/launch-plan.md` — Create a full product launch plan (timeline, channels, departments involved)
  8. `/product/launch-checklist.md` — Pre-launch checklist to ensure everything is ready
  9. `/product/post-launch-review.md` — Post-launch analysis and learnings

  **Product Feedback Analyst**
  10. `/product/feedback-synthesis.md` — Collect and synthesize customer feedback into themes
  11. `/product/improvement-plan.md` — Turn feedback into a prioritized improvement plan

  **Beta Coordinator**
  12. `/product/beta-plan.md` — Design a beta testing program (who, what, how, timeline)
  13. `/product/beta-report.md` — Compile beta testing results and recommendations

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 13. Customer Success
- **Purpose:** Customer onboarding, support, retention, community, and feedback
- **Potential Agents:**
  1. **Onboarding Specialist** — Designs and manages customer onboarding experiences
  2. **Support Agent** — Handles customer questions, troubleshooting, help desk
  3. **Retention Strategist** — Churn prevention, win-back campaigns, renewal strategies
  4. **Community Host** — Manages paid communities (different from social media community)
  5. **Feedback Collector** — Gathers customer feedback, reviews, testimonials
- **Internal Workflow:**
  - Onboarding Specialist → triggered after a sale, works with Email Marketing (Dept 5) for sequences
  - Support Agent → first line of response, escalates to relevant departments as needed
  - Retention Strategist → uses Analytics (Dept 8) to identify at-risk customers, triggers win-back via Email (Dept 5)
  - Community Host → coordinates with Content Creation (Dept 2) for community-exclusive content
  - Feedback Collector → feeds directly into Product Feedback Analyst (Dept 12) to close the loop
- **Skill Files (14):**

  **Onboarding Specialist**
  1. `/success/onboarding-design.md` — Design an onboarding flow for a product
  2. `/success/welcome-sequence.md` — Create a welcome email/message sequence
  3. `/success/onboarding-audit.md` — Audit existing onboarding for drop-off points

  **Support Agent**
  4. `/success/support-response.md` — Draft a response to a customer question or issue
  5. `/success/faq-builder.md` — Create/update FAQ and knowledge base
  6. `/success/escalation-plan.md` — Define escalation paths for complex issues

  **Retention Strategist**
  7. `/success/churn-analysis.md` — Analyze churn patterns and identify at-risk customers
  8. `/success/winback-campaign.md` — Design a win-back campaign for churned customers
  9. `/success/upsell-plan.md` — Identify and plan upsell/cross-sell opportunities

  **Community Host**
  10. `/success/community-plan.md` — Plan and structure a paid community experience
  11. `/success/engagement-calendar.md` — Create an engagement calendar for the community (events, AMAs, challenges)

  **Feedback Collector**
  12. `/success/feedback-survey.md` — Design a customer feedback survey
  13. `/success/testimonial-request.md` — Draft testimonial/review request outreach
  14. `/success/feedback-report.md` — Compile customer feedback into a report for Product (Dept 12)

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 14. UI/UX Design
- **Purpose:** Visual design, user experience, brand visual system, templates
- **Potential Agents:**
  1. **UX Designer** — User flows, wireframes, usability, information architecture
  2. **Visual Designer** — Brand visual system — colors, typography, imagery style
  3. **Landing Page Designer** — Conversion-focused landing page layouts and design
  4. **Email Template Designer** — Email template design, layout, mobile responsiveness
  5. **Presentation Designer** — Decks, pitch presentations, keynote slides
- **Internal Workflow:**
  - Visual Designer → defines the visual system that all other design agents follow, extends Brand DNA (Dept 1)
  - UX Designer → works with Product Designer (Dept 12) on product experience, Web Developer (Dept 10) on implementation
  - Landing Page Designer → pairs with Funnel Strategist (Dept 5) for copy + Web Developer (Dept 10) for build
  - Email Template Designer → pairs with Email Marketing Manager (Dept 5) for consistent email visuals
  - Presentation Designer → supports Speaking & Events Manager (Dept 6) and Sponsor Pitch (Dept 6)
- **Skill Files (12):**

  **UX Designer**
  1. `/design/user-flow.md` — Design a user flow for a product or page
  2. `/design/wireframe.md` — Create wireframe specs for a page or feature
  3. `/design/ux-audit.md` — Audit an existing page/product for UX issues

  **Visual Designer**
  4. `/design/visual-identity.md` — Define/update brand visual system (colors, typography, imagery)
  5. `/design/style-guide.md` — Create a visual style guide for consistency across platforms
  6. `/design/asset-brief.md` — Create a brief for visual assets (photos, illustrations, icons)

  **Landing Page Designer**
  7. `/design/landing-layout.md` — Design a landing page layout (sections, hierarchy, CTA placement)
  8. `/design/conversion-review.md` — Review a landing page for conversion optimization

  **Email Template Designer**
  9. `/design/email-template.md` — Design an email template layout
  10. `/design/email-audit.md` — Audit email templates for visual consistency and mobile responsiveness

  **Presentation Designer**
  11. `/design/deck-design.md` — Design a presentation/pitch deck structure and visuals
  12. `/design/slide-template.md` — Create reusable slide templates

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

## Implementation Architecture

### UX Flow
```
Ash
 └→ Tony (CEO)
      ├→ C-Suite agents (Tony's direct tools)
      └→ 19 Departments (14 professional + 5 personal)

Ash → /wake-up → Tony (CEO) → natural conversation
Tony delegates → @agent-name → agent uses skill playbooks → returns result to Tony → Tony reports to Ash
```

- Ash only types `/wake-up` and talks naturally
- Tony (CEO, defined in CLAUDE.md) is the sole interface and router
- Tony delegates to 91 agents via @-mentions (2 C-Suite + 89 department agents)
- Agents execute tasks using 223 skill playbooks (not user-facing)
- All context compounds over time via persistent memory

### C-Suite — Tony's Direct Agents
Not part of any department. Executive-level agents that help Tony do his job.

| # | Agent | Role |
|---|-------|------|
| 1 | **Knowledge Manager** | Processes web clippings from vault/inbox/, categorizes, tags with frontmatter, files into the right folder across vault/ and data/ |
| 2 | **Executive Researcher** | Deep research on anything Ash asks that doesn't fit a specific department. Web research, competitive deep dives, market analysis, due diligence. |

**Future C-Suite agents (add when needed):**
- **Chief of Staff** — preps wake-up briefings, summarizes long threads, manages Tony's context

**Knowledge Manager workflow:**
```
Ash: "Process my clippings"
Tony → @knowledge-manager
  → Reads all files in vault/inbox/
  → For each clipping:
    1. Reads content, understands topic
    2. Adds frontmatter tags:
       ---
       tags: [branding, linkedin]
       source: https://example.com
       clipped: 2026-03-18
       ---
    3. Moves to relevant folder:
       Health article      → vault/personal/health/
       Branding tip        → vault/professional/notes/
       Competitor intel    → data/strategy/references/
       Product idea        → vault/professional/ideas/
  → Reports summary to Tony: "5 clippings processed — 2 professional, 2 personal, 1 moved to company data"
```

**Tony on wake-up:** "You have 5 unprocessed clippings in your inbox. Want me to process them?"

### Orchestration Modes
Tony picks the right mode based on task complexity:

**Mode 1: Subagent Delegation (default — simple tasks)**
- Tony spawns a single agent via @-mention
- Agent does its work, returns result to Tony
- Tony reports back to Ash
- Best for: single-department tasks (write a blog post, run a brand audit)
```
Ash → Tony → @long-form-writer → result → Tony → Ash
```

**Mode 2: Subagent Chaining (multi-step tasks)**
- Tony spawns agents sequentially, passing context between them
- Each agent writes output to `data/`, Tony routes the next agent to read from there
- Tony orchestrates every handoff
- Best for: tasks needing 2-3 agents in sequence (write post → edit → voice check)
```
Ash → Tony → @long-form-writer (writes to data/) → Tony → @content-editor (reads from data/) → Tony → Ash
```

**Mode 3: Agent Teams (complex multi-department tasks)**
- Tony acts as team lead, spawns department agents as teammates
- Teammates can message each other directly (peer-to-peer)
- Each teammate has its own independent context window
- Best for: product launches, quarterly planning, campaigns spanning 3+ departments
```
Ash → Tony (team lead)
        ├→ @content-editor ←→ @brand-strategist (direct peer communication)
        ├→ @social-scheduler ←→ @platform-manager
        └→ Tony synthesizes and reports to Ash
```

**When to use which:**
| Complexity | Example | Mode |
|-----------|---------|------|
| Single agent | "Write me a LinkedIn post" | Mode 1: Subagent |
| 2-3 agents in sequence | "Write and edit a blog post" | Mode 2: Chaining |
| 3+ departments in parallel | "Launch the new course" | Mode 3: Agent Teams |

> Note: Agent Teams is experimental (since Feb 2026). Enabled via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings.

### `/wake-up` — First Run (Bootstrap / Onboarding)
When Tony detects empty `data/` files, he runs onboarding instead of daily briefing.

**Tony interviews Ash:**
1. "Tell me about yourself — who are you, what do you do?"
2. "Who is your target audience?"
3. "What platforms are you active on?"
4. "What are your goals for the next 3 months?"
5. "Who are your competitors/peers in this space?"
6. "Any existing content, website, or brand assets?"

**Tony delegates to populate initial data:**
- @brand-strategist → creates `data/brand/brand-dna.md`
- @audience-researcher → creates `data/strategy/audience-personas.md`
- @strategy-planner → creates `data/strategy/quarterly-roadmap.md`
- @competitive-intel-analyst → creates `data/strategy/competitive-landscape.md`
- Tony → saves Ash's profile to `ceo-memory/user_ash.md`

After bootstrap, all future `/wake-up` runs the normal daily briefing below.

### `/wake-up` Boot Sequence (Cold Start)
Every session is a cold start. Tony's brain is empty until he reads his memory.

**Auto-loaded (free):**
- `CLAUDE.md` — Tony's identity and company structure
- `ceo-memory/` files — Tony reads these explicitly on wake-up (auto-memory disabled)

**Step 1: Reload Tony's brain**
```
→ ceo-memory/user_ash.md          # Who Ash is, preferences, goals
→ ceo-memory/feedback.md          # What to do / not do
→ ceo-memory/active_projects.md   # What's in motion right now
→ ceo-memory/decisions.md         # Key decisions made over time
```

**Step 2: Read company pulse**
```
→ data/operations/master-calendar.md    # What's scheduled
→ data/operations/decision-log.md       # Recent decisions
→ data/strategy/quarterly-roadmap.md    # Current roadmap
→ data/content/content-calendar.md      # What content is planned
→ data/analytics/kpi-dashboard.md       # Latest metrics
→ data/finance/revenue-dashboard.md     # Revenue status
```

**Step 2.5: Read Tony's inbox (overnight reports from scheduled tasks)**
```
→ data/inbox/*.md                       # All reports dropped by scheduled tasks
```

**Step 3: Synthesize and brief Ash**
- Overnight highlights (from inbox)
- What's in motion
- What needs attention / is overdue
- Key metrics snapshot
- "What do you want to focus on today?"

**Step 4: Archive processed inbox**
- Move processed inbox files to `data/archive/` so they don't pile up

**What Tony does NOT read on wake-up:**
- 70 individual agent memories (only loaded when delegating to that agent)
- Deep data files (personas, competitive landscape — only when relevant)

### Model Tier Strategy
Not every agent needs Opus. Assign model based on task complexity.

| Tier | Model | When to Use | Example Agents |
|------|-------|-------------|----------------|
| **Tier 1: Opus** | Deep thinking, strategy, creative writing | Brand Strategist, Strategy Planner, PR Strategist, Product Strategist, Long-Form Writer, Crisis Manager, Revenue Strategist, UX Designer, Deal Negotiator, Growth Hacker, Investment Advisor |
| **Tier 2: Sonnet** | Most tasks — solid reasoning + execution | Content Editor, Short-Form Writer, Script Writer, SEO Specialist, Email Marketing Manager, Competitive Intel Analyst, Audience Researcher, Fitness Coach, Nutrition Advisor, Mental Health Guide, Network Manager, Learning Coach, Mindset Coach, Budget Manager, most agents |
| **Tier 3: Haiku** | Simple lookups, formatting, tracking | Income Tracker, Content Scheduler, Report Builder, Invoice & Payments Manager, Schedule Manager, Habit Tracker, Expense Tracker, Subscription Manager, Task Manager |

- ~11 agents on Opus, ~61 on Sonnet, ~19 on Haiku
- Start low, upgrade if output quality isn't good enough
- Tony (CEO) always runs on Opus (he's the main session)

### Approval Gate — Draft vs. Publish

**Rule: Agents NEVER take external actions. They always produce drafts.**

| Action Type | Approval | Examples |
|------------|----------|---------|
| **Draft** (no approval) | Agent writes to `data/` | Writing content, analysis, reports, plans, strategies |
| **Publish** (Ash approves) | Tony presents draft → Ash says go | Posting to social, sending emails/DMs, outreach, invoicing, purchases |

**Flow for external actions:**
```
Agent produces draft → writes to data/ → Tony presents to Ash → Ash approves → execute
```

**Enforced via:**
1. Every agent file includes: "You NEVER publish, send, or execute externally. You produce drafts only."
2. Hook (PreToolUse) blocks external MCP calls unless explicitly approved
3. Tony always confirms with Ash before any external action

### Scheduled Tasks (Claude Desktop Scheduler)
Runs overnight/recurring work while Ash is away. Tasks dump reports to `data/inbox/` for Tony to read on wake-up.

**Requires:** Claude Desktop app open + computer awake.

| Schedule | Task | Agent | Output |
|----------|------|-------|--------|
| Daily 8:00am | Trend scan | Trend Scout | `data/inbox/trend-scan-YYYY-MM-DD.md` |
| Daily 8:15am | Social mention scan | Social Listener | `data/inbox/mention-scan-YYYY-MM-DD.md` |
| Daily 8:30am | Daily metrics | Performance Analyst | `data/inbox/daily-metrics-YYYY-MM-DD.md` |
| Weekly Monday 8am | Content calendar review | Content Scheduler | `data/inbox/content-review-YYYY-MM-DD.md` |
| Weekly Friday 5pm | Weekly performance digest | Report Builder | `data/inbox/weekly-digest-YYYY-MM-DD.md` |
| Monthly 1st 8am | Revenue report | Income Tracker | `data/inbox/revenue-report-YYYY-MM.md` |
| Quarterly | Strategy review prep | Strategy Planner | `data/inbox/quarterly-review-YYYY-QN.md` |

**In-session polling:** Use `/loop` for live monitoring (e.g., `/loop 30m check post engagement`). Session-scoped, dies when session ends.

**Task prompts stored at:** `~/.claude/scheduled-tasks/<task-name>/SKILL.md`

### Layer Model
| Layer | What | Who Uses It | Purpose |
|-------|------|-------------|---------|
| CLAUDE.md | Tony (CEO) | Ash talks to Tony | Orchestration, delegation |
| `/wake-up` | Daily activation skill | Ash invokes once | Start the day, get pulse |
| 91 agent files | Agent personas + capabilities (2 C-Suite + 89 department) | Tony delegates to them | Who they are, what tools/memory they have |
| 223 skill files | Playbooks/SOPs (not user-facing) | Agents execute with these | How to do tasks well, step-by-step |
| ceo-memory/ | Tony's persistent memory | Tony reads/writes | Company-wide context, Ash's preferences |
| agent-memory/ | Individual agent memory | Each agent reads/writes own | Compound learning per agent |
| data/ | Shared knowledge base | All agents read/write | Company state, living documents |
| data/inbox/ | Scheduled task reports | Scheduled tasks write, Tony reads | Overnight reports for morning briefing |
| Desktop Scheduler | Recurring automated tasks | Runs independently | Trend scans, metrics, digests |

### Folder Structure
```
RennOS/
├── CLAUDE.md                              # Tony (CEO) — always loaded
├── brainstorm.md                          # Planning scratchpad
├── claude-code-meta.md                    # Claude Code feature reference
├── .mcp.json                              # MCP server config
│
├── .claude/
│   ├── settings.json                      # Permissions, hooks, env vars
│   │
│   ├── ceo-memory/                        # Tony's persistent memory (portable)
│   │   ├── MEMORY.md                      # Index (loaded every session)
│   │   ├── user_ash.md                    # Ash's preferences, goals, style
│   │   ├── feedback.md                    # Corrections, what works/doesn't
│   │   ├── active_projects.md             # What's in motion right now
│   │   └── decisions.md                   # Key decisions + rationale
│   │
│   ├── agent-memory/                      # All agents' persistent memory
│   │   ├── knowledge-manager/MEMORY.md    # C-Suite
│   │   ├── executive-researcher/MEMORY.md # C-Suite
│   │   ├── brand-strategist/MEMORY.md
│   │   ├── long-form-writer/MEMORY.md
│   │   ├── content-analyst/MEMORY.md
│   │   └── ... (one per agent)
│   │
│   ├── agents/                            # C-Suite (2) + Department agents (69)
│   │   │
│   │   │  # C-Suite — Tony's direct agents
│   │   ├── knowledge-manager.md
│   │   ├── executive-researcher.md
│   │   │
│   │   │  # Department agents
│   │   ├── brand-strategist.md            # skills: [brand-audit, brand-dna, brand-review]
│   │   ├── audience-researcher.md         # skills: [persona-builder, audience-analysis, audience-scan]
│   │   ├── long-form-writer.md            # skills: [blog-post, newsletter, article]
│   │   └── ... (89 department agents)
│   │
│   └── skills/                            # 1 user-facing + 223 agent playbooks
│       ├── wake-up/SKILL.md               # Only user-facing skill
│       ├── strategy/                      # Dept 1: 14 playbooks
│       │   ├── brand-audit/SKILL.md       #   user-invocable: false
│       │   ├── brand-dna/SKILL.md
│       │   └── ...
│       ├── content/                       # Dept 2: 16 playbooks
│       ├── social/                        # Dept 3: 13 playbooks
│       ├── pr/                            # Dept 4: 12 playbooks
│       ├── marketing/                     # Dept 5: 14 playbooks
│       ├── partnerships/                  # Dept 6: 12 playbooks
│       ├── ops/                           # Dept 7: 9 playbooks
│       ├── analytics/                     # Dept 8: 12 playbooks
│       ├── legal/                         # Dept 9: 11 playbooks
│       ├── tech/                          # Dept 10: 14 playbooks
│       ├── finance/                       # Dept 11: 13 playbooks
│       ├── product/                       # Dept 12: 13 playbooks
│       ├── success/                       # Dept 13: 14 playbooks
│       ├── design/                        # Dept 14: 12 playbooks
│       ├── health/                        # Dept 15: 9 playbooks
│       ├── relationships/                 # Dept 16: 9 playbooks
│       ├── growth/                        # Dept 17: 9 playbooks
│       ├── admin/                         # Dept 18: 9 playbooks
│       └── personal-finance/              # Dept 19: 8 playbooks
│
├── vault/                                 # Second brain (Obsidian vault)
│   ├── inbox/                             # Web clipper dumps here (raw, unprocessed)
│   ├── personal/
│   │   ├── health/
│   │   ├── relationships/
│   │   ├── goals/
│   │   └── journal/
│   ├── professional/
│   │   ├── notes/
│   │   ├── learnings/
│   │   └── ideas/
│   └── resources/                         # Reference material, bookmarks, guides
│
├── templates/                             # Obsidian templates
│   ├── clipping.md
│   ├── meeting-note.md
│   └── daily-note.md
│
└── data/                                  # Shared company knowledge base
    │
    │  # Professional departments
    ├── brand/                             # Dept 1
    │   ├── brand-dna.md                   # Core brand identity (evolves)
    │   ├── visual-identity.md             # Visual system
    │   └── style-guide.md                 # Design guidelines
    ├── strategy/                          # Dept 1
    │   ├── quarterly-roadmap.md           # Current roadmap
    │   ├── audience-personas.md           # Audience personas (refined over time)
    │   └── competitive-landscape.md       # Competitor map
    ├── content/                           # Dept 2
    │   ├── content-calendar.md            # Posting schedule
    │   ├── content-matrix.md              # Repurpose tracking
    │   └── top-performers.md              # Best performing content
    ├── social/                            # Dept 3
    │   └── ...
    ├── pr/                                # Dept 4
    │   └── ...
    ├── marketing/                         # Dept 5
    │   └── ...
    ├── partnerships/                      # Dept 6
    │   └── ...
    ├── operations/                        # Dept 7
    │   ├── master-calendar.md             # Cross-department schedule
    │   └── decision-log.md                # Key company decisions + rationale
    ├── analytics/                         # Dept 8
    │   ├── kpi-dashboard.md               # Key metrics
    │   ├── benchmarks.md                  # Historical benchmarks
    │   └── insights-log.md                # Running log of key findings
    ├── legal/                             # Dept 9
    │   └── ...
    ├── tech/                              # Dept 10
    │   └── ...
    ├── finance/                           # Dept 11
    │   ├── revenue-dashboard.md           # Revenue tracking
    │   ├── rate-card.md                   # Pricing rates
    │   └── revenue-history.md             # Historical tracking
    ├── product/                           # Dept 12
    │   ├── product-roadmap.md             # Product plans
    │   └── feedback-themes.md             # Aggregated customer feedback
    ├── customers/                         # Dept 13
    │   ├── testimonials.md                # Collected over time
    │   └── churn-insights.md              # Why people leave
    ├── design/                            # Dept 14
    │   └── ...
    │
    │  # Personal departments
    ├── personal/
    │   ├── health/                        # Dept 15
    │   │   └── ...
    │   ├── relationships/                 # Dept 16
    │   │   └── ...
    │   ├── growth/                        # Dept 17
    │   │   └── ...
    │   ├── admin/                         # Dept 18
    │   │   └── ...
    │   └── finance/                       # Dept 19
    │       └── ...
    │
    │  # System
    ├── inbox/                             # Scheduled task reports (Tony reads on wake-up)
    │   ├── trend-scan-YYYY-MM-DD.md
    │   ├── mention-scan-YYYY-MM-DD.md
    │   └── daily-metrics-YYYY-MM-DD.md
    └── archive/                           # Processed inbox files
```

### Memory Architecture — 3 Layers of Compounding

**Layer 1: Tony's Memory (CEO-level)**
- Location: `.claude/ceo-memory/` (auto-memory disabled, Tony reads/writes explicitly)
- Remembers: Ash's preferences, strategic decisions, cross-department context, what's in progress
- Portable: lives inside the project folder

**Layer 2: Agent Memory (Individual — 91 agents)**
- Location: `.claude/agent-memory/<agent-name>/MEMORY.md`
- Each agent has `memory: project` in frontmatter
- Remembers: Past work, learnings, patterns that work, domain-specific knowledge
- Example: Content Analyst remembers "carousels outperform threads 3:1"

**Layer 3: Shared Data (Company Knowledge Base)**
- Location: `data/` directory
- Living documents that any agent can read/write
- Compounds over time as agents update with findings
- Example: `data/content/top-performers.md` grows with every analysis

**How compounding works:**
```
Session 1:  Brand Strategist runs audit → saves findings to memory + data/
Session 5:  Long-Form Writer reads brand DNA + own memory → better content
Session 20: Content Analyst reads historical data → finds patterns → updates insights
Session 50: Strategy Planner reads everything → produces roadmap informed by all history
```

**Feedback loops:**
```
Analytics → insights → Strategy → roadmap → Content → posts → Analytics (repeat)
Customers → feedback → Product → improvements → Customer Success → retention (repeat)
Revenue → pricing → Partnerships → deals → Revenue (repeat)
```

### Agent File Pattern
```yaml
---
name: brand-strategist
description: Brand Strategist from Strategy & Research department
tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
memory: project
model: opus
skills:
  - brand-audit
  - brand-dna
  - brand-review
---

You are the **Brand Strategist** of the AI company.
You own core brand positioning...

## Memory Instructions
- After every task, update your memory with key findings
- Always read data/brand/brand-dna.md before any task
- Log important decisions in data/operations/decision-log.md
- Keep your MEMORY.md under 200 lines
- When approaching the limit, summarize older entries and archive details
- Focus on patterns and learnings, not raw logs
```

### Skill File Pattern (Agent-Facing Playbook)
```yaml
---
name: brand-audit
user-invocable: false
description: Step-by-step brand audit methodology
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch
---

## Brand Audit Playbook

### Inputs
- $ARGUMENTS (profiles/links to audit)
- data/brand/brand-dna.md (current positioning)

### Steps
1. Read current brand DNA
2. Analyze provided profiles/links
3. Score across 8 dimensions (voice, visual, consistency, ...)
4. Identify gaps between intended brand and actual presence

### Output
- Write structured audit report to data/brand/latest-audit.md
- Update your memory with key findings
```

### Settings Pattern
```json
{
  "autoMemoryEnabled": false,
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  },
  "permissions": {
    "allow": ["Read", "Write", "Edit", "Grep", "Glob", "WebSearch", "WebFetch", "Agent(*)"]
  }
}
```

### Implementation Phases
```
Phase 1: Foundation
  → .claude/settings.json
  → .claude/ceo-memory/ setup
  → data/ directory with templates
  → /wake-up skill
  → CLAUDE.md (Tony) — already done

Phase 2: Dept 1 — Strategy & Research
  → 5 agent files + 14 skill playbooks
  → Test the full flow: /wake-up → Tony → agent → skill → output

Phase 3: Dept 2 — Content Creation
  → 6 agent files + 16 skill playbooks
  → Test cross-department handoffs (Strategy → Content)

Phase 4: Remaining departments (priority order based on Ash's needs)

Phase 5: Hooks & MCP integrations

Phase 6: CLI Migrator & Packaging (rennos-cli)
  → Node.js CLI tool: `npx rennos init` or `npm install -g rennos`
  → First install flow:
    1. Detects installed CLI tools (claude, codex, gemini)
    2. Asks which CLI to target
    3. Generates CLI-specific files from canonical source
  → Migration flow:
    1. Detects existing RennOS installation
    2. Asks target CLI to migrate to
    3. Translates: instruction files, agent frontmatter, hook event names,
       MCP config format, skill frontmatter extensions
  → What it generates per CLI:
    - Claude Code: CLAUDE.md, .claude/agents/, .claude/skills/, .claude/settings.json
    - Codex CLI: AGENTS.md, .codex/skills/, config.toml (no agents — flattened into skills)
    - Gemini CLI: GEMINI.md, .gemini/agents/, .gemini/commands/, settings.json
    - Cursor: .cursor/rules/, .cursor/mcp.json
  → Publishable on npm + GitHub as open-source package
  → See docs/future-portability-research.md for full compatibility matrix

Phase 7: IT Dev Team — Scrum + Asana (Dept 10 Expansion)
  → Expands Web & Tech (Dept 10) with a dedicated software development team
  → Uses Asana (free tier) as project management tool, Scrum as methodology
  → Asana MCP integration added later — agents start with structured draft outputs

  ## Why This Phase Exists
  - RennOS itself is a software product that needs disciplined development
  - The IT Dev Team dogfoods RennOS by using it to build RennOS
  - Scrum provides structure: clear sprints, defined work, measurable velocity
  - Asana provides visibility: Ash can see all dev work in one board

  ## New Agents (5) — Added to Dept 10: Web & Tech

  | Agent | Scrum Role | Model Tier | Purpose |
  |-------|-----------|------------|---------|
  | **Scrum Master** | Scrum Master | Sonnet | Runs ceremonies, tracks velocity, removes blockers, enforces process |
  | **Tech Lead** | Dev Team (senior) | Opus | Architecture decisions, code reviews, technical direction, PR reviews |
  | **Full-Stack Dev** | Dev Team | Sonnet | Core builder — implements features, fixes bugs, writes code |
  | **QA Engineer** | Dev Team | Sonnet | Test plans, acceptance testing, bug verification, quality gates |
  | **DevOps Engineer** | Dev Team | Sonnet | CI/CD, deployments, infrastructure, automation pipelines |

  Note: Product Owner role is filled by Ash (the actual stakeholder), not an agent.
  Tony (CEO) acts as proxy PO when Ash is unavailable, using priorities from active_projects.md.

  ## Asana Free Tier Setup (Single User)

  **Constraint:** Asana free tier = 1 user (Ash). Agents are not Asana users.
  **Solution:** Tag-based agent assignment. Agents identify their tasks by tag/prefix filtering.

  ### Asana Project Structure
  ```
  Project: "RennOS Development"
  ├── Sections (Scrum board columns):
  │   ├── Product Backlog       — All ungroomed stories/tasks
  │   ├── Sprint Backlog        — Committed work for current sprint
  │   ├── In Progress           — Actively being worked on
  │   ├── In Review             — Code review / QA review
  │   ├── Done                  — Completed in current sprint
  │   └── Blocked               — Waiting on dependency or decision
  │
  ├── Tags (agent assignment):
  │   ├── @scrum-master
  │   ├── @tech-lead
  │   ├── @full-stack-dev
  │   ├── @qa-engineer
  │   ├── @devops-engineer
  │   └── @ash (tasks only Ash can do)
  │
  ├── Tags (task type):
  │   ├── feature
  │   ├── bug
  │   ├── tech-debt
  │   ├── spike (research/exploration)
  │   ├── infra
  │   └── docs
  │
  ├── Tags (priority):
  │   ├── P0-critical
  │   ├── P1-high
  │   ├── P2-medium
  │   └── P3-low
  │
  └── Task naming convention:
      "[AGENT-TAG] Task title — (story points)"
      Examples:
        "@full-stack-dev Build wake-up skill parser — (5)"
        "@qa-engineer Write test plan for agent delegation — (3)"
        "@tech-lead Review architecture for memory system — (2)"
  ```

  ### Task Template (Asana task description)
  ```
  **User Story:** As a [persona], I want [goal] so that [benefit]
  **Acceptance Criteria:**
  - [ ] Criterion 1
  - [ ] Criterion 2
  - [ ] Criterion 3
  **Story Points:** [1/2/3/5/8/13]
  **Sprint:** [Sprint number]
  **Agent:** [@agent-tag]
  **Dependencies:** [list any blocking tasks]
  **Definition of Done:**
  - [ ] Code complete
  - [ ] Tests written/passing
  - [ ] Code reviewed by @tech-lead
  - [ ] QA verified by @qa-engineer
  - [ ] Docs updated
  - [ ] Merged to main
  ```

  ## Scrum Ceremonies (Mapped to Skills)

  | Ceremony | Cadence | Agent | Skill | Output |
  |----------|---------|-------|-------|--------|
  | Sprint Planning | Start of sprint (bi-weekly) | Scrum Master | `/it/sprint-planning.md` | Sprint backlog, committed stories, capacity plan |
  | Daily Standup | Daily (or on-demand) | Scrum Master | `/it/daily-standup.md` | Status summary: done, doing, blocked per agent |
  | Backlog Grooming | Mid-sprint | Scrum Master + Tech Lead | `/it/backlog-grooming.md` | Refined stories, estimated points, priorities |
  | Sprint Review | End of sprint | Scrum Master | `/it/sprint-review.md` | Demo summary, completed vs committed, stakeholder notes |
  | Sprint Retrospective | End of sprint | Scrum Master | `/it/sprint-retro.md` | What went well, what didn't, action items for next sprint |
  | Code Review | Per PR/task | Tech Lead | `/it/code-review.md` | Review feedback, approval/rejection, improvement notes |
  | Bug Triage | As needed | QA Engineer | `/it/bug-triage.md` | Severity, reproduction steps, assigned agent, sprint slot |
  | Deploy Checklist | Per release | DevOps Engineer | `/it/deploy-checklist.md` | Pre-deploy checks, rollback plan, post-deploy verification |
  | Sprint Metrics | End of sprint | Scrum Master | `/it/sprint-metrics.md` | Velocity chart, burndown, completion rate, carry-over |
  | Spike Report | As needed | Tech Lead | `/it/spike-report.md` | Research findings, recommendation, time-boxed summary |
  | Test Plan | Per feature | QA Engineer | `/it/test-plan.md` | Test cases, edge cases, acceptance test checklist |
  | Release Notes | Per release | Full-Stack Dev | `/it/release-notes.md` | What shipped, what changed, known issues |

  ## Sprint Workflow (2-Week Sprints)

  ```
  Day 1 (Monday):
    → Scrum Master runs Sprint Planning (/it/sprint-planning.md)
    → Pulls from Product Backlog → Sprint Backlog
    → Team capacity estimated, stories committed
    → Output: Sprint plan written to data/tech/current-sprint.md

  Days 2-9 (Tues-Tues):
    → Daily Standup (/it/daily-standup.md) — Scrum Master checks status
    → Full-Stack Dev builds features
    → Tech Lead reviews code (/it/code-review.md)
    → QA Engineer tests completed work (/it/test-plan.md)
    → DevOps Engineer handles CI/CD and infra tasks
    → Blocked items escalated to Tony → Ash if needed

  Day 9 (Wednesday):
    → Mid-sprint Backlog Grooming (/it/backlog-grooming.md)
    → Refine upcoming stories for next sprint

  Day 10 (Thursday):
    → Sprint Review (/it/sprint-review.md) — demo to Ash
    → Sprint Retrospective (/it/sprint-retro.md) — team improvement
    → Sprint Metrics (/it/sprint-metrics.md) — velocity tracking
    → Release if applicable (/it/deploy-checklist.md + /it/release-notes.md)
    → Scrum Master archives sprint data to data/tech/sprint-history/

  Day 10 (Friday) or Day 1 of next sprint:
    → Next Sprint Planning begins
  ```

  ## Data Layer

  ```
  data/tech/
  ├── current-sprint.md          — Active sprint: goals, committed stories, status
  ├── product-backlog.md         — Full backlog (mirror of Asana, for offline/agent access)
  ├── sprint-history/            — Archived sprints
  │   ├── sprint-001.md
  │   ├── sprint-002.md
  │   └── ...
  ├── velocity-log.md            — Sprint-over-sprint velocity tracking
  ├── tech-decisions.md          — Architecture Decision Records (ADRs)
  └── release-log.md             — All releases with dates, notes, issues
  ```

  ## Pre-MCP Workflow (Manual Sync)
  Before Asana MCP access is available:
  1. Scrum Master produces sprint plans → writes to data/tech/current-sprint.md
  2. Ash manually creates matching tasks in Asana board
  3. Agents reference data/tech/ files for their assignments
  4. Status updates written to data/tech/current-sprint.md by agents
  5. Ash manually updates Asana board to match

  ## Post-MCP Workflow (Automated Sync)
  Once Asana MCP is connected:
  1. Scrum Master reads Asana backlog directly via MCP
  2. Sprint planning creates/moves tasks in Asana automatically
  3. Agents read their assigned tasks (filtered by their @tag)
  4. Status updates written to both Asana (via MCP) and data/tech/
  5. Sprint metrics pulled from Asana task completion data
  6. Full bidirectional sync — Asana is source of truth, data/tech/ is local cache

  ## Integration with Existing Dept 10 Agents
  The 5 new IT Dev Team agents join the existing 5 Web & Tech agents:
  - Web Developer, Automation Engineer, Tech Stack Manager, Performance Optimizer, Security Specialist
  - Dept 10 grows from 5 → 10 agents, 14 → 26 skill files
  - Existing agents continue their roles; dev team handles structured software delivery
  - Tech Lead coordinates with Tech Stack Manager on tooling decisions
  - DevOps Engineer coordinates with Performance Optimizer on deployments
  - Full-Stack Dev works alongside Web Developer (Web Dev = site work, Full-Stack Dev = product/system code)

  ## Rollout Strategy — Pilot First
  This is a PILOT. The IT Dev Team tests the Asana + Scrum workflow first.
  - Prove the tag-based assignment model works with single-user Asana
  - Prove agents can produce useful sprint artifacts (plans, standups, retros)
  - Prove the pre-MCP → post-MCP transition path is smooth
  - Measure: Are sprints actually helping ship faster? Is the overhead worth it?

  Once the pilot is validated:
  - Revisit Asana for other departments (Ops, Content, Marketing, etc.)
  - Each department may adapt the workflow (not all need full Scrum — some may use Kanban)
  - The tag-based model scales: just add new department tags to the same Asana workspace
  - Scrum Master agent could evolve into a shared resource or spawn department-specific PMs

---

## Personal Departments

### 15. Health & Wellness
- **Purpose:** Physical fitness, nutrition, mental health, sleep, habits
- **Potential Agents:**
  1. **Fitness Coach** — Workout planning, exercise routines, progress tracking
  2. **Nutrition Advisor** — Meal planning, diet tracking, nutrition goals
  3. **Mental Health Guide** — Stress management, mindfulness, journaling prompts, mental wellness
  4. **Habit Tracker** — Builds and tracks daily habits, streaks, accountability
- **Internal Workflow:**
  - Fitness Coach + Nutrition Advisor → work together (diet supports training goals)
  - Habit Tracker → tracks habits from all agents (gym, meals, journaling, sleep)
  - Mental Health Guide → connects to Mindset Coach (Dept 17) for holistic wellbeing
  - Fitness Coach → informs Schedule Manager (Dept 7) to block gym time on master calendar
  - All agents → write to `vault/personal/health/` and `data/personal/health/`
- **Skill Files (9):**

  **Fitness Coach**
  1. `/health/workout-plan.md` — Create/update a workout plan
  2. `/health/fitness-review.md` — Review fitness progress and adjust plan
  3. `/health/exercise-log.md` — Log and track workouts

  **Nutrition Advisor**
  4. `/health/meal-plan.md` — Create a meal plan based on goals
  5. `/health/nutrition-review.md` — Review diet and suggest improvements

  **Mental Health Guide**
  6. `/health/journal-prompt.md` — Generate a reflective journaling prompt
  7. `/health/wellness-check.md` — Mental wellness check-in and recommendations

  **Habit Tracker**
  8. `/health/habit-setup.md` — Define and set up a new habit to track
  9. `/health/habit-review.md` — Review habit streaks and accountability

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 16. Relationships
- **Purpose:** Personal connections, professional networking, CRM, follow-ups
- **Potential Agents:**
  1. **Network Manager** — Personal CRM — tracks contacts, relationship strength, last interaction, follow-up reminders
  2. **Connection Strategist** — Identifies who to connect with, intro strategies, networking goals
  3. **Follow-Up Agent** — Drafts follow-up messages, thank-you notes, check-ins
  4. **Family & Friends Planner** — Tracks birthdays, events, gift ideas, quality time planning
- **Internal Workflow:**
  - Network Manager → extends Partnership Scout (Dept 6) for personal contacts (same CRM, different tags)
  - Connection Strategist → informed by Audience Researcher (Dept 1) for professional networking
  - Follow-Up Agent → drafts only, Tony presents for approval (follows approval gate)
  - Family & Friends Planner → feeds into Schedule Manager (Dept 7) for birthday reminders, events
  - All agents → write to `data/personal/relationships/`
- **Skill Files (9):**

  **Network Manager**
  1. `/relationships/contact-add.md` — Add a new contact with context and notes
  2. `/relationships/contact-review.md` — Review contacts, flag stale relationships, suggest re-engagement
  3. `/relationships/network-map.md` — Map your network by categories (mentors, peers, industry, personal)

  **Connection Strategist**
  4. `/relationships/connection-plan.md` — Plan who to connect with and why
  5. `/relationships/intro-request.md` — Draft an introduction request

  **Follow-Up Agent**
  6. `/relationships/follow-up-draft.md` — Draft a follow-up message after meeting/event
  7. `/relationships/check-in-draft.md` — Draft a casual check-in message

  **Family & Friends Planner**
  8. `/relationships/events-tracker.md` — Track birthdays, anniversaries, important dates
  9. `/relationships/gift-ideas.md` — Brainstorm gift ideas for someone

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 17. Personal Growth
- **Purpose:** Learning goals, skill development, reading, mindset, reflection
- **Potential Agents:**
  1. **Learning Coach** — Plans learning goals, builds study schedules, tracks progress (guitar in 3 months, etc.)
  2. **Reading Manager** — Manages reading list, book summaries, key takeaways
  3. **Skill Tracker** — Tracks skills being developed, milestones, skill gaps
  4. **Mindset Coach** — Goal-setting frameworks, motivation, reflection, personal vision
- **Internal Workflow:**
  - Mindset Coach ↔ Mental Health Guide (Dept 15) — holistic wellbeing loop
  - Learning Coach → informs Content Creation (Dept 2) — learning journey becomes content topics
  - Reading Manager → processes book clippings from Knowledge Manager (C-Suite)
  - Skill Tracker → feeds into Strategy Planner (Dept 1) for personal brand positioning (new skills = new authority)
  - Learning Coach → informs Schedule Manager (Dept 7) to block study/practice time
  - All agents → write to `vault/personal/goals/` and `data/personal/growth/`
- **Skill Files (9):**

  **Learning Coach**
  1. `/growth/learning-plan.md` — Create a structured learning plan with milestones
  2. `/growth/learning-review.md` — Review learning progress and adjust plan
  3. `/growth/resource-finder.md` — Find courses, tutorials, resources for a skill

  **Reading Manager**
  4. `/growth/reading-list.md` — Add to / manage the reading list
  5. `/growth/book-summary.md` — Summarize a book's key takeaways

  **Skill Tracker**
  6. `/growth/skill-assessment.md` — Assess current skill level and define target
  7. `/growth/milestone-check.md` — Check progress against skill milestones

  **Mindset Coach**
  8. `/growth/goal-setting.md` — Define a personal goal with structure and accountability
  9. `/growth/reflection.md` — Guided reflection on progress, wins, and lessons

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 18. Life Admin
- **Purpose:** Personal to-dos, travel, errands, subscriptions, home management
- **Potential Agents:**
  1. **Task Manager** — Personal to-dos, errands, reminders, daily logistics
  2. **Travel Planner** — Trip planning, itineraries, bookings research, packing lists
  3. **Subscription Manager** — Tracks subscriptions, renewal dates, cost optimization
  4. **Home Manager** — Home maintenance, chores, repairs, household planning
- **Internal Workflow:**
  - Task Manager → syncs with Project Coordinator (Dept 7) for unified personal + work task view
  - Subscription Manager → feeds costs into Expense Tracker (Dept 19) for budget tracking
  - Travel Planner → informs Schedule Manager (Dept 7) to block travel dates on master calendar
  - Home Manager → uses Schedule Manager (Dept 7) for recurring maintenance reminders
  - All agents → write to `data/personal/admin/`
- **Skill Files (9):**

  **Task Manager**
  1. `/admin/todo-list.md` — Create/update personal to-do list
  2. `/admin/errand-plan.md` — Plan and prioritize errands for the day/week
  3. `/admin/reminder-set.md` — Set a reminder for something important

  **Travel Planner**
  4. `/admin/trip-plan.md` — Plan a trip (itinerary, logistics, budget)
  5. `/admin/packing-list.md` — Generate a packing list for a trip

  **Subscription Manager**
  6. `/admin/subscription-audit.md` — Audit all subscriptions, flag unused, calculate total spend
  7. `/admin/renewal-tracker.md` — Track upcoming renewals and cancellation deadlines

  **Home Manager**
  8. `/admin/maintenance-schedule.md` — Create/review home maintenance schedule
  9. `/admin/household-plan.md` — Plan household tasks and chores

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

### 19. Personal Finance
- **Purpose:** Personal budgeting, savings, investments, expense tracking (separate from business finance)
- **Potential Agents:**
  1. **Budget Manager** — Personal budget tracking, expense categories, monthly reviews
  2. **Savings Planner** — Savings goals, emergency fund, milestones
  3. **Investment Advisor** — Portfolio tracking, investment research, allocation strategy
  4. **Expense Tracker** — Logs expenses, flags overspending, spending trends
- **Internal Workflow:**
  - Budget Manager → receives salary/distribution data from Income Tracker (Dept 11) — the bridge between business and personal
  - Expense Tracker → receives subscription costs from Subscription Manager (Dept 18)
  - Savings Planner → informs Financial Planner (Dept 11) for holistic financial picture
  - Investment Advisor → uses Executive Researcher (C-Suite) for deep investment research
  - All agents → write to `data/personal/finance/`
- **Skill Files (8):**

  **Budget Manager**
  1. `/personal-finance/budget-create.md` — Create/update monthly personal budget
  2. `/personal-finance/budget-review.md` — Review spending vs budget, flag overages

  **Savings Planner**
  3. `/personal-finance/savings-goal.md` — Set up a savings goal with target and timeline
  4. `/personal-finance/savings-review.md` — Review progress toward savings goals

  **Investment Advisor**
  5. `/personal-finance/portfolio-review.md` — Review investment portfolio and allocation
  6. `/personal-finance/investment-research.md` — Research an investment opportunity

  **Expense Tracker**
  7. `/personal-finance/expense-log.md` — Log and categorize expenses
  8. `/personal-finance/spending-trends.md` — Analyze spending trends and flag patterns

- **Tools / Integrations:** *(decide at implementation)*
  -
- **Notes:**
  -

---

## Open Questions
- [ ] Which platforms are we targeting? (X, LinkedIn, YouTube, TikTok, Instagram, etc.)
- [ ] What is the primary brand goal? (Thought leadership, audience growth, monetization, etc.)
- [ ] What MCP servers will each department need?
- [ ] What actions can agents take autonomously vs. requiring Ash's approval?

---

## Parking Lot (Handle during implementation)
- [ ] Knowledge Manager: define routing taxonomy (how clippings get categorized and where they go)
- [ ] Knowledge Manager: define template usage (when/how agents apply Obsidian templates)
- [ ] Vault: bidirectional access rules (which agents can read which vault folders)
- [ ] Obsidian web clipper configuration (which plugin, markdown format)

---

## Future Enhancements (Post-UAT)

### Personality Configuration (inspired by OpenClaw)
After initial UAT of the hardcoded system, rework Tony's identity to be user-configurable:

1. **Let user name the agent** — during onboarding, ask "What should I call myself?" instead of hardcoding "Tony." Update CLAUDE.md, org-chart, and all agent references dynamically.
2. **Separate SOUL from OPERATIONS** — split CLAUDE.md into operational rules (delegation, approval gate, paths) and a new `ceo-memory/identity.md` for personality (name, tone, values, anti-patterns). Different update cadences.
3. **Specificity-driven personality** — replace vague rules ("Speak concisely") with concrete ones ("Default to 1-2 sentences. Never open with a compliment. If the idea is bad, say so directly."). Include example good/bad responses.
4. **Anti-pattern list** — explicitly list what the agent should NEVER say ("I hope this helps", "Great question!", unnecessary apologies, corporate buzzwords, sycophancy).
5. **Personality evolution via feedback** — make `ceo-memory/feedback.md` actively update personality rules based on corrections, not just log them. The agent sharpens its voice over time.

**Trigger:** Run this after 5-10 real sessions with the hardcoded system. By then Ash will know which personality traits work, which annoy, and what anti-patterns to add based on real frustrations — not guesses.

**Reference:** OpenClaw's architecture (SOUL.md + IDENTITY.md + BOOTSTRAP.md self-delete pattern). See research notes from 2026-03-22 session.

### Tools & MCP Reference Doc (Post-Integration)
When MCP servers and CLI tools are configured, create `ceo-memory/tools.md` documenting:
- What integrations are live (GitHub, Slack, Notion, etc.)
- What each MCP does and when Tony should use it vs asking Ash
- Which agents have which MCPs scoped to them (via agent frontmatter `mcpServers:`)
- Integration status: live vs planned vs not needed

**Why:** MCP tools auto-load into sessions, so Tony sees them automatically. But he needs *operational context* — when to reach for each tool, not just that it exists.

**Trigger:** When first MCP server is configured in `.mcp.json`.
