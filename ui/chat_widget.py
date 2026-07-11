from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QScrollArea
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QScrollBar
from ui.message_widget import MessageWidget


class ChatWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.layout = QVBoxLayout()

        self.layout.addStretch()

        container = QWidget()

        container.setLayout(self.layout)

        self.scroll = QScrollArea()

        self.scroll.setWidgetResizable(True)

        self.scroll.setWidget(container)

        root = QVBoxLayout()

        root.addWidget(self.scroll)

        self.setLayout(root)

    def add_user(self, text):

        self.layout.insertWidget(

            self.layout.count()-1,

            MessageWidget("user", text)

        )
        QTimer.singleShot(
        0,
        lambda: self.scroll.verticalScrollBar().setValue(
        self.scroll.verticalScrollBar().maximum()
         )
        )

    def add_jarvis(self, text):

        self.layout.insertWidget(

            self.layout.count()-1,

            MessageWidget("jarvis", text)

        )

        QTimer.singleShot(
    0,
    lambda: self.scroll.verticalScrollBar().setValue(
        self.scroll.verticalScrollBar().maximum()
    )
)