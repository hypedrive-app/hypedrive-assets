# ugly/broken sweep layer 1
XT1 = r"""
/* danger = a true red in the kit's first seven sections (the token reads orange) */
:root, .sec, .phone .scr[data-theme="light"] { --hd-danger: #d92d20; --hd-danger-strong: #b42318; --hd-danger-solid: #d92d20; --hd-danger-subtle: color-mix(in oklab, #d92d20 13%, #fff); }
[data-theme="dark"], [data-theme="dark"] .sec, .phone .scr[data-theme="dark"] { --hd-danger: #ff6a6f; --hd-danger-strong: #ffa3a6; --hd-danger-solid: #e5484d; --hd-danger-subtle: color-mix(in oklab, #e5484d 26%, #16181d); }
/* buttons: the 48 phone-bar size is real */
html body .sec .btn.xt1-bar:not(.sm) { height: 48px !important; border-radius: 12px !important; }
/* cards size to their content, no dead space */
.sec:nth-of-type(3) > .grid, .sec:nth-of-type(4) > .grid, .sec:nth-of-type(5) > .grid, .sec:nth-of-type(6) > .grid { align-items: start; }
/* data display */
.sec .row img.lead.xt1-ava { border-radius: 50%; }
.sec .xa-d2 .xa-stats { flex-direction: row; gap: 12px; }
.sec .xa-d2 .xa-stats > .panel { flex: 1 1 0; min-width: 0; }
.sec .xa-d2 .xa-stats .stat .vz { height: auto; min-height: 0; padding-top: 0; margin-top: 8px; }
.sec .xt1-spots { padding: 16px; }
.sec .xt1-spots .sv { margin-top: 6px; display: flex; align-items: baseline; gap: 8px; }
.sec .xt1-spots .sv b { font: 650 28px/32px var(--font-ui); letter-spacing: -.03em; }
.sec .xt1-spots .su { font-size: 14px; color: var(--hd-fg-muted); }
.sec .xt1-bar3 { height: 3px; border-radius: 2px; background: var(--hd-edge); margin-top: 14px; overflow: hidden; }
.sec .xt1-bar3 i { display: block; height: 100%; background: var(--hd-accent); border-radius: 2px; }
"""
