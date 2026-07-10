from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout

from PySide6.QtCore import Qt

from ui.title_widget import TitleWidget
from ui.status_widget import StatusWidget
from ui.waveform_widget import WaveformWidget

from ui.theme import *

from ui.chat_widget import ChatWidget
from ui.input_widget import InputWidget
from ui.notification_widget import NotificationWidget

class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("JARVIS")

        self.resize(420,550)

        self.setStyleSheet(f"""

            background:{BACKGROUND};

            border-radius:20px;

        """)

        self.setWindowFlags(

            Qt.FramelessWindowHint |

            Qt.WindowStaysOnTopHint

        )
        self.notification = NotificationWidget()

        layout = QVBoxLayout()

        self.title = TitleWidget()

        self.status = StatusWidget()

        self.wave = WaveformWidget()

        self.chat = ChatWidget()

        self.input_widget = InputWidget()

        layout.addWidget(self.title)

        layout.addWidget(self.status)

        layout.addWidget(self.wave)

        layout.addWidget(self.title)

        layout.addWidget(self.status)

        layout.addWidget(self.wave)

        layout.addWidget(self.chat)

        layout.addWidget(self.input_widget)

        layout.addWidget(self.notification)

        self.setLayout(layout)