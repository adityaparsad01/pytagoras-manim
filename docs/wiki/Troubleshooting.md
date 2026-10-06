# Troubleshooting

## ManimGL fails during installation

Use:

`setuptools<81`

ManimGL depends on packaging behavior that is not present in newer setuptools releases.

## Text containing ² causes rendering problems

For compatibility with the renderer, the scene source uses ASCII-style mathematical notation where required.

## OpenGL/X display errors

Run ManimGL through Xvfb and software rendering:

`xvfb-run -a -s '-screen 0 1920x1080x24' env LIBGL_ALWAYS_SOFTWARE=1 ...`

## Missing FFmpeg

Install FFmpeg on the rendering machine before running the pipeline.
