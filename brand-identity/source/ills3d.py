"""The seven standing/volume illustrations rebuilt on iso3d (real meshes, shaded by normal)."""
import math, sys
sys.path.insert(0, "/tmp/hdwm")
import numpy as np
import re
import iso3d as I
from versions import rpoly
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


def rpoly_pts(pts, r, n=10):
    d = rpoly(pts, r); toks = re.findall(r"[MLCz]|-?\d+\.?\d*(?:e-?\d+)?", d); out = []; i = 0; cur = None
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
XZ = ((0, 0, 0), (1, 0, 0), (0, 0, 1), (0, 1, 0))      # outline (x, z), extruded along +y (front = +y, the Cobalt face)
XY = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
def sigm(c, ks=1.3, beta=10.0, tb=0.22):
    m = I.sig_mat(ks=ks, beta=beta); m.topbias = tb; return m

# ------------------------------------------------------------------ bell
def i_bell(c):
    M = mats(c); sc = Scene(c); sig = sigm(c)
    sc.part(); I.sphere(sc, (0, 0, -5.4), 2.3, M["ink"], n=24, layer=0)
    sc.part()
    ctrl = [(0, 12.3), (1.6, 12.1), (3.1, 11.2), (4.2, 9.6), (4.9, 7.6), (5.5, 5.6), (6.5, 3.7), (7.7, 2.2), (8.6, 1.3), (9.0, 0.55)]
    lip = [(9.0, 0.55), (8.9, 0.1), (8.5, -0.25), (8.0, -0.3), (7.4, -0.1)]
    I.lathe(sc, catmull(ctrl, 7)[:-1] + lip, sig, (0, 0, 0), n=120, layer=1)
    sc.part(); I.sphere(sc, (0, 0, 12.6), 1.45, M["gold"], n=24, layer=2)
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
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.9, beta=22, tb=0.0)
    W, D, H = 14.0, 4.8, 13.4
    sc.part(); I.rbox(sc, (0, 0, 0), (W, D, H), 1.2, sig, seg=3)
    sc.part(); I.rbox(sc, (1.7, D - 0.7, 1.7), (W - 1.7, D + 0.38, 10.1), 0.6, M["white"], seg=3, layer=1)
    sc.part(); I.rbox(sc, (7.1, D + 0.1, 2.9), (11.5, D + 0.8, 6.9), 0.85, M["verm"], seg=4, layer=2)
    for x in (4.0, 10.0):
        sc.part(); I.capsule_z(sc, x, D / 2, H, H + 3.4, 0.85, M["ink"], layer=3)
    return sc.render()

# ------------------------------------------------------------------ shield
def bez(p0, p1, p2, p3, n=14):
    return [tuple((1 - t) ** 3 * p0[j] + 3 * (1 - t) ** 2 * t * p1[j] + 3 * (1 - t) * t * t * p2[j] + t ** 3 * p3[j] for j in (0, 1)) for t in [i / n for i in range(n + 1)]]

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
def i_bag(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.9, beta=22, tb=0.0)
    D = 6.6; W = 12.0; H = 12.6
    body = rpoly_pts([(0.7, 0), (W - 0.7, 0), (W - 0.05, H), (0.05, H)], [1.4, 1.4, 0.4, 0.4], 6)
    sc.part(); I.extrude(sc, body, XZ, D, 1.0, sig, seg=4)
    sc.part(); I.rbox(sc, (-0.5, -0.5, H - 2.0), (W + 0.5, D + 0.5, H), 0.75, sig, seg=3, layer=1)
    for y in (1.9, D - 1.9):
        r = 2.75; zc = H + 2.0; path = [(W / 2 - r, y, H - 0.0), (W / 2 - r, y, zc)]
        for i in range(1, 24):
            a = math.pi * i / 24; path.append((W / 2 - r * math.cos(a), y, zc + r * math.sin(a)))
        path += [(W / 2 + r, y, zc), (W / 2 + r, y, H)]
        sc.part(); I.tube(sc, path, 0.85, M["inkm"], sides=14, plane_normal=(0, 1, 0), layer=2)
    sc.dot((W * 0.42, D + 0.0, 6.2), 1.05, M["dot"].solid)
    return sc.render()

# ------------------------------------------------------------------ lock
def i_lock(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.9, beta=22, tb=0.0)
    W, D, H = 12.0, 8.0, 9.0
    sc.part(); I.rbox(sc, (0, 0, 0), (W, D, H), 1.4, sig, seg=3)
    r = 3.4; zc = H + 2.6; y = D / 2; path = [(W / 2 - r, y, H), (W / 2 - r, y, zc)]
    for i in range(1, 28):
        a = math.pi * i / 28; path.append((W / 2 - r * math.cos(a), y, zc + r * math.sin(a)))
    path += [(W / 2 + r, y, zc), (W / 2 + r, y, H)]
    sc.part(); I.tube(sc, path, 1.15, M["inkm"], sides=16, plane_normal=(0, 1, 0), layer=2)
    I.keyhole_left(sc, W / 2, D + 0.02, 5.2, 1.3, M["dot"])
    return sc.render()

# ------------------------------------------------------------------ inbox
def i_inbox(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=0.9, beta=22, tb=0.0)
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
