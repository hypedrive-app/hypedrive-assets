"""Hypedrive concepts informed by Mobbin research (letter-in-mark, glyph-swap wordmark, one-colour splash)."""
import sys, os, re, math, subprocess
sys.path.insert(0, "/tmp/hdwm")
import isofam as F
from isofam import Ctx, box, tape, P, C30, S30, SIGNATURE, HUE, INK, SOLID, rpoly
import optical as OPT
import palette as PL

AX = {"opsz": 96, "wdth": 100}
WG, CAP, SP = 700, 18.6, dict(strength=0.75, extra=0.012)

def face_left(D):
    """Affine for drawing in (u along x, v up) on the front-left face y = D."""
    return f"matrix({C30:.5f} {S30} 0 -1 {-C30*D:.4f} {S30*D:.4f})"

# ---------------------------------------------------------------- A: H-box
def a_hbox(c):
    o = box(c, 0, 0, 0, 10, 10, 10, SIGNATURE, tape(c, 0, 0, 0, 10, 10, 10))
    cut = SOLID[c.theme]["dot"]
    H = (rpoly([(2.1, 2.0), (3.95, 2.0), (3.95, 8.0), (2.1, 8.0)], 0.45) +
         rpoly([(6.05, 2.0), (7.9, 2.0), (7.9, 8.0), (6.05, 8.0)], 0.45) +
         rpoly([(3.6, 4.25), (6.4, 4.25), (6.4, 5.75), (3.6, 5.75)], 0.01))
    return o + f'<path transform="{face_left(10)}" fill="{cut}" d="{H}"/>'

# ---------------------------------------------------------------- C: speed H (flat)
def c_speedh(c):
    ink = SOLID[c.theme]["ink"]; o = []
    lean = 3.4; w = 6.0
    def pillar(x0, pair):
        gid = c.id("g")
        c.defs.append(f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="28" gradientUnits="userSpaceOnUse"><stop stop-color="{pair[0]}"/><stop offset="1" stop-color="{pair[1]}"/></linearGradient>')
        return f'<path fill="url(#{gid})" d="{rpoly([(x0,28),(x0+lean,0),(x0+lean+w,0),(x0+w,28)], 2.2)}"/>'
    xl, xr = 9.0, 22.0
    gid = c.id("g")
    c.defs.append(f'<linearGradient id="{gid}" x1="0" y1="0" x2="40" y2="0" gradientUnits="userSpaceOnUse"><stop stop-color="{PL.YELL[1][0]}"/><stop offset="1" stop-color="{PL.YELL[1][1]}"/></linearGradient>')
    bar = rpoly([(xl+2, 16.4), (xr+3.0, 16.4), (xr+3.6, 11.6), (xl+2.6, 11.6)], 0.01)
    o.append(f'<path fill="url(#{gid})" d="{bar}"/>')
    o.append(pillar(xl, PL.BLUE[1])); o.append(pillar(xr, PL.ORNG[1]))
    for y, x0, x1 in [(9.0, 1.8, 7.6), (14.0, 0, 6.9), (19.0, 2.4, 6.2)]:
        o.append(f'<path d="M{x0+1.2} {y}H{x1}" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>')
    c.pts += [(0, 0), (xr+lean+w, 28)]
    return "".join(o)

# ---------------------------------------------------------------- E: H-bag (flat)
def e_hbag(c):
    ink = SOLID[c.theme]["ink"]; cut = SOLID[c.theme]["dot"]; o = []
    o.append(f'<path d="M8.6 9V6.4a4.9 4.9 0 0 1 9.8 0V9" fill="none" stroke="{ink}" stroke-width="2.9" stroke-linecap="round"/>')
    body = rpoly([(1.2, 8.2), (25.8, 8.2), (27, 28), (0, 28)], [2, 2, 3, 3])
    cid = c.id("c"); c.defs.append(f'<clipPath id="{cid}"><path d="{body}"/></clipPath>')
    def g(pair, y0, y1):
        gid = c.id("g"); c.defs.append(f'<linearGradient id="{gid}" x1="0" y1="{y0}" x2="0" y2="{y1}" gradientUnits="userSpaceOnUse"><stop stop-color="{pair[0]}"/><stop offset="1" stop-color="{pair[1]}"/></linearGradient>'); return f"url(#{gid})"
    o.append(f'<g clip-path="url(#{cid})"><rect x="-1" y="0" width="14.5" height="30" fill="{g(PL.BLUE[1], 8, 28)}"/>'
             f'<rect x="13.5" y="0" width="15" height="30" fill="{g(PL.ORNG[1], 8, 28)}"/>'
             f'<rect x="-1" y="0" width="30" height="12.2" fill="{g(F.SIGNATURE[0], 8, 12)}"/></g>')
    H = (rpoly([(7.6, 15), (10.7, 15), (10.7, 25), (7.6, 25)], 0.8) + rpoly([(16.3, 15), (19.4, 15), (19.4, 25), (16.3, 25)], 0.8)
         + rpoly([(10.2, 18.8), (16.8, 18.8), (16.8, 21.2), (10.2, 21.2)], 0.01))
    o.append(f'<path fill="{cut}" d="{H}"/>')
    c.pts += [(0, 0), (27, 28)]
    return "".join(o)

# ---------------------------------------------------------------- shared output helpers
def mark_svg(fn, theme, H=28):
    c = Ctx(theme); body = fn(c)
    xs = [p[0] for p in c.pts]; ys = [p[1] for p in c.pts]
    x0, y0, x1, y1 = min(xs), min(ys), max(xs), max(ys); k = H/(y1-y0)
    return f'<defs>{"".join(c.defs)}</defs><g transform="scale({k:.5f}) translate({-x0:.3f} {-y0:.3f})">{body}</g>', (x1-x0)*k

def lockup(fn, theme, text="Hypedrive"):
    ink = SOLID[theme]["ink"]; m, mw = mark_svg(fn, theme)
    d, tw, _ = OPT.optical_text_path(text, WG, CAP, "Bricolage", AX, **SP)
    ox = mw + 8.0; W = ox + tw + 0.3
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 {W+2:.2f} 30" width="{(W+2)*10:.0f}" height="300">{m}'
            f'<path fill="{ink}" stroke="{ink}" stroke-width="0.3" stroke-linejoin="round" transform="translate({ox:.2f} 22.9)" d="{d}"/></svg>')

# ---------------------------------------------------------------- B: the i's dot is the parcel
def b_wordmark(theme, text="Hypedrive"):
    ink = SOLID[theme]["ink"]
    t2 = text.replace("i", "ı")
    d, tw, _, pos = OPT.optical_text_path(t2, WG, CAP, "Bricolage", AX, positions=True, **SP)
    k = CAP / 660
    gx = [x for n, x, a in pos if n == "dotlessi"][0]
    icx = gx + (39 + 183) / 2 * k                       # dotless-i stem centre
    bh = 7.8                                            # parcel height
    m, mw = mark_svg(F.f_box, theme, bh)
    top = 22.9 - 525*k - 1.25 - bh                      # sits 1.25 above the x-height
    W = tw + 0.3; y0 = min(-1, top - 0.8)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 {y0:.2f} {W+2:.2f} {29-y0:.2f}" width="{(W+2)*10:.0f}" height="{(29-y0)*10:.0f}">'
            f'<path fill="{ink}" stroke="{ink}" stroke-width="0.3" stroke-linejoin="round" transform="translate(0 22.9)" d="{d}"/>'
            f'<g transform="translate({icx - mw/2:.3f} {top:.3f})">{m}</g></svg>')

def square(fn, theme, size=512, pad=0.12, tile=None):
    s = 100.0; inner = s*(1-2*pad)
    _, w28 = mark_svg(fn, theme, 28); r = w28/28
    H = inner if r <= 1 else inner/r
    m, mw = mark_svg(fn, theme, H)
    bg = f'<rect width="{s}" height="{s}" rx="{s*0.225}" fill="{tile}"/>' if tile else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}" width="{size}" height="{size}">{bg}<g transform="translate({(s-mw)/2:.3f} {(s-H)/2:.3f})">{m}</g></svg>'

def mono(svg, bg, fg="#ffffff"):
    """One-colour version for a coloured background: each colour becomes fg mixed into bg by its lightness,
    so iso faces keep their light/mid/dark read; the cut-outs become the background."""
    def lum(h):
        r, g, b = (int(h[i:i+2], 16)/255 for i in (1, 3, 5)); return 0.2126*r + 0.7152*g + 0.0722*b
    br = [int(bg[i:i+2], 16) for i in (1, 3, 5)]; fr = [int(fg[i:i+2], 16) for i in (1, 3, 5)]
    def rep(m):
        h = m.group(0).lower()
        if h == PL.INK_TEXT_L.lower(): t = 0.0                # dark-theme cut-outs (dot, H) knock out
        elif h == "#ffffff": t = 1.0                          # wordmark + white parts stay full
        else: t = 0.62 + 0.38*min(1, lum(h)/0.85)
        return "#" + "".join(f"{round(b + (f-b)*t):02x}" for b, f in zip(br, fr))
    return re.sub(r"#[0-9a-fA-F]{6}\b", rep, svg)

def splash(inner_svg, bg, w=300, h=640):
    body = re.sub(r"^<svg[^>]*>|</svg>$", "", inner_svg)
    vb = re.search(r'viewBox="([^"]+)"', inner_svg).group(1).split()
    vx, vy, vw, vh = map(float, vb); target_w = w*0.62; k = target_w/vw
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<rect width="{w}" height="{h}" rx="42" fill="{bg}"/>'
            f'<g transform="translate({(w-target_w)/2:.2f} {(h-vh*k)/2:.2f}) scale({k:.4f}) translate({-vx} {-vy})">{body}</g></svg>')

CONCEPTS = [("A-hbox", a_hbox), ("C-speedh", c_speedh), ("E-hbag", e_hbag)]
COBALT = PL.BLUE[1][1]

if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    def save(name, svg, h):
        p = os.path.join(out, name + ".svg"); open(p, "w").write(svg)
        subprocess.run(["rsvg-convert", "-h", str(h), p, "-o", p[:-4] + ".png"], check=True)
    for name, fn in CONCEPTS:
        for th in ("light", "dark"):
            save(f"hypedrive-{name}-lockup-{th}", lockup(fn, th), 600)
            save(f"hypedrive-{name}-mark-{th}", square(fn, th), 512)
        save(f"hypedrive-{name}-app-icon", square(fn, "dark", 1024, 0.2, "#141414"), 1024)
        save(f"hypedrive-{name}-splash-mono", splash(mono(lockup(fn, "dark"), COBALT), COBALT), 1280)
        save(f"hypedrive-{name}-splash-color", splash(lockup(fn, "dark"), "#121417"), 1280)
    for text, tag in (("Hypedrive", "title"), ("hypedrive", "lower")):
        for th in ("light", "dark"):
            save(f"hypedrive-B-ibox-{tag}-{th}", b_wordmark(th, text), 600)
        save(f"hypedrive-B-ibox-{tag}-splash-mono", splash(mono(b_wordmark("dark", text), COBALT), COBALT), 1280)
        save(f"hypedrive-B-ibox-{tag}-splash-color", splash(b_wordmark("dark", text), "#121417"), 1280)
