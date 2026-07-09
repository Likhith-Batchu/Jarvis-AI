from ollama import chat

from assistant.conversation import ConversationMemory
from assistant.context_builder import ContextBuilder
from memory.manager import MemoryManager


class Brain:

    def __init__(self, model="qwen2.5:7b"):

        self.model = model

        # Short-term conversation memory
        self.memory = ConversationMemory()

        # Long-term context (SQLite)
        self.context = ContextBuilder()
        self.memory_manager = MemoryManager()
        self.system_prompt = """
You are JARVIS, an intelligent AI assistant inspired by Iron Man.

Rules:
- Never say you are Qwen.
- Always introduce yourself as JARVIS.
- Be polite.
- Speak naturally.
- Keep answers concise unless the user asks for details.
- The user's name is Likhith.
- Your purpose is to assist with coding, studies, productivity, and controlling the computer.
"""

    def ask(self, message: str):

        # Build long-term context
        context = self.context.build(message)

        # Save user message in conversation memory
        self.memory.add("user", message)
        self.memory_manager.process(message)

        # Build message list
        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            }
        ]

        # Add previous conversation
        messages.extend(self.memory.get())

        # Add current user message with context
        messages.append(
            {
                "role": "user",
                "content": f"""
Known Information:

{context}

Current User Message:

{message}
"""
            }
        )

        # Ask the AI
        response = chat(
            model=self.model,
            messages=messages
        )

        reply = response["message"]["content"]

        # Save assistant reply
        self.memory.add("assistant", reply)

        return reply