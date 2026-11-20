#!/bin/bash
# usage: xa_shot.sh <nth section 1-based> <theme light|dark> <out> [w] [h]
U=~/Downloads/hypedrive-wordmark/BRAND/ui
f=hypedrive-ui-kit; [ "$2" = dark ] && f=hypedrive-ui-kit-dark
T=$U/_xa_tmp_$2_$1.html
python3 - "$U/$f.html" "$T" "$1" <<'PY'
import sys
s=open(sys.argv[1]).read(); n=sys.argv[3]
css=f"<style>.sec{{display:none!important}} .sheet-w>.sec:nth-of-type({n}){{display:block!important}} .hero{{display:none!important}} .sheet-w{{padding-top:20px!important}}</style></head>"
open(sys.argv[2],'w').write(s.replace("</head>",css,1))
PY
mkdir -p /tmp/hdwm/zt/pa2
timeout 90 ~/.local/share/zen/zen --headless --no-remote --profile /tmp/hdwm/zt/pa2 --screenshot "$3" --window-size=${4:-1600},${5:-1500} "file://$T" >/dev/null 2>&1
rm -f $T
