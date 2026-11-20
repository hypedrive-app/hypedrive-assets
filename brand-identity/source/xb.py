# Section polish layer (xb): Empty states & tables, Charts, Shell, More components, Interaction.
XB = r"""
/* ---- Empty states & tables ---- */
.eb-wrap .lbl { margin: 0; }
.eb-empty { padding: 20px; display: grid; grid-template-columns: 120px 1fr; gap: 20px; align-items: center; }
.eb-empty > img { width: 120px; display: block; }
.eb-empty .eb-p { margin: 6px 0 16px; padding: 0; background: none; font-size: 15px; line-height: 22px; color: var(--hd-fg-muted); max-width: 40ch; }
.eb-near { padding: 10px; display: flex; flex-direction: column; gap: 2px; }
.eb-near > img { width: 100%; height: 84px; object-fit: cover; border-radius: 8px; display: block; margin-bottom: 8px; }
.eb-tbl th { padding: 12px 16px; }
.eb-tbl td { padding: 12px 16px; }

/* ---- Charts ---- */
.k-goalring .gr { align-items: flex-start; }

/* ---- Shell ---- */
.panel > .sb .nav { flex-shrink: 0; }
.panel.rail { background: var(--hd-bg-subtle); }

/* ---- More components ---- */
.cal .cg .rng { background: var(--hd-accent-subtle); color: var(--hd-accent-strong, var(--hd-link)); }
.cal .cg .rng + .rng, .cal .cg .sel + .rng { margin-left: 0; }
.cal .cg { column-gap: 0; }
.cal .cg .sel { border-radius: 10px; }

.mc3 > .stack { gap: 24px !important; }
.mc3 .lbl { margin-bottom: 10px; }
.mc3 .panel.cal { width: 100%; }
.mc3 .panel.pop { max-width: none; }

/* ---- Interaction ---- */
.panel.ix { padding: 18px; gap: 14px; }

/* =============== pb2 round 1 =============== */
/* keyboard hints: plain text, never keycaps */
.cmdk .kbd, .sbsearch .kbd, .search .kbd, .mc3 .kbd { border: 0 !important; box-shadow: none !important; background: none !important; padding: 0 !important; min-width: 0 !important; height: auto !important; font: 400 12.5px var(--font-ui) !important; color: var(--hd-fg-subtle) !important; }
.cmdk .cft span { display: inline-flex; gap: 4px; align-items: center; }
.cmdk .cft .kbd { font-size: 13px !important; }

/* ---- Tables: quiet ---- */
.eb-tbl th { background: none !important; font-weight: 500; font-size: 12.5px; color: var(--hd-fg-subtle); padding: 10px 16px; border-bottom: 1px solid var(--hd-edge); }
.eb-tbl td { padding: 10px 16px; border-bottom: 1px solid color-mix(in oklab, var(--hd-edge) 55%, transparent) !important; }
.eb-tbl tr:last-child td { border-bottom: 0 !important; }
.eb-tbl td:first-child b { font-weight: 600; font-size: 14px; }
.eb-near { gap: 0; }
.eb-near > b { font-size: 14px; font-weight: 600; }
.eb-near > .t-cap { font-size: 13px; margin-top: 2px; }

/* ---- Charts / stat tiles ---- */
.k-goalring { position: relative; }
.k-goalring .gr { display: block; }
.k-goalring .gr .ringw { position: absolute; right: 16px; bottom: 14px; }
.k-goalring { min-height: 0; }

/* ---- Shell ---- */
.panel.rail { background: var(--hd-surface); }
.cmdk .ci { height: 34px; font-size: 14px; border-radius: 8px; gap: 10px; }
.cmdk .ci .ic { width: 16px; height: 16px; color: var(--hd-fg-muted); }
.cmdk .ci.hl { background: color-mix(in oklab, var(--hd-fg) 6%, transparent); }
.cmdk .cgp { padding: 6px; } .cmdk .cin { height: 48px; }
.shell-x .tabs .cnt-b, .panel .tabs > span:not(.on) .cnt-b { background: none; color: var(--hd-fg-subtle); padding: 0 2px; }

/* ---- More components ---- */
.cal2 .c2n .btn, .cal2 .c2n .btn .ic, .c2n .btn.icon { color: var(--hd-fg-muted) !important; }
/* toast stack: front toast + two layers peeking 6px, same ink */
.toasts { height: auto; width: 340px; margin-top: 4px; padding-top: 12px; position: relative; }
.toasts .toast:nth-child(n) { position: relative; transform: none; opacity: 1; display: flex; z-index: 2; left: auto; right: auto; bottom: auto; }
.toasts::before, .toasts::after { content: ''; position: absolute; left: 0; right: 0; top: 12px; height: 44px; border-radius: 12px; background: #16181d; transform-origin: 50% 0; z-index: 1; box-shadow: inset 0 0 0 1px rgba(255,255,255,.06), 0 1px 2px rgba(10,12,18,.16); }
.toasts::before { transform: translateY(-6px) scale(.96); z-index: 1; }
.toasts::after { transform: translateY(-12px) scale(.92); z-index: 0; }
[data-theme="dark"] .toasts::before, [data-theme="dark"] .toasts::after { background: #f4f5f7; box-shadow: inset 0 0 0 1px rgba(0,0,0,.10); }
.toasts::before { filter: none; }
/* payout ticket stub: bare solid glyph, no ring */
.ticket .tr .tk-ok { color: var(--hd-success-solid, var(--hd-success)); display: inline-flex; }
.ticket .tr .tk-lb { color: var(--hd-fg-muted); font-size: 13px; }
.ticket .tr { background: radial-gradient(circle at 0 0, transparent 9px, var(--hd-surface) 9.5px) top / 100% 51% no-repeat, radial-gradient(circle at 0 100%, transparent 9px, var(--hd-surface) 9.5px) bottom / 100% 51% no-repeat; }
/* review stars: small, quiet */
.rcard .stars.rst { gap: 2px; color: var(--hd-star); align-items: center; }
.rcard .stars.rst .ic { width: 13px; height: 13px; }
/* campaign card */
.x-camp .cc-earn { color: var(--hd-fg); font-size: 15px; font-weight: 600; letter-spacing: -.01em; }
.x-camp .cc-tape { height: 3px; background: var(--hd-track); }
.x-camp .t-h3 { font-size: 17px; font-weight: 600; }

/* ---- Interaction: calm ---- */
.panel.ix input.switch:not(:checked) { background: color-mix(in oklab, var(--hd-fg) 18%, var(--hd-surface)); }
.panel.ix .t-cap { font-size: 12.5px; }
.panel.ix .btn { width: 100%; }

/* accordion: separate cards, one trailing down chevron that flips when open */
.acc2 { display: flex; flex-direction: column; gap: 8px; }
.acc2 .ac { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 14px; overflow: hidden; }
.acc2 .ac.open { border-color: var(--hd-border-strong, var(--hd-edge)); }
.acc2 .ai { display: flex; align-items: center; height: 52px; padding: 0 16px; font-size: 15px; font-weight: 600; border: 0; background: none; }
.acc2 .ac-c { margin-left: auto; display: inline-flex; color: var(--hd-fg-muted); }
.acc2 .ac.open .ac-c { transform: rotate(180deg); }
.acc2 .ab { padding: 0 16px 16px; font-size: 14px; line-height: 21px; color: var(--hd-fg-muted); text-wrap: pretty; max-width: 52ch; }

/* toast stack: the layers sit behind; the front toast must be fully visible (xcomp hides nth-child content) */
.toasts .toast:nth-child(n) { color: #f4f5f7 !important; filter: none !important; box-shadow: inset 0 0 0 1px rgba(255,255,255,.06), 0 1px 2px rgba(10,12,18,.20), 0 8px 24px -6px rgba(10,12,18,.32) !important; }
.toasts .toast:nth-child(n) > :not(svg) { opacity: 1 !important; }
.toasts .toast:nth-child(n) b { color: #fff !important; }
[data-theme="dark"] .toasts .toast:nth-child(n), [data-theme="dark"] .toasts .toast:nth-child(n) b { color: #16181d !important; }

/* ---- Charts: one stat anatomy ---- */
.sxrow { align-items: stretch; }
.panel.sx { padding: 16px; display: flex; flex-direction: column; min-width: 0; height: 148px; }
.sx .sxh { display: flex; align-items: baseline; justify-content: space-between; height: 18px; }
.sx .sxl { font-size: 13.5px; font-weight: 500; color: var(--hd-fg-muted); }
.sx .sxd { font-size: 12.5px; font-weight: 600; color: var(--hd-success-strong); font-variant-numeric: tabular-nums; }
.sx .sxv { display: flex; align-items: baseline; gap: 6px; margin-top: 6px; height: 32px; }
.sx .sxv b { font: 650 28px/32px var(--font-ui); letter-spacing: -.03em; }
.sx .sxv span { font-size: 15px; font-weight: 500; color: var(--hd-fg-muted); }
.sx .sxb { margin-top: auto; height: 40px; display: flex; flex-direction: column; justify-content: flex-end; gap: 8px; }
.sx .sxb .mbars { height: 40px; margin: 0; }
.sx .sxc { font-size: 12.5px; color: var(--hd-fg-muted); line-height: 16px; }
.sx .segs { margin: 0; }
.sx .sxstack { display: flex; gap: 2px; height: 8px; }
.sx .sxstack i { display: block; border-radius: 4px; background: var(--hd-accent); }
.sx .sxstack i:nth-child(2) { background: color-mix(in oklab, var(--hd-accent) 60%, var(--hd-surface)); }
.sx .sxstack i:nth-child(3) { background: color-mix(in oklab, var(--hd-accent) 30%, var(--hd-surface)); }
.sx .sxleg { display: flex; gap: 14px; font-size: 12.5px; color: var(--hd-fg-muted); line-height: 16px; }
.sx .sxleg span { display: inline-flex; align-items: center; gap: 5px; }
.sx .sxhair { height: 3px; border-radius: 2px; background: var(--hd-track); overflow: hidden; }
.sx .sxhair i { display: block; height: 100%; background: var(--hd-accent); border-radius: 2px; }

/* ---- Shell (scoped to the kit section) ---- */
.k-shell .sb { background: var(--hd-surface); padding: 14px 12px; }
.k-shell .sb > img { height: 20px !important; margin: 6px 8px 14px !important; }
.k-shell .ws { height: 52px; padding: 0 8px; border: 1px solid var(--hd-edge); border-radius: 10px; box-shadow: none; background: none; }
.k-shell .ws b { font-size: 14px; } .k-shell .ws small { font-size: 12.5px; color: var(--hd-fg-muted); }
.k-shell .ws .ic { color: var(--hd-fg-muted); }
.k-shell .sbsearch { height: 36px; margin: 10px 0 8px; font-size: 14px; }
.k-shell .sbh { font: 560 12px/16px var(--font-ui); color: var(--hd-fg-subtle); padding: 14px 10px 4px; }
.k-shell .nav { height: 36px; font-size: 14px; border-radius: 8px; gap: 10px; }
.k-shell .nav .ic { width: 18px; height: 18px; color: var(--hd-fg-muted); }
.k-shell .nav .cnt { font-size: 12.5px; font-weight: 500; color: var(--hd-fg-subtle); }
.k-shell .nav.on { background: var(--hd-accent-subtle); box-shadow: none; color: var(--hd-accent-strong, var(--hd-link)); font-weight: 550; }
.k-shell .nav.on .ic, .k-shell .nav.on .cnt { color: var(--hd-accent-strong, var(--hd-link)); }
.k-shell .me { height: 52px; border-top: 0; padding: 0 8px; margin-top: 4px; }
.k-shell .rail .nav { width: 40px; height: 40px; padding: 0; justify-content: center; }
.k-shell .rail .nav.on { background: var(--hd-accent-subtle); border: 0; }
/* top area: bare, no cards */
.k-top { display: flex; flex-direction: column; }
.k-crumb { display: flex; align-items: center; gap: 12px; height: 40px; }
.k-crumb .crumb { font-size: 13.5px; color: var(--hd-fg-muted); } .k-crumb .crumb b { color: var(--hd-fg); font-weight: 550; }
.k-crumb .sp { flex: 1; }
.k-top .ph { align-items: center; margin-top: 8px; }
.k-top .k-h1 { font: 650 24px/30px var(--font-display, var(--font-ui)); letter-spacing: -.03em; }
.k-top .ph .t p { margin: 2px 0 0; font-size: 14px; color: var(--hd-fg-muted); }
.k-top .ph .btn.sm { height: 36px; border-radius: 10px; font-size: 14px; padding: 0 14px; }
.k-top .ph .btn.p.sm:has(> .ic:first-child) { padding-left: 12px; }
.k-top .tabs { margin-top: 16px; display: flex; gap: 24px; border-bottom: 1px solid var(--hd-edge); padding: 0; background: none; }
.k-top .tabs > span { display: inline-flex; align-items: center; gap: 7px; height: 42px; padding: 0; font-size: 14.5px; font-weight: 560; color: var(--hd-fg-muted); border-bottom: 2px solid transparent; margin-bottom: -1px; background: none; box-shadow: none; }
.k-top .tabs > span.on { color: var(--hd-fg); border-bottom-color: var(--hd-accent); }
.k-top .tabs .tc { font-size: 13.5px; font-weight: 500; color: var(--hd-fg-subtle); font-variant-numeric: tabular-nums; }
.k-top .tabs > .on .tc { color: var(--hd-accent-strong, var(--hd-link)); }
.k-shell .cmdk .ci { height: 40px; font-size: 14.5px; border-radius: 8px; }
.k-shell .cmdk .ci .ic { width: 18px; height: 18px; }
.k-shell .cmdk .cgh { font: 560 12px/16px var(--font-ui); color: var(--hd-fg-subtle); padding: 8px 10px 4px; }
.k-shell .cmdk .cin { font-size: 15px; }

/* interaction: skeleton row */
.panel.ix .skrow { display: flex; align-items: center; gap: 12px; height: 64px; padding: 12px; border: 1px solid var(--hd-edge); border-radius: 12px; background: var(--hd-surface); overflow: hidden; }
.panel.ix .skrow .sk-th { flex: none; width: 40px; height: 40px; border-radius: 10px; }
.panel.ix .skrow .sk-ln { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 8px; }
.panel.ix .skrow .skel { display: block; border-radius: 6px; background: color-mix(in oklab, var(--hd-fg) 8%, var(--hd-surface)) !important; }
.k-shell .sb > img { align-self: flex-start; }
.k-shell .sb > img + * { }
.k-shell .sb > img { border: 0 !important; padding: 0 !important; }
.k-shell .sb::before, .k-shell .sb > img::after { display: none !important; }

.k-shell .ws { box-shadow: none !important; background: none !important; }
.k-shell .sb > img { margin-top: 8px !important; }
.arrive { animation-delay: 0s; }
.k-shell .sb { padding-top: 18px; }
[data-theme="dark"] .sx .sxstack i:nth-child(2) { background: color-mix(in oklab, var(--hd-accent) 62%, var(--hd-fg) 10%); }
[data-theme="dark"] .sx .sxstack i:nth-child(3) { background: color-mix(in oklab, var(--hd-accent) 38%, var(--hd-fg) 16%); }

/* ---- Charts v2: big charts ---- */
.chrow { align-items: stretch; }
.panel.cc { padding: 20px; display: flex; flex-direction: column; min-width: 0; }
.cc .chh { display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; margin-bottom: 14px; }
.cc .cht { font-size: 15px; font-weight: 600; letter-spacing: -.005em; }
.cc .chv { display: flex; align-items: baseline; gap: 10px; margin-top: 6px; }
.cc .chv b { font: 650 28px/32px var(--font-ui); letter-spacing: -.03em; }
.cc .chd { font-size: 13px; font-weight: 500; color: var(--hd-success-strong); }
.cc .chl { display: flex; gap: 16px; font-size: 12.5px; color: var(--hd-fg-muted); }
.cc .chl span { display: inline-flex; align-items: center; gap: 6px; }
.sw { display: inline-block; width: 12px; height: 2px; border-radius: 1px; background: var(--hd-chart); flex: none; }
.sw.dash { background: repeating-linear-gradient(90deg, var(--hd-fg-subtle) 0 3px, transparent 3px 5px); }
.cw2 { position: relative; margin-top: auto; }
.chart2 { display: block; overflow: visible; font-family: var(--font-ui); }
.chart2 .g2l { stroke: var(--hd-fg); stroke-opacity: .07; stroke-width: 1; shape-rendering: crispEdges; }
.chart2 .g2t { font-size: 11.5px; fill: var(--hd-fg-subtle); font-variant-numeric: tabular-nums; }
.chart2 .g2s { fill: none; stroke: var(--hd-chart); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.chart2 .g2c { fill: none; stroke: var(--hd-fg-subtle); stroke-width: 1.5; stroke-dasharray: 4 4; }
.chart2 .g2v { stroke: var(--hd-fg); stroke-opacity: .16; stroke-width: 1; }
.chart2 .g2d { fill: var(--hd-chart); stroke: var(--hd-surface); stroke-width: 2; }
.chart2 .g2cd { fill: var(--hd-fg-subtle); }
.chart2 .g2b { fill: color-mix(in oklab, var(--hd-chart) 25%, transparent); }
.chart2 .g2b.cur { fill: var(--hd-chart); }
.chart2 .g2v2 { font-size: 12px; font-weight: 600; fill: var(--hd-fg); font-variant-numeric: tabular-nums; }
.g2tip { position: absolute; width: 176px; padding: 12px; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 12px; box-shadow: var(--hd-shadow-e2, 0 8px 24px -8px rgba(16,20,38,.18)); font-size: 13px; display: flex; flex-direction: column; gap: 6px; }
.g2tip .tt-d { font-size: 12.5px; color: var(--hd-fg-muted); margin-bottom: 2px; }
.g2tip .tt-r { display: flex; align-items: center; gap: 8px; color: var(--hd-fg-muted); }
.g2tip .tt-r b { margin-left: auto; color: var(--hd-fg); font-weight: 600; }

/* ---- Review card + campaign card ---- */
.rcrow { grid-template-columns: minmax(0, 560px) minmax(0, 560px) !important; }
.panel.rcard2 { padding: 16px; display: flex; flex-direction: column; gap: 12px; }
.rcard2 .rh { display: flex; align-items: center; gap: 12px; }
.rcard2 .rp { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; flex: none; }
.rcard2 .rn b { display: inline-flex; align-items: center; gap: 5px; font-size: 15px; font-weight: 600; }
.rcard2 .rm { display: flex; align-items: center; gap: 6px; margin-top: 2px; font-size: 13px; color: var(--hd-fg-muted); }
.rcard2 .rs { display: inline-flex; gap: 1px; color: var(--hd-star); }
.rcard2 .rs .ic { width: 13px; height: 13px; }
.rcard2 .rig { display: inline-flex; align-items: center; gap: 4px; }
.rcard2 p { margin: 0; font-size: 14.5px; line-height: 21px; }
.rcard2 .media { display: flex; gap: 6px; } .rcard2 .media img { width: 72px; height: 72px; border-radius: 10px; object-fit: cover; }
.rcard2 .rprod { display: inline-flex; align-items: center; gap: 8px; font-size: 13px; color: var(--hd-fg-muted); }
.rcard2 .rprod img { width: 20px; height: 20px; border-radius: 4px; object-fit: cover; }
.panel.x-camp2 { grid-template-columns: 148px 1fr !important; }
.x-camp2 > img { width: 148px !important; min-height: 148px; }
.x-camp2 .cbody { padding: 16px; display: flex; flex-direction: column; gap: 6px; min-width: 0; }
.x-camp2 .ctop { display: flex; align-items: center; gap: 8px; font-size: 12.5px; color: var(--hd-fg-muted); }
.x-camp2 .ctitle { font-size: 17px; font-weight: 600; letter-spacing: -.01em; }
.x-camp2 .cmeta { display: flex; align-items: center; gap: 8px; font-size: 13.5px; color: var(--hd-fg-muted); }
.x-camp2 .cmeta b { color: var(--hd-fg); font-weight: 600; }
.x-camp2 .cg { display: inline-flex; gap: 6px; }
.x-camp2 .cprog { margin-top: auto; display: flex; flex-direction: column; gap: 6px; }
.x-camp2 .cprog .tape { height: 3px; }
.x-camp2 .cnum { display: flex; justify-content: space-between; font-size: 12.5px; color: var(--hd-fg-muted); }
"""
