def check_file(file_name):
    try: #начала блока обработки исключений
        with open(file_name, 'r') as file: #открытие файла для чтения
            contents = file.read() #чтение содержимого файла
            if not contents:  # Если файл пустой
                raise Exception("Файл пустой")
            else:  # Если в файле есть информация
                print(contents)
    except FileNotFoundError: #обработка исключения
        print("Файл не найден")
    except Exception as e: #обработка исключения
        print(e)

# Проверка пустого файла
print("Содержимое не пустого файла:")
check_file('one')

# Проверка непустого файла
print("\nСодержимое пустого файла:")
check_file('two')