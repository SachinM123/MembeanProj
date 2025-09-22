import pytesseract
from PIL import ImageGrab
from PIL import Image
def read_screenshot(screenshot_path):
    """Reads text from an image using OCR."""
    try:
        img = Image.open(screenshot_path)
        text = pytesseract.image_to_string(img)
        print(f"OCR Text: {text}")
        return text
    except FileNotFoundError:
        print(f"Error: Screenshot file not found at {screenshot_path}")
        return ""
    except Exception as e:
        print(f"Error during OCR: {e}")
        return ""
    
read_screenshot("Screenshot 2025-04-16 095446.png")
print("===================================")
read_screenshot("Screenshot 2025-04-19 153919.png")