import pytesseract
from PIL import Image
import io

def extract_text_from_image(image):
    try:
        img = Image.open(io.BytesIO(image))  
        text = pytesseract.image_to_string(img)  
        return text.strip() if text.strip() else "Error: No text detected."
    except Exception as e:
        return f"Error: {str(e)}"
