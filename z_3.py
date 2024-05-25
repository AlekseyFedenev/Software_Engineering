def count_statistics(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        letter_count = sum(1 for char in text if char.isalpha())
        word_count = len(text.split())
        line_count = text.count('\n') + 1
        print(f"Input file contains:")
        print(f"{letter_count} letters")
        print(f"{word_count} words")
        print(f"{line_count} lines")

count_statistics('text3.txt')
