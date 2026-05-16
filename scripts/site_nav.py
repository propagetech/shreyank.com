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


WHATSAPP_NUMBER = "919900117364"
WHATSAPP_DISPLAY = "+91 9900 117 364"


def layout_width_control():
    return """  <motion class="layout-width" data-layout-width hidden>
    <label class="sr-only" for="layout-width-range">Content width</label>
    <svg class="layout-width__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
      <path d="M4 8h16M4 16h16M8 4v16M16 4v16"/>
    </svg>
    <input type="range" id="layout-width-range" class="layout-width__range" data-layout-width-range min="48" max="88" step="2" value="68" aria-valuemin="48" aria-valuemax="88" aria-valuenow="68" aria-valuetext="68 rem content width">
    <button type="button" class="layout-width__reset" data-layout-width-reset title="Reset content width">Reset</button>
  </motion>""".replace("<motion ", "<motion ").replace("motion", "div")


def whatsapp_float():
    return (
        layout_width_control()
        + f"""
  <a class="whatsapp-float" href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp - {WHATSAPP_DISPLAY}">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
    </svg>
  </a>"""
    )
