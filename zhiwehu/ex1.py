(l, r) = (2000, 3200)

list = [str(i) for i in range(l, r) if i % 7 == 0 and i % 5 != 0]

print(', '.join(list))
