
from skills.base import BaseSkill


class LeetCodeSkill(BaseSkill):

    def run(self):

        return self.analyze(
            """
Explain this LeetCode problem.

Include:

Problem

Observation

Algorithm

Time Complexity

Space Complexity
"""
        )