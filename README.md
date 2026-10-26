# McBride & Sons Plumbing — Atrezzo Studios staging
**Updated:** 2026-10-26  
**Role:** public Atrezzo design demonstration; NOT the official client website.

## Current implementation
The repository contains **10 standalone static HTML pages**:
- `index.html` — Home (existing editorial V2 preserved)
- `about-us/index.html` — About
- `services/index.html` — Services overview
- `contact-us/index.html` — Contact
- `services/drain-cleaning/index.html`
- `services/leak-repair/index.html`
- `services/hydro-jetting/index.html`
- `services/water-heaters/index.html`
- `services/drain-sewer-repair/index.html`
- `services/bathroom-remodeling/index.html`

Shared files: `assets/css/styles.css`, `assets/css/home.css`, `assets/css/service-detail.css`, `assets/js/main.js`. Four genuine user-supplied WebP assets are in `assets/images/` (logo and three family portraits). Preserve these assets and avoid regenerating the identities.

## Navigation
Home cards, Services overview CTAs and links in the About/Services/Contact footers reach the six standalone service pages. Service pages also provide breadcrumbs, related-service links, About and Contact pathways, and telephone CTAs.

The top navigation currently links to Services overview rather than opening a six-service dropdown. Desktop/mobile dropdown expansion remains an optional design implementation task; no empty/fake routes are present in the checked source links.

## Source of truth
Original site: https://mcbrideandsonsplumbing.com/ plus /about-us, /services and /contact-us. Core categories are the same six services published by the business. The source incorrectly places Drain & Sewer text under Water Heaters; these are separated in this staging build. Water Heater details remain intentionally modest because individual subservices are not established; Bathroom Remodeling covers **plumbing support**.

The approved family legacy date is 1953, not independently verified company incorporation. Published phone: (817) 901-3328; email: owner@mcbrideandsonsplumbing.com. Source-published 24/7 availability does not equal guaranteed arrival time. The original website publishes 10% off installations for new customers; do not widen the offer.

## Current checks
**Verified statically in GitHub main (2026-10-26):** 10/10 pages fetchable by repository read, one H1 each, telephone CTA each, staging `noindex` in each, no broken local HTML references across the known tracked pages/assets. Original four-page layout left intact except link updates.

**Not checked:** browser visuals and interactive navigation on live GitHub Pages; real contact form email delivery; PageSpeed/Core Web Vitals; WCAG accessibility conformance; canonical/sitemap for a production domain.

## Form handling — staging only
Home and Contact test forms use FormSubmit with the Atrezzo test inbox `atrezzostudiosv@gmail.com`, explicit demo-recipient disclosure and a consent checkbox. Delivery is NOT VERIFIED. Activation, inbox receipt and anti-spam must be tested; neither AJAX request acceptance nor a mock browser response is proof of delivery. Never use this staging form to receive real customers' enquiries.

Before client delivery replace endpoint with a client-approved recipient, review privacy/legal handling, and repeat end-to-end tests. For genuine business contact, published `tel:` and `mailto:` links remain accessible.

## Build / deployment
Static pages are GitHub Pages compatible as directory-based `index.html` files. Maintain `noindex, nofollow` and visible Atrezzo demonstration notice. Do not portray this staging site as official, and do not remove these protections without authorization.

Tailwind runtime CDN/Font Awesome CDN remain in legacy interior pages; compile production assets and optimize delivery before final launch. Use the project phase log in `ATREZZO-PROJECT-STATUS.md` before touching closed phases.

## Home hero photographic background (2026-10-26)
- Approved redesign applies only to the Home hero background. Keep the editorial copy and right-hand callback form unchanged.
- Photography: [AR Abnoy / Pexels](https://www.pexels.com/photo/close-up-of-man-using-a-spanner-16509869/), listed under the **free Pexels license**. This is an **illustrative image**, not a McBride job, customer, or employee.
- The responsive CDN background is referenced within `assets/css/home.css`, with a dark green fallback and overlaid gradients for text legibility. Image CDN host preconnected in `index.html`.
- Deployment of the updated commit reported GitHub Pages workflow **success**. Actual photo delivery and layout screenshots across viewport sizes are still **not visually verified**; inspect before marking the Home design closed.
