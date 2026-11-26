"""Concept: brand dashboard, designed at discretion (owner 2026-11-26). Content-first. In the kit since 2026-11-26."""
from kit2 import shell
from uikit2 import *
PPL = lambda k: f"{STOCK}/people/{k}.jpg"

def page():
    """Evolved dashboard: the original overview's analytics (KPIs, a period-over-period chart, the platform split)
    with the real business logic, then what needs the brand today as content, money, inbox and live campaigns."""
    from kit2 import WEEKS
    from uikit2 import line_chart, donut, stat
    APPR = [4, 6, 7, 6, 9, 13, 16]; PREV = [3, 4, 5, 5, 6, 7, 9]
    k = (stat("Creators approved", "61", "+18%", True, spark=[3, 4, 6, 7, 9, 13, 16], uid="cv0")
         + stat("Posts live this week", "18", "+42%", True, spark=[6, 9, 11, 10, 13, 15, 18], kind="bars")
         + stat("Spent this month", "₹96,380", "+31%", True, spark=[10, 14, 13, 18, 22, 26, 31], uid="cv2")
         + stat("Cost per approval", "₹1,580", "−4%", True, kind="compare", extra=(1580, 1645)))
    plats = [("Instagram reels", 58, "var(--hd-chart)"), ("Nykaa reviews", 30, "var(--hd-data-hl)"), ("Amazon reviews", 12, "var(--hd-brand-marigold)")]
    leg = "".join(f'<div><i style="background:{c}"></i><span>{n}</span><b>{v}%</b></div>' for n, v, c in plats)
    sub = lambda ph, plat_, who, name, meta, handle="": (f'<div class="bd2-sub"><div class="bd2-th"><img src="{PH[ph]}" alt=""><span class="k">{soc("Instagram", 14) if plat_=="Instagram" else plat(plat_.lower(), 14)}{"Reel" if plat_=="Instagram" else "Review"}</span></div>'
                                             f'<div class="who"><img src="{PPL(who)}" alt=""><div><b>{name}</b><small>{meta}</small></div></div></div>')
    camp = lambda ph, store, name, n, tot, foot, warn="", money="": (f'<div class="bd2-camp"><img src="{PH[ph]}" alt=""><div class="b"><span class="s">{plat(store, 14)}{store.title()}</span><b>{name}</b>'
                                                         f'<div class="bar"><i style="width:{round(n*100/tot)}%"></i></div><small><span>{n} of {tot} creators</span><span class="{"warn" if warn else ""}">{foot}</span></small><small class="m">{money}</small></div></div>')
    body = ('<div class="b1-wrap tall"><div class="bd2">'
        f'<div class="ph"><div class="t"><div class="t-h1">Good morning, Neha</div><p>Glow serum drove <b class="num">31</b> of <b class="num">52</b> posts and is 93% full · <b class="num">9</b> submissions are waiting for you</p></div><span class="chip">{ic("calendar", 16)}Last 7 weeks{ic("down", 14)}</span>'
        f'<button class="btn s sm">{ic("download", 16)}Export</button><button class="btn p sm">{ic("plus", 16)}Create campaign</button></div>'
        f'<div class="grid g4" style="gap:14px">{k}</div>'
        f'<div class="grid" style="grid-template-columns:1.7fr 1fr;gap:14px"><div class="panel"><div class="phd"><b>Approvals over time</b><span class="t-small muted num">+78% vs the 7 weeks before</span></div>'
        f'<div style="padding:10px 14px 2px">{line_chart(APPR, WEEKS, 660, 214, None, PREV, 5, "cvl")}</div><div class="legend" style="padding:0 18px 14px"><span><i style="background:var(--hd-chart)"></i>This period</span><span><i class="dash"></i>Previous period</span></div></div>'
        f'<div class="panel dcard"><div class="phd"><b>Where posts go live</b></div><div class="db">{donut(plats, 136, 16, ("52", "posts"))}<div class="lgd">{leg}</div></div></div></div>'
        '<div class="bd2-row"><div class="bd2-card bd2-need"><div class="bd2-nh"><div><h2>9 submissions to review</h2><small>Oldest waited 2 days · 4 applications and 3 to ship too</small></div><button class="btn p">Review 9</button></div><div class="bd2-subs">'
        + sub("cream", "Amazon", "women-68", "Riya Sharma", "Amazon review · 2 days", "@riya.glows · 18.4k")
        + sub("bottles", "Instagram", "men-12", "Arjun Kapoor", "Reel + review · 1 day", "@arjun.k · 9.2k")
        + sub("serum", "Instagram", "women-44", "Meera Joshi", "Reel + review · 1 day", "@meera.skin · 41k")
        + sub("flatlay", "Instagram", "women-21", "Tanvi Nair", "Reel + review · 6 h", "@tanvi.n · 6.0k")
        + '</div></div>'
        f'<div class="bd2-side"><div class="v3-money"><span class="l">Available</span><b class="n num">₹1,84,500</b><p><span class="num">₹96,320</span> on hold for creators who joined</p>'
        f'<div class="a"><button class="btn p sm">{ic("plus", 16)}Add money</button><em>Open wallet</em></div></div>'
        '<div class="bd2-card bd2-inb"><div class="bd2-sh"><h2>Inbox</h2><em>See all</em></div>'
        '<div class="bd2-ir"><b>Hair oil was sent back</b><small>Hypedrive asked for 2 changes · 18 Nov</small></div>'
        '<div class="bd2-ir"><b>Reply to a dispute</b><small class="warn">Due by 24 Nov · Daily cleanser trio</small></div>'
        '<div class="bd2-ir"><b>Glow serum is 93% full</b><small>8 creators left · ends in 6 days</small></div></div></div></div>'
        f'<div><div class="bd2-sh"><h2>Live campaigns</h2><em>All campaigns</em></div><div class="bd2-camps">'
        + camp("serum", "nykaa", "Glow serum, 30 ml", 112, 120, "Ends in 6 days", True, "₹1,16,920 spent · 31 posts")
        + camp("cream", "amazon", "Night cream, 50 g", 42, 80, "Ends 12 Dec", "", "₹46,020 spent · 9 posts")
        + camp("bottles", "nykaa", "Daily cleanser trio", 18, 90, "Ends 5 Dec", "", "₹9,540 spent · 4 posts")
        + camp("set", "nykaa", "Clear skin set", 60, 60, "Full", "", "₹24,190 spent · 8 posts")
        + '</div></div>'
        + '</div></div>')
    return shell("Home", ["Lumen Labs", "Home"], body)

