from core.tool_registry import TOOLS


class Executor:

    def execute(self, plan):

        action = plan["action"]

        # -----------------------------
        # Open Application
        # -----------------------------

        if action == "open_application":

            return TOOLS["open_application"](
                plan["app"]
            )

        # -----------------------------
        # Open Website
        # -----------------------------

        elif action == "open_website":

            return TOOLS["open_website"](
                plan["website"]
            )

        # -----------------------------
        # Google Search
        # -----------------------------

        elif action == "google_search":

            return TOOLS["google_search"](
                plan["query"]
            )

        # -----------------------------
        # LeetCode
        # -----------------------------

        elif action == "leetcode":

            return TOOLS["leetcode"](
                plan["topic"]
            )

        # -----------------------------
        # Workspace
        # -----------------------------

        elif action == "workspace":

            if plan["workspace"] == "dsa":

                TOOLS["workspace_dsa"]()

                return True, "DSA Workspace Ready."

        return False, "Unknown action."