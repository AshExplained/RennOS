# SEO Audit Best Practices Reference (2026)

> Last updated: 2026-03-24
> Use this document as the methodology backbone for every SEO audit.

---

## Table of Contents

1. [Core Web Vitals](#1-core-web-vitals)
2. [On-Page SEO Checklist](#2-on-page-seo-checklist)
3. [Technical SEO Checklist](#3-technical-seo-checklist)
4. [E-E-A-T Guidelines](#4-e-e-a-t-guidelines)
5. [Mobile-First Indexing Requirements](#5-mobile-first-indexing-requirements)
6. [AI Search Optimization](#6-ai-search-optimization)
7. [Sources](#7-sources)

---

## 1. Core Web Vitals

Core Web Vitals are Google's page experience signals that directly affect rankings. All three metrics are evaluated at the **75th percentile** of real user data (CrUX). A page must pass all three to achieve an overall "good" assessment.

### 1.1 Largest Contentful Paint (LCP) — Loading Performance

Measures the time from navigation start until the largest visible content element (image, video poster, or text block) is rendered.

| Rating            | Threshold     |
|-------------------|---------------|
| Good              | < 2,500 ms    |
| Needs Improvement | 2,500–4,000 ms|
| Poor              | > 4,000 ms    |

**Current benchmark:** Only 62% of mobile pages achieve a "good" LCP score.

**Optimization checklist:**
- [ ] Preload LCP images with `fetchpriority="high"`
- [ ] Use modern image formats (WebP, AVIF)
- [ ] Optimize server response time (TTFB < 800ms)
- [ ] Eliminate render-blocking CSS and JS
- [ ] Use a CDN for static assets
- [ ] Inline critical CSS above the fold
- [ ] Avoid lazy-loading the LCP element
- [ ] Compress and right-size images

### 1.2 Interaction to Next Paint (INP) — Responsiveness

Measures the latency of all user interactions (clicks, taps, key presses) throughout the page lifecycle, reporting the worst interaction (with outliers excluded). Replaced First Input Delay (FID) in March 2024.

| Rating            | Threshold   |
|-------------------|-------------|
| Good              | < 200 ms    |
| Needs Improvement | 200–500 ms  |
| Poor              | > 500 ms    |

**Current benchmark:** 43% of sites fail the 200ms threshold, making INP the most commonly failed Core Web Vital in 2026. 77% of mobile pages pass.

**Optimization checklist:**
- [ ] Defer non-critical JavaScript
- [ ] Break up long tasks (> 50ms) on the main thread
- [ ] Use `requestIdleCallback` or `scheduler.yield()` for non-urgent work
- [ ] Minimize third-party script impact
- [ ] Avoid forced synchronous layouts
- [ ] Use web workers for heavy computation
- [ ] Audit event handlers for unnecessary complexity

### 1.3 Cumulative Layout Shift (CLS) — Visual Stability

Measures the sum of all unexpected layout shifts that occur during the page's entire lifespan. A layout shift occurs when a visible element changes position between rendered frames without user interaction.

| Rating            | Threshold  |
|-------------------|------------|
| Good              | < 0.1      |
| Needs Improvement | 0.1–0.25   |
| Poor              | > 0.25     |

**Current benchmark:** 81% of mobile pages achieve a "good" score — the best-performing CWV metric.

**Optimization checklist:**
- [ ] Set explicit `width` and `height` attributes on all images and videos
- [ ] Reserve space for ads, embeds, and iframes
- [ ] Self-host fonts with `font-display: swap` or `optional`
- [ ] Preload web fonts
- [ ] Avoid dynamically injecting content above existing content
- [ ] Use CSS `contain` property for layout isolation
- [ ] Use `aspect-ratio` CSS for responsive media containers

### 1.4 Measurement Tools

- **Field data (real users):** Google Search Console (CWV report), CrUX Dashboard, PageSpeed Insights (field data section)
- **Lab data (synthetic):** Lighthouse, WebPageTest, Chrome DevTools Performance panel
- **Continuous monitoring:** DebugBear, SpeedCurve, Calibre

---

## 2. On-Page SEO Checklist

Audit every page against these elements:

### 2.1 Title Tag
- [ ] Contains primary keyword within the first 60 characters
- [ ] Unique across all pages on the site
- [ ] Compelling and click-worthy (not keyword-stuffed)
- [ ] Matches search intent for the target query
- [ ] Does not exceed 60 characters (to avoid SERP truncation)

### 2.2 Meta Description
- [ ] Includes primary keyword naturally
- [ ] Between 120–160 characters
- [ ] Contains a clear value proposition or call to action
- [ ] Unique per page (no duplicates across site)
- [ ] Accurately summarizes the page content

### 2.3 Header Structure
- [ ] Exactly one H1 per page, containing the primary keyword
- [ ] Logical H2/H3/H4 hierarchy (no skipping levels)
- [ ] Headers break content into scannable sections
- [ ] Secondary keywords placed in H2/H3 tags where natural
- [ ] Header text is descriptive (not generic like "Introduction")

### 2.4 URL Structure
- [ ] Short, descriptive, and human-readable
- [ ] Contains primary keyword (hyphen-separated)
- [ ] No unnecessary parameters, session IDs, or dynamic strings
- [ ] Lowercase only
- [ ] Consistent trailing slash convention site-wide

### 2.5 Keyword Usage
- [ ] Primary keyword appears in: title, H1, first 100 words, URL, meta description
- [ ] Keyword density is natural (typically 1–2% for primary)
- [ ] LSI (semantically related) keywords are used throughout
- [ ] No keyword cannibalization across pages (one primary keyword per page)
- [ ] Search intent is matched (informational, transactional, navigational)

### 2.6 Content Quality
- [ ] Content length is competitive with top-ranking pages
- [ ] Satisfies search intent completely
- [ ] Provides unique value (original data, perspectives, examples)
- [ ] Up to date (check dates, statistics, references)
- [ ] Well-formatted with lists, tables, images, and whitespace
- [ ] Readability appropriate for audience (aim for Grade 8–10 reading level for general content)

### 2.7 Internal Links
- [ ] At least 3–5 internal links per page to related content
- [ ] Descriptive anchor text (not "click here")
- [ ] Strategic links to high-priority pages
- [ ] No orphan pages (every page reachable within 3–4 clicks of homepage)
- [ ] Broken internal links identified and fixed

### 2.8 External Links
- [ ] Links to authoritative, relevant sources
- [ ] External links open in new tab where appropriate
- [ ] No links to low-quality or spammy domains
- [ ] Outbound link quantity is reasonable (not excessive)

### 2.9 Images
- [ ] All images have descriptive `alt` text including keywords where natural
- [ ] Images are compressed and right-sized
- [ ] Modern formats used (WebP, AVIF with fallbacks)
- [ ] Lazy loading applied to below-the-fold images
- [ ] Image filenames are descriptive (not `IMG_1234.jpg`)

### 2.10 Schema / Structured Data
- [ ] Appropriate schema markup implemented (Article, Product, FAQ, HowTo, etc.)
- [ ] Validated with Google Rich Results Test
- [ ] JSON-LD format used (Google's preferred format)
- [ ] Author and Organization schema present
- [ ] Breadcrumb schema implemented

---

## 3. Technical SEO Checklist

### 3.1 Crawlability
- [ ] `robots.txt` is properly configured (not blocking critical resources)
- [ ] XML sitemap is submitted to Google Search Console and Bing Webmaster Tools
- [ ] XML sitemap excludes: noindex pages, redirected URLs, duplicate pages, 4xx/5xx pages
- [ ] Sitemap is under 50MB / 50,000 URLs per file (use sitemap index for larger sites)
- [ ] No crawl errors in Search Console (fix or deliberately exclude)
- [ ] Redirect chains are 2 hops or fewer
- [ ] No redirect loops
- [ ] Canonical tags are consistent and correct
- [ ] Server log analysis performed to identify crawl waste
- [ ] Crawl budget optimized (for sites with 10,000+ pages)
- [ ] AI crawler access configured in `robots.txt` (GPTBot, Google-Extended, etc.)

### 3.2 Indexing
- [ ] All important pages are indexed (check `site:domain.com` and Search Console Index Coverage)
- [ ] No unintended `noindex` tags on important pages
- [ ] Duplicate content is consolidated via canonical tags
- [ ] Thin/low-value pages are either improved, consolidated, or noindexed
- [ ] Pagination handled correctly (self-referencing canonicals, no noindex on paginated pages)
- [ ] Parameter handling configured in Search Console where applicable
- [ ] Hreflang tags correct for multi-language sites

### 3.3 Site Architecture
- [ ] Logical hierarchy: Homepage → Category → Subcategory → Page
- [ ] Most content reachable within 3–4 clicks from homepage
- [ ] Flat architecture preferred (avoid deep nesting)
- [ ] Breadcrumb navigation implemented
- [ ] HTML sitemap available for users
- [ ] Faceted navigation handled properly (noindex or canonical for filter combinations)

### 3.4 HTTPS & Security
- [ ] Entire site served over HTTPS
- [ ] Valid SSL certificate (not expired, correct domain)
- [ ] HTTP → HTTPS redirects in place (301)
- [ ] Mixed content warnings resolved (no HTTP resources on HTTPS pages)
- [ ] HSTS header configured
- [ ] Security headers present (X-Content-Type-Options, X-Frame-Options, CSP)

### 3.5 Performance
- [ ] Server response time (TTFB) under 800ms
- [ ] GZIP or Brotli compression enabled
- [ ] Browser caching configured with appropriate max-age headers
- [ ] CDN in use for static assets
- [ ] Critical rendering path optimized
- [ ] Async/defer attributes on non-critical scripts
- [ ] CSS and JS minified and bundled
- [ ] HTTP/2 or HTTP/3 enabled

### 3.6 Structured Data
- [ ] Schema markup implemented for content type (Article, Product, FAQ, LocalBusiness, etc.)
- [ ] Validated with Rich Results Test (no errors)
- [ ] Monitored in Search Console Enhancements reports
- [ ] Structured data kept in sync with visible content
- [ ] SameAs properties linking to official social profiles

### 3.7 International SEO (if applicable)
- [ ] Hreflang tags implemented correctly
- [ ] Return hreflang tags present (bidirectional)
- [ ] x-default hreflang specified
- [ ] Language/region targeting configured in Search Console
- [ ] Content is genuinely localized (not just translated)

---

## 4. E-E-A-T Guidelines

E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) is Google's quality evaluation framework used by Search Quality Raters. While not a direct ranking factor, it influences how Google's systems assess content quality. **Trust is the most important pillar** — without it, the others are meaningless.

### 4.1 Experience

Demonstrates the author has firsthand, real-world involvement with the topic.

**How to demonstrate:**
- [ ] Publish real-world case studies with concrete outcomes and timelines
- [ ] Include original photos, screenshots, videos, or process diagrams
- [ ] Share personal anecdotes and insider details only someone involved would know
- [ ] Show product usage duration, testing methodology, and honest pros/cons
- [ ] Include behind-the-scenes content showing actual project delivery
- [ ] Add timestamps and date references showing ongoing involvement

### 4.2 Expertise

Demonstrates depth, accuracy, and clarity of knowledge on the topic.

**How to demonstrate:**
- [ ] Create in-depth guides explaining both "what" and "why"
- [ ] Use correct technical terminology with clear explanations
- [ ] Support claims with credible citations and primary sources
- [ ] Author bios include credentials, years of experience, education, specialization
- [ ] Link author profiles to LinkedIn or verified professional pages
- [ ] Address edge cases, compare approaches, explain misconceptions
- [ ] Update content regularly to reflect industry changes
- [ ] Publish comprehensive resources (whitepapers, long-form tutorials)

### 4.3 Authoritativeness

External recognition and reputation validation from the broader industry.

**How to demonstrate:**
- [ ] Earn backlinks from reputable, relevant websites (quality over quantity)
- [ ] Secure mentions on authoritative platforms (linked and unlinked)
- [ ] Gain press coverage and industry citations from credible publications
- [ ] Contribute guest posts to respected outlets
- [ ] Appear in interviews, podcasts, or speaking engagements
- [ ] Publish original research or proprietary data that others reference
- [ ] Build topical content clusters showing sustained leadership in a niche

### 4.4 Trustworthiness

Accuracy, transparency, and reliability — the foundational pillar.

**How to demonstrate:**
- [ ] Cite primary sources and official documentation
- [ ] Link to high-authority websites supporting claims
- [ ] Fact-check before publishing; correct mistakes openly
- [ ] Avoid exaggerated claims without full support
- [ ] Proactively update outdated information
- [ ] Explain limitations rather than overpromising certainty
- [ ] Maintain clear "About Us," contact information, and author disclosures
- [ ] Display legal pages (Privacy Policy, Terms of Service, Cookie Policy)
- [ ] Ensure HTTPS, fast load times, and mobile-friendliness
- [ ] Implement structured data (Author, Person, Organization schema)
- [ ] Monitor and respond professionally to reviews and brand mentions

### 4.5 YMYL (Your Money or Your Life)

Topics that can significantly impact a person's health, financial stability, safety, or well-being receive the **highest level of E-E-A-T scrutiny**. These include:

- Health and medical information
- Financial advice and services
- Legal information
- News and current events
- Civic, government, and legal processes
- Safety-related information

For YMYL content, ensure expert authorship, rigorous sourcing, and transparent disclosures.

### 4.6 Common E-E-A-T Misconceptions

- E-E-A-T is NOT a direct ranking factor — it is an evaluative lens over existing signals
- E-E-A-T cannot be built quickly — it compounds over time through consistency
- AI content is not automatically penalized — low-effort, generic content is the problem
- More backlinks alone do not equal higher E-E-A-T — quality and relevance matter more
- E-E-A-T requires ongoing maintenance — trust erodes if content becomes outdated

---

## 5. Mobile-First Indexing Requirements

Google uses the **mobile version of every website** as the primary input for its search index (100% rollout completed in 2024). All sites are evaluated by mobile Googlebot first.

### 5.1 Design Requirements
- [ ] Responsive web design implemented (single URL, same HTML, adapts to all screen sizes)
- [ ] No separate mobile site (m.domain.com) unless properly configured with bidirectional annotations
- [ ] Touch-friendly navigation (tap targets at least 48x48 CSS pixels)
- [ ] Readable font sizes without zooming (minimum 16px base font)
- [ ] No horizontal scrolling required
- [ ] No intrusive interstitials or pop-ups blocking content on mobile

### 5.2 Content Parity
- [ ] Mobile and desktop versions contain identical primary content
- [ ] Same metadata (title tags, meta descriptions) on both versions
- [ ] Same structured data on both versions
- [ ] Same alt text on images across both versions
- [ ] Lazy-loaded content is accessible to Googlebot (use Intersection Observer, not scroll-based triggers)

### 5.3 Technical Requirements
- [ ] Same `robots` meta tags on mobile and desktop versions
- [ ] Resources (CSS, JS, images) not blocked from Googlebot mobile
- [ ] Mobile pages load within Core Web Vitals thresholds
- [ ] Mobile sitemap submitted (or unified sitemap covering mobile-friendly pages)
- [ ] Viewport meta tag configured: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] Test with Google's Mobile-Friendly Test tool
- [ ] Check Mobile Usability report in Search Console

### 5.4 Performance on Mobile
- [ ] LCP under 2.5 seconds on mobile (3G/4G network conditions)
- [ ] Images optimized for mobile bandwidth (responsive images with `srcset`)
- [ ] Critical CSS inlined for above-the-fold content
- [ ] Third-party scripts deferred or loaded conditionally
- [ ] Service worker implemented for repeat visit performance (optional but recommended)

---

## 6. AI Search Optimization

In 2026, search discovery happens across three ecosystems simultaneously:
1. **Traditional search** (Google organic) — SEO determines visibility
2. **AI-powered search** (Google AI Overviews, Perplexity, Gemini) — Generative Engine Optimization (GEO) determines citations
3. **AI assistants** (ChatGPT, Claude, Copilot) — Answer Engine Optimization (AEO) determines recommendations

### 6.1 Impact of AI Overviews
- AI Overviews appear in approximately 4.5–12.5% of search queries
- They reduce organic clicks on the top result by an average of 34.5%
- Informational queries are most affected
- Featured snippet content is frequently sourced for AI Overviews

### 6.2 AI Crawler Access
- [ ] Review `robots.txt` for AI crawler directives
- [ ] Ensure GPTBot (OpenAI), Google-Extended (Gemini), ClaudeBot (Anthropic), and other AI crawlers are **not blocked** if you want AI search visibility
- [ ] If blocking AI crawlers, do so intentionally with documented reasoning
- [ ] Monitor AI crawler activity in server logs

### 6.3 Content Optimization for AI Citations
- [ ] Write clear, concise answers to questions in the first 30% of content (44.2% of LLM citations come from the intro)
- [ ] Use structured formats: numbered lists, tables, definition blocks
- [ ] Include direct question-and-answer patterns (Q&A format)
- [ ] Provide factual, data-backed statements with cited sources
- [ ] Write in a neutral, encyclopedic tone for factual content
- [ ] Include comprehensive coverage (AI models favor depth)
- [ ] Use FAQ sections with clear, standalone answers
- [ ] Ensure content readability is high (short sentences, clear structure)

### 6.4 Structured Data for AI
- [ ] Implement FAQ schema for question-answer content
- [ ] Use HowTo schema for instructional content
- [ ] Maintain accurate Organization and Author schema
- [ ] Implement Speakable schema for content suitable for voice/audio playback
- [ ] Use clear, semantic HTML (article, section, nav, header, main, footer)

### 6.5 Brand Visibility in AI Responses
- [ ] Build topical authority through content clusters
- [ ] Earn citations on Wikipedia, industry directories, and authoritative publications
- [ ] Publish original research and proprietary data
- [ ] Maintain consistent NAP (Name, Address, Phone) across the web
- [ ] Monitor AI search results for brand mentions and accuracy
- [ ] Create "About" and author pages with comprehensive entity information

### 6.6 Generative Engine Optimization (GEO) Tactics
- [ ] Optimize for conversational, long-tail queries
- [ ] Structure content to directly answer "People Also Ask" queries
- [ ] Include comparison tables and data visualizations
- [ ] Ensure your site is cited in existing AI Overviews (monitor with third-party tools)
- [ ] Build entity associations (be mentioned alongside related authoritative entities)
- [ ] Provide unique perspectives and original insights (AI models de-prioritize generic content)

---

## 7. Sources

1. [Core Web Vitals Explained: LCP, INP & CLS (2026)](https://www.corewebvitals.io/core-web-vitals) — Comprehensive thresholds and metric definitions
2. [How Core Web Vitals Thresholds Were Defined — web.dev (Google)](https://web.dev/articles/defining-core-web-vitals-thresholds) — Official methodology behind CWV thresholds
3. [Google E-E-A-T Guidelines: An Overview (2026 Playbook) — Keywords Everywhere](https://keywordseverywhere.com/blog/google-e-e-a-t-guidelines-an-overview/) — Detailed E-E-A-T framework and actionable steps
4. [Google Search Quality Rater Guidelines — E-A-T Gets Extra E for Experience](https://developers.google.com/search/blog/2022/12/google-raters-guidelines-e-e-a-t) — Official Google announcement of E-E-A-T
5. [Technical SEO Checklist 2026: What Really Matters — NoGood](https://nogood.io/blog/technical-seo-checklist/) — Comprehensive technical SEO audit categories
6. [Mobile-First Indexing Best Practices — Google Search Central](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) — Official Google documentation on mobile-first requirements
7. [The 2026 SEO Playbook: How AI Is Reshaping Search — Clearscope](https://www.clearscope.io/blog/2026-seo-aeo-playbook) — AI search optimization strategies
8. [Benchmarking the Future of AI Search: 2026 Insights — Search Engine Journal](https://www.searchenginejournal.com/ai-search-benchmark-every-seo-leader-needs/561301/) — AI Overviews impact data and citation statistics
9. [100+ AI SEO Statistics for 2026 — Position Digital](https://www.position.digital/blog/ai-seo-statistics/) — Current AI search statistics and benchmarks
10. [Core Web Vitals 2026: INP, LCP & CLS Optimization — Digital Applied](https://www.digitalapplied.com/blog/core-web-vitals-2026-inp-lcp-cls-optimization-guide) — CWV optimization strategies
