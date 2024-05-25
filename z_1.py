from collections import Counter

def count_words(file_name):
    with open(file_name,encoding='utf-8', mode='r') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
        most_common_word = Counter(words).most_common(1)

    return word_count, most_common_word[0]

file_name = "input.txt"

total_words, most_common = count_words(file_name)
print(f"Общее количество слов в файле: {total_words}")
print(f"Самое часто встречающееся слово: '{most_common[0]}' (встречается {most_common[1]} раз)")

