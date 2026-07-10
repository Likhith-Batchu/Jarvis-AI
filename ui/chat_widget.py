from PySide6.QtWidgets import QTextEdit
from ui.theme import *


class ChatWidget(QTextEdit):

    def __init__(self):

        super().__init__()

        self.setReadOnly(True)

        self.setStyleSheet(f"""
            background:{CARD};
            color:{TEXT};
            border:1px solid {BORDER};
            border-radius:12px;
            padding:8px;
            font-size:13px;
        """)

    def add_user(self, text):

        self.append(f"<b>👤 You:</b> {text}<br>")

    def add_jarvis(self, text):

        self.append(f"<b>🤖 Jarvis:</b> {text}<br>")