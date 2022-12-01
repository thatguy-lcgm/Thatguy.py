from time import sleep
#----------------------------------------FILE MANIPULATION----------------------------------------


def file_exist(value):
    try:
        a = open(value, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def file_create(value):
    try:
        a = open(value, 'wt+')
        a.close()
    except:
        print(f'\033[31mError! fail while trying to create file {value}\033[31m')
        sleep(5)
    else:
        print(f'\033[32mFile {value} created successfully!\033[m')


def file_add(value, name='unknown', age=0):
    try:
        a = open(value, 'at')
    except:
        print(f'\033[31mError while trying to add {name}\033[m')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print(f'\033[31mError while trying to save the information.\033[m')
        else:
            print(f'\033[32m{name} added successfully!\033[m')
    finally:
        a.close()


def read_file(value):
    try:
        a = open(value, 'rt')
        for line in a:
            line = line.split(';')
            line[1] = line[1].replace('\n', '')
            print(f'{line[0]:<30}{line[1]:>3} years')
    except:
        print(f'\033[31mError While opening {value}\033[m')


#----------------------------------------MENU DEFINITION----------------------------------------


def line():
    print('-' * 42)


def title2(msg):
    print('-' * 42)
    print(msg.center(42))
    print('-' * 42)


def menu(lis):
    line()
    c = 1
    for values in lis:
        print(f'\033[33m{c} - \033[34m{values}\033[m')
        c += 1
    line()


def read_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mError! only integer numbers are allowed.')
            continue
        else:
            return n


#----------------------------------------MAIN PROGRAM----------------------------------------
file = 'persons.txt'
if not file_exist(file):
    file_create(file)

while True:
    menu(['Inspect added persons', 'Add new person', 'Exit'])
    choice = read_int('\033[32mYour choice: \033[m')
    if choice == 1:
        title2('Persons added')
        read_file(file)
        sleep(2)
    elif choice == 2:
        name = input('Name: ')
        age = read_int('Age: ')
        file_add(file, name, age)
    elif choice == 3:
        print('\033[36mExiting. . .')
        sleep(1)
        break
    else:
        print('\033[31mError! choice must be from 1 to 3.\033[m')
