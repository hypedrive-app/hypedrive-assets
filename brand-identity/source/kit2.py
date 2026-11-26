"""New kit sections (charts, shell & navigation, more components) and the redesigned desktop screens."""
from uikit2 import *

WEEKS = ["Oct 6", "Oct 13", "Oct 20", "Oct 27", "Nov 3", "Nov 10", "Nov 17"]
REV = [42, 58, 64, 61, 77, 84, 91]


from uikit2 import _smooth
PREV2 = [30, 41, 48, 52, 55, 60, 64]
def _chhead(title, value, delta, legend=True):
    lg = '<div class="chl"><span><i class="sw"></i>This period</span><span><i class="sw dash"></i>Last period</span></div>' if legend else ""
    return f'<div class="chh"><div><div class="cht">{title}</div><div class="chv"><b class="num">{value}</b><span class="chd">{delta}</span></div></div>{lg}</div>'

def chart_line2(series, compare, labels, tip_i, w=796, h=236):
    pl, pr, pt, pb = 36, 24, 10, 24; ph = h - pt - pb; ymax = 100
    X = lambda i: pl + i * (w - pl - pr) / (len(series) - 1); Y = lambda v: pt + ph * (1 - v / ymax)
    grid = "".join(f'<line x1="0" x2="{w}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" class="g2l"/><text x="24" y="{Y(v)+4:.1f}" text-anchor="end" class="g2t">{v}</text>' for v in (25, 50, 75))
    xl = "".join(f'<text x="{X(i):.1f}" y="{h-5}" text-anchor="middle" class="g2t">{t}</text>' for i, t in enumerate(labels))
    pts = [(X(i), Y(v)) for i, v in enumerate(series)]; cp = [(X(i), Y(v)) for i, v in enumerate(compare)]
    line = _smooth(pts); area = line + f"L{pts[-1][0]:.1f} {Y(0):.1f}L{pts[0][0]:.1f} {Y(0):.1f}Z"
    tx, ty = pts[tip_i]; cx, cy = cp[tip_i]
    svg = (f'<svg viewBox="0 0 {w} {h}" width="100%" class="chart2" aria-hidden="true"><defs><linearGradient id="l2g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--hd-chart)" stop-opacity=".08"/><stop offset="1" stop-color="var(--hd-chart)" stop-opacity="0"/></linearGradient></defs>'
           f'{grid}<path d="{area}" fill="url(#l2g)"/><path d="{_smooth(cp)}" class="g2c"/><line x1="{tx:.1f}" x2="{tx:.1f}" y1="{pt}" y2="{Y(0):.1f}" class="g2v"/>'
           f'<path d="{line}" class="g2s"/><circle cx="{cx:.1f}" cy="{cy:.1f}" r="3" class="g2cd"/><circle cx="{tx:.1f}" cy="{ty:.1f}" r="4" class="g2d"/>{xl}</svg>')
    tip = (f'<div class="g2tip" style="right:{(w-tx+14)/w*100:.2f}%;top:{ty+62:.0f}px"><div class="tt-d">Tue, Nov 10</div>'
           f'<div class="tt-r"><i class="sw"></i><span>This period</span><b class="num">{series[tip_i]}</b></div><div class="tt-r"><i class="sw dash"></i><span>Last period</span><b class="num">{compare[tip_i]}</b></div></div>')
    return f'<div class="cw2">{svg}{tip}</div>'

def chart_bars2(values, labels, w=558, h=236):
    pb, pt = 24, 26; ph = h - pb - pt; n = len(values); slot = (w - 16) / n; bw = slot * .55; ymax = 100; r = 6
    out = f'<line x1="0" x2="{w}" y1="{h-pb}" y2="{h-pb}" class="g2l"/>'
    for i, v in enumerate(values):
        cx = 8 + (i + .5) * slot; y = pt + ph * (1 - v / ymax); x0, x1 = cx - bw / 2, cx + bw / 2; cur = i == n - 1
        out += (f'<path d="M{x0:.1f} {h-pb}V{y+r:.1f}Q{x0:.1f} {y:.1f} {x0+r:.1f} {y:.1f}H{x1-r:.1f}Q{x1:.1f} {y:.1f} {x1:.1f} {y+r:.1f}V{h-pb}Z" class="g2b{" cur" if cur else ""}"/>'
                f'<text x="{cx:.1f}" y="{h-5}" text-anchor="middle" class="g2t">{labels[i]}</text>')
        if cur: out += f'<text x="{cx:.1f}" y="{y-7:.1f}" text-anchor="middle" class="g2v2">{v}</text>'
    return f'<div class="cw2"><svg viewBox="0 0 {w} {h}" width="100%" class="chart2" aria-hidden="true">{out}</svg></div>'

# Brand app nav (apps/brand/src/lib/nav.ts). `active` must be one of these labels:
NAV_LABELS = ("Home", "Inbox", "Campaigns", "Enrollments", "Products", "Disputes", "Wallet", "Invoices", "Team", "Settings")
_NAV = [(None, [("home", "Home", ""), ("mail", "Inbox", "")]),
        ("Work", [("campaign", "Campaigns", ""), ("enrolled", "Enrollments", ""), ("box", "Products", ""), ("alert", "Disputes", "0")]),
        ("Finance", [("wallet", "Wallet", "₹1,84,500"), ("receipt", "Invoices", "")]),
        ("Workspace", [("users", "Team", ""), ("settings", "Settings", "")])]

def sidebar2(active, theme="light"):
    nav = ""
    for h, items in _NAV:
        if h: nav += f'<div class="sbh">{h}</div>'
        for i, n, c in items:
            cnt = f'<span class="cnt">{c}</span>' if c else ""
            nav += f'<div class="nav {"on" if n == active else ""}">{ics(i, 18) if n == active else ic(i, 18)}{n}{cnt}</div>'
    UD = f'<svg class="ic" width="16" height="16" viewBox="0 0 18 18" stroke-width="1.5" aria-hidden="true">{NO["ChevronExpandYOutline18"]}</svg>'
    return (f'<aside class="sb"><img class="sb-lg sb-lg-l" src="{LOGO["light"]}" alt="Hypedrive" style="height:22px;align-self:flex-start;margin:6px 8px 16px"><img class="sb-lg sb-lg-d" src="{LOGO["dark"]}" alt="" style="height:22px;align-self:flex-start;margin:6px 8px 16px">'
            f'<div class="ws">{av("LL", 2, 28)}<div style="flex:1;min-width:0"><b>Lumen Labs</b></div>{UD}</div>{nav}'
            f'<div class="sbfoot"><div class="me">{av("NK", 2, 32)}<div style="flex:1;min-width:0"><b>Neha Kapoor</b><small>Owner</small></div>{ic("more", 18)}</div></div></aside>')

def header(crumbs, action=False):
    """Top bar: breadcrumb left; Search and Help right (brand nav spec). The one primary CTA lives in the page header."""
    c = f'<span class="crumb" style="white-space:nowrap">' + f'{ic("chev", 14)}'.join(f"<b>{x}</b>" if i == len(crumbs)-1 else x for i, x in enumerate(crumbs)) + '</span>'
    return (f'<div class="hdr">{c}<span class="sp"></span><span class="b1-search">{ic("search", 16)}<span>Search</span><em>Ctrl K</em></span>'
            f'<span class="iconbtn" aria-label="Help">{ic("help", 20)}</span></div>')

def shell(active, crumbs, page, theme="light", action=False):
    return f'<div class="shell" data-theme="{theme}">{sidebar2(active, theme)}<div class="mn">{header(crumbs, action)}<div class="pg">{page}</div></div></div>'


def interaction(theme="light"):
    lab = lambda t: f'<div class="lbl">{t}</div>'
    return (f'<section class="sec"><h2>Interaction</h2><p>Every pressable thing answers: a 0.97 press, hover only where there is a mouse, a 2px focus ring for keyboards. Motion uses one curve and stays under 300 ms; reduced motion turns it off.</p>'
            f'<div class="grid g4" style="gap:22px">'
            f'<div class="panel stack ix">{lab("Press · try it")}<button class="btn p">Submit 2 tasks</button><button class="btn s">{ic("copy", 18)}Copy link</button><span class="t-cap muted">scale(0.97) · 160 ms · ease-out</span></div>'
            f'<div class="panel stack ix">{lab("Toggle · click it")}<label class="flexw"><input type="checkbox" class="switch" checked><span class="t-small">Campaign updates</span></label><label class="flexw"><input type="checkbox" class="switch"><span class="t-small">Wallet and payouts</span></label><span class="t-cap muted">knob slides 200 ms with the same curve</span></div>'
            f'<div class="panel stack ix">{lab("Tape pull · progress")}<div class="tape tapeanim"><i></i></div><div class="flexw t-small muted">{ic("receipt", 16)}Checking your receipt…</div><span class="t-cap muted">This takes about 20 seconds · 1.6 s linear loop</span></div>'
            f'<div class="panel stack ix">{lab("Arrive · toast")}<div class="toast arrive"><span class="ok">{ics("success", 18)}</span>Spot held for you<b>Add 10 min</b></div><div class="skrow"><span class="skel shimmer sk-th"></span><div class="sk-ln"><span class="skel shimmer" style="width:60%;height:12px"></span><span class="skel shimmer" style="width:36%;height:10px"></span></div></div><span class="t-cap muted">8 px drop + fade · skeleton shimmer</span></div>'
            f'</div></section>')

def kit_more(theme="light"):
    sec = lambda t, d, b: f'<section class="sec"><h2>{t}</h2><p>{d}</p>{b}</section>'
    lab = lambda t: f'<div class="lbl">{t}</div>'
    charts = sec("Charts", "Flat Cobalt series: past periods tinted, the current one solid. Hairline grid, labels in Allo, comparisons dashed and neutral.",
        f'<div class="grid chrow" style="grid-template-columns:1.4fr 1fr;gap:22px"><div class="panel cc">{_chhead("Tasks submitted", "91", "+42% vs last period")}{chart_line2(REV, PREV2, WEEKS, 5)}</div>'
        f'<div class="panel cc">{_chhead("Tasks per week", "91", "+8% vs last week", False)}{chart_bars2(REV, WEEKS)}</div></div>'
        f'<div class="grid g4 sxrow" style="gap:22px;margin-top:22px">'
        f'<div class="panel sx"><div class="sxh"><span class="sxl">Tasks this week</span><span class="sxd">+42%</span></div><div class="sxv"><b class="num">91</b></div><div class="sxb">{mini_bars(REV)}</div></div>'
        f'<div class="panel sx"><div class="sxh"><span class="sxl">By platform</span></div><div class="sxv"><b>Instagram</b><span class="num">58%</span></div>'
        f'<div class="sxb"><div class="sxstack"><i style="width:58%"></i><i style="width:27%"></i><i style="width:15%"></i></div><div class="sxleg num"><span>{soc("Instagram", 14)}58</span><span>{soc("Youtube", 14)}27</span><span>{soc("Threads", 14)}15</span></div></div></div>'
        f'<div class="panel sx"><div class="sxh"><span class="sxl">Spots filled</span></div><div class="sxv"><b class="num">112</b><span class="num">/ 120</span></div><div class="sxb">{segs(112/120)}<span class="sxc num">8 left</span></div></div>'
        f'<div class="panel sx"><div class="sxh"><span class="sxl">Held payouts</span></div><div class="sxv"><b class="num">₹1,04,160</b></div><div class="sxb"><div class="sxhair"><i style="width:70%"></i></div><span class="sxc">releases on approval</span></div></div>'
        '</div>')
    sbx = sidebar2("Campaigns", theme).replace("height:22px", "height:20px")
    rail = "".join(f'<span class="nav {"on" if n == "campaign" else ""}">{ics(n, 20) if n == "campaign" else ic(n, 20)}</span>' for n in ("home", "mail", "campaign", "enrolled", "box", "wallet", "users"))
    shell_s = sec("Shell & sidebar", "Grouped navigation, plain counts, and the account at the bottom. The top bar is bare: breadcrumb, title, actions, tabs.",
        f'<div class="grid k-shell" style="grid-template-columns:252px 72px 1fr;gap:22px;align-items:start"><div class="panel" style="overflow:hidden;height:660px;display:flex">{sbx}</div>'
        f'<div class="panel rail" style="height:660px;padding:14px 0;display:flex;flex-direction:column;align-items:center;gap:6px"><img src="{MARK[theme]}" style="width:26px;margin-bottom:10px">{rail}'
        f'<span style="flex:1"></span>{av("NK", 2, 32)}</div>'
        f'<div class="stack" style="gap:22px"><div class="k-top"><div class="k-crumb"><span class="crumb">Lumen Labs{ic("chev", 14)}<b>Campaigns</b></span><span class="sp"></span><span class="iconbtn">{ic("help", 20)}</span></div>'
        f'<div class="ph"><div class="t"><div class="k-h1">Campaigns</div><p>Everything you have sent to creators.</p></div><button class="btn s sm">Export</button><button class="btn p sm">{ic("plus", 16)}New</button></div>'
        f'<div class="tabs"><span class="on">{ics("clock", 16, "var(--hd-tone-marigold)")}To check <span class="tc">23</span></span><span>{ics("success", 16, "var(--hd-tone-mint)")}Approved <span class="tc">418</span></span><span>{ics("danger", 16, "var(--hd-tone-vermilion)")}Rejected <span class="tc">11</span></span></div></div>'
        f'<div class="cmdk" style="margin-inline:auto"><div class="cin">{ic("search", 18)}<span>glow</span><span class="kbd" style="margin-left:auto">esc</span></div><div class="cgp"><div class="cgh">Campaigns</div>'
        f'<div class="ci hl"><img src="{PH["serum"]}">Glow serum, 30 ml<span class="kbd">↵</span></div><div class="ci">{ic("star", 18)}Glow serum tasks · 23 to check</div>'
        f'<div class="cgh">Actions</div><div class="ci">{ic("plus", 18)}New campaign<span class="kbd">C</span></div><div class="ci">{ic("wallet", 18)}Add funds<span class="kbd">F</span></div></div>'
        f'<div class="cft"><span>{kbd("↑")}{kbd("↓")} to move</span><span>{kbd("↵")} to open</span></div></div></div></div>')
    more = sec("More components", "Built from the same tokens. Brand motifs appear where they mean something: tape for progress, the hexagon for verified, the shipping label for payouts.",
        f'<div class="grid g3 mc3" style="gap:22px"><div class="stack" style="gap:16px">'

        f'<div>{lab("Verified · avatars")}<div class="flexw"><img class="rv-av" src="{STOCK}/people/women-68.jpg" alt="" style="width:40px;height:40px;border-radius:50%;object-fit:cover"><b>Riya Sharma {vhex(16)}</b><div class="avs xt-avs"><img class="av" src="{STOCK}/people/women-68.jpg" alt=""><img class="av" src="{STOCK}/people/men-12.jpg" alt=""><img class="av" src="{STOCK}/people/women-65.jpg" alt="">{av("+81",4)}</div></div></div>'
        f'<div>{lab("Link · pagination")}<div class="flexw t-small"><span style="color:var(--hd-link);font-weight:550">Learn more</span><div class="pager"><span>{ic("back", 16)}</span><span class="on">1</span><span>2</span><span>3</span><span>…</span><span>9</span><span>{ic("chev", 16)}</span></div></div></div>'
        f'<div>{lab("Withdrawal ticket · the shipping-label motif")}<div class="ticket"><div class="tl"><span class="t-small muted">Withdraw · Fee ₹0</span><div class="hero-num num" style="font-size:28px;font-weight:650;letter-spacing:-.03em;margin:2px 0">₹6,820</div><span class="t-small muted">Payout to HDFC ••6093 · Usually within minutes</span></div><div class="tr"><span class="tk-ok">{ics("success", 24)}</span><span class="t-small tk-lb">Requested</span></div></div></div>'
        f'<div>{lab("Toast stack")}<div class="toasts"><div class="toast"><span class="ok">{ics("success", 18)}</span>Spot held for you<b>Add 10 min</b></div></div></div>'
        f'</div><div class="stack" style="gap:16px">'
        f'<div>{lab("Progress")}<div class="pg3">'
        f'<div class="pg3-i"><div class="barlab"><b>Spots</b><span><b class="num">112</b> of 120 taken</span></div><div class="pg3-bar"><i style="width:93.3%"></i></div><small>Brand view. Creators see “8 spots left” only.</small></div>'
        f'<div class="pg3-i"><div class="barlab"><b>Enrollments</b><span><b class="num">91</b> creators</span></div><div class="pg3-stack"><i class="pgpd" style="flex:56"></i><i class="pgrv" style="flex:24"></i><i class="pgfx" style="flex:11"></i></div>'
        f'<div class="pg3-leg"><span><i class="pgpd"></i>Paid <b class="num">56</b></span><span><i class="pgrv"></i>In review <b class="num">24</b></span><span><i class="pgfx"></i>Fix tasks <b class="num">11</b></span></div></div>'
        f'<div class="pg3-i"><div class="barlab"><b>Tasks sent</b><span><b class="num">1</b> of 2</span></div><div class="pg3-seg"><i class="on"></i><i></i></div></div></div></div>'
        f'<div>{lab("Uploads · task screenshots")}<div class="u-list"><div class="u-row go"><img class="u-th" src="{PH["serum"]}" alt=""><div class="u-tx"><b>reel-screenshot.png</b><span class="num">1.1 of 1.8 MB · 64%</span></div><button class="btn g icon sm" aria-label="Cancel">{ic("x", 16)}</button><i class="u-bar" style="width:64%"></i></div>'
        f'<div class="u-row"><img class="u-th" src="{PH["cream"]}" alt=""><div class="u-tx"><b>nykaa-review.png</b><span>0.9 MB</span></div><span class="u-ok">{ics("success", 18)}</span><button class="btn g icon sm" aria-label="Remove">{ic("x", 16)}</button></div></div></div>'
        f'<div>{lab("Banner · with action")}<div class="banner"><span class="bi" style="background:var(--hd-accent);color:#fff">{ics("privacy", 18)}</span><div class="tx"><b>Verify your PAN to join</b><small>Needed before you can join or withdraw</small></div><button class="btn p sm">Verify PAN</button></div></div>'
        f'</div><div class="stack" style="gap:16px">'
        f'<div>{lab("Date range · statements")}<div class="panel cal2"><div class="c2h"><b>November 2026</b><span class="c2n"><button class="btn g icon" aria-label="Previous month">{ic("back", 16)}</button><button class="btn g icon" aria-label="Next month">{ic("chev", 16)}</button></span></div><div class="c2g">'
        + "".join(f'<span class="dw">{d}</span>' for d in ("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")) + "<span></span>" * 6 +
        "".join(f'<span class="c{" rs" if d == 12 else " re" if d == 18 else " in" if 12 < d < 18 else ""}{" l" if (d + 5) % 7 == 0 else ""}{" r" if (d + 5) % 7 == 6 else ""}{" past" if d < 12 else ""}"><i class="{"sel" if d in (12, 18) else "td" if d == 20 else ""}">{d}</i></span>' for d in range(1, 31)) + '</div><div class="c2f"><span>12 Nov 2026 – 18 Nov 2026 · 7 days</span></div></div></div>'
        f'<div>{lab("Accordion · How it works")}<div class="acc2"><div class="ac open"><div class="ai">Can I withdraw my enrollment?<span class="ac-c">{ic("down", 16)}</span></div><div class="ab">Yes, right up until the brand decides. Once it’s approved, rejected or expired, it’s final.</div></div><div class="ac"><div class="ai">How long does it take to receive cashback?<span class="ac-c">{ic("down", 16)}</span></div></div><div class="ac"><div class="ai">Can I participate multiple times?<span class="ac-c">{ic("down", 16)}</span></div></div></div></div>'
        f'<div>{lab("Popover")}<div class="panel pop"><b class="t-small">₹1,339 on hold</b><p class="t-small muted" style="margin:4px 0 0">Cashback is credited the moment the brand approves your tasks.</p></div></div></div></div>'
        f'<div class="grid g2 rcrow" style="gap:22px;margin-top:22px"><div>{lab("Task card")}<div class="panel rcard2"><div class="rh"><span class="x-tile">{soc("Instagram", 20)}</span><div class="rn"><b>Instagram reel</b>'
        f'<span class="rm"><span>Link and screenshots</span>·<span>#ad and Paid partnership label</span></span></div></div>'
        f'<p>Post the reel, then add the link and 1 to 6 screenshots.</p>'
        f'<div class="rprod xt-rf"><span>Due in 41 days</span></div></div></div>'
        f'<div>{lab("Campaign card")}<div class="panel x-camp x-camp2" style="display:grid"><img src="{PH["serum"]}" alt=""><div class="cbody"><div class="ctop"><span class="badge warning"><span class="bdot"></span>Closing soon</span><span>Closes 26 Nov 2026</span></div>'
        f'<b class="ctitle">Glow serum, 30 ml</b><div class="cmeta"><span><b class="num">60% back</b></span>·<span>+₹200 bonus</span>·<span>Nykaa</span></div>'
        f'<div class="cprog"><div class="tape"><i style="width:93%"></i></div><div class="cnum num"><span>8 spots left</span><span>Lumen Labs</span></div></div></div></div></div></div>')
    return charts + shell_s + more + interaction(theme)
