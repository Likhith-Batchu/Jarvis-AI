import json

from ollama import chat


class AIPlanner:

    def __init__(self):

        self.model = "qwen2.5:7b"

        self.system_prompt = """
You are an AI planner.

Convert the user's request into ONE JSON object.

Return ONLY valid JSON.

Supported actions:

1. open_application

{
"action":"open_application",
"app":"chrome"
}

2. open_website

{
"action":"open_website",
"website":"github"
}

3. google_search

{
"action":"google_search",
"query":"python decorators"
}

4. leetcode

{
"action":"leetcode",
"topic":"arrays"
}

5. workspace

{
"action":"workspace",
"workspace":"dsa"
}

6. chat

{
"action":"chat"
}

Return JSON only.
"""

    def plan(self, message):

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

        text = response["message"]["content"]
        

        print("\n========== AI Planner Output ==========")
        print(text)
        print("=======================================\n")

        return json.loads(text)
        