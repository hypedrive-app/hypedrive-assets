import sys, subprocess; sys.path.insert(0, "/tmp/hdwm")
from text2path import text_path
rows = []; y = 10
for name, w in [("Rubik",700),("Jakarta",800),("Manrope",800),("Outfit",700),("Figtree",800),("Onest",700),("Bricolage",700),("Urbanist",800),("Lexend",700),("Fredoka",600)]:
    for soft in (0, 1):
        d, tw = text_path("Hypedrive", w - (60 if soft else 0), 18.9, -0.015, name)
        st = ' stroke="#151515" stroke-width="1.1" stroke-linejoin="round"' if soft else ""
        rows.append(f'<text x="4" y="{y+16}" font-family="sans-serif" font-size="5" fill="#999">{name} {"soft" if soft else ""}</text>'
                    f'<path transform="translate({40+soft*150} {y+22.9})" fill="#151515"{st} d="{d}"/>')
    y += 34
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 {y+6}" width="1700" height="{(y+6)*5}"><rect width="100%" height="100%" fill="#fff"/>{"".join(rows)}</svg>'
open("/tmp/hdwm/fonts.svg","w").write(svg)
subprocess.run(["rsvg-convert","/tmp/hdwm/fonts.svg","-o","/tmp/hdwm/fonts.png"],check=True)
