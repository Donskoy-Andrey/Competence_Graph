from pathlib import Path
import pymorphy2

# Extraction and Processing
ORIGINAL_DICT_PATH = Path("data/original_data/mydict")
ORIGINAL_ARTICLE_PATH = Path("data/original_data/articles")
PROCESSED_DICT_PATH = Path("data/processed_data/mydict")
PROCESSED_ARTICLE_PATH = Path("data/processed_data/articles")
CLEAR_TEXT = "data/processed_data/clear_text.txt"

START_EXTRACTION = False
CREATE_CLEAR_TEXT = False

# Tesseract Parameters
TESSERACT_EXE = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSERACT_DATA = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
TESSERACT_POPPLER = r'C:\Users\User\Downloads\poppler-0.68.0_x86\poppler-0.68.0\bin'

# Text Cleaning
STOPWORDS_PATH = r'data/stopwords.txt'
punctuation = r'!\"#$%&\'()*+,./:;<=>?@[\]^_`{|}~'
morph = pymorphy2.MorphAnalyzer()

# Test Processing
TEST_FOLDER_PATH = "data/test_folder/"
PATH_TO_SAVE = "data/result/result.xlsx"
NEW_STOP_PATH = "data/new_stop.txt"

# Saving Parameters
N_ROWS = 30
N_SEARCH_ROWS = 200  # n-top terms, where we are searching options
N_ADD_ROWS = 5
