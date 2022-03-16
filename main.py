def get_ingridients(i):
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
        ingr_dict['ingridient_name'] = ingr_part[0]
        ingr_dict['quantity'] = int(ingr_part[1])
        ingr_dict['measure'] = ingr_part[2]
        new_list_ingr.append(ingr_dict)
    return new_list_ingr


if __name__ == '__main__':
    cook_book = {}
    with open("1.txt", encoding='utf-8' ) as file:
        list = file.readlines()
        # print(list)
        next_recipe = 0
        while next_recipe != "END":
            # get_ingr(get_ingridients(next_recipe))
            cook_book[list[next_recipe].rstrip("\n")] = get_ingr(get_ingridients(next_recipe))
            print(cook_book)
            try:
                next_recipe = list.index("\n", next_recipe) + 1
            except ValueError:
                next_recipe = "END"
                # print("END")
            # next_recipe = list.index("\n",next_recipe)
            print(next_recipe)








