import chardet

with open('war-and-peace.txt', 'rb') as text:
    print(text.read())
    result = chardet.decode(text.read())
    print(result)
