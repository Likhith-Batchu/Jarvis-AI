import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def read_text(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)