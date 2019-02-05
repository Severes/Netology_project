text = 'alieruigawubhefpbnewivjwbndivbwiuebvpwjainbdvjwaidbvijsabdv'
# print(type(len(text)))


text_list = list()
x = 0
y = 0
while len(''.join(text_list)) < len(text):
    y = x + 10
    text_list.append(text[x:y])
    x += 10
    print(len(''.join(text_list)))