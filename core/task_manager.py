class TaskManager:

    def execute(self, executor, actions):

        results = []

        for action in actions:

            success, message = executor.execute(action)

            results.append(message)

        return results