#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist videos
test -f audio/final_audio.mp3
if [ ! -x ".venv/bin/manimgl" ]; then
  python3 -m venv .venv
  .venv/bin/python -m pip install --upgrade pip
  .venv/bin/pip install 'setuptools<81' manimgl
fi
rm -f videos/PythagoreanTheoremV2.mp4 videos/PythagoreanTheoremV2_temp.mp4 dist/pythagorean_theorem_v2.mp4
timeout 900 xvfb-run -a -s '-screen 0 1920x1080x24' env LIBGL_ALWAYS_SOFTWARE=1 .venv/bin/manimgl -w --hd pythagorean_v2.py PythagoreanTheoremV2
VIDEO="$(find videos -type f -name 'PythagoreanTheoremV2.mp4' | head -1)"
test -f "$VIDEO"
ffmpeg -y -i "$VIDEO" -i audio/final_audio.mp3 -filter_complex "[1:a]apad[a]" -map 0:v:0 -map "[a]" -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 160k -shortest dist/pythagorean_theorem_v2.mp4
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 dist/pythagorean_theorem_v2.mp4
