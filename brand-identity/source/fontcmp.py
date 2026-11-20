import sys, subprocess; sys.path.insert(0, "/tmp/hdwm")
import boxfinal as B
opts = [("Bricolage 800 · opsz 96", dict(font="Bricolage", wght=800, axes={"opsz":96,"wdth":100}, soft=0)),
        ("Bricolage 700 · opsz 96 · soft", dict(font="Bricolage", wght=700, axes={"opsz":96,"wdth":100}, soft=0.45)),
        ("Bricolage 700 · wdth 88 (narrow)", dict(font="Bricolage", wght=700, axes={"opsz":96,"wdth":88}, soft=0.45)),
        ("Bricolage 600 · opsz 96 · soft", dict(font="Bricolage", wght=600, axes={"opsz":96,"wdth":100}, soft=0.5)),
        ("Bricolage 700 · opsz 12 (text cut)", dict(font="Bricolage", wght=700, axes={"opsz":12,"wdth":100}, soft=0.45)),
        ("Plus Jakarta 760 · soft (previous)", dict(font="Jakarta", wght=760, axes={}, soft=0.55, track=-0.008))]
for i, (lab, kw) in enumerate(opts):
    for th in ("light", "dark"):
        open(f"/tmp/hdwm/fc{i}{th}.svg", "w").write(B.lockup(th, **kw))
        subprocess.run(["rsvg-convert", "-h", "130", f"/tmp/hdwm/fc{i}{th}.svg", "-o", f"/tmp/hdwm/fc{i}{th}.png"], check=True)
print("\n".join(l for l, _ in opts))
