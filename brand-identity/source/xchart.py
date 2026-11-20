# Charts + stat cards layer (owned by the charts agent). Appended after XCOMP.
XCHART = r"""
:root, [data-theme] { --hd-empty: color-mix(in oklab, var(--hd-fg) 20%, var(--hd-surface)); }
/* ===== charts: HTML axis labels (11.5px at any scale), hairline grid, 2px series, 2px surface rings ===== */
.cw { position: relative; line-height: 0; } .cw > svg { display: block; overflow: visible; }
.cw .gl { stroke: var(--hairline); stroke-width: 1; } .cw .gl.base { stroke: var(--hd-border); }
.cw .yl, .cw .xl, .cw .bv { position: absolute; font: 500 11.5px/1 var(--font-ui); color: var(--hd-fg-subtle); font-variant-numeric: tabular-nums; white-space: nowrap; pointer-events: none; }
.cw .yl { transform: translateY(-50%); } .cw .xl { transform: translateX(-50%); } .cw .bv { transform: translate(-50%, -100%); color: var(--hd-fg); font-weight: 600; font-size: 12px; }
.cw .serl { fill: none; stroke: var(--hd-chart); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.cw .cmpl { fill: none; stroke: var(--hd-fg-subtle); stroke-width: 1.5; stroke-dasharray: 2 5; stroke-linecap: round; opacity: .9; }
.cw .xh { stroke: var(--hd-border-strong); stroke-width: 1; }
.cw .avgl { stroke: var(--hd-fg-subtle); stroke-width: 1; stroke-dasharray: 2 4; opacity: .7; }
.cdot { position: absolute; width: 9px; height: 9px; margin: -4.5px 0 0 -4.5px; border-radius: 50%; background: var(--hd-chart); box-shadow: 0 0 0 2px var(--hd-surface); pointer-events: none; }
.cdot.hov { width: 10px; height: 10px; margin: -5px 0 0 -5px; box-shadow: 0 0 0 2px var(--hd-surface), 0 0 0 6px color-mix(in oklab, var(--hd-chart) 20%, transparent); }
.cdot.cmpd { width: 7px; height: 7px; margin: -3.5px 0 0 -3.5px; background: var(--hd-fg-subtle); }
.ctip { transform: translate(-50%, calc(-100% - 16px)); line-height: 1.2; gap: 8px; padding: 7px 11px; } .ctip.below { transform: translate(-50%, 16px); }
.ctip.l { transform: translate(-20%, calc(-100% - 16px)); } .ctip.r { transform: translate(-80%, calc(-100% - 16px)); }
.ctip b { font-family: var(--font-brand); font-size: 15px; letter-spacing: -.02em; }
/* donut */
.dn { position: relative; flex: none; } .dn .dc { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px; }
.dn .dc b { font-family: var(--font-brand); font-size: 30px; font-weight: 600; letter-spacing: -.035em; line-height: 1; }
.dn .dc span { font-size: 12px; line-height: 1; }
.lgd i { border-radius: 3px; width: 10px; height: 10px; }
/* ring */
.ringw { position: relative; display: inline-flex; align-items: center; justify-content: center; flex: none; } .ringw b { font-family: var(--font-brand); font-weight: 600; letter-spacing: -.02em; }
/* ===== stat card anatomy: label row · value · fixed visual zone on the bottom ===== */
.stat:not(.compact) { gap: 0; padding: 14px 16px 16px; }
.stat .sh { align-items: center; min-height: 18px; }
.stat:not(.compact) .sv { align-items: baseline; margin-top: 8px; gap: 6px; }
.stat:not(.compact) .sv b { font-variant-numeric: tabular-nums; }
.stat:not(.compact) .sv .su { font-size: 15px; font-weight: 500; letter-spacing: -.01em; color: var(--hd-fg-muted); }
.stat:not(.compact) .vz { height: auto; min-height: 44px; padding-top: 12px; justify-content: flex-end; container-type: inline-size; }
.dtext { font-size: 12.5px; font-weight: 600; letter-spacing: 0; line-height: 1; }
/* trend */
.stat .vz .spk { height: 36px; border-bottom: 1px solid var(--hairline); } .stat .vz .spk svg { height: 36px; }
.spk-dot { width: 8px; height: 8px; margin-top: -4px; right: -4px; box-shadow: 0 0 0 2px var(--hd-surface), 0 0 0 5px color-mix(in oklab, var(--hd-chart) 20%, transparent); }
/* counts: past periods tinted, current solid, square on a hairline baseline */
.stat .vz .mbars { height: 36px; gap: 6px !important; align-items: flex-end; border-bottom: 1px solid var(--hairline); }
.mbars i { border-radius: 4px 4px 0 0 !important; background: color-mix(in oklab, var(--hd-chart) 32%, var(--hd-surface)) !important; min-height: 3px; } .mbars i.hl { background: var(--hd-chart) !important; }
/* rating: stars + 5-bar distribution */

.stat.k-rating:not(.compact) .vz { flex-direction: row; align-items: flex-end; justify-content: space-between; }
.srate { display: flex; gap: 3px; margin: 0; line-height: 0; } .srate .pst { width: 19px; height: 19px; display: block; }
.rhist { display: none; align-items: flex-end; gap: 4px; height: 30px; } .rhist i { width: 6px; min-height: 4px; border-radius: 3px 3px 0 0; background: color-mix(in oklab, var(--hd-chart) 26%, var(--hd-surface)); } .rhist i.hl { background: var(--hd-chart); }
@container (min-width: 190px) { .rhist { display: flex; } }
/* compare */
.stat .vz .cmp2 { gap: 7px; } .cmp2 > div { grid-template-columns: 42px 1fr 58px; gap: 10px; font-size: 12px; line-height: 1; }
.cmp2 .bar.thin { height: 6px; border-radius: 3px; background: transparent; } .cmp2 .bar.thin i { border-radius: 3px; background: var(--hd-chart); }
.cmp2 .pv .bar.thin i { background: var(--hd-empty); }
.cmp2 b { text-align: right; font-size: 12.5px; font-weight: 600; color: var(--hd-fg); } .cmp2 .pv b { font-weight: 500; color: var(--hd-fg-muted); }
/* split */
.stat .vz .bar.multi { height: 8px; gap: 2px; border-radius: 0; overflow: visible; } .bar.multi i { border-radius: 3px; } .bar.multi i:first-child { border-radius: 999px 3px 3px 999px; } .bar.multi i:last-child { border-radius: 3px 999px 999px 3px; }
.stat .vz .bar.multi + .legend { margin-top: 10px; gap: 4px 12px; flex-wrap: wrap; font-size: 12px; line-height: 1.1; }
.stat .legend i { width: 8px; height: 8px; margin-right: 5px; vertical-align: 0; border-radius: 3px; }
/* goal */
.k-goal .segs { height: 10px; gap: 4px; } .segs i { border-radius: 3px; }
.k-goalring .gr { display: flex; align-items: center; justify-content: space-between; margin-top: 4px; } .k-goalring .gr .sv { margin-top: 0 !important; min-width: 0; }
.k-goalring .ringw b { font-size: 13px !important; }
.segs i.on, .segs i b { background: var(--hd-chart); }
"""
