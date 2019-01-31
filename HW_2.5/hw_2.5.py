import subprocess
import os
import shutil

# текущая директория
current_dir = os.path.dirname(os.path.abspath(__file__))
# создаем путь до папки с файлами
source_path = os.path.join(current_dir, 'Source')
# меняем рабочую директорию на папку Source с файлами
os.chdir(source_path)
# создаем список файлов из папки Source
file_list = os.listdir(source_path)
# иректория для хранения новых изображений
result_dir = os.path.join(current_dir, 'Result')

for file in file_list:
    # проверяем, существует ли новая директория Result
    if os.path.exists(result_dir) is False:
        os.mkdir(result_dir)
        continue
    else:
        # запускаем программу:
        print('---Start program')
        # вызываем программу magick.exe из текущей рабочей директории
        process = subprocess.run(os.path.join(current_dir, 'magick.exe') + ' convert ' + file + ' -resize 200 ' + os.path.splitext(file)[0] + '_output.jpg')
        # перемещаем созданныйй файл из папки Source, в которой он создастся в папку Result
        shutil.move(os.path.join(source_path, os.path.splitext(file)[0] + '_output.jpg'), os.path.join(result_dir, os.path.splitext(file)[0] + '_output.jpg'))
        print('-----------------------------')
        print('args->', process.args)
        print('stdout->', process.stdout)
        print('stderr->', process.stderr)
        print('returncode->', process.returncode)
        print('---End program')
        print('-----------------------------')