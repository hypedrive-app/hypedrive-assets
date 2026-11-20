import os, re, json, sys
D = "/home/shivam-gupta/Documents/hypedrive/packages/icons/node_modules/nucleo-ui-fill-18/dist/components"
EL = re.compile(r'React\.createElement\("(\w+)",\s*\{([^{}]*)\}')
AT = re.compile(r'(\w+):\s*"([^"]*)"')
def kebab(k): return re.sub(r'([A-Z])', lambda m: '-' + m.group(1).lower(), k)
out = {}
for f in os.listdir(D):
    if not f.startswith("Icon") or not f.endswith(".js") or f == "Icon.js": continue
    t = open(os.path.join(D, f)).read()
    parts = []
    for tag, attrs in EL.findall(t):
        a = " ".join(f'{kebab(k)}="{v}"' for k, v in AT.findall(attrs))
        parts.append(f"<{tag} {a}/>")
    if parts: out[f[4:-3]] = "".join(parts)
json.dump(out, open("/tmp/hdwm/nucleo_fill.json", "w"))
print(len(out))
