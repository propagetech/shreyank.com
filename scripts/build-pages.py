#!/usr/bin/env python3
"""Generate blog index and 404. Main site is built by build-index.py."""

import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

from site_nav import blog_nav, home_nav, whatsapp_float

_build_articles_spec = importlib.util.spec_from_file_location(
    "build_articles",
    os.path.join(SCRIPTS, "build-articles.py"),
)
_build_articles = importlib.util.module_from_spec(_build_articles_spec)
_build_articles_spec.loader.exec_module(_build_articles)

HEADER_TMPL = """  <a class="skip-link" href="#main">Skip to main content</a>
  <header class="site-header">
    <motion></motion>
    <motion class="container site-header__inner">
      <a class="site-logo" href="{logo_href}">Shreyank Nanjappa<span>Film Sound</span></a>
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
    </motion>
  </header>""".replace("<motion></motion>\n    ", "").replace("<motion ", "<div ").replace("</motion>", "</div>")

FOOTER_TMPL = """  <footer class="site-footer">
    <div class="container footer-bottom">
      <span>© <span id="year"></span> Shreyank Nanjappa</span>
      <p class="footer-tagline">Production sound mixer and sound designer for feature films, documentaries, and series.</p>
      <span>Bengaluru · Mumbai · India</span>
    </div>
  </footer>
{whatsapp}
  <script>document.getElementById("year").textContent = new Date().getFullYear();</script>
  <script src="{asset_prefix}assets/js/navigation.js" defer></script>
  <script src="{asset_prefix}assets/js/layout-width.js" defer></script>
{extra}
  <script src="{asset_prefix}assets/js/main.js" defer></script>""".replace("<motion>", "<div>").replace("</motion>", "</div>")

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
  <link rel="icon" href="{asset_prefix}assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="{asset_prefix}assets/images/site/favicon.webp" type="image/webp" sizes="32x32">
  <link rel="apple-touch-icon" href="{asset_prefix}assets/images/site/favicon.webp">
  <link rel="manifest" href="{asset_prefix}site.webmanifest">
  <meta name="theme-color" content="#000000">
  <script src="{asset_prefix}assets/js/theme-init.js"></script>
  <script src="{asset_prefix}assets/js/layout-width-init.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Quicksand:wght@300..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{asset_prefix}assets/css/style.css">
  <link rel="stylesheet" href="{asset_prefix}assets/css/components.css">
  <link rel="stylesheet" href="{asset_prefix}assets/css/responsive.css">
  <link rel="stylesheet" href="{asset_prefix}assets/css/article.css">
{schema}
</head>
<body>
"""


def write_page(name, title, desc, body, schema="", extra="", nav_lines=None, logo_href="index.html"):
    canonical = name if name != "index.html" else ""
    og = title.split("-")[0].strip() if "-" in title else title
    nav_lines = nav_lines if nav_lines is not None else home_nav()
    html = HEAD.format(
        title=title,
        desc=desc,
        canonical=canonical,
        og=og,
        schema=schema,
        asset_prefix="",
    )
    html += HEADER_TMPL.format(nav=nav_lines, logo_href=logo_href)
    html += f'\n  <main id="main">\n{body}\n  </main>\n\n'
    html += FOOTER_TMPL.format(
        asset_prefix="",
        extra=extra,
        whatsapp=whatsapp_float(),
    )
    html += "\n</body>\n</html>\n"
    path = os.path.join(ROOT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)


BLOG_BODY_TMPL = """    <div class="page-banner page-banner--resources container">
      <p class="eyebrow">Blog</p>
      <h1>Writing on film sound</h1>
      <p class="lead">Practical introductions to sync sound, post workflows, and tools-with context for Indian production.</p>
    </div>
    <div class="container">
{cards}
    </div>"""


def blog_body():
    cards = _build_articles.blog_listing_cards_html()
    return BLOG_BODY_TMPL.format(cards=cards)


ERROR_BODY = """    <div class="error-page">
      <p class="error-page__code" aria-hidden="true">404</p>
      <h1>Page not found</h1>
      <p>The page you requested is not here-it may have moved or the link may be outdated.</p>
      <a class="btn btn--primary" href="index.html">Return home</a>
    </div>"""

if __name__ == "__main__":
    write_page(
        "blog.html",
        "Blog - Shreyank Nanjappa",
        "Practical notes on sync sound, post workflows, and film sound craft.",
        blog_body(),
        schema='  <script type="application/ld+json">{"@context":"https://schema.org","@type":"Blog","name":"Shreyank Nanjappa Blog","url":"https://www.shreyank.com/blog.html"}</script>',
        nav_lines=blog_nav("blog.html", prefix=""),
        logo_href="index.html",
    )
    write_page(
        "404.html",
        "Page Not Found - Shreyank Nanjappa",
        "The page you requested could not be found.",
        ERROR_BODY,
        nav_lines=home_nav(),
    )
    print("done blog + 404")
