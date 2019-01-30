import os

# просмотр текущей директории
current_dir = os.getcwd()
print('Current dir: {}'.format(current_dir))

# изменение текущей директории. Прыгаем на 2 уровня выше. НО по сути рабочая директория изменилась только
# для этой программы. Для остальных программ она осталась прежней
os.chdir('../..')

# просматриваем измененнную дирекорию
current_dir = os.getcwd()
print('New current dir: {}'.format(current_dir))


# # изменение рабочей директории
# new_directory = '/etc/'
# os.chdir(new_directory)  # новая директория /etc
# os.chdir('cup')  # новая директория /etc/cups
