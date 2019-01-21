import json
from pprint import pprint

with open('newsafr.json', encoding='windows-1251') as text:
    movie = json.load(text)  # изменят файл с JSON формата в формат Python
    pprint(movie)

    # six_digit_list = list()
    # text2 = text.read()
    # result = chardet.detect(text2)
    # print(result)
    # text3 = text2.decode(result['encoding'])
    # text_split = text3.split()
    # print(text_split)