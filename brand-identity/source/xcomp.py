# Component refinement layer (owned by the components agent). Appended last.
XCOMP = r"""
/* ===== XCOMP r1 ===== */
.lblgap { display: flex; flex-direction: column; gap: 0; }
.typewt { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
.typewt span { display: flex; flex-direction: column; gap: 2px; font-size: 14px; padding: 10px 12px; border-radius: 10px; background: var(--hd-surface-raised); box-shadow: 0 0 0 1px var(--hairline); }
.typewt small { font-size: 12px; font-weight: 400; color: var(--hd-fg-muted); }

/* control rows: one rhythm for checkbox / radio / switch */
.flexw:has(> .check, > .radio, > .switch) { gap: 10px; min-height: 28px; }
.flexw:has(> .check, > .radio, > .switch) > .t-body { font-size: 15px; line-height: 20px; }
.flexw:has(> .check, > .radio, > .switch) > .t-body + :is(.check, .radio, .switch) { margin-left: 18px; }
.box.stack:has(> .flexw > .switch) { gap: 16px; }

/* avatar stack: a plain surface ring, no mask cut-out */
.avs .av { -webkit-mask: none !important; mask: none !important; margin-left: -8px; box-shadow: 0 0 0 2px var(--avs-ring, var(--hd-surface)) !important; }
.avs .av:first-child { margin-left: 0; }
.box .avs { --avs-ring: var(--hd-canvas); }

/* tab counts: tint, no outline */
.cnt-b { box-shadow: none !important; background: var(--hd-control); color: var(--hd-fg-muted); }
.tabs > .on .cnt-b { background: var(--hd-accent); color: #fff; }

/* breadcrumb chevrons read as separators */
.flexw.t-small > .ic { color: var(--hd-fg-subtle); width: 14px; height: 14px; }

/* calendar range: connected band with rounded ends */
.cal .cg { gap: 2px 0; }
.cal .cg span { border-radius: 10px; }
.cal .cg .rng { background: var(--hd-accent-subtle); color: var(--hd-link); border-radius: 0; }
.cal .cg .sel { position: relative; z-index: 1; }
.cal .cg .today { box-shadow: inset 0 0 0 1px var(--hd-border-strong); }

/* toast stack: peeking cards of the same material */
.toasts { height: 84px; }
.toasts .toast:nth-child(1) { transform: translateY(-14px) scale(.88); opacity: 1; filter: brightness(1.0); z-index: 1; box-shadow: var(--hd-shadow-e1) !important; }
.toasts .toast:nth-child(1) { color: transparent; } .toasts .toast:nth-child(1) > :not(svg) { opacity: 0; }
.toasts .toast:nth-child(2) { transform: translateY(-7px) scale(.94); opacity: 1; z-index: 2; box-shadow: var(--hd-shadow-e1) !important; }
.toasts .toast:nth-child(2) { color: transparent; } .toasts .toast:nth-child(2) > :not(svg) { opacity: 0; }
.toasts .toast:nth-child(3) { z-index: 3; }

/* menu: a divider before the destructive item */
.menu .dg { margin-top: 5px; position: relative; }
.menu .dg::before { content: ''; position: absolute; left: 6px; right: 6px; top: -3px; height: 1px; background: var(--hairline); }

/* ===== XCOMP r3 ===== */
/* skeleton: a flat resting fill, no hard gradient band (shimmer only when .shimmer is set) */
.skel { background: var(--hd-skeleton) !important; }
.skel.shimmer { background: linear-gradient(90deg, var(--hd-skeleton), var(--hd-skeleton-hi), var(--hd-skeleton)) !important; }
[data-theme="dark"] .notice.info .icf { color: var(--hd-info); }

.tbl td, .tbl th { border-bottom-color: var(--hd-border); }
.tbl th { font-weight: 560; }
.tbl tbody tr:hover td, .tbl tr:not(:first-child):hover td { background: color-mix(in oklab, var(--hd-fg) 3%, transparent); }
.hdr .crumb, .flexw.t-small { gap: 4px; }

/* partial star: stop-color attributes cannot read CSS variables in Gecko, so set them as properties */
.pst stop:first-child { stop-color: var(--hd-star); } .pst stop:last-child { stop-color: var(--hd-empty, var(--hd-track-strong)); }

/* a header shown inside a framed panel: the panel is the edge */
.panel > .hdr { border-bottom: 0 !important; }

/* radius scale lock: nothing between the stated steps */
.mbars i, .rhist i, .stat .cmp2 i, .bar.multi i:not(:first-child):not(:last-child), .otp2 i { border-radius: 4px; }
.sheetdemo { border-radius: 24px; }

.sec :is(.rhist, .segs, .mbars) i, .sec .legend i, .sec .lgd i, .sec .bar.multi i:not(:first-child):not(:last-child) { border-radius: 4px !important; }
.sec .sheetdemo { border-radius: 24px !important; }

.sec .bar.multi i:first-child { border-radius: 999px 4px 4px 999px !important; } .sec .bar.multi i:last-child { border-radius: 4px 999px 999px 4px !important; }
"""
