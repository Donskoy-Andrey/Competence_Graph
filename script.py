import pandas as pd
from src.params import *
from sklearn.feature_extraction.text import TfidfVectorizer
from src.OCR import get_ocr_file
from script_transform_pdf import extractor, load_articles_data
from src.txt_file_processing import file_processing


mydict_files = sorted(list(PROCESSED_DICT_PATH.rglob('*.txt')))
articles_files = sorted(list(PROCESSED_ARTICLE_PATH.rglob('*.txt')))
articles_names = [i.name for i in articles_files]
mydict_names = [i.name for i in mydict_files]

def start_ocr(filename_pdf: str) -> None:
    print('File unreadable. Use OCR...')
    filename_txt = filename_pdf[:-4] + '.txt'
    text = get_ocr_file(TEST_FOLDER_PATH+filename_pdf)
    with open(PROCESSED_TEST_PATH+filename_txt, 'w', encoding='utf-8') as file:
        file.write(text)

    df = check_new_file(PROCESSED_TEST_PATH+filename_txt, fromOCR=True)
    all_names = df.term.head(N_SEARCH_ROWS).values

    df['variants'] = \
        df.term.head(N_ROWS).apply(
            lambda x: ', '.join(
                [i for i in all_names if (x in i) and (x != i)][:N_ADD_ROWS - 1]
            )
        )
    df.index = range(1, df.shape[0] + 1)
    df.head(N_ROWS).to_excel(PATH_TO_SAVE, encoding='utf-8')


def check_new_file(path: str, fromOCR: bool = False) -> pd.DataFrame():
    new_articles_data = load_articles_data()
    current_file_path = Path(path)
    if fromOCR:
        txt_file_path = path
    else:
        txt_file_path = extractor(current_file_path, folder='test_folder', return_path=True)
    new_file_txt = file_processing(txt_file_path)
    new_articles_data.append(new_file_txt)

    vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_df=0.9)
    vectors = vectorizer.fit_transform(new_articles_data)

    xlsx_file = pd.DataFrame(
        vectors.toarray(),
        columns=vectorizer.get_feature_names_out(),
        index=articles_names + [current_file_path.name]
    )
    xlsx_file = xlsx_file.loc[current_file_path.name, :].sort_values(ascending=False)

    return xlsx_file.to_frame().reset_index().rename(
        {'index': 'term', f'{current_file_path.name}': 'value'}, axis=1
    )


def main() -> None:
    test_file = input('Enter file name from test_folder. Example: file.pdf\n')
    check_path = TEST_FOLDER_PATH + test_file

    df = check_new_file(check_path)
    all_names = df.term.head(N_SEARCH_ROWS).values

    df['variants'] = \
        df.term.head(N_SEARCH_ROWS)\
            .apply(lambda x: ', '.join(
            [i for i in all_names
                if (x in i) and (x != i)][:N_ADD_ROWS-1]
            )
        )
    df.index = range(1, df.shape[0] + 1)
    print(f"Saving result: {PATH_TO_SAVE}")
    df.head(N_ROWS).to_excel(PATH_TO_SAVE, encoding='utf-8')

    if df.loc[1, 'value'] < 0.05:
        start_ocr(test_file)

if __name__ == '__main__':
    main()
