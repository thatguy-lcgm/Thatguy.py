def fun():
    from time import sleep
    print('\033[1:29:42m~' * 35)
    print(f'{"SYSTEM OF HELP PyHELP":^35}')
    print('~' * 35)
    while True:
        t = input('\033[mFunction or library > ').lower()
        if t == 'end':
            break
        print('\033[46m~' * 45)
        print(f"{f'Looking in the manual for command {t}':^45}")
        print('\033[46m~' * 45)
        sleep(0.5)
        print('\033[7m')
        help(t)
    print('\033[41m~' * 10)
    print(f'{"END.":^10}')
    print('~' * 10)


fun()
