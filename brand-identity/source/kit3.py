"""New kit sections: missing primitives and components (owned by the new-components agent).

Every component here is plain HTML + the XNEW CSS layer (`.n-*` classes). Surfaces reuse the kit's
`.card / .row / .menu / .dialog / .suggest / .btn` classes so squircle.js gives them the squircle + layered shadow.
"""
from uikit2 import *
import uikit as _u
import calendar as _cal

# ------------------------------------------------------------------ helpers
def sec(title, desc, body, cls=""):
    return f'<section class="sec nw {cls}"><h2>{title}</h2><p>{desc}</p>{body}</section>'
def lab(t): return f'<div class="lbl">{t[0].upper() + t[1:] if t[:2].islower() and not t.startswith("ios") else ("iOS" + t[3:] if t.startswith("ios") else t)}</div>'
def g(key, size=18, color=None, sw=None):
    """Nucleo UI Outline 18 by raw glyph key (for names that are not in NMAP yet)."""
    st = f' style="color:{color}"' if color else ""
    return f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 18 18" stroke-width="{sw or 1.5}"{st} aria-hidden="true">{NO[key + "Outline18"]}</svg>'
def gs(key, size=18, color=None):
    """Nucleo UI Fill 18 by raw glyph key."""
    st = f' style="color:{color}"' if color else ""
    return f'<svg class="ic icf" width="{size}" height="{size}" viewBox="0 0 18 18" fill="currentColor"{st} aria-hidden="true">{NF[key + "Fill18"]}</svg>'
def inr(n):
    s = str(int(abs(n))); head, tail = s[:-3], s[-3:]
    if head:
        parts = []
        while len(head) > 2: parts.insert(0, head[-2:]); head = head[:-2]
        if head: parts.insert(0, head)
        s = ",".join(parts) + "," + tail
    return ("−" if n < 0 else "") + "₹" + s
def illu(name, theme):
    return uri_file(os.path.join(B, "assets", "illustrations", f"hypedrive-ill-{name}-{theme}.svg"))
def pe(k): return f"{STOCK}/people/{k}.jpg"
def btn(cls, text, icon="", extra=""):
    return f'<button class="btn {cls}"{extra}>{icon}{text}</button>'
def ibtn(icon, label, cls="s", size=""):
    return f'<button class="btn {cls} icon {size}" aria-label="{label}">{icon}</button>'
def field(label, ctl, help_="", err=False, hint="", ok=False):
    h = f'<span class="help {"err" if err else "ok" if ok else ""}">{help_}</span>' if help_ else ""
    r = f'<div class="labrow"><label>{label}</label>{f"<span>{hint}</span>" if hint else ""}</div>'
    return f'<div class="field">{r}{ctl}{h}</div>'
def _grow(av_, k, n, sub, t): return f'<div class="row">{av(av_, k, 40)}<div class="tx"><b>{n}</b><small>{sub}</small></div><span class="t-cap muted num">{t}</span></div>'
GHOST_Q = ('<div class="n-ghost"><div class="n-gh1"><b class="t-h2">In review</b><span class="badge info">' + ics("clock", 13) + '23</span></div>'
           + _grow("RS", 0, "Riya Sharma", "Glow serum · 2 tasks", "2m") + _grow("AK", 1, "Arjun Kapoor", "Night cream · 2 tasks", "18m") + _grow("MJ", 2, "Meera Joshi", "Daily cleanser trio · 2 tasks", "1h") + _grow("TN", 3, "Tanvi Nair", "Glow serum · 2 tasks", "3h") + '</div>')
GHOST_D = (f'<div class="n-ghost"><div class="n-gh1"><b class="t-h2">Glow serum, 30 ml</b></div><img src="{PH["serum"]}" alt="">'
           f'<div class="n-gh2"><span class="n-brand">{av("LL", 2, 20)}<span>Lumen Labs</span>{vhex(13)}</span><b class="n-gr num">{"₹1,240"}</b></div>'
           f'<div class="tape n-t4"><i style="width:70%"></i></div><span class="t-small muted">36 of 120 slots left · ships from Kolkata</span></div>')
def kb(*keys): return "".join(kbd(k) for k in keys)
def stars(n, size=14):
    return '<span class="n-stars">' + "".join(ics("star", size, "var(--hd-star)") for _ in range(n)) + "</span>"

import os
B = _u.B
os_path = os.path

# ================================================================== 1 · FORM CONTROLS · FIELDS
def form_fields(theme):
    chev = f'<span class="trail n-chev">{ic("down", 18)}</span>'
    tick = f'<span class="n-tick">{ic("check", 16, sw=2.4)}</span>'

    # Select ---------------------------------------------------------------
    sel_closed = (field("Category", f'<div class="input n-sel"><span class="n-val">Skincare</span>{chev}</div>', "Pick the closest fit.")
                  + field("Store", f'<div class="input n-sel"><span class="n-val ph">Choose a store</span>{chev}</div>')
                  + field("Platform", f'<div class="input n-sel dis">{ic("lock", 18)}<span class="n-val">Instagram</span></div>', "Instagram is your only connected social."))
    opts = [("Skincare", True, False), ("Makeup", False, True), ("Haircare", False, False), ("Fashion", False, False), ("Home and kitchen", False, False)]
    sel_open = field("Category", f'<div class="n-pair"><div class="input n-sel foc"><span class="n-val">Skincare</span><span class="trail n-chev up">{ic("down", 18)}</span></div>'
        f'<div class="suggest n-list" role="listbox">' + "".join(f'<span class="n-opt {"on" if s else ""} {"hv" if h else ""}" role="option" aria-selected="{str(s).lower()}">{t}{tick if s else ""}</span>' for t, s, h in opts) + '</div></div>')

    # Combobox ---------------------------------------------------------------
    brands = [("LL", 2, "<mark>Lum</mark>en Labs", "8 open campaigns", True), ("LG", 1, "<mark>Lum</mark>ina Glow", "3 open campaigns", False), ("LS", 4, "<mark>Lum</mark>ière Skin", "1 open campaign", False)]
    combo = field("Brand", f'<div class="n-pair"><div class="input foc">{ic("search", 18)}<span class="n-q">lum<i class="n-caret"></i></span><span class="trail"><span class="n-clr">{ic("x", 11, sw=3)}</span></span></div>'
        f'<div class="suggest n-list" role="listbox"><span class="n-gh">Brands matching “lum”</span>' +
        "".join(f'<span class="n-opt {"hv" if h else ""}" role="option">{av(a, k, 28)}<span class="n-t">{n}</span><span class="n-sub">{s}</span></span>' for a, k, n, s, h in brands) + '</div></div>')

    # Multi-select ----------------------------------------------------------
    def tok(icon, t): return f'<span class="n-tok">{t}<button class="n-x" aria-label="Remove {t}">{ic("x", 12, sw=2.4)}</button></span>'
    ml = [("drop", "Skincare", True), ("lipstick", "Makeup", True), ("shirt", "Fashion", False), ("lamp", "Home", True)]
    multi = field("Categories", f'<div class="n-pair"><div class="input n-multi foc">{tok("drop", "Skincare")}{tok("lipstick", "Makeup")}{tok("lamp", "Home")}<span class="n-q"><i class="n-caret"></i></span></div>'
        f'<div class="suggest n-list" role="listbox" aria-multiselectable="true">' +
        "".join(f'<span class="n-opt {"hv" if t == "Fashion" else ""}" role="option"><span class="check {"on" if on else ""}">{ic("check", 14, sw=3) if on else ""}</span><span class="n-t">{t}</span></span>' for i, t, on in ml) + '</div></div>',
        hint="Up to 5")

    # Date ------------------------------------------------------------------
    first = _cal.monthrange(2026, 11)[0]  # Monday-first offset
    cells = ""
    for i in range(42):
        d = i - first + 1
        if d < 1: cells += f'<span class="mu"></span>'      # October
        elif d > 30: cells += f'<span class="mu"></span>'
        else:
            c = "off" if d < 20 else "td" if d == 20 else "sl" if d == 26 else "hv" if d == 24 else ""
            cells += f'<span class="{c}">{d}</span>'
    dw = "".join(f'<span class="dw">{x}</span>' for x in ("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"))
    date = field("Closes on", f'<div class="n-pair"><div class="input foc">{ic("calendar", 18)}<span class="n-val">26 Nov 2026</span><span class="trail t-small">in 6 days</span></div>'
        f'<div class="suggest n-cal"><div class="n-calh"><b>November 2026</b><span class="n-calnav">{ibtn(ic("back", 16), "Previous month", "g", "sm")}{ibtn(ic("chev", 16), "Next month", "g", "sm")}</span></div>'
        f'<div class="n-cg">{dw}{cells}</div></div></div>',
        "")

    # Number stepper --------------------------------------------------------
    def stepper(v, minus_dis=False, plus_dis=False, cls=""):
        return (f'<div class="n-step {cls}"><button aria-label="Decrease"{" disabled" if minus_dis else ""}>{ic("minus", 18)}</button><output class="num">{v}</output>'
                f'<button aria-label="Increase"{" disabled" if plus_dis else ""}>{ic("plus", 18)}</button></div>')
    step = (field("Spots", f'<div class="n-steprow">{stepper(120)}<span class="t-small muted">creators can join</span></div>', "Shown to creators only at 10 or fewer left.")
            + field("Tasks", f'<div class="n-steprow">{stepper(1, True)}<span class="t-small muted">at least one task</span></div>')
            + field("Screenshots per task", f'<div class="n-steprow">{stepper(6, False, True)}<span class="t-small muted">up to 6</span></div>'))

    A = f'<div class="box n-stage">{lab("select · closed")}{sel_closed}{lab("select · open")}{sel_open}</div>'
    Bx = f'<div class="box n-stage">{lab("combobox · typed query")}{combo}{lab("multi-select · removable tokens")}{multi}{lab("number stepper")}{step}</div>'
    Cx = f'<div class="box n-stage">{lab("date field · open picker")}{date}</div>'
    return sec("Form controls · fields", "Selection, a date and counts. Every open state shows the highlighted option, the selected one and the typed match.",
               f'<div class="grid g3 n-top">{A}{Bx}{Cx}</div>', "nw1")

# ================================================================== 2 · FORM CONTROLS · INPUT & UPLOAD
def form_inputs(theme):
    copy_idle = field("Your UPI ID", f'<div class="input n-copy">{bank("hdfc", 18)}<span class="n-id n-val">riya.sharma@okhdfcbank</span>{btn("s sm", "Copy", ic("copy", 16))}</div>', "Your withdrawals go to this ID.")
    copy_done = field("Your UPI ID · copied", f'<div class="input n-copy">{bank("hdfc", 18)}<span class="n-id n-val">riya.sharma@okhdfcbank</span>{btn("s sm n-done", "Copied", ic("check", 16, sw=2.4))}</div>', f'{ic("check", 14)}Copied to clipboard', ok=True)
    ref = field("Order number", f'<div class="input n-copy dis"><span class="n-id n-val">NYK-48210-93</span>{btn("g sm", "Copy", ic("copy", 16))}</div>')

    def ring(pct):
        c = 2 * 3.14159 * 31
        return (f'<svg class="n-ringo" viewBox="0 0 64 64" width="64" height="64" aria-hidden="true"><circle cx="32" cy="32" r="31" fill="none" stroke="var(--hd-track)" stroke-width="2"/>'
                f'<circle cx="32" cy="32" r="31" fill="none" stroke="var(--hd-accent)" stroke-width="2" stroke-linecap="round" stroke-dasharray="{c * pct / 100:.1f} {c:.1f}" transform="rotate(-90 32 32)"/></svg>')
    av_empty = (f'<div class="n-avu"><div class="n-av empty"><span class="n-ph">{ic("camera", 24)}</span></div><div class="n-avt"><b>Profile photo</b><span class="t-small muted">JPG or PNG, 400 × 400 or larger</span>'
                f'<div class="n-act">{btn("s sm", "Upload")}</div></div></div>')
    av_fill = (f'<div class="n-avu"><div class="n-av"><img src="{pe("women-68")}" alt="Riya Sharma"></div><div class="n-avt"><b>Riya Sharma</b><span class="t-small muted">riya-portrait.jpg · 1.4 MB</span>'
               f'<div class="n-act">{btn("s sm", "Change")}{btn("g sm", "Remove")}</div></div></div>')
    av_up = (f'<div class="n-avu"><div class="n-av up"><img src="{pe("women-68")}" alt="">{ring(64)}</div><div class="n-avt"><b>Uploading · 64%</b><span class="t-small muted num">riya-portrait.jpg · 0.9 of 1.4 MB</span>'
             f'<div class="n-act">{btn("g sm", "Cancel")}</div></div></div>')

    ty = lambda icon, t: f'<span class="n-ty">{icon}{t}</span>'
    types = ty(ic("play", 14), "MP4") + ty(ic("play", 14), "MOV") + ty(ic("clock", 14), "Up to 90 s") + ty(ic("file", 14), "200 MB")
    dz_idle = (f'<div class="u-dz"><span class="u-ic">{ic("upload", 20)}</span><div><b>Drop your receipt or invoice, or <u>browse</u></b><span>PDF, JPG or PNG</span></div></div>')
    dz_drag = (f'<div class="u-dz drag"><span class="u-ic">{ic("upload", 20)}</span><div><b>Release to upload</b><span>nykaa-receipt.pdf · 1.4 MB</span></div></div>')
    def frow(kind, name, meta, img, pct=0):
        thumb = f'<img class="u-th" src="{PH[img]}" alt="">'
        if kind == "err":
            end = f'{ibtn(ic("refresh", 16), "Choose another file", "g", "sm")}{ibtn(ic("x", 16), "Remove", "g", "sm")}'
            return f'<div class="u-row err">{thumb}<div class="u-tx"><b>{name}</b><span>{meta}</span></div>{end}</div>'
        if kind == "ok":
            return f'<div class="u-row">{thumb}<div class="u-tx"><b>{name}</b><span>{meta}</span></div><span class="u-ok">{ics("success", 18)}</span>{ibtn(ic("x", 16), "Remove", "g", "sm")}</div>'
        return (f'<div class="u-row go">{thumb}<div class="u-tx"><b>{name}</b><span class="num">{meta} · {pct}%</span></div>{ibtn(ic("x", 16), "Cancel", "g", "sm")}'
                f'<i class="u-bar" style="width:{pct}%"></i></div>')
    rows = ('<div class="u-list">' + frow("go", "reel-screenshot-1.png", "1.1 of 1.8 MB", "serum", 62) + frow("ok", "reel-screenshot-2.png", "0.9 MB", "bottles")
            + frow("err", "reel-screenshot-3.png", "Too large to upload. Choose another.", "cream") + '</div>')

    slider = (f'<div class="n-rngw"><div class="n-rhead"><b>Cashback</b><span class="num n-rv">40% – 70% back</span></div>'
              f'<div class="n-rng" style="--a:40%;--b:70%"><span class="tr"></span><span class="fill"></span><span class="th" style="--p:40%" role="slider" aria-valuenow="40"></span><span class="th" style="--p:70%" role="slider" aria-valuenow="70"></span></div>'
              f'<div class="n-rsc"><span>0%</span><span>100%</span></div>'
              f'<div class="n-rin"><div class="n-rf"><span class="n-rl">Min</span><div class="input"><span class="num">40%</span></div></div><span class="n-dash"></span><div class="n-rf"><span class="n-rl">Max</span><div class="input"><span class="num">70%</span></div></div></div></div>')

    tg1 = f'<span class="seg" role="tablist" aria-label="Layout"><span class="on" aria-label="Grid">{ics("grid", 18)}</span><span aria-label="List">{ic("list", 18)}</span></span>'
    tg2 = f'<span class="seg"><span class="on">Activity</span><span>Statements</span></span>'
    tg3 = (f'<span class="n-tgm" role="group" aria-label="Platforms"><span class="on">{soc("Instagram", 18)}Instagram</span><span class="on">{soc("Youtube", 18)}YouTube</span><span>{soc("Threads", 18)}Threads</span></span>')

    txt = "Used it every night for two weeks. Light, absorbs fast, and my skin feels calmer by the second week. The dropper leaks a little, but I would happily buy it again."
    ta_ok = field("Your Nykaa review", f'<div class="input textarea foc n-ta"><span>{txt}</span></div>', f'At least 40 words<span class="cnt num">46 words</span>', hint="Required")
    ta_err = field("Your Nykaa review · too short", f'<div class="input textarea err n-ta"><span>Used it every night for two weeks. Light and absorbs fast.</span></div>', f'Add at least 40 words to submit<span class="cnt num">11 / 40 words</span>', err=True)
    ta_dis = field("Describe the problem", f'<div class="input textarea n-ta"><span>My withdrawal to HDFC ••6093 has shown Requested for 3 days.</span></div>', f'Hypedrive support replies in the same thread<span class="cnt num">58 / 600</span>', hint="Raise a dispute")

    A = f'<div class="box n-stage">{lab("copy field · idle, copied, disabled")}{copy_idle}{copy_done}{ref}{lab("avatar upload · empty, set, uploading")}{av_empty}{av_fill}{av_up}{lab("toggle button group")}<div class="n-tgs">{tg2}</div>{tg3}</div>'
    Bx = f'<div class="box n-stage">{lab("receipt dropzone · idle")}{dz_idle}{lab("drag over")}{dz_drag}{lab("screenshot rows · uploading, done, error")}<div class="n-frs">{rows}</div></div>'
    Cx = (f'<div class="box n-stage">{lab("range slider · two thumbs")}{slider}'
          f'{lab("counted textarea · task text")}{ta_ok}{ta_err}{lab("counted textarea · dispute")}{ta_dis}</div>')

    # form section layout ------------------------------------------------------
    chev = f'<span class="trail n-chev">{ic("down", 18)}</span>'
    s1 = (f'<div class="n-fs"><div class="n-fsh"><h3 class="t-h3">Payout method</h3><p class="t-small muted">Where your withdrawals go. Brands never see these details.</p></div>'
          f'<div class="n-ff"><div class="n-fgrid">' + field("Account holder", f'<div class="input"><span>Riya Sharma</span></div>', "Exactly as on your bank account.", hint="Required") +
          field("UPI ID", f'<div class="input err"><span class="n-id">riya.sharma@okhdfc</span></div>', f'{ic("alert", 14)}We couldn’t find that UPI ID. Check the bank handle, like @okhdfcbank.', err=True, hint="Required") +
          field("Bank account", f'<div class="input dis">{bank("hdfc", 20)}<span class="n-val">HDFC ••6093</span><span class="trail"><span class="badge success">{ics("success", 13)}Verified</span></span></div>', "A new account can take withdrawals 24 hours after it’s added.") + '</div></div></div>')
    s2 = (f'<div class="n-fs"><div class="n-fsh"><h3 class="t-h3">Verify your PAN</h3><p class="t-small muted">Verify your PAN to withdraw. It also lifts the earnings cap.</p></div>'
          f'<div class="n-ff"><div class="n-fgrid">' + field("PAN", f'<div class="input"><span class="n-id">ABCDE1234F</span></div>', "Five letters, four digits, one letter.", hint="Optional") +
          field("Legal name", f'<div class="input dis"><span class="n-val">Riya Sharma</span></div>', "Verify your PAN to see your legal name here.") +
          field("Wallet and payouts", f'<div class="n-togl"><span class="switch on"></span><span class="t-body">Tell me when money lands</span></div>', "") + '</div></div></div>')
    form = (f'<div class="card n-form">{s1}{s2}<div class="n-ffoot"><span class="sp"></span>{btn("s", "Cancel")}{btn("p", "Save")}</div></div>')

    return sec("Form controls · input, upload and layout", "Copy, receipt and screenshot upload, a cashback range and counted text, plus the form section layout that holds them: label, help and error in one rhythm.",
               f'<div class="grid g3 n-top">{A}{Bx}{Cx}</div><div class="n-gap"></div>{lab("form section layout")}<div class="box">{form}</div>', "nw2")

# ================================================================== 3 · FLOW & NAVIGATION · STEPS AND OVERLAYS
def flow_a(theme):
    def hstep(steps, now):
        out = []
        for i, (t, s) in enumerate(steps):
            st = "done" if i < now else "now" if i == now else ""
            k = ic("check", 14, sw=2.6) if st == "done" else str(i + 1)
            ln = f'<i class="ln {"done" if i < now else ""}" aria-hidden="true"></i>' if i < len(steps) - 1 else ""
            out.append(f'<div class="s {st}" role="listitem"{" aria-current=\"step\"" if st == "now" else ""}><span class="n-sr1"><span class="k">{k}</span>{ln}</span><span class="n-st"><b>{t}</b><small>{s}</small></span></div>')
        return '<div class="n-wz" role="list">' + "".join(out) + '</div>'
    steps = [("Buy it", "On Nykaa"), ("Receipt", "Upload and check"), ("Join", "Join and earn ₹1,339")]
    wz_d = (f'<div class="card n-wzcard">{hstep(steps, 1)}</div>')
    wz_d2 = (f'<div class="card n-wzcard">{hstep(steps, 0)}</div>')

    def seg(n, now): return '<span class="n-sg">' + "".join(f'<i class="{"on" if i < now else "cur" if i == now else ""}"></i>' for i in range(n)) + '</span>'
    m1 = (f'<div class="n-dev n-wzm"><div class="n-wzt">{ibtn(ic("back", 20), "Back", "g", "icon")}<div><b>Receipt</b><small>Step 2 of 3</small></div><span class="n-skip"></span></div>{seg(3, 1)}</div>')
    m2 = (f'<div class="n-dev n-wzm"><div class="n-wzt">{ibtn(ic("back", 20), "Back", "g", "icon")}<div><b>Join</b><small>Step 3 of 3</small></div><span class="n-skip"></span></div>{seg(3, 2)}</div>')
    dots = (f'<div class="n-dev n-wzm"><div class="n-wzt">{ibtn(ic("x", 20), "Close", "g", "icon")}<div><b>Where should we send it?</b></div><span class="n-skip"></span></div>'
            f'<div class="n-dots2"><i class="on"></i><i class="cur"></i><i></i></div></div>')

    # command palette
    def ci(lead, label, sub="", tail="", hl=False): return f'<span class="n-ci {"hl" if hl else ""}">{lead}<span class="n-t">{label}</span>{f"<span class=n-sub>{sub}</span>" if sub else ""}{tail}</span>'
    cmd = (f'<div class="dialog n-cmd"><div class="n-cin">{ic("search", 20)}<span class="n-q">glow<i class="n-caret"></i></span>{kbd("esc")}</div>'
           f'<div class="n-tabs"><span class="on">All<b class="num">5</b></span><span>Campaigns<b class="num">3</b></span><span>Pages<b class="num">2</b></span></div>'
           f'<div class="n-cs"><span class="n-gh">Campaigns</span>'
           + ci(f'<img src="{PH["serum"]}" alt="">', "<b>Glow</b> serum, 30 ml", "Lumen Labs · Nykaa", f'<span class="n-go">Open {kbd("↵")}</span>', True)
           + ci(f'<img src="{PH["cream"]}" alt="">', "Night cream, 50 g", "Lumen Labs · Amazon")
           + ci(f'<img src="{PH["bottles"]}" alt="">', "Clear skin set", "Lumen Labs · Free product")
           + '<span class="n-gh">Pages</span>'
           + ci(ic("wallet", 20), "Wallet", "", f'<span class="n-k">{kb("G", "W")}</span>')
           + ci(ic("campaign", 20), "Enrollments", "", f'<span class="n-k">{kb("G", "E")}</span>')
           + f'</div><div class="n-cf"><span>{kb("↑", "↓")} move</span><span>{kb("↵")} open</span><span>{kb("esc")} close</span><span class="sp"></span><span>5 results</span></div></div>')

    pop = (f'<div class="n-anchor">{btn("s sm", "When do I get paid?", ic("info", 16))}<div class="dialog n-pop"><b>Right after the brand approves</b><p class="t-small muted">Approval is the payout: your cashback is credited to your wallet the moment the brand approves your tasks.</p>'
           f'<div class="n-popf"><a class="n-popl">How it works{ic("chev", 14)}</a><button class="btn s sm">Got it</button></div></div></div>')

    hover = (f'<div class="n-anchor"><span class="n-mention">Submitted by <u>@riya.glows</u></span><div class="dialog n-hc"><div class="n-hch"><img src="{pe("women-68")}" alt=""><div><b>Riya Sharma {vhex(14)}</b><span class="t-small muted">@riya.glows · Kolkata</span></div></div>'
             f'<p class="t-small">Honest skincare and everyday routines. Tests one product at a time.</p>'
             f'<div class="n-hcs"><div><b class="num">18.4k</b><span>{soc("Instagram", 14)}Instagram</span></div><div><b class="num">6</b><span>{ic("campaign", 14)}Enrollments</span></div></div>'
             f'<div class="n-act n-hca">{btn("s", "View enrollment")}</div></div></div>')

    return sec("Flow and navigation · steps, search and overlays", "The join steps for desktop and phone, the command palette, and the small floating surfaces that anchor to a trigger.",
        f'<div class="box n-stage">{lab("wizard stepper · desktop")}<div class="grid g2">{wz_d}{wz_d2}</div>{lab("wizard stepper · compact, mobile")}<div class="n-mrow">{m1}{m2}{dots}</div></div>'
        f'<div class="n-gap"></div><div class="grid n-g31"><div class="box n-stage n-center">{lab("command palette · ⌘K")}{cmd}</div>'
        f'<div class="box n-stage">{lab("popover")}{pop}{lab("hover card · creator")}{hover}</div></div>', "nw3")

# ================================================================== 4 · FLOW & NAVIGATION · MENUS, SHEETS, FILTERS
def flow_b(theme):
    mi = lambda icon, t, k="", cls="": f'<div class="{cls}">{icon}<span class="n-t">{t}</span>{k}</div>'
    ctx = (f'<div class="n-ctxw"><div class="menu n-ctx" role="menu">'
           + mi(gs("CircleCheck", 18, "var(--hd-success)") if False else ic("ok", 18), "Approve tasks", f'<span class="n-k">{kb("A")}</span>', "hl")
           + mi(ic("edit", 18), "Ask for fixes", f'<span class="n-k">{kb("F")}</span>')
           + mi(ic("link", 18), "Copy link", f'<span class="n-k">{kb("⌘", "C")}</span>')
           + '<i class="n-sep"></i>'
           + mi(ic("x", 18), "Not approve", f'<span class="n-k">{kb("Del")}</span>', "dg")
           + '</div></div>')

    def asr(icon, t, cls=""): return f'<span class="n-asa {cls}">{icon}<span>{t}</span></span>'
    asheet = (f'<div class="n-dev n-asd">{GHOST_Q}<div class="n-scrim"></div>'
              f'<div class="n-as"><div class="n-asg"><span class="n-ash"><span class="n-ast"><img src="{PH["serum"]}" alt=""><img class="n-asv" src="{pe("women-68")}" alt=""></span>'
              f'<span class="n-asx"><b>Riya Sharma’s tasks</b><small>Glow serum · {soc("Instagram", 13)}Instagram reel</small></span></span>'
              f'{asr(gs("CircleCheck", 18, "var(--hd-success)"), "Approve tasks")}{asr(ic("edit", 18), "Ask for fixes")}</div>'
              f'<div class="n-asg">{asr(ic("link", 18), "Copy link")}</div>'
              f'<div class="n-asg">{asr(gs("Flag3", 18, "var(--hd-danger)"), "Raise a dispute", "dg")}</div>'
              f'<div class="n-asg">{asr("", "Cancel", "cn")}</div><i class="n-hi"></i></div></div>')

    def chipt(icon, t, on=False): return f'<span class="chip {"on" if on else ""}">{icon}{t}</span>'
    fil = (f'<div class="card n-fil"><div class="n-filh"><b class="t-h3">Filters</b><span class="n-fc">3 applied</span><button class="btn link">Reset all</button></div>'
           f'<div class="n-fsec"><b>Category</b><div class="flexw">{chipt(ics("drop", 16), "Skincare", True)}{chipt(ics("lipstick", 16), "Makeup", True)}{chipt(ic("shirt", 16), "Fashion")}{chipt(ic("lamp", 16), "Home")}{chipt(ic("headphones", 16), "Gadgets")}</div></div>'
           f'<div class="n-fsec"><b>Platform</b><div class="flexw">{chipt(soc("Instagram", 16), "Instagram", True)}{chipt(soc("Youtube", 16), "YouTube")}{chipt(soc("Threads", 16), "Threads")}</div></div>'
           f'<div class="n-fsec"><b>Store</b><div class="flexw">{chipt("", "Nykaa", True)}{chipt("", "Amazon")}</div></div>'
           f'<div class="n-fsec"><div class="n-rhead"><b>Cashback</b><span class="num n-rv">40% – 70% back</span></div>'
           f'<div class="n-rng" style="--a:40%;--b:70%"><span class="tr"></span><span class="fill"></span><span class="th" style="--p:40%"></span><span class="th" style="--p:70%"></span></div><div class="n-rsc"><span>0%</span><span>100%</span></div></div>'
           f'<div class="n-filf">{btn("s", "Reset")}{btn("p", "Show 23 campaigns")}</div></div>')

    sopt = [("Cashback high to low", True), ("Newest first", False), ("Ending soon", False), ("Most spots left", False)]
    sort = (f'<div class="n-sortw"><button class="btn s sm n-sortb">{ic("sort", 16)}<span class="muted">Sort</span><b>Cashback high to low</b>{ic("down", 14)}</button><div class="menu n-sortm" role="menu"><span class="n-mh">Sort by</span>'
            + "".join(f'<div class="{"on" if s else ""}"><span class="n-t">{t}</span><span class="n-tk">{ic("check", 16, sw=2.4) if s else ""}</span></div>' for t, s in sopt) + '</div></div>')

    more = (f'<div class="n-more2"><div class="n-m2t"><span>Showing <b class="num">24</b> of <b class="num">118</b></span><i class="n-m2bar"><i style="width:20%"></i></i></div>{btn("s sm", "Load 24 more")}</div>')
    more2 = (f'<div class="n-more2"><div class="n-m2t"><span>Showing <b class="num">24</b> of <b class="num">118</b></span><i class="n-m2bar"><i style="width:20%"></i></i></div><button class="btn s sm" aria-busy="true"><span class="n-spin sm"></span>Loading</button></div>')
    more3 = (f'<div class="n-more2 done"><div class="n-m2t"><span>All <b class="num">118</b> campaigns shown</span><i class="n-m2bar"><i style="width:100%"></i></i></div><span class="n-end2">{ics("success", 16)}All caught up</span></div>')

    return sec("Flow and navigation · menus, sheets and filters", "The brand\u2019s review menu, the iOS action sheet, the creator filter panel, sort and load-more.",
        f'<div class="grid g3 n-top"><div class="box n-stage">{lab("review menu · destructive")}{ctx}{lab("sort menu")}{sort}</div>'
        f'<div class="box n-stage">{lab("filter panel")}{fil}</div>'
        f'<div class="box n-stage">{lab("iOS action sheet")}{asheet}</div></div><div class="n-gap"></div>'
        f'<div class="box n-stage">{lab("load more · idle, loading, done")}<div class="grid g3">{more}{more2}{more3}</div></div>', "nw4")

# ================================================================== 5 · FEEDBACK · LOADING, DIALOGS, ERRORS
def feedback_a(theme):
    spin = (f'<div class="n-spins"><div><span class="n-spin sm"></span><small>16</small></div><div><span class="n-spin"></span><small>24</small></div><div><span class="n-spin lg"></span><small>40</small></div></div>'
            f'<div class="flexw">{btn("p", "Sending application…", "", " aria-busy=\"true\"").replace("Sending application…", "<span class=\"spin\"></span>Sending application…")}{btn("s", "Saving", "", "").replace("Saving", "<span class=\"n-spin sm\"></span>Saving")}</div>')
    rows = (f'<div class="stack"><div class="row n-lr"><span class="n-spin"></span><div class="tx"><b>Checking your UPI ID</b><small>riya.sharma@okhdfcbank</small></div>{btn("s sm", "Cancel")}</div>'
            f'<div class="row n-lr"><span class="n-spin"></span><div class="tx"><b>Checking your receipt</b><small>This takes about 20 seconds.</small><div class="tape n-t4"><i style="width:55%"></i></div></div></div>'
            f'<div class="n-lmore"><span class="n-spin sm"></span><span class="t-small muted">Loading more campaigns…</span></div></div>')

    dlg = (f'<div class="dialog n-dlg2"><div class="d2b"><b class="d2t">Raise a dispute</b>'
           f'<p class="d2p"><b>Hypedrive support steps in.</b> Your payout stays as it is while we look.</p>'
           f'<label class="d2l">What went wrong?</label><div class="input foc d2i"><span>Problem with the payout</span></div></div>'
           f'<div class="d2f">{btn("s sm", "Cancel")}{btn("d sm", "Raise a dispute")}</div></div>')
    dlg2 = (f'<div class="dialog n-dlg2 sm"><div class="d2b"><b class="d2t">Ask for fixes?</b><p class="d2p"><b>Riya Sharma can fix and resubmit.</b> The status changes to Fix tasks.</p></div>'
            f'<div class="d2f">{btn("s sm", "Cancel")}{btn("p sm", "Ask for fixes")}</div></div>')

    err = (f'<div class="card n-state"><span class="x-tile n-errt">{ics("wifioff", 22)}</span><div class="t-h2">You’re offline</div>'
           f'<p class="n-errp">Check your connection and try again.</p><div class="n-errb">{btn("p", "Try again", ic("refresh", 18))}</div></div>')
    err2 = (f'<div class="card n-serr"><span class="x-tile n-errt">{ics("alert", 20)}</span><div><b>Couldn’t load your wallet</b><span>Check your connection and try again.</span></div>{btn("s sm", "Try again")}</div>')

    off = (f'<div class="n-bwrap"><div class="n-banner warn">{ics("wifioff", 18)}<b>You’re offline.</b><span class="n-bm">We’ll reconnect when you’re back.</span></div>'
           f'<div class="n-banner ok">{ics("success", 18)}<b>Back online.</b><span>Your changes are saved.</span><span class="sp"></span><button class="btn link">Dismiss</button></div></div>')

    skl = '<div class="stack">' + "".join(f'<div class="row"><span class="skel n-sk1"></span><div class="tx"><span class="skel n-sk2"></span><span class="skel n-sk3"></span></div><span class="skel n-sk4"></span></div>' for _ in range(3)) + '</div>'
    A = f'<div class="box n-stage">{lab("spinner · 16, 24, 40")}{spin}{lab("inline loading row")}{rows}{lab("skeleton rows · first load")}{skl}</div>'
    Bx = f'<div class="box n-stage n-center">{lab("dispute · describe the problem")}{dlg}{lab("confirm · one action")}{dlg2}{lab("offline banner")}<div class="n-wide">{off}</div></div>'
    Cx = f'<div class="box n-stage">{lab("error state · offline")}{err}{lab("error state · section")}{err2}</div>'
    return sec("Feedback and states · loading, dialogs and errors", "Loaders in three sizes, the dispute dialog, and the failure states a creator can hit.",
               f'<div class="grid g3 n-top">{A}{Bx}{Cx}</div>', "nw5")

# ================================================================== 6 · FEEDBACK · PAGES, INLINE EDIT, SUCCESS
def feedback_b(theme):
    def page(ill, title, body, btns, code=""):
        return (f'<div class="card n-page"><img src="{illu(ill, theme)}" alt=""><div class="t-h2">{title}</div><p class="t-body muted">{body}</p><div class="flexw n-c">{btns}</div>{f"<span class=n-code>{code}</span>" if code else ""}</div>')
    p404 = page("search", "Campaign not found", "This campaign may have ended, been removed, or the link is invalid.", btn("p", "View campaigns"))
    pinb = page("inbox", "Nothing to do right now", "We’ll tell you when there is.", btn("s", "Browse campaigns"))
    pbell = page("payout", "No activity yet", "Cashback and withdrawals show here once you have some.", btn("p", "Browse campaigns"))
    plock = page("lock", "Your account is on hold", "We paused your account. Your balance is safe, and you can still sign in and send an appeal.", btn("p", "Ask us to look again"))

    def blk(ic_, title, sub, act="", cls=""):
        return f'<div class="n-okrow">{f"<span class=x-tile>{ic_}</span>"}<div><b>{title}</b>{f"<span class=\"t-small muted\">{sub}</span>" if sub else ""}</div>{act}</div>'
    blocked = (blk(ics("alert", 20, "var(--hd-warning)"), "Verify your PAN to join", "", btn("p sm", "Verify PAN"))
               + blk(ics("alert", 20, "var(--hd-warning)"), "Complete your profile to join", "", btn("p sm", "Complete profile"))
               + blk(ics("lock", 20, "var(--hd-fg-muted)"), "This campaign isn’t taking creators right now", "", btn("s sm", "Browse")))
    filled = (f'<div class="notice warning">{icf("warning")}<span><b style="display:block">That version just filled up</b>Pick another version to join.</span></div>'
              f'<div class="notice info">{icf("info")}<span><b style="display:block">Opens 27 Nov</b>We’ll tell you when spots open.</span></div>')

    ok = (f'<div class="card n-page n-succ"><img src="{illu("approved", theme)}" alt=""><div class="t-h2">Tasks submitted</div><p class="t-body muted">Cashback is credited the moment the brand approves. We’ll tell you when they decide.</p>'
          f'<div class="n-sum"><span>Glow serum, 30 ml</span><b class="num">{inr(1339)}</b></div><div class="flexw n-c">{btn("p", "View enrollment")}{btn("s", "Browse campaigns")}</div></div>')
    ok3 = f'<div class="n-okrow"><span class="x-tile n-okt">{ics("success", 20)}</span><div><b>Application sent</b><span class="t-small muted">We’ll tell you when the brand decides.</span></div>{btn("s sm", "View")}</div>'
    ok2 = (f'<div class="n-okrow"><span class="x-tile n-okt">{ics("success", 20)}</span><div><b>Withdrawal requested</b><span class="t-small muted">{inr(6820)} to HDFC ••6093 · Usually within minutes</span></div>{btn("s sm", "Receipt")}</div>'
           f'<div class="n-okrow"><span class="x-tile n-okt">{ics("success", 20)}</span><div><b>Your receipt is verified</b><span class="t-small muted">It passed and is ready to join.</span></div></div>')

    return sec("Feedback and states · pages, blockers and success", "Every empty or missing page gets one isometric illustration, one sentence and one way forward. Blockers say what to fix.",
        f'<div class="grid n-g4"><div class="box">{lab("not found")}{p404}</div><div class="box">{lab("empty · home")}{pinb}</div><div class="box">{lab("empty · wallet")}{pbell}</div><div class="box">{lab("account on hold")}{plock}</div></div>'
        f'<div class="n-gap"></div><div class="grid g3 n-top"><div class="box n-stage">{lab("eligibility blockers · fix buttons")}<div class="stack">{blocked}</div>{lab("campaign state")}<div class="stack">{filled}</div></div>'
        f'<div class="box n-stage">{lab("success state")}{ok}</div><div class="box n-stage">{lab("success · inline")}<div class="stack">{ok2}{ok3}</div></div></div>', "nw6")

# ================================================================== 7 · CONTENT · CARDS AND MEDIA
def content_a(theme):
    def pcard(img, title, back, bonus, spots, badge, bcls, store, action, saved=False):
        meta = f'<b class="num">{back}</b>' + (f' · {bonus}' if bonus else "") + f' · {store}'
        return (f'<div class="card n-pc"><div class="n-ph"><img src="{PH[img]}" alt="{title}"><span class="badge {bcls} n-bd">{ics(badge[1], 13)}{badge[0]}</span><button class="n-disc" aria-label="Save">{ic("heart", 18)}</button></div>'
                f'<div class="n-pb"><span class="n-brand">Lumen Labs {vhex(12)}</span><b class="n-pt">{title}</b>'
                f'<span class="n-meta">{meta}</span>'
                + (f'<span class="n-meta">{spots}</span>' if spots else "") + f'{action}</div></div>')
    pv = (pcard("serum", "Glow serum, 30 ml", "60% back", "+₹200 bonus", "8 spots left", ("Closing soon", "clock"), "warning", "Nykaa", btn("p block", "Join campaign"))
          + pcard("cream", "Night cream, 50 g", "50% back", "", "", ("Open", "live"), "success", "Amazon", btn("p block", "Join campaign"))
          + pcard("bottles", "Daily cleanser trio", "55% back", "+₹100 bonus", "", ("Joined", "check"), "info", "Nykaa", btn("s block", "View enrollment")))

    def enr(img, title, status, bcls, bic, nxt, due, action=""):
        return (f'<div class="card n-pc"><div class="n-ph"><img src="{PH[img]}" alt="{title}"><span class="badge {bcls} n-bd">{ics(bic, 13)}{status}</span></div>'
                f'<div class="n-pb"><span class="n-brand">Lumen Labs {vhex(12)}</span><b class="n-pt">{title}</b>'
                f'<span class="n-meta"><b>{nxt}</b></span><span class="n-meta">{due}</span>{action}</div></div>')
    ev = (enr("serum", "Glow serum, 30 ml", "Submit tasks", "info", "clock", "Submit 2 tasks", "Due in 41 days", btn("p block", "Submit 2 tasks"))
          + enr("cream", "Night cream, 50 g", "In review", "warning", "clock", "The brand is reviewing your tasks", "We’ll tell you when they decide")
          + enr("bottles", "Daily cleanser trio", "Paid", "success", "success", "₹1,339 in your wallet", "Paid 18 Nov 2026"))

    def ph(img, title, line, spots, action):
        return (f'<div class="card n-ph2"><img src="{PH[img]}" alt="{title}"><div class="n-hb"><span class="n-hbr">Lumen Labs{vhex(13)}</span>'
                f'<b class="n-hpt">{title}</b><span class="n-hee">{line}</span><span class="n-hlf">{spots}</span></div>'
                f'<div class="n-he">{action}</div></div>')
    ph_ = (ph("serum", "Glow serum, 30 ml", '<b class="num">60% back</b> · +₹200 bonus', "8 spots left · closes 26 Nov 2026", btn("s sm", "Join"))
           + ph("bottles", "Daily cleanser trio", '<b class="num">55% back</b> · +₹100 bonus', "Closes 2 Dec 2026", btn("s sm", "Join")))
    eh = (ph("serum", "Glow serum, 30 ml", '<span class="badge info">Submit tasks</span>', "Due in 41 days", btn("p sm", "Submit 2 tasks"))
          + ph("cream", "Night cream, 50 g", '<span class="badge danger">Fix tasks</span>', "Fix 1 task · due in 3 days", btn("s sm", "Fix tasks")))

    return sec("Content · cards", "Campaign cards and enrollment cards. Photos sit bare inside the card; the only discs are over a photo. The spots line only shows at 10 or fewer.",
        f'<div class="box n-stage">{lab("campaign card · vertical")}<div class="n-trio">{pv}</div></div><div class="n-gap"></div>'
        f'<div class="box n-stage">{lab("enrollment card · vertical · status and next step")}<div class="n-trio">{ev}</div></div><div class="n-gap"></div>'
        f'<div class="grid g2 n-top"><div class="box n-stage">{lab("campaign card · horizontal")}{ph_}</div>'
        f'<div class="box n-stage">{lab("enrollment card · horizontal")}{eh}</div></div>', "nw7")


def content_b(theme):
    # ---- desktop product gallery: thumbnail rail + 4:5 hero --------------------------------
    gal = [("serum", "Glow serum, 30 ml on a stone surface"), ("cream", "Body lotion on linen"), ("flatlay", "Skincare flat lay"), ("bottles", "Cleanser bottles on a shelf")]
    def thumb(k, i, on):
        return f'<button class="m-th {"on" if on else ""}" aria-label="Photo {i + 1} of 4" aria-current="{str(on).lower()}"><img src="{PH[k]}" alt=""></button>'
    def dots(n, on): return '<span class="m-dots" aria-hidden="true">' + "".join(f'<i class="{"on" if i == on else ""}"></i>' for i in range(n)) + '</span>'
    hero = (f'<div class="m-hero"><img src="{PH["serum"]}" alt="{gal[0][1]}"><span class="m-chip num">1/4</span>'
            f''
            f'<button class="m-disc m-prev" aria-label="Previous photo" disabled>{ic("back", 18)}</button><button class="m-disc m-next" aria-label="Next photo">{ic("chev", 18)}</button></div>')
    desk = f'<div class="m-gal"><div class="m-rail">' + "".join(thumb(k, i, i == 0) for i, (k, _) in enumerate(gal)) + f'</div>{hero}</div>'

    # ---- mobile carousel with a peeking next slide, in a page ---------------------------------
    mob = (f'<div class="n-dev m-phone"><div class="m-top">{ibtn(ic("back", 20), "Back", "g", "icon")}<span class="sp"></span>{ibtn(ic("share", 20), "Share", "g", "icon")}</div>'
           f'<div class="m-track"><div class="m-slide"><img src="{PH["serum"]}" alt=""></div><div class="m-slide"><img src="{PH["cream"]}" alt=""></div></div>{dots(4, 0).replace("m-dots", "m-dots on-canvas")}'
           f'<div class="m-info"><b class="t-h2">Glow serum, 30 ml</b>'
           f'<div class="n-rw"><b class="num">60% back</b><span class="muted">+₹200 bonus</span></div></div></div>')
    ind = (f'<div class="m-inds"><div><span class="t-cap muted">Story bars</span><span class="m-bars"><i class="on"></i><i class="cur"></i><i></i><i></i></span></div>'
           f'<div><span class="t-cap muted">Counter only</span><span class="m-chip m-chip-s num">2/4</span></div></div>')

    # ---- task screenshots ---------------------------------------------------------------
    def shot(src, cap, task, pl, pos="50% 50%"):
        return (f'<div class="m-reelw"><div class="m-reel"><img class="m-ph" src="{src}" alt="" style="object-position:{pos}"><span class="m-pl">{soc(pl, 16)}</span>'
                f'<div class="m-meta"><b class="m-cap">{cap}</b><span class="m-views">{task}</span></div></div></div>')
    reels = "".join([
        shot(PH["serum"], "Screenshot 1", "Instagram reel", "Instagram", "56% 50%"),
        shot(PH["bottles"], "Screenshot 2", "Instagram reel", "Instagram", "72% 50%"),
        shot(PH["cream"], "Screenshot 1", "Nykaa review", "Instagram"),
        shot(PH["flatlay"], "Screenshot 3", "Instagram reel", "Instagram")])

    # ---- task rows -----------------------------------------------------------------------
    def lr(src, t, who, badge, bcls, bic):
        return (f'<div class="row m-lr"><span class="m-lt"><img src="{src}" alt=""></span><div class="tx"><b>{t}</b><small>{who}</small></div><span class="badge {bcls}">{ics(bic, 13)}{badge}</span></div>')
    lrs = (lr(PH["serum"], "Instagram reel", f'{soc("Instagram", 13)}Link and 2 screenshots', "In review", "warning", "clock")
           + lr(PH["cream"], "Nykaa review", "Link and 1 screenshot · at least 40 words", "Fix tasks", "danger", "alert"))

    # ---- review photo mosaic + upload tiles -------------------------------------------------
    mos = (f'<div class="m-mos"><img class="b" src="{PH["flatlay"]}" alt=""><img src="{PH["serum"]}" alt="" style="object-position:10% 40%">'
           f'<span class="m-last"><img src="{PH["bottles"]}" alt="" style="object-position:60% 50%"><span class="m-more">{btn("s sm", "Show all 6", ic("grid", 16))}</span></span></div>')
    def tile(kind, src="", name="", sz=""):
        if kind == "add": body = f'<span class="m-up add">{ic("plus", 22)}<small>Add photo</small></span>'
        elif kind == "ok": body = f'<span class="m-up"><img src="{src}" alt=""><span class="m-ok">{ics("success", 18)}</span></span>'
        elif kind == "go":
            c = 2 * 3.14159 * 18
            body = (f'<span class="m-up"><img src="{src}" alt=""><span class="m-dim"><svg width="44" height="44" viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="18" fill="none" stroke="currentColor" stroke-opacity=".3" stroke-width="2"/>'
                    f'<circle cx="22" cy="22" r="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-dasharray="{c * .64:.1f} {c:.1f}" transform="rotate(-90 22 22)"/></svg><b class="num">64%</b></span></span>')
        else: body = f'<span class="m-up err">{ics("alert", 22)}<b>Too large</b><button class="btn link">Retry</button></span>'
        return f'<div class="m-tile">{body}<span class="m-fn">{name or "&nbsp;"}</span></div>'
    ups = (f'<div class="m-ups">{tile("ok", PH["serum"], "screenshot-1.png · 1.2 MB")}{tile("go", PH["cream"], "screenshot-2.png · 0.8 MB")}{tile("err", "", "screenshot-3.png · 14 MB")}</div>')

    fk = ["serum", "cream", "flatlay", "bottles"]
    frames = '<div class="m-frames">' + "".join(f'<button class="{"on" if i == 2 else ""}" aria-label="Frame {i + 1}"><img src="{PH[k]}" alt=""{"" }>{"<span class=m-cv>Cover</span>" if i == 2 else ""}</button>' for i, k in enumerate(fk)) + '</div>'
    return sec("Content · media", "Campaign photos and task screenshots. Photos are edge to edge with a crisp 1px border; controls sit on the photo as discs.",
        f'<div class="grid m-g2 n-top"><div class="box n-stage">{lab("campaign gallery · desktop, 4:5 hero")}{desk}</div>'
        f'<div class="box n-stage">{lab("image carousel · mobile, peeking next slide")}{mob}</div></div><div class="n-gap"></div>'
        f'<div class="box n-stage">{lab("task screenshots · 1 to 6 per task")}<div class="m-reels">{reels}</div></div><div class="n-gap"></div>'
        f'<div class="grid g2 n-top"><div class="box n-stage">{lab("tasks in an enrollment")}<div class="stack">{lrs}</div></div>'
        f'<div class="box n-stage">{lab("screenshot set")}{mos}{lab("upload previews · done, uploading, failed")}{ups}</div></div>', "nw8")


def content_c(theme):
    # message thread
    def msg(side, inner, last=False, meta=""):
        who = f'<span class="t-av"><span class="t-lg">HS</span></span>' if side == "in" and last else (f'<span class="t-av"></span>' if side == "in" else "")
        return f'<div class="t-m {side}{" last" if last else ""}{" hm" if meta else ""}">{who}<div class="t-c">{inner}{f"<span class=t-meta>{meta}</span>" if meta else ""}</div></div>'
    bubble = lambda s: f'<p class="t-b">{s}</p>'
    pdf = f'<div class="t-file"><span class="t-ft">{ic("file", 18)}</span><div><b>wallet-screenshot.png</b><span>PNG · 0.8 MB</span></div><span class="t-dl" aria-label="Download">{ic("download", 16)}</span></div>'
    def comp(txt=""):
        f_ = f'<span class="t-txt">{txt}</span>' if txt else '<span class="ph">Message Hypedrive support</span>'
        dis = "" if txt else " disabled"
        return (f'<div class="t-comp"><div class="t-field{" on" if txt else ""}"><button class="t-ib" aria-label="Attach">{ic("clip", 18)}</button>{f_}</div>'
                f'<button class="btn p icon t-send" aria-label="Send"{dis}>{ics("send", 20)}</button></div>')
    thread = (f'<div class="card t-thr"><div class="t-head"><span class="t-lg lg">HS</span><div><b>Problem with the payout</b><span>Dispute · Hypedrive support</span></div>'
              f'</div>'
              f'<div class="t-body"><span class="t-day">Today</span>'
              + msg("out", bubble("My withdrawal of ₹6,820 to HDFC ••6093 has shown Requested for 3 days."), True, "10:42 am")
              + msg("in", bubble("Hi Riya, I’m looking into it. Can you share a screenshot of your wallet?"), True, "10:50 am")
              + msg("out", pdf)
              + msg("in", bubble("Thanks. That account was added less than 24 hours before the withdrawal, so it was held. It’s released now."), True, "10:58 am")
              + msg("out", bubble("It just landed. Thank you!"), True, f'11:05 am · <span class="t-rd">{ic("check", 12, sw=2.6)}Read</span>')
              + '<div class="t-m in last"><span class="t-av"><span class="t-lg">HS</span></span><div class="t-c"><p class="t-b t-typ" aria-label="Support is typing"><i></i><i></i><i></i></p></div></div>'
              + f'</div>' + comp() + '</div>')

    dl = [("You paid", "₹1,899"), ("Cashback", "₹1,139"), ("Bonus", "+₹200"), ("You get", f'<b class="num">₹1,339</b>')]
    dl_h = '<dl class="n-dl">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in dl) + '</dl>'
    
    PEOPLE = {p: f"{STOCK}/people/{p}.jpg" for p in ("women-68", "women-44", "men-12")}
    dv = (f'<div class="n-dvx">'
          f'<div class="n-dvc"><span class="n-dvt">Inset · settings list</span><div class="n-dvl">'
          + "".join(f'<div class="n-dvi">{ic(i, 20)}<b>{t}</b><span class="m">{m}</span>{ic("chev", 16)}</div>' for i, t, m in (("user", "Personal info", ""), ("bank", "Payout methods", "HDFC ••6093"), ("bell", "Notifications", "On"))) +
          f'</div></div>'
          f'<div class="n-dvc"><span class="n-dvt">Labelled · sign in</span><div class="n-dvsign"><button class="btn p block">{ic("phone", 18)}Continue with phone</button><div class="n-hrl"><i></i><span>or</span><i></i></div><button class="btn s block">{ic("mail", 18)}Continue with email</button></div></div>'
          f'<div class="n-dvc"><span class="n-dvt">Section label · wallet activity</span><div class="n-dvfeed"><div class="n-hrl left"><span>Today</span><i></i></div>'
          f'<div class="n-dvr"><b>Cashback</b><span class="num">+₹1,339</span></div><div class="n-hrl left"><span>Earlier this week</span><i></i></div>'
          f'<div class="n-dvr"><b>Withdrawal</b><span class="m">−₹2,000</span></div><div class="n-dvr"><b>On hold</b><span class="m">₹1,339</span></div></div></div>'
          f'<div class="n-dvc"><span class="n-dvt">Inline vertical · creator</span><div class="n-dvprof"><img src="{PEOPLE["women-68"]}" alt=""><div><b>Riya Sharma {vhex(14)}</b>'
          f'<div class="n-vrow"><span><b class="num">18.4k</b> on Instagram</span><i class="n-vr"></i><span><b class="num">6</b> enrollments</span></div></div></div>'
          f'<span class="n-dvt" style="margin-top:14px">Section break · sheet</span><div class="n-dvbreak"><div class="n-dvr"><b>Glow serum, 30 ml</b><span class="m">Lumen Labs</span></div><div class="n-band2"></div><div class="n-dvr"><b>Ship to</b><span class="m">14 Park Street, Kolkata</span></div></div></div>'
          f'</div>')

    swipe = (f'<div class="n-dev n-sw"><div class="n-swr"><div class="n-swa l"><span class="a ok">{ic("check", 20, sw=2.4)}Mark read</span></div><div class="row n-sr off"><img class="n-swp" src="{PH["bottles"]}" alt=""><div class="tx"><b>Your earnings have landed</b><small>Daily cleanser trio</small></div><span class="t-cap muted num">2m</span></div></div>'
             f'<div class="n-swr"><div class="n-swa r"><span class="a mu">{ic("archive", 20)}Archive</span></div><div class="row n-sr left"><img class="n-swp" src="{PH["cream"]}" alt=""><div class="tx"><b>Your enrollment needs a change</b><small>Night cream</small></div><span class="t-cap muted num">18m</span></div></div>'
             f'<div class="n-swr"><div class="row n-sr"><img class="n-swp" src="{PH["serum"]}" alt=""><div class="tx"><b>Glow serum is open</b><small>Lumen Labs · Nykaa</small></div><span class="t-cap muted num">1h</span></div></div></div>')

    apps = [("Whatsapp", "WhatsApp"), ("Instagram", "Instagram"), ("Threads", "Threads"), ("Facebook", "Facebook"), ("XTwitter", "X")]
    share = (f'<div class="n-dev n-shd n-shclean"><div class="sheet n-shs"><div class="grab"></div><div class="n-shh"><div class="t-h2">Share campaign</div><span class="x-disc n-shx" aria-label="Close">{ic("x", 16)}</span></div>'
             f'<div class="n-shp"><img src="{PH["serum"]}" alt=""><div><b>Glow serum, 30 ml</b><span class="t-small muted">hypedrive.in/c/glow-serum</span></div></div>'
             f'<div class="n-apps">' + "".join(f'<div><span class="n-app">{soc(k, 26)}</span><small>{n}</small></div>' for k, n in apps) + '</div>'
             f'<div class="group n-shg"><div class="gi">{ic("link", 20)}<b>Copy link</b></div><div class="gi">{ic("more", 20)}<b>More options</b></div></div></div></div>')

    ea = (f'<div class="card n-ea n-ea3"><img src="{illu("bag", theme)}" alt=""><div class="t-h2">No enrollments yet</div><p class="n-eap">Join a campaign, send your tasks, and get cashback once the brand approves.</p>'
          f'<ol class="n-steps3"><li><i>1</i><span>Join a campaign</span></li><li><i>2</i><span>Send your tasks</span></li><li><i>3</i><span>Get cashback</span></li></ol>'
          f'<div class="n-eab">{btn("p", "Browse campaigns", ic("search", 18))}</div></div>')
    ea2 = (f'<div class="n-ea2"><span class="n-eai">{ic("heart", 22)}</span><div><b>No saved campaigns</b><span class="t-small muted">Tap the heart on a campaign to keep it here.</span></div>{btn("s sm", "Browse campaigns")}</div>'
           f'<div class="n-ea2"><span class="n-eai">{ic("search", 22)}</span><div><b>No campaigns found</b><span class="t-small muted">Nothing matches “glo”. Try a different search.</span></div>{btn("s sm", "Clear search")}</div>')

    return sec("Content · conversation and lists", "A support thread for a dispute, key–value lists, dividers, swipe actions, the share sheet and empty cards with a next step.",
        f'<div class="grid n-g31"><div class="box n-stage">{lab("dispute thread · Hypedrive support")}{thread}</div>'
        f'<div class="box n-stage">{lab("description list · enrollment money")}<div class="card n-dlc t-ctxcard"><div class="t-ch"><img src="{PH["serum"]}" alt=""><div><b>Glow serum, 30 ml</b><span>Lumen Labs · Nykaa</span></div><span class="badge warning">In review</span></div>{dl_h}</div>{lab("composer · empty, send disabled")}<div class="card t-ctxcard t-comps">{comp()}</div>{lab("composer · typed, send enabled")}<div class="card t-ctxcard t-comps">{comp("It just landed. Thank you!")}</div></div></div>'
        f'<div class="n-gap"></div><div class="grid g2 n-top"><div class="n-col"><div class="box n-stage">{lab("divider variants")}{dv}</div><div class="box n-stage">{lab("swipe actions · inbox")}{swipe}</div></div>'
        f'<div class="box n-stage">{lab("share sheet")}{share}</div></div>'
        f'<div class="n-gap"></div><div class="grid g2 n-top"><div class="box n-stage">{lab("empty with action · card")}{ea}</div><div class="box n-stage">{lab("empty with action · compact")}<div class="stack">{ea2}</div></div></div>', "nw9")


def kit_new(theme="light"):
    return "".join([form_fields(theme), form_inputs(theme), flow_a(theme), flow_b(theme), feedback_a(theme), feedback_b(theme), content_a(theme), content_b(theme), content_c(theme)])
