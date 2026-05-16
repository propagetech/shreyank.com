#!/usr/bin/env python3
"""Build blog article pages from content fragments."""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

from site_nav import blog_nav, whatsapp_float

BLOG_DIR = os.path.join(ROOT, "blog")
CONTENT_DIR = os.path.join(ROOT, "content", "blog")

HEADER_TMPL = """  <a class="skip-link" href="#main">Skip to main content</a>
  <header class="site-header">
    <div class="container site-header__inner">
      <a class="site-logo" href="../index.html">
        Shreyank Nanjappa
        <span>Film Sound</span>
      </a>
      <div class="header-actions">
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
  </header>"""

FOOTER_TMPL = """  <footer class="site-footer">
    <div class="container footer-bottom">
      <span>© <span id="year"></span> Shreyank Nanjappa</span>
      <p class="footer-tagline">Production sound mixer and sound designer for feature films, documentaries, and series.</p>
      <span>Bengaluru · Mumbai · India</span>
    </div>
  </footer>
{whatsapp}
  <script>document.getElementById("year").textContent = new Date().getFullYear();</script>
  <script src="../assets/js/navigation.js" defer></script>
  <script src="../assets/js/main.js" defer></script>"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Shreyank Nanjappa</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://www.shreyank.com/blog/{slug}.html">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://www.shreyank.com/blog/{slug}.html">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{description}">
  <meta property="article:published_time" content="{iso_date}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@NShreyank">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{description}">
  {og_image}
  <link rel="icon" href="../assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="../assets/images/site/favicon.webp" type="image/webp" sizes="32x32">
  <link rel="apple-touch-icon" href="../assets/images/site/favicon.webp">
  <link rel="manifest" href="../site.webmanifest">
  <meta name="theme-color" content="#000000">
  <script src="../assets/js/theme-init.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Quicksand:wght@300..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="../assets/css/components.css">
  <link rel="stylesheet" href="../assets/css/article.css">
  <link rel="stylesheet" href="../assets/css/responsive.css">
  <script type="application/ld+json">
{schema}
  </script>
</head>
<body>
"""


def related_cards(current_slug, posts):
    items = [p for p in posts if p["slug"] != current_slug][:2]
    html = ['      <div class="card-grid card-grid--2">']
    for p in items:
        card_id = f"blog-card-{p['slug']}"
        html.append(f"""        <article class="blog-card" data-category="{p['category_slug']}">
          <a class="blog-card__link" href="{p['slug']}.html" aria-labelledby="{card_id}">
            <span class="sr-only">Read article: {p['title']}</span>
          </a>
          <span class="tag blog-card__category">{p['category']}</span>
          <h3 id="{card_id}">{p['title']}</h3>
          <p>{p['excerpt']}</p>
          <span class="blog-card__cta" aria-hidden="true">Read article</span>
        </article>""")
    html.append("      </div>")
    return "\n".join(html)


def build_article(post, posts, body_html):
    slug = post["slug"]
    og_image = ""
    if post.get("image"):
        og_image = f'  <meta property="og:image" content="https://www.shreyank.com/assets/images/blog/{post["image"]}">'
    schema = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": post["title"],
            "description": post["description"],
            "datePublished": post["iso_date"],
            "author": {
                "@type": "Person",
                "name": "Shreyank Nanjappa",
                "url": "https://www.shreyank.com/",
            },
            "publisher": {
                "@type": "Person",
                "name": "Shreyank Nanjappa",
            },
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": f"https://www.shreyank.com/blog/{slug}.html",
            },
            "articleSection": post["category"],
            "inLanguage": "en-IN",
        },
        indent=2,
    )

    main = f"""  <main id="main" class="article-layout">
    <article class="article" itemscope itemtype="https://schema.org/BlogPosting">
      <header class="article-hero container">
        <nav class="article-breadcrumb" aria-label="Breadcrumb">
          <a href="../blog.html">← All notes</a>
        </nav>
        <p class="eyebrow">{post['category']}</p>
        <h1 itemprop="headline">{post['title']}</h1>
        {f'<p class="article-hero__deck">{post["deck"]}</p>' if post.get('deck') else ''}
        <div class="article-meta">
          <time datetime="{post['iso_date']}" itemprop="datePublished">{post['display_date']}</time>
          <span>{post['read_time']} read</span>
        </div>
      </header>
      <div class="article-body" itemprop="articleBody">
{body_html}
      </div>
      <aside class="article-author container" aria-labelledby="author-heading-{slug}">
        <div class="article-author__inner">
          <img class="article-author__avatar" src="../assets/images/site/author.webp" alt="Shreyank Nanjappa" width="64" height="64" loading="lazy">
          <div>
            <h2 id="author-heading-{slug}">About the author</h2>
            <p itemprop="author" itemscope itemtype="https://schema.org/Person">
              <span itemprop="name"><strong>Shreyank Nanjappa</strong></span> — production sound mixer and sound designer.
              FTII alumnus. Bengaluru &amp; Mumbai.
            </p>
            <p style="margin-top: var(--space-3);"><a href="../index.html">Home</a> · <a href="../index.html#contact">Contact</a></p>
          </div>
        </div>
      </aside>
      <aside class="article-related" aria-labelledby="related-heading-{slug}">
        <h2 id="related-heading-{slug}">More notes</h2>
{related_cards(slug, posts)}
      </aside>
    </article>
  </main>"""

    html = HEAD.format(
        title=post["title"],
        description=post["description"],
        slug=slug,
        og_title=post["title"],
        iso_date=post["iso_date"],
        og_image=og_image,
        schema=schema,
    )
    html += HEADER_TMPL.format(nav=blog_nav(slug)) + "\n" + main + "\n\n"
    html += FOOTER_TMPL.format(whatsapp=whatsapp_float()) + "\n</body>\n</html>\n"

    path = os.path.join(BLOG_DIR, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


POSTS = [
    {
        "slug": "sync-sound-requirements",
        "title": "Sync Sound Requirements",
        "category": "Sound basics",
        "category_slug": "basics",
        "description": "What sync sound demands from direction, production, actors, camera, crew, and editorial—especially in Indian film production.",
        "excerpt": "Why sync sound matters, when it is feasible, and what every department must commit to on set.",
        "iso_date": "2016-11-16",
        "display_date": "16 November 2016",
        "read_time": "8 min",
        "image": "blog-thumb-1.webp",
        "deck": "A practical introduction to recording dialogue on set—and why it fails when departments are not aligned.",
    },
    {
        "slug": "checking-audio-mxf-after-the-dcp-is-made",
        "title": "Checking Audio MXF after the DCP is made",
        "category": "Technical",
        "category_slug": "technical",
        "description": "How to extract and compare DCP audio MXF files with ffmpeg and Pro Tools—and why track layout matters for festival delivery.",
        "excerpt": "Verifying PCM MXF from a finished DCP against your stereo mix using ffmpeg and phase cancellation in Pro Tools.",
        "iso_date": "2017-02-02",
        "display_date": "2 February 2017",
        "read_time": "7 min",
        "image": "image-24.webp",
        "deck": "After a Berlinale-bound short revealed different sound between two DCPs, I started always checking the sound MXF.",
    },
    {
        "slug": "shoortcuts",
        "title": "Shoortcuts",
        "category": "Sound post",
        "category_slug": "post",
        "description": "Pro Tools shortcuts worth knowing for dialogue, effects, and foley editorial—including delete fades across selected clips.",
        "excerpt": "A short list of Pro Tools shortcuts I use regularly for editorial work—not an exhaustive list.",
        "iso_date": "2016-04-21",
        "display_date": "21 April 2016",
        "read_time": "2 min",
        "image": None,
        "deck": "You do not need every shortcut—only the ones that match the work you actually do.",
    },
]


def blog_listing_cards_html():
    """Blog index cards — keep in sync with article eyebrow, title, and excerpt."""
    lines = ['      <div class="card-grid card-grid--3">']
    for post in POSTS:
        card_id = f"blog-card-{post['slug']}"
        lines.append(
            f"""        <article class="blog-card">
          <a class="blog-card__link" href="blog/{post['slug']}.html" aria-labelledby="{card_id}">
            <span class="sr-only">Read article: {post['title']}</span>
          </a>
          <p class="blog-card__category">{post['category']}</p>
          <h2 id="{card_id}">{post['title']}</h2>
          <p>{post['excerpt']}</p>
          <span class="blog-card__cta" aria-hidden="true">Read article</span>
        </article>"""
        )
    lines.append("      </div>")
    return "\n".join(lines)


def redirect_html(target):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="canonical" href="https://www.shreyank.com{target}">
  <title>Redirecting…</title>
  <script>location.replace("{target}");</script>
</head>
<body>
  <p>This page has moved. <a href="{target}">Continue to the article</a>.</p>
</body>
</html>
"""


if __name__ == "__main__":
    os.makedirs(BLOG_DIR, exist_ok=True)
    for post in POSTS:
        fragment_path = os.path.join(CONTENT_DIR, f"{post['slug']}.html")
        with open(fragment_path, encoding="utf-8") as f:
            body = f.read()
        build_article(post, POSTS, body)

    # Legacy redirects (old filenames at site root / old folder)
    redirects = {
        os.path.join(ROOT, "old", "blog-shoortcuts.html"): "/blog/shoortcuts.html",
        os.path.join(
            ROOT,
            "old",
            "blog-checking-audio-mxf-after-the-dcp-is-made.html",
        ): "/blog/checking-audio-mxf-after-the-dcp-is-made.html",
        os.path.join(ROOT, "old", "blog-sync-sound-requirements.html"): "/blog/sync-sound-requirements.html",
    }
    for path, target in redirects.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(redirect_html(target))
        print("redirect", path)
