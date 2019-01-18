########################################################################################################################
# Взять из github-репозитория все файлы с новостями в формате txt: newsfr.txt, newsit.txt, newsafr.txt, newscy.txt.
# Для этого нужно склонировать репозиторий, или скачать его архивом.
#
# Для определения кодировки использовать модуль chardet
#
# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях
# слов длиннее 6 символов для каждого файла.
#
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания
# вам могут помочь: split(), sort() или sorted().
########################################################################################################################

import chardet

# открываем файл и считываем весь текст построчно, попутно вычисляя кодировку и форматируя итоговый список
# таким образом, чтобы отобрать слова с длинной от 6 символов
with open('newsafr.txt', 'rb') as text:
    six_digit_list = list()
    text2 = text.read()
    result = chardet.detect(text2)
    print(result)
    text3 = text2.decode(result['encoding'])
    text_split = text3.split()
    # print(text_split)
    for word in text_split:
        if len(word) > 5:
            six_digit_list.append(word)
print('Слова с более чем 6 символами:', six_digit_list)

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
# print('Отсортированный список', sorted_six_digit_list_count)

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







