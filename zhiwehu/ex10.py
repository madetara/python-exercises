sentence = input().split()
result = []

for word in sentence:
    if not word in result:
        result.append(word)

print(' '.join(sorted(result)))
