from vision.capture import capture
from vision.ocr import read_text
from vision.analyzer import VisionAnalyzer

print("📸 Taking Screenshot...")

image = capture()

print("👀 Reading Screen...")

text = read_text(image)

print("🧠 Thinking...\n")

vision = VisionAnalyzer()

reply = vision.analyze(text)

print(reply)