class RuntimeCommands:

    EXIT = {

        "sleep",

        "go to sleep",

        "standby",

        "that's all",

        "goodbye",

        "bye"

    }

    @staticmethod
    def should_sleep(text):

        return text.lower().strip() in RuntimeCommands.EXIT