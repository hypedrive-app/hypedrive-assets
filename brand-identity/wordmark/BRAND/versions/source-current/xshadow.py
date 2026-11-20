# Shadow layer (owned by the shadows agent). Appended after XCSS, wins.
XSHADOW = r"""
/* ---- one elevation system. L0 in-flow hairline + contact, L1 raised, L2 menus/toasts, L3 sheets/dialogs ---- */
:root, [data-theme="light"] {
  --hd-edge: rgba(16,20,38,.16);
  --hd-edge-2: rgba(16,20,38,.14);
  --hd-shadow-e1: 0 0 0 1px var(--hd-edge), 0 1px 2px rgba(16,20,38,.05), 0 2px 4px -1px rgba(16,20,38,.045);
  --hd-shadow-e2: 0 0 0 1px var(--hd-edge-2), 0 1px 2px rgba(16,20,38,.06), 0 4px 8px -2px rgba(16,20,38,.07), 0 12px 16px -4px rgba(16,20,38,.09);
  --hd-shadow-e3: 0 0 0 1px var(--hd-edge-2), 0 2px 4px rgba(16,20,38,.05), 0 8px 16px -2px rgba(16,20,38,.08), 0 24px 40px -8px rgba(16,20,38,.12);
}
[data-theme="dark"] {
  --hd-edge: rgba(255,255,255,.12);
  --hd-edge-2: rgba(255,255,255,.13);
  --hd-shadow-e1: 0 0 0 1px var(--hd-edge), 0 1px 2px rgba(0,0,0,.45), 0 2px 4px -1px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.05);
  --hd-shadow-e2: 0 0 0 1px var(--hd-edge-2), 0 1px 2px rgba(0,0,0,.5), 0 4px 8px -2px rgba(0,0,0,.45), 0 12px 16px -4px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.07);
  --hd-shadow-e3: 0 0 0 1px var(--hd-edge-2), 0 2px 4px rgba(0,0,0,.5), 0 8px 16px -2px rgba(0,0,0,.5), 0 24px 40px -8px rgba(0,0,0,.6), inset 0 1px 0 rgba(255,255,255,.08);
}
.sq-bg { overflow: visible; }

/* payout ticket: notched shape, so the edge is drawn by chained drop-shadows that follow the notches (no mask) */
.ticket { filter: drop-shadow(0 0 .5px rgba(16,20,38,.55)) drop-shadow(0 0 .5px rgba(16,20,38,.35)) drop-shadow(0 1px 1px rgba(16,20,38,.06)) drop-shadow(0 2px 3px rgba(16,20,38,.05)); }
[data-theme="dark"] .ticket { filter: drop-shadow(0 0 .5px rgba(255,255,255,.55)) drop-shadow(0 0 .5px rgba(255,255,255,.3)) drop-shadow(0 1px 2px rgba(0,0,0,.5)); }
"""
