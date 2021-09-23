def draw_library():
    #roof
    letter = '/'
    number = 16

    for i in range(0, number):
        print((letter).rjust(number-i, ' ') + (' '*i) + ('\\').rjust(i+1))
    #title
    print('LIBRARY'.center(31,'-'))
    print('|                             |')
    print('|                             |')
    #windows
    print('|        ----       ----      |')
    for i in range(3):
        print('|       |    |     |    |     |')
    
    print('|        ----       ----      |')
    for i in range(9):
        print('|                             |')
    #roof
    print('|          -----------        |')
    for i in range(5):
        print('|          |         |        |')
    print('-'*31)
    return

draw_library()
