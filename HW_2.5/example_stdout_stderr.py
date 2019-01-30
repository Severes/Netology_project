import sys

print('Это stdout', file=sys.stdout)
print('Это stderr', file=sys.stderr)

with open('log.txt', mode='a') as text:
    # данный print не выведется в нашем скрипте, а направится в файл log.txt и запишет выводимый текст
    # в созданный файл
    print('This is text in file "log.txt"', file=text)
