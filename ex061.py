d = 1
while d != 5:
    print('''\033[34mFunctions:
[ 1 ] Addition
[ 2 ] Subtraction
[ 3 ] Multiplication
[ 4 ] Division
[ 5 ] Exit''')
    d = int(input('Select a function: \033[m'))
    if d != 5:
        n1 = int(input('Digit the first number: '))
        n2 = int(input('Digit the second number: '))
        if d == 1:
            print('{} + {} = {}'.format(n1, n2, n1 + n2))
        elif d == 2:
            print('{} - {} = {}'.format(n1, n2, n1 - n2))
        elif d == 3:
            print('{} X {} = {}'.format(n1, n2, n1 * n2))
        elif d == 4:
            print('{} / {} = {}'.format(n1, n2, n1 / n2))
print('\033[31mEND.\033[m')
