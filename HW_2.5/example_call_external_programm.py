import subprocess


print('---Start programm')
# вызвав данную программу в cmd, мы выполним то, что указано ниже в мараметре .run
process = subprocess.run('python example_args.py') #, stdout=subprocess.PIPE)
print('-----------------------------')
print('args->', process.args)
print('stdout->', process.stdout) # чтобы строка 6 возвращала данные в корректной кодировке, нужно
# поколдовать с данной строкой. Может прописать параметр read?
print('stderr->', process.stderr)
print('returncode->', process.returncode)

print('---End programm')
