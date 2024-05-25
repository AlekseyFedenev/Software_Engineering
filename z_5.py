def sum_positive_numbers(numbers):
    total_sum = 0

    for number in numbers:
        if number > 0:
            total_sum += number

    return total_sum

number_list = [5, -3, 10, -2, 7, -1, 8]

print(f"Сумма всех положительных чисел: {sum_positive_numbers(number_list)}")