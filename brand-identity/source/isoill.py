"""Hypedrive spot illustrations, v2. Same craft as the parcel: chunky rounded volumes, true 30° iso,
the signature three faces (Marigold top, Cobalt left, Vermilion right), one Ink accent, a white dot.
No thin slabs, no flat cut-outs, no tiny detail."""
import sys, math, json, re
sys.path.insert(0, "/tmp/hdwm")
import isofam as F
from versions import rpoly
from isofam import P, Ctx, HUE, INK, SOLID, box
SIG = F.SIGNATURE
def pt(p): return f"{p[0]:.3f},{p[1]:.3f}"

# ---------------------------------------------------------------- 2D shapes (u, v), counter-clockwise
def round_poly(pts, r, n=8):
    rl = r if isinstance(r, list) else None
    """Round every corner of a polygon with a quadratic arc of radius ~r (keeps the parcel's soft corners)."""
    out = []; m = len(pts)
    for i in range(m):
        a, b, c = pts[i - 1], pts[i], pts[(i + 1) % m]
        la = math.dist(a, b); lc = math.dist(b, c); k = min(rl[i] if rl else r, la / 2.2, lc / 2.2)
        p0 = (b[0] + (a[0] - b[0]) * k / la, b[1] + (a[1] - b[1]) * k / la)
        p2 = (b[0] + (c[0] - b[0]) * k / lc, b[1] + (c[1] - b[1]) * k / lc)
        for j in range(n + 1):
            t = j / n; out.append(((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * b[0] + t * t * p2[0], (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * b[1] + t * t * p2[1]))
    return out
def rpoly_pts(pts, r, n=10):
    """The parcel's continuous-curvature rounded polygon (versions.rpoly), sampled to points for sweeping."""
    d = rpoly(pts, r); toks = re.findall(r"[MLCz]|-?\d+\.?\d*(?:e-?\d+)?", d)
    out = []; i = 0; cur = None
    while i < len(toks):
        t = toks[i]
        if t in "ML": cur = (float(toks[i + 1]), float(toks[i + 2])); out.append(cur); i += 3
        elif t == "C":
            v = [float(x) for x in toks[i + 1:i + 7]]; p0 = cur; p1, p2, p3 = (v[0], v[1]), (v[2], v[3]), (v[4], v[5])
            for k in range(1, n + 1):
                u = k / n; out.append(tuple((1 - u) ** 3 * p0[j] + 3 * (1 - u) ** 2 * u * p1[j] + 3 * (1 - u) * u * u * p2[j] + u ** 3 * p3[j] for j in (0, 1)))
            cur = p3; i += 7
        else: i += 1
    return out
def circle(cx, cy, r, n=72): return [(cx + r * math.cos(2 * math.pi * i / n), cy + r * math.sin(2 * math.pi * i / n)) for i in range(n)]
def hexagon(cx, cy, r, rr): return round_poly([(cx + r * math.cos(math.radians(30 + 60 * k)), cy + r * math.sin(math.radians(30 + 60 * k))) for k in range(6)], rr)
def star(cx, cy, R, ratio, rr):
    return round_poly([(cx + (R if k % 2 == 0 else R * ratio) * math.cos(math.radians(90 + 36 * k)), cy + (R if k % 2 == 0 else R * ratio) * math.sin(math.radians(90 + 36 * k))) for k in range(10)], rr)

def prism(c, shape, x, y, z, h, tones=SIG, halves=False):
    """A shape lying on the ground, extruded up. Facets facing +y take the left tone, +x the right tone,
    each as ONE path (so no seams between facets); the cap takes the top tone."""
    t, l, r = tones; n = len(shape)
    bot = [P(x + u, y + v, z) for u, v in shape]; top = [P(x + u, y + v, z + h) for u, v in shape]
    c.pts += bot + top
    R, L = [], []
    for i in range(n):
        j = (i + 1) % n; (u0, v0), (u1, v1) = shape[i], shape[j]
        nx, ny = (v1 - v0), -(u1 - u0)                       # outward normal for a CCW polygon
        if nx + ny <= 0: continue                            # faces away from the viewer
        d = f"M{pt(bot[i])} L{pt(bot[j])} L{pt(top[j])} L{pt(top[i])}Z"
        (L if ny > nx else R).append(d)
        if halves: R.append(d); L.append(d)
    y0 = min(p[1] for p in top); y1 = max(p[1] for p in bot)
    gr = c.grad(r, (0, y0), (0, y1)); gl = c.grad(l, (0, y0), (0, y1))
    xs = [p[0] for p in top]; ys = [p[1] for p in top]
    gt = c.grad(t, (min(xs), min(ys)), (max(xs), max(ys)))
    o = f'<path fill="{gr}" d="{"".join(R + L)}"/>'      # right tone under everything
    if halves:
        mx = P(x, y, z)[0]
        cid = c.clip(f"M{mx:.3f},-1000 L{mx-1000:.3f},-1000 L{mx-1000:.3f},1000 L{mx:.3f},1000Z")
        o += f'<g clip-path="url(#{cid})"><path fill="{gl}" d="{"".join(L)}"/></g>'
    elif L: o += f'<path fill="{gl}" d="{"".join(L)}"/>'
    o += f'<path fill="{gt}" d="M{" L".join(pt(p) for p in top)}Z"/>'
    return o

def _orient(d):
    """Make a facet path wind one way so overlapping facets in one path never cancel (nonzero fill)."""
    return d

def _quad(pts):
    a = sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1] for i in range(len(pts)))
    q = pts if a >= 0 else pts[::-1]
    return "M" + " L".join(pt(p) for p in q) + "Z"

def prism_up(c, shape, x, y, z, d, cap=None, up=None, right=None, mode="split", extra="", gbox=None, deco="", hole=None, nocap=False, capc=None):
    """A shape standing upright (u = +x, v = up), extruded toward the viewer along +y by d.
    The face toward the viewer is the cap. mode "split": upward facets take `up`, the rest `right`;
    mode "grad": the whole sweep is one path with a single up->right gradient (smooth round forms).
    extra: drawn on the sweep, beneath the cap. deco: drawn on the cap, clipped to it.
    hole: a shape cut out of the cap (even-odd). gbox: fixed (x0,y0,x1,y1) for every gradient, so
    two parts of one object share a gradient and join without a seam."""
    cap = cap or SIG[1]; up = up or SIG[0]; right = right or SIG[2]
    n = len(shape)
    back = [P(x + u, y, z + v) for u, v in shape]; front = [P(x + u, y + d, z + v) for u, v in shape]
    c.pts += back + front
    U, R, A = [], [], []
    for i in range(n):
        j = (i + 1) % n; (u0, v0), (u1, v1) = shape[i], shape[j]
        nu, nv = (v1 - v0), -(u1 - u0)
        dd = _quad([back[i], back[j], front[j], front[i]])
        A.append(dd)
        if nu <= 0 and nv <= 0: continue
        (U if nv > nu * 0.9 else R).append(dd)
    allp = back + front
    x0 = min(p[0] for p in allp); x1 = max(p[0] for p in allp); y0 = min(p[1] for p in allp); y1 = max(p[1] for p in allp)
    if gbox: x0, y0, x1, y1 = gbox
    if mode == "grad":
        g = c.grad((up[0], right[1]), (x0, y0), (x1, y1))
        o = f'<path fill="{g}" d="{"".join(A)}"/>'
    else:
        gr = c.grad(right, (0, y0), (0, y1)); gu = c.grad(up, (0, y0), (0, y1))
        o = f'<path fill="{gr}" d="{"".join(R + U)}"/>'
        if U: o += f'<path fill="{gu}" d="{"".join(U)}"/>'
    o += extra
    if nocap: return o
    fy0, fy1 = (gbox[1], gbox[3]) if gbox else (min(p[1] for p in front), max(p[1] for p in front))
    gc = c.grad(cap, (0, fy0), (0, fy1))
    od = "M" + " L".join(pt(p) for p in front) + "Z"
    d_ = od
    if hole:
        hp = [P(x + u, y + d, z + v) for u, v in hole]
        d_ += "M" + " L".join(pt(p) for p in hp) + "Z"
    o += f'<path fill="{gc}" fill-rule="evenodd" d="{d_}"/>'
    if deco:
        cid = c.clip(od); o += f'<g clip-path="url(#{cid})">{deco}</g>'
    return o

def prism_hole(c, shape, x, y, z, d, **kw): return prism_up(c, shape, x, y, z, d, **kw)

def on_top(x, y, z, svg2d):
    """Flat artwork lying on a top face (local u = +x, v = +y)."""
    o = P(x, y, z); a = P(x + 1, y, z); b = P(x, y + 1, z)
    return f'<g transform="matrix({a[0]-o[0]:.4f} {a[1]-o[1]:.4f} {b[0]-o[0]:.4f} {b[1]-o[1]:.4f} {o[0]:.3f} {o[1]:.3f})">{svg2d}</g>'
def on_left(x, y, z, svg2d):
    """Flat artwork on a +y (left) face (local u = +x, v = up)."""
    o = P(x, y, z); a = P(x + 1, y, z); b = P(x, y, z + 1)
    return f'<g transform="matrix({a[0]-o[0]:.4f} {a[1]-o[1]:.4f} {b[0]-o[0]:.4f} {b[1]-o[1]:.4f} {o[0]:.3f} {o[1]:.3f})">{svg2d}</g>'
def dot(c, x, y, z, r=1.05):
    a = P(x, y, z); return f'<circle cx="{a[0]:.3f}" cy="{a[1]:.3f}" r="{r}" fill="{SOLID[c.theme]["dot"]}"/>'
def ink(c): return SOLID[c.theme]["ink"]
def ptones(c):
    """Physical Ink parts (tyres, handles, shackles): dark in both themes; in dark a lighter face lifts them off the page."""
    L = F.PL.INK_L
    if c.theme == "light": return (L[0], L[1], L[2])
    return (("#646975", "#50545e"), ("#40434c", "#2d3038"), ("#2d3038", "#23262d"))
def phys(c):
    t, l, r = ptones(c)
    return dict(cap=l, up=t, right=r, rim=None if c.theme == "light" else "#6f7480")
def rim(c, shape, x, y, z, d, w=.35):
    p = phys(c)["rim"]
    if not p: return ""
    return f'<path fill="none" stroke="{p}" stroke-width="{w}" stroke-linejoin="round" d="M{" L".join(pt(P(x + u, y + d, z + v)) for u, v in shape)}Z"/>'

# ---------------------------------------------------------------- illustrations
INK_SCREEN = lambda: F.PL.INK_L[1][0]
RUPEE = json.load(open("/tmp/hdwm/nucleo_sharp.json"))["CurrencyRupee"]

def _mix(hexc, k, to=(255, 255, 255)):
    h = hexc.lstrip("#"); r = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
    return "#" + "".join(f"{round(v + (t - v) * k):02x}" for v, t in zip(r, to))

def coin_stack(c, cx, cy, R, h, n):
    """n flush coins, one exact-iso cylinder: elliptical caps (ry/rx = 1/sqrt3), each side wall one path with the
    Cobalt|Vermilion split on the silhouette's centre line, thin darker seam bands, a bevelled top face."""
    rx, ry = R * F.C30 * math.sqrt(2), R * math.sqrt(2) / 2
    X = P(cx, cy, 0)[0]
    def Y(z): return P(cx, cy, z)[1]
    c.pts += [(X - rx, Y(0) + ry), (X + rx, Y(0) + ry), (X - rx, Y(n * h) - ry), (X + rx, Y(n * h) - ry)]
    def band(z0, z1, left, right, glr):
        yb, yt = Y(z0), Y(z1)
        full = f"M{X-rx:.3f},{yb:.3f}A{rx:.3f},{ry:.3f} 0 0 0 {X+rx:.3f},{yb:.3f}L{X+rx:.3f},{yt:.3f}A{rx:.3f},{ry:.3f} 0 0 1 {X-rx:.3f},{yt:.3f}Z"
        lh = f"M{X-rx:.3f},{yb:.3f}A{rx:.3f},{ry:.3f} 0 0 0 {X:.3f},{yb+ry:.3f}L{X:.3f},{yt+ry:.3f}A{rx:.3f},{ry:.3f} 0 0 1 {X-rx:.3f},{yt:.3f}Z"
        gl = c.grad(left, (0, glr[0]), (0, glr[1])); gr = c.grad(right, (0, glr[0]), (0, glr[1]))
        return f'<path fill="{gr}" d="{full}"/><path fill="{gl}" d="{lh}"/>'
    glr = (Y(n * h), Y(0) + ry)
    o = band(0, n * h, SIG[1], SIG[2], glr)                           # one continuous wall for the whole stack
    sb, so = HUE["blue"][2], HUE["orange"][2]
    for k in range(1, n):                                           # darker seam band: a thin strip of the same wall
        o += band(k * h - .2, k * h + .2, sb, so, glr)
    zt = n * h; yt = Y(zt)
    ell = lambda rr: f"M{X-rr*rx/R:.3f},{yt:.3f}A{rr*rx/R:.3f},{rr*ry/R:.3f} 0 1 0 {X+rr*rx/R:.3f},{yt:.3f}A{rr*rx/R:.3f},{rr*ry/R:.3f} 0 1 0 {X-rr*rx/R:.3f},{yt:.3f}Z"
    t0, t1 = SIG[0]
    o += f'<path fill="{c.grad((t0, t1), (X - rx, yt - ry), (X + rx, yt + ry))}" d="{ell(R)}"/>'
    lo = (_mix(t0, .35), _mix(t1, .28))                             # bevel: a lighter inner face
    o += f'<path fill="{c.grad(lo, (X - rx, yt - ry), (X + rx, yt + ry))}" d="{ell(R * .84)}"/>'
    o += on_top(cx, cy, zt, f'<circle r="{R*.60:.3f}" fill="none" stroke="{HUE["yellow"][2][0]}" stroke-width=".55"/>')
    return o

def i_payout(c):
    """Payouts: a stack of coins and one more coin standing on its edge, with a rupee drawn as geometry."""
    R, h = 4.8, 2.5
    o = coin_stack(c, 12.4, 4.6, R, h, 3)
    RS = 5.6; dk = SOLID["light"]["ink"]
    g = (f'<g fill="none" stroke="{dk}" stroke-width="1.15" stroke-linecap="round" stroke-linejoin="round" transform="scale(1.05)">'
         '<path d="M-2.2 2.5H2.4M-2.2 .6H2.4M-1.4 2.5H.4C2.9 2.5 2.9-1.0 .4-1.0H-1.4L1.6-3.4"/></g>')
    o += prism_up(c, circle(0, 0, RS, 120), 5.2, 7.0, RS, 2.2, cap=SIG[0], up=SIG[0], right=SIG[2], mode="grad", deco=on_left(5.2, 9.2, RS, g))
    return o

def faceon(pts_screen, rad, n=10):
    """A shape designed in SCREEN space (x right, y up, symmetric about x = 0) with the parcel's rounded corners,
    mapped into the (u, v) plane of a standing prism so its face looks straight at the viewer."""
    sp = rpoly_pts(pts_screen, rad, n)
    return [(X / F.C30, X * 0.5 / F.C30 + Y) for X, Y in sp]

DEPTH = 3.0                                                         # one thickness for every standing object



def i_content(c):
    """Creator content: a phone standing on its edge, Ink screen, playing a reel."""
    W, H = 11.2, 14.6
    o = box(c, 0, 0, 0, W, DEPTH, H, SIG, r=1.7)
    cx, cy = W / 2, H / 2
    o += on_left(0, DEPTH, 0, f'<rect x=".95" y=".95" width="{W-1.9}" height="{H-1.9}" rx="1.2" fill="{INK_SCREEN()}"/>'
                 f'<path d="M{cx-1.3} {cy-2.1}v4.2l3.6-2.1z" fill="#fff" stroke="#fff" stroke-width=".8" stroke-linejoin="round" transform="translate({0.25} 0)"/>')
    return o

def i_growth(c):
    """Reports: three chunky bars stepping up, each in the signature faces."""
    o = ""
    for i, h in enumerate([6.4, 10.6, 14.8]):
        x = i * 5.0; y = 10.0 - i * 5.0
        o += box(c, x, y, 0, 4.6, 4.6, h, SIG, r=1.1)
    return o


# ---------------------------------------------------------------- shared builders
def arch(Ro, Ri, leg, n=40):
    """A thick upside-down U (handle / shackle) in (u, v), base on v = 0, CCW."""
    p = [(Ro, 0)] + [(Ro, leg)]
    p += [(Ro * math.cos(math.pi * i / n), leg + Ro * math.sin(math.pi * i / n)) for i in range(1, n)] + [(-Ro, leg), (-Ro, 0), (-Ri, 0), (-Ri, leg)]
    p += [(Ri * math.cos(math.pi - math.pi * i / n), leg + Ri * math.sin(math.pi - math.pi * i / n)) for i in range(1, n)] + [(Ri, leg), (Ri, 0)]
    return p
def bbox_scr(c0, pts3):
    xs = [p[0] for p in pts3]; ys = [p[1] for p in pts3]; return (min(xs), min(ys), max(xs), max(ys))
def dkink(): return F.PL.INK_L[2][0]
def pale(): return HUE["blue"][0]
def rrect(x, y, w, h, r, fill): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"/>'
def poly2(pts2, fill): return f'<path d="M{" L".join(f"{u:.3f},{v:.3f}" for u, v in pts2)}Z" fill="{fill}"/>'

def on_top_in(W, D, H, svg2d): return on_top(0, 0, H, svg2d)

def i_tracking(c):
    """On its way: a delivery van — one side-profile volume with wheel arches, roomy cab, Ink windows."""
    d = 7.0; WX = (3.6, 13.8); WR = 1.9; WZ = 1.9
    prof = round_poly([(0, 1.0), (16.9, 1.0), (16.9, 4.9), (15.2, 5.4), (13.3, 9.2), (9.9, 9.2), (9.9, 10.9), (0, 10.9)], [0.9, 0.9, 1.0, 0.7, 1.0, 0.5, 1.0, 1.0], 8)
    pp = phys(c); circ = circle(0, 0, WR, 72)
    o = ""
    for wx in WX:
        o += prism_up(c, circ, wx, 0.0, WZ, 1.0, cap=pp["cap"], up=pp["up"], right=pp["right"], mode="grad")
    def at(s_, yy): return P(15.2 - 1.9 * s_, yy, 5.4 + 3.8 * s_)
    ws = f'<path fill="{INK_SCREEN()}" d="{rpoly([at(.12, .8), at(.88, .8), at(.88, d - .8), at(.12, d - .8)], .6)}"/>'
    hl = [P(16.9, d - 2.3, 3.0), P(16.9, d - .7, 3.0), P(16.9, d - .7, 4.0), P(16.9, d - 2.3, 4.0)]
    ws += f'<path fill="{HUE["yellow"][0][0]}" d="{rpoly(hl, .4)}"/>'
    arches = "".join(f'<circle cx="{wx}" cy="{WZ}" r="{WR + .75}" fill="{dkink()}"/>' for wx in WX)
    wl = round_poly([(10.7, 6.0), (14.45, 6.0), (13.1, 8.7), (10.7, 8.7)], .6, 7)
    deco = on_left(0, d, 0, arches + poly2(wl, INK_SCREEN()) + f'<circle cx="3.0" cy="7.2" r="1.0" fill="{SOLID[c.theme]["dot"]}"/>')
    o += prism_up(c, prof, 0, 0, 0, d, mode="split", extra=ws, deco=deco)
    for wx in WX:
        o += prism_up(c, circ, wx, d - 0.2, WZ, 1.3, cap=pp["cap"], up=pp["up"], right=pp["right"], mode="grad")
        o += rim(c, circ, wx, d - 0.2, WZ, 1.3)
    return o


def _sweep_d(shape, x, y, z, d):
    """The wall strip of a shape swept along +y by d (one path, consistent winding)."""
    back = [P(x + u, y, z + v) for u, v in shape]; front = [P(x + u, y + d, z + v) for u, v in shape]
    n = len(shape); return "".join(_quad([back[i], back[(i + 1) % n], front[(i + 1) % n], front[i]]) for i in range(n))




def i_camera(c):
    """Unboxing video: a chunky camera — body, one lens (Ink barrel, glass set in), a viewfinder bump, a white flash dot."""
    W, D, H = 13.6, 6.6, 7.8
    t = ptones(c)
    o = box(c, 0, 0, 0, W, D, H, SIG, r=1.5)
    o += box(c, 8.4, 1.0, H, 3.8, 3.4, 1.7, SIG, r=.7)
    o += F.dot_left(c, 2.3, 6.2, D, 1.05)
    cx, cz, R = 7.0, 3.8, 3.1
    glass = f'<circle r="1.9" fill="{pale()[0]}"/>'
    circ = circle(0, 0, R, 96)
    o += prism_up(c, circ, cx, D - .2, cz, 2.0, cap=t[1], up=t[0], right=t[2], mode="grad", deco=on_left(cx, D + 1.8, cz, glass))
    o += rim(c, circ, cx, D - .2, cz, 2.0)
    return o









# Optical-mass normalisation: every illustration is fitted to the square, then the heavier ones are shrunk so
# their opaque area matches the parcel's (measured with measure.py). Lighter ones are already at the fit limit.
MASS = {"chat": .95, "camera": .98, "approved": .94, "bell": .95}
def fit(fn, k):
    if k >= 1: return fn
    def g(c):
        o = fn(c); xs = [p[0] for p in c.pts]; ys = [p[1] for p in c.pts]
        cx, cy, hw, hh = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2, (max(xs) - min(xs)) / 2 / k, (max(ys) - min(ys)) / 2 / k
        c.pts += [(cx - hw, cy - hh), (cx + hw, cy + hh)]
        return o
    return g
# ---------------------------------------------------------------- the seven volumes, built on iso3d (real meshes, shaded by facet normal)
import numpy as np, re
import iso3d as I
from iso3d import Scene

def mats(c):
    th = c.theme
    return dict(sig=I.sig_mat(), ink=I.ink_mat(th), inkm=I.ink_mono(th), white=I.white_mat(th), verm=I.verm_mat(), vermm=I.verm_mono(),
                cav=I.cavity_mat(), gold=I.Mat((I.sig_mat().ramps[0],)*3, mono=True, ks=0.9), dot=I.solid_mat("#ffffff" if th == "light" else "#17181c"))

def catmull(pts, n=8):
    p = [pts[0]] + list(pts) + [pts[-1]]; out = []
    for i in range(1, len(p) - 2):
        for k in range(n):
            t = k / n
            out.append(tuple(0.5 * ((2 * p[i][j]) + (-p[i - 1][j] + p[i + 1][j]) * t + (2 * p[i - 1][j] - 5 * p[i][j] + 4 * p[i + 1][j] - p[i + 2][j]) * t * t + (-p[i - 1][j] + 3 * p[i][j] - 3 * p[i + 1][j] + p[i + 2][j]) * t ** 3) for j in (0, 1)))
    out.append(tuple(pts[-1])); return out


XZ = ((0, 0, 0), (1, 0, 0), (0, 0, 1), (0, 1, 0))      # outline (x, z), extruded along +y (front = +y, the Cobalt face)
XY = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
def sigm(c, ks=1.3, beta=10.0, tb=0.22):
    m = I.sig_mat(ks=ks, beta=beta); m.topbias = tb; return m

# ------------------------------------------------------------------ bell
def seg_decal(sc, y, pts, w, mat, layer=6):
    """A round-capped polyline (x, z) as flat polygons on the plane y = const (white decal)."""
    n = 20
    for (x0, z0), (x1, z1) in zip(pts, pts[1:]):
        dx, dz = x1 - x0, z1 - z0; L = math.hypot(dx, dz); nx, nz = -dz / L * w / 2, dx / L * w / 2
        sc.add([(x0 + nx, y, z0 + nz), (x1 + nx, y, z1 + nz), (x1 - nx, y, z1 - nz), (x0 - nx, y, z0 - nz)], (0, 1, 0), mat, layer)
    for x, z in pts:
        sc.add([(x + w / 2 * math.cos(2 * math.pi * i / n), y, z + w / 2 * math.sin(2 * math.pi * i / n)) for i in range(n)], (0, 1, 0), mat, layer)

def i_approved(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.9, beta=400, tb=0.0)
    D = 5.2; R = 8.6; sx = 1.22; cx = 0.0; cz = R * math.sqrt(3) / 2 * 0.5 + 0.0
    cz = 7.6
    hexa = [(cx + R * sx * math.cos(math.radians(60 * k)), cz + R * math.sin(math.radians(60 * k))) for k in range(6)]
    outline = rpoly_pts(hexa, 2.8, 9)
    sc.part(); I.extrude(sc, outline, XZ, D, 1.1, sig, seg=4, layer=1)
    seg_decal(sc, D + 0.02, [(cx - 3.9, cz - 0.2), (cx - 1.3, cz - 3.0), (cx + 4.2, cz + 3.1)], 2.2, M["dot"])
    return sc.render()

def i_chat(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.9, beta=400, tb=0.0)
    D = 4.6; W = 16.0
    pts = [(0, 13), (W, 13), (W, 4.8), (10.8, 4.8), (3.8, -2.4), (5.4, 4.8), (0, 4.8)]
    outline = rpoly_pts(pts, [3.8, 3.8, 3.8, 1.8, 3.0, 1.4, 3.8], 9)
    sc.part(); I.extrude(sc, outline, XZ, D, 1.0, sig, seg=4)
    for x in (4.6, 8.0, 11.4): sc.dot((x, D, 8.9), 1.0, M["dot"].solid)
    return sc.render()


def i_lock(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.9, beta=400, tb=0.0)
    W, D, H = 12.0, 8.0, 9.0
    sc.part(); I.rbox(sc, (0, 0, 0), (W, D, H), 1.7, sig, seg=4)
    ink = mats(c)["ink"]; ink.beta = 6.0
    r = 3.0; zc = H + 3.0; y = D / 2; x0 = W / 2 - r; path = [(x0, y, H), (x0, y, zc)]
    for i in range(1, 28):
        a = math.pi * i / 28; path.append((W / 2 - r * math.cos(a), y, zc + r * math.sin(a)))
    path += [(W / 2 + r, y, zc), (W / 2 + r, y, H)]
    sc.part(); I.tube(sc, path, 0.8, ink, sides=16, plane_normal=(0, 1, 0), layer=2)
    I.keyhole_left(sc, W / 2, D + 0.02, 5.0, 1.3, M["dot"])
    return sc.render()




def star_mat(W, U):
    m = I.Mat((I.Ramp("#ffe27b", "#ffc83e"), I.Ramp("#fff0a6", "#ffe27b"), I.Ramp("#ffbb2e", "#ee9400"), I.Ramp("#ffd04a", "#ffb41c"), I.Ramp("#fb6603", "#e44000")), ks=0.35, beta=400.0)
    W = np.array(W); U = np.array(U)
    def tf(n):
        nw = float(n @ W)
        if nw > 0.93: return 0
        if nw > 0.3: return 1
        if n[2] < -0.25: return 2
        if float(n @ U) > 0.45: return 4
        return 3
    m.tonefn = tf; return m

def i_review(c):
    sc = Scene(c); ph = math.radians(22); W = (math.sin(ph), math.cos(ph), 0); U = (math.cos(ph), -math.sin(ph), 0)
    m = star_mat(W, U); R = 9.0; k = 0.58; D = 3.6
    pts = [((R if i % 2 == 0 else R * k) * math.cos(math.radians(90 + 36 * i)) + 9.0, (R if i % 2 == 0 else R * k) * math.sin(math.radians(90 + 36 * i)) + 9.0) for i in range(10)]
    outline = rpoly_pts(pts, [2.3 if i % 2 == 0 else 1.3 for i in range(10)], 10)
    sc.part(); I.extrude(sc, outline, ((0, 0, 0), U, (0, 0, 1), W), D, 0.7, m, seg=8)
    return sc.render()

def i_bag(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.5, beta=400, tb=0.0); cav = I.cavity_mat(); cav.beta = 400.0; cav.ks = 0.4
    W, D, H = 11.4, 6.6, 13.0; tp = 1.1; rb = 0.4; t = 1.1; fl = 3.2
    outline = I.rrect(W, D, 1.5, 8)
    prof = I.arc((tp + 0.6, 0.6), 0.6, 270, 180, 4) + [(0.15, H - 2.5), (-0.28, H - 2.5)] + I.arc((0.12, H - 0.45), 0.4, 180, 90, 4) + I.arc((t - 0.4, H - 0.45), 0.4, 90, 0, 4)
    prof = prof[:5 + 1] if False else prof
    sc.part(); I.sweep(sc, outline, XY, prof, sig, layer=1)
    inner = [(t, H - 0.45), (t, fl)]
    sc.part(); rings, _ = I.sweep(sc, outline, XY, inner, cav, layer=0)
    I.cap(sc, rings[-1][0], fl, XY, +1, cav, layer=0)
    for y in (0.62, D - 0.62):
        r = 3.7; zc = H + 0.6; x0 = W / 2 - r; path = [(x0, y, H - 0.2), (x0, y, zc)]
        for i in range(1, 48):
            a = math.pi * i / 48; path.append((W / 2 - r * math.cos(a), y, zc + r * 0.95 * math.sin(a)))
        path += [(W / 2 + r, y, zc), (W / 2 + r, y, H - 0.2)]
        sc.part(); I.tube(sc, path, 0.58, M["ink"], sides=20, plane_normal=(0, 1, 0), layer=2)
    sc.dot((W * 0.5, D - 0.45, 6.2), 1.05, M["dot"].solid)
    return sc.render()

def i_bell(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=1.0, beta=400.0, tb=0.22); sig.ring = True
    sc.part(); I.sphere(sc, (0, 0, -4.9), 2.2, M["ink"], n=20, layer=0)
    ctrl = [(0, 13.2), (1.7, 13.0), (3.2, 12.0), (4.2, 10.2), (4.8, 8.2), (5.3, 6.2), (5.95, 4.4), (6.6, 2.9), (7.0, 1.9)]
    body = catmull(ctrl, 4)[:-1]
    sc.part(); I.lathe(sc, body + [(7.0, 1.9)], sig, (0, 0, 0), n=72, layer=1)
    # a subtle rolled lip: same tones, a touch lighter, then a darker band under it
    lip = [(7.0, 1.9), (7.45, 1.7), (7.65, 1.2), (7.55, 0.7), (7.2, 0.45)]
    lipm = sigm(c, ks=1.0, beta=400.0, tb=3.0); lipm.ring = True
    sc.part(); I.lathe(sc, lip, lipm, (0, 0, 0), n=72, layer=2, dt=-0.25)
    under = [(7.2, 0.45), (7.0, 0.1), (6.6, -0.1)]
    sc.part(); I.lathe(sc, under, lipm, (0, 0, 0), n=72, layer=2, dt=0.5)
    sc.part(); I.sphere(sc, (0, 0, 13.6), 1.45, M["gold"], n=28, layer=3)
    return sc.render()

def i_search(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.5, beta=400, tb=0.2)
    cav = I.cavity_mat(); cav.beta = 400.0; cav.ks = 0.5
    R = 7.0; t = 2.5; D = 3.6; rb = 0.7; ym = D / 2; n = 112
    ang = math.radians(-40); d = np.array([math.cos(ang), 0, math.sin(ang)])
    outline = [(R * math.cos(2 * math.pi * i / n), R * math.sin(2 * math.pi * i / n)) for i in range(n)]
    glass = I.Mat((I.Ramp("#d6eaff", "#a4cfff"),) * 3, mono=True, ks=0.3)
    gr = R - t + 0.3
    sc.part(); I.poly(sc, [(gr * math.cos(2 * math.pi * i / n), 1.0, gr * math.sin(2 * math.pi * i / n)) for i in range(n)], (0, 1, 0), glass, layer=0)
    arc_pts = [(3.2 * math.cos(math.radians(a)), 3.2 * math.sin(math.radians(a))) for a in range(110, 172, 10)]
    white = I.solid_mat("#ffffff")
    seg_decal(sc, 1.05, arc_pts, 0.8, white, layer=1)
    sc.dot((3.2 * math.cos(math.radians(100)), 1.05, 3.2 * math.sin(math.radians(100))), 0.32, "#ffffff")
    prof = I.arc((rb, rb), rb, 270, 180, 6) + I.arc((rb, D - rb), rb, 180, 90, 8) + I.arc((t - 0.4, D - 0.4), 0.4, 90, 0, 3)
    sc.part(); I.sweep(sc, outline, XZ, prof, sig, layer=2)
    sc.part(); I.sweep(sc, outline, XZ, [(t, D - 0.4), (t, 1.0)], cav, layer=1)
    p0 = (R - 0.4) * d + np.array([0, ym, 0])
    coll = I.Mat((I.Ramp("#2380ff", "#2d58ee"),) * 3, mono=True, ks=0.7)
    sc.part(); I.tube(sc, [p0 + d * u for u in np.linspace(0.0, 3.2, 6)], 2.4, coll, sides=20, plane_normal=(0, 1, 0), layer=3, cap_ends=True)
    hk = mats(c)["ink"]; hk.beta = 400.0; hk.ks = 0.5
    sc.part(); I.tube(sc, [p0 + d * u for u in np.linspace(2.4, 11.0, 14)], 1.8, hk, sides=18, plane_normal=(0, 1, 0), layer=3)
    sc.part(); I.sphere(sc, tuple(p0 + d * 11.0), 1.8, hk, n=20, layer=3)
    return sc.render()

# ------------------------------------------------------------------ gift
def ribbon_ring(sc, mat, frame, w0, w1, a, b, t, rb, layer, rr=1.2):
    """A band wrapped round the box cross-section (a x b) and standing t proud of it, spanning w0..w1 along the frame's W."""
    outline = I.rrect(a + 2 * t, b + t, rr + t, 8, -t, 0.0)
    hw = (w1 - w0)
    prof = [(t, w0)] + I.arc((rb, w0 + rb), rb, 270, 180, 3)[:] + I.arc((rb, w1 - rb), rb, 180, 90, 3) + [(t, w1)]
    sc.part(); I.sweep(sc, outline, frame, prof, mat, layer=layer, visible_only=True)

def i_gift(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.9, beta=22, tb=0.0)
    W = D = 10.0; H = 8.6; t = 0.45; hw = 1.4; m = W / 2
    sc.part(); I.rbox(sc, (0, 0, 0), (W, D, H), 1.2, sig, seg=3)
    ribbon_ring(sc, M["verm"], XZ, m - hw, m + hw, W, H, t, 0.4, 1)
    ribbon_ring(sc, M["verm"], ((0, 0, 0), (0, 1, 0), (0, 0, 1), (1, 0, 0)), m - hw, m + hw, D, H, t, 0.4, 2)
    K = np.array([m, m, H + t]); up = np.array([0, 0, 1.0]); bm = M["vermm"]
    sc.part(); I.rbox(sc, K + (-1.25, -1.25, -0.2), K + (1.25, 1.25, 1.5), 0.7, bm, seg=3, layer=3)
    for sgn in (1, -1):
        d = np.array([1, -1, 0]) / math.sqrt(2) * sgn; p = np.array([1, 1, 0]) / math.sqrt(2)
        al = math.radians(34); a = math.cos(al) * d + math.sin(al) * up
        Lh, Wd = 5.6, 3.5; path = []
        for i in range(56):
            th = 2 * math.pi * i / 56; u = Lh * (1 - math.cos(th)) / 2
            v = Wd * math.sin(th) * (0.34 + 0.66 * (u / Lh) ** 0.5)
            path.append(K + np.array([0, 0, 1.0]) * 0.8 + u * a + v * p)
        sc.part(); I.tube(sc, path, 0.9, bm, sides=12, closed=True, plane_normal=np.cross(a, p), layer=3)
    return sc.render()

# ------------------------------------------------------------------ calendar
def i_calendar(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.9, beta=400, tb=0.0)
    W, D, H = 14.0, 4.8, 13.4
    sc.part(); I.rbox(sc, (0, 0, 0), (W, D, H), 1.2, sig, seg=3)
    sc.part(); I.rbox(sc, (1.7, D - 0.02, 1.7), (W - 1.7, D + 0.4, 10.1), (0.6, 0.2, 0.6), M["white"], seg=3, layer=1)
    sc.part(); M["verm"].beta = 400.0; I.rbox(sc, (7.1, D + 0.38, 2.9), (11.5, D + 1.0, 6.9), (0.85, 0.3, 0.85), M["verm"], seg=4, layer=2)
    for x in (4.0, 10.0):
        sc.part(); I.capsule_z(sc, x, D / 2, H, H + 3.4, 0.85, M["ink"], layer=3)
    return sc.render()

# ------------------------------------------------------------------ shield

def i_shield(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.9, beta=18, tb=0.0)
    D = 4.8; W = 13.6; Z = 14.6
    h = W / 2
    pts = [(0, Z), (W, Z), (W, 9.4), (W - 0.5, 6.0), (W - 2.2, 3.0), (h, -0.4), (2.2, 3.0), (0.5, 6.0), (0, 9.4)]
    outline = rpoly_pts(pts, [2.6, 2.6, 1.5, 3.5, 3.4, 2.0, 3.4, 3.5, 1.5], 9)
    sc.part(); I.extrude(sc, outline, XZ, D, 1.0, sig, seg=4)
    I.keyhole_left(sc, W / 2, D + 0.02, 9.0, 1.5, M["dot"])
    return sc.render()

# ------------------------------------------------------------------ bag

# ------------------------------------------------------------------ lock

# ------------------------------------------------------------------ inbox
def i_inbox(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.9, beta=400, tb=0.0)
    W, D, H = 16.0, 14.0, 6.2; t = 1.7; fl = 2.3
    outline = I.rrect(W, D, 3.4, 8)
    prof = I.arc((0.9, 0.9), 0.9, 270, 180, 4) + I.arc((0.9, H - 0.9), 0.9, 180, 90, 4) + I.arc((t - 0.6, H - 0.6), 0.6, 90, 0, 3)
    sc.part(); I.sweep(sc, outline, XY, prof, sig, layer=1)
    inner = [(t, H - 0.6), (t, fl + 0.5)] + I.arc((t + 0.5, fl + 0.5), 0.5, 180, 270, 3)
    sc.part(); rings, _ = I.sweep(sc, outline, XY, inner, M["cav"], layer=0)
    I.cap(sc, rings[-1][0], fl, XY, +1, M["cav"], layer=0)
    ye = 2.4
    sc.part(); I.rbox(sc, (3.0, ye, fl), (12.6, ye + 0.7, 9.6), 0.3, M["white"], seg=2, layer=1)
    I.poly(sc, [(3.5, ye + 0.72, 9.4), (12.1, ye + 0.72, 9.4), (7.8, ye + 0.72, 5.9)], (0, 1, 0), I.solid_mat("#ffdb68"), layer=1)
    return sc.render()

_RAW = [("parcel", F.f_box), ("payout", i_payout), ("approved", i_approved), ("review", i_review),
        ("content", i_content), ("tracking", i_tracking), ("growth", i_growth), ("search", i_search),
        ("bell", i_bell), ("gift", i_gift), ("calendar", i_calendar), ("shield", i_shield), ("camera", i_camera),
        ("chat", i_chat), ("bag", i_bag), ("lock", i_lock), ("inbox", i_inbox)]
ILLS = [(n, fit(fn, MASS.get(n, 1))) for n, fn in _RAW]

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/hdwm/_ills.html"
    def img(fn, th, size, pad=0.16): return f'<img style="width:{'100%' if size == 360 else str(size) + 'px'}" src="data:image/svg+xml;utf8,{F.square(fn, th, size, pad).replace(chr(35), "%23").replace(chr(34), chr(39))}">'
    cells = ""
    for th, bg in (("light", "#f4f5f8"), ("dark", "#0f1115")):
        cells += "".join(f'<figure style="background:{bg}">{img(fn, th, 360)}<figcaption style="color:{"#555" if th == "light" else "#aaa"}">{n}</figcaption></figure>' for n, fn in ILLS)
    small = ""
    for th, bg in (("light", "#f4f5f8"), ("dark", "#0f1115")):
        for sz in (56, 72): small += f'<div class=row style="background:{bg}">' + "".join(img(fn, th, sz, 0.1) for n, fn in ILLS) + '</div>'
    open(out, "w").write(f'<html><body style="margin:0;padding:20px;background:#fff;font-family:sans-serif"><style>.g{{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}} figure{{margin:0;border-radius:18px;padding:12px;text-align:center}} figure img{{width:100%}} img{{display:block}} figcaption{{font-size:13px;margin-top:4px}} .row{{display:flex;gap:6px;justify-content:space-between;align-items:center;padding:10px;margin-top:10px;border-radius:14px}}</style><div class=g>{cells}</div>{small}</body></html>')
