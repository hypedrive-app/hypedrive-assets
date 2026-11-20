# final pass layer 2
XQ2 = r"""
/* r1: selected review rows are fill-only (no tinted edge) */
:root:root .shell .rc2.chk { border-color: transparent !important; }
/* r1: the average-rating mini histogram carries nothing the stars do not */
:root:root .shell .stat .rhist { display: none !important; }
/* r1: header controls on desktop pages are white hairline controls, not grey slabs */
:root:root .shell .ph .chip, :root:root .shell .ph .search { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge) !important; box-shadow: none !important; }
/* r1: swipe Delete is the true danger red */
:root:root .n-sw .n-swa .a.dg { background: var(--btn-red) !important; }
/* r1: the three compact steppers share one height */
:root:root .n-mrow { align-items: stretch; }
/* r2: filter chips in the desktop toolbar are white hairline too; review rows size to their content */
:root:root .shell .toolbar .chip { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge) !important; box-shadow: none !important; }
:root:root .shell .rc2 { height: auto !important; min-height: 92px; padding: 14px 16px !important; }
/* r3: the full-campaign banner glyph is a warning, so it takes the warning colour, not the accent */
:root:root .shell .banner .bi, :root:root .shell .banner .bi svg { color: var(--hd-tone-marigold) !important; }
"""
