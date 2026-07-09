class InputMode:

    VOICE = "voice"

    TEXT = "text"

    @staticmethod
    def toggle(current):

        if current == InputMode.VOICE:
            return InputMode.TEXT

        return InputMode.VOICE