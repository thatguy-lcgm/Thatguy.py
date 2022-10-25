from random import choice
from time import sleep
print('\033[35mWelcome!\033[m')
print('\033[34m=-=\033[m' * 20)
print('''\033[31m[ 1 ] ROCk
[ 2 ] SCISSORS
[ 3 ] PAPER\033[m''')
lis = [1, 2, 3]
x = int(input('\033[32mYour choice: \033[m'))
print('\033[34m=-=\033[m' * 20)
print('\033[34mPROCESSING. . .\033[m')
lis2 = choice(lis)
sleep(3)
#print(lis2)
if x == lis2:
    print('\033[32mYou got this!\033[m')
else:
    print('\033[31mTry again!\033[m')
if lis2 == 1:
    print('ROCK')
elif lis2 == 2:
    print('SCISSORS')
elif lis2 == 3:
    print('PAPER')