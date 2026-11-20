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
    return f'<img class="rp" alt="Hypedrive desktop screen" style="height:{h}px" src="{_b64(im)}"/>'
def crop_img(n, theme, w, extra=""):
    im = _Im.open(f"{BSHOT}/sec{n}-{theme}.png").convert("RGB"); tw = min(im.width, round(w * 1.5))
    im = im.resize((tw, round(im.height * tw / im.width)), _Im.LANCZOS)
    return f'<img class="crop" alt="UI kit section" style="width:{w}px;{extra}" src="{_b64(im)}"/>'
def crop_h(n, theme, w): return round(_Im.open(f"{BSHOT}/sec{n}-{theme}.png").height * w / _Im.open(f"{BSHOT}/sec{n}-{theme}.png").width)
def rules(items, cols=1):
    return f'<div class="rules c{cols}">' + "".join(f'<div><b>{t}</b><p>{p}</p></div>' for t, p in items) + '</div>'

# ---- typography -----------------------------------------------------------------
FONT_ROLES = [("Bricolage Grotesque", "Brand voice", "Display, headings, hero numbers", "var(--hd-font-display)", "font-weight:650;font-variation-settings:'opsz' 96;letter-spacing:-.03em",
               "Products in. Hype out.", "Variable: opsz 12–96, wdth 75–100, wght 200–800"),
              ("Geist", "Interface", "Every label, row, button, field and paragraph in the product", "var(--hd-font-ui)", "font-weight:400",
               "120 creators are trying your serum this week.", "Variable: wght 100–900 · Open Font License"),
              ("Geist Mono", "Codes and IDs", "Tracking numbers, order IDs, API keys. Never inside running text", "var(--hd-font-mono)", "font-weight:450",
               "Delhivery 4471 2280", "Variable: wght 100–900 · Open Font License")]
SAMPLE_STY = ["font-weight:650;letter-spacing:-.024em;font-variation-settings:'opsz' 48", "font-weight:400", "font-weight:450"]
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
 page(head("00", "Typography", "Three typefaces, three jobs. Bricolage Grotesque speaks for the brand, Geist runs the interface, and Geist Mono carries codes and IDs.") +
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
    if kind == "grey": return f'<div class="rs" style="width:{w}px;height:{h}px;border-radius:{r}px;background:var(--hd-control);color:var(--hd-fg)">Later</div>'
    if kind == "chip": return f'<div class="rs line" style="width:{w}px;height:{h}px;border-radius:{r}px">For you</div>'
    if kind == "badge": return f'<div class="rs" style="width:{w}px;height:{h}px;border-radius:{r}px;background:{N[700]};color:#fff;font-size:12px">Live</div>'
    if kind == "check": return f'<div class="rs" style="width:{w}px;height:{h}px;border-radius:{r}px;background:var(--hd-accent);color:#fff"><svg width="14" height="14" viewBox="0 0 14 14"><path d="M2.5 7.5l3 3 6-7" fill="none" stroke="#fff" stroke-width="2"/></svg></div>'
    if kind == "input": return f'<div class="rs line" style="width:{w}px;height:{h}px;border-radius:{r}px;justify-content:flex-start;padding-left:14px;color:var(--hd-fg-subtle)">Search drops</div>'
    return f'<div class="rs line" style="width:{w}px;height:{h}px;border-radius:{r}px"></div>'
RAD = [("Button", "12", 132, 44, 12, "btn", "44 tall · height × 0.27"), ("Small button", "8", 96, 32, 8, "grey", "32 tall"), ("Chip", "8–10", 92, 32, 9, "chip", "32 tall"),
       ("Badge", "6", 56, 22, 6, "badge", "22 tall"), ("Checkbox", "6", 22, 22, 6, "check", "22 square"), ("Input", "12", 200, 44, 12, "input", "44 tall"),
       ("Card, panel", "16", 200, 84, 16, "card", "Rows, stat cards, panels"), ("Dialog, sheet", "24", 200, 100, 24, "card", "Floating, largest"), ("Tag", "8", 72, 28, 8, "chip", "28 tall")]
rad_cells = "".join(f'<div class="rc"><div class="rz">{rshape(w, h, r, k)}</div><b>{n} · {v}</b><span>{note}</span></div>' for n, v, w, h, r, k, note in RAD)
conc = "".join(f'<div class="cc"><div style="border-radius:{o}px;padding:{g}px"><div style="border-radius:{max(o - g, 4)}px"></div></div><b>outer {o} − gap {g} = {max(o - g, 4)}</b></div>' for o, g in ((24, 8), (16, 8), (16, 12)))
def flat(t): return f'<div class="ft"><b>{t}</b></div>'
def elev_panel(theme):
    return (f'<div class="ep" data-theme="{theme}"><h4>{theme.title()}</h4><p class="eh">In-flow: hairline only, no shadow</p><div class="e4">' + "".join(flat(t) for t in ("Card", "Row", "Panel", "Stat card")) + '</div>'
            f'<p class="eh">Floating: shadow</p><div class="e3x">' + "".join(f'<div class="ff" style="box-shadow:var(--hd-shadow-{k})"><b>{k}</b><span>{t}</span></div>' for k, t in (("e1", "Tooltips, small menus"), ("e2", "Menus, popovers, toasts"), ("e3", "Sheets, dialogs"))) + '</div></div>')
PG_LAYOUT = [
 page(head("00", "Layout & spacing", "A 4-pixel base. Every gap, padding and radius comes from these steps, named by role. No per-page margins and no one-off values.") +
      f'<div class="cols2" style="grid-template-columns:1.25fr 1fr;gap:56px"><div class="space">' + "".join(f'<div><i style="width:{v*4}px"></i><b>space-{i+1}</b><span>{v}px</span></div>' for i, v in enumerate(SPACE)) + '</div>'
      + rules([("Hit areas", "44 px for anything you tap: top bar icons, search, buttons, tabs. Small controls grow their hit area, not their look."),
               ("Row cards", "Every list item is its own rounded card with a gap between. Only tables and nav or settings menus join rows with inset dividers."),
               ("Real estate", "Empty states show suggestions and related items, never a lone illustration.")]) + '</div>'),
 page(head("00", "Radius", "Radius is maths, not taste. Concentric elements take the outer radius minus the gap, never below 4. Everything else is about 0.27 of its height.") +
      f'<div class="rwrap"><div class="rgrid">{rad_cells}</div><div class="rside"><h3>Concentric</h3><p class="cap" style="margin:0 0 14px">Inner = max(outer − gap, 4). A row inside a card, an icon tile inside a row.</p>{conc}'
      f'<p class="cap" style="margin-top:14px">Phone frame 52 outer, 42 screen. Pills (999) only for avatars and toggles.</p></div></div>'),
 page(head("00", "Elevation", "In-flow surfaces separate with a hairline, never a shadow. Only things that float above the page, from a tooltip to a dialog, get one.") +
      f'<div class="elevs">{elev_panel("light")}{elev_panel("dark")}</div>'),
]

# ---- brand in UI, components ----------------------------------------------------
PG_UI = [
 page(head("00", "The brand in UI: mobile", "Calm surfaces, one strong action. Cobalt marks the next thing to do; everything else stays quiet.") +
      f'<div class="uiflex"><div class="phones">{real_phone("03-home", 570)}{real_phone("04-drop-details", 570)}{real_phone("11-profile-dark", 570)}</div>'
      + rules([("Photos run full-bleed", "Product photos fill their card edge to edge. Controls sit over them on solid discs."),
               ("Inline meta rows", "Earnings and rating sit as icon and value between hairlines. No stat tiles on phone."),
               ("Separate row cards", "Each drop is its own card. Product thumbnails sit bare, with no plate behind them."),
               ("Underline tabs", "Solid icons coloured by meaning, a Cobalt underline on the active tab. No pills."),
               ("Dark mode", "The same tokens remapped. Surfaces step up from Ink 950, Cobalt stays the action colour.")]) + '</div>'),
 page(head("00", "The brand in UI: desktop", "The same system with room to breathe: a grouped sidebar, a quiet top bar, stat cards with one anatomy, and a table only where a table helps.") +
      f'<div class="uiflex">{real_desktop("hypedrive-desktop-1", 560)}'
      + rules([("One search", "The sidebar's ⌘K is the global search. No second field."),
               ("Stat cards", "Label row with the delta top right, the value, then a visual pinned to the bottom. No captions, no pills."),
               ("Tint is rare", "Only for alerts, repeated statuses in tables and selected rows. A lone status stays solid."),
               ("Flat in flow", "Cards and panels carry a hairline and no shadow.")]) + '</div>'),
]
PG_COMP = [
 page(head("00", "Components: buttons", "Flat deep Cobalt for the one main action. Grey for everything secondary. Rendered from the UI kit, not redrawn.") +
      crop_img(2, "light", 1424) +
      f'<div class="rules c4 inl"><div><b>Primary</b><p>Flat Cobalt, a 1px darker edge, a 0.97 press. No glow.</p></div><div><b>Secondary</b><p>Grey, no border. Disabled is solid grey with subtle text.</p></div>'
      f'<div><b>Icons on key actions only</b><p>New, Upload, Export, Filter and icon-only buttons. Not every label.</p></div><div><b>Optical padding</b><p>14 px on the icon side so icon and label look centred.</p></div></div>'),
 page(head("00", "Components: navigation", "Bare icons in the top bar, underline tabs, a labelled four-item tab bar on phone.") +
      crop_img(4, "light", 1424) +
      f'<div class="rules c3 inl" style="margin-top:28px"><div><b>Underline tabs</b><p>Icons are solid and coloured by meaning, the same everywhere: Drops and Campaigns are a box, Creators are people, Home is a house. The active tab shows by its underline and its text colour.</p></div>'
      f'<div><b>Top bar</b><p>Bare icons with no discs, 44 px hit areas. Discs appear only over a photo.</p></div>'
      f'<div><b>Tab bar</b><p>Four labelled items. A floating bar that hides the labels was tried and rejected: recognition matters more.</p></div></div>'),
 page(head("00", "Components: lists and data", "Every item is its own card. Rendered from the UI kit.") +
      f'<div class="uiflex">{crop_img(5, "light", 930)}'
      + rules([("Separate row cards", "A gap between every item, a hairline around each, no shadow."),
               ("Bare product photos", "No plate, tile or ring behind a photo. A glyph fallback keeps its tile."),
               ("Solid badges", "Status is solid. Tint is for alerts, repeated table statuses and selected rows."),
               ("Stat cards", "One anatomy, compact, customised per data type: trend, counts, rating, split, goal.")]) + '</div>'),
 page(head("00", "Components: feedback", "Notices explain, toasts confirm, dialogs ask. One action each.") +
      f'<div class="uiflex">{crop_img(6, "light", 930)}'
      + rules([("Alerts are tinted", "The one place tint is the rule: a quiet wash with strong-colour text at full contrast, and a solid icon."),
               ("Floating means shadow", "Toasts, menus and dialogs lift with e2 or e3. Nothing else does."),
               ("One focus ring", "A 2px gap in the surface colour plus 2px Cobalt, everywhere. Inputs focus with a 2px accent border.")]) + '</div>'),
 page(head("00", "Components in dark") +
      f'<div class="dkgrid"><div>{crop_img(2, "dark", 700)}{crop_img(8, "dark", 700, "margin-top:16px")}</div><div>{crop_img(5, "dark", 700)}{crop_img(6, "dark", 700, "margin-top:16px")}</div></div>'),
]
PG_CHART = [
 page(head("00", "Charts & data", "Series are flat brand colours, drawn in a fixed order and labelled directly. Rendered from the UI kit.") +
      f'<div class="uiflex">{crop_img(8, "light", 1000)}<div class="cside2"><h3>Categorical order</h3><div class="cat">' +
      "".join(f'<div><i style="background:{h}"></i><b>{i+1}. {n}</b><span>{h}</span></div>' for i, (n, h) in enumerate([("Cobalt 500", SCALES["cobalt"][500]), ("Vermilion 500", SCALES["vermilion"][500]), ("Marigold 300", SCALES["marigold"][300]), ("Mint 500", SCALES["mint"][500]), ("Ink 400", SCALES["ink"][400])])) +
      f'</div><p class="cap" style="margin-top:10px">One highlight in Vermilion, the rest Cobalt. Comparisons are dashed and grey. Hairline grid, labels in Geist.</p></div></div>'),
]
