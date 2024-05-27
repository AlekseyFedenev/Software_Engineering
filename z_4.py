class Rectangle: #определение класса
    def __init__(self, a, b): #метод инициализации
        self.a = a #инициализзация атрибута
        self.b = b #инициализация атрибута

    @property #декоратор
    def area(self): #метод для вычисления площади
        return self.a * self.b #результат умножения

rect = Rectangle(15, 5) #создание объекта класса Rectangle с параметрами
print(rect.area) #вывод на экран значения