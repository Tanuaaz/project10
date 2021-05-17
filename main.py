import ru_local

shopping_basket = {}
print(ru_local.OPTION)

option = int(input(ru_local.MENU))

while option != 0:
    if option == 1:
        item = input(ru_local.ITEM)

        if item in shopping_basket:
            print(ru_local.ALREADY)
            count = int(input(ru_local.COUNT))
            shopping_basket[item] = shopping_basket[item] + count
        else:
            count = int(input(ru_local.COUNT))
            shopping_basket[item] = count

    elif option == 2:
        item = input(ru_local.ITEM)
        del(shopping_basket[item])

    elif option == 3:
        for item in shopping_basket:
            print(item, ':', shopping_basket[item])

    elif option != 0:
        print(ru_local.NOT)

    option = int(input(ru_local.MENU))

else:
    print(ru_local.CLOSE)