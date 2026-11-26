# Layer (xmd): mediator pages. Kit components are WIDENED from xr3 (dm-) and xr4 (mn-) so they work in phones; only page layout is new (md-/v4-).
import re
def _widen():
    import xr3, xr4
    out = []
    pat = re.compile(r'([^{}@]+)\{([^{}]*)\}')
    for src in (xr3.XR3, xr4.XR4):
        for sel, body in pat.findall(re.sub(r'/\*.*?\*/', '', src, flags=re.S)):
            keep = []
            for s in sel.split(','):
                s = s.strip()
                m = re.match(r'^(\[data-theme="dark"\] )?(\.sec\.dm|\.mn-sec) (\.(dm|mn)-[a-z0-9]+.*)$', s)
                if m and not re.match(r'\.dm-(grp|gh|row|cell|lbl)\b|\.mn-(grid|blk)', m.group(3)):
                    keep.append((m.group(1) or "") + ".phone " + m.group(3))
            if keep: out.append(", ".join(keep) + " {" + body + "}")
    return "\n".join(out)
KIT_WIDE = _widen()

XMD = KIT_WIDE + """
.phone .scr:has(.md-pg) { background: var(--hd-canvas); }
.phone .md-pg { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 12px; padding: 0 16px 12px; background: var(--hd-canvas); font-family: var(--font-ui); color: var(--hd-fg); }
.phone .md-pg > * { flex: none; }
.phone .md-bar { height: 44px; display: flex; align-items: center; justify-content: space-between; padding: 0 4px; margin: 0 -4px; }
.phone .md-bar .l, .phone .md-bar .r { display: flex; align-items: center; gap: 18px; }
.phone .md-bar .bell { position: relative; display: flex; } .phone .md-bar .bell i { position: absolute; top: -1px; right: 0; width: 8px; height: 8px; border-radius: 50%; background: var(--hd-tone-vermilion); box-shadow: 0 0 0 2px var(--hd-canvas); }
.phone .md-av { border-radius: 50%; object-fit: cover; flex: none; display: block; } .phone .md-av.s32 { width: 32px; height: 32px; } .phone .md-av.s40 { width: 40px; height: 40px; } .phone .md-av.s64 { width: 64px; height: 64px; }
.phone .md-hd h1, .phone .md-top h1 { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 0; }
.phone .md-hd { margin: 0 4px; } .phone .md-hd p { margin: 2px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.phone .md-top { height: 48px; display: flex; align-items: center; justify-content: space-between; margin: 0 4px; padding-top: 2px; }
.phone .md-sh { display: flex; align-items: baseline; justify-content: space-between; margin: 4px 4px -4px; }
.phone .md-sh h2 { font-family: var(--font-brand); font-size: 18px; line-height: 24px; font-weight: 650; margin: 0; } .phone .md-sh span { font-size: 14px; font-weight: 600; color: var(--hd-link); } .phone .md-sh span b { color: var(--hd-fg); font-weight: 650; }
.phone .md-pg .tabs { margin: 0 -16px; padding: 0 20px; }
.phone .md-pg .chiprow, .phone .md-chips { display: flex; gap: 8px; }
.phone .md-pg .row .lead, .phone .md-pg .row img.lead { width: 48px; height: 48px; border-radius: 10px; object-fit: cover; flex: none; }
.phone .md-pg .row .tx small { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.phone .md-pg .warn { color: var(--hd-warning-strong); font-style: normal; font-weight: 600; }
.phone .md-pg .lk { font-style: normal; font-weight: 600; font-size: 14px; color: var(--hd-link); flex: none; }
/* today: kit dm-ns as the payback action card, kit cv-wal as the Ink money card */
.phone .md-pg .dm-ns .badge { align-self: flex-start; width: fit-content; }
.phone .md-pg .dm-ns { flex-wrap: wrap; } .phone .md-pg .dm-ns .tx { flex: 1; } .phone .md-pg .dm-ns .btn { flex: 0 0 100%; }
.phone .md-pg .dm-ns img.md-pf { width: 64px; height: 64px; border-radius: 50%; }
.phone .md-pg .cv-wal { margin: 0; }
.phone .md-pg .cv-wal .wd { border: 0; }
/* deals: kit campaign card (dm-cc) full width, photo shorter */
.phone .md-pg .dm-cc .dm-ph { aspect-ratio: auto; height: 150px; }
.phone .md-pg .dm-cc .dm-pay { gap: 8px; } .phone .md-pg .dm-cc .dm-ft .btn { flex: none; }
.phone .md-pg .dm-cc .dm-cb { gap: 4px; }
/* store card: dm-cc with a three-photo strip */
.phone .md-pg .v4-strip { display: grid; grid-template-columns: 1.3fr 1fr 1fr; gap: 2px; height: 72px; background: var(--hd-canvas); } .phone .md-pg .v4-strip img { width: 100%; height: 72px; object-fit: cover; display: block; border-radius: 0; }
.phone .md-pg .v4-link { display: flex; align-items: center; gap: 8px; height: 40px; padding: 0 12px; margin-top: 6px; border-radius: 10px; background: var(--hd-surface); border: 1px solid var(--hd-edge); font-size: 14px; color: var(--hd-fg-muted); }
.phone .md-pg .v4-sw { display: flex; align-items: center; gap: 12px; margin-top: 6px; } .phone .md-pg .v4-sw b { flex: 1; font-size: 15px; font-weight: 600; }
.phone .md-pg .v4-btns { display: flex; gap: 8px; margin-top: 8px; } .phone .md-pg .v4-btns .btn { flex: 1; }
/* sheets */
.phone .md-sheet { padding: 8px 16px 28px; display: flex; flex-direction: column; gap: 12px; }
.phone .md-sh2 { display: flex; justify-content: space-between; align-items: flex-start; }
.phone .md-sh2 small { font-size: 13px; font-weight: 600; color: var(--hd-fg-muted); }
.phone .md-sh2 h2 { margin: 2px 0 0; font: 700 24px/28px var(--font-brand); letter-spacing: -.02em; }
.phone .md-x { color: var(--hd-fg-muted); display: flex; padding-top: 4px; }
.phone .md-sheet .btn.lg { height: 48px !important; }
.phone .md-sl { display: flex; flex-direction: column; gap: 4px; } .phone .md-sl .t { display: flex; justify-content: space-between; align-items: baseline; } .phone .md-sl .t b { font-size: 15px; font-weight: 600; } .phone .md-sl .t span { font-size: 15px; font-weight: 600; }
.phone .md-sl .slider { margin: 10px 0 8px; } .phone .md-sl small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .md-note { margin: 0; text-align: center; font-size: 13px; color: var(--hd-fg-muted); }
.phone .md-sheet .dm-mb .tot b { font-size: 34px; line-height: 40px; }
.phone .md-sheet .row.no { opacity: .6; } .phone .md-sheet .row small { white-space: normal; }
.phone .md-sheet .row .tick { color: var(--hd-accent); display: flex; flex: none; }
/* enrollment */
.phone .md-pg .dm-po { padding: 14px 16px 16px !important; } .phone .md-pg .dm-po6 .btn { margin-top: 14px; }
.phone .md-pg .dm-jr { padding: 18px 4px 16px; } .phone .md-pg .dm-jr .s { font-size: 12px; text-align: center; white-space: nowrap; }
.phone .md-pg .md-hd + .cv-wal { margin-top: 4px; }
.phone .md-pg .v4-two { display: flex; gap: 8px; } .phone .md-pg .v4-two .btn { flex: 1; }
/* wallet / trust */
.phone .md-pg .mn-gl { width: 48px; height: 48px; display: block; } .phone .md-pg .mn-gl img { width: 48px; height: 48px; border-radius: 10px; object-fit: cover; display: block; }
.phone .md-pg .mn-card { overflow: hidden; } .phone .md-pg .mn-row { min-height: 60px; }
.phone .md-pg .v4-score { display: flex; align-items: center; justify-content: space-between; gap: 12px; }
.phone .md-pg .dm-po .dm-kv:first-of-type { margin-top: 10px; } .phone .md-pg .dm-kv.mute b { color: var(--hd-fg-subtle); }
.phone .md-pg .notice { align-items: center; }
/* dock */
.phone .md-dock { height: 64px; flex: none; display: flex; border-top: 1px solid var(--hd-edge); background: var(--hd-surface); }
.phone .md-di { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 8px; gap: 3px; font-size: 11px; font-weight: 560; color: var(--hd-fg-subtle); }
.phone .md-di.on { color: var(--hd-link); }
"""
XMD += """
[data-theme="dark"] .phone .md-pg .ringw > svg:not(:first-child) { stroke: #9db6ff; }
.phone .md-pg .v4-score .mix { margin-bottom: 8px; }
.phone .md-pg { padding-bottom: 20px; }
"""
XMD += """
.phone .md-pg .md-chips .chip { background: var(--hd-surface); border: 1px solid var(--hd-edge); }
.phone .md-pg .md-chips .chip.on { background: var(--hd-accent-subtle); border-color: var(--hd-edge); color: var(--hd-link); }
.phone .md-pg .v4-strip, .phone .md-pg .v4-strip img { height: 56px; }
.phone .md-sheet .md-sh2 + .md-sl { margin-top: 4px; }
"""
XMD += """
.phone .md-pg .md-money { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 18px; padding: 16px; display: flex; flex-direction: column; gap: 4px; }
.phone .md-money small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .md-money .big { display: flex; align-items: center; justify-content: space-between; }
.phone .md-money .big b { font: 700 38px/44px var(--font-brand); letter-spacing: -.02em; color: var(--hd-fg); }
.phone .md-money p { margin: 0; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); } .phone .md-money p span { color: var(--hd-fg); font-weight: 600; }
.phone .md-money .ft { display: flex; align-items: center; gap: 8px; margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--hd-edge); font-size: 14px; } .phone .md-money .ft span { flex: 1; color: var(--hd-fg-muted); }
"""
XMD += """
.phone .md-pg .dm-cc .dm-ph.v4-strip { height: 64px; aspect-ratio: auto; } .phone .md-pg .dm-cc .v4-strip img { height: 64px; }
"""
