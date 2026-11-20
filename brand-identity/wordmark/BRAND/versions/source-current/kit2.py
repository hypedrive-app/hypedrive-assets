"""New kit sections (charts, shell & navigation, more components) and the redesigned desktop screens."""
from uikit2 import *

WEEKS = ["Oct 6", "Oct 13", "Oct 20", "Oct 27", "Nov 3", "Nov 10", "Nov 17"]
REV = [42, 58, 64, 61, 77, 84, 91]; PREV = [30, 41, 48, 52, 55, 60, 66]

def sidebar2(active, theme="light"):
    groups = [("Workspace", [("overview", "Overview", ""), ("campaign", "Campaigns", "5"), ("star", "Reviews", "23"), ("users", "Creators", "")]),
              ("Money", [("wallet", "Wallet", ""), ("payouts", "Payouts", ""), ("reports", "Reports", "")])]
    nav = ""
    for h, items in groups:
        nav += f'<div class="sbh">{h}</div>'
        for i, n, c in items:
            cnt = f'<span class="cnt {"hot" if n == "Reviews" else ""}">{c}</span>' if c else ""
            nav += f'<div class="nav {"on" if n == active else ""}">{ics(i, 18) if n == active else ic(i, 18)}{n}{cnt}</div>'
    return (f'<aside class="sb"><img src="{LOGO[theme]}" alt="Hypedrive" style="height:24px;align-self:flex-start;margin:4px 8px 14px"><div class="ws" style="background:var(--hd-surface-raised);box-shadow:0 0 0 1px var(--hairline),var(--hd-shadow-e1)">{av("LL", 2, 28)}<div style="flex:1"><b>Lumen Labs</b><small>Brand workspace</small></div>{ic("down", 16)}</div>'
            f'<div class="sbsearch">{ic("search", 16)}<span class="q">Search campaigns, creators</span>{kbd("⌘K")}</div>{nav}'
            f'<div class="sbfoot"><div class="nav">{ic("help", 18)}Help</div><div class="nav">{ic("settings", 18)}Settings</div>'
            f'<div class="me">{av("AM", 2, 32)}<div style="flex:1;min-width:0"><b>Aditi Mehra</b><small>aditi@lumenlabs.in</small></div>{ic("more", 18)}</div></div></aside>')

def header(crumbs, action=False):
    """Top bar: breadcrumb and bell only. The one primary CTA lives in the page header."""
    c = f'<span class="crumb" style="white-space:nowrap">' + f'{ic("chev", 14)}'.join(f"<b>{x}</b>" if i == len(crumbs)-1 else x for i, x in enumerate(crumbs)) + '</span>'
    return f'<div class="hdr">{c}<span class="sp"></span><span class="iconbtn">{ic("bell", 18)}<span class="badge-dot"></span></span></div>'

def shell(active, crumbs, page, theme="light", action=False):
    return f'<div class="shell" data-theme="{theme}">{sidebar2(active, theme)}<div class="mn">{header(crumbs, action)}<div class="pg">{page}</div></div></div>'

def d_overview(theme="light"):
    k = (stat("Active creators", "204", "+18%", True, spark=[12, 14, 13, 17, 19, 22, 26], uid="ov0" + theme)
         + stat("Reviews this week", "91", "+42%", True, spark=REV, kind="bars")
         + stat("Avg. rating", "4.7", kind="rating", uid="ovr" + theme)
         + stat("Cost per review", "₹1,495", "−4%", True, kind="compare", extra=(1495, 1560)))
    plats = [("Instagram", 58, "var(--hd-chart)"), ("YouTube", 27, "var(--hd-data-hl)"), ("Threads", 15, "var(--hd-brand-marigold)")]
    leg = "".join(f'<div><i style="background:{c}"></i><span>{n}</span><b>{v}%</b></div>' for n, v, c in plats)
    PEOPLE = {k: f"{STOCK}/people/{k}.jpg" for k in ("women-68", "women-44", "women-65", "men-12", "men-32")}
    revs = [("women-68", "Riya Sharma", True, "serum", "Glow serum", "Instagram", 5, "Used it every night for two weeks. Light, no smell, and my skin feels calmer.", "warning", "To check", "2m"),
            ("men-12", "Arjun Kapoor", False, "serum", "Glow serum", "Youtube", 4, "Good texture. The dropper leaks a little, but results showed in a week.", "warning", "To check", "18m"),
            ("KN", "Kabir Nanda", True, "cream", "Night cream", "Instagram", 5, "Heavy but in a good way. Woke up with calmer, softer skin all week.", "success", "Approved", "52m")]
    def rstars(r): return '<span class="rv-st">' + "".join(ics("star", 14, "var(--hd-star)") if i < r else ic("star", 14, "var(--hd-track-strong)") for i in range(5)) + '</span>'
    rvav = lambda p: av(p, 4, 40) if p == "KN" else "<img class=\"rv-av\" src=\"" + PEOPLE[p] + "\" alt=\"\">"
    tr = "".join(f'<div class="rv">{rvav(p)}<div class="rv-who"><b>{n} {vhex(13) if v else ""}</b><small><img src="{PH[pi]}" alt="">{pn} · {soc(pl, 12, "currentColor")}</small></div>'
                 f'<p class="rv-q">“{q}”</p>{rstars(r)}<span class="badge {b}">{bl}</span><span class="rv-t num">{t}</span></div>' for p, n, v, pi, pn, pl, r, q, b, bl, t in revs)
    page = (f'<div class="ph"><div class="t"><div class="t-h1">Overview</div><p>Glow serum and 4 other campaigns · last 7 weeks</p></div><span class="chip">{ic("calendar", 16)}Last 7 weeks{ic("down", 14)}</span><button class="btn s sm">{ic("download", 16)}Export</button><button class="btn p sm">{ic("plus", 16)}New campaign</button></div>'
            f'<div class="grid g4" style="gap:14px">{k}</div>'
            f'<div class="grid" style="grid-template-columns:1.7fr 1fr;gap:14px"><div class="panel"><div class="phd"><b>Reviews over time</b><span class="t-small muted num">+ 117% in 7 weeks</span></div>'
            f'<div style="padding:10px 14px 2px">{line_chart(REV, WEEKS, 660, 214, None, PREV, 5, "ov" + theme)}</div><div class="legend" style="padding:0 18px 14px"><span><i style="background:var(--hd-chart)"></i>This period</span><span><i class="dash"></i>Previous period</span></div></div>'
            f'<div class="panel dcard"><div class="phd"><b>Where reviews go live</b></div><div class="db">{donut(plats, 136, 16, ("91", "reviews"))}<div class="lgd">{leg}</div></div></div></div>'
            f'<div class="sect"><div class="shd"><span class="l"><b class="t">Latest reviews</b><span class="t-small muted"><b class="num" style="color:var(--hd-fg)">23</b> waiting for you</span></span><button class="btn s sm">Open queue</button></div>'
            f'<div class="rvs">{tr}</div></div>')
    return shell("Overview", ["Lumen Labs", "Overview"], page, theme)

def d_campaigns():
    rows = [("serum", "Glow serum, 30 ml", "Live", "success", 84, 120, "₹1,04,160", REV), ("cream", "Night cream", "Live", "success", 42, 100, "₹41,580", [8, 12, 18, 20, 26, 33, 42]),
            ("mask", "Repair hair mask", "Draft", "neutral", 0, 80, "—", [0, 0, 0, 0, 0, 0, 0]), ("set", "Clear skin set", "Full", "neutral", 60, 60, "₹58,800", [10, 22, 35, 48, 55, 59, 60]),
            ("bottles", "Daily cleanser trio", "Live", "success", 18, 90, "₹11,520", [0, 2, 5, 8, 11, 15, 18])]
    tr = "".join(f'<tr class="{"sel-row" if i == 0 else ""}"><td><span class="check {"on" if i == 0 else ""}">{ic("check", 14, "#fff", 3) if i == 0 else ""}</span></td>'
                 f'<td><div class="flexw" style="flex-wrap:nowrap"><img src="{PH[k]}" style="width:40px;height:40px"><div><b>{n}</b><div class="t-cap muted">{f}/{tot} creators</div></div></div></td>'
                 f'<td><span class="badge {b}">{s}</span></td><td style="width:180px"><div class="tape{" ok" if f >= tot else ""}"><i style="width:{min(f/tot,1)*100:.0f}%"></i></div></td>'
                 f'<td class="num" style="text-align:right;font-weight:550">{sp_}</td><td>{spark(sp, 80, 24) if f else ""}</td><td style="text-align:right">{ic("more", 18)}</td></tr>'
                 for i, (k, n, s, b, f, tot, sp_, sp) in enumerate(rows))
    page = (f'<div class="ph"><div class="t"><div class="t-h1">Campaigns</div><p>5 campaigns · 3 live</p></div><button class="btn s sm">{ic("sliders", 16)}Filter</button><button class="btn p sm">{ic("plus", 16)}New campaign</button></div>'
            f'<div class="grid g4" style="gap:14px">' + stat("Campaigns", "5", kind="split", extra=[("3 live", 60, "var(--hd-success-solid)"), ("1 full", 20, "var(--hd-fg-subtle)"), ("1 draft", 20, "var(--hd-track-strong)")]) + stat("Spent this quarter", "₹2,16,060", "+31%", True, spark=[40, 62, 81, 120, 160, 190, 222], uid="cs") + stat("Reviews per week", "91", "+42%", True, spark=REV, kind="bars") + goal("Creators active", 204, 450) + '</div>'
            f'<div class="tabs"><span class="on">{ics("grid", 16, "var(--hd-accent)")}All <span class="cnt-b">5</span></span><span>{ics("live", 16, "var(--hd-tone-mint)")}Live <span class="cnt-b">3</span></span><span>{ics("success", 16, "var(--hd-tone-ink)")}Full <span class="cnt-b">1</span></span><span>{ics("edit", 16, "var(--hd-tone-ink)")}Drafts <span class="cnt-b">1</span></span></div>'
            f'<div class="banner"><span class="bi" style="background:{M['300']};color:{I['900']}">{icf("warning")}</span><div class="tx"><b>Clear skin set is full</b><small>All 60 slots filled. Add slots to keep it running.</small></div><button class="btn s sm">Close campaign</button><button class="btn p sm">{ic("plus", 16)}Add slots</button></div>'
            f'<div class="panel tblwrap"><table class="tbl"><tr><th></th><th><span class="th-sort">Campaign{ic("down", 12)}</span></th><th>Status</th><th>Slots</th><th style="text-align:right">Spent</th><th>Trend</th><th></th></tr>{tr}</table>'
            f'<div class="bulk"><span class="t-small"><b>1 selected</b></span><button class="btn s sm">Pause</button><button class="btn s sm">Duplicate</button></div></div>')
    return shell("Campaigns", ["Lumen Labs", "Campaigns"], page)

def d_review():
    PEOPLE = {"RS": "women-68", "AK": "men-12", "MJ": "women-65", "TN": "women-44"}
    PLAT = {"RS": "Instagram", "AK": "Youtube", "MJ": "Instagram", "TN": "Instagram", "DR": "Youtube"}
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
                f'<div class="bd"><div class="l1"><b>{n} {vhex(14) if v else ""}</b>{stars}</div><div class="l2"><span class="x-plat">{soc(PLAT.get(a, "Instagram"), 14)}{h}</span> · {f} followers · {t}</div><p>{q}</p></div>{th}</div>')
    cards = "".join(card(i, *r) for i, r in enumerate(revs))
    page = (f'<div class="rvw"><div class="rvl">'
            f'<div class="ph"><div class="t"><div class="t-h1">Reviews</div><p>23 waiting for you · median wait 4 h</p></div><div class="search" style="width:260px">{ic("search", 18)}Search reviews<span class="kbd">⌘K</span></div></div>'
            f'<div class="tabs"><span class="on">{ics("clock", 16, "var(--hd-tone-marigold)")}To check <span class="cnt-b">23</span></span><span>{ics("success", 16, "var(--hd-tone-mint)")}Approved</span><span>{ics("danger", 16, "var(--hd-tone-vermilion)")}Rejected</span></div>'
            f'<div class="toolbar"><span class="chip"><img src="{PH["serum"]}" style="width:18px;height:18px">Glow serum{ic("x", 14)}</span><span class="chip">{ic("star", 16)}All ratings{ic("down", 14)}</span><span class="chip">{soc("Instagram", 14)}Instagram{ic("down", 14)}</span><span class="sp" style="flex:1"></span><button class="btn s sm">Reject</button><button class="btn p sm">{ic("check", 16)}Approve 2</button></div>'
            f'<div class="rvlist">{cards}</div></div>'
            f'<div class="drawer"><div class="flexw" style="justify-content:space-between"><b class="t-h2">Riya’s review</b>{ic("x", 20)}</div>'
            f'<div style="position:relative;border-radius:14px;overflow:hidden;height:236px;flex:none"><img src="{PH["serum"]}" style="width:100%;height:100%;border-radius:0;object-fit:cover"><span class="badge neutral" style="position:absolute;left:12px;bottom:12px;background:rgba(16,20,38,.7);color:#fff;box-shadow:none">{ic("play", 14)}Reel · 0:24</span></div>'
            f'<div class="rvtxt"><div class="flexw" style="justify-content:space-between"><span class="stars">{"".join(ics("star", 16, "var(--hd-star)") for _ in range(5))}</span><span class="t-small muted">@riya.glows · 18.4k followers</span></div>'
            f'<p>Used it every night for two weeks. Light, no smell, and my skin feels calmer.</p><div class="th"><img src="{PH["serum"]}" alt=""><img src="{PH["bottles"]}" alt=""></div></div>'
            f'<div class="dl"><div class="flexw t-small"><span class="muted" style="width:96px">Platform</span>{soc("Instagram", 16)}Instagram</div><div class="flexw t-small"><span class="muted" style="width:96px">Link</span><span style="color:var(--hd-link)">instagram.com/p/C9x…</span></div>'
            f'<div class="flexw t-small"><span class="muted" style="width:96px">Brand tag</span><span class="badge success">Found</span></div><div class="flexw t-small"><span class="muted" style="width:96px">Payout</span><b class="num">₹1,240</b></div></div>'
            f'<div class="notice success">{icf("success")}<span>Link is public and the brand tag is present.</span></div><div style="flex:1"></div>'
            f'<div class="flexw"><button class="btn s" style="flex:1">Reject</button><button class="btn p" style="flex:2">Approve and pay</button></div><span class="t-cap muted" style="text-align:center">Press {kbd("A")} to approve, {kbd("R")} to reject</span></div></div>')
    return shell("Reviews", ["Lumen Labs", "Reviews"], page)

DESKTOP2 = [("Overview", d_overview), ("Campaigns", d_campaigns), ("Review queue", d_review), ("Overview · dark", lambda: d_overview("dark"))]

def interaction(theme="light"):
    lab = lambda t: f'<div class="lbl">{t}</div>'
    return (f'<section class="sec"><h2>Interaction</h2><p>Every pressable thing answers: a 0.97 press, hover only where there is a mouse, a 2px focus ring for keyboards. Motion uses one curve and stays under 300 ms; reduced motion turns it off.</p>'
            f'<div class="grid g4" style="gap:22px">'
            f'<div class="box stack">{lab("Press · try it")}<button class="btn p">Send review</button><button class="btn s">{ic("copy", 18)}Copy link</button><span class="t-cap muted">scale(0.97) · 160 ms · ease-out</span></div>'
            f'<div class="box stack">{lab("Toggle · click it")}<label class="flexw"><input type="checkbox" class="switch" checked><span class="t-small">Payout alerts</span></label><label class="flexw"><input type="checkbox" class="switch"><span class="t-small">Weekly digest</span></label><span class="t-cap muted">knob slides 200 ms with the same curve</span></div>'
            f'<div class="box stack">{lab("Tape pull · progress")}<div class="tape tapeanim"><i></i></div><div class="flexw t-small muted">{ic("upload", 16)}Uploading reel…</div><span class="t-cap muted">the brand’s tape motif, 1.6 s linear loop</span></div>'
            f'<div class="box stack" style="gap:14px">{lab("Arrive · toast")}<div class="toast arrive"><span class="ok">{ic("check", 14, "#fff", 3)}</span>Review submitted<b>Undo</b></div><div class="panel" style="padding:12px;display:flex;gap:10px;align-items:center"><span class="skel shimmer" style="width:36px;height:36px;border-radius:10px"></span><div style="flex:1"><div class="skel shimmer" style="height:10px;width:80%"></div><div class="skel shimmer" style="height:10px;width:50%;margin-top:8px"></div></div></div><span class="t-cap muted">8 px drop + fade · skeleton shimmer</span></div>'
            f'</div></section>')

def kit_more(theme="light"):
    sec = lambda t, d, b: f'<section class="sec"><h2>{t}</h2><p>{d}</p>{b}</section>'
    lab = lambda t: f'<div class="lbl">{t}</div>'
    charts = sec("Charts", "Flat Cobalt series: past periods tinted, the current one solid. Hairline grid, labels in Geist, comparisons dashed and neutral.",
        f'<div class="grid" style="grid-template-columns:1.4fr 1fr;gap:22px"><div class="panel" style="padding:16px">{lab("Line · with comparison and tooltip")}{line_chart(REV, WEEKS, 640, 230, None, PREV, 5, "k" + theme)}</div>'
        f'<div class="panel" style="padding:16px">{lab("Bars · current period")}{bar_chart(REV, ["W1", "W2", "W3", "W4", "W5", "W6", "W7"], 460, 230, 6)}</div></div>'
        f'<div class="grid g4" style="gap:22px;margin-top:22px"><div class="panel" style="padding:16px;display:flex;gap:18px;align-items:center">{donut([("a", 58, "var(--hd-chart)"), ("b", 27, "var(--hd-data-hl)"), ("c", 15, "var(--hd-brand-marigold)")], 130, 12, ("91", "reviews"))}'
        f'<div class="legend" style="flex-direction:column;align-items:flex-start;gap:8px"><span><i style="background:var(--hd-chart)"></i>Instagram 58%</span><span><i style="background:var(--hd-data-hl)"></i>YouTube 27%</span><span><i style="background:var(--hd-brand-marigold)"></i>Threads 15%</span></div></div>'
        + stat("Reviews this week", "91", "+42%", True, spark=REV, kind="bars") + goal("Slots filled", 84, 120) +
        goal("Campaign goal", 84, 120, variant="ring") + '</div>')
    shell_s = sec("Shell & sidebar", "Grouped navigation, ⌘K search, counts that only turn Cobalt when they need you, and the account at the bottom.",
        f'<div class="grid" style="grid-template-columns:252px 72px 1fr;gap:22px;align-items:start"><div class="panel" style="overflow:hidden;height:620px;display:flex">{sidebar2("Reviews", theme)}</div>'
        f'<div class="panel" style="height:620px;padding:14px 0;display:flex;flex-direction:column;align-items:center;gap:6px"><img src="{MARK[theme]}" style="width:26px;margin-bottom:10px">'
        + "".join(f'<span class="nav {"on" if n == "star" else ""}" style="width:40px;justify-content:center;padding:0">{ics(n, 18) if n == "star" else ic(n, 18)}</span>' for n in ("overview", "campaign", "star", "users", "wallet", "payouts", "reports")) +
        f'<span style="flex:1"></span>{av("AM", 2, 30)}</div>'
        f'<div class="stack" style="gap:22px"><div class="panel" style="overflow:hidden">{header(["Lumen Labs", "Reviews"])}</div>'
        f'<div class="panel" style="padding:18px"><div class="ph"><div class="t"><div class="t-h1">Reviews</div><p>Page header: title, one line of context, actions on the right.</p></div><button class="btn s sm">Export</button><button class="btn p sm">{ic("plus", 16)}New</button></div>'
        f'<div class="tabs" style="margin-top:14px"><span class="on">{ics("clock", 16, "var(--hd-tone-marigold)")}To check <span class="cnt-b">23</span></span><span>{ics("success", 16, "var(--hd-tone-mint)")}Approved <span class="cnt-b">418</span></span><span>{ics("danger", 16, "var(--hd-tone-vermilion)")}Rejected</span></div></div>'
        f'<div class="cmdk"><div class="cin">{ic("search", 18)}<span>glow</span><span class="kbd" style="margin-left:auto">esc</span></div><div class="cgp"><div class="cgh">Campaigns</div>'
        f'<div class="ci hl"><img src="{PH["serum"]}">Glow serum, 30 ml<span class="kbd">↵</span></div><div class="ci">{ic("star", 18)}Glow serum reviews · 23 to check</div>'
        f'<div class="cgh">Actions</div><div class="ci">{ic("plus", 18)}New campaign<span class="kbd">C</span></div><div class="ci">{ic("wallet", 18)}Add funds<span class="kbd">F</span></div></div>'
        f'<div class="cft"><span>{kbd("↑")}{kbd("↓")} to move</span><span>{kbd("↵")} to open</span></div></div></div></div>')
    more = sec("More components", "Built from the same tokens. Brand motifs appear where they mean something: tape for progress, the hexagon for verified, the shipping label for payouts.",
        f'<div class="grid g3" style="gap:22px"><div class="stack" style="gap:16px"><div>{lab("Badges")}<div class="flexw"><span class="badge success"><span class="bdot"></span>Live</span><span class="badge warning"><span class="bdot"></span>In review</span><span class="badge danger"><span class="bdot"></span>Rejected</span><span class="badge info">New</span><span class="badge neutral">Paid</span><span class="badge solid">3</span></div></div>'
        f'<div>{lab("Tabs · with counts")}<div class="tabs"><span class="on">{ics("clock", 16, "var(--hd-tone-marigold)")}To check <span class="cnt-b">23</span></span><span>{ics("success", 16, "var(--hd-tone-mint)")}Approved <span class="cnt-b">418</span></span><span>{ics("danger", 16, "var(--hd-tone-vermilion)")}Rejected</span></div></div>'
        f'<div>{lab("Verified · avatars")}<div class="flexw">{av("RS", 0, 40)}<span class="avst">{av("AK", 1, 40)}<i></i></span><b>Riya Sharma {vhex(16)}</b><div class="avs">{av("RS",0)}{av("AK",1)}{av("MJ",2)}{av("+81",4)}</div></div></div>'
        f'<div>{lab("Keyboard · links")}<div class="flexw t-small">{kbd("⌘")}{kbd("K")}<span class="muted">to search</span><span style="color:var(--hd-link);font-weight:550">Learn more</span></div></div>'
        f'<div>{lab("Progress")}<div class="stack" style="gap:14px"><div><div class="barlab"><b>Slots filled</b><span>84 / 120</span></div><div class="bar"><i style="width:70%"></i></div></div>'
        f'<div><div class="barlab"><b>Review status</b><span>91 reviews</span></div><div class="bar multi"><i style="width:62%;background:var(--hd-success-solid)"></i><i style="width:26%;background:{M['300']}"></i><i style="width:12%;background:var(--hd-danger-solid)"></i></div>'
        f'<div class="legend" style="margin-top:8px"><span><i style="background:var(--hd-success-solid)"></i>Approved 56</span><span><i style="background:{M['300']}"></i>In review 24</span><span><i style="background:var(--hd-danger-solid)"></i>Rejected 11</span></div></div>'
        f'<div><div class="barlab"><b>Segmented · slots</b><span>7 of 10</span></div>{segs(.7, 10)}</div><div><div class="barlab"><b>Thin · upload</b><span>64%</span></div><div class="bar thin"><i style="width:64%"></i></div></div>'
        f'<div><div class="barlab"><b>Upload complete</b><span class="ok">100%</span></div><div class="bar ok"><i style="width:100%"></i></div></div>'
        f'<div><div class="barlab"><b>Paused · no connection</b><span>38%</span></div><div class="bar paused"><i style="width:38%"></i></div></div>'
        f'<div><div class="barlab"><b>Failed · file too large</b><span class="err">72%</span></div><div class="bar err"><i style="width:72%"></i></div></div></div></div>'
        f'<div>{lab("Quantity · pagination")}<div class="flexw"><span class="qty"><span>{ic("plus", 16).replace("M12", "M5 12h14M12") if False else "−"}</span><b class="num">2</b><span>{ic("plus", 16)}</span></span><div class="pager"><span>{ic("back", 16)}</span><span class="on">1</span><span>2</span><span>3</span><span>…</span><span>9</span><span>{ic("chev", 16)}</span></div></div></div>'
        f'<div>{lab("Tag input")}<div class="tagin"><span class="tag">Skincare{ic("x", 12)}</span><span class="tag">Under 25{ic("x", 12)}</span><span class="t-small subtle" style="padding-left:4px">Add tag…</span></div></div></div>'
        f'<div class="stack" style="gap:16px"><div>{lab("Payout ticket · the shipping-label motif")}<div class="ticket"><div class="tl"><span class="t-small muted">Payout · Glow serum</span><div class="hero-num num" style="font-size:28px;font-weight:650;letter-spacing:-.03em;margin:2px 0">₹1,240</div><span class="t-small muted">Lands by Tue, Nov 24 · HDFC ••6093</span></div><div class="tr">{ring(100, 40, 4, "✓")}<span class="t-cap muted">Approved</span></div></div></div>'
        f'<div>{lab("Uploads")}<div class="stack" style="gap:8px"><div class="panel upl"><img src="{PH["serum"]}" style="width:40px;height:40px"><div class="tx"><b>unboxing-reel.mp4</b><small>18.4 MB · 64%</small><div class="tape"><i style="width:64%"></i></div></div>{ic("x", 16)}</div>'
        f'<div class="panel upl"><img src="{PH["bottles"]}" style="width:40px;height:40px"><div class="tx"><b>product-shot.jpg</b><small>2.1 MB · uploaded</small></div><span style="color:var(--hd-success)">{ic("check", 18)}</span></div></div></div>'
        f'<div>{lab("Banner · with actions")}<div class="banner"><span class="bi" style="background:var(--hd-accent);color:#fff">{ics("box", 18)}</span><div class="tx"><b>3 new drops match you</b><small>Skincare · under ₹2,000</small></div><button class="btn p sm">View</button></div></div>'
        f'<div>{lab("Toast stack")}<div class="toasts"><div class="toast"><span class="ok">{ic("check", 14, "#fff", 3)}</span>Draft saved</div><div class="toast"><span class="ok">{ic("check", 14, "#fff", 3)}</span>Link copied</div><div class="toast"><span class="ok">{ic("check", 14, "#fff", 3)}</span>Review submitted<b>Undo</b></div></div></div></div>'
        f'<div class="stack" style="gap:16px"><div>{lab("Date range")}<div class="panel cal"><div class="flexw" style="justify-content:space-between;margin-bottom:8px">{ic("back", 16)}<b class="t-small">November 2026</b>{ic("chev", 16)}</div><div class="cg">'
        + "".join(f'<span class="dw">{d}</span>' for d in "MTWTFSS") + "".join('<span class="mute">' + str(d) + '</span>' for d in (27, 28, 29, 30, 31)) +
        "".join(f'<span class="{"sel" if d in (12, 18) else "rng" if 12 < d < 18 else "today" if d == 20 else ""}">{d}</span>' for d in range(1, 31)) + '</div></div></div>'
        f'<div>{lab("Accordion")}<div class="panel acc"><div class="ai">How do payouts work?<span style="margin-left:auto">{ic("down", 16)}</span></div><div class="ab">You’re paid within 48 h of the brand approving your review, straight to your bank.</div>'
        f'<div class="ai">Can I keep the product?<span style="margin-left:auto">{ic("chev", 16)}</span></div><div class="ai">What if my post is private?<span style="margin-left:auto">{ic("chev", 16)}</span></div></div></div>'
        f'<div>{lab("Popover")}<div class="panel pop"><b class="t-small">Payout held</b><p class="t-small muted" style="margin:4px 0 0">We hold ₹640 until the brand approves your review. It usually takes a day.</p></div></div></div></div>'
        f'<div class="grid g2" style="gap:22px;margin-top:22px"><div>{lab("Review card")}<div class="panel rcard"><div class="rh">{av("RS", 0, 36)}<div style="flex:1"><b>Riya Sharma {vhex(14)}</b><small>@riya.glows · 2m</small></div><div class="stars">{"".join(ic("star", 15, fill="x") for _ in range(5))}</div></div>'
        f'<p>Used it every night for two weeks. Light, no smell, and my skin feels calmer.</p><div class="media"><img src="{PH["serum"]}"><img src="{PH["bottles"]}"><img src="{PH["flatlay"]}"></div></div></div>'
        f'<div>{lab("Campaign card")}<div class="panel x-camp" style="display:grid"><img src="{PH["serum"]}" alt=""><div class="stack" style="gap:6px"><div class="flexw"><span class="badge success"><span class="bdot"></span>Live</span><span class="t-cap muted">Ends Thu</span></div>'
        f'<b class="t-h3">Glow serum, 30 ml</b><span class="flexw t-small muted">Lumen Labs · {soc("Instagram", 14)}{soc("Youtube", 14)}</span><div class="flexw" style="justify-content:space-between;margin-top:auto"><b class="num" style="color:var(--hd-success)">+₹1,240</b><span class="t-small muted num">36 of 120 left</span></div><div class="tape"><i style="width:70%"></i></div></div></div></div></div>')
    return charts + shell_s + more + interaction(theme)
