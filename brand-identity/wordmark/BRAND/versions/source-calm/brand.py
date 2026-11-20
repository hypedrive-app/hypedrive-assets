"""Hypedrive brand identity: guidelines book (HTML → PDF), application assets, design tokens."""
import sys, os, re, math, json, base64, subprocess
sys.path.insert(0, "/tmp/hdwm")
import final as FN
import isofam as F
import palette as PL
from palette import oklch_to_hex
import optical as OPT
from text2path import text_path

OUT = sys.argv[1]
A = os.path.join(OUT, "assets"); TK = os.path.join(OUT, "tokens")
for d in (OUT, A, TK, os.path.join(A, "illustrations"), os.path.join(A, "social"), os.path.join(A, "print"), os.path.join(A, "patterns"), os.path.join(A, "screens")):
    os.makedirs(d, exist_ok=True)

def save(path, svg, png_w=None):
    open(path, "w").write(svg)
    if png_w: subprocess.run(["rsvg-convert", "-w", str(png_w), path, "-o", path[:-4] + ".png"], check=True)
    return svg

def uri(svg): return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()
def inner(svg): return re.sub(r"^<svg[^>]*>|</svg>$", "", svg)
def vb(svg): return [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
_NS = [0]
def namespaced(body):
    """Give every id inside an embedded svg a unique prefix so composed files never collide."""
    _NS[0] += 1; p = f"n{_NS[0]}-"
    ids = set(re.findall(r'\bid="([^"]+)"', body))
    for i in sorted(ids, key=len, reverse=True):
        body = re.sub(rf'\bid="{re.escape(i)}"', f'id="{p}{i}"', body)
        body = re.sub(rf'url\(#{re.escape(i)}\)', f'url(#{p}{i})', body)
        body = re.sub(rf'href="#{re.escape(i)}"', f'href="#{p}{i}"', body)
    return body
def place(svg, x, y, w=None, h=None):
    """Embed an svg string at x,y scaled to width w (or height h)."""
    vx, vy, vw, vh = vb(svg); k = (w / vw) if w else (h / vh)
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({k:.5f}) translate({-vx} {-vy})">{namespaced(inner(svg))}</g>', vw*k, vh*k

def outlined(text, size, wght=700, opsz=96, fill="#fff", x=0, y=0, track=0.0, font="Bricolage"):
    """Text as outlines (Bricolage) at cap-height `size`; y is the baseline."""
    axes = {"opsz": opsz, "wdth": 100} if font == "Bricolage" else {}
    d, w = text_path(text, wght, size, track, font, axes)
    return f'<path fill="{fill}" transform="translate({x:.2f} {y:.2f})" d="{d}"/>', w

# ============================================================== colour system
def scale(peakL, cmax, h, shift, dark_span=0.5):
    steps = [(50, .975), (100, .948), (200, .895), (300, .82), (400, .735), (500, .655), (600, .575), (700, .495), (800, .415), (900, .335), (950, .265)]
    out = {}
    for s, L in steps:
        t = abs(L - peakL) / (0.55 if L > peakL else dark_span)
        c = cmax * max(0.06, 1 - t**1.6)
        out[s] = oklch_to_hex(L, c, h + shift*(peakL - L))
    return out
SCALES = {
    "cobalt":    scale(.60, .23, 262, 18),
    "vermilion": scale(.68, .21, 40, -10, 0.62),
    "marigold":  scale(.86, .18, 86, -46, 0.78),
    "ink":       {s: oklch_to_hex(L, .006 + .004*(1-L), 272) for s, L in
                  [(50, .985), (100, .962), (200, .92), (300, .855), (400, .70), (500, .52), (600, .445), (700, .36), (800, .28), (900, .21), (950, .165)]},
    "mint":      scale(.72, .16, 160, 14),
}
ANCHORS = {"cobalt": (600, F.SIGNATURE[1][1]), "vermilion": (500, F.SIGNATURE[2][0]), "marigold": (300, F.SIGNATURE[0][1]), "ink": (900, PL.INK_TEXT_L)}
for _n, (_step, _hex) in ANCHORS.items(): SCALES[_n][_step] = _hex          # brand colours ARE scale steps
BRAND = {"cobalt": SCALES["cobalt"][600], "vermilion": SCALES["vermilion"][500], "marigold": SCALES["marigold"][300], "ink": SCALES["ink"][900], "paper": "#ffffff"}
C, V, M, I, N = SCALES["cobalt"], SCALES["vermilion"], SCALES["marigold"], SCALES["ink"], SCALES["mint"]
SEM_L = {"bg": "#ffffff", "bg-subtle": I[50], "canvas": I[100], "surface": "#ffffff", "surface-raised": "#ffffff", "surface-sunken": I[50], "overlay": "#ffffff",
         "fg": I[900], "fg-muted": I[600], "fg-subtle": I[500], "border": I[200], "border-strong": I[300],
         "accent": C[600], "accent-hover": C[700], "accent-pressed": C[800], "accent-subtle": C[50], "accent-fg": "#ffffff", "focus": C[600],
         "success": N[700], "success-subtle": N[50], "warning": M[700], "warning-subtle": M[50],
         "danger": V[700], "danger-subtle": V[50], "info": C[600], "info-subtle": C[50], "link": C[600],
         "info-strong": C[800], "warning-strong": M[800], "success-strong": N[800], "danger-strong": V[800],
         "control": I[200], "control-hover": I[300], "control-pressed": I[300], "control-edge": I[300],
         "track": I[200], "track-strong": I[500], "skeleton": I[100], "skeleton-hi": I[50],
         "inverse": I[900], "inverse-fg": "#ffffff", "inverse-link": C[300], "focus-ring": C[100],
         "danger-solid": V[600], "danger-solid-hover": V[700], "danger-edge": V[800], "success-solid": N[500], "star": M[300], "data-1": C[500], "data-hl": V[500],
         "indicator": C[600], "border-input": I[400], "border-input-hover": I[500], "tone-cobalt": C[600], "tone-vermilion": V[600], "tone-marigold": M[600], "tone-mint": N[600], "tone-ink": I[500]}
SEM_D = {"bg": I[950], "bg-subtle": I[900], "canvas": I[950], "surface": I[900], "surface-raised": I[800], "surface-sunken": I[950], "overlay": I[800],
         "fg": I[50], "fg-muted": I[300], "fg-subtle": I[400], "border": I[800], "border-strong": I[700],
         "accent": C[600], "accent-hover": C[700], "accent-pressed": C[800], "accent-subtle": C[950], "accent-fg": "#ffffff", "focus": C[400],
         "success": N[400], "success-subtle": N[950], "warning": M[300], "warning-subtle": M[950],
         "danger": V[400], "danger-subtle": V[950], "info": C[400], "info-subtle": C[950], "link": C[300],
         "info-strong": C[200], "warning-strong": M[200], "success-strong": N[200], "danger-strong": V[200],
         "control": I[700], "control-hover": I[600], "control-pressed": I[800], "control-edge": I[600],
         "track": I[700], "track-strong": I[400], "skeleton": I[800], "skeleton-hi": I[700],
         "inverse": I[50], "inverse-fg": I[900], "inverse-link": C[600], "focus-ring": C[900],
         "danger-solid": V[600], "danger-solid-hover": V[700], "danger-edge": V[800], "success-solid": N[500], "star": M[300], "data-1": C[400], "data-hl": V[400],
         "indicator": C[400], "border-input": I[600], "border-input-hover": I[500], "tone-cobalt": C[400], "tone-vermilion": V[400], "tone-marigold": M[300], "tone-mint": N[400], "tone-ink": I[400]}
# deepened -subtle tints = the values the UI ships (xlead.py): tint colour mixed in OKLab into white (light) or #16181d (dark)
def _lin(v):
    v /= 255; return v/12.92 if v <= 0.04045 else ((v+0.055)/1.055)**2.4
def _tolab(h):
    r, g, b = (_lin(int(h[i:i+2], 16)) for i in (1, 3, 5))
    l = (0.4122214708*r + 0.5363325363*g + 0.0514459929*b) ** (1/3); m = (0.2119034982*r + 0.6806995451*g + 0.1073969566*b) ** (1/3); s = (0.0883024619*r + 0.2817188376*g + 0.6299787005*b) ** (1/3)
    return (0.2104542553*l + 0.7936177850*m - 0.0040720468*s, 1.9779984951*l - 2.4285922050*m + 0.4505937099*s, 0.0259040371*l + 0.7827717662*m - 0.8086757660*s)
def _fromlab(L, a, b):
    l = (L + 0.3963377774*a + 0.2158037573*b) ** 3; m = (L - 0.1055613458*a - 0.0638541728*b) ** 3; s = (L - 0.0894841775*a - 1.2914855480*b) ** 3
    rgb_ = (4.0767416621*l - 3.3077115913*m + 0.2309699292*s, -1.2684380046*l + 2.6097574011*m - 0.3413193965*s, -0.0041960863*l - 0.7034186147*m + 1.7076147010*s)
    return "#" + "".join(f"{max(0, min(255, round(255*(12.92*c if c <= 0.0031308 else 1.055*max(c, 0)**(1/2.4) - 0.055)))):02x}" for c in rgb_)
def mix(tint, pct, base):
    A, B = _tolab(tint), _tolab(base); k = pct / 100
    return _fromlab(*(B[i] + (A[i] - B[i]) * k for i in range(3)))
TINT_L = {"accent": ("#2d58ee", 18), "info": ("#2d58ee", 18), "success": ("#0a8a5c", 22), "warning": ("#ffc83c", 48), "danger": ("#e04f10", 19)}
TINT_D = {"accent": ("#2d58ee", 30), "info": ("#2d58ee", 30), "success": ("#0a8a5c", 32), "warning": ("#ffc83c", 22), "danger": ("#e04f10", 28)}
for _k, (_h, _p) in TINT_L.items(): SEM_L[f"{_k}-subtle"] = mix(_h, _p, "#ffffff")
for _k, (_h, _p) in TINT_D.items(): SEM_D[f"{_k}-subtle"] = mix(_h, _p, "#16181d")
SEMANTIC = SEM_L

def lum(h):
    if len(h) == 4: h = '#' + ''.join(c*2 for c in h[1:])
    def ch(v):
        v /= 255; return v/12.92 if v <= 0.04045 else ((v+0.055)/1.055)**2.4
    r, g, b = (int(h[i:i+2], 16) for i in (1, 3, 5)); return 0.2126*ch(r) + 0.7152*ch(g) + 0.0722*ch(b)
def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + 0.05) / (lb + 0.05)
def check_semantic():
    bad = []
    for name, S in (("light", SEM_L), ("dark", SEM_D)):
        for fg, bg, need in [("fg", "bg", 4.5), ("fg-muted", "bg", 4.5), ("fg-subtle", "bg", 4.5), ("fg-subtle", "bg-subtle", 4.5), ("fg-subtle", "surface-raised", 4.5), ("fg-muted", "surface-raised", 4.5), ("fg", "surface-raised", 4.5),
                             ("link", "bg", 4.5), ("accent", "bg", 3), ("accent-fg", "accent", 4.5), ("accent-fg", "accent-hover", 4.5), ("accent-fg", "accent-pressed", 4.5), ("focus", "bg", 3),
                             ("success", "bg", 4.5), ("warning", "bg", 4.5), ("danger", "bg", 4.5), ("info", "bg", 4.5),
                             ("info-strong", "accent-subtle", 4.5),
                             ("info-strong", "info-subtle", 4.5), ("warning-strong", "warning-subtle", 4.5), ("success-strong", "success-subtle", 4.5), ("danger-strong", "danger-subtle", 4.5),
                             ("fg", "control", 4.5), ("fg", "control-pressed", 4.5), ("fg", "control-hover", 4.5), ("inverse-fg", "inverse", 4.5), ("inverse-link", "inverse", 4.5),
                             ("accent-fg", "danger-solid", 4.5), ("accent-fg", "danger-solid-hover", 4.5), ("track-strong", "bg", 3), ("track-strong", "surface-raised", 3), ("indicator", "bg", 3), ("indicator", "canvas", 3), ("indicator", "surface-raised", 3), ("border-input", "surface", 1.5), ("tone-vermilion", "bg", 3), ("tone-mint", "bg", 3), ("tone-marigold", "bg", 3)]:
            r = contrast(S[fg], S[bg])
            if r < need: bad.append(f"{name}: {fg} on {bg} = {r:.2f} (< {need})")
    return bad
def rgb(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))

# ============================================================== tokens
css = [":root {"]
for n, sc in SCALES.items():
    for s, h in sc.items(): css.append(f"  --hd-{n}-{s}: {h};")
for n, h in BRAND.items(): css.append(f"  --hd-brand-{n}: {h};")
for n, h in SEM_L.items(): css.append(f"  --hd-{n}: {h};")
css += ["  --hd-font-display: 'Bricolage Grotesque', ui-sans-serif, system-ui, sans-serif;",
        "  --hd-font-ui: 'Geist', ui-sans-serif, system-ui, sans-serif;",
        "  --hd-font-body: 'Geist', ui-sans-serif, system-ui, sans-serif;",
        "  --hd-font-mono: 'Geist Mono', ui-monospace, SFMono-Regular, monospace;",
        "  --hd-ease-arrive: cubic-bezier(.2, .9, .25, 1.15);", "  --hd-ease-standard: cubic-bezier(.2, .8, .2, 1);",
        "  --hd-dur-quick: 120ms;", "  --hd-dur-base: 200ms;", "  --hd-dur-arrive: 320ms;"]
SPACE = [4, 8, 12, 16, 24, 32, 48, 64]
RADII = {"xs": 6, "sm": 8, "md": 12, "lg": 16, "xl": 24, "full": 999}
SHADOWS = {"e1": "0 0 0 1px rgba(16,20,38,.09), 0 1px 1px rgba(16,20,38,.04), 0 2px 4px -1px rgba(16,20,38,.04)",
           "e2": "0 0 0 1px rgba(16,20,38,.08), 0 2px 4px -1px rgba(16,20,38,.05), 0 8px 16px -4px rgba(16,20,38,.08)",
           "e3": "0 0 0 1px rgba(16,20,38,.08), 0 4px 8px -2px rgba(16,20,38,.06), 0 16px 32px -8px rgba(16,20,38,.12), 0 32px 64px -16px rgba(16,20,38,.10)"}   # layered: ring + contact + ambient
SHADOWS_D = {"e1": "0 0 0 1px rgba(255,255,255,.07), 0 1px 2px rgba(0,0,0,.40), inset 0 1px 0 rgba(255,255,255,.04)",
             "e2": "0 0 0 1px rgba(255,255,255,.05), 0 4px 8px -2px rgba(0,0,0,.45), 0 12px 24px -6px rgba(0,0,0,.40), inset 0 1px 0 rgba(255,255,255,.05)",
             "e3": "0 0 0 1px rgba(255,255,255,.06), 0 8px 16px -4px rgba(0,0,0,.50), 0 24px 48px -12px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.06)"}
css += [f"  --hd-space-{i+1}: {v}px;" for i, v in enumerate(SPACE)] + [f"  --hd-radius-{k}: {v}px;" for k, v in RADII.items()] + [f"  --hd-shadow-{k}: {v};" for k, v in SHADOWS.items()] + ["}"]
css += ["", '[data-theme="light"] {'] + [f"  --hd-{n}: {h};" for n, h in SEM_L.items()] + [f"  --hd-shadow-{k}: {v};" for k, v in SHADOWS.items()] + ["}", "", '[data-theme="dark"] {'] + [f"  --hd-{n}: {h};" for n, h in SEM_D.items()] + [f"  --hd-shadow-{k}: {v};" for k, v in SHADOWS_D.items()] + ["}"]
open(os.path.join(TK, "colors.css"), "w").write("\n".join(css) + "\n")
json.dump({"brand": BRAND, "scales": SCALES, "semantic": {"light": SEM_L, "dark": SEM_D}, "space": SPACE, "radius": RADII, "shadow": SHADOWS}, open(os.path.join(TK, "tokens.json"), "w"), indent=2)
open(os.path.join(TK, "tailwind.preset.js"), "w").write(
    "module.exports = {\n  theme: {\n    extend: {\n      colors: " +
    json.dumps({n: {str(k): v for k, v in sc.items()} for n, sc in SCALES.items()}, indent=8)[:-1] + "      },\n" +
    "      fontFamily: { display: ['\"Bricolage Grotesque\"', 'sans-serif'], sans: ['Geist', 'sans-serif'], mono: ['\"Geist Mono\"', 'monospace'] },\n" +
    "      transitionTimingFunction: { arrive: 'cubic-bezier(.2,.9,.25,1.15)' },\n    },\n  },\n};\n")
UITYPE = [("UI Display", 32, 36, 650, 96, -0.03), ("Title 1", 24, 30, 650, 48, -0.024), ("Title 2", 19, 25, 650, 32, -0.018),
          ("Title 3", 15, 21, 600, 24, -0.012), ("UI Body", 15, 22, 400, 16, -0.006), ("UI Small", 13, 18, 400, 14, 0), ("UI Caption", 12, 16, 500, 12, 0)]
TYPE = [("Display", 72, 76, 700, 96, -0.02), ("H1", 48, 54, 700, 72, -0.015), ("H2", 32, 38, 700, 48, -0.01),
        ("H3", 24, 30, 650, 32, -0.005), ("Body L", 18, 28, 400, 18, 0), ("Body", 16, 24, 400, 16, 0),
        ("Small", 14, 20, 400, 14, 0), ("Caption", 12, 16, 500, 12, 0)]
GEIST_ROLES = {"Title 3", "UI Body", "UI Small", "UI Caption", "Body L", "Body", "Small", "Caption"}     # everything else is Bricolage
def _tcss(n, s, lh, w, o, ls):
    ui = n in GEIST_ROLES
    return (f".hd-{n.lower().replace(' ', '-')} {{ font-family: var(--hd-font-{'ui' if ui else 'display'}); font-size: {s}px; line-height: {lh}px; font-weight: {w}; "
            + ("" if ui else f"font-variation-settings: 'opsz' {o}; ") + f"letter-spacing: {ls}em; }}")
open(os.path.join(TK, "type.css"), "w").write("\n".join(_tcss(*r) for r in TYPE + UITYPE) + "\n")

# ============================================================== core logo assets
LOCK_L = FN.lockup("light"); LOCK_D = FN.lockup("dark")
LOCK_BW = FN.lockup("light", mono=PL.INK_TEXT_L); LOCK_WW = FN.lockup("dark", mono="#ffffff")
MARK_L = FN.square("light", 512); MARK_D = FN.square("dark", 512)
MARK_W = FN.square("dark", 512, mono="#ffffff"); MARK_B = FN.square("light", 512, mono=PL.INK_TEXT_L)
WORD_B = FN.wordmark_only("light"); WORD_W = FN.wordmark_only("dark")
ST_L = FN.lockup_stacked("light"); ST_D = FN.lockup_stacked("dark"); ST_W = FN.lockup_stacked("dark", mono="#ffffff")
APP_INK = FN.app_icon("dark", 512); APP_COB = FN.app_icon("dark", 512, tile="cobalt", mono="#ffffff"); APP_PAPER = FN.app_icon("light", 512, tile="paper")
INK = BRAND["ink"]; COB = BRAND["cobalt"]

# illustrations (iso family)
ILL = {}
try:
    import isoill as IL
    _ills = {}
    for name, fn in IL.ILLS:
        for th in ("light", "dark"):
            svg = F.square(fn, th, 512, 0.14)
            _ills[(name, th)] = save(os.path.join(A, "illustrations", f"hypedrive-ill-{name}-{th}.svg"), svg, 512)
    ILL = _ills
except Exception as _e:      # the illustration generator is edited by another agent: fall back to the last good files so the book still builds
    print("illustration generator failed, using saved files:", repr(_e)[:120])
    import types, glob
    _nm = []
    for _f in sorted(glob.glob(os.path.join(A, "illustrations", "hypedrive-ill-*-light.svg"))):
        n_ = os.path.basename(_f)[len("hypedrive-ill-"):-len("-light.svg")]; _nm.append(n_)
        for th in ("light", "dark"): ILL[(n_, th)] = open(os.path.join(A, "illustrations", f"hypedrive-ill-{n_}-{th}.svg")).read()
    try: _order = [n for n, _ in __import__("isoill").ILLS]
    except Exception: _order = []
    IL = types.SimpleNamespace(ILLS=[(n, None) for n in (_order if set(_order) == set(_nm) else _nm)])

# ============================================================== patterns
def pattern_parcels(bg, fg_mono, tile=240, scale_k=0.34, opacity=1.0):
    m = FN.square("dark" if bg != "#ffffff" else "light", 100, 0.0, mono=fg_mono)
    cells = []
    for (cx, cy) in [(0.25, 0.25), (0.75, 0.75)]:
        g, _, _ = place(m, cx*tile - tile*scale_k/2, cy*tile - tile*scale_k/2, w=tile*scale_k)
        cells.append(f'<g opacity="{opacity}">{g}</g>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {tile} {tile}" width="{tile}" height="{tile}"><rect width="{tile}" height="{tile}" fill="{bg}"/>{"".join(cells)}</svg>'

def tape_svg(w=2400, h=120, bg=None):
    """Packaging tape: the real one-colour lockup, repeated in whole units so the roll tiles seamlessly."""
    bg = bg or COB
    lk = FN.lockup("dark", mono="#ffffff", pad=0)
    lh = h*0.5; vw, vh = vb(lk)[2], vb(lk)[3]; lw = vw*lh/vh
    unit = lw + h*1.1
    n = max(1, round(w / unit)); w = n * unit
    parts = [place(lk, h*0.55 + i*unit, (h-lh)/2, h=lh)[0] for i in range(n)]
    edge = "".join(f'<rect x="0" y="{y}" width="{w:.1f}" height="3" fill="#000" fill-opacity=".12"/>' for y in (0, h-3))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h}" width="{w:.0f}" height="{h}"><rect width="{w:.1f}" height="{h}" fill="{bg}"/>{edge}{"".join(parts)}</svg>'

PAT_INK = save(os.path.join(A, "patterns", "pattern-parcels-ink.svg"), pattern_parcels(INK, SCALES["ink"][800]), 480)
PAT_COB = save(os.path.join(A, "patterns", "pattern-parcels-cobalt.svg"), pattern_parcels(COB, SCALES["cobalt"][500]), 480)
PAT_PAPER = save(os.path.join(A, "patterns", "pattern-parcels-paper.svg"), pattern_parcels("#ffffff", SCALES["ink"][100]), 480)
TAPE = save(os.path.join(A, "print", "packaging-tape.svg"), tape_svg(), 2400)
TAPE_V = save(os.path.join(A, "print", "packaging-tape-vermilion.svg"), tape_svg(bg=SCALES["vermilion"][500]), 2400)

def tiled(pattern, w, h, x=0, y=0, pid="p"):
    t = vb(pattern)[2]
    return (f'<defs><pattern id="{pid}" width="{t}" height="{t}" patternUnits="userSpaceOnUse" x="{x}" y="{y}">{namespaced(inner(pattern))}</pattern></defs>'
            f'<rect width="{w}" height="{h}" fill="url(#{pid})"/>')

# ============================================================== applications
TAGLINE = "Products in. Hype out."
def og_image():
    w, h = 1200, 630
    g, lw, lh = place(LOCK_WW, 90, 0, w=560)
    g, lw, lh = place(LOCK_D, 90, 190, w=560)
    tag, tw = outlined(TAGLINE, 54, 700, 96, "#ffffff", 100, 430)
    sub, _ = outlined("Brands ship it. Creators try it. Everyone hears about it.", 22, 450, 18, SCALES["ink"][300], 102, 490)
    big = FN.square("dark", 100, 0.0)
    bg_, _, _ = place(big, 860, 150, w=280)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="{INK}"/>'
            f'{bg_}{g}{tag}{sub}</svg>')
def avatar():
    s = 800; g, _, _ = place(FN.square("dark", 100, 0.0), s*0.21, s*0.21, w=s*0.58)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}" width="{s}" height="{s}"><rect width="{s}" height="{s}" fill="{INK}"/>{g}</svg>'
def banner():
    w, h = 1500, 500
    g, _, _ = place(LOCK_D, 120, 150, w=620)
    tag, _ = outlined(TAGLINE, 40, 700, 96, SCALES["marigold"][300], 128, 400)
    ills = "".join(place(ILL[(n, "dark")], x, y, w=s)[0] for n, x, y, s in [("content", 930, 60, 230), ("payout", 1150, 200, 230), ("tracking", 950, 290, 210)])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="{INK}"/>'
            f'{ills}{g}{tag}</svg>')
def card_front():
    w, h = 1050, 600
    g, _, _ = place(FN.square("dark", 100, 0.0), w/2 - 120, h/2 - 120, w=240)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect width="{w}" height="{h}" rx="28" fill="{INK}"/>'
            f'{g}</svg>')
def card_back():
    w, h = 1050, 600
    g, _, _ = place(LOCK_L, 70, 60, w=330)
    name, _ = outlined("Full Name", 34, 700, 48, INK, 82, 380)
    role, _ = outlined("Role, Hypedrive", 18, 450, 16, SCALES["ink"][600], 82, 420)
    mail, _ = outlined("name@yourdomain.com", 18, 450, 16, INK, 82, 500)
    tel, _ = outlined("+00 00000 00000", 18, 450, 16, INK, 82, 534)
    stripe = ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><clipPath id="cb"><rect width="{w}" height="{h}" rx="28"/></clipPath>'
            f'<g clip-path="url(#cb)"><rect width="{w}" height="{h}" fill="#fff"/>{stripe}</g>{g}{name}{role}{mail}{tel}</svg>')
def shipping_label():
    """A calm courier label, 4 x 6 in: small lockup, an ink tag, hairline rules, ink type, a barcode."""
    w, h = 600, 900; I_ = SCALES["ink"]; PAD = 44; HAIR = "#e8e8eb"
    g, lw, lh = place(FN.lockup("light", pad=0), PAD, 46, w=176)
    tg_txt, tw_ = outlined("PRIORITY · CREATOR DROP", 12, 600, 12, "#ffffff", 0, 0, 0.06, "Geist")
    tag_w = tw_ + 28
    tag = (f'<rect x="{w - PAD - tag_w:.1f}" y="46" width="{tag_w:.1f}" height="30" rx="6" fill="{INK}"/>'
           + outlined("PRIORITY · CREATOR DROP", 12, 600, 12, "#ffffff", w - PAD - tag_w + 14, 66, 0.06, "Geist")[0])
    lab = lambda t, x, y: outlined(t, 13, 600, 12, I_[500], x, y, 0.0, "Geist")[0]
    txt = lambda t, x, y, c=INK, cap=15, wg=500, fnt="Geist": outlined(t, cap, wg, 16, c, x, y, -0.02 if fnt == "Bricolage" else 0.0, fnt)[0]
    rule = lambda y: f'<rect x="{PAD}" y="{y}" width="{w - 2*PAD}" height="1" fill="{HAIR}"/>'
    import random; random.seed(7)
    bars = []; x = PAD
    while x < w - PAD - 4:
        bw = random.choice([2, 3, 4, 6]); bars.append(f'<rect x="{x}" y="656" width="{bw}" height="132" fill="{INK}"/>'); x += bw + random.choice([2, 3, 4])
    body = (rule(112)
            + lab("Ship to", PAD, 156) + txt("Riya Sharma", PAD, 206, INK, 28, 700, "Bricolage") 
            + txt("14 Park Street", PAD, 246, I_[700], 17, 450) + txt("Kolkata 700016, West Bengal", PAD, 276, I_[700], 17, 450) + txt("India", PAD, 306, I_[700], 17, 450)
            + rule(344)
            + lab("From", PAD, 388) + txt("Lumen Labs", PAD, 418, INK, 17, 600) + txt("Plot 22, Sector V", PAD, 446, I_[700], 15, 450) + txt("Kolkata 700091", PAD, 470, I_[700], 15, 450)
            + lab("Product", 330, 388) + txt("Glow serum, 30 ml", 330, 418, INK, 17, 600) + txt("Small box · 180 g", 330, 446, I_[700], 15, 450)
            + rule(494)
            + lab("Tracking", PAD, 538) + lab("Drop", 330, 538) + txt("HD 0000 0000 0000", PAD, 570, INK, 17, 600) + txt("No. 2041", 330, 570, INK, 17, 600)
            + rule(612) + "".join(bars) + (lambda r: f'<g transform="translate({w/2 - r[1]/2:.1f} 0)">{r[0]}</g>')(outlined("HD 0000 0000 0000", 15, 500, 16, INK, 0, 834, 0.1, "Geist")))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="14" fill="#fff" stroke="{HAIR}"/>'
            f'{g}{tag}{body}</svg>')
def splash(mono):
    w, h = 1170, 2532
    lk = FN.lockup("light", mono=INK, pad=0) if mono else FN.lockup("dark", pad=0)      # tight lockup: the 62% is the logo itself, not its clear space
    _, lw, lh = place(lk, 0, 0, w=w*0.62)
    g, lw, lh = place(lk, w*0.19, h/2 - lh/2, w=w*0.62)
    bg = '#ffffff' if mono else INK
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="{bg}"/>{g}</svg>'

def splash_cobalt():
    w, h = 1170, 2532
    lk = FN.lockup("dark", mono="#ffffff", pad=0)
    _, lw, lh = place(lk, 0, 0, w=w*0.62)
    g, lw, lh = place(lk, w*0.19, h/2 - lh/2, w=w*0.62)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="{COB}"/>{g}</svg>'
APPS = {
    "og": save(os.path.join(A, "social", "og-image-1200x630.svg"), og_image(), 1200),
    "avatar": save(os.path.join(A, "social", "avatar-800.svg"), avatar(), 800),
    "banner": save(os.path.join(A, "social", "banner-1500x500.svg"), banner(), 1500),
    "card_f": save(os.path.join(A, "print", "business-card-front.svg"), card_front(), 1050),
    "card_b": save(os.path.join(A, "print", "business-card-back.svg"), card_back(), 1050),
    "label": save(os.path.join(A, "print", "shipping-label-4x6.svg"), shipping_label(), 600),
    "splash_c": save(os.path.join(A, "screens", "splash-color.svg"), splash(False), 1170),
    "splash_m": save(os.path.join(A, "screens", "splash-paper.svg"), splash(True), 1170),
    "splash_cob": save(os.path.join(A, "screens", "splash-cobalt.svg"), splash_cobalt(), 1170),
}

# construction diagram
def construction():
    c = F.Ctx("light"); body = FN.parcel(c)
    W = D = H = 10.0
    lines = []
    st = 'stroke="#2380ff" stroke-width="0.06" stroke-opacity=".9"'
    for i in range(11):
        a, b = F.P(i, 0, H), F.P(i, D, H); lines.append(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" {st}/>')
        a, b = F.P(0, i, H), F.P(W, i, H); lines.append(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" {st}/>')
        a, b = F.P(i, D, 0), F.P(i, D, H); lines.append(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" {st}/>')
        a, b = F.P(0, D, i), F.P(W, D, i); lines.append(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" {st}/>')
        a, b = F.P(W, i, 0), F.P(W, i, H); lines.append(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" {st}/>')
        a, b = F.P(W, 0, i), F.P(W, D, i); lines.append(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" {st}/>')
    xs = [p[0] for p in c.pts]; ys = [p[1] for p in c.pts]
    x0, y0, x1, y1 = min(xs)-2, min(ys)-2, max(xs)+2, max(ys)+2
    ox, oy = F.P(W, D, 0)
    ang = (f'<path d="M{ox+3:.2f} {oy:.2f}A3 3 0 0 0 {ox+3*math.cos(math.radians(30)):.2f} {oy-1.5:.2f}" fill="none" stroke="{COB}" stroke-width="0.08"/>'
           f'<line x1="{ox:.2f}" y1="{oy:.2f}" x2="{ox+4.5:.2f}" y2="{oy:.2f}" stroke="{COB}" stroke-width="0.06" stroke-dasharray=".3 .2"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.2f} {y0:.2f} {x1-x0+5:.2f} {y1-y0:.2f}" width="800" height="800">'
            f'<defs>{"".join(c.defs)}</defs><g opacity=".9">{body}</g>{"".join(lines)}{ang}</svg>')
CONSTR = construction()

def clearspace():
    lk = LOCK_L; vx, vy, vw, vh = vb(lk); pad = FN.CAP*0.5
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx} {vy} {vw} {vh}" width="{vw*10:.0f}" height="{vh*10:.0f}">'
            f'<rect x="{vx}" y="{vy}" width="{vw}" height="{vh}" fill="{SCALES["cobalt"][50]}"/>'
            f'<rect x="{vx+pad}" y="{vy+pad}" width="{vw-2*pad}" height="{vh-2*pad}" fill="#fff" stroke="{SCALES["cobalt"][400]}" stroke-width="0.12" stroke-dasharray=".6 .4"/>'
            f'{inner(lk)}</svg>')
CLEAR = clearspace()

# ============================================================== the book
font64 = base64.b64encode(open("/tmp/hdwm/fonts/Bricolage.ttf", "rb").read()).decode()
geist64 = base64.b64encode(open("/tmp/hdwm/fonts/Geist.ttf", "rb").read()).decode()
gmono64 = base64.b64encode(open("/tmp/hdwm/fonts/GeistMono.ttf", "rb").read()).decode()
def img(svg, style="", cls="", alt="Hypedrive"): return f'<img class="{cls}" style="{style}" alt="{alt}" src="{uri(svg)}"/>'
def swatch_block(name, hexv, note):
    r, g, b = rgb(hexv)
    on = "#fff" if contrast(hexv, "#ffffff") > contrast(hexv, INK) else INK
    return (f'<div class="sw" style="background:{hexv};color:{on}"><b>{name}</b><span>{hexv.upper()}<br>RGB {r} {g} {b}<br>'
            f'{"White text " + format(contrast(hexv, "#fff"), ".1f") + ":1" if on == "#fff" else "Ink text " + format(contrast(hexv, INK), ".1f") + ":1"}</span><i>{note}</i></div>')
def scale_row(n, sc):
    chips = "".join(f'<div class="chip" style="background:{h};color:{"#fff" if contrast(h, "#fff") >= 3 else INK}"><b>{s}</b><span>{h}</span></div>' for s, h in sc.items())
    return f'<div class="srow"><div class="sname">{n.title()}</div>{chips}</div>'
def pair(fg, bg, label):
    r = contrast(fg, bg); badge = "AAA" if r >= 7 else "AA" if r >= 4.5 else "AA Large" if r >= 3 else "Fail"
    return f'<div class="pair" style="background:{bg};color:{fg}"><b>Aa</b><span>{label}</span><em>{r:.1f}:1 · {badge}</em></div>'

PAIRS = [(INK, "#ffffff", "Ink on Paper"), ("#ffffff", INK, "Paper on Ink"), ("#ffffff", SCALES["cobalt"][600], "Paper on Cobalt 600"),
         (INK, BRAND["marigold"], "Ink on Marigold"), ("#ffffff", SCALES["vermilion"][600], "Paper on Vermilion 600"),
         (SCALES["cobalt"][700], SCALES["cobalt"][50], "Cobalt 700 on Cobalt 50"), (SCALES["ink"][600], "#ffffff", "Ink 600 on Paper"),
         ("#ffffff", BRAND["marigold"], "Paper on Marigold — never")]


def crop(svg, x, y, w, h):
    return re.sub(r'viewBox="[^"]+" width="[^"]+" height="[^"]+"', f'viewBox="{x} {y} {w} {h}" width="{w*20:.0f}" height="{h*20:.0f}"', svg, count=1)

def page(content, cls="", style=""): return f'<section class="page {cls}" style="{style}">{content}</section>'
def head(num, title, lead=""): return f'<header><small>{num}</small><h2>{title}</h2>{f"<p class=lead>{lead}</p>" if lead else ""}</header>'

ill_grid = "".join(f'<figure>{img(ILL[(n, "light")])}<figcaption>{n.title()}</figcaption></figure>' for n, _ in IL.ILLS)
dont = [("transform:scaleX(1.35);width:58%", "Don’t stretch or squash"), ("transform:rotate(-14deg)", "Don’t rotate"),
        ("filter:hue-rotate(140deg)", "Don’t recolour the faces"), ("filter:drop-shadow(8px 10px 6px rgba(0,0,0,.45))", "Don’t add shadows or effects"),
        ("opacity:.35", "Don’t fade it out"), ("", "Don’t place colour logo on busy colour")]
dont_html = "".join(f'<figure class="dont"><div class="dbox">{(f'<div style="background:{SCALES["vermilion"][400]};border-radius:14px;width:80%;height:128px;display:flex;align-items:center;justify-content:center">' + img(LOCK_L, "width:78%;" + s, alt="Incorrect logo use") + '</div>') if i == 5 else img(LOCK_L, "width:78%;" + s, alt="Incorrect logo use")}</div><figcaption>{{NO:{t}}}</figcaption></figure>' for i, (s, t) in enumerate(dont))
# ---- real UI renders (kit PNGs) -------------------------------------------------
from PIL import Image as _Im, ImageDraw as _ID
import io as _io
UIDIR = os.path.expanduser("~/Downloads/hypedrive-wordmark/BRAND/ui"); BSHOT = "/tmp/hdwm/bookshots3"
def _b64(im, fmt="PNG"):
    buf = _io.BytesIO(); im.save(buf, fmt, optimize=True); return f"data:image/{fmt.lower()};base64," + base64.b64encode(buf.getvalue()).decode()
def _clear_corners(im):
    im = im.convert("RGBA"); bgc = im.getpixel((0, 0))
    for p in ((0, 0), (im.width - 1, 0), (0, im.height - 1), (im.width - 1, im.height - 1)): _ID.floodfill(im, p, (0, 0, 0, 0), thresh=10)
    return im
def real_phone(name, h):
    im = _Im.open(f"{UIDIR}/screens/{name}.png").convert("RGB").crop((29, 29, 421, 875)); im = _clear_corners(im)
    w = round(im.width * (h * 1.5) / im.height); im = im.resize((w, round(h * 1.5)), _Im.LANCZOS)
    return f'<img class="rp" alt="Hypedrive mobile screen" style="height:{h}px" src="{_b64(im)}"/>'
def real_desktop(name, h):
    im = _Im.open(f"{UIDIR}/{name}.png").convert("RGB").crop((41, 41, 1480, 940)); im = _clear_corners(im)
    w = round(im.width * (h * 1.5) / im.height); im = im.resize((w, round(h * 1.5)), _Im.LANCZOS)
    return f'<img class="rp" alt="Hypedrive desktop screen" style="height:{h}px;border-radius:14px;box-shadow:0 0 0 1px {I[200]}" src="{_b64(im)}"/>'
def _trim_crop(im, pad=1):
    from PIL import ImageChops
    box = ImageChops.difference(im, _Im.new("RGB", im.size, im.getpixel((2, im.height - 2)))).getbbox()
    return im.crop((max(box[0] - pad, 0), max(box[1] - pad, 0), min(box[2] + pad, im.width), min(box[3] + pad, im.height))) if box else im
def crop_img(n, theme, w, extra=""):
    im = _trim_crop(_Im.open(f"{BSHOT}/sec{n}-{theme}.png").convert("RGB")); tw = min(im.width, round(w * 1.5))
    im = im.resize((tw, round(im.height * tw / im.width)), _Im.LANCZOS)
    return f'<img class="crop" alt="UI kit section" style="width:{w}px;{extra}" src="{_b64(im)}"/>'
def rules_inl(items, cols, top=28):
    return f'<div class="rules c{cols} inl" style="margin-top:{top}px">' + "".join(f'<div><b>{t}</b><p>{p}</p></div>' for t, p in items) + '</div>'
def rules(items, cols=1):
    return f'<div class="rules c{cols}">' + "".join(f'<div><b>{t}</b><p>{p}</p></div>' for t, p in items) + '</div>'

# ---- typography -----------------------------------------------------------------
FONT_ROLES = [("Bricolage Grotesque", "Brand voice", "Display, headings, hero numbers", "var(--hd-font-display)", "font-weight:650;font-variation-settings:'opsz' 96;letter-spacing:-.02em",
               "Products in. Hype out.", "Variable: opsz 12–96, wdth 75–100, wght 200–800"),
              ("Geist", "Interface", "Every label, row, button, field and paragraph in the product", "var(--hd-font-ui)", "font-weight:400",
               "120 creators are trying your serum this week.", "Variable: wght 100–900 · Open Font License"),
              ("Geist Mono", "Codes and IDs", "Tracking numbers, order IDs, API keys. Never inside running text", "var(--hd-font-mono)", "font-weight:450",
               "Delhivery 4471 2280", "Variable: wght 100–900 · Open Font License")]
SAMPLE_STY = ["font-weight:650;letter-spacing:-.02em;font-variation-settings:'opsz' 48", "font-weight:400", "font-weight:450"]
font_cards = "".join(f'<div class="fcard"><div class="fa" style="font-family:{fam};{sty}">Aa</div><b class="fn">{n}</b><span class="fr">{r}</span><p class="fu">{u}</p>'
                     f'<p class="fs" style="font-family:{fam};{SAMPLE_STY[i]}">{s}</p><p class="cap">{cap}</p></div>'
                     for i, (n, r, u, fam, sty, s, cap) in enumerate(FONT_ROLES))
def trow_html(n, s, lh, w, o, ls, fam, label, text):
    st = f"font-family:{fam};font-size:{s}px;line-height:{lh}px;font-weight:{w};letter-spacing:{ls}em" + (f";font-variation-settings:'opsz' {o}" if "display" in fam else "")
    return (f'<div class="trow"><div class="tmeta"><b>{n}</b><span>{s}/{lh} · {w} · {label}{f" · opsz {o}" if "display" in fam else ""} · {ls:+.3f}em</span></div><div style="{st}">{text}</div></div>')
BRAND_ROWS = "".join(trow_html(n, s, lh, w, o, ls, "var(--hd-font-ui)" if n in GEIST_ROLES else "var(--hd-font-display)", "Geist" if n in GEIST_ROLES else "Bricolage",
                               "Products in. Hype out." if s >= 24 else "Creators get the product, try it for real, and tell their people. Payouts land fast and fair.") for n, s, lh, w, o, ls in TYPE)
UI_SAMPLES = {"UI Display": "Hi Riya, 3 drops picked for you.", "Title 1": "Your drops", "Title 2": "Glow serum, 30 ml", "Title 3": "Riya Sharma",
              "UI Body": "Used it every night for two weeks. Light, no smell, and my skin feels calmer.", "UI Small": "Lumen Labs · 120 creators · ends Friday", "UI Caption": "Nov 12 · approved in 2 h"}
UI_ROWS = "".join(trow_html(n.replace("UI ", ""), s, lh, w, o, ls, "var(--hd-font-ui)" if n in GEIST_ROLES else "var(--hd-font-display)", "Geist" if n in GEIST_ROLES else "Bricolage", UI_SAMPLES[n]) for n, s, lh, w, o, ls in UITYPE)

PG_TYPE = [
 page(head("00", "Three typefaces", "Three typefaces, three jobs. Bricolage Grotesque speaks for the brand, Geist runs the interface, and Geist Mono carries codes and IDs.") +
      f'<div class="fonts3">{font_cards}</div>'
      f'<div class="values"><div><b>One job each</b><span>Never set interface text in Bricolage, and never set running text in Geist Mono.</span></div>'
      f'<div><b>Weights with restraint</b><span>Titles 650, buttons and labels about 560, body 400. Never 700 everywhere.</span></div>'
      f'<div><b>Sentence case</b><span>No capitals for emphasis and no letter-spaced labels. Hierarchy comes from size and weight.</span></div></div>'),
 page(head("00", "Type scale: brand", "For brand surfaces: posters, social, the book. Headlines are Bricolage with its optical size set to the text size; the body roles are Geist.") + f'<div class="tscale">{BRAND_ROWS}</div>'),
 page(head("00", "Type scale: interface", "Seven roles, the same on every screen. Display and the first two titles are Bricolage; everything from Title 3 down is Geist.") + f'<div class="tscale">{UI_ROWS}</div>'
      f'<p class="cap" style="margin-top:18px">Tokens: <code>--hd-font-display</code> Bricolage Grotesque · <code>--hd-font-ui</code> Geist · <code>--hd-font-mono</code> Geist Mono. Classes in <code>tokens/type.css</code>.</p>'),
]

# ---- layout, radius, elevation --------------------------------------------------
def rshape(w, h, r, kind):
    if kind == "btn": return f'<div class="rs" style="width:{w}px;height:{h}px;border-radius:{r}px;background:var(--hd-accent);color:#fff">Send</div>'
    if kind == "grey": return f'<div class="rs" style="width:{w}px;height:{h}px;border-radius:{r}px;background:var(--hd-surface);box-shadow:inset 0 0 0 1px var(--hd-border-strong);color:var(--hd-fg)">Later</div>'
    if kind == "chip": return f'<div class="rs line" style="width:{w}px;height:{h}px;border-radius:{r}px">For you</div>'
    if kind == "badge": return f'<div class="rs" style="width:{w}px;height:{h}px;border-radius:{r}px;background:{N[50]};color:{N[800]};font-size:15px;gap:5px"><svg width="14" height="14" viewBox="0 0 14 14"><circle cx="7" cy="7" r="7" fill="{N[600]}"/><path d="M4 7.2l2 2 4-4.4" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Live</div>'
    if kind == "check": return f'<div class="rs" style="width:{w}px;height:{h}px;border-radius:{r}px;background:var(--hd-accent);color:#fff"><svg width="14" height="14" viewBox="0 0 14 14"><path d="M2.5 7.5l3 3 6-7" fill="none" stroke="#fff" stroke-width="2"/></svg></div>'
    if kind == "input": return f'<div class="rs line" style="width:{w}px;height:{h}px;border-radius:{r}px;justify-content:flex-start;padding-left:14px;color:var(--hd-fg-subtle)">Search drops</div>'
    return f'<div class="rs line" style="width:{w}px;height:{h}px;border-radius:{r}px"></div>'
RAD = [("Button", "12", 132, 44, 12, "btn", "44 tall · height × 0.27"), ("Small button", "8", 96, 32, 8, "grey", "32 tall"), ("Chip", "8–10", 92, 32, 9, "chip", "32 tall"),
       ("Badge", "6", 56, 22, 6, "badge", "22 tall"), ("Checkbox", "6", 22, 22, 6, "check", "22 square"), ("Input", "12", 200, 44, 12, "input", "44 tall"),
       ("Card, panel", "16", 200, 56, 16, "card", "Rows, stat cards, panels"), ("Dialog, sheet", "24", 200, 64, 24, "card", "Floating, largest"), ("Tag", "8", 72, 28, 8, "chip", "28 tall")]
rad_cells = "".join(f'<div class="rc"><div class="rz">{rshape(w, h, r, k)}</div><b>{n} · {v}</b><span>{note}</span></div>' for n, v, w, h, r, k, note in RAD)
conc = "".join(f'<div class="cc"><div style="border-radius:{o}px;padding:{g}px"><div style="border-radius:{max(o - g, 4)}px"></div></div><b>outer {o} − gap {g} = {max(o - g, 4)}</b></div>' for o, g in ((24, 8), (16, 8), (16, 12)))
def flat(t): return f'<div class="ft"><b>{t}</b></div>'
def elev_panel(theme):
    return (f'<div class="ep" data-theme="{theme}"><h4>{theme.title()}</h4><p class="eh">Level 0: a 1 px border, no shadow</p><div class="e4">' + "".join(flat(t) for t in ("Card", "Row", "Panel", "Stat card")) + '</div>'
            f'<p class="eh">Floating: shadow</p><div class="e3x">' + "".join(f'<div class="ff" style="box-shadow:var(--hd-shadow-{k})"><b>{k}</b><span>{t}</span></div>' for k, t in (("e1", "Tooltips, small menus"), ("e2", "Menus, popovers, toasts"), ("e3", "Sheets, dialogs"))) + '</div></div>')
PG_LAYOUT = [
 page(head("00", "Layout & spacing", "A 4-pixel base. Every gap, padding and radius comes from these steps, named by role. No per-page margins and no one-off values.") +
      f'<div class="cols2" style="grid-template-columns:1.25fr 1fr;gap:56px"><div class="space">' + "".join(f'<div><i style="width:{v*4}px"></i><b>space-{i+1}</b><span>{v}px</span></div>' for i, v in enumerate(SPACE)) + '</div>'
      + rules([("Hit areas", "44 px for anything you tap: top bar icons, search, buttons, tabs. Small controls grow their hit area, not their look."),
               ("Row cards", "Every list item is its own rounded card with a gap between. Only tables and nav or settings menus join rows with inset dividers."),
               ("Real estate", "Empty states show suggestions and related items, never a lone illustration.")]) + '</div>'
      f'<h3 style="margin:34px 0 12px">Spacing in use</h3><div class="cols3 sdemo">'
      f'<div><div class="sd"><p class="sc">Glow serum</p><i class="gap" style="height:12px"><em>space-3 · 12</em></i><p class="sc">Kick scooter</p></div><b>Between row cards</b><span>space-3, 12 px</span></div>'
      f'<div><div class="sd"><div class="sc pad"><u></u><span>Riya Sharma</span></div></div><b>Inside a card</b><span>space-4, 16 px of padding</span></div>'
      f'<div><div class="sd"><p class="sc">Your drops</p><i class="gap" style="height:24px"><em>space-5 · 24</em></i><p class="sc">Earnings</p></div><b>Between sections</b><span>space-5, 24 px</span></div></div>'),
 page(head("00", "Radius", "Radius is maths, not taste. Concentric elements take the outer radius minus the gap, never below 4. Everything else is about 0.27 of its height.") +
      f'<div class="rwrap"><div class="rgrid">{rad_cells}</div><div class="rside"><h3>Concentric</h3><p class="cap" style="margin:0 0 14px">Inner = max(outer − gap, 4). A row inside a card, an icon tile inside a row.</p>{conc}'
      f'<p class="cap" style="margin-top:14px">Phone frame 52 outer, 42 screen. Pills (999) only for avatars and toggles.</p></div></div>'),
 page(head("00", "Elevation", "Cards and rows sit at level 0: a crisp native 1 px border and no shadow. Only floating things (menus, toasts, sheets, dialogs) lift. Inputs and tracks carry an inset shadow.") +
      f'<div class="elevs">{elev_panel("light")}{elev_panel("dark")}</div>'
      + rules([("Level 0 is a border", "Cards, rows, panels and stat cards carry a crisp 1 px native border and no shadow. Inputs and tracks add a small inset shadow so they read as recessed."),
               ("Floating things lift", "Deeper levels for tooltips and small menus, menus and toasts, then sheets and dialogs."),
               ("Dark shadows go deeper", "On Ink the shadow darkens and adds a faint top highlight, so a floating surface still reads.")], 3)),
]

# ---- brand in UI, components ----------------------------------------------------
PG_UI = [
 page(head("00", "The brand in UI: mobile", "Calm surfaces, one strong action. Cobalt marks the next thing to do; everything else stays quiet.") +
      f'<div class="uiflex"><div class="phones">{real_phone("03-home", 592)}{real_phone("04-drop-details", 592)}{real_phone("11-profile-dark", 592)}</div>'
      + rules([("Photos run full-bleed", "Product photos fill their card edge to edge. Controls sit over them on solid discs."),
               ("Stat cards, not tiles", "Home leads with one trend card. Counts, ratings and splits are compact stat cards with one anatomy."),
               ("Separate row cards", "Each drop is its own card. Product thumbnails sit bare, with no plate behind them."),
               ("Underline tabs", "Solid icons coloured by meaning, a Cobalt underline on the active tab. No pills."),
               ("Dark mode", "The same tokens remapped. Surfaces step up from Ink 950, Cobalt stays the action colour.")]) + '</div>'),
 page(head("00", "The brand in UI: desktop", "The same system with room to breathe: a grouped sidebar, a quiet top bar, stat cards with one anatomy, and a table only where a table helps.") +
      f'<div class="uiflex">{real_desktop("hypedrive-desktop-1", 560)}'
      + rules([("One search", "The sidebar's ⌘K is the global search. No second field."),
               ("Stat cards", "Label row with the delta top right, the value, then a visual pinned to the bottom. No captions, no pills."),
               ("Tint is rare", "Only for alerts, repeated statuses in tables and selected rows. A lone status stays solid."),
               ("Flat in flow", "Cards and panels carry a crisp 1 px border and no shadow. Inputs and tracks are inset.")]) + '</div>'),
]
PG_COMP = [
 page(head("00", "Components: buttons", "Flat deep Cobalt for the one main action. White with a 1 px hairline and a soft lip for everything secondary. Rendered from the UI kit, not redrawn.") +
      crop_img(2, "light", 1330, "margin:0 auto") +
      rules_inl([("Primary", "Flat deep Cobalt with a quiet tactile edge: faint top highlight, 1 px darker contact. 0.97 press. No glow."), ("Secondary", "White, with a 1 px hairline and a soft lip. Never grey. Disabled is solid grey."),
                 ("Icons on key actions only", "New, Upload, Export, Filter and icon-only buttons. Not every label."), ("Optical padding", "14 px on the icon side so icon and label look centred.")], 4)),
 page(head("00", "Components: navigation", "Bare icons in the top bar, underline tabs, a labelled four-item tab bar on phone. Light above, dark below.") +
      crop_img(4, "light", 1180, "display:block;margin:0 auto") + crop_img(4, "dark", 1180, "display:block;margin:12px auto 0") +
      rules_inl([("Underline tabs", "Icons are solid and coloured by meaning, the same everywhere: a box for Drops and Campaigns, people for Creators, a house for Home. The underline and the text colour show the active tab."),
                 ("Top bar", "Bare icons with no discs, 44 px hit areas. Discs appear only over a photo."),
                 ("Tab bar", "Four labelled items. A floating bar that hides the labels was tried and rejected: recognition matters more.")], 3, 22)),
 page(head("00", "Components: lists and data", "Every item is its own card. Rendered from the UI kit.") +
      crop_img(5, "light", 1180) +
      rules_inl([("Separate row cards", "A gap between every item, a crisp 1 px border around each, no shadow."), ("Bare product photos", "No plate, tile or ring behind a photo. A glyph fallback keeps its tile."),
                 ("Tinted badges", "Tinted at high contrast, with a solid status icon. No dot, ever."), ("Stat cards", "One anatomy, compact, customised per data type: trend, counts, rating, split, goal.")], 4, 24)),
 page(head("00", "Components: feedback", "Notices explain, toasts confirm, dialogs ask. One action each.") +
      crop_img(6, "light", 1424) +
      rules_inl([("Alerts are tinted", "The one place tint is the rule: a quiet wash (18 to 48% of the colour mixed into white) with strong-colour text at full contrast, and a solid icon."),
                 ("Floating means shadow", "Toasts, menus and dialogs lift with e2 or e3. Nothing else does."),
                 ("One focus ring", "A 2px gap in the surface colour plus 2px Cobalt, everywhere. Inputs focus with a 2px accent border.")], 3, 24)),
 page(head("00", "Components in dark: actions", "The same components on Ink. Surfaces step up from Ink 950, Cobalt stays the action colour, and secondary buttons keep their hairline and lip.") + crop_img(2, "dark", 1424) +
      rules_inl([("Primary and danger", "Unchanged from light: Cobalt and Vermilion keep their fills and white text."), ("Secondary", "A raised Ink surface with the same hairline and lip as on light."),
                 ("Disabled", "Solid grey with subtle text, never a faded version of the colour.")], 3, 24)),
 page(head("00", "Components in dark: feedback", "Notices, toasts, dialogs and sheets on Ink. Floating surfaces gain a faint top highlight so they still read.") + crop_img(6, "dark", 1424) +
      rules_inl([("Tint on Ink", "Dark tints mix 22 to 32% of the colour into #16181d, so a wash still separates from the surface."), ("Floating surfaces", "Toasts, menus, dialogs and sheets lift with e1 to e3 and a faint top highlight."),
                 ("One focus ring", "A 2 px gap in the surface colour plus 2 px Cobalt, the same as on light.")], 3, 24)),
]
PG_CHART = [
 page(head("00", "Charts & data", "Series are flat brand colours, drawn in a fixed order and labelled directly. Rendered from the UI kit.") +
      f'<div class="uiflex"><div style="width:1000px;flex:none">{crop_img(8, "light", 1000)}' +
      rules_inl([("Flat series", "Solid Cobalt, one Vermilion highlight. The only wash is a soft fill of the same colour under a line."),
                 ("Label directly", "Values and legends sit on the chart, in Geist. Tooltips are Ink with white text."),
                 ("Comparison is quiet", "The previous period is dashed and grey, never a second brand colour.")], 3, 24) +
      f'</div><div class="cside2"><h3>Categorical order</h3><div class="cat">' +
      "".join(f'<div><i style="background:{h}"></i><b>{i+1}. {n}</b><span>{h}</span></div>' for i, (n, h) in enumerate([("Cobalt 500", SCALES["cobalt"][500]), ("Vermilion 500", SCALES["vermilion"][500]), ("Marigold 300", SCALES["marigold"][300]), ("Mint 500", SCALES["mint"][500]), ("Ink 400", SCALES["ink"][400])])) +
      f'</div><h3 style="margin-top:18px">Sequential</h3><div class="seq">' + "".join(f'<i style="background:{SCALES["cobalt"][k]}"></i>' for k in (100, 200, 300, 400, 500, 600, 700, 800)) + '</div></div></div>'),
]

# ============================================================== EXPANSION 1: helpers + new application assets
SOCIAL_DIR = os.path.join(A, "social"); PRINT_DIR = os.path.join(A, "print")
STOCKP = os.path.join(UIDIR, "assets", "stock", "products")
_PH = {}
def photo_uri(name, maxw=1000, q=84, crop=None):
    """A stock product photo as a data URI, optionally cropped (fractions l,t,r,b) and downsized. Bare: no plate, no ring."""
    key = (name, maxw, q, crop)
    if key not in _PH:
        from PIL import Image as _I
        im = _I.open(os.path.join(STOCKP, name)).convert("RGB")
        if crop:
            l, t, r, b = crop; im = im.crop((round(l*im.width), round(t*im.height), round(r*im.width), round(b*im.height)))
        if im.width > maxw: im = im.resize((maxw, round(im.height*maxw/im.width)), _I.LANCZOS)
        buf = _io.BytesIO()
        im.save(buf, "JPEG", quality=q, optimize=True); _PH[key] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    return _PH[key]
def otext(text, cap, x, y, fill, wght=700, font="Bricolage", opsz=96, track=0.0, anchor="start"):
    """Outlined text at cap-height `cap`; Bricolage (display) or Geist (UI). Returns (svg, width)."""
    axes = {"opsz": opsz, "wdth": 100} if font == "Bricolage" else {}
    d, w = text_path(text, wght, cap, track, font, axes)
    x0 = x - (w if anchor == "end" else w/2 if anchor == "middle" else 0)
    return f'<path fill="{fill}" transform="translate({x0:.2f} {y:.2f})" d="{d}"/>', w
def photo_rect(uid, name, x, y, w, h, rx=0, crop=None, maxw=1100, pos="xMidYMid"):
    return (f'<clipPath id="{uid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/></clipPath>'
            f'<image href="{photo_uri(name, maxw, crop=crop)}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="{pos} slice" clip-path="url(#{uid})"/>')
def svg_wrap(w, h, body): return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{body}</svg>'
LK_TIGHT_D = FN.lockup("dark", pad=0); LK_TIGHT_L = FN.lockup("light", pad=0); LK_TIGHT_W = FN.lockup("dark", mono="#ffffff", pad=0); LK_TIGHT_B = FN.lockup("light", mono=INK, pad=0)

def instagram_post():
    w = h = 1080; ph = 690
    photo = photo_rect("igp", "p6.jpg", 0, 0, w, ph, 0, crop=(0, 0.02, 1, 1))
    ill, _, _ = place(ILL[("parcel", "dark")], 640, 470, w=380)
    l1, _ = otext("Products in.", 74, 72, 800, "#ffffff", 700, opsz=96, track=-0.01)
    l2, _ = otext("Hype out.", 74, 72, 910, BRAND["marigold"], 700, opsz=96, track=-0.01)
    lk, _, _ = place(LK_TIGHT_W, 72, 970, w=250)
    sub, _ = otext("Try it first. Say it straight.", 26, w - 72, 1008, SCALES["ink"][300], 500, "Geist", track=0.0, anchor="end")
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{INK}"/>{photo}{ill}{l1}{l2}{lk}{sub}')
def instagram_story():
    w, h = 1080, 1920; ph = 1220
    photo = photo_rect("igs", "p5.jpg", 0, 0, w, ph, 0, crop=(0, 0.05, 1, 0.82), maxw=1080, pos="xMidYMid")
    ill, _, _ = place(ILL[("parcel", "dark")], 670, 1060, w=360)
    lk, _, _ = place(LK_TIGHT_W, 72, 1296, w=270)
    l1, _ = otext("Products in.", 78, 72, 1472, "#ffffff", 700, opsz=96, track=-0.01)
    l2, _ = otext("Hype out.", 78, 72, 1578, BRAND["marigold"], 700, opsz=96, track=-0.01)
    sub, _ = otext("Try it. Review it. Get paid.", 30, 72, 1660, SCALES["ink"][300], 500, "Geist")
    # IG safe zones: nothing but photo in the top 250 and nothing at all in the bottom 340
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{INK}"/>{photo}{ill}{lk}{l1}{l2}{sub}')
def email_header(light=False):
    w, h = 1200, 300
    bg = "#ffffff" if light else INK
    lk, lw, lh = place(LK_TIGHT_L if light else LK_TIGHT_D, 70, 0, w=420); lk, lw, lh = place(LK_TIGHT_L if light else LK_TIGHT_D, 70, (h-8)/2 - lh/2, w=420)
    tag, _ = otext(TAGLINE, 30, w - 70, (h-8)/2 + 11, INK if light else BRAND["marigold"], 700, opsz=48, anchor="end")
    third = w/3
    strip = "" if True else (f'<rect x="0" y="{h-8}" width="{third:.1f}" height="8" fill="{BRAND["marigold"]}"/><rect x="{third:.1f}" y="{h-8}" width="{third:.1f}" height="8" fill="{COB}"/>'
             f'<rect x="{2*third:.1f}" y="{h-8}" width="{third:.1f}" height="8" fill="{BRAND["vermilion"]}"/>')
    edge = f'<rect width="{w}" height="{h}" fill="none" stroke="{SCALES["ink"][200]}" stroke-width="2"/>' if light else ""
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{bg}"/>{lk}{tag}{strip}{edge}')
def media_kit_cover():
    w, h = 1240, 1754; m = 88
    lk, _, _ = place(LK_TIGHT_L, m, m, w=280)
    kind, _ = otext("Creator kit", 30, w - m, m + 36, SCALES["ink"][600], 600, "Geist", anchor="end")
    t1, _ = otext("Creator", 168, m, 620, INK, 700, opsz=96, track=-0.015)
    t2, _ = otext("media kit.", 168, m, 820, INK, 700, opsz=96, track=-0.015)
    sub1, _ = otext("Audience, rates and past drops,", 36, m, 930, SCALES["ink"][600], 400, "Geist")
    sub2, _ = otext("in one place.", 36, m, 984, SCALES["ink"][600], 400, "Geist")
    photo = photo_rect("mkp", "p7.jpg", 0, 1060, w, 544, 0, crop=(0, 0.05, 1, 0.95), pos="xMidYMid")
    ill, _, _ = place(ILL[("parcel", "light")], w - m - 300, 1604 - 300, w=330)
    band = f'<rect x="0" y="{h-150}" width="{w}" height="150" fill="#ffffff"/><rect x="{m}" y="{h-150}" width="{w-2*m}" height="2" fill="#e8e8eb"/>'
    name, _ = otext("Creator name", 40, m, h - 78, INK, 700, opsz=48)
    contact, _ = otext("@yourhandle  ·  hello@yourdomain.com", 28, m, h - 36, SCALES["ink"][600], 450, "Geist")
    year, _ = otext("2026", 40, w - m, h - 78, INK, 700, opsz=48, anchor="end")
    return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="#ffffff"/>{lk}{kind}{t1}{t2}{sub1}{sub2}{photo}{ill}{band}{name}{contact}{year}')

APPS2 = {
    "ig_post": save(os.path.join(SOCIAL_DIR, "instagram-post-1080.svg"), instagram_post(), 1080),
    "ig_story": save(os.path.join(SOCIAL_DIR, "instagram-story-1080x1920.svg"), instagram_story(), 1080),
    "email": save(os.path.join(SOCIAL_DIR, "email-header-1200x300.svg"), email_header(False), 1200),
    "email_l": save(os.path.join(SOCIAL_DIR, "email-header-light-1200x300.svg"), email_header(True), 1200),
    "kit": save(os.path.join(PRINT_DIR, "creator-media-kit-cover-a4.svg"), media_kit_cover(), 1240),
}

# ============================================================== EXPANSION 2: shared CSS helper, foundations, logo extended
from string import Template
PAL = {f"{k}{s}": SCALES[n][s] for k, n in (("i", "ink"), ("c", "cobalt"), ("v", "vermilion"), ("m", "marigold"), ("n", "mint")) for s in SCALES[n]}
PAL.update(n600u=N[600].replace("#", "%23"), ink=INK, cob=COB, mar=BRAND["marigold"], ver=BRAND["vermilion"])
XCSS = []
def xcss(s): XCSS.append(Template(s).substitute(PAL))
def ph_img(name, style="", maxw=1000, crop=None, cls="", alt="Product photo"):
    return f'<img class="{cls}" alt="{alt}" style="{style}" src="{photo_uri(name, maxw, crop=crop)}"/>'
def ill_img(n, th="light", style=""): return img(ILL[(n, th)], style, alt=f"{n} illustration")
_G_OK = '<svg class="vg" viewBox="0 0 16 16"><circle cx="8" cy="8" r="8" fill="#067647"/><path d="M4.6 8.3l2.2 2.2 4.6-4.8" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
_G_NO = '<svg class="vg" viewBox="0 0 16 16"><circle cx="8" cy="8" r="8" fill="#d92d20"/><path d="M5.2 5.2l5.6 5.6M10.8 5.2l-5.6 5.6" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round"/></svg>'
def _verdict(t, ok):
    t = re.sub(r"^(Do:|Don[’']t:?)\s+", "", t)
    if t.lower() in ("do", "don’t", "don't"): t = ""
    return f'<p class="xtag {"ok" if ok else "bad"}">{_G_OK if ok else _G_NO}<b>{"Do:" if ok else "Don’t:"}</b><span>{t[:1].lower() + t[1:] if t[1:2].islower() or t[1:2] in " ’" else t}</span></p>'
def tag_do(t): return _verdict(t, True)
def tag_no(t): return _verdict(t, False)
dont_html = re.sub(r'\{NO:([^}]*)\}', lambda m: tag_no(m.group(1)), dont_html)
xcss("""
.x2 { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; } .x3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; } .x4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 22px; }
.xcard { background: ${i50}; border-radius: 20px; padding: 28px; } .xcard p { margin: 0; font-family: var(--hd-font-ui); font-size: 17px; line-height: 1.5; color: ${i700}; }
.xcard h3 { margin: 0 0 8px; } .xcard .k { font-family: var(--hd-font-ui); font-size: 15px; font-weight: 600; color: ${i600}; margin: 14px 0 4px; display: block; }
.xtag { font-family: var(--hd-font-ui); font-size: 15px; line-height: 1.35; margin: 0 0 6px; display: flex; gap: 8px; align-items: flex-start; color: ${i600}; font-weight: 400; } .xtag .vg { width: 16px; height: 16px; flex: none; margin-top: 2px; } .xtag b { font-size: 13px; font-weight: 600; color: ${ink}; margin-top: 1px; } .xtag span { color: ${i600}; }
.x-note { font-family: var(--hd-font-ui); font-size: 15px; line-height: 1.5; color: ${i600}; margin: 0; }
.x-statement { font-size: 40px; line-height: 1.16; font-weight: 650; font-variation-settings: 'opsz' 48; letter-spacing: -.02em; max-width: 1180px; margin: 0 0 30px; text-wrap: balance; }
.x-aud { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; } .x-aud .xcard { padding: 26px 30px; } .x-aud h3 { font-size: 28px; margin-bottom: 4px; }
.x-flow { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-top: 26px; } .x-flow > div { display: grid; grid-template-columns: 96px 1fr; gap: 14px; align-items: center; border-top: 3px solid ${ink}; padding-top: 14px; }
.x-flow b { display: block; font-size: 19px; font-variation-settings: 'opsz' 24; } .x-flow span { font-family: var(--hd-font-ui); font-size: 15px; line-height: 1.4; color: ${i600}; display: block; margin-top: 2px; }
.x-pos { display: grid; grid-template-columns: 380px 1fr; gap: 56px; align-items: start; } .x-pos .x-statement { font-size: 32px; margin: 0 0 18px; }
.x-cmp { width: 100%; border-collapse: collapse; font-family: var(--hd-font-ui); } .x-cmp th { text-align: left; font-family: var(--hd-font-display); font-size: 22px; font-weight: 650; padding: 0 0 12px 22px; font-variation-settings: 'opsz' 32; }
.x-cmp th:first-child { padding-left: 0; } .x-cmp td { padding: 18px 0 18px 22px; border-top: 1px solid ${i200}; font-size: 17px; line-height: 1.4; color: ${i600}; vertical-align: top; } .x-cmp td:first-child { padding-left: 0; color: ${ink}; font-weight: 600; width: 170px; }
.x-cmp td:last-child { color: ${ink}; background: ${i50}; font-weight: 500; padding-right: 16px; } .x-cmp th:last-child { background: ${i50}; border-radius: 14px 14px 0 0; padding-top: 14px; } .x-cmp tr:last-child td:last-child { border-radius: 0 0 14px 14px; }
.x-traits { display: grid; grid-template-columns: repeat(4, 1fr); gap: 22px; } .x-trait { border-radius: 22px; background: ${i50}; padding: 24px 24px 26px; display: flex; flex-direction: column; }
.x-trait .tn { font-size: 36px; line-height: 1; font-weight: 700; font-variation-settings: 'opsz' 48; letter-spacing: -.02em; margin: 14px 0 4px; } .x-trait .tnot { font-family: var(--hd-font-ui); font-size: 16px; color: ${i600}; margin: 0 0 16px; }
.x-trait .ex { font-family: var(--hd-font-ui); font-size: 16px; line-height: 1.45; border-radius: 12px; padding: 12px 14px; margin: 5px 0 0; } .x-trait .ex.y { background: #fff; color: ${ink}; box-shadow: 0 0 0 1px ${n300}; } .x-trait .ex.n { background: #fff; color: ${i600}; box-shadow: 0 0 0 1px ${v300}; }
.x-trait .xtag { margin-top: 12px; }
""")
IL_PIC = lambda n, w=96, th="light": ill_img(n, th, f"width:{w}px")
PG_FOUND = [
 page(head("00", "Mission", "Honest reviews are the best advertising a product can get. Hypedrive makes them easy to ask for, easy to give, and fair to pay for.") +
      f'<p class="x-statement">Get real products to real creators, and pay them fairly for honest reviews.</p>'
      f'<div class="x-aud"><div class="xcard"><h3>Brands</h3><p>Small and growing brands in India that want real reviews from real people, and a clear view of what they spent.</p>'
      f'<span class="k">What Hypedrive gives them</span><p>List a drop, set the slots and a payout per review, approve what comes in, and pay in one step.</p></div>'
      f'<div class="xcard"><h3>Creators</h3><p>People who review products for their audience on Instagram, YouTube and the other places they already post.</p>'
      f'<span class="k">What Hypedrive gives them</span><p>Free products worth trying, a payout shown up front, and money that lands when we said it would.</p></div></div>'
      f'<div class="x-flow">'
      + "".join(f'<div>{IL_PIC(n)}<p style="margin:0"><b>{t}</b><span>{d}</span></p></div>' for n, t, d in [
          ("parcel", "A brand lists a drop", "Product, slots and payout, set once."), ("tracking", "The parcel arrives", "Tracked from the brand to the creator."),
          ("review", "An honest review goes live", "Checked: the link is public."), ("payout", "The creator is paid", "Within 48 hours of approval.")]) + '</div>'),
 page(head("00", "Positioning", "Generic influencer marketplaces sell reach. Hypedrive sells the one thing that persuades: someone you trust, using the product.") +
      f'<div class="x-pos"><div><p class="x-statement">The place where the product does the talking.</p>'
      f'<p class="x-note" style="font-size:17px">For brands that want honest reviews and creators who want fair pay, Hypedrive is the product-seeding platform that handles the parcel, the review and the payout.</p>'
      f'<p class="x-note" style="font-size:17px;margin-top:14px">We are not an agency, an ad network or a follower marketplace, and we never describe ourselves as one.</p></div>'
      f'<table class="x-cmp"><tr><th></th><th>A generic influencer marketplace</th><th>Hypedrive</th></tr>'
      + "".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in [
          ("What changes hands", "Reach and impressions", "A real product, tried for real"),
          ("What brands pay for", "A post and a promise of audience", "An honest review of the product"),
          ("The creator’s role", "An ad slot", "A reviewer whose opinion is the point"),
          ("Who gets picked", "The biggest following first", "Fit with the product first"),
          ("The money", "Negotiated in DMs, paid when it’s paid", "A payout shown up front, paid within 48 hours of approval"),
          ("The proof", "Screenshots in a spreadsheet", "Every parcel tracked, every review link checked"),
          ("The language", "Campaign, activation, deliverable", "Drop, try, review, payout")]) + '</table></div>'),
 page(head("00", "Personality", "Four traits, each with a limit. Every line we write and every screen we draw should pass the second half of each pair.") +
      '<div class="x-traits">' + "".join(
          f'<div class="x-trait">{IL_PIC(n, 110)}<div class="tn">{t}</div><p class="tnot">{nt}</p>{tag_do("Say this")}<p class="ex y">{y}</p>{tag_no("Say it this way")}<p class="ex n">{no}</p></div>'
          for n, t, nt, y, no in [
              ("bell", "Energetic", "not loud", "120 creators are trying your serum this week.", "HUGE DROP ALERT!!! Don’t miss out!!!"),
              ("shield", "Honest", "not stiff", "We hold ₹640 until the brand approves your review. It usually takes a day.", "Funds remain subject to a pending verification period."),
              ("gift", "Generous", "with credit", "Lumen Labs loved your Night cream review.", "Review processed."),
              ("tracking", "Quick", "to the point", "Pick one now. You can add more later.", "In order to continue, you are required to select at least one option from the list below.")]) + '</div>'),
]

# ---- logo, extended
xcss("""
.x-min { display: grid; grid-template-columns: repeat(4, 1fr); gap: 22px; } .x-min > div { background: ${i50}; border-radius: 20px; height: 300px; padding: 24px; display: flex; flex-direction: column; }
.x-min .sample { flex: 1; display: flex; align-items: center; justify-content: center; } .x-min .dim { height: 0; border-top: 2px solid ${c600}; position: relative; margin: 10px auto 0; } .x-min .dim::before, .x-min .dim::after { content: ''; position: absolute; top: -7px; width: 2px; height: 12px; background: ${c600}; } .x-min .dim::before { left: 0; } .x-min .dim::after { right: 0; }
.x-min b { font-size: 21px; margin-top: 14px; display: block; } .x-min span { font-family: var(--hd-font-ui); font-size: 15px; color: ${i600}; line-height: 1.45; display: block; margin-top: 3px; }
.x-tbl { width: 100%; border-collapse: collapse; font-family: var(--hd-font-ui); font-size: 16px; margin-top: 22px; } .x-tbl th { text-align: left; font-weight: 600; padding: 8px 14px 8px 0; color: ${i600}; border-bottom: 2px solid ${ink}; font-size: 15px; } .x-tbl td { padding: 10px 14px 10px 0; border-bottom: 1px solid ${i200}; font-variant-numeric: tabular-nums; } .x-tbl td:first-child { font-weight: 600; }
.x-ph4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 22px; } .x-ph { margin: 0; } .x-ph .fr { height: 360px; border-radius: 18px; position: relative; overflow: hidden; background: ${i100}; } .x-ph .fr > img.bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.x-ph .fr > img.lg { position: absolute; }
.x-ph figcaption { font-family: var(--hd-font-ui); font-size: 15px; line-height: 1.45; color: ${i700}; margin-top: 10px; } .x-ph figcaption .xtag { margin-bottom: 2px; }
.x-ph .scrim { position: absolute; left: 0; right: 0; bottom: 0; height: 52%; background: linear-gradient(to top, rgba(18,19,22,.74), rgba(18,19,22,0)); }
.x-co { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; } .x-co > div { height: 230px; border-radius: 20px; display: flex; align-items: center; justify-content: center; gap: 28px; border: 1px solid ${i100}; }
.x-co .dv { width: 2px; height: 60px; background: currentColor; opacity: .35; display: block; } .x-co .pt { font: 650 34px/1 var(--hd-font-ui); letter-spacing: -.02em; }
.x-ico { display: grid; grid-template-columns: 1.05fr 1fr; gap: 28px; } .x-ico > div { border-radius: 22px; padding: 26px 28px 24px; } .x-ico h3 { margin: 0 0 4px; font-size: 26px; }
.x-ios { display: flex; gap: 22px; align-items: flex-end; margin-top: 20px; } .x-ios figure { margin: 0; text-align: left; } .x-ios figcaption, .x-and figcaption { font-family: var(--hd-font-ui); font-size: 15px; color: ${i600}; margin-top: 8px; line-height: 1.35; }
.x-ios .ic { border-radius: 22.37%; display: block; overflow: hidden; box-shadow: 0 0 0 1px rgba(16,20,38,.08); } .x-ios .ic img { display: block; width: 100%; height: 100%; }
.x-and { display: flex; gap: 22px; align-items: flex-end; margin-top: 20px; } .x-and figure { margin: 0; } .x-and .ad { position: relative; background: ${ink}; overflow: hidden; } .x-and .ad img { position: absolute; inset: 0; width: 100%; height: 100%; }
.x-fav { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; } .x-fav .big { display: flex; gap: 30px; align-items: flex-end; background: ${i50}; border-radius: 22px; padding: 28px; }
.x-fav figure { margin: 0; } .x-fav figcaption { font-family: var(--hd-font-ui); font-size: 15px; color: ${i600}; margin-top: 10px; line-height: 1.4; } .px { image-rendering: pixelated; display: block; }
.x-tab { background: ${i200}; border-radius: 14px 14px 0 0; padding: 10px 12px 0; } .x-tab .t { display: flex; align-items: center; gap: 10px; background: #fff; border-radius: 10px 10px 0 0; height: 38px; padding: 0 14px; width: 330px; font: 500 15px var(--hd-font-ui); color: ${ink}; } .x-tab .t img { width: 16px; height: 16px; } .x-tab.bar { background: #fff; padding: 0 16px; height: 46px; border-radius: 0; border-bottom: 1px solid ${i200}; display: flex; align-items: center; font: 15px var(--hd-font-ui); color: ${i600}; }
.x-tab.dk { background: ${i950}; } .x-tab.dk .t { background: ${i800}; color: #fff; } .x-tab.dk.bar { background: ${i800}; border-color: ${i700}; color: ${i200}; }
""")
def tight(svg, w, style="", alt="Hypedrive"): return img(svg, f"width:{w}px;{style}", alt=alt)
def minbox(sample_svg, w, title, spec, note):
    return f'<div><div class="sample">{img(sample_svg, f"width:{w}px", alt=title)}</div><div class="dim" style="width:{w}px"></div><b>{title}</b><span>{spec}<br>{note}</span></div>'
FAVPNG = lambda n: "data:image/png;base64," + base64.b64encode(open(os.path.join(OUT, "assets", "logo", "favicon", f"favicon-{n}.png"), "rb").read()).decode()
def mm(px): return f"{px*25.4/96:.0f} mm"
IOS_ICON = FN.app_icon("dark", 512, rounded=False)
PG_LOGO2 = [
 page(head("00", "Minimum sizes", "Below the minimum the parcel loses its tape and the wordmark closes up. Use the next simpler form instead of shrinking further.") +
      '<div class="x-min">' + minbox(LK_TIGHT_L, 96, "Horizontal lockup", f"96 px on screen · {mm(96)} in print", "Narrower than this, use the parcel alone.")
      + minbox(FN.lockup_stacked("light"), 64, "Stacked lockup", f"64 px on screen · {mm(64)} in print", "For square and tall spaces only.")
      + minbox(WORD_B, 80, "Wordmark alone", f"80 px on screen · {mm(80)} in print", "Only where the parcel is already on the page.")
      + minbox(MARK_L, 64, "Parcel, full detail", f"64 px on screen · {mm(64)} in print", "Smaller than 64 px, use the favicon artwork.") + '</div>'
      f'<table class="x-tbl"><tr><th>Form</th><th>Screen</th><th>Print</th><th>Notes</th></tr>'
      f'<tr><td>Favicon, 48 and 32 px</td><td>48 px, 32 px</td><td>Not for print</td><td>Thicker tape and no dot, edges snapped to whole pixels.</td></tr>'
      f'<tr><td>Favicon, 16 px</td><td>16 px</td><td>Not for print</td><td>Faces only: the three colours of the parcel.</td></tr>'
      f'<tr><td>Clear space</td><td colspan="3">Half the cap height on every side, always. It is already built into the files in /assets/logo.</td></tr></table>'
      f'<p class="x-note" style="margin-top:12px">Pixels are CSS pixels at 96 per inch, so 96 px is about 25 mm. The shapes above are drawn at exactly these sizes.</p>'),
]
def ph_tile(cap_t, cap_d, bg, bgstyle, logo_svg, lw, lstyle, scrim=False, ok=True):
    return (f'<figure class="x-ph"><div class="fr"><img class="bg" style="{bgstyle}" src="{photo_uri(bg, 700)}" alt="Product photo"/>{"<div class=scrim></div>" if scrim else ""}'
            f'<img class="lg" style="width:{lw}px;{lstyle}" src="{uri(logo_svg)}" alt="Hypedrive"/></div><figcaption>{tag_do(cap_t) if ok else tag_no(cap_t)}{cap_d}</figcaption></figure>')
PG_LOGO3 = [
 page(head("00", "Logo on photographs", "The logo must stay readable against whatever is behind it. Either place it in a calm area, or give it a scrim. Never let the picture decide.") +
      '<div class="x-ph4">'
      + ph_tile("Paper logo on a scrim", "An Ink scrim from 0 to about 75% over the bottom half, with the one-colour Paper lockup sitting in it.", "p6.jpg", "object-position:50% 40%", LK_TIGHT_W, 190, "left:24px;bottom:24px", True)
      + ph_tile("Ink logo in a calm area", "No scrim needed when the logo sits on a plain area of the picture. Use the one-colour Ink lockup.", "p1.jpg", "object-position:50% 10%", LK_TIGHT_B, 190, "left:24px;top:24px")
      + ph_tile("Not the colour lockup on a busy picture", "Three colours plus a busy picture is noise. The parcel disappears.", "p6.jpg", "object-position:50% 40%", LK_TIGHT_L, 190, "left:24px;top:150px", ok=False)
      + ph_tile("Not Paper on a light picture", "White on a pale area fails. Check the logo against the picture, not the file.", "p1.jpg", "object-position:50% 10%", LK_TIGHT_W, 190, "left:24px;top:24px", ok=False)
      + '</div>' + rules_inl([("One-colour on photos", "Use the Paper or Ink one-colour lockup over photographs. The colour lockup is for flat Paper, Ink and Cobalt."),
                              ("Scrim", "Ink, 0 to about 75% opacity, growing toward the logo. Never a coloured wash, never a blur."),
                              ("Placement", "Corner, with the clear space kept. Not over the product, and not centred on the subject.")], 3, 22)),
 page(head("00", "Co-branding", "When a partner brand appears with us, the two logos share a line, never a container. The host goes first.") +
      '<div class="x-co">'
      f'<div style="background:#fff">{tight(LK_TIGHT_L, 250)}<i class="dv" style="color:{INK}"></i><span class="pt" style="color:{INK}">Partner</span></div>'
      f'<div style="background:{INK};color:#fff">{tight(LK_TIGHT_D, 250)}<i class="dv"></i><span class="pt">Partner</span></div>'
      f'<div style="background:{COB};color:#fff">{tight(LK_TIGHT_W, 250)}<i class="dv"></i><span class="pt">Partner</span></div></div>'
      f'<div class="x-ico" style="margin-top:22px;grid-template-columns:1.2fr 1fr;gap:34px"><div class="xcard" style="padding:24px 28px"><h3>The lockup, measured</h3>'
      f'<div style="display:flex;align-items:center;gap:0;margin:14px 0 8px;font-family:var(--hd-font-ui)"><div style="text-align:center;width:250px">{tight(LK_TIGHT_L, 250)}</div>'
      f'<div style="width:60px;text-align:center;color:{C[700]};font-size:15px;font-weight:600">2×</div><i style="width:2px;height:60px;background:{INK};opacity:.35;display:block"></i>'
      f'<div style="width:60px;text-align:center;color:{C[700]};font-size:15px;font-weight:600">2×</div><span style="font:650 34px/1 var(--hd-font-ui);letter-spacing:-.02em">Partner</span></div>'
      f'<p class="x-note">2× is twice the clear space (half the cap height) on each side of the divider. The divider is 2 px wide and about as tall as the parcel, in the text colour at 35%.</p></div>'
      + rules([("Equal weight", "Both wordmarks share a cap height. Neither logo is larger or bolder than the other."),
               ("Their logo, untouched", "Use the partner’s own artwork, in the Paper or Ink version when their colours clash with ours. Never recolour, outline or merge it."),
               ("Host first", "On a Hypedrive surface we go left. On a partner’s surface they do.")]) + '</div>'),
 page(head("00", "App icon", "The parcel on an Ink tile, at 60% of the tile. Cobalt is the one alternate. Shown at the sizes the phone actually draws.") +
      '<div class="x-ico"><div style="background:' + I[50] + '"><h3>iOS</h3><p class="x-note">One 1024 px square, no rounding: iOS applies the mask itself.</p><div class="x-ios">'
      + "".join(f'<figure><div class="ic" style="width:{s}px;height:{s}px">{img(IOS_ICON, alt="App icon")}</div><figcaption>{c}</figcaption></figure>' for s, c in [(180, "180 px<br>Home, 60 pt @3x"), (120, "120 px<br>Home, 60 pt @2x"), (87, "87 px<br>Settings"), (60, "60 px<br>Notification")])
      + '</div></div><div style="background:' + I[50] + '"><h3>Android</h3><p class="x-note">An adaptive icon: a 108 dp layer with the parcel inside the 66 dp safe zone, over an Ink background.</p><div class="x-and">'
      + f'<figure><div class="ad" style="width:216px;height:216px;border-radius:12px">{img(FN.square("dark", 432, 0.3), alt="Foreground layer")}<div style="position:absolute;left:42px;top:42px;width:132px;height:132px;border:2px dashed {BRAND["marigold"]};border-radius:50%"></div></div><figcaption>108 dp layer<br>66 dp safe zone dashed</figcaption></figure>'
      + "".join(f'<figure><div class="ad" style="width:96px;height:96px;border-radius:{r}">{img(FN.square("dark", 432, 0.3), alt="App icon")}</div><figcaption>{c}</figcaption></figure>' for r, c in [("50%", "Circle<br>48 dp"), ("34%", "Squircle<br>48 dp"), ("22%", "Rounded<br>48 dp")])
      + '</div></div></div>'
      + rules_inl([("The same drawing everywhere", "The iOS file and the Android foreground are the same parcel. Only the mask changes."), ("Cobalt tile", "One-colour Paper parcel on Cobalt for secondary uses. The blue face would vanish otherwise."), ("No text, no badge", "The name sits under the icon. Notification counts are drawn by the system.")], 3, 22)),
 page(head("00", "Favicon", "Three hand-snapped sizes. Edges land on whole pixels, so the parcel stays crisp at the size it is actually drawn.") +
      '<div class="x-fav"><div class="big">'
      + "".join(f'<figure><img class="px" src="{FAVPNG(n)}" width="{n}" height="{n}" alt="Favicon {n}"/><figcaption>{n} px</figcaption></figure>' for n in (16, 32, 48))
      + f'<figure style="margin-left:auto"><img src="{FAVPNG(180)}" width="120" height="120" alt="Touch icon" style="display:block;border-radius:22%"/><figcaption>180 px touch icon</figcaption></figure></div>'
      f'<div class="big" style="align-items:center;gap:22px">'
      + "".join(f'<figure><img class="px" src="{FAVPNG(n)}" width="{n*5}" height="{n*5}" alt="Favicon {n} enlarged"/><figcaption>{n} px at 5×</figcaption></figure>' for n in (16, 32)) + '</div></div>'
      f'<div class="x-fav" style="margin-top:24px"><div><div class="x-tab"><div class="t"><img src="{FAVPNG(16)}" alt=""/>Drops · Hypedrive</div></div><div class="x-tab bar"><span>hypedrive.app/drops</span></div></div>'
      f'<div><div class="x-tab dk"><div class="t"><img src="{FAVPNG(16)}" alt=""/>Drops · Hypedrive</div></div><div class="x-tab dk bar"><span>hypedrive.app/drops</span></div></div></div>'
      + rules_inl([("16 px: faces only", "Marigold, Cobalt and Vermilion, with no tape. Anything finer turns to mud."), ("32 and 48 px", "Thicker tape, no dot."), ("Same file, both themes", "The favicon sits on any browser chrome, light or dark, without a tile.")], 3, 22)),
]

# ============================================================== EXPANSION 3: colour in use
xcss("""
.x-comp3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; } .x-comp3 figure { margin: 0; }
.x-mc { height: 440px; border-radius: 22px; overflow: hidden; position: relative; font-family: var(--hd-font-ui); border: 1px solid ${i200}; }
.x-prop { display: flex; height: 14px; border-radius: 7px; overflow: hidden; margin-top: 14px; box-shadow: 0 0 0 1px ${i200}; } .x-prop i { display: block; }
.x-comp3 figcaption { font-family: var(--hd-font-ui); font-size: 15px; line-height: 1.45; color: ${i700}; margin-top: 10px; } .x-comp3 figcaption b { display: block; font-size: 17px; color: ${ink}; }
.x-btn { display: inline-flex; align-items: center; justify-content: center; height: 44px; padding: 0 20px; border-radius: 12px; font: 560 16px var(--hd-font-ui); background: ${c600}; color: #fff; box-shadow: inset 0 0 0 1px ${c800}; } .x-btn.grey { background: #fff; color: ${ink}; box-shadow: inset 0 0 0 1px ${i300}; }
.x-btn.ver { background: ${v600}; box-shadow: inset 0 0 0 1px ${v800}; } .x-btn.mar { background: ${mar}; color: ${ink}; box-shadow: none; }
.x-bdg { display: inline-flex; align-items: center; height: 24px; padding: 0 9px; border-radius: 6px; font: 600 14px var(--hd-font-ui); color: #fff; } .x-bdg.live { background: ${n50}; color: ${n800}; gap: 6px; } .x-bdg.live::before { content: ''; width: 14px; height: 14px; background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 14 14'%3E%3Ccircle cx='7' cy='7' r='7' fill='${n600u}'/%3E%3Cpath d='M4 7.2l2 2 4-4.4' fill='none' stroke='white' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/14px no-repeat; }
.x-rowc { display: flex; align-items: center; gap: 12px; background: #fff; border: 1px solid ${i200}; border-radius: 16px; padding: 10px 14px 10px 10px; } .x-rowc img.p { width: 56px; height: 56px; border-radius: 10px; object-fit: cover; }
.x-rowc b { font: 600 16px var(--hd-font-ui); display: block; color: ${ink}; } .x-rowc small { font: 15px var(--hd-font-ui); color: ${i600}; display: block; margin-top: 2px; }
.x-dd { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; } .x-dd > div { display: flex; flex-direction: column; gap: 10px; } .x-dd .mini { height: 214px; border-radius: 18px; padding: 18px; font-family: var(--hd-font-ui); position: relative; overflow: hidden; border: 1px solid ${i200}; display: flex; flex-direction: column; justify-content: center; gap: 12px; background: #fff; }
.x-dd .cap2 { font-family: var(--hd-font-ui); font-size: 15px; line-height: 1.4; color: ${i700}; margin: 0; } .x-dd h4 { margin: 0 0 2px; font-size: 22px; font-variation-settings: 'opsz' 32; }
.x-data { display: grid; grid-template-columns: 330px 1fr; gap: 36px; } .x-ord { display: flex; flex-direction: column; gap: 10px; } .x-ord > div { display: grid; grid-template-columns: 44px 1fr; column-gap: 14px; align-items: center; } .x-ord i { grid-row: span 2; width: 44px; height: 44px; border-radius: 10px; display: block; }
.x-ord b { font: 600 16px var(--hd-font-ui); } .x-ord span { font: 15px var(--hd-font-ui); color: ${i600}; }
.x-ch2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; } .x-ch { border: 1px solid ${i200}; border-radius: 20px; padding: 18px 20px 14px; } .x-ch h4 { margin: 0 0 6px; font: 650 19px var(--hd-font-display); font-variation-settings: 'opsz' 24; }
.x-th .bal { display: flex; align-items: flex-start; justify-content: space-between; } .x-th .bal small { display: block; font-size: 14px; color: ${i300}; margin-top: 6px; } .x-th .b1.s { height: 36px; padding: 0 16px; font-size: 15px; flex: none; } .x-th .ern { background: var(--hd-surface); border: 1px solid var(--hd-border); border-radius: 16px; padding: 12px 14px; display: flex; align-items: center; gap: 10px; } .x-th .ern span { white-space: nowrap; font-size: 14px; color: var(--hd-fg-muted); display: block; } .x-th .ern b { font: 700 24px var(--hd-font-display); letter-spacing: -.02em; } .x-th .ern em { font-style: normal; font-weight: 600; font-size: 15px; color: var(--hd-success); } .x-th .ern svg { margin-left: auto; } .x-th .act { display: flex; justify-content: space-between; align-items: baseline; margin-top: 8px; } .x-th .act b { font: 700 18px var(--hd-font-ui); letter-spacing: -.02em; } .x-th .act span { font-size: 15px; font-weight: 600; color: var(--hd-link); }
.x-th2 { display: grid; grid-template-columns: 720px 1fr; gap: 36px; } .x-ths { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.x-th { border-radius: 24px; padding: 16px; height: 560px; background: var(--hd-canvas); color: var(--hd-fg); font-family: var(--hd-font-ui); border: 1px solid ${i200}; display: flex; flex-direction: column; gap: 10px; }
.x-th h4 { font: 650 26px var(--hd-font-display); margin: 6px 6px 4px; font-variation-settings: 'opsz' 32; letter-spacing: -.02em; } .x-th .bal { background: ${i900}; color: #fff; border-radius: 16px; padding: 18px; } .x-th .bal span { font-size: 15px; color: ${i300}; display: block; } .x-th .bal b { font: 700 40px var(--hd-font-display); letter-spacing: -.02em; font-variant-numeric: tabular-nums; }
.x-th .rw { background: var(--hd-surface); border: 1px solid var(--hd-border); border-radius: 16px; padding: 10px; display: flex; align-items: center; gap: 10px; } .x-th .rw img { width: 48px; height: 48px; border-radius: 9px; object-fit: cover; } .x-th .rw b { font-size: 15px; display: block; } .x-th .rw small { font-size: 15px; color: var(--hd-fg-muted); } .x-th .rw em { white-space: nowrap; margin-left: auto; font-style: normal; font-weight: 600; font-size: 16px; color: var(--hd-success); font-variant-numeric: tabular-nums; }
.x-th .b1 { background: var(--hd-accent); color: var(--hd-accent-fg); border-radius: 12px; height: 44px; display: flex; align-items: center; justify-content: center; font-weight: 560; font-size: 16px; } .x-th .b2 { background: var(--hd-surface); box-shadow: inset 0 0 0 1px var(--hd-border-strong); color: var(--hd-fg); border-radius: 12px; height: 44px; display: flex; align-items: center; justify-content: center; font-weight: 560; font-size: 16px; }
.x-th .nt { background: var(--hd-warning-subtle); color: var(--hd-warning-strong); border-radius: 12px; padding: 10px 12px; font-size: 15px; line-height: 1.4; }
.x-roles { width: 100%; border-collapse: collapse; font-family: var(--hd-font-ui); } .x-roles th { text-align: left; font-size: 15px; font-weight: 600; color: ${i600}; padding: 0 0 8px; border-bottom: 2px solid ${ink}; } .x-roles td { padding: 7px 0; border-bottom: 1px solid ${i200}; font-size: 15px; } .x-roles td:first-child { font-weight: 600; font-size: 16px; }
.x-roles i { display: inline-block; width: 18px; height: 18px; border-radius: 5px; vertical-align: -4px; margin-right: 8px; border: 1px solid ${i300}; } .x-roles td.h { font-family: 'Geist Mono', monospace; color: ${i700}; font-size: 15px; }
""")
def prop_bar(parts):
    """parts: (colour, pct, name). A stacked proportion bar plus a legend line."""
    bar = "".join(f'<i style="width:{p}%;background:{c}"></i>' for c, p, n in parts)
    return f'<div class="x-prop">{bar}</div>'
def mcomp(inner_html, parts, title, note):
    return f'<figure><div class="x-mc" style="{inner_html[0]}">{inner_html[1]}</div>{prop_bar(parts)}<figcaption><b>{title}</b>{note}</figcaption></figure>'
_ui = ("background:#fff;padding:26px 22px", f'<div style="display:flex;align-items:center;gap:10px">{img(MARK_L, "width:30px")}<b style="font:650 26px var(--hd-font-display);font-variation-settings:\'opsz\' 32;letter-spacing:-.02em;color:{INK}">Your drops</b></div>'
       f'<div style="margin-top:22px;display:flex;flex-direction:column;gap:10px"><div class="x-rowc">{ph_img("p6.jpg", "", 200, (0.1, 0, 0.7, 1), "p")}<div><b>Glow serum, 30 ml</b><small>Lumen Labs · ends Friday</small></div><span class="x-bdg live" style="margin-left:auto">Live</span></div>'
       f'<div class="x-rowc">{ph_img("p7.jpg", "", 200, (0.1, 0, 0.7, 1), "p")}<div><b>Hair and scalp set</b><small>Zoomi · 48 reviews</small></div><span class="x-bdg live" style="margin-left:auto">Live</span></div>'
       f'<div class="x-rowc">{ph_img("p5.jpg", "", 200, (0, 0.25, 1, 0.75), "p")}<div><b>Barrier cream</b><small>Slots full</small></div></div></div>'
       f'<div style="margin-top:22px;display:flex;gap:10px"><span class="x-btn">Apply for this drop</span><span class="x-btn grey">Save</span></div>')
_poster = (f"background:{INK};padding:34px 30px", f'<div style="position:absolute;right:-10px;bottom:-10px;width:300px">{ill_img("parcel", "dark", "width:300px")}</div>'
           f'<div style="font:700 56px/1.02 var(--hd-font-display);font-variation-settings:\'opsz\' 96;letter-spacing:-.025em;color:#fff;margin-top:6px">Products in.<br><span style="color:{BRAND["marigold"]}">Hype out.</span></div>'
           f'<p style="font:18px/1.4 var(--hd-font-ui);color:{I[300]};margin:18px 0 0;max-width:215px">Try it first. Say it straight. Get paid.</p><div style="margin-top:22px"><span class="x-btn">Join a drop</span></div>')
_chart_bars = "".join(f'<rect x="{30 + i*52}" y="{150 - h}" width="34" height="{h}" rx="4" fill="{(V[500] if i == 4 else C[500])}"/>' for i, h in enumerate([34, 52, 46, 70, 98, 80]))
_stat = ("background:#fff;padding:24px 22px", f'<div style="display:flex;justify-content:space-between;font:600 16px var(--hd-font-ui);color:{I[600]}"><span>Reviews per week</span><span></span></div>'
         f'<div style="font:700 50px/1.05 var(--hd-font-display);font-variation-settings:\'opsz\' 72;letter-spacing:-.02em;color:{INK};margin:8px 0 12px;font-variant-numeric:tabular-nums">248</div>'
         f'<svg viewBox="0 0 340 170" width="100%" aria-label="Weekly bars">{"".join(f"<line x1=0 x2=340 y1={y} y2={y} stroke={I[100]} />" for y in (30, 90, 150))}{_chart_bars}'
         + "".join(f'<text x="{47 + i*52}" y="168" text-anchor="middle" font-family="Geist" font-size="14" fill="{I[600]}">W{i+1}</text>' for i in range(6)) + '</svg>'
         f'<p style="font:15px/1.4 var(--hd-font-ui);color:{I[600]};margin:14px 0 0">Cobalt for the series, one Vermilion bar for the week to look at.</p>')
def svg_stacked():
    wks = ["W1", "W2", "W3", "W4", "W5"]; data = [(30, 14, 8), (36, 16, 10), (34, 22, 12), (44, 20, 14), (52, 26, 16)]
    base = 300; k = 3.0
    out = [f'<line x1="0" x2="440" y1="{y}" y2="{y}" stroke="{I[100]}"/>' for y in (base - 90, base - 180, base - 270)] + [f'<line x1="0" x2="440" y1="{base}" y2="{base}" stroke="{I[200]}"/>']
    cols = [C[500], V[500], M[300]]
    for i, d in enumerate(data):
        y = base
        for kk, v in enumerate(d):
            h = v*k; out.append(f'<rect x="{18 + i*70}" y="{y - h:.1f}" width="46" height="{h:.1f}" rx="3" fill="{cols[kk]}" stroke="#fff" stroke-width="2"/>'); y -= h
        out.append(f'<text x="{41 + i*70}" y="{base + 28}" text-anchor="middle" font-family="Geist" font-size="15" fill="{I[600]}">{wks[i]}</text>')
    for kk, (t, c) in enumerate([("Instagram", C[700]), ("YouTube", V[700]), ("Other", M[800])]):
        out.append(f'<text x="372" y="{base - 40 - kk*80}" font-family="Geist" font-size="15" font-weight="600" fill="{c}">{t}</text>')
    return f'<svg viewBox="0 0 470 {base + 40}" width="100%" role="img" aria-label="Stacked bars, illustrative data">{"".join(out)}</svg>'
def svg_lines():
    a = [30, 52, 48, 80, 96, 130]; b = [34, 40, 58, 62, 76, 84]; base = 300; k = 1.9
    pts = lambda arr: " ".join(f"{20 + i*66},{base - v*k:.1f}" for i, v in enumerate(arr))
    out = [f'<line x1="0" x2="440" y1="{y}" y2="{y}" stroke="{I[100]}"/>' for y in (base - 90, base - 180, base - 270)] + [f'<line x1="0" x2="440" y1="{base}" y2="{base}" stroke="{I[200]}"/>']
    out.append(f'<polyline points="{pts(b)}" fill="none" stroke="{I[400]}" stroke-width="3" stroke-dasharray="7 6" stroke-linecap="round"/>')
    out.append(f'<polyline points="{pts(a)}" fill="none" stroke="{C[500]}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>')
    out.append(f'<circle cx="{20 + 5*66}" cy="{base - a[5]*k:.1f}" r="8" fill="{V[500]}" stroke="#fff" stroke-width="3"/>')
    out.append(f'<text x="{20 + 5*66 - 12}" y="{base - a[5]*k - 6:.1f}" text-anchor="end" font-family="Geist" font-size="15" font-weight="600" fill="{C[700]}">This month</text>')
    out.append(f'<text x="{20 + 5*66}" y="{base - b[5]*k + 34:.1f}" text-anchor="end" font-family="Geist" font-size="15" font-weight="600" fill="{I[600]}">Last month</text>')
    for i in range(6): out.append(f'<text x="{20 + i*66}" y="{base + 28}" text-anchor="middle" font-family="Geist" font-size="15" fill="{I[600]}">W{i+1}</text>')
    return f'<svg viewBox="0 0 470 {base + 40}" width="100%" role="img" aria-label="Line chart, illustrative data">{"".join(out)}</svg>'
def _dd(title, do_html, do_tag, no_html, no_tag):
    return (f'<div class="x-ddc"><h4>{title}</h4><div class="x-spec2">{do_html}</div>{do_tag}<div class="x-spec2">{no_html}</div>{no_tag}</div>')
xcss("""
.x-dd2 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; } .x-ddc h4 { margin: 0 0 14px; font-size: 22px; letter-spacing: -.03em; }
.x-spec2 { height: 190px; border-radius: 18px; background: #fff; box-shadow: inset 0 0 0 1px #e8e8eb; display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap; align-content: center; padding: 0 22px; margin-bottom: 12px; } .x-ddc .xtag { margin-bottom: 26px; min-height: 40px; }
.x-chip { display: inline-flex; align-items: center; height: 30px; padding: 0 14px; border-radius: 8px; font: 600 15px var(--hd-font-ui); width: 120px; justify-content: center; } .x-spec2 .x-chip[style*="width"] { width: auto; }
.x-ratio { font: 400 15px/1.4 var(--hd-font-ui); color: ${i600}; } .x-ratio b { color: ${ink}; font-weight: 650; font-variant-numeric: tabular-nums; }
.x-mq { display: flex; align-items: center; gap: 10px; width: 100%; padding: 10px 14px; border-radius: 12px; box-shadow: inset 0 0 0 1px #e8e8eb; } .x-mq b { font: 600 15px var(--hd-font-ui); } .x-mq small { margin-left: auto; font: 500 14px var(--hd-font-ui); color: ${i600}; } .x-mq.loud { flex-wrap: wrap; justify-content: flex-start; } .x-mq.loud .x-chip { width: auto; height: 26px; padding: 0 10px; }
""")
def _short(t): return t.replace(", ui-sans-serif, system-ui, sans-serif", ", …").replace(", ui-monospace, SFMono-Regular, monospace", ", …").replace(", ui-monospace, SFMono-Regular, monospace;", ", …;")
PG_COLOR = [
 page(head("00", "Colour in use", "Paper and Ink do most of the work. Cobalt marks the one thing to do next. Accents appear once, where the eye should land.") +
      '<div class="x-comp3">'
      + mcomp(_ui, [("#fff", 74, "Paper"), (INK, 13, "Ink"), (COB, 8, "Cobalt"), (N[700], 3, "Mint"), (I[200], 2, "Grey")], "Product screen: Paper-led", "Paper 74 · Ink 13 · Cobalt 8 · Mint 3 · Grey 2. One Cobalt button, one white.").replace('<div class="x-prop">', f'<div class="x-prop" style="box-shadow:0 0 0 1px {I[200]}">')
      + mcomp(_poster, [(INK, 70, "Ink"), ("#fff", 14, "Paper"), (BRAND["marigold"], 7, "Marigold"), (COB, 6, "Cobalt"), (BRAND["vermilion"], 3, "Vermilion")], "Poster: Ink-led", "Ink 70 · Paper 14 · Marigold 7 · Cobalt 6 · Vermilion 3. The parcel carries the colour.")
      + mcomp(_stat, [("#fff", 78, "Paper"), (INK, 8, "Ink"), (C[500], 8, "Cobalt"), (V[500], 2, "Vermilion"), (I[100], 4, "Grey")], "Data card: Paper-led", "Paper 78 · Ink 8 · Cobalt 8 · Grey 4 · Vermilion 2. One highlight, never two.").replace('<div class="x-prop">', f'<div class="x-prop" style="box-shadow:0 0 0 1px {I[200]}">')
      + '</div><p class="x-note" style="margin-top:18px">Shares are approximate, measured by eye on each composition. The pattern holds: neutrals first, one Cobalt action, accents in the single digits.</p>'),
 page(head("00", "Colour, do and don’t", "Three rules that break most often, shown as the compositions they ruin.") +
      '<div class="x-dd2">'
      + _dd("One main action", f'<span class="x-btn">Send application</span><span class="x-btn grey">Save for later</span>', tag_do("Do: one Cobalt button, the rest white"),
            f'<span class="x-btn">Send</span><span class="x-btn ver">Save</span><span class="x-btn mar">Share</span>', tag_no("Don’t: three colours competing for the click"))
      + _dd("Text on Marigold", f'<span class="x-chip" style="background:{BRAND["marigold"]};color:{INK}">Live now</span><span class="x-ratio">Ink on Marigold<br><b>{contrast(INK, BRAND["marigold"]):.1f}:1</b> · AAA</span>', tag_do("Do: Ink text on Marigold"),
            f'<span class="x-chip" style="background:{BRAND["marigold"]};color:#fff">Live now</span><span class="x-ratio">Paper on Marigold<br><b>{contrast("#ffffff", BRAND["marigold"]):.1f}:1</b> · Fail</span>', tag_no("Don’t: Paper text on Marigold"))
      + _dd("Accents, sparingly", f'<div class="x-mq"><b>Instagram link</b><small style="color:{V[700]}">Link not public</small></div><div class="x-mq"><b>YouTube link</b><small>Checked</small></div>', tag_do("Do: one Vermilion note, where it matters"),
            f'<div class="x-mq loud"><b>Instagram link</b><span class="x-chip" style="background:{COB};color:#fff">Live</span><span class="x-chip" style="background:{BRAND["vermilion"]};color:#fff">Fix</span><span class="x-chip" style="background:{BRAND["marigold"]};color:{INK}">New</span><span class="x-chip" style="background:{N[500]};color:#fff">OK</span></div>', tag_no("Don’t: every accent at full strength at once"))
      + '</div>'),
 page(head("00", "Colour in data", "Series take colours in a fixed order, are labelled on the chart, and never rely on colour alone.") +
      '<div class="x-data"><div><h3>The order</h3><div class="x-ord">'
      + "".join(f'<div><i style="background:{h}"></i><b>{i+1}. {n}</b><span>{u}</span></div>' for i, (n, h, u) in enumerate([("Cobalt 500", C[500], "The main series"), ("Vermilion 500", V[500], "The highlight, or the second series"), ("Marigold 300", M[300], "Third series"), ("Mint 500", N[500], "Fourth series"), ("Ink 400", I[400], "Everything else, and comparisons")]))
      + f'</div><h3 style="margin-top:20px">Sequential</h3><div class="seq" style="margin-top:6px">' + "".join(f'<i style="background:{C[k]}"></i>' for k in (100, 200, 300, 400, 500, 600, 700, 800)) + '</div><p class="x-note" style="margin-top:8px">One hue, light to dark, for counts and density.</p></div>'
      f'<div><div class="x-ch2"><div class="x-ch"><h4>Reviews by platform, per week</h4>{svg_stacked()}</div><div class="x-ch"><h4>Earnings, this month and last</h4>{svg_lines()}</div></div>'
      + rules_inl([("Five at most", "Past five series, group the rest as Other in Ink 400 or change the chart."), ("Label on the chart", "Names sit at the end of the line or bar, in Geist 15. A legend alone is a last resort."), ("Colour is never the only signal", "Direct labels, dashes and position carry the meaning too.")], 3, 20) + '</div></div>'),
]
def theme_panel(theme):
    spark = '<svg viewBox="0 0 120 36" width="84" height="26"><path d="M2 30 C20 28 30 22 50 20 S86 14 112 6" fill="none" stroke="var(--hd-accent)" stroke-width="2" stroke-linecap="round"/><circle cx="112" cy="6" r="4" fill="var(--hd-accent)"/></svg>'
    return (f'<div class="x-th" data-theme="{theme}"><h4>Wallet</h4>'
            f'<div class="bal"><div><span>Available</span><b>₹6,820</b><small>₹990 held · next payout Tue, Nov 24</small></div><div class="b1 s">Withdraw</div></div>'
            f'<div class="ern"><div><span>Earned this month</span><b>₹8,460</b></div>{spark}<em>+24%</em></div>'
            f'<div class="act"><b>Activity</b><span>See all</span></div>'
            f'<div class="rw">{ph_img("p6.jpg", "", 160, (0.1, 0, 0.7, 1))}<div><b>Glow serum</b><small>Approved · Nov 18</small></div><em>+₹640</em></div>'
            f'<div class="rw">{ph_img("p7.jpg", "", 160, (0.1, 0, 0.7, 1))}<div><b>Hair and scalp set</b><small>Approved · Nov 11</small></div><em>+₹480</em></div></div>')
ROLE_ROWS = [("canvas", "Page background"), ("surface", "Cards and rows"), ("fg", "Text"), ("fg-muted", "Secondary text"), ("accent", "Primary action"),
             ("link", "Links"), ("focus", "Focus ring"), ("success", "Success text"), ("danger", "Danger text"), ("border-strong", "Secondary button edge")]
PG_COLOR.append(
 page(head("00", "Light and dark surfaces", "The same screen on two surfaces. Roles keep their meaning; only the values move. Cobalt stays the action colour in both.") +
      f'<div class="x-th2"><div class="x-ths">{theme_panel("light")}{theme_panel("dark")}</div>'
      f'<table class="x-roles"><tr><th>Role</th><th>Light</th><th>Dark</th></tr>'
      + "".join(f'<tr><td>{n}<br><span style="font-weight:400;color:{I[600]};font-size:15px">{u}</span></td><td class="h"><i style="background:{SEM_L[n]}"></i>{SEM_L[n]}</td><td class="h"><i style="background:{SEM_D[n]}"></i>{SEM_D[n]}</td></tr>' for n, u in ROLE_ROWS) + '</table></div>'))

# ============================================================== EXPANSION 4: typography in use
xcss("""
.x-tu { display: grid; grid-template-columns: 1.15fr 1fr; gap: 28px; align-items: start; }
.x-mk { background: ${ink}; border-radius: 24px; padding: 40px 44px 36px; height: 470px; color: #fff; position: relative; overflow: hidden; }
.x-mk h5 { margin: 0; font: 700 78px/0.98 var(--hd-font-display); font-variation-settings: 'opsz' 96; letter-spacing: -.025em; } .x-mk h5 span { color: ${mar}; }
.x-mk p { font: 20px/1.5 var(--hd-font-ui); color: ${i300}; margin: 26px 0 28px; max-width: 520px; text-wrap: pretty; }
.x-ui { zoom: 1.3; background: #fff; border: 1px solid ${i200}; border-radius: 16px; padding: 18px; font-family: var(--hd-font-ui); height: 360px; }
.x-ui .ph { width: 100%; height: 126px; border-radius: 12px; object-fit: cover; display: block; }
.x-ui h6 { font: 650 24px/30px var(--hd-font-display); font-variation-settings: 'opsz' 48; letter-spacing: -.024em; margin: 14px 0 2px; } .x-ui .s { font-size: 13px; line-height: 18px; color: ${i600}; margin: 0; }
.x-ui .b { font-size: 15px; line-height: 22px; color: ${i800}; margin: 10px 0 14px; letter-spacing: -.006em; } .x-ui .row { display: flex; align-items: center; justify-content: space-between; } .x-ui .amt { font: 650 19px/25px var(--hd-font-display); font-variation-settings: 'opsz' 32; font-variant-numeric: tabular-nums; }
.x-spec { margin-top: 16px; display: grid; grid-template-columns: 1fr 1fr; gap: 6px 28px; } .x-spec div { border-top: 1px solid ${i200}; padding: 8px 0 0; font: 15px/1.4 var(--hd-font-ui); color: ${i600}; } .x-spec b { color: ${ink}; display: block; font-size: 16px; }
.x-num { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; } .x-n { background: ${i50}; border-radius: 20px; padding: 22px 24px 20px; display: flex; flex-direction: column; gap: 4px; }
.x-n h4 { margin: 0 0 4px; font-size: 21px; font-variation-settings: 'opsz' 32; } .x-n .v { font: 650 36px/1.15 var(--hd-font-ui); letter-spacing: -.02em; font-variant-numeric: tabular-nums; color: ${ink}; } .x-n .v.x { color: ${i500}; text-decoration: line-through; text-decoration-color: ${v500}; text-decoration-thickness: 2px; } .x-n .xtag { margin: 6px 0 0; font-size: 15px; }
.x-n .why { font: 15px/1.4 var(--hd-font-ui); color: ${i600}; margin: 6px 0 0; } .x-n .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; } .x-n .tab { font: 650 26px/1.3 var(--hd-font-ui); text-align: right; color: ${ink}; }
.x-lm { display: grid; grid-template-columns: 290px 450px 1fr; gap: 36px; align-items: start; } .x-lm figure { margin: 0; } .x-lm p.t { font: 17px/1.55 var(--hd-font-ui); color: ${i800}; margin: 0; } .x-lm figcaption { margin-top: 12px; border-top: 3px solid ${ink}; padding-top: 8px; font: 15px/1.4 var(--hd-font-ui); color: ${i600}; } .x-lm figcaption b { display: block; font-size: 16px; color: ${ink}; }
.x-rag { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; margin-top: 26px; } .x-rag h5 { margin: 0 0 8px; font: 650 40px/1.1 var(--hd-font-display); font-variation-settings: 'opsz' 48; letter-spacing: -.02em; } .x-rag > div { border-top: 3px solid ${ink}; padding-top: 14px; }
.x-rag small { display: block; font: 15px/1.4 var(--hd-font-ui); color: ${i600}; margin-top: 8px; }
""")
_lm_text = ("Creators get the product, try it for real, and tell their people what they think. Brands see honest reviews instead of paid promises. "
            "Payouts are shown before anyone applies, and they land within 48 hours of approval. Nobody has to chase anyone for money.")
PG_TYPE2 = [
 page(head("00", "Type in use", "The same two voices, set for two jobs. Bricolage leads at display sizes; Geist carries every sentence that has to be read.") +
      f'<div class="x-tu"><div><div class="x-mk"><h5>Try it first.<br><span>Say it straight.</span></h5><p>Hypedrive sends real products to creators. They try them, review them honestly, and get paid within 48 hours of approval.</p><span class="x-btn">See how it works</span></div>'
      f'<div class="x-spec"><div><b>Headline</b>Display · Bricolage 650 · opsz 96 · 72/76 · −0.02em</div><div><b>Body</b>Body L · Geist 400 · 18/28 · 55–65 characters a line</div></div></div>'
      f'<div><div class="x-ui">{ph_img("p6.jpg", "", 700, (0, 0.05, 1, 0.8), "ph")}<h6>Glow serum, 30 ml</h6><p class="s">Lumen Labs · 120 creators · ends Friday</p>'
      f'<p class="b">A light vitamin C serum. Use it for a week, then tell your people how it went.</p><div class="row"><span class="amt">₹1,240</span><span class="x-btn" style="height:40px;font-size:15px">Apply for this drop</span></div></div>'
      f'<div class="x-spec"><div><b>Title and amount</b>Title 1 24 and Title 2 19 · Bricolage 650</div><div><b>Body and meta</b>Body 15/22 and Small 13/18 · Geist 400<br>Shown here at 130%</div></div></div></div>'),
 page(head("00", "Numerals and rupees", "Money is the most-read thing in the product. Write it the Indian way, and set it so columns line up.") +
      '<div class="x-num">'
      f'<div class="x-n"><h4>No space after ₹</h4><div class="v">₹1,240</div>{tag_do("Do")}<div class="v x">₹ 1,240</div><div class="v x">Rs. 1240</div>{tag_no("Don’t")}</div>'
      f'<div class="x-n"><h4>Indian digit grouping</h4><div class="v">₹1,04,160</div><div class="v">₹12,50,000</div>{tag_do("Do")}<div class="v x">₹104,160</div>{tag_no("Don’t")}<p class="why">The last three digits, then pairs.</p></div>'
      f'<div class="x-n"><h4>A real minus sign</h4><div class="v">−₹2,400</div>{tag_do("Do: U+2212")}<div class="v x">-₹2,400</div>{tag_no("Don’t: a hyphen")}<p class="why">The minus is as wide as the plus and sits at the same height.</p></div>'
      f'<div class="x-n"><h4>Tabular figures in columns</h4><div class="cols"><div><div class="tab" style="font-variant-numeric:tabular-nums">₹11,111<br>₹88,888<br>₹10,101</div>{tag_do("Do: tabular")}</div>'
      f'<div><div class="tab" style="font-variant-numeric:proportional-nums;color:{I[500]}">₹11,111<br>₹88,888<br>₹10,101</div>{tag_no("Don’t: proportional")}</div></div></div>'
      f'<div class="x-n"><h4>Ranges</h4><div class="v">₹900–1,500</div>{tag_do("Do: en dash, one ₹")}<div class="v x">₹900 - ₹1,500</div>{tag_no("Don’t")}<p class="why">From the product: “Creators in your category earn ₹900–1,500.”</p></div>'
      f'<div class="x-n"><h4>Which face</h4><div class="v" style="font-family:var(--hd-font-display);font-weight:700;font-variation-settings:\'opsz\' 72;font-size:44px">₹12,480</div><p class="why" style="margin:0">Hero amounts: Bricolage 700.</p><div class="v" style="font-size:28px">₹1,240 · 120 creators</div><p class="why" style="margin:0">Rows and tables: Geist, tabular.</p><div class="v" style="font-family:var(--hd-font-mono);font-size:26px;font-weight:450">4471 2280</div><p class="why" style="margin:0">IDs and tracking: Geist Mono.</p></div>'
      '</div>'),
 page(head("00", "Line length and rag", "Readability is mostly measure. Aim for 55 to 65 characters a line, and let headlines break where the sense breaks.") +
      f'<div class="x-lm"><figure><p class="t" style="max-width:250px">{_lm_text}</p><figcaption><b>Too narrow · about 30</b>Eyes jump every few words and the rag turns ragged.</figcaption></figure>'
      f'<figure><p class="t" style="max-width:450px">{_lm_text}</p><figcaption><b>Right · 55 to 65</b>Body text in the product and in this book.</figcaption></figure>'
      f'<figure><p class="t" style="max-width:100%;font-size:17px">{_lm_text}</p><figcaption><b>Too wide · about 80</b>Past 75 the eye loses its place on the way back.</figcaption></figure></div>'
      f'<div class="x-rag"><div><h5 style="text-wrap:balance;max-width:560px">Honest reviews, paid within 48 hours of approval</h5><small>Headlines: <code>text-wrap: balance</code>. Two even lines, never one long line and a stray word.</small></div>'
      f'<div><h5 style="text-wrap:wrap;max-width:100%;font-size:40px">Honest reviews, paid within 48 hours of approval</h5><small>Unbalanced. The line breaks where it runs out of room, not where the sense does.</small></div></div>'
      + rules_inl([("Body", "Left-aligned, never justified. <code>text-wrap: pretty</code> so no line ends on a single short word."), ("No hyphenation", "Break the sentence, not the word."), ("Line height", "1.5 for body, 1.1 to 1.2 for headlines.")], 3, 22)),
]

# ============================================================== EXPANSION 5: iconography (real Nucleo glyphs, names read from uikit.NMAP)
import ast as _ast
_uik = _ast.parse(open("/tmp/hdwm/uikit.py").read())
def _lit(name):
    for n in _uik.body:
        if isinstance(n, _ast.Assign) and getattr(n.targets[0], "id", None) == name: return _ast.literal_eval(n.value)
NMAP = _lit("NMAP"); STATUS = _lit("STATUS")
NSJ = json.load(open("/tmp/hdwm/nucleo_outline.json")); NFJ = json.load(open("/tmp/hdwm/nucleo_fill.json"))
FILLM = {k: v + "Fill18" for k, v in NMAP.items() if v + "Fill18" in NFJ}; FILLM.update({k: v + "Fill18" for k, v in STATUS.items()})
def io(name, size=28, color="currentColor"):
    body = NSJ[NMAP[name] + "Outline18"]
    return f'<svg width="{size}" height="{size}" viewBox="0 0 18 18" stroke-width="1.5" style="color:{color}" aria-hidden="true">{body}</svg>'
def isolid(name, size=24, color="currentColor"):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 18 18" fill="currentColor" style="color:{color}" aria-hidden="true">{NFJ[FILLM[name]]}</svg>'
xcss("""
.x-ic1 { display: grid; grid-template-columns: 430px 1fr; gap: 44px; align-items: start; } .x-icbig { background: ${i50}; border-radius: 24px; padding: 28px; }
.x-icbig .cv { display: block; margin: 0 auto; } .x-icbig p { font: 15px/1.45 var(--hd-font-ui); color: ${i600}; margin: 14px 0 0; }
.x-st { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; } .x-st > div { border: 1px solid ${i200}; border-radius: 18px; padding: 18px 20px 16px; } .x-st h4 { margin: 0 0 12px; font: 650 19px var(--hd-font-display); font-variation-settings: 'opsz' 24; }
.x-tbar { display: grid; grid-template-columns: repeat(4, 1fr); } .x-tbar div { display: flex; flex-direction: column; align-items: center; gap: 4px; font: 15px var(--hd-font-ui); color: ${i500}; } .x-tbar div.on { color: ${c700}; font-weight: 600; }
.x-trow { display: flex; gap: 22px; border-bottom: 1px solid ${i200}; font: 560 16px var(--hd-font-ui); color: ${i600}; } .x-trow span { display: flex; align-items: center; gap: 7px; padding: 0 0 12px; } .x-trow span.on { color: ${ink}; box-shadow: inset 0 -3px 0 ${c600}; }
.x-igrid { display: grid; grid-template-columns: repeat(10, 1fr); gap: 8px 6px; } .x-igrid div { display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 14px 0 10px; border-radius: 14px; background: ${i50}; font: 15px var(--hd-font-ui); color: ${i700}; } .x-igrid svg { color: ${ink}; }
.x-twins { display: grid; grid-template-columns: 1fr 380px; gap: 40px; } .x-tw { display: grid; grid-template-columns: repeat(6, 1fr); gap: 12px; } .x-tw > div { background: ${i50}; border-radius: 16px; padding: 22px 0 16px; display: flex; flex-direction: column; align-items: center; gap: 12px; font: 15px var(--hd-font-ui); color: ${i700}; } .x-tw .pr { display: flex; flex-direction: column; align-items: center; gap: 14px; }
.x-mean { width: 100%; border-collapse: collapse; font-family: var(--hd-font-ui); } .x-mean td { padding: 9px 0; border-bottom: 1px solid ${i200}; font-size: 16px; vertical-align: middle; } .x-mean svg { display: block; } .x-mean td:first-child { width: 44px; } .x-mean td:last-child { color: ${i600}; font-size: 15px; text-align: right; }
""")
def tgl(name_a, name_b, size=24): return io(name_a, size)
ICON_GRID = ["home", "search", "box", "wallet", "user", "users", "bell", "camera", "upload", "download",
             "filter", "sliders", "arrow", "back", "chev", "down", "plus", "check", "x", "star",
             "heart", "share", "settings", "chart", "trend", "truck", "fast", "clock", "calendar", "tag",
             "link", "linkbroken", "more", "info", "alert", "lock", "privacy", "bag", "gift", "eye",
             "mail", "send", "phone", "rupee", "receipt", "bank", "payouts", "overview", "list", "grid",
             "help", "copy", "edit", "trash", "logout", "login", "ok", "bolt", "play", "pause", "drop", "shirt"]
ICON_GRID = [k for k in ICON_GRID if k in NMAP and NMAP[k] + "Outline18" in NSJ][:60]
TWINS = [k for k in ["home", "box", "users", "overview", "payouts", "foryou", "bell", "wallet", "star", "heart", "user", "bag", "gift", "search", "settings", "clock", "mail", "lock"] if k in FILLM][:12]
def _constr():
    g = "".join(f'<line x1="{i*20}" y1="0" x2="{i*20}" y2="360" stroke="{C[200]}" stroke-width="1"/><line x1="0" y1="{i*20}" x2="360" y2="{i*20}" stroke="{C[200]}" stroke-width="1"/>' for i in range(19))
    keyl = ""
    ico = f'<g transform="scale(20)" stroke-width="1.5" style="color:{INK}">{NSJ[NMAP["box"] + "Outline18"]}</g>'
    return f'<svg class="cv" viewBox="0 0 360 360" width="360" height="360" role="img" aria-label="Box icon on its 18 pixel grid"><rect width="360" height="360" fill="#fff"/>{g}{keyl}{ico}</svg>'
PG_ICONS = [
 page(head("00", "The icon system", "Nucleo UI: an outline for idle, and its exact solid twin for active and selected. Both drawn on an 18 pixel grid.") +
      f'<div class="x-ic1"><div class="x-icbig">{_constr()}<p>Drawn on an 18 px grid with a 1.5 px stroke and round joins. Shown here at 20 times. Every outline has a solid twin with the same name and the same geometry.</p></div>'
      f'<div><div class="x-st"><div><h4>Idle outline, active solid</h4><div class="x-tbar">'
      + "".join(f'<div class="{"on" if on else ""}">{isolid(k, 24, C[600]) if on else io(k, 24, I[500])}<span>{t}</span></div>' for k, t, on in [("home", "Home", False), ("box", "Drops", True), ("wallet", "Wallet", False), ("user", "Profile", False)])
      + '</div></div><div><h4>Tab rows: all solid, coloured by meaning</h4><div class="x-trow">'
      f'<span class="on">{isolid("clock", 16, M[600])}To check</span><span>{isolid("success", 16, N[600])}Approved</span><span>{isolid("danger", 16, V[600])}Declined</span></div>'
      f'<p class="x-note" style="margin-top:12px">The active tab is the underline and the text colour. Icons never change.</p></div></div>'
      + rules_inl([("Outline is idle", "Nucleo UI Outline 18, a 1.5 px stroke. Shown at 24 px on the tab bar and 22 px elsewhere in the product."),
                   ("Solid twin for state", "Nucleo UI Fill 18: the exact one-to-one twin of the outline, never a look-alike. Tab bar 24 px, tab rows 16 px, alerts 18 px."),
                   ("Meaning is fixed", "A box is always Drops and Campaigns, people are Creators, a house is Home. The same on every screen."),
                   ("Icons help recognition", "On key actions, tabs and chips. Not on every button label.")], 2, 22) + '</div></div>'),
 page(head("00", "The icon set", "Sixty of the glyphs the product uses, drawn from the Nucleo UI Outline 18 set. Names are the product’s own.") +
      '<div class="x-igrid">' + "".join(f'<div>{io(k, 32)}<span>{k}</span></div>' for k in ICON_GRID) + '</div>'
      f'<p class="x-note" style="margin-top:16px">Nucleo is licensed for Hypedrive’s own products. The glyph files are not for redistribution.</p>'),
 page(head("00", "Outline and solid twins", "Every active or selected state swaps to the solid twin of the same glyph. Same shape, filled in.") +
      '<div class="x-twins"><div><div class="x-tw">' + "".join(f'<div class="pr"><span>{io(k, 32)}</span><span>{isolid(k, 32, C[600])}</span><span style="margin-top:2px">{k}</span></div>' for k in TWINS) + '</div>'
      + rules_inl([("Same glyph, two states", "Outline when idle, solid when on. Cobalt on a light surface, the dark theme’s link colour on dark."),
                   ("Twins in pairs", "Every outline has a Fill twin of the same name and geometry. Idle is outline, active and selected is solid; tab rows are all solid.")], 2, 22) + '</div>'
      f'<div><h3>Fixed meanings</h3><table class="x-mean">'
      + "".join(f'<tr><td>{isolid(k, 22, INK)}</td><td>{t}</td><td>{d}</td></tr>' for k, t, d in [("box", "Drops, Campaigns", "Box"), ("users", "Creators", "People"), ("home", "Home", "House"), ("overview", "Overview", "Grid"), ("payouts", "Payouts", "Banknote"), ("live", "Live", "Play"), ("pause", "Paused", "Pause"), ("foryou", "For you", "Compass")] if k in FILLM)
      + '</table></div></div>'),
]

# ============================================================== EXPANSION 6: illustration system
xcss("""
.x-ig { display: grid; grid-template-columns: repeat(6, 1fr); gap: 12px; } .x-ig figure { margin: 0; border-radius: 20px; height: 180px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: ${i50}; gap: 2px; }
.x-ig figure img { width: 126px; height: 126px; display: block; } .x-ig figcaption { font: 600 15px var(--hd-font-ui); color: ${i700}; } .x-ig.dk figure { background: ${i900}; } .x-ig.dk figcaption { color: ${i300}; }
.x-ig .tx { align-items: flex-start; justify-content: flex-end; padding: 22px; background: transparent !important; border: 3px solid ${ink}; border-width: 3px 0 0; border-radius: 0; } .x-ig .tx b { font: 700 64px/1 var(--hd-font-display); font-variation-settings: 'opsz' 96; letter-spacing: -.03em; } .x-ig .tx span { font: 16px/1.4 var(--hd-font-ui); color: ${i600}; }
.x-ig.dk .tx { border-color: ${ink}; } .x-ig.dk .tx b, .x-ig.dk .tx span { color: ${ink}; } .x-ig.dk .tx span { color: ${i600}; }
.x-cr { display: grid; grid-template-columns: 400px 1fr; gap: 40px; align-items: start; } .x-cr .cons { background: ${i50}; border-radius: 22px; padding: 24px; } .x-cr .cons img { width: 100%; display: block; border-radius: 14px; }
.x-steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 20px; } .x-steps > div { background: ${i50}; border-radius: 18px; height: 176px; display: flex; align-items: center; justify-content: center; position: relative; } .x-steps > div img, .x-steps > div svg { height: 128px; }
.x-steps span { position: absolute; left: 14px; bottom: 10px; font: 600 15px var(--hd-font-ui); color: ${i700}; }
.x-sz { display: grid; grid-template-columns: 1fr 1.1fr 1.3fr; gap: 24px; align-items: start; } .x-sz > div > .box { border: 1px solid ${i200}; border-radius: 22px; background: ${i50}; font-family: var(--hd-font-ui); overflow: hidden; height: 400px; display: flex; align-items: center; justify-content: center; } .x-sz .box > div { background: #fff; border-radius: 16px; width: calc(100% - 32px); box-shadow: 0 0 0 1px ${i200}; } .x-sz h4 { margin: 14px 0 2px; font-size: 22px; font-variation-settings: 'opsz' 32; } .x-sz p.n { font: 15px/1.45 var(--hd-font-ui); color: ${i600}; margin: 0; }
.x-sz .c1 { padding: 16px; display: flex; gap: 14px; align-items: center; min-height: 128px; } .x-sz .c1 b, .x-sz .c2 b, .x-sz .c3 b { display: block; font: 650 19px/1.25 var(--hd-font-display); font-variation-settings: 'opsz' 24; color: ${ink}; } .x-sz .t { font: 15px/1.4 var(--hd-font-ui); color: ${i600}; margin: 4px 0 0; }
.x-sz .c2 { padding: 22px; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 4px; } .x-sz .c3 { padding: 24px 22px 22px; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 4px; }
.x-sz .dm { display: flex; gap: 8px; align-items: center; margin-top: 10px; font: 600 15px var(--hd-font-ui); color: ${c700}; } .x-sz .dm i { display: block; height: 2px; background: ${c600}; }
.x-id { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px 24px; } .x-id figure { margin: 0; } .x-id .bx { height: 250px; border-radius: 20px; background: ${i50}; display: flex; align-items: center; justify-content: center; overflow: hidden; position: relative; } .x-id img { width: 190px; display: block; } .x-id figcaption { margin-top: 8px; }
""")
def iso_cube(kind, size=128):
    L = 40; c, s_ = 0.8660254, 0.5; ox, oy = 60, 22
    T = (ox, oy); R = (ox + L*c, oy + L*s_); B = (ox, oy + L); Lf = (ox - L*c, oy + L*s_)
    dn = lambda p: (p[0], p[1] + L)
    f = lambda pts: " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
    top = [T, R, B, Lf]; left = [Lf, B, dn(B), dn(Lf)]; right = [B, R, dn(R), dn(B)]
    if kind == "wire":
        lines = [(T, R), (R, B), (B, Lf), (Lf, T), (Lf, dn(Lf)), (B, dn(B)), (R, dn(R)), (dn(Lf), dn(B)), (dn(B), dn(R))]
        body = "".join(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{C[600]}" stroke-width="1.4" stroke-linecap="round"/>' for a, b in lines)
        ang = f'<path d="M{ox + 20:.1f} {oy + L + L:.1f}" fill="none"/>'
    else:
        body = (f'<polygon points="{f(top)}" fill="{BRAND["marigold"]}"/><polygon points="{f(left)}" fill="{COB}"/><polygon points="{f(right)}" fill="{BRAND["vermilion"]}"/>')
    return f'<svg viewBox="0 0 120 128" width="{size}" height="{size}" role="img" aria-label="Isometric cube">{body}</svg>'
def ill_box(name, theme, extra="", cap=True):
    return f'<figure>{img(ILL[(name, theme)], alt=name + " illustration")}' + (f'<figcaption>{name.title()}</figcaption>' if cap else '') + '</figure>'
_names = [n for n, _ in IL.ILLS]
def ill_grid_page(theme):
    cells = "".join(ill_box(n, theme) for n in _names)
    tx = '<figure class="tx"><b>17</b><span>objects, one set of rules</span></figure>'
    return f'<div class="x-ig{" dk" if theme == "dark" else ""}">{cells}{tx}</div>'
def size_demo():
    return ('<div class="x-sz">'
            f'<div><div class="box"><div class="c1">{ill_img("search", "light", "width:84px;flex:none")}<div><b>No drops near you yet</b><p class="t">We’ll tell you the moment a brand lists one.</p></div></div></div><h4>84 px</h4><p class="n">Inline: a row, a card, a notice. The smallest the family goes.</p></div>'
            f'<div><div class="box"><div class="c2">{ill_img("approved", "light", "width:120px")}<b>Review submitted</b><p class="t" style="text-align:center">Reviews go live after the brand approves them, usually within a day.</p><span class="x-btn" style="margin-top:12px">Done</span></div></div><h4>120 px</h4><p class="n">Sheets and dialogs: one object, one line, one action.</p></div>'
            f'<div><div class="box"><div class="c3">{ill_img("parcel", "light", "width:220px")}<b style="font-size:24px">Find your next drop</b><p class="t" style="max-width:320px">Try new products free, tell your people, and get paid for honest reviews.</p><span class="x-btn" style="margin-top:14px">Browse drops</span></div></div><h4>220 px</h4><p class="n">Full-page empty states, onboarding and the first screen after sign-up.</p></div></div>')
_dont_ill = [("transform:scaleX(1.4)", "Don’t stretch or squash"), ("transform:rotate(-16deg)", "Don’t rotate"), ("filter:hue-rotate(150deg)", "Don’t recolour the faces"),
             ("filter:drop-shadow(10px 12px 8px rgba(0,0,0,.45))", "Don’t add shadows or glows"), ("width:34px", "Don’t shrink below 84 px"), (None, "Don’t crowd a scene with five")]
def dont_ill_tile(style, cap, idx):
    if style is None:
        inner = "".join(f'<img style="width:100px;position:absolute;left:{x}px;top:{y}px" src="{uri(ILL[(n, "light")])}" alt=""/>' for n, x, y in [("gift", 30, 20), ("bag", 130, 60), ("camera", 230, 10), ("payout", 80, 120), ("review", 190, 140)])
    else:
        inner = f'<img style="{"width:190px;" if "width" not in style else ""}{style}" src="{uri(ILL[("gift", "light")])}" alt=""/>'
    return f'<figure><div class="bx">{inner}</div><figcaption>{tag_no(cap)}</figcaption></figure>'
PG_ILL = [
 page(head("00", "The illustration family", "Seventeen objects for empty states, success moments and onboarding. One hand, one light, one set of colours.") + ill_grid_page("light")),
 page(head("00", "The family, in dark", "The same objects on Ink. Faces keep their colours; only physical parts, tyres and handles, stay Ink in both themes.") + ill_grid_page("dark").replace('class="x-ig dk"', 'class="x-ig dk"')),
 page(head("00", "Illustration construction", "Every object is built the same way, so a new one joins the family without looking like a guest.") +
      f'<div class="x-cr"><div class="cons">{img(CONSTR, alt="Construction grid")}<p class="x-note" style="margin-top:12px">The parcel on the 30° grid. Every illustration is drawn on it.</p></div>'
      f'<div><div class="x-steps"><div>{iso_cube("wire")}<span>1 · Draw on the grid</span></div><div>{iso_cube("flat")}<span>2 · Colour the faces</span></div><div>{ill_img("parcel", "light", "height:128px")}<span>3 · Round, then accent</span></div></div>'
      + rules_inl([("True 30° isometric", "Edges run at exactly 30° and 90°. No perspective, no hand-tilted objects."),
               ("Signature faces", "Marigold on top, Cobalt on the left, Vermilion on the right. Light comes from above."),
               ("One volume, one or two accents", "A single chunky body, plus Ink or white details: tape, a dot, a handle. Never a scene."),
               ("Rounded silhouettes", "The parcel’s continuous-curvature corners everywhere. No hairlines, no tiny parts, nothing sharp.")], 2, 6) + '</div></div>'),
 page(head("00", "Sizes in the product", "Three sizes. Pick by the space the object has to fill, then leave air around it.") + size_demo()),
 page(head("00", "Illustration, don’t") + f'<div class="x-id">' + "".join(dont_ill_tile(s_, c, i) for i, (s_, c) in enumerate(_dont_ill)) + '</div>'),
]

# ============================================================== EXPANSION 7: photography, voice, motion
xcss("""
.x-pg { display: grid; grid-template-columns: repeat(12, 1fr); grid-auto-rows: 218px; gap: 12px; } .x-pg figure { margin: 0; overflow: hidden; border-radius: 16px; } .x-pg img { width: 100%; height: 100%; object-fit: cover; display: block; }
.x-pgc { font: 15px/1.4 var(--hd-font-ui); color: ${i600}; margin: 8px 0 0; }
.x-cr3 { display: grid; grid-template-columns: 300px 300px 1fr; gap: 30px; align-items: start; } .x-cr3 h4 { margin: 12px 0 2px; font-size: 22px; font-variation-settings: 'opsz' 32; } .x-cr3 .n { font: 15px/1.45 var(--hd-font-ui); color: ${i600}; margin: 0; }
.x-cr3 .sq, .x-cr3 .hr { border-radius: 16px; overflow: hidden; } .x-cr3 .sq img { width: 100%; height: 300px; object-fit: cover; display: block; } .x-cr3 .hr img { width: 100%; height: 375px; object-fit: cover; display: block; }
.x-lr { margin-top: 12px; display: flex; flex-direction: column; gap: 8px; } .x-lr .x-rowc { padding: 8px 12px 8px 8px; } .x-lr .x-rowc img.p { width: 48px; height: 48px; }
.x-fb { border: 1px solid ${i200}; border-radius: 22px; overflow: hidden; background: #fff; font-family: var(--hd-font-ui); } .x-fb .ph { position: relative; height: 262px; } .x-fb .ph img { width: 100%; height: 100%; object-fit: cover; display: block; }
.x-fb .disc { position: absolute; top: 14px; width: 44px; height: 44px; border-radius: 50%; background: rgba(255,255,255,.94); display: flex; align-items: center; justify-content: center; color: ${ink}; } .x-fb .bd { padding: 16px 18px 18px; } .x-fb h5 { margin: 0; font: 650 24px/30px var(--hd-font-display); font-variation-settings: 'opsz' 48; letter-spacing: -.024em; } .x-fb p { margin: 2px 0 0; font: 15px/1.4 var(--hd-font-ui); color: ${i600}; }
.x-cp { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; } .x-cp > div { background: ${i50}; border-radius: 20px; padding: 20px 22px 22px; } .x-cp h4 { margin: 0 0 12px; font-size: 22px; font-variation-settings: 'opsz' 32; } .x-cp .ctx { font: 600 15px var(--hd-font-ui); color: ${c700}; margin: 0 0 4px; }
.x-cp .bf, .x-cp .af { font: 17px/1.45 var(--hd-font-ui); border-radius: 12px; padding: 11px 14px; margin: 0 0 8px; } .x-cp .bf { background: #fff; color: ${i600}; box-shadow: 0 0 0 1px ${v300}; } .x-cp .af { background: #fff; color: ${ink}; box-shadow: 0 0 0 1px ${n300}; font-weight: 500; }
.x-cp .lbl { font: 600 15px var(--hd-font-ui); margin: 10px 0 4px; display: block; } .x-cp .lbl.b { color: ${v700}; } .x-cp .lbl.a { color: ${n800}; } .x-cp .pp { margin-bottom: 14px; } .x-cp .pp:last-child { margin-bottom: 0; }
.x-rl { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px 28px; } .x-rl > div { border-top: 3px solid ${ink}; padding-top: 12px; } .x-rl b { display: block; font-size: 22px; margin-bottom: 6px; font-variation-settings: 'opsz' 32; } .x-rl p { margin: 0; font: 16px/1.5 var(--hd-font-ui); color: ${i700}; } .x-rl .ex { margin-top: 10px; padding: 10px 14px; border-radius: 12px; background: ${i50}; color: ${ink}; font-weight: 500; }
.x-mo { display: grid; grid-template-columns: 1fr 400px; gap: 40px; align-items: start; } .x-mt { width: 100%; border-collapse: collapse; font-family: var(--hd-font-ui); } .x-mt th { text-align: left; font-size: 15px; font-weight: 600; color: ${i600}; padding: 0 12px 10px 0; border-bottom: 2px solid ${ink}; } .x-mt td { padding: 13px 12px 13px 0; border-bottom: 1px solid ${i200}; font-size: 16px; vertical-align: top; line-height: 1.4; } .x-mt td:first-child { font-weight: 650; font-size: 17px; } .x-mt td.ms { font-variant-numeric: tabular-nums; font-weight: 600; white-space: nowrap; } .x-mt code { font-size: 14px; color: ${i700}; }
.x-bars { margin-top: 26px; } .x-bars h3 { font-size: 22px; margin: 0 0 8px; } .x-bars div { display: flex; align-items: center; gap: 14px; margin: 9px 0; font: 16px var(--hd-font-ui); } .x-bars span { width: 70px; font-weight: 600; } .x-bars i { height: 22px; border-radius: 5px; display: block; } .x-bars em { font-style: normal; color: ${i600}; font-variant-numeric: tabular-nums; }
.x-cv { background: ${i50}; border-radius: 22px; padding: 16px 20px 14px; margin-bottom: 14px; } .x-cv svg { display: block; height: 150px; width: auto; max-width: 100%; margin: 0 auto; } .x-cv h4 { margin: 0 0 4px; font: 650 19px var(--hd-font-display); font-variation-settings: 'opsz' 24; } .x-cv p { margin: 6px 0 0; font: 15px/1.4 var(--hd-font-ui); color: ${i600}; }
""")
_PGAL = [("p6.jpg", None), ("p2.jpg", None), ("p3.jpg", None), ("p4.jpg", None), ("p5.jpg", None)]
PG_PHOTO = [
 page(head("00", "Photography", "Real products on real surfaces, in daylight. The photograph is the proof, so it stays bare and unretouched.") +
      '<div class="x-pg">' + "".join(f'<figure style="grid-column:span {sp}">{ph_img(n, f"object-position:{op}", 900, None)}</figure>' for n, sp, op in [("p6.jpg", 5, "50% 40%"), ("p2.jpg", 4, "50% 50%"), ("p3.jpg", 3, "50% 60%"), ("p4.jpg", 3, "50% 40%"), ("p5.jpg", 3, "50% 70%"), ("p7.jpg", 6, "50% 60%")]) + '</div>'
      + rules_inl([("Real product, real surface", "A counter, a bed, a shelf, sand. Daylight or soft window light. Nothing staged to look like a studio."),
                   ("Bare, always", "No plate, tile, ring, glow or drop shadow behind a product. The photo sits straight on the surface."),
                   ("Honest edits", "Exposure, white balance and crop. No smoothing, no recolouring of the product, no composited extras."),
                   ("People only when real", "A real creator, with their say. Until then avatars are initials. We never use stock faces for named people.")], 4, 30)
      + '<p class="x-note" style="margin-top:18px">Stock stand-ins from the design references. Replace them with each brand’s own photography in production.</p>'),
 page(head("00", "Crops and ratios", "Three crops cover the product. Crop to the product, not the scene, and never stretch to fit.") +
      '<div class="x-cr3"><div><div class="sq">' + ph_img("p1.jpg", "", 700, (0, 0.18, 1, 0.8)) + '</div><h4>1:1, lists and grids</h4><p class="n">Thumbnails and list rows. Centre the product with a tenth of margin around it.</p>'
      '<div class="x-lr"><div class="x-rowc">' + ph_img("p6.jpg", "", 200, (0.1, 0, 0.7, 1), "p") + '<div><b>Glow serum, 30 ml</b><small>Lumen Labs</small></div></div></div></div>'
      '<div><div class="hr">' + ph_img("p3.jpg", "", 700, (0, 0.2, 1, 0.8)) + '</div><h4>4:5, the hero</h4><p class="n">The top of a drop page and the Instagram post. The product sits in the lower two thirds.</p></div>'
      '<div><div class="x-fb"><div class="ph">' + ph_img("p7.jpg", "", 900, (0, 0.05, 1, 0.95)) + f'<span class="disc" style="left:14px">{io("back", 22)}</span><span class="disc" style="right:14px">{io("heart", 22)}</span></div>'
      '<div class="bd"><h5>Hair and scalp set</h5><p>Zoomi · 48 reviews</p></div></div><h4>Full-bleed, the detail</h4><p class="n">Edge to edge inside its card. Controls sit on solid discs over the photo, never on the bare picture.</p></div></div>'
      + rules_inl([("Crop to the product", "Frame the product, not the room. If the product is small in the frame, crop in or choose another picture."), ("Keep it off the controls", "Back, favourite and share sit on discs at the top corners. Leave those corners free of the product."), ("Never stretch", "Scale with the ratio locked. If the ratio does not fit, crop a different part, never squash.")], 3, 26)),
]
# ---- voice
PG_VOICE = [
 page(head("00", "Writing for the interface", "Six rules that cover most screens. Each example is a line the product actually says.") +
      '<div class="x-rl">' + "".join(f'<div><b>{t}</b><p>{d}</p><p class="ex">{e}</p></div>' for t, d, e in [
          ("Sentence case", "Titles, buttons, tabs, menus. Capitals only for names.", "Apply for this drop"),
          ("Verbs on buttons", "Say what happens, starting with the verb. Never OK or Submit.", "Approve and pay ₹1,240"),
          ("Errors say what to do", "Name the problem, then the way out. Never an error code, never blame.", "Link not public. Make the post public and try again."),
          ("Say what happens next", "Tell people when and how, in plain words and real numbers.", "Reviews go live after the brand approves them, usually within a day."),
          ("Numbers are digits", "₹ with no space, Indian grouping, a real minus sign. Dates as “Nov 23”.", "Lands by Mon, Nov 23 · HDFC ••6093"),
          ("Short and human", "One idea a line. Cut the throat-clearing. One exclamation mark at most.", "Pick one now. You can add more later.")]) + '</div>'
      f'<h3 style="margin:34px 0 12px">Buttons in the product</h3><div style="display:flex;gap:12px;flex-wrap:wrap"><span class="x-btn">Apply for this drop</span><span class="x-btn">Send application</span><span class="x-btn">Confirm address</span><span class="x-btn">Share your review</span><span class="x-btn">Approve and pay ₹1,240</span><span class="x-btn grey">Learn how payouts work</span><span class="x-btn grey">Save for later</span></div>'
      f'<p class="x-note" style="margin-top:28px">Indian context is part of the voice: rupees, UPI and bank names, Delhivery and the courier’s first name, Hinglish only where a creator wrote it themselves.</p>'),
 page(head("00", "Before and after", "The same message, written the way a system writes it and the way we write it. Taken from the product’s notifications, empty states and payouts.") +
      '<div class="x-cp">' + "".join(
          f'<div><h4>{g}</h4>' + "".join(f'<div class="pp"><p class="ctx">{c}</p><span class="lbl b">Before</span><p class="bf">{b}</p><span class="lbl a">After</span><p class="af">{a}</p></div>' for c, b, a in prs) + '</div>'
          for g, prs in [("Notifications", [("Push · creator", "Notification: Review #4471 status updated to APPROVED.", "Lumen Labs loved your Night cream review."),
                                           ("Push · delivery", "Shipment status update: out for delivery.", "Ravi is delivering your Kick scooter today. Arrives by 7 pm.")]),
                         ("Empty states", [("Home · no drops nearby", "No data available.", "No drops near you yet. We’ll tell you the moment a brand lists one."),
                                           ("Search · no results", "0 results found for your query.", "No “matcha whisk” drops yet.")]),
                         ("Payouts", [("Wallet · sent", "Your remittance of INR 1240.00 has been initiated to your registered account.", "Payout sent to HDFC ••6093."),
                                      ("Wallet · held", "Payment pending verification.", "We hold ₹640 until the brand approves your review. It usually takes a day.")])]) + '</div>'),
]
# ---- motion table
def bez(x1, y1, x2, y2, w=300, h=170, pad=30):
    X = lambda v: pad + v*(w - 2*pad); Y = lambda v: h - pad - v*(h - 2*pad)
    grid = f'<rect x="{X(0)}" y="{Y(1)}" width="{X(1) - X(0)}" height="{Y(0) - Y(1)}" fill="#fff" stroke="{I[200]}"/><line x1="{X(0)}" y1="{Y(1)}" x2="{X(1)}" y2="{Y(1)}" stroke="{I[100]}" stroke-dasharray="4 4"/>'
    hl = f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(x1)}" y2="{Y(y1)}" stroke="{I[400]}" stroke-width="1.5"/><line x1="{X(1)}" y1="{Y(1)}" x2="{X(x2)}" y2="{Y(y2)}" stroke="{I[400]}" stroke-width="1.5"/>'
    path = f'<path d="M{X(0)} {Y(0)} C {X(x1):.1f} {Y(y1):.1f}, {X(x2):.1f} {Y(y2):.1f}, {X(1)} {Y(1)}" fill="none" stroke="{C[600]}" stroke-width="4" stroke-linecap="round"/>'
    pts = f'<circle cx="{X(x1):.1f}" cy="{Y(y1):.1f}" r="5.5" fill="{V[500]}"/><circle cx="{X(x2):.1f}" cy="{Y(y2):.1f}" r="5.5" fill="{V[500]}"/>'
    return f'<svg viewBox="0 0 {w} {h}" width="100%" role="img" aria-label="Easing curve">{grid}{hl}{path}{pts}</svg>'
PG_MOTION = [
 page(head("00", "Durations and easings", "Three durations and two curves cover everything. Things arrive with a short settle and leave faster than they came.") +
      '<div class="x-mo"><div><table class="x-mt"><tr><th>Token</th><th>Time</th><th>Curve</th><th>Used for</th></tr>'
      + "".join(f'<tr><td>{a}</td><td class="ms">{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in [
          ("quick", "120 ms", "standard", "Hover, press (scale 0.97), focus ring, checkbox, toggle."),
          ("base", "200 ms", "standard", "State changes: the tab underline, tooltips, menus opening, the tape-pull progress step."),
          ("arrive", "320 ms", "arrive", "Entrances: sheets, dialogs, a card on first show, a success moment. An 8 px drop and a fade."),
          ("Exit", "120 to 200 ms", "standard", "Anything leaving. Always shorter than the entrance it answers."),
          ("Reduced motion", "120 ms", "standard", "Fade only. No movement, no scale, no settle.")]) + '</table>'
      + '<div class="x-bars"><h3>The three times, to scale</h3>' + "".join(f'<div><span>{n}</span><i style="width:{ms*2.4}px;background:{col}"></i><em>{ms} ms</em></div>' for n, ms, col in [("quick", 120, C[300]), ("base", 200, C[500]), ("arrive", 320, C[700])]) + '</div></div>'
      f'<div><div class="x-cv"><h4>standard</h4>{bez(.2, .8, .2, 1)}<p><code>cubic-bezier(.2, .8, .2, 1)</code> · fast out, long ease in. Default for everything that is not an arrival.</p></div>'
      f'<div class="x-cv"><h4>arrive</h4>{bez(.2, .9, .25, 1.15)}<p><code>cubic-bezier(.2, .9, .25, 1.15)</code> · overshoots by 15% and settles, like a parcel set down.</p></div></div></div>'),
]

# ============================================================== EXPANSION 8: applications and contact
def _asset_png(path, w=None):
    from PIL import Image as _I
    im = _I.open(path).convert("RGB")
    if w and im.width > w: im = im.resize((w, round(im.height*w/im.width)), _I.LANCZOS)
    buf = _io.BytesIO(); im.save(buf, "JPEG", quality=88); return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
xcss("""
.x-ap { display: grid; gap: 40px; align-items: start; } .x-ap img.sh { display: block; border-radius: 6px; box-shadow: 0 0 0 1px ${i200}, 0 18px 40px -18px rgba(16,20,38,.28); }
.x-sp { display: flex; flex-direction: column; gap: 16px; } .x-sp > div { border-top: 3px solid ${ink}; padding-top: 12px; } .x-sp b { display: block; font-size: 20px; margin-bottom: 4px; font-variation-settings: 'opsz' 32; } .x-sp p { margin: 0; font: 16px/1.5 var(--hd-font-ui); color: ${i700}; }
.x-sp .k { font: 15px/1.5 var(--hd-font-ui); color: ${i600}; }
.x-em { background: ${i100}; border-radius: 22px; padding: 28px 0; display: flex; justify-content: center; } .x-mail { width: 640px; background: #fff; border-radius: 12px; overflow: hidden; font-family: var(--hd-font-ui); box-shadow: 0 0 0 1px ${i200}; } .x-mail img { width: 100%; display: block; }
.x-mail .bd { padding: 28px 36px 30px; } .x-mail h5 { margin: 0 0 8px; font: 700 30px/1.15 var(--hd-font-display); font-variation-settings: 'opsz' 48; letter-spacing: -.02em; color: ${ink}; } .x-mail p { margin: 0 0 18px; font: 17px/1.55 var(--hd-font-ui); color: ${i700}; } .x-mail .ft { border-top: 1px solid ${i200}; padding: 14px 36px 18px; font: 15px/1.5 var(--hd-font-ui); color: ${i600}; }
.x-ct { display: grid; grid-template-columns: 1.1fr 1fr; gap: 56px; } .x-fl { width: 100%; border-collapse: collapse; font-family: var(--hd-font-ui); } .x-fl td { padding: 11px 0; border-bottom: 1px solid ${i200}; font-size: 16px; vertical-align: top; line-height: 1.4; } .x-fl td:first-child { font-family: 'Geist Mono', monospace; font-size: 15px; color: ${c700}; width: 240px; font-weight: 500; }
.x-cb { background: ${ink}; color: #fff; border-radius: 24px; padding: 34px 36px 32px; } .x-cb h3 { font-size: 30px; margin: 0 0 12px; } .x-cb p { margin: 0 0 12px; font: 17px/1.5 var(--hd-font-ui); color: ${i300}; } .x-cb a { color: #fff; font: 650 24px var(--hd-font-ui); text-decoration: none; display: block; margin: 4px 0 2px; } .x-cb small { font: 15px/1.5 var(--hd-font-ui); color: ${i300}; display: block; }
""")
_kit = APPS2["kit"]; _post = APPS2["ig_post"]; _story = APPS2["ig_story"]
PG_APPS = [
 page(head("00", "Creator media kit", "A one-page cover a creator can send to a brand. Their name leads; Hypedrive sits quietly in the corner.") +
      f'<div class="x-ap" style="grid-template-columns:auto 1fr"><div>{img(_kit, "height:580px", "sh", "Creator media kit cover")}</div>'
      f'<div class="x-sp"><div><b>A4, portrait</b><p>1240 × 1754 px at 150 dpi, or 210 × 297 mm. Print with 3 mm bleed on the photo.</p></div>'
      f'<div><b>What the creator fills in</b><p>Name, handle, contact. The headline, line and photo can be swapped for the creator’s own.</p></div>'
      f'<div><b>The photo runs full-bleed</b><p>One bare product photo, edge to edge. The parcel overlaps the photo edge, never the product.</p></div>'
      f'<div><b>Type</b><p>Bricolage 700 for the headline and name, Geist for the line and the contact details.</p></div>'
      f'<p class="k">File: assets/print/creator-media-kit-cover-a4.svg and .png</p></div></div>'),
 page(head("00", "Instagram: post and story", "Both start from the parcel, one product photo and the line. Colour does the rest: Ink, Marigold and white.") +
      f'<div class="x-ap" style="grid-template-columns:auto auto 1fr;gap:34px"><div>{img(_post, "height:560px", "sh", "Instagram post")}</div><div>{img(_story, "height:560px", "sh", "Instagram story")}</div>'
      f'<div class="x-sp"><div><b>Post, 1080 × 1080</b><p>Photo on top, 64% of the height. The line below in Bricolage 700, “Hype out.” in Marigold.</p></div>'
      f'<div><b>Story, 1080 × 1920</b><p>Keep the top 250 px to the photo and the bottom 340 px empty: Instagram draws its own controls there.</p></div>'
      f'<div><b>One product, one line</b><p>Swap the photo for each drop. The parcel and the line stay.</p></div>'
      f'<p class="k">Files: assets/social/instagram-post-1080 and instagram-story-1080x1920, SVG and PNG</p></div></div>'),
 page(head("00", "Email header", "A quiet band at the top of every email: the logo and the line, on Ink or on white. No text that has to be read lives in the image.") +
      f'<div class="x-ap" style="grid-template-columns:700px 1fr"><div class="x-em"><div class="x-mail">{img(APPS2["email"], "", "", "Hypedrive email header")}<div class="bd"><h5>Your payout is on its way</h5><p>₹1,240 for your Glow serum review lands by Mon, Nov 23 in HDFC ••6093. We’ll tell you the moment it arrives.</p><span class="x-btn">See your payout</span></div><div class="ft">Hypedrive · You get this because you reviewed a drop.</div></div></div>'
      f'<div class="x-sp"><div><b>1200 × 300, shown at 600</b><p>Drawn at twice the size so it stays sharp on high-density screens. Give the image a background colour that matches, for clients that block images.</p></div>'
      f'<div><b>Light version</b><p>For clients that force a light theme.</p>{img(APPS2["email_l"], "width:100%;margin-top:10px;border-radius:6px;box-shadow:0 0 0 1px " + I[200], "", "Light email header")}</div>'
      f'<p class="k">Files: assets/social/email-header-1200x300 and email-header-light-1200x300</p></div></div>'),
]
PG_CONTACT = [
 page(head("00", "Using the brand", "Everything in this book ships as files. Use them as they are, and ask when something is not covered.") +
      '<div class="x-ct"><div><h3>Where things live</h3><table class="x-fl">' + "".join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in [
          ("/assets/logo", "Lockups, mark, wordmark, app icons, favicons, SVG and PNG."), ("/assets/illustrations", "Seventeen objects, light and dark."), ("/assets/patterns", "The parcel pattern in Ink, Cobalt and Paper."),
          ("/assets/social", "Link preview, avatar, banners, Instagram, LinkedIn, YouTube, email headers."), ("/assets/print", "Business cards, tape, shipping label, media kit cover."), ("/assets/motifs", "Tape bands, hexagons, the label card and the motif sheet."), ("/assets/packaging", "Box system, mailer, thank-you card, sticker sheet."), ("/assets/campaign", "Three poster key visuals and a wide banner."), ("/assets/merch and /assets/events", "Tee, tote and the booth layout."), ("/assets/screens", "Splash screens."),
          ("/tokens", "CSS variables, JSON, the Tailwind preset and type classes."), ("/ui", "The UI kit and the app screens, light and dark.")]) + '</table></div>'
      '<div><div class="x-cb"><h3>Questions and approvals</h3><p>Anything not covered here, a partner use you want checked, or a file you cannot find.</p><a href="mailto:support@hypedrive.app">support@hypedrive.app</a><small>hypedrive.app</small></div>'
      + rules([("Use the files, never redraw", "Redrawn logos drift. Take the SVG from /assets."), ("Ask before co-branding", "Send partner layouts for a look before they print or go live."), ("Report what is unclear", "If the book and a screen disagree, tell us. The book is the one we fix.")]).replace('class="rules c1"', 'class="rules" style="margin-top:22px"') + '</div></div>'),
]

# @@NEW@@
OLD = [
 page(f'<div class="cover-pat" style="background-image:url({uri(PAT_INK)})"></div><div class="cover">{img(LOCK_D, "width:760px")}'
      f'<h1>Brand Identity Guidelines</h1><p>Version 1.1 · November 2026</p></div>', "dark"),
 page(head("01", "The idea", "Hypedrive turns products into conversation. Brands ship real products; creators try them for real and tell their people.") +
      f'<div class="cols3"><div class="card"><h3>Products in.<br>Hype out.</h3><p>Our line, and our logic. Every part of the identity starts from a parcel that arrives — and the buzz it creates.</p></div>'
      f'<div class="card"><h3>The parcel</h3><p>A true isometric cube: three faces, three colours, one strip of tape. Marigold on top for the moment of opening, Cobalt for trust, Vermilion for energy.</p></div>'
      f'<div class="card"><h3>Personality</h3><p><b>Energetic</b>, not loud. <b>Honest</b>, not stiff. <b>Generous</b> with credit. <b>Quick</b> to the point.</p></div></div>'
      f'<div class="values"><div><b>Real over rehearsed</b><span>Hype only works when it’s earned. We show the product, not the pitch.</span></div>'
      f'<div><b>Fair to every side</b><span>Brands, creators and shoppers all win, or nobody does.</span></div>'
      f'<div><b>Fast feels good</b><span>Short flows, clear numbers, money that moves.</span></div></div><p class="tagline">Products in. Hype out.</p>'),
 page(head("02", "Primary logo", "The primary lockup pairs the parcel with the wordmark, drawn from Bricolage Grotesque. Use the full-colour version wherever the background allows.") +
      f'<div class="hero-logo">{img(LOCK_L, "width:900px")}</div>'
      f'<div class="cols4 logos"><div style="background:#fff">{img(LOCK_L)}<span>Colour · light</span></div><div style="background:{INK}">{img(LOCK_D)}<span>Colour · dark</span></div>'
      f'<div style="background:#fff">{img(LOCK_BW)}<span>One colour · Ink</span></div><div style="background:{COB}">{img(LOCK_WW)}<span>One colour · Paper</span></div></div>'),
 page(head("00", "Lockups", "Three arrangements. Pick by the shape of the space, never by stretching one to fit.") +
      f'<div class="lk"><div class="lk1">{img(LOCK_L, "width:86%")}<b>Horizontal</b><span>Default. Headers, nav bars, documents, anything wide.</span></div>'
      f'<div class="lk2">{img(ST_L, "width:62%")}<b>Stacked</b><span>Square and tall spaces: splash, posters, merch, social tiles.</span></div>'
      f'<div class="lk3">{img(MARK_L, "width:58%")}<b>Parcel only</b><span>App icon, avatar, favicon, or once the name is already on screen.</span></div></div>'
      f'<div class="cols3 lkd"><div style="background:{INK}">{img(ST_D, "width:50%")}</div><div style="background:{COB}">{img(ST_W, "width:50%")}</div><div class="apps">{img(APP_INK, "width:30%")}{img(APP_COB, "width:30%")}{img(APP_PAPER, "width:30%")}</div></div>'),
 page(head("03", "Mark & wordmark", "The parcel works alone as app icon, avatar and favicon. The wordmark works alone where the parcel is already present.") +
      f'<div class="cols4 marks"><div style="background:#fff">{img(MARK_L)}</div><div style="background:{INK}">{img(MARK_D)}</div>'
      f'<div style="background:#fff">{img(MARK_B)}</div><div style="background:{COB}">{img(MARK_W)}</div></div>'
      f'<div class="cols2 words"><div style="background:#fff">{img(WORD_B, "width:80%")}</div><div style="background:{INK}">{img(WORD_W, "width:80%")}</div></div>'
      f'<div class="tittle"><div>{img(crop(WORD_B, 83.2, -1, 16.6, 28), "height:150px;display:block;margin:0 auto")}</div><p><b>The parcel in the name.</b> The dot of the <i>i</i> is the parcel’s hexagon silhouette, drawn 5% larger than a round dot so it reads at the same weight. It’s the one custom detail in the wordmark. Never swap it back to a round dot or add colour to it.</p></div>'),
 page(head("04", "Construction & spacing", "The parcel is drawn on a 30° isometric grid; the logo’s clear space and minimum sizes follow from the cap height.") +
      f'<div class="cols2 constr" style="grid-template-columns:560px 1fr;gap:48px"><div>{img(CONSTR, "height:520px;display:block;margin:0 auto")}<p class="cap" style="margin-top:12px">A 1:1:1 cube on the 30° grid. Tape is 23% of the lid’s depth and drops 46% down the right face. Corners round at 14.5% of a face edge.</p></div>'
      f'<div><div class="clear">{img(CLEAR, "width:100%")}</div><p class="cap" style="margin-top:10px">Clear space is half the cap height on every side (dashed), and the same gap sits between parcel and wordmark. Parcel height is ascender to descender plus 5% optical overshoot.</p>'
      f'</div></div>'),
 page(head("05", "Logo misuse", "Six mistakes to avoid. The logo is always used exactly as supplied in /assets/logo.") + f'<div class="cols3 donts">{dont_html}</div>'),
 page(head("06", "Colour", "Four brand colours. Ink and Paper carry most surfaces; Cobalt leads actions; Vermilion and Marigold are accents that bring the energy.") +
      f'<div class="cols4 sws">{swatch_block("Cobalt", BRAND["cobalt"], "Actions, links, focus, trust")}{swatch_block("Vermilion", BRAND["vermilion"], "Energy, hype moments, alerts")}'
      f'{swatch_block("Marigold", BRAND["marigold"], "Highlights, rewards, celebration")}{swatch_block("Ink", INK, "Text and dark surfaces")}</div>'
      f'<div class="ratio"><div style="flex:46;background:#fff;color:{INK};border:1px solid {SCALES["ink"][200]}">Paper 46%</div><div style="flex:30;background:{INK}">Ink 30%</div>'
      f'<div style="flex:14;background:{COB}">Cobalt 14%</div><div style="flex:6;background:{BRAND["vermilion"]}">6%</div><div style="flex:4;background:{BRAND["marigold"]};color:{INK}">4%</div></div><p class="cap">Rough share of any screen or layout: Paper 46% · Ink 30% · Cobalt 14% · Vermilion 6% · Marigold 4%.</p>'),
 page(head("07", "Colour scales", "Built in OKLCH: every step has matched perceived lightness across hues, with a gentle hue shift so lights stay warm and darks stay deep.") +
      "".join(scale_row(n, sc) for n, sc in SCALES.items()) +
      f'<p class="cap">Mint is the functional success colour only. Semantic tokens: accent = Cobalt 600 · success = Mint 700 · warning = Marigold 700 · danger = Vermilion 700.</p>'),
 page(head("08", "Accessible pairings", "Body text needs 4.5:1 (AA). Large display text needs 3:1. White on Marigold never passes, so use Ink.") +
      f'<div class="pairs">{"".join(pair(*p) for p in PAIRS)}</div>'),
 *PG_TYPE,
 *PG_LAYOUT,
 page(head("11", "Illustration", "The parcel grows into a family of isometric objects. One hue per object, three tones per object (light top, mid left, deep right), Ink for accents, a single round dot.") +
      f'<div class="cols3 ills">{ill_grid}</div>'),
 page(head("12", "Patterns & packaging") +
      f'<div class="cols3 pats"><div style="background-image:url({uri(PAT_INK)})"></div><div style="background-image:url({uri(PAT_COB)})"></div><div style="background-image:url({uri(PAT_PAPER)});border:1px solid {SCALES["ink"][200]}"></div></div>'
      f'<div class="tape">{img(TAPE, "width:100%")}</div><div class="tape">{img(TAPE_V, "width:100%")}</div>'
      f'<p class="cap">Parcel pattern for backgrounds (Ink, Cobalt, Paper). Branded packaging tape in Cobalt and Vermilion.</p>'),
 page(head("13", "In the product") +
      f'<div class="screens"><div class="phone">{img(APPS["splash_c"], "width:100%")}</div><div class="phone">{img(APPS["splash_m"], "width:100%")}</div>'
      f'<div class="home"><div class="grid">{"".join("<i></i>" for _ in range(6))}<div class="app">{img(APP_INK, "width:100%")}<span>Hypedrive</span></div>{"".join("<i></i>" for _ in range(5))}</div></div></div>'
      f'<p class="cap" style="margin-top:22px">Splash: colour lockup on Ink, or the one-colour Ink lockup on Paper, centred at 62% of the screen width. App icon: the parcel on an Ink tile at 60% of the tile.</p>'),
 *PG_UI,
 *PG_COMP,
 page(head("14", "Social") +
      f'<div class="social"><div class="og">{img(APPS["og"], "width:100%")}<span>Link preview 1200×630</span></div>'
      f'<div class="side"><div>{img(APPS["avatar"], "width:180px;border-radius:50%")}<span>Avatar</span></div><div>{img(APPS["banner"], "width:100%")}<span>Banner 1500×500</span></div></div></div>'),
 page(head("15", "Print") +
      f'<div class="print"><div><div class="cards">{img(APPS["card_f"], "width:100%")}{img(APPS["card_b"], "width:100%")}</div><p class="cap">Business card 85×55 mm: Ink front with the parcel pattern, Paper back with the brand stripe.</p><div class="tape" style="margin-top:28px">{img(TAPE, "width:100%")}</div><p class="cap">Packaging tape, 48 mm.</p></div><div class="label">{img(APPS["label"], "width:100%")}<p class="cap" style="text-align:center">Shipping label 4×6 in</p></div></div>'),
 *PG_CHART,
 page(head("16", "Voice & tone", "We sound like a friend who’s great at their job: warm, quick, and straight with the numbers.") +
      f'<div class="voice">'
      f'<div><h3>Say it straight</h3><p class="do">{_G_OK}Your payout is on its way. It lands by Friday.</p><p class="no">{_G_NO}We are pleased to inform you that your remittance has been initiated.</p></div>'
      f'<div><h3>Hype the product, not us</h3><p class="do">{_G_OK}120 creators are trying your serum this week.</p><p class="no">{_G_NO}Hypedrive’s revolutionary AI-powered platform…</p></div>'
      f'<div><h3>Short and human</h3><p class="do">{_G_OK}Box opened? Tell us what you think.</p><p class="no">{_G_NO}Please proceed to submit your product review at your earliest convenience.</p></div>'
      f'<div><h3>Celebrate, briefly</h3><p class="do">✓ Nice, review approved.</p><p class="no">✕ AMAZING!!! You’re a SUPERSTAR!!! Best creator ever!!!</p></div></div>'
      f'<div class="vwords"><div><h3>Words we use</h3><p>creator · product · try · review · drop · payout · campaign · on its way</p></div>'
      f'<div><h3>Words we avoid</h3><p>influencer solution · leverage · synergy · revolutionary · guru · seamless · game-changing</p></div>'
      f'<div><h3>Writing rules</h3><p>Sentence case everywhere. Numbers as digits. The verb comes first on buttons (“Send review”). One exclamation mark, at most.</p></div></div>'),
 page(head("17", "Motion", "Things arrive. Motion feels like a parcel being set down: a short drop, a tiny settle, never a bounce-fest.") +
      f'<div class="cols3 motion"><div class="card"><h3>Arrive</h3><p>Enter: 8px drop + fade, 320ms, ease-arrive <code>cubic-bezier(.2,.9,.25,1.15)</code>.</p><div class="demo arrive">{img(MARK_L, "width:96px")}</div></div>'
      f'<div class="card"><h3>Tape pull</h3><p>Progress and loading: a strip of tape pulls across, left to right, 200ms per step.</p><div class="demo"><div class="tp"></div></div></div>'
      f'<div class="card"><h3>Keep it quick</h3><p>Quick 120ms (hover, press) · Base 200ms (UI) · Arrive 320ms (entrances). Respect reduced-motion: fade only.</p></div></div>'
      f'<h3 style="margin-top:30px">Arrive, frame by frame</h3><div class="story">' + "".join(f'<div><div class="fr">{img(MARK_L, f"width:84px;transform:translateY({y}px);opacity:{o}")}</div><span>{t}</span></div>' for (y, o), t in zip([(-14, 0), (-6, .6), (2, 1), (0, 1)], ["0 ms · above, hidden", "120 ms · dropping in", "240 ms · lands, 2px past", "320 ms · settled"])) + '</div>'),
 page(head("18", "Design tokens", "Everything here ships as code: CSS variables, JSON and a Tailwind preset in /tokens.") +
      f'<pre class="short">{_short(chr(10).join([":root {"] + [l for l in css[:css.index("")] if any(k in l for k in ("brand-", "font-", "ease", "dur", "space-1", "space-4", "radius-md", "shadow-e1"))] + [f"  /* + {sum(len(v) for v in SCALES.values())} scale steps, {len(SEM_L)} semantic roles, light and dark */", "}"]))}</pre>'
      + f'<p class="cap" style="margin-top:18px">Fonts, easing, durations, spacing, radius and shadows all ship as variables. Colour roles follow on the next page.</p>'),
 page(head("00", "Semantic colour tokens", "Left value: light theme (:root). Right value: dark theme ([data-theme=\"dark\"]). Every text pairing passes WCAG AA in both.") +
      f'<div class="semt">' + "".join(f'<div class="srw"><b>--hd-{n}</b><span><i style="background:{SEM_L[n]}"></i>{SEM_L[n]}</span><span><i style="background:{SEM_D[n]}"></i>{SEM_D[n]}</span></div>' for n in SEM_L) + '</div>'
''),
 page(f'<div class="cover-pat" style="background-image:url({uri(PAT_COB)})"></div><div class="cover">{img(LOCK_WW, "width:620px")}<h1 style="font-size:64px">{TAGLINE}</h1></div>', "cobalt"),
]

# @@ASM@@
def G(name): return globals().get(name, [])
exec(open("/tmp/hdwm/brandx.py").read())          # new identity pages, section openers, cover, furniture, TOC
_n = [0]

TOKCSS = "\n".join(css)
CSSB = f"""
@font-face {{ font-family: 'Bricolage Grotesque'; src: url(data:font/ttf;base64,{font64}) format('truetype'); font-weight: 200 800; font-stretch: 75% 100%; }}
@font-face {{ font-family: 'Geist'; src: url(data:font/ttf;base64,{geist64}) format('truetype'); font-weight: 100 900; }}
@font-face {{ font-family: 'Geist Mono'; src: url(data:font/ttf;base64,{gmono64}) format('truetype'); font-weight: 100 900; }}
@page {{ size: 1600px 900px; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: #e9eaee; font-family: 'Bricolage Grotesque', sans-serif; color: {INK}; font-variation-settings: 'opsz' 16; }}
.page {{ width: 1600px; height: 900px; padding: 72px 88px; background: #fff; position: relative; overflow: hidden; margin: 24px auto; page-break-after: always; break-after: page; }}
@media print {{ body {{ background: #fff; }} .page {{ margin: 0; }} }}
.page.dark {{ background: {INK}; color: #fff; }} .page.cobalt {{ background: {COB}; color: #fff; }}
header small {{ font-size: 14px; font-weight: 700; color: {SCALES['cobalt'][600]}; }}
.dark header small, .cobalt header small {{ color: {SCALES['marigold'][300]}; }}
h2 {{ font-size: 52px; line-height: 1.05; margin: 6px 0 14px; font-weight: 700; font-variation-settings: 'opsz' 72; letter-spacing: -.015em; }}
h3 {{ font-size: 24px; margin: 0 0 10px; font-variation-settings: 'opsz' 32; }}
.lead {{ font-size: 21px; line-height: 1.45; max-width: 1040px; color: {SCALES['ink'][600]}; margin: 0 0 30px; }}
.cap {{ font-size: 17px; line-height: 1.5; color: {SCALES['ink'][500]}; }}
.cover {{ position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 28px; }}
.cover h1 {{ font-size: 40px; margin: 10px 0 0; font-weight: 600; font-variation-settings: 'opsz' 48; }}
.cover p {{ color: {SCALES['ink'][300]}; margin: 0; font-size: 18px; }}
.cover-pat {{ position: absolute; inset: 0; opacity: .5; background-size: 240px; }}
.cols2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 28px; }} .cols3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
.cols4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }}
.card {{ background: {SCALES['ink'][50]}; border-radius: 20px; padding: 28px; }} .card p {{ font-size: 17px; line-height: 1.5; color: {SCALES['ink'][700]}; margin: 0; }}
.values {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 26px; }}
.values div {{ border-top: 3px solid {INK}; padding-top: 14px; }} .values b {{ display: block; font-size: 22px; margin-bottom: 6px; }} .values span {{ font-size: 16px; color: {SCALES['ink'][600]}; line-height: 1.5; }}
.hero-logo {{ display: flex; justify-content: center; padding: 40px 0 50px; }}
.logos div, .marks div, .words div {{ border-radius: 18px; border: 1px solid {SCALES['ink'][100]}; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; }}
.logos div {{ height: 270px; }} .logos img {{ width: 84%; }} .logos span {{ position: absolute; bottom: 12px; left: 16px; font-size: 13px; color: {SCALES['ink'][400]}; }}
.marks div {{ height: 250px; }} .marks img {{ width: 72%; }} .words {{ margin-top: 16px; }} .words div {{ height: 150px; }}
.constr img {{ border-radius: 16px; }} .clear {{ border-radius: 16px; overflow: hidden; }}
.minsz {{ display: flex; flex-direction: column; gap: 14px; margin-top: 6px; }} .minsz .mz {{ flex-direction: row; gap: 22px; align-items: center; }} .minsz div {{ display: flex; flex-direction: column; gap: 8px; align-items: flex-start; }} .minsz span {{ font-size: 13px; color: {SCALES['ink'][500]}; }}
.donts .dbox {{ height: 235px; background-image: none; border-radius: 18px; background: {SCALES['ink'][50]}; display: flex; align-items: center; justify-content: center; overflow: hidden; }}
.donts figure {{ margin: 0; }} .donts figcaption {{ margin-top: 10px; font-size: 15px; }}
.sw {{ height: 330px; border-radius: 22px; padding: 26px; display: flex; flex-direction: column; }} .sw b {{ font-size: 30px; }}
.sw span {{ margin-top: auto; font-size: 15px; line-height: 1.6; opacity: .9; }} .sw i {{ font-style: normal; font-size: 14px; margin-top: 10px; opacity: .8; }}
.ratio {{ display: flex; height: 64px; border-radius: 14px; overflow: hidden; margin-top: 26px; font-size: 14px; font-weight: 600; color: #fff; }}
.ratio div {{ display: flex; align-items: center; padding-left: 14px; }}
.srow {{ display: grid; grid-template-columns: 120px repeat(11, 1fr); gap: 6px; margin-bottom: 10px; align-items: stretch; }}
.sname {{ font-weight: 700; font-size: 17px; display: flex; align-items: center; }}
.chip {{ height: 92px; border-radius: 10px; padding: 8px; display: flex; flex-direction: column; justify-content: space-between; font-size: 11px; }} .chip b {{ font-size: 13px; }}
.pairs {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; }}
.pair {{ height: 250px; border-radius: 18px; padding: 24px; display: flex; flex-direction: column; border: 1px solid {SCALES['ink'][100]}; }}
.pair b {{ font-size: 64px; font-variation-settings: 'opsz' 72; }} .pair span {{ font-size: 16px; margin-top: auto; }} .pair em {{ font-style: normal; font-weight: 700; font-size: 15px; margin-top: 6px; }}
.specimen {{ display: grid; grid-template-columns: 420px 1fr; gap: 40px; align-items: center; }}
.aa {{ font-size: 300px; font-weight: 700; line-height: .9; font-variation-settings: 'opsz' 96; letter-spacing: -.03em; }}
.big {{ font-size: 40px; line-height: 1.3; font-weight: 600; font-variation-settings: 'opsz' 48; margin: 0 0 20px; }}
.trow {{ display: grid; grid-template-columns: 220px 1fr; gap: 24px; padding: 10px 0; border-bottom: 1px solid {SCALES['ink'][100]}; align-items: baseline; }}
.tmeta b {{ display: block; font-size: 16px; }} .tmeta span {{ font-size: 13px; color: {SCALES['ink'][500]}; }}
.ills figure {{ margin: 0; background: {SCALES['ink'][50]}; border-radius: 18px; height: 300px; display: flex; flex-direction: column; align-items: center; justify-content: center; }}
.ills img {{ height: 220px; }} .ills figcaption {{ font-size: 15px; font-weight: 600; color: {SCALES['ink'][600]}; }}
.pats div {{ height: 240px; border-radius: 18px; background-size: 160px; }} .tape {{ margin-top: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,.12); }}
.screens {{ display: flex; gap: 40px; align-items: flex-start; }} .phone {{ width: 290px; padding: 8px; border-radius: 46px; background: #1a1b1f; position: relative; box-shadow: inset 0 0 0 1px #45474e, inset 0 0 0 2.5px #0c0d10, inset 0 0 0 3.5px #2b2d33, 0 24px 48px -18px rgba(16,20,38,.35); }}
.phone > img {{ display: block; width: 100% !important; border-radius: 38px; }}
.phone::after {{ content: ''; position: absolute; top: 17px; left: 50%; transform: translateX(-50%); width: 88px; height: 26px; border-radius: 14px; background: #000; }}
.phone::before {{ content: ''; position: absolute; right: -3px; top: 170px; width: 3px; height: 70px; border-radius: 0 2px 2px 0; background: #2b2d33; }}
.home {{ flex: 1; height: 600px; border-radius: 40px; background: #eeeef1; padding: 50px; }}
.home .grid {{ display: grid; grid-template-columns: repeat(4, 120px); gap: 34px 46px; justify-content: center; }}
.home i {{ width: 120px; height: 120px; border-radius: 28px; background: rgba(255,255,255,.35); display: block; }}
.home .app {{ display: flex; flex-direction: column; align-items: center; gap: 6px; }} .home .app img {{ width: 120px !important; border-radius: 28px; box-shadow: 0 8px 20px rgba(0,0,0,.25); }}
.home .app span {{ color: #fff; font-size: 15px; font-weight: 600; text-shadow: 0 1px 3px rgba(0,0,0,.3); }}
.social {{ display: grid; grid-template-columns: 1.1fr 1fr; gap: 30px; }} .social img {{ border-radius: 14px; }} .social span {{ display: block; font-size: 14px; color: {SCALES['ink'][500]}; margin-top: 8px; }}
.side {{ display: flex; flex-direction: column; gap: 26px; }}
.print {{ display: grid; grid-template-columns: 1.7fr 1fr; gap: 40px; align-items: start; }} .cards {{ display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }}
.cards img {{ border-radius: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.15); width: 100% !important; }} .label img {{ width: 62% !important; display:block; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,.12); border-radius: 18px; }}
.voice {{ display: grid; grid-template-columns: 1fr 1fr; gap: 22px 40px; }} .voice p {{ font-size: 18px; margin: 6px 0; padding: 12px 16px; border-radius: 12px; }}
.do, .no {{ background: #fff; color: {INK}; box-shadow: inset 0 0 0 1px #e8e8eb; display: flex; gap: 10px; align-items: center; }} .do .vg, .no .vg {{ width: 16px; height: 16px; flex: none; }} .no {{ color: {SCALES['ink'][700]}; }}
.motion code {{ font-size: 13px; background: #fff; padding: 2px 6px; border-radius: 6px; }}
.demo {{ height: 150px; display: flex; align-items: center; justify-content: center; margin-top: 16px; }}
.arrive img {{ animation: arrive 1.6s cubic-bezier(.2,.9,.25,1.15) infinite; }}
@keyframes arrive {{ 0% {{ transform: translateY(-14px); opacity: 0; }} 30%, 100% {{ transform: none; opacity: 1; }} }}
.tp {{ width: 80%; height: 22px; border-radius: 4px; background: {SCALES['ink'][100]}; position: relative; overflow: hidden; }}
.tp::after {{ content: ''; position: absolute; inset: 0; width: 62%; background: {COB}; border-radius: 4px; }}
.tagline {{ font-size: 132px; font-weight: 700; font-variation-settings: 'opsz' 96; letter-spacing: -.025em; margin: 56px 0 0; line-height: .98; }}
.weights {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 14px; margin-top: 30px; }} .weights div {{ background: {SCALES['ink'][50]}; border-radius: 14px; padding: 18px 20px; }}
.weights b {{ font-size: 44px; font-weight: inherit; display: block; font-variation-settings: 'opsz' 48; }} .weights span {{ font-size: 13px; color: {SCALES['ink'][500]}; }}
.opsz {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 14px; }} .opsz div {{ border: 1px solid {SCALES['ink'][100]}; border-radius: 14px; padding: 14px 20px; }}
.opsz b {{ font-size: 52px; font-weight: 700; display: block; }} .opsz span {{ font-size: 13px; color: {SCALES['ink'][500]}; }}
.vwords {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 30px; }} .vwords div {{ border-top: 3px solid {INK}; padding-top: 14px; }} .vwords p {{ font-size: 17px; line-height: 1.6; color: {SCALES['ink'][700]}; margin: 0; }}
.story {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; }} .story .fr {{ height: 150px; border-radius: 16px; background: {SCALES['ink'][50]}; display: flex; align-items: center; justify-content: center; border-bottom: 3px solid {SCALES['ink'][200]}; }}
.story span {{ display: block; margin-top: 8px; font-size: 14px; color: {SCALES['ink'][600]}; }}
.sem {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px 20px; margin-top: 26px; }} .sem div {{ display: grid; grid-template-columns: 40px 1fr; grid-template-rows: auto auto; column-gap: 12px; align-items: center; }}
.sem i {{ grid-row: span 2; width: 40px; height: 40px; border-radius: 10px; border: 1px solid {SCALES['ink'][200]}; }} .sem b {{ font-size: 14px; }} .sem span {{ font-size: 13px; color: {SCALES['ink'][500]}; font-family: monospace; }}
.lk {{ display: grid; grid-template-columns: 1.5fr 1fr 1fr; gap: 20px; }} .lk > div {{ border: 1px solid {SCALES['ink'][100]}; border-radius: 20px; height: 330px; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px; text-align: center; }}
.lk b {{ margin-top: 22px; font-size: 18px; }} .lk span {{ font-size: 14px; color: {SCALES['ink'][500]}; margin-top: 4px; max-width: 300px; }}
.lkd {{ margin-top: 20px; }} .lkd > div {{ height: 200px; border-radius: 20px; display: flex; align-items: center; justify-content: center; }} .lkd .apps {{ gap: 14px; background: {SCALES['ink'][50]}; }}
.tittle {{ display: grid; grid-template-columns: 260px 1fr; gap: 28px; align-items: center; margin-top: 22px; background: {SCALES['ink'][50]}; border-radius: 18px; padding: 16px 24px; }} .tittle p {{ font-size: 18px; line-height: 1.55; color: {SCALES['ink'][700]}; margin: 0; }}
.space {{ display: flex; flex-direction: column; gap: 10px; }} .space div {{ display: grid; grid-template-columns: 280px 110px 1fr; align-items: center; }}
.space i {{ height: 22px; background: {COB}; border-radius: 4px; display: block; }} .space b {{ font-size: 15px; }} .space span {{ font-size: 14px; color: {SCALES['ink'][500]}; font-variant-numeric: tabular-nums; }}
.radii {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }} .radii div {{ height: 110px; background: {SCALES['cobalt'][50]}; border: 2px solid {SCALES['cobalt'][300]}; padding: 12px; display: flex; flex-direction: column; justify-content: flex-end; }}
.radii b, .elev b {{ font-size: 15px; }} .radii span, .elev span {{ font-size: 13px; color: {SCALES['ink'][500]}; }}
.elev {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }} .elev div {{ height: 110px; background: #fff; border-radius: 14px; padding: 14px; display: flex; flex-direction: column; justify-content: flex-end; }}
.cat div {{ display: grid; grid-template-columns: 44px 1fr; grid-template-rows: auto auto; column-gap: 14px; margin-bottom: 10px; }} .cat i {{ grid-row: span 2; width: 44px; height: 44px; border-radius: 10px; }}
.cat b {{ font-size: 15px; }} .cat span {{ font-size: 13px; color: {SCALES['ink'][500]}; font-family: monospace; }}
.seq {{ display: flex; height: 44px; border-radius: 10px; overflow: hidden; }} .seq i {{ flex: 1; }}
.chart {{ background: {SCALES['ink'][50]}; border-radius: 20px; padding: 28px; }} .bar {{ display: grid; grid-template-columns: 40px auto 1fr; gap: 12px; align-items: center; margin: 12px 0; }}
.bar span {{ font-size: 14px; color: {SCALES['ink'][600]}; }} .bar div {{ height: 34px; border-radius: 6px; }} .bar em {{ font-style: normal; font-weight: 700; font-size: 15px; font-variant-numeric: tabular-nums; }}
h2, .lead {{ text-wrap: balance; }} .chip span, .sw span, .sem span, pre, .pair em {{ font-variant-numeric: tabular-nums; }}
{TOKCSS}
.semt {{ columns: 3; column-gap: 36px; margin-top: 0; }} .semt .srw {{ break-inside: avoid; }}
.srw {{ display: grid; grid-template-columns: 1.35fr 1fr 1fr; padding: 4px 0; border-bottom: 1px solid {I[100]}; align-items: center; font-size: 13px; }}
.srw b {{ font-family: monospace; font-size: 13px; }} .srw span {{ display: flex; gap: 8px; align-items: center; font-family: monospace; color: {I[600]}; font-variant-numeric: tabular-nums; }}
.srw i {{ width: 18px; height: 18px; border-radius: 5px; border: 1px solid {I[200]}; display: inline-block; }}
pre.short {{ columns: 2; font-size: 14px; padding: 20px 28px; }}
pre {{ white-space: pre-wrap; word-break: break-word; background: {INK}; color: {SCALES['marigold'][200]}; font-size: 16px; line-height: 1.6; border-radius: 18px; padding: 28px 34px; margin: 0; columns: 2; }}

.fonts3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; }}
.fcard {{ background: {SCALES['ink'][50]}; border-radius: 20px; padding: 26px 28px; display: flex; flex-direction: column; min-height: 400px; }}
.fa {{ font-size: 120px; line-height: 1; margin-bottom: 14px; }} .fn {{ font-size: 24px; font-variation-settings: 'opsz' 32; }}
.fr {{ font-size: 16px; font-weight: 600; color: {SCALES['ink'][600]}; margin: 2px 0 8px; }} .fu {{ font-size: 15px; line-height: 1.45; color: {SCALES['ink'][700]}; margin: 0 0 14px; }}
.fs {{ font-size: 21px; line-height: 1.3; margin: 0 0 auto; padding-top: 14px; border-top: 1px solid {SCALES['ink'][200]}; }} .fcard .cap {{ margin: 12px 0 0; font-size: 13px; }}
code {{ font-family: 'Geist Mono', monospace; font-size: .92em; }}
.tscale .trow {{ padding: 12px 0; grid-template-columns: 330px 1fr; align-items: center; }} .tscale {{ margin-top: 6px; }}
.rwrap {{ display: grid; grid-template-columns: 1fr 380px; gap: 48px; }} .rgrid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px 24px; }}
.rc b {{ display: block; font-size: 15px; margin-top: 10px; }} .rc span {{ font-size: 13px; color: {SCALES['ink'][500]}; }} .rz {{ height: 104px; display: flex; align-items: center; background: {SCALES['ink'][50]}; border-radius: 16px; justify-content: center; }}
.rs {{ display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 560; font-family: var(--hd-font-ui); background: #fff; }} .rs.line {{ border: 1px solid {SCALES['ink'][300]}; font-weight: 500; color: {SCALES['ink'][700]}; }}
.rside {{ background: {SCALES['ink'][50]}; border-radius: 20px; padding: 24px; }} .cc {{ margin-bottom: 16px; }} .cc > div {{ background: #fff; border: 1px solid {SCALES['ink'][300]}; width: 100%; height: 84px; }} .cc > div > div {{ background: {SCALES['cobalt'][600]}; width: 100%; height: 100%; }}
.cc b {{ display: block; font-size: 14px; margin-top: 6px; font-weight: 600; }}
.sdemo b {{ display: block; margin-top: 10px; font-size: 16px; }} .sdemo span {{ font-size: 14px; color: {SCALES['ink'][500]}; }}
.sd {{ background: {SCALES['ink'][100]}; border-radius: 16px; padding: 16px; height: 150px; display: flex; flex-direction: column; justify-content: center; }}
.sc {{ background: #fff; border: 1px solid {SCALES['ink'][200]}; border-radius: 16px; margin: 0; padding: 12px 16px; font: 600 15px var(--hd-font-ui); height: 44px; display: flex; align-items: center; }}
.sc.pad {{ height: auto; padding: 16px; position: relative; background: {SCALES['cobalt'][100]}; border-color: #e8e8eb; }} .sc.pad span {{ background: #fff; border-radius: 8px; padding: 12px; width: 100%; display: block; }} .sc.pad u {{ display: none; }}
.gap {{ display: flex; align-items: center; justify-content: center; background: {SCALES['cobalt'][200]}; margin: 0; }} .gap em {{ font: 600 11px var(--hd-font-ui); color: {SCALES['cobalt'][800]}; font-style: normal; white-space: nowrap; }}
.elevs {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }} .ep {{ background: var(--hd-canvas); color: var(--hd-fg); border-radius: 20px; padding: 24px 24px 44px; border: 1px solid {SCALES['ink'][200]}; font-family: var(--hd-font-ui); }}
.ep h4 {{ margin: 0 0 4px; font-size: 22px; font-family: var(--hd-font-display); font-weight: 650; }} .eh {{ font-size: 14px; color: var(--hd-fg-muted); margin: 14px 0 12px; }}
.e4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }} .ft {{ background: var(--hd-surface); border: 1px solid var(--hd-border); border-radius: 16px; height: 84px; display: flex; align-items: flex-end; padding: 12px; font-size: 14px; }}
.e3x {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }} .ff {{ background: var(--hd-overlay); border-radius: 16px; height: 130px; padding: 14px; display: flex; flex-direction: column; justify-content: flex-end; }}
.ff b {{ font-size: 18px; }} .ff span {{ font-size: 13px; color: var(--hd-fg-muted); }}
.rules {{ display: flex; flex-direction: column; gap: 16px; }} .rules b {{ display: block; font-size: 17px; margin-bottom: 3px; font-variation-settings: 'opsz' 24; }} .rules p {{ margin: 0; font-family: var(--hd-font-ui); font-size: 15px; line-height: 1.5; color: {SCALES['ink'][700]}; }}
.rules.c3:not(.inl) {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 24px; }} .rules.c3:not(.inl) > div {{ border-top: 3px solid {INK}; padding-top: 12px; }}
.rules.inl {{ display: grid; gap: 28px; margin-top: 28px; }} .rules.c2 {{ grid-template-columns: repeat(2, 1fr); }} .rules.c3 {{ grid-template-columns: repeat(3, 1fr); }} .rules.c4 {{ grid-template-columns: repeat(4, 1fr); }} .rules.inl > div {{ border-top: 3px solid {INK}; padding-top: 12px; }}
.crop {{ display: block; border-radius: 16px; }} .uiflex {{ display: flex; gap: 40px; align-items: flex-start; }} .uiflex > .rules {{ flex: 1; min-width: 0; }}
.phones {{ display: flex; gap: 22px; }} .rp {{ display: block; width: auto; }}
.dkgrid {{ display: grid; grid-template-columns: 700px 700px; gap: 24px; margin-top: 4px; }}
.cside2 {{ flex: 1; }} .cside2 .cat div {{ margin-bottom: 14px; }}
"""
def _floor(h, mn=15):
    h = h.replace(">foryou<", ">for you<")
    h = re.sub(r"(font-size:\s*)(\d+(?:\.\d+)?)px", lambda m: m.group(1) + (str(mn) if float(m.group(2)) < mn else m.group(2)) + "px", h)
    h = re.sub(r"(font:\s*(?:[a-z]+\s+)?(?:\d{3}\s+)?)(\d+(?:\.\d+)?)px", lambda m: m.group(1) + (str(mn) if float(m.group(2)) < mn else m.group(2)) + "px", h)
    return h
html = f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Hypedrive Brand Identity</title><link rel=icon type='image/svg+xml' href='assets/logo/favicon/favicon.svg'><style>{CSSB}{chr(10).join(XCSS)}</style></head><body>{''.join(pages)}</body></html>"
_WARM = {SCALES["ink"][50].lower(): "#ffffff", SCALES["ink"][100].lower(): "#f0f0f3", SCALES["ink"][200].lower(): "#e8e8eb", SCALES["ink"][300].lower(): "#d5d6dc"}
_WSKIP = {25, 26, 27, 31, 94}
def _warm(h):
    return h
    """Direction A: the book's own surfaces go warm (white cards on a warm canvas, warm hairlines). Pages that print the Ink scale as data keep the real hexes."""
    rx = re.compile("|".join(re.escape(k) for k in _WARM), re.I)
    sub = lambda t: rx.sub(lambda m: _WARM[m.group(0).lower()], t)
    head_, body_ = h.split("<body>", 1)
    parts = re.split(r'(?=<section data-p=")', body_)
    out = []
    for q in parts:
        m = re.match(r'<section data-p="(\d+)"', q)
        out.append(q if (m and int(m.group(1)) in _WSKIP) else sub(q))
    return sub(head_) + "<body>" + "".join(out)
open(os.path.join(OUT, "Hypedrive-Brand-Guidelines.html"), "w").write(_warm(_floor(html)))
print("pages", len(pages))
print("contrast issues:", check_semantic())
