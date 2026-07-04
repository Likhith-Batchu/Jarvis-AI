class Planner:

    def __init__(self):

        # Registered applications
        self.apps = [
            "chrome",
            "calculator",
            "notepad",
            "paint",
            "cmd",
            "explorer",
            "vscode",
            "apple music"
        ]

        # Registered websites
        self.websites = [
            "google",
            "youtube",
            "github",
            "chatgpt",
            "gmail"
        ]

        # LeetCode topics
        self.leetcode_topics = [
            "arrays",
            "strings",
            "linked list",
            "trees",
            "graph",
            "dynamic programming"
        ]

    def plan(self, message):

        message = message.lower()

        # ==========================
        # Applications
        # ==========================
        if "open" in message:

            for app in self.apps:

                if app in message:

                    return {
                        "action": "open_application",
                        "app": app
                    }

            for site in self.websites:

                if site in message:

                    return {
                        "action": "open_website",
                        "website": site
                    }

        # ==========================
        # Google Search
        # ==========================
        if message.startswith("search"):

            query = message.replace("search", "").strip()

            return {
                "action": "google_search",
                "query": query
            }

        # ==========================
        # LeetCode Topics
        # ==========================
        if "practice" in message:

            for topic in self.leetcode_topics:

                if topic in message:

                    return {
                        "action": "leetcode",
                        "topic": topic
                    }

        # ==========================
        # Workspaces
        # ==========================
        if "start dsa" in message:

            return {
                "action": "workspace",
                "workspace": "dsa"
            }

        if "start coding" in message:

            return {
                "action": "workspace",
                "workspace": "coding"
            }

        if "start machine learning" in message:

            return {
                "action": "workspace",
                "workspace": "ml"
            }

        # ==========================
        # Memory
        # ==========================
        if message.startswith("remember"):

            return {
                "action": "remember",
                "text": message.replace("remember", "").strip()
            }

        if message.startswith("what is my") or message.startswith("what's my"):

            return {
                "action": "recall",
                "question": message
            }

        # ==========================
        # Default Chat
        # ==========================
        return {
            "action": "chat"
        }