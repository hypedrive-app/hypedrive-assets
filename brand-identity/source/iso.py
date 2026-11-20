"""Isometric Hypedrive marks — true 30° iso, one hue per box, three tones per box
(top = light, left = mid, right = deep), PostHog palette."""
import sys, os, math, subprocess
sys.path.insert(0, "/tmp/hdwm")
import refined as R

C30, S30 = math.cos(math.radians(30)), 0.5
BLUE = ("#4d8bff", "#1f5fff", "#0a3fc4")
ORNG = ("#ff7a3d", "#f24a0c", "#b83300")
YELL = ("#ffdf5e", "#ffbb12", "#e88f00")
INK_L = ("#3b3b3d", "#1d1d1f", "#0c0c0d")      # black box, light theme
INK_D = ("#ffffff", "#e4e4e7", "#c4c4c9")      # same box on the dark theme
SEAM = 0.35                                    # same-colour stroke closes AA seams

def P(x, y, z): return (x*C30 - y*C30, (x + y)*S30 - z)

class Scene:
    def __init__(self): self.items = []          # (depth, svg)
    def poly(self, pts3, fill, depth, sw=SEAM):
        pts = " ".join(f"{a:.3f},{b:.3f}" for a, b in (P(*p) for p in pts3))
        self.items.append((depth, f'<polygon points="{pts}" fill="{fill}" stroke="{fill}" stroke-width="{sw}" stroke-linejoin="round"/>'))
    def raw(self, depth, svg): self.items.append((depth, svg))
    def box(self, x, y, z, w, d, h, tones, depth=None):
        t, l, r = tones; dep = depth if depth is not None else x + y + z
        self.poly([(x, y+d, z), (x+w, y+d, z), (x+w, y+d, z+h), (x, y+d, z+h)], l, dep)          # front-left
        self.poly([(x+w, y, z), (x+w, y+d, z), (x+w, y+d, z+h), (x+w, y, z+h)], r, dep + 0.001)  # front-right
        self.poly([(x, y, z+h), (x+w, y, z+h), (x+w, y+d, z+h), (x, y+d, z+h)], t, dep + 0.002)  # top
    def render(self, H=28):
        """Fit to height H; return (svg, width)."""
        import re
        xs, ys = [], []
        for _, s in self.items:
            for a, b in re.findall(r"(-?[\d.]+),(-?[\d.]+)", s):
                xs.append(float(a)); ys.append(float(b))
            for cx, cy in re.findall(r'data-pt="(-?[\d.]+) (-?[\d.]+)"', s):
                xs.append(float(cx)); ys.append(float(cy))
        x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
        k = H / (y1 - y0)
        body = "".join(s for _, s in sorted(self.items, key=lambda i: i[0]))
        return f'<g transform="translate({-x0*k:.3f} {-y0*k:.3f}) scale({k:.4f})">{body}</g>', (x1 - x0) * k

def dot(s, pt3, r, fill, depth):
    x, y = P(*pt3)
    s.raw(depth, f'<ellipse cx="{x:.3f}" cy="{y:.3f}" rx="{r:.3f}" ry="{r:.3f}" fill="{fill}"/>')

def face_dot_right(s, x, y, z, r, fill, depth):
    """Circle lying on a +x facing plane (ellipse sheared to the iso face)."""
    cx, cy = P(x, y, z)
    s.raw(depth, f'<g transform="translate({cx:.3f} {cy:.3f}) matrix({C30:.4f} {-S30} 0 1 0 0)"><circle r="{r}" fill="{fill}"/></g>')

def face_dot_left(s, x, y, z, r, fill, depth):
    cx, cy = P(x, y, z)
    s.raw(depth, f'<g transform="translate({cx:.3f} {cy:.3f}) matrix({C30:.4f} {S30} 0 1 0 0)"><circle r="{r}" fill="{fill}"/></g>')

def inks(dark): return INK_D if dark else INK_L
def eye(dark): return "#141414" if dark else "#ffffff"

# ---------------------------------------------------------------- marks
def i_parcel(dark):
    """Single orange parcel, ink tape over the lid and down the front, label dot."""
    s = Scene(); k = inks(dark)
    s.box(0, 0, 0, 10, 10, 8, ORNG)
    tw = 1.7; m = 5
    s.poly([(0, m-tw/2, 8), (10, m-tw/2, 8), (10, m+tw/2, 8), (0, m+tw/2, 8)], k[0], 1)   # tape on lid, along x
    s.poly([(10, m-tw/2, 8), (10, m+tw/2, 8), (10, m+tw/2, 4.2), (10, m-tw/2, 4.2)], k[2], 1)  # down the right face
    s.poly([(1.4, 10, 1.4), (5.6, 10, 1.4), (5.6, 10, 5.0), (1.4, 10, 5.0)], BLUE[1], 2, sw=0.7)
    s.poly([(1.4, 10, 4.0), (5.6, 10, 4.0), (5.6, 10, 5.0), (1.4, 10, 5.0)], YELL[1], 3, sw=0.7)
    return s.render()

def i_stack(dark):
    """Pyramid of parcels — blue, orange, yellow, ink on top."""
    s = Scene(); k = inks(dark)
    s.box(0, 6, 0, 6, 6, 6, BLUE)
    s.box(6.6, 0, 0, 6, 6, 6, ORNG, depth=6.0)
    s.box(0, 0, 0, 6, 6, 6, YELL, depth=-1)       # hidden back box gives the pile its depth
    s.box(1.6, 1.6, 6.6, 6, 6, 5.4, YELL, depth=20)
    s.box(3.3, 3.3, 12.6, 2.6, 2.6, 2.6, k, depth=30)
    return s.render()

def i_unbox(dark):
    """Open ink box with three iso bars rising out of it — hype out of the package."""
    s = Scene(); k = inks(dark)
    W, D, Hh = 12, 12, 6.5
    # inside walls (seen from the inside) + floor
    s.poly([(0, 0, 0), (W, 0, 0), (W, D, 0), (0, D, 0)], k[2], -10)
    s.poly([(0, 0, 0), (0, D, 0), (0, D, Hh), (0, 0, Hh)], k[2], -9)       # back-left wall, inner
    s.poly([(0, 0, 0), (W, 0, 0), (W, 0, Hh), (0, 0, Hh)], k[1], -9)       # back-right wall, inner
    # bars (depth between back walls and front walls)
    for i, (pal, h) in enumerate([(BLUE, 9), (ORNG, 14), (YELL, 19)]):
        b = 3.0; x = 1.5 + i*3.4; y = 7.5 - i*3.4
        s.box(x, y, 0, b, b, h, pal, depth=-5 + i*0.1 - (y)*0.01)
    # front walls drawn last
    s.poly([(0, D, 0), (W, D, 0), (W, D, Hh), (0, D, Hh)], k[1], 50)
    s.poly([(W, 0, 0), (W, D, 0), (W, D, Hh), (W, 0, Hh)], k[2], 50.1)
    # rim
    face_dot_left(s, 3.2, D, 2.9, 1.0, eye(dark), 51)
    return s.render()

def i_label(dark):
    """Parcel with an ink shipping label + hole on the right face (tag)."""
    s = Scene(); k = inks(dark)
    s.box(0, 0, 0, 10, 10, 8.4, BLUE)
    # label polygon on the +x face: a tag shape in (y, z)
    yz = [(1.4, 1.6), (6.2, 1.6), (8.8, 4.0), (6.2, 6.4), (1.4, 6.4)]
    s.poly([(10, y, z) for y, z in yz], ORNG[1], 5, sw=0.9)
    face_dot_right(s, 10, 6.4, 4.0, 1.3, k[1], 6)
    # yellow lid band
    s.poly([(0, 0, 8.4), (10, 0, 8.4), (10, 10, 8.4), (0, 10, 8.4)], BLUE[0], 1)
    tw = 1.6
    s.poly([(5-tw/2, 0, 8.4), (5+tw/2, 0, 8.4), (5+tw/2, 10, 8.4), (5-tw/2, 10, 8.4)], YELL[0], 2)
    s.poly([(5-tw/2, 10, 8.4), (5+tw/2, 10, 8.4), (5+tw/2, 10, 4.6), (5-tw/2, 10, 4.6)], YELL[1], 2)
    return s.render()

def i_express(dark):
    """Ink parcel racing forward with three coloured speed trails on the iso x axis."""
    s = Scene(); k = inks(dark)
    s.box(10, 0, 0, 9, 9, 8, k, depth=10)
    tw = 1.5
    s.poly([(10, 4.5-tw/2, 8), (19, 4.5-tw/2, 8), (19, 4.5+tw/2, 8), (10, 4.5+tw/2, 8)], ORNG[0], 20)
    s.poly([(19, 4.5-tw/2, 8), (19, 4.5+tw/2, 8), (19, 4.5+tw/2, 4.4), (19, 4.5-tw/2, 4.4)], ORNG[1], 20)
    for pal, z, y, x0 in [(BLUE, 6.2, 4.5, 2.6), (ORNG, 3.8, 6.5, -1.0), (YELL, 1.4, 4.5, 3.8)]:
        a, b = P(x0, y, z), P(13.0, y, z)   # trails run under the box: drawn first, hidden by it
        s.raw(5, f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" stroke="{pal[1]}" stroke-width="2.3" stroke-linecap="round"/><!--{a[0]-1.2:.3f},{a[1]-1.2:.3f} {a[0]+1.2:.3f},{a[1]+1.2:.3f} {b[0]-1.2:.3f},{b[1]-1.2:.3f} {b[0]+1.2:.3f},{b[1]+1.2:.3f}-->')
    return s.render()

def i_h(dark):
    """Iso H monogram from three blocks + ink cap."""
    s = Scene(); k = inks(dark)
    s.box(0, 0, 0, 3.6, 3.6, 13, BLUE, depth=0)
    s.box(3.6, 0, 4.7, 5.2, 3.6, 3.6, YELL, depth=1)
    s.box(8.8, 0, 0, 3.6, 3.6, 13, ORNG, depth=2)
    s.box(8.8, 0, 13.6, 3.6, 3.6, 1.8, k, depth=3)
    return s.render()

MARKS = dict(parcel=i_parcel, stack=i_stack, unbox=i_unbox, label=i_label, express=i_express, monogram=i_h)

def lockup(mark, dark, font="jakarta", text="Hypedrive", soft=0.55, gap=9.5):
    ink = "#fff" if dark else "#141414"
    m, mw = MARKS[mark](dark)
    name, w = R.FONTS[font]
    d, tw = R.text_path(text, w, 18.6, -0.008, name)
    ox = mw + gap; W = ox + tw + 1
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 {W+2:.2f} 30" width="{(W+2)*10:.0f}" height="300">'
            f'{m}<path fill="{ink}" stroke="{ink}" stroke-width="{soft}" stroke-linejoin="round" transform="translate({ox:.2f} 22.9)" d="{d}"/></svg>')

def mark_only(mark, dark, size=512):
    m, mw = MARKS[mark](dark)
    side = max(mw, 28) + 4
    ox = (side - mw) / 2; oy = (side - 28) / 2
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {side:.2f} {side:.2f}" width="{size}" height="{size}"><g transform="translate({ox:.2f} {oy:.2f})">{m}</g></svg>'

if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for i, mk in enumerate(MARKS, 1):
        for theme, dark in [("light", False), ("dark", True)]:
            base = os.path.join(out, f"hypedrive-iso{i}-{mk}")
            for suffix, svg in [(f"-{theme}", lockup(mk, dark)), (f"-mark-{theme}", mark_only(mk, dark))]:
                p = base + suffix + ".svg"; open(p, "w").write(svg)
                subprocess.run(["rsvg-convert", "-h", "600" if "mark" not in suffix else "512", p, "-o", p[:-4] + ".png"], check=True)
