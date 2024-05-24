string = 'hello'
values = [0, 2, 4, 6, 8, 10]
counter = 0
while counter != 10:
    counter += 1
    if counter in values:
        print(string)
        print(string + ' world')

