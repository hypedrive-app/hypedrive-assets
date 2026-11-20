# Finish-gate layer (xe): fixes found on the real screens. Appended after XD.
XE = r"""
/* .t-body is the chat scroll area in the kit; on the app screens it is plain body copy (a textarea keeps its field padding) */
:is(.phone, .desk) .t-body:not(.t-thr .t-body, .input) { padding: 0; display: block; background: none; gap: 0; }
.phone .input.textarea { padding: 12px 14px; }
/* wallet hero: flat Ink in light; in dark the inverse token is white, so it becomes a raised dark card instead */
[data-theme="dark"] .w-hero { --hd-inverse: var(--hd-surface-raised); --hd-inverse-fg: var(--hd-fg); border: 1px solid var(--hd-border); }
/* status bar over a full-bleed product photo: dark text in both themes (the photo is light) */
[data-theme="dark"]:has(> .x-photo) > .sbar:not([style*="color"]) { color: #111; }
/* chip row scrolls to the screen edge instead of cutting a chip inside the margin */
.phone .chiprow { margin-right: -16px; padding-right: 16px; }
/* dark: cobalt tile glyphs use the lighter link tone so they stay legible */
[data-theme="dark"] .x-tile.cobalt { color: var(--hd-link) !important; }
/* home drop card: product card v5 on the app screen. Full-colour photo, one smooth bottom scrim, no top wash; chips and heart on solid discs; content anchored bottom */
.phone .x-hero .sh { height: 100%; background: linear-gradient(180deg, rgba(8,10,16,0) 0%, rgba(8,10,16,0) 38%, rgba(8,10,16,.38) 54%, rgba(8,10,16,.74) 72%, rgba(8,10,16,.90) 100%); }
.phone .x-hero .top .x-disc { width: 36px; height: 36px; }
.phone .x-hero .bt .t { min-width: 0; }
.phone .x-hero .bt .br { margin: 0 0 2px; font-size: 13px; color: rgba(255,255,255,.78); }
.phone .x-hero .bt .mt { margin-top: 4px; font-size: 14px; color: rgba(255,255,255,.86); }
.phone .x-hero .bt .mt em { font-style: normal; font-weight: 650; color: #fff; }
.phone .x-hero .bt .sl { display: block; height: 4px; margin-top: 10px; border-radius: 2px; background: rgba(255,255,255,.28); overflow: hidden; }
.phone .x-hero .bt .sl u { display: block; height: 100%; border-radius: 2px; background: #fff; text-decoration: none; }
"""
