import requests


def translate(text):
    response = requests.post(
        'https://translate.yandex.net/api/v1/tr.json/translate',
        params={
            'id': '3d08a42c.5c583f38.905d8676-0-0',
            'srv': 'tr-text',
            'lang': 'ru-en',
            'reason': 'paste'
        },
        data={
            'text': text
        }
    )

    return ''.join(response.json()['text'])


print(translate('Приветствую коллеги'))
