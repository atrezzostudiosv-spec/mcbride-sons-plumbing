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

## 2026-10-26 — Home photographic background approved and implemented
- User approved changing the HOME hero only, taking cinematic background inspiration from a supplied 308 Construction video reference. Scope intentionally limited to `index.html` and `assets/css/home.css`.
- Added full-bleed stock photography of hands working on plumbing fittings, with responsive `background-size: cover`, layered green/black gradients and adjusted text contrast. Removed the giant decorative `McB` hero watermark. Preserved original home hero H1, CTA actions, heritage row, genuine family photographs and callback form.
- Photo source: AR Abnoy, `https://www.pexels.com/photo/close-up-of-man-using-a-spanner-16509869/`; listed Free on Pexels. Photo is expressly **ILLUSTRATIVE STOCK** — not a real job or staff member of McBride. CDN asset: `images.pexels.com/photos/16509869/pexels-photo-16509869.jpeg`, with responsive image-size query parameters. External dependency must be reviewed and optionally self-hosted in a production build.
- Photo-host preconnect added on Home. Hero maintains solid dark green fallback if photo cannot load. No service contents or other page design touched.
- **STATIC VERIFIED:** background CSS and tablet/mobile breakpoint overlays committed to GitHub main, watermark removed, original Home form still present, source/license traceability recorded. **NOT COMPROBADO:** live visual screenshots at 375/768/1024/1440, actual external-image network delivery in browser, Lighthouse performance, accessibility contrast measured from rendered image.
- Home photographic design: IN VALIDATION; staging maintains `noindex` and Atrezzo demonstration label.

## 2026-10-26 — HOME hero V3: user-approved industrial editorial correction
- User rejected V2's nearly invisible background photo, excessive green veil, oversized white form and overbearing headline, and authorized execution of a focused Home-hero correction.
- CHANGED ONLY `assets/css/home.css`. No HTML, form handler, site navigation or non-Home page content was modified.
- Replaced previous image #16509869 with landscape (6000×4000) free Pexels photo #6419128 by **Anıl Karakaya**: https://www.pexels.com/photo/plumber-installs-pipe-fittings-6419128/ . The image depicts hands installing steel pipes and is an illustrative licensed photograph, **NOT company staff or a real McBride project**.
- Hero treatment now uses a neutral charcoal (#141b19) backing with localized black/carbon gradient (rather than an opaque green screen); the photo has mild contrast/luminance balancing without desaturating the scene heavily.
- Rebalanced desktop columns, reduced H1 scale to 60px maximum, constrained the form to 444px, softened the form surface to warm ivory, tightened field spacing, improved checkbox/status legibility.
- Added explicit tablet (≤1023px), mobile (≤640px), and narrow mobile (≤375px) layout/photography rules, with the form stacked below the copy when appropriate and the lower hero returning to charcoal.
- **VERIFICADO (source code)**: photo reference replaced, old Pexels URLs absent, desktop/tablet/mobile CSS rules present, original one H1 and existing callback form intact, service dropdown and consent intact, direct call CTA present, live form handler untouched, demo notice and `noindex` unchanged.
- **NO COMPROBADO**: screenshot-driven layout and image focal point at 375/768/1024/1440px, external photo host rendering and latency, measured WCAG contrast, actual form delivery. This remains public Atrezzo **staging**, NOT client production.
- Phase 7: HOME V3 visual approval **EN VALIDACIÓN**. Do not reopen already-approved informational/architectural phases.

## 2026-10-26 — Hero gutters and mobile popup for callback form
- User sent a three-breakpoint video showing Home hero margins were inconsistent and a long inline callback form interrupted the mobile flow. User authorized a mobile-only popup and margin corrections.
- Root cause identified and corrected: HOME hero V3 declared `.hero .hero-grid {width:100%}`, overriding the shared `.wrap` gutters. Restored the same breakpoint-appropriate gutters as site navigation/sections: 40 px per side at 1440 px (content cap 1250px), 26 px at ≤1150, 20 px at ≤900, 18 px at ≤640.
- Mobile ≤767 px with JS: the existing "Request a Callback" anchor is styled as a button and opens a **native modal dialog**, with visible close button, Escape closing, backdrop dismissal, focus restored to CTA and body scroll disabled while open. The existing DOM form panel is **moved**, not cloned; ONE form and its original FormSubmit handler remain.
- ≥768 px: form remains inline in the hero as before, including tablets and desktop. On no-JS/mobile unsupported-dialog fallback, the original inline form is accessible via its anchor, so the contact path is not lost.
- Scoped changes ONLY `assets/js/main.js` and `assets/css/home.css`; hero text, headings, sections, images, contact address, CTA destination, demo disclosure and original form fields were not changed.
- **STATIC SOURCE VALIDATION:** original Home still has one callback form; HTML anchor preserved; CSS and JS breakpoints match, no duplicate forms, `noindex` retained, staging handler preserved.
- **LOCAL CHROMIUM ISOLATED FIXTURE (not a live site test):** 375px form moved out of hero, popup opens, close button/Escape close it, focus returns; 768px and 1440px keep form inline; viewport transition back to 375px does not clone form; zero horizontal overflow in fixture at all tested widths; sample desktop grid gutter was 95px at 1440 (1250px capped).
- **NOT YET VERIFIED ON DEPLOYED SITE:** actual full-page screenshots at 375/768/1024/1440, real provider email receipt, production WCAG/contrast/performance. Keep Home in **EN VALIDACIÓN** until visual and functional checks on live preview are completed.
