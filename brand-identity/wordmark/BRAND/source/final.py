"""Hypedrive — final logo system (signature parcel + Bricolage wordmark)."""
import sys, os, re, math, subprocess, json
sys.path.insert(0, "/tmp/hdwm")
from isofam import Ctx, box, P, C30, S30, SIGNATURE, SOLID, rpoly, silhouette, pts
import optical as OPT
import palette as PL

# ---- wordmark metrics (Bricolage Grotesque, opsz 96, wdth 100, wght 700)
AX, WG, CAP = {"opsz": 96, "wdth": 100}, 700, 18.6
K = CAP / 660                               # px per font unit
BASE = 22.9
ASC, DESC = 695*K, 154*K                    # 'd' ascender top, 'y' descender bottom
H_LSB = 43*K
SPACING = dict(strength=0.75, extra=0.012)
SOFT = 0.3
OVERSHOOT = 1.05                            # solid shapes read smaller than type; 5% overshoot
MARK_H = (ASC + DESC) * OVERSHOOT
MARK_CY = BASE - (ASC - DESC) / 2           # centred on the ascender–descender span
GAP = 0.5 * CAP - H_LSB                     # visual gap mark→H stem = half the cap height

# ---- the parcel
W = D = H = 10.0
TAPE_HALF = 0.118; TAPE_DROP = 0.46
R_MARK = 1.45                               # outer corner radius (iso units)

def parcel(c, detail="full"):
    """detail: full (tape + dot + rim light), small (tape only, thicker), tiny (bare faces)."""
    t = SOLID[c.theme]
    deco = ""
    if detail == "full":                        # rim light along the lid's two front edges
        rim = PL.ramp(.97, .97, .08, .08, 95, 95)[0]
        deco += (f'<polyline fill="none" stroke="{rim}" stroke-opacity=".75" stroke-width="0.32" stroke-linejoin="round" '
                 f'points="{pts((0, D, H), (W, D, H), (W, 0, H))}"/>')
    if detail in ("full", "small"):
        half = D * (TAPE_HALF if detail == "full" else 0.15); m = D/2
        deco += (f'<polygon fill="{t["tape"][0]}" points="{pts((-1,m-half,H),(W,m-half,H),(W,m+half,H),(-1,m+half,H))}"/>'
                 f'<path fill="{t["tape"][1]}" d="{rpoly([P(W,m-half,H),P(W,m+half,H),P(W,m+half,H*(1-TAPE_DROP)),P(W,m-half,H*(1-TAPE_DROP))], [0.01,0.01,0.22,0.22])}"/>')
    o = box(c, 0, 0, 0, W, D, H, SIGNATURE, deco, r=R_MARK)
    if detail == "full":
        cx, cy = P(3.1, D, 4.6)
        o += f'<circle cx="{cx:.3f}" cy="{cy:.3f}" r="1.05" fill="{t["dot"]}"/>'
    return o

def parcel_mono(c, colour):
    """True one-colour mark built from plain geometry (no masks — they break in some PDF viewers):
    three faces separated by seam gaps, the tape as a real notch, the label dot as an even-odd hole."""
    sil = silhouette(0, 0, 0, W, D, H); c.pts += sil
    g = 0.5                                   # seam gap, iso units
    m = D/2; half = D*TAPE_HALF; zt = H*(1-TAPE_DROP)
    def poly(p3): return rpoly([P(*p) for p in p3], 0.16)
    top_a = poly([(0, 0, H), (W-g, 0, H), (W-g, m-half, H), (0, m-half, H)])
    top_b = poly([(0, m+half, H), (W-g, m+half, H), (W-g, D-g, H), (0, D-g, H)])
    left = poly([(0, D, 0), (W-g, D, 0), (W-g, D, H-g), (0, D, H-g)])
    right = poly([(W, 0, 0), (W, D-g, 0), (W, D-g, H-g), (W, m+half, H-g), (W, m+half, zt), (W, m-half, zt), (W, m-half, H-g), (W, 0, H-g)])
    cx, cy = P(3.1, D, 4.6); r = 1.05
    dot = f"M{cx-r:.3f} {cy:.3f}a{r} {r} 0 1 0 {2*r} 0a{r} {r} 0 1 0 {-2*r} 0Z"
    cid = c.clip(rpoly(sil, R_MARK))
    return (f'<g clip-path="url(#{cid})"><path fill="{colour}" d="{top_a}{top_b}{right}"/>'
            f'<path fill="{colour}" fill-rule="evenodd" d="{left}{dot}"/></g>')

def mark(theme, height, detail="full", mono=None):
    c = Ctx(theme)
    body = parcel_mono(c, mono) if mono else parcel(c, detail)
    xs = [p[0] for p in c.pts]; ys = [p[1] for p in c.pts]
    x0, y0, x1, y1 = min(xs), min(ys), max(xs), max(ys); k = height/(y1-y0)
    return f'<defs>{"".join(c.defs)}</defs><g transform="scale({k:.5f}) translate({-x0:.3f} {-y0:.3f})">{body}</g>', (x1-x0)*k

TITTLE = "hex"                              # the i's dot is the parcel's silhouette
I_DOT = (24, 570, 197, 709)                 # Bricolage i-dot bbox at wdth 100 (font units)
def hexagon(cx, cy, s, r):
    c30 = math.cos(math.radians(30))
    p = [(cx, cy-s), (cx+c30*s, cy-s/2), (cx+c30*s, cy+s/2), (cx, cy+s), (cx-c30*s, cy+s/2), (cx-c30*s, cy-s/2)]
    return rpoly(p, r)

def wordmark_path():
    text = "Hypedr\u0131ve" if TITTLE == "hex" else "Hypedrive"
    d, tw, report, pos = OPT.optical_text_path(text, WG, CAP, "Bricolage", AX, positions=True, **SPACING)
    if TITTLE == "hex":
        x0, y0, x1, y1 = I_DOT
        gx = [x for n, x, a in pos if n == "dotlessi"][0]
        s = 84*K                                        # 5% larger than the round dot reads optically
        d += hexagon(gx + (x0+x1)/2*K, -((y0+y1)/2 + 6)*K, s, s*0.16)
    return d, tw, report

def lockup(theme, mono=None, pad=None):
    ink = mono or SOLID[theme]["ink"]
    m, mw = mark(theme, MARK_H, mono=mono)
    d, tw, _ = wordmark_path()
    top = MARK_CY - MARK_H/2
    ox = mw + GAP; Wd = ox + tw + SOFT
    pad = CAP*0.5 if pad is None else pad                   # clear space = half the cap height
    y0 = min(top, BASE-ASC) - pad; y1 = max(top+MARK_H, BASE+DESC) + pad
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad:.2f} {y0:.2f} {Wd+2*pad:.2f} {y1-y0:.2f}" '
            f'width="{(Wd+2*pad)*10:.0f}" height="{(y1-y0)*10:.0f}">'
            f'<g transform="translate(0 {top:.3f})">{m}</g>'
            f'<path fill="{ink}" stroke="{ink}" stroke-width="{SOFT}" stroke-linejoin="round" transform="translate({ox:.3f} {BASE})" d="{d}"/></svg>')

def lockup_stacked(theme, mono=None):
    ink = mono or SOLID[theme]["ink"]
    mh = CAP*2.05
    m, mw = mark(theme, mh, mono=mono)
    d, tw, _ = wordmark_path()
    W = max(mw, tw); base = mh + CAP*0.62 + ASC; H = base + DESC; pad = CAP*0.5
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad:.2f} {-pad:.2f} {W+2*pad:.2f} {H+2*pad:.2f}" width="{(W+2*pad)*10:.0f}" height="{(H+2*pad)*10:.0f}">'
            f'<g transform="translate({(W-mw)/2:.3f} 0)">{m}</g>'
            f'<path fill="{ink}" stroke="{ink}" stroke-width="{SOFT}" stroke-linejoin="round" transform="translate({(W-tw)/2:.3f} {base:.3f})" d="{d}"/></svg>')

def wordmark_only(theme, mono=None):
    ink = mono or SOLID[theme]["ink"]; d, tw, _ = wordmark_path(); pad = CAP*0.5
    y0 = BASE-ASC-pad; y1 = BASE+DESC+pad
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad:.2f} {y0:.2f} {tw+SOFT+2*pad:.2f} {y1-y0:.2f}" width="{(tw+2*pad)*10:.0f}" height="{(y1-y0)*10:.0f}">'
            f'<path fill="{ink}" stroke="{ink}" stroke-width="{SOFT}" stroke-linejoin="round" transform="translate(0 {BASE})" d="{d}"/></svg>')

def square(theme, size, pad=0.1, tile=None, detail="full", mono=None, tile_rx=0.225):
    s = 100.0; inner = s*(1-2*pad)
    m, mw = mark(theme, inner, detail, mono)
    bg = f'<rect width="{s}" height="{s}" rx="{s*tile_rx}" fill="{tile}"/>' if tile else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}" width="{size}" height="{size}">{bg}'
            f'<g transform="translate({(s-mw)/2:.3f} {(s-inner)/2:.3f})">{m}</g></svg>')

ASPECT = 2*math.cos(math.radians(30))*W / ((W + D)*0.5 + H)     # silhouette width / height

def favicon(size, half_px, detail):
    """Pixel-snapped favicon: the cube's three vertical edges land exactly on whole pixels."""
    w = 2*half_px; h = w/ASPECT
    m, mw = mark("light", h, detail)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}" shape-rendering="geometricPrecision">'
            f'<g transform="translate({(size-w)/2:.4f} {(size-h)/2:.4f})">{m}</g></svg>')

def squircle(s, n=5.0, steps=160):
    """Superellipse tile (|x|^n + |y|^n = 1): the continuous-curvature app-icon shape."""
    h = s/2; out = []
    for i in range(steps):
        t = 2*math.pi*i/steps; c, sn = math.cos(t), math.sin(t)
        x = h + h*math.copysign(abs(c)**(2/n), c); y = h + h*math.copysign(abs(sn)**(2/n), sn)
        out.append(f"{x:.3f} {y:.3f}")
    return "M" + "L".join(out) + "Z"

def app_icon(theme, size=1024, tile="ink", rounded=True, mono=None):
    """App icon tile: soft top-lit gradient, parcel at 60%, grounded with a contact shadow (no filters)."""
    s = 100.0; inner = 60.0
    m, mw = mark(theme, inner, mono=mono)
    tones = {"ink": ("#24262c", "#0f1013"), "cobalt": ("#3b74ff", "#1d43d6"), "paper": ("#ffffff", "#eef0f4")}[tile]
    tile_d = rpoly([(0, 0), (s, 0), (s, s), (0, s)], s*0.19, smooth=0.6) if rounded else f"M0 0H{s}V{s}H0Z"
    ox = (s-mw)/2; oy = (s-inner)/2 - 1.5
    sh_op = .38 if tile != "paper" else .16
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}" width="{size}" height="{size}">'
            f'<defs><linearGradient id="tg" x1="0" y1="0" x2="0" y2="1"><stop stop-color="{tones[0]}"/><stop offset="1" stop-color="{tones[1]}"/></linearGradient>'
            f'<radialGradient id="cs" cx=".5" cy=".5" r=".5"><stop stop-color="#000" stop-opacity="{sh_op}"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient></defs>'
            f'<path d="{tile_d}" fill="url(#tg)"/>'
            f'<ellipse cx="50" cy="{oy+inner+0.8:.2f}" rx="{mw*0.44:.2f}" ry="{mw*0.075:.2f}" fill="url(#cs)"/>'
            f'<g transform="translate({ox:.3f} {oy:.3f})">{m}</g></svg>')

if __name__ == "__main__":
    out = sys.argv[1]
    dirs = {k: os.path.join(out, k) for k in ("lockup", "mark", "wordmark", "app-icon", "favicon")}
    for p in dirs.values(): os.makedirs(p, exist_ok=True)
    def save(dir_, name, svg, w=None, h=None):
        p = os.path.join(dirs[dir_], name + ".svg"); open(p, "w").write(svg)
        args = ["rsvg-convert", p, "-o", p[:-4] + ".png"]
        if w: args[1:1] = ["-w", str(w)]
        if h: args[1:1] = ["-h", str(h)]
        subprocess.run(args, check=True)
    ink = SOLID["light"]["ink"]
    save("lockup", "hypedrive-lockup-color-light", lockup("light"), h=600)
    save("lockup", "hypedrive-lockup-color-dark", lockup("dark"), h=600)
    save("lockup", "hypedrive-lockup-mono-black", lockup("light", mono=ink), h=600)
    save("lockup", "hypedrive-lockup-mono-white", lockup("dark", mono="#ffffff"), h=600)
    save("lockup", "hypedrive-lockup-stacked-color-light", lockup_stacked("light"), h=800)
    save("lockup", "hypedrive-lockup-stacked-color-dark", lockup_stacked("dark"), h=800)
    save("lockup", "hypedrive-lockup-stacked-mono-black", lockup_stacked("light", mono=ink), h=800)
    save("lockup", "hypedrive-lockup-stacked-mono-white", lockup_stacked("dark", mono="#ffffff"), h=800)
    save("mark", "hypedrive-mark-color-light", square("light", 1024), h=1024)
    save("mark", "hypedrive-mark-color-dark", square("dark", 1024), h=1024)
    save("mark", "hypedrive-mark-mono-black", square("light", 1024, mono=ink), h=1024)
    save("mark", "hypedrive-mark-mono-white", square("dark", 1024, mono="#ffffff"), h=1024)
    save("wordmark", "hypedrive-wordmark-black", wordmark_only("light"), h=400)
    save("wordmark", "hypedrive-wordmark-white", wordmark_only("dark"), h=400)
    save("app-icon", "hypedrive-app-icon-ios-1024", app_icon("dark", rounded=False), w=1024, h=1024)
    save("app-icon", "hypedrive-app-icon-rounded-dark", app_icon("dark"), h=1024)
    save("app-icon", "hypedrive-app-icon-rounded-cobalt", app_icon("dark", tile="cobalt", mono="#ffffff"), h=1024)
    save("app-icon", "hypedrive-app-icon-rounded-light", app_icon("light", tile="paper"), h=1024)
    save("app-icon", "hypedrive-app-icon-android-foreground", square("dark", 432, 0.3), h=432)
    for s, half, det in [(16, 6, "tiny"), (32, 13, "small"), (48, 20, "small")]:
        save("favicon", f"favicon-{s}", favicon(s, half, det), w=s, h=s)
    for s in (180, 192, 512):
        save("favicon", f"favicon-{s}", app_icon("dark", s), w=s, h=s)
    open(os.path.join(dirs["favicon"], "favicon.svg"), "w").write(favicon(32, 13, "small"))
    subprocess.run(["magick", *[os.path.join(dirs["favicon"], f"favicon-{s}.png") for s in (16, 32, 48)],
                    os.path.join(dirs["favicon"], "favicon.ico")], check=True)
    d, tw, report = wordmark_path()
    json.dump({"spacing_report": report, "mark_height": MARK_H, "gap": GAP, "cap": CAP}, open(os.path.join(out, "_metrics.json"), "w"), indent=1)
