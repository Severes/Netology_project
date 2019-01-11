import chardet

with open('war-and-peace.txt', 'rb') as text:
    text2 = text.read()
    print(text2)
    result = chardet.detect(text2)
    print(result)
    text3 = text2.decode(result['encoding'])
    print(text2)
