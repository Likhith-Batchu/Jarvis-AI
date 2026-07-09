class Runtime:

    def __init__(self):

        self.mode = "voice"

        self.state = "standby"

        self.wake_word = "atlas"

    # ------------------------

    def set_mode(self, mode):

        self.mode = mode

    def get_mode(self):

        return self.mode

    # ------------------------

    def set_state(self, state):

        self.state = state

    def get_state(self):

        return self.state

    # ------------------------

    def is_awake(self):

        return self.state == "conversation"

    def wake(self):

        self.state = "conversation"

    def sleep(self):

        self.state = "standby"