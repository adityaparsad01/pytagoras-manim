# Rendering

## Local rendering

The project uses ManimGL with a virtual X display.

The renderer is configured for 1920×1080 output.

The main script is:

`./render.sh`

The script:

1. Checks ManimGL.
2. Starts Xvfb.
3. Renders the ManimGL scene.
4. Combines the rendered video and narration.
5. Produces `dist/pythagorean_theorem_v2.mp4`.

## Dependencies

Ubuntu packages:

- libpango1.0-dev
- ffmpeg
- xvfb

Python dependency:

- ManimGL
- setuptools < 81
