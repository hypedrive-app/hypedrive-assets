"""Refined Hypedrive icon family — same rendering as the final box:
true 30° iso, two-stop gradient per face, rounded silhouettes, no AA seams, Bricolage wordmark."""
import sys, os, math, subprocess
sys.path.insert(0, "/tmp/hdwm")
from versions import rpoly
from text2path import text_path

C30, S30 = math.cos(math.radians(30)), 0.5
def P(x, y, z): return (x*C30 - y*C30, (x + y)*S30 - z)
def pts(*p3): return " ".join(f"{a:.3f},{b:.3f}" for a, b in (P(*p) for p in p3))

import palette as PL
SIGNATURE = (PL.ramp(.93, .86, .15, .18, 96, 86), PL.BLUE[1], PL.ORNG[1])
HUE = {"blue": PL.BLUE, "orange": PL.ORNG, "yellow": PL.YELL}
INK = {"light": PL.INK_L, "dark": PL.INK_D}
SOLID = {"light": dict(ink=PL.INK_TEXT_L, tape=(PL.INK_L[0][1], PL.INK_L[2][0]), dot="#ffffff"),
         "dark":  dict(ink="#ffffff", tape=("#ffffff", PL.INK_D[2][0]), dot=PL.INK_TEXT_L)}
R_OUT = 1.2

class Ctx:
    def __init__(self, theme): self.theme = theme; self.n = 0; self.defs = []; self.pts = []
    def id(self, p): self.n += 1; return f"{p}{self.n}"
    def grad(self, pair, a, b):
        gid = self.id("g")
        self.defs.append(f'<linearGradient id="{gid}" x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" gradientUnits="userSpaceOnUse">'
                         f'<stop stop-color="{pair[0]}"/><stop offset="1" stop-color="{pair[1]}"/></linearGradient>')
        return f"url(#{gid})"
    def clip(self, d):
        cid = self.id("c"); self.defs.append(f'<clipPath id="{cid}"><path d="{d}"/></clipPath>'); return cid

def silhouette(x, y, z, w, d, h):
    return [P(x, y, z+h), P(x+w, y, z+h), P(x+w, y, z), P(x+w, y+d, z), P(x, y+d, z), P(x, y+d, z+h)]

def box(c, x, y, z, w, d, h, tones, deco="", faces=("top", "left", "right"), r=R_OUT):
    """One rounded iso box. deco: svg drawn inside the box clip (tape etc.)."""
    sil = silhouette(x, y, z, w, d, h); c.pts += sil
    cid = c.clip(rpoly(sil, r))
    t, l, rr = tones; e = 0.05
    out = [f'<g clip-path="url(#{cid})">']
    if "left" in faces:
        out.append(f'<polygon fill="{c.grad(l, P(x, y+d, z+h), P(x, y+d, z))}" points="{pts((x-e,y+d,z-e),(x+w+e,y+d,z-e),(x+w+e,y+d,z+h+e),(x-e,y+d,z+h+e))}"/>')
    if "right" in faces:
        out.append(f'<polygon fill="{c.grad(rr, P(x+w, y, z+h), P(x+w, y, z))}" points="{pts((x+w,y-e,z-e),(x+w,y+d+e,z-e),(x+w,y+d+e,z+h),(x+w,y-e,z+h))}"/>')
    if "top" in faces:
        out.append(f'<polygon fill="{c.grad(t, P(x, y, z+h), P(x+w, y+d, z+h))}" points="{pts((x,y,z+h),(x+w,y,z+h),(x+w,y+d,z+h),(x,y+d,z+h))}"/>')
    out.append(deco + "</g>")
    return "".join(out)

def tape(c, x, y, z, w, d, h, drop=0.46, half=0.115):
    """Tape along x over the lid and down the +x face (sizes relative to the box)."""
    tt = SOLID[c.theme]["tape"]; m = y + d/2; hw = d*half
    return (f'<polygon fill="{tt[0]}" points="{pts((x-1,m-hw,z+h),(x+w,m-hw,z+h),(x+w,m+hw,z+h),(x-1,m+hw,z+h))}"/>'
            f'<polygon fill="{tt[1]}" points="{pts((x+w,m-hw,z+h),(x+w,m+hw,z+h),(x+w,m+hw,z+h-h*drop),(x+w,m-hw,z+h-h*drop))}"/>')

def dot_left(c, x, z, y, r):
    cx, cy = P(x, y, z); return f'<circle cx="{cx:.3f}" cy="{cy:.3f}" r="{r}" fill="{SOLID[c.theme]["dot"]}"/>'

# ------------------------------------------------------------------ icons
def f_box(c):
    return box(c, 0, 0, 0, 10, 10, 10, SIGNATURE, tape(c, 0, 0, 0, 10, 10, 10)) + dot_left(c, 3.1, 4.6, 10, 1.05)

def f_unbox(c):
    """Open ink box, three rounded bars (blue, orange, yellow) rising out of it."""
    W, D, H = 12, 12, 6.6; ink = INK[c.theme]
    sil = silhouette(0, 0, 0, W, D, H); c.pts += sil
    cid = c.clip(rpoly(sil, R_OUT))
    inner = (f'<g clip-path="url(#{cid})">'
             f'<polygon fill="{ink[2][1]}" points="{pts((0,0,H),(W,0,H),(W,D,H),(0,D,H))}"/>'
             f'<polygon fill="{c.grad(ink[2], P(0,0,H), P(0,0,0))}" points="{pts((0,0,0),(0,D,0),(0,D,H),(0,0,H))}"/>'
             f'<polygon fill="{c.grad(ink[1], P(0,0,H), P(0,0,0))}" points="{pts((0,0,0),(W,0,0),(W,0,H),(0,0,H))}"/></g>')
    bars = ""
    for i, (hue, h) in enumerate([("blue", 10.5), ("orange", 15.5), ("yellow", 20.5)]):
        b = 3.1; x = 1.4 + i*3.45; y = 7.5 - i*3.45
        bars += box(c, x, y, 0, b, b, h, HUE[hue], r=0.8)
    front = box(c, 0, 0, 0, W, D, H, ink, faces=("left", "right"))
    return inner + bars + front + dot_left(c, 3.0, 3.1, D, 1.1)

def f_stack(c):
    """Parcel pyramid: blue + orange on the ground, yellow on top, the signature box crowning it."""
    s = 6.2
    o = box(c, 0, s+0.5, 0, s, s, s, HUE["blue"])
    o += box(c, s+0.5, 0, 0, s, s, s, HUE["orange"])
    o += box(c, 1.4, 1.4, s+0.45, s, s, s*0.92, HUE["yellow"])
    o += box(c, 3.0, 3.0, s+0.45+s*0.92+0.45, 3.0, 3.0, 3.0, INK[c.theme], r=0.7)
    return o

def f_express(c):
    """Signature box with three ink speed trails running underneath it."""
    o = ""
    ink = SOLID[c.theme]["ink"]
    for z, y, x0, wdt in [(7.2, 5.0, 2.6, 1.5), (4.4, 6.5, -1.2, 1.5), (1.6, 5.0, 3.8, 1.5)]:
        a, b = P(x0, y, z), P(13.5, y, z)
        c.pts += [(a[0]-1, a[1]-1), (a[0]+1, a[1]+1)]
        o += f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" stroke="{ink}" stroke-width="{wdt*1.2:.2f}" stroke-linecap="round"/>'
    o += box(c, 10, 0, 0, 10, 10, 10, SIGNATURE, tape(c, 10, 0, 0, 10, 10, 10)) + dot_left(c, 13.1, 4.6, 10, 1.05)
    return o

def f_deal(c):
    """Signature box wearing an ink price tag on its orange face."""
    o = box(c, 0, 0, 0, 10, 10, 10, SIGNATURE, tape(c, 0, 0, 0, 10, 10, 10, drop=0.0))
    ink = SOLID[c.theme]["ink"]; eye = SOLID[c.theme]["dot"]
    yz = [(1.3, 1.4), (5.6, 1.4), (8.3, 3.85), (5.6, 6.3), (1.3, 6.3)]
    tag2d = [P(10, y, z) for y, z in yz]
    o += f'<path fill="{ink}" d="{rpoly(tag2d, 0.55)}"/>'
    hx, hy = P(10, 5.8, 3.85)
    o += f'<g transform="translate({hx:.3f} {hy:.3f}) matrix({C30:.4f} {-S30} 0 1 0 0)"><circle r="0.95" fill="{eye}"/></g>'
    return o + dot_left(c, 3.1, 4.6, 10, 1.05)

def f_monogram(c):
    """Iso H: blue and orange pillars, yellow bridge, ink cap."""
    o = box(c, 0, 0, 0, 3.6, 3.6, 13, HUE["blue"])
    o += box(c, 3.6, 0, 4.7, 5.2, 3.6, 3.6, HUE["yellow"], r=0.5)
    o += box(c, 8.8, 0, 0, 3.6, 3.6, 13, HUE["orange"])
    o += box(c, 8.8, 0, 13.6, 3.6, 3.6, 2.0, INK[c.theme], r=0.7)
    return o

ICONS = [("box", f_box), ("unbox", f_unbox), ("stack", f_stack), ("express", f_express), ("deal", f_deal), ("monogram", f_monogram)]

def mark(fn, theme, H=28):
    c = Ctx(theme); body = fn(c)
    xs = [p[0] for p in c.pts]; ys = [p[1] for p in c.pts]
    x0, y0, x1, y1 = min(xs), min(ys), max(xs), max(ys); k = H / (y1 - y0)
    return (f'<defs>{"".join(c.defs)}</defs><g transform="scale({k:.5f}) translate({-x0:.3f} {-y0:.3f})">{body}</g>', (x1-x0)*k)

FONT, WGHT, CAP, SOFT, GAP = "Bricolage", 700, 18.6, 0.3, 8.0
SPACING = dict(strength=0.75, extra=0.012)
import optical as OPT
AXES = {"opsz": 96, "wdth": 100}

def lockup(fn, theme):
    ink = SOLID[theme]["ink"]; m, mw = mark(fn, theme)
    d, tw, _ = OPT.optical_text_path("Hypedrive", WGHT, CAP, FONT, AXES, **SPACING)
    ox = mw + GAP; Wd = ox + tw + SOFT; pad = 1
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {Wd+2*pad:.2f} {28+2*pad}" width="{(Wd+2*pad)*10:.0f}" height="{(28+2*pad)*10:.0f}">'
            f'{m}<path fill="{ink}" stroke="{ink}" stroke-width="{SOFT}" stroke-linejoin="round" transform="translate({ox:.2f} 22.9)" d="{d}"/></svg>')

def square(fn, theme, size=512, pad=0.1, tile=None):
    s = 100.0; inner = s*(1-2*pad)
    m, mw = mark(fn, theme, inner)
    if mw > inner:                      # wide icons: fit by width instead
        m, mw = mark(fn, theme, inner*inner/mw)
    hgt = inner if mw <= inner else inner*inner/mw
    ox = (s-mw)/2; oy = (s-hgt)/2
    bg = f'<rect width="{s}" height="{s}" rx="{s*0.225}" fill="{tile}"/>' if tile else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}" width="{size}" height="{size}">{bg}<g transform="translate({ox:.3f} {oy:.3f})">{m}</g></svg>'

if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for i, (name, fn) in enumerate(ICONS, 1):
        for th in ("light", "dark"):
            for kind, svg, h in [("lockup", lockup(fn, th), 600), ("mark", square(fn, th), 512),
                                 ("app-icon", square(fn, th, 1024, 0.2, "#ffffff" if th == "light" else "#141414"), 1024)]:
                p = os.path.join(out, f"hypedrive-{i}-{name}-{kind}-{th}.svg"); open(p, "w").write(svg)
                subprocess.run(["rsvg-convert", "-h", str(h), p, "-o", p[:-4] + ".png"], check=True)
