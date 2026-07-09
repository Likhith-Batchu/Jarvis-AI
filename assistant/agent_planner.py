import json
from core.capability_manager import CapabilityManager

from ollama import chat


class AgentPlanner:

    def __init__(self):

        self.model = "qwen2.5:7b"
        self.capabilities = CapabilityManager()

        self.system_prompt = """
You are JARVIS Agent Planner.

Your job is to convert a USER GOAL
into a sequence of actions.

Return ONLY JSON.

Example

User:

Prepare for DSA interview.

Return

{
    "goal":"Prepare for DSA interview",

    "steps":[

        {
            "action":"skill",
            "skill":"workspace_dsa"
        },

        {
            "action":"skill",
            "skill":"leetcode"
        }

    ]
}

Return ONLY JSON.
"""

    def plan(self, goal):

        response = chat(

            model=self.model,

            messages=[

                {
                    "role":"system",
                    "content":self.system_prompt
                },

                {
                    "role":"user",
                    "content":goal
                }

            ]

        )

        return json.loads(
            response["message"]["content"]
        )