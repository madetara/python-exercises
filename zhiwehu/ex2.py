input_list = list(map(int, input().split()))
results =[]

fact = lambda x: 1 if x == 0 else x * fact(x - 1)

for x in input_list:
    results.append(str(fact(x)))

print(', '.join(results))
