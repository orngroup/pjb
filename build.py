#!/usr/bin/env python3
"""Generates all HTML pages for the PJB Partnership site.
Run:  python3 build.py   (from the site root)
Each page shares the same shell; header/footer come from js/site.js.
"""
import html, pathlib

ROOT = pathlib.Path(__file__).parent

def shell(*, file, title, desc, nav, body):
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | PJB Partnership</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body data-nav="{nav}">
<div id="site-header"></div>
<main id="main">
{body}
</main>
<div id="site-footer"></div>
<script src="js/site.js"></script>
</body>
</html>
"""

# ---------------------------------------------------------------
# Re-usable blocks
# ---------------------------------------------------------------

def page_hero(eyebrow, title, intro="", backlink=None):
    back = f'<a class="backlink" href="{backlink[1]}">&larr; {backlink[0]}</a>' if backlink else ""
    intro_html = f"<p>{intro}</p>" if intro else ""
    return f"""
<section class="page-hero">
  <div class="wrap">
    {back}
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    {intro_html}
  </div>
</section>"""

def cta(heading="Need a trusted facilities management partner?",
        text="Get in touch today to discuss how PJB Partnership can support your housing, commercial or hospitality needs.",
        button="Contact Us", href="contact.html"):
    return f"""
<section class="cta-band">
  <div class="wrap">
    <span class="eyebrow">{text}</span>
    <h2>{heading}</h2>
    <a class="btn btn-light" href="{href}">{button}</a>
  </div>
</section>"""

def stats():
    return """
<section class="stats">
  <div class="wrap grid-4">
    <div class="stat"><b>30,000</b><span>Homes serviced</span></div>
    <div class="stat"><b>UK</b><span>Nationwide coverage</span></div>
    <div class="stat"><b>24/7</b><span>Responsive support</span></div>
    <div class="stat"><b>100%</b><span>Compliance delivery</span></div>
  </div>
</section>"""

def card(title, text, href=None):
    link = f'<a class="cover more" href="{href}">Learn more &rarr;</a>' if href else ""
    return f'<div class="card"><h3>{title}</h3><p>{text}</p>{link}</div>'

def defrow(title, body):
    return f'<div class="def"><h3>{title}</h3><div>{body}</div></div>'

# ---------------------------------------------------------------
PAGES = []

# ============================ HOME ============================
home_services = "".join([
    card("Planned &amp; Reactive Maintenance", "Keeping assets safe and reliable.", "service-planned-reactive-maintenance.html"),
    card("Compliance &amp; Awaab&rsquo;s Law", "Statutory testing and damp &amp; mould remediation.", "service-compliance-awaabs-law.html"),
    card("Mechanical &amp; Electrical", "Accredited NICEIC and Gas Safe engineers.", "service-mechanical-electrical.html"),
    card("Fire Safety Compliance", "Fire doors, alarms, extinguishers and passive protection.", "service-fire-safety.html"),
    card("Cleaning &amp; Grounds Maintenance", "Professional, flexible and efficient.", "service-cleaning-grounds.html"),
    card("Sustainability &amp; Retrofitting", "Energy efficiency and carbon reduction solutions.", "service-sustainability-retrofitting.html"),
])

home_whatwedo = "".join([
    defrow("Facilities &amp; General Maintenance", "Planned and responsive maintenance services that keep buildings safe, compliant and fully operational."),
    defrow("Survey Reports", "Specialist damp &amp; mould surveys and property condition reports, giving landlords and clients clear insights to act on."),
    defrow("External Works", "High-quality brickwork, fencing and external improvements that protect and enhance property value."),
    defrow("Heating, Plumbing &amp; Electrical", "Certified engineers providing reliable repairs, installations and compliance testing."),
    defrow("Roofing", "Expertise in both pitched and flat roofing solutions, keeping properties watertight and secure."),
])

home_why = "".join([
    defrow("What We Do", "PJB Partnership is a full-service facilities management company dedicated to delivering safe, compliant and sustainable solutions across multiple sectors. Guided by our values &mdash; Community, Accountability, Trust and Operations &mdash; we operate with professionalism and integrity, ensuring that clients across housing, local authorities, commercial properties and hospitality environments receive services they can depend on."),
    defrow("Our Approach", "<ul class='ticks'><li><b>Strategic support</b> &mdash; more than daily maintenance; we provide compliance monitoring and innovative service delivery.</li><li><b>Transparency</b> &mdash; accountability drives complete contract clarity.</li><li><b>Community focus</b> &mdash; working with housing providers and businesses to enhance environments.</li><li><b>Trust</b> &mdash; long-term relationships built on reliability.</li><li><b>Efficient operations</b> &mdash; controlled costs and consistent outcomes.</li></ul>"),
    defrow("We Specialise In", "<ul class='ticks'><li>Facilities management (hard and soft FM) &mdash; complete solutions for properties and assets.</li><li>Planned and reactive maintenance &mdash; ensuring buildings operate smoothly and safely.</li><li>Mechanical &amp; electrical services &mdash; delivered by accredited experts.</li><li>Fire safety compliance &mdash; fire doors, alarms, extinguishers and passive systems.</li><li>Damp and mould remediation &mdash; fully aligned with Awaab&rsquo;s Law.</li><li>Building refurbishments &mdash; including kitchens, bathrooms, roofing and fabric upgrades.</li><li>Cleaning and waste management &mdash; reliable, professional and sustainable.</li><li>Grounds maintenance &mdash; keeping outdoor spaces safe and well maintained.</li><li>Sustainability upgrades &mdash; energy efficiency retrofitting, carbon reduction and green procurement.</li></ul>"),
    defrow("Trusted By Leading Organisations", "PJB Partnership is trusted by leading organisations such as Riverside, One Housing and The Home Group. These partnerships reflect our ability to serve diverse needs while always maintaining compliance, quality and client satisfaction."),
    defrow("Our Mission", "Our mission is to ensure every building we manage is safe, compliant and future-ready. Whether supporting social housing providers in meeting new regulatory standards, assisting councils with large-scale property portfolios, or delivering tailored solutions for hospitality environments, PJB Partnership brings professionalism and reliability to every contract."),
    defrow("Our Values In Action", "At the core of our identity, our values of Community, Accountability, Trust and Operations are not just words &mdash; they are the principles that define how we work. They ensure that our services deliver safer homes, stronger communities and sustainable outcomes for clients and tenants alike."),
])

clients_rows = "".join([
    f'<div class="client"><h3>{n}</h3><p>{t}</p></div>' for n, t in [
        ("Riverside Group", "We work with Riverside Group to deliver compliance, refurbishment and repairs. Our services support safe homes, protect assets and improve tenant wellbeing."),
        ("The Home Group", "Home Group is one of the UK&rsquo;s largest housing associations. We support them with compliance, planned maintenance and repairs, helping deliver safe and sustainable homes for residents."),
        ("One Housing", "We work with One Housing to provide facilities management tailored to residents&rsquo; needs. From minor repairs to major works, we ensure properties remain safe, compliant and welcoming."),
    ]
])

PAGES.append(dict(file="index.html", title="Facilities Management Built on Trust", nav="home",
    desc="PJB Partnership is a trusted facilities management company delivering maintenance, surveys, gas, electrical and roofing services across the UK.",
    body=f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">PJB Partnership &mdash; Built on Trust</span>
      <h1>Full-service facilities management, built on trust</h1>
      <p class="lead">Delivering safe, compliant and sustainable environments for housing, public sector, commercial and hospitality clients across the UK.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="services.html">View Services</a>
        <a class="btn btn-ghost" href="contact.html">Contact Us</a>
      </div>
    </div>
    <div class="roof-panel" role="img" aria-label="PJB Partnership brand panel">
      <div class="roof-quote">Community &bull; Accountability &bull; Trust &bull; Operations
        <small>The values behind every job we deliver</small>
      </div>
    </div>
  </div>
</section>

{stats()}

<section class="section">
  <div class="wrap feature">
    <div>
      <span class="eyebrow">About Our Company</span>
      <h2>PJB Partnership is more than a facilities management company. We are a partner defined by values.</h2>
      <p style="margin-top:16px">Our work is guided by four values &mdash; Community, Accountability, Trust and Operations &mdash; and trust is quite literally built into our name. From damp and mould remediation to large-scale building management, we ensure safety, compliance and sustainability for every client.</p>
      <p style="margin-top:22px"><a class="btn btn-ghost" href="about.html">Read More</a></p>
    </div>
    <div class="feature-media" aria-hidden="true"></div>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Our Services</span>
      <h2>We offer a range of services to meet all types of needs</h2>
    </div>
    <div class="grid-3">{home_services}</div>
    <p style="margin-top:34px"><a class="btn btn-primary" href="services.html">All Services</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What We Do</span>
      <h2>Comprehensive facilities management, built for every sector we serve</h2>
      <p>At PJB Partnership, we deliver end-to-end facilities management solutions tailored to housing, hospitality and commercial clients. Our core services include:</p>
    </div>
    {home_whatwedo}
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Why Choose Us</span>
      <h2>Driven by values, focused on results</h2>
    </div>
    {home_why}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Our Clients</span>
      <h2>We believe every client is a valuable long-term partner</h2>
    </div>
    {clients_rows}
    <p style="margin-top:30px"><a class="btn btn-ghost" href="clients.html">Read More</a></p>
  </div>
</section>

{cta()}
"""))

# ============================ ABOUT ============================
about_story = "".join([
    defrow("Our Story", "PJB Partnership is a facilities management company defined by four principles: Community, Accountability, Trust and Operations. These values are the foundation of our approach, shaping every project we deliver and every partnership we maintain.<br><br>Our story begins with a recognition that housing providers, councils and businesses need more than contractors &mdash; they need reliable partners. We built PJB Partnership to meet this need, creating a company that combines technical expertise with a deep understanding of community impact.<br><br>By embedding compliance, professionalism and transparency into everything we do, we have become a trusted partner across multiple sectors."),
    defrow("Our Partnerships", "We work with major organisations such as Riverside, One Housing and The Home Group, delivering services that range from everyday maintenance to complex compliance-led programmes. Each partnership reflects our commitment to consistency, value for money and long-term results."),
    defrow("Our Values", "<ul class='ticks'><li><b>Community</b> means improving the lives of tenants and service users, ensuring that the environments we maintain are safe, welcoming and sustainable.</li><li><b>Accountability</b> means complete transparency in our delivery, with clear reporting and open communication that allow clients to monitor progress and outcomes.</li><li><b>Trust</b> means reliability. Our clients know we will deliver what we promise, on time and to the highest standard.</li><li><b>Operations</b> means effective, professional and compliant delivery, with a focus on efficiency and innovation.</li></ul>"),
    defrow("Our Accreditations", "We are proud of our accreditations, including Gas Safe, NICEIC, CHAS, Constructionline Gold, ISO&nbsp;9001, ISO&nbsp;14001 and ISO&nbsp;45001. These certifications demonstrate our ongoing commitment to quality, safety and environmental responsibility."),
    defrow("Our Impact", "At PJB Partnership, we do more than manage buildings. We deliver safer homes, stronger communities and lasting value. Our approach combines technical expertise with a people-first ethos, ensuring that every project we deliver contributes positively to both our clients and the communities they serve."),
])

PAGES.append(dict(file="about.html", title="About Us", nav="about",
    desc="Discover PJB Partnership — a UK facilities management company built on community, accountability, trust and operational excellence.",
    body=f"""
{page_hero("About Us", "We deliver safe and compliant works",
  "PJB Partnership was founded with a clear mission: to deliver safe, compliant and professional facilities management that strengthens communities. Four values guide every service we provide &mdash; Community, Accountability, Trust and Operations &mdash; and we work across housing, local authorities, commercial properties and hospitality, ensuring every environment is safe, sustainable and future-ready.")}

<section class="section">
  <div class="wrap grid-3">
    {card("Our Services", "We provide a complete range of facilities management services tailored to client needs: planned and reactive maintenance, compliance and Awaab&rsquo;s Law remediation, mechanical and electrical services, fire safety compliance, cleaning, waste and grounds maintenance, and sustainability and retrofitting.", "services.html")}
    {card("Experience", "With decades of combined industry experience, our team has delivered over 350 projects across the UK. We are proud to be trusted by leading organisations including Riverside, One Housing and The Home Group &mdash; from day-to-day maintenance through to major compliance-led programmes.")}
    {card("Accountability", "Accountability is more than a value &mdash; it is our operating model. We provide clear reporting, compliance monitoring and open communication throughout every project. Every outcome is evidence-based, transparent and aligned with statutory obligations. When we take responsibility, we own it completely.")}
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Built on Trust</span>
      <h2>Delivering lasting value</h2>
    </div>
    {about_story}
  </div>
</section>

<section class="section">
  <div class="wrap feature">
    <div>
      <span class="eyebrow">Our Mission</span>
      <h2>Safer homes, stronger communities</h2>
      <p style="margin-top:16px">Our mission is to deliver safer homes and stronger communities by combining technical excellence with social value. We strive to set new standards in facilities management through innovation, compliance and sustainability.</p>
      <p style="margin-top:14px">Every contract we undertake is an opportunity to improve safety, protect communities and deliver lasting value for both clients and tenants.</p>
    </div>
    <div class="feature-media" aria-hidden="true"></div>
  </div>
</section>

{cta("Looking for a facilities management partner you can trust?",
     "Whether you need compliance-driven maintenance, sustainable building upgrades or complete FM support, PJB Partnership is here to help.")}
"""))

# ============================ WHY PJB ============================
testimonials = "".join([
    f'<div class="quote-card"><p>{q}</p><footer>{n}<small>{r}</small></footer></div>' for q, n, r in [
        ("Jay is a real credit to both himself and your company. Not only skilled and professional, but he was kind, patient and respectful throughout &ndash; it made me feel completely at ease.", "Dionne Brown", "Resident"),
        ("Zoe has been singing Roxanne&rsquo;s praises and the partnership is going from strength to strength. Honestly could not be happier with the delivery and teamwork.", "Natalie Magri", "Head of Voids, Minor &amp; Major Works, Property Services"),
        ("Extremely pleased with the works, operatives cleaned everything up neatly &ndash; it was one of the best services I have had.", "Ms Annette Holmes", "Resident"),
        ("Delighted with Simon from PJB &ndash; outstanding work on the extractor fan.", "Miss Robyn Ann Thackara", "Resident"),
        ("The decorator was very professional and tidy. The customer complimented his work highly.", "Dan Willis", "Riverside Property Services"),
        ("Eddie did an amazing job &ndash; very professional, tidy and friendly. The matter was resolved promptly and I&rsquo;m hugely grateful.", "Sonia", "Resident"),
        ("Aaron particularly has gone above and beyond to make sure that everything in my property was done to a high standard. It&rsquo;s changed my life and given me confidence and hope for the future.", "Georgia Amodu", "Resident"),
        ("She was extremely happy with the works to the bathroom the second time around and has now signed off the claim with me &ndash; thank you for that.", "Zoe Thomas", "Project Surveyor, Riverside"),
    ]
])

why_rows = "".join([
    defrow("Community", "We create safer, cleaner and more sustainable environments. Our work directly supports tenants and communities, ensuring housing providers and councils can demonstrate positive impact."),
    defrow("Accountability", "We operate with transparency, providing full reporting, compliance data and audit trails. Clients can monitor progress in real time and rest assured that all legal requirements are met."),
    defrow("Trust", "Our reputation is built on reliability. From large-scale housing associations to private hotel groups, our clients know they can depend on us to deliver what we promise, on time and within budget."),
    defrow("Operations", "We combine human expertise with digital technology to deliver services efficiently and professionally. From reactive maintenance to planned compliance programmes, our operations are streamlined and consistent."),
    defrow("Committed to Quality", "By choosing PJB Partnership, clients benefit from a partner that is compliance-led, technology-driven and community-focused. Our accreditations &mdash; including ISO, Gas Safe, NICEIC, CHAS and Constructionline Gold &mdash; further reinforce our credibility and commitment to excellence."),
])

PAGES.append(dict(file="why-pjb.html", title="Why PJB", nav="about",
    desc="Why choose PJB Partnership: a facilities management partner defined by community, accountability, trust and operations.",
    body=f"""
{page_hero("Why PJB", "A partner defined by values: community, accountability, trust and operations",
  "Choosing the right facilities management partner is about more than price. It&rsquo;s about trust, compliance and reliability. At PJB Partnership, four values guide everything we do &mdash; Community, Accountability, Trust and Operations &mdash; ensuring we deliver safe, compliant and sustainable solutions for every client.",
  backlink=("About Us", "about.html"))}

{stats()}

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Our Values</span>
      <h2>Guided by principles that define how we work</h2>
    </div>
    <div class="grid-4">
      {card("Community", "We improve the environments where people live and work, delivering services that strengthen communities and protect tenants.")}
      {card("Accountability", "We provide complete transparency, evidence-based reporting and full compliance monitoring across every project.")}
      {card("Trust", "Long-term partnerships are built on reliability. Our clients know that when we commit, we deliver.")}
      {card("Operations", "Efficient, compliant and professional service delivery &mdash; ensuring safety, sustainability and value for money.")}
    </div>
    <p style="margin-top:34px"><a class="btn btn-primary" href="services.html">View Services</a></p>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Testimonials</span>
      <h2>Trusted by clients, valued by residents</h2>
      <p>We build our reputation on trusted people and strong partnerships, delivering safe, compliant services that improve residents&rsquo; lives.</p>
    </div>
    <div class="grid-2">{testimonials}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Why Choose Us</span>
      <h2>Why clients choose PJB Partnership</h2>
    </div>
    {why_rows}
  </div>
</section>

{cta()}
"""))

# ============================ CLIENTS ============================
PAGES.append(dict(file="clients.html", title="Our Clients", nav="about",
    desc="PJB Partnership is trusted by leading organisations including Riverside, One Housing and The Home Group.",
    body=f"""
{page_hero("Our Clients", "We believe every client is a valuable long-term partner",
  "PJB Partnership is trusted by leading organisations across housing, public sector, commercial and hospitality. These partnerships reflect our ability to serve diverse needs while always maintaining compliance, quality and client satisfaction.",
  backlink=("About Us", "about.html"))}

<section class="section">
  <div class="wrap">
    {clients_rows}
  </div>
</section>

{stats()}
{cta()}
"""))

# ============================ AWAAB'S LAW ============================
PAGES.append(dict(file="awaabs-law.html", title="Awaab's Law Compliance", nav="about",
    desc="PJB Partnership supports housing providers in meeting Awaab's Law requirements, delivering damp and mould remediation within statutory deadlines.",
    body=f"""
{page_hero("Awaab&rsquo;s Law Compliance", "Meeting statutory deadlines. Protecting tenants.",
  "Awaab&rsquo;s Law sets strict legal requirements for social landlords to investigate and remediate damp, mould and other hazards within defined timescales. PJB Partnership supports housing providers in meeting those obligations &mdash; delivering damp and mould remediation within statutory deadlines, backed by clear evidence and reporting.",
  backlink=("About Us", "about.html"))}

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How We Help</span>
      <h2>Compliance is central to our service delivery</h2>
    </div>
    {defrow("Specialist Surveys", "Specialist damp &amp; mould surveys and property condition reports, giving landlords and clients clear insights to act on.")}
    {defrow("Rapid Remediation", "Our remediation teams diagnose issues, apply treatments and restore properties to safe living conditions &mdash; ensuring fast response within the timescales the law requires.")}
    {defrow("Statutory Testing &amp; Inspections", "We carry out statutory testing and inspections across gas, electrical and fire safety systems, keeping every property compliant.")}
    {defrow("Evidence &amp; Reporting", "Every job is supported by transparent reporting, compliance data and audit trails, so providers can demonstrate that legal requirements have been met.")}
  </div>
</section>

<section class="section tint">
  <div class="wrap feature">
    <div>
      <span class="eyebrow">Why It Matters</span>
      <h2>Safer homes, stronger communities</h2>
      <p style="margin-top:16px">Our expertise in damp and mould remediation, aligned with Awaab&rsquo;s Law, positions us as a reliable partner in helping providers meet strict legal standards. From delivering compliance programmes to planned maintenance and refurbishment, our work improves housing stock and creates better living environments.</p>
      <p style="margin-top:22px"><a class="btn btn-primary" href="service-compliance-awaabs-law.html">Our Compliance Service</a></p>
    </div>
    <div class="feature-media" aria-hidden="true"></div>
  </div>
</section>

{cta("Need support with Awaab&rsquo;s Law compliance?",
     "Talk to us about surveys, remediation and compliance reporting for your housing stock.")}
"""))

# ============================ TECHNOLOGY ============================
PAGES.append(dict(file="technology.html", title="Technology & Innovation", nav="about",
    desc="PJB Partnership combines human expertise with digital technology — real-time reporting, compliance data and audit trails.",
    body=f"""
{page_hero("Technology &amp; Innovation", "Human expertise, digital delivery",
  "We combine skilled people with digital technology to deliver services efficiently and professionally. From reactive maintenance to planned compliance programmes, our operations are streamlined, consistent and fully transparent.",
  backlink=("About Us", "about.html"))}

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Innovation In Practice</span>
      <h2>Technology that keeps clients informed and compliant</h2>
    </div>
    {defrow("Real-Time Visibility", "Clients can monitor progress in real time, with full reporting on works, compliance status and outcomes across every contract.")}
    {defrow("Compliance Data &amp; Audit Trails", "Evidence-based delivery: compliance data and audit trails support every project, aligned with statutory obligations.")}
    {defrow("Streamlined Operations", "Digital job management keeps our reactive and planned works efficient, reducing downtime and keeping costs controlled.")}
    {defrow("Strategic Support", "More than daily maintenance &mdash; we provide compliance monitoring and innovative service delivery that helps clients plan ahead.")}
  </div>
</section>

{stats()}
{cta()}
"""))

# ============================ CERTIFICATIONS ============================
PAGES.append(dict(file="certifications.html", title="Certifications", nav="about",
    desc="PJB Partnership accreditations: Gas Safe, NICEIC, CHAS, Constructionline Gold, ISO 9001, ISO 14001 and ISO 45001.",
    body=f"""
{page_hero("Certifications", "Accredited. Audited. Accountable.",
  "Our accreditations demonstrate an ongoing commitment to quality, safety and environmental responsibility &mdash; and give clients confidence that every job is delivered to recognised standards.",
  backlink=("About Us", "about.html"))}

<section class="section">
  <div class="wrap grid-3">
    {card("Gas Safe", "All gas works are carried out by Gas Safe registered engineers &mdash; the legal requirement for anyone working on gas appliances in the UK.")}
    {card("NICEIC", "Our electrical services are delivered by NICEIC accredited engineers, ensuring safe, certified installations and testing.")}
    {card("CHAS", "CHAS accreditation confirms our health and safety processes meet recognised industry standards.")}
    {card("Constructionline Gold", "Constructionline Gold membership demonstrates enhanced pre-qualification across governance, health and safety, and financial standing.")}
    {card("ISO 9001", "Certified quality management &mdash; consistent processes and continual improvement across all our services.")}
    {card("ISO 14001", "Certified environmental management &mdash; reducing our impact and supporting clients&rsquo; sustainability goals.")}
    {card("ISO 45001", "Certified occupational health and safety management &mdash; a safe working environment for our teams and clients on every project.")}
  </div>
</section>

{cta("Want to see our accreditations in your supply chain?",
     "We are happy to provide certificates and supporting documentation as part of any tender or onboarding process.")}
"""))

# ============================ SERVICES HUB ============================
services_full = "".join([
    defrow("Planned &amp; Reactive Maintenance", "Our responsive maintenance teams ensure issues are addressed quickly, while planned programmes extend asset life, reduce long-term costs and minimise disruption."),
    defrow("Compliance &amp; Awaab&rsquo;s Law", "Compliance is central to our service delivery. We support housing providers in meeting Awaab&rsquo;s Law requirements, delivering damp and mould remediation within statutory deadlines. We also carry out statutory testing and inspections across gas, electrical and fire safety systems."),
    defrow("Mechanical &amp; Electrical Services", "Delivered by qualified Gas Safe and NICEIC engineers, our M&amp;E services include installations, testing and maintenance that meet the highest safety and performance standards."),
    defrow("Fire Safety Compliance", "We install and maintain fire alarms, emergency lighting and passive fire protection such as fire doors, ensuring full compliance with current legislation."),
    defrow("Cleaning &amp; Grounds Maintenance", "From daily cleaning schedules to specialist deep cleans and grounds care, our services help create safe, clean and welcoming environments."),
    defrow("Sustainability &amp; Retrofitting", "We help clients reduce their carbon footprint through energy-efficient upgrades, sustainable materials and retrofit solutions designed for long-term environmental and financial benefits."),
    defrow("Gas Services", "Installation, servicing and repair of boilers, heating systems and gas appliances &mdash; carried out safely by Gas Safe registered engineers, alongside statutory gas safety inspections."),
    defrow("Our Promise", "Our service delivery is backed by compliance reporting, transparency and accountability at every stage. By choosing PJB Partnership, clients gain a reliable partner that delivers quality, safety and value."),
])

PAGES.append(dict(file="services.html", title="Our Services", nav="services",
    desc="End-to-end facilities management from PJB Partnership: maintenance, compliance, M&E, fire safety, cleaning, sustainability and gas services.",
    body=f"""
{page_hero("Our Services", "Delivering end-to-end facilities management solutions that protect people, properties and reputations")}

<section class="section">
  <div class="wrap grid-3">
    {card("Planned &amp; Reactive Maintenance", "Timely and reliable support for everyday issues and long-term care &mdash; reducing downtime and extending asset life.", "service-planned-reactive-maintenance.html")}
    {card("Compliance &amp; Awaab&rsquo;s Law", "Specialists in statutory testing, fire safety and damp &amp; mould remediation &mdash; ensuring fast response and legal compliance.", "service-compliance-awaabs-law.html")}
    {card("Mechanical &amp; Electrical Services", "NICEIC and Gas Safe accredited engineers providing safe, efficient electrical and mechanical support.", "service-mechanical-electrical.html")}
    {card("Fire Safety Compliance", "Installation and maintenance of alarms, fire doors and passive systems &mdash; fully certified and compliant.", "service-fire-safety.html")}
    {card("Cleaning &amp; Grounds Maintenance", "Professional cleaning and grounds care across housing, commercial and hospitality environments.", "service-cleaning-grounds.html")}
    {card("Sustainability &amp; Retrofitting", "Energy-efficiency upgrades, carbon reduction strategies and green materials &mdash; built for long-term savings and environmental impact.", "service-sustainability-retrofitting.html")}
    {card("Gas Services", "Boiler and heating installation, servicing, repairs and statutory safety inspections by Gas Safe engineers.", "service-gas.html")}
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Our Full Range Of Services</span>
      <h2>Quality you can trust</h2>
    </div>
    {services_full}
  </div>
</section>

<section class="section">
  <div class="wrap grid-4">
    {card("Full Service Partner", "Comprehensive facilities management across sectors.")}
    {card("Social Housing Experts", "Specialists in compliance for housing providers.")}
    {card("Sustainable Solutions", "Long-term value through energy efficiency.")}
    {card("24/7 Support", "Reactive maintenance whenever it&rsquo;s needed.")}
  </div>
</section>

{cta()}
"""))

# ============================ SERVICE DETAIL PAGES ============================
def service_page(file, title, intro, sections, bullets):
    body = f"""
{page_hero("Our Services", title, intro, backlink=("All Services", "services.html"))}

<section class="section">
  <div class="wrap">
    {''.join(defrow(h, t) for h, t in sections)}
  </div>
</section>

<section class="section tint">
  <div class="wrap feature">
    <div>
      <span class="eyebrow">What&rsquo;s Included</span>
      <h2>Delivered with compliance, transparency and accountability</h2>
      <ul class="ticks" style="margin-top:18px">{''.join(f'<li>{b}</li>' for b in bullets)}</ul>
    </div>
    <div class="feature-media" aria-hidden="true"></div>
  </div>
</section>

{cta()}
"""
    PAGES.append(dict(file=file, title=title, nav="services",
        desc=intro.replace("&rsquo;", "'").replace("&amp;", "&")[:155], body=body))

service_page("service-planned-reactive-maintenance.html", "Planned &amp; Reactive Maintenance",
    "Timely and reliable support for everyday issues and long-term care &mdash; reducing downtime, extending asset life and keeping buildings safe, compliant and fully operational.",
    [("Reactive Maintenance", "Our responsive maintenance teams ensure issues are addressed quickly, with 24/7 support for urgent call-outs &mdash; minimising disruption for tenants, staff and guests."),
     ("Planned Maintenance", "Planned programmes extend asset life, reduce long-term costs and keep buildings operating smoothly and safely, from communal areas to plant and building fabric."),
     ("Multi-Trade Delivery", "Our multi-skilled operatives cover general repairs, external works including brickwork and fencing, roofing (pitched and flat) and building fabric upgrades including kitchens and bathrooms.")],
    ["24/7 reactive call-out support", "Planned preventative maintenance programmes", "Multi-trade repairs and refurbishment", "External works, roofing and fabric upgrades", "Clear reporting on every job"])

service_page("service-compliance-awaabs-law.html", "Compliance &amp; Awaab&rsquo;s Law",
    "Specialists in statutory testing, fire safety and damp &amp; mould remediation &mdash; ensuring fast response and full legal compliance for housing providers.",
    [("Awaab&rsquo;s Law Remediation", "We support housing providers in meeting Awaab&rsquo;s Law requirements, delivering damp and mould remediation within statutory deadlines. Our teams diagnose issues, apply treatments and restore properties to safe living conditions."),
     ("Statutory Testing &amp; Inspections", "We carry out statutory testing and inspections across gas, electrical and fire safety systems, keeping every property compliant with current legislation."),
     ("Surveys &amp; Reporting", "Specialist damp &amp; mould surveys and property condition reports give landlords clear insights to act on &mdash; supported by compliance data and audit trails.")],
    ["Damp &amp; mould surveys and remediation", "Statutory gas, electrical and fire safety testing", "Delivery within legal timescales", "Evidence-based reporting and audit trails", "Support for regulatory returns and tenant communication"])

service_page("service-mechanical-electrical.html", "Mechanical &amp; Electrical Services",
    "NICEIC and Gas Safe accredited engineers providing safe, efficient electrical and mechanical support across housing, commercial and hospitality environments.",
    [("Electrical Services", "Our NICEIC accredited electricians carry out EICRs, testing, installations and safe electrical maintenance to the highest standards."),
     ("Mechanical &amp; Heating", "Qualified Gas Safe engineers deliver heating and plumbing installations, servicing and repairs, keeping systems safe, efficient and reliable."),
     ("Testing &amp; Certification", "All M&amp;E works include the testing and certification clients need to demonstrate compliance and protect their assets.")],
    ["EICRs, testing and electrical installations", "Heating, plumbing and boiler works", "Gas Safe and NICEIC accredited engineers", "Certification for every completed job", "Planned and reactive M&amp;E support"])

service_page("service-fire-safety.html", "Fire Safety Compliance",
    "Installation and maintenance of fire alarms, fire doors, extinguishers, emergency lighting and passive protection &mdash; fully certified and compliant with current legislation.",
    [("Active Fire Protection", "We install and maintain fire alarms, emergency lighting and extinguishers, keeping detection and response systems fully operational."),
     ("Passive Fire Protection", "From fire doors to compartmentation, our passive fire protection works ensure buildings resist the spread of fire and meet legal requirements."),
     ("Assessments &amp; Surveys", "Our fire safety specialists deliver fire risk assessments, surveys and safety installations that protect tenants, guests and staff.")],
    ["Fire alarm installation and maintenance", "Fire doors and passive protection", "Emergency lighting and extinguishers", "Fire risk assessments and surveys", "Full compliance with current legislation"])

service_page("service-cleaning-grounds.html", "Cleaning &amp; Grounds Maintenance",
    "Professional, flexible and efficient cleaning and grounds care across housing, commercial and hospitality environments.",
    [("Cleaning Services", "From daily cleaning schedules to specialist deep cleans, our teams help create safe, clean and welcoming environments for residents, staff and guests."),
     ("Waste Management", "Reliable, professional and sustainable waste management keeps estates and premises tidy, hygienic and compliant."),
     ("Grounds Maintenance", "We keep outdoor spaces safe and well maintained &mdash; grounds upkeep, estate care and external cleaning to a consistently high standard.")],
    ["Daily and scheduled cleaning", "Specialist deep cleans", "Waste removal and management", "Grounds and estate maintenance", "Flexible contracts across sectors"])

service_page("service-sustainability-retrofitting.html", "Sustainability &amp; Retrofitting",
    "Energy-efficiency upgrades, carbon reduction strategies and green materials &mdash; built for long-term savings and environmental impact.",
    [("Energy Efficiency Upgrades", "We help clients reduce their carbon footprint through energy-efficient upgrades and retrofit solutions designed for long-term environmental and financial benefit."),
     ("Sustainable Materials &amp; Procurement", "Green procurement and sustainable materials are built into our delivery, supporting clients&rsquo; environmental commitments."),
     ("Long-Term Value", "Retrofitting is an investment: our programmes are designed to lower running costs, improve comfort and futureproof housing stock and commercial buildings alike.")],
    ["Energy efficiency retrofits", "Carbon reduction strategies", "Sustainable materials and green procurement", "Support for futureproofing housing stock", "ISO 14001 certified environmental management"])

service_page("service-gas.html", "Gas Services",
    "Installation, servicing and repair of boilers, heating systems and gas appliances &mdash; carried out safely by Gas Safe registered engineers.",
    [("Installation &amp; Replacement", "Our Gas Safe engineers install and replace boilers, heating systems and gas appliances safely and efficiently."),
     ("Servicing &amp; Repairs", "Planned servicing and responsive repairs keep heating systems reliable, efficient and safe all year round."),
     ("Statutory Safety Inspections", "We deliver the statutory gas safety inspections landlords require, supported by clear records and certification.")],
    ["Boiler installation, servicing and repair", "Heating system maintenance", "Gas appliance safety checks", "Statutory landlord inspections and certification", "Gas Safe registered engineers on every job"])

# ============================ SECTORS HUB ============================
sector_rows = "".join([
    defrow("Social Housing", "We are trusted by housing associations and providers to deliver maintenance, compliance and improvement programmes that ensure tenant safety and satisfaction. Our expertise in damp and mould remediation, aligned with Awaab&rsquo;s Law, positions us as a reliable partner in helping providers meet strict legal standards. We also deliver planned maintenance and refurbishment works to improve housing stock and create better living environments."),
    defrow("Local Authorities", "Councils and public sector bodies rely on PJB Partnership for transparent, accountable delivery of facilities management programmes. From statutory compliance to large-scale refurbishment, we provide services that balance value for money with high standards of safety and sustainability. We understand the pressures local authorities face and work in partnership to deliver efficient, compliant and cost-effective outcomes."),
    defrow("Commercial", "For offices, retail units and mixed-use developments, we offer tailored FM solutions that prioritise compliance, operational efficiency and tenant satisfaction. Whether through planned maintenance, technical services or sustainability programmes, our commercial services are designed to ensure businesses can operate in safe and efficient spaces."),
    defrow("Hospitality", "PJB Partnership works with hotels and leisure operators to deliver facilities management that enhances guest experience and operational efficiency. From fire safety compliance to reactive maintenance, our services help hospitality businesses maintain high standards while controlling costs and ensuring safety."),
    defrow("Our Values In Action", "In every sector, we apply our core values of Community, Accountability, Trust and Operations to ensure services are delivered transparently, responsibly and with a clear focus on people and outcomes."),
])

PAGES.append(dict(file="sectors.html", title="Sectors We Serve", nav="sectors",
    desc="PJB Partnership delivers facilities management for social housing, local authorities, commercial, hospitality, healthcare and education.",
    body=f"""
{page_hero("Our Sectors", "Delivering safe, compliant and sustainable facilities management across housing, public, commercial and hospitality",
  "PJB Partnership provides facilities management tailored to the unique needs of every sector. From housing associations to hotel groups, we deliver compliance-led, transparent and sustainable solutions that protect people, properties and reputations.")}

{stats()}

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Who We Serve</span>
      <h2>Facilities management expertise for every sector</h2>
    </div>
    <div class="grid-3">
      {card("Social Housing", "Supporting housing associations and providers with compliance, maintenance and refurbishment &mdash; always prioritising tenant safety and comfort.", "sector-social-housing.html")}
      {card("Public Sector &amp; Local Authorities", "Delivering large-scale FM programmes for councils and public buildings with transparency, accountability and value for money.", "sector-public-sector.html")}
      {card("Commercial Properties", "Tailored solutions for offices, retail and mixed-use buildings &mdash; ensuring safe, efficient and compliant environments.", "sector-commercial.html")}
      {card("Hospitality &amp; Leisure", "Working with hotel groups and leisure operators to maintain safe, welcoming and high-performing facilities.", "sector-hospitality-leisure.html")}
      {card("Healthcare &amp; Education", "Safe, hygienic and compliant environments for care settings, schools and colleges &mdash; where standards matter most.", "sector-healthcare-education.html")}
    </div>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Who We Serve</span>
      <h2>Our full sector overview</h2>
    </div>
    {sector_rows}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Our Clients</span>
      <h2>We believe every client is a valuable long-term partner</h2>
    </div>
    {clients_rows}
  </div>
</section>

{cta("Need a trusted facilities management partner?",
     "Looking for a facilities management partner for housing, local authority, commercial or hospitality needs? PJB Partnership is here to deliver.")}
"""))

# ============================ SECTOR DETAIL PAGES ============================
def sector_page(file, title, intro, sections, bullets):
    body = f"""
{page_hero("Sectors We Serve", title, intro, backlink=("All Sectors", "sectors.html"))}

<section class="section">
  <div class="wrap">
    {''.join(defrow(h, t) for h, t in sections)}
  </div>
</section>

<section class="section tint">
  <div class="wrap feature">
    <div>
      <span class="eyebrow">How We Support This Sector</span>
      <h2>Compliance-led, transparent, sustainable</h2>
      <ul class="ticks" style="margin-top:18px">{''.join(f'<li>{b}</li>' for b in bullets)}</ul>
    </div>
    <div class="feature-media" aria-hidden="true"></div>
  </div>
</section>

{cta()}
"""
    PAGES.append(dict(file=file, title=title, nav="sectors",
        desc=intro.replace("&rsquo;", "'").replace("&amp;", "&")[:155], body=body))

sector_page("sector-social-housing.html", "Social Housing",
    "Supporting housing associations and providers with compliance, maintenance and refurbishment &mdash; always prioritising tenant safety and comfort.",
    [("A Trusted Housing Partner", "We are trusted by housing associations and providers to deliver maintenance, compliance and improvement programmes that ensure tenant safety and satisfaction. Our partnerships with organisations such as Riverside, One Housing and The Home Group reflect our track record in this sector."),
     ("Awaab&rsquo;s Law Expertise", "Our expertise in damp and mould remediation, aligned with Awaab&rsquo;s Law, positions us as a reliable partner in helping providers meet strict legal standards within statutory deadlines."),
     ("Improving Housing Stock", "We deliver planned maintenance and refurbishment works &mdash; including kitchens, bathrooms, roofing and fabric upgrades &mdash; that improve housing stock and create better living environments.")],
    ["Damp &amp; mould remediation to Awaab&rsquo;s Law standards", "Statutory gas, electrical and fire safety compliance", "Planned maintenance and refurbishment programmes", "Responsive repairs with 24/7 support", "Transparent reporting for regulatory confidence"])

sector_page("sector-public-sector.html", "Public Sector &amp; Local Authorities",
    "Delivering large-scale FM programmes for councils and public buildings with transparency, accountability and value for money.",
    [("Accountable Delivery", "Councils and public sector bodies rely on PJB Partnership for transparent, accountable delivery of facilities management programmes, with full reporting, compliance data and audit trails."),
     ("Value For Money", "From statutory compliance to large-scale refurbishment, we provide services that balance value for money with high standards of safety and sustainability."),
     ("Working In Partnership", "We understand the pressures local authorities face and work in partnership to deliver efficient, compliant and cost-effective outcomes for public buildings and property portfolios.")],
    ["Large-scale FM programmes for public portfolios", "Statutory compliance across gas, electrical and fire safety", "Refurbishment and improvement works", "Open-book transparency and audit trails", "Sustainability and retrofit programmes"])

sector_page("sector-hospitality-leisure.html", "Hospitality &amp; Leisure",
    "Working with hotel groups and leisure operators to maintain safe, welcoming and high-performing facilities that protect guest experience and brand reputation.",
    [("Guest Experience First", "PJB Partnership works with hotels and leisure operators to deliver facilities management that enhances guest experience and operational efficiency &mdash; discreet, responsive and reliable."),
     ("Compliance &amp; Safety", "From fire safety compliance to reactive maintenance, our services help hospitality businesses maintain high standards while controlling costs and ensuring safety."),
     ("Proven Capability", "Our experience with hotel and leisure operators demonstrates our capability in this sector: smooth operations, compliance and safe environments that protect brand reputation.")],
    ["Reactive maintenance with minimal guest disruption", "Fire safety and statutory compliance", "M&amp;E, heating and plumbing support", "Cleaning and grounds maintenance", "Planned programmes that control costs"])

sector_page("sector-commercial.html", "Commercial Properties",
    "Tailored FM solutions for offices, retail units and mixed-use developments &mdash; ensuring safe, efficient and compliant environments.",
    [("Tailored FM Solutions", "For offices, retail units and mixed-use developments, we offer tailored FM solutions that prioritise compliance, operational efficiency and tenant satisfaction."),
     ("Keeping Business Running", "Whether through planned maintenance, technical services or sustainability programmes, our commercial services are designed to ensure businesses can operate in safe and efficient spaces."),
     ("Protecting Asset Value", "High-quality maintenance, external works and refurbishment protect and enhance property value over the long term.")],
    ["Planned and reactive maintenance", "M&amp;E and technical services", "Fire safety and statutory compliance", "Cleaning, waste and grounds care", "Sustainability and energy-efficiency programmes"])

sector_page("sector-healthcare-education.html", "Healthcare &amp; Education",
    "Safe, hygienic and compliant environments for care settings, schools and colleges &mdash; where standards matter most.",
    [("Environments That Care", "Healthcare and education settings demand the highest standards of safety, hygiene and compliance. Our teams deliver maintenance and cleaning services that keep these environments safe and welcoming for patients, pupils and staff."),
     ("Compliance Without Compromise", "Statutory testing across gas, electrical and fire safety systems, supported by clear reporting and audit trails, gives providers confidence that legal requirements are met."),
     ("Minimal Disruption", "We plan and deliver works around the operational needs of care settings and schools, minimising disruption to services, learning and care.")],
    ["Statutory compliance testing and certification", "Planned and reactive maintenance", "Specialist cleaning and hygiene support", "Fire safety compliance", "Works scheduled around service needs"])

# ============================ CAREERS HUB ============================
career_future = "".join([
    defrow("Training &amp; Development", "We invest in our people, offering ongoing training, apprenticeships and career development opportunities. Whether you are starting out or bringing years of experience, we help you grow and achieve your goals."),
    defrow("Health &amp; Safety Commitment", "We put the safety of our staff first. With ISO&nbsp;45001 accreditation, we ensure a safe and supportive working environment across all projects."),
    defrow("Diversity &amp; Inclusion", "We believe diverse teams deliver the best results. At PJB, every individual is valued, respected and supported to succeed."),
    defrow("Making An Impact", "Our work directly improves homes, communities and businesses. From delivering Awaab&rsquo;s Law compliance to sustainability projects, our teams make a measurable difference."),
    defrow("Our Vision", "We are always looking for professionals who share our vision. If you want to work in a company that values accountability, professionalism and community impact, then PJB Partnership is the right place for you."),
])

PAGES.append(dict(file="careers.html", title="Careers", nav="careers",
    desc="Join PJB Partnership — careers for gas engineers, electricians, compliance officers, fire safety specialists and facilities operatives.",
    body=f"""
{page_hero("Careers at PJB", "Join a team that builds safer communities through trust and accountability",
  "At PJB Partnership, our people are at the heart of our success. We&rsquo;re always looking for talented individuals who share our values of Community, Accountability, Trust and Operations. Whether you&rsquo;re an engineer, compliance officer or facilities specialist, we provide opportunities to grow your career while making a real difference in the communities we serve.")}

<section class="section">
  <div class="wrap grid-4">
    {card("Community", "Work on projects that improve homes, public spaces and communities across the UK.")}
    {card("Accountability", "Be part of a team that takes pride in transparency, quality and responsibility.")}
    {card("Trust", "Join a company that values reliability and builds long-term partnerships with both clients and employees.")}
    {card("Operations", "Develop your skills in a fast-paced environment with structured processes and professional support.")}
  </div>
</section>

<section class="stats">
  <div class="wrap grid-4">
    <div class="stat"><b>Growth</b><span>Ongoing training &amp; development</span></div>
    <div class="stat"><b>Safe</b><span>ISO 45001 accredited workplace</span></div>
    <div class="stat"><b>Inclusive</b><span>Diverse teams, everyone valued</span></div>
    <div class="stat"><b>Impact</b><span>Real difference in communities</span></div>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Job Opportunities</span>
      <h2>Build a career that makes a difference</h2>
    </div>
    <div class="grid-3">
      {card("Project Managers &amp; Compliance Officers", "Oversee contracts, compliance programmes and client relationships with high standards.", "career-project-managers.html")}
      {card("Gas Safe Engineers", "Install, service and repair boilers, heating systems and gas appliances safely.", "career-gas-safe-engineers.html")}
      {card("Electricians (NICEIC)", "Carry out EICRs, testing, installations and deliver safe electrical maintenance.", "career-electricians.html")}
      {card("Fire Safety Specialists", "Deliver fire risk assessments, surveys and safety installations to protect tenants.", "career-fire-safety.html")}
      {card("Damp &amp; Mould Remediation Teams", "Diagnose issues, apply treatments and restore properties to safe living conditions.", "career-damp-mould.html")}
      {card("Facilities Management Operatives", "Perform multi-trade repairs, maintenance and respond quickly to reactive call-outs.", "career-fm-operatives.html")}
      {card("Cleaning &amp; Grounds Maintenance Staff", "Maintain estates with daily cleaning, waste removal and high-standard grounds upkeep.", "career-cleaning-grounds.html")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Your Future With Us</span>
      <h2>Building your career at PJB Partnership</h2>
    </div>
    {career_future}
  </div>
</section>

{cta("Ready to build your career with PJB Partnership?",
     "Apply today and join a company where your skills and values make a real difference.",
     "Apply Now")}
"""))

# ============================ CAREER DETAIL PAGES ============================
def career_page(file, title, summary, duties, lookfor):
    body = f"""
{page_hero("Careers at PJB", title, summary, backlink=("All Roles", "careers.html"))}

<section class="section">
  <div class="wrap">
    {defrow("The Role", summary + " You will join a team guided by our values of Community, Accountability, Trust and Operations, working across housing, public sector, commercial and hospitality environments.")}
    {defrow("What You&rsquo;ll Do", "<ul class='ticks'>" + ''.join(f'<li>{d}</li>' for d in duties) + "</ul>")}
    {defrow("What We Look For", "<ul class='ticks'>" + ''.join(f'<li>{l}</li>' for l in lookfor) + "</ul>")}
    {defrow("What We Offer", "<ul class='ticks'><li>Ongoing training, apprenticeships and career development</li><li>A safe workplace &mdash; ISO&nbsp;45001 accredited</li><li>An inclusive culture where everyone is valued</li><li>Work that makes a real difference in homes and communities</li></ul>")}
  </div>
</section>

{cta("Interested in this role?",
     "Send us your CV and a short note about your experience &mdash; we&rsquo;d love to hear from you.",
     "Apply Now")}
"""
    PAGES.append(dict(file=file, title=title, nav="careers",
        desc=summary.replace("&rsquo;", "'").replace("&amp;", "&")[:155], body=body))

career_page("career-gas-safe-engineers.html", "Gas Safe Engineers",
    "Install, service and repair boilers, heating systems and gas appliances safely.",
    ["Install, service and repair boilers, heating systems and gas appliances",
     "Carry out statutory gas safety inspections and certification",
     "Diagnose faults and complete responsive repairs",
     "Keep clear, accurate job records for compliance reporting"],
    ["Current Gas Safe registration", "Experience in domestic and/or commercial gas work", "A safety-first, customer-focused approach", "Full UK driving licence"])

career_page("career-project-managers.html", "Project Managers &amp; Compliance Officers",
    "Oversee contracts, compliance programmes and client relationships with high standards.",
    ["Manage contracts and compliance-led programmes from mobilisation to completion",
     "Monitor statutory compliance and maintain evidence and audit trails",
     "Build strong client relationships with clear, transparent reporting",
     "Coordinate multi-trade teams to deliver on time and on budget"],
    ["Experience in FM, housing or construction project delivery", "Strong knowledge of statutory compliance requirements", "Excellent communication and reporting skills", "A commitment to accountability and quality"])

career_page("career-electricians.html", "Electricians (NICEIC)",
    "Carry out EICRs, testing, installations and deliver safe electrical maintenance.",
    ["Carry out EICRs, periodic testing and remedial works",
     "Complete installations and planned electrical maintenance",
     "Respond to reactive electrical call-outs",
     "Produce certification and compliance documentation"],
    ["18th Edition qualified; NICEIC experience preferred", "Testing and inspection qualifications (e.g. 2391) desirable", "A tidy, professional approach on site", "Full UK driving licence"])

career_page("career-damp-mould.html", "Damp &amp; Mould Remediation Teams",
    "Diagnose issues, apply treatments and restore properties to safe living conditions.",
    ["Survey and diagnose damp, mould and condensation issues",
     "Apply treatments and complete remediation works to statutory timescales",
     "Restore affected areas including plastering, decoration and ventilation improvements",
     "Record evidence to support Awaab&rsquo;s Law compliance reporting"],
    ["Experience in damp/mould remediation or related trades", "Understanding of Awaab&rsquo;s Law obligations desirable", "A respectful, resident-focused manner", "Attention to detail in recording works"])

career_page("career-fire-safety.html", "Fire Safety Specialists",
    "Deliver fire risk assessments, surveys and safety installations to protect tenants.",
    ["Deliver fire risk assessments and fire safety surveys",
     "Install and maintain fire doors, alarms, emergency lighting and passive protection",
     "Identify and report remedial actions with clear documentation",
     "Work with clients to keep buildings fully compliant"],
    ["Recognised fire safety qualifications and experience", "Knowledge of current fire safety legislation", "Strong report-writing skills", "A meticulous, safety-first mindset"])

career_page("career-cleaning-grounds.html", "Cleaning &amp; Grounds Maintenance Staff",
    "Maintain estates with daily cleaning, waste removal and high-standard grounds upkeep.",
    ["Deliver daily and scheduled cleaning across estates and premises",
     "Carry out waste removal and specialist deep cleans",
     "Maintain grounds and outdoor spaces to a high standard",
     "Report issues and hazards promptly"],
    ["Reliability and pride in high standards", "Experience in cleaning or grounds work helpful, not essential", "A friendly, professional manner with residents and clients", "Willingness to learn and develop"])

career_page("career-fm-operatives.html", "Facilities Management Operatives",
    "Perform multi-trade repairs, maintenance and respond quickly to reactive call-outs.",
    ["Complete multi-trade repairs and planned maintenance tasks",
     "Respond quickly to reactive call-outs, including out of hours where required",
     "Work across housing, commercial and hospitality sites",
     "Keep accurate records of works completed"],
    ["Multi-trade skills (carpentry, plumbing, decorating or similar)", "A flexible, can-do approach", "Good communication with residents and site staff", "Full UK driving licence"])

# ============================ CONTACT ============================
PAGES.append(dict(file="contact.html", title="Contact Us", nav="contact",
    desc="Contact PJB Partnership — 8 Shenley Pavilions, Shenley Wood, Milton Keynes, MK5 6LB. Call 01908 034578.",
    body=f"""
{page_hero("Contact Us", "Let&rsquo;s talk about your facilities",
  "Whether you need compliance-driven maintenance, sustainable building upgrades or complete FM support, we&rsquo;d love to hear from you. Tell us about your requirements and we&rsquo;ll come back to you promptly.")}

<section class="section">
  <div class="wrap contact-grid">
    <div>
      <div class="contact-card">
        <h3>PJB Partnership</h3>
        <em style="font-style:normal;color:#4FA3FF;font-family:var(--font-display);font-weight:700;font-size:.75rem;letter-spacing:.28em;text-transform:uppercase;">Built on Trust</em>
        <p class="label">Head Office</p>
        <p>8 Shenley Pavilions<br>Shenley Wood<br>Milton Keynes, MK5 6LB</p>
        <p class="label">Telephone</p>
        <p><a href="tel:+441908034578">01908 034578</a></p>
        <p class="label">Chief Executive Officer</p>
        <p>Peter Baldwin<br><a href="mailto:peter.baldwin@pjbpartnership.co.uk">peter.baldwin@pjbpartnership.co.uk</a><br><a href="tel:+447793269278">07793 269278</a></p>
      </div>
    </div>
    <div>
      <h2>Request a call back</h2>
      <form class="contact-form" action="mailto:peter.baldwin@pjbpartnership.co.uk" method="post" enctype="text/plain">
        <label for="cf-name">Name</label>
        <input id="cf-name" name="name" type="text" autocomplete="name" required>
        <label for="cf-org">Organisation</label>
        <input id="cf-org" name="organisation" type="text" autocomplete="organization">
        <label for="cf-email">Email</label>
        <input id="cf-email" name="email" type="email" autocomplete="email" required>
        <label for="cf-phone">Phone</label>
        <input id="cf-phone" name="phone" type="tel" autocomplete="tel">
        <label for="cf-topic">What can we help with?</label>
        <select id="cf-topic" name="topic">
          <option>General enquiry</option>
          <option>Planned &amp; reactive maintenance</option>
          <option>Compliance &amp; Awaab&rsquo;s Law</option>
          <option>Mechanical &amp; electrical services</option>
          <option>Fire safety compliance</option>
          <option>Cleaning &amp; grounds maintenance</option>
          <option>Sustainability &amp; retrofitting</option>
          <option>Gas services</option>
          <option>Careers</option>
        </select>
        <label for="cf-msg">Message</label>
        <textarea id="cf-msg" name="message" rows="5" required></textarea>
        <button class="btn btn-primary" type="submit">Send Enquiry</button>
        <p class="form-note">This form opens your email client. For a hosted form service (e.g. Formspree), see the README in the site code.</p>
      </form>
    </div>
  </div>
</section>
"""))

# ============================ POLICIES ============================
def policy_page(file, title, body_html):
    PAGES.append(dict(file=file, title=title, nav="",
        desc=f"{title} for the PJB Partnership website.",
        body=f"""
{page_hero("Legal", title)}
<section class="section">
  <div class="wrap prose">
    <p><em>Template for review &mdash; please have this checked and completed by your legal adviser before launch.</em></p>
    {body_html}
  </div>
</section>
"""))

policy_page("privacy-policy.html", "Privacy Policy", """
<h2>Who we are</h2>
<p>PJB Partnership (&ldquo;we&rdquo;, &ldquo;us&rdquo;), 8 Shenley Pavilions, Shenley Wood, Milton Keynes, MK5 6LB. Contact: <a href="mailto:hello@pjbpartnership.co.uk">hello@pjbpartnership.co.uk</a>.</p>
<h2>What we collect</h2>
<p>When you contact us we may collect your name, organisation, email address, telephone number and the details of your enquiry.</p>
<h2>How we use your information</h2>
<ul>
<li>To respond to enquiries and provide our services</li>
<li>To manage contracts, compliance obligations and client relationships</li>
<li>To consider applications for employment</li>
</ul>
<h2>Legal basis</h2>
<p>We process personal data under UK GDPR on the basis of legitimate interests, contract performance and, where applicable, legal obligation.</p>
<h2>Sharing and retention</h2>
<p>We do not sell personal data. We share it only with service providers who help us operate, and retain it only as long as necessary for the purposes above.</p>
<h2>Your rights</h2>
<p>You have the right to access, correct or request deletion of your personal data, and to complain to the Information Commissioner&rsquo;s Office (ICO). To exercise your rights, email <a href="mailto:hello@pjbpartnership.co.uk">hello@pjbpartnership.co.uk</a>.</p>
""")

policy_page("cookie-policy.html", "Cookie Policy", """
<h2>Cookies on this website</h2>
<p>This website is a static site and does not set cookies of its own. Third-party services we use may set cookies:</p>
<ul>
<li><b>Google Fonts</b> &mdash; used to load the site&rsquo;s typefaces.</li>
</ul>
<h2>Managing cookies</h2>
<p>You can control and delete cookies through your browser settings. Blocking cookies will not prevent you from using this site.</p>
<h2>Changes</h2>
<p>If we add analytics or other services that use cookies, this policy will be updated before they are enabled.</p>
""")

policy_page("terms.html", "Terms &amp; Conditions", """
<h2>Use of this website</h2>
<p>This website is provided by PJB Partnership for general information about our services. By using it you agree to these terms.</p>
<h2>Content</h2>
<p>We take care to keep information accurate and up to date, but content is provided &ldquo;as is&rdquo; without warranties. Nothing on this site constitutes a contractual offer; services are provided under separate written agreements.</p>
<h2>Intellectual property</h2>
<p>The PJB Partnership name, logo and site content are the property of PJB Partnership and may not be reproduced without permission.</p>
<h2>Liability</h2>
<p>To the fullest extent permitted by law, we accept no liability for loss arising from reliance on the content of this website.</p>
<h2>Governing law</h2>
<p>These terms are governed by the laws of England and Wales.</p>
""")

# ---------------------------------------------------------------
for p in PAGES:
    out = shell(file=p["file"], title=p["title"].replace("&amp;", "&").replace("&rsquo;", "\u2019"),
                desc=p["desc"], nav=p["nav"], body=p["body"])
    (ROOT / p["file"]).write_text(out, encoding="utf-8")
    print("wrote", p["file"])
print(f"\n{len(PAGES)} pages generated.")
