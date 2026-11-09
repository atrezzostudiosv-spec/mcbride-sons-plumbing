#!/usr/bin/env python3
"""Generate shared static markup and route-specific SEO without a build dependency.

Default output remains the existing noindex demo. Changing the base URL does not
authorize a production release or change form recipients or demonstration notices.
"""
import argparse
import html
import json
from pathlib import Path
import re
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_URL = "https://atrezzostudiosv-spec.github.io/mcbride-sons-plumbing/"
VERSION = "20261104"
PAGES = {
    "index.html": ("24/7 Plumber in Denton & DFW | McBride & Sons Plumbing", "Family-owned plumbing serving Denton and DFW. Explore drain cleaning, leak repair, hydro-jetting and more. Call (817) 901-3328 for 24/7 availability.", "Home", "WebPage"),
    "about-us/index.html": ("About McBride & Sons Plumbing | Denton & DFW", "Meet the family behind McBride & Sons Plumbing. Discover our service legacy dating back to 1953 and our commitment to customer care in Denton and DFW.", "About Us", "AboutPage"),
    "contact-us/index.html": ("Contact a Plumber in Denton & DFW | McBride & Sons", "Contact McBride & Sons Plumbing in Denton and DFW. Call (817) 901-3328 for plumbing enquiries and 24/7 emergency availability, or email our team.", "Contact Us", "ContactPage"),
    "services/index.html": ("Plumbing Services in Denton & DFW | McBride & Sons", "Explore six plumbing services in Denton and DFW: drain cleaning, leak repair, hydro-jetting, water heaters, drain and sewer repair, and bathroom plumbing.", "Plumbing Services", "CollectionPage"),
    "services/drain-cleaning/index.html": ("Drain Cleaning in Denton & DFW | McBride & Sons", "Clogged or slow drains? Explore drain cleaning from McBride & Sons Plumbing in Denton and DFW. Call (817) 901-3328 to discuss your drainage concern.", "Drain Cleaning", "WebPage"),
    "services/leak-repair/index.html": ("Leak Repair in Denton & DFW | McBride & Sons Plumbing", "Explore pipe and fixture leak repair from McBride & Sons Plumbing in Denton and DFW. Describe your concern and discuss the next step with our team.", "Leak Repair", "WebPage"),
    "services/hydro-jetting/index.html": ("Hydro-Jetting in Denton & DFW | McBride & Sons", "Learn about hydro-jetting for pipe buildup, grease and debris. Contact McBride & Sons Plumbing in Denton and DFW to discuss your plumbing needs.", "Hydro-Jetting", "WebPage"),
    "services/water-heaters/index.html": ("Water Heater Services in Denton & DFW | McBride & Sons", "Have a water heater concern? Contact McBride & Sons Plumbing about water heater services in Denton and DFW. Call (817) 901-3328 to discuss your needs.", "Water Heater Services", "WebPage"),
    "services/drain-sewer-repair/index.html": ("Drain & Sewer Repair in Denton & DFW | McBride & Sons", "Explore drain and sewer repair for damaged, blocked or aging lines. Contact McBride & Sons Plumbing in Denton and DFW to discuss your drainage issue.", "Drain & Sewer Repair", "WebPage"),
    "services/bathroom-remodeling/index.html": ("Bathroom Remodeling Plumbing in Denton | McBride & Sons", "Planning a bathroom update? Explore plumbing support for fixture upgrades and layout changes with McBride & Sons Plumbing in Denton and DFW.", "Bathroom Remodeling Plumbing", "WebPage"),
}


def site_url(base, route):
    return urljoin(base, route.removesuffix("index.html"))


def shared_footer(route):
    prefix = "../" * (len(Path(route).parts) - 1) or "./"
    return (ROOT / "templates/footer.html").read_text().replace("{{root}}", prefix).strip()


def shared_announcement():
    return (ROOT / "templates/site-announcement.html").read_text().strip()


def shared_mobile_callbar():
    return (ROOT / "templates/mobile-callbar.html").read_text().strip()


def rebuild_about():
    page = ROOT / "about-us/index.html"
    old = page.read_text()
    head = re.search(r"<head>(.*?)</head>", old, re.S).group(1)
    head = re.sub(r'<script[^>]+src="https://cdn\.tailwindcss\.com"[^>]*></script>', "", head)
    head = re.sub(r"<script>\s*tailwind\.config\s*=.*?</script>", "", head, flags=re.S)
    head = re.sub(r'<link[^>]+href="https://cdnjs\.cloudflare\.com/[^>]*>', "", head)
    head = head.replace("<!-- Tailwind CSS -->", "").replace("<!-- FontAwesome for Authentic Icons -->", "")
    if "about.css" not in head:
        head += f'\n<link rel="stylesheet" href="../assets/css/about.css?v={VERSION}">\n'
    if "site-chrome.css" not in head:
        head += '\n<link rel="stylesheet" href="../assets/css/site-chrome.css?v=20261109-home-chrome-v1">\n'
    header = re.search(r"<header\b.*?</header>", old, re.S).group(0)
    main = (ROOT / "templates/about-main.html").read_text().strip()
    page.write_text(f'''<!doctype html>
<html lang="en-US" data-page="about">
<head>{head}</head>
<body class="mc-about-page">
<a class="mc-about-skip" href="#main">Skip to content</a>
{shared_announcement()}
{header}
{main}
{shared_footer("about-us/index.html")}
{shared_mobile_callbar()}
<script src="../assets/js/main.js?v=20261109-svg-close-v2" defer></script><script src="../assets/js/site-nav.js?v=20261028-menu-v1" defer></script>
</body></html>
''')


def metadata(base, route, title, description, label, page_type):
    canonical = site_url(base, route)
    prefix = "../" * (len(Path(route).parts) - 1) or "./"
    image = urljoin(base, "assets/images/social/mcbride-social-card.jpg")
    logo = urljoin(base, "assets/images/mcbride-logo.webp")
    business_id = "https://mcbrideandsonsplumbing.com/#business"
    graph = [
        {"@type": "WebSite", "@id": base + "#website", "url": base, "name": "McBride & Sons Plumbing", "inLanguage": "en-US"},
        {"@type": "Plumber", "@id": business_id, "name": "McBride & Sons Plumbing", "url": "https://mcbrideandsonsplumbing.com/", "telephone": "+18179013328", "email": "owner@mcbrideandsonsplumbing.com", "logo": logo, "image": image, "description": "Family-owned plumbing serving Denton and the DFW area, with a family service legacy dating back to 1953.", "areaServed": ["Denton, Texas", "Dallas–Fort Worth, Texas"]},
        {"@type": page_type, "@id": canonical + "#webpage", "url": canonical, "name": title, "description": description, "inLanguage": "en-US", "isPartOf": {"@id": base + "#website"}, "about": {"@id": business_id}, "primaryImageOfPage": {"@type": "ImageObject", "url": image, "width": 1200, "height": 630}},
    ]
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": base}]
    if route.startswith("services/") and route != "services/index.html":
        crumbs.append({"@type": "ListItem", "position": 2, "name": "Services", "item": urljoin(base, "services/")})
        graph.append({"@type": "Service", "@id": canonical + "#service", "name": label, "serviceType": label, "url": canonical, "provider": {"@id": business_id}, "areaServed": ["Denton, Texas", "Dallas–Fort Worth, Texas"]})
        graph[2]["mainEntity"] = {"@id": canonical + "#service"}
    if route != "index.html":
        crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1, "name": label, "item": canonical})
        graph.append({"@type": "BreadcrumbList", "@id": canonical + "#breadcrumbs", "itemListElement": crumbs})
        graph[2]["breadcrumb"] = {"@id": canonical + "#breadcrumbs"}
    esc = lambda text: html.escape(text, quote=True)
    fields = [
        ("property", "og:type", "website"), ("property", "og:locale", "en_US"),
        ("property", "og:site_name", "McBride & Sons Plumbing"),
        ("property", "og:title", title), ("property", "og:description", description),
        ("property", "og:url", canonical), ("property", "og:image", image),
        ("property", "og:image:secure_url", image), ("property", "og:image:type", "image/jpeg"),
        ("property", "og:image:width", "1200"), ("property", "og:image:height", "630"),
        ("property", "og:image:alt", "McBride & Sons Plumbing — Service With Integrity. Denton & DFW."),
        ("name", "twitter:card", "summary_large_image"), ("name", "twitter:title", title),
        ("name", "twitter:description", description), ("name", "twitter:image", image),
        ("name", "twitter:image:alt", "McBride & Sons Plumbing — Service With Integrity. Denton & DFW."),
    ]
    tags = ["<!-- BEGIN GENERATED SEO -->", f"<title>{esc(title)}</title>",
        f'<meta name="description" content="{esc(description)}">',
        '<meta name="robots" content="noindex, nofollow">',
        '<meta name="theme-color" content="#173f35">',
        f'<link rel="canonical" href="{esc(canonical)}">',
        f'<link rel="icon" href="{prefix}assets/icons/favicon.svg?v={VERSION}" type="image/svg+xml">',
        f'<link rel="icon" href="{prefix}favicon.ico?v={VERSION}" sizes="any">',
        f'<link rel="icon" href="{prefix}assets/icons/favicon-32.png?v={VERSION}" type="image/png" sizes="32x32">',
        f'<link rel="apple-touch-icon" href="{prefix}assets/icons/apple-touch-icon.png?v={VERSION}" sizes="180x180">',
        f'<link rel="manifest" href="{prefix}site.webmanifest?v={VERSION}">',
    ]
    tags += [f'<meta {kind}="{key}" content="{esc(value)}">' for kind, key, value in fields]
    tags += ['<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace("<", "\\u003c") + '</script>', "<!-- END GENERATED SEO -->"]
    return "\n".join(tags)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default=DEFAULT_URL)
    args = parser.parse_args()
    base = args.base_url.rstrip("/") + "/"
    if not base.startswith("https://"):
        parser.error("The deployed base URL must use HTTPS.")
    rebuild_about()
    for route, values in PAGES.items():
        path = ROOT / route
        source = path.read_text()
        source = re.sub(r"<footer\b.*?</footer>", lambda _: shared_footer(route), source, count=1, flags=re.S)
        source = source.replace("Licensed &amp; Insured", "Family-Owned Plumbing")
        source = source.replace("pb-20 md:pb-0", "")
        source = re.sub(r"<!-- BEGIN GENERATED SEO -->.*?<!-- END GENERATED SEO -->", "", source, flags=re.S)
        source = re.sub(r"<title\b[^>]*>.*?</title>", "", source, flags=re.S | re.I)
        def keep_meta(match):
            tag = match.group(0)
            return "" if re.search(r'(?:name|property)\s*=\s*[\"\'](?:description|robots|theme-color|og:[^\"\']+|twitter:[^\"\']+)[\"\']', tag, re.I) else tag
        source = re.sub(r"<meta\b[^>]*>", keep_meta, source, flags=re.I)
        prefix = "../" * (len(Path(route).parts) - 1) or "./"
        if "shared-footer.css" not in source:
            source = source.replace("</head>", f'<link rel="stylesheet" href="{prefix}assets/css/shared-footer.css?v={VERSION}">\n</head>')
        source = source.replace("</head>", metadata(base, route, *values) + "\n</head>")
        path.write_text("\n".join(line.rstrip() for line in source.splitlines()) + "\n")
    entries = "\n".join(f"  <url><loc>{html.escape(site_url(base, route))}</loc></url>" for route in PAGES)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n')
    (ROOT / "robots.txt").write_text(f"# Design demo: each HTML page retains its noindex directive.\n# Crawling is allowed so link previews can read Open Graph metadata.\nUser-agent: *\nAllow: /\n\nSitemap: {base}sitemap.xml\n")
    manifest = {"name": "McBride & Sons Plumbing", "short_name": "McBride", "start_url": "./", "scope": "./", "display": "browser", "background_color": "#173f35", "theme_color": "#173f35", "icons": [{"src": "assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png"}]}
    (ROOT / "site.webmanifest").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Updated {len(PAGES)} pages, shared footer, sitemap, robots and manifest for {base}; demo noindex retained.")


if __name__ == "__main__":
    main()
