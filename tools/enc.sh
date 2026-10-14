#!/bin/bash
# enc.sh <in> <name> <v|h> [ss] [t] [poster_ss]
in="$1"; name="$2"; mode="$3"; ss="${4:-0}"; t="${5:-}"; pss="${6:-1.5}"
OUT="C:/Users/Alfonso/Documents/claude code/acceler-portfolio/assets"
if [ "$mode" = "v" ]; then vf="scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2"; crf=25; else vf="scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2"; crf=${CRF:-23}; fi
targs=(); [ -n "$t" ] && targs=(-t "$t")
ffmpeg -v error -y -ss "$ss" -i "$in" "${targs[@]}" -vf "$vf,format=yuv420p" -r 30 -c:v libx264 -preset medium -crf $crf -profile:v high -level 4.0 -c:a aac -b:a 128k -ac 2 -movflags +faststart "$OUT/videos/$name.mp4" || { echo "FAIL $name"; exit 1; }
ffmpeg -v error -y -ss "$pss" -i "$OUT/videos/$name.mp4" -frames:v 1 -q:v 3 "$OUT/posters/$name.jpg"
echo "OK $name $(stat -c %s "$OUT/videos/$name.mp4") bytes"
