import re

def censor(text, prohibited_words):
    word_list = re.findall(r'\b\w+\b', text)  # Using regular expression to find all words in the text
    result = ''
    for j in range(len(prohibited_words)):
        stars = '*' * len(prohibited_words[j])
        for i in range(len(word_list)):
            if word_list[i].lower() == prohibited_words[j].lower():  # Comparing words without considering the case
                word_list[i] = stars
    result = ' '.join(word_list)
    return result

if __name__ == '__main__':
    with open('input4.txt', 'r', encoding='utf-8') as file:
        prohibited_words = file.read().lower().split()

    extract = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"

    print(censor(extract, prohibited_words))