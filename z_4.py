one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def sp_grades(grades):
    for i in range(len(grades)):
        if grades[i] == 2:
            grades[i] = None #удаляем эдемент, если равен 2
        elif grades[i] == 3:
            grades[i] = 4 #Если равен 3, то меняем на 4
    grades = [grade for grade in grades if grade is not None]
    return grades

print("one: ", sp_grades(one))
print("two: ", sp_grades(two))
print("three: ", sp_grades(three))


