# Second-pass audit layer (xf). Appended after XE. CSS only.
XF = r"""
/* primitives: elevation tiles keep one 1px border; the token's ring would double it */
div[style*="--hd-shadow-e1"] { box-shadow: 0 1px 2px rgba(16,20,38,.05), 0 2px 4px -1px rgba(16,20,38,.045) !important; }
div[style*="--hd-shadow-e2"] { box-shadow: 0 1px 2px rgba(16,20,38,.06), 0 4px 8px -2px rgba(16,20,38,.07), 0 12px 16px -4px rgba(16,20,38,.09) !important; }
div[style*="--hd-shadow-e3"] { box-shadow: 0 2px 4px rgba(16,20,38,.05), 0 8px 16px -2px rgba(16,20,38,.08), 0 24px 40px -8px rgba(16,20,38,.12) !important; }
[data-theme="dark"] div[style*="--hd-shadow-e1"] { box-shadow: 0 1px 2px rgba(0,0,0,.45), 0 2px 4px -1px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.05) !important; }
[data-theme="dark"] div[style*="--hd-shadow-e2"] { box-shadow: 0 1px 2px rgba(0,0,0,.5), 0 4px 8px -2px rgba(0,0,0,.45), 0 12px 16px -4px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.07) !important; }
[data-theme="dark"] div[style*="--hd-shadow-e3"] { box-shadow: 0 2px 4px rgba(0,0,0,.5), 0 8px 16px -2px rgba(0,0,0,.5), 0 24px 40px -8px rgba(0,0,0,.6), inset 0 1px 0 rgba(255,255,255,.08) !important; }

/* buttons: one glyph size inside a button; focus ring gap matches the box it sits in; dark focus rings; dark danger hover/pressed */
.btn .ic { width: 20px; height: 20px; }
.btn.sm .ic { width: 18px; height: 18px; }
.box .btn.foc { --ring-gap: var(--hd-bg-subtle); }
[data-theme="dark"] .box .btn.foc { --ring-gap: var(--hd-bg); }
[data-theme="dark"] .btn.p.foc:not(.dis):not([disabled]), [data-theme="dark"] .btn.d.foc:not(.dis):not([disabled]) { box-shadow: inset 0 1px 0 rgba(255,255,255,.18), 0 0 0 2px var(--ring-gap, var(--hd-bg)), 0 0 0 4px var(--hd-focus) !important; }
[data-theme="dark"] .btn.s.foc:not(.dis):not([disabled]), [data-theme="dark"] .btn.g.foc:not(.dis):not([disabled]) { box-shadow: 0 0 0 2px var(--ring-gap, var(--hd-bg)), 0 0 0 4px var(--hd-focus) !important; }
[data-theme="dark"] .btn.d.hov:not(.dis):not([disabled]) { background: color-mix(in oklab, var(--hd-danger-solid, #c93d00) 86%, #000) !important; }
[data-theme="dark"] .btn.d.prs:not(.dis):not([disabled]), [data-theme="dark"] .btn.d:active:not(.dis):not([disabled]) { background: color-mix(in oklab, var(--hd-danger-solid, #c93d00) 72%, #000) !important; }

/* inputs: codes read in Geist, never a monospace face; OTP cells get a real 1px border */
.mono { font-family: var(--font-ui) !important; font-size: inherit !important; font-variant-numeric: tabular-nums; letter-spacing: .02em; }
.otp2 span { box-sizing: border-box; border: 1px solid var(--hd-border-input); box-shadow: none !important; }
.otp2 span.f { border-color: var(--hd-border-strong); }
.otp2 span.on { border-color: var(--hd-focus); box-shadow: inset 0 0 0 1px var(--hd-focus) !important; }

/* data display / interaction: skeleton blocks stay visible on a dark row */
[data-theme="dark"] .row .skel, [data-theme="dark"] .panel .skel { background: color-mix(in oklab, var(--hd-fg) 16%, var(--hd-surface)) !important; }
[data-theme="dark"] .row .skel.shimmer, [data-theme="dark"] .panel .skel.shimmer { background: color-mix(in oklab, var(--hd-fg) 16%, var(--hd-surface)) !important; }

/* tables: dark rows keep their dividers */
[data-theme="dark"] .tbl td, [data-theme="dark"] .tbl th { border-bottom-color: var(--hd-edge); }
[data-theme="dark"] .tbl tr:last-child td { border-bottom: 0; }

/* charts: dark past periods and unfilled segments hold contrast against the card */
[data-theme="dark"] svg.chart path[style*="28%"] { fill: color-mix(in oklab, var(--hd-chart) 38%, var(--hd-surface)) !important; }
[data-theme="dark"] .mbars i:not(.hl) { background: color-mix(in oklab, var(--hd-chart) 38%, var(--hd-surface)) !important; }
[data-theme="dark"] .segs i.on { background: var(--hd-chart) !important; }

/* date range: tinted days use the -strong text */
.cg .rng { color: var(--hd-info-strong); }

/* action sheet: the row behind the gap between groups does not peek through */
div:has(+ .n-scrim) > .row:last-child { visibility: hidden; }

/* tabs: the underline is a painted strip, not an inset shadow (a fractional tab width drew a stray vertical hairline); no negative tracking on tab labels */
.tabs > span { letter-spacing: 0; }
.tabs > span.on { box-shadow: none !important; background: linear-gradient(var(--hd-indicator, var(--hd-accent)), var(--hd-indicator, var(--hd-accent))) left bottom / 100% 2px no-repeat; }

/* command palette: the highlighted row stays visible on a dark surface */
[data-theme="dark"] .cmdk .ci.hl { background: color-mix(in oklab, var(--hd-fg) 7%, var(--hd-surface)); }

/* notices v2 (lead): calm — light status wash + faint status edge, fg text, status-coloured solid glyph. Chips/badges keep the deeper tints. */
.notice { background: color-mix(in oklab, var(--n-c) 7%, var(--hd-surface)) !important; border: 1px solid color-mix(in oklab, var(--n-c) 22%, var(--hd-surface)) !important; color: var(--hd-fg) !important;
  border-radius: 12px !important; padding: 11px 14px !important; gap: 10px !important; font-size: 14px !important; line-height: 20px !important; align-items: flex-start !important; box-shadow: none !important; }
.notice > svg, .notice > .ic { color: var(--n-c) !important; flex: none; margin-top: 1px; width: 18px; height: 18px; }
.notice.info { --n-c: var(--hd-info, var(--hd-accent)); } .notice.warning, .notice.warn { --n-c: var(--hd-warning-solid, #c27a00); }
.notice.success { --n-c: var(--hd-success, #0a8a4a); } .notice.danger { --n-c: var(--hd-danger-solid, #c93d00); }
.notice:not(.info):not(.warning):not(.warn):not(.success):not(.danger) { --n-c: var(--hd-accent); }
[data-theme="dark"] .notice { background: color-mix(in oklab, var(--n-c) 12%, var(--hd-surface)) !important; border-color: color-mix(in oklab, var(--n-c) 32%, var(--hd-surface)) !important; }

.notice span, .notice b, .notice p { color: var(--hd-fg) !important; }

.sec .xa-rcap { height: 40px; display: flex; flex-direction: column; justify-content: flex-end; gap: 8px; font-size: 12.5px; color: var(--hd-fg-muted); font-variant-numeric: tabular-nums; }
.sec .xa-rbar { display: block; height: 3px; border-radius: 3px; background: var(--hd-track, rgba(16,20,38,.1)); overflow: hidden; } .sec .xa-rbar b { display: block; height: 100%; background: var(--hd-accent); border-radius: 3px; }
/* avatar stack: earlier avatars sit on top so initials stay readable; +9 tucks underneath */
.sec .xa-stack > * { position: relative; } .sec .xa-stack > *:nth-child(1) { z-index: 4; } .sec .xa-stack > *:nth-child(2) { z-index: 3; } .sec .xa-stack > *:nth-child(3) { z-index: 2; } .sec .xa-stack > *:nth-child(4) { z-index: 1; }

/* owner rule: no tinted borders — notices are a tint fill only */
.notice { border: 0 !important; background: color-mix(in oklab, var(--n-c) 11%, var(--hd-surface)) !important; }
[data-theme="dark"] .notice { border: 0 !important; background: color-mix(in oklab, var(--n-c) 17%, var(--hd-surface)) !important; }

/* no tinted borders: tinted surfaces are fill-only; edges stay neutral */
.n-it.unread { border-color: var(--hd-edge) !important; }
.n-tgm span.on, .n-tgm > span.on { border-color: transparent !important; }
.u-dz.drag .u-ic { border-color: var(--hd-edge) !important; }
.n-ft.err { border-color: var(--hd-edge) !important; }
.input.ok { border-color: var(--hd-edge, var(--hd-border)) !important; }
.x-tip { border-left: 0 !important; padding-left: 0 !important; }
.card.n-pc .badge, .badge { border: 0 !important; box-shadow: none !important; }
"""
