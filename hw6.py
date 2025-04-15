def display_multiplication_table():
    for i in range(1, 10):
        for n in range(2, 6):
            if n != 5:
                print(f'{n} * {i} = {n * i:2d}', end = '  ')
            else :
                print(f'{n} * {i} = {n * i:2d}')
    print()

    for i in range(1, 10):
        for n in range(6, 10):
            if n != 9:
                print(f'{n} * {i} = {n * i:2d}', end = '  ')
            else :
                print(f'{n} * {i} = {n * i:2d}')

display_multiplication_table()
