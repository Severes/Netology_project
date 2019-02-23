from urllib.parse import urlencode
import requests
from pprint import pprint

# Тимошенко 16269654
# Мой 80619823

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
# данная строка нам больше не нужна. Токен мы записали в переменную TOKEN
# print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = '53518ccf894a013eff70bea649a575f55ceca46c07cdc315ad5eb04fd213f9b4a4a22a5f2fd914936cdd9'

params = {
    'access_token': TOKEN,
    'v': '5.92'
}


def friends_online():
    """
    :return: Возвращает список друзей, которые сейчас on-line
    """
    response = requests.get('https://api.vk.com/method/friends.getOnline', params)
    print(response.json()['response'])


def changing_mine_status():
    """
    Изменяет текст статуса на тот, что указан в параметре 'text', который указан в переменной params
    :return: возвращает текущий статус пользователя
    :return: возвращает новый статус пользователя после изменения статуса

    """
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


def common_friends(id2, id1=None):
    """
    :param id1: id первого пользователя. Если не указан - берется текущий пользователь
    :param id2: id второго пользователя. Обязательный
    :return:    возвращает общих друзей двух пользователей
    """
    # добавляем необходимые параметры в params
    if id1 is not None:
        params['source_uid'] = str(id1)
    params['target_uid'] = str(id2)
    # фрмируем запрос списка общих друзей
    response1 = requests.get('https://api.vk.com/method/friends.getMutual', params)
    result1 = ','.join(str(n) for n in response1.json()['response'])
    # изменяем params для следующего запроса
    if id1 is not None:
        del params['source_uid']
    del params['target_uid']
    params['user_ids'] = result1
    params['fields'] = 'domain'
    # формируем запрос со списком общих друзей + ссылка на профиль каждого друга
    response2 = requests.get('https://api.vk.com/method/users.get', params)
    result2 = response2.json()['response']
    result4 = dict()
    for dict_r in result2:
        link = 'https://vk.com/' + dict_r['domain']
        result4[dict_r['first_name'] + ' ' + dict_r['last_name']] = []
        result4[dict_r['first_name'] + ' ' + dict_r['last_name']].append(dict_r['id'])
        result4[dict_r['first_name'] + ' ' + dict_r['last_name']].append(link)
    for n in result4.values():
        pprint(n)


common_friends(16269654, 80619823)
