from voice.microphone import record_audio
from voice.transcriber import transcribe


def listen():

    audio = record_audio()

    text = transcribe(audio)

    print(f"\n🎤 You: {text}")

    return text