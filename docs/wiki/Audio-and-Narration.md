# Audio and Narration

The final version uses neural text-to-speech rather than the earlier robotic system voice.

## Pipeline

1. Write the narration in `narration.txt`.
2. Generate speech with an English neural voice.
3. Normalize the narration timing.
4. Add a very subtle background tone.
5. Mux the final audio with the rendered MP4 using FFmpeg.

The final audio is stored as:

`audio/final_audio.mp3`

The narration is intentionally concise so that the visuals carry most of the mathematical explanation.
