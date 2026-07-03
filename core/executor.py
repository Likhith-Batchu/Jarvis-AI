from tools.registry import TOOLS


class Executor:

    def execute(self, plan):

        tool = plan["tool"]

        if tool is None:
            return None

        if tool not in TOOLS:
            return "Tool not found."

        args = plan["args"]

        return TOOLS[tool](args["app"])[1]