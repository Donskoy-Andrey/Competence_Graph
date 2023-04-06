"""
Cleaning text from rubbish characters and words.
"""

from src.params import *
import re


def file_processing(path: str) -> str:
    """
    The main function for cleaning files.

    Args:
        path: str
            Path to txt-file.
    Returns:
        final: str
            Reassembled file to a clean row.
    """
    with open(STOPWORDS_PATH, 'r', encoding='utf-8') as file:
        stop_words = [string.strip() for string in file.readlines()]

    print(f"Processing: {path}")
    with open(path, 'r', encoding='utf8') as file:
        text = [line.strip() for line in file.readlines()]
        text = ' '.join(text).replace('- ', '')
        text = re.sub(r'[^а-яё\sА-ЯЁ-]', '', text)

        current_stop_words = set(stop_words)
        pymorphy_results = list(map(lambda x: morph.parse(x), text.split()))
        final = ' '.join([
            res[0].normal_form for res in pymorphy_results
            if (res[0].normal_form not in current_stop_words) and
               (len(res[0].normal_form) > 2)
        ])

    with open(path, 'w', encoding='utf8') as file:
        print(f"Write clear article to: {path}")
        file.write(final)

    return final
