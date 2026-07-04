import subprocess
import tempfile
import os
import pygame
import time


PIPER = "piper/piper.exe"
VOICE = "piper/models/en_US-lessac-medium.onnx"

# Initialize pygame only once
pygame.mixer.init()


def speak(text):

    # Create temporary wav file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        output = f.name

    # Generate speech with Piper
    process = subprocess.run(
        [
            PIPER,
            "-m",
            VOICE,
            "-f",
            output
        ],
        input=text,
        text=True,
        capture_output=True
    )

    # Print Piper errors if any
    if process.stderr:
        print(process.stderr)

    # Play the generated audio
    pygame.mixer.music.load(output)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    # Stop and delete the temporary file
    pygame.mixer.music.unload()
    os.remove(output)