while True:
    try:
        a = int(input('First number: '))
        b = int(input('Second number: '))
        print(a + b)

    except ValueError:
        print('Input error')

    else:
        break