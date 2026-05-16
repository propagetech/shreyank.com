"""Shared navigation markup for single-page + blog."""

HOME_NAV_LINKS = [
    ("#projects", "Projects"),
    ("#sound-recording", "Sound Recording"),
    ("#sound-design", "Sound Design"),
    ("#resources", "Resources"),
    ("#contact", "Contact"),
    ("blog.html", "Blog"),
]

BLOG_NAV_PREFIX = "../"


def _blog_href(href, prefix="../"):
    if href.startswith("#"):
        base = f"{prefix}index.html{href}" if prefix else f"index.html{href}"
        return base
    return f"{prefix}{href}" if prefix else href


def home_nav(current=None):
    lines = []
    for href, label in HOME_NAV_LINKS:
        cur = ""
        if current and (
            (current == href)
            or (current == "blog.html" and href == "blog.html")
        ):
            cur = ' aria-current="page"'
        lines.append(f'          <li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(lines)


def blog_nav(current="blog.html", prefix="../"):
    lines = []
    for href, label in HOME_NAV_LINKS:
        full = _blog_href(href, prefix)
        cur = ' aria-current="page"' if label == "Blog" and current == "blog.html" else ""
        if current and href == f"blog/{current}":
            cur = ' aria-current="page"'
        lines.append(f'          <li><a href="{full}"{cur}>{label}</a></li>')
    return "\n".join(lines)


def home_footer_nav():
    return home_nav()


def blog_footer_nav(prefix="../"):
    lines = []
    for href, label in HOME_NAV_LINKS:
        lines.append(f'          <li><a href="{_blog_href(href, prefix)}">{label}</a></li>')
    return "\n".join(lines)
