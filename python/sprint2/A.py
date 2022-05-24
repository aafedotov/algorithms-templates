n = int(input())
m = int(input())

matrix = []
result = []

for i in range(0, n):
    matrix.append(list(map(int, input().split(' '))))

for i in range(0, m):
    row = []
    for j in range(0, n):
        row.append(matrix[j][i])
    result.append(row)

for i in range(0, m):
    to_print = ' '.join([str(char) for char in result[i]])
    print(to_print)
