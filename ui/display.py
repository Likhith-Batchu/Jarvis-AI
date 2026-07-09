class Display:

    @staticmethod
    def divider():

        print("=" * 60)

    @staticmethod
    def title(text):

        Display.divider()
        print(text.center(60))
        Display.divider()

    @staticmethod
    def status(state):

        print(f"\n⚡ Status : {state}")

    @staticmethod
    def user(text):

        print(f"\n👤 You : {text}")

    @staticmethod
    def jarvis(text):

        print(f"\n🤖 Jarvis : {text}")