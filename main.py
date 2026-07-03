from core.jarvis import Jarvis

jarvis = Jarvis()

print("=" * 50)
print("JARVIS")
print("=" * 50)

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    reply = jarvis.process(user)

    print("\nJarvis:", reply, "\n")