import json

with open('data.json', 'w') as text:
    data = {
        'name': 'банан',
        'price': 30
    }
    json.dump(data, text, indent=2, ensure_ascii=False)  # сериализация записываемого файла
    some_text = json.dumps(data, indent=2, ensure_ascii=False)
    print(some_text)
