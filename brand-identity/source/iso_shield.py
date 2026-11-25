import math, re, subprocess, sys
sys.path.insert(0, "/tmp/hdwm"); import final as F, optical as O
C30, S30 = math.cos(math.radians(30)), math.sin(math.radians(30))
FACE_PEAK = ("M47.2 1.7Q50 0 52.8 1.7C62 7.6 78 12.4 94.6 13.6Q100 14 100 19.4L100 52"
        "C100 80.5 81 103 53.6 116.6Q50 118.4 46.4 116.6C19 103 0 80.5 0 52L0 19.4Q0 14 5.4 13.6"
        "C22 12.4 38 7.6 47.2 1.7Z")
# Front view: one smooth arc over the top (no peak), shoulders rounded like the parcel's corners.
FACE_ARC = ("M50 4C64 4 78 8.6 93.6 12.6Q100 14.2 100 20.4L100 52"
        "C100 80.5 81 103 53.6 116.6Q50 118.4 46.4 116.6C19 103 0 80.5 0 52L0 20.4Q0 14.2 6.4 12.6"
        "C22 8.6 36 4 50 4Z")
FACE = FACE_PEAK
def flatten(d, n=14):
    toks = re.findall(r'[MLQCZ]|-?\d*\.?\d+', d); i = 0; pts = []; cur = None; cmd = None
    num = lambda: float(toks[i])
    while i < len(toks):
        t = toks[i]
        if t in "MLQCZ": cmd = t; i += 1
        if cmd == "Z": break
        if cmd in "ML":
            cur = (float(toks[i]), float(toks[i+1])); i += 2; pts.append(cur)
        elif cmd == "Q":
            c1 = (float(toks[i]), float(toks[i+1])); e = (float(toks[i+2]), float(toks[i+3])); i += 4
            for k in range(1, n+1):
                s = k/n; pts.append(tuple((1-s)**2*cur[j] + 2*(1-s)*s*c1[j] + s*s*e[j] for j in (0,1)))
            cur = e
        elif cmd == "C":
            c1 = (float(toks[i]), float(toks[i+1])); c2 = (float(toks[i+2]), float(toks[i+3])); e = (float(toks[i+4]), float(toks[i+5])); i += 6
            for k in range(1, n+1):
                s = k/n; pts.append(tuple((1-s)**3*cur[j] + 3*(1-s)**2*s*c1[j] + 3*(1-s)*s*s*c2[j] + s**3*e[j] for j in (0,1)))
            cur = e
    if pts[0] == pts[-1]: pts.pop()
    return pts
OUT_PTS = flatten(FACE)
ARC_PTS = flatten(FACE_ARC)
TICK = [(26, 59), (40, 80), (75, 64)]   # chosen in the face plane so it reads as a level tick once skewed
def hexc(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
def mix(a, b, t): return "#%02x%02x%02x" % tuple(round(a[i]+(b[i]-a[i])*t) for i in range(3))
LID, LID2, BLUE, BLUE2 = hexc("#ffe88a"), hexc("#ffc83c"), hexc("#2380ff"), hexc("#2d58ee")
RIGHT, RIGHT2 = hexc("#c94400"), hexc("#962a00")
def shield(depth=21, flat=False, small=False, uid="s", front_view=False):
    if front_view:
        # square-on face; depth runs back to the upper right at 30°, so the lid and the right side show
        P = lambda u, v: (u, v)
        ex, ey = C30*depth*0.62, -S30*depth*0.62
    else:
        # right-face plane of the parcel: u runs back-right (rising 30°), v straight down
        P = lambda u, v: (C30*u, -S30*u + v)
        ex, ey = -C30*depth, -S30*depth          # depth runs back-left, like the parcel's left face
    poly = lambda ps: " ".join(f"{x:.2f},{y:.2f}" for x, y in ps)
    OUT = OUT_PTS   # the shield keeps its own outline (owner: do not change the shape)
    front = [P(u, v) for u, v in OUT]
    sides = []
    if not flat:
        n = len(OUT)
        for i in range(n):
            (u0, v0), (u1, v1) = OUT[i], OUT[(i+1) % n]
            a, b = P(u0, v0), P(u1, v1)
            # outward normal in screen space (outline runs clockwise on screen)
            sx, sy = b[0]-a[0], b[1]-a[1]; L = math.hypot(sx, sy) or 1
            nx, ny = sy/L, -sx/L
            if nx*ex + ny*ey <= 0: continue          # faces away from the viewer
            # light: facing up = lid (Marigold), facing left = Cobalt; deeper as it turns down
            # the top edge is the lid (Marigold); every other edge is the side (Cobalt), creased like the cube
            if front_view:
                # shade by which way the surface faces: up = lid (Marigold), right = side (deep
                # Vermilion), turning smoothly round the rounded shoulder instead of switching
                ang = math.degrees(math.atan2(ny, nx))      # -90 up, 0 right, 90 down
                t = min(1.0, max(0.0, (ang + 38) / 38))      # lid until the surface turns past 38° from right
                t = t*t*(3 - 2*t)
                lid = mix(LID, LID2, min(1, (1-max(0.0, -ny))*1.2))
                side = mix(RIGHT, RIGHT2, min(1, max(0.0, ny)*1.2))
                col = mix(hexc(lid), hexc(side), t)
            elif max(v0, v1) < 15:
                col = mix(LID, LID2, min(1, (1-max(0.0, -ny))*1.4))
            else:
                col = mix(BLUE, BLUE2, min(1, max(0.0, ny)*1.3 + 0.1))
            q = [a, b, (b[0]+ex, b[1]+ey), (a[0]+ex, a[1]+ey)]
            sides.append(f'<polygon fill="{col}" stroke="{col}" stroke-width=".6" stroke-linejoin="round" points="{poly(q)}"/>')
    gid = f"{uid}f"
    defs = (f'<linearGradient id="{gid}" x1="0" y1="{min(p[1] for p in front):.1f}" x2="0" y2="{max(p[1] for p in front):.1f}" gradientUnits="userSpaceOnUse">'
            f'<stop stop-color="#fb6603"/><stop offset="1" stop-color="#e44000"/></linearGradient>')
    body = "".join(sides) + f'<polygon fill="url(#{gid})" points="{poly(front)}"/>'
    if not small and not front_view:   # rim light along the face's top edge, as on the parcel's lid
        top = [P(u, v) for u, v in OUT if v < 15.5]
        body += f'<polyline fill="none" stroke="#fff6d1" stroke-opacity=".6" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" points="{poly(top)}"/>'
    sw = 12.5 if small else 11
    tick = [(29, 59), (44.5, 74), (72, 44)] if front_view else TICK
    body += f'<polyline fill="none" stroke="#ffffff" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" points="{poly([P(*p) for p in tick])}"/>'
    allp = front + ([(x+ex, y+ey) for x, y in front] if not flat else [])
    xs = [p[0] for p in allp]; ys = [p[1] for p in allp]
    return f"<defs>{defs}</defs>{body}", (min(xs), min(ys), max(xs)-min(xs), max(ys)-min(ys))
if __name__ == "__main__":
    import sys as _s
    FV = "front" in _s.argv
    def doc(n, bg, small, pad, flat=False):
        art, (bx, by, bw, bh) = shield(small=small, flat=flat, uid=f"d{n}", front_view=FV)
        s = n*(1-2*pad)/max(bw, bh); tx = (n-bw*s)/2-bx*s; ty = (n-bh*s)/2-by*s
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n} {n}" width="{n}" height="{n}"><rect width="{n}" height="{n}" fill="{bg}"/><g transform="translate({tx:.2f} {ty:.2f}) scale({s:.4f})">{art}</g></svg>'
    for name, svg in [("iso-big", doc(512, "#f2f2f7", False, .08)), ("iso-32", doc(32, "#f2f2f7", True, .03)),
                      ("iso-16", doc(16, "#f2f2f7", True, .02)), ("iso-icon", doc(512, "#16171b", False, .2))]:
        p = f"/tmp/trustopt/{'fv-' if FV else ''}{name}.svg"; open(p, "w").write(svg); subprocess.run(["rsvg-convert", p, "-o", p[:-4]+".png"], check=True)
    # beside the parcel, same height, to check they read as one family
    c = F.square("light", 512)
    open("/tmp/trustopt/parcel.svg", "w").write(c); subprocess.run(["rsvg-convert", "/tmp/trustopt/parcel.svg", "-o", "/tmp/trustopt/parcel.png"], check=True)
    print("ok")
