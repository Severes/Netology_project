import requests
import os


def translate(file, text, lang_from, lang_to):
    text_parts = list()
    translated_text = list()
    x = 0
    while len(''.join(text_parts)) < len(text):
        y = x + 500
        text_parts.append(text[x:y])
        x += 500
        # print(len(''.join(text_parts)))
        # print(text_parts)
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
        # print(''.join(response.json()['text']))
        translated_text.append(''.join(response.json()['text']))
        # print(''.join(response.json()['message']))
        # print(response.json())
    # print(translated_text)
    with open(os.path.splitext(file)[0]+'_TRANSLATED.txt', mode='a') as text_new:
        # данный print не выведется в нашем скрипте, а направится в файл log.txt и запишет выводимый текст
        # в созданный файл
        print(''.join(translated_text), file=text_new)


def set_params():
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