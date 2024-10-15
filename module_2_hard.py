def determine_counter(i):
    if i % 2:
        counter = round(i / 2) + 1
    else:
        counter = round(i / 2) # Привели к типу int() c помощью round()
    return counter

# Функция определяет код:
def variations(i, n):
    global result
    # Верхняя/нижняя граница цикла For
    up_border = n - i + 1
    down_border = i + 1
    #Сам цикл for
    for j in range(down_border, up_border):
        variant = i + j
        if n % variant:
            continue
        else:
            result = result + str(i) + str(j)

n = int(input("Введите число от 3 до 20: "))
counter = determine_counter(n)
#print(counter)
result = ''
for i in range(1, counter):
    variations(i, n)
print(f'Пароль к числу {n} - {result} \n')

n = int(input("А теперь введите свой год рождения: "))
counter = determine_counter(n)
result = ''
for i in range(1, counter):
    variations(i, n)
print(f'Пароль к Вашему году рождения {n} - {result}')
