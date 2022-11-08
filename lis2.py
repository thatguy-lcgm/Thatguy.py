persons = []
data = []
p_count = 1
heavy = light = 0
heavy_list = []
light_list = []
while True:
    data.append(input(f'Enter {p_count}º person name: ').strip().title())
    data.append(float(input(f'Enter the {p_count}º person weight: ')))
    persons.append(data[:])
    data.clear()
    co = int(input('Would you like to continue?(1: YES|2: NO) '))
    while co != 1 and co != 2:
        print('\033[31mYou did not enter the right choice, try again.\033[m')
        co = int(input('Would you like to continue?(1: YES|2: NO) '))
    if co == 2:
        break
    p_count += 1
for c in persons:
    if heavy == 0 and light == 0:
        heavy = light = c[1]
        data.append(c[0])
    else:
        if c[1] > heavy:
            heavy = c[1]
            data.append(c[0])
            heavy_list.clear()
        elif c[1] == heavy:
            data.append(c[0])
    heavy_list.append(data[:])
    data.clear()
for c in persons:
    if c[1] < light:
        light_list.clear()
        data.append(c[0])
        light = c[1]
    if c[1] == light:
        data.append(c[0])
    light_list.append(data[:])
    data.clear()
print(f'the person with the highest weight was: {heavy_list} with {heavy} KG')
print(f'The person with the lightest weight was: {light_list} with {light} KG')
print(f'{p_count} persons were entered')
