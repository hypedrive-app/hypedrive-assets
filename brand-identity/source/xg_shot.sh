#!/bin/bash
# usage: xg_shot.sh tag   -> out_xg/<tag>-<theme>-nwN.png
U=~/Downloads/hypedrive-wordmark/BRAND/ui; Z=~/.local/share/zen/zen
for th in light dark; do
  src=$U/hypedrive-ui-kit.html; [ $th = dark ] && src=$U/hypedrive-ui-kit-dark.html
  for n in 1 2 3 4 5 6 7 8 9; do
    t=$U/_xgtmp_${th}_$n.html
    sed "s#</head>#<style>.sec{display:none!important} .sec.nw$n{display:block!important} .hero,header,nav.toc{display:none!important}</style></head>#" $src > $t
    timeout 90 $Z --headless --no-remote --profile /tmp/hdwm/zt/pg --screenshot /tmp/hdwm/out_xg/$1-$th-nw$n.png --window-size=1600,2700 file://$t >/dev/null 2>&1
    rm -f $t
  done
done
