one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def s_triangle(a,b,c): #формула Герона, для нахождения S треугольника
    p = (a+b+c) / 2
    return (p * (p - a) * (p-b) * (p-c)) ** 0.5

print('Площадь треугольника, составленного из max значений: ',
      s_triangle(max(one), max(two), max(three)))

print('Площадь треугольника, составленного из min значений: ',
      s_triangle(min(one), min(two), min(three)))
