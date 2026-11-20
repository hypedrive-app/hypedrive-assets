
def i_search(c):
    M = mats(c); sc = Scene(c); sig = sigm(c, ks=1.0, beta=400, tb=0.2)
    Rr = 6.0; tr = 1.35; ca, sa = math.cos(math.radians(-45)), math.sin(math.radians(-45))
    glass = I.Mat((I.Ramp("#cfe6ff", "#9ccaff"),) * 3, mono=True, ks=0.3)
    sc.part(); I.poly(sc, [((Rr - 0.6) * math.cos(a), -0.3, (Rr - 0.6) * math.sin(a)) for a in [2 * math.pi * i / 64 for i in range(64)]], (0, 1, 0), glass, layer=0)
    arc_pts = [(3.3 * math.cos(math.radians(a)), 3.3 * math.sin(math.radians(a))) for a in range(105, 171, 11)]
    seg_decal(sc, -0.25, arc_pts, 0.75, M["dot"], layer=1)
    ring = [(Rr * math.cos(a), 0.0, Rr * math.sin(a)) for a in [2 * math.pi * i / 80 for i in range(80)]]
    sc.part(); I.tube(sc, ring, tr, sig, sides=18, closed=True, plane_normal=(0, 1, 0), layer=2)
    p0 = (Rr + tr * 0.4) * np.array([ca, 0, sa]); d = np.array([ca, 0, sa])
    sc.part(); I.tube(sc, [p0 + d * t for t in np.linspace(0.0, 2.6, 6)], 1.95, sig, sides=18, plane_normal=(0, 1, 0), layer=3, cap_ends=True)
    sc.part(); I.tube(sc, [p0 + d * t for t in np.linspace(1.6, 11.5, 12)], 1.25, M["ink"], sides=16, plane_normal=(0, 1, 0), layer=3)
    sc.part(); I.sphere(sc, tuple(p0 + d * 11.5), 1.25, M["ink"], n=16, layer=3)
    return sc.render()
