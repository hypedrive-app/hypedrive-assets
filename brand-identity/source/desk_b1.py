"""Brand desktop, part 1 (agent b1): Home, Campaigns list, Campaign detail, New campaign composer. Spec: BRAND-SPEC.md.

NAV LABELS for shell(active, crumbs, page) — `active` must be exactly one of these (kit2.NAV_LABELS):
    Home · Inbox | Work: Campaigns · Enrollments · Products · Disputes (count 0) | Finance: Wallet (trail ₹1,84,500) · Invoices | Workspace: Team · Settings
Top bar = breadcrumb left, Search + Help right (no bell; Inbox is the nav item). Signed in as Neha Kapoor, Owner; switcher = Lumen Labs.
Page wrapper: put your page inside <div class="b1-wrap">...</div> (add class "tall" to let the frame grow past 900px); b1-* classes
(.b1-head/.b1-h1/.b1-sub, .b1-card, .b1-row, .b1-tile, .b1-thumb, .b1-tabs, .b1-chip, .b1-field, .b1-sort, .btn sizes) are free to reuse.
"""
from kit2 import shell
from uikit2 import *
from uikit import icf


def btn(label, kind="s", size="", icon=None, aria=""):
    ico = ic(icon, 16) if icon else ""
    a = f' aria-label="{aria}"' if aria else ""
    return f'<button class="btn {kind} {size}"{a}>{ico}{label}</button>'


def ibtn(icon, aria, size="", kind="s"):
    return f'<button class="btn {kind} icon {size}" aria-label="{aria}">{ic(icon, 16)}</button>'


def tile(icon, color):
    return f'<span class="b1-tile">{ic(icon, 20, color)}</span>'


# ------------------------------------------------------------------ 1 Home
def d_home():
    """Brand Home, evolved (desk_home.py)."""
    from desk_home import page
    return page()

def _cc3(photo, store, title, line, money, state="", n=None, m=None, cls=""):
    """Brand campaign card, built from the kit's campaign card (dm-cc): photo, store, title, one money figure, the creators bar, one state."""
    sr = (f'<span class="dm-store">{plat(store, 14)}{store.title()}</span>' if store in ("nykaa", "amazon")
          else f'<span class="dm-store">{ic("gift", 14)}We ship it to them</span>')
    pay = f'<div class="dm-pay"><b class="dm-bk num">{money}</b><span class="dm-bn">spent</span></div>' if money else ""
    bar = f'<div class="bar2"><i style="width:{round(n*100/m)}%"></i></div>' if n else ""
    sp = f'<span class="dm-sp"><b class="num">{n} of {m}</b> creators</span>' if n else f'<span class="dm-sp">{line}</span>'
    st = f'<div class="dm-state">{state}</div>' if state else ""
    return (f'<div class="dm-cc {cls}"><div class="dm-ph"><img src="{PH[photo]}" alt=""></div><div class="dm-cb">'
            f'<div class="dm-sr">{sr}<span class="dm-by">{line if n else ""}</span></div><div class="dm-ti">{title}</div>{pay}{bar}'
            f'<div class="dm-ft">{sp}{st}</div></div></div>')


def d_campaigns_list():
    from uikit2 import stat, goal
    P = lambda kind, icon, t: f'<span class="dm-pill {kind}">{ics(icon, 13) if icon else ""}{t}</span>'
    cards = "".join([
        _cc3("serum", "nykaa", "Glow serum, 30 ml", "Ends 26 Nov", "₹1,16,920", P("warn", "clock", "9 to review"), 112, 120),
        _cc3("cream", "amazon", "Night cream, 50 g", "Ends 12 Dec", "₹46,020", "", 42, 100),
        _cc3("bottles", "nykaa", "Daily cleanser trio", "Ends 5 Dec", "₹9,540", "", 18, 90),
        _cc3("set", "barter", "Clear skin set", "Ends 30 Nov", "₹24,190", P("mute", "", "Full"), 60, 60),
        _cc3("sand", "nykaa", "Sunscreen SPF 50, 50 ml", "Sent 19 Nov", "", P("info", "clock", "In review"), cls="off"),
        _cc3("mask", "nykaa", "Hair oil, 100 ml", "Sent back 18 Nov", "", P("warn", "alert", "Sent back"), cls="off"),
        _cc3("flatlay", "nykaa", "Vitamin C drops, 15 ml", "Edited 19 Nov", "", P("mute", "", "Draft"), cls="off"),
        _cc3("serum", "nykaa", "Lip balm duo", "Ended 31 Oct", "₹88,340", P("mute", "", "Ended"), 70, 70, cls="off"),
    ])
    strip = (goal("Creators joined", 232, 370) + stat("Spent this month", "₹96,380", "+31%", True, spark=[10, 14, 13, 18, 22, 26, 31], uid="cl1")
             + stat("Posts live this week", "18", "+42%", True, spark=[6, 9, 11, 10, 13, 15, 18], kind="bars"))
    tabs = "".join(f'<span class="{"on" if i == 0 else ""}">{t}<span class="cnt-b">{c}</span></span>' for i, (t, c) in enumerate(
        (("All", 8), ("Active", 4), ("Action required", 1), ("Draft and in review", 2), ("Ended", 1))))
    page = (f'<div class="b1-wrap tall v3k"><div class="v3-head"><div class="t"><h1 class="b1-h1">Campaigns</h1>'
            f'<p class="b1-sub">Glow serum is <b>93% full</b> and has <b>9 submissions</b> waiting for you. 4 campaigns are live.</p></div>'
            f'<div class="b1-acts">{ibtn("more", "More")}{btn("Create campaign", "p", "", "plus")}</div></div>'
            f'<div class="v3-strip">{strip}</div>'
            f'<div class="tabs">{tabs}</div>'
            f'<div class="v3-tool"><div class="input">{ic("search", 18)}<span class="ph">Search campaigns</span></div><span style="flex:1"></span>'
            f'<span class="chip">Sort: Recent{ic("down", 14)}</span>{btn("Select", "s", "md")}</div>'
            f'<div class="v3-grid4">{cards}</div></div>')
    return shell("Campaigns", ["Lumen Labs", "Campaigns"], page)


# ------------------------------------------------------------------ 3 Campaign detail
def d_campaign():
    from uikit2 import segs
    PP = lambda k: f"{STOCK}/people/{k}.jpg"
    def post(ph, kind, who, name, meta):
        k = (f'{soc("Instagram", 14)}Reel' if kind == "ig" else f'{plat("nykaa", 14)}Review')
        return (f'<div class="v3-post"><div class="th"><img src="{PH[ph]}" alt=""><span class="k">{k}</span></div>'
                f'<div class="who"><img src="{PP(who)}" alt=""><div><b>{name}</b><small>{meta}</small></div></div></div>')
    posts = "".join([post("mask", "ig", "women-68", "Riya Sharma", "Posted 2 days ago"), post("bottles", "ig", "men-12", "Kabir Singh", "Posted 3 days ago"),
                     post("cream", "ny", "women-44", "Meera Joshi", "Posted 3 days ago"), post("flatlay", "ig", "women-21", "Ananya Das", "Posted 4 days ago")])
    def task(icon_html, title, meta):
        return (f'<div class="row"><span class="x-tile">{icon_html}</span><div class="tx"><b>{title}</b><small>{meta}</small></div></div>')
    tasks = "".join([
        task(ic("receipt", 20, "var(--hd-tone-ink)"), "Order receipt", "Order ID, product, value and date · Always required"),
        task(soc("Instagram", 20), "Instagram reel", "Link and screenshots · #ad · “Paid partnership” label"),
        task(plat("nykaa", 20), "Nykaa review", "Link and screenshot · at least 40 words"),
    ])
    sw = '<input type="checkbox" class="switch" checked aria-label="Visible in creator app">'
    facts = [("Campaign type", "Online purchase"), ("Enrollment type", "Open to all"), ("Posting period", "45 days after joining"),
             ("Start date", "12 Nov 2026"), ("Ends", "26 Nov 2026"), ("Visible in creator app", f'{sw}On')]
    det = '<div class="panel v3-facts">' + "".join(f'<div><span>{k}</span><b>{v}</b></div>' for k, v in facts) + '</div>'
    brief = (f'<div class="panel v3-brief"><span class="k">Title</span><h4>Try the Glow serum</h4>'
             f'<div class="v3-dd"><div><span class="k">Do</span><p class="ok">{ic("check", 16)}Show the texture on skin</p></div>'
             f'<div><span class="k">Don’t</span><p class="no">{ic("x", 16)}No before and after claims</p></div></div></div>')
    ink = (f'<div class="mn-hero ink"><div class="mn-hl">Spent so far · 74 approved</div><div class="mn-hn num">₹1,16,920</div>'
           f'<a class="mn-hold"><span class="num">₹60,040</span>&nbsp;on hold for 38 creators in progress</a>'
           f'<div class="mn-hb"><button class="btn inv">{ic("download", 16)}Export CSV</button></div></div>')
    def ln(k, v, b=False): return f'<div class="mn-ln"><span>{k}</span><span class="num{" b" if b else ""}">{v}</span></div>'
    cost = (f'<div class="mn-card mn-rc"><div class="mn-rh"><div class="mn-rt"><b>Your cost per approval</b><small>Listed at ₹1,899 on Nykaa</small></div></div>'
            f'<div class="mn-lns">{ln("Order funding · 60% of the order", "₹1,339")}{ln("Bonus per creator", "₹200")}{ln("GST (18%)", "₹241")}{ln("Total", "₹1,580", True)}</div></div>')
    page = (f'<div class="b1-wrap tall v3k"><div class="v3-prod"><img class="ph" src="{PH["serum"]}" alt="">'
            f'<div class="tx"><div class="top"><span class="badge success">{ics("ok", 13)}Live</span><span class="b1-meta">Ends 26 Nov 2026</span></div>'
            f'<h1 class="b1-h1 big">Glow serum, 30 ml</h1>'
            f'<p class="b1-sub">31 of 52 posts so far came from this campaign. <b>9 submissions</b> are waiting for you.</p>'
            f'<div class="cr"><div class="lab"><b class="num">112 of 120</b> creators joined<span>8 spots left</span></div>{segs(112/120, 24)}</div></div>'
            f'<div class="b1-acts">{ibtn("more", "More")}{btn("Review 9", "p")}</div></div>'
            f'<div class="v3-cols"><div class="v3-main">'
            f'<div><div class="v3-sechd"><h2>Posts from creators</h2><span>31 posts live</span></div><div class="v3-posts">{posts}</div></div>'
            f'<div><div class="v3-sechd"><h2>Tasks</h2><span>Creators do them in this order</span></div><div class="stack" style="gap:8px">{tasks}</div></div>'
            f'<div class="v3-two"><div><div class="v3-sechd"><h2>Brief</h2></div>{brief}</div><div><div class="v3-sechd"><h2>Details</h2></div>{det}</div></div></div>'
            f'<div class="v3-side">{ink}{cost}</div></div></div>')
    return shell("Campaigns", ["Lumen Labs", "Campaigns", "Glow serum, 30 ml"], page)


# ------------------------------------------------------------------ 4 Composer, step 2 (Set up)
def d_composer(theme="light"):
    steps = [("box", "Product", "done"), ("sliders", "Set up", "on"), ("send", "Review", "")]
    track = ""
    for i, (icn, lab, st) in enumerate(steps):
        if i: track += '<span class="ln"></span>'
        track += f'<span class="s {st}">{ics("check", 18) if st == "done" else (ics(icn, 18) if st == "on" else ic(icn, 18))}{lab}</span>'
    top = (f'<div class="b1-top"><div class="l"><span class="b1-ib" aria-label="Leave the composer">{ic("x", 20)}</span><b>New campaign</b></div>'
           f'<div class="b1-track">{track}</div>'
           f'<div class="r"><span class="sv">{ics("ok", 16)}Draft saved</span><span class="b1-ib" aria-label="More">{ic("more", 20)}</span></div></div>')

    def chips(items, on):
        return '<div class="v3-chips">' + "".join(f'<span class="chip{" on" if x == on else ""}">{x}</span>' for x in items) + '</div>'
    fld = lambda label, inner, help_="": f'<div class="field"><label>{label}</label>{inner}{f"<span class=help>{help_}</span>" if help_ else ""}</div>'
    card = lambda title, aside, body: (f'<div class="panel v3-fc"><div class="hd"><h2 class="b1-h2">{title}</h2>{aside}</div>{body}</div>')
    reward = card("Reward", "",
        '<span class="seg v3-seg"><span class="on">Online purchase</span><span>Barter</span><span>Store check-in</span><span>Content post</span></span>'
        '<p class="v3-hint">They buy it with their own money. You fund cashback on what they spent.</p>'
        f'<div class="v3-pay"><div><b class="num">You pay 50% of the order</b><span>about ₹650 per creator</span></div>{chips(["100%", "75%", "50%"], "50%")}</div>'
        '<p class="v3-hint">Your proposal. Hypedrive sets the final price when it approves.</p>'
        + fld("Bonus per creator (optional)", '<div class="input" style="max-width:220px"><span class="addon">₹</span><span class="num">100</span></div>'))
    creators = card("Creators", '<span class="v3-aside">You can add more later</span>',
        f'<div class="v3-inl"><span class="seg v3-step"><span>{ic("minus", 16)}</span><span class="on num">60</span><span>{ic("plus", 16)}</span></span>{chips(["10", "25", "50", "100"], "")}</div>')
    dates = card("Dates", '<span class="v3-aside"><b>23 Nov to 22 Dec</b> · 30 days</span>',
        f'<div class="v3-dg">{fld("Starts", chips(["Today", "Tomorrow", "Next Monday"], "Next Monday"))}{fld("Runs for", chips(["2 weeks", "30 days", "60 days", "Custom"], "30 days"))}</div>')
    trow = lambda icon_html, title, meta, tail: f'<div class="row"><span class="x-tile">{icon_html}</span><div class="tx"><b>{title}</b><small>{meta}</small></div>{tail}</div>'
    tasks = card("Tasks", '<span class="v3-aside">Creators do them in this order</span>',
        '<div class="stack" style="gap:8px">'
        + trow(ic("receipt", 20, "var(--hd-tone-ink)"), "Order receipt", "Order ID, product, value and date · Always required", f'<span class="v3-lock">{ic("lock", 18)}</span>')
        + trow(soc("Instagram", 20), "Instagram reel", "Link and screenshots · #ad · “Paid partnership” label", "")
        + trow(plat("nykaa", 20), "Nykaa review", "Link and screenshot · at least 40 words", "")
        + f'</div><div>{btn("Add task", "s", "sm", "plus")}</div>')
    read = card("What creators read", "",
        fld("Title", '<div class="input"><span>Try the Vitamin C drops</span></div>')
        + '<div class="v3-two2">' + fld("Do", '<div class="input textarea">Show the texture on skin</div>') + fld("Don’t", '<div class="input textarea">No before and after claims</div>') + '</div>'
        + '<div class="v3-two2">' + fld("Reference photos (optional)", f'<div class="input v3-drop">{ic("upload", 18)}<span>Add photos</span></div>')
        + fld("Links (optional)", f'<div class="input">{ic("link", 16)}<span class="ph">Paste a link</span></div>') + '</div>')
    form = (f'<div class="b1-form"><div class="intro"><h1 class="b1-h1">Set up the campaign</h1><p class="b1-sub">Filled in from your last Nykaa campaign. Change anything.</p></div>'
            f'{reward}{creators}{dates}{tasks}{read}</div>')
    summ = (f'<aside class="v3-sum"><img class="ph" src="{PH["flatlay"]}" alt=""><div class="pr"><div class="b1-title">Vitamin C drops, 15 ml</div>'
            f'<div class="st">{plat("nykaa", 14)}Nykaa · ₹1,299</div></div>'
            f'<div class="fig"><span>Your cost per approval</span><b class="num">₹885</b><small>₹650 order funding + ₹100 bonus + ₹135 GST (18%)</small></div>'
            f'<dl><div><dt>Campaign type</dt><dd>Online purchase</dd></div><div><dt>Creators</dt><dd class="num">60</dd></div><div><dt>Dates</dt><dd>23 Nov to 22 Dec</dd></div></dl>'
            f'<div class="notice info">{icf("info")}<span>Hypedrive reviews every campaign before it goes live. You can still edit it until then.</span></div></aside>')
    foot = f'<div class="b1-foot">{btn("Back", "s")}{btn("Review", "p")}</div>'
    return f'<div class="shell b1-focus" data-theme="{theme}">{top}<div class="b1-body">{form}{summ}</div>{foot}</div>'


SCREENS = [("Brand · Home", d_home), ("Brand · Campaigns", d_campaigns_list), ("Brand · Campaign", d_campaign), ("Brand · New campaign", d_composer)]
