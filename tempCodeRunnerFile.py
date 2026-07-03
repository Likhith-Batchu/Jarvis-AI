# from assistant.brain import Brain


# def main():
#     print("=" * 50)
#     print("         JARVIS AI")
#     print("=" * 50)
#     print("Type 'exit' to quit.\n")

#     brain = Brain()

#     while True:
#         user = input("You: ")

#         if user.lower() == "exit":
#             print("Jarvis: Goodbye!")
#             break

#         reply = brain.ask(user)

#         print(f"\nJarvis: {reply}\n")


# if __name__ == "__main__":
#     main()
from tools.app_launcher import open_application

while True:

    command = input(">>> ")

    if command == "exit":
        break

    success, message = open_application(command)

    print(message)