#!/bin/bash
# Render every UI deliverable in Zen (the owner's engine). Per-screen pages are moved into screens/ first,
# because they use <base href="../"> to reach assets/stock.
U=~/Downloads/hypedrive-wordmark/BRAND/ui; Z=~/.local/share/zen/zen; P=/tmp/hdwm/zt/prof
shot() { timeout 90 $Z --headless --no-remote --profile $P --screenshot "$1" --window-size="$2" "file://$3" >/dev/null 2>&1; }
shot $U/hypedrive-ui-kit.png 1600,21000 $U/hypedrive-ui-kit.html
shot $U/hypedrive-ui-kit-dark.png 1600,21000 $U/hypedrive-ui-kit-dark.html
shot $U/hypedrive-screens-mobile.png 1860,3160 $U/hypedrive-screens-mobile.html
for n in 1 2 3 4; do shot $U/hypedrive-desktop-$n.png 1520,1000 $U/hypedrive-desktop-$n.html; done
names=(welcome verify-phone home drop-details apply-sheet parcel-tracking submit-review wallet success notifications profile-dark empty-search)
mkdir -p $U/screens
for n in $(seq 1 12); do
  f=$(printf "_m%02d.html" $n); d=$U/screens/$(printf "%02d" $n)-${names[$((n-1))]}
  mv $U/$f $d.html && shot $d.png 450,920 $d.html
done
echo rendered
