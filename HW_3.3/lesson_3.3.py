from urllib.parse import urlencode
import requests

AUTH_URL = 'https://oauth.vk.com/authorize'
API_ID = '6849372'

auth_data = {
    'client_id': API_ID,
    'display': 'mobile',  # popup, mobile, page
    'scope': 'status, friends, video',  # friends, video, photo
    'response_type': 'token',
    'v': '5.92'  # API version. Текущая версия апи вк = 5.92
}

# При помощи данного запроса мы получаем token, чтобы взаимодействовать с API VK. После того как мы получили токен,
# анная строка нам больше не нужна. токен мы записали в переменную TOKEN
# print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = '327cca380d1a3753352e5f8e4bfb00eecefbb5a77df2f57841ea13583a7717ffa6964f841ea73bae8aa62'

params = {
    'access_token': TOKEN,
    'v': '5.92'
}
# возвращает список друзей, которые сейчас on-line
# response = requests.get('https://api.vk.com/method/friends.getOnline', params)
# print(response.json()['response'])

# возвращает текущий статус пользователя
response1 = requests.get('https://api.vk.com/method/status.get', params)
print(response1.json())

# расширяем словарь params начением 'text'
params['text'] = 'Some text'

# изменяет текст статуса на тот, что указан в параметре 'text', который указан в params
response2 = requests.get('https://api.vk.com/method/status.set', params)
print(response2.json())

# снова запрашиваем статус текущего пользователя
response3 = requests.get('https://api.vk.com/method/status.get', params)
print(response3.json())
