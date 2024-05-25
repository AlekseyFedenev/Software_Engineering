def menu (tup, element):
    if element in tup:
        index = tup.index(element) #вход первого элемента
        new_tup = tup[:index] + tup[index+1:] #новый кортеж, без первого жлемента
        return new_tup
    else:
        return tup

tuple = ((1, 2, 3) , 1)
result_tuple = menu(tuple[0], tuple[1])
print(result_tuple)