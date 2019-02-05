import requests
import os


def translate(file, text, lang_from, lang_to):
    ''' Описание фурнкции

    :param file: имя открываемого файла
    :param text: текст файла file
    :param lang_from: язык, с которого переводим
    :param lang_to: язык, накоторый переводим
    :return: создает новый документ,в который вставляет переведенный текст
    '''
    text_parts = list()
    translated_text = list()
    x = 0
    # пока длина списка text_parts в символах не станет станет равна длине текста из файла file
    # данный икл бед трезать длину текста файла и помещать эичасти в виде элементов списка text_parts
    while len(''.join(text_parts)) < len(text):
        y = x + 500
        text_parts.append(text[x:y])
        x += 500
        # print(len(''.join(text_parts)))
        # print(text_parts)
    # данный цикл берет кажду часть списка text_parts и отправляет запросом post данный текст через API Яндекс
    # переводчик. Затем часть уже переведенного текста вставляется в список translated_text
    for part in text_parts:
        response = requests.get(
            'https://translate.yandex.net/api/v1/tr.json/translate',
            params={
                'key': 'trnsl.1.1.20190205T142849Z.bc010e7d38e65ecb.ddbfd383b957cedd2de27c35168d010aaf0362a1',
                'id': '3d08a42c.5c583f38.905d8676-0-0',
                'srv': 'tr-text',
                'lang': '{}-{}'.format(lang_from, lang_to),
                'reason': 'paste',
            },
            data={
                'text': str(part)
            }
        )
        translated_text.append(''.join(response.json()['text']))
        # print(response.json()) #  проврека на наличие других тэгов JSON
    with open(os.path.splitext(file)[0]+'_TRANSLATED.txt', mode='a') as text_new:
        # данный print не выведется в нашем скрипте, а направится в файл os.path.splitext(file)[0]+'_TRANSLATED.txt'
        # и запишет выводимый текст в созданный файл
        print(''.join(translated_text), file=text_new)


def set_params():
    ''' Описание функции
    Запрашивает данные у пользователя
    Открывает документ и считывает текст
    :return:
    запускает функцию по работе с API Яндекс Переводчик
    '''
    file = input('Введите название файла, который необходимо перевести: ')
    lang_from = input('Введите язык, с которого нужно перевести: ')
    lang_to = input('Введите язык, на который нужно перевести (по-умолчанию русский): ')
    # проверяем язык, на который нужно переводить
    if lang_to == '':
        lang_to = 'ru'
    # вытаскиваем текст из файла
    with open(file, encoding='utf-8') as text_file:
        text = text_file.read()
        # print(text)
    return translate(file, text, lang_from, lang_to)
    # print(text)


set_params()
