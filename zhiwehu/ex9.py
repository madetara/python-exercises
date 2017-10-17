lines = []

while True:
    line = input()
    if not line:
        break
    else:
        lines.append(line)

for line in lines:
    print(line.upper())
