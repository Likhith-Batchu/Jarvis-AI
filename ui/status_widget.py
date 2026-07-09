from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from ui.theme import *


class StatusWidget(QLabel):

    def __init__(self):

        super().__init__("● Standby")

        self.setAlignment(Qt.AlignCenter)

        self.setStyleSheet(f"""

            color:{SUCCESS};

            font-size:18px;

        """)

    def update_status(self, text):

        self.setText(text)