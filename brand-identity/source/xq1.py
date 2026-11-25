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
:root:root:root .phone .xq-cp .cp-st i { font-style: normal; width: 24px; height: 24px; border-radius: 12px; display: grid; place-items: center; font-size: 13px; font-family: var(--font-ui); font-weight: 600; box-shadow: inset 0 0 0 1px var(--hd-edge); color: var(--hd-fg-muted); }
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

/* ===== campaign v4: system-level richness (full-bleed hero, offer chips, payout bar, icon-tile steps, task tiles) ===== */
:root:root:root .phone .c4 { display: flex; flex-direction: column; height: 100%; background: var(--hd-surface, #fff); }
:root:root:root .phone .c4 .c4-hero { position: relative; height: 280px; flex: none; overflow: hidden; }
:root:root:root .phone .c4 .c4-hero > img { width: 100%; height: 100%; object-fit: cover; object-position: 50% 60%; display: block; }
:root:root:root .phone .c4 .c4-hero::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,10,16,.34) 0%, rgba(8,10,16,0) 26%, rgba(8,10,16,0) 46%, rgba(8,10,16,.74) 100%); pointer-events: none; }
:root:root:root .phone .c4 .c4-hero .tb { position: absolute; top: 52px; left: 16px; right: 16px; display: flex; justify-content: space-between; z-index: 2; }
:root:root:root .phone .c4 .c4-hb { position: absolute; left: 16px; right: 16px; bottom: 14px; z-index: 2; color: #fff; display: flex; flex-direction: column; gap: 4px; }
:root:root:root .phone .c4 .c4-hb h1 { margin: 2px 0 0; font: 700 28px/32px var(--font-brand); letter-spacing: -.02em; color: #fff; }
:root:root:root .phone .c4 .c4-hb p { margin: 0; font-size: 13.5px; color: rgba(255,255,255,.86); }
:root:root:root .phone .c4 .c4-store { align-self: flex-start; display: inline-flex; align-items: center; gap: 6px; height: 26px; padding: 0 10px 0 6px; border-radius: 999px; background: #fff; color: #16181d; font-size: 12.5px; font-weight: 600; box-shadow: 0 1px 2px rgba(0,0,0,.18); }
:root:root:root .phone .c4 .c4-store img { border-radius: 4px; }
:root:root:root .phone .c4 .c4-body { flex: 1; min-height: 0; overflow: hidden; padding: 14px 16px 0; display: flex; flex-direction: column; }
:root:root:root .phone .c4 .c4-brand { display: flex; align-items: center; gap: 8px; font-size: 14px; } .phone .c4 .c4-brand .sp { flex: 1; }
:root:root:root .phone .c4 .c4-lt { width: 28px !important; height: 28px !important; border-radius: 8px !important; display: grid !important; place-items: center; } .phone .c4 .c4-lt b { font-size: 11px; font-weight: 700; color: #7a5200; }
:root:root:root .phone .c4 .c4-chip { display: inline-flex; align-items: center; gap: 5px; height: 26px; padding: 0 9px; border-radius: 8px; font-size: 12.5px; font-weight: 600; }
:root:root:root .phone .c4 .c4-chip.ok { background: var(--hd-success-subtle); color: var(--hd-success-strong); } .phone .c4 .c4-chip.ok svg { color: var(--hd-success, #0a8a4a); }
:root:root:root .phone .c4 .c4-chip.info { background: var(--hd-accent-subtle); color: var(--hd-accent-strong, var(--hd-link)); }
:root:root:root .phone .c4 .c4-chip.warn { background: var(--hd-warning-subtle); color: var(--hd-warning-strong); }
:root:root:root .phone .c4 .c4-offer { display: flex; gap: 6px; margin-top: 10px; }
:root:root:root .phone .c4 .c4-pay { margin-top: 12px; padding: 14px 16px 10px; border-radius: 16px; background: #fff; box-shadow: 0 0 0 1px var(--hd-edge), 0 1px 2px rgba(16,20,38,.05), 0 4px 12px -6px rgba(16,20,38,.10); }
:root:root:root .phone .c4 .c4-pay .hd { display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; }
:root:root:root .phone .c4 .c4-pay .hd span { width: 100%; font-size: 13px; color: var(--hd-fg-muted); font-weight: 500; }
:root:root:root .phone .c4 .c4-pay .hd b { font: 700 34px/38px var(--font-brand); letter-spacing: -.025em; }
:root:root:root .phone .c4 .c4-pay .hd small { font-size: 12.5px; color: var(--hd-fg-muted); }
:root:root:root .phone .c4 .c4-bar { margin-top: 10px; height: 8px; border-radius: 4px; background: var(--hd-track, rgba(16,20,38,.10)); overflow: hidden; } .phone .c4 .c4-bar i { display: block; height: 100%; background: var(--hd-accent); border-radius: 4px; }
:root:root:root .phone .c4 .c4-leg { display: flex; gap: 12px; margin-top: 8px; font-size: 12.5px; color: var(--hd-fg-muted); flex-wrap: wrap; } .phone .c4 .c4-leg b { color: var(--hd-fg); font-weight: 600; }
:root:root:root .phone .c4 .c4-leg i { display: inline-block; width: 8px; height: 8px; border-radius: 2px; margin-right: 5px; vertical-align: 0; } .phone .c4 .c4-leg i.b { background: var(--hd-accent); } .phone .c4 .c4-leg i.c { background: var(--hd-track-strong, #d5d7de); }
:root:root:root .phone .c4 .c4-leg .t { margin-left: auto; }
:root:root:root .phone .c4 .c4-br { display: flex; justify-content: space-between; font-size: 13.5px; color: var(--hd-fg-muted); padding-top: 8px; margin-top: 8px; border-top: 1px solid var(--hd-edge); } .phone .c4 .c4-br + .c4-br { border-top: 0; margin-top: 0; padding-top: 4px; } .phone .c4 .c4-br b { color: var(--hd-fg); font-weight: 600; }
:root:root:root .phone .c4 .c4-h { margin: 18px 0 8px; font: 650 16px/20px var(--font-brand); letter-spacing: -.01em; }
:root:root:root .phone .c4 .c4-steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
:root:root:root .phone .c4 .c4-st { display: flex; flex-direction: column; gap: 2px; padding: 10px; border-radius: 14px; background: #fff; box-shadow: 0 0 0 1px var(--hd-edge); }
:root:root:root .phone .c4 .c4-st b { margin-top: 6px; font-size: 13.5px; font-weight: 600; } .phone .c4 .c4-st small { font-size: 12.5px; color: var(--hd-fg-muted); }
:root:root:root .phone .c4 .c4-ti { width: 36px !important; height: 36px !important; border-radius: 10px !important; display: grid !important; place-items: center; color: var(--hd-accent); }
:root:root:root .phone .c4 .c4-task { display: flex; gap: 12px; align-items: flex-start; padding: 12px; border-radius: 14px; background: #fff; box-shadow: 0 0 0 1px var(--hd-edge); margin-bottom: 8px; }
:root:root:root .phone .c4 .c4-task .tx b { display: block; font-size: 14.5px; font-weight: 600; } .phone .c4 .c4-task .tx small { display: block; font-size: 13px; color: var(--hd-fg-muted); margin-top: 1px; }
:root:root:root .phone .c4 .c4-req { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 8px; } .phone .c4 .c4-req span { height: 22px; padding: 0 7px; border-radius: 6px; background: var(--hd-bg-subtle, #f2f3f6); font-size: 11.5px; font-weight: 500; color: var(--hd-fg-muted); display: inline-flex; align-items: center; }
:root:root:root .phone .c4 + .home-ind, :root:root:root .phone .c4 .cp-bar { background: #fff !important; }
:root:root:root .phone .c4 .cp-bar { flex: none; padding: 10px 16px 6px !important; border-top: 1px solid var(--hd-edge); box-shadow: 0 -8px 16px -8px rgba(16,20,38,.08); }
[data-theme="dark"] .phone .c4 :is(.c4-pay, .c4-st, .c4-task) { background: var(--hd-surface-raised) !important; }

:root:root:root .phone .c4 .c4-hero { height: 262px; }
:root:root:root .phone .c4 .c4-pay { padding-bottom: 8px; } :root:root:root .phone .c4 .c4-pay .hd b { font-size: 32px; line-height: 36px; }
:root:root:root .phone .c4 .c4-h { margin: 14px 0 8px; }
:root:root:root .phone .c4 .c4-st { padding: 9px 10px; } :root:root:root .phone .c4 .c4-st b { margin-top: 4px; }

/* ===== campaign v5: one offer card (no repeated chips), connected steps in one card ===== */
:root:root:root .phone .c5 .c5-by { display: flex; align-items: center; gap: 5px; } .phone .c5 .c5-by b { color: #fff; font-weight: 600; } .phone .c5 .c5-by span { opacity: .7; margin: 0 2px; }
:root:root:root .phone .c5 .c4-hero { height: 270px; }
:root:root:root .phone .c5 .c4-body { padding-top: 14px; }
:root:root:root .phone .c5 .c5-offer { padding: 14px 16px 0; border-radius: 16px; background: #fff; box-shadow: 0 0 0 1px var(--hd-edge), 0 1px 2px rgba(16,20,38,.05), 0 6px 16px -8px rgba(16,20,38,.12); overflow: hidden; }
:root:root:root .phone .c5 .c5-offer .top { display: flex; justify-content: space-between; align-items: flex-start; }
:root:root:root .phone .c5 .c5-offer .k { display: block; font-size: 13px; font-weight: 500; color: var(--hd-fg-muted); }
:root:root:root .phone .c5 .c5-offer .top b { display: block; font: 700 36px/40px var(--font-brand); letter-spacing: -.025em; color: var(--hd-fg); }
:root:root:root .phone .c5 .c5-offer .mix { margin: 2px 0 0; font-size: 14px; color: var(--hd-fg-muted); } .phone .c5 .c5-offer .mix b { color: var(--hd-fg); font-weight: 600; }
:root:root:root .phone .c5 .c5-offer .mix span { display: inline-block; margin: 0 2px; padding: 0 5px; height: 18px; line-height: 18px; border-radius: 5px; background: var(--hd-success-subtle); color: var(--hd-success-strong); font-size: 11.5px; font-weight: 600; vertical-align: 1px; }
:root:root:root .phone .c5 .c4-bar { margin-top: 12px; height: 10px; border-radius: 5px; }
:root:root:root .phone .c5 .ends { display: flex; justify-content: space-between; margin-top: 6px; font-size: 12.5px; color: var(--hd-fg-muted); } .phone .c5 .ends b { color: var(--hd-fg); font-weight: 600; }
:root:root:root .phone .c5 .c5-offer .ft { display: flex; align-items: center; gap: 6px; margin: 12px -16px 0; padding: 10px 16px; background: var(--hd-bg-subtle, #f5f6f8); font-size: 12.5px; color: var(--hd-fg-muted); } .phone .c5 .c5-offer .ft b { color: var(--hd-fg); font-weight: 600; } .phone .c5 .c5-offer .ft svg { flex: none; color: var(--hd-fg-subtle); }
:root:root:root .phone .c5 .c5-steps { position: relative; display: grid; grid-template-columns: repeat(3, 1fr); padding: 14px 8px 12px; border-radius: 16px; background: #fff; box-shadow: 0 0 0 1px var(--hd-edge); }
:root:root:root .phone .c5 .c5-steps::before { content: ''; position: absolute; top: 32px; left: 18%; right: 18%; height: 0; border-top: 1.5px dashed var(--hd-track-strong, #cfd2da); }
:root:root:root .phone .c5 .c5-st { position: relative; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 1px; }
:root:root:root .phone .c5 .c5-ti { width: 38px !important; height: 38px !important; border-radius: 12px !important; display: grid !important; place-items: center; color: var(--hd-accent); background: #fff !important; position: relative; z-index: 1; }
:root:root:root .phone .c5 .c5-st b { margin-top: 8px; font-size: 13.5px; font-weight: 600; } .phone .c5 .c5-st small { font-size: 12px; color: var(--hd-fg-muted); }
[data-theme="dark"] .phone .c5 :is(.c5-offer, .c5-steps) { background: var(--hd-surface-raised) !important; }

:root:root:root .phone .c4 .c4-body > * { flex: none !important; }
:root:root:root .phone .c5 .c4-hero { height: 250px; }

:root:root:root .phone .c5 .c5-offer .ft { display: block !important; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
:root:root:root .phone .c5 .c5-offer .ft svg { display: inline-block; vertical-align: -2px; margin-right: 6px; }

/* ===== offer card v6: calm — label, big number, one muted line, one hairline footer ===== */
:root:root:root .phone .c4 .c6-offer { flex: none; padding: 14px 16px 0; border-radius: 16px; background: #fff; box-shadow: 0 0 0 1px var(--hd-edge), 0 1px 2px rgba(16,20,38,.04); }
:root:root:root .phone .c4 .c6-offer .k { display: block; font-size: 13px; font-weight: 500; color: var(--hd-fg-muted); }
:root:root:root .phone .c4 .c6-offer .big { display: block; margin-top: 2px; font: 700 34px/38px var(--font-brand); letter-spacing: -.025em; color: var(--hd-fg); }
:root:root:root .phone .c4 .c6-offer .mix { margin: 4px 0 0; font-size: 13.5px; line-height: 19px; color: var(--hd-fg-muted); } .phone .c4 .c6-offer .mix b { color: var(--hd-fg); font-weight: 600; }
:root:root:root .phone .c4 .c6-offer .ft { display: flex; justify-content: space-between; margin: 12px -16px 0; padding: 11px 16px; border-top: 1px solid var(--hd-edge); font-size: 13px; color: var(--hd-fg-muted); } .phone .c4 .c6-offer .ft b { color: var(--hd-fg); font-weight: 600; }
[data-theme="dark"] .phone .c4 .c6-offer { background: var(--hd-surface-raised) !important; }

/* ===== Join flow (sheet over the campaign) ===== */
.phone .jf-under { position: absolute; inset: 0; } .phone .jf-under img { width: 100%; height: 300px; object-fit: cover; display: block; }
.phone .jf-under .jf-ut { position: absolute; left: 16px; top: 250px; color: #fff; display: flex; flex-direction: column; } .phone .jf-under .jf-ut b { font: 700 24px/28px var(--font-brand); }
.phone .scr:has(.jf) .scrim { position: absolute; inset: 0; background: rgba(10,12,18,.42); }
.phone .scr:has(.jf) .overlay { position: absolute; left: 0; right: 0; bottom: 0; }
.phone .sheet.jf { background: #fff; border-radius: 24px 24px 0 0; padding: 8px 16px 30px; display: flex; flex-direction: column; gap: 12px; }
.phone .jf .grab { width: 40px; height: 5px; border-radius: 3px; background: var(--hd-track-strong, #d5d7de); margin: 0 auto 4px; }
.phone .jf-hd { display: flex; justify-content: space-between; align-items: flex-start; } .phone .jf-hd small { font-size: 12.5px; font-weight: 600; color: var(--hd-fg-muted); } .phone .jf-hd h2 { margin: 2px 0 0; font: 700 24px/28px var(--font-brand); letter-spacing: -.02em; }
.phone .jf-x { width: 32px !important; height: 32px !important; }
.phone .jf-hold { position: relative; display: flex; align-items: center; gap: 10px; padding: 12px 12px 16px; border-radius: 14px; background: #fff; box-shadow: 0 0 0 1px var(--hd-edge); overflow: hidden; }
.phone .jf-ht { width: 36px !important; height: 36px !important; border-radius: 10px !important; display: grid !important; place-items: center; color: var(--hd-accent); flex: none; }
.phone .jf-hold .tx { flex: 1; min-width: 0; } .phone .jf-hold .tx b { display: block; font-size: 14.5px; font-weight: 600; } .phone .jf-hold .tx small { font-size: 12.5px; color: var(--hd-fg-muted); } .phone .jf-hold .tx small b { display: inline; color: var(--hd-fg); font-size: 12.5px; }
.phone .jf-hold .btn.s.sm { height: 32px !important; min-height: 0 !important; padding: 0 10px !important; font-size: 13px !important; flex: none; }
.phone .jf-tape { position: absolute; left: 0; right: 0; bottom: 0; height: 3px; background: var(--hd-track, rgba(16,20,38,.08)); } .phone .jf-tape > i { display: block; height: 100%; background: var(--hd-accent); }
.phone .jf-list { display: flex; flex-direction: column; gap: 0; border-radius: 14px; box-shadow: 0 0 0 1px var(--hd-edge); overflow: hidden; }
.phone .jf-row { display: flex; align-items: center; gap: 12px; padding: 10px 12px; } .phone .jf-row + .jf-row { border-top: 1px solid var(--hd-edge); }
.phone .jf-ti { width: 34px !important; height: 34px !important; border-radius: 10px !important; display: grid !important; place-items: center; color: var(--hd-accent); flex: none; }
.phone .jf-row .tx b { display: block; font-size: 14.5px; font-weight: 600; } .phone .jf-row .tx small { font-size: 12.5px; color: var(--hd-fg-muted); }
.phone .jf-act { display: flex; flex-direction: column; gap: 8px; margin-top: 2px; } .phone .jf-act .btn { height: 48px !important; gap: 8px; }
.phone .jf-note { margin: -2px 0 0; text-align: center; font-size: 12.5px; color: var(--hd-fg-muted); }
.phone .jf-file { display: flex; align-items: center; gap: 12px; padding: 10px 12px; border-radius: 14px; box-shadow: 0 0 0 1px var(--hd-edge); }
.phone .jf-fi { width: 36px !important; height: 36px !important; border-radius: 10px !important; display: grid !important; place-items: center; color: var(--hd-fg-muted); flex: none; }
.phone .jf-file .tx b { display: block; font-size: 14px; font-weight: 600; } .phone .jf-file .tx small { font-size: 12.5px; color: var(--hd-fg-muted); }
.phone .jf-ok { display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 14px; background: var(--hd-success-subtle); }
.phone .jf-ok .ic-ok { color: var(--hd-success, #0a8a4a); display: inline-flex; } .phone .jf-ok .tx b { display: block; font-size: 14px; font-weight: 600; color: var(--hd-success-strong); } .phone .jf-ok .tx small { font-size: 12.5px; color: var(--hd-fg); } .phone .jf-ok .tx small b { display: inline; color: var(--hd-fg); }
.phone .jf-sum { display: flex; justify-content: space-between; align-items: baseline; padding: 2px 2px 0; font-size: 13px; color: var(--hd-fg-muted); } .phone .jf-sum b { font: 700 22px/26px var(--font-brand); color: var(--hd-fg); letter-spacing: -.02em; }

/* spot hold v2: one slim line — clock, time left, quiet "Add 10 min" */
.phone .jf-hold2 { display: flex; align-items: center; gap: 8px; height: 40px; padding: 0 6px 0 12px; border-radius: 12px; background: var(--hd-bg-subtle, #f4f5f7); font-size: 13.5px; color: var(--hd-fg-muted); }
.phone .jf-hold2 svg { color: var(--hd-accent); flex: none; } .phone .jf-hold2 span { flex: 1; } .phone .jf-hold2 b { color: var(--hd-fg); font-weight: 600; }
.phone .jf-add { height: 30px; padding: 0 10px; border: 0; border-radius: 8px; background: none; font: 600 13px var(--font-ui); color: var(--hd-accent-strong, var(--hd-link)); cursor: pointer; }
"""
