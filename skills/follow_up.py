from skills.base import BaseSkill


class FollowUpSkill(BaseSkill):

    def run(self, previous):

        prompt = f"""
Continue helping the user.

Previous answer:

{previous}

The user asked a follow-up question.

Continue naturally.

Do NOT restart from the beginning.
"""

        return self.analyze(prompt)