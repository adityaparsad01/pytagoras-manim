#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist audio
if [ ! -x ".venv/bin/manimgl" ]; then
  python3 -m venv .venv
  .venv/bin/python -m pip install --upgrade pip
  .venv/bin/pip install git+https://github.com/3b1b/manim.git
fi
espeak-ng -s 155 -p 45 -v en-us -f narration.txt -w audio/narration.wav
xvfb-run -a .venv/bin/manimgl -w -m pythagorean.py PythagoreanTheorem
VIDEO="$(find media -type f -name '*.mp4' | sort | tail -1)"
test -n "$VIDEO"
ffmpeg -y -i "$VIDEO" -i audio/narration.wav -filter_complex "[1:a]apad[a]" -map 0:v:0 -map "[a]" -c:v copy -c:a aac -b:a 128k -shortest dist/pythagorean_theorem.mp4
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 dist/pythagorean_theorem.mp4
