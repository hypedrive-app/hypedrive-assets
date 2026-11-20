#!/bin/bash
# usage: sheet.sh <dir> <name...>  -> <dir>/_sheet-packages.png
set -e
OUT="$1"; shift
cd "$OUT"
for t in light dark; do
  bg=white; [ "$t" = dark ] && bg="#0f0f10"
  args=()
  for n in "$@"; do
    f=$(ls hypedrive-p*-"$n"-"$t".png); m=$(ls hypedrive-p*-"$n"-mark-"$t".png)
    args+=( \( \( "$m" -resize x150 -background "$bg" -gravity center -extent 320x190 \) \( "$f" -resize x115 -background "$bg" -gravity west -extent 880x190 \) +append \) )
  done
  magick "${args[@]}" -append -bordercolor "$bg" -border 30 /tmp/hdwm/pk-$t.png
done
magick /tmp/hdwm/pk-light.png /tmp/hdwm/pk-dark.png +append _sheet-packages.png
