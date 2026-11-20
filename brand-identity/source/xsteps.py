# Steps + progress layer (owned by the steps agent). Appended very last.
# One marker system for every stepper: 24px, done = solid Cobalt + white check, current = 2px Cobalt ring + 8px dot,
# upcoming = 2px neutral outline. One line weight (2px). One bar scale: thin 4, default 8, segmented 10.
XSTEPS = r"""
/* ============================ steppers ============================ */
.n-wz .s .k, .x-tl .s .k i { box-sizing: border-box; width: 24px; height: 24px; border-radius: 50%; border: 2px solid var(--hd-border-strong); background: transparent;
  display: grid; place-items: center; flex: none; color: #fff; box-shadow: none; font-size: 0; }
.n-wz .s .k svg, .x-tl .s .k i svg { display: block; }
.n-wz .s.done .k, .x-tl .s.done .k i { background: var(--hd-accent); border-color: var(--hd-accent); color: #fff; }
.n-wz .s.now .k, .x-tl .s.now .k i { background: transparent; border-color: var(--hd-accent); color: var(--hd-accent); box-shadow: none; }
.n-wz .s.now .k::after, .x-tl .s.now .k i::after { content: ''; width: 8px; height: 8px; border-radius: 50%; background: var(--hd-accent); }

/* horizontal: marker, label, even 12px gaps, one 2px connector */
.n-wz { display: flex; align-items: center; gap: 10px; }
.n-wz .s { display: flex; align-items: center; gap: 10px; white-space: nowrap; flex: none; }
.n-wz .ln { flex: 1 1 0; min-width: 16px; height: 2px; border-radius: 2px; background: var(--hd-border-strong); box-shadow: none; }
.n-wz .ln.done { background: var(--hd-accent); }
.n-st b { display: block; font-size: 14px; line-height: 20px; font-weight: 600; color: var(--hd-fg-muted); }
.n-st small { display: block; font-size: 12px; line-height: 16px; color: var(--hd-fg-subtle); }
.n-wz .s.done .n-st b, .n-wz .s.now .n-st b { color: var(--hd-fg); }
.n-wz .s.now .n-st small, .n-wz .s.done .n-st small { color: var(--hd-fg-muted); }
.n-wz .s:not(:has(small)) .n-st b { line-height: 24px; }
.n-wzcard { container-type: inline-size; padding: 20px 24px; box-sizing: border-box; min-width: 0; overflow: hidden; }
.n-wzcard .n-wz { width: 100%; min-width: 0; justify-content: space-between; }
.n-wz .ln { margin: 0; }
@container (max-width: 600px) { .n-wz .n-st small { display: none; } .n-wz .s .n-st b { line-height: 24px; } }
@container (max-width: 420px) { .n-wz .s:not(.now) .n-st { display: none; } .n-wz { gap: 8px; } .n-wz .ln { min-width: 12px; } }

/* vertical: marker column 24, 12px to the text, the line runs through to the next marker with a 4px gap each end */
.x-tl { display: flex; flex-direction: column; }
.x-tl .s { display: flex; gap: 12px; min-height: 0; padding: 0; }
.x-tl .k { width: 24px; flex: none; display: flex; flex-direction: column; align-items: center; }
.x-tl .k em { flex: 1 1 auto; width: 2px; min-height: 8px; margin: 4px 0; border-radius: 2px; background: var(--hd-border-strong); box-shadow: none; }
.x-tl .s.done .k em { background: var(--hd-accent); }
.box > .x-tl { margin-bottom: 12px; }
.x-tl .tx { flex: 1; min-width: 0; padding-bottom: 20px; }
.x-tl .s:last-child .tx { padding-bottom: 0; }
.x-tl .hd { display: flex; align-items: center; justify-content: space-between; gap: 12px; min-height: 24px; }
.x-tl b { display: block; font-size: 15px; line-height: 24px; font-weight: 600; color: var(--hd-fg); letter-spacing: 0; }
.x-tl small { display: block; font-size: 13px; line-height: 20px; margin-top: 0; color: var(--hd-fg-muted); }
.x-tl .s:not(.done):not(.now) b { color: var(--hd-fg-muted); }
.x-tl .tm { flex: none; font-size: 12px; line-height: 16px; font-weight: 600; padding: 2px 8px; border-radius: 999px; background: var(--hd-accent-subtle); color: var(--hd-link); font-variant-numeric: tabular-nums; }

/* compact phone steppers: segment bar and dots share one rhythm (4px gaps, full round ends, same inset) */
.n-sg { display: flex; gap: 4px; padding: 8px 8px 0; } .n-sg i { flex: 1; height: 4px; border-radius: 999px; background: var(--hd-track); box-shadow: none; }
.n-sg i.on, .n-sg i.cur { background: var(--hd-accent); }
.n-dots2, .x-deck { display: flex; gap: 6px; justify-content: center; align-items: center; } .n-dots2 { padding-top: 8px; height: 14px; box-sizing: content-box; }
.n-dots2 i, .x-deck i { width: 6px; height: 6px; border-radius: 999px; background: var(--hd-border-strong); opacity: 1; flex: none; }
.n-dots2 i.on { background: var(--hd-accent); opacity: 1; } .n-dots2 i.cur, .x-deck i.on { width: 18px; background: var(--hd-accent); opacity: 1; }
.x-dots i { border-radius: 999px; }

/* ============================ linear progress ============================ */
.bar, .tape { height: 8px; border-radius: 999px; background: var(--hd-track); overflow: hidden; box-shadow: inset 0 1px 1px rgba(16,20,38,.08); }
.bar.thin, .tape.thin, .n-t4, .upl .tape, .n-sl .tape, .n-prog .tape, .n-ghost .tape { height: 4px; }
.n-t4 { margin-top: 8px; } .upl .tape { margin-top: 8px; }
.bar i, .tape i { border-radius: 999px; }
.bar:not(.multi) i, .tape i { box-shadow: inset 0 1px 0 rgba(255,255,255,.22), inset 0 -1px 0 rgba(8,16,70,.12); }
.bar.thin i, .tape.thin i, .n-t4 i, .upl .tape i, .n-sl .tape i, .n-prog .tape i { box-shadow: none; }
.bar.multi { gap: 2px; height: 8px; } .stat .vz .bar.multi { height: 8px; }
.cmp2 .bar.thin { height: 4px; border-radius: 999px; } .cmp2 .bar.thin i { border-radius: 999px; box-shadow: none; }
.bar.ok i, .tape.ok i { background: var(--hd-success-solid); } .bar.paused i { background: var(--hd-marigold-300); } .bar.err i { background: var(--hd-danger-solid); }
.barlab { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; font-size: 13px; line-height: 20px; margin-bottom: 8px; }
.barlab b { font-weight: 600; } .barlab span { font-weight: 500; font-variant-numeric: tabular-nums; }
.barlab span.ok { color: var(--hd-success-strong); } .barlab span.err { color: var(--hd-danger-strong); }
.tbl td .tape, .tbl td .bar { display: block; margin: 0; }
/* tape: the brand's pull-tape. A moving diagonal texture only while it is pulling, so the motion reads as progress. */
.tapeanim i { background-image: repeating-linear-gradient(-45deg, rgba(255,255,255,.2) 0 5px, transparent 5px 10px); background-size: 14.142px 14.142px; animation: tapepull 1.6s linear infinite, tapeslide .8s linear infinite; }
@keyframes tapeslide { to { background-position: 14.142px 0; } }
@media (prefers-reduced-motion: reduce) { .tapeanim i { animation: none; width: 60%; } }

/* segmented: cells with a 4px gap and a 4px radius, one partial cell */
.segs { display: flex; gap: 4px; height: 10px; } .segs i { flex: 1; height: 10px; border-radius: 4px !important; background: var(--hd-track); position: relative; overflow: hidden; }
.segs i.on, .segs i b { background: var(--hd-accent); } .segs i b { border-radius: 0; }

/* ring: 4–6px stroke, round cap, centre value */
.ringw svg circle { shape-rendering: geometricPrecision; }
.n-ring circle { vector-effect: non-scaling-stroke; }
"""
