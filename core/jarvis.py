from assistant.brain import Brain
from assistant.ai_planner import AIPlanner
from core.executor import Executor
from core.task_manager import TaskManager


class Jarvis:

    def __init__(self):

        self.brain = Brain()

        self.planner = AIPlanner()

        self.executor = Executor()

        self.task_manager = TaskManager()

    def process(self, user_input):

        print("STEP A")

        plan = self.planner.plan(user_input)

        print("STEP B", plan)

        if plan["action"] == "chat":

            print("STEP C")

            return self.brain.ask(user_input)

        print("STEP D")

        actions = [plan]

        results = self.task_manager.execute(
        self.executor,
        actions
        )

        print("STEP E")

        return "\n".join(results)