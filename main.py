from core.jarvis import Jarvis
from voice.listener import listen
from voice.speaker import speak

jarvis = Jarvis()

print("=" * 60)
print("               JARVIS OS")
print("=" * 60)

while True:

    mode = input("\n(T)ype or (V)oice? : ").lower()

    if mode == "v":
        user = listen()
    else:
        user = input("You : ")

    if user.lower() == "exit":
        break

    reply = jarvis.process(user)

    print(f"\nJarvis : {reply}")

    speak(reply)