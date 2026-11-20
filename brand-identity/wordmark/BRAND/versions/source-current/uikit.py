"""Hypedrive UI kit (primitives + components) and high-fidelity screens, all from one component CSS + the brand tokens."""
import os, re, sys, json, base64
B = os.path.expanduser("~/Downloads/hypedrive-wordmark/BRAND")
OUT = os.path.join(B, "ui")
os.makedirs(OUT, exist_ok=True)
T = json.load(open(os.path.join(B, "tokens", "tokens.json")))
SC = T["scales"]; C, V, M, I, N = (SC[k] for k in ("cobalt", "vermilion", "marigold", "ink", "mint"))
TOK = open(os.path.join(B, "tokens", "colors.css")).read()
FONT = base64.b64encode(open("/tmp/hdwm/fonts/Bricolage.ttf", "rb").read()).decode()
GEIST = base64.b64encode(open("/tmp/hdwm/fonts/Geist.ttf", "rb").read()).decode()
GMONO = base64.b64encode(open("/tmp/hdwm/fonts/GeistMono.ttf", "rb").read()).decode()

def uri_file(p):
    return "data:image/svg+xml;base64," + base64.b64encode(open(p, "rb").read()).decode()
LOGO = {k: uri_file(os.path.join(B, "ui", "assets", "logo", f"lockup-tight-{k}.svg")) for k in ("light", "dark")}   # no baked-in clear space: UI sizes mean the real mark height
MARK = {k: uri_file(os.path.join(B, "assets", "logo", "mark", f"hypedrive-mark-color-{k}.svg")) for k in ("light", "dark")}
ILL = {(n, t): uri_file(os.path.join(B, "assets", "illustrations", f"hypedrive-ill-{n}-{t}.svg"))
       for n in ("parcel", "payout", "approved", "review", "content", "tracking", "growth", "search") for t in ("light", "dark")}
PAT = uri_file(os.path.join(B, "assets", "patterns", "pattern-parcels-ink.svg"))

# ------------------------------------------------------------------ icons (24 grid, 1.75 stroke, round)
P = {
 "home": "M4 10.5 12 4l8 6.5V19a1 1 0 0 1-1 1h-4.5v-5.5h-5V20H5a1 1 0 0 1-1-1z",
 "search": "M10.5 4a6.5 6.5 0 1 1 0 13 6.5 6.5 0 0 1 0-13zM15.5 15.5 20 20",
 "box": "M12 3 20 7.5v9L12 21l-8-4.5v-9zM4 7.5l8 4.5 8-4.5M12 12v9M8 5.3l8 4.5",
 "wallet": "M4 7.5A2.5 2.5 0 0 1 6.5 5H18v3M4 7.5V17a2 2 0 0 0 2 2h13a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1H6.5A2.5 2.5 0 0 1 4 7.5zM16 13.5h.01",
 "user": "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4.5 20a7.5 7.5 0 0 1 15 0",
 "bell": "M6 16V11a6 6 0 1 1 12 0v5l1.5 2h-15zM10 20.5a2 2 0 0 0 4 0",
 "back": "M14.5 5.5 8 12l6.5 6.5",
 "chev": "M9.5 5.5 16 12l-6.5 6.5",
 "down": "M5.5 9.5 12 16l6.5-6.5",
 "plus": "M12 5v14M5 12h14",
 "check": "M5 12.5 10 17.5 19 7",
 "x": "M6 6l12 12M18 6 6 18",
 "star": "M12 4l2.4 5 5.4.7-4 3.8 1 5.4L12 16.3 7.2 18.9l1-5.4-4-3.8 5.4-.7z",
 "camera": "M4 8.5A1.5 1.5 0 0 1 5.5 7h2.3L9.5 5h5l1.7 2h2.3A1.5 1.5 0 0 1 20 8.5V17a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 17zM12 15.5a3 3 0 1 0 0-6 3 3 0 0 0 0 6z",
 "upload": "M12 15V5M8 8.5 12 4.5l4 4M5 15v3a1.5 1.5 0 0 0 1.5 1.5h11A1.5 1.5 0 0 0 19 18v-3",
 "filter": "M4 6h16M7 12h10M10 18h4",
 "arrow": "M5 12h14M13 6l6 6-6 6",
 "heart": "M12 19s-7-4.4-7-9.5A3.8 3.8 0 0 1 12 7.3a3.8 3.8 0 0 1 7 2.2C19 14.6 12 19 12 19z",
 "share": "M12 4v11M8 7.5 12 3.5l4 4M6 11v7.5A1.5 1.5 0 0 0 7.5 20h9a1.5 1.5 0 0 0 1.5-1.5V11",
 "settings": "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M5.6 18.4l1.8-1.8M16.6 7.4l1.8-1.8",
 "chart": "M5 19V11M10 19V6M15 19v-5M20 19V9",
 "truck": "M3.5 6.5h10v9h-10zM13.5 9.5h4l3 3v3h-7M7 18.5a1.8 1.8 0 1 0 0-3.6 1.8 1.8 0 0 0 0 3.6zM17 18.5a1.8 1.8 0 1 0 0-3.6 1.8 1.8 0 0 0 0 3.6z",
 "clock": "M12 20a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM12 8v4.5l3 2",
 "tag": "M4 12.2V5a1 1 0 0 1 1-1h7.2L20 11.8 12.8 19zM8.5 8.5h.01",
 "link": "M10 14a4 4 0 0 0 5.7 0l2.8-2.8a4 4 0 0 0-5.7-5.7L11.5 6.8M14 10a4 4 0 0 0-5.7 0l-2.8 2.8a4 4 0 0 0 5.7 5.7l1.3-1.3",
 "more": "M5.5 12h.01M12 12h.01M18.5 12h.01",
 "info": "M12 20a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM12 11v5M12 8h.01",
 "alert": "M12 4 21 19.5H3zM12 10v4M12 17h.01",
 "lock": "M6.5 11h11v8.5h-11zM8.5 11V8a3.5 3.5 0 0 1 7 0v3",
 "spark": "M12 3.5c.6 4.2 2.3 5.9 6.5 6.5-4.2.6-5.9 2.3-6.5 6.5-.6-4.2-2.3-5.9-6.5-6.5 4.2-.6 5.9-2.3 6.5-6.5z",
 "grid": "M4.5 4.5h6v6h-6zM13.5 4.5h6v6h-6zM4.5 13.5h6v6h-6zM13.5 13.5h6v6h-6z",
 "list": "M8.5 6.5h11M8.5 12h11M8.5 17.5h11M4.5 6.5h.01M4.5 12h.01M4.5 17.5h.01",
 "logout": "M14 4.5H6.5a1 1 0 0 0-1 1v13a1 1 0 0 0 1 1H14M10 12h10M16.5 8.5 20 12l-3.5 3.5",
}
ICON_SET = "Nucleo UI · 18 (outline + fill twins)"
NS = json.load(open("/tmp/hdwm/nucleo_sharp.json")); NO = json.load(open("/tmp/hdwm/nucleo_outline.json")); NF = json.load(open("/tmp/hdwm/nucleo_fill.json")); NSOC = json.load(open("/tmp/hdwm/nucleo_social.json"))
NMAP = {"home": "House6", "search": "Magnifier", "box": "Box3", "wallet": "Wallet3", "user": "User", "bell": "Bell", "back": "ChevronLeft", "chev": "ChevronRight",
        "down": "ChevronDown", "plus": "Plus", "check": "Check", "x": "Xmark", "star": "Star", "camera": "Camera", "upload": "ArrowUpFromLine", "filter": "Filter",
        "arrow": "ArrowRight", "heart": "Heart2", "share": "ShareRight", "settings": "Gear", "chart": "ChartArea", "truck": "Truck", "clock": "Clock", "tag": "Tag",
        "link": "Link", "more": "Dots", "info": "CircleInfo", "alert": "TriangleWarning", "lock": "Lock", "spark": "StarTrail", "grid": "Grid", "list": "BulletList",
        "logout": "RectLogout", "bank": "Storehouse", "bag": "BagShopping",
        "users": "Users2", "help": "CircleQuestion", "privacy": "ShieldCheck", "fast": "TruckFast", "linkbroken": "LinkBroken", "edit": "Pen", "copy": "Copy",
        "trash": "Trash", "download": "Download", "sliders": "Sliders", "play": "CirclePlay", "rupee": "CurrencyRupee", "receipt": "Receipt", "campaign": "Megaphone",
        "overview": "GridLayout", "reports": "ChartBar", "trend": "ArrowTrendUp", "gift": "Gift", "eye": "Eye", "calendar": "Calendar", "mail": "Envelope", "send": "PaperPlane2", "login": "RectLogin", "ok": "CircleCheck", "bolt": "Bolt", "phone": "Phone", "drop": "Droplet", "lipstick": "Lipstick", "shirt": "TShirt", "lamp": "DeskLamp", "headphones": "Headphones2", "payouts": "HandHoldingCoin", "pause": "MediaPause", "live": "MediaPlay", "foryou": "Compass", "trending": "Flame", "film": "Film", "minus": "Minus", "wifioff": "WifiOff", "clip": "Paperclip", "checkdouble": "CheckDouble", "file": "File", "filecheck": "FileCheck", "archive": "Archive", "sort": "SortArrows", "refresh": "Refresh", "pin": "MapPin"}
P = {k: None for k in NMAP}
def ic(name, size=22, color="currentColor", sw=None, fill="none"):
    """Outline icon: Nucleo UI Outline 18 (1.5 stroke). Its solid twin is the same name in UI Fill 18, a 1:1 geometric match."""
    if fill not in (None, "none"): return ics(name, size, None if color == "currentColor" else color)
    body = NO[NMAP[name] + "Outline18"]
    stroke = 1.5 if sw is None else round(sw * 0.75, 2)          # old calls passed 24-grid widths
    st = "" if color in (None, "currentColor") else f' style="color:{color}"'
    return f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 18 18" stroke-width="{stroke}"{st} aria-hidden="true">{body}</svg>'
SOC_COLOR = {"Instagram": "#d62976", "Youtube": "#ff0000", "Threads": "currentColor", "XTwitter": "currentColor", "Whatsapp": "#25d366", "Facebook": "#1877f2"}   # black brands follow text colour so they never vanish on dark
# Solids are the EXACT twin of the outline glyph (same Nucleo name + "Fill18"), never a look-alike.
FILL = {k: v + "Fill18" for k, v in NMAP.items() if v + "Fill18" in NF}
STATUS = {"info": "CircleInfo", "warning": "TriangleWarning", "success": "CircleCheck", "danger": "CircleXmark"}   # alert glyphs
FILL.update({k: v + "Fill18" for k, v in STATUS.items()})
NO_TWIN = sorted(k for k in NMAP if k not in FILL)
def icf(name, size=18):
    """Solid icon (Nucleo UI Fill 18) for alerts and status — colour comes from the parent role."""
    return f'<svg class="ic icf" width="{size}" height="{size}" viewBox="0 0 18 18" fill="currentColor" aria-hidden="true">{NF[FILL[name]]}</svg>'
def ics(name, size=18, color=None):
    """Active/selected state: the solid twin of an outline icon (outline = idle, solid = on)."""
    if name not in FILL: raise KeyError(f"no exact solid twin for {name} ({NMAP.get(name)})")
    st = f' style="color:{color}"' if color else ""
    return f'<svg class="ic icf" width="{size}" height="{size}" viewBox="0 0 18 18" fill="currentColor"{st} aria-hidden="true">{NF[FILL[name]]}</svg>'
def soc(name, size=22, color=None):
    return f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 32 32" fill="{color or SOC_COLOR.get(name, "currentColor")}" aria-hidden="true">{NSOC[name]}</svg>'
STOCK = "assets/stock"
PH = {"serum": f"{STOCK}/products/p6.jpg", "serum_hero": f"{STOCK}/products/p6.jpg", "cream": f"{STOCK}/products/p1.jpg", "mask": f"{STOCK}/products/p2.jpg",
      "flatlay": f"{STOCK}/products/p4.jpg", "set": f"{STOCK}/products/p5.jpg", "bottles": f"{STOCK}/products/p7.jpg", "sand": f"{STOCK}/products/p3.jpg",
      "scooter": f"{STOCK}/products/icon-scooter.webp", "trolley": f"{STOCK}/products/icon-trolley.webp", "chair": f"{STOCK}/products/icon-chair.webp", "walker": f"{STOCK}/products/icon-walker.webp"}
def vhex(size=16):
    """Verified mark: the wordmark's hexagon (parcel silhouette) with a check — a brand-native primitive."""
    return (f'<svg class="vhex" width="{size}" height="{size}" viewBox="0 0 24 24" aria-label="Verified"><path d="M12 1.6 21 6.8v10.4L12 22.4 3 17.2V6.8z" fill="var(--hd-accent)" stroke="var(--hd-accent)" stroke-width="1.6" stroke-linejoin="round"/>'
            f'<path d="M8 12.2l2.7 2.7L16.2 9.4" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="square"/></svg>')
def plat(name, size=20): return f'<img class="plat" src="{STOCK}/platforms/{name}.png" width="{size}" height="{size}" alt="{name}">'
def _unused_ic(name, size=22, color="currentColor", sw=2.0, fill="none"):
    return (f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 24 24" fill="{fill}" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="square" stroke-linejoin="miter" stroke-miterlimit="10" aria-hidden="true"><path d="{P[name]}"/></svg>')

# ------------------------------------------------------------------ component CSS (shared by kit + screens)
CSS = f"""
@font-face {{ font-family: 'Bricolage Grotesque'; src: url(data:font/ttf;base64,{FONT}) format('truetype'); font-weight: 200 800; font-stretch: 75% 100%; }}
@font-face {{ font-family: 'Geist'; src: url(data:font/ttf;base64,{GEIST}) format('truetype'); font-weight: 100 900; }}
@font-face {{ font-family: 'Geist Mono'; src: url(data:font/ttf;base64,{GMONO}) format('truetype'); font-weight: 100 900; }}
{TOK}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-variation-settings: 'opsz' 16; color: var(--hd-fg); background: #e9eaee; -webkit-font-smoothing: antialiased; }}
.ic {{ flex: none; display: block; }}
.num {{ font-variant-numeric: tabular-nums; }}
/* type */
.t-display {{ font-size: 40px; line-height: 44px; font-weight: 700; font-variation-settings: 'opsz' 96; letter-spacing: -.02em; }}
.t-h1 {{ font-size: 28px; line-height: 34px; font-weight: 700; font-variation-settings: 'opsz' 48; letter-spacing: -.015em; }}
.t-h2 {{ font-size: 21px; line-height: 27px; font-weight: 700; font-variation-settings: 'opsz' 32; letter-spacing: -.01em; }}
.t-h3 {{ font-size: 17px; line-height: 23px; font-weight: 650; font-variation-settings: 'opsz' 24; }}
.t-body {{ font-size: 15px; line-height: 22px; }} .t-small {{ font-size: 13px; line-height: 18px; }} .t-cap {{ font-size: 12px; line-height: 16px; font-weight: 500; }}
.muted {{ color: var(--hd-fg-muted); }} .subtle {{ color: var(--hd-fg-subtle); }}
img[src*="/products/p"] {{ object-fit: cover; border-radius: 10px; }} img[src*="/products/icon-"] {{ object-fit: contain; }}
.plat {{ border-radius: 6px; flex: none; display: block; }}
/* buttons */
.btn {{ font: 700 15px 'Bricolage Grotesque'; font-variation-settings: 'opsz' 16; border: 0; border-radius: var(--hd-radius-md); height: 44px; padding: 0 18px; display: inline-flex; align-items: center; justify-content: center; gap: 8px; cursor: pointer; white-space: nowrap; }}
.btn.p {{ background: var(--hd-accent); color: var(--hd-accent-fg); box-shadow: inset 0 -2px 0 var(--hd-accent-pressed); }}
.btn.s {{ background: var(--hd-control); color: var(--hd-fg); box-shadow: inset 0 -2px 0 var(--hd-control-edge); }}
.btn.g {{ background: transparent; color: var(--hd-link); }}
.btn.d {{ background: var(--hd-danger-solid); color: #fff; box-shadow: inset 0 -2px 0 var(--hd-danger-edge); }}
.btn.hov.p {{ background: var(--hd-accent-hover); }} .btn.prs {{ transform: translateY(1px); box-shadow: none; }} .btn.prs.p {{ background: var(--hd-accent-pressed); }}
.btn.hov.s {{ background: var(--hd-control-hover); }} .btn.prs.s {{ background: var(--hd-control-pressed); }} .btn.hov.d {{ background: var(--hd-danger-solid-hover); }} .btn.hov.g {{ background: var(--hd-accent-subtle); }}
.btn.foc {{ outline: 2px solid var(--hd-focus); outline-offset: 2px; }} .btn.dis {{ opacity: .4; box-shadow: none; }}
.btn.sm {{ height: 32px; font-size: 13px; padding: 0 12px; border-radius: 8px; }} .btn.lg {{ height: 52px; font-size: 16px; padding: 0 24px; }}
.btn.block {{ width: 100%; }} .btn.icon {{ width: 44px; padding: 0; }} .btn.icon.sm {{ width: 32px; }}
/* fields */
.field {{ display: flex; flex-direction: column; gap: 6px; }} .field > label {{ font-size: 13px; font-weight: 600; color: var(--hd-fg-muted); }}
.input {{ height: 48px; border: 1px solid var(--hd-border-strong); border-radius: 12px; padding: 0 14px; display: flex; align-items: center; gap: 10px; font-size: 15px; font-weight: 500; background: var(--hd-surface); color: var(--hd-fg); }}
.input .ph {{ color: var(--hd-fg-subtle); font-weight: 400; }} .input.foc {{ border-color: var(--hd-focus); box-shadow: 0 0 0 3px var(--hd-focus-ring); }}
.input.err {{ border-color: var(--hd-danger); }} .input.dis {{ background: var(--hd-bg-subtle); color: var(--hd-fg-subtle); }}
.input .pre {{ color: var(--hd-fg-muted); font-weight: 600; }} .help {{ font-size: 12px; color: var(--hd-fg-subtle); }} .help.err {{ color: var(--hd-danger); font-weight: 500; }}
.textarea {{ height: 104px; align-items: flex-start; padding-top: 12px; line-height: 21px; }}
.search {{ height: 44px; border-radius: 12px; background: var(--hd-bg-subtle); border: 1px solid var(--hd-border); display: flex; align-items: center; gap: 10px; padding: 0 12px; color: var(--hd-fg-subtle); font-size: 15px; }}
.otp {{ display: flex; gap: 10px; }} .otp span {{ width: 46px; height: 54px; border-radius: 12px; border: 1px solid var(--hd-border-strong); display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 700; }}
.otp span.on {{ border-color: var(--hd-focus); box-shadow: 0 0 0 3px var(--hd-focus-ring); }}
/* selection */
.check, .radio {{ width: 22px; height: 22px; border-radius: 8px; border: 1.75px solid var(--hd-track-strong); display: inline-flex; align-items: center; justify-content: center; flex: none; background: var(--hd-surface); }}
.radio {{ border-radius: 50%; }} .check.on {{ background: var(--hd-accent); border-color: var(--hd-accent); color: #fff; }}
.radio.on {{ border: 6.5px solid var(--hd-accent); }}
.switch {{ width: 44px; height: 26px; border-radius: 12px; background: var(--hd-track-strong); position: relative; flex: none; }} .switch::after {{ content: ''; position: absolute; width: 20px; height: 20px; border-radius: 50%; background: #fff; top: 3px; left: 3px; box-shadow: 0 1px 2px rgba(0,0,0,.2); }}
.switch.on {{ background: var(--hd-accent); }} .switch.on::after {{ left: 21px; }}
.chip {{ height: 36px; padding: 0 12px; border-radius: 10px; border: 1px solid var(--hd-border); display: inline-flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600; color: var(--hd-fg-muted); background: var(--hd-surface); white-space: nowrap; }}
.chip.on {{ border-color: var(--hd-accent); color: var(--hd-link); background: var(--hd-accent-subtle); }}
.slider {{ height: 6px; border-radius: 4px; background: var(--hd-track); position: relative; }} .slider i {{ position: absolute; inset: 0 40% 0 0; background: var(--hd-accent); border-radius: 4px; }}
.slider b {{ position: absolute; left: 60%; top: 50%; width: 22px; height: 22px; margin: -11px; border-radius: 50%; background: #fff; border: 2px solid var(--hd-accent); }}
/* tabs (underline) */
.tabs {{ display: flex; gap: 22px; border-bottom: 1px solid var(--hd-border); }} .tabs > span {{ display: flex; align-items: center; gap: 7px; padding: 11px 0; font-size: 15px; font-weight: 600; color: var(--hd-fg-muted); }}
.tabs > .on {{ color: var(--hd-fg); box-shadow: inset 0 -3px 0 var(--hd-accent); }}
/* badges, avatars */
.badge {{ font-size: 12px; font-weight: 700; padding: 3px 9px; border-radius: 999px; display: inline-flex; align-items: center; gap: 4px; white-space: nowrap; }}
.badge.success {{ background: var(--hd-success-subtle); color: var(--hd-success); }} .badge.warning {{ background: var(--hd-warning-subtle); color: var(--hd-warning); }}
.badge.danger {{ background: var(--hd-danger-subtle); color: var(--hd-danger); }} .badge.info {{ background: var(--hd-info-subtle); color: var(--hd-info); }}
.badge.neutral {{ background: var(--hd-bg-subtle); color: var(--hd-fg-muted); box-shadow: inset 0 0 0 1px var(--hd-border); }}
.dot {{ width: 8px; height: 8px; border-radius: 50%; background: var(--hd-accent); flex: none; }}
.av {{ width: 40px; height: 40px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: 700; font-size: 15px; flex: none; }}
.avs {{ display: flex; }} .avs .av {{ width: 30px; height: 30px; font-size: 12px; box-shadow: 0 0 0 2px var(--hd-surface); margin-left: -8px; }} .avs .av:first-child {{ margin-left: 0; }}
/* surfaces */
.card {{ background: var(--hd-surface-raised); border: 1px solid var(--hd-border); border-radius: var(--hd-radius-lg); }}
.row {{ background: var(--hd-surface-raised); border: 1px solid var(--hd-border); border-radius: var(--hd-radius-md); padding: 12px 14px; display: flex; align-items: center; gap: 12px; }}
.row img.lead {{ width: 48px; height: 48px; }} .row .tx {{ flex: 1; min-width: 0; }} .row .tx b {{ display: block; font-size: 15px; font-weight: 650; }}
.row .tx small {{ display: block; font-size: 13px; color: var(--hd-fg-muted); margin-top: 1px; }} .row .end {{ text-align: right; }} .row .end small {{ display: block; }}
.stack {{ display: flex; flex-direction: column; gap: 10px; }}
.notice {{ display: flex; gap: 10px; padding: 12px 14px; border-radius: 12px; font-size: 14px; line-height: 20px; align-items: flex-start; }}
.notice.info {{ background: var(--hd-info-subtle); color: var(--hd-info-strong); }} .notice.warning {{ background: var(--hd-warning-subtle); color: var(--hd-warning-strong); }}
.notice.success {{ background: var(--hd-success-subtle); color: var(--hd-success-strong); }} .notice.danger {{ background: var(--hd-danger-subtle); color: var(--hd-danger-strong); }}
.toast {{ display: inline-flex; gap: 12px; align-items: center; background: var(--hd-inverse); color: var(--hd-inverse-fg); border-radius: 12px; padding: 12px 14px 12px 12px; font-size: 14px; box-shadow: var(--hd-shadow-e3); }}
.toast .ok {{ width: 24px; height: 24px; border-radius: 50%; background: var(--hd-success-solid); color: #fff; display: flex; align-items: center; justify-content: center; }} .toast b {{ color: var(--hd-inverse-link); margin-left: 10px; }}
.tooltip {{ background: var(--hd-inverse); color: var(--hd-inverse-fg); font-size: 13px; padding: 7px 10px; border-radius: 8px; position: relative; display: inline-block; }}
.tooltip::after {{ content: ''; position: absolute; left: 50%; bottom: -5px; margin-left: -5px; border: 5px solid transparent; border-bottom: 0; border-top-color: var(--hd-inverse); }}
.tape {{ height: 8px; border-radius: 999px; background: var(--hd-track); overflow: hidden; }} .tape i {{ display: block; height: 100%; background: var(--hd-accent); border-radius: 999px; }}
.skel {{ background: linear-gradient(90deg, var(--hd-skeleton), var(--hd-skeleton-hi), var(--hd-skeleton)); border-radius: 8px; }}
.steps {{ display: flex; flex-direction: column; }} .step {{ display: grid; grid-template-columns: 28px 1fr; gap: 12px; position: relative; padding-bottom: 18px; }}
.step::before {{ content: ''; position: absolute; left: 13px; top: 28px; bottom: 0; width: 2px; background: var(--hd-border); }} .step:last-child::before {{ display: none; }}
.step.done::before {{ background: var(--hd-accent); }} .step .k {{ width: 28px; height: 28px; border-radius: 50%; border: 2px solid var(--hd-border-strong); display: flex; align-items: center; justify-content: center; background: var(--hd-surface); }}
.step.done .k {{ background: var(--hd-accent); border-color: var(--hd-accent); color: #fff; }} .step.now .k {{ border-color: var(--hd-accent); }} .step.now .k::after {{ content: ''; width: 10px; height: 10px; border-radius: 50%; background: var(--hd-accent); }}
.step b {{ display: block; font-size: 15px; }} .step small {{ font-size: 13px; color: var(--hd-fg-muted); }}
.stars {{ display: flex; gap: 4px; color: var(--hd-star); }}
.drop {{ border: 1.5px dashed var(--hd-border-strong); border-radius: 14px; padding: 18px; display: flex; flex-direction: column; align-items: center; gap: 6px; color: var(--hd-fg-muted); font-size: 14px; background: var(--hd-bg-subtle); }}
.kpi {{ padding: 16px; }} .kpi small {{ font-size: 13px; color: var(--hd-fg-muted); font-weight: 600; }} .kpi b {{ display: block; font-size: 28px; font-weight: 700; font-variation-settings: 'opsz' 48; letter-spacing: -.01em; margin: 4px 0 2px; }}
.delta {{ font-size: 13px; font-weight: 700; }} .delta.up {{ color: var(--hd-success); }} .delta.dn {{ color: var(--hd-danger); }}
.sheet {{ background: var(--hd-surface); border-radius: var(--hd-radius-xl) var(--hd-radius-xl) 0 0; padding: 10px 18px 24px; box-shadow: var(--hd-shadow-e3); }} .grab {{ width: 40px; height: 5px; border-radius: 4px; background: var(--hd-track-strong); margin: 0 auto 14px; }}
.dialog {{ background: var(--hd-surface); border-radius: var(--hd-radius-xl); padding: 22px; box-shadow: var(--hd-shadow-e3); width: 320px; }}
.menu {{ background: var(--hd-surface); border-radius: 14px; box-shadow: var(--hd-shadow-e2); border: 1px solid var(--hd-border); padding: 6px; width: 210px; }}
.menu div {{ display: flex; gap: 10px; align-items: center; padding: 9px 10px; border-radius: 10px; font-size: 14px; font-weight: 500; }} .menu .hl {{ background: var(--hd-bg-subtle); }} .menu .dg {{ color: var(--hd-danger); }}
.tbl {{ width: 100%; border-collapse: separate; border-spacing: 0; font-size: 14px; }} .tbl th {{ text-align: left; font-size: 13px; font-weight: 650; color: var(--hd-fg-muted); padding: 10px 14px; border-bottom: 1px solid var(--hd-border); }}
.tbl td {{ padding: 12px 14px; border-bottom: 1px solid var(--hd-border); vertical-align: middle; }} .tbl tr:last-child td {{ border-bottom: 0; }}
.bars {{ display: flex; align-items: flex-end; gap: 12px; height: 160px; padding-top: 8px; }} .bars div {{ flex: 1; display: flex; flex-direction: column; align-items: center; gap: 6px; height: 100%; justify-content: flex-end; }}
.bars i {{ width: 100%; border-radius: 6px 6px 2px 2px; background: var(--hd-data-1); display: block; }} .bars span {{ font-size: 12px; color: var(--hd-fg-subtle); }}

/* ===== refinement layer (Emil-style craft, AI-product restraint) ===== */
:root {{ --ease-out: cubic-bezier(0.23, 1, 0.32, 1); --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1); --hairline: var(--hd-border); }}
[data-theme="dark"] {{ --hairline: rgba(255,255,255,.07); }}
/* font pairing: Bricolage = brand voice (display, headings, hero numbers) · Geist = interface text · Geist Mono = codes */
:root {{ --font-brand: 'Bricolage Grotesque', ui-sans-serif, system-ui, sans-serif; --font-ui: 'Geist', ui-sans-serif, system-ui, sans-serif; --font-mono: 'Geist Mono', ui-monospace, monospace; }}
body, .btn, .input, .chip, .badge, .tbl, .toast, .tooltip, .menu {{ font-family: var(--font-ui); font-variation-settings: normal; }}
.t-display, .t-h1, .t-h2, .hero-num {{ font-family: var(--font-brand); }}
.mono {{ font-family: var(--font-mono); font-size: .92em; letter-spacing: 0; }}
body {{ letter-spacing: -0.006em; text-rendering: optimizeLegibility; font-feature-settings: 'ss01' off; }}
b, strong {{ font-weight: 600; }}
h1, h2, h3, .t-display, .t-h1, .t-h2 {{ text-wrap: balance; }} p {{ text-wrap: pretty; }}
.t-display {{ font-size: 32px; line-height: 36px; font-weight: 650; letter-spacing: -0.03em; font-variation-settings: 'opsz' 96; }}
.t-h1 {{ font-size: 24px; line-height: 30px; font-weight: 650; letter-spacing: -0.024em; font-variation-settings: 'opsz' 48; }}
.t-h2 {{ font-size: 19px; line-height: 25px; font-weight: 650; letter-spacing: -0.018em; font-variation-settings: 'opsz' 32; }}
.t-h3 {{ font-size: 15px; line-height: 21px; font-weight: 600; letter-spacing: -0.012em; }}
.t-body {{ font-size: 15px; line-height: 22px; }} .t-small {{ font-size: 13px; line-height: 18px; }} .t-cap {{ font-size: 12px; line-height: 16px; font-weight: 500; letter-spacing: 0; }}
.btn {{ font-weight: 560; font-size: 15px; letter-spacing: -0.01em; transition: transform 160ms var(--ease-out), background-color 160ms ease, box-shadow 160ms ease; }}
.btn:active {{ transform: scale(0.97); }}
.btn.p {{ box-shadow: inset 0 -1px 0 var(--hd-accent-pressed), inset 0 1px 0 rgba(255,255,255,.14), 0 1px 2px rgba(16,20,38,.10); }}
.btn.s {{ background: var(--hd-control); box-shadow: none; }}   /* owner rule: grey secondary, no border */ .btn.d {{ box-shadow: inset 0 -1px 0 var(--hd-danger-edge), 0 1px 2px rgba(16,20,38,.08); }}
.btn.prs {{ transform: scale(0.97); }}
@media (hover: hover) and (pointer: fine) {{ .btn.p:hover {{ background: var(--hd-accent-hover); }} .btn.s:hover {{ background: var(--hd-control-hover); }} .row:hover {{ box-shadow: var(--hd-shadow-e2); }} }}
.btn.sm {{ font-size: 13px; }} .btn.lg {{ height: 50px; font-size: 16px; border-radius: 14px; }}
.card {{ border: 1px solid var(--hairline); box-shadow: var(--hd-shadow-e1); }}
.row {{ border: 1px solid var(--hairline); box-shadow: var(--hd-shadow-e1); padding: 11px 12px; gap: 12px; transition: box-shadow 200ms ease; }}
.row .tx b {{ font-size: 14.5px; font-weight: 560; letter-spacing: -0.012em; }} .row .tx small {{ font-size: 12.5px; }}
.badge {{ font-size: 12px; font-weight: 550; padding: 2px 8px; border-radius: 6px; letter-spacing: 0; }}
.tabs {{ gap: 20px; }} .tabs > span {{ font-size: 14px; font-weight: 550; padding: 10px 0; }} .tabs > .on {{ box-shadow: inset 0 -2px 0 var(--hd-indicator); }}
.input {{ height: 44px; border-radius: 10px; border-color: var(--hd-border-input); font-size: 15px; font-weight: 450; transition: border-color 160ms ease, box-shadow 160ms ease; }}
.input.textarea {{ height: 96px; }} .field > label {{ font-size: 13px; font-weight: 550; color: var(--hd-fg); }}
.search {{ background: var(--hd-surface); border-color: var(--hd-hairline, var(--hd-border)); box-shadow: var(--hd-shadow-e1); }}
.chip {{ height: 32px; border-radius: 10px; font-size: 13px; font-weight: 550; border-color: var(--hairline); }}
.kpi small {{ font-size: 12.5px; font-weight: 500; }} .kpi b {{ font-size: 24px; font-weight: 600; letter-spacing: -0.03em; }}
.delta {{ font-size: 12.5px; font-weight: 600; }}
img[src*="/products/p"] {{ outline: 1px solid rgba(0,0,0,.06); outline-offset: -1px; }}
.av {{ font-weight: 600; letter-spacing: -0.01em; }}
.topbar {{ height: 48px; }} .topbar > .ic, .topbar > span > .ic {{ box-sizing: content-box; padding: 11px; margin: -11px; }} .topbar .ttl {{ font-size: 16px; font-weight: 600; letter-spacing: -0.012em; }}
.tabbar {{ height: 60px; border-top-color: var(--hairline); }} .tabbar div {{ font-size: 10.5px; font-weight: 550; gap: 2px; flex: 1; height: 100%; justify-content: center; }}
.phone .scr {{ background: var(--hd-canvas); }} .cta {{ background: color-mix(in oklab, var(--hd-surface) 92%, transparent); border-top-color: var(--hairline); }}
.notice {{ font-size: 13.5px; border-radius: 10px; }} .toast {{ font-size: 13.5px; }}
.step b {{ font-size: 14.5px; font-weight: 600; }} .step small {{ font-size: 12.5px; }}
.tbl th {{ font-size: 12.5px; font-weight: 550; }} .tbl td {{ font-size: 13.5px; }}
.sheet {{ border-radius: 24px 24px 0 0; }} .dialog {{ border-radius: 16px; }}
.switch {{ transition: background-color 200ms ease; }} .switch::after {{ transition: transform 200ms var(--ease-out); box-shadow: 0 1px 2px rgba(16,20,38,.2), 0 0 0 .5px rgba(16,20,38,.06); }}
/* avatars: solid brand colours */
.av-0 {{ background: {C['600']}; color: #fff; }} .av-1 {{ background: {V['600']}; color: #fff; }} .av-2 {{ background: {M['300']}; color: {I['900']}; }}
.av-3 {{ background: {N['700']}; color: #fff; }} .av-4 {{ background: {I['600']}; color: #fff; }}
/* inputs, refined */
@media (hover: hover) and (pointer: fine) {{ .input:not(.foc):not(.err):not(.dis):hover {{ border-color: var(--hd-border-input-hover); }} }}
.input.hov {{ border-color: var(--hd-border-input-hover); }}
.input .addon {{ align-self: stretch; margin-left: -14px; padding: 0 12px; display: flex; align-items: center; border-right: 1px solid var(--hd-border); background: var(--hd-bg-subtle); border-radius: 12px 0 0 12px; color: var(--hd-fg-muted); font-weight: 550; }}
.input .trail {{ margin-left: auto; display: flex; align-items: center; gap: 8px; color: var(--hd-fg-subtle); }}
.input > .ic:first-child {{ color: var(--hd-fg-subtle); }}
.input.ok {{ border-color: var(--hd-success); }}
.field .labrow {{ display: flex; justify-content: space-between; align-items: baseline; }} .field .labrow label {{ font-size: 13px; font-weight: 550; }} .field .labrow span {{ font-size: 12px; color: var(--hd-fg-subtle); }}
.help {{ display: flex; align-items: center; gap: 5px; }} .help.ok {{ color: var(--hd-success); font-weight: 500; }} .help .cnt {{ margin-left: auto; font-variant-numeric: tabular-nums; }}
/* alerts: solid icons, no borders */
.notice {{ gap: 10px; padding: 12px 14px; align-items: flex-start; }} .notice .icf {{ flex: none; margin-top: 1px; }}
.notice.info .icf {{ color: var(--hd-accent); }} .notice.warning .icf {{ color: var(--hd-warning); }} .notice.success .icf {{ color: var(--hd-success); }} .notice.danger .icf {{ color: var(--hd-danger); }}
.notice b {{ font-weight: 600; }}
/* avatar group: cut-out overlap instead of rings */
.avs .av {{ box-shadow: none !important; margin-left: -6px; -webkit-mask: radial-gradient(circle at calc(100% + 9px) 50%, transparent 17px, #000 17.5px); mask: radial-gradient(circle at calc(100% + 9px) 50%, transparent 17px, #000 17.5px); }}
.avs .av:first-child {{ margin-left: 0; }} .avs .av:last-child {{ -webkit-mask: none; mask: none; }}
/* toast: hug content, action on the right */
.stack > .toast, .box > .toast {{ align-self: flex-start; }} .toast {{ gap: 10px; padding: 10px 12px 10px 10px; min-width: 260px; }} .toast b {{ margin-left: auto; padding-left: 18px; }}
/* grouped list (nav/settings menus only) */
.group {{ background: var(--hd-surface-raised); border: 1px solid var(--hairline); border-radius: 16px; overflow: hidden; box-shadow: var(--hd-shadow-e1); }}
.group .gi {{ display: flex; align-items: center; gap: 12px; padding: 0 14px; height: 52px; position: relative; }}
.group .gi + .gi::before {{ content: ''; position: absolute; top: 0; left: 46px; right: 0; height: 1px; background: var(--hairline); }}
.group .gi > .ic:first-child {{ color: var(--hd-fg-muted); }} .group .gi b {{ flex: 1; font-size: 14.5px; font-weight: 500; letter-spacing: -0.012em; }}
.group .gi .meta {{ font-size: 13px; color: var(--hd-fg-muted); }} .group .gi .chevr {{ color: var(--hd-fg-subtle); }}
.ghead {{ font-size: 12.5px; font-weight: 550; color: var(--hd-fg-muted); margin: 6px 4px -6px; }}
.statbar {{ display: grid; grid-template-columns: repeat(3, 1fr); padding: 12px 0; }} .statbar > div {{ text-align: center; }} .statbar > div + div {{ border-left: 1px solid var(--hairline); }}
.statbar b {{ display: block; font-size: 19px; font-weight: 650; letter-spacing: -0.02em; }} .statbar small {{ font-size: 12px; color: var(--hd-fg-muted); }}
.vhex {{ display: inline-block; vertical-align: -2px; }}
/* micro-interactions: hover only on fine pointers, press everywhere, keyboard focus ring */
.chip, .row, .nav, .tabs > span, .iconbtn, .gi, .pager span, .qty span, .tag, .ci {{ transition: background-color 150ms ease, color 150ms ease, box-shadow 200ms ease, transform 160ms var(--ease-out); }}
@media (hover: hover) and (pointer: fine) {{
  .chip:hover {{ border-color: var(--hd-border-strong); color: var(--hd-fg); }} .nav:not(.on):hover {{ background: color-mix(in oklab, var(--hd-fg) 5%, transparent); color: var(--hd-fg); }}
  .tabs > span:not(.on):hover {{ color: var(--hd-fg); }} .iconbtn:hover {{ background: color-mix(in oklab, var(--hd-fg) 6%, transparent); color: var(--hd-fg); }}
  .gi:hover {{ background: color-mix(in oklab, var(--hd-fg) 3%, transparent); }} .pager span:not(.on):hover {{ background: color-mix(in oklab, var(--hd-fg) 5%, transparent); }}
  .ci:hover {{ background: var(--hd-bg-subtle); }} .btn.g:hover {{ background: var(--hd-accent-subtle); }}
}}
.chip:active, .row:active, .iconbtn:active, .gi:active, .pager span:active, .qty span:active {{ transform: scale(0.98); }}
.btn:focus-visible, .chip:focus-visible, .iconbtn:focus-visible, .switch:focus-visible {{ outline: 2px solid var(--hd-focus); outline-offset: 2px; }}
button.btn {{ -webkit-tap-highlight-color: transparent; user-select: none; }}
input.switch {{ appearance: none; margin: 0; cursor: pointer; }} input.switch:checked {{ background: var(--hd-accent); }} input.switch:checked::after {{ transform: translateX(18px); }}
.switch.on::after {{ left: 3px; transform: translateX(18px); }}
/* buttons: loading, group, link */
.spin {{ width: 16px; height: 16px; border-radius: 50%; border: 2px solid currentColor; border-right-color: transparent; animation: spin 700ms linear infinite; opacity: .9; }}
@keyframes spin {{ to {{ transform: rotate(360deg); }} }}
.btngroup {{ display: inline-flex; }} .btngroup .btn {{ border-radius: 0; }} .btngroup .btn:first-child {{ border-radius: 12px 0 0 12px; }} .btngroup .btn:last-child {{ border-radius: 0 12px 12px 0; padding: 0 12px; }}
.btngroup .btn.p + .btn.p {{ box-shadow: inset 1px 0 0 rgba(255,255,255,.22), inset 0 -1px 0 var(--hd-accent-pressed); }} .btngroup .btn.s + .btn.s {{ box-shadow: inset 1px 0 0 var(--hd-control-edge); }}
.btn.link {{ background: none; padding: 0; height: auto; color: var(--hd-link); font-weight: 550; box-shadow: none; text-decoration: underline; text-decoration-color: color-mix(in oklab, var(--hd-link) 35%, transparent); text-underline-offset: 3px; }}
/* ===== focus: one ring everywhere (2px gap in the surface colour, 2px focus colour) ===== */
:root {{ --ring-gap: var(--hd-surface); }} .box, .phone .scr, .sb {{ --ring-gap: var(--hd-canvas); }}
.btn.foc, .btn:focus-visible, .chip.foc, .chip:focus-visible, .iconbtn:focus-visible, .tabs > span:focus-visible, .row.foc, .check.foc, .radio.foc, .switch.foc, input.switch:focus-visible, .nav:focus-visible {{
  outline: none; box-shadow: 0 0 0 2px var(--ring-gap), 0 0 0 4px var(--hd-focus) !important; }}
.input.foc, .otp span.on {{ border-color: var(--hd-focus); box-shadow: inset 0 0 0 1px var(--hd-focus) !important; }}
.input.err {{ box-shadow: inset 0 0 0 1px var(--hd-danger) !important; }}
/* ===== solid over tint (alerts stay tinted) ===== */
.badge {{ border-radius: 6px; }}
.badge.success {{ background: {N['700']}; color: #fff; }} .badge.warning {{ background: {M['300']}; color: {I['900']}; }}
.badge.danger {{ background: {V['600']}; color: #fff; }} .badge.info {{ background: {C['600']}; color: #fff; }}
.badge.neutral {{ background: var(--hd-control); color: var(--hd-fg); }}
.chip.on {{ background: var(--hd-fg); color: var(--hd-bg); border-color: var(--hd-fg); }}
.row.sel {{ background: var(--hd-surface-raised); border-color: var(--hd-accent); box-shadow: inset 0 0 0 1px var(--hd-accent); }}
.btn.g.hov, .btn.hov.g {{ background: var(--hd-control); }}
@media (hover: hover) and (pointer: fine) {{ .btn.g:hover {{ background: var(--hd-control); }} }}
/* ===== radius: one scale, concentric (inner ≈ outer − padding) ===== */
.btn {{ border-radius: 12px; }} .btn.sm {{ border-radius: 8px; }} .btn.lg {{ border-radius: 14px; }}
.input, .search, .otp span {{ border-radius: 12px; }} .input .addon {{ border-radius: 12px 0 0 12px; }}
.chip {{ border-radius: 8px; }} .tag {{ border-radius: 6px; }} .kbd {{ border-radius: 6px; }}
.row {{ border-radius: 12px; }} .row img.lead {{ border-radius: 6px; }} .card, .panel, .group {{ border-radius: 16px; }}
.card img[src*="/products/p"], .panel img[src*="/products/p"] {{ border-radius: 8px; }}
.notice {{ border-radius: 12px; }} .toast {{ border-radius: 12px; }} .tooltip {{ border-radius: 8px; }}
.menu {{ border-radius: 14px; }} .menu div {{ border-radius: 8px; }} .dialog {{ border-radius: 24px; }} .sheet {{ border-radius: 24px 24px 0 0; }}
/* ===== radius by maths =====
   concentric (inner sits near a corner, gap < outer): inner = max(outer − gap, 4)
   free-standing: radius ≈ height × 0.27  (44→12 · 32→8 · 28→8 · 22→6 · 20→6) */
.check {{ border-radius: 6px; }} .cnt-b {{ border-radius: 6px; }} .tag {{ border-radius: 8px; }} .pager span {{ border-radius: 8px; }} .qty {{ border-radius: 12px; }}
.phone {{ border-radius: 52px; }} .phone .scr {{ border-radius: 42px; }}
.row img.lead, .row > .av {{ }} .row img.lead {{ border-radius: 4px; }}
.card img[src*="/products/p"], .panel img[src*="/products/p"] {{ border-radius: 4px; }}
.ctip {{ border-radius: 8px; }} .cmdk .ci {{ border-radius: 8px; }} .cmdk .ci img {{ border-radius: 4px; }}
.banner .bi {{ border-radius: 4px; }} .upl img {{ border-radius: 4px !important; }}
.dialog {{ padding: 20px; }}
/* ===== shadows: only things that float get one ===== */
.card, .row:not(.sel), .panel, .group, .search, .banner, .stat {{ box-shadow: none !important; }}
.ws {{ background: var(--hd-surface) !important; box-shadow: 0 0 0 1px var(--hd-border) !important; }}
.sbsearch {{ background: var(--hd-control) !important; border: 0 !important; box-shadow: none !important; color: var(--hd-fg-muted); }}
.nav.on {{ box-shadow: 0 0 0 1px var(--hairline) !important; }}
.menu, .toast, .dialog, .sheet, .tooltip, .ctip, .cmdk, .drawer {{ box-shadow: var(--hd-shadow-e3); }}
.sel-row td {{ background: var(--hd-control) !important; }}
/* ===== buttons, refined ===== */
.btn:not(.icon):not(.link) {{ min-width: 88px; }} .btn.sm:not(.icon) {{ min-width: 0; }}
.btn:has(> .ic:first-child):not(.icon) {{ padding-left: 14px; }} .btn:has(> .ic:last-child):not(.icon) {{ padding-right: 14px; }} .btn.sm:has(> .ic:first-child) {{ padding-left: 10px; }}
.btn .ic {{ width: 18px; height: 18px; }} .btn.sm .ic {{ width: 16px; height: 16px; }} .btn.lg .ic {{ width: 20px; height: 20px; }}
.btn.dis, .btn:disabled {{ opacity: 1; background: var(--hd-control) !important; color: var(--hd-fg-subtle) !important; box-shadow: none !important; cursor: not-allowed; }}
.btn.g.dis, .btn.g:disabled {{ background: transparent !important; }}
.btn[aria-busy="true"] {{ pointer-events: none; }}
/* ===== search ===== */
.search {{ background: var(--hd-control) !important; border: 0 !important; box-shadow: none !important; height: 40px; border-radius: 12px; padding: 0 12px; gap: 8px; color: var(--hd-fg-muted); font-size: 15px; }}
.search > .ic:first-child {{ color: var(--hd-fg-muted); }} .search .q {{ color: var(--hd-fg); flex: 1; }} .search .q b {{ font-weight: 600; }}
.search.foc {{ background: var(--hd-surface) !important; box-shadow: inset 0 0 0 2px var(--hd-focus) !important; }}
.search .clr {{ width: 18px; height: 18px; border-radius: 50%; background: var(--hd-fg-subtle); color: var(--hd-canvas); display: inline-flex; align-items: center; justify-content: center; flex: none; margin-left: auto; }}
.search .kbd {{ margin-left: auto; }}
.searchbar {{ display: flex; align-items: center; gap: 12px; padding: 4px 18px 8px; flex: none; }} .searchbar .search {{ flex: 1; }}
.chiprow {{ display: flex; gap: 8px; overflow: hidden; white-space: nowrap; margin-right: -18px; }}
.suggest {{ background: var(--hd-overlay); border-radius: 16px; box-shadow: var(--hd-shadow-e3), 0 0 0 1px var(--hairline); padding: 6px; }}
.suggest .sg-h {{ font-size: 12px; font-weight: 550; color: var(--hd-fg-muted); padding: 8px 10px 4px; }}
.suggest .sg {{ display: flex; align-items: center; gap: 10px; height: 40px; padding: 0 10px; border-radius: 10px; font-size: 14.5px; color: var(--hd-fg); }}
.suggest .sg .ic {{ color: var(--hd-fg-subtle); }} .suggest .sg.hl {{ background: var(--hd-control); }} .suggest .sg .sub {{ margin-left: auto; font-size: 12.5px; color: var(--hd-fg-muted); }}
.suggest .sg img {{ width: 28px; height: 28px; border-radius: 6px; }} .suggest .sg b {{ font-weight: 600; }} .suggest .sg span.m {{ color: var(--hd-fg-muted); }}
.suggest .sg-f {{ display: flex; gap: 14px; padding: 8px 10px 4px; border-top: 1px solid var(--hairline); margin-top: 4px; font-size: 12px; color: var(--hd-fg-muted); align-items: center; }}
@media (prefers-reduced-motion: reduce) {{ * {{ transition-duration: 0ms !important; }} }}
/* phone */
.phone {{ width: 390px; height: 844px; border-radius: 52px; background: #000; padding: 10px; flex: none; box-shadow: 0 8px 24px rgba(16,20,38,.06); }}
.scr {{ width: 370px; height: 824px; border-radius: 43px; overflow: hidden; position: relative; background: var(--hd-bg); color: var(--hd-fg); display: flex; flex-direction: column; }}
.sbar {{ height: 50px; display: flex; align-items: center; justify-content: space-between; padding: 6px 28px 0 34px; font-size: 15px; font-weight: 700; flex: none; }}
.sbar .r {{ display: flex; gap: 6px; align-items: center; }} .sbar .bat {{ width: 25px; height: 12px; border-radius: 4px; border: 1.5px solid currentColor; position: relative; }} .sbar .bat::after {{ content: ''; position: absolute; inset: 1.5px 5px 1.5px 1.5px; background: currentColor; border-radius: 2px; }}
.topbar {{ height: 52px; display: flex; align-items: center; gap: 12px; padding: 0 18px; flex: none; }} .topbar .ttl {{ flex: 1; font-size: 17px; font-weight: 700; }} .topbar .ic {{ color: var(--hd-fg); }}
.body {{ flex: 1; overflow: hidden; padding: 4px 18px 18px; display: flex; flex-direction: column; gap: 16px; }} .body > * {{ flex-shrink: 0; }}
.home-ind {{ height: 30px; display: flex; align-items: center; justify-content: center; flex: none; }} .home-ind i {{ width: 134px; height: 5px; border-radius: 4px; background: var(--hd-fg); opacity: .9; }}
.tabbar {{ height: 64px; border-top: 1px solid var(--hd-border); display: flex; justify-content: space-around; align-items: center; flex: none; background: var(--hd-surface); }}
.tabbar div {{ display: flex; flex-direction: column; align-items: center; gap: 3px; font-size: 11px; font-weight: 600; color: var(--hd-fg-subtle); }} .tabbar .on {{ color: var(--hd-link); }}
.cta {{ padding: 12px 18px 4px; border-top: 1px solid var(--hd-border); display: flex; gap: 10px; background: var(--hd-surface); flex: none; }}
.scrim {{ position: absolute; inset: 0; background: rgba(13,14,18,.48); }}
.overlay {{ position: absolute; left: 0; right: 0; bottom: 0; }}
"""

def phone(inner, theme="light", label="", sbar_color=None):
    return (f'<figure class="pf"><div class="phone"><div class="scr" data-theme="{theme}">'
            f'<div class="sbar" style="{f"color:{sbar_color}" if sbar_color else ""}"><span class="num">9:41</span><span class="r"><svg width="18" height="12" viewBox="0 0 18 12" fill="currentColor" aria-hidden="true"><rect x="0" y="8" width="3" height="4" rx=".8"/><rect x="5" y="5.5" width="3" height="6.5" rx=".8"/><rect x="10" y="3" width="3" height="9" rx=".8"/><rect x="15" y="0" width="3" height="12" rx=".8"/></svg><svg width="17" height="12" viewBox="0 0 17 12" fill="currentColor" aria-hidden="true"><path d="M8.5 2.3c2.3 0 4.4.9 6 2.4l1.1-1.2A10.2 10.2 0 0 0 8.5.6 10.2 10.2 0 0 0 1.4 3.5l1.1 1.2c1.6-1.5 3.7-2.4 6-2.4Z"/><path d="M8.5 5.6c1.4 0 2.6.5 3.6 1.4l1.1-1.2A7 7 0 0 0 8.5 3.9 7 7 0 0 0 3.8 5.8l1.1 1.2c1-.9 2.2-1.4 3.6-1.4Z"/><path d="M8.5 8.9c.5 0 .9.2 1.2.5L8.5 11 7.3 9.4c.3-.3.7-.5 1.2-.5Z"/></svg><span class="bat"></span></span></div>'
            f'{inner}<div class="home-ind"><i></i></div></div></div><figcaption>{label}</figcaption></figure>')

def tabbar(active):
    """Labelled 4-item tab bar: every destination keeps its name (icon-only tabs hurt recognition); the active one is solid + Cobalt."""
    items = [("home", "Home"), ("box", "Drops"), ("wallet", "Wallet"), ("user", "You")]
    return '<div class="tabbar">' + "".join(f'<div class="{"on" if n == active else ""}">{ics(i, 24) if n == active else ic(i, 24)}<span>{n}</span></div>' for i, n in items) + '</div>'

from xcss import XCSS
CSS += XCSS
from xshadow import XSHADOW
CSS += XSHADOW
from xcomp import XCOMP
CSS += XCOMP
from xchart import XCHART
CSS += XCHART
from xnew import XNEW
CSS += XNEW
from xpass import XPASS
CSS += XPASS
from xsteps import XSTEPS
CSS += XSTEPS
from xlead import XLEAD
CSS += XLEAD

def av(t, k=0, size=None):
    """Initials avatar; tint comes from the theme (av-0..4), never inline colour."""
    st = f' style="width:{size}px;height:{size}px;font-size:{size*0.38:.0f}px"' if size else ""
    return f'<span class="av av-{k % 5}"{st}>{t}</span>'
