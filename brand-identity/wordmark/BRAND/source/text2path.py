import io
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb

FONTS = "/tmp/hdwm/fonts/"
_cache = {}
def font(name, wght, axes=None):
    axes = axes or {}
    key = (name, wght, tuple(sorted(axes.items())))
    if key not in _cache:
        f = TTFont(FONTS + name + ".ttf")
        loc = {a.axisTag: (wght if a.axisTag == "wght" else axes.get(a.axisTag, a.defaultValue)) for a in f["fvar"].axes}
        inst = instantiateVariableFont(f, loc)
        buf = io.BytesIO(); inst.save(buf); data = buf.getvalue()
        _cache[key] = (TTFont(io.BytesIO(data)), data)
    return _cache[key]

def text_path(text, wght=700, cap_px=18.9, track=0.0, name="Rubik", axes=None):
    tt, data = font(name, wght, axes)
    upm = tt["head"].unitsPerEm
    cap = tt["OS/2"].sCapHeight or 0.7 * upm
    k = cap_px / cap
    face = hb.Face(data); hfont = hb.Font(face)
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(hfont, buf, {"kern": True, "liga": False})
    gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    x = 0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        tp = TransformPen(pen, (k, 0, 0, -k, (x + pos.x_offset) * k, 0))
        gs[order[info.codepoint]].draw(tp)
        x += pos.x_advance + track * upm
    return pen.getCommands(), (x - track * upm) * k
