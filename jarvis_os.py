import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from ui.ui_controller import UIController

from core.jarvis import Jarvis

from voice.speaker import speak

from controllers.voice_controller import VoiceController


voice = VoiceController()
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


def start_listening():

        ui.set_status("listening")

        text = voice.listen_once()

        window.input_widget.input.setText(text)

        ui.set_status("standby")


window.input_widget.send.clicked.connect(send_message)

window.input_widget.input.returnPressed.connect(send_message)

window.input_widget.mic.clicked.connect(start_listening)

window.show()

sys.exit(app.exec())