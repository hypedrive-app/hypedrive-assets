"""Hypedrive isometric parcel — the chosen icon, rebuilt on a true 30° grid and polished.
Top = yellow, front-left = blue (label dot), front-right = orange, ink tape over the lid and down the right face."""
import sys, os, math, subprocess
sys.path.insert(0, "/tmp/hdwm")
from versions import rpoly
from text2path import text_path

C30, S30 = math.cos(math.radians(30)), 0.5
W = D = 10.0; H = 10.0                     # a true cube
TAPE = 1.15                                # half-width of the tape
TAPE_DROP = 4.6                            # how far the tape runs down the right face
R_OUT = 1.25                               # outer silhouette corner radius (in iso units)
DOT = (3.1, 4.6, 1.05)                     # label dot on the front-left face: x, z, r

YELL = ("#ffe066", "#ffc21a")
BLUE = ("#3d7dff", "#1a54f0")
ORNG = ("#ff6a24", "#d93d00")
THEMES = {
    "light": dict(ink="#141414", tape_top="#2b2b2e", tape_side="#111113", dot="#ffffff"),
    "dark":  dict(ink="#ffffff", tape_top="#ffffff", tape_side="#d6d6dc", dot="#141414"),
}

def P(x, y, z): return (x*C30 - y*C30, (x + y)*S30 - z)
def pts(*p3): return " ".join(f"{a:.3f},{b:.3f}" for a, b in (P(*p) for p in p3))

def mark(theme, uid="hd"):
    t = THEMES[theme]
    sil = [P(0, 0, H), P(W, 0, H), P(W, 0, 0), P(W, D, 0), P(0, D, 0), P(0, D, H)]
    clip = rpoly(sil, R_OUT)
    m = D / 2
    g = []
    g.append(f'<defs><clipPath id="{uid}-c"><path d="{clip}"/></clipPath>'
             f'<linearGradient id="{uid}-t" x1="0" y1="{P(0,0,H)[1]:.2f}" x2="0" y2="{P(W,D,H)[1]:.2f}" gradientUnits="userSpaceOnUse"><stop stop-color="{YELL[0]}"/><stop offset="1" stop-color="{YELL[1]}"/></linearGradient>'
             f'<linearGradient id="{uid}-l" x1="0" y1="{P(0,D,H)[1]:.2f}" x2="0" y2="{P(W,D,0)[1]:.2f}" gradientUnits="userSpaceOnUse"><stop stop-color="{BLUE[0]}"/><stop offset="1" stop-color="{BLUE[1]}"/></linearGradient>'
             f'<linearGradient id="{uid}-r" x1="0" y1="{P(W,0,H)[1]:.2f}" x2="0" y2="{P(W,D,0)[1]:.2f}" gradientUnits="userSpaceOnUse"><stop stop-color="{ORNG[0]}"/><stop offset="1" stop-color="{ORNG[1]}"/></linearGradient></defs>')
    g.append(f'<g clip-path="url(#{uid}-c)">')
    # faces — each overdrawn by a hair past the shared edges so no AA seam shows; outer edge is clipped
    e = 0.06
    g.append(f'<polygon fill="url(#{uid}-l)" points="{pts((0,D,0),(W+e,D,0),(W+e,D,H+e),(0,D,H+e))}"/>')
    g.append(f'<polygon fill="url(#{uid}-r)" points="{pts((W,-0.0,0),(W,D,0),(W,D,H),(W,0,H))}"/>')
    g.append(f'<polygon fill="url(#{uid}-t)" points="{pts((0,0,H),(W,0,H),(W,D,H),(0,D,H))}"/>')
    # tape: across the lid along x, then over the edge and down the right face
    g.append(f'<polygon fill="{t["tape_top"]}" points="{pts((-1,m-TAPE,H),(W,m-TAPE,H),(W,m+TAPE,H),(-1,m+TAPE,H))}"/>')
    g.append(f'<polygon fill="{t["tape_side"]}" points="{pts((W,m-TAPE,H),(W,m+TAPE,H),(W,m+TAPE,H-TAPE_DROP),(W,m-TAPE,H-TAPE_DROP))}"/>')
    g.append('</g>')
    # label dot, drawn in the plane of the front-left face
    cx, cy = P(DOT[0], D, DOT[1])
    g.append(f'<circle cx="{cx:.3f}" cy="{cy:.3f}" r="{DOT[2]}" fill="{t["dot"]}"/>')
    xs = [p[0] for p in sil]; ys = [p[1] for p in sil]
    return "".join(g), (min(xs), min(ys), max(xs), max(ys))

def fitted(theme, h, uid):
    body, (x0, y0, x1, y1) = mark(theme, uid)
    k = h / (y1 - y0)
    return f'<g transform="scale({k:.5f}) translate({-x0:.3f} {-y0:.3f})">{body}</g>', (x1 - x0) * k

FONT, WGHT, CAP, TRACK, SOFT, GAP = "Bricolage", 700, 18.6, -0.01, 0.45, 8.5
AXES = {"opsz": 96, "wdth": 100}

def lockup(theme, font=None, wght=None, axes=None, soft=None, track=None):
    font = font or FONT; wght = wght or WGHT; axes = AXES if axes is None else axes
    soft = SOFT if soft is None else soft; track = TRACK if track is None else track
    ink = THEMES[theme]["ink"]
    m, mw = fitted(theme, 28, "hdl")
    d, tw = text_path("Hypedrive", wght, CAP, track, font, axes)
    ox = mw + GAP; Wd = ox + tw + soft; pad = 1
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {Wd+2*pad:.2f} {28+2*pad}" width="{(Wd+2*pad)*10:.0f}" height="{(28+2*pad)*10:.0f}">'
            f'{m}<path fill="{ink}" stroke="{ink}" stroke-width="{soft}" stroke-linejoin="round" transform="translate({ox:.2f} 22.9)" d="{d}"/></svg>')

def icon(theme, size=512, pad_ratio=0.1, tile=None):
    """Square mark; tile = background colour for app icon tiles."""
    s = 100.0; inner = s * (1 - 2*pad_ratio)
    m, mw = fitted(theme, inner, "hdi")
    ox = (s - mw) / 2; oy = (s - inner) / 2
    bg = f'<rect width="{s}" height="{s}" rx="{s*0.225}" fill="{tile}"/>' if tile else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}" width="{size}" height="{size}">'
            f'{bg}<g transform="translate({ox:.3f} {oy:.3f})">{m}</g></svg>')

if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    jobs = []
    for th in THEMES:
        jobs += [(f"hypedrive-lockup-{th}.svg", lockup(th), 600),
                 (f"hypedrive-mark-{th}.svg", icon(th), 512)]
    jobs += [("hypedrive-app-icon-light.svg", icon("light", 1024, 0.2, "#ffffff"), 1024),
             ("hypedrive-app-icon-dark.svg", icon("dark", 1024, 0.2, "#141414"), 1024)]
    for name, svg, h in jobs:
        p = os.path.join(out, name); open(p, "w").write(svg)
        subprocess.run(["rsvg-convert", "-h", str(h), p, "-o", p[:-4] + ".png"], check=True)
    fav = os.path.join(out, "favicon"); os.makedirs(fav, exist_ok=True)
    src = os.path.join(out, "hypedrive-mark-light.svg")
    open(os.path.join(fav, "favicon.svg"), "w").write(icon("light", 32, 0.04))
    for s in (16, 32, 48, 180, 192, 512):
        open(os.path.join(fav, f"_tmp{s}.svg"), "w").write(icon("light", s, 0.04 if s <= 48 else 0.1))
        subprocess.run(["rsvg-convert", "-w", str(s), "-h", str(s), os.path.join(fav, f"_tmp{s}.svg"), "-o", os.path.join(fav, f"favicon-{s}.png")], check=True)
        os.remove(os.path.join(fav, f"_tmp{s}.svg"))
    subprocess.run(["magick", *[os.path.join(fav, f"favicon-{s}.png") for s in (16, 32, 48)], os.path.join(fav, "favicon.ico")], check=True)
