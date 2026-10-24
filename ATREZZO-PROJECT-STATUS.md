# ATREZZO PROJECT STATUS — McBride & Sons Plumbing
Updated: 2026-10-24

## Workflow
- Phase 1 — Site audit: CLOSED, approved by user.
- Phase 2 — Strategy / architecture: CLOSED, approved by user. Four pages: Home, Services, About Us, Contact Us.
- Phase 3 — Copy / SEO draft: CLOSED for editorial direction, approved by user, with subsequent documented 24/7, payments and Google reviews updates. Reconfirm any added details before publication.
- Phase 4 — Art direction: CLOSED, approved by user. Brand green, Manrope, authentic family assets, minimal editorial style.
- Phase 5 — Gemini master prompt: CLOSED, approved; user supplied generated iterations.
- Phase 6 — Gemini prototype audit (versions 1 and 2): CLOSED with FAIL findings. Version 2 has simulated form success, unsupported commercial detail, no actual portrait/logo images, SPA navigation without per-page metadata.
- Phase 7 — Home design validation: IN VALIDATION. Preview file MCBRIDE_HOME_FASE7_PREVIEW.html created; no production change. Desktop/tablet/mobile widths 375/768/1024/1440 checked for horizontal overflow; menu open/Escape tested.
- Phase 8 — Internal pages and technical completion: PENDING.
- Phase 9 — Production QA: PENDING.
- Phase 10 — Final delivery: PENDING.

## Approved design / business constraints
- Keep McBride & Sons Plumbing as family-owned plumbing company with legacy communicated as 1953, NOT verified incorporation year.
- Six categories: Drain Cleaning; Leak Repair; Hydro-Jetting; Water Heater Services; Drain & Sewer Repair; Bathroom Remodeling Plumbing.
- Original website announces 24/7 availability and flexible payment options. Do not extend to immediate dispatch, 20–30-minute guaranteed arrival, payment terms or live status unless confirmed.
- Public company phone: (817) 901-3328; email: owner@mcbrideandsonsplumbing.com.
- Google aggregate rating and 200+ reviews were reported in prior research; re-verify at publication.
- Use authentic logo and three family portraits; they are not in the received Gemini HTML and not available as isolated assets in this preview.
- No fabricated family biography, technical services, staff titles, operating hours, or social proof.
- No pretend success for contact forms.

## Pending / blockers
1. Approved standalone image files: transparent logo and portraits Jasper McBride, Michael McBride Sr., Michael McBride II.
2. Confirm actual form email delivery / endpoint and permitted handling of customer information, including privacy disclosures.
3. Verify any 20–30 minute response guarantee directly with the business, including coverage and conditions; otherwise do not display it.
4. Confirm operating schedule beyond stated 24/7 availability, specific license identifiers, final location(s) and payment-plan details before publication.
5. Approve Home visual presentation; THEN use its design system on other three pages without changing closed decisions.

## New action — 2026-10-24: Separate Gemini v2 website into real pages
- Four independent static routes, shared CSS and JS: BUILT LOCALLY, UPLOADED TO GITHUB main; VERIFIED by repository file fetch.
- Home visual redesign: IN VALIDATION; no change to approved style until user review.
- Four standalone pages, shared CSS/JS and demo notices committed to main (commit 23b81cd69e92ffce8283cabd473fdaae01e592eb). GitHub file reads verified 4/4 pages.
- Staging meta robots `noindex, nofollow` added to all four pages. This is a crawler directive, not a guarantee against indexing.
- Real FormSubmit receipt, GitHub Pages publishing, and live responsive tests: PENDING.
- Fake callback confirmation: REMOVED; forms now submit to FormSubmit staging, provider delivery UNVERIFIED.
- Navigation from Gemini one-file app changed to ordinary internal links.
- Public repo staging: APPROVED (demo, not official client site). GitHub Pages publication and responsive browser test: PENDING.
- GitHub repository: CREATED by user: `atrezzostudiosv-spec/mcbride-sons-plumbing`.

## Form change — 2026-10-24 (user approval)
- Public demo forms must REALLY send test messages to atrezzostudiosv@gmail.com.
- Home and Contact test forms: CODE IMPLEMENTED with FormSubmit endpoint and AJAX error handling.
- Delivery status: IN VALIDATION, provider activation and real Gmail receipt still required.
- Explicit demo recipient disclosure/checkbox included; no fake success alert.
- The company email/phone remain the official CTA channels, while demo form submissions are only for Atrezzo tests.
