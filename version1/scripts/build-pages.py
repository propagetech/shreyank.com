#!/usr/bin/env python3
"""Generate static HTML pages with shared header/footer."""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEADER_TMPL = """  <a class="skip-link" href="#main">Skip to main content</a>
  <header class="site-header">
    <motion></motion>
    <div class="container site-header__inner">
      <a class="site-logo" href="index.html">Shreyank Nanjappa<span>Film Sound</span></a>
      <div class="header-actions">
        <button type="button" class="theme-toggle" data-theme-toggle aria-label="Switch theme">
          <svg class="icon-sun" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
          <svg class="icon-moon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        </button>
        <button type="button" class="nav-toggle" data-nav-toggle aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
        </button>
      </div>
      <nav id="site-nav" class="site-nav" aria-label="Primary">
        <ul>
{nav}
        </ul>
      </nav>
    </div>
  </header>""".replace("<motion></motion>\n    ", "")

FOOTER = """  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <p class="site-logo" style="margin-bottom: var(--space-4);">Shreyank Nanjappa</p>
        <p style="font-size: var(--text-sm); max-width: 24rem;">Production sound mixer and sound designer for feature films, documentaries, and series.</p>
      </div>
      <div>
        <h2>Navigate</h2>
        <ul>
          <li><a href="projects.html">Work</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="gear.html">Gear</a></li>
          <li><a href="resources.html">Resources</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="blog.html">Notes</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="tel:+919900117364">+91 9900 117 364</a></li>
          <li><a href="tel:+918600266468">+91 8600 266 468</a></li>
          <li><a href="mailto:shreyanknanjappa@gmail.com">shreyanknanjappa@gmail.com</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>© <span id="year"></span> Shreyank Nanjappa</span>
      <span>Bengaluru · Mumbai · India</span>
    </div>
  </footer>
  <script>document.getElementById("year").textContent = new Date().getFullYear();</script>
  <script src="assets/js/theme-toggle.js" defer></script>
  <script src="assets/js/navigation.js" defer></script>
{extra}
  <script src="assets/js/main.js" defer></script>""".replace("      </motion>\n    </motion>", "      </div>")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://www.shreyank.com/{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.shreyank.com/{canonical}">
  <meta property="og:title" content="{og}">
  <meta property="og:description" content="{desc}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:site" content="@NShreyank">
  <link rel="icon" href="assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="assets/images/site/favicon.webp" type="image/webp" sizes="32x32">
  <link rel="apple-touch-icon" href="assets/images/site/favicon.webp">
  <link rel="manifest" href="site.webmanifest">
  <meta name="theme-color" content="#1c1917">
  <script src="assets/js/theme-init.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/components.css">
  <link rel="stylesheet" href="assets/css/responsive.css">
  <link rel="stylesheet" href="assets/css/article.css">
{schema}
</head>
<body>
"""


def nav(active):
    links = [
        ("projects.html", "Work"),
        ("services.html", "Services"),
        ("gear.html", "Gear"),
        ("resources.html", "Resources"),
        ("about.html", "About"),
        ("blog.html", "Notes"),
        ("contact.html", "Contact"),
    ]
    lines = []
    for href, label in links:
        cur = ' aria-current="page"' if href == active else ""
        lines.append(f'          <li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(lines)


def write_page(name, title, desc, body, schema="", extra=""):
    canonical = name if name != "index.html" else ""
    og = title.split("-")[0].strip() if "-" in title else title
    html = HEAD.format(title=title, desc=desc, canonical=canonical, og=og, schema=schema)
    html += HEADER_TMPL.format(nav=nav(name))
    html += f"\n  <main id=\"main\">\n{body}\n  </main>\n\n"
    html += FOOTER.format(extra=extra)
    html += "\n</body>\n</html>\n"
    path = os.path.join(ROOT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)


PROJECT_ROWS = open(os.path.join(ROOT, "scripts", "project-rows.html")).read() if os.path.exists(os.path.join(ROOT, "scripts", "project-rows.html")) else ""

SERVICES_BODY = '''    <motion></motion>
    <div class="page-header container">
      <p class="eyebrow">Services</p>
      <h1>Sound services for film &amp; television</h1>
      <p class="lead">Clear scope, reliable workflows, and material that editorial and post can build on-from location through pre-mix.</p>
    </div>
    <motion></motion>
    <div class="container container--narrow">
      <article class="service-block" id="production-sound">
        <h2>Production sound mixing</h2>
        <img class="service-visual" src="assets/images/site/sound-recording.webp" alt="" width="800" height="450" loading="lazy">
        <p>On-set sync sound and multitrack recording for features, documentaries, and series. The goal is clean, editable dialogue and production effects captured with correct perspective and minimal ADR.</p>
        <p><strong>Includes:</strong> boom and wireless lavs, multitrack mix to recorder, timecode sync, daily sound reports, and handoff to editorial.</p>
        <p><strong>When it matters:</strong> projects shooting sync, interiors with controlled noise, and locations where performance cannot be recreated in ADR.</p>
      </article>
      <article class="service-block" id="sync-sound">
        <h2>Sync sound</h2>
        <p>Capturing vocal performance on set so actors are not asked to re-voice emotion, timing, and texture in a studio later.</p>
        <p><strong>Approach:</strong> scout acoustics, coordinate with camera and AD, protect dialogue in difficult environments, and document issues for post.</p>
      </article>
      <article class="service-block" id="location-recording">
        <h2>Location sound recording</h2>
        <p>Full location sound department support-dialogue, plant mics where appropriate, and communication with production on noise control.</p>
      </article>
      <article class="service-block" id="ambience">
        <h2>Ambience recording</h2>
        <p>MS, ORTF, and spaced-pair recordings tailored to picture geography and editorial needs-room tones, exteriors, and signature environments.</p>
      </article>
      <article class="service-block" id="fx-recording">
        <h2>FX recording</h2>
        <p>Production effects and specific sound events recorded on location or in controlled environments for editorial and design.</p>
      </article>
      <article class="service-block" id="foley-recording">
        <h2>Foley recording</h2>
        <p>Location and studio foley with attention to performance, perspective, and sync-supervision available for features.</p>
      </article>
      <article class="service-block" id="dialogue-edit">
        <h2>Dialogue editing</h2>
        <p>Assembly, cleaning, and preparation of dialogue tracks-RX workflows where needed, consistent nomenclature, and edit-friendly sessions.</p>
      </article>
      <article class="service-block" id="sound-design">
        <h2>Sound design &amp; editorial</h2>
        <img class="service-visual" src="assets/images/site/sound-design.webp" alt="" width="800" height="450" loading="lazy">
        <p>Dialogue, ambience, effects, and foley editorial through pre-mix. Production track re-conform when picture changes.</p>
        <p><strong>Includes:</strong> tracklay prep, perspective-appropriate effects, and support through preview mixes.</p>
      </article>
      <article class="service-block" id="post-support">
        <h2>Post-production support</h2>
        <p>Consultation on workflow, deliverables, and technical requirements for Indian and international finishing paths-including DCP-related audio checks.</p>
      </article>
      <div class="cta-band" style="margin-top: var(--space-12);">
        <h2>Discuss scope for your project</h2>
        <p>Share format, schedule, and locations-a brief call is usually enough to align kit and crew.</p>
        <a class="btn btn--primary" href="contact.html">Contact</a>
      </div>
    </div>'''.replace("<motion></motion>\n    ", "").replace("    <motion></motion>\n    ", "")

GEAR_BODY = '''    <div class="page-header container">
      <p class="eyebrow">Technical</p>
      <h1>Gear &amp; workflow</h1>
      <p class="lead">Kit chosen for reliability on Indian locations and compatibility with standard post pipelines.</p>
    </div>
    <div class="container container--narrow">
      <section class="gear-category"><h2>Recorders &amp; mixers</h2><ul class="gear-list">
        <li>Sound Devices 788T, 688, 664, 633, 302</li>
        <li>Sound Devices MixPre-10T, MixPre-6</li>
        <li>Deva 5.8</li>
      </ul></section>
      <section class="gear-category"><h2>Boom microphones</h2><ul class="gear-list">
        <li>Schoeps MK41, Super CMIT, CMIT 5U, Mini CMIT</li>
        <li>Sennheiser MKH 60, 50, 416, 8060</li>
        <li>Sanken CS-3e</li>
        <li>DPA 4017B</li>
      </ul></section>
      <section class="gear-category"><h2>Wireless</h2><ul class="gear-list">
        <li>Lectrosonics systems with Sanken COS-11 / DPA 4060 capsules</li>
      </ul></section>
      <section class="gear-category"><h2>Ambience &amp; stereo</h2><ul class="gear-list">
        <li>Sennheiser MKH 50/30 MS pair</li>
        <li>Sennheiser MKH 418</li>
        <li>MKH 50 pair - XY or AB</li>
        <li>Holophone</li>
        <li>Line Audio CM3 - ORTF pair</li>
      </ul></section>
      <section class="gear-category"><h2>FX &amp; location foley</h2><ul class="gear-list"><li>Sennheiser MKH 60 / 416</li></ul></section>
      <section class="gear-category"><h2>Studio foley</h2><ul class="gear-list">
        <li>Sennheiser MKH 60</li>
        <li>Rode NT1, NT2-A</li>
        <li>Schoeps CMC6-MK41</li>
        <li>Neumann U 87, TLM 103</li>
      </ul></section>
      <section class="gear-category"><h2>DAW &amp; plugins</h2><ul class="gear-list">
        <li>Avid Pro Tools Ultimate</li>
        <li>iZotope RX Advanced</li>
        <li>FabFilter suite</li>
        <li>Audio Ease Altiverb</li>
      </ul></section>
    </motion>
    </div>'''.replace("    </motion>\n    </div>", "    </div>")

RESOURCES_BODY = '''    <div class="page-header container">
      <p class="eyebrow">Library</p>
      <h1>Resources</h1>
      <p class="lead">Books, podcasts, and sites worth returning to-for craft, theory, and practical post work.</p>
    </div>
    <div class="container container--narrow">
      <section class="resource-group"><h2>Books</h2><ul class="resource-list">
        <li><strong>Audio-Vision</strong> - Michel Chion<span>Sound and image relationships; essential reading.</span></li>
        <li><strong>Notes on the Cinematographer</strong> - Robert Bresson<span>Concise craft thinking applicable to sound discipline.</span></li>
        <li><strong>Master Handbook of Acoustics</strong> - F. Alton Everest<span>Room acoustics and practical measurement.</span></li>
        <li><a href="http://www.euppublishing.com/loi/sound" rel="noopener noreferrer">The New Soundtrack</a><span>Journal - Edinburgh University Press</span></li>
      </ul></section>
      <section class="resource-group"><h2>Podcasts</h2><ul class="resource-list">
        <li><a href="http://tonebenderspodcast.com/" rel="noopener noreferrer">Tonebenders</a></li>
        <li><a href="http://soundworkscollection.com/news/category/AudioPodcast" rel="noopener noreferrer">Soundworks Collection</a></li>
        <li><a href="http://smartcast.smartpostsound.com/" rel="noopener noreferrer">Smartcast</a></li>
      </ul></section>
      <section class="resource-group"><h2>Websites &amp; tools</h2><ul class="resource-list">
        <li><a href="http://filmsound.org/" rel="noopener noreferrer">FilmSound.org</a></li>
        <li><a href="https://www.schoolofsound.co.uk/sos/audio-and-video-archives/" rel="noopener noreferrer">School of Sound - Archives</a></li>
        <li><a href="http://designingsound.org/" rel="noopener noreferrer">Designing Sound</a></li>
        <li><a href="https://amcoustics.com/tools/amroc" rel="noopener noreferrer">Amroc - Room modes calculator</a></li>
        <li><a href="http://foley-artistry.blogspot.in/" rel="noopener noreferrer">Foley Artistry</a></li>
        <li><a href="http://duc.avid.com/" rel="noopener noreferrer">Avid Pro Tools Community</a></li>
        <li><a href="http://soundrolling.com/" rel="noopener noreferrer">Sound Rolling</a></li>
      </ul></section>
      <section class="resource-group"><h2>Blogs</h2><ul class="resource-list">
        <li><a href="http://markmangini.com/Mark_Mangini/Blog/Blog.html" rel="noopener noreferrer">Mark Mangini</a></li>
        <li><a href="https://randythomblog.wordpress.com/" rel="noopener noreferrer">Randy Thom</a></li>
        <li><a href="http://www.musicofsound.co.nz/blog/" rel="noopener noreferrer">Tim Prebble - Music of Sound</a></li>
      </ul></section>
    </div>'''

ABOUT_BODY = '''    <div class="page-header container">
      <p class="eyebrow">About</p>
      <h1>Shreyank Nanjappa</h1>
      <p class="lead">Production sound mixer and sound designer based in Bengaluru, working across India and internationally.</p>
    </div>
    <div class="container container--narrow">
      <p>Shreyank is a Bengaluru-based sound professional working in production sound mixing and sound design for feature films, documentaries, shorts, and series. He is an alumnus of the Film and Television Institute of India (FTII), where he trained alongside filmmakers whose work has travelled to Cannes, Berlinale, and beyond.</p>
      <p>He served as production sound mixer on <em>The Elephant Whisperers</em>-the Academy Award-winning documentary short-and has production and editorial credits on Hindi and regional features including <em>Article 15</em> and <em>Kabir Singh</em>, as well as festival-selected work with directors such as Payal S Kapadia and Rima Das.</p>
      <h2>Approach to sound</h2>
      <p>Good film sound is invisible until it is not: dialogue you do not strain to hear, ambience that holds space without calling attention, and effects that belong to the frame. On set, that means protecting performance and building tracks editorial can trust. In post, it means editorial that serves picture and rhythm-not decoration.</p>
      <h2>Collaboration</h2>
      <p>Shreyank works closely with directors, producers, and post supervisors from prep through delivery. Communication is direct; expectations on deliverables, schedules, and noise are set early.</p>
      <h2>Availability</h2>
      <p>Based in Bengaluru with regular projects in Mumbai and on location across India. International collaborations by arrangement.</p>
    </div>'''

CONTACT_BODY = '''    <motion></motion>
    <div class="page-header container">
      <p class="eyebrow">Contact</p>
      <h1>Enquiries</h1>
      <p class="lead">For production sound, location recording, or sound design-share a brief outline of your project.</p>
    </div>
    <div class="container split">
      <div>
        <h2>Direct contact</h2>
        <ul>
          <li><a href="tel:+919900117364">+91 9900 117 364</a></li>
          <li><a href="tel:+918600266468">+91 8600 266 468</a></li>
          <li><a href="mailto:shreyanknanjappa@gmail.com">shreyanknanjappa@gmail.com</a></li>
        </ul>
        <p><strong>Location:</strong> Bengaluru, India - available Mumbai &amp; on location</p>
        <p><strong>Response:</strong> Typically within 2–3 business days. Urgent production enquiries-call.</p>
        <p class="form-note">This form opens your email client with a pre-filled message. No data is stored on this website.</p>
      </div>
      <form id="contact-form" action="#" method="post" novalidate>
        <div class="form-group">
          <label for="name">Name</label>
          <input type="text" id="name" name="name" required autocomplete="name">
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" required autocomplete="email">
        </div>
        <div class="form-group">
          <label for="category">Enquiry type</label>
          <select id="category" name="category" required>
            <option value="">Select…</option>
            <option value="Production sound / sync">Production sound / sync</option>
            <option value="Sound design / post">Sound design / post</option>
            <option value="Ambience / FX recording">Ambience / FX recording</option>
            <option value="General">General</option>
          </select>
        </div>
        <motion></motion>
        <div class="form-group">
          <label for="message">Project details</label>
          <textarea id="message" name="message" required placeholder="Format, dates, locations, and any links to references."></textarea>
        </div>
        <button type="submit" class="btn btn--primary">Send enquiry</button>
        <p class="form-hint">By submitting, you agree to be contacted about your enquiry. Your message is sent via your email app only.</p>
      </form>
    </div>'''.replace("<motion></motion>\n    ", "").replace("        <motion></motion>\n        ", "")

BLOG_BODY = '''    <div class="page-header container">
      <p class="eyebrow">Notes</p>
      <h1>Writing on film sound</h1>
      <p class="lead">Practical introductions to sync sound, post workflows, and tools-with context for Indian production.</p>
    </div>
    <motion></motion>
    <div class="container container--narrow">
      <div class="card-grid card-grid--2">
        <article class="blog-card">
          <p class="blog-card__date">Sound for film</p>
          <h2><a href="old/blog-sync-sound-requirements.html">Sync sound requirements</a></h2>
          <p>Why sync sound matters, when it is feasible, and what production needs to plan for-especially in India.</p>
          <a class="btn btn--ghost" href="old/blog-sync-sound-requirements.html">Read article</a>
        </article>
        <article class="blog-card">
          <p class="blog-card__date">Post-production</p>
          <h2><a href="old/blog-checking-audio-mxf-after-the-dcp-is-made.html">Checking audio MXF after the DCP</a></h2>
          <p>Technical notes on verifying audio deliverables in the finishing chain.</p>
          <a class="btn btn--ghost" href="old/blog-checking-audio-mxf-after-the-dcp-is-made.html">Read article</a>
        </article>
        <article class="blog-card">
          <p class="blog-card__date">Pro Tools</p>
          <h2><a href="old/blog-shoortcuts.html">Useful Pro Tools shortcuts</a></h2>
          <p>Shortcuts for dialogue, effects, and foley editorial-the ones worth learning first.</p>
          <a class="btn btn--ghost" href="old/blog-shoortcuts.html">Read article</a>
        </article>
      </div>
      <p style="margin-top: var(--space-8); color: var(--color-text-subtle); font-size: var(--text-sm);">Older posts are being migrated to this layout. Categories: sync sound · post · tools.</p>
    </div>'''.replace("    <motion></motion>\n    ", "")

ERROR_BODY = '''    <div class="error-page">
      <p class="error-page__code" aria-hidden="true">404</p>
      <h1>Page not found</h1>
      <p>The page you requested is not here-it may have moved or the link may be outdated.</p>
      <a class="btn btn--primary" href="index.html">Return home</a>
    </div>'''

if __name__ == "__main__":
    # projects
    projects_body = f'''    <div class="page-header container">
      <p class="eyebrow">Filmography</p>
      <h1>Selected work &amp; credits</h1>
      <p class="lead">Features, documentaries, shorts, and series-organized for quick scanning. Filter by role or format.</p>
    </div>
    <div class="container container--narrow">
      <p id="filter-status" class="sr-only" aria-live="polite"></p>
      <div class="filter-bar" data-project-filters role="group" aria-label="Filter projects">
        <button type="button" class="filter-btn" data-filter="all" aria-pressed="true">All</button>
        <button type="button" class="filter-btn" data-filter="recordist" aria-pressed="false">Production sound</button>
        <button type="button" class="filter-btn" data-filter="designer" aria-pressed="false">Sound design</button>
        <button type="button" class="filter-btn" data-filter="dialogue" aria-pressed="false">Dialogue / foley</button>
        <button type="button" class="filter-btn" data-filter="feature" aria-pressed="false">Features</button>
        <button type="button" class="filter-btn" data-filter="documentary" aria-pressed="false">Documentary</button>
        <button type="button" class="filter-btn" data-filter="short" aria-pressed="false">Shorts</button>
      </div>
      <div class="project-list" data-project-list>
{open(os.path.join(ROOT, "scripts", "project-rows.html")).read()}
      </div>
    </div>'''
    write_page(
        "projects.html",
        "Work &amp; Filmography - Shreyank Nanjappa",
        "Film credits including The Elephant Whisperers, Article 15, Kabir Singh, and festival-selected shorts. Production sound and sound design.",
        projects_body,
        schema='  <script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","name":"Filmography","url":"https://www.shreyank.com/projects.html","about":{"@type":"Person","name":"Shreyank Nanjappa"}}</script>',
        extra='  <script src="assets/js/filters.js" defer></script>',
    )
    write_page("services.html", "Services - Shreyank Nanjappa",
        "Production sound mixing, sync sound, location recording, sound design, and post-production support for film and television.",
        SERVICES_BODY)
    write_page("gear.html", "Gear &amp; Technical Setup - Shreyank Nanjappa",
        "Location sound and post-production kit: Sound Devices recorders, Schoeps and Sennheiser microphones, Lectrosonics wireless, Pro Tools.",
        GEAR_BODY)
    write_page("resources.html", "Resources - Shreyank Nanjappa",
        "Curated books, podcasts, blogs, and tools for film sound professionals and students.",
        RESOURCES_BODY)
    write_page("about.html", "About - Shreyank Nanjappa",
        "Bengaluru-based production sound mixer and sound designer. FTII alumnus. Credits across Indian and international film.",
        ABOUT_BODY,
        schema='  <script type="application/ld+json">{"@context":"https://schema.org","@type":"AboutPage","mainEntity":{"@type":"Person","name":"Shreyank Nanjappa","alumniOf":{"@type":"CollegeOrUniversity","name":"Film and Television Institute of India"}}}</script>')
    write_page("contact.html", "Contact - Shreyank Nanjappa",
        "Contact Shreyank Nanjappa for production sound and sound design enquiries. Bengaluru and Mumbai.",
        CONTACT_BODY,
        schema='  <script type="application/ld+json">{"@context":"https://schema.org","@type":"ContactPage","url":"https://www.shreyank.com/contact.html"}</script>',
        extra='  <script src="assets/js/contact-form.js" defer></script>')
    write_page("blog.html", "Notes &amp; Writing - Shreyank Nanjappa",
        "Practical notes on sync sound, post workflows, and film sound craft.",
        BLOG_BODY,
        schema='  <script type="application/ld+json">{"@context":"https://schema.org","@type":"Blog","name":"Shreyank Nanjappa Notes","url":"https://www.shreyank.com/blog.html"}</script>')
    write_page("404.html", "Page Not Found - Shreyank Nanjappa",
        "The page you requested could not be found.",
        ERROR_BODY)
    print("done all pages")
