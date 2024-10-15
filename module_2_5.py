def get_matrix(n, m, value):
    matrix = []
    for i in range(0, n):
        list_ = []
        for j in range(0, m):
            list_.append(value)
        matrix.append(list_)
    return matrix

result1 = get_matrix(2, 2, 10)
print(result1)
result2 = get_matrix(3, 5, 42)
print(result2)
result3 = get_matrix(4, 2, 13)
print(result3)