import json
import chardet

file = 'newscy.json'

# открываем файл и считываем весь текст построчно, попутно вычисляя кодировку
with open(file, 'rb') as text:
    six_digit_list = list()
    text2 = text.read()
    result = chardet.detect(text2)
    print(result)
    text3 = text2.decode(result['encoding'])
    text_split = text3.split()
    # print(text_split)

    # на этот раз открываем файл в уже правильной кодировке, полученной из предыдущего файла
    with open(file, encoding=result['encoding']) as text:
        six_digit_list = list()
        movie = json.load(text)  # изменят файл с JSON формата в формат Python
        i = 0
        movie_full_text = ''
        items_len = len(movie['rss']['channel']['items'])  # выходим на уровень списка items и просматриваем,
        # сколько в нем элементов

        # перебираем каждый элемент списка items, вытаскиваем значение ключа description и включаем в общий текст
        for i in range(items_len):
            movie_channel_description = movie['rss']['channel']['items'][i]['description']
            movie_full_text += movie_channel_description + ' '
            i += 1
        movie_full_text_list = movie_full_text.split(' ')  # делаем список слов из единой строки текста. Это
        # необходимо, потому что строка неизменяемый объект и его не получится перебрать циклом
        # print(movie_full_text_list)
        for word in movie_full_text_list:
            if len(word) > 6:
                six_digit_list.append(word)
    print('Слова с более чем 6 символами:', six_digit_list)
    # print(movie_full_text)
    # считаем повторения слов в списке и создаем список из значения и его количества в списке
    six_digit_list_count = list()
    for item in six_digit_list:
        x = item, six_digit_list.count(item)
        if x not in six_digit_list_count:
            six_digit_list_count.append(x)
    # print(six_digit_list_count)

    # функция, которая поможет отсортировать значения в списке в зависимости от количества повторений слов в списке
    def sorted_key(key):
        return key[1]

    # сортируем список по количеству повторений значений этого списка
    sorted_six_digit_list_count = sorted(six_digit_list_count, key=sorted_key, reverse=True)

    # На строках 34-36 данного скрипта
    # (x = item, six_digit_list.count(item)
    #     if x not in six_digit_list_count:
    #         six_digit_list_count.append(x))
    # мы составили список, в котором элементами кортежи.
    # Ниже мы элементы итогового списка превращаем в списки и выводим первый элемент этого списка
    hateful_10 = list()
    for a in range(10):
        item_list = list(sorted_six_digit_list_count[a])
        hateful_10.append(item_list[0])

    # Выводим итоговый список строк
    print("10 максимально повторяющихся слов из списка: ", hateful_10)





