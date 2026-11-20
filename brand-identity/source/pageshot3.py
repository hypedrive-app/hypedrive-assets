import subprocess, sys, os, re
H=os.path.expanduser("~/Downloads/hypedrive-wordmark/BRAND/Hypedrive-Brand-Guidelines.html")
Z=os.path.expanduser("~/.local/share/zen/zen"); os.makedirs("/tmp/hdwm/pg3",exist_ok=True)
html=open(H).read()
for k in map(int,sys.argv[1:]):
    tmp=f"/tmp/hdwm/pg3/_p{k}.html"
    open(tmp,"w").write(html.replace("</head>",f"<style>.page{{display:none!important}} .page:nth-of-type({k}){{display:block!important;margin:0!important}} body{{background:#fff!important}}</style></head>",1))
    subprocess.run(["timeout","90",Z,"--headless","--no-remote","--profile","/tmp/hdwm/zt/prof3","--screenshot",f"/tmp/hdwm/pg3/p{k}.png","--window-size=1600,900","file://"+tmp],capture_output=True)
    os.remove(tmp)
