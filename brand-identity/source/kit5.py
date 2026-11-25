"""Domain components: money (wallet, withdraw, payout methods, PAN) from the real business logic."""
from uikit2 import *
from kit3 import sec, inr, g, gs, btn, field

def _b(tone, icon, text): return f'<span class="badge {tone}">{ics(icon, 13)}{text}</span>'
def _blk(title, body, cls=""): return f'<div class="mn-blk {cls}"><div class="lbl">{title}</div>{body}</div>'
def _tile(glyph): return f'<span class="x-tile mn-gl">{glyph}</span>'
def _note(tone, icon, title, detail="", action=""):
    d = f'<span class="mn-nd">{detail}</span>' if detail else ""
    a = f'<div class="mn-na">{action}</div>' if action else ""
    return f'<div class="mn-note {tone}">{ics(icon, 18)}<div class="mn-nt"><b>{title}</b>{d}</div>{a}</div>'

# ---------------------------------------------------------------- 1 wallet hero
def _hero(avail, hold, btn_html, extra="", neg=False):
    cls = "mn-hero neg" if neg else "mn-hero"
    return (f'<div class="{cls}"><div class="mn-hl">{"Balance" if neg else "Available"}</div>'
            f'<div class="mn-hn num">{avail}</div>{extra}'
            f'<a class="mn-hold">{hold}{ic("chev", 14)}</a><div class="mn-hb">{btn_html}</div></div>')

def _heroes():
    w = btn("p", "Withdraw")
    v = btn("p", "Verify PAN")
    n = btn("s dis", "Withdraw", extra=" disabled")
    return "".join([
        _blk("Wallet hero", _hero("₹6,820", "₹1,339 on hold", w)),
        _blk("PAN required", _hero("₹6,820", "₹1,339 on hold", v, f'<span class="mn-hs">Verify your PAN to withdraw.</span>')),
        _blk("Negative balance", _hero("−₹240", "₹1,339 on hold", n,
              f'<span class="mn-hs">You owe ₹240 from Glow serum; new cashback pays it off. Withdraw opens when it\'s back above zero.</span>', neg=True)),
    ])

# ---------------------------------------------------------------- 2 money states
def _states():
    items = [("Available to withdraw", "₹6,820", "Cashback that has reached your wallet and is ready to withdraw."),
             ("On hold", "₹1,339", "Cashback for your work in progress that the brand has already set aside. It moves to your balance when they approve it."),
             ("Pending approval", "₹2,450", "Cashback for your work in progress that the brand pays when they approve it."),
             ("Reserved", "₹4,000", "Money set aside for withdrawals in progress. It leaves your balance when the bank confirms."),
             ("Earned so far", "₹24,610", "All the cashback that has reached your wallet since you joined, after fees.")]
    cells = "".join(f'<div class="mn-sc{" last" if i == 4 else ""}"><span class="mn-sl">{l}</span><b class="mn-sv num">{v}</b><span class="mn-sh">{h}</span></div>' for i, (l, v, h) in enumerate(items))
    return f'<div class="mn-blk wide"><div class="lbl">Money states</div><div class="mn-card mn-strip">{cells}</div></div>'

# ---------------------------------------------------------------- 3 movements
def _mrow(glyph, title, sub, amt, state=None, out=False, sel=False):
    badge = {"progress": _b("info", "clock", "In progress"), "failed": _b("danger", "danger", "Failed"), "released": _b("neutral", "refresh", "Released")}.get(state, "")
    cls = "mn-amt out" if out else "mn-amt"
    if state in ("failed", "released"): cls += " off"
    return (f'<div class="mn-row{" sel" if sel else ""}">{_tile(ic(glyph, 18))}<div class="mn-rt"><b>{title}</b><small>{sub}</small></div>'
            f'{badge}<span class="{cls} num">{amt}</span></div>')

def _movements():
    rows = "".join([
        _mrow("rupee", "Cashback", "Glow serum · 18 Nov 2026", "+₹1,139"),
        _mrow("gift", "Bonus", "Glow serum · 18 Nov 2026", "+₹200"),
        _mrow("bank", "Withdrawal", "To HDFC ••6093 · 20 Nov 2026", "−₹4,000", "progress", True, sel=True),
        _mrow("users", "Referral", "Aarav joined · 12 Nov 2026", "+₹100"),
        _mrow("receipt", "Refund", "Night cream · 9 Nov 2026", "−₹990", "released", True),
        _mrow("sliders", "Adjustment", "Wallet correction · 2 Nov 2026", "+₹150"),
        _mrow("bank", "Withdrawal", "To HDFC ••6093 · 28 Oct 2026", "−₹2,000", "failed", True),
    ])
    chips = "".join(f'<span class="mn-chip{" on" if i == 0 else ""}">{t}</span>' for i, t in enumerate(["All", "Money in", "Money out", "On hold"]))
    states = "".join([_b("info", "clock", "In progress"), _b("neutral", "ok", "Done"), _b("danger", "danger", "Failed"), _b("neutral", "refresh", "Released")])
    left = (f'<div class="mn-chips">{chips}</div><div class="mn-card mn-list">{rows}</div>'
            f'<div class="mn-states"><span class="t-small muted">States</span>{states}</div>')
    def line(k, v, b=False): return f'<div class="mn-ln"><span>{k}</span><span class="num{" b" if b else ""}">{v}</span></div>'
    rcpt = (f'<div class="mn-card mn-rc"><div class="mn-rh">{_tile(ic("bank", 18))}<div class="mn-rt"><b>Withdrawal</b><small>20 Nov 2026, 4:19 pm</small></div>{_b("warning", "clock", "In review")}</div>'
            f'<div class="mn-rbig num">−₹12,000</div><p class="mn-rd">We check large or first withdrawals before sending. We\'ll notify you when it\'s reviewed.</p>'
            f'<div class="mn-lns">{line("To", f"HDFC ••6093")}{line("Fee", "₹0.00")}{line("You receive", "₹12,000.00", True)}{line("Arrives", "After a quick review")}{line("Reference", "WD-48213907")}</div>'
            f'<div class="mn-ra">{btn("s sm", "Share receipt")}{btn("s sm", "Cancel withdrawal")}</div></div>')
    return (f'<div class="mn-blk"><div class="lbl">Movement rows and filters</div>{left}</div>'
            f'<div class="mn-blk"><div class="lbl">Receipt detail</div>{rcpt}</div>')

# ---------------------------------------------------------------- 4 withdraw flow
def _panel(n, title, body, foot=""):
    f = f'<div class="mn-pf">{foot}</div>' if foot else ""
    return f'<div class="mn-card mn-panel"><div class="mn-ph"><span class="mn-step num">{n}</span><b>{title}</b></div><div class="mn-pb">{body}</div>{f}</div>'

def _flow():
    amount = (f'<div class="mn-amtf"><span class="mn-cur">₹</span><span class="mn-av num">4,000</span></div>'
              f'<span class="mn-help">Min ₹100 · max ₹50,000 · ₹6,820 available</span>')
    acct = ('<div class="mn-opt sel"><span class="radio on"></span>' + bank("hdfc", 24, True) + '<div class="mn-rt"><b>HDFC ••6093</b><small>Bank account</small></div></div>'
            '<div class="mn-opt"><span class="radio"></span>' + bank("upi-gpay", 24, True) + '<div class="mn-rt"><b>riya@okhdfcbank</b><small>UPI ID</small></div></div>')
    def rv(amt, arrives):
        return (f'<div class="mn-lns tight"><div class="mn-ln"><span>To</span><span>HDFC ••6093</span></div><div class="mn-ln"><span>Amount</span><span class="num">{amt}</span></div>'
                f'<div class="mn-ln"><span>Fee</span><span class="num">₹0.00</span></div><div class="mn-ln"><span>You receive</span><span class="num b">{amt}.00</span></div>'
                f'<div class="mn-ln"><span>Arrives</span><span>{arrives}</span></div></div>')
    confirm = (f'<p class="mn-p">Enter your authenticator code.</p><div class="mn-code">' + "".join(f'<i class="num">{d}</i>' for d in "48 21".replace(" ", "") ) + '<i></i><i class="cur"></i></div>')
    done = (f'<div class="mn-done">{ics("success", 28)}<b>Withdrawal requested</b><span>₹4,000 to HDFC ••6093</span><span class="mn-dm">Usually within minutes</span></div>')
    cont = btn("p", "Continue", extra="")
    P = [_panel(1, "Amount", amount, cont), _panel(2, "Choose account", acct, cont),
         _panel(3, "Review", rv("₹4,000", "Usually within minutes"), btn("p", "Withdraw ₹4,000")),
         _panel(3, "Review · ₹10,000 or more", rv("₹12,000", "After a quick review"), btn("p", "Send for review")),
         _panel(4, "Confirm it's you", confirm, btn("p", "Confirm")),
         _panel(5, "Requested", done, btn("s", "Done"))]
    return f'<div class="mn-blk wide"><div class="lbl">Withdraw flow</div><div class="mn-flow">{"".join(P)}</div></div>'

# ---------------------------------------------------------------- 5 statuses
def _statuses():
    S = [("info", "clock", "Requested", "We'll send it shortly."), ("warning", "eye", "In review", "We check large or first withdrawals before sending."),
         ("info", "send", "Sending", "With your bank now. Most arrive within minutes."), ("success", "success", "Paid out", "Sent to HDFC ••6093 on 20 Nov 2026."),
         ("danger", "danger", "Failed", "₹4,000 is back in your balance."), ("danger", "danger", "Declined", "₹4,000 is back in your balance."),
         ("neutral", "x", "Cancelled", "You cancelled this. The money is back in your balance."), ("danger", "danger", "Reversed", "Your bank returned this payment. The money is back in your balance."),
         ("warning", "warning", "Delayed", "Taking longer than usual. We're on it; no action needed.")]
    items = "".join(f'<div class="mn-st">{_b(t, i, l)}<span>{d}</span></div>' for t, i, l, d in S)
    return f'<div class="mn-blk wide"><div class="lbl">Withdrawal statuses</div><div class="mn-card mn-stl">{items}</div></div>'

# ---------------------------------------------------------------- 6 blockers
def _blockers():
    ns = [_note("warning", "clock", "Your payout method is cooling off. Ready to use in 23 h 14 min"),
          _note("neutral", "info", "Nothing to withdraw yet"),
          _note("info", "privacy", "Verify your PAN to withdraw", "Without it, you can withdraw ₹5,000 each time and ₹25,000 in 365 days.", btn("p sm", "Verify PAN")),
          _note("danger", "lock", "Your wallet is frozen", "Contact support to unfreeze it."),
          _note("warning", "pause", "Withdrawals are paused", "Try again later.")]
    cap = (f'<div class="mn-note warning">{ics("warning", 18)}<div class="mn-nt"><b>You are close to your yearly limit</b>'
           f'<span class="mn-nd">Without a verified PAN, withdrawals stop at ₹25,000 in 365 days.</span>'
           f'<div class="mn-bar"><i style="width:84%"></i></div><span class="mn-bm num">₹21,000 of ₹25,000</span></div><div class="mn-na">{btn("p sm", "Verify PAN")}</div></div>')
    return (f'<div class="mn-blk"><div class="lbl">Withdraw blockers</div><div class="mn-stack">{"".join(ns[:3])}</div></div>'
            f'<div class="mn-blk"><div class="lbl">&nbsp;</div><div class="mn-stack">{"".join(ns[3:])}{cap}</div></div>')

# ---------------------------------------------------------------- 7 payout methods
def _methods():
    def m(logo, t, s, badge=""): return f'<div class="mn-row">{logo}<div class="mn-rt"><b>{t}</b><small>{s}</small></div>{badge}<span class="mn-more">{ic("more", 18)}</span></div>'
    lst = ('<div class="mn-card mn-list">' +
           m(bank("hdfc", 24, True), "HDFC ••6093", "Salary account · HDFC0001234", '<span class="badge neutral">Default</span>') +
           m(bank("upi-gpay", 24, True), "riya@okhdfcbank", "Personal UPI", _b("warning", "clock", "Ready in 23 h 14 min")) + '</div>'
           '<p class="mn-cool">A new account can take withdrawals 24 hours after it\'s added.</p>')
    form = ('<div class="mn-card mn-form"><div class="mn-seg"><span class="on">Bank account</span><span>UPI ID</span></div>'
            + field("Account number", '<div class="input"><span class="ph">123456789012</span></div>')
            + field("IFSC", '<div class="input"><span class="ph">HDFC0001234</span></div>')
            + field("Nickname (optional)", '<div class="input"><span class="ph">Salary account</span></div>')
            + '<div class="mn-sw"><div class="mn-rt"><b>Make this my default</b><small>Withdrawals go here unless you choose another.</small></div><span class="mn-tg"><i></i></span></div>'
            + btn("p", "Add payout method") + '</div>')
    return f'<div class="mn-blk"><div class="lbl">Payout methods</div>{lst}<div class="lbl" style="margin-top:14px">Add a bank account</div>{form}</div>'

# ---------------------------------------------------------------- 8 PAN
def _pan():
    def card(tone, icon, state, title, body, action="", extra=""):
        a = f'<div class="mn-pa">{action}</div>' if action else ""
        return f'<div class="mn-card mn-pan"><div class="mn-pt">{_b(tone, icon, state)}</div><b>{title}</b><p>{body}</p>{extra}{a}</div>'
    cards = "".join([
        card("neutral", "info", "Not verified yet", "Verify your PAN", "Verifying your PAN lets you withdraw and raises your limits. Without it, you can withdraw ₹5,000 each time and ₹25,000 in 365 days.", btn("p sm", "Verify PAN")),
        card("warning", "clock", "In review", "Your PAN is in review.", "Under review. We'll notify you."),
        card("success", "success", "Verified", "Your PAN is verified.", "ABCDE••••F · valid until 20 Nov 2027. Withdrawals are uncapped."),
        card("warning", "warning", "Expired", "Your verified PAN has expired.", "Verify it again to go on.", btn("p sm", "Verify PAN again")),
        card("danger", "danger", "Didn't go through", "Your last attempt didn't go through", "We couldn't verify this PAN. Check the name and number against your PAN card and try again.", btn("s sm", "Try again")),
    ])
    form = ('<div class="mn-card mn-form">'
            + field("PAN", '<div class="input err"><span class="num">ABCDE12345</span></div>', "A PAN is five letters, four digits, then one letter.", err=True)
            + field("Name as printed on your PAN", '<div class="input"><span>Riya Sharma</span></div>', "Exactly as it's printed on the card.")
            + field("Date of birth", '<div class="input"><span class="num">14 Mar 1998</span></div>')
            + btn("p", "Verify your PAN") + '</div>')
    return f'<div class="mn-blk wide"><div class="lbl">PAN verification states</div><div class="mn-pans">{cards}</div></div>', _blk("Verify form", form)

# ---------------------------------------------------------------- 9 statements
def _statements():
    S = [("Nov 2026", "So far", "6 entries · ₹1,439 in"), ("Oct 2026", "", "11 entries · ₹3,410 in"), ("Sep 2026", "", "8 entries · ₹2,780 in"), ("FY 2025–26", "Whole year", "64 entries · ₹21,170 in")]
    rows = "".join(f'<div class="mn-row">{_tile(ic("calendar", 18))}<div class="mn-rt"><b>{t}{f"<span class=mn-so>{so}</span>" if so else ""}</b><small>{m}</small></div>{btn("s sm", ic("download", 16) + "Download")}</div>' for t, so, m in S)
    return _blk("Statements", f'<div class="mn-card mn-list">{rows}</div>')

def kit_money(theme):
    body = ('<div class="mn-grid3">' + _heroes() + '</div>' + '<div class="mn-grid1">' + _states() + '</div>'
            + '<div class="mn-grid2">' + _movements() + '</div>' + '<div class="mn-grid1">' + _flow() + '</div>'
            + '<div class="mn-grid1">' + _statuses() + '</div>' + '<div class="mn-grid2">' + _blockers() + '</div>'
            + '<div class="mn-grid1">' + _pan()[0] + '</div>' + '<div class="mn-grid2">' + _methods() + '<div class="mn-blk mn-stack2">' + _pan()[1] + _statements() + '</div></div>')
    return sec("Money", "Wallet and payouts, from the real product: the five money figures, movements, the withdraw flow, withdrawal statuses, blockers, payout methods, PAN and statements.", body, "mn-sec")
