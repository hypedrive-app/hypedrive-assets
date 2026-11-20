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
GHOST_Q = ('<div class="n-ghost"><div class="n-gh1"><b class="t-h2">Reviews to check</b><span class="badge info">' + ics("clock", 13) + '23</span></div>'
           + _grow("RS", 0, "Riya Sharma", "Glow serum · reel", "2m") + _grow("AK", 1, "Arjun Kapoor", "Night cream · story", "18m") + _grow("MJ", 2, "Meera Joshi", "Clear skin set · reel", "1h") + _grow("TN", 3, "Tanvi Nair", "Glow serum · short", "3h") + '</div>')
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
    sel_closed = (field("Category", f'<div class="input n-sel"><span class="n-val">Skincare</span>{chev}</div>', "Pick the closest fit. You can change it later.")
                  + field("Ships from", f'<div class="input n-sel"><span class="n-val ph">Choose a city</span>{chev}</div>')
                  + field("Payout day", f'<div class="input n-sel dis">{ic("lock", 18)}<span class="n-val">Every Monday</span></div>', "Set by your plan."))
    opts = [("Skincare", True, False), ("Makeup", False, True), ("Haircare", False, False), ("Fashion", False, False), ("Home and kitchen", False, False)]
    sel_open = field("Category", f'<div class="n-pair"><div class="input n-sel foc"><span class="n-val">Skincare</span><span class="trail n-chev up">{ic("down", 18)}</span></div>'
        f'<div class="suggest n-list" role="listbox">' + "".join(f'<span class="n-opt {"on" if s else ""} {"hv" if h else ""}" role="option" aria-selected="{str(s).lower()}">{t}{tick if s else ""}</span>' for t, s, h in opts) + '</div></div>')

    # Combobox ---------------------------------------------------------------
    brands = [("LL", 2, "<mark>Lum</mark>en Labs", "8 live drops", True), ("LG", 1, "<mark>Lum</mark>ina Glow", "3 live drops", False), ("PL", 4, "Co<mark>lum</mark>bia Naturals", "1 live drop", False)]
    combo = field("Brand", f'<div class="n-pair"><div class="input foc">{ic("search", 18)}<span class="n-q">lum<i class="n-caret"></i></span><span class="trail"><span class="n-clr">{ic("x", 11, sw=3)}</span></span></div>'
        f'<div class="suggest n-list" role="listbox"><span class="n-gh">Brands matching “lum”</span>' +
        "".join(f'<span class="n-opt {"hv" if h else ""}" role="option">{av(a, k, 28)}<span class="n-t">{n}</span><span class="n-sub">{s}</span></span>' for a, k, n, s, h in brands) +
        f'<span class="n-sep"></span><span class="n-opt n-new">{ic("plus", 18)}<span class="n-t">Invite “lum” by email</span></span></div></div>')

    # Multi-select ----------------------------------------------------------
    def tok(icon, t): return f'<span class="n-tok">{ic(icon, 14)}{t}<button class="n-x" aria-label="Remove {t}">{ic("x", 12, sw=2.4)}</button></span>'
    ml = [("drop", "Skincare", True), ("lipstick", "Makeup", True), ("shirt", "Fashion", False), ("lamp", "Home", True)]
    multi = field("Categories you review", f'<div class="n-pair"><div class="input n-multi foc">{tok("drop", "Skincare")}{tok("lipstick", "Makeup")}{tok("lamp", "Home")}<span class="n-q"><i class="n-caret"></i></span></div>'
        f'<div class="suggest n-list" role="listbox" aria-multiselectable="true">' +
        "".join(f'<span class="n-opt {"hv" if t == "Fashion" else ""}" role="option"><span class="check {"on" if on else ""}">{ic("check", 14, sw=3) if on else ""}</span>{ic(i, 18)}<span class="n-t">{t}</span></span>' for i, t, on in ml) + '</div></div>',
        "Choose up to 5. Brands match you by these.")

    # Date ------------------------------------------------------------------
    first = _cal.monthrange(2026, 11)[0]  # Monday-first offset
    cells = ""
    for i in range(42):
        d = i - first + 1
        if d < 1: cells += f'<span class="mu">{31 + d}</span>'      # October
        elif d > 30: cells += f'<span class="mu">{d - 30}</span>'
        else:
            c = "off" if d < 20 else "td" if d == 20 else "sl" if d == 27 else "hv" if d == 24 else ""
            cells += f'<span class="{c}">{d}</span>'
    dw = "".join(f'<span class="dw">{x}</span>' for x in ("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"))
    date = field("Post by", f'<div class="n-pair"><div class="input foc">{ic("calendar", 18)}<span class="n-val">Fri, Nov 27</span><span class="trail t-small">in 7 days</span></div>'
        f'<div class="suggest n-cal"><div class="n-calh">{ibtn(ic("back", 16), "Previous month", "g", "sm")}<b>November 2026</b>{ibtn(ic("chev", 16), "Next month", "g", "sm")}</div>'
        f'<div class="n-cg">{dw}{cells}</div><div class="n-calf"><button class="btn g sm">Clear</button><button class="btn s sm">Today</button></div></div></div>',
        "")

    # Time ------------------------------------------------------------------
    slots = [("10:00 am", False), ("10:30 am", False), ("11:00 am", True), ("11:30 am", False)]
    time_ = (field("Pickup time", f'<div class="input n-time">{ic("clock", 18)}<span class="n-seg">04</span><span class="n-colon">:</span><span class="n-seg">30</span><span class="n-seg">pm</span></div>', "Courier arrives within the hour.")
             + field("Pickup time · editing minutes", f'<div class="input n-time foc">{ic("clock", 18)}<span class="n-seg">04</span><span class="n-colon">:</span><span class="n-seg on">30</span><span class="n-seg">pm</span></div>')
    )
    slot = (field("Slot", f'<div class="n-pair"><div class="input n-sel foc">{ic("clock", 18)}<span class="n-val">11:00 am</span><span class="trail n-chev up">{ic("down", 18)}</span></div>'
                     f'<div class="suggest n-list">' + "".join(f'<span class="n-opt {"on" if s else ""}">{t}{tick if s else ""}</span>' for t, s in slots) + '</div></div>'))

    # Number stepper --------------------------------------------------------
    def stepper(v, minus_dis=False, plus_dis=False, cls=""):
        return (f'<div class="n-step {cls}"><button aria-label="Decrease"{" disabled" if minus_dis else ""}>{ic("minus", 18)}</button><output class="num">{v}</output>'
                f'<button aria-label="Increase"{" disabled" if plus_dis else ""}>{ic("plus", 18)}</button></div>')
    step = (field("Units to send", f'<div class="n-steprow">{stepper(3)}<span class="t-small muted">units · {inr(3 * 620)} product value</span></div>', "Up to 5 per creator.")
            + field("Slots", f'<div class="n-steprow">{stepper(1, True)}<span class="t-small muted">minimum reached</span></div>')
            + field("Creators per week", f'<div class="n-steprow">{stepper(20, False, True)}<span class="t-small muted">plan limit</span></div>')
            + f'<div>{lab("compact")}<div class="n-steprow">{stepper(2, cls="sm")}{stepper(10, cls="sm")}</div></div>')

    A = f'<div class="box n-stage">{lab("select · closed")}{sel_closed}{lab("select · open")}{sel_open}{lab("number stepper")}{step}</div>'
    Bx = f'<div class="box n-stage">{lab("combobox · typed query")}{combo}{lab("multi-select · removable tokens")}{multi}{lab("time field")}{time_}</div>'
    Cx = f'<div class="box n-stage">{lab("date field · open picker")}{date}{lab("time field · slot list")}{slot}</div>'
    return sec("Form controls · fields", "Selection, dates and numbers. Every open state shows the highlighted option, the selected one and the typed match.",
               f'<div class="grid g3 n-top">{A}{Bx}{Cx}</div>', "nw1")

# ================================================================== 2 · FORM CONTROLS · INPUT & UPLOAD
def form_inputs(theme):
    copy_idle = field("Your UPI ID", f'<div class="input n-copy"><span class="n-id n-val">riya.sharma@okhdfcbank</span>{btn("s sm", "Copy", ic("copy", 16))}</div>', "Brands pay straight to this ID.")
    copy_done = field("Your UPI ID · copied", f'<div class="input n-copy"><span class="n-id n-val">riya.sharma@okhdfcbank</span>{btn("s sm n-done", "Copied", ic("check", 16, sw=2.4))}</div>', f'{ic("check", 14)}Copied to clipboard', ok=True)
    ref = field("Order reference", f'<div class="input n-copy dis"><span class="n-id n-val">HD-48210-GLOW</span>{btn("g sm", "Copy", ic("copy", 16))}</div>')

    def ring(pct):
        c = 2 * 3.14159 * 38
        return (f'<svg class="n-ringo" viewBox="0 0 84 84" width="84" height="84" aria-hidden="true"><circle cx="42" cy="42" r="38" fill="none" stroke="var(--hd-track)" stroke-width="3"/>'
                f'<circle cx="42" cy="42" r="38" fill="none" stroke="var(--hd-accent)" stroke-width="3" stroke-linecap="round" stroke-dasharray="{c * pct / 100:.1f} {c:.1f}" transform="rotate(-90 42 42)"/></svg>')
    av_empty = (f'<div class="n-avu"><div class="n-av empty"><span class="n-ph">{ic("camera", 24)}</span></div><div class="n-avt"><b>Profile photo</b><span class="t-small muted">JPG or PNG, 400 × 400 px or larger.</span>'
                f'<div class="n-act">{btn("s sm", "Add photo", ic("upload", 16))}</div></div></div>')
    av_fill = (f'<div class="n-avu"><div class="n-av"><img src="{pe("women-68")}" alt="Riya Sharma"></div><div class="n-avt"><b>Riya Sharma</b><span class="t-small muted">riya-portrait.jpg · 1.4 MB</span>'
               f'<div class="n-act">{btn("s sm", "Change")}{btn("g sm", "Remove")}</div></div></div>')
    av_up = (f'<div class="n-avu"><div class="n-av up"><img src="{pe("women-44")}" alt="">{ring(64)}</div><div class="n-avt"><b>Uploading photo</b><span class="t-small muted num">64% · 0.9 of 1.4 MB</span>'
             f'<div class="n-act">{btn("g sm", "Cancel")}</div></div></div>')

    ty = lambda icon, t: f'<span class="n-ty">{icon}{t}</span>'
    types = ty(ic("play", 14), "MP4") + ty(ic("play", 14), "MOV") + ty(ic("clock", 14), "Up to 90 s") + ty(ic("file", 14), "200 MB")
    dz_idle = (f'<div class="n-dz"><span class="n-ft lg">{ic("upload", 20)}</span><div class="n-dzt"><b>Drag and drop your review video</b><span>or <u>browse files</u> · MP4 or MOV, up to 200 MB</span></div></div>')
    dz_drag = (f'<div class="n-dz drag"><span class="n-ft lg">{ics("upload", 20)}</span><div class="n-dzt"><b>Drop to upload</b><span>glow-serum-review.mp4 · 18.4 MB</span></div></div>')
    def frow(kind, name, meta, pct=0):
        if kind == "err":
            return (f'<div class="n-fr err"><span class="n-ft err">{ics("alert", 18)}</span><div class="n-frb"><b>{name}</b><span class="n-frm">{meta}</span></div>{btn("s sm", "Replace")}{ibtn(ic("x", 16), "Remove file", "g", "sm")}</div>')
        if kind == "ok":
            return (f'<div class="n-fr"><span class="n-ft">{ic("play", 20)}</span><div class="n-frb"><b>{name}</b><span class="n-frm">{meta}</span></div><span class="badge success">{ics("success", 13)}Uploaded</span>{ibtn(ic("x", 16), "Remove file", "g", "sm")}</div>')
        return (f'<div class="n-fr"><span class="n-ft">{ic("play", 20)}</span><div class="n-frb"><b>{name}</b><span class="n-frm num">{meta}</span><div class="tape n-t4"><i style="width:{pct}%"></i></div></div><span class="n-pct num">{pct}%</span>{ibtn(ic("x", 16), "Cancel upload", "g", "sm")}</div>')
    rows = (frow("go", "glow-serum-review.mp4", "11.4 of 18.4 MB", 62) + frow("ok", "unboxing-clip.mp4", "6.2 MB") + frow("err", "night-routine.mov", "412 MB · over the 200 MB limit"))

    hist = [3, 5, 8, 12, 15, 18, 22, 26, 24, 20, 17, 14, 11, 9, 7, 5, 4, 3, 2, 2]
    lo, hi = 3, 13
    bars = "".join(f'<i class="{"in" if lo <= i <= hi else ""}" style="--h:{h}"></i>' for i, h in enumerate(hist))
    slider = (f'<div class="n-rngw"><div class="n-rhead"><b>Reward per review</b><span class="num n-rv">{inr(600)} – {inr(2500)}</span></div>'
              f'<div class="n-hist">{bars}</div>'
              f'<div class="n-rng" style="--a:15%;--b:65%"><span class="tr"></span><span class="fill"></span><span class="th" style="--p:15%" role="slider" aria-valuenow="600"></span><span class="th foc" style="--p:65%" role="slider" aria-valuenow="2500"></span></div>'
              f'<div class="n-rin"><div class="input"><span class="addon">Min</span><span class="num">₹600</span></div><span class="n-dash"></span><div class="input"><span class="addon">Max</span><span class="num">₹2,500</span></div></div></div>')

    tg1 = f'<span class="seg" role="tablist" aria-label="Layout"><span class="on" aria-label="Grid">{ics("grid", 18)}</span><span aria-label="List">{ic("list", 18)}</span></span>'
    tg2 = f'<span class="seg"><span>Week</span><span class="on">Month</span><span>Year</span></span>'
    tg3 = (f'<span class="n-tgm" role="group" aria-label="Platforms"><span class="on">{soc("Instagram", 18)}Instagram</span><span class="on">{soc("Youtube", 18)}YouTube</span><span>{soc("Threads", 18)}Threads</span></span>')

    txt = "Used it every night for two weeks. Light, absorbs fast, and my skin feels calmer by the second week. The dropper leaks a little."
    ta_ok = field("Your review", f'<div class="input textarea foc n-ta"><span>{txt}</span></div>', f'Say what changed for you<span class="cnt num">128 / 600</span>', hint="Required")
    ta_warn = field("Short bio", f'<div class="input textarea n-ta"><span>Skincare nerd from Kolkata. I test one product at a time and say what I really think, with photos and before-after.</span></div>', f'<span class="n-warn w">{ic("alert", 14)}22 characters left</span><span class="cnt num n-warn">118 / 140</span>')
    ta_err = field("Short bio · over the limit", f'<div class="input textarea err n-ta"><span>Skincare nerd from Kolkata. I test one product at a time and say what I really think, with photos, before-after and a link to every shop.</span></div>', f'{ic("alert", 14)}Trim 9 characters to save<span class="cnt num">149 / 140</span>', err=True)

    A = f'<div class="box n-stage">{lab("copy field · idle, copied, disabled")}{copy_idle}{copy_done}{ref}{lab("avatar upload · empty, set, uploading")}{av_empty}{av_fill}{av_up}{lab("toggle button group")}<div class="n-tgs">{tg1}{tg2}</div>{tg3}</div>'
    Bx = f'<div class="box n-stage">{lab("file dropzone · idle")}{dz_idle}{lab("drag over")}{dz_drag}{lab("upload rows · uploading, done, error")}<div class="n-frs">{rows}</div></div>'
    Cx = (f'<div class="box n-stage">{lab("range slider · two thumbs")}{slider}'
          f'{lab("character-counted textarea")}{ta_ok}{ta_warn}{ta_err}</div>')

    # form section layout ------------------------------------------------------
    chev = f'<span class="trail n-chev">{ic("down", 18)}</span>'
    s1 = (f'<div class="n-fs"><div class="n-fsh"><h3 class="t-h3">Payout account</h3><p class="t-small muted">Where we send your earnings. Brands never see these details.</p></div>'
          f'<div class="n-ff"><div class="n-fgrid">' + field("Account holder", f'<div class="input"><span>Riya Sharma</span></div>', "Exactly as on your bank account.", hint="Required") +
          field("UPI ID", f'<div class="input err"><span class="n-id">riya.sharma@okhdfc</span></div>', f'{ic("alert", 14)}We couldn’t find that UPI ID. Check the bank handle, like @okhdfcbank.', err=True, hint="Required") +
          field("Bank account", f'<div class="input dis">{ic("lock", 18)}<span class="n-val">HDFC ••6093</span><span class="trail"><span class="badge success">{ics("success", 13)}Verified</span></span></div>', "To change this account, contact support.") + '</div></div></div>')
    s2 = (f'<div class="n-fs"><div class="n-fsh"><h3 class="t-h3">Tax details</h3><p class="t-small muted">We need your PAN to pay out more than ₹30,000 a year.</p></div>'
          f'<div class="n-ff"><div class="n-fgrid">' + field("PAN", f'<div class="input"><span class="n-id">ABCDE1234F</span></div>', "Five letters, four digits, one letter.", hint="Optional") +
          field("Financial year", f'<div class="input n-sel"><span class="n-val">2026–27</span>{chev}</div>', "Statements follow this year.") +
          field("Statements", f'<div class="n-togl"><span class="switch on"></span><span class="t-body">Email me every month</span></div>', "Sent on the 1st.") + '</div></div></div>')
    form = (f'<div class="card n-form">{s1}{s2}<div class="n-ffoot"><span class="t-small muted">Unsaved changes</span><span class="sp"></span>{btn("s", "Discard")}{btn("p", "Save changes")}</div></div>')

    return sec("Form controls · input, upload and layout", "Copy, upload, range and counted text, plus the form section layout that holds them: label, help and error in one rhythm.",
               f'<div class="grid g3 n-top">{A}{Bx}{Cx}</div><div class="n-gap"></div>{lab("form section layout")}<div class="box">{form}</div>', "nw2")

# ================================================================== 3 · FLOW & NAVIGATION · STEPS AND OVERLAYS
def flow_a(theme):
    def hstep(steps, now):
        out = []
        for i, (t, s) in enumerate(steps):
            st = "done" if i < now else "now" if i == now else ""
            k = ic("check", 14, sw=3) if st == "done" else ""
            out.append(f'<div class="s {st}" role="listitem"{" aria-current=\"step\"" if st == "now" else ""}><span class="k">{k}</span><span class="n-st"><b>{t}</b><small>{s}</small></span></div>')
            if i < len(steps) - 1: out.append(f'<i class="ln {"done" if i < now else ""}" aria-hidden="true"></i>')
        return '<div class="n-wz" role="list">' + "".join(out) + '</div>'
    steps = [("Basics", "Name and city"), ("Socials", "Instagram, YouTube"), ("Payout", "UPI or bank"), ("Review", "Check and submit")]
    wz_d = (f'<div class="card n-wzcard">{hstep(steps, 2)}</div>')
    wz_d2 = (f'<div class="card n-wzcard">{hstep(steps, 0)}</div>')

    def seg(n, now): return '<span class="n-sg">' + "".join(f'<i class="{"on" if i < now else "cur" if i == now else ""}"></i>' for i in range(n)) + '</span>'
    m1 = (f'<div class="n-dev n-wzm"><div class="n-wzt">{ibtn(ic("back", 20), "Back", "g", "icon")}<div><b>Payout</b><small>Step 3 of 4</small></div><span class="n-skip">Skip</span></div>{seg(4, 2)}</div>')
    m2 = (f'<div class="n-dev n-wzm"><div class="n-wzt">{ibtn(ic("back", 20), "Back", "g", "icon")}<div><b>Review and submit</b><small>Step 4 of 4</small></div><span class="n-skip"></span></div>{seg(4, 3)}</div>')
    dots = (f'<div class="n-dev n-wzm"><div class="n-wzt">{ibtn(ic("x", 20), "Close", "g", "icon")}<div><b>Where should we ship it?</b></div><span class="n-skip"></span></div>'
            f'<div class="n-dots2"><i class="on"></i><i class="cur"></i><i></i><i></i></div></div>')

    # command palette
    def ci(lead, label, sub="", tail="", hl=False): return f'<span class="n-ci {"hl" if hl else ""}">{lead}<span class="n-t">{label}</span>{f"<span class=n-sub>{sub}</span>" if sub else ""}{tail}</span>'
    cmd = (f'<div class="dialog n-cmd"><div class="n-cin">{ic("search", 20)}<span class="n-q">glow<i class="n-caret"></i></span>{kbd("esc")}</div>'
           f'<div class="n-tabs"><span class="on">All<b class="num">9</b></span><span>Drops<b class="num">3</b></span><span>Creators<b class="num">2</b></span><span>Pages<b class="num">1</b></span></div>'
           f'<div class="n-cs"><span class="n-gh">Drops</span>'
           + ci(f'<img src="{PH["serum"]}" alt="">', "<b>Glow</b> serum, 30 ml", "Lumen Labs", f'<span class="n-go">Open {kbd("↵")}</span>', True)
           + ci(f'<img src="{PH["cream"]}" alt="">', "<b>Glow</b> night cream, 50 g", "Lumen Labs")
           + ci(f'<img src="{PH["bottles"]}" alt="">', "Clear skin set", "Lumen Labs")
           + '<span class="n-gh">Creators</span>'
           + ci(av("GS", 0, 28), "<b>Glo</b>ria Samuel", "Mumbai · 9.2k")
           + ci(f'<img class="n-r" src="{pe("women-68")}" alt="">', "Riya Sharma", "Kolkata · 18.4k")
           + '<span class="n-gh">Actions</span>'
           + ci(ic("plus", 20), "Create campaign", "", f'<span class="n-k">{kb("⌘", "N")}</span>')
           + ci(ic("wallet", 20), "Go to wallet", "", f'<span class="n-k">{kb("G", "W")}</span>')
           + ci(ic("download", 20), "Export reviews as CSV", "", f'<span class="n-k">{kb("⌘", "E")}</span>')
           + f'</div><div class="n-cf"><span>{kb("↑", "↓")} move</span><span>{kb("↵")} open</span><span>{kb("esc")} close</span><span class="sp"></span><span>9 results</span></div></div>')

    pop = (f'<div class="n-anchor">{btn("s sm", "When do I get paid?", ic("info", 16))}<div class="dialog n-pop"><b>Paid within 48 hours</b><p class="t-small muted">Once the brand approves your review, the money moves to HDFC ••6093. Weekends can add a day.</p>'
           f'<div class="n-popf"><button class="btn link">How payouts work</button><button class="btn s sm">Got it</button></div></div></div>')

    hover = (f'<div class="n-anchor"><span class="n-mention">Reviewed by <u>@riya.sharma</u></span><div class="dialog n-hc"><div class="n-hch"><img src="{pe("women-68")}" alt=""><div><b>Riya Sharma {vhex(14)}</b><span class="t-small muted">@riya.sharma · Kolkata</span></div></div>'
             f'<p class="t-small">Honest skincare and everyday routines. Tests one product at a time.</p>'
             f'<div class="n-hcs"><div><b class="num">18.4k</b><span>{soc("Instagram", 14)}Instagram</span></div><div><b class="num">6.1k</b><span>{soc("Youtube", 14)}YouTube</span></div><div><b class="num">4.8</b><span>{ics("star", 14, "var(--hd-star)")}62 reviews</span></div></div>'
             f'<div class="n-act">{btn("p sm", "View profile")}{btn("s sm", "Invite", ic("send", 16))}</div></div></div>')

    return sec("Flow and navigation · steps, search and overlays", "Wizard steppers for desktop and phone, the command palette, and the small floating surfaces that anchor to a trigger.",
        f'<div class="box n-stage">{lab("wizard stepper · desktop")}<div class="grid g2">{wz_d}{wz_d2}</div>{lab("wizard stepper · compact, mobile")}<div class="n-mrow">{m1}{m2}{dots}</div></div>'
        f'<div class="n-gap"></div><div class="grid n-g31"><div class="box n-stage n-center">{lab("command palette · ⌘K")}{cmd}</div>'
        f'<div class="box n-stage">{lab("popover")}{pop}{lab("hover card · creator")}{hover}</div></div>', "nw3")

# ================================================================== 4 · FLOW & NAVIGATION · MENUS, SHEETS, FILTERS
def flow_b(theme):
    mi = lambda icon, t, k="", cls="": f'<div class="{cls}">{icon}<span class="n-t">{t}</span>{k}</div>'
    ctx = (f'<div class="n-ctxw"><div class="menu n-ctx" role="menu">'
           + mi(ic("ok", 18), "Approve review", f'<span class="n-k">{kb("A")}</span>')
           + mi(ic("edit", 18), "Request changes", f'<span class="n-k">{kb("R")}</span>')
           + mi(ic("link", 18), "Copy review link", f'<span class="n-k">{kb("⌘", "C")}</span>')
           + '<i class="n-sep"></i>'
           + mi(ic("send", 18), "Move to", f'<span class="n-chv">{ic("chev", 16)}</span>', "hl")
           + mi(ic("users", 18), "Assign to", f'<span class="n-chv">{ic("chev", 16)}</span>')
           + '<i class="n-sep"></i>'
           + mi(ic("trash", 18), "Reject review", f'<span class="n-k">{kb("Del")}</span>', "dg")
           + '</div><div class="menu n-ctx n-subm" role="menu">'
           + mi(ic("clock", 18), "Needs changes") + mi(ic("ok", 18), "Approved", f'<span class="n-k n-tk">{ic("check", 16, sw=2.4)}</span>') + mi(ic("archive", 18), "Archived") + '</div></div>')

    def asr(t, cls=""): return f'<span class="n-asa {cls}">{t}</span>'
    asheet = (f'<div class="n-dev n-asd">{GHOST_Q}<div class="n-scrim"></div>'
              f'<div class="n-as"><div class="n-asg"><span class="n-ash"><b>Riya Sharma’s review</b>Glow serum · Instagram reel</span>{asr("Approve review")}{asr("Request changes")}{asr("Copy link")}{asr("Report a problem", "dg")}</div>'
              f'<div class="n-asg">{asr("Cancel", "cn")}</div><i class="n-hi"></i></div></div>')

    def chipt(icon, t, on=False): return f'<span class="chip {"on" if on else ""}">{icon}{t}</span>'
    hist = [4, 7, 11, 16, 22, 27, 24, 19, 14, 10, 7, 5, 3, 2]
    bars = "".join(f'<i class="{"in" if 3 <= i <= 10 else ""}" style="--h:{h}"></i>' for i, h in enumerate(hist))
    fil = (f'<div class="card n-fil"><div class="n-filh"><b class="t-h3">Filters</b><span class="n-fc">3 applied</span><button class="btn link">Reset all</button></div>'
           f'<div class="n-fsec"><b>Category</b><div class="flexw">{chipt(ics("drop", 16), "Skincare", True)}{chipt(ics("lipstick", 16), "Makeup", True)}{chipt(ic("shirt", 16), "Fashion")}{chipt(ic("lamp", 16), "Home")}{chipt(ic("headphones", 16), "Gadgets")}</div></div>'
           f'<div class="n-fsec"><b>Platform</b><div class="flexw">{chipt(soc("Instagram", 16), "Instagram", True)}{chipt(soc("Youtube", 16), "YouTube")}{chipt(soc("Threads", 16), "Threads")}</div></div>'
           f'<div class="n-fsec"><div class="n-rhead"><b>Reward</b><span class="num n-rv">{inr(600)} – {inr(2500)}</span></div><div class="n-hist">{bars}</div>'
           f'<div class="n-rng" style="--a:22%;--b:72%"><span class="tr"></span><span class="fill"></span><span class="th" style="--p:22%"></span><span class="th" style="--p:72%"></span></div></div>'
           f'<div class="n-fsec n-frow"><span class="n-t"><b>Ships from Kolkata</b><small>Faster delivery, 1 to 2 days</small></span><span class="switch on"></span></div>'
           f'<div class="n-filf">{btn("s", "Reset")}{btn("p", "Show 23 drops")}</div></div>')

    sopt = [("Most relevant", False), ("Highest reward", True), ("Newest first", False), ("Ending soon", False), ("Most reviewed", False)]
    sort = (f'<div class="n-sortw"><span class="chip on">{ic("sort", 16)}Sort: Highest reward{ic("down", 14)}</span><div class="menu n-sortm" role="menu"><span class="n-mh">Sort by</span>'
            + "".join(f'<div class="{"on" if s else ""} {"hl" if s else ""}"><span class="n-tk">{ic("check", 16, sw=2.4) if s else ""}</span><span class="n-t">{t}</span></div>' for t, s in sopt) + '</div></div>')

    more = (f'<div class="n-more"><div class="n-prog"><span class="t-small muted">Showing <b class="num">24</b> of <b class="num">118</b> drops</span><div class="tape"><i style="width:20%"></i></div></div>{btn("s", "Load 24 more")}</div>')
    more2 = (f'<div class="n-more"><div class="n-prog"><span class="t-small muted">Showing <b class="num">24</b> of <b class="num">118</b> drops</span><div class="tape"><i style="width:20%"></i></div></div><button class="btn s" aria-busy="true"><span class="n-spin sm"></span>Loading…</button></div>')
    more3 = (f'<div class="n-more"><div class="n-prog"><span class="t-small muted">You’ve seen all <b class="num">118</b> drops</span><div class="tape"><i style="width:100%"></i></div></div><span class="n-end">{ics("success", 16)}All caught up</span></div>')

    return sec("Flow and navigation · menus, sheets and filters", "Context menu with a submenu, the iOS action sheet, the filter panel, sort and load-more.",
        f'<div class="grid g3 n-top"><div class="box n-stage">{lab("context menu · submenu · destructive")}{ctx}{lab("sort menu")}{sort}</div>'
        f'<div class="box n-stage">{lab("filter panel")}{fil}</div>'
        f'<div class="box n-stage">{lab("iOS action sheet")}{asheet}</div></div><div class="n-gap"></div>'
        f'<div class="box n-stage">{lab("load more · idle, loading, done")}<div class="grid g3">{more}{more2}{more3}</div></div>', "nw4")

# ================================================================== 5 · FEEDBACK · LOADING, DIALOGS, ERRORS
def feedback_a(theme):
    spin = (f'<div class="n-spins"><div><span class="n-spin sm"></span><small>16</small></div><div><span class="n-spin"></span><small>24</small></div><div><span class="n-spin lg"></span><small>40</small></div></div>'
            f'<div class="flexw">{btn("p", "Sending…", "", " aria-busy=\"true\"").replace("Sending…", "<span class=\"spin\"></span>Sending…")}{btn("s", "Saving", "", "").replace("Saving", "<span class=\"n-spin sm\"></span>Saving")}</div>')
    rows = (f'<div class="stack"><div class="row n-lr"><span class="n-spin"></span><div class="tx"><b>Checking your UPI ID</b><small>riya.sharma@okhdfcbank</small></div>{btn("g sm", "Cancel")}</div>'
            f'<div class="row n-lr"><span class="n-spin"></span><div class="tx"><b>Fetching Instagram insights</b><small>This takes about 10 seconds</small><div class="tape n-t4"><i style="width:55%"></i></div></div></div>'
            f'<div class="n-lmore"><span class="n-spin sm"></span><span class="t-small muted">Loading more reviews…</span></div></div>')

    dlg = (f'<div class="dialog n-dlg"><span class="n-dti dg">{ic("trash", 22)}</span><div class="t-h2">Delete Glow serum?</div>'
           f'<p class="t-body muted">This ends the campaign for 84 creators and cannot be undone. {inr(104160)} in held payouts returns to your wallet.</p>'
           f'<div class="field"><label>Type the campaign name to confirm</label><div class="input foc"><span>Glow serum</span></div></div>'
           f'<div class="n-dlf">{btn("s", "Keep campaign")}{btn("d", "Delete campaign")}</div></div>')
    dlg2 = (f'<div class="dialog n-dlg n-sm"><div class="t-h2">Reject this review?</div><p class="t-body muted">Riya Sharma can edit and resubmit within 3 days.</p>'
            f'<div class="n-dlf">{btn("s", "Cancel")}{btn("d", "Reject review")}</div></div>')

    err = (f'<div class="card n-state"><span class="n-ti">{ic("wifioff", 24)}</span><div class="t-h2">Can’t reach Hypedrive</div>'
           f'<p class="t-body muted">Check your connection and try again. Your draft is saved on this device.</p><div class="flexw n-c">{btn("p", "Try again", ic("send", 18) if False else ic("refresh", 18))}{btn("s", "Work offline")}</div>'
           f'<span class="n-code">NET_TIMEOUT · Fri, Nov 20 · 4:32 pm</span></div>')
    err2 = (f'<div class="card n-state"><span class="n-ti dg">{ic("alert", 24)}</span><div class="t-h2">Reviews didn’t load</div>'
            f'<p class="t-body muted">Something went wrong on our side. Nothing was lost.</p><div class="flexw n-c">{btn("p", "Reload reviews")}</div></div>')

    off = (f'<div class="n-bwrap"><div class="n-banner warn">{ics("wifioff", 18)}<b>You’re offline.</b><span class="n-bm">Changes sync when you’re back.</span><span class="sp"></span><span class="n-rc" role="status" aria-label="Reconnecting"><span class="n-spin sm"></span></span></div>'
           f'<div class="n-banner ok">{ics("success", 18)}<b>Back online.</b><span>3 changes synced.</span><span class="sp"></span><button class="btn link">Dismiss</button></div></div>')

    skl = '<div class="stack">' + "".join(f'<div class="row"><span class="skel n-sk1"></span><div class="tx"><span class="skel n-sk2"></span><span class="skel n-sk3"></span></div><span class="skel n-sk4"></span></div>' for _ in range(3)) + '</div>'
    A = f'<div class="box n-stage">{lab("spinner · 16, 24, 40")}{spin}{lab("inline loading row")}{rows}{lab("skeleton rows · first load")}{skl}</div>'
    Bx = f'<div class="box n-stage n-center">{lab("destructive confirm · type to confirm")}{dlg}{lab("destructive confirm · simple")}{dlg2}{lab("offline banner")}<div class="n-wide">{off}</div></div>'
    Cx = f'<div class="box n-stage">{lab("error state · network")}{err}{lab("error state · section")}{err2}</div>'
    return sec("Feedback and states · loading, dialogs and errors", "Loaders in three sizes, the destructive confirm, and the two failure states a creator can hit.",
               f'<div class="grid g3 n-top">{A}{Bx}{Cx}</div>', "nw5")

# ================================================================== 6 · FEEDBACK · PAGES, INLINE EDIT, SUCCESS
def feedback_b(theme):
    def page(ill, title, body, btns, code=""):
        return (f'<div class="card n-page"><img src="{illu(ill, theme)}" alt=""><div class="t-h2">{title}</div><p class="t-body muted">{body}</p><div class="flexw n-c">{btns}</div>{f"<span class=n-code>{code}</span>" if code else ""}</div>')
    p404 = page("search", "We can’t find that page", "The link may be old, or the drop has ended. Try searching for it instead.", btn("p", "Go home") + btn("s", "Search", ic("search", 18)), "404 · /drops/glow-serum-2")
    pinb = page("inbox", "You’re all caught up", "No reviews are waiting for you. New ones land here as creators submit.", btn("s", "See approved reviews"), "0 waiting")
    pbell = page("bell", "Nothing new yet", "Turn on alerts and we’ll tell you the moment a brand invites you.", btn("p", "Turn on alerts", ic("bell", 18)), "0 unread")
    plock = page("lock", "You don’t have access", "Only workspace admins can see payouts. Ask Aditi Mehra to add you.", btn("p", "Request access") + btn("s", "Back"), "403")

    ie_idle = (f'<div class="n-ie"><span class="t-h2 n-iev">Glow serum, 30 ml<span class="n-pen">{ic("edit", 16)}</span></span></div>')
    ie_hov = (f'<div class="n-ie hov"><span class="t-h2 n-iev">Glow serum, 30 ml<span class="n-pen">{ic("edit", 16)}</span></span></div>')
    ie_edit = (f'<div class="n-ie ed"><div class="input foc n-iei"><span class="t-h2">Glow serum, 30 ml<i class="n-caret"></i></span></div>{ibtn(ic("check", 18, sw=3), "Save", "p")}{ibtn(ic("x", 18), "Cancel", "s")}</div>'
               f'<span class="n-hint"><span>{kb("↵")} save</span><span>{kb("esc")} cancel</span></span>')
    ie_row = (f'<div class="row n-ier"><span class="n-iel">Ship-by date</span><span class="n-iev2"><b>Wed, Dec 2</b><span class="n-pen2">{ic("edit", 16)}</span></span></div>'
              f'<div class="row n-ier ed"><span class="n-iel">Slots</span><div class="n-iee"><div class="input foc"><span class="num">120</span></div>{ibtn(ic("check", 16, sw=3), "Save", "p", "sm")}{ibtn(ic("x", 16), "Cancel", "s", "sm")}</div></div>')

    ok = (f'<div class="card n-page n-succ"><img src="{illu("approved", theme)}" alt=""><div class="t-h2">Review submitted</div><p class="t-body muted">Lumen Labs checks it within a day. {inr(1240)} lands in HDFC ••6093 once it’s approved.</p>'
          f'<div class="n-sum"><span>Glow serum, 30 ml</span><b class="num">{inr(1240)}</b></div><div class="flexw n-c">{btn("p", "Back to drops")}{btn("s", "View review")}</div></div>')
    ok3 = f'<div class="n-okrow"><span class="n-okk">{ic("check", 22, sw=3)}</span><div><b>Campaign published</b><span class="t-small muted">Glow serum is live for 120 creators</span></div>{btn("g sm", "View")}</div>'
    ok2 = (f'<div class="n-okrow"><span class="n-okk">{ic("check", 22, sw=3)}</span><div><b>Payout sent</b><span class="t-small muted">{inr(1240)} to HDFC ••6093 · arrives today</span></div>{btn("g sm", "Receipt")}</div>'
           f'<div class="n-okrow"><span class="n-okk">{ic("check", 22, sw=3)}</span><div><b>UPI ID verified</b><span class="t-small muted">riya.sharma@okhdfcbank · Riya Sharma</span></div></div>')

    A = f'<div class="box n-stage">{lab("404 · page not found")}{p404}</div>'
    return sec("Feedback and states · pages, inline edit and success", "Every empty or missing page gets one isometric illustration, one sentence and one way forward.",
        f'<div class="grid n-g4"><div class="box">{lab("404 · not found")}{p404}</div><div class="box">{lab("empty · inbox")}{pinb}</div><div class="box">{lab("empty · notifications")}{pbell}</div><div class="box">{lab("no access")}{plock}</div></div>'
        f'<div class="n-gap"></div><div class="grid g3 n-top"><div class="box n-stage">{lab("inline edit · idle, hover, editing")}<div class="card n-iec2">{ie_idle}{ie_hov}{ie_edit}</div>{lab("inline edit · in a row")}<div class="stack">{ie_row}</div></div>'
        f'<div class="box n-stage">{lab("success state")}{ok}</div><div class="box n-stage">{lab("success · inline")}<div class="stack">{ok2}{ok3}</div></div></div>', "nw6")

# ================================================================== 7 · CONTENT · CARDS AND MEDIA
def content_a(theme):
    def pcard(img, brand, ba, title, reward, left, total, badge, bcls, city, dis=False):
        pct = round(100 * left / total) if total else 0
        full = left == 0
        return (f'<div class="card n-pc"><div class="n-ph"><img src="{PH[img]}" alt="{title}"><span class="badge {bcls} n-bd">{ics(badge[1], 13)}{badge[0]}</span><button class="n-disc" aria-label="Save">{ic("heart", 18)}</button></div>'
                f'<div class="n-pb"><span class="n-brand">{brand} {vhex(12)}</span><b class="n-pt">{title}</b>'
                f'<span class="n-meta">You earn <b class="num">{inr(reward)}</b> · {f"{left} of {total} left" if not full else "All slots taken"}</span>'
                f'<div class="n-line"><i style="width:{100 - pct}%"></i></div>'
                f'{btn("p block", "Apply") if not full else btn("s block", "Join waitlist")}</div></div>')
    pv = (pcard("serum", "Lumen Labs", "LL", "Glow serum, 30 ml", 1240, 36, 120, ("Live", "live"), "success", "Ships from Kolkata")
          + pcard("cream", "Lumen Labs", "LL", "Night cream, 50 g", 990, 58, 100, ("Ending soon", "clock"), "warning", "Ships from Kolkata")
          + pcard("bottles", "Lumen Labs", "LL", "Clear skin set", 980, 0, 60, ("Full", "lock"), "neutral", "Ships from Kolkata"))

    def ph(img, brand, title, reward, meta):
        return (f'<div class="card n-ph2"><img src="{PH[img]}" alt="{title}"><div class="n-hb"><div class="n-brand"><span>{brand}</span>{vhex(13)}</div>'
                f'<b class="n-pt">{title}</b><span class="n-meta">{meta}</span></div>'
                f'<div class="n-he"><b class="num">{inr(reward)}</b>{btn("p sm", "Apply")}</div></div>')
    ph_ = (ph("serum", "Lumen Labs", "Glow serum, 30 ml", 1240, "Kolkata · ends in 6 days · 84 applied")
           + ph("bottles", "Lumen Labs", "Daily cleanser trio", 640, "Kolkata · ends in 12 days · 18 applied"))

    def crc(img, n, handle, city, ig, yt, rating, rev, ver=True):
        yt_ = f'<span>{soc("Youtube", 18)}<b class="num">{yt}</b></span>' if yt else ""
        return (f'<div class="card n-cc"><img class="n-cav" src="{pe(img)}" alt="{n}"><div class="n-cn"><b>{n}</b>{vhex(16) if ver else ""}</div>'
                f'<span class="t-small muted">{handle} · {city}</span>'
                f'<div class="n-plat"><span>{soc("Instagram", 18)}<b class="num">{ig}</b></span>{yt_}</div>'
                f'<div class="n-cr">{ics("star", 14, "var(--hd-star)")}<b class="num">{rating}</b><span class="muted">· {rev} reviews</span></div>'
                f'<div class="n-pf">{btn("p block", "Invite to a drop")}</div></div>')
    cv = (crc("women-68", "Riya Sharma", "@riya.sharma", "Kolkata", "18.4k", "6.1k", "4.8", 62)
          + crc("men-12", "Arjun Kapoor", "@arjun.tests", "Delhi", "9.8k", "22.0k", "4.6", 38)
          + crc("women-65", "Meera Joshi", "@meerajoshi", "Pune", "3.2k", "", "4.9", 14, False))
    ch = (f'<div class="card n-ch"><img src="{pe("women-44")}" alt=""><div class="n-cb2"><div class="n-cn"><b>Tanvi Nair</b>{vhex(16)}<span class="muted t-small">@tanvi.n · Mumbai</span></div>'
          f'<div class="n-plat"><span>{soc("Instagram", 18)}<b class="num">24.6k</b></span><span>{soc("Youtube", 18)}<b class="num">11.2k</b></span><span class="n-cr">{ics("star", 14, "var(--hd-star)")}<b class="num">4.7</b><span class="muted">· 51 reviews</span></span></div></div>'
          f'<div class="n-hc2">{btn("p sm", "Invite")}</div></div>'
          f'<div class="card n-ch"><span class="n-chav">{av("KN", 3, 56)}</span><div class="n-cb2"><div class="n-cn"><b>Kabir Nanda</b><span class="muted t-small">@kabir.nanda · Bengaluru</span></div>'
          f'<div class="n-plat"><span>{soc("Instagram", 18)}<b class="num">5.1k</b></span><span class="n-cr">{ics("star", 14, "var(--hd-star)")}<b class="num">4.4</b><span class="muted">· 9 reviews</span></span></div></div>'
          f'<div class="n-hc2">{btn("p sm", "Invite")}</div></div>')

    return sec("Content · cards", "Drop and creator cards. Photos sit bare inside the card; the only discs are over a photo.",
        f'<div class="box n-stage">{lab("product card · vertical")}<div class="n-trio">{pv}</div></div><div class="n-gap"></div>'
        f'<div class="box n-stage">{lab("creator card · vertical")}<div class="n-trio">{cv}</div></div><div class="n-gap"></div>'
        f'<div class="grid g2 n-top"><div class="box n-stage">{lab("product card · horizontal")}{ph_}</div>'
        f'<div class="box n-stage">{lab("creator card · horizontal")}{ch}</div></div>', "nw7")


def content_b(theme):
    # ---- desktop product gallery: thumbnail rail + 4:5 hero --------------------------------
    gal = [("serum", "Glow serum, 30 ml on a stone surface"), ("cream", "Body lotion on linen"), ("flatlay", "Skincare flat lay"), ("bottles", "Cleanser bottles on a shelf")]
    def thumb(k, i, on):
        return f'<button class="m-th {"on" if on else ""}" aria-label="Photo {i + 1} of 4" aria-current="{str(on).lower()}"><img src="{PH[k]}" alt=""></button>'
    def dots(n, on): return '<span class="m-dots" aria-hidden="true">' + "".join(f'<i class="{"on" if i == on else ""}"></i>' for i in range(n)) + '</span>'
    hero = (f'<div class="m-hero"><img src="{PH["serum"]}" alt="{gal[0][1]}"><span class="m-chip num">1/4</span>'
            f''
            f'<button class="m-disc m-prev" aria-label="Previous photo" disabled>{ic("back", 18)}</button><button class="m-disc m-next" aria-label="Next photo">{ic("chev", 18)}</button>{dots(4, 0)}</div>')
    desk = f'<div class="m-gal"><div class="m-rail">' + "".join(thumb(k, i, i == 0) for i, (k, _) in enumerate(gal)) + f'</div>{hero}</div>'

    # ---- mobile carousel with a peeking next slide, in a page ---------------------------------
    mob = (f'<div class="n-dev m-phone"><div class="m-top">{ibtn(ic("back", 20), "Back", "g", "icon")}<span class="sp"></span>{ibtn(ic("share", 20), "Share", "g", "icon")}</div>'
           f'<div class="m-track"><div class="m-slide"><img src="{PH["serum"]}" alt=""></div><div class="m-slide"><img src="{PH["cream"]}" alt=""></div></div>{dots(4, 0).replace("m-dots", "m-dots on-canvas")}'
           f'<div class="m-info"><b class="t-h2">Glow serum, 30 ml</b>'
           f'<div class="n-rw"><span class="muted">You earn</span><b class="num">{inr(1240)}</b></div></div></div>')
    ind = (f'<div class="m-inds"><div><span class="t-cap muted">Story bars</span><span class="m-bars"><i class="on"></i><i class="cur"></i><i></i><i></i></span></div>'
           f'<div><span class="t-cap muted">Counter only</span><span class="m-chip m-chip-s num">2/4</span></div></div>')

    # ---- reels ---------------------------------------------------------------------------
    def reel(src, dur, views, cap, when, who, handle, pl, av_=None, pos="50% 50%"):
        a = f'<img class="m-av" src="{pe(av_)}" alt="">' if av_ else av(who, 3, 24)
        return (f'<div class="m-reelw"><div class="m-reel"><img class="m-ph" src="{src}" alt="" style="object-position:{pos}"><span class="m-pl">{soc(pl, 16)}</span><span class="m-dur num">{dur}</span>'
                f'<span class="m-play" role="img" aria-label="Play reel">{gs("MediaPlay", 20)}</span>'
                f'<div class="m-meta"><div class="m-who">{a}<b>{handle}</b></div><span class="m-views">{ic("eye", 14)}<span class="num">{views}</span> views</span></div></div>'
                f'<b class="m-cap">{cap}</b></div>')
    reels = "".join([
        reel(PH["serum"], "0:42", "12.4k", "Night routine with Glow serum", "2 days ago · Glow serum", "RS", "riya.sharma", "Instagram", "women-68", "56% 50%"),
        reel(PH["bottles"], "0:58", "8.1k", "Two weeks on the Lumen set, honest", "4 days ago · Clear skin set", "TN", "tanvi.n", "Instagram", "women-44", "72% 50%"),
        reel(PH["cream"], "0:31", "3.6k", "Does the body lotion layer well?", "5 days ago · Night cream", "AK", "arjun.tests", "Threads", "men-12"),
        reel(PH["flatlay"], "1:04", "21.8k", "Everything in my April box", "1 week ago · Daily cleanser trio", "MJ", "meerajoshi", "Instagram", "women-65"),
        reel(PH["serum"], "0:27", "1.9k", "Desert-proof skincare test", "1 week ago · Clear skin set", "KN", "kabir.nanda", "Youtube", None, "4% 50%")])

    # ---- landscape + list rows -----------------------------------------------------------
    yt = (f'<div class="m-ytw"><div class="m-yt"><img src="{PH["bottles"]}" alt=""><span class="m-pl">{soc("Youtube", 16)}</span><span class="m-dur num">8:14</span>'
          f'<span class="m-play" role="img" aria-label="Play video">{gs("MediaPlay", 22)}</span></div>'
          f'<div class="m-ytb"><img class="m-av l" src="{pe("men-12")}" alt=""><div><b>30 days with the Lumen cleanser trio</b><span class="t-small muted">Arjun Kapoor {vhex(12)} · 22.0k views · 3 days ago</span></div></div></div>')
    def lr(src, dur, t, who, views, badge, bcls, bic):
        return (f'<div class="row m-lr"><span class="m-lt"><img src="{src}" alt=""></span><div class="tx"><b>{t}</b><small>{who}</small></div><span class="badge {bcls}">{ics(bic, 13)}{badge}</span></div>')
    lrs = (lr(PH["serum"], "0:42", "Night routine with Glow serum", "Riya Sharma · Instagram reel", "12.4k", "Approved", "success", "success")
           + lr(PH["cream"], "0:31", "Does the body lotion layer well?", "Arjun Kapoor · Threads video", "3.6k", "To check", "warning", "clock"))

    # ---- review photo mosaic + upload tiles -------------------------------------------------
    mos = (f'<div class="m-mos"><img class="b" src="{PH["flatlay"]}" alt=""><img src="{PH["serum"]}" alt="" style="object-position:10% 40%"><img src="{PH["cream"]}" alt=""><img src="{PH["bottles"]}" alt="" style="object-position:20% 50%">'
           f'<span class="m-last"><img src="{PH["bottles"]}" alt="" style="object-position:90% 50%"><span class="m-more">{btn("s sm", "Show all 12", ic("grid", 16))}</span></span></div>')
    def tile(kind, src="", name="", sz=""):
        if kind == "add": body = f'<span class="m-up add">{ic("plus", 22)}<small>Add photo</small></span>'
        elif kind == "ok": body = f'<span class="m-up"><img src="{src}" alt=""><span class="m-ok">{ics("success", 18)}</span></span>'
        elif kind == "go":
            c = 2 * 3.14159 * 18
            body = (f'<span class="m-up"><img src="{src}" alt=""><span class="m-dim"><svg width="44" height="44" viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="18" fill="none" stroke="currentColor" stroke-opacity=".3" stroke-width="3"/>'
                    f'<circle cx="22" cy="22" r="18" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-dasharray="{c * .64:.1f} {c:.1f}" transform="rotate(-90 22 22)"/></svg><b class="num">64%</b></span></span>')
        else: body = f'<span class="m-up err">{ics("alert", 22)}<b>Too large</b><button class="btn link">Retry</button></span>'
        return f'<div class="m-tile">{body}<span class="m-fn">{name or "&nbsp;"}</span></div>'
    ups = (f'<div class="m-ups">{tile("ok", PH["serum"], "glow-1.jpg · 1.2 MB")}{tile("go", PH["cream"], "glow-2.jpg · 0.8 MB")}{tile("err", "", "glow-3.mov · 412 MB")}</div>')

    fk = ["serum", "cream", "flatlay", "bottles"]
    frames = '<div class="m-frames">' + "".join(f'<button class="{"on" if i == 2 else ""}" aria-label="Frame {i + 1}"><img src="{PH[k]}" alt=""{"" }>{"<span class=m-cv>Cover</span>" if i == 2 else ""}</button>' for i, k in enumerate(fk)) + '</div>'
    return sec("Content · media", "Product gallery, reels, video and review photos. Photos are edge to edge with a crisp 1px border; controls sit on the photo as discs.",
        f'<div class="grid m-g2 n-top"><div class="box n-stage">{lab("product gallery · desktop, 4:5 hero")}{desk}</div>'
        f'<div class="box n-stage">{lab("image carousel · mobile, peeking next slide")}{mob}</div></div><div class="n-gap"></div>'
        f'<div class="box n-stage">{lab("reel thumbnails · 9:16")}<div class="m-reels">{reels}</div></div><div class="n-gap"></div>'
        f'<div class="grid g2 n-top"><div class="box n-stage">{lab("video thumbnail · landscape")}{yt}{lab("reel in a review queue")}<div class="stack">{lrs}</div></div>'
        f'<div class="box n-stage">{lab("review photo set")}{mos}{lab("upload previews · done, uploading, failed")}{ups}</div></div>', "nw8")


def content_c(theme):
    # message thread
    def msg(side, inner, last=False, meta=""):
        who = f'<span class="t-av">{av("AM", 2, 28)}</span>' if side == "in" and last else (f'<span class="t-av"></span>' if side == "in" else "")
        return f'<div class="t-m {side}{" last" if last else ""}">{who}<div class="t-c">{inner}{f"<span class=t-meta>{meta}</span>" if meta else ""}</div></div>'
    bubble = lambda s: f'<p class="t-b">{s}</p>'
    pdf = f'<div class="t-file"><span class="x-tile cobalt">{ic("file", 20)}</span><div><b>Brief, Glow serum.pdf</b><span>1.2 MB · PDF</span></div>{ibtn(ic("download", 16), "Download", "g", "sm")}</div>'
    img = f'<img class="t-img" src="{PH["serum"]}" alt="Draft cover">'
    thread = (f'<div class="card t-thr"><div class="t-head"><span class="av av-2">LL</span><div><b>Lumen Labs</b><span>Aditi Mehra · replies in a few hours</span></div>'
              f'</div>'
              f'<div class="t-body"><span class="t-day">Today</span>'
              + msg("in", pdf)
              + msg("in", bubble("Hi Riya! Thanks for applying. The brief has the talking points and the dos and don’ts."), True, "10:42 am")
              + msg("out", bubble("Thanks Aditi. Can I post the reel on Saturday evening?"), True, "10:50 am")
              + msg("in", bubble("Saturday works. Please tag @lumenlabs and keep the serum label visible."), True, "10:58 am")
              + msg("out", img)
              + msg("out", bubble("Here’s the draft cover. Okay to use?"), True, f'11:05 am · Read')
              + f'</div><div class="t-comp"><div class="t-field"><button class="t-ib" aria-label="Attach">{ic("clip", 18)}</button><span class="ph">Message Lumen Labs</span></div>{ibtn(ic("send", 18, sw=3), "Send", "p")}</div></div>')

    dl = [("Your reward", f'<b class="num">{inr(1240)}</b>'), ("Ships to", "14 Park Street, Kolkata 700016"), ("Review due", "Fri, Nov 27"), ("Payout to", "HDFC ••6093")]
    dl_h = '<dl class="n-dl">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in dl) + '</dl>'
    dl_g = '<dl class="n-dl grid2">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in dl[:6]) + '</dl>'

    PEOPLE = {p: f"{STOCK}/people/{p}.jpg" for p in ("women-68", "women-44", "men-12")}
    dv = (f'<div class="n-dvx">'
          f'<div class="n-dvc"><span class="n-dvt">Inset · settings list</span><div class="n-dvl">'
          + "".join(f'<div class="n-dvi">{ic(i, 20)}<b>{t}</b><span class="m">{m}</span>{ic("chev", 16)}</div>' for i, t, m in (("user", "Personal details", ""), ("bank", "Payout method", "HDFC ••6093"), ("bell", "Notifications", "On"))) +
          f'</div></div>'
          f'<div class="n-dvc"><span class="n-dvt">Labelled · sign in</span><div class="n-dvsign"><button class="btn p block">Continue with phone</button><div class="n-hrl"><i></i><span>or</span><i></i></div><button class="btn s block">Continue with email</button></div></div>'
          f'<div class="n-dvc"><span class="n-dvt">Section label · activity</span><div class="n-dvfeed"><div class="n-hrl left"><span>Today</span><i></i></div>'
          f'<div class="n-dvr"><b>Payout sent</b><span class="num">+₹1,240</span></div><div class="n-hrl left"><span>Earlier this week</span><i></i></div>'
          f'<div class="n-dvr"><b>Review approved</b><span class="num">+₹990</span></div><div class="n-dvr"><b>Parcel delivered</b><span class="m">Mon</span></div></div></div>'
          f'<div class="n-dvc"><span class="n-dvt">Inline vertical · profile</span><div class="n-dvprof"><img src="{PEOPLE["women-68"]}" alt=""><div><b>Riya Sharma {vhex(14)}</b>'
          f'<div class="n-vrow"><span><b class="num">18.4k</b> followers</span><i class="n-vr"></i><span><b class="num">62</b> reviews</span><i class="n-vr"></i><span>Kolkata</span></div></div></div>'
          f'<span class="n-dvt" style="margin-top:14px">Section break · sheet</span><div class="n-dvbreak"><div class="n-dvr"><b>Glow serum, 30 ml</b><span class="m">Lumen Labs</span></div><div class="n-band"></div><div class="n-dvr"><b>Ship to</b><span class="m">14 Park Street, Kolkata</span></div></div></div>'
          f'</div>')

    def sw(img, t, s, st, time): return f'<div class="n-sc"><img src="{PH[img]}" alt=""><div class="tx"><b>{t}</b><small>{s}</small></div><span class="t-cap muted num">{time}</span></div>'
    swipe = (f'<div class="n-dev n-sw"><div class="n-swr"><div class="n-swa l"><span class="a ok">{ic("check", 20, sw=2.4)}Approve</span></div><div class="row n-sr off">{av("RS", 0, 40)}<div class="tx"><b>Riya submitted her Glow serum reel</b><small>Riya Sharma</small></div><span class="t-cap muted num">2m</span></div></div>'
             f'<div class="n-swr"><div class="n-swa r"><span class="a mu">{ic("archive", 20)}Archive</span><span class="a dg">{ic("trash", 20)}Delete</span></div><div class="row n-sr left">{av("AK", 1, 40)}<div class="tx"><b>Arjun asked for changes to Night cream</b><small>Arjun Kapoor</small></div><span class="t-cap muted num">18m</span></div></div>'
             f'<div class="n-swr"><div class="row n-sr">{av("MJ", 2, 40)}<div class="tx"><b>Meera’s Clear skin set review is approved</b><small>Meera Joshi</small></div><span class="t-cap muted num">1h</span></div></div></div>')

    apps = [("Whatsapp", "WhatsApp"), ("Instagram", "Instagram"), ("Threads", "Threads"), ("Facebook", "Facebook"), ("XTwitter", "X")]
    share = (f'<div class="n-dev n-shd">{GHOST_D}<div class="n-scrim"></div><div class="sheet n-shs"><div class="grab"></div><div class="n-shh"><div class="t-h2">Share</div><span class="x-disc n-shx" aria-label="Close">{ic("x", 16)}</span></div>'
             f'<div class="n-shp"><img src="{PH["serum"]}" alt=""><div><b>Glow serum, 30 ml</b><span class="t-small muted">hypedrive.in/d/glow-serum</span></div></div>'
             f'<div class="n-apps">' + "".join(f'<div><span class="n-app">{soc(k, 26)}</span><small>{n}</small></div>' for k, n in apps) + '</div>'
             f'<div class="group n-shg"><div class="gi">{ic("link", 20)}<b>Copy link</b><span class="meta">hypedrive.in/d/glow-serum</span></div><div class="gi">{ic("download", 20)}<b>Save image</b></div><div class="gi">{ic("more", 20)}<b>More options</b></div></div></div></div>')

    ea = (f'<div class="card n-ea"><img src="{illu("camera", theme)}" alt=""><div class="t-h2">Post your first review</div><p class="t-body muted">Apply to a drop, try it for real, and share an honest review. You get paid in ₹ once it’s approved.</p>'
          f'<ul class="n-chk"><li>{ic("check", 18)}Pick a drop that fits your audience</li><li>{ic("clock", 18)}Receive the product in 3 to 5 days</li><li>{ic("rupee", 18)}Get paid within 48 hours of approval</li></ul>'
          f'<div class="flexw n-c">{btn("p", "Browse drops", ic("search", 18))}{btn("g", "How payouts work")}</div></div>')
    ea2 = (f'<div class="n-ea2"><span class="n-eai">{ic("heart", 22)}</span><div><b>No saved drops</b><span class="t-small muted">Tap the heart on a drop to keep it here.</span></div>{btn("s sm", "Browse drops")}</div>'
           f'<div class="n-ea2"><span class="n-eai">{ic("users", 22)}</span><div><b>No creators yet</b><span class="t-small muted">Invite creators to apply to Glow serum.</span></div>{btn("p sm", "Invite creators", ic("plus", 16))}</div>')

    ea3 = (f'<div class="n-ea2"><span class="n-eai">{ic("payouts", 22)}</span><div><b>No payouts yet</b><span class="t-small muted">Your first payout shows here once a review is approved.</span></div>{btn("g sm", "How payouts work")}</div>'
           f'<div class="n-ea2"><span class="n-eai">{ic("search", 22)}</span><div><b>Nothing matches “glo”</b><span class="t-small muted">Check the spelling, or search by brand name.</span></div>{btn("s sm", "Clear search")}</div>')
    return sec("Content · conversation and lists", "Brand and creator thread, key–value lists, dividers, swipe actions, the share sheet and empty cards with a next step.",
        f'<div class="grid n-g31"><div class="box n-stage">{lab("message thread · bubbles, timestamps, attachment")}{thread}</div>'
        f'<div class="box n-stage">{lab("description list · drop context")}<div class="card n-dlc t-ctxcard"><div class="t-ch"><img src="{PH["serum"]}" alt=""><div><b>Glow serum, 30 ml</b><span>Lumen Labs</span></div><span class="badge success">Live</span></div>{dl_h}</div></div></div>'
        f'<div class="n-gap"></div><div class="grid g2 n-top"><div class="n-col"><div class="box n-stage">{lab("divider variants")}{dv}</div><div class="box n-stage">{lab("swipe actions · right, left, idle")}{swipe}</div></div>'
        f'<div class="box n-stage">{lab("share sheet")}{share}</div></div>'
        f'<div class="n-gap"></div><div class="grid g2 n-top"><div class="box n-stage">{lab("empty with action · card")}{ea}</div><div class="box n-stage">{lab("empty with action · compact")}<div class="stack">{ea2}{ea3}</div></div></div>', "nw9")


def kit_new(theme="light"):
    return "".join([form_fields(theme), form_inputs(theme), flow_a(theme), flow_b(theme), feedback_a(theme), feedback_b(theme), content_a(theme), content_b(theme), content_c(theme)])
