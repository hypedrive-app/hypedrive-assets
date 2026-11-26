"""Brand desktop, part 2 (agent b2): Review queue + submission, Wallet & funding (+ invoices), Team & settings. Spec: BRAND-SPEC.md."""
from kit2 import shell
from uikit2 import *

PEOPLE = {k: f"{STOCK}/people/{k}.jpg" for k in ("women-68", "women-44", "women-65", "men-12", "men-32", "women-21")}
NAV_ENROLL, NAV_WALLET, NAV_TEAM = "Enrollments", "Wallet", "Team"   # nav labels (re-check desk_b1.py header)

def inr(n):
    s = str(int(n))
    if len(s) <= 3: return "₹" + s
    head, tail = s[:-3], s[-3:]; parts = []
    while len(head) > 2: parts.insert(0, head[-2:]); head = head[:-2]
    if head: parts.insert(0, head)
    return "₹" + ",".join(parts) + "," + tail

def _btn(kind, label, icon=None, sm=True, extra=""):
    i = ic(icon, 16) if icon else ""
    return f'<button class="btn {kind}{" sm" if sm else ""}"{extra}>{i}{label}</button>'

# ====================================================================== 5 · review queue + one submission
def _seg(on):
    g = "on" if on == "good" else ""; n = "on" if on == "fix" else ""
    return (f'<span class="seg v3-vd {"fix" if on == "fix" else "good"}"><span class="{g}">{ics("check", 16) if g else ""}Looks good</span><span class="{n}">{ics("alert", 16) if n else ""}Needs a change</span></span>')

def _shot(src, w=200, h=252, tag="", zoom=""):
    """zoom = transform-origin: frames a different part of the same product photo, so every shot shows the campaign's product."""
    t = f'<span class="k">{tag}</span>' if tag else ""
    z = f' style="transform-origin:{zoom};transform:scale(1.8)"' if zoom else ""
    return f'<div class="v3-shot" style="width:{w}px;height:{h}px"><img src="{src}" alt=""{z}>{t}<a class="full">{ic("eye", 16)}Full size</a></div>'

def _task(glyph, title, meta, body, verdict):
    return (f'<div class="panel v3-task{" flag" if verdict == "fix" else ""}"><div class="th"><span class="x-tile">{glyph}</span>'
            f'<div class="tt"><b>{title}</b><small>{meta}</small></div>{_seg(verdict)}</div>{body}</div>')

def _link(url):
    return f'<div class="input v3-link">{ic("link", 16)}<span>{url}</span><a class="btn g sm">{ic("external", 16)}Open</a></div>'

def d_queue():
    def ln(k, v, cls=""): return f'<div class="mn-ln"><span>{k}</span><span class="num {cls}">{v}</span></div>'
    order = ('<div class="mn-lns v3-ord">' + ln("Product", "Glow serum, 30 ml") + ln("Store", plat("nykaa", 16) + " Nykaa") + ln("Order value", "₹1,899")
             + ln("Order ID", '<span class="b2-mono">NYK-2611-48213</span>') + ln("Order date", "14 Nov 2026")
             + ln("Order check", f'<span class="v3-ok">{ic("check", 16)}Matches</span>') + '</div>')
    rcpt = f'<div class="v3-recv">{_shot(PH["serum"], 200, 252, "", "50% 45%")}{order}</div>'
    reel = _link("instagram.com/reel/C-9xLm2Qa7R") + f'<div class="v3-shots fill">{_shot(PH["serum"], 200, 252, "Reel")}{_shot(PH["serum"], 200, 252, "", "80% 20%")}{_shot(PH["serum"], 200, 252, "", "20% 80%")}</div>'
    rev = _link("nykaa.com/glow-serum-30-ml/reviews") + f'<div class="v3-shots">{_shot(PH["serum"], 200, 200, "", "60% 60%")}<p class="v3-quote">“Nice texture, I use it every night.”<small>11 words, the brief asks for at least 40.</small></p></div>'
    tasks = (_task(ic("receipt", 20), "Order receipt", "Always required · Sent 18 Nov", rcpt, "good")
             + _task(soc("Instagram", 22), "Instagram reel", "Sent 18 Nov · Link and 3 screenshots", reel, "good")
             + _task(plat("nykaa", 22), "Nykaa review", "Sent 18 Nov · At least 40 words", rev, "fix"))
    chips = "".join(f'<span class="chip{" on" if i == 0 else ""}">{t}</span>' for i, t in enumerate(["Under 40 words", "Not about the product", "Screenshot unclear", "Link doesn't open"]))
    note = (f'<div class="panel v3-note"><b>Your note to Arjun</b><div class="v3-chips">{chips}</div>'
            '<div class="input textarea">The review is under 40 words. Please add a few lines on how the serum felt on your skin, then send it again.</div>'
            '<small>The creator gets until 25 Nov to fix these.</small></div>')
    cost = (f'<div class="mn-card mn-rc"><div class="mn-rh"><div class="mn-rt"><b>Your cost</b><small>Paid when you approve</small></div></div>'
            f'<div class="mn-lns">{ln("Cashback · 60% of ₹1,899", "₹1,139")}{ln("Bonus", "₹200")}{ln("GST (18%)", "₹241")}<div class="mn-ln"><span>Total</span><span class="num b">₹1,580</span></div></div></div>')
    bar = (f'<div class="b2-bar"><span class="b2-bt">Needs review</span><span class="b2-bn num">1 of 9</span><i class="b2-prog"><i style="width:11%"></i></i><span class="sp"></span>'
           f'{_btn("s", "Back", "back")}{_btn("s", "Next", "chev")}</div>')
    head = (f'<div class="b2-hd"><img class="b2-av" src="{PEOPLE["men-12"]}" alt=""><div class="b2-who"><div class="t-h1 b2-name">Arjun Kapoor</div>'
            f'<p>Waiting 2 days · Trusted · @arjun.k · Pune</p></div>'
            f'<div class="b2-camp"><img src="{PH["serum"]}" alt=""><div><b>Glow serum, 30 ml</b><small>Lumen Labs · Joined 14 Nov</small></div></div>{_btn("s", "Details")}</div>')
    band = (f'<div class="b2-band"><div class="b2-money"><b class="num">₹1,580</b><span>stays on hold while the creator fixes.</span></div><span class="sp"></span>'
            f'<button class="btn g">More</button><button class="btn s">Reject</button><button class="btn p">Send back 1 task</button></div>')
    body = f'<div class="v3-rbody v3k"><div class="v3-proof">{tasks}</div><div class="v3-decide">{note}{cost}</div></div>'
    page = f'<div class="v3-rv">{bar}{head}{body}{band}</div>'
    return shell(NAV_ENROLL, ["Lumen Labs", "Enrollments", "Arjun Kapoor"], page)

# ====================================================================== 6 · wallet and funding
def _arow(glyph, title, meta, amt, kind=""):
    return (f'<div class="b2-row"><span class="x-tile b2-tl">{glyph}</span><div class="b2-tt"><b>{title}</b><small>{meta}</small></div>'
            f'<b class="b2-amt num {kind}">{amt}</b></div>')

def _inv(week, num, n, total, status):
    gst = round(total * 18 / 118)
    badge = f'<span class="badge {"success" if status == "Paid" else "neutral"}">{status}</span>'
    cls = " void" if status == "Void" else ""
    return (f'<div class="b2-ir{cls}"><div class="b2-tt"><b>{week}</b><small><span class="b2-mono">{num}</span> · {n} enrollments</small></div>'
            f'<div class="b2-iamt"><b class="num">{inr(total)}</b><small class="num">GST {inr(gst)}</small></div>{badge}<a class="btn g sm b2-dl" aria-label="Download">{ic("download", 16)}</a></div>')

def d_wallet():
    """Wallet: the Ink balance (the kit's money hero), the kit's movement rows as the ledger, invoices and TDS as kit rows."""
    from kit5 import _mrow, _tile, _b
    hero = (f'<div class="v3-money wide"><div><span class="l">Available</span><b class="n num">₹1,84,500</b>'
            f'<p><span class="num">₹96,320</span> on hold for creators who joined · each approval is paid from here</p></div>'
            f'<div class="a"><button class="btn s">Withdraw</button><button class="btn p">{ic("plus", 16)}Add money</button></div></div>')
    rows = "".join([
        _mrow("plus", "Money added", "Razorpay · 19 Nov 2026", "+₹2,00,000"),
        _mrow("check", "Enrollment paid", "Ananya Das · Glow serum · 19 Nov 2026", "−₹1,580", out=True),
        _mrow("clock", "On hold", "Kabir Singh · Glow serum · 18 Nov 2026", "−₹1,580", out=True),
        _mrow("refresh", "Hold released", "Tanvi Shah · Clear skin set · 17 Nov 2026", "+₹2,900"),
        _mrow("bank", "Withdrawal", "HDFC Bank ••6093 · 12 Nov 2026", "−₹50,000", out=True),
        _mrow("receipt", "Refund", "Order cancelled · 10 Nov 2026", "+₹1,580"),
        _mrow("sliders", "Adjustment", "Hypedrive · 9 Nov 2026", "+₹320"),
    ])
    chips = "".join(f'<span class="{"on" if i == 0 else ""}">{ics(n, 16, c)}{t}</span>' for i, (n, c, t) in enumerate([("grid", "var(--hd-accent)", "All"), ("download", "var(--hd-success)", "Money in"), ("upload", "var(--hd-fg-muted)", "Money out"), ("clock", "var(--hd-tone-marigold)", "On hold")]))
    ledger = (f'<div><div class="v3-sechd"><h2>Activity</h2><em class="v3-lk">Statements</em></div><div class="tabs b6-tabs b6-wt">{chips}</div>'
              f'<div class="mn-card mn-list">{rows}</div></div>')
    def irow(wk, num, n, amt, void=False):
        sub = f'<span class="b2-mono">{num}</span> · ' + ("Void" if void else f"{n} enrollments")
        return (f'<div class="mn-row"><div class="mn-rt"><b>{wk}</b><small>{sub}</small></div>'
                f'<span class="mn-amt out num{" off" if void else ""}">{inr(amt)}</span><span class="v3-dlb">{ic("download", 16)}</span></div>')
    inv = (f'<div><div class="v3-sechd"><h2>Invoices</h2><span><b class="num">₹18,42,300</b> in FY 2026-27</span></div><div class="mn-card mn-list">'
           + irow("9 – 15 Nov", "LL/2627/0042", 31, 48980) + irow("2 – 8 Nov", "LL/2627/0041", 27, 42660)
           + irow("26 Oct – 1 Nov", "LL/2627/0040", 24, 37920) + irow("19 – 25 Oct", "LL/2627/0039", 22, 34760, True) + '</div></div>')
    q = lambda n, d, tail="": f'<div class="mn-row"><div class="mn-rt"><b>{n}</b><small>{d}</small></div>{tail}</div>'
    tds = (f'<div><div class="v3-sechd"><h2>TDS certificates</h2><span><b class="num">₹23,240</b> credited</span></div><div class="mn-card mn-list">'
           + q("Q3 Oct – Dec", "Due by 31 Jan 2027", '<em class="v3-lk">Send certificate</em>')
           + q("Q2 Jul – Sep", "Credited 12 Nov") + q("Q1 Apr – Jun", "Credited 12 Aug") + '</div></div>')
    head = ('<div class="v3-head"><div class="t"><h1 class="b1-h1">Wallet</h1><p class="b1-sub">Your balance covers about <b>116 approvals</b> at ₹1,580.</p></div></div>')
    page = f'<div class="b1-wrap tall v3k">{head}{hero}<div class="v3-wgrid">{ledger}<div class="v3-wside">{inv}{tds}</div></div></div>'
    return shell(NAV_WALLET, ["Lumen Labs", "Wallet"], page)

# ====================================================================== 7 · team and settings
ROLES = [("Owner", "Everything, and the only one who can hand the brand on."), ("Admin", "Everything: campaigns, money, people and settings."),
         ("Campaign manager", "Runs campaigns and listings, reviews work, answers disputes. Sees the wallet."),
         ("Finance manager", "Runs the wallet, withdrawals, invoices and bank accounts. Sees campaigns."), ("Viewer", "Sees everything, changes nothing.")]

def d_team():
    from kit5 import _mrow
    def mrow(photo, name, you, mail, role, seen):
        fixed = role == "Owner"
        ctl = f'<span class="chip">{role}</span>' if fixed else f'<span class="chip">{role}{ic("down", 14)}</span>'
        return (f'<div class="row v3-mem">{av("".join(w[0] for w in name.split()[:2]), photo, 40)}<div class="tx"><b>{name}{"<em>You</em>" if you else ""}</b><small>{mail}</small></div>'
                f'<div class="v3-rc">{ctl}</div><span class="v3-seen">{seen}</span></div>')
    members = "".join([mrow(2, "Neha Kapoor", True, "neha@lumenlabs.in", "Owner", "Active now"),
                       mrow(0, "Arjun Mehta", False, "arjun@lumenlabs.in", "Campaign manager", "Active today"),
                       mrow(3, "Divya Rao", False, "divya@lumenlabs.in", "Finance manager", "Active yesterday"),
                       mrow(1, "Sanjay Iyer", False, "sanjay@lumenlabs.in", "Viewer", "Active 3 days ago")])
    inv = (f'<div class="row v3-mem"><span class="x-tile">{ic("mail", 20)}</span><div class="tx"><b>aman@lumenlabs.in</b><small>Sent on WhatsApp · Expires in 7 days</small></div>'
           f'<div class="v3-rc"><span class="chip">Campaign manager</span></div><span class="v3-acts"><em>Resend</em><em>Cancel invite</em></span></div>')
    link = (f'<div class="panel v3-linkc"><div class="tx"><b>Invite link</b><small>Anyone with it joins as the role you pick.</small></div>'
            f'<span class="chip">Viewer{ic("down", 14)}</span><div class="input n-copy"><span class="n-val">hypedrive.in/join/lumen-labs</span><button class="btn s">{ic("copy", 16)}Copy invite link</button></div><em class="v3-lk">Turn off link</em></div>')
    rail_item = lambda i, t, on=False: f'<div class="b2-ri{" on" if on else ""}">{ics(i, 18) if on else ic(i, 18)}{t}</div>'
    rail = ('<div class="b2-rail"><div class="b2-rg">Workspace</div>' + rail_item("settings", "Workspace") + rail_item("users", "Team", True) + rail_item("receipt", "Tax")
            + rail_item("bank", "Bank account") + rail_item("bell", "Notifications") + '<div class="b2-rg">You</div>' + rail_item("user", "Profile") + rail_item("lock", "Security") + '</div>')
    head = (f'<div class="v3-head"><div class="t"><h1 class="b1-h1">Team</h1><p class="b1-sub">4 members and 1 invite waiting. Only an owner or admin manages people and settings.</p></div>'
            f'<button class="btn p sm">{ic("plus", 16)}Invite members</button></div>')
    roles = '<div class="mn-card mn-list">' + "".join(f'<div class="mn-row"><div class="mn-rt"><b>{r}</b><small>{d}</small></div></div>' for r, d in ROLES) + '</div>'
    sh = lambda t, n="": f'<div class="v3-sechd"><h2>{t}</h2><span>{n}</span></div>'
    main = (f'<div class="v3-tmain v3k">{head}{sh("Members")}'
            f'<div class="stack v3-mlist" style="gap:8px">{members}</div>{sh("Invites")}<div class="stack">{inv}</div>{link}{sh("Roles", "Pick one for each member and invite")}{roles}</div>')
    return shell(NAV_TEAM, ["Lumen Labs", "Team"], f'<div class="b2-split">{rail}{main}</div>')

SCREENS = [("Brand · Review queue", d_queue), ("Brand · Wallet", d_wallet), ("Brand · Team", d_team)]
