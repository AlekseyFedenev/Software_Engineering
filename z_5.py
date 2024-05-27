class DivisionError(Exception): #определение класса
    def __init__(self, number, divisor): #метод инициализация
        self.message = f"Число {number} не делится на {divisor}" #сообщение об ошибке
        super().__init__(self.message) #вызов конструктора класса Exception

def divide_number(number, divisor): #метод игициализации
    if number % divisor != 0: #проверяем, делится ли число без остатка
        raise DivisionError(number, divisor) #если нет, то исключение
    return number / divisor #иначе результат

try:
    result = divide_number(10, 5) #выполняем деление
    print(f"Результат деления: {result}") #выводим результат, если успешно
except DivisionError as e:  #исключение
    print(f"Ошибка деления: {e.message}") #выводим об ошибке
