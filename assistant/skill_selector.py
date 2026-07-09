import json
from ollama import chat


class SkillSelector:

    def __init__(self):

        self.model = "qwen2.5:7b"

        self.prompt = """
You are JARVIS.

The user is coding.

Choose ONE skill.

Available skills:

developer
review
hint
leetcode
debug

Return ONLY JSON.

Example:

{
    "skill":"review"
}

Examples:

Review my code
→ review

Explain this error
→ debug

Give me a hint
→ hint

Help me solve this problem
→ leetcode

Fix my code
→ developer
"""

    def choose(self, message):

        response = chat(

            model=self.model,

            messages=[

                {
                    "role":"system",
                    "content":self.prompt
                },

                {
                    "role":"user",
                    "content":message
                }

            ]

        )

        return json.loads(
            response["message"]["content"]
        )