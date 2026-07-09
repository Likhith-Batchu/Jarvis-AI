from ollama import chat
import json


class MemoryExtractor:

    def __init__(self):

        self.model = "qwen2.5:7b"

        self.prompt = """
You are a memory extraction AI.

Your task is to determine whether the user has shared
a long-term personal fact that should be remembered.

Examples:

User:
My favorite programming language is Python.

Return:

{
"remember":true,
"key":"favorite_language",
"value":"Python"
}

-----------------------

User:
I use VS Code.

Return

{
"remember":true,
"key":"favorite_ide",
"value":"VS Code"
}

-----------------------

User:
Open Chrome.

Return

{
"remember":false
}

-----------------------

Return ONLY JSON.
"""

    def extract(self, text):

        response = chat(

            model=self.model,

            messages=[
                {
                    "role": "system",
                    "content": self.prompt
                },
                {
                    "role": "user",
                    "content": text
                }
            ]

        )

        return json.loads(
            response["message"]["content"]
        )