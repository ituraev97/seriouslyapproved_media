#!/usr/bin/env bash
# usage: build_short.sh <short_dir>  — render frames, mix, encode short.mp4 (expects tts.py + compose.py already run)
set -euo pipefail
P=$(cd "$(dirname "$0")" && pwd); S="$1"
rm -rf "$S/frames"; node "$P/render.mjs" "$S" 30 >/dev/null && python3 "$P/mix.py" "$S" >/dev/null && bash "$P/encode.sh" "$S" "$S/short.mp4" 95
