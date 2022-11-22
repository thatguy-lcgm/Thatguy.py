def higher():
    from time import sleep
    numbers = list()
    while True:
        while True:
            number = input('Enter a value: ')
            if len(number) >= 1:
                numbers.append(int(number))
            co = input('Would you like to continue with the numbers?(1: YES|2: NO) ')
            while co != '1' and co != '2':
                print('\033[31mThe value must be "1" or "2".\033[m')
                co = input('Would you like to continue with the numbers?(1: YES|2: NO) ')
            if co == '2':
                break
        high = 0
        values = 0
        print('-=' * 30)
        if len(numbers) > 0:
            for c in numbers:
                values += 1
                sleep(0.5)
                print(c, end=' ')
                if c > high:
                    high = c
            print()
            sleep(0.5)
            print(f'The highest value was {high}')
            sleep(0.5)
            print(f'{values} values were entered.')
        else:
            sleep(0.5)
            print('0 values were entered.')
        print('-=' * 30)
        sleep(0.5)
        co = input('\033[33mWould you like to continue the function?(1: YES|2: NO) \033[m')
        while co != '1' and co != '2':
            print('\033[31mThe value must be "1" or "2".\033[m')
            co = input('Would you like to continue?(1: YES|2: NO) ')
        if co == '2':
            break
        numbers.clear()
    print('\033[31mEND.\033[m')


higher()
