from assistant.agent_planner import AgentPlanner
from assistant.plan_validator import PlanValidator
from core.executor import Executor
from core.task_manager import TaskManager


class Agent:

    def __init__(self):

        self.planner = AgentPlanner()
        self.validator = PlanValidator()

        self.executor = Executor()
        self.task_manager = TaskManager()

    def execute_goal(self, goal):

        plan = self.planner.plan(goal)


        print("=" * 50)
        print("JARVIS AGENT")
        print("=" * 50)

        print("\nGoal:")
        print(plan["goal"])

        print("\nPlan:")

        for i, step in enumerate(plan["steps"], start=1):

           print(f"{i}. {step}")

           print()
        

        plan = self.validator.validate(plan)

        results = self.task_manager.execute(

            self.executor,

            plan["steps"]

        )

        return "\n".join(results)