import random

from PySide6.QtWidgets import QLabel

from PySide6.QtCore import Qt, QTimer

from ui.theme import *


class WaveformWidget(QLabel):

    def __init__(self):

        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        self.setStyleSheet(f"""

            color:{PRIMARY};

            font-size:18px;

        """)

        self.timer = QTimer()

        self.timer.timeout.connect(self.animate)

        self.timer.start(100)

    def animate(self):

        bars = ""

        for _ in range(20):

            bars += random.choice("▁▂▃▄▅▆▇█")

        self.setText(bars)