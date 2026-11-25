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
/* campaign page (.xq-cp) */
:root:root:root .phone .xq-cp .ph { height: 196px; }
:root:root:root .phone .xq-cp .sh { padding: 20px 20px 0; gap: 20px; overflow: hidden; }
:root:root:root .phone .xq-cp .cp-head { display: grid; grid-template-columns: auto 1fr; align-items: center; column-gap: 10px; }
:root:root:root .phone .xq-cp .cp-store { display: inline-flex; align-items: center; gap: 6px; height: 28px; padding: 0 10px 0 6px; border-radius: 14px; background: var(--hd-surface); box-shadow: inset 0 0 0 1px var(--hd-edge); font-size: 13px; font-weight: 560; }
:root:root:root .phone .xq-cp .cp-head .by { margin: 0; font-size: 13.5px; }
:root:root:root .phone .xq-cp .cp-head .xm1-t { grid-column: 1 / -1; margin-top: 12px; }
:root:root:root .phone .xq-cp .cp-close { grid-column: 1 / -1; margin: 4px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
:root:root:root .phone .xq-cp .cp-close b { color: var(--hd-fg); font-weight: 560; }
:root:root:root .phone .xq-cp .cp-calc { border-radius: 16px; box-shadow: inset 0 0 0 1px var(--hd-edge); padding: 4px 16px 12px; }
:root:root:root .phone .xq-cp .cp-calc .r { display: flex; justify-content: space-between; align-items: baseline; height: 36px; align-items: center; font-size: 15px; }
:root:root:root .phone .xq-cp .cp-calc .r span { color: var(--hd-fg-muted); }
:root:root:root .phone .xq-cp .cp-calc .r em { font-style: normal; font-size: 13px; margin-left: 6px; color: var(--hd-fg-subtle, var(--hd-fg-muted)); }
:root:root:root .phone .xq-cp .cp-calc .r b { font-weight: 600; }
:root:root:root .phone .xq-cp .cp-calc .r.tot { height: 52px; margin-top: 4px; border-top: 1px solid var(--hd-edge); }
:root:root:root .phone .xq-cp .cp-calc .r.tot span { color: var(--hd-fg); font-weight: 600; }
:root:root:root .phone .xq-cp .cp-calc .r.tot b { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; }
:root:root:root .phone .xq-cp .cp-calc small { display: block; font-size: 13px; color: var(--hd-fg-muted); text-align: right; }
:root:root:root .phone .xq-cp .cp-sec h2 { margin: 0 0 12px; font-size: 17px; line-height: 22px; font-weight: 600; }
:root:root:root .phone .xq-cp .cp-steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
:root:root:root .phone .xq-cp .cp-st { display: flex; flex-direction: column; gap: 8px; font-size: 13.5px; line-height: 18px; font-weight: 520; letter-spacing: -0.005em; }
:root:root:root .phone .xq-cp .cp-st i { font-style: normal; width: 24px; height: 24px; border-radius: 12px; display: grid; place-items: center; font-size: 13px; font-family: 'Geist', sans-serif; font-weight: 600; box-shadow: inset 0 0 0 1px var(--hd-edge); color: var(--hd-fg-muted); }
:root:root:root .phone .xq-cp .cp-task { display: flex; gap: 12px; align-items: center; min-height: 64px; padding: 10px 14px; border-radius: 16px; box-shadow: inset 0 0 0 1px var(--hd-edge); margin-bottom: 8px; }
:root:root:root .phone .xq-cp .cp-task .tx b { display: block; font-size: 15px; line-height: 20px; font-weight: 600; }
:root:root:root .phone .xq-cp .cp-task .tx small { display: block; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
:root:root:root .phone .xq-cp .cp-dd { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; font-size: 14px; line-height: 20px; }
:root:root:root .phone .xq-cp .cp-dd b { font-weight: 600; } :root:root:root .phone .xq-cp .cp-dd p { margin: 6px 0 0; color: var(--hd-fg-muted); }
:root:root:root .phone .xq-cp .cp-bar { flex: none; padding: 10px 20px 8px; background: var(--hd-surface); border-top: 1px solid var(--hd-edge); display: flex; flex-direction: column; gap: 8px; align-items: stretch; position: relative; z-index: 2; }
:root:root:root .phone .xq-cp .cp-bar small { text-align: center; font-size: 13px; color: var(--hd-fg-muted); }
:root:root:root .phone .xq-cp .cp-bar .btn { height: 48px !important; }
:root:root:root .phone .xq-cp .cp-bar::before { content: ''; position: absolute; left: 0; right: 0; bottom: 100%; height: 36px; background: linear-gradient(180deg, rgba(255,255,255,0), #fff); pointer-events: none; }
:root:root:root .phone .xq-cp .cp-st { display: grid; justify-items: start; align-content: start; gap: 8px; } :root:root:root .phone .xq-cp .cp-st span { display: block; }
:root:root:root .phone .xq-cp .ph > img { object-position: 50% 100%; }

/* lead: lead with "You get back" (the selling point); cost becomes the quiet footer */
:root:root:root .phone .xq-cp .cp2 { padding: 14px 16px 0 !important; }
:root:root:root .phone .xq-cp .cp2 .hd { display: flex; flex-direction: column; gap: 2px; padding-bottom: 10px; border-bottom: 1px solid var(--hd-edge); margin-bottom: 4px; }
:root:root:root .phone .xq-cp .cp2 .hd span { font-size: 13.5px; color: var(--hd-fg-muted); font-weight: 500; }
:root:root:root .phone .xq-cp .cp2 .hd b { font-family: var(--font-brand); font-size: 34px; line-height: 38px; font-weight: 700; letter-spacing: -0.025em; color: var(--hd-fg); }
:root:root:root .phone .xq-cp .cp2 .hd small { font-size: 12.5px; color: var(--hd-fg-muted); text-align: left; }
:root:root:root .phone .xq-cp .cp2 .r { height: 34px; font-size: 14.5px; }
:root:root:root .phone .xq-cp .cp2 .ft { display: flex; justify-content: space-between; gap: 8px; margin: 6px -16px 0; padding: 10px 16px; border-top: 1px solid var(--hd-edge); font-size: 13px; color: var(--hd-fg-muted); }
:root:root:root .phone .xq-cp .cp2 .ft b { color: var(--hd-fg); font-weight: 600; }
/* readable clock over the photo */
:root:root:root .phone .xq-cp .ph::before { content: ''; position: absolute; left: 0; right: 0; top: 0; height: 90px; background: linear-gradient(180deg, rgba(255,255,255,.72), rgba(255,255,255,0)); z-index: 1; pointer-events: none; }
:root:root:root .phone .xq-cp .ph .tb { z-index: 2; }

/* campaign v3: shorter photo so tasks show, connected steps, split bottom bar */
:root:root:root .phone .xq-cp .ph { height: 150px !important; }
:root:root:root .phone .xq-cp .cp-steps { position: relative; }
:root:root:root .phone .xq-cp .cp-steps::before { content: ''; position: absolute; left: 12px; right: calc(33.3% - 12px); top: 12px; height: 1px; background: var(--hd-edge); z-index: 0; }
:root:root:root .phone .xq-cp .cp-st i { position: relative; z-index: 1; background: var(--hd-surface, #fff); }
:root:root:root .phone .xq-cp .cp-sec { margin-top: 18px !important; }
:root:root:root .phone .xq-cp .cp-bar2 { display: flex !important; flex-direction: row !important; align-items: center; gap: 12px; }
:root:root:root .phone .xq-cp .cp-bar2 .l { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 1px; }
:root:root:root .phone .xq-cp .cp-bar2 .l b { font-family: var(--font-brand); font-size: 20px; line-height: 24px; font-weight: 700; letter-spacing: -.02em; }
:root:root:root .phone .xq-cp .cp-bar2 .l small { font-size: 12.5px; color: var(--hd-fg-muted); }
:root:root:root .phone .xq-cp .cp-bar2 .btn { flex: none; width: auto !important; padding: 0 22px !important; }
"""
