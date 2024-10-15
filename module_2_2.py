x = int(input('Введите чилсло 1: '))
y = int(input('Введите чилсло 2: '))
z = int(input('Введите чилсло 3: '))

if x == y and x == z:
    print('3')
    print('Все числа одинаковые')
elif x == y or y == z or x == z:
    print('2')
else:
    print('0')
