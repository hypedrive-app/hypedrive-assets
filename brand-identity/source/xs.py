# Final polish layer: the standard scale + snaps. Loads before xz (buttons) so the button interaction layer stays last.
XS = r"""
/* ===== XS — the standard scale (final polish; loads before xz). Snap, never redesign. =====
   Control heights   xs 32 · sm 36 · md 40 · lg 44 · cta 48-52
   Radii             badge 6 · menu item / small control 8 · button, input, thumb 10 · chip, tile 12 · card 14-16 · sheet 24 · full
   Type (size/line/weight)  11.5/16/500 · 12.5/16/500 · 13.5/18/400 · 14/20/400 · 15/22/400 (titles 15/20/600) · 17/22/600 · 20/26/650 · 24/30/700 · 28/34/700 · 34+/1.1/700
   Icons             16 sm controls + menus · 18 md controls · 20 rows + top bars · 24 tab bar (12 inside badges)
   Avatars           24 · 32 · 40 · 56 · 64
   Card gap          8 in lists · 12-16 between groups
   Shadows           e1 cards · e2 popovers · e3 dialogs + sheets
   Only the keyboard focus ring and the input focus/error edge may be coloured. */
:root {
  --xs-h-xs: 32px; --xs-h-sm: 36px; --xs-h-md: 40px; --xs-h-lg: 44px; --xs-h-cta: 52px;
  --xs-r-badge: 6px; --xs-r-item: 8px; --xs-r-ctl: 10px; --xs-r-chip: 12px; --xs-r-card: 16px; --xs-r-card-sm: 14px; --xs-r-sheet: 24px; --xs-r-full: 999px;
  --xs-fs-1: 11.5px; --xs-fs-2: 12.5px; --xs-fs-3: 13.5px; --xs-fs-4: 14px; --xs-fs-5: 15px; --xs-fs-6: 17px; --xs-fs-7: 20px; --xs-fs-8: 24px; --xs-fs-9: 28px; --xs-fs-10: 34px;
  --xs-lh-1: 16px; --xs-lh-2: 16px; --xs-lh-3: 18px; --xs-lh-4: 20px; --xs-lh-5: 22px; --xs-lh-6: 22px; --xs-lh-7: 26px; --xs-lh-8: 30px; --xs-lh-9: 34px; --xs-lh-10: 38px;
  --xs-fw-reg: 400; --xs-fw-med: 500; --xs-fw-semi: 600; --xs-fw-bold: 700;
  --xs-ic-sm: 16px; --xs-ic-md: 18px; --xs-ic-row: 20px; --xs-ic-tab: 24px;
  --xs-av-1: 24px; --xs-av-2: 32px; --xs-av-3: 40px; --xs-av-4: 56px; --xs-av-5: 64px;
  --xs-gap-list: 8px; --xs-gap-group: 16px;
  --xs-e1: 0 1px 1px rgba(16,20,38,.04), 0 2px 4px -1px rgba(16,20,38,.04);
  --xs-e2: 0 0 0 1px rgba(16,20,38,.14), 0 1px 2px rgba(16,20,38,.06), 0 4px 8px -2px rgba(16,20,38,.07), 0 12px 16px -4px rgba(16,20,38,.09);
  --xs-e3: 0 0 0 1px rgba(16,20,38,.14), 0 2px 4px rgba(16,20,38,.05), 0 8px 16px -2px rgba(16,20,38,.08), 0 24px 40px -8px rgba(16,20,38,.12);
}
:root, [data-theme] { --xs-ctl-off: color-mix(in srgb, var(--hd-fg) 28%, transparent); --xs-track-off: color-mix(in srgb, var(--hd-fg) 16%, transparent); }
[data-theme="dark"] {
  --xs-e1: 0 1px 2px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.05);
  --xs-e2: 0 0 0 1px rgba(255,255,255,.13), 0 1px 2px rgba(0,0,0,.5), 0 4px 8px -2px rgba(0,0,0,.45), 0 12px 16px -4px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.07);
  --xs-e3: 0 0 0 1px rgba(255,255,255,.13), 0 2px 4px rgba(0,0,0,.5), 0 8px 16px -2px rgba(0,0,0,.5), 0 24px 40px -8px rgba(0,0,0,.6), inset 0 1px 0 rgba(255,255,255,.08);
  --xs-track-off: rgba(255,255,255,.18);
}

/* ---- controls: heights ---- */
:root:root .btn.sm, :root:root .btn.s.sm.block { height: var(--xs-h-sm) !important; min-height: var(--xs-h-sm) !important; }

/* ---- checkbox · radio · toggle · slider (owner spec) ---- */
:root:root .check, :root:root .radio { width: 20px; height: 20px; box-sizing: border-box; border: 1.5px solid var(--xs-ctl-off); background: var(--hd-surface); box-shadow: none; }
:root:root .check { border-radius: 6px; }
:root:root .radio { border-radius: 50%; }
:root:root .check.on, :root:root .radio.on { border-color: var(--hd-accent); }
:root:root .check.on { background: var(--hd-accent); }
:root:root .check.on svg, :root:root .check.on .ic { width: 14px; height: 14px; stroke: #fff; color: #fff; stroke-width: 2.5; }
:root:root .radio.on { background: radial-gradient(circle at 50% 50%, #fff 0 4px, var(--hd-accent) 4.5px); }
:root:root .switch { width: 40px; height: 24px; border-radius: 12px; background: var(--xs-track-off); box-shadow: none; }
:root:root .switch::after { width: 20px; height: 20px; top: 2px; left: 2px; background: #fff; box-shadow: 0 1px 2px rgba(0,0,0,.2); }
:root:root .switch.on, :root:root input.switch:checked { background: var(--hd-accent); box-shadow: none; }
:root:root .switch.on::after, :root:root input.switch:checked::after { left: 2px; transform: translateX(16px); }
:root:root input.switch:not(:checked), :root:root .panel.ix input.switch:not(:checked) { background: var(--xs-track-off); }
:root:root .flexw:has(> .check, > .radio, > .switch) { gap: 10px; min-height: 36px; align-items: center; }
:root:root .flexw:has(> .check, > .radio, > .switch) > .kt-body, :root:root .flexw:has(> .check, > .radio, > .switch) > .t-body { font-size: 15px; font-weight: 400; line-height: 20px; }
:root:root .flexw:has(> .check, > .radio, > .switch) > .kt-body + :is(.check, .radio, .switch) { margin-left: 20px; }
:root:root .slider { height: 4px; border-radius: 2px; background: var(--xs-track-off); box-shadow: none; }
:root:root .slider i { border-radius: 2px; background: var(--hd-accent); }
:root:root .slider b { width: 20px; height: 20px; margin: -10px; border: 0; background: #fff; box-shadow: 0 0 0 1px var(--hd-edge-strong, rgba(16,20,38,.22)), 0 1px 3px rgba(16,20,38,.22); }

:root:root .slider + .flexw > span { font-size: 12.5px !important; font-weight: 400 !important; color: var(--hd-fg-muted) !important; }

/* ---- keyboard focus: one ring, 2px focus colour + 2px surface gap, follows each control's radius ---- */
:root:root .chip.foc, :root:root .chip:focus-visible, :root:root .check.foc, :root:root .radio.foc, :root:root .switch.foc, :root:root input.switch:focus-visible,
:root:root .iconbtn:focus-visible, :root:root .tabs > span:focus-visible, :root:root .nav:focus-visible, :root:root .row.foc {
  outline: none !important; box-shadow: 0 0 0 2px var(--xs-ring-gap, var(--hd-surface)), 0 0 0 4px var(--hd-focus) !important; }
:root:root .box { --xs-ring-gap: var(--hd-bg-subtle); }
[data-theme="dark"] .box { --xs-ring-gap: var(--hd-bg); }
:root:root .flexw:has(> .foc) { gap: 16px; padding: 4px; }
:root:root .btn.foc, :root:root .btn:focus-visible { outline: none !important; }

/* ---- type roles ---- */
:root:root .t-display { font-size: 34px; line-height: 38px; font-weight: 700; }
:root:root .t-h1 { font-size: 24px; line-height: 30px; }
:root:root .t-h2 { font-size: 20px; line-height: 26px; }
:root:root .t-h3 { font-size: 15px; line-height: 20px; }

/* ---- elevation tiers ---- */
:root:root :is(.card, .row:not(.sel), .panel, .group, .stat, .banner, .ws) { box-shadow: var(--xs-e1) !important; }
:root:root :is(.suggest, .tooltip, .g2tip, .ctip, .toast) { box-shadow: var(--xs-e2) !important; }
:root:root :is(.dialog, .sheet.sd-sheet, .cmdk, .drawer) { box-shadow: var(--xs-e3) !important; }

/* ---- no tinted borders / glows: a selected card is fill-only ---- */
:root:root .shell .rc2.open { box-shadow: var(--xs-e1) !important; border-color: var(--hd-edge) !important; background: var(--hd-accent-subtle) !important; }
:root:root .bar i, :root:root .tape i { box-shadow: inset 0 1px 0 rgba(255,255,255,.22), inset 0 -1px 0 rgba(0,0,0,.12); }

:root:root .u-dz.drag { border-color: var(--hd-border-strong, var(--hd-edge)) !important; background: var(--hd-accent-subtle) !important; }
:root:root .xm3-id > img { width: 56px !important; height: 56px !important; }

:root:root .n-iev2 { background: transparent !important; }

:root:root .row small > svg.ic { display: inline-block; vertical-align: -2px; margin-right: 4px; }

:root:root kbd, :root:root .kbd { border: 0 !important; box-shadow: none !important; background: none !important; padding: 0 2px !important; min-width: 0 !important; height: auto !important; color: var(--hd-fg-subtle); font-family: var(--font-ui); }

/* ---- generated snaps: every off-scale size/weight/radius/icon/avatar measured in the audit -> nearest step ---- */
/*AUTO-BEGIN*/
:root:root div.barlab > b { font-size:13.5px !important; }
:root:root div.bt > b { font-size:20px !important; }
:root:root div.e > b { font-size:20px !important; }
:root:root div.flexw > b { font-size:15px !important; }
:root:root div.row.n-lr > div.tx > b { font-size:15px !important; }
:root:root p > b { font-size:15px !important; }
:root:root span.m-up.err > b { font-size:12.5px !important; }
:root:root span.n-sub > b { font-size:13.5px !important; }
:root:root span.t-small > b { font-size:13.5px !important; }
:root:root b.d2t { font-size:15px !important; }
:root:root div.cmp2 > div > b.num { font-size:12.5px !important; }
:root:root div.end > b.num { font-size:15px !important; }
:root:root div.flexw.t-small > b.num { font-size:13.5px !important; }
:root:root div.n-cr > b.num { font-size:13.5px !important; }
:root:root div.pv > b.num { font-size:12.5px !important; }
:root:root div.tt-r > b.num { font-size:13.5px !important; }
:root:root div.en-b > span > b.num { font-size:13.5px !important; }
:root:root div.n-plat > span > b.num { font-size:13.5px !important; }
:root:root div.n-vrow > span > b.num { font-size:13.5px !important; }
:root:root span.n-cr > b.num { font-size:13.5px !important; }
:root:root span.qty > b.num { font-size:15px !important; }
:root:root span.t-small.muted > b.num { font-size:13.5px !important; }
:root:root b.num.hero-num { font-size:28px !important; }
:root:root div.flexw > b.t-h2 { font-size:20px !important; }
:root:root div.n-gh1 > b.t-h2 { font-size:20px !important; }
:root:root b.t-small { font-size:13.5px !important; }
:root:root button.btn.p.lg { font-size:15px !important; }
:root:root button.btn.p.lg.block { font-size:15px !important; }
:root:root button.btn.p.lg.block.dis { font-size:15px !important; }
:root:root div.flexw > div { font-size:12.5px !important; }
:root:root div.cgh { font-size:12.5px !important; }
:root:root div.ci { font-size:15px !important; }
:root:root div.ci.hl { font-size:15px !important; }
:root:root div.flexw.t-small { font-size:13.5px !important; }
:root:root div.flexw.t-small.muted { font-size:13.5px !important; }
:root:root div.l2 { font-size:13.5px !important; }
:root:root div.lbl { font-size:13.5px !important; }
:root:root div.rprod { font-size:13.5px !important; }
:root:root div.sbh { font-size:12.5px !important; }
:root:root div.sg-h { font-size:12.5px !important; }
:root:root div.t-cap.muted { font-size:12.5px !important; }
:root:root div.t-cap.subtle { font-size:12.5px !important; }
:root:root div.t > div.t-h1 { font-size:28px !important; }
:root:root div.box.tstack > div.t-h2 { font-size:20px !important; }
:root:root div.card.n-page > div.t-h2 { font-size:20px !important; }
:root:root div.card.n-page.n-succ > div.t-h2 { font-size:20px !important; }
:root:root div.card.n-state > div.t-h2 { font-size:17px !important; }
:root:root div.sheet.sd-sheet > div.t-h2 { font-size:20px !important; }
:root:root div.t-small { font-size:13.5px !important; }
:root:root div.t-small.muted { font-size:13.5px !important; }
:root:root div.xa-h { font-size:20px !important; }
:root:root div.sheet > div.xm2-h { font-size:24px !important; }
:root:root div.xm2-c.xm2-earn > em { font-size:13.5px !important; }
:root:root small > em { font-size:13.5px !important; }
:root:root div.xm3-nil > h2 { font-size:20px !important; }
:root:root section.sec > h2 { font-size:28px !important; }
:root:root section.sec.nw.nw1 > h2 { font-size:28px !important; }
:root:root section.sec.nw.nw2 > h2 { font-size:28px !important; }
:root:root section.sec.nw.nw3 > h2 { font-size:28px !important; }
:root:root section.sec.nw.nw4 > h2 { font-size:28px !important; }
:root:root section.sec.nw.nw5 > h2 { font-size:28px !important; }
:root:root section.sec.nw.nw6 > h2 { font-size:28px !important; }
:root:root section.sec.nw.nw7 > h2 { font-size:28px !important; }
:root:root section.sec.nw.nw8 > h2 { font-size:28px !important; }
:root:root section.sec.nw.nw9 > h2 { font-size:28px !important; }
:root:root b > i { font-size:13.5px !important; }
:root:root div.cft > span > kbd.kbd { font-size:13.5px !important; }
:root:root span.t-cap.muted > kbd.kbd { font-size:12.5px !important; }
:root:root label { font-size:13.5px !important; }
:root:root div.panel.rcard2 > p { font-size:15px !important; }
:root:root div.xm3-nt > p { font-size:15px !important; }
:root:root section.sec > p { font-size:15px !important; }
:root:root section.sec.nw.nw1 > p { font-size:15px !important; }
:root:root section.sec.nw.nw2 > p { font-size:15px !important; }
:root:root section.sec.nw.nw3 > p { font-size:15px !important; }
:root:root section.sec.nw.nw4 > p { font-size:15px !important; }
:root:root section.sec.nw.nw5 > p { font-size:15px !important; }
:root:root section.sec.nw.nw6 > p { font-size:15px !important; }
:root:root section.sec.nw.nw7 > p { font-size:15px !important; }
:root:root section.sec.nw.nw8 > p { font-size:15px !important; }
:root:root section.sec.nw.nw9 > p { font-size:15px !important; }
:root:root p.n-eap { font-size:15px !important; }
:root:root p.t-small.muted { font-size:13.5px !important; }
:root:root p.xm1-p { font-size:15px !important; }
:root:root div.me > div > small { font-size:12.5px !important; }
:root:root div.n-apps > div > small { font-size:12.5px !important; }
:root:root div.n-spins > div > small { font-size:12.5px !important; }
:root:root div.n-wzt > div > small { font-size:12.5px !important; }
:root:root div.ws > div > small { font-size:12.5px !important; }
:root:root div.xm1-facts > div > small { font-size:13.5px !important; }
:root:root div.xm2-c.xm2-earn > div > small { font-size:13.5px !important; }
:root:root div.bt > small { font-size:13.5px !important; }
:root:root div.e > small { font-size:13.5px !important; }
:root:root div.rv-who > small { font-size:13.5px !important; }
:root:root div.banner > div.tx > small { font-size:13.5px !important; }
:root:root div.row > div.tx > small { font-size:13.5px !important; }
:root:root div.row.m-lr > div.tx > small { font-size:13.5px !important; }
:root:root div.row.n-lr > div.tx > small { font-size:13.5px !important; }
:root:root div.row.sel > div.tx > small { font-size:13.5px !important; }
:root:root div.s > div.tx > small { font-size:13.5px !important; }
:root:root div.s.done > div.tx > small { font-size:13.5px !important; }
:root:root div.s.now > div.tx > small { font-size:13.5px !important; }
:root:root div.xm2-c > div.tx > small { font-size:13.5px !important; }
:root:root div.xm2-c.on > div.tx > small { font-size:13.5px !important; }
:root:root div.xm2-c.xm2-cour > div.tx > small { font-size:13.5px !important; }
:root:root div.xm2-c.xm2-ship > div.tx > small { font-size:13.5px !important; }
:root:root div.xm2-c.xm2-tx > div.tx > small { font-size:13.5px !important; }
:root:root div.xm1-mini > small { font-size:13.5px !important; }
:root:root div.xm2-wh > small { font-size:13.5px !important; }
:root:root div.xm3-lt > small { font-size:13.5px !important; }
:root:root div.xm3-nt > small { font-size:13.5px !important; }
:root:root div.typewt > span > small { font-size:12.5px !important; }
:root:root div.xm1-pad > span > small { font-size:11px !important; }
:root:root span.n-asx > small { font-size:13.5px !important; }
:root:root span.n-t > small { font-size:13.5px !important; }
:root:root small.muted.t-cap { font-size:12.5px !important; }
:root:root small.t-cap.muted { font-size:12.5px !important; }
:root:root div.cmp2 > div > span { font-size:12.5px !important; }
:root:root div.t-ch > div > span { font-size:13.5px !important; }
:root:root div.xm3-id > div > span { font-size:13.5px !important; }
:root:root div.barlab > span { font-size:13.5px !important; }
:root:root div.cft > span { font-size:12.5px !important; }
:root:root div.en-b > span { font-size:13.5px !important; }
:root:root div.flexw.t-small > span { font-size:13.5px !important; }
:root:root div.input > span { font-size:15px !important; }
:root:root div.input.foc.d2i > span { font-size:15px !important; }
:root:root div.labrow > span { font-size:12.5px !important; }
:root:root div > div.legend > span { font-size:13.5px !important; }
:root:root div.panel > div.legend > span { font-size:13.5px !important; }
:root:root div.vz > div.legend > span { font-size:12.5px !important; }
:root:root div.n-hrl > span { font-size:13.5px !important; }
:root:root div.n-hrl.left > span { font-size:13.5px !important; }
:root:root div.n-vrow > span { font-size:13.5px !important; }
:root:root div.pv > span { font-size:12.5px !important; }
:root:root div.sd-pt > span { font-size:13.5px !important; }
:root:root div.sg-f > span { font-size:12.5px !important; }
:root:root div.k-top > div.tabs > span { font-size:15px !important; }
:root:root div.tt-r > span { font-size:13.5px !important; }
:root:root div.xm1-code.num > span { font-size:20px !important; }
:root:root p.xm2-tip > span { font-size:13.5px !important; }
:root:root span.n-hint > span { font-size:12.5px !important; }
:root:root span.qty > span { font-size:15px !important; }
:root:root span.rm > span { font-size:13.5px !important; }
:root:root div.avs > span.av.av-0 { font-size:12.5px !important; }
:root:root div.avs > span.av.av-1 { font-size:12.5px !important; }
:root:root div.avs > span.av.av-2 { font-size:12.5px !important; }
:root:root div.me > span.av.av-2 { font-size:12.5px !important; }
:root:root div.panel.rail > span.av.av-2 { font-size:12.5px !important; }
:root:root div.avs > span.av.av-4 { font-size:12.5px !important; }
:root:root span.badge.danger { font-size:12.5px !important; }
:root:root span.badge.info { font-size:12.5px !important; }
:root:root span.badge.neutral { font-size:12.5px !important; }
:root:root span.badge.solid { font-size:12.5px !important; }
:root:root span.badge.success { font-size:12.5px !important; }
:root:root span.badge.warning { font-size:12.5px !important; }
:root:root span.chd { font-size:13.5px !important; }
:root:root div > div.flexw > span.chip { font-size:13.5px !important; }
:root:root div.toolbar > span.chip { font-size:13.5px !important; }
:root:root div.top > span.chip { font-size:13.5px !important; }
:root:root span.chip.foc { font-size:13.5px !important; }
:root:root div > div.flexw > span.chip.on { font-size:13.5px !important; }
:root:root span.cnt { font-size:12.5px !important; }
:root:root span.cnt-b { font-size:12.5px !important; }
:root:root span.cnt.hot { font-size:12.5px !important; }
:root:root div.panel.stat.k-bars > div.sh > span.dtext.up { font-size:13.5px !important; }
:root:root div.panel.stat.k-compare > div.sh > span.dtext.up { font-size:13.5px !important; }
:root:root div.grid.g4 > div.panel.stat.k-spark > div.sh > span.dtext.up { font-size:13.5px !important; }
:root:root span.err { font-size:13.5px !important; }
:root:root span.help.xm2-cnt { font-size:13.5px !important; }
:root:root span.k { font-size:13.5px !important; }
:root:root div.n-dvi > span.m { font-size:13.5px !important; }
:root:root div.n-dvr > span.m { font-size:13.5px !important; }
:root:root span.m-chip.num { font-size:12.5px !important; }
:root:root span.m-fn { font-size:12.5px !important; }
:root:root div.ctip > span.muted { font-size:12.5px !important; }
:root:root div.flexw.t-small > span.muted { font-size:13.5px !important; }
:root:root div.n-cr > span.muted { font-size:13.5px !important; }
:root:root span.n-cr > span.muted { font-size:13.5px !important; }
:root:root span.muted.t-small { font-size:13.5px !important; }
:root:root span.n-dvt { font-size:12.5px !important; }
:root:root span.n-fc { font-size:12.5px !important; }
:root:root span.n-gh { font-size:12.5px !important; }
:root:root span.n-sub { font-size:13.5px !important; }
:root:root span.n-tok { font-size:13.5px !important; }
:root:root div.sbar > span.num { font-size:15px !important; }
:root:root span.ok { font-size:13.5px !important; }
:root:root div.k-top > div.tabs > span.on { font-size:15px !important; }
:root:root div.search.foc > span.q { font-size:15px !important; }
:root:root span.rig { font-size:13.5px !important; }
:root:root span.rm { font-size:13.5px !important; }
:root:root span.rv-t.num { font-size:13.5px !important; }
:root:root span.sl { font-size:13.5px !important; }
:root:root span.sub { font-size:13.5px !important; }
:root:root span.t-cap.muted { font-size:12.5px !important; }
:root:root div.row > span.t-cap.muted.num { font-size:12.5px !important; }
:root:root span.t-cap.num.muted { font-size:12.5px !important; }
:root:root span.t-cap.subtle.num { font-size:12.5px !important; }
:root:root span.t-h2.n-iev { font-size:20px !important; }
:root:root div.topbar > span.t-small { font-size:13.5px !important; }
:root:root label.flexw > span.t-small { font-size:13.5px !important; }
:root:root div > span.t-small.muted { font-size:13.5px !important; }
:root:root div.card.n-cc > span.t-small.muted { font-size:13.5px !important; }
:root:root div.flexw > span.t-small.muted { font-size:13.5px !important; }
:root:root div.n-avt > span.t-small.muted { font-size:13.5px !important; }
:root:root div.n-ffoot > span.t-small.muted { font-size:13.5px !important; }
:root:root div.n-lmore > span.t-small.muted { font-size:13.5px !important; }
:root:root div.tl > span.t-small.muted { font-size:13.5px !important; }
:root:root span.l > span.t-small.muted { font-size:13.5px !important; }
:root:root span.t-small.muted.num { font-size:13.5px !important; }
:root:root span.t-small.subtle { font-size:13.5px !important; }
:root:root span.t-small.tk-lb { font-size:13.5px !important; }
:root:root span.tag { font-size:13.5px !important; }
:root:root span.th-sort { font-size:13.5px !important; }
:root:root span.tooltip { font-size:13.5px !important; }
:root:root span.trail.t-small { font-size:13.5px !important; }
:root:root span.x-plat { font-size:13.5px !important; }
:root:root span.xl { font-size:12.5px !important; }
:root:root span.xm2-hint { font-size:13.5px !important; }
:root:root span.xm3-day { font-size:13.5px !important; }
:root:root span.yl { font-size:12.5px !important; }
:root:root table.tbl > tbody > tr > th { font-size:13.5px !important; }
:root:root a.e2l { font-weight:600 !important; }
:root:root a.n-popl { font-weight:600 !important; }
:root:root div.me > div > b { font-weight:600 !important; }
:root:root div.xm1-facts > div > b { font-weight:600 !important; }
:root:root div.bt > b { font-weight:600 !important; }
:root:root div.e > b { font-weight:600 !important; }
:root:root div.n-dvi > b { font-weight:600 !important; }
:root:root div.n-dvr > b { font-weight:600 !important; }
:root:root div.sd-pt > b { font-weight:600 !important; }
:root:root div.sxv > b { font-weight:600 !important; }
:root:root div.row > div.tx > b { font-weight:600 !important; }
:root:root div.row.m-lr > div.tx > b { font-weight:600 !important; }
:root:root div.row.sel > div.tx > b { font-weight:600 !important; }
:root:root div.xm1-sech > b { font-weight:600 !important; }
:root:root div.xm2-ah > b { font-weight:600 !important; }
:root:root p.desc > b { font-weight:600 !important; }
:root:root p.xm1-earn > b { font-weight:600 !important; }
:root:root div.xm1-pad > span > b { font-weight:500 !important; }
:root:root span.crumb > b { font-weight:600 !important; }
:root:root span.n-sub > b { font-weight:600 !important; }
:root:root span.n-t > b { font-weight:600 !important; }
:root:root dd > b.num { font-weight:600 !important; }
:root:root div > b.num { font-weight:600 !important; }
:root:root div.chv > b.num { font-weight:600 !important; }
:root:root div.n-sum > b.num { font-weight:600 !important; }
:root:root div.sxv > b.num { font-weight:600 !important; }
:root:root p.xm1-sub > b.num { font-weight:600 !important; }
:root:root p.xm3-fact > b.num { font-weight:600 !important; }
:root:root b.t-h2 { font-weight:600 !important; }
:root:root button.btn.d { font-weight:600 !important; }
:root:root button.btn.d.dis { font-weight:600 !important; }
:root:root button.btn.d.foc { font-weight:600 !important; }
:root:root button.btn.d.hov { font-weight:600 !important; }
:root:root button.btn.d.prs { font-weight:600 !important; }
:root:root button.btn.d.sm { font-weight:600 !important; }
:root:root button.btn.g { font-weight:600 !important; }
:root:root button.btn.g.block { font-weight:600 !important; }
:root:root button.btn.g.dis { font-weight:600 !important; }
:root:root button.btn.g.foc { font-weight:600 !important; }
:root:root button.btn.g.hov { font-weight:600 !important; }
:root:root button.btn.g.prs { font-weight:600 !important; }
:root:root button.btn.g.sm { font-weight:600 !important; }
:root:root button.btn.link { font-weight:600 !important; }
:root:root button.btn.p { font-weight:600 !important; }
:root:root div.n-dvsign > button.btn.p.block { font-weight:600 !important; }
:root:root div.sheet > button.btn.p.block { font-weight:600 !important; }
:root:root button.btn.p.block.sd-cta { font-weight:600 !important; }
:root:root button.btn.p.dis { font-weight:600 !important; }
:root:root button.btn.p.e2b { font-weight:600 !important; }
:root:root button.btn.p.foc { font-weight:600 !important; }
:root:root button.btn.p.hov { font-weight:600 !important; }
:root:root button.btn.p.lg { font-weight:600 !important; }
:root:root button.btn.p.lg.block { font-weight:600 !important; }
:root:root button.btn.p.lg.block.dis { font-weight:600 !important; }
:root:root button.btn.p.prs { font-weight:600 !important; }
:root:root button.btn.p.sm { font-weight:600 !important; }
:root:root button.btn.s { font-weight:600 !important; }
:root:root div.cta.xm3-cta > button.btn.s.block { font-weight:600 !important; }
:root:root div.n-dvsign > button.btn.s.block { font-weight:600 !important; }
:root:root button.btn.s.dis { font-weight:600 !important; }
:root:root button.btn.s.foc { font-weight:600 !important; }
:root:root button.btn.s.hov { font-weight:600 !important; }
:root:root button.btn.s.prs { font-weight:600 !important; }
:root:root button.btn.s.sm { font-weight:600 !important; }
:root:root button.btn.s.sm.block { font-weight:600 !important; }
:root:root button.btn.s.sm.foc { font-weight:600 !important; }
:root:root button.btn.s.sm.n-done { font-weight:600 !important; }
:root:root div.cgh { font-weight:600 !important; }
:root:root div.hero-num.num { font-weight:600 !important; }
:root:root div.input.textarea { font-weight:500 !important; }
:root:root div.input.textarea.t-body { font-weight:500 !important; }
:root:root div.k-h1 { font-weight:600 !important; }
:root:root div.lbl { font-weight:600 !important; }
:root:root div.panel > aside.sb > div.nav.on { font-weight:600 !important; }
:root:root div.sbh { font-weight:600 !important; }
:root:root div.sg-h { font-weight:600 !important; }
:root:root div.t-display { font-weight:600 !important; }
:root:root div.t-h1 { font-weight:600 !important; }
:root:root div.t-h2 { font-weight:600 !important; }
:root:root div.x-title { font-weight:600 !important; }
:root:root div.xa-h { font-weight:600 !important; }
:root:root div.xm2-big { font-weight:600 !important; }
:root:root div.xm2-h { font-weight:600 !important; }
:root:root div.xm2-wb.num { font-weight:600 !important; }
:root:root div.xm3-nm { font-weight:600 !important; }
:root:root em { font-weight:600 !important; }
:root:root div.xm1-copy > h1.xm1-h { font-weight:600 !important; }
:root:root h1.xm3-h { font-weight:600 !important; }
:root:root div.xm3-nil > h2 { font-weight:600 !important; }
:root:root b > i { font-weight:500 !important; }
:root:root div.n-cin > kbd.kbd { font-weight:500 !important; }
:root:root div.n-cf > span > kbd.kbd { font-weight:500 !important; }
:root:root div.sg-f > span > kbd.kbd { font-weight:500 !important; }
:root:root span.n-hint > span > kbd.kbd { font-weight:500 !important; }
:root:root span.n-go > kbd.kbd { font-weight:500 !important; }
:root:root span.n-ci > span.n-k > kbd.kbd { font-weight:500 !important; }
:root:root span.sub > kbd.kbd { font-weight:500 !important; }
:root:root label { font-weight:600 !important; }
:root:root mark { font-weight:600 !important; }
:root:root div.tabbar > div > span { font-weight:600 !important; }
:root:root div > div.flexw.t-small > span { font-weight:600 !important; }
:root:root div.input > span { font-weight:500 !important; }
:root:root div.input.foc.d2i > span { font-weight:500 !important; }
:root:root div.input.hov > span { font-weight:500 !important; }
:root:root div.input.ok > span { font-weight:500 !important; }
:root:root div.input.textarea.err.n-ta > span { font-weight:500 !important; }
:root:root div.input.textarea.foc.n-ta > span { font-weight:500 !important; }
:root:root div.input.textarea.n-ta > span { font-weight:500 !important; }
:root:root div.n-tabs > span { font-weight:600 !important; }
:root:root div.on > span { font-weight:600 !important; }
:root:root div.tabs > span { font-weight:600 !important; }
:root:root div.tabs.xa-tabs > span { font-weight:600 !important; }
:root:root div.xm1-code.num > span { font-weight:600 !important; }
:root:root div.xm3-chips > span { font-weight:600 !important; }
:root:root h1.xm1-h > span { font-weight:600 !important; }
:root:root span.n-tgm > span { font-weight:600 !important; }
:root:root span.seg > span { font-weight:600 !important; }
:root:root span.chip { font-weight:600 !important; }
:root:root span.chip.foc { font-weight:600 !important; }
:root:root span.chip.on { font-weight:600 !important; }
:root:root div.shell > aside.sb > div.nav > span.cnt { font-weight:600 !important; }
:root:root div.shell > aside.sb > div.nav.on > span.cnt { font-weight:600 !important; }
:root:root span.cnt-b { font-weight:600 !important; }
:root:root span.cnt.hot { font-weight:600 !important; }
:root:root span.dtext.up { font-weight:600 !important; }
:root:root span.mono { font-weight:500 !important; }
:root:root button.btn.s.sm.n-sortb > span.muted { font-weight:500 !important; }
:root:root span.n-colon { font-weight:500 !important; }
:root:root span.n-end2 { font-weight:600 !important; }
:root:root span.n-gh { font-weight:600 !important; }
:root:root span.n-id { font-weight:500 !important; }
:root:root span.n-id.n-val { font-weight:500 !important; }
:root:root span.n-opt.n-slot.on { font-weight:600 !important; }
:root:root span.n-opt.on { font-weight:600 !important; }
:root:root div.input.foc > span.n-q { font-weight:500 !important; }
:root:root span.n-skip { font-weight:600 !important; }
:root:root span.n-val { font-weight:500 !important; }
:root:root div.field > div.input > span.num { font-weight:500 !important; }
:root:root div.input.foc > span.num { font-weight:500 !important; }
:root:root div.n-tabs > span.on { font-weight:600 !important; }
:root:root div.tabs > span.on { font-weight:600 !important; }
:root:root div.tabs.xa-tabs > span.on { font-weight:600 !important; }
:root:root span.n-tgm > span.on { font-weight:600 !important; }
:root:root span.seg > span.on { font-weight:600 !important; }
:root:root div.sh > span.sl { font-weight:500 !important; }
:root:root div.input > span.t-body { font-weight:500 !important; }
:root:root span.t-h2 { font-weight:600 !important; }
:root:root span.t-h2.n-iev { font-weight:600 !important; }
:root:root span.th-sort { font-weight:600 !important; }
:root:root span.trail.t-small { font-weight:500 !important; }
:root:root span.ttl.x-page { font-weight:600 !important; }
:root:root span.xa-more { font-weight:600 !important; }
:root:root span.xm3-day { font-weight:600 !important; }
:root:root td.num { font-weight:600 !important; }
:root:root th { font-weight:600 !important; }
:root:root u { font-weight:600 !important; }
:root:root div.n-more2 > button.btn.s.sm { border-radius:10px !important; }
:root:root button.btn.s.sm.n-sortb { border-radius:10px !important; }
:root:root div.card.t-ctxcard.t-comps > div.t-comp > div.t-field { border-radius:24px !important; }
:root:root div.t-field.on { border-radius:24px !important; }
:root:root div.xm1-card { border-radius:16px !important; }
:root:root div.xm2-wh { border-radius:16px !important; }
:root:root div > img { border-radius:16px !important; }
:root:root a.n-popl > svg { width:16px !important;height:16px !important; }
:root:root b > svg { width:20px !important;height:20px !important; }
:root:root button.btn.g.icon.icon > svg { width:20px !important;height:20px !important; }
:root:root div.flexw.t-small > svg { width:16px !important;height:16px !important; }
:root:root div.flexw.t-small.muted > svg { width:16px !important;height:16px !important; }
:root:root div.n-cr > svg { width:16px !important;height:16px !important; }
:root:root div.lblgap > div.stars > svg { width:20px !important;height:20px !important; }
:root:root div.xm1-bar > svg { width:20px !important;height:20px !important; }
:root:root div.xm1-bar.xm1-s > svg { width:20px !important;height:20px !important; }
:root:root div.xm2-add > svg { width:20px !important;height:20px !important; }
:root:root small > svg { width:12px !important;height:12px !important; }
:root:root div > span > svg { width:16px !important;height:16px !important; }
:root:root div.sxleg.num > span > svg { width:16px !important;height:16px !important; }
:root:root div.xm2-ph > span > svg { width:12px !important;height:12px !important; }
:root:root span.badge.danger > svg { width:12px !important;height:12px !important; }
:root:root span.badge.info > svg { width:12px !important;height:12px !important; }
:root:root span.badge.neutral > svg { width:12px !important;height:12px !important; }
:root:root span.badge.success > svg { width:12px !important;height:12px !important; }
:root:root span.badge.warning > svg { width:12px !important;height:12px !important; }
:root:root span.bell > svg { width:20px !important;height:20px !important; }
:root:root span.cg > svg { width:16px !important;height:16px !important; }
:root:root span.check.on > svg { width:16px !important;height:16px !important; }
:root:root span.check.on.foc > svg { width:16px !important;height:16px !important; }
:root:root span.chip > svg { width:16px !important;height:16px !important; }
:root:root span.clr > svg { width:12px !important;height:12px !important; }
:root:root span.crumb > svg { width:16px !important;height:16px !important; }
:root:root span.k > svg { width:16px !important;height:16px !important; }
:root:root span.m-up.err > svg { width:20px !important;height:20px !important; }
:root:root span.n-app > svg { width:24px !important;height:24px !important; }
:root:root span.n-clr > svg { width:12px !important;height:12px !important; }
:root:root span.n-eai > svg { width:20px !important;height:20px !important; }
:root:root span.rig > svg { width:16px !important;height:16px !important; }
:root:root span.rs > svg { width:12px !important;height:12px !important; }
:root:root span.rv-st > svg { width:16px !important;height:16px !important; }
:root:root span.stars > svg { width:16px !important;height:16px !important; }
:root:root span.tst.danger > svg { width:16px !important;height:16px !important; }
:root:root span.tst.neutral > svg { width:16px !important;height:16px !important; }
:root:root span.tst.success > svg { width:16px !important;height:16px !important; }
:root:root span.tst.warning > svg { width:16px !important;height:16px !important; }
:root:root div.tb > span.x-disc > svg { width:20px !important;height:20px !important; }
:root:root span.x-plat > svg { width:16px !important;height:16px !important; }
:root:root span.x-tile.n-errt > svg { width:20px !important;height:20px !important; }
:root:root span.xa-st > svg { width:16px !important;height:16px !important; }
:root:root div.n-dvprof > img { width:56px !important;height:56px !important;flex:none !important; }
:root:root div.n-hch > img { width:56px !important;height:56px !important;flex:none !important; }
:root:root span.x-avs > img { width:32px !important;height:32px !important;flex:none !important; }
:root:root div.panel.rc2 > img.av { width:40px !important;height:40px !important;flex:none !important; }
:root:root div.panel.rc2.chk > img.av { width:40px !important;height:40px !important;flex:none !important; }
:root:root div.panel.rc2.chk.open > img.av { width:40px !important;height:40px !important;flex:none !important; }
:root:root img.n-r { width:32px !important;height:32px !important;flex:none !important; }
:root:root img.tav { width:32px !important;height:32px !important;flex:none !important; }
:root:root div.avs > span.av.av-0 { width:32px !important;height:32px !important;flex:none !important; }
:root:root div.avs.xa-stack > span.av.av-0 { width:32px !important;height:32px !important;flex:none !important; }
:root:root span.n-ci > span.av.av-0 { width:32px !important;height:32px !important;flex:none !important; }
:root:root div.avs > span.av.av-1 { width:32px !important;height:32px !important;flex:none !important; }
:root:root div.avs.xa-stack > span.av.av-1 { width:32px !important;height:32px !important;flex:none !important; }
:root:root span.n-opt > span.av.av-1 { width:32px !important;height:32px !important;flex:none !important; }
:root:root span.sg-logo > span.av.av-1 { width:32px !important;height:32px !important;flex:none !important; }
:root:root div.avs > span.av.av-2 { width:32px !important;height:32px !important;flex:none !important; }
:root:root div.avs.xa-stack > span.av.av-2 { width:32px !important;height:32px !important;flex:none !important; }
:root:root div.ws > span.av.av-2 { width:32px !important;height:32px !important;flex:none !important; }
:root:root span.n-opt.hv > span.av.av-2 { width:32px !important;height:32px !important;flex:none !important; }
:root:root div.panel.rc2 > span.av.av-3 { width:40px !important;height:40px !important;flex:none !important; }
:root:root div.avs > span.av.av-4 { width:32px !important;height:32px !important;flex:none !important; }
:root:root span.n-opt > span.av.av-4 { width:32px !important;height:32px !important;flex:none !important; }
/*AUTO-END*/
"""
