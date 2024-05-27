# Software_Engineering
#Базовые операции языка Python
Отчет по Теме выполнил:
- Феденёв Алексей Сергеевич
- ИНО ОЗБ ПОАС-22-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + | 
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили: Панов Михаил Александрович
(и.о. заведующего кафедрой информационных технологий и статистики,
кандидат экономических наук, доцент.)

## Самостоятельная работа №8
## Задание 1.
###  Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях.

```python
class Smartphone: # определение класса
    def __init__(self, make, model): 
        self._make = make 
        self.__model = model 
my_phone = Smartphone('Reale', 'C5')
```
### Результат
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema8/pic/tema81.png)
### Вывод: с помощью класса и его объектов удобно создавать и хранить данные, связанные с определенным типов объектов.

## Задание 2.
###   Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях.

```python
class Smartphone: # определение класса
    def __init__(self, make, model): 
        self._make = make 
        self.__model = model
    def write(self):
        print(f'У меня телефон марки {self.make}, а модель {self._model} )


my_phone = Smartphone('Reale', 'C5')
my_phone.write()
```
### Результат
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema8/pic/tema82.png)
### Вывод: с помощью атрибутов и методов класса можно получать и хранить данные, связанные с каждым отдельным объектом. А также изменять значения атрибутов для конкретных объектов

## Задание 3.
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях.

```python
class Smartphone: # определение класса
    def __init__(self, make, model): 
        self._make = make 
        self.__model = model
    def write(self):
        print(f'У меня телефон марки {self.make}, а модель {self._model} )


my_phone = Smartphone('Realme', 'C5')
my_phone.write()

class FlagPhone(Smartphone): #определение класса FlagPhone, который наследуется от Smartphone
    def __init__(self, make, model, memory): #метод инициализации с параметрами
        super().__init__(make, model) #вызов метода инициализация родительского класса
        self.memory = memory #инициализация атрибута

    def write(self):
        print(f'У меня флагманский телефон марки {self.get_make()}, модель {self._Smartphone__model} и память {self.memory} Gb') #вывод строчки

my_flag_phone = FlagPhone('Xiaomi', 'Poco X6', '12/512')
my_flag_phone.write()
```
### Результат
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema8/pic/tema83.png)
### Вывод: с помощью наследования можно создавать специальные классы, которые наследуют атрибуты и методы родительского класса, при этом позволяя добавлять новый функционал и изменять существующие методы.

## Задание 4.
###  Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях

```python
class Smartphone: # определение класса
    def __init__(self, make, model): 
        self._make = make 
        self.__model = model

    def write(self):
        print(f'У меня телефон марки {self.make}, а модель {self._model} )

my_phone = Smartphone('Realme', 'C5')
my_phone.write()


class FlagPhone(Smartphone): #определение класса FlagPhone, который наследуется от Smartphone
    def __init__(self, make, model, memory): #метод инициализации с параметрами
        super().__init__(make, model) #вызов метода инициализация родительского класса
        self.memory = memory #инициализация атрибута

    def write(self):
        print(f'У меня флагманский телефон марки {self.get_make()}, модель {self._Smartphone__model} и память {self.memory} Gb') #вывод строчки

my_flag_phone = FlagPhone('Xiaomi', 'Poco X6', '12/512')
my_flag_phone.write()
```
### Результат
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema8/pic/tema84.png)
### Вывод: с защищенными атрибутами( _ ) можно работать только внутри класса, приватные атрибуты (_ _) предназначены для ограничения доступа и предотвращения изменения значения извне класса
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema8/pic/tema841.png)
### Вывод: с помощью инкапсуляции можно обеспечить защиту данных так, что придется полностью переписывать программу, для того, чтобы все заработало как прежде

## Задание 5.
###  Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях.

```python
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
```
### Результат
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema8/pic/tema85.png)
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema8/pic/tema851.png)
### Вывод: с помощью полиморфизма можно использовать один и тот же метод для разных типов объекта, не зависимо от их конкретной реализации или класса. 
