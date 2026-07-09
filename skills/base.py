from vision.capture import capture
from vision.ocr import read_text
from vision.analyzer import VisionAnalyzer


class BaseSkill:

    def __init__(self):

        self.vision = VisionAnalyzer()

    def analyze(self, prompt):

        image = capture()

        text = read_text(image)

        return self.vision.analyze(

            prompt + "\n\n" + text

        )