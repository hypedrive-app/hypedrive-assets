# mobile screens redesign layer 3: success, notifications, profile, empty search. Every selector is xm3- scoped.
XM3 = r"""
/* shared: these four screens sit on the plain surface, not the grey canvas */
.scr:has(.xm3-s) { background: var(--hd-surface); }
.xm3-s { background: transparent; }
.xm3-s h1, .xm3-s h2, .xm3-s p { margin: 0; }

/* ---------- success ---------- */
.xm3-succ { align-items: center; justify-content: center; text-align: center; gap: 0; padding-bottom: 72px; }
.xm3-succ img { width: 160px; height: auto; display: block; margin-bottom: 24px; }
.xm3-h { font-family: var(--font-brand); font-variation-settings: 'opsz' 96; font-size: 32px; line-height: 36px; font-weight: 650; letter-spacing: -0.03em; color: var(--hd-fg); }
.xm3-fact { margin-top: 12px !important; font-size: 15px; line-height: 22px; color: var(--hd-fg-muted); max-width: 300px; text-wrap: balance; }
.xm3-fact b { color: var(--hd-fg); font-weight: 650; }
.xm3-cta { border: 0 !important; background: transparent !important; flex-direction: column; gap: 10px; padding: 12px 18px 8px; }

/* ---------- notifications: rows sit on the surface, the white tile is the only container ---------- */
.xm3-notifs { gap: 0; padding-top: 6px; }
.xm3-day { font-size: 13px; line-height: 18px; font-weight: 560; color: var(--hd-fg-muted); margin: 14px 0 6px; }
.xm3-day:first-child { margin-top: 4px; }
.xm3-nl { display: flex; flex-direction: column; }
.xm3-nr { display: flex; align-items: center; gap: 12px; height: 64px; }
.xm3-nr .x-tile { width: 40px; height: 40px; flex: none; display: inline-grid; place-items: center; border-radius: 12px; }
.xm3-nt { flex: 1; min-width: 0; }
.xm3-nt p { font-size: 14.5px; line-height: 20px; color: var(--hd-fg); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.xm3-nt p b { font-weight: 600; }
.xm3-nt small { display: block; margin-top: 1px; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.xm3-ne { display: flex; align-items: center; gap: 8px; flex: none; align-self: flex-start; padding-top: 10px; font-size: 12.5px; line-height: 20px; color: var(--hd-fg-subtle); }
.xm3-ne i { width: 8px; height: 8px; border-radius: 50%; background: transparent; }
.xm3-ne i.on { background: var(--hd-accent); }
[data-theme="dark"] .xm3-ne i.on { background: var(--hd-link); }

/* link buttons on these screens: quiet, no underline */
.scr:has(.xm3-s) .btn.link { text-decoration: none; font-weight: 560; }

/* ---------- profile ---------- */
.xm3-top { height: 44px; }
.xm3-top .ttl { flex: 1; }
.xm3-prof { gap: 24px; padding-top: 2px; }
.xm3-id { display: flex; align-items: center; gap: 16px; }
.xm3-id img { width: 64px; height: 64px; border-radius: 50%; object-fit: cover; flex: none; }
.xm3-nm { display: flex; align-items: center; gap: 6px; font-family: var(--font-brand); font-variation-settings: 'opsz' 96; font-size: 24px; line-height: 28px; font-weight: 650; letter-spacing: -0.025em; color: var(--hd-fg); }
.xm3-nm .vhex { flex: none; }
.xm3-id span { display: block; margin-top: 2px; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.xm3-stats { display: flex; gap: 32px; }
.xm3-stats b { display: block; font-size: 18px; line-height: 22px; font-weight: 600; letter-spacing: -0.01em; color: var(--hd-fg); }
.xm3-stats small { display: block; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.xm3-grp { background: var(--hd-surface-raised); border: 1px solid var(--hd-edge); border-radius: 14px; overflow: hidden; }
.xm3-gi { display: flex; align-items: center; gap: 12px; height: 52px; padding: 0 14px; position: relative; }
.xm3-gi + .xm3-gi::before { content: ''; position: absolute; top: 0; left: 46px; right: 0; height: 1px; background: var(--hd-edge); }
.xm3-gi > .ic:first-child { color: var(--hd-fg-muted); flex: none; }
.xm3-gi b { flex: 1; font-size: 15px; line-height: 22px; font-weight: 500; color: var(--hd-fg); }
.xm3-gi .meta { font-size: 13.5px; color: var(--hd-fg-muted); }
.xm3-gi .chevr { color: var(--hd-fg-subtle); display: inline-flex; }
.xm3-gi svg + svg, .xm3-gi svg + .chevr { flex: none; }
.xm3-out { display: flex; align-items: center; gap: 12px; height: 48px; padding: 0 15px; margin-top: -4px; color: var(--hd-danger-strong); }
.xm3-out b { font-size: 15px; font-weight: 500; }
.xm3-out .ic { color: inherit; }

/* ---------- empty search ---------- */
.xm3-emp { gap: 24px; padding-top: 8px; }
.xm3-nil { display: flex; flex-direction: column; align-items: center; text-align: center; }
.xm3-nil img { width: 88px; height: auto; margin-bottom: 8px; }
.xm3-nil h2 { font-family: var(--font-brand); font-variation-settings: 'opsz' 96; font-size: 22px; line-height: 26px; font-weight: 650; letter-spacing: -0.025em; color: var(--hd-fg); }
.xm3-nil p { margin-top: 6px; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.xm3-nil .btn { margin-top: 16px; }
.xm3-sec { display: flex; flex-direction: column; gap: 10px; }
.xm3-sec > b, .xm3-sh b { font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.xm3-sh { display: flex; align-items: center; justify-content: space-between; }
.xm3-chips { display: flex; gap: 8px; overflow: hidden; white-space: nowrap; margin-right: -18px; }
.xm3-chips span { display: inline-flex; align-items: center; gap: 6px; height: 36px; padding: 0 12px 0 10px; border-radius: 10px; background: var(--hd-surface); border: 1px solid var(--hd-edge); color: var(--hd-fg-muted); font-size: 14px; font-weight: 560; flex: none; }
.xm3-chips span .ic { color: var(--hd-fg-subtle); }
[data-theme="dark"] .xm3-chips span { background: var(--hd-surface-raised); }
.xm3-ll { display: flex; flex-direction: column; gap: 8px; }
.xm3-lr { display: flex; align-items: center; gap: 12px; height: 64px; padding: 0 14px 0 8px; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 14px; }
[data-theme="dark"] .xm3-lr { background: var(--hd-surface-raised); }
.xm3-lr img { width: 48px; height: 48px; object-fit: cover; border-radius: 8px; flex: none; }
.xm3-lt { flex: 1; min-width: 0; }
.xm3-lt b { display: block; font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.xm3-lt small { display: block; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.xm3-amt { font-size: 15px; font-weight: 600; color: var(--hd-success); }
"""
