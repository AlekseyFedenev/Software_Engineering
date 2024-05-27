class Smartphone: # определение класса
    def __init__(self, make, model): # определение метода инициализации с параметрами
        self._make = make #инициализация защищенного атрибута
        self.__model = model #инициализация приватного атрибута

    def get_make(self): #определение метода
        return self._make #возвращает знаечние атрибута


class FlagPhone(Smartphone): #определение класса FlagPhone, который наследуется от Smartphone
    def __init__(self, make, model, memory): #метод инициализации с параметрами
        super().__init__(make, model) #вызов метода инициализация родительского класса
        self.memory = memory #инициализация атрибута

    def write(self):
        print(f'У меня флагманский телефон марки {self.get_make()}, модель {self._Smartphone__model} и память {self.memory} Gb') #вывод строчки

my_flag_phone = FlagPhone('Xiaomi', 'Poco X6', '12/512')
my_flag_phone.write()

