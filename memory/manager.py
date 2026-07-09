from assistant.memory import Memory
from memory.extractor import MemoryExtractor


class MemoryManager:

    def __init__(self):

        self.database = Memory()
        self.extractor = MemoryExtractor()

    def process(self, message):

        try:

            result = self.extractor.extract(message)

            if result.get("remember"):

                self.database.remember(
                    result["key"],
                    result["value"]
                )

                return f"Remembered {result['key']}."

        except Exception:
            pass

        return None