#Using while to calculate the factorial:
n = int(input('Digit a number: '))
cont = n
factorial = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    factorial *= cont
    cont -= 1
print(factorial)
#Using range to calculate the factorial:
n = int(input('Digit a number: '))
factorial = 1
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    factorial *= c
print(factorial)
