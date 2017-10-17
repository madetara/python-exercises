import math

(C, H) = (50, 30)

D = list(map(int, input().split(',')))

print(','.join(list(map(str, [round(math.sqrt(2 * C * x / H)) for x in D]))))
