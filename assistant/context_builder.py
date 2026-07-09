from assistant.memory import Memory


class ContextBuilder:

    def __init__(self):

        self.memory = Memory()

    def build(self, user_message):

        context = ""

        favourite = self.memory.recall("favorite_language")

        if favourite:

            context += f"""
Known Information:

Favorite Programming Language:
{favourite}

"""

        return context