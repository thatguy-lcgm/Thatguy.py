#Multiplication table
num = int(input('Digit a number: '))
for m in range(1, 10):
    print('{} X {} = {}'.format(m, num, num * m))
