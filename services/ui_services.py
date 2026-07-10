from ui.ui_controller import UIController


class UIService:

    def __init__(self, window):

        self.controller = UIController(window)

    def controller_instance(self):

        return self.controller