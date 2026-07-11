from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QVBoxLayout

from ui.theme import *


class MessageWidget(QWidget):

    def __init__(self, sender, message):

        super().__init__()

        root = QHBoxLayout()

        bubble = QLabel(message)

        bubble.setWordWrap(True)

        bubble.setMaximumWidth(450)

        bubble.setStyleSheet(f"""
            background:{CARD};
            color:{TEXT};
            padding:12px;
            border-radius:12px;
            font-size:14px;
        """)
        

        if sender == "user":

            root.addStretch()

            root.addWidget(bubble)
            bubble.setStyleSheet("""
            background:#2563EB;
            color:white;
            padding:16px;
            border-radius:14px;
            font-size:15px;
            """)

            

        else:

            root.addWidget(bubble)

            root.addStretch()
            bubble.setStyleSheet("""
            background:#2D2D2D;
            color:white;
            padding:16px;
            border-radius:18px;
            font-size:15px;
            """)

        self.setLayout(root)