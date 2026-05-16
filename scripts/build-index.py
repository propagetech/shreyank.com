#!/usr/bin/env python3
"""Build single-page index.html and redirect stubs for legacy page URLs."""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

from site_nav import home_nav, whatsapp_float

PROJECT_ROWS = open(os.path.join(SCRIPTS, "project-rows.html"), encoding="utf-8").read()

REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0;url={url}">
  <link rel="canonical" href="https://www.shreyank.com/{canonical}">
  <title>Redirecting…</title>
  <script>location.replace("{url}");</script>
</head>
<body>
  <p>This page has moved. <a href="{url}">Continue</a></p>
</body>
</html>
"""


def panel(section_id, banner_class, heading_id, title, lead, inner):
    lead_html = f'\n          <p class="lead">{lead}</p>' if lead else ""
    return f"""    <section id="{section_id}" class="page-panel page-panel--{banner_class}" aria-labelledby="{heading_id}">
      <div class="page-banner page-banner--{banner_class}">
        <div class="container container--narrow">
          <h2 id="{heading_id}">{title}</h2>{lead_html}
        </div>
      </div>
      <div class="page-panel__body">
{inner}
      </div>
    </section>"""


RECORDING_INNER = """        <div class="container container--narrow content-stack content-stack--tight">
          <ul class="service-list">
            <li>Production Sound Mixing (Sync Sound)</li>
            <li>Ambience Recording</li>
            <li>FX Recording</li>
            <li>Foley Recording</li>
          </ul>
          <div class="gear-section">
            <h3 class="gear-section__title">Gear I often use</h3>
            <section class="gear-category"><h4>Mixer/Recorder</h4><ul class="gear-list">
              <li>Sound Devices - 788T, 688, 664, 633, 302, Mix Pre 10T, Mix Pre 6</li>
              <li>Deva - 5.8</li>
            </ul></section>
            <section class="gear-category"><h4>Boom</h4><ul class="gear-list">
              <li>Schoeps - MK41, Super CMIT, CMIT 5U, Mini CMIT</li>
              <li>Sennheiser - MKH 60, 50, 416, 8060</li>
              <li>Sanken - CS3e</li>
              <li>DPA - 4017B</li>
            </ul></section>
            <section class="gear-category"><h4>Wireless Lavalier System</h4><ul class="gear-list">
              <li>Lectrosonics with Sanken COS-11/DPA 4060 capsule</li>
            </ul></section>
            <section class="gear-category"><h4>For Ambience</h4><ul class="gear-list">
              <li>Sennheiser MKH 50-30 MS pair</li>
              <li>MKH 418</li>
              <li>2 × MKH 50 in XY or AB configuration</li>
              <li>Holofone</li>
              <li>2 × Line Audio CM3 ORTF</li>
            </ul></section>
            <section class="gear-category"><h4>For FX &amp; Location Foley</h4><ul class="gear-list">
              <li>Sennheiser MKH 60/416</li>
            </ul></section>
            <section class="gear-category"><h4>For Studio Foley</h4><ul class="gear-list">
              <li>Sennheiser MKH 60</li>
              <li>Rode NT1, NT2A</li>
              <li>Schoeps CMC6-MK41</li>
              <li>Neumann U 87, TLM 103</li>
            </ul></section>
          </div>
        </div>""".replace("<div ", "<div ").replace("</div>", "</div>")

DESIGN_INNER = """        <div class="container container--narrow content-stack content-stack--tight">
          <ul class="service-list">
            <li>Production tracks re-conform</li>
            <li>Dialogue edit</li>
            <li>Ambience edit</li>
            <li>FX edit</li>
            <li>Foley edit</li>
            <li>Mix</li>
          </ul>
          <div class="gear-section">
            <section class="gear-category"><h3>DAW &amp; Plugins</h3><ul class="gear-list">
              <li>Pro Tools Ultimate 2020.9 Perpetual</li>
              <li>Izotope RX 8 Advanced</li>
              <li>Fab Filter</li>
              <li>Altiverb</li>
            </ul></section>
          </div>
        </div>"""

PROJECTS_INNER = f"""        <div class="container container--narrow">
{PROJECT_ROWS}
        </div>"""

RESOURCES_INNER = """        <div class="container container--narrow">
          <section class="resource-group"><h3>Books</h3><ul class="resource-list">
            <li><strong>Audio-Vision</strong> - Michel Chion</li>
            <li><strong>Notes on the Cinematographer</strong> - Robert Bresson</li>
            <li><strong>Master Handbook of Acoustics</strong> - F. Alton Everest</li>
            <li><a href="http://www.euppublishing.com/loi/sound" rel="noopener noreferrer">The New Soundtrack</a></li>
          </ul></section>
          <section class="resource-group"><h3>Podcasts</h3><ul class="resource-list">
            <li><a href="http://tonebenderspodcast.com/" rel="noopener noreferrer">Tonebenders</a></li>
            <li><a href="http://soundworkscollection.com/news/category/AudioPodcast" rel="noopener noreferrer">Soundworks Collection</a></li>
            <li><a href="http://smartcast.smartpostsound.com/" rel="noopener noreferrer">Smartcast</a></li>
          </ul></section>
          <section class="resource-group"><h3>Websites &amp; tools</h3><ul class="resource-list">
            <li><a href="http://filmsound.org/" rel="noopener noreferrer">FilmSound.org</a></li>
            <li><a href="https://www.schoolofsound.co.uk/sos/audio-and-video-archives/" rel="noopener noreferrer">School of Sound - Archives</a></li>
            <li><a href="http://designingsound.org/" rel="noopener noreferrer">Designing Sound</a></li>
            <li><a href="https://amcoustics.com/tools/amroc" rel="noopener noreferrer">Amroc</a></li>
            <li><a href="http://foley-artistry.blogspot.in/" rel="noopener noreferrer">Foley Artistry</a></li>
            <li><a href="http://duc.avid.com/" rel="noopener noreferrer">Avid Pro Tools Community</a></li>
            <li><a href="http://soundrolling.com/" rel="noopener noreferrer">Sound Rolling</a></li>
          </ul></section>
          <section class="resource-group"><h3>Blogs</h3><ul class="resource-list">
            <li><a href="http://markmangini.com/Mark_Mangini/Blog/Blog.html" rel="noopener noreferrer">Mark Mangini</a></li>
            <li><a href="https://randythomblog.wordpress.com/" rel="noopener noreferrer">Randy Thom</a></li>
            <li><a href="http://www.musicofsound.co.nz/blog/" rel="noopener noreferrer">Tim Prebble</a></li>
          </ul></section>
        </div>"""

CONTACT_INNER = """        <div class="container container--narrow contact-details">
          <ul>
            <li><a href="tel:+919900117364">+91 9900 117 364</a></li>
            <li><a href="tel:+918600266468">+91 8600 266 468</a></li>
            <li><a href="mailto:shreyanknanjappa@gmail.com">shreyanknanjappa@gmail.com</a></li>
          </ul>
        </div>"""


def build_sections():
    return "\n".join(
        [
            panel(
                "projects",
                "projects",
                "projects-heading",
                "Projects",
                "Features, documentaries, shorts, and series.",
                PROJECTS_INNER,
            ),
            panel(
                "sound-recording",
                "recording",
                "sound-recording-heading",
                "Sound Recording",
                "",
                RECORDING_INNER,
            ),
            panel(
                "sound-design",
                "design",
                "sound-design-heading",
                "Sound Design",
                "",
                DESIGN_INNER,
            ),
            panel(
                "resources",
                "resources",
                "resources-heading",
                "Resources",
                "Books, podcasts, and sites for film sound craft.",
                RESOURCES_INNER,
            ),
            panel(
                "contact",
                "contact",
                "contact-heading",
                "Contact",
                "",
                CONTACT_INNER,
            ),
        ]
    )


INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Shreyank Nanjappa - Production Sound Mixer &amp; Sound Designer</title>
  <meta name="description" content="Bengaluru-based production sound mixer and sound designer. Credits include Article 15, Kabir Singh, and The Elephant Whisperers.">
  <link rel="canonical" href="https://www.shreyank.com/">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.shreyank.com/">
  <meta property="og:title" content="Shreyank Nanjappa - Film Sound">
  <meta property="og:description" content="Production sound mixing and sound design for feature films, documentaries, and series.">
  <meta property="og:locale" content="en_IN">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:site" content="@NShreyank">
  <link rel="icon" href="assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="assets/images/site/favicon.webp" type="image/webp" sizes="32x32">
  <link rel="apple-touch-icon" href="assets/images/site/favicon.webp">
  <meta property="og:image" content="https://www.shreyank.com/assets/images/site/og-default.webp">
  <link rel="manifest" href="site.webmanifest">
  <meta name="theme-color" content="#000000">
  <script src="assets/js/theme-init.js"></script>
  <script src="assets/js/layout-width-init.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Quicksand:wght@300..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/components.css">
  <link rel="stylesheet" href="assets/css/responsive.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{"@type": "WebSite", "url": "https://www.shreyank.com/", "name": "Shreyank Nanjappa"}},
      {{"@type": "Person", "name": "Shreyank Nanjappa", "jobTitle": "Production Sound Mixer and Sound Designer", "email": "shreyanknanjappa@gmail.com", "telephone": "+91-9900117364"}}
    ]
  }}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <header class="site-header">
    <div class="container site-header__inner">
      <a class="site-logo" href="#home">
        Shreyank Nanjappa
        <span>Film Sound</span>
      </a>
      <div class="header-actions">
        <button type="button" class="nav-toggle" data-nav-toggle aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 7h16"/><path d="M4 12h16"/><path d="M4 17h16"/></svg>
        </button>
      </div>
      <nav id="site-nav" class="site-nav" aria-label="Primary">
        <ul>
{nav}
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
    <section id="home" class="hero hero--photo" aria-labelledby="hero-heading">
      <div class="container hero__content">
        <h1 id="hero-heading">Shreyank Nanjappa</h1>
        <p class="hero__tagline">Sound Recording | Sound Design | Bangalore / Mumbai</p>
        <p class="hero__contact-line">
          <a href="tel:+919900117364">9900117364</a>
          <span aria-hidden="true"> | </span>
          <a href="tel:+918600266468">8600266468</a>
          <span aria-hidden="true"> | </span>
          <a href="mailto:shreyanknanjappa@gmail.com">shreyanknanjappa@gmail.com</a>
        </p>
        <p class="hero__credibility">Production sound mixer on the Academy Award-winning documentary short <em>The Elephant Whisperers</em>. Credits include <em>Article 15</em>, <em>Kabir Singh</em>, and <em>Nocturnes</em>.</p>
      </div>
    </section>

{sections}
  </main>

  <footer class="site-footer">
    <div class="container footer-bottom">
      <span>© <span id="year"></span> Shreyank Nanjappa</span>
      <p class="footer-tagline">Production sound mixer and sound designer for feature films, documentaries, and series.</p>
      <span>Bengaluru · Mumbai · India</span>
    </div>
  </footer>

{whatsapp}
  <script>document.getElementById("year").textContent = new Date().getFullYear();</script>
  <script src="assets/js/navigation.js" defer></script>
  <script src="assets/js/layout-width.js" defer></script>
  <script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def write_redirect(filename, hash_anchor):
    url = f"index.html{hash_anchor}"
    canonical = url.replace("#", "")
    if hash_anchor:
        canonical = "index.html" + hash_anchor
    html = REDIRECT.format(url=url, canonical=canonical.lstrip("/") or "")
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("redirect", filename, "->", url)


if __name__ == "__main__":
    html = INDEX_HTML.format(
        nav=home_nav(),
        sections=build_sections(),
        whatsapp=whatsapp_float(),
    )
    out = os.path.join(ROOT, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote index.html")

    redirects = {
        "home.html": "",
        "projects.html": "#projects",
        "services.html": "#sound-recording",
        "gear.html": "#sound-design",
        "resources.html": "#resources",
        "contact.html": "#contact",
        "about.html": "#home",
    }
    for name, anchor in redirects.items():
        write_redirect(name, anchor)
