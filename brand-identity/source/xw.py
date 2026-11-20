# Direction A base (lead) — "Warm editorial": one type family (Geist, tight display), warm canvas, ink type, cobalt only for primary.
XW = r"""
:root { --font-brand: 'Bricolage Grotesque', ui-sans-serif, system-ui, sans-serif; --warm: #f7f7f8; --warm-edge: rgba(16,20,38,.09); }
/* display type: Geist 700, tight tracking, everywhere Bricolage used to be */
.t-display, .t-h1, .t-h2, .hero-num, .w-big, .n-pc .n-pt, .n-he b, .n-rw b, .xm1-h, .xm3-nm, .xz-ptop .ttl, h1, h2 { font-family: 'Bricolage Grotesque', ui-sans-serif, system-ui, sans-serif !important; font-weight: 650 !important; letter-spacing: -0.02em !important; }
.t-h3, .sec h2 + p { letter-spacing: -0.01em; }
/* app screens: warm canvas, white cards, warm hairline */
.phone .scr[data-theme="light"]:not(:has(.xm1-wel)) { background: var(--warm) !important; }
.phone .scr .body { background: transparent !important; }
.phone .scr[data-theme="light"] :is(.card, .row, .xm3-grp, .panel) { border-color: var(--warm-edge) !important; }
.phone .scr[data-theme="light"] .tabbar { background: rgba(247,247,248,.94) !important; border-top: 1px solid var(--warm-edge) !important; }
.phone .topbar { background: transparent !important; }
.phone .scr[data-theme="dark"] { background: #0f1014 !important; } .phone .scr[data-theme="dark"] .tabbar { background: rgba(15,16,20,.96) !important; border-top: 1px solid rgba(255,255,255,.08) !important; } .phone .scr[data-theme="dark"] .ttl, .phone .scr[data-theme="dark"] h1 { color: #fff !important; }

/* home indicator strip + bottom bars inherit the screen surface (was a white band under warm screens) */
.phone .scr[data-theme="light"] .home-ind { background: transparent !important; }
.phone .scr[data-theme="light"] :is(.bbar, .xm2-bar, .xy-bar, .botbar, .sticky-bottom) { background: var(--warm) !important; }
.phone .scr[data-theme="light"]:has(.tabbar) .home-ind { background: rgba(247,247,248,.94) !important; }
"""
