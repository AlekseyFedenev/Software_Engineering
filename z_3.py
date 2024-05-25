def count_digits(string):
    counts = {}
    for char in string:
        if char.isdigit():
            number = int(char)
            counts[number] = counts.get(number, 0) + 1

    sorted_counts = sorted(counts.items())
    top_three = dict(sorted_counts[:3])

    return top_three

input_string = input('Введите строку из цифр (минимум 15 символов): ')
while len(input_string) < 15:
    print('Ошибка: введите строку минимум из 15 цифр!')
    input_string = input('Введите строку из цифр (минимум 15 символов): ')

result_dict = count_digits(input_string)
print(result_dict)