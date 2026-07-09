from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout

from PySide6.QtCore import Qt

from ui.title_widget import TitleWidget
from ui.status_widget import StatusWidget
from ui.waveform_widget import WaveformWidget

from ui.theme import *


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("JARVIS")

        self.resize(320,220)

        self.setStyleSheet(f"""

            background:{BACKGROUND};

            border-radius:20px;

        """)

        self.setWindowFlags(

            Qt.FramelessWindowHint |

            Qt.WindowStaysOnTopHint

        )

        layout = QVBoxLayout()

        self.title = TitleWidget()

        self.status = StatusWidget()

        self.wave = WaveformWidget()

        layout.addWidget(self.title)

        layout.addWidget(self.status)

        layout.addWidget(self.wave)

        self.setLayout(layout)