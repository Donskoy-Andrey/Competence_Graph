"""
Interface for Tesseract-OCR
"""

import pytesseract
from pdf2image import convert_from_path


def get_ocr_file(pdf_path: str) -> str:
    """
    Convert pdf file to string variable.
    Args:
        pdf_path: str
            Path to pdf file.

    Returns:
        text: str
            All text from pdf-pages.
    """
    # Convert the PDF to an image
    images = convert_from_path(pdf_path)

    # Loop through all the pages and extract text using pytesseract
    text = ""
    for page in images:
        page_text = pytesseract.image_to_string(page, lang='rus+eng')
        text += page_text

    return text
