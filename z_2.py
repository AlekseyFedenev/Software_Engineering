import random
def main():
    result = random.randint(1,6)
    print("Выпало: ", result)

    if result == 5 or result == 6:
        print("Вы победили!!!")
    elif result == 3 or result == 4:
        print("Повторите")
        main()
    else:
        print("К сожалению, Вы проиграли")

if __name__ == '__main__':
    main()