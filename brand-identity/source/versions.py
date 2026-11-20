import sys, os, math, subprocess
sys.path.insert(0, "/tmp/hdwm")
from text2path import text_path

BLUE = ("#3f80ff", "#0255ff", "#0041c6")
ORNG = ("#ff651e", "#ef3c00", "#c42c00")
YELL = ("#ffd849", "#ffb700", "#ff9500")
PAL = [BLUE, ORNG, YELL]

SMOOTH = 0.6        # 0 = circular corners, 1 = very soft continuous-curvature ("squircle") corners

def rpoly(pts, r, smooth=None):
    """Closed polygon with smooth rounded corners (radius r, or a list of radii).
    Each corner is a cubic whose tangent run is stretched by `smooth` and whose handles reach
    further in, giving continuous curvature instead of a pinched quadratic corner."""
    sm = SMOOTH if smooth is None else smooth
    n = len(pts); rs = r if isinstance(r, list) else [r]*n
    d = []
    for i in range(n):
        p0, p1, p2 = pts[i-1], pts[i], pts[(i+1) % n]
        v1 = (p0[0]-p1[0], p0[1]-p1[1]); v2 = (p2[0]-p1[0], p2[1]-p1[1])
        l1 = math.hypot(*v1); l2 = math.hypot(*v2)
        ang = math.acos(max(-1, min(1, (v1[0]*v2[0]+v1[1]*v2[1])/(l1*l2))))
        t = rs[i]/math.tan(ang/2) if ang > 1e-6 else 0
        te = min(t*(1 + sm), l1/2, l2/2)                      # stretched tangent run
        cd = te*(0.45 - 0.33*sm)                              # control points sit this far from the corner
        u1 = (v1[0]/l1, v1[1]/l1); u2 = (v2[0]/l2, v2[1]/l2)
        a = (p1[0]+u1[0]*te, p1[1]+u1[1]*te); bb = (p1[0]+u2[0]*te, p1[1]+u2[1]*te)
        c1 = (p1[0]+u1[0]*cd, p1[1]+u1[1]*cd); c2 = (p1[0]+u2[0]*cd, p1[1]+u2[1]*cd)
        d.append(("M" if i == 0 else "L") + f"{a[0]:.4f} {a[1]:.4f}")
        d.append(f"C{c1[0]:.4f} {c1[1]:.4f} {c2[0]:.4f} {c2[1]:.4f} {bb[0]:.4f} {bb[1]:.4f}")
    return "".join(d) + "z"

class Ids:
    n = 0
    @classmethod
    def new(cls, p): cls.n += 1; return f"{p}{cls.n}"

def banded(shape_d, pal, x0, x1, cuts, slope):
    """Fill shape with 3 tonal bands; cuts are y positions at x0; band edges have the given slope."""
    cid = Ids.new("c")
    out = [f'<clipPath id="{cid}"><path d="{shape_d}"/></clipPath><g clip-path="url(#{cid})">']
    ys = [-50] + cuts
    for c, y in zip(pal, ys):
        w = x1 - x0 + 20
        out.append(f'<path fill="{c}" d="M{x0-10:.2f} {y:.2f}L{x1+10:.2f} {y+slope*w:.2f}V90H{x0-10:.2f}z"/>')
    out.append("</g>")
    return "".join(out)

# ---------- marks (height 28) ----------
def mark_stripes(ink, eye):
    o = []; lean = 6.5; sw = 7.6; gap = 2.2
    for i, pal in enumerate(PAL):
        x = i*(sw+gap)
        d = rpoly([(x, 28), (x+lean, 0), (x+lean+sw, 0), (x+sw, 28)], 1.6)
        o.append(banded(d, pal, x, x+lean+sw, [9.5, 19], 0.35))
    x = 3*(sw+gap); tip = x + lean + 19
    o.append(f'<path fill="{ink}" d="{rpoly([(x,28),(x+lean,0),(tip,14)], [1.6,1.6,3.2])}"/>')
    o.append(f'<circle cx="{x+lean/2+6.4:.2f}" cy="14" r="2.1" fill="{eye}"/>')
    return "".join(o), tip

def mark_steps(ink, eye):
    o = []; cw = 10
    top = lambda x: 16 - 16*x/30
    for i, pal in enumerate(PAL):
        x = i*cw
        d = rpoly([(x, 28), (x, top(x)), (x+cw, top(x+cw)), (x+cw, 28)], [2.4 if i == 0 else 0.01, 2.4 if i == 0 else 0.01, 0.01, 0.01])
        o.append(banded(d, pal, x, x+cw, [top(x)+7, top(x)+15], -16/30))
    x = 3*cw
    d = rpoly([(x, 28), (x, 0), (x+15, 0), (x+15, 28)], [0.01, 0.01, 7, 7])
    o.append(f'<path fill="{ink}" d="{d}"/>')
    o.append(f'<circle cx="{x+7.5:.2f}" cy="14" r="2.1" fill="{eye}"/>')
    return "".join(o), x+15

def mark_h(ink, eye):
    o = []; sw = 9
    o.append(banded(rpoly([(0,28),(0,0),(sw,0),(sw,28)], 2.6), BLUE, 0, sw, [9.5, 19], 0.6))
    x = 19
    o.append(banded(rpoly([(x,28),(x,0),(x+sw,0),(x+sw,28)], 2.6), ORNG, x, x+sw, [9.5, 19], 0.6))
    # rising crossbar
    o.append(banded(rpoly([(sw-1,22),(sw-1,13.5),(x+1,7),(x+1,15.5)], 0.01), YELL, sw-1, x+1, [30, 31], -0.6))
    o.append(f'<path fill="{ink}" d="{rpoly([(x+sw+2.2,28),(x+sw+2.2,0),(x+sw+16,14)], [1.6,1.6,3])}"/>')
    o.append(f'<circle cx="{x+sw+7:.2f}" cy="14" r="2.1" fill="{eye}"/>')
    return "".join(o), x+sw+16

def mark_chevrons(ink, eye):
    o = []; step = 9.5; w = 5.4
    for i, pal in enumerate(PAL + [None]):
        x = 2.7 + i*step
        col = ink if pal is None else None
        if pal:
            gid = Ids.new("g")
            o.append(f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="28" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{pal[0]}"/><stop offset=".5" stop-color="{pal[1]}"/><stop offset="1" stop-color="{pal[2]}"/></linearGradient>')
            col = f"url(#{gid})"
        o.append(f'<path d="M{x:.2f} 2.7L{x+11:.2f} 14L{x:.2f} 25.3" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
    xe = 2.7 + 3*step + 11 + 2.7
    return "".join(o), xe

def mark_gauge(ink, eye):
    o = []; cx, cy, rc, w = 27, 24.2, 18, 12
    segs = [(180, 122), (118, 62), (58, 0)]
    for (a0, a1), pal in zip(segs, PAL):
        def pt(a, r): return (cx + r*math.cos(math.radians(a)), cy - r*math.sin(math.radians(a)))
        ro, ri = rc + w/2, rc - w/2
        p = [pt(a0, ro), pt(a1, ro), pt(a1, ri), pt(a0, ri)]
        d = (f"M{p[0][0]:.2f} {p[0][1]:.2f}A{ro} {ro} 0 0 1 {p[1][0]:.2f} {p[1][1]:.2f}"
             f"L{p[2][0]:.2f} {p[2][1]:.2f}A{ri} {ri} 0 0 0 {p[3][0]:.2f} {p[3][1]:.2f}z")
        gid = Ids.new("g")
        o.append(f'<linearGradient id="{gid}" x1="{p[0][0]:.2f}" y1="{p[0][1]:.2f}" x2="{p[2][0]:.2f}" y2="{p[2][1]:.2f}" gradientUnits="userSpaceOnUse"><stop stop-color="{pal[0]}"/><stop offset=".55" stop-color="{pal[1]}"/><stop offset="1" stop-color="{pal[2]}"/></linearGradient>')
        o.append(f'<path fill="url(#{gid})" stroke="url(#{gid})" stroke-width="1.6" stroke-linejoin="round" d="{d}"/>')
    a = math.radians(38)
    tx, ty = cx + 20*math.cos(a), cy - 20*math.sin(a)
    o.append(f'<path d="M{cx:.2f} {cy:.2f}L{tx:.2f} {ty:.2f}" stroke="{ink}" stroke-width="3.6" stroke-linecap="round"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="4.4" fill="{ink}"/><circle cx="{cx}" cy="{cy}" r="1.6" fill="{eye}"/>')
    return "".join(o), 54

MARKS = {"stripes": mark_stripes, "steps": mark_steps, "monogram": mark_h, "chevrons": mark_chevrons, "gauge": mark_gauge}

def lockup(mark, ink, eye, text="Hypedrive", wght=700, track=-0.012, gap=10.5):
    m, mw = MARKS[mark](ink, eye) if mark else ("", -gap)
    d, tw = text_path(text, wght, 18.9, track)
    ox = mw + gap
    W = ox + tw + 0.6
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-0.6 -0.6 {W+1.2:.2f} 29.2" width="{(W+1.2)*10:.0f}" height="292">'
            f'{m}<path fill="{ink}" transform="translate({ox:.2f} 22.9)" d="{d}"/></svg>')

VERSIONS = [
    ("v1-stripes", dict(mark="stripes")),
    ("v2-steps", dict(mark="steps")),
    ("v3-monogram", dict(mark="monogram")),
    ("v4-chevrons", dict(mark="chevrons")),
    ("v5-gauge", dict(mark="gauge")),
    ("v6-stripes-lowercase", dict(mark="stripes", text="hypedrive")),
    ("v7-wordmark-only", dict(mark=None)),
]

if __name__ == "__main__":
    out = sys.argv[1]
    for name, kw in VERSIONS:
        for theme, ink, eye in [("light", "#151515", "#fff"), ("dark", "#fff", "#151515")]:
            svg = lockup(ink=ink, eye=eye, **kw)
            p = os.path.join(out, f"hypedrive-{name}-{theme}.svg")
            open(p, "w").write(svg)
            subprocess.run(["rsvg-convert", "-h", "560", p, "-o", p[:-4] + ".png"], check=True)
