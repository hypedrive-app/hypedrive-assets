import re
p='/tmp/hdwm/uikit2.py'; s=open(p).read()
s=s.replace("var(--hd-data-1)","var(--hd-chart)")
# line chart headroom + compact tooltip
s=s.replace("pl, pr, pt, pb = 36, 28, 14, 26","pl, pr, pt, pb = 36, 28, 30, 26")
s=s.replace("below = ty < h*0.42 ","below = ty < 40 ")
s=s.replace('''<span class="muted">{labels[tip_i]}</span>'
               f'<b class="num">{series[tip_i]}</b>{f"<span class=muted>vs {compare[tip_i]}</span>" if compare else ""}</div></div>')''','''<span class="muted">{labels[tip_i]}</span>'
               f'<b class="num">{series[tip_i]}</b>{f"<span class=muted>vs {compare[tip_i]}</span>" if compare else ""}</div></div>')''')
# rating star: clean partial via inline SVG clipPath
old=s[s.index("    elif kind == \"rating\":"):s.index("    elif kind == \"compare\":")]
new='''    elif kind == "rating":
        r = float(value); full = int(r); frac = r - full
        body = '<div class="srate">' + "".join(ics("star", 16, "var(--hd-star)") if i < full else (partial_star(frac, f"{uid}{i}") if i == full and frac > .05 else ic("star", 16, "var(--hd-track-strong)")) for i in range(5)) + '</div>'
'''
s=s.replace(old,new)
helper='''
STAR18 = "M16.963,6.786c-.088-.271-.323-.469-.605-.51l-4.62-.671L9.672,1.418c-.252-.512-1.093-.512-1.345,0l-2.066,4.186-4.62,.671c-.282,.041-.517,.239-.605,.51-.088,.271-.015,.57,.19,.769l3.343,3.258-.79,4.601c-.048,.282,.067,.566,.298,.734,.231,.167,.538,.189,.79,.057l4.132-2.173,4.132,2.173c.11,.058,.229,.086,.349,.086,.155,0,.31-.048,.441-.143,.231-.168,.347-.452,.298-.734l-.79-4.601,3.343-3.258c.205-.199,.278-.498,.19-.769Z"
def partial_star(frac, uid):
    """One star filled to `frac` of its width: grey base star + gold star under an inline clipPath (no mask)."""
    x = 1 + 16*frac
    return (f'<svg class="ic icf" width="16" height="16" viewBox="0 0 18 18" aria-hidden="true"><defs><clipPath id="ps{uid}"><rect x="0" y="0" width="{x:.2f}" height="18"/></clipPath></defs>'
            f'<path d="{STAR18}" fill="var(--hd-track-strong)"/><path d="{STAR18}" fill="var(--hd-star)" clip-path="url(#ps{uid})"/></svg>')

def stat('''
s=s.replace("\ndef stat(",helper,1)
# compare labels
old=s[s.index("        body = (f'<div class=\"cmp2\">"):s.index("    elif kind == \"split\":")]
new='''        body = (f'<div class="cmp2"><div><span>Now</span><div class="bar thin"><i style="width:{cur/mx*100:.0f}%"></i></div><b class="num">₹ {cur:,}</b></div>'
                f'<div><span>Before</span><div class="bar thin"><i style="width:{prev/mx*100:.0f}%;background:var(--hd-track-strong)"></i></div><b class="num">₹ {prev:,}</b></div></div>')
'''
s=s.replace(old,new)
s=s.replace('grid-template-columns: 48px 1fr; align-items: center; gap: 8px; font-size: 12px;','grid-template-columns: 44px 1fr 52px; align-items: center; gap: 8px; font-size: 12px;')
s=s.replace(".stat .vz .srate .ic {{ width: 18px; height: 18px; }}",".stat .vz .srate .ic {{ width: 18px; height: 18px; }}")
s=s.replace(".ctip {{ position: absolute; transform: translate(-50%, calc(-100% - 14px));",".ctip {{ position: absolute; transform: translate(-50%, calc(-100% - 12px));")
s=s.replace("flex-direction: column; gap: 1px; white-space: nowrap; box-shadow: var(--hd-shadow-e2); }}","flex-direction: row; align-items: baseline; gap: 8px; white-space: nowrap; box-shadow: var(--hd-shadow-e2); pointer-events: none; }}")
s=s.replace(".ctip b {{ font-size: 15px;",".ctip b {{ font-size: 14px;").replace(".ctip.below {{ transform: translate(-50%, 14px); }}",".ctip.below {{ transform: translate(-50%, 12px); }}")
css=r'''
/* ---- desktop pass: one primary CTA in the page header, grey filled controls, review queue layout ---- */
:root, [data-theme] { --hd-chart: var(--hd-accent); } [data-theme="dark"] { --hd-chart: var(--hd-data-1); }
.shell .ph .btn.sm, .shell .ph .chip { height: 44px; border-radius: 12px; font-size: 14px; padding: 0 16px; }
.shell .ph .btn.sm:has(> .ic:first-child) { padding-left: 14px; } .shell .ph .btn.p.sm { box-shadow: inset 0 -1px 0 var(--hd-accent-pressed); }
.shell .ph .chip, .shell .toolbar .chip, .shell .toolbar .chip.on { background: var(--hd-control); border: 0; box-shadow: none; color: var(--hd-fg); font-weight: 550; }
.shell .toolbar .chip, .shell .toolbar .btn.sm { height: 36px; border-radius: 10px; }
.shell .toolbar .chip .ic { color: var(--hd-fg-muted); }
.shell .toolbar .chip img { border-radius: 5px; }
.shell .ph .chip .ic { color: var(--hd-fg-muted); }
.shell .mn > .pg { flex: 1; min-height: 0; }
/* overview: latest reviews as separate row cards */
.sect .shd { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; } .sect .shd .l { flex: 1; display: flex; align-items: baseline; gap: 10px; } .sect .shd b.t { font-size: 15px; font-weight: 600; letter-spacing: -.012em; }
.shell .sect .rvs { gap: 8px; }
.shell .rv { border: 1px solid var(--hairline); border-radius: 12px; background: var(--hd-surface-raised); padding: 10px 16px; }
.shell .rv-av { width: 40px; height: 40px; }
/* donut card */
.dcard { display: flex; flex-direction: column; } .dcard .db { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 18px; padding: 4px 22px 20px; }
.lgd { width: 100%; display: flex; flex-direction: column; gap: 10px; } .lgd > div { display: flex; align-items: center; gap: 10px; font-size: 13.5px; } .lgd i { width: 8px; height: 8px; border-radius: 3px; flex: none; } .lgd span { flex: 1; } .lgd b { font-weight: 600; font-variant-numeric: tabular-nums; }
/* campaigns bulk bar */
.shell .tblwrap { position: relative; overflow: hidden; padding-bottom: 68px; }
.bulk { position: absolute; left: 50%; bottom: 12px; transform: translateX(-50%); height: 44px; display: flex; align-items: center; gap: 8px; padding: 0 6px 0 16px; border-radius: 12px; background: var(--hd-surface-raised); box-shadow: var(--hd-shadow-e2), 0 0 0 1px var(--hairline); white-space: nowrap; }
.bulk .btn.sm { height: 32px; } .bulk .t-small { margin-right: 6px; }
/* review queue */
.shell .pg:has(> .rvw) { padding: 0; gap: 0; }
.rvw { flex: 1; min-height: 0; display: grid; grid-template-columns: minmax(0, 1fr) 380px; grid-template-rows: minmax(0, 1fr); }
.rvl { padding: 24px 28px 0; display: flex; flex-direction: column; gap: 16px; min-height: 0; min-width: 0; overflow: hidden; }
.rvlist { display: flex; flex-direction: column; gap: 8px; flex: 1; min-height: 0; overflow: hidden; }
.shell .rc2 { height: 120px; flex: none; box-sizing: border-box; display: grid; grid-template-columns: 22px 36px minmax(0, 1fr) auto; column-gap: 14px; align-items: start; padding: 14px 16px; border-radius: 12px; box-shadow: none; background: var(--hd-surface-raised); }
.rc2 .check { margin-top: 7px; } .rc2 > img.av { width: 36px; height: 36px; border-radius: 50%; object-fit: cover; margin-top: 2px; }
.rc2 .bd { min-width: 0; display: flex; flex-direction: column; gap: 2px; }
.rc2 .l1 { display: flex; align-items: center; gap: 10px; } .rc2 .l1 b { font-size: 14px; font-weight: 600; display: inline-flex; align-items: center; gap: 4px; } .rc2 .l1 .stars { gap: 1px; }
.rc2 .l2 { font-size: 12.5px; color: var(--hd-fg-muted); } .rc2 .bd p { margin: 4px 0 0; font-size: 13.5px; line-height: 19px; color: var(--hd-fg); display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
.rc2 .th { display: flex; gap: 8px; } .rc2 .th img { width: 72px; height: 72px; border-radius: 8px; object-fit: cover; }
.shell .rc2.chk { background: var(--hd-accent-subtle); }
.shell .rc2.open { box-shadow: 0 0 0 2px var(--hd-accent); border-color: transparent; }
.shell .drawer { box-shadow: none; height: 100%; box-sizing: border-box; min-height: 0; overflow: hidden; padding: 20px; gap: 14px; }
.drawer .rvtxt { display: flex; flex-direction: column; gap: 8px; } .drawer .rvtxt p { margin: 0; font-size: 14px; line-height: 21px; }
.drawer .rvtxt .th { display: flex; gap: 8px; } .drawer .rvtxt .th img { width: 72px; height: 72px; border-radius: 8px; object-fit: cover; }
.drawer .dl { display: flex; flex-direction: column; gap: 8px; }
.drawer .sec-l { font-size: 12.5px; font-weight: 550; color: var(--hd-fg-subtle); }
'''
css=css.replace("{","{{").replace("}","}}")
idx=s.rindex('"""')
s=s[:idx]+css+s[idx:]
open(p,'w').write(s)
