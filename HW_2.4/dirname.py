import os

# возвращает сам исполняемый файл
print(__file__)
# возвращает имя директории
print(os.path.dirname(__file__))


print(os.path.dirname('/tmp/hello/'))  # вернет /tmp/hello
print(os.path.dirname('/tmp/hello'))  # вернет /tmp Разница потому, что dirname понмиает, что мы
# в hello не заходили
