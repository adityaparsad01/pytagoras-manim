#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist audio
if [ ! -x ".venv/bin/manimgl" ]; then
  python3 -m venv .venv
  .venv/bin/python -m pip install --upgrade pip
  .venv/bin/pip install 'setuptools<81' manimgl
fi
test -f audio/narration.mp3
timeout 600 xvfb-run -a -s '-screen 0 1280x720x24' env LIBGL_ALWAYS_SOFTWARE=1 .venv/bin/manimgl -w -l pythagorean.py PythagoreanTheorem
VIDEO="$(find videos -type f -name '*.mp4' ! -name '*_temp.mp4' | sort | tail -1)"
test -n "$VIDEO"
ffmpeg -y -i "$VIDEO" -i audio/narration.mp3 -filter_complex "[1:a]apad[a]" -map 0:v:0 -map "[a]" -c:v copy -c:a aac -b:a 128k -shortest dist/pythagorean_theorem.mp4
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 dist/pythagorean_theorem.mp4
