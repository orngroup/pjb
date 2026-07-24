# PJB Partnership — Website

Multi-page static website for **PJB Partnership** ("Built on Trust").
No build tools, databases or frameworks required — plain HTML, CSS and a small
JavaScript file. Anyone comfortable editing text files can maintain it.

## Hosting on GitHub Pages

1. Create a new GitHub repository (e.g. `pjb-partnership-site`).
2. Upload the entire contents of this folder to the repository root.
3. In the repository, go to **Settings → Pages**.
4. Under *Build and deployment*, set **Source: Deploy from a branch**,
   choose branch **main** and folder **/ (root)**, then save.
5. The site will be live within a minute or two at
   `https://<your-username>.github.io/pjb-partnership-site/`.
6. To use the `pjbpartnership.co.uk` domain later, add it under
   **Settings → Pages → Custom domain** and point the domain's DNS
   (CNAME record) at `<your-username>.github.io`.

The `.nojekyll` file tells GitHub Pages to serve the files exactly as-is.

## How the site is structured

| Path | What it is |
|---|---|
| `index.html` | Home page |
| `about.html`, `why-pjb.html`, `clients.html`, `awaabs-law.html`, `technology.html`, `certifications.html` | About section |
| `services.html` + `service-*.html` | Services hub + 7 service pages |
| `sectors.html` + `sector-*.html` | Sectors hub + 5 sector pages |
| `careers.html` + `career-*.html` | Careers hub + 7 role pages |
| `contact.html` | Contact details + enquiry form |
| `privacy-policy.html`, `cookie-policy.html`, `terms.html` | Legal pages (templates — have them reviewed before launch) |
| `css/style.css` | All styling. Brand colours are defined once at the top as CSS variables. |
| `js/site.js` | **The header and footer for every page live here.** Edit navigation, phone, email or address in this one file and every page updates. |
| `assets/` | Logo, favicon |
| `build.py` | Optional. The Python script originally used to generate the pages. You can ignore it and edit the HTML files directly, or edit `build.py` and re-run `python3 build.py` to regenerate everything consistently. |

## Common edits

- **Change a phone number, email or the address** → edit the `PJB` object at
  the top of `js/site.js` (footer + contact page card in `contact.html`).
- **Add or remove a menu item** → edit the `NAV` array in `js/site.js`.
- **Change brand colours** → edit the `:root` variables at the top of
  `css/style.css` (they are sampled from the logo: navy `#0B1B3A`,
  blue `#1E6FD9`, sky `#4FA3FF`).
- **Edit page text** → open the relevant `.html` file; the content is plain
  HTML inside `<main>`.
- **Add photos** → drop images into `assets/` and replace any
  `<div class="feature-media">` panel with
  `<img src="assets/your-photo.jpg" alt="Description" style="border-radius:10px">`.

## Contact form

The form on `contact.html` currently opens the visitor's email client
(`mailto:`). For a proper hosted form on a static site, sign up with a free
form service such as Formspree, then change the form tag to:

```html
<form class="contact-form" action="https://formspree.io/f/YOUR-ID" method="POST">
```

## Notes for launch

- The legal pages are marked as templates — have them reviewed and completed
  by a legal adviser before going live.
- Client names, statistics and testimonials were carried over from the
  previous Cato Services site content as requested — confirm these remain
  accurate for the PJB Partnership brand before launch.
