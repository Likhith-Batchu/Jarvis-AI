from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from ui.theme import *


class StatusWidget(QLabel):

    COLORS = {

        "standby": "#22C55E",

        "listening": "#22C55E",

        "thinking": "#A855F7",

        "executing": "#F59E0B",

        "speaking": "#38BDF8",

        "error": "#EF4444"
    }

    def __init__(self):

        super().__init__("💤 Standby")

        self.setAlignment(Qt.AlignCenter)

        self.set_status("standby")

    def set_status(self, state):

        color = self.COLORS.get(state, TEXT)

        names = {

            "standby": "💤 Standby",

            "listening": "🎤 Listening",

            "thinking": "🧠 Thinking",

            "executing": "⚙ Executing",

            "speaking": "🔊 Speaking",

            "error": "❌ Error"

        }

        self.setText(names[state])

        self.setStyleSheet(f"""

            color:{color};

            font-size:18px;

            font-weight:bold;

        """)