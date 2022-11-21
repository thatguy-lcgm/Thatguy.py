from time import sleep


def count(start1, end1, jump1):
    if start1 < end1:
        while start1 <= end1:
            print(start1, end=' ')
            sleep(0.4)
            start1 += jump1
        if start1 != end1:
            print(end1)
        print()
    elif start1 > end1:
        while start1 >= end1:
            print(start1, end=' ')
            sleep(0.4)
            start1 -= jump1
        if start1 != end1:
            print(end1)
    if jump1 == 0:
        jump1 = 1


print('-=' * 20)
print('counting from 1 to 10 in 1 by 1')
ini = 1
while ini <= 10:
    print(ini, end=' ')
    ini += 1
    sleep(0.4)
print()
print('-=' * 20)
print('Counting from 10 to 2 in 2 by 2')
ini = 10
while ini >= 0:
    print(ini, end=' ')
    ini -= 2
    sleep(0.4)
print()
print('-=' * 20)
print("Now it's your turn. . .")
count(start1=int(input('Enter the start: ')), end1=int(input('Enter the last value: ')),
      jump1=int(input('Enter the jump: ')))
