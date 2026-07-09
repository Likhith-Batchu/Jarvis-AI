
from skills.base import BaseSkill

class DebugSkill(BaseSkill):

    def run(self):

        return self.analyze(
            """
Explain this programming error.

Suggest the fix.
"""
        )