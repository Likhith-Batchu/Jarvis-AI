from ollama import chat


class VisionAnalyzer:

    def __init__(self):

        self.model = "qwen2.5:7b"

        self.system_prompt = """
You are JARVIS.

You are looking at text extracted from the user's computer screen.

Your job is to understand what is happening.

If it is:

• Python code
→ Explain errors and suggest fixes.

• VS Code
→ Explain what the user is doing.

• Browser
→ Summarize the webpage.

• LeetCode
→ Explain the problem and suggest an approach.

• PDF / Notes
→ Summarize the content.

Be concise.

Speak naturally.
"""

    def analyze(self, screen_text):

        response = chat(

            model=self.model,

            messages=[

                {
                    "role": "system",
                    "content": self.system_prompt
                },

                {
                    "role": "user",
                    "content": screen_text
                }

            ]

        )

        return response["message"]["content"]