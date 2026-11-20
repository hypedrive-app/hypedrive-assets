# final pass layer 1 (mobile screens)
XQ1 = r"""
/* R1: one surface — top bar, tab bar, bottom action bar and home indicator are all the screen's own white (no grey strips) */
:root:root .phone .scr[data-theme="light"] :is(.xm1-bar, .cta, .xm3-cta, .tabbar, .home-ind) { background: var(--hd-surface) !important; }
:root:root .phone .scr[data-theme="light"] .xm1-bar { border-top: 0 !important; }
/* welcome: the mosaic dissolves under the status bar so the logo sits on dark */
:root:root:root:root .phone .xm1-wel .xm1-fade { background: linear-gradient(180deg, #0d0e12 0px, rgba(13,14,18,.82) 48px, rgba(13,14,18,.38) 92px, rgba(13,14,18,0) 140px, rgba(13,14,18,0) 250px, rgba(13,14,18,.86) 400px, #0d0e12 480px) !important; }
/* empty search: chips wrap inside the margins instead of running off the edge */
:root:root .phone .xm3-chips { flex-wrap: wrap; margin-right: 0; white-space: normal; }
/* detail: photo dots read on a bright photo */
:root:root .phone .xm1-det .x-dots i { background: rgba(255,255,255,.9); box-shadow: 0 0 0 1px rgba(16,20,38,.22); }
/* apply: the radio is the selection signal; no tint behind the chosen card */
:root:root:root:root .scr:has(.xm2m[data-s=apply]) .xm2-c.on { background: var(--hd-surface); border-color: var(--hd-edge); }
:root:root:root:root .scr:has(.xm2m[data-s=apply]) .xm2-c { min-height: 60px; }
/* success: title on the 28 scale */
:root:root:root:root h1.xm3-h { font-size: 28px; line-height: 32px; }
/* detail: the three facts share one baseline (the small "days / of 120" no longer stretches its line) */
:root:root:root:root .phone .xm1-facts b { height: 22px; overflow: visible; } :root:root:root:root .phone .xm1-facts b i { line-height: 0; }
/* wallet: the sparkline end dot keeps its white gap but loses the tinted halo */
:root:root:root:root .phone .spk-dot { box-shadow: 0 0 0 2px var(--hd-surface); }
/* verify: the six cells span exactly the content width, so the first box lines up with the title */
:root:root:root:root .phone .xm1-code { justify-content: space-between; gap: 0; }
"""
