from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton

from ui.theme import *


class InputWidget(QWidget):

    def __init__(self):

        super().__init__()

        layout = QHBoxLayout()

        self.input = QLineEdit()

        self.input.setPlaceholderText("Ask Atlas...")

        self.input.setStyleSheet(f"""
        QLineEdit {{
            background:{CARD};
            color:{TEXT};
            border:2px solid {BORDER};
            border-radius:12px;
            padding:10px;
            font-size:14px;
        }}

        QLineEdit:focus {{
            border:2px solid {PRIMARY};
        }}
        """)

        self.mic = QPushButton("🎤")

        self.send = QPushButton("➤")

        self.mic.setFixedWidth(55)

        self.send.setFixedWidth(55)

        button_style = f"""
        QPushButton {{
            background:{PRIMARY};
            color:black;
            border:none;
            border-radius:12px;
            font-size:18px;
            font-weight:bold;
        }}

        QPushButton:hover {{
            background:#48E7FF;
        }}
        """

        self.mic.setStyleSheet(button_style)

        self.send.setStyleSheet(button_style)

        layout.addWidget(self.input)

        layout.addWidget(self.mic)

        layout.addWidget(self.send)

        self.setLayout(layout)