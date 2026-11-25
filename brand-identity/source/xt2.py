# ugly/broken sweep layer 2
XT2 = r"""
/* bell dot: solid danger, not marigold-orange */
.iconbtn .badge-dot { background: var(--hd-danger-solid, #d92d20) !important; }
[data-theme="dark"] .iconbtn .badge-dot { background: #e5484d !important; }
/* chart tooltip clears the series lines */
.cw2 .g2tip { margin-top: 12px; }
/* avatar stack from photos: round, ringed, same overlap as initials */
.avs img.av { object-fit: cover; display: block; border-radius: 50%; }
/* campaign + task cards share the row evenly */
.grid.rcrow { grid-template-columns: 1fr 1fr !important; }
.rcard2 .xt-rf { display: flex; align-items: center; justify-content: space-between; padding-top: 12px; border-top: 1px solid var(--hd-edge); margin-top: 4px; }
/* filter panel: one quiet count, no tinted pill */
.n-fil .n-filh .n-fc { background: transparent !important; padding: 0 !important; color: var(--hd-fg-muted) !important; font-weight: 500; }
/* form section layout fills its card: label column + three even fields */
.sec .n-form .n-fs { grid-template-columns: 260px minmax(0, 1fr) !important; }
.sec .n-form .n-ff { max-width: none !important; }
.sec .n-form .n-fgrid { grid-template-columns: repeat(3, minmax(0, 1fr)) !important; }
/* load-more done state: neutral bar and neutral end label, one signal (the tick) */
.n-more2.done .n-m2bar > i { background: var(--hd-accent) !important; }
.n-more2.done .n-end2 { color: var(--hd-fg-muted) !important; }
.n-more2.done .n-end2 .ic { color: var(--hd-success-solid, #0a8a4a); }
/* menu destructive row stays neutral (red only on the final confirm) */
.menu.n-ctx > div.dg, .menu.n-ctx > div.dg .ic { color: var(--hd-fg) !important; }
.n-asa.dg { color: var(--hd-fg) !important; }
"""
