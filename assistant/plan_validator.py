from core.capability_manager import CapabilityManager


class PlanValidator:

    def __init__(self):

        self.capabilities = CapabilityManager()

    def validate(self, plan):

        valid_steps = []

        for step in plan.get("steps", []):

            action = step.get("action")

            if action == "skill":

                if self.capabilities.has_skill(step["skill"]):
                    valid_steps.append(step)

            elif self.capabilities.has_tool(action):

                valid_steps.append(step)

        plan["steps"] = valid_steps

        return plan