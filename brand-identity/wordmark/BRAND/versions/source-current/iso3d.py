"""Small software 3D renderer for the Hypedrive illustrations.
Meshes (rounded box, lathe, outline extrusion with rounded edges, swept ring, swept tube, sphere, decal) go into a Scene;
Scene.render() projects with the brand's true-30deg iso P(), culls back facets, sorts far to near (painter) and shades every
facet by its normal, mapped onto the brand palette: the dominant axis picks the tone (up Marigold, +y Cobalt, +x Vermilion),
tones blend smoothly across curved surfaces in OKLCH, and the position / tilt picks the point on that tone's ramp.
Output is plain SVG (flat fills, linear gradients, same-colour hairline strokes against anti-alias seams; no masks)."""
import sys, math
sys.path.insert(0, "/tmp/hdwm")
import numpy as np
import palette as PL

GRAD_MIN = 6.0
QSMALL = 1
C30 = math.cos(math.radians(30))
VIEW = np.array([1.0, 1.0, 1.0]) / math.sqrt(3)


def proj(V):
    V = np.asarray(V, float)
    return np.stack([(V[:, 0] - V[:, 1]) * C30, (V[:, 0] + V[:, 1]) * 0.5 - V[:, 2]], 1)


# ------------------------------------------------------------------ colour
def qhex(h, q=1):
    return "#" + "".join(f"{min(255, int(round(int(h[i:i + 2], 16) / q)) * q):02x}" for i in (1, 3, 5))
def hex2rgb(h): return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)], float) / 255
def rgb2hex(c): return "#" + "".join(f"{int(round(min(1, max(0, v)) * 255)):02x}" for v in c)
def mixhex(a, b, k): return rgb2hex(hex2rgb(a) * (1 - k) + hex2rgb(b) * k)

def _lin(v): return np.where(v <= 0.04045, v / 12.92, ((v + 0.055) / 1.055) ** 2.4)
_lch_cache = {}
def hex2lch(h):
    if h in _lch_cache: return _lch_cache[h]
    r, g, b = _lin(hex2rgb(h))
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = np.cbrt(l), np.cbrt(m), np.cbrt(s)
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    bb = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    C = math.hypot(a, bb); H = math.degrees(math.atan2(bb, a)) % 360
    if H > 200: H -= 360                       # unwrapped so cobalt(-102) < vermilion(40) < marigold(90): blends run through warm hues
    out = (float(L), C, H); _lch_cache[h] = out; return out

def blend(cols, w):
    """Weighted OKLCH mix (hue on the unwrapped axis)."""
    L = C = H = 0.0
    for c, k in zip(cols, w):
        l, ch, h = hex2lch(c); L += k * l; C += k * ch; H += k * h
    return PL.oklch_to_hex(L, C * (1 - 0.5 * (1 - max(w))), H % 360)


class Ramp:
    """Anchors at t = -1, 0, 1, 2 (lighter, stop0, stop1, deeper). 0..1 is exactly the brand's two-stop gradient."""
    T = (-1.0, 0.0, 1.0, 2.0)
    def __init__(self, a, b, hl=None, dk=None):
        self.c = [np.array(hex2rgb(x)) for x in (hl or mixhex(a, "#ffffff", 0.35), a, b, dk or mixhex(b, "#000000", 0.22))]
    def __call__(self, t):
        t = min(2.0, max(-1.0, t))
        i = min(2, int(math.floor(t + 1)))
        k = t - (i - 1)
        return rgb2hex(self.c[i] * (1 - k) + self.c[i + 1] * k)


class Mat:
    """ramps = (top, left, right) Ramp triple. mono: one ramp, shaded by absolute light. solid: a fixed colour."""
    _n = 0
    def __init__(self, ramps=None, solid=None, mono=False, ks=0.9, beta=14.0, topbias=0.0):
        Mat._n += 1; self.id = Mat._n
        self.ramps = ramps; self.solid = solid; self.mono = mono; self.ks = ks; self.beta = beta; self.topbias = topbias; self.ring = False; self.tonefn = None


def sig_mat(ks=0.9, beta=14.0):
    return Mat((Ramp("#fff0a6", "#ffdb68", "#fff8cc", "#ffc84c"),
                Ramp("#2380ff", "#2d58ee", "#63a6ff", "#2348ce"),
                Ramp("#fb6603", "#e44000", "#ffa56a", "#c73f15")), ks=ks, beta=beta)

def verm_mat(ks=0.9):
    """Vermilion as an accent material (ribbon, date block): lighter top, vermilion left, deeper right."""
    return Mat((Ramp("#ff9a5c", "#ff7a2e", "#ffc29a", "#fb6603"), Ramp("#fb6603", "#e44000", "#ff8a3d", "#c73f15"),
                Ramp("#d9400f", "#b52a0e", "#e44000", "#8f1d0a")), ks=ks)

def verm_mono(ks=0.8):
    return Mat((Ramp("#fb6603", "#e44000", "#ff9a5c", "#c73f15"),) * 3, mono=True, ks=ks)

def cavity_mat(ks=0.7):
    return Mat((Ramp("#2a3fcf", "#232aa0", "#3b55e6", "#191b78"), Ramp("#2348ce", "#292da8", "#2d58ee", "#1c1f86"),
                Ramp("#c73f15", "#a82418", "#e44000", "#7d150f")), ks=ks)

def ink_mat(theme, ks=0.9):
    if theme == "light":
        t, l, r = PL.INK_L
    else:
        t, l, r = ("#646975", "#50545e"), ("#40434c", "#2d3038"), ("#2d3038", "#23262d")
    hl = (lambda a: mixhex(a, "#ffffff", 0.3))
    return Mat((Ramp(*t, hl=hl(t[0])), Ramp(*l, hl=hl(l[0])), Ramp(*r, hl=hl(r[0]))), ks=ks)

def ink_mono(theme, ks=0.8):
    m = ink_mat(theme, ks); m.ramps = (m.ramps[1],) * 3; m.mono = True; return m

def white_mat(theme, ks=0.5):
    if theme == "light":
        return Mat((Ramp("#ffffff", "#f4f5f8", dk="#e3e4e9"), Ramp("#ffffff", "#eceef3", hl="#ffffff", dk="#d5d7dd"),
                    Ramp("#e3e4e9", "#cfd2da", hl="#f0f1f5", dk="#b9bcc4")), ks=ks)
    return Mat((Ramp("#3a3d44", "#30333a"), Ramp("#30333a", "#25272d"), Ramp("#25272d", "#1c1e23")), ks=ks)

def solid_mat(hexc): return Mat(solid=hexc)

LIGHT = np.array([-0.45, 0.5, 0.75]); LIGHT /= np.linalg.norm(LIGHT)
TAXES = [np.array([0, 0, 1.0]), np.array([0, 1.0, 0]), np.array([1.0, 0, 0])]   # tone 0 top, 1 left(+y), 2 right(+x)


def _unit(v): v = np.asarray(v, float); return v / (np.linalg.norm(v) + 1e-12)


# ------------------------------------------------------------------ scene
class Facet:
    __slots__ = ("V", "n", "mat", "grp", "layer", "dt", "scr", "dom", "depth", "fixed", "tag", "fill")


def tone_of(m, n):
    if m.tonefn: return m.tonefn(n)
    if m.ring:
        h = math.hypot(n[0], n[1])
        if n[2] - m.topbias > 0.7071 * h: return 0
        return 1 if n[1] >= n[0] else 2
    return int(np.argmax([n[2] - m.topbias, n[1], n[0]]))


class Scene:
    def __init__(self, c, sw=0.22):
        self.c = c; self.F = []; self.grp = 0; self.sw = sw; self.gcache = {}

    def part(self): self.grp += 1; return self.grp

    def dot(self, centre, R, colour, layer=9, n=64):
        """A true circle on screen (the parcel's dot): centre in 3D, radius in screen units."""
        f = Facet(); f.V = np.array([centre], float); f.n = np.array([0, 1.0, 0]); f.mat = solid_mat(colour); f.grp = self.grp; f.layer = layer; f.dt = 0.0; f.tag = None
        c0 = proj(f.V)[0]; f.scr = np.array([(c0[0] + R * math.cos(2 * math.pi * i / n), c0[1] + R * math.sin(2 * math.pi * i / n)) for i in range(n)])
        f.fixed = True; self.F.append(f)

    def add(self, V, n, mat, layer=0, dt=0.0, tag=None):
        f = Facet(); f.V = np.asarray(V, float); f.n = _unit(n); f.mat = mat; f.grp = self.grp; f.layer = layer; f.dt = dt; f.fixed = False; f.tag = tag
        self.F.append(f)

    # ---- colour of a facet at screen height sy
    def colour(self, f, sy, rng):
        m = f.mat
        if m.solid: return m.solid
        n = f.n
        if m.mono:
            lo, hi = rng[(f.grp, m.id, 0)]
            t = (sy - lo) / (hi - lo) + f.dt - m.ks * (float(n @ LIGHT) - 0.45)
            return m.ramps[0](t)
        if m.beta >= 100:
            k = tone_of(m, n); lo, hi = rng[(f.grp, m.id, k)]
            t = (sy - lo) / (hi - lo) + f.dt - m.ks * (float(n @ LIGHT) - float(TAXES[k] @ LIGHT) if k < 3 else 0.0)
            return m.ramps[k](t)
        v = np.array([n[2] - m.topbias, n[1], n[0]]); e = np.exp(m.beta * (v - v.max())); w = e / e.sum()
        cols = []; ws = []
        for k in range(3):
            if w[k] < 0.02: continue
            lo, hi = rng[(f.grp, m.id, k)]
            t = (sy - lo) / (hi - lo) + f.dt - m.ks * (float(n @ LIGHT) - float(TAXES[k] @ LIGHT))
            cols.append(m.ramps[k](t)); ws.append(w[k])
        if len(cols) == 1: return cols[0]
        s = sum(ws); return blend(cols, [x / s for x in ws])

    def grad(self, a, b, stops):
        key = (round(a, 2), round(b, 2), tuple(stops))
        if key in self.gcache: return self.gcache[key]
        c = self.c; gid = c.id("g")
        st = "".join(f'<stop offset="{o:.3f}" stop-color="{col}"/>' for o, col in stops)
        c.defs.append(f'<linearGradient id="{gid}" x1="0" y1="{a:.2f}" x2="0" y2="{b:.2f}" gradientUnits="userSpaceOnUse">{st}</linearGradient>')
        self.gcache[key] = f"url(#{gid})"; return self.gcache[key]

    @staticmethod
    def _run(cur):
        return [cur['layer'], sum(cur['d']) / len(cur['d']), cur['fill'], cur['top'] + cur['bot'][::-1]]

    def render(self):
        vis = []
        for f in self.F:
            if f.n @ VIEW < 0.01: continue
            if not f.fixed: f.scr = proj(f.V)
            f.depth = float(f.V.sum(1).mean()); f.dom = tone_of(f.mat, f.n)
            vis.append(f)
        rng = {}
        for f in vis:
            ks = [0] if f.mat.mono else [f.dom]
            for k in ks:
                key = (f.grp, f.mat.id, k); a, b = f.scr[:, 1].min(), f.scr[:, 1].max()
                if key in rng: rng[key] = (min(rng[key][0], a), max(rng[key][1], b))
                else: rng[key] = (a, b)
        for key in list(rng):                              # tones that never dominate still need a range: use the group's
            lo, hi = rng[key]; rng[key] = (lo, hi if hi - lo > 1e-6 else lo + 1)
        glo = {}
        for (g, m, k), (a, b) in rng.items():
            glo[(g, m)] = (min(glo.get((g, m), (a, b))[0], a), max(glo.get((g, m), (a, b))[1], b))
        for f in vis:
            for k in range(len(f.mat.ramps) if f.mat.ramps else 3): rng.setdefault((f.grp, f.mat.id, k), glo[(f.grp, f.mat.id)])
        items = []                                           # (layer, depth, fill, pts)
        runs = {}
        for f in vis:
            sy = f.scr[:, 1]; lo, hi = float(sy.min()), float(sy.max())
            if hi - lo > GRAD_MIN and not f.mat.solid:
                stops = [(o, self.colour(f, lo + o * (hi - lo), rng)) for o in (0.0, 0.5, 1.0)]
                fill = stops[0][1] if stops[0][1] == stops[1][1] == stops[2][1] else self.grad(lo, hi, stops)
            else:
                fill = self.colour(f, float(sy.mean()), rng)
                if not f.mat.solid: fill = qhex(fill, QSMALL)
            f.fill = fill
            if f.tag is not None and not fill.startswith("url"): runs.setdefault(f.tag[0], []).append(f)
            else: items.append([f.layer, f.depth, fill, [tuple(p) for p in f.scr]])
        for row, fs in runs.items():                          # merge neighbours of one strip that ended up the same colour
            fs.sort(key=lambda f: f.tag[1]); cur = None
            for f in fs:
                if cur and cur["fill"] == f.fill and cur["col"] + 1 == f.tag[1] and cur["layer"] == f.layer:
                    cur["top"].append(tuple(f.scr[1])); cur["bot"].append(tuple(f.scr[2])); cur["col"] = f.tag[1]; cur["d"].append(f.depth)
                else:
                    if cur: items.append(self._run(cur))
                    cur = dict(fill=f.fill, col=f.tag[1], layer=f.layer, top=[tuple(f.scr[0]), tuple(f.scr[1])], bot=[tuple(f.scr[3]), tuple(f.scr[2])], d=[f.depth])
            if cur: items.append(self._run(cur))
        items.sort(key=lambda it: (it[0], it[1]))
        out = ['<g stroke-linejoin="round" stroke-width="%s">' % self.sw]
        for layer, depth, fill, pts in items:
            ps = " ".join(f"{p[0]:.2f},{p[1]:.2f}".replace(".00", "") for p in pts)
            out.append(f'<polygon fill="{fill}" stroke="{fill}" points="{ps}"/>')
            self.c.pts += pts
        out.append("</g>")
        return "".join(out)


# ------------------------------------------------------------------ builders
def rbox(sc, lo, hi, r, mat, seg=3, skip=(), layer=0, dt=0.0):
    """Rounded box lo..hi (3-vectors), bevel radius r, seg segments per 45deg half-bevel. skip: {(axis, sign)} faces to omit."""
    lo = np.array(lo, float); hi = np.array(hi, float); rv = np.broadcast_to(np.asarray(r, float), (3,)).copy(); ilo = lo + rv; ihi = hi - rv
    ang = [math.radians(45.0 * i / seg) for i in range(seg + 1)]
    for c in range(3):
        for s in (1, -1):
            if (c, s) in skip: continue
            a, b = [i for i in range(3) if i != c]
            def stops(ax):
                return [(ilo[ax], -p) for p in reversed(ang)] + [(ihi[ax], p) for p in ang]
            SA, SB = stops(a), stops(b)
            Pm = np.zeros((len(SA), len(SB), 3)); Nm = np.zeros_like(Pm)
            for i, (qa, pa) in enumerate(SA):
                for j, (qb, pb) in enumerate(SB):
                    n = np.zeros(3); n[c] = s; n[a] = math.tan(pa); n[b] = math.tan(pb); n = _unit(n)
                    q = np.zeros(3); q[c] = ihi[c] if s > 0 else ilo[c]; q[a] = qa; q[b] = qb
                    Pm[i, j] = q + rv * n; Nm[i, j] = _unit(n / rv)
            for i in range(len(SA) - 1):
                for j in range(len(SB) - 1):
                    V = [Pm[i, j], Pm[i + 1, j], Pm[i + 1, j + 1], Pm[i, j + 1]]
                    sc.add(V, Nm[i:i + 2, j:j + 2].reshape(-1, 3).sum(0), mat, layer, dt)


def arc(c0, R, a0, a1, n):
    return [(c0[0] + R * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c0[1] + R * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def inset_ring(outline, s):
    p = np.array(outline, float); e = np.roll(p, -1, 0) - p; d = e / np.linalg.norm(e, axis=1)[:, None]
    nin = np.stack([-d[:, 1], d[:, 0]], 1); npv = np.roll(nin, 1, 0)
    off = (nin + npv) / (1 + (nin * npv).sum(1))[:, None]
    return p + off * s, nin


def ccw(outline):
    q = [outline[0]]
    for x in outline[1:]:
        if math.dist(x, q[-1]) > 1e-4: q.append(x)
    if math.dist(q[0], q[-1]) < 1e-4: q.pop()
    p = np.array(q, float); a = (p[:, 0] * np.roll(p[:, 1], -1) - np.roll(p[:, 0], -1) * p[:, 1]).sum()
    return [tuple(x) for x in (p if a > 0 else p[::-1])]


def sweep(sc, outline, frame, profile, mat, layer=0, dt=0.0, cap_front=None, cap_mat=None, visible_only=False):
    """Sweep a profile [(s inset, w height)] around a closed outline (2D, in the frame's (u,v) plane).
    Profile is walked so that its normal (-dw, ds) in (inward, w) faces out of the solid."""
    O, U, Vv, W = [np.array(x, float) for x in frame]
    outline = ccw(outline); N = len(outline)
    rings = []
    for s, w in profile:
        ring, nin = inset_ring(outline, s); rings.append((ring, w))
    def to3(p, w): return O + p[0] * U + p[1] * Vv + w * W
    for k in range(len(profile) - 1):
        (r0, w0), (r1, w1) = rings[k], rings[k + 1]
        ds = profile[k + 1][0] - profile[k][0]; dw = w1 - w0
        L = math.hypot(ds, dw)
        if L < 1e-9: continue
        ns, nw = -dw / L, ds / L
        for j in range(N):
            j2 = (j + 1) % N
            if visible_only and -(nin[j][0] * U + nin[j][1] * Vv) @ VIEW < 0.02: continue
            V = [to3(r0[j], w0), to3(r0[j2], w0), to3(r1[j2], w1), to3(r1[j], w1)]
            ni = nin[j]; n = ns * (-(-ni[0] * U - ni[1] * Vv)) + nw * W      # inward = +ni mapped to 3D
            n = ns * (ni[0] * U + ni[1] * Vv) + nw * W
            sc.add(V, n, mat, layer, dt)
    return rings, to3


def cap(sc, ring, w, frame, normal_sign, mat, layer=0, dt=0.0):
    O, U, Vv, W = [np.array(x, float) for x in frame]
    V = [O + p[0] * U + p[1] * Vv + w * W for p in ring]
    sc.add(V, normal_sign * W, mat, layer, dt)


def extrude(sc, outline, frame, depth, r, mat, seg=4, layer=0, dt=0.0, back=True):
    """Outline extruded along the frame's W with rounded edges (radius r). Front cap at w = depth (normal +W)."""
    prof = []
    if back:
        prof += [(r, 0.0)] + [(x, y) for x, y in arc((r, r), r, 270, 180, seg)[1:]]
    else:
        prof += [(0.0, 0.0)]
    prof += [(x, y) for x, y in arc((r, depth - r), r, 180, 90, seg)]
    rings, to3 = sweep(sc, outline, frame, prof, mat, layer, dt)
    cap(sc, rings[-1][0], depth, frame, +1, mat, layer, dt)
    if back: cap(sc, rings[0][0], 0.0, frame, -1, mat, layer, dt)
    return rings


_LID = 0
def lathe(sc, profile, mat, center=(0, 0, 0), n=48, layer=0, dt=0.0, closed_top=True):
    """Solid of revolution about +z. profile [(r, z)] walked top -> bottom along the outside."""
    global _LID
    _LID += 1; lid = _LID
    cx, cy, cz = center; prof = np.array(profile, float)
    th = [2 * math.pi * i / n for i in range(n + 1)]
    for k in range(len(prof) - 1):
        (r0, z0), (r1, z1) = prof[k], prof[k + 1]
        dr, dz = r1 - r0, z1 - z0; L = math.hypot(dr, dz)
        if L < 1e-9: continue
        nr, nz = -dz / L, dr / L
        for i in range(n):
            t0, t1 = th[i], th[i + 1]; tm = (t0 + t1) / 2
            V = [(cx + r0 * math.cos(t0), cy + r0 * math.sin(t0), cz + z0), (cx + r0 * math.cos(t1), cy + r0 * math.sin(t1), cz + z0),
                 (cx + r1 * math.cos(t1), cy + r1 * math.sin(t1), cz + z1), (cx + r1 * math.cos(t0), cy + r1 * math.sin(t0), cz + z1)]
            if r0 < 1e-9: V = V[1:]
            sc.add(V, (nr * math.cos(tm), nr * math.sin(tm), nz), mat, layer, dt, tag=((lid, k), i) if r0 > 1e-9 else None)


def sphere(sc, c, R, mat, n=28, layer=0, dt=0.0):
    prof = [(R * math.sin(math.pi * i / (n // 2)), R * math.cos(math.pi * i / (n // 2))) for i in range(n // 2 + 1)]
    lathe(sc, prof, mat, c, n, layer, dt)


def capsule_z(sc, x, y, z0, z1, R, mat, layer=0, n=20, dt=0.0):
    """Vertical capsule: cylinder z0..z1 with a domed top and flat (buried) bottom."""
    seg = 6
    prof = [(R * math.sin(math.pi / 2 * i / seg), z1 - R + R * math.cos(math.pi / 2 * i / seg)) for i in range(seg + 1)] + [(R, z0)]
    lathe(sc, prof, mat, (x, y, 0), n, layer, dt)


def tube(sc, path, R, mat, sides=14, closed=False, plane_normal=None, layer=0, dt=0.0, cap_ends=False):
    """Swept tube along a polyline. plane_normal: constant binormal for planar paths (exact frames)."""
    p = np.array(path, float); M = len(p)
    if closed: T = np.roll(p, -1, 0) - np.roll(p, 1, 0)
    else:
        T = np.zeros_like(p); T[1:-1] = p[2:] - p[:-2]; T[0] = p[1] - p[0]; T[-1] = p[-1] - p[-2]
    T = T / np.linalg.norm(T, axis=1)[:, None]
    B = _unit(plane_normal)
    Nn = np.cross(T, B); Nn /= np.linalg.norm(Nn, axis=1)[:, None]
    ring = []
    rr = R if callable(R) else (lambda i: R)
    for i in range(M):
        row = []
        for s in range(sides):
            a = 2 * math.pi * s / sides; n = math.cos(a) * Nn[i] + math.sin(a) * B
            row.append((p[i] + rr(i) * n, n))
        ring.append(row)
    top = M if closed else M - 1
    for i in range(top):
        i2 = (i + 1) % M
        for s in range(sides):
            s2 = (s + 1) % sides
            V = [ring[i][s][0], ring[i][s2][0], ring[i2][s2][0], ring[i2][s][0]]
            n = ring[i][s][1] + ring[i][s2][1] + ring[i2][s2][1] + ring[i2][s][1]
            sc.add(V, n, mat, layer, dt)
    if cap_ends and not closed:
        for idx, sgn in ((0, -1), (M - 1, 1)):
            sc.add([ring[idx][s][0] for s in range(sides)], sgn * T[idx], mat, layer, dt)


def poly(sc, V, n, mat, layer=0, dt=0.0): sc.add(V, n, mat, layer, dt)


def disc(sc, centre, normal, R, mat, n=28, layer=1):
    nn = _unit(normal); a = _unit(np.cross(nn, [0, 0, 1.0]) if abs(nn[2]) < 0.9 else np.cross(nn, [1.0, 0, 0])); b = np.cross(nn, a)
    c0 = np.array(centre, float)
    sc.add([c0 + R * (math.cos(2 * math.pi * i / n) * a + math.sin(2 * math.pi * i / n) * b) for i in range(n)], nn, mat, layer)


def keyhole_left(sc, x, y, z, R, mat, layer=5):
    """Keyhole decal on a +y face: a disc and a flared stem (flat polygons, y = const)."""
    n = 28
    sc.add([(x + R * math.cos(2 * math.pi * i / n), y, z + R * math.sin(2 * math.pi * i / n)) for i in range(n)], (0, 1, 0), mat, layer)
    sc.add([(x - R * 0.42, y, z), (x + R * 0.42, y, z), (x + R * 0.78, y, z - R * 1.9), (x - R * 0.78, y, z - R * 1.9)], (0, 1, 0), mat, layer)


def rrect(w, h, r, n=8, x0=0.0, y0=0.0):
    pts = []
    for (cx, cy, a0) in ((w - r, r, 270), (w - r, h - r, 0), (r, h - r, 90), (r, r, 180)):
        for x, y in arc((cx, cy), r, a0, a0 + 90, n): pts.append((x0 + x, y0 + y))
    return pts
