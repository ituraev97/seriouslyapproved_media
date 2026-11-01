#!/usr/bin/env bash
# usage: encode.sh <episode_dir> <out.mp4> [max_MB=95]
# frames/ + mix.wav -> loudnorm -14 LUFS -> H.264 30 fps; re-encodes at a computed bitrate if over the GitHub limit.
set -euo pipefail
EP="$1"; OUT="$2"; MAXMB="${3:-95}"; cd "$EP"
ffmpeg -nostdin -v error -y -i mix.wav -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 mixn.wav
ffmpeg -nostdin -v error -y -framerate 30 -i frames/f%05d.jpg -i mixn.wav -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -shortest -movflags +faststart "$OUT"
SZ=$(stat -c%s "$OUT")
if [ "$SZ" -gt $((MAXMB*1024*1024)) ]; then
  D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT")
  VBR=$(python3 -c "print(int(($MAXMB*8*1024*0.95)/$D - 192))")
  ffmpeg -nostdin -v error -y -framerate 30 -i frames/f%05d.jpg -i mixn.wav -c:v libx264 -preset veryfast -b:v ${VBR}k -maxrate ${VBR}k -bufsize $((VBR*2))k \
    -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart "$OUT"
fi
ffmpeg -nostdin -i "$OUT" -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1
ls -la "$OUT"
