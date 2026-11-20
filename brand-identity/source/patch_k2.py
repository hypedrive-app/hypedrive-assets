p='/tmp/hdwm/kit2.py'; s=open(p).read()
s=s.replace("var(--hd-data-1)","var(--hd-chart)")
a=s.index("def header("); b=s.index("def shell(")
s=s[:a]+'''def header(crumbs, action=False):
    """Top bar: breadcrumb and bell only. The one primary CTA lives in the page header."""
    c = f'<span class="crumb" style="white-space:nowrap">' + f'{ic("chev", 14)}'.join(f"<b>{x}</b>" if i == len(crumbs)-1 else x for i, x in enumerate(crumbs)) + '</span>'
    return f'<div class="hdr">{c}<span class="sp"></span><span class="iconbtn">{ic("bell", 18)}<span class="badge-dot"></span></span></div>'

'''+s[b:]
s=s.replace("def shell(active, crumbs, page, theme=\"light\", action=True):","def shell(active, crumbs, page, theme=\"light\", action=False):")

a=s.index("def d_overview("); b=s.index("DESKTOP2 =")
new=r'''def d_overview(theme="light"):
    k = (stat("Active creators", "204", "+18%", True, spark=[12, 14, 13, 17, 19, 22, 26], uid="ov0" + theme)
         + stat("Reviews this week", "91", "+42%", True, spark=REV, kind="bars")
         + stat("Avg. rating", "4.7", kind="rating", uid="ovr" + theme)
         + stat("Cost per review", "₹ 1,495", "−4%", True, kind="compare", extra=(1495, 1560)))
    plats = [("Instagram", 58, "var(--hd-chart)"), ("YouTube", 27, "var(--hd-data-hl)"), ("Threads", 15, f"{M['300']}")]
    leg = "".join(f'<div><i style="background:{c}"></i><span>{n}</span><b>{v}%</b></div>' for n, v, c in plats)
    PEOPLE = {k: f"{STOCK}/people/{k}.jpg" for k in ("women-21", "women-44", "women-65", "men-12", "men-32")}
    revs = [("women-21", "Riya Sharma", True, "serum", "Glow serum", "Instagram", 5, "Used it every night for two weeks. Light, no smell, and my skin feels calmer.", "warning", "To check", "2m"),
            ("men-12", "Arjun Kapoor", False, "serum", "Glow serum", "Youtube", 4, "Good texture. The dropper leaks a little, but results showed in a week.", "warning", "To check", "18m"),
            ("men-32", "Kabir Nanda", True, "cream", "Night cream", "Instagram", 5, "Heavy but in a good way. Woke up with calmer, softer skin all week.", "success", "Approved", "52m")]
    def rstars(r): return '<span class="rv-st">' + "".join(ics("star", 14, "var(--hd-star)") if i < r else ic("star", 14, "var(--hd-track-strong)") for i in range(5)) + '</span>'
    tr = "".join(f'<div class="rv"><img class="rv-av" src="{PEOPLE[p]}" alt=""><div class="rv-who"><b>{n} {vhex(13) if v else ""}</b><small><img src="{PH[pi]}" alt="">{pn} · {soc(pl, 12, "currentColor")}</small></div>'
                 f'<p class="rv-q">“{q}”</p>{rstars(r)}<span class="badge {b}">{bl}</span><span class="rv-t num">{t}</span></div>' for p, n, v, pi, pn, pl, r, q, b, bl, t in revs)
    page = (f'<div class="ph"><div class="t"><div class="t-h1">Overview</div><p>Glow serum and 4 other campaigns · last 7 weeks</p></div><span class="chip">{ic("calendar", 16)}Last 7 weeks{ic("down", 14)}</span><button class="btn s sm">{ic("download", 16)}Export</button><button class="btn p sm">{ic("plus", 16)}New campaign</button></div>'
            f'<div class="grid g4" style="gap:14px">{k}</div>'
            f'<div class="grid" style="grid-template-columns:1.7fr 1fr;gap:14px"><div class="panel"><div class="phd"><b>Reviews over time</b><span class="t-small muted num">+ 117% in 7 weeks</span></div>'
            f'<div style="padding:10px 14px 2px">{line_chart(REV, WEEKS, 760, 206, None, PREV, 5, "ov" + theme)}</div><div class="legend" style="padding:0 18px 14px"><span><i style="background:var(--hd-chart)"></i>This period</span><span><i class="dash"></i>Previous period</span></div></div>'
            f'<div class="panel dcard"><div class="phd"><b>Where reviews go live</b></div><div class="db">{donut(plats, 150, 16, ("91", "reviews"))}<div class="lgd">{leg}</div></div></div></div>'
            f'<div class="sect"><div class="shd"><span class="l"><b class="t">Latest reviews</b><span class="t-small muted"><b class="num" style="color:var(--hd-fg)">23</b> waiting for you</span></span><button class="btn s sm">Open queue</button></div>'
            f'<div class="rvs">{tr}</div></div>')
    return shell("Overview", ["Lumen Labs", "Overview"], page, theme)

def d_campaigns():
    rows = [("serum", "Glow serum, 30 ml", "Live", "success", 84, 120, "₹ 1,04,160", REV), ("cream", "Night cream", "Live", "success", 42, 100, "₹ 41,580", [8, 12, 18, 20, 26, 33, 42]),
            ("mask", "Repair hair mask", "Draft", "neutral", 0, 80, "—", [0, 0, 0, 0, 0, 0, 0]), ("set", "Clear skin set", "Full", "neutral", 60, 60, "₹ 59,780", [10, 22, 35, 48, 55, 59, 60]),
            ("bottles", "Daily cleanser trio", "Live", "success", 18, 90, "₹ 16,740", [0, 2, 5, 8, 11, 15, 18])]
    tr = "".join(f'<tr class="{"sel-row" if i == 0 else ""}"><td><span class="check {"on" if i == 0 else ""}">{ic("check", 14, "#fff", 3) if i == 0 else ""}</span></td>'
                 f'<td><div class="flexw" style="flex-wrap:nowrap"><img src="{PH[k]}" style="width:40px;height:40px"><div><b>{n}</b><div class="t-cap muted">{f}/{tot} creators</div></div></div></td>'
                 f'<td><span class="badge {b}">{s}</span></td><td style="width:180px"><div class="tape" style="height:6px"><i style="width:{min(f/tot,1)*100:.0f}%"></i></div></td>'
                 f'<td class="num" style="text-align:right;font-weight:550">{sp_}</td><td>{spark(sp, 80, 24) if f else ""}</td><td style="text-align:right">{ic("more", 18)}</td></tr>'
                 for i, (k, n, s, b, f, tot, sp_, sp) in enumerate(rows))
    page = (f'<div class="ph"><div class="t"><div class="t-h1">Campaigns</div><p>5 campaigns · 3 live</p></div><button class="btn s sm">{ic("sliders", 16)}Filter</button><button class="btn p sm">{ic("plus", 16)}New campaign</button></div>'
            f'<div class="grid g4" style="gap:14px">' + stat("Campaigns", "5", kind="split", extra=[("3 live", 60, "var(--hd-success-solid)"), ("1 full", 20, "var(--hd-fg-subtle)"), ("1 draft", 20, "var(--hd-track-strong)")]) + stat("Spent this quarter", "₹ 2,22,260", "+31%", True, spark=[40, 62, 81, 120, 160, 190, 222], uid="cs") + stat("Reviews per week", "91", "+42%", True, spark=REV, kind="bars") + goal("Creators active", 204, 450) + '</div>'
            f'<div class="tabs"><span class="on">{ics("grid", 16, "var(--hd-accent)")}All <span class="cnt-b">5</span></span><span>{ics("live", 16, "var(--hd-tone-mint)")}Live <span class="cnt-b">3</span></span><span>{ics("success", 16, "var(--hd-tone-ink)")}Full <span class="cnt-b">1</span></span><span>{ics("edit", 16, "var(--hd-tone-ink)")}Drafts <span class="cnt-b">1</span></span></div>'
            f'<div class="banner"><span class="bi" style="background:{M['300']};color:{I['900']}">{icf("warning")}</span><div class="tx"><b>Clear skin set is full</b><small>All 60 slots filled. Add slots to keep it running.</small></div><button class="btn s sm">Close campaign</button><button class="btn p sm">{ic("plus", 16)}Add slots</button></div>'
            f'<div class="panel tblwrap"><table class="tbl"><tr><th></th><th><span class="th-sort">Campaign{ic("down", 12)}</span></th><th>Status</th><th>Slots</th><th style="text-align:right">Spent</th><th>Trend</th><th></th></tr>{tr}</table>'
            f'<div class="bulk"><span class="t-small"><b>1 selected</b></span><button class="btn s sm">Pause</button><button class="btn s sm">Duplicate</button></div></div>')
    return shell("Campaigns", ["Lumen Labs", "Campaigns"], page)

def d_review():
    PEOPLE = {"RS": "women-21", "AK": "men-12", "MJ": "women-44", "TN": "women-65"}
    revs = [("RS", "Riya Sharma", True, "@riya.glows", "18.4k", "2m", 5, "Used it every night for two weeks. Light, no smell, and my skin feels calmer.", ["serum", "bottles"]),
            ("AK", "Arjun Kapoor", False, "@arjun.k", "9.2k", "18m", 4, "Good texture. The dropper leaks a little, but results showed in a week.", ["flatlay"]),
            ("MJ", "Meera Joshi", True, "@meera.skin", "41k", "1h", 5, "My new nightly step. Brighter skin in about ten days, no breakouts.", ["bottles", "cream"]),
            ("TN", "Tanvi Nair", False, "@tanvi.n", "6.0k", "3h", 3, "Nice texture, but I couldn’t see much change yet.", []),
            ("DR", "Dev Rao", False, "@dev.rao", "12k", "4h", 4, "Absorbs fast and doesn’t leave a sticky layer. Would repurchase.", ["cream"])]
    def card(i, a, n, v, h, f, t, r, q, ms):
        av_ = f'<img class="av" src="{STOCK}/people/{PEOPLE[a]}.jpg" alt="">' if a in PEOPLE else av("DR", 3, 36)
        stars = '<span class="stars">' + "".join(ics("star", 14, "var(--hd-star)") if j < r else ic("star", 14, "var(--hd-track-strong)") for j in range(5)) + '</span>'
        th = f'<div class="th">{"".join(f"<img src={chr(34)}{PH[m]}{chr(34)} alt={chr(34)}{chr(34)}>" for m in ms)}</div>' if ms else ""
        return (f'<div class="panel rc2{" chk" if i < 2 else ""}{" open" if i == 0 else ""}"><span class="check {"on" if i < 2 else ""}">{ic("check", 14, "#fff", 3) if i < 2 else ""}</span>{av_}'
                f'<div class="bd"><div class="l1"><b>{n} {vhex(14) if v else ""}</b>{stars}</div><div class="l2">{h} · {f} followers · {t}</div><p>{q}</p></div>{th}</div>')
    cards = "".join(card(i, *r) for i, r in enumerate(revs))
    page = (f'<div class="rvw"><div class="rvl">'
            f'<div class="ph"><div class="t"><div class="t-h1">Reviews</div><p>23 waiting for you · median wait 4 h</p></div><div class="search" style="width:260px">{ic("search", 18)}Search reviews<span class="kbd">⌘K</span></div></div>'
            f'<div class="tabs"><span class="on">{ics("clock", 16, "var(--hd-tone-marigold)")}To check <span class="cnt-b">23</span></span><span>{ics("success", 16, "var(--hd-tone-mint)")}Approved</span><span>{ics("danger", 16, "var(--hd-tone-vermilion)")}Rejected</span></div>'
            f'<div class="toolbar"><span class="chip"><img src="{PH["serum"]}" style="width:18px;height:18px">Glow serum{ic("x", 14)}</span><span class="chip">{ic("star", 16)}All ratings{ic("down", 14)}</span><span class="chip">{soc("Instagram", 14)}Instagram{ic("down", 14)}</span><span class="sp" style="flex:1"></span><button class="btn s sm">Reject</button><button class="btn p sm">{ic("check", 16)}Approve 2</button></div>'
            f'<div class="rvlist">{cards}</div></div>'
            f'<div class="drawer"><div class="flexw" style="justify-content:space-between"><b class="t-h2">Riya’s review</b>{ic("x", 20)}</div>'
            f'<div style="position:relative;border-radius:14px;overflow:hidden;height:200px;flex:none"><img src="{PH["serum"]}" style="width:100%;height:100%;border-radius:0;object-fit:cover"><span class="badge neutral" style="position:absolute;left:12px;bottom:12px;background:rgba(16,20,38,.7);color:#fff;box-shadow:none">{ic("play", 14)}Reel · 0:24</span></div>'
            f'<div class="rvtxt"><div class="flexw" style="justify-content:space-between"><span class="stars">{"".join(ics("star", 16, "var(--hd-star)") for _ in range(5))}</span><span class="t-small muted">@riya.glows · 18.4k followers</span></div>'
            f'<p>Used it every night for two weeks. Light, no smell, and my skin feels calmer.</p><div class="th"><img src="{PH["serum"]}" alt=""><img src="{PH["bottles"]}" alt=""></div></div>'
            f'<div class="dl"><div class="flexw t-small"><span class="muted" style="width:96px">Platform</span>{soc("Instagram", 16)}Instagram</div><div class="flexw t-small"><span class="muted" style="width:96px">Link</span><span style="color:var(--hd-link)">instagram.com/p/C9x…</span></div>'
            f'<div class="flexw t-small"><span class="muted" style="width:96px">Brand tag</span><span class="badge success">Found</span></div><div class="flexw t-small"><span class="muted" style="width:96px">Payout</span><b class="num">₹ 1,240</b></div></div>'
            f'<div class="notice success">{icf("success")}<span>Link is public and the brand tag is present.</span></div><div style="flex:1"></div>'
            f'<div class="flexw"><button class="btn s" style="flex:1">Reject</button><button class="btn p" style="flex:2">Approve and pay</button></div><span class="t-cap muted" style="text-align:center">Press {kbd("A")} to approve, {kbd("R")} to reject</span></div></div>')
    return shell("Reviews", ["Lumen Labs", "Reviews"], page)

'''
s=s[:a]+new+s[b:]
s=s.replace('{header(["Lumen Labs", "Reviews", "To check"])}','{header(["Lumen Labs", "Reviews"])}')
open(p,'w').write(s)
