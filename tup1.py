tup = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
       'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
       'Nineteen', 'Twenty')
n = int(input('Digit a number: '))
while n < 0 or n > 20:
    n = int(input('\033[31mThe value must be between 0 and 20: \033[m'))
print(f'You entered the number: \033[34m{tup[n]}\033[m')
