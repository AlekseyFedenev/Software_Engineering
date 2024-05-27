class Smartphone: # определение класса
    def __init__(self, make, model): # определение метода инициализации с параметрами
        self.make = make #инициализация атрибута
        self.model = model #инициализация атрибута

    def write(self):
        print(f'У меня телефон марки {self.make}, модель {self.model}')

class FlagPhone(Smartphone): #определение класса FlagPhone, который наследуется от Smartphone
    def __init__(self, make, model, memory): #метод инициализации с параметрами
        super().__init__(make, model) #вызов метода инициализация родительского класса
        self.memory = memory #инициализация атрибута
    def write(self):
        print(f'У меня флагманский телефон марки {self.make}, модель {self.model} и память {self.memory} Gb') #вывод строчки

class Tablet:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def write(self):
        print(f'У меня планшет марки {self.make}, модель {self.model}')

def describe_device(device):
    device.write()

my_smartphone = Smartphone('Realme', 'C5')
my_flag_phone = FlagPhone('Xiaomi', 'Poco X6', '12/512')
my_tablet = Tablet('Apple', 'iPad Air')

describe_device(my_smartphone)
describe_device(my_flag_phone)
describe_device(my_tablet)
