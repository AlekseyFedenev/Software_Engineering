from z5 import s_triangle

def main():
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))

    s = s_triangle(a,b,c)

    print('Площадь треугольника равна = ', s)

if __name__ == "__main__":
    main()