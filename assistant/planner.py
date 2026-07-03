class Planner:

    def plan(self, message: str):

        message = message.lower()

        if "open" in message:

            apps = [
                "chrome",
                "calculator",
                "notepad",
                "paint",
                "cmd",
                "explorer",
                "vscode"
            ]

            for app in apps:
                if app in message:
                    return {
                        "tool": "open_application",
                        "args": {
                            "app": app
                        }
                    }

        return {
            "tool": None,
            "args": {}
        }