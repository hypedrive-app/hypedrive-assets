import sys, os, math, subprocess
sys.path.insert(0, "/tmp/hdwm")
from text2path import text_path
from versions import rpoly, banded, Ids, BLUE, ORNG, YELL, PAL

G = 1.5   # gap between pieces
def clipwrap(d, inner):
    cid = Ids.new("w"); return f'<clipPath id="{cid}"><path d="{d}"/></clipPath><g clip-path="url(#{cid})">{inner}</g>'
def lean_band(b0, b1, lean, H=28):
    xa = lambda b, y: b + lean*(H-y)/H
    return f"M{xa(b0,30):.2f} 30L{xa(b1,30):.2f} 30L{xa(b1,-2):.2f} -2L{xa(b0,-2):.2f} -2z"
def grad(pal, x1, y1, x2, y2):
    gid = Ids.new("g")
    return gid, (f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" gradientUnits="userSpaceOnUse">'
                 f'<stop stop-color="{pal[0]}"/><stop offset=".5" stop-color="{pal[1]}"/><stop offset="1" stop-color="{pal[2]}"/></linearGradient>')

def striped(sil, bounds, lean, fills, ink, slope):
    o = []
    for i, f in enumerate(fills):
        b0 = bounds[i] + (G/2 if i else -20); b1 = bounds[i+1] - (G/2 if i < len(fills)-1 else -40)
        band = lean_band(b0, b1, lean)
        inner = (f'<path fill="{ink}" d="M-10 -10H90V40H-10z"/>' if f is None
                 else banded("M-10 -10H90V40H-10z", f, bounds[i], bounds[i+1]+lean, [9.6, 18.8], slope))
        o.append(clipwrap(sil, clipwrap(band, inner)))
    return "".join(o)

def r_tag(ink, eye):
    lean = 7; sil = rpoly([(0, 28), (lean, 0), (33, 0), (44, 14), (33, 28)], [2.4, 2.4, 2.4, 3.2, 2.4])
    o = striped(sil, [0, 8, 16, 24, 99], lean, [BLUE, ORNG, YELL, None], ink, 0.3)
    return o + f'<circle cx="35.4" cy="14" r="2.3" fill="{eye}"/>', 44

def r_bag(ink, eye):
    o = [f'<path d="M10.2 10V7a5.5 5.5 0 0 1 11 0V10" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>']
    sil = rpoly([(3, 8.8), (28.4, 8.8), (31.4, 28), (0, 28)], [2.2, 2.2, 2.6, 2.6])
    lean = 3.0
    o.append(striped(sil, [0, 8.4, 16.4, 24.4, 99], lean, [BLUE, ORNG, YELL, None], ink, 0.3))
    return "".join(o), 31.4

def spark(cx, cy, r, k=0.30):
    p = lambda dx, dy: f"{cx+dx*r:.2f} {cy+dy*r:.2f}"
    c = k
    return (f"M{p(0,-1)}C{p(c,-c*1.2)} {p(c*1.2,-c)} {p(1,0)}C{p(c*1.2,c)} {p(c,c*1.2)} {p(0,1)}"
            f"C{p(-c,c*1.2)} {p(-c*1.2,c)} {p(-1,0)}C{p(-c*1.2,-c)} {p(-c,-c*1.2)} {p(0,-1)}z")

def r_spark(ink, eye):
    o = []; cx, cy, R = 14, 14, 14
    sil = spark(cx, cy, R)
    quads = [(BLUE, -1, -1), (ORNG, 1, -1), (YELL, 1, 1), (None, -1, 1)]
    for pal, sx, sy in quads:
        x0 = cx + (G/2 if sx > 0 else -30); x1 = cx + (30 if sx > 0 else -G/2)
        y0 = cy + (G/2 if sy > 0 else -30); y1 = cy + (30 if sy > 0 else -G/2)
        q = f"M{x0} {y0}H{x1}V{y1}H{x0}z"
        if pal is None: inner = f'<path fill="{ink}" d="M-10 -10H90V40H-10z"/>'
        else:
            gid, g = grad(pal, cx - sx*2, cy - sy*2, cx + sx*12, cy + sy*12)
            inner = g + f'<path fill="url(#{gid})" d="M-10 -10H90V40H-10z"/>'
        o.append(clipwrap(sil, clipwrap(q, inner)))
    o.append(f'<path fill="{ink}" d="{spark(33.5, 6, 6, 0.3)}"/>')
    return "".join(o), 39.5

def r_mega(ink, eye):
    o = []
    o.append(f'<path fill="{ink}" d="{rpoly([(0,9),(7.4,9),(7.4,19),(0,19)], [2.4,0.8,0.8,2.4])}"/>')
    o.append(f'<circle cx="3.7" cy="14" r="1.7" fill="{eye}"/>')
    sil = rpoly([(8.9, 9), (26, 1.8), (26, 26.2), (8.9, 19)], [0.8, 1.2, 1.2, 0.8])
    for i, pal in enumerate(PAL):
        w = (26 - 8.9) / 3; x0 = 8.9 + i*w + (G/2 if i else 0); x1 = 8.9 + (i+1)*w - (G/2 if i < 2 else -2)
        o.append(clipwrap(sil, banded(f"M{x0:.2f} -2H{x1:.2f}V30H{x0:.2f}z", pal, x0, x1, [10.5, 17.5], 0.35)))
    o.append(f'<path fill="{ink}" d="{rpoly([(27.5,0),(32,0),(32,28),(27.5,28)], 2.25)}"/>')
    for r in (5.2, 10.4):
        a = math.radians(42); cx, cy = 33, 14
        o.append(f'<path d="M{cx+r*math.cos(a):.2f} {cy-r*math.sin(a):.2f}A{r} {r} 0 0 1 {cx+r*math.cos(a):.2f} {cy+r*math.sin(a):.2f}" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>')
    return "".join(o), 33 + 10.4 + 1.5

def r_box(ink, eye):
    o = []
    o.append(f'<path fill="{ink}" d="{rpoly([(0,0),(30,0),(30,8),(0,8)], [2.6,2.6,0.8,0.8])}"/>')
    o.append(f'<path fill="{eye}" d="{rpoly([(12.2,0),(17.8,0),(17.8,8),(12.2,8)], 0.01)}" opacity="0"/>')
    o.append(f'<circle cx="15" cy="4" r="1.7" fill="{eye}"/>')
    sil = rpoly([(1.2, 9.5), (28.8, 9.5), (28.8, 28), (1.2, 28)], [0.8, 0.8, 2.6, 2.6])
    o.append(striped(sil, [1.2, 10.4, 19.6, 99], 0, [BLUE, ORNG, YELL], ink, 0.45))
    return "".join(o), 30

MARKS = dict(tag=r_tag, bag=r_bag, spark=r_spark, megaphone=r_mega, box=r_box)
FONTS = dict(jakarta=("Jakarta", 760), figtree=("Figtree", 760))

def lockup(mark, ink, eye, font="jakarta", text="Hypedrive", soft=0.55):
    name, w = FONTS[font]
    m, mw = MARKS[mark](ink, eye) if mark else ("", 0)
    d, tw = text_path(text, w, 18.6, -0.008, name)
    ox = (mw + 9.5) if mark else soft/2
    W = ox + tw + 1
    st = f' stroke="{ink}" stroke-width="{soft}" stroke-linejoin="round"' if soft else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-0.8 -0.8 {W+1.6:.2f} 29.6" width="{(W+1.6)*10:.0f}" height="296">'
            f'{m}<path fill="{ink}"{st} transform="translate({ox:.2f} 22.9)" d="{d}"/></svg>')

if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for i, mk in enumerate(["tag", "bag", "spark", "megaphone", "box", None], 1):
        for font in FONTS:
            for theme, ink, eye in [("light", "#141414", "#fff"), ("dark", "#fff", "#141414")]:
                nm = f"hypedrive-r{i}-{mk or 'wordmark'}-{font}-{theme}"
                p = os.path.join(out, nm + ".svg"); open(p, "w").write(lockup(mk, ink, eye, font))
                subprocess.run(["rsvg-convert", "-h", "592", p, "-o", p[:-4] + ".png"], check=True)
