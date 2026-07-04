from assistant.brain import Brain
from assistant.planner import Planner
from core.executor import Executor


class Jarvis:

    def __init__(self):

        self.brain = Brain()

        self.planner = Planner()

        self.executor = Executor()

    def process(self, user_input):

        plan = self.planner.plan(user_input)

        if plan["action"] == "chat":

            return self.brain.ask(user_input)

        success, message = self.executor.execute(plan)

        return message