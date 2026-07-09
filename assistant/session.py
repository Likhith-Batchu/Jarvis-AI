class Session:

    def __init__(self):

        self.current_skill = None
        self.last_result = None
        self.current_goal = None

    def set_skill(self, skill):

        self.current_skill = skill

    def get_skill(self):

        return self.current_skill

    def remember_result(self, result):

        self.last_result = result

    def get_result(self):

        return self.last_result

    def set_goal(self, goal):

        self.current_goal = goal

    def get_goal(self):

        return self.current_goal