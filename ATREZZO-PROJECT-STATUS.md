# ATREZZO PROJECT STATUS — McBride & Sons Plumbing
Updated: 2026-10-24

## Workflow
- Phase 1 — Site audit: CLOSED, approved by user.
- Phase 2 — Strategy / architecture: CLOSED, approved by user. Four pages: Home, Services, About Us, Contact Us.
- Phase 3 — Copy / SEO draft: CLOSED for editorial direction, approved by user, with subsequent documented 24/7, payments and Google reviews updates. Reconfirm any added details before publication.
- Phase 4 — Art direction: CLOSED, approved by user. Brand green, Manrope, authentic family assets, minimal editorial style.
- Phase 5 — Gemini master prompt: CLOSED, approved; user supplied generated iterations.
- Phase 6 — Gemini prototype audit (versions 1 and 2): CLOSED with FAIL findings. Version 2 has simulated form success, unsupported commercial detail, no actual portrait/logo images, SPA navigation without per-page metadata.
- Phase 7 — Home design validation: IN VALIDATION. Home V2 editorial conversion redesign committed to GitHub demo main (HTML commit 331254709e2be7babf31eefb9e7ca734889a913b; CSS commit c8581deed126212b9b1c6f63ab5fea74d185fde5). Local Chromium inlined-assets testing: 375/768/1024/1440 widths, no horizontal overflow, 8/8 images loaded, menu open/Escape passed, no JS errors. Form POST success MOCK ONLY; Gmail delivery still unverified. User visual approval pending.
- Phase 8 — Internal pages and technical completion: PENDING.
- Phase 9 — Production QA: PENDING.
- Phase 10 — Final delivery: PENDING.

## Approved design / business constraints
- Keep McBride & Sons Plumbing as family-owned plumbing company with legacy communicated as 1953, NOT verified incorporation year.
- Six categories: Drain Cleaning; Leak Repair; Hydro-Jetting; Water Heater Services; Drain & Sewer Repair; Bathroom Remodeling Plumbing.
- Original website announces 24/7 availability and flexible payment options. Do not extend to immediate dispatch, 20–30-minute guaranteed arrival, payment terms or live status unless confirmed.
- Public company phone: (817) 901-3328; email: owner@mcbrideandsonsplumbing.com.
- Google aggregate rating and 200+ reviews were reported in prior research; re-verify at publication.
- Use authentic logo and three supplied family portraits. Authentic assets uploaded and integrated into header on all four pages, and Home/About portrait galleries; visual browser validation pending.
- No fabricated family biography, technical services, staff titles, operating hours, or social proof.
- No pretend success for contact forms.

## Pending / blockers
1. Authentic logo and three portrait images: RECEIVED AND INTEGRATED (2026-10-24); verify visual layout on GitHub Pages.
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
- Public repo staging: APPROVED (demo, not official client site). GitHub Pages publication: deployed successfully (GitHub Actions 40105813147); post-image-update responsive browser test: PENDING.
- GitHub repository: CREATED by user: `atrezzostudiosv-spec/mcbride-sons-plumbing`.

## Form change — 2026-10-24 (user approval)
- Public demo forms must REALLY send test messages to atrezzostudiosv@gmail.com.
- Home and Contact test forms: CODE IMPLEMENTED with FormSubmit endpoint and AJAX error handling.
- Delivery status: IN VALIDATION, provider activation and real Gmail receipt still required.
- Explicit demo recipient disclosure/checkbox included; no fake success alert.
- The company email/phone remain the official CTA channels, while demo form submissions are only for Atrezzo tests.

## 2026-10-24 — Authentic image integration
- Received four user-supplied WebP files; original image bytes preserved, no regenerated faces or logos.
- Header logo replaced on all four independent pages.
- Home and About placeholders replaced with portraits, in user-provided family order: Jasper McBride, Michael McBride Sr., Michael McBride II.
- Asset files under `assets/images/`; dimensions documented in README.
- No family titles, biographies or new claims introduced.
- Static source integration verified; published responsive visual inspection remains pending.

## 2026-10-24 — Home V2 implementation (ONLY Home)
- Replaced `index.html` and added `assets/css/home.css` scoped to Home; did not alter Services, About or Contact or shared JS.
- Direct-call CTA, 24/7 availability, FormSubmit staging form, real logo and family portraits, 4.9/5 and 200+ Google reviews (prior verified reference, publication revalidation pending), six correct service anchors, published 24/7 and payment options retained.
- No 20–30 minute arrival claim or live-presence badge; mobile CTA remains persistent.
- Local Chromium inline-assets tests: 375/768/1024/1440, 0 horizontal overflow and 0 JS errors; keyboard Escape menu; accepted form response simulated, not an actual email.
- Open/unfinished: public Pages deployment smoke test, live screenshots, real Gmail receiving tests, final approval from user. Maintain Phase 7 EN VALIDACIÓN until approved.
