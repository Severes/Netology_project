import os

# изменение рабочей директории
new_directory = '/etc/'
os.chdir(new_directory)  # новая директория /etc
os.chdir('cup')  # новая директория /etc/cups
