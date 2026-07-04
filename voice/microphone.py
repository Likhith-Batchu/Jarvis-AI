import sounddevice as sd
import soundfile as sf

def record_audio(filename="voice/input.wav", duration=5):

    print("\n🎤 Listening...\n")

    samplerate = 16000

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    sf.write(filename, audio, samplerate)

    print("✅ Recording finished.")

    return filename