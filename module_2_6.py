def draw_area(): #прорисовываем поле для игры
    for i in area:
        print(*i)
    print()

def is_win(): #ищем победителя
    #str = area[0] + area[1] + area[2]
    if area[0][0] == area[0][1] == area[0][2] == ('X' or 'O') or area[0][0] == area[1][1] == area[2][2] == (
            'X' or 'O') or area[0][0] == area[1][0] == area[2][0] == ('X' or 'O'):
        print(f'Победили {area[0][0]}')
        return 1 #return area[0][0]
    elif area[1][0] == area[1][1] == area[1][2] == ('X' or 'O') or area[0][1] == area[1][1] == area[2][1] == (
            'X' or 'O') or area[0][2] == area[1][1] == area[2][0] == ('X' or 'O'):
        print(f'Победили {area[1][1]}')
        return 1 #return area[1][1]
    elif area[0][2] == area[1][2] == area[2][2] == ('X' or 'O') or area[2][0] == area[2][1] == area[2][2] == (
            'X' or 'O'):
        print(f'Победили {area[2][2]}')
        return 1 #return area[2][2]
    else:
        return 0

def step_func(n): #кому принадлежит код + запись хода
    print(f'Ход №{n}')
    if n % 2 == 0:
        print('Ходят нолики')
        step_char = 'O'
    else:
        print('Ходят крестики')
        step_char = 'X'
    row = int(input('Введите номер строки: 1, 2, 3 ')) - 1
    column = int(input('Введите номер столбца: 1, 2, 3 ')) - 1
    if area[row][column] == '*':
        area[row][column] = step_char
    else:
        print(f'Вы пропускаете ход, т.к. ячейка уже занята {area[row][column]}')
    draw_area()
    global step #МОЖНО ОБОЙТИСЬ БЕЗ ГЛОБАЛЬНЫХ ПЕРЕМЕННЫХ?
    step += 1 #МОЖНО ОБОЙТИСЬ БЕЗ ГЛОБАЛЬНЫХ ПЕРЕМЕННЫХ?

def stars_count():
    str = area[0] + area[1] + area[2]
    return str.count('*')

area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
greeting = 'Добро пожаловать в игру Крестики/нолики'
print(greeting)
print('-' * len(greeting))
draw_area()
step = 1

while stars_count(): #может нужно было выше объявить переменную stars чтобы не гонять ф-ю
    if stars_count() > 6: # опять гоняем ф-ю. Как улучшить код?
        step_func(step)
    elif not is_win():
        step_func(step)
    else:
        break
else:
    print('Игра закончена в ничью')


# while not is_win():
#     step_func(step)
#     if step > 9:
#         if is_nichya():
#             print('Игра закончена в ничью')
#             break

'''for step in range(1, 10):
    print(f'Ход №{step}')
    if step % 2 == 0:
        print(f'Ходят нолики')
        step_char = 'O'
    else:
        print(f'Ходят крестики')
        step_char = 'X'

    row = int(input('Введите номер строки: 1, 2, 3')) - 1
    column = int(input('Введите номер столбца: 1, 2, 3')) - 1
    if area[row][column] == '*':
        area[row][column] = step_char
    else:
        print(f'Вы пропускаете ход, т.к. ячейка уже занята {area[row][column]}')
    draw_area()
    if step>=5:
        if is_win():
            draw_area()
            print('Game over')
            break
        if step == n:
            print('Игра окончена в ничью')'''
