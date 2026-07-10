from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

from ui.theme import *


class NotificationWidget(QLabel):

    def __init__(self):

        super().__init__("")

        self.setAlignment(Qt.AlignCenter)

        self.setStyleSheet(f"""

            background:{CARD};

            color:{TEXT};

            padding:8px;

            border-radius:10px;

        """)

    def show_message(self, text):

        self.setText(text)

        self.show()