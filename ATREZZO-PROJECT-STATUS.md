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

## 2026-10-26 — Tablet callback modal and desktop CTA deduplication
- User approved the mobile popup and requested the same behavior on tablet, with the redundant `Request a Callback` action removed from the desktop hero (the form is already visible beside the H1).
- Updated only `assets/js/main.js` and `assets/css/home.css`: tablet/mobile viewport `<=1023px` now moves the **same existing form node** into the native accessible popup and exposes the callback CTA. Desktop `>=1024px` retains the inline form and hides only `.hero-form-link`; `Call Now` remains.
- With JavaScript unsupported or disabled, the original form remains available inline and the link still scrolls to it on tablet/mobile. Desktop does not need a callback link because the form remains inline.
- Isolated local Chromium fixture checks **passed** at widths 375, 768, 900, 1023, 1024, and 1440: popup opens and closes with Escape at <=1023, is not rendered as a button at >=1024, viewport resize 768→1440 closes popup and restores the same form to the hero, only one form exists, and no fixture horizontal overflow was seen.
- Repository static checks passed for matching CSS and JS breakpoints, unchanged company Call Now link, `noindex`, demo consent, and existing staging submit handler.
- **Pending:** real published site browser screenshots, visual breakpoint/layout approval, and end-to-end Gmail delivery. Do not label isolated fixture coverage as production QA.

## 2026-10-26 — Desktop CTA visibility corrective fix
- User reported `Request a Callback` still visible in the desktop hero despite the earlier desktop-only CSS hide rule.
- Verified that the CTA remained as a valid HTML anchor, and its visibility depended on a late stylesheet media query. Actual user-facing cause could include stale browser CSS or viewport width and was not proven from live browser telemetry.
- Added **critical inline responsive CSS** in `index.html`: CTA hidden by default with `!important`, shown only when viewport <=1023 px. The desktop hero still presents the existing callback form beside the H1.
- Applied matching desktop-first visibility rule to `assets/css/home.css`, and versioned CSS/JS resource URLs to avoid stale cached files. At tablet/mobile sizes the same CTA still opens the existing native dialog; `Call Now` preserved.
- **VERIFICADO EN CÓDIGO:** 1 callback CTA, 1 original form, inline desktop hide and tablet/mobile show, matching stylesheet rules, one popup reused in JavaScript, source cache versioning, `noindex` retained.
- **NO COMPROBADO:** a browser screenshot from the latest public Pages URL and Gmail delivery. Pending real-world user validation of the desktop disappearance.


## 2026-10-26 — Approved HOME cinematic video and editorial motion
- User approved the prior audit of Hill Country and asked to implement the selected `Technical Modern Cinematic` direction. Scope controlled to **Home only**: `index.html`, `assets/css/home.css`, `assets/js/main.js`. Existing nine internal pages, header/footer, core content, brand assets, real family portraits, CTA destinations and form submission handler unchanged.
- Background footage **licensed illustrative stock**, not McBride work or employees: Pexels video [A Person doing Plumbing by Stepan SK, #7584762](https://www.pexels.com/video/a-person-doing-plumbing-7584762/). Published footage depicts a hand adjusting water-pipe connections below a sink; 16:9, duration 20 s. Pexels permits commercial use. **Do not imply McBride endorsement or employee identity.**
- Implemented DOM `<video>` layer behind existing hero text/form, with `muted`, `playsinline`, `loop` and `preload=none`. Existing still-photo CSS #6419128 remains fallback. Video source assigned in JavaScript only at **viewport >=1024 px** with `prefers-reduced-motion` off and no save-data/slow-2g, with 720p and 1080p CDN variants attempted in order. Playback stops when tab is hidden or hero leaves viewport. The user can pause/restart via subtle accessible desktop control; videos remain absent from mobile/tablet and reduced-motion views.
- Mild desktop entry timing for hero eyebrow/title/description/action/heritage and IntersectionObserver reveal for Home intro, service title, family portraits, values and final CTA. Respect reduced-motion and preserve fully visible content without JavaScript.
- **REPOSITORY STATIC QA VERIFIED:** one background video, one video control, one original callback form, valid JS syntax, source URL references, appropriate breakpoints and media preferences, static image fallback, pause behavior source, phone/CTA preserved, popup at <=1023px preserved, `noindex` and staging demo notice preserved.
- **NOT VERIFIED:** actual MP4 download/playback from Pexels CDN, sizes/bandwidth, rendered video crop and overlay in live browser, direct desktop/mobile screenshots (375, 768, 1024, 1440), actual email receipt, Lighthouse, WCAG compliance. The 720p and 1080p CDN URL patterns are plausible but could not be requested end-to-end from this runtime. Real video operation therefore remains **EN VALIDACIÓN**, not a verified video delivery claim.
- Existing Home and responsive behavior remain in visual validation. Once live tested, optimize or self-host an approved short video clip if performance merits it. No client production publication authorization.

## 2026-10-26 — HOME cinematic v2: brighter overlay, new clip, tablet/mobile playback
- User confirmed that the first background video did play on desktop but rejected its visual quality and the excessive darkness; asked for a better video and playback on more devices.
- Source replaced: previous Pexels #7584762 retired. Selected **Stepan SK / Pexels #7584858**, a 9-second, 16:9 free-use clip of faucet repair in a modern residential kitchen. Source: https://www.pexels.com/video/man-fixing-the-faucet-on-the-kitchen-sink-7584858/ . It is illustrative stock, **not** McBride staff or work.
- Changed files only `index.html`, `assets/css/home.css`, `assets/js/main.js`. Added `autoplay` to muted/playsinline loop tag, replaced CDN URL candidates with new 360p (mobile) and 720p/1080p files (tablet/desktop), and preserved static CSS photograph #6419128 as fallback.
- Playback now allowed for mobile/tablet/desktop, subject to `prefers-reduced-motion`, `saveData`, low-bandwidth connection detection, visibility and out-of-viewport pause. The mobile/tablet callback modal still reuses the one original form; video pauses while popup is open. Pause/Play button is available at all supported sizes when frames are playing.
- Overlay opacity reduced and independently tuned for desktop, tablet and mobile. Desktop H1 and small caption use restrained text shadows for readability. Original business messaging/CTA/demonstration noindex preserved.
- Cache version advanced to `cinematic-2` in Home HTML.
- **VERIFICADO EN REPOSITORIO:** JavaScript syntax, correct media breakpoint logic, reduced overlays, one original form, poster fallback, no old video reference, callback popup and desktop CTA rules preserved, external media URLs defined; internal page files not edited.
- **NO COMPROBADO:** live successful decoding of the NEW Pexels MP4 variants or their exact bandwidth; live visual crop and text contrast at 375/768/1024/1440; mail delivery; Lighthouse. New video CDN variant URLs require a real-browser smoke test. If remote files fail, photo remains.
- HOME cinematic v2 status: **EN VALIDACIÓN**, not production/client-approved.

## 2026-10-26 — Home trust rail and customer reviews (user-authorized)
- User approved conceptual trust design and explicitly requested implementation: three functional trust entries (Google, family legacy, emergency phone), plus a customer reviews section placed immediately above the existing final CTA and footer.
- **Scope:** updated Home `index.html`, `assets/css/home.css`, and a small addition to existing scroll reveal selectors in `assets/js/main.js`. Existing services/about/contact pages and Home video/form/contact behavior were not changed.
- New three-part editorial trust rail: Google 4.9 / 200+ reviews (linked to `#reviews`), 1953 family legacy (linked to `./about-us/index.html` with **genuine user-supplied portraits**, not fake historic vehicles), and 24/7 emergency availability (direct `tel:+18179013328`). Each panel is one keyboard-accessible click target and adapts as a full-width Google panel over two equal heritage/emergency panels on mobile/tablet.
- New `#reviews` section immediately BEFORE `end-cta`, retaining `end-cta` and `footer` unchanged. Includes two short customer excerpts attributed to **Michael Powledge Jr** and **James Esser**, as publicly listed at https://www.draincleaningnear.me/drain-cleaning/tx/denton . Quoted language limited to exact short portions of that third-party review listing. The section explicitly labels excerpts as `publicly listed customer review excerpt`, and links to its public listing.
- Google business profile identification confirmed via place ID `ChIJfUZDv4MTCaERpoBYnpQWmBY`, returned for business McBride & Sons Plumbing, Argyle TX, +1 817-901-3328, rating 4.9 and 272 reviews at audit. Live site shows conservative `200+` to avoid hardcoded rapidly changing count. Google Maps deep-link is an address to the confirmed place ID rather than a fabricated review-profile screenshot.
- Avoided fake Google screenshot, invented historic truck photos, fabricated testimony, and award-style badges or unverified ranking claims.
- **VERIFICADO EN CÓDIGO:** three correct targets, exactly one `#reviews`, source link and review attributions present, order after approach and before final CTA, one H1, one original callback form, mobile/tablet popup still configured, video unchanged, reduced-motion behavior and responsive CSS present, no unresolved in-page anchor destinations, JS syntax valid.
- **NO COMPROBADO:** live screenshots and visual navigation at 375/768/1024/1440, Google Maps link opening externally, external email receipt, Google rating refresh, or formal WCAG audit. This remains a non-official Atrezzo staging site with `noindex` and demo disclosure.
- Phase: trust rail/reviews **EN VALIDACIÓN**; prior Home hero and ten-page architecture remain unchanged. No need to repeat completed stages.

## 2026-10-26 — HOME editorial experience 1.0 (Services / Family / Approach)
- User explicitly authorized implementing the experience improvements proposed by the prior Home audit using Ranchman, Everest, Elite, Julie Siddons and CR Plumbing only as inspiration. Scope limited to three existing Home sections plus a small intro spacing improvement; **no new business claims or new services**, and no modification of internal pages, hero conversion design, proof rail or reviews.
- Files changed: `index.html`, `assets/js/main.js`, and **new isolated** `assets/css/home-experience.css`. Original `home.css` untouched to preserve approved design; a targeted stylesheet is easier to remove or tune without disturbing the hero and trust interactions.
- Services now has a responsive image-led two-column editorial composition (sticky photograph on >=1024px; stacked landscape stage in tablet/mobile), with all six original service links and exact descriptions retained. Active number/name in the **illustrative** photo panel track the focused/hovered or scrolled service; no service is replaced by a fake gallery or case study.
- Free Pexels illustrative plumber stock photo #32588548 credited to Bulat843: https://www.pexels.com/photo/plumber-repairing-pipe-with-wrench-indoors-32588548/ ; alternate tablet/mobile illustrative pipe-fitting stock #6419128 by Anıl Karakaya, already referenced in the Home; neither represents a McBride employee/project. Attribution is visible below the photo and truthful alt text is supplied. Exact remote image delivery not live-verified.
- Family section now has a restrained 01–02–03 chapter connector and scroll emphasis of the three **authentic existing** portraits, while retaining all names, photo src paths, and destination to About Us.
- Our Approach keeps its four original facts and descriptions; now displays a subtle active rail as users scroll, with a static left panel on mobile, sticky text on desktop, and `prefers-reduced-motion` protections.
- Home intro has better typographic breathing room and a rule alongside the copy, without changing the approved messaging. The existing `IntersectionObserver` reveal effect is preserved and enhanced only within scoped sections; no scroll hijacking and no heavy animation library.
- **VERIFICADO EN CÓDIGO:** one H1, one FormSubmit staging form, one hero video, existing CTA and tablet/mobile popup, Google trust anchors, review section before final CTA, six valid internal service links, three original family portrait image paths, four approach steps, no unresolved in-page anchors, valid main.js syntax, CSS reduced-motion rules, noindex/demo disclosure intact.
- **NO COMPROBADO:** actual live screenshots and visual approval at 375/768/1024/1440px, photo CDN decoding, visual smoothness on touch devices, Lighthouse, contrast measurements, end-to-end form email receipt.
- State: **EN VALIDACIÓN**. Do not reopen approved header/hero/proof/reviews unless a verified regression exists.

## 2026-10-26 — HOME service scenes 2.0; Tri-Lane cards × Ranchman scroll
- User rejected both the mobile photographic/list hybrid and the proposed accordion. Reference screen recordings from Ranchman and Tri-Lane reviewed: **visual service cards integrated with photography** (Tri-Lane) plus **one chapter replacing the next as the visitor scrolls** (Ranchman). The desired medium is normal vertical scrolling, not lists, accordions, horizontal carousels or a hijacked wheel.
- Replaced the `services-experience` and six `service-line` elements with six **full-card anchor links** (`service-scene`). The same six verified service names, descriptions, URLs and order are preserved verbatim in Home HTML. Each service card has a unique illustrative Pexels photo, service index, descriptive text, CTA and progress rule. No added service, benefit or capability.
- Desktop: premium photography-led bento with a dominant first card and five secondary cards, inspired by Tri-Lane's visual composition but independently designed for McBride's dark-forest palette. Tablet: responsive two-column cards. Mobile <=640px: six large sticky, progressively overlaid chapters with normal page scroll, no hover-only UI and no forced snapping. Existing sticky emergency callbar remains.
- Pexels illustrative image IDs: 6419128 (pipe repair), 32588548 (plumbing tools/repair), 39885416 (copper pipe work, generic visual for hydro-jetting), 34938439 (heating system, generic visual for water heater services), 37627673 (drainage pipe construction, generic visual for drain/sewer services), 7031564 (finished bathroom interior, generic visual for bathroom remodeling plumbing). All are illustrations **not McBride work** and this disclaimer is visibly stated in the service section; some images relate broadly to the service category, not exact methods. Each source page presents a free Pexels license. Verify live image delivery, crops and client acceptance.
- `index.html` was updated; `assets/css/home-experience.css` now includes isolated scene layouts and reduced-motion rules; `assets/js/main.js` replaces only the obsolete service text-list observer with a passive, lightweight scene emphasis observer. Original family/approach enhancement and all prior approved sections retained. Existing Home script and CSS are cache-busted with `20261026-scenes-1`.
- **VERIFICADO EN REPOSITORIO:** six unique service scenes and unique stock photo IDs, six real unchanged local service URLs, H3 tags, no old list in services section, 1 H1, 1 staging form, approved hero video/popup/trust/reviews retained, syntax of main.js valid, CSS braces balanced, noindex demo preserved, low-motion fallback to normal stacked cards.
- **NO COMPROBADO:** visual cross-fade/scroll experience in an actual mobile browser (375, 390, 640, 768, 1024, 1440px); exact photo CDN delivery, contrast and visual crops; updated Lighthouse or WCAG audit. Status **EN VALIDACIÓN**, not yet closed.

## 2026-10-26 — HOME WHAT WE DO / SERVICES CAROUSEL 3.0
- User supplied a 12-second screen recording showing current desktop/tablet bento and mobile stacked sticky cards. Explicit direction: mobile is liked despite perceived density and **must not change**; desktop/tablet were visually disliked as too crowded; user favored a carousel and requested the designer choose the best approach quickly.
- Decision implemented: **manual editorial carousel for >=641px only** with one large panoramic service card and a glimpse of the next, scroll-snap for horizontal touch/trackpad navigation, Previous/Next circular buttons and 01/06 counter; **no autoplay, no new images, no extra services, no forced vertical-scroll scene changes on desktop/tablet**. Tablet gets a wider single card ratio (87% vs 80% desktop) with navigable remainder visible.
- Desktop/tablet visual complexity reduced from six simultaneous photos to one main photo plus teaser; headings/descriptions/CTAs remain inside photographs with legible text and dark overlay. The six HTML service card links and exact service content stay unchanged. User-approved <=640px mobile sticky vertical cards and existing passive scroll tracking remain **unmodified**. Carousel controls are CSS-hidden on mobile.
- Scope: Home HTML adds controls and cache busting; `assets/css/home-experience.css` adds only >=641px carousel overrides; `assets/js/main.js` appends a self-contained responsive manual navigator without changes to mobile code. Other pages, hero, phone CTA, trust band, testimonials and footer untouched.
- Accessibility: labeled arrow buttons with disabled ends, focus outlines, keyboard ArrowLeft/ArrowRight when carousel track has focus, aria-roledescription only at desktop/tablet sizes, polite live current index, no automatic motion, reduced-motion overrides.
- **VERIFICADO EN CÓDIGO:** six service destinations unchanged, mobile sticky CSS unchanged, desktop/tablet CSS gated >=641px, nav controls present and hidden <=640px, JS valid, CSS braces balanced, unique HTML IDs, one H1 and form, demo noindex and old approved sections preserved.
- **NO COMPROBADO:** rendered browser viewport screenshots 375/768/1024/1440, actual desktop click/swipe behavior, horizontal overscroll and crop, remote photographs, measured Lighthouse/contrast. Static implementation status **EN VALIDACIÓN**, do not assert visual approval yet.
