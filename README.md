# McBride & Sons Plumbing — Atrezzo Studios staging

Separated from Gemini's second single-file prototype on 2026-10-24.

## Files and paths
- `index.html` — Home
- `services/index.html` — Services
- `about-us/index.html` — About Us
- `contact-us/index.html` — Contact Us
- `assets/css/styles.css` — shared additional CSS
- `assets/js/main.js` — accessible mobile menu JS
- `assets/images/` — empty until authentic assets are provided
- `ATREZZO-PROJECT-STATUS.md` — project phase register

Each page includes its own title and meta description, with real interpage links. The current visual implementation remains based on Gemini version 2; this commit is a **structural migration**, not an approved redesign.

## Critical blockers (do not publish)
1. **Callback forms configured for real delivery to Atrezzo test inbox:** now POST to FormSubmit (AJAX, fallback HTML). Activation and real inbox delivery remain UNVERIFIED. The user must activate the recipient from atrezzostudiosv@gmail.com and perform a controlled test. Public demo forms explicitly identify Atrezzo as recipient and require test consent; do not send genuine customer requests.
2. **Original brand assets are absent:** upload approved transparent logo and authentic portraits (Jasper McBride, Michael McBride Sr., Michael McBride II). Current design uses typographic/icon/silhouette placeholders only.
3. **External Tailwind runtime CDN and Font Awesome CDN:** allowed for draft preview; replace with compiled production assets before deployment.
4. **Claims:** Do not add arrival in 20–30 minutes, live dispatch, invented technician titles, detailed family bios, exact business hours or unverified technical service methods. The 24/7 availability and flexible payment options are company-published claims, not independently operationally tested.
5. **Google aggregate rating:** 4.9 / 5 and 200+ Google reviews were previously researched; recheck on publication.
6. **Navigation and mobile testing:** local smoke tests done only; complete WCAG/responsive/SEO/form testing before publication.

## Preview
From the project directory run: `python3 -m http.server 8000` and open `http://localhost:8000/`.
GitHub Pages may be enabled only as a clearly identified Atrezzo demonstration. Keep `noindex, nofollow` until the actual business authorizes publication and production settings are ready.

## Deployment
The user approved a **public GitHub repository for a clearly identified Atrezzo preview**, not an official McBride website. Each page contains visible demo notice and meta robots `noindex, nofollow`.
GitHub Pages can serve the directory-based pages once hosting is deliberately approved.

## Test callback forms — activation required
- Home and Contact forms use `https://formsubmit.co/atrezzostudiosv@gmail.com` and asynchronous submission to the documented AJAX endpoint.
- First submission triggers an activation message to the Atrezzo mailbox. A user with mailbox access must confirm the form before emails will arrive.
- Verify BOTH pages separately with synthetic test details, and inspect inbox and spam. Form provider acceptance alone is not proof of delivery.
- Test message recipient is Atrezzo Studios; the public page makes this explicit and requires checkbox acknowledgment.
- Before client handoff: replace the endpoint with a client-approved destination, prepare client-approved privacy/disclosure text, retest deliverability and anti-spam behavior.
- Do not mark production-ready before real acceptance and receipt are checked.
