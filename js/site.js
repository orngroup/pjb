/* ============================================================
   PJB PARTNERSHIP — shared layout
   The header and footer for every page live here, in ONE place.
   To change navigation, contact details or footer links,
   edit this file only — all pages update automatically.
   ============================================================ */

const PJB = {
  name: "PJB Partnership",
  tagline: "Built on Trust",
  phone: "01908 034578",
  phoneHref: "tel:+441908034578",
  email: "hello@pjbpartnership.co.uk",
  address: ["8 Shenley Pavilions", "Shenley Wood", "Milton Keynes, MK5 6LB"]
};

const NAV = [
  {
    label: "About Us", href: "about.html", key: "about",
    children: [
      { label: "Why PJB", href: "why-pjb.html" },
      { label: "Clients", href: "clients.html" },
      { label: "Awaab\u2019s Law Compliance", href: "awaabs-law.html" },
      { label: "Technology & Innovation", href: "technology.html" },
      { label: "Certifications", href: "certifications.html" }
    ]
  },
  {
    label: "Services", href: "services.html", key: "services",
    children: [
      { label: "Planned & Reactive Maintenance", href: "service-planned-reactive-maintenance.html" },
      { label: "Compliance & Awaab\u2019s Law", href: "service-compliance-awaabs-law.html" },
      { label: "Mechanical & Electrical Services", href: "service-mechanical-electrical.html" },
      { label: "Fire Safety Compliance", href: "service-fire-safety.html" },
      { label: "Cleaning & Grounds Maintenance", href: "service-cleaning-grounds.html" },
      { label: "Sustainability & Retrofitting", href: "service-sustainability-retrofitting.html" },
      { label: "Gas Services", href: "service-gas.html" }
    ]
  },
  {
    label: "Sectors We Serve", href: "sectors.html", key: "sectors",
    children: [
      { label: "Social Housing", href: "sector-social-housing.html" },
      { label: "Public Sector & Local Authorities", href: "sector-public-sector.html" },
      { label: "Hospitality & Leisure", href: "sector-hospitality-leisure.html" },
      { label: "Commercial Properties", href: "sector-commercial.html" },
      { label: "Healthcare & Education", href: "sector-healthcare-education.html" }
    ]
  },
  {
    label: "Careers", href: "careers.html", key: "careers",
    children: [
      { label: "Gas Safe Engineers", href: "career-gas-safe-engineers.html" },
      { label: "Project Managers & Compliance Officers", href: "career-project-managers.html" },
      { label: "Electricians (NICEIC)", href: "career-electricians.html" },
      { label: "Damp & Mould Remediation Teams", href: "career-damp-mould.html" },
      { label: "Fire Safety Specialists", href: "career-fire-safety.html" },
      { label: "Cleaning & Grounds Maintenance Staff", href: "career-cleaning-grounds.html" },
      { label: "Facilities Management Operatives", href: "career-fm-operatives.html" }
    ]
  }
];

function buildNav(activeKey) {
  return NAV.map(item => {
    const active = item.key === activeKey ? " class=\"active\"" : "";
    const children = item.children
      ? "<ul class=\"dropdown\">" +
        item.children.map(c => `<li><a href="${c.href}">${c.label}</a></li>`).join("") +
        "</ul>"
      : "";
    return `<li${active}><a href="${item.href}">${item.label}</a>${children}</li>`;
  }).join("");
}

function renderHeader() {
  const activeKey = document.body.dataset.nav || "";
  const el = document.getElementById("site-header");
  if (!el) return;
  el.innerHTML = `
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap nav-bar">
      <a class="brand" href="index.html" aria-label="${PJB.name} — home">
        <img src="assets/logo.png" alt="${PJB.name} — Built on Trust">
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu">Menu</button>
      <nav id="nav-menu" class="nav-menu" aria-label="Main navigation">
        <ul class="nav-list">
          ${buildNav(activeKey)}
          <li><a class="btn btn-primary nav-cta" href="contact.html">Contact Us</a></li>
        </ul>
      </nav>
    </div>
  </header>`;

  const toggle = el.querySelector(".nav-toggle");
  const menu = el.querySelector("#nav-menu");
  toggle.addEventListener("click", () => {
    const open = menu.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });
}

function renderFooter() {
  const el = document.getElementById("site-footer");
  if (!el) return;
  const year = new Date().getFullYear();
  el.innerHTML = `
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          <strong>${PJB.name}</strong>
          <em>${PJB.tagline}</em>
          <p>Full-service facilities management delivering safe, compliant and sustainable environments for housing, public sector, commercial and hospitality clients across the UK.</p>
        </div>
        <div>
          <h4>Company</h4>
          <ul>
            <li><a href="about.html">About Us</a></li>
            <li><a href="why-pjb.html">Why PJB</a></li>
            <li><a href="clients.html">Our Clients</a></li>
            <li><a href="certifications.html">Certifications</a></li>
            <li><a href="careers.html">Careers</a></li>
          </ul>
        </div>
        <div>
          <h4>Services</h4>
          <ul>
            <li><a href="service-planned-reactive-maintenance.html">Planned &amp; Reactive Maintenance</a></li>
            <li><a href="service-compliance-awaabs-law.html">Compliance &amp; Awaab\u2019s Law</a></li>
            <li><a href="service-mechanical-electrical.html">Mechanical &amp; Electrical</a></li>
            <li><a href="service-fire-safety.html">Fire Safety Compliance</a></li>
            <li><a href="service-sustainability-retrofitting.html">Sustainability &amp; Retrofitting</a></li>
          </ul>
        </div>
        <div>
          <h4>Head Office</h4>
          <p>${PJB.name}<br>${PJB.address.join("<br>")}</p>
          <ul>
            <li><a href="${PJB.phoneHref}">${PJB.phone}</a></li>
            <li><a href="mailto:${PJB.email}">${PJB.email}</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; ${year} ${PJB.name}. All rights reserved.</span>
        <ul>
          <li><a href="privacy-policy.html">Privacy Policy</a></li>
          <li><a href="cookie-policy.html">Cookie Policy</a></li>
          <li><a href="terms.html">Terms &amp; Conditions</a></li>
        </ul>
      </div>
    </div>
  </footer>`;
}

document.addEventListener("DOMContentLoaded", () => {
  renderHeader();
  renderFooter();
});
