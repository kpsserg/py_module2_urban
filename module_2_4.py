my_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 23, 24]
primes = []
not_primes = []

for i in range(1,len(my_list)):
    if my_list[i] == 2:
        primes.append(my_list[i])
    elif my_list[i] == 1:
        continue
    else:
        for j in range(2, my_list[i]): #Начинаем проверку числа является оно простым или нет
            if my_list[i]%j:
                if j == my_list[i]-1:
                    primes.append(my_list[i])
            else:
                not_primes.append(my_list[i])
                break

print('Primes:', primes)
print('Not primes', not_primes)
#

#Задача для чисел от 1 до 100

primes = []
not_primes = []

for i in range(1, 101):
    if i == 2:
        primes.append(i)
    elif i == 1:
        continue
    else:
        for j in range(2, i): #Начинаем проверку числа является оно простым или нет
            if i%j:
                if j == i-1:
                    primes.append(i)
            else:
                not_primes.append(i)
                break

print('Primes:', primes)
print('Not primes', not_primes)