A = float(input('число: '))
B = float(input('число: '))
if A != 0:
    x = -B / A
    print(f'решение уравнения {A}x + {B} = 0 : x = {round(x, 2)}')
else:
    print("неправильно, A не равно 0")