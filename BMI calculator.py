w = float(input('Digit your weight: ').strip())
h = float(input('Digit your height: ').strip())
ca = w / (h ** 2)
print('{:.1f}'.format(ca))
if ca < 18.5:
    print('\033[31mUnderweight\033[m')
elif ca < 24.9:
    print('\033[32mNormal weight\033[m')
elif ca < 29.9:
    print('\033[31mOverweight\033[m')
elif ca < 34.9:
    print('\033[31mObesity (Class I)')
elif ca < 39:
    print('\033[31mObesity (Class II)\033[m')
else:
    print('\03[31mExtreme Obesity')
