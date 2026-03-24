# Site Audit Best Practices Reference

> Reference material for the site-audit skill. Covers performance (Core Web Vitals),
> accessibility (WCAG 2.2), mobile responsiveness, SEO, UX, and broken link auditing.

---

## Table of Contents

1. [Performance — Core Web Vitals](#1-performance--core-web-vitals)
2. [Accessibility — WCAG 2.2](#2-accessibility--wcag-22)
3. [Mobile Responsiveness](#3-mobile-responsiveness)
4. [SEO Audit Checklist](#4-seo-audit-checklist)
5. [UX Audit Checklist](#5-ux-audit-checklist)
6. [Broken Link Audit](#6-broken-link-audit)
7. [Security Basics](#7-security-basics)
8. [Scoring Methodology](#8-scoring-methodology)
9. [Audit Tools Reference](#9-audit-tools-reference)
10. [Audit Frequency and Process](#10-audit-frequency-and-process)

---

## 1. Performance — Core Web Vitals

### The Three Core Web Vitals (2025/2026)

Google evaluates all three metrics at the **75th percentile** of real visitor data.
All three must pass at the 75th percentile for a page to achieve an overall "good" assessment.

#### LCP — Largest Contentful Paint (Loading Speed)

Measures how quickly the largest visible content element loads.

| Rating | Threshold | Action |
|--------|-----------|--------|
| Good | Under 2.5 seconds | No action needed |
| Needs Improvement | 2.5 - 4.0 seconds | Optimize — see fixes below |
| Poor | Over 4.0 seconds | Urgent fix required |

**Common LCP Elements**: Hero images, large text blocks, video poster images, background images.

**Optimization Checklist**:
- [ ] Optimize and compress images (WebP/AVIF format)
- [ ] Implement responsive images with `srcset`
- [ ] Preload the LCP image/resource (`<link rel="preload">`)
- [ ] Use a CDN for static assets
- [ ] Minimize render-blocking CSS and JavaScript
- [ ] Optimize server response time (TTFB under 800ms)
- [ ] Set appropriate cache headers
- [ ] Use font-display: swap for web fonts
- [ ] Inline critical CSS
- [ ] Defer non-critical JavaScript

#### INP — Interaction to Next Paint (Responsiveness)

Measures how quickly the page responds to user interactions (clicks, taps, key presses).
Replaced FID (First Input Delay) in March 2024.

| Rating | Threshold | Action |
|--------|-----------|--------|
| Good | Under 200ms | No action needed |
| Needs Improvement | 200 - 500ms | Optimize |
| Poor | Over 500ms | Urgent fix required |

**Optimization Checklist**:
- [ ] Break up long JavaScript tasks (> 50ms) into smaller chunks
- [ ] Use `requestIdleCallback` for non-urgent work
- [ ] Minimize main thread blocking
- [ ] Defer non-critical third-party scripts
- [ ] Use web workers for heavy computation
- [ ] Optimize event handlers (debounce/throttle where appropriate)
- [ ] Reduce DOM size (aim for under 1,500 elements)
- [ ] Minimize style recalculations triggered by JavaScript
- [ ] Use CSS `content-visibility: auto` for off-screen content

#### CLS — Cumulative Layout Shift (Visual Stability)

Measures unexpected layout shifts during page loading and interaction.

| Rating | Threshold | Action |
|--------|-----------|--------|
| Good | Under 0.1 | No action needed |
| Needs Improvement | 0.1 - 0.25 | Optimize |
| Poor | Over 0.25 | Urgent fix required |

**Optimization Checklist**:
- [ ] Set explicit `width` and `height` on all images and videos
- [ ] Use `aspect-ratio` CSS property for responsive media
- [ ] Reserve space for ads and embeds before they load
- [ ] Avoid inserting content above existing content dynamically
- [ ] Use `font-display: optional` or preload fonts to prevent FOUT shifts
- [ ] Avoid late-loading CSS that changes layout
- [ ] Use `transform` animations instead of layout-triggering properties
- [ ] Preconnect to required origins for third-party embeds

### Additional Performance Metrics

| Metric | Good Threshold | What It Measures |
|--------|---------------|-----------------|
| TTFB (Time to First Byte) | Under 800ms | Server response time |
| FCP (First Contentful Paint) | Under 1.8s | First visible content |
| Speed Index | Under 3.4s | How quickly content is visually populated |
| TTI (Time to Interactive) | Under 3.8s | When page becomes fully interactive |
| Total Blocking Time | Under 200ms | Sum of long task blocking time |

### Performance Testing Commands

```bash
# Run Lighthouse via CLI
npx lighthouse https://example.com --output=json --output-path=./lighthouse-report.json

# Run Lighthouse for specific categories
npx lighthouse https://example.com --only-categories=performance

# Check page load time
curl -o /dev/null -s -w "Total time: %{time_total}s\nTTFB: %{time_starttransfer}s\n" https://example.com

# Check resource sizes
curl -sI https://example.com | grep -i content-length
```

---

## 2. Accessibility — WCAG 2.2

### Overview

WCAG 2.2 (October 2023) is the current standard. It contains **87 success criteria** organized
around four principles: **POUR** — Perceivable, Operable, Understandable, Robust.

Most regulations require **Level AA** conformance. Automated tools catch only **30-57%** of issues —
manual testing is essential.

### Perceivable

Content must be presentable in ways all users can perceive.

#### Images and Non-Text Content
- [ ] All images have meaningful `alt` text (not "image1.jpg" or empty for decorative)
- [ ] Decorative images have `alt=""` or are CSS backgrounds
- [ ] Complex images (charts, infographics) have extended descriptions
- [ ] Icons used as controls have accessible labels
- [ ] CAPTCHAs have alternatives (audio, logic puzzles)

#### Text and Typography
- [ ] Text contrast ratio meets 4.5:1 minimum (3:1 for large text 18pt+)
- [ ] Non-text elements (icons, borders, form controls) meet 3:1 contrast
- [ ] Text can be resized to 200% without loss of content or function
- [ ] Content reflows at 320px width without horizontal scrolling (1.4.10 Reflow)
- [ ] Content remains functional when users adjust text spacing (1.4.12)

#### Multimedia
- [ ] Videos have synchronized captions (prerecorded and live)
- [ ] Audio descriptions are available for video when visual info is important
- [ ] Audio-only content has text transcripts
- [ ] No auto-playing media with sound (or easy mechanism to stop)

### Operable

Users must be able to operate the interface.

#### Keyboard Accessibility
- [ ] All functionality works via keyboard alone
- [ ] No keyboard traps (user can always tab away from any element)
- [ ] Focus order is logical and follows visual order
- [ ] Focus indicator is visible on all interactive elements (2.4.7)
- [ ] Focused elements aren't hidden behind sticky headers/banners (2.4.11 — most common WCAG 2.2 failure)
- [ ] Skip navigation link is present and functional

#### Timing and Motion
- [ ] Time limits can be extended or turned off
- [ ] Auto-moving content can be paused, stopped, or hidden
- [ ] No content flashes more than 3 times per second
- [ ] Motion-based interactions have alternatives (2.5.4)

#### Navigation
- [ ] At least two ways to find pages (nav, search, sitemap)
- [ ] Page titles are descriptive and unique
- [ ] Link purpose is clear from link text (no "click here")
- [ ] Headings and labels are descriptive

#### Pointer and Touch (WCAG 2.2 New)
- [ ] Dragging actions have single-pointer alternatives (2.5.7)
- [ ] Touch targets are at least 24x24 CSS pixels (2.5.8)
- [ ] Multi-point gestures have single-point alternatives (2.5.1)
- [ ] Actions trigger on pointer up, not down (2.5.2)

### Understandable

Content and interface must be understandable.

#### Language and Readability
- [ ] Page language is set via `lang` attribute on `<html>`
- [ ] Content in different languages is marked with appropriate `lang`
- [ ] Writing is clear and concise (aim for 8th-grade reading level)

#### Predictability
- [ ] Navigation is consistent across pages (3.2.3)
- [ ] Elements with same function are identified consistently (3.2.4)
- [ ] No unexpected context changes on focus or input
- [ ] Help information appears consistently across pages (3.2.6)

#### Input Assistance
- [ ] Form errors are clearly identified with suggestions (3.3.3)
- [ ] Labels and instructions are provided for form inputs
- [ ] Sensitive submissions can be reviewed/confirmed/reversed (3.3.4)
- [ ] Previously entered info is auto-populated (3.3.7 Redundant Entry)
- [ ] Authentication doesn't require cognitive tests (3.3.8) — allow copy/paste, password managers

### Robust

Content must work with assistive technologies.

- [ ] HTML validates without critical errors
- [ ] ARIA roles, states, and properties are used correctly
- [ ] Custom components have proper `role`, `name`, and `value`
- [ ] Status messages are announced via ARIA live regions (4.1.3)
- [ ] Dynamic content updates are announced to screen readers

### Accessibility Testing Approach

1. **Automated scan** — axe DevTools, WAVE, Lighthouse accessibility audit (catches 30-57%)
2. **Keyboard-only navigation** — Tab through entire site without mouse
3. **Screen reader test** — VoiceOver (Mac), NVDA (Windows), or JAWS
4. **Visual inspection** — Zoom to 200%, check contrast, check focus indicators
5. **Color-blind simulation** — Verify content isn't conveyed by color alone
6. **Mobile test** — Test with mobile screen reader (VoiceOver iOS, TalkBack Android)

---

## 3. Mobile Responsiveness

### Essential Checks

#### Viewport Configuration
- [ ] Viewport meta tag is present: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] Page doesn't use `maximum-scale=1` or `user-scalable=no` (blocks pinch zoom — accessibility violation)
- [ ] Content fits within viewport without horizontal scrolling

#### Responsive Design
- [ ] Layout adapts at all common breakpoints (320px, 375px, 414px, 768px, 1024px, 1440px)
- [ ] Images scale properly and don't overflow containers
- [ ] Tables are responsive (scrollable, stackable, or reformatted)
- [ ] Navigation is usable on mobile (hamburger menu, off-canvas, or bottom nav)
- [ ] Fonts are readable without zooming (minimum 16px body text)
- [ ] No fixed-width elements that break on small screens

#### Touch Targets
- [ ] Interactive elements are at least 44x44px (Apple) / 48x48dp (Material Design)
- [ ] Adequate spacing between touch targets (8px minimum gap)
- [ ] No hover-only interactions (must work on tap)
- [ ] No reliance on right-click or long-press without alternatives

#### Mobile-Specific UX
- [ ] Phone numbers are tappable (`tel:` links)
- [ ] Email addresses are tappable (`mailto:` links)
- [ ] Maps/addresses link to native maps app
- [ ] Forms use appropriate input types (`type="email"`, `type="tel"`, `type="number"`)
- [ ] Autocomplete attributes are set on form fields
- [ ] Content doesn't require landscape orientation exclusively

#### Mobile Performance
- [ ] Images serve mobile-optimized sizes (not desktop images scaled down)
- [ ] Lazy loading is implemented for below-fold images
- [ ] Third-party scripts don't block mobile rendering
- [ ] Page weight under 3MB for mobile connections
- [ ] Test on real 3G/4G connection speeds

### Testing Methods

```bash
# Check viewport meta tag
curl -s https://example.com | grep -i viewport

# Test with Lighthouse mobile
npx lighthouse https://example.com --preset=desktop
npx lighthouse https://example.com  # default is mobile

# Check page weight
curl -sI https://example.com | grep -i content-length
```

- Chrome DevTools device emulation (toggle device toolbar)
- BrowserStack or LambdaTest for real device testing
- Google Mobile-Friendly Test

---

## 4. SEO Audit Checklist

### Technical SEO

#### Crawlability
- [ ] `robots.txt` is accessible and correctly configured
- [ ] XML sitemap exists, is valid, and submitted to Google Search Console
- [ ] No unintentional `noindex` tags blocking important pages
- [ ] No unintentional `nofollow` on internal links
- [ ] Crawl budget is not wasted on low-value pages
- [ ] Google Search Console shows no critical crawl errors

#### Indexation
- [ ] Important pages are indexed (check `site:domain.com` in Google)
- [ ] Duplicate pages have proper canonical tags
- [ ] Pagination uses `rel="next"` / `rel="prev"` or is handled properly
- [ ] URL parameters are handled (Google Search Console parameter tool)
- [ ] No orphan pages (every page reachable via internal links)

#### Site Architecture
- [ ] Logical URL structure (human-readable, keyword-relevant)
- [ ] Important pages are within 3 clicks of homepage
- [ ] Breadcrumb navigation is implemented
- [ ] Clean URL structure (no unnecessary parameters)
- [ ] Consistent URL format (trailing slash or not, www or not)

### On-Page SEO

#### Title Tags
- [ ] Every page has a unique title tag
- [ ] Titles are 50-60 characters (display limit)
- [ ] Primary keyword is included near the beginning
- [ ] Titles are compelling for click-through

#### Meta Descriptions
- [ ] Every page has a unique meta description
- [ ] Descriptions are 150-160 characters
- [ ] Include target keyword and call-to-action
- [ ] Accurately summarize page content

#### Heading Structure
- [ ] One H1 per page containing primary keyword
- [ ] Logical heading hierarchy (H1 > H2 > H3, no skipping levels)
- [ ] Headings are descriptive (not "Section 1" or "Read More")
- [ ] No headings used purely for styling

#### Content
- [ ] Content is original and provides unique value
- [ ] Content matches search intent (informational, navigational, transactional)
- [ ] Target keywords appear naturally in content
- [ ] Content is comprehensive for the topic
- [ ] Content is current and regularly updated

#### Images
- [ ] All images have descriptive alt text with keywords where natural
- [ ] Images are optimized (WebP/AVIF, compressed, proper dimensions)
- [ ] Images have descriptive file names (not `IMG_1234.jpg`)
- [ ] Image sitemaps are included if image-heavy site

#### Structured Data / Schema Markup
- [ ] Organization/Person schema on homepage
- [ ] Article schema on blog posts
- [ ] FAQ schema where applicable
- [ ] Product/Service schema where applicable
- [ ] BreadcrumbList schema for breadcrumbs
- [ ] Schema validates in Google Rich Results Test

### Off-Page Factors to Note

- [ ] Check backlink profile health (Google Search Console > Links)
- [ ] Identify any toxic or spammy backlinks
- [ ] Review Google Business Profile (if local business)
- [ ] Check social media profiles link back to website

---

## 5. UX Audit Checklist

### Navigation

- [ ] Primary navigation is clear and limited to 5-7 items
- [ ] Navigation labels use familiar, descriptive terms
- [ ] Current page is indicated in navigation
- [ ] Search is available and functional
- [ ] Footer contains secondary navigation and key links
- [ ] 404 page is helpful (suggestions, search, navigation)

### Content Readability

- [ ] Body text is minimum 16px
- [ ] Line height is 1.4-1.6x font size
- [ ] Line length is 50-75 characters (measure element width)
- [ ] Adequate contrast between text and background
- [ ] Content is broken into scannable chunks (short paragraphs, headings, lists)
- [ ] Important information is not buried in long text blocks

### Calls to Action (CTAs)

- [ ] Primary CTA is immediately visible (above the fold)
- [ ] CTA text is action-oriented ("Get Started" not "Submit")
- [ ] CTAs are visually distinct from other elements
- [ ] CTA placement follows natural reading flow
- [ ] Not too many competing CTAs on one page (1-2 primary)
- [ ] CTA is accessible on mobile

### Forms

- [ ] Forms are as short as possible (remove unnecessary fields)
- [ ] Labels are visible and associated with inputs (not placeholder-only)
- [ ] Required fields are clearly marked
- [ ] Error messages are specific and helpful (not "invalid input")
- [ ] Form validates in real-time where appropriate
- [ ] Success state is clear after submission
- [ ] Forms are mobile-friendly (appropriate input types, large tap targets)

### Trust Signals

- [ ] Professional design (no broken layouts, consistent styling)
- [ ] Contact information is easy to find
- [ ] Testimonials or reviews are displayed
- [ ] Certifications, awards, or credentials are visible
- [ ] Privacy policy and terms are linked
- [ ] HTTPS is enabled (padlock in browser)
- [ ] No broken images or placeholder content

### Page Speed Perception

- [ ] Page feels fast (content appears quickly even if full load takes longer)
- [ ] Loading states are shown for dynamic content (skeleton screens, spinners)
- [ ] No blank white screens during load
- [ ] Critical content loads first (above-the-fold prioritization)

---

## 6. Broken Link Audit

### Types of Broken Links

| Type | Description | Impact |
|------|-------------|--------|
| **404 errors** | Page not found | Bad UX, lost link equity |
| **500 errors** | Server errors | Bad UX, signals instability |
| **Redirect chains** | Multiple redirects (A > B > C) | Slower load, lost link equity |
| **Redirect loops** | Infinite redirects (A > B > A) | Page never loads |
| **Mixed content** | HTTP resources on HTTPS page | Security warnings |
| **Timeout** | Resource takes too long to respond | Bad UX |

### Audit Process

#### Step 1: Crawl the Site
```bash
# Using curl to check individual URLs
curl -o /dev/null -s -w "%{http_code}" https://example.com/page

# Check multiple URLs from a list
while read url; do
  status=$(curl -o /dev/null -s -w "%{http_code}" "$url")
  echo "$status $url"
done < urls.txt

# Check for redirect chains
curl -sIL https://example.com/old-page 2>&1 | grep -E "HTTP/|Location:"
```

#### Step 2: Check External Links
- Verify all outbound links return 200
- Check for links to sites that have gone down
- Verify no links point to HTTP when HTTPS is available
- Check for links to outdated content

#### Step 3: Check Internal Links
- Verify all navigation links work
- Check footer links
- Test links in content (blog posts, pages)
- Verify image sources load
- Check anchor links (scroll to section)

#### Step 4: Review Redirects
- [ ] No redirect chains longer than 2 hops
- [ ] All HTTP URLs redirect to HTTPS
- [ ] Old URLs redirect to new URLs (301, not 302)
- [ ] No redirect loops exist
- [ ] Redirects point to live pages (not to other redirects or 404s)

### Tools
- Screaming Frog SEO Spider (comprehensive crawler)
- Google Search Console > Pages report (shows crawl errors)
- Ahrefs / Semrush site audit tools
- W3C Link Checker (free online tool)

---

## 7. Security Basics

> For comprehensive security auditing, refer to the security-audit skill and its
> `references/best-practices.md`. This section covers the basics relevant to site audits.

### Quick Security Checks

- [ ] HTTPS is enforced sitewide (HTTP redirects to HTTPS)
- [ ] No mixed content warnings (HTTP resources on HTTPS pages)
- [ ] SSL certificate is valid and not expiring soon
- [ ] Security headers are present (HSTS, CSP, X-Content-Type-Options, X-Frame-Options)
- [ ] No exposed sensitive paths (`/.git/`, `/.env`, `/wp-admin/`, `/phpinfo.php`)
- [ ] Admin panels are not publicly accessible
- [ ] Contact forms have spam protection (CAPTCHA, honeypot)
- [ ] No sensitive information in HTML source (API keys, comments with credentials)
- [ ] Cookie security flags are set (Secure, HttpOnly, SameSite)

### Security Header Quick Check

```bash
curl -I -s https://example.com | grep -iE "^(strict-transport|content-security|x-frame|x-content-type|referrer-policy|permissions-policy)"
```

---

## 8. Scoring Methodology

### Category Scoring (1-10)

Score each audit category on a 1-10 scale based on the criteria below.

#### Performance Score

| Score | Criteria |
|-------|----------|
| 9-10 | All Core Web Vitals "Good". Lighthouse performance 90+. |
| 7-8 | All CWV "Good" or "Needs Improvement". Lighthouse 70-89. |
| 5-6 | One CWV "Poor", others acceptable. Lighthouse 50-69. |
| 3-4 | Multiple CWV "Poor". Lighthouse 30-49. |
| 1-2 | All CWV "Poor". Lighthouse under 30. Major performance issues. |

#### Accessibility Score

| Score | Criteria |
|-------|----------|
| 9-10 | Passes automated scan with 0 errors. Keyboard nav works. Screen reader tested. |
| 7-8 | Minor automated issues (< 5). Keyboard nav mostly works. |
| 5-6 | Moderate issues (5-15). Some keyboard traps or missing labels. |
| 3-4 | Significant issues (15-30). Major keyboard or screen reader barriers. |
| 1-2 | Critical failures. Site unusable without mouse. Missing alt text throughout. |

#### Mobile Responsiveness Score

| Score | Criteria |
|-------|----------|
| 9-10 | Perfect rendering on all devices. Touch targets appropriate. No horizontal scroll. |
| 7-8 | Minor issues on edge devices. Generally good mobile experience. |
| 5-6 | Some elements broken on mobile. Usable but suboptimal. |
| 3-4 | Significant mobile issues. Content cut off or overlapping. |
| 1-2 | Site is not mobile-responsive. Desktop-only layout. |

#### SEO Score

| Score | Criteria |
|-------|----------|
| 9-10 | All technical SEO checks pass. Complete meta tags. Schema markup. Clean architecture. |
| 7-8 | Minor gaps (few missing meta descriptions, some heading issues). |
| 5-6 | Moderate gaps (missing sitemaps, several pages without proper meta). |
| 3-4 | Significant SEO issues (crawl errors, duplicate content, no schema). |
| 1-2 | Major SEO failures (site not indexed, robots.txt blocking, no HTTPS). |

#### UX Score

| Score | Criteria |
|-------|----------|
| 9-10 | Intuitive navigation. Clear CTAs. Fast perceived speed. Trust signals present. |
| 7-8 | Good UX with minor friction points. |
| 5-6 | Usable but noticeable UX issues (confusing nav, unclear CTAs). |
| 3-4 | Significant UX problems. Users likely to bounce. |
| 1-2 | Poor UX. Broken elements, confusing layout, no clear purpose. |

#### Broken Links Score

| Score | Criteria |
|-------|----------|
| 9-10 | Zero broken links. Clean redirect map. |
| 7-8 | 1-5 broken links, no critical pages affected. |
| 5-6 | 6-15 broken links, some in navigation or key content. |
| 3-4 | 16-30 broken links, including key pages. Redirect chains present. |
| 1-2 | 30+ broken links. Navigation links broken. Redirect loops. |

### Overall Site Score

Calculate weighted average:

```
Overall = (Performance x 0.20) + (Accessibility x 0.20) + (Mobile x 0.15) +
          (SEO x 0.20) + (UX x 0.15) + (Links x 0.05) + (Security x 0.05)
```

Weights reflect relative importance for a personal brand website. Adjust based
on specific site priorities.

---

## 9. Audit Tools Reference

### Free Tools

| Tool | Category | URL |
|------|----------|-----|
| Google Lighthouse | Performance, SEO, Accessibility | Built into Chrome DevTools |
| Google PageSpeed Insights | Core Web Vitals, Performance | pagespeed.web.dev |
| Google Search Console | SEO, Indexation, Errors | search.google.com/search-console |
| Google Mobile-Friendly Test | Mobile Responsiveness | search.google.com/test/mobile-friendly |
| Google Rich Results Test | Structured Data | search.google.com/test/rich-results |
| Mozilla Observatory | Security Headers | observatory.mozilla.org |
| SSL Labs | SSL/TLS | ssllabs.com/ssltest |
| WAVE | Accessibility | wave.webaim.org |
| axe DevTools | Accessibility | Chrome/Firefox extension |
| W3C Markup Validator | HTML Validity | validator.w3.org |
| SecurityHeaders.com | Security Headers | securityheaders.com |

### CLI Tools

```bash
# Lighthouse CLI
npx lighthouse https://example.com --output=html --output-path=./report.html

# Pa11y (accessibility)
npx pa11y https://example.com

# axe CLI
npx @axe-core/cli https://example.com

# Broken link checker
npx broken-link-checker https://example.com --recursive
```

### Paid Tools (for Reference)

| Tool | Best For |
|------|----------|
| Screaming Frog | Comprehensive site crawling |
| Ahrefs | SEO + backlinks |
| Semrush | SEO + competitive analysis |
| DebugBear | Core Web Vitals monitoring |
| BrowserStack | Cross-device testing |

---

## 10. Audit Frequency and Process

### Recommended Schedule

| Audit Type | Frequency | Trigger |
|------------|-----------|---------|
| Full site audit | Quarterly | Scheduled |
| Performance check | Monthly | Scheduled |
| Broken link scan | Monthly | Scheduled |
| Security basics | Monthly | Scheduled |
| Post-deployment audit | After every deploy | Event-driven |
| Accessibility review | Quarterly + after major changes | Scheduled + event |
| SEO review | Monthly | Scheduled |

### Audit Process

1. **Baseline**: Run automated tools first (Lighthouse, WAVE, Observatory)
2. **Manual review**: Walk through site as a user on desktop and mobile
3. **Document**: Record all findings with evidence (screenshots, scores, URLs)
4. **Classify**: Assign severity to each finding (critical / high / medium / low)
5. **Prioritize**: Use impact vs effort matrix to order fixes
6. **Report**: Write findings with specific remediation steps
7. **Track**: Compare against previous audit to measure improvement
8. **Follow up**: Verify fixes were implemented correctly

### Priority Matrix

| | High Impact | Low Impact |
|---|-----------|-----------|
| **Easy Fix** | Do first | Do soon |
| **Hard Fix** | Plan and schedule | Backlog |

---

## Sources

- [The Complete Website Audit Checklist for 2026 — Red Rattler Creative](https://redrattlercreative.com/complete-website-audit-checklist-2026/)
- [The Ultimate Website Audit Checklist — ThrillX Design](https://thrillxdesign.com/the-ultimate-website-audit-checklist/)
- [Core Web Vitals — corewebvitals.io](https://www.corewebvitals.io/core-web-vitals)
- [Core Web Vitals 2026: INP, LCP & CLS — Digital Applied](https://www.digitalapplied.com/blog/core-web-vitals-2026-inp-lcp-cls-optimization-guide)
- [WCAG 2.2 Checklist: Complete 2026 Guide — Level Access](https://www.levelaccess.com/blog/wcag-2-2-aa-summary-and-checklist-for-website-owners/)
- [WebAIM WCAG 2 Checklist](https://webaim.org/standards/wcag/checklist)
- [WCAG 2.2 Checklist 2026: All 87 Criteria — Web Accessibility Checker](https://web-accessibility-checker.com/en/blog/wcag-2-2-checklist-2026)
- [Understanding Core Web Vitals — Google](https://developers.google.com/search/docs/appearance/core-web-vitals)
- [The Ultimate Technical SEO Checklist for 2026 — The HOTH](https://www.thehoth.com/blog/seo-technical-checklist/)
- [Website Audit Checklist 2026 — WebUpon](https://webupon.com/blog/website-audit-checklist/)
