def add_expense(amount):
    with open('book.txt', mode='a', encoding='utf-8') as file:
        file.write(f"{amount}\n")

while True:
    amount_input = input("Введите сумму расхода или 'q' для выхода: ")
    if amount_input.lower() == 'q':
        break
    amount = float(amount_input)
    add_expense(amount)