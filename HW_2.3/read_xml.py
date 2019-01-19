from xml.etree import ElementTree as ET

tree = ET.parse('GodFather.xml')
print('tree', tree)
director = tree.find('Director')
print('director.text', director.text)  # при помощи "text" обращаемся к тексту, содержащийся внутри тега "Director"
# ищем актеров внутри тега MainCharacters. Тег tree может быть использован только для поиска по дереву.
# Вложенные теги он не видит
mc = tree.find('MainCharacters')
characters = mc.findall('MainCharacter')
print('characters',characters)  # выдаст следующее:
# сейчасбудем уже перечислять всех актеров внутри тега "MainCharacters"
for character in characters:
    print('character.attrib', character.attrib)  # тег attrib выводит значение атрибутов тега



