def get_shop_list_by_dish(dishes, person_count):
    with open("cook_book.txt", encoding="utf-8") as text:
        recipe_book = dict()
        ingredient_list = list()
        shop_list = dict()
        ingredient_dict = dict()
        for row in text:
            if row != "\n":
                meal_row = row.strip()
                recipe_book[meal_row] = list()
                ingredient_count_row = text.readline().strip()
                i = 0
                while True:
                    i += 1
                    ingredient_row = text.readline().strip()
                    ingredient_list.append(ingredient_row)
                    for ingredient in ingredient_list:
                        dict_keys = ["ingredient_name", "quantity", "measure"]
                        ingredient_split = ingredient.split("|")
                        ingredient_dict = dict(zip(dict_keys, ingredient_split))
                    if i <= int(ingredient_count_row):
                        recipe_book[meal_row].append(ingredient_dict)
                        continue
                    else:
                        break
    for dish in dishes:
        for ingredients in recipe_book[dish]:
            new_shop_list_item = dict(ingredients)
            new_shop_list_item["quantity"] = int(new_shop_list_item["quantity"])
            new_shop_list_item["quantity"] *= person_count
            if new_shop_list_item["ingredient_name"] not in shop_list:
                shop_list[new_shop_list_item["ingredient_name"]] = new_shop_list_item
            else:
                shop_list[new_shop_list_item["ingredient_name"]]["quantity"] += new_shop_list_item["quantity"]
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print("{} {} {}".format(shop_list_item["ingredient_name"], shop_list_item["quantity"], shop_list_item["measure"]))


def create_shop_list():
    person_count = int(input("Введите количество человек: "))
    dishes = input("Введите блюда в рассчете на одного человека через запятую: ").split(",")
    shop_list = get_shop_list_by_dish(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()

