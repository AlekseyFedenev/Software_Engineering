# Software_Engineering
#Базовые операции языка Python
Отчет по Теме выполнил:
- Феденёв Алексей Сергеевич
- ИНО ОЗБ ПОАС-22-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + | 
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили: Панов Михаил Александрович
(и.о. заведующего кафедрой информационных технологий и статистики,
кандидат экономических наук, доцент.)

## Самостоятельная работа №7
## Задание 1.
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
#### Статья:
##### Клубника — ягода, без которой не обходится ни один садовый участок. Ее обожают абсолютно все: и взрослые, и дети. Но клубники почему-то каждый раз не хватает даже на то, чтобы сделать мало-мальский запас варенья. Как же быть, если хочется собрать большой урожай? Собрали советы от агронома Михаила Карпухина: Первым делом нужно посмотреть, как перезимовали прошлогодние кусты, и при необходимости посадить новые. У старых кустов мы убираем все отмершие листья, рыхлим землю и обязательно подкармливаем. Самое лучшее — использовать азотные удобрения. Они помогают сформироваться хорошей корневой системе: пока почва холодная, лучше всего подходит аммиачная селитра. По теплой почве очень хорошо идет мочевина из расчета 15–20 граммов на квадратный метр. И, чтобы не потерять азот, который есть в этих удобрениях, их нужно обязательно перемешать с землей. Можно подкормить гуминовыми препаратами. Подойдет «Фертика», «Растворин», «Юнона» — водорастворимые удобрения. И еще можно взять подкормку с микроэлементами. Земляника не является зимостойкой культурой, поэтому она время от времени умирает из-за морозов и засухи. Сейчас самое время сделать ремонтные посадки, заменить или заложить новую плантацию. Сделайте это — и на следующий год у вас будут ягоды. Пересаживать землянику каждый год с места на место не стоит. Через четыре года, как только куст отживет свое, просто убирайте его, срезав предварительно в
```python
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
```
### Результат
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema7/pic/tema71.png)

## Задание 2.
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль.

```python
def add_expense(amount):
    with open('book.txt', mode='a', encoding='utf-8') as file:
        file.write(f"{amount}\n")

while True:
    amount_input = input("Введите сумму расхода или 'q' для выхода: ")
    if amount_input.lower() == 'q':
        break
    amount = float(amount_input)
    add_expense(amount)
```
### Результат
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema7/pic/tema72.png)

## Задание 3.
### Имеется файл text3.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. 
### • Текст в файле:
#### Beautiful is better than ugly.
#### Explicit is better than implicit.
#### Simple is better than complex.
#### Complex is better than complicated.

```python
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
```
### Результат
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema7/pic/tema73.png)

## Задание 4.
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова.

```python
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
```
### Результат
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema7/pic/tema74.png)

## Задание 5.
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
#### Читает его содержимое, подсчитывает количество слов и выводит результат. Если файл не найден, программа выведет соответствующее сообщение.

```python
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
```
### Результат
![Меню](https://github.com/AlekseyFedenev/Software_Engineering/blob/Tema7/pic/tema75.png)
