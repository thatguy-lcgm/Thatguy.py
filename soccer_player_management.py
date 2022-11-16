players = dict()
data = []
while True:
    players['name'] = input(f'{len(data) + 1}º player name: ').title().strip()
    players['matches'] = int(input('Enter the amount of matches: '))
    players['goals'] = []
    for c in range(players['matches']):
        players['goals'].append(int(input(f'Enter the amount of goals for the {c + 1} match: ')))
    players['total'] = sum(players['goals'])
    data.append(players.copy())
    co = int(input('Would you like to continue?(1: YES|2: NO) '))
    while co != 1 and co != 2:
        print('\033[31mIt appears that you have entered the wrong value.\033[m')
        co = int(input('Would you like to continue?(1: YES|2: YES) '))
    if co == 2:
        break
print('-=' * 50)
print('cod ', end='')
for i in players.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 55)
for k, v in enumerate(data):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
print()
while co != 999:
    print('-' * 55)
    co = int(input('which player would you like to extract more details?(999 to stop.) '))
    while co > len(data) and co != 999:
        print(f'\033[31mPlayer not in list, enter the player cod (0~{len(data)}) or (999) to stop.')
        co = int(input('\033[37mplayer cod: \033[m'))
    if co == 999:
        break
    else:
        for c in range(len(data[co]['goals'])):
            print(f'{c + 1} match player {data[co]["name"]} scored: {data[co]["goals"][c]}')
print()
print('\033[31mEND.')
