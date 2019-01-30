import os

print(__file__)

print(os.path.abspath(__file__))
print(os.path.abspath('abrakadabra'))  # abspath также не делает проверок на существование пути
