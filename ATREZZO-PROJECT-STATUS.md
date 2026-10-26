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

## 2026-10-26 — User-approved architecture expansion: 10 pages
- User explicitly approved a new 10-page architecture and requested continuation. This supersedes the previous four-page architecture while preserving its existing approved work.
- Original four pages and their established Manrope/dark-green design system are preserved. The Home visual composition was NOT redesigned in this change; only its six service destination links were updated.
- **Six standalone service pages ADDED:** `services/drain-cleaning/index.html`, `services/leak-repair/index.html`, `services/hydro-jetting/index.html`, `services/water-heaters/index.html`, `services/drain-sewer-repair/index.html`, `services/bathroom-remodeling/index.html`.
- **Scoped CSS ADDED:** `assets/css/service-detail.css`. Reuses existing shared styles, Manrope, brand greens, authentic logo and overall editorial styling.
- **Navigation links UPDATED:** all six Home service tiles point to their new detail page; six Services overview CTAs point to pages; About, Services and Contact footer lists link to detail pages. The existing top-level Services menu takes visitors to the Services overview; a direct dropdown of six services is not yet implemented.
- Published source fidelity: water-heater offering kept general because original descriptive paragraph incorrectly belongs to Drain & Sewer Repair; bathroom remodeling is confined to plumbing support. No new service types, guarantees or technician biographies.
- **STATIC REPOSITORY CHECK VERIFIED:** ten HTML files fetched from main, one H1 per page (10/10), `noindex` present on all (10/10), business telephone CTA present on all, zero broken local HTML asset/page references based on the tracked resource set.
- **NOT COMPROBADO:** live GitHub Pages rendered screenshots at 375/768/1024/1440; interactive browser operation for new routes; real email receipt and consent flow; Lighthouse; WCAG conformance; server-side form delivery; canonical and public production SEO.
- Public staging remains a **design demonstration, not the official business site**. Maintain `noindex, nofollow` and demo disclosure. Do not hand off to client until genuine contact handling and live QA are verified.
- Current phase: **Phase 8 — IN VALIDACIÓN** (six service pages and link integration); **Phase 9 — PENDIENTE**; **Phase 10 — PENDIENTE**. Home legacy Phase 7 visual signoff not independently evidenced by this GitHub edit.

## 2026-10-26 — Contact form added to Services hero and all six service-detail heroes
- User identified the missing hero contact form. GitHub read confirmed Home V2 ALREADY had its callback form inside the hero, so Home was preserved unchanged.
- Added the same visible, conversion-focused staging form panel to the Services overview hero and each of six service detail heroes (7 new hero forms). Desktop split hero presents copy/call CTA and form side by side; mobile CSS stacks them.
- Fields: name, phone, service (read-only visual context + hidden service input for detail pages, selectable service for overview) and optional description, plus explicit demo-consent checkbox.
- Reused the existing `assets/js/main.js` staging FormSubmit AJAX handler. Submissions are addressed to `atrezzostudiosv@gmail.com` with an Atrezzo demo notice; the business telephone CTA stays prominent. No fake success claim and no alleged appointment booking.
- Added and refined responsive form CSS in `assets/css/service-detail.css`. The Home hero form was not modified.
- **VERIFIED STATICALLY:** 8/8 pages (Home + overview + six service pages) have one form, one H1, no duplicate element IDs, every `label[for]` resolves locally, staging consent and `data-form-status` are present, and the seven added pages load the form CSS.
- **NOT COMPROBADO:** deployment/browser screenshots at actual widths, form relay activation and real Gmail receipt. Keep staging `noindex` and demo notice until approved production migration.
