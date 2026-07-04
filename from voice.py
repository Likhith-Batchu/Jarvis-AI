from voice.microphone import record_audio
from voice.transcriber import transcribe

audio = record_audio()

text = transcribe(audio)

print()

print("You said:")

print(text)