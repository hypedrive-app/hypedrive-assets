# ---- brandx_pages.py: new pages ------------------------------------------------------------------------------------------
xcss("""
.fgc { font: 15px/1.45 var(--hd-font-ui); color: ${i600}; margin: 10px 0 0; } .fgc b { color: ${ink}; font-weight: 650; }
.shd { display: block; border-radius: 10px; box-shadow: 0 0 0 1px ${i200}, 0 18px 40px -20px rgba(16,20,38,.3); }
.sheet2 { display: grid; gap: 40px; align-items: start; }
.tile6 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px 22px; } .tile6 figure { margin: 0; } .tile6 .fr { height: 205px; border-radius: 18px; overflow: hidden; position: relative; background: ${i100}; } .tile6 .fr > img { width: 100%; height: 100%; object-fit: cover; display: block; }
.tile6 figcaption { font: 15px/1.45 var(--hd-font-ui); color: ${i700}; margin-top: 10px; }
.mini2 { border-radius: 18px; overflow: hidden; } .mini2 svg, .mini2 img { display: block; width: 100%; }
.col4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 28px; } .col4 > div { border-top: 3px solid ${ink}; padding-top: 12px; } .col4 b { display: block; font: 650 20px var(--hd-font-display); margin-bottom: 4px; } .col4 p { margin: 0; font: 16px/1.5 var(--hd-font-ui); color: ${i700}; }
.tint { background: ${i50}; border-radius: 22px; }
""")
def tile(cls, inner, cap_ok, cap, desc, ok=True):
    return f'<figure><div class="fr {cls}">{inner}</div><figcaption>{tag_do(cap) if ok else tag_no(cap)}{desc}</figcaption></figure>'
def svgf(svg, w=None, cls="shd", alt="Hypedrive asset"): return img(svg, (f"width:{w}px;" if w else ""), cls, alt)
def mini_svg(body, w=460, h=205, bg="#fff"): return svg_wrap(w, h, f'<rect width="{w}" height="{h}" fill="{bg}"/>{body}')

# ================================================================ motifs
def _m_tape_do():
    return mini_svg(T("Hype out.", 38, 30, 106, "#fff", 700, opsz=72) + T("Products in.", 38, 30, 56, "#fff", 700, opsz=72) + f'<g transform="translate(0 135)">{tape_band(460, 52, COB, "#ffffff", "dark")}</g>', bg=INK)
def _m_hex_do():
    return mini_svg(hex_photo("mh1", "p5.jpg", 230, 103, 88, crop=(0, 0.02, 1, 0.98), maxw=500), bg=SCALES["cobalt"][600])
def _m_label_do():
    return mini_svg(place(label_motif(), 100, 20, w=260)[0], bg=I[100])
def _m_tape_no():
    return mini_svg(T("Products in.", 38, 30, 70, INK, 700, opsz=72) + f'<g transform="translate(80 100) rotate(-14 130 26)">{tape_band(260, 52, COB, "#ffffff", "dark")}</g>', bg="#fff")
def _m_hex_no():
    c30 = math.cos(math.radians(30)); s = 62; cx, cy = 230, 103
    pts = [(cx - s, cy), (cx - s/2, cy - c30*s), (cx + s/2, cy - c30*s), (cx + s, cy), (cx + s/2, cy + c30*s), (cx - s/2, cy + c30*s)]
    return mini_svg(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{COB}"/>' + mono_mark("#fff", cx - 28, cy - 28, 56), bg="#fff")
def _m_all_no():
    return mini_svg(hexp(70, 60, 44, MAR) + hexp(400, 150, 44, VER) + f'<g transform="translate(0 92)">{tape_band(460, 34, COB, "#ffffff", "dark")}</g>' + place(label_motif(), 150, 14, w=130)[0] + ill_at("parcel", "light", 330, 6, 80) + ill_at("parcel", "light", 20, 120, 80), bg="#fff")
PG_MOTIFS = [
 page(head("00", "Four motifs from one logo", "The identity borrows four shapes from the parcel itself. Use them to give a layout its character, one at a time, in place of decoration.") +
      f'<div class="mini2" style="margin-top:6px">{img(MOTIF_SHEET, "width:100%", alt="The four motifs")}</div>'
      '<div class="col4" style="margin-top:30px">' + "".join(f'<div><b>{t}</b><p>{d}</p></div>' for t, d in [
          ("The tape band", "A strip of packing tape with the lockup repeated in whole units. It runs edge to edge, like tape across a lid."),
          ("The hexagon", "The parcel’s silhouette, taken from the dot of the i. It holds a mark, a glyph or one photograph."),
          ("The label", "The shipping label as a card: a small lockup, an ink tag, hairline rules and a code. For anything that carries facts."),
          ("The parcel", "The isometric cube. The mark, and the starting point of every illustration in the family.")]) + '</div>'),
 page(head("00", "Using the motifs", "One motif leads each layout, a second may support it. Together they should read as a parcel that has just arrived, not as a pattern.") +
      '<div class="tile6">' + tile("", f'<div class="mini2">{img(_m_tape_do(), "", "", "Tape band across the bottom")}</div>', 0, "Tape runs edge to edge", "Horizontal or vertical, bleeding off both sides, with a clear area above it. One band per layout.")
      + tile("", f'<div class="mini2">{img(_m_hex_do(), "", "", "Hexagon photo")}</div>', 0, "Hexagon holds one thing", "A single photograph or mark, point up, with soft corners. Never a pattern of them.")
      + tile("", f'<div class="mini2">{img(_m_label_do(), "", "", "Label card")}</div>', 0, "The label carries facts", "Names, addresses, tracking codes. Geist for the text, Geist Mono for codes only.")
      + tile("", f'<div class="mini2">{img(_m_tape_no(), "", "", "Tilted short tape")}</div>', 0, "Don’t tilt or shorten the tape", "A short strip floating at an angle looks like a sticker. Tape always spans the whole width.", False)
      + tile("", f'<div class="mini2">{img(_m_hex_no(), "", "", "Rotated hexagon")}</div>', 0, "Don’t rotate the hexagon", "Flat-top is a different shape. The point stays up, as in the wordmark.", False)
      + tile("", f'<div class="mini2">{img(_m_all_no(), "", "", "All motifs at once")}</div>', 0, "Don’t stack every motif", "Four motifs and three colours on one page is noise. Pick a lead.", False) + '</div>'),
]
for _p in PG_MOTIFS: pass

# ================================================================ packaging
PG_PACK = [
 page(head("00", "Box system", "Brands pack their own products. Hypedrive adds the tape and the label, so any box reads as one of ours the moment it arrives.") +
      f'<div class="mini2" style="padding:0;margin-top:0;text-align:center;box-shadow:inset 0 0 0 1px rgba(16,20,38,.1)">{img(PKG_ASSETS["boxes"], "width:1130px;margin:0 auto", alt="Three box sizes with tape and label placement")}</div>'
      '<div class="col4" style="grid-template-columns:repeat(3,1fr);margin-top:18px">' + "".join(f'<div><b>{t}</b><p>{d}</p></div>' for t, d in [
          ("Three sizes cover a drop", "Small for a single bottle or tube, medium for a set, large for bulkier products. Sizes shown are a starting point; use the nearest stock box."),
          ("Tape over the lid, down the side", "One Cobalt strip across the middle of the lid and down the side, so the seal is also the signature. Vermilion tape marks a return."),
          ("Label on the side, never the lid", "The 4 × 6 in shipping label sits on a side face beside the tape, flat and clear of every edge and seam.")]) + '</div>'),
 page(head("00", "Mailer and thank-you card", "For soft goods the mailer carries the brand; inside every parcel a card says thank you and tells the creator what happens next.") +
      f'<div class="sheet2" style="grid-template-columns:auto 1fr;gap:56px"><div>{svgf(PKG_ASSETS["mailer"], 400, alt="Branded mailer")}<p class="fgc"><b>Mailer, front.</b> Ink bag, Cobalt peel-and-press strip, the parcel at full size.</p></div>'
      f'<div style="display:grid;gap:22px"><div style="display:grid;grid-template-columns:1fr 1fr;gap:22px"><div>{svgf(PKG_ASSETS["card_f"], 440, alt="Thank-you card front")}<p class="fgc"><b>Card, front.</b> Marigold with the gift illustration.</p></div>'
      f'<div>{svgf(PKG_ASSETS["card_b"], 440, alt="Thank-you card back")}<p class="fgc"><b>Card, back.</b> White, with the brand stripe.</p></div></div>'
      + rules([("Card: A6, 148 × 105 mm", "Printed on uncoated stock, 350 gsm. The line is “Thanks for trying it first.” and nothing else on the front."),
               ("Mailer: Ink, one Cobalt strip", "The one-colour mark is for tape and labels; the full-colour parcel appears once, large, on the mailer front.")]) + '</div></div>'),
 page(head("00", "Stickers and tape", "Small, cheap and kept. Stickers use the die-cut white border; tape comes in Cobalt for sealing and Marigold for gifts and extras.") +
      f'<div class="sheet2" style="grid-template-columns:900px 1fr;gap:44px"><div>{svgf(PKG_ASSETS["stickers"], 900, alt="Sticker sheet")}<p class="fgc"><b>Sticker sheet.</b> Parcel, hexagon, the line, and the gift. A 3 mm white border on each.</p></div>'
      + rules([("One idea per sticker", "A mark, a shape or a line. Never a mark and a line together."), ("White die-cut border", "3 mm of white around every sticker so it reads on any laptop or bottle."), ("Full colour only on white", "On dark tape or sheets, use the one-colour mark.")]) + '</div>'
      f'<div style="margin-top:22px;display:grid;gap:10px">{svgf(TAPE_COB, 1424, "mini2", "Cobalt tape")}{svgf(TAPE_MAR, 1424, "mini2", "Marigold tape")}</div>'),
]

# ================================================================ campaign
def kvfig(k, h, cap, desc): return f'<figure style="margin:0">{svgf(KV[k], None, alt=cap).replace("<img ", f"<img height=\'{h}\' ").replace("class=\"shd\"", "class=\"shd\" style=\"height:%dpx;width:auto\"" % h)}<p class="fgc"><b>{cap}.</b> {desc}</p></figure>'
PG_CAMP = [
 page(head("00", "Key visuals", "Three poster layouts that all use the same four parts: a real product photo, the parcel, the line and the brand colours.") +
      '<div style="display:grid;grid-template-columns:repeat(3,432px);gap:36px;justify-content:space-between">'
      + kvfig("ink", 540, "Ink, photo first", "The default. Photo on top, the parcel breaks its corner, the line below, tape at the foot.")
      + kvfig("cobalt", 540, "Cobalt, hexagon", "For a single hero product. The hexagon is the only frame and the line sits above it.")
      + kvfig("marigold", 540, "Marigold, tape split", "For the honest-review message. Full&#8209;bleed photo above a tape band, then the headline.") + '</div>'),
 page(head("00", "The key visual formula", "Every campaign layout has the same anatomy, so a new one can be made without a designer and still look like us.") +
      f'<div class="sheet2" style="grid-template-columns:960px 1fr;gap:56px"><div>{svgf(KV["wide"], 960, alt="Wide banner key visual")}<p class="fgc"><b>Wide banner, 16:9.</b> The same parts for web heroes and screens: photo left, Ink panel right.</p></div>'
      + rules([("1. A real product photo", "Bare and unretouched, at least half of the layout. It is the proof."), ("2. One parcel illustration", "One, large, breaking an edge. Never over the product."),
               ("3. The line in Bricolage 700", "“Hype out.” in Marigold on Ink and Cobalt, Ink on Marigold. Two lines at most."), ("4. One tape band or one hexagon", "The motif that frames the layout. Not both."),
               ("5. The lockup, small", "In a corner, in the one-colour version over photos.")]) + '</div>'),
]

# ================================================================ social: profiles, linkedin, youtube
PG_SOCIAL = [
 page(head("00", "Social: profile and link", "A square avatar, a wide banner and a link preview. All three lead with the parcel on Ink.") +
      f'<div class="sheet2" style="grid-template-columns:760px 1fr;gap:44px"><div>{svgf(APPS["og"], 760, alt="Link preview")}<p class="fgc"><b>Link preview, 1200 × 630.</b> Shown when the site is shared.</p></div>'
      f'<div style="display:grid;gap:26px"><div style="display:grid;grid-template-columns:200px 1fr;gap:26px;align-items:start"><div>{img(APPS["avatar"], "width:200px;border-radius:50%", "", "Avatar")}<p class="fgc"><b>Avatar, 800 px.</b> The parcel on Ink, round crop safe.</p></div>'
      + rules([("Circle-safe", "The mark sits inside the central 60% so no platform crop touches it.")]) + f'</div><div>{svgf(APPS["banner"], 620, alt="Banner")}<p class="fgc"><b>Banner, 1500 × 500.</b> Lockup, line and three illustrations.</p></div></div></div>'),
 page(head("00", "Social: LinkedIn and YouTube", "Two more templates. LinkedIn is a banner behind a profile photo; YouTube is a thumbnail that has to read at the size of a thumb.") +
      f'<div class="sheet2" style="grid-template-columns:1000px 1fr;gap:40px"><div>{svgf(APPS3["li"], 1000, alt="LinkedIn banner")}<p class="fgc"><b>LinkedIn banner, 1584 × 396.</b> The left 400 px stay empty: the profile photo sits there.</p></div>'
      + rules([("Keep the left clear", "LinkedIn draws the profile photo over the lower left. Nothing important goes there."), ("Tape along the foot", "The band is the only hard edge and keeps the banner grounded.")]) + '</div>'
      f'<div class="sheet2" style="grid-template-columns:420px 1fr;gap:40px;margin-top:22px"><div>{svgf(APPS3["yt"], 420, alt="YouTube thumbnail")}<p class="fgc"><b>YouTube thumbnail, 1280 × 720.</b></p></div>'
      + rules([("Four words or fewer", "Bricolage 700, Paper on Ink with the second line in Marigold. It must read at 120 px wide."), ("Photo and text never overlap", "Text sits on the Ink panel; the photo gets its own half with a Marigold edge between.")]) + '</div>'),
]

# ================================================================ merch + events
def _mt(svg, cap, tone): return f'<figure style="margin:0"><div class="tint" style="background:{tone};height:400px;display:flex;align-items:center;justify-content:center">{img(svg, "width:84%", alt=cap)}</div><p class="fgc"><b>{cap}</b></p></figure>'
PG_MERCH = [
 page(head("00", "Tee and tote", "Merch is the mark at rest: one placement, one print colour where fabric allows, the full-colour parcel only on white or natural cloth.") +
      '<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:18px">' + _mt(MERCH_A["tee_ink"], "Ink tee, chest lockup", I[100]) + _mt(MERCH_A["tee_paper"], "White tee, full colour", I[100]) + _mt(MERCH_A["tee_cobalt"], "Cobalt tee, white mark", I[100])
      + _mt(MERCH_A["tote_nat"], "Natural tote", I[100]) + _mt(MERCH_A["tote_ink"], "Ink tote, white mark", I[100]) + '</div>'
      + rules_inl([("Placement", "Left chest at about 9 cm wide, or centred chest at about 22 cm. Totes carry the mark centred, lower than the handles."),
                   ("One colour on dark fabric", "White on Ink and Cobalt. The full-colour parcel is for white and natural only, where the blue face stays visible."),
                   ("Screen print, flat", "Solid inks, no gradients, no distressing. The tape stays a notch in the one-colour mark.")], 3, 26)),
 page(head("00", "Booth", "One simple layout for an event: a backdrop with the line, a counter with the lockup, and two roll-ups at the sides.") +
      f'<div class="sheet2" style="grid-template-columns:1000px 1fr;gap:44px"><div>{svgf(EVENT, 1000, alt="Booth layout")}<p class="fgc"><b>Booth elevation.</b> Backdrop 3.0 × 2.4 m, counter 1.8 m, two roll-ups of 0.85 × 2.0 m.</p></div>'
      + rules([("Backdrop", "Ink with the parcel pattern at low opacity. The line is in the upper half, so it clears heads; the tape band sits above counter height."),
               ("Counter", "Cobalt, with the white lockup. The call to action is “Join a drop”, in sentence case."),
               ("Roll-ups", "Marigold with one illustration and two words. One idea each: the backdrop makes the promise, they make it small.")]) + '</div>'),
]

# ================================================================ photography do/don't and illustration mix
def phf(name, st="", crop=None, extra="", maxw=700): return f'<img style="{st}" src="{photo_uri(name, maxw, crop=crop)}" alt="Product photo"/>{extra}'
PG_PHOTO2 = [
 page(head("00", "Photography, do and don’t", "A photograph is the proof, so edit it as little as the label allows. These six cover most of what goes wrong.") +
      '<div class="tile6">'
      + tile("", phf("p1.jpg", "object-position:50% 70%"), 0, "Centre the product, leave air", "One product, a tenth of margin, soft daylight.")
      + tile("", phf("p6.jpg", "object-position:50% 40%"), 0, "Real surface, real light", "Stone, linen, sand or wood. Nothing staged to look like a studio.")
      + tile("", phf("p7.jpg", "object-position:50% 60%"), 0, "Crop to the product", "Frame the product, not the room around it.")
      + tile("", phf("p6.jpg", "object-position:50% 40%;filter:saturate(2.4) contrast(1.35) hue-rotate(-30deg)"), 0, "Don’t grade or recolour", "Heavy filters change what the product looks like. Exposure and white balance only.", False)
      + tile("", phf("p3.jpg", "object-position:50% 0%;transform:scale(1.9) translate(-18%,-26%)"), 0, "Don’t crop the product away", "If the product is cut off at the edge, choose another picture.", False)
      + tile("", f'<div style="position:absolute;inset:0;background:{SCALES["cobalt"][100]};display:flex;align-items:center;justify-content:center"><div style="width:62%;aspect-ratio:1;border-radius:28px;background:#fff;box-shadow:0 20px 40px rgba(16,20,38,.25);overflow:hidden"><img style="width:100%;height:100%;object-fit:cover" src="{photo_uri("p1.jpg", 400, crop=(0.1, 0.25, 0.9, 0.85))}" alt=""/></div></div>', 0, "Don’t put it on a plate", "No tile, ring, glow or shadow card behind a product photo. It sits bare.", False) + '</div>'),
 page(head("00", "Photography and illustration", "Pictures prove, illustration explains. Use one of each per layout at most, side by side and never on top of one another.") +
      '<div class="tile6">'
      + tile("", f'<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr"><img style="width:100%;height:100%;object-fit:cover" src="{photo_uri("p5.jpg", 500)}" alt=""/><div style="background:{MAR};display:flex;align-items:center;justify-content:center">{ill_img("parcel", "light", "width:190px")}</div></div>', 0, "Side by side", "Photo on one half, the parcel on flat colour on the other.")
      + tile("", f'<div style="position:absolute;inset:0"><img style="width:100%;height:100%;object-fit:cover" src="{photo_uri("p7.jpg", 700)}" alt=""/><div style="position:absolute;right:14px;bottom:-14px">{ill_img("payout", "light", "width:110px")}</div></div>', 0, "Breaks an edge, clears the product", "One illustration on a corner of the frame, away from the product.")
      + tile("", f'<div style="position:absolute;inset:0;background:#fff;display:flex;align-items:center;justify-content:center;gap:16px"><div style="font:650 24px var(--hd-font-display);color:{INK};max-width:150px">No drops near you yet</div>{ill_img("search", "light", "width:120px")}</div>', 0, "Illustration alone for empty states", "When there is no photograph to show, the illustration carries the screen.")
      + tile("", f'<div style="position:absolute;inset:0"><img style="width:100%;height:100%;object-fit:cover" src="{photo_uri("p1.jpg", 500)}" alt=""/><div style="position:absolute;left:38%;top:30%">{ill_img("gift", "light", "width:130px")}</div></div>', 0, "Don’t cover the product", "An illustration over the product hides the very thing the photo proves.", False)
      + tile("", f'<div style="position:absolute;inset:0"><img style="width:100%;height:100%;object-fit:cover" src="{photo_uri("p4.jpg", 600)}" alt=""/>' + "".join(f'<div style="position:absolute;left:{x}%;top:{y}%">{ill_img(n, "light", "width:80px")}</div>' for n, x, y in (("gift", 8, 8), ("star" if False else "review", 60, 12), ("bell", 30, 55), ("bag", 70, 58))) + '</div>', 0, "Don’t scatter several", "A scene of floating objects over a photograph is clutter.", False)
      + tile("", f'<div style="position:absolute;inset:0;display:flex;gap:10px;align-items:center;justify-content:center;background:{I[50]}"><div style="width:120px;height:160px;border-radius:14px;overflow:hidden"><img style="width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.3)" src="{photo_uri("p5.jpg", 300)}" alt=""/></div>{ill_img("parcel", "light", "width:110px;filter:hue-rotate(160deg) saturate(.6)")}</div>', 0, "Don’t restyle either one", "Never desaturate the photo or recolour the illustration to make them match.", False) + '</div>'),
]

# ================================================================ pattern and tape (moved from Product) and print
def _pat(pat, bg): return f'<div style="height:250px;border-radius:20px;background-image:url({uri(pat)});background-size:180px;{bg}"></div>'
PG_PATTERN = [
 page(head("00", "Pattern and tape", "The parcel pattern fills backgrounds; the tape band is the same lockup in a strip. Both are built from the logo and nothing else.") +
      '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px">' + _pat(PAT_INK, "") + _pat(PAT_COB, "") + _pat(PAT_PAPER, f"box-shadow:inset 0 0 0 1px {I[200]};") + '</div>'
      f'<div style="display:grid;gap:10px;margin-top:22px">{svgf(TAPE_COB, 1424, "mini2", "Cobalt tape")}{svgf(TAPE_VER, 1424, "mini2", "Vermilion tape")}</div>'
      + rules_inl([("Pattern at low contrast", "Tone on tone: Ink 800 on Ink, Cobalt 500 on Cobalt, Ink 100 on Paper. It sits behind content and never competes with it."),
                   ("Tape in whole units", "The lockup repeats in whole units so a roll tiles with no cut-off wordmark. Cobalt seals, Vermilion marks a return, Marigold is for extras."),
                   ("Never both at full strength", "A pattern and a tape band on one layout: the pattern drops to its lowest opacity.")], 3, 22)),
]
PG_PRINT = [
 page(head("00", "Print", "A business card, a shipping label and tape. Print uses the same files as screen: nothing is redrawn for paper.") +
      f'<div class="sheet2" style="grid-template-columns:430px 360px 1fr;gap:44px"><div style="display:grid;gap:18px">{svgf(APPS["card_f"], 430, alt="Business card front")}{svgf(APPS["card_b"], 430, alt="Business card back")}<p class="fgc"><b>Business card, 85 × 55 mm.</b> Ink front with the parcel pattern; Paper back with the brand stripe.</p></div>'
      f'<div>{svgf(APPS["label"], 330, alt="Shipping label")}<p class="fgc"><b>Shipping label, 4 × 6 in.</b> A small lockup, an ink tag, hairline rules and a barcode.</p></div>'
      + rules([("Uncoated stock", "Cards print on uncoated 350 gsm. The Cobalt, Marigold and Vermilion stripe is the only spot colour."), ("Label in sentence case", "Field names read “Ship to”, “From”, “Tracking”. Codes only are set in Geist Mono."), ("Tape is 48 mm", "One Cobalt strip per box, with the lockup repeated in whole units.")]) + '</div>'),
]
