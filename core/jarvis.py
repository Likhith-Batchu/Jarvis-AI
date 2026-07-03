from assistant.brain import Brain
from assistant.planner import Planner
from core.executor import Executor


class Jarvis:

    def __init__(self):

        self.brain = Brain()
        self.planner = Planner()
        self.executor = Executor()

    def process(self, message):

        plan = self.planner.plan(message)

        if plan["tool"]:

            return self.executor.execute(plan)

        return self.brain.ask(message)