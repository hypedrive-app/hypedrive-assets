# New components layer (owned by the new-components agent). Appended last.
XNEW = r"""
/* ===================== XNEW · missing primitives and components ===================== */
.sec.nw { --n-hover: color-mix(in oklab, var(--hd-fg) 6%, transparent); --n-hover-2: color-mix(in oklab, var(--hd-fg) 10%, transparent); }
.sec.nw .box { padding: 24px; }
.n-stage { display: flex; flex-direction: column; gap: 16px; align-content: start; }
.n-stage > .lbl { margin: 8px 0 -4px; } .n-stage > .lbl:first-child { margin-top: 0; }
.n-top { align-items: start; } .n-gap { height: 22px; }
.n-center { align-items: center; } .n-center > .lbl { align-self: flex-start; }
.n-g31 { display: grid; grid-template-columns: 1.55fr 1fr; gap: 22px; align-items: start; }
.n-g4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 22px; align-items: stretch; }
.n-c { justify-content: center; }
.n-t4 { height: 4px; margin-top: 8px; }
.sp { flex: 1; }
.n-caret { display: inline-block; width: 1.5px; height: 18px; margin-left: 1px; background: var(--hd-accent); vertical-align: -4px; border-radius: 4px; }
.n-code { font: 450 12px var(--font-mono); color: var(--hd-fg-subtle); }
.n-dev { position: relative; overflow: hidden; border-radius: 24px; background: var(--hd-canvas); border: 1px solid var(--hd-border); --ring-gap: var(--hd-surface); }
.n-act { display: flex; gap: 8px; flex-wrap: wrap; }
.n-stars { display: inline-flex; gap: 1px; }

/* ---------- select · combobox · multi · list ---------- */
.n-pair { display: flex; flex-direction: column; gap: 6px; }
.input.n-sel { cursor: pointer; }
.input .n-val { flex: 1; min-width: 0; } .input .n-val.ph { color: var(--hd-fg-subtle); font-weight: 400; }
.n-chev { color: var(--hd-fg-muted) !important; transition: transform 160ms var(--ease-out); } .n-chev.up { transform: rotate(180deg); }
.input.dis .n-val { color: var(--hd-fg-subtle); }
.n-list { padding: 6px; display: flex; flex-direction: column; gap: 2px; }
.n-opt { display: flex; align-items: center; gap: 10px; min-height: 40px; padding: 0 10px; border-radius: 8px; font-size: 14.5px; color: var(--hd-fg); }
.n-opt .n-t { flex: 1; min-width: 0; }
.n-opt.hv { background: var(--n-hover); } .n-opt.on { font-weight: 560; }
.n-opt .ic { color: var(--hd-fg-muted); }
.n-opt .n-tick { margin-left: auto; color: var(--hd-accent); display: inline-flex; }
.n-opt .n-sub { margin-left: auto; font-size: 12.5px; color: var(--hd-fg-muted); }
.n-opt mark { background: var(--hd-accent-subtle); color: var(--hd-info-strong); font-weight: 650; border-radius: 4px; padding: 0 1px; margin: 0 -1px; }
.n-opt.n-new { color: var(--hd-link); } .n-opt.n-new .ic { color: var(--hd-link); }
.n-gh { font-size: 12px; font-weight: 550; color: var(--hd-fg-muted); padding: 8px 10px 4px; display: block; }
.n-sep { display: block; height: 1px; background: var(--hairline); margin: 4px 6px; }
.n-q { flex: 1; min-width: 0; display: inline-flex; align-items: center; color: var(--hd-fg); }
.n-clr { width: 18px; height: 18px; border-radius: 50%; background: var(--hd-fg-subtle); color: var(--hd-canvas); display: inline-flex; align-items: center; justify-content: center; }
.input.n-multi { height: auto; min-height: 44px; padding: 7px 10px; flex-wrap: wrap; gap: 6px; }
.input.n-multi .n-q { min-width: 60px; height: 28px; }
.n-tok { height: 28px; padding: 0 4px 0 8px; border-radius: 8px; background: var(--hd-control); color: var(--hd-fg); font-size: 13px; font-weight: 560; display: inline-flex; align-items: center; gap: 6px; }
.n-tok > .ic { color: var(--hd-fg-muted); }
.n-x { all: unset; box-sizing: border-box; width: 20px; height: 20px; border-radius: 6px; display: inline-flex; align-items: center; justify-content: center; color: var(--hd-fg-muted); cursor: pointer; transition: background-color 150ms ease; }
.n-x:hover { background: var(--n-hover-2); color: var(--hd-fg); }

/* ---------- date + time ---------- */
.n-cal { padding: 12px; }
.n-calh { display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px; } .n-calh b { font-size: 14.5px; font-weight: 600; letter-spacing: -0.012em; }
.n-cg { display: grid; grid-template-columns: repeat(7, 1fr); gap: 2px; text-align: center; font-size: 13.5px; }
.n-cg span { height: 36px; display: grid; place-items: center; border-radius: 8px; font-variant-numeric: tabular-nums; font-weight: 450; }
.n-cg .dw { height: 28px; font-size: 12px; font-weight: 500; color: var(--hd-fg-subtle); }
.n-cg .mu { color: var(--hd-fg-subtle); opacity: .6; } .n-cg .off { color: var(--hd-fg-subtle); opacity: .5; }
.n-cg .td { border: 1px solid var(--hd-border-strong); font-weight: 600; } .n-cg .hv { background: var(--n-hover); }
.n-cg .sl { background: var(--hd-accent); color: #fff; font-weight: 600; box-shadow: inset 0 -1px 0 var(--hd-accent-pressed); }
.n-calf { display: flex; justify-content: space-between; margin-top: 10px; padding-top: 10px; border-top: 1px solid var(--hairline); }
.input.n-time { gap: 2px; } .input.n-time > .ic { margin-right: 8px; }
.n-seg { padding: 3px 6px; border-radius: 6px; font-variant-numeric: tabular-nums; font-weight: 500; } .n-seg:last-child { margin-left: 4px; color: var(--hd-fg-muted); }
.n-seg.on { background: var(--hd-accent); color: #fff; } .n-colon { color: var(--hd-fg-muted); }

/* ---------- number stepper ---------- */
.n-steprow { display: flex; align-items: center; gap: 12px; }
.n-step { display: inline-flex; align-items: center; height: 44px; border-radius: 12px; background: var(--hd-surface); border: 1px solid var(--hd-border-input); overflow: hidden; }
.n-step button { all: unset; box-sizing: border-box; width: 44px; height: 100%; display: grid; place-items: center; color: var(--hd-fg); cursor: pointer; transition: background-color 150ms ease, transform 160ms var(--ease-out); }
.n-step button:hover:not(:disabled) { background: var(--n-hover); } .n-step button:active:not(:disabled) { background: var(--n-hover-2); }
.n-step button:disabled { color: var(--hd-fg-subtle); opacity: .55; cursor: not-allowed; }
.n-step output { min-width: 56px; height: 100%; display: grid; place-items: center; font-size: 16px; font-weight: 600; border-left: 1px solid var(--hd-border); border-right: 1px solid var(--hd-border); }
.n-step.sm { height: 32px; border-radius: 8px; } .n-step.sm button { width: 32px; } .n-step.sm output { min-width: 40px; font-size: 14px; }

/* ---------- copy field ---------- */
.input.n-copy { padding-right: 6px; } .input.n-copy .n-val { font-size: 14px; }
.input.n-copy.dis { background: var(--hd-bg-subtle); }
.btn.s.n-done:not(.dis):not([disabled]) { background: var(--hd-success-subtle); color: var(--hd-success-strong); box-shadow: none; }
.btn.n-done .ic { color: var(--hd-success); }

/* ---------- avatar upload ---------- */
.n-avu { display: flex; gap: 16px; align-items: center; }
.n-avt { display: flex; flex-direction: column; gap: 2px; min-width: 0; } .n-avt > b { font-size: 14.5px; font-weight: 600; letter-spacing: -0.012em; } .n-avt .n-act { margin-top: 8px; }
.n-av { position: relative; width: 72px; height: 72px; flex: none; }
.n-av > img { width: 100%; height: 100%; border-radius: 50%; object-fit: cover; display: block; }
.n-av .n-ph { width: 100%; height: 100%; border-radius: 50%; display: grid; place-items: center; color: var(--hd-fg-muted); background: var(--hd-surface); border: 1px solid var(--hd-border); box-shadow: var(--hd-shadow-e1); }
.n-plus { position: absolute; right: -2px; bottom: -2px; width: 24px; height: 24px; border-radius: 50%; display: grid; place-items: center; background: var(--hd-accent); color: #fff; box-shadow: 0 0 0 3px var(--hd-canvas); }
.n-cam { position: absolute; right: -4px; bottom: -4px; width: 28px; height: 28px; border-radius: 50%; display: grid; place-items: center; background: var(--hd-surface); color: var(--hd-fg); border: 1px solid var(--hd-border); box-shadow: 0 0 0 3px var(--hd-canvas), 0 2px 4px rgba(16,20,38,.14); cursor: pointer; }
.n-av.up { margin: 6px; } .n-ringo { position: absolute; left: -6px; top: -6px; width: 84px; height: 84px; }

/* ---------- dropzone · upload rows ---------- */
.n-dz { display: flex; flex-direction: column; align-items: center; text-align: center; gap: 16px; padding: 24px 20px; border-radius: 16px; border: 1.5px dashed var(--hd-border-strong); background: var(--hd-surface); color: var(--hd-fg); transition: transform 200ms var(--ease-out), background-color 150ms ease, border-color 150ms ease; }
.n-dzt { display: flex; flex-direction: column; gap: 2px; } .n-dzt b { font-size: 14.5px; font-weight: 600; letter-spacing: -0.012em; } .n-dzt span { font-size: 13px; color: var(--hd-fg-muted); } .n-dzt u { color: var(--hd-link); font-weight: 560; text-decoration-color: color-mix(in oklab, var(--hd-link) 40%, transparent); text-underline-offset: 3px; }
.n-ft { width: 40px; height: 40px; border-radius: 10px; display: grid; place-items: center; flex: none; background: var(--hd-surface); color: var(--hd-fg); border: 1px solid var(--hd-border); box-shadow: var(--hd-shadow-e1); }
.n-ft.lg { width: 48px; height: 48px; border-radius: 12px; }
.n-ft.err { color: var(--hd-danger); border-color: color-mix(in oklab, var(--hd-danger) 40%, var(--hd-border)); }
.n-types { display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; }
.n-ty { height: 24px; padding: 0 8px 0 6px; border-radius: 6px; background: var(--hd-control); color: var(--hd-fg); font-size: 12px; font-weight: 560; display: inline-flex; align-items: center; gap: 4px; } .n-ty .ic { color: var(--hd-fg-muted); }
.n-dz.drag { border-color: var(--hd-accent); background: var(--hd-accent-subtle); transform: scale(1.015); }
.n-dz.drag .n-ft { background: var(--hd-accent); border-color: var(--hd-accent); color: #fff; transform: translateY(-2px); box-shadow: 0 6px 16px -4px color-mix(in oklab, var(--hd-accent) 50%, transparent); }
.n-dz.drag .n-dzt b { color: var(--hd-info-strong); } .n-dz.drag .n-dzt span { color: var(--hd-info-strong); } .n-dz.drag .n-ty { background: var(--hd-surface); }
.n-frs { display: flex; flex-direction: column; gap: 8px; }
.n-fr { display: flex; align-items: center; gap: 12px; padding: 12px; border-radius: 12px; background: var(--hd-surface); border: 1px solid var(--hd-border); }
.n-fr.err { border-color: var(--hd-danger); }
.n-frb { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px; } .n-frb b { font-size: 14px; font-weight: 560; letter-spacing: -0.01em; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.n-frm { font-size: 12.5px; color: var(--hd-fg-muted); } .n-fr.err .n-frm { color: var(--hd-danger-strong); }
.n-frb .tape { margin-top: 6px; } .n-pct { font-size: 13px; font-weight: 600; color: var(--hd-fg); min-width: 36px; text-align: right; }
.n-id { font-family: var(--font-ui); font-variant-numeric: tabular-nums; letter-spacing: -0.005em; font-size: 14.5px; }
.n-code { font: 450 12px var(--font-ui) !important; font-variant-numeric: tabular-nums; }

/* ---------- range slider ---------- */
.n-rngw { display: flex; flex-direction: column; gap: 14px; }
.n-rhead { display: flex; justify-content: space-between; align-items: baseline; } .n-rhead b { font-size: 13.5px; font-weight: 600; } .n-rv { font-size: 13.5px; color: var(--hd-fg-muted); font-weight: 500; }
.n-hist { display: flex; align-items: flex-end; gap: 3px; height: 44px; margin-bottom: -6px; }
.n-hist i { flex: 1; height: calc(var(--h) * 1.7%); border-radius: 4px 4px 0 0; background: var(--hd-track); } .n-hist i.in { background: var(--hd-data-1); }
.n-rng { position: relative; height: 24px; }
.n-rng .tr { position: absolute; left: 0; right: 0; top: 9px; height: 6px; border-radius: 4px; background: var(--hd-track); }
.n-rng .fill { position: absolute; top: 9px; height: 6px; background: var(--hd-accent); left: var(--a); right: calc(100% - var(--b)); }
.n-rng .th { position: absolute; top: 1px; left: var(--p); width: 22px; height: 22px; margin-left: -11px; border-radius: 50%; background: #fff; border: 2px solid var(--hd-accent); box-shadow: 0 1px 3px rgba(16,20,38,.28); }
[data-theme="dark"] .n-rng .th { box-shadow: 0 1px 3px rgba(0,0,0,.6); }
.n-rng .th.foc { box-shadow: 0 0 0 2px var(--hd-canvas), 0 0 0 4px var(--hd-focus); }
.n-rin { display: flex; align-items: center; gap: 10px; } .n-rin .input { flex: 1; height: 40px; font-size: 14px; gap: 8px; } .n-rin .addon { font-size: 13px; }
.n-dash { width: 10px; height: 1.5px; background: var(--hd-fg-subtle); border-radius: 4px; flex: none; }

/* ---------- toggle button group ---------- */
.n-tgs { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }
.seg span { gap: 8px; } .seg span.on { color: var(--hd-fg); }
.n-tgm { display: inline-flex; align-self: flex-start; border-radius: 12px; overflow: hidden; border: 1px solid var(--hd-border-input); background: var(--hd-surface); }
.n-tgm span { height: 42px; padding: 0 14px; display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 560; color: var(--hd-fg-muted); transition: background-color 150ms ease; }
.n-tgm span + span { border-left: 1px solid var(--hd-border); }
.n-tgm span.on { background: var(--hd-accent-subtle); color: var(--hd-info-strong); }

/* ---------- textarea counter ---------- */
.input.n-ta { align-items: flex-start; height: 100px; padding: 11px 14px; line-height: 22px; font-size: 14.5px; }
.n-warn { color: var(--hd-warning-strong) !important; font-weight: 500; }
.help.err .cnt { color: var(--hd-danger); font-weight: 600; } .help .cnt.n-warn { font-weight: 600; }

/* ---------- form section layout ---------- */
.n-form { padding: 0; }
.n-fs { display: grid; grid-template-columns: 300px 1fr; gap: 40px; padding: 28px 28px 32px; } .n-fs + .n-fs { border-top: 1px solid var(--hairline); }
.n-fsh h3 { margin: 0 0 4px; } .n-fsh p { margin: 0; max-width: 260px; }
.n-ff { display: flex; flex-direction: column; gap: 20px; max-width: 640px; } .n-fgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.n-ffoot { display: flex; align-items: center; gap: 8px; padding: 16px 28px; border-top: 1px solid var(--hairline); }

/* ---------- wizard stepper ---------- */
.n-wzcard { padding: 20px 24px; }
.n-wz { display: flex; align-items: center; gap: 14px; }
.n-wz .s { display: flex; align-items: center; gap: 10px; white-space: nowrap; }
.n-wz .k { width: 28px; height: 28px; border-radius: 50%; display: grid; place-items: center; font-size: 13px; font-weight: 600; color: var(--hd-fg-muted); background: var(--hd-surface); border: 1px solid var(--hd-border-strong); flex: none; }
.n-st b { display: block; font-size: 13.5px; font-weight: 560; color: var(--hd-fg-muted); line-height: 18px; } .n-st small { display: block; font-size: 12px; color: var(--hd-fg-subtle); line-height: 16px; }
.n-wz .s.done .k { background: var(--hd-accent); border-color: var(--hd-accent); color: #fff; } .n-wz .s.done .n-st b { color: var(--hd-fg); }
.n-wz .s.now .k { border: 2px solid var(--hd-accent); color: var(--hd-link); } .n-wz .s.now .n-st b { color: var(--hd-fg); font-weight: 600; }
.n-wz .ln { flex: 1; min-width: 12px; height: 2px; border-radius: 4px; background: var(--hd-border); } .n-wz .ln.done { background: var(--hd-accent); }
.n-mrow { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; align-items: start; }
.n-wzm { padding: 8px 8px 18px; border-radius: 16px; background: var(--hd-surface); }
.n-wzt { display: flex; align-items: center; gap: 4px; min-height: 48px; } .n-wzt > div { flex: 1; text-align: center; } .n-wzt b { display: block; font-size: 15px; font-weight: 600; letter-spacing: -0.012em; } .n-wzt small { display: block; font-size: 12px; color: var(--hd-fg-muted); }
.n-skip { width: 44px; text-align: right; font-size: 14px; font-weight: 560; color: var(--hd-link); padding-right: 8px; }
.n-sg { display: flex; gap: 4px; padding: 6px 8px 0; } .n-sg i { flex: 1; height: 4px; border-radius: 4px; background: var(--hd-track); } .n-sg i.on { background: var(--hd-accent); } .n-sg i.cur { background: var(--hd-accent); }
.n-dots2 { display: flex; gap: 6px; justify-content: center; padding-top: 8px; } .n-dots2 i { width: 6px; height: 6px; border-radius: 50%; background: var(--hd-track-strong); opacity: .5; } .n-dots2 i.on { opacity: 1; background: var(--hd-accent); } .n-dots2 i.cur { opacity: 1; width: 18px; border-radius: 4px; background: var(--hd-accent); }

/* ---------- command palette ---------- */
.dialog.n-cmd { width: 100%; max-width: 620px; padding: 0; border-radius: 16px; }
.n-cin { display: flex; align-items: center; gap: 12px; height: 56px; padding: 0 18px; font-size: 16px; border-bottom: 1px solid var(--hairline); color: var(--hd-fg-muted); }
.n-cs { padding: 6px 8px 8px; display: flex; flex-direction: column; gap: 2px; }
.n-ci { display: flex; align-items: center; gap: 12px; height: 44px; padding: 0 10px; border-radius: 10px; font-size: 14.5px; }
.n-ci .n-t { flex: none; } .n-ci .n-t b { font-weight: 650; } .n-ci img { width: 28px; height: 28px; border-radius: 6px; object-fit: cover; } .n-ci > .ic { color: var(--hd-fg-muted); margin: 0 2px; }
.n-ci .n-sub { color: var(--hd-fg-muted); font-size: 13px; } .n-ci > .kbd, .n-ci > .n-go { margin-left: auto; } .n-ci > .kbd + .kbd { margin-left: -4px; }
.n-ci kbd + kbd { margin-left: 4px; }
.n-ci.hl { background: var(--n-hover); } .n-go { display: inline-flex; align-items: center; gap: 8px; font-size: 12.5px; color: var(--hd-fg-muted); }
.n-cf { display: flex; gap: 16px; align-items: center; padding: 10px 18px; border-top: 1px solid var(--hairline); font-size: 12px; color: var(--hd-fg-muted); } .n-cf > span { display: inline-flex; gap: 6px; align-items: center; }

/* ---------- popover · hover card ---------- */
.n-anchor { position: relative; display: flex; flex-direction: column; gap: 10px; align-items: flex-start; }
.dialog.n-pop, .dialog.n-hc { width: 340px; max-width: 100%; padding: 16px; border-radius: 14px; display: flex; flex-direction: column; gap: 8px; }
.n-pop b { font-size: 14.5px; font-weight: 600; } .n-pop p, .n-hc p { margin: 0; }
.n-popf { display: flex; align-items: center; justify-content: space-between; margin-top: 8px; }
.n-mention { font-size: 14.5px; color: var(--hd-fg-muted); } .n-mention u { color: var(--hd-link); text-decoration: none; font-weight: 560; background: var(--hd-accent-subtle); padding: 1px 4px; border-radius: 4px; }
.n-hch { display: flex; gap: 12px; align-items: center; } .n-hch img { width: 48px; height: 48px; border-radius: 50%; object-fit: cover; }
.n-hch b { display: flex; align-items: center; gap: 4px; font-size: 15px; font-weight: 600; } .n-hch span { display: block; }
.n-hcs { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; padding: 10px 0; margin: 4px 0; border-top: 1px solid var(--hairline); border-bottom: 1px solid var(--hairline); }
.n-hcs b { display: block; font-size: 16px; font-weight: 600; letter-spacing: -0.02em; } .n-hcs span { display: flex; align-items: center; gap: 4px; font-size: 12px; color: var(--hd-fg-muted); margin-top: 2px; }

/* ---------- context menu · sort menu ---------- */
.n-ctxw { display: flex; gap: 6px; align-items: flex-start; }
.menu.n-ctx { width: 232px; flex: none; padding: 6px; }
.menu.n-ctx div, .menu.n-sortm div { height: 36px; padding: 0 10px; gap: 10px; font-size: 14px; }
.menu.n-ctx div .ic, .menu.n-sortm div .ic { color: var(--hd-fg-muted); }
.menu .n-t { flex: 1; } .menu .n-k { display: inline-flex; gap: 3px; margin-left: auto; } .menu .n-chv { margin-left: auto; display: inline-flex; color: var(--hd-fg-subtle); }
.menu .hl { background: var(--n-hover); } .menu .dg, .menu .dg .ic { color: var(--hd-danger) !important; } .menu .dg { margin-top: 0; } .menu .dg::before { display: none; }
.menu .n-sep { margin: 4px 4px; }
.menu.n-subm { width: 180px; margin-top: 118px; } .menu.n-subm .n-tk { color: var(--hd-accent); margin-left: auto; display: inline-flex; }
.n-sortw { display: flex; flex-direction: column; gap: 8px; align-items: flex-start; }
.menu.n-sortm { width: 240px; padding: 6px; } .n-mh { display: block; font-size: 12px; font-weight: 550; color: var(--hd-fg-muted); padding: 6px 10px 4px; }
.menu.n-sortm .n-tk { width: 18px; display: inline-flex; color: var(--hd-accent); } .menu.n-sortm div.on { font-weight: 560; }

/* ---------- action sheet (iOS) ---------- */
.n-asd { height: 372px; }
.n-ghost { position: absolute; inset: 0; padding: 20px 16px; display: flex; flex-direction: column; gap: 12px; } .n-ghost .skel { display: block; height: 56px; border-radius: 12px; }
.n-scrim { position: absolute; inset: 0; background: rgba(13,14,18,.48); }
.n-as { position: absolute; left: 8px; right: 8px; bottom: 6px; display: flex; flex-direction: column; gap: 8px; }
.n-asg { background: var(--hd-surface); border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; }
.n-ash { padding: 12px 16px; text-align: center; font-size: 13px; color: var(--hd-fg-muted); line-height: 18px; } .n-ash b { display: block; font-weight: 600; color: var(--hd-fg); }
.n-asa { height: 54px; display: flex; align-items: center; justify-content: center; font-size: 17px; font-weight: 450; color: var(--hd-link); box-shadow: inset 0 1px 0 var(--hairline); letter-spacing: -0.01em; }
.n-ash + .n-asa { box-shadow: inset 0 1px 0 var(--hairline); } .n-asa.dg { color: var(--hd-danger); } .n-asa.cn { font-weight: 600; box-shadow: none; }
.n-hi { display: block; width: 134px; height: 5px; border-radius: 4px; background: var(--hd-fg); margin: 4px auto 0; opacity: .9; }

/* ---------- filter panel ---------- */
.n-fil { padding: 0; }
.n-filh { display: flex; align-items: center; gap: 8px; padding: 16px 20px; } .n-filh .btn.link { margin-left: auto; }
.n-fc { font-size: 12px; font-weight: 600; padding: 2px 8px; border-radius: 6px; background: var(--hd-accent-subtle); color: var(--hd-info-strong); }
.n-fsec { padding: 16px 20px; border-top: 1px solid var(--hairline); display: flex; flex-direction: column; gap: 12px; } .n-fsec > b, .n-fsec .n-rhead b { font-size: 13.5px; font-weight: 600; }
.n-fsec .n-hist { margin-bottom: -4px; }
.n-frow { flex-direction: row; align-items: center; gap: 12px; } .n-frow .n-t { flex: 1; } .n-frow .n-t b { display: block; font-size: 14px; font-weight: 560; } .n-frow small { font-size: 12.5px; color: var(--hd-fg-muted); }
.n-filf { display: flex; gap: 8px; padding: 14px 20px 16px; border-top: 1px solid var(--hairline); } .n-filf .btn { flex: 1; }
.n-filf .btn.p { flex: 2; }
.n-fil .chip .plat, .n-fil .chip svg { flex: none; }

/* ---------- load more ---------- */
.n-more { display: flex; flex-direction: column; align-items: center; gap: 14px; padding: 18px 20px; border-radius: 16px; background: var(--hd-surface); border: 1px solid var(--hd-border); }
.n-prog { width: 100%; max-width: 260px; display: flex; flex-direction: column; align-items: center; gap: 8px; } .n-prog .tape { width: 100%; height: 4px; } .n-prog b { color: var(--hd-fg); font-weight: 600; }
.n-end { display: inline-flex; align-items: center; gap: 6px; height: 44px; font-size: 14px; font-weight: 560; color: var(--hd-success-strong); } .n-end .ic { color: var(--hd-success); }

/* ---------- spinners · loading ---------- */
.n-spin { width: 24px; height: 24px; border-radius: 50%; border: 2.5px solid var(--hd-track); border-top-color: var(--hd-accent); animation: spin 760ms linear infinite; flex: none; display: inline-block; }
.n-spin.sm { width: 16px; height: 16px; border-width: 2px; } .n-spin.lg { width: 40px; height: 40px; border-width: 3.5px; }
.btn .n-spin { border-color: color-mix(in oklab, currentColor 25%, transparent); border-top-color: currentColor; }
.n-spins { display: flex; gap: 32px; align-items: flex-end; padding: 8px 0 2px; } .n-spins > div { display: flex; flex-direction: column; align-items: center; gap: 10px; } .n-spins small { font-size: 12px; color: var(--hd-fg-subtle); font-variant-numeric: tabular-nums; }
.n-lr { align-items: flex-start; } .n-lr > .n-spin { margin-top: 2px; }
.n-lmore { display: flex; align-items: center; justify-content: center; gap: 10px; height: 40px; }

/* ---------- dialogs · states · banners ---------- */
.dialog.n-dlg { width: 100%; max-width: 420px; padding: 24px; border-radius: 24px; display: flex; flex-direction: column; gap: 12px; } .dialog.n-dlg p { margin: 0; } .dialog.n-dlg .t-h2 { margin-top: 4px; }
.dialog.n-dlg.n-sm { max-width: 380px; } .dialog.n-dlg.n-sm .t-h2 { margin-top: 0; }
.n-dti { width: 44px; height: 44px; border-radius: 12px; display: grid; place-items: center; background: var(--hd-danger-subtle); color: var(--hd-danger-strong); }
.n-dlf { display: flex; gap: 8px; justify-content: flex-end; margin-top: 8px; }
.n-state { display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px; padding: 32px 28px 28px; } .n-state p { margin: 0 0 8px; max-width: 320px; }
.n-ti { width: 52px; height: 52px; border-radius: 16px; display: grid; place-items: center; background: var(--hd-control); color: var(--hd-fg); margin-bottom: 8px; } .n-ti.dg { background: var(--hd-danger-subtle); color: var(--hd-danger-strong); }
.n-state .n-code { margin-top: 8px; }
.n-bwrap { display: flex; flex-direction: column; gap: 10px; }
.n-banner { display: flex; align-items: center; gap: 10px; padding: 0 16px; min-height: 48px; border-radius: 12px; font-size: 14px; }
.n-banner b { font-weight: 600; } .n-banner.warn { background: var(--hd-warning-subtle); color: var(--hd-warning-strong); } .n-banner.warn > .ic { color: var(--hd-warning); }
.n-banner.ok { background: var(--hd-success-subtle); color: var(--hd-success-strong); } .n-banner.ok > .ic { color: var(--hd-success); }
.n-rc { display: inline-flex; align-items: center; gap: 8px; font-weight: 560; } .n-banner .btn.link { color: inherit; text-decoration-color: color-mix(in oklab, currentColor 40%, transparent); }
.n-banner .n-spin { border-color: color-mix(in oklab, currentColor 25%, transparent); border-top-color: currentColor; }

/* ---------- pages (illustration states) ---------- */
.n-page { display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px; padding: 28px 24px 28px; height: 100%; }
.n-page img { width: 168px; height: 168px; object-fit: contain; margin-bottom: 4px; } .n-page p { margin: 0 0 12px; max-width: 280px; font-size: 14px; line-height: 21px; } .n-page .flexw { margin-top: auto; }
.n-page .n-code { margin-top: 4px; }
.n-succ { padding: 32px 28px 28px; } .n-succ img { width: 180px; height: 180px; }
.n-sum { display: flex; justify-content: space-between; align-items: center; width: 100%; padding: 12px 14px; border-radius: 12px; background: var(--hd-bg-subtle); border: 1px solid var(--hd-border); font-size: 14px; margin: 0 0 16px; } .n-sum b { font-size: 15px; font-weight: 650; }
.n-okrow { display: flex; align-items: center; gap: 12px; padding: 14px; border-radius: 12px; background: var(--hd-surface); border: 1px solid var(--hd-border); } .n-okrow > div { flex: 1; min-width: 0; } .n-okrow b { display: block; font-size: 14.5px; font-weight: 600; }
.n-okk { width: 36px; height: 36px; border-radius: 50%; display: grid; place-items: center; background: var(--hd-success-solid); flex: none; }

/* ---------- inline edit ---------- */
.n-iec2 { padding: 18px 20px; display: flex; flex-direction: column; gap: 14px; }
.n-ie { display: flex; gap: 8px; align-items: center; } .n-ie.ed { align-items: center; }
.n-iev { display: inline-flex; align-items: center; gap: 10px; padding: 4px 8px; margin: 0 -8px; border-radius: 8px; transition: background-color 150ms ease; }
.n-pen { width: 28px; height: 28px; border-radius: 8px; display: grid; place-items: center; color: var(--hd-fg-muted); opacity: 0; transition: opacity 150ms ease; font-family: var(--font-ui); }
.n-ie.hov .n-iev { background: var(--n-hover); } .n-ie.hov .n-pen { opacity: 1; }
@media (hover: hover) and (pointer: fine) { .n-iev:hover { background: var(--n-hover); } .n-iev:hover .n-pen { opacity: 1; } }
.n-iei { flex: 1; height: 48px; } .n-iei .t-h2 { font-size: 19px; }
.n-hint { display: flex; gap: 6px; align-items: center; font-size: 12px; color: var(--hd-fg-muted); }
.n-iec { display: flex; gap: 6px; align-items: center; } .n-iec .input { width: 96px; height: 32px; padding: 0 10px; border-radius: 8px; font-size: 14px; }
.n-ier { align-items: center; } .n-ier .tx small { margin-bottom: 4px; }

/* ---------- product card ---------- */
.n-trio { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; } .n-duo { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; } .n-one { max-width: 100%; }
.n-pc { padding: 8px; display: flex; flex-direction: column; gap: 12px; }
.n-ph { position: relative; aspect-ratio: 4 / 3; }
.n-pc .n-ph img { width: 100%; height: 100%; object-fit: cover; border-radius: 8px; display: block; outline: 0 !important; }
.n-bd { position: absolute; left: 8px; top: 8px; }
.n-disc { all: unset; box-sizing: border-box; position: absolute; right: 8px; top: 8px; width: 32px; height: 32px; border-radius: 50%; display: grid; place-items: center; background: rgba(255,255,255,.94); color: #121417; box-shadow: 0 1px 3px rgba(16,20,38,.22); cursor: pointer; transition: transform 160ms var(--ease-out); } .n-disc:active { transform: scale(.94); }
[data-theme="dark"] .n-disc { background: rgba(18,20,23,.82); color: #fff; box-shadow: 0 0 0 1px rgba(255,255,255,.14); }
.n-pb { padding: 0 8px 8px; display: flex; flex-direction: column; gap: 6px; }
.n-brand { display: flex; align-items: center; gap: 6px; font-size: 13px; color: var(--hd-fg-muted); } .n-brand .av { font-size: 8px; } .n-brand .n-r { margin-left: auto; }
.n-pt { font-size: 15.5px; font-weight: 600; letter-spacing: -0.014em; line-height: 21px; }
.n-rw { display: flex; align-items: baseline; gap: 6px; font-size: 13px; } .n-rw b { font-size: 18px; font-weight: 650; letter-spacing: -0.02em; font-family: var(--font-brand); }
.n-sl { display: flex; flex-direction: column; gap: 6px; margin-top: 4px; } .n-sl .tape { height: 4px; margin: 0; }
.n-pf { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 8px; } .n-loc { display: inline-flex; align-items: center; gap: 4px; font-size: 12.5px; color: var(--hd-fg-muted); }
.n-ph2 { display: flex; gap: 14px; padding: 8px; align-items: stretch; }
.n-ph2 > img { width: 112px; height: 112px; object-fit: cover; border-radius: 8px; flex: none; outline: 0 !important; }
.n-hb { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 6px; padding: 4px 0; } .n-meta { display: flex; gap: 14px; flex-wrap: wrap; font-size: 12.5px; color: var(--hd-fg-muted); margin-top: auto; } .n-meta span { display: inline-flex; align-items: center; gap: 4px; }
.n-he { display: flex; flex-direction: column; align-items: flex-end; justify-content: space-between; padding: 4px 6px 4px 0; text-align: right; } .n-he b { font-size: 19px; font-weight: 650; letter-spacing: -0.02em; font-family: var(--font-brand); display: block; line-height: 22px; }
.n-he .btn { margin-top: auto; }

/* ---------- creator card ---------- */
.n-cc { padding: 8px; display: flex; flex-direction: column; gap: 12px; }
.n-cph { aspect-ratio: 5 / 4; } .n-cph img { width: 100%; height: 100%; object-fit: cover; object-position: 50% 25%; border-radius: 8px; display: block; }
.n-cb { padding: 0 8px 8px; display: flex; flex-direction: column; gap: 4px; }
.n-cn { display: flex; align-items: center; gap: 6px; } .n-cn b { font-size: 16px; font-weight: 650; letter-spacing: -0.016em; }
.n-plat { display: flex; align-items: center; gap: 16px; margin: 8px 0 4px; font-size: 13.5px; } .n-plat span { display: inline-flex; align-items: center; gap: 6px; } .n-plat b { font-weight: 600; letter-spacing: -0.01em; }
.n-cr { display: inline-flex; align-items: center; gap: 4px; font-size: 13px; } .n-cr b { font-weight: 600; } .n-cc .n-cr { margin-bottom: 4px; }
.n-ch { display: flex; align-items: center; gap: 14px; padding: 12px; }
.n-ch > img, .n-ch .n-chav { width: 56px; height: 56px; border-radius: 50%; object-fit: cover; flex: none; display: block; } .n-chav .av { display: flex; }
.n-cb2 { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px; } .n-cb2 .n-cn { flex-wrap: wrap; } .n-cb2 .n-cn span { margin-left: 4px; } .n-cb2 .n-plat { margin: 2px 0 0; gap: 14px; }
.n-hc2 { display: flex; gap: 8px; align-items: center; }

/* ---------- message thread ---------- */
.n-thr { padding: 0; display: flex; flex-direction: column; }
.n-thh { display: flex; align-items: center; gap: 12px; padding: 14px 16px; border-bottom: 1px solid var(--hairline); } .n-thh > div { flex: 1; min-width: 0; } .n-thh b { display: block; font-size: 14.5px; font-weight: 600; } .n-thh .av { width: 36px; height: 36px; font-size: 13px; }
.n-tb { padding: 16px; display: flex; flex-direction: column; gap: 12px; }
.n-day { align-self: center; font-size: 12px; font-weight: 560; color: var(--hd-fg-muted); padding: 3px 10px; border-radius: 8px; background: var(--hd-control); }
.n-m { display: flex; gap: 8px; align-items: flex-end; max-width: 82%; } .n-m.out { align-self: flex-end; flex-direction: row-reverse; }
.n-bn { align-self: flex-end; } .n-bn .av { font-size: 10px; }
.n-mc { display: flex; flex-direction: column; gap: 4px; padding: 10px 14px 8px; font-size: 14.5px; line-height: 21px; border-radius: 16px 16px 16px 4px; background: var(--hd-control); color: var(--hd-fg); min-width: 0; }
.n-m.out .n-mc { background: var(--hd-accent); color: #fff; border-radius: 16px 16px 4px 16px; align-items: flex-end; } .n-mc p { margin: 0; align-self: stretch; }
.n-mt { display: inline-flex; align-items: center; gap: 6px; font-size: 11.5px; line-height: 14px; color: var(--hd-fg-muted); align-self: flex-end; } .n-m.out .n-mt { color: rgba(255,255,255,.82); }
.n-rd { display: inline-flex; align-items: center; gap: 3px; } .n-m.out .n-rd .ic { color: #fff; }
.n-att { display: flex; align-items: center; gap: 10px; padding: 8px 6px 8px 10px; margin: 0 -4px; border-radius: 10px; background: var(--hd-surface); border: 1px solid var(--hd-border); } .n-att > div { flex: 1; min-width: 0; } .n-att b { display: block; font-size: 13.5px; font-weight: 560; line-height: 18px; } .n-att span { font-size: 12px; color: var(--hd-fg-muted); } .n-att > .ic { color: var(--hd-fg-muted); }
.n-attimg { width: 220px; max-width: 100%; aspect-ratio: 4/3; object-fit: cover; border-radius: 10px !important; display: block; outline: 0 !important; }
.n-comp { display: flex; align-items: center; gap: 8px; padding: 12px 12px 14px; border-top: 1px solid var(--hairline); } .n-comp .input { flex: 1; }
.n-ib { all: unset; box-sizing: border-box; width: 44px; height: 44px; display: grid; place-items: center; border-radius: 12px; color: var(--hd-fg-muted); cursor: pointer; transition: background-color 150ms ease; } .n-ib:hover { background: var(--n-hover); }

/* ---------- description list ---------- */
.n-dlc { padding: 4px 20px; } .n-dl { margin: 0; }
.n-dl > div { display: grid; grid-template-columns: 132px 1fr; gap: 16px; padding: 12px 0; align-items: center; min-height: 48px; } .n-dl > div + div { border-top: 1px solid var(--hairline); }
.n-dl dt { font-size: 13.5px; color: var(--hd-fg-muted); } .n-dl dd { margin: 0; font-size: 14.5px; font-weight: 500; display: flex; align-items: center; gap: 6px; } .n-dl dd b { font-weight: 650; }
.n-dl.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 0 24px; padding: 8px 0; } .n-dl.grid2 > div { display: flex; flex-direction: column; align-items: flex-start; gap: 2px; padding: 12px 0; border-top: 0; min-height: 0; } .n-dl.grid2 > div:nth-child(n+3) { border-top: 1px solid var(--hairline); }

/* ---------- dividers ---------- */
.n-dvs { display: flex; flex-direction: column; gap: 18px; } .n-dvs > div { display: flex; flex-direction: column; gap: 8px; }
.n-hr { border: 0; height: 1px; background: var(--hd-border); margin: 0; } .n-hr.in { margin-left: 48px; }
.n-hrl { display: flex; align-items: center; gap: 12px; font-size: 13px; color: var(--hd-fg-muted); } .n-hrl i { flex: 1; height: 1px; background: var(--hd-border); } .n-hrl.left span { font-weight: 560; }
.n-vrow { display: flex; align-items: center; gap: 14px; font-size: 14px; } .n-vr { width: 1px; height: 16px; background: var(--hd-border-strong); }
.n-band { height: 12px; margin: 0 -24px; background: var(--hd-canvas); box-shadow: inset 0 1px 0 var(--hairline), inset 0 -1px 0 var(--hairline); border-radius: 0; }
.n-dvs .n-band { background: var(--hd-surface); }

/* ---------- swipe rows ---------- */
.n-sw { padding: 12px; display: flex; flex-direction: column; gap: 10px; border-radius: 16px; }
.n-swr { position: relative; }
.n-sr { background: var(--hd-surface); } .n-sr .av { flex: none; }
.n-sr.off { transform: translateX(96px); } .n-sr.left { transform: translateX(-168px); }
.n-swa { position: absolute; top: 0; bottom: 0; display: flex; gap: 8px; align-items: stretch; }
.n-swa.l { left: 0; } .n-swa.r { right: 0; }
.n-swa .a { width: 80px; border-radius: 12px; display: flex; flex-direction: column; gap: 4px; align-items: center; justify-content: center; font-size: 12px; font-weight: 560; color: #fff; }
.n-swa .a.ok { background: var(--hd-success-solid); color: #fff; } .n-swa .a.dg { background: var(--hd-danger-solid); } .n-swa .a.mu { background: var(--hd-track-strong); }
.n-swr { overflow: hidden; border-radius: 12px; }

/* ---------- share sheet ---------- */
.n-shd { height: 500px; }
.n-shs { position: absolute; left: 0; right: 0; bottom: 0; padding: 10px 16px 14px; border-radius: 24px 24px 0 0; display: flex; flex-direction: column; gap: 14px; } .n-shs .grab { margin: 0 auto 2px; }
.n-shp { display: flex; align-items: center; gap: 12px; padding: 10px; border-radius: 12px; background: var(--hd-bg-subtle); border: 1px solid var(--hd-border); } .n-shp img { width: 48px; height: 48px; border-radius: 6px; object-fit: cover; } .n-shp b { display: block; font-size: 14.5px; font-weight: 600; } .n-shp span { display: block; }
.n-apps { display: grid; grid-template-columns: repeat(5, 1fr); gap: 4px; } .n-apps > div { display: flex; flex-direction: column; align-items: center; gap: 6px; } .n-apps small { font-size: 12px; color: var(--hd-fg-muted); }
.n-app { width: 56px; height: 56px; border-radius: 16px; display: grid; place-items: center; background: var(--hd-control); transition: transform 160ms var(--ease-out); } .n-app:active { transform: scale(.96); }
.n-shl { display: flex; gap: 8px; } .n-shl .btn { flex: 1; min-width: 0; padding: 0 12px; }
.n-shd .sheet { background: var(--hd-surface); }

/* ---------- empty with action ---------- */
.n-ea { display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px; padding: 28px 28px 28px; } .n-ea img { width: 160px; height: 160px; object-fit: contain; } .n-ea p { margin: 0; max-width: 380px; }
.n-chk { list-style: none; margin: 8px 0 12px; padding: 0; display: flex; flex-direction: column; gap: 10px; text-align: left; font-size: 14px; } .n-chk li { display: flex; align-items: center; gap: 10px; } .n-chk li .ic:not(.icf) { color: var(--hd-fg-muted); }
.n-ea2 { display: flex; align-items: center; gap: 14px; padding: 16px; border-radius: 16px; border: 1.5px dashed var(--hd-border-strong); background: var(--hd-surface); } .n-ea2 > div { flex: 1; min-width: 0; } .n-ea2 b { display: block; font-size: 14.5px; font-weight: 600; }
.n-eai { width: 44px; height: 44px; border-radius: 12px; display: grid; place-items: center; background: var(--hd-control); color: var(--hd-fg); flex: none; }

/* ===== round 2 ===== */
.n-hist i { height: calc(var(--h) * 1.7px); }
.n-warn.w { display: inline-flex; gap: 5px; align-items: center; }
.n-calh .btn.g, .n-wzt .btn.g { color: var(--hd-fg-muted); } .n-calh .btn.g:hover, .n-wzt .btn.g:hover { color: var(--hd-fg); }
.n-banner b, .n-banner .n-bm { white-space: nowrap; } .n-banner .n-bm { overflow: hidden; text-overflow: ellipsis; }
.n-sk1 { width: 40px; height: 40px; border-radius: 8px; flex: none; } .n-sk2 { display: block; height: 12px; width: 55%; border-radius: 4px; } .n-sk3 { display: block; height: 10px; width: 35%; border-radius: 4px; margin-top: 8px; } .n-sk4 { width: 48px; height: 22px; border-radius: 6px; }
.n-page .flexw { flex-wrap: nowrap; margin-top: 12px; } .n-page { justify-content: flex-start; } .n-page .n-code { margin-top: 12px; }
.n-hint { gap: 14px; } .n-hint > span { display: inline-flex; gap: 6px; align-items: center; }
.n-pc .n-ph { aspect-ratio: 3 / 2; }
.n-cc { align-items: center; text-align: center; padding: 24px 20px 20px; gap: 4px; }
.n-cav { width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 8px; box-shadow: 0 0 0 1px var(--hairline); }
.n-cc .n-cn { justify-content: center; } .n-cc .n-plat { justify-content: center; margin: 12px 0 8px; } .n-cc .n-cr { margin: 0 0 12px; }
.n-cc .n-pf { width: 100%; margin-top: 4px; } .n-cc .n-pf .btn.p { flex: 1; }
.n-slide { aspect-ratio: 1 / 1; }
.n-band { margin: 0; height: 8px; border-radius: 4px; background: var(--hd-control); box-shadow: none; } .n-dvs .n-band { background: var(--hd-control); }
.n-ghost img { width: 100%; height: 120px; object-fit: cover; border-radius: 12px; display: block; } .n-ghost .skel { display: block; border-radius: 6px; height: 14px; } .n-ghost .n-g1 { width: 70%; height: 18px; } .n-ghost .n-g2 { width: 40%; } .n-ghost .n-g3 { width: 90%; }
.n-ff { max-width: none; }
.n-fs { grid-template-columns: 300px 1fr; } .n-fs .n-ff { max-width: 720px; }
.n-more { padding: 14px 20px; gap: 12px; }
.n-page img { width: 150px; height: 150px; }

[data-theme="dark"] .n-asg, [data-theme="dark"] .n-shd .sheet { background: var(--hd-surface-raised); box-shadow: 0 0 0 1px var(--hairline); }
[data-theme="dark"] .n-scrim { background: rgba(0,0,0,.6); }
.n-asd .n-ghost img { height: 140px; }

.n-sr.off { transform: none; margin-left: 88px; } .n-sr.left { transform: none; margin-right: 176px; }
.n-sr .tx small { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

/* ===== round 3 ===== */
.n-cav { width: 72px; height: 72px; }
.n-r { width: 28px; height: 28px; border-radius: 50%; object-fit: cover; }
.n-ci img.n-r { border-radius: 50%; }
.n-tabs { display: flex; gap: 6px; padding: 8px 12px; border-bottom: 1px solid var(--hairline); }
.n-tabs span { height: 28px; padding: 0 10px; border-radius: 8px; display: inline-flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 560; color: var(--hd-fg-muted); }
.n-tabs span b { font-size: 12px; font-weight: 560; color: var(--hd-fg-subtle); }
.n-tabs span.on { background: var(--hd-accent-subtle); color: var(--hd-info-strong); } .n-tabs span.on b { color: var(--hd-info-strong); }
.n-ci .n-k { margin-left: auto; display: inline-flex; gap: 3px; }
.n-fgrid { grid-template-columns: repeat(3, 1fr); } .n-fs .n-ff { max-width: none; }
.n-fsh p { max-width: 240px; }
.n-togl { height: 44px; display: flex; align-items: center; gap: 12px; }
/* illustration pages: no stretched whitespace */
.n-g4 { align-items: start; } .n-page { height: auto; padding: 24px 20px 24px; } .n-page img { width: 140px; height: 140px; margin-bottom: 0; } .n-page p { margin-bottom: 8px; }
.n-succ { padding: 28px 24px 24px; }
/* swipe: the row slides, the actions wait behind it */
.n-sr.off { transform: translateX(88px); margin: 0; } .n-sr.left { transform: translateX(-176px); margin: 0; }
.n-swr { border-radius: 12px; }
/* believable page behind a scrim */
.n-ghost { padding: 14px 14px 0; gap: 10px; } .n-ghost .row { border-radius: 12px; padding: 10px 12px; }
.n-gh1 { display: flex; align-items: center; gap: 8px; min-height: 32px; } .n-gh1 .badge { margin-left: auto; }
.n-ghost img { height: 150px; } .n-gh2 { display: flex; align-items: center; justify-content: space-between; } .n-gr { font: 650 22px var(--font-brand); letter-spacing: -0.02em; }
.n-asd { height: 420px; } .n-shd { height: 560px; }
.n-ghost .tape { margin: 0; }
.n-asd { height: 640px; }
.dialog.n-pop, .dialog.n-hc { width: 420px; }
.n-top > *, .n-g31 > *, .n-g4 > * { min-width: 0; }
.n-wide { width: 100%; } .n-banner { min-width: 0; } .n-banner .n-bm { flex: 0 1 auto; min-width: 0; } .n-banner .sp { flex: 1 1 0; min-width: 8px; }
.n-spin { border-color: var(--hd-border-strong); border-top-color: var(--hd-accent); }
.btn .n-spin, .n-banner .n-spin { border-color: color-mix(in oklab, currentColor 25%, transparent); border-top-color: currentColor; }
.n-sk1.skel, .n-sk2.skel, .n-sk3.skel, .n-sk4.skel { background: var(--hd-control) !important; }
.n-tl { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; } .n-tl .badge { flex: none; }
.n-he { flex: none; }
.n-col { display: flex; flex-direction: column; gap: 22px; min-width: 0; }
.n-sr.left { transform: translateX(-152px); } .n-swa .a { width: 72px; }
.n-ea2 { min-height: 80px; }
.n-okk { color: #fff; }
.n-m.out .n-mt { color: #fff; }
.n-swa .a.ok { background: var(--hd-mint-700); } .n-swa .a.mu { background: var(--hd-ink-700); }
.n-act .btn.g:first-child { margin-left: -12px; }
.input.n-copy.dis .btn { color: var(--hd-fg-subtle); pointer-events: none; } .input.n-copy.dis .btn .ic { color: var(--hd-fg-subtle); }
.n-opt mark { background: none; color: var(--hd-link); padding: 0; margin: 0; font-weight: 650; }
.n-wz .ln { background: var(--hd-border-strong); } .n-wz .ln.done { background: var(--hd-accent); }
.n-okk { background: var(--hd-mint-700); }
.n-brand .av { width: 22px !important; height: 22px !important; font-size: 11px !important; }

/* ===== nw8 · media (m-*) ===== */
.m-g2 { display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }
.m-chip { position: absolute; top: 12px; right: 12px; height: 24px; padding: 0 10px; border-radius: 12px; background: rgba(13,14,18,.64); color: #fff; font-size: 12px; font-weight: 600; display: inline-flex; align-items: center; z-index: 2; letter-spacing: 0; }
.m-chip-s { position: static; }
.m-disc { all: unset; box-sizing: border-box; position: absolute; width: 40px; height: 40px; border-radius: 50%; display: grid; place-items: center; background: rgba(255,255,255,.96); color: #121417; box-shadow: 0 1px 2px rgba(16,20,38,.16), 0 4px 12px rgba(16,20,38,.18); cursor: pointer; z-index: 2; transition: transform 160ms var(--ease-out), opacity 150ms ease; }
.m-disc:active { transform: scale(.94); } .m-disc:disabled { opacity: 0; pointer-events: none; }
[data-theme="dark"] .m-disc { background: rgba(18,20,23,.86); color: #fff; box-shadow: 0 0 0 1px rgba(255,255,255,.16), 0 4px 12px rgba(0,0,0,.5); }
.m-save { top: 12px; left: 12px; width: 36px; height: 36px; } .m-prev, .m-next { top: 50%; margin-top: -20px; } .m-prev { left: 12px; } .m-next { right: 12px; }
.m-dots { position: absolute; left: 50%; bottom: 16px; transform: translateX(-50%); display: inline-flex; gap: 8px; padding: 8px 12px; border-radius: 12px; background: rgba(13,14,18,.48); z-index: 2; }
.m-dots i { width: 8px; height: 8px; border-radius: 50%; background: rgba(255,255,255,.56); } .m-dots i.on { width: 24px; border-radius: 4px; background: #fff; }
.m-dots.on-canvas { position: static; transform: none; align-self: center; background: none; padding: 12px 0 4px; } .m-dots.on-canvas i { background: var(--hd-track-strong); opacity: .45; } .m-dots.on-canvas i.on { background: var(--hd-fg); opacity: 1; }
.m-gal { display: grid; grid-template-columns: 72px 1fr; gap: 16px; align-items: start; }
.m-rail { display: flex; flex-direction: column; gap: 8px; }
.m-th { all: unset; box-sizing: border-box; width: 72px; height: 88px; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--hd-border); position: relative; transition: opacity 150ms ease; }
.m-th img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; outline: 0 !important; }
.m-th:not(.on) { opacity: .78; } .m-th:not(.on):hover { opacity: 1; }
.m-th.on { outline: 2px solid var(--hd-accent); outline-offset: 2px; border-color: transparent; }
.m-hero { position: relative; aspect-ratio: 4 / 5; border-radius: 16px; overflow: hidden; border: 1px solid var(--hd-border); background: var(--hd-control); }
.m-hero > img { width: 100%; height: 100%; object-fit: cover; object-position: 52% 50%; display: block; border-radius: 0 !important; outline: 0 !important; }
.m-phone { width: 390px; max-width: 100%; margin: 0 auto; background: var(--hd-surface); border-radius: 24px; padding-bottom: 20px; display: flex; flex-direction: column; }
.m-top { display: flex; align-items: center; height: 52px; padding: 0 8px; }
.m-track { display: flex; gap: 8px; padding: 0 0 0 16px; overflow: hidden; }
.m-slide { position: relative; flex: 0 0 calc(100% - 48px); aspect-ratio: 4 / 5; border-radius: 16px; overflow: hidden; border: 1px solid var(--hd-border); background: var(--hd-control); }
.m-slide img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; outline: 0 !important; }
.m-info { padding: 8px 16px 0; display: flex; flex-direction: column; gap: 4px; } .m-info .t-h2 { margin-top: 2px; }
.m-inds { display: flex; gap: 32px; align-items: center; } .m-inds > div { display: flex; flex-direction: column; gap: 8px; }
.m-bars { display: flex; gap: 4px; width: 160px; } .m-bars i { flex: 1; height: 4px; border-radius: 4px; background: var(--hd-track); } .m-bars i.on { background: var(--hd-fg); } .m-bars i.cur { background: var(--hd-fg); opacity: .5; }
.m-chip-s { background: var(--hd-fg); color: var(--hd-bg); }
.m-reels { display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; }
.m-reelw { display: flex; flex-direction: column; gap: 4px; min-width: 0; }
.m-reel { position: relative; aspect-ratio: 9 / 16; border-radius: 16px; overflow: hidden; border: 1px solid var(--hd-border); background: var(--hd-control); color: #fff; }
.m-reel .m-ph { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; outline: 0 !important; }
.m-reel::before, .m-yt::before { content: ''; position: absolute; left: 0; right: 0; top: 0; height: 28%; background: linear-gradient(to bottom, rgba(13,14,18,.4), rgba(13,14,18,0)); z-index: 1; pointer-events: none; }
.m-reel::after, .m-yt::after { content: ''; position: absolute; left: 0; right: 0; bottom: 0; height: 46%; background: linear-gradient(to top, rgba(13,14,18,.78), rgba(13,14,18,0)); z-index: 1; pointer-events: none; }
.m-yt::after { height: 36%; }
.m-pl { position: absolute; left: 12px; top: 12px; width: 28px; height: 28px; border-radius: 50%; display: grid; place-items: center; background: rgba(255,255,255,.96); z-index: 2; box-shadow: 0 1px 3px rgba(16,20,38,.24); }
.m-dur { position: absolute; right: 12px; top: 12px; height: 24px; padding: 0 8px; border-radius: 8px; background: rgba(13,14,18,.64); color: #fff; font-size: 12px; font-weight: 600; display: inline-flex; align-items: center; z-index: 2; }
.m-dur.s { right: 4px; top: auto; bottom: 4px; height: 16px; padding: 0 4px; font-size: 11px; border-radius: 4px; }
.m-play { position: absolute; left: 50%; top: 50%; width: 48px; height: 48px; margin: -24px 0 0 -24px; border-radius: 50%; display: grid; place-items: center; background: rgba(255,255,255,.96); color: #121417; padding-left: 2px; z-index: 2; box-shadow: 0 2px 12px rgba(13,14,18,.36); }
.m-meta { position: absolute; left: 12px; right: 12px; bottom: 12px; z-index: 2; display: flex; flex-direction: column; gap: 8px; }
.m-who { display: flex; align-items: center; gap: 8px; min-width: 0; } .m-who b { font-size: 13px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; color: #fff; }
.m-av { width: 24px; height: 24px; border-radius: 50%; object-fit: cover; flex: none; border: 1.5px solid rgba(255,255,255,.9); box-sizing: border-box; } .m-who .av { width: 24px; height: 24px; font-size: 10px; border: 1.5px solid rgba(255,255,255,.9); box-sizing: border-box; }
.m-av.l { width: 40px; height: 40px; border: 0; }
.m-views { display: inline-flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 500; color: rgba(255,255,255,.92); }
.m-cap { margin-top: 8px; font-size: 13.5px; line-height: 18px; font-weight: 600; letter-spacing: -0.01em; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.m-ytw { display: flex; flex-direction: column; gap: 12px; }
.m-yt { position: relative; aspect-ratio: 16 / 9; border-radius: 16px; overflow: hidden; border: 1px solid var(--hd-border); background: var(--hd-control); color: #fff; }
.m-yt > img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; outline: 0 !important; }
.m-yt .m-dur { top: auto; bottom: 16px; right: 12px; } .m-yt .m-play { width: 56px; height: 56px; margin: -28px 0 0 -28px; }
.m-prog { position: absolute; left: 0; right: 0; bottom: 0; height: 4px; background: rgba(255,255,255,.32); z-index: 3; } .m-prog i { display: block; height: 100%; width: 38%; background: #fff; }
.m-ytb { display: flex; gap: 12px; align-items: flex-start; } .m-ytb > div { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px; } .m-ytb b { font-size: 15px; font-weight: 600; letter-spacing: -0.012em; line-height: 20px; } .m-ytb .vhex { vertical-align: -2px; }
.m-lr { align-items: center; gap: 16px; padding: 12px; }
.m-lt { position: relative; width: 56px; height: 100px; border-radius: 8px; overflow: hidden; flex: none; border: 1px solid var(--hd-border); } .m-lt img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; outline: 0 !important; }
.m-lr .tx b { font-size: 14.5px; } .m-st { display: inline-flex; align-items: center; gap: 6px; margin-top: 8px; font-size: 12.5px; color: var(--hd-fg-muted); }
.m-mos { display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(2, 1fr); gap: 4px; aspect-ratio: 2 / 1; border-radius: 16px; overflow: hidden; border: 1px solid var(--hd-border); }
.m-mos img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; outline: 0 !important; min-height: 0; } .m-mos img.b { grid-column: span 2; grid-row: span 2; }
.m-last { position: relative; display: block; min-height: 0; overflow: hidden; } .m-last img { position: absolute; inset: 0; }
.m-more { position: absolute; right: 8px; bottom: 8px; }
.m-ups { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
.m-tile { display: flex; flex-direction: column; gap: 8px; min-width: 0; }
.m-up { position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; border: 1px solid var(--hd-border); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; background: var(--hd-surface); }
.m-up > img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; border-radius: 0 !important; outline: 0 !important; }
.m-ok { position: absolute; right: 4px; bottom: 4px; width: 24px; height: 24px; border-radius: 50%; background: var(--hd-surface); display: grid; place-items: center; color: var(--hd-success); }
.m-dim { position: absolute; inset: 0; background: rgba(13,14,18,.56); color: #fff; display: grid; place-items: center; } .m-dim svg { grid-area: 1/1; } .m-dim b { grid-area: 1/1; font-size: 11px; font-weight: 600; }
.m-up.err { background: var(--hd-danger-subtle); border-color: transparent; color: var(--hd-danger-strong); } .m-up.err b { font-size: 12px; font-weight: 600; } .m-up.err .btn.link { font-size: 12px; color: var(--hd-danger-strong); }
.m-up.add { border: 1px dashed var(--hd-border-strong); background: none; color: var(--hd-fg-muted); } .m-up.add small { font-size: 12px; font-weight: 560; }
.m-fn { font-size: 11.5px; line-height: 14px; color: var(--hd-fg-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

/* nw2 grid must never overflow */
.sec.nw .grid.g3, .n-top.g3 { grid-template-columns: repeat(3, minmax(0, 1fr)); } .sec.nw .grid.g2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.sec.nw .n-stage > *, .sec.nw .field, .sec.nw .input { min-width: 0; max-width: 100%; }
.n-ta span { min-width: 0; overflow-wrap: anywhere; }
.m-pl { color: #121417; }
.m-top .btn.g, .m-top .btn.g .ic { color: var(--hd-fg); }
.m-frames { display: flex; gap: 8px; } .m-frames button { all: unset; box-sizing: border-box; position: relative; flex: 1; aspect-ratio: 9 / 16; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--hd-border); }
.m-frames img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; outline: 0 !important; }
.m-frames button.on { outline: 2px solid var(--hd-accent); outline-offset: 2px; border-color: transparent; }
.m-frames .m-cv { position: absolute; left: 4px; bottom: 4px; height: 16px; padding: 0 4px; border-radius: 4px; background: var(--hd-accent); color: #fff; font-size: 11px; font-weight: 600; display: inline-flex; align-items: center; }
.n-dz.drag { background: color-mix(in oklab, var(--hd-accent) 7%, var(--hd-surface)); }
.n-fr .btn.g, .n-fr .btn.g .ic { color: var(--hd-fg-muted); } .n-fr .btn.g:hover { color: var(--hd-fg); }
.n-avu:has(.up) { gap: 10px; }
.sec.nw .n-stage > .m-phone, .m-phone { width: 390px; max-width: 390px; align-self: center; flex: none; }
.m-inds { align-items: flex-start; } .m-inds > div { align-items: flex-start; }

/* ===== nw7 review ===== */
.n-pc { height: 100%; } .n-pb { flex: 1; } .n-pf { margin-top: auto; padding-top: 8px; }
.n-ft.sm { width: 24px; height: 24px; border-radius: 6px; box-shadow: var(--hd-shadow-e1); } .n-ft.sm .ic { color: var(--hd-fg-muted); }
.n-loc { display: inline-flex; align-items: center; gap: 8px; font-size: 13px; color: var(--hd-fg-muted); }
.n-bd.badge { top: 12px; left: 12px; height: 24px; box-shadow: 0 1px 2px rgba(16,20,38,.2); }
.n-bd.badge.success { background: color-mix(in oklab, var(--hd-success-subtle) 94%, var(--hd-surface)) !important; } .n-bd.badge.warning { background: color-mix(in oklab, var(--hd-warning-subtle) 94%, var(--hd-surface)) !important; } .n-bd.badge.neutral { background: var(--hd-surface) !important; }
.n-ph .n-disc { top: 8px; right: 8px; width: 32px; height: 32px; }
.n-rw b { font-size: 20px; line-height: 24px; } .n-rw { align-items: baseline; }
.n-sl .tape, .n-prog .tape { height: 8px; border-radius: 999px; background: var(--hd-track); box-shadow: inset 0 1px 2px rgba(16,20,38,.14); overflow: hidden; } .n-sl .tape i, .n-prog .tape i { border-radius: 999px; }
[data-theme="dark"] .n-sl .tape { box-shadow: inset 0 1px 2px rgba(0,0,0,.5); }
.n-brand { align-items: center; } .n-brand .vhex { vertical-align: 0; flex: none; }
.n-mention u { color: var(--hd-info-strong); }
.n-cc .n-pf .btn.p { width: 100%; }
.n-hc2 { align-items: center; }

/* ===== cut decoration ===== */
.n-meta { font-size: 13px; color: var(--hd-fg-muted); margin-top: auto; } .n-hb { gap: 4px; }
.n-ph2 > img { width: 104px; height: 104px; }
.n-dz.drag .n-ft { box-shadow: var(--hd-shadow-e1); transform: none; }
.n-loc .ic { color: var(--hd-fg-muted); }
.m-ups { grid-template-columns: repeat(3, 1fr); }
.m-lt { height: 80px; width: 48px; }
.n-meta { line-height: 32px; margin-top: auto; } .n-hb, .n-he { padding-top: 0; padding-bottom: 0; }
.n-sr .tx b { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.sec.nw .n-brand .av, .sec.nw .m-who .av { font-size: 11px !important; }
"""
