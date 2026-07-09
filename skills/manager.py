from skills.leetcode import LeetCodeSkill
from skills.debug import DebugSkill
from skills.workspace import WorkspaceSkill
from skills.developer import DeveloperSkill 
from skills.review import ReviewSkill
from skills.hint import HintSkill
from assistant.session import Session


class SkillManager:

    def __init__(self):

        self.skills = {

            "leetcode": LeetCodeSkill(),

            "debug": DebugSkill(),

            "workspace_dsa": WorkspaceSkill(),

            "developer": DeveloperSkill(),

            "review": ReviewSkill(),

            "hint": HintSkill(),

        }

    def execute(self, name):

        skill = self.skills.get(name)

        if skill:

            result = skill.run()

            Session.set_skill(name)

            Session.remember_result(result)

            return result

        return "Unknown skill."