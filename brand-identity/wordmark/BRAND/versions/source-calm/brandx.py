# ---- brandx.py: assembly of the book (exec'd from brand.py at @@ASM@@) ------------------------------------------------
for _f in ("brandx_assets.py", "brandx_pages.py"):
    if os.path.exists("/tmp/hdwm/" + _f): exec(open("/tmp/hdwm/" + _f).read())

def OT(t): return next(p for p in OLD if f"<h2>{t}</h2>" in p)
SECTIONS = [
 ("Foundations", [OLD[1]] + G("PG_FOUND"), "ink", "Why Hypedrive exists, who it is for, and how it sounds when it speaks."),
 ("Logo", OLD[2:6] + G("PG_LOGO2") + [OLD[6]] + G("PG_LOGO3"), "cobalt", "The parcel, the wordmark, and the rules that keep them readable."),
 ("Brand motifs", G("PG_MOTIFS") + G("PG_PATTERN"), "marigold", "Four shapes taken straight from the logo: the tape, the hexagon, the label and the parcel."),
 ("Colour", OLD[7:10] + G("PG_COLOR"), "vermilion", "Four brand colours, one neutral, and the rules that stop them competing."),
 ("Typography", OLD[10:13] + G("PG_TYPE2"), "ink", "Bricolage for the brand, Geist for the interface, Geist Mono for codes."),
 ("Layout", OLD[13:16], "cobalt", "A 4 pixel base, radius by maths, and floating things that lift."),
 ("Iconography", G("PG_ICONS"), "marigold", "Nucleo outlines, with an exact solid twin for every active state."),
 ("Illustration", G("PG_ILL") or [OLD[16]], "vermilion", "Seventeen chunky isometric objects built from the parcel."),
 ("Photography", G("PG_PHOTO") + G("PG_PHOTO2"), "ink", "Real products on real surfaces, and how pictures and illustration share a page."),
 ("Product", [OT("In the product")] + G("PG_UI") + G("PG_COMP") + G("PG_CHART"), "cobalt", "How the identity shows up in the app: calm surfaces and one strong action."),
 ("Voice and motion", [OT("Voice &amp; tone") if any("<h2>Voice &amp; tone</h2>" in p for p in OLD) else OT("Voice & tone")] + G("PG_VOICE") + [OT("Motion")] + G("PG_MOTION"), "marigold", "Warm, quick and straight, and things that arrive like a parcel being set down."),
 ("Applications", (G("PG_SOCIAL") + G("PG_PRINT") if G("PG_SOCIAL") else OLD[26:28]) + G("PG_APPS"), "vermilion", "Social, print, the creator media kit and email."),
 ("Packaging", G("PG_PACK"), "ink", "What the creator opens: the box, the mailer, a thank-you card and stickers."),
 ("Campaigns", G("PG_CAMP"), "cobalt", "Key visuals that join a product photo, the parcel, the line and the colours."),
 ("Merch and events", G("PG_MERCH"), "marigold", "A tee, a tote and one booth layout, all built from the same parts."),
 ("Tokens", [OT("Design tokens"), OT("Semantic colour tokens")], "vermilion", "Colour, type, space and motion as code."),
 ("Contact", G("PG_CONTACT"), "ink", "Where the files live and who to ask."),
]
SECTIONS = [s for s in SECTIONS if s[1]]
OPEN_BG = {"ink": (INK, "#ffffff", SCALES["ink"][800], COB, "#ffffff", SCALES["marigold"][300]),          # bg, text, tone-on-tone parcel, tape bg, tape text, accent
           "cobalt": (COB, "#ffffff", SCALES["cobalt"][500], INK, "#ffffff", SCALES["marigold"][300]),
           "marigold": (BRAND["marigold"], INK, SCALES["marigold"][200], COB, "#ffffff", COB),
           "vermilion": (BRAND["vermilion"], INK, SCALES["vermilion"][400], INK, "#ffffff", "#ffffff")}
def tape_band(w, h, bg, fg, mode):
    lk = FN.lockup(mode, mono=fg, pad=0); lh = h*0.46; vw, vh = vb(lk)[2], vb(lk)[3]; lw = vw*lh/vh
    unit = lw + h*1.15; n = int(w // unit) + 2
    parts = "".join(place(lk, h*0.5 + i*unit, (h-lh)/2, h=lh)[0] for i in range(n))
    return f'<rect width="{w}" height="{h}" fill="{bg}"/><rect width="{w}" height="3" fill="#000" fill-opacity=".14"/><rect y="{h-3}" width="{w}" height="3" fill="#000" fill-opacity=".14"/>{parts}'
def opener(num, name, blurb, titles, tone):
    lines = name.split(" and ")
    nm = "<br>".join([lines[0] + (" and" if len(lines) > 1 else "")] + lines[1:]) if len(lines) > 1 else name
    lis = "".join(f"<li><span>{t}</span><em>{pg}</em></li>" for t, pg in titles)
    return (f'<section class="page opener" style="background:#ffffff;color:{INK}">'
            f'<div class="op-top">{img(LK_TIGHT_L, "height:32px")}<span class="op-n"><b>{num:02d}</b> / {len(SECTIONS):02d}</span></div>'
            f'<h2 class="op-h">{nm}</h2>'
            f'<div class="op-rule"></div><p class="op-b">{blurb}</p><ul class="op-l">{lis}</ul></section>')
def _title(p):
    m = re.search(r"<h2>(.*?)</h2>", p); return m.group(1) if m else None

# ---- cover
def cover_page():
    hero = ill_img("parcel", "light", "width:470px")
    return (f'<section class="page cover2" style="background:#ffffff;color:{INK}">'
            f'<div class="cv-top">{img(LK_TIGHT_L, "height:40px")}<span>Version 1.2 · November 2026</span></div>'
            f'<h1 class="cv-h">Brand<br>identity.</h1><div class="cv-hero">{hero}</div>'
            f'<div class="cv-foot"><p class="cv-s">Guidelines for the logo, colour, type, imagery, product, packaging and campaigns of Hypedrive.</p><span>hypedrive.app</span></div></section>')
def back_cover():
    return (f'<section class="page cover2 back" style="background:#ffffff;color:{INK}">'
            f'<div class="bk">{img(LK_TIGHT_L, "width:420px")}<h1>{TAGLINE}</h1><p>hypedrive.app · support@hypedrive.app</p></div></section>')
def tiled_pat(pat):
    return svg_wrap(1600, 900, tiled(pat, 1600, 900, pid="bkp"))

# ---- contents (two pages) -----------------------------------------------------------------------------------------
def build_flat():
    fl = [(None, "@@COVER@@"), ("Guide", "@@TOC1@@"), ("Guide", "@@TOC2@@")]
    for i, (sec, ps, tone, blurb) in enumerate(SECTIONS, 1):
        _o = len(fl) + 1
        fl.append((sec, ("@@OPEN@@", i, sec, blurb, [(_title(p), _o + k + 1) for k, p in enumerate(ps) if _title(p)], tone)))
        fl += [(sec, p) for p in ps]
    fl.append((None, "@@BACK@@"))
    return fl
flat = build_flat()
def _pgno(sec, first=False):
    for i, (s2, q) in enumerate(flat, 1):
        if s2 == sec and (isinstance(q, tuple) if first else True): return i
def build_toc(half):
    secs = list(enumerate(SECTIONS, 1)); cut = 8
    secs = secs[:cut] if half == 1 else secs[cut:]
    cols = []
    for k, (sec, ps, tone, bl) in secs:
        rows = "".join(f'<li><span>{_title(p)}</span><em>{[i for i, (s2, q) in enumerate(flat, 1) if q is p][0]}</em></li>' for p in ps if _title(p))
        cols.append(f'<div class="toc-s"><h3><i>{k:02d}</i>{sec}<em>{_pgno(sec, True)}</em></h3><ul>{rows}</ul></div>')
    return page(head("00", "Contents" if half == 1 else "Contents, continued", "Every page, in order. Page numbers match the PDF." if half == 1 else "") + f'<div class="toc">{"".join(cols)}</div>')
def _expand(sec, p):
    if isinstance(p, tuple): return opener(p[1], p[2], p[3], p[4], p[5])
    if p == "@@COVER@@": return cover_page()
    if p == "@@BACK@@": return back_cover()
    if p == "@@TOC1@@": return build_toc(1)
    if p == "@@TOC2@@": return build_toc(2)
    return p
_ph = {i: (s, p) for i, (s, p) in enumerate(flat, 1)}
_exp = [(s, _expand(s, p)) for s, p in flat]
FOOT_LK = img(LK_TIGHT_B, "height:17px", alt="Hypedrive")
def _furn(i, sec, p):
    if 'class="page opener"' in p or 'class="page cover2' in p: return p
    p = re.sub(r"<small>\d\d</small>", f"<small>{sec}</small>", p, count=1)
    foot = f'<footer class="pf"><span class="pl">{FOOT_LK}<i>Brand identity guidelines</i><i>{sec}</i></span><b>{i}</b></footer>'
    p = p.replace('<section class="page', f'<section data-p="{i}" class="page', 1)
    return p[:-len("</section>")] + foot + "</section>"
pages = [_furn(i, s, p) for i, (s, p) in enumerate(_exp, 1)]
xcss("""
code { font-size: 15px !important; }
@page { size: 1600px 900px; margin: 0; }
header small { font: 600 17px var(--hd-font-ui); color: ${i600}; letter-spacing: 0; display: block; margin-bottom: 8px; }
h2 { font-size: 56px; line-height: 1.02; margin: 0 0 12px; letter-spacing: -.025em; }
.lead { font: 21px/1.42 var(--hd-font-ui); color: ${i600}; max-width: 1240px; margin: 0 0 22px; }
.page { padding: 60px 88px 0; background: #fff; } .page.dark header small { color: ${m300}; }
.pf { position: absolute; left: 88px; right: 88px; bottom: 0; height: 58px; display: flex; align-items: center; justify-content: space-between; border-top: 1px solid ${i200}; font: 500 15px var(--hd-font-ui); color: ${i600}; }
.pf .pl { display: flex; align-items: center; gap: 22px; } .pf .pl img { display: block; } .pf i { font-style: normal; } .pf i + i::before { content: ''; display: inline-block; width: 1px; height: 14px; background: ${i300}; margin-right: 22px; vertical-align: -2px; }
.pf b { font: 650 17px var(--hd-font-ui); color: ${ink}; font-variant-numeric: tabular-nums; }
.bgdeco { position: absolute; left: 0; top: 0; width: 1600px; height: 900px; display: block; }
.opener, .cover2 { padding: 0; } .opener > *, .cover2 > * { position: relative; }
.opener .bgdeco, .cover2 .bgdeco { position: absolute; }
.op-top { position: absolute; left: 88px; right: 88px; top: 64px; display: flex; justify-content: space-between; align-items: center; font: 500 18px var(--hd-font-ui); color: ${i600}; } .op-top img { display: block; }
.op-n { font-variant-numeric: tabular-nums; } .op-n b { color: ${ink}; font-weight: 700; }
.op-h { position: absolute; left: 82px; bottom: 372px; margin: 0; font-size: 184px; line-height: .92; font-weight: 700; letter-spacing: -.035em; font-variation-settings: 'opsz' 96; max-width: 1440px; color: ${ink}; }
.op-rule { position: absolute; left: 88px; right: 88px; top: 560px; height: 1px; background: #dcdce1; }
.op-b { position: absolute; left: 88px; top: 596px; width: 500px; margin: 0; font: 500 26px/1.38 var(--hd-font-ui); letter-spacing: -.012em; color: ${ink}; }
.op-l { position: absolute; left: 720px; right: 88px; top: 596px; margin: 0; padding: 0; list-style: none; columns: 2; column-gap: 56px; font: 500 18px/1.3 var(--hd-font-ui); color: ${i800}; } .op-l li { break-inside: avoid; padding: 8px 0; display: flex; justify-content: space-between; gap: 16px; border-bottom: 1px solid #ebebef; } .op-l li em { font-style: normal; color: ${i500}; font-variant-numeric: tabular-nums; }
.cv-top { position: absolute; left: 88px; right: 88px; top: 72px; display: flex; justify-content: space-between; align-items: center; font: 500 18px var(--hd-font-ui); color: ${i600}; } .cv-top img { display: block; }
.cv-h { position: absolute; left: 80px; top: 214px; margin: 0; font-size: 248px; line-height: .88; font-weight: 700; letter-spacing: -.04em; font-variation-settings: 'opsz' 96; color: ${ink}; }
.cv-hero { position: absolute; right: 120px; top: 180px; } .cv-hero img { display: block; }
.cv-foot { position: absolute; left: 88px; right: 88px; bottom: 56px; border-top: 1px solid #dcdce1; padding-top: 22px; display: flex; justify-content: space-between; font: 500 18px var(--hd-font-ui); color: ${i600}; }
.cv-s { margin: 0; width: 1100px; font: 400 20px/1.4 var(--hd-font-ui); color: ${i700}; }
.cover2.back .bk { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 30px; } .cover2.back h1 { margin: 0; font-size: 92px; font-weight: 700; letter-spacing: -.03em; font-variation-settings: 'opsz' 96; color: ${ink}; } .cover2.back p { margin: 0; font: 500 20px var(--hd-font-ui); color: ${i600}; }
.toc { columns: 4; column-gap: 40px; margin-top: 10px; } .toc-s { break-inside: avoid; margin-bottom: 30px; }
.toc-s h3 { font-size: 26px; margin: 0 0 6px; padding-bottom: 10px; border-bottom: 1px solid ${ink}; display: flex; align-items: baseline; gap: 10px; letter-spacing: -.02em; font-weight: 650; } .toc-s h3 i { font: 700 15px var(--hd-font-ui); color: ${i500}; font-style: normal; } .toc-s h3 em { margin-left: auto; font: 600 17px var(--hd-font-ui); font-style: normal; color: ${i600}; }
.toc ul { list-style: none; margin: 0; padding: 0; } .toc li { display: flex; justify-content: space-between; gap: 12px; font: 16px/1.25 var(--hd-font-ui); padding: 6px 0; border-bottom: 1px solid #ebebef; color: ${i800}; }
.toc li em { font-style: normal; font-variant-numeric: tabular-nums; color: ${i500}; font-weight: 600; }
""")

# ---- round-1 fixes (bug sweep): per-page overrides keyed on data-p; content must end >= 24px above the footer rule (y 842)
xcss("""
[data-p="12"] .marks div { height: 226px; } [data-p="12"] .words { margin-top: 14px; } [data-p="12"] .words div { height: 132px; } [data-p="12"] .tittle { margin-top: 16px; padding: 12px 24px; } [data-p="12"] .tittle img { height: 104px !important; }
[data-p="41"] .rz { height: 90px; } [data-p="41"] .rgrid { gap: 18px 24px; } [data-p="41"] .rside { padding: 20px 24px; } [data-p="41"] .cc { margin-bottom: 12px; } [data-p="41"] .cc > div { height: 72px; }
[data-p="54"] .x-pg { grid-auto-rows: 196px; } [data-p="54"] .x-note { margin-top: 14px !important; }
[data-p="96"] .x-fl td { padding: 7px 0; }
[data-p="64"] .crop { margin-left: auto; margin-right: auto; }
""")

# ---- round-2: alignment, crisp borders (no ring shadows on in-flow surfaces), thin pages
xcss("""
.x-trait .ex.y, .x-cp .af { box-shadow: none; border: 1px solid #e8e8eb; } .x-trait .ex.n, .x-cp .bf { box-shadow: none; border: 1px solid #e8e8eb; }
.x-prop { box-shadow: none; border: 1px solid ${i200}; } .x-sz .box > div { box-shadow: none; border: 1px solid ${i200}; } .x-mail { box-shadow: none; border: 1px solid ${i200}; }
.x-ap img.sh { box-shadow: 0 18px 40px -18px rgba(16,20,38,.28); border: 1px solid ${i200}; }
[data-p="6"] .x-flow > div { align-items: start; } [data-p="6"] .x-flow { margin-top: 36px; }
[data-p="8"] .x-trait .ex { min-height: 88px; }
[data-p="13"] .constr { align-items: center; }
[data-p="14"] .x-min span:last-child { min-height: 2.9em; }
[data-p="17"] .x-co img { width: 206px !important; } [data-p="17"] .x-co > div { gap: 22px; }
[data-p="19"] .x-fav .big { align-items: flex-end !important; } [data-p="19"] .x-tab.dk.bar span { color: ${i300}; }
[data-p="25"] .sw { height: 372px; }
[data-p="46"] .x-tw > div { padding: 34px 0 26px; gap: 18px; }
[data-p="50"] .x-cr .cons { padding: 28px; } [data-p="50"] .x-steps > div { height: 210px; } [data-p="50"] .x-steps > div img, [data-p="50"] .x-steps > div svg { height: 150px; }
[data-p="51"] .x-sz > div > .box { height: 440px; }
[data-p="71"] .x-rl > div { display: flex; flex-direction: column; } [data-p="71"] .x-rl .ex { margin-top: auto; }
[data-p="93"] pre { font-size: 18px; line-height: 1.75; padding: 38px 46px; }
""")

# round-3: pages with a large empty foot get an even share of it above the content (measured gaps)
xcss("""
[data-p="3"] > header + * { margin-top: 28px !important; }
[data-p="5"] > header + * { margin-top: 36px !important; }
[data-p="6"] > header + * { margin-top: 40px !important; }
[data-p="7"] > header + * { margin-top: 36px !important; }
[data-p="8"] > header + * { margin-top: 32px !important; }
[data-p="11"] > header + * { margin-top: 24px !important; }
[data-p="12"] > header + * { margin-top: 36px !important; }
[data-p="14"] > header + * { margin-top: 32px !important; }
[data-p="17"] > header + * { margin-top: 40px !important; }
[data-p="18"] > header + * { margin-top: 32px !important; }
[data-p="19"] > header + * { margin-top: 36px !important; }
[data-p="25"] > header + * { margin-top: 28px !important; }
[data-p="27"] > header + * { margin-top: 32px !important; }
[data-p="30"] > header + * { margin-top: 36px !important; }
[data-p="35"] > header + * { margin-top: 44px !important; }
[data-p="40"] > header + * { margin-top: 24px !important; }
[data-p="44"] > header + * { margin-top: 36px !important; }
[data-p="46"] > header + * { margin-top: 40px !important; }
[data-p="50"] > header + * { margin-top: 44px !important; }
[data-p="51"] > header + * { margin-top: 40px !important; }
[data-p="52"] > header + * { margin-top: 28px !important; }
[data-p="68"] > header + * { margin-top: 40px !important; }
[data-p="70"] > header + * { margin-top: 44px !important; }
[data-p="71"] > header + * { margin-top: 44px !important; }
[data-p="72"] > header + * { margin-top: 24px !important; }
[data-p="76"] > header + * { margin-top: 32px !important; }
[data-p="81"] > header + * { margin-top: 24px !important; }
[data-p="83"] > header + * { margin-top: 32px !important; }
[data-p="93"] > header + * { margin-top: 32px !important; }
[data-p="94"] > header + * { margin-top: 28px !important; }
[data-p="96"] > header + * { margin-top: 32px !important; }
""")

# ---- final polish: spacing and alignment found in the full-size read
xcss("""
.x-cp .ctx { color: ${i600} !important; } .x-cp .lbl.b, .x-cp .lbl.a { color: ${ink} !important; font-weight: 600; }
[data-p="10"] .hero-logo { padding: 8px 0 24px; } [data-p="10"] .hero-logo img { width: 800px !important; } [data-p="10"] .logos > div { height: 188px !important; }
[data-p="11"] .lk > div { justify-content: flex-end !important; padding-bottom: 26px; }
[data-p="23"] > div:first-of-type > div { height: 250px !important; }
[data-p="90"] .fgc { text-align: center; } [data-p="90"] .tint { height: 340px !important; }
[data-p="34"] .trow { padding-top: 8px; padding-bottom: 8px; }
""")
