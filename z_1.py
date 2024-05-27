import time
def e_time(function):
    def wrapper():
        start_time = time.time() #время начала выполнения функции
        function() #запускаем функцию
        end_time = time.time() #время окончания выполнения функции
        result = end_time - start_time #время выполнения
        print(f'Время выполнения функции: {result} секунд')
    return wrapper()

@e_time #декоратор
def fibonacci():
    fib1 = fib2 = 1

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end='')

if __name__ == '__main__':
    fibonacci()