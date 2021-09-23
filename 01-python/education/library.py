def draw_library():
    #roof
    letter = 'L'
    number = 16
    for i in range(0, number, 2):
        print((letter*i).rjust(number-1) + letter + (letter*i).ljust(number-1))
    print('LIBRARY'.center(31,'-'))
    for i in range(9):
        print('|                             |')

    print('|          -----------        |')
    for i in range(5):
        print('|          |         |        |')
    print('-'*31)
    return

draw_library()
