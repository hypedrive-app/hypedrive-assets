#!/bin/bash
# usage: sh_shot.sh outdir
U=~/Downloads/hypedrive-wordmark/BRAND/ui; Z=~/.local/share/zen/zen; P=/tmp/hdwm/zt/prof8; O=$1
shot() { timeout 120 $Z --headless --no-remote --profile $P --screenshot "$1" --window-size="$2" "file://$3" >/dev/null 2>&1; }
shot $O/kit.png 1600,9000 $U/hypedrive-ui-kit.html
shot $O/kitd.png 1600,9000 $U/hypedrive-ui-kit-dark.html
shot $O/mob.png 1860,3160 $U/hypedrive-screens-mobile.html
for n in 1 2 3 4; do shot $O/d$n.png 1520,1000 $U/hypedrive-desktop-$n.html; done
