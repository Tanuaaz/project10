'''This program helps to make shopping list'''
import ru_local

#making the shopping list dictionary
shopping_basket = {}
print(ru_local.OPTION)

option = int(input(ru_local.MENU))


while option != 0:
    if option == 1: #checking menu
        item = input(ru_local.ITEM)

        if item in shopping_basket: #checking if item already in bakset
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