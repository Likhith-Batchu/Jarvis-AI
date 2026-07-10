from core.tool_registry import TOOLS
from skills.manager import SkillManager


class Executor:

    def __init__(self):

        self.skill_manager = SkillManager()

    def execute(self, plan):

        action = plan["action"]

        # Handle AI Skills
        if action == "skill":

            result = self.skill_manager.execute(
                plan["skill"]
            )

            return True, result

        # Handle Tools
        tool = TOOLS.get(action)

        if tool is None:
            return False, f"Unknown action: {action}"

        kwargs = {}

        for arg in tool.arguments:
            kwargs[arg] = plan[arg]

       
    
        print("========== EXECUTOR ==========")
        print("Action:", action)
        print("Tool:", tool.function.__name__)
        print("Kwargs:", kwargs)

        result = tool.function(**kwargs)

        print("Result:", result)
        print("==============================")

        return result