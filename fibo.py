a1 = 1
a2 = 1
a3 = 1

n = 9

for _ in range(n - 3):
    print(_)
    print(f'Предыдущие значения: a1 = {a1}, a2 = {a2}, a3 = {a3}')
    a1, a2, a3 = a3, a1, a1 +a2 +a3
    print(f'Новые значения: a1 = {a1}, a2 = {a2}, a3 = {a3} \n')
print(a3)