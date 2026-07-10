class UIController:

    def __init__(self, window):

        self.window = window

    # ------------------------

    def user_message(self, text):

        self.window.chat.add_user(text)

    # ------------------------

    def jarvis_message(self, text):

        self.window.chat.add_jarvis(text)

    # ------------------------

    def set_status(self, state):

        self.window.status.set_status(state)