import json

# pretty print. Выводит в более красивом виде информацию. Без него функция print выводила
# бы инфу в одну строчку. Очень удобная штука.
# Кстати он выводит информацию в алфавитном порядке
from pprint import pprint


with open('GodFather.json') as text:
    movie = json.load(text)  # изменят файл с JSON формата в формат Python
    pprint(movie)
