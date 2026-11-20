"""Hypedrive palette built in OKLCH so every face tone has matched lightness steps,
with a hue shift along the gradient (lights lean warm, darks lean deep) for a richer read."""
import math

def oklch_to_hex(L, C, h):
    def to_rgb(C):
        a, b = C*math.cos(math.radians(h)), C*math.sin(math.radians(h))
        l_ = L + 0.3963377774*a + 0.2158037573*b
        m_ = L - 0.1055613458*a - 0.0638541728*b
        s_ = L - 0.0894841775*a - 1.2914855480*b
        l, m, s = l_**3, m_**3, s_**3
        r = 4.0767416621*l - 3.3077115913*m + 0.2309699292*s
        g = -1.2684380046*l + 2.6097574011*m - 0.3413193965*s
        bb = -0.0041960863*l - 0.7034186147*m + 1.7076147010*s
        return r, g, bb
    lo, hi = 0.0, C
    rgb = to_rgb(C)
    if not all(-1e-4 <= v <= 1+1e-4 for v in rgb):        # gamut map: reduce chroma
        for _ in range(30):
            mid = (lo+hi)/2; rgb = to_rgb(mid)
            if all(-1e-4 <= v <= 1+1e-4 for v in rgb): lo = mid
            else: hi = mid
        rgb = to_rgb(lo)
    def enc(v):
        v = min(1, max(0, v))
        v = 12.92*v if v <= 0.0031308 else 1.055*v**(1/2.4) - 0.055
        return round(v*255)
    return "#" + "".join(f"{enc(v):02x}" for v in rgb)

def ramp(L0, L1, C0, C1, h0, h1): return (oklch_to_hex(L0, C0, h0), oklch_to_hex(L1, C1, h1))

# hue anchors: cobalt blue, vermilion orange, marigold yellow
BH, OH, YH = 262, 42, 84
BLUE = (ramp(.78, .72, .13, .16, 250, 256),  ramp(.62, .53, .21, .23, 258, 266), ramp(.47, .39, .21, .19, 266, 272))
ORNG = (ramp(.83, .77, .13, .16, 58, 50),    ramp(.69, .61, .20, .21, 44, 36),    ramp(.56, .48, .18, .17, 36, 30))
YELL = (ramp(.95, .90, .14, .17, 98, 92),    ramp(.86, .80, .17, .18, 84, 76),    ramp(.74, .67, .16, .16, 70, 62))
SIGNATURE = (YELL[0], BLUE[1], ORNG[1])
INK_L = (ramp(.36, .31, .008, .008, 270, 270), ramp(.25, .21, .008, .008, 270, 270), ramp(.17, .13, .006, .006, 270, 270))
INK_D = (ramp(1.0, .97, 0, .004, 270, 270), ramp(.92, .88, .006, .008, 270, 270), ramp(.80, .75, .008, .01, 270, 270))
INK_TEXT_L, INK_TEXT_D = oklch_to_hex(.19, .008, 270), "#ffffff"

if __name__ == "__main__":
    for n, v in [("BLUE", BLUE), ("ORNG", ORNG), ("YELL", YELL), ("INK_L", INK_L), ("INK_D", INK_D)]:
        print(n, v)
    print("text", INK_TEXT_L)
