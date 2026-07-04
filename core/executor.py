from tools.app_launcher import open_application
from tools.browser import (
    open_website,
    google_search,
    open_leetcode_topic
)
from workspaces.dsa import start as start_dsa

from assistant.memory import Memory


class Executor:

    def __init__(self):
        self.memory = Memory()

    def execute(self, plan):

        action = plan["action"]

        # ------------------------
        # Applications
        # ------------------------

        if action == "open_application":
            return open_application(plan["app"])

        # ------------------------
        # Websites
        # ------------------------

        elif action == "open_website":
            return open_website(plan["website"])

        # ------------------------
        # Google Search
        # ------------------------

        elif action == "google_search":
            return google_search(plan["query"])

        # ------------------------
        # LeetCode
        # ------------------------

        elif action == "leetcode":
            return open_leetcode_topic(plan["topic"])

        # ------------------------
        # Workspaces
        # ------------------------

        elif action == "workspace":

            if plan["workspace"] == "dsa":
                start_dsa()
                return True, "DSA Workspace Ready."

            return False, "Unknown workspace."

        # ------------------------
        # Memory (temporary)
        # ------------------------

        elif action == "remember":

            print("\nMemory feature will be upgraded in Sprint 3.\n")

            return True, "Memory module detected."

        elif action == "recall":

            print("\nRecall feature will be upgraded in Sprint 3.\n")

            return True, "Recall module detected."

        return False, "Unknown action."