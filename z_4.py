string = str(input('Введите предложение: '))
print('Длина предложения равна: ', len(string))
print('Предложение в нижнем регистре: ', string.lower())
count = 0
for i in range(len(string)):
    if string[i] in 'aeiou':
        count += 1
print('Количество гласных равно: ', count)
print('Заменить слова UNGLY на BEAUTY: ', string.replace('ugly', 'beauty'))
if string.startswith('The') & string.endswith('end'):
    print('Предложение начинается с THE и заканчивается на END')
else: print('Предложение не подходит под заданные условия')

