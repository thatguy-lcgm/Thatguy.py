def half(value, show=False):
    res = value / 2
    if show:
        return currency(res)
    else:
        return res


def double(value, show=False):
    res = value * 2
    #return res if not show else currency(res)
    #return res if show is false else currency(res)
    if show:
        return currency(res)
    else:
        return res


def increase(value, s=0, show=False):
    res = value + (value / 100 * s)
    if show:
        return currency(res)
    else:
        return res


def decrease(value, s=0, show=False):
    res = value - (value / 100 * s)
    if show:
        return currency(res)
    else:
        return res


def currency(value):
    res = f'{"$"}{value:.2f}'.replace('.', ',')
    return res


def resume(value, inc=0, rec=0):
    print('-' * 39)
    print(F"RESUME OF THE VALUE".center(39))
    print('-' * 39)
    #print(f'Price entered:{currency(value): >30}')
    print(f'{"Price entered":.<26}{currency(value)}')
    print(f'{"Double of the price":.<26}{currency(double(value))}')
    if inc != 0:
        print(f'{f"{inc}% Increase":.<26}{currency(increase(value, inc))}')
    if rec != 0:
        print(f'{f"{rec}% Decrease":.<26}{currency(decrease(value, rec))}')
        #print(f'{rec}% Decrease: \t{currency(decrease(value, rec))}')
    print('-' * 39)

#ex 107
from currency import currency

num = float(input('Enter the value: $'))
print(f'The half of {num} is {currency.half(num)}')
print(f'The double of {num} is {currency.double(num)}')
print(f'Adding 10% in {num} we get {currency.increase(num, 10)}')
print(f'Taking 13% from {num} we get {currency.decrease(num, 13)}')

#ex108
from currency import currency

num = float(input('Enter a value: $'))
print(f'The double of {currency.currency(num)} is {currency.currency(currency.double(num))}')
print(f'The half of {currency.currency(num)} is {currency.currency(currency.half(num))}')
print(f'Adding 10% in {currency.currency(num)} we get {currency.currency(currency.increase(num, 10))}')
print(f'taking 13% off from {currency.currency(num)} we get {currency.currency(currency.decrease(num, 13))}')

#ex109
from currency import currency

num = float(input('Enter the value: $'))
print(f'The half of {currency.currency(num)} is {currency.half(num, True)}')
print(f'The double of {currency.currency(num)} is {currency.double(num, True)}')
print(f'Adding 10% we get {currency.increase(num, 10, True)}')
print(f'Taking 13% we get {currency.decrease(num, 13, True)}')

#ex110
from currency import currency

num = float(input('Enter a value: '))
currency.resume(num, 10, 13)

#ex111
from data111.CeV import currency

num = float(input('Enter a value: '))
currency.resume(num, 10, 13)

#ex112
from CeV.datas import ex112

ex112.read_money()
  #ex112.resume(int(input('Value: $')))
  #def read_money():
    #value = input('Enter a value: $').strip()
    #value_1 = value.replace(',', '')
    #value_1 = value_1.replace('.', '')
    #while not value_1.isnumeric():
        #print(f'\033[31m "{value}" is not a price.\033[m')
        #value = input('Enter a value: $').strip()
    #value = float(value.replace(',', '.'))
    #print(f'{resume(value, 10, 13)}')
