my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i <= len(my_list):
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] < 0:
        break
    i += 1
print('\n')

# Вариант 2
# Мне он:
# а) не нравится тем, что i += 1 в цикле встречается дважды
# б) нравится тем, что в if идут жесткие проверки на выполнение всех условий <, =, >
i = 0
while i <= len(my_list):
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] == 0: # Нравится доп. проверка
        i += 1 # Не нравится
        continue
    elif my_list[i] < 0:
        break
    i += 1