from core.runtime import Runtime


class RuntimeService:

    def __init__(self):

        self.runtime = Runtime()

    def instance(self):

        return self.runtime