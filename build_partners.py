#!/usr/bin/env python3
"""Generate the per-partner detail (inner / dropdown sub) pages.
THEME: white — follows /platform/trustdspm (light mint gradient hero + hero-bg diamonds +
green glow + gradient keyword + SOLID nav with dark logo). Content + images faithful to
trustlogix.ai/partners/<slug>. All six partners (incl. Snowflake) are generated from this one
template so they stay uniform."""
import html, os

NAV = '''  <header class="nav" id="nav">
    <div class="nav__inner">
      <a href="/" class="nav__logo" aria-label="TrustLogix home">
        <img src="../../trustlogix-logo.svg" alt="TrustLogix" class="nav__logo-img" width="200" height="34" />
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

STYLE = '''  <style>
    /* ─── Partner detail page — WHITE theme, hero matches /platform/trustdspm exactly ─── */
    .pn-hero { position:relative; padding:7rem 0 4rem; text-align:center; overflow:hidden;
      background-image:url("../../hero-bg.svg"), linear-gradient(#fff,#f4faf8 60%,#eaf4f3 101%);
      background-position:50% 0,0 0; background-size:70px,auto; background-repeat:repeat,no-repeat; color:var(--neutral-darkest); }
    .pn-hero__glow { position:absolute; width:600px; height:600px; bottom:-130px; left:-250px; background-image:radial-gradient(circle closest-side,rgba(111,190,70,.28),transparent); pointer-events:none; }
    .pn-hero__glow2 { position:absolute; width:520px; height:520px; top:-160px; right:-180px; background-image:radial-gradient(circle closest-side,rgba(8,170,195,.18),transparent); pointer-events:none; }
    .pn-hero__inner { position:relative; z-index:2; max-width:56rem; margin:0 auto; }
    .pn-badge { display:inline-flex; align-items:center; gap:.5rem; font-family:var(--font-heading); font-weight:700; font-size:.85rem; letter-spacing:.12em; text-transform:uppercase; color:var(--pine-green); background:rgba(0,115,115,.08); padding:.5rem 1rem; border-radius:99px; margin-bottom:1.25rem; }
    .pn-badge b { color:var(--mantis); }
    .pn-lockup { display:inline-flex; align-items:center; gap:1rem; margin-bottom:1.5rem; }
    .pn-lockup img { height:34px; width:auto; display:block; }
    .pn-lockup .pn-lockup__partner { height:38px; }
    .pn-lockup__plus { font-family:var(--font-heading); font-weight:400; font-size:1.6rem; color:var(--neutral-lighter); line-height:1; }
    .pn-hero__title { font-family:var(--font-heading); font-weight:400; font-size:clamp(2.2rem,4vw,3.5rem); line-height:1.2; letter-spacing:-.01em; margin-bottom:1.5rem; color:var(--neutral-darkest); }
    .pn-hero__title .grad { font-weight:700; background:var(--grad-brand); -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; }
    .pn-hero__desc { font-size:1rem; line-height:1.6; color:var(--neutral); max-width:46.5rem; margin:0 auto 2.4rem; }
    .pn-hero__cta { display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; }
    .pn-hero__badge-row { display:flex; gap:.75rem; margin-top:1.75rem; flex-wrap:wrap; justify-content:center; }
    .pn-hero__badge-row img { height:60px; width:auto; }
    .pn-hero__graphic { width:100%; max-width:80rem; margin:3.5rem auto 0; border-radius:20px; overflow:hidden; box-shadow:2px 6px 20px rgba(0,0,0,.13); border:1px solid rgba(0,6,6,.04); }
    .pn-hero__graphic img { display:block; width:100%; height:auto; border-radius:20px; }

    .pn-sec { padding:5rem 0; }
    .pn-sec--alt { background:#f4f8f8; }
    .pn-eyebrow { font-family:var(--font-heading); font-weight:700; font-size:1rem; letter-spacing:.15em; text-transform:uppercase; color:var(--pine-green); margin-bottom:1rem; }
    .pn-h2 { font-family:var(--font-heading); font-weight:800; font-size:clamp(1.9rem,2.6vw,2.5rem); letter-spacing:-.02em; line-height:1.15; color:var(--neutral-darkest); margin-bottom:1rem; }
    .pn-h2 b { color:var(--pine-green); }
    .pn-lead { font-size:1.125rem; line-height:1.7; color:var(--neutral); max-width:52rem; }
    .pn-head { margin-bottom:2.5rem; }

    .pn-why { display:grid; grid-template-columns:repeat(2,1fr); gap:1rem; margin-top:2.5rem; }
    .pn-why__item { display:flex; gap:1rem; align-items:flex-start; background:#fff; border:1px solid #e5edee; border-radius:16px; padding:1.4rem 1.6rem; }
    .pn-why__check { flex:none; width:28px; height:28px; border-radius:50%; background:var(--grad-brand); display:grid; place-items:center; }
    .pn-why__check svg { width:16px; height:16px; color:#fff; }
    .pn-why__text { font-size:1rem; line-height:1.6; color:var(--neutral-darkest); }
    @media (max-width:760px){ .pn-why{ grid-template-columns:1fr; } }

    .pn-value { background:linear-gradient(110deg,#08aac3 0%,#23ad9c 48%,#6fbe46 100%); position:relative; overflow:hidden; }
    .pn-value::before { content:""; position:absolute; inset:0; opacity:.26; background-image:radial-gradient(circle,#fff 1.2px,transparent 1.2px); background-size:24px 24px; }
    .pn-value__card { position:relative; z-index:1; background:#fff; border-radius:24px; padding:3.5rem; text-align:center; box-shadow:0 24px 60px rgba(12,63,65,.12); max-width:60rem; margin:0 auto; }
    .pn-value__logo { height:42px; width:auto; margin:0 auto 1.25rem; display:block; }
    .pn-value__title { font-family:var(--font-heading); font-weight:800; font-size:clamp(1.6rem,2.4vw,2.25rem); letter-spacing:-.02em; color:var(--eden); margin-bottom:1rem; }
    .pn-value__sub { font-size:1.05rem; line-height:1.7; color:var(--neutral); margin-bottom:2rem; }
    .pn-value__cta { display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; }

    /* module split — matches /platform/trustdspm .dspm-split exactly */
    .pn-mod { display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:center; }
    .pn-mod + .pn-mod { margin-top:4.5rem; }
    .pn-mod--rev .pn-mod__text { order:2; }
    .pn-mod--rev .pn-mod__img { order:1; }
    .pn-mod__tag { display:inline-flex; align-items:center; gap:.5rem; font-family:var(--font-heading); font-weight:700; font-size:.78rem; letter-spacing:.1em; text-transform:uppercase; color:var(--pine-green); background:rgba(0,115,115,.08); padding:.45rem .9rem; border-radius:99px; margin-bottom:1rem; }
    .pn-mod__title { font-family:var(--font-heading); font-weight:400; font-size:40px; line-height:1.15; letter-spacing:-.02em; color:var(--neutral-darkest); margin-bottom:1rem; }
    .pn-mod__title b { font-weight:800; }
    .pn-mod__body { font-size:1.05rem; line-height:1.7; color:var(--neutral); margin-bottom:1.25rem; }
    .pn-mod__list { list-style:none; display:flex; flex-direction:column; gap:.7rem; }
    .pn-mod__list li { position:relative; padding-left:1.85rem; font-size:1rem; line-height:1.55; color:var(--neutral-darkest); }
    .pn-mod__list li::before { content:""; position:absolute; left:0; top:.3rem; width:18px; height:18px; border-radius:50%; background:var(--mantis-lighter); }
    .pn-mod__list li::after { content:""; position:absolute; left:5px; top:.55rem; width:8px; height:5px; border-left:2px solid var(--pine-green); border-bottom:2px solid var(--pine-green); transform:rotate(-45deg); }
    .pn-mod__img { position:relative; padding:32px; border-radius:24px; overflow:hidden; background:linear-gradient(110deg,#08aac3 0%,#23ad9c 48%,#6fbe46 100%); box-shadow:0 20px 50px rgba(12,63,65,.16); }
    .pn-mod__img::before { content:""; position:absolute; inset:0; pointer-events:none; opacity:.28; background-image:radial-gradient(circle,#fff 1.2px,transparent 1.2px); background-size:24px 24px; }
    .pn-mod__img img { position:relative; z-index:1; display:block; width:100%; height:auto; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,.18); }
    @media (max-width:860px){ .pn-mod{ grid-template-columns:1fr; gap:2rem; } .pn-mod--rev .pn-mod__text,.pn-mod--rev .pn-mod__img{ order:0; } }

    .pn-testi { background:var(--eden); color:#fff; position:relative; overflow:hidden; }
    .pn-testi::before { content:""; position:absolute; inset:0; opacity:.06; background-image:radial-gradient(circle,#fff 1.2px,transparent 1.2px); background-size:24px 24px; }
    .pn-testi__inner { position:relative; z-index:1; max-width:56rem; margin:0 auto; text-align:center; }
    .pn-testi__mark { font-family:var(--font-heading); font-weight:800; font-size:4rem; line-height:.6; color:rgba(255,255,255,.18); }
    .pn-testi__text { font-family:var(--font-heading); font-weight:600; font-size:clamp(1.3rem,2vw,1.75rem); line-height:1.5; letter-spacing:-.01em; margin:1rem 0 1.5rem; }
    .pn-testi__text b { color:var(--mantis); }
    .pn-testi__attr { font-size:1rem; color:rgba(255,255,255,.7); font-family:var(--font-heading); font-weight:700; letter-spacing:.04em; text-transform:uppercase; }
  </style>'''

CTA_FOOTER = '''    <section class="cta-final">
      <div class="cta-final__card reveal">
        <div class="cta-final__bg"></div>
        <img class="cta-final__graphic" src="../../logos/cta-bg-graphic.svg" alt="" aria-hidden="true" />
        <div class="cta-final__content">
          <div class="cta-final__left"><h2 class="cta-final__title">Experience TrustLogix in Action</h2></div>
          <div class="cta-final__right">
            <p class="cta-final__sub">Schedule a call to discover how TrustLogix can accelerate your AI initiatives with faster, safer data access.</p>
            <div class="cta-final__buttons">
              <a href="/get-started" class="btn cta-final__btn cta-final__btn--primary"><span class="btn__swap"><span>Get Started</span><span aria-hidden="true">Get Started</span></span></a>
              <a href="/platform" class="btn cta-final__btn cta-final__btn--secondary"><span class="btn__swap"><span>Our Platform</span><span aria-hidden="true">Our Platform</span></span></a>
            </div>
          </div>
        </div>
      </div>
      <div class="cta-final__strip"></div>
    </section>
  </main>

  <footer class="footer footer--brand footer--light">
    <div class="container">
      <div class="footer__top">
        <a href="/" class="footer__logo" aria-label="TrustLogix"><img src="../../trustlogix-logo.svg" alt="TrustLogix" width="180" height="31" /></a>
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

  <script src="../../script.js"></script>
  <script>(function(){var nav=document.getElementById('nav');function onScroll(){nav.classList.toggle('nav--solid',window.scrollY>20);}window.addEventListener('scroll',onScroll,{passive:true});onScroll();})();</script>
</body>
</html>'''

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 13l4 4L19 7"/></svg>'

def why_items(items):
    return '\n'.join(f'          <div class="pn-why__item"><span class="pn-why__check">{CHECK}</span><span class="pn-why__text">{html.escape(t)}</span></div>' for t in items)

# Partner brand logo used in the hero lockup + value band (snowflake uses a crisp SVG wordmark)
LOGO = {
    'snowflake': 'logos/live/logo-snowflake.svg',
    'databricks': 'logos/eco/databricks.png',
    'microsoft': 'logos/eco/power-bi.png',
    'aws': 'logos/eco/aws.png',
    'alation': 'logos/eco/alation.png',
    'collibra': 'logos/eco/collibra.png',
}

PNG_MODS = {('snowflake', 1)}  # (slug, 0-based module index) whose downloaded image is .png

def modules(mods, slug):
    out = []
    for i, m in enumerate(mods):
        rev = ' pn-mod--rev' if i % 2 == 1 else ''
        bullets = '\n'.join(f'              <li>{html.escape(b)}</li>' for b in m['bullets'])
        ext = 'png' if (slug, i) in PNG_MODS else 'webp'
        imgfile = f'mod-{slug}-{i+1}.{ext}'
        img = f'<div class="pn-mod__img"><img src="../../logos/live/{imgfile}" alt="{html.escape(m["tag"])} for {slug.title()}" loading="lazy" /></div>'
        text = f'''          <div class="pn-mod__text">
            <span class="pn-mod__tag">{html.escape(m['tag'])}</span>
            <h3 class="pn-mod__title">{html.escape(m['title'])}</h3>
            <p class="pn-mod__body">{html.escape(m['body'])}</p>
            <ul class="pn-mod__list">
{bullets}
            </ul>
          </div>'''
        inner = (img + '\n' + text) if rev else (text + '\n          ' + img)
        out.append(f'        <div class="pn-mod{rev}">\n          {inner}\n        </div>')
    return '\n\n'.join(out)

def value_band(v):
    cta = '\n'.join(f'            <a href="{href}" class="btn {cls}">{html.escape(label)}</a>' for (label, href, cls) in v['cta'])
    logo = f'\n          <img class="pn-value__logo" src="../../{v["logo"]}" alt="" />' if v.get('logo') else ''
    return f'''    <section class="pn-sec pn-value">
      <div class="container">
        <div class="pn-value__card">{logo}
          <h2 class="pn-value__title">{html.escape(v['title'])}</h2>
          <p class="pn-value__sub">{html.escape(v['sub'])}</p>
          <div class="pn-value__cta">
{cta}
          </div>
        </div>
      </div>
    </section>

'''

def page(p):
    badge_row = ''
    if p.get('badges'):
        imgs = '\n'.join(f'            <img src="../../logos/live/{b}" alt="badge" />' for b in p['badges'])
        badge_row = f'\n          <div class="pn-hero__badge-row">\n{imgs}\n          </div>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(p['title_tag'])} | TrustLogix</title>
  <meta name="description" content="{html.escape(p['desc'])}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Roboto:wght@300;400;500;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../styles.css?v=255" />
{STYLE}
</head>
<body>

{NAV}

  <main>
    <section class="pn-hero">
      <div class="pn-hero__glow"></div><div class="pn-hero__glow2"></div>
      <div class="container pn-hero__inner">
        <div class="pn-lockup">
          <img src="../../trustlogix-logo.svg" alt="TrustLogix" />
          <span class="pn-lockup__plus">+</span>
          <img class="pn-lockup__partner" src="../../{LOGO[p['slug']]}" alt="{html.escape(p['partner'])}" />
        </div>
        <h1 class="pn-hero__title">{p['headline_html']}</h1>
        <p class="pn-hero__desc">{html.escape(p['subhead'])}</p>{badge_row}
      </div>
      <div class="container">
        <div class="pn-hero__graphic"><img src="../../logos/live/hero-{p['slug']}.webp" alt="TrustLogix for {html.escape(p['partner'])} — architecture diagram" /></div>
      </div>
    </section>

    <section class="pn-sec">
      <div class="container">
        <div class="pn-head">
          <p class="pn-eyebrow">{html.escape(p['why_eyebrow'])}</p>
          <h2 class="pn-h2">{p['why_h2_html']}</h2>
        </div>
        <div class="pn-why">
{why_items(p['why'])}
        </div>
      </div>
    </section>

{value_band(p['value']) if p.get('value') else ''}    <section class="pn-sec pn-sec--alt">
      <div class="container">
        <div class="pn-head" style="text-align:center;">
          <p class="pn-eyebrow">One Platform, Three Modules</p>
          <h2 class="pn-h2">{p['mod_h2_html']}</h2>
        </div>
{modules(p['modules'], p['slug'])}
      </div>
    </section>

    <section class="pn-sec pn-testi">
      <div class="container pn-testi__inner">
        <div class="pn-testi__mark">&ldquo;</div>
        <p class="pn-testi__text">{p['testi_html']}</p>
        <p class="pn-testi__attr">— {html.escape(p['testi_attr'])}</p>
      </div>
    </section>

{CTA_FOOTER}'''

PARTNERS = [
  {
    'slug':'snowflake','partner':'Snowflake','eco_logo':'snowflake.png','hero_img':'snowflake-hero.webp',
    'badges':['snowflake-horizon-badge.webp'],
    'title_tag':'TrustLogix + Snowflake — Extend Snowflake Security',
    'desc':'TrustLogix integrates natively with Snowflake to unify access control, share real-time risk insights, and secure AI-driven data use including Snowflake Cortex AI.',
    'headline_html':'Extend <span class="grad">Snowflake Security</span> Across Your Entire Data Ecosystem',
    'subhead':"TrustLogix integrates natively with Snowflake to strengthen and unify access control, share real-time risk insights, and secure AI-driven data use—including support for Snowflake Cortex AI. As part of the Snowflake Horizon architecture and as a Snowflake Trust Center partner, TrustLogix extends consistent protections across Databricks, AWS, and Power BI—so you can eliminate blind spots and control access at scale.",
    'why_eyebrow':'Why Snowflake Customers Use TrustLogix',
    'why_h2_html':"Snowflake secures your data. <b>TrustLogix secures how it's accessed.</b>",
    'why':[
      'Extend Snowflake access control with fine-grained policies across multiple Snowflake accounts and the broader data ecosystem.',
      "Gain real-time visibility into who's accessing what, with continuous monitoring from day one.",
      'Control AI access with identity- and purpose-based policies for Snowflake Cortex AI.',
      'Activate instantly and run natively without performance impact.',
      'Start with one account and scale easily with flexible, account-based pricing.',
      'Integrate natively with Snowflake Horizon with only 2–5% performance overhead, even at petabyte scale.',
    ],
    'value':{'title':'Available in the Snowflake Marketplace','sub':'Get the Trust Center Data Security Scanner from Snowflake Marketplace—or use your Snowflake credits for our private offer.',
             'logo':'logos/live/logo-snowflake.svg',
             'cta':[('Snowflake Marketplace','/get-started','btn--primary'),('Private Offer','/get-started','btn--outline')]},
    'mod_h2_html':'Unified Security for Snowflake <b>and the Ecosystem Around It</b>',
    'modules':[
      {'tag':'TrustDSPM','title':'Access Monitoring in Snowflake—And the Ecosystem Around It','body':'Data security posture management that continuously monitors data access to help you detect risk early, prioritize remediation, and stay audit-ready.',
       'bullets':['Map sensitive data and monitor usage patterns, access anomalies, and policy drift in real time.','Surface over-permissioned users, unused entitlements, and overlapping roles to ensure least-privilege access.','Integrate with Snowflake Trust Center to enrich risk signals and accelerate issue resolution.','Support HIPAA, GDPR, and data residency requirements for continuous compliance.']},
      {'tag':'TrustAccess','title':'Policy-Based Access Control for Snowflake and Beyond','body':'Enforce consistent, least-privileged access across Snowflake accounts, teams, and environments—without proxies, added infrastructure, or touching the data.',
       'bullets':['Define fine-grained access policies for dynamic scenarios such as managerial hierarchy or cost center.','Unify access management across Snowflake and all connected data environments.','Eliminate Snowflake RBAC sprawl with intuitive, no-code policy creation.','Integrate natively with Snowflake Horizon with only 2–5% performance overhead at petabyte scale.']},
      {'tag':'TrustAI','title':'Secure Enablement for AI Projects in Snowflake','body':'Support AI agents and analytics use cases with identity- and context-aware governance.',
       'bullets':['Enforce just-in-time, purpose-based access for Cortex AI agents so every query aligns with approved objectives.','Maintain full visibility and auditability of AI data access across accounts and workloads.','Prevent data overexposure as AI expands into sensitive or cross-border data.','Extend secure, governed AI access to external models, applications, and ML platforms.']},
    ],
    'testi_html':'By centralizing access controls and visibility across 100+ Snowflake data products, a global telecom provider achieved <b>50% faster data product rollout</b> and a <b>30% boost in productivity</b>—while strengthening regulatory compliance.',
    'testi_attr':'Global Telecom Provider',
  },
  {
    'slug':'databricks','partner':'Databricks','eco_logo':'databricks.png','hero_img':'databricks-hero.webp',
    'badges':['databricks-validated-badge.webp'],
    'title_tag':'TrustLogix + Databricks — Beyond Unity Catalog',
    'desc':"TrustLogix integrates natively with Databricks to deliver access control and AI/ML governance that Unity Catalog alone doesn't provide.",
    'headline_html':'Beyond Unity Catalog: <span class="grad">Enforce Access Policies</span> Across Databricks and More',
    'subhead':"TrustLogix integrates natively with Databricks to deliver capabilities that Unity Catalog alone doesn't provide—a central control plane across accounts, workspaces, jobs, notebooks, pipelines, and feature stores; securing AI/ML workflows with scoped, just-in-time entitlements; and extending visibility and policy control across your entire data ecosystem.",
    'why_eyebrow':'Why Customers Use TrustLogix',
    'why_h2_html':"Databricks powers your lakehouse. <b>TrustLogix governs how it's accessed.</b>",
    'why':[
      'Enforce access control across Unity Catalog, workspaces, and downstream tools.',
      'Unify visibility into entitlements, activity, and risk across human and non-human identities.',
      'Extend protection to AI/ML jobs, pipelines, and shared data assets.',
      'Deploy natively—no proxy or agent architecture to manage.',
      'Start small and scale fast with account-based pricing and fast activation.',
    ],
    'mod_h2_html':'Governance That Scales Across <b>Workspaces, Regions, and AI</b>',
    'modules':[
      {'tag':'TrustDSPM','title':'Turn Access Inventory into Actionable Risk Insights','body':"Understand not just what data exists, but how it's being used, who's accessing it—and where the risks are.",
       'bullets':['Map entitlements, usage, and data flows from notebooks into BI tools across workspaces.','Detect and remediate excessive permissions, unused roles, and overlapping access patterns.','Surface dark data, configuration gaps, and policy drift and prioritize fixes by business impact.','Ensure continuous compliance with built-in support for HIPAA, PCI-DSS, and internal data boundaries.']},
      {'tag':'TrustAccess','title':'Policy-Based Access Controls for the Lakehouse','body':'Go beyond Unity Catalog roles with access policies that scale across workspaces, regions, and the entire Databricks environment.',
       'bullets':['Enforce least-privilege access across jobs, notebooks, pipelines, and environments.','Apply consistent controls across workspaces and cloud regions to eliminate policy silos.','Support dynamic policy conditions like purpose, geography, or project alignment.','Manage access for non-human identities including jobs, service principals, and pipelines.','Avoid custom code with no-code policy creation and native integration.']},
      {'tag':'TrustAI','title':'Secure Enablement for AI/ML Workflows','body':'Empower data science teams to move faster—without sacrificing governance.',
       'bullets':['Provide just-in-time, scoped access for ML jobs, notebooks, and feature stores.','Deliver entitlements to Mosaic AI agents based on identity and intent.','Protect sensitive features in the Databricks Feature Store across training and inference.','Maintain auditability for dynamic access requests and agent-driven workflows.','Govern data flowing into and out of Databricks-native and external AI platforms.']},
    ],
    'testi_html':'A Fortune 500 healthcare company implemented TrustLogix to govern access across Databricks and Snowflake—<b>cutting access provisioning time by 50%</b>, audit prep time by 25%, and reducing the risk of HIPAA/GDPR violations.',
    'testi_attr':'Global Healthcare Provider',
  },
  {
    'slug':'microsoft','partner':'Power BI','eco_logo':'power-bi.png','hero_img':'powerbi-hero.webp',
    'title_tag':'TrustLogix + Power BI — Close the Governance Gap',
    'desc':'TrustLogix extends policy-based security into Power BI with native integration for consistent access enforcement and compliant self-service analytics.',
    'headline_html':'Close the Governance Gap from <span class="grad">Cloud Data Platforms</span> to Power BI',
    'subhead':'When sensitive data moves into Power BI, access controls from platforms like Snowflake and Databricks are often left behind—creating gaps in governance and exposing data to risk. TrustLogix extends policy-based security into Power BI with native integration, enabling consistent access enforcement, enterprise-grade risk visibility, and compliant self-service analytics at scale.',
    'why_eyebrow':'Why Power BI Customers Rely on TrustLogix',
    'why_h2_html':'Consistent governance <b>from source to dashboard.</b>',
    'why':[
      'Direct integration with Power BI—no agents, proxies, or custom connectors required.',
      'Fine-grained access policies from source to dashboard.',
      'Enterprise-grade DSPM for risk detection and access visibility.',
      'Built-in compliance controls for HIPAA, GDPR, PCI-DSS, and more.',
      'Account-based pricing for flexible adoption.',
      'Fast time-to-value—see analytics and enforcement in minutes, not weeks.',
    ],
    'mod_h2_html':'Extend Source-Level Policy <b>Into Your BI Layer</b>',
    'modules':[
      {'tag':'TrustDSPM','title':'Monitor Risks Across Your BI Environment','body':'Monitor access risks and policy violations before they escalate into incidents.',
       'bullets':['Detect dark data, over-privileged access, and misconfigurations in Power BI.','Correlate access activity with data movement from source platforms to spot policy gaps.','Visualize exposure risks and enable privacy-aware sharing across dashboards.','Identify unused roles and enforce least-privileged access across all user types.','Eliminate blind spots across multi-cloud environments.']},
      {'tag':'TrustAccess','title':'Enforce Access Policies Inside Power BI','body':'Keep access controls aligned from source to visualization—no custom connectors or proxies required.',
       'bullets':['Carry forward access policies from Snowflake, Databricks, and other platforms.','Define fine-grained, no-code policies based on business context, geography, and user role.','Enable fast, self-service access to dashboards—even when they contain sensitive data.','Empower data owners to manage policies directly through federated controls.','Deploy in hours, not weeks—with the only native Power BI integration available.']},
    ],
    'testi_html':'TrustLogix closed the visibility and policy-enforcement gap between Power BI and upstream data sources by <b>automatically extending source-level policies into Power BI</b>, restoring consistent governance without added complexity.',
    'testi_attr':'Fortune 100 Healthcare Distributor',
  },
  {
    'slug':'aws','partner':'AWS','eco_logo':'aws.png','hero_img':'aws-hero.webp',
    'title_tag':'TrustLogix + AWS — Unified Data Security for Redshift, S3 & RDS',
    'desc':'TrustLogix brings centralized governance and identity-aware policy enforcement to Amazon Redshift, S3, and RDS.',
    'headline_html':'Unified Data Security Across <span class="grad">Amazon Redshift, S3, and RDS</span>',
    'subhead':"TrustLogix brings centralized governance and identity-aware policy enforcement to your AWS data services. Whether you're storing structured data in Redshift, unstructured files in S3, or transactional records in RDS, TrustLogix delivers fine-grained access control, visibility, and compliance without slowing down performance.",
    'why_eyebrow':'Why Customers Choose TrustLogix',
    'why_h2_html':'One control plane <b>across every AWS data service.</b>',
    'why':[
      'One unified control plane for access policies across Redshift, S3, RDS, and beyond.',
      'Real-time visibility into entitlements, activity, and risks—no agents required.',
      'No-code policy creation that works with your existing IAM model.',
      'Fast to deploy, easy to scale—see insights within minutes.',
      'Account-based pricing for flexible adoption across business units.',
    ],
    'mod_h2_html':'Fine-Grained Control <b>Across Redshift, S3, and RDS</b>',
    'modules':[
      {'tag':'Amazon Redshift','title':'Secure Analytics at Scale','body':'Bring least-privileged, business-aware access governance to your Redshift analytics.',
       'bullets':['Enforce least-privileged access by user, role, or job function.','Align data access with business context and compliance requirements.','Monitor usage patterns to detect and remediate risky or unused entitlements.','Centralize policy governance across Redshift and other AWS services.','Avoid manual IAM configurations with no-code policy creation.']},
      {'tag':'Amazon S3','title':'Control Access to Unstructured Data','body':'Govern object storage with policies that reflect business context, not just bucket roles.',
       'bullets':['Monitor access to unstructured data across buckets and services.','Visualize data access patterns and policy violations in real time.','Define and enforce policies reflecting business context, not just bucket-level roles.','Reduce reliance on complex IAM and bucket-policy configurations.','Govern S3 alongside Redshift, RDS, and downstream analytics tools.']},
      {'tag':'Amazon RDS','title':'Visibility into Who Accesses What—and Why','body':'Bring database access into a centralized, auditable governance model.',
       'bullets':['Track access by identity, time, and purpose.','Identify excessive or unnecessary entitlements to reduce risk.','Enforce policy-based controls without altering RDS operations.','Bring database access into a centralized governance model.','Support security, audit, and compliance requirements.']},
    ],
    'testi_html':'A leading financial institution used TrustLogix to unify governance across Redshift, RDS, S3, and Snowflake—<b>reducing time-to-value for secure data access from days to minutes</b> while eliminating policy drift and manual audits.',
    'testi_attr':'Fortune 500 Investment Bank',
  },
  {
    'slug':'alation','partner':'Alation','eco_logo':'alation.png','hero_img':'alation-hero.webp',
    'title_tag':'TrustLogix + Alation — Turn Data Intelligence into Enforced Policy',
    'desc':'Alation defines how data should be governed. TrustLogix makes sure those rules are enforced as real-time access controls.',
    'headline_html':'Turn <span class="grad">Data Intelligence</span> into Enforced Policy',
    'subhead':'Alation defines how data should be governed. TrustLogix makes sure those rules are enforced—turning trusted metadata into real-time access controls and secure data usage across platforms like Snowflake, Databricks, and Power BI.',
    'why_eyebrow':'Why Use This Integration',
    'why_h2_html':'From <b>defined governance</b> to <b>enforced policy.</b>',
    'why':[
      'Enforce catalog policies across platforms in real time.',
      'Reduce risk and policy drift with unified governance.',
      'Automate compliance for HIPAA, GDPR, DORA, and more.',
      'Maximize catalog value with fast, no-code deployment.',
    ],
    'mod_h2_html':'Make <b>Alation Metadata</b> Actionable Everywhere',
    'modules':[
      {'tag':'TrustAccess','title':'Enforce Access from Your Catalog','body':'Make Alation metadata actionable across your environment.',
       'bullets':['Use classifications, ownership, and purpose tags to drive no-code access policies.','Apply rules across Snowflake, Databricks, Redshift, Power BI, and more.','Empower stewards to manage policies while reducing over-permissioning and delays.']},
      {'tag':'TrustDSPM','title':'Align Risk Detection with Governance Intent','body':'Bridge the gap between policy definition and real-world access.',
       'bullets':['Correlate access activity with catalog metadata to expose misalignment.','Detect overlapping roles, excessive access, and drift from defined policies.','Prioritize remediation using sensitivity context from Alation.']},
      {'tag':'TrustAI','title':'Govern AI Access with Trusted Metadata','body':'Extend Alation-defined policies into AI and ML workflows.',
       'bullets':['Enforce entitlements based on use case, sensitivity, and geography.','Apply masking and row-level controls across catalogued datasets.','Monitor how AI tools interact with sensitive data across platforms.']},
    ],
    'testi_html':'TrustLogix runs on top of Snowflake out of band, consuming only metadata without accessing the data. With a <b>single pane of glass</b>, policies are applied automatically—providing real-time protection without manual deployment.',
    'testi_attr':'Seth Youssef, Security Field CTO, Snowflake',
  },
  {
    'slug':'collibra','partner':'Collibra','eco_logo':'collibra.png','hero_img':'collibra-hero.webp',
    'title_tag':'TrustLogix + Collibra — Enforce the Governance You Define',
    'desc':'Collibra helps you establish trusted governance policies. TrustLogix turns those into real-time access controls and secure data usage.',
    'headline_html':'Enforce the <span class="grad">Governance You Define</span>',
    'subhead':'Collibra helps organizations establish trusted governance policies and data definitions. TrustLogix turns those into real-time access controls, risk visibility, and secure data usage across your cloud and analytics platforms.',
    'why_eyebrow':'Why Collibra Customers Need TrustLogix',
    'why_h2_html':'Turn <b>governance policy</b> into <b>real-time enforcement.</b>',
    'why':[
      'Transform metadata and Collibra-defined rules into real-time enforcement across platforms.',
      'Detect and fix access risks that catalog tools alone cannot surface.',
      'Automate compliance with frameworks like GDPR, HIPAA, and DORA.',
      'Speed up secure access for analytics and AI by removing governance bottlenecks.',
      'Get started fast with native integrations and no-code deployment.',
    ],
    'mod_h2_html':'Operationalize <b>Collibra Governance</b> End to End',
    'modules':[
      {'tag':'TrustAccess','title':'Operationalize Collibra Governance Policies','body':'Turn Collibra metadata into dynamic, no-code access policies.',
       'bullets':['Turn Collibra metadata into dynamic, no-code access policies.','Apply identity-aware controls across Snowflake, Databricks, Power BI, and more.','Empower data stewards to manage policies with business context.','Accelerate access to governed data by eliminating manual approvals and provisioning delays.']},
      {'tag':'TrustDSPM','title':'Connect Catalog Intelligence to Risk Detection','body':'Monitor how governed data is actually used—and uncover where policies break down.',
       'bullets':['Correlate metadata with usage to detect excessive access and policy drift.','Identify overlapping roles, unused entitlements, and misconfigurations.','Prioritize remediation based on sensitivity and business impact.']},
      {'tag':'TrustAI','title':'Secure AI Use with Policy-Aware Governance','body':'Apply Collibra-defined rules across AI and ML workflows.',
       'bullets':['Apply Collibra-defined rules to control AI access by identity, geography, and purpose.','Enforce masking and row-level filters across AI-generated outputs.','Maintain auditability as AI pipelines scale and evolve.','Align AI data access with internal policy and external compliance.']},
    ],
    'testi_html':'Healthcare AI without governance is a non-starter—and <b>TrustLogix lets us innovate with AI while staying compliant.</b>',
    'testi_attr':'VP, IT, Healthcare and Biotech — Gartner Peer Insights™',
  },
]

base = os.path.dirname(os.path.abspath(__file__))
for p in PARTNERS:
    out_dir = os.path.join(base, 'partners', p['slug'])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.html'), 'w') as f:
        f.write(page(p))
    print('wrote', p['slug'])
