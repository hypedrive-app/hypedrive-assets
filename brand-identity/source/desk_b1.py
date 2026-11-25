"""Brand desktop, part 1 (agent b1): Home, Campaigns list, Campaign detail, New campaign composer. Spec: BRAND-SPEC.md.

NAV LABELS for shell(active, crumbs, page) — `active` must be exactly one of these (kit2.NAV_LABELS):
    Home · Inbox | Work: Campaigns · Enrollments · Products · Disputes (count 0) | Finance: Wallet (trail ₹1,84,500) · Invoices | Workspace: Team · Settings
Top bar = breadcrumb left, Search + Help right (no bell; Inbox is the nav item). Signed in as Neha Kapoor, Owner; switcher = Lumen Labs.
Page wrapper: put your page inside <div class="b1-wrap">...</div> (add class "tall" to let the frame grow past 900px); b1-* classes
(.b1-head/.b1-h1/.b1-sub, .b1-card, .b1-row, .b1-tile, .b1-thumb, .b1-tabs, .b1-chip, .b1-field, .b1-sort, .btn sizes) are free to reuse.
"""
from kit2 import shell
from uikit2 import *


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
    def todo(title, meta, label, due=False):
        m = f'<div class="b1-meta{" due" if due else ""}">{meta}</div>'
        return (f'<div class="b1-row"><div class="tx"><div class="b1-title">{title}</div>{m}</div>'
                f'<span class="b1-act">{label}</span></div>')
    rows = "".join([
        todo("Review submissions", "Oldest waited 2 days · Approve or send back each one", "Review 9"),
        todo("Review applications", "For 1 campaign · Accept or decline each one", "Review 4"),
        todo("Ship products", "Oldest waited 1 day · Creators’ days to post start on delivery", "Ship 3"),
        todo("Reply to disputes", "Reply by 24 Nov", "Reply", True),
    ])
    last = (f'<div class="b1-card b1-last"><div><span class="b1-meta">Creators approved</span><b>61</b></div>'
            f'<p><span>52 reviews published</span><span>₹1,580 average per creator</span></p></div>')

    def live(img, name, meta, warn=""):
        w = f' · <span class="due">{warn}</span>' if warn else ""
        return (f'<div class="b1-row"><img class="b1-thumb" src="{PH[img]}" alt=""><div class="tx"><div class="b1-title">{name}</div>'
                f'<div class="b1-meta">{meta}{w}</div></div></div>')
    lives = "".join([
        live("serum", "Glow serum, 30 ml", "112/120 joined", "Ends in 6 days"),
        live("cream", "Night cream, 50 g", "42/100 joined"),
        live("bottles", "Daily cleanser trio", "18/90 joined"),
        live("set", "Clear skin set", "60/60 joined · Full"),
    ])
    wallet = (f'<div class="b1-card b1-wal"><span class="b1-meta">Available balance</span><span class="big">₹1,84,500</span>'
              f'<p><b>₹96,320</b> on hold for creators who joined</p>'
              f'<div class="foot">{btn("Add money", "s", "md")}</div></div>')
    page = (f'<div class="b1-wrap"><div class="b1-head"><div class="t"><h1 class="b1-h1">Good morning, Neha</h1><p class="b1-sub">4 things need you today.</p></div>'
            f'<div class="b1-acts">{btn("Create campaign", "p", "", "plus")}</div></div>'
            f'<div class="b1-home"><div class="b1-col" style="gap:32px"><section><div class="b1-sechd"><h2 class="b1-h2">For you today</h2></div><div class="b1-todo">{rows}</div></section>'
            f'<section><div class="b1-sechd"><h2 class="b1-h2">Last 30 days</h2></div>{last}</section></div>'
            f'<div class="b1-side"><section><div class="b1-sechd"><h2 class="b1-h2">Wallet</h2><span class="b1-link">Open wallet</span></div>{wallet}</section>'
            f'<section><div class="b1-sechd"><h2 class="b1-h2">Live campaigns</h2><span class="b1-link">All campaigns</span></div><div class="b1-live">{lives}</div></section></div></div></div>')
    return shell("Home", ["Lumen Labs", "Home"], page)


# ------------------------------------------------------------------ 2 Campaigns list
def d_campaigns_list():
    N = '<img src="assets/stock/platforms/nykaa.png" alt="">'
    A = '<img src="assets/stock/platforms/amazon.png" alt="">'
    # img, title, store html, store label, status badge, dates, creators, spent
    W = lambda t: f'<span class="badge warning">{t}</span>'
    M = lambda t: f'<span class="b1-sx">{t}</span>'
    # img, title, store html, store label, status (only exceptions carry a badge), dates, creators, spent
    data = [
        ("serum", "Glow serum, 30 ml", N, "Nykaa", W("9 to review"), "Ends 26 Nov", "112", "120", "₹1,16,920"),
        ("cream", "Night cream, 50 g", A, "Amazon", "", "Ends 12 Dec", "42", "100", "₹46,020"),
        ("bottles", "Daily cleanser trio", N, "Nykaa", "", "Ends 5 Dec", "18", "90", "₹9,540"),
        ("set", "Clear skin set", "", "We ship it to them", M("Full"), "Ends 30 Nov", "60", "60", "₹24,190"),
        ("sand", "Sunscreen SPF 50, 50 ml", N, "Nykaa", M("In review"), "Sent 19 Nov", "", "", ""),
        ("mask", "Hair oil, 100 ml", N, "Nykaa", W("Sent back"), "18 Nov", "", "", ""),
        ("flatlay", "Vitamin C drops, 15 ml", N, "Nykaa", M("Draft"), "Edited 19 Nov", "", "", ""),
        ("serum", "Lip balm duo", N, "Nykaa", M("Ended"), "31 Oct", "70", "70", "₹88,340"),
    ]
    rows = ""
    for img, title, ico, store, badge, dt, j, m, sp in data:
        meta = f'<span class="b1-st">{ico}{store}</span>'
        cr = f'<span class="cr">{j} of {m} <small>creators</small></span>' if j else '<span></span>'
        spv = f'<span class="sp">{sp}</span>' if sp else ''
        rows += (f'<div class="b1-row b1-crow"><img class="b1-thumb" src="{PH[img]}" alt=""><div class="tx"><div class="b1-title">{title}</div>{meta}</div>'
                 f'<span>{badge}</span><span class="dt">{dt}</span>{cr}<span class="r">{spv}</span></div>')
    tabs = "".join(f'<span class="{"on" if i == 0 else ""}">{t}<i>{c}</i></span>' for i, (t, c) in enumerate(
        (("All", 8), ("Active", 4), ("Action required", 1), ("Draft and in review", 2), ("Ended", 1))))
    page = (f'<div class="b1-wrap tall"><div class="b1-head"><div class="t"><h1 class="b1-h1">Campaigns</h1><p class="b1-sub">8 campaigns, 4 live.</p></div>'
            f'<div class="b1-acts">{ibtn("more", "More")}{btn("Create campaign", "p", "", "plus")}</div></div>'
            f'<div class="b1-tabs">{tabs}</div>'
            f'<div class="b1-tool"><div class="b1-field">{ic("search", 18)}Search campaigns</div><span style="flex:1"></span>'
            f'<span class="b1-sort">Sort<b>Recent</b>{ic("down", 16)}</span>{btn("Select", "s")}</div>'
            f'<div class="b1-cols"><span></span><span>Campaign</span><span>Status</span><span>Dates</span><span>Creators</span><span class="r">Spent</span></div>'
            f'<div class="b1-list">{rows}</div></div>')
    return shell("Campaigns", ["Lumen Labs", "Campaigns"], page)


# ------------------------------------------------------------------ 3 Campaign detail
def d_campaign():
    def task(icon_html, title, meta):
        return (f'<div class="b1-row b1-task"><span class="b1-tile">{icon_html}</span><div class="tx"><div class="b1-title">{title}</div>'
                f'<div class="b1-meta">{meta}</div></div></div>')
    tasks = "".join([
        task(ic("receipt", 20, "var(--hd-tone-ink)"), "Order receipt", "Order ID, product, value and date · Always required"),
        task(soc("Instagram", 20), "Instagram reel", "Link and screenshots · #ad · “Paid partnership” label"),
        task('<img src="assets/stock/platforms/nykaa.png" alt="">', "Nykaa review", "Link and screenshot · at least 40 words"),
    ])
    brief = (f'<div class="b1-card"><div class="b1-brief"><div style="grid-column:1/-1"><div class="k">Title</div><h4 style="margin:0">Try the Glow serum</h4></div>'
             f'<div><div class="k">Do</div><div class="it do">{ic("check", 16)}<span style="color:var(--hd-fg)">Show the texture on skin</span></div></div>'
             f'<div><div class="k">Don’t</div><div class="it dont">{ic("x", 16)}<span style="color:var(--hd-fg)">No before and after claims</span></div></div></div></div>')
    sw = '<input type="checkbox" class="switch" checked aria-label="Visible in creator app">'
    det = (f'<div class="b1-card"><div class="b1-dl">'
           f'<div><div class="k">Product</div><div class="v"><img src="{PH["serum"]}" alt="">Glow serum, 30 ml</div></div>'
           f'<div><div class="k">Campaign type</div><div class="v">Online purchase</div></div>'
           f'<div><div class="k">Enrollment type</div><div class="v">Open to all</div></div>'
           f'<div><div class="k">Posting period</div><div class="v">45 days after joining</div></div>'
           f'<div><div class="k">Start date</div><div class="v">12 Nov 2026</div></div>'
           f'<div><div class="k">Ends</div><div class="v">26 Nov 2026</div></div>'
           f'<div><div class="k">Visible in creator app</div><div class="v">{sw}On</div></div>'
           f'<div><div class="k">Share link</div><div class="v"><span class="mono">hypedrive.in/c/glow-serum</span>{ibtn("copy", "Copy link", "sm")}</div></div>'
           f'</div></div>')
    cost = (f'<div class="b1-card b1-cost"><div class="h">Your cost per approved enrollment</div><b class="big">₹1,580</b>'
            f'<p>60% of each order · ₹200 bonus · 18% GST</p>'
            f'<div class="b1-st" style="margin-top:12px">Listed at ₹1,899 on <img src="assets/stock/platforms/nykaa.png" alt="">Nykaa</div></div>')
    spent = (f'<div class="b1-card b1-cost"><div class="h">Spent so far · 74 approved</div><b class="big">₹1,16,920</b>'
             f'<p>Order ₹84,286 · bonus ₹14,800 · GST ₹17,834</p>'
             f'<div class="foot">{btn("Export CSV", "s", "md", "download")}</div></div>')
    page = (f'<div class="b1-wrap tall"><div class="b1-dh"><img class="b1-thumb" src="{PH["serum"]}" alt=""><div class="t"><h1 class="b1-h1">Glow serum, 30 ml</h1>'
            f'<div class="line"><span>Live · Ends 26 Nov</span></div></div>'
            f'<div class="b1-acts">{ibtn("more", "More")}{btn("Review 9", "p")}</div></div>'
            f'<p class="b1-line"><b>112 of 120</b> creators joined · <b>9</b> waiting for you · <b>₹60,040</b> on hold for 38 in progress</p>'
            f'<div class="b1-det"><div class="b1-col">'
            f'<section><div class="b1-sechd"><h2 class="b1-h2">Brief</h2></div>{brief}</section>'
            f'<section><div class="b1-sechd"><h2 class="b1-h2">Tasks</h2><span class="b1-meta">Creators do them in this order</span></div><div class="b1-stack">{tasks}</div></section>'
            f'<section><div class="b1-sechd"><h2 class="b1-h2">Details</h2></div>{det}</section></div>'
            f'<div class="b1-col"><section><div class="b1-sechd"><h2 class="b1-h2">Reward and spend</h2></div><div class="b1-stack" style="gap:12px">{cost}{spent}</div></section></div></div></div>')
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

    def opts(items, on):
        return '<div class="b1-opts">' + "".join(f'<span class="b1-opt{" on" if x == on else ""}">{x}</span>' for x in items) + '</div>'
    reward = (f'<div class="b1-card b1-fc"><div class="hd"><h2 class="b1-h2">Reward</h2></div>'
              f'<div class="b1-seg"><span class="on">Online purchase</span><span>Barter</span><span>Store check-in</span><span>Content post</span></div>'
              f'<p class="hint">They buy it with their own money. You fund cashback on what they spent.</p>'
              f'<div class="b1-grp"><div class="b1-payrow"><div class="b1-pay"><b>You pay 50% of the order</b><span>≈ ₹650</span></div>{opts(["100%", "75%", "50%"], "50%")}</div>'
              f'<p class="hint">Your proposal. Hypedrive sets the final price when it approves.</p></div>'
              f'<div class="b1-grp"><div class="lab">Bonus per creator <em>(optional)</em></div><div class="b1-in" style="max-width:200px"><span class="pre">₹</span>100</div></div></div>')
    creators = (f'<div class="b1-card b1-fc"><div class="hd"><h2 class="b1-h2">Creators</h2><span class="b1-meta">You can add more later</span></div>'
                f'<div class="b1-inl"><div class="b1-stepper"><span>{ic("minus", 16)}</span><b>60</b><span>{ic("plus", 16)}</span></div>{opts(["10", "25", "50", "100"], "")}</div></div>')
    dates = (f'<div class="b1-card b1-fc"><div class="hd"><h2 class="b1-h2">Dates</h2><span class="b1-aside"><b>23 Nov to 22 Dec</b> · 30 days</span></div>'
             f'<div class="b1-dg"><div class="b1-grp"><div class="lab">Starts</div>{opts(["Today", "Tomorrow", "Next Monday"], "Next Monday")}</div>'
             f'<div class="b1-grp"><div class="lab">Runs for</div>{opts(["2 weeks", "30 days", "60 days", "Custom"], "30 days")}</div></div></div>')
    trow = lambda icon_html, title, meta, tail: (f'<div class="b1-trow"><span class="b1-tile">{icon_html}</span><div class="tx"><div class="b1-title">{title}</div><div class="b1-meta">{meta}</div></div>{tail}</div>')
    tasks = (f'<div class="b1-card b1-fc"><div class="hd"><h2 class="b1-h2">Tasks</h2><span class="b1-meta">Creators do them in this order</span></div><div class="b1-grp">'
             + trow(ic("receipt", 20, "var(--hd-tone-ink)"), "Order receipt", "Order ID, product, value and date · Always required", ic("lock", 18))
             + trow(soc("Instagram", 20), "Instagram reel", "Link and screenshots · #ad · “Paid partnership” label", "")
             + trow('<img src="assets/stock/platforms/nykaa.png" alt="">', "Nykaa review", "Link and screenshot · at least 40 words", "")
             + f'</div><div>{btn("Add task", "s", "sm", "plus")}</div></div>')
    read = (f'<div class="b1-card b1-fc"><div class="hd"><h2 class="b1-h2">What creators read</h2></div>'
            f'<div class="b1-grp"><div class="lab">Title</div><div class="b1-in">Try the Vitamin C drops</div></div>'
            f'<div class="b1-cols2"><div class="b1-grp"><div class="lab">Do</div><div class="b1-in ta">Show the texture on skin</div></div>'
            f'<div class="b1-grp"><div class="lab">Don’t</div><div class="b1-in ta">No before and after claims</div></div></div>'
            f'<div class="b1-cols2"><div class="b1-grp"><div class="lab">Reference photos <em>(optional)</em></div><div class="b1-drop">{ic("upload", 18)}Add photos</div></div>'
            f'<div class="b1-grp"><div class="lab">Links <em>(optional)</em></div><div class="b1-in ph">{ic("link", 16)}Paste a link</div></div></div></div>')
    form = (f'<div class="b1-form"><div class="intro"><h1 class="b1-h1">Set up the campaign</h1><p class="b1-sub">Filled in from your last Nykaa campaign. Change anything.</p></div>'
            f'{reward}{creators}{dates}{tasks}{read}</div>')
    summ = (f'<aside class="b1-card b1-sum"><div class="pr"><img class="b1-thumb" src="{PH["flatlay"]}" alt=""><div class="tx"><div class="b1-title">Vitamin C drops, 15 ml</div>'
            f'<div class="b1-st"><img src="assets/stock/platforms/nykaa.png" alt="">Nykaa · ₹1,299</div></div></div>'
            f'<dl><div><dt>Campaign type</dt><dd>Online purchase</dd></div><div><dt>Reward</dt><dd>50% of the order ≈ ₹650<br>+ ₹100 bonus per creator</dd></div>'
            f'<div><dt>Creators</dt><dd>60</dd></div><div><dt>Dates</dt><dd>23 Nov to 22 Dec</dd></div></dl>'
            f'<div class="rule">Hypedrive reviews every campaign before it goes live. You can still edit it until then.</div></aside>')
    foot = f'<div class="b1-foot">{btn("Back", "s")}{btn("Review", "p")}</div>'
    return f'<div class="shell b1-focus" data-theme="{theme}">{top}<div class="b1-body">{form}{summ}</div>{foot}</div>'


SCREENS = [("Brand · Home", d_home), ("Brand · Campaigns", d_campaigns_list), ("Brand · Campaign", d_campaign), ("Brand · New campaign", d_composer)]
