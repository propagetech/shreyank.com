# Shreyank.com Redesign — Strategy & Documentation

## A. Executive Summary

This redesign transforms a single-page, builder-generated portfolio into a **premium, cinematic, multi-page static site** for Shreyank Nanjappa—a Bengaluru-based production sound mixer and sound designer. The new site communicates craft and technical credibility to filmmakers, producers, and post teams without hype or template aesthetics.

**Delivered:** Multi-page portfolio, 3 redesigned blog articles at preserved `/blog/` URLs, article template + `article.css`, BlogPosting schema, category-filtered notes index, and redirects from legacy `old/blog-*.html` paths.

---

## B. Redesign Strategy

| Problem (current site) | Solution |
|------------------------|----------|
| Single long page, poor scanability | Multi-page IA with dedicated Work, Services, Gear, Resources |
| Weak visual hierarchy | Editorial typography, restrained sonic texture, card/list patterns |
| Contact buried in hero | Dedicated Contact page with form + clear CTAs |
| No theme/accessibility story | System-aware light/dark toggle, WCAG-minded contrast |
| Credibility hard to parse | Featured credits + filterable filmography with careful award wording |

**Positioning line:** Sound built for presence, texture, and control.

**Accuracy rule:** Credit *The Elephant Whisperers* as Academy Award–winning film; Shreyank as production sound mixer on that project—not as an “Oscar-winning individual.”

---

## C. Audience + User Journeys

### Audiences
1. **Film directors** — judge sensibility + set experience  
2. **Producers / production houses** — verify credits, availability, scope  
3. **Post supervisors / editors** — assess editorial quality, deliverables  
4. **Collaborators** (boom ops, designers) — understand kit and workflow  
5. **Students** — discover resources and notes  

### Key journeys
| Goal | Path |
|------|------|
| “Is he right for my film?” | Home → Work → Contact |
| “Can he shoot sync in Mumbai?” | Services → Gear → Contact |
| “What has he done?” | Work (filters) → IMDb links |
| “Learn from his writing” | Notes → legacy articles |
| “Hire for documentary” | Home credibility → Work (documentary filter) → Contact |

---

## D. Sitemap + IA

```
/ (index.html)
├── projects.html      [Work — primary]
├── services.html
├── gear.html
├── resources.html
├── about.html
├── contact.html
├── blog.html          [Notes index]
├── blog/              [Article pages — canonical URLs preserved]
│   ├── sync-sound-requirements.html
│   ├── checking-audio-mxf-after-the-dcp-is-made.html
│   └── shoortcuts.html
├── content/blog/      [Article body fragments]
├── 404.html
├── old/               [legacy site; blog HTML redirects to /blog/]
├── assets/
│   ├── css/
│   ├── js/
│   └── icons/
├── robots.txt
├── sitemap.xml
└── site.webmanifest
```

---

## E. Content Architecture

- **Home:** Hero, credibility, selected work, expertise, services preview, approach, gear/notes preview, CTA  
- **Work:** Filterable full filmography from verified legacy content  
- **Services:** 9 service blocks with includes / when / approach  
- **Gear:** Categorized kit lists from existing site  
- **Resources:** Books, podcasts, sites, blogs from existing site  
- **About:** Bio, FTII, Elephant Whisperers credit, philosophy, availability  
- **Contact:** Phones, email, mailto form, enquiry types  
- **Notes:** Index with category filters; 3 full articles at original `/blog/*.html` URLs  

---

## F. Visual & Theme Direction

- **Fonts:** Cormorant Garamond (display) + Source Sans 3 (body) via Google Fonts  
- **Light:** Warm paper `#f4f1ec`, charcoal text, copper accent `#8b4519`  
- **Dark:** Studio charcoal `#121110`, warm gray text, muted gold accent `#c4a574`  
- **Motifs:** Subtle waveform SVG texture in hero only; no neon/glass/gradient clichés  
- **Layout:** Max-width containers, editorial spacing scale, list-based project rows  

---

## G. Page-by-Page Content

See live HTML files. All copy derived from shreyank.com legacy content, restructured and toned down—no invented credits.

---

## H. Folder Structure

```
/
├── index.html, projects.html, services.html, gear.html,
│   resources.html, about.html, contact.html, blog.html, 404.html
├── assets/css/style.css, components.css, responsive.css
├── assets/js/theme-init.js, theme-toggle.js, navigation.js,
│   filters.js, contact-form.js, main.js
├── assets/icons/favicon.svg
├── scripts/build-pages.py, project-rows.html  [maintainability]
├── old/                    [legacy site + blog]
├── STRATEGY.md
├── robots.txt, sitemap.xml, site.webmanifest, .nojekyll
└── .github/workflows/deploy.yml
```

---

## I. HTML/CSS/JS Build Plan

1. **theme-init.js** in `<head>` — prevents FOUC  
2. **CSS custom properties** on `html[data-theme="light|dark"]`  
3. **Shared header/footer** — generated via `scripts/build-pages.py` for consistency  
4. **Defer** all scripts except theme-init  
5. **No frameworks** — per assignment requirements  

---

## K. SEO + Schema

- Unique `<title>` and meta description per page  
- Canonical + Open Graph on all pages  
- JSON-LD: Person + WebSite (home), CollectionPage (work), AboutPage, ContactPage, Blog  
- `sitemap.xml` + `robots.txt`  
- Internal linking: footer nav + in-content CTAs  

---

## L. Accessibility Checklist

- [x] Skip link  
- [x] Landmarks: header, nav, main, footer  
- [x] One h1 per page  
- [x] Focus visible styles  
- [x] Theme toggle keyboard + aria-label  
- [x] Mobile menu aria-expanded, Escape to close  
- [x] Form labels + required fields  
- [x] `prefers-reduced-motion` respected  
- [x] Touch targets ≥ 44px on buttons  
- [x] `aria-live` on project filter status  
- [ ] Manual screen reader pass recommended before launch  

---

## M. Performance Checklist

- [x] No CSS/JS frameworks  
- [x] Minimal JS (<5 small files)  
- [x] SVG favicon  
- [x] Font preconnect + `display=swap`  
- [x] No hero background images (text-first LCP)  
- [ ] Run Lighthouse on deployed URL  
- [ ] Compress if large images added later  

---

## N. Future Improvements

1. Migrate blog posts into `/notes/` with shared article template  
2. Add `project-detail.html` template for case-study depth  
3. Press/recognition page if new verified awards  
4. WebP hero stills (optional, lazy-loaded)  
5. Hindi/Kannada metadata if regional SEO matters  
6. Form backend (Formspree/Netlify) if mailto insufficient  

---

## O. Interview Talking Points

1. **Why multi-page?** Film professionals scan credits quickly; one page hid the filmography.  
2. **Why this visual language?** Title-card editorial tone matches sound craft—quiet confidence.  
3. **Theme system** — respects system preference, persists choice, no flash, CSS variables only.  
4. **Accuracy** — Oscar language tied to *The Elephant Whisperers*, not personal award claims.  
5. **Maintainability** — Python generator for shared chrome; project rows in one file.  
6. **Trade-offs** — Blog stays in `/old/` short-term to ship; gateway preserves SEO paths.  
7. **What I'd do next** — Lighthouse on production, case studies for 2–3 flagship films, structured `VideoObject` if reels added.
