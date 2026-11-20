"""Extra primitives for the refined kit: SVG charts, desktop shell, and new components (CSS + helpers)."""
import math
from uikit import *

def nice_max(v, ticks=4):
    """Round the axis top so every tick is a clean number (25, 50, 100, 250…)."""
    raw = v / ticks; mag = 10 ** math.floor(math.log10(raw))
    step = next(m*mag for m in (1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10) if m*mag >= raw)
    return step * ticks

def _smooth(pts):
    """Catmull-Rom → cubic Bézier path through points."""
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[i-1] if i else pts[i]; p1, p2 = pts[i], pts[i+1]; p3 = pts[i+2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0]-p0[0])/6, p1[1] + (p2[1]-p0[1])/6); c2 = (p2[0] - (p3[0]-p1[0])/6, p2[1] - (p3[1]-p1[1])/6)
        d += f"C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d

def _fmt(v):
    return f"{v:,.0f}" if abs(v) >= 1000 else f"{round(v, 1):g}"

def _tint(pct=26):
    """Past-period tint of the series colour, mixed against the surface so it works in both themes."""
    return f"color-mix(in oklab, var(--hd-chart) {pct}%, var(--hd-surface))"

def _axes(w, h, pl, pr, pt, pb, ymax, labels, X, ny=4):
    """Hairline grid in the SVG; axis labels as HTML so they stay 11.5px however the SVG scales."""
    Y = lambda v: pt + (1 - v/ymax)*(h-pt-pb)
    grid = "".join(f'<line x1="{pl}" x2="{w-pr}" y1="{Y(ymax*k/ny):.1f}" y2="{Y(ymax*k/ny):.1f}" class="gl{" base" if k == 0 else ""}" vector-effect="non-scaling-stroke"/>' for k in range(ny+1))
    yl = "".join(f'<span class="yl" style="right:{(w-pl+9)/w*100:.2f}%;top:{Y(ymax*k/ny)/h*100:.2f}%">{_fmt(ymax*k/ny)}</span>' for k in range(ny+1))
    xl = "".join(f'<span class="xl" style="left:{X(i)/w*100:.2f}%;top:{(h-pb+9)/h*100:.2f}%">{l}</span>' for i, l in enumerate(labels))
    return Y, grid, yl + xl

def line_chart(series, labels, w=640, h=220, ymax=None, compare=None, tip_i=None, uid="lc"):
    """Area/line chart: hairline grid, nice ticks, soft wash, dashed neutral comparison, end dot, hover marker + tooltip that sits clear of the data."""
    pl, pr, pt, pb = 40, 28, 30, 30
    ymax = nice_max(ymax or max(series + (compare or [])) * 1.05)
    X = lambda i: pl + i*(w-pl-pr)/(len(series)-1)
    Y, grid, lab = _axes(w, h, pl, pr, pt, pb, ymax, labels, X)
    pts = [(X(i), Y(v)) for i, v in enumerate(series)]
    line = _smooth(pts); area = line + f"L{pts[-1][0]:.1f} {h-pb}L{pts[0][0]:.1f} {h-pb}Z"
    cpts = [(X(i), Y(v)) for i, v in enumerate(compare)] if compare else None
    cmp = f'<path d="{_smooth(cpts)}" class="cmpl" vector-effect="non-scaling-stroke"/>' if cpts else ""
    xs = ""; dots = ""
    last = len(series) - 1
    if tip_i is not None:
        tx, ty = pts[tip_i]
        xs = f'<line x1="{tx:.1f}" x2="{tx:.1f}" y1="{pt-6}" y2="{h-pb}" class="xh" vector-effect="non-scaling-stroke"/>'
        if cpts: dots += f'<i class="cdot cmpd" style="left:{cpts[tip_i][0]/w*100:.2f}%;top:{cpts[tip_i][1]/h*100:.2f}%"></i>'
        dots += f'<i class="cdot hov" style="left:{tx/w*100:.2f}%;top:{ty/h*100:.2f}%"></i>'
    if tip_i != last:
        dots += f'<i class="cdot end" style="left:{pts[last][0]/w*100:.2f}%;top:{pts[last][1]/h*100:.2f}%"></i>'
    svg = (f'<svg viewBox="0 0 {w} {h}" width="100%" class="chart" aria-hidden="true"><defs><linearGradient id="{uid}g" x1="0" y1="0" x2="0" y2="1">'
           f'<stop offset="0" stop-color="var(--hd-chart)" stop-opacity=".16"/><stop offset="1" stop-color="var(--hd-chart)" stop-opacity="0"/></linearGradient></defs>'
           f'{grid}<path d="{area}" fill="url(#{uid}g)"/>{cmp}{xs}<path d="{line}" class="serl" vector-effect="non-scaling-stroke"/></svg>')
    tip = ""
    if tip_i is not None:
        tx, ty = pts[tip_i]
        below = ty < 44
        edge = " l" if tx < 70 else (" r" if tx > w - 70 else "")
        tip = (f'<div class="ctip{" below" if below else ""}{edge}" style="left:{tx/w*100:.2f}%;top:{ty/h*100:.2f}%"><span class="muted">{labels[tip_i]}</span>'
               f'<b class="num">{_fmt(series[tip_i])}</b>{f"<span class=muted>vs {_fmt(compare[tip_i])}</span>" if compare else ""}</div>')
    return f'<div class="cw">{svg}{lab}{dots}{tip}</div>'

def bar_chart(values, labels, w=640, h=200, hl=None, avg=False):
    """Columns: <=24px, 4px rounded tops, square at the baseline, past periods tinted, the current (hl, default last) solid; value on the cap."""
    pl, pr, pt, pb = 40, 8, 26, 30; ymax = nice_max(max(values) * 1.05); n = len(values)
    hl = n - 1 if hl is None else hl
    slot = (w-pl-pr)/n; bw = min(24, slot*0.56); r = 4
    X = lambda i: pl + (i+.5)*slot
    Y, grid, lab = _axes(w, h, pl, pr, pt, pb, ymax, labels, X)
    bars = ""; cap = ""
    for i, v in enumerate(values):
        cx = X(i); y = Y(v); x0, x1 = cx-bw/2, cx+bw/2
        col = "var(--hd-chart)" if i == hl else _tint(28)
        bars += f'<path d="M{x0:.1f} {h-pb}V{y+r:.1f}Q{x0:.1f} {y:.1f} {x0+r:.1f} {y:.1f}H{x1-r:.1f}Q{x1:.1f} {y:.1f} {x1:.1f} {y+r:.1f}V{h-pb}Z" style="fill:{col}"/>'
        if i == hl: cap += f'<span class="bv" style="left:{cx/w*100:.2f}%;top:{(y-6)/h*100:.2f}%">{_fmt(v)}</span>'
    ref = ""
    if avg:
        a = sum(values)/n; ref = f'<line x1="{pl}" x2="{w-pr}" y1="{Y(a):.1f}" y2="{Y(a):.1f}" class="avgl" vector-effect="non-scaling-stroke"/>'
    return f'<div class="cw"><svg viewBox="0 0 {w} {h}" width="100%" class="chart" aria-hidden="true">{grid}{ref}{bars}</svg>{lab}{cap}</div>'

def donut(parts, size=150, sw=18, center=("", "")):
    """Ring with round caps and a true 5px surface gap between parts (the caps are added to the dash, so the gap stays visible)."""
    r = (size - sw)/2; c = 2*math.pi*r; tot = sum(v for _, v, _ in parts); off = 0; segs = ""
    gv = 5
    for _, v, col in parts:
        ln = c*v/tot
        segs += (f'<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" '
                 f'stroke-dasharray="{max(ln-gv-sw,0.01):.2f} {c:.2f}" stroke-dashoffset="{-(off+(gv+sw)/2):.2f}" transform="rotate(-90 {size/2} {size/2})"/>')
        off += ln
    return (f'<div class="dn" style="width:{size}px;height:{size}px"><svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" aria-hidden="true">'
            f'<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="var(--hd-track)" stroke-width="{sw}" opacity=".5"/>{segs}</svg>'
            f'<div class="dc"><b class="num hero-num">{center[0]}</b><span class="t-cap muted">{center[1]}</span></div></div>')

def spark(values, w=84, h=26, col="var(--hd-chart)"):
    mx, mn = max(values), min(values); X = lambda i: i*(w-6)/(len(values)-1)+2; Y = lambda v: 4 + (1-(v-mn)/(mx-mn or 1))*(h-8)
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true"><path d="{_smooth([(X(i), Y(v)) for i, v in enumerate(values)])}" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="{X(len(values)-1):.1f}" cy="{Y(values[-1]):.1f}" r="2.6" fill="{col}"/></svg>')

def spark_area(values, w=240, h=44, uid="sa", col="var(--hd-chart)"):
    """Full-width sparkline: 2px line, soft wash fading out, end dot with a halo (HTML so it stays round)."""
    mx, mn = max(values), min(values); X = lambda i: i*w/(len(values)-1); Y = lambda v: 6 + (1-(v-mn)/(mx-mn or 1))*(h-12)
    line = _smooth([(X(i), Y(v)) for i, v in enumerate(values)]); area = line + f"L{w} {h}L0 {h}Z"
    ly = Y(values[-1]) / h * 100
    return (f'<svg class="spa" viewBox="0 0 {w} {h}" preserveAspectRatio="none" width="100%" height="{h}" aria-hidden="true"><defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{col}" stop-opacity=".18"/><stop offset=".9" stop-color="{col}" stop-opacity="0"/></linearGradient></defs>'
            f'<path d="{area}" fill="url(#{uid})"/><path d="{line}" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"/></svg>'
            f'<i class="spk-dot" style="top:{ly:.1f}%"></i>')

def delta_text(delta, up=True):
    if not delta: return ""
    return f'<span class="dtext {"up" if up else "dn"}">{delta}</span>'

def mini_bars(values, hl=None, h=40):
    """Counts per period: past periods tinted, the current one solid; 4px rounded tops, square on the baseline."""
    hl = len(values) - 1 if hl is None else hl; mx = max(values) or 1
    return '<div class="mbars">' + "".join(f'<i style="height:{max(v/mx*100, 8):.0f}%" class="{"hl" if i == hl else ""}"></i>' for i, v in enumerate(values)) + '</div>'

STAR18 = "M16.963,6.786c-.088-.271-.323-.469-.605-.51l-4.62-.671L9.672,1.418c-.252-.512-1.093-.512-1.345,0l-2.066,4.186-4.62,.671c-.282,.041-.517,.239-.605,.51-.088,.271-.015,.57,.19,.769l3.343,3.258-.79,4.601c-.048,.282,.067,.566,.298,.734,.231,.167,.538,.189,.79,.057l4.132-2.173,4.132,2.173c.11,.058,.229,.086,.349,.086,.155,0,.31-.048,.441-.143,.231-.168,.347-.452,.298-.734l-.79-4.601,3.343-3.258c.205-.199,.278-.498,.19-.769Z"
def partial_star(frac, uid, size=18):
    """One star filled to exactly `frac` of its width: a hard-stop gradient across the glyph's own bounding box (no clip, no mask)."""
    frac = max(0.0, min(1.0, frac)); g = f"ps{uid}"
    fill = "var(--hd-star)" if frac >= .999 else ("var(--hd-empty)" if frac <= .001 else f"url(#{g})")
    defs = "" if fill.startswith("var") else (f'<defs><linearGradient id="{g}" x1="0" x2="1" y1="0" y2="0"><stop offset="{frac:.3f}" stop-color="var(--hd-star)"/>'
                                              f'<stop offset="{frac:.3f}" stop-color="var(--hd-empty)"/></linearGradient></defs>')
    return f'<svg class="pst" width="{size}" height="{size}" viewBox="0 0 18 18" aria-hidden="true">{defs}<path d="{STAR18}" fill="{fill}"/></svg>'

def _rating_hist(r):
    """Plausible 1-5 star distribution centred on the average (used only when the caller gives none)."""
    wts = [math.exp(-((k - r)**2) / 1.5) for k in range(1, 6)]; m = max(wts)
    return [w_/m for w_ in wts]

def stat(label, value, delta=None, up=True, note="", spark=None, unit="", uid="st", compact=False, kind=None, extra=None):
    """Stat card, customised by what the number is.
    kind: spark (trend) · bars (counts per period) · rating · compare (vs previous) · split (breakdown) · none."""
    kind = kind or ("spark" if spark else "none")
    body = ""
    if kind == "spark": body = f'<div class="spk">{spark_area(spark, uid=uid)}</div>'
    elif kind == "bars": body = mini_bars(spark)
    elif kind == "rating":
        r = float(value)
        stars = "".join(partial_star(max(0, min(1, r - i)), f"{uid}{i}") for i in range(5))
        hist = extra if extra else _rating_hist(r); hm = max(hist) or 1; top = hist.index(hm)
        hbars = "".join(f'<i class="{"hl" if k == top else ""}" style="height:{max(h_/hm*100, 20):.0f}%"></i>' for k, h_ in enumerate(hist))
        body = f'<div class="srate">{stars}</div><div class="rhist">{hbars}</div>'
    elif kind == "compare":
        cur, prev = extra
        mx = max(cur, prev)
        body = (f'<div class="cmp2"><div><span>Now</span><div class="bar thin"><i style="width:{cur/mx*100:.0f}%"></i></div><b class="num">₹{cur:,}</b></div>'
                f'<div class="pv"><span>Before</span><div class="bar thin"><i style="width:{prev/mx*100:.0f}%"></i></div><b class="num">₹{prev:,}</b></div></div>')
    elif kind == "split":
        parts = extra
        body = ('<div class="bar multi">' + "".join(f'<i style="width:{p}%;background:{c}"></i>' for _, p, c in parts) + '</div>'
                '<div class="legend">' + "".join(f'<span><i style="background:{c}"></i>{n}</span>' for n, _, c in parts) + '</div>')
    return (f'<div class="panel stat{" compact" if compact else ""} k-{kind}"><div class="sh"><span class="sl">{label}</span>{delta_text(delta, up)}</div><div class="sv"><b class="num">{value}</b>{f"<span class=su>{unit}</span>" if unit else ""}</div>'
            f'{f"<div class=vz>{body}</div>" if body else ""}</div>')

def goal(label, done, total, note="", right="", variant="segs"):
    """Goal: value / total with 12 segments, or variant="ring" for a ring beside the value. Text never clips."""
    if variant == "ring":
        pct = round(done/total*100)
        return (f'<div class="panel stat k-goal k-goalring"><div class="sh"><span class="sl">{label}</span></div><div class="gr"><div class="sv"><b class="num">{done}</b><span class="su">/ {total}</span></div>'
                f'{ring(pct, 52, 6)}</div></div>')
    return (f'<div class="panel stat k-goal"><div class="sh"><span class="sl">{label}</span></div><div class="sv"><b class="num">{done}</b><span class="su">/ {total}</span></div>'
            f'<div class="vz">{segs(done/total)}</div></div>')

def segs(frac, n=12):
    """Segmented progress: n rounded cells, filled cells solid Cobalt, the boundary cell partially filled."""
    full = round(frac * n); part = 0  # slots are discrete: no partial cells
    return '<div class="segs">' + "".join(f'<i class="{"on" if i < full else ""}">{f"<b style=width:{part*100:.0f}%></b>" if i == full and part > .05 else ""}</i>' for i in range(n)) + '</div>'

def ring(pct, size=44, sw=4, label=None):
    r = (size-sw)/2; c = 2*math.pi*r
    arc = f'<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="var(--hd-chart)" stroke-width="{sw}" stroke-linecap="round" stroke-dasharray="{max(c*pct/100, .01):.1f} {c:.1f}" transform="rotate(-90 {size/2} {size/2})"/>' if pct > 0 else ""
    return (f'<span class="ringw" style="width:{size}px;height:{size}px"><svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" style="position:absolute;inset:0" aria-hidden="true">'
            f'<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="var(--hd-track)" stroke-width="{sw}"/>{arc}</svg>'
            + (ic("check", size*0.45, "var(--hd-accent)", 2.4) if label == "✓" else f'<b class="num" style="font-size:{size*0.27:.0f}px">{label if label is not None else f"{pct}%"}</b>') + '</span>')

def kbd(t): return f'<kbd class="kbd">{t}</kbd>'

CSS2 = f"""
/* stat anatomy (one grid for every kind): label row · value · a fixed 44px visual zone pinned to the bottom, same inset */
.stat:not(.compact) {{ padding: 14px 16px 14px; gap: 0; }}
.stat:not(.compact) .sv {{ margin-top: 6px; }} .stat:not(.compact) .sv b {{ font-size: 28px; }}
.stat .vz {{ margin-top: auto; padding-top: 10px; }}
.stat:not(.compact) .vz {{ height: 46px; display: flex; flex-direction: column; justify-content: flex-end; }}
.stat .vz .spk {{ margin: 0; height: 36px; }} .stat .vz .spk svg {{ width: 100%; height: 36px; display: block; }}
.stat .vz .mbars {{ margin: 0; height: 36px; }}
.stat .vz .srate {{ margin: 0; gap: 4px; }} .stat .vz .srate .ic {{ width: 18px; height: 18px; }} .stat .vz .halfstar {{ width: 18px; }}
.stat .vz .cmp2 {{ margin: 0; gap: 6px; }} .stat .vz .bar.seg, .stat .vz .bar.multi {{ margin: 0; }}
.stat.compact .vz {{ padding-top: 8px; }}
.pg .ph .t .t-h1 {{ font-size: 30px; line-height: 34px; letter-spacing: -0.035em; font-variation-settings: 'opsz' 96; }} .pg .ph .t p {{ font-size: 15px; margin-top: 6px; }}
/* repeated statuses in tables/lists read calmer tinted (strong text, AA); a lone status stays solid */
.tbl .badge, .rv .badge {{ box-shadow: none; }}
.tbl .badge.success, .rv .badge.success {{ background: var(--hd-success-subtle); color: var(--hd-success-strong); }}
.tbl .badge.warning, .rv .badge.warning {{ background: var(--hd-warning-subtle); color: var(--hd-warning-strong); }}
.tbl .badge.neutral, .rv .badge.neutral {{ background: var(--hd-control); color: var(--hd-fg-muted); }}
.tbl tr.sel-row td {{ background: var(--hd-accent-subtle) !important; }}
/* latest reviews: a readable list, not a sparse table */
.rvs {{ display: flex; flex-direction: column; }}
.rv {{ display: grid; grid-template-columns: 40px 210px 1fr 86px 88px 36px; align-items: center; gap: 14px; padding: 12px 18px; border-top: 1px solid var(--hd-border); }}
.rv-av {{ width: 40px; height: 40px; border-radius: 50%; object-fit: cover; display: block; }}
.rv-who b {{ display: flex; align-items: center; gap: 4px; font-size: 14px; font-weight: 600; }}
.rv-who small {{ display: flex; align-items: center; gap: 5px; font-size: 12.5px; color: var(--hd-fg-muted); margin-top: 3px; }}
.rv-who small img {{ width: 16px; height: 16px; border-radius: 4px; object-fit: cover; }}
.rv-q {{ margin: 0; font-size: 13.5px; line-height: 19px; color: var(--hd-fg-muted); display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }}
.rv-st {{ display: flex; gap: 2px; }} .rv .badge {{ justify-self: start; }} .rv-t {{ font-size: 12.5px; color: var(--hd-fg-subtle); text-align: right; }}

/* tabs & badges polish */
.cnt-b {{ display: inline-flex; align-items: center; height: 18px; padding: 0 6px; border-radius: 6px; font-size: 11.5px; font-weight: 550; font-variant-numeric: tabular-nums; background: var(--hd-bg-subtle); color: var(--hd-fg-muted); box-shadow: inset 0 0 0 1px var(--hairline); margin-left: 2px; }}
.tabs > .on .cnt-b {{ background: var(--hd-accent); color: #fff; box-shadow: none; }}
.bdot {{ width: 6px; height: 6px; border-radius: 50%; background: currentColor; display: inline-block; margin-right: 1px; }}
.badge.solid {{ background: var(--hd-accent); color: #fff; min-width: 20px; justify-content: center; }}
/* looping demos (kit only) */
.tapeanim i {{ animation: tapepull 1.6s linear infinite; }} @keyframes tapepull {{ from {{ width: 0; }} to {{ width: 100%; }} }}
.arrive {{ animation: arrive 2.4s var(--ease-out) infinite; }} @keyframes arrive {{ 0% {{ opacity: 0; transform: translateY(8px); }} 12%, 80% {{ opacity: 1; transform: none; }} 100% {{ opacity: 0; }} }}
.shimmer {{ background-size: 200% 100%; animation: shimmer 1.4s linear infinite; }} @keyframes shimmer {{ from {{ background-position: 200% 0; }} to {{ background-position: -200% 0; }} }}
@media (prefers-reduced-motion: reduce) {{ .tapeanim i, .arrive, .shimmer {{ animation: none; }} .tapeanim i {{ width: 60%; }} }}
/* stat cards */
.stat {{ padding: 16px 16px 14px; display: flex; flex-direction: column; gap: 6px; position: relative; overflow: hidden; }}
.stat .sl {{ font-size: 13px; font-weight: 500; color: var(--hd-fg-muted); letter-spacing: -.005em; }}
.stat .sh {{ display: flex; align-items: baseline; justify-content: space-between; }}
.stat .sv {{ display: flex; align-items: baseline; gap: 6px; margin-top: 2px; }} .stat .sv b {{ font: 600 28px/1.05 var(--font-ui); letter-spacing: -.035em; }}
.stat .su {{ font-size: 15px; font-weight: 500; color: var(--hd-fg-muted); }}
.stat .sd {{ display: flex; align-items: center; gap: 6px; min-height: 20px; }} .stat .sf {{ font-size: 12.5px; color: var(--hd-fg-muted); }}
.dpill {{ display: inline-flex; align-items: center; height: 20px; font-size: 12px; line-height: 1; font-weight: 600; padding: 0 6px; border-radius: 6px; font-variant-numeric: tabular-nums; }}
.dpill.up {{ background: {N['700']}; color: #fff; }} .dpill.dn {{ background: {V['600']}; color: #fff; }}
.stat .spk {{ margin: 6px -16px -14px; line-height: 0; }}
.stat.compact {{ padding: 12px 12px 11px; gap: 3px; }} .stat.compact .sl {{ font-size: 12px; }} .stat.compact .sv b {{ font-size: 19px; letter-spacing: -.03em; }} .stat.compact .sd {{ min-height: 0; }}
.dtext {{ font-size: 12.5px; font-weight: 550; font-variant-numeric: tabular-nums; white-space: nowrap; }} .dtext.up {{ color: var(--hd-success); }} .dtext.dn {{ color: var(--hd-danger); }}
.mbars {{ display: flex; align-items: flex-end; gap: 4px; height: 40px; margin-top: 6px; }} .mbars i {{ flex: 1; border-radius: 4px 4px 1px 1px; background: var(--hd-track); }} .mbars i.hl {{ background: var(--hd-accent); }}
.srate {{ display: flex; gap: 3px; margin-top: 6px; }} .halfstar {{ display: inline-flex; position: relative; width: 16px; overflow: hidden; -webkit-mask: linear-gradient(90deg, #000 70%, rgba(0,0,0,.25) 70%); mask: linear-gradient(90deg, #000 70%, rgba(0,0,0,.25) 70%); }}
.cmp2 {{ display: flex; flex-direction: column; gap: 6px; margin-top: 6px; }} .cmp2 > div {{ display: grid; grid-template-columns: 44px 1fr 52px; align-items: center; gap: 8px; font-size: 12px; color: var(--hd-fg-muted); }}
.stat.k-split .legend {{ font-size: 12px; gap: 10px; }}
/* progress bars */
.bar {{ height: 8px; border-radius: 999px; background: var(--hd-track); overflow: hidden; display: flex; gap: 2px; }}
.bar i {{ display: block; height: 100%; border-radius: 999px; background: var(--hd-accent); }}
.bar.thin {{ height: 4px; }} .bar.seg {{ -webkit-mask: repeating-linear-gradient(90deg, #000 0 calc(10% - 2px), transparent calc(10% - 2px) 10%); mask: repeating-linear-gradient(90deg, #000 0 calc(10% - 2px), transparent calc(10% - 2px) 10%); border-radius: 4px; }}
.bar.seg i {{ border-radius: 0; }} .bar.multi {{ background: transparent; }} .bar.multi i {{ border-radius: 2px; }} .bar.multi i:first-child {{ border-radius: 999px 2px 2px 999px; }} .bar.multi i:last-child {{ border-radius: 2px 999px 999px 2px; }}
.barlab {{ display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 8px; }} .barlab b {{ font-weight: 550; }} .barlab span {{ color: var(--hd-fg-muted); font-variant-numeric: tabular-nums; }}
.ringcard {{ padding: 16px; display: flex; gap: 14px; align-items: center; }}
/* charts */
.chart text.ax {{ font: 500 11px var(--font-ui); fill: var(--hd-fg-subtle); }} .chart text.ax.strong {{ fill: var(--hd-fg); font-weight: 600; }}
.ctip {{ position: absolute; transform: translate(-50%, calc(-100% - 12px)); background: var(--hd-inverse); color: var(--hd-inverse-fg); border-radius: 10px; padding: 7px 10px; font-size: 12px; display: flex; flex-direction: row; align-items: baseline; gap: 8px; white-space: nowrap; box-shadow: var(--hd-shadow-e2); pointer-events: none; }}
.ctip b {{ font-size: 14px; font-weight: 600; }} .ctip.below {{ transform: translate(-50%, 12px); }} .ctip .muted {{ color: color-mix(in oklab, var(--hd-inverse-fg) 65%, transparent); }}
.legend {{ display: flex; gap: 14px; font-size: 12.5px; color: var(--hd-fg-muted); align-items: center; }} .legend i {{ width: 10px; height: 10px; border-radius: 4px; display: inline-block; margin-right: 6px; vertical-align: -1px; }}
.legend .dash {{ width: 14px; height: 0; border-top: 1.5px dashed var(--hd-fg-subtle); border-radius: 0; }}
/* desktop shell */
.shell {{ width: 1440px; height: 900px; border-radius: 14px; overflow: hidden; box-shadow: 0 8px 28px rgba(16,20,38,.05); display: grid; grid-template-columns: 252px 1fr; grid-template-rows: minmax(0, 1fr); background: var(--hd-canvas); border: 1px solid var(--hairline); color: var(--hd-fg); }}
.sb {{ background: var(--hd-bg-subtle); border-right: 1px solid var(--hairline); padding: 14px 12px; display: flex; flex-direction: column; gap: 2px; }}
.ws {{ display: flex; align-items: center; gap: 10px; padding: 8px; border-radius: 10px; }} .ws img {{ width: 28px; height: 28px; }} .ws b {{ font-size: 14px; font-weight: 600; display: block; letter-spacing: -.01em; }} .ws small {{ font-size: 12px; color: var(--hd-fg-muted); }}
.sbsearch {{ display: flex; align-items: center; gap: 8px; height: 34px; margin: 8px 0 10px; padding: 0 10px; border-radius: 8px; background: var(--hd-surface); border: 1px solid var(--hairline); color: var(--hd-fg-subtle); font-size: 13.5px; box-shadow: var(--hd-shadow-e1); }}
.sbsearch .kbd {{ margin-left: auto; }}
.sbh {{ font-size: 12px; font-weight: 550; color: var(--hd-fg-subtle); padding: 12px 10px 4px; }}
.nav {{ display: flex; align-items: center; gap: 10px; height: 34px; padding: 0 10px; border-radius: 8px; font-size: 14px; font-weight: 500; color: var(--hd-fg-muted); letter-spacing: -.01em; }}
.nav .ic {{ color: var(--hd-fg-subtle); }} .nav .cnt {{ margin-left: auto; font-size: 12px; font-weight: 550; color: var(--hd-fg-subtle); font-variant-numeric: tabular-nums; }}
.nav.on {{ background: var(--hd-surface-raised); color: var(--hd-fg); box-shadow: var(--hd-shadow-e1), 0 0 0 1px var(--hairline); }} .nav.on .ic {{ color: var(--hd-accent); }}
.nav .cnt.hot {{ background: var(--hd-accent); color: #fff; border-radius: 6px; padding: 1px 6px; }}
.sbfoot {{ margin-top: auto; display: flex; flex-direction: column; gap: 2px; }}
.me {{ display: flex; align-items: center; gap: 10px; padding: 8px; border-radius: 10px; margin-top: 6px; border-top: 1px solid var(--hairline); padding-top: 12px; }} .me b {{ font-size: 13.5px; font-weight: 550; display: block; }} .me small {{ font-size: 12px; color: var(--hd-fg-muted); }}
.mn {{ display: flex; flex-direction: column; min-width: 0; min-height: 0; overflow: hidden; }} .panel > .sb {{ flex: 1; border-right: 0; }} .sb {{ min-height: 0; overflow: hidden; }}
.hdr {{ height: 52px; display: flex; align-items: center; gap: 12px; padding: 0 28px; border-bottom: 1px solid var(--hairline); background: var(--hd-surface); }}
.crumb {{ display: flex; align-items: center; gap: 6px; font-size: 13.5px; color: var(--hd-fg-muted); }} .crumb b {{ color: var(--hd-fg); font-weight: 550; }} .crumb .ic {{ color: var(--hd-fg-subtle); }}
.hdr .sp {{ flex: 1; }} .iconbtn {{ width: 34px; height: 34px; border-radius: 8px; display: inline-flex; align-items: center; justify-content: center; color: var(--hd-fg-muted); position: relative; }}
.iconbtn .badge-dot {{ position: absolute; top: 7px; right: 8px; width: 7px; height: 7px; border-radius: 50%; background: var(--hd-data-hl); box-shadow: 0 0 0 2px var(--hd-canvas); }}
.pg {{ padding: 24px 28px; display: flex; flex-direction: column; gap: 18px; overflow: hidden; }}
.ph {{ display: flex; align-items: flex-end; gap: 12px; }} .ph .t {{ flex: 1; }} .ph .t p {{ margin: 4px 0 0; font-size: 14px; color: var(--hd-fg-muted); }}
.kbd {{ font: 500 11.5px var(--font-ui); min-width: 20px; height: 20px; padding: 0 5px; border-radius: 6px; background: var(--hd-surface); color: var(--hd-fg-muted); box-shadow: inset 0 0 0 1px var(--hd-border), inset 0 -1px 0 var(--hd-border); display: inline-flex; align-items: center; justify-content: center; }}
.panel {{ background: var(--hd-surface-raised); border: 1px solid var(--hairline); border-radius: 16px; box-shadow: var(--hd-shadow-e1); }}
.panel > .phd {{ display: flex; align-items: center; gap: 10px; padding: 16px 18px 6px; }} .panel > .phd b {{ font-size: 15px; font-weight: 600; letter-spacing: -.012em; flex: 1; }}
.kpi2 {{ padding: 14px 16px; display: grid; grid-template-columns: 1fr auto; grid-template-rows: auto auto auto; column-gap: 8px; }} .kpi2 small {{ font-size: 12.5px; color: var(--hd-fg-muted); font-weight: 500; grid-column: 1 / -1; }}
.kpi2 b {{ font-size: 26px; font-weight: 600; letter-spacing: -.03em; margin-top: 4px; }} .kpi2 svg {{ align-self: end; grid-row: 2 / 4; grid-column: 2; }} .kpi2 .delta {{ grid-column: 1 / -1; white-space: nowrap; margin-top: 2px; }}
/* segmented-free filters: toolbar */
.toolbar {{ display: flex; align-items: center; gap: 8px; }}
/* more components */
.acc {{ border-radius: 14px; overflow: hidden; }} .acc .ai {{ padding: 14px 16px; display: flex; align-items: center; gap: 10px; font-size: 14.5px; font-weight: 550; }} .acc .ai + .ai, .acc .ab + .ai {{ border-top: 1px solid var(--hairline); }}
.acc .ab {{ padding: 0 16px 14px 16px; font-size: 13.5px; line-height: 20px; color: var(--hd-fg-muted); margin-top: -4px; }}
.pager {{ display: flex; align-items: center; gap: 4px; }} .pager span {{ min-width: 32px; height: 32px; border-radius: 8px; display: inline-flex; align-items: center; justify-content: center; font-size: 13.5px; font-weight: 500; color: var(--hd-fg-muted); }}
.pager .on {{ background: var(--hd-surface-raised); color: var(--hd-fg); box-shadow: 0 0 0 1px var(--hd-border), var(--hd-shadow-e1); }}
.qty {{ display: inline-flex; align-items: center; height: 40px; border-radius: 12px; border: 1px solid var(--hd-border); background: var(--hd-surface); }} .qty span {{ width: 40px; height: 100%; display: flex; align-items: center; justify-content: center; color: var(--hd-fg-muted); }} .qty b {{ min-width: 36px; text-align: center; font-weight: 600; }}
.cal {{ width: 280px; padding: 14px; }} .cal .cg {{ display: grid; grid-template-columns: repeat(7, 1fr); gap: 2px; text-align: center; font-size: 13px; }}
.cal .cg span {{ height: 34px; display: flex; align-items: center; justify-content: center; border-radius: 8px; font-variant-numeric: tabular-nums; }} .cal .cg .dw {{ font-size: 11.5px; color: var(--hd-fg-subtle); height: 24px; }}
.cal .cg .mute {{ color: var(--hd-fg-subtle); opacity: .55; }} .cal .cg .rng {{ background: var(--hd-control); border-radius: 0; }} .cal .cg .sel {{ background: var(--hd-accent); color: #fff; font-weight: 600; }} .cal .cg .today {{ box-shadow: inset 0 0 0 1px var(--hd-border-strong); }}
.upl {{ display: flex; align-items: center; gap: 12px; padding: 10px 12px; }} .upl .tx {{ flex: 1; min-width: 0; }} .upl .tx b {{ font-size: 13.5px; font-weight: 550; display: block; }} .upl .tx small {{ font-size: 12px; color: var(--hd-fg-muted); }}
.upl .tape {{ height: 4px; margin-top: 6px; }}
.ticket {{ position: relative; border-radius: 16px; display: grid; grid-template-columns: 1fr 112px; filter: drop-shadow(0 0 0.5px rgba(16,20,38,.45)) drop-shadow(0 1px 1px rgba(16,20,38,.06)) drop-shadow(0 2px 3px rgba(16,20,38,.04)); }}
[data-theme="dark"] .ticket {{ filter: drop-shadow(0 0 0.6px rgba(255,255,255,.35)); }}
.ticket .tl {{ padding: 16px; border-radius: 16px 0 0 16px; background: radial-gradient(circle at 100% 0, transparent 9px, var(--hd-surface) 9.5px) top / 100% 51% no-repeat, radial-gradient(circle at 100% 100%, transparent 9px, var(--hd-surface) 9.5px) bottom / 100% 51% no-repeat; }}
.ticket .tr {{ position: relative; border-radius: 0 16px 16px 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px;
  background: radial-gradient(circle at 0 0, transparent 9px, var(--hd-bg-subtle) 9.5px) top / 100% 51% no-repeat, radial-gradient(circle at 0 100%, transparent 9px, var(--hd-bg-subtle) 9.5px) bottom / 100% 51% no-repeat; }}
.ticket .tr::before {{ content: ''; position: absolute; left: 0; top: 14px; bottom: 14px; border-left: 1.5px dashed var(--hd-border-strong); }}
.rcard {{ padding: 14px; display: flex; flex-direction: column; gap: 10px; }} .rcard .rh {{ display: flex; align-items: center; gap: 10px; }} .rcard .rh b {{ font-size: 14px; font-weight: 600; display: block; }} .rcard .rh small {{ font-size: 12px; color: var(--hd-fg-muted); }}
.rcard p {{ margin: 0; font-size: 14px; line-height: 21px; }} .rcard .media {{ display: flex; gap: 8px; }} .rcard .media img {{ width: 72px; height: 72px; }}
.cmdk {{ width: 520px; border-radius: 16px; background: var(--hd-surface); box-shadow: var(--hd-shadow-e3), 0 0 0 1px var(--hairline); overflow: hidden; }}
.cmdk .cin {{ display: flex; align-items: center; gap: 10px; height: 52px; padding: 0 16px; border-bottom: 1px solid var(--hairline); font-size: 15px; }}
.cmdk .cgp {{ padding: 8px; }} .cmdk .cgh {{ font-size: 12px; font-weight: 550; color: var(--hd-fg-subtle); padding: 6px 10px; }}
.cmdk .ci {{ display: flex; align-items: center; gap: 10px; height: 40px; padding: 0 10px; border-radius: 10px; font-size: 14px; }} .cmdk .ci.hl {{ background: var(--hd-bg-subtle); }} .cmdk .ci .kbd {{ margin-left: auto; }}
.cmdk .ci img {{ width: 24px; height: 24px; border-radius: 6px; }}
.cmdk .cft {{ display: flex; gap: 14px; padding: 10px 16px; border-top: 1px solid var(--hairline); font-size: 12px; color: var(--hd-fg-subtle); align-items: center; }}
.drawer {{ width: 380px; background: var(--hd-surface); border-left: 1px solid var(--hairline); box-shadow: var(--hd-shadow-e3); padding: 20px; display: flex; flex-direction: column; gap: 14px; }}
.banner {{ display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 16px; background: var(--hd-surface-raised); box-shadow: var(--hd-shadow-e1); }}
.banner .bi {{ width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex: none; }} .banner .tx {{ flex: 1; }} .banner .tx b {{ font-size: 14px; font-weight: 600; display: block; }} .banner .tx small {{ font-size: 12.5px; color: var(--hd-fg-muted); }}
.tagin {{ min-height: 44px; border: 1px solid var(--hd-border-input); border-radius: 12px; padding: 6px; display: flex; flex-wrap: wrap; gap: 6px; align-items: center; background: var(--hd-surface); }}
.tag {{ height: 28px; padding: 0 6px 0 10px; border-radius: 8px; background: var(--hd-bg-subtle); box-shadow: inset 0 0 0 1px var(--hd-border); display: inline-flex; align-items: center; gap: 4px; font-size: 13px; font-weight: 500; }} .tag .ic {{ color: var(--hd-fg-subtle); }}
.toasts {{ position: relative; height: 76px; width: 340px; margin-top: 4px; }} .toasts .toast {{ position: absolute; left: 0; right: 0; bottom: 0; transform-origin: 50% 0; }} .toasts .toast:nth-child(1) {{ transform: translateY(-16px) scale(.9); opacity: .45; }}
.toasts .toast:nth-child(2) {{ transform: translateY(-8px) scale(.95); opacity: .75; }}
.th-sort {{ display: inline-flex; align-items: center; gap: 4px; }} .sel-row td {{ background: var(--hd-accent-subtle); }}
.avst {{ position: relative; display: inline-flex; }} .avst i {{ position: absolute; right: 0; bottom: 0; width: 11px; height: 11px; border-radius: 50%; background: var(--hd-success-solid); box-shadow: 0 0 0 2px var(--hd-surface); }}
.pop {{ position: relative; padding: 14px; width: 260px; }} .pop::before {{ content: ''; position: absolute; top: -6px; left: 28px; width: 12px; height: 12px; background: var(--hd-surface-raised); border-left: 1px solid var(--hairline); border-top: 1px solid var(--hairline); transform: rotate(45deg); }}

/* ---- desktop pass: one primary CTA in the page header, grey filled controls, review queue layout ---- */
:root, [data-theme] {{ --hd-chart: var(--hd-accent); }} [data-theme="dark"] {{ --hd-chart: var(--hd-data-1); }}
.shell .ph .btn.sm, .shell .ph .chip {{ height: 44px; border-radius: 12px; font-size: 14px; padding: 0 16px; }}
.shell .ph .btn.sm:has(> .ic:first-child) {{ padding-left: 14px; }} .shell .ph .btn.p.sm {{ box-shadow: inset 0 -1px 0 var(--hd-accent-pressed); }}
.shell .ph .chip, .shell .toolbar .chip, .shell .toolbar .chip.on {{ background: var(--hd-control); border: 0; box-shadow: none; color: var(--hd-fg); font-weight: 550; }}
.shell .toolbar .chip, .shell .toolbar .btn.sm {{ height: 36px; border-radius: 10px; }}
.shell .toolbar .chip .ic {{ color: var(--hd-fg-muted); }}
.shell .toolbar .chip img {{ border-radius: 6px; }}
.shell .ph .chip .ic {{ color: var(--hd-fg-muted); }}
.shell .mn > .pg {{ flex: 1; min-height: 0; }}
/* overview: latest reviews as separate row cards */
.sect .shd {{ display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }} .sect .shd .l {{ flex: 1; display: flex; align-items: baseline; gap: 10px; }} .sect .shd b.t {{ font-size: 15px; font-weight: 600; letter-spacing: -.012em; }}
.shell .sect .rvs {{ gap: 8px; }}
.shell .rv {{ border: 1px solid var(--hairline); border-radius: 12px; background: var(--hd-surface-raised); padding: 10px 16px; }}
.shell .rv-av {{ width: 40px; height: 40px; }}
/* donut card */
.dcard {{ display: flex; flex-direction: column; }} .dcard .db {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 14px; padding: 4px 22px 18px; }}
.lgd {{ width: 100%; display: flex; flex-direction: column; gap: 10px; }} .lgd > div {{ display: flex; align-items: center; gap: 10px; font-size: 13.5px; }} .lgd i {{ width: 8px; height: 8px; border-radius: 4px; flex: none; }} .lgd span {{ flex: 1; }} .lgd b {{ font-weight: 600; font-variant-numeric: tabular-nums; }}
/* campaigns bulk bar */
.shell .tblwrap {{ position: relative; overflow: hidden; padding-bottom: 68px; }}
.bulk {{ position: absolute; left: 50%; bottom: 12px; transform: translateX(-50%); height: 44px; display: flex; align-items: center; gap: 8px; padding: 0 6px 0 16px; border-radius: 12px; background: var(--hd-surface-raised); box-shadow: var(--hd-shadow-e2), 0 0 0 1px var(--hairline); white-space: nowrap; }}
.bulk .btn.sm {{ height: 32px; }} .bulk .t-small {{ margin-right: 6px; }}
/* review queue */
.shell .pg:has(> .rvw) {{ padding: 0; gap: 0; }}
.rvw {{ flex: 1; min-height: 0; display: grid; grid-template-columns: minmax(0, 1fr) 380px; grid-template-rows: minmax(0, 1fr); }}
.rvl {{ padding: 24px 28px 0; display: flex; flex-direction: column; gap: 16px; min-height: 0; min-width: 0; overflow: hidden; }}
.rvlist {{ display: flex; flex-direction: column; gap: 8px; flex: 1; min-height: 0; overflow: hidden; padding: 2px 2px 16px; margin: -2px -2px 0; }}
.shell .rc2 {{ height: 112px; flex: none; box-sizing: border-box; display: grid; grid-template-columns: 22px 36px minmax(0, 1fr) auto; column-gap: 14px; align-items: start; padding: 12px 16px; border-radius: 12px; box-shadow: none; background: var(--hd-surface-raised); }}
.rc2 .check {{ margin-top: 7px; }} .rc2 > img.av {{ width: 36px; height: 36px; border-radius: 50%; object-fit: cover; margin-top: 2px; }}
.rc2 .bd {{ min-width: 0; display: flex; flex-direction: column; gap: 2px; }}
.rc2 .l1 {{ display: flex; align-items: center; gap: 10px; }} .rc2 .l1 b {{ font-size: 14px; font-weight: 600; display: inline-flex; align-items: center; gap: 4px; }} .rc2 .l1 .stars {{ gap: 1px; }}
.rc2 .l2 {{ font-size: 12.5px; color: var(--hd-fg-muted); }} .rc2 .bd p {{ margin: 4px 0 0; font-size: 13.5px; line-height: 19px; color: var(--hd-fg); display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }}
.rc2 .th {{ display: flex; gap: 8px; }} .rc2 .th img {{ width: 72px; height: 72px; border-radius: 8px; object-fit: cover; }}
.shell .rc2.chk {{ background: var(--hd-accent-subtle); }}
.shell .rc2.open {{ box-shadow: 0 0 0 2px var(--hd-accent) !important; border-color: transparent; }}
.shell .drawer {{ box-shadow: none; height: 100%; box-sizing: border-box; min-height: 0; overflow: hidden; padding: 20px; gap: 14px; }}
.drawer .rvtxt {{ display: flex; flex-direction: column; gap: 8px; }} .drawer .rvtxt p {{ margin: 0; font-size: 14px; line-height: 21px; }}
.drawer .rvtxt .th {{ display: flex; gap: 8px; }} .drawer .rvtxt .th img {{ width: 72px; height: 72px; border-radius: 8px; object-fit: cover; }}
.drawer .dl {{ display: flex; flex-direction: column; gap: 8px; }}
.drawer .sec-l {{ font-size: 12.5px; font-weight: 550; color: var(--hd-fg-subtle); }}
.stat .cmp2 b {{ font-size: 12px; font-weight: 600; color: var(--hd-fg); text-align: right; }}
.stat .sh {{ min-width: 0; gap: 8px; }} .stat .sl {{ white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-width: 0; }} .stat .dtext {{ flex: none; }}
.stat:not(.compact) .sh {{ height: 18px; align-items: center; }} .stat:not(.compact) > .sl {{ display: block; height: 18px; line-height: 18px; }}
.stat:not(.compact) .sv {{ height: 30px; align-items: baseline; }}
"""
