number = input('Введите последовательность чисел: ')

print('Список чисел: ', list(map(int, number.split())))
print('Котреж чисел: ', tuple(list(map(int, number.split()))))
