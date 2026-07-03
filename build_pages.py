#!/usr/bin/env python3
"""Generate the top-level marketing pages (about, pricing, get-started, contact, resources).
Content faithful to trustlogix.ai; theme matches the local build. Paths use ../ (one level deep)."""
import os

P = '..'  # asset prefix for one-level-deep pages

NAV = f'''  <header class="nav nav--transparent" id="nav">
    <div class="nav__inner">
      <a href="/" class="nav__logo" aria-label="TrustLogix home">
        <img src="{P}/logos/trustlogix-logo-darkbg.svg" alt="TrustLogix" class="nav__logo-img nav__logo-img--darkbg" width="200" height="34" />
        <img src="{P}/trustlogix-logo.svg" alt="TrustLogix" class="nav__logo-img nav__logo-img--lightbg" width="200" height="34" />
      </a>
      <nav class="nav__menu" aria-label="Primary">
        <div class="nav__item">
          <a href="/platform" class="nav__link"><span class="nav__swap"><span>Platform</span><span aria-hidden="true">Platform</span></span>
            <svg class="nav__chevron" viewBox="0 0 512 512" fill="currentColor"><path d="M255.998 406.054C246.292 406.054 237.469 402.524 230.41 395.466L9.81896 166.051C-3.41649 151.933 -3.41649 129.874 10.7013 115.756C24.8191 102.521 46.8782 102.521 60.996 116.639L255.998 319.582L451 116.639C464.236 102.521 487.177 102.521 501.295 115.756C515.413 128.992 515.413 151.933 502.178 166.051L281.587 395.466C274.528 402.524 265.704 406.054 255.998 406.054Z"/></svg>
          </a>
          <div class="nav__dropdown">
            <a href="/platform" class="nav__dropdown-overview"><span class="nav__menu-label">Overview</span><span class="nav__dropdown-desc">Our platform architecture, core modules, and benefits.</span></a>
            <a href="/platform/trustai">– TrustAI</a>
            <a href="/platform/trustdspm">– TrustDSPM</a>
            <a href="/platform/trustaccess">– TrustAccess</a>
          </div>
        </div>
        <div class="nav__item">
          <a href="/partners" class="nav__link"><span class="nav__swap"><span>Partners</span><span aria-hidden="true">Partners</span></span>
            <svg class="nav__chevron" viewBox="0 0 512 512" fill="currentColor"><path d="M255.998 406.054C246.292 406.054 237.469 402.524 230.41 395.466L9.81896 166.051C-3.41649 151.933 -3.41649 129.874 10.7013 115.756C24.8191 102.521 46.8782 102.521 60.996 116.639L255.998 319.582L451 116.639C464.236 102.521 487.177 102.521 501.295 115.756C515.413 128.992 515.413 151.933 502.178 166.051L281.587 395.466C274.528 402.524 265.704 406.054 255.998 406.054Z"/></svg>
          </a>
          <div class="nav__dropdown">
            <a href="/partners" class="nav__dropdown-overview"><span class="nav__menu-label">Overview</span><span class="nav__dropdown-desc">Introduction to the TrustLogix Interoperable Ecosystem.</span></a>
            <a href="/partners/snowflake">– Snowflake</a>
            <a href="/partners/databricks">– Databricks</a>
            <a href="/partners/microsoft">– Power BI</a>
            <a href="/partners/aws">– AWS</a>
            <a href="/partners/alation">– Alation</a>
            <a href="/partners/collibra">– Collibra</a>
          </div>
        </div>
        <div class="nav__item"><a href="/pricing" class="nav__link"><span class="nav__swap"><span>Pricing</span><span aria-hidden="true">Pricing</span></span></a></div>
        <div class="nav__item">
          <a href="/resources" class="nav__link"><span class="nav__swap"><span>Resources</span><span aria-hidden="true">Resources</span></span>
            <svg class="nav__chevron" viewBox="0 0 512 512" fill="currentColor"><path d="M255.998 406.054C246.292 406.054 237.469 402.524 230.41 395.466L9.81896 166.051C-3.41649 151.933 -3.41649 129.874 10.7013 115.756C24.8191 102.521 46.8782 102.521 60.996 116.639L255.998 319.582L451 116.639C464.236 102.521 487.177 102.521 501.295 115.756C515.413 128.992 515.413 151.933 502.178 166.051L281.587 395.466C274.528 402.524 265.704 406.054 255.998 406.054Z"/></svg>
          </a>
          <div class="nav__dropdown">
            <a href="/resources" class="nav__dropdown-overview"><span class="nav__menu-label">Overview</span><span class="nav__dropdown-desc">Resources available to existing and potential customers.</span></a>
            <a href="/resource-library">– Resource Library</a>
            <a href="/blog">– The TrustLogix Blog</a>
            <a href="https://docs.trustlogix.io/">– Documentation</a>
            <a href="/newsletter">– Newsletter</a>
          </div>
        </div>
        <div class="nav__item">
          <a href="/about" class="nav__link"><span class="nav__swap"><span>About</span><span aria-hidden="true">About</span></span>
            <svg class="nav__chevron" viewBox="0 0 512 512" fill="currentColor"><path d="M255.998 406.054C246.292 406.054 237.469 402.524 230.41 395.466L9.81896 166.051C-3.41649 151.933 -3.41649 129.874 10.7013 115.756C24.8191 102.521 46.8782 102.521 60.996 116.639L255.998 319.582L451 116.639C464.236 102.521 487.177 102.521 501.295 115.756C515.413 128.992 515.413 151.933 502.178 166.051L281.587 395.466C274.528 402.524 265.704 406.054 255.998 406.054Z"/></svg>
          </a>
          <div class="nav__dropdown">
            <a href="/about" class="nav__dropdown-overview"><span class="nav__menu-label">Overview</span><span class="nav__dropdown-desc">About TrustLogix – our culture, values, and more.</span></a>
            <a href="/events">– Events</a>
            <a href="/newsroom">– Newsroom</a>
            <a href="/newsroom/press-releases">– Press Releases</a>
            <a href="/careers">– Careers</a>
            <a href="/contact">– Contact</a>
          </div>
        </div>
      </nav>
      <div class="nav__actions">
        <a href="/get-started" class="btn btn--primary"><span class="btn__swap"><span>Get Started</span><span aria-hidden="true">Get Started</span></span></a>
        <button class="nav__burger" id="burger" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>'''

def cta(primary=('Get Started','/get-started'), secondary=('Our Platform','/platform')):
    return f'''    <section class="cta-final">
      <div class="cta-final__card reveal">
        <div class="cta-final__bg"></div>
        <img class="cta-final__graphic" src="{P}/logos/cta-bg-graphic.svg" alt="" aria-hidden="true" />
        <div class="cta-final__content">
          <div class="cta-final__left"><h2 class="cta-final__title">Experience TrustLogix in Action</h2></div>
          <div class="cta-final__right">
            <p class="cta-final__sub">Schedule a call to discover how TrustLogix can accelerate your AI initiatives with faster, safer data access.</p>
            <div class="cta-final__buttons">
              <a href="{primary[1]}" class="btn cta-final__btn cta-final__btn--primary"><span class="btn__swap"><span>{primary[0]}</span><span aria-hidden="true">{primary[0]}</span></span></a>
              <a href="{secondary[1]}" class="btn cta-final__btn cta-final__btn--secondary"><span class="btn__swap"><span>{secondary[0]}</span><span aria-hidden="true">{secondary[0]}</span></span></a>
            </div>
          </div>
        </div>
      </div>
      <div class="cta-final__strip"></div>
    </section>'''

FOOTER = f'''  <footer class="footer footer--brand footer--light">
    <div class="container">
      <div class="footer__top">
        <a href="/" class="footer__logo" aria-label="TrustLogix"><img src="{P}/trustlogix-logo.svg" alt="TrustLogix" width="180" height="31" /></a>
        <p class="footer__tagline">Unified, secure access to the data that drives AI—so innovation moves quickly, safely.</p>
        <div class="footer__social">
          <a href="https://x.com/TrustLogix" target="_blank" rel="noopener" aria-label="X"><svg viewBox="0 0 24 24" fill="none"><path d="M17.1761 4H19.9362L13.9061 10.7774L21 20H15.4456L11.0951 14.4066L6.11723 20H3.35544L9.80517 12.7508L3 4H8.69545L12.6279 9.11262L17.1761 4ZM16.2073 18.3754H17.7368L7.86441 5.53928H6.2232L16.2073 18.3754Z" fill="currentColor"/></svg></a>
          <a href="https://www.linkedin.com/company/trustlogix/" target="_blank" rel="noopener" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.5 3C3.67157 3 3 3.67157 3 4.5V19.5C3 20.3284 3.67157 21 4.5 21H19.5C20.3284 21 21 20.3284 21 19.5V4.5C21 3.67157 20.3284 3 19.5 3H4.5ZM8.52076 7.00272C8.52639 7.95897 7.81061 8.54819 6.96123 8.54397C6.16107 8.53975 5.46357 7.90272 5.46779 7.00413C5.47201 6.15897 6.13998 5.47975 7.00764 5.49944C7.88795 5.51913 8.52639 6.1646 8.52076 7.00272ZM12.2797 9.76176H9.7583V18.3216H12.4217V16.9819C12.4203 15.9674 12.4194 14.9532 12.4246 13.9397C12.426 13.6936 12.4372 13.4377 12.5005 13.2028C12.7381 12.3253 13.5271 11.7586 14.4074 11.8979C14.9727 11.9864 15.3467 12.3141 15.5042 12.8471C15.6013 13.1803 15.6449 13.5389 15.6491 13.8863C15.6589 15.9815 15.6573 17.0294 15.6561 18.1388V18.3202H18.328V16.7591C18.327 15.6293 18.3264 14.5001 18.3294 13.3702C18.3308 12.8597 18.276 12.3563 18.1508 11.8627C17.9638 11.1286 17.5771 10.5211 16.9485 10.0824C16.5027 9.77019 16.0133 9.5691 15.4663 9.5466C15.404 9.54401 14.7141 9.50673 14.4467 9.56066C13.6817 9.71394 13.0096 10.0641 12.5019 10.6814C12.4429 10.7522 12.3852 10.8241 12.2991 10.9315L12.2797 10.9557V9.76176ZM5.68164 18.3244H8.33242V9.76733H5.68164V18.3244Z" fill="currentColor"/></svg></a>
          <a href="http://www.youtube.com/@trustlogix" target="_blank" rel="noopener" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M20.5686 4.77345C21.5163 5.02692 22.2555 5.76903 22.5118 6.71673C23.1821 9.42042 23.1385 14.5321 22.5259 17.278C22.2724 18.2257 21.5303 18.965 20.5826 19.2213C17.9071 19.8831 5.92356 19.8015 3.40294 19.2213C2.45524 18.9678 1.71595 18.2257 1.45966 17.278C0.827391 14.7011 0.871044 9.25144 1.44558 6.73081C1.69905 5.78311 2.44116 5.04382 3.38886 4.78753C6.96561 4.0412 19.2956 4.282 20.5686 4.77345ZM9.86682 8.70227L15.6122 11.9974L9.86682 15.2925V8.70227Z" fill="currentColor"/></svg></a>
        </div>
      </div>
      <div class="footer__links">
        <div class="footer__col"><h5>Platform</h5><a href="/platform">Platform Overview</a><a href="/platform/trustdspm">TrustDSPM</a><a href="/platform/trustaccess">TrustAccess</a><a href="/platform/trustai">TrustAI</a></div>
        <div class="footer__col"><h5>Partners</h5><a href="/partners">Partners Overview</a><a href="/partners/snowflake">Snowflake</a><a href="/partners/databricks">Databricks</a><a href="/partners/microsoft">Power BI</a><a href="/partners/aws">AWS</a><a href="/partners/alation">Alation</a><a href="/partners/collibra">Collibra</a></div>
        <div class="footer__col"><h5>Resources</h5><a href="/resources">Resources Overview</a><a href="/resource-library">Resource Library</a><a href="/blog">The TrustLogix Blog</a><a href="https://docs.trustlogix.io/">Documentation</a><a href="/newsletter">Newsletter</a></div>
        <div class="footer__col"><h5>About</h5><a href="/about">About TrustLogix</a><a href="/newsroom">Newsroom</a><a href="/newsroom/press-releases">Press Releases</a><a href="/contact">Contact</a><a href="#">Cookie Preferences</a></div>
      </div>
      <div class="footer__divider"></div>
      <div class="footer__bottom">
        <span class="footer__credit">© 2026 TrustLogix. All rights reserved.</span>
        <div class="footer__legal"><a href="/privacy-policy">Privacy Policy</a><a href="/terms-of-service">Terms of Service</a><a href="/security-pledge">Security Pledge</a></div>
      </div>
    </div>
  </footer>

  <script src="{P}/script.js"></script>
  <script>(function(){{var nav=document.getElementById('nav');function onScroll(){{nav.classList.toggle('nav--solid',window.scrollY>20);}}window.addEventListener('scroll',onScroll,{{passive:true}});onScroll();}})();</script>
</body>
</html>'''

# Shared base styles for these pages (hero, section heads, cards) — token-driven
BASE_STYLE = '''  <style>
    .mp-hero { background: var(--eden); background-image:
        radial-gradient(circle at 12% 30%, rgba(8,170,195,.26), transparent 44%),
        radial-gradient(circle at 88% 15%, rgba(111,190,70,.18), transparent 40%),
        radial-gradient(circle at 55% 88%, rgba(8,170,195,.14), transparent 36%);
      color:#fff; position:relative; overflow:hidden; padding: calc(55px + 7rem) 0 5rem; text-align:center; }
    .mp-hero::before { content:""; position:absolute; inset:0; pointer-events:none; opacity:.07; background-image: radial-gradient(circle,#fff 1.2px,transparent 1.2px); background-size:24px 24px; }
    .mp-hero__inner { position:relative; z-index:2; max-width: 54rem; margin:0 auto; }
    .mp-badge { display:inline-flex; align-items:center; gap:.5rem; font-family:var(--font-heading); font-weight:700; font-size:.9rem; letter-spacing:.1em; text-transform:uppercase; background:rgba(255,255,255,.1); padding:.5rem 1rem; border-radius:20px; margin-bottom:1.25rem; color:#fff; }
    .mp-hero__title { font-family:var(--font-heading); font-weight:800; font-size:clamp(2.3rem,4vw,3.4rem); line-height:1.1; letter-spacing:-.02em; margin-bottom:1.25rem; }
    .mp-hero__title .grad { background:linear-gradient(120deg,#6fbe46,#23ad9c 50%,#08aac3); -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; }
    .mp-hero__desc { font-size:1.1rem; line-height:1.7; color:rgba(255,255,255,.85); margin-bottom:2rem; }
    .mp-hero__cta { display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; }
    .mp-btn-w { background:#fff; color:var(--eden); font-family:var(--font-heading); font-weight:700; padding:.9rem 2rem; border-radius:var(--r-btn); text-decoration:none; transition:transform .2s var(--ease); }
    .mp-btn-g { background:rgba(255,255,255,.1); color:#fff; border:1px solid rgba(255,255,255,.3); font-family:var(--font-heading); font-weight:700; padding:.9rem 2rem; border-radius:var(--r-btn); text-decoration:none; }
    .mp-btn-w:hover,.mp-btn-g:hover { transform:translateY(-2px); }
    .mp-sec { padding:5rem 0; }
    .mp-sec--alt { background:#f4f8f8; }
    .mp-eyebrow { font-family:var(--font-heading); font-weight:700; font-size:1rem; letter-spacing:.15em; text-transform:uppercase; color:var(--pine-green); margin-bottom:1rem; }
    .mp-h2 { font-family:var(--font-heading); font-weight:800; font-size:clamp(1.9rem,2.6vw,2.5rem); letter-spacing:-.02em; line-height:1.15; color:var(--neutral-darkest); margin-bottom:1rem; }
    .mp-h2 b { color:var(--pine-green); }
    .mp-lead { font-size:1.125rem; line-height:1.7; color:var(--neutral); max-width:52rem; }
    .mp-head { margin-bottom:2.5rem; }
    .mp-head--c { text-align:center; } .mp-head--c .mp-lead { margin:0 auto; }
'''

def doc(title, desc, extra_style, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | TrustLogix</title>
  <meta name="description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Roboto:wght@300;400;500;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{P}/styles.css?v=255" />
{BASE_STYLE}{extra_style}  </style>
</head>
<body>

{NAV}

  <main>
{body}
  </main>

{FOOTER}'''

# ───────────────────────── ABOUT ─────────────────────────
about_style = '''    .ab-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.25rem; margin-top:2.5rem; }
    .ab-card { background:#fff; border:1px solid #e5edee; border-radius:18px; padding:2rem; text-align:center; }
    .ab-card__img { width:88px; height:88px; border-radius:50%; object-fit:cover; margin:0 auto 1rem; display:block; border:3px solid #eaf4f3; }
    .ab-card h4 { font-family:var(--font-heading); font-weight:800; font-size:1.15rem; color:var(--neutral-darkest); margin-bottom:.5rem; }
    .ab-card p { font-size:1rem; line-height:1.65; color:var(--neutral); }
    .ab-people { display:grid; grid-template-columns:repeat(3,1fr); gap:1.25rem; margin-top:2.5rem; }
    .ab-person { background:#fff; border:1px solid #e5edee; border-radius:18px; padding:1.75rem; text-align:center; }
    .ab-person__img { width:120px; height:120px; border-radius:50%; object-fit:cover; margin:0 auto 1.1rem; display:block; border:3px solid #eaf4f3; }
    .ab-person__name { font-family:var(--font-heading); font-weight:800; font-size:1.1rem; color:var(--eden); }
    .ab-person__role { font-size:.95rem; color:var(--pine-green); font-weight:600; margin-top:.25rem; }
    .ab-invest { display:grid; grid-template-columns:repeat(4,1fr); gap:1.25rem; margin-top:2.5rem; }
    .ab-invest__item { background:#fff; border:1px solid #e5edee; border-radius:16px; padding:1.75rem; display:grid; place-items:center; min-height:110px; }
    .ab-invest__item img { max-width:160px; max-height:54px; width:auto; height:auto; object-fit:contain; }
    @media (max-width:860px){ .ab-grid,.ab-people{ grid-template-columns:1fr 1fr; } .ab-invest{ grid-template-columns:1fr 1fr; } }
'''
about_body = f'''    <section class="mp-hero">
      <div class="container mp-hero__inner">
        <span class="mp-badge">About TrustLogix</span>
        <h1 class="mp-hero__title">The Unified <span class="grad">Data Control Platform</span> for the Modern Data Stack</h1>
        <p class="mp-hero__desc">TrustLogix is the AI-powered platform for unified data control. It keeps access, protection, and compliance in sync across all clouds and data platforms—helping enterprises move faster and innovate safely.</p>
        <div class="mp-hero__cta"><a href="/careers" class="mp-btn-w">Explore Open Positions</a><a href="/platform" class="mp-btn-g">Our Platform</a></div>
      </div>
    </section>

    <section class="mp-sec">
      <div class="container">
        <div class="mp-head mp-head--c">
          <p class="mp-eyebrow">Our Mission</p>
          <h2 class="mp-h2">Securing the Data That <b>Drives AI</b></h2>
          <p class="mp-lead">As enterprises share data across multiple clouds and build Gen-AI applications, data security has never been harder. TrustLogix takes a no-proxy, high-performance approach—integrating policy-based access controls and data security posture management into a single platform. Our leadership previously founded Palerra, the industry's pioneering API-based CASB platform, which revolutionized how enterprises secure cloud services.</p>
        </div>
      </div>
    </section>

    <section class="mp-sec mp-sec--alt">
      <div class="container">
        <div class="mp-head mp-head--c"><p class="mp-eyebrow">Leadership</p><h2 class="mp-h2">The Team Behind <b>TrustLogix</b></h2></div>
        <div class="ab-people">
          <div class="ab-person"><img class="ab-person__img" src="{P}/logos/live/ron-longo.webp" alt="Ron Longo" /><div class="ab-person__name">Ron Longo</div><div class="ab-person__role">Chief Executive Officer</div></div>
          <div class="ab-person"><img class="ab-person__img" src="{P}/logos/live/ganesh-kirti.webp" alt="Ganesh Kirti" /><div class="ab-person__name">Ganesh Kirti</div><div class="ab-person__role">Founder, Board Chair &amp; CTO</div></div>
          <div class="ab-person"><img class="ab-person__img" src="{P}/logos/live/srikanth-sallaka.webp" alt="Srikanth Sallaka" /><div class="ab-person__name">Srikanth Sallaka</div><div class="ab-person__role">Co-Founder &amp; Head of Product</div></div>
        </div>
      </div>
    </section>

    <section class="mp-sec">
      <div class="container">
        <div class="mp-head mp-head--c"><p class="mp-eyebrow">Security Advisors</p><h2 class="mp-h2">Guided by <b>Enterprise CISOs</b></h2></div>
        <div class="ab-grid">
          <div class="ab-card"><img class="ab-card__img" src="{P}/logos/live/adv-steve-zalewski.webp" alt="Steve Zalewski" /><h4>Steve Zalewski</h4><p>Former CISO, Levi Strauss</p></div>
          <div class="ab-card"><img class="ab-card__img" src="{P}/logos/live/adv-mike-bass.webp" alt="Mike Bass" /><h4>Mike Bass</h4><p>Morgan Stanley</p></div>
          <div class="ab-card"><img class="ab-card__img" src="{P}/logos/live/adv-john-donovan.webp" alt="John Donovan" /><h4>John Donovan</h4><p>Former CISO, Malwarebytes</p></div>
          <div class="ab-card"><img class="ab-card__img" src="{P}/logos/live/adv-jerry-kowalski.webp" alt="Jerry Kowalski" /><h4>Jerry Kowalski</h4><p>CISO, Jefferies</p></div>
          <div class="ab-card"><img class="ab-card__img" src="{P}/logos/live/adv-alex-yampolskiy.webp" alt="Alex Yampolskiy" /><h4>Alex Yampolskiy</h4><p>Co-Founder &amp; CEO, SecurityScorecard</p></div>
        </div>
      </div>
    </section>

    <section class="mp-sec mp-sec--alt">
      <div class="container">
        <div class="mp-head mp-head--c"><p class="mp-eyebrow">Backed By</p><h2 class="mp-h2">Our <b>Investors</b></h2></div>
        <div class="ab-invest">
          <div class="ab-invest__item"><img src="{P}/logos/live/inv-norwest.webp" alt="Norwest Venture Partners" /></div>
          <div class="ab-invest__item"><img src="{P}/logos/live/inv-westwave.webp" alt="WestWave Capital" /></div>
          <div class="ab-invest__item"><img src="{P}/logos/live/inv-alter.webp" alt="Alter Global VC" /></div>
          <div class="ab-invest__item"><img src="{P}/logos/live/inv-thehive.webp" alt="The Hive" /></div>
        </div>
      </div>
    </section>

{cta(primary=('Explore Open Positions','/careers'))}'''

# ───────────────────────── PRICING ─────────────────────────
pricing_style = '''    .pr-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.25rem; margin-top:3rem; align-items:stretch; }
    .pr-card { background:#fff; border:1.5px solid #e5edee; border-radius:22px; padding:2.25rem; display:flex; flex-direction:column; }
    .pr-card--feature { border-color:transparent; background:linear-gradient(#fff,#fff) padding-box, linear-gradient(135deg,#6fbe46,#23ad9c 45%,#08aac3) border-box; box-shadow:var(--shadow-card); }
    .pr-card__name { font-family:var(--font-heading); font-weight:800; font-size:1.35rem; color:var(--eden); }
    .pr-card__tag { font-size:.9rem; color:var(--pine-green); font-weight:600; margin-top:.35rem; min-height:1.2rem; }
    .pr-card__price { font-family:var(--font-heading); font-weight:800; font-size:2.4rem; color:var(--neutral-darkest); margin:1.25rem 0 .25rem; }
    .pr-card__price span { font-size:1rem; font-weight:600; color:var(--neutral); }
    .pr-card__list { list-style:none; display:flex; flex-direction:column; gap:.7rem; margin:1.5rem 0; flex:1; }
    .pr-card__list li { position:relative; padding-left:1.7rem; font-size:.97rem; line-height:1.5; color:var(--neutral-darkest); }
    .pr-card__list li::before { content:""; position:absolute; left:0; top:.15rem; width:18px; height:18px; border-radius:50%; background:var(--mantis-lighter); }
    .pr-card__list li::after { content:""; position:absolute; left:5px; top:.4rem; width:8px; height:5px; border-left:2px solid var(--pine-green); border-bottom:2px solid var(--pine-green); transform:rotate(-45deg); }
    .pr-card .btn { width:100%; text-align:center; }
    .pr-metrics { display:grid; grid-template-columns:repeat(3,1fr); gap:1.25rem; margin-top:2.5rem; }
    .pr-metric { background:#fff; border:1px solid #e5edee; border-radius:18px; padding:1.75rem; text-align:center; }
    .pr-metric__num { font-family:var(--font-heading); font-weight:800; font-size:2.4rem; background:var(--grad-brand); -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; }
    .pr-metric__label { font-size:.95rem; color:var(--neutral); margin-top:.35rem; }
    .pr-faq { max-width:46rem; margin:0 auto; display:flex; flex-direction:column; gap:.75rem; }
    .pr-faq__item { border:1px solid #e5edee; border-radius:14px; background:#fff; padding:1.4rem 1.6rem; }
    .pr-faq__q { font-family:var(--font-heading); font-weight:700; font-size:1.05rem; color:var(--neutral-darkest); margin-bottom:.4rem; }
    .pr-faq__a { font-size:1rem; line-height:1.6; color:var(--neutral); }
    @media (max-width:900px){ .pr-grid,.pr-metrics{ grid-template-columns:1fr; } }
'''
pricing_body = f'''    <section class="mp-hero">
      <div class="container mp-hero__inner">
        <span class="mp-badge">Pricing</span>
        <h1 class="mp-hero__title">Pricing for <span class="grad">Enterprise-Grade</span> AI Data Security</h1>
        <p class="mp-hero__desc">No Proxies. No Agents. No Data Movement. Scale productivity across your entire data ecosystem with secure, compliant access in minutes—powered by AI-ready governance and seamless enterprise integration.</p>
        <div class="mp-hero__cta"><a href="/get-started" class="mp-btn-w">Get Started</a><a href="/get-started" class="mp-btn-g">Try Free Scanners</a></div>
      </div>
    </section>

    <section class="mp-sec">
      <div class="container">
        <div class="pr-grid">
          <div class="pr-card">
            <div class="pr-card__name">Proof of Concept</div>
            <div class="pr-card__tag">Free / 30 days</div>
            <div class="pr-card__price">Free</div>
            <ul class="pr-card__list">
              <li>1 Snowflake or Databricks warehouse of any size</li>
              <li>TrustDSPM, TrustAccess &amp; TrustAI</li>
              <li>Email support</li>
              <li>Activation &amp; implementation assistance</li>
              <li>Processes up to 30 days of recent historical data</li>
            </ul>
            <a href="/get-started" class="btn btn--outline">Start Free POC</a>
          </div>
          <div class="pr-card pr-card--feature">
            <div class="pr-card__name">Departmental</div>
            <div class="pr-card__tag">Proven ROI in &lt; 6 months</div>
            <div class="pr-card__price">$50k<span>/year</span></div>
            <ul class="pr-card__list">
              <li>1 Snowflake or Databricks warehouse of any size</li>
              <li>TrustDSPM, TrustAccess &amp; TrustAI</li>
              <li>24/7 support</li>
              <li>Integrates with IAM, SIEM &amp; collaboration tools (Slack, Teams)</li>
              <li>Activation &amp; implementation assistance</li>
              <li>Available on AWS &amp; Snowflake Marketplace</li>
            </ul>
            <a href="/get-started" class="btn btn--primary">Get Started</a>
          </div>
          <div class="pr-card">
            <div class="pr-card__name">Enterprise</div>
            <div class="pr-card__tag">Custom contracts &amp; terms</div>
            <div class="pr-card__price">Custom</div>
            <ul class="pr-card__list">
              <li>All Departmental features</li>
              <li>Unlimited warehouses</li>
              <li>On-premise database support</li>
              <li>Multi-cloud and multi-region</li>
              <li>Deploy the Trustlet (data plane) in your cloud</li>
              <li>Bring your own key (BYOK)</li>
              <li>Design partnership opportunities</li>
            </ul>
            <a href="/contact" class="btn btn--outline">Get a Custom Quote</a>
          </div>
        </div>
      </div>
    </section>

    <section class="mp-sec mp-sec--alt">
      <div class="container">
        <div class="mp-head mp-head--c"><p class="mp-eyebrow">The TrustLogix Difference</p><h2 class="mp-h2">Measurable Outcomes, <b>From Day One</b></h2></div>
        <div class="pr-metrics">
          <div class="pr-metric"><div class="pr-metric__num">85%</div><div class="pr-metric__label">Faster setup &amp; onboarding</div></div>
          <div class="pr-metric"><div class="pr-metric__num">100%</div><div class="pr-metric__label">AI agent activity monitoring</div></div>
          <div class="pr-metric"><div class="pr-metric__num">40+ hrs</div><div class="pr-metric__label">Saved per month on audit readiness</div></div>
          <div class="pr-metric"><div class="pr-metric__num">73%</div><div class="pr-metric__label">Data risk reduction</div></div>
          <div class="pr-metric"><div class="pr-metric__num">60%</div><div class="pr-metric__label">Cost savings</div></div>
          <div class="pr-metric"><div class="pr-metric__num">75%</div><div class="pr-metric__label">Faster access requests</div></div>
        </div>
      </div>
    </section>

    <section class="mp-sec">
      <div class="container">
        <div class="mp-head mp-head--c"><p class="mp-eyebrow">Pricing FAQs</p><h2 class="mp-h2">Questions, <b>Answered</b></h2></div>
        <div class="pr-faq">
          <div class="pr-faq__item"><div class="pr-faq__q">How quickly can we activate the platform?</div><div class="pr-faq__a">You can activate TrustLogix in 1–2 hours.</div></div>
          <div class="pr-faq__item"><div class="pr-faq__q">Does TrustLogix store or see my data?</div><div class="pr-faq__a">No. TrustLogix is metadata-only, so it doesn't store or see your data.</div></div>
          <div class="pr-faq__item"><div class="pr-faq__q">Do you charge per user or by data used?</div><div class="pr-faq__a">No—we do not charge per user or by the amount of data you use.</div></div>
          <div class="pr-faq__item"><div class="pr-faq__q">How does the ROI compare to proxy-based tools?</div><div class="pr-faq__a">Deploy in under 2 hours versus 4–8 weeks, with no proxies or agents, 70% lower implementation cost, 2–4× faster time-to-value, and typical payback in under 6 months.</div></div>
        </div>
      </div>
    </section>

{cta(primary=('Get Started','/get-started'))}'''

# ───────────────────────── GET STARTED ─────────────────────────
gs_style = '''    .gs-wrap { display:grid; grid-template-columns:1.1fr .9fr; gap:3.5rem; align-items:start; }
    .gs-form { background:#fff; border:1px solid #e5edee; border-radius:22px; padding:2.5rem; box-shadow:var(--shadow-card); }
    .gs-form h3 { font-family:var(--font-heading); font-weight:800; font-size:1.4rem; color:var(--eden); margin-bottom:.4rem; }
    .gs-form p { font-size:1rem; color:var(--neutral); margin-bottom:1.5rem; }
    .gs-field { margin-bottom:1.1rem; }
    .gs-field label { display:block; font-family:var(--font-heading); font-weight:600; font-size:.85rem; color:var(--neutral-darkest); margin-bottom:.4rem; }
    .gs-field input, .gs-field select { width:100%; border:1px solid #d8d9d9; border-radius:8px; padding:.8rem 1rem; font-family:var(--font-body); font-size:1rem; color:var(--neutral-darkest); }
    .gs-field input:focus, .gs-field select:focus { outline:none; border-color:var(--pine-green); }
    .gs-form .btn { width:100%; text-align:center; margin-top:.5rem; }
    .gs-points { list-style:none; display:flex; flex-direction:column; gap:1.25rem; margin-top:1.5rem; }
    .gs-points li { display:flex; gap:1rem; align-items:flex-start; }
    .gs-points__ic { flex:none; width:36px; height:36px; border-radius:10px; background:var(--eden); display:grid; place-items:center; color:#fff; font-weight:800; font-family:var(--font-heading); }
    .gs-points__t { font-family:var(--font-heading); font-weight:700; color:var(--neutral-darkest); }
    .gs-points__d { font-size:.97rem; color:var(--neutral); line-height:1.55; }
    .gs-testi { background:#f4f8f8; border-left:4px solid var(--pine-green); border-radius:12px; padding:1.5rem 1.75rem; margin-top:2rem; }
    .gs-testi p { font-family:var(--font-heading); font-weight:600; font-size:1.05rem; color:var(--eden); line-height:1.5; }
    .gs-testi span { display:block; font-size:.9rem; color:var(--neutral); margin-top:.75rem; font-style:italic; }
    @media (max-width:860px){ .gs-wrap{ grid-template-columns:1fr; } }
'''
gs_body = f'''    <section class="mp-hero">
      <div class="container mp-hero__inner">
        <span class="mp-badge">Get Started</span>
        <h1 class="mp-hero__title">Unlock Your <span class="grad">Data Security Potential</span> Today</h1>
        <p class="mp-hero__desc">Getting started with TrustLogix is fast and easy. Activate in just a few minutes and start seeing data sprawl and activity dashboards in just two hours. No long implementation, no change to your existing data stack, no proxies or agents. Just data insight and control.</p>
      </div>
    </section>

    <section class="mp-sec">
      <div class="container gs-wrap">
        <div>
          <p class="mp-eyebrow">Schedule a Call</p>
          <h2 class="mp-h2">Meet With a <b>Product Expert</b></h2>
          <p class="mp-lead">See how TrustLogix can help you gain control over your data, across your entire data stack.</p>
          <ul class="gs-points">
            <li><span class="gs-points__ic">1</span><div><div class="gs-points__t">Activate in minutes</div><div class="gs-points__d">No proxies, no agents, no changes to your existing data or stack.</div></div></li>
            <li><span class="gs-points__ic">2</span><div><div class="gs-points__t">Dashboards in two hours</div><div class="gs-points__d">See data sprawl and activity dashboards the same day you start.</div></div></li>
            <li><span class="gs-points__ic">3</span><div><div class="gs-points__t">Insight and control</div><div class="gs-points__d">Role- and attribute-based access plus dynamic masking, out of the box.</div></div></li>
          </ul>
          <div class="gs-testi">
            <p>"Snowflake offered ease of use, enhanced performance, and key insights, while TrustLogix quickly integrated, providing role and attribute-based access and dynamic masking to help us build robust security in our highly regulated industry."</p>
            <span>— Bhaskar Mulugu, Head of Enterprise Architecture &amp; Enterprise Data Platform, Vialto Partners</span>
          </div>
        </div>
        <form class="gs-form" onsubmit="return false;">
          <h3>Schedule a Call</h3>
          <p>Tell us a bit about you and we'll be in touch.</p>
          <div class="gs-field"><label>Full name</label><input type="text" placeholder="Jane Doe" /></div>
          <div class="gs-field"><label>Work email</label><input type="email" placeholder="jane@company.com" /></div>
          <div class="gs-field"><label>Company</label><input type="text" placeholder="Company name" /></div>
          <div class="gs-field"><label>Primary data platform</label><select><option>Snowflake</option><option>Databricks</option><option>AWS (Redshift / S3 / RDS)</option><option>Power BI</option><option>Other</option></select></div>
          <button class="btn btn--primary">Schedule a Call</button>
        </form>
      </div>
    </section>

    <section class="mp-sec mp-sec--alt">
      <div class="container">
        <div class="mp-head mp-head--c"><p class="mp-eyebrow">Getting Started FAQs</p><h2 class="mp-h2">Everything You Need to <b>Begin</b></h2></div>
        <div class="pr-faq" style="max-width:46rem;margin:0 auto;display:flex;flex-direction:column;gap:.75rem;">
          <div class="gs-testi" style="border-left:0;background:#fff;border:1px solid #e5edee;"><p style="font-weight:700;">How does the startup process work?</p><span style="font-style:normal;color:var(--neutral);">Activate in minutes and see dashboards within two hours—no proxies, agents, or data-stack changes.</span></div>
          <div class="gs-testi" style="border-left:0;background:#fff;border:1px solid #e5edee;"><p style="font-weight:700;">What's included?</p><span style="font-style:normal;color:var(--neutral);">TrustDSPM, TrustAccess, and TrustAI, with activation and implementation assistance.</span></div>
          <div class="gs-testi" style="border-left:0;background:#fff;border:1px solid #e5edee;"><p style="font-weight:700;">Is training and support available?</p><span style="font-style:normal;color:var(--neutral);">Yes—email support on the POC, and 24/7 support on paid plans.</span></div>
        </div>
      </div>
    </section>

{cta(primary=('Schedule a Call','/get-started'))}'''

# ───────────────────────── CONTACT ─────────────────────────
contact_style = '''    .ct-wrap { display:grid; grid-template-columns:1fr 1fr; gap:3.5rem; align-items:start; }
    .ct-card { background:#f4f8f8; border:1px solid #e5edee; border-radius:18px; padding:1.75rem; margin-bottom:1.25rem; }
    .ct-card h4 { font-family:var(--font-heading); font-weight:800; font-size:1.1rem; color:var(--eden); margin-bottom:.4rem; }
    .ct-card p, .ct-card a { font-size:1rem; color:var(--neutral); line-height:1.6; text-decoration:none; }
    .ct-card a { color:var(--pine-green); font-weight:600; }
    @media (max-width:860px){ .ct-wrap{ grid-template-columns:1fr; } }
'''
contact_body = f'''    <section class="mp-hero">
      <div class="container mp-hero__inner">
        <span class="mp-badge">Contact</span>
        <h1 class="mp-hero__title">Let's <span class="grad">Talk Data Security</span></h1>
        <p class="mp-hero__desc">Whether you're exploring the platform, evaluating a proof of concept, or have a question for our team—we'd love to hear from you.</p>
      </div>
    </section>

    <section class="mp-sec">
      <div class="container ct-wrap">
        <div>
          <p class="mp-eyebrow">Reach Us</p>
          <h2 class="mp-h2">How Can We <b>Help?</b></h2>
          <div class="ct-card"><h4>Talk to Sales</h4><p>See the platform in action and explore a proof of concept in your own environment.</p><a href="/get-started">Schedule a Call →</a></div>
          <div class="ct-card"><h4>Partnerships</h4><p>Join the TrustLogix Interoperable Ecosystem as a technology or services partner.</p><a href="/partners">Partner With Us →</a></div>
          <div class="ct-card"><h4>Support &amp; Documentation</h4><p>Existing customer? Find product guides and technical documentation.</p><a href="https://docs.trustlogix.io/">View Documentation →</a></div>
        </div>
        <form class="gs-form" onsubmit="return false;">
          <h3>Send Us a Message</h3>
          <p>We'll route your note to the right team and respond quickly.</p>
          <div class="gs-field"><label>Full name</label><input type="text" placeholder="Jane Doe" /></div>
          <div class="gs-field"><label>Work email</label><input type="email" placeholder="jane@company.com" /></div>
          <div class="gs-field"><label>Company</label><input type="text" placeholder="Company name" /></div>
          <div class="gs-field"><label>How can we help?</label><select><option>Request a demo</option><option>Start a proof of concept</option><option>Partnership inquiry</option><option>Customer support</option><option>Other</option></select></div>
          <button class="btn btn--primary">Send Message</button>
        </form>
      </div>
    </section>

{cta(primary=('Get Started','/get-started'))}'''

# ───────────────────────── RESOURCES ─────────────────────────
res_style = '''    .rl-filters { display:flex; flex-wrap:wrap; gap:.65rem; margin-top:2rem; }
    .rl-filter { font-family:var(--font-heading); font-weight:600; font-size:.9rem; background:#fff; border:1px solid #e5edee; padding:.55rem 1.2rem; border-radius:99px; color:var(--neutral-darkest); cursor:pointer; }
    .rl-filter.is-active { background:var(--eden); color:#fff; border-color:var(--eden); }
    .rl-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; margin-top:2.5rem; }
    .rl-card { background:#fff; border:1px solid #e5edee; border-radius:18px; overflow:hidden; display:flex; flex-direction:column; transition:transform .25s var(--ease), box-shadow .25s var(--ease); }
    .rl-card:hover { transform:translateY(-5px); box-shadow:var(--shadow-card); }
    .rl-card__thumb { height:160px; background:linear-gradient(135deg,#0c3f41,#08aac3); position:relative; }
    .rl-card__thumb::before { content:""; position:absolute; inset:0; opacity:.12; background-image:radial-gradient(circle,#fff 1.2px,transparent 1.2px); background-size:20px 20px; }
    .rl-card__type { position:absolute; top:1rem; left:1rem; font-family:var(--font-heading); font-weight:700; font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; background:#fff; color:var(--pine-green); padding:.35rem .8rem; border-radius:99px; }
    .rl-card__body { padding:1.5rem; display:flex; flex-direction:column; flex:1; }
    .rl-card__title { font-family:var(--font-heading); font-weight:700; font-size:1.05rem; line-height:1.4; color:var(--neutral-darkest); margin-bottom:.75rem; }
    .rl-card__date { font-size:.85rem; color:var(--neutral); margin-top:auto; }
    @media (max-width:900px){ .rl-grid{ grid-template-columns:1fr; } }
'''
RES = [
    ('Case Study','Securing a Modern Data Mesh in the Snowflake Data Cloud','May 31, 2024'),
    ('Data Sheet','Why Security Teams Are Replacing IBM Guardium with TrustLogix','Apr 17, 2026'),
    ('Data Sheet','Solution Brief: Preemptive Data Security for the Age of AI Agents','Jan 12, 2026'),
    ('Ebook','Data Security for Agentic AI','Dec 4, 2025'),
    ('Report','Use Agile, Adaptive, AI-Ready (3A) Data Security Governance to Secure Shadow AI — Gartner','Apr 13, 2026'),
    ('Report',"AI Agents Are Your New Blind Spot: A CISO's Framework for Governing Agentic AI — GigaOm",'Mar 16, 2026'),
    ('Video','Securing Your AI Agents Before They Become Your Biggest Liability','Mar 3, 2026'),
    ('Video','Building the Policy Control Plane: The Architecture Behind TrustAI','Feb 23, 2026'),
    ('Webinar','Self-Service Analytics Without the Chaos: Governing Insights at Scale','May 11, 2026'),
]
res_cards = '\n'.join(f'''          <a class="rl-card" href="/resource-library">
            <div class="rl-card__thumb"><span class="rl-card__type">{t}</span></div>
            <div class="rl-card__body"><div class="rl-card__title">{title}</div><div class="rl-card__date">{date}</div></div>
          </a>''' for (t,title,date) in RES)
res_body = f'''    <section class="mp-hero">
      <div class="container mp-hero__inner">
        <span class="mp-badge">Resource Library</span>
        <h1 class="mp-hero__title">Insights for the <span class="grad">Age of AI-Ready</span> Data Access</h1>
        <p class="mp-hero__desc">Unlock innovation with our latest insights and thought leadership—case studies, data sheets, eBooks, analyst reports, videos, and webinars.</p>
      </div>
    </section>

    <section class="mp-sec">
      <div class="container">
        <div class="mp-head"><p class="mp-eyebrow">Featured Resources</p><h2 class="mp-h2">Browse the <b>Library</b></h2>
          <div class="rl-filters">
            <span class="rl-filter is-active">All</span><span class="rl-filter">Case Studies</span><span class="rl-filter">Data Sheets</span><span class="rl-filter">eBooks</span><span class="rl-filter">Reports</span><span class="rl-filter">Videos</span><span class="rl-filter">Webinars</span>
          </div>
        </div>
        <div class="rl-grid">
{res_cards}
        </div>
      </div>
    </section>

{cta(primary=('Get Started','/get-started'))}'''

PAGES = [
  ('about/index.html','About TrustLogix — The Unified Data Control Platform','Learn about TrustLogix, the AI-powered platform for unified data control across clouds and data platforms.', about_style, about_body),
  ('pricing/index.html','Pricing — Enterprise-Grade AI Data Security','TrustLogix pricing: free POC, Departmental, and Enterprise plans. No proxies, no agents, no data movement.', pricing_style, pricing_body),
  ('get-started/index.html','Get Started — Activate in Minutes','Get started with TrustLogix: activate in minutes and see data sprawl and activity dashboards in two hours.', gs_style, gs_body),
  ('contact/index.html','Contact TrustLogix','Contact the TrustLogix team — sales, partnerships, and support.', contact_style, contact_body),
  ('resources/index.html','Resource Library — TrustLogix','Case studies, data sheets, eBooks, reports, videos, and webinars on AI-ready data access and data security.', res_style, res_body),
]

base = os.path.dirname(os.path.abspath(__file__))
for path, title, desc, style, body in PAGES:
    full = os.path.join(base, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(doc(title, desc, style, body))
    print('wrote', path)
