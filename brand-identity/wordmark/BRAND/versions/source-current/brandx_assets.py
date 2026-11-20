# ---- brandx_assets.py: new identity assets (motifs, packaging, campaign, social, merch, events). exec'd inside brand.py ----
for _d in ("motifs", "packaging", "campaign", "merch", "events"): os.makedirs(os.path.join(A, _d), exist_ok=True)
MAR, VER = BRAND["marigold"], BRAND["vermilion"]
def tape_band(w, h, bg, fg, mode):
    lk = FN.lockup(mode, mono=fg, pad=0); lh = h*0.46; vw, vh = vb(lk)[2], vb(lk)[3]; lw = vw*lh/vh
    unit = lw + h*1.15; n = int(w // unit) + 2
    parts = "".join(place(lk, h*0.5 + i*unit, (h-lh)/2, h=lh)[0] for i in range(n))
    return f'<rect width="{w}" height="{h}" fill="{bg}"/><rect width="{w}" height="3" fill="#000" fill-opacity=".14"/><rect y="{h-3}" width="{w}" height="3" fill="#000" fill-opacity=".14"/>{parts}'
def tape_whole(w, h, bg, fg):
    """A band whose lockups repeat in whole units so it tiles seamlessly; fg is the lockup colour."""
    mode = "dark" if fg == "#ffffff" else "light"
    lk = FN.lockup(mode, mono=fg, pad=0); lh = h*0.46; vw, vh = vb(lk)[2], vb(lk)[3]; lw = vw*lh/vh
    unit = lw + h*1.15; n = max(1, round(w/unit)); w2 = n*unit
    parts = "".join(place(lk, h*0.55 + i*unit, (h-lh)/2, h=lh)[0] for i in range(n))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w2:.1f} {h}" width="{w2:.0f}" height="{h}"><rect width="{w2:.1f}" height="{h}" fill="{bg}"/>'
            f'<rect width="{w2:.1f}" height="3" fill="#000" fill-opacity=".12"/><rect y="{h-3}" width="{w2:.1f}" height="3" fill="#000" fill-opacity=".12"/>{parts}</svg>')
def hexp(cx, cy, s, fill, extra=""):
    return f'<path d="{FN.hexagon(cx, cy, s, s*0.16)}" fill="{fill}" {extra}/>'
def hex_photo(uid, name, cx, cy, s, crop=None, maxw=900, pos="xMidYMid"):
    c30 = math.cos(math.radians(30)); w_, h_ = 2*c30*s, 2*s
    return (f'<clipPath id="{uid}"><path d="{FN.hexagon(cx, cy, s, s*0.16)}"/></clipPath>'
            f'<image href="{photo_uri(name, maxw, crop=crop)}" x="{cx - w_/2:.1f}" y="{cy - h_/2:.1f}" width="{w_:.1f}" height="{h_:.1f}" preserveAspectRatio="{pos} slice" clip-path="url(#{uid})"/>')
def mono_mark(color, x, y, w, mode="dark"): return place(FN.square(mode, 100, 0.0, mono=color), x, y, w=w)[0]
def full_mark(x, y, w, theme="dark"): return place(FN.square(theme, 100, 0.0), x, y, w=w)[0]
def ill_at(n, th, x, y, w): return place(ILL[(n, th)], x, y, w=w)[0]
def T(text, cap, x, y, fill, wght=700, font="Bricolage", opsz=96, track=0.0, anchor="start"): return otext(text, cap, x, y, fill, wght, font, opsz, track, anchor)[0]
def TW(text, cap, wght=700, font="Bricolage", opsz=96, track=0.0): return otext(text, cap, 0, 0, "#000", wght, font, opsz, track)[1]
def PNG(path, svg, w): return save(path, svg, w)
MOT = os.path.join(A, "motifs"); PKG = os.path.join(A, "packaging"); CAMP = os.path.join(A, "campaign"); MERCH = os.path.join(A, "merch"); EVT = os.path.join(A, "events")

PAPER = "#ffffff"; HAIR = "#e8e8eb"
# ---------------------------------------------------------------- motifs
TAPE_INK = tape_whole(2400, 120, INK, "#ffffff"); TAPE_MAR = tape_whole(2400, 120, MAR, INK); TAPE_COB = tape_whole(2400, 120, COB, "#ffffff"); TAPE_VER = tape_whole(2400, 120, VER, INK)
for n, sv in (("cobalt", TAPE_COB), ("vermilion", TAPE_VER), ("ink", TAPE_INK), ("marigold", TAPE_MAR)): save(os.path.join(MOT, f"motif-tape-band-{n}.svg"), sv, 2400)
def hexagon_set():
    w, h = 1600, 400; parts = []
    for i, (fill, sub) in enumerate([(COB, "#ffffff"), (INK, "#ffffff"), (MAR, INK), (VER, INK)]):
        cx = 200 + i*400
        parts.append(hexp(cx, 200, 150, fill))
        parts.append(mono_mark(sub, cx - 72, 200 - 72, 144, "dark" if sub == "#ffffff" else "light"))
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="#ffffff"/>' + "".join(parts))
save(os.path.join(MOT, "motif-hexagon-set.svg"), hexagon_set(), 1600)
def hexagon_single(fill, name, glyph):
    s = svg_wrap(400, 400, hexp(200, 200, 190, fill) + mono_mark(glyph, 122, 122, 156, "dark" if glyph == "#ffffff" else "light"))
    save(os.path.join(MOT, f"motif-hexagon-{name}.svg"), s, 800)
for fill, name, glyph in ((COB, "cobalt", "#ffffff"), (INK, "ink", "#ffffff"), (MAR, "marigold", INK), (VER, "vermilion", INK)): hexagon_single(fill, name, glyph)
def label_motif():
    """The shipping label as a UI-and-print motif: a calm card, a small lockup, an ink tag, hairline rules, ink type and a code."""
    w, h = 800, 520; hair = HAIR
    lk, _, lh = place(LK_TIGHT_L, 40, 0, h=34); lk, _, _ = place(LK_TIGHT_L, 40, 38, h=34)
    tw_ = TW("PRIORITY · CREATOR DROP", 13, 600, "Geist", 12, 0.06) + 28
    tag = f'<rect x="{w - 40 - tw_:.1f}" y="40" width="{tw_:.1f}" height="32" rx="6" fill="{INK}"/>' + T("PRIORITY · CREATOR DROP", 13, w - 40 - tw_ + 14, 61, "#ffffff", 600, "Geist", track=0.06)
    body = (f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="20" fill="#fff" stroke="{hair}"/>' + lk + tag
            + f'<rect x="40" y="100" width="{w-80}" height="1" fill="{hair}"/>'
            + T("Ship to", 15, 40, 146, I[500], 600, "Geist") + T("Riya Sharma", 34, 40, 194, INK, 700, "Bricolage", 48, -0.02) + T("14 Park Street, Kolkata 700016", 21, 40, 232, I[700], 450, "Geist")
            + f'<rect x="40" y="266" width="{w-80}" height="1" fill="{hair}"/>'
            + T("Product", 15, 40, 310, I[500], 600, "Geist") + T("Glow serum, 30 ml", 21, 40, 346, INK, 600, "Geist")
            + T("Tracking", 15, 420, 310, I[500], 600, "Geist") + T("HD 0000 0000 0000", 21, 420, 346, INK, 600, "Geist")
            + f'<rect x="40" y="384" width="{w-80}" height="1" fill="{hair}"/>'
            + "".join(f'<rect x="{40 + i*12.5:.1f}" y="408" width="{[3,6,3,8,3,5,3,7][i % 8]}" height="72" fill="{INK}"/>' for i in range(0, 58)))
    return svg_wrap(w, h, body)
save(os.path.join(MOT, "motif-label.svg"), label_motif(), 800)
def motif_sheet():
    """One sheet: the four motifs, each on its own tile."""
    w, h = 1600, 480; g = 24; tw = (w - 3*g)/4; parts = []
    tiles = [(COB, "tape"), (I[50], "hex"), (I[50], "label"), (INK, "parcel")]
    for i, (bg, k) in enumerate(tiles):
        x = i*(tw + g); parts.append(f'<rect x="{x:.1f}" width="{tw:.1f}" height="{h}" rx="24" fill="{bg}"/>')
        cx = x + tw/2
        if k == "tape":
            parts.append(f'<clipPath id="mt"><rect x="{x:.1f}" width="{tw:.1f}" height="{h}" rx="24"/></clipPath><g clip-path="url(#mt)"><g transform="translate({x - 40:.1f} {h/2 - 58})">{tape_band(tw + 80, 116, INK, "#ffffff", "dark")}</g></g>')
        elif k == "hex": parts.append(hexp(cx, h/2, 150, COB) + mono_mark("#ffffff", cx - 70, h/2 - 70, 140))
        elif k == "label": parts.append(place(label_motif(), x + 22, h/2 - 130, w=tw - 44)[0])
        else: parts.append(ill_at("parcel", "dark", cx - 175, h/2 - 175, 350))
    return svg_wrap(w, h, "".join(parts))
MOTIF_SHEET = save(os.path.join(MOT, "motif-sheet.svg"), motif_sheet(), 1600)

# ---------------------------------------------------------------- social: LinkedIn banner, YouTube thumbnail
def linkedin_banner():
    w, h = 1584, 396
    pat = f'<g opacity=".5">{tiled(PAT_INK, w, h, pid="lib")}</g><rect width="{w}" height="{h}" fill="{INK}" fill-opacity=".62"/>'
    tape = f'<g transform="translate(0 {h - 74})">{tape_band(w, 74, COB, "#ffffff", "dark")}</g>'
    l1 = T("Products in.", 62, 420, 168, "#ffffff", 700, opsz=96, track=-0.01); l2 = T("Hype out.", 62, 420, 244, MAR, 700, opsz=96, track=-0.01)
    sub = T("Brands ship it. Creators try it. Everyone hears about it.", 24, 422, 298, I[300], 450, "Geist")
    ills = ill_at("tracking", "dark", 1090, 24, 210) + ill_at("review", "dark", 1280, 120, 190)
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{INK}"/>{pat}{ills}{l1}{l2}{sub}{tape}')
def youtube_thumb():
    w, h = 1280, 720
    photo = photo_rect("yt", "p6.jpg", 0, 0, w, h, 0, crop=(0.0, 0.0, 1, 1), maxw=1280, pos="xMidYMid")
    block = f'<rect x="0" y="0" width="760" height="{h}" fill="{INK}"/>'
    hx = hexp(130, 130, 62, COB) + mono_mark("#ffffff", 130 - 30, 130 - 30, 60)
    t1 = T("Honest review.", 66, 60, 400, "#ffffff", 700, opsz=96, track=-0.015); t2 = T("Worth it?", 66, 60, 486, MAR, 700, opsz=96, track=-0.015)
    sub = T("Glow serum, 30 ml", 38, 62, 570, I[200], 500, "Geist")
    tape = f'<rect x="0" y="{h - 24}" width="760" height="24" fill="{COB}"/>'
    edge = f'<rect x="760" y="0" width="12" height="{h}" fill="{MAR}"/>'
    return svg_wrap(w, h, f'{photo}{block}{edge}{hx}{t1}{t2}{sub}{tape}')
APPS3 = {"li": save(os.path.join(SOCIAL_DIR, "linkedin-banner-1584x396.svg"), linkedin_banner(), 1584),
         "yt": save(os.path.join(SOCIAL_DIR, "youtube-thumbnail-1280x720.svg"), youtube_thumb(), 1280)}

# ---------------------------------------------------------------- campaign key visuals (4:5 posters + 16:9 banner)
def kv_ink():
    w, h = 1080, 1350
    photo = photo_rect("kva", "p6.jpg", 64, 64, w - 128, 700, 36, crop=(0, 0, 1, 1), maxw=1000)
    ill = ill_at("parcel", "dark", 640, 520, 400)
    l1 = T("Products in.", 112, 64, 1000, "#ffffff", 700, opsz=96, track=-0.015); l2 = T("Hype out.", 112, 64, 1130, MAR, 700, opsz=96, track=-0.015)
    sub = T("Try it first. Say it straight.", 34, 66, 1196, I[300], 500, "Geist")
    tape = f'<g transform="translate(0 {h - 104})">{tape_band(w, 104, COB, "#ffffff", "dark")}</g>'
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{INK}"/>{photo}{ill}{l1}{l2}{sub}{tape}')
def kv_cobalt():
    w, h = 1080, 1350
    pat = f'<g opacity=".55">{tiled(PAT_COB, w, h, pid="kvc")}</g>'
    head1 = T("Try it first.", 104, 64, 190, "#ffffff", 700, opsz=96, track=-0.015); head2 = T("Say it straight.", 104, 64, 310, MAR, 700, opsz=96, track=-0.015)
    hx = hex_photo("kvh", "p5.jpg", 540, 800, 420, crop=(0, 0.02, 1, 0.98))
    ring = f'<path d="{FN.hexagon(540, 800, 438, 70)}" fill="none" stroke="#ffffff" stroke-width="10"/>'
    ill = ill_at("review", "light", 780, 940, 250)
    lk, _, _ = place(LK_TIGHT_W, 64, h - 100, w=250)
    cta = T("Join a drop at hypedrive.app", 28, w - 64, h - 62, "#ffffff", 600, "Geist", anchor="end")
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{COB}"/>{pat}{head1}{head2}{ring}{hx}{ill}{lk}{cta}')
def kv_marigold():
    w, h = 1080, 1350
    photo = photo_rect("kvm", "p3.jpg", 0, 0, w, 700, 0, crop=(0, 0.1, 1, 0.9), maxw=1080)
    tape = f'<g transform="translate(0 700)">{tape_band(w, 104, INK, "#ffffff", "dark")}</g>'
    l1 = T("Real products.", 92, 64, 960, INK, 700, opsz=96, track=-0.015); l2 = T("Honest reviews.", 92, 64, 1066, INK, 700, opsz=96, track=-0.015)
    sub = T("Paid fairly, within 48 hours.", 32, 66, 1140, I[800], 500, "Geist")
    ill = ill_at("payout", "light", 800, 1060, 210)
    lk, _, _ = place(LK_TIGHT_B, 64, h - 100, w=250)
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{MAR}"/>{photo}{tape}{ill}{l1}{l2}{sub}{lk}')
def kv_wide():
    w, h = 1920, 1080
    photo = photo_rect("kvw", "p7.jpg", 0, 0, 1080, h, 0, crop=(0, 0, 1, 1), maxw=1200, pos="xMidYMid")
    panel = f'<rect x="1080" width="{w - 1080}" height="{h}" fill="{INK}"/><rect x="1068" width="12" height="{h}" fill="{MAR}"/>'
    hx = hexp(1180, 200, 70, COB) + mono_mark("#ffffff", 1180 - 34, 200 - 34, 68)
    l = T("Products in.", 96, 1160, 500, "#ffffff", 700, opsz=96, track=-0.015) + T("Hype out.", 96, 1160, 624, MAR, 700, opsz=96, track=-0.015)
    sub = T("Try it first. Say it straight.", 34, 1162, 700, I[300], 500, "Geist")
    ill = ill_at("parcel", "dark", 1500, 760, 360)
    tape = f'<g transform="translate(0 {h - 96})">{tape_band(w, 96, COB, "#ffffff", "dark")}</g>'
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{INK}"/>{photo}{panel}{hx}{l}{sub}{ill}{tape}')
KV = {k: save(os.path.join(CAMP, f"key-visual-{k}.svg"), fn(), 1080 if k != "wide" else 1920) for k, fn in (("ink", kv_ink), ("cobalt", kv_cobalt), ("marigold", kv_marigold), ("wide", kv_wide))}
def kv_paper_hexagon():
    """Paper poster: warm canvas, ink type, the hexagon photo. Cobalt only on the one action."""
    w, h = 1080, 1350
    head1 = T("Try it first.", 104, 64, 190, INK, 700, "Bricolage", 96, -0.02); head2 = T("Say it straight.", 104, 64, 310, INK, 700, "Bricolage", 96, -0.02)
    hx = hex_photo("kvh", "p5.jpg", 540, 780, 400, crop=(0, 0.02, 1, 0.98))
    ill = ill_at("review", "light", 780, 910, 230)
    lk, _, _ = place(LK_TIGHT_B, 64, h - 108, w=230)
    cta_w = TW("Join a drop", 28, 600, "Geist") + 64
    cta = f'<rect x="{w - 64 - cta_w:.1f}" y="{h - 122}" width="{cta_w:.1f}" height="64" rx="14" fill="{COB}"/>' + T("Join a drop", 28, w - 64 - cta_w + 32, h - 80, "#ffffff", 600, "Geist")
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{PAPER}"/>{head1}{head2}{hx}{ill}{lk}{cta}')
def kv_paper_photo():
    """Paper poster: the full-bleed photo above, ink type below."""
    w, h = 1080, 1350
    photo = photo_rect("kvm", "p3.jpg", 0, 0, w, 760, 0, crop=(0, 0.1, 1, 0.9), maxw=1080)
    l1 = T("Real products.", 92, 64, 1000, INK, 700, "Bricolage", 96, -0.02); l2 = T("Honest reviews.", 92, 64, 1120, INK, 700, "Bricolage", 96, -0.02)
    sub = T("Paid fairly, within 48 hours.", 32, 66, 1196, I[700], 500, "Geist")
    lk, _, _ = place(LK_TIGHT_B, 64, h - 80, w=210)
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{PAPER}"/>{photo}{l1}{l2}{sub}{lk}')
def kv_wide():
    w, h = 1920, 1080
    photo = photo_rect("kvw", "p7.jpg", 0, 0, 1080, h, 0, crop=(0, 0, 1, 1), maxw=1200, pos="xMidYMid")
    panel = f'<rect x="1080" width="{w - 1080}" height="{h}" fill="{INK}"/>'
    hx = hexp(1180, 200, 70, "#ffffff") + mono_mark(INK, 1180 - 34, 200 - 34, 68, "light")
    l = T("Products in.", 96, 1160, 500, "#ffffff", 700, opsz=96, track=-0.015) + T("Hype out.", 96, 1160, 624, MAR, 700, opsz=96, track=-0.015)
    sub = T("Try it first. Say it straight.", 34, 1162, 700, I[300], 500, "Geist")
    ill = ill_at("parcel", "dark", 1500, 760, 360)
    tape = ""
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{INK}"/>{photo}{panel}{hx}{l}{sub}{ill}{tape}')
def kv_cobalt_orig():
    w, h = 1080, 1350
    pat = f'<g opacity=".55">{tiled(PAT_COB, w, h, pid="kvc")}</g>'
    head1 = T("Try it first.", 104, 64, 190, "#ffffff", 700, opsz=96, track=-0.015); head2 = T("Say it straight.", 104, 64, 310, MAR, 700, opsz=96, track=-0.015)
    hx = hex_photo("kvh", "p5.jpg", 540, 800, 420, crop=(0, 0.02, 1, 0.98))
    ring = f'<path d="{FN.hexagon(540, 800, 438, 70)}" fill="none" stroke="#ffffff" stroke-width="10"/>'
    ill = ill_at("review", "light", 780, 940, 250)
    lk, _, _ = place(LK_TIGHT_W, 64, h - 100, w=250)
    cta = T("Join a drop at hypedrive.app", 28, w - 64, h - 62, "#ffffff", 600, "Geist", anchor="end")
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{COB}"/>{pat}{head1}{head2}{ring}{hx}{ill}{lk}{cta}')
def kv_marigold_orig():
    w, h = 1080, 1350
    photo = photo_rect("kvm", "p3.jpg", 0, 0, w, 700, 0, crop=(0, 0.1, 1, 0.9), maxw=1080)
    tape = f'<g transform="translate(0 700)">{tape_band(w, 104, INK, "#ffffff", "dark")}</g>'
    l1 = T("Real products.", 92, 64, 960, INK, 700, opsz=96, track=-0.015); l2 = T("Honest reviews.", 92, 64, 1066, INK, 700, opsz=96, track=-0.015)
    sub = T("Paid fairly, within 48 hours.", 32, 66, 1140, I[800], 500, "Geist")
    ill = ill_at("payout", "light", 800, 1060, 210)
    lk, _, _ = place(LK_TIGHT_B, 64, h - 100, w=250)
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{MAR}"/>{photo}{tape}{ill}{l1}{l2}{sub}{lk}')
save(os.path.join(CAMP, "key-visual-paper-hexagon.svg"), kv_paper_hexagon(), 1080)
save(os.path.join(CAMP, "key-visual-paper-photo.svg"), kv_paper_photo(), 1080)

# ---------------------------------------------------------------- packaging
def isoP(x, y, z, ox, oy, k=1.0):
    c, s = math.cos(math.radians(30)), 0.5
    return (ox + (x - y)*c*k, oy + (x + y)*s*k - z*k)
def box_iso(ox, oy, L, Wd, Hh, k, tape_col=COB, fills=(I[50], I[100], I[200]), edge=I[300], label=True):
    """An isometric shipper box: L along x (to lower right), Wd along y (to lower left), Hh up. Tape over the lid and down the front, label on the right face."""
    P = lambda x, y, z: isoP(x, y, z, ox, oy, k)
    f = lambda pts: " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
    top = [P(0, 0, Hh), P(L, 0, Hh), P(L, Wd, Hh), P(0, Wd, Hh)]
    left = [P(0, Wd, Hh), P(L, Wd, Hh), P(L, Wd, 0), P(0, Wd, 0)]       # front-left face (along x)
    right = [P(L, 0, Hh), P(L, Wd, Hh), P(L, Wd, 0), P(L, 0, 0)]        # right face (along y)
    out = [f'<polygon points="{f(top)}" fill="{fills[0]}" stroke="{edge}" stroke-width="2" stroke-linejoin="round"/>',
           f'<polygon points="{f(left)}" fill="{fills[1]}" stroke="{edge}" stroke-width="2" stroke-linejoin="round"/>',
           f'<polygon points="{f(right)}" fill="{fills[2]}" stroke="{edge}" stroke-width="2" stroke-linejoin="round"/>']
    tw = Wd*0.17; y0, y1 = Wd/2 - tw/2, Wd/2 + tw/2           # tape runs along x over the lid, down the right face
    tp = [P(0, y0, Hh), P(L, y0, Hh), P(L, y1, Hh), P(0, y1, Hh)]
    drop = Hh*0.46
    rf = [P(L, y0, Hh), P(L, y1, Hh), P(L, y1, Hh - drop), P(L, y0, Hh - drop)]
    out.append(f'<polygon points="{f(tp)}" fill="{tape_col}"/><polygon points="{f(rf)}" fill="{tape_col}" fill-opacity=".82"/>')
    if label:
        a, b = Wd*0.08, Wd*0.5 - tw/2 - Wd*0.02     # label sits on the right face, to the left of the tape
        zl0, zl1 = Hh*0.1, Hh*0.5
        lb = [P(L, a, zl1), P(L, b, zl1), P(L, b, zl0), P(L, a, zl0)]
        out.append(f'<polygon points="{f(lb)}" fill="#fff" stroke="{I[300]}" stroke-width="1.5"/>')
        out += [f'<line x1="{P(L, a + (b - a)*0.12, zl1 - (zl1 - zl0)*q)[0]:.1f}" y1="{P(L, a + (b - a)*0.12, zl1 - (zl1 - zl0)*q)[1]:.1f}" x2="{P(L, a + (b - a)*0.88, zl1 - (zl1 - zl0)*q)[0]:.1f}" y2="{P(L, a + (b - a)*0.88, zl1 - (zl1 - zl0)*q)[1]:.1f}" stroke="{I[400]}" stroke-width="3" stroke-linecap="round"/>' for q in (0.25, 0.45, 0.65)]
    return "".join(out)
BOXES = [("Small", 180, 130, 60, "S", 1.5), ("Medium", 260, 190, 90, "M", 1.5), ("Large", 340, 260, 130, "L", 1.5)]
def box_system():
    w, h = 1600, 560; parts = [f'<rect width="{w}" height="{h}" fill="#fff"/>']
    k = 1.0; c = math.cos(math.radians(30))
    for i, (nm, L, Wd, Hh, cc, _) in enumerate(BOXES):
        cx = 250 + i*500
        ox = cx - (L - Wd)*c*k/2; oy = 470 - (L + Wd)*0.5*k
        parts.append(box_iso(ox, oy, L, Wd, Hh, k))
        parts.append(T(f"{nm}  ·  {L} x {Wd} x {Hh} mm", 22, cx, 520, INK, 600, "Geist", anchor="middle"))
    # callouts on the large box
    L, Wd, Hh = BOXES[2][1:4]; ox = 1250 - (L - Wd)*c*k/2; oy = 470 - (L + Wd)*0.5*k
    px, py = isoP(L*0.3, Wd/2, Hh, ox, oy, k); parts.append(f'<line x1="{px:.0f}" y1="{py:.0f}" x2="{px:.0f}" y2="{py - 96:.0f}" stroke="{INK}" stroke-width="2"/><circle cx="{px:.0f}" cy="{py:.0f}" r="5" fill="{INK}"/>' + T("Tape runs over the lid and down the side", 22, px, py - 110, INK, 600, "Geist", anchor="middle"))
    qx, qy = isoP(L, Wd*0.25, Hh*0.3, ox, oy, k); parts.append(f'<line x1="{qx:.0f}" y1="{qy:.0f}" x2="{qx + 40:.0f}" y2="{qy + 50:.0f}" stroke="{INK}" stroke-width="2"/><circle cx="{qx:.0f}" cy="{qy:.0f}" r="5" fill="{INK}"/>' + T("Label", 22, qx + 20, qy + 84, INK, 600, "Geist"))
    return svg_wrap(w, h, "".join(parts))
def mailer_svg():
    w, h = 700, 900
    body = (f'<rect x="20" y="20" width="{w - 40}" height="{h - 40}" rx="36" fill="{INK}"/>'
            f'<rect x="20" y="20" width="{w - 40}" height="150" rx="36" fill="{COB}"/><rect x="20" y="130" width="{w - 40}" height="40" fill="{COB}"/>'
            f'<rect x="20" y="168" width="{w - 40}" height="3" fill="#000" fill-opacity=".2"/>'
            + T("Peel and press", 28, w/2, 118, "#ffffff", 600, "Geist", anchor="middle")
            + full_mark(w/2 - 150, 270, 300)
            + place(LK_TIGHT_W, w/2 - 190, 640, w=380)[0]
            + T("Your drop is inside.", 44, w/2, 760, MAR, 700, opsz=48, anchor="middle")
            + T("Try it first. Say it straight.", 26, w/2, 810, I[300], 450, "Geist", anchor="middle")
            + f'<rect x="{w - 250}" y="{h - 340}" width="170" height="0" fill="none"/>')
    return svg_wrap(w, h, body)
def thanks_card_front():
    w, h = 1480, 1050     # A6 landscape ratio, 148 x 105
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" rx="36" fill="{MAR}"/>' + ill_at("gift", "light", 860, 130, 560)
                    + T("Thanks for", 110, 90, 320, INK, 700, opsz=96, track=-0.015) + T("trying it", 110, 90, 480, INK, 700, opsz=96, track=-0.015) + T("first.", 110, 90, 640, INK, 700, opsz=96, track=-0.015)
                    + place(LK_TIGHT_B, 90, h - 150, w=300)[0])
def thanks_card_back():
    w, h = 1480, 1050
    body = f'<rect width="{w}" height="{h}" rx="36" fill="#fff" stroke="{I[200]}" stroke-width="3"/>' + place(LK_TIGHT_L, 90, 90, w=300)[0]
    body += T("Say what you really think.", 64, 90, 330, INK, 700, opsz=72, track=-0.01)
    lines = ["Your review is the whole point of the drop.", "Post it on Instagram or YouTube, add the review link", "in the Hypedrive app, and your payout follows once", "the brand approves it."]
    body += "".join(T(t, 34, 92, 430 + i*56, I[700], 400, "Geist") for i, t in enumerate(lines))
    body += f'<rect x="90" y="{h - 210}" width="{w - 180}" height="3" fill="{I[200]}"/>' + T("Questions about your drop?", 30, 90, h - 140, INK, 600, "Geist") + T("support@hypedrive.app", 30, 90, h - 90, COB, 600, "Geist")
    body += f'<rect x="{w - 56}" y="0" width="56" height="{h}" fill="{COB}"/><rect x="{w - 56}" y="0" width="56" height="{h/3}" fill="{MAR}"/><rect x="{w - 56}" y="{2*h/3}" width="56" height="{h/3}" fill="{VER}"/>'
    return svg_wrap(w, h, f'<clipPath id="tcb"><rect width="{w}" height="{h}" rx="36"/></clipPath><g clip-path="url(#tcb)">{body}</g>')
def sticker_sheet():
    w, h = 1600, 640; parts = [f'<rect width="{w}" height="{h}" fill="{I[100]}"/>']
    shadow = lambda inner: inner
    def die(path_or_circle, fill):  # a white kiss-cut border behind the sticker
        return path_or_circle
    # 1 round parcel sticker
    cx = 210; parts.append(f'<circle cx="{cx}" cy="320" r="190" fill="#fff"/><circle cx="{cx}" cy="320" r="172" fill="{INK}"/>' + full_mark(cx - 100, 220, 200))
    # 2 hexagon sticker
    cx = 590; parts.append(hexp(cx, 320, 200, "#fff") + hexp(cx, 320, 178, COB) + mono_mark("#ffffff", cx - 90, 230, 180))
    # 3 line sticker (rounded rect)
    x0 = 810; parts.append(f'<rect x="{x0}" y="210" width="400" height="220" rx="52" fill="#fff"/><rect x="{x0 + 16}" y="226" width="368" height="188" rx="38" fill="{MAR}"/>'
                           + T("Products in.", 44, x0 + 200, 322, INK, 700, opsz=72, anchor="middle") + T("Hype out.", 44, x0 + 200, 384, INK, 700, opsz=72, anchor="middle"))
    # 4 tape-label sticker
    x1 = 1300; parts.append(f'<rect x="{x1 - 40}" y="150" width="300" height="340" rx="44" fill="#fff"/><rect x="{x1 - 24}" y="166" width="268" height="308" rx="30" fill="{VER}"/>' + ill_at("gift", "light", x1 - 4, 196, 228)
                            + T("Try it first.", 30, x1 + 110, 450, INK, 700, opsz=48, anchor="middle"))
    return svg_wrap(w, h, "".join(parts))
PKG_ASSETS = {"boxes": save(os.path.join(PKG, "box-system.svg"), box_system(), 1600), "mailer": save(os.path.join(PKG, "mailer-front.svg"), mailer_svg(), 700),
              "card_f": save(os.path.join(PKG, "thank-you-card-front.svg"), thanks_card_front(), 1480), "card_b": save(os.path.join(PKG, "thank-you-card-back.svg"), thanks_card_back(), 1480),
              "stickers": save(os.path.join(PKG, "sticker-sheet.svg"), sticker_sheet(), 1600)}

# ---------------------------------------------------------------- merch: tee and tote
TEE_BODY = ("M214 44 Q300 112 386 44 L478 78 Q548 104 592 168 L536 262 L468 226 L468 612 Q468 624 456 624 L144 624 Q132 624 132 612 L132 226 L64 262 L8 168 Q52 104 122 78 Z")
def tee_svg(fill, print_kind, edge_col):
    w, h = 600, 660
    shade = f'<path d="{TEE_BODY}" fill="#000" fill-opacity=".0"/>'
    collar = f'<path d="M214 44 Q300 112 386 44" fill="none" stroke="{edge_col}" stroke-width="16" stroke-linecap="round"/>'
    seams = f'<path d="M132 226 Q150 150 122 78 M468 226 Q450 150 478 78" fill="none" stroke="{edge_col}" stroke-width="3" stroke-opacity=".7"/>'
    hem = f'<path d="M136 604 L464 604" stroke="{edge_col}" stroke-width="3" stroke-opacity=".7"/>'
    if print_kind == "chest-mono":
        pr = place(LK_TIGHT_W, 316, 170, w=130)[0]
    elif print_kind == "centre-colour":
        pr = full_mark(190, 190, 220)
    else:
        pr = mono_mark(INK, 220, 170, 160, "light")
    body = f'<path d="{TEE_BODY}" fill="{fill}" stroke="{edge_col}" stroke-width="3" stroke-linejoin="round"/>'
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="none"/>{body}{seams}{collar}{hem}{pr}')
def tote_svg(fill, print_kind, edge_col):
    w, h = 600, 740
    hand = f'<path d="M190 190 Q190 30 300 30 Q410 30 410 190" fill="none" stroke="{fill}" stroke-width="30" stroke-linecap="round"/><path d="M190 190 Q190 30 300 30 Q410 30 410 190" fill="none" stroke="{edge_col}" stroke-width="3" transform="translate(0 -15)" stroke-opacity="0"/>'
    body = f'<path d="M70 180 L530 180 L548 700 Q548 716 532 716 L68 716 Q52 716 52 700 Z" fill="{fill}" stroke="{edge_col}" stroke-width="3" stroke-linejoin="round"/>'
    top = f'<path d="M76 214 L524 214" stroke="{edge_col}" stroke-width="3" stroke-opacity=".7"/>'
    if print_kind == "colour": pr = full_mark(190, 330, 220) + place(LK_TIGHT_B, 190, 590, w=220)[0]
    else: pr = mono_mark("#ffffff", 190, 330, 220) + place(LK_TIGHT_W, 190, 590, w=220)[0]
    return svg_wrap(w, h, f'{hand}{body}{top}{pr}')
MERCH_A = {"tee_ink": save(os.path.join(MERCH, "tee-ink-chest.svg"), tee_svg(INK, "chest-mono", I[700]), 900),
           "tee_paper": save(os.path.join(MERCH, "tee-paper-parcel.svg"), tee_svg("#ffffff", "centre-colour", I[300]), 900),
           "tee_cobalt": save(os.path.join(MERCH, "tee-cobalt-mark.svg"), tee_svg(COB, "centre-mono", C[700]), 900),
           "tote_nat": save(os.path.join(MERCH, "tote-natural.svg"), tote_svg(SCALES["marigold"][100], "colour", SCALES["marigold"][300]), 900),
           "tote_ink": save(os.path.join(MERCH, "tote-ink.svg"), tote_svg(INK, "mono", I[700]), 900)}
# the cobalt tee print is a white mark, not Ink
MERCH_A["tee_cobalt"] = save(os.path.join(MERCH, "tee-cobalt-mark.svg"), tee_svg(COB, "centre-mono", C[700]).replace(f'fill="{INK}"', 'fill="#ffffff"'), 900)

# ---------------------------------------------------------------- event: booth layout
def booth_svg():
    w, h = 1600, 900; m = 260                                   # 1 m = 260 px
    floor = f'<rect width="{w}" height="{h}" fill="{I[100]}"/><rect y="720" width="{w}" height="180" fill="{I[200]}"/>'
    wx, ww, wh = 410, 780, 624; wy = 720 - wh
    wall = (f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="{INK}"/>'
            f'<clipPath id="bw"><rect x="{wx}" y="{wy}" width="{ww}" height="{wh}"/></clipPath><g clip-path="url(#bw)" opacity=".6">{tiled(PAT_INK, w, h, 0, 0, "bwp")}</g>'
            + ill_at("parcel", "dark", 930, wy + 30, 220)
            + T("Products in.", 60, wx + 44, wy + 120, "#ffffff", 700, opsz=96, track=-0.015) + T("Hype out.", 60, wx + 44, wy + 190, MAR, 700, opsz=96, track=-0.015)
            + T("Try it first. Say it straight.", 24, wx + 46, wy + 236, I[300], 500, "Geist")
            + f'<g clip-path="url(#bw)"><g transform="translate({wx} {wy + 270})">{tape_band(ww, 70, COB, "#ffffff", "dark")}</g></g>')
    cw, ch = round(1.8*m), round(0.9*m); cx0 = wx + (ww - cw)//2
    counter = (f'<rect x="{cx0}" y="{720 - ch}" width="{cw}" height="{ch}" fill="{COB}"/><rect x="{cx0 - 12}" y="{720 - ch - 18}" width="{cw + 24}" height="18" rx="5" fill="#fff" stroke="{I[300]}" stroke-width="2"/>'
               + place(LK_TIGHT_W, cx0 + 74, 720 - ch + 54, w=320)[0] + T("Join a drop", 26, cx0 + cw/2, 720 - 36, C[100], 600, "Geist", anchor="middle"))
    rw, rh = round(0.85*m), round(2.0*m)
    def rollup(x):
        y = 720 - rh
        return (f'<rect x="{x}" y="{y}" width="{rw}" height="{rh}" fill="{MAR}"/><rect x="{x - 8}" y="{720 - 16}" width="{rw + 16}" height="16" rx="5" fill="{I[700]}"/>'
                + ill_at("review", "light", x + 36, y + 40, rw - 72) + T("Real", 34, x + rw/2, y + 300, INK, 700, opsz=48, anchor="middle") + T("reviews.", 34, x + rw/2, y + 346, INK, 700, opsz=48, anchor="middle")
                + mono_mark(INK, x + rw/2 - 30, y + rh - 110, 60, "light"))
    def dim(x0, x1, y, label):
        return (f'<g stroke="{I[600]}" stroke-width="2"><line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}"/><line x1="{x0}" y1="{y - 9}" x2="{x0}" y2="{y + 9}"/><line x1="{x1}" y1="{y - 9}" x2="{x1}" y2="{y + 9}"/></g>'
                + T(label, 20, (x0 + x1)/2, y + 34, I[700], 600, "Geist", anchor="middle"))
    dims = dim(wx, wx + ww, 790, "Backdrop 3.0 m wide, 2.4 m high") + dim(120, 120 + rw, 790, "Roll-up 0.85 x 2.0 m") + dim(cx0, cx0 + cw, 850, "Counter 1.8 m wide")
    return svg_wrap(w, h, floor + wall + counter + rollup(120) + rollup(1259) + dims + dim(1259, 1259 + rw, 790, "Roll-up 0.85 x 2.0 m"))
EVENT = save(os.path.join(EVT, "booth-layout.svg"), booth_svg(), 1600)
