from skills.base import BaseSkill
from utils.code_parser import extract_code

from tools.clipboard import copy

class DeveloperSkill(BaseSkill):

    def run(self):

        prompt = """
You are an expert software engineer.

Look carefully at the screen.

Return your answer in EXACTLY this format.

EXPLANATION

<Explain the problem.>

-------------------------

CORRECTED_CODE

```language
Corrected code here
"""
        result = self.analyze(prompt)
        code = extract_code(result)

        if code:
            copy(code)
        return result