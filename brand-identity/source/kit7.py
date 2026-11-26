"""Kit section: the current page patterns (v7, 2026-11-26). Live specimens of the classes the screens use (w5-*, m7-*, b7-*), not copies."""
from uikit2 import *
from kit4 import sec

def _ph(inner, w=358, canvas=False):
    """A frameless phone-width specimen, so the .phone-scoped rules apply exactly as on screens."""
    return (f'<div class="phone k7-ph" style="width:{w}px"><div class="scr k7-scr{" k7-cv" if canvas else ""}">'
            f'<div class="xm1-s w5 m7 k7-pg">{inner}</div></div></div>')

def kit_v7(theme="light"):
    AV = lambda k: f"{STOCK}/people/{k}.jpg"
    lk = lambda t: f'<em class="w5-lk">{t}</em>'
    row = lambda img, t, m, trail=None, cls="", rnd=False: (f'<div class="w5-row {cls}"><img{" class=m6-pa" if rnd else ""} src="{img}" alt=""><div class="tx"><b>{t}</b><small>{m}</small></div>'
                                                          + (ic("chev", 16) if trail is None else trail) + '</div>')
    lbl = lambda t: f'<div class="lbl">{t}</div>'
    money = (
        '<div class="grid g3 k7-g">'
        + '<div>' + lbl("Creator · blocked") + _ph('<div class="m7-money"><small>Available</small><b class="num">₹6,820</b><p><b class=num>₹1,339</b> on hold · <b class=num>₹24,610</b> earned so far</p>'
              f'<div class="m7-ft">{ics("privacy", 18, "var(--hd-accent)")}<span>Verify your PAN to withdraw</span>{lk("Verify")}</div></div>', canvas=True) + '</div>'
        + '<div>' + lbl("Mediator · withdraw") + _ph('<div class="m7-money"><small>You can withdraw</small><b class="num">₹3,240</b><p><b class=num>₹2,440</b> is held for paybacks</p>'
              f'<div class="m7-ft">{bank("hdfc", 20)}<span>To kavya@okhdfc</span><button class="btn p sm">Withdraw</button></div></div>', canvas=True) + '</div>'
        + '<div>' + lbl("Score with breakdown bar") + _ph(
              '<div class="m7-money m7-score"><small>Paid back on time</small><b class="num">95%</b><p><b class=num>38</b> of 40 shoppers</p><div class="m7-bar">'
              + "".join(f'<i style="flex:{n};background:{c}"></i>' for n, c in [(36, "var(--hd-success)"), (2, "var(--hd-accent)"), (1, "var(--hd-tone-marigold)"), (1, "var(--hd-danger)")])
              + '</div><div class="m7-leg">' + "".join(f'<span><i style="background:{c}"></i>{t} <b class="num">{n}</b></span>' for t, n, c in
                  [("Confirmed", 36, "var(--hd-success)"), ("In progress", 2, "var(--hd-accent)"), ("Partly paid", 1, "var(--hd-tone-marigold)"), ("Disputed", 1, "var(--hd-danger)")])
              + '</div></div>', canvas=True) + '</div></div>')
    rows = (
        '<div class="grid g2 k7-g"><div>' + lbl("Row cards · one style per list") + _ph(
            row(PH["serum"], "Glow serum, 30 ml", "Submit 2 tasks · due in 41 days")
            + row(PH["bottles"], "Daily cleanser trio", "<span class='warn'>Fix 1 task</span> · due in 6 days")
            + f'<div class="w5-row m7-due"><img class="m6-pa" src="{AV("women-65")}" alt=""><div class="tx"><b>Pay Asha ₹1,195</b><small>Glow serum · 20 Nov</small></div><button class="btn p sm">Mark paid</button></div>'
            + row(PH["cream"], "Night cream, 50 g", "5% · 4 shoppers", '<b class="num m6-amt">₹330</b>')
            + f'<div class="w5-row w5-task"><span class="x-tile w5-ti">{ics("star", 20, "var(--hd-tone-marigold)")}</span><div class="tx"><b>Calm otter</b><small>Rated you 5 stars · 18 Nov</small></div>{lk("Reply")}</div>', canvas=True)
        + '</div><div>' + lbl("Tabs · coloured icon, grey count, cobalt underline") + _ph(
            '<div class="tabs w5-tabs">' + "".join(f'<span{" class=on" if i == 0 else ""}>{ics(n, 16, c)}{t} <span class="tc">{k}</span></span>' for i, (n, c, t, k) in enumerate(
                [("grid", "var(--hd-accent)", "All", 8), ("clock", "var(--hd-tone-marigold)", "Ending soon", 2), ("spark", "var(--hd-info)", "New", 3)])) + '</div>')
        + lbl("Progress steps") + _ph('<div class="w5-steps">' + "".join(
            f'<div class="w5-st {k}"><i>{ics("check", 12, "#fff") if k == "done" else ""}</i><span>{t}</span></div>'
            for t, k in [("Joined", "done"), ("Bought", "done"), ("Tasks", "now"), ("Review", ""), ("Paid", "")]) + '</div>')
        + lbl("Money breakdown") + _ph('<div class="w5-sum k7-sum"><small>You get back</small><b class="num">₹1,339</b><dl><dt>Order on Nykaa</dt><dd>₹1,899</dd>'
            '<dt>Cashback, 60%</dt><dd class="in">₹1,139</dd><dt>Bonus</dt><dd class="in">₹200</dd></dl><p>Paid to your wallet when Lumen Labs approves</p></div>')
        + '</div></div>')
    media = (
        '<div class="grid g2 k7-g"><div>' + lbl("Featured photo card · one scrim") + _ph(
            f'<div class="w5-feat"><img src="{PH["flatlay"]}" alt=""><span class="w5-tag">{plat("nykaa", 13)}6 spots left</span>'
            '<div class="w5-ft"><small>Rose toner · Lumen Labs</small><b>Get ₹780 back</b><span>50% back + ₹150 bonus</span></div></div>')
        + '</div><div>' + lbl("Campaign photo card · desktop") + '<div class="bd2-camps k7-camps">'
        + f'<div class="bd2-camp b7-c"><div class="b7-ph"><img src="{PH["serum"]}" alt=""><span class="b7-tag">{ics("clock", 14, "var(--hd-tone-marigold)")}9 to review</span></div><div class="b"><span class="s">{plat("nykaa", 14)}Nykaa</span><b>Glow serum, 30 ml</b><div class="bar"><i style="width:93%"></i></div><small><span>112 of 120 creators</span><span class="warn">Ends in 6 days</span></small><small class="m">₹1,16,920 spent · 31 posts</small></div></div>'
        + f'<div class="bd2-camp b7-c"><div class="b7-ph"><div class="b7-noph">{ic("camera", 22)}<span>No photo yet</span></div></div><div class="b"><span class="s">{plat("nykaa", 14)}Nykaa</span><b>Vitamin C drops</b><div class="bar b7-nobar"></div><small><span>Draft</span><span>Edited 19 Nov</span></small><small class="m"><em class="b7-lk">Finish the draft</em></small></div></div>'
        + '</div></div></div>')
    return sec("Page patterns", "What every page is built from now. Money is one white card: label, one figure, one muted sentence, the action in its footer. Lists are separate row cards with one meta line. Status filters are underline tabs with coloured icons. Only exceptions get colour. No dark cards.",
               lbl("Money card") + money + rows + media)

K7 = """
.sec .phone.k7-ph { height: auto; padding: 0; border: 0; background: none; box-shadow: none; border-radius: 0 !important; max-width: 100%; }
.sec .phone.k7-ph .scr.k7-scr { position: static; height: auto; border-radius: 18px !important; overflow: hidden; background: var(--hd-surface); border: 1px solid var(--hd-edge); }
.sec .phone.k7-ph .scr.k7-cv { background: var(--hd-canvas); }
.sec .phone.k7-ph .k7-pg { padding: 16px; overflow: visible; }
.sec .phone.k7-ph .k7-pg > .m7-money:first-child, .sec .phone.k7-ph .k7-pg > .w5-sum:first-child { margin-top: 0; }
.sec .phone.k7-ph .k7-pg > .w5-sum { border-top: 0; padding-top: 0; }
.sec .phone.k7-ph .k7-pg > .w5-feat { margin-top: 0; }
.sec .phone.k7-ph .k7-pg > .w5-tabs { margin: 0 -16px; }
.sec .k7-g { gap: 20px; align-items: start; margin-bottom: 20px; }
.sec .k7-g .lbl { margin: 0 0 8px; } .sec .k7-g .phone + .lbl { margin-top: 18px; }
.sec .k7-camps { grid-template-columns: 1fr 1fr; }
"""
