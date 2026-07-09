from core.tool_registry import TOOLS
from skills.manager import SkillManager


class CapabilityManager:

    def __init__(self):

        self.skill_manager = SkillManager()

    def available_tools(self):

        return list(TOOLS.keys())

    def available_skills(self):

        return list(self.skill_manager.skills.keys())

    def has_tool(self, tool):

        return tool in TOOLS

    def has_skill(self, skill):

        return skill in self.skill_manager.skills