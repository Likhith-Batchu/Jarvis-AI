from ollama import chat


class Brain:
    def __init__(self, model="qwen2.5:7b"):
        self.model = model

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

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response["message"]["content"]