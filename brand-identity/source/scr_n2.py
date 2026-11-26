"""Creator screens, part 2: Enrollment detail, Withdraw, Settings, Barter. Built from kit components (dm-ns, dm-jr, dm-ship, dm-task, dm-sb, cv-wal Ink card, eb-empty2, row, badge)."""
from uikit2 import *
from kit4 import _st, _kv
from scr_v5 import s_enrollment_detail, _top, _steps  # v5: white pages (2026-11-26)
BA = "assets/brand"

def _bar(title="", right=""):
    t = f'<b class="n2-bt">{title}</b>' if title else '<span class="n2-bt"></span>'
    return f'<div class="xm1-bar xm1-s n2-bar">{ic("back", 22)}{t}{right}</div>'

def _row(lead, t, d, end=""):
    return f'<div class="row">{lead}<div class="tx"><b>{t}</b><small>{d}</small></div>{end}</div>'


# ====================================================================== c6: creator pages in the v5 language
STORE = lambda n: plat(n, 13) + n.title()
_T = lambda lead, t, m, end="", cls="": (f'<div class="w5-row {cls}">{lead}<div class="tx"><b>{t}</b><small>{m}</small></div>{end}</div>')
_task_tile = lambda logo: f'<span class="x-tile w5-ti">{logo}</span>'
_OFFER = (f'<div class="w5-sum c6-offer"><small>You get back</small><b class="num">₹1,339</b><dl>'
          '<dt>Order on Nykaa</dt><dd>₹1,899</dd><dt>Cashback, 60%</dt><dd class="in">₹1,139</dd><dt>Bonus</dt><dd class="in">₹200</dd></dl>'
          '<p>Paid to your wallet when Lumen Labs approves</p></div>')


def c6_welcome():
    body = (
        '<div class="xm1-s w5 c6-wel">'
        f'<img class="c6-logo" src="{LOGO["light"]}" alt="Hypedrive">'
        f'<div class="c6-mos"><img class="a" src="{PH["serum_hero"]}" alt=""><img class="b" src="{PH["cream"]}" alt=""><img class="c" src="{PH["sand"]}" alt=""></div>'
        '<h1 class="w5-h1 c6-wh">Products in.<br>Hype out.</h1>'
        '<p class="w5-lead">Try new products free, tell your people, and get paid for honest reviews.</p></div>'
        '<div class="w5-bb c6-wb"><button class="btn p lg block">Get started</button><button class="btn g block">I already have an account</button></div>')
    return phone(body, label="Welcome")


def c6_otp():
    cells = "".join(f'<span>{d}</span>' for d in "482") + '<span class="on"></span><span></span><span></span>'
    keys = [('1', ''), ('2', 'ABC'), ('3', 'DEF'), ('4', 'GHI'), ('5', 'JKL'), ('6', 'MNO'), ('7', 'PQRS'), ('8', 'TUV'), ('9', 'WXYZ'), ('', ''), ('0', ''), ('⌫', '')]
    body = (
        _top(ic("back", 22))
        + '<div class="xm1-s w5 c6-otp"><h1 class="w5-h1">Verify your phone</h1>'
        '<p class="w5-lead">Enter the 6-digit code sent to <b class="num c6-fg">+91 98•••• 4821</b></p>'
        f'<div class="xm1-code num c6-code" role="group" aria-label="6-digit code">{cells}</div>'
        '<p class="c6-auto">We check it as soon as you type the last digit.</p>'
        '<div class="c6-aux2"><span>Resend code in <span class="num">0:24</span></span><em class="w5-lk">Change number</em></div></div>'
        '<div class="xm1-pad">' + "".join(f'<span><b>{ic("back", 22) if a == "⌫" else a}</b><small>{b}</small></span>' for a, b in keys) + '</div>')
    return phone(body, label="Verify phone")


def c6_detail():
    top = (f'<div class="c6-hero"><img src="{PH["serum_hero"]}" alt=""><div class="tb"><span class="x-disc">{ic("back", 22)}</span>'
           f'<span class="c6-tbr"><span class="x-disc">{ic("heart", 20)}</span><span class="x-disc">{ic("share", 20)}</span></span></div></div>')
    body = (
        '<div class="xm1-s w5 c6-det">' + top
        + f'<div class="c6-by">{plat("nykaa", 14)}Nykaa<span>·</span>Lumen Labs{vhex(14)}<span>·</span>Closes 26 Nov</div>'
        '<h1 class="w5-h1">Glow serum, 30 ml</h1>'
        + _OFFER
        + '<div class="w5-sh"><h2>What you\'ll create</h2><span>2 tasks</span></div>'
        + _T(_task_tile(soc("Instagram", 22)), "Instagram reel", "Link + screenshots · #ad")
        + _T(_task_tile(plat("nykaa", 22)), "Nykaa review", "Link + screenshot · 40+ words")
        + '</div><div class="w5-bb"><button class="btn p lg block">Join campaign</button></div>')
    return phone(body, label="Campaign")


def _sheet(step, title, left, inner, act, note):
    return (f'<div class="jf-under"><img src="{PH["serum_hero"]}" alt=""></div><div class="scrim"></div><div class="overlay"><div class="sheet jf c6-sh"><div class="grab"></div>'
            f'<div class="jf-hd"><div><small>{step}</small><h2>{title}</h2></div><span class="x-disc jf-x">{ic("x", 18)}</span></div>'
            f'<div class="c6-hold">{ics("clock", 16)}<span>Spot held · <b class="num">{left}</b> left</span><button class="jf-add">Add 10 min</button></div>'
            f'{inner}<div class="jf-act">{act}</div><p class="jf-note">{note}</p></div></div>')


def c6_apply():
    inner = (_T(f'<img src="{PH["serum"]}" alt="">', "Glow serum, 30 ml", "You pay ₹1,899 on Nykaa")
             + '<dl class="c6-dl"><dt>You get back</dt><dd class="in">₹1,339</dd><dt>It costs you</dt><dd>₹560</dd></dl>')
    act = f'<button class="btn p lg block"><span class="c6-bn">Buy on {plat("nykaa", 16)}Nykaa</span></button><button class="btn g block">I\'ve ordered, add receipt</button>'
    return phone(_sheet("Step 1 of 2", "Buy it first", "9:41", inner, act, "You can leave before you buy."), label="Join · buy", sbar_color="#fff")


def c6_receipt():
    inner = (_T(f'<span class="x-tile w5-ti">{ic("file", 20)}</span>', "nykaa-order-4471.pdf", "284 KB", '<span class="w5-lk">Replace</span>')
             + f'<div class="c6-ok">{ics("success", 20)}<div><b>Your receipt is verified</b><small>Nykaa · <span class="num">₹1,899</span> · 20 Nov 2026</small></div></div>')
    act = '<button class="btn p lg block">Join and earn ₹1,339</button>'
    return phone(_sheet("Step 2 of 2", "Add your receipt", "6:12", inner, act, "You\'ll have 45 days to post after you join."), label="Join · receipt", sbar_color="#fff")


def c6_submit(theme="light"):
    def task(logo, t, req, lab, link, shots):
        Z = ["40% 40%", "80% 25%", "20% 80%", "60% 70%"]   # every screenshot shows Glow serum, framed differently
        th = "".join(f'<span class="c6-sh1"><span class="c6-shc"><img src="{PH["serum"]}" alt="" style="transform-origin:{Z[n % 4]};transform:scale(2)"></span><i>{ic("x", 10, "currentColor", 3)}</i></span>' for n, k in enumerate(shots) if k)
        return (f'<div class="c6-tk"><div class="c6-th">{_task_tile(logo)}<div class="tx"><b>{t}</b><small>{req}</small></div></div>'
                f'<label class="w5-f c6-f"><div class="w5-in c6-in">{ic("link", 16)}<em>{link}</em></div></label>'
                f'<div class="c6-fl"><div class="c6-shots">{th}<span class="c6-add">{ic("plus", 20)}</span></div></div></div>')
    body = (
        _top(ic("x", 22), '<span class="c6-saved">Draft saved</span>')
        + '<div class="xm1-s w5 c6-sub"><h1 class="w5-h1">Submit tasks</h1><p class="w5-lead">Glow serum, 30 ml · due in 41 days</p>'
        + '<div class="c6-tks">'
        + task(soc("Instagram", 22), "Instagram reel", "#ad, paid partnership label", "Link to your reel", "instagram.com/reel/C9xQ2…", ("serum", "flatlay", "sand"))
        + task(plat("nykaa", 22), "Nykaa review", "40+ words, 1 screenshot", "Link to your review", "nykaa.com/reviews/glow-serum…", ("bottles",))
        + '</div></div>'
        '<div class="w5-bb"><p>2 of 2 ready · I confirm these posts are mine.</p><button class="btn p lg block">Submit 2 tasks</button></div>')
    return phone(body, theme=theme, label="Submit tasks")


def c6_wallet(theme="light"):
    led = lambda lead, t, m, amt, cls="": _T(lead, t, m, f'<b class="num c6-amt {cls}">{amt}</b>')
    body = (
        _top('<h1 class="w5-h1 w5-inbar">Wallet</h1>', ic("settings", 22))
        + '<div class="xm1-s w5 c6-wal m7">'
        '<div class="m7-money"><small>Available</small><b class="num">₹6,820</b><p><b class=num>₹1,339</b> on hold · <b class=num>₹24,610</b> earned so far</p>'
        f'<div class="m7-ft">{ics("privacy", 18, "var(--hd-accent)")}<span>Verify your PAN to withdraw</span><em class="w5-lk">Verify</em></div></div>'
        '<div class="w5-sh"><h2>Activity</h2><span class="c6-lk">Statements</span></div>'
        + led(bank("hdfc", 28, True), "Withdrawal", "HDFC ••6093 · 16 Nov", "−₹2,000")
        + led(f'<img src="{PH["bottles"]}" alt="">', "Cashback", "Face wash · 12 Nov", "+₹540", "in")
        + led(bank("hdfc", 28, True), "Withdrawal", "HDFC ••6093 · 2 Nov", "−₹3,000")
        + '</div>' + tabbar("Wallet"))
    return phone(body, theme=theme, label="Wallet")


def c6_success(theme="light"):
    body = (
        _top("", ic("x", 22))
        + '<div class="xm1-s w5 c6-ok1">'
        f'<img class="c6-ill" src="{ILL[("approved", theme)]}" alt="">'
        '<h1 class="w5-h1">Tasks submitted</h1>'
        '<p class="w5-lead">Lumen Labs will review your 2 tasks. We\'ll tell you the moment they\'re approved.</p>'
        + _T(f'<img src="{PH["serum"]}" alt="">', "Glow serum, 30 ml", "₹1,339 back after approval", "", "c6-nx")
        + '</div><div class="w5-bb"><button class="btn p lg block">View enrollment</button><button class="btn g block c6-bk">Back to Home</button></div>')
    return phone(body, theme=theme, label="Tasks submitted")


def c6_inbox(theme="light"):
    dot = lambda on: f'<i class="c6-dot{" on" if on else ""}"></i>'
    item = lambda lead, t, m, tm, on=False: _T(lead, t, f'{m} · {tm}', dot(on))
    img = lambda k: f'<img src="{PH[k]}" alt="">'
    tabs = [("grid", "var(--hd-accent)", "All", "5"), ("clock", "var(--hd-tone-marigold)", "To do", "2"),
            ("wallet", "var(--hd-success-strong)", "Money", "2"), ("campaign", "var(--hd-info)", "Campaigns", "1")]
    # inbox tabs
    chips = "".join(f'<span{" class=on" if i == 0 else ""}>{ics(n, 16, c)}{t} <span class="tc">{k}</span></span>' for i, (n, c, t, k) in enumerate(tabs))
    body = (
        _top('<h1 class="w5-h1 w5-inbar">Inbox</h1>', '<span class="c6-lk">Mark all read</span>')
        + '<div class="xm1-s w5 c6-inb">'
        f'<div class="tabs w5-tabs c6-tabs">{chips}</div>'
        '<div class="w5-sh"><h2>Today</h2></div>'
        + item(img("sand"), "You can join Skin routine kit", "Approved · join by 26 Nov", "2m", True)
        + item(img("serum"), "Receipt checked", "Submit 2 tasks next", "4h", True)
        + item(img("bottles"), "Fix 1 task", "Daily cleanser trio", "6h", True)
        + '<div class="w5-sh"><h2>Earlier</h2></div>'
        + item(img("bottles"), "Earnings landed", "₹540 from Face wash", "Wed")
        + item(bank("hdfc", 28, True), "Withdrawal sent", "₹2,000 to HDFC ••6093", "Mon")
        + '</div>')
    return phone(body, theme=theme, label="Inbox")


def c6_empty(theme="light"):
    sim = [("flatlay", "nykaa", "Rose toner", "50% back"), ("sand", "nykaa", "Skin routine kit", "40% back")]   # only campaigns Riya hasn't joined
    rows = "".join(_T(f'<img src="{PH[i]}" alt="">', t, f'{plat(p, 13)}{p.title()} · Lumen Labs', f'<b class="num c6-amt">{r}</b>') for i, p, t, r in sim)
    body = (
        f'<div class="searchbar"><div class="search foc">{ic("search", 18)}<span class="q">matcha whisk</span><span class="clr">{ic("x", 11, sw=3)}</span></div><button class="btn link" style="text-decoration:none">Cancel</button></div>'
        '<div class="xm1-s w5 c6-emp">'
        f'<div class="c6-em"><img src="{ILL[("search", theme)]}" alt=""><b>No campaigns found</b><p>Nothing matches “matcha whisk”. Check the spelling or try a shorter word.</p></div>'
        '<div class="w5-sh"><h2>Open now</h2><span class="c6-lk">See all</span></div>' + rows + '</div>' + tabbar("Campaigns"))
    return phone(body, theme=theme, label="Empty search")


def s_withdraw():
    """Honest state: PAN is not verified, so the page is the blocker, with no keypad."""
    body = (
        _top(ic("back", 22))
        + '<div class="xm1-s w5 c6-wd m7"><h1 class="w5-h1">Withdraw</h1><p class="w5-lead">Verify your PAN first. It takes a minute and is needed once.</p>'
        f'<img class="c6-ill c6-ill2" src="{BA}/hypedrive-ill-payout-light.svg" alt="">'
        '<div class="m7-money"><small>Available to withdraw</small><b class="num">₹6,820</b><p><b class=num>₹1,339</b> on hold · stays safe until you verify</p>'
        f'<div class="m7-ft">{bank("hdfc", 20)}<span>To HDFC ••6093 · fee ₹0</span><em class="w5-lk">Change</em></div></div>'
        + '</div><div class="w5-bb"><button class="btn p lg block">Verify PAN</button></div>')
    return phone(body, label="Withdraw")


def s_settings(theme="light"):
    dark = theme == "dark"
    row = lambda ico, t, v, cls="": f'<div class="c6-sr">{ic(ico, 20)}<b>{t}</b><span class="{cls}">{v}</span>{ic("chev", 16)}</div>'
    grp = lambda h, *rows: f'<div class="w5-sh c6-gh"><h2>{h}</h2></div><div class="c6-grp">' + "".join(rows) + '</div>'
    body = (
        _top(ic("back", 22))
        + '<div class="xm1-s w5 c6-set"><h1 class="w5-h1">Settings</h1>'
        f'<div class="w5-row c6-me"><img class="c6-ava" src="{STOCK}/people/women-68.jpg" alt="Riya Sharma"><div class="tx"><b>Riya Sharma</b><small>@riya.glows · Kolkata</small></div></div>'
        + grp("Account", row("user", "Personal info", ""), row("privacy", "Verification (PAN)", "Not verified", "warn"),
              row("bank", "Payout methods", "HDFC ••6093"), row("pin", "Addresses", "1 saved"))
        + grp("Security", row("lock", "Sign-in and security", ""), row("phone", "Devices", "2"))
        + grp("Preferences", row("bell", "Notifications", ""), row("sliders", "Appearance", "Dark" if dark else "Light"))
        + '</div>')
    return phone(body, theme=theme, label="Settings · dark" if dark else "Settings")


def s_barter():
    body = (
        _top(ic("back", 22), ic("more", 22))
        + '<div class="xm1-s w5 c6-bar">'
        f'<div class="w5-prod"><img src="{PH["set"]}" alt=""><div><b>Clear skin set</b><small>Worth ₹2,400 · +₹500 bonus</small></div></div>'
        f'<div class="c6-bh"><div><h1 class="w5-h1">Arriving Mon, 23 Nov</h1><p class="w5-lead">Delhivery is bringing your Clear skin set</p></div></div>'
        + _steps(["Requested", "On the way", "Delivered"], 1)
        + f'<img class="c6-ill c6-ill3" src="{BA}/hypedrive-ill-tracking-light.svg" alt="">'
        '<div class="w5-sh"><h2>Delivery</h2></div>'
        '<dl class="c6-dl c6-dl2 c6-card"><dt>Ship to</dt><dd>14 Park Street, Kolkata 700016</dd><dt>Carrier</dt><dd>Delhivery</dd><dt>Tracking</dt><dd class="num">4471 2280</dd></dl>'
        '<div class="w5-sh"><h2>After it arrives</h2></div>'
        + _T(_task_tile(soc("Instagram", 22)), "Instagram reel", "Opens when your order arrives", ics("lock", 18, "var(--hd-fg-subtle)"))
        + '</div><div class="w5-bb"><button class="btn p lg block">Track shipment</button></div>')
    return phone(body, label="Barter enrollment")
