p = 3.14
a = float(input("число: "))
if a <= 0 or a >= 360:
    print("неправильно, a должно быть [0, 360]")
else:
    R = p * a / 180
    print(f"R = {R}")