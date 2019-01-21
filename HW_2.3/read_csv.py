import csv

# чтение файла построчно, списком
with open('sample_csv.csv') as text:
    reader = csv.reader(text, delimiter=';')
    for row in reader:
        print(row[2])

# чтение файла построчно, словарем
with open('sample_csv.csv') as text2:
    reader = csv.DictReader(text2, delimiter=';')
    for row in reader:
        print(int(row['Square']) + 10)  # выводится через OrderDict, чтобы задать порядок вывода. необходимо обозначать
        # тип данных, так как в csv тип данных неопределен

