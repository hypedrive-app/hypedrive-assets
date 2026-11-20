#!/bin/bash
# usage: sx.sh light|dark N OUT [H]
U=~/Downloads/hypedrive-wordmark/BRAND/ui
f=$U/hypedrive-ui-kit$([ "$1" = dark ] && echo -dark).html
t=$U/_tmp_pq2_$1_$2.html
if [ "$2" -le 11 ]; then sel=".sec:nth-of-type($2)"; else sel=".sec.nw$(($2-11))"; fi
sed "s#</head>#<style>.sec{display:none!important} $sel{display:block!important} .hero{display:none!important}</style></head>#" $f > $t
timeout 90 ~/.local/share/zen/zen --headless --no-remote --profile /tmp/pq2 --screenshot $3 --window-size=1600,${4:-2400} file://$t >/dev/null 2>&1
rm -f $t
