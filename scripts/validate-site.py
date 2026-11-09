#!/usr/bin/env python3
"""Check metadata, structured data, generated footer and local destinations."""
from collections import Counter
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("generator", ROOT / "scripts/update-site.py")
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


class Tags(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.tags = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


errors = []
descriptions, titles, urls = [], [], []
references = 0
for route in generator.PAGES:
    file = ROOT / route
    source = file.read_text()
    tags = Tags(source).tags
    def check(condition, message):
        if not condition:
            errors.append(f"{route}: {message}")
    check(len(re.findall(r"<h1\b", source)) == 1, "must have one H1")
    check(len(re.findall(r"<title\b", source)) == 1, "must have one title")
    titles.append(re.search(r"<title>(.*?)</title>", source).group(1))
    ids = Counter(attrs["id"] for _, attrs in tags if "id" in attrs)
    check(not any(count > 1 for count in ids.values()), "duplicate IDs")
    metas = [(attrs.get("name", attrs.get("property")), attrs.get("content")) for tag, attrs in tags if tag == "meta"]
    for key in ["description", "robots", "og:title", "og:url", "og:image", "og:image:alt", "twitter:card", "twitter:image"]:
        check(sum(name == key for name, _ in metas) == 1, f"missing or duplicate {key}")
    meta = dict(metas)
    check(meta["robots"] == "noindex, nofollow", "demo noindex must remain")
    check(meta["twitter:card"] == "summary_large_image", "missing large social card")
    descriptions.append(meta["description"])
    canonical = [attrs["href"] for tag, attrs in tags if tag == "link" and attrs.get("rel") == "canonical"]
    check(len(canonical) == 1 and canonical[0] == meta["og:url"], "canonical and og:url differ")
    urls.extend(canonical)
    footer = re.search(r"<footer\b.*?</footer>", source, re.S).group(0)
    check(footer == generator.shared_footer(route), "footer differs from shared template")
    footer_tags = Tags(footer).tags
    check(sum(tag == "a" and "/services/" in attrs.get("href", "") for tag, attrs in footer_tags) >= 6, "footer service links missing")
    check(generator.shared_announcement() in source, "ribbon differs from shared Home component")
    check(generator.shared_mobile_callbar() in source, "mobile callbar differs from shared Home component")
    check("assets/css/site-chrome.css?v=20261109-home-chrome-v1" in source, "missing shared chrome CSS")
    check(source.count('class="site-announcement"') == 1, "duplicate or missing announcement")
    check(source.count('class="mobile-callbar"') == 1, "duplicate or missing callbar")
    check("Licensed &amp; Insured" not in source, "unverified insurance claim")
    check(any(tag == "link" and attrs.get("rel") == "apple-touch-icon" for tag, attrs in tags), "missing Apple icon")
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', source, re.S):
        data = json.loads(block)
        check("aggregateRating" not in block and "foundingDate" not in block, "unverified structured claim")
        check(any(entity["@type"] == "Plumber" for entity in data["@graph"]), "missing plumbing business schema")
    for tag, attrs in tags:
        if tag == "img":
            check("alt" in attrs, "image without alt")
        for attribute in ["href", "src"]:
            ref = attrs.get(attribute)
            if not ref:
                continue
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc:
                continue
            references += 1
            target = file.parent / unquote(parsed.path) if parsed.path else file
            if target.is_dir():
                target = target / "index.html"
            check(target.exists(), f"missing local resource {ref}")
            if parsed.fragment and target.exists() and target.suffix == ".html":
                target_ids = [a.get("id") for _, a in Tags(target.read_text()).tags]
                check(unquote(parsed.fragment) in target_ids, f"missing fragment {ref}")
for values, name in [(titles, "titles"), (descriptions, "descriptions"), (urls, "canonical URLs")]:
    if len(set(values)) != 10:
        errors.append(f"Duplicate {name}")
sitemap = ET.parse(ROOT / "sitemap.xml")
locations = [element.text for element in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
if set(locations) != set(urls):
    errors.append("Sitemap does not match canonical URLs")
manifest = json.loads((ROOT / "site.webmanifest").read_text())
for icon in manifest["icons"]:
    if not (ROOT / icon["src"]).exists():
        errors.append(f"Missing manifest icon {icon['src']}")

# Keep emoji and text-based pictograms out of deployed HTML and maintained assets.
# User-visible controls must use decorative inline SVG icons instead.
EMOJI_OR_GLYPH = re.compile(r"[\\u2190-\\u21ff\\u2600-\\u27bf\\U0001f000-\\U0001faff\\u200d\\ufe0f]")
for file in [*(ROOT / p for p in generator.PAGES),
             *ROOT.glob("assets/js/*.js"), *ROOT.glob("assets/css/*.css"),
             *ROOT.glob("templates/*.html"), *ROOT.glob("scripts/*.py"),
             *ROOT.glob("content/*.json")]:
    if EMOJI_OR_GLYPH.search(file.read_text()):
        errors.append(f"{file.relative_to(ROOT)}: emoji or decorative text glyph detected; use SVG instead")

if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: 10 unique SEO sets, social cards, schema, shared footers and {references} local references. Sitemap, manifest and demo protections valid.")
