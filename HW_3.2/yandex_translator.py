import requests


def translate(text, lang_from, lang_to):
    response = requests.post(
        'https://translate.yandex.net/api/v1/tr.json/translate',
        params={
            'key': 'trnsl.1.1.20190205T142849Z.bc010e7d38e65ecb.ddbfd383b957cedd2de27c35168d010aaf0362a1',
            'id': '3d08a42c.5c583f38.905d8676-0-0',
            'srv': 'tr-text',
            'lang': '{}-{}'.format(lang_from, lang_to),
            'reason': 'paste'
        },
        data={
            'text': str(text)
        }
    )

    print(''.join(response.json()['message']))
    print(response.json())


def set_params():
    file = 'DE.txt' #input('Введите название файла, который необходимо перевести: ')
    lang_from = 'de' #input('Введите язык, с которого нужно перевести: ')
    lang_to = 'ru' #input('Введите язык, на который нужно перевести (по-умолчанию русский): ')
    # проверяем язык, на который нужно переводить
    if lang_to == '':
        lang_to = 'ru'
    # вытаскиваем текст из файла
    with open(file, encoding='utf-8') as text_file:
        text = text_file.read()
        # print(text)
    return translate(text, lang_from, lang_to)
    # print(text)


set_params()

# translate('Приветствую коллеги')
