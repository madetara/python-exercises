(x, y) = map(int, input().split(','))

result = [[0 for i in range(y)] for j in range(x)]

for i in range(x):
    for j in range(y):
        result[i][j] = i * j

print(result)
