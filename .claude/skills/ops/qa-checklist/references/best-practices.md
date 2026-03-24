# QA Checklists by Deliverable Type

Reference guide for quality assurance checks organized by content type. Each section contains a comprehensive checklist to run before any deliverable goes live.

---

## Universal Checks (Apply to ALL Deliverable Types)

Run these checks on every piece of content regardless of type:

- [ ] **Brand voice alignment** -- Does it sound like us? Compare against `data/brand/brand-dna.md`
- [ ] **Style guide compliance** -- Formatting, tone, and conventions match `data/brand/style-guide.md`
- [ ] **Factual accuracy** -- All claims verified; no unsubstantiated statistics or assertions
- [ ] **Spelling and grammar** -- Clean copy, no typos, correct punctuation
- [ ] **Link validation** -- Every link tested and pointing to the correct destination (no 404s)
- [ ] **Sensitive information** -- No leaked internal data, passwords, pricing errors, or PII
- [ ] **CTA present and clear** -- Reader knows what to do next
- [ ] **Legal compliance** -- No trademark misuse, copyright violations, or regulatory issues
- [ ] **Accessibility** -- Alt text on images, legible fonts, sufficient color contrast
- [ ] **Mobile readability** -- Content renders correctly on smaller screens

---

## 1. Blog Post / Article

### Structure
- [ ] Single H1 tag containing the primary keyword
- [ ] Logical H2/H3 hierarchy -- no skipped heading levels
- [ ] Opening paragraph hooks the reader and states the value proposition
- [ ] Short paragraphs (2-4 lines max) for scannability
- [ ] Bullet points or numbered lists break up dense sections
- [ ] Strong conclusion with a clear CTA or takeaway
- [ ] Word count appropriate for topic (typically 1,200-2,400 words for SEO)

### SEO
- [ ] Meta title present (50-60 characters, includes primary keyword)
- [ ] Meta description written (150-160 characters, compelling, includes keyword)
- [ ] Primary keyword appears in H1, first 100 words, and naturally throughout
- [ ] Secondary keywords woven in without stuffing
- [ ] URL slug is short, descriptive, and hyphenated
- [ ] Internal links to 2-3 relevant pages/posts
- [ ] External links to authoritative sources where appropriate
- [ ] Image alt text is descriptive and includes keywords where natural
- [ ] Schema markup applied (Article or BlogPosting structured data)

### Readability
- [ ] Flesch Reading Ease score appropriate for target audience (aim for 60+ for general)
- [ ] Active voice used predominantly
- [ ] Jargon replaced with clear language unless audience expects it
- [ ] Transition words connect paragraphs and sections
- [ ] BLUF (Bottom Line Up Front) formatting for key takeaways

### Formatting
- [ ] Featured image present and correctly sized
- [ ] All images optimized for web (compressed, correct dimensions)
- [ ] Image captions added where helpful
- [ ] Code blocks formatted correctly (if applicable)
- [ ] Publish date and author attribution present
- [ ] Category and tags assigned

---

## 2. Email / Newsletter

### Subject Line
- [ ] Under 50 characters (avoid mobile truncation)
- [ ] Compelling -- creates curiosity, states benefit, or addresses pain point
- [ ] No spam trigger words (FREE!!!, Act Now, Limited Time, etc.)
- [ ] Personalization tokens render correctly (e.g., {{first_name}} resolves)
- [ ] A/B variant prepared if volume justifies testing

### Preview Text
- [ ] Custom preview text set (not defaulting to "View in browser")
- [ ] Complements the subject line -- extends the hook, does not repeat it
- [ ] Under 90 characters for consistent display across clients

### Content
- [ ] Single primary CTA (one clear action per email)
- [ ] Copy is scannable -- short paragraphs, subheadings, bold key phrases
- [ ] Personalization tokens all resolve correctly (test with real data)
- [ ] Reply-to address is monitored (not a no-reply@ address if engagement matters)
- [ ] Tone matches brand voice and the audience segment

### Links and Tracking
- [ ] Every link tested and working (buttons, text links, images)
- [ ] UTM parameters appended to all outbound links
- [ ] Links open in new tab/window where appropriate
- [ ] Unsubscribe link present and functional

### CAN-SPAM / Legal Compliance
- [ ] Physical mailing address included in footer
- [ ] Unsubscribe mechanism works and processes within 10 business days
- [ ] Sender name and email address accurately identify the sender
- [ ] Subject line is not deceptive or misleading
- [ ] Email is clearly identified as an advertisement (if applicable)

### Technical / Rendering
- [ ] Tested across major email clients (Gmail, Outlook, Apple Mail, Yahoo)
- [ ] Mobile responsive -- stacks correctly on small screens
- [ ] Images have alt text (in case images are blocked by default)
- [ ] Fallback fonts specified for custom web fonts
- [ ] Dark mode rendering checked
- [ ] Total email size under 100KB (excluding images) for deliverability
- [ ] SPF, DKIM, and DMARC authentication confirmed on sending domain

### Segmentation
- [ ] Correct audience segment selected
- [ ] Exclusion lists applied (recent purchasers, unsubscribers, etc.)
- [ ] Send time optimized for audience time zone

---

## 3. Social Media Post

### Platform Specifications

**X (Twitter)**
- [ ] Post under 280 characters (ideal: under 100 for engagement)
- [ ] 1-2 hashtags maximum
- [ ] Image dimensions: 1200 x 675 px (1.91:1 ratio)

**Instagram**
- [ ] Caption under 2,200 characters (key message in first 125 before truncation)
- [ ] 3-5 relevant hashtags (not the max 30)
- [ ] Image: 1080 x 1080 px (square) or 1080 x 1350 px (portrait)
- [ ] Reels/Stories: 1080 x 1920 px (9:16)

**LinkedIn**
- [ ] Post under 3,000 characters (sweet spot: 1,000-1,500 for engagement)
- [ ] 2-3 professional, industry-specific hashtags
- [ ] Image: 1200 x 627 px

**Facebook**
- [ ] Key message in first 80 characters (66% more engagement)
- [ ] Image: 1200 x 630 px
- [ ] Video: under 1 minute for feed, captions enabled

**TikTok**
- [ ] Caption under 2,200 characters
- [ ] 3-5 trend-aligned hashtags
- [ ] Video: 1080 x 1920 px (9:16), ideal length 15-60 seconds

### Content Quality
- [ ] Copy tailored for the specific platform (not copy-pasted across all)
- [ ] @mentions are correct and accounts exist
- [ ] Hashtags are relevant, not banned, and properly formatted (no spaces)
- [ ] Media assets meet platform resolution and file size requirements
- [ ] Video has captions/subtitles (85% of social video watched without sound)
- [ ] No watermarks from other platforms (e.g., TikTok watermark on Reels)

### Voice and Brand
- [ ] Tone appropriate for the platform context
- [ ] Aligns with brand voice guidelines
- [ ] No off-brand humor, slang, or references that could misfire
- [ ] Emoji usage matches brand style (if applicable)

### CTA and Engagement
- [ ] Clear CTA (comment, share, click link, save, etc.)
- [ ] Link in bio updated if CTA references it
- [ ] Comment strategy planned (first comment, response templates)
- [ ] Posting time aligned with audience activity data

### Compliance
- [ ] Paid partnership/sponsorship disclosed per FTC guidelines
- [ ] No copyrighted music, images, or video without license
- [ ] Geo-restrictions applied if content is market-specific

---

## 4. Landing Page

### Above the Fold
- [ ] Headline is clear, benefit-driven, and matches the traffic source
- [ ] Message match -- ad/email promise is reflected on the page
- [ ] Hero image or video supports the value proposition
- [ ] Primary CTA visible without scrolling
- [ ] No navigation menu (minimize exit paths on dedicated landing pages)

### CTA Design
- [ ] Button text is action-oriented ("Get Started," "Download Now," not "Submit")
- [ ] CTA button has high contrast against the background
- [ ] CTA appears at least twice on longer pages (top and bottom minimum)
- [ ] Form fields are minimal (only ask for what you need)
- [ ] Multi-step forms used for complex data collection

### Trust Signals
- [ ] Social proof present (testimonials, logos, review counts, case study snippets)
- [ ] Trust badges displayed (security, certifications, guarantees)
- [ ] Real customer quotes with names, titles, and photos where possible
- [ ] Privacy policy linked near any form or data collection point

### Content
- [ ] Copy is benefits-focused, not feature-focused
- [ ] Objections addressed (FAQ section, guarantee, risk reversal)
- [ ] Urgency or scarcity used honestly (if applicable)
- [ ] No distracting elements (excessive animations, auto-play audio)
- [ ] Content hierarchy guides the eye: headline -> benefit -> proof -> CTA

### Mobile Optimization
- [ ] Fully responsive -- tested on iOS and Android devices
- [ ] Tap targets are large enough (minimum 44x44 px)
- [ ] Forms are mobile-friendly (proper input types, auto-fill support)
- [ ] Images scale correctly without overflow
- [ ] CTA button is thumb-reachable on mobile

### Page Speed and Technical
- [ ] Page loads in under 3 seconds (test with Google PageSpeed Insights)
- [ ] Images compressed and served in modern formats (WebP, AVIF)
- [ ] Lazy loading enabled for below-fold images
- [ ] No broken elements in incognito/private browsing mode
- [ ] Analytics and conversion tracking pixels firing correctly
- [ ] Form submission confirmation/thank-you page works
- [ ] HTTPS enforced (no mixed content warnings)
- [ ] Cookie consent banner present per GDPR/CCPA requirements

### Compliance
- [ ] Privacy policy accessible
- [ ] Terms of service linked (if collecting data or processing payments)
- [ ] FTC-compliant if making product claims or showing testimonials
- [ ] ADA/WCAG accessibility standards met (screen reader compatible)

---

## 5. Press Release

### AP Style Formatting
- [ ] Headline in title case, under 100 characters, active verbs
- [ ] Subheadline adds context (sentence case, no period)
- [ ] Dateline format: CITY NAME, Month Day, Year --
- [ ] Single space after periods (not double)
- [ ] Numbers one through nine spelled out; 10+ use numerals
- [ ] State names abbreviated per AP style (not postal codes)
- [ ] Percent spelled out in text ("percent" not "%")
- [ ] Titles capitalized before names, lowercase after

### Structure (Inverted Pyramid)
- [ ] Lead paragraph answers Who, What, When, Where, Why (5 Ws)
- [ ] Most newsworthy information in the first two paragraphs
- [ ] Supporting details descend in order of importance
- [ ] Total length between 300-500 words
- [ ] Font: Times New Roman or Arial, 12pt, single-spaced, left-aligned

### Quotes
- [ ] At least one executive quote included
- [ ] Full name and title on first reference; last name only after
- [ ] Quotes add insight or perspective, not just restate facts
- [ ] Periods and commas placed inside quotation marks
- [ ] Each new speaker starts a new paragraph
- [ ] Attribution uses "said" (not "stated," "exclaimed," or "shared")

### Boilerplate
- [ ] Under 100 words
- [ ] Includes company mission, founding date, and key offerings
- [ ] Mentions significant achievements or recognitions
- [ ] Consistent across all releases (no one-off variations)
- [ ] Placed after the body text, before contact information

### Contact Information
- [ ] Media contact name and title listed
- [ ] Phone number and email address included
- [ ] Contact person is reachable and briefed on the announcement
- [ ] Placed at the bottom of the release

### Distribution
- [ ] End mark present ("###" or "-30-" centered below body)
- [ ] Embargo date/time clearly stated at top if applicable
- [ ] Multimedia assets (photos, logos) attached with captions
- [ ] Distribution list matches the news angle and beat

---

## 6. Ad Copy

### Compliance and Legal
- [ ] All claims are truthful, substantiated, and not misleading
- [ ] Required disclosures present (FTC, industry-specific regulations)
- [ ] Competitor references are factual and defensible
- [ ] Testimonial/endorsement disclaimers included where required
- [ ] Copyright and trademark symbols used correctly
- [ ] Platform-specific ad policies reviewed (Google, Meta, LinkedIn, etc.)

### Character Limits by Platform

**Google Ads (Search)**
- [ ] Headlines: 30 characters each (up to 15 headlines in RSA)
- [ ] Descriptions: 90 characters each (up to 4 descriptions)
- [ ] Display URL path: 15 characters per path field

**Meta (Facebook/Instagram)**
- [ ] Primary text: 125 characters visible (up to 2,200)
- [ ] Headline: 40 characters recommended
- [ ] Link description: 30 characters recommended

**LinkedIn**
- [ ] Intro text: 150 characters visible (up to 600)
- [ ] Headline: 70 characters
- [ ] Description: 100 characters

### CTA
- [ ] CTA is specific and action-oriented
- [ ] CTA matches the landing page action (consistency from ad to page)
- [ ] Urgency created without false scarcity
- [ ] One CTA per ad (no competing actions)

### Targeting Alignment
- [ ] Ad copy speaks to the defined audience segment
- [ ] Pain points and language match the target persona
- [ ] Offer is relevant to the awareness stage (TOFU/MOFU/BOFU)
- [ ] Geographic or demographic references are accurate
- [ ] Negative keywords reviewed (search ads)

### Creative and Technical
- [ ] Image/video meets platform specs (resolution, aspect ratio, file size)
- [ ] Text overlay under 20% of image area (Meta guideline)
- [ ] No pixelated, stretched, or cropped-off visuals
- [ ] Brand logo visible but not dominant
- [ ] A/B variants prepared (at least 2 creative variations)
- [ ] Tracking pixels and UTM parameters configured
- [ ] Landing page URL is correct and live
- [ ] Ad preview reviewed in all placements (feed, stories, sidebar, etc.)

---

## 7. Pitch / Outreach Email

### Subject Line
- [ ] 4-8 words, under 50 characters (avoids mobile truncation)
- [ ] Personalized (name, company, or specific reference)
- [ ] Creates curiosity or states a clear benefit
- [ ] No spam triggers (all caps, excessive punctuation, "FREE")
- [ ] Question-format subject lines average 46% open rate -- use where appropriate

### Personalization
- [ ] Recipient's name spelled correctly
- [ ] Company name accurate and current
- [ ] Reference to a specific achievement, post, or event (shows genuine research)
- [ ] Pain point or challenge is relevant to their role/industry
- [ ] No template artifacts (e.g., [COMPANY NAME] or {{variable}} visible)
- [ ] Addressing specific challenges performs 202% better than generic approaches

### Length and Structure
- [ ] Under 150 words total (cold outreach sweet spot)
- [ ] Opening line is about THEM, not about you
- [ ] Value proposition stated in 1-2 sentences max
- [ ] Social proof included briefly (1 line -- a client name, result, or metric)
- [ ] Single clear ask in the closing line
- [ ] P.S. line used strategically if it adds value (not as a crutch)

### The Ask
- [ ] One specific, low-friction ask (not multiple requests)
- [ ] Calendar link or specific times offered (reduce back-and-forth)
- [ ] Ask is proportional to the relationship (don't ask too much too soon)
- [ ] Clear next step defined

### Technical
- [ ] Sent from a warmed-up domain (not a brand-new email address)
- [ ] Signature includes name, title, company, and one relevant link
- [ ] No large attachments (link to resources instead)
- [ ] Follow-up sequence planned (3-5 touches over 2-3 weeks)
- [ ] Reply tracking enabled to measure engagement
- [ ] Sent during business hours in recipient's time zone

### Compliance
- [ ] CAN-SPAM compliant (physical address, opt-out mechanism for bulk)
- [ ] GDPR compliant if contacting EU recipients (legitimate interest basis)
- [ ] Not scraping contact info from sources that prohibit it

---

## Sources

1. [Email On Acid -- Email QA Checklist: How to Nail Quality Assurance in 7 Steps](https://www.emailonacid.com/blog/article/needs-improvement/solid-email-qa/)
2. [Unbounce -- The Ultimate 49-Point Landing Page Checklist](https://unbounce.com/landing-pages/checklist/)
3. [PR Newswire -- How to Write an AP Style Press Release: Format & Examples](https://www.prnewswire.com/resources/articles/ap-style-press-release/)
4. [Ad Reform -- Key Ad QA Processes and Checklists](https://blog.adreform.com/key-ad-qa-processes-checklists)
5. [Sociality.io -- Social Media Character Limits in 2025](https://sociality.io/blog/social-media-character-limits/)
6. [Cleverly -- Cold Email Outreach Best Practices: The Ultimate Guide for 2025-26](https://www.cleverly.co/blog/cold-email-outreach-best-practices)
7. [Search Atlas -- SEO Readability Checklist for Stronger SEO Scores](https://searchatlas.com/blog/seo-readability-checklist/)
8. [Siteimprove -- How to Build Your Content Quality Assurance Framework](https://www.siteimprove.com/blog/content-quality-assurance-framework/)
9. [SocialBee -- 30+ Social Media Best Practices to Follow in 2025](https://socialbee.com/blog/social-media-best-practices/)
10. [Newswire -- How to Write a Press Release Boilerplate](https://www.newswire.com/blog/how-to-write-a-press-release-boilerplate)
11. [Overloop -- The 2025 Cold Email Guide](https://overloop.com/blog/how-to-write-a-successful-cold-email)
12. [KlientBoost -- Landing Page Checklist: A Proven System for Better Performance](https://www.klientboost.com/landing-pages/landing-page-checklist/)
