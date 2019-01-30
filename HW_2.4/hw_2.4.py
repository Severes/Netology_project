import os
'''
Задание
мне нужно отыскать файл среди десятков других
я знаю некоторые части этого файла (на память или из другого источника)
я ищу только среди .sql файлов
1. программа ожидает строку, которую будет искать (input())
после того, как строка введена, программа ищет её во всех файлах
выводит список найденных файлов построчно
выводит количество найденных файлов
2. снова ожидает ввод
поиск происходит только среди найденных на этапе 1
3. снова ожидает ввод
...
Выход из программы программировать не нужно.
Достаточно принудительно остановить, для этого можете нажать Ctrl + C
'''

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

# Поехали...

# создаем путь до папки с файлами
migration_path = os.path.join(current_dir, migrations)
# меняем рабочую директорию на папку Migrations с файлами
os.chdir(migration_path)
# создаем список файлов из папки Migrations
file_list = os.listdir(migration_path)

if __name__ == '__main__':
    # функция получения общего списка SQL файлов
    def getting_main_sql_list():
        file_list_sql = list()
        for file in file_list:
            if '.sql' in file:
                file_list_sql.append(file)
        # print(len(file_list_sql))  # тестирование
        a = file_list_sql
        return input_text_search(a)

    # функция, которая будет принимать строчку
    def input_text_search(a):
        text_to_find = input('Введите текст для поиска: ')
        # print(len(a))  # тестирование
        return file_list_removing(text_to_find, a)

    # функция сокращения списка в зависимости от фразы
    def file_list_removing(text_to_find, a):
        file_list_execute = list()
        for file in a:
            with open(file) as text:
                sql_text = text.read()
                # print(sql_text)  # тестирование
                if text_to_find.lower() in sql_text.lower():
                    # print(file)  # тестирование
                    file_list_execute.append(file)
        print('Список файлов:')
        print('\n'.join(file_list_execute))
        print('Всего: ', len(file_list_execute))
        return input_text_search(file_list_execute)

    getting_main_sql_list()
    pass

