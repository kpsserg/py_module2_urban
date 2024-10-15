from xml.sax.handler import property_interning_dict

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
length_list = len(my_list)
for i in range(len(my_list)):
    if my_list[i] == 1:
        continue
    elif my_list[i] == 2:
        primes.append(my_list[i])
        continue

    for j in range(1, i):
        a = my_list[i]
        b = my_list[j]
        # print('Сравниваем ', a, 'и', b)
        res = a % b
        # print('Остаток от деления равен', res)
        if not res:
            not_primes.append(a)
            break
        elif j == i - 1:
            primes.append(a)

print('Primes:', primes)
print('Not primes', not_primes)
#