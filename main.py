def get_ingridients(i, list):
    ingr_list = []
    for ingr in range(int(list[i + 1].rstrip("\n"))):
        ingr_list.append(list[i + 2 + ingr].rstrip("\n"))
        # print(ingr_list)
    return ingr_list

def get_ingr(list):
    new_list_ingr = []
    for ingr in list:
        ingr_dict = {}
        ingr_part = ingr.split("|")
        ingr_dict['ingredient_name'] = ingr_part[0]
        ingr_dict['quantity'] = int(ingr_part[1])
        ingr_dict['measure'] = ingr_part[2]
        new_list_ingr.append(ingr_dict)
    return new_list_ingr

def create_cook_book():
    cook_book = {}
    with open("1.txt", encoding='utf-8') as file:
        list = file.readlines()
        # print(list)
        next_recipe = 0
        while next_recipe != "END":
            # get_ingr(get_ingridients(next_recipe))
            cook_book[list[next_recipe].rstrip("\n")] = get_ingr(get_ingridients(next_recipe, list))
            # print(cook_book)
            try:
                next_recipe = list.index("\n", next_recipe) + 1
            except ValueError:
                next_recipe = "END"
                # print("END")
            # next_recipe = list.index("\n",next_recipe)
            # print(next_recipe)
    # print(cook_book)
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book()
    shop_list = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            if ingr['ingredient_name'] not in shop_list:
                shop_list[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': person_count * ingr['quantity']}
            else:
                quantity = shop_list[ingr['ingredient_name']]['quantity']
                # print(shop_list[ingr['ingredient_name']]['quantity'])
                shop_list[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': (person_count * ingr['quantity'] + quantity)}
    return shop_list

if __name__ == '__main__':
    # print(create_cook_book())
    zakaz = ['Запеченный картофель', 'Омлет']
    print(get_shop_list_by_dishes(zakaz, 2))










