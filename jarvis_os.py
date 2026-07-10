import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from ui.ui_controller import UIController

from core.jarvis import Jarvis

from voice.speaker import speak


jarvis = Jarvis()

app = QApplication(sys.argv)

window = MainWindow()

ui = UIController(window)


def send_message():

    text = window.input_widget.input.text().strip()

    if not text:
        return

    ui.user_message(text)

    window.input_widget.input.clear()

    ui.set_status("thinking")

    try:

        reply = jarvis.process(text)

        ui.jarvis_message(reply)

        ui.set_status("speaking")

        speak(reply)

    except Exception as e:

        ui.jarvis_message(f"ERROR:\n{e}")

    finally:

        ui.set_status("standby")


window.input_widget.send.clicked.connect(send_message)

window.input_widget.input.returnPressed.connect(send_message)

window.show()

sys.exit(app.exec())