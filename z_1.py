from datetime import datetime #импорт класса datetime из модуля datetime
from math import sqrt #импорт класса sqrt из модуля math


def main(**kwargs): #определяет функцию main c именованными аргументами **kwargs (словарь)
    for key in kwargs.items(): #перебор элементов словаря
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) #вычмсление корня из суммы квадратов элементов
        print(result) #вывод результата на экран


if __name__ == '__main__': #обычный вызов функции, принимающей кортеж **kwargs, как параметр
    start_time = datetime.now() #импорт даты и времени в переменную start_time
    main( #вызывается функцция main с набором аргументов
        one=[10,3],
        two=[5,4],
        three=[15.13],
        four=[93,53],
        five=[133,15]
    )
   time_costs = datetime.now() - start_time #Вычесляется время выполнение программы
   print(f"Время выполнения программы - {time_costs}") #Выводится время выполнения программы