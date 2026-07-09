class ConversationMemory:

    def __init__(self):
        self.messages = []

    def add(self, role, content):

        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )

        # Keep only the last 20 messages
        if len(self.messages) > 20:
            self.messages.pop(0)

    def get(self):
        return self.messages