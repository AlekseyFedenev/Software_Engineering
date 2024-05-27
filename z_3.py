def two_numbers():
    try:  # Начало блока обработки исключений
        user_input = input("Введите число: ")
        number = float(user_input)  # Преобразование введенной строки в число типа float
        result = 2 + number  # Сложение 2 и введенного числа
        print(f"Результат сложения: {result}")

    except ValueError:  # Обработка исключения
        print("Неподходящий тип данных. Ожидалось число")

two_numbers()  #Вызов функции