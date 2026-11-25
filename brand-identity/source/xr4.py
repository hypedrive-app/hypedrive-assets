# design-system-by-logic layer 4
XR4 = r"""
.mn-sec .mn-grid3 { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 24px; margin-bottom: 28px; align-items: stretch; }
.mn-sec .mn-grid2 { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 24px 32px; margin-bottom: 28px; align-items: start; }
.mn-sec .mn-grid1 { margin-bottom: 28px; }
.mn-sec .mn-blk { display: flex; flex-direction: column; gap: 10px; min-width: 0; }
.mn-sec .mn-blk .lbl { margin: 0; }
.mn-sec .mn-card { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 12px; box-shadow: none; }
.mn-sec .mn-stack { display: flex; flex-direction: column; gap: 8px; }
.mn-sec .num { font-variant-numeric: tabular-nums; }
.mn-sec .mn-rt { display: flex; flex-direction: column; min-width: 0; flex: 1; }
.mn-sec .mn-rt b { font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.mn-sec .mn-rt small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.mn-sec .mn-help { font-size: 13px; color: var(--hd-fg-muted); }
/* hero */
.mn-sec .mn-hero { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; padding: 20px; display: flex; flex-direction: column; align-items: flex-start; gap: 4px; }
.mn-sec .mn-hl { font-size: 14px; color: var(--hd-fg-muted); font-weight: 500; }
.mn-sec .mn-hn { font-family: var(--font-brand); font-size: 44px; line-height: 52px; font-weight: 700; letter-spacing: -.03em; color: var(--hd-fg); }
.mn-sec .mn-hero.neg .mn-hn { color: var(--hd-danger-strong); }
.mn-sec .mn-hold { display: inline-flex; align-items: center; gap: 2px; font-size: 14px; color: var(--hd-fg-muted); font-weight: 500; cursor: pointer; }
.mn-sec .mn-hold .ic { color: var(--hd-fg-subtle); }
.mn-sec .mn-hs { font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); margin-top: 2px; }
.mn-sec .mn-hb { margin-top: auto; padding-top: 16px; }
.mn-sec .mn-grid3 .mn-blk > .mn-hero { flex: 1; }
.mn-sec .mn-stack2 { gap: 24px; }
.mn-sec .mn-stack2 > .mn-blk { gap: 10px; }
/* states strip */
.mn-sec .mn-strip { display: grid; grid-template-columns: repeat(5, minmax(0,1fr)); }
.mn-sec .mn-sc { padding: 16px 18px; display: flex; flex-direction: column; gap: 4px; border-right: 1px solid var(--hd-edge); }
.mn-sec .mn-sc.last { border-right: 0; }
.mn-sec .mn-sl { font-size: 13.5px; font-weight: 600; color: var(--hd-fg-muted); }
.mn-sec .mn-sv { font-family: var(--font-brand); font-size: 26px; line-height: 32px; font-weight: 700; letter-spacing: -.02em; color: var(--hd-fg); }
.mn-sec .mn-sh { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
/* chips, rows */
.mn-sec .mn-chips { display: flex; gap: 8px; flex-wrap: wrap; }
.mn-sec .mn-chip { height: 36px; padding: 0 14px; border-radius: 10px; display: inline-flex; align-items: center; font-size: 14px; font-weight: 600; color: var(--hd-fg-muted); background: var(--hd-surface); border: 1px solid var(--hd-edge); }
.mn-sec .mn-chip.on { background: var(--hd-accent-subtle); color: var(--hd-link); border-color: transparent; }
.mn-sec .mn-list { overflow: hidden; }
.mn-sec .mn-row { display: flex; align-items: center; gap: 12px; min-height: 60px; padding: 8px 14px; border-top: 1px solid var(--hd-edge); }
.mn-sec .mn-list > .mn-row:first-child { border-top: 0; }
.mn-sec .mn-row.sel { background: var(--hd-bg-subtle); }
.mn-sec .mn-gl { width: 40px; height: 40px; border-radius: 10px; display: inline-flex; align-items: center; justify-content: center; flex: none; color: var(--hd-fg-muted); }
.mn-sec .mn-gl.bankt { color: inherit; }
.mn-sec .mn-amt { font-size: 15px; font-weight: 600; min-width: 72px; text-align: right; color: var(--hd-success-strong); }
.mn-sec .mn-amt.out { color: var(--hd-fg); }
.mn-sec .mn-amt.off { color: var(--hd-fg-subtle); text-decoration: line-through; }
.mn-sec .mn-states { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.mn-sec .mn-more { color: var(--hd-fg-subtle); display: inline-flex; }
.mn-sec .mn-so { font-weight: 500; color: var(--hd-fg-muted); font-size: 13px; margin-left: 8px; }
/* receipt */
.mn-sec .mn-rc { padding: 16px; display: flex; flex-direction: column; gap: 12px; }
.mn-sec .mn-rh { display: flex; align-items: center; gap: 12px; }
.mn-sec .mn-rbig { font-family: var(--font-brand); font-size: 36px; line-height: 40px; font-weight: 700; letter-spacing: -.03em; }
.mn-sec .mn-rd { margin: 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.mn-sec .mn-lns { display: flex; flex-direction: column; border-top: 1px solid var(--hd-edge); }
.mn-sec .mn-ln { display: flex; justify-content: space-between; gap: 16px; padding: 9px 0; font-size: 14px; border-bottom: 1px solid var(--hd-edge); color: var(--hd-fg); }
.mn-sec .mn-ln > span:first-child { color: var(--hd-fg-muted); }
.mn-sec .mn-ln .b { font-weight: 700; }
.mn-sec .mn-lns.tight .mn-ln:last-child { border-bottom: 0; }
.mn-sec .mn-ra { display: flex; gap: 8px; }
/* flow */
.mn-sec .mn-flow { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 16px; }
.mn-sec .mn-panel { display: flex; flex-direction: column; }
.mn-sec .mn-ph { display: flex; align-items: center; gap: 10px; padding: 14px 16px; border-bottom: 1px solid var(--hd-edge); }
.mn-sec .mn-ph b { font-size: 15px; font-weight: 600; }
.mn-sec .mn-step { width: 22px; height: 22px; border-radius: 999px; background: var(--hd-control); color: var(--hd-fg-muted); font-size: 12px; font-weight: 600; display: inline-flex; align-items: center; justify-content: center; }
.mn-sec .mn-pb { padding: 16px; display: flex; flex-direction: column; gap: 10px; flex: 1; }
.mn-sec .mn-pf { padding: 0 16px 16px; display: flex; }
.mn-sec .mn-pf .btn { flex: 1; }
.mn-sec .mn-amtf { display: flex; align-items: baseline; gap: 4px; height: 64px; padding: 0 14px; border: 1px solid var(--hd-focus); border-radius: 10px; background: var(--hd-surface); align-items: center; }
.mn-sec .mn-cur, .mn-sec .mn-av { font-family: var(--font-brand); font-size: 32px; font-weight: 700; letter-spacing: -.02em; }
.mn-sec .mn-cur { color: var(--hd-fg-muted); }
.mn-sec .mn-opt { display: flex; align-items: center; gap: 12px; min-height: 56px; padding: 8px 12px; border: 1px solid var(--hd-edge); border-radius: 10px; }
.mn-sec .mn-opt.sel { background: var(--hd-accent-subtle); border-color: transparent; }
.mn-sec .mn-opt .x-tile { width: 36px; height: 36px; border-radius: 9px; display: inline-flex; align-items: center; justify-content: center; flex: none; }
.mn-sec .mn-p { margin: 0; font-size: 14px; color: var(--hd-fg-muted); }
.mn-sec .mn-code { display: flex; gap: 8px; }
.mn-sec .mn-code i { width: 40px; height: 48px; border: 1px solid var(--hd-border-input); border-radius: 10px; display: inline-flex; align-items: center; justify-content: center; font-style: normal; font-size: 20px; font-weight: 600; background: var(--hd-surface); }
.mn-sec .mn-code i.cur { border-color: var(--hd-focus); }
.mn-sec .mn-done { display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 8px 0; text-align: center; }
.mn-sec .mn-done .icf { color: var(--hd-success); margin-bottom: 6px; }
.mn-sec .mn-done b { font-size: 17px; font-weight: 600; }
.mn-sec .mn-done span { font-size: 14px; color: var(--hd-fg-muted); }
.mn-sec .mn-done .mn-dm { color: var(--hd-fg-subtle); font-size: 13px; }
/* statuses */
.mn-sec .mn-stl { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); overflow: hidden; }
.mn-sec .mn-st { display: flex; flex-direction: column; align-items: flex-start; gap: 6px; padding: 14px 16px; border-right: 1px solid var(--hd-edge); border-bottom: 1px solid var(--hd-edge); }
.mn-sec .mn-st:nth-child(3n) { border-right: 0; }
.mn-sec .mn-st:nth-last-child(-n+3) { border-bottom: 0; }
.mn-sec .mn-st > span:last-child { font-size: 13.5px; line-height: 18px; color: var(--hd-fg-muted); }
/* notes: fill only, no border */
.mn-sec .mn-note { display: flex; align-items: flex-start; gap: 10px; padding: 12px 14px; border-radius: 12px; background: color-mix(in srgb, var(--hd-fg) 5%, var(--hd-surface)); color: var(--hd-fg); }
.mn-sec .mn-note > .ic { margin-top: 1px; flex: none; color: var(--hd-fg-muted); }
.mn-sec .mn-note.info { background: var(--hd-info-subtle); } .mn-sec .mn-note.info > .ic { color: var(--hd-info-strong); }
.mn-sec .mn-note.warning { } .mn-sec .mn-note.warning > .ic { color: var(--hd-warning-strong); }
.mn-sec .mn-note.danger { background: var(--hd-danger-subtle); } .mn-sec .mn-note.danger > .ic { color: var(--hd-danger-strong); }
.mn-sec .mn-nt { display: flex; flex-direction: column; gap: 2px; flex: 1; min-width: 0; }
.mn-sec .mn-nt b { font-size: 14px; line-height: 20px; font-weight: 600; }
.mn-sec .mn-nd { font-size: 13.5px; line-height: 18px; color: var(--hd-fg-muted); }
.mn-sec .mn-na { flex: none; align-self: center; }
.mn-sec .mn-bar { height: 3px; border-radius: 999px; background: var(--hd-track); margin-top: 8px; overflow: hidden; }
.mn-sec .mn-bar i { display: block; height: 100%; background: var(--hd-warning); border-radius: 999px; }
.mn-sec .mn-bm { font-size: 13px; color: var(--hd-fg-muted); margin-top: 4px; }
/* methods, form */
.mn-sec .mn-cool { margin: 0; font-size: 13.5px; color: var(--hd-fg-muted); }
.mn-sec .mn-form { padding: 16px; display: flex; flex-direction: column; gap: 14px; }
.mn-sec .mn-form .field { margin: 0; }
.mn-sec .mn-seg { display: flex; padding: 3px; gap: 2px; background: var(--hd-control); border-radius: 10px; height: 40px; }
.mn-sec .mn-seg span { flex: 1; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600; color: var(--hd-fg-muted); border-radius: 8px; }
.mn-sec .mn-seg span.on { background: var(--hd-surface); color: var(--hd-fg); box-shadow: 0 1px 2px rgba(16,20,38,.12); }
.mn-sec .mn-sw { display: flex; align-items: center; gap: 12px; }
.mn-sec .mn-tg { width: 40px; height: 24px; border-radius: 999px; background: var(--hd-accent); position: relative; flex: none; }
.mn-sec .mn-tg i { position: absolute; top: 2px; right: 2px; width: 20px; height: 20px; border-radius: 999px; background: #fff; }
/* pan */
.mn-sec .mn-pans { display: grid; grid-template-columns: repeat(5, minmax(0,1fr)); gap: 12px; }
.mn-sec .mn-pan { padding: 16px; display: flex; flex-direction: column; gap: 6px; align-items: flex-start; }
.mn-sec .mn-pan b { font-size: 15px; line-height: 20px; font-weight: 600; margin-top: 4px; }
.mn-sec .mn-pan p { margin: 0; font-size: 13.5px; line-height: 19px; color: var(--hd-fg-muted); flex: 1; }
.mn-sec .mn-pa { margin-top: 10px; }
"""
