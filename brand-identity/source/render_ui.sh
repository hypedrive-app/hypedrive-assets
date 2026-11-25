#!/bin/bash
# Render every UI deliverable in Zen (the owner's engine). Per-screen pages are moved into screens/ first,
# because they use <base href="../"> to reach assets/stock.
U=~/Downloads/hypedrive-wordmark/BRAND/ui; Z=~/.local/share/zen/zen; P=/tmp/hdwm/zt/prof
shot() { timeout 90 $Z --headless --no-remote --profile $P --screenshot "$1" --window-size="$2" "file://$3" >/dev/null 2>&1; }
shot $U/hypedrive-ui-kit.png 1600,34000 $U/hypedrive-ui-kit.html
shot $U/hypedrive-ui-kit-dark.png 1600,34000 $U/hypedrive-ui-kit-dark.html
shot $U/hypedrive-screens-mobile.png 1860,3900 $U/hypedrive-screens-mobile.html
for n in $(seq 1 7); do shot $U/hypedrive-desktop-$n.png 1520,2300 $U/hypedrive-desktop-$n.html; /tmp/hdwm/venv/bin/python -I /tmp/hdwm/trim_bottom.py $U/hypedrive-desktop-$n.png; done
names=(welcome verify-phone home campaign join-buy join-receipt enrollment-in-review submit-review wallet success notifications settings-dark empty-search onboarding campaigns enrollments enrollment-detail withdraw settings barter m-today m-deals m-store m-enroll m-enrollments m-wallet m-trustdrive)
mkdir -p $U/screens
for n in $(seq 1 ${#names[@]}); do
  f=$(printf "_m%02d.html" $n); d=$U/screens/$(printf "%02d" $n)-${names[$((n-1))]}
  mv $U/$f $d.html && shot $d.png 450,920 $d.html
done
echo rendered
