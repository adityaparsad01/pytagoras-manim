# GitHub Actions

The repository automatically renders the video on pushes affecting the rendering project.

Workflow:

`.github/workflows/render.yml`

## Pipeline

1. Checkout repository.
2. Install Python 3.12.
3. Install Pango, FFmpeg and Xvfb.
4. Install ManimGL.
5. Run `render.sh`.
6. Upload the final MP4 as a GitHub Actions artifact.

The workflow uses a concurrency group so a newer render supersedes an older render.

## Manual render

Open **Actions → Render video → Run workflow** in GitHub.
