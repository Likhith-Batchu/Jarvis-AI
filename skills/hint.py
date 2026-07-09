from skills.base import BaseSkill


class HintSkill(BaseSkill):

    def run(self):

        prompt = """
Look at the programming problem on the screen.

DO NOT solve it.

Only provide:

- One hint.
- One observation.
- One direction.

Never reveal the complete solution.
"""

        return self.analyze(prompt)