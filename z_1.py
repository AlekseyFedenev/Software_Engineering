class Tomato:
    states = ["отсутствует", "цветение", "зеленый", "красный"]  #создание статического сво-ва states, который содержит стадии созревания помидора

    def __init__(self, index): #определение метода инициализации с параметрами
        self._index = index  # инициализация защищенного атрибута
        self._state = self.states[0]  # инициализация защищенного атрибута, который принимает первое значение из списка states

    def grow(self): #определение метода инициализации
        state_index = self.states.index(self._state)  #узнаем индекс текущего состояния помидора
        if state_index < len(self.states) - 1:  #проверка, что индекс входит в рамки дозволенного
            self._state = self.states[state_index + 1]  #переводим помидор в следующую стадию созревания

    def is_ripe(self):
        return self._state == self.states[-1]  #проверка, что помидор находится на последней стадии созревания


class TomatoBush: #
    def __init__(self, count): #определение метода инициализации с параметрами
        self.tomatoes = []  #пустой список для хранения объектов класса Tomato
        for i in range(count):
            tomato = Tomato(i)  # создание объектов класса Tomato
            self.tomatoes.append(tomato)  #добавить каждый объект в список tomatoes

    def grow_all(self): #переводит ВСЕ объекты из списка на следующий этап
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self): #возвращает TRUE, если ВСЕ томаты из списка целые
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
        return True

    def give_away_all(self): #очищает весь список после сборки
        self.tomatoes.clear()

class Gardener:
    def __init__(self, name, plant): #определение метода инициализации с параметрами
        self.name = name  # Публичный атрибут для имени садовника
        self._plant = plant  # Защищенный атрибут для объекта класса TomatoBush

    def work(self): #заставляет садовника работать
        self._plant.grow_all()

    def harvest(self): #проверяет, все ле созрело
        if self._plant.all_are_ripe():
            print("Урожай созрел! Садовник убирает урожай.")
            self._plant.give_away_all()  # Убираем урожай
        else:
            print("Предупреждение: Не все плоды созрели")

    @staticmethod #статический метод
    def knowledge_base(): #справка по садоводству
        print("Справка по садоводству: не проветривать, не охлаждать, поливать раз в день")

Gardener.knowledge_base() #вывод справки по садовоству

tomato_bush = TomatoBush(8) #создание объекта класса TomatoBush
gardener = Gardener('Костя', tomato_bush) #создание объекта класса Gardener

gardener.work() #садовник работает, помидоры растут

gardener.harvest() # Сбор урожая

gardener.work() #садовник работает, помидоры растут
gardener.harvest()


gardener.work() # Сбор урожая после дозревания всех томатов
gardener.harvest()