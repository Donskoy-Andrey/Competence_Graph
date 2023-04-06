"""
The main script for creating a dictionary of articles.
"""

from pdfminer.high_level import extract_text
from src.txt_file_processing import file_processing
from typing import Optional
from src.params import *

def extractor(path: Path, folder: str, return_path: bool = False) -> Optional[str]:
    """ Extract text from pdf files """

    print(f"Extraction: {path}")
    file = extract_text(path)
    result_path = f"data/processed_data/{folder}/{path.name}"[:-3]+'txt'
    with open(result_path, 'w', encoding='utf-8') as f:
        f.write(file)

    if return_path:
        return result_path

def load_articles_data() -> list[str]:
    """ Get all txt data """

    with open(CLEAR_TEXT, 'r') as file:
        articles_data = file.readlines()
    return articles_data

def save_articles_data(articles_data: list, mode='w') -> None:
    """ Group txt files into CLEAR_TEXT """

    if mode == 'w':
        with open(CLEAR_TEXT, 'w', encoding='utf-8') as file:
            file.write('\n'.join(articles_data))

    elif mode == 'a':
        with open(CLEAR_TEXT, 'a', encoding='utf-8') as file:
            file.write('\n' + articles_data[-1])

def start_extraction() -> None:
    """ Start extraction process """

    mydict_files = sorted(
        list(
            ORIGINAL_DICT_PATH.rglob('*.pdf')
        )
    )
    articles_files = sorted(
        list(
            ORIGINAL_ARTICLE_PATH.rglob('*.pdf')
        )
    )

    [extractor(path, folder='mydict') for path in mydict_files]
    [extractor(path, folder='articles') for path in articles_files]


def create_clear_txt() -> None:
    """ Save all data as a processed txt file """

    mydict_files = sorted(list(PROCESSED_DICT_PATH.rglob('*.txt')))
    articles_files = sorted(list(PROCESSED_ARTICLE_PATH.rglob('*.txt')))

    mydict_data = [file_processing(path) for path in mydict_files]
    articles_data = [file_processing(path) for path in articles_files]

    save_articles_data(articles_data)


if __name__ == '__main__':
    if START_EXTRACTION:
        start_extraction()

    if CREATE_CLEAR_TEXT:
        create_clear_txt()
