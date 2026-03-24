# Compliance Best Practices Reference

> Last updated: 2026-03-24
> This document is the regulatory reference for the compliance-audit skill.
> Cross-referenced from 3+ sources per regulation. See Sources at bottom.

---

## 1. GDPR (General Data Protection Regulation)

### Applicability
Applies to any entity that collects or processes personal data of EU/EEA residents, regardless of where the entity is located.

### Six Lawful Bases for Processing
Every data processing activity must be mapped to exactly one lawful basis:

1. **Consent** -- Freely given, specific, informed, and unambiguous. Must be as easy to withdraw as to give. Cannot be bundled with other terms. Pre-ticked boxes are invalid.
2. **Contract** -- Processing necessary to fulfill or enter into a contract with the data subject.
3. **Legal obligation** -- Processing necessary to comply with a legal obligation (e.g., tax reporting).
4. **Vital interests** -- Processing necessary to protect someone's life (narrow use).
5. **Public task** -- Processing necessary for a task carried out in the public interest.
6. **Legitimate interests** -- Processing necessary for legitimate interests of the controller, balanced against the data subject's rights. Requires a documented Legitimate Interest Assessment (LIA).

### Consent Requirements
- Must be a clear affirmative action (opt-in, not opt-out)
- Must specify the purpose of each processing activity
- Must be granular -- separate consent for separate purposes
- Must be documented and auditable
- Withdrawal must be as easy as giving consent
- Cannot condition service on unnecessary consent (no "consent walls")
- Parental consent required for children under 16 (or 13 in some member states)

### Data Subject Rights
Organizations must facilitate these rights within one month (extendable to three months for complex requests):

| Right | Description |
|-------|-------------|
| Access | Provide copy of personal data and processing details |
| Rectification | Correct inaccurate data without undue delay |
| Erasure ("right to be forgotten") | Delete data when no longer necessary, consent withdrawn, or unlawful processing |
| Restriction | Limit processing while accuracy is contested or processing is unlawful |
| Data portability | Provide data in machine-readable format for transfer to another controller |
| Object | Object to processing based on legitimate interests or direct marketing |
| Automated decision-making | Not be subject to decisions based solely on automated processing with legal effects |
| Withdraw consent | Withdraw consent at any time |

### Data Protection Officer (DPO)
Mandatory when:
- Organization is a public authority
- Core activities involve large-scale systematic monitoring of individuals
- Core activities involve large-scale processing of special category data

### Data Protection Impact Assessment (DPIA)
Required before processing that is likely to result in high risk, including:
- Large-scale processing of sensitive data
- Systematic monitoring of public areas
- AI-driven profiling or automated decision-making
- New technologies with unknown privacy impact

### Breach Notification
- **Supervisory authority:** Within 72 hours of becoming aware (unless unlikely to result in risk)
- **Data subjects:** Without undue delay when breach is likely to result in high risk to their rights

### Cross-Border Data Transfers
Transfers outside EEA require:
- Adequacy decision by European Commission, OR
- Standard Contractual Clauses (SCCs) with Transfer Impact Assessment, OR
- Binding Corporate Rules (BCRs), OR
- Explicit consent with informed acknowledgment of risks

### AI Processing Requirements (2026 Update)
The EU AI Act compliance deadline of August 2, 2026 creates dual obligations:
- AI systems require valid legal basis (typically legitimate interests after comprehensive assessment)
- Mandatory DPIAs for high-risk AI processing
- Human oversight for decisions producing significant effects
- Transparency about automated decision-making
- Verification that training data was lawfully obtained

### Penalties
- **Tier 1 (severe):** Up to EUR 20 million or 4% of worldwide annual turnover, whichever is higher. Applies to violations of basic principles (lawfulness, consent, data subject rights).
- **Tier 2 (administrative):** Up to EUR 10 million or 2% of worldwide annual turnover, whichever is higher. Applies to obligations like DPIA failures, DPO requirements, certification issues.

---

## 2. CAN-SPAM Act (Controlling the Assault of Non-Solicited Pornography And Marketing)

### Applicability
Applies to all commercial electronic mail messages sent to recipients in the United States, regardless of sender location. Both the company whose product is promoted and the company that sends the message can be held liable.

### Core Requirements

| Requirement | Details |
|-------------|---------|
| **Accurate header information** | "From," "To," "Reply-To," and routing information must be truthful. Sender identity must not be concealed. |
| **Honest subject lines** | Must accurately reflect the message content. No deceptive or misleading subjects. |
| **Commercial identification** | Message must clearly indicate it is an advertisement or solicitation. |
| **Physical postal address** | Must include a valid, current physical postal address of the sender (street address, PO Box, or registered private mailbox). |
| **Opt-out mechanism** | Every message must include a clear, conspicuous, easy-to-find way to opt out of future commercial email. Must be functional for at least 30 days after sending. |
| **10-business-day opt-out window** | Opt-out requests must be honored within 10 business days. Once opted out, cannot share or sell the email address to third parties. |
| **No opt-out fees or barriers** | Cannot require the recipient to pay, provide information beyond an email address, or take multiple steps beyond a single reply or single web page visit. |

### Third-Party Liability
- You cannot contract away legal responsibility by hiring another company for email marketing
- Both the promoting company and the sending company may be held liable
- Affiliate marketers sending on your behalf expose you to liability

### Transactional vs. Commercial Messages
- **Transactional messages** (order confirmations, account updates) are exempt from most CAN-SPAM rules but must not contain false routing information
- A message is "commercial" if its primary purpose is commercial advertisement or promotion
- Mixed-purpose messages: if the subject line would lead a recipient to think it is commercial, CAN-SPAM applies

### 2025-2026 Enforcement Trends
- Increased scrutiny of third-party affiliates and agencies
- Companies cannot claim plausible deniability for non-compliant emails sent on their behalf
- Penalty amount adjusted to up to $51,744 per violating email (2025 adjusted)
- No maximum cap on total fines

---

## 3. FTC Endorsement Guidelines

### Applicability
Applies to anyone promoting a product or service -- influencers, bloggers, content creators, celebrities, employees, and everyday users. Both the endorser and the brand/advertiser can be held liable.

### Material Connection -- What Must Be Disclosed
A "material connection" is any relationship that might affect the weight or credibility of an endorsement:
- Financial payment or compensation
- Free or discounted products/services
- Employment or consulting relationship
- Family or personal relationships with the brand
- Affiliate commissions or revenue sharing
- Brand ambassadorships or sponsorships
- Contest/sweepstakes entries tied to promotion
- Any other benefit received

### Disclosure Requirements -- Clear and Conspicuous

**General Rules:**
- Use plain, unambiguous language: "Ad," "Sponsored," "Paid partnership," "Thanks to [Brand] for the free product"
- Disclosure must be in the same language as the endorsement
- Must be hard to miss -- not buried in hashtags, fine print, or "more" folds
- Must appear with the endorsement itself, not on a separate page
- Abbreviations like "#sp" or vague terms like "#ambassador" are insufficient

**Platform-Specific Placement:**

| Platform | Placement Rules |
|----------|----------------|
| **Instagram/Facebook** | Before the "more" cutoff in captions. Use platform's "Paid partnership" tool when available. In Stories/Reels: superimpose text that is large and visible for adequate time. |
| **YouTube** | Both verbal (spoken in video) and written (description) disclosure. Use YouTube's paid promotion checkbox. Disclose within the video itself, not just in the description or pinned comments. |
| **TikTok** | Use built-in branded content toggle. Include verbal disclosure in video. Add #ad in description. Superimpose text disclosure on video content. |
| **Twitter/X** | Include disclosure in the tweet itself (not in a reply or thread). Use terms like "#Ad," "[Brand] Partner," or "[Brand] Ambassador." |
| **Podcasts/Audio** | State disclosure aloud at both beginning and end of the episode/segment. Spoken disclosure is essential. |
| **Livestreams** | Repeat disclosure periodically since viewers join at different times. |
| **Blog posts** | Disclosure at the top of the post, before any endorsement content. |

### Truthful Claims
- Cannot endorse a product you have not actually tried
- Cannot claim positive experience if your actual experience was negative
- Cannot make claims that require proof the advertiser does not have (e.g., health claims without scientific evidence)
- Testimonials must reflect typical consumer experience, or clearly disclose atypical results

### Fake Reviews Rule (Finalized August 2024)
- Bans creation or sale of fake reviews, including AI-generated reviews
- Bans buying fake followers or engagement to misrepresent influence
- Bans review suppression (selectively hiding negative reviews)
- Bans insider reviews without disclosure (employees reviewing their own products)
- Violations: up to $51,744 per incident

### AI-Generated Content Rules
- If AI tools create endorsement content, must disclose both: (1) the content is sponsored, AND (2) the content is AI-generated
- Deepfake videos, synthetic voices, and AI-generated likenesses require explicit disclosure
- Audiences must not be misled into thinking a real person provided the endorsement

### Notable Enforcement Cases
- **Google/iHeartMedia (2024):** ~29,000 deceptive endorsements, $9.4 million in penalties
- **Teami LLC:** Undisclosed influencer partnerships + false health claims, $930,000 restitution
- **CSGO Lotto:** Promoting gambling without disclosing ownership stakes

### Penalties
- Civil penalties up to $51,744 per violation (2025 adjusted amount)
- Both brands and endorsers face accountability
- FTC can pursue injunctive relief, consumer restitution, and disgorgement of profits

---

## 4. CCPA/CPRA (California Consumer Privacy Act / California Privacy Rights Act)

### Applicability Thresholds
For-profit businesses doing business in California meeting ANY one criterion:
- Annual gross revenue exceeding $26,625,000 (2025-2026 adjusted)
- Process personal information of 100,000+ California consumers/households/devices annually
- Derive 50%+ annual revenue from selling or sharing personal information

Applies regardless of business location if processing California residents' data.

### Consumer Rights

| Right | Description |
|-------|-------------|
| **Right to Know/Access** | Request details about what personal information is collected, used, shared, or sold. Extended lookback to January 1, 2022 for data subject access requests. |
| **Right to Delete** | Request deletion of personal information. Business must also direct service providers to delete. |
| **Right to Correct** | Fix inaccurate personal information. Business must notify original sources of correction. |
| **Right to Opt-Out** | Opt out of sale or sharing of personal information. Must honor Global Privacy Control (GPC) signals. |
| **Right to Limit** | Restrict use and disclosure of sensitive personal information to purposes necessary for the service. |
| **Right to Non-Discrimination** | Cannot deny goods/services, charge different prices, or provide different quality for exercising rights. |

### Business Obligations

**Privacy Policy Requirements:**
- Categories of personal information collected in the preceding 12 months
- Sources of personal information
- Business/commercial purpose for collection or selling
- Categories of third parties with whom PI is shared
- Specific pieces of personal information collected
- Retention periods for each category
- Consumer rights and how to exercise them

**Notice at Collection:**
- Must be provided at or before the point of data collection
- Must identify categories of PI being collected and purposes
- Must link to the full privacy policy

**Do Not Sell/Share:**
- Prominent "Do Not Sell or Share My Personal Information" link on website
- Must honor Global Privacy Control (GPC) browser signals
- "Choice symmetry" -- opt-out process must not be harder than opt-in
- Cannot default users into data-sharing programs
- Must provide visible confirmation of opt-out requests

**Data Minimization:**
- Limit collection to what is reasonably necessary for the disclosed purpose
- Cannot collect more than needed or use for incompatible purposes

### Sensitive Personal Information (SPI)
Special protections for:
- Social Security numbers, driver's license, passport numbers
- Financial account information (with credentials)
- Precise geolocation data
- Racial/ethnic origin
- Religious beliefs
- Health information
- Biometric data
- Contents of mail, email, or text messages (where business is not the intended recipient)
- Youth data (under 16) -- classified as SPI effective 2026

### Service Provider Requirements
Contracts must include:
- Prohibition on using PI outside contract scope
- Commitment to assist with consumer rights requests
- Requirement to honor consumer opt-outs
- Subcontractor flow-down requirements
- Reasonable security measures
- Annual compliance certifications

### 2026 Regulatory Updates (Effective January 1, 2026)
- Formal risk assessments for high-risk processing
- Automated Decision-Making Technology (ADMT) inventory and pre-use notices
- Youth data classified as SPI
- Cybersecurity audit requirements (phased filing: 2028-2030 based on revenue)
- Dark pattern prohibitions and consent management protocols
- Updated privacy policy disclosure standards

### Penalties
- Up to $2,500 per unintentional violation
- Up to $7,500 per intentional violation
- Up to $7,500 per violation involving minors under 16
- Statutory damages: $100-$750 per consumer per incident (data breach private right of action)
- No cap on total penalties

---

## 5. Platform Terms of Service -- Key Compliance Points

### Twitter/X

| Area | Requirement |
|------|-------------|
| **Content ownership** | Users retain ownership but grant X a broad license to use, modify, and distribute content |
| **Automation rules** | May automate content creation and scheduling; must NOT automate engagement (likes, follows, retweets, replies, DMs) |
| **Bot accounts** | Must clearly identify as a bot in profile bio |
| **Duplicate content** | Cannot post identical or substantially similar content across multiple accounts |
| **API access** | Basic tier minimum ($200/month) for production applications; pay-per-use beta launched Nov 2025 |
| **Spam** | Zero tolerance for bulk, automated, or spammy actions |
| **Trademark** | Cannot use X or Twitter trademarks without written consent (updated Jan 15, 2026) |
| **AI content** | AI-generated content is permitted but must not be used for automated engagement |

### YouTube

| Area | Requirement |
|------|-------------|
| **Content ownership** | Users retain ownership; grant YouTube a worldwide, non-exclusive, royalty-free license |
| **Monetization** | Must comply with YouTube Partner Program policies and advertiser-friendly content guidelines |
| **Paid promotion** | Must use YouTube's paid promotion disclosure checkbox; include verbal disclosure at video start |
| **Inauthentic content** | Renamed policy (July 2025): prohibits repetitive or mass-produced content |
| **Restricted categories** | Enhanced compliance documentation required for health, finance, legal content |
| **Copyright** | Three-strike copyright system; Content ID matching for music and video |
| **Community Guidelines** | Strike system for violations; severe violations can lead to immediate termination |

### Instagram

| Area | Requirement |
|------|-------------|
| **Content license** | Non-exclusive, royalty-free, transferable, sub-licensable, worldwide license (as of April 2025 ToS) |
| **Branded content** | Must use "Paid partnership with" tag for sponsored content |
| **Disclosure** | #ad or #sponsored in caption before "more" fold; use platform branded content tools |
| **Authenticity** | Authentic identity required; misrepresentation prohibited |
| **Special ad categories** | Enhanced requirements for housing, employment, and credit ads |
| **Community Guidelines** | Prohibition on hate speech, violence, nudity (with exceptions), spam, and misleading content |

### TikTok

| Area | Requirement |
|------|-------------|
| **Content license** | Broad license granted for platform use and distribution |
| **Branded content** | Must use built-in branded content toggle |
| **Disclosure** | Verbal disclosure in video + #ad in description; superimpose text disclosure |
| **Age restrictions** | Stricter content standards for younger audiences; age-gating for mature content |
| **Prohibited industries** | Restrictions on financial services, health products, gambling, political advertising |
| **Safety standards** | Content must meet community safety and wellbeing standards |
| **AI content** | Must label AI-generated or manipulated content |

### LinkedIn

| Area | Requirement |
|------|-------------|
| **Professional standards** | Content must maintain professional relevance; accurate professional information required |
| **Advertising** | Stricter claim substantiation for SaaS/software (2026 PTI framework) |
| **Ad format** | 600 char intro text limit; image max 20% text overlay for Sponsored Content |
| **Lead gen forms** | New data consent rules exceeding GDPR minimums |
| **Recruitment ads** | Enhanced anti-discrimination enforcement |
| **Endorsement disclosure** | Clear notice of any personal benefit received in exchange for endorsement |
| **Automated review** | 43% more ads rejected in Q1 2026 vs Q1 2025 under new PTI system |

### Medium

| Area | Requirement |
|------|-------------|
| **Content ownership** | Writers retain ownership; grant Medium license for platform display and distribution |
| **Original content** | Plagiarism is prohibited; copyright violations result in immediate removal with no appeal |
| **AI-generated content** | Majority AI-generated content is not eligible for paywalling/monetization (Partner Program) |
| **AI tools permitted** | AI outlining, AI-assisted fact-checking, spelling, and grammar tools are allowed |
| **Meta content** | Stories primarily about Medium/Partner Program are not eligible for monetization (effective April 1, 2025) |
| **Community rules** | No threats, violence, or hateful content based on protected characteristics |
| **Partner Program** | Must comply with all content policies to remain eligible for monetization |

---

## 6. Compliance Scoring Methodology

### Per-Area Rating Scale

| Rating | Definition | Criteria |
|--------|------------|----------|
| **Compliant** | Meets all requirements | All mandatory elements present and correctly implemented. No remediation needed. |
| **Partially Compliant** | Meets some but not all requirements | Core elements present but gaps exist. Minor to moderate risk. Remediation needed within 30-90 days. |
| **Non-Compliant** | Fails to meet requirements | Critical elements missing or incorrect. High risk of enforcement action. Immediate remediation required. |

### Severity Levels for Findings

| Severity | Description | Action Timeline |
|----------|-------------|-----------------|
| **Critical** | Immediate legal/financial risk. Active violation that could trigger enforcement. | Remediate within 7 days |
| **High** | Significant gap likely to result in violation if not addressed. | Remediate within 30 days |
| **Medium** | Gap that creates moderate risk; not currently in violation but vulnerable. | Remediate within 60 days |
| **Low** | Minor improvement opportunity; best practice not currently followed. | Remediate within 90 days |

### Overall Compliance Score Calculation

Score each audited area on a 0-100 scale:

| Score Range | Rating | Meaning |
|-------------|--------|---------|
| 90-100 | Excellent | Fully compliant across all areas; minor best-practice improvements only |
| 75-89 | Good | Substantially compliant; a few medium-severity gaps |
| 60-74 | Fair | Partially compliant; multiple gaps requiring attention |
| 40-59 | Poor | Significant non-compliance; high-severity issues present |
| 0-39 | Critical | Widespread non-compliance; immediate remediation required |

**Weighted scoring by risk:**
- Email marketing (CAN-SPAM): 15%
- Sponsored content (FTC): 20%
- Data collection (GDPR/CCPA): 25%
- Social media (Platform ToS): 15%
- Advertising claims (FTC): 15%
- Privacy policy & notices: 10%

The overall score is the weighted average of individual area scores.

---

## Sources

### FTC Endorsement Guidelines
- [FTC Endorsements, Influencers, and Reviews](https://www.ftc.gov/business-guidance/advertising-marketing/endorsements-influencers-reviews)
- [FTC Disclosures 101 for Social Media Influencers](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers)
- [FTC Endorsement Guides: What People Are Asking](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking)
- [inBeat Agency -- FTC Guidelines for Influencers 2025](https://inbeat.agency/blog/ftc-guidelines-for-influencers)
- [Termly -- FTC Requirements for Influencers](https://termly.io/resources/articles/ftc-requirements-for-influencers/)
- [Luthor AI -- Full Guide on FTC Influencer Guidelines](https://www.luthor.ai/blog-post/ftc-guidelines)

### GDPR
- [Formbricks -- GDPR Compliance Checklist 2026](https://formbricks.com/blog/gdpr-compliance-checklist-2025)
- [BitSight -- GDPR Compliance Checklist 2025](https://www.bitsight.com/learn/gdpr-compliance-checklist)
- [SecurityWall -- GDPR Compliance Checklist 2026](https://securitywall.co/blog/gdpr-compliance-checklist-2026-guide-templates-audit-steps)
- [Sprinto -- List of Key GDPR Requirements 2026](https://sprinto.com/blog/gdpr-requirements/)
- [Captain Compliance -- GDPR Compliance Checklist 2026](https://captaincompliance.com/education/gdpr-compliance-checklist/)

### CAN-SPAM
- [FTC -- CAN-SPAM Act Compliance Guide for Business](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)
- [Shopify -- Understanding the CAN-SPAM Act 2025](https://www.shopify.com/blog/can-spam-act)
- [Mailmodo -- Email Regulations 2026](https://www.mailmodo.com/guides/email-regulation/)
- [Termly -- CAN-SPAM Act Laws and Requirements](https://termly.io/resources/articles/can-spam-act/)

### CCPA/CPRA
- [SecurePrivacy -- CCPA Requirements 2026](https://secureprivacy.ai/blog/ccpa-requirements-2026-complete-compliance-guide)
- [Captain Compliance -- CPRA Compliance Checklist 2026](https://captaincompliance.com/education/cpra-compliance-checklist/)
- [Thompson Coburn -- California 2026 CCPA Regulations Summary](https://www.thompsoncoburn.com/insights/californias-2026-ccpa-regulations-summary-and-preparation-guide/)
- [Drata -- CCPA Compliance Checklist 2026](https://drata.com/blog/ccpa-compliance-checklist-2026)
- [Jackson Lewis -- CCPA FAQs Including 2026 Regulations](https://www.jacksonlewis.com/insights/navigating-california-consumer-privacy-act-30-essential-faqs-covered-businesses-including-clarifying-regulations-effective-1126)

### Platform Terms of Service
- [SocialRails -- Social Media Compliance Guide 2026](https://socialrails.com/blog/social-media-compliance-guide)
- [InfluenceFlow -- Social Media Compliance Tools 2026](https://influenceflow.io/resources/social-media-compliance-tools-the-complete-2026-guide-for-brands-and-creators/)
- [OpenTweet -- Twitter/X Automation Rules 2026](https://opentweet.io/blog/twitter-automation-rules-2026)
- [X Developer Policy](https://developer.x.com/en/developer-terms/policy)
- [Medium Rules](https://policy.medium.com/medium-rules-30e5502c4eb4)
- [Medium Terms of Service](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)
- [LinkedIn Advertising Policies](https://www.linkedin.com/legal/ads-policy)
- [LinkedIn Professional Community Policies](https://www.linkedin.com/legal/professional-community-policies)
- [AuditSocials -- LinkedIn Ad Compliance for B2B 2026](https://www.auditsocials.com/blog/linkedin-b2b-ad-compliance-2026)
