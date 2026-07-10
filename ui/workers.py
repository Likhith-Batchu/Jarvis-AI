from PySide6.QtCore import QObject, Signal, Slot
import traceback


class AIWorker(QObject):

    finished = Signal(str)

    def __init__(self, jarvis, text):
        super().__init__()

        self.jarvis = jarvis
        self.text = text

    @Slot()
    def run(self):

        print("STEP 1")

        try:

            print("STEP 2")

            reply = self.jarvis.process(self.text)

            print("STEP 3")

            self.finished.emit(reply)

            print("STEP 4")

        except Exception:

            traceback.print_exc()

            self.finished.emit("An error occurred.")