A1 = float(input('число A1: '))
B1 = float(input('число B1: '))
A2 = float(input('число A2: '))
B2 = float(input('число B2: '))
C1 = float(input('число C1: '))
C2 = float(input('число C2: '))
D = A1 * B2 - A2 * B1
x = (C1 * B2 - C2 * B1) / D
y = (A1 * C2 - A2 * C1) / D
print(f'решение: x = {round(x, 2)}, y = {round(y, 2)}')