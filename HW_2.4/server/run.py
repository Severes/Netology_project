import os
import json

# получаем абсолютный путь до config.json
file_dir = os.path.dirname(__file__)
abs_file_dir = os.path.abspath(file_dir)
config_path = os.path.join(abs_file_dir, 'config.json')
print(config_path)

with open(config_path) as text:
    print(json.load(text))


# Данная программа (то есть файл run.py) уже не зависит от рабочей директории и из любой директории при запуске
# найдет путь до файла config.json благодаря формированию абослютного пути до файла


# ДОМАШКА

