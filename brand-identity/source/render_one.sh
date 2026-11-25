#!/bin/bash
# Render one built mobile screen: render_one.sh <index 1-based> <profile-name> [out.png]
# Builds nothing; run `venv/bin/python -I kit_build.py` first. Copies _mNN.html into screens/ so asset paths resolve.
U=~/Downloads/hypedrive-wordmark/BRAND/ui; n=$(printf "%02d" $1); P=/tmp/hdwm/zt/$2; mkdir -p $P
cp $U/_m$n.html $U/screens/_one-$2-$n.html
out=${3:-/tmp/hdwm/zt/$2/m$n.png}
timeout 90 ~/.local/share/zen/zen --headless --no-remote --profile $P --screenshot "$out" --window-size=450,920 "file://$U/screens/_one-$2-$n.html" >/dev/null 2>&1
rm -f $U/screens/_one-$2-$n.html; echo "$out"
