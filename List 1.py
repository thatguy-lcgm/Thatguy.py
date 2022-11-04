#Studying lists
#in this scenario the user will have to enter 5 values and the program should return the list, the...
#highest number entered by the user with its position inside a list and the lowest number as well  
lis = list()
highest = lowest = 0
for c in range(5):
    lis.append(int(input(f'Digit a {c}º value: ')))
print(f'Your list: {lis}')
for c in lis:
    if highest == lowest == 0:
        lowest = highest = c
    if c < lowest:
        lowest = c
    if c > highest:
        highest = c
print(f'The lowest value is: {lowest}, located in the Position: ')
for position, c in enumerate(lis):
    if c == lowest:
        print(position, end=' ')
print(f'\nThe highest value was {highest}, located in position: ')
for position, c in enumerate(lis):
    if c == highest:
        print(position, end=' ')
print('\n\033[31mEND.\033[m')
