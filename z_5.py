def count_words_in_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            print(f"The file '{file_name}' contains {num_words} words.")
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")


file_name = 'input.txt'
count_words_in_file(file_name)