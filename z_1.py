def fib(n):
    a, b = 0, 1  # присваиваем значения
    count = 0
    with open('fib', 'w') as file:
        while count < n:
            file.write(str(a) + '\n')
            yield a  # возвращаем число Фибоначчи
            a, b = b, a + b  # генерируем число Фибоначчи
            count += 1  # +1

for num in fib(200):  #вызов функции
   print(num)  # Выводим число Фибоначчи