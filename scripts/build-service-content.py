#!/usr/bin/env python3
"""Integrate original Atrezzo component contracts into McBride service pages."""
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "content/service-content.json").read_text())
VERSION = "20261109-atlas-photo-v1"
PHOTOS = {
    "drain-cleaning": ("mcbride-sons-plumbing-drain-cleaning-service-technician.webp", 1852, 849, "66% center"),
    "leak-repair": ("mcbride-sons-plumbing-leak-repair-exterior-pipe-service.webp", 1852, 849, "66% center"),
    "hydro-jetting": ("mcbride-sons-plumbing-hydro-jetting-drain-service.webp", 1876, 838, "65% center"),
    "water-heaters": ("mcbride-sons-plumbing-water-heater-service-technician.webp", 1877, 838, "72% center"),
    "drain-sewer-repair": ("mcbride-sons-plumbing-drain-sewer-repair-trench-service.webp", 1864, 844, "70% center"),
    "bathroom-remodeling": ("mcbride-sons-plumbing-bathroom-remodeling-fixture-installation.webp", 1853, 849, "66% center"),
}
# Licensed illustrative Pexels photographs for Atlas chapter 02 only.
# They do not depict McBride work or employees. Keep original local hero/01 imagery.
# Remote-image delivery and mobile focal crops require deployed-browser QA.
SECOND_PHOTOS = {
    "drain-cleaning": ("12142829", "50% center"),      # PVC drain pipework
    "leak-repair": ("15206136", "50% center"),         # visibly leaking pipe
    "hydro-jetting": ("17882785", "55% center"),       # water flowing from pipe; illustrative, not claimed jetting tool
    "water-heaters": ("6436774", "60% center"),       # bathroom interior, water heater reflected
    "drain-sewer-repair": ("37627673", "50% center"),  # drainage pipe in trench
    "bathroom-remodeling": ("27624015", "50% center"),# finished bathroom fixtures, not McBride work
}

def chapter_two_photo(slug, root, fallback):
    entry = SECOND_PHOTOS.get(slug)
    if not entry:
        return fallback
    photo_id, focal = entry
    return (f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&w=1600", 1600, 1067, focal)

PREP = {
    "drain-cleaning": [("Affected fixtures", "Tell us whether the concern involves one drain or several fixtures."), ("When it began", "Mention when you first noticed the problem and whether it has happened before."), ("Drainage pattern", "Describe the flow or backup as clearly as you can, including anything that changes when other fixtures are used.")],
    "leak-repair": [("Visible location", "Describe the area where you can see water, moisture or staining."), ("Timing of the leak", "Let the team know whether water is present continuously or appears only at certain times."), ("Nearby fixtures", "Mention the closest fixture or pipe without assuming that it is the source of the leak.")],
    "hydro-jetting": [("Previous blockages", "Mention recurring problems and approximately when they happened."), ("Affected drains", "Describe whether the concern involves a single fixture or more than one drain."), ("Previous work", "Share any known cleaning or repair history so the team has context for the conversation.")],
    "water-heaters": [("What changed", "Describe the change you have noticed rather than attempting a diagnosis."), ("Your water heater", "If you already know the type of unit, share that information. There is no need to open the equipment."), ("When it started", "Mention when you first noticed the change and whether it is ongoing or intermittent.")],
    "drain-sewer-repair": [("Affected fixtures", "Mention whether the concern is limited to one fixture or appears in several places."), ("Recurring issues", "Tell the team whether the problem is new or has happened before."), ("Other signs", "Describe any observations you can make safely without entering a contaminated area.")],
    "bathroom-remodeling": [("Fixture changes", "List the fixtures involved so the conversation stays focused on the plumbing portion of your plans."), ("Layout decisions", "Mention whether fixtures will stay where they are or move to a different location."), ("Project stage", "Explain whether the bathroom is still being planned or renovation has already begun.")],
    "services": [("Choose a service", "Use the six service categories to identify the closest match to your concern."), ("Describe the concern", "Share what you have observed or the plumbing change you are planning."), ("Contact the team", "Call the business to discuss the next step. Demo forms are for Atrezzo testing only.")],
}
ESC = lambda value: html.escape(value, quote=True)


def image(src, width, height, focal, mobile=False, active=False):
    attrs = 'class="atz-image-mobile"' if mobile else f'data-atz-atlas-photo class="{"is-active" if active else ""}" aria-hidden="true"'
    return f'<img {attrs} src="{ESC(src)}" width="{width}" height="{height}" alt="" loading="lazy" decoding="async" style="--mc-focal:{focal}">'


def build(data):
    slug = data["slug"]
    root = "../" if slug == "services" else "../../"
    primary = PHOTOS["drain-cleaning" if slug == "services" else slug]
    photos = [
        (root + "assets/images/services/" + primary[0], *primary[1:]),
        chapter_two_photo(slug, root, (root + "assets/images/services/" + primary[0], primary[1], primary[2], "38% center")),
        (root + "assets/images/approach/mcbride-sons-plumbing-honest-communication-customer-consultation.webp", 1875, 839, "65% center"),
    ]
    chapters = [{"title": data["overview_title"], "text": data["overview_text"]}, *data["chapters"]]
    articles = []
    for n, (chapter, photo) in enumerate(zip(chapters, photos), 1):
        extra = f'<h4>{ESC(data["conversation_title"])}</h4><p>{ESC(data["conversation_text"])}</p>' if n == 1 else ""
        articles.append(f'''<article class="atz-atlas-item" data-atz-atlas-item data-stage-title="{ESC(chapter['title'])}" id="service-chapter-{n}">
<span class="atz-micro">0{n} / {'OUR SERVICE' if n == 1 else 'PLUMBING INSIGHTS'}</span><h3>{ESC(chapter['title'])}</h3>{image(*photo, mobile=True)}<p>{ESC(chapter['text'])}</p>{extra}<a class="atz-outline-link" href="tel:+18179013328">Discuss your service needs <span aria-hidden="true"><svg class="mc-ui-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9"/></svg></span></a></article>''')
    stage = ''.join(image(*photo, active=n == 0) for n, photo in enumerate(photos))
    dots = ''.join(f'<button type="button" data-atz-atlas-jump aria-label="Go to chapter {n}: {ESC(ch["title"])}"'+(' aria-current="true"' if n == 1 else '')+'></button>' for n, ch in enumerate(chapters, 1))
    atlas = f'''<div class="atz-service-showcase" data-atz-service-showcase><section class="atz-atlas" data-atz-atlas aria-labelledby="service-insights-title"><div class="atz-shell">
<div class="atz-section-lead"><div><span class="atz-micro">YOUR SERVICE, EXPLAINED</span><h2 id="service-insights-title">{ESC(data['education_title'])}</h2></div><p>{ESC(data['education_intro'])}</p></div>
<div class="atz-lead-footer"><span>GENERAL PLUMBING INFORMATION</span><span>01 — 03</span></div><div class="atz-atlas-grid"><div class="atz-atlas-copy">{''.join(articles)}</div>
<div class="atz-atlas-stage">{stage}<div class="atz-atlas-stage-meta"><div><span class="atz-micro">INSIGHT / <span data-atz-atlas-number>01</span></span><strong data-atz-atlas-title>{ESC(chapters[0]['title'])}</strong></div><div class="atz-atlas-dots">{dots}</div></div></div></div>
<p class="mc-photo-note">Illustrative service and consultation scenes. The people shown are not verified McBride &amp; Sons employees or customers; these are not documented company projects.</p></div></section></div>'''
    questions = [question.strip() + '?' for question in data['questions'].split('?') if question.strip()]
    if len(questions) != 3:
        questions = ["Which service best matches your needs?", "What is happening, or what change are you planning?", "How can the team contact you?"]
    cards = []
    for n, ((title, expanded), question) in enumerate(zip(PREP[slug], questions), 1):
        cards.append(f'''<details class="atc-process-card"><summary><span class="atc-process-top"><span>0{n} / BEFORE YOU CALL</span><span class="atc-process-plus" aria-hidden="true">+</span></span><span class="atc-process-title">{ESC(title)}</span><span class="atc-process-summary">{ESC(question)}</span><span class="atc-process-action">More guidance <span aria-hidden="true"><svg class="mc-ui-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9"/></svg></span></span></summary><div class="atc-process-expanded"><p>{ESC(expanded)}</p></div></details>''')
    prep = f'''<section class="mc-preparation" aria-labelledby="before-call-title"><div class="mc-content-wrap"><div class="mc-content-head"><div><span class="mc-eyebrow">A LITTLE CONTEXT HELPS</span><h2 id="before-call-title">Before you call.<br>Three useful details.</h2></div><p>A few observations can make the conversation clearer. Open a topic for guidance on what to share with the team.</p></div><div class="atc atc-process" aria-label="Helpful details to share">{''.join(cards)}</div><div class="mc-before-call-note"><p>{ESC(data['caution'])}</p><a href="tel:+18179013328">Call (817) 901-3328 <svg class="mc-ui-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9"/></svg></a></div></div></section>'''
    related = ""
    if data['related']:
        mosaic = []
        for n, item in enumerate(data['related'], 1):
            related_slug = Path(item['href']).parts[-2]
            photo = PHOTOS[related_slug]
            name = item['name']
            mosaic.append(f'''<a class="atc-mosaic-card {'atc-mosaic-card--lead' if n == 1 else 'atc-mosaic-card--secondary'}" href="{ESC(item['href'])}" aria-label="Explore {ESC(name)}"><img src="{root}assets/images/services/{photo[0]}" width="{photo[1]}" height="{photo[2]}" alt="" loading="lazy" decoding="async" style="object-position:{photo[3]}"><span class="atc-mosaic-top"><span>0{n} / RELATED SERVICE</span><span aria-hidden="true"><svg class="mc-ui-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9"/></svg></span></span><span class="atc-mosaic-copy"><span>EXPLORE YOUR OPTIONS</span><strong>{ESC(name)}</strong>{'<span>Learn more about this service and discuss your needs with the team.</span>' if n == 1 else ''}</span></a>''')
        mosaic.append(f'''<a class="atc-mosaic-card atc-mosaic-card--third" href="{root}about-us/index.html"><img src="{root}assets/images/michael-mcbride-ii.webp" width="1254" height="1254" alt="Portrait of Michael McBride II" loading="lazy" decoding="async"><span class="atc-mosaic-top"><span>03 / THE FAMILY BEHIND THE NAME</span><span aria-hidden="true"><svg class="mc-ui-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9"/></svg></span></span><span class="atc-mosaic-copy"><span>SERVICE WITH INTEGRITY</span><strong>Meet the McBride family.</strong></span></a>''')
        related = f'''<section class="mc-related" aria-labelledby="related-services-title"><div class="mc-content-wrap"><div class="mc-content-head"><div><span class="mc-eyebrow">KEEP EXPLORING</span><h2 id="related-services-title">More ways<br>we can help.</h2></div><p>Explore related plumbing services, or learn about the family behind McBride &amp; Sons Plumbing.</p></div><div class="atc atc-mosaic" aria-label="Related services and family story">{''.join(mosaic)}</div><p class="mc-photo-note">Service photographs are illustrative. The family portrait is an authentic supplied McBride image.</p></div></section>'''
    return '<!-- BEGIN MCBRIDE ATREZZO CONTENT -->\n<div class="mc-service-content">' + atlas + prep + related + '</div>\n<!-- END MCBRIDE ATREZZO CONTENT -->'


if __name__ == "__main__":
    for data in DATA.values():
        page = ROOT / data['route']
        source = page.read_text()
        component = build(data)
        if '<!-- BEGIN MCBRIDE ATREZZO CONTENT -->' in source:
            source = re.sub(r'<!-- BEGIN MCBRIDE ATREZZO CONTENT -->.*?<!-- END MCBRIDE ATREZZO CONTENT -->', lambda _: component, source, flags=re.S)
        elif data['slug'] == 'services':
            source = re.sub(r'<section class="at-service-education".*?</section>', lambda _: component, source, count=1, flags=re.S)
        else:
            start = source.index('<section class="py-16')
            end = source.index('<section class="at-reviews"', start)
            source = source[:start] + component + '\n\n' + source[end:]
        root = '../' if data['slug'] == 'services' else '../../'
        if 'assets/atrezzo/service-showcase.css' not in source:
            resources = f'''<link rel="stylesheet" href="{root}assets/atrezzo/service-showcase.css?v={VERSION}">
<link rel="stylesheet" href="{root}assets/atrezzo/cards-01.css?v={VERSION}">
<link rel="stylesheet" href="{root}assets/css/service-content-atrezzo.css?v={VERSION}">
<script src="{root}assets/atrezzo/service-showcase.js?v={VERSION}" defer></script>\n'''
            source = source.replace('</head>', resources + '</head>')
        if data['slug'] in PHOTOS:
            photo = PHOTOS[data['slug']]
            source = re.sub(r'(<section class="detail-hero" style=")[^"]*(")', lambda m: m[1]+f'--at-service-image:url({root}assets/images/services/{photo[0]});--at-service-photo-position:{photo[3]}'+m[2], source, count=1)
            source = source.replace('Illustrative stock photography, not McBride &amp; Sons completed work or employees.', 'Illustrative service scene, not McBride &amp; Sons completed work or employees.')
        page.write_text(source)
    print('Integrated Atrezzo Atlas + native Open Process Cards in 7 pages; Visual Feature Mosaic in 6 detail pages.')
