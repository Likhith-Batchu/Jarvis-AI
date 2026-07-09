from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from ui.theme import *


class TitleWidget(QLabel):

    def __init__(self):

        super().__init__("⚡ JARVIS")

        self.setAlignment(Qt.AlignCenter)

        self.setStyleSheet(f"""

            color:{PRIMARY};

            font-size:24px;

            font-weight:bold;

            padding:10px;

        """)