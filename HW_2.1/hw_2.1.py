cook_book = {
  'яйчница': [
    {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
  'стейк': [
    {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
    {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
  'салат': [
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
    {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
    ]
  }


def create_cook_book():
    with open("cook_book.txt", encoding="utf-8") as text:
        recipe_book = dict()
        ingredient_count = list()
        ingredient_list = list()
        for row in text:
            if row != "\n":
                meal_row = row.strip()
                recipe_book[meal_row] = []
                ingredient_count_row = text.readline().strip()
                ingredient_count.append(ingredient_count_row)
                i = 0
                while True:
                    i += 1
                    ingredient_row = text.readline().strip()
                    ingredient_list.append(ingredient_row)
                    if i < int(ingredient_count_row):
                        continue
                    else:
                        break
    print(cook_book)
    print(ingredient_count)
    print(ingredient_list)


create_cook_book()


# def get_shop_list_by_dishes(dishes, person_count):
#   shop_list = {}
#   for dish in dishes:
#     for ingridient in cook_book[dish]:
#       new_shop_list_item = dict(ingridient)
#
#       new_shop_list_item['quantity'] *= person_count
#       if new_shop_list_item['ingridient_name'] not in shop_list:
#         shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
#       else:
#         shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=
#           new_shop_list_item['quantity']
#   return shop_list
#
# def print_shop_list(shop_list):
#   for shop_list_item in shop_list.values():
#     print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
#                             shop_list_item['measure']))
#
# def create_shop_list():
#   person_count = int(input('Введите количество человек: '))
#   dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
#     .lower().split(', ')
#   shop_list = get_shop_list_by_dishes(dishes, person_count)
#   print_shop_list(shop_list)
#
# create_shop_list()

