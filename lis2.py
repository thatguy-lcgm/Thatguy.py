data = []
temp = []
heavy = light = 0
while True:
    temp.append(input(f'Enter the {len(data) + 1}º person name: ').strip().title())
    temp.append(float(input(f'Enter the {len(data) + 1}º person weight: ')))
    if heavy == light == 0:
        heavy = light = temp[1]
    else:
        if temp[1] > heavy:
            heavy = temp[1]
        if temp[1] < light:
            light = temp[1]
    data.append(temp[:])
    temp.clear()
    co = input('would you like to continue(1: YES|2: NO): ')
    while co != '1' and co != '2':
        print('\033[31mIt appears that you have not entered the right value.\033[m')
        co = input('would you like to continue(1: YES|2: NO): ')
    if co == '2':
        break
print(f'The heaviest weight was {heavy}: ', end='')
for c in data:
    if c[1] == heavy:
        print(c[0], end=' ')
print()
print(f'The lightest weight was {light}: ', end='')
for c in data:
    if c[1] == light:
        print(c[0], end=' ')
